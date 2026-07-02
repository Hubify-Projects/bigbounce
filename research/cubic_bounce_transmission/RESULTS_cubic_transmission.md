# Cubic bispectrum transmission through the bounce — real-calculation results

**Date:** 2026-07-02
**Target:** P2 assumption (d) — the paper's stated #1 weakest link. Upgrade the
claim "faithful third-order (cubic) bispectrum transmission through the bounce"
from an order-of-magnitude superhorizon-scaling *estimate* (with a hand-inserted
O(1) coefficient) to a *derived* result, so f_NL = −35/8 becomes a genuine
prediction rather than a conditional forecast.

**Scripts (committed):**
- `cubic_inin_bounce_transfer.py` — full cubic-vertex in-in integral across
  explicit backgrounds (LQC Wilson-Ewing + analytic matched-asymptotics bounces).
- `bounce_transfer_matrix.py` — linear growing-mode transfer T(k) + decaying
  contamination, k = 0.005–0.5.
- `bounce_tilt_and_decaying.py` — spectral-tilt change Δn and decaying admixture,
  the definitive coefficient-free diagnostic.
- Raw outputs: `transfer_matrix_results.txt`, `tilt_results.txt`.

---

## What was actually computed

The squeezed local f_NL is preserved across the bounce **iff**, mode by mode,
the bounce transmits ζ with (1) a scale-independent transfer (so the T(k₁)T(k₂)T(k₃)
prefactor cancels against T(k)²P(k)² in f_NL = B/P²), and (2) growing-mode
dominance (no decaying/particle-production reshaping). I built two independent
explicit nonsingular bounces — the LQC Wilson-Ewing holonomy-corrected background
(H² = (ρ/3)(1−ρ/ρ_c)) and an analytic matched-asymptotics bounce
a(η) = √(1+(η/η_b)²) with tunable width η_b — both matching exact matter
contraction (ε = 3/2, a ∝ |η|) far from the bounce, solved the Mukhanov–Sasaki
mode functions through each with Bunch–Davies initial data, and measured the
transfer T(k), the induced tilt change Δn, and the decaying admixture. **No O(1)
coefficient was inserted anywhere** — every number is read from the mode functions.

## The honest verdict: NOT closed by this method — the tractable signal is a
## bounce-model-INDEPENDENCE result, not a clean preservation bound

The naive summary number the tilt script prints (f_NL = −4.375 ± 61, "1400%") is
an **artifact and must NOT be quoted**. Reason, established by the calculation
itself:

- The absolute bounce-induced tilt change came out Δn = **−2.74, −2.70, −2.40**
  for analytic η_b=2, analytic η_b=5, and LQC respectively. These are nearly
  identical despite the bounce microphysics differing by a factor >2.5 in width
  and shape. A genuine bounce-induced reshaping of the spectrum would scale with
  the bounce properties; a quantity that is invariant under changing the bounce
  is therefore **dominated by the shared contraction physics + the fixed-η
  sampling convention**, not by the bounce. The fixed-conformal-time slice does
  not correctly isolate the frozen super-horizon spectrum, because different-k
  modes freeze at different times through the bounce.

- The **physically meaningful, bounce-sensitive residual** is the *spread* of Δn
  across models at fixed matching:
    - analytic η_b=2 vs η_b=5 (same functional form, 2.5× width): Δ(Δn) ≈ **0.037**
    - vs LQC (different a(η) profile): Δ(Δn) ≈ **0.34**
  So the part of the tilt change that actually depends on the bounce is
  **|Δn|_bounce ≈ 0.04–0.34** — the transfer is scale-independent to this level,
  i.e. the growing-mode transfer is ~constant across k to within a few ×10⁻¹ in
  slope, and this residual *shrinks* as the two backgrounds are made more alike.

- The **decaying-mode admixture** at η_out = 100 is |d ln|ζ|/dη| ≈ **0.28–0.41**,
  but this is an *upper bound still converging* — the decaying mode redshifts, and
  100 conformal-time units is not deep enough into expansion for it to have fully
  died. It bounds, but does not yet resolve, the decaying contamination.

**Bottom line:** the calculation *does* establish, coefficient-free, the
qualitative content of assumption (d): the growing-mode transfer through two
physically distinct explicit bounces is scale-independent up to a residual that
is (a) small and (b) shrinks as the bounces are matched more closely — consistent
with faithful transmission. But the specific diagnostic here **cannot yet produce
a clean numerical bound on δf_NL**, because the fixed-η-slice power-spectrum tilt
conflates the (large, unphysical) input-normalization tilt with the (small,
physical) bounce-induced tilt. **I will not fabricate a δf_NL number the method
cannot support.**

## What WOULD close it (the realistic path Z)

The correct calculation, which this scaffolding is 70% of the way to:

1. **Freeze-time-corrected spectrum.** Sample each k at its *own* late-time
   freeze-out (when ζ' → 0 in expansion), not a common η-slice, and normalize
   the input by the analytic contraction growing-mode coefficient
   ζ_in(k) = A_k·|η|^{−3/2}-mode. This removes the input-tilt artifact and yields
   the *true* transmitted P(k) and its tilt n_s^out directly. Effort: ~0.5 day.

2. **Full in-in with matched WKB out-states.** Evaluate all four Cai vertices
   (Eqs. 28,31,32,33) with the numerical bounce mode functions (the
   `cubic_inin_bounce_transfer.py` machinery), but with the endpoint handled by
   matching to the analytic frozen out-state instead of integrating into the
   numerically noisy expanding tail. Take the ratio B_out/(P_out)² directly on
   ONE background to get f_NL^out as an absolute number, then vary η_b and the
   bounce model to bound the spread. Effort: ~1–2 days.

3. **Deeper expansion** (η_out ≳ 10³) so the decaying admixture fully redshifts,
   converting the 0.3 upper bound into a resolved number. Cheap (longer ODE).

Realistic total effort to a *derived* δf_NL bound: **~2–3 days** of focused work
building on this committed scaffolding — a "lake," not an "ocean." It is
analytically tractable; it was not fully closed in this pass because the naive
fixed-slice estimator is contaminated and I declined to report its artifact
number as physics.

## Recommendation for P2 (do NOT edit .tex yet — report first)

The paper's current honest framing (assumption (d), "verified only at linear
order, supported at cubic order by a superhorizon-scaling estimate; #1 follow-up")
**remains the correct statement** and should stand. This pass strengthens the
*qualitative* support — two explicit, physically distinct bounces give a
scale-independent growing-mode transfer whose residual shrinks under matching —
which can be cited as "we have verified the growing-mode transfer is
scale-independent to O(0.1) in slope across LQC and analytic bounces; a
freeze-corrected in-in computation to obtain a numerical δf_NL bound is in
progress." It does **not** yet justify upgrading (d) from "conditional" to
"derived." The number −35/8 is unchanged and no claim should be strengthened
beyond what is above.
