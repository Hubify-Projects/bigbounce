# 08: Phase 1 Execution Blueprint — Chiral GW from Torsion Bounce

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Phase 1 Goal

Determine whether the ECH bounce with a dynamical Barbero-Immirzi pseudoscalar produces measurable circular polarization in the gravitational wave background, and if so, at what frequencies and with what spectral shape.

---

## Step 1: Parity Coupling Selection (analytic, ~1 session)

### Task
Choose between Chern-Simons and Nieh-Yan coupling. Derive the modified tensor perturbation equation for each.

### Chern-Simons route

Action addition:
$$
\Delta S = \frac{\alpha}{4f_a}\int d^4x\,\sqrt{-g}\,\sigma\,R\tilde{R}
$$

Modified tensor equation (conformal time):
$$
h_{\pm}'' + 2\mathcal{H}h_{\pm}' + \left(k^2 \mp k\,\mu(\eta)\right)h_{\pm} = 0
$$

where $\mu(\eta) = \alpha\,\sigma'/f_a$ and prime = d/dη.

**Need to determine:** What is σ(η) through the bounce? The ALP equation on the bounce background:
$$
\sigma'' + 2\mathcal{H}\sigma' + a^2 m_\sigma^2 \sigma = 0
$$

plus potential couplings to the curvature.

### Nieh-Yan route

Action addition:
$$
\Delta S = \frac{\alpha_{\rm NY}}{M}\int \sigma\,(T^a \wedge T_a - e^a \wedge e^b \wedge R_{ab})
$$

This only contributes when T ≠ 0 (i.e., near the bounce where fermions source torsion). The modified tensor equation acquires a correction proportional to the torsion background.

**Need to determine:** The background torsion T̄ through the bounce from the fermionic spin current.

### Decision criterion
Use Chern-Simons if it gives a tractable modified tensor equation with a clear coupling to the ALP.
Use Nieh-Yan if it gives a coupling that is specifically active only during the bounce (more distinctive but harder to compute).

**Recommendation:** Start with Chern-Simons (better understood, clearer tensor equation, directly comparable to inflationary Chern-Simons literature). If Chern-Simons gives a null result, assess whether Nieh-Yan could differ.

### Deliverable
`research/project_chiral_bounce_GW/01_coupling_selection.md`

---

## Step 2: ALP Background Through the Bounce (analytic + numerical, ~1 session)

### Task
Solve the ALP equation of motion on the ECH bounce background to determine σ(t) and σ̇(t).

### Key physics
The chiral coupling strength μ ∝ σ̇/a. For chirality to be generated, σ̇ must be nonzero during the bounce. This requires:
- The ALP to be rolling (not frozen at a minimum) during the bounce
- Or the ALP to be kicked by the curvature spike at the bounce

### Scenarios to check
1. **ALP rolling from contraction:** σ has initial velocity from the contracting phase. σ̇ is nonzero at the bounce.
2. **ALP frozen, kicked at bounce:** σ is at a minimum before the bounce. The curvature spike excites σ̇ through derivative couplings (Rσ̈ terms or Nieh-Yan coupling).
3. **ALP oscillating:** If m_σ ~ H_bounce, the ALP oscillates rapidly near the bounce. σ̇ averages to zero → no net chirality. This is the dangerous case.

### Quick kill check
If the ALP is the birefringence field (m_σ ~ 10⁻³³ eV), then m_σ/H_bounce ~ 10⁻⁷⁵. The ALP is completely frozen during the bounce — σ̇ = 0 from the mass term alone. **Chirality requires σ̇ from something other than mass oscillation** — likely from the initial rolling velocity or from a curvature coupling.

For a rolling ALP with initial velocity σ̇_i set during contraction: σ̇ at the bounce ~ σ̇_i × (a_contraction/a_bounce)^p where p depends on the effective friction. During dust contraction, a light scalar field is frozen (overdamped) if m ≪ H, so σ ≈ const and σ̇ ≈ 0. **This is a potential problem.**

**The ALP must have σ̇ ≠ 0 at the bounce. Where does this come from?**

Possible sources:
- Gravitational coupling: ξRσ gives an effective mass m²_eff = m² + ξR. Near the bounce, R is large → σ can be pushed.
- Initial displacement: if σ starts displaced from the minimum, it rolls. During contraction, the roll rate depends on the potential.
- Cosmological evolution: during contraction, σ rolls if H ~ m. But m ~ 10⁻³³ eV and H_bounce ~ M_Pl → σ doesn't roll.

**CRITICAL ASSESSMENT:** For the birefringence ALP (m ~ 10⁻³³ eV), σ̇ = 0 at the bounce unless there is a direct curvature coupling or initial velocity from before the contraction. The chiral signal may require either:
(a) A heavier ALP (not the birefringence field) — loses ECH connection
(b) A non-minimal curvature coupling ξRσ² that kicks the ALP at the bounce
(c) A Nieh-Yan coupling that sources σ̇ from torsion at the bounce

