// P4 v1.0.223 bump — FULL8 EXT round closure (Grok+Gemini MINOR REVISIONS, ChatGPT MAJOR REVISIONS).
// Edits: GZ1-human-only forward pointer (Sec II), Table I cosmological-weight note, Table VII synthesis
// sentence, peq>0.6 selection-function disclosure (Sec IV.A), A95 language fix ("undetectable" ->
// "would not be reliably recovered"), catalog citation template in Data Availability. No science numbers
// changed. Recompile 0 undef-refs; PDF re-mirrored byte-identical to all served paths; tarball standalone-verified.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-4",
  version: "v1.0.223",
  datestamp: "July 7, 2026",
  texCommit: "5ccdb94f",
  pdfMd5: "a9b8516646624412a0898f1ca91d80dd",
  pdfPages: 31,
  pdfSizeBytes: 33999871,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.223.tar.gz",
  arxivTarballSizeBytes: 26708964,
  sitePdfPath: "/papers/chirality_catalog_paper_v1.0.223.pdf",
  changelog:
    "FULL8 EXT round closure (Grok+Gemini MINOR REVISIONS, ChatGPT MAJOR REVISIONS). " +
    "Grok: GZ1-human-only independence cross-check forward pointer added Sec II; Table I cosmological-weight footnote; Table VII synthesis sentence. " +
    "Gemini: peq>0.6 selection-function scope disclosure (Sec IV.A); GZ1 N~4.6e4 noise floor and 47% residual already unmissable (confirmed). " +
    "ChatGPT: A95 language corrected — 'undetectable in real space and excluded at 95% recovery' -> 'would not be reliably recovered by the real-space estimator, bounded below A95'; " +
    "Table V (+3.64/+7.93 mixed conventions) = FALSE-POSITIVE (caption already explains distinct null-run sizes and field conventions); " +
    "other MAJOR findings (classifier validity, pseudo-label independence, z~-18 scope, parity-even framing, A50/A95 as falsification thresholds) all honestly disclosed in-paper — dispositioned non-real with source-cited text. " +
    "Catalog citation template added to Data Availability. No science number changed. Recompile 0 undef-refs, mirrored byte-identical, tarball standalone-verified.",
});
console.log("Inserted paper-4:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-4" });
console.log("Latest paper-4:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
