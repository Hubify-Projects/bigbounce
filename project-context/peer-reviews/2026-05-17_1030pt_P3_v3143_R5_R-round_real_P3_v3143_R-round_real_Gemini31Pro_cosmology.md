# P3_v3143 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_1030pt_P3_v3143_R5_R-round_real
**Wall time**: 55.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=60139, completion=5143, reasoning=3983, total=65282

---

## PAPER-GEM-B1: BLOCKER — Unpropagated Arithmetic Contradiction in Sec 4.3
**Location:** Section 4.3, first paragraph.
**Issue:** The text asserts: "All 637 are pairwise; no triple coincidences appear at 5''. The catalog therefore contains 378,280 unique physical objects". This is a direct mathematical contradiction ($388,493 - 637 = 387,856 \neq 378,280$). While Deferral 6.4(a) acknowledges the 9,576-object shortfall, stating the false arithmetic as a derived fact ("therefore") in the main text is a propagation failure that breaks the logical flow of the section.
**Fix:** Change the sentence to: "All 637 are pairwise; collapsing these would yield 387,856 unique objects, though the published headline remains frozen at 378,280 pending a full intra-survey duplicate recompute (see Deferral 6.4a)."

## PAPER-GEM-M1: MAJOR — Table 1 Footnote Missed "Strict Subset" Softening
**Location:** Table 1, footnote $\S$.
**Issue:** Closure (1) successfully softened "strict subset" to "high overlap" in Section 3.4, but the propagation missed Table 1. Footnote $\S$ still explicitly claims: "The published catalog headline of 298 sources... is a strict subset of this reference set."
**Fix:** In Table 1 footnote $\S$, replace "is a strict subset of this reference set" with "has high overlap with this reference set (exact intersection queued for v3.1.44)".

## PAPER-GEM-M2: MAJOR — GR Projections are Theoretical Errors, Not Observational Systematics
**Location:** Section 5, paragraph 3.
**Issue:** The text frames the Fisher forecast as a "zero-systematics upper bound" and lists missing components (fiber-assignment, photo-$z$, foregrounds). However, for $f_{\rm NL} \sim \mathcal{O}(1)$, GR projection effects (Doppler, Sachs-Wolfe) are not observational systematics; they are fundamental gauge-invariant corrections to the theoretical observable template at $\mathcal{O}(\mathcal{H}^2/k^2)$. Omitting them means the Fisher matrix is evaluating a physically invalid, gauge-dependent theoretical model at the scales where the signal peaks.
**Fix:** Add a sentence to Section 5 explicitly stating: "Furthermore, the theoretical template currently omits $\mathcal{O}(\mathcal{H}^2/k^2)$ GR projection corrections, which are required for gauge-invariant observable predictions at $f_{\rm NL} \sim \mathcal{O}(1)$ and perfectly mimic scale-dependent bias (see Deferral 6.4e)."

## PAPER-GEM-M3: MAJOR — Invalid 1D Likelihood Ratio on 2D Correlated Posterior
**Location:** Section 5.1 and Appendix D' (Parameter-shift likelihood ratio).
**Issue:** The text calculates $\Delta\chi^2$ for $\gamma$ relative to the 1D marginal posterior mean, then constructs a "parameter-shift likelihood ratio" $\mathcal{L}_{\rm bounce}/\mathcal{L}_{\rm SMBHB} \approx 2.2 \times 10^4$. This is mathematically invalid because it ignores the covariance between $\gamma$ and $\log_{10}A$; the ratio of 1D marginal slices does not equal the ratio of the 2D likelihood surface maxima.
**Fix:** Remove the pseudo-likelihood ratio $\exp(10.0) \approx 2.2 \times 10^4$. Report only the 1D marginal deviations ($+1.13\sigma$ and $+4.61\sigma$) and explicitly state that a joint 2D evaluation is required to quantify the relative likelihood.

## PAPER-GEM-m1: minor — Missing Bispectrum Shape Specification
**Location:** Appendix D', "Bounce-physics connection" paragraph.
**Issue:** The text states that $f_{\rm NL} = -35/8$ is an observable consequence of the $w=0$ matter-bounce class. It fails to specify that this is strictly the *local* shape amplitude ($f_{\rm NL}^{\rm local}$); bouncing models also generate distinct equilateral or folded bispectrum shapes depending on the sound speed $c_s$ during contraction.
**Fix:** Change "$f_{\rm NL} = -35/8$ prediction" to "local-shape $f_{\rm NL}^{\rm local} = -35/8$ prediction" to properly bound the EFT/model-class scope.

## PAPER-GEM-n1: nit — Abstract Repetition
**Location:** Abstract.
**Issue:** The exact stratification breakdown ("The catalog stratifies into the 378,080 point-source object detections... plus the 200 Planck CMB map patches... summing to the 378,280 headline") is repeated almost verbatim in consecutive sentences in the first paragraph.
**Fix:** Delete the redundant second sentence ("The catalog stratifies into the 378,080 point-source object detections... summing to the 378,280 headline.").
