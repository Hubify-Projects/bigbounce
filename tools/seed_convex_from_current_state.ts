/**
 * Seed the new paper-orchestration Convex tables from the current
 * (drift-prone) source files. Read-only on the source files; writes
 * only to Convex.
 *
 * Run with:
 *   cd bigbounce && npx convex run -e site/.env.local tools/seed_convex_from_current_state.ts
 *
 * Or, after Convex auth is set up, the equivalent: node + ConvexHttpClient.
 *
 * Sources we read:
 *   - site/src/data/papers.ts        — current readiness, version, lastUpdated, focusAreas-equiv
 *   - site/src/app/papers/[slug]/page.tsx  — focusAreas hardcoded array
 *   - project-context/SSOT/paper-N/status.md  — per-paper SSOT (free-form, not parsed)
 *   - pipelines/p3_anomaly_engine/paper3_draft.tex — §pathc_caveats items a-j (for P3)
 *
 * This is a one-shot migration; after Convex is the source of truth,
 * the old papers.ts becomes a thin Convex-backed shim or is removed.
 *
 * NOTE: This file is `seed_convex_from_current_state.ts` (NOT inside
 * convex/); it is a Convex *action* that calls the mutations we wrote.
 * Place at tools/ so it's outside the convex/ deploy bundle.
 */
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api";

// ──────────────────────────────────────────────────────────────────────
// Canonical seed data — captured from current state of the repo on
// 2026-05-29 PDT. After first seed, mutations land via the MCP server
// (Phase 2) and this script is preserved as the audit-trail of the
// initial migration.
// ──────────────────────────────────────────────────────────────────────

