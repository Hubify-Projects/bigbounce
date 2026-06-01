import { query } from "./_generated/server";
import { v } from "convex/values";

/**
 * Unified time-sorted activity feed. Combines every paper-orchestration
 * event written to Convex into a single descending-time list. Used by the
 * /activity page on the site. Read-only.
 *
 * Sources mixed in:
 *   - paper_versions: each .tex version bump (with changelog + md5)
 *   - r_rounds: each cross-vendor R-round dispatch
 *   - findings: open + closed (timestamp = closedAt if closed, else _creationTime)
 *   - pathc_caveats: each caveat closure
 *   - pods: lifecycle events (started/stopped)
 *
 * Each entry has { id, kind, paperSlug, headline, detail, timestamp,
 *   colorHint }.
 */
export const recent = query({
  args: { limit: v.optional(v.number()) },
  handler: async (ctx, args) => {
    const limit = args.limit ?? 100;
    const events: Array<{
      id: string;
      kind: string;
      paperSlug: string | null;
      headline: string;
      detail: string;
      timestamp: number;
      colorHint: string;
    }> = [];

    // Paper-version bumps
    const versions = await ctx.db.query("paper_versions").collect();
    for (const v of versions) {
      events.push({
        id: `version:${v._id}`,
        kind: "version_bump",
        paperSlug: v.paperSlug,
        headline: `${v.paperSlug.toUpperCase()} bumped to ${v.version}`,
        detail: v.changelog.slice(0, 240),
        timestamp: v.createdAt,
        colorHint: "#0369a1",
      });
    }

    // R-round dispatches
    const rounds = await ctx.db.query("r_rounds").collect();
    for (const r of rounds) {
      events.push({
        id: `round:${r._id}`,
        kind: "r_round",
        paperSlug: r.paperSlug,
        headline: `R-round dispatched on ${r.paperSlug} (${r.source})`,
        detail: `${r.roundLabel} · reviewers: ${r.vendors.slice(0, 4).join(", ")}`,
        timestamp: r.dispatchedAt,
        colorHint: "#7c2d12",
      });
      if (r.completedAt) {
        events.push({
          id: `round_done:${r._id}`,
          kind: "r_round_done",
          paperSlug: r.paperSlug,
          headline: `R-round complete on ${r.paperSlug}`,
          detail: `${r.roundLabel}: ${r.vendors.length} reviewers`,
          timestamp: r.completedAt,
          colorHint: "#16a34a",
        });
      }
    }

    // Finding closures (only closed; open ones show in queue not feed)
    const findings = await ctx.db.query("findings").collect();
    for (const f of findings) {
      if (f.closedAt) {
        const isFalsified = f.closureStatus === "closed-by-truth-audit-falsification";
        events.push({
          id: `finding:${f._id}`,
          kind: isFalsified ? "finding_audit_close" : "finding_real_close",
          paperSlug: f.paperSlug,
          headline: `${f.paperSlug} ${f.findingId} closed (${f.closureStatus.replace("closed-by-", "")})`,
          detail: `${f.classification}: ${f.claim.slice(0, 200)}${f.claim.length > 200 ? "…" : ""}`,
          timestamp: f.closedAt,
          colorHint: isFalsified ? "#a16207" : "#16a34a",
        });
      }
    }

    // Pathc-caveat closures
    const caveats = await ctx.db.query("pathc_caveats").collect();
    for (const c of caveats) {
      if (c.closedAt) {
        events.push({
          id: `caveat:${c._id}`,
          kind: "caveat_close",
          paperSlug: c.paperSlug,
          headline: `${c.paperSlug} §pathc_caveats (${c.label}) closed via ${c.closureMethod ?? "?"}`,
          detail: c.description.slice(0, 220),
          timestamp: c.closedAt,
          colorHint: c.closureMethod === "real-computation" ? "#15803d" :
                     c.closureMethod === "artifact-verification" ? "#15803d" :
                     c.closureMethod === "truth-audit-falsification" ? "#a16207" : "#dc2626",
        });
      }
    }

    // Pod lifecycle (last-synced; treat as a single event per pod for the feed)
    const pods = await ctx.db.query("pods").collect();
    for (const p of pods) {
      if (p.startedAt) {
        events.push({
          id: `pod_start:${p._id}`,
          kind: "pod_start",
          paperSlug: null,
          headline: `pod ${p.name} (${p.podId}) started`,
          detail: `${p.gpu} · purpose: ${p.purpose}`,
          timestamp: p.startedAt,
          colorHint: "#0369a1",
        });
      }
      if (p.stoppedAt) {
        events.push({
          id: `pod_stop:${p._id}`,
          kind: "pod_stop",
          paperSlug: null,
          headline: `pod ${p.name} stopped`,
          detail: `total cost $${p.totalCostUsd.toFixed(2)} · backed up: ${p.artifactsBackedUp ? "yes" : "NO"}`,
          timestamp: p.stoppedAt,
          colorHint: p.artifactsBackedUp ? "#16a34a" : "#dc2626",
        });
      }
    }

    events.sort((a, b) => b.timestamp - a.timestamp);
    return events.slice(0, limit);
  },
});

export const summary = query({
  handler: async (ctx) => {
    const versions = await ctx.db.query("paper_versions").collect();
    const rounds = await ctx.db.query("r_rounds").collect();
    const findings = await ctx.db.query("findings").collect();
    const caveats = await ctx.db.query("pathc_caveats").collect();
    const pods = await ctx.db.query("pods").collect();
    return {
      paperVersions: versions.length,
      rRounds: rounds.length,
      findings: { total: findings.length, closed: findings.filter((f) => f.closedAt !== undefined).length, open: findings.filter((f) => !f.closedAt).length },
      caveats: { total: caveats.length, closed: caveats.filter((c) => c.closedAt !== undefined).length, open: caveats.filter((c) => !c.closedAt).length },
      pods: { total: pods.length, running: pods.filter((p) => p.status === "running").length },
    };
  },
});
