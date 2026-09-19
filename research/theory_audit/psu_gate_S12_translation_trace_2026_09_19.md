# PSU gate S12 — the translation term's trace part at general constant-$\eps$

**Date:** 2026-09-19 · **Lane:** `bb-LS3-psu-s12` (campaign
`CAMPAIGN_2026-09-18_publication_push.md`) · **Paper:** `arxiv/paper_su_criterion/`
(v1S.0.9, Appendix A2/A3) · **Script:** `psu_gate_S12_translation_trace_2026_09_19.py`
(exact sympy, 27 s local CPU) · **Machine output:** `…_2026_09_19.json`

## 0. The gate

`project-context/peer-reviews/DISPOSITIONS/PSU.md` §S12 (Gemini, R3VERIFY pass-2):
Appendix A3's translation term

$$T(\eps,\mu)\equiv f^{\rm init}_{\rm map}-f^{\rm fin}_{\rm map}
=\frac{5\eps}{4(3-\eps)}\,(1-3\mu^2),\qquad\text{“monopole } 0\ (\text{all }\eps)\text{”}$$

is justified in the paper by the sentence *“in the squeezed bispectrum the
$O(k_S/k_L)$ poles cancel between the two short legs, **the trace part vanishes at
$n_s=1$**, and the shear gives the quadrupole-only translation term.”* At general
constant $\eps$, $n_s\neq1$, so the exact monopole may carry an $\eps$-dependent
correction that would break the exact, $\eps$-independent
$f^{\rm init}_{\delta N}\equiv-5$. Nobody had independently re-derived the trace part.

**The assumption is real and explicit in both committed sources** — not an inference
from prose:

| file | line | what it hardwires |
|---|---|---|
| `threading_map_second_order_2026_09_04.py` | `B = Mq / kq**3 + Mp / kp**3` (in `f_of`) | $P(k)\propto k^{-3}$ |
| `fnl_monopole_adjudication_2026_09_03_general_eps.py` | `Pw = {k1:k1**-3, k2:k2**-3, k3:k3**-3}` | $P(k)\propto k^{-3}$ |

$P(k)\propto k^{-3}\iff n_s=1$. So the map assembly **and** the in-in shape it is
composed with were both computed at $n_s=1$.

## 1. Verdict

**(b) — CLOSED-WITH-CORRECTION.** Two findings, and they point in opposite directions:

1. **Gemini is right about the mechanism.** The trace part does *not* vanish
   identically. $\partial_i\xi^i=\eps\,\zeta_L$ exactly (script §S1/S2), and the
   translation term at general tilt is
   $$\boxed{\;T(\eps,\mu,n_s)=\frac{5\eps}{4(3-\eps)}\Big[1-3\mu^2+(n_s-1)\,\mu^2\Big],
   \qquad \text{monopole}\;=\;\frac{5\eps\,(n_s-1)}{12\,(3-\eps)}\;}$$
   (script §S5 — `T_of_s`, `T_monopole_of_s`). The printed “monopole $0$ (all $\eps$)”
   is therefore **true only at $n_s=1$**, and $n_s\ne1$ at general constant $\eps$
   (§4 below). *The paper's stated justification is incomplete as written.*
2. **The paper's result survives anyway — unconditionally.** The in-in shape carries an
   exactly compensating tilt term,
   $$\delta f^{\rm in\text{-}in}(n_s)=-\frac{5\eps}{12}\,(n_s-1)\,\mu^2
   \quad\Longrightarrow\quad \frac{\delta f^{\rm in\text{-}in}}{\lambda}=-\,\delta T ,$$
   so
   $$f^{\rm init}_{\delta N}(\eps,\mu,n_s)=\frac{f^{\rm in\text{-}in}}{\lambda}+f^{\rm init}_{\rm map}
   \;=\;-5\quad\textbf{exactly, for every constant }\eps\textbf{ and every }n_s .$$
   (script §S7 — `composed_general_s: "-5"`, `residual_composed_plus_5: "0"`,
   `composed_at_physical_ns: "-5"`.) The residual is identically zero *before* $n_s(\eps)$
   is substituted, so the result does not depend on the mode-function calculation of §4.

