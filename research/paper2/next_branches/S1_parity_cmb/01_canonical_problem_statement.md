# Branch S1 — Canonical Problem Statement: Parity-Sensitive CMB Phenomenology

**Version:** v1 (DRAFT — NOT FROZEN)
**Date:** 2026-03-13
**Status:** Ready for Phase 1 (mapping assessment)
**Prerequisite:** None (signal branch, independent of theory branches)

---

## Motivation

The main paper's framework predicts parity-odd observables through the operator ε^{abcd} K_{ab} R_{cd}. Current observational anchors include:

- **Isotropic cosmic birefringence:** Planck 2.4–2.7σ, ACT DR6 2.9σ, combined SPIDER+Planck+ACT ~7σ
- **ΔN_eff:** MCMC verification shows ΔN_eff ≈ 0 (consistent with SM); not a distinguishing signal
- **Galaxy spin dipole:** Empirical A₀ ~ 0.003 with large theory-observation gap

The ΔN_eff channel is effectively null. The galaxy spin channel has an unsolved order-of-magnitude gap. The CMB parity-odd channels (EB, TB correlations, birefringence spectral shape) are the most theoretically native observables for this framework and are the closest to being testable with existing data.

**This is a signal branch, not a first-principles derivation branch.** It asks: "Given the framework's parity-odd structure, what CMB observables can we constrain or detect?"

---

## The Central Question

> Can the spin-torsion dark energy framework's parity-odd operator structure be mapped to specific CMB parity-odd observables (EB, TB, birefringence angle, spectral shape) in a way that is:
> (a) defensible given the current theory-to-observable mapping,
> (b) testable with existing or near-future CMB data and likelihoods,
> (c) distinguishable from generic parity-violation models?

---

## Target Observables

### Observable 1: EB cross-power spectrum C_ℓ^{EB}
- **Theory mapping:** The parity-odd operator generates a nonzero EB correlation through its coupling to photon polarization. The spectral shape C_ℓ^{EB}(ℓ) depends on the mechanism (uniform rotation vs scale-dependent birefringence).
- **Data availability:** Planck NPIPE, ACT DR6 (publicly available)
- **Current status:** Nonzero detection at ~3σ combined. Main paper cites consistency but does not derive the amplitude.
- **What S1 would do:** Constrain the framework's predicted EB shape against data. Upper bounds or compatibility checks.

### Observable 2: Birefringence rotation angle β
- **Theory mapping:** The parity-odd operator induces a rotation of the CMB polarization plane. β = (α/M) × (path integral of parity-odd field along line of sight).
- **Data availability:** Combined β = 0.242° ± 0.061° (3.9σ) from Planck+ACT
- **Current status:** Main paper shows f_photon × C₀ = 1.73 ± 0.44 is required — O(1) product.
- **What S1 would do:** Assess whether the framework's operator can produce this rotation with natural parameters. This requires specifying the photon-torsion coupling (currently missing from the framework).
- **IMPORTANT CAVEAT:** Without a derived photon-torsion coupling, the framework strictly predicts β = 0. S1 cannot claim a birefringence signal; it can only check consistency IF the coupling is added.

### Observable 3: TB cross-power spectrum C_ℓ^{TB}
- **Theory mapping:** Parity-odd birefringence also rotates E into B, producing nonzero TB.
- **Data availability:** Same as EB (derived from same maps)
- **Current status:** Less constraining than EB but provides independent check
- **What S1 would do:** Joint EB+TB consistency check

### Observable 4: Scale-dependent birefringence β(ℓ)
- **Theory mapping:** If the parity-odd operator has a non-trivial scale dependence (e.g., from the evolution of the spin density during inflation), β could be ℓ-dependent rather than uniform.
- **Data availability:** Currently consistent with uniform β; constraints on scale dependence are weak
- **What S1 would do:** Derive the expected β(ℓ) shape from the framework's dilution mechanism and compare with data

---

## What Is Derived vs Assumed vs Missing

| Element | Status |
|---------|--------|
| Parity-odd operator structure | **Derived** in main paper |
| Inflationary dilution scaling | **Derived** in main paper |
| Photon-torsion coupling | **MISSING** — not in the minimal framework |
| β amplitude | **Cannot be derived** without photon-torsion coupling |
| EB spectral shape | **Partially derivable** from dilution + photon coupling model |
| ΔN_eff | **Already tested** — null result |

---

## Gate Structure

### Gate S1-1: Defensible theory-to-observable mapping
There exists a mapping from the framework's parity-odd operator to at least one CMB parity-odd observable that:
- is physically motivated (not arbitrary parameterization),
- has clearly stated assumptions,
- produces a specific prediction or constraint that is not trivially degenerate with other parameters.

**Kill criterion:** If no defensible mapping exists without introducing an arbitrary photon-torsion coupling, Gate S1-1 fails. The branch reduces to "add coupling, fit data" — which is just generic phenomenology with no spin-torsion content.

