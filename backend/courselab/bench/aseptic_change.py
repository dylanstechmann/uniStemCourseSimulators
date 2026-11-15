"""Aseptic medium change with hidden contamination events."""

from __future__ import annotations

from .engine import ActionRejected, Event, ProtocolModel, coach

LOTS = ("medium_lot_a", "medium_lot_b")
FLASKS = ("target_flask", "turbid_flask", "other_line_flask")
BOTTLES = {"medium_lot_a", "medium_lot_b", "waste_container", "antibiotics"}
BLOCKED_ZONES = {"front_opening", "front_grille", "rear_grille"}
PROTECTED_CONTAINERS = {"target_flask", "medium_lot_a", "medium_lot_b", "other_line_flask"}
STERILE_AGENT = "sterile_alcohol70"
VALID_WASTE_METHODS = ("chemical_then_autoclave", "autoclave_only")

LABELS = {
    "target_flask": "target culture flask",
    "turbid_flask": "turbid culture flask",
    "other_line_flask": "second cell-line flask",
    "medium_lot_a": "fresh-medium lot A",
    "medium_lot_b": "fresh-medium lot B",
    "waste_container": "spent-medium waste container",
    "pipettes": "sterile single-use pipettes",
    "pipette_aid": "pipette aid",
    "sterility_broth": "sterility-test broth tubes",
    "antibiotics": "penicillin-streptomycin stock",
}
EXPECTED_ZONE = {
    "target_flask": "work_center",
    "turbid_flask": "dirty_side",
    "medium_lot_a": "clean_side",
    "medium_lot_b": "clean_side",
    "waste_container": "dirty_side",
    "pipettes": "clean_side",
    "pipette_aid": "clean_side",
    "sterility_broth": "clean_side",
    "antibiotics": "clean_side",
}
AGENT_LABELS = {
    "sterile_alcohol70": "sterile 70% isopropyl alcohol",
    "nonsterile_alcohol70": "non-sterile 70% isopropyl alcohol",
    "water": "water",
}
LID_LABELS = {
    "held_above": "held above the opening",
    "upright_clean_surface": "upright on a disinfected surface",
    "face_down_surface": "face down on a surface",
}
CONTACT_LABELS = {
    "sterile_only": "sterile surfaces only",
    "dirty_cabinet_surface": "a dirty cabinet surface",
    "nonsterile_bench_surface": "a non-sterile bench surface",
}
APPROACH_LABELS = {"side": "from the side", "over_open_container": "over the open container"}
MOTION_LABELS = {"slow_gentle": "slow and gentle", "rapid": "rapid"}
CONTAINMENT_LABELS = {"sealed_biohazard": "sealed biohazard container", "open_bench_trash": "open bench trash"}
METHOD_LABELS = {
    "chemical_then_autoclave": "chemical decontamination followed by autoclaving",
    "autoclave_only": "autoclaving only",
    "no_treatment": "no treatment",
}
SOURCE_LABELS = {
    "spent_medium": "spent-medium control",
    "fresh_medium": "fresh-medium control",
    "target_flask": "target-culture control",
}


