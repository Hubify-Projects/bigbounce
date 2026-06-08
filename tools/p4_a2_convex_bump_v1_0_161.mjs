// P4 v1.0.161 — TIER A2 #A2 footnote regression closure
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-4",
  version: "v1.0.161",
  datestamp: "2026-06-08",
  texCommit: "ea9d8f07",
  pdfMd5: "5c3b834aaf9be5958f5e1475c7cbff72",
  pdfPages: 11,
  pdfSizeBytes: 466226,
  sitePdfPath: "/papers/chirality_catalog_paper_v161.pdf",
  changelog:
    "TIER A2 #A2 closure — §IV.D fn:binomial_nspiral footnote regression I introduced in v1.0.160 is CLOSED. The wrong claim ('mode-coupling decoupling absorbs trial-count for pre-MASTER pseudo-Cℓ; expected sub-0.1σ effect') was internally inconsistent because mode-coupling decoupling is a POST-MASTER operation and cannot affect a PRE-MASTER (masked) statistic by definition. Replaced with honest empirical-rerun framing: the per-pixel trial-count inflation factor ⟨N_all/N_spiral⟩ ≈ 1.49 propagates directly into the binomial variance of the per-pixel CW-count draws and hence into the null-distribution variance of the pre-MASTER pseudo-Cℓ; the size of the shift in the headline 99.3% reproduction figure and the +1.68σ residual is NOT analytically predictable from a pre-MASTER pseudo-Cℓ statistic and will be reported empirically when the N(p)_all rerun completes. Headline qualitative conclusion preserved as robust to trial-pool choice; quantitative 99.3% is specific to the N_spiral draw. Caught by fire-14 P4-META-E3 + tools/v3_pattern040_cross_section_check.py. After this fix, pattern-040 detector sweep-clean across ALL 6 papers (0 flagged contradictions across the entire corpus). PDF 11pp/466KB/md5 5c3b834a. Compile clean (0 undef refs).",
});
console.log("Inserted:", result);

console.log("\n--- verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
