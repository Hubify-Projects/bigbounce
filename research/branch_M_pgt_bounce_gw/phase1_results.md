# Branch M Phase 1 Results: PGT Bounce GW Spectrum

**Date:** 2026-03-16

---

## Verdict: PGT_GW_GENERIC

---

## What Was Computed

The gravitational wave spectrum from the PGT lower-scale bounce
was derived from first principles:

1. Background evolution a(t) = a_b(1+4α²t²)^{1/4} with
   α = m_T√(8π/3)
2. Tensor mode equation μ'' + (k² - a''/a)μ = 0
3. Bogoliubov coefficient |β_k|² as function of k/k_b
4. GW energy density Ω_GW(f) h² = 1.6 × 10⁻⁵ × (m_T/M_Pl)² × |β|²
5. Comparison with inflation, LQC, and phase transitions
6. Overlay with LIGO, ET, LISA, DECIGO, PTA sensitivity curves

---

## Key Results

### Result 1: The spectrum shape is universal

The GW spectrum from the PGT radiation bounce is a one-parameter
family indexed by m_T:

```
Ω_GW(f) h² = 5 × 10⁻⁶ × (m_T/M_Pl)² × S(f/f_b)
```

Shape function S(x):
- x ≪ 1: S ≈ 1 (flat plateau, n_T = 0)
- x ~ 1: S oscillatory with 1/x² envelope
- x ≫ 1: S ~ exp(-αx) with α ~ 2–4

Bounce frequency: f_b ≈ 2.6 × 10¹⁰ × (m_T/M_Pl)^{1/2} Hz.

### Result 2: The amplitude is (m_T/M_Pl)², NOT O(1)

The Phase 2 (Branch L) estimate of Ω ~ 10⁻⁵ × ε with ε ~ O(1)
was INCORRECT. The correct efficiency for vacuum amplification:

```
ε = ρ_GW / ρ_crit ~ m_T² / M_Pl² = (m_T/M_Pl)²
```

This is the standard graviton production efficiency: O(1) gravitons
per mode, but each graviton carries energy ~ m_T while the total
budget is ~ m_T M_Pl. The ratio is (m_T/M_Pl)².

**This corrects the overly optimistic estimate from Branch L Phase 2.**

### Result 3: The amplitude-frequency tradeoff is fatal

```
Ω_peak ~ (f_b/f_Pl)⁴
```

Lowering f_b by a factor of 10 reduces the amplitude by 10⁴.
Moving from f_Pl ~ 10¹⁰ Hz to LISA frequencies (10⁻³ Hz)
requires 10¹³ in frequency, giving 10⁵² in amplitude suppression.

**This tradeoff is universal to ALL vacuum-amplification bounces.**

### Result 4: Minimum gap to any detector is 10¹⁷

| Best case | Value |
|-----------|-------|
| Optimal m_T | ~10⁷ GeV |
| Corresponding f_b | ~2.4 × 10⁴ Hz |
| Ω_peak h² | ~3 × 10⁻³⁰ |
| Best detector | ET (Ω ~ 10⁻¹³) |
| **Gap** | **10¹⁷** |

Even the most favorable parameter choice leaves the signal 17
orders of magnitude below the best future detector.

### Result 5: The spectrum IS distinctive — but undetectable

The bounce spectrum (flat + exponential cutoff) differs qualitatively
from:
- Inflation (near-flat power law, no cutoff in detector bands)
- Phase transitions (f³ rise, f⁻¹ decay, sharp peak)
- Cosmic strings (flat, no cutoff)

But these shape differences are moot because the amplitude is 10¹⁷+
below any detector threshold.

### Result 6: The result is NOT PGT-specific

The amplitude-frequency tradeoff Ω ∝ f_b⁴ applies to:
- PGT bounce
- LQC bounce
- Ekpyrotic bounce
- Any bounce producing GWs via vacuum amplification

The specific bounce model only affects the oscillation fine
structure near f_b — a sub-leading feature that is even further
from detectability than the smooth background.

---

## Correction to Branch L Phase 2

Branch L Phase 2 concluded PGT_BOUNCE_CONSTRAINED based on the
estimate Ω ~ 10⁻⁵ (detectable but generic). Branch M corrects
this:

| Estimate | Value | Source |
|----------|-------|--------|
| Branch L Phase 2 | Ω ~ 10⁻⁵ | ε ~ O(1) (WRONG) |
| Branch M (correct) | Ω ~ 10⁻⁵ × (m_T/M_Pl)² | Bogoliubov calculation |
| Actual peak | 10⁻³⁰ to 10⁻⁶² | Depending on m_T |

The error in Branch L was assuming the bounce converts O(1) of its
energy to GWs. The correct conversion efficiency is (m_T/M_Pl)²,
which is the standard vacuum amplification factor. This applies
to inflation too: the inflationary GW background has
Ω ~ 10⁻⁵ × r, with r = 16(H_inf/M_Pl)² — the same (H/M_Pl)²
suppression.

---

## Why GENERIC (Not PROMISING or WEAK)

### Not PROMISING because:
The signal is 17+ orders below any detector sensitivity. There is
no parameter choice, detector improvement, or analysis technique
that bridges a 10¹⁷ gap. The spectrum is undetectable in the most
literal sense.