const PAPERS = [
  {
    slug: "paper-1a",
    number: "1A",
    title:
      "Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–f_NL Tension, and Surviving Matter-Bounce Tests",
    shortTitle:
      "ECH structural no-go theorem; perturbation transparency + inflation-f_NL tension",
    targetJournal: "PRD" as const,
    status: "paused-houston-external" as const,
    texPath: "arxiv/paper1a_ech_nogo.tex",
    sitePdfPath: "/papers/paper1a_ech_nogo.pdf",
    focusAreas: [
      "14-barrier no-go structure (Sec. III + Appendix)",
      "ALP birefringence β=0.27° prediction vs Eskilt 0.342°±0.094° observed",
      "Perturbation-transparency theorem in §IV.D",
      "Mercuri-Capozziello phase-space-vs-loop framing at §II.C.1 (post-R23)",
    ],
    currentVersion: {
      version: "v1A.0.36",
      datestamp: "2026-05-28",
      texCommit: "1ef92d23",
      pdfMd5: "e667e5b79a1f27221b01c5277acd1132",
      pdfPages: 20,
      pdfSizeBytes: 832811,
      changelog:
        "Block-bootstrap σ correction (P4 fire #N) + P1A subagent BLOCKER fixes (sample-count drift 424,781 → 309,189, Caldwell→Cai/Quintom bibkey, ABCK γ U(1) vs SU(2) attribution).",
    },
  },
  {
    slug: "paper-1b",
    number: "1B",
    title:
      "ΛCDM+ΔNeff MCMC and NaMaster Pseudo-C_ℓ Validation Companion to Paper 1A",
    shortTitle:
      "MCMC + NaMaster pipeline companion + spectator-ALP self-consistency",
    targetJournal: "PRD" as const,
    status: "active-drive-to-100" as const,
    texPath: "arxiv/paper1b_mcmc_companion.tex",
    sitePdfPath: "/papers/paper1b_mcmc_companion.pdf",
    focusAreas: [
      "309,189 MCMC posterior samples across 2 converged dataset combinations (176,240 full-tension + 132,949 Planck+BAO+SN)",
      "ΔNeff ≈ 0 result and H_0 = 67.68 ΛCDM-consistent",
      "NaMaster pseudo-C_ℓ pipeline 500 MC recovery at SNR=20.32σ",
      "Spectator-ALP carved-out regime (f_a ~ M_Pl, m ~ H_0) — explicit parameter-restriction where Ω_φ ≪ Ω_crit holds",
    ],
    currentVersion: {
      version: "v1B.0.30",
      datestamp: "2026-05-26",
      texCommit: "bfad67ab",
      pdfMd5: "263ec963cc5c7f18a76d193766a9c744",
      pdfPages: 18,
      pdfSizeBytes: 699400,
      changelog:
        "R28 Grok scope-critique surgical closure following P4 v1.0.132 closure pattern.",
    },
  },
  {
    slug: "paper-2",
    number: "2",
    title:
      "Matter-Bounce f_NL = −35/8 Forecast: Multi-Tracer SDB and SPHEREx-Bispectrum Sensitivity-Envelope",
    shortTitle:
      "Matter-bounce f_NL=−35/8 forecast with b_phi sensitivity envelope",
    targetJournal: "JCAP" as const,
    status: "active-drive-to-100" as const,
    texPath: "research/focused_paper_source_integration/02_full_draft.tex",
    sitePdfPath: "/papers/paper2_fnl_forecast.pdf",
    focusAreas: [
      "f_NL = -35/8 = -4.375 parameter-free bounce prediction",
      "Heinrich+2023 σ(f_NL)=0.7 externalization vs own Fisher",
      "Detection significance 3-5σ post-systematic-budget",
      "DBI category-error closure at §IV (post-R22 Gemini)",
    ],
    currentVersion: {
      version: "v1.7.37",
      datestamp: "2026-05-24",
      texCommit: "3b88161f",
      pdfMd5: "26778f860ccf7b7be2db903b25eec9cd",
      pdfPages: 19,
      pdfSizeBytes: 818324,
      changelog: "R-next-f abstract-envelope MAJ closed.",
    },
  },
  {
    slug: "paper-3",
    number: "3",
    title:
      "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Anomalies and Native-Trained Novelty Rates from 37.3 Million Sources",
    shortTitle:
      "378,280-anomaly multi-survey catalog + NANOGrav γ + multi-tracer f_NL forecast",
    targetJournal: "MNRAS" as const,
    status: "active-drive-to-100" as const,
    texPath: "pipelines/p3_anomaly_engine/paper3_apjs.tex",
    sitePdfPath: "/papers/paper3_apjs.pdf",
    focusAreas: [
      "378,280 anomalies headline (=378,080 + 200) across 7 surveys",
      "7-way 5″ positional FoF dedup arithmetic (10,213 = 637 + 9,576)",
      "Fisher-positivity caveats in §6 — canonical 1σ envelope σ(f_NL) ∈ [3.92, 8.98] under 1/σ² = F_0 + c·α² (NOT the retracted symmetric ±2.37 form)",
      "σ(f_NL)=8.14 central at empirical α=0.19 jackknife (jk dispersion 0.65) at <1σ from null",
      "v3.1.69 §sec:fnl retracted-value scrub + Table I threshold-consistency caption verification",
      "NANOGrav 15-yr γ = 2.567 ± 0.382 (real-KDE Zenodo emcee fit); matter-bounce γ=3.0 at +1.13σ; SMBHB γ=4.33 at +4.61σ; Savage-Dickey B_mb/SMBHB = 7,138 decisive",
    ],
    currentVersion: {
      version: "v3.1.69",
      datestamp: "2026-05-29",
      texCommit: "e12a1e56",
      pdfMd5: "a0cff1b3131487305062609b10865554",
      pdfPages: 49,
      pdfSizeBytes: 28464812,
      changelog:
        "§sec:fnl retracted-Fisher-form scrub (8.27/2.28±7.43 reference removed from body, replaced with canonical positivity-respecting central+envelope) + §pathc_caveats item (h) Threshold consistency CLOSED via direct caption verification. Driven by first REAL direct-vendor R-round.",
    },
  },
  {
    slug: "paper-4",
    number: "4",
    title:
      "Survey-Scale Galaxy Chirality with Equivariant TTA: 8.47M Sources, 3.2M Spirals, and Block-Bootstrap-Validated Formal Exclusion of a 1.7% Cosmological Dipole",
    shortTitle:
      "8.47M galaxy chirality catalog + 18σ block-bootstrap formal exclusion of 1.7% dipole",
    targetJournal: "MNRAS" as const,
    status: "paused-houston-external" as const,
    texPath: "pipelines/p2_chirality/chirality_catalog_paper.tex",
    sitePdfPath: "/papers/chirality_catalog_paper.pdf",
    focusAreas: [
      "Subsample-mask −0.12σ MASTER-deconvolved load-bearing null",
      "v1.0.139 joint nuisance-marginalized fit: interpretation (i) at 1.7% f_CW formally excluded at ~18σ under block-bootstrap σ (NSIDE=8 super-pixels, N_boot=1000) — naive WLS gave 264σ, but residual is spatially coherent",
      "Canonical-mask +3.64σ three-interpretation closure (interpretation (ii) coherent depth/morphology systematic favored by 5+ anchors)",
      "ℓ=2 cross-spectrum r=−0.65 σ=−2.89 vs pixel-density proxy",
      "MASTER-decoupled monopole-only null × 500 (88% unexplained by monopole-only leakage)",
      "Shamir 2020 vs 2022 split with arXiv IDs (post-R22 Perplexity BL-1)",
    ],
    currentVersion: {
      version: "v1.0.139",
      datestamp: "2026-05-28",
      texCommit: "1ef92d23",
      pdfMd5: "65c652f4da00586dc49a00b22a72952c",
      pdfPages: 55,
      pdfSizeBytes: 26260986,
      changelog:
        "Block-bootstrap σ correction landed: σ(A_dipole) inflates 14.7× under spatial-coherence-respecting NSIDE=8 super-pixel bootstrap → naive 264σ formal exclusion of 1.7% cosmological dipole reframed to honest 18σ formal exclusion (still decisive but statistically defensible). §VI.D paragraph rewritten.",
    },
  },
  {
    slug: "paper-5",
    number: "5",
    title:
      "Environmental Dependence of Spiral Chirality Across DESI LSS: A V-Web Cosmic-Web Phase-1 Analysis",
    shortTitle:
      "DESI LSS spiral-chirality V-Web environmental analysis + EFT framing",
    targetJournal: "MNRAS" as const,
    status: "active-drive-to-100" as const,
    texPath: "pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex",
    sitePdfPath: "/papers/p5_desi_chirality.pdf",
    focusAreas: [
      "V-Web env_finder Phase 1 MVP cosmic-web classification on 14.6M DESI spectro galaxies",
      "Per-environment cw_fraction: void/wall/filament/cluster (range 1.7pp dominated by counting statistics)",
      "Phase 2 sensitivity sweep (10/25/50 Mpc/h × 128³/256³/512³)",
      "Tempel+2018 cross-validation status",
      "EFT bound on parity-violating coupling: Chern-Simons modified GR sense (Alexander–Yunes 2009) + photon-graviton parity sector (Lue–Wang–Kamionkowski 1999) — citations in §VII",
      "Shot-noise residual diagnostic: skewness +0.044, excess kurtosis consistent with pure-shot-noise null (post-GEM-M3 closure)",
    ],
    currentVersion: {
      version: "v0.1.32",
      datestamp: "2026-05-26",
      texCommit: "396b7978",
      pdfMd5: "75a76e1c12bc5907158bfbc2d71f6775",
      pdfPages: 27,
      pdfSizeBytes: 927499,
      changelog: "Gemini-M1+M2+M3 bundled closure + P3 v3.1.63 restart streak → 2.",
    },
  },
];

