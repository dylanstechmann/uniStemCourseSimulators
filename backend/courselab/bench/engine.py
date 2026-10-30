"""Deterministic replay of bench-procedure practice runs.

A run is a protocol, a seed, a mode and the ordered list of actions the learner has
taken. The server replays the whole list on every request, so no run state is stored
and every run can be reproduced exactly. Hidden variables (a pipette's true bias, a
contaminated diluent) and checkpoint rules stay on the server; the browser receives
only what a person at the bench could see, and the checkpoint debrief once the run ends.
"""

from __future__ import annotations

import math
import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

MODES = ("guided", "practice")
MAX_ACTIONS = 400


class ActionRejected(Exception):
    """An action that is physically impossible in the current state (not a mistake)."""


class ProtocolInvalid(Exception):
    """A protocol definition that does not match its model."""


@dataclass
class Event:
    kind: str  # "info", "readout", "warning" or "consequence"
    text: str
    data: dict[str, Any] = field(default_factory=dict)

    def view(self) -> dict:
        return {"kind": self.kind, "text": self.text, "data": self.data}


def coach(state: dict, events: list[Event], text: str) -> None:
    """Immediate feedback on a mistake, given only in guided mode.

    In practice mode the learner finds out the way they would at a bench: through a
    later readout, a failed result, or the debrief.
    """
    if state.get("mode") == "guided":
        events.append(Event("warning", text))


def check_parameters(spec: dict, params: Any) -> dict:
    """Validate one action's parameters against the action spec from the definition."""
    if not isinstance(params, dict):
        raise ActionRejected("Action parameters must be an object")
    declared = {item["name"]: item for item in spec.get("params", [])}
    unknown = set(params) - set(declared)
    if unknown:
        raise ActionRejected(f"Unknown parameter for {spec['name']}: {sorted(unknown)[0]}")
    clean = {}
    for name, item in declared.items():
        if name not in params:
            raise ActionRejected(f"{spec['label']} needs a value for {item['label'].lower()}")
        value = params[name]
        kind = item["type"]
        if kind == "boolean":
            if not isinstance(value, bool):
                raise ActionRejected(f"{item['label']} must be true or false")
        elif kind in ("number", "integer"):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ActionRejected(f"{item['label']} must be a number")
            if kind == "integer" and int(value) != value:
                raise ActionRejected(f"{item['label']} must be a whole number")
            if not item["min"] <= value <= item["max"]:
                raise ActionRejected(
                    f"{item['label']} must be between {item['min']} and {item['max']} {item.get('unit', '')}".rstrip()
                )
            value = int(value) if kind == "integer" else float(value)
        elif kind == "choice":
            if value not in [option["value"] for option in item["options"]]:
                raise ActionRejected(f"{item['label']} must be one of the listed options")
        else:  # pragma: no cover - the schema forbids other kinds
            raise ProtocolInvalid(f"Unknown parameter type {kind}")
        clean[name] = value
    return clean


class ProtocolModel(ABC):
    """Physics, error models and checkpoint rules for one protocol definition."""

    protocol_id: str

    def __init__(self, definition: dict):
        if definition["id"] != self.protocol_id:
            raise ProtocolInvalid(f"Definition {definition['id']} does not match model {self.protocol_id}")
        self.definition = definition
        self.parameters = {item["name"]: item["value"] for item in definition["parameters"]}
        self.action_specs = {item["name"]: item for item in definition["actions"]}
        handled = {name[len("act_"):] for name in dir(self) if name.startswith("act_")}
        if handled != set(self.action_specs):
            raise ProtocolInvalid(
                f"{self.protocol_id}: actions in definition {sorted(self.action_specs)} "
                f"do not match handlers {sorted(handled)}"
            )
        declared = {item["id"] for item in definition["checkpoints"]}
        if declared != set(self.checkpoint_ids()):
            raise ProtocolInvalid(
                f"{self.protocol_id}: checkpoints in definition {sorted(declared)} "
                f"do not match model {sorted(self.checkpoint_ids())}"
            )

    @abstractmethod
    def start(self, rng: random.Random) -> dict:
        """Initial state, including hidden variables drawn from the seeded generator."""

    @abstractmethod
    def visible(self, state: dict) -> list[dict]:
        """Panels of what the learner can see now: [{"title": str, "rows": [[label, value], ...]}]."""

    @abstractmethod
    def checkpoint_ids(self) -> list[str]:
        """Every checkpoint the model evaluates; must equal the definition's list."""

    @abstractmethod
    def evaluate(self, state: dict) -> dict[str, tuple[bool | None, str]]:
        """Checkpoint id -> (met, detail). None means the checkpoint did not apply in this run."""

    def reveal(self, state: dict) -> list[str]:
        """Hidden facts shown in the debrief once the run has finished."""
        return []

    def apply(self, state: dict, name: str, params: dict, rng: random.Random) -> list[Event]:
        if state.get("finished"):
            raise ActionRejected("This run has finished; start a new run to practise again")
        spec = self.action_specs.get(name)
        if spec is None:
            raise ActionRejected(f"Unknown action {name}")
        clean = check_parameters(spec, params)
        return getattr(self, f"act_{name}")(state, rng, **clean)


