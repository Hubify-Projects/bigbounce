# Phase 2 — Cycle Four-Volume

**Date:** 2026-03-15

---

## Goal

Compute V₄ = ∫ a³(t) dt over one complete cycle and determine its
dependence on Λ and matter content.

---

## The Obstacle From Task 1

Task 1 showed that no viable cyclic cosmology exists with both a
spin-torsion bounce AND Λ ~ Λ_obs:

- k = 0, Λ > 0: no turnaround, no cycle
- k = +1, Λ ~ Λ_obs: a_min ~ 10²⁶ m, matter content absurd
- k = +1, Λ ~ M_Pl²: Λ wrong by 10¹²²

Nevertheless, we proceed with FORMAL estimates to determine what
V₄ would be IF a cycle existed, to see whether the self-consistency
equation has interesting structure.

---

## Formal Cycle Model (k = +1, Neglecting Spin-Torsion)

For a closed FRW universe with matter (ρ_m) and Λ:

```
H² = (8πG/3)ρ_m/a³ - 1/a² + Λ/3
```

### Turnaround (H = 0, expansion → contraction)

```
0 = (8πG/3)ρ_m/a_max³ - 1/a_max² + Λ/3
```

### Cycle duration

For a matter-dominated closed universe WITHOUT Λ:
```
H² = (8πG/3)ρ_m/a³ - 1/a²
```

Parametric solution:
```
a(η) = a_max/2 (1 - cos η)
t(η) = a_max/2 (η - sin η)
```

where η ∈ [0, 2π] is conformal time through one cycle.

a_max = (8πG/3) ρ_m    [in appropriate units]

Cycle duration: T_cycle = π a_max

### Four-volume (k = +1, matter only)

```
V₄ = ∫₀^{T_cycle} dt a³(t) × V₃(a)
```

For k = +1: V₃(a) = 2π² a³ (volume of a 3-sphere of radius a).
So the physical spatial volume is 2π² a³.

The 4-volume per cycle:
```
V₄ = 2π² ∫₀^{2π} dη × a³ × (dt/dη) × a³(η)
   = 2π² ∫₀^{2π} dη × a(η)³ × a(η)/2 × (1 - cos η) × a(η)²
```

Wait, let me be more careful. The FRW metric for k = +1:
```
ds² = -dt² + a²(t)[dχ² + sin²χ (dθ² + sin²θ dφ²)]
```

√g = a³(t) sin²χ sinθ

∫ d³x √g₃ = 2π² a³(t)    [volume of unit 3-sphere × a³]

So:
```
V₄ = ∫ dt × 2π² a³(t)
```

Using the parametric solution:
```
dt = (a_max/2)(1 - cos η) dη = a(η) dη

V₄ = 2π² ∫₀^{2π} dη × a(η) × a(η)³
   = 2π² ∫₀^{2π} dη × a(η)⁴
   = 2π² × (a_max/2)⁴ ∫₀^{2π} dη (1-cos η)⁴
```

Compute:
```
∫₀^{2π} (1-cosη)⁴ dη = ∫₀^{2π} [1 - 4cosη + 6cos²η - 4cos³η + cos⁴η] dη
= 2π - 0 + 6π - 0 + 3π/4 × (8/3)
```

Actually, let me use standard integrals:
```
∫₀^{2π} cos^n η dη:
n=0: 2π
n=1: 0
n=2: π
n=3: 0
n=4: 3π/4
```

So:
```
∫₀^{2π} (1-cosη)⁴ dη = 2π - 0 + 6π - 0 + 3π/4 = 2π + 6π + 3π/4
= 8π + 3π/4 = 35π/4
```

Therefore:
```
V₄ = 2π² × (a_max/2)⁴ × 35π/4
   = 2π² × a_max⁴/16 × 35π/4
   = 35π³ a_max⁴ / 32
```

### Order of magnitude

```
V₄ ~ a_max⁴
```

The four-volume per cycle is dominated by the era near maximum
expansion, scaling as a_max⁴.

---

## Dependence on Λ

### With Λ > 0 (small)

Adding Λ to the closed matter universe: the turnaround occurs at
a smaller a_max (Λ delays recollapse). For Λ close to the critical
value Λ_crit:

```
Λ_crit = (4/9)(8πGρ_m)²/(3k)²    [Einstein static universe value]
```

At Λ = Λ_crit: the universe approaches the Einstein static solution
(a = const). a_max → ∞ and V₄ → ∞.

For Λ slightly below Λ_crit: a_max is very large and V₄ ∝ a_max⁴
is enormous.

For Λ = 0: a_max = (8πG/3)ρ_m and V₄ ~ a_max⁴ is finite.

For Λ > Λ_crit: no turnaround. V₄ → ∞. No cycle.

### V₄ as a function of Λ

```
V₄(Λ) ~ [a_max(Λ)]⁴

a_max(Λ) increases as Λ → Λ_crit from below
a_max(Λ) → ∞ as Λ → Λ_crit
V₄(Λ) → ∞ as Λ → Λ_crit
```

This is a monotonically INCREASING function of Λ (for Λ < Λ_crit).

---

## Dependence on Bounce Parameters

The bounce contributes V₄^bounce ~ a_min⁴ × t_Pl (from Foundation E
analysis). For a Planck-scale bounce: a_min ~ l_Pl, so
V₄^bounce ~ l_Pl⁵ ~ 10⁻¹⁷⁵ m⁴.

Compare to the cycle total: V₄ ~ a_max⁴. For a_max ~ 10²⁶ m:
V₄ ~ 10¹⁰⁴ m⁴.

```
V₄^bounce / V₄^cycle ~ (l_Pl/a_max)⁴ ~ 10⁻²⁸⁰
```

**The bounce contributes negligibly to V₄.** The four-volume is
entirely dominated by the turnaround era (maximum expansion).

This confirms Foundation E's scale-separation result in the cyclic
context: the bounce is irrelevant for volume-weighted quantities.

---

## Summary

| Quantity | Estimate | Depends on |
|----------|----------|-----------|
| V₄ per cycle | ~ 35π³ a_max⁴ / 32 | a_max (turnaround radius) |
| a_max | Determined by ρ_m, Λ, k | Matter content and Λ |
| V₄ dependence on Λ | Monotonically increasing | V₄ → ∞ as Λ → Λ_crit |
| Bounce contribution to V₄ | ~ l_Pl⁵ ~ 10⁻¹⁷⁵ m⁴ | Negligible |

**The four-volume per cycle is determined by the turnaround physics,
not by the bounce. V₄ depends on Λ (through a_max) but the bounce
does not constrain this relationship.**
