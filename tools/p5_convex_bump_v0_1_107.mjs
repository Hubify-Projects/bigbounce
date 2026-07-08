import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p5",
  version: "v0.1.107",
  datestamp: "July 7, 2026",
  texCommit: "b42644c8",
  pdfMd5: "1b569055e7ae4fe0859711f6a148d762",
  pdfPages: 39,
  pdfSizeBytes: 1477610,
  changelog:
    "FULL8 EXT closure (2026-07-08): closed all Grok+Gemini MINORs + ChatGPT editable MAJORs. " +
    "Abstract headline scoped to DESIVAST void/non-void contrast + post-hoc caveat + family-wise emphasis. " +
    "Conclusions: post-hoc pre-registration caveat + family-wise Bonferroni-5 prominent. " +
    "DESIVAST RSD para: added quantitative membership-shift bound (~1.3x MC max shift needed to exit 0.5-0.6pp window). " +
    "Bright/dark sign-flip: residual-ambiguity flag made unmissable (no mock reproduces exact amplitude). " +
    "Data availability: explicit Zenodo-pending + per-artifact GitHub pin for DESIVAST-join parquet + T-Web grid + sweep configs. " +
    "VI.D: added mechanistic BGS-photometric-selection->ViT propagation explanation. " +
    "Limitations Paper IV: explicit coordinated-co-review / acceptance-conditional framing + env-stratified confusion-matrix scope limitation. " +
    "DESIVAST primary: void membership definition caveat (PIS union as permissive proxy) made unmissable with 3-variant cross-check summary. " +
    "Discussion: T-Web status bold block = failed/diagnostic secondary, not load-bearing. " +
    "App toy_eft: speculative/outside-empirical-result scope disclosure added. " +
    "ZERO verified numbers changed. Recompile 0 undef 0 overfull (39 pp). Standalone-verified.",
  sitePdfPath: "site/public/papers/p5-chirality.pdf",
  arxivTarballPath: "submissions/P5/arxiv_p5_v0.1.107.tar.gz",
});
console.log("P5 v0.1.107 inserted:", result);
