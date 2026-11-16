"""Deterministic adherent passage and viable target-density planning.

The model uses explicit synthetic microscopy panels and tally transformations. It
checks a learner's own count and seeding arithmetic; it is not a biological growth,
dissociation-kinetics, pipetting-error or physical-validation model. The
counting aliquot is unavailable for seeding; original harvest remains the PDL basis.
"""

from __future__ import annotations

import math

from .engine import ActionRejected, Event, ProtocolModel, coach, round_significant


class AdherentPassage(ProtocolModel):
    protocol_id = "passage-an-adherent-line-to-a-target-density"

    def checkpoint_ids(self):
        return [
            "culture-inspected", "confluence-window", "overconfluent-refused",
            "spent-medium-removed", "wash-removes-inhibitors",
            "dissociation-reagent-volume", "dissociation-time-bounded",
            "detachment-confirmed", "neutralized-before-count",
            "centrifuge-and-resuspension", "count-dilution-and-tallies",
            "count-concentration-and-viability", "harvest-viability",
            "seed-volume-correct", "passage-and-pdl-record", "incubation-and-result",
        ]

    def start(self, rng):
        p = self.parameters
        overconfluent = rng.random() < p["overconfluent_probability"]
        confluence = (p["overconfluent_pct"] if overconfluent
                      else rng.randint(p["routine_confluence_pct"][0] + 2,
                                       p["routine_confluence_pct"][1] - 1))
        base_detachment = rng.randint(*p["base_detachment_range_pct"])
        return {
            "hidden": {
                "confluence_pct": confluence,
                "overconfluent": overconfluent,
                "base_detachment_pct": base_detachment,
            },
            "inspected": False,
            "entered_confluence": None,
            "disposition": None,
            "spent_removed": False,
            "wash": None,
            "reagent": None,
            "dissociation_minutes": None,
            "actual_detachment": None,
            "reported_detachment": None,
            "neutralization_volume": None,
            "collected": False,
            "resuspension_volume": None,
            "remaining_suspension_volume_ml": None,
            "dilution": None,
            "display_counts": None,
            "count_record": None,
            "count_calculation": None,
            "plan": None,
            "seeded": False,
            "label": None,
            "incubation": None,
            "result": None,
        }

    def _require_disposition(self, state):
        if state["disposition"] != "proceed":
            raise ActionRejected("Inspect the culture and choose routine passage first")

    def _viability_factor(self, state):
        p = self.parameters
        factor = 1.0
        minutes = state["dissociation_minutes"]
        if minutes is not None and minutes > p["dissociation_max_min"]:
            factor *= max(0.5, 1.0 - p["overexposure_penalty_per_min"]
                          * (minutes - p["dissociation_max_min"]))
        if (state["neutralization_volume"] is not None
                and state["neutralization_volume"] < p["neutralization_volume_ml"]):
            factor *= p["neutralization_viability_factor"]
        return factor

    def _make_display_counts(self, state):
        # Fixed correct-run tallies align with the reading. Penalties alter only the
        # unstained cells; chamber totals remain 63 and 67 respectively.
        factor = self._viability_factor(state)
        viable_a = round(58 * factor)
        viable_b = round(63 * factor)
        return {
            "A": {"unstained": viable_a, "stained": 63 - viable_a},
            "B": {"unstained": viable_b, "stained": 67 - viable_b},
        }

    def visible(self, state):
        culture = [["Material", "generic synthetic non-human adherent mammalian line"]]
        if state["inspected"]:
            culture += [
                ["Displayed confluence", f"{state['hidden']['confluence_pct']}%"],
                ["Entered confluence", f"{state['entered_confluence']}%"],
                ["Morphology", "expected for the synthetic panel; medium clear"],
            ]
        else:
            culture.append(["Inspection", "required before disposition"])
        culture.append(["Disposition", state["disposition"] or "not chosen"])
        panels = [{"title": "Culture", "rows": culture}]

        harvest = []
        if state["spent_removed"]:
            harvest.append(["Spent medium", "removed"])
        if state["wash"]:
            harvest.append(["Wash", f"{state['wash']['solution']}; {state['wash']['volume_ml']:g} mL"])
        if state["reagent"]:
            harvest.append(["Dissociation reagent", f"{state['reagent']['reagent']}; {state['reagent']['volume_ml']:g} mL"])
        if state["dissociation_minutes"] is not None:
            harvest.append(["Dissociation time", f"{state['dissociation_minutes']:g} min"])
        if state["reported_detachment"] is not None:
            harvest.append(["Detachment", f"{state['actual_detachment']}% displayed; {state['reported_detachment']}% entered"])
        if state["neutralization_volume"] is not None:
            harvest.append(["Complete medium added", f"{state['neutralization_volume']:g} mL"])
        if state["collected"]:
            harvest.append(["Collection", f"{state['collection_rcf']:g} × g for {state['collection_minutes']:g} min"])
            harvest.append(["Resuspension", f"{state['resuspension_volume']:g} mL"])
            if state["dilution"] is not None:
                harvest.append(["Suspension remaining after count sample", f"{state['remaining_suspension_volume_ml']:g} mL"])
        if harvest:
            panels.append({"title": "Harvest", "rows": harvest})

        if state["display_counts"]:
            rows = [["Dilution", f"1:{state['dilution']:g}"]]
            for chamber, tally in state["display_counts"].items():
                rows.append([f"Chamber {chamber}", f"{tally['unstained']} unstained; {tally['stained']} stained"])
            if state["count_record"]:
                expected = self.expected(state)
                rows += [["Recorded viable concentration", f"{expected['concentration_cells_ml']:.6g} cells/mL"],
                         ["Recorded viability", f"{expected['viability_pct']:.4g}%"]]
            panels.append({"title": "Synthetic counting panel", "rows": rows})

        if state["plan"]:
            plan = state["plan"]
            rows = [
                ["Flasks", str(plan["flask_count"])],
                ["Target", f"{plan['target_viable_cells_per_flask']:g} viable cells/flask"],
                ["Final volume", f"{plan['final_volume_ml_per_flask']:g} mL/flask"],
                ["Entered inoculum", f"{plan['seed_volume_ml_per_flask']:.6g} mL/flask"],
                ["Required fresh medium", f"{plan['fresh_medium_ml_per_flask']:.6g} mL/flask"],
                ["Seeded", "yes" if state["seeded"] else "no"],
            ]
            panels.append({"title": "Seeding plan", "rows": rows})
        if state["label"]:
            label = state["label"]
            panels.append({"title": "Passage record", "rows": [
                ["Passage", f"{label['previous_passage_number']} → {label['new_passage_number']}"],
                ["PDL increment", f"{label['pdl_increment']:.6g}"],
                ["Cumulative PDL", f"{label['new_cumulative_pdl']:.6g}"],
            ]})
        if state["incubation"]:
            item = state["incubation"]
            panels.append({"title": "Incubation record (no growth prediction)", "rows": [
                ["Conditions", f"{item['temperature_c']:g} °C; {item['co2_pct']:g}% CO₂; {item['hours']:g} h"],
            ]})
        return panels

    def act_inspect_culture(self, state, rng, confluence_pct):
        if state["inspected"]:
            raise ActionRejected("The culture has already been inspected")
        state["inspected"] = True
        state["entered_confluence"] = confluence_pct
        actual = state["hidden"]["confluence_pct"]
        state["clock"] += 1
        events = [Event("readout", f"The synthetic monolayer shows {actual}% confluence with expected morphology and clear medium.",
                        {"confluence_pct": actual})]
        if confluence_pct != actual:
            coach(state, events, "Record the displayed confluence, not the value you expected.")
        return events

    def act_decide_culture(self, state, rng, disposition):
        if not state["inspected"]:
            raise ActionRejected("Inspect the culture before choosing its disposition")
        if state["disposition"] is not None:
            raise ActionRejected("The culture disposition has already been chosen")
        state["disposition"] = disposition
        state["clock"] += 0.2
        if disposition == "discard_overconfluent":
            state["finished"] = True
            return [Event("info", "Routine passage is refused; the culture is assigned to the over-confluent discard/investigation branch.")]
        events = [Event("info", "The routine adherent-passage workflow is selected.")]
        if state["hidden"]["overconfluent"]:
            coach(state, events, "The displayed 95% culture belongs to the refusal branch, not routine passaging.")
        return events

    def act_remove_medium(self, state, rng):
        self._require_disposition(state)
        if state["spent_removed"]:
            raise ActionRejected("Spent medium has already been removed")
        if state["wash"] or state["reagent"]:
            raise ActionRejected("Spent medium must be removed before washing or dissociation")
        state["spent_removed"] = True
        state["clock"] += 1
        return [Event("info", "Spent medium is removed to culture waste.")]

    def act_wash_cells(self, state, rng, solution, volume_ml):
        self._require_disposition(state)
        if not state["spent_removed"]:
            raise ActionRejected("Remove spent medium before washing")
        if state["wash"]:
            raise ActionRejected("The monolayer has already been washed")
        state["wash"] = {"solution": solution, "volume_ml": volume_ml}
        state["clock"] += 1
        events = [Event("info", f"The monolayer is washed with {volume_ml:g} mL {solution.replace('_', ' ')}.")]
        if solution != "calcium_magnesium_free_bss" or volume_ml != self.parameters["wash_volume_ml"]:
            coach(state, events, "Use the declared calcium/magnesium-free wash and T-75 volume.")
        return events

    def act_add_dissociation_reagent(self, state, rng, reagent, volume_ml):
        self._require_disposition(state)
        if not state["wash"]:
            raise ActionRejected("Wash the monolayer before adding dissociation reagent")
        if state["reagent"]:
            raise ActionRejected("Dissociation reagent has already been added")
        state["reagent"] = {"reagent": reagent, "volume_ml": volume_ml}
        state["clock"] += 0.5
        events = [Event("info", f"Added {volume_ml:g} mL {reagent.replace('_', ' ')} dissociation reagent.")]
        if reagent != "enzyme_based" or volume_ml != self.parameters["dissociation_volume_ml"]:
            coach(state, events, "Use the declared generic enzyme-based reagent and coverage volume.")
        return events

    def act_incubate_dissociation(self, state, rng, minutes):
        self._require_disposition(state)
        if not state["reagent"]:
            raise ActionRejected("Add dissociation reagent before incubation")
        if state["dissociation_minutes"] is not None:
            raise ActionRejected("Dissociation incubation has already been recorded")
        state["dissociation_minutes"] = minutes
        base = state["hidden"]["base_detachment_pct"]
        reagent = state["reagent"]["reagent"]
        if reagent == "none":
            actual = 0
        elif reagent == "enzyme_free":
            actual = max(0, base - 20)
        elif minutes < 1:
            actual = round(base * 0.75)
        else:
            actual = min(99, base + (2 if minutes > self.parameters["dissociation_max_min"] else 0))
        state["actual_detachment"] = actual
        state["clock"] += minutes
        events = [Event("info", f"The dissociation reaction incubates for {minutes:g} min; the microscopy panel is ready.")]
        if not 1 <= minutes <= self.parameters["dissociation_max_min"]:
            coach(state, events, "Stay within the declared teaching bound and inspect rather than assuming complete detachment.")
        return events

    def act_check_detachment(self, state, rng, detached_pct):
        self._require_disposition(state)
        if state["dissociation_minutes"] is None:
            raise ActionRejected("Incubate the dissociation reaction before checking detachment")
        if state["reported_detachment"] is not None:
            raise ActionRejected("Detachment has already been recorded")
        state["reported_detachment"] = detached_pct
        actual = state["actual_detachment"]
        state["clock"] += 0.5
        events = [Event("readout", f"The synthetic microscopy panel shows {actual}% detached cells.",
                        {"detached_pct": actual})]
        if detached_pct != actual:
            coach(state, events, "Enter the displayed detachment percentage.")
        elif actual < self.parameters["minimum_detachment_pct"]:
            coach(state, events, "Fewer than 90% are detached; do not treat this as a successful harvest.")
        return events

    def act_neutralize(self, state, rng, volume_ml):
        self._require_disposition(state)
        if state["reported_detachment"] is None:
            raise ActionRejected("Inspect detachment before neutralization")
        if state["neutralization_volume"] is not None:
            raise ActionRejected("Neutralization has already been recorded")
        state["neutralization_volume"] = volume_ml
        state["clock"] += 1
        events = [Event("info", f"Added {volume_ml:g} mL complete growth medium after detachment inspection.")]
        if volume_ml != self.parameters["neutralization_volume_ml"]:
            coach(state, events, "Use two volumes of complete medium relative to the dissociation reagent.")
        return events

    def act_centrifuge_and_resuspend(self, state, rng, rcf_g, minutes, final_volume_ml):
        self._require_disposition(state)
        if state["neutralization_volume"] is None:
            raise ActionRejected("Neutralize before collection")
        if state["collected"]:
            raise ActionRejected("The cells have already been collected and resuspended")
        state["collected"] = True
        state["collection_rcf"] = rcf_g
        state["collection_minutes"] = minutes
        state["resuspension_volume"] = final_volume_ml
        state["remaining_suspension_volume_ml"] = final_volume_ml
        state["clock"] += minutes + 1
        events = [Event("info", f"Collected at {rcf_g:g} × g for {minutes:g} min and resuspended in {final_volume_ml:g} mL.")]
        if (rcf_g != self.parameters["centrifuge_rcf_g"] or minutes != self.parameters["centrifuge_min"]
                or final_volume_ml != self.parameters["resuspension_volume_ml"]):
            coach(state, events, "Use the declared collection conditions and final resuspension volume.")
        return events

    def act_prepare_count(self, state, rng, sample_ul, dye_ul):
        self._require_disposition(state)
        if not state["collected"]:
            raise ActionRejected("Collect and resuspend the cells before counting")
        if state["dilution"] is not None:
            raise ActionRejected("The counting mixture has already been prepared")
        state["remaining_suspension_volume_ml"] -= sample_ul / 1000
        state["dilution"] = (sample_ul + dye_ul) / sample_ul
        state["display_counts"] = self._make_display_counts(state)
        state["clock"] += 3  # the lesson-3 model assumes prompt counting after staining
        events = [Event("readout", "Two synthetic chamber tallies are available for the prepared mixture.",
                        {"chambers": state["display_counts"], "dilution": state["dilution"],
                         "count_sample_volume_ml": sample_ul / 1000,
                         "remaining_suspension_volume_ml": state["remaining_suspension_volume_ml"]})]
        if state["dilution"] != self.parameters["target_dilution"]:
            coach(state, events, "Use equal sample and dye volumes for the declared twofold dilution.")
        return events

    def act_record_count(self, state, rng, chamber_a_unstained, chamber_a_stained,
                         chamber_b_unstained, chamber_b_stained, viable_concentration_cells_ml, viability_pct):
        self._require_disposition(state)
        if not state["display_counts"]:
            raise ActionRejected("Prepare the counting mixture before recording tallies")
        if state["count_record"]:
            raise ActionRejected("The two-chamber count has already been recorded")
        state["count_record"] = {
            "A": {"unstained": chamber_a_unstained, "stained": chamber_a_stained},
            "B": {"unstained": chamber_b_unstained, "stained": chamber_b_stained},
        }
        state["count_calculation"] = {"concentration": viable_concentration_cells_ml, "viability": viability_pct}
        expected = self.expected(state)
        state["clock"] += 1
        return [Event("readout", "The two-chamber count and calculations are recorded.",
                      {"viable_concentration_cells_ml": expected["concentration_cells_ml"],
                       "viability_pct": expected["viability_pct"]})]

    def act_calculate_seed_volume(self, state, rng, flask_count, target_viable_cells_per_flask,
                                  final_volume_ml_per_flask, seed_volume_ml_per_flask):
        self._require_disposition(state)
        if not state["count_record"]:
            raise ActionRejected("Record the viable count before calculating seed volume")
        if state["plan"]:
            raise ActionRejected("The seeding plan has already been recorded")
        expected = self.expected(state)
        concentration = expected["concentration_cells_ml"]
        if concentration <= 0:
            raise ActionRejected("A nonzero viable-cell concentration is required for target-density seeding")
        required = target_viable_cells_per_flask / concentration
        if required > final_volume_ml_per_flask:
            raise ActionRejected("The required inoculum exceeds the destination flask's final volume")
        if required * flask_count > state["remaining_suspension_volume_ml"] + 1e-9:
            raise ActionRejected("The suspension remaining after the counting sample does not contain enough viable cells for this plan")
        if seed_volume_ml_per_flask > final_volume_ml_per_flask:
            raise ActionRejected("The entered inoculum cannot exceed the final culture volume")
        if seed_volume_ml_per_flask * flask_count > state["remaining_suspension_volume_ml"] + 1e-9:
            raise ActionRejected("The entered plan uses more suspension than remains after the counting sample")
        state["plan"] = {
            "flask_count": flask_count,
            "target_viable_cells_per_flask": target_viable_cells_per_flask,
            "final_volume_ml_per_flask": final_volume_ml_per_flask,
            "seed_volume_ml_per_flask": seed_volume_ml_per_flask,
            "required_seed_volume_ml_per_flask": required,
            "fresh_medium_ml_per_flask": final_volume_ml_per_flask - required,
        }
        state["clock"] += 1
        return [Event("readout", "The target-density plan is recorded with its conservation calculation.",
                      {"required_seed_volume_ml_per_flask": required,
                       "fresh_medium_ml_per_flask": final_volume_ml_per_flask - required})]

    def act_seed_flasks(self, state, rng):
        self._require_disposition(state)
        if not state["plan"]:
            raise ActionRejected("Calculate and record the seeding plan first")
        if state["seeded"]:
            raise ActionRejected("The destination flasks have already been seeded")
        state["seeded"] = True
        expected = self.expected(state)
        plan = state["plan"]
        state["clock"] += 2
        return [Event("info", f"Seeded {plan['flask_count']} synthetic T-75 flasks according to the recorded plan.",
                      {"viable_cells_seeded_per_flask": expected["viable_cells_seeded_per_flask"],
                       "total_viable_cells_seeded": expected["total_viable_cells_seeded"]})]

    def act_label_flasks(self, state, rng, previous_passage_number, previous_cumulative_pdl, pdl_increment):
        self._require_disposition(state)
        if not state["seeded"]:
            raise ActionRejected("Seed the flasks before completing their labels")
        if state["label"]:
            raise ActionRejected("The passage labels have already been recorded")
        state["label"] = {
            "previous_passage_number": previous_passage_number,
            "new_passage_number": previous_passage_number + 1,
            "previous_cumulative_pdl": previous_cumulative_pdl,
            "pdl_increment": pdl_increment,
            "new_cumulative_pdl": previous_cumulative_pdl + pdl_increment,
        }
        state["clock"] += 0.5
        return [Event("info", f"Labels record passage {previous_passage_number + 1} and cumulative PDL {previous_cumulative_pdl + pdl_increment:.6g}.")]

    def act_incubate_and_finish(self, state, rng, temperature_c, co2_pct, hours):
        self._require_disposition(state)
        if not state["label"]:
            raise ActionRejected("Complete the passage and PDL labels before incubation")
        state["incubation"] = {"temperature_c": temperature_c, "co2_pct": co2_pct, "hours": hours}
        state["result"] = self.expected(state)
        state["finished"] = True
        state["clock"] += hours * 60
        return [Event("readout", "The synthetic passage result is complete; no attachment or growth outcome is predicted.",
                      {"result": state["result"]})]

    def expected(self, state):
        """Structured derived values; all calculations use the learner's recorded tallies."""
        result = {
            "disposition": state["disposition"],
            "concentration_cells_ml": None,
            "viability_pct": None,
            "viable_harvest_cells": None,
            "pdl_increment": None,
            "new_passage_number": None,
            "new_cumulative_pdl": None,
        }
        if not state["count_record"]:
            return result
        viable = sum(item["unstained"] for item in state["count_record"].values())
        stained = sum(item["stained"] for item in state["count_record"].values())
        total = viable + stained
        concentration = (viable / 2) / self.parameters["chamber_volume_ml"] * state["dilution"]
        viability = viable / total * 100 if total else 0.0
        harvest = concentration * state["resuspension_volume"]
        result.update({
            "included_unstained_cells": viable,
            "included_stained_cells": stained,
            "included_total_cells": total,
            "dilution_factor": state["dilution"],
            "concentration_cells_ml": concentration,
            "viability_pct": viability,
            "resuspension_volume_ml": state["resuspension_volume"],
            "remaining_suspension_volume_ml": state["remaining_suspension_volume_ml"],
            "viable_harvest_cells": harvest,
            "pdl_increment": math.log2(harvest / self.parameters["previous_seeded_viable_cells"]) if harvest > 0 else None,
        })
        if state["plan"]:
            plan = state["plan"]
            result.update({
                "flask_count": plan["flask_count"],
                "target_viable_cells_per_flask": plan["target_viable_cells_per_flask"],
                "required_seed_volume_ml_per_flask": plan["required_seed_volume_ml_per_flask"],
                "fresh_medium_ml_per_flask": plan["fresh_medium_ml_per_flask"],
                "entered_seed_volume_ml_per_flask": plan["seed_volume_ml_per_flask"],
                "final_volume_ml_per_flask": plan["final_volume_ml_per_flask"],
                "viable_cells_seeded_per_flask": plan["seed_volume_ml_per_flask"] * concentration,
                "total_viable_cells_seeded": plan["seed_volume_ml_per_flask"] * concentration * plan["flask_count"],
            })
        if state["label"]:
            result.update({
                "new_passage_number": state["label"]["new_passage_number"],
                "new_cumulative_pdl": state["label"]["new_cumulative_pdl"],
            })
        if state["incubation"]:
            result["incubation"] = dict(state["incubation"])
        return result

    def evaluate(self, state):
        p = self.parameters
        r: dict[str, tuple[bool | None, str]] = {}
        inspected = state["inspected"] and state["entered_confluence"] == state["hidden"]["confluence_pct"]
        r["culture-inspected"] = (inspected, "The displayed confluence was inspected and recorded." if inspected
                                          else "Confluence was not inspected and recorded accurately.")
        over = state["hidden"]["overconfluent"]
        if over:
            r["confluence-window"] = (None, "The 95% scenario is evaluated by its own refusal checkpoint.")
            r["overconfluent-refused"] = (state["disposition"] == "discard_overconfluent",
                                                  "The 95% culture must not enter routine passage.")
        else:
            low, high = p["routine_confluence_pct"]
            r["confluence-window"] = (state["disposition"] == "proceed" and low <= state["hidden"]["confluence_pct"] <= high,
                                              f"Routine window {low}–{high}%; displayed {state['hidden']['confluence_pct']}%.")
            r["overconfluent-refused"] = (None, "No 95% over-confluent scenario applies.")
        if state["disposition"] != "proceed":
            for cid in self.checkpoint_ids()[3:]:
                r[cid] = (None, "No routine passage was performed.")
            return r

        wash = state["wash"] or {}
        reagent = state["reagent"] or {}
        r["spent-medium-removed"] = (state["spent_removed"], "Spent medium was removed." if state["spent_removed"] else "Spent medium was not removed.")
        wash_ok = (wash.get("solution") == "calcium_magnesium_free_bss" and wash.get("volume_ml") == p["wash_volume_ml"])
        r["wash-removes-inhibitors"] = (wash_ok, f"Wash: {wash or 'none'}; expected calcium/magnesium-free BSS, {p['wash_volume_ml']:g} mL.")
        reagent_ok = reagent.get("reagent") == "enzyme_based" and reagent.get("volume_ml") == p["dissociation_volume_ml"]
        r["dissociation-reagent-volume"] = (reagent_ok, f"Reagent: {reagent or 'none'}; expected enzyme_based, {p['dissociation_volume_ml']:g} mL.")
        minutes = state["dissociation_minutes"]
        time_ok = minutes is not None and 1 <= minutes <= p["dissociation_max_min"]
        r["dissociation-time-bounded"] = (time_ok, f"Dissociation time: {minutes}; expected 1–{p['dissociation_max_min']:g} min.")
        detach_ok = (state["reported_detachment"] == state["actual_detachment"]
                     and state["actual_detachment"] is not None
                     and state["actual_detachment"] >= p["minimum_detachment_pct"])
        r["detachment-confirmed"] = (detach_ok, f"Displayed/entered detachment: {state['actual_detachment']}/{state['reported_detachment']}%; minimum {p['minimum_detachment_pct']:g}%.")
        neutral_ok = state["neutralization_volume"] == p["neutralization_volume_ml"]
        r["neutralized-before-count"] = (neutral_ok, f"Complete medium: {state['neutralization_volume']}; expected {p['neutralization_volume_ml']:g} mL before collection/counting.")
        collect_ok = (state["collected"] and state["collection_rcf"] == p["centrifuge_rcf_g"]
                      and state["collection_minutes"] == p["centrifuge_min"]
                      and state["resuspension_volume"] == p["resuspension_volume_ml"])
        r["centrifuge-and-resuspension"] = (collect_ok, f"Collection/resuspension recorded: {collect_ok}; expected {p['centrifuge_rcf_g']:g} × g, {p['centrifuge_min']:g} min, {p['resuspension_volume_ml']:g} mL.")

        count_matches = bool(state["count_record"]) and state["count_record"] == state["display_counts"]
        dilution_ok = state["dilution"] == p["target_dilution"]
        r["count-dilution-and-tallies"] = (count_matches and dilution_ok,
                                                   f"Dilution {state['dilution']}; displayed tallies faithfully recorded: {count_matches}.")
        # The derived values are computed from the submitted tallies, so a false
        # transcription is caught above rather than silently corrected here.
        calculation_ok = False
        viability_ok = False
        if state["count_record"]:
            expected = self.expected(state)
            viability_ok = expected["viability_pct"] >= p["minimum_harvest_viability_pct"]
            detail = (f"Expected {round_significant(expected['concentration_cells_ml'], 4):g} viable cells/mL; "
                      f"viability {round_significant(expected['viability_pct'], 4):g}%.")
            calculation = state["count_calculation"]
            if calculation:
                calculation_ok = (math.isclose(calculation["concentration"], expected["concentration_cells_ml"], rel_tol=0.002)
                                  and math.isclose(calculation["viability"], expected["viability_pct"], rel_tol=0.002))
                detail += (f" Entered {calculation['concentration']:g} cells/mL and "
                           f"{calculation['viability']:g}% (0.2% rounding allowance).")
        else:
            detail = "No two-chamber calculation was recorded."
        r["count-concentration-and-viability"] = (calculation_ok, detail)
        r["harvest-viability"] = (viability_ok, f"Post-harvest viability must be at least {p['minimum_harvest_viability_pct']:g}%. {detail}")

        plan = state["plan"]
        if not plan:
            seed_ok = False
            seed_detail = "No seeding plan was recorded."
        else:
            required = plan["required_seed_volume_ml_per_flask"]
            tolerance = required * p["seed_volume_tolerance_pct"] / 100
            seed_ok = (plan["flask_count"] == p["target_flasks"]
                       and plan["target_viable_cells_per_flask"] == p["target_viable_cells_per_flask"]
                       and plan["final_volume_ml_per_flask"] == p["target_final_volume_ml"]
                       and abs(plan["seed_volume_ml_per_flask"] - required) <= tolerance)
            seed_detail = (f"Required {required:.6g} mL/flask; entered {plan['seed_volume_ml_per_flask']:.6g}; "
                           f"fresh medium {plan['fresh_medium_ml_per_flask']:.6g} mL/flask; tolerance {tolerance:.3g} mL.")
        r["seed-volume-correct"] = (seed_ok and state["seeded"], seed_detail + (" Seeded." if state["seeded"] else " Not seeded."))

        label = state["label"]
        if not label or not state["count_record"]:
            record_ok = False
            record_detail = "Passage and PDL labels are incomplete."
        else:
            expected_pdl = self.expected(state)["pdl_increment"]
            record_ok = (label["previous_passage_number"] == p["previous_passage_number"]
                         and label["new_passage_number"] == p["previous_passage_number"] + 1
                         and label["previous_cumulative_pdl"] == p["previous_cumulative_pdl"]
                         and abs(label["pdl_increment"] - expected_pdl) <= p["pdl_tolerance"])
            record_detail = (f"Expected passage {p['previous_passage_number'] + 1}; PDL increment {expected_pdl:.6g}; "
                             f"entered {label['pdl_increment']:.6g}; cumulative {label['new_cumulative_pdl']:.6g}.")
        r["passage-and-pdl-record"] = (record_ok, record_detail)

        incubation = state["incubation"]
        incubation_ok = bool(incubation) and incubation == {
            "temperature_c": p["incubation_temperature_c"], "co2_pct": p["incubation_co2_pct"],
            "hours": p["incubation_hours"]}
        r["incubation-and-result"] = (incubation_ok and state["finished"] and bool(state["result"]),
                                              f"Expected {p['incubation_temperature_c']:g} °C, {p['incubation_co2_pct']:g}% CO₂, {p['incubation_hours']:g} h; recorded {incubation}.")
        return r

    def reveal(self, state):
        h = state["hidden"]
        notes = [
            f"Initial synthetic confluence: {h['confluence_pct']}%; over-confluent scenario: {h['overconfluent']}.",
            f"Base detachment after the recommended exposure: {h['base_detachment_pct']}%.",
            f"Synthetic viability multiplier from dissociation/neutralization decisions: {self._viability_factor(state):.4g}.",
            "The tally transformation and incubation record are not physical validation or predictions of future growth, identity or sterility.",
        ]
        if state["result"]:
            notes.append("Structured result: " + repr(state["result"]))
        return notes
