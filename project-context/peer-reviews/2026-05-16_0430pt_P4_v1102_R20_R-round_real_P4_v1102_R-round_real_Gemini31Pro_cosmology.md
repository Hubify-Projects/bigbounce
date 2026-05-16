# P4_v1102 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0430pt_P4_v1102_R20_R-round_real
**Wall time**: 73.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=84286, completion=7425, reasoning=6358, total=91711

---

**BOTTOM-LINE READINESS:** 
The propagation tail is genuinely exhausted. The substantive theoretical physics corrections from R19 (parity transformation rules, $w(\theta)$ parity-even classification, EFT of Inflation vs. LSS scope, and the distinction between isotropy-violation and parity-violation for a pseudoscalar field) have been executed with textbook-level precision. The paper's mathematical framework is now rigorous and conceptually airtight. The manuscript is **READY for external Houston review**. 

Below is the final adversarial truth-audit of the R20 state. I found zero BLOCKER or MAJOR issues.

## PAPER-GEM-P1: Theoretical Physics Audit (PASS)
**Section:** Abstract, Sec. IV.F, Sec. VI.H
**Issue:** Verification of R19 substantive physics fixes. 
**Audit Result:** Flawless. The paper correctly identifies that for a pseudoscalar field $A(\hat{n})$, the spherical harmonic coefficients transform as $a_{\ell m}^P = (-1)^{\ell+1} a_{\ell m}$. Consequently, the monopole ($\ell=0$) is parity-odd, while the dipole ($\ell=1$) is parity-even (an axial vector). The text brilliantly clarifies that a non-zero chirality dipole tests *isotropy violation* (a preferred axial direction), not *parity violation*, while the monopole tests parity violation. Furthermore, the proof that $w(\theta) = \langle A(\hat{n}_1)A(\hat{n}_2) \rangle$ is parity-even (since the two minus signs cancel) correctly reclassifies it as a $\Lambda$CDM TTT consistency test. The EFT of Inflation $g_*$ parameterization is also perfectly scoped.
**Fix:** None required. Excellent work.

## PAPER-GEM-m1: Monopole rounding mismatch in Abstract math (minor)
**Section:** Abstract
**Issue:** The text states "$2\langle p_{\rm CW}\rangle - 1 \approx -0.0053$ at $\langle p_{\rm CW}\rangle = 0.4974$". However, $2(0.4974) - 1 = -0.0052$. The $-0.0053$ value derives from the exact unrounded $0.49735$ value ($2 \times 0.49735 - 1 = -0.0053$). The abstract still mixes `0.4974` and `0.49735` in a few places as a propagation tail residual.
**Fix:** Change `0.4974` to `0.49735` in the math expression: "$2\langle p_{\rm CW}\rangle - 1 \approx -0.0053$ at $\langle p_{\rm CW}\rangle = 0.49735$". Also update the later instance: "residual spatially-uniform monopole $\CW/(\CW+\CCW) = 0.49735 \pm 0.000279$".

## PAPER-GEM-m2: 27-pixel drift in canonical mask definitions (minor)
**Section:** Sec. IV.C vs. Table IV
**Issue:** Sec. IV.C quotes the canonical mask as having "$N_{\rm pix, active} \approx 24{,}114$" ($f_{\rm sky} = 0.491$). Table IV quotes the canonical mask as having "$24{,}087$ NSIDE=64 pixels" ($f_{\rm sky} = 0.49005$). This 27-pixel discrepancy is a minor propagation tail residual, likely reflecting a slight difference in the $\geq 10$ spirals cut application between two different pipeline stages.
**Fix:** Unify the active pixel count to the exact `24,087` ($f_{\rm sky} = 0.49005$) in Sec. IV.C, or add a half-sentence parenthetical explaining the 27-pixel drop (e.g., edge-pixel exclusion in the specific NaMaster run).

## PAPER-GEM-n1: Table III footnote `d` reverse-engineering (nit)
**Section:** Table III, footnote d
**Issue:** The footnote explains that the null means $\langle C_\ell^{\rm null} \rangle$ are non-zero due to mask coupling and can be reverse-engineered via $\langle C_\ell^{\rm null}\rangle = C_\ell^{\rm meas} - \sigma_\ell^{\rm null} \cdot z$. While mathematically true, forcing the reader to reverse-engineer the null mean from the $z$-score is slightly hostile UX.
**Fix:** Since you already state "A dedicated null-mean column is queued for the next post-submission revision", this is acceptable for the current arXiv/review submission. No immediate action required.
