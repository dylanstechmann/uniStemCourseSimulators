import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, describe, expect, it, vi } from "vitest";
import type { BenchRun } from "../types";
import AsepticBench3D, {
  asepticSceneState,
  layoutCabinetItems,
  nextCameraPosition,
} from "./AsepticBench3D";

const graphics = vi.hoisted(() => ({
  fail: false,
  frameloop: "",
  contactShadowFrames: [] as number[],
  orbitEnablePan: [] as boolean[],
  invalidate: vi.fn(),
  cameraPositionSet: vi.fn(),
  lookAt: vi.fn(),
}));

vi.mock("@react-three/fiber", () => ({
  Canvas: ({
    role,
    "aria-label": ariaLabel,
    "aria-describedby": ariaDescribedBy,
    frameloop,
    children,
  }: {
    role: string;
    "aria-label": string;
    "aria-describedby": string;
    frameloop: string;
    children: React.ReactNode;
  }) => {
    if (graphics.fail) throw new Error("WebGL unavailable");
    graphics.frameloop = frameloop;
    return (
      <div
        role={role}
        aria-label={ariaLabel}
        aria-describedby={ariaDescribedBy}
      >
        {children}
      </div>
    );
  },
  useThree: (selector: (state: unknown) => unknown) => {
    const state = {
      camera: {
        position: {
          x: 8,
          y: 6.2,
          z: 11,
          set: graphics.cameraPositionSet,
        },
        lookAt: graphics.lookAt,
      },
      invalidate: graphics.invalidate,
    };
    return selector(state);
  },
}));

vi.mock("@react-three/drei", () => ({
  ContactShadows: ({ frames }: { frames: number }) => {
    graphics.contactShadowFrames.push(frames);
    return null;
  },
  Html: ({ children }: { children: React.ReactNode }) => <div>{children}</div>,
  OrbitControls: ({ enablePan }: { enablePan: boolean }) => {
    graphics.orbitEnablePan.push(enablePan);
    return null;
  },
}));

afterEach(() => {
  graphics.fail = false;
  graphics.frameloop = "";
  graphics.contactShadowFrames.length = 0;
  graphics.orbitEnablePan.length = 0;
  graphics.invalidate.mockClear();
  graphics.cameraPositionSet.mockClear();
  graphics.lookAt.mockClear();
});

const visiblePanels: BenchRun["panels"] = [
  {
    title: "Cabinet",
    rows: [
      ["Critical zone", "ISO 5 (Class 100)"],
      ["Interior", "sterile 70% isopropyl alcohol"],
      ["UV lamp", "15 min"],
      ["Open flame", "lit"],
    ],
  },
  {
    title: "Inside the cabinet",
    rows: [
      ["target culture flask", "work center"],
      ["fresh-medium lot A", "clean side, not wiped"],
      ["spent-medium waste container", "dirty side"],
      ["sterile single-use pipettes", "clean side"],
      ["unrecognized trolley", "rear grille"],
    ],
  },
  {
    title: "Open containers",
    rows: [
      ["target culture flask", "held above the opening"],
      ["fresh-medium lot A", "face down on a surface"],
    ],
  },
  {
    title: "Culture",
    rows: [
      ["Target flask", "clear at this point"],
      ["Spent medium removed", "12 mL"],
      ["Fresh medium added", "12 mL from fresh-medium lot A"],
    ],
  },
  { title: "Future panel", rows: [["New reading", "visible value"]] },
];

