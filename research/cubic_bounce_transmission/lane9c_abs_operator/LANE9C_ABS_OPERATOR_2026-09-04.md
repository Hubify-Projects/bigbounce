# Ledger row 9 (A3-1e), lane (c) — is the Agullo–Bolliet–Sreenath LQC non-Gaussianity enhancement an operator the lab's bounce carries?

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` row 9 — bounce-scale enhancement at
$k\eta_B\sim1$ (A3-1e), the remaining non-null route for Track A.
**Date:** 2026-09-04 · **Venue:** local CPU + arXiv literature fetch · **Cost:** \$0.
**Prior lanes:** (a) `../lane_a_vertex_table/VERTEX_TABLE_2026-09-03.md` (classical scheme-S1 cubic
vertex table V1–V7 + R1–R4); (b) `../lane_b_numerical/`; (c) `../lane_c_comparison/LANE_C_COMPARISON_2026-09-03.md`
(literature comparison, which recorded that the lab could neither reproduce nor refute the LQC
enhancement because the lab's table holds only the *classical* $P(X,\phi)$ counterpart).

**Plan (this file).**
1. Recover Agullo, Bolliet & Sreenath 2017 (arXiv:1712.08148) $H^{(3)}$ (their Eqs. ~23, 39–42) and the
   Agullo–Ashtekar–Nelson dressed-metric framework (1211.1354, 1302.0254) incl. the effective
   potential $\mathfrak U(\eta)$; quote, never paraphrase-as-equation.
2. Operator-by-operator mapping table: which $H^{(3)}$ terms are lane (a)'s V1–V7 in disguise, and
   which are genuinely quantum-corrected ($\rho/\rho_c$-dependent, or $\mathfrak U$-dependent).
3. Scale window: their $k_{\rm LQC}$ expressed in the lab's $k\eta_B$; compare against the S1 validity
   band ($k\eta_B\lesssim10^{-2}$) and the row-9 regime ($k\eta_B\sim1$).
4. Magnitude: their $f_{\rm NL}(k)$ just above the enhancement scale → $\Delta f_{\rm NL}^{\rm bounce}$
   in the lab's normalisation, **and** the decisive matter-sector question: their matter is a
   kinetic-dominated scalar field ($V\simeq0$ at the bounce); the lab's LQC background is **dust**.
   Does $H^{(3)}$ exist at all on a dust background?
5. Observability: their enhanced $k$ today under the A3 paper §V $T_B\gtrsim10^{8}$–$10^{10}$ GeV
   condition; PTA ($k\sim6.5\times10^{6}\,{\rm Mpc}^{-1}$ per nHz) and PBH ($10^{5}$–$10^{15}\,{\rm Mpc}^{-1}$) overlap.
6. VERDICT (one of): OPERATOR ABSENT ON THE LAB'S DUST BACKGROUND / OPERATOR PRESENT AND
   REPRESENTABLE / NOT DETERMINABLE WITHOUT A COMPUTATION (named exactly). Plus the paper sentence.

**Provenance rule (hard, inherited from lane (c)).** Every equation attributed to a paper is fetched
from that paper's text and cited by equation number. Nothing is invented. Where a fetch fails, that is
said, and the conclusion is stated at the evidential strength the recovered text supports.

*Sections 1–6 follow below as they are completed.*

---

## 0. Source and numbering

The arXiv source package of **Agullo, Bolliet & Sreenath 2017, "Non-Gaussianity in loop quantum
cosmology", arXiv:1712.08148** (`NGLQC.tex`, v2, 26 Feb 2018) was fetched from
`https://arxiv.org/e-print/1712.08148` and read directly, so every equation below is transcribed from
the authors' own LaTeX rather than reconstructed. **Equation numbers were recovered by counting
numbered environments in that source**; the count is anchored on two independent checkpoints that
reproduce the numbers recorded in lane (c) of 2026-09-03 from the HTML rendering — the third-order
Hamiltonian at **Eq. (23)** (`\label{eq:H3}`) and the dressed-metric construction at **Eqs. (39)–(42)**
(`\label{dres}`, `\label{ta}`, `\label{teta}`, `\label{qpot}`). LaTeX labels are quoted alongside every
number so a reader can verify against the source independently of the numbering.

## 1. ABS 2017's $\mathcal H^{(3)}$, and its map onto lane (a)'s vertex table

### 1.1 The operator, as printed (their Eq. 23, `eq:H3`)

Spatially-flat gauge, variables $(\dph,\delta p_\phi)$, lapse/shift potential $\chi$; the authors'
notation $\pp\equiv p_\phi$, $\pi_a$, $\kappa=8\pi G$:

