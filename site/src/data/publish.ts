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
  lastUpdatedDisplay: "August 4, 2026",
  headline:
    "Publication follows three research programs, not a six-paper quota. Candidate-package readiness preserves evidence and packaging state; it does not establish a scientific flagship, journal acceptance, or a submission decision.",
  decisions: [
    {
      title: "DESI anomaly flagship",
      detail:
        "Rebuild the discovery paper only after the enhanced parent, model, score lineage, and selection reproducibility are restored or regenerated. Current P3 is technical provenance support.",
    },
    {
      title: "P3 role approved",
      detail:
        "The public-ID recovery is a citable supporting data release integrated with the rebuilt anomaly flagship, not a standalone ApJS submission.",
    },
    {
      title: "P5 role approved",
      detail:
        "The chirality–environment null test remains a standalone AJ companion because it asks a distinct environment-dependence question with its own joins and controlled null.",
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
    detail: "Six standalone works are the endpoint; P3 is an integrated supporting data release, not a seventh discovery paper.",
    rows: [
      { name: "P2 · bounce-theory lead", role: "Lead theory paper", status: "Selected standalone manuscript", destination: "Physical Review D", dependency: "Stated bounce-transmission and survey-covariance conditions", nextGate: "Houston visual approval, then independent review", href: "/papers/paper-2" },
      { name: "P1A · ECH boundary Note", role: "Focused theory Note", status: "Selected standalone manuscript", destination: "CQG Note", dependency: "Narrow algebraic scope and venue fit", nextGate: "Houston visual approval, then independent review", href: "/papers/paper-1a" },
      { name: "P1B · namaster-proof", role: "Research-software metapaper", status: "Selected standalone manuscript", destination: "JORS software paper", dependency: "Installable package and independent software review", nextGate: "Houston visual approval, then independent review", href: "/papers/paper-1b" },
      { name: "Rebuilt DESI anomaly flagship", role: "Discovery paper", status: "New work; rebuild in parallel", destination: "Venue chosen after reproducible result exists", dependency: "Immutable parent catalog, model, score/selection lineage, and candidate validation", nextGate: "Complete the fail-closed DESI rerun before drafting", href: "https://github.com/Hubify-Projects/bigbounce/blob/main/pipelines/p1_highz_tracers/clean_rerun_contract.md", external: true },
      { name: "P4 · chirality catalog", role: "Lead catalog/null-result paper", status: "Selected standalone manuscript", destination: "Astrophysical Journal Supplement Series", dependency: "Released labels, stated observed-label scope, and systematic boundary", nextGate: "Houston visual approval, then independent review", href: "/papers/paper-4" },
      { name: "P5 · chirality × environment", role: "Independent companion null test", status: "Selected standalone manuscript", destination: "Astronomical Journal", dependency: "Catalog-native joins and controlled environment null", nextGate: "Houston visual approval, then independent review", href: "/papers/paper-5" },
      { name: "P3 · DESI Public-ID Recovery", role: "Integrated supporting data release", status: "Citable provenance support", destination: "Bundle with rebuilt anomaly flagship", dependency: "Frozen historical list and transparent match-confidence split", nextGate: "Maintain versioned release; do not submit as a discovery paper", href: "/papers/paper-3" },
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
  selectedOrder: ["P2", "P1A", "P4", "P1B", "P5"],
  detail: "Review and submit the five selected manuscripts in this order. The clean DESI rerun proceeds in parallel; only a reproducible, scientifically validated result earns the rebuilt anomaly flagship its own submission.",
} as const;
