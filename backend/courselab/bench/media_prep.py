"""Deterministic supplemented-medium preparation, filtration and QC teaching model."""

from __future__ import annotations

import math

from .engine import ActionRejected, Event, ProtocolModel, coach

SERUM_LOTS = ("serum_lot_a", "serum_lot_b")
GLUTAMINE_ALIQUOTS = ("glutamine_aliquot_a", "glutamine_aliquot_b")
BOTTLES = ("bottle_a", "bottle_b")
COMPONENTS = ("basal", *SERUM_LOTS, *GLUTAMINE_ALIQUOTS)
SUPPORTED_INTEGRITY_TESTS = {"bubble_point", "pressure_hold"}

LABELS = {
    "basal": "basal-medium lot",
    "serum_lot_a": "serum lot A",
    "serum_lot_b": "serum lot B",
    "glutamine_aliquot_a": "glutamine aliquot A",
    "glutamine_aliquot_b": "glutamine aliquot B",
    "bottle_a": "receiving bottle A",
    "bottle_b": "receiving bottle B",
}


class SupplementedMediumPreparation(ProtocolModel):
    protocol_id = "filter-sterilize-and-qc-a-supplemented-medium"

    def checkpoint_ids(self):
        return [
            "supplies-inspected", "serum-in-date", "glutamine-aliquot-cold",
            "supplement-volumes", "prefiltration-qc", "correct-filter",
            "filter-integrity-verified", "labeled-collection-bottle",
            "sterility-samples-incubated", "dual-temperature-incubation",
            "mycoplasma-test-requested", "complete-label-and-lot-trace",
            "cold-dark-storage", "release-pending-qc",
        ]

    def start(self, rng):
        p = self.parameters
        mollicute_lot = rng.choice(COMPONENTS) if rng.random() < p["mollicute_lot_probability"] else None
        visible_lot = rng.choice(COMPONENTS) if rng.random() < p["visible_contaminant_lot_probability"] else None
        return {
            "hidden": {
                "expired_serum_lot": rng.choice(SERUM_LOTS),
                "warm_glutamine_aliquot": rng.choice(GLUTAMINE_ALIQUOTS),
                "unlabeled_bottle": rng.choice(BOTTLES),
                "mollicute_lot": mollicute_lot,
                "visible_contaminant_lot": visible_lot,
                "base_ph": rng.uniform(*p["base_ph_range"]),
            },
            "action_count": 0,
            "inspected": False,
            "inspection_late": False,
            "serum_lot": None,
            "serum_volume_ml": None,
            "glutamine_aliquot": None,
            "glutamine_volume_ml": None,
            "ph_method": None,
            "osmolality_method": None,
            "ph": None,
            "osmolality_mosm_kg": None,
            "filter": None,
            "filtered": False,
            "collection_bottle": None,
            "pre_rinsed": False,
            "aseptic_assembly": False,
            "filtered_volume_ml": 0.0,
            "remaining_volume_ml": 0.0,
            "mollicute_in_batch": False,
            "visible_contaminant_in_batch": False,
            "integrity_method": None,
            "integrity_pass": False,
            "aliquots": [],
            "label": None,
            "control": None,
            "incubations": [],
            "mycoplasma_requested": False,
            "storage": None,
            "product_risks": [],
        }

    def _advance(self, state, minutes):
        state["action_count"] += 1
        state["clock"] += minutes

    def _other(self, value, choices):
        return next(choice for choice in choices if choice != value)

    def _composition(self, state):
        if state["serum_volume_ml"] is None or state["glutamine_volume_ml"] is None:
            return None
        p = self.parameters
        final = p["final_batch_volume_ml"]
        serum = state["serum_volume_ml"]
        glutamine = state["glutamine_volume_ml"]
        return {
            "final_volume_ml": final,
            "basal_volume_ml": final - serum - glutamine,
            "serum_volume_ml": serum,
            "serum_final_percent": 100 * serum / final,
            "glutamine_volume_ml": glutamine,
            "glutamine_final_mm": p["glutamine_stock_mm"] * glutamine / final,
            "glutamine_final_fold": p["glutamine_stock_fold"] * glutamine / final,
        }

    def _component_used(self, state, component):
        if component == "basal":
            return True
        if component in SERUM_LOTS:
            return state["serum_lot"] == component
        return state["glutamine_aliquot"] == component

    def _valid_days(self, state):
        low = self.parameters["low_incubation_c"]
        high = self.parameters["high_incubation_c"]
        return sum(item["days"] for item in state["incubations"]
                   if low[0] <= item["temperature_c"] <= high[1])

    def _dual_temperature_ok(self, state):
        p = self.parameters
        required = p["dual_temp_min_days_each"]
        low, high = p["low_incubation_c"], p["high_incubation_c"]
        low_days = 0
        high_days = 0
        for item in state["incubations"]:
            temperature = item["temperature_c"]
            if low[0] <= temperature <= low[1]:
                low_days += item["days"]
            elif high[0] <= temperature <= high[1] and low_days >= required:
                high_days += item["days"]
        return low_days >= required and high_days >= required

    def _control_turbid(self, state):
        return bool(state["control"] and state["control"]["visible_contaminant"]
                    and self._valid_days(state) >= self.parameters["visible_growth_min_days"])

    def _lot_id(self, component):
        if component == "basal":
            return self.parameters["basal_lot_id"]
        if component == "filter":
            return self.parameters["filter_lot_id"]
        return self.parameters[f"{component}_id"]

    def _sterility_control_result(self, state):
        valid_days = self._valid_days(state)
        dual_temperature = self._dual_temperature_ok(state)
        schedule_complete = bool(
            state["control"] is not None
            and valid_days >= self.parameters["sterility_min_days"]
            and dual_temperature
        )
        if state["control"] is None:
            status = "not_drawn"
            visible_growth = None
        elif self._control_turbid(state):
            status = "visible_growth"
            visible_growth = True
        elif not schedule_complete:
            status = "insufficient_incubation"
            visible_growth = None
        else:
            status = "no_visible_growth"
            visible_growth = False
        return {
            "control_drawn": state["control"] is not None,
            "status": status,
            "valid_incubation_days": valid_days,
            "dual_temperature_schedule_met": dual_temperature,
            "schedule_complete": schedule_complete,
            "visible_growth": visible_growth,
        }

    def _mycoplasma_result(self, state):
        requested = state["mycoplasma_requested"]
        return {
            "requested": requested,
            "result": ("positive" if state["mollicute_in_batch"] else "negative")
            if requested else "not_submitted",
        }

    def act_inspect_supplies(self, state, rng):
        state["inspected"] = True
        state["inspection_late"] = state["action_count"] > 0
        hidden = state["hidden"]
        expired = hidden["expired_serum_lot"]
        valid = self._other(expired, SERUM_LOTS)
        warm = hidden["warm_glutamine_aliquot"]
        cold = self._other(warm, GLUTAMINE_ALIQUOTS)
        unlabeled = hidden["unlabeled_bottle"]
        labeled = self._other(unlabeled, BOTTLES)
        lot_ids = {component: self._lot_id(component) for component in COMPONENTS}
        data = {
            "expired_serum_lot": expired, "in_date_serum_lot": valid,
            "room_temperature_glutamine_aliquot": warm, "cold_glutamine_aliquot": cold,
            "unlabeled_bottle": unlabeled, "labeled_bottle": labeled,
            "lot_ids": lot_ids, "filter_lot_id": self._lot_id("filter"),
        }
        lot_text = "; ".join(f"{LABELS[component]}={lot_id}" for component, lot_id in lot_ids.items())
        text = (f"{LABELS[expired].capitalize()} expired on {self.parameters['expired_serum_on']}; {LABELS[valid]} expires on {self.parameters['valid_serum_expiry']}. "
                f"{LABELS[warm].capitalize()} was held at room temperature overnight; {LABELS[cold]} has a frozen/cold record. "
                f"{LABELS[unlabeled].capitalize()} has no identity label; {LABELS[labeled]} is sterile and labelled. "
                f"Original synthetic lot IDs: {lot_text}; filter={self._lot_id('filter')}.")
        self._advance(state, 2)
        return [Event("readout", text, data)]

    def act_add_serum(self, state, rng, lot, volume_ml):
        if state["filtered"]:
            raise ActionRejected("The medium is already filtered; start a new run to change its composition")
        if state["serum_lot"] is not None:
            raise ActionRejected("Serum has already been added")
        state["serum_lot"] = lot
        state["serum_volume_ml"] = volume_ml
        events = [Event("info", f"{volume_ml:g} mL of {LABELS[lot]} is added; basal medium will bring the final volume to 500 mL.")]
        if state["inspected"] and lot == state["hidden"]["expired_serum_lot"]:
            coach(state, events, "That serum lot is expired; select the in-date lot.")
        self._advance(state, 2)
        return events

    def act_add_glutamine(self, state, rng, aliquot, volume_ml):
        if state["filtered"]:
            raise ActionRejected("The medium is already filtered; start a new run to change its composition")
        if state["glutamine_aliquot"] is not None:
            raise ActionRejected("Glutamine has already been added")
        state["glutamine_aliquot"] = aliquot
        state["glutamine_volume_ml"] = volume_ml
        events = [Event("info", f"{volume_ml:g} mL of {LABELS[aliquot]} is added to the batch.")]
        if state["inspected"] and aliquot == state["hidden"]["warm_glutamine_aliquot"]:
            coach(state, events, "That aliquot has a room-temperature history; use the documented frozen/cold aliquot.")
        self._advance(state, 2)
        return events

    def act_measure_prefiltration_qc(self, state, rng, ph_method, osmolality_method):
        composition = self._composition(state)
        if composition is None:
            raise ActionRejected("Add both supplements before measuring the complete mixture")
        if state["filtered"]:
            raise ActionRejected("Pre-filtration QC must be measured before filtration")
        p = self.parameters
        hidden = state["hidden"]
        ph = (hidden["base_ph"] + 0.02 * (composition["serum_volume_ml"] - p["serum_volume_ml"]) / p["serum_volume_ml"]
              + 0.01 * (composition["glutamine_volume_ml"] - p["glutamine_volume_ml"]) / p["glutamine_volume_ml"])
        if state["glutamine_aliquot"] == hidden["warm_glutamine_aliquot"]:
            ph -= 0.05
        basal = composition["basal_volume_ml"]
        osmolality = (basal * p["basal_osmolality_mosm_kg"]
                      + composition["serum_volume_ml"] * p["serum_osmolality_mosm_kg"]
                      + composition["glutamine_volume_ml"] * p["glutamine_osmolality_mosm_kg"]) / composition["final_volume_ml"]
        state["ph_method"] = ph_method
        state["osmolality_method"] = osmolality_method
        state["ph"] = ph if ph_method == "calibrated_ph_meter" else None
        state["osmolality_mosm_kg"] = osmolality if osmolality_method == "osmometer" else None
        data = {
            "ph": state["ph"], "osmolality_mosm_kg": state["osmolality_mosm_kg"],
            "composition": composition, "osmolality_basis": "synthetic volume-weighted approximation",
        }
        readings = []
        if state["ph"] is not None:
            readings.append(f"pH {ph:.3f}")
        else:
            readings.append("pH not measured (colour only)")
        if state["osmolality_mosm_kg"] is not None:
            readings.append(f"osmolality {osmolality:.3f} mOsm/kg")
        else:
            readings.append("osmolality not measured")
        events = [Event("readout", "; ".join(readings) + ".", data)]
        if ph_method != "calibrated_ph_meter" or osmolality_method != "osmometer":
            coach(state, events, "Phenol-red colour and appearance cannot replace pH-meter and osmometer measurements.")
        self._advance(state, 3)
        return events

    def act_select_filter(self, state, rng, pore_size_um, membrane):
        if state["filtered"]:
            raise ActionRejected("Filtration is complete; start a new run to select another filter")
        filter_lot_id = self._lot_id("filter")
        state["filter"] = {"pore_size_um": pore_size_um, "membrane": membrane, "lot_id": filter_lot_id}
        events = [Event("info", f"Selected a {pore_size_um:g} µm {membrane} filter, lot {filter_lot_id}.",
                        {"lot_id": filter_lot_id})]
        if not math.isclose(pore_size_um, self.parameters["filter_pore_um"]) or membrane != self.parameters["filter_membrane"]:
            coach(state, events, "This exercise uses a 0.22 µm protein-compatible PVDF membrane.")
        self._advance(state, 1)
        return events

    def act_filter_medium(self, state, rng, collection_bottle, pre_rinsed, aseptic_assembly):
        if state["filtered"]:
            raise ActionRejected("The batch has already been filtered")
        if state["ph_method"] is None or state["osmolality_method"] is None:
            raise ActionRejected("Complete the pre-filtration QC step first")
        if state["filter"] is None:
            raise ActionRejected("Select a filter first")
        hidden = state["hidden"]
        mollicute_source = hidden["mollicute_lot"]
        visible_source = hidden["visible_contaminant_lot"]
        mollicute_present = mollicute_source is not None and self._component_used(state, mollicute_source)
        visible_present = visible_source is not None and self._component_used(state, visible_source)
        pore = state["filter"]["pore_size_um"]
        state["filtered"] = True
        state["collection_bottle"] = collection_bottle
        state["pre_rinsed"] = pre_rinsed
        state["aseptic_assembly"] = aseptic_assembly
        state["filtered_volume_ml"] = self.parameters["final_batch_volume_ml"] * self.parameters["filter_recovery_fraction"]
        state["remaining_volume_ml"] = state["filtered_volume_ml"]
        state["mollicute_in_batch"] = mollicute_present and pore > self.parameters["mollicute_retention_pore_um"]
        state["visible_contaminant_in_batch"] = (visible_present and pore > 0.22) or not aseptic_assembly
        if collection_bottle == hidden["unlabeled_bottle"]:
            state["product_risks"].append("filtrate collected in an unlabelled receiving bottle")
        if not state["inspected"]:
            coach_text = "Inspect supply and receiving-bottle records before selecting a receiver."
        elif collection_bottle == hidden["unlabeled_bottle"]:
            coach_text = "The selected receiving bottle is unlabelled; its identity and history are unknown."
        else:
            coach_text = ""
        events = [Event("info", f"Filtered {state['filtered_volume_ml']:g} mL into {LABELS[collection_bottle]}; "
                                "98% recovery is a synthetic accounting choice.")]
        if coach_text:
            coach(state, events, coach_text)
        if not pre_rinsed or not aseptic_assembly:
            coach(state, events, "Prime the filter and use aseptic sterile-receiver assembly.")
        self._advance(state, 8)
        return events

    def act_test_filter_integrity(self, state, rng, method):
        if not state["filtered"]:
            raise ActionRejected("Filter the medium before testing filter integrity")
        if state["integrity_method"] is not None:
            raise ActionRejected("The filter-integrity result is already recorded")
        state["integrity_method"] = method
        state["integrity_pass"] = method in SUPPORTED_INTEGRITY_TESTS
        result = "pass" if state["integrity_pass"] else "not established by visual inspection"
        events = [Event("readout", f"Filter-integrity result: {result}.",
                        {"method": method, "passed": state["integrity_pass"]})]
        if not state["integrity_pass"]:
            coach(state, events, "Use a device-supported bubble-point or pressure-hold integrity test.")
        self._advance(state, 3)
        return events

    def act_aliquot_medium(self, state, rng, count, volume_each_ml):
        if not state["filtered"]:
            raise ActionRejected("Filter the medium before aliquoting")
        requested = count * volume_each_ml
        if requested > state["remaining_volume_ml"] + 1e-9:
            raise ActionRejected(f"Requested {requested:g} mL exceeds the {state['remaining_volume_ml']:g} mL still available")
        state["aliquots"].append({"count": count, "volume_each_ml": volume_each_ml, "total_volume_ml": requested})
        state["remaining_volume_ml"] -= requested
        self._advance(state, count)
        return [Event("info", f"Prepared {count} × {volume_each_ml:g} mL aliquots; {state['remaining_volume_ml']:g} mL remains unallocated.",
                      {"aliquoted_ml": requested, "remaining_ml": state["remaining_volume_ml"]})]

    def act_label_bottle(self, state, rng, medium_name, prepared_on, expires_on, cell_line,
                         basal_lot_id, serum_lot_id, glutamine_lot_id, filter_lot_id, component_lots_linked):
        if not state["filtered"]:
            raise ActionRejected("Filter the medium before completing its batch label")
        if state["label"] is not None:
            raise ActionRejected("The batch label is already recorded; start a new run to replace it")
        state["label"] = {
            "batch_id": self.parameters["batch_id"], "medium_name": medium_name,
            "prepared_on": prepared_on, "expires_on": expires_on,
            "cell_line": cell_line, "basal_lot_id": basal_lot_id,
            "serum_lot_id": serum_lot_id, "glutamine_lot_id": glutamine_lot_id,
            "filter_lot_id": filter_lot_id, "component_lots_linked": component_lots_linked,
        }
        self._advance(state, 1)
        return [Event("info", f"Batch {self.parameters['batch_id']} labelled {medium_name} for {cell_line}; expiry {expires_on}.",
                      {"lot_ids": {
                          "basal": basal_lot_id, "serum": serum_lot_id,
                          "glutamine": glutamine_lot_id, "filter": filter_lot_id,
                      }})]

    def act_draw_sterility_control(self, state, rng, volume_ml, fresh_pipette):
        if not state["filtered"]:
            raise ActionRejected("Filter the medium before drawing a filtrate control")
        if state["control"] is not None:
            raise ActionRejected("The representative sterility control has already been drawn")
        if volume_ml > state["remaining_volume_ml"]:
            raise ActionRejected("The control volume exceeds the remaining filtrate")
        state["control"] = {
            "volume_ml": volume_ml, "fresh_pipette": fresh_pipette,
            "visible_contaminant": state["visible_contaminant_in_batch"] or not fresh_pipette,
            "mollicute": state["mollicute_in_batch"],
        }
        state["remaining_volume_ml"] -= volume_ml
        if not fresh_pipette:
            state["product_risks"].append("reused pipette for the filtrate control")
        self._advance(state, 1)
        return [Event("info", f"Drew a {volume_ml:g} mL filtrate control with a {'fresh' if fresh_pipette else 'reused'} pipette.")]

    def act_incubate_sterility_control(self, state, rng, days, temperature_c):
        if state["control"] is None:
            raise ActionRejected("Draw the filtrate sterility control before incubation")
        state["incubations"].append({"days": days, "temperature_c": temperature_c})
        state["clock"] += days * 1440
        state["action_count"] += 1
        return [Event("info", f"The filtrate control is incubated for {days} d at {temperature_c:g} °C.")]

    def act_submit_mycoplasma_lot_test(self, state, rng):
        if not state["filtered"]:
            raise ActionRejected("Filter the medium before submitting the batch for mycoplasma testing")
        if state["mycoplasma_requested"]:
            raise ActionRejected("A dedicated mycoplasma test has already been submitted")
        state["mycoplasma_requested"] = True
        self._advance(state, 1)
        return [Event("info", "A dedicated mycoplasma test is submitted for the supplemented-medium batch.")]

    def act_store_medium(self, state, rng, temperature_c, light_protected, release_status):
        if not state["filtered"]:
            raise ActionRejected("There is no filtered medium to store")
        state["storage"] = {
            "temperature_c": temperature_c, "light_protected": light_protected,
            "release_status": release_status,
        }
        events = [Event("info", f"Storage set to {temperature_c:g} °C, {'dark' if light_protected else 'in light'}; "
                                f"status {release_status.replace('_', ' ')}.")]
        if release_status == "release_immediately":
            coach(state, events, "Quarantine the batch until the required sterility schedule and mycoplasma evidence are acceptable.")
        self._advance(state, 1)
        return events

    def act_finish_preparation(self, state, rng):
        control_result = self._sterility_control_result(state)
        mycoplasma_result = self._mycoplasma_result(state)
        qc_outcome = {
            "sterility_control": control_result,
            "mycoplasma": mycoplasma_result,
            # Flattened compatibility fields retain the original result names.
            "valid_incubation_days": control_result["valid_incubation_days"],
            "dual_temperature_schedule_met": control_result["dual_temperature_schedule_met"],
            "visible_growth": control_result["visible_growth"],
            "mycoplasma_result": mycoplasma_result["result"],
        }
        result = {
            "batch_id": self.parameters["batch_id"] if state["filtered"] else None,
            "composition": self._composition(state),
            "prefiltration_qc": {"ph": state["ph"], "osmolality_mosm_kg": state["osmolality_mosm_kg"]},
            "filtration": {
                "filter": state["filter"], "recovered_volume_ml": state["filtered_volume_ml"],
                "integrity_method": state["integrity_method"], "integrity_pass": state["integrity_pass"],
            },
            "inventory": {
                "aliquots": state["aliquots"], "control_volume_ml": state["control"]["volume_ml"] if state["control"] else 0,
                "unallocated_volume_ml": state["remaining_volume_ml"],
            },
            "label": state["label"], "storage": state["storage"], "qc_outcome": qc_outcome,
        }
        state["finished"] = True
        events = [Event("info", "The supplemented-medium batch record is closed for debrief.", {"batch_result": result})]
        status = control_result["status"]
        if status == "not_drawn":
            control_text = "not drawn"
        elif status == "insufficient_incubation":
            control_text = (f"insufficient/incubation incomplete ({control_result['valid_incubation_days']} valid days); "
                            "no visible-growth-negative interpretation")
        elif status == "no_visible_growth":
            control_text = "no visible growth after the complete dual-temperature schedule"
        else:
            control_text = "visible growth observed"
            if not control_result["schedule_complete"]:
                control_text += "; incubation schedule incomplete"
        events.append(Event("consequence",
                            f"Sterility control: {control_text}; "
                            f"dedicated mycoplasma result: {mycoplasma_result['result']}."))
        return events

    def visible(self, state):
        panels = []
        if state["inspected"]:
            hidden = state["hidden"]
            lot_text = "; ".join(f"{LABELS[component]}={self._lot_id(component)}" for component in COMPONENTS)
            supply_rows = [
                ["Serum suitability", f"Use {LABELS[self._other(hidden['expired_serum_lot'], SERUM_LOTS)]}; the other lot is expired"],
                ["Glutamine suitability", f"Use {LABELS[self._other(hidden['warm_glutamine_aliquot'], GLUTAMINE_ALIQUOTS)]}; the other has a room-temperature history"],
                ["Receiver suitability", f"Use {LABELS[self._other(hidden['unlabeled_bottle'], BOTTLES)]}; the other is unlabelled"],
                ["Original synthetic lot IDs", f"{lot_text}; filter={self._lot_id('filter')}"],
            ]
        else:
            supply_rows = [["Labels and storage histories", "not inspected"]]
        panels.append({"title": "Supply review", "rows": supply_rows})
        composition = self._composition(state)
        if composition is not None:
            panels.append({"title": "Composition", "rows": [
                ["Basal medium", f"{composition['basal_volume_ml']:g} mL"],
                ["Serum", f"{composition['serum_volume_ml']:g} mL ({composition['serum_final_percent']:g}% final)"],
                ["Glutamine", f"{composition['glutamine_volume_ml']:g} mL stock; {composition['glutamine_final_mm']:g} mM final"],
                ["Final volume", f"{composition['final_volume_ml']:g} mL"],
            ]})
        if state["ph_method"] is not None:
            panels.append({"title": "Pre-filtration QC", "rows": [
                ["pH", "not measured" if state["ph"] is None else f"{state['ph']:.3f}"],
                ["Osmolality", "not measured" if state["osmolality_mosm_kg"] is None else f"{state['osmolality_mosm_kg']:.3f} mOsm/kg"],
            ]})
        if state["filter"] is not None:
            rows = [["Selected filter", f"{state['filter']['pore_size_um']:g} µm {state['filter']['membrane']}; lot {state['filter']['lot_id']}"],
                    ["Integrity", state["integrity_method"] or "not tested"]]
            if state["filtered"]:
                rows += [["Receiver", LABELS[state["collection_bottle"]]],
                         ["Recovered", f"{state['filtered_volume_ml']:g} mL"]]
            panels.append({"title": "Filtration", "rows": rows})
        if state["filtered"]:
            aliquoted = sum(item["total_volume_ml"] for item in state["aliquots"])
            panels.append({"title": "Batch inventory", "rows": [
                ["Aliquoted", f"{aliquoted:g} mL"],
                ["Sterility control", "not drawn" if state["control"] is None else f"{state['control']['volume_ml']:g} mL"],
                ["Unallocated", f"{state['remaining_volume_ml']:g} mL"],
            ]})
        if state["incubations"]:
            panels.append({"title": "Sterility-control schedule", "rows": [
                [f"{item['days']} d", f"{item['temperature_c']:g} °C"] for item in state["incubations"]
            ]})
        if state["label"] is not None:
            panels.append({"title": "Batch label", "rows": [[key.replace('_', ' '), str(value)] for key, value in state["label"].items()]})
        if state["storage"] is not None:
            panels.append({"title": "Storage and release", "rows": [[key.replace('_', ' '), str(value)] for key, value in state["storage"].items()]})
        return panels

    def evaluate(self, state):
        p = self.parameters
        hidden = state["hidden"]
        composition = self._composition(state)
        r: dict[str, tuple[bool | None, str]] = {}
        r["supplies-inspected"] = (state["inspected"] and not state["inspection_late"],
                                    "All supply records were inspected first." if state["inspected"] and not state["inspection_late"]
                                    else "Supply inspection was late or absent.")
        r["serum-in-date"] = (state["serum_lot"] is not None and state["serum_lot"] != hidden["expired_serum_lot"],
                               f"Serum used: {LABELS.get(state['serum_lot'], 'none')}.")
        r["glutamine-aliquot-cold"] = (state["glutamine_aliquot"] is not None
                                        and state["glutamine_aliquot"] != hidden["warm_glutamine_aliquot"],
                                        f"Glutamine used: {LABELS.get(state['glutamine_aliquot'], 'none')}.")
        volumes_ok = composition is not None and math.isclose(composition["serum_volume_ml"], p["serum_volume_ml"]) and math.isclose(composition["glutamine_volume_ml"], p["glutamine_volume_ml"])
        r["supplement-volumes"] = (volumes_ok,
                                    "Required 50 mL serum + 5 mL glutamine + 445 mL basal = 500 mL final."
                                    if volumes_ok else f"Actual composition: {composition}.")
        ph_ok = state["ph"] is not None and p["ph_range"][0] <= state["ph"] <= p["ph_range"][1]
        osmo_ok = state["osmolality_mosm_kg"] is not None and p["osmolality_range_mosm_kg"][0] <= state["osmolality_mosm_kg"] <= p["osmolality_range_mosm_kg"][1]
        r["prefiltration-qc"] = (state["ph_method"] == "calibrated_ph_meter" and state["osmolality_method"] == "osmometer" and ph_ok and osmo_ok,
                                  f"pH: {state['ph']}; osmolality: {state['osmolality_mosm_kg']}; methods: {state['ph_method']}/{state['osmolality_method']}.")
        selected = state["filter"]
        filter_ok = (state["filtered"] and selected is not None
                     and math.isclose(selected["pore_size_um"], p["filter_pore_um"])
                     and selected["membrane"] == p["filter_membrane"]
                     and state["pre_rinsed"] and state["aseptic_assembly"])
        r["correct-filter"] = (filter_ok, f"Filter: {selected}; primed: {state['pre_rinsed']}; aseptic assembly: {state['aseptic_assembly']}.")
        r["filter-integrity-verified"] = (state["integrity_pass"],
                                            f"Integrity method: {state['integrity_method'] or 'none'}; pass: {state['integrity_pass']}.")
        r["labeled-collection-bottle"] = (state["collection_bottle"] is not None
                                            and state["collection_bottle"] != hidden["unlabeled_bottle"],
                                            f"Receiving bottle: {LABELS.get(state['collection_bottle'], 'none')}.")
        control = state["control"]
        control_ok = (control is not None and control["fresh_pipette"]
                      and math.isclose(control["volume_ml"], p["sterility_control_volume_ml"])
                      and self._valid_days(state) >= p["sterility_min_days"])
        r["sterility-samples-incubated"] = (control_ok,
                                             f"Control: {control}; valid incubation: {self._valid_days(state)} d.")
        r["dual-temperature-incubation"] = (control is not None and self._dual_temperature_ok(state),
                                             "At least 7 d at 20–25 °C followed by at least 7 d at 30–35 °C is required.")
        r["mycoplasma-test-requested"] = (state["mycoplasma_requested"],
                                            "Dedicated test submitted." if state["mycoplasma_requested"] else "No dedicated mycoplasma test submitted.")
        expected_label = {
            "medium_name": p["medium_name"], "prepared_on": p["preparation_date"],
            "expires_on": p["expiry_date"], "cell_line": p["cell_line_id"],
            "basal_lot_id": self._lot_id("basal"),
            "serum_lot_id": self._lot_id(state["serum_lot"]) if state["serum_lot"] else None,
            "glutamine_lot_id": self._lot_id(state["glutamine_aliquot"]) if state["glutamine_aliquot"] else None,
            "filter_lot_id": state["filter"]["lot_id"] if state["filter"] else None,
            "component_lots_linked": True,
        }
        label_ok = state["label"] is not None and all(state["label"].get(key) == value for key, value in expected_label.items())
        r["complete-label-and-lot-trace"] = (label_ok, f"Recorded label: {state['label']}.")
        storage = state["storage"]
        cold_dark = (storage is not None and p["storage_temperature_c"][0] <= storage["temperature_c"] <= p["storage_temperature_c"][1]
                     and storage["light_protected"])
        r["cold-dark-storage"] = (cold_dark, f"Storage: {storage}.")
        r["release-pending-qc"] = (storage is not None and storage["release_status"] == "quarantine_until_qc",
                                     f"Release decision: {storage['release_status'] if storage else 'none'}.")
        return r

    def reveal(self, state):
        hidden = state["hidden"]
        mollicute = LABELS[hidden["mollicute_lot"]] if hidden["mollicute_lot"] else "none"
        visible = LABELS[hidden["visible_contaminant_lot"]] if hidden["visible_contaminant_lot"] else "none"
        return [
            f"Expired serum: {LABELS[hidden['expired_serum_lot']]}; room-temperature glutamine: {LABELS[hidden['warm_glutamine_aliquot']]}; unlabelled receiver: {LABELS[hidden['unlabeled_bottle']]}.",
            f"Hidden mollicute-carrying component: {mollicute}; hidden visibly culturable component contaminant: {visible}.",
            "Product risks: " + ("; ".join(state["product_risks"]) or "none recorded") + ".",
            f"Filtered batch carries mollicutes: {'yes' if state['mollicute_in_batch'] else 'no'}; visible contaminant: {'yes' if state['visible_contaminant_in_batch'] else 'no'}.",
            "The osmolality readout is a synthetic volume-weighted approximation; recovery, assays and growth timing are deterministic teaching choices.",
        ]
