# Lane (c) — literature comparison for the bounce's own cubic contribution to $f_{\rm NL}$

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` item #2, second half.
**Lanes:** (a) `../lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md` — cubic-vertex table + regularisation;
(b) `../lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md` — numerical in-in over the bounce window;
(c) **this file** — mapping the lab result onto the published bounce-$f_{\rm NL}$ literature.
**Date:** 2026-09-03 · **Venue:** local CPU + literature fetch · **Cost:** \$0.

**Provenance rule (hard).** Every statement attributed to a paper is *literature*, fetched from that
paper's text and cited by section/equation where the fetch returned one. Every lab number is quoted
**unchanged** from lanes (a)/(b) and the A2 brief. **No lab number is reinterpreted, rescaled, or
re-signed to agree with a published claim.** Where the lab and a paper disagree, the disagreement is
stated together with its identified cause; where a comparison could not be made because the source
text was not recoverable, that is said instead of guessed.

**Fetch limitation, stated up front.** Section IV of Agullo, Bolliet & Sreenath 2017
(arXiv:1712.08148) — the section carrying their numerical bispectrum — was **not** recoverable from
the HTML rendering. Their mechanism, third-order Hamiltonian (their Eq. 23) and dressed-metric
construction (their Eqs. 39–42) were recovered; the absolute $f_{\rm NL}$ numbers quoted in §3 below
come from the companion review arXiv:2006.09605 and are labelled as such.

---

## 1. The lab result being compared

From lanes (a)+(b), scheme **S1** (geometric, $z=a$, $\epsilon_{\rm eff}=1/2$, $c_s=1$),
validity $k\eta_B \lesssim 10^{-2}$:

| background | $T_{f_{\rm NL}}=(1-\rho_B)/2$ | $T\cdot(-35/16)$ | $\Delta f_{\rm NL}^{\rm bounce}$ | $f_{\rm NL}^{\rm after}$ |
|---|---|---|---|---|
| Quintin+2015-type | 0.165005 | $-0.360949$ | $-0.13982$ | **$-0.5008$** |
| LQC effective dust | 0.250000 | $-0.546875$ | $-0.10431$ | **$-0.6512$** |
| poly analytic non-LQC | 0.195501 | $-0.427659$ | $-0.12711$ | **$-0.5548$** |

Structure of the lab statement, which is what the comparison must respect:

* **A multiplicative term.** Uniform super-Hubble rescaling $\lambda_\zeta = 4.0$–$6.1$ of $\zeta$
  across the bounce sends a *pre-existing* local $f_{\rm NL}$ to $f_{\rm NL}/\lambda_\zeta$, i.e.
  $T_{f_{\rm NL}}=(1-\rho_B)/2 \le 1/2$: the transmission of the **contraction-phase** coefficient is a
  **suppression**, by at least a factor 2, for every bounce of this class.
* **An additive term.** $\Delta f_{\rm NL}^{\rm bounce}$, the bounce window's own third-order in-in
  integral, $=-(5/24)\rho_B$ in S1 (V2 $\zeta\dot\zeta^2$ carries 99.95 %), **negative**, i.e. it
  *increases* $|f_{\rm NL}|$ — an **enhancement in magnitude** at the 28–39 % level of the transmitted
  term, not orders of magnitude.
* **A divergence, not a number, in S2.** The effective-fluid scheme's $\epsilon^3$ constraint vertices
  (V6, V7) give a clean $d_{\rm cut}^{-1}$ with no limit (measured slopes $-1.005$, $-1.007$, $-1.007$).

So the lab does **not** claim "the bounce suppresses $f_{\rm NL}$". It claims: the *transmitted*
contraction coefficient is suppressed, the bounce's *own* term enhances $|f_{\rm NL}|$, and in S1 the
two together give $|f_{\rm NL}^{\rm after}| = 0.50$–$0.65$. Any comparison that reads the lab as
"suppression" and the literature as "enhancement" is comparing different terms.

---

## 2. Quintin, Sherkatghanad, Cai & Brandenberger 2015 (arXiv:1508.04141)

### 2.1 Parametrisation map

*Literature.* Their bounce phase (their Eqs. 52–54):
$H(t)=\Upsilon\,(t-t_B)$, $a(t)=a_Be^{\Upsilon(t-t_B)^2/2}$, and
$\dot\phi(t)=\dot\phi_Be^{-(t-t_B)^2/T^2}$; "the parameters which describe the bounce phase are
$\Upsilon$, $\dot\phi_B$, $t_B^\pm$ (or assuming symmetric bounce), and $T$" (their Sec. IV).
Perturbations are treated on super-Hubble scales, $k\ll\mathcal H$ (their Sec. V), and they note that
"modes of cosmological interest today were on super-Hubble scales during the bounce phase".

*Lab.* Background 3 of the A2 brief is exactly their first two equations, with the bounce duration
$\Delta t_B$ fixed by matching $H$ at the NEC boundary, $\Upsilon = 8/(3\Delta t_B^2)$; lane (a)
computes $\epsilon = -1/(\Upsilon t^2)$ and $\eta_{\rm sr}=2\epsilon$ exactly in that phase, and shows
the LQC dust bounce is *locally* the same bounce with $\Upsilon_{\rm eff}=\rho_c/2$.

| their symbol | lab symbol | relation |
|---|---|---|
| $\Upsilon$ | $\eta_B$, $\Delta t_B$ | $\Upsilon=8/(3\Delta t_B^2)$; Quintin grid $\Delta t_B=1\Rightarrow\Upsilon=2.667$, $\eta_B=0.44960$ |
| $\Delta t_B$ (duration) | $\eta_B$ (NEC half-width, conformal) | same physical window ($\dot H>0$) |
| $\Delta\zeta/\zeta$ (amplification) | $\lambda_\zeta = \zeta(+\infty)/\zeta(-\eta_B)$ | **not the same object** — see §2.3 |
| $\dot\phi_B/\dot\phi(t_{\rm amp-})$ | *absent* | the lab's backgrounds carry no scalar-velocity dip |

**Duration.** Lane (a)/(b) find $\Delta f_{\rm NL}^{\rm bounce}$ is $\Upsilon$-**independent** in S1
(self-similar; brief §4.3 finds the same for $T_{f_{\rm NL}}$, fixed to $1.5\times10^{-5}$ over
$\Delta t_B\in[0.25,4]$). Quintin's $f_{\rm NL}$ *is* $\Delta t_B$-dependent — their Eq. (44),
$f_{\rm NL}\sim(\Delta\zeta)^2/(\Delta t_B M_p^2)$. This is not a disagreement about the same
quantity: their $\Delta t_B$ enters through $\Delta\zeta$, which is set by the field-velocity profile
$T$, not by the geometry (§2.3).

### 2.2 What they actually claim

*Literature, their Sec. III.3 / Conjecture 1 (Sec. III.4):* "if curvature perturbations were to
experience a nontrivial growth through the bounce, one should expect additional nonzero contributions
to the bispectrum coming from the bounce phase, and there would then be the danger that the final
amplitude of the bispectrum exceeds the observational upper bounds"; and "an upper bound on the
tensor-to-scalar ratio ($r$) is equivalent to a lower bound on the amplification of curvature
perturbations ($\Delta\zeta/\zeta$) which in turn is equivalent to a lower bound on the amount of
primordial non-Gaussianities ($f_{\rm NL}$)." Their scaling is their **Eq. (44)**,
$f_{\rm NL}\sim(\Delta\zeta)^2/(\Delta t_B M_p^2)$; the bispectrum is built by an in-in integral over
the amplification interval $[\eta_{\rm amp-},\eta_{\rm amp+}]$ (their Sec. VI, Eq. 88). The growth
itself is bounded by their Eqs. (79)–(80), with amplification factor
$\dot\zeta_{\max}\simeq\dot\zeta(t_B^-)[\dot\phi_B/\dot\phi(t_{\rm amp-})]^2$. They quote the
matter-contraction value as $f_{\rm NL}^{\rm local}=-35/16$ (their Sec. III.3, citing Cai et al. 2009)
— the same value the lab uses as input, and the corroboration already recorded in ledger #1.

### 2.3 Verdict: **not a contradiction — a different corner of their own parameter space**

Three separate reasons, in order of weight:

1. **Different terms of the same decomposition.** Their Eq. (44) is an estimate of the *additive*
   bounce-generated bispectrum. Its lab counterpart is $\Delta f_{\rm NL}^{\rm bounce}$, which is
   **negative, i.e. an enhancement of $|f_{\rm NL}|$ — the same direction they describe.** The lab's
   *suppression* statement is about the multiplicative transmission $T_{f_{\rm NL}}\le1/2$ of the
   pre-existing contraction coefficient, a term Quintin+2015 do not compute at all. There is no
   quantity on which the two results have opposite signs.
2. **Different amplification, hence different magnitude.** Their large $f_{\rm NL}$ requires large
   $\Delta\zeta$, and their $\Delta\zeta$ is driven by the **scalar-field-velocity dip**
   $[\dot\phi_B/\dot\phi(t_{\rm amp-})]^2$ (their Eq. 79) — a matter-sector feature. The lab's three
   backgrounds are specified geometrically (LQC effective dust, $a=a_b(1+\eta^2/\eta_b^2)$, and their
   own $a_Be^{\Upsilon t^2/2}$) with no such dip, and the lab's growth $\lambda_\zeta=4.0$–$6.1$ is the
   ordinary super-Hubble branch mixing $\zeta = C_1+C_2J$, **not** their amplification mechanism.
   Feeding $\lambda_\zeta\sim5$ rather than $\sim50$ into their own scaling gives an $O(0.1)$ effect,
   which is what lane (b) measures. **The lab sits in the un-amplified corner of their parameter
   space, and their Conjecture 1 then predicts a small $f_{\rm NL}$ there — which the lab confirms.**
   Their conjecture's other leg applies with equal force: in that corner $r$ is *not* suppressed, so
   the lab's backgrounds do not evade their no-go; they sit on its unfavourable side. This is recorded
   as a cost of the lab's scenario, not a success.
3. **A definitional gap, in the lab's favour and stated as such.** Quintin's treatment has no
   multiplicative $1/\lambda_\zeta$ dilution of the inherited contraction $f_{\rm NL}$. The lab's
   $T_{f_{\rm NL}}=(1-\rho_B)/2$ is an addition to their picture, not a correction of it; it has not
   been checked against any published calculation, because none was found that computes it.

**Regime agreement:** both are super-Hubble; the lab's stated band $k\eta_B\lesssim10^{-2}$ is inside
their $k\ll\mathcal H$. **No regime excuse is needed for this comparison, and none is claimed.**

**One honest residual disagreement.** Their Eq. (44) is a parametric *estimate*; lane (b) is an
explicit vertex-by-vertex in-in evaluation on their own background with the boundary terms and an
$\eta_*$-independence test. Where the two would be compared at fixed $\Delta\zeta$ the lab has no way
to check the coefficient of their estimate, because their Eq. (44) carries no fixed prefactor. The
comparison is therefore at the level of **sign and mechanism (agree)**, not of amplitude.

---

## 3. Agullo, Bolliet & Sreenath 2017 (arXiv:1712.08148)

### 3.1 Their mechanism, as recovered

*Literature.* Their cubic interaction Hamiltonian is their **Eq. (23)**, with operators
$\delta\phi^3$, $\delta p_\phi^2\,\delta\phi$, $\delta p_\phi(\partial\delta\phi)^2$ and terms
involving the shift $\chi$. Crucially, verbatim: **"Most terms in $\mathcal H^{(3)}$ are independent
of $V(\phi)$, and therefore would be present even if $V(\phi)=0$. These are self-interaction mediated
by gravity."** The background is the **dressed metric** of their Eqs. (39)–(42), built from
expectation values $\langle\hat H_0^{-1/2}\hat a^4\hat H_0^{-1/2}\rangle$ etc.; on ordering, verbatim:
"we are not free of factor ordering ambiguities, and we choose a symmetric ordering". Their bounce is
a **kinetic-dominated Planck-scale scalar bounce** followed by inflation. Abstract, verbatim: "the
bounce in LQC produces an enhancement of non-Gaussianity of several orders of magnitude, on length
scales that were larger than the curvature radius at the bounce."

*Literature, companion review arXiv:2006.09605* (used because Sec. IV of 1712.08148 was not
recoverable): the amplitude is of order $\mathfrak f_{\rm NL}\sim10^3$ (their Eq. 24), and the
$k$-dependence has **three regimes** about the bounce scale $k_B=a_B\sqrt{R_B/6}$: $k>k_B$
unaffected (Bunch–Davies); $k_I<k<k_B$ enhanced with a red tilt; and $k<k_I$ **blue-tilted,
$\propto k^2$**.

### 3.2 Does the lab's S1 contain that operator? — **No, and this is the lane's main limitation**

Lane (a) §1 builds the cubic action from the **classical comoving-gauge $P(X,\phi)$** form (Chen,
Huang, Kachru & Shiu 2007 Eq. 4.28; Maldacena 2003 Eq. 3.9), and lane (a) assumption **(A3)** states
the S1 coefficients are the *substitution* $\epsilon\to1/2$, $c_s\to1$ — with the explicit caveat,
already written before this lane: "the dressed-metric third-order Hamiltonian of Agullo–Bolliet–
Sreenath 2017 has explicit quantum-geometric couplings that this substitution does not produce."

Operator-class correspondence (structural, gauge-map level — **not** a coefficient match):

| ABS 2017 Eq. (23) operator | lab lane-(a) vertex | present in S1? | coefficient equal? |
|---|---|---|---|
| $\delta\phi^3$ | V2 $\zeta\dot\zeta^2$, V5 $\zeta^2\dot\zeta$ (after gauge map) | V2 yes; **V5 $\equiv0$ in S1** ($\dot\eta_{\rm sr}=0$) | **no** |
| $\delta p_\phi(\partial\delta\phi)^2$ | V3 $\zeta(\partial\zeta)^2/a^2$ | yes | **no** |
| $\delta p_\phi^2\delta\phi$ | V1 $\dot\zeta^3$ | **V1 $\equiv0$ in S1** ($c_s=1$, $\lambda=0$) | **no** |
| shift-$\chi$ terms | V4, V6, V7 (constraint sector, $\tilde\chi=\partial^{-2}\dot\zeta$) | yes | **no** |
| quantum-geometry dressing of every coefficient | — | **absent** | — |

So: the lab's S1 contains the *classical* gravitational self-interaction — V2, the vertex that carries
99.95 % of $\Delta f_{\rm NL}^{\rm bounce}$, is exactly a gravity-mediated self-coupling surviving at
$V=0$ — but it does **not** contain the dressed-metric quantum-geometric dressing that makes ABS's
coefficients Planckian at the bounce. **The lab's number is scheme-limited relative to their full
quantum treatment, and the lab does not and cannot refute their result.** Two of the three lab
backgrounds are not even LQC; the third is LQC-*effective* with quasi-dust matter, whose AAN quantum
mass $U(\eta)$ has no published closed form (A2 brief §6.2) and was therefore not used.

### 3.3 Is there also a regime difference? — Probably yes, and it is stated as literature-derived

The abstract's "larger than the curvature radius at the bounce" is $k<k_B$, which naively contains the
lab band. But the companion review's three-regime structure says the enhancement peaks in
$k_I<k<k_B$ and **turns off $\propto k^2$ for $k<k_I$**. The lab's validity band is
$k\eta_B\lesssim10^{-2}$ — deep infrared relative to the bounce curvature scale, i.e. at or below
$k_I$, where by that reading the LQC enhancement is itself suppressed. **This is offered as the
likely reconciliation, not as an established one:** it rests on a companion review rather than on
Sec. IV of ABS 2017 itself, and it does not remove the operator-content limitation of §3.2, which
stands on its own.

Two further mismatches that make a direct numerical comparison inadmissible in either direction:
the **backgrounds differ** (their kinetic-dominated Planck-scale scalar bounce plus inflation vs the
lab's quasi-dust matter bounce with no inflation), and the **quantities differ** — their
$\mathfrak f_{\rm NL}\sim10^3$ is the amplitude of their Eq. (24), reported positive, not a
squeezed-limit local $f_{\rm NL}$ in the lab's convention
$\zeta=\zeta_L+\tfrac35 f_{\rm NL}\zeta_L^2$. **The signs are therefore not compared**; doing so
without their convention fixed would be a fabricated agreement or a fabricated conflict.

### 3.4 Verdict: **not a contradiction; the lab result is scheme-limited and says so**

The lab's honest position: *within* a classical $P(X,\phi)$ comoving-gauge cubic action, on the three
stated bounce backgrounds, in the bounded S1 scheme, at $k\eta_B\lesssim10^{-2}$, the bounce's own
term is $O(0.1)$ and negative. That statement is compatible with ABS 2017 because the lab's action is
not theirs. The lab must **not** claim that "there is no orders-of-magnitude enhancement" as a
general result; lane (b) §6's sentence "In scheme S1 there is no 'orders of magnitude' enhancement in
the super-Hubble band" is correct **only with its scheme qualifier**, and is carried forward with it.

---

## 4. Li, Quintin, Wang & Cai 2016 (arXiv:1612.02036) and Cai, Easson & Brandenberger 2012 (arXiv:1206.2382)

* **Li+2016** (*literature*, abstract) computes "the primordial three-point correlation function
  generated during the matter-dominated contraction stage", finding it "only depends on the sound
  speed parameter", "mainly dominated by a local form, though for some specific sound speed values a
  new shape emerges", and extends the no-go: "it does not seem possible to suppress the tensor-to-scalar
  ratio without amplifying the production of non-Gaussianities beyond current observational
  constraints." **It does not treat transmission through the bounce or the bounce-phase
  contribution.** It is therefore *not* a comparison object for lane (b); it is a corroboration of the
  lab's **input** $f_{\rm NL}^{\rm before}$ and of its $c_s$-dependence (already used in ledger #1,
  where Li+2016 Eq. 4.19 supplied the $\mu$-dependence). Ledger #1 also records that Li+2016 reuses
  Cai 2009's rows and is not an independent derivation — that assessment is unchanged here.
* **Cai, Easson & Brandenberger 2012** (*literature*, abstract): a nonsingular bounce from "single
  scalar field matter with non-trivial potential and non-standard kinetic term" via a **ghost
  condensate** phase, with "a controlled period of exponential growth of the fluctuation amplitude for
  the perturbations" around the bounce. **No $f_{\rm NL}$ or bispectrum computation.** Its role is the
  one the A2 brief already assigned: background conventions. Its "controlled exponential growth" is
  the amplification that Quintin+2015 later parametrise, and — like Quintin's — it is a matter-sector
  effect absent from the lab's geometric backgrounds. This is a **known gap in the lab's background
  coverage**, not a resolved point: a ghost-condensate/Horndeski bounce with genuine amplification has
  not been run, and lane (a) assumption (A2) excludes the Horndeski/Galileon vertices such a model
  would add.

---

## 5. Comparison table

$k\eta_B$ column: the mode regime in which each result is stated, in the lab's variable
($\eta_B$ = NEC-window conformal half-width; $k_B$ = LQC bounce curvature scale, $k_B\eta_B\sim1$).

| paper | regime ($k\eta_B$) | quantity | sign | magnitude | lab equivalent | agreement |
|---|---|---|---|---|---|---|
| Quintin+2015 (Eq. 44, Sec. III.3–III.4, VI) | super-Hubble, $k\ll\mathcal H$; contains the lab band | additive bounce-phase bispectrum, $f_{\rm NL}\sim(\Delta\zeta)^2/(\Delta t_B M_p^2)$ | *enhances* $\|f_{\rm NL}\|$ | grows with amplification; large ($\gtrsim$ obs. bounds) when $\Delta\zeta/\zeta\sim50$ | $\Delta f_{\rm NL}^{\rm bounce}=-(5/24)\rho_B$ = $-0.104$…$-0.140$ | **AGREE in sign + mechanism.** Magnitude differs because the lab's $\lambda_\zeta=4$–$6$ (geometric branch mixing) $\ne$ their $\Delta\zeta/\zeta\sim50$ (scalar-velocity dip, their Eq. 79) — different corner of *their* parameter space, not a conflict |
| Quintin+2015 (Sec. V, Eqs. 79–80) | super-Hubble | growth of $\zeta$ through the bounce; "very limited by super-Hubble conservation" absent a dip | growth ($\lambda>1$) | $O(1)$–$O(10)$ without a dip | $\lambda_\zeta=4.00$ (LQC), 5.12 (poly), 6.06 (Quintin-type) | **AGREE quantitatively** (both $O(1)$–$O(10)$) |
| Quintin+2015 Conjecture 1 | super-Hubble | small $r$ ⟺ large $\Delta\zeta$ ⟺ large $f_{\rm NL}$ | — | no-go | lab has small $\Delta\zeta$ ⇒ small $f_{\rm NL}$ **and** unsuppressed $r$ | **AGREE, unfavourably for the lab** — the backgrounds sit on the no-go's bad side; recorded, not spun |
| Quintin+2015 (any section) | — | multiplicative transmission of the inherited contraction $f_{\rm NL}$ | — | — | $T_{f_{\rm NL}}=(1-\rho_B)/2\le1/2$ | **NO COMPARISON EXISTS** — they do not compute it; the lab's suppression is unchecked against literature |
| Agullo, Bolliet & Sreenath 2017 (Eq. 23; Eqs. 39–42) | $k<k_B$ per abstract; peak at $k_I<k<k_B$ per 2006.09605 — lab band is $k\eta_B\le10^{-2}$, i.e. $\lesssim k_I$ | dressed-metric quantum $\mathcal H^{(3)}$; gravitational self-interaction at $V=0$ | reported positive for their $\mathfrak f_{\rm NL}$; **convention not fixed ⇒ not compared** | "several orders of magnitude"; $\mathfrak f_{\rm NL}\sim10^3$ (2006.09605 Eq. 24) | S1 contains the *classical* analogue (V2 dominant) but **not** the quantum-geometric coefficients | **NOT COMPARABLE AS COMPUTED — lab is scheme-limited.** Different action, different background, different $k$-window, unmatched convention. Lab does **not** refute them |
| Li, Quintin, Wang & Cai 2016 | contraction only | contraction-phase bispectrum, $c_s$-dependence, local shape | $f_{\rm NL}<0$ | $-35/16$ at $c_s=1$ | lab **input** $f_{\rm NL}^{\rm before}=-35/16$ | **AGREE (input corroboration)**; no bounce-phase object to compare |
| Cai, Easson & Brandenberger 2012 | — | ghost-condensate nonsingular bounce; "controlled exponential growth" of the amplitude | — | no $f_{\rm NL}$ computed | background conventions only | **NO $f_{\rm NL}$ COMPARISON.** Flags an uncovered background class (amplifying / Horndeski) |

---

## 6. Verdict

1. **Quintin+2015 — no contradiction.** The lab's bounce term is negative and therefore *enhances*
   $|f_{\rm NL}|$, the same direction as their claim; the lab's "suppression" is a different
   (multiplicative, transmission) term they never compute. The magnitude gap is fully accounted for by
   the amplification: theirs is a scalar-velocity-dip effect ($\Delta\zeta/\zeta\sim50$), the lab's
   backgrounds are geometric with $\lambda_\zeta=4$–$6$, and in that corner their own conjecture
   predicts small $f_{\rm NL}$ — with the unfavourable corollary that $r$ is not suppressed there.
2. **Agullo+2017 — not comparable as computed; the lab is honestly scheme-limited.** Their operator
   is the quantum-geometry-dressed third-order Hamiltonian (their Eq. 23 on the dressed metric of
   Eqs. 39–42). Lane (a)'s S1 contains only the classical $P(X,\phi)$ counterpart (assumption A3,
   written before this comparison), so the lab's $O(0.1)$ result carries no evidential weight against
   their several-orders-of-magnitude enhancement. A plausible additional reconciliation — the lab's
   band lying below their enhancement window $k_I<k<k_B$ — is recorded as literature-derived and
   **not** relied upon.
3. **Scope of the lab claim, restated.** "No orders-of-magnitude enhancement" is true **only in
   scheme S1, on these three backgrounds, at $k\eta_B\lesssim10^{-2}$, for the classical
   $P(X,\phi)$ cubic action." That qualifier is not optional and is carried into the A2 brief.
4. **What the literature comparison newly exposes as open:** (i) no published calculation of the
   multiplicative $T_{f_{\rm NL}}$ exists to check the lab against; (ii) no lab background carries the
   Quintin/CEB amplification mechanism, so the amplifying corner of matter-bounce parameter space is
   untested here; (iii) the dressed-metric $\mathcal H^{(3)}$ remains the one route that could move
   $f_{\rm NL}^{\rm after}$ outside $[-0.65,-0.50]$, and it is not implemented.
