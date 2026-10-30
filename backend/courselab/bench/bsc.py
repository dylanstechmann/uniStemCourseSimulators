"""Working in a Class II biological safety cabinet, including a spill during the work."""

from __future__ import annotations

from .engine import ActionRejected, Event, ProtocolModel, coach

NEEDED = {"culture", "media", "plates", "pipettes", "pipette_aid", "discard_tray", "biohazard_bag"}
BULKY = {"discard_tray", "biohazard_bag"}
NAMES = {
    "culture": "BSL-2 culture", "media": "media bottle", "plates": "fresh culture plates",
    "pipettes": "sterile serological pipettes", "pipette_aid": "pipette aid",
    "discard_tray": "horizontal discard tray with disinfectant", "biohazard_bag": "biohazard bag",
    "vortex": "vortex mixer", "extra_gloves": "spare box of gloves", "upright_canister": "upright pipette canister",
}
WORK_STEPS = 3


class BiosafetyCabinetSession(ProtocolModel):
    protocol_id = "class-ii-bsc-session-with-spill"

    def checkpoint_ids(self):
        return [
            "certification-checked", "certification-current", "ppe", "purge-before-loading",
            "interior-disinfected", "bleach-rinsed", "drain-valve-closed", "toweling-placement",
            "items-wiped", "biological-last", "only-needed-items", "bulky-to-side", "aerosol-equipment-rear",
            "no-outside-bag", "sash-at-certified-height", "arms-slow", "arms-settle", "work-four-inches",
            "no-open-flame", "uv-not-sole", "spill-covered-outside-in", "spill-contact-time",
            "spill-towels-edge-to-center", "spill-biohazard-disposal", "spill-gloves-changed",
            "large-spill-drain", "teardown-blower-running", "teardown-biological-first", "final-wipe",
            "ppe-off-handwash",
        ]

    def start(self, rng):
        p = self.parameters
        expired = rng.random() < p["expired_certification_probability"]
        months = rng.randint(13, 20) if expired else rng.randint(2, 11)
        return {
            "hidden": {
                "months_since_certification": months, "expired": months > p["certification_interval_months"],
                "drain_open": rng.random() < 0.5,
                "spill_size": "large" if rng.random() < p["large_spill_probability"] else "small",
                "spill_step": rng.randint(1, 2), "product_risk": [], "personnel_risk": [],
            },
            "inspected": False, "out_of_service": False, "ppe": None, "blower_on_at": None, "blower_off_events": 0,
            "sash": "closed", "sash_during_work": set(), "surface_agent": None, "bleach_unrinsed": False,
            "toweling": None, "items": {}, "load_order": [], "loaded_before_purge": False,
            "arms_in_at": None, "arm_motions": [], "settled_each_entry": [], "flame": False, "uv_minutes": 0.0,
            "work_done": 0, "work_distances": [], "spill": None, "removed": [], "final_wipe": None,
            "ppe_removed": False, "hands_washed": False, "ppe_removed_before_wash": None,
        }

    # Helpers -------------------------------------------------------------------

    def _purged(self, state):
        return state["blower_on_at"] is not None and state["clock"] - state["blower_on_at"] >= self.parameters["purge_min"]

    def _spill_open(self, state):
        spill = state["spill"]
        return spill is not None and not spill.get("resolved")

    def _resolve_if_done(self, state):
        spill = state["spill"]
        if spill and spill.get("discarded") and spill.get("wiped") and (
                spill["size"] == "small" or spill.get("drained")):
            spill["resolved"] = True

    # Set-up --------------------------------------------------------------------

    def act_inspect_cabinet(self, state, rng):
        state["inspected"] = True
        hidden = state["hidden"]
        state["clock"] += 1
        return [Event("readout", f"Certification label: last field-certified {hidden['months_since_certification']} "
                                 f"months ago. Drain valve: {'open' if hidden['drain_open'] else 'closed'}. "
                                 f"Sash: {state['sash']}.",
                      {"months_since_certification": hidden["months_since_certification"],
                       "drain_valve": "open" if hidden["drain_open"] else "closed"})]

    def act_report_out_of_service(self, state, rng):
        state["out_of_service"] = True
        state["finished"] = True
        return [Event("info", "The cabinet is tagged out of service and the biosafety officer is notified.")]

    def act_don_ppe(self, state, rng, coat_buttoned, gloves):
        state["ppe"] = {"coat": coat_buttoned, "gloves": gloves}
        state["clock"] += 1
        events = [Event("info", "PPE put on.")]
        if not (coat_buttoned and gloves):
            coach(state, events, "Wear a buttoned laboratory coat and gloves for BSL-2 work.")
        return events

    def act_blower(self, state, rng, on):
        if on and state["blower_on_at"] is None:
            state["blower_on_at"] = state["clock"]
            return [Event("info", "The cabinet blower is switched on.")]
        if not on and state["blower_on_at"] is not None:
            state["blower_on_at"] = None
            state["blower_off_events"] += 1
            return [Event("info", "The cabinet blower is switched off.")]
        raise ActionRejected("The blower is already in that state")

    def act_set_sash(self, state, rng, position):
        state["sash"] = position
        events = [Event("info", f"Sash moved to the {position} position.")]
        if position == "raised" and state["blower_on_at"] is not None:
            events.append(Event("warning", "The airflow alarm sounds: the sash is above its certified height."))
        return events

    def act_wait(self, state, rng, minutes):
        state["clock"] += minutes
        text = f"{minutes:g} min pass."
        if self._spill_open(state) and state["spill"].get("applied_at") is not None:
            text += f" The spill has had {self._contact(state):.0f} min of contact with disinfectant."
        return [Event("info", text)]

    def _contact(self, state):
        spill = state["spill"]
        return 0.0 if spill.get("applied_at") is None else state["clock"] - spill["applied_at"]

    def act_close_drain_valve(self, state, rng):
        state["hidden"]["drain_open"] = False
        return [Event("info", "The drain valve under the work surface is closed.")]

    def act_disinfect_interior(self, state, rng, agent):
        if state["items"]:
            raise ActionRejected("Disinfect the empty cabinet before loading it")
        state["surface_agent"] = agent
        state["bleach_unrinsed"] = agent == "bleach"
        state["clock"] += 3
        events = [Event("info", "Work surface, interior walls and the inside of the window wiped down.")]
        if agent == "water":
            coach(state, events, "Non-sterile water is not a disinfectant and may recontaminate the surfaces.")
        return events

    def act_rinse_sterile_water(self, state, rng):
        state["bleach_unrinsed"] = False
        state["clock"] += 2
        return [Event("info", "Surfaces wiped a second time with sterile water.")]

    def act_lay_toweling(self, state, rng, location):
        state["toweling"] = location
        events = [Event("info", f"Plastic-backed absorbent toweling laid on the {location.replace('_', ' ')}.")]
        if location == "front_grille":
            state["hidden"]["product_risk"].append("toweling over the front grille")
            state["hidden"]["personnel_risk"].append("toweling over the front grille")
            coach(state, events, "Toweling over the grille blocks the air that keeps the cabinet contained.")
        return events

    def act_load_item(self, state, rng, item, zone, wiped):
        if item in state["items"]:
            raise ActionRejected(f"The {NAMES[item]} is already in place")
        if state["blower_on_at"] is None:
            raise ActionRejected("Switch the blower on before loading the cabinet")
        if self._spill_open(state):
            raise ActionRejected("Deal with the spill first")
        events = [Event("info", f"The {NAMES[item]} is placed at the {zone.replace('_', ' ')}.")]
        if not self._purged(state):
            state["loaded_before_purge"] = True
            coach(state, events, f"Run the blower at least {self.parameters['purge_min']:g} min before starting work.")
        if not wiped:
            state["hidden"]["product_risk"].append(f"unwiped {NAMES[item]}")
            coach(state, events, "Wipe each item with disinfectant before it goes in.")
        if zone == "front_grille":
            state["hidden"]["personnel_risk"].append(f"{NAMES[item]} on the front grille")
            coach(state, events, "Nothing may rest on the front grille.")
        state["items"][item] = {"zone": zone, "wiped": wiped}
        state["load_order"].append(item)
        state["clock"] += 0.5
        return events

    def act_insert_arms(self, state, rng, motion):
        state["arms_in_at"] = state["clock"]
        state["arm_motions"].append(motion)
        state["settled_each_entry"].append(False)
        events = [Event("info", f"Arms moved into the cabinet ({motion.replace('_', ' ')}).")]
        if motion == "sweeping":
            state["hidden"]["product_risk"].append("sweeping arm movement")
            coach(state, events, "Move arms in and out slowly, perpendicular to the opening.")
        return events

    def act_settle(self, state, rng, seconds):
        if state["arms_in_at"] is None:
            raise ActionRejected("Your arms are not in the cabinet")
        state["clock"] += seconds / 60
        if seconds >= self.parameters["arm_settle_s"]:
            state["settled_each_entry"][-1] = True
        return [Event("info", f"You hold still for {seconds:g} s while the airflow stabilizes.")]

    def act_withdraw_arms(self, state, rng):
        if state["arms_in_at"] is None:
            raise ActionRejected("Your arms are not in the cabinet")
        state["arms_in_at"] = None
        return [Event("info", "Arms withdrawn slowly.")]

    def act_light_burner(self, state, rng):
        state["flame"] = True
        state["hidden"]["product_risk"].append("open flame disrupting the airflow")
        events = [Event("info", "A Bunsen burner is lit inside the cabinet.")]
        coach(state, events, "Open flames are not recommended in a BSC: they disrupt the HEPA-filtered airflow.")
        return events

    def act_uv_lamp(self, state, rng, minutes):
        if state["arms_in_at"] is not None:
            raise ActionRejected("Withdraw your arms before using the UV lamp")
        state["uv_minutes"] += minutes
        state["clock"] += minutes
        return [Event("info", f"The UV lamp runs for {minutes:g} min with the sash closed.")]

    # Work and spill ------------------------------------------------------------

    def act_work_step(self, state, rng, distance_in, lids_over_plates):
        p = self.parameters
        if state["arms_in_at"] is None:
            raise ActionRejected("Put your arms in the cabinet first")
        if not {"culture", "plates", "pipettes", "pipette_aid"} <= set(self._remaining(state)):
            raise ActionRejected("The culture, plates, pipettes and pipette aid must be in the cabinet")
        if self._spill_open(state):
            raise ActionRejected("Deal with the spill first")
        if state["work_done"] >= WORK_STEPS:
            raise ActionRejected("The subculture is complete")
        if state["work_done"] == 0:
            state["drain_open_at_start"] = state["hidden"]["drain_open"]
        state["work_done"] += 1
        state["work_distances"].append(distance_in)
        state["sash_during_work"].add(state["sash"])
        state["clock"] += 4
        events = [Event("info", f"Subculture step {state['work_done']} of {WORK_STEPS} done "
                                f"{distance_in:g} in behind the front grille.")]
        if distance_in < p["min_distance_in"]:
            state["hidden"]["personnel_risk"].append("work too close to the front grille")
            coach(state, events, f"Work at least {p['min_distance_in']:g} in behind the front grille.")
        if state["sash"] != "certified":
            state["hidden"]["personnel_risk"].append(f"work with the sash {state['sash']}")
            coach(state, events, "Work only with the sash at its certified height.")
        if not lids_over_plates:
            state["hidden"]["product_risk"].append("open plates exposed to the downflow")
            coach(state, events, "Hold lids above open plates to shield them from the downward air.")
        if state["work_done"] == state["hidden"]["spill_step"] and state["spill"] is None:
            size = state["hidden"]["spill_size"]
            state["spill"] = {"size": size}
            text = ("A tube slips: about 2 mL of culture splashes onto the work surface." if size == "small" else
                    "The culture flask tips over: about 50 mL of culture floods the work surface and runs "
                    "through the front and rear grilles.")
            events.append(Event("consequence", text, {"spill": size}))
            if size == "large" and state["hidden"]["drain_open"]:
                events.append(Event("consequence", "Liquid drips from under the cabinet: the drain valve is open."))
                state["hidden"]["personnel_risk"].append("culture leaking through the open drain valve")
        return events

    def _need_spill(self, state):
        if state["spill"] is None or state["spill"].get("resolved"):
            raise ActionRejected("There is no spill to deal with")
        return state["spill"]

    def act_cover_spill(self, state, rng):
        spill = self._need_spill(state)
        spill["covered"] = True
        state["clock"] += 1
        return [Event("info", "The spill is covered with paper towels.")]

    def act_apply_disinfectant(self, state, rng, direction):
        spill = self._need_spill(state)
        if spill.get("applied_at") is None:
            spill["applied_at"] = state["clock"]
            spill["direction"] = direction
            spill["covered_first"] = spill.get("covered", False)
        state["clock"] += 1
        events = [Event("info", f"Disinfectant poured over the spill, working {direction.replace('_', ' ')}.")]
        if direction == "center_out":
            coach(state, events, "Start at the outside of the spill so you do not spread it.")
        return events

    def act_push_towels(self, state, rng, direction):
        spill = self._need_spill(state)
        if spill.get("applied_at") is None:
            raise ActionRejected("Apply disinfectant first")
        spill["contact_min"] = self._contact(state)
        spill["push_direction"] = direction
        state["clock"] += 1
        events = [Event("info", f"Towels gathered {direction.replace('_', ' ')}.")]
        if spill["contact_min"] < self.parameters["spill_contact_min"][0]:
            coach(state, events, f"Only {spill['contact_min']:.0f} min of contact; leave the disinfectant "
                                 "20–30 min first.")
        return events

    def act_discard_towels(self, state, rng, into):
        spill = self._need_spill(state)
        if spill.get("push_direction") is None:
            raise ActionRejected("Gather the towels first")
        spill["discarded"] = into
        state["clock"] += 0.5
        events = [Event("info", f"Towels discarded into the {into.replace('_', ' ')}.")]
        if into != "biohazard_bag":
            state["hidden"]["personnel_risk"].append("spill towels in ordinary waste")
            coach(state, events, "Spill towels go into the biohazard bag.")
        self._resolve_if_done(state)
        return events

    def act_wipe_down_interior(self, state, rng):
        spill = self._need_spill(state)
        spill["wiped"] = True
        spill["wiped_at"] = state["clock"]
        state["clock"] += 2
        self._resolve_if_done(state)
        return [Event("info", "Cabinet interior and the items inside wiped with a disinfectant-dampened towel.")]

    def act_flood_drain_pan(self, state, rng):
        spill = self._need_spill(state)
        if spill["size"] != "large":
            raise ActionRejected("The spill has not reached the grilles")
        if self._remaining(state):
            raise ActionRejected("Surface-decontaminate and remove every item before flooding the drain pan")
        spill["flooded_with_drain_open"] = state["hidden"]["drain_open"]
        spill["flooded"] = True
        state["clock"] += 2
        events = [Event("info", "Disinfectant poured onto the work surface and through the grilles into the drain pan.")]
        if state["hidden"]["drain_open"]:
            state["hidden"]["personnel_risk"].append("disinfectant and culture draining onto the floor")
            events.append(Event("consequence", "Liquid runs out of the open drain valve onto the floor."))
        return events

    def act_drain_to_disinfectant(self, state, rng):
        spill = self._need_spill(state)
        if not spill.get("flooded"):
            raise ActionRejected("Flood the drain pan with disinfectant first")
        spill["drained"] = True
        state["clock"] += 5
        self._resolve_if_done(state)
        return [Event("info", "Drain pan emptied through a tube submerged in a collection vessel of disinfectant, "
                              "then flushed with water and the valve closed.")]

    def act_change_gloves(self, state, rng):
        spill = state["spill"]
        if spill is not None and spill.get("wiped") and spill.get("gloves_changed_after") is None:
            spill["gloves_changed_after"] = True
        state["clock"] += 0.5
        return [Event("info", "Gloves changed.")]

    # Teardown ------------------------------------------------------------------

    def _remaining(self, state):
        return [item for item in state["items"] if item not in {r["item"] for r in state["removed"]}]

    def act_remove_item(self, state, rng, item, decontaminated):
        if item not in self._remaining(state):
            raise ActionRejected(f"The {NAMES[item]} is not in the cabinet")
        state["removed"].append({"item": item, "decontaminated": decontaminated,
                                 "blower_on": state["blower_on_at"] is not None})
        state["clock"] += 0.5
        events = [Event("info", f"The {NAMES[item]} is removed.")]
        if not decontaminated:
            state["hidden"]["personnel_risk"].append(f"{NAMES[item]} removed without surface decontamination")
            coach(state, events, "Surface-decontaminate items before taking them out.")
        return events

    def act_final_wipe(self, state, rng, agent):
        if self._remaining(state):
            raise ActionRejected("Remove everything from the cabinet first")
        state["final_wipe"] = agent
        state["clock"] += 3
        return [Event("info", "Work surface, sides, back and the inside of the glass wiped down.")]

    def act_remove_ppe(self, state, rng):
        state["ppe_removed"] = True
        state["clock"] += 1
        return [Event("info", "Gloves and coat removed without touching the outer surfaces.")]

    def act_wash_hands(self, state, rng):
        state["hands_washed"] = True
        state["ppe_removed_before_wash"] = state["ppe_removed"]
        state["clock"] += 1
        return [Event("info", "Hands washed.")]

    def act_end_session(self, state, rng):
        state["finished"] = True
        events = [Event("info", "The session is closed.")]
        risk = state["hidden"]["product_risk"]
        if state["work_done"]:
            if len(risk) >= 2 or (risk and rng.random() < 0.5):
                events.append(Event("consequence", "Two days later, mould and bacterial colonies appear on several "
                                                   "of the new plates."))
            else:
                events.append(Event("consequence", "Two days later, the new plates show only the expected growth."))
        return events

    # Views and evaluation ------------------------------------------------------

    def visible(self, state):
        blower = "off" if state["blower_on_at"] is None else f"on for {state['clock'] - state['blower_on_at']:.1f} min"
        cabinet = [
            ["Blower", blower], ["Sash", state["sash"]],
            ["Surfaces", "not yet disinfected" if state["surface_agent"] is None else f"wiped with {state['surface_agent']}"],
            ["Toweling", "none" if state["toweling"] is None else state["toweling"].replace("_", " ")],
            ["Arms", "in the cabinet" if state["arms_in_at"] is not None else "outside"],
            ["Subculture", f"{state['work_done']} of {WORK_STEPS} steps done"],
        ]
        if state["inspected"]:
            cabinet.insert(0, ["Certification label", f"{state['hidden']['months_since_certification']} months ago"])
        items = [[NAMES[name], f"{info['zone'].replace('_', ' ')}{'' if info['wiped'] else ', not wiped'}"]
                 for name, info in state["items"].items() if name not in {r["item"] for r in state["removed"]}]
        panels = [{"title": "Cabinet", "rows": cabinet}, {"title": "Inside the cabinet", "rows": items or [["—", "empty"]]}]
        spill = state["spill"]
        if spill is not None and not spill.get("resolved"):
            status = []
            if spill.get("covered"):
                status.append("covered with towels")
            if spill.get("applied_at") is not None:
                status.append(f"disinfectant contact {self._contact(state):.0f} min")
            panels.append({"title": "Spill", "rows": [["Size", spill["size"]], ["Status", ", ".join(status) or "untreated"]]})
        return panels

    def evaluate(self, state):
        p = self.parameters
        hidden = state["hidden"]
        r: dict[str, tuple[bool | None, str]] = {}
        r["certification-checked"] = (state["inspected"], "The certification label was read before use."
                                      if state["inspected"] else "The certification label was never checked.")
        if hidden["expired"]:
            ok = state["out_of_service"] and state["work_done"] == 0
            r["certification-current"] = (ok, f"The cabinet was {hidden['months_since_certification']} months past "
                                              "certification; it must not be used until recertified.")
        else:
            r["certification-current"] = (not state["out_of_service"],
                                          f"The cabinet was certified {hidden['months_since_certification']} months ago "
                                          "and was fit for use.")
        if state["out_of_service"]:
            for key in self.checkpoint_ids():
                r.setdefault(key, (None, "Not applicable: the cabinet was taken out of service."))
            return r
        ppe = state["ppe"]
        r["ppe"] = (bool(ppe) and ppe["coat"] and ppe["gloves"], "A buttoned coat and gloves are required.")
        r["purge-before-loading"] = (bool(state["items"]) and not state["loaded_before_purge"],
                                     f"Run the blower at least {p['purge_min']:g} min before loading.")
        r["interior-disinfected"] = (state["surface_agent"] in ("ethanol70", "bleach"),
                                     f"Interior wiped with: {state['surface_agent'] or 'nothing'}.")
        r["bleach-rinsed"] = ((not state["bleach_unrinsed"]) if state["surface_agent"] == "bleach" else None,
                              "Bleach needs a second wipe with sterile water to remove residual chlorine.")
        opened = state.get("drain_open_at_start")
        r["drain-valve-closed"] = ((not opened) if state["work_done"] else None,
                                   "The drain valve should be closed before work begins.")
        r["toweling-placement"] = (state["toweling"] != "front_grille",
                                   "Toweling may cover the work surface but never the grilles.")
        items = state["items"]
        r["items-wiped"] = (bool(items) and all(info["wiped"] for info in items.values()),
                            "Every item should be wiped with disinfectant before it goes in.")
        order = state["load_order"]
        r["biological-last"] = (("culture" in order and order[-1] == "culture") if order else False,
                                "Biological material is placed in the cabinet last.")
        extra = sorted(set(items) - NEEDED - {"vortex"})
        r["only-needed-items"] = (not extra, "Only what the work needs goes in." if not extra
                                  else f"Not needed inside: {', '.join(NAMES[e] for e in extra)}.")
        bulky = [name for name in BULKY if name in items]
        r["bulky-to-side"] = ((all(items[name]["zone"] == "side" for name in bulky)) if bulky else None,
                              "The discard tray and biohazard bag belong to one side of the interior.")
        r["aerosol-equipment-rear"] = ((items["vortex"]["zone"] == "rear") if "vortex" in items else None,
                                       "Aerosol-generating equipment goes toward the rear.")
        bag = items.get("biohazard_bag")
        r["no-outside-bag"] = ((bag["zone"] != "outside_taped") if bag else None,
                               "The biohazard bag must not be taped to the outside of the cabinet.")
        r["sash-at-certified-height"] = (bool(state["work_done"]) and state["sash_during_work"] == {"certified"},
                                         f"Sash positions during work: {sorted(state['sash_during_work']) or ['no work']}.")
        motions = state["arm_motions"]
        r["arms-slow"] = (bool(motions) and all(m == "slow_perpendicular" for m in motions),
                          "Arms should move in and out slowly, perpendicular to the opening.")
        settled = state["settled_each_entry"]
        r["arms-settle"] = (bool(settled) and all(settled),
                            f"Wait about {p['arm_settle_s']:g} s after putting your arms in before working.")
        dist = state["work_distances"]
        r["work-four-inches"] = (bool(dist) and min(dist) >= p["min_distance_in"],
                                 f"Closest work: {min(dist) if dist else 0:g} in from the front grille; at least "
                                 f"{p['min_distance_in']:g} in is required.")
        r["no-open-flame"] = (not state["flame"], "No open flame was used." if not state["flame"]
                              else "An open flame was used inside the cabinet.")
        r["uv-not-sole"] = ((state["surface_agent"] in ("ethanol70", "bleach")) if state["uv_minutes"] else None,
                            "UV may supplement but never replace chemical disinfection.")
        spill = state["spill"]
        if spill is None:
            for key in ("spill-covered-outside-in", "spill-contact-time", "spill-towels-edge-to-center",
                        "spill-biohazard-disposal", "spill-gloves-changed", "large-spill-drain"):
                r[key] = (None, "No spill occurred in this run.")
        else:
            r["spill-covered-outside-in"] = (bool(spill.get("covered_first")) and spill.get("direction") == "outside_in",
                                             "Cover with towels, then pour disinfectant starting from the outside.")
            low, high = p["spill_contact_min"]
            contact = spill.get("contact_min")
            r["spill-contact-time"] = (contact is not None and contact >= low,
                                       f"Contact time before gathering: {contact or 0:.0f} min; usually {low}–{high} min.")
            r["spill-towels-edge-to-center"] = (spill.get("push_direction") == "edge_to_center",
                                                "Push towels from the edge of the spill to the centre.")
            r["spill-biohazard-disposal"] = (spill.get("discarded") == "biohazard_bag",
                                             "Spill towels go into the biohazard bag.")
            r["spill-gloves-changed"] = (bool(spill.get("gloves_changed_after")),
                                         "Change gloves after the surface is decontaminated.")
            if spill["size"] == "large":
                r["large-spill-drain"] = (bool(spill.get("drained")) and not spill.get("flooded_with_drain_open"),
                                          "With the drain valve closed, flood the drain pan with disinfectant and "
                                          "empty it into a vessel of disinfectant.")
            else:
                r["large-spill-drain"] = (None, "The spill stayed on the work surface.")
        removed = state["removed"]
        r["teardown-blower-running"] = (bool(removed) and all(x["blower_on"] and x["decontaminated"] for x in removed),
                                        "Decontaminate and remove items with the blower running.")
        r["teardown-biological-first"] = ((removed[0]["item"] == "culture") if removed and "culture" in items else None,
                                          "Biological materials come out first.")
        r["final-wipe"] = (state["final_wipe"] in ("ethanol70", "bleach"),
                           "End with a wipe of the work surface, sides, back and glass.")
        r["ppe-off-handwash"] = (state["hands_washed"] and bool(state["ppe_removed_before_wash"]),
                                 "Remove gloves and coat, then wash hands as the final step.")
        return r

    def reveal(self, state):
        hidden = state["hidden"]
        notes = [f"Spill planned for step {hidden['spill_step']} ({hidden['spill_size']})."]
        notes.append("Risks to the culture: " + ("; ".join(hidden["product_risk"]) or "none recorded") + ".")
        notes.append("Risks to you and the room: " + ("; ".join(hidden["personnel_risk"]) or "none recorded") + ".")
        return notes
