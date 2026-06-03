# P4 R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 61.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=99396, completion=677, total=106288

---

No blocker-grade findings. The paper is exceptionally thorough.

## PAPER-GEM-M1

**ID:** PAPER-GEM-M1
**CLASSIFICATION:** MAJOR
**SECTION:** Sec. 3.4 (TTA), Sec. 9.10 ($D_4$-TTA validation)
**ISSUE:** The $D_4$-TTA hold-out reveals a 21.4% per-galaxy argmax flip rate, indicating significant rotational non-equivariance in the classifier. The production catalog uses only $Z_2$ TTA, leaving a known model instability that could couple with survey systematics in uncharacterized ways, potentially affecting the hard-label diagnostics used throughout the paper.
**FIX:** The paper must either re-run key analyses on a full $D_4$-TTA catalog or provide a more rigorous argument for why this instability does not impact the soft-map-based null results. Justifying the choice by compute cost is insufficient for a primary systematic.

## PAPER-GEM-M2

**ID:** PAPER-GEM-M2
**CLASSIFICATION:** MAJOR
**SECTION:** Sec. 3.1, Sec. 4.3, Sec. 9.10 (Conclusions)
**ISSUE:** The paper reports two MASTER-deconvolved $\ell=1$ results that differ starkly: $-0.12\sigma$ (subsample mask) and $+3.64\sigma$ (canonical mask). The interpretation that this difference is due to the subsample mask's more contiguous geometry suppressing leakage is plausible but not directly demonstrated.
**FIX:** Add a direct test to support this interpretation. For example, apply a contiguous-patch selection to the canonical mask data to show that this selection alone drives the $+3.64\sigma$ residual toward the null.

## PAPER-GEM-m1

**ID:** PAPER-GEM-m1
**CLASSIFICATION:** minor
**SECTION:** Sec. 9.8 (Symmetry classification)
**ISSUE:** The description of the dipole as a parity-even observable is correct but the wording is confusing. The phrase "the dipole vector is parity-even and axial" is tautological and obscures the core point that the dipole *coefficients* of the pseudoscalar field are parity-even.
**FIX:** Rephrase to clarify that the dipole *pattern* in the pseudoscalar map is the parity-even observable that breaks isotropy, and that this pattern would be sourced by a background axial vector.

## PAPER-GEM-m2

**ID:** PAPER-GEM-m2
**CLASSIFICATION:** minor
**SECTION:** Abstract, Sec. 9.8 (Multi-null battery)
**ISSUE:** The paper describes the bootstrap pixel-resample test as "tautological for cosmological-dipole hypothesis testing." This is an overstatement; the test correctly captures spatial variance but simply lacks the statistical power to discriminate a signal of this size, which is a valid finding.
**FIX:** Reframe the description of the bootstrap test to state that it correctly measures the full sample variance but is shown by injection-recovery to lack the statistical power to detect a $\sim 1.7\%$ dipole.
