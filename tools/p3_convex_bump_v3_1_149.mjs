import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p3",
  version: "v3.1.149",
  datestamp: "July 9, 2026",
  texCommit: process.env.TEX_COMMIT || "POST_COMMIT_SHA",
  pdfMd5: "50e165200eaa97c7dd1e7771538b0c5c",
  pdfPages: 36,
  pdfSizeBytes: 4452052,
  changelog:
    "CV-round EXT closure (framing/figure only, 0 verified numbers changed): (B1) new consolidated per-survey provenance Table in §III (public-archive -> read/scored -> thresholded -> count-retained -> tier), reproduced from existing values only; title/abstract scan-volume now points to it. (B4/directive-I6) Fig 6 (novelty fractions) REGENERATED to remove the excised Gaia DR3 27% bar (render-verified gone; 5 real coordinate-cross-matched surveys); Fig 10 (injection-recovery) caption relabeled so the Gaia curve is an explicit historical-record overplot, not a retained survey. (M1/M2) title now '...Sources and CMB Map Patches'; NEOWISE geometry-QA + Planck CMB-patch separation surfaced. (minors) post-break 'the'->'The' cap fix; 'Seven limitations'->'Eight'. Grok/Gemini majors dispositioned already-disclosed re-flags (pattern-066); ChatGPT re-flags of disclosed content dispositioned non-real (directive-H). 268,519 / 377,482 / 195,829 / 2,468 / 77,905 all unchanged.",
  sitePdfPath: "/papers/paper3_anomaly_catalog_v3.1.149.pdf",
});
console.log("P3 inserted:", result);
