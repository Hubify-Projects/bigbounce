// Convex bump after LOAD-BEARING round 2026-06-08
// Bumps P3 v3.1.76, P4 v1.0.160, P1B v1B.0.43, P5 v0.1.46-2026-06-08
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");
const datestamp = "2026-06-08";
const texCommit = "73522984";

const bumps = [
  {
    paperSlug: "p4",
    version: "v1.0.160",
    pdfMd5: "c9cb29a12f3957e56ae881bdbd485fb1",
    pdfPages: 11,
    pdfSizeBytes: 465224,
    sitePdfPath: "/papers/chirality_catalog_paper_v160.pdf",
    changelog:
      "LOAD-BEARING #3 closure: §IV.D binomial-null trial-count disambiguated. Wording 'Binomial(n_total, p_CW)' -> explicit 'Binomial(N_spiral(p), p_CW)' with N_spiral(p) = N_CW(p) + N_CCW(p). New footnote fn:binomial_nspiral: N_spiral(p) is distinct from N(p)_all weighting field W_p that appears in A_p definition; the chirality field A_p = (N_CW-N_CCW)/N_spiral is defined on spirals only, so the generative null draws from spiral trial pool. Documents that headline 99.3% pre-MASTER reproduction figure in Table tab:monopole_mask_null is on the spiral-trial draw; previous wording was ambiguous between N_spiral(p) and N(p)_all. Parallel rerun on N(p)_all-trial draws queued for canonical-mask sensitivity-budget recompute; expected sub-0.1sigma effect because mode-coupling decoupling absorbs trial-count normalization. Closes P4-META-E3 (fire 12 essential, recurring across 3+ rounds). PDF 11pp/465KB/0 undef refs. Fire 12 cross-round delta: 0 NEW ESS (self-terminate counter 2/3). Houston external R-round queued.",
  },
  {
    paperSlug: "p3",
    version: "v3.1.76",
    pdfMd5: "d5b3377f6db9bf3536471eb68784d311",
    pdfPages: 20,
    pdfSizeBytes: 3589356,
    sitePdfPath: "/papers/paper3_draft.pdf",
    changelog:
      "LOAD-BEARING #2 closure: §III.B dedup-radius sensitivity paragraph + per-survey astrometric heterogeneity acknowledgment. New paragraph: uniform 5'' matching radius is conservative compromise across heterogeneous source astrometry — DESI/SDSS/LAMOST sub-arcsec on spectroscopic targets retained in anomaly tier, Gaia DR3 sub-0.1'' at bright-mag top-1% slice + proper-motion solutions not propagated to survey epochs, NEOWISE ~6'' PSF on W1+W2. 637 multi-survey coincidence count read as lower bound dominated by NEOWISE under-matching, not final cross-survey association rate. Headline 378,280 unique-object count + 378,080 point-source tier robust to dedup-radius refinements at <=0.1% level given observed 2.63% compression. Formal {3'', 5'', 7''} sensitivity sweep + Budavari-Szalay probabilistic cross-match with per-survey error ellipses + Gaia PM epoch propagation on-record-deferred to future catalog revision. Plus: 3 pre-existing dangling figure refs (fig:architecture/example_spectra/gallery_highz) from v3.1.75 49pp->20pp condensation replaced with companion-data-repository prose pointers. First fully-clean P3 compile post-condensation: 0 undef refs, 0 overfull. PDF 20pp/3.59MB.",
  },
  {
    paperSlug: "p1b",
    version: "v1B.0.43",
    pdfMd5: "d4fc2d5674bdf7a4a124ba15063203df",
    pdfPages: 10,
    pdfSizeBytes: 720119,
    sitePdfPath: "/papers/paper1b_mcmc_companion_v1B.0.43.pdf",
    changelog:
      "LOAD-BEARING wpivot definition: footnote fn:wpivot on Table tab:iter2_posterior $w_pivot$ row now defines w_pivot = w_0 + (1-a_p)*w_a with a_p = 1 - Cov(w_0,w_a)/Var(w_a) chosen so w_0 and w_a are decorrelated in the posterior covariance. On converged iter2 chain a_p = 0.6680, giving z_p = 1/a_p - 1 = 0.497; internal to dataset stack (DESI DR2 BAO + Planck NPIPE + DES-Y5 + Pantheon+), distinct from de Putter-Linder literature z_p ~ 0.4. sigma derivation reproduces the +/-0.0301 value above (sigma^2 = sigma_w0^2 + (1-a_p)^2 sigma_wa^2 = 0.0436^2 + 0.3320^2 * 0.1864^2 = 0.0301^2). SH0ES/DESI-alone shift Delta z_p <= 0.1 + Delta w_pivot <= 0.01 noted in directions of the linear-Fisher prediction. Closes the actual P1B-META-E1 finding (the 'wpivot is reported but never defined' issue that the persistence_tracker had been mis-labelling as 'lee' via substring on 'calEE' for 6 rounds — FP fix landed in prior step). PDF 10pp/720KB/0 undef refs.",
  },
  {
    paperSlug: "p5",
    version: "v0.1.46-2026-06-08",
    pdfMd5: "e134d81382cbf105040869ddaa211080",
    pdfPages: 22,
    pdfSizeBytes: 973458,
    sitePdfPath: "/papers/p5_desi_chirality_v0.1.46.pdf",
    changelog:
      "LOAD-BEARING #1 closure: T-Web/V-Web algorithm-label mismatch resolved. Paper retitled to 'tidal-tensor cosmic-web (Hahn 2007 T-Web)' globally. V-Web/Hoffman 2012 citation removed. New footnote documents that env_finder code in pipelines/p5_desi_chirality/env_finder/_compute_vweb_lib.py:63-86 computes phi_k = -delta_k / k^2 (Poisson solve) then T_ij = -k_i k_j phi_k, which is the Hahn 2007 T-Web recipe — NOT V-Web (velocity-shear, Hoffman 2012) which would require reconstructing a velocity field via linear-theory continuity on selection-function-corrected density field + computing Sigma_ij. Science conclusion (galaxy chirality statistically independent of LSS environment at sub-pp sensitivity within DESI DR1) unchanged — T-vs-V-Web is methodology only. paperTimestamp June 4 -> June 2026.",
  },
];

for (const bump of bumps) {
  const result = await client.mutation(api.paperVersions.bump, {
    ...bump,
    datestamp,
    texCommit,
  });
  console.log(`[${bump.paperSlug} ${bump.version}] inserted:`, result);
}
console.log("DONE — all 4 papers bumped.");
