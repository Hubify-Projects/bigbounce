# Phase 2: Priors and Parameter Ranges

**Date:** 2026-03-16
**Branch:** R Phase 2

---

## 1. Minimal Model Priors (Models 2 & 3)

Two new ALP parameters beyond standard LCDM:

### theta_i -- Initial misalignment angle

| Property | Value |
|----------|-------|
| Prior | Uniform |
| Range | [0.01, pi] |
| Reference value | 1.0 |
| Proposal width | 0.3 |
| LaTeX | \theta_i |

**Physical motivation:**
- theta_i is set during inflation as a random phase across the potential
- The range [0, pi] covers the full physical range (theta_i and 2pi - theta_i are related by symmetry of the cosine potential)
- O(1) values are "natural" -- no alignment mechanism required
- theta_i = 0 gives no birefringence (trivial); theta_i = pi is the hilltop (unstable, leads to domain walls in realistic multi-field models)
- Lower cutoff at 0.01 avoids numerical issues at theta_i = 0

**Why not [0, 2 pi]?** The cosine potential V = m^2 f_a^2 (1 - cos theta) is symmetric about theta = pi. Fields with theta_i and 2 pi - theta_i produce opposite-sign birefringence. Since we observe beta > 0, we restrict to [0, pi] by convention (the sign of beta determines which branch).

### log10(m_a / eV) -- ALP mass

| Property | Value |
|----------|-------|
| Prior | Uniform |
| Range | [-35, -30] |
| Reference value | -32.8 |
| Proposal width | 0.5 |
| LaTeX | \log_{10}(m_a/\mathrm{eV}) |

**Physical motivation:**
- H_0 ~ 1.4 x 10^{-33} eV, so log10(H_0/eV) ~ -32.85
- The "sweet spot" for birefringence is m ~ H_0 (field rolls between recombination and today)
- m < 0.01 H_0 (log10 < -35): field still frozen, no birefringence
- m > 100 H_0 (log10 > -31): field oscillates many times, birefringence washes out
- The range [-35, -30] covers the physically interesting window with margin

## 2. Extended Model Priors (Phase 2b)

Four ALP parameters:

### log10(f_a / GeV) -- Decay constant

| Property | Value |
|----------|-------|
| Prior | Uniform |
| Range | [16, 19] |
| Reference value | 18.39 (M_Pl) |
| Proposal width | 0.5 |
| LaTeX | \log_{10}(f_a/\mathrm{GeV}) |

**Physical motivation:**
- f_a = M_Pl is the canonical scale for gravitational ALPs (string axiverse, ECH)
- f_a > M_Pl: may violate Weak Gravity Conjecture (but not definitively excluded)
- f_a < 10^{16} GeV: isocurvature constraints become relevant for high-scale inflation
- For m ~ H_0 regime: beta is independent of f_a (the f_a in g_{a gamma} cancels the f_a in Delta_phi), so the posterior on f_a should be flat (unconstrained by birefringence alone)
- f_a becomes constrained only through the DE density: Omega_a propto f_a^2

### C_{a gamma} -- Anomaly coefficient

| Property | Value |
|----------|-------|
| Prior | Uniform |
| Range | [4, 16] |
| Reference value | 8 (SM) |
| Proposal width | 1.0 |
| LaTeX | C_{a\gamma} |

**Physical motivation:**
- C_{a gamma} = 8 for the SM with universal PQ charge (KSVZ-like convention)
- C_{a gamma} < 8: possible if not all SM fermions carry PQ charge, or in DFSZ-like models where there are cancellations from multiple Higgs doublets
- C_{a gamma} > 8: if there are additional charged fermions in a dark/hidden sector
- The lower bound of 4 corresponds roughly to leptons-only coupling
- The upper bound of 16 allows generous BSM contributions
- Note: C_{a gamma} x theta_i is degenerate in beta. Breaking this requires independent information about C_{a gamma} (from particle physics model) or theta_i (from ALP dark energy density)

## 3. Focused Prior Set (Recommended for Phase 2a)

For the fastest first pass, fix the well-motivated parameters:

| Parameter | Value | Justification |
|-----------|-------|---------------|
| f_a | M_Pl = 2.435 x 10^{18} GeV | Canonical for gravitational ALP |
| C_{a gamma} | 8 | SM fermion content |
| theta_i | sampled, [0.01, pi] | Only free "amplitude" |
| log10(m_a/eV) | sampled, [-35, -30] | Controls rolling dynamics |

