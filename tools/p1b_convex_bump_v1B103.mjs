import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1b",
  version: "v1B.0.103",
  datestamp: "July 7, 2026",
  texCommit: "103a81cf",
  pdfMd5: "3d14c2a11e7af0fc39eda47f9579fb3d",
  pdfPages: 22,
  pdfSizeBytes: 1175827,
  arxivTarballPath: "submissions/P1B/arxiv_p1b_v1B.0.103.tar.gz",
  changelog: "Venue-compliance disclosure edit (consistency pass, VENUE_POLICY_COMPLIANCE.md): AI-methods disclosure now names the models used (Anthropic Claude Opus 4 family 2026, with OpenAI GPT-5/o3, xAI Grok-4, Google Gemini 2.5). No science number changed. Recompile 0 undef-refs, mirrored byte-identical, bundle rebuilt+standalone-verified.",
  sitePdfPath: "/papers/paper1b_mcmc_companion_v1B.0.103.pdf",
});
console.log("Inserted:", result);
