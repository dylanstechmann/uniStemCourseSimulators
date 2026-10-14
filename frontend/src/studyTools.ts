export type StudyToolId =
  "dilution" | "buffer" | "enzyme" | "rc" | "diffusion" | "ohm";

type Field = {
  id: string;
  label: string;
  initial: string;
  minimum?: number;
  exclusiveMinimum?: boolean;
};

export type StudyTool = {
  id: StudyToolId;
  title: string;
  description: string;
  equation: string;
  assumptions: string;
  fields: Field[];
  courseIds: string[];
};

export const studyTools: StudyTool[] = [
  {
    id: "dilution",
    title: "Dilution",
    description:
      "Find the stock and diluent volumes for a target concentration.",
    equation: "C₁V₁ = C₂V₂; V₁ = C₂V₂/C₁",
    assumptions:
      "Uses the same concentration unit for stock and target and assumes additive volumes. The target cannot exceed the stock concentration.",
    fields: [
      {
        id: "stock",
        label: "Stock concentration (mM)",
        initial: "100",
        minimum: 0,
        exclusiveMinimum: true,
      },
      {
        id: "target",
        label: "Target concentration (mM)",
        initial: "2",
        minimum: 0,
      },
      {
        id: "volume",
        label: "Final volume (mL)",
        initial: "25",
        minimum: 0,
        exclusiveMinimum: true,
      },
    ],
    courseIds: ["cell-biology", "general-chemistry-1", "bioreactors"],
  },
  {
    id: "buffer",
    title: "Buffer pH",
    description:
      "Explore the Henderson–Hasselbalch concentration approximation.",
    equation: "pH = pKa + log₁₀([base]/[acid])",
    assumptions:
      "Assumes both conjugate forms are present and concentration ratios approximate activity ratios. Account for any strong acid or base reaction before entering the remaining concentrations.",
    fields: [
      { id: "pka", label: "pKa", initial: "7.2" },
      {
        id: "base",
        label: "Conjugate-base concentration (mM)",
        initial: "10",
        minimum: 0,
        exclusiveMinimum: true,
      },
      {
        id: "acid",
        label: "Conjugate-acid concentration (mM)",
        initial: "1",
        minimum: 0,
        exclusiveMinimum: true,
      },
    ],
    courseIds: ["general-chemistry-2", "cell-biology"],
  },
  {
    id: "enzyme",
    title: "Enzyme kinetics",
    description: "Calculate a rate in the simple Michaelis–Menten model.",
    equation: "v = Vmax[S]/(Km + [S])",
    assumptions:
      "Assumes initial-rate, steady-state Michaelis–Menten behavior, with no inhibitor or cooperativity. Km and substrate concentration use the same unit.",
    fields: [
      { id: "vmax", label: "Vmax (μM/min)", initial: "100", minimum: 0 },
      {
        id: "km",
        label: "Km (μM)",
        initial: "5",
        minimum: 0,
        exclusiveMinimum: true,
      },
      {
        id: "substrate",
        label: "Substrate concentration (μM)",
        initial: "10",
        minimum: 0,
      },
    ],
    courseIds: ["cell-biology", "biochemistry"],
  },
  {
    id: "rc",
    title: "RC charging",
    description:
      "Find the time constant and fraction of an ideal voltage step reached.",
    equation: "τ = RC; fraction charged = 1 − exp(−t/τ)",
    assumptions:
      "Assumes an ideal series RC circuit, an initially uncharged capacitor, and a constant voltage step. Resistance is entered in kΩ and capacitance in μF.",
    fields: [
      {
        id: "resistance",
        label: "Resistance (kΩ)",
        initial: "100",
        minimum: 0,
        exclusiveMinimum: true,
      },
      {
        id: "capacitance",
        label: "Capacitance (μF)",
        initial: "10",
        minimum: 0,
        exclusiveMinimum: true,
      },
      { id: "time", label: "Time (s)", initial: "1", minimum: 0 },
    ],
    courseIds: ["circuits", "physics-em"],
  },
  {
    id: "diffusion",
    title: "Diffusion timescale",
    description:
      "Estimate how diffusion time scales with distance and diffusivity.",
    equation: "t ≈ L²/D",
    assumptions:
      "This is a characteristic timescale. Geometry, boundary conditions, advection, and reactions determine a full transport solution.",
    fields: [
      {
        id: "length",
        label: "Diffusion distance (μm)",
        initial: "100",
        minimum: 0,
      },
      {
        id: "diffusivity",
        label: "Diffusivity (m²/s)",
        initial: "1e-9",
        minimum: 0,
        exclusiveMinimum: true,
      },
    ],
    courseIds: ["transport", "cell-biology"],
  },
  {
    id: "ohm",
    title: "Ohm’s law",
    description: "Calculate current and dissipated power for a resistive load.",
    equation: "I = V/R; P = VI",
    assumptions:
      "Assumes a positive, constant ohmic resistance. The voltage sign sets the current direction; dissipated power is nonnegative.",
    fields: [
      { id: "voltage", label: "Voltage (V)", initial: "5" },
      {
        id: "resistance",
        label: "Resistance (kΩ)",
        initial: "10",
        minimum: 0,
        exclusiveMinimum: true,
      },
    ],
    courseIds: ["circuits", "physics-em"],
  },
];

