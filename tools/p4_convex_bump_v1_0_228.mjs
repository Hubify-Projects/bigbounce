// P4 v1.0.228 bump — CV-round (2026-07-09) EXT closure.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-4",
  version: "v1.0.228",
  datestamp: "July 9, 2026",
  texCommit: "1f6ef3f0",
  pdfMd5: "176e493b75ded77e540367c733e34f10",
  pdfPages: 34,
  pdfSizeBytes: 25105175,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.228.tar.gz",
  arxivTarballSizeBytes: 27470946,
  sitePdfPath: "/papers/paper4_chirality_catalog.pdf",
  changelog:
    "CV-round (2026-07-09) EXT closure: framing/relocation of the harmonic residual (below recovery threshold, origin unresolved — not 'non-cosmological'), hemisphere-LEE recast (rejects random-label null but attributed to systematics), GZ1 human-only cross-check tone neutralized + coarse-sensitivity qualifier, overconfidence 'cannot bias' → conditional, VI C theory-citations re-described to match cited refs (cosmic-birefringence/parity-violation), A95 labeled recovery/detection-efficiency threshold (not exclusion/upper-limit), flip-identity QC (59,515 rows) surfaced into Results, single primary science sample declared with full-field WLS as diagnostic. Verified numbers unchanged. Recompile 0 undef, 0 overfull; mirrored byte-identical to 3 served paths; tarball rebuilt + standalone-verified (34pp, 0 undef).",
});
console.log("Inserted paper-4:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-4" });
console.log("Latest paper-4:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
