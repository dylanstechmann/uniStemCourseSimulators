"""Deterministic synthetic hPSC-maintenance decisions and QC traceability.

This is a formative state machine, not a culture protocol, growth model or physical
validation. It does not authorize or certify hPSC work. All cells, lots, QC outcomes,
thresholds and consequences are synthetic and contain no donor or clinical data.
"""

from __future__ import annotations

import math

from .engine import ActionRejected, Event, ProtocolModel, coach


class HpscMaintenance(ProtocolModel):
    protocol_id = "maintain-an-hpsc-culture-without-spontaneous-differentiation"

    def checkpoint_ids(self):
        return [
            "consent-and-transfer-reviewed",
            "intake-quarantine-maintained",
            "intake-qc-bundle",
            "intake-contamination-cleared",
            "daily-morphology-scored",
            "differentiated-areas-removed",
            "daily-complete-feeds",
            "density-window-and-decisions",
            "matrix-coating-and-handling",
            "matrix-defect-response",
            "clump-not-single-cell",
            "clump-allocation-and-handling",
            "periodic-qc-bundle",
            "marker-interpretation",
            "maintenance-records",
            "privacy-preserving-records",
            "synthetic-finish-no-authorization",
        ]

    def start(self, rng):
        p = self.parameters
        return {
            "hidden": {
                "intake_mycoplasma_positive": rng.random() < p["intake_positive_probability"],
                "degrading_matrix": rng.random() < p["degrading_matrix_probability"],
            },
            "intake_review": None,
            "intake_qc": None,
            "quarantine_released": False,
            "terminal_reason": None,
            "day": 1,
            "density_pct": p["initial_density_pct"],
            "differentiated_area_pct": p["initial_differentiated_area_pct"],
            "daily": [],
            "passage_selected": False,
            "coating": None,
            "passage": None,
            "periodic_qc": None,
            "record": None,
            "stress_events": 0,
            "synthetic_viability_index": 100.0,
            "acknowledged_synthetic_only": False,
            "result": None,
        }

    @staticmethod
    def _event(kind, text, data=None, **kwargs):
        return Event(kind, text, {**(data or {}), **kwargs})

    @staticmethod
    def _qc_results(requests, intake_mycoplasma_positive=False):
        """Return evidence only for requested assays; never expose an unrequested outcome."""
        return {
            "mycoplasma": (
                "detected" if intake_mycoplasma_positive else "not_detected"
            ) if requests["mycoplasma_requested"] else "not_requested",
            "str_identity": "match" if requests["str_requested"] else "not_requested",
            "karyotype": "expected" if requests["karyotype_requested"] else "not_requested",
            "undifferentiated_markers": (
                "consistent_not_functional_proof"
                if requests["undifferentiated_markers_requested"] else "not_requested"
            ),
        }

    @staticmethod
    def _qc_text(prefix, results):
        labels = {
            "mycoplasma": "mycoplasma",
            "str_identity": "STR identity",
            "karyotype": "karyotype",
            "undifferentiated_markers": "undifferentiated markers",
        }
        statuses = "; ".join(f"{label}={results[key]}" for key, label in labels.items())
        return (
            f"{prefix}: {statuses}. Only requested assays have outcomes; "
            "not_requested means the assay was not performed and no categorical outcome is available."
        )

    @staticmethod
    def _qc_panel(title, results):
        labels = {
            "mycoplasma": "Mycoplasma",
            "str_identity": "STR identity",
            "karyotype": "Karyotype",
            "undifferentiated_markers": "Undifferentiated markers",
        }
        return {
            "title": title,
            "rows": [[label, results[key]] for key, label in labels.items()],
        }

    def _require_release(self, state):
        if not state["quarantine_released"]:
            raise ActionRejected("The incoming line remains in quarantine until consent and intake QC clear it")

    def _today(self, state):
        if len(state["daily"]) != state["day"] - 1:
            raise ActionRejected("Complete the current maintenance day before starting another")
        return None

    def _current(self, state):
        if len(state["daily"]) != state["day"]:
            raise ActionRejected("Score the current synthetic culture first")
        return state["daily"][-1]

    def _current_mutable(self, state):
        current = self._current(state)
        if current.get("completed"):
            raise ActionRejected("The current maintenance day is completed; further daily mutations are not permitted")
        return current

    def _finish_early(self, state, reason):
        state["terminal_reason"] = reason
        state["finished"] = True
        state["result"] = self.expected(state)

    def act_review_intake(self, state, rng, transfer_record, consent_scope_verified,
                          mta_restrictions_reviewed, provenance_recorded):
        if state["intake_review"] is not None:
            raise ActionRejected("Intake consent and transfer review is already recorded")
        state["intake_review"] = {
            "transfer_record": transfer_record,
            "consent_scope_verified": consent_scope_verified,
            "mta_restrictions_reviewed": mta_restrictions_reviewed,
            "provenance_recorded": provenance_recorded,
        }
        state["clock"] += 5
        cleared = (
            transfer_record == "MTA_SYNTH_01"
            and consent_scope_verified
            and mta_restrictions_reviewed
            and provenance_recorded
        )
        events = [self._event(
            "info",
            "Synthetic consent scope, transfer restrictions and provenance are reviewed; the line stays quarantined.",
        )]
        if not cleared:
            coach(state, events, "Missing or out-of-scope permissions cannot be replaced by promising morphology or QC results.")
            self._finish_early(state, "quarantined_consent_or_transfer")
            events.append(self._event(
                "consequence",
                "The synthetic line remains quarantined: no maintenance or passaging is permitted.",
                {"result": state["result"]},
            ))
        return events

    def act_submit_intake_qc(self, state, rng, mycoplasma_requested, str_requested,
                             karyotype_requested, undifferentiated_markers_requested):
        if state["intake_review"] is None:
            raise ActionRejected("Review consent and transfer restrictions before intake QC")
        if state["intake_qc"] is not None:
            raise ActionRejected("The intake QC bundle is already submitted")
        state["intake_qc"] = {
            "mycoplasma_requested": mycoplasma_requested,
            "str_requested": str_requested,
            "karyotype_requested": karyotype_requested,
            "undifferentiated_markers_requested": undifferentiated_markers_requested,
        }
        complete = all(state["intake_qc"].values())
        positive = state["hidden"]["intake_mycoplasma_positive"]
        results = self._qc_results(state["intake_qc"], positive)
        state["clock"] += 10
        events = [self._event(
            "readout",
            self._qc_text("Synthetic intake categorical results", results),
            {**results, "bundle_complete": complete},
        )]
        if complete and not positive:
            state["quarantine_released"] = True
            events.append(self._event("info", "Intake QC clears the synthetic line for the maintenance exercise."))
        else:
            self._finish_early(state, "quarantined_intake_qc")
            explanation = (
                "Quarantine remains in force because the intake bundle is incomplete; "
                "unrequested assays were not performed."
                if not complete else
                "Quarantine remains in force because the requested mycoplasma assay detected contamination."
            )
            events.append(self._event(
                "consequence",
                explanation,
                {"result": state["result"]},
            ))
        return events

    def act_score_culture(self, state, rng, density_pct, differentiated_area_pct):
        self._require_release(state)
        if state["passage_selected"]:
            raise ActionRejected("The maintenance phase has already ended with a passage decision")
        self._today(state)
        actual_density = state["density_pct"]
        actual_diff = state["differentiated_area_pct"]
        record = {
            "day": state["day"],
            "entered_density_pct": density_pct,
            "entered_differentiated_area_pct": differentiated_area_pct,
            "actual_density_pct": actual_density,
            "actual_differentiated_area_pct": actual_diff,
        }
        state["daily"].append(record)
        state["clock"] += 5
        recurrent = state["hidden"]["degrading_matrix"] and state["day"] >= 2
        events = [self._event(
            "readout",
            f"Day {state['day']} synthetic microscopy: density {actual_density:g}%; differentiated area {actual_diff:g}%.",
            {
                "day": state["day"],
                "density_pct": actual_density,
                "differentiated_area_pct": actual_diff,
                "pattern": (
                    "recurrent differentiation despite prior removal; investigate the matrix"
                    if recurrent else "routine synthetic colony panel"
                ),
            },
        )]
        if (density_pct != actual_density
                or not math.isclose(differentiated_area_pct, actual_diff, abs_tol=1e-9)):
            coach(state, events, "Record the displayed density and differentiated area, not expected values.")
        if state["stress_events"]:
            events.append(self._event(
                "consequence",
                "Earlier missed feeding contributes to the synthetic differentiation and viability-index changes.",
                {"stress_events": state["stress_events"]},
            ))
        return events

    def act_remove_differentiated(self, state, rng, removed_area_pct):
        self._require_release(state)
        current = self._current_mutable(state)
        if "removed_area_pct" in current:
            raise ActionRejected("Differentiated areas for this day are already recorded")
        actual = current["actual_differentiated_area_pct"]
        if removed_area_pct > actual + 1e-9:
            raise ActionRejected("Removal cannot exceed the displayed differentiated area")
        current["removed_area_pct"] = removed_area_pct
        state["differentiated_area_pct"] = actual - removed_area_pct
        state["clock"] += 5
        events = [self._event(
            "info",
            f"Manually removed {removed_area_pct:g}% differentiated area from the synthetic panel; residual {state['differentiated_area_pct']:g}%.",
        )]
        if removed_area_pct < actual:
            coach(state, events, "Selective removal should address every displayed differentiated area in this exercise.")
        return events

    def act_feed_culture(self, state, rng, complete_medium_change):
        self._require_release(state)
        current = self._current_mutable(state)
        if "complete_medium_change" in current:
            raise ActionRejected("Feeding for this day is already recorded")
        current["complete_medium_change"] = complete_medium_change
        state["clock"] += 5
        events = [self._event(
            "info",
            "Complete synthetic medium change recorded." if complete_medium_change
            else "No complete medium change recorded for this maintenance day.",
        )]
        if not complete_medium_change:
            coach(state, events, "A missed feed is a deviation with later synthetic consequences, not a neutral choice.")
        return events

    def act_decide_passage(self, state, rng, disposition, reason):
        self._require_release(state)
        current = self._current_mutable(state)
        if "disposition" in current:
            raise ActionRejected("The passage decision for this day is already recorded")
        current["disposition"] = disposition
        current["reason"] = reason
        state["clock"] += 2
        if disposition == "passage_now":
            state["passage_selected"] = True
        return [self._event("info", f"Day {state['day']} decision: {disposition.replace('_', ' ')}; reason: {reason.replace('_', ' ')}.")]

    def act_complete_day(self, state, rng):
        self._require_release(state)
        current = self._current(state)
        if current.get("completed"):
            raise ActionRejected("The current maintenance day is already completed")
        if "disposition" not in current:
            raise ActionRejected("Record the daily passage decision before completing the day")
        if not state["passage_selected"] and state["day"] >= self.parameters["maintenance_days"]:
            raise ActionRejected("On the final maintenance day, choose passage_now before completing the day")
        fed = current.get("complete_medium_change", False)
        if not fed:
            state["stress_events"] += 1
            state["synthetic_viability_index"] = max(
                0.0,
                state["synthetic_viability_index"] - self.parameters["missed_feed_viability_penalty"],
            )
        if state["passage_selected"]:
            current["completed"] = True
            return [self._event("info", "Maintenance ends for the synthetic clump-passage workflow; no later morphology panel is created.")]
        if not fed:
            state["differentiated_area_pct"] += self.parameters["missed_feed_differentiation_penalty_pct"]
        increment = (
            self.parameters["degrading_matrix_daily_differentiation_pct"]
            if state["hidden"]["degrading_matrix"]
            else self.parameters["stable_matrix_daily_differentiation_pct"]
        )
        state["differentiated_area_pct"] += increment
        state["density_pct"] += self.parameters["daily_density_increment_pct"]
        current["completed"] = True
        state["day"] += 1
        state["clock"] += 24 * 60
        return [self._event(
            "info",
            f"Advanced to day {state['day']}; fresh observation is required before any further action.",
        )]

    def act_coat_destination_matrix(self, state, rng, matrix_lot, handling, coverage, kept_moist):
        self._require_release(state)
        if not state["passage_selected"]:
            raise ActionRejected("Choose passage before preparing the destination matrix")
        if not self._current(state).get("completed"):
            raise ActionRejected("Complete the current passage day before preparing the destination matrix")
        if state["coating"] is not None:
            raise ActionRejected("The destination matrix is already prepared")
        state["coating"] = {
            "matrix_lot": matrix_lot,
            "handling": handling,
            "coverage": coverage,
            "kept_moist": kept_moist,
        }
        state["clock"] += 15
        events = [self._event(
            "readout",
            "Destination coating recorded; the synthetic harvest panel contains 156 small clumps.",
            {"available_clumps": self.parameters["available_clumps"]},
        )]
        if matrix_lot != "MAT_SYNTH_NEW" or handling != "cold_liquid" or coverage != "complete_even" or not kept_moist:
            coach(state, events, "Use the new synthetic lot, cold liquid handling, complete even coverage and a moist coating.")
        return events

    def act_passage_clumps(self, state, rng, method, triturations, well_count, clumps_per_well):
        self._require_release(state)
        if state["coating"] is None:
            raise ActionRejected("Prepare the destination matrix before clump passaging")
        if state["passage"] is not None:
            raise ActionRejected("The clump passage is already recorded")
        if well_count * clumps_per_well > self.parameters["available_clumps"]:
            raise ActionRejected("The allocation exceeds the 156 clumps in the synthetic harvest panel")
        state["passage"] = {
            "method": method,
            "triturations": triturations,
            "well_count": well_count,
            "clumps_per_well": clumps_per_well,
        }
        state["clock"] += 15
        events = [self._event(
            "info",
            f"Recorded {method.replace('_', ' ')} with {triturations} triturations into {well_count} wells at {clumps_per_well} clumps/well.",
        )]
        if method != "small_clumps" or not 2 <= triturations <= 3 or well_count != 6 or clumps_per_well != 26:
            coach(state, events, "Use gentle small-clump passage: 2–3 triturations and 156/6 = 26 clumps per well.")
        return events

    def act_submit_periodic_qc(self, state, rng, mycoplasma_requested, str_requested,
                               karyotype_requested, undifferentiated_markers_requested,
                               marker_interpretation):
        if state["passage"] is None:
            raise ActionRejected("Record the clump passage before periodic QC")
        if state["periodic_qc"] is not None:
            raise ActionRejected("The periodic QC bundle is already recorded")
        state["periodic_qc"] = {
            "mycoplasma_requested": mycoplasma_requested,
            "str_requested": str_requested,
            "karyotype_requested": karyotype_requested,
            "undifferentiated_markers_requested": undifferentiated_markers_requested,
            "marker_interpretation": marker_interpretation,
        }
        state["clock"] += 10
        results = self._qc_results(state["periodic_qc"])
        return [self._event(
            "readout",
            self._qc_text("Periodic synthetic categorical QC", results),
            results,
        )]

    def act_record_maintenance(self, state, rng, line_alias, medium_lot, matrix_lot,
                               new_passage_number, observation_days, deviation_recorded):
        if state["periodic_qc"] is None:
            raise ActionRejected("Submit periodic QC before closing the maintenance record")
        if state["record"] is not None:
            raise ActionRejected("The maintenance record is already complete")
        state["record"] = {
            "line_alias": line_alias,
            "medium_lot": medium_lot,
            "matrix_lot": matrix_lot,
            "new_passage_number": new_passage_number,
            "observation_days": observation_days,
            "deviation_recorded": deviation_recorded,
        }
        state["clock"] += 5
        return [self._event("info", "Synthetic-only maintenance, lot, passage, observation and deviation fields are recorded.")]

    def act_finish(self, state, rng, acknowledge_synthetic_only):
        if state["record"] is None:
            raise ActionRejected("Complete the maintenance record before finishing")
        state["acknowledged_synthetic_only"] = acknowledge_synthetic_only
        state["finished"] = True
        state["result"] = self.expected(state)
        return [self._event(
            "readout",
            "Synthetic maintenance loop complete. This does not authorize or certify hPSC work and predicts no real biological outcome.",
            {"result": state["result"]},
        )]

    def expected(self, state):
        intake_complete = bool(state["intake_qc"]) and all(state["intake_qc"].values())
        periodic_complete = bool(state["periodic_qc"]) and all(
            state["periodic_qc"][key]
            for key in (
                "mycoplasma_requested", "str_requested",
                "karyotype_requested", "undifferentiated_markers_requested",
            )
        )
        record_complete = self._record_ok(state)
        outcome = "in_progress"
        if state["terminal_reason"]:
            outcome = state["terminal_reason"]
        elif state["finished"]:
            outcome = "synthetic_loop_complete"
        return {
            "outcome": outcome,
            "quarantine_released": state["quarantine_released"],
            "intake_qc_complete": intake_complete,
            "days_observed": len(state["daily"]),
            "feeds_completed": sum(day.get("complete_medium_change") is True for day in state["daily"]),
            "missed_feeds": sum(not day.get("complete_medium_change", False) for day in state["daily"]),
            "stress_events": state["stress_events"],
            "synthetic_viability_index": state["synthetic_viability_index"],
            "final_density_pct": state["density_pct"],
            "final_differentiated_area_pct": state["differentiated_area_pct"],
            "matrix_defect_suspected": any(
                day.get("reason") == "matrix_investigation" for day in state["daily"]
            ),
            "passage_method": state["passage"]["method"] if state["passage"] else None,
            "periodic_qc_complete": periodic_complete,
            "record_complete": record_complete,
            "physical_hpsc_work_authorized": False,
            "certification_awarded": False,
            "real_biological_outcome_predicted": False,
        }

    def _record_ok(self, state):
        record = state["record"]
        if not record or not state["coating"]:
            return False
        any_missed_feed = any(not day.get("complete_medium_change", False) for day in state["daily"])
        deviation_required = bool(
            any_missed_feed
            or state["hidden"]["degrading_matrix"]
            or state["day"] != self.parameters["maintenance_days"]
            or state["coating"]["handling"] != "cold_liquid"
            or state["coating"]["coverage"] != "complete_even"
            or not state["coating"]["kept_moist"]
            or (state["passage"] and state["passage"]["method"] != "small_clumps")
        )
        return (
            record["line_alias"] == "SYNTH_HPSC_A"
            and record["medium_lot"] == "MED_SYNTH_01"
            and record["matrix_lot"] == state["coating"]["matrix_lot"]
            and record["new_passage_number"] == self.parameters["new_passage_number"]
            and record["observation_days"] == len(state["daily"])
            and record["deviation_recorded"] == deviation_required
        )

    def _empty_evaluation(self):
        return {cid: (None, "Not applicable in this terminal quarantine branch.") for cid in self.checkpoint_ids()}

    def evaluate(self, state):
        p = self.parameters
        r = self._empty_evaluation()
        review = state["intake_review"] or {}
        review_ok = (
            review.get("transfer_record") == "MTA_SYNTH_01"
            and review.get("consent_scope_verified") is True
            and review.get("mta_restrictions_reviewed") is True
            and review.get("provenance_recorded") is True
        )
        r["consent-and-transfer-reviewed"] = (
            review_ok,
            "Synthetic consent scope, transfer restrictions and provenance must all be verified before work.",
        )
        r["intake-quarantine-maintained"] = (
            not state["quarantine_released"] or bool(state["intake_qc"] and review_ok),
            "Culture actions are unreachable until the intake gates clear; quarantine was not bypassed.",
        )
        if state["terminal_reason"] == "quarantined_consent_or_transfer":
            return r
        intake = state["intake_qc"] or {}
        intake_complete = bool(intake) and all(intake.values())
        r["intake-qc-bundle"] = (
            intake_complete,
            "Intake bundle requires mycoplasma, STR identity, karyotype and undifferentiated-marker assessment.",
        )
        if intake_complete:
            cleared = not state["hidden"]["intake_mycoplasma_positive"] and state["quarantine_released"]
            r["intake-contamination-cleared"] = (
                cleared,
                "A complete bundle clears quarantine only when synthetic mycoplasma is not detected.",
            )
        if not state["quarantine_released"]:
            return r

        full_days_completed = (
            len(state["daily"]) == p["maintenance_days"]
            and all(day.get("completed") is True for day in state["daily"])
        )
        score_ok = full_days_completed and all(
            day["entered_density_pct"] == day["actual_density_pct"]
            and math.isclose(
                day["entered_differentiated_area_pct"],
                day["actual_differentiated_area_pct"],
                abs_tol=1e-9,
            )
            for day in state["daily"]
        )
        r["daily-morphology-scored"] = (
            score_ok,
            "Each of three days needs the displayed density and differentiated area recorded accurately.",
        )
        removal_ok = full_days_completed and all(
            math.isclose(
                day.get("removed_area_pct", 0),
                day["actual_differentiated_area_pct"],
                abs_tol=1e-9,
            )
            for day in state["daily"]
        )
        r["differentiated-areas-removed"] = (
            removal_ok,
            "Every displayed differentiated area is selectively removed without removing more than was displayed.",
        )
        feeds_ok = full_days_completed and all(
            day.get("complete_medium_change") is True for day in state["daily"]
        )
        r["daily-complete-feeds"] = (
            feeds_ok,
            f"Complete medium changes recorded on all three days; missed-feed stress events: {state['stress_events']}.",
        )
        decisions_ok = (
            full_days_completed
            and all(day.get("disposition") == "continue_maintenance" for day in state["daily"][:-1])
            and state["daily"][-1].get("disposition") == "passage_now"
            and p["passage_density_window_pct"][0] <= state["density_pct"] <= p["passage_density_window_pct"][1]
        )
        r["density-window-and-decisions"] = (
            decisions_ok,
            f"Continue on days 1–2 and passage on day 3 in the {p['passage_density_window_pct'][0]}–{p['passage_density_window_pct'][1]}% synthetic window; displayed {state['density_pct']}%.",
        )
        coating = state["coating"] or {}
        coating_ok = (
            coating.get("matrix_lot") == "MAT_SYNTH_NEW"
            and coating.get("handling") == "cold_liquid"
            and coating.get("coverage") == "complete_even"
            and coating.get("kept_moist") is True
        )
        r["matrix-coating-and-handling"] = (
            coating_ok,
            "Destination matrix requires the new synthetic lot, cold liquid handling, complete even coverage and no drying.",
        )
        final_reason = state["daily"][-1].get("reason") if state["daily"] else None
        matrix_reason_ok = (
            final_reason == "matrix_investigation"
            if state["hidden"]["degrading_matrix"]
            else final_reason == "routine_density"
        )
        r["matrix-defect-response"] = (
            matrix_reason_ok,
            "Recurrent differentiation despite removal should trigger matrix investigation; a routine panel uses the density rationale.",
        )
        passage = state["passage"] or {}
        r["clump-not-single-cell"] = (
            passage.get("method") == "small_clumps",
            "The routine synthetic method is small clumps, not default single-cell passaging.",
        )
        allocation_ok = (
            passage.get("method") == "small_clumps"
            and 2 <= passage.get("triturations", 0) <= 3
            and passage.get("well_count") == p["destination_wells"]
            and passage.get("clumps_per_well") == p["available_clumps"] // p["destination_wells"]
        )
        r["clump-allocation-and-handling"] = (
            allocation_ok,
            f"Expected 2–3 triturations and {p['available_clumps']}/{p['destination_wells']} = {p['available_clumps'] // p['destination_wells']} clumps per well.",
        )
        periodic = state["periodic_qc"] or {}
        periodic_complete = bool(periodic) and all(
            periodic.get(key) is True
            for key in (
                "mycoplasma_requested", "str_requested",
                "karyotype_requested", "undifferentiated_markers_requested",
            )
        )
        r["periodic-qc-bundle"] = (
            periodic_complete,
            "Periodic QC repeats mycoplasma, STR identity, karyotype and undifferentiated-marker assessment under the synthetic schedule.",
        )
        r["marker-interpretation"] = (
            periodic.get("undifferentiated_markers_requested") is True
            and periodic.get("marker_interpretation") == "undifferentiated_state_not_functional_proof",
            "Marker interpretation requires requested marker evidence; consistency supports an undifferentiated-state assessment but does not prove functional pluripotency.",
        )
        r["maintenance-records"] = (
            self._record_ok(state),
            "Record the synthetic line alias, medium and matrix lots, passage 13, actual observation-day count and any deviation.",
        )
        r["privacy-preserving-records"] = (
            bool(state["record"]) and state["record"]["line_alias"] == "SYNTH_HPSC_A",
            "Only synthetic aliases and categorical QC fields are accepted; no donor, clinical or STR-profile data are collected.",
        )
        r["synthetic-finish-no-authorization"] = (
            state["finished"] and state["acknowledged_synthetic_only"] and bool(state["result"]),
            "Finishing requires acknowledgement that the loop neither authorizes nor certifies hPSC work and predicts no real outcome.",
        )
        return r

    def visible(self, state):
        status = "quarantined"
        if state["quarantine_released"]:
            status = "released for synthetic maintenance"
        rows = [
            ["Material", "entirely synthetic hPSC-like teaching line; no donor or clinical data"],
            ["Quarantine", status],
            ["Consent/transfer review", "recorded" if state["intake_review"] else "required"],
            ["Intake QC", "recorded" if state["intake_qc"] else "required"],
        ]
        panels = [{"title": "Intake and permissions", "rows": rows}]
        if state["intake_qc"]:
            intake_results = self._qc_results(
                state["intake_qc"], state["hidden"]["intake_mycoplasma_positive"]
            )
            panels.append(self._qc_panel("Intake categorical QC", intake_results))
        if state["quarantine_released"]:
            culture = [["Maintenance day", str(state["day"])]]
            awaiting_score = (
                not state["passage_selected"]
                and len(state["daily"]) == state["day"] - 1
                and not state.get("finished", False)
            )
            if awaiting_score:
                culture += [
                    ["Current observation status", "awaiting score_culture"],
                    ["Current displayed density", f"{state['density_pct']:g}%"],
                    ["Current displayed differentiated area", f"{state['differentiated_area_pct']:g}%"],
                ]
            if state["daily"]:
                latest = state["daily"][-1]
                culture += [
                    ["Last displayed density", f"{latest['actual_density_pct']:g}%"],
                    ["Last displayed differentiated area", f"{latest['actual_differentiated_area_pct']:g}%"],
                    ["Entered density", f"{latest['entered_density_pct']:g}%"],
                    ["Entered differentiated area", f"{latest['entered_differentiated_area_pct']:g}%"],
                    ["Complete medium change", str(latest.get("complete_medium_change", "not recorded"))],
                    ["Disposition", latest.get("disposition", "not recorded")],
                ]
                if state["hidden"]["degrading_matrix"] and latest["day"] >= 2:
                    culture.append(["Observable pattern", "recurrent differentiation despite removal; investigate matrix"])
            culture.append(["Passage selected", str(state["passage_selected"])])
            panels.append({"title": "Synthetic culture observations", "rows": culture})
        if state["coating"]:
            panels.append({"title": "Destination matrix and harvest panel", "rows": [
                ["Coating", str(state["coating"])],
                ["Available synthetic clumps", str(self.parameters["available_clumps"])],
            ]})
        if state["passage"]:
            panels.append({"title": "Clump passage", "rows": [[key, str(value)] for key, value in state["passage"].items()]})
        if state["periodic_qc"]:
            periodic_panel = self._qc_panel(
                "Periodic categorical QC", self._qc_results(state["periodic_qc"])
            )
            periodic_panel["rows"].append([
                "Entered interpretation (not independent evidence)",
                state["periodic_qc"]["marker_interpretation"].replace("_", " "),
            ])
            panels.append(periodic_panel)
        if state["record"]:
            panels.append({"title": "Synthetic maintenance record", "rows": [[key, str(value)] for key, value in state["record"].items()]})
        return panels

    def reveal(self, state):
        return [
            f"Synthetic intake mycoplasma positive: {state['hidden']['intake_mycoplasma_positive']}.",
            f"Synthetic source-matrix degradation: {state['hidden']['degrading_matrix']}.",
            f"Missed-feed stress events: {state['stress_events']}; synthetic viability index: {state['synthetic_viability_index']:g}.",
            "The penalties, density trajectory and QC readouts are deterministic teaching choices, not measured hPSC biology or acceptance criteria.",
            "No physical technique, competency, authorization, certification or real biological outcome is established.",
        ]
