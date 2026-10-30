import json
import random
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from courselab.bench import MODELS, BenchLibrary, ProtocolInvalid
from courselab.bench.engine import ActionRejected, check_parameters, replay, run_state
from courselab.bench.pipette import water_density, z_factor
from courselab.bench.plate_count import bam_round
from courselab.config import Settings
from courselab.main import create_app

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
ORIGIN = "http://localhost:8080"
PIPETTE = "micropipette-gravimetric-verification"
APC = "decimal-dilution-aerobic-plate-count"
BSC = "class-ii-bsc-session-with-spill"


@pytest.fixture(scope="module")
def library():
    return BenchLibrary(CONTENT)


def act(name, **params):
    return {"name": name, "params": params}


def hidden(model, seed):
    rng = random.Random(f"{model.protocol_id}:{model.definition['version']}:{seed}")
    return model.start(rng)["hidden"]


def seed_where(model, test, limit=500):
    for seed in range(limit):
        if test(hidden(model, seed)):
            return seed
    raise AssertionError("no seed found")


def checkpoint_map(view):
    return {row["id"]: row["met"] for row in view["debrief"]["checkpoints"]}


# Library and definitions ------------------------------------------------------

def test_every_protocol_file_has_a_model_and_loads(library):
    models = library.models()
    assert set(models) == {path.stem for path in (CONTENT / "bench/protocols").glob("*.json")}
    assert set(models) == set(MODELS)


def test_cited_sources_exist_in_registry(library):
    registry = {item["id"] for item in json.loads((CONTENT / "sources/registry.json").read_text())["sources"]}
    for model in library.models().values():
        for use in model.definition["sources"]:
            assert use["source_id"] in registry


def test_definition_and_model_must_agree(tmp_path):
    directory = tmp_path / "bench" / "protocols"
    directory.mkdir(parents=True)
    raw = json.loads((CONTENT / f"bench/protocols/{PIPETTE}.json").read_text())
    raw["checkpoints"] = raw["checkpoints"][1:]
    (directory / f"{PIPETTE}.json").write_text(json.dumps(raw))
    with pytest.raises(ProtocolInvalid, match="checkpoints"):
        BenchLibrary(tmp_path).models()


def test_cited_value_needs_location(tmp_path):
    directory = tmp_path / "bench" / "protocols"
    directory.mkdir(parents=True)
    raw = json.loads((CONTENT / f"bench/protocols/{APC}.json").read_text())
    del raw["parameters"][0]["source"]["location"]
    (directory / f"{APC}.json").write_text(json.dumps(raw))
    with pytest.raises(ProtocolInvalid):
        BenchLibrary(tmp_path).models()


# Engine -----------------------------------------------------------------------

def test_replay_is_deterministic_and_seed_dependent(library):
    model = library.get(PIPETTE)
    actions = [act("measure_water_temperature"), act("set_volume", volume_ul=1000), act("fit_tip"),
               act("prewet", cycles=2), act("tare"), act("aspirate", immersion_mm=3, vertical=True),
               act("dispense", touch_off=True), act("read_balance")]
    first = replay(model, 11, "practice", actions).view()
    assert first == replay(model, 11, "practice", actions).view()
    readings = {replay(model, seed, "practice", actions).view()["log"][-1]["events"][0]["data"]["mg"]
                for seed in range(8)}
    assert len(readings) > 1


@pytest.mark.parametrize("params, message", [
    ({"volume_ul": 50}, "between"),
    ({"volume_ul": "1000"}, "number"),
    ({"volume_ul": True}, "number"),
    ({"volume_ul": float("nan")}, "number"),
    ({}, "needs a value"),
    ({"volume_ul": 500, "speed": 1}, "Unknown parameter"),
])
def test_parameter_validation(library, params, message):
    spec = library.get(PIPETTE).action_specs["set_volume"]
    with pytest.raises(ActionRejected, match=message):
        check_parameters(spec, params)


def test_integer_and_choice_parameters(library):
    model = library.get(PIPETTE)
    with pytest.raises(ActionRejected, match="whole number"):
        check_parameters(model.action_specs["prewet"], {"cycles": 1.5})
    report = model.action_specs["submit_report"]
    with pytest.raises(ActionRejected, match="listed options"):
        check_parameters(report, {"mean_volume_ul": 1000, "systematic_error_pct": 0,
                                  "random_error_cv_pct": 0.1, "verdict": "maybe"})


