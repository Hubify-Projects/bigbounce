# Branch T: Order-of-Magnitude Screening

**Date:** 2026-03-16

---

## Screening protocol

Each candidate is evaluated on three gates:
1. **Source gate:** Does the coupling produce a nonzero source S(t) on FRW during the bounce?
2. **Amplitude gate:** Does the resulting xi reach O(1) for allowed parameter values?
3. **Observable gate:** Does the amplification map to a detectable signal?

Verdict labels: PASS, MARGINAL, FAIL, FATAL

---

## Candidate A: (partial_mu a / f_a) J^{5 mu}

| Gate | Result | Verdict |
|------|--------|---------|
| Source | Nonzero only if n_5 != 0 (free parameter). Symmetric bounce gives zero net kick at leading order. Subleading from dissipation. | FAIL |
| Amplitude | xi ~ n_5/(2 f_a^2 H). For maximal n_5 ~ T^3 at ECH bounce: xi ~ (M_Pl/f_a)^2. Reaches 1 for f_a ~ M_Pl. | MARGINAL |
| Observable | Backreaction limits xi < 1.1 at ECH scale. GW at 10^{11} Hz (undetectable). Birefringence degenerate with misalignment. | FAIL |

**Overall: FAIL.** Source requires free parameter; signal degenerate with generic ALP.

---

## Candidate B: (a / f_a) R-tilde-R

| Gate | Result | Verdict |
|------|--------|---------|
| Source | R-tilde-R = 0 on FRW. Identically zero. | FATAL |

**Overall: FATAL.** Zero source on FRW background.

---

## Candidate C: (a / f_a) epsilon T T

| Gate | Result | Verdict |
|------|--------|---------|
| Source | After torsion elimination: reduces to kappa^2 (J^5)^2 / f_a. Same as A with extra G^2 suppression. | FATAL |

**Overall: FATAL.** Not independent of A; strictly weaker.

---

## Candidate D: Immirzi-axion mixing

| Gate | Result | Verdict |
|------|--------|---------|
| Source | Immirzi drops out on-shell on FRW (Branch Q). Zero source. | FATAL |

**Overall: FATAL.** Already closed.

---

## Candidate E: (a / f_a) * Nieh-Yan

| Gate | Result | Verdict |
|------|--------|---------|
| Source | Topological in RC geometry (total derivative). After torsion elimination: same as C. | FATAL |

**Overall: FATAL.** Reduces to C.

---

## Candidate F: Parametric resonance

| Gate | Result | Verdict |
|------|--------|---------|
| Source | No oscillatory H(t) in spin-torsion bounce. Single zero-crossing. | FATAL |

**Overall: FATAL.** Wrong bounce topology.

---

## Candidate G: Dynamical n_5 generation

| Gate | Result | Verdict |
|------|--------|---------|
| Source | Gravitational chiral anomaly ~ R-tilde-R = 0 on FRW. Sphalerons equilibrate chirality, don't produce it. Gravitational particle production parity-symmetric on FRW. | FATAL |

**Overall: FATAL.** FRW parity symmetry prevents chiral generation.

---

## Summary table

| Candidate | Source | Amplitude | Observable | Overall |
|-----------|--------|-----------|------------|---------|
| A: partial a . J^5 | FAIL (free param) | MARGINAL | FAIL | **FAIL** |
| B: a R-tilde-R | FATAL | -- | -- | **FATAL** |
| C: a eps TT | FATAL | -- | -- | **FATAL** |
| D: Immirzi mix | FATAL | -- | -- | **FATAL** |
| E: a Nieh-Yan | FATAL | -- | -- | **FATAL** |
| F: parametric | FATAL | -- | -- | **FATAL** |
| G: dynamical n_5 | FATAL | -- | -- | **FATAL** |

**Zero candidates pass all three gates.** The best candidate (A) fails at the source gate (requires free n_5) and at the observable gate (degenerate with generic ALP).

---

## Structural barriers identified

**Barrier 18 (Bounce symmetry cancellation):** The time-reversal symmetry of the ECH/PGT bounce ensures that any parity-odd source integrated through the bounce gives zero at leading order. The net axion kick comes only from dissipative corrections (subleading, model-dependent).

**Barrier 19 (Amplification duration):** The bounce lasts ~ 1/H_max ~ 1 e-fold. Gauge field amplification requires sustained tachyonic growth over many e-folds. The bounce is too short by a factor of ~ 50-60 compared to inflation.

**Barrier 20 (Backreaction ceiling):** At the Planck-scale bounce, even moderate xi ~ 1 produces gauge field energy comparable to rho_crit. There is no perturbative regime: either the amplification is negligible or it destroys the background.

These three barriers are independent and each is individually sufficient to close the branch.
