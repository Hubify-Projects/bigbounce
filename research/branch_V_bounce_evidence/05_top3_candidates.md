# Branch V: Top 3 Candidate Programs

**Created:** 2026-03-17

---

## Candidate 1: Matter Bounce through ECH (V2a)

### The Idea
A universe that contracts in a dust-dominated (w = 0) phase, reaches ρ_crit ≈ 0.21 M_Pl⁴, undergoes a non-singular ECH bounce, then expands into the standard hot Big Bang. The contracting dust epoch generates the primordial perturbation spectrum; the ECH bounce provides the non-singular transition.

### Exact Questions to Answer
1. **Does a dust-dominated contraction + ECH bounce produce n_s = 0.965 ± 0.004?** Pure matter bounce gives n_s = 1 (Harrison-Zel'dovich), which is 8σ from Planck. We need to compute the correction from (a) finite bounce duration, (b) transition from dust to radiation near the bounce, and (c) possible entropy production. The question is whether the red tilt Δn_s ≈ -0.035 emerges naturally.

2. **What is the exact non-Gaussianity prediction?** The leading-order result f_NL^local = 5/12 is established for a symmetric matter bounce. How does the ECH bounce modify this? What are the higher-order corrections from torsion?

3. **What is the low-ℓ power deficit prediction?** If the contracting phase has finite duration T_contraction, there is a maximum mode that can be generated: k_min ~ 1/(c_s T_contraction). Modes with k < k_min are suppressed. Does this naturally explain the Planck low-ℓ anomaly?

4. **What is the tensor-to-scalar ratio and tensor tilt?** The matter bounce gives r ~ 0.01–0.1 and n_T = 0. Are these within LiteBIRD's sensitivity?

### Observables and Their Targets

| Observable | Prediction | Current Data | Next-Gen Sensitivity | Status |
|-----------|-----------|-------------|---------------------|--------|
| n_s | ~1 (needs red tilt mechanism) | 0.965 ± 0.004 | ±0.002 (CMB-S4) | **CRITICAL TEST** |
| f_NL^local | 5/12 ≈ 1.25 | -0.9 ± 5.1 (Planck) | ±0.5 (SPHEREx) | Testable |
| r | ~0.01–0.1 | < 0.036 (BICEP3) | ~10⁻³ (LiteBIRD) | Testable |
| n_T | ~0 | Unconstrained | Measurable if r > 0.01 | Testable |
| Low-ℓ TT deficit | Depends on T_contraction | 2–3σ anomaly (Planck) | Limited by cosmic variance | Qualitative match |
| Consistency relation | r = 16c_s n_T (NOT r = -8n_T) | Unconstrained | CMB-S4 + LiteBIRD | **SMOKING GUN** |

### First Calculation
**Compute the scalar power spectrum P(k) and f_NL for a dust contraction → ECH bounce → radiation expansion.** This requires:
1. Setting up the Mukhanov-Sasaki equation with background a(t) that transitions from dust contraction to ECH bounce to radiation expansion
2. Numerically integrating mode functions through the bounce
3. Extracting P(k), n_s, r, n_T from the Bogoliubov coefficients
4. Computing the bispectrum at leading order

### Known Challenges
- **n_s problem**: Pure matter bounce gives n_s = 1. Getting n_s = 0.965 may require a specific transition profile or additional physics. This is the make-or-break test.
- **Anisotropy instability**: Dust contraction is BKL-unstable. ECH doesn't cure this. Need to argue that anisotropy growth is slow enough (number of e-folds of contraction is finite).
- **Transition dynamics**: How does the universe transition from dust to radiation? Need a specific reheating/thermalization mechanism.

### Why ECH Adds Value
Standard matter bounce models need an *ad hoc* non-singular bounce mechanism (often hand-waved as "quantum gravity effects"). ECH provides an explicit, calculable bounce with known critical density, known duration, and known mode-coupling structure. This is a genuine advance.

---

## Candidate 2: ECH-Resolved Ekpyrotic Bounce (V4)

### The Idea
Ekpyrotic cosmology is the leading competitor to inflation, but its Achilles' heel has always been the singular bounce (or "Big Crunch → Big Bang" transition). ECH provides a clean resolution: the ekpyrotic contraction drives ρ → ρ_crit, where torsion kicks in and produces a non-singular bounce.

### Exact Questions to Answer
1. **Can the ekpyrotic entropy mechanism operate through an ECH bounce?** The entropy mechanism converts isocurvature perturbations to curvature perturbations during the bounce. This conversion is sensitive to the bounce dynamics. Does the ECH bounce preserve the entropy-to-curvature transfer?

2. **What is the ekpyrotic non-Gaussianity f_NL^equil after ECH bounce?** Standard ekpyrotic gives f_NL ~ -c²/8. Does the ECH bounce modify this?

3. **Does ECH naturally isotropize during ekpyrotic contraction?** Ekpyrotic contraction isotropizes the universe (anisotropy dies as a⁻⁶ while ekpyrotic energy grows as a⁻(3+3/w)). Does the ECH bounce preserve this isotropization?

4. **What is the combined (r, f_NL, n_s) prediction?** The three-observable space (r, f_NL, n_s) is the key discriminator between inflation, matter bounce, and ekpyrotic.

### Observables

| Observable | Prediction | Distinctiveness |
|-----------|-----------|----------------|
| r | ≈ 0 (< 10⁻¹⁰) | Decisive vs inflation (where r > 10⁻³ for most models) |
| f_NL^equil | ~ -10 to -50 (for c = 8–20) | Large negative equilateral; inflation predicts |f_NL| < 1 |
| n_s | 1 - 2/c² ≈ 0.97–0.98 | Consistent with Planck; fixes the matter bounce n_s = 1 problem |
| n_T | Very negative (suppressed tensors) | Opposite to inflation's n_T < 0 with moderate r |

### First Calculation
**Compute the entropy-to-curvature conversion efficiency through an ECH bounce for a two-field ekpyrotic model.**

### Known Challenges
- **Two-field requirement**: Entropy mechanism needs at least two fields with specific potential. This adds parameters.
- **c-dependence**: Many predictions depend on the ekpyrotic slope c, which is a free parameter.
- **Motivation for steep potential**: Why does V(φ) ∝ e^{-cφ/M_Pl} with c ≫ 1 exist?

### Why ECH Adds Value
This is where ECH adds the MOST value. The singular bounce is the single biggest criticism of ekpyrotic cosmology. If ECH resolves it cleanly, this is a genuine theoretical contribution. The combination "ekpyrotic contraction + ECH bounce" could be a complete alternative to inflation.

---

## Candidate 3: Kinetic Bounce with Blue Tensor Tilt (V2c)

### The Idea
A contraction dominated by a free scalar field (w = 1, "kinetic contraction") followed by an ECH bounce. This produces a strongly blue-tilted tensor spectrum (n_T = 2) — the single most distinctive prediction of any bouncing cosmology.

### Exact Questions to Answer
1. **What is the GW spectrum Ω_GW(f) for kinetic contraction + ECH bounce?** The blue tilt n_T = 2 means the spectrum rises with frequency. At what frequency does it peak? What is the amplitude at LISA/DECIGO/LIGO frequencies?

2. **Can the blue tensor spectrum explain the NANOGrav signal?** If the spectrum peaks near nHz, it could contribute to the stochastic GW background seen by pulsar timing arrays.

3. **What constrains the scalar spectrum?** Kinetic contraction gives n_s = 3 (strongly blue, ruled out). How can the scalar spectrum be modified independently of the tensor spectrum?

4. **What is the tensor-to-scalar consistency relation?** For w = 1 contraction, the consistency relation is r = 24(1 - n_s)/5, completely different from inflation's r = -8n_T.

### Observables

| Observable | Prediction | Distinctiveness |
|-----------|-----------|----------------|
| n_T | 2 (strongly blue) | UNIQUE to w = 1 bounce; inflation gives n_T < 0 |
| Ω_GW(f) | Rising ∝ f² | Direct detection target for LISA/DECIGO |
| n_s | 3 (ruled out without modification) | **FATAL unless modified** |
| r | Depends on normalization | Could be large |

### First Calculation
**Compute Ω_GW(f) for kinetic contraction + ECH bounce across all detector bands.**

### Known Challenges
- **n_s = 3 problem**: The scalar spectrum is completely wrong without an additional mechanism. This is a showstopper unless we add a second field or a different mechanism for scalar perturbations.
- **Need for hybrid model**: V2c almost certainly requires combining kinetic contraction (for tensors) with another mechanism (curvaton, entropy) for scalars. This adds complexity.

### Why ECH Adds Value
The blue tensor tilt is the most spectacular smoking-gun prediction in all of bouncing cosmology. If the scalar problem can be solved, this is the most falsifiable and distinctive program. ECH provides the non-singular bounce that makes the calculation well-defined.

---

## Comparison of Top 3

| Criterion | V2a (Matter Bounce) | V4 (Ekpyrotic+ECH) | V2c (Kinetic+ECH) |
|-----------|--------------------|--------------------|-------------------|
| Upside score | 71 | 31 | 46 |
| Parameter-free predictions | f_NL = 5/12 | None (depends on c) | n_T = 2 |
| n_s consistency | PROBLEMATIC (n_s = 1) | GOOD (n_s = 1-2/c²) | FATAL (n_s = 3) |
| BKL stability | PROBLEMATIC | RESOLVED by ekpyrosis | MARGINAL |
| ECH-specific content | Bounce mechanism | Bounce resolves singularity | Bounce mechanism |
| Existing data hints | Low-ℓ deficit | None specific | NANOGrav? |
| Falsifiability | f_NL measurement | r + f_NL combination | n_T measurement |
| First calculation difficulty | MODERATE | HARD (two-field) | MODERATE |
| Paper potential | HIGH | VERY HIGH | MODERATE (needs hybrid) |

### Verdict
**V2a has the highest raw upside** but faces the n_s = 1 problem.
**V4 has the highest theoretical impact** (resolves ekpyrotic's biggest weakness) but is harder to compute.
**V2c has the most spectacular single prediction** (n_T = 2) but the scalar sector is broken.

**Recommended primary target: V2a** — it has the most parameter-free predictions, the clearest connection to existing anomalies, and the most manageable first calculation. The n_s problem is actually a *feature*: computing how ECH bounce dynamics shift n_s from 1 to ~0.965 is the key original result.

**Recommended secondary target: V4** — for theoretical impact. Even without a full perturbation calculation, showing that "ECH resolves the ekpyrotic singular bounce" is a publishable result.
