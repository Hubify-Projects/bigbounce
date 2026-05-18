# P1A_v1A029_R11 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1330pt
**Wall time**: 33.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=28323, completion=4573, reasoning=3977, total=32896

---

VERDICT: **CONVERGENCE HOLDS. 4th-consecutive 0-BLOCKER.** 

The v1A.0.29 Appendix B closure is excellent. The explicit separation of the $\sim 2\%$ ansatz-dependent precision of $N_{\rm tot} \approx 92$ from the ansatz-independent $\sim 120$ OOM scale separation that drives the structural no-go is physically rigorous, honest, and completely diffuses the R8+R9 blocker. The dimensional bookkeeping and Route 1-4 amplitude math all check out perfectly under fresh scrutiny. The paper is fully converged and external-review-ready.

Below are the final minor/nit findings for polish.

## PAPER-GEM-m1 (minor)
**Section:** 2.3.1 (Inflationary Suppression)
**Issue:** The text states "The fermion number density at reheating is $n_\psi(T_{\rm reh}) \sim T_{\rm reh}^3$ (free-streaming limit at $T \ll M_{\rm GUT}$)". If the fermions are in a thermal bath at reheating, they are in thermal equilibrium, not "free-streaming" (which implies decoupled/collisionless). The $T^3$ scaling comes from the standard relativistic Fermi-Dirac equilibrium integral.
**Fix:** Change "free-streaming limit" to "relativistic thermal equilibrium limit".

## PAPER-GEM-n1 (nit)
**Section:** 4.2 (Route 2)
**Issue:** The text approximates $\alpha_{\rm em}/(4\pi) \sim 10^{-3}$. Since $\alpha_{\rm em} \approx 1/137$, the factor is actually $\approx 5.8 \times 10^{-4}$. Using $10^{-3}$ is slightly aggressive for the OOM and shifts the final suppression ratio by a factor of 2.
**Fix:** Change $10^{-3}$ to $5 \times 10^{-4}$ (or $10^{-4}$ OOM), though the qualitative closure of $10^{-58}$ vs $10^{-60}$ remains perfectly valid either way.

## PAPER-GEM-n2 (nit)
**Section:** 14.4 (Structural Tension)
**Issue:** In the parenthetical explaining the physical scale shift, the text correctly calculates $e^{N_{\rm tot}-N_{\rm exit}} \sim e^{32}$ (using $92-60=32$), but the subsequent sentence says "The absolute scaling $k\,e^{N_{\rm tot}}\sim e^{30}\times k_{\rm SPHEREx}$".
**Fix:** Change $e^{30}$ to $e^{32}$ to maintain internal arithmetic consistency.