$$\mathcal{H}^{(3)}=\int \d^3x\left(\delta N\,\mathbb S^{(2)}+\delta N^i\,\mathbb V^{(2)}_i+N\,\mathbb S^{(3)}\right)= N\!\int\! \d^3x\Big[\;$$
$$\underbrace{\Big(\tfrac{9\kappa p_\phi^3}{4a^4\pi_a}-\tfrac{27p_\phi^5}{2a^6\pi_a^3}-\tfrac{3a^2p_\phi V_{\phi\phi}}{2\pi_a}+\tfrac{a^3V_{\phi\phi\phi}}{6}\Big)\dph^3}_{\rm A1}
\;\underbrace{-\tfrac{3p_\phi}{2a^4\pi_a}\,\delta p_\phi^2\,\dph}_{\rm A2}
\;\underbrace{-\tfrac{9p_\phi^3}{a^5\pi_a^2}\,\delta p_\phi\,\dph^2}_{\rm A3}
\;\underbrace{-\tfrac{3a^2p_\phi}{2\pi_a}\,\dph\,(\vec\partial\dph)^2}_{\rm A4}$$
$$\underbrace{+\tfrac{3p_\phi^2}{N a\pi_a}\,\dph^2\,\partial^2\chi}_{\rm A5}
\;\underbrace{+\tfrac{3a^2p_\phi}{2N^2\kappa\pi_a}\,\dph\,\partial^2\chi\,\partial^2\chi}_{\rm A6}
\;\underbrace{+\tfrac{3p_\phi^2}{Na\pi_a}\,\dph\,\partial^i\chi\,\partial_i\dph}_{\rm A7}
\;\underbrace{+\tfrac1N\,\delta p_\phi\,\partial_i\dph\,\partial^i\chi}_{\rm A8}
\;\underbrace{-\tfrac{3a^2p_\phi}{2N^2\kappa\pi_a}\,\dph\,\partial_i\partial_j\chi\,\partial^i\partial^j\chi}_{\rm A9}\Big],$$

with (their Eq. 20-block, `matrixbases`/shift solution)
$\tilde\chi=N\,\tfrac{\sqrt6\,\kappa}{k^2a}\,\tilde\pi_2$,
$\tilde\pi_2=\sqrt{\tfrac32}\big[\big(\tfrac{p_\phi}{2}-\tfrac{a^5V_\phi}{\kappa\pi_a}\big)\delta\tilde\phi-\tfrac{p_\phi}{\kappa a\pi_a}\delta\tilde p_\phi\big]$,
and background dictionary $\dot a=-\kappa\pi_a/(6a)\Rightarrow \pi_a=-\tfrac{6}{\kappa}a^2H$ (their Eq. 10, `eoma`),
$\dot\phi=p_\phi/a^3$ (their Eq. 11, `eomphi`), $z\equiv-\tfrac6\kappa\tfrac{p_\phi}{\pi_a}=\tfrac{a\dot\phi}{H}$ (their Eq. 25).

**Two facts read directly off the printed operator, both decisive for this lane:**

1. **Nothing in $\mathcal H^{(3)}$ is quantum-corrected.** No $\rho/\rho_{\rm c}$, no $\rho_{\rm sup}$,
   no area gap $\Delta_0$, and no $\mathfrak U$ or $\tilde{\mathfrak U}$ appears anywhere in Eq. (23).
   The authors state this themselves immediately after the equation: *"By performing a Legendre
   transformation, it can be checked that these expressions agree with the third-order Lagrangian
   derived in [Maldacena 2002]"* (their §II C, after Eq. 23). The dressed potential
   $\mathfrak U$ (their Eq. 22, `potu`) enters only the **quadratic** Hamiltonian, and its quantum
   version $\tilde{\mathfrak U}$ (their Eq. 42, `qpot`) only the **free** equation of motion
   $(\tilde\Box-\tilde{\mathfrak U})\hat{\dph}=0$ (their Eq. 38, `eqnspert`) on the dressed metric
   $\tilde g_{ab}=\tilde a^2(-\d\tilde\eta^2+\d\vec x^2)$ (their Eqs. 39–41, `dres`/`ta`/`teta`).
2. **Every term carries the background scalar momentum $p_\phi$ (or a $V$-derivative).** A1–A7 and A9
   carry an explicit $p_\phi^n$; A8's only $p_\phi$-free prefactor is compensated because
   $\chi\propto p_\phi\,\dph+p_\phi\,\delta p_\phi+V_\phi\,\dph$ through $\tilde\pi_2$ above. Hence
   $\mathcal H^{(3)}\to0$ identically as $p_\phi\to0$ at $V_\phi=V_{\phi\phi}=V_{\phi\phi\phi}=0$.
   In $\zeta$-language this is the familiar statement that the cubic action is $O(\epsilon)$, with
   $\epsilon=\kappa p_\phi^2/(2a^6H^2)$.

