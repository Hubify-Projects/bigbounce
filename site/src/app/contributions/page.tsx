import type { Metadata } from "next";
import Link from "next/link";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export const metadata: Metadata = {
  title: "Contributions",
  description:
    "Every novel contribution from the BigBounce research program ranked on the canonical N1–N4 novelty scale. Self-claim ceiling is N3 (first-of-kind). N4 (paradigm-shifting / Nobel-worthy) is reserved for outside arbiters and never self-claimed.",
};

type Tier = "N4" | "N3" | "N2" | "N1";

interface Contribution {
  id: string;
  tier: Tier;
  title: string;
  paper: string;
  oneLine: string;
  why?: string;
  what?: string;
  equation?: string;
  prior?: string;
  ours?: string;
  verify?: { label: string; href: string }[];
}

const TIER_LABEL: Record<Tier, string> = {
  N4: "PARADIGM-SHIFTING (RESERVED)",
  N3: "FIRST-OF-KIND DEMONSTRATION",
  N2: "NOVEL COMBINATION / EXTENSION",
  N1: "INCREMENTAL REFINEMENT / REPLICATION",
};

const TIER_DEF: Record<Tier, string> = {
  N4: "Paradigm-shifting / consensus-breaking / Nobel-worthy. Awarded by the field over time — never self-claimed by the authors.",
  N3: "First-of-kind demonstration, new constraint, or new direction that meaningfully opens or closes a measurable testbed. Ceiling for our self-claims.",
  N2: "Novel application or combination of existing methods — applying a known technique to a regime it hasn't seen, or combining pipelines to broaden what's measurable.",
  N1: "Incremental refinement or replication — tightens an existing measurement, fixes a known bias, or reproduces a prior result with a new dataset.",
};

const TIER_COLOR: Record<Tier, string> = {
  N4: "var(--tier-n4)",
  N3: "var(--tier-n3)",
  N2: "var(--tier-n2)",
  N1: "var(--tier-n1)",
};

