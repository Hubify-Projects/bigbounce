import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");

const result = await client.mutation(api.paperVersions.bump, {
  paperSlug: "paper-a3m",
  version: "v3M.0.15",
  datestamp: "2026-09-04",
  texCommit: "916313aafdff5a7b369a483304cafa64c848a931",
  pdfMd5: "4f2bf5e8204021bf06cbe27e3b8932c9",
  pdfPages: 17,
  pdfSizeBytes: 739165,
  changelog: "D-A3-10/D-A3-11 science reframe (ledger rows 10/14, not a review round): title/abstract reframed to the joint (r,f_NL) no-go. New Sec VII 'The tensor amplitude of the modelled background' -- r=16eps=24 exactly (bounce-invariant, ~670x above BICEP/Keck r<0.036), n_s=1 exactly, n_T=n_s-1=-0.035 the surviving falsifiable tilt; the earlier tensor-sense r=0.84 withdrawn (was the bispectrum shape-overlap coefficient). New Sec VIII 'The joint (r,f_NL) no-go and the curvaton route' -- r=24c_s, f_NL^pre=-165/16+65/(8c_s^2) (reproduces Li+2016); r<0.036 needs c_s<1.5e-3 (f_NL^after 6e5-9e5); |f_NL|<=5.1 needs c_s>=0.444 (r>=10.7); windows disjoint 296x; single-field matter bounce (canonical or k-essence) excluded jointly by r and f_NL, strengthening Li+2016's no-go 3.8x; curvaton-type spectator route named as (r,n_s)-viable but dilutes -35/16 by (r/24)^2, detectable only for r>~23, needs an unmodelled entropy sector. Sec II Appendix A wording corrected: the delta N_c second-order monopole match to a pure-translation coefficient is a numerical coincidence of the threading map, not evidence of a translation mechanism (a rigid translation is isotropic and cannot itself supply a monopole). Sec V (PBH, ledger row 11) sign-disagreement with Choudhury et al. resolved -- the apparent low-gamma_cr enhancement is an IR-divergent O(eps^2) artefact, not physical; Choudhury et al. are right that negative f_NL suppresses. In-coverage amplitude ratio corrected to 1.84+-0.03 (144 pts, [1.76,1.89]) over this model's own gamma_cr in [0.267,0.630]; the narrower 1.732+-0.050 (27-pt committed grid) is no longer quoted as universal. Discussion/Next-steps and reproducibility statement updated for the new sections and their committed scripts (row10_r_ns, row14_cs_window, curvaton_matter_bounce_adjudication, threading_map_second_order, row11_pbh_residuals). Directive G: 4-pass, 0 undefined refs, 0 overfull hboxes >10pt. Readiness held at 75 pending a new verification board (R7) on this reframed content; site data sync pending in a separate bundle.",
});
console.log("Inserted:", result);
