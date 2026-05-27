# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P1A_v1A_0_35
**Wall time**: 99.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29801, completion=6186, reasoning=5174, total=35987

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR

**Section:** Abstract; §IV “Scope”; §IV.E; §XV Conclusions  
**Issue:** The paper explicitly defers Jackiw–Pi \(R\wedge\widetilde R\) and the parity-odd four-fermion partner, then later says R1–R4 “exhaust” the channels and “close every minimal-ECH dark-energy route.” That is an operator-basis overclaim; the proven result is only enumerated-channel closure.  
**Fix:** Replace “exhaust/every/no-go theorem” with “enumerated channel-level routes,” or add an operator table and close the omitted operators quantitatively.

## PAPER-GPT-M2 — MAJOR

**Section:** §II.C.1 Eq. \(\eqref{eq:Dinf}\); §XII.A; Appendix B  
**Issue:** The \(e^{-3N_{\rm tot}}\) dilution derivation is not internally consistent: torsion scales as \(T\propto J^5\sim n\propto a^{-3}\), but the EC contact energy scales as \((J^5)^2\propto a^{-6}\). The text also describes the antisymmetrized gamma product as a “cube of the fermion bilinear,” which is false.  
**Fix:** Specify the actual operator expectation value sourcing \(\rho_\Lambda\), derive its scale-factor dependence, and recompute \(N_{\rm tot}\); remove the \(N_{\rm tot}\approx92\) precision and “\(10^5\)” bookkeeping until then.

## PAPER-GPT-M3 — MAJOR

**Section:** §IV.B Route 2  
**Issue:** The one-loop Holst-to-birefringence ratio is not a derived observable: it compares a \(\partial_\mu\theta J^{5\mu}\) term to a photon Chern–Simons rotation without deriving the effective \(\theta F\widetilde F\) coupling. The manuscript admits two “dimensionless orderings” giving \(10^{-60}\) vs \(10^{-33}\), a 27-order ambiguity.  
**Fix:** Derive the photon coupling, normalization, and line-of-sight rotation integral explicitly, or drop the claimed \(58\)–\(60\) OOM suppression.

## PAPER-GPT-M4 — MAJOR

**Section:** §IV.C Route 3  
**Issue:** The claimed suppression \((\Delta\gamma/\gamma)(H/M_{\rm Pl})\sim10^{-63}\) “relative to the dark-energy density” mixes an amplitude ratio with an energy-density comparison. No induced dimension-4 operator or \(\delta\rho/\rho_\Lambda\) calculation is shown, and \(\Delta\gamma/\gamma\sim10^{-2}\) is not obtained from the displayed beta function.  
**Fix:** Write the induced operator, compute the energy-density correction with correct powers of \(H\) and \(M_{\rm Pl}\), and show the RG integral with thresholds; otherwise remove the quantitative Route 3 closure.

## PAPER-GPT-M5 — MAJOR

**Section:** §IV.D Route 4; §XII “Spectator-ALP birefringence”  
**Issue:** R4 is labeled “closed by birefringence-amplitude bound,” but the text itself shows \(\beta\) and \(\rho_\Lambda\) match for \(m_\theta\sim H_0\), and that floating \(\alpha/M\) fits arbitrary \(m_\theta\). This is a naturalness/prior objection, not an amplitude no-go; §XII then says \(m\sim H_0\) is “without fine-tuning,” contradicting R4.  
**Fix:** Recast R4 as conditional on fixed one-loop \(\alpha/M\) plus an explicit prior against \(m_\theta\sim H_0\), or remove it from the no-go list; make the fine-tuning language consistent.

## PAPER-GPT-M6 — MAJOR

**Section:** Abstract; §VII; §XIII matter-bounce \(\fnl\) forecast  
**Issue:** The \(3\)–\(5\sigma\) SPHEREx claim is quoted after ad hoc degradation factors, but this paper shows no Fisher covariance, nuisance marginalization, or systematic-error propagation. Raw \(4.375/0.7=6.25\sigma\) degraded by template overlap, GR projection, \(b_\phi\), and photo-\(z\) can move materially across the quoted range.  
**Fix:** Present it strictly as an external Paper II forecast, quote the fully marginalized \(\sigma(\fnl)\) from that analysis, and remove standalone high-significance phrasing here.