**Important nuance:** A consistency check (showing the framework is COMPATIBLE with observed birefringence for natural coupling values) may survive Gate S1-1 even if a detection claim does not. The bar for a consistency check is lower than for a prediction.

### Gate S1-2: Clean data constraint
The observable from Gate S1-1 can be constrained with existing public data and likelihood codes (Planck NPIPE, ACT DR6) without requiring custom pipeline development beyond minor modifications.

**Kill criterion:** If the constraint requires a new end-to-end CMB analysis pipeline (map-level analysis, custom foreground subtraction), Gate S1-2 fails. S1 should use published summary statistics, not raw maps.

### Gate S1-3: Nonzero allowed/preferred region or informative bound
The data either:
- prefer a nonzero signal consistent with the framework (weak preference OK), OR
- place an informative upper bound that constrains the framework's parameters, OR
- exclude the framework's natural parameter range.

Any of these three outcomes is a publishable result. Only a completely unconstraining bound (no information gained) fails Gate S1-3.

---

## Predeclared Failure Modes

| Code | Failure mode | Description |
|------|-------------|-------------|
| FM-S1-1 | No defensible mapping | Cannot connect framework operator to CMB observable without arbitrary coupling |
| FM-S1-2 | Degenerate with generic models | Framework prediction is identical to generic constant-β birefringence; no distinguishing power |
| FM-S1-3 | Pipeline barrier | Constraint requires custom CMB analysis beyond available tools |
| FM-S1-4 | Known systematics territory | Predicted signal amplitude falls in the regime dominated by instrumental systematics |
| FM-S1-5 | Already done | Existing papers have already performed this exact analysis |

---

## Computation Sequence

### Phase 1: Mapping Assessment (1 week)
**No computation — pure assessment.**

| Step | Task | Output |
|------|------|--------|
| 1.1 | Review existing birefringence-from-torsion literature | Assessment notes |
| 1.2 | Identify the minimal photon-torsion coupling model | Explicit Lagrangian term |
| 1.3 | Derive β in terms of framework parameters | Formula |
| 1.4 | Assess Gate S1-1 | Go/no-go |
| 1.5 | If S1-1 survives: assess available data/likelihoods | Pipeline plan |

**Deliverable:** `notes/S1_mapping_assessment.md`

### Phase 2: Pipeline and Constraint (2–3 weeks, conditional on S1-1)

| Step | Task | Output |
|------|------|--------|
| 2.1 | Implement birefringence likelihood (Planck + ACT combined) | Python script |
| 2.2 | Derive EB spectral shape for framework's parity-odd operator | C_ℓ^{EB} template |
| 2.3 | Run constraint analysis | Posterior on (α/M) × f_photon |
| 2.4 | Test Gate S1-2 | Data constraint verdict |

**Deliverable:** `derivations/S1_birefringence_constraint.py`

### Phase 3: Results and Interpretation (1 week, conditional on S1-2)

| Step | Task | Output |
|------|------|--------|
| 3.1 | Interpret constraint within framework | Parameter bounds |
| 3.2 | Compare with generic birefringence models | Distinguishing power assessment |
| 3.3 | Test Gate S1-3 | Final verdict |
| 3.4 | Draft results section | Publishable text |

---

## Expected Figures / Tables

| Figure | Description |
|--------|-------------|
| S1_birefringence_constraint | Posterior on f_photon × C₀ or equivalent |
| S1_EB_spectral_shape | Predicted vs observed C_ℓ^{EB} (if distinguishable from uniform rotation) |
| S1_parameter_space | Allowed region in (α/M, f_photon) plane |

---

## Datasets and Tools

| Resource | Purpose | Availability |
|----------|---------|-------------|
| Planck NPIPE EB/TB bandpowers | Primary constraint data | Public (PLA) |
| ACT DR6 birefringence posterior | Combined constraint | Published in Diego-Palazuelos+2025 |
| Cobaya v3.6.1 | MCMC framework | Already installed |
| CAMB | Boltzmann code for C_ℓ templates | Already installed |
| healpy | Map manipulation (only if map-level analysis needed) | pip install |

---

## Honest Assessment

The most likely outcome of S1 is a **consistency check** showing that the framework's parity-odd operator is compatible with observed birefringence for natural values of the photon-torsion coupling (f_photon ~ O(1)). This is a modest but publishable result.

A **detection claim** is unlikely because the framework does not derive the photon-torsion coupling — it can only show compatibility once the coupling is introduced.

A **null result** (no defensible mapping) is also possible and would be documented as part of the framework's limitation inventory.

The strongest publishable outcome would be showing that the framework's EB spectral shape (if it differs from uniform rotation) is preferred over generic constant-β birefringence. This requires the dilution mechanism to produce a specific ℓ-dependence in β, which is an open question.
