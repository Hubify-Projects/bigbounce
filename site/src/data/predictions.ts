export interface Prediction {
  slug: string;
  name: string;
  value: string;
  status: string;
  statusVariant: "green" | "blue" | "amber" | "red" | "purple";
  bestModel: string;
  experiment: string;
  timeline: string;
  description: string;
  currentConstraint: string;
  surveys: string[];
  papers: string[];
  keyResults: string[];
  nextSteps: string[];
}

export const predictions: Prediction[] = [
  {
    slug: "fnl",
    name: "Galaxy Bispectrum f_NL",
    value: "f_NL = -35/8 = -4.375",
    status: "FLAGSHIP",
    statusVariant: "purple",
    bestModel: "Matter bounce (all variants)",
    experiment: "SPHEREx (~2028)",
    timeline: "σ ≈ 0.7-1.0 from SPHEREx. Currently σ ≈ 4.1 combined.",
    description: "The decisive bounce-vs-inflation discriminator. The matter bounce predicts f_NL = -35/8 = -4.375, parameter-free and mechanism-independent across all matter bounce variants. Inflation predicts |f_NL| < 1. One measurement settles the question.",
    currentConstraint: "σ(f_NL) ≈ 4.1 (Planck + DESI combined). Our multi-tracer improvement: 6.1% (DESI), 16.4% (DESI+SDSS). SPHEREx forecast: 4.38σ detection if f_NL = -4.375.",
    surveys: ["DESI DR1 (9.5% f_NL improvement)", "SDSS DR18 (2nd tracer)", "LAMOST DR10 (3rd tracer pending)"],
    papers: ["Paper 2 — primary prediction paper", "Paper 3 — multi-tracer improvement"],
    keyResults: [
      "f_NL = -35/8 verified across 3 bounce models (mechanism-independent)",
      "Current Planck alone: σ ≈ 5.1, f_NL = -0.9 ± 5.1",
      "Combined Planck + DESI: σ ≈ 4.1 (our -4.375 at ~1.1σ)",
      "Multi-tracer improvement: 6.1% from AI-purified DESI anomaly tracers",
      "SPHEREx (~2028) will measure to σ ≈ 0.7-1.0 → 4.4-6.3σ detection",
      "Triple role: galaxy bispectrum + PBH abundance regulator + induced GW shape",
    ],
    nextSteps: [
      "Pipeline 1 Steps 2-6: bias validation (REQUIRED), classify, re-measure σ(f_NL)",
      "Add LAMOST as 3rd tracer population",
      "Score threshold sensitivity sweep",
      "BOSS/eBOSS DR16 for independent tracers",
      "VLASS radio (highest-bias tracers, b~2.5-3)",
    ],
  },
  {
    slug: "birefringence",
    name: "ALP Birefringence",
    value: "β = 0.27°",
    status: "Supporting",
    statusVariant: "amber",
    bestModel: "ECH (ALP field evolution)",
    experiment: "LiteBIRD (~2032)",
    timeline: "LiteBIRD will test at ~9σ. Current: 3.6σ observed signal.",
    description: "Axion-like particle field evolution through the bounce predicts a specific CMB polarization rotation angle β = 0.27°. The observed Eskilt 2023 combined measurement is β = 0.342° ± 0.094° (3.6σ) — consistent at 0.8σ.",
    currentConstraint: "Observed: β = 0.342° ± 0.094° (3.6σ, Planck+WMAP combined). Our prediction: 0.27°. Consistent at 0.8σ. ACT H200 measurement: β = 17.4° ± 12.1° (systematic-dominated — needs NaMaster).",
    surveys: ["Planck CMB (patch anomalies)", "ACT DR6 (needs NaMaster re-run)"],
    papers: ["Paper 1 — prediction derivation", "Paper 3 — ACT measurement attempt"],
    keyResults: [
      "ALP prediction β = 0.27° from field evolution through bounce",
      "Matches 3.6σ observed signal (0.342° ± 0.094°) at 0.8σ",
      "ACT H200 measurement dominated by foreground systematics",
      "Birefringence simulation validated: injected 0.27°, recovered 0.261° ± 0.037°",
    ],
    nextSteps: [
      "ACT re-run with NaMaster + galactic mask + multipole estimator",
      "Cross-frequency decorrelation for foreground removal",
      "Planck EB cross-spectrum independent measurement",
      "Wait for LiteBIRD (~2032) for definitive ~9σ test",
    ],
  },
  {
    slug: "nanograv",
    name: "NANOGrav GW Background",
    value: "γ = 3.0",
    status: "1σ consistent",
    statusVariant: "green",
    bestModel: "Matter bounce (induced GWs)",
    experiment: "NANOGrav / PTA (NOW)",
    timeline: "Current measurement. More data arriving from EPTA, PPTA, IPTA.",
    description: "The matter bounce predicts an induced gravitational wave spectral index γ = 3.0 from primordial perturbation growth during contraction. NANOGrav 15yr measures γ = 3.2 ± 0.6 — just 0.33σ away.",
    currentConstraint: "NANOGrav 15yr: γ = 3.20 ± 0.42. Bounce γ = 3.0 at 0.33σ. Bayesian: bounce preferred 5.6:1 over SMBH, 3.2:1 over cosmic strings.",
    surveys: ["NANOGrav 15yr (template fit complete)"],
    papers: ["Paper 1 — consistency check", "Paper 3 — Bayesian model comparison"],
    keyResults: [
      "Matter bounce γ = 3.0 vs observed 3.2 ± 0.6 (0.33σ)",
      "Bayesian model comparison: BIC favors bounce over SMBH at 5.6:1",
      "Bounce preferred over cosmic strings at 3.2:1",
      "PBH-induced GW spectrum consistent with observed amplitude",
    ],
    nextSteps: [
      "PTArcade proper noise-marginalized Bayesian analysis",
      "Include EPTA + PPTA + IPTA combined data",
      "Fit bounce-specific spectral templates (not just power-law)",
      "Compare matter bounce vs ekpyrotic vs inflation GW predictions",
    ],
  },
  {
    slug: "quintom",
    name: "Quintom w-Crossing",
    value: "w(z) crosses w = −1",
    status: "Theoretical (no in-house MCMC yet)",
    statusVariant: "amber",
    bestModel: "Quintom bounce",
    experiment: "DESI DR2 (external, 2.8–4.2σ)",
    timeline: "DESI DR2 (external groups) shows 2.8–4.2σ for w-crossing. Our independent MCMC has not yet been run.",
    description: "The quintom bounce unifies the bounce with dark energy through phantom fields. It predicts the dark energy equation of state w(z) crosses −1 (quintom-B behavior). The DESI DR2 BAO + supernova combination from external groups now reports w-crossing at 2.8–4.2σ, but this is treated theoretically in our program — we have not run a free-w0–wa MCMC ourselves.",
    currentConstraint: "Paper 1 §VII.H explicitly: zero free-w0–wa samples among the 309,789 frozen posterior samples. All quintom analysis in our papers is theoretical/discrimination-table only. External: DESI DR2 + Pantheon+ + DES SN5YR shows w-crossing at 2.8–4.2σ depending on the dataset combination (corrected fire #25).",
    surveys: [],
    papers: ["Paper 1 — quintom framework + discrimination table"],
    keyResults: [
      "Quintom bounce achieves bounce↔dark-energy unification that ECH cannot",
      "Discrimination table positions quintom vs matter bounce vs cuscuton vs ekpyrotic vs inflation",
      "External DESI DR2 (Adame et al.) shows 2.8–4.2σ w-crossing — independent of our program",
      "Earlier in-house claim P(quintom-B) = 98.6% (50.9K samples) was a bookkeeping confabulation from fire #21; corrected fire #25 — there are zero free-w0–wa samples in any of our chains",
    ],
    nextSteps: [
      "Stand up an actual quintom MCMC: add free w0, wa to the model and run on DESI DR2 BAO + Pantheon+ + DES SN5YR",
      "Add DES Y6 weak lensing once chains exist",
      "Compute quintom bounce f_NL (fill literature gap)",
      "Decide whether quintom belongs as Paper 5 or as a Paper 1 §VII.H expansion",
    ],
  },
];

export function getPredictionBySlug(slug: string): Prediction | undefined {
  return predictions.find((p) => p.slug === slug);
}
