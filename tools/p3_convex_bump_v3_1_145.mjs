import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p3",
  version: "v3.1.145",
  datestamp: "July 8, 2026",
  texCommit: "58395e24",
  pdfMd5: "873fabc8b121170518cc03d11990e97f",
  pdfPages: 34,
  pdfSizeBytes: 4435776,
  changelog:
    "Pod-gated closure: EXACT spatial-uniformity chi^2 recomputed on the 377,482 post-excision headline set. Prior drafts reported chi^2=376,713 on the full inclusive 378,280 set (incl. now-excised Gaia-500 + eROSITA-298) and stated the exact recompute was not possible without fabricating (pod-side LAMOST positions uncommitted). Those positions ARE reachable: HF bamfai/bigbounce-anomaly-catalog pathc_unique_objects.parquet ships per-object ra/dec + survey provenance incl. all 108,963 LAMOST DR10 positions. Recompute (NSIDE=64, uniform-mean over occupied pixels; IDENTICAL method to r24conf pod item#35) VALIDATED against the pod reference to delta=0.0000 on the inclusive set, then computed on 377,482: chi^2=365,428 (dof=23,636, chi^2_nu=15.46) vs 376,713 (15.67). Footprint-dominated conclusion unchanged. No pod spent. Artifact: outputs/spatial_chi2_excised_377482.json. NEVER fabricated.",
  sitePdfPath: "/papers/paper3_draft_v3.1.145.pdf",
});
console.log("P3 inserted:", result);
