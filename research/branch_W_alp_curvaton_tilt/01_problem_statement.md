# 01: Problem Statement — ALP Curvaton Tilt Program

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Why n_s = 1 is unacceptable

The dust contraction → bounce → radiation expansion scenario produces a Harrison-Zel'dovich spectrum:

$$
n_s = 1.000
$$

Planck 2018 measures:

$$
n_s = 0.9649 \pm 0.0042
$$

This is an **8.3σ** discrepancy. The model is excluded as-is.

The n_s = 1 result is a fundamental property of dust-dominated contraction (Finelli & Brandenberger 2002). It does not depend on the bounce mechanism. The ECH bounce faithfully transmits the pre-bounce spectrum (T = 1 for super-Hubble modes). **The bounce cannot fix the tilt. Something else must generate it.**

---

## Why ALP/curvaton is the cleanest available tilt mechanism

### What the literature offers

| Mechanism | Reference | Status |
|-----------|----------|--------|
| Nearly-dust contraction (w ≈ 0.003) | Quintin et al. 2015 | Works but requires fine-tuned w ≠ 0 |
| Entropy-to-curvature conversion | Cai et al. 2009 | Requires second field + specific bounce coupling |
| Curvaton mechanism | Cai & Brandenberger 2011 | Standard curvaton physics, needs a spectator field |
| Fermion curvaton (Fermi-bounce) | Alexander, Cai, Marcianò 2014 | Uses EC torsion + second fermion species |
| ALP as curvaton | This work (proposed) | Uses ECH pseudoscalar already in the framework |

### Why ALP curvaton is preferred

1. **The ALP already exists in the ECH framework.** The Barbero-Immirzi pseudoscalar, when promoted to a dynamical field, is an axion-like particle. This same field is responsible for the cosmic birefringence prediction (our surviving positive prediction from Paper 1).

2. **No new fields are introduced.** The curvaton IS the ALP that the framework already motivates. This is economical.

3. **Standard curvaton physics applies.** The curvaton mechanism is well-understood (Lyth & Wands 2001, Moroi & Takahashi 2001). The ALP just needs to be light enough during contraction to acquire nearly scale-invariant fluctuations, with a mass that generates the observed red tilt.

4. **The fermion curvaton precedent exists.** Alexander et al. (2014) already proposed a fermion curvaton in the Fermi-bounce context. Our ALP curvaton is the bosonic/pseudoscalar analog.

---

## How this branch relates to the bounce

### If Part A (ECH perturbation gate) survives:
ALP curvaton is built on top of ECH-specific perturbation dynamics. The tilt comes from the ALP, and the bounce provides ECH-specific transfer corrections.

### If Part A fails (which it did):
ALP curvaton is a **bounce-compatible extension**. The ECH framework provides:
1. The bounce background (modified Friedmann equation)
2. The ALP's existence (motivated by the Barbero-Immirzi pseudoscalar)
3. The birefringence prediction (from the same ALP)

The perturbation dynamics are standard (no ECH corrections). The novelty is in the **specific ALP model** motivated by the ECH framework, not in the perturbation equations themselves.

**This is an honest framing:** the bounce provides the cosmological scenario; the ALP provides the tilt and the birefringence; the connection to ECH is through the ALP's origin as the Barbero-Immirzi field.

---

## Success criteria

1. **Generate n_s ≈ 0.965** — The ALP curvaton must produce a red-tilted spectrum consistent with Planck.
2. **Preserve viable amplitude** — A_s ≈ 2.1 × 10⁻⁹ from the curvaton's contribution.
3. **Keep f_NL acceptable** — The curvaton mechanism generically produces f_NL ~ O(1–10). Must remain within Planck bounds (|f_NL| < ~5 at 1σ).
4. **Avoid obvious fine tuning** — The ALP mass and initial conditions should be natural, not contrived.
5. **Remain simpler and cleaner than ad-hoc alternatives** — If the ALP curvaton requires more tuning than "nearly-dust contraction" (w ≈ 0.003), it loses its advantage.

---

## Key prior work to distinguish from

- **Cai & Brandenberger (2011)**, arXiv: 1101.0822 — "The Matter Bounce Curvaton Scenario." Generic curvaton in a matter bounce. We must show what's different about the ALP curvaton (answer: ECH origin, birefringence connection).

- **Alexander, Cai, Marcianò (2014)**, arXiv: 1406.1456 — "Fermi-bounce Curvaton Mechanism." Fermion curvaton in the Fermi-bounce. Different matter content but same conceptual framework.

Our novelty over these: the curvaton is the **specific ALP motivated by the Barbero-Immirzi pseudoscalar**, with mass and coupling constrained by the birefringence observation. This is more predictive than a generic curvaton.
