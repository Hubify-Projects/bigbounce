# Track C -- Parity/CMB Observable Model: Model-to-Observable Map

**Date:** 2026-03-12
**Status:** CONSTRAINT ANALYSIS (Gaussian sampling) + FORWARD MODEL
**Readiness:** Ready for implementation with published data

---

## 1. Parameter Definitions

### 1.1 Minimal Parameter Set

| Symbol | Name | Status | Prior / Range |
|--------|------|--------|---------------|
| `beta_iso` | Isotropic birefringence angle | **Directly measurable** | Gaussian: published measurements |
| `alpha_over_M` | Parity-odd coefficient | Phenomenological (one-loop motivated) | Log-uniform [10^{-40}, 10^{-20}] GeV^{-1} |
| `f_photon` | Photon-torsion vertex factor | **Unknown (not derived)** | Dimensionless; log-uniform [10^{-6}, 1] |
| `g_eff` | Effective parity-odd coupling to photons | Composite: g_eff = (alpha/M) * f_photon | Derived |
| `Delta_phi_over_2f` | Net pseudo-scalar field excursion / (2 * decay constant) | Proxy for beta | Derived |
| `A_aniso` | Anisotropic birefringence amplitude at low-ell | **Optional; not derivable from framework** | Uniform [0, 10^{-2}] rad |

### 1.2 Ancillary Parameters (from parent paper, not re-fit here)

| Symbol | Value | Role in this track |
|--------|-------|-------------------|
| [(alpha/M) * M_Pl] | ~10^{-2} | Dimensionless one-loop suppression factor |
| Xi | ~10^{-123} | Sets dark energy scale; not directly relevant to birefringence |
| D_inf | ~10^{-121} | Inflationary dilution; not directly relevant to birefringence |
| gamma | 0.274 | Barbero-Immirzi parameter (enters M = M_{area-gap}) |

---

## 2. Equation Chain: From Theory to Observables

### Step 1: Parity-Odd Operator (DERIVED in paper)

The effective action (Eq. 4 of paper):

    S_eff = (alpha/M) integral[ e_I wedge e_J wedge F^{IJ}[K, R-ring] ]

This operator is parity-odd, diffeomorphism-covariant, generated at one loop. The coefficient:

    (alpha/M) ~ (g^2 / 32 pi^2) * (gamma / M) * ln(Lambda_UV^2 / mu^2) + delta_NY

Best-fit: alpha/M ~ 10^{-21} GeV^{-1}, giving [(alpha/M) * M_Pl] ~ 10^{-2}.

**Epistemic status:** The operator exists and its order of magnitude is one-loop motivated. The exact value is a phenomenological parameter fit to data. This step is on solid ground.

### Step 2: Photon-Torsion Coupling (NOT DERIVED -- the gap)

For the parity-odd gravitational operator to rotate photon polarization, one needs an effective coupling between the spin-torsion sector and the electromagnetic field. The paper acknowledges this explicitly (Sec. V.A):

    L superset phi(tau) / (4f) * F_{mu nu} * F-tilde^{mu nu}

where phi is a pseudo-scalar sourced by the spin-torsion sector and f is the associated decay constant.

**What is missing:** The one-loop computation of the photon-torsion vertex that would yield phi and f from the operator (alpha/M) * epsilon^{abcd} K_{ab} R_{cd}. This is the key theoretical gap.

We parameterize this gap with a single dimensionless factor:

    f_photon = (effective photon-torsion vertex strength)

such that the net pseudo-scalar excursion is:

    Delta_phi / (2f) = f_photon * (alpha/M) * Lambda_eff

where Lambda_eff is the effective energy scale at which the pseudo-scalar is sourced (of order M_Pl at the bounce, then diluted).

**Epistemic status:** SCALING ANSATZ. The functional form is standard (axion-like coupling), but the coefficient f_photon is entirely undetermined. This is the honest gap.

