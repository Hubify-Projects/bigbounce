# S1 Phase 1 — Assessment Checklist

**Purpose:** Determine in ≤1 week whether S1 has a defensible theory-to-observable mapping
**Output:** 1-page mapping memo answering 4 questions
**Decision:** If any of Q1–Q3 is "no," S1 closes at Phase 1

---

## Q1: What exact observable does the framework predict?

### What to determine
- [ ] Does the parity-odd operator ε^{abcd} K_{ab} R_{cd} couple to photon polarization at all in the minimal framework?
- [ ] If yes: through what coupling? (Direct torsion-photon? Chern-Simons F∧F? Effective axion-photon from Nieh-Yan?)
- [ ] If no: what is the MINIMAL extension that produces photon-polarization rotation?
- [ ] Is this extension theoretically motivated or purely phenomenological?

### Sources to check
- Mercuri (2009) §III: does the Immirzi field couple to F∧F?
- Alexander & Yunes (2009) §IV: Chern-Simons birefringence mechanism
- Main paper Sec. III.B.2 (birefringence discussion): what exactly is claimed vs assumed?

### Kill criterion
If the minimal framework has NO photon coupling and the required extension is arbitrary (i.e., "just add a coupling constant"), then S1 reduces to generic ALP birefringence phenomenology with no spin-torsion content. **Gate S1-1 fails.**

### Survival criterion
If there is a SPECIFIC coupling that arises naturally from the Holst/torsion sector (e.g., the Nieh-Yan term coupling to the photon sector through a definite mechanism), then the mapping is defensible.

---

## Q2: What exact parameterization results?

### What to determine
- [ ] Write down the explicit formula: β = f(α/M, f_photon, z, ℓ, ...)
- [ ] How many free parameters does the mapping introduce? (Must be ≤ 2 to be sharp)
- [ ] Is β predicted to be uniform (constant across ℓ) or scale-dependent?
- [ ] If scale-dependent: what sets the shape? The inflationary dilution history?

### The critical sub-question
- [ ] Does the framework predict a SPECIFIC β(ℓ) shape that differs from constant rotation?

If yes → S1 has distinguishing power (proceed to Q3).
If no → S1 reduces to "our framework is consistent with observed β for f_photon ~ O(1)." This is a consistency check, not a prediction. Still potentially publishable but much weaker.

### What to write in the memo
- Explicit β formula with all parameters identified
- Classification: each parameter is {derived, assumed, fit, missing}
- Number of genuinely free parameters after framework constraints

---

## Q3: Is this distinguishable from generic birefringence?

### What to determine
- [ ] List the 3 leading alternative birefringence mechanisms:
  1. Axion-like particle with constant coupling (constant β)
  2. Early dark energy with parity violation (β ∝ ℓ-dependent)
  3. Primordial magnetic fields (anisotropic, not isotropic β)
- [ ] For each: does the spin-torsion prediction differ in spectral shape, amplitude scaling, or ℓ-dependence?
- [ ] If the spin-torsion prediction is identical to mechanism 1 (constant β): is there ANY distinguishing feature?

### Kill criterion
If the prediction is exactly constant β with one free amplitude → indistinguishable from generic ALP birefringence → S1 has no distinctive content beyond "our framework is one of many that can produce this."

### Survival criteria (any one suffices)
- The dilution mechanism produces a specific β(ℓ) shape ≠ constant
- The framework predicts a specific relationship between β and another observable (e.g., ΔN_eff, or the galaxy spin amplitude)
- The framework predicts a specific sign or magnitude constraint on β from its other fitted parameters

---

## Q4: Can current data test this meaningfully?

### What to determine
- [ ] What is the current best measurement? (Combined β = 0.242° ± 0.061°, 3.9σ from Planck+ACT)
- [ ] What EB/TB bandpower data is publicly available?
- [ ] Can the constraint be implemented with existing likelihood codes (no custom map analysis)?
- [ ] Is the framework's predicted signal in the regime where data has sensitivity?

### Sources to check
- Diego-Palazuelos & Komatsu (2025): ACT DR6 birefringence methodology
- Planck NPIPE data products: what is publicly available?
- Cobaya/CosmoMC: any existing birefringence likelihood module?

### Assessment
- [ ] Estimate: how long would the pipeline work take? (Days? Weeks?)
- [ ] Is this a standard analysis or does it require custom development?

---

## Memo Template

After completing Q1–Q4, write a 1-page memo with this structure:

```
S1 MAPPING MEMO — [date]

OBSERVABLE: [exact quantity]
FORMULA: β = [explicit formula]
FREE PARAMETERS: [list with status: derived/assumed/fit/missing]
DISTINGUISHING POWER: [yes/no, with specific reason]
DATA AVAILABILITY: [what exists, what's needed]
PIPELINE EFFORT: [estimate]

VERDICT: [Gate S1-1 PASS / FAIL]
REASONING: [2-3 sentences]
RECOMMENDED NEXT STEP: [if PASS: what specifically to do next]
```

---

## Timeline

| Day | Task |
|-----|------|
| 1 | Read main paper birefringence section + Mercuri 2009 |
| 2 | Read Diego-Palazuelos+2025 + Eskilt+Komatsu 2022 |
| 3 | Answer Q1 and Q2 |
| 4 | Answer Q3 and Q4 |
| 5 | Write mapping memo + Gate S1-1 verdict |

---

## What NOT to do in Phase 1

- Do NOT start writing pipeline code
- Do NOT run any MCMC
- Do NOT modify CAMB or any Boltzmann code
- Do NOT draft a paper abstract
- Do NOT assume the mapping works — test it first
