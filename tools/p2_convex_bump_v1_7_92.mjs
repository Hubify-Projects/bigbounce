// P2 v1.7.92 bump — non-local-tails MAJOR closed (standard-basis template decomposition).
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.92",
  datestamp: "July 5, 2026",
  texCommit: "ac79230a122c5d46bbe0b7deee2015ace0b7fd0d",
  pdfMd5: "ea1f79805fd0390aba15caddc3b47ddf",
  pdfPages: 34,
  pdfSizeBytes: 988592,
  arxivTarballPath: "project-context/SSOT/arxiv_tarballs/paper2_arxiv_v1.7.92.tar.gz",
  arxivTarballSizeBytes: 419264,
  sitePdfPath: "/papers/paper2_fnl_forecast_v1.7.92.pdf",
  changelog:
    "INT-v3 verified-real-science: closed the non-local-tails reviewer MAJOR ('the r=0.84 local-template recast does not model the NON-LOCAL bounce-shape tails; equilateral/orthogonal deviations could carry missed signal') with a standard-basis template-decomposition paragraph in sec:template. The PHYSICAL bounce bispectrum B_bounce = BNL(k) x S_local(k) (carrying the local 1/k^3 envelope, ~97% local) is projected onto the Senatore-Smith-Zaldarriaga local/equil/ortho basis on the identical committed 23,098-triangle grid, reproducing the paper's r_cos = 0.985 exactly (-0.9849). Uniform-weight cosines: LOCAL -0.985, EQUIL -0.45, ORTHO +0.94. A JOINT projection onto span{LOCAL,EQUIL,ORTHO} raises the recovered Fisher-norm fraction from 0.970 (local-only) to at most 0.974 => delta r <= +0.002 (<0.3% of the r=0.84 headline, << the +/-0.02 uncertainty), so the single-local-template recast is ROBUST and multi-template analysis is NOT needed. Two honest points stated: (1) the projection is of the physical bispectrum (local envelope), not the bare BNL ratio; (2) the high ORTHO cosine is COLLINEARITY (ortho template == -3*local + ...), not independent signal - the joint fit removes the double-counting. Honest scope limit kept: geometry-only shape overlap (matching r_cos); the full 3D estimator-mismatch variance under the true SPHEREx multi-tracer bispectrum Fisher covariance is not computed here (needs the Heinrich et al. noise covariance). NO headline number changed. Added Senatore:2010 (arXiv:0905.3746) to focused_paper_refs.bib; cited c11_nonlocal_template_projection.py/.json. Recompile clean: 0 undef-refs, 0 overfull >50pt, 34 pages, arXiv tarball smoke-recompiled clean. Nothing fabricated - exact numbers from the committed c11 script/JSON.",
});
console.log("Inserted:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-2" });
console.log("Latest paper-2:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