def test_rejected_action_reports_its_index(library):
    model = library.get(PIPETTE)
    with pytest.raises(ActionRejected) as caught:
        replay(model, 1, "practice", [act("fit_tip"), act("dispense", touch_off=True)])
    assert caught.value.index == 1
    assert "tip is empty" in str(caught.value)


def test_finished_runs_accept_no_more_actions(library):
    model = library.get(BSC)
    with pytest.raises(ActionRejected, match="finished"):
        replay(model, 1, "practice", [act("report_out_of_service"), act("inspect_cabinet")])


def test_guidance_and_coaching_only_in_guided_mode(library):
    model = library.get(PIPETTE)
    actions = [act("fit_tip"), act("aspirate", immersion_mm=8, vertical=False)]
    guided = replay(model, 3, "guided", actions).view()
    practice = replay(model, 3, "practice", actions).view()
    assert guided["guidance"] and practice["guidance"] is None
    assert any(e["kind"] == "warning" for e in guided["log"][-1]["events"])
    assert not any(e["kind"] == "warning" for e in practice["log"][-1]["events"])


# Pipette verification -----------------------------------------------------------

def test_water_density_and_z_factor():
    assert water_density(20) == pytest.approx(0.9982067, abs=2e-7)
    assert water_density(4) == pytest.approx(0.99997, abs=1e-5)
    assert z_factor(20) == pytest.approx(1.00285, abs=2e-5)
    assert z_factor(25) > z_factor(20)


def pipette_run(technique=None, tare=True, n=10):
    technique = technique or {}
    actions = [act("measure_water_temperature"), act("set_volume", volume_ul=1000), act("fit_tip"),
               act("prewet", cycles=technique.get("prewet", 3))]
    for _ in range(n):
        if tare:
            actions.append(act("tare"))
        actions += [act("aspirate", immersion_mm=technique.get("depth", 3), vertical=technique.get("vertical", True)),
                    act("dispense", touch_off=technique.get("touch", True)), act("read_balance")]
    return actions


def finish_pipette(model, seed, actions, override=None):
    state, _ = run_state(model, seed, "practice", actions)
    expected = model.expected(state)
    report = {"mean_volume_ul": round(expected["mean"], 2), "systematic_error_pct": round(expected["systematic"], 3),
              "random_error_cv_pct": round(expected["cv"], 3), "verdict": expected["verdict"]}
    report.update(override or {})
    return replay(model, seed, "practice", actions + [act("submit_report", **report)]).view(), expected


def test_pipette_correct_run_meets_every_checkpoint(library):
    model = library.get(PIPETTE)
    view, _ = finish_pipette(model, 5, pipette_run())
    assert all(checkpoint_map(view).values())
    assert view["debrief"]["all_critical_met"]


def test_pipette_faulty_instrument_fails_with_good_technique(library):
    model = library.get(PIPETTE)
    seed = seed_where(model, lambda h: h["fault"] == "bias")
    view, expected = finish_pipette(model, seed, pipette_run())
    assert expected["verdict"] == "fail"
    assert checkpoint_map(view)["report-verdict"]
    assert "calibration offset" in view["debrief"]["revealed"][0]


def test_pipette_sound_instrument_reports_pass(library):
    model = library.get(PIPETTE)
    seed = seed_where(model, lambda h: h["fault"] == "none" and abs(h["bias"]) < 0.002 and h["sd"] < 0.0015)
    _, expected = finish_pipette(model, seed, pipette_run())
    assert expected["verdict"] == "pass"


def test_pipette_wrong_verdict_and_wrong_mean_are_flagged(library):
    model = library.get(PIPETTE)
    view, expected = finish_pipette(model, 5, pipette_run(), {"verdict": "fail" if True else "pass"})
    if expected["verdict"] == "pass":
        assert checkpoint_map(view)["report-verdict"] is False
    view, expected = finish_pipette(model, 5, pipette_run(), {"mean_volume_ul": round(expected["mean"] + 3, 2)})
    assert checkpoint_map(view)["report-mean"] is False
    # Forgetting the buoyancy and density correction (Z = 1) is a near miss that must fail.
    state, _ = run_state(model, 5, "practice", pipette_run())
    raw_mean = sum(item["display_mg"] for item in state["replicates"]) / len(state["replicates"])
    view, _ = finish_pipette(model, 5, pipette_run(), {"mean_volume_ul": round(raw_mean, 2)})
    assert checkpoint_map(view)["report-mean"] is False


