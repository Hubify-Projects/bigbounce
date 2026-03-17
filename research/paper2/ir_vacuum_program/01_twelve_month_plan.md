# 12-Month Research Plan: IR Vacuum Persistence

**Start date:** 2026-04 (after Paper 1 preaudit)
**End date:** 2027-03
**Structure:** 6 phases, 3 parallel tracks, 3 potential papers

---

## Phase 1 — Clean Up the Microscopic Theory (Months 1–2)

**Deliverable:** Canonical Action Memo (2–4 pages, internal)

### 1.1 Settle Foundational Questions

| Question | Options | Must decide before Phase 2 |
|----------|---------|---------------------------|
| Is the parity-odd operator fundamental, induced at loop level, or just a scaling proxy? | Fundamental in Holst action / Loop-induced / Phenomenological | YES |
| Which fields are dynamical? | Tetrad + connection / Metric + torsion / Metric only (after integration) | YES |
| Is the Barbero-Immirzi parameter fixed, running, or replaced by a field? | Fixed (γ = 0.274) / Running / Promoted to pseudoscalar | YES |
| What is being integrated out? | Torsion only / Torsion + fermions / Torsion + fermions + Immirzi field | YES |

### 1.2 Write the Canonical Action

Start from Einstein-Cartan-Holst + Dirac fermions in first-order (tetrad/spin-connection) form:

```
S = S_EC[e, ω] + S_Holst[e, ω; γ] + S_Dirac[e, ω, ψ]
```

where:
```
S_EC = (M_Pl²/2) ∫ ε_{IJKL} e^I ∧ e^J ∧ F^{KL}[ω]

S_Holst = (M_Pl²/2γ) ∫ e^I ∧ e^J ∧ F_{IJ}[ω]

S_Dirac = ∫ d⁴x e [ψ̄ (iγ^μ D_μ - m) ψ]
```

Specify:
- Full field content
- Symmetries (local Lorentz, diffeomorphisms, parity behavior)
- Boundary terms (Nieh-Yan)
- Which sector generates the parity-odd operator

### 1.3 Torsion Elimination

Solve the torsion equation of motion algebraically (Einstein-Cartan torsion is non-propagating):

```
T^I_{μν} = (κ²/4) ε^I_{JKL} ψ̄ γ^J γ^K γ^L ψ  (+ Holst correction)
```

Substitute back to get the **reduced action** in metric + fermion variables:
- Four-fermion contact interaction (Hehl 1976)
- Parity-odd four-fermion interaction (from Holst term; Freidel-Minic-Takeuchi 2005)
- Any induced pseudo-scalar terms

**Milestone 1:** Canonical action memo complete. No ambiguity about starting point.

---

## Phase 2 — Compute the Low-Energy Effective Action (Months 2–5)

**Deliverable:** Explicit 1-loop or semiclassical Γ_eff

This is the core Track A computation.

### 2.1 Reformulate with Auxiliary Fields

Introduce Hubbard-Stratonovich auxiliary fields to decouple the four-fermion interactions:

```
(ψ̄ Γ ψ)² → σ (ψ̄ Γ ψ) - σ²/4G
```

where:
- σ: scalar channel (fermion bilinear ⟨ψ̄ψ⟩)
- π: pseudoscalar channel (⟨ψ̄ γ⁵ ψ⟩)
- Possibly vector/axial-vector channels

The parity-odd interaction specifically generates a **pseudoscalar** auxiliary field. This is the natural candidate for a condensate.

### 2.2 One-Loop Effective Potential

Integrate out fermions in a controlled background:

**Background choice (simplest first):**
1. de Sitter (technically cleanest — maximally symmetric)
2. FRW with constant H (quasi-de Sitter)
3. Full FRW with time-dependent H (hardest)

**Method:** Functional determinant / heat-kernel expansion / zeta-function regularization

Compute:
```
V_eff(σ, π) = V_tree(σ, π) + V_1-loop(σ, π)
```

where V_1-loop comes from the fermion determinant in the background (σ, π, g_μν).

### 2.3 The Critical Fork

Inspect V_eff for whether it contains a source-independent minimum:

