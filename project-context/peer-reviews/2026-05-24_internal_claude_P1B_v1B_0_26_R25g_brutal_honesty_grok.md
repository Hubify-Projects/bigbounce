# P1B v1B.0.26 — R25g brutal-honesty-Grok verdict

**Round:** 3-of-3 cross-model rotation streak (after R25e DeepSeek-confab CLEAN + R25f theoretical-physics-Gemini CLEAN)
**Artifact:** `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.tex` (986 lines, v1B.0.26)
**Reviewer perspective:** brutal-honesty stress-test (Grok-4.3 style); adversarial mindset; assume hidden flaw
**Cross-checked artifacts:** `reproducibility/cosmology/iter2_converged_2026-05-18/posterior_summary.txt`, `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json`

---

## Summary

**1 MAJOR + 1 MINOR + 1 nit.** The streak is BROKEN at round 3-of-3. The v1B.0.26 R25d-MAJ-1 caption rewrite at L379 introduced a NEW factual inaccuracy: the claim that iter2 "trades one frozen-chain Planck-likelihood nuisance for a different foreground-amplitude/spectral-index split" is false against the on-disk chain header — the foreground amplitudes and spectral indices are IDENTICAL between frozen and iter2 chains; the actual difference is that the frozen chain has $M_b$ (SH0ES SN-Ia absolute magnitude) as a 10th nuisance which iter2 drops. The "trade" is M_b → ∅, not "foreground split swap." This is the kind of caption-rewrite regression that the cascaded-loop protocol is specifically designed to catch.

§4.4.1 cascaded-loop-exit gate NOT SATISFIED — recommend v1B.0.27 surgical rewrite of L379 caption to correctly characterize the trade, then restart the 3-round clean streak.

---

## MAJOR FINDINGS

### MAJ-1 (NEW, R25g-introduced via R25d-MAJ-1-fix regression): L379 caption claim "trades one frozen-chain Planck-likelihood nuisance for a different foreground-amplitude/spectral-index split" is FACTUALLY WRONG

**Location:** `arxiv/paper1b_mcmc_companion.tex` L379, table caption for `tab:iter2_posterior`.

**Verbatim claim (post-R25d-MAJ-1 rewrite):**
> "...the iter2 chain trades the frozen-chain $\Delta N_{\rm eff}$ in the cosmological block for the extended-parameter pair $(w, w_a)$, **and trades one frozen-chain Planck-likelihood nuisance for a different foreground-amplitude/spectral-index split**; the totals match by construction at $k_{\rm sampled}=17$ but the parameter spaces are otherwise distinct..."

**On-disk nuisance enumeration:**

- **Frozen ΛCDM+ΔNeff (Table I footnote L365, `convergence_latest.csv`):** A_planck, amp_143, amp_217, amp_143×217, n_143, n_217, n_143×217, calTE, calEE, **M_b** = **10 nuisance**.
- **iter2 DESI DR2 w0wa (`posterior_summary.txt` L18-19 + L96-99):** A_planck, amp_143, amp_217, amp_143×217, n_143, n_217, n_143×217, calTE, calEE = **9 nuisance**.

**Direct comparison:** all six CamSpec foreground amplitudes and spectral indices (`amp_143`, `amp_217`, `amp_143×217`, `n_143`, `n_217`, `n_143×217`) PLUS A_planck/calTE/calEE are **IDENTICAL** between the two chains. The only difference in the nuisance block is the SH0ES SN-Ia absolute magnitude $M_b$, which is sampled in the frozen full-tension chain (with `H0.riess2020Mb` active per the v1B.0.14 audit at L460-462) and absent in iter2 (which has no SH0ES likelihood, per the explicit caveat at L453-454 "the iter2 chain is BAO + CMB + SN-only, no local-distance ladder").

**Implication:** the actual cosmological+nuisance trade structure is:
- Cosmological (frozen 7 → iter2 8): adds (w, w_a), drops ΔNeff. Net +1.
- Nuisance (frozen 10 → iter2 9): drops M_b. Net −1.
- Totals match at 17 by **construction-via-dropping-SH0ES**, NOT by "foreground split swap."