describe("aseptic 3D scene state", () => {
  it("maps visible cabinet, placement, closure and medium readings", () => {
    const state = asepticSceneState(visiblePanels);
    expect(state.cabinet).toEqual({
      criticalZone: "ISO 5 (Class 100)",
      interior: "sterile 70% isopropyl alcohol",
      uvLamp: "15 min",
      openFlame: "lit",
    });
    expect(state.culture).toEqual({
      spentMedium: "12 mL",
      freshMedium: "12 mL from fresh-medium lot A",
    });
    expect(state.items).toHaveLength(5);
    expect(state.items[0]).toMatchObject({
      name: "target culture flask",
      kind: "flask",
      zone: "work center",
      open: true,
      closure: "held above the opening",
      appearance: "clear at this point",
    });
    expect(state.items[1]).toMatchObject({
      kind: "bottle",
      notWiped: true,
      open: true,
      closure: "face down on a surface",
    });
    expect(state.items[3]).toMatchObject({ kind: "supplies", open: false });
    expect(state.items[4]).toMatchObject({
      kind: "unknown",
      zone: "rear grille",
    });
    expect(state.description).toContain("front grille");
    expect(state.description).toContain("New reading — visible value");
  });

  it("handles empty and unrecognized panels without inventing state", () => {
    const empty = asepticSceneState([
      { title: "Inside the cabinet", rows: [["—", "empty"]] },
      { title: "Unknown", rows: [["Unsupported", "still visible"]] },
    ]);
    expect(empty.items).toEqual([]);
    expect(empty.cabinet.interior).toBe("");
    expect(empty.culture.freshMedium).toBe("");
    expect(empty.description).toContain("Unsupported — still visible");
    expect(asepticSceneState([]).description).toContain(
      "No visible panel rows were supplied",
    );
  });

  it("does not infer undisclosed lot, cabinet or contamination conditions", () => {
    const state = asepticSceneState([
      {
        title: "Cabinet",
        rows: [["Interior", "not disinfected"]],
      },
      {
        title: "Inside the cabinet",
        rows: [
          ["target culture flask", "work center"],
          ["fresh-medium lot A", "clean side"],
        ],
      },
      {
        title: "Culture",
        rows: [
          ["Target flask", "clear at this point"],
          ["Fresh medium added", "12 mL from fresh-medium lot A"],
        ],
      },
    ]);
    expect(state.items[0].appearance).toBe("clear at this point");
    expect(state.description).not.toMatch(
      /expired|mollicute|mycoplasma|contaminat/i,
    );
    expect(state.description).not.toContain("dirty interior");
  });
});

describe("aseptic scene layout and camera commands", () => {
  function itemsFor(rows: [string, string][]) {
    return asepticSceneState([{ title: "Inside the cabinet", rows }]).items;
  }

  function expectSeparated(layout: ReturnType<typeof layoutCabinetItems>) {
    expect(new Set(layout.map(({ position }) => position.join(":"))).size).toBe(
      layout.length,
    );
    for (let first = 0; first < layout.length; first += 1) {
      for (let second = first + 1; second < layout.length; second += 1) {
        const a = layout[first].position;
        const b = layout[second].position;
        expect(Math.hypot(a[0] - b[0], a[2] - b[2])).toBeGreaterThanOrEqual(
          1.149999,
        );
      }
    }
  }

  it("separates a realistic maximal set of all ten protocol items across zones", () => {
    const rows: [string, string][] = [
      ["target culture flask", "work center"],
      ["turbid culture flask", "dirty side"],
      ["second cell-line flask", "work center"],
      ["fresh-medium lot A", "clean side"],
      ["fresh-medium lot B", "clean side"],
      ["spent-medium waste container", "dirty side"],
      ["sterile single-use pipettes", "clean side"],
      ["pipette aid", "clean side"],
      ["sterility-test broth tubes", "clean side"],
      ["penicillin-streptomycin stock", "clean side"],
    ];
    const layout = layoutCabinetItems(itemsFor(rows));
    expect(layout).toHaveLength(10);
    expect(layout.map(({ item }) => item.zone)).toEqual(
      rows.map(([, zone]) => zone),
    );
    expectSeparated(layout);
  });

  it("coordinates work-center, opening, grille, clean and dirty placements", () => {
    const layout = layoutCabinetItems(
      itemsFor([
        ["target culture flask", "work center"],
        ["turbid culture flask", "front opening"],
        ["fresh-medium lot A", "front grille"],
        ["spent-medium waste container", "rear grille"],
        ["second cell-line flask", "dirty side"],
        ["sterile single-use pipettes", "clean side"],
      ]),
    );
    expectSeparated(layout);
  });

  it("keeps pathological zone overflow within bounded candidate slots", () => {
    const zones = [
      "clean side",
      "work center",
      "dirty side",
      "front opening",
      "front grille",
      "rear grille",
      "stacked",
    ];
    const items = zones.flatMap((zone) =>
      itemsFor(
        Array.from({ length: 10 }, (_, index) => [
          `${zone} item ${index + 1}`,
          zone,
        ]),
      ),
    );
    for (const { position } of layoutCabinetItems(items)) {
      expect(position[0]).toBeGreaterThanOrEqual(-3.750000001);
      expect(position[0]).toBeLessThanOrEqual(3.750000001);
      expect(position[1]).toBeLessThanOrEqual(0.3);
      expect(position[2]).toBeGreaterThanOrEqual(-1.200000001);
      expect(position[2]).toBeLessThanOrEqual(1.500000001);
    }
  });

  it("rotates, zooms and resets the camera with bounded distances", () => {
    const initial: [number, number, number] = [8, 6.2, 11];
    const distance = (position: [number, number, number]) =>
      Math.hypot(position[0], position[1] - 1.25, position[2]);
    const rotated = nextCameraPosition("rotate-left", initial);
    expect(rotated).not.toEqual(initial);
    expect(distance(rotated)).toBeCloseTo(distance(initial));
    const restored = nextCameraPosition("rotate-right", rotated);
    restored.forEach((coordinate, index) =>
      expect(coordinate).toBeCloseTo(initial[index]),
    );
    expect(distance(nextCameraPosition("zoom-in", initial))).toBeLessThan(
      distance(initial),
    );
    expect(
      distance(nextCameraPosition("zoom-out", [0.01, 1.26, 0.01])),
    ).toBeCloseTo(6);
    expect(distance(nextCameraPosition("zoom-out", [16, 12, 22]))).toBeCloseTo(
      20,
    );
    expect(nextCameraPosition("reset", rotated)).toEqual(initial);
  });
});

