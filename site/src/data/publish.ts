export interface PublicationMapRow {
  name: string;
  role: string;
  status: string;
  destination: string;
  dependency: string;
  nextGate: string;
  href: string;
  external?: boolean;
}

export interface PublicationMapGroup {
  title: string;
  detail: string;
  rows: readonly PublicationMapRow[];
}

export const publicationArchitecture = {
  lastUpdatedDisplay: "September 2, 2026",
  headline:
    "Publication follows a flagship line + one closed-line note + data products (Track A/B/C), not the retired three-research-programs framing and not a paper-count quota. Candidate-package readiness preserves evidence and packaging state; it does not establish a scientific flagship, journal acceptance, or a submission decision.",
  decisions: [
    {
      title: "Track A — bounce vs. inflation (flagship)",
      detail:
        "A1 · P2′'s exact-amplitude theory (ledger #1 CLOSED) is now folded into A3 (paper-a3m, v3M.0.26), the flagship submission candidate combining the exact amplitude with multi-channel consistency checks (NANOGrav γ, PBH abundance, SPHEREx/MegaMapper). Ledger row 19 (D-A3-14) closed 2026-09-04, lifting the R2 rounds-stop; R9 closed 3 MAJOR + 1 MAJOR-lite + 20 minor/nit → v3M.0.25, then an R10 confirmation board did NOT confirm — 17 further genuinely-new-real findings (4 MAJOR) closed → v3M.0.26 (Table V's f_PBH columns re-evaluated at their own labels, the DBI window minimum corrected AGAINST the paper). Directive R2 budget SPENT (R9+R10) — rounds STOPPED, readiness 75 COMPUTED, a scope decision is required before any further board. A2 (transmission through an explicit bounce) remains a research brief in progress.",
    },
    {
      title: "Track B — the ECH Note (closed line)",
      detail:
        "P1A merged into P1C as one ≤12 pp gr-qc/CQG Note (P1N, v1N.0.1): what minimal Einstein–Cartan torsion does for the bounce (Popławski's spin-spin repulsion mechanism) and cannot do for dark energy. P1A and P1C stay listed as P1N's archived lineage, frozen on disk, not separate submission targets.",
    },
    {
      title: "Track C — DESI data products (on-vision)",
      detail:
        "P5 folded into P4 as P4′ (v4P.0.9): the largest test of the rotating-black-hole-universe galaxy-spin-axis prediction, excluding literature alignment amplitudes by 2–20×. The anomaly line (P3) is redirected to an early-universe anomaly map, now a registered first full draft (paper-af, vAF.0.3): a 1,244-object DESI DR1 anomaly-score catalogue reported as a validated data release, not a discovery (ledger #8 condition NOT met); namaster-proof (P1B) is an optional software note.",
    },
  ],
} as const;

/**
 * The public publishing map deliberately separates scientific manuscripts from
 * the data, trained models, and software that make them inspectable. Links are
 * the existing public artifacts or their canonical in-site record.
 */
