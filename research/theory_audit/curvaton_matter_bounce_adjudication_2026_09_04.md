# Adjudication: the curvaton-type matter bounce (ledger row 15) — 2026-09-04

**Role:** independent adjudicator of contested math (Fable, not the row-15 owner lane).
**Disputed artifact:** `research/track_a3_multichannel/row15_curvaton/` (report, `results.json`,
`row15_curvaton.py`). Does not touch `research/track_a3_multichannel/paper/main.tex`.
**Stance:** re-derive every item from stated assumptions; validate the machinery on the
de Sitter / inflationary-curvaton limit first; never steer toward viability or non-viability.

## Plan

| Item | Claim under adjudication | Method |
|---|---|---|
| A | CXB11 (arXiv:1101.0822) Eq. 18 is "the de Sitter coefficient", 4x too small for the contraction; Case 1 collapses to f_NL = -320/pi^4 | fetch source; re-derive massive-spectator tilt in a ~ eta^2; check Eq. 65 substitution |
| B | branch-W ALP-curvaton tilt sign (n_sigma - 1 ~ -m^2/H^2) is wrong | same derivation, both backgrounds |
| C | light spectator obeys the same MS operator as zeta; tilt 12w/(1+3w); n_s inherited | sympy: u''+(k^2-a''/a)u=0 vs v''+(k^2-z''/z)v=0 for constant w |
| D | r = 24/[1 + (4/3) r_dec^2 (M_pl/sigma_*)^2]; r<0.036 needs r_dec M_pl/sigma_* > 22.35 | two-channel P_zeta; check P_dsigma normalisation and P_zeta,ad = P_v/(2 eps M_pl^2) |
| E | f_NL = 5/(4 r_dec) - 5/3 - 5 r_dec/6; +9.30 -> -1.25 on [0.113,1]; zero at 0.5811 | LUW03 / SVW06 delta-N; evaluate |
| F | adiabatic -35/16 enters with weight (r/24)^2; SPHEREx-detectable only for r >= 22.95 | two-uncorrelated-channel bispectrum algebra |

Outputs: this file (verdicts + paper-ready sentences + open items),
`curvaton_matter_bounce_adjudication_2026_09_04.py` + `.json`,
`reproducibility/manifests/experiments/a3-row15-curvaton-adjudication.json`, ledger row 15 status line.

## Status

- [x] literature fetched (1101.0822 source; 1206.2382 source; astro-ph/0208055; astro-ph/0607627)
- [x] sympy derivations + de Sitter validation (script committed)
- [x] verdicts A–F written
- [ ] manifest validated; ledger updated

---

# Verdicts (2026-09-04; every number from `curvaton_matter_bounce_adjudication_2026_09_04.py`)

**Machinery validation (before the contraction case).** de Sitter spectator, `a = -1/(H\eta)`:
`\nu^2 = 9/4 - m^2/H^2`, `n_\sigma - 1 = 3 - 2\nu = 2m^2/(3H^2)` (textbook; blue for `m^2 > 0`),
massless limit exactly scale-invariant. The numeric integrator reproduces the exact tracking-mass
Bessel tilt `2\gamma/3` to 3% at `\gamma = 0.01` and 1% at `\gamma = 0.03` (noise floor `2\times10^{-4}`).
Sources read in full: arXiv:1101.0822 (CXB11) source, astro-ph/0208055 (LUW03) §f_NL,
astro-ph/0607627 (SVW06) Eq. (standardsdfNL); arXiv:1206.2382 (CEB12) only *mentions* the bounce
curvaton (its §V is the single-field bounce), so it carries no independent curvaton formula.

## A — CXB11 Eq. 18 and the Case-1 `f_NL` — **CONFIRMED (both parts), with one refinement**