const contributions: Contribution[] = [
  {
    id: "perturbation-transparency",
    tier: "N2",
    title: "Minimal-ECH Branch Clarification",
    paper: "Paper 1A · focused boundary Note",
    oneLine:
      "A convention-audited account of what follows when the non-propagating connection is eliminated in the stated minimal Einstein--Cartan--Holst setup, including the spin-sourced contact term and the zero-spin scalar branch.",
    why: "It supplies a bounded theoretical baseline for the bounce program: which minimal branches are addressed here, and which cosmological mechanisms are outside the Note's scope.",
    what: "The Note consolidates standard identities, gives the contact-interaction coefficient and a scale benchmark, and separates spin-sourced from zero-spin scalar statements. It does not claim an all-orders observable theorem or a complete cosmological no-go result.",
    prior:
      "Hehl et al. (1976); Freidel, Minic & Takeuchi (2005); Calcagni & Mercuri (2009); Mercuri (2009); de Berredo-Peixoto et al. (2012); Långvik et al.",
    ours:
      "The contribution is careful convention and scope control for this narrow branch; novelty and broader significance are for independent review.",
    verify: [
      {
        label: "P1A source Note",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/arxiv/paper1a_ech_nogo.tex",
      },
    ],
  },
  {
    id: "14-barriers",
    tier: "N1",
    title: "Archived ECH Route Map",
    paper: "Legacy program archive · not current P1A",
    oneLine:
      "Earlier route-mapping material is retained as provenance, not presented as a current universal closure result or as the scope of P1A.",
    why: "It documents how the program narrowed; it is not a selected scientific claim.",
    what: "The historical map contains exploratory constraints and branch notes. It must not be read as closing every minimal-ECH route to dark energy or as a replacement for a model-specific analysis.",
    prior:
      "Blagojević & Hehl (2013); Weinberg (1989); 't Hooft (1979); Shie, Nester & Yo (2008).",
    ours:
      "Preserved for traceability only; no current novelty or closure claim is assigned.",
    verify: [
      {
        label: "research/foundation_A_pgt through foundation_G",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research",
      },
    ],
  },
  {
    id: "matter-bounce-fnl",
    tier: "N2",
    title: "Exact Matter-Contraction Non-Gaussianity Derivation",
    paper: "Paper 2",
    oneLine:
      "A reproducible rederivation of the stated matter-contraction local amplitude, with explicit convention, bounce-transfer, and survey-mapping limits.",
    why: "Makes a specific matter-contraction calculation inspectable and potentially testable. P2 rederives the squeezed value −35/16 and states the bounce-transmission and survey-mapping assumptions that must hold before it becomes an observational test.",
    what: "A convention-pinned local non-Gaussian amplitude for the stated matter-contraction setup, paired with conditional sensitivity studies. The survey numbers are forecasting diagnostics, not a detection or a unique proof of a bounce.",
    equation: "f_NL^{local} = -35/16 = -2.1875",
    prior:
      "Cai, Xue, Brandenberger & Zhang (2009); Heinrich, Doré & Krause (2023); Dalal et al. (2008); Li & Brandenberger (2014).",
    ours:
      "A reproducible derivation plus explicit accounting of convention, template, transmission, projection, and survey-covariance boundaries. Novelty and venue significance remain for independent review.",
    verify: [
      {
        label: "research/bayesian_discrimination_program/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/bayesian_discrimination_program",
      },
      {
        label: "algebraic_commutator_proof.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/matter_bounce_parameters/algebraic_commutator_proof.py",
      },
    ],
  },
  {
    id: "physics-commutator",
    tier: "N2",
    title: "Exact Ordered Four-Vertex Polynomial",
    paper: "Paper 2",
    oneLine:
      "Re-sums the four stated cubic vertices in an explicitly ordered symmetric basis and makes the coefficient convention independently checkable.",
    what: "The exact rational re-summation gives the unique ordered-basis coefficients (3, 1, -9, 5, -33, 9) and the squeezed amplitude −35/16. Independent checks use the order-grouped expressions and the general-c_s formula; the result is algebraic and scoped to the stated contraction-phase action.",
    why: "It makes the calculation's ordered-vertex convention inspectable and separates that derivation from conditional observational forecasts.",
    equation:
      "Ordered-basis coefficients: (3, 1, -9, 5, -33, 9)  ·  squeezed f_NL = −35/16",
    verify: [
      {
        label: "algebraic_commutator_proof.py",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/matter_bounce_parameters/algebraic_commutator_proof.py",
      },
    ],
  },
  {
    id: "alp-birefringence",
    tier: "N1",
    title: "Archived ALP Birefringence Exploration",
    paper: "Legacy program archive · not current P1A/P2 claim",
    oneLine:
      "Earlier exploratory ALP calculations are retained as provenance; they are not a selected claim of P1A or P2.",
    what: "The archive contains exploratory ALP evolution and synthetic-estimator checks. None is assigned to the selected P1A or P2 scientific claims, and the material is not presented as a sky measurement or an ECH prediction.",
    why: "It records an exploratory line without implying a present ECH prediction or measurement.",
    verify: [
      {
        label: "alp_field_evolution/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/alp_field_evolution",
      },
    ],
  },
  {
    id: "topological-shift-duality",
    tier: "N1",
    title: "Archived Nieh--Yan Branch Note",
    paper: "Legacy program archive · not current P1A",
    oneLine:
      "An earlier conceptual branch is preserved for traceability; it is not a general theorem or a current P1A conclusion.",
    what: "The archive records a conditional discussion of topological and non-topological Nieh--Yan constructions. It does not establish universal mutual exclusivity across gravitational models.",
    why: "The item explains prior exploration, not the present publication claim.",
    verify: [
      {
        label: "foundation_B_lock_breaking/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/research/foundation_B_lock_breaking",
      },
    ],
  },
  {
    id: "chirality-catalog",
    tier: "N2",
    title: "DESI Observed-Label Chirality Catalog and Dipole Null",
    paper: "Paper 4",
    oneLine:
      "An 8.47-million-row DESI observed-label catalog with a declared 890,069-object high-confidence sample and a primary dipole result consistent with zero.",
    what:
      "The release contains 8,474,531 DESI Legacy DR8 labels. Starting from 949,584 high-confidence rows, the declared safety quarantine removes 59,515, leaving 890,069 quality-controlled rows; 887,472 enter the supported-pixel fit. The primary result is null-consistent at z_mom=+0.635 with one-sided rank p=0.23768. Coverage-calibrated injection–recovery gives an observed-label sensitivity A95_obs≈0.98%, not a physical parity bound.",
    why:
      "It tests an observed-label chirality claim at scale while keeping label-transfer and training-composition limits explicit. It is not a physical primordial-parity constraint.",
    equation:
      "N_selected=890,069  ·  N_support=887,472  ·  z_mom=+0.635  ·  rank p=0.23768  ·  A95_obs≈0.98%",
    verify: [
      {
        label: "bamfai/galaxy-chirality-catalog (HuggingFace)",
        href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
      },
      {
        label: "chirality_catalog_paper.pdf",
        href: "/papers/chirality_catalog_paper.pdf",
      },
    ],
  },
  {
    id: "anomaly-catalog",
    tier: "N2",
    title: "Supporting DESI Public-ID Recovery (181 TARGETIDs)",
    paper: "Paper 3 · integrated supporting data release",
    oneLine:
      "A focused, reproducible public-ID recovery of a frozen historical DESI DR1 anomaly list: 181 warning-free global-primary TARGETIDs, split transparently into 170 high-coordinate-consistency core associations and 11 lower-confidence positional associations. This is an archive-recovery / provenance product — explicitly NOT a purity, novelty, or detection claim.",
    what:
      "A declared 1-arcsec positional join over 20,299,155 eligible DESI rows → 2,468 positional parents → 2,448 global-primary rows → 181 warning-free associations (170 at ≤0.1″, 11 between 0.1″ and 1″). Every released row and all 18 carried DESI fields are re-read exactly from the recorded FITS row; the release carries exact source-row provenance, quality tiers, warned-row auxiliary data, shift controls, checksums, and a clean-checkout validator. As of r10 every claim site states that the sub-0.1″ core excess is expected seed self-recovery (the single-member cluster centroid equals the seed member's own coordinates by construction), not independent association evidence.",
    why:
      "Reproducible archive provenance — recovering public IDs from a surviving historical anomaly list, with exact source-row lineage — is a transparency contribution: a reviewer can replay the exact selection waterfall and coordinate-association quality tiers. The paper deliberately declines physical classification, purity, novelty, and anomaly-rate claims that the surviving lineage does not support.",
    verify: [
      {
        label: "pipelines/p3_anomaly_engine/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p3_anomaly_engine",
      },
    ],
  },
  {
    id: "spherex-fisher",
    tier: "N2",
    title: "Conditional SPHEREx Sensitivity Mapping",
    paper: "Paper 2",
    oneLine:
      "Conditional survey-sensitivity diagnostics for the stated matter-contraction amplitude; not a detection forecast guaranteed by P2.",
    equation:
      "r=0.8354  ·  shape cosine=0.9817  ·  adopted arithmetic map=2.63σ  ·  nuisance ladder=3.5σ to 0.4σ",
    what:
      "The exact shape maps onto the published Heinrich et al. baseline with flat-grid recovery r=0.8354 (adopted r=0.84) and shape cosine 0.9817. The illustrative map is 2.63σ before additional nuisance marginalization; a channel-native surrogate spans 3.5σ with nuisances fixed, 3.1σ after A_GR marginalization, 2.3σ with a 30% b_φ prior, and 0.4σ when b_φ is free.",
    why:
      "Illustrates what additional bounce-transfer and survey assumptions would be needed to turn the derivation into an observational test.",
    verify: [
      {
        label: "research/focused_paper_source_integration/02_full_draft.tex",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/research/focused_paper_source_integration/02_full_draft.tex",
      },
    ],
  },
  {
    id: "desi-environment",
    tier: "N2",
    title: "DESI Chirality × Environment Null (z-shell corrected)",
    paper: "Paper 5",
    oneLine:
      "A catalog-native, exploratory chirality--environment comparison whose focal contrast is consistent with zero under declared controls and sensitivity checks.",
    what:
      "The released DESIVAST GALZONE universe contains 694,642 unique TARGETIDs. Joining P4 yields 145,789 rows; 145,766 OUT=0 rows form the quality parent, split into 31,937 void and 113,829 non-void rows. The adjusted non-void-minus-void contrast is +0.00145442 with SE=0.00331502, 95% CI [−0.00504290,+0.00795174], normal p=0.66085, and wild-cluster p=0.67345.",
    why:
      "It asks a distinct environment-dependence question using P4 labels; it is not preregistered, independent of P4, or a physical-handedness constraint.",
    equation:
      "Δf_CW=+0.00145442  ·  SE=0.00331502  ·  95% CI [−0.00504290,+0.00795174]  ·  p=0.66085  ·  wild-cluster p=0.67345",
    verify: [
      {
        label: "pipelines/p5_desi_chirality/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/pipelines/p5_desi_chirality",
      },
    ],
  },
  {
    id: "mcmc-verification",
    tier: "N2",
    title: "Archived MCMC Verification Infrastructure",
    paper: "Program archive · not P1B's publication role",
    oneLine:
      "Frozen posterior records document earlier verification work. They are retained for provenance and are not a current lead result; P1B is namaster-proof research software.",
    what:
      "Cobaya/CAMB chain artifacts and diagnostics are preserved as historical research records. Their prior publication assignment and headline interpretations are superseded by the approved portfolio map.",
    why: "Demonstrates honest negative reporting — we found our own bug and disclosed it.",
    verify: [
      {
        label: "reproducibility/cosmology/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility/cosmology",
      },
    ],
  },
  {
    id: "pta-bounce",
    tier: "N2",
    title: "Archived NANOGrav Slope Comparison",
    paper: "Legacy program record · not current P3",
    oneLine:
      "A simplified historical power-law slope comparison is preserved for reproducibility; it does not identify a bounce origin or exclude complete astrophysical alternatives.",
    what:
      "The archived computation uses a public summary likelihood and a simplified slope family. It is not part of the selected lead claims and would require a preregistered, multi-model physical analysis to revisit.",
    why:
      "It records an exploratory model-comparison path and, more importantly, the boundary that a single fitted slope cannot determine physical origin.",
    equation:
      "Archived simplified comparison only · no bounce detection · no complete-source exclusion",
  },
  {
    id: "namaster-validation-suite",
    tier: "N2",
    title: "namaster-proof Verification Software",
    paper: "Paper 1B",
    oneLine:
      "An installable verification library for exact NaMaster bandpower windows and content-bound execution receipts; it is software infrastructure, not a sky measurement.",
    what:
      "The package exercises exact bandpower-window application, validates receipt/result byte binding, and ships tests and examples for the two failure modes described by P1B. Historical birefringence and chirality experiments remain program provenance and are not P1B headline results.",
    why:
      "It turns two reproducibility hazards into testable software contracts that other pseudo-C_ℓ analyses can reuse.",
  },
  {
    id: "provenance-audit",
    tier: "N2",
    title: "Provenance-Audit Methodology (retract-and-rebuild)",
    paper: "Paper 4 / program-wide",
    oneLine:
      "Artifact-level provenance checks caught unsupported intermediate claims, which were withdrawn before submission and replaced only when a current, reproducible result existed.",
    what:
      "The workflow binds claims to file hashes, generators, footprint checks, exact inputs, and rerunnable outputs. Failed provenance does not become a caveat attached to a headline; it removes the headline until a supported replacement exists. Current paper values must come from each final candidate, not superseded audit-era numbers.",
    why:
      "Most published nulls and detections never face an artifact-level audit. Treating retraction-and-rebuild as a first-class, documented workflow is itself a transparency contribution — reviewers can replay the exact decision chain.",
  },
  {
    id: "compute-reproducibility-chain",
    tier: "N2",
    title: "12-Job Compute Reproducibility Chain",
    paper: "Program-wide",
    oneLine:
      "All 12 load-bearing compute closures (fsky sweeps, continuous-prior MCMC, permutation rebuilds, sign-symmetry reruns) executed on a dedicated pod with committed scripts + JSON artifacts, for ~$0.55 total.",
    what:
      "Each archived job ships its driver, inputs, seeds, and output artifact. Earlier P1B/MCMC assignments are superseded; the current P1B contribution is namaster-proof. P4/P5 receipts remain supporting reproducibility evidence for their scoped claims.",
    why:
      "A reviewer can rerun any headline number from the committed chain — reproducibility as an artifact, not a promise.",
    verify: [
      {
        label: "h200_scripts/experiments/",
        href: "https://github.com/Hubify-Projects/bigbounce/tree/main/h200_scripts/experiments",
      },
    ],
  },
  {
    id: "bigae-anomaly-detector",
    tier: "N2",
    title: "Archived BigAE Multi-Survey Pipeline",
    paper: "Legacy anomaly work · not current P3",
    oneLine:
      "Historical autoencoder pipeline artifacts are preserved, but their cross-survey counts and validation claims are not the current anomaly flagship and are not acceptance targets for the clean DESI rerun.",
    why: "The archive records useful lessons about domain shift, native retraining, and provenance. Its scientific claims must be regenerated under the new fail-closed model/input/scaler contract.",
    what:
      "Legacy per-survey retrains exposed severe cross-transfer domain shift. The new flagship must regenerate the DESI sample with immutable inputs, the hash-bound model, a sealed scaler, shard receipts, deterministic deduplication, and independent candidate validation.",
    prior:
      "Autoencoder outlier detection (Baron & Poznanski 2017); single-survey spectral anomaly searches.",
    ours:
      "No current novelty claim is assigned to the unreconciled multi-survey catalog. The reusable contribution is the preserved failure analysis and the clean-rerun contract now governing the rebuild.",
    verify: [
      {
        label: "6-way dedup artifact (EXACT-MATCH)",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p3_anomaly_engine/outputs/sixway_dedup_artifact.json",
      },
      {
        label: "bamfai/desi-spectral-anomaly-detector (model)",
        href: "https://huggingface.co/bamfai/desi-spectral-anomaly-detector",
      },
      {
        label: "bamfai/bigbounce-anomaly-catalog (dataset)",
        href: "https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog",
      },
    ],
  },
  {
    id: "chirality-equivariant-classifier",
    tier: "N2",
    title: "Z₂-Flip-Equivariant Chirality Classifier (released model)",
    paper: "Papers 4 & 5",
    oneLine:
      "A released classifier/checkpoint used to produce observed chirality labels, with reflection-aware processing and documented training-composition limits.",
    why: "Reflection-aware processing is a useful control for orientation-sensitive labels, but it does not calibrate true spin or remove every survey and training systematic.",
    what:
      "The released ViT-based checkpoint supports P4/P5 reproducibility. P4 documents unresolved historical training-composition conflicts and an unreproduced CE-included accuracy path; the released catalog labels remain observed classifier outputs, not calibrated physical handedness.",
    prior:
      "CNN/ViT galaxy-morphology classifiers (Galaxy Zoo DECaLS, Zoobot); standard non-equivariant chirality classifiers (Shamir et al.).",
    ours:
      "The reusable output is the released checkpoint plus its declared scope and provenance boundary; priority claims are left to independent review.",
    verify: [
      {
        label: "bamfai/galaxy-chirality-v2 (model)",
        href: "https://huggingface.co/bamfai/galaxy-chirality-v2",
      },
      {
        label: "bamfai/galaxy-chirality-catalog (dataset)",
        href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog",
      },
    ],
  },
  {
    id: "gz1-only-independence",
    tier: "N2",
    title: "Historical GZ1-Only Control",
    paper: "Paper 4",
    oneLine:
      "A lower-power human-label control is preserved as supporting evidence; it neither proves a physical null nor replaces P4's current quality-controlled primary estimator.",
    why: "The control probes sensitivity to one training path while leaving morphology transfer, footprint, and upstream imaging systematics unresolved.",
    what:
      "The archived GZ1-only run is null-consistent at lower power. It is a historical robustness control, not the current P4 headline and not a physical-parity constraint.",
    prior:
      "Self-training / pseudo-label validation typically checks classifier accuracy, not downstream-measurement independence.",
    ours:
      "Useful supporting control with a deliberately bounded interpretation.",
    verify: [
      {
        label: "gz1only_dipole_result.json",
        href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p2_chirality/outputs/gz1only_dipole_result.json",
      },
      {
        label: "bamfai/galaxy-chirality-v2 (gz1only ckpt)",
        href: "https://huggingface.co/bamfai/galaxy-chirality-v2/tree/main/gz1only",
      },
    ],
  },
];

