# Phase 0 Results: Chiral GW Frequency Reach Gate

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Verdict

$$
\boxed{\textbf{CHIRAL\_GW\_FREQUENCY\_GATE\_FAILED}}
$$

---

## Characteristic frequency today

The ECH bounce occurs at ρ_crit = 0.21 M_Pl⁴, with characteristic timescale Δt ~ 4 t_Pl and physical frequency scale f_* ~ 0.265 M_Pl/(2π) ~ 10⁴¹ Hz.

After redshifting from the bounce to today (assuming standard radiation → matter → Λ expansion with entropy conservation):

$$
f_0 \approx 10^{9}\text{–}10^{10}\,\text{Hz} \quad (\text{GHz})
$$

This is 6 orders of magnitude above the highest-frequency operating detector (LIGO at ~kHz) and 12–18 orders above LISA/PTA.

---

## Detector-band overlap

| Detector | Band | Gap from f_0 | Overlap? |
|----------|------|-------------|----------|
| PTA | nHz | 10¹⁸ | **NO** |
| LISA | mHz | 10¹² | **NO** |
| DECIGO | Hz | 10⁹ | **NO** |
| ET | Hz–kHz | 10⁶ | **NO** |
| LIGO | 10 Hz–kHz | 10⁶ | **NO** |
| High-f concepts | MHz–GHz | 0–1 | **MARGINAL** (but sensitivity ~10⁻²⁰, signal ~10⁻³⁰) |

**Zero overlap with any current or planned detector.**

---

## Parametric windows tested

Five mechanisms were tested to bring the signal to observable frequencies:

1. **Lower bounce energy:** Frequency scales as ρ^{1/4}, but amplitude scales as ρ². To reach LISA: need ρ^{1/4} ~ 10⁶ GeV, giving Ω_GW ~ 10⁻⁵³. Dead.

2. **Post-bounce inflation (30–60 e-folds):** Redshifts frequency by e^{-N} but dilutes amplitude by e^{-4N}. Net: amplitude killed. Dead.

3. **Extended matter-dominated phase:** Reshapes spectrum but cannot bridge 13-order frequency gap within BBN bounds. Dead.

4. **Extended parity coupling duration:** Coupling dies as 1/t² after bounce. To reach LISA modes: coupling must persist for 10¹⁴ t_Pl, at which point it is suppressed by 10⁻²⁸. Dead.

5. **Parametric resonance:** Resonance occurs at k ~ k_b (bounce scale), no extension to lower k. Dead.

**No non-absurd parameter window survives.**

---

## The fundamental obstruction

This is not a parameter-tuning failure. It is a structural scaling relation:

$$
f_0 \propto \rho_{\rm bounce}^{1/4}, \quad \Omega_{\rm GW} \propto \rho_{\rm bounce}^2
$$

$$
\therefore\quad \Omega_{\rm GW} \propto f_0^8
$$

Bringing the signal from GHz to mHz (factor 10⁻¹³) kills the amplitude by factor 10⁻¹⁰⁴. This cannot be circumvented by any post-bounce processing.

The core issue: **a Planck-scale bounce produces Planck-scale signals.** The entire observable universe today is the inflated/expanded version of a Planck-sized patch. Bounce-scale physics is irretrievably diluted by this expansion. The only way bounce-scale physics reaches us is through superhorizon modes that were processed during the contraction phase — but those modes pass through the bounce transparently (T = 1), carrying no bounce imprint.

**This is the same transparency problem in frequency space.** The bounce is either:
- Transparent to long-wavelength modes (no imprint, but modes at observable frequencies), or
- Active on short-wavelength modes (strong imprint, but modes at GHz frequencies)

There is no intermediate regime.

---

## Should the branch proceed to full Phase 1?

**NO.** The frequency gate has failed definitively. The chiral signal cannot reach any detector band under any physically reasonable assumption. Proceeding to compute the detailed chirality spectrum would be an academic exercise with no observational relevance.

---

## What this means for the broader program

The frequency-reach problem is not specific to the chiral GW proposal. It applies to ALL bounce-scale signals from a Planck-energy bounce:

- Chiral GWs → GHz (failed)
- GW memory from the bounce → GHz (would also fail)
- Resonant spectral features at the bounce scale → GHz (would also fail)
- Modified SIGW kernel at the bounce → only affects modes near k_b → GHz (would also fail)
- Phase transition at the bounce → GHz (would also fail)

**Every candidate theory class from the next-gen scan that relies on bounce-SCALE physics (as opposed to contraction-phase physics) is killed by the same frequency-amplitude scaling.**

The only bounce signals that reach observable frequencies are those generated during the CONTRACTION phase (when modes are at CMB-scale wavelengths and evolve on sub-Hubble scales). But these are exactly the signals we already showed are generic and non-novel (n_s = 1, f_NL = -35/8, transparent transfer).

---

## Exact recommended next move

The bounce-signal program faces a fundamental structural barrier that goes beyond any specific theory class:

> **A Planck-scale bounce cannot leave sub-Planck-scale observable imprints, because the expansion ratio a_0/a_b ~ 10³¹ dilutes all bounce-scale physics to GHz frequencies or above.**

This is not a problem with ECH specifically. It is a problem with ANY Planck-scale bounce.

The only escape routes are:
1. **A sub-Planckian bounce** (ρ_bounce ≪ M_Pl⁴) — but then the bounce has nothing to do with quantum gravity or ECH, and the signal amplitude is negligible
2. **Contraction-phase signals** — these reach observable frequencies but are generic (matter bounce n_s = 1, already in the literature)
3. **Late-time consequences of the bounce** (e.g., the ALP/birefringence prediction, which is set by the ALP mass and coupling, not the bounce scale) — these are observable but independent of the bounce

**Recommended:** Document this structural barrier and assess whether the bounce program as a whole retains any viable path to an observable that is both novel and bounce-dependent. If not, the honest conclusion is that the ECH bounce resolves the singularity but is observationally silent — and the surviving predictions (birefringence) are independent of the bounce.
