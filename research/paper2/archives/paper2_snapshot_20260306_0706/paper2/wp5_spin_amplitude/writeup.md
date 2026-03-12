# Scaling Estimate for Galaxy Spin Dipole Amplitude from Parity-Odd Tidal Torque Correction

**WP5 Technical Note — BigBounce Paper 2, Track B**

Houston Golden, March 2026

---

## 1. Introduction

Galaxy spin direction surveys have reported a persistent dipolar asymmetry
in the ratio of clockwise (CW) to counterclockwise (CCW) spirals across
the sky. Shamir (2024) finds a dipole amplitude A_0 ~ 0.003 using
multiple survey datasets (SDSS, Pan-STARRS, DECaLS), corresponding to a
~0.3% excess of one handedness along a preferred axis.

No first-principles prediction for this amplitude exists. The standard
Tidal Torque Theory (TTT) predicts exactly zero handedness preference
by parity symmetry. In this note, we derive a scaling estimate for A_0
as a function of a parity-odd coupling parameter epsilon_PO. This is a
phenomenological parity-odd tidal torque mapping — we do not derive
epsilon_PO from any specific Lagrangian. We determine the coupling
strength required to reproduce the observed signal, and assess its
plausibility.

## 2. Standard Tidal Torque Theory

The angular momentum of a protogalactic region arises from the
misalignment between its inertia tensor I and the tidal tensor T of the
large-scale gravitational potential (White 1984):

    L_i = epsilon_{ijk} T_{jl} I_{lk}                          (1)

The dimensionless spin parameter lambda = J |E|^{1/2} / (G M^{5/2})
follows a log-normal distribution with mean <lambda> ~ 0.035 and
sigma_{ln lambda} ~ 0.5 (Porciani, Dekel & Hoffman 2002).

**Key point**: Equation (1) is equivariant under parity (P: x -> -x
implies T -> T, I -> I, but epsilon_{ijk} -> -epsilon_{ijk}, so L -> -L).
The projection of L along any fixed axis is equally likely to be positive
or negative. Therefore, **TTT predicts A_0 = 0 identically**.

Any observed A_0 > 0 requires new physics that breaks parity.

## 3. Parity-Odd Extension

We introduce a minimal parity-odd correction to the TTT angular momentum:

    L -> L + epsilon_PO * (n_hat . L) * (n_hat x L)            (2)

where n_hat is a preferred direction (the "bounce axis" in the BigBounce
framework, physically motivated by the pre-bounce cosmic torsion field)
and epsilon_PO is a dimensionless coupling parameter.

This term is parity-odd: under P, n_hat -> -n_hat (it is a pseudovector
tied to the torsion field), L -> -L, so the correction term changes sign
relative to L, breaking the CW/CCW degeneracy.

### 3.1 Handedness probability

The probability of observing CW rotation depends on the viewing angle
theta relative to n_hat:

    P(CW | theta) = 0.5 + epsilon_PO * |cos theta| * g         (3)

where the geometric coupling factor is:

    g = (2/3) * lambda_mean / delta_rms                         (4)

The (2/3) arises from the angular average of tidal tensor eigenvalue
ratios; lambda_mean / delta_rms captures how efficiently the tidal
torque converts into observable spin.

### 3.2 Dipole amplitude

Averaging over a galaxy sample with uniform viewing angles:

    A_0 = epsilon_PO * <|cos theta|> * g
        = epsilon_PO * (2/pi) * (2/3) * lambda_mean / delta_rms
        ~ epsilon_PO * 0.015                                    (5)

where we used <|cos theta|> = 2/pi for isotropic viewing angles
and the standard TTT values lambda_mean = 0.035, delta_rms = 1.0.

## 4. Results

### 4.1 Required coupling strength

For the observed A_0 ~ 0.003 (Shamir 2024):

    epsilon_PO = A_0 / 0.015 ~ 0.2                             (6)

This corresponds to a **~20% parity-odd correction** to the standard
tidal torque.

### 4.2 Monte Carlo sensitivity

