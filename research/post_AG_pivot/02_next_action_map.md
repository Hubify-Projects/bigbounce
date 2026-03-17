# Post-A–G Pivot: Next Action Map

**Date:** 2026-03-15

---

## Single Best Computation

**Tensor perturbation spectrum through the spin-torsion bounce.**

Why:
- Blue-tilted GW spectrum is THE smoking gun for bounce cosmology
- Distinguishes bounce from inflation (which predicts red tilt)
- Well-defined computation: ODE for tensor modes on modified
  Friedmann background
- Does not require specifying the full pre-bounce history (the
  bounce itself determines the transfer matrix)
- Result is independent of the (closed) DE program

What to compute:
1. Background: a(η) from H² = (8πG/3)(ρ - ρ²/ρ_crit)
2. Tensor equation: h'' + 2(a'/a)h' + k²h = 0
3. Bogoliubov coefficients: β_k from mode matching
4. Spectrum: P_T(k) = (k³/2π²)|β_k|² × (bounce amplification)

---

## Best Theory Scan

**Horndeski DE stability at the bounce (Test I-1).**

Why:
- Most DE theories are trivially compatible with the bounce
- Horndeski models are the exception: their stability conditions
  involve background curvature, which is extreme at the bounce
- A nontrivial exclusion of Horndeski subclasses would be a
  genuine new result
- Publishable regardless of outcome

---

## What to STOP Doing

| Activity | Status | Action |
|----------|--------|--------|
| Testing bounce → DE mechanisms | CLOSED (A–G) | STOP |
| Looking for geometric dark energy | CLOSED | STOP |
| Tweaking EFT parameters | CLOSED (generic by C) | STOP |
| Running MCMC on phenomenological model | NOT NEEDED NOW | PAUSE |
| Editing Paper 1 | STABLE | PAUSE until new results |

---

## MCMC Timing

**No new MCMC is needed now.**

The existing MCMC infrastructure (236,622 samples, 64 chains)
constrains the phenomenological scalar-tensor parameters. These
constraints remain valid but are now understood as GENERIC (not
geometric).

New MCMC becomes relevant ONLY when:
1. A specific bounce prediction (e.g., n_T from Priority 1) is
   computed analytically
2. That prediction maps onto an observable parameter with existing
   data constraints
3. The parameter space is large enough (>3 dimensions) to require
   sampling

For the tensor perturbation computation (Priority 1), the result
is an ANALYTIC FUNCTION P_T(k), not a high-dimensional parameter
space. MCMC is not the right tool.

For Horndeski compatibility (Test I-1), the stability conditions
are ALGEBRAIC inequalities in the Horndeski functions evaluated
at the bounce. Again, not a sampling problem.

**Earliest possible MCMC need:** When combining bounce tensor
spectrum + CMB data to constrain bounce parameters (ρ_crit, pre-
bounce equation of state). Estimated: 4–8 weeks from now.

---

## Timeline

```
Week 1–2:   Tensor perturbation computation (Priority 1)
Week 2–3:   Horndeski stability analysis (Test I-1)
Week 3–4:   Assess results, decide next step
Week 4–6:   Parity violation / leptogenesis (Priority 2)
            OR K-essence stability (Test I-3)
            [depends on Week 1–3 results]
Week 6–10:  Full scalar perturbation theory (Priority 3)
            OR publication of no-go results
```

---

## Decision Tree

```
Tensor spectrum computed
├── Blue tilt observable (f < 10⁴ Hz) → Branch H active, compute
│   ├── Compatible with CMB → full paper
│   └── Incompatible → revise pre-bounce model
├── Blue tilt at f > 10¹⁰ Hz only → Branch H theoretical only
│   └── Shift to Branch I and/or no-go paper
└── Degenerate with inflation → Branch H closed
    └── Focus entirely on no-go paper + Branch I

Horndeski stability
├── Nontrivial exclusion found → Branch I paper
│   └── Map excluded Horndeski parameter space
├── All Horndeski trivially compatible → Branch I weak
│   └── Test massive gravity (I-4) or close Branch I
└── Mixed results → deeper investigation needed
```