The R25d-MAJ-1 rewrite tried to explain WHY both chains hit k=17 and got the structural answer wrong. R25e (DeepSeek) + R25f (Gemini) missed this because they accepted the caption's surface narrative without cross-checking against the chain header. Brutal-honesty round is supposed to be the safety net against exactly this kind of "elegant narrative defeats fact-check" error.

**Severity rationale:** MAJOR not BLOCKER because the headline numbers ($w_0=-0.812\pm0.044$ at +4.3σ, $w_a=-0.667\pm0.186$ at −3.6σ) and the totals (17 = 17) are unaffected. But the caption is publicly false and an external referee reading the on-disk `posterior_summary.txt` parameter audit (which the caption explicitly hyperlinks to) will catch the discrepancy immediately. Houston-method §4.4.1 requires zero false statements at the caption level.

**Surgical fix for v1B.0.27:** rewrite L379 trade-clause to:

> "...the iter2 chain trades the frozen-chain $\Delta N_{\rm eff}$ in the cosmological block for the extended-parameter pair $(w, w_a)$ (net +1 cosmological), and drops the frozen-chain $M_b$ SH0ES SN-Ia absolute-magnitude nuisance (the iter2 likelihood stack is BAO + CMB + SN-only with no local-distance ladder, see caveat (c) at L453-454; net −1 nuisance); the totals match at $k_{\rm sampled}=17$ via this +1/−1 construction, but the parameter spaces are otherwise distinct (the six CamSpec foreground amplitudes and spectral indices are identical between the two chains)."

---

## MINOR FINDINGS

### MIN-1: ALP β-range "joint-trajectory scan" clarification at L700-705 is physically defensible but does not fully justify why a $C_{a\gamma}=4 \times \Delta\phi/f_a=0.2$ corner is excluded

**Location:** L697-705.

**Verbatim:**
> "The prediction spans $\beta\approx 0.17$--$0.43^\circ$ over $C_{a\gamma}\in[4,12]$, $m/H_0\in[1,3]$, $\theta_i\in[0.5,2]$, comfortably bracketing the observed value without fine-tuning. The range $[0.17,0.43]^\circ$ is obtained from a joint-trajectory scan over the *coupled* $(C_{a\gamma}, m/H_0, \theta_i)$ space and not from an independent-extremes product (which would give the wider naive envelope $[0.027,0.44]^\circ$); $\Delta\phi/f_a$ is a function of $m/H_0$ and $\theta_i$ along ALP trajectories rather than an independent variable (R25b-BLK-1 clarification, v1B.0.24)."

**Brutal-honesty take:** $\Delta\phi/f_a$ being a function of $(m/H_0, \theta_i)$ is a true statement, but $C_{a\gamma}$ is genuinely independent of $(m/H_0, \theta_i)$ — the photon-coupling is a Lagrangian parameter, not an EOM-derived quantity. So the corner $C_{a\gamma}=4 \wedge \Delta\phi/f_a=0.2$ is physically populated (it occurs when $\theta_i=0.5, m=H_0$, $C_{a\gamma}=4$) and gives $\beta = 4 \times 0.2 \times 0.0333 \approx 0.027°$. The claim that a "joint-trajectory scan" excludes this corner is not justified by the "$\Delta\phi/f_a$ depends on $(m/H_0, \theta_i)$" argument alone — the additional restriction must come from somewhere else (e.g., MCMC posterior weighting), which the paper does not specify.

**Severity:** MINOR because both ranges ([0.17,0.43] and [0.027,0.44]) are explicitly named in the paper, and both comfortably bracket the observed $\beta = 0.342°$. R25b accepted the "joint-trajectory scan" framing as partial-falsification; R25g brutal-honesty re-flags it because the language papers over the underlying degeneracy rather than resolving it. Houston-judgment item for v1B.0.27+ batch.

