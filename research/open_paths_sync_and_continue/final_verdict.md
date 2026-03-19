# Final Verdict: Open Paths Sync and Continue

**Created:** 2026-03-19
**Status:** COMPLETE

---

## 1. What was stale/superseded?

| Item | Classification | Superseded By |
|------|---------------|---------------|
| f_NL coefficient resolution (-35/8 vs -35/16) | **SUPERSEDED** | Cai action audit: three specific differences identified, convention resolved, -35/8 accepted at >85% confidence |
| Numerical in-in integral as bottleneck | **SUPERSEDED** | Cai audit showed problem was wrong starting point, not integration. SymPy verified T1-T4 = 35/16 to 0.07%. |
| Gradient expansion as frontier | **SUPERSEDED** | Now SUPPORTING_ONLY. Confirms structural features already known. Full coefficient resolved by Cai audit, not by gradient expansion. |
| Sign convention debate | **SUPERSEDED** | Mode-function conjugation (Cai's u_k = A*sqrt(3)*zeta_k*) explains sign flip. f_NL(Planck) = |B|_NL(Cai) in squeezed limit. No ambiguity. |
| "75% confidence in f_NL" | **SUPERSEDED** | Now >85% after three independent verifications. |
| "Gradient expansion verification is #1 priority" | **SUPERSEDED** | Overtaken by Cai audit. Post-submission roadmap correctly places PBH+GW as #1. |
| Scale-dependent f_NL | **STALE** | LQC correction: 10^{-112}. Contraction running: 0.14 sigma. Permanently undetectable. |

---

## 2. Is the gradient expansion still frontier?

**NO. SUPPORTING_CROSS_CHECK only.**

The gradient expansion independently confirms four structural features (negative sign, O(1) magnitude, local shape, parameter-free). These were ALL already established by the in-in execution phase. The exact coefficient (the only open quantitative question) was resolved by the Cai action audit, not by the gradient expansion. The gradient expansion deserves 3-4 sentences in the paper or a 1-page appendix. No further computation warranted.

See `01_role_of_gradient_expansion_now.md` for the complete analysis.

---

## 3. What genuinely remained open before this session?

Before executing the PBH feasibility test, three paths were genuinely open:

1. **PBH + Induced GW second observable** -- consensus #1 from both post-submission roadmap and LQC openings audit
2. **LQC formalism sensitivity** -- untested, but likely null
3. **Paper 1 framework paper** -- 75% ready, compilation exercise

After executing the PBH feasibility test (File 05):

**The PBH + GW channel is now DEAD.** The Wilson-Ewing LQC bounce occurs at Planck density (rho_c ~ 0.41 M_Pl^4). Enhanced modes are at frequencies ~ 10^{11} - 10^{12} Hz today -- permanently inaccessible to any detector. For PBH-relevant modes, the transfer function is T = 1 + O(10^{-30}). Same frequency-gate physics that killed the chiral GW program.

The genuinely open paths are now:

| Path | Status | Probability of Positive Result |
|------|--------|-------------------------------|
| LQC formalism sensitivity audit | OPEN | ~15% (non-null) |
| Paper 1 framework paper completion | OPEN | N/A (compilation) |
| Companion theory paper | OPEN | N/A (compilation) |

---

## 4. Single best remaining path

**LQC formalism sensitivity audit.**

This is the only remaining path that could produce NEW positive science. The other open paths (Paper 1 completion, companion theory paper) are compilation exercises that package existing results.

The formalism audit asks: do the dressed-metric and hybrid LQC perturbation formalisms give the same bispectrum for modes at k << k_LQC?

**Most likely outcome:** Both formalisms agree (probability ~85%). The prediction's robustness is formally established. This is a null result but a USEFUL null result that strengthens the submitted paper.

**Exciting outcome:** The formalisms disagree (probability ~15%). This would be testable quantum gravity -- the first bispectrum-level prediction that depends on the choice of LQC formalism. This would be a major result, worthy of its own paper.

**First step:** Read arXiv:2405.12296 (2024 LQC perturbation comparison). Determine if their power-spectrum comparison extends to the bispectrum. If not, assess whether their superhorizon-mode results imply bispectrum insensitivity by dimensional analysis.

**Effort estimate:** Literature check (hours). If a gap exists, 1-2 sessions for the calculation.

---

## 5. First step executed: PBH + GW feasibility OOM estimate

**Result: KILLED.**

The complete calculation is in `05_first_step_execution.md`. Key numbers:

```
Wilson-Ewing bounce density:          rho_c ~ 0.41 M_Pl^4
Bounce timescale:                     ~ 0.44 t_Pl
Enhancement scale (frequency today):  ~ 10^{11} - 10^{12} Hz (THz)
Gap to LISA:                          10^{12-13}
Gap to LIGO/ET:                       10^{7-8}
Transfer function at PBH scale:       T = 1 + O(10^{-30})
Enhancement at PBH scale:             ZERO
```

The kill mechanism is identical to the chiral GW frequency gate: a Planck-scale bounce produces Planck-scale features that are permanently inaccessible after cosmological expansion. Enhanced modes at k ~ k_* ~ a_bounce * M_Pl correspond to ~ THz frequencies today. PBH-relevant modes (k ~ 10^{5} - 10^{12} Mpc^{-1}) are 14-21 orders of magnitude below the enhancement scale, deeply superhorizon during the bounce, and pass through with T = 1 to 30-digit precision.

The Papanikolaou et al. (2024) mechanism requires a bounce at much lower energy density than LQC provides. Their parametrized bounce can be tuned to enhance modes at any scale; the Wilson-Ewing bounce cannot.

No escape route (lower bounce density, post-bounce phase transition, cyclic amplification, modified dispersion) survives within the Wilson-Ewing model.

---

## 6. What this terminal must NOT do

| Action | Reason |
|--------|--------|
| Reopen ECH perturbation theory | Permanently closed. Mathematical proof. 14+ barriers. |
| Redo f_NL verification | Resolved: -35/8 (3 methods). |
| Extend gradient expansion | SUPPORTING_ONLY. Coefficient resolved by Cai audit. |
| Draft papers | Not this terminal's scope. Focused-paper draft already complete. |
| Propose publication | Not this terminal's scope. |
| Restart PBH channel | NOW DEAD. Same frequency gate as chiral GW. |
| Run more MCMC | Delta-N_eff = 0. No new theory hooks. |
| Explore teleparallel/f(T)/f(Q) | Sprawl without discriminators. |
| Reopen convention debates | Fully resolved by Cai audit. |
| Propose sub-Planckian bounce models | Reintroduces model-dependence, undermines the Wilson-Ewing framework. |

---

## 7. Updated Program Architecture

```
FROZEN (quantitatively complete):
  f_NL = -35/8 benchmark .............. VERIFIED (3 methods)
  SPHEREx forecast .................... 4-6 sigma (hardened, 800K MC)
  MegaMapper forecast ................. 3-7 sigma (hardened, GR-marginalized)
  Bayesian discrimination ............. >300:1 vs standard inflation
  Inflation mimicry ................... Quantified (0-param vs 2+-param)
  ECH perturbation program ............ PERMANENTLY CLOSED (14+ barriers)
  MCMC infrastructure ................. FROZEN (236K samples, 64 chains)
  Cai action audit .................... RESOLVED (3 mismatches explained)
  Convention analysis .................. RESOLVED (no hidden factor)
  Gradient expansion ................... SUPPORTING_CROSS_CHECK
  Focused paper draft .................. COMPLETE (9 sections)

NEWLY DEAD (killed this session):
  PBH + induced GW channel ............ DEAD (frequency-gate kill, T = 1 + O(10^{-30}))

PREVIOUSLY DEAD:
  Chiral GW from ECH .................. DEAD (5 closures, same frequency gate)
  Galaxy spin dipole ................... DEAD (9-12 OOM gap)
  Hybrid DE splice .................... DEAD (7 forms rejected)
  Tension reduction via Delta-N_eff ... DEAD (approximately 0)
  Scale-dependent f_NL ................ DEAD (permanently below detection)

LIVE:
  LQC formalism sensitivity ........... OPEN (likely null, 15% non-trivial)
  Paper 1 framework paper .............. 75% READY (compilation)
  Companion theory paper ............... COMPILABLE FROM EXISTING MATERIAL
```

---

## 8. The One-Sentence Summary

The PBH + induced GW channel -- the single highest-priority open path identified by two independent audits -- is killed by the same Planck-scale frequency gate that killed chiral GWs, leaving the LQC formalism sensitivity audit as the only remaining path that could produce new positive science, with ~15% probability of a non-null result.
