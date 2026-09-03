# A3-1b — The lab's own primordial curvature spectrum Δ²_ζ(k) at PBH scales

**Date:** 2026-09-03 · **Ledger:** `NEXT_SCIENCE_LEDGER.md` #3 (sub-item A3-1b), #6 (early-SMBH discriminator)
· **Script:** `inlab_delta2_zeta_2026-09-03.py` · **Outputs:** `outputs/inlab_delta2_zeta_2026-09-03.{json,png}`

## Plan (header written first; results below filled by the committed script)

1. Build Δ²_ζ(k) = A_s (k/k_*)^{n_s−1} for the matter contraction with the lab's
   conventions (A_s = 2.1e−9, k_* = 0.05 Mpc⁻¹, Planck 2018), n_s−1 from the
   matter-bounce tilt; extrapolate to k ~ 1e5–1e15 Mpc⁻¹ and state assumptions,
   including the A2 validity bound kη_B ≪ 1 (compute k_B per background).
2. Survey the literature enhancement candidates (Quintin+2015, Agullo–Bolliet–
   Sreenath 2017, matter-bounce PBH papers) — labelled as literature.
3. Feed Δ²_ζ(k) into the committed `pbh_compaction_fnl.py` machinery (imported,
   not modified) to get delivered vs required amplitude at each PBH mass scale
   for f_PBH ∈ {1e−3, 1e−2, 1} at f_NL = −35/16 and −35/8.
4. FIRAS μ-distortion check on any required amplitude at k ~ 1e2–1e4 Mpc⁻¹.

Integrity: the spectrum is never tuned to produce PBHs; every number below is
emitted by the committed script.
