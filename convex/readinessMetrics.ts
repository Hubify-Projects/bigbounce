import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

/**
 * readinessMetrics — per-paper per-wave verdict rows + the honest
 * publishability-ETA computation.
 *
 * HONESTY CONTRACT (Houston, 2026-07-10):
 *   - `verdicts[].verdict` are the REAL recorded verdicts from INT-API raws
 *     and EXT browser raws. Never synthesized. A leg with no output is
 *     recorded verdict:"failed" and rendered as a GAP (never a zero).
 *   - The ETA states its assumption explicitly (`confidence` field): it
 *     assumes 0 new findings from here; a single genuinely-new finding on a
 *     paper resets that paper's clean-wave streak and pushes the ETA out.
 *   - Journal ACCEPTANCE is a separate, external clock (human referees,
 *     months) — this ETA is only the loop's own "papers stop surfacing
 *     genuinely-new findings" clock. The widget copy says so.
 */

const VERDICT = v.union(
  v.literal("reject"),
  v.literal("major-revisions"),
  v.literal("minor-revisions"),
  v.literal("accept"),
  v.literal("failed"),
);

const CHANNEL = v.union(v.literal("INT"), v.literal("EXT"));

// Chronological sort key from an ISO date; ties broken by insertion order.
function seqFor(dateISO: string): number {
  const t = Date.parse(dateISO);
  return Number.isNaN(t) ? 0 : t;
}

// ── Mutations ────────────────────────────────────────────────────────────

/**
 * Upsert ONE per-paper per-wave row (idempotent on paperSlug+waveLabel).
 * Called by the backfill script and by the live loop (tools/record_wave.sh)
 * after every harvest/audit. Re-recording the same wave overwrites in place.
 */
export const recordWave = mutation({
  args: {
    paperSlug: v.string(),
    paperId: v.string(),
    waveLabel: v.string(),
    dateISO: v.string(),
    genuinelyNewCount: v.number(),
    cleanWaveStreak: v.number(),
    openComputeCount: v.number(),
    openVenueCount: v.number(),
    verdicts: v.array(
      v.object({ reviewer: v.string(), channel: CHANNEL, verdict: VERDICT }),
    ),
    note: v.optional(v.string()),
    // Optional explicit ordering tiebreak (ms). When omitted, derived from dateISO.
    seq: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const seq = args.seq ?? seqFor(args.dateISO);
    const existing = await ctx.db
      .query("readinessMetrics")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.paperSlug))
      .collect();
    const match = existing.find((r) => r.waveLabel === args.waveLabel);
    const doc = {
      paperSlug: args.paperSlug,
      paperId: args.paperId,
      waveLabel: args.waveLabel,
      dateISO: args.dateISO,
      seq,
      genuinelyNewCount: args.genuinelyNewCount,
      cleanWaveStreak: args.cleanWaveStreak,
      openComputeCount: args.openComputeCount,
      openVenueCount: args.openVenueCount,
      verdicts: args.verdicts,
      note: args.note,
      createdAt: Date.now(),
    };
    if (match) {
      await ctx.db.patch(match._id, doc);
      return { updated: match._id };
    }
    const id = await ctx.db.insert("readinessMetrics", doc);
    return { inserted: id };
  },
});

export const recordRigorEvent = mutation({
  args: {
    label: v.string(),
    dateISO: v.string(),
    description: v.string(),
    source: v.string(),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("rigorEvents")
      .withIndex("by_date", (q) => q.eq("dateISO", args.dateISO))
      .collect();
    const match = existing.find((r) => r.label === args.label);
    const doc = { ...args, createdAt: Date.now() };
    if (match) {
      await ctx.db.patch(match._id, doc);
      return { updated: match._id };
    }
    const id = await ctx.db.insert("rigorEvents", doc);
    return { inserted: id };
  },
});

// ── Queries ──────────────────────────────────────────────────────────────

/** All wave rows, chronological (oldest → newest). Drives the trajectory chart. */
export const listWaves = query({
  args: {},
  handler: async (ctx) => {
    const rows = await ctx.db.query("readinessMetrics").withIndex("by_seq").collect();
    return rows.sort((a, b) => a.seq - b.seq || a.paperId.localeCompare(b.paperId));
  },
});

export const listRigorEvents = query({
  args: {},
  handler: async (ctx) => {
    const rows = await ctx.db.query("rigorEvents").withIndex("by_date").collect();
    return rows.sort((a, b) => a.dateISO.localeCompare(b.dateISO));
  },
});

// ── ETA computation ──────────────────────────────────────────────────────

