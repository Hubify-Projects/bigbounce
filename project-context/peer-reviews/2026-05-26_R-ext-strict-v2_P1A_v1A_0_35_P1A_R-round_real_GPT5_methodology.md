# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P1A_v1A_0_35
**Wall time**: 91.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29811, completion=6087, reasoning=5159, total=35898

---

## PAPER-GPT-B1 — BLOCKER

**Location:** §IV, Route 2, Eq. `\Gamma_{\rm one-loop}^{parity-odd}` and following ratio.  
**Issue:** The written one-loop operator couples `∂μθ` to the fermion axial current, not to `F\tilde F`; no EFT matching to a photon Chern-Simons term is derived. The two quoted “dimensionless” suppressions (`10^{-58}`–`10^{-60}` vs `10^{-33}`) are mutually inconsistent, and the latter still carries an unremoved `H0` dimension.  
**Fix:** Derive the Holst/Nieh-Yan → photon-CS matching with explicit dimensions and line-of-sight integration, or remove the R2 birefringence-amplitude closure.

## PAPER-GPT-B2 — BLOCKER

**Location:** §IV “Scope,” §IV.E “Closure summary,” Conclusions.  
**Issue:** The paper admits the four routes are not an operator-complete basis and explicitly omits Jackiw-Pi `R∧\tilde R` and the parity-odd four-fermion partner, but later says R1–R4 “exhaust” the available channels and “close every minimal-ECH dark-energy route.” That is an overclaimed no-go theorem.  
**Fix:** Replace all “exhaust/every route” language with “four enumerated channels only,” or actually enumerate and close the omitted operators.

## PAPER-GPT-B3 — BLOCKER

**Location:** §IV Route 4; Appendix A parameter table.  
**Issue:** R4 is only “closed” after fixing `α/M≈10^{-21} GeV^{-1}` from a one-loop/prior matching, while the paper elsewhere treats `α/M` as phenomenological/log-flat and admits that floating it can fit both `βobs` and `ρΛ` for arbitrary `mθ`. This is a prior-dependent parameter-shift, not a marginalized no-go.  
**Fix:** Perform a joint likelihood/marginalization over `(α/M,mθ,ρθ)` with external ALP/photon constraints, or state R4 closure as conditional on a rigid one-loop prior.

## PAPER-GPT-M1 — MAJOR

**Location:** §II.C.1, Eq. `Dinf`; §XII; Appendix B.  
**Issue:** The `e^{-3Ntot}` dilution exponent is not derived for the quantity being identified with vacuum energy. Torsion/current amplitude scales like `n∝a^{-3}`, but the EC four-fermion energy density scales like `n^2/M_Pl^2∝a^{-6}`; meanwhile the reheating-reset paragraph says any bounce memory is overwritten. The headline `Ntot≈92` depends on this unsupported exponent.  
**Fix:** Derive the scaling of the actual scalar feeding `Λeff` through reheating, or demote `Ntot≈92` to a toy bookkeeping number and remove it from structural conclusions.

## PAPER-GPT-M2 — MAJOR

**Location:** §II.A Eq. `\mathcal L_int`; §IV Route 1.  
**Issue:** The Holst four-fermion coefficient is internally inconsistent: Eq. `\mathcal L_int` contains `γ^2/(γ^2+1)`, while Route 1 uses the pure EC coefficient and says the torsion-elimination map is independent of `γ`. The omitted parity-odd partner with `γ/(γ^2+1)` also contradicts the “parity-even only” simplification.  
**Fix:** Specify the fermion-coupling convention and carry the full Holst-dependent four-fermion operator basis through R1, or state that a Mercuri non-minimal choice removes the `γ` dependence.

## PAPER-GPT-M3 — MAJOR

**Location:** §VI–§VII, §XIII, Conclusions.  
**Issue:** The quoted SPHEREx `3–5σ` significance is imported without showing the Fisher matrix, nuisance marginalization, template-overlap covariance, GR-projection degradation, `bφ` prior propagation, or photo-`z` treatment in this paper. As written, the systematic budget is asserted, not propagated.  
**Fix:** Include the covariance/nuisance propagation or phrase the result only as “Paper II forecasts `3–5σ` under its stated assumptions.”
