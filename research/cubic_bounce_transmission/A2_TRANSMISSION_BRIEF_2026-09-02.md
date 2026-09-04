# Track A2 — transmission of the matter-contraction $f_{\rm NL}$ through an explicit nonsingular bounce

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` item #2 (March-2026 audit item #1).
**Date:** 2026-09-02 · **Venue:** local CPU · **Cost:** \$0 · **Wall clock:** 1.5 s (main) + 4 s (figure).
**Artifacts:** `a2_transmission_linear.py` → `a2_transmission_linear.{json,log}`;
`a2_transmission_figures.py` → `a2_transmission_summary.png`;
manifest `reproducibility/manifests/experiments/p2-a2-bounce-fnl-transmission.json`.
**Every number below is produced by the committed scripts.** Literature statements are cited
and are labelled as literature, not as our computation.

---

## 1. Question

P2 forecasts $f_{\rm NL}^{\rm loc} = -35/16$ from a matter-dominated contraction. Turning that
into an observable prediction requires the transmission coefficient

$$T_{f_{\rm NL}} \;\equiv\; \frac{f_{\rm NL}^{\rm after\ bounce}}{f_{\rm NL}^{\rm before\ bounce}},$$

which P2 carries as its assumption (d) ("faithful transmission", $T \simeq 1$). Every P2 reviewer has
asked for it. The ledger's success condition is *"a scheme-labeled transmission coefficient with
stated validity"*.

## 2. Prior results

### 2.1 In this repository

| phase | artifact | result |
|---|---|---|
| 1 | `g1_gradient_transmission_scheme.py` | effective-**fluid** MS variable $z^2=a^2(\rho+p)/(c_s^2H^2)$ has an $H=0$ pole; the gradient-transmission coefficient has **no scheme-independent limit** ($c\sim d_{\rm cut}^{-1}$) |
| 2 | `g1_dressedmetric_transmission.py` | bounded dressed geometric potential $a''/a = x^{1/3}(1/6+x/3)$ cures the regulator pathology; absolute coefficient still IC-epoch sensitive |
| 3 | `g1_dressedmetric_ic_close.py` | with adiabatic-vacuum ICs, the **constant (Weinberg) branch** transmits with $T_c(k)=1$; quoted as "$|\delta f_{\rm NL}|\le 6.8\times10^{-8}$" |
| — | `pathz2_calibrated_inin.py` | full in-in engine **failed its own Maldacena calibration gate**; amplitude not derivable at that fidelity. Honest negative; the *shape* (scale-independent transfer) result stands |

**The gap this brief closes.** Phase 3's $T_c=1$ is a statement about the constant branch **alone**.
Section 4.2 shows the physical adiabatic-vacuum mode in a matter contraction is *not* constant-branch
dominated — it is dominated by the branch that grows in contraction, by the factor
$|r| = 9A^2 I_\infty/k^3 \sim 10^5\text{--}10^8$ over the observable range — and it is that branch which
carries the contraction-phase $f_{\rm NL}$. The transmission of the physical perturbation is therefore
**not** unity, and the P2 wording built on phase 3 is an under-statement of the true transfer.

### 2.2 Literature

* **Quintin, Sherkatghanad, Cai & Brandenberger 2015** (arXiv:1508.04141). Nonsingular bounce from a
  generic single scalar field; bounce phase parametrised by $H(t)=\Upsilon(t-t_B)$,
  $a = a_B e^{\Upsilon (t-t_B)^2/2}$, duration $\Delta t_B$. Two findings we engage directly:
  (i) growth of $\zeta$ through the bounce "is very limited because of the conservation of curvature
  perturbations on super-Hubble scales"; (ii) $f_{\rm NL}$ "is enhanced during the bounce phase if the
  curvature fluctuations grow", giving their tension between small $r$ and acceptable $f_{\rm NL}$.
  **Their quoted pre-bounce value is $f_{\rm NL}^{\rm local}=-35/16$** — i.e. the same value P2 derives,
  not Cai et al. 2009's $-35/8$. *(Directly relevant to ledger item #1; flagged, not resolved here.)*
* **Agullo, Bolliet & Sreenath 2017** (arXiv:1712.08148), dressed-metric LQC to second order in
  perturbations: "the bounce in LQC produces an enhancement of non-Gaussianity of several orders of
  magnitude, on length scales that were larger than the curvature radius at the bounce", arising from
  gravitational self-interactions in the third-order Hamiltonian (present even for $V(\phi)=0$), and
  robust across their three operator-ordering choices.
* **Agullo, Ashtekar & Nelson** (arXiv:1211.1354, 1302.0254): the dressed-metric framework whose
  geometric potential this work uses; the quantum-corrected effective mass $U(\eta)$ is published for
  scalar-field matter, not for the quasi-dust fluid used here (see §6).
* **Cai, Easson & Brandenberger 2012** (arXiv:1206.2382): matter-bounce background conventions.

## 3. Method

Units $8\pi G=1$, $a_{\rm b}=1$, $c_s=1$. Mode equation $\mu'' + (k^2-W)\mu = 0$, $\zeta=\mu/z$.

**Schemes (the label on every number).**
*S1 — geometric / dressed-metric prescription:* $z=a$, $W=a''/a$ (the bounded potential verified in
phase 2). *S2 — effective fluid:* $z^2=a^2(\rho+p)/(c_s^2H^2)$.

**Backgrounds (three explicit nonsingular bounces).**
1. **LQC effective, quasi-dust:** $H^2=(\rho/3)(1-\rho/\rho_c)$, $w=0$. Traversed exactly via
   $s=\sqrt{1-x}$, $x\equiv\rho/\rho_c=a^{-3}$ — **no bounce regulator exists by construction**;
   matter tail resolved on a log-$x$ grid to $x_{\min}=10^{-12}$.
2. **Analytic non-LQC ("poly"):** $a(\eta)=a_{\rm b}(1+\eta^2/\eta_b^2)$, so
   $a''/a = 2/(\eta^2+\eta_b^2)$ — bounded, with *exact* matter asymptotics $a\propto\eta^2$; one
   explicit bounce-duration parameter $\eta_b$. Everything closed form.
3. **Quintin+2015-type:** their bounce-phase $H(t)=\Upsilon t$, $a=a_Be^{\Upsilon t^2/2}$ for
   $|t|\le\Delta t_B/2$, matched to matter contraction/expansion at the NEC boundary; matching $H$ fixes
   $\Upsilon = 8/(3\Delta t_B^2)$, giving a one-parameter family in $\Delta t_B$.

The **bounce duration** is defined physically and identically in all three as the NEC-violation window
$\dot H>0$, half-width $\eta_B$. (Our LQC $\eta_B = 1.06015$ agrees with the value committed in phase 2/3,
$1.05938$, to $7\times10^{-4}$.)

**Branch structure.** At $k=0$ the exact solution in *any* FRW is
$\zeta(\eta)=C_1 + C_2 J(\eta)$, $J(\eta)\equiv\int_0^\eta d\eta'/a'^2$, so the super-Hubble transfer
between any two epochs is the **$k$-independent** ratio $(C_1+C_2J_2)/(C_1+C_2J_1)$. In matter
asymptotics $a\to A\tau^2$ the exact finite-$k$ basis is the $\nu=3/2$ pair
$S(u)=\sin u/u-\cos u$ (constant branch) and $C(u)=\cos u/u + \sin u$ (growing branch), $u=k\tau$, and the
adiabatic/Bunch–Davies vacuum is the *exact* matter solution
$\mu_{\rm vac}=e^{-iu}(1-i/u)/\sqrt{2k} = (-S-iC)/\sqrt{2k}$ (sympy-verified identity).
Projecting gives, in closed form,
$$\alpha_-=-\frac{k^2}{3A\sqrt{2k}},\qquad \beta_-=\frac{3iA}{k\sqrt{2k}},\qquad
r\equiv\frac{\beta_-I_\infty}{\alpha_-}=-\,\frac{9iA^2I_\infty}{k^3},\qquad C_1=\alpha_-(1+r),\ C_2=\beta_-.$$

**Transmission of $f_{\rm NL}$.** Because $|r|\gg1$ the vacuum satisfies $C_1 \simeq I_\infty C_2$, so
$\zeta(\eta,\mathbf x) = C_2(\mathbf x)\,[\,I_\infty + J(\eta)\,]$: the spatial profile is fixed and only a
single $k$-independent amplitude evolves. A local $\zeta = \zeta_L + \tfrac35 f_{\rm NL}\zeta_L^2$ at a
handoff epoch $-\eta_h$, uniformly rescaled by
$\lambda(\eta_h)=\zeta(+\infty)/\zeta(-\eta_h)$, has $f_{\rm NL}\to f_{\rm NL}/\lambda$. Hence

$$\boxed{\;T_{f_{\rm NL}}(\eta_h,k)=\frac{1+r\,[1-\rho(\eta_h)]}{1+2r}\;\xrightarrow[\;|r|\gg1\;]{}\;
\frac{1-\rho(\eta_h)}{2},\qquad \rho(\eta_h)\equiv\frac{|J(-\eta_h)|}{I_\infty}\in(0,1]\;}$$

and therefore the **universal bound $0 < T_{f_{\rm NL}}\le 1/2$** for every bounce of this class:
the linear transfer can only *suppress* $f_{\rm NL}$, by at least a factor 2.
The natural handoff is the NEC boundary $\eta_h=\eta_B$ (end of the contracting phase, where the
matter-contraction in-in integral saturates); $\rho_B \equiv \rho(\eta_B)$ is the fraction of the
mode-mixing integral accumulated *before* the bounce phase.

## 4. Results

### 4.1 Transmission coefficients (headline)

Handoff at the NEC boundary; $f_{\rm NL}^{\rm before}=-35/16=-2.1875$.

| background | scheme | $\eta_B$ | $I_\infty$ | $\rho_B$ | $\lambda_\zeta$ | $T_{f_{\rm NL}}$ | $f_{\rm NL}^{\rm after}$ |
|---|---|---|---|---|---|---|---|
| LQC effective (dust) | S1 geometric / dressed-metric | 1.06015 | 1.813798 | **0.500000** | 4.0000 | **0.250000** | $-0.54687$ |
| analytic non-LQC (poly) | S1 geometric / dressed-metric | 0.57735 | 0.785398 | 0.608998 | 5.1151 | **0.195501** | $-0.42766$ |
| Quintin+2015-type | S1 geometric / dressed-metric | 0.44960 | 0.557352 | 0.669989 | 6.0604 | **0.165005** | $-0.36095$ |
| LQC effective (dust) | S2 effective fluid | 1.06015 | 0.302300 | 0.181690 | 2.4440 | **0.409155** | $-0.89502$ |

**Scheme/background spread: $T_{f_{\rm NL}} \in [0.165,\,0.409]$, i.e. $0.29 \pm 0.12$ (full range).**
On the *same* LQC background the two MS-variable schemes differ by a factor **1.64** (0.250 vs 0.409) —
this is the scheme dependence the ledger row asks to have stated, and it is irreducible without an
independent principle selecting the perturbation variable.

Two exact closed forms fall out and are confirmed numerically to $\le 7\times10^{-7}$:
* **LQC, geometric scheme:** $\rho_B = \tfrac12$ *exactly*
  ($J\propto 2\arcsin\sqrt x$, $\dot H = 0$ at $x=\tfrac12$), so
  $$T_{f_{\rm NL}}^{\rm LQC,\,S1} = \tfrac14 \quad\Longrightarrow\quad f_{\rm NL}^{\rm after} = -\tfrac{35}{64}.$$
  Also exact and reproduced: $I_\infty=\pi/\sqrt3$, $A=1/12$.
* **poly:** $\dot H=0$ at $u=1/\sqrt3$, $I_\infty=\pi\eta_b/4$, hence
  $\rho_B=\big[\pi/6+\sqrt3/4\big]/(\pi/2)=0.6089981$ (numerics agree to $1.1\times10^{-8}$).

### 4.2 Why this differs from phase 3's $T\simeq1$

The adiabatic vacuum is growing-branch dominated by $|r| = 9A^2I_\infty/k^3$: measured
$1.7\times10^{8}$ (poly), $1.7\times10^{7}$ (LQC), $8.3\times10^{7}$ (Quintin) at $k\eta_B=2\times10^{-3}$,
agreeing with the closed form to $\le1.1\times10^{-15}$. The constant branch carries a fraction
$\sim|r|^{-1}\lesssim10^{-5}$ of the physical mode. Phase 3's $T_c=1$ is correct **and irrelevant to the
observable**: it describes the sub-dominant component.

We reproduce $T_c\to1$ independently. Preparing the constant branch to $O(k^4)$ (i.e. including the
Weinberg correction $\zeta_C = 1+k^2f_1$, $f_1=-\int_0^\eta d\eta' a'^{-2}\int_0^{\eta'} a^2$) gives
$|T_c-1| = 1.6\times10^{-3},\,3.0\times10^{-3},\,1.2\times10^{-2},\,6.6\times10^{-2},\,0.81$ for
$k\eta_B=0.03\ldots0.002$ (LQC). The residual **grows** as $k$ falls because any state-preparation error
$\varepsilon$ is amplified by the bounce mixing $\propto k^{-3}$. That is itself a physical statement worth
recording: *the constant branch is not a preparable state through a matter contraction* — an
$O((k\eta)^2)$ error in preparing it dominates the transmitted amplitude. For a symmetric bounce
$T_c=1$ is anyway **exact by parity** ($W$ even $\Rightarrow$ the even solution is the constant branch,
$J$ odd), so no numerics are needed for that claim.

### 4.3 Verification and validity

* **Direct check.** $T_{f_{\rm NL}}$ obtained by integrating the full mode equation from the adiabatic
  vacuum and reading $\zeta$ at $-\eta_B$ against the projected post-bounce constant agrees with the
  super-Hubble formula to $1.0\times10^{-5}$ ($k\eta_B=0.002$) rising to $4.7\times10^{-3}$
  ($k\eta_B=0.03$), scaling as $(k\eta_B)^2$ — panel (c) of the figure. **Validity: $k\eta_B\ll1$**,
  with a quantified $\sim2.5\,(k\eta_B)^2$ fractional correction.
* **Matter-bounce benchmark recovered.** $\Delta^2 \propto k^3|\alpha_{\rm post}|^2$ is flat across the
  $k$ grid to 1.2–4.2 % — the post-bounce spectrum is scale invariant, as it must be. (The residual
  tilt is the finite-$k$ truncation, same $(k\eta_B)^2$ order.)
* **Bounce-duration independence.** Sweeping $\Delta t_B \in [0.25,4]$ (Quintin) and
  $\eta_b\in[0.25,4]$ (poly) leaves $T_{f_{\rm NL}}$ fixed to $1.5\times10^{-5}$ and $3.7\times10^{-12}$
  respectively. Both families are exactly self-similar in their duration parameter, so
  **$T_{f_{\rm NL}}$ depends on the bounce *shape*, not its duration** — a cleaner statement than the
  ledger asked for.
* **Handoff-epoch dependence** is explicit, monotone and bounded (figure panel b, table §4.1 of the
  JSON): $T_{f_{\rm NL}}(\eta_h) = [1-\rho(\eta_h)]/2$ falls from $\approx0.17$–$0.25$ at $\eta_h=\eta_B$
  to $\lesssim10^{-4}$ at $\eta_h=50\eta_B$. This replaces phase 2's *uncontrolled* IC-epoch sensitivity
  with a **controlled, physical, closed-form** dependence: it is the statement that
  $f_{\rm NL}$ is generated late in the contraction, and the handoff must be placed at the end of the
  contracting phase (where the in-in integral saturates), which is the NEC boundary.
* **Convergence.** $\eta_{\rm far}\times2$: $5.5\times10^{-22}$; rtol $10^{-11}\!\to\!10^{-9}$:
  $1.1\times10^{-23}$; grid halved: $3.3\times10^{-10}$ (LQC), $9.2\times10^{-7}$ (poly),
  $4.1\times10^{-5}$ (Quintin); LQC $x_{\min}\ 10^{-12}\!\to\!10^{-14}$: $5.7\times10^{-7}$.
* **Fluid-scheme pathology reproduced.** $K=\int z^2 d\eta \sim d_{\rm cut}^{-0.4998}$ (analytic $-1/2$),
  matching phase 3's $-0.49984$. The *mixing* integral $\int d\eta/z^2$ is nevertheless finite in that
  scheme, which is why S2 still has a transmission coefficient (row 4 of §4.1) — at leading gradient
  order only.

### 4.4 Assumptions

(A1) super-Hubble, $k\eta_B\ll1$; (A2) single-clock/adiabatic matter contraction, $a>0$ throughout,
bounded $a''/a$; (A3) the second-order (quadratic) piece of $\zeta$ is carried by the *same* branch
mixture as the linear one at the handoff epoch — true if the nonlinearity is local in the
separate-universe sense and generated under the same dynamics before handoff; (A4) **the bounce's own
cubic vertices are switched off** — see §5.

## 5. The term we did not compute, and the resulting honest verdict

The intrinsic bounce contribution $\Delta f_{\rm NL}^{\rm bounce}$ from the third-order action during NEC
violation is **not computed here** (the repo's own in-in engine failed its Maldacena calibration gate;
we did not resurrect it, and per `/never-fabricate-derivation` we do not estimate it from a formula we
cannot verify). The literature is unambiguous about its sign and about the fact that it is *not* bounded
by the linear term:

* Quintin+2015: $f_{\rm NL}$ is **enhanced** during the bounce phase whenever $\zeta$ grows — and $\zeta$
  does grow here, by $\lambda = 4.0$–$6.1$ (§4.1). Their no-go is built on exactly that enhancement.
* ABS 2017: the LQC bounce enhances non-Gaussianity by **several orders of magnitude** on scales larger
  than the curvature radius at the bounce — i.e. precisely our $k\eta_B\ll1$ regime.

**We do not contradict either paper.** Their enhancement and our suppression are *different terms of the
same decomposition*: they compute the intrinsic cubic term, we compute the linear rescaling. Our
$\lambda\in[4.0,6.1]$ is quantitatively consistent with Quintin's "growth is very limited by super-Hubble
conservation" (an $O(1)$–$O(10)$ factor, not an exponential). What the combination implies is the
verdict below.

> **Verdict.** P2's assumption (d) — faithful transmission, $T_{f_{\rm NL}}\simeq1$ — is **not supported by
> either term**. The linear transfer alone gives $T_{f_{\rm NL}} = 0.17$–$0.41$ (scheme dependent), a
> factor $2.4$–$6.1$ *suppression*, so $|f_{\rm NL}^{\rm after}| = 0.36$–$0.90$ rather than $2.19$. The
> intrinsic cubic term, per two independent published computations, acts in the opposite direction and
> can be orders of magnitude larger. The observable $f_{\rm NL}$ of this scenario is therefore **not
> currently predicted at better than order-of-magnitude**, and the honest P2 statement is that
> $-35/16$ is a *contraction-phase* coefficient, not a CMB/LSS prediction.

This also means the phase-3-derived P2 wording "$|\delta f_{\rm NL}| \le 6.8\times10^{-8}$" should be
**narrowed** to what it actually establishes (the constant branch), not carried as a statement about the
observable. That is a text change for the P2 owner, not made here.

## 6. What is genuinely open

1. **$\Delta f_{\rm NL}^{\rm bounce}$** — the intrinsic cubic term. This is now the *only* thing between
   here and a real prediction, and it is the item to fund next: either a calibrated in-in computation
   (the previous engine's failure mode is diagnosed in `pathz2_results.json`: a truncated single-vertex
   quadrature on exact-dS modes cannot reproduce the tilt-locked squeezed amplitude) or a second-order
   matching across the bounce à la ABS 2017.
2. **The AAN quantum-mass term $U(\eta)$** for a *quasi-dust* background. The published closed form is
   for scalar-field matter; no verifiable form exists for this fluid, so it is not guessed. Structural
   remark (unchanged from phase 3): any $U$ even about a symmetric bounce cannot alter the parity
   result, and since $U$ enters only through the mode equation it shifts $\rho_B$ but not the bound
   $T\le1/2$.
3. **Hybrid LQC.** Not implemented — its effective mass for quasi-dust is not available in a form we can
   verify. The two schemes implemented (dressed-metric-geometric, effective-fluid) already bracket a
   factor 1.64, which is the honest current scheme uncertainty.
4. **Asymmetric bounces.** Only mild asymmetry was probed (phase 3's $w_{\rm post}=0.05$ null). The
   formula $T=(1-\rho)/2$ assumes $J(+\infty)=I_\infty$ with the same $I_\infty$ on both sides; a strongly
   asymmetric completion changes $\rho$ and must be redone.
5. **Ledger item #1 cross-link.** Quintin+2015 independently quote $f_{\rm NL}^{\rm local}=-35/16$ for the
   matter contraction, i.e. an external corroboration of P2's value over Cai et al. 2009's $-35/8$. This
   is *evidence*, not the independent re-derivation item #1 requires, but it should be recorded there.

## 7. Assessment against the ledger row

| ledger field | status |
|---|---|
| *First cheap test:* extend `research/cubic_bounce_transmission/`; formalism-dependence check | **Done.** Three backgrounds (one LQC, two non-LQC incl. the Quintin+2015 family), two MS-variable schemes. |
| *Success:* "a scheme-labeled transmission coefficient with stated validity" | **MET, with a caveat.** $T_{f_{\rm NL}} = 0.250$ (LQC / dressed-metric-geometric, exact $1/4$), $0.196$ (analytic non-LQC), $0.165$ (Quintin-type), $0.409$ (LQC / effective-fluid); validity $k\eta_B\ll1$ with a quantified $(k\eta_B)^2$ correction; duration-independent; handoff dependence closed form. **Caveat:** this is the *linear-transfer* term; the intrinsic cubic term is open and can dominate. |
| *Kill condition* | Not triggered. The line is alive but the deliverable is narrower than "the observable $f_{\rm NL}$". |

**Recommended ledger update:** keep item #2 OPEN, re-scoped to its remaining half —
*"compute $\Delta f_{\rm NL}^{\rm bounce}$, the intrinsic cubic contribution of the bounce phase"* —
with the linear-transfer half recorded as closed and this brief as its artifact. Under directive R2 no
review round is owed on this; under R6 the P2 claim should be restated at its actual evidential
strength (§5).

---

# Second half: the bounce's own cubic term ($\Delta f_{\rm NL}^{\rm bounce}$)

**Added 2026-09-03.** §5 above recorded the intrinsic bounce contribution as *not computed*. It is now
computed. Three lanes, all committed:
`lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md` (+ `REGULARISATION_ASSUMPTION.md`) — the cubic-vertex
table, pole structure at $H\to0$, and the scheme/regulator statement;
`lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md` (+ `results.json`) — the numerical in-in evaluation;
`lane_c_comparison/LANE_C_COMPARISON_2026-09-03.md` — the literature comparison summarised in §8.4.
Venue local CPU, cost \$0. Every number below is emitted by the committed scripts;
$f_{\rm NL}^{\rm before}=-35/16$ remains an **input** (ledger #1), never recomputed.

## 8.1 Result

Scheme **S1** (geometric / dressed-metric prescription: $z=a$, $\epsilon_{\rm eff}=1/2$, $c_s=1$),
squeezed isoceles, bounce window $[-\eta_B,+\eta_B]$, $\eta_*$ post-bounce:

$$\Delta f_{\rm NL}^{\rm bounce}[\mathrm{S1}] = -\frac{5}{24}\,\rho_B \quad\text{(closed form, lane a)},$$

confirmed by the independent numerical evaluation of lane (b) — finite-$k$ evolved modes, exact
kernels, all six $S_3$ attachments, boundary terms R1–R4 — to $3\times10^{-5}$ (Quintin, poly) and
$3\times10^{-4}$ (LQC). The vertex $V2 = \zeta\dot\zeta^2$ carries **99.95–99.97 %**; $V4$ is negative
but $5\times10^{-4}$ of it; $V6+V7$ are positive but $1.1\times10^{-4}$ of it (lane (a)'s pure-time
$-7/8$ rewrite estimate is **not** confirmed — the squeezed angular average cancels it, and the
correct S1 total is $-(5/24)\rho_B$ to 0.2 %); $V1$ and $V5$ vanish identically in S1;
$V3$ is $(k\eta_B)^2$-suppressed.

## 8.2 Combined statement per background

$f_{\rm NL}^{\rm after} = T_{f_{\rm NL}}\cdot(-35/16) + \Delta f_{\rm NL}^{\rm bounce}$:

| background | $T_{f_{\rm NL}}$ | $T\cdot(-35/16)$ | $\Delta f_{\rm NL}^{\rm bounce}$ | **$f_{\rm NL}^{\rm after}$** |
|---|---|---|---|---|
| Quintin+2015-type | 0.165005 | $-0.360949$ | $-0.13982$ | **$-0.5008$** |
| LQC effective dust | 0.250000 | $-0.546875$ | $-0.10431$ | **$-0.6512$** |
| poly analytic non-LQC | 0.195501 | $-0.427659$ | $-0.12711$ | **$-0.5548$** |

The bounce's own term is **negative** — it *adds* to $|f_{\rm NL}|$, i.e. it acts in the direction the
literature calls enhancement — at **28–39 %** of the transmitted contraction term. It partially undoes
the linear suppression but does not reverse it: $|f_{\rm NL}^{\rm after}| = 0.50$–$0.65$ against
$|f_{\rm NL}^{\rm before}| = 2.19$.

## 8.3 Scheme label and validity (not optional)

* **Scheme S1**, whose cubic coefficients are the substitution $\epsilon\to1/2$, $c_s\to1$ into the
  classical comoving-gauge $P(X,\phi)$ cubic action (Chen+2007 Eq. 4.28; Maldacena 2003 Eq. 3.9) —
  an **assumption of the scheme**, not a derivation (lane (a) A3).
* **Validity $k\eta_B\lesssim10^{-2}$**, set by two competing requirements: $J(\eta_*)\to I_\infty$
  needs $\eta_*$ deep post-bounce, while the super-Hubble treatment of the boundary terms needs
  $k\eta_*\ll1$. Rows outside the band are flagged `valid: false` in `results.json`.
* **$\eta_*$-independence: partial pass.** The total is flat to 1.3–3.6 % for $\eta_*\ge10\eta_B$, and
  is *not* flat at $2\eta_B$–$5\eta_B$ — as the regularisation note predicts, since R2/R3/R4 are
  singular at $H=0$. Independent in its stated domain, not globally.
* **The bounce/expansion split is a definition, not a convergent isolation.** The integrand falls off
  as $1/a^2$ and does not vanish at the NEC boundary; widening the window $[-f,f]\eta_B$ from
  $f=0.8$ to 3 moves the bulk from $-0.108$ to $-0.196$ (poly). Stated, not hidden.
* **Scheme S2 (effective fluid) is reported as a divergence, not a number.** Excising
  $|\eta|<d_{\rm cut}\eta_B$ from the $V6+V7$ integrand gives fitted log–log slopes $-1.0050$
  (Quintin), $-1.0071$ (LQC), $-1.0072$ (poly): a clean $d_{\rm cut}^{-1}$ with **no
  $d_{\rm cut}\to0$ limit**, the cubic-order restatement of the linear-order $z^2$ pathology. No
  regulated S2 value is quoted anywhere.
* Gates passed: Wronskian $-0.50000000$ on every leg; local-redefinition normalisation
  $f_{\rm NL}=\tfrac53F$ to $<10^{-12}$; triangle closure $<10^{-12}$; step-size convergence
  $10^{-8}$–$10^{-13}$.

## 8.4 Literature comparison verdict

Full mapping in `lane_c_comparison/LANE_C_COMPARISON_2026-09-03.md`. Summary:

* **Quintin, Sherkatghanad, Cai & Brandenberger 2015 (arXiv:1508.04141) — no contradiction.** Their
  parametrisation is background 3 here ($H=\Upsilon(t-t_B)$, $a=a_Be^{\Upsilon(t-t_B)^2/2}$, their
  Eqs. 52–54; $\Upsilon=8/(3\Delta t_B^2)$). Their "$f_{\rm NL}$ is enhanced during the bounce phase if
  the curvature fluctuations grow" refers to the **additive** bounce-generated bispectrum, their
  Eq. (44) $f_{\rm NL}\sim(\Delta\zeta)^2/(\Delta t_B M_p^2)$ — whose counterpart here,
  $\Delta f_{\rm NL}^{\rm bounce}$, is **negative, i.e. enhances $|f_{\rm NL}|$: the same direction.**
  §4.1's suppression is the *multiplicative* transmission $T_{f_{\rm NL}}\le1/2$ of the inherited
  contraction coefficient, a term they do not compute at all — so the two results share no quantity of
  opposite sign. The magnitude gap is the amplification: theirs is driven by the scalar-field-velocity
  dip $[\dot\phi_B/\dot\phi(t_{\rm amp-})]^2$ (their Eq. 79) reaching $\Delta\zeta/\zeta\sim50$, while
  the three backgrounds here are purely geometric with $\lambda_\zeta=4.0$–$6.1$ — consistent with
  their own "growth is very limited by super-Hubble conservation". The lab therefore occupies the
  **un-amplified corner of their parameter space**, where their Conjecture 1 predicts a small
  $f_{\rm NL}$ (confirmed) **and**, unfavourably for this scenario, an unsuppressed $r$. Recorded as a
  cost, not a success. They also quote $f_{\rm NL}^{\rm local}=-35/16$ for the contraction (their
  Sec. III.3) — the corroboration already logged under ledger #1.
* **Agullo, Bolliet & Sreenath 2017 (arXiv:1712.08148) — not comparable as computed; this result is
  scheme-limited relative to their treatment, and does not refute it.** Their mechanism is the
  gravitational self-interaction in the third-order Hamiltonian, their Eq. (23) — verbatim, "Most
  terms in $\mathcal H^{(3)}$ are independent of $V(\phi)$, and therefore would be present even if
  $V(\phi)=0$" — evaluated on the **dressed metric** of their Eqs. (39)–(42) with symmetric operator
  ordering. Lane (a)'s S1 contains the *classical* counterpart of that operator (V2, the dominant
  vertex here, is exactly a gravity-mediated self-coupling surviving at $V=0$) but **not** the
  quantum-geometric dressing of the coefficients — assumption A3, written before the comparison. Their
  background is a kinetic-dominated Planck-scale scalar bounce plus inflation, not a quasi-dust matter
  bounce; their quoted $\mathfrak f_{\rm NL}\sim10^3$ (companion review arXiv:2006.09605 Eq. 24) is an
  amplitude in an unmatched sign convention, so **signs are not compared**. A further plausible
  reconciliation — that their enhancement peaks in $k_I<k<k_B$ and is blue-tilted $\propto k^2$ below
  $k_I$, while the band here, $k\eta_B\le10^{-2}$, lies at or below $k_I$ — is recorded as
  literature-derived (same review) and **not relied upon**.
* **Li, Quintin, Wang & Cai 2016 (arXiv:1612.02036)** treats the contraction stage only; it
  corroborates the **input** $-35/16$ and its $c_s$-dependence, and supplies no bounce-phase object to
  compare against. **Cai, Easson & Brandenberger 2012 (arXiv:1206.2382)** computes no $f_{\rm NL}$;
  its ghost-condensate "controlled exponential growth" is the amplification mechanism Quintin+2015
  later parametrise, and marks an **uncovered background class** here.

**Net.** §5's verdict — "not currently predicted at better than order-of-magnitude" — is **narrowed,
not overturned**: *within scheme S1*, on these three backgrounds, at $k\eta_B\lesssim10^{-2}$, for the
classical $P(X,\phi)$ cubic action, $f_{\rm NL}^{\rm after} \in [-0.65,\,-0.50]$. The residual
uncertainty is now the **scheme**, not the integral. P2's assumption (d) ($T\simeq1$,
$f_{\rm NL}^{\rm after}\simeq-2.19$) remains **unsupported** by either term. The qualifier "in scheme
S1" is mandatory on every use of the $[-0.65,-0.50]$ range; the unqualified claim "the bounce produces
no orders-of-magnitude enhancement" is **not** established and must not be made.
