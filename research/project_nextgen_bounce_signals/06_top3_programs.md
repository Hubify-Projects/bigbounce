# 06: Top 3 Theory Programs

**Created:** 2026-03-17
**Status:** COMPLETE

---

## Program 1: CHIRAL GRAVITATIONAL WAVES FROM TORSION BOUNCE

### Exact scientific question
Does the parity-odd structure of the Einstein-Cartan-Holst action produce a net circular polarization in the gravitational wave spectrum generated at the bounce?

### Exact observable target
The circular polarization fraction V/I of the stochastic GW background, as a function of frequency f. Specifically:
- The degree of chirality Δ_h(f) = [P_+(f) − P_−(f)] / [P_+(f) + P_−(f)]
- Where P_+(f) and P_−(f) are the power spectra of right- and left-handed tensor modes

### Exact minimal new ingredient
One parity-violating coupling in the gravitational sector. The most natural options:
1. **Chern-Simons coupling from the Barbero-Immirzi pseudoscalar:** S_CS = (1/f_a) ∫ σ R_μνρλ R̃^{μνρλ}
2. **Nieh-Yan coupling:** S_NY = (α/M) ∫ σ (T^a ∧ T_a − e^a ∧ e^b ∧ R_{ab})

Both are natural extensions of the Holst term when the Barbero-Immirzi parameter is promoted to a dynamical field. The coupling strength is related to γ = 0.274.

### What from the current repo can be reused
- ECH bounce background solution (a(t), H(t), ρ(t)) from Branch V Phase 1a
- Modified Friedmann equation and bounce dynamics
- Barbero-Immirzi parameter value and ECH framework
- ALP coupling structure from Paper 1

### First cheap test
**Analytic estimate of the chirality parameter at the bounce.**

During the bounce, H passes through zero and Ḣ > 0. The Chern-Simons coupling sources differential amplification of left vs right tensor modes:

$$
h_+'' + (k^2 \pm \lambda k \dot{\sigma}/a)h_+ = 0
$$

At the bounce, the effective coupling is maximized because curvature is Planckian. Estimate Δ_h at the bounce scale k_b analytically and determine whether it is O(1) (strongly chiral) or O(ε) (weakly chiral).

**Cheap kill:** If Δ_h ~ (k/k_b)^n with n ≥ 2 and k_b is Planckian, then no detector can see the chirality — signal is at 10⁹ GHz. Dead.

### First expensive test
Full numerical solution of the chiral tensor equation through the bounce for a range of k values. Extract P_+(k) and P_−(k) separately. Map to frequency-dependent V/I.

### Likely kill condition
- Chirality confined to k ~ k_b ~ M_Pl (unobservable frequency)
- Coupling strength too small (Planck-suppressed, Δ_h ~ 10⁻⁶⁰)
- Ghost or gradient instability in one polarization during the bounce

### What would count as a major win
- Δ_h = O(1) at frequencies accessible to LISA or ET (10⁻⁴–10³ Hz)
- A parametric prediction: Δ_h(f) with shape determined by γ = 0.274
- Testable within 10 years by cross-correlation techniques
- The story: "the Barbero-Immirzi parameter, fixed by black hole entropy, determines the chirality of the gravitational wave background from the bounce"

---

## Program 2: MODIFIED SIGW KERNEL FROM THE BOUNCE PHASE

### Exact scientific question
Does the non-standard background dynamics during the bounce (NEC violation, H = 0, Ḣ > 0) modify the scalar-induced gravitational wave kernel in a way that changes the SIGW spectrum at observable frequencies?

### Exact observable target
The SIGW spectrum Ω_GW(f) from the bounce, computed with the correct (bounce-modified) kernel, compared to the standard (FRW) kernel. The difference:
- ΔΩ_GW(f) = Ω_GW^{bounce kernel}(f) − Ω_GW^{standard kernel}(f)

### Exact minimal new ingredient
None — this uses the existing bounce background + second-order perturbation theory. The only "new" ingredient is doing the calculation correctly (not importing the standard FRW kernel).

### What from the current repo can be reused
- Full bounce background solution
- Scalar perturbation transfer function from Phase 1a
- PTA/LISA signal interpretation framework (from literature)

### First cheap test
**Estimate the kernel modification at the bounce point.**

The SIGW Green's function G_k(η, η') satisfies: G'' + (k² − a''/a)G = δ(η − η'). During the bounce, a''/a is modified. Estimate the fractional change in G at the bounce relative to pure radiation-dominated G.

**Cheap kill:** If the modification is O((k/k_b)²) for modes with k ≪ k_b, it is 10⁻⁵⁶ for CMB modes — zero. Need to check at PTA/LISA frequencies.

### First expensive test
Numerical computation of the SIGW kernel through the full bounce, for modes in the PTA band (f ~ nHz). Compare with standard kernel.

### Likely kill condition
- Kernel modification negligible for all modes below k_b
- No modes in the PTA/LISA band are affected by the bounce dynamics

### What would count as a major win
- A measurable correction to the SIGW spectral shape at PTA or LISA frequencies
- A distinctive spectral feature (notch, bump, phase shift) that distinguishes bounce from inflation
- Directly applicable to the existing NANOGrav/LISA data pipeline

---

## Program 3: RESONANT SPECTRAL FEATURES FROM NON-TRANSPARENT BOUNCE

### Exact scientific question
Can a non-instantaneous bounce with a structured effective potential produce resonant features (echoes, oscillations, spectral bumps) in the tensor or scalar power spectrum at frequencies accessible to GW detectors?

### Exact observable target
Oscillatory features in Ω_GW(f) at specific frequencies set by the bounce structure. The key signature: oscillations with period set by the bounce timescale, amplitude set by the degree of non-transparency.

### Exact minimal new ingredient
An extended bounce phase with a specific effective potential structure (e.g., double barrier from EOS transitions). This requires specifying the bounce interior in more detail than the single-parameter ECH bounce.

### What from the current repo can be reused
- ECH bounce background (as the starting point, to be extended)
- Perturbation solver framework from Phase 1a notebook
- Transfer function analysis tools

### First cheap test
**Compute the effective potential V_eff(η) = a''/a for the ECH bounce and check for structure.**

If the ECH bounce gives a smooth, single-peak potential: resonances are unlikely. If it gives a double-peak (barrier-well-barrier): resonant tunneling is possible.

**Cheap kill:** If the ECH bounce potential is a single smooth peak, there is no resonant structure and features require modifying the bounce model — losing the ECH connection.

### First expensive test
Numerical solution of tensor mode equation through the full ECH bounce potential, for a dense grid of k values. Map the transfer function |T_tensor(k)|² and look for oscillatory features.

### Likely kill condition
- ECH bounce potential is single-peaked → no resonances
- Features only at k ~ k_b (Planckian frequencies) → unobservable
- Features too small to distinguish from noise

### What would count as a major win
- Observable oscillatory features in Ω_GW(f) at LISA or ET frequencies
- Features with period and amplitude determined by γ = 0.274
- Similar to but distinct from the Zhu & Cai (2026) "echoes" result, with ECH-specific predictions
