export type StudyToolId =
  | "dilution"
  | "buffer"
  | "enzyme"
  | "rc"
  | "diffusion"
  | "ohm"
  | "habitat-ledger"
  | "crystal-diffraction"
  | "stream-balance"
  | "tolerance-stack"
  | "process-capability";

type Field = {
  id: string;
  label: string;
  initial: string;
  minimum?: number;
  exclusiveMinimum?: boolean;
  maximum?: number;
};

type StudyToolControl = {
  id: string;
  label: string;
  initial: string;
  options: {
    value: string;
    label: string;
    resultNote: string;
  }[];
};

export type StudyTool = {
  id: StudyToolId;
  title: string;
  description: string;
  equation: string;
  assumptions: string;
  fields: Field[];
  controls?: StudyToolControl[];
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
  {
    id: "crystal-diffraction",
    title: "Cubic crystal diffraction",
    description:
      "Calculate cubic interplanar spacing and a first-order Bragg angle for a synthetic reflection.",
    equation: "dₕₖₗ = a/√(h² + k² + l²); 2d sin(θ) = λ; 2θ = 2asin[λ/(2d)]",
    assumptions:
      "Cubic, first-order toy model only. Lattice parameter and wavelength must use the same length unit (nm here); h, k and l are nonnegative integers and cannot all be zero. This is not phase identification, crystallographic refinement, an instrument procedure or a source of instrument settings.",
    fields: [
      {
        id: "a",
        label: "Cubic lattice parameter a (nm)",
        initial: "0.4",
        minimum: 0,
        exclusiveMinimum: true,
      },
      { id: "h", label: "Miller index h", initial: "1", minimum: 0 },
      { id: "k", label: "Miller index k", initial: "0", minimum: 0 },
      { id: "l", label: "Miller index l", initial: "0", minimum: 0 },
      {
        id: "wavelength",
        label: "Wavelength λ (nm)",
        initial: "0.154",
        minimum: 0,
        exclusiveMinimum: true,
      },
    ],
    courseIds: ["materials-science"],
  },
  {
    id: "stream-balance",
    title: "Reactive stream balance",
    description:
      "Close a steady synthetic reactor/separator balance for generic species A and B.",
    equation:
      "A in = FzA; B formed = X(A in); A out = A in − B formed; B product = R(B formed)",
    assumptions:
      "Steady synthetic arithmetic for exactly 1 mol A → 1 mol B, with no other reaction and no invented recycle, bypass or accumulation. Feed flow is total mol/h, zA is feed A mole fraction, X is fractional conversion of feed A and R is fractional recovery of formed B into product. B unrecovered is formed B minus product B. Closure residual is A in − A out − B formed. Missing data are not zero; this is not a plant recipe, operating target or safety assessment.",
    fields: [
      {
        id: "feed",
        label: "Total feed flow (mol/h)",
        initial: "100",
        minimum: 0,
      },
      {
        id: "feedFraction",
        label: "Feed A mole fraction",
        initial: "0.8",
        minimum: 0,
        maximum: 1,
      },
      {
        id: "conversion",
        label: "A conversion fraction",
        initial: "0.5",
        minimum: 0,
        maximum: 1,
      },
      {
        id: "recovery",
        label: "B recovery fraction",
        initial: "0.9",
        minimum: 0,
        maximum: 1,
      },
    ],
    courseIds: ["chemical-engineering-foundations"],
  },
  {
    id: "tolerance-stack",
    title: "Tolerance stack",
    description:
      "Compare a three-term arithmetic worst-case stack with a conditional independent RSS model.",
    equation:
      "Nominal total = Σxᵢ; worst-case tolerance = Σtᵢ; conditional RSS = √(Σtᵢ²)",
    assumptions:
      "Adds three signed nominal dimensions in one declared linear direction; each symmetric tolerance is ±tᵢ. Worst case is the arithmetic sum. RSS is shown only after explicitly declaring independent variation; it is a conditional statistical model, not a guaranteed limit. This does not establish GD&T compliance, inspection acceptance, assembly conformity or design release.",
    fields: [
      { id: "x1", label: "Nominal dimension 1 (mm)", initial: "10" },
      { id: "x2", label: "Nominal dimension 2 (mm)", initial: "20" },
      { id: "x3", label: "Nominal dimension 3 (mm)", initial: "30" },
      {
        id: "t1",
        label: "Symmetric tolerance 1 (±mm)",
        initial: "0.1",
        minimum: 0,
      },
      {
        id: "t2",
        label: "Symmetric tolerance 2 (±mm)",
        initial: "0.2",
        minimum: 0,
      },
      {
        id: "t3",
        label: "Symmetric tolerance 3 (±mm)",
        initial: "0.3",
        minimum: 0,
      },
    ],
    controls: [
      {
        id: "variationModel",
        label: "RSS variation model",
        initial: "not-declared",
        options: [
          {
            value: "not-declared",
            label: "Independence not declared — omit RSS",
            resultNote:
              "RSS is omitted because independent variation has not been declared. The nominal total and worst-case sum do not require that statistical assumption.",
          },
          {
            value: "independent",
            label: "Declare independent variation for conditional RSS",
            resultNote:
              "RSS is conditional on the declared independent-variation model. Dependence or shared causes would require a different model; this arithmetic is not GD&T compliance or acceptance evidence.",
          },
        ],
      },
    ],
    courseIds: ["materials-engineering-fabrication"],
  },
  {
    id: "process-capability",
    title: "Process capability indices",
    description:
      "Calculate Cp and Cpk only for an explicitly declared stable synthetic process.",
    equation: "Cp = (USL − LSL)/(6s); Cpk = min(USL − mean, mean − LSL)/(3s)",
    assumptions:
      "Uses the entered sample standard deviation s and consistent units. Cp/Cpk are omitted for unknown or unstable process states and require LSL < USL and s > 0 even for those states. A stable declaration does not prove normality, appropriate subgrouping/pooling, measurement adequacy or future performance. Arithmetic alone never means capable, accepted, conforming, validated or release-approved.",
    fields: [
      { id: "mean", label: "Sample mean", initial: "50" },
      {
        id: "sd",
        label: "Sample standard deviation s",
        initial: "2",
        minimum: 0,
        exclusiveMinimum: true,
      },
      { id: "lsl", label: "Lower specification limit (LSL)", initial: "40" },
      { id: "usl", label: "Upper specification limit (USL)", initial: "60" },
    ],
    controls: [
      {
        id: "processState",
        label: "Declared process state",
        initial: "unknown",
        options: [
          {
            value: "unknown",
            label: "Unknown — omit Cp and Cpk",
            resultNote:
              "Cp and Cpk are omitted because process stability is unknown. Establish stability with appropriate evidence before interpreting capability indices.",
          },
          {
            value: "unstable",
            label: "Unstable — omit Cp and Cpk",
            resultNote:
              "Cp and Cpk are omitted because the process is declared unstable. Investigate the process rather than interpreting capability indices.",
          },
          {
            value: "stable",
            label: "Stable — show arithmetic Cp and Cpk",
            resultNote:
              "Cp and Cpk are arithmetic for the declared stable state only. They do not establish capability, acceptance, validation or release approval.",
          },
        ],
      },
    ],
    courseIds: [
      "materials-engineering-fabrication",
      "chemical-process-design-scale-up",
    ],
  },
  {
    id: "habitat-ledger",
    title: "Habitat ledger",
    description:
      "Estimate daily light, equipment-energy and water accounting for a habitat model.",
    equation:
      "DLI = PPFD × hours × 3600/10⁶; energy = power × hours/1000; makeup = demand − recovered",
    assumptions:
      "Daily accounting only: other equipment runs for 24 hours, and reservoir endurance is reservoir volume divided by positive daily makeup. This is not crop yield, HVAC, nutrient prescription, or life-support certification. Recovery percentage is omitted at zero demand, and endurance is omitted at full recovery.",
    fields: [
      { id: "ppfd", label: "PPFD (μmol/m²/s)", initial: "200", minimum: 0 },
      {
        id: "photoperiod",
        label: "Photoperiod (h/day)",
        initial: "16",
        minimum: 0,
        maximum: 24,
      },
      {
        id: "lighting",
        label: "Lighting power (W)",
        initial: "120",
        minimum: 0,
      },
      {
        id: "other",
        label: "Other continuous equipment (W)",
        initial: "80",
        minimum: 0,
      },
      {
        id: "demand",
        label: "Water demand (L/day)",
        initial: "40",
        minimum: 0,
      },
      {
        id: "recovered",
        label: "Recovered water (L/day)",
        initial: "30",
        minimum: 0,
      },
      {
        id: "reservoir",
        label: "Reservoir volume (L)",
        initial: "120",
        minimum: 0,
      },
    ],
    courseIds: [
      "agriculture-construction-habitats",
      "biochemistry",
      "circuits",
    ],
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
    if (field.maximum !== undefined && value > field.maximum) {
      throw new Error(`${field.label} must be at most ${field.maximum}.`);
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
    case "crystal-diffraction": {
      for (const index of ["h", "k", "l"] as const) {
        if (!Number.isInteger(values[index]))
          throw new Error(
            `${tool.fields.find((field) => field.id === index)!.label} must be an integer.`,
          );
      }
      if (values.h === 0 && values.k === 0 && values.l === 0)
        throw new Error("Miller indices h, k and l cannot all be zero.");
      const norm = Math.hypot(values.h, values.k, values.l);
      const spacing = values.a / norm;
      if (!Number.isFinite(norm) || !Number.isFinite(spacing) || spacing <= 0)
        throw new Error(
          "These inputs exceed the calculator’s numeric range. Use smaller or larger values.",
        );
      const scaledWavelength = values.wavelength / spacing;
      if (!Number.isFinite(scaledWavelength) || scaledWavelength > 2)
        throw new Error(
          "Wavelength cannot exceed 2d for a first-order Bragg reflection.",
        );
      const theta = Math.asin(scaledWavelength / 2) * (180 / Math.PI);
      result = [
        { label: "Cubic interplanar spacing d", value: spacing, unit: "nm" },
        { label: "Bragg angle θ", value: theta, unit: "°" },
        { label: "Diffraction angle 2θ", value: 2 * theta, unit: "°" },
      ];
      break;
    }
    case "stream-balance": {
      const aIn = values.feed * values.feedFraction;
      const bFormed = aIn * values.conversion;
      const aOut = aIn - bFormed;
      const bProduct = bFormed * values.recovery;
      result = [
        { label: "A in", value: aIn, unit: "mol/h" },
        { label: "A out", value: aOut, unit: "mol/h" },
        { label: "B formed", value: bFormed, unit: "mol/h" },
        { label: "B product", value: bProduct, unit: "mol/h" },
        {
          label: "B unrecovered",
          value: bFormed - bProduct,
          unit: "mol/h",
        },
        {
          label: "A balance closure residual",
          value: aIn - aOut - bFormed,
          unit: "mol/h",
        },
      ];
      break;
    }
    case "tolerance-stack": {
      const model = input.variationModel ?? "not-declared";
      if (!["not-declared", "independent"].includes(model))
        throw new Error("Select a declared RSS variation model.");
      result = [
        {
          label: "Nominal total",
          value: values.x1 + values.x2 + values.x3,
          unit: "mm",
        },
        {
          label: "Worst-case tolerance (±)",
          value: values.t1 + values.t2 + values.t3,
          unit: "mm",
        },
      ];
      if (model === "independent")
        result.push({
          label: "Conditional independent RSS tolerance (±)",
          value: Math.hypot(values.t1, values.t2, values.t3),
          unit: "mm",
        });
      break;
    }
    case "process-capability": {
      const state = input.processState ?? "unknown";
      if (!["unknown", "unstable", "stable"].includes(state))
        throw new Error("Select a declared process state.");
      if (values.lsl >= values.usl)
        throw new Error("Lower specification limit must be less than USL.");
      result = [];
      if (state === "stable") {
        const width = values.usl - values.lsl;
        const upperDistance = values.usl - values.mean;
        const lowerDistance = values.mean - values.lsl;
        const cpDenominator = 6 * values.sd;
        const cpkDenominator = 3 * values.sd;
        if (
          ![width, upperDistance, lowerDistance].every(Number.isFinite) ||
          !Number.isFinite(cpDenominator) ||
          !Number.isFinite(cpkDenominator) ||
          cpDenominator <= 0 ||
          cpkDenominator <= 0
        )
          throw new Error(
            "These inputs exceed the calculator’s numeric range. Use smaller or larger values.",
          );
        const cp = width / cpDenominator;
        const cpk = Math.min(upperDistance, lowerDistance) / cpkDenominator;
        result = [
          { label: "Cp (declared stable process)", value: cp, unit: "" },
          { label: "Cpk (declared stable process)", value: cpk, unit: "" },
        ];
      }
      break;
    }
    case "habitat-ledger": {
      if (values.recovered > values.demand)
        throw new Error("Recovered water cannot exceed water demand.");
      const makeup = values.demand - values.recovered;
      const lightingEnergy = (values.lighting * values.photoperiod) / 1000;
      const otherEnergy = (values.other * 24) / 1000;
      result = [
        {
          label: "Daily light integral (DLI)",
          value: (values.ppfd * values.photoperiod * 3600) / 1e6,
          unit: "mol/m²/day",
        },
        { label: "Lighting energy", value: lightingEnergy, unit: "kWh/day" },
        {
          label: "Total equipment energy",
          value: lightingEnergy + otherEnergy,
          unit: "kWh/day",
        },
        { label: "Water makeup", value: makeup, unit: "L/day" },
      ];
      if (values.demand > 0)
        result.push({
          label: "Water recovery",
          value: (values.recovered / values.demand) * 100,
          unit: "%",
        });
      if (makeup > 0)
        result.push({
          label: "Reservoir endurance",
          value: values.reservoir / makeup,
          unit: "days",
        });
      break;
    }
  }
  if (result.some((item) => !Number.isFinite(item.value)))
    throw new Error(
      "These inputs exceed the calculator’s numeric range. Use smaller values.",
    );
  return result;
}
