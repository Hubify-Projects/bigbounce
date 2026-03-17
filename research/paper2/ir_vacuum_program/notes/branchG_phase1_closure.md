# Branch G Phase 1 Closure: FM-G6 Fires

**Date:** 2026-03-13
**Verdict:** FM-G6 — Trivial one-loop reduction. Branch G v1 closes at Phase 1.
**Confidence:** HIGH — structural argument confirmed by two independent literature checks

---

## The Central Question

> Under what precise circumstances can γ enter Γ_eff[e] at the stated approximation order (strict one-loop, Approach B)?

## Answer

**γ does not enter.** At strict one-loop after torsion elimination, the fermion determinant is the standard curved-space Dirac determinant. It has zero γ-dependence.

---

## The Structural Argument

After exact torsion elimination, the reduced action is:

```
S_reduced = S_EH[e] + S_Dirac^free[e, ψ] + S_4f[e, ψ; γ]
```

The free Dirac term uses the Levi-Civita connection ∇̊. The entire γ-dependence resides in S_4f, the four-fermion interaction.

At strict one-loop, the Dirac operator whose determinant is computed is:

```
D̸ = iγ^μ ∇̊_μ
```

This is the standard curved-space Dirac operator. It does not depend on γ. The four-fermion term S_4f is quartic in ψ and contributes only at two loops or beyond.

Therefore: **Γ^(1-loop)_ferm[e] is γ-independent as a functional.** The Seeley-DeWitt coefficients (a₀, a₁, a₂, ...) are the standard ones for a spin-½ field on a Riemannian background, with no γ-dependence.

---

## Three Candidate Channels — All Closed

### Channel (a): Modified background equations — EXCLUDED

γ enters the classical background solution (the bounce geometry depends on γ through the four-fermion stress-energy). The one-loop determinant evaluated ON this background inherits indirect γ-dependence. But this is γ-dependence of the field configuration, not the effective action as a functional. Per the frozen canonical statement, this does not count as novel Holst content.

### Channel (b): Parity-odd sector / η-invariant — CLOSED

The η-invariant (APS) is computed from the spectrum of the Dirac operator D̸ = iγ^μ ∇̊_μ, which is γ-independent. The gravitational chiral anomaly ∂_μ J^μ₅ = (1/384π²)R^{ab}_{cd}R̃^{cd}_{ab} is a property of the Dirac operator, not of the Barbero-Immirzi parameter.

Furthermore:
- On homogeneous FRW backgrounds, the Pontryagin density P₄ = 0 (FRW is conformally flat)
- The Pontryagin term is curvature-local, not vacuum-like — it vanishes as R → 0
- Even if nonzero on some background, it has no γ-dependence

### Channel (c): Functional measure corrections — CLOSED

