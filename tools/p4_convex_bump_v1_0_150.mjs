import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p4",
  version: "v1.0.150",
  datestamp: "2026-06-03",
  texCommit: "PENDING_COMMIT_SHA",
  pdfMd5: "9722ff36d26f53ad9b6cf1905ad43268",
  pdfPages: 55,
  pdfSizeBytes: 26255923,
  changelog:
    "R9 P4 triage cosmetic bibkey re-tag. Two bibitem keys renamed to match published-year metadata inside the entries: Philcox:2023 -> Philcox:2022 (PRD 106 063501 (2022), arXiv:2206.04227); Cahn:2021 -> Cahn:2023 (PRL 130 201002 (2023), arXiv:2110.12004). Bibliography ENTRIES (author list, title, journal, page, arXiv) unchanged - only the \\bibitem{} keys were renamed. All inline \\cite{Philcox:2023} and \\cite{Cahn:2021} sweeps applied across the manuscript. Zero numerical / methodological / scientific change. 0 undef cites. Cap 95% held per feedback_99_pct_readiness_cap.",
});
console.log("Inserted:", result);
