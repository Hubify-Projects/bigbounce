#!/usr/bin/env node
/**
 * Build-time reproducibility-manifest snapshot.
 *
 * Reads reproducibility/manifests/{programs,experiments}/*.json (repo root —
 * canonical source of truth per directive Q2, reproducibility/manifests/SCHEMA.md)
 * and writes site/src/data/repro.ts as a fully-prerendered, typed snapshot so
 * the static export never depends on a path outside site/ at request time.
 *
 * Mirrors the extract-figures-from-convex.mjs pattern: generated file, do not
 * hand-edit. Regenerate with: cd site && node scripts/sync-repro-manifests.mjs
 *
 * If the manifests directory is missing (e.g. a trimmed deploy checkout), the
 * existing repro.ts is left untouched so builds don't fail.
 */
import { existsSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { resolve, dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const SITE = resolve(dirname(__filename), "..");
const REPO_ROOT = resolve(SITE, "..");
const MANIFESTS_ROOT = join(REPO_ROOT, "reproducibility", "manifests");
const PROGRAMS_DIR = join(MANIFESTS_ROOT, "programs");
const EXPERIMENTS_DIR = join(MANIFESTS_ROOT, "experiments");
const OUT = resolve(SITE, "src/data/repro.ts");

function readJsonDir(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .sort()
    .map((f) => JSON.parse(readFileSync(join(dir, f), "utf8")));
}

function main() {
  if (!existsSync(MANIFESTS_ROOT)) {
    console.warn(
      `[sync-repro-manifests] ${MANIFESTS_ROOT} not found; leaving existing repro.ts in place.`,
    );
    process.exit(0);
  }

  const programs = readJsonDir(PROGRAMS_DIR).sort((a, b) => a.id.localeCompare(b.id));
  const experiments = readJsonDir(EXPERIMENTS_DIR).sort((a, b) => a.id.localeCompare(b.id));

  const banner = `// AUTO-GENERATED from reproducibility/manifests/{programs,experiments}/*.json by
// site/scripts/sync-repro-manifests.mjs — do not edit by hand.
// Source of truth: reproducibility/manifests/ (directive Q2, repo CLAUDE.md;
// schema: reproducibility/manifests/SCHEMA.md).
// Regenerate this snapshot with: cd site && node scripts/sync-repro-manifests.mjs
`;

  const types = `
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
`;

  const body = `
export const reproPrograms: ReproProgram[] = ${JSON.stringify(programs, null, 2)};

export const reproExperiments: ReproExperiment[] = ${JSON.stringify(experiments, null, 2)};
`;

  writeFileSync(OUT, banner + types + body);
  console.log(
    `[sync-repro-manifests] wrote ${programs.length} programs + ${experiments.length} experiments to ${OUT.replace(SITE + "/", "")}`,
  );
}

main();