def test_pipette_technique_errors_are_recorded(library):
    model = library.get(PIPETTE)
    view, _ = finish_pipette(model, 5, pipette_run({"prewet": 0, "depth": 7, "vertical": False, "touch": False}))
    met = checkpoint_map(view)
    assert not met["tip-prewetted"] and not met["immersion-depth"]
    assert not met["vertical-aspiration"] and not met["touch-off"]
    # The analysis is still checked against the learner's own readings.
    assert met["report-mean"] and met["report-systematic"]


def test_pipette_cumulative_readings_must_be_differenced(library):
    model = library.get(PIPETTE)
    actions = [act("tare")] + pipette_run(tare=False)
    state, _ = run_state(model, 9, "practice", actions)
    assert state["replicates"][-1]["display_mg"] > 9000
    view, expected = finish_pipette(model, 9, actions)
    assert 990 < expected["mean"] < 1010
    met = checkpoint_map(view)
    assert met["tare-before-each"] is False and met["report-mean"]


def test_pipette_too_few_replicates_and_no_temperature(library):
    model = library.get(PIPETTE)
    actions = pipette_run(n=4)[1:]
    view = replay(model, 2, "practice", actions + [act("submit_report", mean_volume_ul=1000, systematic_error_pct=0,
                                                       random_error_cv_pct=0.1, verdict="pass")]).view()
    met = checkpoint_map(view)
    assert not met["replicate-count"] and not met["temperature-recorded"] and not met["report-mean"]


def test_pipette_dispense_requires_reading_previous(library):
    model = library.get(PIPETTE)
    actions = [act("fit_tip"), act("aspirate", immersion_mm=3, vertical=True), act("dispense", touch_off=True),
               act("aspirate", immersion_mm=3, vertical=True), act("dispense", touch_off=True)]
    with pytest.raises(ActionRejected, match="previous dispense"):
        replay(model, 1, "practice", actions)


# Aerobic plate count ------------------------------------------------------------

@pytest.mark.parametrize("value, expected", [
    (12700, 13000), (12400, 12000), (15500, 16000), (14500, 14000),
    (308000 / 22, 14000), (143000 / 11, 13000), (3900, 3900), (2700, 2700), (99, 99), (0, 0),
])
def test_bam_rounding_examples(value, expected):
    assert bam_round(value) == expected


def apc_actions(steps=5, fresh=True, agar_temp=45, wait_before_pour=0.0, controls=True, inverted=True,
                hours=48, shake=True):
    actions = []
    bottles = ["H"] + [f"B{i}" for i in range(1, steps + 1)]
    for source, dest in zip(bottles, bottles[1:]):
        if shake:
            actions.append(act("shake", bottle=source, times=25, arc_cm=30, seconds=7))
        actions.append(act("transfer", source=source, destination=dest, volume_ml=10, fresh_pipet=fresh))
    for bottle in bottles[1:]:
        if shake:
            actions.append(act("shake", bottle=bottle, times=25, arc_cm=30, seconds=7))
        actions += [act("plate", bottle=bottle, volume_ml=1, fresh_pipet=fresh)] * 2
    if controls:
        actions += [act("add_control", kind="diluent"), act("add_control", kind="agar")]
    if wait_before_pour:
        actions.append(act("wait", minutes=wait_before_pour))
    actions += [act("pour_agar", volume_ml=14, temperature_c=agar_temp), act("mix_plates"), act("wait", minutes=15),
                act("incubate", temperature_c=35, hours=hours, inverted=inverted), act("count_plates")]
    return actions


def finish_apc(model, seed, actions, override=None):
    state, _ = run_state(model, seed, "practice", actions)
    expected = model.expected(state)
    report = {"apc_cfu_per_g": expected["apc"] or 0, "estimated": expected["estimated"],
              "laboratory_accident": expected["accident"]}
    report.update(override or {})
    view = replay(model, seed, "practice", actions + [act("submit_result", **report)]).view()
    return view, expected, state