function ContributionCard({ c }: { c: Contribution }) {
  const color = TIER_COLOR[c.tier];
  return (
    <Card
      id={c.id}
      style={{
        padding: 20,
        borderLeft: `3px solid ${color}`,
        scrollMarginTop: 80,
      }}
    >
      <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: 10 }}>
        <span
          style={{
            display: "inline-block",
            padding: "2px 8px",
            borderRadius: 4,
            background: color,
            color: "#fff",
            fontFamily: "var(--font-mono-stack)",
            fontSize: 10,
            fontWeight: 700,
            letterSpacing: 0.4,
          }}
        >
          {TIER_LABEL[c.tier]}
        </span>
        <span
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: 11,
            color: "var(--text-muted)",
          }}
        >
          {c.paper}
        </span>
      </div>
      <h3
        style={{
          marginTop: 10,
          marginBottom: 6,
          fontFamily: "var(--font-mono-stack)",
          fontSize: 16,
          fontWeight: 600,
        }}
      >
        {c.title}
      </h3>
      <p style={{ marginTop: 0, fontSize: 13, lineHeight: 1.6 }}>{c.oneLine}</p>
      {c.equation && (
        <div
          style={{
            marginTop: 10,
            padding: "8px 12px",
            background: "color-mix(in srgb, var(--accent) 6%, var(--surface))",
            borderLeft: "2px solid var(--accent)",
            fontFamily: "var(--font-mono-stack)",
            fontSize: 12,
            lineHeight: 1.6,
          }}
        >
          {c.equation}
        </div>
      )}
      <h4 style={{ marginTop: 14, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
        Why it matters
      </h4>
      <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.why}</p>
      <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
        What it is
      </h4>
      <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.what}</p>
      {c.prior && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            What existed before
          </h4>
          <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.prior}</p>
        </>
      )}
      {c.ours && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            What we did
          </h4>
          <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>{c.ours}</p>
        </>
      )}
      {c.verify && c.verify.length > 0 && (
        <>
          <h4 style={{ marginTop: 12, marginBottom: 4, fontSize: 12, textTransform: "uppercase", letterSpacing: 0.6, color: "var(--text-muted)" }}>
            How to verify
          </h4>
          <ul style={{ margin: 0, paddingLeft: 18, fontSize: 13, lineHeight: 1.8 }}>
            {c.verify.map((v) => (
              <li key={v.href}>
                <a
                  href={v.href}
                  target={v.href.startsWith("http") ? "_blank" : undefined}
                  rel="noopener noreferrer"
                  style={{ color: "var(--accent)", fontFamily: "var(--font-mono-stack)", fontSize: 12, overflowWrap: "anywhere" }}
                >
                  {v.label}
                </a>
              </li>
            ))}
          </ul>
        </>
      )}
    </Card>
  );
}