### 1.2 Mapping table, operator by operator

Gauge dictionary (their Eq. 25, `zetadph`, first line): $\mathcal R=-\tfrac az\dph+O(\dph^2)$, i.e.
$\dph=-\tfrac za\zeta$; and from their $\mathcal H^{(2)}$ (Eq. 21, `hams`), $\delta p_\phi=a^3\dot{\dph}$
at $N=1$. The lab column is lane (a) §1 (`VERTEX_TABLE_2026-09-03.md`) at $c_s=1,\ \lambda=0$, where
$\tilde\chi\equiv\partial^{-2}\dot\zeta$.

| ABS term (Eq. 23) | structure | $\epsilon$-order | lab counterpart (lane (a)) | quantum-corrected? |
|---|---|---|---|---|
| A1 ($\kappa p_\phi^3$, $p_\phi^5$ pieces) | $\dph^3$, no derivative | $\epsilon^{3/2},\epsilon^{5/2}$ | no bare $\zeta^3$ vertex exists in Maldacena form: absorbed by the redefinition **R1** ($\eta_{\rm sr}\zeta^2/4$) + total derivatives | **no** — classical, $V$-independent |
| A1 ($V_{\phi\phi}$, $V_{\phi\phi\phi}$ pieces) | $\dph^3$ | — | **outside lane (a)'s scope** (lane (a) is built at $V=0$, $\lambda=0$); vanishes in ABS's own kinetic-dominated bounce regime | **no** — classical potential sector |
| A2 $-\tfrac{3p_\phi}{2a^4\pi_a}\delta p_\phi^2\dph$ | $\zeta\dot\zeta^2$ | $\epsilon^2$ | **V2** $a^3\epsilon^2\,\zeta\dot\zeta^2$ | **no** |
| A3 $-\tfrac{9p_\phi^3}{a^5\pi_a^2}\delta p_\phi\dph^2$ | $\zeta^2\dot\zeta$ | $\epsilon^2$ | **V5** $\tfrac12a^3\epsilon\dot\eta_{\rm sr}\,\zeta^2\dot\zeta$ | **no** |
| A4 $-\tfrac{3a^2p_\phi}{2\pi_a}\dph(\vec\partial\dph)^2$ | $\zeta(\partial\zeta)^2$ | $\epsilon^2$ | **V3** $a\epsilon^2\,\zeta(\partial\zeta)^2/a^2$ | **no** |
| A5 $+\tfrac{3p_\phi^2}{Na\pi_a}\dph^2\partial^2\chi$ | $\zeta^2\partial^2\tilde\chi=\zeta^2\dot\zeta$ | $\epsilon^2$ | **V5** (+ **V2** after parts) | **no** |
| A6 $+\tfrac{3a^2p_\phi}{2N^2\kappa\pi_a}\dph(\partial^2\chi)^2$ | $\zeta(\partial^2\tilde\chi)^2$ | $\epsilon^3$ | **V6/V7** constraint sector | **no** |
| A7 $+\tfrac{3p_\phi^2}{Na\pi_a}\dph\,\partial^i\chi\partial_i\dph$ | $\zeta\,\partial\zeta\,\partial\tilde\chi$ | $\epsilon^2$ | **V4** $-2a^3\epsilon^2\dot\zeta\,\partial\zeta\,\partial\tilde\chi$ (after parts) | **no** |
| A8 $+\tfrac1N\delta p_\phi\,\partial_i\dph\,\partial^i\chi$ | $\dot\zeta\,\partial\zeta\,\partial\tilde\chi$ | $\epsilon^2$ | **V4** | **no** |
| A9 $-\tfrac{3a^2p_\phi}{2N^2\kappa\pi_a}\dph\,\partial_i\partial_j\chi\,\partial^i\partial^j\chi$ | $\zeta(\partial_i\partial_j\tilde\chi)^2$ | $\epsilon^3$ | **V6+V7**, *in exactly the form lane (a) verified*: $V6+V7\to-\tfrac12a^3\epsilon^3\zeta\dot\zeta^2+\tfrac12a^3\epsilon^3\zeta(\partial_i\partial_j\tilde\chi)^2+\text{t.d.}$ | **no** |
| — (absent in ABS) | $\dot\zeta^3$ | — | **V1**, coefficient $\propto(1-c_s^{-2})+2\lambda$ — **zero** for a canonical scalar, consistent with its absence from Eq. (23) | — |
| — | boundary/redefinition | — | **R1–R4** reproduced by their Eq. 25 lines 2–3 ($\tfrac{d}{dt}[\tfrac az\dph]^2$, $(\vec\partial\dph)^2$, $\partial^{-2}\partial_i\partial_j$, $\partial\chi\partial\dph$ terms) | **no** |