describe("aseptic 3D scene accessibility and fallback", () => {
  it("offers keyboard-accessible view controls and a visible text alternative", async () => {
    const user = userEvent.setup();
    vi.spyOn(console, "error").mockImplementation(() => {});
    const { rerender } = render(<AsepticBench3D panels={visiblePanels} />);
    expect(
      screen.getByRole("heading", { name: "Interactive 3D cabinet" }),
    ).toBeInTheDocument();
    expect(screen.getByText("Visual model · not to scale")).toBeInTheDocument();
    const canvasRegion = screen.getByRole("region", {
      name: "Procedural Class II cabinet illustration",
    });
    expect(canvasRegion).toHaveAttribute(
      "aria-describedby",
      "aseptic-3d-description",
    );
    expect(graphics.frameloop).toBe("demand");
    expect(graphics.orbitEnablePan).toEqual([false]);
    expect(graphics.contactShadowFrames).toEqual([1]);
    const refreshedPanels = structuredClone(visiblePanels);
    refreshedPanels[0].rows[2][1] = "20 min";
    rerender(<AsepticBench3D panels={refreshedPanels} />);
    expect(graphics.contactShadowFrames).toEqual([1, 1]);
    const invalidations = graphics.invalidate.mock.calls.length;
    await user.click(screen.getByRole("button", { name: "Rotate left" }));
    expect(graphics.invalidate.mock.calls.length).toBeGreaterThan(
      invalidations,
    );
    expect(graphics.cameraPositionSet).toHaveBeenCalled();
    await user.click(screen.getByRole("button", { name: "Rotate right" }));
    await user.click(screen.getByRole("button", { name: "Zoom in" }));
    await user.click(screen.getByRole("button", { name: "Zoom out" }));
    await user.click(screen.getByRole("button", { name: "Reset 3D view" }));
    await user.click(screen.getByText("Text description and visible readings"));
    expect(screen.getByText(/Procedural cabinet illustration/)).toBeVisible();
    expect(screen.getByText(/New reading — visible value/)).toBeVisible();
    expect(screen.getByText(/cannot|does not/)).toBeInTheDocument();
  });

  it("retains the text alternative when graphics fail", () => {
    vi.spyOn(console, "error").mockImplementation(() => {});
    graphics.fail = true;
    render(<AsepticBench3D panels={visiblePanels} />);
    expect(screen.getByRole("status")).toHaveTextContent(
      "3D graphics are unavailable",
    );
    expect(
      screen.queryByRole("group", { name: "3D view controls" }),
    ).toBeNull();
    expect(
      screen.getByText("Text description and visible readings"),
    ).toBeInTheDocument();
    expect(screen.getByText(/New reading — visible value/)).toBeInTheDocument();
  });
});
