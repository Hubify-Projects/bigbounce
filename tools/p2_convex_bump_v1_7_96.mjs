// P2 v1.7.96 bump — DATA-UNLOCK: named Cov_B external gate strengthened (Heinrich 2023 covariance not publicly released).
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.96",
  datestamp: "July 6, 2026",
  texCommit: "2322b57a8dddad3893363847b984a02ceb97774e",
  pdfMd5: "4b1adf9caa4f55752bddb133de9e3f5e",
  pdfPages: 34,
  pdfSizeBytes: 995575,
  arxivTarballPath: "submissions/P2/arxiv_p2_v1.7.96.tar.gz",
  arxivTarballSizeBytes: 420622,
  sitePdfPath: "/papers/paper2_fnl_forecast_v1.7.96.pdf",
  changelog:
    "DATA-UNLOCK: strengthened the named Cov_B external gate in sec:systematics with one sentence. A systematic availability search (arXiv ancillary files, Zenodo, authors' public code repositories) confirms the Heinrich et al. 2023 per-triangle SPHEREx multi-tracer bispectrum covariance Cov_B is NOT publicly released: no data/code-availability statement, no arXiv ancillary, no Zenodo DOI; the only public generating code (github.com/chenheinrich/SphereLikes) is an unvalidated pre-publication WIP branch ('[Not validated; under construction]', last pushed 2021, no paper-matching release, no per-triangle Cov_B). Therefore the computed-degeneracy bracket with the rho=-0.868 proxy is the best currently-constructible estimate of the marginalized floor. Record: project-context/peer-reviews/INT_v3/DATA_UNLOCK_2026-07-05.md (Item 4). NO headline/f_NL/sigma number changed; -35/16 UNCHANGED; documented external-data non-availability, nothing fabricated. Recompile clean (0 undef-refs, 0 overfull, 34 pages); arXiv tarball rebuilt (420KB) + smoke-recompiled clean.",
});
console.log("Inserted paper-2:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-2" });
console.log("Latest paper-2:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