At $\eps=3/2$ (dust) the correction vanishes twice over — $n_s=1$ there exactly — so
**every number the paper actually headlines is untouched**: in-in monopole $-15/8$, the
gap $25/8$, the factor $8/3$, the composed final-label $-25/4+\tfrac{15}{4}\mu^2$
(all re-verified in script §S4).

Net effect on the manuscript: **one wrong clause in Appendix A3 to fix, and a claim to
strengthen** ($-5$ needs no scale-invariance assumption). No numerical value changes.

## 2. From-scratch derivation of the trace part (script §S1–§S2)

Nothing here is read from the committed notes; the committed kernels are used only
afterwards, as an independent cross-check.

1. Background $a=\tau^{1/\eps}$ in cosmic time $t=-\tau$, $\dot\phi^2=2\eps H^2$,
   $V=(3-\eps)H^2$; the Friedmann and $\eps$ definitions are asserted and pass.
2. The exact ADM Hamiltonian and momentum constraints are built for
   $h_{ij}=a^2e^{2\zeta}\delta_{ij}$, $N=1+\alpha$, $N_i=\partial_i\psi$, truncated at
   $O(\zeta)$, and **solved** for the two unknown functions $\alpha_1(\tau),\psi_1(\tau)$
   (`sp.solve`, unique solution). Output:
   $$\alpha_1=-\eps m\,\zeta=\dot\zeta/H,\qquad
   \psi_1=-\frac{\zeta}{H}+\chi,\quad \partial^2\chi=a^2\eps\dot\zeta ,$$
   i.e. Maldacena's first-order solution is *derived*, not assumed
   (`S1_first_order_solution`, asserts on lines with `# = zetadot/H (Maldacena), DERIVED`).
3. The fluid worldline obeys $dx^i/dt=-N^i$, so $x_i=x_f+\xi$ with
   $\xi^i=\int_{t_i}^{t_f}N^i dt$. Integrating $N^x$ term-by-term (power-law `tail`,
   convergence conditions recorded: $-m<0$ and $-m+2-2/\eps<0$) and taking the
   super-Hubble leading term on the growing mode $m=3/\eps-1$:
   $$\frac{\xi^x}{\zeta_L}=-\,\frac{i\,\eps}{k_L}
   \;\Longrightarrow\;
   \underbrace{\partial_i\xi^i=\eps\,\zeta_L}_{\textbf{trace}},\qquad
   \underbrace{\partial_x\xi^x-\tfrac13\partial_i\xi^i=\tfrac{2\eps}{3}\zeta_L}_{\textbf{shear }(xx)} .$$
   **The trace is $\eps\zeta_L$ — it never vanishes** (`S2_trace`). What the paper's
   sentence must mean is that the trace's *contribution to the monopole* cancels; §3
   shows that cancellation is what is $n_s$-dependent.
4. Relabelling is a rigid translation of the whole field,
   $F^{\rm init}(x)=F^{\rm fin}(x-\xi)\Rightarrow\Delta F=-\xi^j\partial_jF_S$, and
   $\delta N_c=\lambda\zeta$ at linear order, so in the script's
   $\delta N_c^{(2)}=\mathcal M\,\zeta_L\zeta_S$ normalisation
   $$\mathcal M_T=-\lambda\,\frac{\eps\,k_S\mu}{k_L}=\frac{\eps\,k_S\,\mu\,(\eps-3)}{3\,k_L}.$$
   **Cross-check:** this equals the committed `lab_init + wl_initextra` *exactly*
   (`S2_translation_kernel.agree: true`) — an independent reproduction of the
   threading-map note's label-change kernel from the constraints alone.

