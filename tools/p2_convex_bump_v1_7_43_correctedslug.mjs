// P2 v1.7.43 bump — REDO with corrected paperSlug ("paper-2" not "p2").
// The original tools/p2_convex_bump_v1_7_43.mjs wrote to paperSlug "p2"
// which is NOT what convex/papers.ts:249 listAllPaperStates reads
// (it queries by papers.slug = "paper-2"). Same bug as the
// post_loadbearing_convex_bump_2026-06-08.mjs found 2026-06-08.
//
// This re-bump pushes the same v1.7.43 metadata to the correct slug so the
// homepage Paper State table updates from v1.7.42 -> v1.7.43.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.43",
  datestamp: "2026-06-03",
  texCommit: "f1d312483f38a1a64dea1d19716bdc81bd8309a3",
  pdfMd5: "6ca34e3b0e5ca6447920d11f7a4ecb9e",
  pdfPages: 23,
  pdfSizeBytes: 826517,
  sitePdfPath: "/papers/paper2_fnl_forecast_v1.7.43.pdf",
  changelog:
    "R9 GEM-M1 closure: closure-introduced math regression fix. v1.7.42 GEM-m1 closure had ADDED an incorrect 'exactly 6 S_3-symmetric orbits' justification at L225 (12 orbits exist mathematically). R3-R8 (32 reviewer passes) missed it because the closure fabricated rather than verified. Path-A fix: demoted phrasing from 'complete S_3-symmetric basis' to 'Cai-physics-restricted subset' — the 6 monomials are the non-zero-coefficient orbits in Cai et al. Eq.~37 vertex-level derivation; the 6 omitted orbits (8,1,0),(7,1,1),(6,2,1),(5,3,1),(4,4,1),(3,3,3) carry zero coefficient under the matter-bounce vertex selection rules. New review-pattern candidate: closure-fabricates-math-justification. Readiness oscillates 99 -> 95 per readiness-oscillation directive. Counter resets 3/3 -> 0/3.",
});
console.log("Inserted:", result);

// Verify
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
