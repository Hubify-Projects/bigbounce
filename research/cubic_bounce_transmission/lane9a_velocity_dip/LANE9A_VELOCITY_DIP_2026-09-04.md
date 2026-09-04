# Ledger row 9 (A3-1e), lane (a) — scalar-field-velocity-dip amplification at kη_B ~ 1

**Date:** 2026-09-04 · **Status:** COMPLETE

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

## 0. Literature anchor (quoted, not recomputed)

Quintin, Sherkatghanad, Cai & Brandenberger, *"Evolution of cosmological perturbations and
the production of non-Gaussianities through a nonsingular bounce: Indications for a no-go
theorem in single field matter bounce cosmologies"*, arXiv:1508.04141 (PRD 92, 063532).

| object | statement |
|---|---|
| bounce-phase ansatz | $H(t)=\Upsilon(t-t_B)$, $a(t)=a_Be^{\Upsilon(t-t_B)^2/2}$, $\dot\phi(t)=\dot\phi_Be^{-(t-t_B)^2/T^2}$ |
| Eq. (44) | $f_{\rm NL}\sim(\Delta\zeta)^2/(\Delta t_B M_p^2)$ |
| Eq. (79) | $\dot\zeta_{\max}\simeq\dot\zeta(t_B^-)\,[\dot\phi_B/\dot\phi(t_{\rm amp-})]^2$ |
| Eq. (80) | $\zeta(t_{\rm amp+})-\zeta(t_{\rm amp-})\lesssim\dot\zeta(t_B^-)[\dot\phi_B/\dot\phi(t_{\rm amp-})]^2(t_{\rm amp+}-t_{\rm amp-})$ |
| $t_{\rm amp\pm}$ | $t_{\rm amp\pm}\equiv t_B\pm\Delta t_{\rm amp}$ — the window in which their Regime-II linear-growth approximation holds |
| Eq. (30) | $|1+\Delta\zeta_{k_*}/\zeta_{k_*}(\eta_B^-)|\gtrsim50.1$ |

**Correction to the framing of the task.** The "~50" is *not* an amplification they achieve.
Eq. (30) is the amplification **required** to push $r$ below $0.12$; their own conclusion is the
opposite — the growth "is very limited because of the conservation of curvature perturbations on
super-Hubble scales". The gap between *required* $\gtrsim50$ and *achievable* $O(1)$ **is** their
no-go theorem. Under their Eq. (79) ansatz the factor is

$$\Big[\frac{\dot\phi_B}{\dot\phi(t_{\rm amp-})}\Big]^2=\exp\!\Big(\frac{2\,\Delta t_{\rm amp}^2}{T^2}\Big),$$

controlled **entirely** by $T$, the width of the matter-sector velocity profile — a free matter
parameter that the bounce geometry does not fix.

## 1. Is a $\dot\phi$ dip even definable on the lab's backgrounds?

Two candidate identifications, and only one of them is Quintin's.

**(i) Total-sector.** The Friedmann constraint gives $\rho+p=-2M_p^2\dot H$ on *any* background, so a
single canonical field would need $\dot\phi^2=-2M_p^2\dot H$. But $\dot H=0$ *is* the definition of
the NEC boundary $\pm\eta_B$, so this candidate velocity vanishes there identically and is negative
(ghost) throughout the NEC-violating window. Substituting it into Eq. (79) manufactures a
divergence, not a physical amplification — measured in the log: $[\dot\phi_B/\dot\phi]^2\to
2.2\times10^{10}$ (LQC) and $7.6\times10^{3}$ (poly) as $t_{\rm amp-}\to-\eta_B$. It is therefore
**rejected**: Quintin's $\dot\phi$ is the velocity of the *regular matter scalar* in a two-component
(matter + ghost-condensate/Lee-Wick) model, which stays finite while the **total** $\rho+p$ crosses
zero. This identification is reported only as the diagnostic that shows why it cannot be used.

**(ii) Matter-sector.** The lab's backgrounds do not specify a matter Lagrangian, so $\dot\phi$ is an
*added input*, not a property of the background — except in the one case where the geometry fixes it:

| background | single-scalar realisation? | $\dot H$ inside the NEC window | Eq. (79) factor |
|---|---|---|---|
| Quintin-type $H=\Upsilon(t-t_B)$, $\Delta t_B=1$ | **yes** — it is their own single-field ansatz | $\dot H=\Upsilon=2.66667$, **constant to $7.2\times10^{-6}$** (measured) | **exactly 1** |
| LQC effective dust (dressed metric) | no — effective fluid, $w=0$, no field velocity | $0.5\to0$ across the window (factor-of-1 variation) | **1** (undefined without added matter input) |
| poly non-LQC $a=a_b(1+\eta^2/\eta_b^2)$ | no — pure $a(\eta)$ ansatz, no matter model at all | $2\to0$ across the window (98% variation) | **1** (undefined without added matter input) |

