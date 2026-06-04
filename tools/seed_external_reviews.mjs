#!/usr/bin/env node
/**
 * Seed `papers_externalReviews` from project-context/peer-reviews/
 * historical record. Round-level rollup only — per-finding rows live in
 * the `findings` table.
 *
 * Two input sources:
 *   1. project-context/peer-reviews/external/*.md
 *      → source = "houston-paste" (Houston pasted GPT/Gemini/Grok output)
 *   2. project-context/peer-reviews/findings-archive/*.json
 *      → source = "internal-stage3" (multi-vendor synthesis rollup)
 *
 * Counts (blocker/major/minor) = post-truth-audit VERIFIED counts. Where a
 * round's audit verdict isn't recorded, we fall back to raw classification
 * counts and note that in `notes`.
 *
 * Idempotent — uses externalReviews:upsertByLabelDate so re-runs replace
 * the same (paperSlug, reviewerLabel, receivedAt) tuple rather than
 * appending duplicates.
 */
import fs from "node:fs";
import path from "node:path";
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient(
  process.env.CONVEX_URL || "https://brilliant-panther-471.convex.cloud"
);

const REPO_ROOT = "/Users/houstongolden/Desktop/CODE_2025/bigbounce";
const ARCHIVE_DIR = path.join(REPO_ROOT, "project-context/peer-reviews/findings-archive");
const EXTERNAL_DIR = path.join(REPO_ROOT, "project-context/peer-reviews/external");

// Map paper-letter code → Convex slug
const SLUG_MAP = {
  P1A: "paper-1a",
  P1B: "paper-1b",
  P2: "paper-2",
  P3: "paper-3",
  P4: "paper-4",
  P5: "paper-5",
};

function countByVerdict(reviewers, classification) {
  // Count VERIFIED findings of the given classification across all reviewers
  // in the round. Treats "minor"/"MINOR" case-insensitively.
  let count = 0;
  for (const findings of Object.values(reviewers ?? {})) {
    if (!Array.isArray(findings)) continue;
    for (const f of findings) {
      const cls = (f.raw_classification ?? "").toUpperCase();
      if (cls !== classification) continue;
      const verdict = (f.truth_audit_verdict ?? "").toUpperCase();
      // VERIFIED counts; PARTIAL VERIFIED counts; everything else (STALE,
      // FALSIFIED, OPINION, OUT-OF-SCOPE) does not count toward verified
      // severity.
      if (verdict.includes("VERIFIED")) count++;
    }
  }
  return count;
}

function countByRawClassification(reviewers, classification) {
  let count = 0;
  for (const findings of Object.values(reviewers ?? {})) {
    if (!Array.isArray(findings)) continue;
    for (const f of findings) {
      const cls = (f.raw_classification ?? "").toUpperCase();
      if (cls === classification) count++;
    }
  }
  return count;
}

const rows = [];

// ── findings-archive/*.json (per-round internal-stage3 rollups) ──────
const archiveFiles = fs
  .readdirSync(ARCHIVE_DIR)
  .filter((f) => f.endsWith(".json") && f !== "ALL-FINDINGS.json");

