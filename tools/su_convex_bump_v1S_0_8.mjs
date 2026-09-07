import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const bump = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-su",
  version: "v1S.0.8",
  datestamp: "2026-09-07",
  texCommit: "379526ae",
  pdfMd5: "87bda8d5faf08102b621a3ea1755d233",
  pdfPages: 6,
  pdfSizeBytes: 446055,
  sitePdfPath: "/papers/paper_su_criterion_v1S.0.8.pdf",
  changelog: "A2 lapse-monopole gap reconciled per independent adjudication (research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md). S9's constraint solve A2=eps(3-eps)^2/3 stands as correct (not 2(3-eps)^2). The uniform-density-surface squeezed monopole is f^rho_NL=5(eps-7)/8=-55/16 at eps=3/2 -- the earlier initial-label figure 5(2eps-15)/24=-5/2 came from composing the threading map with the linear-mode weight lambda'=2lambda where the rho-surface time shift, acting on the second-order curvature perturbation, instead carries weight 3lambda; correcting the weight closes the gap 5(6-eps)/24 exactly. An independent exact separate-universe solution reproduces both -55/16 (uniform-density) and -5 (comoving) for all eps from the same ADM monopole equations, so the in-in monopole -15/8, the comoving delta-N -5, and the uniform-density delta-N -55/16 are three well-defined variables related by exact threading maps, not competing claims. No new math; Appendix A composition step corrected in place. Directive G: 4-pass pdflatex, 0 undefined refs, max overfull hbox 8.3pt. Three-way md5 87bda8d5faf08102b621a3ea1755d233 (fresh compile == site/public/papers == public/papers), 6 pages. arXiv tarball rebuilt, standalone smoke-compiled clean (0 undef refs). Readiness 65 -> 70. Rounds stopped; next step is venue.",
});
console.log("paperVersions.bump:", bump);

const activity = await client.mutation(api.activityFeed.add, {
  type: "paper-update",
  date: "2026-09-07",
  title: "paper-su v1S.0.8 -- A2 monopole gap reconciled",
  body: "Independent adjudication (a2_lapse_monopole_adjudication_2026_09_07.md) resolves the A2/f^rho dispute: A2=eps(3-eps)^2/3 correct, f^rho=5(eps-7)/8=-55/16 at dust, composition weight 3lambda not 2lambda. In-in monopole -15/8, comoving delta-N -5, uniform-density delta-N -55/16 now stated as three reconciled variables. Readiness 65 -> 70.",
  tags: [{ label: "paper-su", kind: "paper" }, { label: "v1S.0.8", kind: "version" }],
});
console.log("activityFeed.add:", activity);

const cap = await client.mutation(api.papers.setReadinessCap, { slug: "paper-su", cap: 70 });
console.log("setReadinessCap:", cap);