## 3. General-tilt assembly, and where $n_s$ enters (script §S3–§S5)

The squeezed assembly is redone with $P(k)=k^{\,n_s-4}$ kept symbolic
($s\equiv n_s-1$, $P(k)=k^{s-3}$):
$$f[\mathcal M]=\frac{5}{12\lambda^2}\,
\frac{\mathcal M_q P(k_q)+\mathcal M_p P(k_p)}{P(k_S)}\bigg|_{k_L\to0},\qquad
p=k_S\hat n-\tfrac{k_L}{2},\; q=-k_S\hat n-\tfrac{k_L}{2}.$$
Each $1/k_L$ pole is asserted to cancel before the $O(k_L^0)$ term is read off.

**Lemma (proved, then verified on all seven kernels).** Write the pole part of a kernel
as $\mathcal M\to(k_S/k_L)\,g(\mu)$. Then the entire tilt dependence is
$$f[\mathcal M](s)-f[\mathcal M](0)=-\frac{5s}{12\lambda^2}\,\mu\,g(\mu).$$
Pole cancellation requires $g$ odd; the surviving $O(k_L^0)$ piece comes from
$k_q^{s-3}-k_p^{s-3}\simeq(s-3)k_S^{s-4}k_L\mu$, which is where — and *only* where — $n_s$
enters. Consequences (`S5_general_tilt.pole_g`):

| kernel | $g(\mu)$ | tilt-dependent? |
|---|---|---|
| `psi2`+`grad`+`zlap`+`wl_fin` = $\mathcal M^{\rm fin}$ | $0$ | **no** — $f^{\rm fin}_{\rm map}$ is tilt-independent |
| `lab_init`+`wl_initextra` = $\mathcal M_T$ | $-\lambda\eps\mu$ | **yes** |
| $\mathcal M^{\rm init}$ | $-\lambda\eps\mu$ | yes (all of it from $T$) |

So the *whole* $n_s$-sensitivity of the map is the translation term — exactly the object
S12 names. Its correction is $\delta T=\frac{5\eps}{4(3-\eps)}s\,\mu^2$, monopole
$\frac{5\eps s}{12(3-\eps)}$.

**Validation before any general-tilt claim** (script §S4, all assertions pass at $s=0$):
per-piece $f$ for `psi2`/`grad`/`zlap`/`wl_fin` reproduce
`threading_map_second_order_2026_09_04.json` term by term;
$f^{\rm fin}_{\rm map}=-\tfrac{5\eps}{4}(1-\mu^2)$ and
$f^{\rm init}_{\rm map}=\tfrac{5\eps}{4(3-\eps)}[(\eps-2)-\eps\mu^2]$ reproduce the paper's
printed equations; both monopoles $=-5\eps/6$; $T$ reproduces the printed $T$ with monopole
$0$; the composition gives $-5$; dust gives $-15/8$, $25/8$, $8/3$ and
$-25/4+\tfrac{15}{4}\mu^2$; every map kernel $\to0$ as $\eps\to0$ (the USR/attractor rows).

## 4. $n_s$ for a constant-$\eps$ background (script §S6)

$z=a\sqrt{2\eps}\propto a\propto(-\eta)^{p}$ with $p=1/(\eps-1)$;
$z''/z=p(p-1)/\eta^2\Rightarrow\nu^2=(p-\tfrac12)^2$ (asserted), and
$P_\zeta\propto k^{3-2|\nu|}$:
$$P_\zeta\propto k^{3-2|\nu|},\qquad \nu=p-\tfrac12 .$$
Two indices must be kept apart, and the blind adjudicator (§5b) was right to insist on it:

