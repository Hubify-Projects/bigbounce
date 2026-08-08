// P1A v1A.0.114 — Fierz-by-Fierz projection lemma PROVEN (completeness major closure)
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1a",
  version: "v1A.0.114",
  datestamp: "July 7, 2026",
  texCommit: "b875807a",
  pdfMd5: "37de050aa00bfdedfa23837efce07af7",
  pdfPages: 38,
  pdfSizeBytes: 1812640,
  arxivTarballPath: "submissions/P1A/arxiv_p1a_v1A.0.114.tar.gz",
  sitePdfPath: "/papers/paper1a_ech_nogo_v1A.0.114.pdf",
  changelog:
    "Fierz-by-Fierz projection lemma PROVEN + machine-verified (arxiv/scripts/fierz_lemma_check.py -> LEMMA PROVEN) and applied: closes the 'completeness asserted, not proven' MAJOR at the M_Pl-power-counting-class level the paper claims. New appendix states the 5x5 Fierz matrix from explicit Dirac gammas (matches Itzykson-Zuber/Nieves-Pal hep-ph/0306087, F^2=1), the closure table (AA -> 1/4 SS + 1/2 VV - 1/2 AA - 1/4 PP; VV symmetric; VA within {V,A}), zero escape classes, all coeffs dimensionless rationals => kappa=M_Pl^-2 preserved term-by-term => single-scale NDA ceiling bounds the entire finite minimal-ECH tower. 8 body/abstract/conclusion sites upgraded 'left to follow-up' -> 'proven in App. Fierz'. Honest residual scope KEPT: single-species minimal ECH proven; multi-flavor + non-minimal completions remain the STATED no-go boundary (no overclaim). No quantitative number changed. Recompile 0 undef-refs, 0 overfull>50pt, 38 pages; mirrored byte-identical to all served paths; bundle rebuilt + standalone-verified.",
});
console.log("Inserted:", result);

console.log("\n--- verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