def test_apc_correct_run(library):
    model = library.get(APC)
    seed = seed_where(model, lambda h: not h["diluent_cfu_ml"])
    view, expected, state = finish_apc(model, seed, apc_actions())
    met = checkpoint_map(view)
    assert all(value for value in met.values() if value is not None), met
    true = 10 ** hidden(model, seed)["log_cfu_per_g"]
    assert 0.6 < expected["raw"] / true < 1.6
    assert state["clock"] - 15 - 48 * 60 - 2 * len(state["plates"]) < 15


def test_apc_unshaken_and_reused_pipets_are_flagged(library):
    model = library.get(APC)
    seed = seed_where(model, lambda h: not h["diluent_cfu_ml"])
    view, _, state = finish_apc(model, seed, apc_actions(fresh=False, shake=False))
    met = checkpoint_map(view)
    assert not met["separate-pipets"] and not met["shake-before-sampling"]
    assert state["pipet_reuses"] > 0


def test_apc_carryover_inflates_high_dilutions(library):
    model = library.get(APC)
    seed = seed_where(model, lambda h: not h["diluent_cfu_ml"] and h["log_cfu_per_g"] > 5.5)
    _, _, dirty_state = finish_apc(model, seed, apc_actions(fresh=False))
    clean_state, _ = run_state(model, seed, "practice", apc_actions())
    last = lambda st: sum(p["target"] for p in st["plates"] if p["bottle"] == "B5")  # noqa: E731
    # 0.1 mL carried from a tenfold stronger dilution adds about 10% per step, compounding to roughly 2x by B5.
    assert last(dirty_state) > 1.6 * last(clean_state)


def test_apc_hot_agar_and_late_pour(library):
    model = library.get(APC)
    seed = seed_where(model, lambda h: not h["diluent_cfu_ml"])
    view, expected, _ = finish_apc(model, seed, apc_actions(agar_temp=52))
    good, good_expected, _ = finish_apc(model, seed, apc_actions())
    assert checkpoint_map(view)["agar-temperature"] is False
    if expected["raw"] and good_expected["raw"]:
        assert expected["raw"] < good_expected["raw"]
    late, _, _ = finish_apc(model, seed, apc_actions(wait_before_pour=10))
    assert checkpoint_map(late)["agar-within-window"] is False


def test_apc_contaminated_diluent_needs_controls_to_detect(library):
    model = library.get(APC)
    seed = seed_where(model, lambda h: h["diluent_cfu_ml"] > 4)
    view, expected, _ = finish_apc(model, seed, apc_actions())
    assert expected["accident"] is True
    assert checkpoint_map(view)["report-flags"]
    missed, _, _ = finish_apc(model, seed, apc_actions(), {"laboratory_accident": False})
    assert checkpoint_map(missed)["report-flags"] is False
    blind, blind_expected, _ = finish_apc(model, seed, apc_actions(controls=False))
    assert blind_expected["accident"] is False
    assert checkpoint_map(blind)["controls"] is False


def test_apc_wrong_rounding_is_a_near_miss(library):
    model = library.get(APC)
    seed = seed_where(model, lambda h: not h["diluent_cfu_ml"])
    _, expected, _ = finish_apc(model, seed, apc_actions())
    view, _, _ = finish_apc(model, seed, apc_actions(), {"apc_cfu_per_g": round(expected["raw"])})
    if round(expected["raw"]) != expected["apc"]:
        assert checkpoint_map(view)["report-apc"] is False


def test_apc_upright_short_incubation(library):
    model = library.get(APC)
    view, _, _ = finish_apc(model, 4, apc_actions(inverted=False, hours=24))
    assert checkpoint_map(view)["incubation"] is False


def test_apc_cannot_count_before_incubation(library):
    model = library.get(APC)
    with pytest.raises(ActionRejected, match="Incubate"):
        replay(model, 1, "practice", [act("count_plates")])


# Biosafety cabinet --------------------------------------------------------------

def bsc_setup():
    actions = [act("inspect_cabinet"), act("don_ppe", coat_buttoned=True, gloves=True), act("blower", on=True),
               act("set_sash", position="certified"), act("wait", minutes=5), act("close_drain_valve"),
               act("disinfect_interior", agent="ethanol70"), act("lay_toweling", location="work_surface")]
    for item, zone in [("pipettes", "rear"), ("pipette_aid", "center"), ("media", "rear"), ("plates", "rear"),
                       ("discard_tray", "side"), ("biohazard_bag", "side"), ("culture", "rear")]:
        actions.append(act("load_item", item=item, zone=zone, wiped=True))
    return actions + [act("insert_arms", motion="slow_perpendicular"), act("settle", seconds=60)]


