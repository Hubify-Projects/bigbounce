// Convex bump for TIER A2 quick-win round 2026-06-08 ~15:10pt
// P3 v3.1.77, P5 v0.1.47, P1B v1B.0.44. Long-form slugs per
// tools/README_convex_bump_slug_convention.md.
import { ConvexHttpClient } from "convex/browser";
import { api } from "../convex/_generated/api.js";

const client = new ConvexHttpClient("https://brilliant-panther-471.convex.cloud");
const datestamp = "2026-06-08";
const texCommit = "5bde3a31";  // will be updated to actual commit after push

const bumps = [
  {
    paperSlug: "paper-3",
    version: "v3.1.77",
    pdfMd5: "19d50d693699c2c62c668cb838b3f70b",
    pdfPages: 20,
    pdfSizeBytes: 3590379,
    sitePdfPath: "/papers/paper3_draft.pdf",
    changelog:
      "TIER A2 fire-14 P3-META-E4 closure: γ ± 0.382 vs CI [2.304, 2.882] arithmetic inconsistency. Truth-audit verified Gaussian half-width 0.382 inconsistent with CI half-widths 0.287/0.291 (49% mismatch — posterior is non-Gaussian/asymmetric). §V.B + App. E now distinguish the two summaries: γ = 2.567 ± 0.382 (Gaussian-approximation mean ± std-dev, used for +1.13σ matter-bounce parameter-shift test) vs γ = 2.591^{+0.291}_{-0.287} (median + asymmetric 68% CI [2.304, 2.882]). Both summaries presented in parens with explicit interpretation. PDF 20pp/3.59MB/0 undef refs.",
  },
  {
    paperSlug: "paper-5",
    version: "v0.1.47-2026-06-08",
    pdfMd5: "d9f93b07f07a1eaf096094e3fc3f6983",
    pdfPages: 20,
    pdfSizeBytes: 973440,
    sitePdfPath: "/papers/p5_desi_chirality_v0.1.47.pdf",
    changelog:
      "TIER A2 fire-14 P5-META-E1 closure: §X.B 'range ~0.2 percentage points across the four V-Web classes' replaced with 'inter-class range 1.98 percentage points' (matching Table II tab:cw_vs_env canonical run). Parenthetical added clarifying that the max per-cell inter-class range across the nine (R_s, λ_th) Phase 2 sweep cells is 0.22pp — DIFFERENT statistic, §sec:phase2. Truth-audit refined the meta-reviewer's actual finding: the contradiction is 1.98pp (inter-class) vs 0.22pp/0.2pp (per-cell), NOT 1.98pp vs 1.7pp as the fire-14 closeout summary mislabeled. PDF 20pp/951KB/0 undef refs.",
  },
  {
    paperSlug: "paper-1b",
    version: "v1B.0.44",
    pdfMd5: "ec19863c1700936549c20536b90e380b",
    pdfPages: 11,
    pdfSizeBytes: 721260,
    sitePdfPath: "/papers/paper1b_mcmc_companion_v1B.0.44.pdf",
    changelog:
      "TIER A2 fire-14 P1B-META-E1 β-bound clarification: parenthetical added on β_ALP = 0.336° ± 0.107° MCMC line explaining the direct-sample priors are on (θ_i, m/H_0), NOT on Δφ/f_a (which is derived along ALP trajectories). The natural-envelope Δφ/f_a ∈ [0.2, 1.1] corresponds to the corners of the (θ_i, m/H_0) natural-prior box. The MCMC posterior, anchored to Planck PR4 + ACT DR6 EB-spectrum data, pulls (θ_i, m/H_0) toward the upper edge — implying C_aγ · Δφ/f_a ≈ 10.3 which at C_aγ=8 fixed corresponds to Δφ/f_a ≈ 1.29, ~17% above natural envelope upper bound (same ~25× fine-tuning regime as fn:theta_backreaction). Truth-audit refinement: the meta-reviewer's 'much less than 0.336°' phrasing overstated the gap; actual gap is 15% not order-of-magnitude. PDF 11pp/721KB/0 undef refs (paper grew 1pp from 10 due to footnote expansion).",
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

// Verify
console.log("\n--- post-bump verification ---");
const states = await client.query(api.papers.listAllPaperStates);
for (const p of states) {
  console.log(`${p.number}: ${p.currentVersion ?? "null"} / ${p.lastUpdated ?? "null"}`);
}
