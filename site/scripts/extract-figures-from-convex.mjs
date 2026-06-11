#!/usr/bin/env node
/**
 * Build-time figures snapshot.
 *
 * Reads paper_figures from Convex (canonical source — seeded by
 * tools/seed_paper_figures.mjs from each paper's current .tex) and writes
 * site/src/data/figures.ts so the static export has a fully-prerendered
 * gallery even when Convex isn't reachable from the browser.
 *
 * If Convex is unreachable at build time, the existing figures.ts is
 * left untouched so builds don't fail in air-gapped environments.
 */
import { writeFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { ConvexHttpClient } from "convex/browser";

const __filename = fileURLToPath(import.meta.url);
const SITE = resolve(dirname(__filename), "..");
const OUT = resolve(SITE, "src/data/figures.ts");
const CONVEX_URL =
  process.env.CONVEX_URL ||
  process.env.NEXT_PUBLIC_CONVEX_URL ||
  "https://brilliant-panther-471.convex.cloud";

// Map paperSlug → section header rendered on /figures.
// Order is the canonical display order (P1A → P1B → P2 → P3 → P4 → P5).
const SECTION_ORDER = [
  { slug: "paper-1a", title: "Paper 1A — ECH Channel-Level Closure (4 Dark-Energy Routes)" },
  { slug: "paper-1b", title: "Paper 1B — Technical Verification Companion (MCMC + NaMaster)" },
  { slug: "paper-2",  title: "Paper 2 — Matter-Bounce f_NL SPHEREx Forecast" },
  { slug: "paper-3",  title: "Paper 3 — DESI Spectral Anomalies (Multi-Survey Catalog)" },
  { slug: "paper-4",  title: "Paper 4 — Galaxy Chirality Catalog (3.3M Spirals)" },
  { slug: "paper-5",  title: "Paper 5 — DESI Chirality × Cosmic-Web Environment" },
];

async function main() {
  const client = new ConvexHttpClient(CONVEX_URL);
  let grouped;
  try {
    grouped = await client.query("figures:listAll");
  } catch (err) {
    console.warn(
      `[extract-figures-from-convex] Convex unreachable (${err.message}); ` +
      `leaving existing figures.ts in place.`
    );
    process.exit(0);
  }

  const sections = [];
  let totalFigures = 0;
  for (const { slug, title } of SECTION_ORDER) {
    const rows = (grouped[slug] || []).slice().sort((a, b) => a.ordinal - b.ordinal);
    if (rows.length === 0) continue;
    const items = rows.map((r) => ({
      src: r.src,
      alt: r.alt,
      number: r.citationLabel
        ? `Figure ${r.ordinal} (${r.citationLabel})`
        : `Figure ${r.ordinal}`,
      title: r.title,
      desc: r.desc,
      source: `${title.split("—")[0].trim()} · ${r.paperVersion}`,
    }));
    sections.push({
      title,
      count: `${items.length} figure${items.length === 1 ? "" : "s"}`,
      items,
    });
    totalFigures += items.length;
  }

  const body =
    `// AUTO-GENERATED from Convex paper_figures by\n` +
    `// site/scripts/extract-figures-from-convex.mjs — do not edit by hand.\n` +
    `// Source of truth: each paper's current .tex \\includegraphics + \\caption.\n` +
    `// Re-seed Convex with: node tools/seed_paper_figures.mjs\n` +
    `// Regenerate this snapshot with: cd site && node scripts/extract-figures-from-convex.mjs\n` +
    `\n` +
    `export interface Figure {\n` +
    `  src: string;\n` +
    `  alt: string;\n` +
    `  number: string;\n` +
    `  title: string;\n` +
    `  desc: string;\n` +
    `  source: string;\n` +
    `}\n` +
    `\n` +
    `export interface FigureSection {\n` +
    `  title: string;\n` +
    `  count: string;\n` +
    `  items: Figure[];\n` +
    `}\n` +
    `\n` +
    `export const figureSections: FigureSection[] = ${JSON.stringify(sections, null, 2)};\n`;

  writeFileSync(OUT, body, "utf8");
  console.log(
    `[extract-figures-from-convex] wrote ${OUT} — ` +
    `${sections.length} sections, ${totalFigures} figures.`
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
