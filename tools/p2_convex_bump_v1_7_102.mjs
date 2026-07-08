// P2 v1.7.102 bump — RS8 closure: tone-regression rewrite (Gemini MAJOR) + Cai-Li Appendix-A consistency clarification (ChatGPT MAJOR: MISREAD verdict). No science number changed.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.102",
  datestamp: "July 7, 2026",
  texCommit: "TBD",
  pdfMd5: "266118c10810cd0410f7f33abc4e3bc1",
  pdfPages: 35,
  pdfSizeBytes: 1339389,
  arxivTarballPath: "submissions/P2/arxiv_p2_v1.7.102.tar.gz",
  sitePdfPath: "papers/02_full_draft_v1.7.102.pdf",
  changelog:
    "Tone-regression rewrite (Gemini MAJOR): neutralized rebuttal/defensive register in Sec IX.E (signpost paragraph recast as declarative scope summary), Sec IX.E body ('We emphasize that a detection' -> neutral), Sec template ('a referee may ask' -> neutral), Sec benchmark ('we emphasize sigma_3/sigma_1' -> declarative), App A ('a narrative we explicitly reject' -> neutral; 'We emphasize that the identity' -> declarative). Cai-Li Appendix-A consistency (ChatGPT MAJOR): MISREAD verdict -- paper is internally consistent; added one clarifying sentence making explicit that Li and Cai printed polynomials agree coefficient-for-coefficient at c_s=1, so -35/8 is what both printed polynomials yield; -35/16 comes from vertex re-summation. No number changed. No disclosure changed.",
});
console.log("Inserted paper-2:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-2" });
console.log("Latest paper-2:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