export default function ContributionsPage() {
  const grouped: Record<Tier, Contribution[]> = { N4: [], N3: [], N2: [], N1: [] };
  for (const c of contributions) grouped[c.tier].push(c);
  const counts = {
    N4: grouped.N4.length,
    N3: grouped.N3.length,
    N2: grouped.N2.length,
    N1: grouped.N1.length,
  };
  return (
    <>
      <div className="hero">
        <p className="eyebrow" style={{ marginBottom: 8 }}>
          Novelty accounting
        </p>
        <h1 style={{ fontFamily: "var(--font-mono-stack)", fontWeight: 600 }}>
          contributions
        </h1>
        <p className="subtitle">
          Each contribution is scored on the canonical four-tier novelty scale.
          Our self-claim ceiling is <strong>N3</strong> (first-of-kind
          demonstration). <strong>N4</strong> — paradigm-shifting / Nobel-worthy —
          is intentionally reserved for outside arbiters and is never
          self-claimed. Definitions, prior work, and verification links below.
        </p>
      </div>

      <section id="program-arc" style={{ marginTop: 28 }}>
        <p
          className="eyebrow"
          style={{ marginBottom: 8 }}
        >
          How the research outputs fit together
        </p>
        <p style={{ marginTop: 0, fontSize: 14, lineHeight: 1.7, maxWidth: "64ch" }}>
          The portfolio now follows <strong>three scientific questions</strong>,
          not a fixed paper count. Bounce theory contains the lead P2 calculation,
          a focused P1A boundary Note, and P1B verification software. DESI anomaly
          discovery is being rebuilt as a science-first flagship, with the current
          P3 retained as its public-ID provenance release. Galaxy chirality contains
          the lead P4 observed-label catalog/null result and the distinct P5
          chirality–environment companion. These programs share methods and data,
          but they do not constitute a single evidentiary chain from bounce theory
          to a claimed survey detection.
        </p>
        <div style={{ display: "grid", gap: 0, marginTop: 16 }}>
          {[
            { n: "P1A", role: "Focused theory Note: derives the minimal ECH contact term and identifies the zero-spin scalar branch boundary under stated assumptions." },
            { n: "P1B", role: "Research software: exact pseudo-Cℓ window inference and tamper-evident provenance for reproducible spin-2 analyses; it makes no cosmological detection claim." },
            { n: "P2", role: "Lead theory paper: rederives f_NL^local = −35/16 for the stated matter-contraction setup and makes its bounce-transmission and survey-mapping conditions explicit." },
            { n: "P3", role: "Supporting data release: recovers 181 DESI DR1 TARGETIDs from a frozen historical list. It is provenance support for the rebuilt anomaly flagship, not a replacement discovery paper." },
            { n: "P4", role: "Lead catalog paper: releases 8.47M observed chirality labels and reports a declared primary dipole statistic consistent with zero, without converting it into a physical primordial-parity constraint." },
            { n: "P5", role: "Standalone AJ companion: tests a distinct catalog-native void/non-void classifier-label contrast and finds no detected difference; it does not establish physical environment independence." },
          ].map((p, i) => (
            <div
              key={p.n}
              style={{
                display: "grid",
                gridTemplateColumns: "56px 1fr",
                gap: 14,
                alignItems: "baseline",
                padding: "10px 0",
                borderTop: i === 0 ? "none" : "1px solid var(--border)",
              }}
            >
              <span
                style={{
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 13,
                  fontWeight: 700,
                  color: "var(--accent)",
                }}
              >
                {p.n}
              </span>
              <span style={{ fontSize: 13, lineHeight: 1.6 }}>{p.role}</span>
            </div>
          ))}
        </div>
        <p style={{ marginTop: 12, fontSize: 12.5, lineHeight: 1.6, color: "var(--text-muted)" }}>
          Approved endpoint: six standalone works across the three programs, plus
          P3 as a supporting data release integrated with the rebuilt anomaly
          flagship. See the{" "}
          <Link href="/paper" style={{ color: "var(--accent)" }}>
            research programs and evidence library
          </Link>{" "}
          for full status and PDFs.
        </p>
      </section>

      <section
        id="tier-scale"
        style={{
          marginTop: 24,
          padding: 16,
          border: "1px solid var(--border)",
          borderRadius: 8,
          background: "var(--surface)",
        }}
      >
        <div
          style={{
            fontFamily: "var(--font-mono-stack)",
            fontSize: 10,
            textTransform: "uppercase",
            letterSpacing: 0.8,
            color: "var(--text-muted)",
            marginBottom: 10,
          }}
        >
          Novelty tier scale
        </div>
        <div style={{ display: "grid", gap: 8 }}>
          {(["N4", "N3", "N2", "N1"] as Tier[]).map((tier) => {
            const isReserved = tier === "N4";
            return (
              <div
                key={tier}
                style={{
                  display: "grid",
                  gridTemplateColumns: "auto 1fr auto",
                  alignItems: "center",
                  gap: 12,
                  padding: "8px 10px",
                  borderLeft: `3px solid ${TIER_COLOR[tier]}`,
                  background: isReserved
                    ? "color-mix(in srgb, #b91c1c 5%, var(--surface))"
                    : "transparent",
                  opacity: isReserved ? 0.85 : 1,
                }}
              >
                <span
                  style={{
                    display: "inline-block",
                    padding: "2px 8px",
                    borderRadius: 4,
                    background: TIER_COLOR[tier],
                    color: "#fff",
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 10,
                    fontWeight: 700,
                    letterSpacing: 0.4,
                    minWidth: 28,
                    textAlign: "center",
                  }}
                >
                  {tier}
                </span>
                <span style={{ fontSize: 12, lineHeight: 1.5 }}>
                  <strong
                    style={{
                      fontFamily: "var(--font-mono-stack)",
                      fontSize: 11,
                      letterSpacing: 0.4,
                      color: TIER_COLOR[tier],
                    }}
                  >
                    {TIER_LABEL[tier]}
                  </strong>
                  {" — "}
                  {TIER_DEF[tier]}
                </span>
                <span
                  style={{
                    fontFamily: "var(--font-mono-stack)",
                    fontSize: 11,
                    color: "var(--text-muted)",
                    minWidth: 50,
                    textAlign: "right",
                  }}
                >
                  {isReserved ? "reserved" : `${counts[tier]} item${counts[tier] === 1 ? "" : "s"}`}
                </span>
              </div>
            );
          })}
        </div>
      </section>

      <div className="contrib-layout">
        <aside className="contrib-layout-aside" style={{ position: "sticky", top: 80, alignSelf: "start" }}>
          <div
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 10,
              textTransform: "uppercase",
              letterSpacing: 0.8,
              color: "var(--text-muted)",
              marginBottom: 8,
            }}
          >
            By tier
          </div>
          {(["N4", "N3", "N2", "N1"] as Tier[]).map((tier) => (
            <a
              key={tier}
              href={`#tier-${tier}`}
              style={{
                display: "block",
                padding: "6px 10px",
                marginBottom: 4,
                fontFamily: "var(--font-mono-stack)",
                fontSize: 12,
                color: "var(--text)",
                textDecoration: "none",
                borderLeft: `2px solid ${TIER_COLOR[tier]}`,
              }}
            >
              <span style={{ color: TIER_COLOR[tier], fontWeight: 700 }}>{tier}</span>
              {" — "}
              {tier === "N4" ? "reserved" : `${counts[tier]} item${counts[tier] === 1 ? "" : "s"}`}
            </a>
          ))}
          <div
            style={{
              fontFamily: "var(--font-mono-stack)",
              fontSize: 10,
              textTransform: "uppercase",
              letterSpacing: 0.8,
              color: "var(--text-muted)",
              marginTop: 18,
              marginBottom: 8,
            }}
          >
            All contributions
          </div>
          {contributions.map((c) => (
            <a
              key={c.id}
              href={`#${c.id}`}
              style={{
                display: "block",
                padding: "4px 10px",
                fontFamily: "var(--font-mono-stack)",
                fontSize: 11,
                color: "var(--text-muted)",
                textDecoration: "none",
                lineHeight: 1.4,
              }}
            >
              {c.title}
            </a>
          ))}
          <Link
            href="/old/contributions.html"
            style={{
              display: "block",
              marginTop: 20,
              padding: "8px 10px",
              fontFamily: "var(--font-mono-stack)",
              fontSize: 11,
              color: "var(--accent)",
              textDecoration: "none",
              border: "1px solid var(--border)",
              borderRadius: 6,
            }}
          >
            ↗ full legacy contributions page
          </Link>
        </aside>

        <div style={{ display: "grid", gap: 14 }}>
          <section id="tier-N4" style={{ scrollMarginTop: 80 }}>
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: 10,
                marginBottom: 12,
              }}
            >
              <Badge variant="outline" className="font-mono text-[10px]">
                N4
              </Badge>
              <h2
                style={{
                  margin: 0,
                  fontFamily: "var(--font-mono-stack)",
                  fontSize: 14,
                  textTransform: "uppercase",
                  letterSpacing: 0.6,
                  color: TIER_COLOR.N4,
                }}
              >
                {TIER_LABEL.N4}
              </h2>
            </div>
            <Card
              style={{
                padding: 20,
                borderLeft: `3px solid ${TIER_COLOR.N4}`,
                background: "color-mix(in srgb, #b91c1c 4%, var(--surface))",
              }}
            >
              <p style={{ margin: 0, fontSize: 13, lineHeight: 1.6 }}>
                <strong>Intentionally empty.</strong> N4 is reserved for
                paradigm-shifting, consensus-breaking, or Nobel-worthy results.
                That tier is awarded by the field over time — through broad
                community replication, citation, and consensus — not by the
                authors. We cap our own claims at N3 (first-of-kind
                demonstration / new constraint / new direction) and let outside
                arbiters raise the ceiling if any of this work earns it.
              </p>
              <p
                style={{
                  marginTop: 10,
                  marginBottom: 0,
                  fontSize: 12,
                  lineHeight: 1.6,
                  color: "var(--text-muted)",
                }}
              >
                No BigBounce paper self-annotates at N4. Site copy, paper abstracts,
                and all contribution records are capped at N3 by internal review.
              </p>
            </Card>
          </section>

          {(["N3", "N2", "N1"] as Tier[]).map(
            (tier) =>
              grouped[tier].length > 0 && (
                <section key={tier} id={`tier-${tier}`} style={{ scrollMarginTop: 80 }}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 10,
                      marginBottom: 12,
                    }}
                  >
                    <Badge variant="outline" className="font-mono text-[10px]">
                      {tier}
                    </Badge>
                    <h2
                      style={{
                        margin: 0,
                        fontFamily: "var(--font-mono-stack)",
                        fontSize: 14,
                        textTransform: "uppercase",
                        letterSpacing: 0.6,
                        color: TIER_COLOR[tier],
                      }}
                    >
                      {TIER_LABEL[tier]}
                    </h2>
                  </div>
                  <div style={{ display: "grid", gap: 14 }}>
                    {grouped[tier].map((c) => (
                      <ContributionCard key={c.id} c={c} />
                    ))}
                  </div>
                </section>
              ),
          )}
        </div>
      </div>
    </>
  );
}
