import { describe, expect, it } from "vitest";
import { calculateStudyTool, studyTools } from "./studyTools";
import type { StudyToolId } from "./studyTools";

function calculate(id: StudyToolId, overrides: Record<string, string> = {}) {
  const tool = studyTools.find((item) => item.id === id)!;
  const input = Object.fromEntries(
    tool.fields.map((field) => [field.id, field.initial]),
  );
  return calculateStudyTool(tool, { ...input, ...overrides });
}

describe("scientific study calculations", () => {
  it("balances stock and diluent volume, including no dilution and a zero target", () => {
    expect(calculate("dilution").map((item) => item.value)).toEqual([
      0.5, 24.5,
    ]);
    expect(
      calculate("dilution", { target: "100" }).map((item) => item.value),
    ).toEqual([25, 0]);
    expect(
      calculate("dilution", { target: "0" }).map((item) => item.value),
    ).toEqual([0, 25]);
    expect(() => calculate("dilution", { target: "101" })).toThrow(
      /cannot exceed/,
    );
  });

  it("uses the buffer ratio without overflowing an intermediate division", () => {
    expect(calculate("buffer")[0].value).toBeCloseTo(8.2);
    expect(calculate("buffer", { base: "1", acid: "10" })[0].value).toBeCloseTo(
      6.2,
    );
    expect(
      calculate("buffer", { pka: "0", base: "1e300", acid: "1e-300" })[0].value,
    ).toBe(600);
  });

  it("gives half Vmax at Km and accepts zero substrate", () => {
    expect(
      calculate("enzyme", { substrate: "5" }).map((item) => item.value),
    ).toEqual([50, 50]);
    expect(
      calculate("enzyme", { substrate: "0" }).map((item) => item.value),
    ).toEqual([0, 0]);
    expect(
      calculate("enzyme", { substrate: "1e300", km: "1e300" })[0].value,
    ).toBe(50);
  });

  it("converts kΩ and μF to seconds and evaluates the first-order response", () => {
    const result = calculate("rc", {
      resistance: "2",
      capacitance: "5",
      time: "0.01",
    });
    expect(result[0]).toEqual({
      label: "Time constant",
      value: 0.01,
      unit: "s",
    });
    expect(result[1].value).toBeCloseTo(63.21205588);
    expect(calculate("rc", { time: "0" })[1].value).toBe(0);
  });

  it("converts micrometres and preserves the square-distance diffusion scaling", () => {
    const baseline = calculate("diffusion")[0];
    expect(baseline.unit).toBe("s");
    expect(baseline.value).toBeCloseTo(10);
    expect(calculate("diffusion", { length: "200" })[0].value).toBeCloseTo(40);
    expect(
      calculate("diffusion", { length: "200", diffusivity: "2e-9" })[0].value,
    ).toBeCloseTo(20);
  });

  it("uses mA and mW and preserves current direction while power remains positive", () => {
    const result = calculate("ohm", { voltage: "-5", resistance: "2" });
    expect(result[0]).toEqual({ label: "Current", value: -2.5, unit: "mA" });
    expect(result[1].value).toBe(12.5);
    expect(result[1].unit).toBe("mW");
  });

  it.each([
    ["dilution", { stock: "0" }],
    ["buffer", { acid: "0" }],
    ["enzyme", { substrate: "-1" }],
    ["rc", { capacitance: "0" }],
    ["diffusion", { diffusivity: "-1" }],
    ["ohm", { resistance: "0" }],
    ["buffer", { pka: "" }],
    ["enzyme", { vmax: "Infinity" }],
    ["ohm", { voltage: "1e300", resistance: "1e-300" }],
  ] as [StudyToolId, Record<string, string>][])(
    "rejects invalid or nonfinite %s calculations",
    (id, input) => {
      expect(() => calculate(id, input)).toThrow();
    },
  );
});
