"""Generate answer-free Biochemistry homework 3–8 candidates from authored prompts."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "content/courses/biochemistry"
VERSION = "0.4.31"
GATES = [
    "independent-recalculation",
    "grader-mutation-review",
    "qualified-biochemical-review",
    "assessment-blueprint-review",
    "accessibility-and-fairness-review",
    "measured-workload",
    "candidate-specific-protected-delivery-verification",
    "operator-release-and-retake-policy",
]


def field(fid, prompt, objective, kind="single_choice", unit=None, options=None, sig=None):
    return {
        "id": fid,
        "prompt": prompt,
        "objective_ids": objective if isinstance(objective, list) else [objective],
        "type": kind,
        "unit": unit,
        "options": options or [],
        "sig": sig,
    }


def question(case, prompt, left, right):
    return {"id": case, "prompt": prompt, "fields": [left, right]}


SPECS = [
    {
        "number": 3,
        "title": "Homework 3 review candidate: enzyme mechanisms and kinetic models",
        "weeks": [5, 6],
        "purpose": (
            "This set moves from mechanism language to model-based quantities. It tests "
            "what the simplest Michaelis–Menten and inhibition models allow a learner to "
            "calculate, and what those calculations cannot establish. The numerical values "
            "are synthetic and are supplied only for the questions listed below."
        ),
        "items": [
            question(
                "case-01",
                "A fictional inhibitor binds only the free enzyme and competes with substrate for the same site.",
                field("mechanism-model", "Which simple inhibition model is most consistent with the stated binding competition?", "biochemistry-2-objective-1", options=["Competitive inhibition.", "Pure noncompetitive inhibition.", "Uncompetitive inhibition."]),
                field("model-limit", "Which statement should accompany a simple inhibition diagnosis?", "biochemistry-2-objective-2", options=["It is conditional on the model and assay assumptions.", "It proves the inhibitor binds in a living organism.", "It identifies the inhibitor structure."]),
            ),
            question(
                "case-02",
                "Use the catalytic parameters and total enzyme amount in the synthetic dataset.",
                field("rate-at-substrate", "Calculate the initial rate at the listed substrate concentration with the Michaelis–Menten relation.", "biochemistry-5-objective-1", "numeric", "µmol/min", sig=3),
                field("turnover-number", "Calculate kcat from Vmax and the listed total active-enzyme amount in the assay.", "biochemistry-5-objective-1", "numeric", "1/min", sig=3),
            ),
            question(
                "case-03",
                "Use the stated kcat and Km inputs; preserve compatible units when calculating catalytic efficiency.",
                field("catalytic-efficiency", "Calculate kcat/Km and report compatible concentration and time units.", "biochemistry-2-objective-2", "numeric", "L/(µmol·min)", sig=3),
                field("efficiency-limit", "Which interpretation of kcat/Km is appropriate under the stated model?", "biochemistry-2-objective-2", options=["It is a model-based efficiency measure, not a universal binding constant.", "It is numerically identical to Kd in every mechanism.", "It does not depend on the units chosen for concentration."]),
            ),
            question(
                "case-04",
                "Compare the control and inhibitor parameters in the dataset under the stated simple models.",
                field("apparent-km", "Which apparent Km pattern is expected for the listed competitive-inhibitor input?", "biochemistry-5-objective-2", options=["Apparent Km increases while Vmax is unchanged in the simple model.", "Apparent Km decreases while Vmax is unchanged.", "Both apparent Km and Vmax must become zero."]),
                field("noncompetitive-pattern", "Which pair of apparent parameter changes is associated with pure noncompetitive inhibition in the simple model?", "biochemistry-5-objective-2", options=["Vmax decreases while Km is unchanged.", "Vmax is unchanged while Km increases.", "Both Vmax and Km increase by the same factor."]),
            ),
            question(
                "case-05",
                "A learner estimates parameters from a reciprocal plot built from a small set of rates.",
                field("linearized-risk", "Why can a double-reciprocal plot distort parameter estimates?", "biochemistry-5-objective-3", options=["Reciprocal transformation disproportionately weights low-substrate, low-rate observations.", "It removes measurement error from every point.", "It makes all assay conditions equivalent."]),
                field("assay-condition", "Which assay feature most directly supports interpretation of a measured rate as an initial velocity?", ["biochemistry-5-objective-3", "biochemistry-2-objective-2"], options=["A short linear time window with substrate depletion and product accumulation kept small.", "A long endpoint after substrate is exhausted.", "Mixing rates from different enzyme concentrations without normalization."]),
            ),
        ],
        "data": [
            ["case-01", "inhibitor_binding_site", "free enzyme substrate site", "none", "fictional mechanistic stipulation"],
            ["case-02", "vmax", "120", "µmol/min", "synthetic model parameter"],
            ["case-02", "km", "30", "µM", "synthetic model parameter"],
            ["case-02", "substrate", "45", "µM", "synthetic model input"],
            ["case-02", "active_enzyme", "0.20", "µmol", "synthetic total active-enzyme amount in the assay"],
            ["case-03", "kcat", "600", "min−1", "synthetic model parameter"],
            ["case-03", "km", "30", "µM", "synthetic model parameter"],
            ["case-04", "control_vmax", "100", "µmol/min", "simple model reference"],
            ["case-04", "competitive_vmax", "100", "µmol/min", "stipulated simple-model value"],
            ["case-04", "competitive_km", "75", "µM", "stipulated simple-model value"],
            ["case-04", "noncompetitive_vmax", "55", "µmol/min", "stipulated simple-model value"],
            ["case-04", "noncompetitive_km", "30", "µM", "stipulated simple-model value"],
            ["case-05", "substrate_range", "low to saturating", "none", "reciprocal-fit interpretation prompt; no raw learner observations supplied"],
        ],
    },
    {
        "number": 4,
        "title": "Homework 4 review candidate: enzyme-kinetics data analysis",
        "weeks": [7],
        "dataset_note": (
            "For case 3, the `inhibitor_concentration_uM` column gives the stipulated "
            "inhibitor concentration on inhibitor-condition rows. "
        ),
        "purpose": (
            "This set practices the full data path from replicate summaries to fitted "
            "parameters and an evidence-bounded inhibition interpretation. Each row in "
            "the accompanying dataset is a synthetic initial-rate observation. It is not "
            "a wet-lab protocol and does not identify a real enzyme or inhibitor."
        ),
        "items": [
            question(
                "case-01",
                "Use the paired replicate initial-rate observations in the dataset and keep substrate concentrations grouped by condition.",
                field("control-mean-rate", "Calculate the mean control initial rate at 40 µM substrate.", "biochemistry-lab-01-objective-1", "numeric", "µmol/min", sig=3),
                field("inhibitor-mean-rate", "Calculate the mean inhibitor-condition initial rate at 40 µM substrate.", "biochemistry-lab-01-objective-1", "numeric", "µmol/min", sig=3),
            ),
            question(
                "case-02",
                "Fit the untransformed control replicate means to v = Vmax[S]/(Km + [S]) by minimizing squared rate residuals; do not use a reciprocal plot.",
                field("control-vmax", "Estimate Vmax for the control series.", "biochemistry-lab-01-objective-2", "numeric", "µmol/min", sig=3),
                field("control-km", "Estimate Km for the control series.", "biochemistry-lab-01-objective-2", "numeric", "µM", sig=3),
            ),
            question(
                "case-03",
                "Compare the inhibitor series with control at matched substrate concentrations.",
                field("inhibited-km", "Estimate apparent Km under the inhibitor condition.", "biochemistry-lab-01-objective-2", "numeric", "µM", sig=3),
                field("inhibition-constant", "Estimate the inhibition constant using the simple competitive model and supplied inhibitor concentration.", "biochemistry-lab-01-objective-2", "numeric", "µM", sig=3),
            ),
            question(
                "case-04",
                "Interpret the fitted parameter pattern without treating a model fit as a molecular structure determination.",
                field("mode-diagnosis", "Which simple inhibition mode is consistent with an increased apparent Km and approximately unchanged Vmax?", "biochemistry-lab-01-objective-3", options=["Competitive inhibition.", "Pure noncompetitive inhibition.", "No inhibition is possible."]),
                field("fit-limitation", "Which limitation should be reported for a double-reciprocal estimate?", "biochemistry-lab-01-objective-3", options=["It can overweight low-rate points and should be compared with the data range and assay quality.", "It guarantees an unbiased estimate from any number of points.", "It removes the need for replicate observations."]),
            ),
            question(
                "case-05",
                "Use the assay context stated in the candidate instructions.",
                field("initial-rate-window", "Which condition best supports an initial-rate interpretation?", "biochemistry-lab-01-objective-3", options=["A linear early-time interval with little substrate depletion and product buildup.", "An endpoint after substantial substrate depletion.", "Rates measured at different temperatures without recording the change."]),
                field("replicate-unit", "What is the replicate unit in this dataset?", ["biochemistry-lab-01-objective-1", "biochemistry-lab-01-objective-3"], options=["The separately labeled replicate observation at a matched substrate and condition.", "Every time the same row is copied into a graph.", "Each concentration value, regardless of how measurements were obtained."]),
            ),
        ],
        "rate_data": True,
    },
    {
        "number": 5,
        "title": "Homework 5 review candidate: free energy, redox and nucleotide pathways",
        "weeks": [8, 9],
        "purpose": (
            "This set links cellular thermodynamics and redox bookkeeping to nucleotide "
            "synthesis and the citric acid cycle. The dataset supplies model terms rather "
            "than real metabolite measurements. State the reaction and reference convention "
            "when calculating; standard-state free energy, actual free energy, equilibrium "
            "and pathway flux are distinct quantities."
        ),
        "items": [
            question(
                "case-01",
                "Use the standard free energy, reaction quotient and temperature in the dataset.",
                field("actual-dg", "Calculate actual ΔG using the stated relation between ΔG°, R, T and Q.", "biochemistry-6-objective-1", "numeric", "kJ/mol", sig=3),
                field("direction", "Which conclusion follows from the sign of the calculated ΔG under the stated condition?", "biochemistry-6-objective-1", options=["With positive ΔG, the reverse direction is favored under this condition; this does not specify a universal pathway flux.", "It directly specifies the reaction rate.", "It is independent of the metabolite concentrations."]),
            ),
            question(
                "case-02",
                "Use the supplied coupled standard free-energy terms and temperature.",
                field("coupled-dg0", "Calculate the net standard free-energy change for the stated coupled reaction.", "biochemistry-6-objective-2", "numeric", "kJ/mol", sig=3),
                field("equilibrium", "Relate the net standard free-energy value to the dimensionless equilibrium constant using the stated temperature.", "biochemistry-6-objective-2", "numeric", "", sig=3),
            ),
            question(
                "case-03",
                "Use the synthetic donor and acceptor reduction potentials in the CSV.",
                field("redox-free-energy", "Calculate ΔG from the stated electron count and potential difference.", "biochemistry-6-objective-3", "numeric", "kJ/mol", sig=3),
                field("electron-transport", "Where is the energy released in the stated electron-transfer chain?", "biochemistry-6-objective-3", options=["As electrons move from the donor to the more positive-potential acceptor.", "Only when ATP is hydrolyzed in the cytosol.", "At a site independent of redox potential."]),
            ),
            question(
                "case-04",
                "Compare the supplied pathway descriptions for purine and pyrimidine nucleotide construction.",
                field("ring-construction", "Which description distinguishes the two de novo pathway orders?", "biochemistry-nucleotide-objective-1", options=["Purine atoms are assembled onto a ribose-phosphate scaffold; the pyrimidine ring is built before attachment to the ribose-phosphate.", "Both rings are built only after attachment to ribose, by identical steps.", "Purines are salvaged from pyrimidines."]),
                field("branch-control", "At the IMP branch point, which type of input helps balance AMP and GMP production?", "biochemistry-nucleotide-objective-1", options=["Reciprocal energy-nucleotide use and end-product feedback.", "Only oxygen concentration.", "No branch regulation is possible."]),
            ),
            question(
                "case-05",
                "Use the pathway map in the lesson to connect salvage and deoxyribonucleotide synthesis.",
                field("salvage-purpose", "What does purine salvage do in the stated pathway framework?", "biochemistry-nucleotide-objective-2", options=["Reuses free purine bases with PRPP to regenerate nucleotides.", "Converts every nucleotide directly into glucose.", "Replaces all de novo synthesis in every tissue."]),
                field("dtmp-link", "Which linked process supplies the methylated pyrimidine nucleotide used in DNA?", "biochemistry-nucleotide-objective-2", options=["Folate-dependent dTMP formation from a deoxyuridine nucleotide.", "Oxidative decarboxylation of pyruvate.", "Glycogen phosphorylase."]),
            ),
            question(
                "case-06",
                "Track one acetyl-CoA through the citric acid cycle and distinguish it from electron transport.",
                field("tca-accounting", "Which set of outputs belongs to one cycle turn per acetyl-CoA in the standard accounting model?", "biochemistry-tca-cycle-objective-1", options=["Two CO₂ and reduced cofactors plus one nucleotide triphosphate equivalent.", "One glucose and six ATP directly.", "Oxygen consumption and water only."]),
                field("anaplerosis", "Why can withdrawal of a cycle intermediate alter flux even when acetyl-CoA supply is unchanged?", ["biochemistry-tca-cycle-objective-2", "biochemistry-3-objective-1", "biochemistry-3-objective-2"], options=["Intermediate pools support cycle capacity and biosynthetic branches; replenishment and redox demand affect flux.", "Every intermediate is a terminal waste product.", "Cycle flux is determined only by the amount of acetyl-CoA."]),
            ),
        ],
        "data": [
            ["case-01", "delta_g_standard", "8.0", "kJ/mol", "fictional reaction input"],
            ["case-01", "reaction_quotient", "0.10", "none", "stipulated concentration ratio"],
            ["case-01", "temperature", "298.15", "K", "model temperature"],
            ["case-01", "gas_constant", "0.008314", "kJ/(mol K)", "model constant"],
            ["case-02", "delta_g1_standard", "-18.0", "kJ/mol", "fictional coupled reaction term"],
            ["case-02", "delta_g2_atp_hydrolysis", "-30.5", "kJ/mol", "stipulated ATP-hydrolysis term"],
            ["case-02", "temperature", "298.15", "K", "model temperature"],
            ["case-03", "donor_potential", "-0.32", "V", "fictional standard reduction potential"],
            ["case-03", "acceptor_potential", "0.82", "V", "fictional standard reduction potential"],
            ["case-03", "electrons", "2", "mol electrons/mol reaction", "stipulated electron count"],
            ["case-03", "faraday_constant", "96.485", "kJ/(V mol)", "conversion constant"],
            ["case-04", "purine_intermediate", "IMP", "none", "fictionalized pathway label"],
            ["case-04", "pyrimidine_intermediate", "UMP", "none", "fictionalized pathway label"],
            ["case-05", "salvage_substrate", "free purine base plus PRPP", "none", "pathway substrate labels"],
            ["case-05", "dna_precursor", "dTMP", "none", "pathway product label"],
            ["case-06", "acetyl_coa_per_turn", "1", "mol", "standard cycle accounting basis"],
            ["case-06", "cycle_intermediate_withdrawal", "0.25", "mol", "fictional perturbation scale per model interval"],
            ["case-06", "cycle_intermediate_replenishment", "0.10", "mol", "fictional replenishment scale per model interval"],
        ],
    },
    {
        "number": 6,
        "title": "Homework 6 review candidate: glycolysis, energy charge and gluconeogenesis",
        "weeks": [10],
        "purpose": (
            "This set connects adenylate energy charge, glycolytic carbon and ATP accounting, "
            "phosphofructokinase regulation and gluconeogenic bypasses. Keep pools distinct "
            "from rates, and keep ATP molecules distinct from GTP and reducing equivalents. "
            "All values are synthetic model inputs; the tasks do not describe a living-cell experiment."
        ),
        "items": [
            question(
                "case-01",
                "Use the adenylate kinase equilibrium inputs supplied for the stated model.",
                field("amp", "Calculate AMP from the stated adenylate kinase relation and ATP/ADP concentrations.", "biochemistry-10-objective-1", "numeric", "mM", sig=3),
                field("energy-charge", "Calculate adenylate energy charge from ATP, ADP and AMP.", "biochemistry-10-objective-1", "numeric", "", sig=3),
            ),
            question(
                "case-02",
                "Use the specified glucose-to-lactate accounting boundary and ATP demand.",
                field("glycolytic-atp", "How many ATP equivalents per glucose are produced when one glucose is converted to two lactate molecules under the stated model? Enter a dimensionless number.", "biochemistry-10-objective-2", "numeric", "", sig=3),
                field("glucose-demand", "Calculate the glucose amount needed to meet the listed ATP demand using that net yield.", "biochemistry-10-objective-2", "numeric", "mmol", sig=3),
            ),
            question(
                "case-03",
                "Interpret the stipulated metabolite pool and flux observations.",
                field("pfk-control", "Which listed regulator pattern is consistent with allosteric control of phosphofructokinase?", "biochemistry-10-objective-3", options=["Energy charge and metabolite effectors can alter enzyme activity rapidly.", "A larger metabolite pool always means larger pathway flux.", "Flux can only change after new protein synthesis."]),
                field("pool-flux", "Which statement correctly separates a pool from a flux?", "biochemistry-10-objective-3", options=["A steady pool can coexist with changing throughput when input and output change together.", "A pool is a rate per time.", "A flux is the concentration measured at one instant."]),
            ),
            question(
                "case-04",
                "Use the stated pyruvate-to-glucose pathway accounting and count ATP, GTP and reducing equivalents separately.",
                field("gluconeogenic-cost", "Calculate the listed amount of ATP molecules, in mmol, for the stated pyruvate amount.", "biochemistry-gluconeogenesis-objective-1", "numeric", "mmol", sig=3),
                field("bypass", "Which reaction set captures the purpose of gluconeogenic bypasses?", "biochemistry-gluconeogenesis-objective-1", options=["Use distinct enzymes to bypass strongly exergonic glycolytic steps.", "Reverse every glycolytic step with the same enzyme.", "Convert acetyl-CoA directly into glucose."]),
            ),
            question(
                "case-05",
                "Compare the supplied glycolytic and gluconeogenic conditions and the listed carbon sources.",
                field("reciprocal-regulation", "Which regulatory pattern helps limit simultaneous high glycolytic and gluconeogenic flux?", "biochemistry-gluconeogenesis-objective-2", options=["Reciprocal regulation of opposing pathway steps.", "Activation of every step in both directions at once.", "Only changing the total ATP pool."]),
                field("carbon-source", "Which carbon-source conclusion is consistent with mammalian net-glucose accounting?", "biochemistry-gluconeogenesis-objective-2", options=["Propionate-derived carbon can contribute through a net-glucose intermediate; acetyl-CoA alone cannot.", "Even-chain fatty-acid acetyl-CoA yields net glucose without another carbon input.", "All amino-acid carbon is ketogenic."]),
            ),
        ],
        "data": [
            ["case-01", "ATP", "2.4", "mM", "synthetic adenylate pool input"],
            ["case-01", "ADP", "0.8", "mM", "synthetic adenylate pool input"],
            ["case-01", "adenylate_kinase_constant", "1.0", "none", "stipulated model constant"],
            ["case-02", "net_atp_per_glucose_to_lactate", "2", "mol/mol glucose", "explicit glycolytic accounting boundary"],
            ["case-02", "atp_demand", "18", "mmol ATP", "fictional cell demand over stated interval"],
            ["case-03", "amp_change", "small increase", "none", "fictional observation for pool-versus-flux discussion"],
            ["case-03", "flux_change", "twofold increase", "none", "fictional throughput observation with input and output matched"],
            ["case-04", "pyruvate_input", "4", "mmol", "fictional gluconeogenic substrate input"],
            ["case-04", "atp_per_glucose", "4", "mol ATP/mol glucose", "model entry for requested ATP-molecule count"],
            ["case-04", "gtp_per_glucose", "2", "mol GTP/mol glucose", "model entry"],
            ["case-04", "nadh_per_glucose", "2", "mol NADH/mol glucose", "model entry"],
            ["case-05", "propionate_entry", "succinyl-CoA", "none", "fictional carbon-source route"],
            ["case-05", "acetyl_coa_entry", "acetyl-CoA", "none", "carbon-accounting boundary"],
        ],
    },
    {
        "number": 7,
        "title": "Homework 7 review candidate: mitochondrial and fuel metabolism",
        "weeks": [11, 12],
        "purpose": (
            "This set integrates mitochondrial coupling, fatty-acid oxidation, ketone use, "
            "glycogen physiology, cholesterol feedback and lipoprotein transport. State the "
            "accounting convention for energetic estimates and distinguish tissue-specific "
            "pathway capability from a general statement about all cells. Dataset labels "
            "are fictional teaching inputs."
        ),
        "items": [
            question(
                "case-01",
                "Use the stated electrical and pH components of the proton-motive force.",
                field("pmf", "Calculate the combined proton-motive force from the listed electrical and pH components using the lesson convention.", "biochemistry-11-objective-1", "numeric", "mV", sig=3),
                field("glucose-atp", "Estimate ATP equivalents per glucose using the listed P/O ratios, carrier counts and substrate-level ATP under the stated accounting boundary. Enter a dimensionless number.", "biochemistry-11-objective-2", "numeric", "", sig=3),
            ),
            question(
                "case-02",
                "Use the course accounting assumptions for proton use and ATP/O ratios.",
                field("uncoupling", "Which change is expected when a proton leak increases while oxygen use continues?", "biochemistry-11-objective-3", options=["Less ATP is made per oxygen consumed under the stated coupling model.", "More ATP must be made per oxygen consumed.", "Oxygen consumption becomes mathematically zero."]),
                field("oxidation-cycle", "For an even-chain saturated fatty acyl-CoA, which relationship links chain length to beta-oxidation cycles and acetyl-CoA output?", "biochemistry-fatty-acid-objective-1", options=["Each cycle shortens the chain by two carbons, with final accounting depending on chain length.", "Each cycle adds two carbons.", "A saturated C16 chain produces one acetyl-CoA total."]),
            ),
            question(
                "case-03",
                "Use the stated carnitine-shuttle and oxidation context.",
                field("carnitine-control", "Which role is most consistent with the carnitine shuttle and malonyl-CoA regulation?", "biochemistry-fatty-acid-objective-2", options=["Long-chain acyl groups enter mitochondria through the shuttle, which is restrained by malonyl-CoA at CPT1.", "Carnitine is the terminal electron acceptor in the respiratory chain.", "Malonyl-CoA directly hydrolyzes fatty-acid acyl chains."]),
                field("oxidation-integration", "Which accounting boundary must be stated when estimating ATP from fatty-acid oxidation?", "biochemistry-fatty-acid-objective-2", options=["P/O assumptions and activation cost if starting with a free fatty acid.", "Only the number of carbon atoms.", "A fixed ATP yield independent of electron carriers."]),
            ),
            question(
                "case-04",
                "Compare the liver and extrahepatic pathways in the supplied fasting-state model.",
                field("ketone-formation", "Which condition pattern supports hepatic ketogenesis in the course model?", "biochemistry-ketone-objective-1", options=["High acetyl-CoA supply, mitochondrial redox state and gluconeogenic demand interact.", "Ketones form only when acetyl-CoA is absent.", "Ketogenesis is independent of mitochondrial redox."]),
                field("ketone-use", "Why does the liver export rather than oxidize the ketone bodies it produces in the standard pathway account?", "biochemistry-ketone-objective-2", options=["The liver lacks the key SCOT transferase step for ketolysis.", "The liver cannot form acetyl-CoA.", "Ketone bodies are not oxidizable by any tissue."]),
            ),
            question(
                "case-05",
                "Use the tissue labels and glycogen-state descriptions in the data.",
                field("glycogen-accounting", "Which statement correctly relates nucleotide cost to glycogen breakdown?", "biochemistry-glycogen-objective-1", options=["UDP-glucose incorporation uses a UTP equivalent per residue; phosphorylase releases glucose 1-phosphate and the debranching enzyme handles branch links.", "Glycogen synthesis has no nucleotide cost and phosphorylase removes every branch linkage.", "Each glycogen residue is directly released as free glucose by hexokinase."]),
                field("tissue-role", "Which distinction between liver and muscle glycogen is supported by the course model?", "biochemistry-glycogen-objective-2", options=["Liver glycogen supports blood-glucose maintenance; muscle glycogen primarily supports local use.", "Muscle glycogen is the main direct source of circulating glucose.", "Liver and muscle glycogen have identical systemic roles."]),
            ),
            question(
                "case-06",
                "Use the stipulated low-sterol response and lipoprotein route labels.",
                field("sterol-feedback", "Which response is expected when ER sterol is low in the course model?", "biochemistry-cholesterol-objective-1", options=["SREBP2 signaling increases HMG-CoA reductase and LDL-receptor expression.", "SREBP2 permanently blocks all cholesterol synthesis.", "LDL-receptor expression is unrelated to sterol state."]),
                field("lipoprotein-route", "Which apolipoprotein/enzyme relationship best matches dietary triacylglycerol delivery?", "biochemistry-cholesterol-objective-2", options=["ApoC-II activates capillary lipoprotein lipase on triglyceride-rich particles.", "ApoB-48 is the ligand for the LDL receptor in all routes.", "HDL carries dietary triacylglycerol from the intestine directly to adipose."]),
            ),
            question(
                "case-07",
                "A fictional perturbation changes substrate supply and hormonal signaling in two connected pathways.",
                field("control-layers", "Which regulatory layers can alter pathway activity on different time scales?", "biochemistry-4-objective-1", options=["Substrate supply, allostery, covalent modification and enzyme expression.", "Only gene expression at every time scale.", "Only substrate concentration with no enzyme regulation."]),
                field("connected-flux", "Why should a pathway perturbation be evaluated with connected fluxes rather than one metabolite pool alone?", "biochemistry-4-objective-2", options=["A pool can change without a proportional flux change, and connected pathways redistribute carbon and cofactors.", "Every metabolite pool equals its pathway flux.", "A single concentration proves the full causal chain."]),
            ),
        ],
        "data": [
            ["case-01", "delta_psi", "150", "mV", "matrix-negative potential expressed as a positive driving component"],
            ["case-01", "delta_pH", "0.8", "pH units", "matrix pH minus intermembrane-space pH"],
            ["case-01", "temperature", "310", "K", "model temperature"],
            ["case-01", "protons_per_atp", "4", "mol H+/mol ATP", "explicit accounting convention"],
            ["case-01", "protons_per_nadh", "10", "mol H+/mol NADH", "explicit accounting convention"],
            ["case-01", "protons_per_fadh2", "6", "mol H+/mol FADH2", "explicit accounting convention"],
            ["case-01", "p_o_nadh", "2.5", "mol ATP/mol NADH", "explicit model assumption"],
            ["case-01", "p_o_fadh2", "1.5", "mol ATP/mol FADH2", "explicit model assumption"],
            ["case-01", "glucose_nadh", "10", "mol NADH/mol glucose", "chosen textbook accounting convention"],
            ["case-01", "glucose_fadh2", "2", "mol FADH2/mol glucose", "chosen textbook accounting convention"],
            ["case-01", "substrate_level_atp", "4", "mol ATP/mol glucose", "chosen accounting convention"],
            ["case-02", "fatty_acyl_chain_length", "16", "carbons", "even-chain saturated model substrate"],
            ["case-02", "starting_form", "acyl-CoA", "none", "activation cost excluded in this item"],
            ["case-02", "malonyl_coa_state", "elevated", "none", "fictional regulation cue"],
            ["case-03", "fatty_acid_start", "free fatty acid", "none", "activation cost must be stated in an ATP estimate"],
            ["case-03", "carnitine_shuttle", "required for long-chain acyl groups", "none", "standard pathway label"],
            ["case-03", "malonyl_coa_effect", "CPT1 restraint", "none", "standard pathway label"],
            ["case-04", "hepatic_acetyl_coa", "elevated", "none", "fictional fasting-state context"],
            ["case-04", "hepatic_nadh_nad_ratio", "elevated", "none", "fictional redox context"],
            ["case-04", "scot_in_liver", "absent", "none", "standard human pathway teaching model"],
            ["case-05", "liver_glycogen_role", "blood glucose support", "none", "fictional summary label"],
            ["case-05", "muscle_glycogen_role", "local ATP supply", "none", "fictional summary label"],
            ["case-05", "branch_point_frequency", "12", "residues", "stipulated illustrative structural spacing"],
            ["case-06", "ER_sterol", "low", "none", "fictional regulatory state"],
            ["case-06", "dietary_particle", "chylomicron", "none", "fictional route label"],
            ["case-06", "apoCII", "activates LPL", "none", "standard pathway label"],
            ["case-07", "substrate_supply", "reduced", "none", "fictional perturbation"],
            ["case-07", "hormone_signal", "increased", "none", "fictional perturbation"],
        ],
    },
    {
        "number": 8,
        "title": "Homework 8 review candidate: biosynthesis, flux and metabolic perturbation",
        "weeks": [13, 14],
        "purpose": (
            "This cumulative set joins steady-state flux reasoning, regulatory time scales, "
            "pentose-phosphate output, fatty-acid and neutral-lipid synthesis, and interpretation "
            "of a metabolic perturbation. The data are synthetic and are not mass-balanced "
            "beyond the specific teaching relations stated. A single index or ratio is not a "
            "diagnosis or proof of a unique mechanism."
        ),
        "items": [
            question(
                "case-01",
                "Use the supplied two-step steady-state model and control coefficient.",
                field("pool-versus-flux", "Which pair of observations can coexist at steady state when input and output rates change together?", "biochemistry-12-objective-1", options=["The pool size stays similar while pathway throughput changes.", "A pool is always identical to a flux.", "A steady pool proves zero flux."]),
                field("control-coefficient", "Use the supplied small-change control coefficient to estimate the local fractional flux response to the stated enzyme change; report percent.", "biochemistry-12-objective-2", "numeric", "%", sig=3),
            ),
            question(
                "case-02",
                "Use the regulation time-scale inputs in the dataset.",
                field("regulatory-layer", "Which regulatory layer can change activity rapidly without waiting for new protein synthesis?", "biochemistry-12-objective-3", options=["Allosteric regulation or covalent modification.", "Only transcription and translation.", "Only protein degradation after a week."]),
                field("expression-time", "Calculate the stated first-order response time, in hours, to reach the supplied fraction of the new enzyme level.", "biochemistry-12-objective-3", "numeric", "h", sig=3),
            ),
            question(
                "case-03",
                "Use the oxidative and nonoxidative pentose-phosphate pathway data and stated carbon boundary.",
                field("nadph-output", "Calculate the amount of NADPH output, in mmol, from the listed oxidative-branch input.", "biochemistry-ppp-objective-1", "numeric", "mmol", sig=3),
                field("carbon-rearrangement", "Which statement describes the nonoxidative branch?", "biochemistry-ppp-objective-2", options=["Reversible carbon rearrangements connect pentoses with glycolytic intermediates.", "It produces ATP directly in every reaction.", "It irreversibly converts all pentoses to carbon dioxide."]),
            ),
            question(
                "case-04",
                "Use the explicit palmitate synthesis accounting convention and precursor values.",
                field("palmitate-requirements", "Calculate the amount of malonyl-CoA required, in mmol, for the stated palmitate synthesis amount.", "biochemistry-fatty-synthesis-objective-1", "numeric", "mmol", sig=3),
                field("nadph-boundary", "Which accounting statement is needed when reporting the ATP and NADPH cost?", "biochemistry-fatty-synthesis-objective-1", options=["State the carbon-source and shuttle boundary, plus the number of chain-extension and carboxylation steps counted.", "Treat all NADPH as ATP.", "Ignore the activation and precursor-supply assumptions."]),
            ),
            question(
                "case-05",
                "Trace the stipulated citrate-shuttle and acetyl-CoA carboxylase regulation.",
                field("citrate-shuttle", "What role does citrate export play in cytosolic fatty-acid synthesis?", "biochemistry-fatty-synthesis-objective-2", options=["It can supply cytosolic acetyl-CoA after citrate cleavage.", "It carries long-chain fatty acids directly into the mitochondrial matrix.", "It replaces NADPH in every reduction step."]),
                field("malonyl-control", "What is the pathway consequence of elevated malonyl-CoA in the stated model?", "biochemistry-fatty-synthesis-objective-2", options=["It supports fatty-acid synthesis and inhibits CPT1-mediated mitochondrial entry.", "It activates CPT1 and blocks synthesis.", "It is a direct product of beta-oxidation."]),
            ),
            question(
                "case-06",
                "Use the glycerolipid and tissue labels in the synthetic data.",
                field("neutral-lipid-path", "Which sequence leads from glycerol-3-phosphate toward stored triacylglycerol and its hepatic export route?", "biochemistry-neutral-lipid-objective-1", options=["Acylation to phosphatidic acid, then diacylglycerol, then triacylglycerol; liver can package TAG into VLDL.", "Direct conversion to cholesterol with no acylation or export.", "Beta-oxidation followed by glycogen synthesis."]),
                field("lipolysis-products", "Which statement distinguishes adipose intracellular lipolysis from capillary lipoprotein lipase?", "biochemistry-neutral-lipid-objective-2", options=["Adipose lipases mobilize stored triacylglycerol; capillary LPL hydrolyzes circulating lipoprotein triacylglycerol.", "They are the same enzyme in the same compartment.", "LPL releases glycerol only from stored intracellular droplets."]),
            ),
            question(
                "case-07",
                "A fictional respiratory-chain perturbation changes ATP demand, substrate uptake and lactate output.",
                field("glucose-demand", "Calculate glucose uptake, in mmol, needed for the listed ATP demand when oxidative phosphorylation is blocked and the stated glycolytic yield applies.", "biochemistry-13-objective-1", "numeric", "mmol", sig=3),
                field("lactate-output", "Calculate the lactate output, in mmol, under the stated glucose-to-lactate carbon balance.", "biochemistry-13-objective-1", "numeric", "mmol", sig=3),
            ),
            question(
                "case-08",
                "Interpret the paired redox and tracer summaries using only the measurement labels provided.",
                field("redox-ratio", "What can a changed lactate/pyruvate ratio support in this teaching model?", "biochemistry-13-objective-2", options=["A shift in the cytosolic redox-related signal under the stated assumptions, not a direct measurement of every pathway flux.", "An exact count of mitochondrial ATP synthase turns.", "Proof that glucose is the only carbon source."]),
                field("tracer-limit", "What does tracer labeling add to the interpretation?", "biochemistry-13-objective-2", options=["Evidence about carbon-source contribution and routing, within the tracer and model limits.", "A direct measurement of all enzyme concentrations.", "A guarantee that total carbon recovery is complete."]),
            ),
            question(
                "case-09",
                "Choose a follow-up measurement for a fictional oxidative-phosphorylation versus glycolytic defect.",
                field("discriminating-measurement", "Which measurement pair best separates a primary oxidative-phosphorylation impairment from a primary glycolytic defect?", "biochemistry-13-objective-3", options=["Compare oxygen consumption and ATP-linked responses with glucose uptake/lactate under matched conditions.", "Measure only total protein once.", "Repeat the same lactate measurement with no matched control."]),
                field("result-scope", "How should the follow-up result be reported?", "biochemistry-13-objective-3", options=["State what each measured result supports and what competing explanations remain.", "Treat one endpoint as proof of a unique molecular cause.", "Ignore assay timing and normalization."]),
            ),
        ],
        "data": [
            ["case-01", "control_coefficient", "0.40", "none", "fictional local coefficient for a small perturbation"],
            ["case-01", "enzyme_fractional_change", "10", "percent", "small-change approximation input"],
            ["case-01", "pool_before", "5", "mM", "fictional metabolite pool"],
            ["case-01", "input_before", "2", "mmol/min", "input balances output before the perturbation"],
            ["case-01", "output_before", "2", "mmol/min", "input balances output before the perturbation"],
            ["case-01", "input_after", "1", "mmol/min", "input balances output after the perturbation"],
            ["case-01", "output_after", "1", "mmol/min", "input balances output after the perturbation"],
            ["case-01", "pool_after", "5", "mM", "fictional steady pool"],
            ["case-01", "flux_before", "2", "mmol/min", "fictional throughput"],
            ["case-01", "flux_after", "1", "mmol/min", "fictional throughput"],
            ["case-02", "enzyme_amount_half_time", "4", "hours", "fictional first-order time constant label"],
            ["case-02", "fractional_response_target", "0.75", "none", "target fraction for a first-order response"],
            ["case-03", "glucose6phosphate_input", "12", "mmol", "fictional oxidative-branch input"],
            ["case-03", "nadph_per_g6p", "2", "mol/mol", "standard oxidative-branch accounting"],
            ["case-03", "co2_per_g6p", "1", "mol/mol", "standard oxidative-branch accounting"],
            ["case-03", "pentose_demand", "5", "mmol", "fictional biosynthetic demand"],
            ["case-04", "palmitate_target", "2", "mmol", "fictional target amount"],
            ["case-04", "malonyl_per_palmitate", "7", "mol/mol", "explicit synthesis accounting"],
            ["case-04", "nadph_per_palmitate", "14", "mol/mol", "explicit synthesis accounting"],
            ["case-04", "atp_per_malonyl", "1", "mol/mol", "carboxylation accounting"],
            ["case-05", "citrate_export", "increased", "none", "fictional precursor-supply state"],
            ["case-05", "acc_activity", "increased", "none", "fictional regulatory state"],
            ["case-05", "malonyl_coa", "elevated", "none", "fictional inhibitory signal"],
            ["case-06", "glycerolipid_intermediate", "phosphatidic acid to diacylglycerol", "none", "fictional pathway sequence label"],
            ["case-06", "adipose_lipase_sequence", "ATGL-HSL-MGL", "none", "intracellular storage mobilization label"],
            ["case-06", "capillary_lipase", "LPL", "none", "circulating lipoprotein processing label"],
            ["case-07", "atp_demand", "30", "mmol ATP", "fictional cell demand"],
            ["case-07", "net_atp_per_glucose", "2", "mol/mol", "explicit glycolytic-only boundary"],
            ["case-07", "lactate_per_glucose", "2", "mol/mol", "explicit carbon balance"],
            ["case-08", "lactate_pyruvate_ratio", "increased", "none", "fictional redox-associated signal"],
            ["case-08", "tracer_source", "[U-13C]glucose", "none", "fictional source label"],
            ["case-09", "oxygen_consumption", "decreased", "none", "fictional respiratory measurement"],
            ["case-09", "glucose_uptake", "increased", "none", "fictional uptake measurement"],
            ["case-09", "lactate", "increased", "none", "fictional output measurement"],
        ],
    },
]


def write_candidate(spec: dict, manifest: dict) -> None:
    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
    }
    scheduled = [
        week for week in manifest["duration"]["weeks"] if week["week"] in spec["weeks"]
    ]
    lesson_ids = [item for week in scheduled for item in week["lesson_ids"]]
    objective_ids = list(
        dict.fromkeys(
            objective
            for lesson_id in lesson_ids
            for objective in lessons[lesson_id]["objectives"]
        )
    )
    questions = []
    evidence = []
    choice_position = 0
    for item in spec["items"]:
        question_id = (
            f"biochemistry-homework-{spec['number']:02d}-candidate-v1:{item['id']}"
        )
        fields = []
        question_objectives = []
        for source in item["fields"]:
            question_objectives.extend(
                objective
                for objective in source["objective_ids"]
                if objective not in question_objectives
            )
            fields.append(
                {
                    "id": source["id"],
                    "type": source["type"],
                    "prompt": source["prompt"],
                    "options": source["options"],
                    "unit": source["unit"],
                    "points": 5,
                    "significant_figures": source["sig"],
                }
            )
            evidence.append(
                {
                    "question_id": question_id,
                    "field_id": source["id"],
                    "objective_ids": source["objective_ids"],
                    "points": 5,
                    "evidence_type": source["type"],
                }
            )
        for response_field in fields:
            if response_field["type"] != "single_choice":
                continue
            options = response_field["options"]
            if len(options) != 3:
                raise ValueError(
                    f"Homework {spec['number']} choice field needs exactly three options: "
                    f"{response_field['id']}"
                )
            target = choice_position % 3
            if target == 1:
                response_field["options"] = [options[1], options[0], options[2]]
            elif target == 2:
                response_field["options"] = [options[1], options[2], options[0]]
            choice_position += 1
        questions.append(
            {
                "id": question_id,
                "type": "structured",
                "prompt": item["prompt"],
                "options": [],
                "unit": None,
                "significant_figures": None,
                "points": 10,
                "selection": "single",
                "partial_credit_policy": None,
                "response_fields": fields,
                "graph_spec": None,
                "accepted_media_types": [],
                "max_upload_bytes": None,
                "variant_id": None,
                "variant_token": None,
                "learning_objective_ids": question_objectives,
                "assessment_role": "graded",
            }
        )
    mapped = {
        objective for item in questions for objective in item["learning_objective_ids"]
    }
    if mapped != set(objective_ids):
        raise ValueError(
            f"Homework {spec['number']} objective mismatch: "
            f"missing={set(objective_ids) - mapped}, extra={mapped - set(objective_ids)}"
        )
    outcomes = list(
        dict.fromkeys(
            outcome
            for objective in objective_ids
            for outcome in next(
                item
                for item in manifest["lesson_objectives"]
                if item["id"] == objective
            )["course_outcome_ids"]
        )
    )
    folder = COURSE / "assessment-specs"
    data_path = folder / f"homework-{spec['number']:02d}-candidate-data.csv"
    if spec.get("rate_data"):
        with data_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "case_id",
                    "condition",
                    "substrate_uM",
                    "replicate",
                    "initial_rate_umol_min",
                    "notes",
                    "inhibitor_concentration_uM",
                ]
            )
            observations = []
            for condition, vmax, km in (
                ("control", 100.0, 50.0),
                ("inhibitor", 100.0, 100.0),
            ):
                for substrate in (10, 20, 40, 80, 160):
                    for replicate, multiplier in ((1, 0.99), (2, 1.00), (3, 1.02)):
                        rate = vmax * substrate / (km + substrate) * multiplier
                        observations.append(
                            (condition, substrate, replicate, f"{rate:.6f}")
                        )
            for case_id, selected in (
                ("case-01", [row for row in observations if row[1] == 40]),
                ("case-02", [row for row in observations if row[0] == "control"]),
                ("case-03", observations),
                ("case-04", observations),
            ):
                for condition, substrate, replicate, rate in selected:
                        writer.writerow(
                            [
                                case_id,
                                condition,
                                substrate,
                                replicate,
                                rate,
                                "fictional replicate initial-rate observation; no real assay was performed",
                                "10" if case_id == "case-03" and condition == "inhibitor" else "",
                            ]
                        )
            writer.writerow(
                [
                    "case-05",
                    "assay context",
                    "",
                    "not applicable",
                    "",
                    "Synthetic observations only; no wet-lab timing or protocol supplied.",
                    "",
                ]
            )
    else:
        with data_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["case_id", "variable", "value", "unit", "notes"])
            writer.writerows(spec["data"])
    case_lines = []
    for index, item in enumerate(spec["items"], start=1):
        fields_text = " ".join(field["prompt"] for field in item["fields"])
        case_lines.append(f"{index}. {item['prompt']} {fields_text}")
    brief = (
        f"# {spec['title']}\n\n"
        f"**State: inactive answer-free review candidate.** This {len(questions)}-case, "
        f"{10 * len(questions)}-point draft covers proposed week(s) "
        f"{', '.join(map(str, spec['weeks']))}. It is not scheduled, assigned, submitted, "
        "graded or included in the course assessment policy. An unreviewed private key/grader "
        "draft is stored outside this public package; it is not approved or active. This public "
        "candidate does not define a due date, attempt rule or time estimate. Draft "
        "points are for blueprint discussion only.\n\n"
        "## Preparation and purpose\n\n"
        f"{spec['purpose']} Read the corresponding course lessons before attempting the "
        "cases. Every row and entity is fictional. Use only the values and assumptions "
        "stated in this brief, the attached data file and the relevant lesson. Keep units "
        "and denominators explicit. A result supports only the quantity or model requested; "
        "it does not establish a real enzyme mechanism, patient state, treatment choice or "
        "laboratory outcome. Structured response fields do not score free-text reasoning "
        "unless a later reviewed rubric explicitly says otherwise.\n\n"
        "## Dataset and response boundaries\n\n"
        "The accompanying UTF-8 CSV is the sole source of candidate-specific numeric "
        "observations. It uses case identifiers to associate rows with prompts and records "
        "the stipulated context. "
        f"{spec.get('dataset_note', '')}"
        "Units are part of the data, not decorative labels. The "
        "values are synthetic; repeated observations must not be described as independent "
        "biological replicates beyond their stated identifiers. Do not extrapolate beyond "
        "the model range or treat a teaching parameter as a measured biological constant. "
        "Unless a prompt says otherwise, report numeric answers to three significant figures "
        "and use the units requested in the structured response fields. "
        "These cases do not define deadlines, required course workload, grade weights, "
        "partial-credit rules or an approved assessment schedule.\n\n"
        "## Candidate cases\n\n"
        + "\n".join(case_lines)
        + "\n\n## Limits and review needed\n\n"
        "This draft is a prospective assessment blueprint, not a validated graded assignment. "
        "Before activation, the data and every numerical result need independent recalculation; "
        "the private key and grader need candidate-specific hash checks and mutation testing; "
        "a qualified biochemical reviewer "
        "and assessment-blueprint reviewer must examine the exact version; accessibility and "
        "fairness need review; workload must be measured after the required schedule is frozen; "
        "protected delivery must be verified for this candidate; and an operator must approve "
        "release and retake policy. The candidate remains outside the live manifest until all "
        "gates are resolved. No reviewer is identified or implied by this authoring.\n\n"
        "## Provenance\n\n"
        "Original answer-free authoring with synthetic teaching data, CC BY 4.0. No external "
        "assessment, real assay or third-party dataset was copied.\n"
    )
    instruction_path = folder / f"homework-{spec['number']:02d}-candidate.md"
    instruction_path.write_text(brief, encoding="utf-8")
    prerequisite_paths = sorted({lessons[lesson_id]["reading"] for lesson_id in lesson_ids})
    prerequisite_hashes = {
        relative: hashlib.sha256((COURSE / relative).read_bytes()).hexdigest()
        for relative in prerequisite_paths
    }
    candidate_id = f"biochemistry-homework-{spec['number']:02d}-candidate-v1"
    candidate = {
        "candidate_id": candidate_id,
        "course_id": "biochemistry",
        "content_version": VERSION,
        "state": "inactive-review-candidate",
        "title": spec["title"],
        "points": 10 * len(questions),
        "lesson_ids": lesson_ids,
        "objective_ids": objective_ids,
        "course_outcome_ids": outcomes,
        "objective_link_occurrences": sum(len(item["objective_ids"]) for item in evidence),
        "objective_evidence": evidence,
        "instruction_path": f"assessment-specs/homework-{spec['number']:02d}-candidate.md",
        "dataset_path": f"assessment-specs/homework-{spec['number']:02d}-candidate-data.csv",
        "prerequisite_sha256": prerequisite_hashes,
        "questions": questions,
        "review": {"status": "unreviewed", "reviewers": []},
        "activation_gates": GATES,
        "key_status": "An unreviewed private key/grader draft is stored outside the public package. It is not approved or active and requires candidate-specific hash checks, independent recalculation and mutation review.",
        "provenance": {
            "kind": "original",
            "license": "CC-BY-4.0",
            "ai_assistance": "Codex authored an answer-free draft; no independent or qualified review occurred.",
            "source_scope": "Existing course lessons and synthetic observations authored for this candidate; no external assessment or dataset was copied.",
        },
    }
    output = folder / f"homework-{spec['number']:02d}-candidate.json"
    output.write_text(json.dumps(candidate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"wrote homework {spec['number']:02d}: {len(questions)} cases, "
        f"{len(objective_ids)} objectives, {len(brief.split())} brief words"
    )


def main() -> None:
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    if manifest["version"] != VERSION:
        raise SystemExit(f"Expected Biochemistry {VERSION}, found {manifest['version']}")
    for spec in SPECS:
        write_candidate(spec, manifest)


if __name__ == "__main__":
    main()