The Quintin-type row is a **derivation, not an assertion**: $\dot H=\Upsilon$ is constant across the
entire bounce phase by construction, so any single field with a fixed kinetic normalisation has
$\dot\phi^2=2M_p^2\Upsilon=\text{const}$. That is exactly $T\to\infty$ in their profile, giving
$\exp(0)=1$. Their own $T=\Delta t_{\rm amp}$ choice would give $e^2=7.389$; the lab's geometry
supplies no reason to choose it. This upgrades lane (c) §2.3 item 2 ("the lab's backgrounds carry no
scalar-velocity dip") from an assertion to a result.

## 2. The lab's own growth factor, extended into $k\eta_B\in[0.1,10]$

Machinery: `a2_transmission_linear.evolve()` — adiabatic-vacuum initial data in the contracting
matter era, full finite-$k$ Mukhanov–Sasaki evolution $\mu''=(k^2-a''/a)\mu$ across the bounce,
then **exact** projection onto the $S/C$ matter basis at both ends (no super-Hubble approximation
anywhere in the measurement). Two quantities:

- $\lambda_\zeta(k)=|\alpha_{\rm post}|/|\zeta(-\eta_B)|$ — the lab's $\lambda_\zeta$ with the
  numerically evolved $\zeta=\mu/a$ at the NEC boundary in the denominator.
- $G(k)=|\alpha_{\rm post}|/|\alpha_{\rm pre}+2\beta_{\rm pre}I_\infty|$ — the ratio of the true
  transfer to the **S1 super-Hubble prediction** $(\alpha,\beta)\to(\alpha+2\beta I_\infty,\beta)$.
  $G=1$ means the S1 formula is exact. $\Delta^2_\zeta$ ratio $=G^2$. **This is the quantity the
  $k\eta_B\lesssim10^{-2}$ band never tested.**

| $k\eta_B$ | Quintin $\lambda_\zeta$ | $G$ | $\Delta^2$ ratio | LQC $\lambda_\zeta$ | $G$ | $\Delta^2$ | poly $\lambda_\zeta$ | $G$ | $\Delta^2$ |
|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 5.971 | 1.0130 | 1.026 | 3.919 | 1.0380 | 1.077 | 4.898 | 0.9523 | 0.907 |
| 0.3 | 5.446 | 1.1057 | 1.223 | 3.553 | 1.2744 | 1.624 | 3.722 | 0.7433 | 0.552 |
| 1 | 3.543 | 1.2111 | 1.467 | 4.582 | 1.0491 | 1.101 | 0.952 | 0.2829 | 0.080 |
| 3 | (17.0)† | 1.0012 | 1.002 | (40.0)† | 0.9996 | 0.999 | (11.8)† | 0.9949 | 0.990 |
| 10 | (189.8)† | 0.9974 | 0.995 | (448.1)† | 1.0000 | 1.000 | (133.2)† | 1.0000 | 1.000 |

† For $k\eta_B\gtrsim1$ the mode is sub-Hubble at the bounce and $|\zeta(-\eta_B)|$ samples an
oscillation phase, so the $\lambda_\zeta$ column stops being a growth factor there and is flagged as
such in the log and on the figure. $G(k)$ stays well defined at all $k$ (both ends are projected,
not sampled) and is the quantity carried forward.

**Band extrema** (46-point log sweep, $k\eta_B\in[10^{-3},30]$), against the small-$k$ numerical
floor $|G-1|$ measured at $k\eta_B\le10^{-2}$ where S1 is exact by construction:

| background | floor $|G-1|$ | extremum $G$ | at $k\eta_B$ | $\Delta^2$ ratio | significant? |
|---|---|---|---|---|---|
| Quintin-type | $1.35\times10^{-2}$ | **1.328** | 0.768 | **1.76** | yes ($>5\times$ floor) |
| LQC dust | $2.18\times10^{-2}$ | **1.497** | 0.611 | **2.24** | yes |
| poly non-LQC | $8.35\times10^{-4}$ | **0.241** | 0.768 | **0.058** | yes |

The $1.3$–$2.2\%$ small-$k$ floor on the Quintin/LQC backgrounds is a systematic of the matter-basis
fit ($A$, $\eta_{\rm off}$) in the numerically-tabulated tails, not a physical $k$-dependence; it is
reported rather than subtracted, and every band feature exceeds it by more than an order of
magnitude. ODE convergence is far below it: $\le8.2\times10^{-8}$ for rtol $10^{-11}\to10^{-9}$ and
exactly $0$ for $\eta_{\rm far}\times2$.

**Shape of the result.** There *is* a real feature, and it lives exactly where the S1 band ends: a
single-decade transfer excursion peaking at $k\eta_B\simeq0.6$–$0.8$, dying to $|G-1|<1\%$ for
$k\eta_B\gtrsim3$ on all three backgrounds. Its **sign is background-dependent** — enhancement on
the Quintin-type ($\times1.76$ in $\Delta^2$) and LQC ($\times2.24$) backgrounds, strong suppression
on the poly background ($\times0.058$) — so it is a property of the individual $a(\eta)$ profile, not
a robust prediction of "a bounce". Figure: `lane9a_growth_vs_ketaB.png`.