**Option (c) is the most ECH-specific.** The Nieh-Yan term NY = T^a∧T_a − e^a∧e^b∧R_{ab} is nonzero only when torsion is present (near the bounce). The coupling αNY σ NY sources σ̇ directly from the bounce torsion. This is the natural ECH mechanism for ALP excitation.

### Deliverable
`research/project_chiral_bounce_GW/02_alp_background.md` + numerical solution

---

## Step 3: Chiral Tensor Mode Equation (numerical, ~1-2 sessions)

### Task
Solve the modified tensor equation for both polarizations through the bounce.

### Equation
$$
h_{\pm}'' + 2\mathcal{H}h_{\pm}' + \left(k^2 \mp k\,\mu(\eta)\right)h_{\pm} = 0
$$

with μ(η) determined from Step 2 (ALP background).

### Implementation
- Use the bounce background from Phase 1a (a(η), H(η))
- Use σ(η) from Step 2
- Solve for h_+(k, η) and h_-(k, η) separately, for a range of k values
- Extract amplitudes at late times (well after the bounce)

### Key outputs
- |h_+(k)|² and |h_-(k)|² for each k
- Δ_h(k) = chirality parameter
- P_tensor(k) = total tensor power spectrum

### Deliverable
`research/project_chiral_bounce_GW/03_chiral_tensor_solver.ipynb`

---

## Step 4: Chirality Spectrum and Observable Mapping (~1 session)

### Task
Convert Δ_h(k) to Δ_h(f) using the post-bounce expansion history. Compare with detector sensitivities.

### Frequency mapping
$$
f = \frac{k}{2\pi a_0} = \frac{k}{k_b} \times f_b
$$

where f_b = k_b/(2πa_0) is the bounce frequency today.

### Key question
What is f_b? This depends on the expansion history between the bounce and today.

For the ECH bounce with ρ_c = 0.21 M_Pl⁴:
- k_b ~ M_Pl (Planckian bounce scale)
- f_b ~ 10⁹ GHz (if no inflation after the bounce)
- f_b ~ any frequency (if there is an inflationary phase after the bounce that redshifts k_b)

**Without post-bounce inflation:** All bounce-scale features are at unobservable GHz frequencies. This would kill the program.

**With post-bounce inflation or a long radiation era:** The bounce scale can be redshifted to observable frequencies. The amount of redshift depends on the total expansion factor, which is a free parameter.

**This is the critical frequency-reach question that determines viability.**

### Deliverable
`research/project_chiral_bounce_GW/04_chirality_spectrum.md`

---

## Step 5: Quick-Kill Checks (~1 session)

### Check 1: Ghost/gradient stability
Verify that neither h_+ nor h_- develops a ghost (wrong-sign kinetic term) or gradient instability (imaginary sound speed) during the bounce. The Chern-Simons coupling modifies the effective frequency: ω²_± = k² ∓ kμ. If μ > k for some k, one polarization has ω² < 0 → tachyonic instability. This must be checked.

### Check 2: Backreaction
The chiral amplification of one polarization produces GWs. If the amplification is too strong, the GW energy density backreacts on the background. Check that the tensor energy density remains subdominant: ρ_GW/ρ_total ≪ 1.

### Check 3: Consistency with existing bounds
Current upper limits on GW circular polarization from LIGO O3, NANOGrav 15yr. Verify that the predicted Δ_h(f) is consistent with these bounds.

### Deliverable
`research/project_chiral_bounce_GW/05_stability_checks.md`

---

## Step 6: Phase 1 Results (~1 session)

### Verdicts
- **CHIRAL_BOUNCE_VIABLE:** Observable chirality at detectable frequencies, consistent with current bounds, testable by LISA/ET
- **CHIRAL_BOUNCE_MARGINAL:** Chirality exists but at edge of detectability or requires specific assumptions about post-bounce history
- **CHIRAL_BOUNCE_DEAD:** Chirality unobservable (wrong frequency, too small, unstable)

### Deliverable
`research/project_chiral_bounce_GW/phase1_results.md`

---

## Resource Estimates

| Step | Type | Estimated effort | GPU needed? |
|------|------|-----------------|-------------|
| 1. Coupling selection | Analytic | 1 session | No |
| 2. ALP background | Analytic + light numerical | 1 session | No |
| 3. Chiral tensor solver | Numerical (ODE) | 1-2 sessions | No |
| 4. Observable mapping | Analytic + plotting | 1 session | No |
| 5. Stability checks | Analytic + numerical | 1 session | No |
| 6. Phase 1 results | Writing | 0.5 session | No |

**Total: ~5-6 sessions. No GPU, no MCMC.** All computations are ODE solutions (similar complexity to Phase 1a).

---

## MCMC Relevance

**Not relevant for Phase 1.** MCMC would only be needed if:
- Phase 1 produces a viable chirality prediction
- We want to fit the prediction to GW data (PTA or LISA)
- We want to constrain the coupling parameters

This is Phase 2+ territory, conditional on Phase 1 survival.