SMALL_SPILL = [act("cover_spill"), act("apply_disinfectant", direction="outside_in"), act("wait", minutes=25),
               act("push_towels", direction="edge_to_center"), act("discard_towels", into="biohazard_bag"),
               act("wipe_down_interior"), act("change_gloves")]
TEARDOWN_ORDER = ["culture", "media", "plates", "pipettes", "pipette_aid", "discard_tray", "biohazard_bag"]
CLOSE = [act("final_wipe", agent="ethanol70"), act("remove_ppe"), act("wash_hands"), act("end_session")]


def bsc_good_run(size, spill_step):
    actions = bsc_setup()
    work = act("work_step", distance_in=6, lids_over_plates=True)
    for step in range(1, 4):
        actions.append(work)
        if step == spill_step:
            actions += SMALL_SPILL
            if size == "large":
                actions += [act("remove_item", item=item, decontaminated=True) for item in TEARDOWN_ORDER]
                actions += [act("flood_drain_pan"), act("drain_to_disinfectant")]
                return actions + CLOSE
    actions.append(act("withdraw_arms"))
    actions += [act("remove_item", item=item, decontaminated=True) for item in TEARDOWN_ORDER]
    return actions + CLOSE


@pytest.mark.parametrize("size", ["small", "large"])
def test_bsc_correct_run(library, size):
    model = library.get(BSC)
    seed = seed_where(model, lambda h: not h["expired"] and h["spill_size"] == size)
    view = replay(model, seed, "practice", bsc_good_run(size, hidden(model, seed)["spill_step"])).view()
    met = checkpoint_map(view)
    assert all(value for value in met.values() if value is not None), met
    assert met["large-spill-drain"] is (True if size == "large" else None)


def test_bsc_expired_cabinet_must_be_taken_out_of_service(library):
    model = library.get(BSC)
    seed = seed_where(model, lambda h: h["expired"])
    view = replay(model, seed, "practice", [act("inspect_cabinet"), act("report_out_of_service")]).view()
    met = checkpoint_map(view)
    assert met["certification-current"] and met["certification-checked"]
    assert all(value is None for key, value in met.items() if not key.startswith("certification"))
    size, step = hidden(model, seed)["spill_size"], hidden(model, seed)["spill_step"]
    used = replay(model, seed, "practice", bsc_good_run(size, step)).view()
    assert checkpoint_map(used)["certification-current"] is False


def test_bsc_common_errors_are_flagged(library):
    model = library.get(BSC)
    seed = seed_where(model, lambda h: not h["expired"] and h["spill_size"] == "small" and h["drain_open"])
    actions = [act("blower", on=True), act("set_sash", position="raised"),
               act("disinfect_interior", agent="water"), act("lay_toweling", location="front_grille"),
               act("load_item", item="culture", zone="rear", wiped=False),
               act("load_item", item="plates", zone="center", wiped=True),
               act("load_item", item="pipettes", zone="center", wiped=True),
               act("load_item", item="pipette_aid", zone="center", wiped=True),
               act("load_item", item="extra_gloves", zone="side", wiped=True),
               act("insert_arms", motion="sweeping"), act("light_burner"),
               act("work_step", distance_in=2, lids_over_plates=False)]
    spill_step = hidden(model, seed)["spill_step"]
    if spill_step == 2:
        actions.append(act("work_step", distance_in=2, lids_over_plates=False))
    actions += [act("apply_disinfectant", direction="center_out"), act("wait", minutes=5),
                act("push_towels", direction="center_to_edge"), act("discard_towels", into="regular_trash"),
                act("wipe_down_interior"), act("end_session")]
    view = replay(model, seed, "practice", actions).view()
    met = checkpoint_map(view)
    for key in ("certification-checked", "ppe", "purge-before-loading", "interior-disinfected", "drain-valve-closed",
                "toweling-placement", "items-wiped", "biological-last", "only-needed-items",
                "sash-at-certified-height", "arms-slow", "arms-settle", "work-four-inches", "no-open-flame",
                "spill-covered-outside-in", "spill-contact-time", "spill-towels-edge-to-center",
                "spill-biohazard-disposal", "spill-gloves-changed", "final-wipe", "ppe-off-handwash"):
        assert met[key] is False, key
    assert not view["debrief"]["all_critical_met"]
    assert any("mould" in e["text"] for e in view["log"][-1]["events"])


