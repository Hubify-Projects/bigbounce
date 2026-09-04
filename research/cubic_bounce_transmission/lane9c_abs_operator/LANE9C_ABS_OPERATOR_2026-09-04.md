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