| Result | Meaning |
|--------|---------|
| V_eff has a minimum at (σ*, π*) ≠ 0 with V_eff(σ*, π*) ≠ 0 | **Condensate forms** — vacuum term survives |
| V_eff minimum is at (σ*, π*) = 0 when spin density → 0 | **No condensate** — no residual vacuum term |
| V_eff minimum exists but V_eff(σ*, π*) = 0 identically | **Condensate but zero vacuum energy** — interesting but doesn't help |

This is the make-or-break point.

### 2.4 Equations to Derive

1. **Fermion propagator** in curved spacetime with auxiliary field background
2. **Heat-kernel coefficients** a₀, a₁, a₂ (Seeley-DeWitt) for the Dirac operator with parity-odd mass term
3. **Effective potential** V_eff(σ, π; R, H) including curvature corrections
4. **Gap equation** ∂V_eff/∂σ = 0, ∂V_eff/∂π = 0
5. **Vacuum energy density** ρ_vac = V_eff(σ*, π*)

### 2.5 Key References to Follow

- Odintsov (1991): Effective action in curved spacetime with four-fermion interaction
- Inagaki, Muta, Odintsov (1997): NJL model in curved spacetime
- Parker & Toms (2009): Quantum Field Theory in Curved Spacetime (textbook)
- Buchbinder, Odintsov, Shapiro (1992): Effective Action in Quantum Gravity (textbook)
- Chattopadhyay (2023): One-loop effective action in chiral Einstein-Cartan gravity [arXiv:2310.10405] — **directly relevant**

**Milestone 2:** Explicit V_eff computed. Fork decision made.

---

## Phase 3 — Build Condensate Model (Months 4–7)

**Deliverable:** Effective potential with gap equation and vacuum energy

This is Track B — execute in parallel with Phase 2, accelerate if Phase 2 fork goes to "no direct residual."

### 3.1 NJL-Type Model in Curved Spacetime

The torsion-induced four-fermion interaction has exactly the structure of a Nambu–Jona-Lasinio (NJL) model:

```
L_4f = -G_s (ψ̄ψ)² - G_p (ψ̄ iγ⁵ψ)²
```

where G_s and G_p come from torsion elimination (Phase 1). The Holst term contribution makes G_s ≠ G_p (parity breaking).

**Key question:** Does the parity-odd coupling G_p − G_s create a pseudoscalar condensate ⟨ψ̄ iγ⁵ψ⟩ ≠ 0 that would not form in standard NJL?

### 3.2 Candidate Order Parameters

| Order parameter X | Physical meaning | Symmetry broken | Mechanism |
|-------------------|-----------------|-----------------|-----------|
| ⟨ψ̄ψ⟩ (scalar bilinear) | Chiral condensate | Chiral symmetry | Standard NJL |
| ⟨ψ̄ iγ⁵ψ⟩ (pseudoscalar) | Parity condensate | P symmetry | **Novel — from Holst term** |
| ⟨K_{[abc]}⟩ (torsion VEV) | Torsion condensate | — | Induced by spin density |
| Immirzi field ⟨φ_γ⟩ | Promoted Immirzi | — | Misalignment / Peccei-Quinn |

The **pseudoscalar condensate** is the most promising because:
1. It is directly sourced by the parity-odd interaction
2. Standard NJL does NOT produce it (needs the Holst term)
3. It carries a vacuum energy contribution

### 3.3 Solve the Gap Equation

In mean-field approximation:

```
∂V_eff/∂σ = σ/2G_s - ⟨ψ̄ψ⟩_σ,π = 0
∂V_eff/∂π = π/2G_p - ⟨ψ̄ iγ⁵ψ⟩_σ,π = 0
```

where the fermion expectation values depend on (σ, π) through the fermion propagator. Solve self-consistently.

### 3.4 Compute Vacuum Energy at the Minimum

```
ρ_vac = V_eff(σ*, π*) = V_tree + V_1-loop
```

Check:
- Sign (must be positive for dark energy)
- Magnitude (must be ∼ (2.3 meV)⁴ after inflationary dilution)
- Parameter dependence (must connect to α/M and Ξ in a sensible way)

### 3.5 Gravitationally Enhanced Gap

In curved spacetime, the NJL gap equation gets curvature corrections:

