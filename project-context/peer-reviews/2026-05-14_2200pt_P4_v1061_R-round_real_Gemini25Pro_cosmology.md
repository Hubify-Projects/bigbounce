# P4_v1061 R-round — REAL cross-vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `google/gemini-2.5-pro` (via OpenRouter)
**Round**: 2026-05-14_2200pt
**Wall time**: 60.6s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=58251, completion=6044, total=64295

---

No BLOCKER or MAJOR issues were found that would prevent publication. The paper is exceptionally rigorous in its systematic checks and transparent in its claims. The v1.0.61 update to clarify the Fisher-floor arithmetic has landed cleanly. The analysis is sound, and the conclusions are well-supported. The paper is in a publish-ready state.

The following are minor points for improving clarity and correctness.

***

## PAPER-GEM-m1

**Classification:** minor
**Location:** Section VII.B (The 3.05σ Hemisphere Signal), Section IV.C (Hemisphere Asymmetry)
**Issue:** The text presents two look-elsewhere-effect (LEE) methods (analytic Bonferroni/BH vs. direct MC) that give conflicting verdicts on the random-label null hypothesis. While the interpretation is correct, the presentation could more decisively frame the direct MC test as the primary, more powerful test of that specific null, whose rejection is a key characterization of the structured systematic floor.
**Fix:** Revise the paragraph to state that the direct MC permutation test is the definitive test of the random-label null, which it rejects, and this rejection serves as a measurement of a structured systematic that random shuffling cannot reproduce. The analytic corrections are conservative approximations superseded by this direct test.

## PAPER-GEM-m2

**Classification:** minor
**Location:** Section VII.D (Mapping the bound onto cosmological parity-violation observables)
**Issue:** The discussion correctly notes that the morphology dipole and CMB birefringence are complementary probes of parity violation. The text could be strengthened by explicitly stating the different physical couplings they primarily constrain.
**Fix:** Add a sentence clarifying that CMB birefringence constrains an axion-photon coupling, whereas a morphology dipole would primarily trace couplings to gravity (e.g., chiral tensors) or the matter sector.

## PAPER-GEM-m3

**Classification:** minor
**Location:** Section VIII (Conclusions), item 5
**Issue:** The falsification criterion sets a future detection threshold of `A >= 0.1%`. This is well-motivated relative to the projected LSST sensitivity floor (`~0.08%` on A), but the paper's own empirical sensitivity is `>0.5%`. The text could briefly clarify that this `0.1%` threshold is chosen to be just above the *projected future sensitivity* of LSST, not the sensitivity of the present work.
**Fix:** Add a parenthetical clarification to the falsification criterion, e.g., "(a threshold chosen to be just above the projected LSST sensitivity floor of $\sim\!0.08\%$, see Sec.~\ref{sec:future})".

## PAPER-GEM-n1

**Classification:** nit
**Location:** Bibliography, [Ref. 2] Shamir:2022
**Issue:** The bibliography contains a note stating that `arXiv:2207.11885` points to an unrelated paper. A check of the arXiv database confirms this ID does in fact correspond to the correct Shamir (2022) paper, "Analysis of the alignment of non-random patterns of spin directions...". The note is incorrect.
**Fix:** Remove the incorrect verification note from the bibitem entry for Shamir (2022).
