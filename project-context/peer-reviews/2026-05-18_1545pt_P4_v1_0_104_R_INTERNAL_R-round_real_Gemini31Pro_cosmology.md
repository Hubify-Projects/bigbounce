# P4_v1_0_104_R_INTERNAL R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1545pt
**Wall time**: 116.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=86445, completion=15996, reasoning=15360, total=102441

---

## PAPER-GEM-B1: Propagation Tail Contradiction ("identical data" vs "full chain")
**Class:** MAJOR
**Location:** Abstract (end of paragraph 3)
**Issue:** The closure wave successfully replaced "on the same data" with the "full chain (map choice + monopole-subtraction + mask choice + MASTER)" clarification in multiple sites to explicitly state that the pre- and post-MASTER estimators use different inputs. However, the abstract still contains the sentence: "since the independent wider-coverage $\ell=1$ estimators on the **identical data** are null." This directly contradicts the newly added closure text in the same abstract which states they are "not pure MASTER on identical inputs."
**Fix:** Change "on the identical data" to "on the wider-coverage subsample mask" or remove the phrase entirely to maintain consistency with the closure.

## PAPER-GEM-B2: Bonferroni Math Error for $\alpha=0.001$
**Class:** minor
**Location:** Section IV.E (Signal-Hunt Diagnostics), paragraph 5
**Issue:** The text states: "across the 15-cell grid... the family-wise Bonferroni penalty at $\alpha=0.05$ is $z_{\rm Bonf}^{15} \approx 2.94\sigma$ and at the tighter $\alpha=0.001$ is $z_{\rm Bonf}^{15,\alpha=0.001} \approx 4.04\sigma$." A two-tailed Bonferroni correction for $m=15$ at $\alpha=0.001$ yields a per-test threshold of $p = 0.001/15 = 6.66 \times 10^{-5}$, which corresponds to a two-tailed z-score of $3.99\sigma$, not $4.04\sigma$. (A z-score of $4.04$ corresponds to $m \approx 19$ for two-tailed or $m \approx 38$ for one-tailed).
**Fix:** Correct the text to "$z_{\rm Bonf}^{15,\alpha=0.001} \approx 3.99\sigma$". The conceptual conclusion remains valid since the $+4.06\sigma$ cell still survives this corrected threshold.

## PAPER-GEM-B3: Theoretical Physics Framing (Praise/Verification)
**Class:** nit
**Location:** Section IX.H and Section IV.F
**Issue:** Not an error, but a verification of the theoretical physics framing requested in the prompt. The text correctly identifies that the dipole moment of a pseudoscalar field is an axial vector, and therefore the $\ell=1$ dipole is parity-EVEN and tests isotropy, not parity violation. It also correctly identifies that the 2-point correlation $w_{CW}(\theta)$ is parity-EVEN because the two minus signs cancel
