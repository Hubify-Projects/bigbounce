# paper1a R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P1A_v1A_0_33
**Wall time**: 47.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=28572, completion=6390, reasoning=5822, total=34962

---

## PAPER-GEM-B1
**Class:** BLOCKER
**Section:** VI (Systematic Analysis)
**Issue:** The review instructions explicitly request scrutiny of "the NaMaster methods paragraph added at §VI L427", but Section VI contains absolutely no mention of NaMaster, pseudo-$C_\ell$ estimators, or related methodology. The promised text was either omitted during drafting or lost in a merge conflict.
**Fix:** Insert the missing NaMaster methodology paragraph into Section VI as intended.

## PAPER-GEM-M1
**Class:** MAJOR
**Section:** II.C.1 (Inflationary Suppression), paragraph 2
**Issue:** The text justifies a $\sqrt{T_{\rm reh}/M_{\rm GUT}}$ factor by claiming "the parity-odd combination carries an extra phase-space suppression at thermal equilibrium, the same factor that drives the Mercuri & Capozziello one-loop coefficient $\alpha_{\rm em}/(4\pi)$". This is a severe theoretical conflation; the Mercuri-Capozziello factor is a quantum loop suppression derived from a chiral anomaly triangle diagram, which is physically unrelated to thermal phase-space suppression.
**Fix:** Remove the false equivalence to the Mercuri-Capozziello loop factor. Justify the $\sqrt{T_{\rm reh}/M_{\rm GUT}}$ scaling purely on dimensional/phase-space grounds for the axial current variance, or explicitly label it as a purely phenomenological ansatz.

## PAPER-GEM-m1
**Class:** minor
**Section:** XII.A (The Inflationary Suppression Factor)
**Issue:** The discussion treats the dilution factor $\Dinf \propto e^{-3 N_{\rm tot}}$ as a valid analytical parameterization, but Sec 2.3.1 already established the "Reheating thermal-reset barrier" which proves non-propagating torsion has no memory and cannot be diluted. Sec 12.1 fails to remind the reader that this mathematical bookkeeping is physically invalidated by the thermal reset.
**Fix:** Add a sentence in 12.1 explicitly noting that while $N_{\rm tot}$ controls the mathematical ansatz, the physical mechanism is already closed by the thermal-reset barrier (B14/R2).

## PAPER-GEM-n1
**Class:** nit
**Section:** IV.D (Route 4)
**Issue:** The text references "the Chern-Simons 4-current" $K^\mu$ without defining its explicit gauge-field structure, which is necessary to immediately verify the parity-odd contraction.
**Fix:** Briefly define $K^\mu = \epsilon^{\mu\nu\rho\sigma} A_\nu F_{\rho\sigma}$ inline.
