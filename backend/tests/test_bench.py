import json
import math
import random
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from courselab.bench import MODELS, BenchLibrary, ProtocolInvalid, public_protocol
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



# Autoclave validation ---------------------------------------------------------

AUTOCLAVE = "autoclave-waste-load-validation"


def autoclave_run(model, seed, closure="loosely_closed", control=True, exposure_extra_d=2, mass=6.0, verdict=None,
                  report_exposure=None):
    h = hidden(model, seed)
    lag = round(h["lag_per_kg"] * mass * 0.8, 1)
    exposure = math.ceil(lag + (12 + exposure_extra_d) * h["d_value"])
    actions = [act("prepare_load", mass_kg=mass, bag_closure=closure, water_added=True, in_tray=True),
               act("place_thermocouple", position="centre"), act("place_thermocouple", position="top"),
               act("place_bi", position="centre"), act("place_bi", position="top")]
    if control:
        actions.append(act("keep_control_bi"))
    actions += [act("run_cycle", temperature_c=121, exposure_min=exposure), act("record_cycle"),
                act("incubate_bis", temperature_c=57, hours=48), act("read_bis")]
    state, _ = run_state(model, seed, "practice", actions)
    results = state["bi_read"]
    expected = "pass" if control and results.get("control") == "growth" and all(
        v == "no growth" for k, v in results.items() if k != "control") else "fail"
    observed = state["cycle"]["reached"]["centre"]
    actions.append(act("submit_report", centre_lag_min=observed if observed is not None else 0,
                       verdict=verdict or expected, validated_exposure_min=report_exposure or exposure))
    return replay(model, seed, "practice", actions).view(), state, expected


def test_autoclave_correct_validation(library):
    model = library.get(AUTOCLAVE)
    view, state, expected = autoclave_run(model, 3)
    assert expected == "pass" and state["bi_read"]["centre"] == "no growth"
    assert all(v for v in checkpoint_map(view).values() if v is not None), checkpoint_map(view)
    assert "D₁₂₁" in json.dumps(view["panels"], ensure_ascii=False)


def test_autoclave_sealed_bag_keeps_steam_out(library):
    model = library.get(AUTOCLAVE)
    view, state, expected = autoclave_run(model, 3, closure="tightly_sealed")
    assert state["cycle"]["reached"]["centre"] is None and state["bi_read"]["centre"] == "growth"
    met = checkpoint_map(view)
    assert expected == "fail" and met["bag-loosely-closed"] is False and met["exposure-sufficient"] is False
    assert met["report-cycle-time"] is None and met["report-verdict"]
    assert any("100 °C" in e["text"] for entry in view["log"] for e in entry["events"])


def test_autoclave_short_exposure_fails_at_the_centre(library):
    model = library.get(AUTOCLAVE)
    view, state, expected = autoclave_run(model, 5, exposure_extra_d=-7)
    assert state["bi_read"]["centre"] == "growth" and expected == "fail"
    assert checkpoint_map(view)["exposure-sufficient"] is False


def test_autoclave_needs_a_positive_control(library):
    model = library.get(AUTOCLAVE)
    view, _, expected = autoclave_run(model, 3, control=False)
    met = checkpoint_map(view)
    assert expected == "fail" and met["positive-control"] is False and met["report-verdict"]
    wrong, _, _ = autoclave_run(model, 3, control=False, verdict="pass")
    assert checkpoint_map(wrong)["report-verdict"] is False


def test_autoclave_cold_incubation_hides_survivors(library):
    model = library.get(AUTOCLAVE)
    h = hidden(model, 5)
    actions = [act("prepare_load", mass_kg=6.0, bag_closure="loosely_closed", water_added=True, in_tray=True),
               act("place_bi", position="centre"), act("keep_control_bi"),
               act("run_cycle", temperature_c=121, exposure_min=5), act("incubate_bis", temperature_c=37, hours=12),
               act("read_bis")]
    state, _ = run_state(model, 5, "practice", actions)
    assert state["bi_read"] == {"centre": "no growth", "control": "no growth"}
    assert h["d_value"] > 0


def test_autoclave_short_validated_time_is_flagged(library):
    model = library.get(AUTOCLAVE)
    view, _, _ = autoclave_run(model, 3, report_exposure=10)
    assert checkpoint_map(view)["report-cycle-time"] is False



# Exposure first response ---------------------------------------------------------

EXPOSURE = "exposure-incident-first-response"


def exposure_good(kind):
    first = [act("flush_at_eyewash", minutes=15)] if kind == "eye-splash" else [act("wash_with_soap_and_water", seconds=60)]
    return [act("begin_work"), *first, act("secure_material"), act("notify_supervisor"), act("contact_occupational_health"),
            act("document_route_and_circumstances"), act("identify_source_material"), act("complete_incident_record"),
            act("end_response")]


@pytest.mark.parametrize("kind", ["needlestick", "eye-splash", "cut"])
def test_exposure_correct_response(library, kind):
    model = library.get(EXPOSURE)
    seed = seed_where(model, lambda h: h["exposure"] == kind)
    view = replay(model, seed, "practice", exposure_good(kind)).view()
    met = checkpoint_map(view)
    assert all(v for v in met.values() if v is not None), met
    assert (met["flush-duration"] is None) == (kind != "eye-splash")
    assert view["log"][0]["events"][0]["kind"] == "consequence"


def test_exposure_wrong_method_late_report_and_early_return(library):
    model = library.get(EXPOSURE)
    seed = seed_where(model, lambda h: h["exposure"] == "eye-splash")
    actions = [act("begin_work"), act("wait", minutes=10), act("wash_with_soap_and_water", seconds=20),
               act("wait", minutes=30), act("return_to_work")]
    met = checkpoint_map(replay(model, seed, "practice", actions).view())
    for key in ("decontaminate-immediately", "right-method", "flush-duration", "report-immediately", "occupational-health",
                "no-return-before-report", "document-route", "identify-source"):
        assert met[key] is False, key


def test_exposure_short_eye_flush_is_flagged(library):
    model = library.get(EXPOSURE)
    seed = seed_where(model, lambda h: h["exposure"] == "eye-splash")
    actions = exposure_good("eye-splash")
    actions[1] = act("flush_at_eyewash", minutes=2)
    assert checkpoint_map(replay(model, seed, "practice", actions).view())["flush-duration"] is False


def test_exposure_actions_need_the_incident_first(library):
    model = library.get(EXPOSURE)
    with pytest.raises(ActionRejected, match="Begin the work"):
        replay(model, 1, "practice", [act("notify_supervisor")])


# Hemocytometer counting ---------------------------------------------------------

CELL_COUNT = "hemocytometer-cell-count-viability"


def cell_count_setup():
    return [act("mix_sample", seconds=10), act("prepare_dilution", sample_ul=10, dye_ul=10),
            act("place_coverslip"), act("load_chamber", chamber="A"), act("load_chamber", chamber="B")]


