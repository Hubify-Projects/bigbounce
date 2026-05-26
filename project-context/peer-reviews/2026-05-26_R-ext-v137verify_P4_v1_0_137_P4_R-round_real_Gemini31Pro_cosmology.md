# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v137verify_P4_v1_0_137
**Wall time**: 110.9s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=106045, completion=11703, reasoning=10447, total=117748

---

## PAPER-GEM-B1: Misinterpretation of Marginalized Posterior in Joint Fit (BLOCKER)
**Section:** VI.D (Joint nuisance-marginalized model fit)
**Issue:** The text claims the $0.23\%$ residual dipole in the joint fit "absorbs the same template structure" and is "formally consistent with interpretation (ii)" (a depth/PSF/morphology systematic). This is mathematically backwards. In multiple linear regression, the marginalized dipole posterior represents the signal *orthogonal* to the nuisance templates. A $40.9\sigma$ detection of a $0.23\%$ dipole in this posterior means the 9 templates *failed* to absorb it, leaving a highly significant unexplained dipole.
**Fix:** Correct the interpretation to state that the $0.23\%$ residual is the component *orthogonal* to the 9-template model, indicating that density and leg-fractions alone are insufficient to fully absorb the canonical-mask excess, requiring the full morphology/PSF basis (or representing a real signal).

## PAPER-GEM-B2: Impossible Bernoulli Variance in Hard-Label Flip Derivation (BLOCKER)
**Section:** III.E (Hard-label variance widening)
**Issue:** The derivation $\sigma_{total} \approx \sigma_{binomial} \sqrt{1 + p_{flip}(1-p_{flip})/[p(1-p)]}$ violates the Law of Total Variance. A binary variable $x_{obs} \in \{0,1\}$ cannot have a variance exceeding $0.25$. You incorrectly added the conditional variance to the unconditional variance. Flip noise *dilutes the signal expectation* (which you handled correctly in Sec III.A) but does *not* inflate the observed per-bin variance above $p_{obs}(1-p_{obs}) \le 0.25$.
**Fix:** Remove the $1.21x$/$1.29x$ variance inflation factor for observed counts. State instead that flip noise dilutes the signal by $(1-2p_{flip})$, which inflates the *inferred* cosmological dipole error by $\sim 1.75x$, but the *observed* per-bin scatter remains strictly binomial.

## PAPER-GEM-M1: Contradiction in "Formal Exclusion" Logic vs 40.9-sigma Residual (MAJOR)
**Section:** VI.D (Joint nuisance-marginalized model fit)
**Issue:** You claim "INTERPRETATION (i) AT 1.7% f_CW IS FORMALLY EXCLUDED AT 99% CONFIDENCE". While true for the specific $1.7\%$ value, the same fit yields a $40.9\sigma$ detection of a $0.23\%$ dipole. If interpretation (i) is "a clean real cosmological dipole", your fit formally *detects* a cosmological dipole at $0.23\%$ (unless attributed to missing templates). You cannot claim a clean exclusion of the dipole hypothesis when your fit returns a $40.9\sigma$ dipole detection.
**Fix:** Clarify that the fit formally excludes the *Shamir-scale $1.7\%$ amplitude*, but strongly detects a $0.23\%$ residual dipole, meaning the 9-template model does not yield a null dipole and requires further systematic templates (like PSF/fracdev) to close.

## PAPER-GEM-M2: Linear Algebra Error in Collinearity Description (MAJOR)
**Section:** VI.D (Joint nuisance-marginalized model fit)
**Issue:** The text states "the three fractions plus a constant span a 3-dimensional null subspace". Four columns (3 leg fractions + 1 constant) with one linear constraint ($f_1+f_2+f_3 = C$) span a 3-dimensional *column space* and have a 1-dimensional *null space*, not a 3-dimensional null space.
**Fix:** Change "span a 3-dimensional null subspace" to "span a 3-dimensional column space with a 1-dimensional null space".

## PAPER-GEM-m1: Imprecise EFT of LSS Parameterization Claim (minor)
**Section:** VI.H (Parity-odd galaxy-trispectrum amplitude)
**Issue:** The text claims "$g_*$ itself parameterizes the primordial inflationary parity-odd coupling, not an LSS operator". In Cabass et al. 2022, $g_*$ is used in the power counting of the EFT of Inflation, but the actual LSS observables are parameterized by Wilson coefficients (like $b_{\mathcal{E}}$) which map to the inflationary cutoff $\Lambda_{PV}$ or dimensionless coefficients. The phrasing oversimplifies the EFT mapping.
**Fix:** Soften to "$g_*$ parameterizes the power counting of the inflationary parity-odd coupling, which maps to late-time LSS Wilson coefficients".

## PAPER-GEM-n1: Z-score Rounding Mismatch (nit)
**Section:** VI.D (Joint nuisance-marginalized model fit)
**Issue:** The text states "z(data vs 1.7%) = -264.5" with $\sigma = 0.006\%$. However, $(0.23 - 1.7) / 0.006 = -245$. The true sigma used for the $z=-264.5$ calculation was $\sim 0.005557\%$. Rounding $\sigma$ to $0.006\%$ in the text makes the explicit $z$-score arithmetic look wrong to a reader checking the math.
**Fix:** Change "sigma_A_dipole = 0.006%" to "sigma_A_dipole = 0.0056%" to make the $z$-score arithmetic transparently correct.
