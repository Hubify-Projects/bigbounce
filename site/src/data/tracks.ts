import type { EvidenceGrade } from "@/components/primitives";
import type { ResearchProgramId } from "@/data/papers";
import type { ContributionType } from "@/lib/contributionTypes";

/**
 * Track content for /research and /research/[track] (REDESIGN_SPEC.md §3.3,
 * Lane 2). Sourced verbatim-in-substance from VISION.md (the three routes to
 * the guiding question) and PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md (the
 * three-program map), with the 2026-09-04 session's science results
 * (SESSION_HANDOFF_2026-09-04.md) folded into lead results and channels.
 * Readiness/version numbers are NOT stored here — every work row resolves
 * its live number through lib/livePapers.ts at render time.
 */

export type TrackSlug = "track-a" | "track-b" | "track-c";

export interface TrackChannel {
  channel: string;
  prediction: string;
  currentData: string;
  grade: EvidenceGrade;
  receiptLabel: string;
  receiptHref: string;
}

export interface TrackOpenItem {
  item: string;
  blocker: string;
}

export interface Track {
  slug: TrackSlug;
  letter: "A" | "B" | "C";
  /** Links this track's works into researchPrograms (papers.ts) + Convex. */
  programId: ResearchProgramId;
  navTitle: string;
  question: string;
  leadResult: string;
  leadEquation?: string;
  leadGrade: EvidenceGrade;
  channels: TrackChannel[];
  /** Paper slugs shown under "Works in this track", in display order. */
  paperSlugs: string[];
  openItems: TrackOpenItem[];
  boundary: string;
}

const REPO = "https://github.com/Hubify-Projects/bigbounce/blob/main";
const TREE = "https://github.com/Hubify-Projects/bigbounce/tree/main";

