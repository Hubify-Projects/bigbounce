# 06: BKL and Stability Check

**Created:** 2026-03-17
**Status:** IN PROGRESS

---

## The BKL Problem

During a contracting phase, anisotropies (described by the shear σ²) grow relative to the isotropic energy density:

$$
\frac{d(\sigma^2/\rho)}{d\ln a} = -\frac{6\sigma^2 - 3(1+w)\rho}{\rho} = -6\frac{\sigma^2}{\rho} + 3(1+w)
$$

In terms of scaling:
- Shear: σ² ∝ a⁻⁶ (always, regardless of matter content)
- Matter density: ρ ∝ a⁻³⁽¹⁺ʷ⁾

The ratio:
$$
\frac{\sigma^2}{\rho} \propto a^{-6+3(1+w)} = a^{3w-3}
$$

During contraction (a decreasing), this ratio GROWS if:
$$
3w - 3 > 0 \implies w > 1
$$

Wait — during contraction, a is decreasing, so a⁻ⁿ grows for n > 0 and decreases for n < 0.

$$
\frac{\sigma^2}{\rho} \propto a^{3w-3}
$$

During contraction (a → 0):
- If 3w − 3 < 0 (i.e., w < 1): the ratio σ²/ρ → ∞ as a → 0 → **anisotropy dominates → BKL instability**
- If 3w − 3 > 0 (i.e., w > 1): the ratio σ²/ρ → 0 as a → 0 → **anisotropy is diluted → stable**
- If w = 1: the ratio is constant → marginal

**The critical value is w = 1.**

---

## BKL Assessment for Each Model Variant

### Matter contraction (w ≈ 0)

$$
\frac{\sigma^2}{\rho} \propto a^{-3} \to \infty \quad \text{as } a \to 0
$$

**Strongly unstable.** The anisotropy grows as a⁻³ relative to matter density during contraction. After N_contract e-folds of contraction:

$$
\frac{\sigma^2}{\rho}\bigg|_{\rm bounce} = \frac{\sigma^2}{\rho}\bigg|_{\rm initial} \times e^{3N_{\rm contract}}
$$

For N_contract = 60 (needed for observable modes to fit within the Hubble radius):
$$
\text{amplification} = e^{180} \approx 10^{78}
$$

For the FRW solution to be valid until the bounce, the initial anisotropy must satisfy:
$$
\frac{\sigma^2}{\rho}\bigg|_{\rm initial} < 10^{-78}
$$

**This is an extreme fine-tuning of initial conditions.** The contracting FRW solution is an unstable attractor — nearly all initial conditions lead to anisotropy-dominated (Kasner/Mixmaster) contraction, not FRW contraction.

### Nearly-matter contraction (w = 0.003)

$$
\frac{\sigma^2}{\rho} \propto a^{-2.991}
$$

Essentially the same as w = 0. The tiny EOS modification does nothing for BKL stability.

**Still strongly unstable.**

### Ekpyrotic contraction (w >> 1)

For w = 10:
$$
\frac{\sigma^2}{\rho} \propto a^{27}
$$

During contraction (a → 0): a²⁷ → 0. **Anisotropy is powerfully diluted.**

For w = 3:
$$
\frac{\sigma^2}{\rho} \propto a^{6}
$$

Still diluted, though less powerfully.

**Ekpyrotic contraction with w > 1 resolves BKL.** This is the Ijjas & Steinhardt result.

---

## The BKL-Tilt Tension

### The Problem

To resolve BKL: need w > 1 during contraction
To get n_s ≈ 1 (before curvaton tilt): need w ≈ 0 during contraction
To get f_NL ≈ −35/8: need w ≈ 0 during contraction

**These requirements are contradictory for a single-phase contraction.**

### The Two-Phase Solution

**Phase 1 (early contraction): Ekpyrotic (w >> 1)**
- Dilutes anisotropy
- Does NOT generate the observable scalar perturbations (those modes are still sub-Hubble)

**Phase 2 (late contraction): Matter-dominated (w ≈ 0)**
- Generates scale-invariant scalar spectrum
- Generates f_NL ≈ −35/8
- Lasts for the final ~60 e-folds before the bounce

**The transition:** At some point during contraction, the EOS transitions from w >> 1 to w ≈ 0. This could happen through:
- A phase transition in the scalar potential
- The scalar field rolling from a steep region (ekpyrotic) to a flat region (matter-like) of V(φ)
- A two-field system where one field dominates early and another dominates late

### Does this resolve BKL?

**Yes, IF the ekpyrotic phase dilutes anisotropy sufficiently before the matter phase begins.**

During the ekpyrotic phase (w >> 1, lasting N_ek e-folds):
$$
\frac{\sigma^2}{\rho}\bigg|_{\rm end\,ek} = \frac{\sigma^2}{\rho}\bigg|_{\rm initial} \times e^{-(3w-3)N_{\rm ek}}
$$