export type StudyToolResult = {
  label: string;
  value: number;
  unit: string;
}[];

export function calculateStudyTool(
  tool: StudyTool,
  input: Record<string, string>,
): StudyToolResult {
  const values: Record<string, number> = {};
  for (const field of tool.fields) {
    const raw = input[field.id]?.trim();
    const value = Number(raw);
    if (!raw || !Number.isFinite(value)) {
      throw new Error(`Enter a finite number for ${field.label}.`);
    }
    if (
      field.minimum !== undefined &&
      (field.exclusiveMinimum ? value <= field.minimum : value < field.minimum)
    ) {
      throw new Error(
        `${field.label} must be ${field.exclusiveMinimum ? "greater than" : "at least"} ${field.minimum}.`,
      );
    }
    values[field.id] = value;
  }
  let result: StudyToolResult;
  switch (tool.id) {
    case "dilution": {
      if (values.target > values.stock)
        throw new Error(
          "The target concentration cannot exceed the stock concentration by dilution.",
        );
      const stockVolume = (values.target / values.stock) * values.volume;
      result = [
        { label: "Stock volume", value: stockVolume, unit: "mL" },
        {
          label: "Diluent volume",
          value: values.volume - stockVolume,
          unit: "mL",
        },
      ];
      break;
    }
    case "buffer":
      result = [
        {
          label: "Approximate pH",
          value: values.pka + Math.log10(values.base) - Math.log10(values.acid),
          unit: "",
        },
      ];
      break;
    case "enzyme": {
      const ratio = values.substrate / values.km;
      const fraction =
        values.substrate >= values.km
          ? 1 / (1 + values.km / values.substrate)
          : ratio / (1 + ratio);
      result = [
        {
          label: "Initial rate",
          value: values.vmax * fraction,
          unit: "μM/min",
        },
        { label: "Fraction of Vmax", value: fraction * 100, unit: "%" },
      ];
      break;
    }
    case "rc": {
      const tau = values.resistance * values.capacitance * 1e-3;
      if (!Number.isFinite(tau) || tau <= 0)
        throw new Error(
          "These inputs exceed the calculator’s numeric range. Use smaller or larger values.",
        );
      result = [
        { label: "Time constant", value: tau, unit: "s" },
        {
          label: "Voltage step reached",
          value: -Math.expm1(-values.time / tau) * 100,
          unit: "%",
        },
      ];
      break;
    }
    case "diffusion":
      result = [
        {
          label: "Characteristic diffusion time",
          value: (values.length * 1e-6) ** 2 / values.diffusivity,
          unit: "s",
        },
      ];
      break;
    case "ohm": {
      const current = values.voltage / values.resistance;
      result = [
        { label: "Current", value: current, unit: "mA" },
        {
          label: "Dissipated power",
          value: values.voltage * current,
          unit: "mW",
        },
      ];
      break;
    }
  }
  if (result.some((item) => !Number.isFinite(item.value)))
    throw new Error(
      "These inputs exceed the calculator’s numeric range. Use smaller values.",
    );
  return result;
}
