// P4 v1.0.218 bump — DATA-UNLOCK: edge-on-isolated argmax tie-break coherence now COMPUTED.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-4",
  version: "v1.0.218",
  datestamp: "July 5, 2026",
  texCommit: "2322b57a8dddad3893363847b984a02ceb97774e",
  pdfMd5: "2182361bf6a2671dfd705d44f6ba0855",
  pdfPages: 31,
  pdfSizeBytes: 33999246,
  arxivTarballPath: "submissions/P4/arxiv_p4_v1.0.218.tar.gz",
  arxivTarballSizeBytes: 26702049,
  sitePdfPath: "/papers/chirality_catalog_paper_v1.0.218.pdf",
  changelog:
    "DATA-UNLOCK: the edge-on-ISOLATED argmax tie-break coherence (Gemini App E strengthening item, previously pod/data-lab-deferred) is now COMPUTED on real data. Joining catalog_production (class_eq/RA/Dec) to the committed spiral_morphology_dr8 b/a on dr8_id, the edge-on (b/a<0.30) borderline tie-break population N=295,170 is spatially ISOTROPIC: family-wise joint p=0.49 (obs max|z|=1.17 @ DES vs null p99 max|z|=3.54), every per-leg l=1 dipole |z|<1.4 (BASS+MzLS -0.23 / DECaLS +0.71 / DES +1.17). Isolating to edge-on removes the full-band DECaLS coherence (+4.72 -> +0.71), so the argmax tie-break introduces no directional dipole even in the edge-on-isolated slice. Closes the last pod-gated caveat in App E. Artifacts: pipelines/p2_chirality/outputs/canonical_provenance/edgeon_isolated_tiebreak_coherence.json + scripts/edgeon_isolated_tiebreak_coherence.py. Record: project-context/peer-reviews/INT_v3/DATA_UNLOCK_2026-07-05.md. Recompile clean (0 undef-refs, 0 overfull, 31 pages); arXiv tarball rebuilt (26.7MB) + smoke-recompiled. NO headline dipole number changed; nothing fabricated.",
});
console.log("Inserted paper-4:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-4" });
console.log("Latest paper-4:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
