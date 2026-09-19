// Content source: research/archaeology_2025/RETIRED_HYPOTHESES.md +
// LEGACY_HYPOTHESIS_LEDGER.md (2026-09-19)
//
// This file renders the /genealogy page — the pre-2026 exploratory lineage of
// the BigBounce program, mined for questions, never restored as theory.
// Every claim below is either (a) a plain historical fact about what Houston
// explored and when, or (b) a disposition already recorded in
// research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md and the
// director's corrections in the same file. Nothing here is current science.

export interface Generation {
  period: string;
  title: string;
  explored: string;
  survived: string;
}

export type RetiredStatus = "retired" | "null" | "closed";

export interface RetiredHypothesis {
  name: string;
  claim: string;
  whyRetired: string;
  evidence: string;
  status: RetiredStatus;
}

export interface OpenQuestion {
  title: string;
  question: string;
  ledgerItem: string;
  layer: "open-question";
  /** The archaeology memo's answer, in <=25 words. Not a new result. */
  finding: string;
}

export interface ProvenanceEntry {
  title: string;
  role: string;
}

export const generations: Generation[] = [
  {
    period: "Mar 2025",
    title: "White Hole Sponge / ICBC",
    explored:
      "A universe ending in a giant black hole with white-hole rebirth — ICBC, QGBW, the Omega Black Hole, and a Vacuum Collapse Anomaly (VCA) triggering mechanism.",
    survived:
      "The White Hole Sponge / ICBC physics package itself was retired outright (ledger status F, zero derivation) — only the general intuition that gravitational collapse might terminate in a nonsingular new expanding spacetime carried forward, via the Black Hole Sponge pivot below.",
  },
  {
    period: "Mar 25–27, 2025",
    title: "Black Hole Sponge pivot",
    explored:
      "A reframing away from a literal “white-hole universe” toward our universe as the interior, or daughter, of a parent black hole.",
    survived:
      "The genuine conceptual seed of the parent→daughter framing (ledger status C) — historical/speculative, not a retired package, and what later became scientifically tractable.",
  },
  {
    period: "Jul 2025",
    title: "“Born in a black hole” (ECSK + LQC)",
    explored:
      "Einstein–Cartan spin-torsion combined with a loop-quantum-cosmology-like bounce, a rotating parent black hole, and inherited observables passed from parent to daughter universe.",
    survived:
      "The legitimate Einstein–Cartan–Sciama–Kibble (ECSK) nonsingular black-hole/bounce literature and the parent→daughter-universe question — the strongest scientific kernel of the old work.",
  },
  {
    period: "2026",
    title: "BigBounce falsifiable program",
    explored:
      "Derivations, reproducibility, adversarial peer review, DESI data, and actual falsification tests replace the earlier speculative framing.",
    survived:
      "A much narrower, substantially more defensible program: bounce phenomenology, the ECH torsion mechanism, and DESI tests, with failed routes openly published as nulls rather than quietly dropped.",
  },
  {
    period: "18 Sep 2026",
    title: "Legacy archaeology lane",
    explored:
      "A rigorous re-audit of the 2025 Notion notes against current literature and the live BigBounce record: recover every distinct idea, locate its scientific kernel if any, and disposition it explicitly.",
    survived:
      "This page — a curated, disclaimed genealogy separating retired hypotheses from the small number of questions still open, plus three new ledger items (#20–#22) tracking the surviving questions.",
  },
];

export const retired: RetiredHypothesis[] = [
  {
    name: "ICBC as dark energy",
    claim:
      "The Inverted/Interior Cosmic Boundary Curvature (ICBC) was proposed as a mechanism replacing the cosmological constant as the driver of late-time cosmic acceleration.",
    whyRetired:
      "No covariant action or dimensional derivation for ICBC was ever produced. BigBounce's own Einstein-Cartan-Holst (ECH) analysis independently closed four candidate dark-energy routes without invoking it.",
    evidence:
      "research/archaeology_2025/memos/DAUGHTER_UNIVERSE_MEMO.md §7 (Q15); arxiv/paper1bc_ech_note/main.tex",
    status: "closed",
  },
  {
    name: "Inevitable Omega Black Hole",
    claim:
      "All black holes in the universe inevitably merge over cosmic time into a single “Omega Black Hole,” treated as a required endpoint of cosmic evolution.",
    whyRetired:
      "False under an eternally accelerating, constant, positive cosmological constant: causally disconnected regions never merge, and no coalescence mechanism was ever derived for the claim.",
    evidence: "research/archaeology_2025/memos/COSMIC_FATE_MEMO.md §3(a), §8 (Branch A)",
    status: "retired",
  },
  {
    name: "Inherited galaxy-spin-axis dipole",
    claim:
      "A rotating parent black hole imprints a preferred spin axis on its daughter universe, observable today as a dipole in galaxy chirality or spin alignment.",
    whyRetired:
      "DESI Legacy DR8 (887,472 galaxies) gives a dipole consistent with zero. The 2026-09-02 exclusion shows the literature-claimed Popławski alignment amplitudes sit 2-30x above the observed sensitivity floor.",
    evidence:
      "research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py; pipelines/p2_chirality/chirality_catalog_paper.tex",
    status: "null",
  },
  {
    name: "M_crit = Λc²r³/3G as a universal collapse mass",
    claim:
      "A single critical mass within a cosmic radius was thought to trigger universal gravitational collapse once a region's mass exceeded it.",
    whyRetired:
      "Superseded, not falsified: rearranged, it is the established ΛCDM maximum-turnaround-radius relation for one bound structure (Pavlidou & Tomaras), not a global collapse test. Applied globally it only diagnoses deceleration, never recollapse.",
    evidence: "research/archaeology_2025/memos/COSMIC_FATE_MEMO.md §6, §9 (Q12)",
    status: "retired",
  },
  {
    name: "Central SMBH causes spiral galaxy morphology",
    claim:
      "A galaxy's central black hole determines whether it forms a spiral rather than an elliptical shape.",
    whyRetired:
      "Kormendy & Ho (2013) show the most massive supermassive black holes sit in giant ellipticals, not spirals. Morphology tracks angular momentum, gas fraction, merger history, and environment, not black-hole presence.",
    evidence: "research/archaeology_2025/memos/DAUGHTER_UNIVERSE_MEMO.md §6",
    status: "retired",
  },
  {
    name: "UMPBH as a required cosmic era",
    claim:
      "Ultra-massive primordial black holes (UMPBH) were treated as a mandatory intermediate era of cosmic evolution.",
    whyRetired:
      "No supporting derivation or observational requirement exists anywhere in the source material or the repo; the era was asserted, never derived.",
    evidence:
      "research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md (“Complete idea triage”); research/archaeology_2025/SOURCE_MAP.md",
    status: "retired",
  },
];

