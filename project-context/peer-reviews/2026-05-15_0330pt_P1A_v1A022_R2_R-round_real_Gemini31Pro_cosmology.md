# P1A_v1A022_R2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0330pt
**Wall time**: 69.1s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=25666, completion=8561, reasoning=7579, total=34227

---

## BLOCKER: Appendix B Dimensional Bookkeeping Violates EFT Rules
**ID:** PAPER-GEM-B1
**Section:** Appendix B (Eq. 24)
**Concrete Issue:** The dimensional "fix" is EFT word salad. An off-shell Lagrangian density must have mass dimension +4. You cannot fix a dimension +1 operator ($\frac{\alpha}{M}\epsilon e e \mathcal{F}$) by multiplying it by on-shell background curvature values ($K, R$) that are absent from the operator, nor by inventing a "spatial volume integration density" factor of $M_{Pl}^2$. 
**Fix:** Acknowledge the operator is dimensionally invalid as written, or write the correct dimension-4 operator (e.g., by explicitly including the required $M_{Pl}^3$ in the coupling coefficient rather than relying on illegal on-shell background insertions).

## BLOCKER: Route 2 Dimensional Error Retained in Proof
**ID:** PAPER-GEM-B2
**Section:** 4.2 (Eq. 13)
**Concrete Issue:** Leaving a known dimensional error in a load-bearing proof equation with a "deferral note" is unacceptable for a no-go theorem claiming amplitude-level closure. Eq. 13 equates a dimensionless ratio $\Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs}$ to a quantity with units of mass ($\frac{H_0}{M_{Pl}(\alpha/M)\beta_{\rm obs}} \sim 10^{-58}$ GeV).
**Fix:** Correct the dimensional matching in Eq. 13 by inserting the missing $1/M_{Pl}$ factor derived from the proper effective action, ensuring both sides of the equation are strictly dimensionless.

## MAJOR: Torsion "Dilution" Memory is Physically Impossible
**ID:** PAPER-GEM-M1
**Section:** 2.3.1 (Eq. 10)
**Concrete Issue:** The inflationary dilution argument ($\Dinf \sim e^{-3N_{\rm tot}}$) fails because torsion in minimal ECH is non-propagating and tracks *instantaneous* local fermion density. Reheating creates a massive thermal bath of fermions ($n_\psi \sim T_{\rm reh}^3$), which completely overwrites any "diluted" torsion from the bounce.
**Fix:** State explicitly that reheating destroys the bounce-torsion memory, adding this thermodynamic reset as an additional fatal barrier to the ECH dark-energy route.

## MAJOR: Structural Tension Erasure is Understated
**ID:** PAPER-GEM-M2
**Section:** 14.4
**Concrete Issue:** The structural tension claims $N_{\rm tot}\approx 92$ "plausibly erases" the bounce $\fnl$ at SPHEREx scales. This is a severe understatement. $N_{\rm tot}\approx 92$ definitively pushes bounce-crossing scales $\sim e^{30}$ times larger than the observable universe; SPHEREx modes would originate entirely from standard inflationary quantum fluctuations ($\fnl \sim 0.015$).
**Fix:** Change "plausibly erased (precise threshold mode-dependent...)" to "definitively erased, as SPHEREx comoving scales would originate deep inside the inflationary horizon."

## minor: Misattribution of Bare Operator to Mercuri 2009
**ID:** PAPER-GEM-m1
**Section:** 2.1.2 (Step 3, Eq. 5)
**Concrete Issue:** Eq. 5 and 6 are misattributed. Mercuri (2009) derives the Nieh-Yan invariant coupled to an axion field ($\partial_\mu a J^\mu_5$), not a dimensionally broken bare operator $\frac{\alpha}{M} \epsilon e e \mathcal{F}$.
**Fix:** Remove the direct attribution of the bare Eq. 5/6 to Mercuri 2009, or write the actual Nieh-Yan topological density he derived.

## nit: Compute-Log Filler in Table Footnote
**ID:** PAPER-GEM-n1
**Section:** Table III (Footnote $\ddagger$)
**Concrete Issue:** The footnote detailing MPI pods, OMP threads, BLAS oversubscription, and exact $\hat{R}-1$ descent values is compute-log filler that does not belong in a theoretical physics paper.
**Fix:** Truncate to "A new DESI DR2 $w_0w_a$ chain is currently running; results will be reported when convergence ($\hat{R}-1 < 10^{-2}$) is achieved."