// P3 §pathc_caveats items a-j with current closure state (captured 2026-05-29).
const P3_PATHC_CAVEATS = [
  {
    label: "a",
    description:
      "378,280 union-find dedup arithmetic — option (ii) intra-survey duplicates account for 9,576 shortfall.",
    status: "closed" as const,
    closureMethod: "artifact-verification" as const,
    closureArtifact:
      "pipelines/p3_anomaly_engine/pathc_dedup/pathc_dedup_summary_no_act.json",
    closureCommit: "<v3.1.56 wave>",
  },
  {
    label: "b",
    description:
      "DESI OOD MSE threshold-in-OOD-units — to preserve 0.87% rate on OOD, threshold = MSE≈60.2 / S≈2,098 (420× canonical S>5).",
    status: "closed" as const,
    closureMethod: "real-computation" as const,
    closureArtifact:
      "pipelines/p3_anomaly_engine/r42_results/ood_threshold_2026-05-29.json",
    closureCommit: "e41d7e83",
  },
  {
    label: "c",
    description:
      "σ(f_NL) full Fisher with photo-z + fiber-assignment + selection-function nuisance blocks — open, ~1 day local.",
    status: "open" as const,
  },
  {
    label: "d",
    description:
      "NANOGrav Savage-Dickey Bayes factor — B_{matter-bounce/SMBHB} = 7,138 decisive (log10B=+3.85).",
    status: "closed" as const,
    closureMethod: "real-computation" as const,
    closureArtifact:
      "pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/savage_dickey_2026-05-29.json",
    closureCommit: "7b5d1ef3",
  },
  {
    label: "e",
    description:
      "GR projection effects (Doppler, Sachs-Wolfe, ISW, Shapiro) deterministically modeled in multi-tracer Fisher — open, ~1 day local derivation.",
    status: "open" as const,
  },
  {
    label: "f",
    description:
      "BigAE-vs-IsolationForest intersection — 284/298 = 95.3% overlap, 95.3× enriched, hypergeometric p ≈ 0.",
    status: "closed" as const,
    closureMethod: "real-computation" as const,
    closureArtifact:
      "pipelines/p3_anomaly_engine/r42_results/bigae_vs_if_intersection_2026-05-29.json",
    closureCommit: "87fd3a80",
  },
  {
    label: "g",
    description:
      "5-fold Jaccard internal-inconsistency reconcile — full-pool scoring convention confirmed (n_rows=47k, top_k=470 per fold).",
    status: "closed" as const,
    closureMethod: "artifact-verification" as const,
    closureArtifact:
      "pipelines/p3_anomaly_engine/pathc_desi_kfold/results/kfold_stability_summary.json",
    closureCommit: "a1f7498a",
  },
  {
    label: "h",
    description:
      "SDSS/LAMOST threshold consistency — Table I caption already contains per-survey disclosure (S≥0.1060 SDSS / S≥0.4613 LAMOST + footnotes ♥/♠).",
    status: "closed" as const,
    closureMethod: "truth-audit-falsification" as const,
    closureCommit: "e12a1e56",
  },
  {
    label: "i",
    description:
      "5-α-grid Fisher refit (Fisher-positivity-respecting form 1/σ² = F_0 + c·α² refit) — open, ~1-2 hr local.",
    status: "open" as const,
  },
  {
    label: "j",
    description:
      "GS asymmetric envelope (negative Fisher error bar arithmetic) — body propagated 50% in v3.1.69; remaining §sec:fnl prose hardening pending.",
    status: "open" as const,
  },
];