export const publicationMap: readonly PublicationMapGroup[] = [
  {
    title: "Manuscripts and releases",
    detail: "P1N and P4′ are the current submission targets for Tracks B and C1; P1A/P1C/P4/P5 remain listed as their archived lineage, never deleted. P3 is an integrated supporting/provenance release, not a standalone discovery paper.",
    rows: [
      { name: "A3 · Track A flagship multi-channel paper", role: "Flagship submission candidate (A3 skeleton + P2′ theory folded in)", status: "v3M.0.26 — R10 confirmation board did NOT confirm: 17 genuinely-new-real findings (4 MAJOR) closed, incl. Table V's f_PBH columns mis-evaluated at their own row labels and the DBI window minimum corrected AGAINST the paper (r_min 10.3, 286x BICEP/Keck). No physics error found. Directive R2 budget SPENT (R9+R10) — rounds STOPPED, readiness 75 COMPUTED, a scope decision is required before any further board", destination: "Physical Review D (regular article)", dependency: "Houston final author review and sign-off for readiness 100", nextGate: "Houston visual approval + independent review, then submission", href: "/papers/paper-a3m" },
      { name: "P2′ · Track A1 flagship Letter", role: "Archived theory record", status: "Archived (v2L.0.2) — R1 truth-audited, scope decision: folded into A3", destination: "Content carried forward inside the A3 multi-channel paper", dependency: "—", nextGate: "None — not an independent submission target", href: "/papers/paper-2l" },
      { name: "P1N · Track B ECH Note", role: "Closed-line theory Note (P1A + P1C merged)", status: "v1N.0.6 — D-round + P-round complete 2026-09-18 (arXiv tarball rebuilt + standalone-smoke-tested, CQG submission kit assembled), readiness 99", destination: "Classical and Quantum Gravity — Paper", dependency: "Houston sign-off for readiness 100; arXiv endorsement + submission", nextGate: "Houston visual approval + independent review, then submission", href: "/papers/paper-1n" },
      { name: "P1B · namaster-proof", role: "Research-software metapaper", status: "Selected standalone manuscript — v2B.0.23: all deferred text items from the R3 audit closed (batch-3 audit trail, rule-file digests, Table 1 trust category); rounds stopped under R2, venue decision (ACM REP) next", destination: "ACM REP (measurement) + JORS/JOSS software companion", dependency: "Venue decision and independent software review", nextGate: "Houston venue decision, then independent review", href: "/papers/paper-1b" },
      { name: "P4′ · Track C1 chirality test", role: "Lead catalog/null-result paper (P4 + P5 folded)", status: "v4P.0.8 — exact-version INT confirmation board closed 7 genuinely-new-real MAJOR + 12 MINOR on the post-R3 disclosure content 2026-09-18, readiness 95; re-verification board in progress", destination: "Astrophysical Journal Supplement Series", dependency: "Houston sign-off for readiness 100; arXiv endorsement + submission", nextGate: "Houston visual approval + independent review, then submission", href: "/papers/paper-4p" },
      { name: "Paper-af · Track C2 anomaly-score catalogue", role: "Data-release paper (Track C2)", status: "vAF.0.3 (2026-09-19) — registered in Convex; ADS bibliography verification + real acknowledgements section closed. 15pp, 9 figures, 11 tables, every number sourced from a committed artifact; corrected science-target parent (21,793,550 unique TARGETIDs, not 27,547,223 all-fibre), executed FT-A Lyman-break follow-up test (refutes 1 candidate, supports 1, 2 undecidable on schema gap); ledger #8 framing held (data release, pre-declared discovery condition NOT met). Readiness 60 COMPUTED. R1 INT board dispatched (Claude-opus leg running; Grok/Gemini API legs pending)", destination: "Venue chosen after a bounce-vs-inflation discriminator is earned per candidate channel", dependency: "R1 INT board closure on the vAF.0.3 draft", nextGate: "Close the R1 board findings", href: "/papers/paper-af" },
      { name: "P3 · DESI Public-ID Recovery", role: "Provenance support for the anomaly map (Track C2)", status: "Citable provenance support", destination: "Bundle with the redirected anomaly map", dependency: "Frozen historical list and transparent match-confidence split", nextGate: "Maintain versioned release; do not submit as a discovery paper", href: "/papers/paper-3" },
      { name: "P1A · archived into P1N", role: "Superseded theory Note", status: "Archived lineage — frozen on disk", destination: "See P1N", dependency: "—", nextGate: "None — not an independent submission target", href: "/papers/paper-1a" },
      { name: "P4 · archived into P4′", role: "Superseded catalog paper", status: "Archived lineage — frozen on disk", destination: "See P4′", dependency: "—", nextGate: "None — not an independent submission target", href: "/papers/paper-4" },
      { name: "P5 · archived into P4′", role: "Superseded companion null test", status: "Archived lineage — frozen on disk", destination: "See P4′", dependency: "—", nextGate: "None — not an independent submission target", href: "/papers/paper-5" },
    ],
  },
  {
    title: "Data products",
    detail: "Catalogs are reusable research outputs. They support papers but are not themselves evidence for a bounce.",
    rows: [
      { name: "DESI Public-ID recovery dataset", role: "Historical-list provenance dataset", status: "Released supporting data", destination: "Integrated with rebuilt anomaly flagship", dependency: "P3’s frozen-list provenance", nextGate: "Keep match-confidence and scope labels with every reuse", href: "https://doi.org/10.5281/zenodo.21461888", external: true },
      { name: "8.47M galaxy chirality catalog", role: "Observed-label catalog", status: "Released research dataset", destination: "P4 lead paper and P5 companion", dependency: "Classifier/systematics documentation", nextGate: "Archive final paper-linked snapshot after approval", href: "https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog", external: true },
    ],
  },
  {
    title: "Models and checkpoints",
    detail: "Models are implementation artifacts, not independent scientific claims.",
    rows: [
      { name: "DESI spectral anomaly detector", role: "Historical exploratory checkpoint", status: "Legacy/superseded for flagship science", destination: "Provenance record only", dependency: "Rebuilt flagship requires a hash-bound replacement", nextGate: "Do not use for new discovery claims; regenerate under the rerun contract", href: "https://huggingface.co/bamfai/desi-spectral-anomaly-detector", external: true },
      { name: "Galaxy chirality v2", role: "Parity-equivariant classifier checkpoint", status: "Released reusable model", destination: "P4/P5 reproducibility support", dependency: "Catalog’s observed-label and morphology-transfer boundary", nextGate: "Freeze the paper-linked model snapshot with final catalog release", href: "https://huggingface.co/bamfai/galaxy-chirality-v2", external: true },
    ],
  },
  {
    title: "Software and code",
    detail: "Code makes results inspectable; only P1B is a software paper in its own right.",
    rows: [
      { name: "namaster-proof", role: "Exact-window verification software", status: "Released; P1B’s subject", destination: "JORS metapaper and reusable package", dependency: "Independent software review and release metadata", nextGate: "Houston approval, then independent software review", href: "/papers/paper-1b" },
      { name: "Clean DESI rerun pipeline", role: "Reproducibility infrastructure", status: "Active rebuild", destination: "Evidence backbone for anomaly flagship", dependency: "Sealed inputs, model/scaler hashes, shard receipts, deterministic selection", nextGate: "Execute and validate clean rerun", href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p1_highz_tracers/clean_rerun_contract.md", external: true },
    ],
  },
] as const;

export const publicationExecution = {
  selectedOrder: ["P4′", "P1N", "P2′", "P1B"],
  detail: "P4′ (condensed, model-tested null) and the P1N ECH Note are the fastest honest candidates; P2′ follows once ledger #1's independent re-derivation closes. The redirected early-universe anomaly map proceeds in parallel; only an earned, scientifically validated result draws its own submission. P1A, P4, and P5 remain archived lineage, not separate submissions.",
} as const;
