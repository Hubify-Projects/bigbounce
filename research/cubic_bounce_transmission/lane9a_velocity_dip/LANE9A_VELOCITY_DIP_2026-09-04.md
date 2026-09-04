# Ledger row 9 (A3-1e), lane (a) — scalar-field-velocity-dip amplification at kη_B ~ 1

**Date:** 2026-09-04 · **Status:** COMPLETE

## Question

Does the Quintin, Sherkatghanad, Cai & Brandenberger (2015, arXiv:1508.04141)
scalar-field-velocity-dip amplification of ζ through the bounce — their Eq. (79),
Δζ/ζ ~ [φ̇_B/φ̇(t_amp−)]² (the ~50 in the task framing is their *required* amplification,
their Eq. 30 — see §0) — exist on the lab's three
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

## 3. Eq. (79) evaluated for the lab's $\Upsilon$ and $\Delta t_B$

Parameter map (lane (c) §2.1, re-derived here): $\Upsilon=8/(3\Delta t_B^2)$ from matching $H$ at the
NEC boundary. The lab's grid point $\Delta t_B=1$ gives $\Upsilon=2.66667$ and $\eta_B=0.449601$ —
both confirmed by the run ($\dot H$ measured $=+2.66667$ at the bounce).

$$\Big[\frac{\dot\phi_B}{\dot\phi(t_{\rm amp-})}\Big]^2=\exp\!\Big(\frac{2\Delta t_{\rm amp}^2}{T^2}\Big)
\;\xrightarrow[\ \dot H=\Upsilon=\text{const}\ \Rightarrow\ \dot\phi^2=2M_p^2\Upsilon=\text{const}\ ]{}\;
\exp(0)=\mathbf{1}.$$

| background | Eq. (79) factor | why |
|---|---|---|
| Quintin-type ($\Upsilon=2.667$, $\Delta t_B=1$) | **1** | $\dot H$ constant to $7.2\times10^{-6}$ across the NEC window $\Rightarrow$ $|\dot\phi|$ constant $\Rightarrow T\to\infty$ |
| LQC effective dust | **1** | effective fluid; no matter-sector $\dot\phi$ exists to dip |
| poly non-LQC | **1** | pure geometric $a(\eta)$; no matter sector at all |

There is no free parameter left to tune here without *adding* a matter sector the lab has not
specified; if one is added, $T$ becomes a new input and Eq. (79) is a statement about that input, not
about the lab's backgrounds.

## 4. Consequences for $\Delta^2_\zeta$ and for $\Delta f_{\rm NL}^{\rm bounce}$

**Scheme label: S1** (geometric / dressed-metric extension: $z=a$, $\epsilon_{\rm eff}=1/2$,
$c_s=1$, $\eta_{\rm sr}=0$, $\lambda=0$), adiabatic-vacuum initial data, exact matter-basis
projection at both ends.

**(a) Curvature spectrum.** $\Delta^2_\zeta(k)$ is multiplied by $G(k)^2$ relative to the S1
extrapolation: $\le\!1.76$ (Quintin-type), $\le\!2.24$ (LQC), $\ge\!0.058$ (poly), all confined to
$k\eta_B\in[0.2,2]$ and back to $1\pm0.01$ by $k\eta_B=3$. Since $\lambda_\zeta$ itself is unchanged
in the super-Hubble band ($4.0$–$6.1$, matching the A2 brief), the CMB-anchored normalisation of the
lab's spectrum is untouched.

**(b) Cubic term.** Quintin Eq. (44), $f_{\rm NL}\sim(\Delta\zeta)^2/(\Delta t_BM_p^2)$, takes
$\Delta\zeta/\zeta=\lambda_\zeta-1$. With the Eq. (79) factor $=1$, $\lambda_\zeta$ stays at its
measured $4$–$6$, so the Eq. (44) *scaling* is unchanged from what lane (b) already normalises by
direct in-in integration: $\Delta f_{\rm NL}^{\rm bounce}=-0.1398$ / $-0.1043$ / $-0.1271$ and
$f_{\rm NL}^{\rm after}=-0.5008$ / $-0.6512$ / $-0.5548$ (Quintin / LQC / poly). Had the dip existed
with their $T=\Delta t_{\rm amp}$, $\Delta\zeta$ would have grown by $e^2=7.39$ and Eq. (44) would
have scaled $f_{\rm NL}^{\rm bounce}$ by $\sim55$ — the mechanism is real, it simply has no carrier
on these backgrounds.

A *scaling* estimate of the residual $k$-dependence: if every external leg near $k\eta_B\sim0.7$
carries $G(k)$, then $B\propto G^3$ and $(P_1P_2+{\rm perms})\propto G^4$, so $f_{\rm NL}\propto
1/G$ — a modulation of $0.75$ (Quintin), $0.67$ (LQC), $4.1$ (poly) confined to that one decade.
**This is a scaling argument, not an in-in computation**: the bounce-window vertex integral is
generated during the same interval in which the transfer acts, so the legs cannot be factorised
rigorously. Quantifying it properly is lane (b)'s job (§6 below).

**What is and is not covered.** *Covered:* the linear transfer of $\zeta$ through the bounce at
finite $k$ across $k\eta_B\in[10^{-3},30]$, on all three backgrounds, in S1, with the Eq. (79)
amplification question settled by derivation. *Not covered:* (i) the cubic in-in integral itself at
$k\eta_B\gtrsim10^{-2}$ — lane (b)'s assumption A1 still stands unrelaxed, and this lane shows the
error it hides is a factor $G^{3}/G^{4}$-type $O(1)$ effect in a single decade, not the $O(1)$ it was
assumed to be everywhere; (ii) any background with an actual matter-sector velocity profile
(two-field, ghost-condensate, Lee-Wick), where the dip and hence Eq. (79) can be non-trivial;
(iii) S2 (effective-fluid) scheme, which remains divergent (lane 9b).

