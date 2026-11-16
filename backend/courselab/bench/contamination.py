"""Synthetic contamination, mycoplasma and STR evidence investigation.

The model permutes five anonymous scenarios with a seeded generator. Hidden condition
assignments stay out of panels until their specific evidence is revealed; final reveal
is available only through the engine's finished debrief. No biological or diagnostic
performance is simulated or validated.
"""

from __future__ import annotations

from .engine import ActionRejected, Event, ProtocolModel, coach

FLASKS = ("flask_p", "flask_q", "flask_r", "flask_s", "flask_t")
CONDITIONS = ("bacterial", "fungal", "mycoplasma", "str_mismatch", "clear_match")
VISIBLE_CONDITIONS = {"bacterial", "fungal"}
CLEAR_CONDITIONS = {"mycoplasma", "str_mismatch", "clear_match"}
MYCOPLASMA_TESTS = {"mycoplasma_pcr", "mycoplasma_culture", "mycoplasma_dna_stain"}
EXPECTED_VISIBLE_TEST = {"bacterial": "gram_stain", "fungal": "fungal_subculture"}
EXPECTED_SOURCE = {
    "bacterial": "shared_medium",
    "fungal": "shared_incubator",
    "mycoplasma": "incoming_shipment",
    "str_mismatch": "shared_pipette",
    "clear_match": "no_route_identified",
}
REFERENCE_PROFILE = {
    "SYN-L1": [8, 8],
    "SYN-L2": [10, 11],
    "SYN-L3": [12, 12],
    "SYN-L4": [7, 9],
}
MISMATCH_PROFILE = {
    "SYN-L1": [9, 10],
    "SYN-L2": [10, 12],
    "SYN-L3": [13, 14],
    "SYN-L4": [7, 8],
}
OBSERVATIONS = {
    "bacterial": "Turbid medium; pH 6.5 with acidic indicator shift; numerous small rod-shaped objects in the synthetic field.",
    "fungal": "Branching filaments and micro-colonies; pH 7.8 with alkaline indicator shift in the synthetic field.",
    "mycoplasma": "Clear medium; expected pH and synthetic cell morphology; no visible microbial clue.",
    "str_mismatch": "Clear medium; expected pH; synthetic cells look familiar, which does not authenticate identity.",
    "clear_match": "Clear medium; expected pH and synthetic cell morphology; no visible microbial clue.",
}
LINKED_RECORDS = {
    "bacterial": {
        "record_id": "SYN-LINK-LOT-06",
        "supports": "shared_medium",
        "clue": "Medium preparation log SYN-MED-06 places this flask and a linked vessel in the same medium-lot preparation window; their other recorded lots differ.",
        "competing_hypotheses": ["shared_pipette", "unresolved"],
        "interpretation_limit": "Shared-lot use prioritises a medium-lot investigation, but closure handling and workspace contact remain possible; the record does not prove the route.",
    },
    "fungal": {
        "record_id": "SYN-LINK-INC-02",
        "supports": "shared_incubator",
        "clue": "Equipment log SYN-INC-02 places this flask in an incubator during a flagged water-pan cleaning gap; the linked comparison flask used a different medium lot.",
        "competing_hypotheses": ["shared_medium", "shared_pipette"],
        "interpretation_limit": "The location and water-pan flag prioritise equipment review, but airborne or handling events remain possible; neither condition nor root cause is proven.",
    },
    "mycoplasma": {
        "record_id": "SYN-LINK-RCPT-03",
        "supports": "incoming_shipment",
        "clue": "Receipt/QC log SYN-RCPT-03 shows an incoming-shipment quarantine record with the local mycoplasma QC field incomplete before this flask entered the shared workflow.",
        "competing_hypotheses": ["shared_medium", "shared_pipette"],
        "interpretation_limit": "The receipt/QC gap prioritises incoming-shipment review, but later local contamination remains possible; the record is not a mycoplasma result.",
    },
    "str_mismatch": {
        "record_id": "SYN-LINK-HAND-04",
        "supports": "shared_pipette",
        "clue": "Handling log SYN-HAND-04 records a shared pipette and a temporary-label swap during a two-line transfer involving this flask; the medium and equipment entries show no matching exception.",
        "competing_hypotheses": ["incoming_shipment", "unresolved"],
        "interpretation_limit": "The transfer event prioritises pipette/label investigation, but an earlier mix-up or reference-record error remains possible; it does not reveal the STR result.",
    },
    "clear_match": {
        "record_id": "SYN-LINK-REV-05",
        "supports": "no_route_identified",
        "clue": "Review bundle SYN-REV-05 contains complete lot, incubator, receipt and handling entries with no flask-specific exception or linked positive finding.",
        "competing_hypotheses": ["unresolved", "incoming_shipment"],
        "interpretation_limit": "No route is identified in the reviewed records, but an unrecorded event cannot be excluded; this says nothing by itself about mycoplasma or identity status.",
    },
}


