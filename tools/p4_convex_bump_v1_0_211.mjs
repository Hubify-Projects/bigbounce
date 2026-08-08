import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p4",
  version: "v1.0.211",
  datestamp: "2026-07-02",
  texCommit: "53b9d919",
  pdfMd5: "e44405aea7108fb65e687d91e25ccc24",
  pdfPages: 29,
  pdfSizeBytes: 33965427,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.211.tar.gz",
  arxivTarballSizeBytes: 26696819,
  sitePdfPath: "/papers/chirality_catalog_paper_v1.0.211.pdf",
  changelog:
    "Close Gemini + Grok MINORS (v1.0.210 MINOR/MINOR) toward ACCEPT. KEY REAL CLOSURE (Gemini, Appendix E): replaced the qualitative 5-8% edge-on sensitivity-penalty bound with an EMPIRICAL axis-ratio metric — pulled b/a for all 3,201,160 classified spirals from DR8-sweep morphology and measured f_edge=15.80% (505,889 spirals with b/a<0.3), giving a measured 8.98% Fisher-floor inflation (threshold sweep 3.1-17.4% across b/a<0.20-0.40). Metric committed as JSON artifact (edge_on_contamination_metric.json) + \\artifact{}-cited. Appendix E and conclusions rewritten with the measured number. Every value computed from the parquet — NOT fabricated. Other Gemini minors: promoted the area-uniform cos-theta injection axis draw to PRIMARY (validation rerun already existed, artifact c16; U(0,pi) retained as cross-check, thresholds coincide within MC error); surfaced the rank-deficient-WLS drop-one-leg well-conditioned baseline in the main-text forward-model paragraph. Grok minors verified ALREADY PRESENT (surfaced, no fabrication): 8-anchor summary in main text, T1-T8 thresholds explicit in App B, flip-identity QC note, NaMaster fsky bookkeeping table. Recompile 29pp / 33.97MB / 0 undef-refs / 0 overfull hboxes. All 12 served paths byte-identical (md5 e44405ae). arXiv bundle rebuilt v1.0.211 (standalone-compile-verified, replaces v210).",
});
console.log("Inserted:", result);