## 5. VERDICT

**No velocity-dip amplification exists on the lab's three A2 backgrounds — the PTA and PBH nulls
stand — but a real, quantified, background-dependent $O(1)$ transfer feature does exist at
$k\eta_B\simeq0.6$–$0.8$, and it is not enough to reopen either channel.**

1. **Eq. (79) factor $=1$ on all three backgrounds**, by derivation on the Quintin-type background
   ($\dot H=\Upsilon$ constant $\Rightarrow$ $|\dot\phi|$ constant $\Rightarrow T\to\infty$) and by
   non-definability on the two effective-fluid backgrounds. The only geometry-fixed velocity,
   $\dot\phi^2=-2M_p^2\dot H$, vanishes at $\pm\eta_B$ by construction and is rejected as a
   substitute. The lab therefore sits in the *un-amplified* corner of Quintin's parameter space,
   which is exactly where their Conjecture 1 predicts small $f_{\rm NL}$ — and, symmetrically, no
   suppression of $r$. That remains a **cost** of the lab's scenario, recorded as such.
2. **The band $k\eta_B\in[0.1,10]$ does contain a genuine feature**, invisible to the S1 result:
   $\Delta^2_\zeta$ ratio $1.76$ (Quintin-type) / $2.24$ (LQC) / $0.058$ (poly), peaking at
   $k\eta_B=0.77/0.61/0.77$, against numerical floors of $1.4\times10^{-2}$/$2.2\times10^{-2}$/
   $8.4\times10^{-4}$. It changes sign between backgrounds, so it is a property of the individual
   $a(\eta)$, not of bouncing per se, and it cannot be quoted as a prediction.
3. **It cannot reopen PTA.** A3-3 already established that for $T_B\ge10^8$ GeV the *entire*
   NANOGrav band sits at $k\eta_B\le2.26\times10^{-8}$ — roughly eight decades in $k$ below this
   feature. A factor $\le2.24$ localised at $k\eta_B\sim0.7$ is not in the PTA band at all.
4. **It cannot reopen PBH.** A3-1b requires an amplitude ratio of $9.79\times10^{6}$
   ($\Delta^2$ delivered $6.49\times10^{-10}$ vs required $6.36\times10^{-3}$ at $f_{\rm PBH}=10^{-3}$,
   $M_H=10^{20}$ g). $2.24$ is short by a factor $4\times10^{6}$. Even the maximal-possible reading of
   Quintin's own required amplification, $\sim50$ in $\zeta$ ($2.5\times10^3$ in $\Delta^2$), would
   still fall four orders short.
5. **Honest bound on what a dip *could* buy, if a matter sector were added:** their
   $T=\Delta t_{\rm amp}$ gives $[\dot\phi_B/\dot\phi]^2=7.39$, and Eq. (44) then scales
   $f_{\rm NL}^{\rm bounce}$ by $\sim55$ — i.e. $\Delta f^{\rm bounce}_{\rm NL}\sim-7.7$ rather than
   $-0.14$. That is a *bispectrum* statement, not a spectrum one, and it does not move $\Delta^2$
   into the PBH/PTA windows either. This is the honest upper bound on the channel, and it costs a
   new, unconstrained matter-sector input to claim.

## 6. What lanes (b)/(c) and the paper must do next

- **Lane (b) — relax assumption A1 in one decade only.** A1 ($k\eta_B\le10^{-2}$ super-Hubble
  transfer) is now known to be violated at the $O(1)$ level only for $k\eta_B\in[0.2,2]$ and to be
  accurate to $<1\%$ for $k\eta_B\ge3$. The scoped follow-up is to re-run the in-in vertex integral
  with numerically evolved (not super-Hubble) legs at $k\eta_B=0.3,\,0.7,\,1$ on the Quintin-type
  background and compare with the $1/G$ scaling estimate of §4(b). Nothing outside that decade needs
  redoing.
- **Lane (c) — upgrade §2.3 item 2.** Replace "the lab's backgrounds carry no scalar-velocity dip"
  (assertion) with this lane's derivation, and add the rejected total-sector identification as the
  reason the substitution is not available. Add the sentence that the "$\sim\!50$" in Quintin is the
  *required* amplification (their Eq. 30), not an achieved one.
- **Paper (P2).** One sentence in the transmission section: the super-Hubble transfer is exact to
  $<1\%$ outside $k\eta_B\in[0.2,2]$, with an $O(1)$, background-dependent, sign-indefinite excursion
  inside it — disclosed, not modelled. No claim of a feature.
- **Ledger row 9.** Lane (a) closes as a **null for the amplification mechanism** with a quantified
  by-product (the $G(k)$ transfer curve). Do not open a PTA/PBH re-analysis on this basis.

## 7. Reproducibility

Manifest: `reproducibility/manifests/experiments/p2-a3-lane-9a-velocity-dip.json` (validated;
registered in `reproducibility/manifests/programs/bounce-theory.json`). Local, CPU-only, no network,
no seeds; 143.7 s measured, $0.00. Script `lane9a_velocity_dip.py`, outputs `results.json`,
`lane9a_velocity_dip.log`, `lane9a_growth_vs_ketaB.png`. Every number in this note comes from that
run; nothing was tuned toward an outcome, and the one result that would have been convenient —
an amplification at $k\eta_B\sim1$ — is reported as absent.
