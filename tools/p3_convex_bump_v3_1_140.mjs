import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p3",
  version: "v3.1.140",
  datestamp: "2026-07-06",
  texCommit: "2b8fb0be09fa16659600a167edc1c18e0732f931",
  pdfMd5: "55459a5f46ec48754a74db448f1e7657",
  pdfPages: 33,
  pdfSizeBytes: 4678433,
  changelog:
    "D-round final polish (presentation + disclosure ONLY, 0 numbers changed): title sharpened 24->20 words (kept 268,519 validated + 37.3M); abstract rewritten first-time-reader (lead with catalog + real-object demo, process-volume disclaimer stated once, caveat repetition removed, ~1000->~550 words, every number byte-identical); prose de-densified (Intro/Method/sec:sdss/sec:desi/Discussion/Conclusions); AI-assisted-methodology disclosure added to acknowledgments; CC-BY-4.0 license added to catalog availability. Verified 0 distinct numeric values added/deleted vs v3.1.139.",
  sitePdfPath: "/papers/paper3_draft_v3.1.140.pdf",
});
console.log("P3 inserted:", result);