export const tracks: Track[] = [
  {
    slug: "track-a",
    letter: "A",
    programId: "track-a-bounce-vs-inflation",
    navTitle: "Track A — Bounce vs. inflation",
    question:
      "Does a nonsingular matter-bounce produce a distinctive, reproducible, and observationally testable primordial non-Gaussian signature that beats inflation-from-a-singularity as the origin of structure?",
    leadResult:
      "The exact matter-contraction amplitude f_NL^local = −35/16 is confirmed by an independent from-scratch in-in computation, which also locates Cai et al. (2009)'s published −35/8 as a uniform missing factor of 2, not a competing result. Transmitted through an explicit nonsingular bounce (the bounce's own cubic term, Δf_NL^bounce = −(5/24)ρ_B), the amplitude becomes f_NL^after ∈ [−0.65, −0.50] across three background choices — the number a survey would actually see.",
    leadEquation: "f_NL^local = −35/16  →  f_NL^after ∈ [−0.65, −0.50]",
    leadGrade: "derived",
    channels: [
      {
        channel: "Pulsar timing array (nHz stochastic background)",
        prediction: "Bounce-sourced scalar-induced GW spectrum, γ_pred = 5.07.",
        currentData: "Ω_GW h²(f_yr) = 1.45e−23 — 14.3 dex below the NANOGrav 15-yr signal.",
        grade: "null",
        receiptLabel: "SIGW_NHZ_NOTE_2026-09-04.md",
        receiptHref: `${TREE}/research/track_a3_multichannel`,
      },
      {
        channel: "Primordial black holes",
        prediction: "Bounce-sourced Δ²_ζ produces an observable PBH abundance.",
        currentData: "f_PBH = 0 — 7.0 dex short of a detectable population.",
        grade: "null",
        receiptLabel: "inlab_delta2_zeta_2026-09-03",
        receiptHref: `${TREE}/research/track_a3_multichannel`,
      },
      {
        channel: "High-z PNG / early-SMBH seeds",
        prediction: "A broadband early-SMBH-seed amplitude from bounce non-Gaussianity.",
        currentData: "FIRAS excludes the amplitude by roughly 1.8e3×.",
        grade: "null",
        receiptLabel: "inlab_delta2_zeta_2026-09-03",
        receiptHref: `${TREE}/research/track_a3_multichannel`,
      },
      {
        channel: "LSS bispectrum (SPHEREx-era)",
        prediction: "f_NL^after ∈ [−0.65, −0.50], transmitted through the bounce.",
        currentData: "Reachable but not separable from ΛCDM at 0.7–0.9σ with SPHEREx-class survey sensitivity.",
        grade: "open",
        receiptLabel: "SSOT/paper-a3m/status.md",
        receiptHref: `${REPO}/project-context/SSOT/paper-a3m/status.md`,
      },
    ],
    paperSlugs: ["paper-a3m", "paper-2l"],
    openItems: [
      {
        item: "Ledger row 9 — bounce-scale enhancement at kη_B ~ 1",
        blocker: "The only remaining non-null route for the PTA/PBH channels; a science decision here is required before another review round (directive R2).",
      },
      {
        item: "A3-4(r) — remaining multi-channel robustness check",
        blocker: "Open at end of the 2026-09-04 session; tracked in NEXT_SCIENCE_LEDGER.md.",
      },
      {
        item: "A2 — nonlinear transmission research brief",
        blocker: "Not yet a complete manuscript; the transmission result folded into A3M so far covers the bounce's own cubic term only.",
      },
    ],
    boundary:
      "This track does not claim a measured detection. Three of its four observational channels are closed nulls; the fourth (LSS bispectrum) is reachable but not yet separable from ΛCDM at current survey sensitivity. Readiness on the flagship manuscript (A3M) stands at 75 — R2 verification closed, further rounds require a new science decision.",
  },
  {
    slug: "track-b",
    letter: "B",
    programId: "track-b-ech-note",
    navTitle: "Track B — The ECH Note",
    question:
      "What does minimal Einstein–Cartan–Holst spin-torsion gravity do for the bounce, and what can it not do for dark energy?",
    leadResult:
      "The derived axial spin-spin contact term is identified with Popławski's torsion-bounce repulsion mechanism — the positive result. The same algebraic elimination that produces it closes four candidate dark-energy routes — the negative result, stated in the same Note rather than hedged around.",
    leadGrade: "derived",
    channels: [
      {
        channel: "Torsion-bounce repulsion mechanism",
        prediction: "Minimal ECH's axial spin-spin contact term matches Popławski's bounce mechanism.",
        currentData: "Derived and identified; consistent with the mechanism as stated.",
        grade: "derived",
        receiptLabel: "paper-1n source",
        receiptHref: `${REPO}/arxiv/paper1n_ech_note.tex`,
      },
      {
        channel: "Minimal-ECH dark-energy routes (4 candidates)",
        prediction: "A viable dark-energy mechanism survives the same elimination.",
        currentData: "All four candidate routes close under the algebra — none survives.",
        grade: "null",
        receiptLabel: "paper-1n source",
        receiptHref: `${REPO}/arxiv/paper1n_ech_note.tex`,
      },
      {
        channel: "Chiral gravitational waves (LISA band)",
        prediction: "A parity-odd O(h²) operator from minimal ECH + Dirac/Weyssenhoff matter.",
        currentData: "No such operator exists in this setup; Δ_h is structurally k-odd, ≤6e−13 at LISA — ledger #7 closed negative.",
        grade: "null",
        receiptLabel: "chiral_gw_gate",
        receiptHref: `${TREE}/research/chiral_gw_gate`,
      },
    ],
    paperSlugs: ["paper-1n"],
    openItems: [
      {
        item: "First INT/EXT review board on the merged Note",
        blocker: "P1N has not yet been through any review board; P1A + P1C review churn stopped after R13 as separate manuscripts.",
      },
      {
        item: "Houston's final sign-off read",
        blocker: "Readiness 95 (v1N.0.5) pending Houston's personal review quote in SSOT/paper-1n/status.md.",
      },
    ],
    boundary:
      "This is a closed theory line, not a dark-energy model or a cosmological detection. It states plainly what minimal ECH torsion can and cannot explain, and does not extend the contact-term result beyond the stated minimal assumptions.",
  },
  {
    slug: "track-c",
    letter: "C",
    programId: "track-c-desi-data-products",
    navTitle: "Track C — DESI data products",
    question:
      "What do DESI's public galaxy and spectral data show when tested directly against the rotating-black-hole-universe spin-axis prediction and scanned for early-universe anomalies — and what does that say about bounce vs. inflation?",
    leadResult:
      "The largest test to date of Popławski's galaxy-spin-axis prediction, run on 8.47M DESI spirals with a void-environment cross-check, is a null: the catalog's own sensitivity floor excludes alignment fractions η > 0.98% at ≥95% coverage — a factor of 2–20× below the amplitudes reported in the literature it tests.",
    leadGrade: "null",
    channels: [
      {
        channel: "Galaxy spin-axis alignment (chirality dipole)",
        prediction: "A preferred large-scale spin axis per the rotating-black-hole-universe model.",
        currentData: "Null: z_mom=+0.635, rank p=0.238 on 890,069 QC'd galaxies; A_95 ≈ 0.98% exclusion.",
        grade: "null",
        receiptLabel: "paper-4p source",
        receiptHref: `${REPO}/arxiv/paper4p_chirality.tex`,
      },
      {
        channel: "Early-universe anomaly map (C2, redirected)",
        prediction: "Anomalies that strain single-field inflation (over-massive high-z galaxies, PNG, isolated early SMBHs).",
        currentData: "Answered as a data release, not yet a discriminator paper: anomaly catalogue v2, 1,244 science targets, no reference class clears the confirmed-class bar (best match 4.2×).",
        grade: "open",
        receiptLabel: "ANOMALY_CATALOGUE_RELEASE_v2",
        receiptHref: `${TREE}/pipelines/p3_anomaly_engine/release`,
      },
    ],
    paperSlugs: ["paper-4p", "paper-3", "paper-1b"],
    openItems: [
      {
        item: "C2 discriminator paper",
        blocker: "Contingent on an autoencoder catalogue earning its way past the known-object recovery benchmark (ledger #8, now answered as a data release rather than a detector paper).",
      },
      {
        item: "Houston's final sign-off read",
        blocker: "P4′ v4P.0.5 readiness 95 pending Houston's personal review quote in SSOT/paper-4p/status.md.",
      },
    ],
    boundary:
      "P4′'s exclusion bears on the rotating-black-hole-universe model's spin-axis claim only — it is not itself a bounce-cosmology detection. P3 is a provenance/public-ID data release, not a validated anomaly-rate or discovery claim; P1B (namaster-proof) is a software/verification result, not a physical measurement.",
  },
];