*A(i), the coefficient.* For `a \propto \eta^2` (dust): `H = 2/(a\eta)`, so `m^2 a^2 \eta^2 = 4m^2/H^2 \equiv \gamma`
(identity, checked). A **tracking** mass (`m^2 \propto H^2`, which is CXB11's `m_\chi^2 = g^2\tilde\phi^2/2 \propto 1/t^2`)
makes `\gamma` constant, `\nu^2 = 9/4 - \gamma`, and

```
n_\chi - 1 = 3 - 2\nu = 2\gamma/3 + O(\gamma^2) = 8 m_\chi^2 / (3 H^2)        [sympy; exact Bessel index]
```

CXB11 Eq. (18) reads `n_\chi = 2m_\chi^2/(3H^2)`. That expression is exactly the de Sitter result above
(there `m^2a^2\eta^2 = m^2/H^2`, so `\gamma_{dS} = m^2/H^2`), and it is **4× smaller** than the dust-contraction
value. The lane's diagnosis is correct. **Refinement the lane missed:** CXB11's Eq. (19), `n_\chi \simeq g^2 m_{pl}^2/(2\pi m^2)`,
follows from their Eq. (18) only with the *un-halved* mass `m_\chi^2 = g^2\tilde\phi^2` (ratio 1 with the full mass,
1/2 with the Eq.-13 mass); with the corrected 8/3 coefficient and their own halved mass, Eq. (19) becomes
`g^2m_{pl}^2/(\pi m^2)` (ratio 2). Their near-scale-invariance condition therefore tightens to `|g m_{pl}| \ll \sqrt{\pi}\,m`.
Sign: `m_\chi^2 > 0` ⇒ **blue**, in both backgrounds. **Not adjudicable:** *why* CXB11 wrote the de Sitter
coefficient (no derivation is shown between their Eqs. 15 and 18); only that the stated formula is the de Sitter one.

*A(ii), Case 1.* Re-deriving Eq. (65) from their Eqs. (55), (60), (64) gives
`f_{NL} = -5120\,d^2\mathcal{C}/\pi^6 + 640\,m/(\pi^4 m_{pl})`; the second term is the `(1 - \ldots)` prefactor's
"1" and is `O(m/m_{pl})`, so their Eq. (65) is the leading term — reproduced exactly. With Eq. (32),
`\mathcal{C} = (\pi/4d_1)^2`, and `d = d_1` (Case 1: `\chi` dominates first), `d` cancels identically:

```
f_{NL}^{Case 1} = -5120/\pi^6 \times \pi^2/16 = -320/\pi^4 = -3.2851   (CXB11 quote: -3.3)
```

**CONFIRMED as arithmetic on CXB11's own equations.** Evidential strength: Eqs. (62)–(64) are CXB11's
analytic *estimates* ("≃", deflation modelled as `H = \alpha t`, freeze-out values), which neither the lane nor this
adjudication re-derives — `-320/\pi^4` is parameter-free *within that estimate*, not an independently derived number.

## B — branch-W ALP-curvaton tilt sign — **CONFIRMED that the derivation is wrong; the erring step is identified**

`research/branch_W_alp_curvaton_tilt/03_tilt_mechanisms.md` writes `n_\sigma - 1 \approx 2\nu - 3` and then
`\nu \approx 3/2 - m_\sigma^2/(3H_k^2)`, obtaining `-2m_\sigma^2/(3H_k^2)`. Since `P_v \propto k^{3-2\nu}`, the
relation is `n_\sigma - 1 = 3 - 2\nu`; the `\nu` expansion is right (`\nu < 3/2` for `m^2 > 0`), the tilt
relation is inverted. Within branch W's own crossing-time approximation the correct result is
`+2m_\sigma^2/(3H_k^2)` (blue), and phase-1's "`m \simeq 0.2 H_k` fixes `n_s = 0.965`" does not follow.

**Caveat on the physics (NOT DETERMINABLE, either sign):** branch W assumes a *constant* `m_\sigma`. In a dust
contraction `m/H \propto |t|`, so a constant-mass field is **heavy in the far past** (`m/H = 400`–`4000` at the
integrator's start) and light only near the bounce; the heavy→relativistic transition at `\eta_m = -\sqrt{k/m}` has
non-adiabaticity `\sqrt{m/8H_k}` (4–14% here), so the initial state is not the Bunch–Davies state of a light field
and the crossing-time formula does not apply. Numerically (first-order WKB vacuum at `\eta_i = -300`, `k = 0.2, 0.4`,
`\eta_f = -0.02`) the mass-induced tilt is `+2.6\times10^{-4}, -1.4\times10^{-4}, +0.8\times10^{-4}, -1.7\times10^{-3}`
for `m^2/H_k^2 = 2.3\times10^{-4}` … `2.3\times10^{-2}`, against crossing-time estimates `1.5\times10^{-4}` … `1.5\times10^{-2}`:
oscillatory in `m`, mostly at the noise floor, and the one significant value is *red*. The lane's sentence "a
positive mass tilts blue" is exact for a **tracking** mass (CXB11's model) and is **not established for a constant
mass**; branch W's scenario needs its heavy-epoch initial state specified before any tilt sign can be quoted.

## C — spectator obeys the same MS operator; tilt `12w/(1+3w)`; `n_s` inherited — **CONFIRMED (constant `w`)**

For `a \propto (-\eta)^q`, `q = 2/(1+3w)`, and constant `\epsilon`, `z = a\sqrt{2\epsilon}M_{pl} \propto a`, so
`z''/z = a''/a` identically (checked symbolically); the massless spectator (`u = a\sigma`), the adiabatic `v`, and each
tensor polarisation obey one operator. `\nu = q - 1/2` (valid for `q > 1/2`, i.e. `w < 1`), and

```
n - 1 = 3 - 2\nu = 4 - 2q = 12w/(1+3w)      [sympy identity];   w = -0.0029  ->  n_s = 0.96489
```

Dust (`w = 0`) is exactly scale-invariant (Wands 1999 / Finelli–Brandenberger 2002). Because both channels carry the
same `k`-tilt, `P_{\zeta,tot}` inherits it for **any** mixing weight; `n_s` remains row 10's *anchor* (`w` fitted),
not a prediction. **Assumption that must be stated:** `\epsilon = const` through the whole window of modes; any
`w(t)` (e.g. CXB11's deflationary phase) breaks `z''/z = a''/a` and the two channels' tilts can then differ.

## D — `r = 24/[1 + (4/3) r_{dec}^2 (M_{pl}/\sigma_*)^2]`, threshold 22.35 — **CONFIRMED (22.34)**

With one mode function `v` for all three channels: `P_{\zeta,ad} = P_v/(2\epsilon a^2 M_{pl}^2)`, `P_{\delta\sigma} = P_v/a^2`,
`P_h = 8P_v/(a^2M_{pl}^2)` (two polarisations, `u_h = aM_{pl}h/2`), so `r_{single} = 16\epsilon` (24 at `\epsilon = 3/2`) and,
with `\zeta_{curv} = r_{dec}(2/3)\delta\sigma/\sigma_*` (LUW03, quadratic `V`),

```
P_{\zeta,curv}/P_{\zeta,ad} = (8\epsilon/9)\, r_{dec}^2 (M_{pl}/\sigma_*)^2 = (4/3) r_{dec}^2 (M_{pl}/\sigma_*)^2   [sympy]
r = 144\epsilon\sigma_*^2 / (8\epsilon M_{pl}^2 r_{dec}^2 + 9\sigma_*^2)
```

`r < 0.036` ⇔ `r_{dec}M_{pl}/\sigma_* > 22.344` (lane: 22.35, rounding); `r < 0.01` ⇔ `> 42.42`; row-10-normalised
`\mathcal{F} \ge 25.82` (CXB11's own `r \simeq 35\mathcal{F}^{-2}` would give 31.18). **Assumptions the formula rests on
(not derived by the lane or here):** (1) `\sigma_*` is the homogeneous curvaton value *at conversion* and is unchanged
through contraction and bounce (a massless field started at rest stays at rest; any `\dot\sigma \ne 0` grows as `a^{-3}`
in the contraction); (2) `\delta\sigma` and `\zeta_{ad}` receive the same bounce transfer — true by construction
for the massless operator but an assumption once the curvaton is not massless; (3) the curvaton is sub-dominant
during the contraction (otherwise `\epsilon` is not the dust value and C fails); (4) conversion happens after
reheating into radiation. None of these is questionable at the modelled level; all must be stated.

## E — curvaton `f_{NL} = 5/(4r_{dec}) - 5/3 - 5r_{dec}/6`, `+9.30 \to -1.25`, zero at 0.5811 — **CONFIRMED**

Independent `\delta N` derivation, sudden decay, `\rho_r e^{4(\zeta_r-\zeta)} + \rho_\sigma e^{3(\zeta_\sigma-\zeta)} = \rho`,
`\zeta_\sigma = (2/3)\ln(1+\delta\sigma/\sigma_*)` (quadratic `V`, `\rho_\sigma \propto \sigma^2` exactly), expanded to
second order and `r_{dec} = 3\Omega_\sigma/(4-\Omega_\sigma)`:

```
f_{NL} = (5/3) N''/N'^2 = 5(3 - 4r_{dec} - 2r_{dec}^2)/(12 r_{dec}) = 5/(4r_{dec}) - 5/3 - 5r_{dec}/6   [= SVW06 Eq. (standardsdfNL), g''=0]
```

Zero at `r_{dec} = \sqrt{10}/2 - 1 = 0.58114`; `f_{NL}(1) = -5/4`; Planck `2\sigma` upper (`+9.3`) at `r_{dec} = 0.1130`.
All lane numbers reproduce. The SVW `(1 + gg''/g'^2)` factor is zero only if the curvaton's evolution between
Hubble exit and decay is linear in `\sigma_*` — true for a free field, **an assumption through the bounce**; a
`\sigma^4` or axion-cosine self-interaction (branch W's Model B) reintroduces it as free parameters.

## F — dilution `(r/24)^2`; SPHEREx only for `r \ge 22.95` — **CONFIRMED, with the transfer dependence made explicit**

Two independent Gaussian seeds, `\zeta_i = g_i + (3/5)f_i g_i^2`: `f_{NL}^{eff} = \sum_i f_i (P_i/P)^2` (symbolic). The
adiabatic power fraction is `1/(1 + P_{curv}/P_{ad}) = r/24` exactly, weight `r^2/576 = 2.25\times10^{-6}` at `r = 0.036`,
so the bounce term is `-4.9\times10^{-6}` (pre-transfer), `-1.2\times10^{-6}` (LQC, `T = 0.250`), `-8.1\times10^{-7}` (Quintin, 0.165).
**The lane's `r \ge 22.95` is the `T = 0.250` (most favourable A2) value**; `T = 1` gives 11.47 and `T = 0.165` gives
28.25 — above 24, i.e. never. The qualitative statement (bounce `f_{NL}` observable only on the tensor-excluded
branch) holds for every `T \le 1`. Assumption: no `N_{\phi\sigma}` cross term (independent channels) and the
adiabatic shape `-35/16 + (15/16)\mu^2` diluted uniformly.

## What the A3M paper may state (evidential strength as adjudicated)

> Adding a light spectator to the dust contraction leaves the tensor spectrum untouched and, because the spectator
> obeys the same Mukhanov–Sasaki operator as the adiabatic mode when `\epsilon` is constant, adds a scalar channel
> with the identical tilt `12w/(1+3w)`; for a quadratic curvaton with sudden decay, `r = 24/[1 + (4/3) r_{dec}^2
> (M_{pl}/\sigma_*)^2]` and the local non-Gaussianity is the curvaton's `5/(4r_{dec}) - 5/3 - 5r_{dec}/6`
> (Lyth–Ungarelli–Wands; Sasaki–Valiviita–Wands). The contraction's intrinsic `f_{NL}` then enters the observable
> bispectrum with weight `(r/24)^2 \simeq 2\times10^{-6}` at `r = 0.036` and is below SPHEREx reach for any
> `r < 11.5` (`< 23` after the modelled bounce transfer). The spectator's own mass cannot supply the red tilt in
> this setting: for a mass tracking `H` the tilt is `+8m^2/(3H^2)` (blue; Cai–Xue–Brandenberger's Eq. 18
> quotes the de Sitter coefficient `2/3`), and for a constant mass the field is heavy in the far past and no
> clean power-law tilt results.

Do **not** state: that CXB11's `-320/\pi^4` is a derived prediction (it is arithmetic on their estimate); that a
positive constant mass gives a blue tilt (not established); that branch W's sign is "opposite to CXB11" as if
CXB11 were the contraction result (both carry the de Sitter form; branch W's error is the `3 - 2\nu` step).

## What remains open

1. CXB11 Eqs. (62)–(64) (the `\zeta_{NL}` integral through deflation and bounce) — not re-derived by anyone in the lab.
2. The constant-mass spectator in a contraction: initial state in the heavy epoch and the resulting `k`-dependence
   (numerics here show oscillatory, sub-`10^{-3}` structure, not a tilt) — decides whether any *mass* mechanism exists.
3. `\mathcal{F}` (entropy-only kinetic amplification) and `\sigma_*`'s constancy through the A2 backgrounds — need an
   entropy sector in those backgrounds; without it `r` is *free* in the sense of "unconstrained", not "predicted".
4. Whether `\epsilon = const` holds across the observable window in any concrete two-field realisation (C's assumption).

## Reproduce

`python3 research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.py` — local CPU, ~2 s, $0, deterministic.
Manifest: `reproducibility/manifests/experiments/a3-row15-curvaton-adjudication.json`.