def finish_cell_count(model, seed, actions=None, wrong_boundary=False, override=None):
    actions = actions or cell_count_setup()
    state, _ = run_state(model, seed, "practice", actions)
    for chamber, cells in state["chambers"].items():
        actions.append(act("select_chamber", chamber=chamber))
        tally = {"unstained": 0, "stained": 0}
        for cell in cells:
            decision = "exclude" if cell["boundary"] == "exclude" else "stained" if cell["stained"] else "unstained"
            if wrong_boundary and cell["boundary"] == "exclude":
                decision = "unstained"
            actions.append(act("mark_cell", cell_id=cell["id"], classification=decision))
            if decision != "exclude":
                tally[decision] += 1
        actions.append(act("record_tally", chamber=chamber, **tally))
    state, _ = run_state(model, seed, "practice", actions)
    expected = model.expected(state)
    report = {"concentration_cells_ml": expected["concentration"],
              "viability_pct": expected["viability"],
              "relative_counting_uncertainty_pct": expected["uncertainty"]}
    report.update(override or {})
    return replay(model, seed, "practice", actions + [act("submit_report", **report)]).view(), state


def test_cell_count_correct_run_and_replay(library):
    model = library.get(CELL_COUNT)
    view, state = finish_cell_count(model, 7)
    assert all(checkpoint_map(view).values()), checkpoint_map(view)
    assert 20 <= len(state["chambers"]["A"]) <= 80
    assert any(cell["boundary"] == "exclude" for cell in state["chambers"]["A"])
    actions = [{"name": entry["name"], "params": entry["params"]} for entry in view["log"]]
    assert view == replay(model, 7, "practice", actions).view()


@pytest.mark.parametrize("seed", range(1, 41))
def test_cell_count_correct_run_meets_every_checkpoint_for_any_seed(library, seed):
    # Regression: generated concentrations once put most mixed twofold fields above the 20–80 range.
    model = library.get(CELL_COUNT)
    view, state = finish_cell_count(model, seed)
    assert all(checkpoint_map(view).values()), (seed, checkpoint_map(view))
    assert all(20 <= len(cells) <= 80 for cells in state["chambers"].values())


def test_cell_count_boundary_and_stain_decisions_are_checked(library):
    model = library.get(CELL_COUNT)
    view, _ = finish_cell_count(model, 7, wrong_boundary=True)
    assert checkpoint_map(view)["boundary-rule"] is False
    assert checkpoint_map(view)["report-concentration"] is True


def test_cell_count_dilution_changes_field_and_report(library):
    model = library.get(CELL_COUNT)
    actions = cell_count_setup()
    actions[1] = act("prepare_dilution", sample_ul=10, dye_ul=90)
    view, state = finish_cell_count(model, 7, actions)
    assert len(state["chambers"]["A"]) < 20
    assert checkpoint_map(view)["dilution-recorded"] is False
    assert checkpoint_map(view)["countable-density"] is False
    assert checkpoint_map(view)["report-concentration"] is True


def test_cell_count_requires_all_cells_and_both_chambers(library):
    model = library.get(CELL_COUNT)
    with pytest.raises(ActionRejected, match="Classify every"):
        replay(model, 7, "practice", cell_count_setup() + [act("record_tally", chamber="A", unstained=1, stained=1)])
    with pytest.raises(ActionRejected, match="both chambers"):
        replay(model, 7, "practice", cell_count_setup() + [act("submit_report", concentration_cells_ml=1e6,
                                                               viability_pct=90, relative_counting_uncertainty_pct=10)])


def test_cell_count_poisson_uncertainty_uses_all_included_cells(library):
    model = library.get(CELL_COUNT)
    view, state = finish_cell_count(model, 7, override={"relative_counting_uncertainty_pct": 1})
    expected = model.expected(state)
    assert expected["uncertainty"] == pytest.approx(100 / math.sqrt(expected["total"]))
    assert checkpoint_map(view)["report-uncertainty"] is False


ASEPTIC = "aseptic-medium-change-with-hidden-contamination"


def aseptic_valid_lot(hidden_state):
    return "medium_lot_b" if hidden_state["expired_lot"] == "medium_lot_a" else "medium_lot_a"


def aseptic_lot(model, seed, kind="valid"):
    hidden_state = hidden(model, seed)
    return hidden_state["expired_lot"] if kind == "expired" else aseptic_valid_lot(hidden_state)


def aseptic_run(model, seed, *, lot=None, disinfect=True, disinfect_agent="sterile_alcohol70", uv=False,
                loads=None, extra_loads=(), lid="held_above", open_turbid=False, spent=None, fresh=None,
                sample_fresh=True, antibiotics=False, incubations=((7, 22), (7, 32)), mycoplasma=True,
                waste_method="chemical_then_autoclave", containment="sealed_biohazard",
                dispose_decontaminated=True, final_agent="sterile_alcohol70"):
    lot = lot or aseptic_lot(model, seed)
    actions = [act("inspect_supplies")]
    if disinfect:
        actions.append(act("disinfect_interior", agent=disinfect_agent))
    if uv:
        actions.append(act("run_uv_lamp", minutes=15))
    actions.append(act("sanitize_gloves", agent="sterile_alcohol70"))
    base = [("target_flask", "work_center"), ("turbid_flask", "dirty_side"), ("pipettes", "clean_side"),
            ("pipette_aid", "clean_side"), ("sterility_broth", "clean_side"), ("waste_container", "dirty_side")]
    used_loads = base if loads is None else loads
    for item, zone in list(used_loads) + list(extra_loads):
        actions.append(act("load_item", item=item, zone=zone, wiped=True))
    actions += [act("inspect_flask", container="target_flask"), act("inspect_flask", container="turbid_flask")]
    if open_turbid:
        actions.append(act("open_container", container="turbid_flask", lid_position="held_above"))
    actions.append(act("open_container", container="target_flask", lid_position=lid))
    transfer = {"volume_ml": 10, "pipette_fresh": True, "tip_contact": "sterile_only", "approach": "side",
                "motion": "slow_gentle", "talking": False}
    transfer.update(spent or {})
    actions.append(act("remove_spent_medium", **transfer))
    actions.append(act("draw_sterility_sample", source="spent_medium", pipette_fresh=sample_fresh))
    actions.append(act("close_container", container="target_flask"))
    if open_turbid:
        actions.append(act("close_container", container="turbid_flask"))
    actions.append(act("decontaminate_waste", method=waste_method))
    actions.append(act("remove_item", item="waste_container", decontaminated=True))
    actions.append(act("load_item", item=lot, zone="clean_side", wiped=True))
    actions.append(act("open_container", container=lot, lid_position="held_above"))
    actions.append(act("open_container", container="target_flask", lid_position="held_above"))
    transfer = {"volume_ml": 12, "pipette_fresh": True, "tip_contact": "sterile_only", "approach": "side",
                "motion": "slow_gentle", "talking": False}
    transfer.update(fresh or {})
    actions.append(act("add_fresh_medium", **transfer))
    if antibiotics:
        actions.append(act("load_item", item="antibiotics", zone="clean_side", wiped=True))
        actions.append(act("add_antibiotics"))
    actions.append(act("draw_sterility_sample", source="fresh_medium", pipette_fresh=sample_fresh))
    actions.append(act("close_container", container="target_flask"))
    actions.append(act("close_container", container=lot))
    actions.append(act("remove_item", item=lot, decontaminated=True))
    if antibiotics:
        actions.append(act("remove_item", item="antibiotics", decontaminated=True))
    actions.append(act("remove_item", item="sterility_broth", decontaminated=True))
    for item, _ in extra_loads:
        actions.append(act("remove_item", item=item, decontaminated=True))
    if mycoplasma:
        actions.append(act("submit_mycoplasma_test"))
    for days, temperature_c in incubations:
        actions.append(act("incubate_samples", days=days, temperature_c=temperature_c))
    actions.append(act("inspect_samples"))
    actions.append(act("dispose_flask", container="turbid_flask", containment=containment,
                       decontaminated=dispose_decontaminated))
    actions.append(act("sanitize_gloves", agent="sterile_alcohol70"))
    for item in [name for name, _ in used_loads if name in {"target_flask", "pipettes", "pipette_aid"}]:
        actions.append(act("remove_item", item=item, decontaminated=True))
    actions.append(act("final_clean", agent=final_agent))
    return actions + [act("finish_session")]