For w = 10 and N_ek = 10:
$$
\text{suppression} = e^{-270} \approx 10^{-117}
$$

Then during the matter phase (w ≈ 0, lasting N_mat = 60 e-folds):
$$
\frac{\sigma^2}{\rho}\bigg|_{\rm bounce} = \frac{\sigma^2}{\rho}\bigg|_{\rm end\,ek} \times e^{3 N_{\rm mat}} = \frac{\sigma^2}{\rho}\bigg|_{\rm initial} \times e^{-270+180}
$$

$$
= \frac{\sigma^2}{\rho}\bigg|_{\rm initial} \times e^{-90} \approx 10^{-39} \times \frac{\sigma^2}{\rho}\bigg|_{\rm initial}
$$

**For O(1) initial anisotropy:** σ²/ρ at the bounce ~ 10⁻³⁹. This is tiny — FRW is an excellent approximation at the bounce.

**The two-phase model resolves BKL.** 10 e-folds of ekpyrotic contraction (w ~ 10) before 60 e-folds of matter contraction is sufficient.

### Effect on Observables

**Observable modes** (CMB scales, k ~ 0.05 Mpc⁻¹) exit the Hubble radius during the MATTER phase, not the ekpyrotic phase. Therefore:
- n_s, f_NL are set by the matter phase → unchanged from the single-phase analysis
- The ekpyrotic phase only affects very small-scale modes (those that exit during the ekpyrotic phase)

**The curvaton must also operate during the matter phase** (not the ekpyrotic phase) to generate the tilt. This is consistent — the curvaton perturbation δσ is generated when the relevant mode exits the horizon during the matter phase.

---

## Other Stability Concerns

### Gradient Instability

In the matter bounce, the perturbation equation is:
$$
v_k'' + (c_s^2 k^2 - z''/z) v_k = 0
$$

For c_s² > 0 (standard matter or scalar field): no gradient instability. ✓

For DBI models: c_s² > 0 always. ✓

**Potential issue:** Near the bounce, the effective mass z''/z changes rapidly. If z''/z becomes large and negative during the bounce, modes could be temporarily unstable. This is model-dependent and is already accounted for in the LQC treatment (the dressed-metric approach handles this).

### Ghost Instability

In the matter bounce, a ghost (wrong-sign kinetic term) can appear if the NEC is violated at the bounce. For the LQC effective equation:
- No ghost — the ρ² correction comes from quantum geometry, not a modified kinetic term
- The effective Friedmann equation H² = (ρ/3M²)(1 − ρ/ρ_c) with ρ_c > 0 is ghost-free

For generic NEC-violating bounces (Galileon, Horndeski): ghosts and gradient instabilities are a serious concern. The LQC/ECH bounce avoids this because it is not a classical NEC violation — it is a quantum-gravity effect.

### Particle Production at the Bounce

At the bounce, the rapid change in the scale factor can produce particles (preheating-like effects). This has been studied in LQC:
- Particle production is efficient for modes near the bounce scale (~Planck)
- For superhorizon modes (observable scales): particle production is negligible
- This does not affect the perturbation spectrum on observable scales ✓

---

## Summary: Stability Verdict

| Issue | Status | Resolution |
|-------|--------|-----------|
| BKL instability | CRITICAL for w ≈ 0 | Two-phase contraction (ek → matter) |
| Gradient instability | OK | c_s² > 0 throughout |
| Ghost instability | OK | LQC bounce is ghost-free |
| Particle production | OK | Negligible on observable scales |

**The BKL problem is the ONLY serious stability issue, and it is resolved by a two-phase contraction.**

The two-phase model adds one more ingredient (the ekpyrotic pre-phase) but:
- It is physically motivated (scalar field rolling from steep to flat potential)
- It does not affect observable predictions (those are set by the matter phase)
- It requires only ~10 e-folds of ekpyrotic contraction

---

## Updated Model: Two-Phase LQC Bounce + Curvaton

**Phase 1 (early):** Ekpyrotic contraction with w >> 1, lasting ~10 e-folds → resolves BKL
**Phase 2 (late):** Matter contraction with w ≈ 0, lasting ~60 e-folds → generates spectrum
**Bounce:** LQC (quantum-geometry corrections suppress r to ~10⁻⁴)
**Curvaton:** Spectator with m_σ ≈ 0.76 H_k, α ≈ 0.3 → provides red tilt
**Post-bounce:** Radiation domination, curvaton decays

This is the COMPLETE model. All known issues are addressed:
- n_s ≈ 0.965 ✓ (curvaton)
- r ~ 10⁻⁴ ✓ (LQC)
- f_NL ≈ −3.7 ✓ (matter contraction, partially diluted by curvaton)
- BKL ✓ (ekpyrotic pre-phase)
- Ghost/gradient ✓ (LQC bounce)