**Result of §1.** The mapping is complete and onto: every operator in ABS's $\mathcal H^{(3)}$ has a
lane-(a) counterpart, and every lane-(a) vertex that survives at $c_s=1,\lambda=0$ appears in ABS.
**Not one term is quantum-corrected.** This *corrects* the statement recorded in the 2026-09-03 lane
(c) file and carried into ledger row 2 — *"Agullo+2017's dressed-metric $H^{(3)}$ quantum-geometric
operator is NOT contained in S1"*. It is contained in S1, exactly and term-by-term. What S1 does not
contain is not an **operator** but a **regime**: ABS evaluate the same operators with the full
(non-super-Hubble, oscillatory, non-adiabatically-excited) mode functions of their Eq. (60), `chieq`,
$v_k''+(k^2+f(\eta))v_k=0$ with $f=a^2(\tilde{\mathfrak U}-R/6)$, whereas lane (a)/(b) evaluated them
with the super-Hubble reduction $\zeta=C_1+C_2J$ valid only for $k\eta_B\lesssim10^{-2}$.

---

## 2. The scale of the enhancement, in the lab's $k\eta_B$

### 2.1 What ABS define (literature)

*Their §IV A:* "we define the bounce scale $k_{\rm LQC}$ as
$k_{\rm LQC}\equiv a(\eta_B)\sqrt{R_{\rm B}/6}\approx a(\eta_B)\sqrt{\kappa\rho_{\rm B}}$ … we expect the
power spectrum to be significantly affected by the bounce for modes with $k\lesssim k_{\rm LQC}$."
*Their §V*, using $a(t)=a_B(1+3\kappa\rho_{\rm B}t^2)^{1/6}$ (kinetic-dominated LQC bounce, their
citation to Bolliet+2015), locates the pole of $a^{-1}$ at $t_p=i/\sqrt{3\kappa\rho_{\rm B}}$, i.e.
$$\eta_p=i\sqrt{\pi/3}\,\frac{\Gamma[5/6]}{2\Gamma[4/3]}\frac{1}{a_B\sqrt{\kappa\rho_{\rm B}}}=i\,\frac{\alpha}{k_{\rm LQC}},\qquad \alpha\simeq0.64677,$$
whence "the bounce produces a contribution to $f_{\rm NL}(k_1,k_2,k_3)$ whose amplitude changes with
$k_i$ according to $e^{-\alpha(k_1+k_2+k_3)/k_{\rm LQC}}$, when $(k_1+k_2+k_3)\gtrsim k_{\rm LQC}$."
Their summary point (4) adds: modes with $k\gg k_{\rm LQC}$ are unaffected; and point (7)/§IV point 4:
the power spectrum departs from scale invariance for $k\lesssim k_{\rm LQC}$ but $f_{\rm NL}$ does so
for $k\lesssim10\,k_{\rm LQC}$, so there is a window $k\in(2k_{\rm LQC},10k_{\rm LQC})$ where the
power-spectrum effect is already negligible while the $f_{\rm NL}$ effect is not.

### 2.2 Conversion to $k\eta_B$ (computed, `lane9c_scale_window.py`)

The lab's $\eta_B$ is the conformal half-width of the NEC-violating window, which in LQC is
$\rho\ge\rho_{\rm c}/2$ for any matter content (since $\dot H=-\tfrac\kappa2(\rho+P)(1-2\rho/\rho_{\rm c})$).
With $\kappa=1$, $a_B=1$ (lane (a) conventions), so that $k_{\rm LQC}=\sqrt{\rho_{\rm B}}$:

| background | $a$ near the bounce | NEC edge | $\eta_B\sqrt{\rho_{\rm B}}$ | $k_{\rm LQC}\eta_B$ |
|---|---|---|---|---|
| lab **LQC dust** (lane (a) Table 2) | $a^3=1+\tfrac34\rho_{\rm c}t^2$ | $a^3=2$ | $\tfrac2{\sqrt3}\int_0^1\!(1+u^2)^{-1/3}\d u=1.0601$ | **1.060** |
| ABS **kinetic-dominated** (their §V) | $a^6=1+3\kappa\rho_{\rm B}t^2$ | $a^6=2$ | $\tfrac1{\sqrt3}\int_0^1\!(1+u^2)^{-1/6}\d u=0.5529$ | **0.553** |

and their pole sits at $|\eta_p|=\alpha/k_{\rm LQC}=1.170\,\eta_B$ on their own background — just
outside the NEC window, as it must be. Therefore, in the lab's normalisation (LQC dust):

