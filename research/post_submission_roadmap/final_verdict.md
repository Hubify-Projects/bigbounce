# Final Verdict: Post-Submission Roadmap

**Created:** 2026-03-19
**Status:** COMPLETE

---

## 1. Single best post-submission research path

**PBH + induced GW second observable channel.** It is the only path that fundamentally changes the program architecture from one-observable to two-observable. Quick feasibility determination (1-2 sessions). High payoff if viable (second paper, LISA/ET predictions). Clean failure mode (smooth bounce -> dead in one session). Genuinely independent of the f_NL channel (different k-range, different experiments, different systematics).

---

## 2. What should be deprioritized immediately

- ECH perturbation loops (permanently closed, 14+ barriers, mathematical proof)
- Gradient expansion extensions (supporting cross-check only, reaches same bottleneck)
- More MCMC without new theory hooks (reconfirms Delta-N_eff = 0)
- Teleparallel / f(T) / f(Q) sprawl (expands theory space without converging on discriminators)
- Galaxy spin dipole (effectively falsified, 9-12 OOM gap)
- Re-verifying f_NL = -35/8 (done: Cai audit + SymPy + gradient expansion)
- Factor-of-2 debate (resolved: convention/implementation difference)
- Hybrid DE splice (7 forms rejected)
- GFT condensate cosmology (too far from observation)
- CMB anomalies without sharp predictions (2-3 sigma, qualitative fits)

---

## 3. First concrete next calculation

**Characterize the Wilson-Ewing LQC bounce transition sharpness.** Compute w_eff(t) through the bounce using the effective Friedmann equation H^2 = (8piG/3) rho (1 - rho/rho_c). Determine if the transition is sharp enough for perturbation enhancement at k ~ k_bounce. This is an ODE integration, laptop-scale, completable in 1 session. The answer is either "enhancement possible -> proceed to PBH/GW calculation" or "too smooth -> channel dead, pivot to formalism audit."

---

## 4. Next 30 days

- **Week 1:** Submit focused PNG paper + PBH feasibility OOM estimate
- **Week 2:** PBH deep dive (if GO) or LQC formalism audit (if NO-GO)
- **Week 3:** Second paper skeleton or framework paper progress
- **Week 4:** Referee response preparation + strategic review

---

## 5. What future agents must NOT redo

| Work | Status | Evidence Location |
|------|--------|-------------------|
| f_NL = -35/8 verification | COMPLETE (3 methods) | `cai_action_audit/`, `fnl_symbolic_cancellation/`, `gradient_expansion_fnl_derivation/` |
| ECH perturbation novelty search | PERMANENTLY CLOSED (14+ barriers) | `ech_bispectrum_gate/`, `ech_tensor_gate/` |
| Gradient expansion of f_NL | SUPPORTING (not frontier) | `gradient_expansion_fnl_derivation/` |
| 800K Monte Carlo Bayes factors | COMPLETE | `bayesian_discrimination_program/`, `gr_contamination_claim_hardening/` |
| SPHEREx/MegaMapper forecast | HARDENED (GR marginalized) | `forecast_hardening_program/`, `survey_realism_reconciliation/` |
| Wilson-Ewing model viability filtering | COMPLETE (only Model B survives) | `project_viable_bounce_model_pass2/` |
| Convention analysis (Cai-to-Planck) | RESOLVED (no hidden factor) | `fnl_derivation_execution/` |
| Survey realism reconciliation | COMPLETE (GR projection = dominant systematic) | `survey_realism_reconciliation/` |
| Inflation mimicry analysis | COMPLETE (negative O(1) f_NL hard-to-mimic) | `inflation_mimicry_deep_comparison/` |
| Galaxy spin coupling gap | EFFECTIVELY FALSIFIED (9-12 OOM) | `branch_V_bounce_evidence/` |
| Hybrid DE splice | EXHAUSTIVELY REJECTED (7 forms) | `foundation_A-G/`, `next_flagship_program/` |
| 200K synthetic power spectra | COMPLETE (BF 425:1) | `optional_premium_robustness/` |
| Fisher robustness surface | COMPLETE (k_min sensitivity mapped) | `fisher_robustness_surface/` |
| Ultra-large-scale systematics | COMPLETE (GR, b_phi, bispectrum) | `ultra_large_scale_systematics_audit/` |
| Last-mile robustness | COMPLETE (83% of realizations BF > 10) | `last_mile_robustness_program/` |

---

## Program State Summary

```
FROZEN:
  Focused PNG paper .................. DRAFT COMPLETE
  f_NL = -35/8 benchmark ............ VERIFIED (3 methods)
  SPHEREx forecast .................. 4-6 sigma (hardened)
  MegaMapper forecast ............... 3-7 sigma (hardened)
  Bayesian discrimination ........... >300:1 vs standard inflation
  Inflation mimicry ................. Quantified (0-param vs 2+-param)
  ECH perturbation program .......... PERMANENTLY CLOSED
  MCMC infrastructure ............... FROZEN (236K samples, 64 chains)
  Cai action audit .................. RESOLVED (3 mismatches explained)
  Convention analysis ............... RESOLVED (no hidden factor)

LIVE:
  PBH + induced GW channel .......... NOT YET ASSESSED (30-50% viability)
  LQC formalism sensitivity ......... OPEN (likely null, 15-25% non-trivial)
  Paper 1 framework paper ........... 75% READY
  Companion theory paper ............. COMPILABLE FROM EXISTING MATERIAL
  Scale-dependent f_NL .............. OPEN (likely negligible, ~5% viable)

DEAD:
  ECH perturbation novelty .......... 14+ barriers (mathematical proof)
  Galaxy spin dipole ................ 9-12 OOM coupling gap
  Hybrid DE splice .................. 7 forms rejected
  Tension reduction via Delta-N_eff . Disproved (approximately 0)
  Chiral GW from ECH ............... Frequency gate failed (5 closures)
  Blue tensor tilt (practical) ...... r too small for any planned detector
  S8 tension from bounce ............ One paper, requires hybrid, not competitive
  PBH from dust-radiation .......... Vanishing fractions (2026 calculation)
  Baryogenesis from bounce .......... No quantitative prediction
  CMB anomalies (without predictions) Qualitative only, 2-3 sigma
```

---

## The One-Sentence Summary

Submit the focused PNG paper, then spend 1-2 sessions determining whether the Wilson-Ewing LQC bounce produces PBH and induced gravitational waves as a second independent observable -- this is the single highest-leverage action that could transform the program from one-prediction fragile to two-prediction resilient.
