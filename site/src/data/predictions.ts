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
    value: "f_NL = -35/16 = -2.1875",
    status: "P2 lead theory result",
    statusVariant: "purple",
    bestModel: "Matter-contraction scenario (conditional)",
    experiment: "SPHEREx (~2028)",
    timeline: "Prospective SPHEREx sensitivity is a conditional test; present constraints do not discriminate the scenario.",
    description: "P2 is the lead theoretical result: under its stated matter-contraction assumptions, it derives f_NL = -35/16 = -2.1875. A future non-Gaussianity measurement can test that conditional prediction; no current survey measurement establishes a bounce.",
    currentConstraint: "Current external constraints remain too broad to establish this prediction. Earlier DESI anomaly-tracer improvement estimates are legacy/superseded pipeline work, not a current flagship result. SPHEREx forecasts are conditional tests, not detections.",
    surveys: ["SPHEREx (future conditional test)", "Legacy DESI/SDSS/LAMOST pipeline records (not current evidence)"],
    papers: ["P2 — lead f_NL theory result", "P3 — Integrated Supporting Data Release · DESI Public-ID Recovery"],
    keyResults: [
      "P2 derives f_NL = -35/16 under its stated matter-contraction assumptions",
      "Existing external constraints do not discriminate this conditional value",
      "Legacy anomaly-tracer forecasts are preserved as superseded methodology, not current evidence",
      "SPHEREx sensitivity forecasts describe a prospective conditional test",
      "Possible links to PBH or gravitational-wave phenomenology remain theoretical",
    ],
    nextSteps: [
      "Maintain the P2 derivation and its stated assumptions",
      "Treat future SPHEREx analysis as a prospective conditional test",
      "Do not use legacy anomaly-pipeline candidate counts as bounce evidence",
    ],
  },
  {
    slug: "birefringence",
    name: "ALP Birefringence",
    value: "Conditional β model value",
    status: "Supporting theoretical context",
    statusVariant: "amber",
    bestModel: "ECH (ALP field evolution)",
    experiment: "LiteBIRD (~2032)",
    timeline: "Future CMB measurements may test model-dependent birefringence scenarios; they are not a bounce detection.",
    description: "A model-dependent ALP field-evolution calculation motivates a β value near 0.27°. Existing birefringence measurements have systematic and model-dependence questions and do not validate a bounce scenario.",
    currentConstraint: "Published CMB rotation estimates provide external context only. They are not an in-house validation of the β calculation or evidence that a bounce occurred.",
    surveys: ["Planck CMB (patch anomalies)", "ACT DR6 (needs NaMaster re-run)"],
    papers: ["P1A — boundary note", "P1B — namaster-proof research software"],
    keyResults: [
      "A model-dependent ALP calculation motivates β near 0.27°",
      "External birefringence estimates do not identify a bounce mechanism",
      "Foreground and estimator systematics remain material",
      "An injection-recovery exercise checks a pipeline response, not the physical model",
    ],
    nextSteps: [
      "ACT re-run with NaMaster + galactic mask + multipole estimator",
      "Cross-frequency decorrelation for foreground removal",
      "Planck EB cross-spectrum independent measurement",
      "Treat future LiteBIRD measurements as one constraint among model alternatives",
    ],
  },
  {
    slug: "nanograv",
    name: "NANOGrav GW Background",
    value: "γ = 3.0",
    status: "Legacy comparison",
    statusVariant: "amber",
    bestModel: "Legacy simplified slope comparison",
    experiment: "NANOGrav / PTA external context",
    timeline: "Historic model comparison retained as context; it is not a current program result or bounce detection.",
    description: "A historic simplified comparison placed a matter-bounce slope near an external free-spectrum estimate under specific modeling choices. It cannot identify the origin of the signal or establish a bounce.",
    currentConstraint: "External PTA measurements remain relevant context, but this legacy simplified comparison does not exclude astrophysical alternatives or select a bounce scenario.",
    surveys: ["NANOGrav 15yr free-spectrum HD-correlated KDE pack (Zenodo 8060824)"],
    papers: ["P1A — theoretical context", "P2 — lead f_NL theory result"],
    keyResults: [
      "Historic fitted values depend on the chosen simplified likelihood and model family",
      "This comparison does not exclude astrophysical alternatives",
      "Model choice and data representation materially affect inferred slopes",
      "Sampling diagnostics describe the historic computation, not physical confirmation",
      "PBH-induced gravitational-wave connections remain theoretical",
    ],
    nextSteps: [
      "Keep this as a legacy consistency comparison rather than a bounce-detection claim",
      "If revisited, preregister a multi-model comparison with independent validation",
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
    currentConstraint: "P1A's model-discrimination table records no in-house free-w0–wa analysis. P1B is namaster-proof research software, not an MCMC paper. Quintom discussion is theoretical context only; external DESI analyses do not establish a BigBounce result.",
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
