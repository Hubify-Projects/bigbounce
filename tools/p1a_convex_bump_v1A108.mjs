// P1A v1A.0.108 — INT-flagged internal-consistency reconciliation (ROUND_2026-07-05)
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1a",
  version: "v1A.0.108",
  datestamp: "July 5, 2026",
  texCommit: "50b9db50",
  pdfMd5: "709eb3507c2bd90e92ff8383daf2cb95",
  pdfPages: 37,
  pdfSizeBytes: 1784981,
  arxivTarballPath: "arxiv/paper1a_arxiv_v1A.0.108.tar.gz",
  sitePdfPath: "/papers/paper1a_ech_nogo_v1A.0.108.pdf",
  changelog:
    "INT review (v107, ROUND_2026-07-05, Claude Code full-source leg — verdict MINOR) flagged three REAL internal inconsistencies from the fast v106/v107 edits; reconciled with NO physics/number changes. MINOR-1: abstract Scope de-synced from body — it still deferred the Jackiw-Pi gravitational Chern-Simons term and the parity-odd four-fermion partner to a follow-up while the v107 body closes both explicitly; abstract now states both are closed in-body, covered by the completeness argument. MINOR-2: completeness paragraph ('basis-complete within minimal ECH') directly contradicted the residual-scope paragraph 260 lines later ('do NOT claim operator-level closure'); harmonized — the basis IS power-counting-class complete WITHIN MINIMAL ECH via F1 (algebraic non-propagating torsion) + F2 (totally-antisymmetric axial spin current) + NDA monotonicity, the sole residual open item is the explicit Fierz-by-Fierz projection lemma, and genuine operator-level escape requires a NON-minimal completion (new light scale mu<<M_Pl or exact cancellation) = the stated scope boundary. MINOR-3: NDA class-blind monotonicity caveat stated once — it is an NDA-coefficient statement assuming no anomalously-enhanced higher-dimension Wilson coefficient (true under single-scale NDA). Recompile 4-pass + bibtex: 0 undefined refs/cites, 0 overfull hbox >50pt, 37pp/1.78MB/md5 709eb350. arXiv bundle v1A.0.108 rebuilt + standalone-smoke-tested (37pp, 0 undef).",
});
console.log("Inserted:", result);

console.log("\n--- verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
