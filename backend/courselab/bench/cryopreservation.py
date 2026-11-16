"""Deterministic synthetic DMSO freeze, storage, thaw and recount practice.

The model checks action order, conservation and learner-entered recovery arithmetic.
Its viability multipliers are teaching transformations, not cryobiological kinetics,
physical validation, a quality-control release rule or a future-growth prediction.
"""

from __future__ import annotations

import copy
import json
import math

from .engine import ActionRejected, Event, ProtocolModel, coach


class CryopreservationRun(ProtocolModel):
    protocol_id = "freeze-and-thaw-with-viability-outcomes"

    def checkpoint_ids(self):
        return [
            "harvest-and-count", "freeze-medium-composition", "cold-dropwise-dmso",
            "aliquot-conservation", "controlled-cooling", "vapour-phase-storage",
            "location-record", "fast-thaw", "post-thaw-dilution", "dmso-removal",
            "recount-arithmetic", "post-thaw-viability", "quarantine-pending-qc",
            "bank-tier-forward-link", "structured-result",
        ]

    def start(self, rng):
        return {
            "hidden": {
                "baseline_post_thaw_viability_pct": rng.choice(
                    self.parameters["baseline_post_thaw_viability_choices_pct"]
                ),
            },
            "harvest": None,
            "freeze_medium": None,
            "dmso_addition": None,
            "aliquot": None,
            "cooling": None,
            "storage": None,
            "location": None,
            "thaw": None,
            "dilution": None,
            "removal": None,
            "recount": None,
            "quarantine": None,
            "result": None,
        }

    @staticmethod
    def _once(state, key, message):
        if state[key] is not None:
            raise ActionRejected(message)

    @staticmethod
    def _format_number(value, significant=7):
        """Readable fixed/scientific display without raw exponent notation."""
        if isinstance(value, int) and not isinstance(value, bool):
            return f"{value:,}"
        value = float(value)
        if value == 0:
            return "0"
        magnitude = abs(value)
        if magnitude < 0.0001:
            coefficient, exponent = f"{value:.{significant}g}".split("e")
            coefficient = coefficient.rstrip("0").rstrip(".")
            superscript = str(int(exponent)).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
            return f"{coefficient} × 10{superscript}"
        if magnitude >= 10000:
            return f"{value:,.0f}"
        decimals = max(0, significant - 1 - math.floor(math.log10(magnitude)))
        return f"{value:,.{decimals}f}".rstrip("0").rstrip(".")

    @classmethod
    def _display_data(cls, value):
        """Round direct-render numbers without changing internal full precision."""
        if isinstance(value, dict):
            return {key: cls._display_data(item) for key, item in value.items()}
        if isinstance(value, list):
            return [cls._display_data(item) for item in value]
        if isinstance(value, float):
            rounded = float(f"{value:.7g}")
            if rounded and abs(rounded) < 0.0001:
                return cls._format_number(rounded)
            if rounded.is_integer():
                return int(rounded)
            return rounded
        return value

    def present_view(self, view):
        """Return a sanitized deep presentation copy; never mutate run inputs/views."""
        return self._display_data(copy.deepcopy(view))

    def _medium_ok(self, state):
        p = self.parameters
        item = state["freeze_medium"] or {}
        expected_total = p["vial_count"] * p["volume_per_vial_ml"]
        expected_dmso = expected_total * p["dmso_final_fraction"]
        return bool(item) and (
            math.isclose(item["final_volume_ml"], expected_total)
            and math.isclose(item["dmso_volume_ml"], expected_dmso)
            and math.isclose(item["base_volume_ml"], expected_total - expected_dmso)
            and item["temperature_c"] == p["freeze_medium_temperature_c"]
        )

    def _addition_ok(self, state):
        p = self.parameters
        item = state["dmso_addition"] or {}
        return bool(item) and (
            item["temperature_c"] == p["freeze_medium_temperature_c"]
            and item["addition_method"] == "cold_dropwise"
            and item["elapsed_minutes"] <= p["dmso_addition_max_min"]
        )

    def _aliquot_ok(self, state):
        p = self.parameters
        item = state["aliquot"] or {}
        return bool(item) and (
            item["vial_count"] == p["vial_count"]
            and item["volume_per_vial_ml"] == p["volume_per_vial_ml"]
            and item["viable_cells_per_vial"] == p["viable_cells_per_vial"]
        )

    def _cooling_ok(self, state):
        p = self.parameters
        item = state["cooling"] or {}
        return bool(item) and (
            item["method"] in {"controlled_rate", "passive_container"}
            and abs(item["rate_c_per_min"] - p["cooling_rate_c_per_min"])
            <= p["cooling_rate_tolerance_c_per_min"]
            and item["hold_temperature_c"] == p["passive_hold_temperature_c"]
            and item["hold_hours"] == p["passive_hold_hours"]
        )

    def _thaw_ok(self, state):
        p = self.parameters
        item = state["thaw"] or {}
        return bool(item) and (
            item["temperature_c"] == p["thaw_temperature_c"]
            and item["duration_seconds"] <= p["thaw_max_seconds"]
            and item["endpoint"] == "small_ice_remains"
        )

    def _dilution_ok(self, state):
        p = self.parameters
        item = state["dilution"] or {}
        return bool(item) and (
            item["medium_ml"] == p["post_thaw_medium_ml"]
            and item["addition_method"] == "gradual_with_mixing"
            and item["medium_temperature_c"] == p["thaw_temperature_c"]
        )

    def _removal_ok(self, state):
        p = self.parameters
        item = state["removal"] or {}
        return bool(item) and (
            item["rcf_g"] == p["collection_rcf_g"]
            and item["minutes"] == p["collection_minutes"]
            and item["supernatant_removed"]
            and item["final_volume_ml"] == p["recount_volume_ml"]
        )

    def _viability_factor(self, state):
        p = self.parameters
        factor = 1.0
        if state["dmso_addition"] is not None and not self._addition_ok(state):
            factor *= p["room_temperature_dmso_factor"]
        if state["cooling"] is not None and not self._cooling_ok(state):
            factor *= p["uncontrolled_cooling_factor"]
        if state["thaw"] is not None and not self._thaw_ok(state):
            factor *= p["slow_thaw_factor"]
        if state["dilution"] is not None and not self._dilution_ok(state):
            factor *= p["no_dilution_factor"]
        if (state["removal"] is not None
                and not state["removal"]["supernatant_removed"]):
            factor *= p["dmso_not_removed_factor"]
        return factor

    def _outcome(self, state):
        """Synthetic count-panel values; independent of the learner's recount entry."""
        p = self.parameters
        factor = self._viability_factor(state)
        viability = min(100.0, state["hidden"]["baseline_post_thaw_viability_pct"] * factor)
        initial_viable = p["viable_cells_per_vial"]
        total_cells = initial_viable / (p["harvest_viability_pct"] / 100)
        viable = total_cells * viability / 100
        final_volume = ((state["removal"] or {}).get("final_volume_ml")
                        or p["recount_volume_ml"])
        medium_ml = (state["dilution"] or {}).get("medium_ml", 0)
        initial_volume = p["volume_per_vial_ml"]
        diluted_volume = initial_volume + medium_ml
        diluted_dmso_pct = (100 * p["dmso_final_fraction"] * initial_volume / diluted_volume
                            if diluted_volume else None)
        removed = ((state["removal"] or {}).get("supernatant_removed")
                   if state["removal"] is not None else False)
        remaining_fraction = p["dmso_solute_removal_fraction"] if removed else 0.0
        remaining_solute_fraction = 1 - remaining_fraction
        initial_dmso_ml = initial_volume * p["dmso_final_fraction"]
        residual_dmso_ml = initial_dmso_ml * remaining_solute_fraction
        residual_pct = 100 * residual_dmso_ml / final_volume
        return {
            "viability_multiplier": factor,
            "post_thaw_viability_pct": viability,
            "prefreeze_viable_cells_in_vial": initial_viable,
            "prefreeze_total_cells_in_vial": total_cells,
            "post_thaw_viable_cells_recovered": viable,
            "recount_volume_ml": final_volume,
            "post_thaw_viable_concentration_cells_ml": viable / final_volume,
            "recovery_of_initially_viable_pct": 100 * viable / initial_viable,
            "diluted_volume_ml": diluted_volume,
            "diluted_dmso_pct": diluted_dmso_pct,
            "residual_dmso_ml": residual_dmso_ml,
            "residual_dmso_pct": residual_pct,
        }

    def visible(self, state):
        panels = [{"title": "Synthetic harvest", "rows": [
            ["Material", "generic synthetic non-human mammalian cells"],
            ["Displayed viable concentration", "2.00 × 10⁶ cells/mL"],
            ["Displayed pre-freeze viability", "95.0%"],
            ["Suspension volume", "5.00 mL"],
            ["Harvest/count recorded", "yes" if state["harvest"] else "no"],
        ]}]
        if state["freeze_medium"]:
            item = state["freeze_medium"]
            panels.append({"title": "Freeze medium", "rows": [
                ["Final volume", f"{self._format_number(item['final_volume_ml'])} mL"],
                ["DMSO", f"{self._format_number(item['dmso_volume_ml'])} mL"],
                ["Base medium", f"{self._format_number(item['base_volume_ml'])} mL"],
                ["Preparation temperature", f"{self._format_number(item['temperature_c'])} °C"],
                ["Addition", state["dmso_addition"]["addition_method"]
                 if state["dmso_addition"] else "not yet recorded"],
            ]})
        if state["aliquot"]:
            item = state["aliquot"]
            panels.append({"title": "Cryovials", "rows": [
                ["Vials", str(item["vial_count"])],
                ["Volume per vial", f"{self._format_number(item['volume_per_vial_ml'])} mL"],
                ["Viable target per vial", f"{self._format_number(item['viable_cells_per_vial'])} cells"],
            ]})
        if state["cooling"]:
            item = state["cooling"]
            panels.append({"title": "Cooling and storage", "rows": [
                ["Cooling", f"{item['method']}; {self._format_number(item['rate_c_per_min'])} °C/min"],
                ["Initial hold", f"{self._format_number(item['hold_temperature_c'])} °C for {self._format_number(item['hold_hours'])} h"],
                ["Nitrogen phase", state["storage"]["phase"] if state["storage"] else "not recorded"],
            ]})
        if state["location"]:
            item = state["location"]
            panels.append({"title": "Bank location", "rows": [
                ["Address", f"{item['dewar_id']} / {item['rack_id']} / {item['box_id']} / {item['position_id']}"],
                ["Tier", item["bank_tier"]],
            ]})
        if state["thaw"]:
            item = state["thaw"]
            panels.append({"title": "Thaw and DMSO removal", "rows": [
                ["Thaw", f"{self._format_number(item['temperature_c'])} °C for {self._format_number(item['duration_seconds'])} s; {item['endpoint']}"],
                ["Dilution", f"{self._format_number(state['dilution']['medium_ml'])} mL medium" if state["dilution"] else "not recorded"],
                ["Resuspension", f"{self._format_number(state['removal']['final_volume_ml'])} mL" if state["removal"] else "not recorded"],
            ]})
        if state["removal"]:
            outcome = self._outcome(state)
            panels.append({"title": "Synthetic post-thaw recount panel", "rows": [
                ["Viability", f"{self._format_number(outcome['post_thaw_viability_pct'])}%"],
                ["Viable cells recovered", self._format_number(outcome["post_thaw_viable_cells_recovered"])],
                ["Resuspension volume", f"{self._format_number(outcome['recount_volume_ml'])} mL"],
                ["Recount entered", "yes" if state["recount"] else "no"],
            ]})
        if state["quarantine"]:
            item = state["quarantine"]
            panels.append({"title": "QC and forward record", "rows": [
                ["Disposition", item["disposition"]],
                ["Sterility QC", item["sterility_status"]],
                ["Identity evidence", item["identity_status"]],
                ["Forward record", item["forward_record"]],
            ]})
        return panels

    def act_harvest_and_count(self, state, rng, viable_concentration_cells_ml,
                              viability_pct, suspension_volume_ml):
        self._once(state, "harvest", "The harvest/count has already been recorded")
        state["harvest"] = {
            "viable_concentration_cells_ml": viable_concentration_cells_ml,
            "viability_pct": viability_pct,
            "suspension_volume_ml": suspension_volume_ml,
            "viable_harvest_cells": viable_concentration_cells_ml * suspension_volume_ml,
        }
        state["clock"] += 5
        return [Event("readout", "The pre-freeze harvest/count is recorded.",
                      dict(state["harvest"]))]

    def act_prepare_freeze_medium(self, state, rng, final_volume_ml, dmso_volume_ml,
                                  base_volume_ml, temperature_c):
        if not state["harvest"]:
            raise ActionRejected("Record the harvest/count before preparing freeze medium")
        self._once(state, "freeze_medium", "The freeze medium has already been prepared")
        state["freeze_medium"] = {
            "final_volume_ml": final_volume_ml, "dmso_volume_ml": dmso_volume_ml,
            "base_volume_ml": base_volume_ml, "temperature_c": temperature_c,
        }
        state["clock"] += 2
        events = [Event("info", "The freeze-medium components and temperature are recorded.")]
        if not self._medium_ok(state):
            coach(state, events, "Check final-volume fraction, component conservation and cold handling.")
        return events

    def act_add_dmso(self, state, rng, temperature_c, addition_method, elapsed_minutes):
        if not state["freeze_medium"]:
            raise ActionRejected("Prepare freeze medium before adding DMSO")
        self._once(state, "dmso_addition", "DMSO addition has already been recorded")
        state["dmso_addition"] = {
            "temperature_c": temperature_c, "addition_method": addition_method,
            "elapsed_minutes": elapsed_minutes,
        }
        state["clock"] += elapsed_minutes
        events = [Event("info", f"DMSO addition recorded as {addition_method} at {self._format_number(temperature_c)} °C.")]
        if not self._addition_ok(state):
            coach(state, events, "Use cold, dropwise addition with mixing rather than a warm or abrupt addition.")
        return events

    def act_aliquot_vials(self, state, rng, vial_count, volume_per_vial_ml,
                          viable_cells_per_vial):
        if not state["dmso_addition"]:
            raise ActionRejected("Add DMSO before aliquoting")
        self._once(state, "aliquot", "The vials have already been aliquoted")
        required = vial_count * viable_cells_per_vial
        available = (self.parameters["harvest_viable_concentration_cells_ml"]
                     * self.parameters["harvest_volume_ml"])
        if required > available:
            raise ActionRejected("The aliquot plan needs more viable cells than the displayed harvest contains")
        state["aliquot"] = {
            "vial_count": vial_count, "volume_per_vial_ml": volume_per_vial_ml,
            "viable_cells_per_vial": viable_cells_per_vial,
        }
        state["clock"] += 4
        return [Event("info", f"Aliquoted {vial_count} synthetic cryovials.",
                      {"total_viable_cells_planned": required,
                       "total_volume_ml": vial_count * volume_per_vial_ml})]

    def act_cool_vials(self, state, rng, method, rate_c_per_min,
                       hold_temperature_c, hold_hours):
        if not state["aliquot"]:
            raise ActionRejected("Aliquot the vials before cooling")
        self._once(state, "cooling", "The cooling step has already been recorded")
        state["cooling"] = {
            "method": method, "rate_c_per_min": rate_c_per_min,
            "hold_temperature_c": hold_temperature_c, "hold_hours": hold_hours,
        }
        state["clock"] += hold_hours * 60
        events = [Event("info", f"Cooling recorded by {method} at a nominal {self._format_number(rate_c_per_min)} °C/min.")]
        if not self._cooling_ok(state):
            coach(state, events, "Use a controlled-rate device or passive container at about 1 °C/min and record the overnight hold.")
        return events

    def act_store_vials(self, state, rng, phase, temperature_c):
        if not state["cooling"]:
            raise ActionRejected("Complete initial cooling before nitrogen storage")
        self._once(state, "storage", "Nitrogen storage has already been recorded")
        state["storage"] = {"phase": phase, "temperature_c": temperature_c}
        state["clock"] += 2
        events = [Event("info", f"Vials transferred to {phase}-phase nitrogen storage.")]
        if phase != "vapour":
            coach(state, events, "Use vapour-phase storage for this scenario; liquid immersion introduces additional hazards.")
        return events

    def act_record_location(self, state, rng, dewar_id, rack_id, box_id,
                            position_id, bank_tier):
        if not state["storage"]:
            raise ActionRejected("Select nitrogen storage before recording its location")
        self._once(state, "location", "The storage location has already been recorded")
        state["location"] = {
            "dewar_id": dewar_id, "rack_id": rack_id, "box_id": box_id,
            "position_id": position_id, "bank_tier": bank_tier,
        }
        state["clock"] += 1
        return [Event("info", f"Recorded {dewar_id}/{rack_id}/{box_id}/{position_id} as {bank_tier}.")]

    def act_thaw_vial(self, state, rng, temperature_c, duration_seconds, endpoint):
        if not state["location"]:
            raise ActionRejected("Record the storage location before thawing its vial")
        self._once(state, "thaw", "The vial has already been thawed")
        state["thaw"] = {
            "temperature_c": temperature_c, "duration_seconds": duration_seconds,
            "endpoint": endpoint,
        }
        state["clock"] += duration_seconds / 60
        events = [Event("info", f"Thaw recorded at {self._format_number(temperature_c)} °C for {self._format_number(duration_seconds)} s.")]
        if not self._thaw_ok(state):
            coach(state, events, "Thaw promptly at 37 °C until only a small ice remnant remains; slow thawing is not gentler.")
        return events

    def act_dilute_post_thaw(self, state, rng, medium_ml, addition_method,
                             medium_temperature_c):
        if not state["thaw"]:
            raise ActionRejected("Thaw the vial before post-thaw dilution")
        self._once(state, "dilution", "Post-thaw dilution has already been recorded")
        state["dilution"] = {
            "medium_ml": medium_ml, "addition_method": addition_method,
            "medium_temperature_c": medium_temperature_c,
        }
        state["clock"] += 2
        events = [Event("info", f"Post-thaw dilution with {self._format_number(medium_ml)} mL complete medium recorded.")]
        if not self._dilution_ok(state):
            coach(state, events, "After the rapid thaw, add 9.00 mL prewarmed complete medium gradually with mixing.")
        return events

    def act_remove_dmso(self, state, rng, rcf_g, minutes, supernatant_removed,
                        final_volume_ml):
        if not state["dilution"]:
            raise ActionRejected("Dilute the thawed suspension before DMSO removal")
        self._once(state, "removal", "DMSO removal has already been recorded")
        state["removal"] = {
            "rcf_g": rcf_g, "minutes": minutes,
            "supernatant_removed": supernatant_removed,
            "final_volume_ml": final_volume_ml,
        }
        state["clock"] += minutes + 2
        outcome = self._outcome(state)
        return [Event("readout", "The post-thaw synthetic recount panel is ready.",
                      {"post_thaw_viability_pct": outcome["post_thaw_viability_pct"],
                       "post_thaw_viable_cells_recovered": outcome["post_thaw_viable_cells_recovered"],
                       "recount_volume_ml": final_volume_ml})]

    def act_recount_post_thaw(self, state, rng, viable_cells_recovered,
                              viability_pct, viable_concentration_cells_ml):
        if not state["removal"]:
            raise ActionRejected("Remove DMSO and resuspend before recounting")
        self._once(state, "recount", "The post-thaw recount has already been recorded")
        state["recount"] = {
            "viable_cells_recovered": viable_cells_recovered,
            "viability_pct": viability_pct,
            "viable_concentration_cells_ml": viable_concentration_cells_ml,
        }
        state["clock"] += 4
        return [Event("readout", "The post-thaw viability, recovery and concentration are recorded.")]

    def act_quarantine_stock(self, state, rng, disposition, sterility_status,
                             identity_status, forward_record):
        if not state["recount"]:
            raise ActionRejected("Record the post-thaw recount before stock disposition")
        self._once(state, "quarantine", "The stock disposition has already been recorded")
        state["quarantine"] = {
            "disposition": disposition, "sterility_status": sterility_status,
            "identity_status": identity_status, "forward_record": forward_record,
        }
        state["clock"] += 1
        events = [Event("info", f"Stock disposition recorded as {disposition}; sterility QC {sterility_status}.")]
        if (disposition != "quarantine_pending_qc" or sterility_status != "pending"
                or identity_status != "reference_on_file"):
            coach(state, events, "Keep the stock quarantined; viability is not QC release, and pending identity is not reference-on-file evidence.")
        return events

    def act_finish(self, state, rng):
        if not state["quarantine"]:
            raise ActionRejected("Record quarantine and the bank-tier forward link before finishing")
        state["result"] = self.expected(state)
        state["finished"] = True
        return [Event("readout", "The synthetic freeze–thaw run is complete; no future growth or QC release is predicted.",
                      {"result": state["result"]})]

    def expected(self, state):
        p = self.parameters
        result = {
            "harvest": dict(state["harvest"]) if state["harvest"] else None,
            "freeze_medium": dict(state["freeze_medium"]) if state["freeze_medium"] else None,
            "aliquot": dict(state["aliquot"]) if state["aliquot"] else None,
            "cooling": dict(state["cooling"]) if state["cooling"] else None,
            "storage": dict(state["storage"]) if state["storage"] else None,
            "location": dict(state["location"]) if state["location"] else None,
            "thaw": dict(state["thaw"]) if state["thaw"] else None,
            "dilution": dict(state["dilution"]) if state["dilution"] else None,
            "removal": dict(state["removal"]) if state["removal"] else None,
            "quarantine": dict(state["quarantine"]) if state["quarantine"] else None,
        }
        if state["harvest"]:
            result["expected_viable_harvest_cells"] = (
                p["harvest_viable_concentration_cells_ml"] * p["harvest_volume_ml"]
            )
        if state["aliquot"]:
            result["expected_batch_viable_concentration_cells_ml"] = (
                p["vial_count"] * p["viable_cells_per_vial"]
                / (p["vial_count"] * p["volume_per_vial_ml"])
            )
        if state["removal"]:
            result.update(self._outcome(state))
        if state["recount"]:
            result["entered_recount"] = dict(state["recount"])
        return result

    def evaluate(self, state):
        p = self.parameters
        harvest = state["harvest"] or {}
        harvest_ok = bool(harvest) and (
            harvest["viable_concentration_cells_ml"] == p["harvest_viable_concentration_cells_ml"]
            and harvest["viability_pct"] == p["harvest_viability_pct"]
            and harvest["suspension_volume_ml"] == p["harvest_volume_ml"]
        )
        r = {
            "harvest-and-count": (harvest_ok, "Expected 2.00 × 10⁶ viable cells/mL, 95.0% and 5.00 mL."),
            "freeze-medium-composition": (self._medium_ok(state), "Expected 4.00 mL = 0.400 mL DMSO + 3.60 mL base at 4 °C."),
            "cold-dropwise-dmso": (self._addition_ok(state), "Expected cold_dropwise at 4 °C within 5 min."),
            "aliquot-conservation": (self._aliquot_ok(state), "Expected four 1.00 mL vials at 2.50 × 10⁶ viable cells each."),
            "controlled-cooling": (self._cooling_ok(state), "Expected controlled_rate/passive_container at 0.8–1.2 °C/min and −80 °C for 16 h."),
            "vapour-phase-storage": (bool(state["storage"]) and state["storage"]["phase"] == "vapour" and state["storage"]["temperature_c"] == p["vapour_storage_temperature_c"], "Expected vapour at the displayed −150 °C."),
            "fast-thaw": (self._thaw_ok(state), "Expected 37 °C, no more than 60 s, small_ice_remains."),
            "post-thaw-dilution": (self._dilution_ok(state), "Expected 9.00 mL complete medium, gradual_with_mixing at 37 °C."),
            "dmso-removal": (self._removal_ok(state), "Expected 200 × g for 5 min, supernatant removed and 2.00 mL final volume."),
            "quarantine-pending-qc": (bool(state["quarantine"]) and state["quarantine"]["disposition"] == "quarantine_pending_qc" and state["quarantine"]["sterility_status"] == "pending" and state["quarantine"]["identity_status"] == "reference_on_file", "Expected quarantine_pending_qc with sterility pending and documented reference_on_file identity; pending identity does not satisfy this checkpoint."),
            "bank-tier-forward-link": (bool(state["location"]) and state["location"]["bank_tier"] == "working_stock" and bool(state["quarantine"]) and state["quarantine"]["forward_record"] == "lesson_8_bank_ledger", "Expected working_stock and lesson_8_bank_ledger."),
            "structured-result": (state["finished"] and bool(state["result"]), "A structured synthetic result must be submitted without future-growth or release claims."),
        }
        location = state["location"] or {}
        location_ok = location == {
            "dewar_id": "CRYO-A", "rack_id": "R-02", "box_id": "B-07",
            "position_id": "D4", "bank_tier": "working_stock",
        }
        r["location-record"] = (location_ok, "Expected CRYO-A/R-02/B-07/D4 and working_stock.")
        outcome = self._outcome(state)
        viability_ok = (state["removal"] is not None
                        and outcome["post_thaw_viability_pct"] >= p["minimum_post_thaw_viability_pct"])
        r["post-thaw-viability"] = (viability_ok, f"Synthetic viability {self._format_number(outcome['post_thaw_viability_pct'])}%; teaching threshold {self._format_number(p['minimum_post_thaw_viability_pct'])}%.")
        entered = state["recount"]
        if not entered:
            recount_ok = False
            detail = "No post-thaw recount was entered."
        else:
            tolerance = p["recount_relative_tolerance"]
            recount_ok = all((
                math.isclose(entered["viable_cells_recovered"], outcome["post_thaw_viable_cells_recovered"], rel_tol=tolerance),
                math.isclose(entered["viability_pct"], outcome["post_thaw_viability_pct"], rel_tol=tolerance),
                math.isclose(entered["viable_concentration_cells_ml"], outcome["post_thaw_viable_concentration_cells_ml"], rel_tol=tolerance),
            ))
            detail = (f"Expected {self._format_number(outcome['post_thaw_viable_cells_recovered'])} viable cells, "
                      f"{self._format_number(outcome['post_thaw_viability_pct'])}% and "
                      f"{self._format_number(outcome['post_thaw_viable_concentration_cells_ml'])} cells/mL; 0.2% allowance.")
        r["recount-arithmetic"] = (recount_ok, detail)
        return {cid: r[cid] for cid in self.checkpoint_ids()}

    def reveal(self, state):
        outcome = self._outcome(state)
        notes = [
            f"Hidden seeded baseline post-thaw viability: {self._format_number(state['hidden']['baseline_post_thaw_viability_pct'])}%.",
            f"Combined synthetic viability multiplier from handling decisions: {self._format_number(outcome['viability_multiplier'])}.",
            "The multiplier, conserved-total-cell assumption and 95% DMSO-solute removal are synthetic accounting choices, not physical validation.",
            "The recount is membrane integrity at one time; it establishes no future growth, identity, sterility or stock release.",
        ]
        if state["result"]:
            display_result = json.dumps(self._display_data(state["result"]), ensure_ascii=False, sort_keys=True)
            notes.append("Rounded display result (full precision remains internal): " + display_result)
        return notes