def test_bsc_work_blocked_until_spill_dealt_with(library):
    model = library.get(BSC)
    seed = seed_where(model, lambda h: not h["expired"] and h["spill_step"] == 1)
    actions = bsc_setup() + [act("work_step", distance_in=6, lids_over_plates=True)]
    with pytest.raises(ActionRejected, match="spill"):
        replay(model, seed, "practice", actions + [act("work_step", distance_in=6, lids_over_plates=True)])


def test_bsc_large_spill_with_open_drain(library):
    model = library.get(BSC)
    seed = seed_where(model, lambda h: not h["expired"] and h["spill_size"] == "large")
    actions = [a for a in bsc_good_run("large", hidden(model, seed)["spill_step"]) if a["name"] != "close_drain_valve"]
    state, _ = run_state(model, seed, "practice", actions)
    view = replay(model, seed, "practice", actions).view()
    if state["hidden"]["drain_open"]:
        assert checkpoint_map(view)["large-spill-drain"] is False
        assert any("floor" in risk for risk in state["hidden"]["personnel_risk"])


# API ------------------------------------------------------------------------------

@pytest.fixture
def api(tmp_path):
    settings = Settings(database_url=f"sqlite:///{tmp_path / 'bench.db'}", content_root=CONTENT,
                        private_assessments_root=tmp_path / "private", allowed_origins=(ORIGIN,),
                        cookie_secure=False)
    from courselab.db import Base
    app = create_app(settings)
    Base.metadata.create_all(app.state.engine)
    with TestClient(app) as client:
        yield client


def test_api_lists_protocols_without_checkpoints(api):
    listed = api.get("/api/v1/bench/protocols").json()
    assert {item["id"] for item in listed} == set(MODELS)
    for item in listed:
        detail = api.get(f"/api/v1/bench/protocols/{item['id']}").json()
        assert "checkpoints" not in detail and "parameters" not in detail and "guided_steps" not in detail
        assert detail["actions"] and detail["limitations"]


def test_api_replay_hides_debrief_until_finished(api):
    url = f"/api/v1/bench/protocols/{BSC}/replay"
    body = {"seed": 3, "mode": "practice", "actions": [act("inspect_cabinet")]}
    running = api.post(url, json=body, headers={"Origin": ORIGIN})
    assert running.status_code == 200
    payload = running.json()
    assert payload["debrief"] is None and "hidden" not in json.dumps(payload)
    assert "description" not in json.dumps(payload["panels"])
    body["actions"].append(act("report_out_of_service"))
    finished = api.post(url, json=body, headers={"Origin": ORIGIN}).json()
    assert finished["finished"] and finished["debrief"]["checkpoints"]
    assert "not a grade" in finished["debrief"]["note"]


def test_api_rejections(api):
    url = f"/api/v1/bench/protocols/{PIPETTE}/replay"
    rejected = api.post(url, json={"seed": 1, "mode": "practice", "actions": [act("dispense", touch_off=True)]},
                        headers={"Origin": ORIGIN})
    assert rejected.status_code == 422 and rejected.json()["rejected_index"] == 0
    assert api.post(url, json={"seed": -1, "mode": "practice", "actions": []},
                    headers={"Origin": ORIGIN}).status_code == 422
    assert api.post(url, json={"seed": 1, "mode": "exam", "actions": []}, headers={"Origin": ORIGIN}).status_code == 422
    assert api.post(url, json={"seed": 1, "mode": "practice", "actions": [], "extra": 1},
                    headers={"Origin": ORIGIN}).status_code == 422
    assert api.post(url, json={"seed": 1, "mode": "practice", "actions": []}).status_code == 403
    assert api.post("/api/v1/bench/protocols/none/replay", json={"seed": 1, "mode": "practice", "actions": []},
                    headers={"Origin": ORIGIN}).status_code == 404
    assert api.get("/api/v1/bench/protocols/none").status_code == 404
