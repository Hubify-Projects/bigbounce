# P2 v1.7.34 — R-next-c brutal-honesty-Grok verdict

**Date:** 2026-05-24
**Reviewer:** Claude (Opus 4.7) acting as Grok-4.3 brutal-honesty stress-test reviewer
**Round:** 2-of-3 in the fresh §4.4.1 cross-model streak on v1.7.34
**Perspective:** Adversarial stress-test — assume the paper hides a flaw both prior rounds missed because R-next-a was narrowly theoretical-physics and R-next-b was narrowly citation-rigor.
**Artifacts read:**
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.tex` (549 lines, v1.7.34)
- R-next-a theoretical-physics verdict (2 MAJ both closed/falsified)
- R-next-b Perplexity-citation verdict (0/0/2-min clean)

---

## One-line summary

Paper survives the brutal cross-check on five of seven attack vectors (a/c/d/e/f/g), with one **MAJOR arithmetic finding** (the headline `BF ≈ 6` at curvaton-natural [-5,+5] / σ_th=1.0 corner is inflated by ~50% — analytic recomputation gives BF ≈ 4.0, not 6) plus one **MINOR** on the BF=8 broad-Gaussian baseline being slightly overstated (paper says 8, analytic gives 9.8 — opposite-direction rounding, but inconsistent with the same Gaussian arithmetic logic used elsewhere). One-tally: **1 MAJOR / 1 minor / 0 nit**.

---

## Per-finding blocks

### MAJOR-1 — Headline BF ≈ 6 at curvaton-natural [-5,+5] / σ_theory=1.0 corner is ~50% inflated

**Location:** L29 abstract ("a detection near $\fnl = -4.375$ favors the bounce over tuned multifield competitors at Bayes factor $\mathrm{BF} \approx 6$ (curvaton-natural $[-5,+5]$ competitor prior, $\sigma_{\rm theory}=1.0$ Gaussian bounce prior)"); L216 §sec:bayesian ("under the curvaton-natural $[-5, +5]$ prior the headline Bayes factor at the recommended $\sigma_{\rm theory} = 1.0$ bounce prior is $\mathrm{BF} \approx 6$"); L260 Table corner ($\sigma_{\rm theory}\!=\!1.0$ Gaussian, narrow $[-5,+5]$: BF~6); L266 ("BF~$\sim 7$ (delta) and BF~$\sim 6$ ($\sigma_{\rm theory}\!=\!1.0$) values quoted in the prose"); L293.

**Issue:** Direct analytic reconstruction of the four-corner Bayes-factor grid using the paper's own framework (L233 analytic formula `BF = (fnl_max - fnl_min) * L(obs|fnl=-35/8) / integral L(obs|fnl) dfnl`, σ(fnl)=0.7, observation at -4.375) gives:

| Corner | Width | Paper claims | Analytic recompute (scipy.stats.norm) | Discrepancy |
|---|---|---|---|---|
| Delta prior, broad [-15,+15] | 30 | BF~17 | BF=17.10 | matches ✓ |
| Delta prior, narrow [-5,+5] | 10 | BF~7 | BF=7.00 | matches ✓ |
| Gauss σ_th=1.0, broad [-15,+15] | 30 | BF~8 (headline) | BF=9.80 | paper UNDERSTATES by ~20% |
| **Gauss σ_th=1.0, narrow [-5,+5]** | **10** | **BF~6** | **BF=4.01** | **paper OVERSTATES by ~50%** |

The narrow-Gaussian corner is the lowest BF in the entire grid and is the one most-cited as the curvaton-natural baseline. The other three corners agree with paper to within rounding (and the delta-rows are exact to four-digit precision). The σ_th=1.0/narrow corner is **anomalously inflated** by a factor of ~1.5 relative to the same arithmetic that produces the other three corners.

**Mechanism of the discrepancy:** Under a Gaussian bounce prior σ_th=1.0 centered on -4.375 and observation also at -4.375, the marginal likelihood at the observation is `1/sqrt(2π(σ_obs²+σ_th²)) = 1/sqrt(2π·1.49) = 0.327`. The competitor [-5,+5] mass under N(obs=-4.375, σ_obs=0.7) is `norm.cdf(5;−4.375,0.7) - norm.cdf(−5;−4.375,0.7) = 0.819`. Then BF = 10 · 0.327 / 0.819 = 3.99. To get 6, the paper would need either (i) the bounce prior to be a delta-at-σ_th, not a Gaussian (in which case the row should say "delta", not "Gauss σ_th=1.0"), or (ii) a different effective σ_obs or a different convention for the bounce-prior normalization.

**Why this matters:** This is the **abstract's lower envelope of the BF range** ("$\mathrm{BF}\,{\sim}\,6$--$17$"). If the lower end is actually BF≈4, the abstract envelope is `BF ~ 4-17`, with the headline (recommended baseline σ_th=1.0/broad) at BF≈9.8 — meaning the bounce is favored at the BF=9.8 level over tuned-multifield, **stronger** at the recommended baseline than the paper claims, but the **lower-corner envelope falls below the Kass-Raftery 'strong evidence' threshold of BF=10** rather than sitting comfortably at BF=6 above the BF=3 'positive evidence' threshold. Specifically: the narrow-competitor curvaton-natural corner at BF≈4 is in the 'positive but not strong' Kass-Raftery band, weaker than the paper's BF~6 framing implies. An external referee running the same arithmetic check (which is one scipy call) will see the discrepancy immediately.

**Hard-fix (v1.7.35):** Recompute the four-corner grid from the explicit analytic formula `BF = W_comp · ∫π_b(fnl)·L(obs;fnl,σ_obs)dfnl / ∫_{a}^{b} L(obs;fnl,σ_obs)dfnl` with σ_obs=0.7, obs=-4.375, π_b = N(-4.375, σ_th²), and report the four corners as: delta/narrow=7.0, delta/broad=17.1, gauss/narrow=4.0, gauss/broad=9.8. Update L29 abstract to "$\mathrm{BF}\,{\sim}\,4$–$17$" (or, if preferred, anchor to the recommended baseline only: "$\mathrm{BF}\approx 9.8$ at the recommended physically motivated baseline"). Update L216, L260 Table, L266, L293. The fix is a one-paragraph + one-table-cell + abstract-envelope edit; it strengthens the headline (BF=9.8 instead of BF=8) at the cost of widening the envelope downward.

**Severity:** MAJOR — this is the paper's primary Bayesian-discrimination result, the arithmetic is reproducible in 10 lines of scipy, and the discrepancy is at the abstract-headline level. A clean cascaded-loop-exit cannot proceed without closing this.

---

### minor-1 — BF=8 broad-Gaussian baseline understates the analytic BF=9.8 by ~20%

**Location:** L29 abstract ("$\mathrm{BF} \approx 8$ at the recommended physically motivated baseline ($\sigma_{\rm theory} = 1.0$ Gaussian bounce prior, broad multifield competitor prior $[-15,+15]$)"); L241 ("Gaussian prior, $\sigma_{\rm theory} = 1.0$ (recommended baseline, encompassing both literature values and the full $\epsilon$-correction range): $\sim 8$"); L260 Table; L281 Table~\ref{tab:bayes} row 1.

**Issue:** Analytic recompute (using the same arithmetic that gives exact agreement on the delta-prior rows and the recommended-baseline corner) returns BF = 9.80 at σ_th=1.0/broad, **not** BF=8. Direction is opposite to MAJOR-1 (paper understates by 20%), and the discrepancy is smaller in magnitude, but inconsistent with the framework: if the delta-rows match to four significant figures (17.10 ↔ 17, 7.00 ↔ 7), the Gaussian rows should also match. The σ_th=1.0/broad ≈ 9.8 result is robust under any reasonable variant of the formula (Gaussian-on-Gaussian convolution is fixed by σ_eff = sqrt(σ_obs² + σ_th²) = sqrt(0.49+1.0) = 1.221).

**Speculation on origin:** The paper's BF=8 may come from including a numerical Monte Carlo result that adds ~20% jitter, OR from a slightly different definition of the Gaussian prior normalization (e.g., truncated at $\pm 3\sigma_{\rm th}$ rather than full-real-line). Neither variant is documented in the prose.

**Hard-fix:** Either (a) replace BF~8 with BF~10 (the truncation-to-significant-figures of 9.80), making it slightly more bullish on the bounce, OR (b) add one sentence clarifying that the BF~8 includes a ~20% downward Monte-Carlo penalty / σ_GR=0.5 effective broadening / etc. — i.e., explain why the analytic-formula reader gets 9.8 and the paper's recommended-baseline cell says 8.

**Severity:** MINOR — does not flip any qualitative conclusion (BF~8 and BF~10 are both 'strong evidence' under Kass-Raftery), but introduces ~20% inconsistency between the paper's own arithmetic-formula corner (delta-rows exact) and the Gaussian-row corners. An external referee running the BF recompute will notice.

---

## Stress-test vectors that the paper SURVIVED cleanly

| Vector | Audit | Verdict |
|---|---|---|
| **(a) bispectrum-only 5.2-5.5σ optimistic baseline** | Anchored to $|f_{NL}|\cdot r/\sigma = 4.375 \cdot 0.83$–$0.876/0.7 = 5.19$–$5.47$. Arithmetic exact. The "optimistic" framing is explicitly labeled "before GR and $b_\phi$ degradation", and the post-systematic 3–5σ headline absorbs both. The L191 shot-noise caveat correctly flags that the Heinrich baseline assumes $\bar n \sim 10^{-3}\,h^3\,\mathrm{Mpc}^{-3}$ and that anomaly-selected subsamples would degrade. | ✅ Clean |
| **(c) Heinrich+2023 σ(f_NL)=0.7 spec-vs-SPHEREx-reality** | L185 explicitly cites Heinrich+2024 = PRD 109 123511, arXiv 2311.13082, the Heinrich-Doré-Krause "Measuring f_NL with the SPHEREx Multi-tracer Redshift Space Bispectrum" paper, with the SPHEREx-selected ELG redshift distribution z≈0.5–2. L187 explicitly flags three caveats: (1) b_φ universality vs free-per-bin marginalization (`O(20-50%)` widening), (2) local-template-only assumption (mismatch handled via r=0.84), (3) full-SPHEREx-depth assumption (early-data-release degradation). The "leading-order linearization that the Fisher matrix is approximately invariant under fiducial shifts of order the parameter uncertainty" caveat at L185 is the **standard but non-trivial Fisher-forecast assumption** that recasts a σ(f_NL=0)≈0.7 forecast onto σ(f_NL=-4.375). This is an honest disclosure of the known limitation. | ✅ Clean |
| **(d) Wilson-Ewing class restriction flagging** | L29 abstract (assumption (e)), L57 intro ("erases the f_NL signal and replaces it with the standard slow-roll value"), L133 assumption (e) with explicit $N_{\rm tot} \gg 60$ threshold and Zhu-Cai 2026 citation as the prolonged-inflation counterexample, L434 conclusion. The restriction is flagged in **four** distinct prose locations and is the load-bearing assumption (e) of the paper. | ✅ Clean |
| **(e) Li & Brandenberger c=1 vs Cai c=2 halving** | Explicitly resolved at three levels: (i) abstract L29 caveat reports the halved 2.6–2.75σ range, (ii) Appendix A.1 (L466) gives the explicit Wick-doubling operator-algebra derivation $i\langle[\zeta^3,L]\rangle = -2\,\text{Im}\langle\zeta^3 L\rangle$, (iii) Appendix A.2 dual-normalization Fisher table (L528). The 0.5000 ε-decomposition ratio is the independent empirical signature. Honest disclosure throughout — "the convention sensitivity should be resolved before SPHEREx data are interpreted" (L29). | ✅ Clean |
| **(f) ε-correction range 0.6–8%** | Direct arithmetic check: at $\kappa_1=5.6$, $\Delta\epsilon=-0.0045$ → $\Delta f_{NL}=+0.025$ = 0.6% of 4.375. At $\kappa_1=80$, $\Delta f_{NL}=+0.36$ = 8.2% of 4.375. The κ₁=80 case gives 8%, NOT 30% as R-next-a's MAJ-1 falsely claimed. R-next-a was correctly self-falsified by Houston/v1.7.34 truth-audit; the 0.6–8% range is the correct propagation of the κ₁∈[5.6,80] uncertainty into the f_NL prediction at quasi-dust Δw=-0.003. | ✅ Clean (R-next-a falsification re-verified) |
| **(g) Joint $(f_{NL}, n_{f_{NL}})$ Fisher 9.9σ deferral** | L418 §sec:discussion gives a model paragraph: explicitly flags that the joint-Fisher 9.9σ figure is an "idealized-Fisher self-consistency check" not a competing forecast, that the unmarg σ(f_NL)≈0.114 is "sharper than any published SPHEREx SDB forecast known to us", that "the 6-bin Fisher inputs are not yet on disk in this release", and that the figure should be read as "self-consistency check on the arithmetic" not "independent detection forecast". The L29 abstract correctly **does not quote** the 9.9σ number, deferring to the companion artifact. This is a model deferral — the load-bearing quantity is NOT being smuggled into the headline. | ✅ Clean |

---

## Closing

R-next-c on v1.7.34 returns **0 BLOCKER / 1 MAJOR / 1 MINOR / 0 NIT**.

Per the §4.4.1 cascaded-loop-exit rule, the streak needs:
- Three rounds (R-next-a + R-next-b + R-next-c), under three different model-class perspectives, each returning **≤ 0 MAJOR + ≤ 2 MINOR**.
- R-next-a (theoretical-physics): 2 MAJ → 0 MAJ after v1.7.34 closure of MAJ-2 + falsification of MAJ-1.
- R-next-b (Perplexity-citation): 0 MAJ / 2 MIN — clean.
- R-next-c (brutal-honesty-Grok, this round): **1 MAJ / 1 MIN — NOT clean.**

**The streak is BROKEN at round 2-of-3** by the BF=6 → BF=4 arithmetic finding. A v1.7.35 closure of MAJOR-1 (recompute the four-corner grid, update abstract envelope to BF~4-17 or BF~10 baseline) is required before a fresh three-round streak can commence.

The MAJOR is **closable in a single v1.7.35 edit**: it is a 10-line scipy recompute, a one-table-cell update, an abstract envelope rewrite, and a §sec:bayesian prose tweak. PDF impact <1KB. No re-derivation of physics, no new figures, no new MCMC.

**Recommended next action for Houston:**
1. v1.7.35 closure of MAJOR-1 (BF four-corner grid recompute) + MINOR-1 (BF~8 → BF~10 truncation, or one-sentence Monte-Carlo-penalty explanation).
2. Re-run R-next-c brutal-honesty stress-test on v1.7.35 to verify zero residual MAJORs.
3. If clean, proceed to R-next-d for round 3-of-3 of the fresh §4.4.1 cascaded-loop-exit streak.

**Readiness impact:** 95% cap holds. Honest mid-streak rollback to ~90% is appropriate while MAJOR-1 is open (this is a load-bearing arithmetic finding at the abstract-envelope level, not a deferrable minor). Forward step to 93–95% after v1.7.35 closure + clean R-round-d. The 95% ceiling remains gated on a clean three-round cross-model streak PLUS the still-blocked external 5-vendor wave PLUS Houston sign-off.
