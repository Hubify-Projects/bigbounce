# Systematic Effects in Cosmic Birefringence Measurements

**P6 Track D — Systematics Review**

Houston Golden, March 2026

---

## 1. Overview

Cosmic birefringence — the rotation of the linear polarization plane of CMB
photons by an angle beta — is measured through the EB cross-power spectrum.
In standard LCDM, C_l^EB = 0 by parity symmetry. A nonzero beta rotates
E-modes into B-modes and vice versa, producing:

    C_l^EB(beta) = (1/2) sin(4*beta) * (C_l^EE - C_l^BB)     (1)

For small beta (in radians):

    C_l^EB ~ 2*beta * C_l^EE                                   (2)

since C_l^EE >> C_l^BB on most scales and sin(4*beta) ~ 4*beta.

The challenge is that instrumental and astrophysical effects can also produce
nonzero EB correlations. This writeup catalogues the three dominant
systematic effects and summarizes the current status of their control.

## 2. Calibration Angle Degeneracy

**This is the single largest systematic in all current measurements.**

### 2.1 The Problem

Every polarization-sensitive detector has an orientation angle psi relative
to the telescope. An error alpha_misc in the knowledge of this angle produces
a rotation of the measured polarization:

    (Q +/- iU)_obs = e^{+/- 2i*alpha_misc} * (Q +/- iU)_true

This generates a spurious EB signal:

    C_l^EB(alpha_misc) = (1/2) sin(4*alpha_misc) * (C_l^EE - C_l^BB)

Comparing with Eq. (1), we see that the miscalibration angle alpha_misc is
*exactly degenerate* with the cosmic birefringence angle beta at each
frequency:

    C_l^EB(observed) = C_l^EB(beta + alpha_misc)

### 2.2 The Self-Calibration Method

Minami & Komatsu (2020, arXiv:2011.11254) resolved this degeneracy by
exploiting the fact that:

- Cosmic birefringence beta rotates ALL frequencies by the same angle
  (because it is a propagation effect between last scattering and today)
- Miscalibration angles alpha_i are different for each frequency channel
  (because each channel has different optics and detector orientations)

By fitting a model with one common beta and separate alpha_i for each
frequency channel i, they can separate the two effects. The key assumption
is that Galactic dust emission does NOT have intrinsic EB correlation
(which is supported by dust models and by the frequency independence of
the extracted beta).

### 2.3 Residual Risk

The self-calibration method assumes:
- Galactic foreground EB is negligible after frequency decorrelation
- The cosmic beta is truly frequency-independent
- There are enough frequency channels to break the degeneracy

Planck provides 5 polarization channels (30-353 GHz), giving 4 degrees
of freedom for alpha_i after fixing one reference channel. ACT provides
2 channels (98, 150 GHz). SPIDER provides 2 channels (95, 150 GHz).

The combined SPIDER+Planck+ACT analysis (arXiv:2510.25489) uses 7+
independent channels across three different instruments with completely
different scan strategies and optics, providing the strongest test of
the self-calibration method.

**Current assessment**: The self-calibration method is well-motivated and
has been validated by consistency across instruments. However, any
frequency-dependent birefringence (e.g., from Faraday rotation in
magnetized media) would not be captured by this method. The Eskilt (2022)
analysis explicitly checked for frequency dependence and found none.

## 3. Galactic Dust EB Contamination

### 3.1 The Problem

Galactic thermal dust emission is polarized. If the dust polarization
has intrinsic EB correlation (due to the morphology of the Galactic
magnetic field), it would contaminate the cosmic birefringence signal.

### 3.2 Current Understanding

- Dust EB is expected to be nonzero due to the misalignment between
  filament orientations and the magnetic field (Clark et al. 2015,
  Planck Intermediate Results XXXVIII).
- However, dust EB has a known frequency dependence: it scales as
  the square of the dust spectral energy distribution, which is steep
  in the Planck HFI bands.
- Cosmic birefringence, by contrast, is frequency-independent.
- The multi-frequency analysis of Eskilt (2022) found that the
  extracted beta is consistent across frequencies after accounting for
  dust, providing evidence that dust EB is not driving the signal.

### 3.3 Masking

All analyses use Galactic masks that remove the Galactic plane (typically
40-60% sky fraction retained). The beta measurement is stable under
variations of the mask threshold (tested by Minami & Komatsu 2020 and
Eskilt 2022), suggesting that residual dust in the unmasked region is
not a dominant contaminant.