```
m_dyn² = m² + G_eff × Λ_UV² + ξR + ...
```

The curvature R near the bounce is enormous (∼ M_Pl²). This could:
- Catalyze symmetry breaking that wouldn't occur in flat space
- Generate a condensate that then "freezes" as the universe expands
- Provide the mechanism by which the theory remembers the early source

**This is the most promising route.**

**Milestone 3:** Gap equation solved. Condensate exists or does not. Vacuum energy computed at minimum.

---

## Phase 4 — Derive the Equation of State (Months 6–8)

**Deliverable:** T_μν^eff and w(a)

### 4.1 Effective Stress-Energy Tensor

From the effective action Γ_eff[g], derive:

```
T_μν^eff = -(2/√-g) δΓ_eff/δg^μν
```

For a condensate at its minimum:
```
T_μν^eff = -V_eff(σ*, π*) g_μν + (kinetic terms if σ*, π* vary)
```

If the condensate is truly frozen (σ* = const, π* = const), then T_μν = -ρ_vac g_μν exactly, giving w = −1.

### 4.2 Time Dependence Check

The condensate values (σ*, π*) might evolve as the universe expands (R, T, μ change). Solve the evolution:

```
σ̈ + 3Hσ̇ + ∂V_eff/∂σ = 0
π̈ + 3Hπ̇ + ∂V_eff/∂π = 0
```

If the condensate tracks its minimum adiabatically, w(a) ≈ −1 + small corrections.
If it oscillates, w(a) deviates significantly — changes the paper's predictions.

### 4.3 Connection to Existing Parameterization

Verify that the theory-derived ρ_vac matches:

```
ρ_vac = Ξ M_Pl⁴ = [(α/M) M_Pl] × D_inf × M_Pl⁴
```

This requires showing:
- The condensate energy scales as (α/M) (one-loop suppression)
- Inflationary dilution reduces it by D_inf
- The result is independent of late-time spin density

**Milestone 4:** w(a) derived. Either w = −1 (confirms current assumption) or w ≠ −1 (requires revision).

---

## Phase 5 — Stability and Naturalness Audit (Months 8–10)

**Deliverable:** "Does it really persist?"

### 5.1 Radiative Stability

Compute higher-loop corrections to V_eff(σ*, π*). Check:
- Does the vacuum energy receive large radiative corrections?
- Is the condensate technically natural (protected by a symmetry)?
- What is the renormalization group running of ρ_vac?

### 5.2 Decoupling Test

Explicitly set late-time spin density to zero and verify:
- Condensate (σ*, π*) does NOT relax to zero
- Vacuum energy V_eff(σ*, π*) does NOT vanish
- The condensate is maintained by its own self-interaction, not by an external source

**This is the make-or-break test from the executive summary.**

### 5.3 Ghost and Instability Checks

- No ghost degrees of freedom in the auxiliary field sector
- No gradient instabilities
- No tachyonic modes around the condensate minimum
- Perturbation theory around the condensate background is well-defined

### 5.4 Sensitivity Analysis

| Parameter | Sensitivity | Acceptable? |
|-----------|------------|-------------|
| α/M | Must enter at one-loop level | Check |
| γ (Barbero-Immirzi) | Should enter through G_p − G_s | Check |
| N_tot | Must produce the right dilution | Check (already in paper) |
| T_reh | Should enter through reheating factor | Check (already in paper) |
| Fermion mass spectrum | New dependence — how strong? | CRITICAL CHECK |

**Milestone 5:** Stability established or fatal instability found.

---

## Phase 6 — Cosmological Implementation (Months 10–12)

**Deliverable:** Replace phenomenological Λ with theory-derived module

### 6.1 Modified CAMB/CLASS Module

Only if Phases 2–5 succeed:

1. Encode V_eff(σ*, π*; a) as a dark energy density function
2. If w ≠ −1 exactly, implement w(a) from Phase 4
3. Couple to the Boltzmann hierarchy if perturbation effects are non-negligible

### 6.2 Rerun MCMC

- Planck + BAO + SN
- Full tension dataset
- Compare: does the theory-derived module give the same or different constraints?

### 6.3 Updated Predictions

