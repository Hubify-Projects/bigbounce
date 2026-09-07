import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const bump = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-a3m",
  version: "v3M.0.24",
  datestamp: "2026-09-07",
  texCommit: "0c7048c7",
  pdfMd5: "b29ebb90be09f8d0bbc3875647bb150a",
  pdfPages: 19,
  pdfSizeBytes: 766084,
  sitePdfPath: "/papers/a3_multichannel_arxiv_v3M.0.24.pdf",
  changelog: "A2 lapse-monopole gap reconciled per independent adjudication (research/theory_audit/a2_lapse_monopole_adjudication_2026_09_07.md). Sec. II and Appendix A: the earlier 'not reconciled / open item' wording on the uniform-density f^rho gap is replaced. A2=eps(3-eps)^2/3 stands as the correct constraint-solve value (not 2(3-eps)^2). The uniform-density delta-N value is f^rho=5(eps-7)/8=-55/16 at dust, obtained by correcting the composition weight on the second-order curvature perturbation from lambda'=2lambda to 3lambda; this closes the 15/16 gap to the earlier initial-label figure -5/2 exactly. The in-in monopole -15/8 (delta N_c normalization), the comoving-slice delta N value -5, and the uniform-density delta N value -55/16 are now stated as three well-defined variables related by exact threading maps, not competing claims. The flagship in-in monopole -35/16 (Maldacena normalization) is unaffected; no new math introduced. Directive G: 4-pass pdflatex, 0 undefined refs, max overfull hbox 3.9pt. Three-way md5 b29ebb90be09f8d0bbc3875647bb150a (fresh compile == site/public/papers == public/papers), 19 pages. arXiv tarball rebuilt, standalone smoke-compiled clean (0 undef refs, 19pp). Readiness held at 75. Rounds still stopped (directive R2).",
});
console.log("paperVersions.bump:", bump);

const activity = await client.mutation(api.activityFeed.add, {
  type: "paper-update",
  date: "2026-09-07",
  title: "paper-a3m v3M.0.24 -- A2 monopole gap reconciled",
  body: "Independent adjudication (a2_lapse_monopole_adjudication_2026_09_07.md) resolves the A2/f^rho dispute in Sec. II and Appendix A: A2=eps(3-eps)^2/3 correct, f^rho=5(eps-7)/8=-55/16 at dust via the 3lambda (not 2lambda) composition weight. In-in -15/8, comoving delta-N -5, uniform-density delta-N -55/16 now stated as three reconciled variables. Readiness held at 75.",
  tags: [{ label: "paper-a3m", kind: "paper" }, { label: "v3M.0.24", kind: "version" }],
});
console.log("activityFeed.add:", activity);
