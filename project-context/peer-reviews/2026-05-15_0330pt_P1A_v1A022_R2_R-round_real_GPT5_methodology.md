# P1A_v1A022_R2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0330pt
**Wall time**: 106.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=25815, completion=6557, reasoning=5593, total=32372

---

## PAPER-GPT-B1 — BLOCKER

**Location:** Appendix B, Eq. `\ref{eq:onshell_rho}`.  
**Issue:** The dimensional “fix” is still invalid: after declaring `[\mathcal L_{\rm odd}]=+1`, the text first supplies the missing `+3` via `K R`, then adds an extra `M_Pl^2` from “volume integration density,” which has no justified positive mass dimension and contradicts local energy-density counting. The stated density hierarchy is also wrong: `M_Pl^4 / ρ_Λ` is ~`10^120`, not “~35 orders.”  
**Fix:** Remove the volume-integration placeholder and either treat `ρ_Λ = Xi M_Pl^4` as a pure phenomenological ansatz or derive a local dimension-4 operator explicitly; then recompute the hierarchy and `N_tot`.

## PAPER-GPT-B2 — BLOCKER

**Location:** Sec. 4.2, Route 2 one-loop ratio; deferral paragraph.  
**Issue:** Route 2 remains dimensionally unresolved despite being used as an amplitude closure. The two “dimensionless” orderings are algebraically the same if units are handled consistently, yet the paper reports both `10^-58–10^-60` and `10^-33`; the latter is a units error, not a cross-check.  
**Fix:** Either delete the numerical Route-2 closure and keep it explicitly deferred, or derive the photon Chern-Simons/birefringence coupling with a single dimensionless line-of-sight integral in fixed units.

## PAPER-GPT-B3 — MAJOR

**Location:** Sec. 2.1.2 Eq. `\ref{eq:4fermi}` vs Sec. 4.1 Eq. `\ref{eq:NJL_torsion}`.  
**Issue:** The Holst four-fermion coefficient is internally inconsistent: Eq. `\ref{eq:4fermi}` contains `γ^2/(γ^2+1)`, while Route 1 drops the factor and claims the torsion-elimination map is γ-independent. This also ignores the admitted parity-odd four-fermion partner while claiming amplitude closure.  
**Fix:** Specify one fermion-coupling convention, solve the Cartan equation once, and carry the resulting parity-even and parity-odd four-fermion coefficients consistently through R1/R4.

## PAPER-GPT-B4 — MAJOR

**Location:** Abstract; Sec. 4 “Scope”; Sec. 4.5; Sec. 15.  
**Issue:** The paper simultaneously admits the four routes are not an operator-level basis and then claims they “exhaust” the minimal-ECH parity/dark-energy channels and “close every minimal-ECH dark-energy route.” Missing Jackiw-Pi gravitational Chern-Simons and parity-odd four-fermion operators invalidate the stronger no-go wording.  
**Fix:** Downgrade all theorem language to “enumerated-channel amplitude closure,” or add a complete diffeomorphism-invariant operator basis and close the omitted operators explicitly.

## PAPER-GPT-B5 — MAJOR

**Location:** Sec. 9, Barrier 12.  
**Issue:** The GW amplitude arithmetic is wrong: `(ρ_crit/ρ_Pl)^2` is ~`0.07–0.17`, not `10^-2`, and an `Ω_GW ~ 10^-2` bound is far above, not “far below,” NANOGrav-scale amplitudes. No transfer function or frequency mapping to nHz is given.  
**Fix:** Replace Barrier 12 with a present-day spectral-density calculation including redshift/transfer functions and the relevant frequency band, or remove this barrier.

## PAPER-GPT-B6 — MAJOR

**Location:** Table I caption/footnote; Sec. 7; Sec. 13; Sec. 15.  
**Issue:** The SPHEREx `f_NL` significance language is still overclaimed/inconsistent: `σ(f_NL)≈0.7` is described as post-systematic in Table I, but the footnote calls it Fisher-ideal and later degrades to `σ≈1.0` plus template overlap/systematics.  
**Fix:** State one forecast consistently: scalar-only `w=0` matter-bounce under Paper II Assumption (f), `σ≈0.7` ideal, degraded systematic forecast from Paper II only, and quote `3–5σ` strictly as a forecasted external result, not a result of this paper.
