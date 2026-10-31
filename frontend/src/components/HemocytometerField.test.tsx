import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import type { BenchRun } from "../types";
import HemocytometerField, {
  chamberCells,
  tallyCells,
} from "./HemocytometerField";

const field =
  "A-0 at x=0, y=0.15; unstained; decision: pending; A-8 at x=1, y=0.3; stained; decision: exclude; A-12 at x=0.5, y=0.5; stained; decision: pending";

function run(): BenchRun {
  return {
    protocol_id: "hemocytometer-cell-count-viability",
    protocol_version: "0.1.0",
    seed: 7,
    mode: "guided",
    finished: false,
    clock_minutes: 2,
    panels: [
      {
        title: "Microscope field: chamber A",
        rows: [["Visible cells", field]],
      },
    ],
    log: [],
    guidance: null,
    debrief: null,
  };
}

describe("hemocytometer field", () => {
  it("reads only visible cell positions, stains and decisions", () => {
    const cells = chamberCells(run());
    expect(cells).toHaveLength(3);
    expect(cells[0]).toMatchObject({ id: "A-0", x: 0, stained: false });
    expect(tallyCells(cells)).toEqual({
      unstained: 0,
      stained: 0,
      excluded: 1,
    });
  });

  it("sends cell decisions through the replay action callback", async () => {
    const user = userEvent.setup();
    const onAct = vi.fn();
    render(<HemocytometerField run={run()} busy={false} onAct={onAct} />);
    const cell = screen.getByRole("button", { name: /Cell A-0,/ });
    await user.click(cell);
    await user.click(screen.getByRole("button", { name: "Include unstained" }));
    expect(onAct).toHaveBeenCalledWith({
      name: "mark_cell",
      params: { cell_id: "A-0", classification: "unstained" },
    });
    cell.focus();
    await user.keyboard("{Enter}");
    await user.click(screen.getByRole("button", { name: "Exclude boundary" }));
    expect(onAct).toHaveBeenLastCalledWith({
      name: "mark_cell",
      params: { cell_id: "A-0", classification: "exclude" },
    });
  });
});
