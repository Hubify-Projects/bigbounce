# Lane 9b — S2 regularisation of Δf_NL^bounce (ledger row 9 / A3-1e, lane b)

**Date:** 2026-09-04 · **Owner:** Claude lane 9b · **Status:** DONE (structural verdict; value step named).
**Artifacts (this dir):** `lane9b_s2_regulation.py` → `lane9b_s2_regulation.json`, `lane9b_s2_regulation.log`;
manifest `reproducibility/manifests/experiments/p2-a3-lane-9b-s2-regularisation.json`.
**Venue:** local CPU (sympy 1.14), $0, ~1 s. **Provenance rule:** everything marked *computed* is produced by the
committed script; *literature* statements are cited, not re-derived; Quintin+2015 equation numbers are **not**
asserted (see §5 iii — offline lane, no verified copy of the paper).

## 0. Question and answer in one paragraph

Lane (a)/(b) found the effective-fluid scheme S2 ($z^2=2a^2\epsilon/c_s^2$, pole at $H=0$) gives a divergent
bounce-window cubic contribution (V6+V7 $\propto d_{\rm cut}^{-1}$), while the geometric scheme S1 ($z=a$) gives
$\Delta f_{\rm NL}^{\rm bounce}[{\rm V2}]=-\tfrac{5}{24}\rho_B$. **Result (computed):** the S2 divergence is an artefact
of the *form* of the cubic action, not of the fluid physics at $H=0$. On the exact linear solution of the S2
Mukhanov–Sasaki equation through the bounce, the comoving-gauge constraint solutions
$N_1=\dot\zeta/H$ and $\psi=-\zeta/H+\chi$ are **regular at $H=0$** — the $1/H$ poles of $-\zeta/H$ and of
$\chi=-a^2\epsilon\dot\zeta/(c_s^2k^2)$ cancel identically (residues $\mp1/\Upsilon$, §2). Hence the raw ADM cubic
Lagrangian (Maldacena 2003 Eq. 2.9–2.11 form, before integrations by parts), whose coefficients are polynomials in
$(a,H,\dot\phi,V)$ — all finite at the bounce — is **finite on-shell through $H=0$**. The Maldacena/Chen form used by
lanes (a),(b) differs from it by total time derivatives $\dot F$ whose antiderivative $F$ is built with explicit
$1/H$ and $\epsilon=\dot\phi^2/2H^2$ and is singular *at* the bounce; $\int\dot F\,dt$ across $t=0$ is not
$F(t_B)-F(-t_B)$, and that is the whole divergence. **No cutoff is needed and none is legitimate.** What this lane
does *not* deliver is the finite S2 number: it requires the raw-form in-in integral (§6), so equality with S1's
$-\tfrac{5}{24}\rho_B$ is **not** established and must not be claimed.

## 1. Background and the exact S2 mode functions at the bounce (computed, script §A)

Quintin+2015-type bounce phase: $H=\Upsilon t$, $a=e^{\Upsilon t^2/2}$, $\epsilon=-1/(\Upsilon t^2)$,
$\rho+p=\dot\phi^2=-2\dot H=-2\Upsilon$ (NEC violation; in a $P(X,\phi)$ fluid this is $P_X<0$, i.e. the quadratic
action has $z^2<0$ throughout the window — a ghost. Lane (b) used these modes anyway; we do the same, flagged.)
$$z^2=\frac{2a^2\epsilon}{c_s^2}=-\frac{2e^{\Upsilon t^2}}{\Upsilon c_s^2t^2},\qquad
\int z^2\,dt=\frac{1}{\Upsilon c_s^2}\Big(\frac{2}{t}-2\Upsilon t-\tfrac13\Upsilon^2t^3\Big)+\dots$$
The MS equation $\frac{d}{dt}\big(\tfrac{z^2}{a}\dot\zeta\big)+c_s^2k^2az^2\zeta=0$ has indicial exponents $0$ and $3$
at $t=0$; the Frobenius solution (residual $=0$ through $O(t^2)$ with all solved coefficients) is
$$\zeta=C_1\Big[1+\tfrac12c_s^2k^2t^2-\big(\tfrac12\Upsilon c_s^2k^2+\tfrac18c_s^4k^4\big)t^4+\dots\Big]
+C_2\Big[t^3-\big(\tfrac3{10}\Upsilon+\tfrac1{10}c_s^2k^2\big)t^5+\dots\Big].$$
**The point lane (a) missed:** $\dot\zeta|_{C_1}=c_s^2k^2t+\dots\propto H$, not $H^2$. The constant mode's
$k^2$ correction is $1/t$-enhanced by $\int z^2dt\sim 2/(\Upsilon c_s^2t)$, so on the bounce window it is *not*
subleading to the $C_2$ mode ($\dot\zeta|_{C_2}=3t^2$). Lane (a)'s S2 pole table assumed $\dot\zeta\propto H^2$ for
every leg; that is the $C_2$-only sub-case.

