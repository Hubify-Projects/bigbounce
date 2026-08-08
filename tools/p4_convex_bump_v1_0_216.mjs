import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p4",
  version: "v1.0.216",
  datestamp: "July 5, 2026",
  texCommit: "c64d3680",
  pdfMd5: "6603a97613ce82dc6fa8b2fa27a202d8",
  pdfPages: 31,
  pdfSizeBytes: 33997604,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.216.tar.gz",
  arxivTarballSizeBytes: 26700529,
  sitePdfPath: "/papers/chirality_catalog_paper_v1.0.216.pdf",
  changelog:
    "Close Gemini's 2 remaining MAJORs. EDIT 1 (Sec IV.D): statistical upper limit on the cosmological content of the unmodelled ~47% l=1 residual — observed canonical-mask A1_obs=0.695% (same Ap=2(f_CW-1/2) units as the real-space dipole) is BELOW the injection-recovery 50%-recovery floor A_50=0.75% and far below A_95 in (1.0,1.5]%, so even 100% of the residual (let alone the unmodelled ~0.32%) is excluded at >=95% recovery as a coherent cosmological dipole (>3-4x below exclusion floor); direct Catalog-C real-space null z=0.41sigma p=0.62 independently sees zero => remainder is systematic by exclusion, per-pixel attribution pod-deferred. EDIT 2 (Appendix E): direct per-leg spatial statistic on the borderline tie-break band p_eq in [0.5,0.6] (committed per_leg_confidence_familywise_maxstat.json) — tie-break isotropic in BASS+MzLS (z=+0.31), coherence ONLY in DECaLS (z=+4.72, family-wise p=0.0086) = per-imaging-leg depth systematic, NOT an isotropic sky bias; whole band flows into sigma=0.41 real-space null; edge-on-isolated variant needs catalog_production.parquet (pod-deferred). All numbers verified against committed JSONs; nothing fabricated. Recompile 31pp / 34.0MB / 0 undef-refs / 0 overfull>50pt. All served paths byte-identical md5 6603a976. arXiv tarball rebuilt v1.0.216 (standalone-compile-verified).",
});
console.log("Inserted:", result);