### Step 3: Birefringence Angle (PHENOMENOLOGICAL PROXY)

For a spatially uniform pseudo-scalar, the standard result (Carroll 1998):

    beta = Delta_phi / (2f)

The paper uses observed beta as a consistency benchmark, not a prediction. We define:

    beta_iso = g_eff * Phi_net

where:
- g_eff = (alpha/M) * f_photon is the effective coupling
- Phi_net encodes the integrated field excursion from last scattering to today

For the consistency window analysis (Section 5 below), the key relation is:

    beta_iso = f_photon * [(alpha/M) * M_Pl] * (M_Pl * Delta_tau_eff)

where Delta_tau_eff absorbs the cosmological evolution. Since [(alpha/M) * M_Pl] ~ 10^{-2} and beta_obs ~ 5 * 10^{-3} rad, this constrains:

    f_photon * (M_Pl * Delta_tau_eff) ~ 0.5

This is a one-parameter family: for any assumed Delta_tau_eff, f_photon is determined by the observed beta.

**Epistemic status:** PHENOMENOLOGICAL PROXY. beta is directly measured; its connection to alpha/M requires the undetermined f_photon.

### Step 4: EB/TB Power Spectra (DERIVED, given beta)

Given beta_iso, the CMB cross-spectra follow from standard rotation algebra (Eq. 18 in paper):

    C_ell^{EB} = sin(4 beta) / 2 * (C_ell^{EE} - C_ell^{BB})
              approx 2 beta * (C_ell^{EE} - C_ell^{BB})    [small-angle]

    C_ell^{TB} approx 2 beta * C_ell^{TE}

These are exact results for uniform rotation -- no model dependence beyond the value of beta. The shape is entirely determined by the unlensed EE, BB, and TE spectra.

**Epistemic status:** DERIVED (standard CMB physics). The only input is beta; the spectral shape is a firm prediction.

### Step 5: Anisotropic Component (QUALITATIVE ONLY)

The cosmic rotation axis defines a preferred direction n-hat, introducing anisotropic birefringence beta(n-hat) with power at low multipoles. The paper states:

- Axion models: scale-invariant power in beta(n-hat)
- Chern-Simons gravity: peaks at ell ~ 100-1000
- Spin-torsion: isotropic (all ell) + anisotropic low-ell component (amplitude and shape TBD)

No quantitative prediction exists for the anisotropic spectrum. We parameterize as:

    C_L^{beta beta} = A_aniso * f(L)

where f(L) is a template peaking at L ~ 1-5, but f(L) is not derived.

**Epistemic status:** QUALITATIVE. The existence of a preferred axis is motivated; the angular spectrum is not derivable.

---

## 3. Summary: Epistemic Classification

| Quantity | Classification | Notes |
|----------|---------------|-------|
| Parity-odd operator S_eff | Derived | One-loop motivated, well-defined |
| alpha/M ~ 10^{-21} GeV^{-1} | Phenomenological fit | Order of magnitude from one-loop estimate |
| [(alpha/M) * M_Pl] ~ 10^{-2} | Scaling ansatz | Dimensionless suppression factor |
| Photon-torsion coupling (f_photon) | **Not derived (gap)** | Requires one-loop computation not yet performed |
| beta from alpha/M | **Not derivable without f_photon** | Framework is consistent with beta != 0 but cannot predict its value |
| C_ell^{EB} given beta | Derived (standard) | No model dependence beyond beta |
| Anisotropic birefringence spectrum | Qualitative only | Preferred axis exists; spectrum not derived |
| Axis alignment (birefringence vs galaxy spin) | Qualitative prediction | Same axis expected; quantitative correlation not derived |

---

## 4. Direct Observables and Public Data

### 4.1 Isotropic Birefringence Angle beta

