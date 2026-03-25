/**
 * Convex Schema — Galaxy Chirality Catalog
 * =========================================
 *
 * Table: galaxies
 *
 * Stores the chirality classification catalog produced by Pipeline 2.
 * Each row is one galaxy from the DESI Legacy Survey DR8, classified
 * as CW (clockwise), CCW (counter-clockwise), or NOT_SPIRAL by the
 * equivariant Zoobot-based chirality model.
 *
 * Deployment:
 *   1. Copy this file into your Convex project's `convex/` directory as `schema.ts`.
 *   2. Run `npx convex dev` (dev) or `npx convex deploy` (prod) to push the schema.
 *
 * Convex URLs (from .env.local):
 *   Dev:  https://impressive-quail-879.convex.cloud
 *   Prod: https://scintillating-cow-269.convex.cloud
 */

import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  galaxies: defineTable({
    // --- Core identifiers ---
    dr8_id: v.string(), // DESI Legacy Survey DR8 object identifier

    // --- Sky coordinates (J2000, degrees) ---
    // Added in Phase 2 via GZ DESI Zenodo cross-match
    ra: v.float64(),  // Right ascension [0, 360)
    dec: v.float64(), // Declination [-90, +90]

    // --- Chirality probabilities (sum to ~1) ---
    p_cw: v.float64(),  // P(clockwise spiral)       [0, 1]
    p_ccw: v.float64(), // P(counter-clockwise spiral) [0, 1]
    p_ns: v.float64(),  // P(not a spiral)            [0, 1]

    // --- Derived classification ---
    classification: v.string(), // "CW" | "CCW" | "NOT_SPIRAL"
    confidence: v.float64(),    // max(p_cw, p_ccw, p_ns) [0, 1]

    // --- Optional future fields ---
    // Uncomment these as the pipeline evolves:
    // z_phot: v.optional(v.float64()),    // Photometric redshift
    // survey_name: v.optional(v.string()), // Source survey identifier
    // image_url: v.optional(v.string()),   // URL to galaxy cutout image
  })
    // --- Indexes for efficient queries ---
    .index("by_class", ["classification"])          // Filter by CW/CCW/NOT_SPIRAL
    .index("by_confidence", ["confidence"])          // Sort/filter by confidence
    .index("by_dr8_id", ["dr8_id"])                  // Lookup by survey ID
    // --- Search index for dr8_id text search ---
    .searchIndex("search_dr8_id", {
      searchField: "dr8_id",
    }),
});
