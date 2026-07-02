# Path Z — Full Cubic In-In Bounce Transmission: LAUNCH STATUS

**Launched:** 2026-07-02 (local, nohup detached, survives disconnect)
**Goal:** upgrade P2 f_NL = -35/8 from CONDITIONAL forecast (assumption d:
"the bounce transmits the contracting-phase bispectrum unmodified") to a DERIVED
prediction, by explicitly computing <ζζζ> with the complete Maldacena cubic
vertex on the explicit nonsingular LQC bounce background.

## What Path Z implements (vs the prior (k·η_bounce)² semi-analytic estimate)
1. Explicit nonsingular LQC background H² = (ρ/3)(1−ρ/ρc), dust (w=0), a_min>0.
2. Numerically-solved Mukhanov-Sasaki mode functions through
   contracting→bounce→expanding, WKB adiabatic Bunch-Davies in-state deep in
   contraction (freeze-time-corrected sampling).
3. Smooth, bounded z''/z through the bounce (no 2/η² singularity).
4. Full cubic vertex set (all Maldacena terms) with time-dependent ε(η), H(η).
5. In-in squeezed-limit quadrature; f_NL = (5/12) B/(P P) + field-redef.
6. Two robust normalisation-free observables:
   - **T_growing** = growing-mode coefficient α_out/α_in across the bounce.
   - **T3** = f_NL^bounce / f_NL^contraction-only (same machinery both sides).
   Convergence study over 5 backgrounds (coarse→ultradeep) × k-tower.

## Job control
- Process: `python3 -u pathz_full_inin_bounce.py`, PID in `pathz_pid.txt`.
- Log:    `pathz_run.log` (+ `pathz_stdout.log`)
- Results: `pathz_results.json` (written incrementally after each background)
- DONE marker: `PATHZ_DONE` (written on completion)

## Harvest instructions (heartbeat)
```
cd research/cubic_bounce_transmission
ps -p $(cat pathz_pid.txt)          # still running?
tail -20 pathz_run.log              # latest progress
cat pathz_results.json | python3 -m json.tool | tail -40   # partials
ls PATHZ_DONE                       # exists => finished; read "derived" block in JSON
```
Final answer lives in `pathz_results.json["derived"]`:
`delta_fnl`, `bispectrum_transfer_T3_k0`, `numerical_uncertainty_estimate`.

## Preliminary signal (coarse background, ~18 s in)
`|T_growing|` is **scale-independent** across k = 0.03 → 0.002 (plateau ~7.8e7,
<5% variation over 15× in k). Scale-independent transfer preserves the
bispectrum SHAPE and hence f_NL (a ratio) — the qualitative signature that the
bounce transmits the -35/8. Decaying-mode fraction β/α ~ O(1): subdominant but
real, to be resolved in the deep runs. NOT the final number — the k→0
extrapolation on the ultradeep background is the derived result.

## ETA
Backgrounds: coarse(~2min) medium(~4) fine(~10) deep(~25) ultradeep(~60+).
Per-background mode+in-in scan dominates; small-k + deep-η legs are the
expensive ones. Rough total wallclock: several hours to ~1 day on this CPU.
Genuinely-hard growing-mode-coefficient extraction on the deepest grids may
need a re-run at higher resolution if convergence isn't clean → that is the
multi-day tail.

## HONESTY / pattern-036
No number is fabricated. delta_fnl / T3 are whatever the quadrature computes.
If the deep runs do not converge to a clean k→0 limit, the correct reported
outcome is the best rigorous numerical bound on |T3−1| with its uncertainty,
plus a precise statement of what it establishes — NOT a manufactured value.
Do NOT edit the paper from partial output.

## RESULT (2026-07-02, after normalisation-bug fix)
The first run reported delta_fNL=+4.375 with T3~1e-29 — a NUMERICAL ARTIFACT.
Root cause: f_NL = (5/12)B/(PP) is only normalisation-free when the external
legs, the vertex-integral endpoint, and P are ALL read at the SAME frozen
super-horizon reference time. The old code read the full-bounce case at
eta_max*0.85 but the contraction-only benchmark at eta_max*0.05, which was
(a) POSITIVE (post-bounce, wrong branch) and (b) OUTSIDE the contraction grid
[eta_min,-0.5] → cubic-spline extrapolation garbage. Because matter contraction
has a GROWING mode ζ~η⁻² that never freezes, that mismatched read left ~2
uncancelled powers of a runaway amplitude → f_NL_cont ~ 1e17…1e70 (growing with
background depth). FIX: read ext/P/vertex-endpoint at a common frozen reference
(deep expansion for full, deep contraction for benchmark, both inside-grid).

After the fix: f_NL_cont is FINITE, O(1–100) — the 1e70 divergence is gone.
T3(k→0) ≈ −0.88, |T_growing| and T3 are SCALE-INDEPENDENT across the k-tower.
BUT the numerical contraction-only f_NL does NOT reproduce the analytic −35/8
(benchmark ratio ~−2.5x), so the machinery is NOT amplitude-faithful.

VERDICT: METHOD CANNOT DERIVE AN AMPLITUDE. Path Z establishes only the SHAPE
result (scale-independent transfer ⇒ bounce preserves the bispectrum shape); it
does NOT pin f_NL. P2's f_NL = −35/8 STAYS CONDITIONAL (assumption d). This is
consistent with the paper's existing framing (assumption-d flagged as the #1
follow-up compute / core uncertainty). NO paper edit made. See
pathz_results.json["derived"].status == "conditional-shape-only".
