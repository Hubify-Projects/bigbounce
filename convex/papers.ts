import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

// ──────────────────────────────────────────────────────────────────────
// Paper-level CRUD
// ──────────────────────────────────────────────────────────────────────

export const list = query({
  handler: async (ctx) => {
    return await ctx.db.query("papers").collect();
  },
});

export const getBySlug = query({
  args: { slug: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("papers")
      .withIndex("by_slug", (q) => q.eq("slug", args.slug))
      .unique();
  },
});

export const upsert = mutation({
  args: {
    slug: v.string(),
    number: v.string(),
    title: v.string(),
    shortTitle: v.string(),
    targetJournal: v.union(
      v.literal("PRD"),
      v.literal("MNRAS"),
      v.literal("JCAP"),
      v.literal("ApJ"),
      v.literal("other")
    ),
    status: v.union(
      v.literal("active-drive-to-100"),
      v.literal("paused-houston-external"),
      v.literal("submitted-arxiv"),
      v.literal("in-revision"),
      v.literal("accepted")
    ),
    texPath: v.string(),
    sitePdfPath: v.string(),
    focusAreas: v.array(v.string()),
    houstonSignOff: v.optional(v.string()),
    houstonSignOffNote: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const existing = await ctx.db
      .query("papers")
      .withIndex("by_slug", (q) => q.eq("slug", args.slug))
      .unique();
    if (existing) {
      await ctx.db.patch(existing._id, args);
      return existing._id;
    }
    return await ctx.db.insert("papers", args);
  },
});

export const setStatus = mutation({
  args: {
    slug: v.string(),
    status: v.union(
      v.literal("active-drive-to-100"),
      v.literal("paused-houston-external"),
      v.literal("submitted-arxiv"),
      v.literal("in-revision"),
      v.literal("accepted")
    ),
  },
  handler: async (ctx, args) => {
    const paper = await ctx.db
      .query("papers")
      .withIndex("by_slug", (q) => q.eq("slug", args.slug))
      .unique();
    if (!paper) throw new Error(`paper not found: ${args.slug}`);
    await ctx.db.patch(paper._id, { status: args.status });
  },
});

export const setHoustonSignOff = mutation({
  args: {
    slug: v.string(),
    signOffDate: v.string(),
    note: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const paper = await ctx.db
      .query("papers")
      .withIndex("by_slug", (q) => q.eq("slug", args.slug))
      .unique();
    if (!paper) throw new Error(`paper not found: ${args.slug}`);
    await ctx.db.patch(paper._id, {
      houstonSignOff: args.signOffDate,
      houstonSignOffNote: args.note,
    });
  },
});

// ──────────────────────────────────────────────────────────────────────
// The load-bearing query: getPaperState(slug) — computes readiness from
// open findings + open caveats. THIS is the structural fix for the
// "I forgot to bump readiness after 5 closures" drift.
//
// Formula (per DATA_MODEL_ARCHITECTURE.md):
//   readiness = 95 − 2·openBlockers − 1·openMajors − 0.2·openMinors − 1·openCaveats
//   capped at the 95-floor pre-Houston-sign-off (per feedback_99_pct_readiness_cap).
//   Once Houston signs off → readiness = 100.
//   readiness is clamped to [0, 100].
// ──────────────────────────────────────────────────────────────────────