@pytest.mark.parametrize("seed", range(20))
def test_aseptic_correct_run_meets_every_checkpoint(library, seed):
    model = library.get(ASEPTIC)
    view = replay(model, seed, "practice", aseptic_run(model, seed)).view()
    met = checkpoint_map(view)
    assert all(value for value in met.values() if value is not None), met
    assert view["debrief"]["all_critical_met"]


def test_aseptic_replay_is_deterministic(library):
    model = library.get(ASEPTIC)
    seed = seed_where(model, lambda h: h["mollicute_lot"] == aseptic_valid_lot(h))
    actions = aseptic_run(model, seed)
    first = replay(model, seed, "practice", actions).view()
    assert first == replay(model, seed, "practice", actions).view()
    assert any("positive" in note for note in first["debrief"]["revealed"])


def test_aseptic_expired_medium_is_flagged(library):
    model = library.get(ASEPTIC)
    view = replay(model, 4, "practice", aseptic_run(model, 4, lot=aseptic_lot(model, 4, "expired"))).view()
    assert checkpoint_map(view)["medium-in-date"] is False
    assert any("expired" in note for note in view["debrief"]["revealed"])


def test_aseptic_dirty_interior_and_technique_errors_are_flagged(library):
    model = library.get(ASEPTIC)
    seed = seed_where(model, lambda h: h["dirty_interior"])
    actions = aseptic_run(model, seed, disinfect=False, lid="face_down_surface",
                          spent={"pipette_fresh": False, "tip_contact": "dirty_cabinet_surface",
                                 "approach": "over_open_container", "motion": "rapid", "talking": True})
    view = replay(model, seed, "practice", actions).view()
    met = checkpoint_map(view)
    for key in ("interior-disinfected-before-work", "caps-never-face-down", "side-approach-not-over",
                "slow-gentle-manipulation", "fresh-pipette-per-flask", "sterile-items-touch-nothing-dirty"):
        assert met[key] is False, key
    assert any("present" in note for note in view["debrief"]["revealed"])


def test_aseptic_layout_and_cell_line_rules_are_flagged(library):
    model = library.get(ASEPTIC)
    seed = 0
    expired = aseptic_lot(model, seed, "expired")
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, extra_loads=[("other_line_flask", "clean_side")])).view())
    assert met["one-cell-line-only"] is False
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, extra_loads=[(expired, "clean_side")])).view())
    assert met["bottles-one-at-a-time"] is False
    loads = [("target_flask", "stacked"), ("turbid_flask", "dirty_side"), ("pipettes", "front_grille"),
             ("pipette_aid", "clean_side"), ("sterility_broth", "clean_side"), ("waste_container", "dirty_side")]
    met = checkpoint_map(replay(model, seed, "practice", aseptic_run(model, seed, loads=loads)).view())
    for key in ("no-inside-stacking", "grilles-and-opening-clear", "clean-to-dirty-arrangement"):
        assert met[key] is False, key


def test_aseptic_hidden_mollicutes_need_a_dedicated_test(library):
    model = library.get(ASEPTIC)
    seed = seed_where(model, lambda h: h["mollicute_lot"] == aseptic_valid_lot(h))
    view = replay(model, seed, "practice", aseptic_run(model, seed)).view()
    assert checkpoint_map(view)["mycoplasma-test-requested"] is True
    assert any("positive" in event["text"] for event in view["log"][-1]["events"])
    missed = replay(model, seed, "practice", aseptic_run(model, seed, mycoplasma=False)).view()
    assert checkpoint_map(missed)["mycoplasma-test-requested"] is False
    assert any("not submitted" in note for note in missed["debrief"]["revealed"])


def test_aseptic_visible_medium_contamination_is_detected_after_incubation(library):
    model = library.get(ASEPTIC)
    seed = seed_where(model, lambda h: h["visible_medium_lot"] == aseptic_valid_lot(h))
    view = replay(model, seed, "practice", aseptic_run(model, seed)).view()
    assert any("fresh-medium control: turbid" in event["text"] for entry in view["log"] for event in entry["events"])


def test_aseptic_antibiotics_mask_contamination(library):
    model = library.get(ASEPTIC)
    seed = seed_where(model, lambda h: h["dirty_interior"])
    actions = aseptic_run(model, seed, disinfect=False, antibiotics=True,
                          fresh={"tip_contact": "dirty_cabinet_surface"})
    view = replay(model, seed, "practice", actions).view()
    assert checkpoint_map(view)["no-antibiotic-rescue"] is False
    assert any("deceptively clear" in event["text"] for event in view["log"][-1]["events"])


def test_aseptic_incubation_rules_are_checked(library):
    model = library.get(ASEPTIC)
    seed = 0
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, incubations=((10, 22),))).view())
    assert met["sterility-samples-incubated"] is False and met["dual-temperature-incubation"] is False
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, incubations=((7, 32), (7, 22)))).view())
    assert met["dual-temperature-incubation"] is False
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, incubations=((7, 22), (7, 37)))).view())
    assert met["sterility-samples-incubated"] is False and met["dual-temperature-incubation"] is False


def test_aseptic_containment_waste_and_cleanup_rules(library):
    model = library.get(ASEPTIC)
    seed = 0
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, waste_method="no_treatment")).view())
    assert met["waste-decontaminated"] is False
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, open_turbid=True, containment="open_bench_trash",
                                            dispose_decontaminated=False)).view())
    assert met["contaminated-flasks-contained"] is False
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, disinfect=False, uv=True)).view())
    assert met["uv-not-a-substitute"] is False and met["interior-disinfected-before-work"] is False
    met = checkpoint_map(replay(model, seed, "practice",
                                aseptic_run(model, seed, final_agent="water")).view())
    assert met["post-session-clean"] is False




# filter-sterilize-and-qc-a-supplemented-medium -------------------------------

MEDIA = "filter-sterilize-and-qc-a-supplemented-medium"


def lot_id(model, component):
    if component == "basal":
        return model.parameters["basal_lot_id"]
    if component == "filter":
        return model.parameters["filter_lot_id"]
    return model.parameters[f"{component}_id"]


def used_component(hidden_state, component):
    if component is None:
        return False
    if component == "basal":
        return True
    if component.startswith("serum_lot_"):
        return component != hidden_state["expired_serum_lot"]
    return component != hidden_state["warm_glutamine_aliquot"]


def result_from(view):
    return view["log"][-1]["events"][0]["data"]["batch_result"]


