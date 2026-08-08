// P2 v1.7.99 bump — venue-compliance disclosure: AI-methods now names models per IOP/JCAP; NO science number changed.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.99",
  datestamp: "July 7, 2026",
  texCommit: "103a81cf",
  pdfMd5: "b081ce65e0c02751f11dd43d78eac752",
  pdfPages: 34,
  pdfSizeBytes: 1328470,
  arxivTarballPath: "submissions/P2/arxiv_p2_v1.7.99.tar.gz",
  sitePdfPath: "papers/02_full_draft_v1.7.99.pdf",
  changelog:
    "Venue-compliance disclosure edit (Edit C, VENUE_POLICY_COMPLIANCE.md): AI-methods now names models (Anthropic Claude Opus 4 2026 + OpenAI GPT-5/o3 + xAI Grok-4 + Google Gemini 2.5) per IOP/JCAP. No science number changed. Recompile 0 undef, mirrored byte-identical, bundle rebuilt+standalone-verified.",
});
console.log("Inserted paper-2:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-2" });
console.log("Latest paper-2:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