export const openQuestions: OpenQuestion[] = [
  {
    title: "Cosmic fate: can an accelerating universe recollapse?",
    question:
      "Given all current cosmological constraints, what physically complete classes of dark-energy models permit our currently accelerating universe to undergo a future turnaround, and what observable present-day signatures distinguish them?",
    ledgerItem: "#20",
    layer: "open-question",
    finding:
      "Constant positive Λ forbids any turnaround; only dark energy whose density crosses zero could permit one, and nothing measured requires or excludes it.",
  },
  {
    title: "Black-hole daughter universes: which causal structure?",
    question:
      "Which mathematically consistent black-hole interior models produce an expanding daughter cosmology, and which causal structure does “born in a black hole” actually denote — an Einstein–Rosen bridge, a black→white transition, a closed FLRW region behind the horizon, or a pinched-off false-vacuum bubble?",
    ledgerItem: "#21",
    layer: "open-question",
    finding:
      "Only a closed FLRW region behind the horizon matches “born in a black hole”; it is causally sealed, so no exterior signal exists.",
  },
  {
    title: "Parent–child bookkeeping: what does ‘more matter than the parent’ mean?",
    question:
      "Does a black-hole daughter universe contain “vastly more matter” than the parent's mass, in what invariant sense, and does Popławski's Einstein–Cartan particle-production amplification (arXiv:1410.3881) reproduce independently?",
    ledgerItem: "#22",
    layer: "open-question",
    finding:
      "15 of 26 reproduction steps hold exactly, 8 need unstated assumptions, 3 do not; no invariant parent-to-child amplification ratio exists.",
  },
];

export const disclaimer =
  "These early AI-assisted exploratory notes predate the project's current derivation, reproducibility and adversarial-review standards. They are preserved for provenance. Historical hypotheses are not current claims; several were subsequently retired, reformulated, or falsified.";

export const provenance: ProvenanceEntry[] = [
  {
    title: "Interior Black Hole Sponge Multiverse Theory — 3/20/25",
    role: "Giant master tree: Omega BH, M_crit, Crunch/Freeze, BHCP, UMPBHs. Preserved as historical source only.",
  },
  {
    title: "NEW BEST VERSION — White Hole Sponge Multiverse / ICBC",
    role: "Peak ICBC/QGBW/Omega synthesis. Archived, not revived.",
  },
  {
    title: "Born in a black hole",
    role: "Later ECSK/LQC/rotating-black-hole version — the strongest old scientific base, mined carefully.",
  },
  {
    title: "Refining ICBC / replacing dark energy",
    role: "β = l_P/L_cosmic² boundary-acceleration construction. Retired.",
  },
  {
    title: "Black Hole Sponge — Equations Part 1",
    role: "CTEF, ICBP, GGSC, BCR, WHCIF, SBA equations invented without derivation from an action, symmetry, EFT, or field equations. Raw archive only, zero present-day authority.",
  },
  {
    title: "Black Hole Sponge Cosmology — official outline",
    role: "The pivot document from white-hole framing to black-hole-interior framing. Historical genealogy record.",
  },
  {
    title: "Grok — Black Hole Inverted Cosmology",
    role: "Maximum AI overreach: invented parameters, equations, and citations. Not used as science.",
  },
  {
    title: "White Holes — book outline",
    role: "Big Freeze → black-hole era → Omega → rebirth narrative. Useful as history and philosophy only.",
  },
  {
    title: "Internal archive",
    role: "research/archaeology_2025/ — the 2026-09-18 campaign workspace holding the source map, verified bibliography, memos, and this ledger's supporting artifacts.",
  },
];
