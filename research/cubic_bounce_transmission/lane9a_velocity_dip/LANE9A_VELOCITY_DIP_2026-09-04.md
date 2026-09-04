# Ledger row 9 (A3-1e), lane (a) — scalar-field-velocity-dip amplification at kη_B ~ 1

**Date:** 2026-09-04 · **Status:** IN PROGRESS (plan header committed first per anti-stall rule)

## Question

Does the Quintin, Sherkatghanad, Cai & Brandenberger (2015, arXiv:1508.04141)
scalar-field-velocity-dip amplification of ζ through the bounce — their Eq. (79),
Δζ/ζ ~ [φ̇_B/φ̇(t_amp−)]², which they find can reach ~50 — exist on the lab's three
A2 backgrounds? And what does it do to the curvature spectrum and to the cubic term
in the band kη_B ∈ [0.1, 10] that the S1 super-Hubble transfer (validity kη_B ≲ 1e−2)
does not cover?

## Plan

1. Fix the literature statement: quote Quintin Eqs. (44), (79) and the definition of t_amp−.
2. Per A2 background, decide whether a φ̇ dip is even *definable*
   (Quintin-type = single scalar by construction; LQC dust dressed-metric and poly
   non-LQC = effective fluid).
3. Numerically evolve the linear MS/ζ mode across the bounce with the lane-b machinery
   at kη_B ∈ {0.1, 0.3, 1, 3, 10}; measure λ_ζ(k) = |ζ_after/ζ_before|. This is the lab's
   own growth factor extended past the S1 validity band.
4. Evaluate Eq. (79)'s factor for the lab's Υ, Δt_B mapping; report per background.
5. Propagate to Δ²_ζ at the bounce scale and to Δf_NL^bounce via the Eq. (44) structure,
   with an explicit scheme label and an honest coverage statement.
6. VERDICT: quantified enhancement at kη_B ~ 1 (→ reopen PTA/PBH channels) or none
   (→ nulls stand).

Integrity: no tuning to a desired outcome; every number in this note comes from the
committed script `lane9a_velocity_dip.py` → `results.json`.

## Results

(filled in below by the run)