for (const filename of archiveFiles) {
  let doc;
  try {
    doc = JSON.parse(fs.readFileSync(path.join(ARCHIVE_DIR, filename), "utf8"));
  } catch {
    continue;
  }
  const roundLabel = doc.round_label ?? filename.replace(/\.json$/, "");
  const date = doc.date ?? filename.slice(0, 10);
  // Skip the multi-round campaigns (R-multi-roundN) that aren't really
  // one report; they're synthesised separately into ALL-FINDINGS.json.
  // Keep R-upgraded-roundN since those are per-paper rollups.
  const isExternal = (doc.round_type ?? "").startsWith("external");
  const source = isExternal ? "houston-paste" : "internal-stage3";

  const papers = doc.papers ?? {};
  for (const [code, paperData] of Object.entries(papers)) {
    const slug = SLUG_MAP[code];
    if (!slug) continue;
    const reviewers = paperData.reviewers ?? {};
    if (!isExternal && Object.keys(reviewers).length === 0) continue;

    // Prefer truth-audit VERIFIED counts; fall back to raw classification
    // when no audit is recorded.
    let blockers = countByVerdict(reviewers, "BLOCKER");
    let majors = countByVerdict(reviewers, "MAJOR");
    let minors = countByVerdict(reviewers, "MINOR") + countByVerdict(reviewers, "MINOR");
    let usedRaw = false;
    if (!paperData.summary?.by_audit_verdict) {
      blockers = countByRawClassification(reviewers, "BLOCKER");
      majors = countByRawClassification(reviewers, "MAJOR");
      minors = countByRawClassification(reviewers, "MINOR");
      usedRaw = true;
    }

    // Recommendation heuristic: any VERIFIED blocker → major-revisions
    const recommendation =
      blockers > 0
        ? "major-revisions"
        : majors > 0
          ? "minor-revisions"
          : "accept";

    const notes = [
      `round: ${roundLabel}`,
      paperData.version_at_time_of_review &&
        `version-at-review: ${paperData.version_at_time_of_review}`,
      paperData.closure_version && `version-at-closure: ${paperData.closure_version}`,
      usedRaw && "counts: raw classification (no truth-audit recorded)",
      paperData.summary?.by_audit_verdict &&
        `audit-verdict: ${JSON.stringify(paperData.summary.by_audit_verdict)}`,
    ]
      .filter(Boolean)
      .join(" · ");

    const vendorTag = Object.keys(reviewers).join(", ") || "multi-vendor";
    const reviewerLabel = isExternal
      ? `External · ${roundLabel} (${vendorTag})`
      : `${roundLabel} (${vendorTag})`;

    rows.push({
      paperSlug: slug,
      source,
      reviewerLabel,
      receivedAt: date,
      blockerCount: blockers,
      majorCount: majors,
      minorCount: minors,
      recommendation,
      pdfUrl: `https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/findings-archive/${filename}`,
      notes,
    });
  }
}

// ── external/*.md (Houston-pasted vendor reports) ────────────────────
const externalFiles = fs.existsSync(EXTERNAL_DIR)
  ? fs.readdirSync(EXTERNAL_DIR).filter((f) => f.endsWith(".md"))
  : [];

for (const filename of externalFiles) {
  // Parse pattern: 2026-05-15_P4_v1066_houston_external_4vendor_consolidated.md
  const m = filename.match(/^(\d{4}-\d{2}-\d{2})_(P\d[A-Z]?)_/);
  if (!m) continue;
  const [, date, code] = m;
  const slug = SLUG_MAP[code];
  if (!slug) continue;
  rows.push({
    paperSlug: slug,
    source: "houston-paste",
    reviewerLabel: filename.includes("synthesis")
      ? "Houston external (synthesis)"
      : "Houston external paste",
    receivedAt: date,
    // No counts in raw .md without parsing; deferred to per-finding archive
    // rows for those numbers. This is the report-existence row.
    blockerCount: 0,
    majorCount: 0,
    minorCount: 0,
    recommendation: "pending",
    pdfUrl: `https://github.com/Hubify-Projects/bigbounce/blob/main/project-context/peer-reviews/external/${filename}`,
    notes: `source-file: project-context/peer-reviews/external/${filename}`,
  });
}

// ── Push to Convex ───────────────────────────────────────────────────
let pushed = 0;
for (const row of rows) {
  await client.mutation(api.externalReviews.upsertByLabelDate, row);
  pushed++;
}
console.log(`✔ ${pushed} external-review rows seeded across ${rows.length} candidate rows`);

// Verify
const grouped = await client.query(api.externalReviews.listAll);
console.log("\nPost-seed counts per paper:");
const allSlugs = ["paper-1a", "paper-1b", "paper-2", "paper-3", "paper-4", "paper-5"];
for (const slug of allSlugs) {
  const rs = grouped[slug] ?? [];
  console.log(`  ${slug.padEnd(12)} ${rs.length} reviews`);
}
