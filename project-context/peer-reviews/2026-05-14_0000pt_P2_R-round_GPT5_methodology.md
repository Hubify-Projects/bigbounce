# P2 R-Round — GPT-5 Methodology Adversarial Review

**Date:** 2026-05-14 00:00 PT
**Reviewer:** GPT-5 (simulated, methodology-focused)
**Target:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.27
**Scope:** Residual methodological issues that prior reviewers (GPT-5 R1, Gemini-3.1-Pro, Grok-4, Perplexity, DeepSeek) missed on v1.7.26→v1.7.27. Quantitative checks: formula derivations, statistical-method scrutiny, dimensional analysis, propagation of uncertainties.

---

## Findings (8 total: 0 BLOCKER, 3 MAJOR, 3 minor, 2 nit)

---

### P2-GPT-M1 — MAJOR — Joint-Fisher arithmetic identity is self-undermining

**Location:** §VII.D (Discussion / "Joint $(\fnl, n_{\fnl})$ Forecast"), lines 367–369; also abstract.

**Issue.** The paper writes:

> "$\sigma(n_{\fnl}) = 0.086$, $\sigma_{\rm marg}(\fnl) = 0.44$, $\rho = 0.966$ ... $\sigma_{\rm marg}/\sigma_{\rm unmarg} = 1/\sqrt{1-\rho^2} \approx 3.86$ at $\rho = 0.966$ ... the implied $\sigma_{\rm unmarg}(\fnl) = \sigma_{\rm marg}/3.86 \approx 0.114$ ... would be $6.1\times$ sharper than the bispectrum-only $\sigma(\fnl) = 0.7$ baseline, which is sharper than any published SPHEREx SDB forecast known to us."

This is a self-flagged contradiction the paper raises but then proceeds to *quote the 9.9σ number anyway* (in the abstract, headline list, and §VII.D). If $\sigma_{\rm unmarg} = 0.114$ implies a Fisher 6× tighter than every published SPHEREx forecast (Doré+2014, Heinrich+2024, Münchmeyer+2019), then either (a) the assumed $\sigma(n_{\fnl}) = 0.086$ is wrong, (b) the assumed $\rho = 0.966$ is wrong, or (c) the 6-bin SDB Fisher stack is unrealistic — *not* simply "an internal-consistency check." A real methodology-respecting paper would either (i) drop the 9.9σ entirely, or (ii) re-derive $\sigma(n_{\fnl})$ from on-disk Fisher inputs before quoting.

The current treatment — "we admit it's not credible but still report it as the headline-adjacent figure" — is methodologically inconsistent with the v1.7.27 promotion of the bispectrum-only 5.2–5.5σ as the headline. The abstract still leads with "${\sim}\,9.9\sigma$ marginalized over $n_\fnl$".

**Fix.** Either (a) compute the 6-bin SDB Fisher inputs in-repo and back $\sigma(n_{\fnl})$ out from a real Fisher rather than asserting it (only credible path); or (b) remove the 9.9σ from the abstract and §VII.D and replace with "joint $(\fnl, n_{\fnl})$ forecast deferred to companion artifact pending Fisher-input release." Option (b) is the minimum methodological hygiene fix; option (a) is the complete fix.

---

### P2-GPT-M2 — MAJOR — Template-overlap variance $\pm 0.02$ is not what the scan produces

**Location:** §III.B (eq. r_noise, line 137); abstract.

**Issue.** Two different $r$ scans are reported as if they are one combined uncertainty:
1. **10-weighting-scheme scan over $x_{3,\rm min}$:** range $r \in [0.821, 0.879]$, central $r = 0.84 \pm 0.02$.
2. **10,000-sample null-space scan over $(c_1,...,c_6)$:** $r = 0.85 \pm 0.13$, range $0.55$–$1.14$, IQR $[0.75, 0.94]$.

The headline equation `eq:r_noise` quotes only (1). But the *physical* template-overlap uncertainty is a *joint* draw over both the noise weighting *and* the polynomial-coefficient null-space — these are independent sources of shape uncertainty that must be combined, not reported alternately. Quoting $\pm 0.02$ as the template-overlap uncertainty in the headline (and thereby in the 5.2–5.5σ optimistic range) ignores the much larger $\pm 0.13$ scatter from null-space coefficients (a ${\sim}15\%$ amplitude uncertainty in $r$).

Even granting that the median over 10,000 samples is $r = 0.85$ (consistent with the 10-scheme central value $0.84$), the *uncertainty* on $r$ that should propagate into $\sigma(\fnl^{\rm bounce})$ is $\sqrt{0.02^2 + 0.13^2} \approx 0.132$, not $0.02$. This widens the 5.2–5.5σ optimistic range by a factor $0.84/(0.84-0.13) = 1.18$ on the low side and shifts the realistic headline from 5.2σ → as low as 4.4σ on the same Fisher inputs.

