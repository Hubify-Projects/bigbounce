# P1A_v1A023 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P1A_v1A023_R3_R-round_real
**Wall time**: 127.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=27231, completion=8494, reasoning=6732, total=35725

---

Blocker-grade findings present.

## PAPER-GPT-B1 — BLOCKER — Sec. 4.2 Route 2

| Field | Audit |
|---|---|
| Section / line | Sec. 4.2, Route 2; “Real cross-vendor adversarial-review deferrals” |
| Paper says verbatim | “Item (c)… remains **on-record deferred** pending a dedicated photon-Chern-Simons coupling derivation” and later “the **dimensionless ratio** \(\Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs}\sim \frac{\alpha_{\rm em}}{4\pi}\frac{H_0}{M_{\rm Pl}(\alpha/M)\beta_{\rm obs}}\)” |
| Known fact | \([H_0]=M\), \([M_{\rm Pl}(\alpha/M)]=1\), \([\beta]=1\); the displayed “dimensionless ratio” has mass dimension \(+1\). The same paragraph gives mutually inconsistent estimates \(10^{-58}\)–\(10^{-60}\) and \(10^{-33}\). |
| Verdict | STILL-UNRESOLVED / REGRESSION |
| Concrete issue | Route 2 is still dimensionally wrong and the text simultaneously says the derivation is deferred and “corrected.” |
| Fix | Delete the quantitative R2 suppression claim until a photon-Chern-Simons coupling and line-of-sight rotation integral are derived with consistent units; keep only a qualitative deferred statement. |

## PAPER-GPT-B2 — BLOCKER — Sec. 4.1 Route 1

| Field | Audit |
|---|---|
| Section / line | Sec. 4.1, Eq. \(\ref{eq:NJL_torsion}\) paragraph |
| Paper says verbatim | “\(\rho_{\rm NJL} \sim \kappa\,n_\psi^2/m^2 \sim n_\psi^2/(m^2 M_{\rm Pl}^2)\)” |
| Known fact | \(n_\psi\) has mass dimension \(3\), \(\kappa\) has dimension \(-2\); \(\kappa n_\psi^2\) has dimension \(4\), but \(\kappa n_\psi^2/m^2\) has dimension \(2\), not energy-density dimension \(4\). |
| Verdict | NOVEL |
| Concrete issue | The Route 1 amplitude bound uses a dimensionally invalid energy-density estimate. The same section also conflicts with Eq. \(\ref{eq:4fermi}\), which contains a \(\gamma^2/(\gamma^2+1)\) Holst factor, while Route 1 says the torsion-elimination map is \(\gamma\)-independent. |
| Fix | Remove the spurious \(1/m^2\), define the axial-current normalization, recompute \(\rho_{\rm NJL}\sim \kappa J_5^2\), and state explicitly whether the paper assumes minimal Holst fermions or the Mercuri/Nieh-Yan non-minimal cancellation. |

## PAPER-GPT-B3 — BLOCKER — Appendix B / Secs. 12, 14.2

| Field | Audit |
|---|---|
| Section / line | Appendix B Eq. \(\ref{eq:onshell_rho}\); Sec. 12; Sec. 14.2 |
| Paper says verbatim | “\(\rho_\Lambda^{\rm bounce}\sim(\alpha/M)M_{\rm Pl}^5\)” is “a phenomenological on-shell scaling ansatz” and “**no quantitative claim in the main text relies on this dimensional ansatz**.” |
| Known fact | Main text repeatedly uses \(\Xi=[(\alpha/M)M_{\rm Pl}]\mathcal D_{\rm inf}\), \(N_{\rm tot}\approx92\), and the DE-vs-\(f_{\rm NL}\) structural tension; these follow from the Appendix B scaling assignment. |
| Verdict | STILL-UNRESOLVED |
| Concrete issue | The Appendix B “fix” is not a derivation, and the claim that no main-text quantitative result relies on it is false. |
| Fix | Mark \(N_{\rm tot}\approx92\), \(\Xi\), and the structural-tension arithmetic as conditional on the phenomenological ansatz, or supply a genuine local dimension-\(+4\) EFT operator derivation. |

## PAPER-GPT-B4 — MAJOR — Abstract / Sec. 4 Scope / Sec. 4.6 / Conclusions

| Field | Audit |
|---|---|
| Section / line | Abstract; Sec. 4 “Scope”; Sec. 4.6; Sec. 15 |
| Paper says verbatim | Abstract: “not an operator-level theorem”; Sec. 4 Scope: “Jackiw-Pi gravitational Chern-Simons… and the parity-odd four-fermion partner… are not separately enumerated”; Sec. 4.6: “Routes R1--R4 between them **exhaust** the parity-odd / dark-energy channels”; Conclusions: “close **every** minimal-ECH dark-energy route.” |
| Known fact | A channel list cannot be exhaustive after explicitly omitting diffeomorphism-invariant parity-odd operators. |
| Verdict | REGRESSION |
| Concrete issue | The no-go scope is internally contradictory: “enumerated channels only” becomes “exhausts every route.” |
| Fix | Replace all “exhaust,” “every route,” and theorem-level closure language with “the four enumerated routes,” or add the missing operator-basis proof. |

## PAPER-GPT-B5 — MAJOR — Sec. 9 Barrier 12

| Field | Audit |
|---|---|
| Section / line | Sec. 9.12, Barrier 12 |
| Paper says verbatim | “\(\Omega_{\rm GW}^{\rm ECH}\lesssim(\rho_{\rm crit}/\rho_{\rm Pl})^2\sim10^{-2}\), far below the NANOGrav signal range” |
| Known fact | \((0.27)^2\simeq7\times10^{-2}\), \((0.41)^2\simeq1.7\times10^{-1}\), not \(10^{-2}\). NANOGrav-band \(\Omega_{\rm GW}\) is order \(10^{-9}\)–\(10^{-8}\), so \(10^{-2}\) is many orders above, not below. |
| Verdict | NOVEL |
| Concrete issue | Barrier 12 has the wrong arithmetic and wrong inequality direction relative to PTA amplitudes. |
| Fix | Derive a frequency-dependent transfer function to the nHz band, or delete Barrier 12 as stated. |

## PAPER-GPT-B6 — MAJOR — Secs. 1, 7, 13; bibliography provenance

| Field | Audit |
|---|---|
| Section / line | Table I note; Sec. 7 footnote; Sec. 13; final `\bibliography{references}` |
| Paper says verbatim | “\(3\)--\(5\sigma\) realistic after full systematic budget”; “the present paper does not perform an independent SPHEREx Fisher computation”; “reported here only as a cross-reference”; source ends with `\bibliography{references}`. |
| Known fact | Proper significance after GR projection, \(b_\phi\), photo-\(z\), and template-overlap degradation requires an explicit marginalized Fisher covariance. The supplied source contains no `.bib`, no Paper II Fisher artifact, and no auditable metadata for Freidel2005, Mercuri2009, Holst1996, Shamir refs, or Golden2026 companion claims. |
| Verdict | STILL-UNRESOLVED |
| Concrete issue | The \(f_{\rm NL}\) significance is an unauditable external forecast, not an in-paper result; “mechanism-independent” also contradicts the later scalar-only \(w=0\) Assumption-(f) scoping. |
| Fix | Demote to “external Paper II forecast,” remove in-paper \(3\)--\(5\sigma\) claims unless the Fisher matrix and nuisance marginalization are included, and supply the `.bib`/DOI metadata. |