If the derivation gives w(a) ≠ −1:
- New predictions for DESI, Euclid, LSST
- Distinguishability from ΛCDM
- Falsification criteria update

**Milestone 6:** Theory-anchored cosmological fits complete.

---

## Timeline Summary

| Month | Phase | Track | Deliverable |
|-------|-------|-------|-------------|
| 1–2 | Phase 1 | — | Canonical action memo |
| 2–3 | Phase 2a | A | Auxiliary field reformulation |
| 3–5 | Phase 2b | A | One-loop V_eff computation |
| 4–5 | Phase 3a | B | NJL condensate setup |
| 5–7 | Phase 3b | B | Gap equation + vacuum energy |
| 6–8 | Phase 4 | C | Stress tensor + w(a) |
| 8–10 | Phase 5 | A+B+C | Stability audit |
| 10–12 | Phase 6 | C | Cosmological implementation |

**Decision gates:**
- **Month 5:** Does V_eff have a nontrivial minimum? (Go/No-Go for Track B)
- **Month 7:** Does the vacuum energy survive when spin density → 0? (Make-or-break)
- **Month 10:** Is the result radiatively stable? (Publish/revise decision)

---

## Paper Sequence

### Theory Paper 1 (Target: Month 8)
**"IR effective action and vacuum persistence in parity-odd Einstein-Cartan cosmology"**

Contents:
- Canonical action (Phase 1)
- Torsion elimination + auxiliary field reformulation
- One-loop effective potential
- Gap equation and condensate solution
- Vacuum energy at the minimum
- The IR persistence test

This paper answers: *does the mechanism work?*

### EFT Paper 2 (Target: Month 11)
**"Equation of state and radiative stability of torsion-induced vacuum energy"**

Contents:
- Stress-energy tensor from the effective action
- w(a) derivation
- Radiative stability analysis
- RG running
- Ghost/instability checks

This paper answers: *is the result robust?*

### Cosmology Validation Paper 3 (Target: Month 12+)
**"First-principles dark energy from spin-torsion cosmology: MCMC constraints with a theory-derived vacuum sector"**

Contents:
- Modified Boltzmann code with theory-derived dark energy
- MCMC fits to Planck + BAO + SN
- Comparison with phenomenological fits
- Updated predictions for next-generation surveys

This paper answers: *does it fit the data better or differently?*

---

## Compute Requirements

| Task | Resource | Time |
|------|----------|------|
| Symbolic computation (action, torsion elimination) | Mathematica / xAct | 2–4 weeks |
| Heat-kernel coefficients | Analytic (by hand or CAS) | 2–3 weeks |
| Gap equation (numerical) | Laptop Python/Julia | Days |
| V_eff numerical evaluation | Laptop | Days |
| CAMB module + MCMC | RunPod (32 vCPU) | ~1 week |

**Total compute cost:** Negligible. This is primarily a pen-and-paper / CAS program.

---

## Risk Assessment

| Risk | Probability | Mitigation |
|------|-------------|------------|
| No condensate forms (G_p too weak) | Medium | Try multiple fermion species; check gravitational catalysis |
| Condensate forms but vacuum energy = 0 | Medium | Check if fine-tuning is shifted, not removed |
| Result depends on UV cutoff (non-renormalizable) | High | Use proper regularization; acknowledge if unavoidable |
| w deviates significantly from −1 | Low-Medium | Interesting scientifically; revise paper accordingly |
| Calculation intractable beyond 1-loop | Low | 1-loop is sufficient for proof of concept |
| Author lacks technical depth in QFT-in-curved-spacetime | Real risk | Collaboration with specialist recommended |

---

## Collaboration Opportunities

This program would benefit enormously from collaboration with:

1. **Curved-spacetime QFT specialist** — for the heat-kernel / effective action computation
2. **NJL / condensed-matter-in-gravity expert** — for the gap equation in curved spacetime
3. **LQG phenomenologist** — for connecting to the Barbero-Immirzi sector

Potential collaborators to approach:
- Groups working on gravitational catalysis of chiral symmetry breaking
- Groups working on NJL models in de Sitter space
- Chattopadhyay (arXiv:2310.10405) — already computed one-loop in chiral EC gravity
