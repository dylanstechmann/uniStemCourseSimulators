"""Bench-procedure practice: protocol definitions, models and deterministic replay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from .bsc import BiosafetyCabinetSession
from .engine import ActionRejected, ProtocolInvalid, ProtocolModel, replay
from .pipette import PipetteVerification
from .plate_count import AerobicPlateCount

MODELS: dict[str, type[ProtocolModel]] = {
    model.protocol_id: model for model in (PipetteVerification, AerobicPlateCount, BiosafetyCabinetSession)
}

__all__ = ["ActionRejected", "BenchLibrary", "ProtocolInvalid", "replay"]


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Source(_Strict):
    kind: Literal["cited", "simulation-typical", "simulation-model"]
    source_id: str | None = None
    location: str | None = None
    note: str | None = None

    @model_validator(mode="after")
    def cited_needs_source(self):
        if self.kind == "cited" and not (self.source_id and self.location):
            raise ValueError("A cited value needs a source_id and a location")
        return self


class Option(_Strict):
    value: str
    label: str


class Param(_Strict):
    name: str
    label: str
    type: Literal["number", "integer", "boolean", "choice"]
    min: float | None = None
    max: float | None = None
    unit: str | None = None
    options: list[Option] | None = None

    @model_validator(mode="after")
    def complete(self):
        if self.type in ("number", "integer") and (self.min is None or self.max is None or self.min > self.max):
            raise ValueError(f"{self.name}: numeric parameters need min <= max")
        if self.type == "choice" and not self.options:
            raise ValueError(f"{self.name}: choice parameters need options")
        return self


class Action(_Strict):
    name: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    label: str
    params: list[Param]


class Parameter(_Strict):
    name: str
    value: float | int | str | list[float]
    unit: str
    label: str
    source: Source


class Checkpoint(_Strict):
    id: str = Field(pattern=r"^[a-z0-9-]+$")
    severity: Literal["critical", "major", "minor"]
    description: str
    rationale: str
    source: Source


class SourceUse(_Strict):
    source_id: str
    use: str


class ProtocolDefinition(_Strict):
    schema_version: Literal["1.0"]
    id: str = Field(pattern=r"^[a-z0-9-]+$")
    version: str = Field(pattern=r"^\d+\.\d+\.\d+$")
    title: str
    layer: int = Field(ge=0, le=5)
    summary: str
    scenario: str
    guided_steps: list[str] = Field(min_length=1)
    parameters: list[Parameter]
    actions: list[Action] = Field(min_length=1)
    checkpoints: list[Checkpoint] = Field(min_length=1)
    sources: list[SourceUse]
    limitations: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def unique_names(self):
        for label, names in (("parameter", [p.name for p in self.parameters]),
                             ("action", [a.name for a in self.actions]),
                             ("checkpoint", [c.id for c in self.checkpoints])):
            if len(names) != len(set(names)):
                raise ValueError(f"Duplicate {label} name in {self.id}")
        return self


class BenchLibrary:
    """Loads every protocol under content/bench/protocols and pairs it with its model."""

    def __init__(self, content_root: Path):
        self.directory = Path(content_root) / "bench" / "protocols"
        self._models: dict[str, ProtocolModel] | None = None

    def models(self) -> dict[str, ProtocolModel]:
        if self._models is None:
            models = {}
            if self.directory.is_dir():
                for path in sorted(self.directory.glob("*.json")):
                    try:
                        raw = json.loads(path.read_text(encoding="utf-8"))
                        ProtocolDefinition.model_validate(raw)
                    except (ValueError, ValidationError) as exc:
                        raise ProtocolInvalid(f"{path.name}: {exc}") from exc
                    if raw["id"] != path.stem:
                        raise ProtocolInvalid(f"{path.name}: file name must match the protocol id")
                    model = MODELS.get(raw["id"])
                    if model is None:
                        raise ProtocolInvalid(f"{path.name}: no simulation model for {raw['id']}")
                    models[raw["id"]] = model(raw)
            self._models = models
        return self._models

    def get(self, protocol_id: str) -> ProtocolModel | None:
        return self.models().get(protocol_id)

    def summaries(self) -> list[dict]:
        return [public_summary(model.definition) for model in self.models().values()]


def public_summary(definition: dict) -> dict:
    return {key: definition[key] for key in ("id", "version", "title", "layer", "summary")}


def public_protocol(definition: dict) -> dict:
    """What the browser may see before a run ends: no checkpoints, no hidden-model parameters."""
    return {
        **public_summary(definition),
        "scenario": definition["scenario"],
        "actions": definition["actions"],
        "limitations": definition["limitations"],
        "sources": definition["sources"],
    }