## 2. The decisive computation: the comoving-gauge metric is regular at $H=0$ (computed, script §B)

Comoving gauge, ADM: $N=1+N_1$, $N_i=\partial_i\psi$, with the linear constraint solutions (Maldacena 2003
Eq. 2.13–2.14; Chen+2007 Eq. 3.5–3.6, *literature*): $N_1=\dot\zeta/H$, $\psi=-\zeta/H+\chi$,
$\partial^2\chi=a^2\epsilon\dot\zeta/c_s^2$. Laurent expansions on the exact modes of §1:

| quantity | $C_1$ mode | $C_2$ mode |
|---|---|---|
| $N_1=\dot\zeta/H$ | $c_s^2k^2/\Upsilon+O(t^2)$ | $3t/\Upsilon$ |
| $-\zeta/H$ | $-\dfrac{1}{\Upsilon t}+\dots$ | $-t^2/\Upsilon$ |
| $\chi=-a^2\epsilon\dot\zeta/(c_s^2k^2)$ | $+\dfrac{1}{\Upsilon t}+\dots$ | $3/(\Upsilon c_s^2k^2)$ |
| $\psi=-\zeta/H+\chi$ | $-\dfrac{\Upsilon+c_s^2k^2}{\Upsilon}\,t+O(t^2)$ | $3/(\Upsilon c_s^2k^2)$ |

$$\boxed{\;{\rm Res}_{t=0}\Big[-\frac{\zeta}{H}\Big]_{C_1}=-\frac1\Upsilon,\qquad {\rm Res}_{t=0}[\chi]_{C_1}=+\frac1\Upsilon,\qquad
\psi=-\frac{\zeta}{H}+\chi\ \text{is regular at }H=0\;}$$
for every $c_s$ and $k$. Physically: the comoving-gauge shift is $B_c=-\delta\phi_N/\dot\phi$ (the time shift from
Newtonian to comoving slicing), and $\dot\phi=\sqrt{2\Upsilon}\neq0$ at the bounce, so the linear comoving-gauge
metric is finite at $H=0$. The $1/H$ that lane (a) traced to "the constraint solution" is real in each *piece* but
absent in the *metric*. The cancellation fails if $\dot\zeta\propto H^2$ is assumed (then $\chi$ is finite and
$-\zeta/H$ is not), which is exactly lane (a)'s counting.

## 3. What this does to the Maldacena/Chen-form vertices on the exact modes (computed, script §C)

Cosmic-time integrand pole orders, three legs, with the $C_1$ mode on every leg ($\dot\zeta\propto k^2t$) versus
lane (a)'s $[C_1,C_2,C_2]$ weights ($\dot\zeta\propto t^2$):

| vertex | exact modes $[C_1^3]$ | lane (a) weights $[C_1,C_2,C_2]$ | class |
|---|---|---|---|
| V2 $a^3\epsilon^2\zeta\dot\zeta^2$ | $t^{-2}$, lead $c_s^4k^4/\Upsilon^2$ | $t^{0}$ | **non-integrable** (was "finite") |
| V3 $a\epsilon^2\zeta(\partial\zeta)^2$ | $t^{-4}$ | $t^{-4}$ | non-integrable |
| V4 $-2a^3\epsilon^2\dot\zeta\partial\zeta\partial\tilde\chi$ | $t^{-2}$ | $t^{0}$ | **non-integrable** (was "finite") |
| V5 $\tfrac12a^3\epsilon\dot\eta_{\rm sr}\zeta^2\dot\zeta$ | $t^{-4}$ (even!) | $t^{-3}$ odd | non-integrable (was "PV-finite") |
| V6+V7 $\tfrac34a^3\epsilon^3\zeta\dot\zeta^2$-type | $t^{-4}$, lead $-\tfrac34c_s^4k^4/\Upsilon^3$ | $t^{-2}$ ($d_{\rm cut}^{-1}$, lane b) | non-integrable |

So the honest S2 statement in the Maldacena form is *worse* than lanes (a),(b) reported: with the exact modes every
bulk vertex, including V2 and V4, has an even non-integrable pole at the bounce, and the $k^4$ factors show these
are the $k^2$-corrections of the constant mode squared — precisely the sector whose $\int z^2dt\sim1/t$ enhancement
the super-Hubble reduction discards. This is also the cubic-order face of the lab's linear finding
(`g1_gradient_transmission_scheme.py`: the S2 gradient-transmission coefficient scales as $d_{\rm cut}^{-1}$).

