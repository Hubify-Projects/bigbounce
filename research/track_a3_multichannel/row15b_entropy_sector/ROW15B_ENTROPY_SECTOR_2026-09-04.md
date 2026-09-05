# Row 15b — Entropy (spectator) sector through the A2 matter-bounce backgrounds

**Status:** IN PROGRESS (plan header committed 2026-09-04)
**Parent:** ledger row 15 (curvaton dilution factor ℱ) — named open item:
"ℱ needs an entropy sector in the A2 backgrounds."

## Plan

1. Evolve a spectator field δσ (massless, then light m² ≪ H_B²) on each of the
   three A2 backgrounds (Quintin, LQC-dust, poly) with adiabatic-vacuum ICs:
   u'' + (k² − a''/a + a² m²) u = 0. Extract the bounce transfer λ_σ(k).
2. Compare λ_σ against the adiabatic scalar λ_ζ (schemes S1, S2) and the tensor
   λ_T. Test the structural claim: a massless spectator shares the tensor's
   pump term a''/a, so λ_σ = λ_T exactly, and the σ/ζ amplitude ratio is
   preserved through the bounce in S1 (λ_ζ^S1 = λ_T) but rescaled by
   λ_T/λ_ζ^S2 in S2.
3. Convert row 15's requirement ℱ ≥ 25.8 (i.e. r < 0.036 with r = 24/[1 +
   (4/3) r_dec² (M_pl/σ_*)²], threshold r_dec M_pl/σ_* > 22.34) into a
   PRE-bounce condition on σ_* and r_dec, per background × scheme.
4. State (not compute) which cubic vertices apply to a spectator, i.e. whether
   the curvaton's intrinsic f_NL inherits the same Δf_NL^bounce structure.
5. Check the surviving discriminator n_T = n_s − 1 = −0.035: is λ_T
   k-dependent across the observable band (row 18a λ_T(kη_B) values)?

**Never tune.** All parameters are inherited from the A2 background definitions
and row 15; no fit factors are introduced.

## Outputs
- this .md (derivation, table, verdict, paper-ready sentences)
- row15b_entropy_sector.py + results.json + .log + .png
- manifest registered in programs/bounce-theory.json
- ledger row 15 status update (≤5 lines)
