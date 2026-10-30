"""Gravimetric verification of an air-displacement micropipette."""

from __future__ import annotations

import random
import statistics

from .engine import ActionRejected, Event, ProtocolModel, coach

AIR_DENSITY = 0.0012  # g/mL, a typical laboratory value
WEIGHT_DENSITY = 8.0  # g/mL, conventional density of balance reference weights


def water_density(celsius: float) -> float:
    """Density of air-free water in g/mL, using the formula tabulated by Tanaka et al. (2001)."""
    a1, a2, a3, a4, a5 = -3.983035, 301.797, 522528.9, 69.34881, 999.974950
    t = celsius
    return a5 * (1 - (t + a1) ** 2 * (t + a2) / (a3 * (t + a4))) / 1000


def z_factor(celsius: float) -> float:
    """Conversion from balance reading (mg) to delivered volume (uL), with air buoyancy."""
    return (1 / (water_density(celsius) - AIR_DENSITY)) * (1 - AIR_DENSITY / WEIGHT_DENSITY)


class PipetteVerification(ProtocolModel):
    protocol_id = "micropipette-gravimetric-verification"

    def checkpoint_ids(self):
        return [
            "temperature-recorded", "nominal-volume", "tip-prewetted", "immersion-depth",
            "vertical-aspiration", "touch-off", "tare-before-each", "replicate-count",
            "report-mean", "report-systematic", "report-random", "report-verdict",
        ]

    def start(self, rng: random.Random) -> dict:
        p = self.parameters
        faulty = rng.random() < p["fault_probability"]
        if faulty:
            kind = rng.choice(["bias", "seal"])
            bias = rng.choice([-1, 1]) * rng.uniform(1.1, 2.2) / 100 if kind == "bias" else rng.uniform(-0.3, 0.3) / 100
            sd = rng.uniform(0.45, 0.8) / 100 if kind == "seal" else rng.uniform(0.08, 0.18) / 100
        else:
            kind = "none"
            bias = rng.uniform(-0.4, 0.4) / 100
            sd = rng.uniform(0.06, 0.18) / 100
        return {
            "hidden": {"bias": bias, "sd": sd, "fault": kind,
                       "water_c": round(rng.uniform(19.5, 23.5), 1)},
            "volume_ul": p["nominal_volume_ul"] / 2, "tip": None, "loaded": None,
            "temperature_read": None, "balance_mg": 0.0, "since_tare": [],
            "replicates": [], "deliveries": [], "aspirations": [], "report": None,
            "tared_before_dispense": [],
        }

    def visible(self, state):
        p = self.parameters
        tip = state["tip"]
        rows = [
            ["Pipette", f"{p['nominal_volume_ul']:g} µL adjustable air-displacement pipette"],
            ["Volume setting", f"{state['volume_ul']:g} µL"],
            ["Tip", "none" if tip is None else ("fitted, pre-wetted" if tip["prewet"] else "fitted, dry")],
            ["In tip", "nothing" if state["loaded"] is None else f"water (about {state['volume_ul']:g} µL)"],
        ]
        bench = [
            ["Balance", f"{state['balance_mg']:.1f} mg displayed (readability {p['balance_readability_mg']:g} mg)"],
            ["Water temperature", "not measured" if state["temperature_read"] is None
             else f"{state['temperature_read']:.1f} °C"],
            ["Readings recorded", str(len(state["replicates"]))],
        ]
        panels = [{"title": "Pipette", "rows": rows}, {"title": "Bench", "rows": bench}]
        if state["replicates"]:
            panels.append({"title": "Your balance readings after each dispense (mg)", "rows": [
                [f"Reading {i + 1}", f"{item['display_mg']:.1f}"] for i, item in enumerate(state["replicates"])
            ]})
        return panels

    # Actions -------------------------------------------------------------------

    def act_measure_water_temperature(self, state, rng):
        state["clock"] += 1
        state["temperature_read"] = state["hidden"]["water_c"]
        return [Event("readout", f"Test water reads {state['temperature_read']:.1f} °C.",
                      {"water_c": state["temperature_read"]})]

    def act_set_volume(self, state, rng, volume_ul):
        if state["loaded"] is not None:
            raise ActionRejected("Dispense the liquid in the tip before changing the volume")
        state["volume_ul"] = volume_ul
        state["clock"] += 0.2
        return [Event("info", f"Volume set to {volume_ul:g} µL.")]

    def act_fit_tip(self, state, rng):
        if state["tip"] is not None:
            raise ActionRejected("A tip is already fitted")
        state["tip"] = {"prewet": False, "used": False}
        state["clock"] += 0.2
        return [Event("info", "A new tip is fitted.")]

    def act_eject_tip(self, state, rng):
        if state["tip"] is None:
            raise ActionRejected("There is no tip to eject")
        state["tip"] = None
        state["loaded"] = None
        state["clock"] += 0.1
        return [Event("info", "The tip is ejected into the waste.")]

    def act_prewet(self, state, rng, cycles):
        if state["tip"] is None:
            raise ActionRejected("Fit a tip before pre-wetting")
        if state["loaded"] is not None:
            raise ActionRejected("Dispense the liquid in the tip first")
        if cycles >= 1:
            state["tip"]["prewet"] = True
        state["clock"] += 0.15 * cycles
        return [Event("info", f"The tip is filled and emptied {cycles} times in the reservoir and discarded to waste.")]

    def act_tare(self, state, rng):
        state["balance_mg"] = 0.0
        state["since_tare"] = []
        state["clock"] += 0.3
        return [Event("info", "The balance is tared with the weighing vessel in place.")]

    def act_aspirate(self, state, rng, immersion_mm, vertical):
        p = self.parameters
        if state["tip"] is None:
            raise ActionRejected("Fit a tip before aspirating")
        if state["loaded"] is not None:
            raise ActionRejected("The tip already holds liquid")
        events = []
        relative = 0.0
        low, high = p["immersion_mm_range"]
        if immersion_mm < 1:
            relative -= rng.uniform(0.02, 0.08)
            coach(state, events, "The tip barely touched the surface and drew in air.")
        elif immersion_mm < low:
            relative -= 0.002
            coach(state, events, f"Immerse the tip {low:g}–{high:g} mm; shallower risks drawing air.")
        elif immersion_mm > high:
            relative += 0.0015 * (immersion_mm - high)
            coach(state, events, f"The tip went deeper than {high:g} mm, so liquid clings to the outside.")
        if not vertical:
            relative -= 0.003
            coach(state, events, "Aspirate with the pipette held vertical; tilting changes the volume drawn.")
        if not state["tip"]["prewet"] and not state["tip"]["used"]:
            relative -= 0.003
            coach(state, events, "The first aspiration into a dry tip delivers less: pre-wet it first.")
        state["aspirations"].append({"immersion_mm": immersion_mm, "vertical": vertical,
                                     "prewet": state["tip"]["prewet"] or state["tip"]["used"]})
        state["loaded"] = {"relative": relative, "volume_ul": state["volume_ul"]}
        state["tip"]["used"] = True
        state["clock"] += 0.15
        events.insert(0, Event("info", "Water is aspirated from the reservoir."))
        return events

    def act_dispense(self, state, rng, touch_off):
        hidden = state["hidden"]
        if state["loaded"] is None:
            raise ActionRejected("The tip is empty")
        if len(state["deliveries"]) > len(state["replicates"]):
            raise ActionRejected("Record the balance reading for the previous dispense first")
        events = [Event("info", "The water is dispensed into the weighing vessel.")]
        loaded = state["loaded"]
        relative = loaded["relative"]
        if not touch_off:
            relative -= 0.002
            coach(state, events, "Touch the tip against the vessel wall so the last drop is delivered.")
        volume = loaded["volume_ul"] * (1 + hidden["bias"] + relative + rng.gauss(0, hidden["sd"]))
        mass = volume / z_factor(hidden["water_c"])
        state["tared_before_dispense"].append(not state["since_tare"])
        state["since_tare"].append(mass)
        state["balance_mg"] = sum(state["since_tare"])
        state["deliveries"].append({"volume_ul": loaded["volume_ul"], "touch_off": touch_off})
        state["loaded"] = None
        state["clock"] += 0.15
        return events

    def act_read_balance(self, state, rng):
        p = self.parameters
        if not state["deliveries"] or len(state["replicates"]) >= len(state["deliveries"]):
            raise ActionRejected("Record a reading after each dispense")
        state["clock"] += 0.3
        step = p["balance_readability_mg"]
        display = round(state["balance_mg"] / step) * step
        mass = state["since_tare"][-1]
        state["replicates"].append({
            "display_mg": display, "mass_mg": mass,
            "volume_ul": state["deliveries"][-1]["volume_ul"],
            "cumulative": len(state["since_tare"]) > 1,
        })
        return [Event("readout", f"The balance shows {display:.1f} mg.", {"mg": display})]

    def act_submit_report(self, state, rng, mean_volume_ul, systematic_error_pct, random_error_cv_pct, verdict):
        if len(state["replicates"]) < 2:
            raise ActionRejected("Record at least two readings before reporting")
        state["report"] = {
            "mean": mean_volume_ul, "systematic": systematic_error_pct,
            "cv": random_error_cv_pct, "verdict": verdict,
        }
        state["finished"] = True
        return [Event("info", "The verification record is submitted.")]

    # Evaluation ----------------------------------------------------------------

    def expected(self, state) -> dict | None:
        """What a correct analyst computes from the readings this learner recorded."""
        p = self.parameters
        temperature = state["temperature_read"]
        if temperature is None or len(state["replicates"]) < 2:
            return None
        masses, previous = [], 0.0
        for item in state["replicates"]:
            # A learner who did not tare must difference successive readings.
            masses.append(item["display_mg"] - previous if item["cumulative"] else item["display_mg"])
            previous = item["display_mg"]
        volumes = [m * z_factor(temperature) for m in masses]
        mean = statistics.fmean(volumes)
        nominal = p["nominal_volume_ul"]
        systematic = (mean - nominal) / nominal * 100
        cv = statistics.stdev(volumes) / mean * 100
        passes = abs(systematic) <= p["systematic_limit_pct"] and cv <= p["random_limit_pct"]
        return {"mean": mean, "systematic": systematic, "cv": cv, "verdict": "pass" if passes else "fail",
                "z": z_factor(temperature)}

    def evaluate(self, state):
        p = self.parameters
        reps = state["replicates"]
        low, high = p["immersion_mm_range"]
        asp = state["aspirations"]
        results = {}
        results["temperature-recorded"] = (
            state["temperature_read"] is not None,
            "Measured the water temperature, which sets the conversion from mass to volume."
            if state["temperature_read"] is not None else "The water temperature was never measured, so the "
            "density correction could not be chosen.")
        at_nominal = bool(reps) and all(item["volume_ul"] == p["nominal_volume_ul"] for item in reps)
        results["nominal-volume"] = (at_nominal, f"Readings were taken at {sorted({r['volume_ul'] for r in reps})} µL; "
                                     f"the test volume is the nominal {p['nominal_volume_ul']:g} µL.")
        dry = sum(1 for a in asp if not a["prewet"])
        results["tip-prewetted"] = (bool(asp) and dry == 0,
                                    "Every tip was pre-wetted before its first measured aspiration." if asp and not dry
                                    else f"{dry} measured aspiration(s) went into a dry tip.")
        depth_ok = bool(asp) and all(low <= a["immersion_mm"] <= high for a in asp)
        results["immersion-depth"] = (depth_ok, f"Immersion depths used: {sorted({a['immersion_mm'] for a in asp})} mm.")
        results["vertical-aspiration"] = (bool(asp) and all(a["vertical"] for a in asp),
                                          "Every aspiration was vertical." if asp and all(a["vertical"] for a in asp)
                                          else "At least one aspiration was tilted.")
        touched = bool(state["deliveries"]) and all(d["touch_off"] for d in state["deliveries"])
        results["touch-off"] = (touched, "Every dispense ended with a touch-off." if touched
                                else "At least one dispense left the last drop on the tip.")
        tared = bool(state["tared_before_dispense"]) and all(state["tared_before_dispense"])
        results["tare-before-each"] = (tared, "The balance was tared before each dispense." if tared
                                       else "Some readings were cumulative; they must be differenced.")
        results["replicate-count"] = (len(reps) >= p["replicates_required"],
                                      f"{len(reps)} readings recorded; the procedure asks for "
                                      f"{p['replicates_required']}.")
        expected = self.expected(state)
        report = state["report"]
        if expected is None or report is None:
            for key in ("report-mean", "report-systematic", "report-random", "report-verdict"):
                results[key] = (False, "No result can be checked without a temperature and at least two readings.")
            return results
        results["report-mean"] = (abs(report["mean"] - expected["mean"]) <= p["mean_tolerance_ul"],
                                  f"From your readings and Z = {expected['z']:.4f} µL/mg, the mean is "
                                  f"{expected['mean']:.2f} µL; you reported {report['mean']:g} µL.")
        results["report-systematic"] = (
            abs(report["systematic"] - expected["systematic"]) <= p["percent_tolerance"],
            f"Systematic error = (mean − nominal)/nominal × 100 = {expected['systematic']:.2f}%; "
            f"you reported {report['systematic']:g}%.")
        results["report-random"] = (
            abs(report["cv"] - expected["cv"]) <= p["percent_tolerance"],
            f"Random error as a coefficient of variation = s/mean × 100 = {expected['cv']:.3f}%; "
            f"you reported {report['cv']:g}%.")
        results["report-verdict"] = (
            report["verdict"] == expected["verdict"],
            f"Against the limits of ±{p['systematic_limit_pct']:g}% systematic and {p['random_limit_pct']:g}% "
            f"random, your data give '{expected['verdict']}'; you reported '{report['verdict']}'.")
        return results

    def reveal(self, state):
        hidden = state["hidden"]
        fault = {"none": "no fault", "bias": "a calibration offset", "seal": "a worn piston seal"}[hidden["fault"]]
        return [
            f"This pipette had {fault}: true bias {hidden['bias'] * 100:+.2f}% and random spread "
            f"{hidden['sd'] * 100:.2f}% before any technique error.",
            "Technique errors (dry tip, depth, angle, missed touch-off) add to what the pipette itself does, "
            "so a sound pipette can fail a check run carelessly.",
        ]