## 4. Why the raw ADM form is finite and the integrated-by-parts form is not (computed §D + literature)

Maldacena 2003 Eq. 2.9–2.11 (*literature*): $\mathcal L=\tfrac12\sqrt h\,[NR^{(3)}-2NV+N^{-1}(E_{ij}E^{ij}-E^2)+N^{-1}\dot\phi^2]$
with $h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $N=1+N_1$, $N_i=\partial_i\psi$. Expanded to cubic order *before* any
integration by parts, every coefficient is a polynomial in $\{a^{\pm1},H,\dot\phi,V\}$ (from $\dot h_{ij}=2a^2e^{2\zeta}(H+\dot\zeta)\delta_{ij}$,
$V=3H^2-\dot\phi^2/2$) and in $1/N=1-N_1+N_1^2-\dots$, multiplying products of $\{\zeta,\dot\zeta,N_1,\psi\}$ and
gradients. No $1/H$ appears explicitly. Building-block Laurent orders on the exact modes (script §D):
$\zeta\sim t^0$, $\dot\zeta\sim t^1$, $N_1\sim t^0$, $\psi\sim t^0$, $H\sim t$, $\dot\phi^2=2\Upsilon$,
$V\to-\Upsilon$, $a\to1$ — **all regular**, so the on-shell cubic integrand is finite through $H=0$ and the
bounce-window in-in integral in the raw form is absolutely convergent (for $k\eta_B$ finite).

The passage to the Maldacena/Chen form (Maldacena Eq. 3.8→3.9; Chen+2007 Eq. 4.28–4.29; Seery–Lidsey Eq. 51,
*literature*) integrates by parts in time repeatedly, using the background equations to trade $\dot\phi^2\to2\epsilon H^2$,
$\ddot\phi$, $\dot H$ for $\epsilon,\eta_{\rm sr}$ and introducing $1/H$ through $N_1=\dot\zeta/H$ and $\psi\ni-\zeta/H$
*separately*. The result is
$\mathcal L_{\rm Mald}=\mathcal L_{\rm raw}+\dot F+(\text{terms}\propto\delta L_2/\delta\zeta)$, where $F$ is a
cubic functional carrying explicit $1/H^n$ and $\epsilon^n$ — e.g. the field-redefinition pieces R2 $\zeta\dot\zeta/(c_s^2H)$,
R3 $(\partial\zeta)^2/(4a^2H^2)$, R4 $\epsilon(\dots)/(2c_s^2H)$ of lane (a) are exactly such boundary functionals and lane (a)
already found them singular *at* the bounce. On an interval containing $t=0$,
$$\int_{-t_B}^{t_B}\dot F\,dt\neq F(t_B)-F(-t_B)\quad\text{when }F\text{ has a pole at }t=0,$$
so the Maldacena-form bulk integral inherits the pole of $F$ (even $t^{-2}$ or $t^{-4}$ integrands from
$F\propto t^{-1},t^{-3}$, giving $d_{\rm cut}^{-1},d_{\rm cut}^{-3}$ — lane (b)'s measured slope $-1.005$ is the $[C_1,C_2,C_2]$
member of this family). The physical bispectrum is the raw-form one; equivalently it is the Maldacena-form integral
*plus* $F(0^+)-F(0^-)$-type subtractions — which no symmetric excision, $H^2\to H^2+\mu^2$ smoothing or principal
value reproduces in general (they reproduce it only if the singular part of $F$ is even in $t$, which for $F\propto t^{-1}$
with even coefficient it is not).

## 5. The four candidate regularisations, dispositioned

**(i) Correct variable — RESOLVED, this is the answer.** Not $v=z\zeta$: in S2 $v\propto\zeta/|t|$ has a $t^{-1}$
pole for the $C_1$ mode (Frobenius exponents of $v''+(k^2-z''/z)v=0$ with $z''/z=2/t^2$ are $-1$ and $2$), so $v$ is
the *wrong* variable at the bounce. $\zeta$ itself is regular (§1), the Bardeen potential is regular
($\Psi_N=H\chi\propto k^{-2}\dot\zeta\,a^2\epsilon H$: finite, $\to C_1$-dependent constant), and — the decisive point —
the comoving-gauge *metric* $(N_1,\psi)$ is regular (§2). The finite object is the raw ADM cubic action in any of
comoving/Newtonian gauge; the singular object is the integrated-by-parts $\zeta$-vertex table. (Battefeld & Peter
2015 arXiv:1406.2790, Peter & Pinto-Neto, Xue & Steinhardt — *literature*, cited for the linear-order statement that
$\Phi$ is regular through $H=0$ while $\zeta$-based pieces individually are not; not re-derived here.)