@dataclass
class RunView:
    protocol_id: str
    protocol_version: str
    seed: int
    mode: str
    finished: bool
    clock_minutes: float
    panels: list[dict]
    log: list[dict]
    guidance: list[str] | None
    debrief: dict | None

    def view(self) -> dict:
        return {
            "protocol_id": self.protocol_id, "protocol_version": self.protocol_version,
            "seed": self.seed, "mode": self.mode, "finished": self.finished,
            "clock_minutes": round(self.clock_minutes, 2), "panels": self.panels,
            "log": self.log, "guidance": self.guidance, "debrief": self.debrief,
        }


def debrief(model: ProtocolModel, state: dict) -> dict:
    results = model.evaluate(state)
    rows = []
    for checkpoint in model.definition["checkpoints"]:
        met, detail = results[checkpoint["id"]]
        rows.append({
            "id": checkpoint["id"], "severity": checkpoint["severity"],
            "description": checkpoint["description"], "rationale": checkpoint["rationale"],
            "source": checkpoint["source"], "met": met, "detail": detail,
        })
    applicable = [row for row in rows if row["met"] is not None]
    missed = {severity: sum(1 for row in applicable if row["severity"] == severity and not row["met"])
              for severity in ("critical", "major", "minor")}
    return {
        "checkpoints": rows,
        "missed": missed,
        "met_count": sum(1 for row in applicable if row["met"]),
        "applicable_count": len(applicable),
        "all_critical_met": missed["critical"] == 0,
        "revealed": model.reveal(state),
        "note": "Formative practice only. This debrief is not a grade, a competency record or a certification.",
    }


def replay(model: ProtocolModel, seed: int, mode: str, actions: list[dict]) -> RunView:
    """Rebuild a run from its seed and action list. Raises ActionRejected with the failing index."""
    state, log = run_state(model, seed, mode, actions)
    guidance = model.definition["guided_steps"] if mode == "guided" else None
    return RunView(
        protocol_id=model.protocol_id, protocol_version=model.definition["version"], seed=seed,
        mode=mode, finished=state["finished"], clock_minutes=state["clock"],
        panels=model.visible(state), log=log, guidance=guidance,
        debrief=debrief(model, state) if state["finished"] else None,
    )


def run_state(model: ProtocolModel, seed: int, mode: str, actions: list[dict]) -> tuple[dict, list[dict]]:
    """The full server-side state after replaying the actions, including hidden variables."""
    if mode not in MODES:
        raise ActionRejected(f"Mode must be one of {', '.join(MODES)}")
    if len(actions) > MAX_ACTIONS:
        raise ActionRejected(f"A run is limited to {MAX_ACTIONS} actions")
    rng = random.Random(f"{model.protocol_id}:{model.definition['version']}:{seed}")
    state = model.start(rng)
    state["mode"] = mode
    state.setdefault("clock", 0.0)
    state.setdefault("finished", False)
    log = []
    for index, action in enumerate(actions):
        if not isinstance(action, dict) or not isinstance(action.get("name"), str):
            raise ActionRejected(f"Action {index + 1} is malformed")
        try:
            events = model.apply(state, action["name"], action.get("params", {}), rng)
        except ActionRejected as exc:
            rejected = ActionRejected(f"Action {index + 1} ({action['name']}): {exc}")
            rejected.index = index
            raise rejected from None
        log.append({
            "index": index, "name": action["name"],
            "label": model.action_specs[action["name"]]["label"],
            "params": action.get("params", {}),
            "clock_minutes": round(state["clock"], 2),
            "events": [event.view() for event in events],
        })
    return state, log


def round_significant(value: float, digits: int) -> float:
    if value == 0:
        return 0.0
    return round(value, digits - 1 - int(math.floor(math.log10(abs(value)))))
