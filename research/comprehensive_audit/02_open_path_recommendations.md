# 02: Open Path Recommendations

## Genuinely Open Paths

### 1. LQC Formalism Sensitivity: Dressed-Metric vs Hybrid (HIGH VALUE)
**Status:** Nobody in the literature has compared f_NL predictions between the dressed-metric and hybrid approaches to LQC perturbation theory.
**Value:** If they give different f_NL, that's a genuine new result (N3 potential). If they agree, that's a robustness confirmation.
**Effort:** Medium — requires LQC perturbation theory expertise. Analytic work, no MCMC.
**Recommendation:** PURSUE as the next theoretical project after Paper 5 submission.

### 2. Scale-Dependent f_NL from LQC Corrections (LOW-MEDIUM VALUE)
**Status:** LQC quantum corrections could modify f_NL at scales near k_bounce (~M_Pl). At CMB scales (60 orders away), the effect is negligible.
**Value:** Theoretically interesting but observationally irrelevant with current technology.
**Effort:** Medium analytic.
**Recommendation:** DEFER unless formalism sensitivity (path 1) reveals something unexpected.

### 3. ALP Birefringence Continuation (MEDIUM VALUE, INDEPENDENT)
**Status:** β = 0.27° prediction matches 3.9σ observed signal. LiteBIRD will test decisively.
**Value:** A clean, published positive result. Bounce-independent.
**Effort:** Paper 2 drafting (~1-2 sessions).
**Recommendation:** CONTINUE as independent parallel track. Write Paper 2 after Paper 5 is submitted.

## Paths That Should NOT Be Reopened

| Path | Reason |
|------|--------|
| ECH scalar perturbations | Permanently closed (Barrier 14) |
| ECH tensor perturbations | Permanently closed (same + 5 prior barriers) |
| Dark energy from bounce | 14 barriers; 7 foundations exhausted |
| Hybrid-DE / w₀wₐ freedom | Rejected; 7 forms explored |
| Chiral GW from bounce | Frequency gate failed (GHz) |
| PBH + induced GW | Killed by same frequency gate |
| Dynamical Immirzi | Reduces to generic ALP (Branch Q closed) |

## Should Additional MCMC or MC Simulations Be Run?

**NO for the current science case.** 800K+ MC samples are already converged. 236K MCMC posteriors are archived. No additional computation adds meaningful value to the focused paper.

**POSSIBLY for Paper 2 (ALP):** The Branch R Phase 2 MCMC may need completion for publication-quality posteriors. This would be the only justified additional computation.

**POSSIBLY for LQC formalism sensitivity (path 1):** If pursued, this would be a new analytic + possibly numerical project, not a re-run of existing chains.
