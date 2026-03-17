# Final Verdict: Paper 1 Salvage Assessment

**Date:** 2026-03-17

---

## 1. Can Paper 1 be salvaged honestly?

**YES.** But only by removing roughly half its claims.

The salvaged paper retains:
- A well-defined bounce cosmology (ECH action, quantum bounce, torsion physics)
- A comprehensive closure of DE derivation routes (13 barriers, honest negative result)
- A quantitative ALP birefringence prediction (beta ~ 0.27 deg, 1-sigma match to data)
- MCMC constraints on ALP parameter space
- A concrete falsification program (LiteBIRD, CMB-S4)

The salvaged paper removes:
- All DE derivation claims (Lambda_eff = Xi M_Pl^2 + ...)
- All tension reduction claims (H_0 = 69.2, sigma_8 = 0.785)
- All galaxy spin predictions (9+ OOM gap)
- The ALP-as-DE interpretation (factor-2 tension)
- The fine-tuning reduction claim (10^{120} -> 10^5)
- Correlated-axes prediction

This is a net improvement. The remaining paper is smaller, sharper, and more honest.

---

## 2. What is the strongest salvaged version?

A three-part paper:

**Part 1: ECH Bounce Cosmology** (~4 pages)
- Action, torsion, four-fermion interaction, bounce
- Well-established physics, no overclaims

**Part 2: Structural Closure** (~3 pages)
- 13 barriers in compact table form
- 5 failure modes summarized
- Referencing companion note for full details
- "The ECH framework cannot derive dark energy or produce distinctive signatures"

**Part 3: Spectator ALP Birefringence** (~6 pages)
- ALP sector specification
- Birefringence prediction: beta = C alpha theta_i / (4 pi)
- MCMC constraints from current data
- Model comparison (ALP vs null)
- LiteBIRD forecast
- Falsification criteria

**Appendices** (~4 pages)
- Notation, parameter summary, dimensional analysis, reproducibility, claims table

**Total: ~17 pages two-column** (down from ~31 pages). A focused, publishable paper.

---

## 3. What must be removed no matter what?

These claims are dead and cannot be resurrected by any framing:

1. **Lambda_eff = Xi M_Pl^2** — All four derivation routes closed. This is not a result.
2. **H_0 = 69.2 +/- 0.8** — Artifact of SH0ES prior. Own verification disproved it.
3. **sigma_8 = 0.785** — Same issue.
4. **"Simultaneous tension reduction"** — Does not exist. Delta-Neff is zero.
5. **Galaxy spin dipole from ECH** — 9-12 OOM gap. Cannot be bridged.
6. **A(z) = A_0(1+z)^{-p} e^{-qz}** — Empirical fit to contested data with no theory connection.
7. **"Fine-tuning from 10^120 to 10^5"** — The dimensional chain is illustrative, not a derivation.
8. **ALP = dark energy** — Factor-2 tension between birefringence and DE requirements.
9. **"Correlated cosmic anomaly axes"** — Requires galaxy spin dipole, which is dead.
10. **NJL condensate vacuum energy** — Subcritical by factor 175.

Keeping ANY of these would be intellectually dishonest and would undermine the credibility of the real results.

---

## 4. Is the spectator ALP branch strong enough to anchor the paper?

**YES, with caveats.**

### Strengths as paper anchor:
- Quantitative prediction: beta = 0.27 deg (not an order-of-magnitude estimate)
- 1-sigma match to 3.9-sigma detection (not a vague "consistency")
- f_a independence (robust against UV uncertainty)
- All constraints satisfied by 9+ orders of magnitude
- Concrete MCMC posterior (publishable figure)
- Clean falsification by LiteBIRD (sigma_beta ~ 0.01 deg)

### Caveats:
- **Not unique to ECH.** Any Planck-scale ALP with SM coupling gives the same. ECH is motivation, not derivation.
- **theta_i is free.** O(1) is natural but not predicted. The data constrain theta_i ~ 0.6-2.0.
- **m_a is free.** m ~ H_0 is the CC problem. The spectator regime (m >> H_0) is less fine-tuned but also less interesting for DE.
- **The coupling is assumed.** The one-loop photon-torsion vertex has not been computed. Branch S showed it exists (ABJ triangle) but is Planck-suppressed for ECH-specific terms.

### Assessment:
The ALP prediction is strong enough for a focused paper. It is NOT strong enough to be the sole content of the paper --- it needs the ECH context (Part 1) and the closure assessment (Part 2) to have weight. A standalone "we predict beta = 0.27 deg from a Planck-scale ALP" paper would be correct but thin. The three-part structure gives it substance.

---

## 5. What is the exact immediate next move?

### This week (priority order):

1. **Implement `alp_ode.py`** (~2 hours)
   - ALP ODE integrator on LCDM background
   - Validate against Phase 2 prefit table
   - Confirm single evaluation < 0.1 sec

2. **Implement `alp_theory.py` + `birefringence_lk.py`** (~1 hour)
   - Cobaya Theory and Likelihood classes
   - Test with `cobaya-run --test`

3. **Run MCMC (Run 2)** (~3 hours)
   - 4 chains x 100K, birefringence-only
   - Target R-1 < 0.01
   - Generate triangle plot and posterior summary

4. **Post-process and assess** (~1 hour)
   - Does the posterior make sense?
   - Does beta_deg encompass the observed value?
   - Is the constraint informative?

### If Run 2 succeeds:

5. **Begin Paper 1 restructure** using salvage map (01), section rebuild plan (03), and claims table (05)
6. Insert MCMC results into revised birefringence section
7. Run 3 (floating C_{agamma}) if time permits

### If Run 2 fails (pathological posterior, code bugs, etc.):

5. Debug and fix
6. Do not proceed to paper restructure until MCMC works

---

## Bottom Line

Paper 1 can be salvaged into an honest, focused, publishable paper. The core pivot is from "dark energy from quantum gravity" to "bounce cosmology + ALP birefringence phenomenology." This is a smaller paper with bigger integrity. The spectator ALP prediction (beta ~ 0.27 deg) is the single strongest result from the entire research program, and it deserves a clean presentation. Everything else --- the DE derivation, the tension reduction, the galaxy spins --- was hope, not physics. Cutting it makes the paper better, not worse.

The immediate next step is implementing the ALP ODE integrator and running the first MCMC. Everything else follows from that.
