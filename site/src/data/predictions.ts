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
    currentConstraint: "σ(f_NL) ≈ 4.1 (Planck + DESI combined, external). Our DESI multi-tracer central forecast: 9.4% improvement (empirical α, consistent with no improvement at <1σ). SPHEREx forecast: 2.6–5σ conditional detection if f_NL = -4.375.",
    surveys: ["DESI DR1 (central 9.4% multi-tracer f_NL forecast)", "SDSS DR18 (2nd tracer)", "LAMOST DR10 (3rd tracer pending)"],
    papers: ["Paper 2 (f_NL forecast) — primary prediction paper", "Paper 3 (anomaly catalog) — multi-tracer improvement"],
    keyResults: [
      "f_NL = -35/8 derived across 3 bounce models (mechanism-independent, parameter-free)",
      "Current Planck alone: σ ≈ 5.1, f_NL = -0.9 ± 5.1",
      "Combined Planck + DESI: σ ≈ 4.1 (our -4.375 at ~1.1σ)",
      "Multi-tracer central forecast: 9.4% improvement from AI-purified DESI anomaly tracers (consistent with no improvement at <1σ)",
      "SPHEREx (~2028) will measure to σ ≈ 0.7-1.0 → 2.6-5σ conditional detection",
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
    timeline: "Wave 13 (2026-05-01): real KDE free-spectrum γ = 2.567 ± 0.382. Bounce 3.0 still consistent (-1.13σ); SMBHB excluded at -4.6σ.",
    description: "The matter bounce predicts an induced gravitational wave spectral index γ = 3.0 from primordial perturbation growth during contraction. The R42 Wave 13 emcee run on the real NANOGrav 15-yr HD-correlated KDE free-spectrum (Zenodo 8060824, 30 Fourier bins, 32 walkers × 10K production) recovers γ = 2.567 ± 0.382 — bounce 3.0 sits at -1.13σ, SMBHB γ = 4.33 is excluded at -4.6σ.",
    currentConstraint: "NANOGrav 15yr real-KDE free-spectrum: γ = 2.567 ± 0.382 (median 2.591, 68% CI [2.304, 2.882]); log10_A = -14.025 ± 0.380. Bounce γ = 3.0 consistent at -1.13σ. SMBHB γ = 4.33 excluded at -4.6σ. Supersedes the prior synthetic-power-law summary statistic γ = 3.20 ± 0.42; the real-vs-synthetic shift is -1.48σ. ESS = 5,507; autocorr τ ≈ 58; acceptance = 0.63.",
    surveys: ["NANOGrav 15yr free-spectrum HD-correlated KDE pack (Zenodo 8060824)"],
    papers: ["Paper 1 — consistency check", "Paper 3 — Bayesian model comparison"],
    keyResults: [
      "Wave 13 real-KDE: γ = 2.567 ± 0.382 (matter bounce 3.0 at -1.13σ)",
      "SMBHB γ = 4.33 excluded at -4.6σ (sharper than the synth-PL exclusion of ~2.7σ)",
      "Real-vs-synthetic shift: -1.48σ — substantive, not cosmetic",
      "Wave 13 emcee: 32 walkers × 10K production + 2.5K burn-in, ESS = 5,507, τ ≈ 58",
      "PBH-induced GW spectrum consistent with observed amplitude",
    ],
    nextSteps: [
      "Update Paper 3 §V.A with real-KDE γ + MCMC documentation appendix",
      "Add EPTA + PPTA + IPTA combined data for cross-PTA validation",
      "Fit bounce-specific spectral templates (not just power-law) on the real KDE",
      "R̂ Gelman-Rubin convergence check across the 32 walkers",
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
    currentConstraint: "Paper 1A's model-discrimination table is explicit: zero free-w0–wa samples among the 309,189 frozen posterior samples (Paper 1B). All quintom analysis in our papers is theoretical/discrimination-table only. External: DESI DR2 + Pantheon+ + DES SN5YR shows w-crossing at 2.8–4.2σ depending on the dataset combination.",
    surveys: [],
    papers: ["Paper 1A — quintom framework + model-discrimination table"],
    keyResults: [
      "Quintom bounce achieves bounce↔dark-energy unification that ECH cannot",
      "Discrimination table positions quintom vs matter bounce vs cuscuton vs ekpyrotic vs inflation",
      "External DESI DR2 (Adame et al.) shows 2.8–4.2σ w-crossing — independent of our program",
      "An earlier in-house claim of P(quintom-B) = 98.6% (50.9K samples) was traced to a bookkeeping error in an automated run and retracted — there are zero free-w0–wa samples in any of our chains",
    ],
    nextSteps: [
      "Stand up an actual quintom MCMC: add free w0, wa to the model and run on DESI DR2 BAO + Pantheon+ + DES SN5YR",
      "Add DES Y6 weak lensing once chains exist",
      "Compute quintom bounce f_NL (fill literature gap)",
      "Decide whether quintom belongs as its own paper or as a Paper 1A discrimination-table expansion",
    ],
  },
];

export function getPredictionBySlug(slug: string): Prediction | undefined {
  return predictions.find((p) => p.slug === slug);
}
