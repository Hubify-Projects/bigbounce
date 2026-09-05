import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.activityFeed.add, {
  type: "r-round",
  date: "2026-09-04",
  title: "A3M v3M.0.16 — R7 truth-audit closure (16 items), rounds STOPPED under directive R2",
  body: "Closed all 16 genuinely-new-real items from the R7 truth-audit (0 physics errors beyond scoping/staleness): S2 tensor-transfer scoping (r_after[S2]~=9.4e2, worse not cured), a stale Fig. 1 legend (superseded NANOGrav amplitude A=2.4e-15 vs the current A=6.46e-15, regenerated and re-mirrored), the c_s sign-flip at 0.8876 disclosed, the Delta f_NL^bounce omission disclosed, the CaiXue2011 bib entry rebuilt from arXiv:1101.0822, Table V non-perturbative-branch labelling, a stale NANOGrav-amplitude cross-reference reconciled (10^6.2 not 10^5.3), version-history/open-item prose removed (3rd recurrence), a false QCD/baryogenesis claim deleted, the Cai shape-conversion wording and monomial-reading qualifier fixed, and Appendix A's 'translation coincidence' replaced with the label-resolved change-of-variable statement. Two reviewer MAJORs (Grok REJECT, Gemini MAJOR) rested substantially on findings falsified against committed artifacts. This is the 4th consecutive verification round on A3M (directive R2): rounds now STOP pending a science decision on the (ii) ledger (A3-S2r, A3-cs-bounce, A3-ns, A3-dN, DESI-4). Directive G hygiene: 4-pass recompile, 0 undef refs, 0 overfull hbox >10pt, three-way md5 5544bea1 verified, tarball rebuilt (sha256 69d9178f) and standalone smoke-compiled.",
  tags: [
    { label: "A3M", kind: "paper" },
    { label: "v3M.0.16", kind: "version" },
    { label: "R7", kind: "review-round" },
  ],
});
console.log("Inserted:", result);