$$\boxed{\ k\lesssim k_{\rm LQC}\ \Longleftrightarrow\ k\eta_B\lesssim 1.06\ ,\qquad
k\lesssim10\,k_{\rm LQC}\ \Longleftrightarrow\ k\eta_B\lesssim 10.6\ ,}$$
$$|f_{\rm NL}^{\rm bounce}|\propto e^{-\alpha k_t/k_{\rm LQC}}=e^{-1.830\,k\eta_B}\ \ \text{(equilateral, }k_t=3k).$$

**Where this sits relative to the lab's bands.** The onset of the ABS enhancement is at
$k\eta_B\approx1$ — i.e. **exactly the row-9 regime**, and **two decades above the S1 validity band**
$k\eta_B\lesssim10^{-2}$ in which $\Delta f_{\rm NL}^{\rm bounce}=-\tfrac5{24}\rho_B$ was computed.
Note the sense of the inequality: ABS's $e^{-1.83k\eta_B}$ is a **suppression at large $k$**, so the
lab's band $k\eta_B\lesssim10^{-2}$ lies on the *plateau* of their bounce contribution, not outside
it. The lab and ABS therefore evaluate the same operators on the same side of the same scale — and
still differ by four orders of magnitude in the answer (§3). That difference is not an operator gap.

---

## 3. Magnitude, and whether a dust background admits the operator at all

### 3.1 Their numbers (literature, quoted)

*Their §IV B:* "In the regime $k\gtrsim k_{\rm LQC}$ the result agrees with the inflationary
prediction, i.e., $f_{\rm NL}\sim\epsilon$ … For scales that were larger than the curvature radius at
the bounce, i.e., $k\lesssim k_{\rm LQC}$, $f_{\rm NL}$ oscillates between positive and negative values
with an amplitude of order $10^{3}$." Their summary point 2 gives the large-$k$ floor as
$f_{\rm NL}\sim10^{-2}$, and §VII repeats: "$f_{\rm NL}$ is of order $10^{-2}$ for large wave-numbers,
and then it increases for small wave-numbers, reaching values of order $10^{3}$." Their bounce-only
piece $\Delta f^{\rm bounce}_{\rm NL}$ (fig. 13 caption) is "the value of $f_{\rm NL}$ given only by the
first term in equation (\ref{BR}), and evaluating the integral in (\ref{Bphi}) just before the onset of
inflation" — structurally the same object as the lab's $\Delta f_{\rm NL}^{\rm bounce}$.

**"Just above the enhancement scale."** Combining the $10^3$ plateau with their §V decay law, in lab
units, $|\Delta f^{\rm bounce}_{\rm NL}|(k\eta_B)\simeq10^{3}\,e^{-1.830\,(k\eta_B-1.06)}$ (equilateral).
This crosses their own inflationary floor $10^{-2}$ at $k\eta_B\simeq1.06+\ln(10^{5})/1.830=7.4$, i.e.
at $k\simeq7\,k_{\rm LQC}$ — an internal consistency check against their independent statement that
$f_{\rm NL}$ is affected out to $k\lesssim10\,k_{\rm LQC}$.

**Convention caution.** ABS define $f_{\rm NL}\equiv-\tfrac56 B_{\mathcal R}/(\Delta_{k_1}\Delta_{k_2}+\dots)$
(their Eq. 51, `fNLdef`; $\Delta_k=2\pi^2\mathcal P_{\mathcal R}/k^3$), citing LoVerde+2007 App. A on
sign conventions. The lab uses $f_{\rm NL}=+\tfrac56B/(P_1P_2+\dots)$ (lane (a) §5), the
$\zeta=\zeta_g+\tfrac35f_{\rm NL}\zeta_g^2$ convention. **The two differ by an overall sign**; ABS's
$f_{\rm NL}$ oscillates in sign over the enhanced band anyway, so only the magnitude is comparable.

### 3.2 The four-orders-of-magnitude gap is not an operator gap

Lab (S1, LQC dust, $k\eta_B\lesssim10^{-2}$): $\Delta f_{\rm NL}^{\rm bounce}=-\tfrac5{24}\rho_B=-5/48=-0.104$.
ABS (same operators, $k\lesssim k_{\rm LQC}$): $|\Delta f^{\rm bounce}_{\rm NL}|\sim10^{3}$.
Ratio $\sim10^{4}$, on **the same operator set, on the same (plateau) side of $k_{\rm LQC}$**. The
differences that can carry it, in the order this lane can defend:

1. **Mode functions and initial state.** The lab used the super-Hubble reduction $\zeta=C_1+C_2J$
   (lane (a) §5); ABS integrate $v_k''+(k^2+f(\eta))v_k=0$ numerically from a Minkowski-like vacuum at
   $\eta_0=-281.5\,T_{\rm P\ell}$, which they state is "not a fourth-order adiabatic state (it is only
   of adiabatic order zero)" (their §IV F). Their own §IV A adds that other state choices in the
   literature give a spectrum that is **suppressed rather than enhanced** on these scales
   (their citations deBlas–Olmedo 2016, Ashtekar+2016 ×2), which they explicitly do not consider.
   **The ABS enhancement is therefore initial-state dependent, not a state-independent prediction.**
