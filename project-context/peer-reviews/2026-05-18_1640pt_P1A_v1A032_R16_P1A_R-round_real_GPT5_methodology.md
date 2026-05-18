# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1640pt_P1A_v1A032_R16
**Wall time**: 107.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28467, completion=6467, reasoning=5588, total=34934

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR

- **Section:** Abstract; §4 “Scope”; §4.5; §15 Conclusions  
- **Issue:** The paper alternates between “channel-level four-route no-go” and “exhaust/close every minimal-ECH dark-energy route,” while explicitly omitting Jackiw–Pi gravitational Chern–Simons and the parity-odd four-fermion partner. This overstates the theorem.  
- **Fix:** Restrict all theorem/conclusion language to “four enumerated channels,” or add a complete operator-basis enumeration and close the omitted operators quantitatively.

## PAPER-GPT-M2 — MAJOR

- **Section:** §4.2 Route 2, equation after `\Gamma_{\rm one-loop}`  
- **Issue:** The one-loop birefringence suppression is not rigorously derived: the text gives incompatible dimensionless estimates, `10^{-58}–10^{-60}` and `10^{-33}`, differing by ~27 orders of magnitude. That is not an acceptable amplitude-budget closure.  
- **Fix:** Derive β from the normalized effective action through the photon propagation equation, define θ dimensions, keep one dimensionless ratio, and recompute the suppression.

## PAPER-GPT-M3 — MAJOR

- **Section:** §2.3.1 Inflationary Suppression; §12.1; Appendix B  
- **Issue:** `D_inf = e^{-3N_tot}(T_reh/M_GUT)^{3/2}` and `N_tot≈92` are used as quantitative inputs, but the exponent and reheating prefactor are admitted dimensional/aesthetic assumptions with no propagated uncertainty. The structural-tension claim inherits this unquantified systematic.  
- **Fix:** Derive the scaling from an explicit torsion/axial-current operator expectation through reheating, or quote `N_tot` as a broad nuisance-dependent interval and remove precise/“definitive” wording tied to 92.

## PAPER-GPT-M4 — MAJOR

- **Section:** §4.4 Route 4; §12 “Spectator-ALP birefringence”; §13; §15  
- **Issue:** Route 4 is not closed by amplitude: the paper itself shows `m_θ≈H0` with `α/M≈10^{-21} GeV^{-1}` matches both β and `ρ_Λ`. The closure is therefore a naturalness prior, yet later text says `m∼H0` is “without fine-tuning” and calls β a prediction despite being fitted.  
- **Fix:** State explicitly that R4 is rejected only by an imposed naturalness criterion, not by amplitude mismatch; remove “without fine-tuning” and recast β as an external ALP consistency check.

## PAPER-GPT-M5 — MAJOR

- **Section:** §6 Systematics; §7 footnote 1; §10/§13/§15 SPHEREx claims  
- **Issue:** The `3–5σ` SPHEREx forecast is quoted after mentioning GR projection, template overlap, `b_φ`, and photo-z degradation, but this paper does not propagate them through a covariance/nuisance-marginalized Fisher matrix. The significance is imported and over-presented as an internal result.  
- **Fix:** Either reproduce the final Fisher covariance/table with all degradations applied, or state only “forecasted in Paper II” and avoid using the sigma range as a result of this paper.

## PAPER-GPT-M6 — minor

- **Section:** §9 Barrier 12  
- **Issue:** The bound `Ω_GW^ECH|bounce ≲ (ρ_crit/ρ_Pl)^2 ≃ 0.07–0.17` is asserted without derivation and is not clearly an energy-fraction bound relative to the bounce density. It also does not connect to any present-day spectral observable, so it does not by itself “close” the GW-amplification channel.  
- **Fix:** Derive the bound from the tensor power/energy density definition and propagate through a transfer function, or downgrade Barrier 12 to a qualitative ceiling rather than a closure constraint.