def media_run(model, seed, *, inspect=True, serum_lot=None, serum_volume=50, glutamine_aliquot=None,
              glutamine_volume=5, ph_method="calibrated_ph_meter", osmolality_method="osmometer",
              pore=0.22, membrane="pvdf", collection_bottle=None, pre_rinsed=True, aseptic=True,
              integrity="bubble_point", label=None, draw_control=True, control_volume=10, fresh_pipette=True,
              incubations=((7, 22), (7, 32)), mycoplasma=True, temperature=4,
              light_protected=True, release_status="quarantine_until_qc", aliquots=((4, 50),)):
    state = hidden(model, seed)
    serum_lot = serum_lot or next(lot for lot in ("serum_lot_a", "serum_lot_b") if lot != state["expired_serum_lot"])
    glutamine_aliquot = glutamine_aliquot or next(
        lot for lot in ("glutamine_aliquot_a", "glutamine_aliquot_b") if lot != state["warm_glutamine_aliquot"])
    collection_bottle = collection_bottle or next(
        bottle for bottle in ("bottle_a", "bottle_b") if bottle != state["unlabeled_bottle"])
    complete_label = {
        "medium_name": "MEM-serum-glutamine", "prepared_on": "2026-11-15",
        "expires_on": "2026-11-29", "cell_line": "synthetic-line-1",
        "basal_lot_id": lot_id(model, "basal"), "serum_lot_id": lot_id(model, serum_lot),
        "glutamine_lot_id": lot_id(model, glutamine_aliquot), "filter_lot_id": lot_id(model, "filter"),
        "component_lots_linked": True,
    }
    if label:
        complete_label.update(label)
    actions = []
    if inspect:
        actions.append(act("inspect_supplies"))
    actions += [
        act("add_serum", lot=serum_lot, volume_ml=serum_volume),
        act("add_glutamine", aliquot=glutamine_aliquot, volume_ml=glutamine_volume),
        act("measure_prefiltration_qc", ph_method=ph_method, osmolality_method=osmolality_method),
        act("select_filter", pore_size_um=pore, membrane=membrane),
        act("filter_medium", collection_bottle=collection_bottle, pre_rinsed=pre_rinsed, aseptic_assembly=aseptic),
        act("test_filter_integrity", method=integrity),
    ]
    if draw_control:
        actions.append(act("draw_sterility_control", volume_ml=control_volume, fresh_pipette=fresh_pipette))
    for count, volume in aliquots:
        actions.append(act("aliquot_medium", count=count, volume_each_ml=volume))
    actions.append(act("label_bottle", **complete_label))
    if draw_control:
        for days, temperature_c in incubations:
            actions.append(act("incubate_sterility_control", days=days, temperature_c=temperature_c))
    if mycoplasma:
        actions.append(act("submit_mycoplasma_lot_test"))
    actions += [
        act("store_medium", temperature_c=temperature, light_protected=light_protected, release_status=release_status),
        act("finish_preparation"),
    ]
    return actions


@pytest.mark.parametrize("seed", range(20))
def test_media_correct_run_meets_every_checkpoint(library, seed):
    model = library.get(MEDIA)
    view = replay(model, seed, "practice", media_run(model, seed)).view()
    assert all(checkpoint_map(view).values()), (seed, checkpoint_map(view))
    assert view["debrief"]["all_critical_met"]
    result = view["log"][-1]["events"][0]["data"]["batch_result"]
    assert result["composition"] == {
        "final_volume_ml": 500, "basal_volume_ml": 445, "serum_volume_ml": 50,
        "serum_final_percent": 10, "glutamine_volume_ml": 5,
        "glutamine_final_mm": 2, "glutamine_final_fold": 1,
    }
    assert result["prefiltration_qc"]["osmolality_mosm_kg"] == pytest.approx(292.1)
    assert result["inventory"]["unallocated_volume_ml"] == pytest.approx(280)
    assert result["filtration"]["filter"]["lot_id"] == lot_id(model, "filter")
    selected_serum = next(entry for entry in view["log"] if entry["name"] == "add_serum")["params"]["lot"]
    selected_glutamine = next(entry for entry in view["log"] if entry["name"] == "add_glutamine")["params"]["aliquot"]
    assert result["label"]["basal_lot_id"] == lot_id(model, "basal")
    assert result["label"]["serum_lot_id"] == lot_id(model, selected_serum)
    assert result["label"]["glutamine_lot_id"] == lot_id(model, selected_glutamine)
    assert result["label"]["filter_lot_id"] == lot_id(model, "filter")


def test_media_replay_is_deterministic_seed_dependent_and_structured(library):
    model = library.get(MEDIA)
    actions = media_run(model, 8)
    first = replay(model, 8, "practice", actions).view()
    assert first == replay(model, 8, "practice", actions).view()
    signatures = {(hidden(model, seed)["expired_serum_lot"], hidden(model, seed)["warm_glutamine_aliquot"],
                   hidden(model, seed)["unlabeled_bottle"]) for seed in range(12)}
    assert len(signatures) > 1
    qc = result_from(first)["qc_outcome"]
    assert qc["mycoplasma"]["result"] in {"positive", "negative"}
    assert qc["mycoplasma_result"] == qc["mycoplasma"]["result"]
    assert qc["sterility_control"]["status"] == "no_visible_growth"


def test_media_expired_serum_is_rejected_by_checkpoint(library):
    model = library.get(MEDIA)
    seed = 4
    lot = hidden(model, seed)["expired_serum_lot"]
    view = replay(model, seed, "practice", media_run(model, seed, serum_lot=lot)).view()
    assert checkpoint_map(view)["serum-in-date"] is False
    assert any("Expired serum" in note for note in view["debrief"]["revealed"])


def test_media_room_temperature_glutamine_is_flagged(library):
    model = library.get(MEDIA)
    seed = 3
    aliquot = hidden(model, seed)["warm_glutamine_aliquot"]
    view = replay(model, seed, "practice", media_run(model, seed, glutamine_aliquot=aliquot)).view()
    assert checkpoint_map(view)["glutamine-aliquot-cold"] is False


def test_media_wrong_stock_volumes_change_composition_and_checkpoint(library):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2, serum_volume=25, glutamine_volume=10)).view()
    assert checkpoint_map(view)["supplement-volumes"] is False
    result = view["log"][-1]["events"][0]["data"]["batch_result"]
    assert result["composition"]["basal_volume_ml"] == 465
    assert result["composition"]["glutamine_final_mm"] == 4


def test_media_pH_and_osmolality_require_real_measurement_methods(library):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2, ph_method="phenol_red_colour", osmolality_method="visual_estimate")).view()
    assert checkpoint_map(view)["prefiltration-qc"] is False
    result = view["log"][-1]["events"][0]["data"]["batch_result"]
    assert result["prefiltration_qc"] == {"ph": None, "osmolality_mosm_kg": None}


def test_media_filter_selection_priming_and_assembly_are_checked(library):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2, pore=0.45, membrane="cellulose", pre_rinsed=False, aseptic=False)).view()
    assert checkpoint_map(view)["correct-filter"] is False
    assert checkpoint_map(view)["filter-integrity-verified"] is True


