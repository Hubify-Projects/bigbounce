import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p3",
  version: "v3.1.73",
  datestamp: "2026-06-03",
  texCommit: "PENDING_COMMIT_SHA",
  pdfMd5: "ac627bd88f7cd6c968daf6137b65db07",
  pdfPages: 50,
  pdfSizeBytes: 28463591,
  changelog:
    "R9 P3 triage bib-hygiene polish (PER-M1, PER-m1, PER-m2, PER-n1; all VERIFIED bib hygiene per peer-review-truth-audit). Added 4 bib entries cited inline in §pathc_caveats(e): Yoo+2009 (arXiv:0907.0707, PRD 80 083514); Bonvin & Durrer 2011 (arXiv:1105.5280, PRD 84 063505); Challinor & Lewis 2011 (arXiv:1105.5292, PRD 84 043516); Di Dio+2013 (arXiv:1307.1459, JCAP 11 044). Converted §pathc_caveats(e) prose mentions to explicit \\cite{} commands. Added arXiv:0903.0631 to Cai:2009fn entry. Expanded Foreman-Mackey to Publ. Astron. Soc. Pac. 125, 306-312 (2013) with arXiv:1202.3665 [astro-ph.IM] tag. Standardized Heinrich2023 with explicit JCAP 2024 074 + publication-year note (bibkey retained for arXiv-submission-year continuity). Zero content changes; bib hygiene only. Cap 95% held per feedback_99_pct_readiness_cap.",
});
console.log("Inserted:", result);