**Current assessment**: Galactic dust EB is a subdominant systematic
after multi-frequency decorrelation and masking. The consistency of beta
across frequencies is strong evidence against dust contamination.

## 4. Instrumental Polarization Leakage

### 4.1 The Problem

Imperfect optics can leak temperature (T) signal into polarization (Q, U).
Since the CMB temperature anisotropy is much brighter than polarization,
even small leakage can produce spurious EB.

### 4.2 Control

- Planck PR4/NPIPE reprocessing corrected known bandpass leakage effects
  (Planck 2020, A&A 643, A42).
- ACT DR6 uses a different optical design (crossed-Dragone) with
  different leakage properties, providing an independent check.
- SPIDER uses a completely different platform (balloon-borne) with
  its own leakage characterization.
- The consistency of beta across Planck, ACT, and SPIDER is evidence
  against instrumental leakage as the origin of the signal.

**Current assessment**: Instrumental leakage is controlled at the level
required for current beta precision. Future sub-0.01 degree measurements
will require more stringent leakage characterization.

## 5. Other Effects

### 5.1 Beam Systematics

Asymmetric beams can couple temperature to polarization. Planck NPIPE
reprocessing includes improved beam models. ACT DR6 also uses refined
beam characterization. Not expected to be a dominant systematic at
current precision.

### 5.2 Noise Bias

EB noise bias is expected to be zero in the cross-spectrum formalism
used by all current analyses (different detector splits or frequency
channels are cross-correlated, so noise does not correlate). This is
a well-established technique in CMB analysis.

### 5.3 Gravitational Lensing

Weak gravitational lensing by large-scale structure converts E-modes
to B-modes, producing a small EB correlation. This effect is
well-modeled and can be subtracted. At current precision, it is
subdominant to the beta signal.

## 6. Summary Table

| Systematic              | Impact on beta        | Control method                    | Status     |
|-------------------------|-----------------------|-----------------------------------|------------|
| Calibration angle       | Exactly degenerate    | Multi-frequency self-calibration  | Controlled |
| Galactic dust EB        | Subdominant           | Frequency decorrelation + masking | Controlled |
| Instrumental leakage    | Small                 | Cross-instrument consistency      | Controlled |
| Beam asymmetry          | Small                 | Improved beam models (NPIPE)      | Controlled |
| Noise bias              | Zero (cross-spectra)  | Cross-correlation formalism       | N/A        |
| Gravitational lensing   | Subdominant           | Lensing template subtraction      | Controlled |

## 7. Implications for BigBounce

The current observational status of cosmic birefringence is:

- **Planck-only**: 2.4-3.6 sigma depending on analysis method
- **ACT DR6**: 2.9 sigma (independent of Planck)
- **SPIDER+Planck+ACT combined**: 7 sigma

The signal appears robust against known systematics, as evidenced by:
1. Consistency across three independent instruments
2. Frequency independence (argues against dust and miscalibration)
3. Stability under mask variations
4. Consistency between spectrum-level and map-level analyses (within
   systematic uncertainties)

However, claiming cosmic birefringence as "detected" requires caution:
- The 7sigma combined result uses correlated data from overlapping
  analyses
- Systematic uncertainties (especially calibration angle) are
  partially correlated between Planck-based analyses
- Map-level analyses (Zagatti+2025) show mild tension with
  spectrum-level analyses, suggesting unresolved systematics

**Our position**: Cosmic birefringence is a strong observational hint
(2.4-2.9 sigma from individual experiments, 7 sigma combined) that is
consistent with the parity violation predicted by Einstein-Cartan torsion
in the BigBounce framework. We treat it as supporting evidence, not a
confirmed detection, pending further cross-instrument validation from
CMB-S4, LiteBIRD, and Simons Observatory.

## References

- Minami & Komatsu (2020), PRL 125, 221301, arXiv:2011.11254
- Eskilt (2022), A&A 662, A10, arXiv:2205.13962
- Eskilt et al. (2022), PRD 106, 063503, arXiv:2203.04830
- Zagatti et al. (2025), arXiv:2502.07654
- Diego-Palazuelos & Komatsu (2025), arXiv:2509.13654
- SPIDER Collaboration (2025), arXiv:2510.25489
- Clark et al. (2015), ApJ 789, 82
- Planck 2020, A&A 643, A42 (NPIPE)
