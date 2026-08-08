// P2 v1.7.115 bump — INT-Claude genuinely-new MAJOR closed by RE-COMPUTE: the c15
// channel-native Fisher's GR leg dB/dA_GR was built WITHOUT the M123 transfer product
// the f_NL primordial leg carries, leaving it in potential space vs the density basis;
// this collapsed F[2,2]~1e-18 and FAKED rho(f_NL,A_GR)=-0.001 orthogonality. Fixed
// (Dg *= M123) + re-ran: corrected rho=-0.42 (2x2)/-0.49 (3x3), sigma_marg=0.94->2.32sigma.
// Load-bearing conclusion survives (channel-native floor 2.32sigma > proxy floor 1.30sigma).
// -35/16 unchanged, nothing fabricated.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.115",
  datestamp: "July 12, 2026",
  texCommit: "TBD",
  pdfMd5: "1f4252203c492ff09451e8a1633d7ea6",
  pdfPages: 37,
  pdfSizeBytes: 1372123,
  arxivTarballPath: "submissions/P2/arxiv_p2_v1.7.115.tar.gz",
  sitePdfPath: "papers/02_full_draft_v1.7.115.pdf",
  changelog:
    "INT-Claude genuinely-new MAJOR closed by RE-COMPUTE: the c15 channel-native joint {f_NL,b_phi,A_GR} Fisher built the GR-projection derivative dB/dA_GR = b*b*b*S_GR WITHOUT the M123=M(k1)M(k2)M(k3) transfer product the f_NL primordial leg (b*b*b*M123*B_phi) carries. S_GR is a potential-space template (P_phi legs), so omitting M123 left the GR leg in potential space while the f_NL leg was in the observed galaxy-density basis; contracted against the density-space covariance this collapsed F[2,2] to ~2.8e-18 and FAKED the rho(f_NL,A_GR)=-0.001 near-orthogonality v1.7.114 headlined. This is a real code-consistency bug, not referee variance: the same file's cross_fisher_alpha() already applies M123. FIX: Dg = b*b*b*(M123*S_GR); re-ran the full CAMB Fisher (231s). CORRECTED: F[2,2]=1.14e-3; rho(f_NL,A_GR)=-0.42 (2x2)/-0.49 (3x3) -- GR channel moderately correlated with f_NL, NOT orthogonal; rho(f_NL,b_phi)=+0.99; b_phi-30%-prior sigma_marg(f_NL^bounce)=0.94 -> 2.32sigma for -35/16 (local self-consistency sigma_local=0.94); b_phi-free=5.2. Load-bearing conclusion SURVIVES: channel-native floor 2.32sigma still HIGHER than the retained 1.30sigma proxy floor, so the rho=-0.868 proxy stays the conservative quoted endpoint (no headline loosened); alpha=0.992 unchanged. Abstract Scope + Sec.systematics corrected 'near-orthogonal/both proxies overstated' -> 'moderately correlated (rho~-0.42), less degenerate than the proxies but not orthogonal'. Recompiled 0 undef-refs/0 overfull, 37pp, mirrored byte-identical to all served paths. Nothing fabricated. Genuinely-new finding resets P2's directive-K clean-wave streak.",
});
console.log("Inserted paper-2:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-2" });
console.log("Latest paper-2:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