async function main() {
  const url = process.env.CONVEX_URL || process.env.NEXT_PUBLIC_CONVEX_URL;
  if (!url) {
    console.error(
      "set CONVEX_URL or NEXT_PUBLIC_CONVEX_URL to your Convex deployment URL"
    );
    process.exit(1);
  }
  const client = new ConvexHttpClient(url);

  for (const paper of PAPERS) {
    const { currentVersion, ...paperFields } = paper;
    await client.mutation(api.papers.upsert, paperFields);
    await client.mutation(api.paperVersions.bump, {
      paperSlug: paper.slug,
      ...currentVersion,
    });
    console.log(`✓ seeded ${paper.slug} @ ${currentVersion.version}`);
  }

  for (const caveat of P3_PATHC_CAVEATS) {
    await client.mutation(api.pathcCaveats.upsert, {
      paperSlug: "paper-3",
      label: caveat.label,
      description: caveat.description,
      status: caveat.status,
    });
    if (caveat.status === "closed" && caveat.closureMethod) {
      await client.mutation(api.pathcCaveats.close, {
        paperSlug: "paper-3",
        label: caveat.label,
        closureMethod: caveat.closureMethod,
        closureArtifact: caveat.closureArtifact,
        closureCommit: caveat.closureCommit,
      });
    }
    console.log(`✓ seeded P3 caveat (${caveat.label}) [${caveat.status}]`);
  }

  const states = await client.query(api.papers.listAllPaperStates);
  console.log("\n=== POST-SEED STATE ===");
  for (const s of states) {
    console.log(
      `  ${s.number}  ${s.shortTitle.slice(0, 60).padEnd(60)}  ${(s.currentVersion ?? "?").padEnd(10)}  readiness=${s.readinessComputed}  open: ${s.openBlockers}B/${s.openMajors}M/${s.openMinors}m/${s.openCaveats}C`
    );
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
