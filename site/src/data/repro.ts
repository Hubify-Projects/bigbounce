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
      },
      {
        "id": "p3-flagship-s8-enrichment",
        "depends_on": []
      },
      {
        "id": "p3-flagship-s8-allwise-photometry",
        "depends_on": [
          "p3-flagship-s8-enrichment"
        ]
      },
      {
        "id": "p3-flagship-s8-simbad-ned-crossmatch",
        "depends_on": [
          "p3-flagship-s8-enrichment"
        ]
      },
      {
        "id": "p3-flagship-s8-taxonomy",
        "depends_on": [
          "p3-flagship-s8-simbad-ned-crossmatch"
        ]
      },
      {
        "id": "p3-flagship-v2-enrichment",
        "depends_on": []
      },
      {
        "id": "p3-flagship-v2-allwise-photometry",
        "depends_on": [
          "p3-flagship-v2-enrichment"
        ]
      },
      {
        "id": "p3-flagship-v2-simbad-ned-crossmatch",
        "depends_on": [
          "p3-flagship-v2-enrichment"
        ]
      },
      {
        "id": "p3-flagship-v2-taxonomy",
        "depends_on": [
          "p3-flagship-v2-simbad-ned-crossmatch"
        ]
      },
      {
        "id": "anomaly-known-object-recovery-benchmark",
        "depends_on": []
      },
      {
        "id": "anomaly-known-object-recovery-benchmark-v2",
        "depends_on": [
          "p3-flagship-v2-enrichment"
        ]
      },
      {
        "id": "p3-ledger8-known-object-recovery-benchmark",
        "depends_on": [
          "p3-flagship-s8-enrichment"
        ]
      },
      {
        "id": "anomaly-map-png-highz-abundance",
        "depends_on": []
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
      "module_notes": "AUG-011 is complete and receipt-verified (36,634 groups; 27,547,223 unique TARGETIDs; 52,188 raw rows above the sealed S>5 threshold, all fibers including sky — NOT a science-candidate count; ~85% of the S>=8 tail are sky fibers per the 2026-09-03 provenance finding; science-target counts pending the provenance-filtered rerun). Its corpus is not present in this checkout and its named Hugging Face mirror returned unauthenticated/private 401, so Hubify must not present the completed corpus as anonymously forkable. Historical BigAE/H200 legs remain lineage, not live reproduction targets."
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
        "id": "p2-a2-bounce-fnl-transmission",
        "depends_on": [
          "p2-g1-dressedmetric-transmission"
        ]
      },
      {
        "id": "p2-a2-lane-a-cubic-vertex-table",
        "depends_on": [
          "p2-a2-bounce-fnl-transmission",
          "p2-fnl-adjudication-inin-from-scratch"
        ]
      },
      {
        "id": "p2-a2-lane-b-numerical-inin",
        "depends_on": [
          "p2-a2-lane-a-cubic-vertex-table",
          "p2-a2-bounce-fnl-transmission"
        ]
      },
      {
        "id": "p2-a3-lane-9b-s2-regularisation",
        "depends_on": [
          "p2-a2-lane-a-cubic-vertex-table",
          "p2-a2-lane-b-numerical-inin"
        ]
      },
      {
        "id": "p2-a3-lane-9b2-s2-rawadm",
        "depends_on": [
          "p2-a3-lane-9b-s2-regularisation",
          "p2-a2-lane-b-numerical-inin"
        ]
      },
      {
        "id": "p2-a3-row18a-s2-tensor-transfer",
        "depends_on": [
          "p2-a3-lane-9b2-s2-rawadm"
        ]
      },
      {
        "id": "p2-a3-lane-9a-velocity-dip",
        "depends_on": [
          "p2-a2-bounce-fnl-transmission",
          "p2-a2-lane-b-numerical-inin"
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
      },
      {
        "id": "p2-fnl-adjudication-inin-from-scratch",
        "depends_on": []
      },
      {
        "id": "p2-fnl-second-method-deltan",
        "depends_on": []
      },
      {
        "id": "a3-2-fnl-bianchi-separate-universe",
        "depends_on": [
          "p2-fnl-adjudication-inin-from-scratch",
          "p2-fnl-second-method-deltan"
        ]
      },
      {
        "id": "p2-fnl-monopole-adjudication",
        "depends_on": [
          "p2-fnl-adjudication-inin-from-scratch",
          "p2-fnl-second-method-deltan",
          "a3-2-fnl-bianchi-separate-universe"
        ]
      },
      {
        "id": "a3-pbh-compaction-fnl",
        "depends_on": []
      },
      {
        "id": "a3-pbh-abundance-fnl",
        "depends_on": []
      },
      {
        "id": "a3-pta-gamma-reproduction",
        "depends_on": []
      },
      {
        "id": "a3-pta-injection-30bin-2026-09-02",
        "depends_on": []
      },
      {
        "id": "a3-survey-reach-fnl",
        "depends_on": []
      },
      {
        "id": "a3-1b-inlab-delta2-zeta",
        "depends_on": [
          "a3-pbh-compaction-fnl",
          "p2-a2-bounce-fnl-transmission"
        ]
      },
      {
        "id": "a3-3-sigw-nhz-from-lab-spectrum",
        "depends_on": [
          "a3-1b-inlab-delta2-zeta",
          "p2-a2-bounce-fnl-transmission",
          "a3-pta-gamma-reproduction"
        ]
      },
      {
        "id": "a3-r5-15-tensor-omega-nhz",
        "depends_on": [
          "a3-3-sigw-nhz-from-lab-spectrum",
          "a3-pta-gamma-reproduction"
        ]
      },
      {
        "id": "a3-4-row10-r-ns",
        "depends_on": [
          "p2-a2-bounce-fnl-transmission",
          "a3-r5-15-tensor-omega-nhz",
          "a3-1b-inlab-delta2-zeta"
        ]
      },
      {
        "id": "a3-r5-18-gammacr-coverage",
        "depends_on": [
          "a3-pbh-compaction-fnl",
          "a3-1b-inlab-delta2-zeta"
        ]
      },
      {
        "id": "ledger9-c-abs-operator-map",
        "depends_on": [
          "p2-a2-lane-a-cubic-vertex-table",
          "a3-3-sigw-nhz-from-lab-spectrum",
          "a3-1b-inlab-delta2-zeta"
        ]
      },
      {
        "id": "ledger4-desi-dr1-lss-sanity",
        "depends_on": [
          "a3-survey-reach-fnl"
        ]
      },
      {
        "id": "ledger7-chiral-gw-delta-h",
        "depends_on": []
      },
      {
        "id": "ledger9-c2-lqc-exact-modes-inin",
        "depends_on": [
          "ledger9-c-abs-operator-map",
          "p2-a2-lane-a-cubic-vertex-table",
          "a3-1b-inlab-delta2-zeta"
        ]
      },
      {
        "id": "a3-row11a-choudhury-sign",
        "depends_on": [
          "a3-pbh-compaction-fnl",
          "a3-r5-18-gammacr-coverage",
          "a3-1b-inlab-delta2-zeta"
        ]
      },
      {
        "id": "row11c-threading-map-second-order",
        "depends_on": [
          "p2-fnl-monopole-adjudication"
        ]
      },
      {
        "id": "a3-row11b-gammacr-extension",
        "depends_on": [
          "a3-pbh-compaction-fnl",
          "a3-r5-18-gammacr-coverage",
          "a3-row11a-choudhury-sign"
        ]
      },
      {
        "id": "a3-row14-cs-window",
        "depends_on": [
          "a3-4-row10-r-ns",
          "p2-fnl-adjudication-inin-from-scratch"
        ]
      },
      {
        "id": "a3-row18b-cs-bounce-cubic",
        "depends_on": [
          "p2-a2-lane-b-numerical-inin",
          "p2-a2-lane-a-cubic-vertex-table",
          "a3-row14-cs-window"
        ]
      },
      {
        "id": "a3-row19-lambda",
        "depends_on": [
          "a3-row14-cs-window",
          "a3-row18b-cs-bounce-cubic",
          "p2-a2-lane-a-cubic-vertex-table"
        ]
      },
      {
        "id": "a3-row15-curvaton",
        "depends_on": [
          "a3-row14-cs-window",
          "a3-4-row10-r-ns"
        ]
      },
      {
        "id": "a3-row15-curvaton-adjudication",
        "depends_on": [
          "a3-row15-curvaton"
        ]
      },
      {
        "id": "a3-row15b-entropy-sector",
        "depends_on": [
          "a3-row15-curvaton",
          "p2-a3-row18a-s2-tensor-transfer"
        ]
      },
      {
        "id": "lift2-separate-universe-failure-criterion",
        "depends_on": []
      },
      {
        "id": "psu-gates-s1-s2-label-composition-criterion",
        "depends_on": [
          "lift2-separate-universe-failure-criterion"
        ]
      },
      {
        "id": "psu-gates-s6-s11-science-gates",
        "depends_on": [
          "psu-gates-s1-s2-label-composition-criterion"
        ]
      },
      {
        "id": "psu-gate-s7-cai-factor-2",
        "depends_on": [
          "psu-gates-s6-s11-science-gates"
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
        "id": "p4p-row16i-full-parent-dipole",
        "depends_on": [
          "p4-v2-vit-production-training",
          "p4-a95-dipole-injection-limit"
        ]
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
      },
      {
        "id": "p4prime-a95-neyman-cl-2026-09-02",
        "depends_on": []
      },
      {
        "id": "p4prime-bh-universe-dipole-exclusion",
        "depends_on": [
          "p4prime-a95-neyman-cl-2026-09-02"
        ]
      },
      {
        "id": "row16iv-chirality-structure",
        "depends_on": []
      },
      {
        "id": "p4p-row16ib-axis-shift",
        "depends_on": [
          "p4p-row16i-full-parent-dipole"
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
    "id": "a3-1b-inlab-delta2-zeta",
    "title": "A3-1b - the lab's own matter-bounce curvature power spectrum Delta^2_zeta(k) at PBH scales: delivered vs required amplitude in the compaction-function PBH criterion, and the COBE/FIRAS mu-distortion check on the early-SMBH seed amplitude",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Planck 2018 cosmological parameters (A_s = 2.1e-9 at k_* = 0.05 Mpc^-1; n_s = 0.9649 +/- 0.0042)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1807.06209",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Easson & Brandenberger 2012 - matter-bounce spectrum and tilt (n_s - 1 = 12w/(1+w))",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1206.2382",
        "checksum": null,
        "license": null
      },
      {
        "name": "Quintin, Sherkatghanad, Cai & Brandenberger 2015 - matter bounce spectrum, tilt, bounce growth",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1508.04141",
        "checksum": null,
        "license": null
      },
      {
        "name": "Agullo, Bolliet & Sreenath 2017 - LQC bounce enhancement of non-Gaussianity (checked, not imported)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1712.08148",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Zhu, Yan, Wang & Cai 2022/2023 (JCAP 01 (2023) 015) - PBH enhancement from non-linear processes around the bounce point (checked, not imported)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2207.14532",
        "checksum": null,
        "license": null
      },
      {
        "name": "Papanikolaou, Banerjee, Cai, Capozziello & Saridakis 2024 - PBHs by direct collapse in the contracting phase (recorded as new open item A3-1e)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2404.03779",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chluba, Erickcek & Ben-Dayan 2012 - mu-distortion window; Fixsen et al. 1996 COBE/FIRAS |mu| < 9e-5",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1203.2681",
        "checksum": null,
        "license": null
      },
      {
        "name": "Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025 - compaction-function PBH formalism implemented by the imported script",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2409.18983",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1 compaction-function PBH machinery (imported unmodified; only its module-level spectrum function is swapped and restored)",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/pbh_compaction_fnl.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear bounce transmission - eta_B per background, scale-independence of the transfer for k eta_B << 1",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.py",
        "entrypoint": "cd research/track_a3_multichannel && python3 inlab_delta2_zeta_2026-09-03.py",
        "sha256": "aca88410c4eff683dcd817e13a807c15eeac3a81d1b0883978af1328914278fe"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy 2.5.1 + scipy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-03",
      "wall_clock": "170 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~3 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). Must be run from research/track_a3_multichannel/ so that 'import pbh_compaction_fnl' resolves. The committed A3-1 script is imported, never edited: the run swaps only its module-level delta2_zeta and restores it (the script asserts the restore before writing outputs), so no A3-1 result changes. The lognormal-vs-power-law change of shape means 'A' here is Delta^2_zeta AT k_p, not a lognormal integrated amplitude - the two are not numerically interchangeable."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/inlab_delta2_zeta_2026-09-03.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/inlab_delta2_zeta_2026-09-03.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) k-mass anchor check k = 2.9e5 Mpc^-1 -> M_H = 166.18 Msun, i.e. M_PBH = gamma M_H = 33.2 Msun at gamma = 0.2 (literature ~30 Msun); (b) spectrum.branches['MB_anchored_ns0.9649'].implied_w_matter_bounce == -0.002920 +/- 1e-6 and Delta^2_zeta(1e13 Mpc^-1) == 6.611e-10 (rel. 1e-3); (c) per_mass_scale['M_H=1e20 g (asteroid window; the A3-1 mass)'] has k_p == 1.667e13 Mpc^-1, delivered == 6.493e-10, A_required(f_PBH=1e-3, -35/16) == 0.00636 and ratio == 9.79e6 (rel. 1e-2); (d) f_PBH_at_delivered_amplitude == 0.0 exactly at every mass and every f_NL; (e) threshold_sensitivity ratio A(-35/16)/A(-35/8) in [1.84, 1.90] for C_th in {0.4,0.5,0.6}; (f) ir_cutoff_sensitivity spans gamma_cr 0.267->0.630 and A(-35/16) 0.0064->0.0265 (factor <= 4.2); (g) mu_distortion.branches: mu == 1.654e-8 (ns=0.9649) and 2.242e-8 (pure dust), both ALLOWED at 1.8e-4 and 2.5e-4 of the FIRAS bound; (h) mu_distortion.required_amplitude_check.seeds: broadband mu ~ 1.6e-1 (~1.8e3 x FIRAS) for all four seed masses, narrow-peak mu 1.90e-6 / 3.18e-4 / 5.18e-3 / 1.89e-2 for 1e3/1e4/1e5/1e6 Msun; (i) verdict.does_the_lab_spectrum_make_PBHs == 'NO' with margin_log10_in_amplitude == 6.99 +/- 0.01.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3 (sub-item A3-1b) and item 6 (early-SMBH discriminator, previously BLOCKED on this result)",
      "research/track_a3_multichannel/PBH_COMPACTION_NOTE_2026-09-02.md section 8 (A3-1b opened there; deviation D1 is what this closes)",
      "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md section 4 (validity domain k eta_B << 1)",
      "directive Q2 (per-experiment reproducibility manifests), directive Q1 (pure-contribution framing: the result is stated as a null, not as a redo narrative), directive R1 (ledger-first)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-2-fnl-bianchi-separate-universe",
    "title": "A3-2: second-order Bianchi-I (anisotropic) separate-universe cross-check of the matter-contraction squeezed f_NL, including the long mode's shear",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "lab in-in adjudication (2026-09-02)",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md (commit aa2987cf)",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab second-method delta-N (2026-09-02)",
        "locator": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.md (commit d7dac953)",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "Maldacena 2003",
        "locator": "https://arxiv.org/abs/astro-ph/0210603",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Namjoo, Firouzjahi & Sasaki 2012",
        "locator": "https://arxiv.org/abs/1210.3692",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Pajer, Schmidt & Zaldarriaga 2013; Dai, Pajer & Schmidt 2015",
        "locator": "https://arxiv.org/abs/1305.0824 ; https://arxiv.org/abs/1504.00351",
        "type": "external-literature",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.py",
        "entrypoint": "python3 research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.py",
        "sha256": "cc393a1236869745236923a90e168b6126a21f9011eeb38f5d6a47079fa2aac4"
      }
    ],
    "environment": {
      "python": "python3 with sympy (>=1.12; run on sympy 1.14.0)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-03",
      "wall_clock": "4 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 minute",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic exact-rational sympy. No network access at run time. The script self-validates: eps recovered from H; the growing mode solves d/dt(a^3 eps zetadot)=0; the isotropic projection response equals (1-n_s) zeta_L (consistency relation); the attractor limit gives (5/12)(1-n_s) with no quadrupole; the shear vanishes as eps -> 0 (USR); the second-order delta-N ODE residual is identically zero."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required exact values: growing_mode.zetadot_over_H_zeta == 'epsilon - 3'; anisotropy['beta_z / zeta_L'] == '2*epsilon*s_conv/3'; delta_N_comoving.f_NL_comoving_general_eps == '-5'; projection.isotropic_part == '1 - n_s'; result['f_total(mu)_eps_3_2_sconv_+1'] == '15*mu**2/8 - 45/8'; result.monopole == '-5'; result.mu2_coefficient == '15/8'; comparison.ratio_mu2_coefficients == '2'; comparison.monopole_gap == '-25/8'; comparison.shear_monopole_contribution == '0'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 1 (open item: 'second-order Bianchi-I separate-universe check of the shear response') and row 3 (A3-2 method-independent f_NL check)",
      "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md, 'What remains open'",
      "directive R (vision governance) and directive Q2 (reproducibility manifests)",
      "input 'lab in-in adjudication (2026-09-02)' (research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md (commit aa2987cf)) used for: the open item this work executes; the comparison values f(mu) = -35/16 + (15/16) mu^2, monopole -15/8, comoving delta-N -5, and the quoted shear sign convention — all used only AFTER the computation",
      "input 'lab second-method delta-N (2026-09-02)' (research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.md (commit d7dac953)) used for: separate-universe system (exponential potential, x/Y variables) and the -55/16 uniform-density value",
      "input 'Maldacena 2003' (https://arxiv.org/abs/astro-ph/0210603) used for: comoving gauge ADM variables, psi = -zeta/H + a^2 eps grad^{-2} zetadot; consistency-relation normalisation used as a VALIDATION",
      "input 'Namjoo, Firouzjahi & Sasaki 2012' (https://arxiv.org/abs/1210.3692) used for: ultra-slow-roll non-attractor benchmark: f_NL = 5/2 with no angular dependence, used to VALIDATE that the shear term vanishes as eps -> 0",
      "input 'Pajer, Schmidt & Zaldarriaga 2013; Dai, Pajer & Schmidt 2015' (https://arxiv.org/abs/1305.0824 ; https://arxiv.org/abs/1504.00351) used for: conformal-Fermi-coordinate / separate-universe-with-shear framework; their attractor-only validity is recorded as the identified incompleteness"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-3-sigw-nhz-from-lab-spectrum",
    "title": "A3-3 - scalar-induced gravitational waves in the NANOGrav band from the lab's own curvature power spectrum: does the CMB-anchored matter-bounce spectrum give the paper's Channel-I gamma = 3?",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Planck 2018 cosmological parameters (A_s = 2.1e-9 at k_* = 0.05 Mpc^-1; n_s = 0.9649)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1807.06209",
        "checksum": null,
        "license": null
      },
      {
        "name": "Kohri & Terada 2018 - radiation-era induced-GW kernel, oscillation-averaged x^2 <I^2> (the transfer used here)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1804.08577",
        "checksum": null,
        "license": null
      },
      {
        "name": "Domenech 2021 - scalar-induced GW review; Eq. (2.21) kernel form and the Omega_GW ~ f^{2n} rule for broad P_R ~ k^n in RD",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2109.01398",
        "checksum": null,
        "license": null
      },
      {
        "name": "Espinosa, Racco & Riotto 2018 - closed-form Omega_GW = 0.8222 A^2 for scale-invariant P_zeta = A (the kernel-normalisation benchmark asserted at runtime)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1804.07732",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Pi & Sasaki 2020 - universal IR causal tail Omega_GW ~ f^3 (gamma = 2), cited to show gamma = 3 is not the causal floor",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1909.13728",
        "checksum": null,
        "license": null
      },
      {
        "name": "NANOGrav 15 yr - HD-correlated power law A = 2.4e-15 at f_yr, gamma = 3.2 (+/-0.6 at 90%)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2306.16213",
        "checksum": null,
        "license": null
      },
      {
        "name": "Papanikolaou 2025 - the source whose low-k P_R ~ k tail the paper's section IV D borrows for gamma = 3 (contrast case; its spectrum carries a small-scale enhancement)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2504.11641",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1b lab curvature spectrum Delta^2_zeta(k) - the exact spectrum evaluated here",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/outputs/inlab_delta2_zeta_2026-09-03.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear bounce transmission - eta_B per background; scale-independence of the transfer for k eta_B << 1 (validity test in section 3 of the note)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "The paper's own gamma convention Omega_GW ~ f^{5-gamma}",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/pta_gamma_reproduce.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/sigw_nhz_from_lab_spectrum_2026_09_04.py",
        "entrypoint": "cd research/track_a3_multichannel && python3 sigw_nhz_from_lab_spectrum_2026_09_04.py",
        "sha256": "6c8efd80b212455e06a148fbc77819c16b53f4b1e064da0cf6b088d3737722da"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy 2.5.1 + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "3.2 s (measured, field wall_seconds in the output JSON)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~5 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). The kernel normalisation is asserted against the published scale-invariant benchmark at the top of main() BEFORE any lab spectrum is inserted, so a normalisation regression aborts the run rather than propagating. Nothing is tuned toward gamma = 3. The double integral is a fixed 1200x1200 grid over ln v in [1e-3, 300]; the benchmark is stable to 0.05% across grids from 400x400/vmax=50 to 2000x2000/vmax=2000."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/sigw_nhz_from_lab_spectrum_2026_09_04.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/sigw_nhz_2026_09_04.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) kernel_validation.computed_coefficient == 0.82254 vs published 0.8222, rel_error < 1e-3 (this assertion is executed in main() and aborts on failure); (b) f_to_k.k_per_nHz_Mpc-1 == 646710.2 (i.e. k = 6.467e5 Mpc^-1 per nHz, so k(10 nHz) = 6.47e6 Mpc^-1, matching the R4 audit's independent 6.5e6 figure), k_at_f_yr == 2.0493e7; (c) transfer_validity.k_eta_B_at_60nHz <= 2.264e-8 for every T_B >= 1e8 GeV, i.e. the whole PTA band is deep inside the A2 scale-independent domain; (d) branches['MB_anchored_ns0.9649'].gamma_pred == 5.0702 and branches['pure_dust_ns1'].gamma_pred == 5.0000, each matching gamma_pred_analytic_2(ns-1)+5 to 1e-4; (e) z_vs_NANOGrav_official_gamma == 5.13 and 4.93 respectively; (f) log10_amplitude_shortfall_vs_NANOGrav_at_f_yr == 14.34 (ns=0.9649) and 13.74 (pure dust); (g) what_would_give_gamma3.required_spectral_index_of_P_R_at_nHz == 1.0, log10_amplitude_gap == 7.197, T_B_needed_GeV == 2.264 and decades_below_section_V == 7.645; (h) verdict.answer == 'A'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 3 (item A3-3)",
      "project-context/peer-reviews/INT_v3/A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md item DA3M-R4-02 (MAJOR, SCIENCE; closure plan (ii)) - this experiment is that item's closure evidence",
      "research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md (derivation summary, tables, and VERDICT A)",
      "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md section 4 (validity domain k eta_B << 1)",
      "directive Q2 (per-experiment reproducibility manifests), directive Q1 (the result is stated as a null in its own terms, not as a redo narrative), directive R1 (ledger-first)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-4-row10-r-ns",
    "title": "Ledger row 10 (A3-4 + A3-ns) - the matter bounce's OWN tensor-to-scalar ratio r and scalar tilt n_s, derived for the dust contraction and propagated through all three A2 bounce backgrounds",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Cai, Easson & Brandenberger 2012 - nonsingular bouncing cosmology; the matter bounce's known large tensor-to-scalar ratio",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1206.2382",
        "checksum": null,
        "license": null
      },
      {
        "name": "Quintin, Sherkatghanad, Cai & Brandenberger 2015 - perturbations through a nonsingular bounce; single-field matter-bounce no-go trading r against f_NL",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1508.04141",
        "checksum": null,
        "license": null
      },
      {
        "name": "Wands 1999 - dust-contraction / de Sitter duality making the contracting spectra scale-invariant",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/gr-qc/9809062",
        "checksum": null,
        "license": null
      },
      {
        "name": "Brandenberger & Peter 2016 - bouncing cosmologies review",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1603.05834",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ade et al. (BICEP/Keck) 2021 - r < 0.036 (95% CL) at k_* = 0.05 Mpc^-1, the bound the model is tested against",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2018 - n_s = 0.9649, A_s = 2.1e-9, the anchor (not a prediction) for the tilt branch",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1807.06209",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear-transmission module - the three bounce backgrounds (LQC-effective dust, poly-analytic non-LQC, Quintin2015-type), the adiabatic-vacuum scalar evolution and the exact matter-basis projection, imported directly",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "First-order tensor Omega_GW at nHz - re-run with the model's own r as CASE C",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/r5_15_tensor_omega_nhz.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row10_r_ns/row10_r_ns.py",
        "entrypoint": "cd research/track_a3_multichannel/row10_r_ns && python3 row10_r_ns.py",
        "sha256": "4554ac9add31704f973be6b4118d3c814aad2e15baa4b9f7db591eacc63d54b3"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy + scipy + sympy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "1.5 s (measured, field wall_seconds in results.json)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~3 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). The symbolic block derives r = 16 eps and n_s - 1 = 12w/(1+3w) with sympy rather than asserting them. The tensor mode is integrated in h-form, an independent numerical route from A2's mu-form scalar integration, so T_h/T_zeta = 1 is a genuine numerical check and not an identity of the code. Nothing is tuned; no free parameter enters r."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row10_r_ns/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row10_r_ns/row10_r_ns.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row10_r_ns/row10_r_ns.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row10_r_ns/ROW10_R_NS_2026-09-04.md",
        "type": "document",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/r5_15b_tensor_omega_nhz_model_r_2026_09_04.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) analytic.r_symbolic == '16*epsilon' and analytic.ns_minus_1_of_w == '12*w/(3*w + 1)' (both derived symbolically); (b) analytic.pure_dust.r == 24.0 and analytic.planck_anchored.w == -0.0028996 with r == 23.9304; (c) numeric_summary.max_abs_T_h_over_T_zeta_minus_1_all_backgrounds <= 1e-4 (poly 8.5e-9, LQC 1.0e-9, Quintin 8.0e-5), i.e. the tensor and scalar transfers through every bounce agree; (d) backgrounds.{poly,LQC,quintin}.r_after_median == 24.0000/24.0000/23.9962, so r is bounce-invariant; (e) cmb_verdict.ratio_model_over_bound == 664.7, verdict == CMB TENSION; (f) the CASE C rows in r5_15b_tensor_omega_nhz_model_r_2026_09_04.json give Omega_GW1 h^2(f_yr) = 1.691e-14 with log10 shortfall vs NANOGrav 5.33, so the PTA null of A3-3 is unchanged.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 10 (A3-4 + A3-ns), promoted 2026-09-04 by the R6 audit item R6-10",
      "research/track_a3_multichannel/row10_r_ns/ROW10_R_NS_2026-09-04.md (derivation, per-background table, CMB verdict, paper-ready sentences)",
      "research/cubic_bounce_transmission/a2_transmission_linear.py (backgrounds and scalar mode machinery, imported not copied)",
      "directive Q2 (per-experiment reproducibility manifests); directive Q1 (the CMB tension is stated in its own terms as a limitation of the modelled background, not narrated as a fix of an earlier error)",
      "provenance finding: the tensor-sense r = 0.84 at r5_15_tensor_omega_nhz.py:73,98 and paper/main.tex:769 is a conflation of P2's noise-weighted bispectrum shape overlap R_OVERLAP = 0.84 (survey_reach_fnl.py:46) with the tensor-to-scalar ratio; no in-repo derivation of a tensor r = 0.84 exists"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-pbh-abundance-fnl",
    "title": "Track A3 channel 2 — Press-Schechter PBH abundance with local quadratic non-Gaussianity at f_NL = -35/16 vs -35/8 vs 0",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [],
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
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3",
      "project-context/bounce_portfolio_strategy.md (Track C, Choudhury+ 2025)",
      "research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-pbh-compaction-fnl",
    "title": "Track A3 item A3-1 — compaction-function PBH abundance with local non-Gaussianity at f_NL = -35/16 vs -35/8 vs 0 (Choudhury et al. 2025 formalism)",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/pbh_compaction_fnl.py",
        "entrypoint": "python3 research/track_a3_multichannel/pbh_compaction_fnl.py",
        "sha256": "27e4021f84b8607acc5da0811f4cacf030d5068464457b5534a647ba6a39de38"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + scipy 1.18.0 + matplotlib (repo requirements.txt subset)",
      "hardware": "cpu-only; Apple M5, 24 GB RAM, macOS 26.5 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (Apple M5)",
      "date": "2026-09-02",
      "wall_clock": "215 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~4 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Pure numpy/scipy, deterministic (no RNG). Implements Choudhury et al. 2025 (arXiv:2409.18983, EPJC 85:472) Eqs. 30/31/34/35/40/41/48-56/60-66. NOT a full reproduction: their regularized-renormalized-resummed EFT-of-bounce + USR curvature spectrum is not reconstructible from the published paper (no closed-form Delta^2_zeta(k), no loop-counterterm normalisation, no tabulated EFT coefficients or k_s/k_e/Delta N_USR values), so a lognormal stand-in is used and the amplitude is scanned. Supersedes a3-pbh-abundance-fnl (Press-Schechter quadratic map), whose conclusion this run REVERSES."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/pbh_compaction_fnl.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/pbh_compaction_fnl.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/PBH_COMPACTION_NOTE_2026-09-02.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) the 2-D grid reproduces the exact 1-D Gaussian quadrature to <3% at A = 0.05, 0.1314, 0.2; (b) f(w) = 2/3, C_max = 2/3, and C_lin- = 0.666667 at C_th = 0.5; (c) at C_th = 0.5, Delta = 0.5, r_p k_p = 1 with A* = 0.131446 (Gaussian f_PBH = 1): f_PBH = 3.62e-14 at -35/16 and 1.57e-2 at -35/8, i.e. f_PBH(-35/16) < f_PBH(-35/8), the REVERSE of the Press-Schechter first pass; (d) the amplitude ratio A(-35/16)/A(-35/8) for f_PBH = 1e-3 is 1.732 with range [1.610, 1.809] and std 0.050 over the 27-point (Delta, r_p k_p, C_th) grid.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3, open sub-item A3-1",
      "research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md section 2.5",
      "research/track_a3_multichannel/PBH_COMPACTION_NOTE_2026-09-02.md",
      "supersedes reproducibility/manifests/experiments/a3-pbh-abundance-fnl.json",
      "Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025, arXiv:2409.18983, EPJC 85:472",
      "Young, Byrnes & Sasaki 2019, arXiv:1904.00984; Musco 2019, arXiv:1809.02127"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-pta-gamma-reproduction",
    "title": "Track A3 channel 1 — reproduction of the NANOGrav 15-yr free-spectrum gamma posterior and Savage-Dickey Bayes factors from the committed chain",
    "program": "bounce-theory",
    "paper": "A3",
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
        "name": "committed reference summaries for the diff (results.json + savage_dickey_2026-05-29.json in this dir)",
        "type": "internal-artifact",
        "locator": "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/",
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
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 3",
      "research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-pta-injection-30bin-2026-09-02",
    "title": "Track A3 §IV C closure (DA3M-R2-01) — injection-recovery test at gamma=13/3 and gamma=3 through the same 30-bin free-spectrum interpolated-density likelihood/priors as emcee_freespec.py",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "validation",
    "inputs": [],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/pta_injection_30bin_2026_09_02.py",
        "entrypoint": "python3 research/track_a3_multichannel/pta_injection_30bin_2026_09_02.py",
        "sha256": "e3c893046297a17ef0aa7e29ae0db379a7c72011cdc756bcbcfb3050ad8d07aa"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.2 + emcee 3.1.6 (emcee imported for parity with pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py; the recovery itself uses a dense 2D grid marginalization of the identical log_prior/log_likelihood, not emcee sampling — see 'method' note below)",
      "hardware": "cpu-only; Apple M5, 24 GB RAM, macOS 26.5 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (Apple M5)",
      "date": "2026-09-02",
      "wall_clock": "5.8 s (measured, 10 realizations)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "6 s (measured)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "model_log10rho(theta), log_prior(theta) and the 30-bin/T_obs=16.03yr geometry and gamma~U[0,7], log10_A~U[-18,-11] priors are copied verbatim from pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py. The ONE substitution: the real NANOGrav 15-yr KDE density grids (Zenodo 8060824) live only on the RunPod workspace that built emcee_freespec.py's inputs and are not present in this repo or on this machine, so this script synthesizes a per-bin Gaussian log-density (sigma=0.22 dex, representative of the real KDE per-bin posterior width) centered on a noisy injected observation at the chosen true (gamma, log10_A). Recovery is by exact dense 2D grid (1200x900) posterior marginalization of the identical log_prior+log_likelihood rather than emcee ensemble sampling: a preliminary emcee run on this strongly-degenerate 2D ridge showed near-zero acceptance (a known ensemble-sampler failure mode on ridge-shaped 2D posteriors, not evidence of pipeline bias), while the dense grid is an exact, faster, and more reliable computation of the same posterior for a 2-parameter problem. 5 realizations per gamma_true (10 total)."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/pta_injection_30bin_2026_09_02.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: mean recovered gamma at gamma_true=13/3=4.3333 is 4.328 +/- (realization scatter 0.48), mean pull -0.026sigma over 5 realizations; at gamma_true=3.0, mean recovered 3.015, mean pull +0.068sigma over 5 realizations. Both consistent with unbiased recovery at the <0.1sigma level, replacing the paper's prior unverified claim of a -0.018sigma pull from a different (6-bin, Gaussian chi-squared, gamma=3.2-injected) pipeline that DA3M-R2-01 found was misdescribed as 'the identical pipeline' injected at 13/3.",
    "status": "runnable-now",
    "provenance": [
      "project-context/peer-reviews/INT_v3/ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY/A3M_v3M.0.4_R2_truth_audit.md finding #1 / DA3M-R2-01",
      "project-context/peer-reviews/DISPOSITIONS/A3M.md DA3M-R2-01",
      "research/track_a3_multichannel/paper/main.tex §IV C"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-r5-15-tensor-omega-nhz",
    "title": "A3M R5-15 - the model's own FIRST-ORDER (primordial) tensor Omega_GW h^2 in the NANOGrav band, compared with the scalar-induced background and with NANOGrav: which dominates, and does the PTA null change?",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Ade et al. (BICEP/Keck + Planck) 2021 - r < 0.036 (95% CL) at k_* = 0.05 Mpc^-1; CASE A tensor amplitude (an UPPER LIMIT)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      },
      {
        "name": "Watanabe & Komatsu 2006 - radiation-era propagation of a first-order tensor mode; Omega_GW = P_T/24 deep inside the horizon",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0604176",
        "checksum": null,
        "license": null
      },
      {
        "name": "Caprini & Figueroa 2018 - cosmological GW background review, Sec. 2 (same propagation and the g_* transfer factor)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1801.04268",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2018 - A_s = 2.1e-9 at k_* = 0.05 Mpc^-1, n_s = 0.9649 (the background from which n_T = n_s - 1 is taken)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1807.06209",
        "checksum": null,
        "license": null
      },
      {
        "name": "NANOGrav 15 yr - HD-correlated power law, Omega_GW h^2(f_yr) = 3.6235e-9 (the comparison target)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2306.16213",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai et al. 2009 matter-bounce r = 0.84 - CASE B scenario only; this program's OPEN item A3-4 (re-derivation unresolved)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/0810.4677",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-3 induced (second-order) background: Omega_GW h^2(f_yr) = 1.4545e-23 (anchored) / 5.8764e-23 (dust) - the comparator this item is measured against, and the source of the identical f<->k map and transfer prefactor",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "The paper's gamma convention Omega_GW ~ f^{5-gamma} and its 'prim. tensors n_T = 0' Table II row",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/pta_gamma_reproduce.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/r5_15_tensor_omega_nhz.py",
        "entrypoint": "cd research/track_a3_multichannel && python3 r5_15_tensor_omega_nhz.py",
        "sha256": "25123c89cbfcb8cac0992212faf53966c92d56da2c8d786dd315fc064c469fae"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy 2.5.1",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "<0.01 s (measured, field wall_seconds in the output JSON)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~1 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline, deterministic, closed-form (no RNG, no data files, no network, no quadrature). Nothing is tuned: r is a published CMB upper bound (CASE A) or the program's own open literature value (CASE B, labelled a scenario); the transfer prefactor 1.62e-5 (g_*/106.75)^{-1/3} is copied verbatim from the companion induced-GW script whose kernel normalisation is already validated against a published benchmark. A g_* = 20 variant (nHz horizon entry, T ~ 0.2 GeV) is carried in every case row as a x1.75 sensitivity."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/r5_15_tensor_omega_nhz.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/R5_15_TENSOR_NOTE_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) cases['A_CMB_bound_r0.036|MB_anchored_ns0.9649'].Omega_GW1_h2_at_f_yr == 2.544e-17 with log10_ratio_first_order_over_induced_at_f_yr == 6.243 and log10_shortfall_vs_NANOGrav_at_f_yr == 8.154; (b) the pure-dust CASE A row gives 5.103e-17, ratio 5.939, shortfall 7.851; (c) CASE B (r = 0.84) gives 5.936e-16 (anchored) and 1.191e-15 (dust), shortfalls 6.786 and 6.483; (d) gamma_pred_first_order == 5.0351 (n_T = n_s - 1) and 5.0000 (dust), i.e. within 0.04 of the induced gamma_pred = 5.0702; (e) every g_star20_variant row is x1.75 its baseline; (f) verdict.does_the_PTA_null_change begins 'NO.'",
    "status": "runnable-now",
    "provenance": [
      "project-context/peer-reviews/INT_v3/A3M_v3M.0.11_R5_TRUTH_AUDIT_2026-09-04.md item DA3M-R5-15 (MINOR-SCIENCE; closure plan (ii)) - this experiment is that item's closure evidence",
      "research/track_a3_multichannel/outputs/R5_15_TENSOR_NOTE_2026-09-04.md (method, table, and the sentence the paper may state)",
      "research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md (the second-order comparator this result is measured against)",
      "directive Q2 (per-experiment reproducibility manifests), directive Q1 (the result is stated in its own terms as a null, not as a redo narrative), directive R1 (ledger-first)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-r5-18-gammacr-coverage",
    "title": "A3M R5-18 - gamma_cr coverage of the 27-point PBH (Delta, r_p k_p, C_th) grid: how many points sit on the enhancement branch (gamma_cr <= 0.85), and is the quoted 1.7-1.9 required-amplitude ratio inside the scanned coverage?",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025 - gamma_cr = sigma_cr^2/(sigma_c sigma_r), Eq. 50; the compaction-function formalism the grid implements, and the source of the unresolved sign disagreement the ratio is conditional on",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2409.18983",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1 compaction-function PBH grid - the 27 (Delta, r_p k_p, C_th) points with gamma_cr and ratio_-35/16_over_-35/8 (robust_amplitude_requirement_grid)",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/outputs/pbh_compaction_fnl.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1b in-lab curvature spectrum - gamma_cr of the lab's own near-scale-invariant shape over the IR-cutoff scan (ir_cutoff_sensitivity)",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/outputs/inlab_delta2_zeta_2026-09-03.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1b note - the 1.85-1.89 ratio at the in-lab shape and the observation that it lies outside the grid's [1.610, 1.809]",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1 note - the sign-flip statement (enhancement at gamma_cr <~ 0.85, suppression above), step (4) of the generating script",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/PBH_COMPACTION_NOTE_2026-09-02.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/r5_18_gammacr_coverage.py",
        "entrypoint": "cd research/track_a3_multichannel && python3 r5_18_gammacr_coverage.py",
        "sha256": "17dbba072f883f47dfc8e8113fa069a0fd77360d4d163320a3ee5b7f2214dc28"
      }
    ],
    "environment": {
      "python": "python3.14.6 (stdlib only; no numpy required)",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "<0.01 s (measured, field wall_seconds in the output JSON)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~1 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic re-reading of two COMMITTED result JSONs. No physics is re-derived, no integral re-run, no parameter fitted: the script tabulates gamma_cr and the required-amplitude ratio already stored per grid point, counts how many fall at or below the 0.85 sign-flip scale, and compares the covered range with the in-lab shape's gamma_cr. Regenerating the two input JSONs (a3-pbh-compaction-fnl, a3-1b-inlab-delta2-zeta) is the upstream reproduction path."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/outputs/r5_18_gammacr_coverage.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/outputs/R5_18_GAMMACR_NOTE_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) n_points == 27 and n_distinct_gamma_cr == 9 (gamma_cr is C_th-independent, so each shape value repeats over C_th in {0.4,0.5,0.6}); (b) gamma_cr_covered_range == [0.76604, 0.96752]; (c) n_points_at_or_below_flip == 9, at gamma_cr in {0.766037, 0.807754, 0.846110} -- i.e. the grid straddles the 0.85 sign-flip scale; (d) ratio_range_over_grid == [1.6097, 1.8086], consistent with the committed headline 1.7320 +- 0.0502 (n=27); (e) inlab_gamma_cr_range == [0.26681, 0.62979] and inlab_inside_grid_coverage == false, i.e. the lab's own spectrum shape sits ENTIRELY BELOW the scanned coverage; (f) verdict.is_the_quoted_ratio_inside_coverage begins 'NO for the lab's own spectrum shape.'",
    "status": "runnable-now",
    "provenance": [
      "project-context/peer-reviews/INT_v3/A3M_v3M.0.11_R5_TRUTH_AUDIT_2026-09-04.md item DA3M-R5-18 (residual of Fable M5; closure plan (ii)-lite) - this experiment is that item's closure evidence",
      "research/track_a3_multichannel/outputs/R5_18_GAMMACR_NOTE_2026-09-04.md (per-point table and the sentence the paper may state)",
      "research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md (open item A3-1d: the in-lab shape reaches the enhancement branch by a physically-motivated shape, not only by grid corners)",
      "directive Q2 (per-experiment reproducibility manifests), directive Q1 (result stated in its own terms), directive R1 (ledger-first)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row11a-choudhury-sign",
    "title": "A3M ledger row 11(a) - operator-by-operator location of the Choudhury et al. 2025 compaction-function f_NL sign disagreement: does negative local f_NL suppress or enhance the PBH abundance at fixed Gaussian amplitude?",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025, 'Negative non-Gaussianity as a salvager for PBHs with PTAs in bounce', EPJC 85:472 - the compaction-function + local-f_NL formalism (Eqs. 30, 35, 40, 49-54, 60-66) whose f_NL sign response is under test; full text states 'f_NL<0 is considered more favourable to suppress the PBH abundance', with a sharply peaked USR/RRR spectrum",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2409.18983",
        "checksum": null,
        "license": null
      },
      {
        "name": "Kitajima, Tada, Yokoyama & Yoo 2021, 'Primordial black holes in peak theory with a non-Gaussian tail' - the averaged-compaction PBH criterion with critical scaling, the standard treatment the operator chain is checked against",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2109.00791",
        "checksum": null,
        "license": null
      },
      {
        "name": "Young & Byrnes 2013, 'Signatures of non-Gaussianity in the isocurvature modes of primordial black hole dark matter' - the standard local-f_NL PBH abundance treatment and the long-wavelength-mode modulation argument",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1307.4995",
        "checksum": null,
        "license": null
      },
      {
        "name": "Franciolini, Kehagias, Matarrese & Riotto 2018, 'Primordial black holes from inflation and non-Gaussianity'",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1801.09415",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1 compaction-function integrator (Eqs. 52-54 covariances, Eq. 60 abundance) - imported unmodified as the numerical engine",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/pbh_compaction_fnl.py",
        "checksum": "27e4021f84b8607acc5da0811f4cacf030d5068464457b5534a647ba6a39de38",
        "license": null
      },
      {
        "name": "A3-1 note - the enhancement-at-gamma_cr<~0.85 statement (sec 4.3) this item adjudicates",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/PBH_COMPACTION_NOTE_2026-09-02.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "R5-18 gamma_cr coverage note - the in-lab shape's gamma_cr in [0.267, 0.630] and the standing of the quoted 1.7-1.9 ratio",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/outputs/R5_18_GAMMACR_NOTE_2026-09-04.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row11_pbh_residuals/row11_choudhury_sign.py",
        "entrypoint": "cd research/track_a3_multichannel/row11_pbh_residuals && python3 row11_choudhury_sign.py",
        "sha256": "b0274f1669bfd3c68d99e8158c23735e922655e6f7a63289eaa6c6a4dfa62bcf"
      }
    ],
    "environment": {
      "python": "python3 + numpy/scipy/matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "~9 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~10 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic. Part (A) minimises the compaction-threshold saddle exponent S(x)=x^2/2+(nu/(1+eps x)-g x)^2/(2(1-g^2)) by bounded 1-D minimisation and compares finite-difference eps-derivatives with the analytic coefficients -g nu^3 and nu^4(6g^2-1). Part (B) calls the COMMITTED beta_ng/A_for_fpbh integrator unmodified. Part (C) monkeypatches only the spectrum shape (a power law with an explicit IR cutoff) and restores it in a finally block. No fitting, no tuning: the amplitude at each shape is SOLVED for from the fixed condition f_PBH(Gaussian)=1."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/results/row11_choudhury_sign.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/ROW11_PBH_RESIDUALS_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) max_relative_error_d2S < 0.05, i.e. the numeric second eps-derivative of S_min reproduces nu^4(6 gamma_cr^2 - 1) at every (nu, g) checked; (b) gamma_cr_sign_flip_analytic == 1/sqrt(6) = 0.40825; (c) in full_beta_shape_scan, beta/beta_gauss < 1 at f_NL = -0.02 for EVERY gamma_cr including 0.305 (the O(eps) term suppresses universally); (d) beta/beta_gauss > 1 at f_NL = -35/16 only for gamma_cr <= 0.766; (e) in ir_sensitivity, sigma_cr2_over_sigma_c is constant to 5 significant figures (0.31921) over k_min/k_p from 1e-5 to 1e-2 while sigma_r changes by a factor 1.67 and gamma_cr moves 0.267 -> 0.446.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 11 - this experiment is that row's closure evidence",
      "project-context/peer-reviews/INT_v3/A3M_v3M.0.13_R6_TRUTH_AUDIT_2026-09-04.md sec 4 class (e): 'the Choudhury et al. gamma_cr<~0.85 sign disagreement (:929-930, a genuine discrepancy left unresolved)'",
      "directive Q2 (per-experiment reproducibility manifests), directive R1 (ledger-first), directive R6 (evidence-graded claims)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row11b-gammacr-extension",
    "title": "A3M ledger row 11(b) - compaction-function scan extended to gamma_cr in [0.2, 1.0]: the required-amplitude ratio A(-35/16)/A(-35/8) INSIDE the in-lab spectrum shape's own coverage [0.267, 0.630], and whether the quoted '1.7-1.9' survives",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Choudhury, Dey, Ganguly, Karde, Singh & Tiwari 2025, 'Negative non-Gaussianity as a salvager for PBHs with PTAs in bounce', EPJC 85:472 - the compaction-function + local-f_NL formalism (Eqs. 30, 35, 40, 49-54, 60-66) whose f_NL sign response is under test; full text states 'f_NL<0 is considered more favourable to suppress the PBH abundance', with a sharply peaked USR/RRR spectrum",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2409.18983",
        "checksum": null,
        "license": null
      },
      {
        "name": "Kitajima, Tada, Yokoyama & Yoo 2021, 'Primordial black holes in peak theory with a non-Gaussian tail' - the averaged-compaction PBH criterion with critical scaling, the standard treatment the operator chain is checked against",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2109.00791",
        "checksum": null,
        "license": null
      },
      {
        "name": "Young & Byrnes 2013, 'Signatures of non-Gaussianity in the isocurvature modes of primordial black hole dark matter' - the standard local-f_NL PBH abundance treatment and the long-wavelength-mode modulation argument",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1307.4995",
        "checksum": null,
        "license": null
      },
      {
        "name": "Franciolini, Kehagias, Matarrese & Riotto 2018, 'Primordial black holes from inflation and non-Gaussianity'",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1801.09415",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1 compaction-function integrator (Eqs. 52-54 covariances, Eq. 60 abundance) - imported unmodified as the numerical engine",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/pbh_compaction_fnl.py",
        "checksum": "27e4021f84b8607acc5da0811f4cacf030d5068464457b5534a647ba6a39de38",
        "license": null
      },
      {
        "name": "A3-1 note - the enhancement-at-gamma_cr<~0.85 statement (sec 4.3) this item adjudicates",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/PBH_COMPACTION_NOTE_2026-09-02.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "R5-18 gamma_cr coverage note - the in-lab shape's gamma_cr in [0.267, 0.630] and the standing of the quoted 1.7-1.9 ratio",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/outputs/R5_18_GAMMACR_NOTE_2026-09-04.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Row 11(a) sign adjudication - establishes that gamma_cr controls the sign of the f_NL response, hence that the ratio must be quoted inside the in-lab gamma_cr coverage",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/results/row11_choudhury_sign.json",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row11_pbh_residuals/row11_gammacr_extension.py",
        "entrypoint": "cd research/track_a3_multichannel/row11_pbh_residuals && python3 row11_gammacr_extension.py",
        "sha256": "a0c01e1598295d59f577dd1147afecd12d2151c76a51c28d07ad30c8db4daf28"
      }
    ],
    "environment": {
      "python": "python3 + numpy/scipy/matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "~20-40 min (measured; field in the output JSON print line)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~30 min",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Deterministic. Two shape families (lognormal(Delta, r_p k_p) extended to broad Delta; the in-lab power law Delta^2 = A (k/k_p)^{n_s-1} with an explicit IR cutoff) are pushed through the COMMITTED beta_ng/A_for_fpbh integrator, with PC.covariances temporarily replaced by _cov_wide - the SAME Eqs. 52-54 integrals on a k-grid widened from [1e-5,1e3] k_p to [1e-9,1e3] k_p, which is what lets gamma_cr reach 0.2. _cov_wide is asserted against the committed integrator (max rel. diff < 1e-6) before any scan point is taken, and both PC.covariances and PC.delta2_zeta are restored in a finally block. NOTHING IS TUNED: at every point the amplitude A is solved by brentq from the fixed target f_PBH = 1e-3 (the floor of the Choudhury et al. band); the ratio is a property of the solution. Committed outputs (outputs/pbh_compaction_fnl.json) are not touched."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/results/row11_gammacr_extension.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/results/row11_gammacr_extension.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/results/row11_gammacr_extension.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row11_pbh_residuals/ROW11_PBH_RESIDUALS_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) wide_integrator_validation_max_rel_diff < 1e-6 (the assert is in the script); (b) the union of scan points covers gamma_cr from <=0.2 to >=0.96, i.e. the [0.2,1.0] target the committed 27-point grid ([0.766,0.968]) does not reach; (c) summary.committed_grid_coverage reproduces the committed headline 1.732 +- 0.050 over gamma_cr in [0.766,0.968]; (d) summary.inlab_coverage reports the ratio over gamma_cr in [0.267,0.630] - the interval the lab's own spectrum shape occupies - with its own mean, std and [min,max]; (e) survives_1.7_to_1.9 records whether every scanned point falls in the quoted band.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 11 - this experiment is that row's closure evidence",
      "project-context/peer-reviews/INT_v3/A3M_v3M.0.13_R6_TRUTH_AUDIT_2026-09-04.md sec 4 class (e): 'the Choudhury et al. gamma_cr<~0.85 sign disagreement (:929-930, a genuine discrepancy left unresolved)'",
      "directive Q2 (per-experiment reproducibility manifests), directive R1 (ledger-first), directive R6 (evidence-graded claims)",
      "research/track_a3_multichannel/outputs/R5_18_GAMMACR_NOTE_2026-09-04.md - the finding this experiment closes: the quoted 1.7-1.9 was a UNION of an in-coverage scan (1.732 +- 0.050 over [0.766,0.968]) and ONE out-of-coverage evaluation (1.85-1.89 at [0.267,0.630]), not a scan result over that range",
      "project-context/peer-reviews/INT_v3/A3M_v3M.0.13_R6_TRUTH_AUDIT_2026-09-04.md R6-11 (abstract 'shape-robust' carries none of the body's conditionality)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row14-cs-window",
    "title": "Ledger row 14 - joint dependence of the tensor-to-scalar ratio r and the squeezed local f_NL on the contraction's scalar sound speed c_s, and the (empty) window in which r < 0.036 with an acceptable f_NL",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Li, Quintin, Wang & Cai 2016 - matter bounce with a k-essence field: shape function Eq. (4.19), r = 24 c_s (Eq. 3.18), extended no-go theorem",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1612.02036",
        "checksum": null,
        "license": null
      },
      {
        "name": "Quintin, Sherkatghanad, Cai & Brandenberger 2015 - perturbations and non-Gaussianity through a nonsingular bounce; Eq. (31) |Delta zeta/zeta| >~ 49.1 and Eq. (44) f_NL ~ (Delta zeta)^2/(Delta t_B) M_p^2",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1508.04141",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Easson & Brandenberger 2012 - the matter bounce's large-r problem",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1206.2382",
        "checksum": null,
        "license": null
      },
      {
        "name": "Garriga & Mukhanov 1999 - perturbations in k-inflation; P_zeta ~ 1/(epsilon c_s) and the c_s-dependent canonical variable",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/9904176",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Huang, Kachru & Shiu 2007 - cubic action and non-Gaussianity for general single-field P(X,phi); the 1/c_s^2 scaling of f_NL",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/0605045",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ade et al. (BICEP/Keck) 2021 - r < 0.036 (95% CL), the tensor bound tested here",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2019 - local f_NL = -0.9 +/- 5.1, the non-Gaussianity bound tested here",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1905.05697",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear-transmission module - the three bounce backgrounds and the adiabatic-vacuum scalar evolution with exact matter-basis projection, imported directly",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lab in-in adjudication of the matter-contraction f_NL at c_s = 1 (comoving-gauge isoceles squeezed limit -35/16), the c_s -> 1 cross-check target",
        "type": "internal-artifact",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 10 - r = 16 epsilon = 24 at c_s = 1, bounce-invariant; the starting point of this row",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row10_r_ns/row10_r_ns.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row14_cs_window/row14_cs_window.py",
        "entrypoint": "cd research/track_a3_multichannel/row14_cs_window && python3 row14_cs_window.py",
        "sha256": "f3bc5214cd1f37d59e7f7422e35388e3a02259505d086ac7e6b5d39b882f13f0"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy + scipy + sympy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "4.5 s (measured, field wall_seconds in results.json)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~6 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). r(c_s) is DERIVED symbolically from the c_s-dependent Mukhanov-Sasaki problem (z^2 = 2 a^2 eps/c_s^2, BD normalisation 1/sqrt(2 c_s k)) by two independent routes - the small-argument Hankel limit for general power-law index and the exact q = 2 mode functions - rather than imported from the inflationary formula. Li+2016's Eq. (4.19) shape function is transcribed once; both of its limits are taken symbolically here and checked against their quoted f_NL^equil and f_NL^local."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row14_cs_window/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row14_cs_window/row14_cs_window.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row14_cs_window/row14_cs_window.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row14_cs_window/ROW14_CS_WINDOW_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) analytic.r_dust_str == '16*c_s*epsilon' and analytic.r_exact_equals_16_eps_cs == true (two independent symbolic routes), reproducing Li+2016 Eq. (3.18) r = 24 c_s at eps = 3/2; (b) fnl_cs.f_NL_equilateral_matches_paper == true and fnl_cs.f_NL_squeezed_matches_paper == true (their Eq. 4.19 limits re-derived here), with fnl_cs.reproduces_lab_in_in_minus_35_over_16 == true; (c) numeric.*.max_abs_lambda_ratio_minus_1 <= 1e-10 and every numeric.*.rows[*].r_after_over_16epscs == 1.0, i.e. the bounce transfer is c_s-independent and r stays 16 eps c_s through all three A2 backgrounds; (d) window.cs_for_r_0.036 == 1.5e-3 with window.at_cs_for_r_0.036.f_NL_pre == 3.611e6 and f_NL_after (Quintin) == 5.959e5; (e) window.acceptable_fNL_requires.Planck_1sigma_5.1.min_c_s_per_background.quintin == 0.4440 with min_r == 10.66, so the gap between the two requirements is a factor ~296 in c_s; (f) window.no_go.verdict == 'NO VIABLE c_s WINDOW'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 14, promoted 2026-09-04 from row 10 by decision D-A3-10",
      "research/track_a3_multichannel/row14_cs_window/ROW14_CS_WINDOW_2026-09-04.md (derivation, c_s table, no-go check, paper-ready sentences)",
      "research/track_a3_multichannel/row10_r_ns/ROW10_R_NS_2026-09-04.md (r = 16 eps = 24 at c_s = 1, bounce-invariant)",
      "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md (the lab's independent in-in -35/16 that Li+2016's c_s -> 1 limit reproduces exactly)",
      "directive Q2 (per-experiment reproducibility manifest); directive Q1 (the null is stated in its own terms as a limitation of the modelled background)",
      "model-dependence disclosed: the general-c_s f_NL inherits Li+2016's k-essence kinetic sector; the lab's own in-in machinery is c_s = 1 only, and this lab's pressureless-dust / canonical-scalar contraction does not itself provide c_s < 1"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row15-curvaton",
    "title": "Ledger row 15 - the curvaton-type matter bounce: whether a light spectator in the dust contraction gives r < 0.036 with n_s ~ 0.965 and an O(1) local f_NL, and what happens to the intrinsic -35/16 at that point",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Cai, Xue & Brandenberger 2011 - the matter bounce curvaton scenario: Eq. (18) spectator tilt, Eq. (58)/(61) r ~ 35 F^-2, Eq. (65) f_NL = -(5120/pi^6) d^2 C, Eq. (66) Case-1 f_NL ~ -3.3",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1101.0822",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lyth, Ungarelli & Wands 2003 - the primordial density perturbation in the curvaton scenario; zeta_sigma = (2/3) dsigma/sigma and the r_dec-dependent local f_NL",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0208055",
        "checksum": null,
        "license": null
      },
      {
        "name": "Sasaki, Valiviita & Wands 2006 - non-Gaussianity of the curvaton: f_NL = 5/(4 r_dec) - 5/3 - 5 r_dec/6 with the non-quadratic corrections",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0607627",
        "checksum": null,
        "license": null
      },
      {
        "name": "Bartolo, Komatsu, Matarrese & Riotto 2004 - non-Gaussianity from inflation: theory and observations (the f_NL^local convention zeta = zeta_L + (3/5) f_NL zeta_L^2 used here)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0406398",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Easson & Brandenberger 2012 - towards a nonsingular bouncing cosmology; the matter bounce's large-r problem and its curvaton cure",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1206.2382",
        "checksum": null,
        "license": null
      },
      {
        "name": "Li, Quintin, Wang & Cai 2016 - matter bounce with a k-essence field; Eq. (4.19), the c_s-dependent f_NL used in row 14",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1612.02036",
        "checksum": null,
        "license": null
      },
      {
        "name": "Wands 1999 - duality invariance of cosmological perturbation spectra; the scale-invariant spectrum of a light field in a matter contraction",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/gr-qc/9809062",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ade et al. (BICEP/Keck) 2021 - r < 0.036 (95% CL), the tensor bound tested here",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2019 - local f_NL = -0.9 +/- 5.1, the non-Gaussianity bound tested here",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1905.05697",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear-transmission module - the three bounce backgrounds and the u'' + (k^2 - a''/a)u = 0 evolution, imported directly for the spectator's frozen-branch transfer",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 10 - r = 16 epsilon = 24 and n_s - 1 = 12w/(1+3w) on the w = -0.0029 anchor; the tensor amplitude and tilt this row reuses unchanged",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row10_r_ns/row10_r_ns.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 14 - the c_s no-go and the A2 transfer values T = 0.165-0.250 quoted here",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row14_cs_window/results.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lab in-in adjudication of the matter-contraction f_NL (-35/16), the amplitude diluted by (r/24)^2 in this row",
        "type": "internal-artifact",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Branch-W ALP-curvaton tilt program, phase 1 - the lab's existing curvaton work; its n_sigma - 1 sign is corrected here",
        "type": "internal-artifact",
        "locator": "research/branch_W_alp_curvaton_tilt/phase1_results.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row15_curvaton/row15_curvaton.py",
        "entrypoint": "cd research/track_a3_multichannel/row15_curvaton && python3 row15_curvaton.py",
        "sha256": "aa493476e5936ea3f1d6f7723bb9ee516e83cdb074db52dcc951dbe3d2886a46"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy + scipy + sympy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "~4 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~6 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). The spectator index nu = q - 1/2 and the tilt 12w/(1+3w) are DERIVED symbolically from the Mukhanov-Sasaki operator, not imported; the tracking-mass shift is expanded symbolically and is reported as 8m^2/(3H^2), a factor 4 above CXB11 Eq. (18)'s de Sitter value (sign unchanged). The curvaton power ratio, r(r_dec, sigma_*) and the (r/24)^2 dilution weight are symbolic. The A2 spectator transfer is a direct import of the same ODE used in rows 10 and 14."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row15_curvaton/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row15_curvaton/row15_curvaton.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row15_curvaton/row15_curvaton.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row15_curvaton/ROW15_CURVATON_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) analytic.spectator_tilt_equals_adiabatic_tilt == true and analytic.ns_at_w_anchor == 0.9649, i.e. the curvaton inherits row 10's tilt exactly; (b) analytic.massive_shift_coeff_over_m2H2 == 8/3 (vs CXB11 Eq. 18's 2/3), sign positive => a curvaton mass tilts BLUE; (c) power_ratio.r_of_rdec_sigma_str == '216*sigma_star**2/(12*r_dec**2 + 9*sigma_star**2)' and power_ratio.F_needed_CXB_Eq61['r<0.036'] == 25.8199; (d) fnl.f_NL_at_rdec_1 == -1.25, fnl.sign_change_r_dec == 0.5811, fnl.rdec_min_Planck_2sigma == 0.1130; (e) fnl.bounce_term_at_r_0.036 is order 1e-6 on all three backgrounds and observability.r_max_for_bounce_term_above_SPHEREx_0.5 == 22.95; (f) cxb11.f_NL_case1_value == -3.2851 (= -320/pi^4, their quoted -3.3); (g) transmission.frozen_branch_check LQC/quintin T_c -> 1 as u_out decreases.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 15, promoted 2026-09-04 by decision D-A3-11",
      "research/track_a3_multichannel/row15_curvaton/ROW15_CURVATON_2026-09-04.md (derivation, viable-window table, verdict, paper-ready sentences)",
      "research/track_a3_multichannel/row14_cs_window/ROW14_CS_WINDOW_2026-09-04.md (the c_s no-go this row is the alternative to)",
      "research/track_a3_multichannel/row10_r_ns/ROW10_R_NS_2026-09-04.md (r = 24, n_s anchor, nHz tensor amplitude rescaled here)",
      "directive Q2 (per-experiment reproducibility manifest); directive Q1 (the partial result is stated in its own terms)",
      "model-dependence disclosed: CXB11's kinetic-amplification factor F is an assumption of their entropy sector and is NOT computed here - the A2 backgrounds carry no entropy field; the LUW/SVW f_NL is the exact-quadratic branch"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row15-curvaton-adjudication",
    "title": "Row 15 adjudication: independent sympy re-derivation of the curvaton-type matter bounce claims (CXB11 Eq. 18 coefficient and Case-1 f_NL, branch-W tilt sign, spectator MS operator and tilt, two-channel r, delta-N curvaton f_NL, adiabatic-bispectrum dilution)",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "row-15 lane under adjudication",
        "locator": "research/track_a3_multichannel/row15_curvaton/ (ROW15_CURVATON_2026-09-04.md, results.json, row15_curvaton.py)",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "branch-W ALP-curvaton tilt note",
        "locator": "research/branch_W_alp_curvaton_tilt/03_tilt_mechanisms.md ; 04_dynamical_screening.md ; phase1_results.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "Cai, Xue & Brandenberger 2011 (source)",
        "locator": "https://arxiv.org/abs/1101.0822",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Easson & Brandenberger 2012 (source)",
        "locator": "https://arxiv.org/abs/1206.2382",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lyth, Ungarelli & Wands 2003",
        "locator": "https://arxiv.org/abs/astro-ph/0208055",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Sasaki, Valiviita & Wands 2006",
        "locator": "https://arxiv.org/abs/astro-ph/0607627",
        "type": "external-literature",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.py",
        "entrypoint": "python3 research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.py",
        "sha256": "2db10d9a7fe967a29b67d5c8e7bb09c860c9c36f3533559f83241b8151e588df"
      }
    ],
    "environment": {
      "python": "python3 with sympy (>=1.12; run on sympy 1.14.0), numpy, scipy",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-04",
      "wall_clock": "2 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 minute",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic sympy plus a small scipy DOP853 mode integration (first-order WKB vacuum). Self-validates: de Sitter massive-spectator tilt 2m^2/(3H^2) recovered before the contraction case; the integrator reproduces the exact tracking-mass Bessel tilt 2*gamma/3 to <=3%; the delta-N sudden-decay f_NL reproduces SVW06 exactly; CXB11 Eq. 65 is reproduced from their Eqs. 55/60/64. No network at run time."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required exact values: validation_de_sitter.matches_textbook_2m2_over_3H2 == true; C_spectator_tilt.equals_12w_over_1p3w == true and same_MS_operator_as_adiabatic_for_const_eps == true; A_massive_spectator_dust.tilt_tracking_mass == '8*m**2/(3*H**2)' and coefficient_ratio_contraction_over_deSitter == '4'; D_r_formula.P_curv_over_P_ad_dust == '4*M_pl**2*r_dec**2/(3*sigma_star**2)' and x_threshold_for_r_lt_0.036 == 22.34 (2 dp); E_curvaton_fNL.deltaN_matches_SVW == true and zero_crossing_exact == '-1 + sqrt(10)/2'; F_dilution.adiabatic_weight_of_r == 'r**2/576'; A_CXB11_case1.case1_symbolic == '-320/pi**4'; B_massive_numeric.tracking_mass_validation within 3% of exact.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 15 (curvaton-type matter bounce) — adjudication of the lane's two literature corrections and central claims before the A3M paper may rely on them",
      "directive R (vision governance) and directive Q2 (reproducibility manifests); /never-fabricate-derivation",
      "input 'row-15 lane under adjudication' used for: the six claims A-F and their stated assumptions; its numbers compared only AFTER independent computation",
      "input 'branch-W ALP-curvaton tilt note' used for: item B, locating the erring step (n-1 written as 2nu-3)",
      "input 'Cai, Xue & Brandenberger 2011 (source)' used for: Eqs. 10-19 (spectator equation, Eq. 18 tilt, Eq. 19), Eq. 32 (C), Eqs. 55/60/61/64-67 (amplitudes, r, f_NL)",
      "input 'Cai, Easson & Brandenberger 2012 (source)' used for: checked for an independent curvaton section — none (only a mention of the bounce curvaton); recorded as such",
      "input 'Lyth, Ungarelli & Wands 2003' used for: Phi = -(3/5) zeta = -(r/5) delta rho_sigma/rho_sigma, f_NL = 5/(4r) leading term; zeta_curv = r_dec (2/3) delta sigma/sigma_*",
      "input 'Sasaki, Valiviita & Wands 2006' used for: sudden-decay f_NL = (5/4r)(1+gg''/g'^2) - 5/3 - 5r/6, used as a VALIDATION target of the independent delta-N derivation"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row15b-entropy-sector",
    "title": "Ledger row 15b - the entropy (spectator) sector in the three A2 matter-bounce backgrounds: lambda_sigma vs lambda_T vs lambda_zeta per scheme, and the pre-bounce condition on r_dec Mpl/sigma_* for r < 0.036",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "A2 linear-transmission module - the three bounce backgrounds (Quintin-type, LQC-effective-dust, poly-analytic) and the a''/a arrays used for both the spectator and the tensor evolution",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 18a - lambda_T, lambda_zeta^S1 and lambda_zeta^S2 on the Quintin background; the S2 scalar transfer imported here",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/row18a_s2_tensor/results.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 15 - the curvaton window r = 24/[1 + (4/3) r_dec^2 (Mpl/sigma_*)^2], the F >= 25.82 requirement and the (r/24)^2 dilution of the intrinsic -35/16",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row15_curvaton/results.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "Curvaton matter-bounce adjudication - confirms the spectator obeys the same MS operator for constant epsilon, so n_s is inherited",
        "type": "internal-artifact",
        "locator": "research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Xue & Brandenberger 2011 - the matter-bounce curvaton scenario and the kinetic-amplification factor F",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1101.0822",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lyth, Ungarelli & Wands 2003 - zeta = r_dec zeta_sigma and the curvaton local f_NL",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0208055",
        "checksum": null,
        "license": null
      },
      {
        "name": "Quintin, Sherkatghanad, Cai & Brandenberger 2015 - the bounce background (iii) integrated here",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1508.04141",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ade et al. (BICEP/Keck) 2021 - r < 0.036 (95% CL), the target of the viability condition",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row15b_entropy_sector/row15b_entropy_sector.py",
        "entrypoint": "cd research/track_a3_multichannel/row15b_entropy_sector && python3 row15b_entropy_sector.py",
        "sha256": "0b1e15c6a36ca7a343a78ec7ade61cc7c3d029c004ae3e911da168597aaec8b8"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy + scipy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "~4 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~10 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). The spectator is integrated as u'' + (k^2 - a''/a + a^2 m^2)u = 0 with the EXACT matter-era mode function as the initial condition (exact for all k tau, so no sub-Hubble requirement); the tensor is integrated from an INDEPENDENT first-order system h' = Pi/a^2, Pi' = -a^2 k^2 h, so lambda_sigma/lambda_T - 1 is a genuine numerical test of the operator identity rather than a tautology. lambda_zeta^S2 is imported from row 18a (Quintin only); S2 on the LQC and poly backgrounds is NOT computed here and is disclosed as such."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row15b_entropy_sector/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row15b_entropy_sector/row15b_entropy_sector.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row15b_entropy_sector/row15b_entropy_sector.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row15b_entropy_sector/ROW15B_ENTROPY_SECTOR_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) backgrounds.<bg>.max_abs_lam_sigma_over_lam_T_minus_1 <= 8e-5 (Quintin) and <= 3e-9 (LQC, poly), i.e. the massless spectator transfers exactly like the tensor on all three backgrounds; (b) the light-mass correction dlam/lam scales as (m eta_B)^2 and tends to 0 (about -4e-7 at m eta_B = 1e-6 on Quintin), so the massless limit is recovered smoothly; (c) viability.S1.Lambda == 1 and viability.S2.Lambda == 6.2487 (= row 18a lam_T/lam_zeta^S2); (d) viability.S1['r<0.036'].X_min == 22.344 and viability.S2['r<0.036'].X_min == 22.360, i.e. the pre-bounce condition on X = r_dec Mpl/sigma_* is scheme-independent to 7.3e-4; (e) viability.<scheme>['r<0.036'].F_eff_min == 25.8199 in both schemes, reproducing row 15's F >= 25.82; (f) backgrounds.<bg>.delta_n_T at k eta_B = 1e-3 is about -1e-3 and scales as (k eta_B)^2, so the tensor tilt is unshifted by the bounce on observable scales.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 15 named open item: 'F needs an entropy sector in the A2 backgrounds'",
      "research/track_a3_multichannel/row15b_entropy_sector/ROW15B_ENTROPY_SECTOR_2026-09-04.md (derivation, background x scheme table, verdict, paper-ready sentences)",
      "research/track_a3_multichannel/row15_curvaton/ROW15_CURVATON_2026-09-04.md (the parent row this closes an item of)",
      "research/cubic_bounce_transmission/row18a_s2_tensor/ROW18A_S2_TENSOR_2026-09-04.md (source of lambda_zeta^S2)",
      "directive Q2 (per-experiment reproducibility manifest)",
      "model-dependence disclosed: CXB11's kinetic-amplification factor F is still an assumption of THEIR entropy sector; this row computes the TRANSFER of a spectator through the A2 backgrounds and the resulting pre-bounce condition, it does not derive F from a microphysical model. lambda_zeta^S2 is measured on the Quintin background only."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row18b-cs-bounce-cubic",
    "title": "Ledger row 18(b) - c_s-dependence of the bounce's own cubic contribution Delta f_NL^bounce(c_s) in scheme S1, and the resulting shift of the joint (r, f_NL) window boundary of row 14",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Lane (a) cubic-vertex table - the c_s-dependent coefficients c_V(a,H,eps,eta_sr,c_s) of the P(X,phi) cubic action (Chen, Huang, Kachru & Shiu 2007; Seery & Lidsey 2005; Maldacena 2003) transcribed and checked",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (b) S1 in-in integrator at c_s = 1 - imported directly for its vertex slot/kernel definitions, mode class, dot-product table and quadrature; supplies the c_s = 1 regression gate (-0.139818 / -0.104311 / -0.127111)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/bounce_cubic_inin.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear-transmission module - the three bounce backgrounds (Quintin-type, LQC-effective dust, poly) and the adiabatic-vacuum scalar evolution, imported directly",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 14 - f_NL^pre(c_s) = -165/16 + 65/(8 c_s^2), r = 24 c_s, and the c_s-independence of the bounce transfer T (verified to 4e-11); the window this row re-evaluates",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row14_cs_window/ROW14_CS_WINDOW_2026-09-04.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Li, Quintin, Wang & Cai 2016 - matter bounce with a k-essence field; Eq. (4.19) shape function and Eq. (3.18) r = 24 c_s, the source of f_NL^pre(c_s)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1612.02036",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Huang, Kachru & Shiu 2007 - cubic action for general single-field P(X,phi); the c_s-dependent vertex coefficients used here",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/0605045",
        "checksum": null,
        "license": null
      },
      {
        "name": "Garriga & Mukhanov 1999 - k-inflation perturbations; z^2 = 2a^2 eps/c_s^2 and the BD normalisation 1/sqrt(2 c_s k)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/9904176",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ade et al. (BICEP/Keck) 2021 - r < 0.036 (95% CL)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2019 - local f_NL = -0.9 +/- 5.1, the bound defining the window",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1905.05697",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/row18b_cs_bounce_cubic.py",
        "entrypoint": "cd research/cubic_bounce_transmission/row18b_cs_bounce_cubic && python3 row18b_cs_bounce_cubic.py",
        "sha256": "f8f8cd8d5266fd6866e62a326a83635c38cda39bb1b009b885eaaa3aa1faf588"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy + scipy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "8.0 s (measured, printed in row18b_cs_bounce_cubic.log)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~10 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). Scheme S1 sets z = a exactly, so the Mukhanov-Sasaki equation is mu'' + (c_s^2 k^2 - a''/a) mu = 0 and c_s enters the mode functions ONLY through the sound horizon; this is implemented literally by evolving the modes at k_s = c_s k with the same Wronskian normalisation Im(v* v') = -1/2 (which IS the BD normalisation 1/sqrt(2 c_s k)), while every momentum kernel and dot product uses the physical k. c_s enters elsewhere only through the lane (a) vertex coefficients with the S1 substitutions eps -> 1/2, eta_sr -> 0, s -> 0, lambda -> 0 - the c_s extension of lane (a) assumption (A3). No parameter is tuned."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/row18b_cs_bounce_cubic.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/row18b_cs_bounce_cubic.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/ROW18B_CS_BOUNCE_CUBIC_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) backgrounds.*.gate_cs1.rel_diff <= 2e-3 - the c_s = 1 limit reproduces the lane (b) totals -0.139818 (Quintin), -0.104311 (LQC dust), -0.127111 (poly) at k eta_B = 1e-3, and the assert in dfnl_bounce/main fires otherwise; (b) every backgrounds.*.cs_scan[*].V2_scaling_numeric agrees with V2_scaling_analytic = (6 c_s^2 - 5)/c_s^4 to <= 3e-4 relative, the independent check that the S1 V2 coefficient is a^2 eps(eps-3+3c_s^2)/c_s^4; (c) backgrounds.quintin.cs_scan values Delta f_NL^bounce = +14.29, +3.058, +0.0611, -0.1398 at c_s = 0.44, 0.6, 0.8876, 1; (d) backgrounds.*.boundary.row14_no_bounce_cs.cs_min reproduces row 14 (Quintin 0.4440); (e) backgrounds.*.boundary.with_bounce_term.cs_min == 0.5997 / 0.6064 / 0.6020 with r_min == 14.39 / 14.55 / 14.45, i.e. the |f_NL^after| <= 5.1 boundary MOVES UP in c_s and the no-go strengthens; (f) backgrounds.*.boundary.at_tensor_viable_cs.fnl_after_with_bounce ~ 1e11 at c_s = 1.5e-3 versus ~1e6 without the bounce term.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 18 item (b), A3-cs-bounce",
      "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/ROW18B_CS_BOUNCE_CUBIC_2026-09-04.md (derivation, c_s x background table, boundary statement, paper-ready sentences)",
      "research/cubic_bounce_transmission/lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md (the c_s-dependent coefficients, literature-cited)",
      "research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md (the c_s = 1 values this row must reproduce)",
      "research/track_a3_multichannel/row14_cs_window/ROW14_CS_WINDOW_2026-09-04.md (f_NL^pre(c_s), r = 24 c_s, c_s-independent T)",
      "directive Q2 (per-experiment reproducibility manifest); directive Q1 (the strengthened no-go is stated in its own terms)",
      "model-dependence disclosed: f_NL^pre(c_s) inherits Li+2016's k-essence kinetic sector (row 14 sec 2), and the S1 vertex coefficients keep eps -> eps_eff = 1/2 while retaining c_s exactly, which is a scheme assumption (lane (a) A3) and not the dressed-metric H_3 of Agullo+2017"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-row19-lambda",
    "title": "Ledger row 19 - the joint (r, f_NL) no-go for general P(X) k-essence with the cubic-action coefficient lambda free: lambda-general f_NL^pre(c_s, lambda/Sigma), the exact lambda-independence of r and of the bounce's own cubic term, and the window scan",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Li, Quintin, Wang & Cai 2016 - matter bounce with a generalized single field. Eq. (2.11)-(2.12) define Sigma and lambda; Eq. (4.18) is the only lambda-carrying shape contribution; Eq. (4.19) is the total shape function AFTER lambda/Sigma = (1-c_s^2)/(6c_s^2) has been substituted; Eq. (A.19)-(A.20) derive that substitution; Eq. (3.18) gives r = 24 c_s",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1612.02036",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Huang, Kachru & Shiu 2007 - cubic action for general single-field P(X,phi); identical Sigma and lambda conventions (their Eq. 4.7-4.8) and the vertex coefficients used by lane (a)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/0605045",
        "checksum": null,
        "license": null
      },
      {
        "name": "Garriga & Mukhanov 1999 - k-inflation perturbations; c_s^2 = P_X/(P_X + 2X P_XX), used for the lambda-independence argument for r",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/9904176",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ade et al. (BICEP/Keck) 2021 - r < 0.036 (95% CL)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2110.00483",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2019 - local f_NL = -0.9 +/- 5.1",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1905.05697",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 14 - f_NL^pre(c_s) = -165/16 + 65/(8c_s^2) at lambda = 0, r = 24 c_s, and the transfer T = 0.16500538 (Quintin background); the lambda = 0 result this row generalises",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row14_cs_window/ROW14_CS_WINDOW_2026-09-04.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger row 18(b) - Delta f_NL^bounce(c_s) = -(5/24) rho_B (6c_s^2-5)/c_s^4 in scheme S1; its integrator is imported and its V1 coefficient patched to carry lambda",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/row18b_cs_bounce_cubic/row18b_cs_bounce_cubic.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (a) cubic-vertex table - c_V1 = -a^3[Sigma(1-1/c_s^2) + 2 lambda]/H, the lambda-carrying vertex",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lab in-in adjudication - the canonical-field squeezed value -35/16 that the lambda-general formula must reproduce at c_s = 1, lambda = 0",
        "type": "internal-artifact",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/track_a3_multichannel/row19_lambda/row19_lambda.py",
        "entrypoint": "cd research/track_a3_multichannel/row19_lambda && python3 row19_lambda.py",
        "sha256": "bcf832b3b2a9bb92b53300e7a20e1549961a8f66459172834811d6388c35b446"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy + scipy + sympy + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "2.8 s (measured, printed in row19_lambda.log)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~5 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no data files, no network). The lambda-restoration is algebraic: A_tot(c_s, L) = A_tot^Li(c_s) - 9[L - (1-c_s^2)/(6c_s^2)] sum_i k_i^3, undoing the substitution Li+2016 state below their Eq. (4.19). The bounce leg imports row 18(b) and monkeypatches only the V1 coefficient to c_V1^conf(L) = -(aH) eps [(1/c_s^2 - 1/c_s^4) + 2L/c_s^2]. Nothing is tuned; the tuned-lambda numbers in section [E] are reported as the COST of a viable window, not as a model."
    },
    "outputs": [
      {
        "locator": "research/track_a3_multichannel/row19_lambda/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row19_lambda/row19_lambda.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row19_lambda/row19_lambda.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/track_a3_multichannel/row19_lambda/ROW19_LAMBDA_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) r_lambda_independence.quadratic_action_independent_of_lambda is true, with dSigma/dP_XXX = dc_s^2/dP_XXX = 0 and dlambda/dP_XXX = 2X^3/3; (b) fnl_pre.matches_closed_form_squeezed / _equilateral true, i.e. f_NL^sq = -245/16 + 105/(8c_s^2) - 30 L and f_NL^eq = -495/32 + 105/(8c_s^2) + 45c_s^2/128 - 30 L; (c) fnl_pre.gate_Li_line_reproduces_row14_squeezed and _equilateral true (the lambda-general form collapses to row 14 on Li's matter line) and gate_cs1_L0_equals_minus_35_over_16 true - all three are asserts; (d) fnl_pre.L_that_cancels_the_1_over_cs2_divergence == 7/(16*c_s**2); (e) bounce.max_abs_total_over_L0_minus_1 <= 1e-6 (2.8e-7 measured) and bounce.lambda_vertex_is_odd_in_eta true, with Delta f_NL^bounce = +14.291777 / +3.057749 / -0.139818 at c_s = 0.44/0.6/1.0 unchanged from row 18(b) for every L; (f) window.min_r_over_scan == 12.5664 on the DBI line and window.any_L_reaches_r_below_0.036 is false; (g) tuning.L_required_for_zero_f_NL_pre_only == 194444.44 with s_that_would_give_L_pre_only == 2.4375 = 39/16, versus Li's |s| << 1 assumption.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 19 (A3-lambda), opened by R8 audit item R8-01",
      "decision D-A3-13 (the (r, f_NL) no-go stated for lambda = 0) - row 19 removes the qualifier",
      "research/track_a3_multichannel/row19_lambda/ROW19_LAMBDA_2026-09-04.md (convention map, derivation, tables, paper-ready sentences, scope limits)",
      "directive Q2 (per-experiment reproducibility manifest); directive Q1 (the generalised no-go is stated in its own terms, not as a correction narrative)",
      "model-dependence disclosed: the shape contributions are Li+2016's in-in integrals (transcribed, with their lambda term re-exposed), not re-derived here; eps = 3/2 is held fixed; the bounce term uses scheme S1 with eps_eff = 1/2 and a SYMMETRIC bounce - the lambda-independence of section 3 is a parity statement and would not hold exactly for an asymmetric bounce"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "a3-survey-reach-fnl",
    "title": "Track A3 channel 3 — survey reach and current-constraint tension table for f_NL^local = -35/16",
    "program": "bounce-theory",
    "paper": "A3",
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
    "status": "runnable-now",
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
      "notes": "The AUG-011 clean rerun is complete and receipt-verified: 36,634/36,634 shard groups scored, 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate rows removed, and 52,188 raw rows above the sealed anomaly_score>5.0 threshold (all fibers, incl. sky — not a science-candidate count; science-target counts pending the 2026-09-03 provenance-filtered rerun). On 2026-08-26, all B2 shards/receipts were freshly fetched locally and receipt-verified; the fixed-ladder observed distribution then produced a 3,810-row anomaly_score>=8.0 characterization sample — subsequently found to be 84.8% sky fibers by TARGETID/OBJTYPE (2026-09-03), so it is provenance-contaminated and superseded by the pending science-target rerun; its own (contaminated) Parquet SHA-256 is 00bf453e864a2fda93ef6d72cd351984c4b8f43975d9962b65d168901ee1b852, retained for provenance only. The sample, its full receipt-binding manifest, and parent summary were uploaded to the authenticated private rerun archive. Do not describe the corpus or selected sample as anonymously public or forkable from this repository. Remaining active work is enrichment, validation, taxonomy, external-catalog joins, public immutable archiving, and manuscript drafting."
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
    "verification": "Full-scan verification passed: verify-receipts covered 36,634/36,634 groups, summarize-after-dedup produced 28,425,963 raw rows, 27,547,223 unique TARGETIDs, 878,740 duplicate rows removed, and 52,188 raw rows above anomaly_score>5.0 (all fibers, incl. sky; not a science-candidate count). Output checksums are raw file SHA-256 values. Separately, run-contract.json's internal calibration_sha256 is the canonical JSON-payload SHA-256 25498638fd23bb0033960e8199608e890feacd9e0eb220b24b300efcc954eb2f, and summary.json's contract_sha256 is the canonical contract-payload SHA-256 6699d09ff886f74dab6608bd70a70b73b7a34afabc436d365c69f16a95ac5edf; those are semantic bindings, not file-byte hashes. The completed run is recorded in pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/{complete.log,summary.json,comparison.json}. On 2026-08-26 the full retained B2 shard/receipt corpus was freshly fetched locally and verified, then build_flagship_sample.py replayed the binding to produce the 3,810-row anomaly_score>=8.0 selected sample. This does not assert a fresh re-download of original multi-TB DESI coadds or a public data release.",
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
    "id": "anomaly-known-object-recovery-benchmark",
    "title": "Known-object recovery benchmark for the anomaly flagship catalogue (ledger item #8)",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "Sealed locator inventory (HEALPix footprint definition)",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/locator_inventory.jsonl",
        "checksum": null
      },
      {
        "name": "Partial S>8 enrichment bundle (preview run only)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/tree/main/phase3/2026-08-26/partial-enrichment-s8",
        "checksum": null,
        "license": null
      },
      {
        "name": "Reference 'unusual object' classes (Baron & Poznanski 2017, Roma-BZCAT, BALQSO, CV, carbon-star, LAE, EELG, changing-look-QSO, SLSN-host, GRB-host catalogues)",
        "type": "external-dataset",
        "locator": "VizieR (astroquery.vizier) -- see REFERENCE_CLASSES in benchmark_known_object_recovery.py for per-class catalogue IDs and source papers",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "VizieR (CDS)",
        "endpoint": "https://vizier.cds.unistra.fr/viz-bin/votable",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py",
        "entrypoint": "python3 benchmark_known_object_recovery.py --fetch-references --reference-cache-dir <cache> && python3 benchmark_known_object_recovery.py --crossmatch --reference-cache-dir <cache> --catalogs-config <config.json> --locator-inventory sealed_2026-08-05/locator_inventory.jsonl --out-dir <out>",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, astroquery, healpy, pandas, pyarrow, numpy -- see clean_rerun's phase-3 pip install line in RUNBOOK.md",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-02",
      "wall_clock": "under 5 minutes (fetch-references + crossmatch stages combined) for the PREVIEW run",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU or the phase-3 RunPod pod (same host, no extra GPU need)",
      "est_wall_clock": "minutes for --fetch-references (VizieR query latency dominates, ~10-30s per class with checkpointless single-shot fetch); seconds to low minutes for --crossmatch once the flagship sample carries target_ra/target_dec (via enrich_flagship_sample.py) for the full S>5/S>8 samples",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "The PREVIEW run committed under results_2026-08-07/phase3/recovery_benchmark_preview/ used the 57/3810-group PARTIAL S>8 enrichment bundle (not the full sample) and returned 0 fetched reference classes because this build environment's outbound route to vizier.cds.unistra.fr's VizieR TAP/query endpoint (not just the raw TCP port) times out/resets on every attempt, though the TCP port itself is reachable -- see reference_manifest.json's per-class error field for the exact honest failure mode of each attempt. Re-run --fetch-references from a host with working VizieR access (Houston's machine or the RunPod pod) to get real reference-class row counts, then re-run --crossmatch once build_flagship_sample.py's S>5 output has been joined to target_ra/target_dec (it currently is not -- only the S>8 enriched sample carries coordinates) and the full (not partial) S>8 sample has landed from phase 3."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark_preview/recovery_benchmark.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark_preview/recovery_benchmark.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "pipelines/p1_highz_tracers/tests/test_recovery_benchmark.py (26 offline unit tests, pytest -q) covers the pure/offline matching, HEALPix footprint-restriction, Wilson-score CI, and enrichment/closed-loop-candidate arithmetic against hand-verified synthetic fixtures. The committed PREVIEW recovery_benchmark.json/.md are the actual output of a real run against real (partial) data -- not synthetic -- and are honest about their 0-fetched-classes outcome; do not treat the preview's empty results table as evidence against any reference class, only as evidence this build environment could not reach VizieR's query endpoint on 2026-09-02.",
    "status": "needs-data-restore",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 8",
      "project-context/SESSION_HANDOFF_2026-08-05_to_2026-08-28.md (Anomaly flagship section: S>5=52188, S>8=3810, unique_targetids=27547223)",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/summary.json (threshold=5.0, threshold_count_after_dedup=52188, unique_targetids=27547223)",
      "pipelines/p1_highz_tracers/clean_rerun/RUNBOOK.md Section 19",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark_preview/recovery_benchmark.json (this run's own committed output)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-known-object-recovery-benchmark-v2",
    "title": "Known-object recovery benchmark (ledger item #8) run against the S>3 v2 science-only flagship sample",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "Sealed locator inventory (HEALPix footprint definition)",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/locator_inventory.jsonl",
        "checksum": null
      },
      {
        "name": "flagship_sample_v2_enriched.parquet (S>3 science-only sample, n=1244)",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet",
        "checksum": "c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff"
      },
      {
        "name": "Cached reference 'unusual object' classes (BAL quasars, Roma-BZCAT blazars, CV/WD binaries, LAEs, SLSN hosts)",
        "type": "external-dataset",
        "locator": "huggingface/local cache: ~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/ (fetched 2026-09-02, reused unchanged for this v2 run)",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "VizieR (CDS)",
        "endpoint": "https://vizier.cds.unistra.fr/viz-bin/votable",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py",
        "entrypoint": "python3 benchmark_known_object_recovery.py --crossmatch --reference-cache-dir ~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02 --reference-manifest ~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/reference_manifest_local.json --catalogs-config /tmp/catalogs_config_v2.json --locator-inventory pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/locator_inventory.jsonl --radius-arcsec 1.5 --out-dir pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, astroquery, healpy, pandas, pyarrow, numpy",
      "hardware": "cpu-only, local (Houston's machine, not the RunPod pod)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-04",
      "wall_clock": "under 1 minute (offline crossmatch stage against cached reference classes)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU (any host with the cached reference_catalogs, or a fresh --fetch-references run from a host that can reach vizier.cds.unistra.fr's TAP query endpoint)",
      "est_wall_clock": "under 1 minute for --crossmatch once references are cached; 10-40 min for a fresh --fetch-references pass",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Unlike the v1 recovery_benchmark_preview run (which returned 0 fetched classes due to a VizieR TAP-endpoint connectivity failure), this v2 run reused the successfully cached 2026-09-02 reference fetch (5/11 classes fetched, 4 unavailable for missing RA/Dec columns, 1 with no known catalogue ID) and produced real per-class recovery numbers against the S>3 v2 sample's 1244 rows."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/recovery_benchmark.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/recovery_benchmark.md",
        "type": "document",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/PHASE3_V2_BENCHMARK_SUMMARY.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "pipelines/p1_highz_tracers/tests/test_recovery_benchmark.py (26 offline unit tests) covers the pure matching/CI/enrichment arithmetic. This run's real output: 1 BAL-quasar positional match (4.2x enrichment, out of 5285 in-footprint references) out of 5 fetched classes; ledger #8's >10x-enrichment/>=5-match confirmed-class bar is NOT met. 0 matches for Roma-BZCAT, CV/WD binaries, LAEs, SLSN hosts.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 8",
      "pipelines/p1_highz_tracers/clean_rerun/RUNBOOK.md Section 19",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/PHASE3_V2_BENCHMARK_SUMMARY.md (this run's own committed output)",
      "project-context/PHASE3_V2_LANDING_2026-09-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "anomaly-map-png-highz-abundance",
    "title": "Ledger #6 first discriminator - local-PNG correction to the z=8-14 massive-galaxy abundance at f_NL = -35/16 vs -35/8 vs 0 (LoVerde+2008 Edgeworth mass function)",
    "program": "anomaly-discovery",
    "paper": "none",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Eisenstein & Hu 1998 no-wiggle transfer function",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/9709112",
        "checksum": null,
        "license": null
      },
      {
        "name": "LoVerde, Miller, Shandera & Verde 2008 non-Gaussian mass function Eq. (45)/(46)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/0711.4126",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2018 VI cosmological parameters (TT,TE,EE+lowE+lensing+BAO, Table 2)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1807.06209",
        "checksum": null,
        "license": null
      },
      {
        "name": "Planck 2018 IX local f_NL constraint (KSW T+E)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1905.05697",
        "checksum": null,
        "license": null
      },
      {
        "name": "f_NL = -35/16 matter-contraction squeezed value (ledger #1, closed in-lab)",
        "type": "internal-artifact",
        "locator": "research/theory_audit/",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/anomaly_map/ledger6_png_highz_abundance.py",
        "entrypoint": "python3 research/anomaly_map/ledger6_png_highz_abundance.py",
        "sha256": "f1121e2b79c4d43a98117d022876e72d9c972754d26b9e090b7b96e446742365"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy 2.5.1 + scipy 1.18.0 + matplotlib 3.11.1",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-02",
      "wall_clock": "2.4 s (measured, `time` on the full script)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~3 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no external data files, no network). All cosmology is analytic: Eisenstein & Hu 1998 no-wiggle transfer function normalised to sigma_8, local-bispectrum skewness by 3-D Gauss-Legendre/Simpson quadrature, LoVerde+2008 Eq. (45) Edgeworth mass-function ratio. The Edgeworth expansion is a linear-response result; the reported fnl_for_factor_N entries lie outside its validity and are labelled order-of-magnitude scale indicators in the JSON and the brief."
    },
    "outputs": [
      {
        "locator": "research/anomaly_map/outputs/ledger6_png_highz_abundance.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/anomaly_map/outputs/ledger6_png_highz_abundance.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/anomaly_map/LEDGER6_DISCRIMINATOR_BRIEF_2026-09-02.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) sigma8_check == 0.8111 to 4 decimals (self-consistency of the normalisation); (b) S_3/f_NL at R = 8 Mpc/h equals 8.784e-4 and at M_h = 2.15e11 Msun/h equals 3.366e-4, stable to 5 significant figures under refinement (n_k, n_mu, k_max) = 140/48/60 -> 300/96/300; (c) threshold_cases.eps_0.20.z11.0.lab_matter_contraction == 0.93158 +/- 1e-4 and .cai2009 == 0.86316 +/- 1e-4; (d) threshold_cases.eps_0.05.z12.0.lab_matter_contraction == 0.84720 +/- 1e-4; (e) confrontation.cases.eps_0.20.z11.0.dR_dfnl == 0.031277 +/- 1e-5 and fnl_for_factor_2 == 31.97 +/- 0.01.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 6 (first cheap test)",
      "project-context/VISION.md route 3 (early-universe anomaly map)",
      "project-context/PORTFOLIO_DECISION_2026-09-02.md Addendum (anomaly line redirected, not retired)",
      "research/anomaly_map/LEDGER6_DISCRIMINATOR_BRIEF_2026-09-02.md",
      "f_NL = -35/16 from ledger #1 (CLOSED 2026-09-02), commits d7dac953 / aa2987cf / 66cf1cb0",
      "ledger #3 A3-1 compaction-function PBH result, reproducibility/manifests/experiments/a3-pbh-compaction-fnl.json"
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
        "type": "document",
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
    "id": "ledger4-desi-dr1-lss-sanity",
    "title": "Ledger #4 step 1 - provenance-bound download and lab-native sanity check of the DESI DR1 public LSS clustering catalogues (QSO, LSScats v1.5), the input products for an independent reproduction of the DR1 local-PNG scale-dependent-bias constraint",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "validation",
    "inputs": [
      {
        "name": "DESI DR1 QSO NGC clustering catalogue (LSScats v1.5)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/QSO_NGC_clustering.dat.fits",
        "checksum": "sha256:9d01efdc6dc3c2a403369e5a8e0f7129a8ff08b5e503d9b0c6b91b7bc589f784",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "DESI DR1 QSO SGC clustering catalogue (LSScats v1.5)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/QSO_SGC_clustering.dat.fits",
        "checksum": "sha256:875c67fe9ef5c03c1daf9fe5606f254b3ab6e91c4fb01ef304f6fa9a7a2c1bc4",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "DESI DR1 QSO SGC randoms realisation 0 of 18 (LSScats v1.5)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/QSO_SGC_0_clustering.ran.fits",
        "checksum": "sha256:2965a952b3a59902f0de84f91e95f4106c3f63a2b32e9f539450b3ed73d9d9c9",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "DESI DR1 QSO NGC n(z) table (FKP weights)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/QSO_NGC_nz.txt",
        "checksum": "sha256:853fa9c56bbfdd659373d216bc1c9fc2ce4365fa9babddd3850ee4135c529505",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "DESI DR1 QSO SGC n(z) table (FKP weights)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/QSO_SGC_nz.txt",
        "checksum": "sha256:80608da63516ac0afbf704a1e073611c2c5bb75232785ea13f67d369a0e3b357",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "Chaussidon et al. 2024 - DESI DR1 LRG+QSO local PNG constraint (the measurement being reproduced; supplies the 1,189,129 QSO / 0.8<z<3.1 comparison numbers)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2411.17623",
        "checksum": null,
        "license": null
      },
      {
        "name": "Brown, Levi, Randall, Chaussidon et al. 2026 - configuration-space DR1 LRG+QSO PNG measurement (method-independent cross-check)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2606.24651",
        "checksum": null,
        "license": null
      },
      {
        "name": "Rezaie et al. 2023 - imaging-systematics mitigation for photometric DESI LRG PNG (source of the systematics-budget design)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2307.01753",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ledger #3 survey-reach study (DESI DR1 = 0.16 sigma on f_NL = -35/16; sets this item's honest scope)",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/survey_reach_fnl.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "DESI public data server (anonymous HTTP, no key)",
        "endpoint": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "research/desi_png_reproduction/dr1_lss_sanity.py",
        "entrypoint": "python3 research/desi_png_reproduction/dr1_lss_sanity.py",
        "sha256": "aff455a671b6a1494443c71869d57d92f38907dc0500cb7891ab52fbfecf05fc"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + astropy 8.0.1 + matplotlib 3.11.1",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-03",
      "wall_clock": "download 0.86 GB ~ 20 s; sanity check 0.7 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~2 min including download",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Data live OUTSIDE the repo at ~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/ (0.86 GB). Re-fetch with curl -O from the five locators above and confirm the sha256s before re-running. The script memory-maps the FITS files and never loads the 736 MB randoms table into memory (header row count only)."
    },
    "outputs": [
      {
        "locator": "research/desi_png_reproduction/outputs/dr1_lss_sanity.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/dr1_lss_sanity_zhist.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/dr1_lss_sanity_footprint.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) the five input sha256s match the values recorded above; (b) row counts QSO NGC = 793,219 and QSO SGC = 430,172 (total 1,223,391); (c) checks.n_qso_in_published_z_range == 1,190,839 in 0.8 < z < 3.1, i.e. ratio_zrange_to_published == 1.0014 against Chaussidon et al. 2024's 1,189,129 - a 0.14% agreement, which is the pass condition (an EXACT match is not expected and is not claimed, since the published count follows further analysis selection); (d) both caps carry WEIGHT_SYS, WEIGHT_COMP, WEIGHT_ZFAIL, WEIGHT_RF, WEIGHT_FKP, WEIGHT, NX; (e) WEIGHT_SYS NGC mean == 0.97676 +/- 1e-4, std == 0.06538, range [0.6244, 1.5945], zero non-finite values - i.e. the imaging-systematics weight that the plan's section 3.4 test 1 switches off is present and non-trivial; (f) randoms QSO_SGC_0 has 6,511,977 rows, 15.14x the SGC data.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 4 (first cheap test: reproduce the published DESI PNG pipeline on DR1 public products)",
      "research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md sections 2 (inputs) and 7 (execution log)",
      "directive Q2 (per-experiment reproducibility manifests with external sources, licences, venue, cost, wall clock), directive R1 (ledger-first), directive R6 (claims at their evidential strength: this is a provenance check, not a measurement)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "ledger4-desi-dr1-qso-fnl-reproduction",
    "title": "Ledger #4 steps 2-6 - independent pypower P_ell(k) measurement and scale-dependent-bias f_NL^loc fit on DESI DR1 QSO (LSScats v1.5), with a WEIGHT_SYS systematics test and b_Phi-marginalised posterior overlap against the flagship f_NL=-35/16",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "DESI DR1 QSO clustering + randoms catalogues (LSScats v1.5) - NGC+SGC data, 4/18 randoms realisations per cap (0-3)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
        "checksum": "sha256:2e14a4d112deada4f41f2c1768048184d5c2b97d2874844e2cc12adbab8964ce (QSO_NGC_0_clustering.ran.fits; full list in research/desi_png_reproduction/venv_setup/qso_randoms_1-3_sha256.txt plus the ledger4-desi-dr1-lss-sanity manifest for the step-1 files)",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "Chaussidon et al. 2024 - DESI DR1 LRG+QSO local PNG constraint (reproduction target; supplies b1(z) formula, FKP P0 fiducial, published f_NL central values/errors)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2411.17623",
        "checksum": null,
        "license": null
      },
      {
        "name": "cosmoprimo DESI fiducial cosmology (eisenstein_hu transfer engine - CLASS/pyclass unavailable, fails to build in this environment)",
        "type": "external-literature",
        "locator": "https://github.com/cosmodesi/cosmoprimo",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "DESI public data server (anonymous HTTP, no key)",
        "endpoint": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "research/desi_png_reproduction/pk_estimator_qso.py",
        "entrypoint": "python3 pk_estimator_qso.py [NGC|SGC]",
        "sha256": "7ace8a26fce9acf22069e17528646cd89728edfd7fbc0e77c71348da462925bb"
      },
      {
        "path": "research/desi_png_reproduction/combine_and_compare.py",
        "entrypoint": "python3 combine_and_compare.py",
        "sha256": "d63c48607eca68b7615457a653383d5f47e1a0a5500e0b0f98210da02ea58ae3"
      },
      {
        "path": "research/desi_png_reproduction/fit_fnl.py",
        "entrypoint": "python3 fit_fnl.py",
        "sha256": "628da290a1f02520bdd81a499208384b6fbd2544c421f1b3bf05c7f83b05cb35"
      },
      {
        "path": "research/desi_png_reproduction/systest_weight_sys.py",
        "entrypoint": "python3 systest_weight_sys.py",
        "sha256": "b4dd467e924f6fb5e1b0f3da9fa2b90ccbeb5ec8e525b00eebaaf5d65fa2f4c9"
      },
      {
        "path": "research/desi_png_reproduction/systest_fit.py",
        "entrypoint": "python3 systest_fit.py",
        "sha256": "62f13c5fab3d78af58aaf4050e4590f13d0bd6a04a9975b9731dab872d3b6f7a"
      }
    ],
    "environment": {
      "python": "python3.12.13 (dedicated venv: research/desi_png_reproduction/.venv312, gitignored) + numpy 2.5.2 + scipy 1.18.1 + astropy 8.0.1 + fitsio 1.4.2 + emcee 3.1.6 + mpi4py 4.1.2 + pyFFTW 0.15.1 + pmesh (git) + pypower 1.0.0 (git) + cosmoprimo (git, eisenstein_hu engine) + desilike (git); brew open-mpi required for mpi4py/pmesh build",
      "hardware": "cpu-only; Apple M-series MacBook Air, 25.8 GB RAM, 10 cores, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "package install ~15 min; +7.8GB download ~4 min; P_ell(k) NGC+SGC ~3 min; f_NL fit (3 MCMC runs, 3000 steps x 32 walkers) ~10 min; WEIGHT_SYS systematics test (4 pypower runs) ~12 min; total session ~1 hour of compute",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~45 min after environment setup (venv + package install ~15-20 min one-time)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Requires the step-1 sanity-check files (ledger4-desi-dr1-lss-sanity manifest) plus randoms realisations 1-3 per cap (re-fetch from the DESI URL, sha256s in venv_setup/qso_randoms_1-3_sha256.txt). CLASS/pyclass fails to build in this environment (ValueError: could not build CLASS) -- cosmoprimo falls back to the eisenstein_hu transfer engine, a documented fidelity limitation vs the published CLASS-based pipeline. Run order: pk_estimator_qso.py NGC, pk_estimator_qso.py SGC, combine_and_compare.py, fit_fnl.py, systest_weight_sys.py, systest_fit.py.\nAddenda: [{\"id\": \"v3-official-products-2026-09-04\", \"note\": \"RunPod pod p8vj377enumve4 (RTX A6000) created, never reachable, stopped+terminated, $0 compute cost. Substituted official DESI DR1 full-shape-bao-clustering v1.0 VAC products (window matrix, full-18-randoms measured P_ell, EZmock covariance for QSO GCcomb z0.8-2.1) downloaded from data.desi.lbl.gov -- see research/desi_png_reproduction/official_products_sha256.txt for checksums and LEDGER4_RESULT_v3_2026-09-04.md for the full result.\", \"code\": [\"research/desi_png_reproduction/official_window_io.py\", \"research/desi_png_reproduction/fit_fnl_official.py\"], \"result\": \"f_NL(p=1.6)=-2.17+/-25.3, f_NL(p=1.0)=-1.13+/-13.1, marginalised(midpoint)=-1.65+/-19.2\", \"cost_usd\": 0.0}]"
    },
    "outputs": [
      {
        "locator": "research/desi_png_reproduction/outputs/pk_qso_NGC.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/pk_qso_SGC.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/pk_qso_combined_comparison.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/fnl_fit_results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/fnl_chain_marginalised.npy",
        "type": "dataset",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/systest_weight_sys_fnl.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/LEDGER4_RESULT_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) P0(k=0.01,zeff) at f_NL=0, b1=2.242 (published Table-2 formula) predicts 35,522 (Mpc/h)^3 vs measured combined P0(k=0.01)=34,944 -- 1.7% agreement (fnl_fit_results.json note field); (b) f_NL posterior medians: -50.6 (p=1.6), -26.7 (p=1.0), -36.3 (p marginalised over [1.0,1.6]) with sigma 18.5/9.3/15.5 respectively (fnl_fit_results.json); (c) WEIGHT_SYS on/off point-estimate Delta f_NL = +62.4 (systest_weight_sys_fnl.json), exceeding the statistical sigma by >3x; (d) posterior distance from f_NL=-35/16 is 2.20 sigma, from -35/8 is 2.06 sigma, from 0 is 2.34 sigma, using the p-marginalised chain's median/std.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 4",
      "research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md sections 3 (method), 4 (compute), 5 (kill/success)",
      "research/desi_png_reproduction/RUN_LOG.md (full step-by-step log with commit SHAs)",
      "research/desi_png_reproduction/LEDGER4_RESULT_2026-09-04.md (result writeup)",
      "directive Q2 (reproducibility manifests), directive R1 (ledger-first), directive R6 (claims at their evidential strength -- central-value offset from published reported honestly, not smoothed)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "ledger4-desi-dr1-qso-fnl-reproduction-v2",
    "title": "Ledger #4 v2 - cause-removal follow-up (window/IC, CAMB transfer, measured-shot-noise covariance, gal-lat systematics) on the DESI DR1 QSO f_NL^loc reproduction; supersedes ledger4-desi-dr1-qso-fnl-reproduction",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "DESI DR1 QSO clustering + randoms catalogues (LSScats v1.5) - NGC+SGC data, 4/18 randoms realisations per cap used in the headline fit (realisations 4-6 additionally downloaded/sha256'd for the blocked fix-3 attempt)",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
        "checksum": "sha256 list in research/desi_png_reproduction/venv_setup/qso_randoms_1-3_sha256.txt and qso_randoms_4-6_sha256.txt",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "Chaussidon et al. 2024 - DESI DR1 LRG+QSO local PNG constraint (reproduction target)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2411.17623",
        "checksum": null,
        "license": null
      },
      {
        "name": "cosmoprimo DESI fiducial cosmology (eisenstein_hu engine, baseline) + CAMB (fix 2, A_s-matched to cosmoprimo)",
        "type": "external-literature",
        "locator": "https://github.com/cosmodesi/cosmoprimo ; https://camb.readthedocs.io/",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "DESI public data server (anonymous HTTP, no key)",
        "endpoint": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "research/desi_png_reproduction/window_conv.py",
        "entrypoint": "python3 window_conv.py 4",
        "sha256": "c17beb7cc760dab06d1cb24b1b580bcda40343d33701a64242d61d742b14fdc1"
      },
      {
        "path": "research/desi_png_reproduction/camb_transfer.py",
        "entrypoint": "python3 camb_transfer.py",
        "sha256": "dc8b88d202824df24d069a7fe51a63e14e205778bb6e0c653da58a84dffa3053"
      },
      {
        "path": "research/desi_png_reproduction/fit_fnl_v2.py",
        "entrypoint": "python3 fit_fnl_v2.py --point --tk {eh,camb} [--window-ic] [--shotnoise-fixed] --out <file>",
        "sha256": "29ecd96a2d470f09ef71f74e1be2369581ee2baf499f692a9f19cddd33bc3b73"
      },
      {
        "path": "research/desi_png_reproduction/systest_gal_lat_fast.py",
        "entrypoint": "python3 systest_gal_lat_fast.py",
        "sha256": "3ce05519d38487e2905143f969f79b80bad1d86d26f262de41d5df58397b2011"
      },
      {
        "path": "research/desi_png_reproduction/systest_splits_fit_v2.py",
        "entrypoint": "python3 systest_splits_fit_v2.py",
        "sha256": "f3cd557076434439774694cf5be82f24e47a91c2fd88083040e5d153b7db6d4f"
      }
    ],
    "environment": {
      "python": "python3.12.13 (dedicated venv: research/desi_png_reproduction/.venv312, gitignored) + camb 2.0.4 added this session (prebuilt macOS arm64 wheel, no gfortran issue)",
      "hardware": "cpu-only; Apple M-series MacBook Air, 25.8 GB RAM, 10 cores, macOS 25.5.0 arm64 -- SHARED with concurrent sessions this run (swap usage peaked 24.4/25.6 GB, disk free swung 28GB-6GB-34GB from other activity, not this job)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "window power computation ~11 min (NGC 77s + SGC 560s under contention); camb install+validation ~5 min; point-estimate fits (4 configs) ~2 min; n_ran=7 and n_ran=5 full-randoms attempts ~65 min combined, both killed without completing (fix 3 blocked); reduced-scope gal-lat systematics (nmesh=256, NGC-only) ~1 min; total session several hours, dominated by host-contention retries",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local (on an UNCONTENDED host -- this session's compute-time overruns were measured host-contention artifacts, not algorithmic cost)",
      "est_wall_clock": "~20 min on an idle host with the venv + step-1 pypower P0/P2 outputs already present",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Requires outputs/pk_qso_{NGC,SGC}.json from the v1 pipeline (pk_estimator_qso.py) already on disk. Run order: window_conv.py 4 -> camb_transfer.py (sanity print) -> fit_fnl_v2.py --point --tk eh --out step0 -> --window-ic --out step1 -> --tk camb --window-ic --out step2 -> --tk camb --window-ic --shotnoise-fixed --out step4 -> systest_gal_lat_fast.py -> systest_splits_fit_v2.py. Fix 3 (full/expanded randoms) is UNRESOLVED -- retry PK_N_RAN=7 pk_estimator_qso.py on an idle host; realisations 4-6/cap are already downloaded+sha256'd (qso_randoms_4-6_sha256.txt), no new download needed. Known blockers this session: Fix 3 (full 18/cap or even 5-7/cap randoms) did not complete within this session's compute budget under measured host contention (concurrent sessions, swap 24+/25.6 GB) -- realisations 4-6/cap are downloaded+sha256'd and ready for a retry on an idle host. | Full pypower CatalogFFTWindow mode-mixing matrix (the plan's specified window-convolution method) is computationally infeasible in this environment at any tested scope (a 1-bin/1-ell minimal config exceeded 3 min CPU without completing) -- the shipped fix-1 uses a cheaper shuffled-randoms global-IC approximation instead, documented as a real simplification. | E(B-V), stellar-density, and depth/seeing systematics splits require the DESI imaging pixel-weight map, not downloaded this session. | Covariance remains analytic-diagonal (no EZmocks, no window mode-coupling) -- RunPod/EZmock contingency remains unauthorised per the governing plan."
    },
    "outputs": [
      {
        "locator": "research/desi_png_reproduction/outputs/window_qso_NGC.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/window_qso_SGC.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/fnl_fit_v2_step0_baseline.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/fnl_fit_v2_step1_windowic.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/fnl_fit_v2_step2_camb.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/fnl_fit_v2_step4_shotnoise.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/systest_splits_pk.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/systest_splits_fnl_v2.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/LEDGER4_RESULT_v2_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) step0 point estimate reproduces v1's MCMC medians to <1% (-50.43 vs -50.6 p=1.6, -26.06 vs -26.7 p=1.0) -- validates the point-estimate simplification; (b) step1 (window-IC) moves f_NL to -23.22/-12.00; (c) step2 (+CAMB, A_s-matched to cosmoprimo's 2.083e-9) moves to -16.68/-8.62; (d) step4 (measured-shotnoise covariance) leaves the central value at -16.68/-8.62 (Delta~0, as expected for a covariance-only change); (e) camb_transfer.py's T(k) differs from EH by -0.1% to -1.6% over k=0.003-0.05 (fnl_fit_v2_step2 vs step1 movement is NOT proportional to this small T(k) difference -- amplified via 1/alpha(k) sensitivity, documented in the result writeup); (f) gal-lat NGC-only split gives Delta f_NL=-197.3 (systest_splits_fnl_v2.json), confirming systematics >> statistics (sigma=18.5) as in v1's WEIGHT_SYS test (+62.4). Supersedes: ledger4-desi-dr1-qso-fnl-reproduction.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 4",
      "research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md",
      "research/desi_png_reproduction/RUN_LOG.md follow-up section (2026-09-04)",
      "research/desi_png_reproduction/LEDGER4_RESULT_2026-09-04.md (v1, superseded)",
      "research/desi_png_reproduction/LEDGER4_RESULT_v2_2026-09-04.md (this result)",
      "directive Q2 (reproducibility manifests), directive R1 (ledger-first), directive R6 (claims at their evidential strength)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "ledger4-desi-dr1-qso-fnl-reproduction-v4",
    "title": "Ledger #4 v4 - wide-angle correction check (genuine null) + imaging-systematics splits (E(B-V), stellar density, galactic depth) at official-window/official-EZmock-covariance fidelity, on the DESI DR1 QSO f_NL^loc reproduction; supersedes ledger4-desi-dr1-qso-fnl-reproduction-v3 headline (numbers unchanged, two open items closed)",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Official DESI DR1 full-shape-bao-clustering v1.0 VAC (window matrix, full-18-randoms P_ell, EZmock covariance) for QSO - same products as v3",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/vac/dr1/full-shape-bao-clustering/",
        "checksum": "sha256 list in research/desi_png_reproduction/official_products_sha256.txt",
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "DESI DR1 QSO clustering + randoms catalogues (LSScats v1.5), split by imaging property median (E(B-V), STARDENS, GALDEPTH_Z) - NGC+SGC, produced by pk_estimator_qso_splits.py",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/",
        "checksum": null,
        "license": "CC BY 4.0 (DESI public data releases)"
      },
      {
        "name": "pypower PowerSpectrumOddWideAngleMatrix (Beutler/Castorina-White wide-angle formalism)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2106.06324 ; https://github.com/cosmodesi/pypower",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chaussidon et al. 2024 - DESI DR1 LRG+QSO local PNG constraint (reproduction target)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2411.17623",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "DESI public data server (anonymous HTTP, no key)",
        "endpoint": "https://data.desi.lbl.gov/public/dr1/",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "research/desi_png_reproduction/wideangle_check.py",
        "entrypoint": "python3 wideangle_check.py",
        "sha256": "07b74363e8e7e9643f48b6835e6e7df6d0616bed4670a894b6df215fd6eafef0"
      },
      {
        "path": "research/desi_png_reproduction/imaging_splits_crossmatch.py",
        "entrypoint": "python3 imaging_splits_crossmatch.py",
        "sha256": "287e449f1a04ab51746d73456550fb407969e12cadb06a7284269cb1ca7f3a8e"
      },
      {
        "path": "research/desi_png_reproduction/pk_estimator_qso_splits.py",
        "entrypoint": "python3 pk_estimator_qso_splits.py {EBV,STARDENS,GALDEPTH_Z}",
        "sha256": "2260f73a7e7fc8a03293db4b0c922869c05fef72fc4ad4ba12e96c262743d700"
      },
      {
        "path": "research/desi_png_reproduction/fit_fnl_splits.py",
        "entrypoint": "python3 fit_fnl_splits.py",
        "sha256": "de0e20c1d59e324c5eefef36b967571f4086b43220995f64f42724b27dc761cf"
      }
    ],
    "environment": {
      "python": "python3.12.13 (dedicated venv: research/desi_png_reproduction/.venv312, gitignored)",
      "hardware": "cpu-only; Apple M-series MacBook Air, 25.8 GB RAM, 10 cores, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "wide-angle matrix construction + check ~10s; three split P(k) NGC+SGC pypower runs (prior session instance) several minutes each; fit_fnl_splits.py six official-fidelity fits with profile-likelihood scans ~3 min total",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~5 min given outputs/pk_split_*.json and official_products/ already on disk",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Requires official_products/ (window matrix, EZmock covariance) already downloaded per v3, and outputs/pk_split_{NGC,SGC}_{EBV,STARDENS,GALDEPTH_Z}_{low,high}.json already on disk (pk_estimator_qso_splits.py). Run order: wideangle_check.py (standalone, no split dependency) -> fit_fnl_splits.py (reads combine_and_compare.py-convention NGC+SGC combination internally). No new external data required beyond v1-v3's downloads."
    },
    "outputs": [
      {
        "locator": "research/desi_png_reproduction/outputs/wideangle_check.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/outputs/imaging_splits_fnl_v4.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/desi_png_reproduction/LEDGER4_RESULT_v4_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) wideangle_check.py's library guard raises ValueError 'Wide-angle order 1 produces only odd poles' when an even-ell projout is requested at wa_order=1, and the constructed matrix's even-ell blocks (ell=0,2,4) have max|M|=0.0 over k<=0.08 for all three; (b) fit_fnl_splits.py reproduces the table: E(B-V) Delta f_NL=-1.69 (sigma_Delta=29.30), STARDENS Delta f_NL=-2.37 (sigma_Delta=34.70), GALDEPTH_Z Delta f_NL=-18.66 (sigma_Delta=31.73) -- none exceeds |Delta/sigma|=2; (c) v3's headline numbers (f_NL=-2.169+/-25.3 at p=1.6, -1.127+/-13.1 at p=1.0) are UNCHANGED by the wide-angle correction, confirming the analytic null. Supersedes: ledger4-desi-dr1-qso-fnl-reproduction-v3 (v3 had no separate manifest; this manifest documents both v3's carried-forward headline and v4's two new closed items).",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 4",
      "research/desi_png_reproduction/LEDGER4_DESI_PNG_PLAN_2026-09-03.md",
      "research/desi_png_reproduction/RUN_LOG.md v4 section (2026-09-04)",
      "research/desi_png_reproduction/LEDGER4_RESULT_v3_2026-09-04.md (v3, headline carried forward unchanged)",
      "research/desi_png_reproduction/LEDGER4_RESULT_v4_2026-09-04.md (this result)",
      "directive Q2 (reproducibility manifests), directive R1 (ledger-first), directive R6 (claims at their evidential strength)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "ledger7-chiral-gw-delta-h",
    "title": "Ledger #7 gate - net helicity asymmetry Delta_h of the SGWB from the minimal Einstein-Cartan-Holst torsion bounce (symbolic parity-operator check + super-Hubble k-odd estimate)",
    "program": "bounce-theory",
    "paper": "none",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Freidel, Minic & Takeuchi 2005 - minimal fermion coupling in Einstein-Cartan-Holst, gamma^2/(1+gamma^2) four-fermion term",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/0507253",
        "checksum": null,
        "license": null
      },
      {
        "name": "Mercuri 2006 - Nieh-Yan formulation; Immirzi parameter unobservable at constant gamma",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/gr-qc/0601013",
        "checksum": null,
        "license": null
      },
      {
        "name": "Alexander & Yunes 2009 - Chern-Simons modified gravity review",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/0907.2562",
        "checksum": null,
        "license": null
      },
      {
        "name": "Taveras & Yunes 2008 - dynamical Barbero-Immirzi field",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/0807.2652",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai, Li, Wang & Zhu 2021 - chiral GWs in Nieh-Yan modified teleparallel gravity",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/2104.08376",
        "checksum": null,
        "license": null
      },
      {
        "name": "Poplawski 2010 - torsion spin-fluid bounce (Hehl-Datta term, parity-even)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1007.0587",
        "checksum": null,
        "license": null
      },
      {
        "name": "Seto & Taruya 2007/2008 - circular-polarisation sensitivity of a planar GW detector",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/0707.0535",
        "checksum": null,
        "license": null
      },
      {
        "name": "Domcke et al. 2020 - measuring SGWB chirality with LISA via the kinematic dipole",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1910.08052",
        "checksum": null,
        "license": null
      },
      {
        "name": "Kato & Soda 2016 - PTA probe of circular polarisation",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1512.09139",
        "checksum": null,
        "license": null
      },
      {
        "name": "Gluscevic & Kamionkowski 2010 - CMB TB/EB from chiral GWs",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1002.1308",
        "checksum": null,
        "license": null
      },
      {
        "name": "On-shell ECH torsion irreps and O4 coefficient (in-lab adjudication, 2026-08-08)",
        "type": "internal-artifact",
        "locator": "research/theory_audit/ech_torsion_onshell_2026_08_08.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "ECH Note four-fermion contact term L_4psi = -(3 kappa/16) gamma^2/(1+gamma^2) (J5.J5)",
        "type": "internal-artifact",
        "locator": "arxiv/paper1bc_ech_note/main.tex",
        "checksum": null,
        "license": null
      },
      {
        "name": "Branch M PGT bounce GW spectrum (amplitude/frequency gap)",
        "type": "internal-artifact",
        "locator": "research/branch_M_pgt_bounce_gw/phase1_results.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Branch Q sourced-parity screening (BRANCH_Q_WEAK)",
        "type": "internal-artifact",
        "locator": "research/branch_Q_sourced_parity/phase1_results.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/chiral_gw_gate/chiral_gw_delta_h.py",
        "entrypoint": "python3 research/chiral_gw_gate/chiral_gw_delta_h.py",
        "sha256": "93eba1315977ed33ffc53031be619844679cb140d9eeefba4a7c12e0e02e5fb2"
      }
    ],
    "environment": {
      "python": "python3.14.6 + numpy 2.5.1 + sympy",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-03",
      "wall_clock": "< 3 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~3 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully offline and deterministic (no RNG, no external data files, no network). Part (A) is exact sympy algebra on the solved on-shell ECH contorsion coefficients; part (B) is a closed-form redshift/parametric evaluation. The Delta_h numbers are CEILINGS at the perturbative-unitarity value xi_B = 1 with an O(1) matching constant set to 1; in minimal ECH the parity-odd coefficient is exactly zero. Unfixed conventions (Holst sign s_H; no committed rho_c/T_B) are listed in the output JSON under convention_flags."
    },
    "outputs": [
      {
        "locator": "research/chiral_gw_gate/outputs/ledger7_chiral_gw_delta_h.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/chiral_gw_gate/LEDGER7_CHIRAL_GW_GATE_2026-09-03.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) symbolic.beta_over_alpha_onshell == 's_H/(2*gamma)'; (b) symbolic.O4_onshell simplifies to -3*J5sq*gamma**3*kappa**2*lambda_src**2*s_H/(gamma**2 + s_H**2)**2, i.e. -3 kappa^2 gamma^3/(1+gamma^2)^2 (J5.J5) at s_H=+1, matching research/theory_audit/ech_torsion_onshell_2026_08_08.md READING-I; (c) symbolic.xi_gamma_numeric['gamma=0.2375'] == 0.053394 +/- 1e-6 (the ECH Note's 0.053) and ['gamma=0.274'] == 0.069833 +/- 1e-6; (d) symbolic.beta_over_alpha_numeric_sH_plus1 == {2.10526, 1.82482} +/- 1e-4 (the 40/19 and 250/137 of the 2026-08-08 adjudication); (e) symbolic.parity_odd_tensor_coefficient_minimal_ECH == '0'; (f) numeric rows: f_B(T_B=1e16 GeV) == 1.668e9 Hz +/- 1e6 and Delta_h_max for LISA == 5.995e-13 (rel. 1e-3), PTA == 5.995e-18, CMB == 1.798e-26; (g) verdict.gate == 'CLOSE WITH REASON (O(epsilon), and requires an ad-hoc ingredient)'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 7 (four-question gate)",
      "research/project_nextgen_bounce_signals/07_single_best_theory.md (March-2026 'single best next theory' call, REVERSED by this gate)",
      "research/branch_M_pgt_bounce_gw/ and research/branch_Q_sourced_parity/ (prior partial work, not redone)",
      "research/theory_audit/ech_torsion_onshell_2026_08_08.md and operator_basis_adjudication_2026_08_07.md",
      "arxiv/paper1bc_ech_note/main.tex v1N.0.5 Eq. (4fermi)",
      "directive Q2 (per-experiment reproducibility manifests), directive Q4 (nothing viable gets lost - salvage recorded)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "ledger9-c-abs-operator-map",
    "title": "Ledger row 9 (A3-1e) lane (c) - literature-bound map of the Agullo-Bolliet-Sreenath 2017 LQC third-order Hamiltonian onto the lab's classical scheme-S1 cubic vertex table, plus the k_LQC -> k*eta_B scale-window conversion and PTA/PBH overlap test",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Agullo, Bolliet & Sreenath 2017 - Non-Gaussianity in loop quantum cosmology (H^(3) Eq. 23; dressed metric Eqs. 39-42; k_LQC and the exp(-alpha k_t/k_LQC) law, sec. V)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1712.08148",
        "checksum": null,
        "license": null
      },
      {
        "name": "arXiv source package read directly (NGLQC.tex, v2 2018-02-26) - equation numbering recovered by counting numbered environments, anchored on Eq. 23 = eq:H3 and Eqs. 39-42 = dres/ta/teta/qpot",
        "type": "external-literature",
        "locator": "https://arxiv.org/e-print/1712.08148",
        "checksum": null,
        "license": null
      },
      {
        "name": "Ashtekar, Kaminski & Lewandowski / Agullo, Ashtekar & Nelson - dressed-metric approach (cited by ABS 2017 as the origin of Eqs. 39-42 and the effective potential U)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1211.1354",
        "checksum": null,
        "license": null
      },
      {
        "name": "Agullo, Ashtekar & Nelson - extension of the quantum theory of cosmological perturbations to the Planck era",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1302.0254",
        "checksum": null,
        "license": null
      },
      {
        "name": "Maldacena 2003 - third-order action ABS state their H^(3) Legendre-transforms into",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0210603",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Huang, Kachru & Shiu 2007 - cubic action coefficients (c_s^-4 structure used for the c_s -> 0 dust argument)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/0605045",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (a) cubic vertex table V1-V7 + R1-R4 and the LQC-dust background",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (c) 2026-09-03 literature comparison (the statement corrected by this lane)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_c_comparison/LANE_C_COMPARISON_2026-09-03.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-3 SIGW note - comoving bounce scale k_B = 1.71e15 Mpc^-1 at T_B = 1e8 GeV, linear in T_B",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1b in-lab Delta^2_zeta - PBH-band amplitude 5e-10 to 1.3e-9 and the 7.0 dex deficit",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane9c_abs_operator/lane9c_scale_window.py",
        "entrypoint": "python3 research/cubic_bounce_transmission/lane9c_abs_operator/lane9c_scale_window.py",
        "sha256": "432f8606f1cc94ed0ffcde583183f1401efbfcdffee24bdc9d3e745ffa454898"
      }
    ],
    "environment": {
      "python": "python3 + numpy + scipy (quad)",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "< 2 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~2 s (script); ~2 min to re-fetch and re-read the arXiv source",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "The operator mapping is literature transcription plus algebra, not computation: it is verified by re-reading NGLQC.tex from https://arxiv.org/e-print/1712.08148 and checking that Eq. 23 (label eq:H3) contains no rho/rho_c, rho_sup, area gap, or U/tilde-U. The script is deterministic (no RNG, no network, no data files); it evaluates two quadratures and closed-form ratios. Conventions: kappa = 1, a_B = 1, k*eta_B = k/k_B with k_B = 1/eta_B and eta_B the conformal half-width of the NEC-violating window (rho >= rho_c/2)."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane9c_abs_operator/lane9c_scale_window.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) scale_window.k_LQC_eta_B_dust == 1.060146 +/- 1e-5 and k_LQC_eta_B_stiff == 0.552857 +/- 1e-5; (b) scale_window.pole_over_eta_B_stiff == 1.169869 +/- 1e-5 (ABS pole at 1.17 eta_B, just outside the NEC window); (c) scale_window.equilateral_decay_exponent_per_k_eta_B == 1.830229 +/- 1e-5, so |Delta f_NL^bounce| ~ exp(-1.83 k eta_B); (d) observability.k_eta_B_of_band['T_B=1e+08 GeV']['PBH_hi'] == 3.0994 +/- 1e-3 and ['PTA_60nHz'] == 2.2807e-7 +/- 1e-11; (e) observability.T_B_for_k_LQC_at_60nHz_GeV == 22.807 +/- 1e-2 GeV, i.e. 6.6 decades below section V's T_B >= 1e8 GeV; (f) pbh_tail['fNL=1000_zeta_c=0.1'].n_sigma == 408.25 +/- 1e-2; (g) by re-reading the source: ABS Eq. 23 contains p_phi or a V-derivative in every term and no rho/rho_c or U, and the sentence after it states the Legendre transform agrees with Maldacena 2003.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 9 (A3-1e), lane (c) literature-bound leg",
      "research/cubic_bounce_transmission/lane_a_vertex_table/ and lane_c_comparison/ (prior lanes; this lane CORRECTS lane (c)'s 'operator not contained in S1' statement)",
      "directive Q2 (per-experiment reproducibility manifests), directive R1 (ledger-first), directive R6 (evidence-graded claims)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "ledger9-c2-lqc-exact-modes-inin",
    "title": "Ledger row 9 (A3-1e) lane 9c-2 - scheme-S1 bounce-window in-in integral (V2-V7 + R1-R4) evaluated with EXACT dressed-metric mode functions on the LQC-dust background over k*eta_B in [0.1, 10], with the initial state varied (lab adiabatic contraction vacuum, ABS adiabatic-order-zero vacuum, 4th-order adiabatic vacuum), testing whether the Agullo-Bolliet-Sreenath 2017 f_NL enhancement near k*eta_B ~ 1 appears in the lab's model",
    "program": "bounce-theory",
    "paper": "A3",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Agullo, Bolliet & Sreenath 2017 - Non-Gaussianity in loop quantum cosmology (H^(3) Eq. 23; dressed metric Eqs. 39-42; |f_NL| ~ 1e3 plateau sec. IV B and VII; exp(-alpha k_t/k_LQC) decay sec. V; adiabatic-order-zero initial state sec. IV F)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1712.08148",
        "checksum": null,
        "license": null
      },
      {
        "name": "Maldacena 2003 - third-order action ABS's H^(3) Legendre-transforms into",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/astro-ph/0210603",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Huang, Kachru & Shiu 2007 - cubic-action coefficients used for the epsilon-scaling estimate",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/hep-th/0605045",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (a) cubic vertex table V1-V7 + R1-R4 (scheme S1 coefficients and kernels)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (b) numerical in-in machinery and its LQC result at k*eta_B = 1e-3 (-0.1043113297), the gate target of this lane",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/bounce_cubic_inin.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane (b) results.json (backgrounds.lqc.k_scan, read by the gate at run time)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/results.json",
        "checksum": null,
        "license": null
      },
      {
        "name": "A2 linear-transmission module - LQC-dust background, dressed geometric potential a''/a = x^(1/3)(1/6 + x/3), matter-basis projection, exact dust adiabatic vacuum",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lane 9c - ABS operator map, k_LQC*eta_B = 1.060146, decay 1.830229 per k*eta_B, 408 sigma PBH tail",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md",
        "checksum": null,
        "license": null
      },
      {
        "name": "A3-1b in-lab Delta^2_zeta ~ 1e-9 and the 7.0 dex PBH-band deficit",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane9c2_lqc_modes/lane9c2_lqc_modes.py",
        "entrypoint": "python3 research/cubic_bounce_transmission/lane9c2_lqc_modes/lane9c2_lqc_modes.py",
        "sha256": "70bcaba34c209115cae533540dd04b28e0341f1c4351e9ea2b4db1ca344fcc36"
      }
    ],
    "environment": {
      "python": "python3 + numpy + scipy (solve_ivp DOP853, CubicSpline, simpson) + matplotlib",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-04",
      "wall_clock": "~140 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~3 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic: no RNG, no network, no data files. The script imports lane (b)'s vertex set, kernels and in-in conventions verbatim and A2's LQC-dust background; only the mode-function initial state and the k-range are new. Conventions: kappa = 1, a_B = 1, rho_c = 1, k*eta_B = k*eta_B with eta_B the conformal half-width of the NEC-violating window; scheme S1 (z = a, eps_eff = 1/2, c_s = 1); f_NL = (5/6) B / (P1P2 + P1P3 + P2P3); squeezed isoceles k1 = 0.02 k unless the equilateral block is read."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane9c2_lqc_modes/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9c2_lqc_modes/lane9c2_lqc_modes.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9c2_lqc_modes/lane9c2_growth_factor.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9c2_lqc_modes/lane9c2_dfnl_bounce.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9c2_lqc_modes/LANE9C2_LQC_MODES_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) gate.passed is true and gate.rel_vs_laneB <= 1e-3 (measured 2.43e-11: the exact-mode pipeline reproduces lane (b)'s LQC total -0.1043113297 at k*eta_B = 1e-3); (b) gate.rel_V2_vs_closed == 3.04e-4 +/- 1e-5 (V2 alone vs the lane (a) closed form -(5/24) rho_B = -5/48) while gate.rel_vs_analytic == 1.389e-3 for the total, the difference being the genuine V3+V4+V6+V7 + R1-R4 content; (c) every mode has Wronskian Im(mu* mu') = -0.5 to 1e-9; (d) modes['0.1']['S-lab'].power_modification == 3.948e4 +/- 1%, modes['1']['S-lab'].power_modification == 1.0950 +/- 1e-3, and modes['3']['S-lab'].power_modification == 1.000001 +/- 1e-5 - the linear bounce imprint switches off within a factor 3 above k_LQC; (e) the state-dependence of dfnl[k][state].total is <= 13% across S-lab / S-ABS0 / S-ad4 at every k in K_SCAN, and eta0_systematic spans <= 15%; (f) |dfnl| stays in 0.3-7 (squeezed) across eta_star_systematic for every k in [0.1, 10], i.e. >= 2 dex below the ABS 1e3 plateau at k*eta_B ~ 1; (g) pbh_tail reproduces lane 9c's anchor: the |f_NL| = 1e3, zeta_c = 0.1 NG-term-only case gives 408.2 sigma.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 9 (A3-1e) - the computation named in lane 9c sec. 5",
      "research/cubic_bounce_transmission/lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md (predecessor lane; its verdict was NOT DETERMINABLE WITHOUT A COMPUTATION, and named this one)",
      "directive Q2 (per-experiment reproducibility manifests), directive R1 (ledger-first), directive R6 (evidence-graded claims)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "lift2-separate-universe-failure-criterion",
    "title": "Novelty lift #2: criterion for the O(1) failure of the isotropic separate universe (delta N) in non-attractor phases — <eps/c_s^2>_zeta, general-w lambda and f_map, validations on dust / USR / attractor / ekpyrotic",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "lab threading map (2026-09-04), frozen constant-eps kernels",
        "locator": "research/theory_audit/threading_map_second_order_2026_09_04.json",
        "type": "internal-artifact",
        "checksum": "sha256:b961e8678c3e8eb27df881600982cf2ce0b97ece902e3873835a9d0ac4d91cf7"
      },
      {
        "name": "lab monopole adjudication (2026-09-03), in-in general-eps input",
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "novelty audit item C2",
        "locator": "project-context/NOVELTY_AUDIT_2026-09-04.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "Namjoo, Firouzjahi & Sasaki 2013",
        "locator": "https://arxiv.org/abs/1210.3692",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Chen, Firouzjahi, Namjoo & Sasaki 2013",
        "locator": "https://arxiv.org/abs/1301.5699",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Pajer, Schmidt & Zaldarriaga 2013",
        "locator": "https://arxiv.org/abs/1305.0824",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Dai, Pajer & Schmidt 2015",
        "locator": "https://arxiv.org/abs/1504.00351",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Cai et al. 2018",
        "locator": "https://arxiv.org/abs/1712.09998",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Bravo, Mooij, Palma & Pradenas 2018",
        "locator": "https://arxiv.org/abs/1711.02680",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Passaglia, Hu & Motohashi 2019",
        "locator": "https://arxiv.org/abs/1812.08243",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lyth, Malik & Sasaki 2005",
        "locator": "https://arxiv.org/abs/astro-ph/0411220",
        "type": "external-literature",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/separate_universe_failure_criterion_2026_09_04.py",
        "entrypoint": "python3 research/theory_audit/separate_universe_failure_criterion_2026_09_04.py",
        "sha256": "21668ab6771101b663a9fcf3a3155e665fca92b30f34f76221ef9343b26a0a29"
      }
    ],
    "environment": {
      "python": "python3 with sympy (>=1.12; run on sympy 1.14.0)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-04",
      "wall_clock": "0.2 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 10 seconds",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic exact sympy on closed forms; reads the frozen threading-map JSON (no constraint re-solve). Self-validating asserts: zetadot/(H zeta) = eps-3 on the constant-eps non-constant mode; f_map = -(5 eps/4)(1-mu^2); delta N initial-label = -5; in-in minus delta N monopole = 5 eps (9-eps)/18; exact USR linear lambda = 1 + eps_f/3 - sqrt(eps_s eps_f)/3; every frozen map piece vanishes at eps -> 0."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/separate_universe_failure_criterion_2026_09_04.json",
        "type": "result-json",
        "checksum": "sha256:4e2a49be541a57d34c4803a20bf7c66cc4016b0612a7881823a9c4cfde85563c"
      },
      {
        "locator": "research/theory_audit/separate_universe_failure_criterion_2026_09_04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required: constant_eps.Theta == 'epsilon*(epsilon - 3)'; constant_eps.lambda_ == '1 - epsilon/3'; USR_exact_linear.lambda_USR_exact == '-sqrt(epsilon_f)*sqrt(epsilon_s)/3 + epsilon_f/3 + 1'; second_order.f_dN_initial_label == '-5'; second_order.all_map_pieces_carry_eps == true; general_w.lambda_ == '-(w - 1)/2'; general_w.f_map_monopole == '-5*(w + 1)/4'; validations.dust_eps_3_2.monopole_gap == '25/8'; validations.ekpyrotic.cases['eps=10'].nonconstant_mode == 'decays as eta->0-'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NOVELTY_AUDIT_2026-09-04.md C2 'Lift to N3': generalise the map, state the failure as a criterion, demonstrate on >=2 backgrounds + USR control",
      "directive R (vision governance) and directive Q2 (reproducibility manifests)",
      "input 'lab threading map' used for: the frozen constant-eps kernels and eps->0 / attractor limits (read, not re-derived)",
      "input 'lab monopole adjudication' used for: f_inin(mu,eps) and the USR 5/2 benchmark statement",
      "external literature used for: placement only (section 4); no result transcribed"
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
    "id": "p1b-blind-shortcut-detection",
    "title": "Blind shortcut-detection test: can a referee decide from receipts alone whether an expensive pseudo-C_ell computation was actually performed?",
    "program": "lab-infra",
    "paper": "P1B",
    "kind": "validation",
    "inputs": [
      {
        "name": "Synthetic HEALPix Gaussian signal realisations (nside=64, lmax=64, power-law C_ell)",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/pcl.py (make_map; healpy.synfast, seeds from the sealed assignment)",
        "checksum": null
      },
      {
        "name": "Synthetic binary sky mask (equatorial cut + 12 random discs, f_sky = 0.7857)",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/pcl.py (make_mask, seed 11)",
        "checksum": null
      },
      {
        "name": "namaster-proof receipt primitive (publish_json / verify_json_receipt)",
        "type": "internal-artifact",
        "locator": "packages/namaster-proof/src/namaster_proof/receipts.py",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/namaster_proof/blind_test/wigner.py",
        "entrypoint": "python3 test_wigner.py",
        "sha256": "13221ecafe217a9cc7d32842fccd73cfd4d41dba966a6e55fb441f8a7d794779"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/pcl.py",
        "entrypoint": "imported by variants.py",
        "sha256": "5d9fb3dcdba5821e187c9597874ab3987c0492b86b4d7b9fa11a53fa6ca9fc80"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/variants.py",
        "entrypoint": "imported by run_blind.py",
        "sha256": "1ea01738dd3a90da2c6260c28a2f6dbdc7d35519e3f3ac29309ca55d1272255b"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/seal.py",
        "entrypoint": "python3 seal.py",
        "sha256": "cd66d949511574cb164bd5247025946adb677ed1f7312b8aef6375ed8f1712e5"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/run_blind.py",
        "entrypoint": "python3 run_blind.py",
        "sha256": "d660743d120f6ed58be46150e03b1992989ec5504c82c9a4f3b3cbc327f1dc9c"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/verify.py",
        "entrypoint": "python3 verify.py",
        "sha256": "e847c512b5e4708830413d057eed0423026738791bef0831e10cf6c71535dc19"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/reveal.py",
        "entrypoint": "python3 reveal.py",
        "sha256": "c27518919c656b0206cdd9c7105af950fc867ce5f1e39278491ea20401e8346c"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + healpy 1.20.0 + scipy 1.18.0; sympy optional (test_wigner.py cross-check only). NaMaster/pymaster is NOT required and is NOT installed: the test ships its own spin-0 MASTER estimator so the Wigner-3j evaluation count can be instrumented.",
      "hardware": "cpu-only, any laptop"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (macOS arm64)",
      "date": "2026-09-04",
      "wall_clock": "~1 min total for seal + 19 runs (1 reference + 18 blind) + verify + reveal",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "~1-2 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "python3 seal.py && python3 run_blind.py && python3 verify.py && python3 reveal.py, from pipelines/namaster_proof/blind_test/. seal.py draws a FRESH random key, so a re-run reproduces the scorecard STATISTICS (detection/false-positive rates per arm) but not the committed assignment digest. To reproduce the committed run exactly, skip seal.py and reuse the committed sealed/key.txt + sealed/assignment.json."
    },
    "outputs": [
      {
        "locator": "pipelines/namaster_proof/blind_test/public/contract.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public/sealed_digest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public/runs",
        "type": "receipt",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public/verdicts.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public/scorecard.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Exact, not tolerance-based. (1) python3 test_wigner.py reproduces the m=0 Wigner-3j kernel against sympy.physics.wigner to < 1e-12 on six cases. (2) reveal.py recomputes the sealed assignment from key.txt and asserts its sha256 equals the pre-run committed digest in public/sealed_digest.json (assignment_sha256 = 0f4ca4ba8e431067c8d47e182264ccedb62a72a6a1c564e72ccbab653a4d5515; seal_verified = true). (3) public/scorecard.json must reproduce byte-identically from the committed sealed/ and public/runs/: detection_rate_excluding_S5 = 1.0 (12/12 across S1-S4), detection_rate_all_shortcuts = 0.8 (12/15), false_positive_rate = 0.0 (0/3 honest). (4) Every run's result/receipt pair must pass namaster_proof.receipts.verify_json_receipt.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NOVELTY_AUDIT_2026-09-04.md, section '#3 — namaster-proof as a verification primitive (candidate 10)' (the lift this test executes)",
      "pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md (design note: threat model, trace fields, blind protocol, pre-declared success criterion)",
      "packages/namaster-proof/src/namaster_proof/receipts.py (the content-binding primitive under test)",
      "commit 0b43d5d6 (design note), b0426b4c (3j kernel), fc2f01b8 (pseudo-C_ell core), 73ec01ff (variants), 00132500 (seal), a07c496b (harness + verifier), d60949b7 (executed run + artifacts)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p1b-blind-shortcut-detection-batch2",
    "title": "Blind shortcut-detection test, batch 2: pre-registered rerun under frozen rules, with the referee-requested effective-multipole shortcut class (S6)",
    "program": "lab-infra",
    "paper": "P1B",
    "kind": "validation",
    "inputs": [
      {
        "name": "Synthetic HEALPix Gaussian signal realisations (nside=64, lmax=64, power-law C_ell; seeds HMAC-derived from the sealed key)",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/pcl.py (make_map)",
        "checksum": null
      },
      {
        "name": "Synthetic binary sky mask (equatorial cut + 12 random discs)",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/pcl.py (make_mask, seed 11)",
        "checksum": null
      },
      {
        "name": "namaster-proof receipt primitive (publish_json / verify_json_receipt)",
        "type": "internal-artifact",
        "locator": "packages/namaster-proof/src/namaster_proof/receipts.py",
        "checksum": null
      },
      {
        "name": "Frozen decision rules R0-R6 (pre-registered, committed alone before the seal)",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/RULES_v2_FROZEN.md",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/namaster_proof/blind_test/variants2.py",
        "entrypoint": "imported by run_blind2.py",
        "sha256": "d1a2211c0fad3567e438cdac375e3af5bcc9c3446ee6d2c51b076edcaddb9881"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/seal2.py",
        "entrypoint": "NP_SEALED_DIR=<outside repo> python3 seal2.py",
        "sha256": "7b7212ef2277d83bc220237ac8bc3c4908c9fb6d30e358929579e23bcbde00eb"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/run_blind2.py",
        "entrypoint": "NP_SEALED_DIR=<outside repo> python3 run_blind2.py",
        "sha256": "149b12d899f671ec42a27e40ecea8640319bd80888a4f21850229c90a76bbff1"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/verify.py",
        "entrypoint": "python3 verify.py public2",
        "sha256": "6a9acd705cb50ce12220b95132f993a7f4a90c617e8f03668b32478b1ba815b2"
      },
      {
        "path": "pipelines/namaster_proof/blind_test/reveal2.py",
        "entrypoint": "NP_SEALED_DIR=sealed2 python3 reveal2.py",
        "sha256": "10dc181cb14c3352cf8269dd389ef6614ea22e869cceaf1a3b2cfc32475fb41a"
      }
    ],
    "environment": {
      "python": "python3.14 + numpy 2.5.1 + healpy 1.20.0 + scipy 1.18.0 (scipy used only for the Clopper-Pearson bounds in reveal2.py). NaMaster/pymaster is NOT required and is NOT installed: the test ships its own instrumented spin-0 MASTER estimator, which is a stated scope limit of the result.",
      "hardware": "cpu-only, any laptop"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation (macOS arm64)",
      "date": "2026-09-04",
      "wall_clock": "~11 s for 36 runs (1 reference + 35 blind); < 1 min including seal, verify and reveal",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "~1 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "To reproduce the committed batch exactly, skip seal2.py and reuse the revealed sealed2/{key.txt,assignment.json}: NP_SEALED_DIR=$PWD/sealed2 python3 run_blind2.py && python3 verify.py public2 && NP_SEALED_DIR=$PWD/sealed2 python3 reveal2.py, from pipelines/namaster_proof/blind_test/. A fresh seal2.py draws a new key and reproduces the statistics, not the committed digest."
    },
    "outputs": [
      {
        "locator": "pipelines/namaster_proof/blind_test/public2/sealed_digest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public2/frozen_rules_digest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public2/contract.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public2/runs",
        "type": "receipt",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public2/verdicts.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/public2/scorecard.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/blind_test/sealed2",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Exact, not tolerance-based. (1) reveal2.py re-derives the assignment from the revealed key and asserts sha256 == the digest committed BEFORE any run output existed (assignment_sha256 = c96b5bf1d6d3dd3f6b8131e6260803bb2049e3481b9613b041091ac00a27e9ee; seal_verified = true), and sha256(sealed2/key.txt) must equal key_file_sha256 = bbf6373bc64bf3fbd6614a06e6b3c33e6332be92c9f951f910ad3e6143b3c535. (2) The commit ordering is itself the audit trail: 4451b135 (rules frozen, alone) -> 28efa21c (seal commitment + scripts, no run output in tree) -> 27300504 (35 run outputs + blind verdicts) -> 974e2859 (key reveal + scorecard). (3) public2/scorecard.json must reproduce byte-identically: S1-S4 detection 20/20 (one-sided 95% lower bound 0.861), honest false positives 0/5 (one-sided 95% upper bound 0.451), S5 escapes 5/5, S6 escapes 5/5. (4) Every run's result/receipt pair must pass namaster_proof.receipts.verify_json_receipt.",
    "status": "runnable-now",
    "provenance": [
      "project-context/peer-reviews/INT_v3/P1B_v2B.0.17_R1_claude_opus_2026-09-04.md (referee MAJORs M1 post-hoc rule amendment, M2 seal priority, M3 implemented-vs-described R6, M4 missing effective-multipole class, M5 intervals — this batch answers them)",
      "pipelines/namaster_proof/blind_test/RULES_v2_FROZEN.md (frozen decision rules, committed alone in 4451b135)",
      "pipelines/namaster_proof/blind_test/BATCH2_PREREGISTRATION.md (design, S6 definition, scoring, expectations)",
      "reproducibility/manifests/experiments/p1b-blind-shortcut-detection.json (batch 1, now labelled the rule-development pilot round)",
      "pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md section 'Batch 2 (pre-registered)'"
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
        "locator": "packages/namaster-proof/examples/rebuild_workspace_check_2026-07-18_podA4000.receipt.json",
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
    "id": "p1b-pymaster-crosscheck-2026-09-05",
    "title": "PyMaster (NaMaster) cross-check of the in-house spin-0 MASTER estimator used by the P1B blind test, plus S6 effective-multipole shortcut error vs NaMaster",
    "program": "lab-infra",
    "paper": "P1B",
    "kind": "validation",
    "inputs": [
      {
        "name": "Alonso, Sanchez, Slosar et al. 2019 - NaMaster: a unified pseudo-Cl framework",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1809.09603",
        "checksum": null,
        "license": null
      },
      {
        "name": "In-house spin-0 MASTER estimator (honest path)",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/pcl.py",
        "checksum": null,
        "license": null
      },
      {
        "name": "S6 effective-multipole shortcut variant",
        "type": "internal-artifact",
        "locator": "pipelines/namaster_proof/blind_test/variants2.py",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/namaster_proof/blind_test/pymaster_crosscheck.py",
        "entrypoint": "MAMBA_ROOT_PREFIX=/tmp/mamba_root micromamba run -n pymaster_env python pipelines/namaster_proof/blind_test/pymaster_crosscheck.py",
        "sha256": "4c79aeaa43a5b78ead155caa2cc5dabab159ae0cedb076055c20aef1788e8db5"
      }
    ],
    "environment": {
      "python": "python3.11.16 (conda-forge, throwaway micromamba env pymaster_env) + numpy 2.4.6 + healpy 1.20.0 + namaster/pymaster 3.0.1",
      "hardware": "cpu-only; Apple M-series MacBook Air, macOS 25.5.0 arm64 (Houstons-MacBook-Air.local)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houstons-MacBook-Air.local",
      "date": "2026-09-05",
      "wall_clock": "under 1 minute (deterministic, small nside=64/lmax=95 run)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~1 min including one-time conda-forge namaster env creation (~2-4 min)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Homebrew pip has no macOS/arm64 pymaster wheel for Python 3.14 and the source build needs a working C toolchain plus GSL/FFTW/CFITSIO/HEALPix; conda-forge's namaster package ships prebuilt and is the reliable path. Deterministic: fixed seeds (mask_seed=11, map_seed=42), no external data or network calls beyond the one-time package install."
    },
    "outputs": [
      {
        "locator": "pipelines/namaster_proof/blind_test/pymaster_crosscheck_result.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/namaster_proof/PYMASTER_CROSSCHECK_2026-09-05.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm: (a) coupling_matrix.max_rel_diff <= 1e-11 (measured 4.25e-13) over l=2..95, i.e. the in-house pcl.coupling_matrix formula matches NaMaster's raw get_coupling_matrix() to floating-point round-off; (b) decoupled_bandpowers.max_rel_diff <= 1e-10 (measured 1.54e-12), i.e. pcl.decouple matches wsp.decouple_cell(); (c) s6_effective_multipole_vs_namaster shows every 8-wide band's max_rel_err_vs_namaster > 0.1 (worst band 2-9 measured 1.177, best band 90-95 measured 0.232), quantifying the S6 shortcut's error in NaMaster-verified terms rather than against the in-house exact result alone.",
    "status": "runnable-now",
    "provenance": [
      "project-context/peer-reviews/INT_v3/P1B_v2B.0.18_R2_TRUTH_AUDIT_2026-09-04.md, science item \"PyMaster cross-check (wheels resolve - feasible)\"",
      "pipelines/namaster_proof/PYMASTER_CROSSCHECK_2026-09-05.md (full tables, install record, paper-ready sentences)",
      "pipelines/namaster_proof/blind_test/pcl.py (honest MASTER estimator, unchanged), variants2.py (S6 shortcut, unchanged) - this cross-check reads both, modifies neither"
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
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/a2_transmission_summary.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm, in HEADLINE: T_fNL = 0.250000 (LQC / geometric dressed-metric prescription; analytic value exactly 1/4), 0.195501 (analytic non-LQC poly bounce), 0.165005 (Quintin+2015-type), and in F_fluid_scheme_contrast.SECOND_SCHEME_transmission T_fNL = 0.409155 (LQC background, effective-fluid scheme). Tolerance 1e-5 relative. Also confirm the analytic cross-checks in B_backgrounds (LQC: I_inf = pi/sqrt3, A = 1/12, rho_B = 1/2; poly: I_inf = pi*eta_b/4, rho_B = [pi/6+sqrt3/4]/(pi/2)) at <1e-6 relative, the fluid-scheme K ~ dcut^-0.4998, and that the direct ODE value matches the super-Hubble formula to <5e-3 over k*eta_B <= 0.03.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item #2 (ranked #1 in research/remaining_live_paths_audit/)",
      "extends research/cubic_bounce_transmission/ phases 1-3 (g1_gradient_transmission_scheme.py, g1_dressedmetric_transmission.py, g1_dressedmetric_ic_close.py)",
      "literature engaged: arXiv:1508.04141 (Quintin, Sherkatghanad, Cai & Brandenberger 2015), arXiv:1712.08148 (Agullo, Bolliet & Sreenath 2017), arXiv:1211.1354 / 1302.0254 (Agullo, Ashtekar & Nelson), arXiv:1206.2382 (Cai, Easson & Brandenberger 2012)",
      "brief: research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md (see §open for the intrinsic-cubic, AAN quantum-mass, and hybrid-LQC open items)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a2-lane-a-cubic-vertex-table",
    "title": "Track A2 lane (a): cubic-vertex table for zeta through a nonsingular bounce — coefficient poles at H=0, scheme regularisation, super-Hubble in-in reduction and S1 bounce-window estimate",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "a2_transmission_linear backgrounds",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": "sha256:bea7758b952eb6cd7c77f624ba8d31557916df5b0614cc60e6d1278105c8fca0"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane_a_vertex_table/cubic_vertex_table.py",
        "entrypoint": "python3 cubic_vertex_table.py",
        "sha256": "2418fb92830ae43016cd37532a965d3d1ffc474a5c54e0deaf09d571a23cd946"
      }
    ],
    "environment": {
      "python": "numpy 2.x, sympy 1.14.0, scipy (via a2_transmission_linear import) (repo requirements.txt)",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-03",
      "wall_clock": "2.0 s, measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 10 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic symbolic + quadrature; imports bg_quintin/bg_lqc/bg_poly from ../a2_transmission_linear.py."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/vertex_table.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/cubic_vertex_table.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md",
        "type": "document",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/REGULARISATION_ASSUMPTION.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm in the log: [B] eps = -1/(Upsilon t^2), eta_sr = 2 eps (Quintin); LQC Upsilon_eff = rho_c/2; [C] coefficient pole orders V1..V7 = -1,-4,-4,-4,-5,-6,-6 and R1..R4 = -2,-1,-2,-3; [D] S2 integrand poles V3 t^-4, V6/V7 t^-2 (non-integrable), V5 t^-3 (odd), V2/V4 finite; [E] leading squeezed kernel 5(-I_inf-3J)/(12 I_inf^2) for zeta zeta'^2; [F] Delta f_NL[V2,S1] = -0.139578 (Quintin, all dtB), -0.104167 (LQC = -5/48 exactly), closed form -(5/24) rho_B to <5e-5 (Quintin) and <2e-6 (LQC).",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item #2 second half (intrinsic bounce cubic contribution), lane (a) of three",
      "builds on research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md (manifest p2-a2-bounce-fnl-transmission) and phases g1_*.py; does not redo them",
      "in-in conventions: research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md",
      "literature: hep-th/0605045 Eq. 4.28-4.29; astro-ph/0503692 Eq. 51; astro-ph/0210603 Eq. 3.9-3.10; arXiv:1103.1102; arXiv:1103.4126; arXiv:1508.04141; arXiv:1712.08148; arXiv:1108.0893"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a2-lane-b-numerical-inin",
    "title": "Track A2 lane (b): numerical bounce-window in-in evaluation of Delta f_NL^bounce on the three A2 backgrounds — every vertex V1-V7 plus redefinition terms, scheme S1, with eta_*/window/step convergence tests and the S2 divergence diagnostic",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "a2_transmission_linear backgrounds + adiabatic-vacuum mode evolution",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": "sha256:bea7758b952eb6cd7c77f624ba8d31557916df5b0614cc60e6d1278105c8fca0"
      },
      {
        "name": "lane (a) vertex table + regularisation prescription (S1/S2, pole orders, closed form -(5/24) rho_B)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/vertex_table.json",
        "checksum": "sha256:dc7b99648f6c2c463bf3010f39adeb719860401ea108b4e393411ed95c50ea9e"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane_b_numerical/bounce_cubic_inin.py",
        "entrypoint": "python3 bounce_cubic_inin.py",
        "sha256": "a69b7f4b7e1743e54346a6351c5eb2e0299d3cafd3f3350da30bbec5e037f207"
      }
    ],
    "environment": {
      "python": "numpy 2.x, scipy (solve_ivp DOP853, CubicSpline, simpson), matplotlib (repo requirements.txt)",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-03",
      "wall_clock": "4.0 s, measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 15 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic ODE + quadrature; imports bg_quintin/bg_lqc/bg_poly and evolve() from ../a2_transmission_linear.py. No random seeds, no external data, no network."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/bounce_cubic_inin.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md",
        "type": "document",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/dfnl_bounce_quintin.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/dfnl_bounce_lqc.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/dfnl_bounce_poly.png",
        "type": "figure",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm in the log: gates Wronskian Im(mu* mu') = -0.50000000 on every leg, local redefinition F zeta^2 -> (5/3)F to <1e-12, triangle closure <1e-12; headline row k eta_B = 1e-3 gives V2 = -0.139586 (Quintin), -0.104198 (LQC), -0.126879 (poly) against lane (a)'s -(5/24) rho_B = -0.139581 / -0.104167 / -0.126875 (rel 3.3e-5 / 3.0e-4 / 3.4e-5); V1 and V5 identically zero in S1; V4 negative and V6+V7 positive but both <1.1e-4 of V2; totals Delta f_NL^bounce = -0.13982 / -0.10431 / -0.12711 and f_NL^after = -0.5008 / -0.6512 / -0.5548; eta_*-independence flat to 1.3-3.6 percent for eta_* >= 10 eta_B; step-size convergence 1e-8 or better; S2 V6+V7 d_cut log-log slope -1.005 to -1.007 (divergence, no regulated number).",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item #2 second half (intrinsic bounce cubic contribution), lane (b) of three; lane (c) (Horndeski/dressed-metric vertex corrections) remains open",
      "consumes lane (a): research/cubic_bounce_transmission/lane_a_vertex_table/ (manifest p2-a2-lane-a-cubic-vertex-table) — vertex table, S1/S2 schemes, closed form -(5/24) rho_B",
      "consumes A2 linear transfer: research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md (manifest p2-a2-bounce-fnl-transmission) — backgrounds, adiabatic vacuum, T_fNL = (1-rho_B)/2",
      "f_NL^before = -35/16 is an INPUT from ledger #1 (manifest p2-fnl-adjudication-inin-from-scratch), not recomputed",
      "in-in conventions: research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py Sec. 1",
      "corrects lane (a) Sec. 5: the S1 pure-time estimate '-(7/8)(5/24) rho_B' is not confirmed — the squeezed angular average of the V6/V7 kernels cancels the naive 1/8 weight to four digits"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a3-lane-9a-velocity-dip",
    "title": "Ledger row 9 (A3-1e) lane (a): does the Quintin+2015 scalar-field-velocity-dip amplification of zeta (their Eq. 79) exist on the lab's three A2 backgrounds, and what is the curvature-spectrum transfer in the band k eta_B in [0.1, 10] that the S1 super-Hubble result does not cover",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "a2_transmission_linear backgrounds (Quintin-type, LQC effective dust, poly non-LQC) + adiabatic-vacuum mode evolution + exact S/C matter-basis projection",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/a2_transmission_linear.py",
        "checksum": "sha256:bea7758b952eb6cd7c77f624ba8d31557916df5b0614cc60e6d1278105c8fca0"
      },
      {
        "name": "lane (b) numerical in-in Delta f_NL^bounce (the term this lane's transfer would modulate)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/bounce_cubic_inin.py",
        "checksum": "sha256:a69b7f4b7e1743e54346a6351c5eb2e0299d3cafd3f3350da30bbec5e037f207"
      },
      {
        "name": "Quintin, Sherkatghanad, Cai & Brandenberger 2015, PRD 92 063532 (Eqs. 30, 44, 79, 80 and the bounce-phase ansatz) -- literature input, quoted not recomputed",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1508.04141",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane9a_velocity_dip/lane9a_velocity_dip.py",
        "entrypoint": "python3 lane9a_velocity_dip.py",
        "sha256": "227ce03404683c35cc5f8e1c9fbced4b5b4c72ac61ac922910a2c3cb0159e76e"
      }
    ],
    "environment": {
      "python": "numpy 2.x, scipy (solve_ivp DOP853, CubicSpline), matplotlib (repo requirements.txt)",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-04",
      "wall_clock": "143.7 s, measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 4 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic ODE + projection; imports bg_quintin/bg_lqc/bg_poly, evolve(), zeta_at() from ../a2_transmission_linear.py. No random seeds, no external data, no network. Cost of the literature input is a single arXiv abs/HTML fetch."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane9a_velocity_dip/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9a_velocity_dip/lane9a_velocity_dip.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9a_velocity_dip/LANE9A_VELOCITY_DIP_2026-09-04.md",
        "type": "document",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9a_velocity_dip/lane9a_growth_vs_ketaB.png",
        "type": "figure",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm in the log: (1) Hdot is constant to 7.2e-06 across the whole NEC window on the Quintin-type background (Upsilon = 2.66667 for dtB = 1) and varies by a factor of order unity on LQC and poly, so the total-sector identification phidot^2 = -2 M_p^2 Hdot vanishes at eta_B and manufactures a divergent factor (2.2e10 on LQC, 7.6e3 on poly) -- the diagnostic that it is NOT Quintin's matter-sector phidot; (2) the adopted Eq. (79) factor is exactly 1 on all three backgrounds; (3) growth table lambda_zeta(k eta_B = 0.1, 0.3, 1) = 5.971/5.446/3.543 (Quintin), 3.919/3.553/4.582 (LQC), 4.898/3.722/0.952 (poly); (4) S1-deviation transfer G(k) band extremum 1.3281 at k eta_B = 0.768 (Quintin), 1.4965 at 0.611 (LQC), 0.2414 at 0.768 (poly), against small-k numerical floors |G-1| = 1.35e-02 / 2.18e-02 / 8.35e-04, i.e. Delta^2 ratios 1.76 / 2.24 / 0.058; (5) G -> 1 to better than 1 percent for k eta_B >= 3 on all three; (6) convergence rel dev <= 8.2e-08 for rtol 1e-11 -> 1e-9 and 0 for eta_far x2.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 9 (A3-1e), lane (a) of three; lane (b) = S2 regularisation (manifest p2-a3-lane-9b-s2-regularisation), lane (c) = comparison ledger",
      "extends research/cubic_bounce_transmission/lane_c_comparison/LANE_C_COMPARISON_2026-09-03.md Sec. 2.3 item 2, which recorded 'the lab's backgrounds carry no scalar-velocity dip' as an assertion; this lane derives it and quantifies the k eta_B ~ 1 transfer the S1 band never tested",
      "the assumption A1 of lane (b) (k eta_B <= 1e-2 super-Hubble transfer) is the object being probed here; this lane does NOT recompute the in-in bispectrum",
      "f_NL^before = -35/16 remains an INPUT from ledger #1, not recomputed"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a3-lane-9b-s2-regularisation",
    "title": "Track A3 (ledger row 9 / A3-1e) lane 9b: is the effective-fluid (S2) divergence of Delta f_NL^bounce physical? Exact S2 modes at H=0, regularity of the comoving-gauge constraint solutions, total-derivative origin of the Maldacena-form poles",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "lane (a) cubic-vertex table (coefficients, S2 pole counting)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_a_vertex_table/cubic_vertex_table.py",
        "checksum": "sha256:2418fb92830ae43016cd37532a965d3d1ffc474a5c54e0deaf09d571a23cd946"
      },
      {
        "name": "lane (b) S2 divergence report (d_cut slope -1.005..-1.007)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane9b_s2_regulation/lane9b_s2_regulation.py",
        "entrypoint": "python3 lane9b_s2_regulation.py",
        "sha256": "36f79edc6c86353d328a9bcfe76fb51eb7e8ef36907f0b5a37f643ccb72fb428"
      }
    ],
    "environment": {
      "python": "sympy 1.14.0 (repo requirements.txt); no numpy/scipy needed",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-04",
      "wall_clock": "1 s, measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 10 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic symbolic (Frobenius series to O(t^9), Laurent residues). Self-contained; does not import lane (a)."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane9b_s2_regulation/lane9b_s2_regulation.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9b_s2_regulation/lane9b_s2_regulation.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9b_s2_regulation/LANE9B_S2_REGULATION_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm in the log: [A] Frobenius indicial exponents 0 and 3; zetadot|C1 = c_s^2 k^2 t (not ~H^2), zetadot|C2 = 3 t^2; MS residual 0 through O(t^2). [B] Res[-zeta/H]_C1 = -1/Upsilon, Res[chi]_C1 = +1/Upsilon, sum 0; psi = -zeta/H + chi regular (leading t^1 for C1, t^0 for C2); N1 regular. [C] Maldacena-form poles on exact [C1^3] modes: V2 t^-2, V3 t^-4, V4 t^-2, V5 t^-4, V6+V7 t^-4 (all even, non-integrable); lane-(a) [C1,C2,C2] weights reproduce V2 t^0, V6+V7 t^-2. [D] all raw-ADM building blocks (zeta, zetadot, N1, psi, H, phidot^2, V, a) regular at t=0. Verdict string: 'S2 REGULARISED-IN-FORM / VALUE UNRESOLVED'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 9 (A3-1e), lane (b): contested math — S2 regularisation of Delta f_NL^bounce",
      "builds on research/cubic_bounce_transmission/lane_a_vertex_table/REGULARISATION_ASSUMPTION.md and lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md (manifests p2-a2-lane-a-cubic-vertex-table, p2-a2-lane-b-numerical-inin); does not redo them",
      "linear-order antecedent: research/cubic_bounce_transmission/g1_gradient_transmission_scheme.py (S2 gradient-transmission coefficient ~ d_cut^-1)",
      "literature (transcribed, not re-derived): astro-ph/0210603 Eq. 2.9-2.14, 3.8-3.10; hep-th/0605045 Eq. 3.5-3.6, 4.28-4.29; astro-ph/0503692 Eq. 51; arXiv:1406.2790; arXiv:1508.04141 (equation numbers NOT asserted; audit item)",
      "named next step: raw-ADM-form in-in bounce-window integral on exact S2 modes (lane-(b)-class numerical job) — the finite S2 value is not computed here and equality with S1 -(5/24) rho_B is not claimed"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a3-lane-9b2-s2-rawadm",
    "title": "Track A3 (ledger row 9 / A3-1e) lane 9b-2: scheme-S2 (effective-fluid MS variable) bounce-window cubic contribution from the RAW ADM cubic Lagrangian on exact S2 modes, end-to-end in-in through the Quintin-type bounce, compared with scheme S1's -(5/24) rho_B",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "lane 9b finding (S2 divergence = total-derivative pole; raw ADM form finite on exact S2 modes; Frobenius data)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane9b_s2_regulation/lane9b_s2_regulation.py",
        "checksum": "sha256:36f79edc6c86353d328a9bcfe76fb51eb7e8ef36907f0b5a37f643ccb72fb428"
      },
      {
        "name": "lane (b) S1 numbers, in-in conventions, window/eta* tests (Quintin rho_B = 0.6700, -(5/24) rho_B = -0.1396, f_NL^after = -0.5002)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/results.json",
        "checksum": null
      },
      {
        "name": "lane (b) in-in engine (conventions reproduced: -2 Im commutator, 3! attachments once, f_NL = (5/6) B / sum PP)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane_b_numerical/bounce_cubic_inin.py",
        "checksum": "sha256:a69b7f4b7e1743e54346a6351c5eb2e0299d3cafd3f3350da30bbec5e037f207"
      },
      {
        "name": "adjudicated matter-contraction value f_NL = -35/16 (ledger #1; used as an independent gate, not an input)",
        "type": "internal-artifact",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/lane9b2_s2_rawadm.py",
        "entrypoint": "python3 lane9b2_s2_rawadm.py",
        "sha256": "44b848063978e912770ed535a99f762765bc7b7e3ee96aee1be240c59c2f9d62"
      }
    ],
    "environment": {
      "python": "numpy, scipy (special.hankel1/2, erf, integrate.simpson), sympy 1.14, matplotlib (repo requirements.txt)",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-04",
      "wall_clock": "25 s, measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic. Symbolic raw ADM expansion (sympy, 184-term cubic Fourier kernel) + exact S2/S1 modes (analytic matter modes, power series through H=0, well-conditioned real matter basis after the bounce) + Simpson in-in on real t (window/expansion) and on a damped contour eta_m = eta_m0 + s(1 - i delta) (contraction)."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/lane9b2_s2_rawadm.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/integrand_across_bounce.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/dfnl_bounce_s2_vs_ketaB.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/LANE9B2_S2_RAWADM_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm in the log: gate (i-a) both constraint solutions derived from the raw quadratic Fourier Lagrangian (N1 = zetadot/H, psi = -zeta/H - a^2 eps zetadot/k^2) -> True/True. Gate (i-b) power-law inflation eps in {0.1, 0.2}: raw/Maldacena-form - 1 = O(1e-4) after (k eta*)^2 extrapolation, Maldacena form vs consistency relation (5/6) eps/(1-eps) within 1e-3, contour independence ~5e-6. Gate (i-c) S1 Maldacena-form window integral = lane b bulk to 3e-5 at k eta_B = 1e-3; |zeta_after/zeta(-tm)| = 6.06 = 2/(1-rho_B). Gate (i-b') raw contraction-only f_NL at -tm = -2.18728 vs -35/16 (1e-4). Gate (i) literal: raw form on S1 pseudo-variables has an odd |t|^-1 pole at H = 0 -> VOID. S2: NEC-window raw +1.640 (k eta_B = 1e-3), f_NL^before -2.18728, f_NL^after -1.2488, |lambda| = 0.9696, Delta_T = +1.007; step convergence 1e-10; window scan [-0.5..2] tm spans -0.30..-4.80 (window-convention dependence, reported). Verdict string starts 'S2 != S1'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 9 (A3-1e), lane 9b named next step: raw-ADM-form in-in bounce-window integral on exact S2 modes",
      "builds on manifests p2-a3-lane-9b-s2-regularisation, p2-a2-lane-b-numerical-inin, p2-a2-lane-a-cubic-vertex-table; does not redo them",
      "literature (transcribed, not re-derived): astro-ph/0210603 Eq. 2.4, 2.9-2.14 (raw ADM action, constraint solutions), consistency relation f_NL^sq = (5/12)(1 - n_s) (Maldacena 2003; Creminelli & Zaldarriaga 2004) used only as an engine gate on an exact power-law background",
      "the S1 pseudo-scheme (eps_eff = 1/2, z = a) has no raw-ADM counterpart: its modes have zetadot(0) != 0 so N1 = zetadot/H is singular at H = 0; S1 remains a Maldacena-form-defined assumption-labelled anchor (lane a wording stands)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-a3-row18a-s2-tensor-transfer",
    "title": "Track A3 (ledger row 18a / A3-S2r): tensor transfer through the Quintin-type bounce and the like-for-like post-bounce tensor-to-scalar ratio r_after per scalar continuation scheme (S1 geometric z=a vs S2 effective-fluid MS variable), including the c_s dependence",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "lane 9b-2 exact S2 scalar modes, Quintin-type background, S1 reference rho_B = 0.6699892 (imported as a module; single source of truth for the background and both scalar schemes)",
        "type": "internal-artifact",
        "locator": "research/cubic_bounce_transmission/lane9b2_s2_rawadm/lane9b2_s2_rawadm.py",
        "checksum": "sha256:44b848063978e912770ed535a99f762765bc7b7e3ee96aee1be240c59c2f9d62"
      },
      {
        "name": "row 10 tensor/scalar transfer on the poly and LQC backgrounds (T_h = T_zeta[S1] to 8.5e-9, r_before = r_after = 24) used as an independent cross-check, not as an input",
        "type": "internal-artifact",
        "locator": "research/track_a3_multichannel/row10_r_ns/row10_r_ns.py",
        "checksum": "sha256:4554ac9add31704f973be6b4118d3c814aad2e15baa4b9f7db591eacc63d54b3"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/cubic_bounce_transmission/row18a_s2_tensor/row18a_s2_tensor.py",
        "entrypoint": "python3 row18a_s2_tensor.py",
        "sha256": "0220439c3ee5bf3444a8919448e5ddd4caeeb5f4362a652253f40b54ae4602f3"
      }
    ],
    "environment": {
      "python": "numpy, scipy (integrate.solve_ivp DOP853, special.erf), matplotlib (repo requirements.txt)",
      "hardware": "cpu-only; no GPU, no network"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": null,
      "date": "2026-09-04",
      "wall_clock": "0.1 s, measured",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 10 s",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic. Tensor mode solved as the regular first-order system hdot = Pi/a^3, Pidot = -a k^2 h in cosmic time (DOP853, rtol 1e-12) between the |t| = tm junctions, with exact matter-phase solutions outside; scalar S1/S2 transmissions from the imported lane 9b-2 BounceModes. A constant c_s enters the scalar problem only as k -> c_s k."
    },
    "outputs": [
      {
        "locator": "research/cubic_bounce_transmission/row18a_s2_tensor/results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/row18a_s2_tensor/row18a_s2_tensor.log",
        "type": "log",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/row18a_s2_tensor/row18a_s2_tensor.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "research/cubic_bounce_transmission/row18a_s2_tensor/ROW18A_S2_TENSOR_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and confirm in the log: lam_T = 6.0585966 / 6.0470743 / 5.9171128 at k eta_B = 1e-3 / 3e-3 / 1e-2, equal to lam_zeta^S1 to |ratio - 1| <= 1.4e-14 at every k (the tensor equation and the S1 scalar equation with z = a are the same ODE); lam_zeta^S2 = 0.9695759 / 0.9677642 / 0.9473239 reproducing lane 9b-2's 0.9696 / 0.9678 at the two smallest k; r_after^S1 = 24.00000 at every k and r_after^S2 = 937.11 / 937.05 / 936.34; c_s scan at k eta_B = 1e-3 gives lam_T unchanged (6.0585966, c_s does not appear in the tensor equation) and lam_zeta^S2 = 0.9695759 / 0.9696239 / 0.9697210 / 0.9697587 at c_s = 1 / 0.888 / 0.6 / 0.44 (a 1.9e-4 relative spread), r_after^S2 = 937.11 / 937.02 / 936.83 / 936.76.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 18 item (a) A3-S2r, raised by the R7 truth-audit: the paper's r_after was stated with S1 transfers only",
      "builds on manifests p2-a3-lane-9b2-s2-rawadm (exact S2 modes, background, rho_B) and the row-10 tensor/scalar transfer computation; does not redo either",
      "no S2 r_after is quoted for the LQC or poly backgrounds: lane 9b-2 assumption (A1) is that their Hdot = 0 crossings put z^2[S2] = 0 and give the S2 zeta a logarithmic point, so exact S2 modes were never constructed there",
      "r_before = 24 is row 10's pure-dust r = 24(1+w) at w = 0; no tuning of any transfer toward any target value"
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
    "id": "p2-fnl-adjudication-inin-from-scratch",
    "title": "Adjudication of the matter-contraction local f_NL: from-scratch in-in (validated on de Sitter and USR), delta-N on both slicings, long-mode shear — NEXT_SCIENCE_LEDGER #1 closure",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Cai, Xue, Brandenberger & Zhang 2009 (arXiv source matterbounceng2.tex, v2) — used for: Eqs. 14-15 (mode function, cubic action), 20-21 (f_NL convention), 25-36 (per-vertex rows, read only for COMPARISON after the from-scratch computation), 37 (printed total), 38-40 (quoted amplitudes -35/8, -255/64, -9/4)",
        "type": "external-literature",
        "locator": "https://arxiv.org/e-print/0903.0631"
      },
      {
        "name": "Li, Quintin, Wang & Cai 2016 (arXiv source) — used for: Eq. 4.19 total shape function and Eq. 5.1 f_NL^local = -165/16 + 65/(8 c_s^2), independence audit",
        "type": "external-literature",
        "locator": "https://arxiv.org/e-print/1612.02036"
      },
      {
        "name": "Quintin, Sherkatghanad, Cai & Brandenberger 2015 (arXiv source) — used for: independence audit: the -35/16 there is a quotation attributed to Cai 2009, not a computation",
        "type": "external-literature",
        "locator": "https://arxiv.org/e-print/1508.04141"
      },
      {
        "name": "Maldacena 2003 (arXiv source) — used for: cubic action; de Sitter three-point benchmark A_eps used to VALIDATE the machinery before use",
        "type": "external-literature",
        "locator": "https://arxiv.org/e-print/astro-ph/0210603"
      },
      {
        "name": "Namjoo, Firouzjahi & Sasaki 2012 — used for: ultra-slow-roll benchmark f_NL = 5/2 used to VALIDATE the field-redefinition term in a non-attractor phase",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1210.3692"
      },
      {
        "name": "Chen, Firouzjahi, Namjoo & Sasaki 2013 — used for: non-attractor in-in context (field-redefinition dominance, consistency-relation violation)",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1301.5699"
      },
      {
        "name": "lab second-method delta-N (uniform-density slices) — used for: separate-universe system and the -55/16 result, reproduced here for general eps and compared with the comoving-slice delta-N",
        "type": "internal-artifact",
        "locator": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.py (commit d7dac953)"
      },
      {
        "name": "BigBounce Paper 2 Appendix A + scripts/p2_vertex_check.py — used for: per-vertex table tab:vertexwalk and Eq. vertexsum, reproduced exactly; 'spurious term' narrative corrected",
        "type": "internal-artifact",
        "locator": "research/focused_paper_source_integration/02_full_draft.tex"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
        "entrypoint": "python3 research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py",
        "sha256": "67dd4842aaa7978310c7ead714d666bff6ab8fc523e7d0bb815844fa517264fc"
      }
    ],
    "environment": {
      "python": "python3.14 with sympy 1.14.0 (in repo requirements.txt); multiprocessing fork context (8 worker processes for the vertex integrals)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-02",
      "wall_clock": "131.6 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "2-5 minutes (exact sympy; eight parallel vertex integrations)",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Fully deterministic exact-rational computation. No network access at run time (the arXiv sources were read once during authorship; only the f_NL convention and, for comparison AFTER the computation, Cai's rows / Eq. 37 / quoted numbers and Li's Eq. 4.19 are transcribed into the script). The script asserts: mode functions solve the EOM; de Sitter total equals Maldacena's A_eps identically; USR redefinition gives f_NL = 5/2; the eps^3 kernel identity holds; divergent imaginary parts cancel; no logarithm at leading order; the delta-N ODE residual vanishes."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required exact values: validation_deSitter_Maldacena == PASS; validation_USR_Namjoo == PASS; in_in_from_scratch.f_local_squeezed_isoceles == '-35/16'; f_equilateral == '-255/128'; f_folded == '-9/8'; f_squeezed_fixed_angle_mu == '15*mu**2/16 - 35/16'; every cai_row_differences value == '0'; cai_eq37_minus_total_distinct_monomial_reading == '0'; li_eq419_minus_total_at_cs1 == '0'; paper2_vertexwalk_table_reproduced == true; delta_N.comoving_slicing_fNL_eps_3_2 == '-5'; delta_N.uniform_density_slicing_fNL_general_eps == '5*(epsilon - 7)/8'; delta_N.linear_ratio_zeta_rho_over_zeta_c == '2'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 1 (independent derivation of the matter-contraction f_NL) — adjudication step",
      "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.md §8 items 1-2 (the two open computations named there)",
      "directive R (vision governance) and directive Q2 (reproducibility manifests)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-fnl-monopole-adjudication",
    "title": "Adjudication of the squeezed-limit monopole of the matter-contraction f_NL: in-in (-15/8) vs comoving delta-N (-5) via the classical O(k^0) super-Hubble kernel with L/K/X tagging",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "lab in-in adjudication (2026-09-02)",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.json (commit aa2987cf)",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab second-method delta-N (2026-09-02)",
        "locator": "research/theory_audit/fnl_matter_contraction_second_method_2026_09_02.md (commit d7dac953)",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab Bianchi-I separate universe (2026-09-03)",
        "locator": "research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.md (commit 866cf342)",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "Maldacena 2003",
        "locator": "https://arxiv.org/abs/astro-ph/0210603",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Namjoo, Firouzjahi & Sasaki 2012",
        "locator": "https://arxiv.org/abs/1210.3692",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lyth, Malik & Sasaki 2005",
        "locator": "https://arxiv.org/abs/astro-ph/0411220",
        "type": "external-literature",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.py",
        "entrypoint": "python3 research/theory_audit/fnl_monopole_adjudication_2026_09_03_general_eps.py && python3 research/theory_audit/fnl_monopole_adjudication_2026_09_03.py",
        "sha256": "058447db00cb61978e05dd0503983ebbe29a558abfd94ad5270fd87e5c3880aa"
      },
      {
        "path": "research/theory_audit/fnl_monopole_adjudication_2026_09_03_general_eps.py",
        "entrypoint": "python3 research/theory_audit/fnl_monopole_adjudication_2026_09_03_general_eps.py",
        "sha256": "0c30afe73b8080e5443fa2af28461782a8a5a01bdebe147830f57f5563d447d7"
      }
    ],
    "environment": {
      "python": "python3 with sympy (>=1.12; run on sympy 1.14.0)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-03",
      "wall_clock": "15 s + 8 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 minute",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic exact sympy; no network. Run the general-eps companion first (main script reads its JSON in Section 9). Self-validates: USR gives 5/2; attractor has no O(k^0) source; the full O(k^0) kernel and every per-vertex row equal lane A's in-in JSON (asserted); 1/k_L poles cancel across classes (asserted); delta-N_c/zeta_Maldacena = 1 - eps/3 (asserted)."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03_general_eps.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSONs. Required exact values: validation_USR.f_NL == '5/2'; validation_vs_laneA_inin.A_total_difference == '0'; matter_classical_O_k0.f_squeezed_mu == '15*mu**2/16 - 35/16'; squeezed_tagging.class_L_f_mu == '-25/8'; class_K_f_mu == '0'; class_X_f_mu == '15*mu**2/16 + 15/16'; deltaN_checks.linear_map_deltaNc_over_zetaMaldacena == '1 - epsilon/3'; general_eps.total.f_mu_eps == '5*(epsilon**2*mu**2 - epsilon**2 + 6*epsilon - 12)/12'; general_eps.L_minus_deltaNc == '5*epsilon/4'; general_eps.inin_over_laneC_quadrupole == 'epsilon/3'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 1 (A3-2 amendment: -25/8 monopole gap OPEN; this work closes it)",
      "research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.md §4 item 2 (the advection/projection prescription = class [X] here)",
      "directive R (vision governance) and directive Q2 (reproducibility manifests)",
      "input 'lab in-in adjudication (2026-09-02)' used ONLY for the post-hoc per-vertex comparison in script Section 4",
      "input 'Lyth, Malik & Sasaki 2005' used for: the gradient-expansion assumption that the shift is first order in gradients — the assumption shown to fail for the non-attractor growing mode in comoving gauge",
      "input 'Namjoo, Firouzjahi & Sasaki 2012' used for: USR f_NL = 5/2 benchmark (validation of both the classical kernel and the delta-N ODE system)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p2-fnl-second-method-deltan",
    "title": "Independent second-method matter-contraction f_NL (separate-universe / nonlinear delta-N) — NEXT_SCIENCE_LEDGER #1",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Cai, Xue, Brandenberger & Zhang 2009 — Eqs. (14),(20),(21),(37),(39): f_NL convention, printed shape function, published -35/8",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/0903.0631",
        "checksum": null
      },
      {
        "name": "Li, Quintin, Wang & Cai — Eq. (5.1) f_NL^local = -165/16 + 65/(8 c_s^2) -> -35/16 at c_s=1",
        "type": "external-literature",
        "locator": "https://arxiv.org/abs/1612.02036",
        "checksum": null
      },
      {
        "name": "BigBounce Paper 2 manuscript — Appendix A four-vertex re-summation (-35/16) for the reconciliation table",
        "type": "internal-artifact",
        "locator": "research/focused_paper_source_integration/02_full_draft.tex",
        "checksum": null
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
        "type": "document",
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
        "locator": "research/cubic_bounce_transmission/g1_gradient_transmission.log",
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
    "id": "p3-flagship-s8-allwise-photometry",
    "title": "AllWISE (VizieR) photometry join for the S>8 enriched sample [SAMPLE-V1, provenance under review]",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "flagship_sample_s8_enriched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_sample_s8_enriched.parquet",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "VizieR AllWISE (astroquery)",
        "endpoint": "https://vizier.cds.unistra.fr",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py",
        "entrypoint": "python3 build_flagship_sample.py --wise-join (pod-side; see phase3.log)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pandas, pyarrow, numpy (RunPod bootstrap.log for exact pins)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T13:19Z to 2026-09-03T15:17Z (~1h58m)",
      "actual_cost_usd": 0.34
    },
    "reproduction": {
      "recommended_venue": "local-cpu",
      "est_wall_clock": "~2h",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Network-bound VizieR query; no GPU required."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_wise.parquet",
        "type": "catalog",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_wise_manifest.json",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "Row count in flagship_wise.parquet cross-checked against flagship_wise_manifest.json at commit time.",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_wise_manifest.json"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-s8-enrichment",
    "title": "S>8 flagship anomaly sample enrichment (photometry/spectroscopy/morphology join) [SAMPLE-V1, provenance under review]",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "analysis",
    "inputs": [
      {
        "name": "flagship_sample_s8.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_sample_s8.parquet",
        "checksum": null,
        "license": null
      },
      {
        "name": "DESI zcatalog/target coordinates",
        "type": "external-dataset",
        "locator": "DESI internal zcatalog (pod-local, bound by input_sample_sha256 in flagship_enriched_manifest.json)",
        "checksum": "b5144115aba9ba18201496d166f2e501ba7657759ca56539aa548dd731090fae",
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py",
        "entrypoint": "python3 build_flagship_sample.py --enrich (pod-side; see phase3.log)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pandas, pyarrow, numpy (RunPod bootstrap.log for exact pins)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-02",
      "wall_clock": "2026-09-02T18:08Z to 2026-09-03T03:50Z (~9h42m)",
      "actual_cost_usd": 1.65
    },
    "reproduction": {
      "recommended_venue": "runpod-a4000-or-equivalent",
      "est_wall_clock": "~10h",
      "est_cost_usd": 1.7,
      "parallelizable": false,
      "resume_support": true,
      "notes": "enrich_checkpoint.json supports resume; contract_sha256/model_sha256/inference_code_sha256 in flagship_enriched_manifest.json bind exact reproduction inputs."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_sample_s8_enriched.parquet",
        "type": "catalog",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_enriched_manifest.json",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "flagship_enriched_manifest.json MSE cross-check: 0 offenders / 3810 rows checked (tolerance 1e-6); groups 3128/3128 completed, 0 skipped.",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_enriched_manifest.json",
      "project-context/PHASE3_LANDING_2026-09-03.md",
      "project-context/SESSION_HANDOFF_2026-09-02.md#Phase-3-landing-runbook"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-s8-simbad-ned-crossmatch",
    "title": "SIMBAD/NED positional cross-match of the S>8 enriched sample [SAMPLE-V1, provenance under review]",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "flagship_sample_s8_enriched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_sample_s8_enriched.parquet",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [
      {
        "name": "SIMBAD (astroquery)",
        "endpoint": "http://simbad.u-strasbg.fr/simbad/sim-tap",
        "auth_required": false
      },
      {
        "name": "NED (astroquery)",
        "endpoint": "https://ned.ipac.caltech.edu",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py",
        "entrypoint": "python3 build_flagship_sample.py --crossmatch-simbad-ned (pod-side; see phase3.log)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "pandas, pyarrow, numpy (RunPod bootstrap.log for exact pins)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T03:50Z to 2026-09-03T13:19Z (~9h29m)",
      "actual_cost_usd": 1.61
    },
    "reproduction": {
      "recommended_venue": "local-cpu-or-runpod",
      "est_wall_clock": "~9-10h (network-bound VizieR/SIMBAD/NED rate limits)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Network-bound; can run on any host with internet access, no GPU required despite pod venue used originally."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_crossmatch_matched.parquet",
        "type": "catalog",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_crossmatch_unmatched.parquet",
        "type": "catalog",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_crossmatch_manifest.json",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "92/3810 matched (2.4%), 3718 unmatched, counts sum to input row count 3810 (see PHASE3_BENCHMARK_SUMMARY.md).",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_crossmatch_manifest.json",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark/PHASE3_BENCHMARK_SUMMARY.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-s8-taxonomy",
    "title": "Descriptive taxonomy (UMAP + clustering, Q1 labels) of the S>8 unmatched population [SAMPLE-V1, provenance under review]",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "analysis",
    "inputs": [
      {
        "name": "flagship_crossmatch_unmatched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_crossmatch_unmatched.parquet",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/build_flagship_sample.py",
        "entrypoint": "python3 build_flagship_sample.py --taxonomy (pod-side; see phase3.log; sklearn 1.9.0, umap_learn 0.5.12, numpy 2.4.6)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy==2.4.6, scikit-learn==1.9.0, umap-learn==0.5.12",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T15:17Z to 2026-09-03T15:18Z (~1min)",
      "actual_cost_usd": 0.003
    },
    "reproduction": {
      "recommended_venue": "local-cpu",
      "est_wall_clock": "~1-5min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fast, CPU-only clustering step; deterministic given the pinned sklearn/umap-learn versions and fixed input."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_taxonomy.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_taxonomy_manifest.json",
        "type": "receipt",
        "checksum": null
      }
    ],
    "verification": "8 families with sizes 1589/1032/556/239/142/80/47/33 summing to 3718 (matches SIMBAD/NED-unmatched row count).",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_taxonomy_manifest.json",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark/PHASE3_BENCHMARK_SUMMARY.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-v2-allwise-photometry",
    "title": "AllWISE (VizieR) photometry join for the S>3 v2 science-only sample",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "flagship_sample_v2_enriched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet",
        "checksum": "c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff",
        "license": null
      }
    ],
    "apis": [
      {
        "name": "AllWISE II/328 (VizieR, astroquery)",
        "endpoint": "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/wise_join_flagship.py",
        "entrypoint": "python3 wise_join_flagship.py (pod-side, stage 06_WISE; radius_arcsec=3.0, astroquery.vizier.Vizier)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astroquery==0.4.11, pandas, pyarrow, numpy",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T23:14:03Z to 2026-09-03T23:55:02Z (~41m)",
      "actual_cost_usd": 0.12
    },
    "reproduction": {
      "recommended_venue": "local-cpu",
      "est_wall_clock": "~40-45min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": true,
      "notes": "Network-bound VizieR query; no GPU required; wise_checkpoint.json supports resume (checkpoint_every=50)."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_wise_v2.parquet",
        "type": "catalog",
        "checksum": "1b42125d5e62830cf44806a842b7253e787ec218c77b3a19e690eed4fedb40f3"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_wise_v2_manifest.json",
        "type": "receipt",
        "checksum": "b060c1f5395b131865eef57fb7678f02349d69e891b6ad2dc8360eccc1a92290"
      }
    ],
    "verification": "Row count in flagship_wise_v2.parquet cross-checked against flagship_wise_v2_manifest.json at landing time (2026-09-03).",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_wise_v2_manifest.json",
      "project-context/PHASE3_V2_LANDING_2026-09-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-v2-enrichment",
    "title": "S>3 flagship anomaly sample enrichment (photometry/spectroscopy/morphology join) [SAMPLE-V2, science-only, contamination-fixed]",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "analysis",
    "inputs": [
      {
        "name": "flagship_sample_v2.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2.parquet",
        "checksum": "d6d43dfa04d6a8b2b4d014f5f4899b5e5b844144a50b6c88e01a9a771a6baa5f",
        "license": null
      },
      {
        "name": "DESI zcatalog/target coordinates",
        "type": "external-dataset",
        "locator": "DESI internal zcatalog (pod-local, bound by zcatalog_sha256 in flagship_enriched_v2_manifest.json)",
        "checksum": "2d95ad99361039b556c402b49e0e7c84df5f00106dc5731d44476a58b128b49b",
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/enrich_flagship_sample.py",
        "entrypoint": "python3 enrich_flagship_sample.py (pod-side, stage 04_ENRICH; see pod_phase3_v2.sh)",
        "sha256": "3e7efb243fa5cc4e7e06c5ce8e13f011e1173d2cc44aecd8df47e0c67c0ab996"
      }
    ],
    "environment": {
      "python": "pandas, pyarrow, numpy (RunPod pod bootstrap for exact pins)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T17:06:50Z to 2026-09-03T19:49:52Z (~2h43m)",
      "actual_cost_usd": 0.46
    },
    "reproduction": {
      "recommended_venue": "runpod-a4000-or-equivalent",
      "est_wall_clock": "~2h45m",
      "est_cost_usd": 0.5,
      "parallelizable": false,
      "resume_support": true,
      "notes": "enrich_checkpoint.json supports resume; contract_sha256/model_sha256/inference_code_sha256/zcatalog_sha256 in flagship_enriched_v2_manifest.json bind exact reproduction inputs. Sample built by 03_CHOOSE_THRESHOLD_AND_BUILD, which passed gates/check_sample_provenance.py clean (status: clean) -- the fix for SAMPLE-V1 negative-TARGETID contamination."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet",
        "type": "catalog",
        "checksum": "c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_enriched_v2_manifest.json",
        "type": "receipt",
        "checksum": "243495ac59987d9a7b461adca1e11668c47cb09cee30b64141cf224f5c9733c5"
      }
    ],
    "verification": "flagship_enriched_v2_manifest.json MSE cross-check: 0 offenders / 1244 rows checked (tolerance 1e-6); groups 752/752 completed, 0 skipped. input_sample_sha256 matches flagship_sample_v2.parquet's own hash.",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_enriched_v2_manifest.json",
      "project-context/PHASE3_V2_LANDING_2026-09-03.md",
      "project-context/ANOMALY_SAMPLE_CONTAMINATION_2026-09-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-v2-simbad-ned-crossmatch",
    "title": "SIMBAD/NED positional cross-match of the S>3 v2 science-only sample",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "crossmatch",
    "inputs": [
      {
        "name": "flagship_sample_v2_enriched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet",
        "checksum": "c3b176ff2d355a421ac48d00c5b6565fdfce8956fe6298eb85596bfb94f09fff",
        "license": null
      }
    ],
    "apis": [
      {
        "name": "SIMBAD (astroquery)",
        "endpoint": "astroquery.simbad.Simbad (v0.4.11)",
        "auth_required": false
      },
      {
        "name": "NED (astroquery)",
        "endpoint": "astroquery.ipac.ned.Ned (v0.4.11)",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/crossmatch_flagship.py",
        "entrypoint": "python3 crossmatch_flagship.py (pod-side, stage 05_CROSSMATCH; radius_arcsec=3.0)",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astroquery==0.4.11, pandas, pyarrow, numpy",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T19:49:52Z to 2026-09-03T23:14:03Z (~3h24m)",
      "actual_cost_usd": 0.58
    },
    "reproduction": {
      "recommended_venue": "local-cpu-or-runpod",
      "est_wall_clock": "~3-4h (network-bound VizieR/SIMBAD/NED rate limits, 1.0s sleep between queries, radius 3.0 arcsec)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": true,
      "notes": "Network-bound; crossmatch_ckpt/ supports resume. No GPU required despite pod venue used originally."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_matched.parquet",
        "type": "catalog",
        "checksum": "4a718d1a7ad253d2f91c69841d81e3b8015650fc0ca1f4a711fa0ee9da17f135"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_unmatched.parquet",
        "type": "catalog",
        "checksum": "c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_manifest.json",
        "type": "receipt",
        "checksum": "dc9734decafa79cb803370d977ec8d7fa88a20fa8444a4de86175e8f513480c9"
      }
    ],
    "verification": "569/1244 matched (45.7%: n_ned_found=562, n_simbad_found=38), 675 unmatched (54.3%), counts sum to input row count 1244 (see PHASE3_V2_BENCHMARK_SUMMARY.md). Match rate is 19x higher than the v1 S>8 sample's 2.4%, consistent with v2's science-only provenance gate having removed sky-fiber contamination.",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_manifest.json",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/PHASE3_V2_BENCHMARK_SUMMARY.md",
      "project-context/PHASE3_V2_LANDING_2026-09-03.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p3-flagship-v2-taxonomy",
    "title": "Descriptive taxonomy (UMAP + clustering, 25 clusters -> 8 families) of the S>3 v2 science-only unmatched population",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "analysis",
    "inputs": [
      {
        "name": "flagship_crossmatch_v2_unmatched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_crossmatch_v2_unmatched.parquet",
        "checksum": "c0a6b57bd672f81b1424a65449f99d891810073ea59e600c1fc35cfec30eb7c3",
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/taxonomy_flagship.py",
        "entrypoint": "python3 taxonomy_flagship.py (pod-side, stage 07_TAXONOMY; umap_neighbors=15, umap_min_dist=0.05, score_tier_quantiles=[0.5,0.8,0.95])",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy==2.4.6, scikit-learn==1.9.0, umap-learn==0.5.12",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "runpod",
      "gpu": "a4000",
      "pod_id_or_host": "8ofv5d4ynu7hku",
      "date": "2026-09-03",
      "wall_clock": "2026-09-03T23:55:02Z to 2026-09-03T23:55:28Z (~26s)",
      "actual_cost_usd": 0.001
    },
    "reproduction": {
      "recommended_venue": "local-cpu",
      "est_wall_clock": "~1-5min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fast, CPU-only clustering step; deterministic given the pinned sklearn/umap-learn versions and fixed input."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_taxonomy_v2.json",
        "type": "result-json",
        "checksum": "1420388b59f3727814dda63c90c8e4cd0d2226c1e6ad2907c3301ed844edbf60"
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_taxonomy_v2_manifest.json",
        "type": "receipt",
        "checksum": "8afbc35ceb912390b153a5ba752075fdb8c734799ed04b79c937d34c11959a87"
      }
    ],
    "verification": "25 clusters roll up to 8 families with sizes 302/87/71/61/44/38/36/36, summing to 675 -- matches SIMBAD/NED-unmatched row count exactly (see PHASE3_V2_BENCHMARK_SUMMARY.md).",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_taxonomy_v2_manifest.json",
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/PHASE3_V2_BENCHMARK_SUMMARY.md",
      "project-context/PHASE3_V2_LANDING_2026-09-03.md"
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
    "id": "p3-ledger8-known-object-recovery-benchmark",
    "title": "Ledger #8 known-object recovery benchmark (VizieR reference classes vs S>8 sample) [SAMPLE-V1, deferred]",
    "program": "anomaly-discovery",
    "paper": "anomaly-flagship",
    "kind": "validation",
    "inputs": [
      {
        "name": "flagship_sample_s8_enriched.parquet",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/flagship_sample_s8_enriched.parquet",
        "checksum": null,
        "license": null
      },
      {
        "name": "VizieR reference class cache (5 fetched classes)",
        "type": "external-dataset",
        "locator": "~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/ (outside repo per phase-3 intermediates convention)",
        "checksum": null,
        "license": null
      },
      {
        "name": "sealed_2026-08-05/locator_inventory.jsonl (DESI footprint)",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/locator_inventory.jsonl",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p1_highz_tracers/clean_rerun/benchmark_known_object_recovery.py",
        "entrypoint": "python3 benchmark_known_object_recovery.py --crossmatch --reference-manifest ~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/recovery_refs_2026-09-02/reference_manifest_local.json --catalogs-config /tmp/catalogs_config_v2.json --locator-inventory sealed_2026-08-05/locator_inventory.jsonl --out-dir results_2026-08-07/phase3/recovery_benchmark",
        "sha256": null
      }
    ],
    "environment": {
      "python": "astropy, astroquery, numpy, pandas, pyarrow",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "houstongolden-mac",
      "date": "2026-09-03",
      "wall_clock": "<5min",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local-cpu",
      "est_wall_clock": "<5min (given cached VizieR reference classes)",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "This session fixed a real bug: 4/5 fetched VizieR classes returned sexagesimal RA/Dec strings the script could not parse; patched to convert via astropy SkyCoord(unit=(hourangle, deg)) before the existing crossmatch_positional() call."
    },
    "outputs": [
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark/recovery_benchmark.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark/recovery_benchmark.md",
        "type": "document",
        "checksum": null
      },
      {
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark/PHASE3_BENCHMARK_SUMMARY.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "0/0/0/0/0 matches across 5 fetched reference classes (BAL quasars, Roma-BZCAT, CV/WD binaries, LAEs, SLSN hosts) at 1.5 arcsec radius; footprint-restricted reference counts 27-5285 per class.",
    "status": "runnable-now",
    "provenance": [
      "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/recovery_benchmark/PHASE3_BENCHMARK_SUMMARY.md",
      "project-context/NEXT_SCIENCE_LEDGER.md#8"
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
        "entrypoint": "BIGBOUNCE_WORKSPACE=/path/to/writable/dir python3 emcee_freespec.py",
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
      "notes": "CONTENT CORRECTION vs the inventory bullet: the inventory's cited headline numbers (gamma=3.20+/-0.42, 192,000 samples = 32 walkers x 6,000 steps, DeltaBIC=7.0 from savage_dickey_2026-05-29.json) do NOT match the actual committed artifacts in this directory. The committed results.json for this exact script (emcee_freespec.py, real 30-bin Zenodo KDE likelihood) reports gamma mean=2.5665 +/- 0.3818 (median 2.5913), n_samples=320,000 (32 walkers x 10,000 production steps, plus 2,500 burn-in per the script docstring), and the committed savage_dickey_2026-05-29.json reports Savage-Dickey Bayes factors (B_matter_bounce_vs_free=3.228, log10_B_matter_bounce_vs_smbhb=3.854), not a Delta-BIC figure. The gamma=3.20+/-0.42 / DeltaBIC=7.0 figures instead belong to a DIFFERENT script, projects/nanograv/nanograv_improved_analysis.py (32 walkers x 6,000 steps, 134k post-burn samples, reconstructed from the published Agazie+2023 best-fit rather than the real Zenodo KDE likelihood — see project-context/SSOT/paper-3/status.md's Wave-14-RR note), which is outside this manifest's 17-id scope. Venue is genuinely ungated: no RunPod pod ID, GPU/CPU class, $/hr, or wall-clock is recorded anywhere in pipelines/p3_pta_mcmc/ (Top-5-gaps #2); the 24.97s committed production_seconds strongly suggests local CPU execution, but that inference is not itself logged evidence. 2026-09-04 hygiene closure: emcee_freespec.py hardcoded ROOT/OUT_DIR under /workspace (pod-only, read-only filesystem elsewhere); the script now reads BIGBOUNCE_WORKSPACE (default /workspace, unchanged numerics/paths) so it can write to any local directory off-pod — set it to a writable path to reproduce outside RunPod."
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
        "locator": "https://huggingface.co/bamfai/galaxy-chirality-v2",
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
    "id": "p4p-row16i-full-parent-dipole",
    "title": "Row 16(i) — full-parent (8,474,531-galaxy) real-space chirality dipole using the exact P4' primary estimator",
    "program": "galaxy-chirality",
    "paper": "P4P",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Full DESI Legacy DR8 chirality catalog (class_eq, production equivariant Z2-TTA classifier; already-committed, not re-run)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet",
        "checksum": "sha256:139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
      },
      {
        "name": "row16(ii) N=20,000 injection-calibrated postprocess residual bias",
        "type": "internal-artifact",
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/scale20k_injection_results.json",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p4prime_chirality_test/full_parent/full_parent_estimator_lib.py",
        "entrypoint": "imports build_projector() verbatim from pipelines/p2_chirality/generate_p4_primary_label_shuffle_strict_v1_0_257.py",
        "sha256": "269add74ab903fb740793655a19684b4464a1c2d6ca07653a2f6a39aa70ccc26"
      },
      {
        "path": "pipelines/p4prime_chirality_test/full_parent/run_full_parent_dipole.py",
        "entrypoint": "python3 pipelines/p4prime_chirality_test/full_parent/run_full_parent_dipole.py",
        "sha256": "7345c344b16f556d9aa2289ee9401da8ab21dd75998ff3bb7a07677308cbcebd"
      }
    ],
    "environment": {
      "python": "python3 + numpy + healpy + pyarrow",
      "hardware": "cpu-only; Apple M-series, macOS arm64 (no GPU/pod needed — classifier inference already existed for all 8,474,531 rows)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation",
      "date": "2026-09-04",
      "wall_clock": "48.1 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~1 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Reuses the already-committed full-catalog class_eq labels; loads one parquet, bins into NSIDE=64 HEALPix pixels, fits a dipole with healpy.fit_dipole via the imported P4' projector, draws a fresh 10,000-sample fixed-occupancy null (seed 20260904), and runs a 14-point x 2000-axis injection-recovery sweep (seed 20260905) to invert A_95."
    },
    "outputs": [
      {
        "locator": "pipelines/p4prime_chirality_test/full_parent/row16i_full_parent_dipole.json",
        "type": "result-json",
        "checksum": "sha256:975b2cf824884aec5d75d11cd25257a6b93926579832e063c559879972e99d89"
      },
      {
        "locator": "pipelines/p4prime_chirality_test/full_parent/fig_row16i_full_parent_injection_recovery.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/full_parent/ROW16I_FULL_PARENT_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Estimator (healpy.fit_dipole on per-pixel (2*n_CW-total)/total, NSIDE=64, support>=10) and null convention (fixed-occupancy multivariate-hypergeometric label randomization) are imported verbatim from the committed P4' strict-primary generator, not re-derived. Selection differs only in dropping the primary_hc/raw_flip_qc_unsafe restriction (full parent: all class_eq in {CW,CCW}, N=3,200,420 in support vs. 887,472 in the strict-primary subset). No tuning: amplitude grid, seed choice, and axis count match the committed a95_observed_label_upper_limit_v1_0_265.py convention.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 16(i)",
      "project-context/SSOT/paper-4p/status.md (887,472-subset A_95_obs=0.98%% comparison baseline)",
      "pipelines/p4prime_chirality_test/full_parent/ROW16I_FULL_PARENT_2026-09-04.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4p-row16ib-axis-shift",
    "title": "Row 16(i-b) — is the full-parent chirality dipole a QC/footprint systematic? Graded QC sweep, per-imaging-leg table, monopole/mask-leakage null",
    "program": "galaxy-chirality",
    "paper": "P4P",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Full DESI Legacy DR8 chirality catalog (class_eq, production equivariant Z2-TTA classifier; already-committed, not re-run)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet",
        "checksum": "sha256:139b761fbeafb34306a0cec60967226c18dc84295285f8317ce3d3af3d28bdf3"
      },
      {
        "name": "row16(ii) N=20,000 injection-calibrated postprocess residual bias",
        "type": "internal-artifact",
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/scale20k_injection_results.json",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p4prime_chirality_test/full_parent/full_parent_estimator_lib.py",
        "entrypoint": "imports build_projector() verbatim from pipelines/p2_chirality/generate_p4_primary_label_shuffle_strict_v1_0_257.py",
        "sha256": "269add74ab903fb740793655a19684b4464a1c2d6ca07653a2f6a39aa70ccc26"
      },
      {
        "path": "pipelines/p4prime_chirality_test/full_parent/row16ib_qc_leg_sweep.py",
        "entrypoint": "python3 pipelines/p4prime_chirality_test/full_parent/row16ib_qc_leg_sweep.py",
        "sha256": "8adacafd3cde0663185ad89015116bb52a198cac6aaa703e17f766d3d6cb4a0f"
      },
      {
        "path": "pipelines/p4prime_chirality_test/full_parent/row16ib_figure.py",
        "entrypoint": "python3 pipelines/p4prime_chirality_test/full_parent/row16ib_figure.py",
        "sha256": "4807049e1311a1e35fcd4b123447c6f511929e840b39407425b61d4400e88e03"
      }
    ],
    "environment": {
      "python": "python3 + numpy + healpy + pyarrow",
      "hardware": "cpu-only; Apple M-series, macOS arm64 (no GPU/pod needed — classifier inference already existed for all 8,474,531 rows)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation",
      "date": "2026-09-04",
      "wall_clock": "95.3 s (measured)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~2 min",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Re-runs the frozen P4' projector estimator on four QC selections (full parent; !raw_flip_qc_unsafe only; primary_hc only; strict), on each imaging leg (Dec boundaries (-20,32) from p2_chirality/c12b_wls_conditioning.py) in only-leg and drop-leg form for the parent and strict sets, and on |b|>20/30 cuts; fixed-occupancy label-shuffle nulls (10,000 draws for C0/C3, 2,000 elsewhere, seed 20260906) plus a 1,000-realisation pure-monopole mask-leakage null."
    },
    "outputs": [
      {
        "locator": "pipelines/p4prime_chirality_test/full_parent/row16ib_axis_shift.json",
        "type": "result-json",
        "checksum": "sha256:01af9a4e37a8f93370760a6d71cfa2252327c10e2f6bb8b1b2b2150a4a93758b"
      },
      {
        "locator": "pipelines/p4prime_chirality_test/full_parent/fig_row16ib_axis_shift.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/full_parent/ROW16IB_AXIS_SHIFT_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Plan pre-registered and committed (a5fde20a) BEFORE any fit was run, including the decision rule. Estimator and null imported verbatim from the committed P4' strict-primary generator; leg boundaries taken from the committed c12b_wls_conditioning.py. Result: the parent dipole is removed by the primary_hc cut alone (z=+0.68) and by dropping the DES imaging leg alone (z=+0.48); C0-vs-C3 axis separation 107.5 deg; pure-monopole mask leakage 0.19%. Verdict SYSTEMATIC per the pre-registered rule. Depth/seeing/E(B-V)/brick-quality legs declared NOT RUN (columns absent from the immutable release).",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md item 16(i-b)",
      "pipelines/p4prime_chirality_test/full_parent/ROW16I_FULL_PARENT_2026-09-04.md",
      "pipelines/p4prime_chirality_test/full_parent/ROW16IB_AXIS_SHIFT_2026-09-04.md"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4prime-a95-neyman-cl-2026-09-02",
    "title": "P4' R2 closure (DP4P-22) — genuine 95% CL upper limit on the primary real-space chirality dipole amplitude via Neyman inversion of the injection-recovery null",
    "program": "galaxy-chirality",
    "paper": "P4P",
    "kind": "analysis",
    "inputs": [
      {
        "name": "Strict-primary catalog (887,472-galaxy / 23,633-pixel support)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet",
        "checksum": null
      },
      {
        "name": "Committed fixed-occupancy 10^4-draw detection null",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/outputs/canonical_provenance/p4_primary_hc_safe_label_shuffle_10k_v1_0_257.npy (SHA-256 3a03ca4b...)",
        "checksum": null
      },
      {
        "name": "Committed strict-primary generator (estimator/selection, imported verbatim)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/generate_p4_primary_label_shuffle_strict_v1_0_257.py",
        "checksum": null
      },
      {
        "name": "Committed detection-power A_95^obs script (injection model + estimator, imported verbatim)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/analysis/a95_observed_label_upper_limit_v1_0_265.py",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/bh_universe_dipole/a95_upper_limit_2026_09_02.py",
        "entrypoint": "python3 research/bh_universe_dipole/a95_upper_limit_2026_09_02.py",
        "sha256": "c553b5fcca3999c463601a226e7e453e98e03986d2d01a899bc4f39a1d66aeeb"
      }
    ],
    "environment": {
      "python": "python3 + numpy + healpy + pyarrow",
      "hardware": "cpu-only; Apple M-series, macOS arm64"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation",
      "date": "2026-09-02",
      "wall_clock": "77.7 s (measured, N_AXES=2000/amplitude x 8 amplitudes)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "~80 s",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Injection Monte Carlo with a fixed seed (20260902); reruns are deterministic given numpy's Generator PCG64 and the same numpy/healpy versions. No GPU or network access required; catalog + null array + generator are all committed to the repo."
    },
    "outputs": [
      {
        "locator": "research/bh_universe_dipole/a95_upper_limit_2026_09_02.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Headline reproduction gate (A_obs=0.00466520, z_mom=+0.63465, p=0.23768) checked against the committed null receipt before any injection is run (hard RuntimeError on mismatch). Estimator/injection model imported verbatim from the committed v1.0.265 script; only the target statistic (5th percentile of recovered_amp, inverted against the observed A_dip) and the amplitude grid differ from v1.0.265's P_det=95% coverage inversion.",
    "status": "runnable-now",
    "provenance": [
      "project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P4P-v4P.0.2-EXACTPDF-78936e36-R2/P4P_v4P.0.2_R2_truth_audit.md finding DP4P-22",
      "pipelines/p4prime_chirality_test/paper/main.tex Sec. 3 (statistical significance / CL statement)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "p4prime-bh-universe-dipole-exclusion",
    "title": "P4' (Track C1) — confront the DESI chirality catalog's coverage-calibrated observed-label 95% sensitivity floor with Poplawski's rotating-black-hole-universe spin-axis claim",
    "program": "galaxy-chirality",
    "paper": "P4P",
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
        "type": "external-literature",
        "locator": "arXiv:1104.2815 (Longo 2011); arXiv:1207.5464 (Shamir 2012); arXiv:2007.16116 (Shamir 2020); arXiv:2208.13866 (Shamir 2022); arXiv:2502.18781 (Shamir 2025)",
        "checksum": null
      },
      {
        "name": "Poplawski black-hole-universe mechanism and preferred-axis papers",
        "type": "external-literature",
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
    "status": "runnable-now",
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "Not evidenced beyond code presence in the inventory; all original_run fields stay null. Reproduction requires a valid HF_TOKEN with write access to bamfai/astra-desi-edr-mirror to complete the mirror step. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "project-context/SSOT/paper-5/status.md",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "reproducibility: runnable-now, gap = no venue/cost evidence — the code runs, just no compute-receipt exists for the original run. Lineage note: the earlier '187-DESI-attribute cosmic-web catalog' blocker (SSOT: 'Houston-mediated, confirmed not in repo') was later resolved via this DESIVAST VAC approach, superseding the earlier env_finder/ 'run our own cosmic-web finder' fallback plan. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "Added `08_analysis_cosmic_web.py` to code[] beyond the inventory's explicit list: verified via `ls pipelines/p5_desi_chirality/scripts/` that this script (within the same 05-09 numbered range referenced by the redshift/density/healpix/systematics bullet) is the cosmic-web analysis, not a HEALPix/systematics script, and its output directory `results/analysis_cosmic_web/` matches this experiment's scope rather than the 16a-16d split.",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — 06_analysis_density.py maps to this analysis.",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
      "notes": "Regenerated 2026-09-04: inputs (p4_chirality.parquet, desi_zall.fits) were already local (no re-download needed). 03_crossmatch.py output: 2,232,212 rows, 1,297,512,873 bytes, sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147. Backed up 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet."
    },
    "outputs": [
      {
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "type": "catalog",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
      },
      {
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi_summary.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet.provenance.json",
        "type": "receipt",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
      }
    ],
    "verification": "Re-run and confirm the matched catalog contains 2,232,212 rows (1.3GB parquet) via p5_matched_chirality_desi_summary.json's row count, exact integer match.",
    "status": "runnable-now",
    "provenance": [
      "project-context/EXPERIMENT_INVENTORY_2026-08-05.md §PROGRAM: chirality / P5 — P4xDESI DR1 crossmatch + matched catalog build bullet",
      "project-context/SSOT/paper-5/status.md",
      "Verified via `find` that the 1.3GB parquet itself is not present in the repo tree; only p5_matched_chirality_desi_summary.json and p5_matched_chirality_desi.parquet.provenance.json are — noted in reproduction.notes rather than fabricating a checksum for the missing parquet.",
      "2026-09-04 restoration run: see reproducibility/FULL_PASS_2026-09-04.md \"P5 parquet restored\" section for full detail."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "runnable-now (code present per inventory); part of the same r-conf family as p5-rconf-closures and shares the same venue-evidence gap — no RunPod pod ID, GPU class, cost, or runtime found in pipelines/p5_desi_chirality/ or in the reachable sections of paper-5/status.md, so all original_run fields stay null. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "project-context/SSOT/paper-5/status.md",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — note the inventory's own '05-09' numbering is not a clean 1:1 map: 07_analysis_healpix.py is the HEALPix script, while 08_analysis_cosmic_web.py (also in the 05-09 range) is NOT a HEALPix/systematics script but the cosmic-web analysis, and is instead attached to p5-cosmic-web-desivast-void.",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "reproducibility: runnable-now (code present per inventory), venue evidence missing. This is gap #3 in the inventory's Top-5-gaps list: the script name `24_r24conf_pod_session.py` implies RunPod use but no pod ID, GPU class, cost, or runtime was found in pipelines/p5_desi_chirality/ or in the reachable sections of paper-5/status.md — so all original_run fields stay null rather than being inferred from the filename alone. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "project-context/SSOT/paper-5/status.md",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — 05_analysis_redshift.py maps to this analysis.",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
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
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet (1,297,512,873 bytes, 2,232,212 rows) -- gitignored (pipelines/p5_desi_chirality/.gitignore:9), NOT present in this git checkout by design, but regenerated 2026-09-04 from the committed recipe (p5-desi-dr1-crossmatch-build) at git_sha fb93e904 and verified 3-way: HF https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/p5/2026-09-04/p5_matched_chirality_desi.parquet ; B2 s3://bigbounce/p5/2026-09-04/p5_matched_chirality_desi.parquet ; local ~/Desktop/CODE_YOU/bigbounce_datasets/p5/2026-09-04/p5_matched_chirality_desi.parquet. sha256=a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147.",
        "checksum": "a0fa4725841c4f6b81233a8dc7d323e1de755ed6cfa0dc878b6af24674adc147"
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
      "notes": "Local CPU, no RunPod reference found for this analysis family per the inventory's own grep. Depends on regenerating pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet via the p5-desi-dr1-crossmatch-build experiment first (not retrievable directly -- see inputs[] disclosure)."
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
      "Split from the inventory's single bundled 05-09 bullet into 4 separate manifests (redshift/density/healpix/systematics) per directive; script mapping verified via `ls pipelines/p5_desi_chirality/scripts/` — 09_systematics.py maps to this analysis.",
      "2026-09-04 hygiene closure: pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet input is not retrievable anywhere (not in git, not on this machine, not on any bamfai/* HF repo, no documented B2 path) -- see this manifest's inputs[] locator disclosure. Regenerate via the p5-desi-dr1-crossmatch-build experiment instead of expecting a direct download.",
      "2026-09-04 P5 parquet restoration: regenerated via p5-desi-dr1-crossmatch-build (scripts/02_fetch_desi_dr1.py + 03_crossmatch.py), verified row count/schema against the committed p5_matched_chirality_desi_summary.json, backed up 3-way (HF/B2/local), sha256 recorded above."
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "psu-gate-s7-cai-factor-2",
    "title": "PSU gate S7: equation-level location of the factor 2 between Cai et al. 2009 (0903.0631) Eq. (37) and Eqs. (38)-(41)/Fig. 5, and the Li et al. 2017 (1612.02036) c_s=1 correspondence",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "Cai, Xue, Brandenberger, Zhang 2009 arXiv e-print source (matterbounceng2.tex, fnl.eps)",
        "locator": "https://arxiv.org/e-print/0903.0631",
        "type": "external-literature",
        "checksum": null
      },
      {
        "name": "Li, Quintin, Wang, Cai 2017 arXiv e-print source (general_matter_bounce_cosmology.tex)",
        "locator": "https://arxiv.org/e-print/1612.02036",
        "type": "external-literature",
        "checksum": null
      },
      {
        "name": "PSU gates S6-S11 note, item S7",
        "locator": "research/theory_audit/psu_gates_S6_S11_2026_09_04.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab f_NL matter-contraction adjudication (claims under test)",
        "locator": "research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md",
        "type": "internal-artifact",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.py",
        "entrypoint": "python3 research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.py",
        "sha256": "e186602fd1e35e1a83a82af7c456ccd01f5020a06b4b8dd954d0acb9a40bc675"
      }
    ],
    "environment": {
      "python": "python3 with sympy 1.14.0",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-05",
      "wall_clock": "about 15 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 1 minute",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic sympy. Transcribes Cai Eqs. 14, 19-21, 23, 27-37 and Li Eqs. 3.17, 4.6, 4.9, 4.12, 4.14, 4.16, 4.19, 4.20, 4.22, 5.1-5.3 verbatim, evaluates the isoceles/equilateral/folded/squeezed configurations under five factor-2 hypotheses. Figure readings from fnl.eps (rendered with ghostscript) are by eye, +-0.05."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.json",
        "type": "result-json",
        "checksum": "sha256:e855ce3ce20fdcf28722fe76fbf2be93fc454b29fd3bdc7fe938f6be191d2a65"
      },
      {
        "locator": "research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required: cai_row_convention six-perm entries all true and DISTINCT entry false; rows_sum_equals_Eqs34_36 true; Eq37_distinct_minus_rows == '0'; Eq37_sixperm_minus_rows == '-99*(k1**3 + k2**3 + k3**3)/128'; Li419_cs1_minus_rows == '0'; hypotheses.HB_uniform_x2_on_A_T.reproduces_printed all true; HA/HC/HD each have at least one false.",
    "status": "runnable-now",
    "provenance": [
      "PSU gate S7 (psu_gates_S6_S11_2026_09_04.md, 'equation-level read of 0903.0631 / 1612.02036 pending')",
      "directive Q2 (reproducibility manifests); directive R2 (rounds stopped); no paper .tex edited by this lane"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "psu-gates-s1-s2-label-composition-criterion",
    "title": "PSU R1 science gates S1/S2 (+S3 math): label-resolved second-order composition (initial vs final worldline label), well-defined separate-universe criterion with the gradient term restored, change-of-variable statement",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "PSU v1S.0.1 R1 truth audit (items S1, S2, S3)",
        "locator": "project-context/peer-reviews/INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab threading map (2026-09-04), frozen map pieces incl. lab_init / wl_initextra",
        "locator": "research/theory_audit/threading_map_second_order_2026_09_04.json",
        "type": "internal-artifact",
        "checksum": "sha256:b961e8678c3e8eb27df881600982cf2ce0b97ece902e3873835a9d0ac4d91cf7"
      },
      {
        "name": "separate-universe failure criterion note (2026-09-04)",
        "locator": "research/theory_audit/separate_universe_failure_criterion_2026_09_04.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab monopole adjudication (2026-09-03), in-in general-eps kernel",
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.md",
        "type": "internal-artifact",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/psu_gates_S1_S2_2026_09_04.py",
        "entrypoint": "python3 research/theory_audit/psu_gates_S1_S2_2026_09_04.py",
        "sha256": "4f6410228fef112775d2c7a29701657f04da67e027b5d8b31d969a1360dd53e4"
      }
    ],
    "environment": {
      "python": "python3 with sympy (>=1.12; run on sympy 1.14.0)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-04",
      "wall_clock": "about 3 s",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 10 seconds",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic exact sympy on closed forms (no constraint re-solve). Self-validating asserts: f_map(final) = -(5 eps/4)(1-mu^2); f_map(initial) = 5 eps/(4(3-eps)) [(eps-2) - eps mu^2]; label term T = 5 eps/(4(3-eps))(1-3 mu^2) with zero monopole; f_inin/lam + f_map(initial) == -5 for all constant eps; final-label total = -15(eps-4)/(4(eps-3)) + 15 eps/(4(3-eps)) mu^2; I(dust) -> 3/2, I(attractor) = 0, I(USR) = sqrt(eps_s eps_f) - eps_f; dust gradient term G -> (k eta_f)^2/6; inversion recovers the in-in monopole -5(eps-3)(eps-6)/18."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/psu_gates_S1_S2_2026_09_04.json",
        "type": "result-json",
        "checksum": "sha256:f4164019c10766738527d93930255ccf1912c55a2ecf8bc2cbf06d908f39f329"
      },
      {
        "locator": "research/theory_audit/psu_gates_S1_S2_2026_09_04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required: S1.f_dN_initial_label.const == '-5' and .mu2 == '0'; S1.at_eps.dust_eps_3_2.f_dN_fin == {const '-25/4', mu2 '15/4'}; S1.T_monopole == '0'; S2.attractor.I == '0'; S2.dust.I_limit_xi_to_inf == '3/2'; S2.dust['G_leading_over_(k_eta_f)^2'] == '1/6'; S2.USR.I == 'sqrt(epsilon_f)*sqrt(epsilon_s) - epsilon_f'; S3_math.inversion_recovers_inin_monopole == '-5*(epsilon - 3)*(epsilon - 6)/18' up to sympy ordering.",
    "status": "runnable-now",
    "provenance": [
      "PSU R1 truth audit S1 (PSU-1, PSU-8): printed Eq. (3) composed the final-label map with the initial-label total",
      "PSU R1 truth audit S2 (PSU-9): <X>_zeta 0/0 on constant-mode rows; gradient term dropped",
      "PSU R1 truth audit S3 (PSU-10): failure vs change-of-variable, math level only; framing left to Houston (R3/R6)",
      "directive Q2 (reproducibility manifests); arxiv/paper_su_criterion/main.tex NOT edited by this lane"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "psu-gates-s6-s11-science-gates",
    "title": "PSU R2 science gates S6-S11: map-independence sentinel + Eq.(4) assertion, Cai factor-2 scope, exact numerical USR delta N(phi,pi) at finite eps_s, final-slice dependence, constant-piece long mode, Zenodo status",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "PSU v1S.0.2 R2 truth audit, section 5(ii) science items S6-S11",
        "locator": "project-context/peer-reviews/INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab threading map (2026-09-04), frozen map pieces",
        "locator": "research/theory_audit/threading_map_second_order_2026_09_04.json",
        "type": "internal-artifact",
        "checksum": "sha256:b961e8678c3e8eb27df881600982cf2ce0b97ece902e3873835a9d0ac4d91cf7"
      },
      {
        "name": "PSU gates S1/S2 note (closed forms re-asserted here)",
        "locator": "research/theory_audit/psu_gates_S1_S2_2026_09_04.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab monopole adjudication (2026-09-03), in-in kernel and Cai/Li discussion",
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.md",
        "type": "internal-artifact",
        "checksum": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/psu_gates_S6_S11_2026_09_04.py",
        "entrypoint": "S6_SENTINEL_JSON=research/theory_audit/psu_gates_S6_sentinel_threading_2026_09_04.json python3 research/theory_audit/psu_gates_S6_S11_2026_09_04.py",
        "sha256": "207c4e118ad46244c7df7b9024ce4c34bfda39b5a99c8bef987b9d25f6c919ad"
      }
    ],
    "environment": {
      "python": "python3 with sympy 1.14.0 and mpmath 1.3.0",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-04",
      "wall_clock": "about 20 s (+ about 100 s for the sentinel re-run of the threading script)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 3 minutes",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Deterministic. S6: static ordering assert + sentinel re-run of threading_map_second_order_2026_09_04.py with the in-in coefficients perturbed (c0i+7, c2i+11): map_fNL_pieces byte-identical, prediction block changes; Eq.(4) asserted with the minus sign. S8: exact USR closed-form N(phi,pi), k->0 linear theory, 40-digit mpmath: delta N_SU/[zeta_f(1-I/3)] = 1 + 1e-12 at eps_s=1e-2, eps_f=1e-6 (both final slices). S9: zeta_rho = zeta_phi - zetadot/(3H); lambda_phi = 1-eps/3, lambda_rho = 2(3-eps)/(6-eps). S10: f_map(g,K_c) with g=1 reproducing the frozen initial-label map."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/psu_gates_S6_S11_2026_09_04.json",
        "type": "result-json",
        "checksum": "sha256:6642580c39cc7ef2c6d4cbbd1708f3e6270ad907b46f204cb234fedf0c15f6f3"
      },
      {
        "locator": "research/theory_audit/psu_gates_S6_sentinel_threading_2026_09_04.json",
        "type": "result-json",
        "checksum": "sha256:bd73587b9b9ccaae0a73ab3c7d14e12422627c4467d637e8b910ded2efc6717e"
      },
      {
        "locator": "research/theory_audit/psu_gates_S6_S11_2026_09_04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run with S6_SENTINEL_JSON pointing at the sentinel receipt and diff the JSON. Required: S6.verdict == 'RESOLVED', S6.Eq4_residual_minus_sign == '0'; S8.cases['es=0.01,ef=1e-06,C1=0,C2=1'].ratio_dN_SU_over_predB within 1e-10 of 1 and ratio_dN_SU_over_zeta_f == 0.99996663...; S9.rows.dust_eps_3_2 == {zeta_rho/zeta_phi '3/2', lambda_phi '1/2', lambda_rho '2/3'}; S10.f_map_g_to_0_known_part == '5*epsilon/9'.",
    "status": "runnable-now",
    "provenance": [
      "PSU R2 truth audit section 5(ii) science items S6-S11 (2026-09-04)",
      "S6 sentinel: scratch copy of threading_map_second_order_2026_09_04.py with in-in coefficients perturbed; receipt committed",
      "directive Q2 (reproducibility manifests); directive R2 (rounds stopped); arxiv/paper_su_criterion/main.tex NOT edited by this lane"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "row11c-threading-map-second-order",
    "title": "Row 11(c): second-order threading map from Maldacena's comoving zeta to the zero-shift (fluid-congruence) delta N_c in a non-attractor contraction; mechanism behind the delta N = -5 vs in-in -15/8 monopole gap",
    "program": "bounce-theory",
    "paper": "P2",
    "kind": "derivation",
    "inputs": [
      {
        "name": "lab monopole adjudication (2026-09-03)",
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.md",
        "type": "internal-artifact",
        "checksum": null
      },
      {
        "name": "lab monopole adjudication script (conventions)",
        "locator": "research/theory_audit/fnl_monopole_adjudication_2026_09_03.py",
        "type": "internal-artifact",
        "checksum": "sha256:058447db00cb61978e05dd0503983ebbe29a558abfd94ad5270fd87e5c3880aa"
      },
      {
        "name": "Maldacena 2003",
        "locator": "https://arxiv.org/abs/astro-ph/0210603",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Namjoo, Firouzjahi & Sasaki 2012",
        "locator": "https://arxiv.org/abs/1210.3692",
        "type": "external-literature",
        "checksum": null,
        "license": null
      },
      {
        "name": "Lyth, Malik & Sasaki 2005",
        "locator": "https://arxiv.org/abs/astro-ph/0411220",
        "type": "external-literature",
        "checksum": null,
        "license": null
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "research/theory_audit/threading_map_second_order_2026_09_04.py",
        "entrypoint": "python3 research/theory_audit/threading_map_second_order_2026_09_04.py",
        "sha256": "b0c934158add4ddedb40f042a26e2f430b77849f301e86b93f0f76f3637c7fbf"
      }
    ],
    "environment": {
      "python": "python3 with sympy (>=1.12; run on sympy 1.14.0)",
      "hardware": "cpu-only"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local macOS workstation",
      "date": "2026-09-04",
      "wall_clock": "~3 min (second-order constraint solve ~105 s; rest ~50 s)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local",
      "est_wall_clock": "under 5 minutes",
      "est_cost_usd": 0,
      "parallelizable": false,
      "resume_support": false,
      "notes": "Fully deterministic exact sympy. No network access. Self-validating: background + first-order ADM constraints satisfied identically by alpha = zetadot/H, psi = -zeta/H + chi (all k); second-order lapse/shift solved from the exact constraints; 1/k_L poles asserted to cancel in the bispectrum; linear threading factor 1 - eps/3 recovered from the exact identity; monopole -5 for both labels and isotropy for the initial-position label asserted for general constant eps; adjudication general-eps in-in monopole reproduced by inversion; eps -> 0 kills every cross kernel; attractor (m = 0) map is the identity. Optional env THREADING_CACHE=<file> caches the slow constraint solve between dev runs (not used for the committed result)."
    },
    "outputs": [
      {
        "locator": "research/theory_audit/threading_map_second_order_2026_09_04.json",
        "type": "result-json",
        "checksum": "sha256:b961e8678c3e8eb27df881600982cf2ce0b97ece902e3873835a9d0ac4d91cf7"
      },
      {
        "locator": "research/theory_audit/threading_map_second_order_2026_09_04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run and diff the JSON. Required exact values: linear_threading_factor == '3 - epsilon' up to the factor 1/3 (printed '-(epsilon - 3)/3'); kernels_growing_mode.zlap == '2*epsilon/3'; map_fNL_pieces.total_final_label == {const '-5*epsilon/4', mu2 '5*epsilon/4', monopole '-5*epsilon/6'}; prediction.initial_label == {const '-5', mu2 '0', monopole '-5'}; prediction.final_label.const_eps_3_2 == '-25/4', mu2_eps_3_2 == '15/4'; map_fNL_pieces.pure_translation_init.monopole == '0'; five_eps_over_4_matches_a_map_term == []; gap_decomposition_inin_minus_dNc.sum == '5*epsilon*(9 - epsilon)/18'; attractor_limit.div_cross == '0'.",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 11(c): 'derive the second-order threading map (Fable-tier)'; acceptance 'mechanism derived or stated as an identity'",
      "research/theory_audit/fnl_monopole_adjudication_2026_09_03.md VERDICT and §4: the '(5/12)(3 eps)' identity recorded as 'a computed identity, not a claimed mechanism'",
      "directive R (vision governance) and directive Q2 (reproducibility manifests)",
      "input 'lab monopole adjudication (2026-09-03)' used for: the open item; the comparison values f(mu,eps) = (5/12)(eps^2 mu^2 - eps^2 + 6 eps - 12), monopole -5(eps-3)(eps-6)/18, delta N_c = -5, and the [L]/[X] class values — used only AFTER the map kernels were computed and printed",
      "input 'Maldacena 2003' used for: comoving-gauge ADM variables and the first-order constraint solution (re-verified here, not transcribed)",
      "input 'Namjoo, Firouzjahi & Sasaki 2012' used for: the USR benchmark statement (structural limit only; 5/2 not re-derived here)",
      "input 'Lyth, Malik & Sasaki 2005' used for: the gradient-expansion delta N = zeta argument whose shift assumption fails at O(1/k_L)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "row13-image-level-injection-pilot",
    "title": "Row 13 PILOT — image-level end-to-end parity-injection test for the galaxy-spin classifier vs the existing label-level injection-recovery curve\ndescription: Status detail: pilot complete, inconclusive (raw single-pass model, N=500); real follow-up at scale through the equivariant pipeline queued (row 13).",
    "program": "galaxy-chirality",
    "paper": "P4P",
    "kind": "analysis",
    "inputs": [
      {
        "name": "bamfai/galaxy-chirality-catalog (catalog_production.parquet)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
        "checksum": null
      },
      {
        "name": "bamfai/galaxy-chirality-v2 checkpoint",
        "type": "model",
        "locator": "chirality_model_v2_best.pt, revision 237d021c451d75cf86a875e86d4de498b74e2f12",
        "checksum": null
      },
      {
        "name": "Legacy Survey DR9 JPEG cutouts (500 real galaxies)",
        "type": "external-dataset",
        "locator": "https://www.legacysurvey.org/viewer/jpeg-cutout?ra=..&dec=..&size=150&layer=ls-dr9",
        "checksum": null
      }
    ],
    "apis": [
      {
        "name": "huggingface_hub.hf_hub_download",
        "endpoint": "https://huggingface.co",
        "auth_required": true
      },
      {
        "name": "legacysurvey.org jpeg-cutout service",
        "endpoint": "https://www.legacysurvey.org/viewer/jpeg-cutout",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/fetch_pilot_sample.py",
        "entrypoint": "python3 fetch_pilot_sample.py",
        "sha256": "2cca334ac0f8ebb583a519bf67ef051aff8dc154aa8d283f986b4d17ed063add"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/run_injection_pilot.py",
        "entrypoint": "python3 run_injection_pilot.py",
        "sha256": "a4cb29e0835fce233fd3b9c8cb981916e1cb13c0e71b01c7b995dd043590b670"
      }
    ],
    "environment": {
      "python": "python3 + torch 2.13.0 + timm 1.0.28 + PIL + healpy + pandas + huggingface_hub",
      "hardware": "cpu-only; Apple M-series, macOS arm64 (RunPod authorized but not used — local run completed in ~6.5 min wall-clock)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "local workstation",
      "date": "2026-09-04",
      "wall_clock": "~6.5 min (500 cutout downloads + 2500 raw single-pass classifier forward passes on CPU)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local for N<=1000; RunPod GPU for N in thousands-tens-of-thousands",
      "est_wall_clock": "~6.5 min for this N=500 reduced pilot; hours for the declared 10k spec on CPU, tens of minutes on GPU",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Cutout downloads are network-bound and can be parallelized; classifier forward passes are the compute-bound step. Re-running with SEED=42 reproduces the same sky-uniform sample and flip-set draws given unchanged catalog snapshot."
    },
    "outputs": [
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/pilot_sample_manifest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/injection_pilot_results.json",
        "type": "result-json",
        "checksum": null
      }
    ],
    "verification": "Manual inspection of injection_pilot_results.json: 500/500 cutouts downloaded successfully, class order (CW=0/CCW=1/NOT_SPIRAL=2) confirmed against run_v2_inference.py/run_eq_dataloader.py/equivariant_postprocess.py before use. Result found INCONCLUSIVE and disclosed as such: (1) this pilot ran the raw single-pass classifier, not the production equivariant D4-averaged pipeline the paper's headline numbers use, so the f=0 baseline (A=-0.396) is far from the paper's post-equivariant residual bias (-0.0026); (2) N=500 with 2-25 flipped images per fraction is underpowered to resolve sub-percent-to-few-percent injected signals against per-image classification noise — ??A does not track f_injected monotonically. No claim of a recovered dipole or a validated comparison to the label-level curve is made; the gap (need equivariant-pass + N in thousands+) is the actionable finding.",
    "status": "runnable-now",
    "provenance": [
      "Task: ledger row 13 PILOT (2026-09-04)",
      "pipelines/p2_chirality/scripts/full_catalog_injection_recovery.py (label-level baseline being compared against)",
      "pipelines/p2_chirality/equivariant_postprocess.py (production pipeline this pilot did NOT replicate — flagged as the needed next step)",
      "project-context/SSOT/paper-4p/status.md (A_95^obs≈0.98% context)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "row13-image-level-injection-scale",
    "title": "Row 13 Part A AT SCALE — pixel-level parity-injection test through the PRODUCTION equivariant (Z2 2-fold flip-TTA) pipeline, N=5000, vs the exact label-level analytic identity",
    "program": "galaxy-chirality",
    "paper": "P4P",
    "kind": "analysis",
    "inputs": [
      {
        "name": "bamfai/galaxy-chirality-catalog (catalog_production.parquet)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
        "checksum": null
      },
      {
        "name": "bamfai/galaxy-chirality-v2 checkpoint",
        "type": "model",
        "locator": "chirality_model_v2_best.pt, revision 237d021c451d75cf86a875e86d4de498b74e2f12",
        "checksum": null
      },
      {
        "name": "Legacy Survey DR9 JPEG cutouts (5000 real galaxies, 2500 CW / 2500 CCW by catalog label)",
        "type": "external-dataset",
        "locator": "https://www.legacysurvey.org/viewer/jpeg-cutout?ra=..&dec=..&size=150&layer=ls-dr9",
        "checksum": null
      }
    ],
    "apis": [
      {
        "name": "huggingface_hub.hf_hub_download",
        "endpoint": "https://huggingface.co",
        "auth_required": true
      },
      {
        "name": "legacysurvey.org jpeg-cutout service",
        "endpoint": "https://www.legacysurvey.org/viewer/jpeg-cutout",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/fetch_scale_sample.py",
        "entrypoint": "python3 fetch_scale_sample.py",
        "sha256": "8d5978f34835eaefb3948fe79765d7611cf7371257f249a22a1b13e18f1b8687"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/run_injection_scale.py",
        "entrypoint": "python3 run_injection_scale.py",
        "sha256": "4300ee1d9c78dde028b43f1bef8033e3e5899c909c57332c16bd7cd3b7dd21c1"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/analyze_injection_scale.py",
        "entrypoint": "python3 analyze_injection_scale.py",
        "sha256": "85b7098d624ce3d82b4dedd6c4bab2bb9a7d84b5ca94f09ae13b86c635876e87"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/gen_fig_scale_injection.py",
        "entrypoint": "python3 gen_fig_scale_injection.py",
        "sha256": "18fd4bd378edd45b34f79b5f8817119ae6215b75e13cc280aee4770b2c464d57"
      }
    ],
    "environment": {
      "python": "python3 + torch 2.13.0 + timm + PIL + healpy + pandas + huggingface_hub + matplotlib",
      "hardware": "local Apple Silicon MPS (Metal), macOS arm64 — no RunPod needed; 200-cutout timing test projected ~50 min for N=5000 (under the 90-min RunPod threshold), actual run completed in 44.5 min"
    },
    "original_run": {
      "venue": "local",
      "gpu": "Apple M-series MPS",
      "pod_id_or_host": "local workstation",
      "date": "2026-09-04",
      "wall_clock": "44.5 min (5000 cutout downloads + 10,000 classifier forward passes [orig+flip per galaxy] on MPS)",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local MPS/GPU for N up to ~10k; RunPod only needed beyond that or on CPU-only hosts",
      "est_wall_clock": "~45 min for N=5000 on Apple Silicon MPS; ~2x that on CPU-only per the N=200 CPU-vs-MPS pilot timing",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "run_injection_scale.py checkpoints every 500 galaxies and resumes from scale_pairs.parquet. Computational optimization: because the production Z2-TTA construction is EXACTLY antisymmetric under a single-image mirror flip (eq_cw(flip(img))=eq_ccw(img), proven identity, verified analytically in the script docstring), only ONE (orig, flip) forward-pass pair per galaxy is needed regardless of the f/seed injection grid — all 5 fractions x 5 seeds are evaluated in closed form by analyze_injection_scale.py from the single N=5000 inference pass, with NO re-inference. This is what makes the at-scale test tractable without a GPU pod."
    },
    "outputs": [
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/scale_sample_manifest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/scale_injection_results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/fig_scale_injection_recovery.png",
        "type": "figure",
        "checksum": null
      }
    ],
    "verification": "5000/5000 cutouts downloaded and classified successfully (0 failures). Baseline spiral-classified asymmetry A0=+0.95% (vs. paper's published post-equivariant residual of -0.26%): opposite sign, same order of magnitude (both sub-1%, both consistent with null within ~1 sigma at this N given per-image classification noise), a dramatic improvement over the N=500 raw single-pass pilot's -39.6% baseline. Injected-fraction slope dA/df (pixel-level, spiral-classified) = -0.116 vs the exact closed-form label-level analytic identity slope of -0.019 (same sign, same order of magnitude, ratio ~6x) -- both slopes are SMALLER than the per-seed sampling noise floor (std across 5 seeds ~0.003-0.005) at f in {0.5%,1%,2%,5%}, so this N=5000 test cannot yet distinguish whether the label-level curve is conservative or optimistic relative to the true pixel-level recovery; it DOES show the production pipeline's pixel-level and label-level responses are consistent in sign and order of magnitude, unlike the raw single-pass pilot which was inconsistent and non-monotonic. Larger N (paper's own ansatz suggests tens of thousands) is needed to resolve the slope ratio outside the noise floor.",
    "status": "runnable-now",
    "provenance": [
      "Task: ledger row 13 Part A at scale (resumed 2026-09-04 from ROW13_PILOT_2026-09-04.md)",
      "Supersedes row13-image-level-injection-pilot.json (N=500 raw single-pass pilot, inconclusive)",
      "pipelines/p2_chirality/scripts/full_catalog_injection_recovery.py (paper's committed sky-map amplitude-vs-detection-probability curve; a DIFFERENT statistic/axis, not directly comparable — disclosed in analyze_injection_scale.py's note_on_comparison_scope)",
      "pipelines/p2_chirality/equivariant_postprocess.py (production Z2 2-fold flip-TTA pipeline replicated exactly here)",
      "pipelines/p4prime_chirality_test/injection_pilot/ROW13_PILOT_2026-09-04.md (prior N=500 pilot this run follows up on)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "row16-image-level-injection-n20k",
    "title": "Row 16 Part A at N=20,000 — pixel-level parity-injection through the PRODUCTION equivariant (Z2 2-fold flip-TTA) pipeline vs the exact label-level mixture identity, resolving the slope comparison outside the noise floor",
    "program": "galaxy-chirality",
    "paper": "P4P",
    "kind": "analysis",
    "inputs": [
      {
        "name": "bamfai/galaxy-chirality-catalog (catalog_production.parquet)",
        "type": "external-dataset",
        "locator": "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
        "checksum": null
      },
      {
        "name": "bamfai/galaxy-chirality-v2 checkpoint",
        "type": "model",
        "locator": "chirality_model_v2_best.pt, revision 237d021c451d75cf86a875e86d4de498b74e2f12",
        "checksum": null
      },
      {
        "name": "Legacy Survey DR9 JPEG cutouts (20,000 real galaxies, catalog-labeled CW/CCW)",
        "type": "external-dataset",
        "locator": "https://www.legacysurvey.org/viewer/jpeg-cutout?ra=..&dec=..&size=150&layer=ls-dr9",
        "checksum": null
      }
    ],
    "apis": [
      {
        "name": "huggingface_hub.hf_hub_download",
        "endpoint": "https://huggingface.co",
        "auth_required": true
      },
      {
        "name": "legacysurvey.org jpeg-cutout service",
        "endpoint": "https://www.legacysurvey.org/viewer/jpeg-cutout",
        "auth_required": false
      }
    ],
    "code": [
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/fetch_scale20k_sample.py",
        "entrypoint": "python3 fetch_scale20k_sample.py",
        "sha256": "473329a5ddca4ebe94a6b2a389ec78e62e06e4c9c33f46c942e0119c49a59770"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/run_injection_scale20k.py",
        "entrypoint": "python3 run_injection_scale20k.py",
        "sha256": "956eefab8880317484b53a97f080a9de8661b897eb92803371473b41a2bc1608"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/analyze_injection_scale20k.py",
        "entrypoint": "python3 analyze_injection_scale20k.py",
        "sha256": "d87aa0f912103c931153786676d5bb3707d07f693ed0034a9fad2e2708247d77"
      },
      {
        "path": "pipelines/p4prime_chirality_test/injection_pilot/gen_fig_scale20k_injection.py",
        "entrypoint": "python3 gen_fig_scale20k_injection.py",
        "sha256": "b36b719f7892f139ef67f264c17a5046cf48a9a9efdcaa14499deb8aa26bbf26"
      }
    ],
    "environment": {
      "python": "python3 + torch 2.13.0 + timm + PIL + healpy + pandas + huggingface_hub + matplotlib",
      "hardware": "local Apple Silicon MPS (Metal), macOS arm64 — no RunPod needed at N=20k"
    },
    "original_run": {
      "venue": "local",
      "gpu": "Apple M-series MPS",
      "pod_id_or_host": "local workstation",
      "date": "2026-09-04",
      "wall_clock": "first attempt: 106.7 min to 10,640/20,000 pairs (9,360 failed on transient cutout-fetch errors); resumed attempt: 109.7 min completing the remaining 9,360 pairs, ending 20,000/20,000 succeeded, 0 failed on the resumed pass",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local MPS/GPU for N up to ~20k; RunPod only needed for a full-parent-catalog dipole run",
      "est_wall_clock": "~110-215 min for N=20,000 on Apple Silicon MPS depending on cutout-fetch retry rate",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": true,
      "notes": "run_injection_scale20k.py checkpoints to scale20k_pairs.parquet and resumes from the last saved offset; the first attempt's 9,360 fetch failures were fully recovered by resuming, with 0 failures on the retry. As at N=5000, the Z2-TTA construction's proven single-mirror-flip antisymmetry means one (orig, flip) forward-pass pair per galaxy covers all 5 fractions x 10 seeds in closed form via analyze_injection_scale20k.py, with no re-inference."
    },
    "outputs": [
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/scale20k_sample_manifest.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/scale20k_injection_results.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/injection_pilot/fig_scale20k_injection_recovery.png",
        "type": "figure",
        "checksum": null
      }
    ],
    "verification": "20,000/20,000 cutouts downloaded and classified successfully across the two attempts (9,360 fetch failures on the first pass, 0 on the resumed retry that completed them). Baseline pixel-level asymmetry A0=-21.72% (paper's published post-equivariant residual: -0.26%; opposite order of magnitude — the two A0 values are DIFFERENT statistics: this A0 is measured over the full injection sample including NOT_SPIRAL mass, while the spiral-classified-only baseline is A0=+0.59%, same order as the paper's -0.26%, opposite sign). Fitted pixel-level slope dA/df (OLS over the 5 fraction means) = +0.0167 +/- 0.0089 (SE from OLS residuals about the 5-point fraction-mean fit). The naive label-level identity A=A0(1-2f) gives slope -2*A0=+0.4343, ~47 sigma from the measured pixel-level slope using the OLS SE (or ~35 sigma using seed-spread-weighted SE) — the measured pixel-level response is far more conservative in magnitude than the naive identity predicts, now resolved well outside the noise floor. The rigorous mixture identity that additionally accounts for the NOT_SPIRAL probability mass (E[A(f)]=(1-f)*A0+f*A0_ccw, disclosed in scale20k_injection_results.json's note_on_comparison_scope) gives slope -0.00934, sign-flipped from the measured +0.0167 and ~2.9-3.0 sigma away — marginally outside the noise floor for the first time at this N, but the two are close in order of magnitude once NOT_SPIRAL mass is properly modeled. N=20k therefore resolves what N=5000 could not: the slope comparison is no longer noise-limited, and the production pipeline's pixel-level response is CONSERVATIVE relative to the naive label-level identity by more than an order of magnitude, while remaining consistent in scale (though not sign) with the NOT_SPIRAL-corrected mixture identity.",
    "status": "runnable-now",
    "provenance": [
      "Task: ledger row 16 Part A at N=20,000 (2026-09-04, follow-on to row 13's N=5000 pilot)",
      "Builds on row13-image-level-injection-scale.json (N=5000, slope comparison inconclusive within the noise floor)",
      "pipelines/p2_chirality/scripts/full_catalog_injection_recovery.py (paper's committed sky-map amplitude-vs-detection-probability curve; a DIFFERENT statistic/axis, not directly comparable — disclosed in analyze_injection_scale20k.py's note_on_comparison_scope)",
      "pipelines/p2_chirality/equivariant_postprocess.py (production Z2 2-fold flip-TTA pipeline replicated exactly here)",
      "pipelines/p4prime_chirality_test/injection_pilot/ROW13_PILOT_2026-09-04.md (Part A at N=20k appended in this run)"
    ]
  },
  {
    "manifest_version": "bigbounce-experiment/v1",
    "id": "row16iv-chirality-structure",
    "title": "Row 16 (iv) — chirality x structure: parity vs environment, anomaly positions, redshift, and preferred axes",
    "program": "galaxy-chirality",
    "paper": "P4",
    "kind": "validation",
    "inputs": [
      {
        "name": "P4 chirality catalog (primary-safe, DESI Legacy DR8 ViT+TTA, 8,474,531 rows)",
        "type": "internal-artifact",
        "locator": "pipelines/p2_chirality/apjs_release_v1.0.244/p4_catalog_primary_safe_v1.0.244.parquet",
        "checksum": null
      },
      {
        "name": "Anomaly catalog v2 science targets (1,244 rows)",
        "type": "internal-artifact",
        "locator": "pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/flagship_sample_v2_enriched.parquet",
        "checksum": null
      },
      {
        "name": "DESI spec-z x chirality crossmatch (P5)",
        "type": "internal-artifact",
        "locator": "pipelines/p5_desi_chirality/results/p5_matched_chirality_desi.parquet",
        "checksum": null
      },
      {
        "name": "DESI DR1 LSS public products (QSO clustering + randoms, z=0.8-2.1) - INSPECTED, NOT USED: no LRG/BGS/void product on disk and no redshift overlap with the z<0.3 spirals",
        "type": "external-dataset",
        "locator": "https://data.desi.lbl.gov/public/dr1/",
        "checksum": null,
        "license": "DESI DR1 public data, CC-BY-4.0"
      }
    ],
    "apis": [],
    "code": [
      {
        "path": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_common.py",
        "entrypoint": "imported",
        "sha256": null
      },
      {
        "path": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_env_z.py",
        "entrypoint": "python3 chirality_structure_env_z.py",
        "sha256": null
      },
      {
        "path": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_anomaly.py",
        "entrypoint": "python3 chirality_structure_anomaly.py",
        "sha256": null
      },
      {
        "path": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_axes.py",
        "entrypoint": "python3 chirality_structure_axes.py",
        "sha256": null
      },
      {
        "path": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_figures.py",
        "entrypoint": "python3 chirality_structure_figures.py",
        "sha256": null
      }
    ],
    "environment": {
      "python": "numpy, scipy, pyarrow, scikit-learn, healpy, matplotlib",
      "hardware": "local laptop CPU (no GPU, no cloud)"
    },
    "original_run": {
      "venue": "local",
      "gpu": null,
      "pod_id_or_host": "Houston laptop (darwin)",
      "date": "2026-09-04",
      "wall_clock": "~50 min total across the three analysis scripts",
      "actual_cost_usd": 0
    },
    "reproduction": {
      "recommended_venue": "local CPU",
      "est_wall_clock": "~1 hour",
      "est_cost_usd": 0,
      "parallelizable": true,
      "resume_support": false,
      "notes": "Pre-registration (statistics, nulls, selection handling, 3-sigma-after-look-elsewhere threshold) was committed BEFORE any statistic was computed: commit 8e429040. Seeds are fixed in the scripts (16041-16045), so all reported numbers are byte-reproducible on a local CPU."
    },
    "outputs": [
      {
        "locator": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_env_z.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_anomaly.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_axes.json",
        "type": "result-json",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/chirality_structure/chirality_structure_summary.png",
        "type": "figure",
        "checksum": null
      },
      {
        "locator": "pipelines/p4prime_chirality_test/chirality_structure/ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md",
        "type": "document",
        "checksum": null
      }
    ],
    "verification": "Re-run the three analysis scripts and confirm every reported observed statistic, null mean/std, z and empirical p match the committed JSON exactly (fixed seeds).",
    "status": "runnable-now",
    "provenance": [
      "project-context/NEXT_SCIENCE_LEDGER.md row 16, item (iv)",
      "pipelines/p4prime_chirality_test/chirality_structure/ROW16IV_CHIRALITY_STRUCTURE_2026-09-04.md (pre-registration committed at 8e429040)"
    ]
  }
];
