import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const bump = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1n",
  version: "v1N.0.6",
  datestamp: "2026-09-18",
  texCommit: "9bd3c7cf", // parent commit at write time; this lane's own commit follows immediately after
  pdfMd5: "b9ac109139b7d88aa0f798ee7ef80c8d",
  pdfPages: 11,
  pdfSizeBytes: 433655,
  sitePdfPath: "/papers/paper1bc_ech_note_v1N.0.6.pdf",
  changelog: "D-round (visual) + P-round (packaging) complete, lane L3 of the 2026-09-18 publication-push campaign. D-round: fresh 4-pass recompile (0 undef refs, 1 pre-existing 4.5pt residual overfull hbox under the >10pt gate), all 11 pages rendered and visually spot-checked -- no overflow. P-round: /artifact-link-verify found 0 broken links (8 pinned GitHub blob links + 1 tree link resolve at commit ded46bc5, 3 self-citation Zenodo DOIs + repo root return HTTP 200); /bib-tarball-rebuild caught and fixed a genuine defect -- references.bib carried one orphaned unused entry (Weinberg1989, left over from the DP1N-47 citation removal) -- deleted, now exactly 30 cited == 30 bib == 30 bbl. arXiv tarball rebuilt from scratch and standalone-smoke-tested (0 undef refs, 11pp, clean extract to a fresh temp dir). Submission kit assembled (CQG_SUBMISSION_KIT_P1N_2026-09-18.md): ORCID (D5) re-verified public HTTP 200, no placeholder needed; arXiv gr-qc endorsement (D4) remains Houston-only open item, not a CQG-submission blocker. SSOT reconciled: status.md and DISPOSITIONS/P1N.md had been left at v1N.0.4/v1N.0.2 headers despite the tex already being at v1N.0.5 (a prior session's abstract-trim closing DP1N-57 was never written back to SSOT) -- both now current. No science content changed at v1N.0.5 or v1N.0.6.",
});
console.log("paperVersions.bump:", bump);

const activity = await client.mutation(api.activityFeed.add, {
  type: "r-round",
  date: "2026-09-18",
  title: "paper-1n v1N.0.6 -- D-round + P-round complete, SSOT reconciled",
  body: "Lane L3 (publication-push campaign): D-round visual audit clean (0 undef refs, 1 pre-existing sub-gate overfull hbox, 11 pages spot-checked). P-round packaging verified: 0 broken artifact links; bib-tarball-rebuild caught + fixed one orphaned unused .bib entry; arXiv tarball rebuilt and standalone-smoke-tested clean. CQG submission kit assembled; ORCID public-status D5 gate resolved; arXiv gr-qc endorsement D4 remains Houston-only. Readiness ladder: R(96)->D(98)->P(99).",
  tags: [{ label: "paper-1n", kind: "paper" }, { label: "v1N.0.6", kind: "version" }, { label: "campaign-2026-09-18", kind: "campaign" }],
});
console.log("activityFeed.add:", activity);

const cap98 = await client.mutation(api.papers.setReadinessCap, { slug: "paper-1n", cap: 98 });
console.log("setReadinessCap 98:", cap98);
const cap99 = await client.mutation(api.papers.setReadinessCap, { slug: "paper-1n", cap: 99 });
console.log("setReadinessCap 99:", cap99);

const state = await client.query(api.papers.getPaperState, { slug: "paper-1n" });
console.log("final state:", JSON.stringify({
  readinessCap: state.readinessCap,
  readinessComputed: state.readinessComputed,
  currentVersion: state.currentVersion,
}, null, 2));