| Measurement | Value | Significance | Reference |
|-------------|-------|-------------|-----------|
| Planck (Minami & Komatsu 2020) | 0.35 +/- 0.14 deg | 2.4 sigma | arXiv:2011.11254 |
| Planck (Eskilt 2022) | 0.30 +/- 0.11 deg | 2.7 sigma | arXiv:2205.13962 |
| ACT DR6 (Diego-Palazuelos & Komatsu 2025) | 0.215 +/- 0.074 deg | 2.9 sigma | arXiv:2503.XXXXX |
| SPIDER+Planck+ACT combined | ~7 sigma total rotation | Calibration degeneracy caveat | arXiv:2411.XXXXX |

**Data format for analysis:** Each measurement provides beta +/- sigma_beta, directly usable as a Gaussian likelihood:

    L(beta | data_i) = N(beta; beta_i, sigma_i)

The Planck and ACT measurements use different instruments and analysis pipelines; their correlation is subdominant to statistical errors. A conservative combined constraint (inverse-variance weighted, ignoring correlations):

    beta_combined = 0.262 +/- 0.063 deg  (from Planck Eskilt + ACT DR6)

This is a 4.2-sigma combined detection (if treating as independent).

**Caveat:** The Planck and ACT measurements share some sky overlap and calibration assumptions. A joint analysis accounting for covariance would be more rigorous but is not publicly available.

### 4.2 EB/TB Power Spectra

**Public data status:**
- Planck NPIPE: Full EB/TB power spectra are available from the Planck Legacy Archive (PLA). However, the *likelihood* (covariance matrix, window functions) for EB/TB is not in the standard Planck likelihood release.
- ACT DR6: EB power spectrum measurements published in Diego-Palazuelos & Komatsu (2025). Bandpower values and uncertainties are in the paper; full likelihood code is not yet public (as of 2026-03-12).
- Eskilt (2022): Published the D_ell^{EB} bandpowers from Planck NPIPE with error bars (Table 1 of that paper).

**Usable for forward modeling:** The published bandpower values with error bars can be compared against the predicted EB shape from uniform rotation. This is a shape test, not a full likelihood analysis.

### 4.3 Anisotropic Birefringence

- Planck constraint on anisotropic birefringence: A_CB < 0.10 deg^2 (95% CL) at L=1 from Planck PR4 (Eskilt & Komatsu 2022, arXiv:2205.13962)
- No public likelihood for anisotropic birefringence.
- This observable is not quantitatively predicted by the framework.

### 4.4 Large-Angle Parity Anomaly

- The Planck large-angle parity anomaly (low-ell TB, EB) has been reported but is not a standard data product with a public likelihood.
- Not recommended for this analysis.

---

## 5. Feasible Analyses

### 5.1 Gaussian Constraint Sampling on beta -- READY

**Method:** Sample g_eff (or equivalently f_photon) using the published beta measurements as Gaussian likelihoods.

**Implementation:**
```
# Likelihood:
L(f_photon | beta_obs) = Product_i N(beta_model(f_photon); beta_i, sigma_i)

# Model:
beta_model = f_photon * [(alpha/M) * M_Pl] * Phi_cosmological
            = f_photon * 10^{-2} * Phi_cosmological

# Phi_cosmological absorbs the integrated field excursion.
# Can be marginalized over with a log-uniform prior.
```

**Outputs:**
- Posterior on f_photon (conditioned on alpha/M from the parent MCMC)
- Posterior on g_eff = (alpha/M) * f_photon
- Consistency window: what range of f_photon makes the framework compatible with data

**Effort:** Trivial (analytic or ~100 lines of Python). No map-level data needed.

**Verdict: READY FOR IMPLEMENTATION.**

### 5.2 Consistency Window Plot -- READY

**Method:** For fixed [(alpha/M) * M_Pl] = 10^{-2}, plot the required f_photon as a function of beta:

    f_photon * Phi_net = beta / [(alpha/M) * M_Pl] = beta / 10^{-2}

For beta = 0.30 deg = 5.24 * 10^{-3} rad:

    f_photon * Phi_net ~ 0.524