**Suggested fix:** add one sentence clarifying that [0.17, 0.43] is obtained from MCMC posterior weighting (i.e., the joint posterior $P(C_{a\gamma}, m/H_0, \theta_i)$ from the 9,720-sample ALP-MCMC chain) rather than an a-priori scan, and that the [0.027, 0.44] envelope corresponds to the unweighted parameter-corner extrema. This converts the framing from "joint-trajectory scan excludes corners" (physically not motivated) to "MCMC posterior down-weights corners" (statistically motivated).

---

## NIT FINDINGS

### NIT-1: Inconsistent target-version markers for the nested-sampling $\ln B$ recompute scattered through paper

Current paper version: **v1B.0.26**. Target-version markers for the nested-sampling deferral appear at:
- L431: "v1B.0.14"
- L446, L943: "v1B.0.15+"
- L819: "v1B.0.16+"
- L886: "v1B.0.17+"
- L656, L970: "v1B.0.18+"

ALL of these target versions are in the past relative to the current v1B.0.26 artifact. While each individual marker was correct at the time of its insertion, the resulting paper reads as if the author has repeatedly slipped the deadline without acknowledging it. This is the kind of staleness external reviewers notice and lose confidence over.

**Severity:** NIT, deferrable. Houston should batch-rewrite all "v1B.0.X+ pending" markers to a single consistent forward target (e.g., "next nested-sampling iteration" or "v1B.0.30+") in a future polish pass.

---

## ITEMS CONFIRMED CLEAN

- **(a) +4.3σ caveat propagation:** all 6 sites confirmed to carry the caveat. L385 (table cell, `\footnote{\label{fn:wcaveat}...}`), L414 (physics interp `(in the marginal-tail sense; see fn.~\ref{fn:wcaveat})`), L435-446 (Caveats paragraph with full Savage-Dickey unviability text), L656 (Model-comparison paragraph with inline Savage-Dickey caveat), L775 (mcmc_inventory caption `(fn.~\ref{fn:wcaveat})`), L835 (cross-paper P1A anchor `(fn.~\ref{fn:wcaveat})`). The R25d-MAJ-2 fix is structurally complete.
- **(d) NaMaster amplitude-dependent bias 0.032-0.040°:** confirmed against `summary.json` — only 3 injection levels (β=0, 0.27, 0.342), worst-case bias 0.040° at β=0.342° is correctly stated. No un-reported injection levels exist. The R25b-MAJ-2 fix is complete.
- **(e) Bayes-factor / model-comparison removal:** no orphan AIC/BIC/$\ln B$ numerical claims remain. All references are either historical ("removed in v1B.0.7") or to status of queued recompute work. Clean.
- **(f) cross-paper Table 1 (tab:crosspaper) staleness (P1A v1A.0.27 / P1B v1B.0.13 / P2 v1.7.30 / P3 v3.1.45 / P4 v1.0.103, P5 missing):** explicitly acknowledged-deferred at L66-67 of preamble. Deferrable per R25d-MIN-1 disposition. No escalation.
- **(g) units:** all equations have consistent units. $H_0$ in km/s/Mpc throughout; $\beta$ in degrees throughout (with explicit radian conversion at L727 `$5.97\times 10^{-3}$`); $\alpha_{\rm EM}/(4\pi)$ correctly dimensionless. Clean.

---

## DISPOSITION RECOMMENDATION

§4.4.1 cascaded-loop-exit gate **NOT satisfied for v1B.0.26**.

Required path forward:
1. **v1B.0.27 surgical rewrite** of L379 caption per MAJ-1 suggested-fix. (Houston-method full-hard-fix, no defer.)
2. **Restart 3-round clean streak** on v1B.0.27. R25e + R25f remain valid evidence that the non-caption body is clean; only L379 needs re-review.
3. Defer MIN-1 (ALP β-range MCMC framing) + NIT-1 (target-version markers) to v1B.0.28+ polish batch per standing peer-review truth-audit protocol.

The brutal-honesty round did its job: caught a NEW caption regression introduced by the previous-round MAJ-1 surgical fix that two non-adversarial reviewers (R25e DeepSeek, R25f Gemini) accepted without cross-checking against the on-disk chain header. This is exactly why cross-model rotation matters.
