// P1A v1A.0.45 — TIER A #A1 Holst→Pontryagin closure
// Long-form slug per tools/README_convex_bump_slug_convention.md
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1a",
  version: "v1A.0.45",
  datestamp: "2026-06-08",
  texCommit: "49d18fe2",
  pdfMd5: "bcc627abd2d0b9d3047896cc8cecf0ce",
  pdfPages: 21,
  pdfSizeBytes: 847895,
  sitePdfPath: "/papers/paper1a_ech_nogo_v1A.0.45.pdf",
  changelog:
    "TIER A #A1 closure — Holst→Pontryagin mathematical error CORRECTED at 4 sites. The prior claim that the Holst dual contraction ε^μνρσ R_μνρσ 'reduces on the Levi-Civita connection to the Pontryagin density ∝ R∼R as a total derivative' conflated two distinct objects: the Pontryagin density has TWO curvatures (a separate true topological invariant), the Holst dual contraction has ONE curvature and on T=0 vanishes IDENTICALLY by the first (algebraic) Bianchi identity R_μ[νρσ]=0. Replaced at abstract L327, transparency §X.B step-4, explicit-verification §X.B-bis, executive summary. Footnote added documenting the differential-form decomposition e∧e∧R = -NY + T∧T (Nieh-Yan + torsion-squared; both vanish at T=0). Headline perturbation-transparency conclusion (Holst sector decouples from all scalar/tensor EOM) preserved via the Bianchi-trivial argument rather than the (incorrect) Pontryagin-total-derivative argument. Caught by fire-13 + fire-15 META-reviewer (gpt-5-pro), pre-bump detector tools/v3_pattern040_cross_section_check.py reproduces mechanically in <1s. PDF 21pp/847KB/md5 bcc627ab. Compile: 0 undef refs, 4 carry-over overfulls (1.7-152pt, none introduced). Readiness rolled BACK 95→92 per feedback_readiness_oscillation (mathematical-error fix is non-trivial enough to warrant a step-down).",
});
console.log("Inserted:", result);

console.log("\n--- verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
