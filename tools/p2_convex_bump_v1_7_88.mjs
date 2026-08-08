// P2 v1.7.88 bump — honest in-in re-derivation strengthening + Li 2017 miscite fix.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.88",
  datestamp: "July 4, 2026",
  texCommit: "8a573b5ff2174b46f1e5ce32e5a976533fea168d",
  pdfMd5: "b64df50f7c1b1f14f0668923465a2a3a",
  pdfPages: 31,
  pdfSizeBytes: 959692,
  sitePdfPath: "/papers/paper2_fnl_forecast_v1.7.88.pdf",
  changelog:
    "BOUNDED honest in-in re-derivation strengthening (factor-of-2 NOT resolved). Four-vertex in-in re-derivation (INT_v3/P2_inin_rederivation_2026-07-04.md) confirmed the Cai/Li fNL=-35/8 vs -35/16 factor-of-2 is genuinely unresolvable from the published polynomials, and independently refuted the retracted single-time-ordering story: Li's own Eq (4.13) is written -2x2 Im (full in-in, both orderings). Appendix A opening: added one sentence citing Li Eq (4.13)'s -2x2 Im as the POSITIVE refutation of the dropped-time-ordering mechanism; factor-of-2 still disclosed as unresolved, -35/8 adopted, -35/16 robustness branch retained, not claimed resolved. Miscite fix: bibkey CaiBrandenberger:2014 -> LiQuintin:2017 (Li, Quintin, Wang & Cai 2017, JCAP 03:031, arXiv:1612.02036); all 8 body cites renamed. NO numbers changed, NO math fabricated. Recompiled 0 undef-refs, 0 overfull >50pt.",
});
console.log("Inserted:", result);
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
