// P2 v1.7.91 bump — cubic transmission DERIVED + marginalized joint-covariance budget.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-2",
  version: "v1.7.91",
  datestamp: "July 5, 2026",
  texCommit: "499d431d184d49e60e273de3693aa6c7cc07bddd",
  pdfMd5: "562f05180ee0b8e9598484287d252079",
  pdfPages: 33,
  pdfSizeBytes: 985228,
  arxivTarballPath: "project-context/SSOT/arxiv_tarballs/paper2_arxiv_v1.7.91.tar.gz",
  arxivTarballSizeBytes: 415204,
  sitePdfPath: "/papers/paper2_fnl_forecast_v1.7.91.pdf",
  changelog:
    "TWO verified-real-science INT-v3 strengthenings. EDIT 1: cubic bounce transmission now DERIVED to a bounded systematic (closes assumption-(d) MAJOR). The Cai-Wilson-Ewing LQC quasi-dust bounce is single-clock (effective LQC adds no new scalar dof - dressed-metric/hybrid per Wilson-Ewing, deformed-algebra per Cailleteau et al. keeps the scalar sector single-clock), so nonlinear superhorizon zeta-conservation holds to all orders; the only zeta-dot source is O((k eta_B)^2) gradient pressure at every order (cubic included) => transmission = 1 +/- O((k eta_B)^2) ~ 1 +/- 1e-4 (delta fNL <~ 1e-3, negligible vs sigma~0.7), derived not assumed. Sole model-choice input: subleading gradient sign (Lorentzian c_s^2=1 dressed-metric adopted) - citable choice, not open computation. Added Cailleteau:2011kr (arXiv:1111.3535). EDIT 2: systematic budget upgraded additive-quadrature -> marginalized joint covariance (honest, slightly worsens the floor). sigma_marg = sigma_base/sqrt(1-rho^2) with the paper's OWN committed c8 CAMB degeneracy rho=-0.868 as a conservative PROXY => marginalized floor ~1.3sigma (vs ~1.5sigma quadrature, ~14% lower). Flagged: SDB channel has a real c8 joint covariance; bispectrum-only uses rho=-0.868 as PROXY pending the deferred partial B_g/partial A_GR triangle-response derivative. ~1.3sigma lands at the existing 1.3-2.75sigma lower endpoint => no abstract range number changes. Recompile clean: 0 undef-refs, 0 overfull >50pt, 33 pages, /latex-audit PASS. Nothing fabricated - anchored to committed c8 Fisher + single-clock physics.",
});
console.log("Inserted:", result);
const cur = await client.query(api.paperVersions.current, { paperSlug: "paper-2" });
console.log("Latest paper-2:", cur?.version, "/", cur?.datestamp, "/ md5", cur?.pdfMd5, "/ pages", cur?.pdfPages);
