"""Bench-procedure practice runs: stateless, replayed from a seed and an action list."""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import Field

from .bench import ActionRejected, ProtocolInvalid, replay
from .bench import public_protocol as public_view
from .bench.engine import MAX_ACTIONS
from .schemas import StrictModel

router = APIRouter(prefix="/api/v1/bench")


class BenchAction(StrictModel):
    name: str = Field(min_length=1, max_length=60)
    params: dict[str, bool | int | float | str] = Field(default_factory=dict, max_length=12)


class ReplayRequest(StrictModel):
    seed: int = Field(ge=0, le=2**31 - 1)
    mode: str = Field(pattern=r"^(guided|practice)$")
    actions: list[BenchAction] = Field(default_factory=list, max_length=MAX_ACTIONS)


def library(request: Request):
    try:
        request.app.state.bench.models()
    except ProtocolInvalid as exc:
        raise HTTPException(503, "Bench protocols are unavailable") from exc
    return request.app.state.bench


@router.get("/protocols")
def protocols(request: Request):
    return library(request).summaries()


@router.get("/protocols/{protocol_id}")
def protocol(protocol_id: str, request: Request):
    model = library(request).get(protocol_id)
    if model is None:
        raise HTTPException(404, "Protocol not found")
    return public_view(model.definition)


@router.post("/protocols/{protocol_id}/replay")
def replay_run(protocol_id: str, body: ReplayRequest, request: Request):
    model = library(request).get(protocol_id)
    if model is None:
        raise HTTPException(404, "Protocol not found")
    actions = [action.model_dump() for action in body.actions]
    try:
        return replay(model, body.seed, body.mode, actions).view()
    except ActionRejected as exc:
        return JSONResponse({"detail": str(exc), "rejected_index": getattr(exc, "index", None)}, status_code=422)
