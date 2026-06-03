# P4 R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round8
**Wall time**: 64.5s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=99458, completion=879, total=106516

---

## PAPER-GEM-M1
**Classification:** MAJOR
**Section:** Abstract, Sec. 5.I.1
**Issue:** The paper correctly identifies the $\ell=1$ dipole as a parity-even, isotropy-breaking observable, but the abstract's framing ("NOT a direct parity-violation test") is imprecise. The measured 9.5$\sigma$ global monopole ($\ell=0$) *is* a direct parity-odd observable, which the paper attributes to systematics. This distinction is crucial for theoretical clarity.
**Fix:** Rephrase the abstract to state the $\ell=1$ dipole tests isotropy (is parity-even), while the measured $\ell=0$ monopole is a parity-odd observable attributed to systematics. This clarifies the scope without changing the scientific conclusion.

## PAPER-GEM-M2
**Classification:** MAJOR
**Section:** Sec. 5.I.2 (Parity Translation)
**Issue:** The discussion of the transfer function from primordial chiral tensors to late-time morphology correctly notes its model dependence but understates the severe signal degradation expected from non-linear evolution and baryonic feedback. The current text may imply the main obstacle is merely a calculation, not fundamental physics that washes out the signal.
**Fix:** Add a sentence explicitly stating that non-linear structure formation and baryonic physics are expected to significantly decorrelate late-time spins from the initial tidal field, strengthening the physical motivation for the null result.

## PAPER-GEM-M3
**Classification:** MAJOR
**Section:** Sec. 3.D, Sec. 4.E (Table V), Sec. 5.D (Table VII)
**Issue:** The paper quantifies a 21.4% per-galaxy argmax-flip rate from rotational non-equivariance and states this uncertainty is propagated via a $\sim 1.21\times$ variance widening for hard-label diagnostics. However, the hard-label analyses in Table V and Table VII do not mention this correction, making it unclear if the reported significances account for this additional uncertainty.
**Fix:** Explicitly state in the captions of Table V and Table VII whether the reported sigmas include the rotational-flip uncertainty. If not, update the tables and associated text with the corrected, presumably lower, significances.

## PAPER-GEM-m4
**Classification:** minor
**Section:** Abstract, Sec. 4.C, Sec. 4.D
**Issue:** The argument disfavoring a primordial origin for the $+3.64\sigma$ canonical-mask residual is powerful but spread across multiple sections, footnotes, and a multi-stage analysis (multi-null battery, cross-spectrum, joint fit, bootstrap correction). This complex narrative is difficult to synthesize.
**Fix:** Consolidate the final, most powerful argument (the joint nuisance-marginalized fit with block-bootstrap correction) into a dedicated summary sub-paragraph in the Discussion (Sec. V) to provide a clear, final verdict.

## PAPER-GEM-m5
**Classification:** minor
**Section:** Sec. 5.C (Sensitivity Floor), Falsification Criterion
**Issue:** The paper presents multiple sensitivity figures (Fisher floor, HC-subsample empirical, full-catalog empirical). The abstract and falsification criterion conservatively use the $\geq 0.75\%$ HC-subsample threshold, which may understate the full catalog's demonstrated power (<0.50% recovery threshold).
**Fix:** State the full-catalog injection-recovery sensitivity as the primary empirical sensitivity of the analysis in the abstract. Retain the HC-subsample result as a conservative robustness check, but clarify the full sample is more sensitive.

## PAPER-GEM-n6
**Classification:** nit
**Section:** Abstract
**Issue:** The abstract states that injected real dipoles show "$\sigma = +2.87$ at $\ell=1$". The main text (Sec 4.D) clarifies this is the *median* sigma over many injection realizations, a more precise statistical description.
**Fix:** Add "median" before "$\sigma = +2.87$" in the abstract.