def test_media_visual_inspection_is_not_an_integrity_test(library):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2, integrity="visual_only")).view()
    assert checkpoint_map(view)["filter-integrity-verified"] is False


def test_media_unlabelled_receiving_bottle_is_flagged(library):
    model = library.get(MEDIA)
    seed = 5
    bottle = hidden(model, seed)["unlabeled_bottle"]
    view = replay(model, seed, "practice", media_run(model, seed, collection_bottle=bottle)).view()
    assert checkpoint_map(view)["labeled-collection-bottle"] is False


def test_media_control_sample_and_incubation_rules_are_checked(library):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2, control_volume=5, fresh_pipette=False, incubations=((10, 22),))).view()
    met = checkpoint_map(view)
    assert met["sterility-samples-incubated"] is False and met["dual-temperature-incubation"] is False
    view = replay(model, 2, "practice", media_run(model, 2, incubations=((7, 32), (7, 22)))).view()
    assert checkpoint_map(view)["dual-temperature-incubation"] is False
    view = replay(model, 2, "practice", media_run(model, 2, incubations=((7, 22), (7, 37)))).view()
    assert checkpoint_map(view)["sterility-samples-incubated"] is False


def test_media_mollicutes_pass_the_filter_and_need_the_dedicated_test(library):
    model = library.get(MEDIA)
    def used_hidden_lot(h):
        lot = h["mollicute_lot"]
        return (lot == "basal" or lot == next(x for x in ("serum_lot_a", "serum_lot_b") if x != h["expired_serum_lot"])
                or lot == next(x for x in ("glutamine_aliquot_a", "glutamine_aliquot_b") if x != h["warm_glutamine_aliquot"]))
    seed = seed_where(model, used_hidden_lot)
    view = replay(model, seed, "practice", media_run(model, seed)).view()
    assert checkpoint_map(view)["mycoplasma-test-requested"] is True
    assert view["log"][-1]["events"][-1]["text"].endswith("mycoplasma result: positive.")
    missed = replay(model, seed, "practice", media_run(model, seed, mycoplasma=False)).view()
    assert checkpoint_map(missed)["mycoplasma-test-requested"] is False
    assert missed["log"][-1]["events"][-1]["text"].endswith("mycoplasma result: not_submitted.")


@pytest.mark.parametrize("mycoplasma_case", ["not_requested", "negative", "positive"])
@pytest.mark.parametrize("control_case,expected_status,expected_growth", [
    ("absent", "not_drawn", None),
    ("insufficient", "insufficient_incubation", None),
    ("valid_negative", "no_visible_growth", False),
    ("valid_positive", "visible_growth", True),
])
def test_media_control_and_mycoplasma_result_matrix(library, control_case, expected_status, expected_growth, mycoplasma_case):
    model = library.get(MEDIA)
    if mycoplasma_case == "positive":
        seed = seed_where(model, lambda h: used_component(h, h["mollicute_lot"]))
    elif mycoplasma_case == "negative":
        seed = seed_where(model, lambda h: not used_component(h, h["mollicute_lot"]))
    else:
        seed = 2
    draw_control = control_case != "absent"
    incubations = ((3, 22),) if control_case == "insufficient" else ((7, 22), (7, 32))
    view = replay(model, seed, "practice", media_run(
        model, seed, draw_control=draw_control, incubations=incubations,
        aseptic=control_case != "valid_positive", mycoplasma=mycoplasma_case != "not_requested",
    )).view()
    qc = result_from(view)["qc_outcome"]
    control = qc["sterility_control"]
    mycoplasma = qc["mycoplasma"]
    expected_mycoplasma = "not_submitted" if mycoplasma_case == "not_requested" else mycoplasma_case
    assert control["status"] == expected_status
    assert control["control_drawn"] is draw_control
    assert control["visible_growth"] is expected_growth
    assert control["schedule_complete"] is (control_case in {"valid_negative", "valid_positive"})
    assert mycoplasma == {
        "requested": mycoplasma_case != "not_requested",
        "result": expected_mycoplasma,
    }
    assert qc["visible_growth"] is expected_growth
    assert qc["mycoplasma_result"] == expected_mycoplasma
    consequence = view["log"][-1]["events"][-1]["text"]
    assert consequence.endswith(f"dedicated mycoplasma result: {expected_mycoplasma}.")
    if control_case == "absent":
        assert consequence.startswith("Sterility control: not drawn;")
    elif control_case == "insufficient":
        assert consequence.startswith("Sterility control: insufficient/incubation incomplete")
        assert "no visible growth after" not in consequence
    elif control_case == "valid_negative":
        assert consequence.startswith("Sterility control: no visible growth after the complete dual-temperature schedule;")
    else:
        assert consequence.startswith("Sterility control: visible growth observed;")


def test_media_requested_mycoplasma_outcome_is_private_until_finish(library):
    model = library.get(MEDIA)
    seed = seed_where(model, lambda h: used_component(h, h["mollicute_lot"]))
    view = replay(model, seed, "practice", media_run(model, seed)[:-2]).view()
    assert view["debrief"] is None
    public_log = json.dumps(view["log"])
    assert "mycoplasma result: positive" not in public_log
    assert '"result": "positive"' not in public_log
    finished = replay(model, seed, "practice", media_run(model, seed)).view()
    assert result_from(finished)["qc_outcome"]["mycoplasma"]["result"] == "positive"


def test_media_guided_receiver_coaching_requires_inspection(library):
    model = library.get(MEDIA)
    seed = 5
    bottle = hidden(model, seed)["unlabeled_bottle"]
    private = replay(model, seed, "guided", media_run(
        model, seed, inspect=False, collection_bottle=bottle,
    )).view()
    filter_log = next(entry for entry in private["log"] if entry["name"] == "filter_medium")
    warnings = [event["text"] for event in filter_log["events"] if event["kind"] == "warning"]
    assert warnings == ["Inspect supply and receiving-bottle records before selecting a receiver."]
    assert all("unlabelled" not in warning and "identity and history" not in warning for warning in warnings)

    inspected = replay(model, seed, "guided", media_run(model, seed, collection_bottle=bottle)).view()
    filter_log = next(entry for entry in inspected["log"] if entry["name"] == "filter_medium")
    warnings = [event["text"] for event in filter_log["events"] if event["kind"] == "warning"]
    assert "The selected receiving bottle is unlabelled; its identity and history are unknown." in warnings


def test_media_inspection_and_filter_selection_supply_original_lot_id_evidence(library):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2)).view()
    inspection = view["log"][0]["events"][0]
    assert inspection["data"]["lot_ids"] == {
        component: lot_id(model, component)
        for component in ("basal", "serum_lot_a", "serum_lot_b", "glutamine_aliquot_a", "glutamine_aliquot_b")
    }
    assert inspection["data"]["filter_lot_id"] == lot_id(model, "filter")
    selection = next(entry for entry in view["log"] if entry["name"] == "select_filter")
    assert selection["events"][0]["data"] == {"lot_id": lot_id(model, "filter")}
    label = result_from(view)["label"]
    assert label["component_lots_linked"] is True
    assert all(label[f"{field}_lot_id"] for field in ("basal", "serum", "glutamine", "filter"))


