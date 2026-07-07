import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p3",
  version: "v3.1.141",
  datestamp: "July 7, 2026",
  texCommit: "103a81cf",
  pdfMd5: "0b4a6ab6ec07d0120e6798376426d0a8",
  pdfPages: 33,
  pdfSizeBytes: 4678731,
  changelog:
    "Venue-compliance disclosure edit (Edit A, VENUE_POLICY_COMPLIANCE.md): added explicit author-responsibility + not-an-author clause AND model naming (Anthropic Claude Opus 4 2026 + OpenAI GPT-5/o3 + xAI Grok-4 + Google Gemini 2.5) per AAS/IOP requirement — closes the P3 responsibility-clause gap. No science number changed. Recompile 0 undef, mirrored byte-identical, bundle rebuilt+standalone-verified.",
  sitePdfPath: "/papers/paper3_draft_v3.1.141.pdf",
  arxivTarballPath: "submissions/P3/arxiv_p3_v3.1.141.tar.gz",
});
console.log("P3 inserted:", result);