class ContaminationDiagnosis(ProtocolModel):
    protocol_id = "diagnose-a-contaminated-culture-from-clues"

    def checkpoint_ids(self):
        return [
            "all-flasks-inspected", "visible-clue-tests", "quarantine-before-identification",
            "dedicated-mycoplasma-evidence", "str-evidence-interpreted",
            "visible-contamination-discarded", "mycoplasma-contained",
            "authenticated-clear-released", "mismatch-isolated", "no-antibiotic-masking",
            "source-trace-complete", "incident-handoff-complete", "finished-with-evidence",
        ]

    def start(self, rng):
        assignments = list(CONDITIONS)
        rng.shuffle(assignments)
        return {
            "hidden": {"conditions": dict(zip(FLASKS, assignments, strict=True))},
            "inspected": [],
            "quarantined": [],
            "tests": {flask: [] for flask in FLASKS},
            "str_interpretations": {},
            "dispositions": {},
            "traces": {},
            "antibiotic_attempts": [],
            "handoff": None,
            "result": None,
        }

    def _condition(self, state, flask):
        return state["hidden"]["conditions"][flask]

    def _flasks_with(self, state, *conditions):
        return [flask for flask in FLASKS if self._condition(state, flask) in conditions]

    def _require_inspected(self, state, flask):
        if flask not in state["inspected"]:
            raise ActionRejected(f"Inspect {flask.replace('_', ' ')} before continuing")

    def _require_quarantine(self, state, flask):
        self._require_inspected(state, flask)
        if flask not in state["quarantined"]:
            raise ActionRejected(f"Quarantine {flask.replace('_', ' ')} before identification or disposition")

    def _require_all_flasks_quarantined(self, state):
        missing = [flask for flask in FLASKS if flask not in state["quarantined"]]
        if missing:
            pending = ", ".join(flask.replace("_", " ") for flask in missing)
            raise ActionRejected(
                "Inspect and quarantine all five linked flasks before testing, disposition "
                f"or antibiotic intervention; pending: {pending}"
            )

    def _test(self, state, flask, test):
        return next((item for item in state["tests"][flask] if item["test"] == test), None)

    def _has_mycoplasma_evidence(self, state, flask):
        return any(item["test"] in MYCOPLASMA_TESTS for item in state["tests"][flask])

    def _has_str_evidence(self, state, flask):
        return self._test(state, flask, "str_profile") is not None

    def _profile_text(self, profile):
        return "; ".join(f"{locus} [{alleles[0]},{alleles[1]}]" for locus, alleles in profile.items())

    def _linked_record(self, state, flask):
        record = LINKED_RECORDS[self._condition(state, flask)]
        return {
            "record_id": record["record_id"],
            "clue": record["clue"],
            "competing_hypotheses": record["competing_hypotheses"],
            "interpretation_limit": record["interpretation_limit"],
        }

    def act_inspect_flask(self, state, rng, flask):
        if flask in state["inspected"]:
            raise ActionRejected("This flask has already been inspected")
        if state["dispositions"]:
            raise ActionRejected("Inspect every flask before beginning dispositions")
        state["inspected"].append(flask)
        state["clock"] += 1
        observation = OBSERVATIONS[self._condition(state, flask)]
        linked_record = self._linked_record(state, flask)
        return [Event(
            "readout",
            f"{flask.replace('_', ' ').title()}: {observation} Linked-record bundle "
            f"{linked_record['record_id']} is revealed; weigh its clue and competing hypotheses before tracing.",
            {"flask": flask, "observation": observation, "linked_record": linked_record},
        )]

    def act_quarantine_flask(self, state, rng, flask):
        self._require_inspected(state, flask)
        if flask in state["quarantined"]:
            raise ActionRejected("This flask is already quarantined")
        if state["tests"][flask] or flask in state["dispositions"]:
            raise ActionRejected("Quarantine must precede testing and disposition")
        state["quarantined"].append(flask)
        state["clock"] += 0.5
        return [Event("info", f"{flask.replace('_', ' ').title()} remains closed and is separated from clean work; identifiers and linked records are preserved.")]

    def act_order_test(self, state, rng, flask, test):
        self._require_quarantine(state, flask)
        self._require_all_flasks_quarantined(state)
        if self._test(state, flask, test):
            raise ActionRejected("That test has already been ordered for this flask")
        if flask in state["dispositions"]:
            raise ActionRejected("The disposition is already recorded; start a new run for further testing")
        condition = self._condition(state, flask)
        positive = condition == "mycoplasma"
        if test == "gram_stain":
            result = ("Numerous Gram-stained rod-shaped objects support the broad bacterial pattern; no species is identified."
                      if condition == "bacterial" else "No bacterial-pattern field is established by this synthetic stain.")
            data = {"category_supported": condition == "bacterial", "species_identified": False}
        elif test == "fungal_subculture":
            result = ("Filamentous growth supports the broad fungal pattern; no species is identified."
                      if condition == "fungal" else "No fungal-pattern growth is established in this synthetic subculture.")
            data = {"category_supported": condition == "fungal", "species_identified": False}
        elif test == "mycoplasma_pcr":
            result = (f"Mycoplasma target {'detected' if positive else 'not detected'}; synthetic internal, positive and negative controls are valid. "
                      "This result is bounded by target coverage and does not prove universal sterility.")
            data = {"detected": positive, "controls_valid": True, "method": "nucleic_acid_amplification"}
        elif test == "mycoplasma_culture":
            result = ("Mycoplasma-pattern colonies observed in the synthetic selective-culture panel."
                      if positive else "No growth in the synthetic culture window; poorly or non-culturable strains remain a method limit.")
            data = {"detected": positive, "controls_valid": True, "method": "selective_culture"}
        elif test == "mycoplasma_dna_stain":
            result = ("Appropriate extranuclear DNA fluorescence pattern observed; interpretation supports mycoplasma in this scenario."
                      if positive else "No appropriate extranuclear pattern in this synthetic field; DNA staining is non-specific and can be insensitive/subjective.")
            data = {"detected": positive, "controls_valid": True, "method": "dna_stain"}
        elif test == "str_profile":
            profile = MISMATCH_PROFILE if condition == "str_mismatch" else REFERENCE_PROFILE
            result = (f"Synthetic reference: {self._profile_text(REFERENCE_PROFILE)}. "
                      f"Sample: {self._profile_text(profile)}. Record the relationship after comparing all four loci.")
            data = {"reference": REFERENCE_PROFILE, "sample": profile, "synthetic": True}
        else:  # pragma: no cover - the action schema excludes other values
            raise ActionRejected("Unknown test")
        record = {"test": test, "text": result, "data": data}
        state["tests"][flask].append(record)
        state["clock"] += 5 if test == "str_profile" else 1
        return [Event("readout", f"{flask.replace('_', ' ').title()} {test.replace('_', ' ')}: {result}", data)]

    def act_record_str_interpretation(self, state, rng, flask, relationship):
        self._require_quarantine(state, flask)
        if not self._has_str_evidence(state, flask):
            raise ActionRejected("Order and read the STR profile before interpreting identity")
        if flask in state["str_interpretations"]:
            raise ActionRejected("The STR interpretation has already been recorded")
        state["str_interpretations"][flask] = relationship
        state["clock"] += 0.5
        events = [Event("info", f"STR interpretation recorded as {relationship.replace('_', ' ')} for {flask.replace('_', ' ')}.")]
        expected = "mismatch" if self._condition(state, flask) == "str_mismatch" else "match"
        if relationship != expected:
            coach(state, events, "Compare every revealed synthetic allele call with the reference; do not infer identity from the label or appearance.")
        return events

    def act_decide_disposition(self, state, rng, flask, disposition):
        self._require_quarantine(state, flask)
        self._require_all_flasks_quarantined(state)
        if flask in state["dispositions"]:
            raise ActionRejected("The flask disposition has already been recorded")
        condition = self._condition(state, flask)
        if condition in VISIBLE_CONDITIONS:
            required = EXPECTED_VISIBLE_TEST[condition]
            if not self._test(state, flask, required):
                raise ActionRejected(f"Order {required.replace('_', ' ')} before the visible-pattern disposition")
        else:
            if not self._has_mycoplasma_evidence(state, flask):
                raise ActionRejected("Clear appearance is insufficient: order dedicated mycoplasma evidence first")
            if not self._has_str_evidence(state, flask) or flask not in state["str_interpretations"]:
                raise ActionRejected("Order and interpret STR evidence before the clear-flask disposition")
        state["dispositions"][flask] = disposition
        state["clock"] += 0.5
        events = [Event("info", f"Disposition recorded for {flask.replace('_', ' ')}: {disposition.replace('_', ' ')}.")]
        expected = self._expected_disposition(condition)
        if disposition != expected:
            coach(state, events, "Reconcile microbial and identity evidence: discard confirmed contamination, hold mismatch, and release only the reviewed clear match.")
        return events

    def _expected_disposition(self, condition):
        if condition in {"bacterial", "fungal", "mycoplasma"}:
            return "discard_sealed_decontaminated"
        if condition == "str_mismatch":
            return "hold_misidentified"
        return "release_after_review"

    def act_attempt_antibiotic_rescue(self, state, rng, flask, agent):
        self._require_quarantine(state, flask)
        self._require_all_flasks_quarantined(state)
        if flask in state["dispositions"]:
            raise ActionRejected("The disposition is already recorded")
        state["antibiotic_attempts"].append({"flask": flask, "agent": agent})
        state["clock"] += 1
        return [Event("consequence", "Visible growth may be suppressed, but the synthetic culture is not sterilised or authenticated. It remains quarantined with no release or rescue disposition; antibiotic masking fails the debrief checkpoint.")]

    def act_trace_source(self, state, rng, flask, source):
        self._require_quarantine(state, flask)
        if flask not in state["dispositions"]:
            raise ActionRejected("Record the evidence-based disposition before tracing the source")
        if flask in state["traces"]:
            raise ActionRejected("The source hypothesis has already been recorded")
        state["traces"][flask] = source
        state["clock"] += 0.5
        return [Event("info", f"Source hypothesis recorded for {flask.replace('_', ' ')}: {source.replace('_', ' ')}. The handoff must distinguish this hypothesis from proof.")]

    def act_record_incident_handoff(self, state, rng, scope, include_test_results,
                                    include_dispositions, include_source_traces, decontamination_requested):
        missing = [flask for flask in FLASKS if flask not in state["dispositions"] or flask not in state["traces"]]
        if missing:
            raise ActionRejected("Complete every disposition and source trace before the incident handoff")
        if state["handoff"]:
            raise ActionRejected("The incident handoff has already been recorded")
        state["handoff"] = {
            "scope": scope,
            "include_test_results": include_test_results,
            "include_dispositions": include_dispositions,
            "include_source_traces": include_source_traces,
            "decontamination_requested": decontamination_requested,
            "contains_personal_or_donor_data": False,
        }
        state["clock"] += 1
        return [Event("info", "Structured synthetic incident handoff recorded without donor or personal data.")]

    def act_finish_investigation(self, state, rng):
        if not state["handoff"]:
            raise ActionRejected("Record the complete incident handoff before finishing")
        state["result"] = {
            "synthetic": True,
            "flasks": {
                flask: {
                    "revealed_condition": self._condition(state, flask),
                    "tests": [item["test"] for item in state["tests"][flask]],
                    "disposition": state["dispositions"][flask],
                    "source_hypothesis": state["traces"][flask],
                }
                for flask in FLASKS
            },
            "handoff": dict(state["handoff"]),
            "physical_validation": False,
        }
        state["finished"] = True
        return [Event("readout", "Synthetic investigation complete. The reveal is formative and is not an incident clearance, diagnostic validation or competency record.", {"result": state["result"]})]

    def visible(self, state):
        rows = []
        for flask in FLASKS:
            if flask not in state["inspected"]:
                observation = "closed; inspection pending"
            else:
                observation = OBSERVATIONS[self._condition(state, flask)]
            rows.append([flask.replace("_", " ").title(), observation])
        panels = [{"title": "Synthetic closed-flask observations", "rows": rows}]
        record_rows = []
        for flask in state["inspected"]:
            record = self._linked_record(state, flask)
            alternatives = ", ".join(item.replace("_", " ") for item in record["competing_hypotheses"])
            record_rows.append([
                f"{flask.replace('_', ' ').title()}: {record['record_id']}",
                f"{record['clue']} Competing hypotheses: {alternatives}. {record['interpretation_limit']}",
            ])
        if record_rows:
            panels.append({"title": "Inspected synthetic linked-record bundles", "rows": record_rows})
        panels.append({"title": "Containment and dispositions", "rows": [
            [flask.replace("_", " ").title(),
             f"{'quarantined' if flask in state['quarantined'] else 'not quarantined'}; "
             f"disposition: {state['dispositions'].get(flask, 'pending')}; "
             f"source: {state['traces'].get(flask, 'pending')}"]
            for flask in FLASKS
        ]})
        evidence = []
        for flask in FLASKS:
            for item in state["tests"][flask]:
                evidence.append([f"{flask.replace('_', ' ').title()}: {item['test'].replace('_', ' ')}", item["text"]])
            if flask in state["str_interpretations"]:
                evidence.append([f"{flask.replace('_', ' ').title()}: recorded STR interpretation", state["str_interpretations"][flask]])
        if evidence:
            panels.append({"title": "Revealed evidence", "rows": evidence})
        if state["antibiotic_attempts"]:
            panels.append({"title": "Antibiotic attempts", "rows": [
                [item["flask"].replace("_", " ").title(), f"{item['agent'].replace('_', ' ')}; still quarantined; masking is not rescue"]
                for item in state["antibiotic_attempts"]
            ]})
        if state["handoff"]:
            panels.append({"title": "Incident handoff", "rows": [[key.replace("_", " "), str(value)] for key, value in state["handoff"].items()]})
        return panels

    def evaluate(self, state):
        r: dict[str, tuple[bool | None, str]] = {}
        inspected = set(state["inspected"]) == set(FLASKS)
        r["all-flasks-inspected"] = (inspected, f"Inspected {len(state['inspected'])}/{len(FLASKS)} flasks.")
        visible = self._flasks_with(state, *VISIBLE_CONDITIONS)
        visible_ok = all(self._test(state, flask, EXPECTED_VISIBLE_TEST[self._condition(state, flask)]) for flask in visible)
        r["visible-clue-tests"] = (visible_ok, "Bacterial pattern needs Gram stain; fungal pattern needs fungal subculture; neither identifies a species.")
        quarantined = set(state["quarantined"]) == set(FLASKS)
        r["quarantine-before-identification"] = (quarantined, f"Quarantined {len(state['quarantined'])}/{len(FLASKS)} flasks; the engine rejects every test, disposition and antibiotic intervention until the full linked set is inspected/quarantined.")
        clear = self._flasks_with(state, *CLEAR_CONDITIONS)
        myco_ok = all(self._has_mycoplasma_evidence(state, flask) for flask in clear)
        r["dedicated-mycoplasma-evidence"] = (myco_ok, f"Dedicated evidence present for {sum(self._has_mycoplasma_evidence(state, flask) for flask in clear)}/{len(clear)} clear flasks.")
        str_ok = True
        for flask in clear:
            expected = "mismatch" if self._condition(state, flask) == "str_mismatch" else "match"
            str_ok = str_ok and self._has_str_evidence(state, flask) and state["str_interpretations"].get(flask) == expected
        r["str-evidence-interpreted"] = (str_ok, "Every clear flask needs revealed STR evidence and the correct match/mismatch interpretation.")
        visible_discard = all(state["dispositions"].get(flask) == "discard_sealed_decontaminated" for flask in visible)
        r["visible-contamination-discarded"] = (visible_discard, "Confirmed bacterial and fungal patterns require sealed decontaminated discard.")
        myco_flask = self._flasks_with(state, "mycoplasma")[0]
        myco_disposed = state["dispositions"].get(myco_flask) == "discard_sealed_decontaminated"
        r["mycoplasma-contained"] = (myco_disposed, "The dedicated-test-positive flask requires sealed decontaminated discard, not antibiotic release.")
        normal = self._flasks_with(state, "clear_match")[0]
        normal_ok = (state["dispositions"].get(normal) == "release_after_review"
                     and state["str_interpretations"].get(normal) == "match")
        r["authenticated-clear-released"] = (normal_ok, "Only the clear mycoplasma-negative flask with a recorded STR match may be released after documented review; inconclusive or mismatch blocks this checkpoint.")
        mismatch = self._flasks_with(state, "str_mismatch")[0]
        mismatch_ok = state["dispositions"].get(mismatch) == "hold_misidentified"
        r["mismatch-isolated"] = (mismatch_ok, "The STR mismatch must be isolated for identity investigation, not released or treated as a microbial cure problem.")
        no_masking = not state["antibiotic_attempts"]
        r["no-antibiotic-masking"] = (no_masking, f"Antibiotic masking attempts: {len(state['antibiotic_attempts'])}; no attempt releases a flask.")
        traces_ok = all(state["traces"].get(flask) == EXPECTED_SOURCE[self._condition(state, flask)] for flask in FLASKS)
        r["source-trace-complete"] = (traces_ok, "Weigh each flask's revealed linked-record clue against its competing hypotheses; a supported source remains an incident hypothesis, not proof.")
        handoff = state["handoff"] or {}
        handoff_ok = handoff == {
            "scope": "all_linked_flasks", "include_test_results": True,
            "include_dispositions": True, "include_source_traces": True,
            "decontamination_requested": True, "contains_personal_or_donor_data": False,
        }
        r["incident-handoff-complete"] = (handoff_ok, f"Recorded handoff: {handoff or 'none'}.")
        complete = state["finished"] and bool(state["result"]) and len(state["dispositions"]) == len(FLASKS) and len(state["traces"]) == len(FLASKS)
        r["finished-with-evidence"] = (complete, "Final structured result is present only after dispositions, traces and handoff.")
        return r

    def reveal(self, state):
        notes = ["Synthetic condition and source assignments (not real organisms, cell lines, donors or ICLAC rows):"]
        for flask in FLASKS:
            condition = self._condition(state, flask)
            notes.append(f"{flask.replace('_', ' ').title()}: {condition}; source hypothesis {EXPECTED_SOURCE[condition]}.")
        notes += [
            "STR profiles use four invented loci and numeric alleles; a match is not sterility, phenotype or proof of reference correctness.",
            "Binary assay outputs assume valid controls and do not reproduce diagnostic sensitivity/specificity or organism behaviour.",
            "Antibiotic attempts never sterilise or release a culture. No physical validation, rescue efficacy or competency is claimed.",
        ]
        return notes
