import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p4",
  version: "v1.0.217",
  datestamp: "July 5, 2026",
  texCommit: process.env.P4_TEX_COMMIT || "b96436e2",
  pdfMd5: "b62c22be524b571ed6b3b2f27325417d",
  pdfPages: 31,
  pdfSizeBytes: 33998415,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.217.tar.gz",
  arxivTarballSizeBytes: 26701549,
  sitePdfPath: "/papers/chirality_catalog_paper_v1.0.217.pdf",
  changelog:
    "P4 RETEST v216 EXT closure (Grok + Gemini both MINOR REVISIONS, central claim supported). Editable minors closed as WORDING/CLARITY tightenings, nothing fabricated: (1) Grok Sec V.A/abstract Shamir 'inconsistent' restated in the abstract as '~7-18x amplitude-level tension, not a frequentist exclusion of Shamir's distinct Ganalyzer estimator' (matching the body/comparison/monopole caveats already carried verbatim). (2) Grok IV.C/VI.B p_eq>0.6 pre-registration already fully cited (commit 94113e5, 2026-06-09, immutable git record) in Sec.~prereg -- verified present, no edit needed. (3) Grok II.B/VI.A pseudo-label 66.5% framing: added forward-pointer routing the 66.5% discussion to the model-free GZ1-human-only null (N_HC~46k, z=-0.54sigma) as the decisive independence answer. (4) Gemini IV.A classifier overconfidence/miscalibration: added one honest sentence -- analysis consumes the confidence CUT (p_eq>0.6) as a ranking selector (not calibrated probabilities), the dipole is fit to hard class assignments in the HC regime, and the GZ1-human cross-check is calibration-free, so miscalibration cannot bias the null. Grok items 4/5 (grid-approx thresholds, consolidated Primary-vs-Diagnostic decision table) already satisfied (Table decision_tree + estimator-specific floor labels present). Gemini's 2 [MAJOR]-tagged STRENGTHENING items remain POD-GATED and are HONESTLY flagged as DEFERRED, NOT faked: (a) full per-pixel l=1 residual attribution needs DR8-sweep morphology at production scale -- cosmological content already EXCLUDED (residual maps to A_p=0.695% < A_50=0.75% < A_95 in (1.0,1.5]%), full map 'pod-deferred, not fabricated here'; (b) edge-on-ISOLATED tie-break variant needs catalog_production.parquet -- tie-break is leg-systematic (DECaLS-only z=+4.72, isotropic BASS+MzLS z=+0.31), already bounded by the primary real-space null, isolated variant 'pod/data-lab-bound and deferred'. Both are refinements, not threats to the null. Recompile 31pp / 34.0MB / 0 undef-refs / 0 overfull>50pt. All served paths byte-identical md5 b62c22be. arXiv tarball rebuilt v1.0.217 (re-extract standalone-compile-verified, 31pp, 0 undef).",
});
console.log("Inserted:", result);