2. **Matter sector.** Theirs is kinetic-dominated ($w\simeq+1$, $\epsilon=3$, $c_s=1$,
   $\rho\propto a^{-6}$); the lab's LQC background is dust ($w=0$, $\epsilon\to3/2$, $c_s^2=0$,
   $\rho\propto a^{-3}$). Vertices scale as $\epsilon^2$ (V2–V4) and $\epsilon^3$ (V6, V7).
3. **Post-bounce history.** ABS have $N_{B\star}\simeq12.3$ e-folds of inflation after the bounce
   (their fig. 1 caption) that both redshift $k_{\rm LQC}$ to CMB scales and set $\mathcal P_{\mathcal R}$
   in the denominator of $f_{\rm NL}$. The lab's A3 bounce model has **no inflationary phase**.

### 3.3 Does the lab's **dust** background admit $\mathcal H^{(3)}$? (the decisive point)

Three separate answers, which must not be collapsed into one:

**(a) Literally, as an operator in $(\dph,\delta p_\phi)$: no.** $\mathcal H^{(3)}$ is built entirely
from the perturbation of a canonical scalar field, and its overall scale is $p_\phi=a^3\dot\phi$
(§1.1 fact 2). A pressureless dust component has no $\phi$, hence no $\dph$, no $\delta p_\phi$, and no
$p_\phi$. On a strict dust background ABS's operator, written in their variables, is **absent**; the
analogous object is the dust fluid's own cubic self-interaction.

**(b) As the $\zeta$-gauge cubic action on a background with the lab's $\epsilon(t)$: yes, but only in
the $c_s=1$ (S1) surrogate.** Under the Legendre transform + gauge map of §1.2, ABS's coefficients
depend on the matter only through $\epsilon(t)$ and $c_s$. Lane (a)'s S1 scheme substitutes
$\epsilon_{\rm eff}=1/2$, $c_s=1$, $z=a$ into the classical $P(X,\phi)$ cubic action — a **geometric
surrogate**, not a derivation of dust's cubic action. In S1 the ABS operator set is present, finite,
and exactly the V1–V7/R1–R4 already tabulated. This is the scheme label the lab has always carried.

**(c) As a genuine dust ($c_s^2\to0$) cubic action: singular, not merely absent.** Dust is $c_s=0$, and
every $\epsilon^2$/$\epsilon^3$ coefficient in the Chen-Huang-Kachru-Shiu form carries $c_s^{-4}$:
$$c_{V2}=\frac{a^3\epsilon}{c_s^4}(\epsilon-3+3c_s^2),\quad c_{V3}=\frac{a\epsilon}{c_s^2}(\epsilon-2s+1-c_s^2),\quad c_{V4}=-\frac{2a^3\epsilon^2}{c_s^4},\quad c_{V6}=\frac{a^3\epsilon^3}{2c_s^4},\quad c_{V7}=\frac{a^3\epsilon^3}{4c_s^4},$$
all divergent as $c_s\to0$. **This is the same pathology the lab already measured**: lane (a)'s S2
effective-fluid scheme diverges as $d_{\rm cut}^{-1}$ with no limit (slopes $-1.005/-1.007/-1.007$).
So the honest statement is not "dust has no such operator" but "**the $P(X,\phi)$ parametrisation of
that operator has no finite $c_s\to0$ limit, and the lab has already demonstrated the divergence
numerically**". A finite dust answer requires a different formalism (irrotational-dust/mimetic
constraint algebra, or a hydrodynamical cubic action with a physical UV completion), which no lane of
this program has built.

**A caveat that cuts the other way, and must be recorded.** ABS's own §V concludes: *"since it is
only the complex pole of the scale factor at the bounce that accounts for the main features of
$f_{\rm NL}$, it is expected that bounces in other cosmological models different from LQC will produce
similar non-Gaussianity."* Their mechanism is the pole of $a^{-n}(\eta)$ at $|\eta_p|=1.17\,\eta_B$ —
a property of the **geometry**, which the lab's LQC-dust background shares (it is a bounce with a
minimum of $a$ at the same $\rho_{\rm c}$). The mechanism is therefore *not* specific to scalar-field
matter; only the vertex prefactors are. This is why (a) alone does not settle row 9.

---

## 4. Observability: where $k_{\rm LQC}$ lands today, under the A3 paper's §V condition

