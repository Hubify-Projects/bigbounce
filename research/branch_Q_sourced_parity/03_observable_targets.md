# Branch Q: Observable Targets for Each Candidate

**Date:** 2026-03-16

---

## Observable 1: Cosmic Birefringence (beta)

### What it is

Rotation of the linear polarization plane of CMB photons during propagation.
Measured through TB and EB cross-correlations in the CMB power spectrum.

### Current data

- **Isotropic birefringence:** beta = 0.35 +/- 0.09 degrees (3.9 sigma)
  from Minami-Komatsu (2020), confirmed by Planck PR4 + ACT DR6
- **Anisotropic birefringence:** consistent with zero, sigma(beta_alm) ~ 0.1 deg
- **Frequency dependence:** none detected (consistent with phi F F-tilde)

### Which candidates produce it

| Candidate | Mechanism | Predicted beta | Match? |
|-----------|-----------|---------------|--------|
| A (Grav CS) | NO (couples to gravity, not photons) | 0 | -- |
| B (Standard ALP) | phi F F-tilde, phi roll | ~ Delta phi / (2 f_a) | YES (by construction) |
| C (Dynamical Immirzi) | Induced phi F F-tilde via ABJ anomaly | ~ alpha Delta phi / (8 pi^2 f_phi) | YES (if f_phi tuned) |
| D (Explicit phi FF-tilde) | Direct coupling | ~ g Delta phi / 2 | YES (by construction) |
| E (Explicit PV) | Indirect, through S_0 matter coupling | ~ 10^{-30} deg | NO |
| F (Nieh-Yan + inst.) | Same as C | Same as C | YES (if f_phi tuned) |
| G (PGT parity-odd) | NO (gravity sector only) | 0 | -- |

### Key data to face

- Planck PR4 + ACT DR6 combined analysis
- LiteBIRD (launch ~2032): sigma(beta) ~ 0.01 deg
- CMB-S4: sigma(beta) ~ 0.03 deg
- Simons Observatory: sigma(beta) ~ 0.05 deg

### Distinctiveness test

For birefringence, the question is: does the ECH origin of phi predict
anything about beta that a generic ALP does not?

Possible distinctive predictions from Candidate C:
1. **Coupling relation:** If phi = Immirzi field, its coupling to photons
   goes through the ABJ anomaly with coefficient alpha/(4 pi f_phi). But
   this is the SAME coupling any ALP-fermion derivative coupling produces.
   No distinction.

2. **Mass-coupling correlation:** If the mass comes from QCD-like instantons,
   m_phi ~ Lambda^2 / f_phi. But this is the standard ALP mass relation.
   No distinction.

3. **Multi-messenger correlation:** If phi also couples to gravity through
   the Pontryagin density (Candidate A), there would be a CORRELATED
   prediction: birefringence AND chiral GWs from the same field. The
   ratio beta / Delta chi would be predicted. THIS IS POTENTIALLY
   DISTINCTIVE -- but requires BOTH couplings to be present, making the
   model less minimal.

---

## Observable 2: Chiral Gravitational Wave Spectrum

### What it is

A difference in the power spectra of left- and right-circular GW
polarizations: Delta P_T = P_R - P_L (or equivalently, a nonzero
V-mode Stokes parameter for the stochastic GW background).

### Current data

- **Tensor-to-scalar ratio:** r < 0.032 (Planck + BICEP/Keck 2021)
- **CMB TB/EB from tensors:** consistent with zero
- **LIGO/Virgo/KAGRA stochastic background:** Omega_GW < 10^{-8} at 25 Hz
- **NANOGrav PTA:** possible stochastic background at nHz, chirality not measured

### Which candidates produce it

| Candidate | Mechanism | Predicted chirality | Frequency band |
|-----------|-----------|-------------------|----------------|
| A (Grav CS) | Modified GW propagation | Delta v/v ~ theta-dot/M_CS | CMB + LIGO |
| B (Standard ALP) | NO (couples to photons, not gravity) | 0 | -- |
| C (Dynamical Immirzi) | Through Nieh-Yan at perturbation level | Planck-suppressed | -- |
| D (Explicit phi FF-tilde) | NO | 0 | -- |
| E (Explicit PV) | Marginal (torsion backreaction) | Negligible | -- |
| F (Nieh-Yan + inst.) | Same as C | Same as C | -- |
| G (PGT parity-odd) | Modified torsion propagator | Model-dependent | LIGO-to-PTA |

### Key data to face

- LiteBIRD: can detect r > 10^{-3}, TB/EB sensitivity at that level
- LIGO O4/O5: stochastic background search with V-mode
- LISA: mHz band, chirality measurable for strong sources
- Einstein Telescope: best prospects for stochastic V-mode

### Distinctiveness test

