# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_1100pt
**Wall time**: 60.7s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=23558, completion=3601, total=27159

---

## PAPER-GPT-B1 — BLOCKER — Secs. 4, 14.4, 14.5, 15

**Issue:** The paper claims a “complete” no-go closing “every minimal-ECH dark-energy route,” but Sec. 4 explicitly admits the four-route closure is **not** an operator-level basis and omits parity-odd dimension-6 four-fermion partners and gravitational Chern-Simons terms. A channel-level survey cannot support a theorem-level exhaustiveness claim.

**Fix:** Either provide a complete diffeomorphism-invariant minimal-ECH operator basis with power counting and show every allowed operator is closed, or downgrade all “no-go theorem / complete closure / every route” language to “the enumerated channels fail.”

## PAPER-GPT-B2 — BLOCKER — Appendix B / Secs. 2.3, 12.1

**Issue:** The dimensional reconstruction of the vacuum density is internally wrong: Appendix B states  
\[
\rho_\Lambda^{\rm bounce}\sim(\alpha/M)M_{\rm Pl}^3=[(\alpha/M)M_{\rm Pl}]M_{\rm Pl}^4,
\]
but \((\alpha/M)M_{\rm Pl}^3\) has mass dimension \(+2\), not \(+4\), and is not equal to the RHS. This breaks the stated scaling ansatz used to justify \(\Xi M_{\rm Pl}^4\) and the \(N_{\rm tot}\approx92\) bookkeeping.

**Fix:** Redo the mass-dimension counting from the component operator to the energy density; if three missing powers are inserted, the scaling should involve \((\alpha/M)M_{\rm Pl}^5=[(\alpha/M)M_{\rm Pl}]M_{\rm Pl}^4\), not \(M_{\rm Pl}^3\). Then recompute \(N_{\rm tot}\) and all hierarchy claims.

## PAPER-GPT-M1 — MAJOR — Sec. 4.2, Route 2

**Issue:** The one-loop Holst suppression estimate is not dimensionally controlled: the text gives two “dimensionless” orderings differing by \(\sim 25\) orders of magnitude (\(10^{-58}\)–\(10^{-60}\) vs \(10^{-33}\)) and says both are acceptable. That is not an amplitude-level closure; it is an unresolved unit-contraction ambiguity.

**Fix:** Derive \(\beta\) from a normalized effective operator and a line-of-sight integral with explicit units, then quote one suppression factor with a reproducible convention. Remove the alternative-ordering paragraph unless it is made mathematically equivalent.

## PAPER-GPT-M2 — MAJOR — Sec. 4.1, Route 1

**Issue:** The NJL energy-density estimate  
\[
\rho_{\rm NJL}\sim \kappa n_\psi^2/m^2
\]
is dimensionally wrong: \(n_\psi^2\) has dimension \(+6\), \(\kappa\) has \(-2\), and dividing by \(m^2\) leaves dimension \(+2\), not energy density \(+4\). The standard torsion four-fermion contribution scales as \(\sim G n_\psi^2\), up to spin/polarization factors.

**Fix:** Remove the spurious \(1/m^2\), recompute the numerical bound at the relevant cosmological fermion densities, and state the closure using a dimensionally correct energy density.

## PAPER-GPT-M3 — MAJOR — Sec. 9, Barrier 12

**Issue:** Barrier 12 claims  
\[
\Omega_{\rm GW}^{\rm ECH}\lesssim(\rho_c/\rho_{\rm Pl})^2\sim10^{-2}
\]
is “far below the NANOGrav signal range.” This is arithmetically/physically false as written: PTA stochastic backgrounds are \(\Omega_{\rm GW}\sim10^{-9}\) at nHz, so \(10^{-2}\) is enormously above, not below, unless an unstated redshift/transfer suppression is applied.

**Fix:** Do not compare a bounce-era bound directly to today’s PTA \(\Omega_{\rm GW}(f)\). Propagate the spectrum with transfer functions and frequency mapping, then compare the present-day nHz amplitude.

## PAPER-GPT-M4 — MAJOR — Secs. 6, 7, 10.6, 13, 15

**Issue:** The SPHEREx \(f_{\rm NL}\) significance is over-presented: the text claims “systematics propagated through the multi-bin Fisher matrix,” but this paper gives only a footnote-level arithmetic mix of raw \(\sigma(f_{\rm NL})\), template overlap, GR projection, \(b_\phi\), and photo-\(z\) degradation without a combined covariance or final likelihood. The advertised \(3\)–\(5\sigma\) is therefore not reproducible from this manuscript.

**Fix:** Either include the Fisher matrix, nuisance marginalization, template-correlation treatment, and final propagated \(\sigma(f_{\rm NL})\) here, or demote the claim to “forecasted in Paper II” and avoid quoting a definitive significance in this paper.