We performed a Monte Carlo analysis with 100,000 samples, varying:
- lambda_mean: log-normal (median 0.035, sigma 0.01)
- sigma_{ln lambda}: uniform [0.4, 0.6]
- delta_rms: uniform [0.5, 2.0]
- z_formation: uniform [0.5, 3.0]
- epsilon_PO: log-uniform [0.01, 1.0]

**Key findings:**
- Required epsilon_PO for A_0 = 0.003: median ~ 0.20, 68% CI ~ [0.10, 0.40]
- The dominant uncertainty comes from delta_rms (the environmental
  density), which enters inversely in the scaling
- The conservative upper bound (95th percentile of A_0 at epsilon_PO ~ 0.2)
  is A_0 ~ 0.005, consistent with observational constraints

## 5. Discussion

The required epsilon_PO ~ 0.2 is large — a 20% modification to the tidal
torque mechanism — but it is not observationally ruled out.

**Consistency with isotropy constraints**: Philcox & Ereza (2022)
searched for parity violation in the BOSS galaxy power spectrum and found
null results at the level of a few percent of the power spectrum amplitude.
Patel & Desmond (2024) tested cosmic isotropy with galaxy surveys and
found no significant dipole above A ~ few x 10^{-3}. Our predicted
A_0 ~ 0.003 sits at or below these upper limits, making it **consistent
but not yet testable** by these methods.

**Nature of the estimate**: This is a **consistency check**, not a
prediction. We show that the observed dipole amplitude is achievable
with a plausible (if somewhat large) parity-odd coupling in the TTT
framework. The main result is the mapping A_0(epsilon_PO): what
coupling strength is needed to reproduce the observed asymmetry.

## 6. Limitations

1. **Toy model**: The parity-odd correction (Eq. 2) is phenomenological.
   A rigorous derivation from the EC torsion action would modify the
   functional form and may introduce additional angular dependence.

2. **No N-body validation**: The scaling g ~ (2/3) * lambda / delta_rms
   has not been calibrated against parity-violating N-body simulations
   (which do not yet exist).

3. **Environmental dependence**: delta_rms varies significantly across
   environments (voids vs. filaments vs. clusters). The uniform [0.5, 2.0]
   prior is a rough approximation.

4. **epsilon_PO not derived**: The coupling is treated as a free
   parameter. Its value is not predicted from the torsion Lagrangian.

5. **Viewing angle distribution**: We assumed isotropic viewing angles.
   Survey-specific selection effects (magnitude limits, inclination cuts)
   could modify <|cos theta|>.

6. **Single preferred direction**: The model assumes a single global
   n_hat. More complex torsion fields could produce multipolar patterns.

## 7. Future Work

- **Paper 3 candidate**: Derive epsilon_PO from the Einstein-Cartan
  torsion coupling constants. The EC Lagrangian contains a parity-odd
  term ~ epsilon^{abcd} S_{abc} S_{d} whose coupling to TTT would
  determine epsilon_PO from first principles.

- **N-body simulations**: Run modified-gravity N-body simulations with
  a parity-odd tidal coupling to calibrate the geometric factor g.

- **Survey-specific predictions**: Apply the model to specific survey
  geometries (DESI, Euclid, LSST) to predict the expected signal
  and optimal detection strategies.

---

## References

- Patel, P. & Desmond, H. (2024). Tests of cosmic isotropy with galaxy surveys.
- Peebles, P. J. E. (1969). Origin of the angular momentum of galaxies. ApJ, 155, 393.
- Philcox, O. & Ereza, J. (2022). Testing parity symmetry of the universe with the BOSS galaxy survey. Phys. Rev. D, 106, 063501.
- Porciani, C., Dekel, A. & Hoffman, Y. (2002). Testing tidal-torque theory. MNRAS, 332, 325.
- Shamir, L. (2024). Asymmetry between galaxy spin directions.
- White, S. D. M. (1984). Angular momentum growth in protogalaxies. ApJ, 286, 38.
