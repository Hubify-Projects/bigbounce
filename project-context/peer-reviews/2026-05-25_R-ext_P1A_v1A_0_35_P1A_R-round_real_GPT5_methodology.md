# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P1A_v1A_0_35
**Wall time**: 96.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29779, completion=5304, reasoning=4142, total=35083

---

## PAPER-GPT-B1 — BLOCKER

- **Section:** §2.1.1–§2.1.2 Eq. (1), Eq. (4); §4.1 Route 1  
- **Issue:** The ECH action and torsion-elimination algebra are internally inconsistent: Eq. (1) inserts a \(T^{abc}T_{abc}\) term into the “fundamental” action while later calling it a post-integration shorthand; Eq. (4) has a \(\gamma^2/(\gamma^2+1)\) four-fermion coefficient, while Route 1 drops it and claims classical \(\gamma\)-independence. This invalidates the R1 amplitude budget and any downstream claim using the same torsion operator.  
- **Fix:** Start from one explicit first-order Holst-Dirac action with specified minimal/non-minimal fermion coupling, solve the Cartan equation once, and use the resulting complete four-fermion operator coefficients consistently. Remove \(T^2\) from the fundamental action or label it only as the post-integration effective term.

## PAPER-GPT-B2 — BLOCKER

- **Section:** §2.3.1 Eq. (12); §12.1; Appendix B  
- **Issue:** The parity-odd operator is admitted to have Lagrangian dimension \(+1\), but the paper still uses the phenomenological repair \(\rho_\Lambda^{\rm bounce}\sim(\alpha/M)M_{\rm Pl}^5\) to compute \(\Xi\), \(N_{\rm tot}\approx92\), \(\Delta N\approx4\), and the dark-energy-vs-\(f_{\rm NL}\) “structural tension.” The dilution law also switches between torsion scaling and energy-density scaling without deriving whether the exponent should be \(e^{-3N}\), \(e^{-6N}\), etc.  
- **Fix:** Either construct a controlled dimension-four EFT/bounce-matching calculation with explicit mass dimensions and a derived dilution exponent, or delete the numerical \(N_{\rm tot}\), fine-tuning-reduction, and structural-tension claims.

## PAPER-GPT-B3 — BLOCKER

- **Section:** §4.2 Route 2  
- **Issue:** The one-loop Holst-to-birefringence closure is not a derivation. The paper compares an axial-current/Nieh-Yan term to a photon Chern-Simons rotation without deriving the photon effective coupling, then accepts two “dimensionless” orderings differing by \(\sim25\) orders of magnitude (\(10^{-60}\) vs. \(10^{-33}\)); that is not an amplitude-level no-go.  
- **Fix:** Derive the photon Chern-Simons coefficient after integrating out/marginalizing the relevant fermion/ALP sector with fixed \(\theta\) normalization and units. Recompute the ratio once; remove Route-2 closure until the mapping is unique.

## PAPER-GPT-M1 — MAJOR

- **Section:** §4 “Scope,” §4.6 Closure summary, §15 Conclusions  
- **Issue:** The paper explicitly says the four routes are not an operator-level basis and omits Jackiw-Pi \(R\wedge\widetilde R\) plus the parity-odd four-fermion partner, but later says R1–R4 “exhaust” the channels and “close every minimal-ECH dark-energy route.” That is an overclaim.  
- **Fix:** Replace “exhaust/every/no-go theorem” with “the four enumerated channels studied here,” or provide a complete diffeomorphism-invariant operator basis and close the omitted operators.

## PAPER-GPT-M2 — MAJOR

- **Section:** §6–§7, §10.6, §13, §15  
- **Issue:** The SPHEREx \(3\)–\(5\sigma\) and LiteBIRD confirm/rule-out language is not supported in this paper: no Fisher matrix, nuisance covariance, template-overlap treatment, correlated GR-projection/\(b_\phi\)/photo-\(z\) degradation, or transfer-function calculation is shown. The “definitively erased” \(f_{\rm NL}\) statement is asserted from scale counting, not propagated through a perturbation transfer calculation.  
- **Fix:** Include the full covariance/systematic propagation and scale-transfer calculation here, or demote all \(\sigma\)-level claims to qualitative cross-references to the companion papers.

## PAPER-GPT-M3 — MAJOR

- **Section:** §4.4 Route 4; §12.2; §13  
- **Issue:** R4 is internally contradictory: it shows \(\beta_{\rm obs}\) and \(\rho_\Lambda\) can both be matched for \(\alpha/M\sim10^{-21}\,{\rm GeV}^{-1}\) if \(m_\theta\sim H_0\), then says the same coupling “cannot deliver both.” Later §12.2 calls \(m\sim H_0\) “without fine-tuning,” while §4.4 calls it a \(10^{-61}\) tuning.  
- **Fix:** State plainly that R4 is not amplitude-excluded; it is only a naturalness objection conditional on a prior against \(m_\theta\sim H_0\). Remove “cannot deliver both” and “without fine-tuning,” or define the prior and quantify the naturalness/Bayesian penalty.