The A3 multi-channel note (`research/track_a3_multichannel/SIGW_NHZ_NOTE_2026-09-04.md`, committed)
fixes the comoving bounce scale today as $k_B=1.71\times10^{15}\,{\rm Mpc^{-1}}$ at $T_B=10^{8}$ GeV,
linear in $T_B$, with $k\eta_B\equiv k/k_B$. Since $k_{\rm LQC}\eta_B=1.060$ (§2.2),
$$k_{\rm LQC}\simeq1.81\times10^{15}\Big(\frac{T_B}{10^{8}\,{\rm GeV}}\Big)\ {\rm Mpc^{-1}}.$$

| window | $k$ [Mpc$^{-1}$] | $k\eta_B$, $T_B=10^{8}$ GeV | $k\eta_B$, $T_B=10^{10}$ GeV | inside ABS's enhanced band? |
|---|---|---|---|---|
| PTA, 2 nHz | $1.3\times10^{7}$ | $7.6\times10^{-9}$ | $7.6\times10^{-11}$ | on the plateau, $\sim8$–10 decades below onset |
| PTA, 60 nHz | $3.9\times10^{8}$ | $2.3\times10^{-7}$ | $2.3\times10^{-9}$ | idem |
| PBH, low end | $10^{5}$ | $5.8\times10^{-11}$ | $5.8\times10^{-13}$ | idem |
| **PBH, high end** | $5.3\times10^{15}$ | **3.10** | $3.1\times10^{-2}$ | **yes at $T_B=10^{8}$ GeV** — inside $(2\!-\!10)k_{\rm LQC}$ |

Putting $k_{\rm LQC}$ *at the top of the PTA band* would require $T_B\simeq2\times10^{1}$ GeV,
**6.7–8.7 decades below** §V's $T_B\gtrsim10^{8}$–$10^{10}$ GeV, and independently excluded by the
paper's own BBN/baryogenesis argument. This reproduces, by a different route, A3-3's finding that the
PTA band would need $T_B\approx2.3$ GeV. **The PTA channel can never reach the ABS enhancement window.**

The **only** overlap anywhere in Track A is the extreme small-scale end of the PBH band at the bottom
of the allowed $T_B$ range: $k\approx5\times10^{15}\,{\rm Mpc^{-1}}$, $T_B\approx10^{8}$ GeV, sitting at
$k\eta_B\approx3$ — precisely ABS's $k\in(2k_{\rm LQC},10k_{\rm LQC})$ window where, in their words, the
power-spectrum effect is already negligible but the $f_{\rm NL}$ effect is not. Two independent checks
show it does not rescue that channel:

1. **The non-Gaussian tail cannot supply the missing amplitude.** A3-1b's null is a **7.0 dex deficit
   in $\Delta^2_\zeta$**. With the lab's own $\Delta^2_\zeta\approx10^{-9}$ ($\sigma_g=3.2\times10^{-5}$)
   and $\zeta=\zeta_g+\tfrac35 f_{\rm NL}\zeta_g^2$, even granting $|f_{\rm NL}|=10^{3}$ at $k\eta_B\sim3$,
   the non-Gaussian term reaches a collapse threshold $\zeta_c=0.1$ only at
   $\zeta_g=1.29\times10^{-2}=408\,\sigma$, and $\zeta_c=0.7$ at $3.4\times10^{-2}=1080\,\sigma$
   (`lane9c_scale_window.json`, `pbh_tail`). No $f_{\rm NL}$ of order $10^{3}$ moves a $400\sigma$ tail.
2. **The ABS feature is infrared, and the lab's anchor is infrared.** Their enhancement grows toward
   *small* $k$ ($k\lesssim k_{\rm LQC}$); in their scenario $\sim12$ e-folds of inflation place
   $k_{\rm LQC}$ near CMB scales, so PBH/PTA scales are on the un-enhanced ultraviolet side. The lab's
   A3 model has no inflation: CMB scales sit $\sim20$ decades **below** $k_B$, i.e. deep inside the
   enhanced region, and the lab's spectrum is *anchored there* to $A_s=2.1\times10^{-9}$ (A3-1b).
   Importing an ABS-type infrared growth and re-anchoring to $A_s$ therefore leaves the PTA/PBH band
   relatively **suppressed**, not enhanced. Quantifying this requires the computation named in §5.

---

## 5. VERDICT

**Primary verdict: NOT DETERMINABLE WITHOUT A COMPUTATION.** Named exactly:

> the scheme-S1 cubic in-in integral of lane (a)'s V2–V7 (+ R1–R4 boundary terms) evaluated with the
> **exact** mode functions of $\mu''+(k^2-W(\eta))\mu=0$ — not the super-Hubble reduction
> $\zeta=C_1+C_2J$ — on the **LQC-dust** background over $k\eta_B\in[0.1,10]$, with the initial state
> stated explicitly and varied over at least (i) the lab's contraction-phase vacuum and (ii) an
> ABS-style adiabatic-order-zero state, reporting $\Delta f_{\rm NL}^{\rm bounce}(k\eta_B)$ and its
> state-dependence. This is lane (b)'s machinery run outside its super-Hubble reduction.

