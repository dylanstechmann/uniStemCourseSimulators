import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import { api, ApiError } from "../api";
import type { BenchProtocol, BenchRun } from "../types";
import { BenchPractice } from "./BenchPractice";

const protocol: BenchProtocol = {
  id: "micropipette-gravimetric-verification",
  version: "0.1.0",
  title: "Gravimetric verification of a 1000 µL micropipette",
  layer: 0,
  summary: "Check a pipette by weighing water.",
  scenario: "A pipette is due for its routine check.",
  actions: [
    { name: "fit_tip", label: "Fit a new tip", params: [] },
    {
      name: "set_volume",
      label: "Set pipette volume",
      params: [
        {
          name: "volume_ul",
          label: "Volume",
          type: "number",
          min: 100,
          max: 1000,
          unit: "µL",
        },
      ],
    },
  ],
  limitations: ["Limits are practice values."],
  sources: [{ source_id: "tanaka-2001-water-density", use: "Water density." }],
};

function run(overrides: Partial<BenchRun> = {}): BenchRun {
  return {
    protocol_id: protocol.id,
    protocol_version: "0.1.0",
    seed: 1,
    mode: "guided",
    finished: false,
    clock_minutes: 0,
    panels: [{ title: "Pipette", rows: [["Tip", "none"]] }],
    log: [],
    guidance: ["Measure the water temperature."],
    debrief: null,
    ...overrides,
  };
}

afterEach(() => vi.restoreAllMocks());

describe("bench practice", () => {
  it("starts a run, sends each action with the full history and shows the debrief", async () => {
    const user = userEvent.setup();
    vi.spyOn(api, "benchProtocols").mockResolvedValue([protocol]);
    vi.spyOn(api, "benchProtocol").mockResolvedValue(protocol);
    const replay = vi
      .spyOn(api, "benchReplay")
      .mockResolvedValueOnce(run())
      .mockResolvedValueOnce(
        run({
          log: [
            {
              index: 0,
              name: "set_volume",
              label: "Set pipette volume",
              params: { volume_ul: 1000 },
              clock_minutes: 0.2,
              events: [{ kind: "warning", text: "Pre-wet the tip.", data: {} }],
            },
          ],
        }),
      )
      .mockResolvedValueOnce(
        run({
          finished: true,
          debrief: {
            checkpoints: [
              {
                id: "replicate-count",
                severity: "critical",
                description: "Record at least 10 readings.",
                rationale: "Few replicates estimate spread poorly.",
                source: { kind: "simulation-typical" },
                met: false,
                detail: "2 readings recorded.",
              },
            ],
            missed: { critical: 1, major: 0, minor: 0 },
            met_count: 0,
            applicable_count: 1,
            all_critical_met: false,
            revealed: ["This pipette had no fault."],
            note: "Formative practice only.",
          },
        }),
      );
    render(<BenchPractice />);
    await user.click(await screen.findByRole("button", { name: "Start run" }));
    expect(
      await screen.findByText("Measure the water temperature."),
    ).toBeInTheDocument();
    await user.selectOptions(
      screen.getByRole("combobox", { name: "Action" }),
      "set_volume",
    );
    await user.type(
      screen.getByRole("spinbutton", { name: "Volume (µL)" }),
      "1000",
    );
    await user.click(screen.getByRole("button", { name: "Do it" }));
    expect(await screen.findByText(/Pre-wet the tip/)).toBeInTheDocument();
    const [, , , actions] = replay.mock.calls[1];
    expect(actions).toEqual([
      { name: "set_volume", params: { volume_ul: 1000 } },
    ]);
    await user.click(screen.getByRole("button", { name: "Do it" }));
    expect(
      await screen.findByRole("heading", { name: "Debrief" }),
    ).toBeInTheDocument();
    expect(screen.getByText("This pipette had no fault.")).toBeInTheDocument();
    expect(screen.getByText("Missed")).toBeInTheDocument();
    expect(replay.mock.calls[2][3]).toHaveLength(2);
  });

  it("refuses an empty number locally and keeps history when the server rejects an action", async () => {
    const user = userEvent.setup();
    vi.spyOn(api, "benchProtocols").mockResolvedValue([protocol]);
    vi.spyOn(api, "benchProtocol").mockResolvedValue(protocol);
    const replay = vi
      .spyOn(api, "benchReplay")
      .mockResolvedValueOnce(run())
      .mockRejectedValueOnce(
        new ApiError("Action 1 (fit_tip): A tip is already fitted", 422),
      );
    render(<BenchPractice protocolId={protocol.id} />);
    await user.click(await screen.findByRole("button", { name: "Start run" }));
    await screen.findByText("Measure the water temperature.");
    await user.selectOptions(
      screen.getByRole("combobox", { name: "Action" }),
      "set_volume",
    );
    await user.click(screen.getByRole("button", { name: "Do it" }));
    expect(screen.getByRole("alert")).toHaveTextContent(
      "Enter a number for volume",
    );
    expect(replay).toHaveBeenCalledTimes(1);
    await user.selectOptions(
      screen.getByRole("combobox", { name: "Action" }),
      "fit_tip",
    );
    await user.click(screen.getByRole("button", { name: "Do it" }));
    await waitFor(() =>
      expect(screen.getByRole("alert")).toHaveTextContent(
        "A tip is already fitted",
      ),
    );
    expect(screen.queryByRole("heading", { name: "Debrief" })).toBeNull();
  });
});