**Fix.** Either (a) propagate the polynomial-null-space $\pm 0.13$ into the headline systematic budget (degrades optimistic to ${\sim}4.4$–$5.5\sigma$), or (b) explicitly argue that the null-space scan is methodologically distinct (e.g., it samples polynomial degeneracy at fixed Cai benchmarks while the noise-scheme scan samples observational weighting at fixed polynomial), and that only one belongs in `eq:r_noise`. Either argument must be made explicitly. Current paper has it both ways.

---

### P2-GPT-M3 — MAJOR — ε-correction "1–8%" uncertainty is not propagated into $\sigma_{\rm theory}$

**Location:** §II.C (Assumptions, line 100); §V.C (Bayesian, line 207); Table II row labels.

**Issue.** The ε-correction shifts $\fnl$ from $-4.375$ toward $-4.02$ (a $\sim 8\%$ relative shift; range $\fnl \in [-4.35, -4.02]$). This is the *central-value* uncertainty in the bounce prediction, not a uniform random draw. The paper folds it into the $\sigma_{\rm theory}$ Gaussian prior on the bounce (e.g., $\sigma_{\rm theory} = 0.5$ "encompassing the central ε-correction window") — but a unidirectional bias ($\fnl$ shifts *toward* zero from $-4.375$, never below) is not Gaussian-distributed. A Gaussian prior centered at $-4.375$ symmetrically penalizes $\fnl < -4.375$ as much as $\fnl > -4.375$, which is wrong: the bounce model itself predicts no value below $-4.375$ (the squeezed-limit floor) under quasi-dust, so the ε-correction prior is one-sided.

**Implication.** The Bayes-factor row $\sigma_{\rm theory} = 0.5$ → BF ${\sim}\,12$ is *over*-penalized at the favorable end (low $|\fnl|$) and *under*-penalized at the predicted endpoint $-4.375$. A correct treatment uses a *half-Gaussian* or *uniform-on-$[-4.375, -4.02]$* prior. The BF would shift to ${\sim}\,14$–$15$ under a half-Gaussian, with the $\sigma_{\rm theory} = 1.0$ headline shifting from ${\sim}\,8$ to ${\sim}\,10$.

**Fix.** Replace symmetric-Gaussian $\sigma_{\rm theory}$ with a one-sided prior reflecting the ε-correction physics. Document the change in §V.C. The headline BF should rise modestly.

---

### P2-GPT-m1 — minor — Joint $(f_{\rm NL}, n_{\rm fNL})$ correlation $\rho = 0.966$ is not justified from first principles

**Location:** §VII.D (line 369).

**Issue.** The correlation $\rho = 0.966$ between $\fnl$ and $n_{\rm fNL}$ in the 6-bin SDB Fisher is asserted without derivation. The paper notes "this degeneracy arises because both parameters modulate the large-scale bias through the same $1/k^2$ transfer kernel," which is the right qualitative argument, but in a 6-bin Fisher *the redshift evolution* of the transfer kernel breaks the degeneracy — that's the whole point of multi-bin SDB. A value $\rho = 0.966$ implies the 6 bins provide almost no leverage on $n_{\rm fNL}$, which seems too pessimistic given the Heinrich+2024 redshift range $z \approx 0.5$–$2$.

**Fix.** Either cite a published 6-bin SDB Fisher (e.g., Sailer+2021, Castorina+2020) that gives a comparable $\rho$, or qualify with "ρ is the maximally-degenerate idealized case; a realistic 6-bin Fisher would partially break this."

---

### P2-GPT-m2 — minor — Bayes factor 6×10⁵ MC realizations: convergence not demonstrated

**Location:** §V.C (line 198–202).

**Issue.** The "$>\!6\!\times\!10^5$ Monte Carlo realizations" is asserted as validation of the analytic BF formula, but no convergence diagnostic is provided (no plot of running BF vs. MC sample count, no bootstrap error on BF, no chi-square goodness-of-fit between MC histogram and analytic Gaussian). The number "6×10⁵" is suspicious because it's exactly 600,000 — a round number that suggests target rather than convergence-driven sample size. Methodologically, the right reporting is "BF converged to ±X at N realizations; ran an additional 2N realizations to confirm stability."

**Fix.** Add a one-sentence convergence diagnostic in §V.C: "Bootstrap resampling over the 6×10⁵ realizations gives BF stable to $\pm 0.3$ at the $\sigma_{\rm theory} = 1.0$ baseline; running to $1.2 \times 10^6$ realizations changes the headline BF by $<\!0.1$."

---

### P2-GPT-m3 — minor — "BF vs SSFSR" column reports $3.3 \times 10^6$ and $329$ without prior specification

