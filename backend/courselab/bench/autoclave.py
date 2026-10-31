"""Validating a steam-autoclave cycle for a typical biohazardous waste load."""

from __future__ import annotations

from .engine import ActionRejected, Event, ProtocolModel, coach

POSITIONS = ("centre", "top", "drain")


class AutoclaveValidation(ProtocolModel):
    protocol_id = "autoclave-waste-load-validation"

    def checkpoint_ids(self):
        return ["bag-loosely-closed", "leak-proof-tray", "within-capacity", "thermocouple-at-centre", "bi-at-centre",
                "positive-control", "exposure-sufficient", "bi-incubation", "cycle-record", "report-lag", "report-verdict",
                "report-cycle-time"]

    def start(self, rng):
        p = self.parameters
        return {
            "hidden": {"d_value": round(rng.uniform(*p["d_value_range_min"]), 2),
                       "lag_per_kg": round(rng.uniform(*p["lag_per_kg_range_min"]), 2)},
            "load": None, "probes": {}, "bis": {}, "control_bi": False, "cycle": None, "results": None,
            "bi_incubation": None, "bi_read": None, "report": None,
        }

    # Actions -------------------------------------------------------------------

    def act_prepare_load(self, state, rng, mass_kg, bag_closure, water_added, in_tray):
        if state["cycle"] is not None:
            raise ActionRejected("The load has already been run")
        state["load"] = {"mass": mass_kg, "closure": bag_closure, "water": water_added, "tray": in_tray}
        events = [Event("info", f"A {mass_kg:g} kg waste load is bagged ({bag_closure.replace('_', ' ')}), "
                                f"{'with' if water_added else 'without'} added water, {'in a leak-proof tray' if in_tray else 'directly on the chamber shelf'}.")]
        if bag_closure == "tightly_sealed":
            coach(state, events, "A tightly sealed bag traps air and keeps steam out; close it loosely.")
        if not in_tray:
            coach(state, events, "Carry and autoclave bags in a leak-proof tray or pan.")
        if mass_kg > self.parameters["chamber_capacity_kg"]:
            coach(state, events, "The load exceeds the chamber's rated capacity; overloading blocks steam circulation.")
        state["clock"] += 5
        return events

    def act_place_thermocouple(self, state, rng, position):
        if state["load"] is None:
            raise ActionRejected("Prepare the load first")
        state["probes"][position] = True
        return [Event("info", f"A thermocouple is placed at the {position} of the load.")]

    def act_place_bi(self, state, rng, position):
        if state["load"] is None:
            raise ActionRejected("Prepare the load first")
        state["bis"][position] = True
        return [Event("info", f"A biological indicator (10⁶ Geobacillus stearothermophilus spores) is placed at the {position} of the load.")]

    def act_keep_control_bi(self, state, rng):
        state["control_bi"] = True
        return [Event("info", "One indicator from the same lot is kept aside, unprocessed, as the positive control.")]

    def act_run_cycle(self, state, rng, temperature_c, exposure_min):
        p = self.parameters
        if state["load"] is None:
            raise ActionRejected("Prepare the load first")
        if state["cycle"] is not None:
            raise ActionRejected("The cycle has already been run")
        load, hidden = state["load"], state["hidden"]
        lag = {"chamber": 0.0}
        base = hidden["lag_per_kg"] * load["mass"] * (0.8 if load["water"] else 1.0)
        if load["mass"] > p["chamber_capacity_kg"]:
            base *= 1.6
        for position, factor in (("centre", 1.0), ("top", 0.45), ("drain", 0.3)):
            lag[position] = round(base * factor, 1)
        penetrates = load["closure"] == "loosely_closed"
        reached = {}
        for position, value in lag.items():
            if position != "chamber" and not penetrates and position == "centre":
                reached[position] = None  # air pocket: the centre never reaches the set temperature
            else:
                reached[position] = value if value < exposure_min or position == "chamber" else None
        state["cycle"] = {"temperature": temperature_c, "exposure": exposure_min, "lag": lag, "reached": reached,
                          "penetrates": penetrates}
        state["clock"] += exposure_min + 20
        rows = {}
        for position in ("chamber",) + POSITIONS:
            if position != "chamber" and position not in state["probes"]:
                continue
            r = reached[position]
            rows[position] = "never reached the set temperature" if r is None else f"reached {temperature_c:g} °C after {r:g} min"
        events = [Event("readout", f"Cycle complete: {temperature_c:g} °C for {exposure_min:g} min. Thermocouples: "
                                   + "; ".join(f"{k} {v}" for k, v in rows.items()) + ".", {"thermocouples": rows})]
        if not penetrates and "centre" in state["probes"]:
            events.append(Event("consequence", "The centre thermocouple plateaued near 100 °C: air was trapped in the sealed bag."))
        return events

    def _survives(self, state, position):
        p, cycle, hidden = self.parameters, state["cycle"], state["hidden"]
        if cycle["temperature"] < p["set_temperature_c"]:
            return True
        reached = cycle["reached"][position]
        if reached is None:
            return True
        time_at_temp = cycle["exposure"] - reached
        log_reduction = time_at_temp / hidden["d_value"]
        survivors = p["bi_population"] * 10 ** (-log_reduction)
        return survivors >= 0.5  # an expected half spore or more counts as growth in this simple model

    def act_incubate_bis(self, state, rng, temperature_c, hours):
        if state["cycle"] is None:
            raise ActionRejected("Run the cycle first")
        state["bi_incubation"] = {"temperature": temperature_c, "hours": hours}
        state["clock"] += hours * 60
        return [Event("info", f"Indicators incubated at {temperature_c:g} °C for {hours:g} h.")]

    def act_read_bis(self, state, rng):
        p = self.parameters
        inc = state["bi_incubation"]
        if inc is None:
            raise ActionRejected("Incubate the indicators first")
        ok_incubation = (p["bi_incubation_c"][0] <= inc["temperature"] <= p["bi_incubation_c"][1]
                         and inc["hours"] >= p["bi_incubation_h"])
        results = {}
        for position in state["bis"]:
            grew = self._survives(state, position) if ok_incubation else False
            results[position] = "growth" if grew else "no growth"
        if state["control_bi"]:
            results["control"] = "growth" if ok_incubation else "no growth"
        state["bi_read"] = results
        return [Event("readout", "Indicator results: " + "; ".join(f"{k} {v}" for k, v in results.items()) + ".", results)]

    def act_record_cycle(self, state, rng):
        if state["cycle"] is None:
            raise ActionRejected("Run the cycle first")
        state["cycle"]["recorded"] = True
        return [Event("info", "Cycle time, temperature and pressure are recorded in the autoclave log with the load description.")]

    def act_submit_report(self, state, rng, centre_lag_min, verdict, validated_exposure_min):
        if state["bi_read"] is None:
            raise ActionRejected("Read the indicators before reporting")
        state["report"] = {"lag": centre_lag_min, "verdict": verdict, "exposure": validated_exposure_min}
        state["finished"] = True
        return [Event("info", "The validation report is submitted.")]

    # Views and evaluation ------------------------------------------------------

    def visible(self, state):
        load = state["load"]
        rows = [["Load", "not prepared" if load is None else
                 f"{load['mass']:g} kg, bag {load['closure'].replace('_', ' ')}, {'water added' if load['water'] else 'no water'}, "
                 f"{'in tray' if load['tray'] else 'no tray'}"],
                ["Thermocouples", ", ".join(state["probes"]) or "none"],
                ["Biological indicators", ", ".join(state["bis"]) or "none"],
                ["Positive control kept", "yes" if state["control_bi"] else "no"]]
        if state["bis"]:
            rows.append(["Indicator lot label", f"10⁶ spores, D₁₂₁ = {state['hidden']['d_value']:g} min"])
        panels = [{"title": "Validation set-up", "rows": rows}]
        if state["cycle"]:
            c = state["cycle"]
            panels.append({"title": "Cycle", "rows": [["Set point", f"{c['temperature']:g} °C"], ["Exposure", f"{c['exposure']:g} min"]]})
        if state["bi_read"]:
            panels.append({"title": "Indicator results", "rows": [[k, v] for k, v in state["bi_read"].items()]})
        return panels

    def evaluate(self, state):
        p = self.parameters
        load, cycle, report, hidden = state["load"], state["cycle"], state["report"], state["hidden"]
        r = {}
        r["bag-loosely-closed"] = (bool(load) and load["closure"] == "loosely_closed", "Bags are closed loosely so steam can enter.")
        r["leak-proof-tray"] = (bool(load) and load["tray"], "Waste is autoclaved in a leak-proof tray or pan.")
        r["within-capacity"] = (bool(load) and load["mass"] <= p["chamber_capacity_kg"],
                                f"Load {load['mass'] if load else 0:g} kg against a rated capacity of {p['chamber_capacity_kg']:g} kg.")
        r["thermocouple-at-centre"] = ("centre" in state["probes"], "The slowest-heating point, the centre, needs a thermocouple.")
        r["bi-at-centre"] = ("centre" in state["bis"], "An indicator at the centre tests the hardest place to sterilize.")
        r["positive-control"] = (state["control_bi"], "An unprocessed indicator from the same lot must grow, or negative results mean nothing.")
        if cycle:
            lag = cycle["lag"]["centre"]
            needed = lag + p["required_log_reduction"] * hidden["d_value"]
            enough = cycle["penetrates"] and cycle["temperature"] >= p["set_temperature_c"] and cycle["exposure"] >= needed
            r["exposure-sufficient"] = (enough, f"With a centre lag of {lag:g} min and D₁₂₁ = {hidden['d_value']:g} min, twelve log reductions need "
                                                f"at least {needed:.1f} min; the cycle ran {cycle['exposure']:g} min.")
            r["cycle-record"] = (bool(cycle.get("recorded")), "Each cycle's time, temperature and pressure are recorded.")
        else:
            r["exposure-sufficient"] = (False, "No cycle was run.")
            r["cycle-record"] = (False, "No cycle was run.")
        inc = state["bi_incubation"]
        r["bi-incubation"] = (bool(inc) and p["bi_incubation_c"][0] <= inc["temperature"] <= p["bi_incubation_c"][1]
                              and inc["hours"] >= p["bi_incubation_h"],
                              f"Incubate steam indicators at {p['bi_incubation_c'][0]:g}–{p['bi_incubation_c'][1]:g} °C for at least {p['bi_incubation_h']:g} h.")
        if report is None or cycle is None:
            for key in ("report-lag", "report-verdict", "report-cycle-time"):
                r[key] = (False, "No report was submitted.")
            return r
        true_lag = cycle["lag"]["centre"]
        observed = cycle["reached"]["centre"] if "centre" in state["probes"] else None
        r["report-lag"] = ((observed is not None and abs(report["lag"] - observed) <= 0.5) if "centre" in state["probes"] else False,
                           f"The centre thermocouple reached temperature after {true_lag:g} min." if observed is not None
                           else "The centre lag was not measured or never reached temperature.")
        results = state["bi_read"]
        valid = state["control_bi"] and results.get("control") == "growth" and "centre" in results
        expected = "pass" if valid and all(v == "no growth" for k, v in results.items() if k != "control") else "fail"
        r["report-verdict"] = (report["verdict"] == expected,
                               f"With these indicator and control results the cycle should be reported as '{expected}'.")
        if observed is None:
            r["report-cycle-time"] = (None, "No validated time can be set until steam reaches the centre.")
        else:
            needed = observed + p["required_log_reduction"] * hidden["d_value"]
            r["report-cycle-time"] = (report["exposure"] >= needed,
                                      f"A validated exposure must be at least the lag plus twelve D-values, {needed:.1f} min.")
        return r

    def reveal(self, state):
        h = state["hidden"]
        return [f"The indicator lot had D₁₂₁ = {h['d_value']:g} min; heating lag was {h['lag_per_kg']:g} min per kg at the centre before adjustments."]
