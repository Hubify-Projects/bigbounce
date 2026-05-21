# paper1a R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P1A_v1A_0_34
**Wall time**: 124.1s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=30043, completion=6532, reasoning=5696, total=36575

---

No blocker-grade findings found.

## PAPER-GPT-M1 — MAJOR — §IV “Closure summary” / §XV Conclusions

**Issue:** The text still overclaims exhaustion: “Routes R1--R4 between them exhaust…” and “close every minimal-ECH dark-energy route,” despite earlier admitting Jackiw--Pi gravitational CS and parity-odd four-fermion operators are not enumerated.  
**Fix:** Replace with “close the four enumerated channel-level routes” everywhere; explicitly state omitted operators are outside this theorem.

## PAPER-GPT-M2 — MAJOR — §II.C.1 Inflationary Suppression

**Issue:** The dilution derivation mixes quantities with different scaling: torsion amplitude scales like axial current $n_\psi\propto a^{-3}$, four-fermion energy scales like $n_\psi^2\propto a^{-6}$, while the text invokes a “cubic axial-current operator” but still uses $e^{-3N}$. This makes the $N_{\rm tot}\approx92$ bookkeeping power-dependent and not internally derived.  
**Fix:** Define the diluted object unambiguously and propagate the correct $a^{-p}$ scaling; otherwise label the whole $e^{-3N}$ law as a phenomenological ansatz, not “matched to first-principles arguments.”

## PAPER-GPT-M3 — MAJOR — §IV.B Route 2

**Issue:** The one-loop birefringence ratio is still not a controlled dimensional reduction: the manuscript admits two “dimensionless” orderings giving $10^{-60}$ vs $10^{-33}$, a 27-order ambiguity. That is incompatible with “amplitude-budget granularity.”  
**Fix:** Derive the photon/CS rotation angle from the stated one-loop operator with all field dimensions fixed, or drop the numerical ratio and state only qualitative Planck/loop suppression.

## PAPER-GPT-M4 — MAJOR — §IV.D Route 4 / §XII.B / §IV.E

**Issue:** R4 is internally inconsistent: §IV.D says the same coupling can reproduce both $\beta_{\rm obs}$ and $\rho_\Lambda$ if $m_\theta\sim H_0$ but this is tuned; §IV.E says the same coupling “cannot deliver both”; §XII.B says $m\sim H_0$ is “without fine-tuning.”  
**Fix:** Use one position consistently: “can fit both only by tuning $m_\theta\sim H_0$; therefore not a natural ECH dark-energy solution.”

## PAPER-GPT-M5 — MAJOR — Abstract / §XIII / §XIV.D Structural Tension

**Issue:** The claim that $N_{\rm tot}\gtrsim60$ “definitively” erases the matter-bounce $\fnl$ is asserted from subhorizon scaling alone. Subhorizon placement does not by itself prove erasure without a transfer/matching calculation and assumptions about inflationary attractor initial conditions.  
**Fix:** Replace “definitively erased” with a conditional statement, or add a perturbation transfer calculation showing decay/overwriting of the pre-bounce bispectrum.

## PAPER-GPT-m1 — minor — §IV.D Route 4, Chern--Simons current

**Issue:** With $K^\mu=\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$, the standard Abelian identity is $\partial_\mu K^\mu = F_{\mu\nu}\tilde F^{\mu\nu}$ up to sign convention, not $\tfrac12\tilde F_{\mu\nu}F^{\mu\nu}$ unless $K^\mu$ carries an extra $1/2$.  
**Fix:** Either define $K^\mu=\tfrac12\epsilon^{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma}$ or remove the extra $1/2$ in the divergence identity.