Torsion elimination is performed at the classical level (algebraic substitution of ω's equation of motion). No change of integration variable in the fermion sector occurs. The standard treatment (Shapiro 2002, Freidel+ 2005) performs this elimination without measure corrections.

The path integral over ω is Gaussian in ω (the action is at most quadratic in ω). The resulting determinant depends on the tetrad e but not on ψ, so it modifies the gravitational measure, not the fermion determinant.

---

## Literature Confirmation

### Chattopadhyay (2023) [2310.10405]

This paper computes the one-loop effective action in chiral Einstein-Cartan gravity. Key findings:

- **It computes the GRAVITON loop** (tetrad + connection fluctuations + ghosts), not the fermion loop
- **No fermions are included** in the one-loop computation
- The Barbero-Immirzi parameter **does not appear** in the paper
- The chiral formulation uses self-dual variables (γ = ±i in complexified theory), not a general real γ
- The paper finds one-loop divergences proportional to R²_μνρσ with a coefficient different from metric GR — but this is about quantizing gravity itself, not about fermion determinants
- Coupling fermions to the chiral action is listed as **future work** (Discussion, p.20)

**Relevance to Branch G v1:** None. Different computation (graviton loop, not fermion loop).

### Shapiro & Teixeira (2014) [1402.4854]

This paper computes one-loop divergences in quantum Einstein-Cartan theory with the Holst term AND fermion currents. Key findings:

- **Fermions are treated as EXTERNAL CURRENTS** (V^μ, A^μ), not dynamical quantum fields
- **The one-loop computation is for the GRAVITON sector** (metric fluctuations h_μν)
- **Torsion is integrated out classically** — the path integral over torsion fluctuations is non-derivative Gaussian, equivalent to using the classical equation of motion
- **γ-dependent divergences DO appear** (eq. 34), but they come from the graviton loop with γ entering through the modified graviton vertices after torsion elimination
- The ghost contribution is "identical to the standard one for Einstein gravity" and does not depend on torsion or external currents

**Relevance to Branch G v1:** Confirms that γ can enter quantum corrections, but ONLY through graviton loops (not fermion loops). The fermion determinant itself is γ-independent.

**Critical distinction:** Shapiro & Teixeira's γ-dependent results arise from quantizing the metric in the presence of external fermion currents that have been modified by γ-dependent torsion elimination. This is:
- A different one-loop object (graviton determinant, not fermion determinant)
- Fermions are classical backgrounds, not quantum fields being integrated out
- The γ-dependence enters through the graviton propagator/vertices, not the fermion operator

---

## Novel Holst Content Criterion — NOT MET

From the frozen canonical statement:

> "Branch G counts as nontrivially alive only if, at the stated approximation order (strict one-loop, Approach B), the renormalized effective action Γ_eff[e] contains at least one finite or regulator-robust term whose existence, sign, or classification depends nontrivially on finite γ and either disappears or changes qualitatively in the γ → ∞ Einstein-Cartan limit."

**No such term exists.** The strict one-loop fermion determinant is the standard Seeley-DeWitt expansion for a Dirac field on a Riemannian background. All coefficients (a₀, a₁, a₂, ...) are γ-independent. They are determined by the spin of the field (½) and the spacetime dimension (4), nothing else.

---

## FM-G6 Declaration

**FM-G6 fires.** After exact torsion elimination, the strict one-loop effective action reduces to the standard curved-space Dirac determinant with no physically meaningful finite-γ dependence beyond ordinary renormalization bookkeeping. All three candidate channels (modified background, parity-odd sector, measure corrections) yield no novel Holst content.

**Branch G v1 closes at Phase 1 without proceeding to Gates G1–G3.**

---

## What This Means

Combined with Track B:

| Route | Result | Approximation |
|-------|--------|---------------|
| Track B (NJL condensate) | Gate 1 failed: S/P channel repulsive at γ = 0.274 | Fierz + gap equation + one-loop V_eff |
| Branch G v1 (strict one-loop Γ_eff) | FM-G6: fermion determinant is γ-independent | Strict one-loop after torsion elimination |

**Together:** In the minimal EC+Holst+Dirac framework, at the stated approximation orders, neither the condensate route nor the strict one-loop effective-action route yields novel vacuum physics from the Holst sector.

---

## What Is NOT Ruled Out

Branch G v1 closes, but the following routes remain logically open (each would require a new branch definition):

1. **Graviton one-loop with fermion currents** (Shapiro & Teixeira approach): γ DOES enter. But this is a graviton loop computation, not a fermion loop. It requires quantizing the metric, which is a much harder program.

2. **Beyond-one-loop / Approach A**: The four-fermion interaction S_4f contributes at two loops. Or via Hubbard-Stratonovich + saddle point (which is effectively a resummation). γ enters through these channels. But Approach A was explicitly excluded from Branch G v1.

3. **Non-perturbative effects**: Instantons, tunneling, non-perturbative condensates. Not tested.

4. **Non-minimal couplings**: Additional torsion-matter couplings beyond minimal EC+Holst+Dirac. Not tested.

None of these are automatically authorized. Each would require its own canonical problem statement.

---

## Artifacts

| File | Content |
|------|---------|
| `derivations/branchG_phase1_operator_analysis.py` | Systematic analysis of three candidate channels |
| `notes/branchG_phase1_closure.md` | This closure document |

---

## Impact on Paper 1

**None.** Paper 1 already labels w = −1 as an assumption. The Branch G closure (like Track B before it) reinforces the phenomenological framing. The paper is correct as written.
