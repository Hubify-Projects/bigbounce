import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-a3m",
  version: "v3M.0.14",
  datestamp: "2026-09-04",
  texCommit: "a2bf84739a14529bc12533ceb03c8c9ab5cb77f4",
  pdfMd5: "de167ede0c3aa1ea31ded3fe9437fd82",
  pdfPages: 15,
  pdfSizeBytes: 722223,
  changelog: "R6 closure (16 genuinely-new real, 0 physics errors): T_B mapping recomputed from committed JSON (10^8-10^10 GeV/eleven decades -> 6e9-6e10 GeV/thirteen decades); Channel I NANOGrav amplitude paired to the free-gamma posterior (shortfall 10^14.3->10^15.2), Fig.1 regenerated; abstract calibrated to body (P+B separation vs bare significance, SMBH FIRAS-vs-model split, two distinct S1/S2 scheme values not a band, PBH ratio conditionality); PTA sigmas labelled Gaussian-equivalent z-distances; DESI DR1 v3 reproduction sentence added to Sec VI (f_NL=-2.2+-25, 0.06sigma from published, too weak to separate candidates); minor fixes (sign inversion, version-history prose, S2 cubic-only clarification, sentence fragment, Table VI upper-bound caption). Rounds stopped under directive R2; open science items (A3-4 r-derivation, Choudhury sign, n_s shift, delta-N mechanism, DESI wide-angle) moved to NEXT_SCIENCE_LEDGER.md.",
});
console.log("Inserted:", result);
