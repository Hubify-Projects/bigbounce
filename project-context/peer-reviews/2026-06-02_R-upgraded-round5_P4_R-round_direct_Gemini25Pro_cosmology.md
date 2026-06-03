# P4 R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 51.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=99410, completion=861, total=105383

---

No blocker-grade findings.

## PAPER-GEM-M1

- **ID:** PAPER-GEM-M1
- **Class:** MAJOR
- **Section:** 9.6, Fig. 13 caption
- **Issue:** Hemisphere asymmetry significance is reported inconsistently. Section 9.6 claims a look-elsewhere correction (LEE) reduces the $3.05\sigma$ peak to $<1\sigma$, while a footnote and the Fig. 13 caption report a direct MC yields $p_{LEE} \le 10^{-4}$ (>3.7$\sigma$).
- **Fix:** Adopt a single, primary LEE result, justify the choice of null model against which it is calibrated, and report the outcome consistently throughout the text.

## PAPER-GEM-M2

- **ID:** PAPER-GEM-M2
- **Class:** MAJOR
- **Section:** 3.5, 9.4, 9.5
- **Issue:** Uncertainty from the 21.4% rotational argmax-flip rate is not clearly propagated. Section 3.5 derives a $\sim 1.21\times$ error widening factor for hard-label diagnostics, but it is not explicit whether this factor has been applied to significances in Table V, Table VII, and related analyses.
- **Fix:** State explicitly whether this correction has been applied to all hard-label-derived significances; if not, apply it and update the results.

## PAPER-GEM-m3

- **ID:** PAPER-GEM-m3
- **Class:** minor
- **Section:** 3.1, 11
- **Issue:** The critical distinction between the "subsample mask" ($f_{sky}=0.659$, giving the $-0.12\sigma$ null) and the "canonical mask" ($f_{sky}=0.490$, giving the $+3.64\sigma$ residual) risks appearing as post-hoc selection.
- **Fix:** Elevate the justification for preferring the subsample mask for the headline cosmological result from footnotes and late-section remarks into the main methods section (Sec 3.1).

## PAPER-GEM-m4

- **ID:** PAPER-GEM-m4
- **Class:** minor
- **Section:** 9.7.1, Abstract, Conclusions
- **Issue:** The paper correctly identifies the $\ell=1$ dipole as a parity-EVEN test of isotropy in Sec 9.7.1, but elsewhere uses less precise "parity symmetry" language.
- **Fix:** Consistently use "statistical isotropy" when discussing the dipole to maintain theoretical precision and avoid conflating it with genuinely parity-odd observables like the monopole.

## PAPER-GEM-n5

- **ID:** PAPER-GEM-n5
- **Class:** nit
- **Section:** 4.2 (footnote b)
- **Issue:** The formal joint-fit analysis that excludes a 1.7% dipole at >18$\sigma$ (bootstrap-corrected) is the most powerful piece of evidence dismissing the canonical-mask residual, but it is embedded deep within a footnote.
- **Fix:** Elevate this analysis to a more prominent position within the main body of the text (e.g., in the multi-null battery discussion) to provide a stronger, more direct closure.

## PAPER-GEM-n6

- **ID:** PAPER-GEM-n6
- **Class:** nit
- **Section:** 9.7.1, 4.5
- **Issue:** The paper correctly identifies the two-point chirality correlation $w_{\rm CW}(\theta)$ as parity-EVEN, but this is not mentioned in the abstract or introduction's framing of the paper's scope.
- **Fix:** Briefly note in the abstract or introduction that all 2-point statistics of the pseudoscalar chirality field (including the dipole and $w_{\rm CW}$) are parity-even to better frame the scope of the entire analysis.