This is the consistency condition. A 2D plot of (f_photon, Phi_net) with the observed beta band overlaid shows the allowed region.

**Key insight:** The framework is consistent with ANY observed beta for some value of f_photon. The analysis is not about ruling out the model (which is unfalsifiable at this level) but about quantifying the required coupling strength. If f_photon turns out to be O(1), the framework is natural. If f_photon >> 1 or f_photon << 10^{-6}, the framework requires fine-tuning of its own.

**Outputs:**
- Consistency window plot: (alpha/M) vs f_photon, colored by predicted beta
- Naturalness assessment of f_photon given observed beta

**Effort:** Straightforward calculation + matplotlib. ~50 lines.

**Verdict: READY FOR IMPLEMENTATION.**

### 5.3 Forward-Model EB Spectrum Comparison -- FEASIBLE

**Method:** Given beta_iso from measurements, compute the predicted C_ell^{EB} and C_ell^{TB} spectra and compare against published bandpowers.

**Implementation:**
```
# Input: beta_iso (from measurement or posterior)
# Compute: C_ell^{EE}, C_ell^{BB}, C_ell^{TE} from CAMB/CLASS (standard LCDM)
# Predict: C_ell^{EB} = 2 * beta * (C_ell^{EE} - C_ell^{BB})
#          C_ell^{TB} = 2 * beta * C_ell^{TE}
# Compare: against Eskilt (2022) Table 1 bandpowers, ACT DR6 bandpowers
```

**What this tests:** Whether the observed EB spectrum is consistent with UNIFORM rotation (as predicted by the isotropic component) versus scale-dependent rotation (which would indicate a different mechanism and potentially falsify the spin-torsion interpretation).

**Outputs:**
- Predicted vs observed D_ell^{EB} plot
- Chi-squared for uniform rotation model
- Residuals that might indicate scale-dependent birefringence

**Effort:** Moderate (~200 lines Python, requires CAMB or CLASS). Needs published bandpower values digitized.

**Verdict: FEASIBLE. Worth doing as a shape consistency check.**

### 5.4 Full MCMC with EB/TB Likelihood -- NOT FEASIBLE

**Why not:** Would require:
- Map-level polarization data (Planck NPIPE QU maps)
- Full pixel-level or harmonic-space likelihood with correlated noise
- Treatment of foreground EB contamination
- Polarization angle self-calibration pipeline

This is the domain of dedicated CMB analysis teams. Not appropriate for an extension analysis.

**Verdict: NOT FEASIBLE (requires map-level data and dedicated pipeline).**

### 5.5 Joint Constraint with Parent MCMC -- FEASIBLE (with caveats)

**Method:** Combine the beta Gaussian likelihood with the parent paper's MCMC posterior on alpha/M.

**Implementation:**
- Draw alpha/M samples from the parent MCMC posterior
- For each sample, compute the required f_photon to match observed beta
- This gives a posterior on f_photon conditioned on the parent fit

**Caveat:** alpha/M in the parent MCMC is constrained by the dark energy scale (through Xi), not by birefringence. The birefringence constraint adds an independent likelihood dimension. However, the connection between the two goes through the unmeasured f_photon, so this is really just:

    P(f_photon | beta_obs, alpha/M_parent) = delta(f_photon - beta_obs / [alpha/M * M_Pl * Phi_net])

which is a derived quantity, not a genuine joint constraint.

**Verdict: FEASIBLE but the information content is limited to the consistency window.**

### 5.6 Model Discrimination (Spin-Torsion vs Axion vs Chern-Simons) -- FUTURE WORK

**Method:** Compare predicted EB spectral shapes for:
- Uniform rotation (spin-torsion isotropic): C_ell^{EB} propto (C_ell^{EE} - C_ell^{BB})
- Axion: similar shape but with specific scale-dependent corrections from axion mass
- Chern-Simons: different ell-dependence (peaks at ell ~ 100-1000)

