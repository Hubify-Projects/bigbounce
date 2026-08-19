#!/usr/bin/env node

import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { execFileSync } from "node:child_process";
import { dirname, resolve } from "node:path";
import process from "node:process";
import YAML from "yaml";

export const DEFAULT_MANIFEST = "project-context/hubify-lab/lab.yaml";
export const DEFAULT_SITE_METADATA = "site/src/data/papers.ts";
const EXPECTED_IDS = ["p1a", "p1b", "p2", "p3", "p4", "p5"];

function parseSitePapers(text) {
  const records = new Map();
  const objectPattern = /^  \{\n    slug: "(paper-[^"]+)"([\s\S]*?)^  \},\n(?=  \{|\];)/gm;
  for (const match of text.matchAll(objectPattern)) {
    const [, slug, body] = match;
    const version = body.match(/\n    version: "([^"]+)"/u)?.[1];
    const pdf = body.match(/href: "(\/papers\/[^"\n]+\.pdf)"/u)?.[1];
    if (version && pdf) records.set(slug, { version, pdf });
  }
  return records;
}

function requireString(value, field) {
  if (typeof value !== "string" || !value.trim()) throw new Error(`${field} must be a non-empty string`);
  return value.trim();
}

export async function checkManifest({ manifestPath = DEFAULT_MANIFEST, siteMetadataPath = DEFAULT_SITE_METADATA, repoRoot = process.cwd() } = {}) {
  const manifest = YAML.parse(await readFile(resolve(repoRoot, manifestPath), "utf8"));
  const siteText = await readFile(resolve(repoRoot, siteMetadataPath), "utf8");
  const site = parseSitePapers(siteText);
  const programs = manifest?.programs;
  if (!Array.isArray(programs)) throw new Error("manifest programs must be an array");
  const ids = programs.map((program) => requireString(program?.id, "program.id")).sort();
  if (JSON.stringify(ids) !== JSON.stringify(EXPECTED_IDS)) throw new Error(`manifest program IDs must be ${EXPECTED_IDS.join(", ")}; got ${ids.join(", ")}`);
  const snapshot = requireString(manifest?.source?.science_snapshot_commit, "source.science_snapshot_commit");
  if (!/^[0-9a-f]{40}$/u.test(snapshot)) throw new Error("source.science_snapshot_commit must be a full 40-character SHA-1");
  if (manifest.source.current_commit !== snapshot) throw new Error("source.current_commit must equal science_snapshot_commit; do not silently claim docs-only HEAD");
  try { execFileSync("git", ["cat-file", "-e", `${snapshot}^{commit}`], { cwd: repoRoot, stdio: "ignore" }); }
  catch { throw new Error(`science snapshot commit is not present in this checkout: ${snapshot}`); }

  const diffs = [];
  for (const program of programs) {
    const id = program.id.toLowerCase();
    const siteRecord = site.get(`paper-${id.slice(1)}`);
    if (!siteRecord) { diffs.push(`${id}: missing from ${siteMetadataPath}`); continue; }
    if (program.version !== siteRecord.version) diffs.push(`${id}: manifest version ${program.version} != site ${siteRecord.version}`);
    const expectedPdf = `/${String(program.paper_pdf).replace(/^site\/public\//u, "")}`;
    if (expectedPdf !== siteRecord.pdf) diffs.push(`${id}: manifest PDF ${expectedPdf} != site ${siteRecord.pdf}`);
    const relativePath = String(program.paper_pdf).replace(/^site\/public\//u, "");
    const absolutePath = resolve(repoRoot, "site/public", relativePath);
    const actualHash = createHash("sha256").update(await readFile(absolutePath)).digest("hex");
    if (!/^[a-f0-9]{64}$/u.test(String(program.paper_sha256 ?? ""))) diffs.push(`${id}: paper_sha256 is missing or malformed`);
    else if (actualHash !== program.paper_sha256) diffs.push(`${id}: manifest hash ${program.paper_sha256} != file ${actualHash}`);
  }
  if (diffs.length) throw new Error(`Hubify lab manifest drift:\n${diffs.map((diff) => `- ${diff}`).join("\n")}`);
  return { ok: true, manifestPath, siteMetadataPath, scienceSnapshotCommit: snapshot, programs: programs.length };
}

async function main() {
  const args = process.argv.slice(2);
  const options = {};
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    const [flag, inline] = arg.split("=", 2);
    if (flag === "--manifest" || flag === "--site-metadata") {
      const value = inline ?? args[++index];
      if (!value) throw new Error(`${flag} requires a value`);
      options[flag === "--manifest" ? "manifestPath" : "siteMetadataPath"] = value;
    } else if (flag === "--help" || flag === "-h") {
      process.stdout.write("Usage: node scripts/check-hubify-lab-manifest.mjs [--manifest PATH] [--site-metadata PATH]\n");
      return;
    } else throw new Error(`unknown argument: ${arg}`);
  }
  process.stdout.write(`${JSON.stringify(await checkManifest(options), null, 2)}\n`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  try { await main(); } catch (error) { process.stderr.write(`${error instanceof Error ? error.message : String(error)}\n`); process.exitCode = 2; }
}