Only Candidates A and G produce chiral GWs. Candidate A is standard dCS
gravity (not ECH-specific). Candidate G requires propagating PGT torsion
and a separate analysis.

---

## Observable 3: Parity Asymmetry in Galaxy Statistics

### What it is

A correlation between galaxy spins and their large-scale environment that
violates parity. Measured through 4-point functions or spin-position
correlations in galaxy surveys.

### Current data

- Claimed detections (Motloch-Hu 2021, Hou et al. 2023): 2-3 sigma
- Systematic uncertainties large; not confirmed at high significance
- DESI, Euclid: future measurements with much larger samples

### Which candidates produce it

None of the candidates A-G directly predict galaxy parity asymmetry.
This observable requires parity violation in the MATTER sector during
structure formation, not just in the photon or gravity sectors.

An ALP coupled to matter could in principle produce parity-dependent
halo formation, but this is a highly model-dependent, multi-step process
with no clear prediction from any candidate.

### Assessment: NOT A DIRECT TARGET for this program.

---

## Observable 4: Dark Radiation (Delta N_eff)

### What it is

Additional relativistic degrees of freedom at BBN and recombination,
parameterized by Delta N_eff.

### Current data

- N_eff = 2.99 +/- 0.17 (Planck 2018 + BAO)
- BBN: N_eff = 2.89 +/- 0.29

### Which candidates produce it

| Candidate | Mechanism | Predicted Delta N_eff |
|-----------|-----------|---------------------|
| A (Grav CS) | theta field oscillations | Model-dependent, likely < 0.03 |
| B (Standard ALP) | ALP dark radiation | Delta N_eff = 0.027 per species if thermalized |
| C (Dynamical Immirzi) | phi oscillations | Same as B |
| G (PGT parity-odd) | Torsion dark radiation | Requires m_T < eV |

### Assessment: GENERIC

Any light scalar/pseudoscalar contributes to N_eff similarly. Not a
distinctive test of ECH origin.

---

## Observable 5: Frequency-Dependent Birefringence

### What it is

If birefringence comes from photon-ALP oscillations (rather than a
uniform phi roll), the rotation angle depends on photon frequency.
This is distinct from the phi F F-tilde mechanism, which gives
frequency-independent rotation.

### Current data

No frequency dependence detected (Planck multi-frequency analysis).

### Which candidates produce it

Only Candidate E (if torsion has a mass m_T ~ eV and couples directly
to photons) could produce frequency-dependent birefringence. All
phi F F-tilde mechanisms (B, C, D, F) give frequency-INDEPENDENT rotation.

### Distinctiveness: POTENTIALLY USEFUL as a null test

The ABSENCE of frequency dependence is consistent with phi F F-tilde
and rules out some alternative mechanisms. But this does not distinguish
among the phi F F-tilde candidates.

---

## Observable Summary: What Faces Real Data

| Observable | Best candidate | Data quality | Distinctive? |
|------------|---------------|-------------|-------------|
| Isotropic birefringence | B, C, D, F | 3.9 sigma detection | NO (all give same) |
| Anisotropic birefringence | B, C, D, F | Upper limits | NO |
| Chiral GWs (CMB tensors) | A | r < 0.032 | YES (A only) |
| Chiral GWs (LIGO band) | A, G | Upper limits | Partially |
| Galaxy parity | None | 2-3 sigma claims | -- |
| Delta N_eff | B, C | N_eff = 2.99 +/- 0.17 | NO |
| Freq-dependent bire. | E | Null | Null test only |

### The uncomfortable conclusion

**No candidate produces a birefringence prediction that is DISTINCTIVE
to the ECH origin.** The birefringence signal, if explained by any of
these extensions, looks identical to a generic ALP. The only potentially
distinctive observable is chiral GWs from Candidate A, which is standard
dynamical CS gravity and not ECH-specific.

The most that can be said for Candidate C (dynamical Immirzi) is that
it provides a GEOMETRIC MOTIVATION for the existence of the ALP. But
the observable consequences are identical to any other ALP with the
same (f_phi, m_phi).

### Multi-messenger correlation: the one possible exception

If the Immirzi field phi couples BOTH to the Nieh-Yan density (producing
birefringence via the ABJ anomaly route) AND to the Pontryagin density
(producing chiral GWs), then the RATIO of birefringence to GW chirality
is a prediction:

```
beta / Delta chi ~ (alpha / 4 pi) * (M_CS / f_phi) * (n_f sum Q_f^2)
```

This ratio would be specific to the model (since both couplings come
from the same field). But:
1. It requires TWO couplings (less minimal)
2. The chiral GW signal is undetectable with current data (r < 0.032)
3. The ratio depends on the two coupling constants, not on ECH geometry

So even the multi-messenger approach is not genuinely distinctive.
