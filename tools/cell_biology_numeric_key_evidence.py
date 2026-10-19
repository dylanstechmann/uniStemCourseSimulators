"""Recompute public Cell Biology formative numeric keys into a review artifact.

The calculator inventory is limited to the 23 numeric items in the public
practice bank. It reads no inactive candidate answer source and does not
establish independent review, course quality, or release readiness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import course_package_digest  # noqa: E402

COURSE_ID = "cell-biology"
COURSE_ROOT = ROOT / "content/courses/cell-biology"
QUESTION_BANK_RELATIVE = "question-banks/practice.json"


def _spec(
    question_id: str,
    formula: str,
    inputs: dict[str, int | float | str],
    prompt_anchor: str,
    compute: Callable[[dict[str, int | float | str]], float],
    *,
    rounding: str = "none",
) -> dict[str, Any]:
    return {
        "question_id": question_id,
        "formula": formula,
        "inputs": inputs,
        "prompt_anchor": prompt_anchor,
        "rounding": rounding,
        "compute": compute,
    }


def _numeric_specs() -> list[dict[str, Any]]:
    return [
        _spec(
            "cell-biology-3:check",
            "Vmax × [S] / (Km + [S])",
            {"vmax_umol_min": 120, "km_mM": 3, "substrate_mM": 6},
            "Vmax = 120 μmol·min⁻¹ and Km = 3 mM",
            lambda v: v["vmax_umol_min"] * v["substrate_mM"] / (v["km_mM"] + v["substrate_mM"]),
        ),
        _spec(
            "cell-biology-3:delta-g-from-k",
            "−R × T × ln(K) / 1000",
            {"gas_constant_j_mol_k": 8.314, "temperature_k": 298, "equilibrium_constant": 10},
            "at 298 K the equilibrium constant is K = 10",
            lambda v: round(
                -v["gas_constant_j_mol_k"] * v["temperature_k"] * math.log(v["equilibrium_constant"]) / 1000,
                1,
            ),
            rounding="nearest 0.1 kJ/mol",
        ),
        _spec(
            "cell-biology-9:coupling-energy",
            "ΔG₁ + ΔG₂",
            {"first_reaction_kj_mol": 12.0, "second_reaction_kj_mol": -21.0},
            "+12.0 kJ/mol and a second reaction has ΔG =",
            lambda v: v["first_reaction_kj_mol"] + v["second_reaction_kj_mol"],
        ),
        _spec(
            "cell-biology-9:rate-at-km",
            "kcat × [active enzyme] × 1/2",
            {"active_sites_nm": 20, "kcat_per_s": 4, "substrate_over_km": 1},
            "20 nM active sites and has kcat = 4 s^-1",
            lambda v: v["active_sites_nm"] * v["kcat_per_s"] * v["substrate_over_km"]
            / (1 + v["substrate_over_km"]),
        ),
        _spec(
            "cell-biology-9:rate-at-twice-km",
            "kcat × [active enzyme] × ([S]/Km) / (1 + [S]/Km)",
            {"active_sites_nm": 20, "kcat_per_s": 4, "substrate_over_km": 2},
            "20 nM active sites and has kcat = 4 s^-1",
            lambda v: v["active_sites_nm"] * v["kcat_per_s"] * v["substrate_over_km"]
            / (1 + v["substrate_over_km"]),
        ),
        _spec(
            "cell-biology-10:rate-prediction",
            "Vmax × [S] / (Km + [S])",
            {"vmax_nm_s": 120, "km_um": 20, "substrate_um": 40},
            "Vmax = 120 nM/s and Km = 20 μM",
            lambda v: v["vmax_nm_s"] * v["substrate_um"] / (v["km_um"] + v["substrate_um"]),
        ),
        _spec(
            "cell-biology-11:resolution-estimate",
            "0.61 × wavelength / numerical aperture",
            {"wavelength_nm": 520, "numerical_aperture": 1.30},
            "520 nm emission and a 1.30 numerical-aperture objective",
            lambda v: round(0.61 * v["wavelength_nm"] / v["numerical_aperture"], 2),
            rounding="nearest 0.01 nm",
        ),
        _spec(
            "cell-biology-12:er-marker-recovery",
            "sum of the four recovered fractions",
            {"input_pct": 4, "fraction_1_pct": 18, "fraction_2_pct": 68, "fraction_3_pct": 5},
            "4% + 18% + 68% + 5%",
            lambda v: v["input_pct"] + v["fraction_1_pct"] + v["fraction_2_pct"] + v["fraction_3_pct"],
        ),
        _spec(
            "cell-biology-13:hybrid-fraction",
            "100% × 1/2 after two semiconservative replication rounds",
            {"initial_heavy_fraction": 1.0, "replication_rounds": 2},
            "exactly two DNA replication rounds",
            lambda v: 100 * v["initial_heavy_fraction"] / (2 ** (v["replication_rounds"] - 1)),
        ),
        _spec(
            "cell-biology-16:chip-percent-input",
            "100 × input fraction × 2^(Cq_input − Cq_IP)",
            {"input_percent": 1, "cq_input": 25, "cq_ip": 22},
            "1% of starting chromatin as input",
            lambda v: 100 * (v["input_percent"] / 100) * (2 ** (v["cq_input"] - v["cq_ip"])),
        ),
        _spec(
            "cell-biology-17:isoform-fraction",
            "100 × skipped counts / (skipped + included counts)",
            {"skipped_counts": 60, "included_counts": 30},
            "skipped isoform has 60 measured counts and the included isoform has 30",
            lambda v: round(100 * v["skipped_counts"] / (v["skipped_counts"] + v["included_counts"]), 1),
            rounding="nearest 0.1 percentage point",
        ),
        _spec(
            "cell-biology-18:protein-half-life",
            "ln(2) / (−ln(signal_end / signal_start) / elapsed time)",
            {"signal_start": 80, "signal_end": 40, "elapsed_hours": 4},
            "80 units at the start of a chase and 40 units after 4 hours",
            lambda v: math.log(2) / (-math.log(v["signal_end"] / v["signal_start"]) / v["elapsed_hours"]),
        ),
        _spec(
            "cell-biology-19:affected-child-risk",
            "100 × 1/2 carrier probability × penetrance",
            {"carrier_probability": 0.5, "penetrance": 0.80},
            "A defined phenotype has 80% penetrance among A/a carriers",
            lambda v: 100 * v["carrier_probability"] * v["penetrance"],
        ),
        _spec(
            "cell-biology-21:occupancy-model",
            "free ligand / (Kd + free ligand)",
            {"free_ligand_nm": 1, "kd_nm": 4},
            "free ligand is 1 nM and Kd is 4 nM",
            lambda v: v["free_ligand_nm"] / (v["kd_nm"] + v["free_ligand_nm"]),
        ),
        _spec(
            "cell-biology-21:relative-response",
            "stimulated signal / matched vehicle signal",
            {"stimulated_relative_units": 36, "vehicle_relative_units": 4},
            "pERK signal is 36 relative units in ligand-stimulated cells and 4 relative units in matched vehicle controls",
            lambda v: v["stimulated_relative_units"] / v["vehicle_relative_units"],
        ),
        _spec(
            "cell-biology-24:uniform-stress",
            "force / original area, with SI unit conversion",
            {"force_micronewtons": 12, "area_m2": 3e-9},
            "12 μN is applied across an original area of 3 × 10⁻⁹ m²",
            lambda v: (v["force_micronewtons"] * 1e-6) / v["area_m2"],
        ),
        _spec(
            "cell-biology-24:yap-relative-increase",
            "100 × (stiff condition − soft condition) / soft condition",
            {"soft_fraction": 0.28, "stiff_fraction": 0.76},
            "fraction is 0.28 at 2 kPa and 0.76 at 30 kPa",
            lambda v: 100 * (v["stiff_fraction"] - v["soft_fraction"]) / v["soft_fraction"],
        ),
        _spec(
            "cell-biology-25:phase-snapshot",
            "100 × labeled viable singlets / gated viable singlets",
            {"edu_positive_singlets": 60, "viable_singlets": 240},
            "labels 60 of 240 viable singlets",
            lambda v: 100 * v["edu_positive_singlets"] / v["viable_singlets"],
        ),
        _spec(
            "cell-biology-25:edu-relative-reduction",
            "100 × (vehicle fraction − treated fraction) / vehicle fraction",
            {"vehicle_fraction_pct": 27, "treated_fraction_pct": 11},
            "fraction is 27% in vehicle and 11% after 24 hours",
            lambda v: round(
                100 * (v["vehicle_fraction_pct"] - v["treated_fraction_pct"]) / v["vehicle_fraction_pct"],
                1,
            ),
            rounding="nearest 0.1 percentage point",
        ),
        _spec(
            "cell-biology-27:functional-fraction",
            "100 × constructs meeting threshold / recovered viable constructs",
            {"functional_constructs": 18, "recovered_viable_constructs": 80},
            "18 of 80 recovered viable constructs",
            lambda v: 100 * v["functional_constructs"] / v["recovered_viable_constructs"],
        ),
        _spec(
            "cell-biology-12:image-quantification-contrast",
            "cue-associated difference = cue mean − vehicle mean",
            {"vehicle_mean_pct": 13, "cue_mean_pct": 22},
            "means of 13% for vehicle and 22% for cue",
            lambda v: v["cue_mean_pct"] - v["vehicle_mean_pct"],
        ),
        _spec(
            "cell-biology-final:gel-modulus",
            "(force / cross-sectional area) / (extension / original length), with SI unit conversion",
            {"force_millinewtons": 1.2, "width_mm": 2, "thickness_mm": 1, "extension_mm": 0.20, "length_mm": 10},
            "stretches by 0.20 mm under an axial force of 1.2 mN",
            lambda v: ((v["force_millinewtons"] * 1e-3) / ((v["width_mm"] * 1e-3) * (v["thickness_mm"] * 1e-3)))
            / (v["extension_mm"] / v["length_mm"]),
        ),
        _spec(
            "cell-biology-project:rehearsal-perk-area",
            "trapezoidal area (y0 + y10)/2 × 10 + (y10 + y30)/2 × 20",
            {"y0_au": 0, "y10_au": 115, "y30_au": 66},
            "0, 115 and 66 arbitrary units at 0, 10 and 30 minutes",
            lambda v: (v["y0_au"] + v["y10_au"]) / 2 * 10 + (v["y10_au"] + v["y30_au"]) / 2 * 20,
        ),
    ]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_evidence(root: Path = ROOT) -> dict[str, Any]:
    course_root = root / "content/courses/cell-biology"
    question_bank_path = course_root / QUESTION_BANK_RELATIVE
    bank = json.loads(question_bank_path.read_text(encoding="utf-8"))
    questions = {question["id"]: question for question in bank["questions"]}
    numeric_ids = {question_id for question_id, question in questions.items() if question.get("type") == "numeric"}
    specs = _numeric_specs()
    spec_ids = {spec["question_id"] for spec in specs}
    if len(spec_ids) != len(specs) or numeric_ids != spec_ids or len(specs) != 23:
        raise ValueError("Public numeric question inventory differs from the recalculation allowlist")

    results = []
    for spec in sorted(specs, key=lambda item: item["question_id"]):
        question = questions[spec["question_id"]]
        if spec["prompt_anchor"] not in question["prompt"]:
            raise ValueError(f"Recalculation inputs no longer match the prompt: {spec['question_id']}")
        calculated = float(spec["compute"](spec["inputs"]))
        solution = question.get("solution_spec", {})
        authored = float(solution["answer"])
        absolute_tolerance = float(solution.get("tolerance", 0))
        relative_tolerance = float(solution.get("relative_tolerance", 0))
        allowed_error = absolute_tolerance + relative_tolerance * abs(authored)
        absolute_error = abs(calculated - authored)
        if not math.isfinite(calculated) or absolute_error > allowed_error:
            raise ValueError(
                f"Recalculation failed for {spec['question_id']}: computed {calculated}, "
                f"expected {authored}, allowed error {allowed_error}"
            )
        results.append({
            "question_id": spec["question_id"],
            "formula": spec["formula"],
            "inputs": spec["inputs"],
            "prompt_anchor": spec["prompt_anchor"],
            "calculated_value": calculated,
            "authored_answer": authored,
            "unit": solution.get("unit", "unspecified"),
            "rounding": spec["rounding"],
            "absolute_error": absolute_error,
            "absolute_tolerance": absolute_tolerance,
            "relative_tolerance": relative_tolerance,
            "maximum_allowed_error": allowed_error,
            "passed": True,
        })

    digest = course_package_digest.compute_digest(COURSE_ID, root)
    return {
        "schema_version": "1.0",
        "evidence_scope": "author-side-public-formative-numeric-key-recalculation",
        "course_id": COURSE_ID,
        "course_version": digest["content_version"],
        "public_package_sha256": digest["package_sha256"],
        "question_bank": {
            "path": (course_root / QUESTION_BANK_RELATIVE).relative_to(root).as_posix(),
            "sha256": _sha256(question_bank_path),
        },
        "scope_limits": {
            "inactive_candidate_answer_sources_read": False,
            "independent_review_established": False,
            "qualified_reviewer_identity_verified": False,
            "release_authorized": False,
        },
        "numeric_item_count": len(results),
        "passed_check_count": len(results),
        "results": results,
    }


def _canonical_json(value: dict[str, Any]) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", metavar="PATH", help="write the evidence JSON to PATH")
    mode.add_argument("--check", metavar="PATH", help="fail if PATH differs from current evidence")
    args = parser.parse_args()
    path = Path(args.write or args.check)
    if not path.is_absolute():
        path = ROOT / path
    try:
        evidence = build_evidence()
        rendered = _canonical_json(evidence)
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered, encoding="utf-8", newline="\n")
            action = "wrote"
        else:
            if not path.is_file() or path.read_text(encoding="utf-8") != rendered:
                raise ValueError(f"Evidence report is missing or stale: {path}")
            action = "checked"
    except (OSError, ValueError, KeyError, TypeError, ZeroDivisionError) as exc:
        parser.exit(1, f"Numeric-key evidence {args.check or args.write} failed: {exc}\n")
    print(json.dumps({
        "action": action,
        "course_version": evidence["course_version"],
        "numeric_item_count": evidence["numeric_item_count"],
        "passed_check_count": evidence["passed_check_count"],
        "inactive_candidate_answer_sources_read": False,
        "release_authorized": False,
        "path": path.as_posix(),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