export const getPaperState = query({
  args: { slug: v.string() },
  handler: async (ctx, args) => {
    const paper = await ctx.db
      .query("papers")
      .withIndex("by_slug", (q) => q.eq("slug", args.slug))
      .unique();
    if (!paper) return null;

    const versions = await ctx.db
      .query("paper_versions")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.slug))
      .collect();
    versions.sort((a, b) => b.datestamp.localeCompare(a.datestamp));
    const currentVersion = versions[0] ?? null;

    const findings = await ctx.db
      .query("findings")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.slug))
      .collect();

    const openFindings = findings.filter(
      (f) => f.closureStatus === "open" || f.closureStatus === "in-progress"
    );
    const openBlockers = openFindings.filter((f) => f.classification === "BLOCKER").length;
    const openMajors = openFindings.filter((f) => f.classification === "MAJOR").length;
    const openMinors = openFindings.filter((f) => f.classification === "MINOR").length;
    const openNits = openFindings.filter((f) => f.classification === "NIT").length;

    const caveats = await ctx.db
      .query("pathc_caveats")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.slug))
      .collect();
    const openCaveats = caveats.filter(
      (c) => c.status === "open" || c.status === "deferred"
    ).length;

    const rRounds = await ctx.db
      .query("r_rounds")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.slug))
      .collect();
    rRounds.sort((a, b) => b.dispatchedAt - a.dispatchedAt);
    const lastRRound = rRounds[0] ?? null;

    // Computed readiness — the source of truth that the site reads.
    let readinessComputed: number;
    if (paper.houstonSignOff) {
      readinessComputed = 100;
    } else {
      const penalty =
        2 * openBlockers +
        1 * openMajors +
        0.2 * openMinors +
        1 * openCaveats;
      readinessComputed = Math.max(0, Math.min(95, 95 - penalty));
    }

    // Last-updated date is max of (current version datestamp, latest closed finding date)
    const closedFindings = findings.filter((f) => f.closedAt !== undefined);
    const latestClosureMs = closedFindings.reduce(
      (max, f) => Math.max(max, f.closedAt ?? 0),
      0
    );
    const latestClosureISO = latestClosureMs
      ? new Date(latestClosureMs).toISOString().slice(0, 10)
      : null;
    const lastUpdated =
      currentVersion && latestClosureISO
        ? currentVersion.datestamp > latestClosureISO
          ? currentVersion.datestamp
          : latestClosureISO
        : currentVersion?.datestamp ?? latestClosureISO ?? null;

    return {
      ...paper,
      currentVersion,
      versions, // newest first
      lastRRound,
      rRoundCount: rRounds.length,
      findingsByClassification: {
        open: {
          blockers: openBlockers,
          majors: openMajors,
          minors: openMinors,
          nits: openNits,
          total: openFindings.length,
        },
        closed: findings.length - openFindings.length,
      },
      caveats: {
        open: openCaveats,
        total: caveats.length,
      },
      readinessComputed: Math.round(readinessComputed),
      lastUpdated,
    };
  },
});

// Cross-paper dashboard view — returns getPaperState for every paper, sorted.
export const listAllPaperStates = query({
  handler: async (ctx) => {
    const papers = await ctx.db.query("papers").collect();
    const results = [];
    for (const paper of papers) {
      // Inline the computation (cannot call other queries from inside a query).
      const versions = await ctx.db
        .query("paper_versions")
        .withIndex("by_paper", (q) => q.eq("paperSlug", paper.slug))
        .collect();
      versions.sort((a, b) => {
        const d = b.datestamp.localeCompare(a.datestamp);
        if (d !== 0) return d;
        return (b.createdAt ?? 0) - (a.createdAt ?? 0);
      });
      const currentVersion = versions[0] ?? null;

      const findings = await ctx.db
        .query("findings")
        .withIndex("by_paper", (q) => q.eq("paperSlug", paper.slug))
        .collect();
      const openFindings = findings.filter(
        (f) => f.closureStatus === "open" || f.closureStatus === "in-progress"
      );
      const openBlockers = openFindings.filter((f) => f.classification === "BLOCKER").length;
      const openMajors = openFindings.filter((f) => f.classification === "MAJOR").length;
      const openMinors = openFindings.filter((f) => f.classification === "MINOR").length;

      const caveats = await ctx.db
        .query("pathc_caveats")
        .withIndex("by_paper", (q) => q.eq("paperSlug", paper.slug))
        .collect();
      const openCaveats = caveats.filter(
        (c) => c.status === "open" || c.status === "deferred"
      ).length;

      let readinessComputed: number;
      if (paper.houstonSignOff) {
        readinessComputed = 100;
      } else {
        const penalty =
          2 * openBlockers + 1 * openMajors + 0.2 * openMinors + 1 * openCaveats;
        readinessComputed = Math.max(0, Math.min(95, 95 - penalty));
      }

      results.push({
        slug: paper.slug,
        number: paper.number,
        shortTitle: paper.shortTitle,
        status: paper.status,
        currentVersion: currentVersion?.version ?? null,
        lastUpdated: currentVersion?.datestamp ?? null,
        readinessComputed: Math.round(readinessComputed),
        openBlockers,
        openMajors,
        openMinors,
        openCaveats,
        houstonSignOff: paper.houstonSignOff ?? null,
        sitePdfPath: paper.sitePdfPath ?? null,
      });
    }
    // Sort by paper number for stable display
    results.sort((a, b) => a.number.localeCompare(b.number, undefined, { numeric: true }));
    return results;
  },
});

