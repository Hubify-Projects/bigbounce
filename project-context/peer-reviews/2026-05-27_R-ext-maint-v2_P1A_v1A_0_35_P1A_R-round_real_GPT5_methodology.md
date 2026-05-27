# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P1A_v1A_0_35
**Wall time**: 130.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=29784, completion=6627, reasoning=5696, total=36411

---

No BLOCKER-grade findings. Clean convergence does **not** hold because MAJOR issues remain.

## PAPER-GPT-M1

**Classification:** MAJOR  
**Section:** Abstract; §IV “Scope”; §IV.E “Closure summary”; §XV Conclusions  
**Issue:** The paper admits the four routes are not an operator-level basis and omits Jackiw–Pi gravitational Chern–Simons and the parity-odd four-fermion partner, but later says R1–R4 “exhaust” minimal-ECH parity-odd/dark-energy channels and “close every minimal-ECH dark-energy route.”  
**Fix:** Replace all exhaustive/no-go theorem language with “enumerated channel-level routes,” or explicitly close the omitted operators with amplitude estimates.

## PAPER-GPT-M2

**Classification:** MAJOR  
**Section:** §IV.B Route 2, Eq. after `\eqref{eq:oneloop_parity_odd}`  
**Issue:** The one-loop birefringence ratio is not a controlled dimensional derivation: the text gives incompatible estimates, \(10^{-58}\!-\!10^{-60}\) and \(10^{-33}\), and admits they differ by contraction ordering. This is not acceptable for an amplitude-budget closure.  
**Fix:** Derive the photon/CS matching from the one-loop Nieh–Yan/axial-current operator with explicit field dimensions and line-of-sight integral, then quote one dimensionless ratio only.

## PAPER-GPT-M3

**Classification:** MAJOR  
**Section:** §II.A.2 Eq. `\eqref{eq:4fermi}` vs §IV.A Route 1  
**Issue:** The Holst four-fermion coefficient is inconsistent: Eq. `\eqref{eq:4fermi}` contains \(\gamma^2/(\gamma^2+1)\), while Route 1 uses the pure EC coefficient and states the torsion-elimination map is classically independent of \(\gamma\). Both cannot be true for the same minimal/non-minimal fermion coupling choice.  
**Fix:** Specify the fermion coupling convention and propagate the correct \(\gamma\)-dependent or \(\gamma\)-independent coefficient consistently through R1, R4, and the barrier table.

## PAPER-GPT-M4

**Classification:** MAJOR  
**Section:** §X Perturbation Transparency; §IX Barrier 14; §XV Conclusions  
**Issue:** The transparency theorem is proven only for canonical scalar matter, but it is used to support broad claims about minimal ECH/SM perturbations and to subsume parity/tensor channels. Fermionic spin density is explicitly listed as a failure mode, yet SM fermions are central to the torsion mechanism.  
**Fix:** Restrict the theorem to scalar-only backgrounds/perturbations and separately analyze spin-fluid/fermionic perturbations, or remove claims that B14 closes fermion-sourced ECH parity channels.

## PAPER-GPT-M5

**Classification:** MAJOR  
**Section:** §VI Systematics; §VII Falsification Criteria; §XIII Surviving Tests  
**Issue:** The quoted SPHEREx \(3\!-\!5\sigma\) \(\fnl=-35/8\) significance is not propagated in this paper: template overlap, GR projection, \(b_\phi\), photo-\(z\), and covariance degradation are listed but not combined into a reproducible Fisher error. The text therefore overclaims a statistical result hosted elsewhere.  
**Fix:** Either include the Fisher covariance/systematic propagation table here, or state only “Paper II forecasts \(3\!-\!5\sigma\)” and remove independent significance language from this paper.

## PAPER-GPT-M6

**Classification:** MAJOR  
**Section:** §IV.D Route 4; §XII.B “Spectator-ALP birefringence”; §XIII  
**Issue:** Internal fine-tuning claim is contradictory: Route 4 says \(m_\theta\sim H_0\) is the cosmological-constant tuning relabelled, while §XII.B says an ALP with \(f_a\sim M_{\rm Pl}, m\sim H_0\) is consistent “without fine-tuning.”  
**Fix:** Distinguish technical naturalness from absolute mass/DE tuning, and remove “without fine-tuning” unless the \(m\sim H_0\) scale is derived or protected.
