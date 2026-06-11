import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p4",
  version: "v1.0.151",
  datestamp: "2026-06-04",
  texCommit: "79a37c28",
  pdfMd5: "18b4adf5b63c1fe09350280884ac95ff",
  pdfPages: 57,
  pdfSizeBytes: 26278202,
  sitePdfPath: "/papers/chirality_catalog_paper_v151.pdf",
  changelog:
    "R-EXT 3-vendor external review closure on v1.0.149 (ChatGPT REJECT / Gemini MINOR / Grok MAJOR). Truth-audited per feedback_peer_review_truth_audit_protocol. 6 convergent BLOCKERs closed Path A: (a) ~18sigma formal-exclusion overclaim softened to 'strongly disfavoured under the adopted template model at >99% confidence' + bootstrap-covariance-scale caveat + NSIDE block-size sensitivity deferred (ChatGPT-B2+Gemini-B+Grok-B-GR-2). (b) Mask hierarchy honestly labelled 'declared after first catalogue results' rather than 'pre-specified' + subsample-mask predicate equation added (ChatGPT-B3+Grok-B-GR-1). (c) Canonical-residual decomposition table added: pre-MASTER 99.3% / post-MASTER 12% monopole / 88% depth-morphology with leg-as-proxy 25% partial closure (ChatGPT-B4+Grok-B-GR-3). (d) Sensitivity-budget consolidated table: 0.29 / 0.50 / 0.75 / 1.19 percent (ChatGPT-B6+Gemini-B). (e) Shamir ~2.5x / ~3% shorthand REMOVED (ChatGPT-B8+Grok-B-GR-4). (f) Journal-clean sweep: dupes, all-caps 'FORMALLY EXCLUDED', internal audit IDs, 'queued' placeholders all fixed (ChatGPT-B9+minors). Release-tag macro paper4-v1.0.145 -> paper4-v1.0.151 globally. New section sec:open_followups delineates 3 deferred analyses (NSIDE block-size sensitivity, full DR8-sweep template regression, fully specified spatial likelihood). PDF 57pp/26.28MB/0 undef refs. 7 mirrors byte-identical. Readiness P4 rolled BACK 95->92 per feedback_readiness_oscillation; headline subsample-mask null at -0.12sigma unchanged. Cap restored to 95% only after clean cross-vendor R-round at v1.0.151. Final 1% remains Houston sign-off per feedback_99_pct_readiness_cap.",
});
console.log("Inserted:", result);