// Rolling median of wave-to-wave durations (hours) from the last N wave dates.
function rollingMedianWaveHours(seqs: number[], fallbackH: number): number {
  const uniq = Array.from(new Set(seqs)).sort((a, b) => a - b);
  if (uniq.length < 2) return fallbackH;
  const last = uniq.slice(-6); // last 5 gaps = last 6 timestamps
  const gaps: number[] = [];
  for (let i = 1; i < last.length; i++) {
    const h = (last[i] - last[i - 1]) / 3_600_000;
    // Sub-30-minute gaps are correction/bookkeeping rows posted back-to-back,
    // not real wave cadence — excluding them keeps the median honest.
    if (h > 0.5) gaps.push(h);
  }
  if (gaps.length === 0) return fallbackH;
  gaps.sort((a, b) => a - b);
  const mid = Math.floor(gaps.length / 2);
  const med = gaps.length % 2 ? gaps[mid] : (gaps[mid - 1] + gaps[mid]) / 2;
  // Clamp to a sane band so a single 12-hour idle gap doesn't blow up the ETA.
  return Math.min(Math.max(med, 0.5), 12);
}

/**
 * computeEta — honest publishability ETA.
 *
 * Per paper, remaining waves to the loop's convergence bar =
 *   max(0, TARGET_CLEAN_WAVES − cleanWaveStreak)
 * (TARGET_CLEAN_WAVES = 2, directive K: two consecutive clean waves).
 * ETA hours = remaining × rolling-median wave-duration (last 5 gaps, fallback 3h)
 *             + 2h closure-buffer if the paper's LAST wave had genuinelyNewCount>0.
 * Program submission-ready ETA = MAX over papers (the last paper to converge).
 */
export const computeEta = query({
  args: {},
  handler: async (ctx) => {
    const TARGET_CLEAN_WAVES = 2;
    const FALLBACK_WAVE_H = 3;
    const CLOSURE_BUFFER_H = 2;

    const rows = await ctx.db.query("readinessMetrics").withIndex("by_seq").collect();
    rows.sort((a, b) => a.seq - b.seq);

    const medianWaveH = rollingMedianWaveHours(
      rows.map((r) => r.seq),
      FALLBACK_WAVE_H,
    );

    // Group by paper, keep the latest wave per paper.
    const byPaper = new Map<string, typeof rows>();
    for (const r of rows) {
      const arr = byPaper.get(r.paperId) ?? [];
      arr.push(r);
      byPaper.set(r.paperId, arr);
    }

    // Canonical six submission targets ONLY (2026-07-23 fix): the P1 merge was
    // reversed — P1B (namaster-proof metapaper) is an active target again and
    // P1U is retired. Older rows also carry raw doc-id paperIds; those and any
    // non-canonical labels must never drive the ETA or the papers count.
    const CANONICAL_PAPERS = new Set(["P1A", "P1B", "P2", "P3", "P4", "P5"]);

    const perPaper = Array.from(byPaper.entries())
      .filter(([paperId]) => CANONICAL_PAPERS.has(paperId))
      .map(([paperId, waves]) => {
        waves.sort((a, b) => a.seq - b.seq);
        const last = waves[waves.length - 1];
        const remainingWaves = Math.max(0, TARGET_CLEAN_WAVES - last.cleanWaveStreak);
        const buffer = last.genuinelyNewCount > 0 ? CLOSURE_BUFFER_H : 0;
        const etaHours = remainingWaves === 0 ? 0 : remainingWaves * medianWaveH + buffer;
        return {
          paperId,
          paperSlug: last.paperSlug,
          cleanWaveStreak: last.cleanWaveStreak,
          remainingWaves,
          openComputeCount: last.openComputeCount,
          openVenueCount: last.openVenueCount,
          lastWaveGenuinelyNew: last.genuinelyNewCount,
          lastWaveLabel: last.waveLabel,
          lastDateISO: last.dateISO,
          etaHours: Math.round(etaHours * 10) / 10,
          converged: remainingWaves === 0,
        };
      })
      .sort((a, b) => a.paperId.localeCompare(b.paperId));

    const programEtaHours = perPaper.reduce((m, p) => Math.max(m, p.etaHours), 0);
    const papersConverged = perPaper.filter((p) => p.converged).length;

    return {
      programEtaHours,
      papersConverged,
      papersTotal: perPaper.length,
      medianWaveHours: Math.round(medianWaveH * 10) / 10,
      targetCleanWaves: TARGET_CLEAN_WAVES,
      perPaper,
      confidence:
        "ETA to the loop's own convergence bar (two consecutive clean review waves). " +
        "Assumes 0 new findings from here — a single genuinely-new finding on any paper " +
        "resets that paper's clean-wave streak and pushes its ETA out. This is NOT the " +
        "journal-acceptance clock: acceptance depends on human referees (months, external).",
    };
  },
});