class AsepticMediumChange(ProtocolModel):
    protocol_id = "aseptic-medium-change-with-hidden-contamination"

    def checkpoint_ids(self):
        return [
            "supplies-inspected", "medium-in-date", "interior-disinfected-before-work",
            "items-surface-disinfected", "gloves-sanitized", "one-cell-line-only",
            "bottles-one-at-a-time", "no-inside-stacking", "grilles-and-opening-clear",
            "clean-to-dirty-arrangement", "no-open-flame", "side-approach-not-over",
            "slow-gentle-manipulation", "caps-never-face-down", "sterile-items-touch-nothing-dirty",
            "fresh-pipette-per-flask", "medium-volume-in-range", "sterility-samples-incubated",
            "dual-temperature-incubation", "contaminated-flasks-contained", "no-antibiotic-rescue",
            "mycoplasma-test-requested", "post-session-clean", "uv-not-a-substitute",
            "waste-decontaminated",
        ]

    def start(self, rng):
        p = self.parameters
        expired_lot = rng.choice(LOTS)
        mollicute_lot = rng.choice(LOTS) if rng.random() < p["mollicute_lot_probability"] else None
        visible_medium_lot = rng.choice(LOTS) if rng.random() < p["visible_medium_lot_probability"] else None
        dirty_interior = rng.random() < p["dirty_interior_probability"]
        return {
            "hidden": {
                "expired_lot": expired_lot,
                "mollicute_lot": mollicute_lot,
                "visible_medium_lot": visible_medium_lot,
                "dirty_interior": dirty_interior,
            },
            "inspected": False,
            "inspection_late": False,
            "interior_agent": None,
            "interior_cleaned_before_items": False,
            "interior_dirty": dirty_interior,
            "uv_minutes": 0.0,
            "glove_events": [],
            "items": {},
            "item_load_count": 0,
            "unwiped_items": set(),
            "arrangement_errors": [],
            "stacked": False,
            "blocked_zones": False,
            "max_bottles": 0,
            "other_line": False,
            "removed": [],
            "disposed": {},
            "open": {},
            "open_count": 0,
            "first_open_at": None,
            "turbid_opened": False,
            "turbid_event_at": None,
            "flame": False,
            "transfer_count": 0,
            "pipette_reuses": 0,
            "approach_errors": False,
            "motion_errors": False,
            "lid_errors": False,
            "critical_contact": False,
            "cross_contamination": False,
            "spend_removed": False,
            "spent_volume": None,
            "fresh_added": False,
            "fresh_volume": None,
            "used_medium": None,
            "visible_medium_used": False,
            "mollicute_target": False,
            "samples": [],
            "incubations": [],
            "samples_inspected": False,
            "antibiotics_added": False,
            "mycoplasma_requested": False,
            "waste_method": None,
            "final_agent": None,
            "product_risk": [],
            "personnel_risk": [],
        }

    def _valid_lot(self, state):
        return "medium_lot_b" if state["hidden"]["expired_lot"] == "medium_lot_a" else "medium_lot_a"

    def _loaded_bottles(self, state):
        return [item for item in state["items"] if item in BOTTLES]

    def _low_range(self):
        return self.parameters["low_incubation_c"]

    def _high_range(self):
        return self.parameters["high_incubation_c"]

    def _in_range(self, temperature, bounds):
        return bounds[0] <= temperature <= bounds[1]

    def _valid_incubation_days(self, state):
        low, high = self._low_range(), self._high_range()
        return sum(item["days"] for item in state["incubations"]
                   if self._in_range(item["temperature_c"], low) or self._in_range(item["temperature_c"], high))

    def _dual_temperature_ok(self, state):
        required = self.parameters["dual_temp_min_days_each"]
        low, high = self._low_range(), self._high_range()
        low_days = 0.0
        high_days = 0.0
        for item in state["incubations"]:
            temperature = item["temperature_c"]
            if self._in_range(temperature, low):
                low_days += item["days"]
            elif self._in_range(temperature, high) and low_days >= required:
                high_days += item["days"]
        return low_days >= required and high_days >= required

    def _sample_results(self, state):
        days = self._valid_incubation_days(state)
        threshold = self.parameters["visible_growth_min_days"]
        return [
            {
                "source": sample["source"],
                "turbid": bool(sample["visible_contaminant"]) and days >= threshold,
                "mollicute": bool(sample["mollicute"]),
            }
            for sample in state["samples"]
        ]

    def _visible_target_contaminated(self, state):
        return state["critical_contact"] or state["cross_contamination"] or state["visible_medium_used"]

    def _record_pipette(self, state, pipette_fresh, step):
        if pipette_fresh:
            return
        state["pipette_reuses"] += 1
        state["product_risk"].append(f"reused pipette during {step}")
        if state["turbid_opened"]:
            state["cross_contamination"] = True

    def _record_technique(self, state, pipette_fresh, tip_contact, approach, motion, talking, step):
        state["transfer_count"] += 1
        self._record_pipette(state, pipette_fresh, step)
        if tip_contact != "sterile_only":
            state["critical_contact"] = True
            state["product_risk"].append(f"sterile pipette touched {CONTACT_LABELS[tip_contact]} during {step}")
        if approach != "side":
            state["approach_errors"] = True
            state["product_risk"].append(f"approached {step} over the open container")
        if motion != "slow_gentle" or talking:
            state["motion_errors"] = True
            state["product_risk"].append(f"rapid movement or talking during {step}")
        if state["interior_dirty"]:
            state["critical_contact"] = True
            state["product_risk"].append(f"{step} while the cabinet interior was still contaminated")

    def act_inspect_supplies(self, state, rng):
        if state["item_load_count"] or state["open"] or state["transfer_count"] or state["samples"]:
            state["inspection_late"] = True
        state["inspected"] = True
        p = self.parameters
        expired = state["hidden"]["expired_lot"]
        valid = self._valid_lot(state)
        text = (
            f"Class II cabinet certification is current; critical zone {p['critical_zone_class']}; "
            f"HEPA downflow {p['hepa_velocity_m_s']:g} m/s ±{p['hepa_velocity_tolerance_pct']:g}%. "
            f"{LABELS[expired].capitalize()} expired on 2026-11-01; {LABELS[valid]} expires on 2026-12-15. "
            f"Both lots are labelled {p['sterilizing_filter_um']:g} µm filtered, which does not assure that "
            f"mollicutes of {p['mycoplasma_size_um'][0]:g}–{p['mycoplasma_size_um'][1]:g} µm are absent. "
            "The target flask has the expected line label and clear medium; the turbid flask has the same line "
            "label but visibly turbid medium; the second flask is a different cell line."
        )
        state["clock"] += 1
        return [Event("readout", text, {"expired_lot": expired, "in_date_lot": valid})]

    def act_disinfect_interior(self, state, rng, agent):
        if agent == STERILE_AGENT:
            state["interior_dirty"] = False
        state["interior_agent"] = agent
        if not state["item_load_count"] and not state["open"] and not state["transfer_count"]:
            state["interior_cleaned_before_items"] = agent == STERILE_AGENT
        state["clock"] += 3
        events = [Event("info", f"The empty cabinet interior is wiped with {AGENT_LABELS[agent]} and held for the "
                                f"written contact time. {self.parameters['alcohol_percent']:g}% alcohol is not sporicidal.")]
        if agent != STERILE_AGENT:
            coach(state, events, "Use a sterile disinfectant and allow contact time before aseptic work.")
        return events

    def act_run_uv_lamp(self, state, rng, minutes):
        state["uv_minutes"] += minutes
        state["clock"] += minutes
        events = [Event("info", f"The UV lamp runs for {minutes:g} min.")]
        if state["interior_agent"] != STERILE_AGENT:
            coach(state, events, "UV effectiveness is limited and does not replace chemical surface disinfection.")
        return events

    def act_sanitize_gloves(self, state, rng, agent):
        state["glove_events"].append({"agent": agent, "clock": state["clock"]})
        state["clock"] += 1
        events = [Event("info", f"Gloves are sanitized with {AGENT_LABELS[agent]}.")]
        if agent != STERILE_AGENT:
            coach(state, events, "Use sterile alcohol and allow it to dry before touching sterile items.")
        return events

    def act_load_item(self, state, rng, item, zone, wiped):
        if item in state["items"]:
            raise ActionRejected(f"The {LABELS[item]} is already in the cabinet")
        if item in state["disposed"]:
            raise ActionRejected(f"The {LABELS[item]} has already been disposed of")
        state["items"][item] = {"zone": zone, "wiped": wiped}
        state["item_load_count"] += 1
        state["max_bottles"] = max(state["max_bottles"], len(self._loaded_bottles(state)))
        events = [Event("info", f"The {LABELS[item]} is placed at the {zone.replace('_', ' ')}.")]
        if not wiped:
            state["unwiped_items"].add(item)
            coach(state, events, "Surface-disinfect items before they enter the cabinet.")
        if zone == "stacked":
            state["stacked"] = True
            coach(state, events, "Do not stack items inside the cabinet.")
        if zone in BLOCKED_ZONES:
            state["blocked_zones"] = True
            coach(state, events, "Keep the front opening and grilles clear.")
        expected = EXPECTED_ZONE.get(item)
        if expected and zone != expected:
            state["arrangement_errors"].append(f"{LABELS[item]} at {zone.replace('_', ' ')}")
            coach(state, events, "Arrange the work area from clean to dirty.")
        if item == "other_line_flask":
            state["other_line"] = True
            state["cross_contamination"] = True
            state["product_risk"].append("a second cell line was brought into the cabinet")
            coach(state, events, "Never have more than one cell line in the cabinet at a time.")
        if state["inspected"] and item == state["hidden"]["expired_lot"]:
            coach(state, events, "That fresh-medium lot is expired.")
        if state["max_bottles"] > 1:
            coach(state, events, "Keep only one medium or waste bottle inside at a time.")
        state["clock"] += 0.5
        return events

    def act_remove_item(self, state, rng, item, decontaminated):
        if item not in state["items"]:
            raise ActionRejected(f"The {LABELS[item]} is not in the cabinet")
        if item in state["open"]:
            raise ActionRejected(f"Close the {LABELS[item]} before removing it")
        del state["items"][item]
        state["removed"].append({"item": item, "decontaminated": decontaminated})
        events = [Event("info", f"The {LABELS[item]} is removed.")]
        if item == "turbid_flask" and "turbid_flask" not in state["disposed"]:
            state["personnel_risk"].append("turbid flask removed without sealed decontaminated disposal")
            coach(state, events, "Dispose of the turbid flask in a sealed decontaminated biohazard container.")
        if item == "waste_container" and state["spend_removed"] and state["waste_method"] not in VALID_WASTE_METHODS:
            state["personnel_risk"].append("spent-medium waste removed before decontamination")
            coach(state, events, "Decontaminate culture waste before disposal.")
        if not decontaminated:
            state["personnel_risk"].append(f"{LABELS[item]} removed without surface decontamination")
        state["clock"] += 0.5
        return events

    def act_open_container(self, state, rng, container, lid_position):
        if container not in state["items"]:
            raise ActionRejected(f"The {LABELS[container]} is not in the cabinet")
        if container in state["open"]:
            raise ActionRejected(f"The {LABELS[container]} is already open")
        state["open"][container] = lid_position
        state["open_count"] += 1
        if state["first_open_at"] is None:
            state["first_open_at"] = state["clock"]
        events = [Event("info", f"The {LABELS[container]} is opened with its closure {LID_LABELS[lid_position]}.")]
        if lid_position == "face_down_surface":
            state["lid_errors"] = True
            state["critical_contact"] = True
            state["product_risk"].append(f"{LABELS[container]} closure placed face down")
            coach(state, events, "Never place a cap or closure face down.")
        if container == "turbid_flask":
            state["turbid_opened"] = True
            state["turbid_event_at"] = state["clock"]
            state["cross_contamination"] = True
            state["product_risk"].append("turbid flask opened in the clean workflow")
            coach(state, events, "Keep the visibly contaminated flask closed and contain it for disposal.")
        if container == "other_line_flask":
            state["other_line"] = True
            state["cross_contamination"] = True
            state["product_risk"].append("second cell line opened")
            coach(state, events, "Never have more than one cell line in the cabinet at a time.")
        if state["interior_dirty"] and container in PROTECTED_CONTAINERS:
            state["critical_contact"] = True
            state["product_risk"].append(f"{LABELS[container]} opened while the cabinet interior was still contaminated")
        state["clock"] += 0.5
        return events

    def act_close_container(self, state, rng, container):
        if container not in state["open"]:
            raise ActionRejected(f"The {LABELS[container]} is not open")
        del state["open"][container]
        state["clock"] += 0.25
        return [Event("info", f"The {LABELS[container]} is closed.")]

    def act_inspect_flask(self, state, rng, container):
        if container not in state["items"]:
            raise ActionRejected(f"The {LABELS[container]} is not in the cabinet")
        if container == "target_flask":
            text = "Target flask: expected line label, adherent monolayer and clear spent medium."
        elif container == "turbid_flask":
            text = "Turbid flask: same line label but visibly turbid medium; keep it closed and contain it."
        else:
            text = "Second cell-line flask: a different line label; it must not enter this clean workflow."
        state["clock"] += 0.5
        return [Event("readout", text)]

    def act_remove_spent_medium(self, state, rng, volume_ml, pipette_fresh, tip_contact, approach, motion, talking):
        if "target_flask" not in state["open"]:
            raise ActionRejected("Open the target flask first")
        if "waste_container" not in state["items"]:
            raise ActionRejected("Place the spent-medium waste container in the cabinet")
        if state["spend_removed"]:
            raise ActionRejected("The spent medium has already been removed")
        state["spend_removed"] = True
        state["spent_volume"] = volume_ml
        self._record_technique(state, pipette_fresh, tip_contact, approach, motion, talking, "spent-medium removal")
        state["clock"] += 2
        return [Event("info", f"{volume_ml:g} mL of spent medium is transferred to the waste container.")]

    def act_add_fresh_medium(self, state, rng, volume_ml, pipette_fresh, tip_contact, approach, motion, talking):
        if "target_flask" not in state["open"]:
            raise ActionRejected("Open the target flask first")
        if not state["spend_removed"]:
            raise ActionRejected("Remove the spent medium first")
        if state["fresh_added"]:
            raise ActionRejected("Fresh medium has already been added")
        open_lots = [item for item in state["open"] if item in LOTS]
        if not open_lots:
            raise ActionRejected("Open one fresh-medium lot")
        if len(open_lots) > 1:
            raise ActionRejected("Only one fresh-medium lot may be open")
        lot = open_lots[0]
        state["used_medium"] = lot
        state["fresh_volume"] = volume_ml
        state["fresh_added"] = True
        hidden = state["hidden"]
        events = [Event("info", f"{volume_ml:g} mL of {LABELS[lot]} is added to the target flask.")]
        if lot == hidden["expired_lot"]:
            state["product_risk"].append("expired fresh medium used")
            coach(state, events, "That lot is expired.")
        if lot == hidden["visible_medium_lot"]:
            state["visible_medium_used"] = True
            state["product_risk"].append("visibly culturable contamination in the fresh-medium lot")
        if lot == hidden["mollicute_lot"]:
            state["mollicute_target"] = True
        self._record_technique(state, pipette_fresh, tip_contact, approach, motion, talking, "fresh-medium addition")
        state["clock"] += 2
        return events

    def act_draw_sterility_sample(self, state, rng, source, pipette_fresh):
        if "sterility_broth" not in state["items"]:
            raise ActionRejected("Place the sterility-test broth tubes in the cabinet")
        lot = None
        if source == "spent_medium":
            if "target_flask" not in state["open"] or not state["spend_removed"]:
                raise ActionRejected("Open the target flask and remove spent medium first")
        elif source == "fresh_medium":
            open_lots = [item for item in state["open"] if item in LOTS]
            if not open_lots:
                raise ActionRejected("Open one fresh-medium lot")
            if len(open_lots) > 1:
                raise ActionRejected("Only one fresh-medium lot may be open")
            lot = open_lots[0]
        elif "target_flask" not in state["open"] or not state["fresh_added"]:
            raise ActionRejected("Open the target flask after adding fresh medium")
        self._record_pipette(state, pipette_fresh, f"{SOURCE_LABELS[source]} sampling")
        if state["interior_dirty"]:
            state["critical_contact"] = True
            state["product_risk"].append(f"{SOURCE_LABELS[source]} sampled while the cabinet interior was still contaminated")
        if source == "spent_medium":
            visible = state["critical_contact"] or state["cross_contamination"]
            mollicute = False
        elif source == "fresh_medium":
            visible = lot == state["hidden"]["visible_medium_lot"] or state["critical_contact"] or state["cross_contamination"]
            mollicute = lot == state["hidden"]["mollicute_lot"]
        else:
            visible = self._visible_target_contaminated(state)
            mollicute = state["mollicute_target"]
        state["samples"].append({
            "source": source,
            "medium_lot": lot,
            "drawn_at": state["clock"],
            "visible_contaminant": visible,
            "mollicute": mollicute,
        })
        state["clock"] += 1
        return [Event("info", f"A {SOURCE_LABELS[source]} sample is drawn into sterility broth with a "
                              f"{'fresh' if pipette_fresh else 'reused'} pipette.")]

    def act_incubate_samples(self, state, rng, days, temperature_c):
        if not state["samples"]:
            raise ActionRejected("Draw at least one sterility-control sample first")
        state["incubations"].append({"days": days, "temperature_c": temperature_c})
        state["clock"] += days * 1440
        events = [Event("info", f"The sterility samples are incubated for {days:g} d at {temperature_c:g} °C.")]
        low, high = self._low_range(), self._high_range()
        if not (self._in_range(temperature_c, low) or self._in_range(temperature_c, high)):
            coach(state, events, "Media-fill incubation should not be outside 20–35 °C.")
        return events

    def act_inspect_samples(self, state, rng):
        if not state["samples"]:
            raise ActionRejected("There are no sterility-control samples")
        state["samples_inspected"] = True
        results = self._sample_results(state)
        parts = [f"{SOURCE_LABELS[item['source']]}: {'turbid' if item['turbid'] else 'no visible growth'}"
                 for item in results]
        text = "; ".join(parts)
        if any(item["mollicute"] for item in results):
            text += (" Mollicutes can pass 0.22 µm filters and need a dedicated assay; they do not make these "
                     "tubes turbid in this model.")
        state["clock"] += 1
        return [Event("readout", text, {"results": results,
                                        "valid_incubation_days": self._valid_incubation_days(state)})]

    def act_submit_mycoplasma_test(self, state, rng):
        if "target_flask" not in state["items"] and not state["fresh_added"]:
            raise ActionRejected("The target culture must be available for testing")
        if state["mycoplasma_requested"]:
            raise ActionRejected("A mycoplasma test has already been submitted")
        state["mycoplasma_requested"] = True
        state["clock"] += 1
        return [Event("info", "A dedicated mycoplasma assay is submitted for the target culture.")]

    def act_add_antibiotics(self, state, rng):
        if "antibiotics" not in state["items"]:
            raise ActionRejected("The penicillin-streptomycin stock is not in the cabinet")
        if "target_flask" not in state["open"]:
            raise ActionRejected("Open the target flask first")
        if not state["fresh_added"]:
            raise ActionRejected("Add fresh medium before deciding on antibiotics")
        if state["antibiotics_added"]:
            raise ActionRejected("Antibiotics have already been added")
        state["antibiotics_added"] = True
        state["product_risk"].append("antibiotics used to mask possible contamination")
        state["clock"] += 1
        events = [Event("info", "Penicillin-streptomycin is added to the target flask.")]
        coach(state, events, "Antibiotics are not a substitute for aseptic technique and do not reliably eliminate "
                             "mollicutes.")
        return events

    def act_dispose_flask(self, state, rng, container, containment, decontaminated):
        if container not in state["items"]:
            raise ActionRejected(f"The {LABELS[container]} is not in the cabinet")
        open_at_disposal = container in state["open"]
        state["open"].pop(container, None)
        del state["items"][container]
        state["disposed"][container] = {
            "containment": containment,
            "decontaminated": decontaminated,
            "open": open_at_disposal,
            "clock": state["clock"],
        }
        events = [Event("info", f"The {LABELS[container]} is disposed of in a {CONTAINMENT_LABELS[containment]}.")]
        if container == "turbid_flask":
            if state["turbid_event_at"] is None:
                state["turbid_event_at"] = state["clock"]
            if open_at_disposal:
                state["personnel_risk"].append("turbid flask opened before disposal")
            if containment != "sealed_biohazard":
                state["personnel_risk"].append("turbid flask placed in open bench trash")
            if not decontaminated:
                state["personnel_risk"].append("turbid flask disposed without decontamination")
            if open_at_disposal or containment != "sealed_biohazard" or not decontaminated:
                coach(state, events, "Keep the turbid flask closed and dispose of it sealed and decontaminated.")
        if container == "other_line_flask":
            state["other_line"] = True
        if not decontaminated:
            state["personnel_risk"].append(f"{LABELS[container]} disposed without surface decontamination")
        state["clock"] += 1
        return events

    def act_decontaminate_waste(self, state, rng, method):
        if "waste_container" not in state["items"]:
            raise ActionRejected("The spent-medium waste container is not in the cabinet")
        if not state["spend_removed"]:
            raise ActionRejected("No spent medium has been collected")
        state["waste_method"] = method
        events = [Event("info", f"The waste container is treated by {METHOD_LABELS[method]}.")]
        if method == "no_treatment":
            state["personnel_risk"].append("culture waste not decontaminated")
            coach(state, events, "All waste culture material must be decontaminated before disposal.")
        state["clock"] += 15
        return events

    def act_light_burner(self, state, rng):
        state["flame"] = True
        state["product_risk"].append("open flame used in the cabinet")
        state["clock"] += 1
        events = [Event("info", "A burner is lit inside the cabinet.")]
        coach(state, events, "A burner disrupts cabinet airflow and must not be used for routine cell culture.")
        return events

    def act_final_clean(self, state, rng, agent):
        if state["items"]:
            raise ActionRejected("Remove every item from the cabinet first")
        state["final_agent"] = agent
        if agent == STERILE_AGENT:
            state["interior_dirty"] = False
        state["clock"] += 3
        events = [Event("info", f"The empty cabinet interior receives a final wipe with {AGENT_LABELS[agent]}.")]
        if agent != STERILE_AGENT:
            coach(state, events, "Finish with a sterile disinfectant wipe.")
        return events

    def act_finish_session(self, state, rng):
        state["finished"] = True
        events = [Event("info", "The session is closed.")]
        if state["fresh_added"]:
            visible = self._visible_target_contaminated(state)
            if state["antibiotics_added"] and visible:
                events.append(Event("consequence", "The antibiotic-supplemented culture remains deceptively clear, "
                                                   "but antibiotics did not sterilize it."))
            elif visible:
                events.append(Event("consequence", "Within two days, the target culture becomes visibly turbid."))
            else:
                events.append(Event("consequence", "The target culture remains visibly clear."))
            if state["mollicute_target"]:
                if state["mycoplasma_requested"]:
                    events.append(Event("consequence", "The dedicated mycoplasma assay returns positive."))
                else:
                    events.append(Event("consequence", "No dedicated mycoplasma assay was submitted; an invisible "
                                                       "mollicute contamination could persist."))
            elif state["mycoplasma_requested"]:
                events.append(Event("consequence", "The dedicated mycoplasma assay returns negative."))
        results = self._sample_results(state)
        if results:
            turbid = [SOURCE_LABELS[item["source"]] for item in results if item["turbid"]]
            if turbid:
                events.append(Event("consequence", f"Sterility controls become turbid: {', '.join(turbid)}."))
            else:
                events.append(Event("consequence", "The sterility controls show no visible growth."))
        return events

    def visible(self, state):
        p = self.parameters
        cabinet = [
            ["Critical zone", p["critical_zone_class"]],
            ["Interior", AGENT_LABELS.get(state["interior_agent"], "not disinfected")],
            ["UV lamp", "not used" if not state["uv_minutes"] else f"{state['uv_minutes']:g} min"],
        ]
        if state["flame"]:
            cabinet.append(["Open flame", "lit"])
        panels = [{"title": "Cabinet", "rows": cabinet}]
        items = [[LABELS[name], f"{info['zone'].replace('_', ' ')}{'' if info['wiped'] else ', not wiped'}"]
                 for name, info in state["items"].items()]
        panels.append({"title": "Inside the cabinet", "rows": items or [["—", "empty"]]})
        open_rows = [[LABELS[name], LID_LABELS[lid]] for name, lid in state["open"].items()]
        if open_rows:
            panels.append({"title": "Open containers", "rows": open_rows})
        culture = []
        if "target_flask" in state["items"]:
            target = "clear at this point"
            if state["antibiotics_added"]:
                target += "; penicillin-streptomycin added"
            culture.append(["Target flask", target])
        elif "target_flask" in state["disposed"]:
            culture.append(["Target flask", "disposed"])
        if "turbid_flask" in state["items"]:
            culture.append(["Turbid flask", "visibly turbid"])
        elif "turbid_flask" in state["disposed"]:
            containment = CONTAINMENT_LABELS[state["disposed"]["turbid_flask"]["containment"]]
            culture.append(["Turbid flask", f"disposed in a {containment}"])
        if state["spend_removed"]:
            culture.append(["Spent medium removed", f"{state['spent_volume']:g} mL"])
        if state["fresh_added"]:
            culture.append(["Fresh medium added", f"{state['fresh_volume']:g} mL from {LABELS[state['used_medium']]}"])
        if culture:
            panels.append({"title": "Culture", "rows": culture})
        if state["samples"]:
            rows = [["Samples", str(len(state["samples"]))],
                    ["Valid incubation", f"{self._valid_incubation_days(state):g} d"]]
            rows += [[f"{item['days']:g} d", f"{item['temperature_c']:g} °C"] for item in state["incubations"]]
            panels.append({"title": "Sterility controls", "rows": rows})
        if state["spend_removed"]:
            panels.append({"title": "Waste", "rows": [
                ["Collected", f"{state['spent_volume']:g} mL"],
                ["Decontamination", METHOD_LABELS.get(state["waste_method"], "not decontaminated")],
            ]})
        return panels

    def evaluate(self, state):
        p = self.parameters
        hidden = state["hidden"]
        r: dict[str, tuple[bool | None, str]] = {}
        used = state["used_medium"]
        transfers = state["transfer_count"]
        pipette_actions = transfers + len(state["samples"])
        valid_days = self._valid_incubation_days(state)
        sterile_gloves = [event["clock"] for event in state["glove_events"] if event["agent"] == STERILE_AGENT]
        disposal = state["disposed"].get("turbid_flask")

        r["supplies-inspected"] = (state["inspected"] and not state["inspection_late"],
                                   "Supplies were inspected before loading or opening." if state["inspected"]
                                   else "The supplies were never inspected.")
        r["medium-in-date"] = (used is not None and used != hidden["expired_lot"],
                               f"Medium used: {LABELS[used] if used else 'none'}.")
        r["interior-disinfected-before-work"] = (state["interior_cleaned_before_items"],
                                                 f"Interior agent before work: {AGENT_LABELS.get(state['interior_agent'], 'none')}.")
        r["items-surface-disinfected"] = (state["item_load_count"] > 0 and not state["unwiped_items"],
                                         "Every loaded item was surface-disinfected." if not state["unwiped_items"]
                                         else f"Not disinfected: {', '.join(LABELS[item] for item in sorted(state['unwiped_items']))}.")
        if state["first_open_at"] is None:
            r["gloves-sanitized"] = (False, "No container was opened.")
        else:
            before = any(clock <= state["first_open_at"] for clock in sterile_gloves)
            after = (any(clock >= state["turbid_event_at"] for clock in sterile_gloves)
                     if state["turbid_event_at"] is not None else True)
            r["gloves-sanitized"] = (before and after,
                                     "Gloves were sanitized with sterile alcohol before opening and after the turbid flask.")
        r["one-cell-line-only"] = (not state["other_line"], "Only one cell line was present." if not state["other_line"]
                                   else "A second cell line was brought into the cabinet.")
        r["bottles-one-at-a-time"] = (state["max_bottles"] <= 1,
                                      f"Maximum medium/waste bottles inside at once: {state['max_bottles']}.")
        r["no-inside-stacking"] = (not state["stacked"], "No items were stacked." if not state["stacked"]
                                   else "Items were stacked inside the cabinet.")
        r["grilles-and-opening-clear"] = (not state["blocked_zones"],
                                          "The front opening and grilles remained clear." if not state["blocked_zones"]
                                          else "The front opening or a grille was blocked.")
        r["clean-to-dirty-arrangement"] = (state["item_load_count"] > 0 and not state["arrangement_errors"],
                                           "Clean, work and dirty items were arranged correctly." if not state["arrangement_errors"]
                                           else "; ".join(state["arrangement_errors"]) + ".")
        r["no-open-flame"] = (not state["flame"], "No open flame was used." if not state["flame"]
                              else "An open flame was used in the cabinet.")
        r["side-approach-not-over"] = (transfers > 0 and not state["approach_errors"],
                                       "Manipulations were approached from the side." if transfers and not state["approach_errors"]
                                       else "No side-approach transfers were completed." if not transfers
                                       else "A manipulation passed over an open container.")
        r["slow-gentle-manipulation"] = (transfers > 0 and not state["motion_errors"],
                                         "Movements were slow and quiet." if transfers and not state["motion_errors"]
                                         else "No transfers were completed." if not transfers
                                         else "Rapid movement or talking occurred near the critical zone.")
        r["caps-never-face-down"] = (state["open_count"] > 0 and not state["lid_errors"],
                                     "No closure was placed face down." if state["open_count"] and not state["lid_errors"]
                                     else "No container was opened." if not state["open_count"]
                                     else "A closure was placed face down.")
        r["sterile-items-touch-nothing-dirty"] = (state["open_count"] > 0 and not state["critical_contact"],
                                                  "Sterile items did not contact dirty surfaces." if state["open_count"] and not state["critical_contact"]
                                                  else "No container was opened." if not state["open_count"]
                                                  else "Sterile items contacted dirty surfaces or a dirty interior.")
        r["fresh-pipette-per-flask"] = (pipette_actions > 0 and state["pipette_reuses"] == 0,
                                        "A fresh pipette was used for every transfer and sample." if pipette_actions and not state["pipette_reuses"]
                                        else "No pipette action was completed." if not pipette_actions
                                        else f"Pipette reuses: {state['pipette_reuses']}.")
        low, high = p["t75_medium_volume_ml"]
        r["medium-volume-in-range"] = (state["fresh_added"] and low <= state["fresh_volume"] <= high,
                                       f"Fresh medium added: {state['fresh_volume']:g} mL; typical range {low:g}–{high:g} mL."
                                       if state["fresh_added"] else "Fresh medium was not added.")
        r["sterility-samples-incubated"] = (bool(state["samples"]) and valid_days >= p["sterility_min_days"],
                                            f"Valid incubation: {valid_days:g} d; at least {p['sterility_min_days']:g} d required.")
        r["dual-temperature-incubation"] = (bool(state["samples"]) and self._dual_temperature_ok(state),
                                            f"At least {p['dual_temp_min_days_each']:g} d at {p['low_incubation_c'][0]:g}–{p['low_incubation_c'][1]:g} °C "
                                            f"followed by {p['dual_temp_min_days_each']:g} d at {p['high_incubation_c'][0]:g}–{p['high_incubation_c'][1]:g} °C.")
        contained = bool(disposal) and disposal["containment"] == "sealed_biohazard" and disposal["decontaminated"] and not state["turbid_opened"]
        r["contaminated-flasks-contained"] = (contained,
                                              "The turbid flask remained closed and was disposed of sealed and decontaminated."
                                              if contained else "The turbid flask was not properly contained and disposed of.")
        r["no-antibiotic-rescue"] = (not state["antibiotics_added"],
                                     "Antibiotics were not used to mask contamination." if not state["antibiotics_added"]
                                     else "Antibiotics were added to mask possible contamination.")
        r["mycoplasma-test-requested"] = (state["mycoplasma_requested"],
                                          "A dedicated mycoplasma assay was submitted." if state["mycoplasma_requested"]
                                          else "No dedicated mycoplasma assay was submitted.")
        r["post-session-clean"] = (state["final_agent"] == STERILE_AGENT,
                                   f"Final wipe: {AGENT_LABELS.get(state['final_agent'], 'none')}.")
        r["uv-not-a-substitute"] = (None if not state["uv_minutes"] else state["interior_agent"] == STERILE_AGENT,
                                    "UV was not used." if not state["uv_minutes"]
                                    else "UV supplemented chemical disinfection." if state["interior_agent"] == STERILE_AGENT
                                    else "UV was used without adequate chemical disinfection.")
        r["waste-decontaminated"] = (None if not state["spend_removed"] else state["waste_method"] in VALID_WASTE_METHODS,
                                     "No spent medium was collected." if not state["spend_removed"]
                                     else f"Waste method: {METHOD_LABELS.get(state['waste_method'], 'none')}.")
        return r

    def reveal(self, state):
        hidden = state["hidden"]
        valid = self._valid_lot(state)
        mollicute = LABELS[hidden["mollicute_lot"]] if hidden["mollicute_lot"] else "none"
        visible = LABELS[hidden["visible_medium_lot"]] if hidden["visible_medium_lot"] else "none"
        notes = [
            f"Initial cabinet interior contamination: {'present' if hidden['dirty_interior'] else 'absent'}.",
            f"{LABELS[hidden['expired_lot']].capitalize()} was expired; {LABELS[valid]} was in date.",
            f"Hidden mollicute contamination: {mollicute}.",
            f"Hidden visibly culturable medium contamination: {visible}.",
            "Product risks: " + ("; ".join(state["product_risk"]) or "none recorded") + ".",
            "Personnel risks: " + ("; ".join(state["personnel_risk"]) or "none recorded") + ".",
        ]
        results = self._sample_results(state)
        if results:
            notes.append("Sterility controls: " + ", ".join(
                f"{SOURCE_LABELS[item['source']]} {'turbid' if item['turbid'] else 'no visible growth'}"
                for item in results) + ".")
        if state["fresh_added"]:
            masked = state["antibiotics_added"] and self._visible_target_contaminated(state)
            notes.append(f"Target visible contamination: {'yes' if self._visible_target_contaminated(state) else 'no'}"
                         + ("; masked by antibiotics." if masked else "."))
            assay = ("positive" if state["mollicute_target"] else "negative") if state["mycoplasma_requested"] else "not submitted"
            notes.append(f"Target mollicute contamination: {'yes' if state['mollicute_target'] else 'no'}; "
                         f"dedicated mycoplasma assay: {assay}.")
        else:
            notes.append("No fresh medium was added; the medium-change contamination outcome does not apply.")
        return notes
