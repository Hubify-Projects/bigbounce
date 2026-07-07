import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "p5",
  version: "v0.1.105",
  datestamp: "July 7, 2026",
  texCommit: "103a81cf",
  pdfMd5: "5c340fd7719d26a51e8e6e763e6f698e",
  pdfPages: 37,
  pdfSizeBytes: 1465939,
  changelog:
    "Venue-compliance disclosure edit (Edit B, VENUE_POLICY_COMPLIANCE.md): added explicit author-responsibility + not-an-author clause AND model naming (Anthropic Claude Opus 4 2026 + OpenAI GPT-5/o3 + xAI Grok-4 + Google Gemini 2.5) per MNRAS/APS requirement — closes the P5 responsibility-clause gap. No science number changed. Recompile 0 undef, mirrored byte-identical, bundle rebuilt+standalone-verified.",
  sitePdfPath: "site/public/papers/p5-chirality.pdf",
  arxivTarballPath: "submissions/P5/arxiv_p5_v0.1.105.tar.gz",
});
console.log("P5 inserted:", result);
