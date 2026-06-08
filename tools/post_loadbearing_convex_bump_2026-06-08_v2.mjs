// Convex bump after LOAD-BEARING round 2026-06-08 — CORRECTED slug form.
// Prior tools/p*_convex_bump_*.mjs used "p4" etc. but listAllPaperStates
// queries paper_versions.paperSlug == papers.slug ("paper-4"), so the prior
// bumps went to the wrong key. This script re-bumps with the correct slugs.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");
const datestamp = "2026-06-08";
const texCommit = "73522984";

const bumps = [
  {
    paperSlug: "paper-4",
    version: "v1.0.160",
    pdfMd5: "c9cb29a12f3957e56ae881bdbd485fb1",
    pdfPages: 11,
    pdfSizeBytes: 465224,
    sitePdfPath: "/papers/chirality_catalog_paper_v160.pdf",
    changelog:
      "LOAD-BEARING #3 closure: §IV.D binomial-null trial-count disambiguated. Binomial(N_spiral(p), p_CW) with footnote fn:binomial_nspiral explaining N_spiral(p) is the per-pixel spiral count (CW+CCW), not the all-galaxy weighting field W_p. Headline 99.3% pre-MASTER reproduction is on the spiral-trial draw. Parallel N(p)_all-trial draw queued for sensitivity-budget recompute; expected sub-0.1sigma effect because mode-coupling decoupling absorbs trial-count normalization. Closes recurring P4-META-E3.",
  },
  {
    paperSlug: "paper-3",
    version: "v3.1.76",
    pdfMd5: "d5b3377f6db9bf3536471eb68784d311",
    pdfPages: 20,
    pdfSizeBytes: 3589356,
    sitePdfPath: "/papers/paper3_draft.pdf",
    changelog:
      "LOAD-BEARING #2 closure: §III.B dedup-radius sensitivity paragraph + per-survey astrometric heterogeneity acknowledgment (DESI/SDSS/LAMOST sub-arcsec vs Gaia <0.1''+PM vs NEOWISE ~6'' PSF). 637 multi-survey count read as lower bound dominated by NEOWISE under-matching. Formal {3'', 5'', 7''} sensitivity + Budavari-Szalay probabilistic cross-match queued for future revision. Plus: 3 pre-existing dangling fig refs from v3.1.75 condensation cleaned. First fully-clean P3 compile post-condensation.",
  },
  {
    paperSlug: "paper-1b",
    version: "v1B.0.43",
    pdfMd5: "d4fc2d5674bdf7a4a124ba15063203df",
    pdfPages: 10,
    pdfSizeBytes: 720119,
    sitePdfPath: "/papers/paper1b_mcmc_companion_v1B.0.43.pdf",
    changelog:
      "LOAD-BEARING wpivot definition: footnote fn:wpivot defines w_pivot = w_0 + (1-a_p)*w_a with a_p = 1 - Cov(w_0,w_a)/Var(w_a) = 0.6680 -> z_p = 0.497 (internal to DESI DR2+Planck+DES-Y5+Pantheon+). sigma derivation reproduces +/-0.0301. SH0ES/DESI-alone shift Delta z_p <= 0.1. Closes P1B-META-E1 (the actual finding the persistence_tracker had been mis-labelling as 'lee' via substring on 'calEE' for 6 rounds before FP fix).",
  },
  {
    paperSlug: "paper-5",
    version: "v0.1.46-2026-06-08",
    pdfMd5: "e134d81382cbf105040869ddaa211080",
    pdfPages: 22,
    pdfSizeBytes: 973458,
    sitePdfPath: "/papers/p5_desi_chirality_v0.1.46.pdf",
    changelog:
      "LOAD-BEARING #1 closure: T-Web/V-Web algorithm-label mismatch. Paper retitled 'tidal-tensor cosmic-web (Hahn 2007 T-Web)' globally; Hoffman 2012 V-Web citation removed. New footnote documents env_finder code computes phi_k = -delta_k/k^2 then T_ij = -k_i k_j phi_k = Hahn 2007 T-Web recipe (not V-Web velocity shear). Science conclusion (chirality independent of LSS environment at sub-pp sensitivity in DESI DR1) unchanged.",
  },
  // P2 not bumped this round but its old slug-mismatch entries should be updated
  // to keep all 6 papers visible — defer to a separate cleanup.
];

for (const bump of bumps) {
  const result = await client.mutation(api.paperVersions.bump, {
    ...bump,
    datestamp,
    texCommit,
  });
  console.log(`[${bump.paperSlug} ${bump.version}] inserted:`, result);
}

// Verify
console.log("\n--- post-bump verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
