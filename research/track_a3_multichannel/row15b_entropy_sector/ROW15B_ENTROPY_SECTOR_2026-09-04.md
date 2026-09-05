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

---

# Results (2026-09-04; every number from `row15b_entropy_sector.py` / `results.json`)

**Status: DONE. Row 15's named open item is closed at the level it can honestly be
closed: the entropy sector's *transfer* through all three A2 backgrounds is now
computed, and it is identical to the tensor's. The consequence is that the curvaton
viability condition is a purely PRE-bounce statement — the bounce neither helps nor
hurts it — and it is the same in both scalar schemes.**

## 1. The operator identity, and why it makes the transfer trivial

A spectator `\sigma` with `m^2 \ll H^2` and canonical kinetic term has `u = a\sigma`
obeying

```
u'' + (k^2 - a''/a + a^2 m^2) u = 0                                   (row 15b)
```

The tensor polarisation `h` has `v = a h` obeying `v'' + (k^2 - a''/a) v = 0`, and the
adiabatic `\zeta` in **scheme S1** (geometric / dressed-metric, `z = a`, `c_s = 1`) has
`\mu = a\zeta` obeying the same. For a massless spectator the three pump terms are
*literally the same function* `a''/a`, so

```
\lambda_\sigma(k)  =  \lambda_T(k)  =  \lambda_\zeta^{S1}(k)      identically (S1)
```

This is an operator identity, not a coincidence: nothing about the bounce
distinguishes a test scalar from a graviton polarisation once both are canonically
normalised on `z = a`. **In scheme S2** (fluid Mukhanov–Sasaki, `z^2 = 2a^2\epsilon/c_s^2`)
the adiabatic variable's pump term is `z''/z \neq a''/a` and the spectator's is
unchanged, so there the spectator still tracks the *tensor*:

```
\lambda_\sigma  =  \lambda_T ,        \Lambda \equiv \lambda_T/\lambda_\zeta \ne 1  (S2)
```

## 2. Numerical verification on all three A2 backgrounds

Both fields are seeded with the **exact** pre-bounce matter mode
`e^{-ik\tau}(1 - i/k\tau)/\sqrt{2k}` (exact for all `k\tau` in a matter era, so no
sub-Hubble requirement), integrated across a symmetric window `\eta \in [-20\eta_B,
+20\eta_B]`, and read out as `\sigma = u/a`, `h`. The tensor uses an **independent**
first-order formulation `h' = \Pi/a^2`, `\Pi' = -a^2k^2h` with `\Pi = a^2h'`, so the
comparison is a real numerical test rather than the same integration twice.

| background | `k\eta_B` | `\lambda_\sigma` | `\lambda_T` | `\lambda_\sigma/\lambda_T - 1` |
|---|---|---|---|---|
| Quintin-type | 0.001 | 4339.806 | 4339.461 | `+8.0\times10^{-5}` |
| Quintin-type | 0.01 | 4226.094 | 4225.757 | `+8.0\times10^{-5}` |
| LQC-eff.-dust | 0.001 | 1016.2634 | 1016.2634 | `+5.5\times10^{-10}` |
| LQC-eff.-dust | 0.01 | 987.2718 | 987.2718 | `+5.5\times10^{-10}` |
| poly-analytic | 0.001 | 7325.0155 | 7325.0155 | `+7.1\times10^{-10}` |
| poly-analytic | 0.01 | 7152.0412 | 7152.0411 | `+2.8\times10^{-9}` |

(The absolute `\lambda` depends on the window — it is the growing-mode amplification
between `-20\eta_B` and `+20\eta_B` — so these numbers are **not** comparable to row 18a's
`\lambda_T = 6.06`, which is measured from the NEC boundary to `50\eta_B`. Only the
*ratios* are physical, and they are window-independent.)

The Quintin residual `8\times10^{-5}` is a numerical floor of that background's
piecewise `t`-sampled arrays (it is `k`-independent to 3 digits, which a physical
effect would not be); LQC and poly reach `10^{-9}`, consistent with the analytic
identity and with row 14's `|\lambda_{scalar}/\lambda_{tensor}-1| \le 4\times10^{-11}`.

**Light mass.** `\Delta\lambda_\sigma/\lambda_\sigma` scales as `(m\eta_B)^2` and vanishes
smoothly: on Quintin, `-4.2\times10^{-7}` at `m\eta_B = 10^{-6}`, `-4.2\times10^{-5}` at
`10^{-5}`, `-4.2\times10^{-3}` at `10^{-4}`, `-0.37` at `10^{-3}`. The massless result is the
`m\eta_B \to 0` limit, and the departure at `m\eta_B \gtrsim 10^{-3}` is not a defect of the
transfer: over a window reaching `20\eta_B` the expansion has driven `H` down to
`\sim m`, which is exactly the epoch at which the curvaton *begins to oscillate* — the
physics that generates `\mathcal{F}` in the first place, and which happens well after the
bounce.