// External-review prompt generator — replaces the hardcoded focusAreas in
// site/src/app/papers/[slug]/page.tsx. Returns the canonical copy/paste
// prompt for Houston, generated from current Convex state.
export const getExternalReviewPrompt = query({
  args: { slug: v.string() },
  handler: async (ctx, args) => {
    const paper = await ctx.db
      .query("papers")
      .withIndex("by_slug", (q) => q.eq("slug", args.slug))
      .unique();
    if (!paper) return null;

    const versions = await ctx.db
      .query("paper_versions")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.slug))
      .collect();
    versions.sort((a, b) => b.datestamp.localeCompare(a.datestamp));
    const cur = versions[0];

    const openCaveats = await ctx.db
      .query("pathc_caveats")
      .withIndex("by_paper", (q) => q.eq("paperSlug", args.slug))
      .collect();
    const openLabels = openCaveats
      .filter((c) => c.status === "open" || c.status === "deferred")
      .map((c) => `(${c.label}) ${c.description.slice(0, 100)}`);

    const lines = [
      `You are an external referee for ${paper.targetJournal} (target journal).`,
      ``,
      `Attached: Paper ${paper.number} ${cur?.version ?? "(unversioned)"} — "${paper.title}"`,
      `Source: ${paper.texPath}`,
      cur ? `PDF: ${cur.pdfPages} pp / ${(cur.pdfSizeBytes / 1e6).toFixed(2)} MB / md5 ${cur.pdfMd5.slice(0, 8)}` : "PDF: (no version recorded)",
      ``,
      `Read the FULL PDF end-to-end. Produce a referee report in MNRAS format with:`,
      ``,
      `1. Recommendation: ACCEPT / MINOR REVISIONS / MAJOR REVISIONS / REJECT`,
      `2. BLOCKERS (must fix before publication) — list each with section/line + proposed fix`,
      `3. MAJORS (should fix) — same format`,
      `4. MINORS (polish) — same format`,
      `5. Strengths (>= 3 bullet points)`,
      ...(paper.focusAreas.length > 0
        ? [
            `6. Specific scrutiny on:`,
            ...paper.focusAreas.map((f) => `   - ${f}`),
          ]
        : []),
      ...(openLabels.length > 0
        ? [
            ``,
            `Currently open §pathc_caveats items (author-tracked deferrals):`,
            ...openLabels.map((l) => `   - ${l}`),
          ]
        : []),
      ``,
      `Be ruthless. We want it harder than the actual journal review. Truth-audit any claim that seems off by grepping the published .tex / on-disk artifacts before flagging — do not echo prompt context.`,
    ];
    return {
      paperSlug: paper.slug,
      paperVersion: cur?.version ?? null,
      pdfPath: paper.sitePdfPath,
      prompt: lines.join("\n"),
    };
  },
});