**Why future work:** Current data (Planck, ACT) cannot distinguish these spectral shapes at the precision available. LiteBIRD and CMB-S4 will be needed.

**Verdict: FUTURE WORK ONLY.**

---

## 6. Recommended Analysis Pipeline

### Tier 1: Implement Now (publishable as supporting analysis)

1. **Consistency window plot** (Section 5.2)
   - Input: alpha/M = 10^{-21} GeV^{-1}, [(alpha/M)*M_Pl] = 10^{-2}
   - Input: beta_obs = 0.30 +/- 0.11 deg (Planck), 0.215 +/- 0.074 deg (ACT)
   - Output: Required f_photon as a function of Phi_net
   - Interpretation: Is f_photon ~ O(1) natural?

2. **Gaussian posterior on g_eff** (Section 5.1)
   - Sample f_photon with log-uniform prior
   - Gaussian likelihood from published beta measurements
   - Output: Posterior P(g_eff | beta_obs)

3. **Forward-model EB shape check** (Section 5.3)
   - Compute predicted C_ell^{EB} from CAMB + beta_obs
   - Compare with published Eskilt (2022) bandpowers
   - Output: Goodness-of-fit for uniform rotation hypothesis

### Tier 2: Include in Paper as Discussion

4. **Joint constraint with parent MCMC** (Section 5.5)
   - Derive f_photon posterior given alpha/M posterior
   - Present as consistency check, not new constraint

5. **Model discrimination forecast** (Section 5.6)
   - Qualitative comparison of spectral shapes
   - Forecast: what precision is needed to distinguish models

---

## 7. Key Honest Statements for the Paper

The following language should appear in any analysis using this track:

1. "The birefringence angle beta is not predicted by the spin-torsion framework; it requires a photon-torsion coupling (phi F F-tilde) that has not been derived from the gravitational operator."

2. "We parameterize this gap with an effective coupling g_eff = (alpha/M) * f_photon, where f_photon is an undetermined dimensionless vertex factor."

3. "The observed beta ~ 0.30 deg is consistent with the framework for f_photon * Phi_net ~ 0.5, but this is a consistency statement, not a prediction."

4. "The EB spectral shape (proportional to C_ell^{EE} - C_ell^{BB}) is a generic prediction of ANY uniform birefringence source and does not uniquely identify the spin-torsion mechanism."

5. "Distinguishing the spin-torsion origin from axion or Chern-Simons birefringence requires measuring the anisotropic birefringence spectrum, which is not quantitatively predicted by the current framework."

---

## 8. Verdict Summary

| Analysis | Readiness | Data Available | Novelty |
|----------|-----------|---------------|---------|
| Consistency window (f_photon) | READY | Yes (published beta) | Moderate -- quantifies the theoretical gap |
| Gaussian sampling on g_eff | READY | Yes (published beta) | Low-moderate -- standard parameter estimation |
| EB shape check | FEASIBLE | Partial (published bandpowers) | Moderate -- tests uniform rotation hypothesis |
| Full EB/TB MCMC | NOT FEASIBLE | No (needs map-level data) | High but inaccessible |
| Model discrimination | FUTURE WORK | No (precision insufficient) | High -- requires LiteBIRD/CMB-S4 |

**Overall recommendation: CONSTRAINT ANALYSIS (Gaussian sampling) + FORWARD MODEL**

The Tier 1 analyses are implementable with ~300 lines of Python, require only published measurements (no proprietary data), and produce scientifically honest results. They quantify the theoretical gap (f_photon) rather than papering over it, which is the right approach for a framework that acknowledges the missing photon-torsion coupling.

The strongest output of this track is the **consistency window**: demonstrating that alpha/M ~ 10^{-21} GeV^{-1} is compatible with beta ~ 0.30 deg for a natural range of the unknown coupling, rather than requiring extreme fine-tuning. This is a genuine (if modest) result.
