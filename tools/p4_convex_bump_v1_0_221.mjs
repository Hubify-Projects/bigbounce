// P4 v1.0.221 bump — Venue-compliance disclosure edit: AI-methods now names the models used.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-4",
  version: "v1.0.221",
  datestamp: "July 7, 2026",
  texCommit: "103a81cf",
  pdfMd5: "3947bbf75898d80f5b1ace977e4d3e4c",
  pdfPages: 31,
  pdfSizeBytes: 33994784,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.221.tar.gz",
  arxivTarballSizeBytes: 26704224,
  sitePdfPath: "/papers/chirality_catalog_paper_v1.0.221.pdf",
  changelog:
    "Venue-compliance disclosure edit (consistency pass, VENUE_POLICY_COMPLIANCE.md): AI-methods now names the models used (Anthropic Claude Opus 4 2026 + OpenAI GPT-5/o3 + xAI Grok-4 + Google Gemini 2.5). No science number changed. Recompile 0 undef, mirrored byte-identical, bundle rebuilt+standalone-verified.",
});
console.log("Inserted paper-4:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-4" });
console.log("Latest paper-4:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
