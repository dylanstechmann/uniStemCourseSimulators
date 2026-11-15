import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import { api, ApiError } from "../api";
import type { BenchProtocol, BenchRun } from "../types";
import { BenchPractice } from "./BenchPractice";

const sceneMocks = vi.hoisted(() => ({ asepticError: false }));

vi.mock("./PipetteBench3D", () => ({
  default: () => <section aria-label="Mock 3D bench" />,
}));

vi.mock("./AsepticBench3D", () => ({
  default: ({ panels }: { panels: BenchRun["panels"] }) => {
    if (sceneMocks.asepticError) throw new Error("Optional scene load failed");
    return (
      <section aria-label="Mock aseptic 3D bench">
        {panels.map((panel) => panel.title).join(" · ")}
      </section>
    );
  },
}));

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

const asepticProtocol: BenchProtocol = {
  ...protocol,
  id: "aseptic-medium-change-with-hidden-contamination",
  title: "Aseptic medium change with hidden contamination",
  actions: [
    { name: "inspect_supplies", label: "Inspect supplies", params: [] },
  ],
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

afterEach(() => {
  sceneMocks.asepticError = false;
  vi.restoreAllMocks();
});

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

  it("lazy-loads the aseptic scene only for its protocol and retains duplicate panel rows", async () => {
    const user = userEvent.setup();
    const consoleError = vi
      .spyOn(console, "error")
      .mockImplementation(() => {});
    vi.spyOn(api, "benchProtocols").mockResolvedValue([
      protocol,
      asepticProtocol,
    ]);
    vi.spyOn(api, "benchProtocol").mockImplementation(async (id) =>
      id === asepticProtocol.id ? asepticProtocol : protocol,
    );
    vi.spyOn(api, "benchReplay").mockResolvedValue(
      run({
        protocol_id: asepticProtocol.id,
        panels: [
          { title: "Cabinet", rows: [["Interior", "not disinfected"]] },
          {
            title: "Inside the cabinet",
            rows: [["target culture flask", "work center"]],
          },
          {
            title: "Sterility controls",
            rows: [
              ["7 d", "22 °C"],
              ["7 d", "32 °C"],
            ],
          },
        ],
        log: [
          {
            index: 0,
            name: "inspect_supplies",
            label: "Inspect supplies",
            params: {},
            clock_minutes: 1,
            events: [
              { kind: "readout", text: "Visible labels checked.", data: {} },
            ],
          },
        ],
      }),
    );
    render(<BenchPractice protocolId={asepticProtocol.id} />);
    await user.click(await screen.findByRole("button", { name: "Start run" }));
    expect(
      await screen.findByLabelText("Mock aseptic 3D bench"),
    ).toHaveTextContent("Cabinet · Inside the cabinet · Sterility controls");
    expect(screen.queryByLabelText("Mock 3D bench")).toBeNull();
    expect(screen.getByText("Inside the cabinet")).toBeInTheDocument();
    expect(screen.getByText("work center")).toBeInTheDocument();
    expect(screen.getByText("Visible labels checked.")).toBeInTheDocument();
    expect(screen.getAllByRole("rowheader", { name: "7 d" })).toHaveLength(2);
    expect(screen.getByText("22 °C")).toBeInTheDocument();
    expect(screen.getByText("32 °C")).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: "Next action" }),
    ).toBeInTheDocument();
    expect(consoleError.mock.calls.flat().join(" ")).not.toContain("same key");
  });

  it("keeps actions, tables, log and debrief usable when the optional scene fails", async () => {
    const user = userEvent.setup();
    vi.spyOn(console, "error").mockImplementation(() => {});
    sceneMocks.asepticError = true;
    vi.spyOn(api, "benchProtocols").mockResolvedValue([asepticProtocol]);
    vi.spyOn(api, "benchProtocol").mockResolvedValue(asepticProtocol);
    const panels: BenchRun["panels"] = [
      { title: "Cabinet", rows: [["Interior", "not disinfected"]] },
    ];
    const log: BenchRun["log"] = [
      {
        index: 0,
        name: "inspect_supplies",
        label: "Inspect supplies",
        params: {},
        clock_minutes: 1,
        events: [
          { kind: "readout", text: "Visible labels checked.", data: {} },
        ],
      },
    ];
    vi.spyOn(api, "benchReplay")
      .mockResolvedValueOnce(
        run({ protocol_id: asepticProtocol.id, panels, log }),
      )
      .mockResolvedValueOnce(
        run({
          protocol_id: asepticProtocol.id,
          panels,
          log,
          finished: true,
          debrief: {
            checkpoints: [],
            missed: { critical: 0, major: 0, minor: 0 },
            met_count: 0,
            applicable_count: 0,
            all_critical_met: true,
            revealed: ["Debrief remains available."],
            note: "Formative practice only.",
          },
        }),
      );
    render(<BenchPractice protocolId={asepticProtocol.id} />);
    await user.click(await screen.findByRole("button", { name: "Start run" }));
    expect(
      await screen.findByText(/Optional 3D view unavailable/),
    ).toBeInTheDocument();
    expect(screen.getByText("not disinfected")).toBeInTheDocument();
    expect(screen.getByText("Visible labels checked.")).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: "Next action" }),
    ).toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Do it" }));
    expect(
      await screen.findByRole("heading", { name: "Debrief" }),
    ).toBeInTheDocument();
    expect(screen.getByText("Debrief remains available.")).toBeInTheDocument();
  });
});
