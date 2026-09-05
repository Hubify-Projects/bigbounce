# Ledger row 14 — the (r, f_NL) window in the contraction's scalar sound speed c_s

**Status:** IN PROGRESS 2026-09-04 (plan header committed first; results appended below).
**Owner lane:** row14_cs_window (does NOT touch `research/track_a3_multichannel/paper/main.tex`)
**Artifacts (planned):** `row14_cs_window.py`, `results.json`, `row14_cs_window.log`,
`row14_cs_window.png`, manifest `reproducibility/manifests/experiments/a3-row14-cs-window.json`.

## Why

Row 10 (`../row10_r_ns/ROW10_R_NS_2026-09-04.md`) closed with `r = 16\epsilon = 24`
for the canonical dust contraction — bounce-invariant across all three A2
backgrounds, ~670x above BICEP/Keck's `r < 0.036`. The textbook remedy is a
scalar sound speed `c_s < 1` in the contracting phase, which suppresses `r`
while *enhancing* the scalar non-Gaussianity. The flagship line's `f_NL` must
therefore be re-stated on whatever `c_s` branch is CMB-viable, or Track A's
claim is conditional on unspecified physics. Ledger success/kill: a viable
`c_s` window with a stated `f_NL^after` -> the flagship claim re-anchored
honestly; no viable window -> Track A states the tensor problem as unresolved.

## Plan

1. **Analytic spectra with constant `c_s`.** `z^2 = a^2(\rho+p)/(c_s^2 H^2) = 2a^2\epsilon/c_s^2`,
   `v = z\zeta`, `v'' + (c_s^2k^2 - z''/z)v = 0`, BD normalisation
   `v \to e^{-ic_sk\eta}/\sqrt{2c_sk}`. Tensors are unchanged (`c_T = 1`).
   Derive `r(c_s,\epsilon)` for the contracting, growing-mode-dominated case —
   do NOT assume the inflationary formula; get the power of `c_s` from the
   index `\nu = q - 1/2`, `q = 2/(1+3w)`.
2. **Numerical confirmation** with a lane-b-style integrator at `k\eta_B << 1`.
3. **The window:** `c_s` at which `r = 0.036` and `r = 0.01`.
4. **`f_NL^{pre}(c_s)`** in the isoceles squeezed limit, TWO ways: (a) Li,
   Quintin, Wang & Cai 2016 (arXiv:1612.02036) Eq. (4.19); (b) the lab's own
   in-in machinery (`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py`)
   with the `c_s`-modified cubic vertices. Li's `c_s = 1` limit must reproduce
   `-35/16`; report any discrepancy honestly.
5. **Transfer `T(c_s)`** through the Quintin-type A2 background (S1), noting
   whether `z`'s `c_s` factor changes the super-Hubble branch mixing; hence
   `f_NL^{after}` at the viable `c_s`.
6. **No-go check:** Quintin, Sherkatghanad, Cai & Brandenberger 2015
   (arXiv:1508.04141) — quote their exact small-`r`/acceptable-`f_NL`
   inequality and test the viable `c_s` against it. Compare `|f_NL^{after}|`
   to Planck 2018 `f_NL^{local} = -0.9 +/- 5.1` and SPHEREx `\sigma = 0.5-0.7`.
7. **What sets `c_s < 1`:** state plainly that a k-essence/DBI-type kinetic
   sector is required (Garriga & Mukhanov 1999; Chen, Huang, Kachru & Shiu
   2007) and that this lab's pressureless-dust model does NOT provide it.

## Ground rules

Never tune. Every number in the results table comes from the committed script.
Claims stated at exactly their evidential strength; a null is published as a null.
