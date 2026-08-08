/**
 * H17 Grok RE-TEST harvest → Convex.
 * Records the 5 Grok retest verdicts (post-H17-closure re-test, Grok-only leg;
 * ChatGPT retest submitted-but-unharvested, Gemini H17 FAILED upload-throttle)
 * and re-caps readiness to the honest best-known board.
 *
 * Retest movement vs H17 initial Grok:
 *   P2  MAJOR → MINOR  (improved)
 *   P4  MINOR → MAJOR  (referee variance / regressed)
 *   P1U MAJOR → MAJOR, P3 MAJOR → MAJOR, P5 MINOR → MINOR (unchanged)
 *
 * Readiness formula (same as H17 board): 50 base + per-EXT-reviewer pts
 *   ACCEPT +16 · MINOR +12 · MAJOR +6 · REJECT/FAILED/pending 0
 *   ChatGPT carry = REJECT (0) · Gemini carry = P5 MAJOR (+6), else 0.
 */
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient(
  process.env.CONVEX_URL || "https://brilliant-panther-471.convex.cloud"
);

const DATE = "2026-07-10";
const PR =
  "https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/EXT_real/H17_2026-07-10/retest";

// Per-paper Grok retest verdict (verbatim verdict WORD → recommendation enum;
// embedded [MAJOR]-tagged items counted in majorCount with a note).
const RETEST = [
  {
    slug: "paper-1a", code: "P1U", rec: "major-revisions", major: 3, minor: 2,
    note: "Grok MAJOR REVISIONS (unchanged vs H17). 3 MAJOR: amplitude/naturalness closure = single-scale NDA power-counting reframe of the CC problem (relocates not resolves); Sec X perturbation-transparency all-orders torsion-vanishing shown only at sketch level in main text; Sec IV/App C scope hedging ('channel-level not operator-level') in tension with the exhaustiveness claim. 2 MINOR: 14-barrier catalog organizational overhead; dense prose/self-cross-citation.",
  },
  {
    slug: "paper-2", code: "P2", rec: "minor-revisions", major: 1, minor: 4,
    note: "Grok MINOR REVISIONS (IMPROVED from H17 MAJOR). Verdict word = MINOR; 1 [MAJOR]-tagged item retained: SPHEREx headline 1.3-2.75sigma range is a heuristic envelope (imported Heinrich sigma≈0.7 rescaled by r=0.84) — full bounce-template covariance never recomputed (compute-gated: recompute-r). 4 MINOR: per-vertex squeezed-limit contributions not tabulated in main text; assumption-(d) cubic integrals only scaling-bounded not numerically evaluated; null-space basis/measure conventionality; Bayes-factor prior-convolution table not consolidated.",
  },
  {
    slug: "paper-3", code: "P3", rec: "major-revisions", major: 3, minor: 3,
    note: "Grok MAJOR REVISIONS (unchanged vs H17). 3 MAJOR: 268,519 headline vs 2,468 science-target yield mismatch (~98.7% sky/filler fibers); eROSITA production score axis irreproducible (excised but exists); LAMOST 5.8%/eROSITA 1.2% injection-recovery gate FAIL + DESI validation rests on short-trained proxy folds that fail the val-loss retain gate. 3 MINOR: Gaia synthetic-placeholder ingestion (excised); abstract structure/null secondary demos; SDSS continuity-slice vs native-threshold column.",
  },
  {
    slug: "paper-4", code: "P4", rec: "major-revisions", major: 3, minor: 2,
    note: "Grok MAJOR REVISIONS (regressed from H17 MINOR — referee variance, pattern-066; the 3 'MAJOR' items are the already-disclosed template-diagnostic + 47% remainder + pseudo-label items). 3 MAJOR: z≈−7.6 template-disfavor phrasing vs the +0.41sigma real-space primary null; Sec IV D monopole-leakage generative null reproduces only ≈53% of the ℓ=1 residual (~47% remainder unclosed, App D unreproduced); 66.5% CE-ResNet pseudo-labels with GZ1-human cross-check ~4.5× coarser. 2 MINOR: p_eq>0.6 cut-at-threshold justification; sigma/z proliferation across null procedures.",
  },
  {
    slug: "paper-5", code: "P5", rec: "minor-revisions", major: 1, minor: 4,
    note: "Grok MINOR REVISIONS (unchanged vs H17). Verdict word = MINOR; 1 [MAJOR]-tagged item: post-hoc designation of the DESIVAST-anchored primary estimand without a timestamped pre-registration (family-wise Bonferroni-5 null holds across all 5). 4 MINOR: de-attenuated 2.26pp bound omits environment-dependent relabeling uncertainty; 0.9pp quadrature-envelope covariance not justified; companion-Paper-IV cross-dependency (not standalone); fixed redshift-space RSD not quantified on void membership.",
  },
];

// Honest readiness caps (best-known board incl. Grok retest delta).
const CAPS = {
  "paper-1a": 56, "paper-1b": 56, "paper-2": 62,
  "paper-3": 56, "paper-4": 56, "paper-5": 68,
};

let pushed = 0;
for (const r of RETEST) {
  await client.mutation(api.externalReviews.upsertByLabelDate, {
    paperSlug: r.slug,
    source: "internal-stage3",
    reviewerLabel: "External · H17-retest Grok (grok)",
    receivedAt: DATE,
    blockerCount: 0,
    majorCount: r.major,
    minorCount: r.minor,
    recommendation: r.rec,
    pdfUrl: `${PR}/${r.code}_grok_retest.md`,
    notes: r.note,
  });
  pushed++;
  console.log(`  ✔ ${r.code.padEnd(4)} ${r.rec.padEnd(16)} (M${r.major}/m${r.minor})`);
}

console.log(`\n✔ ${pushed} Grok-retest rows upserted. Re-capping readiness:`);
for (const [slug, cap] of Object.entries(CAPS)) {
  await client.mutation(api.papers.setReadinessCap, { slug, cap });
  console.log(`  ✔ ${slug.padEnd(12)} cap=${cap}`);
}
console.log("\nDone.");
