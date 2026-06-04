#!/usr/bin/env node
/**
 * Seed Houston-approved novelty defaults for the 6 bigbounce papers.
 * Per convex/CONVEX_GAPS_2026-06-03.md proposed table:
 *   P1A=N3, P1B=N2, P2=N3, P3=N3, P4=N3, P5=N3
 *
 * Idempotent — papers:setNovelty patches the existing row.
 *
 * Per /never-claim-n4 standing directive, the Convex schema enum literally
 * rejects "N4" at the validator layer. Self-claim ceiling is N3.
 */
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient(
  process.env.CONVEX_URL || "https://brilliant-panther-471.convex.cloud"
);

const NOVELTY_DEFAULTS = [
  { slug: "paper-1a", novelty: "N3", note: "first-of-kind ECH no-go" },
  { slug: "paper-1b", novelty: "N2", note: "MCMC companion methodology" },
  { slug: "paper-2", novelty: "N3", note: "first f_NL forecast from this technique" },
  { slug: "paper-3", novelty: "N3", note: "first systematic multi-survey anomaly engine" },
  { slug: "paper-4", novelty: "N3", note: "largest galaxy chirality catalog to date" },
  { slug: "paper-5", novelty: "N3", note: "first end-to-end DESI environmental dependence test" },
];

for (const row of NOVELTY_DEFAULTS) {
  await client.mutation(api.papers.setNovelty, {
    slug: row.slug,
    novelty: row.novelty,
  });
  console.log(`✔ ${row.slug} → ${row.novelty} (${row.note})`);
}

// Verify
const states = await client.query(api.papers.listAllPaperStates);
console.log("\nPost-seed state:");
for (const p of states) {
  console.log(`  ${p.number.padEnd(4)} ${p.slug.padEnd(12)} novelty=${p.novelty ?? "null"}`);
}
const missing = states.filter((p) => !p.novelty);
if (missing.length > 0) {
  console.error(`\n✘ ${missing.length} papers missing novelty:`, missing.map((p) => p.slug));
  process.exit(1);
}
console.log(`\n✔ all ${states.length} papers have novelty populated`);