### Not WEAK because:
The spectrum IS calculable, well-defined, and theoretically
complete. It provides a precise prediction — just an unobservable
one.

### GENERIC because:
The spectral shape (flat + exponential cutoff) and the amplitude
scaling (Ω ∝ (H_b/M_Pl)² ∝ f_b⁴) are UNIVERSAL features of
vacuum amplification in ANY bounce cosmology. Nothing about the
PGT bounce produces a distinct signature that could identify the
torsion mechanism specifically.

The PGT bounce GW spectrum is the SAME as any other radiation
bounce GW spectrum at the same energy scale, up to undetectable
oscillatory sub-structure.

---

## The Twelfth Barrier

> **Barrier 12 (Vacuum amplification ceiling):** The GW energy
> density from vacuum amplification at a cosmological bounce
> satisfies Ω_GW ∝ (H_bounce/M_Pl)² ∝ (f_b/f_Pl)⁴. This
> fundamental bound ensures that any bounce whose features fall
> in a GW detector band (f < 10⁴ Hz) produces a signal at
> least 10¹⁷ below sensitivity. The bound is model-independent
> and applies to all bounce mechanisms relying on vacuum
> amplification.

---

## Complete Branch Status

| Branch | Sector | Verdict | Root cause |
|--------|--------|---------|-----------|
| A–G | Direct bounce → DE | CLOSED | 7 barriers |
| H | Tensor spectrum/parity | CLOSED | Amplitude + parity |
| I | Bounce-compatible DE | WEAK | Scale separation |
| J | State selection | CLOSED | Liouville |
| K | Scalar perturbations | GENERIC | Time-reversal symmetry |
| L (Phase 1) | UV→IR bridge screening | MIXED | Specificity dilemma |
| L (Phase 2) | PGT parameter space | CONSTRAINED | Mass-coupling lock |
| **M** | **PGT bounce GW spectrum** | **GENERIC** | **Vacuum amplification ceiling** |

---

## Twelve Structural Barriers

1. Mass-coupling lock (A) — propagating torsion
2. Topological-shift duality (B) — pseudoscalar protection
3. Scalar-tensor universality (C) — FRW reduction
4. Planck suppression (D) — connection coupling
5. Scale separation (E) — global integrals
6. Attractor-sensitivity dilemma (F) — initial conditions
7. Parameter immunity (G) — vacuum selection
8. Parity-even effective interaction (H) — tensor chirality
9. Hamiltonian phase-space conservation (J) — state selection
10. UV→IR specificity dilemma (L₁) — generic vs non-minimal
11. Decoupling universality (L₂) — light gauge fields decouple
12. **Vacuum amplification ceiling (M)** — Ω ∝ (H/M_Pl)²

---

## Implications for the Overall Program

### What Branch M has established

1. The PGT lower-scale bounce has a well-defined, one-parameter
   family of GW spectra.

2. The spectrum is qualitatively distinctive (vs inflation) but
   quantitatively undetectable.

3. The undetectability is NOT due to the mass-coupling lock
   (Barrier 11) but to the vacuum amplification ceiling
   (Barrier 12) — a more fundamental limit that applies to
   ALL bounce models.

4. No parameter choice within PGT (or any other bounce theory)
   can overcome this ceiling for vacuum-amplification GWs.

### What remains

The only escape from the vacuum amplification ceiling would be
a NON-VACUUM GW source:
- Pre-bounce contraction that coherently amplifies tensor modes
  (requires specifying contraction model — outside minimal bounce)
- Post-bounce particle production / phase transitions
  (standard cosmology, not bounce-specific)
- Topological defect formation (not bounce-specific)

All of these either require additional physics beyond the bounce
or are not bounce-specific.

### Recommended next move

The spin-torsion bounce program (Branches A–M) has now been
comprehensively explored:
- Minimal model: observationally inert (Branches A–K)
- PGT extension: ghost-free but generic (Branches L–M)
- Twelve structural barriers cataloged
- Every observable channel examined (DE, tensors, scalars,
  parity, state selection, GW background)

**The program is ready for a comprehensive write-up.** The
accumulated results constitute a complete theoretical
characterization of the spin-torsion bounce and its observable
prospects — a publishable negative result that closes a natural
research direction.

---

## Summary

| Item | Result |
|------|--------|
| Spectrum shape | Flat plateau + exponential cutoff |
| Spectral tilt (low f) | n_T = 0 (scale-invariant) |
| Peak amplitude | 5 × 10⁻⁶ × (m_T/M_Pl)² |
| Cutoff frequency | f_b ≈ 2.6 × 10¹⁰ (m_T/M_Pl)^{1/2} Hz |
| Minimum detector gap | **10¹⁷** (ET at f ~ 10⁴ Hz) |
| Distinctive vs inflation? | YES (in shape), NO (in practice) |
| Distinctive vs LQC? | Marginally (oscillation fine structure) |
| Distinctive vs generic bounce? | NO (same shape, same amplitude) |
| Detectable by any planned detector? | **NO** |
| Root cause | Vacuum amplification ceiling: Ω ∝ (H/M_Pl)² |
| New barrier | **Barrier 12: vacuum amplification ceiling** |
| Branch M verdict | **PGT_GW_GENERIC** |
