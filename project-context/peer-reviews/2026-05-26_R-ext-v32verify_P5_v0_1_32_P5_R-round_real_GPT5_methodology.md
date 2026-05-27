# P5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v32verify_P5_v0_1_32
**Wall time**: 131.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29237, completion=7359, reasoning=6184, total=36596

---

## PAPER-GPT-B1 — BLOCKER

**Section:** §IV.A V-Web algorithm; §VIII T-Web/ASTRA comparisons  
**Issue:** The density field is built from raw DESI counts divided by a single global in-mask mean on a flux-limited, multi-tracer, masked survey out to \(z=2\). No DESI randoms, \(n(z)\), angular completeness, tracer selection, or boundary/window correction are applied before the FFT Poisson solve, so the “tidal” field is dominated by the survey window/selection function rather than matter overdensity.  
**Fix:** Recompute \(\delta=(n-\alpha n_{\rm rand})/(\alpha n_{\rm rand})\) with DESI randoms/selection weights or restrict to a volume-limited BGS sample with proper mask treatment; rerun all V-Web labels and downstream statistics, or demote V-Web to a heuristic and base the headline on external VACs.

## PAPER-GPT-B2 — BLOCKER

**Section:** §IV.A steps 8–11  
**Issue:** The Fourier tidal-tensor sign is wrong as written. With \(\nabla^2\Phi=\delta\), \(\Phi_k=-\delta_k/k^2\), so \(T_{ij}=\partial_i\partial_j\Phi=-k_i k_j\Phi_k=+k_i k_j\delta_k/k^2\); the manuscript uses \(T_{ij}=k_i k_j\Phi_k=-k_i k_j\delta_k/k^2\), flipping eigenvalue signs and hence web classes.  
**Fix:** Verify the code sign convention; if the code matches the text, rerun the V-Web classification and all tables. If the code is correct, fix the manuscript and add a validation test on a known overdensity.

## PAPER-GPT-B3 — BLOCKER

**Section:** Abstract; §VI.A Table II; §VII Phase 2; §VI.D tracer stratification; §IX Systematics  
**Issue:** Core counts are internally impossible. Table II environment counts sum to \(812{,}793\), not the claimed \(791{,}635\); Table II \(n_{\rm CW}\) sums to \(404{,}111\), exceeding Table I’s total CW count \(393{,}592\). Phase 2 quotes \(n=3{,}696{,}152\) for a chirality bin, larger than the matched-primary catalog, and filament-bright \(n=416{,}701\) exceeds total filament \(n=408{,}187\).  
**Fix:** Define one immutable analysis cohort per result, publish a reconciliation table, and rerun/update every \(n\), \(n_{\rm CW}\), \(f_{\rm CW}\), range, and \(\sigma\). Do not claim a \(791{,}635\)-galaxy headline while using an \(812{,}793\)-row superset.

## PAPER-GPT-M1 — MAJOR

**Section:** §V Statistical methods; §VIII “P4-monopole-residual analysis”; Conclusions  
**Issue:** The monopole correction is treated as a fixed parameter shift, not a nuisance parameter with uncertainty/covariance. The same or highly overlapping catalog is used to estimate the P5/P4 monopole and then test class residuals, but the variance of \(\sigma_{\rm vs\,monopole}\) does not propagate the fitted intercept, class-partition covariance, or Paper IV monopole uncertainty; “entirely the monopole” is overclaimed.  
**Fix:** Fit a binomial/logistic hierarchical model with a common monopole/intercept and environment offsets, marginalize over the monopole and systematic terms, and report joint intervals/LRT or Bayes factors for the environment coefficients.

## PAPER-GPT-M2 — MAJOR

**Section:** §VIII DESIVAST-anchored void classifier / three-algorithm robustness  
**Issue:** The point-in-sphere DESIVAST membership test uses a \(k=20\) nearest-hole KDTree query and asserts this is sufficient from the maximum hole radius. That is false: a containing sphere can be outside the 20 nearest centers if many non-containing centers are closer, especially in dense void catalogs.  
**Fix:** Query all candidate centers within \(R_{\max}\) using `query_ball_point`, then test exact radii; validate against catalog-native GALZONE membership and recompute all DESIVAST void/non-void fractions.

## PAPER-GPT-M3 — MAJOR

**Section:** Conclusions, “Mapping to a physical operator (v0.1.32)”  
**Issue:** The EFT parameterization is dimensionally and symmetry ill-defined. \((\nabla_i\phi)(\nabla^i\rho/\rho_{\rm bg})(\hat L\!\cdot\!\hat z)\) is not a local scalar Lagrangian operator as written: \(\hat z\) is observer-dependent, \(\hat L\) is not a fundamental field, \(g_\phi\nabla\phi/H_0\) is not made dimensionless consistently, and the bound drops the gradient length scale \(R_s\) and transfer function.  
**Fix:** Recast this as a phenomenological response \(\Delta f_{\rm CW}^{\rm env}=\beta\,\Delta_{\rm env}\) and bound \(\beta\), or provide a dimensionally normalized model with explicit mass/Hubble scales, rotationally invariant operators, and a transfer calculation before quoting \(g_\phi\) limits.