export function getTrack(slug: string): Track | undefined {
  return tracks.find((t) => t.slug === slug);
}

// ──────────────────────────────────────────────────────────────────────
// Contributions — N1–N4 novelty-graded list, ported from the retired
// /contributions page and rewritten to track framing (REDESIGN_SPEC.md
// §2.4 "/contributions → /research#contributions"). Kept in this file
// (not a new data file) since Lane 2 owns only tracks.ts + the three
// page.tsx files. Novelty ceiling is N3 — N4 is reserved for outside
// arbiters and never self-claimed.
// ──────────────────────────────────────────────────────────────────────

export type NoveltyTier = "N3" | "N2" | "N1";

export interface Contribution {
  id: string;
  tier: NoveltyTier;
  contributionType: ContributionType;
  /** Paper slugs (papers.ts) this contribution is reported in, for the
   * tier + type chip shown on /papers/[slug]. Not every contribution
   * maps to exactly one paper. */
  paperSlugs?: string[];
  title: string;
  track: "Track A" | "Track B" | "Track C" | "Program-wide";
  oneLine: string;
  href: string;
}

export const contributions: Contribution[] = [
  {
    id: "matter-bounce-fnl",
    tier: "N2",
    contributionType: "derivation",
    paperSlugs: ["paper-a3m"],
    title: "Exact Matter-Contraction Non-Gaussianity",
    track: "Track A",
    oneLine:
      "Reproducible derivation of f_NL^local = −35/16 with explicit convention, bounce-transmission, and survey-mapping boundaries; independently re-derived from scratch.",
    href: `${TREE}/research/matter_bounce_parameters`,
  },
  {
    id: "bounce-transmission",
    tier: "N2",
    contributionType: "derivation",
    paperSlugs: ["paper-a3m"],
    title: "Bounce Transmission of the Non-Gaussian Amplitude",
    track: "Track A",
    oneLine:
      "The bounce's own cubic term (Δf_NL^bounce = −(5/24)ρ_B) carries f_NL^local through an explicit nonsingular bounce to f_NL^after ∈ [−0.65, −0.50] across three background choices.",
    href: `${TREE}/research/cubic_bounce_transmission`,
  },
  {
    id: "multichannel-consistency",
    tier: "N2",
    contributionType: "null-result",
    paperSlugs: ["paper-a3m"],
    title: "Multi-Channel Consistency Test (PTA, PBH, high-z PNG)",
    track: "Track A",
    oneLine:
      "The transmitted amplitude is checked against pulsar timing, primordial black holes, and high-z non-Gaussianity in one lab spectrum — three honest nulls, not three separate hopes.",
    href: `${TREE}/research/track_a3_multichannel`,
  },
  {
    id: "ech-contact-term",
    tier: "N2",
    contributionType: "derivation",
    paperSlugs: ["paper-1n"],
    title: "Minimal-ECH Contact Term Identified with the Popławski Mechanism",
    track: "Track B",
    oneLine:
      "The derived axial spin-spin contact term is identified with Popławski's torsion-bounce repulsion, stated alongside the same algebra's closure of four dark-energy routes.",
    href: `${REPO}/arxiv/paper1n_ech_note.tex`,
  },
  {
    id: "chiral-gw-gate",
    tier: "N1",
    contributionType: "null-result",
    paperSlugs: ["paper-1n"],
    title: "Chiral Gravitational-Wave Gate — Closed Negative",
    track: "Track B",
    oneLine:
      "Minimal ECH + Dirac/Weyssenhoff matter has no parity-odd O(h²) operator; the birefringence signal is structurally k-odd, ≤6e−13 at LISA.",
    href: `${TREE}/research/chiral_gw_gate`,
  },
  {
    id: "chirality-catalog",
    tier: "N2",
    contributionType: "catalogue",
    paperSlugs: ["paper-4p"],
    title: "8.47M-Galaxy Chirality Catalog and Spin-Axis Null",
    track: "Track C",
    oneLine:
      "The largest test of the rotating-black-hole-universe spin-axis prediction: a quality-controlled 890,069-row null (z_mom=+0.635, rank p=0.238) with a void-environment cross-check, excluding literature amplitudes 2–20×.",
    href: `${REPO}/arxiv/paper4p_chirality.tex`,
  },
  {
    id: "anomaly-catalogue-v2",
    tier: "N2",
    contributionType: "data-release",
    paperSlugs: ["paper-3"],
    title: "Anomaly Catalogue v2 — Public Science-Target Data Release",
    track: "Track C",
    oneLine:
      "1,244 science-target spectral anomalies released with provenance and cross-matching; answered as a data release, not yet a discovery paper, after no reference class cleared the confirmed-class bar.",
    href: `${TREE}/pipelines/p3_anomaly_engine/release`,
  },
  {
    id: "namaster-proof",
    tier: "N2",
    contributionType: "method-tool",
    paperSlugs: ["paper-1b"],
    title: "namaster-proof Verification Software",
    track: "Track C",
    oneLine:
      "A small verification library that proves an exact NaMaster bandpower-window inference wasn't shortcut, with tamper-evident, content-bound computational receipts.",
    href: `${REPO}/arxiv/paper1b_namaster_proof.tex`,
  },
];