**(ii) PV for odd poles + V6/V7 cancellation against the redefinition terms — SUBSUMED, and PV alone is wrong.**
On the exact modes V5 is an *even* $t^{-4}$ pole (not odd), so PV does not define it. The cancellation is real but is
between the bulk poles and the singular total derivatives $\dot F$ (§4), of which R1–R4 are the boundary-evaluated
part; evaluating R-terms at $\eta_*$ post-bounce (lane a) is correct but does not remove the interior pole of $F$.

**(iii) Quintin+2015 — NOT VERIFIED HERE (literature, unverified).** arXiv:1508.04141 evolves through
$H=\Upsilon(t-t_B)$ with finite $\Delta t_B$ and reports a finite bounce-phase $f_{\rm NL}$ contribution in terms of
$\zeta$ (lane (a) §5 cites their §5). This lane has no verified copy of the paper, so **no equation number and no
formula is asserted**; the audit item is: check whether their bounce-phase integrand uses the super-Hubble
$\dot\zeta\propto H^2$ form (then their finiteness is the $[C_1,C_2,C_2]$ sub-case plus a finite-$\Delta t_B$ window,
i.e. a $d_{\rm cut}$ in disguise) or the exact modes. Flagged for lane (c)/literature pass.

**(iv) Hard $d_{\rm cut}$ matched to S1 — REJECTED as a derivation.** It is a choice; §4 shows the divergence is a
dropped total derivative, so any finite number obtained by cutting the Maldacena form has no meaning independent of
the cut. It must not be quoted, even "matched".

## 6. VERDICT

**S2 REGULARISED-IN-FORM; VALUE UNRESOLVED.** The divergence is *not physical*: it is the pole of a total time
derivative generated by the Maldacena/Chen integration-by-parts steps, which use $1/H$ explicitly and are invalid
across $H=0$. In the raw ADM form the bounce-window in-in integrand is finite on-shell because the comoving-gauge
constraint solutions are regular at $H=0$ (§2, residue cancellation $\mp1/\Upsilon$). Therefore:
(a) the fluid picture need **not** be abandoned at the bounce on account of this divergence (the ghost $z^2<0$ of the
$P(X,\phi)$ NEC violation is a separate, model-level issue Quintin+2015 address with Galileon terms — *literature*);
(b) **no** cutoff/PV/matching prescription is legitimate, so lane (b)'s "report the scaling, never a number" stands;
(c) the finite S2 value is **not computed** and **not shown equal to** S1's $-\tfrac{5}{24}\rho_B$.
**Exact unresolved step:** the first-order in-in bounce-window integral of the raw ADM cubic Lagrangian
(Maldacena Eq. 2.9–2.11 expanded to cubic order in $\{\zeta,\dot\zeta,N_1,\psi\}$, constraints substituted, no
integration by parts) on the exact Frobenius/numerical S2 modes, on all three A2 backgrounds, with the
$\eta_*$-independence gate — a lane-(b)-class numerical job (~1 day CPU, $0). Until it runs, **S1 remains the only
scheme in which the lab has a number**, and it is an assumption-labelled anchor, not a prediction.

**Sentences the A3M paper should carry (replacing any "S2 diverges, a regulator is required" wording):**
> In the effective-fluid scheme the bounce-window cubic integrals written in the standard integrated-by-parts form
> [Maldacena 2003; Chen et al. 2007] are not absolutely convergent at $H=0$; we show this divergence is a total-derivative
> artefact: on the exact linear solution through the bounce the comoving-gauge lapse and shift perturbations,
> $N_1=\dot\zeta/H$ and $\psi=-\zeta/H+\chi$, are regular at $H=0$, so the cubic action in its raw ADM form is finite
> on-shell and no cutoff is required or permitted. The finite fluid-scheme value requires the raw-form in-in integral,
> which we have not evaluated; the number quoted in this paper, $\Delta f_{\rm NL}^{\rm bounce}=-\tfrac{5}{24}\rho_B$,
> is the geometric-scheme (S1) value and is labelled as such.

## 7. Assumptions and limits

(A1) Quintin-type background only (LQC dust shares the pole structure, lane (a) §2; not re-run here). (A2) $P(X,\phi)$
form of constraints (Chen convention $\partial^2\chi=a^2\epsilon\dot\zeta/c_s^2$); Horndeski/Galileon corrections to the
constraint solution are lane (c). (A3) Regularity of the raw form is argued from the polynomial structure of the ADM
Lagrangian plus computed regularity of its building blocks; the cubic expansion itself is not re-derived symbolically
here. (A4) The singular-$F$ mechanism is established structurally (§4) and by the pole bookkeeping (§3), not by an
explicit reconstruction of $F$; that reconstruction is part of the named next step. (A5) Nothing from Quintin+2015 is
asserted at equation level.