Two sub-verdicts, both settled by this lane and both required for honest reporting:

**(i) The mapping question is settled: OPERATOR PRESENT AND REPRESENTABLE.** ABS's
$\mathcal H^{(3)}$ (their Eq. 23) is, by their own statement, the Legendre transform of Maldacena's
third-order Lagrangian; §1.2 maps every one of its nine terms onto lane (a)'s V2–V7/R1–R4 at
$c_s=1$, $\lambda=0$, including the $\zeta(\partial_i\partial_j\tilde\chi)^2$ structure lane (a) had
already derived independently. **No term of $\mathcal H^{(3)}$ depends on $\rho/\rho_{\rm c}$,
$\rho_{\rm sup}$, $\Delta_0$, or $\mathfrak U$**; the quantum geometry enters only the effective
background (their Eq. 32) and the *free* propagation through the dressed metric and dressed potential
(their Eqs. 39–42). **The 2026-09-03 lane (c) statement that "Agullo+2017's dressed-metric $H^{(3)}$
quantum-geometric operator is NOT contained in S1" is hereby corrected** (and the corresponding
sentence in `NEXT_SCIENCE_LEDGER.md` row 2 should be amended): the operator is contained in S1; what
S1 does not cover is the *regime* $k\eta_B\gtrsim10^{-2}$ and the *initial state*. On a **strict dust
fluid** ($c_s^2=0$) the $P(X,\phi)$ form of those same coefficients is **singular**, not absent — the
$c_s^{-4}$ divergence the lab already measured as S2's unregulable $d_{\rm cut}^{-1}$ scaling.

**(ii) The decision-relevant answer is unchanged: this route does not reopen Track A's channels.**
The enhancement window is $k\eta_B\lesssim1.06$ (onset), $\lesssim10.6$ ($f_{\rm NL}$-affected), i.e.
$k\lesssim1.8\times10^{15}(T_B/10^{8}\,{\rm GeV})\ {\rm Mpc^{-1}}$. The PTA band would need
$T_B\approx2\times10^{1}$ GeV, 6.7–8.7 decades below §V's condition. The PBH band overlaps only at its
extreme high end at the lowest allowed $T_B$ ($k\eta_B\approx3$), and there the channel's deficit is a
**7.0 dex amplitude** shortfall that a non-Gaussian tail with $|f_{\rm NL}|=10^{3}$ does not bridge
($408\sigma$ at $\zeta_c=0.1$). Row 9 stays OPEN as a *scheme/regime* item, not as a live channel.

### Sentence(s) for the A3 paper (§V or the transmission subsection)

> The transmission coefficient quoted here is a scheme-S1 result whose validity band is
> $k\eta_B\lesssim10^{-2}$. Agullo, Bolliet and Sreenath [arXiv:1712.08148] report an enhancement of
> $f_{\rm NL}$ by several orders of magnitude for modes larger than the curvature radius at the
> bounce, $k\lesssim k_{\rm LQC}=a_B\sqrt{R_{\rm B}/6}$; their third-order Hamiltonian is, as they
> state, the Legendre transform of Maldacena's classical cubic action, so it contains no operator
> beyond those used here, and their enhancement arises from the exact bounce-crossing mode functions
> and their choice of initial state rather than from a quantum-geometric vertex. In the present
> normalisation their window is $k\eta_B\lesssim1.06$, two decades above our validity band; we
> therefore neither reproduce nor refute their magnitude, and we make no claim that the bounce
> produces no orders-of-magnitude enhancement at $k\eta_B\sim1$. For the bounce temperatures
> considered in §V, $T_B\gtrsim10^{8}$–$10^{10}$ GeV, that window lies at
> $k\lesssim1.8\times10^{15}(T_B/10^{8}\,{\rm GeV})\,{\rm Mpc^{-1}}$ — seven to eight decades above the
> PTA band, and at the extreme small-scale end of the PBH band, where the amplitude shortfall we
> report is seven decades and is not bridged by a non-Gaussian tail of any plausible $f_{\rm NL}$.

---

## Artifacts

| path | role |
|---|---|
| `LANE9C_ABS_OPERATOR_2026-09-04.md` | this document |
| `lane9c_scale_window.py` → `lane9c_scale_window.json` | $k_{\rm LQC}\eta_B$, decay law, PTA/PBH overlap, NG-tail $\sigma$ |
| `reproducibility/manifests/experiments/ledger9-c-abs-operator-map.json` | reproducibility manifest (directive Q2) |
| source: `https://arxiv.org/e-print/1712.08148` (`NGLQC.tex`, v2 2018-02-26) | literature, read directly |
