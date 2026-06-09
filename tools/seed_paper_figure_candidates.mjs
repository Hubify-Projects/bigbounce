#!/usr/bin/env node
/**
 * Seed `paper_figures` rows with status="candidate" from the
 * project-context/figure-candidates.json manifest.
 *
 * Complements tools/seed_paper_figures.mjs which seeds status="in-paper"
 * by parsing each paper's current .tex \includegraphics blocks.
 *
 * Candidates are figures that exist on disk + are scientifically valid
 * (not retracted) but are NOT yet \includegraphics-ed in the .tex.
 * Houston uses these on the paper detail page gallery to pick which
 * to re-add.
 *
 * Idempotent — re-running upserts by (paperSlug, ordinal). Candidate
 * ordinals start at 100 to avoid colliding with in-paper figures (1..N).
 *
 * Usage:  node tools/seed_paper_figure_candidates.mjs
 */
import { readFileSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const REPO = resolve(__dirname, "..");

function loadEnv() {
  const path = resolve(REPO, ".env.local");
  if (!existsSync(path)) return {};
  const out = {};
  for (const line of readFileSync(path, "utf8").split("\n")) {
    const m = line.match(/^([A-Z_][A-Z0-9_]*)=(.*)$/);
    if (m) out[m[1]] = m[2].trim();
  }
  return out;
}

async function main() {
  const env = loadEnv();
  const url =
    process.env.NEXT_PUBLIC_CONVEX_URL ||
    env.NEXT_PUBLIC_CONVEX_URL ||
    env.CONVEX_URL;
  if (!url) {
    console.error("No NEXT_PUBLIC_CONVEX_URL in env or .env.local — abort");
    process.exit(1);
  }

  const manifestPath = resolve(
    REPO,
    "project-context/figure-candidates.json",
  );
  const manifest = JSON.parse(readFileSync(manifestPath, "utf8"));

  const client = new ConvexHttpClient(url);

  // Read current live papers so we can stamp candidate rows with the
  // current paperVersion (display-only — candidates are not version-locked
  // the way in-paper figures are).
  let liveVersions = {};
  try {
    const live = await client.query(api.papers.listAllPaperStates);
    for (const p of live || []) liveVersions[p.slug] = p.currentVersion || "live";
  } catch (e) {
    console.warn("[candidates] could not read live paper versions:", e.message);
  }

  let total = 0;
  for (const [slug, candidates] of Object.entries(manifest.candidates)) {
    const version = liveVersions[slug] || "candidate-pool";
    console.log(`\n${slug} (${version}): ${candidates.length} candidates`);
    for (const c of candidates) {
      // Sanity: confirm the asset exists under site/public.
      const assetPath = resolve(
        REPO,
        "site/public" + c.src,
      );
      if (!existsSync(assetPath)) {
        console.warn(`  SKIP #${c.ordinal} ${c.title} — missing asset ${c.src}`);
        continue;
      }
      try {
        await client.mutation(api.figures.upsertByOrdinal, {
          paperSlug: slug,
          ordinal: c.ordinal,
          src: c.src,
          alt: c.alt,
          title: c.title,
          desc: c.desc,
          paperVersion: version,
          status: "candidate",
        });
        console.log(`  OK   #${c.ordinal} ${c.title}`);
        total++;
      } catch (e) {
        console.error(`  FAIL #${c.ordinal} ${c.title}: ${e.message}`);
      }
    }
  }

  console.log(`\nSeeded ${total} candidate figures across ${Object.keys(manifest.candidates).length} papers.`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