**Location:** Table III (`tab:gr`, line 282–294).

**Issue.** The Bayes factor against standard single-field slow-roll inflation (SSFSR) varies from $3.3 \times 10^6$ (Ideal/no GR) to $329$ (σ_GR = 1.0) — a *four-orders-of-magnitude* dynamic range that the table reports without disclosing what makes them so different. The SSFSR prediction is $\fnl \approx 0.015$, which is $\approx 4.4\sigma$ from the SPHEREx mock-detected $\fnl = -4.375$ even with σ_GR = 1.0 systematics. The BF should be dominated by the likelihood ratio at that separation, *not* by the prior structure. The 4-order range therefore reflects something other than the SSFSR-vs-bounce discrimination — likely the SSFSR prior width is being held fixed while σ_GR is varied. This is *not* the right BF if the GR systematic is correlated between the two hypotheses.

**Fix.** Disclose the SSFSR prior assumed in Table III caption (e.g., "delta function at $\fnl = +0.015$" or "Gaussian with $\sigma = 0.01$"). If the $3.3 \times 10^6$ value relies on a delta-function SSFSR prior, demote it to a row footnote and quote the more defensible Gaussian-prior BF in the main column.

---

### P2-GPT-nit1 — nit — Convention-halving abstract sentence has unparseable scope

**Location:** Abstract, last sentence (line 29).

**Issue.** The abstract concludes with:

> "the optimistic, pre-systematic-budget $5.2$–$5.5\sigma$ range halves to ${\sim}\,2.6$–$2.75\sigma$ (the abstract previously gave only the central $\sim 2.6\sigma$; the upper-bound of the halved range is reported here for completeness)"

The parenthetical "(the abstract previously gave only..." is a *revision-history comment* — a meta-statement about the paper itself — that should not appear in an arxiv abstract. It reads as draft-tracker debris.

**Fix.** Delete the parenthetical. Result reads cleanly: "the optimistic, pre-systematic-budget $5.2$–$5.5\sigma$ range halves to ${\sim}\,2.6$–$2.75\sigma$, and the post-systematic-budget headline $3$–$5\sigma$ halves to ${\sim}\,1.5$–$2.5\sigma$."

---

### P2-GPT-nit2 — nit — `eq:projection` claim "$0 < r \leq 1$ holds strictly" is contradicted in the same paragraph

**Location:** §III.B (lines 127–133).

**Issue.** Paper states: "$r$ is positive definite and is bounded above near unity for physical bispectrum shapes dominated by the squeezed limit. The canonical inequality $0 < r \leq 1$ holds strictly for canonical single-field bispectra ... for the matter-bounce shape, the weighted average can mildly exceed unity (up to $r \lesssim 1.2$)..."

The phrase "holds strictly for canonical single-field bispectra" is fine, but then the *immediately following* footnote spends 6 lines defending why the constraint is *violated* (samples with $r > 1$ retained without truncation, full distribution $r = 0.85 \pm 0.13$ range $0.55$–$1.14$). The current text reads as if it's both asserting and refuting the same inequality in the same paragraph.

**Fix.** Replace "The canonical inequality $0 < r \leq 1$ holds strictly..." with "For canonical single-field bispectra normalized to their own squeezed limit, $r \leq 1$ is automatic; for the matter-bounce polynomial null-space, this monotonicity does not hold, and we retain the full $r$ distribution including $r > 1$ samples (see footnote)." Cleaner.

---

## Summary

No BLOCKERs found at the methodological level. The 3 MAJORs are real but bounded:
- **M1** (9.9σ identity vs. Fisher inputs) requires either dropping the abstract figure or computing the 6-bin Fisher in-repo. The paper *already self-flags* this as a self-consistency check rather than a measurement, but still leads the abstract with it — that's the contradiction.
- **M2** (template-overlap variance combining) widens the optimistic range by ${\sim}\,0.8\sigma$ on the low end.
- **M3** (ε-correction prior one-sidedness) is a real but small effect — the headline BF would rise slightly under a corrected prior.

The 3 minors and 2 nits are presentational / prior-disclosure issues that don't change the science.

**Net assessment.** Paper v1.7.27 is materially clean on the core Cai $\fnl = -35/8$ derivation, the convention-halving disclosure, the Bayes-factor prior-grid mapping, and the Heinrich-2024 $\sigma(\fnl) = 0.7$ fiducial-shift caveat. The methodology weakness concentrates on (a) the joint $(f_{\rm NL}, n_{\rm fNL})$ Fisher being asserted rather than computed and (b) the template-overlap uncertainty being under-stated by a factor of ${\sim}6$ via separation of weighting-scheme and polynomial-null-space scans. Both are fixable in one revision without rerunning any MCMC or simulations.
