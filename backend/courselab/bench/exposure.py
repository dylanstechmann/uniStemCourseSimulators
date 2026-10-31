"""The first minutes after an exposure to human cell material: decontaminate, secure, report, document."""

from __future__ import annotations

from .engine import ActionRejected, Event, ProtocolModel, coach

EXPOSURES = {
    "needlestick": "A used needle slips while you aspirate medium from a flask of primary human cells and punctures your gloved finger.",
    "eye-splash": "Medium from a tube of primary human cells splashes into your eye as you open it outside the cabinet.",
    "cut": "A glass Pasteur pipette used with primary human cells breaks and cuts your hand through the glove.",
}
SKIN = {"needlestick", "cut"}


class ExposureResponse(ProtocolModel):
    protocol_id = "exposure-incident-first-response"

    def checkpoint_ids(self):
        return ["decontaminate-immediately", "right-method", "flush-duration", "secure-material", "report-immediately",
                "occupational-health", "document-route", "identify-source", "incident-record", "no-return-before-report"]

    def start(self, rng):
        return {"hidden": {"exposure": rng.choice(sorted(EXPOSURES))}, "announced": False, "washed": None, "flushed": None,
                "secured": None, "reported": None, "occ_health": None, "route_documented": False, "source_documented": False,
                "record": False, "returned_before_report": False, "returned": False}

    def _announce(self, state, events):
        if not state["announced"]:
            state["announced"] = True
            events.insert(0, Event("consequence", EXPOSURES[state["hidden"]["exposure"]], {"exposure": state["hidden"]["exposure"]}))

    def act_begin_work(self, state, rng):
        if state["announced"]:
            raise ActionRejected("The incident has already happened")
        events = [Event("info", "You start passaging the culture.")]
        self._announce(state, events)
        return events

    def _need_incident(self, state):
        if not state["announced"]:
            raise ActionRejected("Begin the work first")

    def act_wash_with_soap_and_water(self, state, rng, seconds):
        self._need_incident(state)
        state["washed"] = {"at": state["clock"], "seconds": seconds}
        state["clock"] += seconds / 60
        events = [Event("info", f"The area is washed with soap and running water for {seconds:g} s.")]
        if state["hidden"]["exposure"] not in SKIN:
            coach(state, events, "For an eye splash, flush the eye with water at the eyewash.")
        return events

    def act_flush_at_eyewash(self, state, rng, minutes):
        self._need_incident(state)
        state["flushed"] = {"at": state["clock"], "minutes": minutes}
        state["clock"] += minutes
        events = [Event("info", f"The eye is flushed at the eyewash for {minutes:g} min, holding the eyelids open.")]
        if state["hidden"]["exposure"] in SKIN:
            coach(state, events, "A wound or skin exposure is washed with soap and water.")
        return events

    def act_secure_material(self, state, rng):
        self._need_incident(state)
        state["secured"] = state["clock"]
        state["clock"] += 1
        return [Event("info", "The flask is capped, sharps go into the sharps container, and the area is marked so no one else is exposed.")]

    def act_notify_supervisor(self, state, rng):
        self._need_incident(state)
        state["reported"] = state["clock"]
        state["clock"] += 2
        return [Event("info", "Your supervisor is told what happened and takes over making the area safe.")]

    def act_contact_occupational_health(self, state, rng):
        self._need_incident(state)
        state["occ_health"] = state["clock"]
        state["clock"] += 5
        events = [Event("info", "Occupational health arranges a confidential medical evaluation straight away.")]
        if state["reported"] is None:
            coach(state, events, "Tell your supervisor as well; both must know at once.")
        return events

    def act_document_route_and_circumstances(self, state, rng):
        self._need_incident(state)
        state["route_documented"] = True
        state["clock"] += 3
        return [Event("info", "The route of exposure and the circumstances are written down for the medical evaluation.")]

    def act_identify_source_material(self, state, rng):
        self._need_incident(state)
        state["source_documented"] = True
        state["clock"] += 2
        return [Event("info", "The cell line, its donor code and passage, and the culture vessel are identified and recorded.")]

    def act_complete_incident_record(self, state, rng):
        self._need_incident(state)
        state["record"] = True
        state["clock"] += 10
        return [Event("info", "The laboratory incident record is completed for follow-up and review of the risk assessment.")]

    def act_wait(self, state, rng, minutes):
        state["clock"] += minutes
        return [Event("info", f"{minutes:g} min pass.")]

    def act_return_to_work(self, state, rng):
        self._need_incident(state)
        if state["reported"] is None:
            state["returned_before_report"] = True
        state["returned"] = True
        state["finished"] = True
        return [Event("info", "You return to the bench and the run ends.")]

    def act_end_response(self, state, rng):
        self._need_incident(state)
        state["finished"] = True
        return [Event("info", "The first response is complete; follow-up continues with occupational health.")]

    def visible(self, state):
        rows = [["Clock since incident", f"{state['clock']:.1f} min" if state["announced"] else "work not started"]]
        for label, key in (("Washed", "washed"), ("Eye flushed", "flushed"), ("Material secured", "secured"),
                           ("Supervisor told", "reported"), ("Occupational health", "occ_health")):
            rows.append([label, "no" if state[key] is None else "yes"])
        rows += [["Route documented", "yes" if state["route_documented"] else "no"],
                 ["Source identified", "yes" if state["source_documented"] else "no"],
                 ["Incident record", "yes" if state["record"] else "no"]]
        return [{"title": "Response so far", "rows": rows}]

    def evaluate(self, state):
        p = self.parameters
        kind = state["hidden"]["exposure"]
        first = state["washed"] if kind in SKIN else state["flushed"]
        r = {}
        r["decontaminate-immediately"] = (first is not None and first["at"] <= p["decontaminate_within_min"],
                                          "Wash or flush first, before anything else." if first is None
                                          else f"First wash or flush began {first['at']:.1f} min after the incident.")
        wrong = state["flushed"] if kind in SKIN else state["washed"]
        r["right-method"] = (first is not None and wrong is None,
                             "Soap and water for skin and wounds; water at the eyewash for eyes and mucous membranes.")
        if kind == "eye-splash":
            r["flush-duration"] = (first is not None and first["minutes"] >= p["eye_flush_min"],
                                   f"Flush for at least {p['eye_flush_min']:g} min.")
        else:
            r["flush-duration"] = (None, "No eye exposure in this run.")
        r["secure-material"] = (state["secured"] is not None, "Make the material and sharps safe so no one else is exposed.")
        r["report-immediately"] = (state["reported"] is not None and state["reported"] <= p["report_within_min"],
                                   "The incident was not reported." if state["reported"] is None
                                   else f"Reported {state['reported']:.1f} min after the incident.")
        r["occupational-health"] = (state["occ_health"] is not None, "Contact occupational health for the medical evaluation.")
        r["document-route"] = (state["route_documented"], "Document the route and circumstances of the exposure.")
        r["identify-source"] = (state["source_documented"], "Identify and record the source material.")
        r["incident-record"] = (state["record"], "Complete the laboratory incident record.")
        r["no-return-before-report"] = (not state["returned_before_report"], "Never go back to work before reporting.")
        return r

    def reveal(self, state):
        return [f"This run's exposure was: {state['hidden']['exposure'].replace('-', ' ')}."]
