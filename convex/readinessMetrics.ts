import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

/**
 * readinessMetrics — per-paper per-wave verdict rows. HISTORICAL RECORD.
 *
 * HONESTY CONTRACT (Houston, 2026-07-10):
 *   - `verdicts[].verdict` are the REAL recorded verdicts from INT-API raws
 *     and EXT browser raws. Never synthesized. A leg with no output is
 *     recorded verdict:"failed" and rendered as a GAP (never a zero).
 *
 * SCOPE NOTE (2026-07-24). These rows drive the /reviews verdict-trajectory
 * chart and nothing else. The `computeEta` projection that used to live at
 * the bottom of this file is RETIRED — see the note there. `cleanWaveStreak`
 * is a directive-K quantity; directive K's two-clean-waves bar is no longer
 * the program's exit criterion, so the streak field is history, not status.
 * Live publication status is `publicationStatus:get`.
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

// ── ETA computation — RETIRED 2026-07-24 ─────────────────────────────────
//
// `computeEta` used to live here. It projected "hours to submission-ready"
// from each paper's clean-wave streak against TARGET_CLEAN_WAVES = 2 —
// directive K's bar. Directive L demoted that bar to "a CHECKPOINT, not the
// finish line", and directives M / M-AMENDED / P superseded it again, so the
// homepage was counting down to a target the program no longer holds.
//
// It also read rows that stopped being written on 2026-07-16, so it rendered
// eight-day-old streaks (P1A 18, P2 20) as current — after the 2026-07-22
// confirmation wave had surfaced genuinely-new-real findings on all six
// papers, which under directive K's own definition resets every one of those
// streaks. A retired bar measured against stale data, presented as a live
// clock. Removed rather than backfilled.
//
// The directive-P replacement is `publicationStatus:get`, which derives the
// remaining gates and their owners from live rows and degrades to an explicit
// "stale — last updated X" state instead of silently aging.
//
// The wave rows themselves are HISTORY and are kept: `recordWave` still
// accepts them and `listWaves` still drives the /reviews verdict-trajectory
// chart. Only the ETA projection is gone.
