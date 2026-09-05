# Ledger row 15 — the curvaton-type matter bounce: (r, n_s, f_NL)

**Status:** IN PROGRESS 2026-09-04 (plan committed first; results appended below).
**Owner lane:** row15_curvaton (does NOT touch `research/track_a3_multichannel/paper/main.tex`)
**Question (ledger row 15):** does a matter-bounce curvaton (Cai, Xue &
Brandenberger 2011, arXiv:1101.0822; the lab's branch-W ALP-curvaton work)
give `r < 0.036` with `n_s \simeq 0.965` and a local `f_NL` of O(1) — and at
what value and sign?

## Why

Row 10 (`../row10_r_ns/`) closed the canonical dust contraction at
`r = 16\epsilon = 24`, bounce-invariant, ~670x above BICEP/Keck. Row 14
(`../row14_cs_window/`) closed the k-essence remedy as a NULL: `r < 0.036`
needs `c_s < 1.5e-3` where `f_NL^{after} \sim 6e5`, while `|f_NL| \le 5.1`
needs `c_s \ge 0.444` where `r \ge 10.7` — disjoint by ~296x in `c_s`
(decision D-A3-11). The curvaton is the standard *surviving* route: it does
not touch the tensor sector at all, it adds a second, larger scalar channel,
so `r` falls by the ratio of scalar powers. Whether the surviving point also
has `n_s \simeq 0.965` and an O(1) `f_NL` decides whether the flagship line's
`f_NL` prediction can be re-anchored, or whether Track A must state the whole
matter-bounce family as excluded at the modelled level.

## Plan

1. **Spectator spectrum in the dust contraction.** A light scalar `\sigma`
   (`m \ll H`) on the same `a \propto (-\eta)^2` background: solve
   `u'' + (k^2 - a''/a)u = 0` (same MS operator as the adiabatic mode for a
   massless spectator, `u = a\sigma`), BD vacuum, extract `P_\sigma(k)` and
   its tilt from the small-mass correction. Cross-check against Cai, Xue &
   Brandenberger 2011's stated `n_s` for the curvaton in a matter contraction.
2. **Conversion to `\zeta`.** `\zeta = r_{dec}\,\zeta_\sigma` with
   `\zeta_\sigma = (1/3)\,\delta\rho_\sigma/\rho_\sigma =
   (2/3)\,\delta\sigma/\sigma` (quadratic potential), so
   `P_{\zeta,curv} = (r_{dec}^2/9)(2/\pi)^2 ... ` — coefficient from the
   script, not by hand; `r_{dec} = 3\rho_\sigma/(3\rho_\sigma + 4\rho_r)` at
   decay (Lyth–Ungarelli–Wands 2003, astro-ph/0208055).
3. **`r(r_{dec}, \sigma_*)`.** `P_h` unchanged from row 10; the adiabatic
   scalar unchanged. `r = P_h/(P_{\zeta,ad} + P_{\zeta,curv}) =
   24/(1 + P_{\zeta,curv}/P_{\zeta,ad})`. Solve for the suppression factor
   needed for `r < 0.036` and `r < 0.01`.
4. **`n_s`.** From the curvaton's own tilt in the contraction (mass term +
   background), test whether 0.9649 is reachable and with what `m/H`.
5. **`f_NL`.** Curvaton local formula `f_NL = 5/(4r_{dec}) - 5/3 -
   5r_{dec}/6` (LUW 2003; Sasaki, Valiviita & Wands 2006, astro-ph/0607627),
   evaluated over the `r_{dec}` values that satisfy (3); plus the *intrinsic*
   non-Gaussianity generated in the contraction (is it a `-35/16`-type term
   with a different coefficient?) — cite Cai+2011's own statement. Report
   SIGN and magnitude vs Planck `-0.9 \pm 5.1` and SPHEREx `\sigma \simeq 0.5`.
6. **Transmission.** The curvaton converts *after* the bounce, so state
   whether the A2 transfer applies to `\sigma` (same MS equation for a
   massless spectator?) and whether `\Delta f_NL^{bounce}` applies at all.
7. **Multi-channel map at the viable point:** which of A3's nulls survive,
   and SPHEREx's reach for the curvaton `f_NL`.

## Ground rules

Never tune. Every number in the results table comes from the committed script
`row15_curvaton.py`. Claims at exactly their evidential strength; a null is
published as a null (VISION R6).

---

*(results appended below when the script lands)*
