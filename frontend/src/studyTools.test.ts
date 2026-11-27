import { describe, expect, it } from "vitest";
import { calculateStudyTool, studyTools } from "./studyTools";
import type { StudyToolId } from "./studyTools";

function calculate(id: StudyToolId, overrides: Record<string, string> = {}) {
  const tool = studyTools.find((item) => item.id === id)!;
  const input = Object.fromEntries(
    [...tool.fields, ...(tool.controls ?? [])].map((field) => [
      field.id,
      field.initial,
    ]),
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

  it("compares normalized voltage and energy during source-free RC discharge", () => {
    const results = (time: string) =>
      calculate("rc", { time }).map((item) => item.value);
    expect(results("0")).toEqual([1, 0, 100, 100]);
    const [, charged, voltage, energy] = results("1");
    expect(charged + voltage).toBeCloseTo(100);
    expect(voltage).toBeCloseTo(36.787944);
    expect(energy).toBeCloseTo(13.533528);
    const [, , halfVoltage, quarterEnergy] = results("0.693147");
    expect(halfVoltage).toBeCloseTo(50);
    expect(quarterEnergy).toBeCloseTo(25);
    expect(results("50")[2]).toBeGreaterThan(0);
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

  it("registers the habitat ledger defaults and related courses", () => {
    const tool = studyTools.find((item) => item.id === "habitat-ledger")!;
    expect(tool.fields.map((field) => [field.id, field.initial])).toEqual([
      ["ppfd", "200"],
      ["photoperiod", "16"],
      ["lighting", "120"],
      ["other", "80"],
      ["demand", "40"],
      ["recovered", "30"],
      ["reservoir", "120"],
    ]);
    expect(tool.courseIds).toEqual([
      "agriculture-construction-habitats",
      "biochemistry",
      "circuits",
    ]);
    expect(calculate("habitat-ledger")).toEqual([
      {
        label: "Daily light integral (DLI)",
        value: 11.52,
        unit: "mol/m²/day",
      },
      { label: "Lighting energy", value: 1.92, unit: "kWh/day" },
      { label: "Total equipment energy", value: 3.84, unit: "kWh/day" },
      { label: "Water makeup", value: 10, unit: "L/day" },
      { label: "Water recovery", value: 75, unit: "%" },
      { label: "Reservoir endurance", value: 12, unit: "days" },
    ]);
    expect(tool.assumptions).toContain("Daily accounting only");
    expect(tool.assumptions).toContain("not crop yield, HVAC");
    expect(tool.assumptions).toContain("life-support certification");
  });

  it("scales habitat light, energy and water inputs without changing their units", () => {
    const result = calculate("habitat-ledger", {
      ppfd: "100",
      photoperiod: "8",
      lighting: "60",
      other: "40",
      demand: "20",
      recovered: "15",
      reservoir: "60",
    });
    expect(result.map((item) => item.value)).toEqual([
      2.88, 0.48, 1.44, 5, 75, 12,
    ]);
    expect(result.map((item) => item.unit)).toEqual([
      "mol/m²/day",
      "kWh/day",
      "kWh/day",
      "L/day",
      "%",
      "days",
    ]);
    expect(calculate("habitat-ledger", { ppfd: "400" })[0].value).toBeCloseTo(
      23.04,
    );
    expect(
      calculate("habitat-ledger", { lighting: "240" }).map(
        (item) => item.value,
      ),
    ).toEqual([11.52, 3.84, 5.76, 10, 75, 12]);
  });

  it("accepts zero light and equipment and omits undefined full-recovery results", () => {
    expect(
      calculate("habitat-ledger", {
        ppfd: "0",
        photoperiod: "0",
        lighting: "0",
        other: "0",
      }).map((item) => item.value),
    ).toEqual([0, 0, 0, 10, 75, 12]);
    expect(calculate("habitat-ledger", { photoperiod: "24" })[0].value).toBe(
      17.28,
    );

    const fullRecovery = calculate("habitat-ledger", { recovered: "40" });
    expect(
      fullRecovery.find((item) => item.label === "Water recovery"),
    ).toEqual({ label: "Water recovery", value: 100, unit: "%" });
    expect(
      fullRecovery.some((item) => item.label === "Reservoir endurance"),
    ).toBe(false);

    const zeroDemand = calculate("habitat-ledger", {
      demand: "0",
      recovered: "0",
    });
    expect(zeroDemand.map((item) => item.label)).not.toContain(
      "Water recovery",
    );
    expect(zeroDemand.map((item) => item.label)).not.toContain(
      "Reservoir endurance",
    );
    expect(zeroDemand.every((item) => Number.isFinite(item.value))).toBe(true);
  });

  it.each([
    "ppfd",
    "photoperiod",
    "lighting",
    "other",
    "demand",
    "recovered",
    "reservoir",
  ])("rejects a negative habitat input: %s", (field) => {
    expect(() => calculate("habitat-ledger", { [field]: "-1" })).toThrow(
      /at least 0/,
    );
  });

  it.each(["", "NaN", "Infinity", "-Infinity"])(
    "rejects a missing or nonfinite habitat input: %s",
    (value) => {
      expect(() => calculate("habitat-ledger", { ppfd: value })).toThrow(
        /finite number/,
      );
    },
  );

  it("rejects impossible habitat schedules, recovery and numeric overflow", () => {
    expect(() => calculate("habitat-ledger", { photoperiod: "24.01" })).toThrow(
      /at most 24/,
    );
    expect(() => calculate("habitat-ledger", { recovered: "41" })).toThrow(
      /cannot exceed water demand/,
    );
    expect(() =>
      calculate("habitat-ledger", { ppfd: "1e308", photoperiod: "24" }),
    ).toThrow(/numeric range/);
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

describe("materials and chemical engineering study tools", () => {
  it("registers eleven tools with the four new course relationships", () => {
    expect(studyTools).toHaveLength(11);
    expect(
      studyTools.find((tool) => tool.id === "crystal-diffraction")?.courseIds,
    ).toEqual(["materials-science"]);
    expect(
      studyTools.find((tool) => tool.id === "stream-balance")?.courseIds,
    ).toEqual(["chemical-engineering-foundations"]);
    expect(
      studyTools.find((tool) => tool.id === "tolerance-stack")?.courseIds,
    ).toEqual(["materials-engineering-fabrication"]);
    expect(
      studyTools.find((tool) => tool.id === "process-capability")?.courseIds,
    ).toEqual([
      "materials-engineering-fabrication",
      "chemical-process-design-scale-up",
    ]);
  });

  it("recomputes cubic spacing and Bragg angles and preserves angular scaling", () => {
    const baseline = calculate("crystal-diffraction");
    const expectedTheta = Math.asin(0.154 / (2 * 0.4)) * (180 / Math.PI);
    expect(baseline[0]).toEqual({
      label: "Cubic interplanar spacing d",
      value: 0.4,
      unit: "nm",
    });
    expect(baseline[1].value).toBeCloseTo(expectedTheta, 12);
    expect(baseline[2].value).toBeCloseTo(2 * expectedTheta, 12);

    const scaled = calculate("crystal-diffraction", {
      a: "0.8",
      wavelength: "0.308",
    });
    expect(scaled[0].value).toBeCloseTo(0.8, 12);
    expect(scaled[1].value).toBeCloseTo(expectedTheta, 12);
    expect(scaled[2].value).toBeCloseTo(2 * expectedTheta, 12);

    const d210 = calculate("crystal-diffraction", {
      h: "2",
      k: "1",
      l: "0",
    });
    expect(d210[0].value).toBeCloseTo(0.4 / Math.sqrt(5), 12);
  });

  it("accepts zero indices and the lambda equals 2d grazing boundary", () => {
    const boundary = calculate("crystal-diffraction", {
      h: "0",
      k: "0",
      l: "1",
      wavelength: "0.8",
    });
    expect(boundary.map((item) => item.value)).toEqual([0.4, 90, 180]);
    expect(() =>
      calculate("crystal-diffraction", { wavelength: "0.8000001" }),
    ).toThrow(/cannot exceed 2d/);
  });

  it.each(["h", "k", "l"])(
    "rejects negative and fractional Miller index %s",
    (field) => {
      expect(() => calculate("crystal-diffraction", { [field]: "-1" })).toThrow(
        /at least 0/,
      );
      expect(() =>
        calculate("crystal-diffraction", { [field]: "1.5" }),
      ).toThrow(/integer/);
    },
  );

  it("rejects missing, nonfinite, zero-family and overflow diffraction inputs", () => {
    expect(() =>
      calculate("crystal-diffraction", { h: "0", k: "0", l: "0" }),
    ).toThrow(/cannot all be zero/);
    for (const value of ["", "NaN", "Infinity", "-Infinity"])
      expect(() =>
        calculate("crystal-diffraction", { wavelength: value }),
      ).toThrow(/finite number/);
    expect(() => calculate("crystal-diffraction", { a: "0" })).toThrow(
      /greater than 0/,
    );
    expect(() => calculate("crystal-diffraction", { wavelength: "0" })).toThrow(
      /greater than 0/,
    );
    expect(() =>
      calculate("crystal-diffraction", {
        a: "1e308",
        h: "1.7e308",
        k: "1.7e308",
        l: "1.7e308",
      }),
    ).toThrow(/numeric range/);
    expect(() =>
      calculate("crystal-diffraction", {
        a: "1e-308",
        h: "1e308",
        wavelength: "1e-308",
      }),
    ).toThrow(/numeric range|cannot exceed 2d/);
  });

  it("recomputes one-to-one reactive flows and scales every flow linearly", () => {
    expect(calculate("stream-balance")).toEqual([
      { label: "A in", value: 80, unit: "mol/h" },
      { label: "A out", value: 40, unit: "mol/h" },
      { label: "B formed", value: 40, unit: "mol/h" },
      { label: "B product", value: 36, unit: "mol/h" },
      { label: "B unrecovered", value: 4, unit: "mol/h" },
      {
        label: "A balance closure residual",
        value: 0,
        unit: "mol/h",
      },
    ]);
    const scaled = calculate("stream-balance", { feed: "250" });
    expect(scaled.map((item) => item.value)).toEqual([
      200, 100, 100, 90, 10, 0,
    ]);
    const independent = calculate("stream-balance", {
      feed: "120",
      feedFraction: "0.25",
      conversion: "0.2",
      recovery: "0.75",
    });
    expect(independent.map((item) => item.value)).toEqual([
      30, 24, 6, 4.5, 1.5, 0,
    ]);
  });

  it("keeps zero flow, conversion and recovery distinct from missing data", () => {
    expect(
      calculate("stream-balance", { feed: "0" }).map((item) => item.value),
    ).toEqual([0, 0, 0, 0, 0, 0]);
    expect(
      calculate("stream-balance", { conversion: "0" }).map(
        (item) => item.value,
      ),
    ).toEqual([80, 80, 0, 0, 0, 0]);
    expect(
      calculate("stream-balance", { recovery: "0" }).map((item) => item.value),
    ).toEqual([80, 40, 40, 0, 40, 0]);
    expect(() => calculate("stream-balance", { feed: "" })).toThrow(
      /finite number/,
    );
    expect(() => calculate("stream-balance", { feed: "-1" })).toThrow(
      /at least 0/,
    );
    expect(
      calculate("stream-balance", {
        feed: "1e308",
        feedFraction: "1",
        conversion: "1",
        recovery: "1",
      }).every((item) => Number.isFinite(item.value)),
    ).toBe(true);
  });

  it.each(["feedFraction", "conversion", "recovery"])(
    "validates the cross-field fraction domain for %s",
    (field) => {
      expect(() => calculate("stream-balance", { [field]: "-0.01" })).toThrow(
        /at least 0/,
      );
      expect(() => calculate("stream-balance", { [field]: "1.01" })).toThrow(
        /at most 1/,
      );
      expect(() =>
        calculate("stream-balance", { [field]: "Infinity" }),
      ).toThrow(/finite number/);
    },
  );

  it("always computes worst case and gates conditional RSS on independence", () => {
    const defaults = calculate("tolerance-stack");
    expect(defaults).toEqual([
      { label: "Nominal total", value: 60, unit: "mm" },
      {
        label: "Worst-case tolerance (±)",
        value: 0.6000000000000001,
        unit: "mm",
      },
    ]);
    const independent = calculate("tolerance-stack", {
      variationModel: "independent",
    });
    expect(independent.slice(0, 2)).toEqual(defaults);
    expect(independent[2].label).toContain("Conditional independent RSS");
    expect(independent[2].value).toBeCloseTo(Math.sqrt(0.14), 12);

    const scaled = calculate("tolerance-stack", {
      x1: "20",
      x2: "40",
      x3: "60",
      t1: "0.2",
      t2: "0.4",
      t3: "0.6",
      variationModel: "independent",
    });
    expect(scaled[0].value).toBe(120);
    expect(scaled[1].value).toBeCloseTo(1.2, 12);
    expect(scaled[2].value).toBeCloseTo(2 * Math.sqrt(0.14), 12);
  });

  it("handles signed and zero stack values and rejects invalid or overflowing stacks", () => {
    const zero = calculate("tolerance-stack", {
      x1: "0",
      x2: "-10",
      x3: "10",
      t1: "0",
      t2: "0",
      t3: "0",
      variationModel: "independent",
    });
    expect(zero.map((item) => item.value)).toEqual([0, 0, 0]);
    expect(() => calculate("tolerance-stack", { t1: "-0.1" })).toThrow(
      /at least 0/,
    );
    expect(() => calculate("tolerance-stack", { x1: "NaN" })).toThrow(
      /finite number/,
    );
    expect(() =>
      calculate("tolerance-stack", { x1: "1e308", x2: "1e308" }),
    ).toThrow(/numeric range/);
    expect(() =>
      calculate("tolerance-stack", {
        t1: "1e308",
        t2: "1e308",
        t3: "1e308",
        variationModel: "independent",
      }),
    ).toThrow(/numeric range/);
    expect(() =>
      calculate("tolerance-stack", { variationModel: "assumed" }),
    ).toThrow(/Select a declared/);
  });

  it("omits process indices for unknown or unstable states and recomputes stable Cp/Cpk", () => {
    expect(calculate("process-capability")).toEqual([]);
    expect(
      calculate("process-capability", { processState: "unstable" }),
    ).toEqual([]);
    const stable = calculate("process-capability", { processState: "stable" });
    expect(stable.map((item) => item.label)).toEqual([
      "Cp (declared stable process)",
      "Cpk (declared stable process)",
    ]);
    expect(stable[0].value).toBeCloseTo((60 - 40) / (6 * 2), 12);
    expect(stable[1].value).toBeCloseTo(
      Math.min(60 - 50, 50 - 40) / (3 * 2),
      12,
    );
    const scaled = calculate("process-capability", {
      mean: "100",
      sd: "4",
      lsl: "80",
      usl: "120",
      processState: "stable",
    });
    expect(scaled[0].value).toBeCloseTo(stable[0].value, 12);
    expect(scaled[1].value).toBeCloseTo(stable[1].value, 12);
    const offCenter = calculate("process-capability", {
      mean: "55",
      processState: "stable",
    });
    expect(offCenter[0].value).toBeCloseTo(5 / 3, 12);
    expect(offCenter[1].value).toBeCloseTo(5 / 6, 12);
  });

  it("validates process fields in every state and rejects numeric overflow", () => {
    for (const state of ["unknown", "unstable", "stable"]) {
      expect(() =>
        calculate("process-capability", { sd: "0", processState: state }),
      ).toThrow(/greater than 0/);
      expect(() =>
        calculate("process-capability", {
          lsl: "60",
          usl: "40",
          processState: state,
        }),
      ).toThrow(/less than USL/);
      expect(() =>
        calculate("process-capability", {
          lsl: "40",
          usl: "40",
          processState: state,
        }),
      ).toThrow(/less than USL/);
      expect(() =>
        calculate("process-capability", {
          mean: "Infinity",
          processState: state,
        }),
      ).toThrow(/finite number/);
    }
    expect(() =>
      calculate("process-capability", {
        lsl: "-1e308",
        usl: "1e308",
        processState: "stable",
      }),
    ).toThrow(/numeric range/);
    expect(() =>
      calculate("process-capability", { processState: "inferred" }),
    ).toThrow(/Select a declared/);
  });
});
