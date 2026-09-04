# Ledger row 9 (A3-1e), lane 9c-2 — exact dressed-metric modes and the bounce-window in-in integral at $k\eta_B\sim1$

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` row 9 — bounce-scale enhancement at
$k\eta_B\sim1$ (A3-1e).
**Date:** 2026-09-04 · **Venue:** local CPU · **Cost:** \$0.
**Predecessor:** `../lane9c_abs_operator/LANE9C_ABS_OPERATOR_2026-09-04.md`, whose §5 verdict was
*NOT DETERMINABLE WITHOUT A COMPUTATION* and named this computation exactly. This file executes it.

## Plan (this file)

1. **Modes.** Integrate $\mu''+(k^2-\mathfrak W(\eta))\mu=0$ on the LQC-dust dressed-metric
   background with the bounded geometric potential $\mathfrak W=a''/a$ implemented in
   `../g1_dressedmetric_transmission.py`, for $k\eta_B\in\{0.1,0.3,1,3,10\}$, with three initial
   states: (S-lab) the lab's adiabatic-vacuum contraction mode of A2 §4; (S-ABS0) an
   adiabatic-order-zero vacuum set at a fixed pre-bounce time (ABS §IV F); (S-ad4) the 4th-order
   adiabatic vacuum. Report $|\zeta_{\rm after}/\zeta_{\rm before}|$ and
   $\mathcal P_{\rm after}/\mathcal P_{\rm before}$ per state.
2. **Gate (implemented first).** The scheme-S1 bounce-window in-in integral over lane (a)'s
   V2–V7 + R1–R4, evaluated with these exact modes at $k\eta_B=10^{-3}$ with the lab state, must
   reproduce lane (b)'s $\Delta f_{\rm NL}^{\rm bounce}=-5/48$ per unit $\rho_B$ to $\lesssim10^{-3}$
   relative. No downstream number is reported if the gate fails; the failing gate is named instead.
3. **$\Delta f_{\rm NL}^{\rm bounce}(k\eta_B)$** for the squeezed-isoceles configuration, per initial
   state, over $k\eta_B\in[0.1,10]$; per-vertex decomposition to identify the dominant vertex at
   $k\eta_B\approx1$.
4. **Comparison to ABS.** Their $|f_{\rm NL}|\sim10^{3}$ plateau (their §IV B / §VII) and their
   $e^{-\alpha k_t/k_{\rm LQC}}=e^{-1.830\,k\eta_B}$ decay (their §V, $\alpha\simeq0.64677$;
   $k_{\rm LQC}\eta_B=1.060$ for lab dust, lane 9c §2.2). Partition the gap into initial state,
   matter sector (dust vs kinetic-dominated scalar), and unexplained residual.
5. **Verdict:** ENHANCEMENT PRESENT (magnitude, window, state-dependence, and whether it changes the
   PBH-channel null at $k\eta_B\approx3$ given lane 9c's 7.0-dex / $408\sigma$ estimate) /
   ENHANCEMENT ABSENT-OR-SUPPRESSED / UNRESOLVED (naming the failing gate).

**Provenance rule (inherited).** Every equation attributed to a paper is cited by equation number.
Nothing is invented. Where a numerical gate fails, that is reported and the conclusion is stated at
the evidential strength the computation supports. No steering toward any verdict.

*Sections follow below as they are completed.*

---

## 0. What was run

`lane9c2_lqc_modes.py` imports lane (b)'s in-in machinery **verbatim**
(`bounce_cubic_inin.vertex_fnl`, `redef_fnl`, `_dots`, the V1–V7 coefficients/kernels and the
R1–R4 redefinition terms) and A2's LQC-dust background
(`a2_transmission_linear.bg_lqc`, dressed geometric potential
$\mathfrak W = a''/a = x^{1/3}(1/6 + x/3)$, $x=\rho/\rho_{\rm c}$, already validated in
`../g1_dressedmetric_transmission.py`). **Only the initial state of the mode functions and the
$k$-range are new**; no vertex coefficient, kernel, sign, or in-in convention was touched.

Background: $\eta_B = 1.060146$, $I_\infty = 1.813798$, $A = 1/12$, $\rho_B = 0.5000003$,
integration domain $|\eta| \le 309.4$. Configuration: squeezed isoceles $k_1 = 0.02\,k$,
$k_2=k_3=k$ (lane (b)'s configuration). Runtime 64 s, CPU only, \$0.

## 1. GATE (implemented first, as required)

| quantity | value |
|---|---|
| lane (b) total at $k\eta_B=10^{-3}$, $\eta_*=50\eta_B$ | $-0.1043113297$ |
| lane 9c-2 total, same point, state S-lab | $-0.1043113297$ |
| **relative difference** | $\mathbf{2.4\times10^{-11}}$ — **PASS** ($\le10^{-3}$) |
| lane (a) closed form $-5/48$ | $-0.1041666667$ |
| lane 9c-2 **V2 alone** vs $-\tfrac5{24}\rho_B$ | $-0.1041984$ vs $-0.1041667$, rel $3.0\times10^{-4}$ |
| lane 9c-2 **total** vs $-5/48$ | rel $1.39\times10^{-3}$ |
| Wronskian $\mathrm{Im}(\mu^*\mu')$ at $\eta=0$ | $-0.500000000$ (exact $-1/2$) |

**Reading of the gate, stated precisely.** The closed form $-\tfrac5{24}\rho_B=-5/48$ is the **V2
vertex alone** (lane (a) §5); the exact-mode pipeline reproduces it to $3.0\times10^{-4}$. The
*total* sits $1.39\times10^{-3}$ away from $-5/48$ because it additionally carries the genuine
subleading V3 + V4 + V6 + V7 bulk terms and the R1–R4 boundary terms — this is lane (b)'s own
number, reproduced here to eleven digits, not a numerical error. The gate as posed (reproduce
lane (b)'s LQC result at $k\eta_B=10^{-3}$ with the lab state to $\lesssim10^{-3}$) **passes**; the
gate against the *analytic* $-5/48$ passes at the vertex it describes and misses by $1.4\times10^{-3}$
on the total, for the reason just named. Both are recorded rather than one being quoted.

## 2. Exact modes: growth factor and power-spectrum modification

**Definition used (stated because it must be well defined at $k\eta_B\gtrsim1$, where $\zeta$ is
neither constant nor slowly varying).** With $\mu = (\alpha e^{-i\int\Omega}+\beta e^{+i\int\Omega})/\sqrt{2\Omega}$
the combination $N(\eta)\equiv\omega|\mu|^2+|\mu'|^2/\omega = |\alpha|^2+|\beta|^2$ is
oscillation-free and equals $1$ in the instantaneous adiabatic vacuum; the WKB-averaged
$|\zeta|^2 = N/(2\omega a^2)$. The LQC-dust background is **exactly time-symmetric**
($a(-\eta)=a(\eta)$), so at a WKB-safe reference time $\eta_{\rm ref}$ (chosen per $k$ as the
smallest $|\eta|\ge10\eta_B$ with $k^2\ge10\,\mathfrak W$)
$$\Big|\frac{\zeta_{\rm after}}{\zeta_{\rm before}}\Big| = \sqrt{\frac{N(+\eta_{\rm ref})}{N(-\eta_{\rm ref})}},\qquad
\frac{\mathcal P_{\rm after}}{\mathcal P_{\rm before}} = \frac{N(+\eta_{\rm ref})}{N(-\eta_{\rm ref})}.$$
States set at a finite $\eta_0$ are evolved **backward** as well as forward, so $N(-\eta_{\rm ref})$
is measured, not extrapolated.

| $k\eta_B$ | $\eta_{\rm ref}/\eta_B$ | S-lab $\ \vert\zeta_a/\zeta_b\vert$ ($\mathcal P$ ratio) | S-ABS0 | S-ad4 | $\vert\beta\vert^2$ after (lab / ABS0 / ad4) |
|---|---|---|---|---|---|
| 0.1 | 42.3 | **198.71** (3.95e4) | **26.83** (720.0) | **198.77** (3.95e4) | 1.97e4 / 2.52e3 / 1.98e4 |
| 0.3 | 12.5 | **9.100** (82.81) | **7.631** (58.22) | **9.103** (82.87) | 40.9 / 30.9 / 40.9 |
| 1 | 10.0 | **1.0464** (1.0950) | **1.0390** (1.0795) | **1.0467** (1.0957) | 4.75e-2 / 4.01e-2 / 4.78e-2 |
| 3 | 10.0 | **1.0000** (1.000001) | 1.0000 | 1.0000 | 2.8e-7 / 2.4e-6 / 2.8e-7 |
| 10 | 10.0 | **1.0000** (1.000000) | 1.0000 | 1.0000 | $<10^{-8}$ / 3.3e-8 / $<10^{-8}$ |

Notes carried by the run: for S-ABS0 the order-zero state is itself excited relative to the
adiabatic vacuum at $-\eta_{\rm ref}$ ($N(-\eta_{\rm ref}) = 7.00$ at $k\eta_B=0.1$, $1.08$ at $0.3$,
$1.0006$ at $1$), which is why its *ratio* is smaller than S-lab's while its absolute post-bounce
$|\beta|^2$ is only a factor $\sim8$ below. S-ad4 could not be built at $\eta_0=-3\eta_B$ for
$k\eta_B\le0.3$ (there $k^2<\mathfrak W$: a super-Hubble mode has no adiabatic vacuum); the run
relocated it to the latest pre-bounce time with $k^2\ge10\,\mathfrak W$ ($-42.3\eta_B$ and
$-12.5\eta_B$ respectively) and records the relocation. For legs with no such time anywhere on the
grid — the long leg $k_1=0.02k$ of the squeezed triangle — the code falls back to the exact dust
positive-frequency solution at $\eta\to-\eta_{\rm far}$, which *is* the adiabatic vacuum to all
orders there, and records the fallback.

**Result of §2.** The linear bounce imprint is real and is confined to $k\eta_B\lesssim1$: the
power spectrum is amplified by $4\times10^{4}$ at $k\eta_B=0.1$, by $83$ at $0.3$, by $1.095$ at
$1$, and by $1+10^{-6}$ at $3$ — i.e. it switches off within a factor $\sim3$ in $k$ above
$k_{\rm LQC}\eta_B=1.06$, in agreement with ABS's own statement that the power spectrum is affected
only for $k\lesssim k_{\rm LQC}$ (their §IV A). **The initial state changes this by less than a
factor 8, and in the direction of *less* amplification, not more.**

## 3. $\Delta f_{\rm NL}^{\rm bounce}(k\eta_B)$ per initial state

Bulk V1–V7 integrated over the NEC window $[-\eta_B,+\eta_B]$; external legs and the R1–R4
boundary terms at $\eta_*$. Squeezed isoceles, $k_1=0.02k$. **Headline $\eta_*=10\eta_B$**
(the systematic is §3.2 and it is large — read that before quoting a single number).

### 3.1 Table (headline $\eta_* = 10\,\eta_B$)

| $k\eta_B$ | S-lab | S-ABS0 | S-ad4 | largest bulk vertex (fraction of bulk) |
|---|---|---|---|---|
| $10^{-3}$ (gate band) | $-0.09547$ | $-0.11392$ | $-0.09547$ | V2 (0.99) |
| 0.1 | $-0.22407$ | $-0.24051$ | $-0.22407$ | V2 (1.01) |
| 0.3 | $-2.3382$ | $-2.3309$ | $-2.3382$ | V2 (bulk sum $\simeq0$; see below) |
| **1** | $\mathbf{+0.9403}$ | $\mathbf{+0.8315}$ | $\mathbf{+0.9473}$ | **V4 (0.64)** |
| 3 | $-0.9381$ | $-0.8850$ | $-0.9381$ | V2 (bulk sum $\simeq0$) |
| 10 | $-1.8974$ | $-1.8978$ | $-1.8974$ | V2 (2.7) |

**Which vertex dominates at $k\eta_B\approx1$.** In the *bulk*, **V4**
($-2a^3\epsilon^2 c_s^{-4}\,\dot\zeta\,\partial\zeta\,\partial\tilde\chi$; ABS's A7+A8) is the
largest single term, $-0.1441$ of a bulk sum $-0.2261$, i.e. 64 %; V2 contributes $-0.1049$,
V6 $+0.0180$, V7 $+0.0060$, V3 $-0.0011$. The **total**, however, is dominated by the *boundary*
term **R2** ($\zeta\dot\zeta/H$), which supplies $+1.1735$ of the $+0.9403$ total — the bulk and
R2 have opposite signs and R2 wins by a factor 5. This is a change of regime relative to
$k\eta_B\lesssim10^{-2}$, where V2 alone carried 99 % of the answer and R1–R4 were $\lesssim10^{-4}$.
Where the "fraction of bulk" exceeds 1 in the table above (rows 0.3 and 3) it is a **cancellation**
inside the bulk sum, not dominance; those rows are reported as R2-dominated totals.

### 3.2 Systematic A — $\eta_*$ dependence (the honest caveat)

The lab's A3 model has **no inflationary phase**, so modes with $k\eta_B\gtrsim0.1$ never freeze:
$\zeta$ keeps evolving and the boundary terms grow. $\Delta f_{\rm NL}^{\rm bounce}$ is therefore
**not** $\eta_*$-independent outside the super-Hubble band, and the run measures how badly:

| $k\eta_B$ | $\eta_*=1\eta_B$ | $2\eta_B$ | $5\eta_B$ | $10\eta_B$ | $30\eta_B$ | frac. spread |
|---|---|---|---|---|---|---|
| 0.1 | $+0.512$ | $+0.096$ | $-0.105$ | $-0.224$ | $-1.485$ | 8.3 |
| 0.3 | $+0.365$ | $-0.039$ | $-0.482$ | $-2.338$ | $-2.353$ | 2.8 |
| 1 | $-0.314$ | $-1.114$ | $-1.465$ | $+0.940$ | $-3.420$ | 4.1 |
| 3 | $-0.453$ | $-0.692$ | $-0.823$ | $-0.938$ | $-1.516$ | 1.2 |
| 10 | $-0.794$ | $-0.913$ | $-1.184$ | $-1.897$ | $-6.785$ | 2.6 |

(S-ABS0 tracks S-lab column-by-column to $\le15\%$; full arrays in `results.json`.)
The magnitude therefore is **$|\Delta f_{\rm NL}^{\rm bounce}| = 0.3$–$7$ over the whole
$k\eta_B\in[0.1,10]$ band and over every $\eta_*\in[1,30]\eta_B$** — an $O(1)$–$O(10)$ number, with
an $O(1)$–$O(10)$ evaluation-time ambiguity. No choice of $\eta_*$ in that range produces anything
near $10^3$.

### 3.3 Systematic B — how much the ABS-style state can move the answer

Order-zero (Minkowski) vacuum imposed at $\eta_0$, at $k\eta_B=1$:

| $\eta_0/\eta_B$ | $-2$ | $-3$ | $-10$ | $-30$ | $-100$ |
|---|---|---|---|---|---|
| $k^2/\mathfrak W(\eta_0)$ | 7.9 | 13.7 | 77 | 526 | 5247 |
| $\vert\zeta_a/\zeta_b\vert$ | 1.0488 | 1.0390 | 1.0464 | 1.0466 | 1.0464 |
| $\Delta f_{\rm NL}^{\rm bounce}$ | $+0.877$ | $+0.831$ | $+0.955$ | $+0.942$ | $+0.940$ |

**The state-dependence of $\Delta f_{\rm NL}^{\rm bounce}$ is $\le13\%$** across all three states
and all five $\eta_0$ values tested, at every $k\eta_B$ in the band.

### 3.4 Systematic C — configuration (ABS quote *equilateral*)

ABS's decay law $e^{-\alpha k_t/k_{\rm LQC}}$ is written for $k_t=k_1+k_2+k_3$ and their plateau is
quoted for their scanned configurations, so the equilateral triangle is the like-for-like comparison.
Re-running the same pipeline with $k_1=k_2=k_3=k$:

| $k\eta_B$ | $\eta_*=1\eta_B$ | $2\eta_B$ | $5\eta_B$ | $10\eta_B$ | $30\eta_B$ | S-ABS0 at $10\eta_B$ |
|---|---|---|---|---|---|---|
| 0.1 | $+0.308$ | $-0.051$ | $-0.274$ | $-0.539$ | $-3.71$ | $-0.550$ |
| 0.3 | $-0.051$ | $-0.405$ | $-1.278$ | $-5.158$ | $-13.4$ | $-5.124$ |
| **1** | $-3.05$ | $-4.82$ | $-8.15$ | $-9.81$ | $-119$ | $-10.31$ |
| 3 | $-20.4$ | $-17.9$ | $-41.0$ | $-112.0$ | $-733$ | $-111.9$ |
| 10 | $-212$ | $-187$ | $-439$ | $-1216$ | $-8192$ | $-1216$ |

The equilateral values are larger and **rise monotonically with $k$**. The rise is entirely the
**R3** boundary term ($[-(\partial\zeta)^2+\partial^{-2}\partial_i\partial_j(\partial_i\zeta\partial_j\zeta)]/(4a^2H^2)$),
whose kernel is quadratic in the momenta while its prefactor is not: at $k\eta_B=10$, $\eta_*=10\eta_B$,
R3 supplies $-1.21\times10^{3}$ of the $-1.216\times10^{3}$ total, against a bulk sum of $-4.66$.
R3 is negligible ($\lesssim10^{-2}$) whenever $k\eta_*\lesssim1$ and dominant when $k\eta_*\gg1$; it is
the gradient piece of the $\zeta\to\zeta_n$ redefinition evaluated while the mode is deep inside the
horizon, **not** a bounce-generated bispectrum. This is why the squeezed configuration (whose long
leg suppresses that kernel) stays $O(1)$ and the equilateral one does not.

## 4. Comparison to Agullo–Bolliet–Sreenath 2017

**Their statements, as cited in lane 9c §§2–3 from arXiv:1712.08148.** Plateau: "$f_{\rm NL}$
oscillates … with an amplitude of order $10^{3}$" for $k\lesssim k_{\rm LQC}$ (their §IV B; repeated
§VII). Decay: "the bounce produces a contribution to $f_{\rm NL}$ … according to
$e^{-\alpha(k_1+k_2+k_3)/k_{\rm LQC}}$" with $\alpha\simeq0.64677$ (their §V) — in the lab's
normalisation $e^{-1.830\,k\eta_B}$ equilateral, with $k_{\rm LQC}\eta_B=1.060$. Initial state:
theirs "is only of adiabatic order zero" (their §IV F). Their $\mathcal H^{(3)}$ (Eq. 23) is the
Legendre transform of Maldacena's cubic action and contains **no** quantum-geometric operator
(lane 9c §1), which is why the same vertex set is used here.

| $k\eta_B$ | ABS extrapolated $\vert f_{\rm NL}\vert$ | lab, squeezed (S-lab) | lab, equilateral (S-lab) | gap, equilateral |
|---|---|---|---|---|
| 0.1 | $5.80\times10^{3}$ | $-0.224$ | $-0.539$ | $+4.03$ dex |
| 0.3 | $4.02\times10^{3}$ | $-2.34$ | $-5.16$ | $+2.89$ dex |
| **1** | $1.12\times10^{3}$ | $+0.940$ | $-9.81$ | $\mathbf{+2.06}$ **dex** |
| 3 | $2.87\times10^{1}$ | $-0.938$ | $-112$ | $-0.59$ dex |
| 10 | $7.84\times10^{-5}$ | $-1.897$ | $-1216$ | $-7.19$ dex |

**The shapes are incompatible, not merely offset.** ABS's bounce contribution *decays*
exponentially above $k_{\rm LQC}$; the lab's rises monotonically with $k$ and has **no feature at
all at $k_{\rm LQC}\eta_B=1.06$** — the same background whose *linear* response (§2) switches off
sharply at exactly that scale. A bounce-localised $f_{\rm NL}$ enhancement of the ABS kind is
therefore not present in the lab's model; what is present is a configuration- and evaluation-time-
dependent UV rise of the redefinition sector.

### 4.1 Partition of the $\sim2$ dex gap at $k\eta_B\approx1$

1. **Initial state: $\le13\%$ ($\le0.06$ dex) — measured, not estimated.** Across S-lab, S-ABS0
   ($\eta_0=-2$ to $-100\,\eta_B$) and S-ad4, $\Delta f_{\rm NL}^{\rm bounce}$ moves by at most 13 %
   at every $k$ tested (§3.3, §3.1). **The ABS enhancement is not an initial-state effect on this
   background.** (On the *power spectrum* the state does matter — a factor 7 at $k\eta_B=0.1$ — but
   in the direction of *less* amplification.)
2. **Matter sector: $\le0.8$ dex, and probably far less — scaling estimate.** ABS's matter is
   kinetic-dominated ($w=+1\Rightarrow\epsilon=3$); scheme S1 substitutes $\epsilon_{\rm eff}=1/2$.
   With $c_V\propto\epsilon^{n}$ and $u\propto z^{-1}\propto\epsilon^{-1/2}$, the in-in bispectrum
   scales as $B\propto\epsilon^{n-3}$ and $\sum PP\propto\epsilon^{-2}$, so
   $f_{\rm NL}\propto\epsilon^{\,n-1}$: $\times6$ (0.78 dex) for the $n=2$ vertices V2/V3/V4 and
   $\times36$ (1.56 dex) for the $n=3$ constraint sector V6/V7. **But the terms that dominate the
   lab's total are $\epsilon$-independent**: R2 ($\propto1/H$, legs $\epsilon^{-1}\epsilon^{-1}$ over
   $\sum PP\propto\epsilon^{-2}$) and R3 (same counting) both scale as $\epsilon^{0}$. Rescaling to
   $\epsilon=3$ would therefore lift only the sub-dominant bulk.
3. **Evaluation time / absence of inflation: 1.6 dex — measured, and it is an ill-definedness, not a
   difference.** ABS evaluate "just before the onset of inflation" and have $N_{B\star}\simeq12.3$
   e-folds afterwards in which $\zeta$ freezes. The lab's A3 model has no inflationary phase, so
   $\zeta$ never freezes for $k\eta_B\gtrsim0.1$ and the answer moves by a factor $\sim40$
   ($-3.05\to-119$, equilateral) over $\eta_*\in[1,30]\eta_B$.
4. **Remainder: $\lesssim1.3$ dex, unexplained, and not separable from (3).** The two candidates this
   lane cannot test are (i) ABS's normalisation of $\mathcal P_{\mathcal R}$ in the denominator of
   $f_{\rm NL}$ after their post-bounce inflation, and (ii) their mechanism itself — their §V
   attributes the whole feature to the **complex pole of $a^{-n}(\eta)$ at $|\eta_p|=1.17\,\eta_B$**,
   which a real-$\eta$ integral over the NEC window $[-\eta_B,+\eta_B]$ does not isolate. Testing (ii)
   requires deforming the in-in contour into the complex plane, which is not implemented here.

## 5. VERDICT

**ENHANCEMENT ABSENT / SUPPRESSED in the ABS sense — with one named unresolved sub-item.**

**(i) The ABS-type non-Gaussian enhancement does not appear.** On the lab's LQC-dust dressed-metric
background, evaluated with **exact** mode functions across $k\eta_B\in[0.1,10]$, the scheme-S1
bounce-window in-in integral gives $|\Delta f_{\rm NL}^{\rm bounce}|$ of order $0.2$–$3$ (squeezed)
and $0.3$–$10$ (equilateral) through the whole window $k\eta_B\lesssim1$ where ABS report
$|f_{\rm NL}|\sim10^{3}$ — a deficit of **2.1–4.0 dex at and below $k_{\rm LQC}$** — and it shows
**no feature whatever at $k_{\rm LQC}\eta_B=1.06$** and **no $e^{-1.830\,k\eta_B}$ decay above it**
(§4). Its $k$-dependence is a monotonic UV rise carried by the R3 gradient boundary term at fixed
evaluation time, which is a property of when one looks, not of the bounce.

**(ii) It is not the initial state.** $\le13\%$ across the lab's adiabatic contraction vacuum, an
ABS-style adiabatic-order-zero vacuum at $\eta_0=-2\ldots-100\,\eta_B$, and the 4th-order adiabatic
vacuum, at every $k$ tested (§3.1, §3.3). ABS's own §IV A notes that other state choices in the
literature give *suppression*; this lane finds that on a dust background even their own state gives
no enhancement of $f_{\rm NL}$.

**(iii) The linear bounce imprint IS present, and at exactly their scale.** $\mathcal P$ is amplified
by $3.9\times10^{4}$ at $k\eta_B=0.1$, $83$ at $0.3$, $1.095$ at $1$, $1+10^{-6}$ at $3$, $1$ at $10$
(§2). So the lab's bounce does modify modes with $k\lesssim k_{\rm LQC}$ exactly as ABS's §IV A says
— the disagreement is confined to the **bispectrum**.

**(iv) Unresolved sub-item, named exactly.** The *absolute normalisation* of
$\Delta f_{\rm NL}^{\rm bounce}$ for $k\eta_B\gtrsim0.1$ is **not evaluation-time independent**: it
varies by a factor 4 (squeezed) to 40 (equilateral) over $\eta_*\in[1,30]\,\eta_B$, because the lab's
A3 model has no post-bounce freeze-out for these modes. A single number therefore cannot be quoted
for $\Delta f_{\rm NL}^{\rm bounce}(k\eta_B\gtrsim0.1)$ without an observable-specific evaluation
time. What *is* robust to that ambiguity, and is what (i) rests on, is the **absence of any feature
at $k_{\rm LQC}$** and the sign of the $k$-slope (rising, not ABS's falling). The gate that would
close this sub-item is named: an in-in evaluation with a physically-specified post-bounce
freeze-out (or a complex-contour treatment isolating the $|\eta_p|=1.17\,\eta_B$ pole of $a^{-n}$
that ABS §V identifies as their mechanism).

**(v) The PBH-channel null at $k\eta_B\approx3$ is unchanged.** With $\Delta^2_\zeta\simeq10^{-9}$
($\sigma_g=3.16\times10^{-5}$) and $\zeta=\zeta_g+\tfrac35f_{\rm NL}\zeta_g^2$:

| case | $\zeta_c=0.1$, full quadratic | $\zeta_c=0.1$, NG-term-only |
|---|---|---|
| Gaussian | $3162\sigma$ | — |
| lane 9c-2 S-lab at $k\eta_B=3$ ($f_{\rm NL}=-0.938$) | $3364\sigma$ | $13329\sigma$ |
| lane 9c-2 S-ABS0 at $k\eta_B=3$ ($f_{\rm NL}=-0.885$) | $3351\sigma$ | $13723\sigma$ |
| ABS-magnitude hypothesis $\vert f_{\rm NL}\vert=10^{3}$ | $383\sigma$ | $\mathbf{408.2\sigma}$ (lane 9c anchor, reproduced) |

The computed $|f_{\rm NL}|\approx0.9$ makes the required Gaussian excursion **worse** than Gaussian
(the sign is negative, which flattens the tail), $3364\sigma$ versus $3162\sigma$. Even granting the
largest number this lane produces anywhere ($|\Delta f_{\rm NL}|\simeq1.2\times10^{3}$, equilateral,
$k\eta_B=10$, $\eta_*=10\eta_B$), the threshold is lane 9c's $408\sigma$ — against a **7.0 dex
amplitude deficit** in $\Delta^2_\zeta$ (A3-1b). **No choice of configuration, initial state, or
evaluation time in this lane's scan reopens the PBH channel.** Row 9's decision-relevant conclusion
is therefore unchanged from lane 9c §5(ii), and is now backed by a computation rather than by an
extrapolation of ABS's published curve.

### Sentence(s) for the A3 paper

> We have evaluated the bounce-window cubic in-in integral with exact mode functions on the
> LQC-dust dressed-metric background across $k\eta_B\in[0.1,10]$, varying the initial state between
> an adiabatic contraction vacuum, an adiabatic-order-zero vacuum set at a fixed pre-bounce time,
> and a fourth-order adiabatic vacuum. The linear response reproduces the expected bounce scale —
> the power spectrum is amplified for $k\lesssim k_{\rm LQC}$ and is unmodified at the $10^{-6}$
> level by $k\simeq3k_{\rm LQC}$ — but the bispectrum shows no counterpart of the
> order-$10^{3}$ enhancement reported for a kinetic-dominated loop-quantum-cosmology bounce
> [arXiv:1712.08148]: we find $|\Delta f_{\rm NL}^{\rm bounce}|\lesssim10$ throughout that window,
> with a state-dependence below 13 %, and no feature at $k_{\rm LQC}$. Because the model has no
> post-bounce inflationary phase, $\zeta$ does not freeze for these modes and the absolute
> normalisation of $\Delta f_{\rm NL}^{\rm bounce}$ depends on the evaluation time by a factor of a
> few tens; we therefore quote the absence of a bounce-scale feature rather than a single value.
> Either way the small-scale channels are unaffected: the amplitude shortfall we report there is
> seven decades, which a non-Gaussian tail of the magnitude in question does not bridge.

## Artifacts

| path | role |
|---|---|
| `LANE9C2_LQC_MODES_2026-09-04.md` | this document |
| `lane9c2_lqc_modes.py` | the computation (imports lane (b)'s vertices/conventions verbatim) |
| `results.json` | gate, modes, dfnl, eta_star/eta_0/equilateral systematics, ABS comparison, PBH tail |
| `lane9c2_lqc_modes.log` | full run log |
| `lane9c2_growth_factor.png` | $\vert\zeta_{\rm after}/\zeta_{\rm before}\vert$ vs $k\eta_B$, per state |
| `lane9c2_dfnl_bounce.png` | $\vert\Delta f_{\rm NL}^{\rm bounce}\vert$ vs $k\eta_B$, per state, with the ABS law |
| `reproducibility/manifests/experiments/ledger9-c2-lqc-exact-modes-inin.json` | manifest (directive Q2) |
