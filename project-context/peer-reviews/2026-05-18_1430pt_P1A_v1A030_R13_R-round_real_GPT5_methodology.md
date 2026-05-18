# P1A_v1A030_R13 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1430pt
**Wall time**: 122.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28574, completion=6552, reasoning=5696, total=35126

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR — Sec. 4.2 Route 2

The one-loop amplitude budget is still not a controlled dimensional derivation: the text quotes both a \(10^{-58}\)–\(10^{-60}\) ratio and a “complementary” \(10^{-33}\) ratio from different contractions of \(H_0\), \(M_{\rm Pl}\), and \(M_{\rm Pl}(\alpha/M)\). These cannot both be presented as valid amplitude-budget calculations.  
Fix: derive one unique photon-Chern-Simons/birefringence mapping with explicit dimensions for \(\theta\), \(J^{5\mu}\), and the induced photon coupling; otherwise demote the quantitative OOM claim to qualitative suppression.

## PAPER-GPT-M2 — MAJOR — Sec. 4.3 Route 3

The claim that Immirzi running is suppressed by \((\Delta\gamma/\gamma)(H/M_{\rm Pl})\sim10^{-63}\) “relative to the dark-energy density” mixes dimensionless amplitude scaling with density scaling. A density comparison must be built from a dimension-four operator, e.g. involving \(H^2M_{\rm Pl}^2\) or explicit curvature powers, not a single \(H/M_{\rm Pl}\) factor.  
Fix: specify whether R3 is being compared to a birefringence angle/amplitude or to \(\rho_\Lambda\); redo the dimensional estimate accordingly and remove “relative to dark-energy density” unless a dimension-four derivation is supplied.

## PAPER-GPT-M3 — MAJOR — Sec. 12.1 / Sec. 14.3 Structural tension

The text says the surplus e-folds needed to close the gap are “\(\sim14\)” while the paper’s own numbers are \(N_{\rm tot}\approx92\) versus \(N_{\rm exit}\sim60\), i.e. a differential of \(\sim32\) e-folds, repeatedly used elsewhere. This is an internal arithmetic inconsistency in the structural-tension argument.  
Fix: replace “\(\sim14\)” with “\(\sim32\)” or define a different reference baseline that actually yields 14.

## PAPER-GPT-M4 — MAJOR — Sec. 4.6 Closure summary / Conclusions

The closure summary says R1–R4 “exhaust” the available minimal-ECH parity-odd/dark-energy channels and the conclusion says the barriers close “every” minimal-ECH route, but the abstract/scope explicitly state this is not an operator-basis closure and defer Jackiw–Pi \(R\wedge\widetilde R\) and the parity-odd four-fermion partner. That is a scope regression.  
Fix: replace “exhaust” / “every route” with “the four enumerated standard channels” and restate that omitted parity-odd operators require a later operator-level analysis.

## PAPER-GPT-m1 — minor — Sec. 10 Perturbation-transparency proof

The proof alternates between “Holst term becomes topological,” “total derivative,” and “vanishes identically by Bianchi.” For the torsion-free Levi-Civita connection, the Holst dual contraction vanishes identically; that is not the same statement as a nonzero topological total derivative.  
Fix: say simply that the Levi-Civita Holst integrand is identically zero by the first Bianchi identity, so its variation vanishes.

## PAPER-GPT-m2 — minor — Sec. 12.1 Spectator-ALP birefringence

The sentence claiming \(f_a\sim M_{\rm Pl}, m\sim H_0\) is consistent with the signal “without fine-tuning” contradicts Sec. 4.4, which correctly says \(m_\theta\sim H_0\) reimports the cosmological-constant tuning.  
Fix: change to “phenomenologically viable with the usual ultralight-mass tuning; not ECH-derived.”
