// AUTO-GENERATED from reproducibility/manifests/{programs,experiments}/*.json by
// site/scripts/sync-repro-manifests.mjs — do not edit by hand.
// Source of truth: reproducibility/manifests/ (directive Q2, repo CLAUDE.md;
// schema: reproducibility/manifests/SCHEMA.md).
// Regenerate this snapshot with: cd site && node scripts/sync-repro-manifests.mjs

export interface ReproInput {
  name: string;
  type?: "external-dataset" | "internal-artifact" | "model" | "none" | "external-literature" | string;
  locator: string | null;
  checksum?: string | null;
  license?: string | null;
  used_for?: string;
}

export interface ReproApi {
  name: string;
  endpoint: string;
  auth_required: boolean;
}

export interface ReproCode {
  path: string;
  entrypoint: string;
  sha256?: string | null;
}

export interface ReproEnvironment {
  python: string;
  hardware: string;
}

export interface ReproOriginalRun {
  venue: "local" | "runpod" | null;
  gpu: string | null;
  pod_id_or_host: string | null;
  date: string | null;
  wall_clock: string | null;
  actual_cost_usd: number | null;
}

export interface ReproReproduction {
  recommended_venue: string;
  est_wall_clock: string;
  est_cost_usd: number;
  parallelizable: boolean;
  resume_support: boolean;
  notes: string;
}

export interface ReproOutput {
  locator: string;
  type: "dataset" | "catalog" | "model" | "figure" | "result-json" | "receipt" | string;
  checksum?: string | null;
}

export type ReproStatus = "runnable-now" | "needs-data-restore" | "superseded" | "reproduced";

export interface ReproExperiment {
  manifest_version: string;
  id: string;
  title: string;
  program: "bounce-theory" | "anomaly-discovery" | "galaxy-chirality" | "lab-infra" | "track-a" | "track-b" | "track-c" | string;
  paper: "P1A" | "P1B" | "P1N" | "P2" | "P3-support" | "P4" | "P4P" | "P5" | "anomaly-flagship" | "anomaly-map" | "none" | string;
  kind:
    | "derivation"
    | "training"
    | "inference-scan"
    | "validation"
    | "crossmatch"
    | "mcmc"
    | "analysis"
    | "figure-generation"
    | "packaging"
    | string;
  inputs: ReproInput[];
  apis: ReproApi[];
  code: ReproCode[];
  environment: ReproEnvironment;
  original_run: ReproOriginalRun;
  reproduction: ReproReproduction;
  outputs: ReproOutput[];
  verification: string;
  status: ReproStatus;
  provenance: string[];
  open_items?: string[];
}

export interface ReproProgramPaper {
  paper: string;
  role: string;
  title: string;
}

export interface ReproDagEntry {
  id: string;
  depends_on: string[];
}

export interface ReproExternalData {
  name: string;
  link: string;
  kind: string;
  license: string | null;
}

export interface ReproFullReproduction {
  est_wall_clock: string;
  est_cost_usd: number;
  order: string;
}

export interface ReproHubify {
  lab_slug: string;
  module_notes: string;
}

export interface ReproProgram {
  manifest_version: string;
  id: string;
  title: string;
  question: string;
  papers: ReproProgramPaper[];
  experiments: ReproDagEntry[];
  external_data: ReproExternalData[];
  full_reproduction: ReproFullReproduction;
  hubify: ReproHubify;
}

export const reproPrograms: ReproProgram[] = [
  {
    "manifest_version": "bigbounce-program/v1",
    "id": "anomaly-discovery",
    "title": "DESI anomaly discovery",
    "question": "What unusual spectra emerge from a full-scale DESI anomaly search, and which candidates survive scientific validation?",
    "papers": [
      {
        "paper": "anomaly-flagship",
        "role": "lead",
        "title": "Rebuilt DESI anomaly-science flagship (future primary paper)"
      },
      {
        "paper": "P3-support",
        "role": "support",
        "title": "DESI Public-ID Recovery Catalog (supporting release)"
      }
    ],
    "experiments": [
      {
        "id": "anomaly-bigae-18m-inference-historical",
        "depends_on": []
      },
      {
        "id": "anomaly-silver-crossmatch",
        "depends_on": [
          "anomaly-bigae-18m-inference-historical"
        ]
      },
      {
        "id": "anomaly-uncataloged-taxonomy",
        "depends_on": [
          "anomaly-silver-crossmatch"
        ]
      },
      {
        "id": "anomaly-injection-recovery-test",
        "depends_on": [
          "anomaly-bigae-18m-inference-historical"
        ]
      },
      {
        "id": "anomaly-neowise-crossmatch",
        "depends_on": [
          "anomaly-silver-crossmatch"
        ]
      },
      {
        "id": "anomaly-gold-z6-qso-spectra",
        "depends_on": [
          "anomaly-uncataloged-taxonomy"
        ]
      },
      {
        "id": "anomaly-photoz-latent-vectors",
        "depends_on": [
          "anomaly-bigae-18m-inference-historical"
        ]
      },
      {
        "id": "anomaly-fnl-tracer-selection",
        "depends_on": []
      },
      {
        "id": "anomaly-clean-rerun-scan",
        "depends_on": []
      },
      {
        "id": "p3-dp3-15-heldout",
        "depends_on": []
      },
      {
        "id": "p3-positional-dedup",
        "depends_on": []
      },
      {
        "id": "p3-kfold-cv-gate",
        "depends_on": []
      },
      {
        "id": "p3-planck-heldout-membership",
        "depends_on": []
      },
      {
        "id": "p3-erosita-scaler-leakage-control",
        "depends_on": []
      },
      {
        "id": "p3-nanograv-pta-mcmc",
        "depends_on": []
      },
      {
        "id": "p3-multisurvey-summary-crossmatch",
        "depends_on": []
      },
      {
        "id": "p3-umap-multiseed-stability",
        "depends_on": [
          "p3-multisurvey-summary-crossmatch"
        ]
      }
    ],
    "external_data": [
      {
        "name": "DESI DR1 iron zcatalog (zall-pix-iron.fits)",
        "link": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "DESI DR1 (base release + coadd corpus)",
        "link": "https://data.desi.lbl.gov/public/dr1/",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "SPARCL (spectra retrieval API)",
        "link": "https://astrosparcl.datalab.noirlab.edu/sparc",
        "kind": "api",
        "license": null
      },
      {
        "name": "NEOWISE IR variability catalog (IRSA)",
        "link": "https://irsa.ipac.caltech.edu/Missions/wise.html",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "NANOGrav 15-yr dataset",
        "link": "https://data.nanograv.org/",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "bamfai/bigbounce-anomaly-catalog (HF)",
        "link": "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "GitHub mirror (Hubify-Projects/bigbounce)",
        "link": "https://github.com/Hubify-Projects/bigbounce",
        "kind": "code-mirror",
        "license": null
      },
      {
        "name": "P3 Zenodo archive",
        "link": "https://doi.org/10.5281/zenodo.21461888",
        "kind": "zenodo-archive",
        "license": null
      }
    ],
    "full_reproduction": {
      "est_wall_clock": "The completed AUG-011 scan ran about 45.5 hours on a RunPod A4000 and verified 36,634 shard receipts. Full independent reruns remain download-bound and multi-day; downstream sample selection, validation, taxonomy, and manuscript work are still pending because the full shard corpus is not in this checkout.",
      "est_cost_usd": 7.74,
      "order": "The scan is complete: retain its sealed result as a distinct generation, acquire its verified shard/receipt corpus through an authorized source, then derive a threshold from the observed distribution before sample selection. Do not tune toward historical counts. Historical BigAE/H200 legs remain comparison-only or needs-data-restore."
    },
    "hubify": {
      "lab_slug": "bigbounce",
      "module_notes": "AUG-011 is complete and receipt-verified (36,634 groups; 27,547,223 unique TARGETIDs; 52,188 at the sealed S>5 threshold). Its corpus is not present in this checkout and its named Hugging Face mirror returned unauthenticated/private 401, so Hubify must not present the completed corpus as anonymously forkable. Historical BigAE/H200 legs remain lineage, not live reproduction targets."
    }
  },
  {
    "manifest_version": "bigbounce-program/v1",
    "id": "bounce-theory",
    "title": "Bounce theory",
    "question": "Does matter-dominated contraction produce a distinctive, reproducible primordial non-Gaussian amplitude?",
    "papers": [
      {
        "paper": "P2",
        "role": "lead",
        "title": "f_NL forecast / exact matter-contraction non-Gaussianity (PRD)"
      },
      {
        "paper": "P1A",
        "role": "support",
        "title": "Algebraic Cartan elimination (CQG Note)"
      },
      {
        "paper": "P1B",
        "role": "support",
        "title": "namaster-proof: exact pseudo-Cl window inference and tamper-evident provenance (JORS)"
      }
    ],
    "experiments": [
      {
        "id": "p2-vertex-check",
        "depends_on": []
      },
      {
        "id": "p2-g1-gradient-transmission",
        "depends_on": [
          "p2-vertex-check"
        ]
      },
      {
        "id": "p2-g1-dressedmetric-transmission",
        "depends_on": [
          "p2-g1-gradient-transmission"
        ]
      },
      {
        "id": "p2-g3-torsion-fourfermion-bound",
        "depends_on": [
          "p2-vertex-check"
        ]
      },
      {
        "id": "p2-honest-negative-inin",
        "depends_on": []
      },
      {
        "id": "p2-channel-native-fisher",
        "depends_on": [
          "p2-vertex-check"
        ]
      },
      {
        "id": "p1a-mcmc-dneff",
        "depends_on": []
      },
      {
        "id": "p1a-namaster-500mc-birefringence",
        "depends_on": []
      },
      {
        "id": "p1a-ntot-sensitivity-mc",
        "depends_on": []
      },
      {
        "id": "p1a-alp-prior-predictive",
        "depends_on": []
      },
      {
        "id": "p1b-sn-overlap-control-chains",
        "depends_on": [
          "p1a-mcmc-dneff"
        ]
      },
      {
        "id": "p1b-namaster-window-regen",
        "depends_on": [
          "p1a-namaster-500mc-birefringence"
        ]
      }
    ],
    "external_data": [
      {
        "name": "Planck PR4/PR3 CMB likelihoods (via Cobaya)",
        "link": "https://cobaya.readthedocs.io/en/latest/likelihood_planck.html",
        "kind": "likelihood",
        "license": null
      },
      {
        "name": "BAO compilations (via Cobaya)",
        "link": "https://cobaya.readthedocs.io/en/latest/likelihood_bao.html",
        "kind": "likelihood",
        "license": null
      },
      {
        "name": "Pantheon+ supernova compilation",
        "link": "https://github.com/PantheonPlusSH0ES/DataRelease",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "DES-SN5YR supernova compilation",
        "link": "https://github.com/des-science/DES-SN5YR",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "Heinrich et al. 2023 SPHEREx forecast covariance (Cov_B) — NOT publicly released by original authors; DP2-26/DP2-29 gap",
        "link": "not-publicly-released",
        "kind": "covariance-matrix",
        "license": null
      },
      {
        "name": "P1A archive (algebraic Cartan elimination manuscript + data)",
        "link": "https://doi.org/10.5281/zenodo.21481838",
        "kind": "zenodo-archive",
        "license": "CC-BY-4.0"
      },
      {
        "name": "P1B namaster-proof software archive",
        "link": "https://doi.org/10.5281/zenodo.21481753",
        "kind": "zenodo-archive",
        "license": null
      },
      {
        "name": "P1B namaster-proof paper archive",
        "link": "https://doi.org/10.5281/zenodo.21481842",
        "kind": "zenodo-archive",
        "license": null
      }
    ],
    "full_reproduction": {
      "est_wall_clock": "~1-2 days sequential; dominated by the P1A delta-Neff MCMC (~12-18h to R-1<0.01) and the P1B SN-overlap control chains (several hours per chain pair). All 6 P2 derivation/analysis scripts are minutes-scale and independently parallelizable; the 500-MC NaMaster birefringence recovery (~1.5-2h) and NaMaster window regen (~5-15 min) can run alongside the MCMC legs.",
      "est_cost_usd": 10.3,
      "order": "Run the P2 algebra/derivation scripts first (free, minutes, no dependencies) to re-establish the f_NL^local=-35/16 baseline; then the two G1 transmission closures which build on it; then P1A's MCMC + NaMaster + N_tot + ALP legs in parallel (independent of each other and of P2); then P1B's SN-overlap and NaMaster-window legs, which reuse P1A's Cobaya/pymaster infrastructure. The channel-native Fisher surrogate is runnable-now but the true SPHEREx covariance closure remains external-data-gated."
    },
    "hubify": {
      "lab_slug": "bigbounce",
      "module_notes": "Program maps 1:1 to a Hubify lab research program; each experiment id becomes a reproducible run card. P1A/P1B Zenodo DOIs give Hubify a stable external mirror for the two support papers independent of this repo."
    }
  },
  {
    "manifest_version": "bigbounce-program/v1",
    "id": "galaxy-chirality",
    "title": "Galaxy chirality",
    "question": "Is there a large-scale observed-label chirality dipole in the released DESI imaging catalog?",
    "papers": [
      {
        "paper": "P4",
        "role": "lead",
        "title": "Galaxy Chirality Catalog (ApJS)"
      },
      {
        "paper": "P5",
        "role": "support",
        "title": "Environmental Dependence of Spiral Chirality (AJ)"
      }
    ],
    "experiments": [
      {
        "id": "p4-v2-vit-production-training",
        "depends_on": []
      },
      {
        "id": "p4-g1-vit-retrain-manifest",
        "depends_on": []
      },
      {
        "id": "p4-g1-ce-composition-assembly",
        "depends_on": [
          "p4-g1-vit-retrain-manifest"
        ]
      },
      {
        "id": "p4-g2-disjoint-validation",
        "depends_on": [
          "p4-g1-vit-retrain-manifest"
        ]
      },
      {
        "id": "p4-g3-joint-estimator-covariance",
        "depends_on": [
          "p4-g1-vit-retrain-manifest"
        ]
      },
      {
        "id": "p4-e2e-mirror-flip",
        "depends_on": [
          "p4-g1-vit-retrain-manifest"
        ]
      },
      {
        "id": "p4-g4-monopole-mechanism-injection",
        "depends_on": [
          "p4-e2e-mirror-flip"
        ]
      },
      {
        "id": "p4-a95-dipole-injection-limit",
        "depends_on": [
          "p4-e2e-mirror-flip"
        ]
      },
      {
        "id": "p4-c1-namaster-fsky-sweep",
        "depends_on": []
      },
      {
        "id": "p4-c2-nall-binomial-null",
        "depends_on": [
          "p4-e2e-mirror-flip"
        ]
      },
      {
        "id": "p4-c3-wp-invariance-fsky",
        "depends_on": [
          "p4-e2e-mirror-flip"
        ]
      },
      {
        "id": "p4-gz1only-retrain-dipole-null",
        "depends_on": []
      },
      {
        "id": "p4-dr8-axis-ratio-crossmatch",
        "depends_on": []
      },
      {
        "id": "p4-dipole-8m-fullcatalog",
        "depends_on": []
      },
      {
        "id": "p5-desi-dr1-crossmatch-build",
        "depends_on": [
          "p4-e2e-mirror-flip"
        ]
      },
      {
        "id": "p5-redshift-analysis",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      },
      {
        "id": "p5-density-analysis",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      },
      {
        "id": "p5-healpix-analysis",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      },
      {
        "id": "p5-systematics-analysis",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      },
      {
        "id": "p5-cosmic-web-desivast-void",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      },
      {
        "id": "p5-rconf-closures",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      },
      {
        "id": "p5-focal-cluster-robustness",
        "depends_on": [
          "p5-rconf-closures"
        ]
      },
      {
        "id": "p5-astra-crossmatch-hf-mirror",
        "depends_on": [
          "p5-desi-dr1-crossmatch-build"
        ]
      }
    ],
    "external_data": [
      {
        "name": "Smith42/galaxies (HF, galaxy image dataset)",
        "link": "https://huggingface.co/datasets/Smith42/galaxies",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "Galaxy Zoo 1 (GZ1) CW/CCW S3 labels",
        "link": "https://data.galaxyzoo.org/",
        "kind": "labels",
        "license": null
      },
      {
        "name": "CE-ResNet pre_desi.fits (Zenodo)",
        "link": "https://doi.org/10.5281/zenodo.7167388",
        "kind": "model-artifact",
        "license": null
      },
      {
        "name": "Galaxy Zoo DESI morphology predictions (Walmsley 2023)",
        "link": "https://data.galaxyzoo.org/",
        "kind": "labels",
        "license": null
      },
      {
        "name": "NOIRLab Astro Data Lab TAP (ls_dr8.tractor)",
        "link": "https://datalab.noirlab.edu/tap",
        "kind": "api",
        "license": null
      },
      {
        "name": "DESI DR1 (base release)",
        "link": "https://data.desi.lbl.gov/public/dr1/",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "DESI DR1 DESIVAST value-added catalog",
        "link": "https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "bamfai/galaxy-chirality-catalog (HF)",
        "link": "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "bamfai/galaxy-chirality-v2 (HF checkpoint)",
        "link": "https://huggingface.co/bamfai/galaxy-chirality-v2",
        "kind": "model",
        "license": null
      },
      {
        "name": "bamfai/astra-desi-edr-mirror (HF)",
        "link": "https://huggingface.co/datasets/bamfai/astra-desi-edr-mirror",
        "kind": "dataset",
        "license": null
      },
      {
        "name": "P4 Zenodo archive",
        "link": "https://doi.org/10.5281/zenodo.21461899",
        "kind": "zenodo-archive",
        "license": null
      }
    ],
    "full_reproduction": {
      "est_wall_clock": "~2-3 days sequential; dominated by the G1 ViT-Small retrain (~4h on RunPod A4000) and the e2e mirror-flip full-catalog inference (10.45h wall on RunPod A100, 16.9M inferences). The C1-C3 NaMaster null-test batch, G2/G3/G4 validations, and the A_95 dipole limit are each minutes-scale once the trained model and full-catalog inference exist and can run in parallel. P5's DESI crossmatch build (~hours, local CPU) gates its four downstream environment analyses plus the cosmic-web/DESIVAST and r-conf legs, which are independently parallelizable after that.",
      "est_cost_usd": 18,
      "order": "Rollup estimate, not a literal sum of individual experiment estimates (several P4 legs are needs-data-restore/superseded and are not part of the live reproduction path). Order: G1 retrain -> e2e mirror-flip full-catalog inference -> {G2, G3, G4, A_95, C1-C3 null tests} in parallel -> P5 DESI-DR1 crossmatch build -> {redshift, density, healpix, systematics, cosmic-web/DESIVAST, r-conf closures, astra mirror} in parallel, with focal-cluster robustness following r-conf closures."
    },
    "hubify": {
      "lab_slug": "bigbounce",
      "module_notes": "Program maps 1:1 to a Hubify lab research program. The e2e-mirror-flip experiment is the best-documented cost/venue/time run in the whole lab and is a good Hubify reference card for run-cost display; several historical H200-pod legs (v2 training, dipole-8M, DR8 crossmatch) are flagged superseded/needs-data-restore and should not be offered as live reproduction targets."
    }
  }
];

