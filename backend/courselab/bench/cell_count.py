"""Synthetic hemocytometer counting with boundary decisions and sampling error."""

from __future__ import annotations

import math
import random

from .engine import ActionRejected, Event, ProtocolModel, coach, round_significant


class HemocytometerCount(ProtocolModel):
    protocol_id = "hemocytometer-cell-count-viability"

    def checkpoint_ids(self):
        return ["mixed-before-sampling", "dilution-recorded", "coverslip-before-loading",
                "both-chambers", "countable-density", "boundary-rule", "report-concentration",
                "report-viability", "report-uncertainty"]

    def start(self, rng):
        # 25–75 cells per large square at the required twofold dilution, inside the 20–80 countable range.
        concentration = rng.uniform(0.5e6, 1.5e6)
        viability = rng.uniform(0.72, 0.97)
        return {
            "hidden": {"concentration": concentration, "viability": viability},
            "mixed": False, "sample_ul": None, "dye_ul": None, "dilution": None,
            "coverslip": False, "loaded": set(), "chambers": {}, "current": None,
            "counts": {}, "report": None,
        }

    def _cells(self, state, chamber):
        rng = random.Random(f"{self.protocol_id}:field:{chamber}")
        cells = []
        for index in range(96):
            boundary = None
            if index < 4:
                x, y, boundary = 0.0, 0.15 + index * 0.2, "include"
            elif index < 8:
                x, y, boundary = 0.15 + (index - 4) * 0.2, 0.0, "include"
            elif index < 10:
                x, y, boundary = 1.0, 0.3 + (index - 8) * 0.4, "exclude"
            elif index < 12:
                x, y, boundary = 0.3 + (index - 10) * 0.4, 1.0, "exclude"
            else:
                x, y = rng.uniform(0.06, 0.94), rng.uniform(0.06, 0.94)
            cells.append({"id": f"{chamber}-{index}", "x": round(x, 4), "y": round(y, 4),
                          "stained": rng.random() > state["hidden"]["viability"], "boundary": boundary})
        return cells

    def _make_chamber(self, state, chamber):
        expected = state["hidden"]["concentration"] / state["dilution"] * self.parameters["chamber_volume_ml"]
        if not state["mixed"]:
            expected *= 0.6 if chamber == "A" else 1.4
        count = max(4, min(96, round(expected)))
        cells = self._cells(state, chamber)[:count]
        for cell in cells:
            cell["decision"] = None
        state["chambers"][chamber] = cells
        state["current"] = chamber

    def visible(self, state):
        rows = [["Sample", "synthetic non-human suspension culture"],
                ["Suspension mixed", "yes" if state["mixed"] else "no"],
                ["Dilution", "not prepared" if state["dilution"] is None else
                 f"{state['sample_ul']:g} µL sample + {state['dye_ul']:g} µL trypan blue (1:{state['dilution']:g})"],
                ["Coverslip", "seated" if state["coverslip"] else "not seated"],
                ["Chambers loaded", ", ".join(sorted(state["loaded"])) or "none"]]
        panels = [{"title": "Preparation", "rows": rows}]
        if state["current"] is not None:
            chamber = state["current"]
            counts = state["counts"].get(chamber, {"viable": 0, "stained": 0})
            cells = state["chambers"][chamber]
            field = "; ".join(
                f"{cell['id']} at x={cell['x']:g}, y={cell['y']:g}; "
                f"{'stained' if cell['stained'] else 'unstained'}; "
                f"decision: {cell['decision'] or 'pending'}" for cell in cells)
            panels.append({"title": f"Microscope field: chamber {chamber}", "rows": [
                ["Rule", "Count cells touching the top and left boundaries; exclude bottom and right."],
                ["Your tally", f"{counts['viable']} unstained + {counts['stained']} stained"],
                ["Visible cells", field],
            ]})
        if state["counts"]:
            panels.append({"title": "Recorded chamber tallies", "rows": [
                [f"Chamber {chamber}", f"{tally['viable']} unstained; {tally['stained']} stained"]
                for chamber, tally in sorted(state["counts"].items())]})
        return panels

    def act_mix_sample(self, state, rng, seconds):
        state["mixed"] = seconds >= 5
        state["clock"] += seconds / 60
        events = [Event("info", f"The suspension is mixed for {seconds:g} s.")]
        if not state["mixed"]:
            coach(state, events, "Mix long enough to resuspend settled cells before taking a sample.")
        return events

    def act_prepare_dilution(self, state, rng, sample_ul, dye_ul):
        if state["loaded"]:
            raise ActionRejected("Start a new run to change a loaded dilution")
        state["sample_ul"], state["dye_ul"] = sample_ul, dye_ul
        state["dilution"] = (sample_ul + dye_ul) / sample_ul
        state["clock"] += 1
        events = [Event("info", f"Prepared {sample_ul:g} µL cell suspension with {dye_ul:g} µL trypan blue; dilution factor {state['dilution']:g}.")]
        if not state["mixed"]:
            coach(state, events, "The sample was not adequately mixed before sampling.")
        return events

    def act_place_coverslip(self, state, rng):
        state["coverslip"] = True
        state["clock"] += 0.2
        return [Event("info", "The coverslip is seated over both counting chambers.")]

    def act_load_chamber(self, state, rng, chamber):
        if state["dilution"] is None:
            raise ActionRejected("Prepare the cell and dye mixture first")
        if not state["coverslip"]:
            raise ActionRejected("Seat the coverslip before loading the chamber")
        if chamber in state["loaded"]:
            raise ActionRejected("This chamber is already loaded; inspect it or load the other chamber")
        state["loaded"].add(chamber)
        self._make_chamber(state, chamber)
        state["clock"] += 0.5
        return [Event("readout", f"Chamber {chamber} is filled by capillary action. The synthetic microscope field is now visible.")]

    def act_select_chamber(self, state, rng, chamber):
        if chamber not in state["loaded"]:
            raise ActionRejected("Load this chamber before inspecting it")
        state["current"] = chamber
        return [Event("info", f"Chamber {chamber} is centred in the microscope view.")]

    def act_mark_cell(self, state, rng, cell_id, classification):
        chamber = state["current"]
        if chamber is None:
            raise ActionRejected("Load and inspect a chamber first")
        cell = next((item for item in state["chambers"][chamber] if item["id"] == cell_id), None)
        if cell is None:
            raise ActionRejected("That cell is not in the current field")
        cell["decision"] = classification
        state["clock"] += 0.02
        return []

    def act_record_tally(self, state, rng, chamber, unstained, stained):
        if chamber not in state["loaded"]:
            raise ActionRejected("Load this chamber before recording its tally")
        cells = state["chambers"][chamber]
        if any(cell["decision"] is None for cell in cells):
            raise ActionRejected("Classify every visible cell before recording the tally")
        state["counts"][chamber] = {"viable": unstained, "stained": stained}
        state["clock"] += 0.5
        return [Event("readout", f"Chamber {chamber}: {unstained} unstained and {stained} stained cells recorded.")]

    def act_submit_report(self, state, rng, concentration_cells_ml, viability_pct, relative_counting_uncertainty_pct):
        if len(state["counts"]) < 2:
            raise ActionRejected("Record tallies from both chambers before submitting")
        state["report"] = {"concentration": concentration_cells_ml, "viability": viability_pct,
                           "uncertainty": relative_counting_uncertainty_pct}
        state["finished"] = True
        return [Event("info", "The cell-count record is submitted for debrief.")]

    def expected(self, state):
        if len(state["counts"]) < 2:
            return None
        viable = sum(tally["viable"] for tally in state["counts"].values())
        stained = sum(tally["stained"] for tally in state["counts"].values())
        total = viable + stained
        return {"concentration": viable / 2 / self.parameters["chamber_volume_ml"] * state["dilution"],
                "viability": viable / total * 100 if total else 0,
                "uncertainty": 100 / math.sqrt(total) if total else 100,
                "viable": viable, "stained": stained, "total": total}

    def evaluate(self, state):
        p = self.parameters
        expected = self.expected(state)
        report = state["report"]
        dilution_ok = state["dilution"] is not None and abs(state["dilution"] - p["target_dilution"]) < 1e-9
        density_ok = bool(state["chambers"]) and all(p["count_range"][0] <= len(cells) <= p["count_range"][1]
                                                      for cells in state["chambers"].values())
        boundary_ok = bool(state["chambers"]) and all(
            cell["decision"] == ("exclude" if cell["boundary"] == "exclude" else
                                 "stained" if cell["stained"] else "unstained")
            for cells in state["chambers"].values() for cell in cells)
        results = {
            "mixed-before-sampling": (state["mixed"], "Mix the suspension before withdrawing the sample."),
            "dilution-recorded": (dilution_ok, f"The exercise uses a 1:{p['target_dilution']:g} sample-plus-dye dilution; "
                                  f"you prepared {state['dilution']}."),
            "coverslip-before-loading": (state["coverslip"], "Seat the coverslip before capillary loading."),
            "both-chambers": (len(state["counts"]) == 2, "Count both chambers independently."),
            "countable-density": (density_ok, f"Each chamber should contain {p['count_range'][0]}–{p['count_range'][1]} synthetic cells."),
            "boundary-rule": (boundary_ok, "Every cell needs a stain classification; the top/left inclusion rule is part of the field record."),
        }
        for key, field, tolerance in (("report-concentration", "concentration", p["concentration_tolerance_pct"] / 100),
                                      ("report-viability", "viability", p["viability_tolerance_pct"] / 100),
                                      ("report-uncertainty", "uncertainty", p["uncertainty_tolerance_pct"] / 100)):
            if expected is None or report is None:
                results[key] = (False, "Both chamber tallies and a report are required.")
            else:
                results[key] = (abs(report[field] - expected[field]) <= expected[field] * tolerance,
                                f"From your tallies: {field} = {round_significant(expected[field], 4):g}; "
                                f"you reported {report[field]:g}.")
        return results

    def reveal(self, state):
        return [f"The synthetic culture's generating concentration was {state['hidden']['concentration']:.3g} cells/mL "
                f"with {state['hidden']['viability'] * 100:.1f}% generating viability. A finite chamber count is an estimate, not an exact recovery of those values.",
                "The counting uncertainty is the Poisson approximation 100/√N percent. It excludes dilution, mixing, loading and classification bias."]
