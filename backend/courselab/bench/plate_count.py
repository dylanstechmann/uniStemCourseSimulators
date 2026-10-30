"""Decimal dilutions and the conventional aerobic plate count (pour plates)."""

from __future__ import annotations

import math
import random

from .engine import ActionRejected, Event, ProtocolModel, coach

BLANKS = ("B1", "B2", "B3", "B4", "B5", "B6")


def poisson(rng: random.Random, mean: float) -> int:
    if mean <= 0:
        return 0
    if mean > 500:
        return max(0, round(rng.gauss(mean, math.sqrt(mean))))
    limit, k, product = math.exp(-mean), 0, rng.random()
    while product > limit:
        k += 1
        product *= rng.random()
    return k


def bam_round(value: float) -> int:
    """Two significant figures with the third-digit rule written in BAM Chapter 3, section 3."""
    if value <= 0:
        return 0
    exponent = int(math.floor(math.log10(value)))
    if exponent < 2:
        return int(round(value))
    three = int(math.floor(value / 10 ** (exponent - 2) + 1e-9))
    first_two, third = divmod(three, 10)
    if third >= 6 or (third == 5 and first_two % 2 == 1):
        first_two += 1
    return first_two * 10 ** (exponent - 1)


class AerobicPlateCount(ProtocolModel):
    protocol_id = "decimal-dilution-aerobic-plate-count"

    def checkpoint_ids(self):
        return [
            "decimal-dilutions", "separate-pipets", "shake-before-sampling", "reshake-after-standing",
            "plate-volume", "duplicate-plates", "agar-temperature", "agar-volume", "agar-within-window",
            "controls", "mix-and-solidify", "incubation", "report-apc", "report-flags",
        ]

    def start(self, rng):
        p = self.parameters
        log_cfu = rng.uniform(3.6, 6.4)
        contaminated = rng.random() < p["diluent_contamination_probability"]
        diluent_cfu_ml = rng.uniform(2.0, 6.0) if contaminated else 0.0
        bottles = {"H": {"label": "Homogenate (10⁻¹)", "volume": 450.0, "nominal_volume": 450.0,
                         "target": 10 ** log_cfu * 0.1, "contam": 0.0, "factor": 0.1,
                         "shaken_at": 0.0, "shake_ok": True, "received": True}}
        for name in BLANKS:
            volume = rng.uniform(89.0, 91.0)
            bottles[name] = {"label": f"Dilution blank {name}", "volume": volume, "nominal_volume": 90.0,
                             "target": 0.0, "contam": diluent_cfu_ml, "factor": 0.0,
                             "shaken_at": None, "shake_ok": False, "received": False}
        return {
            "hidden": {"log_cfu_per_g": log_cfu, "diluent_cfu_ml": diluent_cfu_ml, "window_factor": None},
            "bottles": bottles, "plates": [], "transfers": [], "samplings": [],
            "pipet_last": None, "pipet_reuses": 0, "incubation": None, "counted": False,
            "report": None, "inverted_early": False,
        }

    # Helpers -------------------------------------------------------------------

    def _draw(self, state, rng, events, name, volume, fresh_pipet):
        """Remove a sample from a bottle; return its (target, contaminant) cells and nominal sample grams."""
        p = self.parameters
        bottle = state["bottles"].get(name)
        if bottle is None:
            raise ActionRejected(f"There is no bottle {name}")
        if volume > bottle["volume"]:
            raise ActionRejected(f"{name} holds only {bottle['volume']:.0f} mL")
        if not bottle["received"]:
            coach(state, events, f"{name} is still plain diluent.")
        mixed = bottle["shaken_at"] is not None and bottle["shake_ok"]
        stood = None if bottle["shaken_at"] is None else state["clock"] - bottle["shaken_at"]
        state["samplings"].append({"bottle": name, "shaken": mixed,
                                   "stood_too_long": stood is not None and stood > p["reshake_after_min"]})
        factor = 1.0
        if not mixed:
            factor = math.exp(rng.gauss(-0.3, 0.35))
            coach(state, events, f"{name} was not shaken properly since liquid was last added, so cells "
                                 "are unevenly distributed.")
        elif stood > p["reshake_after_min"]:
            factor = math.exp(rng.gauss(-0.1, 0.15))
            coach(state, events, f"{name} stood {stood:.1f} min after shaking; reshake it if it stands "
                                 f"more than {p['reshake_after_min']:g} min.")
        target = bottle["target"] * volume * factor
        contam = bottle["contam"] * volume
        if not fresh_pipet and state["pipet_last"] not in (None, name):
            previous = state["bottles"][state["pipet_last"]]
            carry = p["carryover_ml"]
            target += previous["target"] * carry
            contam += previous["contam"] * carry
            state["pipet_reuses"] += 1
            coach(state, events, f"The pipet still carries liquid from {state['pipet_last']}; use a "
                                 "separate sterile pipet for each transfer.")
        elif not fresh_pipet and state["pipet_last"] is not None:
            state["pipet_reuses"] += 1
            coach(state, events, "Use a separate sterile pipet for each transfer and plate.")
        state["pipet_last"] = name
        bottle["volume"] -= volume
        grams = bottle["factor"] * volume
        return target, contam, grams

    # Actions -------------------------------------------------------------------

    def act_shake(self, state, rng, bottle, times, arc_cm, seconds):
        p = self.parameters
        if bottle not in state["bottles"]:
            raise ActionRejected(f"There is no bottle {bottle}")
        item = state["bottles"][bottle]
        ok = times >= p["shake_times"] and arc_cm >= p["shake_arc_cm"] and seconds <= p["shake_max_seconds"]
        item["shaken_at"] = state["clock"] + seconds / 60
        item["shake_ok"] = ok
        state["clock"] += seconds / 60
        events = [Event("info", f"{bottle} shaken {times} times through about {arc_cm:g} cm in {seconds:g} s.")]
        if not ok:
            coach(state, events, f"Shake {p['shake_times']} times in a {p['shake_arc_cm']:g} cm arc within "
                                 f"{p['shake_max_seconds']:g} s.")
        return events

    def act_transfer(self, state, rng, source, destination, volume_ml, fresh_pipet):
        if destination == source or destination not in state["bottles"]:
            raise ActionRejected("Choose a different destination bottle")
        if destination == "H":
            raise ActionRejected("Do not add liquid back into the homogenate")
        events = []
        target, contam, grams = self._draw(state, rng, events, source, volume_ml, fresh_pipet)
        dest = state["bottles"][destination]
        total = dest["volume"] + volume_ml
        nominal_total = dest["nominal_volume"] + volume_ml
        dest["target"] = (dest["target"] * dest["volume"] + target) / total
        dest["contam"] = (dest["contam"] * dest["volume"] + contam) / total
        dest["factor"] = (dest["factor"] * dest["nominal_volume"] + grams) / nominal_total
        dest["volume"], dest["nominal_volume"] = total, nominal_total
        dest["received"], dest["shaken_at"], dest["shake_ok"] = True, None, False
        state["transfers"].append({"source": source, "destination": destination, "volume": volume_ml,
                                   "decimal": abs(volume_ml - 10) < 1e-9 and abs(nominal_total - 100) < 1e-9})
        state["clock"] += 0.5
        events.insert(0, Event("info", f"{volume_ml:g} mL moved from {source} to {destination}."))
        return events

    def act_plate(self, state, rng, bottle, volume_ml, fresh_pipet):
        if state["incubation"] is not None:
            raise ActionRejected("Plates are already incubating")
        events = []
        target, contam, grams = self._draw(state, rng, events, bottle, volume_ml, fresh_pipet)
        plate_id = f"P{len(state['plates']) + 1}"
        state["plates"].append({"id": plate_id, "kind": "sample", "bottle": bottle, "volume": volume_ml,
                                "grams": grams, "target": target, "contam": contam, "agar": None,
                                "mixed": False, "count": None})
        state["clock"] += 0.3
        events.insert(0, Event("info", f"{volume_ml:g} mL from {bottle} pipetted into plate {plate_id}."))
        return events

    def act_add_control(self, state, rng, kind):
        if state["incubation"] is not None:
            raise ActionRejected("Plates are already incubating")
        plate_id = f"P{len(state['plates']) + 1}"
        contam = state["hidden"]["diluent_cfu_ml"] if kind == "diluent" else 0.0
        state["plates"].append({"id": plate_id, "kind": f"{kind}-control", "bottle": None, "volume": 1.0,
                                "grams": 0.0, "target": 0.0, "contam": contam, "agar": None,
                                "mixed": False, "count": None})
        state["clock"] += 0.3
        text = "1 mL of sterile diluent" if kind == "diluent" else "no inoculum"
        return [Event("info", f"Control plate {plate_id} prepared with {text}.")]

    def act_pour_agar(self, state, rng, volume_ml, temperature_c):
        p = self.parameters
        waiting = [plate for plate in state["plates"] if plate["agar"] is None]
        if not waiting:
            raise ActionRejected("No plates are waiting for agar")
        events = [Event("info", f"{volume_ml:g} mL of plate count agar at {temperature_c:g} °C poured into "
                                f"{len(waiting)} plate(s).")]
        low, high = p["agar_temperature_c"]
        if temperature_c > high:
            coach(state, events, "Agar above 46 °C injures or kills heat-sensitive cells.")
        elif temperature_c < low:
            coach(state, events, "Agar below 44 °C begins to set and will not mix evenly.")
        if state["clock"] > p["agar_within_min"]:
            coach(state, events, f"More than {p['agar_within_min']:g} min have passed since the original "
                                 "dilution; cells in diluent may have multiplied or died.")
        for plate in waiting:
            plate["agar"] = {"volume": volume_ml, "temperature": temperature_c, "clock": state["clock"]}
        state["clock"] += 0.3 * len(waiting)
        return events

    def act_mix_plates(self, state, rng):
        poured = [plate for plate in state["plates"] if plate["agar"] is not None and not plate["mixed"]]
        if not poured:
            raise ActionRejected("There are no freshly poured plates to mix")
        for plate in poured:
            plate["mixed"] = True
            plate["agar"]["mixed_at"] = state["clock"]
        state["clock"] += 0.2 * len(poured)
        return [Event("info", f"{len(poured)} plate(s) mixed by alternate rotation and back-and-forth motion.")]

    def act_wait(self, state, rng, minutes):
        state["clock"] += minutes
        return [Event("info", f"{minutes:g} min pass.")]

    def act_incubate(self, state, rng, temperature_c, hours, inverted):
        p = self.parameters
        if not state["plates"]:
            raise ActionRejected("There are no plates to incubate")
        if any(plate["agar"] is None for plate in state["plates"]):
            raise ActionRejected("Every plate needs agar before incubation")
        if state["incubation"] is not None:
            raise ActionRejected("The plates have already been incubated")
        events = []
        solid = all(state["clock"] - plate["agar"]["clock"] >= p["solidify_min"] for plate in state["plates"])
        if inverted and not solid:
            state["inverted_early"] = True
            coach(state, events, "The agar had not solidified; inverting it now can slide or tear it.")
        state["incubation"] = {"temperature": temperature_c, "hours": hours, "inverted": inverted, "solid": solid}
        state["clock"] += hours * 60
        events.insert(0, Event("info", f"Plates incubated {'inverted' if inverted else 'upright'} at "
                                       f"{temperature_c:g} °C for {hours:g} h."))
        self._grow(state, rng)
        return events

    def _grow(self, state, rng):
        p = self.parameters
        incubation = state["incubation"]
        t_low, t_high = p["incubation_temperature_c"]
        h_low, h_high = p["incubation_hours"]
        growth = 1.0
        if not t_low <= incubation["temperature"] <= t_high:
            growth *= max(0.2, 1 - 0.12 * abs(incubation["temperature"] - 35))
        if incubation["hours"] < h_low:
            growth *= (incubation["hours"] / 48) ** 1.5
        hidden = state["hidden"]
        for plate in state["plates"]:
            agar = plate["agar"]
            survival = 1.0
            if agar["temperature"] > p["agar_temperature_c"][1]:
                survival = math.exp(-0.25 * (agar["temperature"] - 46))
            if agar["clock"] > p["agar_within_min"]:
                if hidden["window_factor"] is None:
                    hidden["window_factor"] = rng.uniform(0.7, 1.4)
                survival *= hidden["window_factor"]
            if not plate["mixed"]:
                survival *= 0.85
            count = poisson(rng, plate["target"] * survival * growth) + poisson(rng, plate["contam"] * growth)
            plate["count"] = count
            plate["spreaders"] = (not incubation["inverted"]) and rng.random() < 0.5
            plate["damaged"] = state["inverted_early"] and rng.random() < 0.3

    def act_count_plates(self, state, rng):
        if state["incubation"] is None:
            raise ActionRejected("Incubate the plates before counting")
        state["counted"] = True
        state["clock"] += 2 * len(state["plates"])
        return [Event("readout", "Colonies counted on every plate.", {
            plate["id"]: self._shown(plate) for plate in state["plates"]})]

    def _shown(self, plate):
        if plate.get("damaged"):
            return "agar torn"
        if plate["count"] > self.parameters["tntc_display_above"]:
            return "TNTC"
        return plate["count"]

    def act_submit_result(self, state, rng, apc_cfu_per_g, estimated, laboratory_accident):
        if not state["counted"]:
            raise ActionRejected("Count the plates before reporting")
        state["report"] = {"apc": apc_cfu_per_g, "estimated": estimated, "accident": laboratory_accident}
        state["finished"] = True
        return [Event("info", "The aerobic plate count is reported.")]

    # Views and evaluation ------------------------------------------------------

    def visible(self, state):
        clock = state["clock"]
        bottles = []
        for name, item in state["bottles"].items():
            if item["shaken_at"] is None:
                shake = "not shaken since last addition"
            else:
                shake = f"last shaken {max(0.0, clock - item['shaken_at']):.1f} min ago"
            contents = item["label"] if not item["received"] or name == "H" else f"{name}, mixed"
            bottles.append([name, f"{contents}; about {item['volume']:.0f} mL; {shake}"])
        panels = [
            {"title": "Clock", "rows": [["Minutes since the original dilution", f"{clock:.1f}"]]},
            {"title": "Bottles", "rows": bottles},
        ]
        if state["transfers"]:
            panels.append({"title": "Transfers", "rows": [
                [f"{i + 1}", f"{t['volume']:g} mL {t['source']} → {t['destination']}"]
                for i, t in enumerate(state["transfers"])]})
        if state["plates"]:
            rows = []
            for plate in state["plates"]:
                source = plate["kind"] if plate["kind"] != "sample" else f"{plate['volume']:g} mL of {plate['bottle']}"
                agar = "no agar" if plate["agar"] is None else f"agar {plate['agar']['volume']:g} mL"
                result = "" if not state["counted"] else f"; count {self._shown(plate)}"
                if state["counted"] and plate.get("spreaders"):
                    result += " (spreading growth)"
                rows.append([plate["id"], f"{source}; {agar}{result}"])
            panels.append({"title": "Plates", "rows": rows})
        return panels

    def expected(self, state):
        p = self.parameters
        low, high = p["countable_range"]
        diluent_positive = any(plate["kind"] == "diluent-control" and plate["count"] for plate in state["plates"])
        usable = [plate for plate in state["plates"] if plate["kind"] == "sample" and not plate.get("damaged")]
        countable = [plate for plate in usable if low <= plate["count"] <= high and plate["grams"] > 0]
        if countable:
            value = sum(plate["count"] for plate in countable) / sum(plate["grams"] for plate in countable)
            return {"apc": bam_round(value), "raw": value, "estimated": False, "accident": diluent_positive,
                    "plates": [plate["id"] for plate in countable]}
        return {"apc": None, "raw": None, "estimated": True, "accident": diluent_positive, "plates": []}

    def evaluate(self, state):
        p = self.parameters
        results = {}
        transfers = state["transfers"]
        results["decimal-dilutions"] = (bool(transfers) and all(t["decimal"] for t in transfers),
                                        "Each step should move 10 mL into a 90 mL blank, a tenfold dilution.")
        results["separate-pipets"] = (state["pipet_reuses"] == 0,
                                      f"A pipet was reused {state['pipet_reuses']} time(s)." if state["pipet_reuses"]
                                      else "A separate sterile pipet was used for every transfer and plate.")
        samplings = state["samplings"]
        unshaken = [s["bottle"] for s in samplings if not s["shaken"]]
        results["shake-before-sampling"] = (bool(samplings) and not unshaken,
                                            "Every bottle was shaken before sampling." if not unshaken
                                            else f"Sampled without a proper shake: {', '.join(unshaken)}.")
        stood = [s["bottle"] for s in samplings if s["shaken"] and s["stood_too_long"]]
        results["reshake-after-standing"] = (not stood, "No bottle stood more than 3 min before sampling."
                                             if not stood else f"Sampled after standing: {', '.join(stood)}.")
        samples = [plate for plate in state["plates"] if plate["kind"] == "sample"]
        results["plate-volume"] = (bool(samples) and all(plate["volume"] == p["plate_volume_ml"] for plate in samples),
                                   f"Plate {p['plate_volume_ml']:g} mL of each dilution.")
        per_bottle: dict[str, int] = {}
        for plate in samples:
            per_bottle[plate["bottle"]] = per_bottle.get(plate["bottle"], 0) + 1
        single = [name for name, n in per_bottle.items() if n < 2]
        results["duplicate-plates"] = (bool(samples) and not single,
                                       "Every plated dilution has duplicate plates." if samples and not single
                                       else f"Single plates only for: {', '.join(single) or 'no plates poured'}.")
        poured = [plate["agar"] for plate in state["plates"] if plate["agar"] is not None]
        low, high = p["agar_temperature_c"]
        results["agar-temperature"] = (bool(poured) and all(low <= a["temperature"] <= high for a in poured),
                                       f"Agar temperatures used: {sorted({a['temperature'] for a in poured})} °C.")
        v_low, v_high = p["agar_volume_ml"]
        results["agar-volume"] = (bool(poured) and all(v_low <= a["volume"] <= v_high for a in poured),
                                  f"Agar volumes used: {sorted({a['volume'] for a in poured})} mL.")
        late = [a for a in poured if a["clock"] > p["agar_within_min"]]
        results["agar-within-window"] = (bool(poured) and not late,
                                         f"Last agar added at {max((a['clock'] for a in poured), default=0):.1f} min "
                                         "after the original dilution.")
        kinds = {plate["kind"] for plate in state["plates"]}
        results["controls"] = ({"agar-control", "diluent-control"} <= kinds,
                               "Agar and dilution-water control plates were poured."
                               if {"agar-control", "diluent-control"} <= kinds
                               else "Without both controls a contaminated agar or diluent cannot be detected.")
        results["mix-and-solidify"] = (
            bool(state["plates"]) and all(plate["mixed"] for plate in state["plates"])
            and state["incubation"] is not None and state["incubation"]["solid"],
            "Plates should be mixed at once and left to solidify before they are inverted.")
        inc = state["incubation"]
        t_low, t_high = p["incubation_temperature_c"]
        h_low, h_high = p["incubation_hours"]
        ok = inc is not None and inc["inverted"] and t_low <= inc["temperature"] <= t_high and h_low <= inc["hours"] <= h_high
        results["incubation"] = (ok, "Incubate inverted for 48 ± 2 h at 35 °C." if inc is None else
                                 f"Incubated {'inverted' if inc['inverted'] else 'upright'} at {inc['temperature']:g} °C "
                                 f"for {inc['hours']:g} h.")
        report = state["report"]
        expected = self.expected(state) if state["counted"] else None
        if report is None or expected is None:
            results["report-apc"] = (False, "No result was reported.")
            results["report-flags"] = (False, "No result was reported.")
            return results
        if expected["apc"] is None:
            results["report-apc"] = (None, "No plate fell in the countable range, so only an estimated count "
                                           "could be reported.")
        else:
            results["report-apc"] = (
                round(report["apc"]) == expected["apc"],
                f"Countable plates {', '.join(expected['plates'])}: total colonies ÷ total grams of sample plated "
                f"= {expected['raw']:.0f} CFU/g, reported to two significant figures as {expected['apc']:,} CFU/g; "
                f"you reported {report['apc']:,.0f}.")
        flags_ok = report["estimated"] == expected["estimated"] and report["accident"] == expected["accident"]
        results["report-flags"] = (
            flags_ok,
            f"Estimated count: {'yes' if expected['estimated'] else 'no'}; laboratory accident (a positive "
            f"diluent control): {'yes' if expected['accident'] else 'no'}.")
        return results

    def reveal(self, state):
        hidden = state["hidden"]
        notes = [f"The sample held about {10 ** hidden['log_cfu_per_g']:,.0f} CFU/g."]
        if hidden["diluent_cfu_ml"]:
            notes.append(f"The diluent was contaminated at about {hidden['diluent_cfu_ml']:.1f} CFU/mL; only a "
                         "dilution-water control plate reveals this.")
        else:
            notes.append("The diluent and agar were sterile in this run.")
        return notes
