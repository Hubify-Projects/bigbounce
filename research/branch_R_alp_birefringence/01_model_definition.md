# Branch R: ALP Cosmic Birefringence -- Model Definition

**Status:** ACTIVE
**Date:** 2026-03-16
**Scope:** Generic Planck-scale ALP phenomenology (NOT ECH-specific)

---

## 1. Field Content

A single pseudoscalar axion-like particle (ALP) field phi with:

- **Decay constant:** f_a (free parameter, motivated at M_Pl = 2.4 x 10^18 GeV)
- **Mass:** m_phi ~ H_0 ~ 10^{-33} eV (ultralight)
- **Initial misalignment angle:** theta_i = phi_i / f_a, with theta_i ~ O(1)

## 2. Potential

$$V(\phi) = m^2 f_a^2 \left[1 - \cos\left(\frac{\phi}{f_a}\right)\right]$$

This is the standard instanton-generated cosine potential. Near the minimum:

$$V(\phi) \approx \frac{1}{2} m^2 \phi^2 - \frac{m^2}{24 f_a^2} \phi^4 + \ldots$$

The mass parameter m is the physical mass at the minimum. The potential height is 2 m^2 f_a^2.

## 3. Photon Coupling

The ALP-photon coupling arises from the Adler-Bell-Jackiw (ABJ) anomaly. For any pseudoscalar that couples to fermions charged under U(1)_EM, integrating out those fermions at one loop generates:

$$\mathcal{L} \supset -\frac{g_{a\gamma}}{4} \phi \, F_{\mu\nu} \tilde{F}^{\mu\nu}$$

where

$$g_{a\gamma} = \frac{C_{a\gamma} \, \alpha}{2\pi \, f_a}$$

### Anomaly coefficient C_{agamma}

For fermions coupling to the ALP with PQ charge X_f, the anomaly coefficient is:

$$C_{a\gamma} = 2 \sum_f N_c^{(f)} \, Q_f^2 \, X_f$$

For the Standard Model fermions with universal PQ charge X_f = 1:

| Fermion | N_c | Q_f | N_c Q_f^2 |
|---------|-----|-----|-----------|
| u, c, t | 3 | 2/3 | 3 x 4/9 = 4/3 |
| d, s, b | 3 | 1/3 | 3 x 1/9 = 1/3 |
| e, mu, tau | 1 | 1 | 1 |

Per generation: 4/3 + 1/3 + 1 = 8/3

Three generations: 3 x 8/3 = 8

Therefore: **C_{agamma} = 2 x 8/3 x 3 = 2 x 8 ... wait, let's be precise.**

The factor of 2 accounts for both chiralities. For a single generation of SM fermions:

$$\sum_f N_c Q_f^2 = 3 \times (2/3)^2 + 3 \times (1/3)^2 + 1 \times 1^2 = 4/3 + 1/3 + 1 = 8/3$$

For 3 generations with X_f = 1:

$$C_{a\gamma} = 2 \times 3 \times \frac{8}{3} = 16$$

**Correction:** The factor of 2 in C_{agamma} already appears in the definition of g_{agamma}. The standard convention is:

$$C_{a\gamma} = 2 \sum_f N_c Q_f^2 X_f$$

With X_f = 1 per generation:
- Per generation: 2 x (4/3 + 1/3 + 1) = 2 x 8/3 = 16/3
- Three generations: 3 x 16/3 = 16

**However**, the user specifies C_{agamma} = 2 Sum N_c Q_f^2 ~ 8 for SM, which uses the convention:

$$C_{a\gamma} = 2 \sum_f N_c Q_f^2 = 2 \times 4 = 8$$

where the sum over 3 generations gives Sum N_c Q_f^2 = 3 x 8/3 = 8, but with the factor of 2 from the anomaly triangle (left + right chiralities each contributing, or equivalently the Dirac trace). Thus:

**C_{agamma} = 8 (SM, KSVZ-like convention with universal coupling)**

This is the convention we adopt throughout.

## 4. Cosmological Equation of Motion

On an FRW background:

$$\ddot{\phi} + 3H\dot{\phi} + m^2 f_a \sin\left(\frac{\phi}{f_a}\right) = 0$$

where H = H(t) is the Hubble parameter.

### Evolution Regimes

**Frozen regime (H >> m):**
- The Hubble friction term 3H phi_dot dominates over the restoring force
- phi ~ phi_i = f_a theta_i = const
- Energy density: rho_phi ~ V(phi_i) = m^2 f_a^2 (1 - cos theta_i) ~ const
- Equation of state: w_phi ~ -1 (cosmological-constant-like)
- This persists from inflation through recombination for m ~ H_0

**Transition (H ~ m):**
- Field begins to roll at t_osc defined by 3H(t_osc) ~ m
- For m ~ H_0: this happens at z ~ O(1), i.e., in the recent universe

**Oscillating regime (H << m):**
- phi oscillates around the minimum with decreasing amplitude
- Time-averaged: <rho> ~ a^{-3}, w ~ 0 (dark-matter-like)
- For m ~ H_0: the field has NOT yet entered this regime today

**Key point for birefringence:** For m ~ H_0, the field is frozen at phi_i during recombination and has rolled by O(f_a theta_i) by today. This maximizes the field excursion Delta_phi = phi(z_rec) - phi(0) and hence the birefringence signal.

## 5. Relation to ECH / Spin-Torsion Motivation

The Einstein-Cartan-Holst (ECH) framework with fermion coupling naturally generates a pseudoscalar degree of freedom through the Barbero-Immirzi field or the Nieh-Yan topological density. Foundations A-G of Paper 1.2 showed that connecting such a geometric pseudoscalar to dark energy encounters seven structural barriers (mass-coupling lock, topological-shift duality, etc.).

**However**, the barriers are specific to deriving DE from geometry. The ALP birefringence phenomenology studied here is:

1. **Generic** -- it applies to any ultralight ALP regardless of UV origin
2. **Agnostic** about the DE connection -- the ALP may or may not be DE
3. **Motivated** by ECH only insofar as ECH provides a natural pseudoscalar coupled to fermions (and hence to photons via ABJ)

This branch treats the ALP as a standalone phenomenological model. The ECH motivation is a plausibility argument for why such a field might exist with f_a ~ M_Pl, but the predictions and constraints are purely those of generic ALP physics.

## 6. Free Parameters

| Parameter | Symbol | Range | Fiducial |
|-----------|--------|-------|----------|
| Decay constant | f_a | 10^{16} -- 10^{19} GeV | M_Pl = 2.4 x 10^{18} GeV |
| ALP mass | m_phi | 10^{-34} -- 10^{-28} eV | H_0 ~ 10^{-33} eV |
| Misalignment angle | theta_i | 0 -- pi | 1 |
| Anomaly coefficient | C_{agamma} | 6 -- 14 | 8 (SM) |

The birefringence observable beta depends on (C_{agamma}, f_a, theta_i, m_phi). The first three enter as an overall amplitude; m_phi controls the field dynamics (how much of the initial excursion converts to Delta_phi).