@pytest.mark.parametrize("field", ["basal_lot_id", "serum_lot_id", "glutamine_lot_id", "filter_lot_id"])
def test_media_wrong_lot_ids_fail_despite_self_attestation(library, field):
    model = library.get(MEDIA)
    view = replay(model, 2, "practice", media_run(model, 2, label={field: "wrong-lot"})).view()
    assert checkpoint_map(view)["complete-label-and-lot-trace"] is False


def test_media_missing_lot_ids_are_rejected(library):
    model = library.get(MEDIA)
    actions = media_run(model, 2)
    label_action = next(action for action in actions if action["name"] == "label_bottle")
    for field in ("basal_lot_id", "serum_lot_id", "glutamine_lot_id", "filter_lot_id"):
        del label_action["params"][field]
    with pytest.raises(ActionRejected, match="basal-medium lot id"):
        replay(model, 2, "practice", actions)


def test_media_nonaseptic_filtration_produces_visible_growth_only_after_incubation(library):
    model = library.get(MEDIA)
    early_actions = media_run(model, 2, aseptic=False)[:-5]
    early = replay(model, 2, "practice", early_actions).view()
    assert "turbid" not in json.dumps(early["panels"])
    view = replay(model, 2, "practice", media_run(model, 2, aseptic=False)).view()
    assert checkpoint_map(view)["correct-filter"] is False
    assert view["log"][-1]["events"][-1]["text"].startswith("Sterility control: visible growth observed")


def test_media_label_storage_and_release_are_independent_checkpoints(library):
    model = library.get(MEDIA)
    bad_label = {"medium_name": "medium", "prepared_on": "2026-11-15", "expires_on": "2026-11-15",
                 "cell_line": "unknown", "component_lots_linked": False}
    met = checkpoint_map(replay(model, 2, "practice", media_run(model, 2, label=bad_label)).view())
    assert met["complete-label-and-lot-trace"] is False
    met = checkpoint_map(replay(model, 2, "practice", media_run(model, 2, temperature=22, light_protected=False)).view())
    assert met["cold-dark-storage"] is False
    met = checkpoint_map(replay(model, 2, "practice", media_run(model, 2, release_status="release_immediately")).view())
    assert met["release-pending-qc"] is False


def test_media_late_inspection_is_not_accepted(library):
    model = library.get(MEDIA)
    actions = media_run(model, 2, inspect=False)
    actions.insert(1, act("inspect_supplies"))
    view = replay(model, 2, "practice", actions).view()
    assert checkpoint_map(view)["supplies-inspected"] is False


@pytest.mark.parametrize("name,params,message", [
    ("add_serum", {"lot": "serum_lot_a"}, "needs a value"),
    ("add_serum", {"lot": "unknown", "volume_ml": 50}, "listed options"),
    ("add_serum", {"lot": "serum_lot_a", "volume_ml": True}, "must be a number"),
    ("add_glutamine", {"aliquot": "glutamine_aliquot_a", "volume_ml": 0, "extra": 1}, "Unknown parameter"),
    ("incubate_sterility_control", {"days": 7.5, "temperature_c": 22}, "whole number"),
])
def test_media_malformed_parameters_are_rejected(library, name, params, message):
    model = library.get(MEDIA)
    with pytest.raises(ActionRejected, match=message):
        replay(model, 1, "practice", [act(name, **params)])


def test_media_impossible_sequence_and_overallocation_are_rejected(library):
    model = library.get(MEDIA)
    with pytest.raises(ActionRejected, match="pre-filtration QC"):
        replay(model, 1, "practice", [act("filter_medium", collection_bottle="bottle_a", pre_rinsed=True, aseptic_assembly=True)])
    actions = media_run(model, 2, aliquots=((10, 100),))
    with pytest.raises(ActionRejected, match="exceeds"):
        replay(model, 2, "practice", actions)


def test_media_hidden_lots_are_not_exposed_before_inspection_or_finish(library):
    model = library.get(MEDIA)
    public = public_protocol(model.definition)
    assert "checkpoints" not in public and "parameters" not in public
    view = replay(model, 1, "practice", []).view()
    assert view["debrief"] is None and view["log"] == []
    text = json.dumps(view["panels"])
    for key in ("expired_serum_lot", "warm_glutamine_aliquot", "unlabeled_bottle", "mollicute_lot", "visible_contaminant_lot"):
        assert key not in text
    assert lot_id(model, "basal") not in text
    inspected = replay(model, 1, "practice", [act("inspect_supplies")]).view()
    assert "mollicute_lot" not in json.dumps(inspected)
    assert inspected["debrief"] is None


# passage-an-adherent-line-to-a-target-density --------------------------------

PASSAGE = "passage-an-adherent-line-to-a-target-density"


def passage_run(model, seed, *, disposition="proceed", entered_confluence=None,
                wash_solution="calcium_magnesium_free_bss", wash_volume=15,
                reagent_kind="enzyme_based", reagent_volume=3.75, minutes=2,
                detachment_override=None, neutralization=7.5,
                rcf=200, collection_minutes=5, resuspension_volume=6.0,
                sample_ul=10, dye_ul=10, wrong_tallies=False, wrong_calculation=None,
                flask_count=2, target_cells=500000, final_volume=12.0,
                seed_volume_override=None, previous_passage=12, previous_pdl=18,
                pdl_override=None, temperature=37, co2=5, hours=24):
    h = hidden(model, seed)
    actions = [
        act("inspect_culture", confluence_pct=h["confluence_pct"] if entered_confluence is None else entered_confluence),
        act("decide_culture", disposition=disposition),
    ]
    if disposition != "proceed":
        return actions
    actions += [
        act("remove_medium"),
        act("wash_cells", solution=wash_solution, volume_ml=wash_volume),
        act("add_dissociation_reagent", reagent=reagent_kind, volume_ml=reagent_volume),
        act("incubate_dissociation", minutes=minutes),
    ]
    state, _ = run_state(model, seed, "practice", actions)
    detached = state["actual_detachment"] if detachment_override is None else detachment_override
    actions += [
        act("check_detachment", detached_pct=detached),
        act("neutralize", volume_ml=neutralization),
        act("centrifuge_and_resuspend", rcf_g=rcf, minutes=collection_minutes, final_volume_ml=resuspension_volume),
        act("prepare_count", sample_ul=sample_ul, dye_ul=dye_ul),
    ]
    state, _ = run_state(model, seed, "practice", actions)
    tallies = state["display_counts"]
    if wrong_tallies:
        tallies = {chamber: dict(values) for chamber, values in tallies.items()}
        tallies["A"]["unstained"] += 1
    viable = sum(tally["unstained"] for tally in tallies.values())
    total = viable + sum(tally["stained"] for tally in tallies.values())
    dilution = (sample_ul + dye_ul) / sample_ul
    calculated_concentration = (viable / 2) / 0.0001 * dilution
    calculated_viability = 100 * viable / total if total else 0
    if wrong_calculation == "concentration":
        calculated_concentration *= 1.1
    elif wrong_calculation == "viability":
        calculated_viability = max(0, calculated_viability - 10)
    actions.append(act("record_count",
                       chamber_a_unstained=tallies["A"]["unstained"], chamber_a_stained=tallies["A"]["stained"],
                       chamber_b_unstained=tallies["B"]["unstained"], chamber_b_stained=tallies["B"]["stained"],
                       viable_concentration_cells_ml=calculated_concentration, viability_pct=calculated_viability))
    state, _ = run_state(model, seed, "practice", actions)
    expected = model.expected(state)
    required = target_cells / expected["concentration_cells_ml"]
    seed_volume = required if seed_volume_override is None else seed_volume_override
    actions += [
        act("calculate_seed_volume", flask_count=flask_count,
            target_viable_cells_per_flask=target_cells, final_volume_ml_per_flask=final_volume,
            seed_volume_ml_per_flask=seed_volume),
        act("seed_flasks"),
    ]
    state, _ = run_state(model, seed, "practice", actions)
    pdl = model.expected(state)["pdl_increment"] if pdl_override is None else pdl_override
    actions += [
        act("label_flasks", previous_passage_number=previous_passage,
            previous_cumulative_pdl=previous_pdl, pdl_increment=pdl),
        act("incubate_and_finish", temperature_c=temperature, co2_pct=co2, hours=hours),
    ]
    return actions


