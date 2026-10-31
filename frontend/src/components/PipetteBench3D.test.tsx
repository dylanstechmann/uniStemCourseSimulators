import { describe, expect, it } from "vitest";
import type { BenchRun } from "../types";
import { pipetteSceneState } from "./PipetteBench3D";

function run(panels: BenchRun["panels"]): BenchRun {
  return {
    protocol_id: "micropipette-gravimetric-verification",
    protocol_version: "0.1.0",
    seed: 1,
    mode: "guided",
    finished: false,
    clock_minutes: 0,
    panels,
    log: [],
    guidance: null,
    debrief: null,
  };
}

describe("pipette 3D scene state", () => {
  it("uses only visible server panels and preserves their readings", () => {
    const state = pipetteSceneState(
      run([
        {
          title: "Pipette",
          rows: [
            ["Volume setting", "1000 µL"],
            ["Tip", "fitted, pre-wetted"],
            ["In tip", "water (about 1000 µL)"],
          ],
        },
        {
          title: "Bench",
          rows: [
            ["Balance", "998.7 mg displayed (readability 0.1 mg)"],
            ["Water temperature", "21.4 °C"],
            ["Readings recorded", "3"],
          ],
        },
      ]),
    );
    expect(state).toMatchObject({
      volume: "1000 µL",
      hasTip: true,
      prewetted: true,
      hasLiquid: true,
      balance: "998.7 mg",
      temperature: "21.4 °C",
      readings: "3",
    });
    expect(state.description).toContain("998.7 mg displayed");
  });

  it("distinguishes an empty, tipless pipette from a dry fitted tip", () => {
    const empty = pipetteSceneState(
      run([
        {
          title: "Pipette",
          rows: [
            ["Volume setting", "500 µL"],
            ["Tip", "none"],
            ["In tip", "nothing"],
          ],
        },
        { title: "Bench", rows: [["Balance", "0.0 mg displayed"]] },
      ]),
    );
    expect(empty.hasTip).toBe(false);
    expect(empty.prewetted).toBe(false);
    expect(empty.hasLiquid).toBe(false);
    expect(empty.balance).toBe("0.0 mg");
    expect(empty.temperature).toBe("");
  });
});
