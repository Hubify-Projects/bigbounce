# 02: Action-by-Action Comparison

## The Three Critical Differences

### Difference 1: Leading Vertex Coefficient

| | Our file 02 (conformal time) | Cai Eq. 15 (cosmic time → conformal) |
|--|-----|-----|
| ζζ'² coefficient | **ε² = 9/4** | **(ε²−ε³/2) = 9/16** |
| Ratio | 4 : 1 | — |

Cai's Eq. 15 in cosmic time: L₃ ⊃ **(ε²−ε³/2)**·a³·ζ·ζ̇²
Converting to conformal time (ζ̇ = ζ'/a, dt = a·dη): **(ε²−ε³/2)**·a²·ζ·ζ'²

At ε = 3/2: (9/4 − 27/16) = **(9/16)** — our coefficient is **4× too large**.

### Difference 2: Mode Function Phase Convention

| | Our mode function | Cai's mode function (Eq. 23) |
|--|-----|-----|
| Phase | e^{**−ik**η} | e^{**+ik**η} |
| Superhorizon limit | ζ_k → **−i**/(√(6k³)η³) [imaginary] | u_k → **A·i**/(√(2k³)η³) [imaginary, but conjugate phase] |
| External legs g* | purely imaginary | purely REAL (after X* convention) |
| Im[ext × I]_superhorizon | **= 0** (proven by SymPy) | **≠ 0** (ext real × I imaginary) |

**This is the most consequential difference.** It determines whether the bispectrum is superhorizon-dominated (Cai, giving large f_NL) or horizon-crossing-dominated (us, giving small f_NL).

Relation: u_k(Cai) = A·√3 · conj[ζ_k(ours)]

Under complex conjugation of the mode function:
- Power spectrum: P = |ζ|² = |ζ*|² → **UNCHANGED** ✓
- Bispectrum: Im[ext × I] → **−Im[ext × I]** → **SIGN FLIPS**
- Superhorizon contribution: goes from **zero** (our convention) to **nonzero** (Cai's convention)

### Difference 3: χ-Sector Structure

| | Our file 02 | Cai Eq. 15 |
|--|-----|-----|
| χ definition | ∇²χ = (3/2)a²ζ' (Maldacena constraint) | χ ≡ ∂⁻²ζ̇ (inverse Laplacian of cosmic-time derivative) |
| Our χ in terms of Cai's | our_χ = (3/2)a³ · Cai_χ | — |
| χ-sector terms | ∂²ζ(∂χ)², ∂²ζ·χ² | ζ·(∂ᵢ∂ⱼχ)² |
| Structure | Laplacian on ζ, plain/gradient χ | Plain ζ, double-gradient χ |
| a-dependence after sub | **a⁴ = η⁸** (spurious!) | **a² = η⁴** (correct) |

Our χ definition carries extra factors of a², producing the η⁸ divergence that made the χ-sector numerically unstable. **This was an artifact of using the wrong χ definition.**

### Summary Table

| Term | Our version | Cai's version | Status |
|------|------------|--------------|--------|
| ζζ'² coeff | ε² = 9/4 | (ε²−ε³/2) = 9/16 | **WRONG by 4×** |
| ζ(∂ζ)² | ε²a² (included) | ε²a (omitted as secondary) | Different treatment |
| ζ' coupling | −2εa²ζ'(∂ζ)(∂χ) | −2ε²a²ζ'(∂ζ)(∂χ) | **Different ε power** |
| ζ²ζ' vertex | Present (our T4) | **Absent** | Missing in Cai |
| χ² sector | ∂²ζ(∂χ)² and ∂²ζχ² | ζ(∂ᵢ∂ⱼχ)² | **Completely different** |
| Mode function | e^{−ikη} | e^{+ikη} | **Conjugate** |
| Field redef | Standard Maldacena (5ε/6) | Growing-mode f(ζ) (Eq. 27-28) | **Different** |

## Root Cause

**Our computation used a DIFFERENT cubic action AND different mode functions than Cai.**
The cubic action was reconstructed from a conformal-time version of Maldacena (2003) that differs from Cai's cosmic-time formulation (which follows Maldacena's original cosmic-time notation more closely). The mode function uses the opposite complex branch.

Both formalisms should yield the same physics when correctly implemented, but our transcription introduced systematic errors in the coefficients and variable definitions.
