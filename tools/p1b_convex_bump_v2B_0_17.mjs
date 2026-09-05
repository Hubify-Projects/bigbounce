import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1b",
  version: "v2B.0.17",
  datestamp: "September 4, 2026",
  texCommit: "916313aa",
  pdfMd5: "7bc21cbe7a1dfb837f08cae2c8b0f2b3",
  pdfPages: 8,
  pdfSizeBytes: 451755,
  arxivTarballPath: "project-context/SSOT/arxiv_tarballs/paper1b_namaster_proof_arxiv_v2B.0.17.tar.gz",
  changelog: "Novelty lift #3 (project-context/NOVELTY_AUDIT_2026-09-04.md #3): reframes namaster-proof around the content-bound execution-receipt primitive it already implements and adds a pre-declared, sealed blind shortcut-detection test (18 runs; S1-S4 shortcut classes detected 12/12 with 0/3 false positives on honest runs; S5 metadata-forgery escaped 3/3 as pre-declared). New title/abstract framing (shortcut detector, not a fraud detector); new Blind Shortcut-Detection Test section with protocol + confusion table + two corrections found while running it; What-the-receipt-binds table; limitations + reproducibility statement (manifest p1b-blind-shortcut-detection). No prior science number changed. Recompile 4-pass clean: 0 undef refs, max overfull 3.6pt, 8pp.",
  sitePdfPath: "/papers/paper1b_namaster_proof_v2B.0.17.pdf",
});
console.log("Inserted:", result);
