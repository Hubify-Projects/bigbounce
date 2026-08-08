// P1A v1A.0.113 — Venue-compliance disclosure edit (Edit C, VENUE_POLICY_COMPLIANCE.md)
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-1a",
  version: "v1A.0.113",
  datestamp: "July 7, 2026",
  texCommit: "103a81cf",
  pdfMd5: "53a63e424f9ff13d7a5b135f6c64093d",
  pdfPages: 37,
  pdfSizeBytes: 1802191,
  arxivTarballPath: "submissions/P1A/arxiv_p1a_v1A.0.113.tar.gz",
  sitePdfPath: "/papers/paper1a_ech_nogo_v1A.0.113.pdf",
  changelog:
    "Venue-compliance disclosure edit (Edit C, VENUE_POLICY_COMPLIANCE.md): AI-methods disclosure now names the models used (Anthropic Claude Opus 4 family 2026, with OpenAI GPT-5/o3, xAI Grok-4, Google Gemini 2.5 as cross-check/internal-review) per IOP/JCAP model+version requirement. No science number changed. Recompile 0 undef-refs, mirrored byte-identical to all served paths, bundle rebuilt+standalone-verified.",
});
console.log("Inserted:", result);

console.log("\n--- verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
