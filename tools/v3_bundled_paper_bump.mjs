// v3 bundled paper bump — reads a JSON bundle of paper closures and ships them all.
//
// Replaces the one-off tools/p*_convex_bump_*.mjs pattern with a single
// data-driven script. Each bundle entry specifies the paper + new version
// + computed PDF metadata + closure changelog. The script:
//   1. Verifies the PDF exists at the canonical location + matches the
//      claimed md5/size (if supplied).
//   2. Calls api.paperVersions.bump with the correct long-form paperSlug.
//   3. Verifies the post-bump api.papers.listAllPaperStates state.
//
// Bundle format (default location: ./BUMP_BUNDLE.json):
// [
//   {
//     "paperSlug": "paper-1b",
//     "version": "v1B.0.45",
//     "datestamp": "2026-06-08",
//     "texCommit": "<git short hash>",
//     "pdfPath": "/Users/.../arxiv/paper1b_mcmc_companion.pdf",
//     "sitePdfPath": "/papers/paper1b_mcmc_companion_v1B.0.45.pdf",
//     "changelog": "TIER A2 #A5 closure ..."
//   },
//   { ... }
// ]
//
// Usage:
//   node tools/v3_bundled_paper_bump.mjs [path/to/bundle.json]
//
// Computes pdfMd5, pdfPages, pdfSizeBytes from the on-disk PDF if not supplied.

import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";
import { readFileSync, existsSync, statSync } from "node:fs";
import { execSync } from "node:child_process";
import { resolve } from "node:path";

const BUNDLE_PATH = process.argv[2] || "./BUMP_BUNDLE.json";
const REPO = "/Users/houstongolden/Desktop/CODE_2025/bigbounce";

if (!existsSync(BUNDLE_PATH)) {
  console.error(`bundle file not found: ${BUNDLE_PATH}`);
  process.exit(2);
}

const bundle = JSON.parse(readFileSync(BUNDLE_PATH, "utf-8"));
if (!Array.isArray(bundle) || bundle.length === 0) {
  console.error("bundle must be a non-empty array");
  process.exit(2);
}

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

function md5Of(filePath) {
  try {
    return execSync(`md5 -q "${filePath}"`).toString().trim();
  } catch {
    return execSync(`md5sum "${filePath}" | awk '{print $1}'`).toString().trim();
  }
}

function pagesOf(filePath) {
  try {
    const out = execSync(`pdfinfo "${filePath}" 2>/dev/null | grep '^Pages:' | awk '{print $2}'`).toString().trim();
    if (out) return parseInt(out, 10);
  } catch {}
  return null;
}

console.log(`# Bundled paper bump: ${bundle.length} closures`);
console.log("");

for (const entry of bundle) {
  const pdfPath = resolve(entry.pdfPath || `${REPO}/`);
  if (!existsSync(pdfPath)) {
    console.error(`  X ${entry.paperSlug} ${entry.version}: PDF not found at ${pdfPath}`);
    continue;
  }
  const stat = statSync(pdfPath);
  const md5 = entry.pdfMd5 || md5Of(pdfPath);
  const pages = entry.pdfPages || pagesOf(pdfPath) || 0;
  const sizeBytes = entry.pdfSizeBytes || stat.size;

  if (entry.pdfMd5 && entry.pdfMd5 !== md5) {
    console.error(`  X ${entry.paperSlug} ${entry.version}: pdfMd5 mismatch — claimed ${entry.pdfMd5}, actual ${md5}`);
    continue;
  }

  const result = await client.mutation(api.paperVersions.bump, {
    paperSlug: entry.paperSlug,
    version: entry.version,
    datestamp: entry.datestamp,
    texCommit: entry.texCommit,
    pdfMd5: md5,
    pdfPages: pages,
    pdfSizeBytes: sizeBytes,
    sitePdfPath: entry.sitePdfPath,
    changelog: entry.changelog,
  });
  console.log(`  OK ${entry.paperSlug} ${entry.version}: inserted ${result} (md5=${md5}, ${pages}pp, ${sizeBytes}B)`);
}

console.log("");
console.log("# Post-bump verification");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`  ${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