- **the branch these kernels actually correlate** is the growing mode
  $\zeta\propto(-\eta)^{1-2p}$ (the script's $m=3/\eps-1$), whose index is
  $$n_s-1=4-2p=\frac{2(2\eps-3)}{\eps-1};$$
- **the late-time dominant super-horizon mode** has $n_s-1=3-2|p-\tfrac12|$ (it is the
  *constant* mode when $p<\tfrac12$).

They coincide exactly when $p>\tfrac12\iff1<\eps<3$, i.e. precisely where the growing branch
*is* the dominant mode (asserted at $\eps=5/4,3/2,2,5/2$). Both vanish at $\eps=3/2$.
Outside that window they part company — growing branch $\to6$ as $\eps\to0$ and $\to4$ as
$\eps\to\infty$; dominant mode $\to0$ and $\to2$ — but **nothing in the verdict depends on
which is used**, because §5's cancellation is proved identically in $n_s$ *before* any
$n_s(\eps)$ is substituted.

**So $n_s=1$ holds only at $\eps=3/2$ (and, for the dominant mode, $\eps\to0$)** — Gemini's
premise is correct; a general constant-$\eps$ background is not scale-invariant.

## 5. The in-in side and the exact cancellation (script §S7)

The committed general-$\eps$ in-in assembly is re-run with $P(k)=k^{s-3}$. This is
legitimate without touching the vertices: the second-order kernels $F(k;P,Q)$ there are
obtained from the classical super-horizon source, bilinear in two linear modes whose
$k$-dependent amplitudes factor out, so the tilt enters **only** through the external
power-spectrum weights. Re-derivation at $s=0$ reproduces
$f^{\rm in\text{-}in}=\frac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ exactly (asserted), and at
general $s$
$$\delta f^{\rm in\text{-}in}=-\frac{5\eps}{12}\,s\,\mu^2,
\qquad \text{monopole } -\frac{5\eps s}{36}.$$
Dividing by $\lambda=(3-\eps)/3$ gives $-\frac{5\eps}{4(3-\eps)}s\mu^2=-\delta T$.
**The cancellation is exact and term-by-term in $\mu$, not just in the monopole.**

Structurally: in the lemma's language the in-in bispectrum's own pole coefficient is
$g_{\rm in\text{-}in}=+\eps\mu$ and the map's initial-label pole is $-\lambda\eps\mu$; the
$1/\lambda$ in the composition makes them cancel identically. Physically — the long mode's
effect on short modes in the squeezed limit is a rescaling plus a displacement; the
displacement piece is the only tilt-sensitive one, and *the initial-position label is
precisely the label in which that displacement is undone.* That is why the composition is
$n_s$-blind, and it is a stronger statement than the paper currently makes.

## 5b. Independent blind adjudication

One `model: "fable"` adjudicator was run once, given the physical setup and the paper's claim
but **not** this note, this script, or its conclusion (it was explicitly instructed not to read
`psu_gate_S12_*`). It wrote its own sympy from the setup up. It returned **the same verdict (b)**
and the same mechanism, and every expression it reported is re-checked against this lane's
symbolic results in script §S9 — all seven agree exactly:

| quantity | agrees |
|---|---|
| $T(\eps,\mu,n_s)$ and its monopole | yes |
| $f^{\rm in\text{-}in}(\eps,\mu,n_s)$ | yes |
| $f^{\rm fin}_{\rm map}$, $f^{\rm init}_{\rm map}$ | yes |
| $f^{\rm init}_{\rm map}$ monopole at general $n_s$ | yes |
| $f^{\rm fin}_{\delta N}$ at general $n_s$ | yes |

The adjudicator also caught **two printed statements this lane had not flagged**, both confirmed
here and now carried into §7:

1. Appendix A2's “**both with monopole $-5\eps/6$**” is $n_s=1$-specific. The correct
   initial-label map monopole is
   $\frac{5\eps\,(2\eps-7+n_s)}{12(3-\eps)}$, which reduces to $-5\eps/6$ only at $n_s=1$
   (the final-label one is $-5\eps/6$ for all $n_s$).
2. The printed $f^{\rm in\text{-}in}(\mu,\eps)=\frac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ is
   the $n_s=1$ shape; at general tilt it carries the extra $-\frac{5}{12}\eps(n_s-1)\mu^2$.

And it noted, correctly, that $f^{\rm fin}_{\delta N}$ — unlike $f^{\rm init}_{\delta N}$ — *is*
$n_s$-dependent: $f^{\rm fin}_{\delta N}=\frac{5[\eps(n_s-4)\mu^2-3\eps+12]}{4(\eps-3)}$. That
is the expected asymmetry: only the initial-position label undoes the displacement.

The only difference between the two derivations was §4's mode-labelling question, reconciled
above. Neither derivation re-derives the five ADM map kernels or the in-in vertex set from
scratch; both take those from the committed notes and re-assemble them (§6).

## 6. Scope and honest limits

- The in-in generalisation inherits the committed adjudication's scope: it is the
  classical super-horizon second-order source with the committed vertex set
  (`T1`,`T3`,`T4` + the two field-redefinition pieces), particular power-law solution, no
  sub-horizon vacuum contribution beyond what that note already covers. S12 is closed
  *within that scope*; it does not re-open or re-audit that note's own scope.
- $f$ is defined throughout as $(5/12)B/(P_LP_S)$ (the map script's convention). A
  symmetrised $\Sigma PP$ denominator agrees at leading squeezed order only while
  $P_S/P_L\to0$, i.e. $n_s-1<3$ ($\eps<3$ on the $\eps>1$ branch); the result above is
  stated in the $(5/12)B/(P_LP_S)$ convention and is unaffected.
- $n_s(\eps)$ in §4 is the growing-mode index. The ekpyrotic Table I row sits on the
  *constant* mode ($m=0$) and is not governed by it; that row is unchanged either way,
  since §5's cancellation is proved before $n_s(\eps)$ is substituted.
- **Not** cross-checked against Maldacena's consistency relation, deliberately. Everything
  above is on the *growing* mode $m=3/\eps-1$; the $\eps\to0$ limit of that family is a
  non-attractor growing mode, not slow-roll inflation (the paper's attractor row is the
  separate constant mode $m=0$, for which the map is the identity at $O(k^0)$). I checked
  and the two do not line up numerically — $f^{\rm in\text{-}in}+5\to\tfrac{5}{2}\eps$ on the
  growing mode versus $\tfrac{5}{6}\eps$ for the slow-roll consistency relation — so the
  consistency relation is *not* a valid check here and is not claimed as one.
- `Abs` in $n_s-1$: for $1<\eps<3$ the argument $1/(\eps-1)-1/2$ changes sign at $\eps=3$;
  sympy's `Abs` is kept symbolic and evaluated per case rather than expanded.

## 6b. Numeric guard on the series extraction (script §S8)

Every squeezed limit above is taken by a sympy series in $k_L$ — the step most likely to
hide an error. §S8 re-evaluates the **full finite-$k_L$ assembly** in exact rationals at
$k_L/k_S=10^{-2},10^{-3},10^{-4}$ and compares with the symbolic answer:

| case | symbolic | $|{\rm err}|$ at $10^{-2},10^{-3},10^{-4}$ |
|---|---|---|
| $T$, $\eps=3/2$, $s=0$, $\mu=2/5$ | $0.65$ | $1.4\!\times\!10^{-5}$, $1.4\!\times\!10^{-7}$, $1.4\!\times\!10^{-9}$ |
| $T$, $\eps=2$, $s=2$, $\mu=2/5$ | $2.10$ | $5.3\!\times\!10^{-6}$, $5.3\!\times\!10^{-8}$, $5.3\!\times\!10^{-10}$ |
| $T$, $\eps=1/2$, $s=1/3$, $\mu=-3/4$ | $-0.125$ | $8.1\!\times\!10^{-6}$, $8.1\!\times\!10^{-8}$, $8.1\!\times\!10^{-10}$ |
| $f^{\rm fin}_{\rm map}$, $\eps=2$, $s=2$ | $-2.10$ | $4.7\!\times\!10^{-8}$ at $10^{-4}$ |
| $f^{\rm init}_{\rm map}$, $\eps=2$, $s=2$ | $0$ | $4.7\!\times\!10^{-8}$ at $10^{-4}$ |

Errors fall as $(k_L/k_S)^2$, the expected first neglected order. The $s\neq0$ rows are
genuine general-tilt evaluations, so the correction term is confirmed numerically, not
only symbolically.

## 7. Printable

Sentences for `arxiv/paper_su_criterion/main.tex` — **this lane does not edit the
manuscript**; the paper edit plus directive-G hygiene (version bump, recompile,
`/latex-audit`, byte-identical PDF re-mirror, Convex `paperVersions:bump`) is the next
lane's job.

**P1 — replace the Appendix A3 clause** “the trace part vanishes at $n_s=1$” with:

> in the squeezed bispectrum the $O(k_S/k_L)$ poles cancel between the two short legs,
> and the surviving trace contribution is proportional to $n_s-1$, so that
> $T(\eps,\mu)=\frac{5\eps}{4(3-\eps)}\big[1-3\mu^2+(n_s-1)\mu^2\big]$; at $n_s=1$ only the
> shear survives and the translation term is the quadrupole
> $\frac{5\eps}{4(3-\eps)}(1-3\mu^2)$.

**P2 — replace “monopole $0$ (all $\eps$)”** under the $T$ display with
“monopole $\frac{5\eps(n_s-1)}{12(3-\eps)}$, which vanishes at $n_s=1$”.

**P2b — Appendix A2 “Totals”**: “both with monopole $-5\eps/6$” is $n_s=1$-specific. Either
label it as such or print the general result: the final-label map monopole is $-5\eps/6$ for any
$n_s$, while the initial-label one is $\frac{5\eps(2\eps-7+n_s)}{12(3-\eps)}$.

**P2c — Appendix A4**: label the printed shape
$f^{\rm in\text{-}in}=\frac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ as the $n_s=1$ shape, or print
the general one, $\frac{5}{12}\big[\eps^2\mu^2-\eps^2+6\eps-12-\eps(n_s-1)\mu^2\big]$.

**P3 — add, after the $f^{\rm init}_{\delta N}\equiv-5$ statement:**

> The $-5$ does not rely on scale invariance. A constant-$\eps$ background is not
> scale-invariant — the growing branch carries $n_s-1=2(2\eps-3)/(\eps-1)$, which vanishes
> only at $\eps=3/2$; away from that point the translation term acquires a monopole
> $5\eps(n_s-1)/[12(3-\eps)]$, but the in-in shape acquires a compensating
> $-\tfrac{5\eps}{12}(n_s-1)\mu^2$, and the two cancel identically after the $1/\lambda$
> of the composition. The composed $f^{\rm init}_{\delta N}=-5$ is therefore exact for
> every constant $\eps$ and every spectral index.

**P4 — optional, one sentence for “What is new”:** the initial-position label is the
label in which the long mode's Lagrangian displacement is undone; this is why the
separate universe's squeezed answer is insensitive to the tilt, while the final-position
label's *map* is tilt-independent for the opposite reason (its kernel has no $1/k_L$ pole) —
and correspondingly the composed final-label value $f^{\rm fin}_{\delta N}$ *does* depend on
$n_s$, $\frac{5[\eps(n_s-4)\mu^2-3\eps+12]}{4(\eps-3)}$, while the initial-label one does not.

**P5 — reproducibility statement:** add
`research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.{py,md,json}` and
manifest `reproducibility/manifests/experiments/psu-gate-s12-translation-trace.json`.

## 8. Reproduce

```
cd research/theory_audit && python3 psu_gate_S12_translation_trace_2026_09_19.py
```
Local CPU, no network, no data, no GPU. ~27 s, $0. Every claim above is an assertion in
the script; the run is green only if all of them hold.
