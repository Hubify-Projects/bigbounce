/**
 * Convex Functions — Galaxy Chirality Catalog
 * =============================================
 *
 * Mutations and queries for bulk-importing and querying the chirality catalog.
 *
 * Deployment:
 *   1. Copy this file into your Convex project's `convex/` directory as `galaxies.ts`.
 *   2. Push with `npx convex dev` or `npx convex deploy`.
 *
 * The Python import script calls the `importBatch` mutation via the HTTP API:
 *   POST {CONVEX_URL}/api/mutation
 *   Body: { "path": "galaxies:importBatch", "args": { "batch": [...] } }
 *
 * The `count` query is used for resume support:
 *   POST {CONVEX_URL}/api/query
 *   Body: { "path": "galaxies:count", "args": {} }
 */

import { mutation, query } from "./_generated/server";
import { v } from "convex/values";

/**
 * importBatch — Insert a batch of galaxies into the catalog.
 *
 * Accepts up to 1000 rows per call (Convex mutation size limit).
 * Each row must have all required fields; optional fields are omitted
 * until Phase 3+ of the pipeline.
 *
 * Returns the number of rows inserted.
 */
export const importBatch = mutation({
  args: {
    batch: v.array(
      v.object({
        dr8_id: v.string(),
        ra: v.float64(),
        dec: v.float64(),
        p_cw: v.float64(),
        p_ccw: v.float64(),
        p_ns: v.float64(),
        classification: v.string(),
        confidence: v.float64(),
      })
    ),
  },
  handler: async (ctx, args) => {
    for (const galaxy of args.batch) {
      await ctx.db.insert("galaxies", galaxy);
    }
    return args.batch.length;
  },
});

/**
 * count — Return total number of galaxies in the catalog.
 *
 * Used by the import script for resume support: if the script is
 * interrupted, it re-reads the count and skips already-imported rows.
 *
 * NOTE: For very large catalogs (>100K), consider replacing .collect()
 * with a dedicated counter document to avoid reading all rows.
 */
export const count = query({
  handler: async (ctx) => {
    const galaxies = await ctx.db.query("galaxies").collect();
    return galaxies.length;
  },
});

/**
 * search — Look up a single galaxy by its DR8 identifier.
 *
 * Uses the by_dr8_id index for O(1) lookup.
 */
export const search = query({
  args: { dr8_id: v.string() },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("galaxies")
      .withIndex("by_dr8_id", (q) => q.eq("dr8_id", args.dr8_id))
      .first();
  },
});

/**
 * byClass — Query galaxies by classification with optional confidence threshold.
 *
 * Example usage from the HTTP API:
 *   POST {CONVEX_URL}/api/query
 *   Body: { "path": "galaxies:byClass", "args": { "classification": "CW" } }
 */
export const byClass = query({
  args: {
    classification: v.string(),
  },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("galaxies")
      .withIndex("by_class", (q) => q.eq("classification", args.classification))
      .take(1000);
  },
});
