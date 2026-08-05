// Derived helpers over the auto-generated reproducibility-manifest snapshot
// (src/data/repro.ts). Hand-maintained — unlike repro.ts this file is never
// regenerated, so DAG/rollup logic lives here rather than in the generator.
import {
  reproPrograms,
  reproExperiments,
  type ReproProgram,
  type ReproExperiment,
} from "@/data/repro";

const experimentById = new Map(reproExperiments.map((e) => [e.id, e]));

/** Maps a manifest `paper` code (e.g. "P1A", "P3-support") to the Paper.slug
 * used by /papers/[slug]. Returns null for codes with no standalone paper
 * page yet (e.g. "anomaly-flagship", "none"). */
const PAPER_CODE_TO_SLUG: Record<string, string> = {
  P1A: "paper-1a",
  P1B: "paper-1b",
  P2: "paper-2",
  "P3-support": "paper-3",
  P4: "paper-4",
  P5: "paper-5",
};

export function paperSlugForCode(code: string): string | null {
  return PAPER_CODE_TO_SLUG[code] ?? null;
}

/** Experiment manifests for a program, in the DAG order given by the
 * program manifest's own `experiments[]` array (already a valid topological
 * order per reproducibility/manifests/SCHEMA.md). Entries whose id has no
 * matching experiment manifest are skipped defensively. */
export function programExperimentsInDagOrder(program: ReproProgram): Array<{
  entry: { id: string; depends_on: string[] };
  experiment: ReproExperiment;
}> {
  return program.experiments
    .map((entry) => {
      const experiment = experimentById.get(entry.id);
      return experiment ? { entry, experiment } : null;
    })
    .filter((x): x is { entry: { id: string; depends_on: string[] }; experiment: ReproExperiment } => x !== null);
}

export interface ProgramRollup {
  totalExperiments: number;
  runnableNow: number;
  needsDataRestore: number;
  superseded: number;
  estCostUsd: number;
  estWallClock: string;
}

export function programRollup(program: ReproProgram): ProgramRollup {
  const rows = programExperimentsInDagOrder(program);
  return {
    totalExperiments: rows.length,
    runnableNow: rows.filter((r) => r.experiment.status === "runnable-now").length,
    needsDataRestore: rows.filter((r) => r.experiment.status === "needs-data-restore").length,
    superseded: rows.filter((r) => r.experiment.status === "superseded").length,
    estCostUsd: program.full_reproduction.est_cost_usd,
    estWallClock: program.full_reproduction.est_wall_clock,
  };
}

export interface LabRollup {
  totalPrograms: number;
  totalExperiments: number;
  runnableNow: number;
  needsDataRestore: number;
  superseded: number;
  totalEstCostUsd: number;
}

export function labRollup(): LabRollup {
  const programs = reproPrograms;
  const perProgram = programs.map(programRollup);
  return {
    totalPrograms: programs.length,
    totalExperiments: perProgram.reduce((a, p) => a + p.totalExperiments, 0),
    runnableNow: perProgram.reduce((a, p) => a + p.runnableNow, 0),
    needsDataRestore: perProgram.reduce((a, p) => a + p.needsDataRestore, 0),
    superseded: perProgram.reduce((a, p) => a + p.superseded, 0),
    totalEstCostUsd: perProgram.reduce((a, p) => a + p.estCostUsd, 0),
  };
}

/** Renders an est_cost_usd value per directive: $0 reads as "free (local)". */
export function formatCost(usd: number): string {
  if (usd === 0) return "free (local)";
  return `$${usd % 1 === 0 ? usd.toFixed(0) : usd.toFixed(2)}`;
}

export const STATUS_LABEL: Record<ReproExperiment["status"], string> = {
  "runnable-now": "runnable now",
  "needs-data-restore": "needs data restore",
  superseded: "superseded",
};