export const reproExperiments: ReproExperiment[] = [
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-pbh-abundance-fnl",
    "title": "Track A3 channel 2 — Press-Schechter PBH abundance with local quadratic non-Gaussianity at f_NL = -35/16 vs -35/8 vs 0",
    "program": "bounce-theory",
    "paper": "A3 (Track A3 portfolio paper)",
    "kind": "analysis",
    "inputs": [
      {
        "name": "none (analytic/numerical; no external data)",
        "type": "none",
        "locator": null,
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/pbh_abundance_fnl.py",
        "entrypoint": "python3 research/track_a3_multichannel/pbh_abundance_fnl.py",
        "sha256": "41305cae3ceea8be88cb975d006eee3ac6ab392d3db4115b49b9b409abe858f1"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + scipy 1.18.0 (repo requirements.txt subset)",
      "hardware": "cpu-only; Apple M5, 24 GB RAM, macOS 26.5 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (Apple M5)",
      "date": "2026-09-02",
      "wall_clock": "0.03 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "0.03 s (measured)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Pure numpy/scipy; sub-second. NOT a reproduction of Choudhury et al. 2025 arXiv:2409.18983 — that paper uses the compaction-function criterion, which this Press-Schechter quadratic-map calculation does not implement."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/pbh_abundance_fnl.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) the analytic ceiling -5/(12 f_NL) = 0.19048 at -35/16 and 0.09524 at -35/8, ratio exactly 2; (b) at zeta_c = 0.05 with sigma calibrated so the Gaussian case gives f_PBH = 1 (sigma* = 0.0063248), f_PBH = 7.32e-3 at -35/16 and 3.75e-6 at -35/8; (c) beta = 0 identically at zeta_c = 0.45 and 1.00 for both negative f_NL in the rare-tail regime.",
    "status": "reproduced",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3",
      "project-context/bounce_portfolio_strategy.md (Track C, Choudhury+ 2025)",
      "research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-pta-gamma-reproduction",
    "title": "Track A3 channel 1 — reproduction of the NANOGrav 15-yr free-spectrum gamma posterior and Savage-Dickey Bayes factors from the committed chain",
    "program": "bounce-theory",
    "paper": "A3 (Track A3 portfolio paper)",
    "kind": "analysis",
    "inputs": [
      {
        "name": "NANOGrav 15-yr HD-correlated free-spectrum emcee chain (320,000 samples)",
        "type": "internal-artifact",
        "locator": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy",
        "checksum": "sha256:50abc38a04e1bf886adc833b5eb653be4e986877fe2476f87a78927f4f3610fc"
      },
      {
        "name": "NANOGrav 15-yr KDE Free Spectra v1.0.0 (30f_fs{hd}_ceffyl) — upstream source of the chain",
        "type": "external-dataset",
        "locator": "https://doi.org/10.5281/zenodo.8060824",
        "checksum": null
      },
      {
        "name": "committed reference summaries for the diff",
        "type": "internal-artifact",
        "locator": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/{results.json,savage_dickey_2026-05-29.json}",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/pta_gamma_reproduce.py",
        "entrypoint": "python3 research/track_a3_multichannel/pta_gamma_reproduce.py",
        "sha256": "d515372eab1e4e6a042a555b6a93d679ec7824d8a1a2aa421fbc7265ad87d4b0"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + scipy 1.18.0 (repo requirements.txt subset)",
      "hardware": "cpu-only; Apple M5, 24 GB RAM, macOS 26.5 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (Apple M5)",
      "date": "2026-09-02",
      "wall_clock": "0.02 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "0.02 s (measured)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "No re-fit is performed; the emcee fit itself (pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py) requires the Zenodo KDE pack and emcee, and took 25 s of production sampling originally. Reproduction of the SUMMARIES needs only numpy+scipy and the committed chain."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/pta_gamma_reproduction.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Script asserts REPRODUCED=true: gamma mean/std match the committed results.json to 0 (exact), Savage-Dickey B_MB/free matches savage_dickey_2026-05-29.json to 3.1e-15 absolute, B_MB/SMBHB to 3.1e-11, z(SMBHB) exactly. Any drift beyond those tolerances means the chain or the KDE bandwidth rule changed.",
    "status": "reproduced",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3",
      "research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-survey-reach-fnl",
    "title": "Track A3 channel 3 — survey reach and current-constraint tension table for f_NL^local = -35/16",
    "program": "bounce-theory",
    "paper": "A3 (Track A3 portfolio paper)",
    "kind": "analysis",
    "inputs": [
      {
        "name": "published sigma(f_NL) forecasts and DESI DR1 measurement (literature values, quoted verbatim from abstracts)",
        "type": "external-literature",
        "locator": "arXiv:2311.13082 (SPHEREx sigma=0.7 bispectrum / 0.5 target); arXiv:1903.09208 (MegaMapper-class order unity); arXiv:1412.4872 (SPHEREx mission); arXiv:2106.09713 (FishLSS); arXiv:2411.17623 (DESI DR1 f_NL^loc = -3.6 +9.0/-9.1)",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/survey_reach_fnl.py",
        "entrypoint": "python3 research/track_a3_multichannel/survey_reach_fnl.py",
        "sha256": "eda632fe3fd683825122ecdf12d1313db5b58cd74ea4028a09f979eddb8996cf"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + scipy 1.18.0 (repo requirements.txt subset)",
      "hardware": "cpu-only; Apple M5, 24 GB RAM, macOS 26.5 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (Apple M5)",
      "date": "2026-09-02",
      "wall_clock": "0.01 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "0.01 s (measured)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Arithmetic only. If any cited sigma is superseded upstream, update ROWS and re-run."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/survey_reach_fnl.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: SPHEREx bispectrum-only bare 3.13 sigma / r-projected 2.63 sigma; SPHEREx target bare 4.38 / projected 3.68; MegaMapper-class bare 2.19 / projected 1.84; DESI DR1 (merger-model) tension 0.16 sigma with |f_NL|/sigma = 0.24. Two rows are flagged ILLUSTRATIVE and must not be quoted as published forecasts.",
    "status": "reproduced",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3",
      "research/focused_paper_source_integration/02_full_draft.tex (P2, r = 0.84 shape overlap)",
      "research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-bigae-18m-inference-historical",
    "title": "BigAE enhanced 18M/22.5M-row DESI inference (historical, unreconciled)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "inference-scan",
    "inputs": [
      {
        "name": "best_model_47k.pt (archived BigAE checkpoint, 496->512->256->128)",
        "type": "model",
        "locator": "best_model_47k.pt",
        "checksum": "f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07",
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/scripts/enhanced_18M_inference.py",
        "entrypoint": "python3 enhanced_18M_inference.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, torch, astropy (fits I/O), urllib.request — see requirements.txt",
      "hardware": "gpu-24gb (historical run architecture; inference itself is a small 3.5MB BigAE, plausibly cpu-only at reduced throughput)"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": "historical pod, unlogged",
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "not recommended for reproduction — superseded by the clean_rerun campaign (see anomaly-clean-rerun-scan)",
      "est_wall_clock": "n/a",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "The 2026-08-04 restoration gate (project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md) found this run cannot be truthfully reconstructed: the claimed 46 enhanced Parquets are absent locally (surviving corpus ~2.35GB vs claimed ~16GB parent), the enhanced checkpoint's 23,798,995 spectra / 22,748,720 rows differs from the summary's 22,504,897 rows by 243,823, and no batch manifest or shard hashes bind either count to a specific run. The archived best_model_47k.pt checkpoint itself is preserved (4 byte-identical local copies, sha256 confirmed to match live HF revision 8100e0933242e5e74df912cb1414d922cd60596e) and its architecture matches the inference code, but no run manifest proves it produced this specific historical output. Primary blocker for this manifest is the failed restoration gate (missing Parquets + unbindable provenance); this experiment is also effectively superseded by the clean_rerun campaign (anomaly-clean-rerun-scan), which is the approved forward path (clean public-ID-first DESI rerun with immutable input/model/scaler/shard/schema/checkpoint/dedup receipts). Do not attempt to reproduce this historical run — reproduce clean_rerun instead."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped/catalog_summary.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "NOT independently verifiable as a reproduction target: the surviving catalog_summary.json (catalog_total=22,504,897; anomalies_score_gt5=249,905) cannot be checked against the 46 absent enhanced Parquets, and the enhanced checkpoint's own row counts (23,798,995 spectra / 22,748,720 rows) disagree with the summary by 243,823 rows with no batch manifest to reconcile them — there is no fresh-run tolerance test that can pass honestly for this historical artifact.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — BigAE enhanced 18M/22.5M-row DESI inference (historical, unreconciled) bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md §Restoration gate result — 2026-08-04"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-clean-rerun-scan",
    "title": "clean_rerun campaign (AUG-011) — completed sealed generation, 2026-08-07",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "inference-scan",
    "inputs": [
      {
        "name": "DESI DR1 iron zcatalog (zall-pix-iron.fits)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits",
        "checksum": "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b",
        "license": "DESI DR1 public data license"
      },
      {
        "name": "Full DESI DR1 iron healpix coadd corpus (streamed per-pixel, multi-TB, no fixed archive locator)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/healpix/ (streamed pixel-by-pixel by run_scan.py; each coadd deleted immediately after scoring, per RUNBOOK.md §0)",
        "checksum": null,
        "license": "DESI DR1 public data license"
      },
      {
        "name": "best_model_47k.pt (archived BigAE checkpoint, 496->512->256->128, reused input)",
        "type": "model",
        "locator": "best_model_47k.pt",
        "checksum": "f5266ba48f476bca2f1b12610e0e81322caaa955af70ab83f0b05bf763885f07",
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/derive_locator_inventory.py",
        "entrypoint": "python3 derive_locator_inventory.py derive --zcatalog zall-pix-iron.fits --output locator_inventory_draft.jsonl",
        "sha256": null
      },
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/build_calibration.py",
        "entrypoint": "python3 build_calibration.py --zcatalog zall-pix-iron.fits --manifest run-contract.json --model best_model_47k.pt --coadd-cache-dir <cache> --training-manifest-output training_manifest.json --validation-manifest-output validation_manifest.json --output calibration.json",
        "sha256": null
      },
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/run_scan.py",
        "entrypoint": "python3 run_scan.py --inventory locator_inventory.jsonl --contract run-contract.json --model best_model_47k.pt --shard-dir <shards> --receipt-dir <receipts> --checkpoint <ckpt> --coadd-cache-dir <cache>",
        "sha256": null
      },
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun_contract.py",
        "entrypoint": "python3 clean_rerun_contract.py build --model best_model_47k.pt --inference-code enhanced_18M_inference.py --input-manifest input_manifest.json --calibration calibration.json",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, torch, astropy — see requirements.txt; fail-closed contract scaffold in clean_rerun_contract.py (never modify per RUNBOOK.md)",
      "hardware": "gpu-a4000-16gb (RUNBOOK.md §0: 'A4000-class GPU or CPU-strong instance' — download-bound, not GPU-bound; inference itself is a small 3.5MB BigAE)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000",
      "pod_id_or_host": "tc291bka0r6fl3",
      "date": "2026-08-05T09:19:13Z",
      "wall_clock": "45.5h",
      "actual_cost_usd": 7.74
    },
    "reproduction": {
      "recommended_venue": "runpod (A4000-class GPU or CPU-strong instance, ~200GB volume)",
      "est_wall_clock": "Completed run recorded at 45.5h on RunPod A4000 tc291bka0r6fl3; no separate estimate remains for the sealed generation.",
      "est_cost_usd": 7.74,
      "parallelizable": true,
      "resume_support": true,
      "notes": "The AUG-011 clean rerun is complete and receipt-verified: 36,634/36,634 shard groups scored, 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate rows removed, and 52,188 candidates above the sealed anomaly_score>5.0 threshold. On 2026-08-26, all B2 shards/receipts were freshly fetched locally and receipt-verified; the fixed-ladder observed distribution then produced a 3,810-row anomaly_score>=8.0 characterization sample, whose Parquet SHA-256 is 00bf453e864a2fda93ef6d72cd351984c4b8f43975d9962b65d168901ee1b852. The sample, its full receipt-binding manifest, and parent summary were uploaded to the authenticated private rerun archive. Do not describe the corpus or selected sample as anonymously public or forkable from this repository. Remaining active work is enrichment, validation, taxonomy, external-catalog joins, public immutable archiving, and manuscript drafting."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/summary.json",
        "type": "result-json",
        "checksum": "cdf9938e5c284a567d85db0d1181124c5f75fe6469e112cad864dc6acde91cbd"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/comparison.json",
        "type": "result-json",
        "checksum": "2c35419d911797e220adcf23dac93e930f94897c825f2270aca51a894eed494e"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/calibration.json",
        "type": "result-json",
        "checksum": "65b35bd94a111409483c2aa352becc2939a7da6e1d207483c3a1d3edb0f658b4"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/training_manifest.json",
        "type": "receipt",
        "checksum": "3bde52d10f0a1c6ea70236c9f1ff5d12346dfbdb2815c24edc157811fa5777bd"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/validation_manifest.json",
        "type": "receipt",
        "checksum": "cfb9227cac001baa62a799a85547602fd77c77a09586f30bb0007f1d32f604e9"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/run-contract.json",
        "type": "receipt",
        "checksum": "4e303b0ba2379960486638535f00be87a4dd923c8a3207f784c7a5394cd3d0af"
      }
    ],
    "verification": "Full-scan verification passed: verify-receipts covered 36,634/36,634 groups, summarize-after-dedup produced 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate rows removed, and 52,188 candidates above anomaly_score>5.0. Output checksums are raw file SHA-256 values. Separately, run-contract.json's internal calibration_sha256 is the canonical JSON-payload SHA-256 25498638fd23bb0033960e8199608e890feacd9e0eb220b24b300efcc954eb2f, and summary.json's contract_sha256 is the canonical contract-payload SHA-256 6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf; those are semantic bindings, not file-byte hashes. The completed run is recorded in pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/{complete.log,summary.json,comparison.json}. On 2026-08-26 the full retained B2 shard/receipt corpus was freshly fetched locally and verified, then build_flagship_sample.py replayed the binding to produce the 3,810-row anomaly_score>=8.0 selected sample. This does not assert a fresh re-download of original multi-TB DESI coadds or a public data release.",
    "status": "runnable-now",
    "provenance": [
      "commit 0663e42cbb7e391b96053bd55d07ee500b22db92 (AUG-011 scan COMPLETE; wall ~45.5h on RunPod A4000 tc291bka0r6fl3 at $0.17/hr)",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/{complete.log,summary.json,comparison.json}",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — clean_rerun campaign (AUG-011) bullet",
      "pipelines/p1_highz_tracers/clean_rerun/RUNBOOK.md §0 (honest scale estimates)",
      "pipelines/p1_highz_tracers/clean_rerun_contract.py",
      "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/calibration.json and run-contract.json (created_utc 2026-08-05T09:19:13Z, stability_check.passed=true)",
      "2026-08-26 authenticated provider audit and local full receipt replay: B2 aug-011-clean-rerun/ contains 36,634 receipts and 36,634 shards, all freshly fetched and verified locally; the private rerun archive now also holds the derived S>=8 selected sample, its full receipt-binding manifest, and the bound summary. It remains a private preservation checkpoint rather than a complete public corpus",
      "project-context/ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md §Restoration gate result — 2026-08-04 (motivation for the clean rerun)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-fnl-tracer-selection",
    "title": "f_NL tracer selection / step4-6 bias validation + alpha empirical calibration (negative result)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/scripts/step4_bias_validation.py",
        "entrypoint": "python3 step4_bias_validation.py",
        "sha256": null
      },
      {
        "path": "pipelines/p1_highz_tracers/scripts/wave_14_vvv_alpha_empirical.py",
        "entrypoint": "python3 wave_14_vvv_alpha_empirical.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, pandas, scipy (spatial.cKDTree) — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "This is explicitly a NEGATIVE result per audit: the empirical alpha (tracer bias amplitude) is statistically consistent with zero — jackknife alpha_internal_jk=0.1936 +/- 0.650 in the committed alpha_empirical_results.json, well within 1-sigma of 0 against the fiducial alpha=0.15. Not a headline discovery; do not present this as a positive f_NL tracer-selection signal."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/fnl_tracer_selection/fnl_forecast.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/outputs/step6_alpha_empirical/alpha_empirical_results.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "The reproduction target is confirming alpha remains statistically consistent with 0 (jackknife alpha_internal_jk = 0.1936 +/- 0.650, i.e. within ~0.3-sigma of zero), not reproducing a positive detection — a re-run passes if the recomputed alpha_internal_jk stays within its own jackknife standard error of 0.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — f_NL tracer selection / step4-6 (bias validation, alpha empirical) bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-gold-z6-qso-spectra",
    "title": "Gold anomalies — z6 QSO spectra (12 DESI Redrock z>6 QSO candidates)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/scripts/download_z6_qso_spectra.py",
        "entrypoint": "python3 download_z6_qso_spectra.py",
        "sha256": null
      },
      {
        "path": "pipelines/p1_highz_tracers/scripts/replot_z6_spectra.py",
        "entrypoint": "python3 replot_z6_spectra.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, pandas, pyarrow, healpy — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes to low hours (DESI spectra download-bound)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Downloads + replots the 12 candidate spectra from DESI Redrock catalogs; the z>6 classifications carry no independent redshift validation, so reproduction should reproduce the candidate list and spectra, not be read as a confirmed-redshift catalog."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/gold_anomalies/spectra/z6_qsos_detailed.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the same 12 DESI Redrock z>6 QSO candidates are recovered (exact object-id set equality expected); note these candidates have no independent redshift validation, so verification is limited to candidate-selection reproducibility, not redshift confirmation.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — gold anomalies, z6 QSO spectra bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-injection-recovery-test",
    "title": "Injection recovery test (per-class completeness / false-positive rates)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/scripts/injection_recovery_test.py",
        "entrypoint": "python3 injection_recovery_test.py --n-per-class 200 --seed 42",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, scipy (signal, optimize.nnls), matplotlib — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "The CODE runs cleanly and is fully reproducible locally — what is flagged is the SCIENCE claim, not reproducibility. Per audit, the headline '0% FP / 10-1,377x enrichment' figure is contradicted/overstated and needs independent re-derivation before it can be cited as verified. Do not re-headline the 0%/10-1377x numbers from a fresh run without first completing that re-derivation."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/injection_recovery/false_positive_analysis.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/outputs/injection_recovery/injection_recovery_results.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Verification requires an independent re-derivation of the completeness/false-positive claim per the audit finding — do NOT treat the existing 0% FP / 10-1,377x enrichment figures in the committed JSON as verified facts; a reproduction is confirmed only when the re-derived per-class completeness and false-positive rates are recomputed from the injected-source recovery statistics and cross-checked, not by matching the existing headline numbers.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — injection recovery (per-class completeness/false-positive) bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-neowise-crossmatch",
    "title": "NEOWISE crossmatch (IR variability, 16/283 meet variability rule)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/neowise_crossmatch.py",
        "entrypoint": "python3 neowise_crossmatch.py",
        "sha256": null
      },
      {
        "path": "pipelines/p1_highz_tracers/neowise_crossmatch_silver.py",
        "entrypoint": "python3 neowise_crossmatch_silver.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, requests — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes to low hours (depends on external IRSA/NEOWISE query throughput)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Both the gold-tier and silver-tier NEOWISE crossmatch scripts are committed and runnable locally; result JSON is preserved."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/neowise_crossmatch/crossmatch_summary.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm 16/283 objects meet the IR-variability rule (exact count equality expected on a deterministic threshold pass over the same crossmatched sample).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — NEOWISE crossmatch (IR variability) bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md",
      "path correction: neowise_crossmatch.py and neowise_crossmatch_silver.py live directly under pipelines/p1_highz_tracers/, not under scripts/"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-photoz-latent-vectors",
    "title": "Photo-z from latent vectors (supervised MLP, sigma_NMAD=0.0279)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "training",
    "inputs": [
      {
        "name": "22.5M-row enhanced DESI catalog latent features (BigAE encoder output)",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/outputs/enhanced_18M_deduped/ (parent latent-feature Parquets absent locally — see anomaly-bigae-18m-inference-historical)",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/outputs/photo_z/train_photo_z.py",
        "entrypoint": "python3 train_photo_z.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, pandas, pyarrow, scikit-learn (MLPRegressor, HistGradientBoostingRegressor), matplotlib — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local (blocked pending data restore)",
      "est_wall_clock": "n/a until parent latent features are restored",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "This training run consumes latent feature vectors derived from the 22.5M-row enhanced-inference parent, which is the same absent-Parquet artifact flagged in anomaly-bigae-18m-inference-historical (46 enhanced Parquets missing locally, restoration gate FAILED 2026-08-04). The committed metrics.json (800k train / 200k test split, sigma_NMAD=0.0279) cannot be honestly re-derived until that parent is restored or a fresh clean_rerun-derived latent feature set is substituted."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/photo_z/metrics.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm sigma_NMAD=0.0279 on the same 800k train / 200k test split, within a small numeric tolerance (<=0.001 absolute) — currently blocked because the input latent-feature parent is absent locally.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — photo-z from latent vectors bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md §Restoration gate result — 2026-08-04"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-silver-crossmatch",
    "title": "Silver crossmatch (2,145-row SNR-filtered slice)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/scripts/silver_crossmatch.py",
        "entrypoint": "python3 silver_crossmatch.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pandas, numpy, requests, xml.etree.ElementTree — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes to low hours (depends on external crossmatch service throughput)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Result JSON is preserved and recountable per audit; the 2,145-row SNR-filtered slice can be re-derived locally without GPU."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/silver_crossmatch/silver_crossmatch_summary.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the silver-tier crossmatch summary reproduces the 2,145-row SNR-filtered slice count (exact row-count equality expected; no numeric tolerance needed for a deterministic filter pass).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — silver crossmatch (2,145-row SNR-filtered slice) bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-uncataloged-taxonomy",
    "title": "Uncataloged taxonomy (1,127 objects, 10 families)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/classify_uncataloged.py",
        "entrypoint": "python3 classify_uncataloged.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, pandas, pyarrow — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Recountable, described as the strongest candidate-science centerpiece per audit. The generating script (classify_uncataloged.py) lives alongside its own outputs rather than under scripts/ — the inventory's bare description did not name a script path, verified by directory listing."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/taxonomy_results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/taxonomy_summary.md",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the taxonomy classification reproduces 1,127 objects across 10 families (exact count equality expected on a deterministic classification pass over the same input catalog).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / Rebuilt DESI anomaly-science flagship — uncataloged taxonomy (1,127 objects, 10 families) bullet",
      "project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md",
      "path correction: inventory did not name a generating script; verified via directory listing that pipelines/p1_highz_tracers/outputs/uncataloged_taxonomy/classify_uncataloged.py is the generator (co-located with its own outputs, not under scripts/)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1a-alp-prior-predictive",
    "title": "ALP prior-predictive / spectator-conditioned prior-predictive",
    "program": "bounce-theory",
    "paper": "P1A",
    "kind": "mcmc",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "reproducibility/cosmology/alp_prior_predictive.py",
        "entrypoint": "python3 alp_prior_predictive.py",
        "sha256": null
      },
      {
        "path": "reproducibility/cosmology/alp_spectator_conditioned_prior_predictive.py",
        "entrypoint": "python3 alp_spectator_conditioned_prior_predictive.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Local CPU prior-predictive checks; no external data or GPU required."
    },
    "outputs": [
      {
        "locator": "reproducibility/cosmology/alp_prior_predictive_result.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "reproducibility/cosmology/alp_spectator_conditioned_prior_predictive_receipt.json",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm prior-predictive coverage statistics match the committed receipt to numeric tolerance (<1% relative).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P1A — ALP prior-predictive bullet"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1a-mcmc-dneff",
    "title": "MCMC full-tension / Planck+BAO+SN / third-combo chains (delta N_eff)",
    "program": "bounce-theory",
    "paper": "P1A",
    "kind": "mcmc",
    "inputs": [
      {
        "name": "Cobaya full-tension config",
        "type": "internal-artifact",
        "locator": "reproducibility/cosmology/cobaya_full_tension.yaml",
        "checksum": null
      },
      {
        "name": "Cobaya Planck+BAO+SN config",
        "type": "internal-artifact",
        "locator": "reproducibility/cosmology/cobaya_planck_bao_sn.yaml",
        "checksum": null
      },
      {
        "name": "Cobaya Planck config",
        "type": "internal-artifact",
        "locator": "reproducibility/cosmology/cobaya_planck.yaml",
        "checksum": null
      },
      {
        "name": "Cobaya Planck+BAO config",
        "type": "internal-artifact",
        "locator": "reproducibility/cosmology/cobaya_planck_bao.yaml",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "reproducibility/cosmology/cobaya_full_tension.yaml",
        "entrypoint": "cobaya-run cobaya_full_tension.yaml",
        "sha256": null
      },
      {
        "path": "reproducibility/cosmology/cobaya_planck_bao_sn.yaml",
        "entrypoint": "cobaya-run cobaya_planck_bao_sn.yaml",
        "sha256": null
      },
      {
        "path": "reproducibility/cosmology/cobaya_planck.yaml",
        "entrypoint": "cobaya-run cobaya_planck.yaml",
        "sha256": null
      },
      {
        "path": "reproducibility/cosmology/cobaya_planck_bao.yaml",
        "entrypoint": "cobaya-run cobaya_planck_bao.yaml",
        "sha256": null
      }
    ],
    "environment": {
      "python": "cobaya, numpy, scipy, astropy (see reproducibility/cosmology/)",
      "hardware": "cpu-32vcpu-64gb"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": null,
      "pod_id_or_host": "RunPod CPU5 Compute-Optimized, 32 vCPU/64GB (manifests/MANIFEST.md) — no GPU used",
      "date": "2026-03-11",
      "wall_clock": ">=15h wall-clock observed from hourly manifest snapshots 2026-03-11 02:00 to 17:00 UTC",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod (32-vCPU CPU-optimized instance)",
      "est_wall_clock": "12-18 hours to R-1<0.01 convergence",
      "est_cost_usd": 8,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Cobaya configs + covmats committed; dollar total was not explicitly logged in the original manifest, only the pod class — estimate based on typical CPU5-class RunPod hourly rate x observed wall-clock."
    },
    "outputs": [
      {
        "locator": "reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/full_tension/",
        "type": "dataset",
        "checksum": null
      },
      {
        "locator": "reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/planck_bao_sn/",
        "type": "dataset",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm sample counts (176,240 / 132,949 / ~114,992 = 424,181 total) and R-1<0.01 convergence; posterior means for delta N_eff within numeric tolerance (<0.02 absolute) of the committed chains.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P1A — MCMC bullet",
      "reproducibility/cosmology/paper1_clean_restart_sync/manifests/MANIFEST.md",
      "project-context/SSOT/paper-1/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1a-namaster-500mc-birefringence",
    "title": "500-MC NaMaster EB birefringence recovery (beta = 0.238 deg, SNR 20.3)",
    "program": "bounce-theory",
    "paper": "P1A",
    "kind": "mcmc",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "reproducibility/p1_namaster_500mc/scripts/physical_spectra.py",
        "entrypoint": "python3 physical_spectra.py (checkpoint/resume harness)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "reproducibility/p1_namaster_500mc/requirements.txt (pymaster, healpy, numpy)",
      "hardware": "cpu-strong (NaMaster MC is CPU-bound)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": null,
      "pod_id_or_host": "budget launcher (runpod_budget_launcher.py); C1 companion ran on pod 5i2td3deu3hojr (A4000, jobs CPU-bound, $0.17/hr)",
      "date": null,
      "wall_clock": "~1.3h ETA at NSIDE=512 (C1 companion figure, project-context/SSOT/compute-queue.md)",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod (CPU-bound instance, ~$0.17/hr class)",
      "est_wall_clock": "~1.5-2h for 500 MC realizations at nside=512, lmax=1024",
      "est_cost_usd": 0.3,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Checkpoint/resume harness supports partial-run recovery; zero-spend preflight contract (runpod_production_contract.json) documented but watchdog-deletion gates are open per inventory."
    },
    "outputs": [
      {
        "locator": "reproducibility/p1_namaster_500mc/results/summary.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run 500 MC realizations and confirm recovered beta=0.238 deg (input 0.27 deg) with SNR within numeric tolerance (+/-1 SNR unit) of 20.3, at f_sky=0.3226.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P1A — 500-MC NaMaster bullet",
      "project-context/SSOT/compute-queue.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1a-ntot-sensitivity-mc",
    "title": "100,000-sample N_tot sensitivity Monte Carlo (Spearman |rho_s|=0.996)",
    "program": "bounce-theory",
    "paper": "P1A",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/vacuum_scale_sensitivity_scan.py",
        "entrypoint": "python3 vacuum_scale_sensitivity_scan.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps) + scipy.stats",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes (100,000-sample Monte Carlo is CPU-light)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Path correction: the inventory cited 'research/sensitivity_scan/', which does not exist in the repo (verified via find + git log --all --diff-filter=A). The actual script implementing the described 100k-sample N_tot Monte Carlo with Spearman correlation is research/theory_audit/vacuum_scale_sensitivity_scan.py."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/ (console output; N_tot viable range [79,95], 2.2% of parameter space)",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run 100,000-sample Monte Carlo and confirm Spearman |rho_s|=0.996 on N_tot to numeric tolerance (+/-0.005), and viable-fraction 2.2% of parameter space.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P1A — N_tot sensitivity MC bullet (path corrected: inventory cites 'research/sensitivity_scan/', actual path is research/theory_audit/vacuum_scale_sensitivity_scan.py)",
      "project-context/SSOT/paper-1/status.md line 257 (Sensitivity scan table row) and line 275 (N_tot viable range)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1b-namaster-window-regen",
    "title": "NaMaster window regenerability check (pymaster 3.0)",
    "program": "bounce-theory",
    "paper": "P1B",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "packages/namaster-proof/examples/rebuild_workspace_check.py",
        "entrypoint": "python3 rebuild_workspace_check.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pymaster 3.0, healpy, numpy",
      "hardware": "cpu-only (ran on GPU pod but job itself is CPU-bound)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000",
      "pod_id_or_host": "580dgszgib3ti4 (shared with P4 G3 MASTER-leg session)",
      "date": "2026-07-18",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local or runpod (CPU-only, no GPU needed)",
      "est_wall_clock": "~5-15 minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Cost/time were bundled into the shared ~2.1h/$0.36 phase-2 pod session with P4 G3 (see p4-g3-joint-estimator-covariance); this check alone is CPU-light and runs fine locally at $0."
    },
    "outputs": [
      {
        "locator": "packages/namaster-proof/examples/rebuild_workspace_check_2026-07-18_podA4000.log",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm max|Delta| < 1e-10 against the regenerated NaMaster workspace (committed result: max|Delta|=9.926e-24, PASS).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P1B — NaMaster window regenerability bullet"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1b-sn-overlap-control-chains",
    "title": "SN-overlap control chains A (Pantheon+) / B (DES-SN5YR)",
    "program": "bounce-theory",
    "paper": "P1B",
    "kind": "mcmc",
    "inputs": [
      {
        "name": "Pantheon+ supernova compilation",
        "type": "external-dataset",
        "locator": "used via Cobaya likelihood cobaya_control_pantheonplus.yaml",
        "checksum": null
      },
      {
        "name": "DES-SN5YR supernova compilation",
        "type": "external-dataset",
        "locator": "used via Cobaya likelihood cobaya_control_desy5.yaml",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "reproducibility/cosmology/cobaya_control_pantheonplus.yaml",
        "entrypoint": "cobaya-run cobaya_control_pantheonplus.yaml",
        "sha256": null
      },
      {
        "path": "reproducibility/cosmology/cobaya_control_desy5.yaml",
        "entrypoint": "cobaya-run cobaya_control_desy5.yaml",
        "sha256": null
      }
    ],
    "environment": {
      "python": "cobaya, numpy, scipy, astropy",
      "hardware": "cpu-only (RTX A4000 pod used historically but job was CPU-bound)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000 (job itself CPU-bound)",
      "pod_id_or_host": "99srknm4s1cc3l (\"bigbounce-p1b-snctrl\"), EUR-IS-1, $0.17/hr, network volume bigbounce-paper1-canonical",
      "date": "2026-07-01",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod (A4000-class, $0.17/hr)",
      "est_wall_clock": "several hours per chain pair to R-1<0.01",
      "est_cost_usd": 2,
      "parallelizable": true,
      "resume_support": true,
      "notes": "RunPod balance was ~$7.86 at launch per queue notes but explicit dollar total for this run was not logged, only the $/hr rate; estimate assumes a few hours at $0.17/hr."
    },
    "outputs": [
      {
        "locator": "reproducibility/cosmology/w0wa_control_chains_result.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm Control A w0=-0.874+/-0.059 / wa=-0.530+/-0.241 and Control B w0=-0.787+/-0.063 / wa=-0.785+/-0.263 within numeric tolerance (+/-0.02 on each parameter).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P1B — SN-overlap control chains bullet",
      "project-context/SSOT/queue.md (RunPod balance note)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a2-bounce-fnl-transmission",
    "title": "Track A2: transmission coefficient of the matter-contraction f_NL through explicit nonsingular bounces (linear-transfer term, scheme-labeled)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "entrypoint": "python3 a2_transmission_linear.py",
        "sha256": "bea7758b952eb6cd7c77f624ba8d31557916df5b0614cc60e6d1278105c8fca0"
      },
      {
        "path": "research/cubic_bounce_transmission/a2_transmission_figures.py",
        "entrypoint": "python3 a2_transmission_figures.py",
        "sha256": "707cd5f7f5c7c2de1e1118023e7aff9e52820944891b43503b6bdf73383d2626"
      }
    ],
    "environment": {
      "python": "numpy 2.5.1, scipy 1.18.0, sympy 1.14.0, matplotlib 3.11.1 (repo requirements.txt)",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-02",
      "wall_clock": "1.5 s (a2_transmission_linear.py) + 4 s (a2_transmission_figures.py), measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 10 s total",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic (seed 20260902 set; no stochastic step is used). Run a2_transmission_linear.py first, then a2_transmission_figures.py which reads its JSON."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.log",
        "type": "run-log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/a2_transmission_summary.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md",
        "type": "brief",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm, in HEADLINE: T_fNL = 0.250000 (LQC / geometric dressed-metric prescription; analytic value exactly 1/4), 0.195501 (analytic non-LQC poly bounce), 0.165005 (Quintin+2015-type), and in F_fluid_scheme_contrast.SECOND_SCHEME_transmission T_fNL = 0.409155 (LQC background, effective-fluid scheme). Tolerance 1e-5 relative. Also confirm the analytic cross-checks in B_backgrounds (LQC: I_inf = pi/sqrt3, A = 1/12, rho_B = 1/2; poly: I_inf = pi*eta_b/4, rho_B = [pi/6+sqrt3/4]/(pi/2)) at <1e-6 relative, the fluid-scheme K ~ dcut^-0.4998, and that the direct ODE value matches the super-Hubble formula to <5e-3 over k*eta_B <= 0.03.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item #2 (ranked #1 in research/remaining_live_paths_audit/)",
      "extends research/cubic_bounce_transmission/ phases 1-3 (g1_gradient_transmission_scheme.py, g1_dressedmetric_transmission.py, g1_dressedmetric_ic_close.py)",
      "literature engaged: arXiv:1508.04141 (Quintin, Sherkatghanad, Cai & Brandenberger 2015), arXiv:1712.08148 (Agullo, Bolliet & Sreenath 2017), arXiv:1211.1354 / 1302.0254 (Agullo, Ashtekar & Nelson), arXiv:1206.2382 (Cai, Easson & Brandenberger 2012)",
      "brief: research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md"
    ],
    "open_items": [
      "Delta f_NL^bounce: the intrinsic cubic (in-in) contribution of the NEC-violating phase is NOT computed here; two published determinations (1508.04141, 1712.08148) find it ENHANCES non-Gaussianity and it is not bounded by the linear term computed here.",
      "AAN quantum-mass U(eta) for quasi-dust: no verifiable published closed form; not guessed.",
      "Hybrid-LQC scheme: not implemented (effective mass for quasi-dust not verifiable)."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-channel-native-fisher",
    "title": "Channel-native Fisher surrogate (c15) + covariance chain (c8-c15)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "CAMB theory spectra",
        "type": "internal-artifact",
        "locator": "generated via c13 script (CAMB Boltzmann code)",
        "checksum": null
      },
      {
        "name": "Heinrich et al. 2023 SPHEREx covariance (Cov_B)",
        "type": "external-dataset",
        "locator": "not publicly released by original authors — DP2-26/DP2-29 gap",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/focused_paper_source_integration/scripts/c8_fnl_running_fisher.py",
        "entrypoint": "python3 c8_fnl_running_fisher.py",
        "sha256": null
      },
      {
        "path": "research/focused_paper_source_integration/scripts/c15_channel_native_fisher.py",
        "entrypoint": "python3 c15_channel_native_fisher.py",
        "sha256": null
      },
      {
        "path": "research/focused_paper_source_integration/scripts/c10_joint_covariance_marginalization.py",
        "entrypoint": "python3 c10_joint_covariance_marginalization.py",
        "sha256": null
      },
      {
        "path": "research/focused_paper_source_integration/scripts/p2_joint_cov.py",
        "entrypoint": "python3 p2_joint_cov.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps) + CAMB",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": "hours-scale (CAMB calls, exact per-script wall-clock not logged)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "2-6 hours (CAMB-bound)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Surrogate chain is runnable-now on local CPU; the true survey covariance (Cov_B) is external-data-gated — Heinrich et al. 2023 SPHEREx covariance was never publicly released."
    },
    "outputs": [
      {
        "locator": "research/focused_paper_source_integration/scripts/outputs/c15_channel_native_fisher.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the nuisance ladder 3.5-sigma/3.1-sigma/2.3-sigma/0.4-sigma reproduces to numeric tolerance (<1% relative); true-covariance closure requires the gated Cov_B and is out of scope for this reproduction.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P2 — channel-native Fisher bullet",
      "DP2-26/DP2-29 gap tracking in project-context/SSOT/paper-2/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-fnl-second-method-deltaN",
    "title": "Independent second-method matter-contraction f_NL (separate-universe / nonlinear delta-N) — NEXT_SCIENCE_LEDGER #1",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Cai, Xue, Brandenberger & Zhang 2009",
        "locator": "https://arxiv.org/abs/0903.0631",
        "used_for": "Eqs. (14),(20),(21),(37),(39) — f_NL convention, printed shape function, published -35/8"
      },
      {
        "name": "Li, Quintin, Wang & Cai",
        "locator": "https://arxiv.org/abs/1612.02036",
        "used_for": "Eq. (5.1) f_NL^local = -165/16 + 65/(8 c_s^2) -> -35/16 at c_s=1"
      },
      {
        "name": "BigBounce Paper 2 manuscript",
        "locator": "research/focused_paper_source_integration/02_full_draft.tex",
        "used_for": "Appendix A four-vertex re-summation (-35/16) for the reconciliation table"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.py",
        "entrypoint": "python3 research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.py",
        "sha256": "033fa555994aefcf2e5c2a4d25eb93a90f45b5140e89c0be77a503d1e9d8d592"
      }
    ],
    "environment": {
      "python": "python3 with sympy 1.14.0 and mpmath 1.3.0 (both in repo requirements.txt)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-02",
      "wall_clock": "2.9 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 minute",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic: exact sympy rationals plus a 40-digit mpmath ODE cross-check. No external data download, no GPU, no network access required at run time (the arXiv sources were read once during authorship and their equations are transcribed into the script and the .md)."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.md",
        "type": "writeup",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required exact values: second_method.fnl_local_general_epsilon == '5*epsilon/8 - 35/8'; fnl_local_matter_epsilon_3_2 == '-55/16'; the mpmath cross-check must agree with -3.4375 to better than 1e-5 relative; cai_eq37_orbit_audit must give '-305/64' (6-permutation reading) and '-35/16' (distinct-monomial (5,2,2) reading). The script asserts its own O(u_i^2) ODE residual is exactly 0.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 1 (Independent second-method derivation of the matter-contraction f_NL)",
      "project-context/VISION.md route 1 (bounce vs inflation signatures — flagship line)",
      "directive R (vision governance: ledger item worked before review rounds)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-g1-dressedmetric-transmission",
    "title": "G1 dressed-metric (Wilson-Ewing) transmission closure (T_c(k)=1, |delta f_NL| <= 6.8e-8)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/g1_dressedmetric_transmission.py",
        "entrypoint": "python3 g1_dressedmetric_transmission.py",
        "sha256": null
      },
      {
        "path": "research/cubic_bounce_transmission/g1_dressedmetric_ic_close.py",
        "entrypoint": "python3 g1_dressedmetric_ic_close.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-07-17",
      "wall_clock": "seconds",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Deterministic closure computation; folded into paper v1.7.125 (commit e641cb1c)."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/g1_dressedmetric_transmission.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/g1_dressedmetric_ic_close.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm T_c(k)=1 and |delta f_NL| <= 6.8e-8 at k*eta_B=1e-2 (numeric tolerance <1e-9 absolute on delta f_NL).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P2 — G1 dressed-metric bullet",
      "commit e641cb1c (v1.7.125)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-g1-gradient-transmission",
    "title": "G1 gradient-transmission scheme-dependence (Phase 1, T_c ~ 1/dcut)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/g1_gradient_transmission_scheme.py",
        "entrypoint": "python3 g1_gradient_transmission_scheme.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-07-17",
      "wall_clock": "seconds-minutes (log timestamp 2026-07-17 13:47)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Deterministic local scheme-dependence scan; no GPU or external data required."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/g1_gradient_transmission_results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/g1_gradient_transmission_results.log",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff g1_gradient_transmission_results.json against the committed copy; scheme-dependence coefficient c ~ 1/dcut should match to numeric tolerance (<1e-6 relative).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P2 — G1 gradient-transmission bullet",
      "COMPUTE_CAMPAIGN_2026-07-17.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-g3-torsion-fourfermion-bound",
    "title": "G3 torsion four-fermion bound (Einstein-Cartan estimate)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.py",
        "entrypoint": "python3 g3_torsion_fourfermion_bound.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "sympy, numpy — requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": "seconds",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Sympy estimate; folded into paper v1.7.123 Eq. 5 (commit 275846c5)."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/g3_torsion_fourfermion_bound.log",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the bound coefficient matches paper Eq. 5 (v1.7.123, commit 275846c5) exactly.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P2 — G3 torsion bullet",
      "commit 275846c5 (v1.7.123)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-honest-negative-inin",
    "title": "Honest-negative in-in bounce attempts (pathz / pathz2, superseded)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/pathz_full_inin_bounce.py",
        "entrypoint": "python3 pathz_full_inin_bounce.py",
        "sha256": null
      },
      {
        "path": "research/cubic_bounce_transmission/pathz2_calibrated_inin.py",
        "entrypoint": "python3 pathz2_calibrated_inin.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-07-02",
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Historical-negative result kept as provenance; not re-run for the headline result. Runnable if a full in-in retest is ever wanted."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/pathz_results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/pathz2_results.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the negative-result structure is reproduced (no positive in-in bounce closure); this is a historical-negative artifact, not a headline claim.",
    "status": "superseded",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P2 — honest-negative in-in attempts bullet"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-vertex-check",
    "title": "Four-vertex f_NL^local = -35/16 amplitude derivation (P2 headline)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/focused_paper_source_integration/scripts/p2_vertex_check.py",
        "entrypoint": "python3 p2_vertex_check.py",
        "sha256": null
      },
      {
        "path": "research/focused_paper_source_integration/scripts/fig_4vertex_sum.py",
        "entrypoint": "python3 fig_4vertex_sum.py",
        "sha256": null
      },
      {
        "path": "research/focused_paper_source_integration/scripts/exact_shape_analysis.py",
        "entrypoint": "python3 exact_shape_analysis.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "sympy, numpy — pure symbolic algebra, no external deps beyond requirements.txt (repo root: numpy, scipy, astropy, sympy-adjacent research deps)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": "minutes",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Pure sympy symbolic algebra; quadruple-certified result, trivially reproducible on any machine."
    },
    "outputs": [
      {
        "locator": "research/focused_paper_source_integration/scripts/ (console output + LaTeX-ready coefficients)",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm symbolic output equals f_NL^local = -35/16, equilateral = -255/128 exactly (rational-number equality, not a numeric tolerance).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: bounce-theory / P2 — vertex-check bullet",
      "project-context/SSOT/paper-2/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-dp3-15-heldout",
    "title": "DP3-15 held-out re-inference (structural-ceiling demonstration)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "validation",
    "inputs": [
      {
        "name": "r42_phase2 5-seed BigAE ensemble checkpoints (496->128)",
        "type": "internal-artifact",
        "locator": "pipelines/p3_anomaly_engine/ (r42_phase2/bigae_seed{101,202,303,404,505}.pt, sha256-pinned in output JSON)",
        "checksum": null
      }
    ],
    "apis": [
      {
        "name": "SPARCL",
        "endpoint": "https://astrosparcl.datalab.noirlab.edu/sparc",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p3_anomaly_engine/dp3_15_heldout_reinference.py",
        "entrypoint": "python3 dp3_15_heldout_reinference.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, pandas, torch, sparclclient — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-07-12",
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "30-60 minutes (dominated by the live SPARCL re-pull of ~20,000 held-out spectra)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Explicitly logged as local CPU, $0, 0 GPU-hours per SSOT status.md line 63. Demonstrates the structural (not compute) ceiling: released DESI tid = 26,218 real TARGETIDs (13.4%) of 195,829 rows, only ~9.8% of those resolve in SPARCL, so ~1.3% of released rows are re-pullable — no GPU can recover the 86.6% hashed-tid majority."
    },
    "outputs": [
      {
        "locator": "pipelines/p3_anomaly_engine/outputs/dp3_15_heldout_reinference.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm (A) the recoverable-fraction bound of ~1.31% of released rows (est_recoverable_released_rows / released_rows) and (B) the 5-seed BigAE ensemble held-out MSE median of 0.2327 (native-scale, matches the committed reconciliation reference of 0.233) plus the injection-recovery gate (broad emission-spike recall 98.8% @5-sigma, spectral-break recall 100% @5-sigma) within a small numeric tolerance (<=0.01 absolute on the MSE median, <=2 percentage points on recall).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — DP3-15 held-out re-inference bullet",
      "project-context/SSOT/paper-3/status.md line 63 (DP3-15 COMPUTE NOTE — 2026-07-12: 'executed to its honest structural ceiling — fabrication-free, 0 GPU-hours, $0 RunPod')"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-erosita-scaler-leakage-control",
    "title": "eROSITA scaler-leakage bounded control (top-298 overlap 257/298, J=0.76)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "validation",
    "inputs": [
      {
        "name": "eROSITA DR1 feature table (930,203 sources, pod-side only)",
        "type": "internal-artifact",
        "locator": "not preserved in-repo — pod-side feature tables only, per inventory",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p3_anomaly_engine/erosita_scaler_refit.json",
        "entrypoint": "generating script not identified in current repo tree (grep -l \"erosita_scaler_refit\" over pipelines/p3_anomaly_engine/**/*.py found no match — the two closest candidates, erosita_membership_reproduce.py and r24conf_erosita_axis_sweep.py, write to differently-named output files: outputs/erosita_membership_reproduce.json and r24conf_erosita_axis_sweep.json respectively, not erosita_scaler_refit.json) — this JSON result file is the surviving artifact and is inspectable/re-analyzable as-is",
        "sha256": null
      }
    ],
    "environment": {
      "python": "unknown — generating script not identified; result JSON requires no code to inspect",
      "hardware": "unknown (930,203-source scaler-refit comparison implies at minimum cpu-heavy, plausibly gpu-24gb given the paired A/B retrain)"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-06-11",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod (pending generating-script recovery)",
      "est_wall_clock": "unknown until the generating script is recovered or rewritten from the committed result JSON's documented method",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "The eROSITA leg is inspectable/re-analyzable now (the result JSON documents its own method: identical seeds np/torch=42, only the scaler-fit population differs between run A (full-catalog scaler) and run B (train-split-only scaler)) — per the inventory's own verdict this leg is runnable-now. Caveat: the specific generating script was not identified in the current repo tree (see path-correction note below), so a from-scratch bit-for-bit RE-RUN is not currently executable without recovering or rewriting that script against the eROSITA feature table; the committed result JSON itself is the reproducible/inspectable artifact. The NEOWISE/Gaia scaler-refit extension of this same leakage-control method remains compute-gated and has NOT been run at all yet (separate open item from this eROSITA result) — do not conflate the two."
    },
    "outputs": [
      {
        "locator": "pipelines/p3_anomaly_engine/erosita_scaler_refit.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Confirm the committed result: top-298 overlap between run A (full-catalog scaler) and run B (train-split-only scaler) = 257/298 (Jaccard 0.7581), top-1%-union overlap 7,279 (Jaccard 0.6427), Spearman rank correlation over the full 930,203-source catalog = 0.9413 — a bit-for-bit fresh-run check additionally requires recovering/rewriting the generating script against the eROSITA feature table; absent that, verification is against the committed JSON's own internally-consistent numbers.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — eROSITA scaler-leakage bounded control bullet",
      "pipelines/p3_anomaly_engine/erosita_scaler_refit.json (leg='eROSITA (load-bearing; NEOWISE/Gaia remain queued — feature tables pod-side only)')",
      "path correction: grep -l \"erosita_scaler_refit\" across pipelines/p3_anomaly_engine/*.py and pipelines/p3_anomaly_engine/**/*.py found no generating script; erosita_membership_reproduce.py writes outputs/erosita_membership_reproduce.json and r24conf_erosita_axis_sweep.py writes r24conf_erosita_axis_sweep.json — neither writes erosita_scaler_refit.json — so the result JSON itself is used as code[].path per the directive's fallback rule",
      "project-context/SSOT/paper-3/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-kfold-cv-gate",
    "title": "DESI 5-fold cross-validation reproducibility gate (mean pairwise Jaccard 0.862)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p3_anomaly_engine/pathc_desi_kfold/train_desi_kfold.py",
        "entrypoint": "python3 train_desi_kfold.py --training-shards <shards> --output-dir outputs/desi_kfold --n-folds 5 --seed 20260420",
        "sha256": null
      },
      {
        "path": "pipelines/p3_anomaly_engine/pathc_desi_kfold/fetch_desi_47k_training.py",
        "entrypoint": "python3 fetch_desi_47k_training.py",
        "sha256": null
      },
      {
        "path": "pipelines/p3_anomaly_engine/pathc_desi_kfold/heldout_tail_preservation.py",
        "entrypoint": "python3 heldout_tail_preservation.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, torch — see requirements.txt",
      "hardware": "cpu-only (5-fold BigAE proxy training over 47,000-row pool)"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "1-3 hours (5-fold model training, 47,000-row pool)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Each of the 5 proxy models trains on 4 folds and scores the full 47,000-row pool; pairwise top-1% Jaccard measures fold-model ranking stability. This is a ranking-stability gate over the training pool, not a fully out-of-sample re-score of the released 195,829-row catalog (per held_out_rescore.py's own framing)."
    },
    "outputs": [
      {
        "locator": "pipelines/p3_anomaly_engine/pathc_desi_kfold/results/kfold_stability_summary.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p3_anomaly_engine/pathc_desi_kfold/results/training_summary.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p3_anomaly_engine/pathc_desi_kfold/results/scoring_summary.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm mean pairwise Jaccard >= 0.70 gate (committed value 0.8625) with 464/546 objects appearing in >=3 of 5 fold-model top-1% lists (consensus_fraction_of_union=0.8498), within a small numeric tolerance (<=0.02 absolute on mean Jaccard given training-seed variance).",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — DESI 5-fold cross-validation reproducibility gate bullet",
      "pipelines/p3_anomaly_engine/held_out_rescore.py (desi.source field cites kfold_stability_summary.json and reproduces mean_pairwise_jaccard=0.8625, gate_pass=true)",
      "project-context/SSOT/paper-3/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-multisurvey-summary-crossmatch",
    "title": "Multi-survey summary / crossmatch / spatial-clustering / score-distributions (8 surveys)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "crossmatch",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/h200_results/pod_backup_20260408_full/bulk_cross_match_all.py",
        "entrypoint": "python3 bulk_cross_match_all.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "requests, urllib — see requirements.txt (external per-survey archive queries)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": "H200 snapshot dir pod_backup_20260408_full (pod since rotated/exited)",
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local (script survives; per-survey raw output regeneration untested since the 2026-04-08 snapshot)",
      "est_wall_clock": "hours (8-survey crossmatch, external archive query throughput bound)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "The generating script (bulk_cross_match_all.py) survives in the H200 pod-backup snapshot directory even though status is needs-data-restore — most of the per-survey raw outputs it produced do NOT survive alongside it (only result JSONs from a subset of the ~30 h200_results/ subdirectories are preserved). Primary blocker is that this raw multi-survey crossmatch has not been regenerated from the surviving script since the 2026-04-08 pod snapshot, so current-state raw per-survey outputs (spatial clustering, score distributions) cannot be verified against a fresh run without first re-executing the script end to end."
    },
    "outputs": [
      {
        "locator": "pipelines/h200_results/pod_backup_20260408_full/",
        "type": "dataset",
        "checksum": null
      }
    ],
    "verification": "Re-run bulk_cross_match_all.py and confirm per-survey detection counts and spatial-clustering/score-distribution summaries reproduce the 2026-04-08 snapshot outputs within the same tolerances used for the 6-way dedup headline (p3-positional-dedup): exact integer-count equality on deterministic crossmatch passes per survey. Not yet re-verified against a fresh run.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — multi-survey summary / cross-match / spatial-clustering / score-distributions (8 surveys) bullet",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps, item 4 (dozens of historical H200-pod artifact directories with no accompanying $/hr or wall-clock manifest)",
      "project-context/SSOT/paper-3/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-nanograv-pta-mcmc",
    "title": "NANOGrav 15-yr free-spectrum PTA MCMC (real Zenodo KDE likelihood, emcee)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "mcmc",
    "inputs": [
      {
        "name": "NANOGrav 15-yr KDE Free Spectra v1.0.0 (30f_fs{hd}_ceffyl)",
        "type": "external-dataset",
        "locator": "https://zenodo.org/records/8060824",
        "checksum": null,
        "license": "NANOGrav 15-yr data release license"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py",
        "entrypoint": "python3 emcee_freespec.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, emcee — see requirements.txt",
      "hardware": "cpu-only (32 walkers, 30 frequency bins, production run completed in 24.97s wall per committed results.json)"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 minute (committed run reports production_seconds=24.97 for 32 walkers x 10,000 production + 2,500 burn-in)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "CONTENT CORRECTION vs the inventory bullet: the inventory's cited headline numbers (gamma=3.20+/-0.42, 192,000 samples = 32 walkers x 6,000 steps, DeltaBIC=7.0 from savage_dickey_2026-05-29.json) do NOT match the actual committed artifacts in this directory. The committed results.json for this exact script (emcee_freespec.py, real 30-bin Zenodo KDE likelihood) reports gamma mean=2.5665 +/- 0.3818 (median 2.5913), n_samples=320,000 (32 walkers x 10,000 production steps, plus 2,500 burn-in per the script docstring), and the committed savage_dickey_2026-05-29.json reports Savage-Dickey Bayes factors (B_matter_bounce_vs_free=3.228, log10_B_matter_bounce_vs_smbhb=3.854), not a Delta-BIC figure. The gamma=3.20+/-0.42 / DeltaBIC=7.0 figures instead belong to a DIFFERENT script, projects/nanograv/nanograv_improved_analysis.py (32 walkers x 6,000 steps, 134k post-burn samples, reconstructed from the published Agazie+2023 best-fit rather than the real Zenodo KDE likelihood — see project-context/SSOT/paper-3/status.md's Wave-14-RR note), which is outside this manifest's 17-id scope. Venue is genuinely ungated: no RunPod pod ID, GPU/CPU class, $/hr, or wall-clock is recorded anywhere in pipelines/p3_pta_mcmc/ (Top-5-gaps #2); the 24.97s committed production_seconds strongly suggests local CPU execution, but that inference is not itself logged evidence."
    },
    "outputs": [
      {
        "locator": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy",
        "type": "dataset",
        "checksum": null
      },
      {
        "locator": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/savage_dickey_2026-05-29.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the gamma posterior mean/std (2.5665 +/- 0.3818, median 2.5913) on the 320,000-sample chain (32 walkers x 10,000 production steps), within a small numeric tolerance (<=0.05 absolute on mean gamma given emcee stochasticity with a fixed seed), and confirm the Savage-Dickey Bayes factor B_matter_bounce_vs_free reproduces near 3.23 (log10_B_matter_bounce_vs_smbhb near 3.85) from savage_dickey_2026-05-29.json.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — NANOGrav 15-yr free-spectrum PTA MCMC bullet",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps, item 2 (no pod ID/GPU class/$/hr/wall-clock recorded)",
      "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/results.json and savage_dickey_2026-05-29.json (actual committed numbers used above; content correction vs the inventory's cited gamma=3.20/DeltaBIC=7.0 figures, which trace to the separate projects/nanograv/nanograv_improved_analysis.py script per project-context/SSOT/paper-3/status.md's Wave-14-RR note)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-planck-heldout-membership",
    "title": "Planck held-out membership test + native re-inference (partial, 48/200 vs 30 expected)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "validation",
    "inputs": [
      {
        "name": "best_cmb_native.pt (native CMB autoencoder checkpoint)",
        "type": "model",
        "locator": "not preserved locally or in HF release — resided on a now-EXITED pod",
        "checksum": null
      },
      {
        "name": "cmb_native_patches.npy (200k masked SMICA patch tensor)",
        "type": "internal-artifact",
        "locator": "not preserved locally or in HF release — resided on a now-EXITED pod",
        "checksum": null
      },
      {
        "name": "HF release Planck cross-transfer baseline (patch_idx < 20k only, not the native 200k rescore)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
        "checksum": null,
        "license": "cc-by-4.0"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p3_anomaly_engine/held_out_rescore.py",
        "entrypoint": "python3 held_out_rescore.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "no third-party deps beyond stdlib (json, math.comb, pathlib) for the membership-test half; full native re-inference would additionally require torch — see requirements.txt",
      "hardware": "cpu-only for the membership test; full native re-inference requirement unknown (blocked, never re-specified post pod exit)"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": "now-EXITED pod (native CMB checkpoint + patch tensor resided here; not in the HF release)",
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local (membership test only; full native re-inference blocked)",
      "est_wall_clock": "minutes for the membership test; full native re-inference is not schedulable until best_cmb_native.pt + cmb_native_patches.npy + cmb_native_all_scores.parquet are re-staged",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "The held-out membership test (48/200 top anomalies fall in the 15%-held-out split vs 30 expected under random, a 1.60x over-representation, binomial one-sided p=5.49e-04) is fully reproducible locally from committed inputs. The FULL native re-inference is BLOCKED: it needs best_cmb_native.pt, cmb_native_patches.npy, and cmb_native_all_scores.parquet, all of which live on a now-EXITED pod and are not in the HF release (bamfai/bigbounce-anomaly-catalog carries only the cross-transfer baseline at patch_idx < 20k). The one currently-running pod (bigbounce-c123-namaster) refused SSH (key mismatch) and hosts a different job, so this cannot be re-staged from any currently accessible source."
    },
    "outputs": [
      {
        "locator": "pipelines/p3_anomaly_engine/outputs/held_out_rescore_result.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run the membership-test half and confirm 48/200 top anomalies fall in the held-out split against an expected 30.0 under random assignment (1.60x over-representation, binomial one-sided p=5.49e-04), within exact integer-count equality on the same held-out split definition (val_frac=0.15, seed=42). Full native re-inference verification is not possible until the checkpoint/patch tensor are restored.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — Planck held-out membership test + native re-inference (partial) bullet",
      "pipelines/p3_anomaly_engine/outputs/held_out_rescore_result.json (planck.full_native_reinference.status='BLOCKED (pod-side data gone)')",
      "project-context/SSOT/paper-3/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-positional-dedup",
    "title": "6-way / 7-way / 8-way positional dedup (275,151 -> 269,317 unique, 2.12% collapse)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Per-object released survey catalogs (DESI DR1, SDSS DR18, eROSITA DR1, Planck CMB, Gaia DR3, NEOWISE)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
        "checksum": null,
        "license": "cc-by-4.0"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p3_anomaly_engine/scripts/reproduce_headline_dedup.py",
        "entrypoint": "python3 reproduce_headline_dedup.py",
        "sha256": null
      },
      {
        "path": "pipelines/p3_anomaly_engine/sixway_dedup.py",
        "entrypoint": "python3 sixway_dedup.py",
        "sha256": null
      },
      {
        "path": "pipelines/p3_anomaly_engine/pathc_positional_dedup.py",
        "entrypoint": "python3 pathc_positional_dedup.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, pandas, astropy (coordinates.SkyCoord, search_around_sky) — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-06-30",
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "reproduce_headline_dedup.py is the current headline reproduction entrypoint under scripts/; sixway_dedup.py and pathc_positional_dedup.py are the historical direct implementations it wraps/reproduces. All run locally with a 5.0 arcsec match radius and an 80-degree NEOWISE ecliptic-pole mask."
    },
    "outputs": [
      {
        "locator": "pipelines/p3_anomaly_engine/outputs/sixway_dedup_artifact.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p3_anomaly_engine/outputs/sixway_dedup_artifact.csv",
        "type": "catalog",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm total_survey_level_detections=275,151 collapses to n_unique_physical_objects=269,317 (n_collapsed_detections=5,834, a 2.12% collapse rate) — exact integer-count equality expected on a deterministic 5.0 arcsec positional crossmatch over the same six-survey input.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — 6-way / 7-way / 8-way positional dedup bullet",
      "project-context/SSOT/paper-3/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-umap-multiseed-stability",
    "title": "UMAP multi-seed stability (Pod 1 production)",
    "program": "anomaly-discovery",
    "paper": "P3-support",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/umap/",
        "entrypoint": "no generating script preserved in repo — historical result artifact only; full reproduction requires restoring the lost UMAP pipeline script from the pod1_namaster_umap production run",
        "sha256": null
      }
    ],
    "environment": {
      "python": "unknown — generating script not preserved; committed artifact is umap_stability.json only",
      "hardware": "unknown (implied H200 pod per directory naming convention pod1_namaster_umap_2026-04-29; no logged hardware spec in the artifact itself)"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "unknown — blocked until the UMAP pipeline script is restored",
      "est_wall_clock": "unknown",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "No .py script exists anywhere under pipelines/h200_results/pod1_namaster_umap_2026-04-29/ (verified via find — only the results/umap/umap_stability.json JSON and a sibling results/namaster/summary.json and results/namaster-birefringence/summary.json survive). The venue is only inferable from the directory name pattern ('pod1_namaster_umap_2026-04-29', implying an H200 pod), not from any $/hr or wall-clock receipt in the artifact itself — this is one of the ~28 sibling h200_results/ subdirectories flagged in the inventory's Top-5-gaps item 4. Full reproduction requires restoring the lost UMAP pipeline script from the original pod1_namaster_umap production run."
    },
    "outputs": [
      {
        "locator": "pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/umap/umap_stability.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Cannot currently define a fresh-run numeric tolerance test — no generating script survives to re-run. Verification is limited to inspecting the committed umap_stability.json for internal consistency until the pipeline script is restored.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: anomaly / P3 — UMAP multi-seed stability (Pod 1 production) bullet",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps, item 4 (dozens of historical H200-pod artifact directories with no accompanying $/hr or wall-clock manifest; venue inferable only from directory naming, not a receipt)",
      "project-context/SSOT/paper-3/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-a95-dipole-injection-limit",
    "title": "A_95^obs coverage-calibrated dipole injection upper limit",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.py",
        "entrypoint": "python3 a95_observed_label_upper_limit_v1_0_265.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, scipy — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": "597.7s (~10 min), logged exactly via a95_run.log",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "~10 minutes",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Best time-logged example in the repo (per inventory) — the reproduction estimate simply restates the exactly-logged original run time since it is already a clean receipt."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm A_95^obs = 0.98% (coverage-calibrated dipole injection upper limit) within the numeric tolerance stated in the result JSON.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — A_95^obs coverage-calibrated dipole injection upper limit bullet (\"best time-logged example\")",
      "project-context/SSOT/paper-4/status.md",
      "Path correction: the inventory names the log as `a95_run.log` without a directory; verified via `find` that the script, log, and output JSON all live in `pipelines/p2_chirality/analysis/`, not under `outputs/`."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-c1-namaster-fsky-sweep",
    "title": "C1 — NaMaster fsky sweep (part of the C1/C2/C3 monopole/dipole-null batch)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "h200_scripts/experiments/c1_p1b_namaster_fsky_sweep.py",
        "entrypoint": "python3 c1_p1b_namaster_fsky_sweep.py",
        "sha256": null
      },
      {
        "path": "h200_scripts/experiments/launch_c123_pod.sh",
        "entrypoint": "bash launch_c123_pod.sh",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pymaster, healpy, numpy — see requirements.txt",
      "hardware": "cpu-strong (12 vCPU/62GB — NaMaster MC jobs are CPU-bound despite running on a GPU-class pod)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000 (unused — job is CPU-bound NaMaster MC)",
      "pod_id_or_host": "5i2td3deu3hojr, $0.17/hr, 12 vCPU/62GB",
      "date": "2026-06-09",
      "wall_clock": "~71 min inferred (compute-queue.md logs pod-session start 2026-06-09 18:42; the committed output reproducibility/p1_namaster_500mc/results/c1_fsky_sweep.json carries a completion timestamp of 2026-06-09T19:53:31Z) — qualitative ETA quoted in compute-queue.md was ~1.3h at the time it was written while the job was still RUNNING",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod CPU-strong instance (12+ vCPU, no GPU required)",
      "est_wall_clock": "~1-1.5 hours for the 2x500 MC fsky sweep (fsky~0.85 and fsky~0.65)",
      "est_cost_usd": 0.2,
      "parallelizable": true,
      "resume_support": true,
      "notes": "The inventory's own compute-queue.md entry captured this job mid-run with only a qualitative ETA (~1.3h), not a completed-run receipt at write time; a completed output file was independently located at reproducibility/p1_namaster_500mc/results/c1_fsky_sweep.json with a real completion timestamp, so the wall-clock above is DERIVED from two real logged timestamps rather than invented. Note: despite being grouped in the inventory under the P4 C1/C2/C3 NaMaster batch (shared pod session with the genuinely P4-scoped C2/C3 nulls), this script's own content and compute-queue.md both describe it as a P1B beta-injection-recovery pipeline-validation rerun, not a P4 chirality measurement — recorded here as paper=P4 per the inventory's grouping, with this discrepancy flagged for honesty."
    },
    "outputs": [
      {
        "locator": "reproducibility/p1_namaster_500mc/results/c1_fsky_sweep.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the canonical fsky=0.32 reference (recovered_beta_deg=0.238, bias_deg=0.032, snr_se=20.32) and the fsky=0.85/0.65 sweep results (e.g. fsky_target=0.85: beta_recovered_deg=0.237, bias_deg=-0.033, snr_se=181.38) match the committed JSON within numeric tolerance.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — C1/C2/C3 NaMaster MC batch bullet",
      "project-context/SSOT/compute-queue.md (pod ID 5i2td3deu3hojr; C1 row, 2026-06-09 18:42 start, RUNNING/~1.3h ETA at doc write time)",
      "Path correction: the inventory does not give a repo-relative output path for C1 (only the pod-local `/workspace/c1_results/c1_fsky_sweep.json`); verified via `find` that the mirrored completed output lives at `reproducibility/p1_namaster_500mc/results/c1_fsky_sweep.json`, under the bounce-theory P1B NaMaster tree rather than pipelines/p2_chirality/outputs/canonical_provenance/ where C2/C3 outputs live."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-c2-nall-binomial-null",
    "title": "C2 — monopole/dipole N_all binomial null",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "h200_scripts/experiments/c2_p4_nall_binomial_null.py",
        "entrypoint": "python3 c2_p4_nall_binomial_null.py",
        "sha256": null
      },
      {
        "path": "h200_scripts/experiments/launch_c123_pod.sh",
        "entrypoint": "bash launch_c123_pod.sh",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, scipy — see requirements.txt",
      "hardware": "cpu-strong (12 vCPU/62GB)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": null,
      "pod_id_or_host": "5i2td3deu3hojr, RTX A4000, $0.17/hr, 12 vCPU/62GB",
      "date": "2026-06-09",
      "wall_clock": "358s",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod CPU-strong instance or local CPU (job is CPU-bound)",
      "est_wall_clock": "~6-10 minutes",
      "est_cost_usd": 0.02,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Wall-clock (358s) is DONE-logged in the inventory/compute-queue; only the pod's hourly rate ($0.17/hr) is known, no single-job dollar total was recorded, so actual_cost_usd stays null per directive and the estimate here is derived from rate x wall-clock."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/c2_nall_binomial_null.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the N_all binomial-null test statistics match the committed JSON within numeric tolerance stated in the result file.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — C1/C2/C3 NaMaster MC batch bullet (C2 DONE 358s)",
      "project-context/SSOT/compute-queue.md (shared pod 5i2td3deu3hojr)",
      "project-context/SSOT/paper-4/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-c3-wp-invariance-fsky",
    "title": "C3 — Wp (N_all vs N_spiral) fsky invariance null",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "h200_scripts/experiments/c3_p4_wp_invariance_fsky.py",
        "entrypoint": "python3 c3_p4_wp_invariance_fsky.py",
        "sha256": null
      },
      {
        "path": "h200_scripts/experiments/launch_c123_pod.sh",
        "entrypoint": "bash launch_c123_pod.sh",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, scipy — see requirements.txt",
      "hardware": "cpu-strong (12 vCPU/62GB)"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": null,
      "pod_id_or_host": "5i2td3deu3hojr, RTX A4000, $0.17/hr, 12 vCPU/62GB",
      "date": "2026-06-09",
      "wall_clock": "387s",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod CPU-strong instance or local CPU (job is CPU-bound)",
      "est_wall_clock": "~6-10 minutes",
      "est_cost_usd": 0.02,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Wall-clock (387s) is DONE-logged in the inventory/compute-queue; only the pod's hourly rate ($0.17/hr) is known, no single-job dollar total was recorded, so actual_cost_usd stays null per directive and the estimate here is derived from rate x wall-clock."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/c3_wp_invariance_fsky.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the Wp (N_all vs N_spiral) fsky-invariance null test statistics match the committed JSON within numeric tolerance stated in the result file.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — C1/C2/C3 NaMaster MC batch bullet (C3 DONE 387s)",
      "project-context/SSOT/compute-queue.md (shared pod 5i2td3deu3hojr; line 29)",
      "project-context/SSOT/paper-4/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-dipole-8m-fullcatalog",
    "title": "Dipole analysis (8.47M full-catalog)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/run_dipole_8M.py",
        "entrypoint": "python3 run_dipole_8M.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, healpy, pandas, matplotlib — see requirements.txt",
      "hardware": "gpu-40gb"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "H200",
      "pod_id_or_host": "historical pod, terminated 2026-04-17",
      "date": "2026-04-17",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod A100/H200-class GPU for the full 8.47M-galaxy dipole computation",
      "est_wall_clock": "several hours, scaling with catalog size and TTA passes",
      "est_cost_usd": 10,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Only the termination date and 'H200 pod' venue are evidenced; the full dipole JSON is only partially reconstructed from a log, not re-run from scratch, so this experiment needs-data-restore rather than being cleanly runnable-now."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/dipole/summary.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/dipole/fig_dipolar_skymap.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/dipole/fig_dipolar_power_spectrum.png",
        "type": "figure",
        "checksum": null
      }
    ],
    "verification": "Re-run the full 8.47M-galaxy dipole analysis and confirm 2.31 sigma raw dipole significance and 0.43 sigma post-TTA (test-time-augmentation-corrected) significance, within +/-0.1 sigma numeric tolerance.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — dipole analysis (8.47M full-catalog) bullet",
      "project-context/SSOT/paper-4/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-dr8-axis-ratio-crossmatch",
    "title": "Empirical b/a (axis-ratio) DR8 morphology cross-match",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "ls_dr8.tractor (Legacy Survey DR8 Tractor catalog, via NOIRLab Astro Data Lab TAP)",
        "type": "external-dataset",
        "locator": "ls_dr8.tractor table, NOIRLab Astro Data Lab TAP service",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "NOIRLab Astro Data Lab TAP",
        "endpoint": "https://datalab.noirlab.edu/tap",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p2_chirality/scripts/pull_dr8_final.py",
        "entrypoint": "python3 pull_dr8_final.py",
        "sha256": null
      },
      {
        "path": "pipelines/p2_chirality/scripts/pull_dr8_datalab.py",
        "entrypoint": "python3 pull_dr8_datalab.py",
        "sha256": null
      },
      {
        "path": "pipelines/p2_chirality/scripts/edge_on_contamination_metric.py",
        "entrypoint": "python3 edge_on_contamination_metric.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, pyarrow, requests — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": null,
      "pod_id_or_host": "spot A4000 that is now EXITED (exact pod ID not recorded)",
      "date": "2026-07-02",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU or any RunPod instance (TAP pull + metric computation are CPU-bound, network-bound on the TAP query)",
      "est_wall_clock": "~30-60 minutes depending on TAP query throughput for the full catalog cross-match",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "This is gap #5 in the inventory's Top-5-gaps list: the original spot-A4000 pod is EXITED with no dollar figure recorded, and the NOIRLab TAP query parameters were not captured as a standalone provenance artifact. The script itself is runnable-now; only the previously TAP-pulled data has not been re-fetched."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/spiral_morphology_dr8.parquet",
        "type": "catalog",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/edge_on_contamination_metric.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run the TAP pull + edge-on metric computation and confirm f_edge=15.8% (edge-on contamination fraction, 505,889 of 3,201,160 objects per the v1.0.240 regeneration) within +/-0.5 percentage-point numeric tolerance.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — empirical b/a (axis-ratio) DR8 morphology cross-match bullet",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps — item 5 (P4 empirical b/a DR8 morphology cross-match)",
      "project-context/SSOT/paper-4/status.md (DP4-22 finding + v1.0.240 regeneration: edge_on_contamination_metric.json regenerated from the parquet on disk, script-reproducible)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-e2e-mirror-flip",
    "title": "e2e mirror-flip full-catalog inference (8.47M galaxies x 2 passes)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "inference-scan",
    "inputs": [
      {
        "name": "G1 retrained checkpoint",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/outputs/g1_retrain/g1_ckpt_best.pt",
        "checksum": "aed109dc… (sha256, partial per inventory)"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/scripts/e2e_mirror_flip_fullrun.py",
        "entrypoint": "python3 e2e_mirror_flip_fullrun.py",
        "sha256": null
      },
      {
        "path": "pipelines/p2_chirality/scripts/e2e_mirror_flip_transfer_function.py",
        "entrypoint": "python3 e2e_mirror_flip_transfer_function.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "torch, timm, pandas, pyarrow, numpy — see requirements.txt",
      "hardware": "gpu-40gb"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "A100",
      "pod_id_or_host": "0hh3humgpacgz1 (\"bigbounce-p4-e2e-mirror\", $1.19/hr rate quoted elsewhere)",
      "date": "2026-07-11/12",
      "wall_clock": "10.45h",
      "actual_cost_usd": 12.44
    },
    "reproduction": {
      "recommended_venue": "runpod A100 (or equivalent 40GB-class GPU)",
      "est_wall_clock": "~10-11 hours for the full 192-shard, 16,949,062-inference run",
      "est_cost_usd": 12.44,
      "parallelizable": true,
      "resume_support": true,
      "notes": "This is the best-documented cost/venue/time experiment in the repo (per inventory) — the estimate here simply restates the evidenced original-run total since it already IS a clean receipt. The 685MB shard outputs are backed to HF + B2 + local but are NOT checked into git (data-availability caveat) even though the pipeline itself remains runnable-now."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/e2e_fullrun/e2e_transfer_function_full.json",
        "type": "result-json",
        "checksum": "925649b7… (md5, partial per inventory)"
      }
    ],
    "verification": "Re-run and confirm T_raw=0.2303, T_eq=0.99974 (transfer function values) with all 192/192 shards completing 16,949,062 inferences, within numeric tolerance stated in the result file; md5 925649b7… for a byte-identical reproduction.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — e2e mirror-flip full-catalog inference bullet (\"the best-documented cost/venue/time experiment in the repo\")",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md (line 533)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-g1-ce-composition-assembly",
    "title": "G1 CE-included full composition (826-vs-846 adjudication)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "analysis",
    "inputs": [
      {
        "name": "G1 retrained checkpoint",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/outputs/g1_retrain/g1_ckpt_best.pt",
        "checksum": "aed109dc… (sha256, partial per inventory)"
      },
      {
        "name": "CE-ResNet Zenodo release (pre_desi.fits)",
        "type": "external-dataset",
        "locator": "https://doi.org/10.5281/zenodo.7167388",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/scripts/g1_ce_composition_assembly.py",
        "entrypoint": "python3 g1_ce_composition_assembly.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pandas, numpy, pyarrow — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "minutes to ~1 hour for the 26,609-object composition/adjudication pass",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "CPU-only composition-assembly stage; the GPU host was capacity-full at original-run time so this ran on local CPU by necessity, which is also the natural reproduction venue."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/g1_full_composition/g1_full_composition_manifest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/g1_full_composition/ce_composition_full.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm 26,609 total objects with ce_not_spiral=819 adjudicated (the 826-vs-846 CE-inclusion adjudication resolved) — exact integer match, not a numeric tolerance.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — G1 CE-included full composition bullet",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-g1-vit-retrain-manifest",
    "title": "G1 — regenerable ViT-Small retrain with manifest (supersedes historical v2 training)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "training",
    "inputs": [
      {
        "name": "Smith42/galaxies (HF)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/Smith42/galaxies",
        "checksum": null,
        "license": null
      },
      {
        "name": "GZ1 CW/CCW human-vote labels (S3-hosted)",
        "type": "external-dataset",
        "locator": "GZ1 CW/CCW label set, S3-hosted — exact bucket path not captured in the inventory",
        "checksum": null,
        "license": null
      },
      {
        "name": "GZ×DESI crossmatch",
        "type": "external-dataset",
        "locator": "GZ×DESI crossmatch (HF revision b7583bb2…; exact HF repo id not captured in the inventory)",
        "checksum": "b7583bb2… (HF revision, partial per inventory)",
        "license": null
      },
      {
        "name": "CE-ResNet Zenodo release (pre_desi.fits)",
        "type": "external-dataset",
        "locator": "https://doi.org/10.5281/zenodo.7167388",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/train_g1_manifest.py",
        "entrypoint": "python3 train_g1_manifest.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "torch, timm, huggingface_hub, datasets, pillow, numpy — see requirements.txt (repo root)",
      "hardware": "gpu-16gb"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000 16GB",
      "pod_id_or_host": "smoke test: 580dgszgib3ti4; full retrain: fresh on-demand pod th0o0l1tp1se4e ($0.17/hr)",
      "date": "2026-07-17",
      "wall_clock": "smoke ~1.5h; full G1 lane running total <1h of billed uptime across the lane, with one recorded pod window at ~4.2h uptime (fragmentary — see reproduction.notes)",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod A4000 16GB on-demand",
      "est_wall_clock": "~1.5h smoke test + ~4-5h full retrain",
      "est_cost_usd": 1,
      "parallelizable": false,
      "resume_support": true,
      "notes": "Evidenced-but-fragmentary cost figures: smoke test ~$0.26 (1.5h); one full-retrain pod window ~$0.71 (~4.2h uptime at $0.17/hr) — these don't sum to one clean run-total, so original_run.actual_cost_usd is left null per directive. best_val_acc=0.9931 @ epoch 47, early-stop epoch 62."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/g1_retrain/g1_ckpt_best.pt",
        "type": "model",
        "checksum": "aed109dc… (sha256, partial per inventory)"
      },
      {
        "locator": "pipelines/p2_chirality/outputs/g1_retrain/g1_training_manifest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/g1_retrain/g1_training_result.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm best_val_acc=0.9931 at epoch 47 (early-stop epoch 62) within +/-0.001 tolerance; for a byte-identical reproduction, sha256 of g1_ckpt_best.pt should match aed109dc…, otherwise fall back to the accuracy tolerance for a fresh-seed retrain.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — G1 regenerable ViT-Small retrain bullet",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md",
      "3-location backup verified: local + HF g1-retrain-2026-07-17/ + pod, hash round-trip MATCH (per inventory)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-g2-disjoint-validation",
    "title": "G2 — training-disjoint held-out GZ1 validation",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "validation",
    "inputs": [
      {
        "name": "G1 retrained checkpoint",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/outputs/g1_retrain/g1_ckpt_best.pt",
        "checksum": "aed109dc… (sha256, partial per inventory)"
      },
      {
        "name": "GZ1 CW/CCW human-vote labels (S3-hosted)",
        "type": "external-dataset",
        "locator": "GZ1 CW/CCW label set, S3-hosted — exact bucket path not captured in the inventory",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/analysis/g2_disjoint_validation_v1_0_266.py",
        "entrypoint": "python3 g2_disjoint_validation_v1_0_266.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "torch, timm, scikit-learn, numpy — see requirements.txt",
      "hardware": "gpu-16gb"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000",
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": "358s",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod A4000 or equivalent 16GB GPU (inference-only)",
      "est_wall_clock": "~6-10 minutes",
      "est_cost_usd": 0.05,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Inference-only validation pass; n=3000 disjoint GZ1 spirals held fully out of G1 training via anti-join on retained training object IDs."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/analysis/g2_disjoint_validation_v1_0_266.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm accuracy=0.9867, Cohen's kappa=0.9733 on the n=3000 disjoint GZ1-spiral held-out set, within +/-0.001 numeric tolerance.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — G2 training-disjoint held-out GZ1 validation bullet",
      "project-context/SSOT/paper-4/status.md",
      "Path correction: the inventory names the output as `g2_disjoint_validation_v1_0_266.json` without a directory; verified via `find` that both the script and its output JSON live in `pipelines/p2_chirality/analysis/`, not under an `outputs/` directory."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-g3-joint-estimator-covariance",
    "title": "G3 — joint estimator covariance (local bootstrap leg + RunPod MASTER-leg refinement)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/scripts/g3_joint_estimator_covariance.py",
        "entrypoint": "python3 g3_joint_estimator_covariance.py",
        "sha256": null
      },
      {
        "path": "pipelines/p2_chirality/scripts/g3_joint_estimator_covariance_master_v2.py",
        "entrypoint": "python3 g3_joint_estimator_covariance_master_v2.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pymaster (MASTER-leg only), numpy, scipy — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000 (MASTER-leg only; the local-bootstrap leg is CPU-only and ran off-pod)",
      "pod_id_or_host": "580dgszgib3ti4 (shared with the p1b-namaster-window-regen phase-2 session)",
      "date": "2026-07-18",
      "wall_clock": "MASTER-leg ~62 min within a shared 2.1h/$0.36 phase-2 pod session; local-bootstrap leg ~573s (N=2000 bootstrap) separately on local CPU",
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU for the base bootstrap leg; RunPod A4000 (or a local pymaster install) for the MASTER-leg refinement",
      "est_wall_clock": "~10-15 min local-bootstrap leg + ~1h MASTER-leg",
      "est_cost_usd": 0.36,
      "parallelizable": true,
      "resume_support": true,
      "notes": "runnable-now, closed-by-artifact per the inventory's own reproducibility verdict — both leg outputs already exist and are treated as the terminal artifact. The MASTER-leg pod session (580dgszgib3ti4) was SHARED with p1b-namaster-window-regen — the $0.36/2.1h phase-2 total is a bundled figure across both experiments, not cleanly attributable to G3 alone."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/g3_joint_estimator_covariance.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/g3_joint_estimator_covariance_master_v2.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run both legs and confirm the joint estimator covariance matrix entries match the committed JSONs within a relative-difference tolerance of <1%; cross-check against the HF backup p4_compute_phase2_2026-07-18/ (sha256-verified) as the primary hash check.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — G3 joint estimator covariance bullet",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md",
      "MASTER-leg pod session shared with reproducibility/manifests/experiments/p1b-namaster-window-regen.json (pod 580dgszgib3ti4, 2026-07-18) — cross-referenced there as 'shared with P4 G3 MASTER-leg session'"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-g4-monopole-mechanism-injection",
    "title": "G4 — per-pixel confusion + generative parity-null (monopole mechanism)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Banked e2e mirror-flip per-galaxy pair record",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/e2e_fullrun/e2e_mirror_pairs.parquet (banked record from the e2e mirror-flip A100 run, pod 0hh3humgpacgz1, 2026-07-11/12 — not confirmed present in git; large-shard data, see p4-e2e-mirror-flip)",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/scripts/g4_monopole_mechanism_injection.py",
        "entrypoint": "python3 g4_monopole_mechanism_injection.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, healpy, pandas, pyarrow — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU or RunPod aggregation-only instance (no GPU inference required, reuses banked e2e mirror-pair record)",
      "est_wall_clock": "tens of minutes for per-pixel confusion + generative parity-null aggregation over the banked record",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "No new GPU inference required — this experiment reuses the banked e2e_mirror_pairs.parquet record, so it ran as aggregation-only on the RunPod pod ($0 H200 spend) with an avoided cost of an estimated $20-50 had fresh GPU inference been required (per inventory); that avoided-cost figure is NOT an actual_cost and is recorded here, not in original_run."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/g4_monopole_mechanism_injection.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/g4_perpixel_confusion_nside64.npz",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run against the banked e2e_mirror_pairs.parquet record and confirm the per-pixel confusion map (nside=64) and generative parity-null statistics match the committed JSON/NPZ within numeric tolerance stated in the result file.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — G4 per-pixel confusion + generative parity-null bullet",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md (line 533: banked per-galaxy record e2e_mirror_pairs.parquet, A100 pod 0hh3humgpacgz1, 2026-07-11/12)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-gz1only-retrain-dipole-null",
    "title": "GZ1-only classifier retrain + dipole null (pseudo-label independence check)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "validation",
    "inputs": [
      {
        "name": "GZ1 CW/CCW human-vote labels (S3-hosted)",
        "type": "external-dataset",
        "locator": "GZ1 CW/CCW label set, S3-hosted — exact bucket path not captured in the inventory",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/run_dipole_gz1only_fullN.py",
        "entrypoint": "python3 run_dipole_gz1only_fullN.py",
        "sha256": null
      },
      {
        "path": "pipelines/p2_chirality/scripts/gz1_stratified_confusion.py",
        "entrypoint": "python3 gz1_stratified_confusion.py",
        "sha256": null
      },
      {
        "path": "pipelines/p2_chirality/validate_p4_v1_0_244_claims.py",
        "entrypoint": "python3 validate_p4_v1_0_244_claims.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, scipy, pandas — see requirements.txt",
      "hardware": "gpu-16gb (for the original GZ1-only classifier retrain); cpu-only for the surviving downstream dipole-null recomputation"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "RTX A4000 16GB community",
      "pod_id_or_host": "8ol1r8eew7h6br (\"bigbounce-p4-gz1only\", $0.17/hr)",
      "date": "2026-07-01",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU for the surviving dipole-null recomputation; RunPod A4000 16GB would be needed to redo the full GZ1-only classifier retrain from scratch",
      "est_wall_clock": "~10 min local for the dipole-null recomputation on the surviving JSON (per COMPUTE_CAMPAIGN's own note); full end-to-end retrain time not estimable without the lost training script",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "The downstream dipole-null re-computation from the surviving gz1only_dipole_result.json / gz1_stratified_confusion.json is runnable-now at $0 locally. Full end-to-end reproduction (retraining the GZ1-only classifier itself) requires restoring a training script that is not preserved in the repo — see provenance."
    },
    "outputs": [
      {
        "locator": "pipelines/p2_chirality/outputs/gz1only_dipole_result.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/gz1only_fullN_dipole_result.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p2_chirality/outputs/gz1_stratified_confusion.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run the surviving dipole-null analysis and confirm dipole z=-0.04 sigma (pseudo-label independence check) within +/-0.02 sigma numeric tolerance.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — GZ1-only classifier retrain + dipole null bullet",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md (G2 spec section, lines 480-500)",
      "Path correction: the inventory cites a script variant `train_chirality_gz1only.py` (\"staged from train_chirality_v2.py\"); verified via `find . -iname \"train_chirality_gz1only.py\"` that this file does NOT exist anywhere in the current repo. What does exist and is used here instead: `pipelines/p2_chirality/run_dipole_gz1only_fullN.py`, `pipelines/p2_chirality/scripts/gz1_stratified_confusion.py`, and `pipelines/p2_chirality/validate_p4_v1_0_244_claims.py` — downstream analysis scripts that operate on the GZ1-only model's surviving output, not the original training script itself. Status set to needs-data-restore because the training script/checkpoint that produced the GZ1-only model is not preserved in-repo, even though the downstream dipole-null recomputation on the surviving JSON is runnable-now."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4-v2-vit-production-training",
    "title": "v2 ViT-Small production training (26,616-object historical realization)",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "training",
    "inputs": [
      {
        "name": "Smith42/galaxies (HF)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/Smith42/galaxies",
        "checksum": "bdd1b063… (HF revision, partial per inventory)",
        "license": null
      },
      {
        "name": "GZ1 CW/CCW human-vote labels (S3-hosted)",
        "type": "external-dataset",
        "locator": "GZ1 CW/CCW label set, S3-hosted — exact bucket path not captured in the inventory",
        "checksum": null,
        "license": null
      },
      {
        "name": "CE-ResNet Zenodo release (pre_desi.fits)",
        "type": "external-dataset",
        "locator": "https://doi.org/10.5281/zenodo.7167388",
        "checksum": null,
        "license": null
      },
      {
        "name": "Galaxy Zoo DESI morphology predictions (Walmsley 2023)",
        "type": "external-dataset",
        "locator": "Galaxy Zoo DESI predictions, Walmsley et al. 2023 — exact data locator not captured in the inventory",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p2_chirality/train_chirality_v2.py",
        "entrypoint": "python3 train_chirality_v2.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "torch, timm, huggingface_hub, datasets, pillow, numpy — see requirements.txt (repo root)",
      "hardware": "gpu-24gb"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "H200",
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "runpod (A100/H200-class GPU, ViT-Small image classifier training)",
      "est_wall_clock": "3-6 hours for a 26,616-object realization at typical ViT-Small batch throughput",
      "est_cost_usd": 5,
      "parallelizable": false,
      "resume_support": true,
      "notes": "The original run's exact labels/split manifest were not retained, so a byte-identical reproduction of THIS checkpoint is not possible — see p4-g1-vit-retrain-manifest for the regenerable, manifest-bound successor that supersedes this training. This estimate covers reproducing an equivalent training run against the same input datasets, not an exact checkpoint match."
    },
    "outputs": [
      {
        "locator": "HF bamfai/galaxy-chirality-v2 (checkpoint SHA 618d170f…)",
        "type": "model",
        "checksum": "618d170f… (partial SHA quoted in inventory)"
      }
    ],
    "verification": "No numeric target is defined for this historical realization since its labels/manifest were not retained; status is superseded. Use p4-g1-vit-retrain-manifest's best_val_acc=0.9931 (epoch 47) as the current verifiable production-training benchmark instead.",
    "status": "superseded",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P4 — v2 ViT-Small production training bullet",
      "project-context/SSOT/paper-4/status.md",
      "project-context/SSOT/paper-4/COMPUTE_CAMPAIGN_2026-07-17.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4prime-bh-universe-dipole-exclusion",
    "title": "P4' (Track C1) — confront the DESI chirality catalog's coverage-calibrated observed-label 95% sensitivity floor with Poplawski's rotating-black-hole-universe spin-axis claim",
    "program": "black-hole-cosmology-test",
    "paper": "P4' (pipelines/p4prime_chirality_test/paper/main.tex, v4P.0.1)",
    "kind": "analysis",
    "inputs": [
      {
        "name": "A_95^obs and N_support (verbatim, not re-derived)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/chirality_catalog_paper.tex (v1.0.274), Sec. 'Coverage-calibrated observed-label upper limit', Eq. eq:a95_obs",
        "checksum": null
      },
      {
        "name": "Literature spin-axis amplitude claims (as published, cited by arXiv id, no re-analysis)",
        "type": "external-reference",
        "locator": "arXiv:1104.2815 (Longo 2011); arXiv:1207.5464 (Shamir 2012); arXiv:2007.16116 (Shamir 2020); arXiv:2208.13866 (Shamir 2022); arXiv:2502.18781 (Shamir 2025)",
        "checksum": null
      },
      {
        "name": "Poplawski black-hole-universe mechanism and preferred-axis papers",
        "type": "external-reference",
        "locator": "arXiv:1007.0587; arXiv:1111.4595; arXiv:1410.3881 (ApJ 832, 96, 2016); arXiv:1910.10819",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py",
        "entrypoint": "python3 research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py",
        "sha256": "9dba968880d61d0deb3fbba4f329e85391d1f247f2a691e90c24d744bb2abf49"
      }
    ],
    "environment": {
      "python": "python3 + numpy (stdlib json/math otherwise)",
      "hardware": "cpu-only; Apple M-series, macOS arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation",
      "date": "2026-09-02",
      "wall_clock": "0.03 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "< 0.1 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Pure arithmetic over literal, cited constants; no data download, no GPU, no network access required. Re-running reproduces the output JSON byte-for-byte given the same numpy/python version (values are exact closed-form arithmetic, not floating-point-sensitive iteration)."
    },
    "outputs": [
      {
        "locator": "research/bh_universe_dipole/outputs/poplawski_dipole_exclusion_2026_09_02.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Manual inspection: every field in the output JSON traces to either (a) a literal constant copied verbatim from the cited source with a section/equation pointer (A_95_obs, N_support, A_dip_observed, g_bridge), (b) a literal published literature amplitude with its arXiv citation, or (c) a closed-form arithmetic function of (a) and (b) (ratio, 1/sqrt(N) scaling). No fitting, optimization, or random draws occur in this script.",
    "status": "reproduced",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 5",
      "project-context/PORTFOLIO_DECISION_2026-09-02.md Track C1 Addendum",
      "pipelines/p4prime_chirality_test/paper/main.tex Sec. 5 (The black-hole-universe prediction and its exclusion)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-astra-crossmatch-hf-mirror",
    "title": "Astra per-object crossmatch + HuggingFace mirror",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/15_astra_per_object_crossmatch.py",
        "entrypoint": "python3 15_astra_per_object_crossmatch.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/mirror_astra_to_hf.py",
        "entrypoint": "python3 mirror_astra_to_hf.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, huggingface_hub — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "~30 min - 1 hour for the per-object crossmatch + HF mirror push",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Not evidenced beyond code presence in the inventory; all original_run fields stay null. Reproduction requires a valid HF_TOKEN with write access to bamfai/astra-desi-edr-mirror to complete the mirror step."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/analysis_astra_per_object/summary.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "https://huggingface.co/datasets/bamfai/astra-desi-edr-mirror",
        "type": "dataset",
        "checksum": null
      }
    ],
    "verification": "Re-run the crossmatch and confirm the per-object summary statistics in analysis_astra_per_object/summary.json match the committed output, and that the HF mirror bamfai/astra-desi-edr-mirror reflects the same row count.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — astra per-object crossmatch + HF mirror bullet",
      "project-context/SSOT/paper-5/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-cosmic-web-desivast-void",
    "title": "Cosmic-web / DESIVAST void analysis (16, 27, 35-39 series)",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "DESI DR1 DESIVAST Value-Added Catalog",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/",
        "checksum": null,
        "license": null
      },
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [
      {
        "name": "DESI DR1 public data portal",
        "endpoint": "https://data.desi.lbl.gov/public/dr1/vac/dr1/desivast/v1.0/",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/16_cosmic_web_zshell_corrected.py",
        "entrypoint": "python3 16_cosmic_web_zshell_corrected.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/08_analysis_cosmic_web.py",
        "entrypoint": "python3 08_analysis_cosmic_web.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/27_rsd_void_recon_bound.py",
        "entrypoint": "python3 27_rsd_void_recon_bound.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/35_desivast_cluster_bootstrap.py",
        "entrypoint": "python3 35_desivast_cluster_bootstrap.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/36_desivast_native_selection_control.py",
        "entrypoint": "python3 36_desivast_native_selection_control.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, scipy, healpy — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-07-12",
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU (no RunPod hit found for the p5 script family per the inventory's own grep)",
      "est_wall_clock": "~1-2 hours across the cluster-bootstrap and RSD/void-reconstruction steps over DESIVAST VAC + the ~2.23M-row matched catalog",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "reproducibility: runnable-now, gap = no venue/cost evidence — the code runs, just no compute-receipt exists for the original run. Lineage note: the earlier '187-DESI-attribute cosmic-web catalog' blocker (SSOT: 'Houston-mediated, confirmed not in repo') was later resolved via this DESIVAST VAC approach, superseding the earlier env_finder/ 'run our own cosmic-web finder' fallback plan."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/outputs/27_rsd_void_recon_bound.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/16_cosmic_web_zshell_corrected.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/35_desivast_cluster_bootstrap.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/36_desivast_native_selection_control.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the DP5-12 closure result in 27_rsd_void_recon_bound.json (RSD void-reconstruction bound, 2026-07-12) matches the committed JSON within the numeric tolerance stated in the result file.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — cosmic-web / DESIVAST void analysis bullet (16, 27, 35-39 series) + its lineage Note",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps — item 3 (P5 cosmic-web / DESIVAST + r24conf pod-session scripts, venue evidence missing)",
      "project-context/SSOT/paper-5/status.md",
      "Added `08_analysis_cosmic_web.py` to code[] beyond the inventory's explicit list: verified via `ls pipelines/p5_desi_chirality/scripts/` that this script (within the same 05-09 numbered range referenced by the redshift/density/healpix/systematics bullet) is the cosmic-web analysis, not a HEALPix/systematics script, and its output directory `results/analysis_cosmic_web/` matches this experiment's scope rather than the 16a-16d split."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-density-analysis",
    "title": "P5 local-density-dependence analysis of spiral chirality",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/06_analysis_density.py",
        "entrypoint": "python3 06_analysis_density.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, scipy, matplotlib — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "minutes to tens of minutes over the ~2.23M-row matched catalog",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/analysis_density/",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the local-density-binned chirality fraction statistics in analysis_density/ match the committed outputs within the numeric tolerance stated in the result files.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — redshift / density / HEALPix / systematics analyses bullet (scripts 05-09)",
      "project-context/SSOT/paper-5/status.md",
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — 06_analysis_density.py maps to this analysis."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-desi-dr1-crossmatch-build",
    "title": "P4xDESI DR1 crossmatch + matched catalog build",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "DESI DR1 public data release",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/",
        "checksum": null,
        "license": null
      },
      {
        "name": "P4 galaxy-chirality catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/ (P4 catalog release, see p4-* manifests)",
        "checksum": null
      }
    ],
    "apis": [
      {
        "name": "DESI DR1 public data portal",
        "endpoint": "https://data.desi.lbl.gov/public/dr1/",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/01_fetch_p4_catalog.py",
        "entrypoint": "python3 01_fetch_p4_catalog.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/02_fetch_desi_dr1.py",
        "entrypoint": "python3 02_fetch_desi_dr1.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/03_crossmatch.py",
        "entrypoint": "python3 03_crossmatch.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, pyarrow, numpy, requests — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU (implied local/CPU-bound crossmatch — no venue was explicitly logged for the original run)",
      "est_wall_clock": "~1-3 hours for the DESI DR1 fetch + 2,232,212-row crossmatch, dominated by DESI DR1 download bandwidth",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "No venue was explicitly logged in the inventory for this run; 'implied local' is a reproduction-side inference only, not an original_run fact, so all original_run fields stay null. The matched parquet itself (1.3GB, 2,232,212 rows) is not checked into git — only its provenance/summary JSONs are — consistent with the repo's pattern of keeping large derived artifacts out of git."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "type": "catalog",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi_summary.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet.provenance.json",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the matched catalog contains 2,232,212 rows (1.3GB parquet) via p5_matched_chirality_desi_summary.json's row count, exact integer match.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — P4xDESI DR1 crossmatch + matched catalog build bullet",
      "project-context/SSOT/paper-5/status.md",
      "Verified via `find` that the 1.3GB parquet itself is not present in the repo tree; only p5_matched_chirality_desi_summary.json and p5_matched_chirality_desi.parquet.provenance.json are — noted in reproduction.notes rather than fabricating a checksum for the missing parquet."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-focal-cluster-robustness",
    "title": "Focal cluster inference sensitivity + interaction clustering robustness",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/38_focal_cluster_inference_sensitivity.py",
        "entrypoint": "python3 38_focal_cluster_inference_sensitivity.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/39_focal_interaction_clustering_robustness.py",
        "entrypoint": "python3 39_focal_interaction_clustering_robustness.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, scipy, scikit-learn — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "~30 min - 1 hour across both robustness scripts",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "runnable-now (code present per inventory); part of the same r-conf family as p5-rconf-closures and shares the same venue-evidence gap — no RunPod pod ID, GPU class, cost, or runtime found in pipelines/p5_desi_chirality/ or in the reachable sections of paper-5/status.md, so all original_run fields stay null."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/outputs/38_focal_cluster_inference_sensitivity.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/39_focal_interaction_clustering_robustness.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run both scripts and confirm the focal-cluster inference sensitivity and interaction-clustering robustness statistics match the committed JSONs within the numeric tolerance stated in each result file.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — r23conf/r24conf/r27conf closure recomputes + focal cluster inference bullet",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps — item 3 (venue evidence missing for this r-conf family)",
      "project-context/SSOT/paper-5/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-healpix-analysis",
    "title": "P5 HEALPix sky-map analysis of spiral chirality",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/07_analysis_healpix.py",
        "entrypoint": "python3 07_analysis_healpix.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "healpy, astropy, pandas, numpy, matplotlib — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "minutes to tens of minutes over the ~2.23M-row matched catalog",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/analysis_healpix/",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the HEALPix-binned sky-map chirality statistics in analysis_healpix/ match the committed outputs within the numeric tolerance stated in the result files.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — redshift / density / HEALPix / systematics analyses bullet (scripts 05-09)",
      "project-context/SSOT/paper-5/status.md",
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — note the inventory's own '05-09' numbering is not a clean 1:1 map: 07_analysis_healpix.py is the HEALPix script, while 08_analysis_cosmic_web.py (also in the 05-09 range) is NOT a HEALPix/systematics script but the cosmic-web analysis, and is instead attached to p5-cosmic-web-desivast-void."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-rconf-closures",
    "title": "r23conf/r24conf/r27conf closure recomputes",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/21_r23conf_meta_closures.py",
        "entrypoint": "python3 21_r23conf_meta_closures.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/22_r24conf_local_batch.py",
        "entrypoint": "python3 22_r24conf_local_batch.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/24_r24conf_pod_session.py",
        "entrypoint": "python3 24_r24conf_pod_session.py",
        "sha256": null
      },
      {
        "path": "pipelines/p5_desi_chirality/scripts/26_r27conf_ess_recomputes.py",
        "entrypoint": "python3 26_r27conf_ess_recomputes.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, scipy — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": null,
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": null
    },
    "reproduction": {
      "recommended_venue": "local CPU (the pod-implying filename is unconfirmed; a local or RunPod CPU-strong instance both work)",
      "est_wall_clock": "~30 min - 2 hours across the four closure/batch scripts",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "reproducibility: runnable-now (code present per inventory), venue evidence missing. This is gap #3 in the inventory's Top-5-gaps list: the script name `24_r24conf_pod_session.py` implies RunPod use but no pod ID, GPU class, cost, or runtime was found in pipelines/p5_desi_chirality/ or in the reachable sections of paper-5/status.md — so all original_run fields stay null rather than being inferred from the filename alone."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/outputs/21_r23conf_meta_closures.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/22_r24conf_local_batch.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/24_r24conf_pod_session.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/outputs/26_r27conf_ess_recomputes.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run all four closure recomputes and confirm the r23conf/r24conf/r27conf statistics match the committed JSONs within the numeric tolerance stated in each result file.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — r23conf/r24conf/r27conf closure recomputes + focal cluster inference bullet",
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §Top 5 gaps — item 3 (P5 cosmic-web / DESIVAST + r24conf pod-session scripts, venue evidence missing)",
      "project-context/SSOT/paper-5/status.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-redshift-analysis",
    "title": "P5 redshift-dependence analysis of spiral chirality",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/05_analysis_redshift.py",
        "entrypoint": "python3 05_analysis_redshift.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, scipy, matplotlib — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "minutes to tens of minutes over the ~2.23M-row matched catalog",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/analysis_redshift/",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the redshift-binned chirality fraction statistics in analysis_redshift/ match the committed outputs within the numeric tolerance stated in the result files.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — redshift / density / HEALPix / systematics analyses bullet (scripts 05-09)",
      "project-context/SSOT/paper-5/status.md",
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — 05_analysis_redshift.py maps to this analysis."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p5-systematics-analysis",
    "title": "P5 systematics analysis of spiral chirality measurement",
    "program": "galaxy-chirality",
    "paper": "P5",
    "kind": "analysis",
    "inputs": [
      {
        "name": "P5 matched chirality x DESI DR1 catalog",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p5_desi_chirality/scripts/09_systematics.py",
        "entrypoint": "python3 09_systematics.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, pandas, numpy, scipy, matplotlib — see requirements.txt",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": null,
      "wall_clock": null,
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "minutes to tens of minutes over the ~2.23M-row matched catalog",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/analysis_systematics/",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm the systematics-control statistics in analysis_systematics/ match the committed outputs within the numeric tolerance stated in the result files.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — redshift / density / HEALPix / systematics analyses bullet (scripts 05-09)",
      "project-context/SSOT/paper-5/status.md",
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — 09_systematics.py maps to this analysis."
    ]
  }
];
