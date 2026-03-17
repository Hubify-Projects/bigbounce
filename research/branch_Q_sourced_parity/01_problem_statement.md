# Branch Q: Sourced Parity Violation — Problem Statement

**Date:** 2026-03-16
**Branch:** Q (minimal parity-violating extension of ECH)
**Prerequisite branches:** A-G (closures), H (parity tensors), N (relics), P (torsion relic), S (photon-torsion vertex)

---

## Why the Minimal Model Failed

The minimal Einstein-Cartan-Holst (ECH) framework with Dirac fermions
on FRW has been comprehensively closed across 15+ barriers spanning
Branches A through S. The barriers fall into three structural classes:

### Class I: No independent torsion dynamics

| Barrier | Branch | Statement |
|---------|--------|-----------|
| 1 | A | Mass-coupling lock: propagating torsion mass tied to Planck scale |
| 2 | B | Topological-shift duality: mass protection and geometric content are mutually exclusive |
| 3 | C | Scalar-tensor universality: after elimination, indistinguishable from generic scalar-tensor |
| 4 | D | Planck suppression: all torsion-mediated effects suppressed by 1/M_Pl^2 |

**Root cause:** Torsion is non-propagating in minimal EC gravity. It satisfies
a constraint equation (algebraic, not dynamical) and is eliminated in terms of
the fermion axial current J^5_mu. There are no independent torsion degrees of
freedom at low energies.

### Class II: No parity-odd observables

| Barrier | Branch | Statement |
|---------|--------|-----------|
| 8 | H | (J^5)^2 is parity-EVEN despite arising from parity-odd torsion |
| 9 | S | ABJ anomaly is universal, Planck-suppressed, requires n_5 != 0 |
| 14 | P | Z_2 symmetry protects pseudoscalar torsion vacuum: S_0 = 0 is a fixed point |

**Root cause:** The four-fermion interaction (J^5)^2 is the product of two
pseudovectors, giving a scalar (parity-even). This is the ONLY non-standard
term in the torsion-eliminated effective action. It cannot source parity-odd
observables (birefringence, chiral GWs, TB/EB correlations). The ABJ anomaly
triangle exists but is 28+ orders too weak and requires a cosmological chiral
density that does not exist.

### Class III: No observable imprint of the bounce

| Barrier | Branch | Statement |
|---------|--------|-----------|
| 5 | E/H | Scale separation: bounce at Planck density, observables at 10^{-122} |
| 6 | F | Attractor-sensitivity dilemma |
| 7 | G | Parameter immunity |
| 12 | M | Vacuum amplification ceiling |
| 13 | N | Gravitational democracy at T ~ M_Pl |

**Root cause:** The bounce is a brief Planck-scale event on an isotropic
background. Its imprint on any late-time observable is diluted by 60+ e-folds
of expansion, overwhelmed by generic gravitational effects at the Planck scale,
and erased by attractor dynamics in the post-bounce evolution.

---

## The Master Obstructions

Two structural facts underpin most of the barriers:

1. **Torsion is non-propagating** (constraint equation, not wave equation).
   This prevents independent torsion dynamics and forces all effects through
   the (J^5)^2 contact interaction.

2. **(J^5)^2 is parity-EVEN.** This kills all parity-odd observables within
   the minimal framework. The Holst term and Barbero-Immirzi parameter are
   parity-odd in the action, but their observable consequences are parity-even
   after torsion elimination.

A successful extension must break at least one of these two obstructions.

---

## What Would Fix This

### Option A: Make torsion propagating

Add kinetic terms for torsion (PGT-type extension). This has been explored
in Branches L, M, P and faces the mass-coupling lock (Barrier 1): the torsion
mass is tied to the Planck scale unless fine-tuned. The PGT program found
a viable GW channel (Branch M) but it is GENERIC (any massive spin-2 field
produces similar GW backgrounds) and the torsion relic program is closed
(Branch P: Z_2 symmetry prevents population).

### Option B: Introduce a parity-odd source

Add a new ingredient that generates parity-odd effective operators. The
minimal such ingredient would be a pseudoscalar field phi coupled to
geometry in a way that produces phi F F-tilde (photon birefringence) or
phi R R-tilde (chiral gravitational waves). The key question: can this
be done in a way that is GEOMETRICALLY MOTIVATED from the ECH framework
rather than purely ad hoc?

### Option C: Both

A propagating pseudoscalar torsion mode with explicit parity-breaking
couplings. Most general but most ad hoc.

---

## What Counts as Success

A successful extension must satisfy ALL of the following:

1. **Minimal new content:** At most ONE new term in the action, ONE new
   coupling constant, ONE new field (or promotion of an existing parameter
   to a field).

2. **Geometric motivation:** The new ingredient should be traceable to the
   ECH structure (Holst term, Barbero-Immirzi parameter, Nieh-Yan identity,
   torsion decomposition) rather than being an arbitrary addition.

3. **Specific observable:** The extension must produce at least one specific,
   quantitative prediction for an observable quantity (birefringence angle,
   chiral GW amplitude, EB correlation, etc.).

4. **Not already excluded:** The prediction must be consistent with existing
   data (Planck, ACT, LiteBIRD projections, LIGO/Virgo/KAGRA, etc.).

5. **Not generic:** The prediction must be DISTINCTIVE to the ECH origin.
   "Any ALP can do this" is not a successful extension. There must be at
   least one relation, correlation, or constraint that comes specifically
   from the geometric embedding.

6. **Tractable first calculation:** The first quantitative result must be
   obtainable analytically or with existing numerical infrastructure
   (Cobaya + CAMB MCMC, already deployed with 300K+ chains).

### What counts as an honest negative result

If the best available extension turns out to be "standard ALP phenomenology
with no ECH-specific content," that is a valid outcome. It means:
- The ECH framework does not produce distinctive parity-odd observables
- The project pivots to generic ALP phenomenology (reusing MCMC infrastructure)
- Paper 2 becomes an ALP constraints paper rather than an ECH predictions paper

This is useful and publishable, but should be stated honestly.

---

## Specific Barriers Each Extension Must Defeat

| Barrier | What must be overcome | Which extensions address it |
|---------|----------------------|---------------------------|
| (J^5)^2 parity-even | Need parity-ODD operator | C (dynamical Immirzi), A (CS), D (phi FF-tilde) |
| n_5 = 0 cosmologically | Need phi-dot != 0 instead | C, B, D (all use pseudoscalar VEV) |
| Planck suppression | Need coupling ~ 1/f_a not 1/M_Pl^2 | B, D (free f_a), C (need to check) |
| ABJ universality | Need ECH-specific operator | C (Nieh-Yan vertex), A (gravitational CS) |
| Z_2 vacuum protection | Need phi != 0 naturally | C (if phi = dynamical gamma, can have VEV from potential) |

The critical question: **Does Candidate C (dynamical Immirzi / torsion-axion
mixing) produce a coupling strength that can explain beta ~ 0.35 degrees
with f_phi at accessible scales (not Planck-suppressed)?**

---

## Scope of This Analysis

This document (Branch Q Phase 1) assesses 5+ candidate extensions at the
order-of-magnitude level. The goal is to identify ONE best candidate for
detailed calculation, or to determine that no ECH-specific extension exists
and the project should pivot to generic ALP phenomenology.

Files in this analysis:
- 01_problem_statement.md (this file)
- 02_candidate_extensions.md
- 03_observable_targets.md
- 04_oom_screening.md
- 05_best_model.md
- phase1_results.md