This is the **minimal 2-parameter extension** of LCDM for ALP birefringence.

## 4. Standard LCDM Priors

Identical to the existing Paper 1 pipeline:

| Parameter | Prior | Range | Reference | Proposal |
|-----------|-------|-------|-----------|----------|
| omega_b h^2 | Uniform | [0.005, 0.1] | N(0.02237, 0.00015) | 0.0001 |
| omega_c h^2 | Uniform | [0.001, 0.99] | N(0.1200, 0.0012) | 0.0005 |
| 100 theta_MC | Uniform | [0.5, 10] | N(1.04092, 0.00031) | 0.0002 |
| tau | Uniform | [0.01, 0.8] | N(0.054, 0.007) | 0.003 |
| log(10^{10} A_s) | Uniform | [1.61, 3.91] | N(3.044, 0.014) | 0.001 |
| n_s | Uniform | [0.8, 1.2] | N(0.9649, 0.0042) | 0.002 |

## 5. Physically Motivated Constraints on Priors

### Energy density bound

$$\rho_a = m^2 f_a^2 (1 - \cos\theta_i) \leq \rho_{\rm crit}$$

For f_a = M_Pl:

$$(m/H_0)^2 \times (1 - \cos\theta_i) \leq 3$$

This carves out a region in (m, theta_i) space:
- For theta_i = 1: m < 2.0 H_0 (log10(m/eV) < -32.5)
- For theta_i = pi: m < 0.87 H_0 (log10(m/eV) < -32.9)
- For theta_i = 0.5: m < 3.7 H_0 (log10(m/eV) < -32.3)

**Implementation:** Either as a hard prior cut or as a steep penalty in the likelihood. Hard cut is simpler and recommended.

### Model 3 specific: Omega_a ~ 0.68

For Model 3 (ALP-as-DE), we need the ALP to contribute the right amount of dark energy. This is not a separate prior -- it is automatically enforced by the Planck + BAO likelihoods, which constrain the expansion history.

However, as a diagnostic, we can compute:

$$\Omega_a = \frac{(m/H_0)^2 (1 - \cos\theta_i)}{3}$$

and flag points where Omega_a is far from 0.68. In Model 3, Lambda is removed, so the total energy budget must close: Omega_m + Omega_r + Omega_a = 1.

### Weak Gravity Conjecture

The WGC suggests f_a < M_Pl for consistent quantum gravity. This is automatically respected by our prior range upper limit of 10^{19} GeV ~ 4 M_Pl.

Some versions of the WGC are stronger (e.g., f_a << M_Pl), which would conflict with our fiducial value. We note this as a theoretical uncertainty but do not impose it as a prior.

## 6. Prior Sensitivity Tests

Run MCMC with three prior choices to assess robustness:

| Test | theta_i prior | m prior | f_a | C_{a gamma} |
|------|-------------|---------|-----|-------------|
| Baseline | U[0.01, pi] | U[-35, -30] | M_Pl | 8 |
| Narrow mass | U[0.01, pi] | U[-33.5, -32] | M_Pl | 8 |
| Wide C_{a gamma} | U[0.01, pi] | U[-35, -30] | M_Pl | U[4, 16] |

Compare posteriors and Bayes factors. If results are prior-dominated (rather than data-dominated), report this prominently.

## 7. Expected Degeneracies

### Exact: C_{a gamma} x theta_i (for fixed m ~ H_0)

beta = C_{a gamma} alpha theta_i eta / (4 pi). For m in the sweet spot where eta ~ const, beta depends only on the product C_{a gamma} theta_i. The posterior in the (C_{a gamma}, theta_i) plane will show a hyperbolic degeneracy band.

**Breaking mechanism:** Varying C_{a gamma} requires varying f_a to keep g_{a gamma} physical, which changes Omega_a. The DE density constraint can in principle break the degeneracy. But for Model 2 (spectator), there is no breaking.

### Approximate: theta_i vs m (through eta)

For m << H_0: eta -> 0, so larger theta_i is needed to compensate.
For m >> H_0: eta -> 0 (oscillation), so no compensation works.

The viable region forms a band in (theta_i, m) space, curved due to the nonlinear eta(m/H_0).

### Flat direction: f_a (in extended model)

f_a drops out of beta (for m ~ H_0). The posterior on f_a will be flat unless the DE density constraint is active. This is a feature (UV insensitivity), not a bug.