def normal_seed(model):
    return seed_where(model, lambda h: not h["overconfluent"])


def test_passage_correct_run_meets_every_applicable_checkpoint_and_returns_structure(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    actions = passage_run(model, seed)
    view = replay(model, seed, "practice", actions).view()
    met = checkpoint_map(view)
    assert all(value for value in met.values() if value is not None), met
    assert met["overconfluent-refused"] is None
    assert view["debrief"]["all_critical_met"]
    result = view["log"][-1]["events"][0]["data"]["result"]
    assert result["included_unstained_cells"] == 121
    assert result["included_stained_cells"] == 9
    assert result["concentration_cells_ml"] == pytest.approx(1.21e6)
    assert result["viability_pct"] == pytest.approx(100 * 121 / 130)
    assert result["resuspension_volume_ml"] == pytest.approx(6.0)
    assert result["remaining_suspension_volume_ml"] == pytest.approx(5.99)
    assert result["viable_harvest_cells"] == pytest.approx(7.26e6)
    assert result["required_seed_volume_ml_per_flask"] == pytest.approx(500000 / 1210000)
    assert result["fresh_medium_ml_per_flask"] == pytest.approx(12 - 500000 / 1210000)
    assert result["viable_cells_seeded_per_flask"] == pytest.approx(500000)
    assert result["total_viable_cells_seeded"] == pytest.approx(1e6)
    assert result["pdl_increment"] == pytest.approx(2)
    assert result["new_passage_number"] == 13 and result["new_cumulative_pdl"] == 20
    assert result["incubation"] == {"temperature_c": 37.0, "co2_pct": 5.0, "hours": 24.0}
    assert "predicted_growth" not in result and "attachment_outcome" not in result


@pytest.mark.parametrize("seed", range(20))
def test_passage_correct_routine_runs_are_seed_robust(library, seed):
    model = library.get(PASSAGE)
    if hidden(model, seed)["overconfluent"]:
        pytest.skip("over-confluent branch tested separately")
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed)).view())
    assert all(value for value in met.values() if value is not None), (seed, met)


def test_passage_overconfluent_culture_is_refused_and_downstream_not_applicable(library):
    model = library.get(PASSAGE)
    seed = seed_where(model, lambda h: h["overconfluent"])
    actions = passage_run(model, seed, disposition="discard_overconfluent")
    view = replay(model, seed, "practice", actions).view()
    met = checkpoint_map(view)
    assert view["finished"] and met["culture-inspected"] and met["overconfluent-refused"]
    assert met["confluence-window"] is None
    assert all(value is None for key, value in met.items() if key not in {
        "culture-inspected", "confluence-window", "overconfluent-refused"})
    view = replay(model, seed, "practice", passage_run(model, seed)).view()
    assert checkpoint_map(view)["overconfluent-refused"] is False


def test_passage_inspection_and_normal_disposition_errors(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, entered_confluence=80 if hidden(model, seed)["confluence_pct"] != 80 else 79)).view())
    assert met["culture-inspected"] is False
    actions = passage_run(model, seed, disposition="discard_overconfluent")
    met = checkpoint_map(replay(model, seed, "practice", actions).view())
    assert met["confluence-window"] is False and met["overconfluent-refused"] is None


def test_passage_wash_and_reagent_choices_are_flagged(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, wash_solution="complete_medium")).view())
    assert met["wash-removes-inhibitors"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, reagent_volume=2)).view())
    assert met["dissociation-reagent-volume"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, reagent_kind="enzyme_free")).view())
    assert met["dissociation-reagent-volume"] is False and met["detachment-confirmed"] is False


def test_passage_overexposure_reduces_viability_and_changes_count_and_pdl(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    good_state, _ = run_state(model, seed, "practice", passage_run(model, seed))
    long_state, _ = run_state(model, seed, "practice", passage_run(model, seed, minutes=10))
    view = replay(model, seed, "practice", passage_run(model, seed, minutes=10)).view()
    met = checkpoint_map(view)
    assert met["dissociation-time-bounded"] is False and met["harvest-viability"] is False
    assert model.expected(long_state)["viability_pct"] < model.expected(good_state)["viability_pct"]
    assert model.expected(long_state)["pdl_increment"] < model.expected(good_state)["pdl_increment"]
    # Arithmetic remains self-consistent with the new displayed tallies.
    assert met["count-dilution-and-tallies"] and met["count-concentration-and-viability"]
    assert met["seed-volume-correct"] and met["passage-and-pdl-record"]


def test_passage_neutralization_collection_and_detachment_errors(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, neutralization=3.75)).view())
    assert met["neutralized-before-count"] is False and met["harvest-viability"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, rcf=800)).view())
    assert met["centrifuge-and-resuspension"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, detachment_override=90)).view())
    assert met["detachment-confirmed"] is False


def test_passage_count_transcription_dilution_and_calculation_rules(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, wrong_tallies=True)).view())
    assert met["count-dilution-and-tallies"] is False
    assert met["count-concentration-and-viability"] is True
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, dye_ul=20)).view())
    assert met["count-dilution-and-tallies"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, wrong_calculation="concentration")).view())
    assert met["count-concentration-and-viability"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, wrong_calculation="viability")).view())
    assert met["count-concentration-and-viability"] is False
    state, _ = run_state(model, seed, "practice", passage_run(model, seed))
    assert model.expected(state)["concentration_cells_ml"] == pytest.approx(1.21e6)


def test_passage_seed_target_volume_and_pdl_mistakes_are_flagged(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, seed_volume_override=0.45)).view())
    assert met["seed-volume-correct"] is False and met["passage-and-pdl-record"] is True
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, target_cells=400000)).view())
    assert met["seed-volume-correct"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, final_volume=10)).view())
    assert met["seed-volume-correct"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, previous_passage=11)).view())
    assert met["passage-and-pdl-record"] is False
    met = checkpoint_map(replay(model, seed, "practice", passage_run(model, seed, pdl_override=3)).view())
    assert met["passage-and-pdl-record"] is False


