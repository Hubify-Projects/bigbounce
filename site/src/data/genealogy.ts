// Provisional content — refined by the W6 legacy-hypothesis ledger; do not
// treat as a result.
//
// Source: research/archaeology_2025/ (2026-09-18 legacy-archaeology campaign).
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
      "The intuition that gravitational collapse might terminate in a nonsingular new expanding spacetime, rather than the specific mechanisms proposed.",
  },
  {
    period: "Mar 25–27, 2025",
    title: "Black Hole Sponge pivot",
    explored:
      "A reframing away from a literal “white-hole universe” toward our universe as the interior, or daughter, of a parent black hole.",
    survived:
      "A stronger conceptual direction with much less dependence on literal white holes — the parent→daughter framing that later became scientifically tractable.",
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
      "The Inverse/Inverted Cosmic Boundary Curvature (ICBC) mechanism was proposed as a replacement for dark energy driving late-time cosmic acceleration.",
    whyRetired:
      "The program's own ECH derivation systematically closed candidate late-time dark-energy routes — the current answer is “no” for this class of mechanism, not a re-opening of it.",
    evidence: "arxiv/paper1bc_ech_note",
    status: "closed",
  },
  {
    name: "Inevitable Omega Black Hole",
    claim:
      "All black holes inevitably merge over cosmic time into a single “Omega Black Hole,” treated as a required endpoint of cosmic evolution.",
    whyRetired:
      "False under an eternally accelerating Λ (cosmological-constant) universe: with a positive, constant Λ, causally disconnected regions never merge, and no mechanism was ever derived for universal black-hole coalescence.",
    evidence:
      "research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md §“Complete idea triage”",
    status: "retired",
  },
  {
    name: "Inherited galaxy-spin alignment",
    claim:
      "A rotating parent black hole would imprint a preferred spin axis on its daughter universe, observable today as a dipole in galaxy chirality or spin alignment.",
    whyRetired:
      "Null on two independent tests: P4's DESI Legacy DR8 survey of 887,472 spiral galaxies found a dipole consistent with zero, P5's environment channel is null, and the Popławski rotating-parent amplitude was excluded against the DESI A95 upper limit on 2026-09-02.",
    evidence: "research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py",
    status: "null",
  },
  {
    name: "M_crit = Λc²r³/3G as a universal collapse mass",
    claim:
      "A single critical mass M_crit = Λc²r³/(3G) within a cosmic radius was proposed as the threshold at which enough matter would overcome dark energy and trigger universal gravitational collapse.",
    whyRetired:
      "Superseded by reidentification: rearranged as r = (3GM/Λc²)^{1/3}, this is the established ΛCDM maximum-turnaround-radius relation for a single bound structure (Pavlidou & Tomaras), not a universal collapse criterion. The historical interpretation was too sweeping; the physics hiding inside it was real.",
    evidence: "research/archaeology_2025/memos/COSMIC_FATE_MEMO.md",
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
  },
  {
    title: "Black-hole daughter universes: which causal structure?",
    question:
      "Which mathematically consistent black-hole interior models produce an expanding daughter cosmology, and which causal structure does “born in a black hole” actually denote — an Einstein–Rosen bridge, a black→white transition, a closed FLRW region behind the horizon, or a pinched-off false-vacuum bubble?",
    ledgerItem: "#21",
    layer: "open-question",
  },
  {
    title: "Parent–child bookkeeping: what does ‘more matter than the parent’ mean?",
    question:
      "Does a black-hole daughter universe contain “vastly more matter” than the parent's mass, in what invariant sense, and does Popławski's Einstein–Cartan particle-production amplification (arXiv:1410.3881) reproduce independently?",
    ledgerItem: "#22",
    layer: "open-question",
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