def test_passage_low_yield_negative_pdl_passes_action_schema_and_updates_cumulative(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    expected_pdl = -0.5849625007211562
    assert expected_pdl == pytest.approx(math.log2(2 / 3), abs=1e-15)
    actions = passage_run(model, seed, resuspension_volume=1.0, pdl_override=expected_pdl)
    view = replay(model, seed, "practice", actions).view()
    result = view["log"][-1]["events"][0]["data"]["result"]
    assert 1210000 / 1815000 == pytest.approx(2 / 3)
    assert expected_pdl < 0
    assert result["resuspension_volume_ml"] == pytest.approx(1.0)
    assert result["remaining_suspension_volume_ml"] == pytest.approx(0.99)
    assert result["viable_harvest_cells"] == pytest.approx(1210000)
    assert result["pdl_increment"] == pytest.approx(expected_pdl)
    assert result["new_cumulative_pdl"] == pytest.approx(17.415037499278844, abs=1e-12)
    assert 18 + expected_pdl == pytest.approx(17.415037499278844, abs=1e-12)
    label = next(action for action in actions if action["name"] == "label_flasks")
    assert label["params"]["pdl_increment"] == pytest.approx(expected_pdl)
    assert checkpoint_map(view)["passage-and-pdl-record"] is True
    with pytest.raises(ActionRejected, match="Current PDL increment must be between -20 and 20 PDL"):
        replay(model, seed, "practice", passage_run(
            model, seed, resuspension_volume=1.0, pdl_override=-20.001))


def test_passage_incubation_record_is_checked_without_growth_claim(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    view = replay(model, seed, "practice", passage_run(model, seed, temperature=35)).view()
    assert checkpoint_map(view)["incubation-and-result"] is False
    assert "no attachment or growth outcome is predicted" in view["log"][-1]["events"][0]["text"]


def test_passage_action_order_and_physical_feasibility_are_rejected(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    with pytest.raises(ActionRejected, match="Inspect the culture"):
        replay(model, seed, "practice", [act("remove_medium")])
    with pytest.raises(ActionRejected, match="before calculating"):
        replay(model, seed, "practice", passage_run(model, seed)[:2] + [
            act("calculate_seed_volume", flask_count=2, target_viable_cells_per_flask=500000,
                final_volume_ml_per_flask=12, seed_volume_ml_per_flask=0.4)])
    with pytest.raises(ActionRejected, match="enough viable cells"):
        replay(model, seed, "practice", passage_run(model, seed, target_cells=5000000))
    with pytest.raises(ActionRejected, match="cannot exceed"):
        replay(model, seed, "practice", passage_run(model, seed, seed_volume_override=13))


@pytest.mark.parametrize("plan_kind", ["required", "entered"])
def test_passage_seed_plan_accepts_exact_post_count_remaining_volume(library, plan_kind):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    sample_ul = 100
    remaining = 6.0 - sample_ul / 1000
    kwargs = {"sample_ul": sample_ul, "dye_ul": sample_ul}
    if plan_kind == "required":
        kwargs["target_cells"] = round(1210000 * remaining / 2)
    else:
        kwargs["seed_volume_override"] = remaining / 2
    state, _ = run_state(model, seed, "practice", passage_run(model, seed, **kwargs))
    result = model.expected(state)
    assert state["remaining_suspension_volume_ml"] == pytest.approx(remaining)
    assert result["remaining_suspension_volume_ml"] == pytest.approx(remaining)
    assert result["resuspension_volume_ml"] == pytest.approx(6.0)
    assert result["viable_harvest_cells"] == pytest.approx(7.26e6)
    assert result["pdl_increment"] == pytest.approx(2)


@pytest.mark.parametrize("plan_kind", ["required", "entered"])
def test_passage_seed_plan_rejects_just_above_post_count_remaining_volume(library, plan_kind):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    sample_ul = 100
    remaining = 6.0 - sample_ul / 1000
    kwargs = {"sample_ul": sample_ul, "dye_ul": sample_ul}
    if plan_kind == "required":
        kwargs["target_cells"] = round(1210000 * (remaining + 0.001) / 2)
        message = "remaining after the counting sample does not contain enough viable cells"
    else:
        kwargs["seed_volume_override"] = (remaining + 0.001) / 2
        message = "more suspension than remains after the counting sample"
    with pytest.raises(ActionRejected, match=message):
        replay(model, seed, "practice", passage_run(model, seed, **kwargs))


def test_passage_prepare_count_deducts_nondefault_sample_exactly_once(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    sample_ul = 25
    actions = passage_run(model, seed, sample_ul=sample_ul, dye_ul=sample_ul)
    prepare_index = next(index for index, action in enumerate(actions) if action["name"] == "prepare_count")
    through_count = actions[:prepare_index + 1]
    state, log = run_state(model, seed, "practice", through_count)
    assert state["resuspension_volume"] == pytest.approx(6.0)
    assert state["remaining_suspension_volume_ml"] == pytest.approx(5.975)
    assert log[prepare_index]["events"][0]["data"] == {
        "chambers": state["display_counts"],
        "dilution": 2.0,
        "count_sample_volume_ml": 0.025,
        "remaining_suspension_volume_ml": 5.975,
    }
    with pytest.raises(ActionRejected, match="counting mixture has already been prepared"):
        run_state(model, seed, "practice", through_count + [actions[prepare_index]])
    final_state, _ = run_state(model, seed, "practice", actions)
    assert final_state["remaining_suspension_volume_ml"] == pytest.approx(5.975)
    assert model.expected(final_state)["remaining_suspension_volume_ml"] == pytest.approx(5.975)
    assert model.expected(final_state)["pdl_increment"] == pytest.approx(2)


def test_passage_schema_rejects_malformed_parameters(library):
    model = library.get(PASSAGE)
    with pytest.raises(ActionRejected, match="number"):
        check_parameters(model.action_specs["inspect_culture"], {"confluence_pct": True})
    with pytest.raises(ActionRejected, match="whole number"):
        check_parameters(model.action_specs["inspect_culture"], {"confluence_pct": 80.5})
    with pytest.raises(ActionRejected, match="Unknown parameter"):
        check_parameters(model.action_specs["remove_medium"], {"volume_ml": 10})
    with pytest.raises(ActionRejected, match="listed options"):
        check_parameters(model.action_specs["decide_culture"], {"disposition": "maybe"})


def test_passage_replay_determinism_seed_dependence_and_hidden_privacy(library):
    model = library.get(PASSAGE)
    seed = normal_seed(model)
    actions = passage_run(model, seed)
    assert replay(model, seed, "practice", actions).view() == replay(model, seed, "practice", actions).view()
    confluences = {hidden(model, value)["confluence_pct"] for value in range(20)}
    detachments = {hidden(model, value)["base_detachment_pct"] for value in range(20)}
    assert len(confluences) > 1 and len(detachments) > 1
    over_seed = seed_where(model, lambda h: h["overconfluent"])
    state, _ = run_state(model, over_seed, "practice", [])
    public_text = json.dumps(model.visible(state)) + json.dumps(public_protocol(model.definition))
    assert "base_detachment" not in public_text and '"hidden"' not in public_text
    assert "Displayed confluence" not in json.dumps(model.visible(state))
    # The actual value becomes observable only through the inspection action.
    inspected = replay(model, over_seed, "practice", [act("inspect_culture", confluence_pct=95)]).view()
    assert inspected["panels"][0]["rows"][1] == ["Displayed confluence", "95%"]


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
