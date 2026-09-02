# P1N — Claude INT referee leg, round R2

**Reviewer:** Claude INT referee leg (independent, skeptical; Classical and Quantum Gravity, article type **Paper**)
**Model:** `claude-opus`
**Manuscript under review:** `arxiv/paper1bc_ech_note/main.pdf`
**Exact-PDF binding — sha256:** `790795fe3d0cd5c3ba68234ddf3a5336d11fbfa1d402c9bc9d4b3be3013f125d`
(computed in this review by `shasum -a 256`; matches the expected `790795fe…`)
**Pages:** 10 · **Words:** 7725 (`pdftotext | wc -w`) · **Version:** v1N.0.2 · **Dated:** September 2, 2026
**Source under review:** `arxiv/paper1bc_ech_note/main.tex` (1009 lines), `references.bib` (27 entries)
**Date of review:** 2026-09-02
**Stance:** No expected verdict was supplied to this leg. Every equation, coefficient, and
numeric claim below was independently recomputed or re-derived before being asserted; every
sign/coefficient dispute is adjudicated against the frozen theory-audit artifacts, not
against a prior reviewer's verdict word. Renders at 300 DPI (`pdftoppm -r 300`) of pp. 1, 4,
6, 8, 10 were inspected.

**Sources consulted:**
`arxiv/paper1a_ech_nogo.tex` (P1A v1A.0.127); `arxiv/paper1c_nogo_survey/main.tex`
(P1C v1C.0.16); `research/theory_audit/fierz_adjudication_2026_08_05.md`;
`research/theory_audit/ech_torsion_onshell_2026_08_08.md`;
`research/theory_audit/operator_basis_adjudication_2026_08_07.md`;
R1 round dir `INT_v3/ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1/`;
`project-context/peer-reviews/DISPOSITIONS/P1N.md`;
`project-context/SSOT/paper-1n/status.md`.

---

## Verdict

# **major-revisions**

**Justification.** This is a materially better manuscript than v1N.0.1. Sixteen of the
nineteen canonical R1 items are closed correctly and verifiably; two of the three
regressions are restored faithfully; the paper's arithmetic is, where it is shown, largely
reproducible — I independently reproduced the on-shell torsion ratio
$\beta/\alpha=1/(2\gamma)=2.11$, the suppression $\gamma^2/(1+\gamma^2)=0.053$, the
finite-density benchmark $3.884\times10^{-69}$, the LQC window endpoints $0.27$–$0.41$ from
$\rho_{\rm crit}=\sqrt3/(32\pi^2\gamma^3)\rho_{\rm Pl}$, the Route-2 chain to $10^{-60}$, and
the Route-3 integration to $|\Delta\gamma/\gamma|=1.4\times10^{-6}$. I also confirmed by
explicit $\varepsilon$-algebra in a flat frame that the *structural* on-shell reductions
$\mathcal O_5^{[4]}=-6\alpha(J^5\!\cdot\!J^5)$, $\mathcal O_4^{[4]}=-24 M_{\rm
Pl}^2\alpha\beta(J^5\!\cdot\!J^5)$, and $T^a{}_{ab}J^{5b}=3\beta(J^5\!\cdot\!J^5)$ are
correct, and that $\mathcal O_4$ does vanish on pure-axial and on pure-trace-vector torsion
alike. The scoping is honest throughout: the paper repeatedly and accurately declares
channel-level rather than operator-level closure, tiers its own evidence, and names what it
does not establish. Gemini's R1 "fatal sign error" and "Fierz factor 2" claims were correctly
falsified and have not reappeared — I re-checked both against the frozen artifacts and concur.

It is nonetheless not yet acceptable. Four defects are load-bearing at CQG Paper standard.
(1) A **displayed equation is wrong by exactly $8\pi$** — verified numerically — and its
stated consequence (the $\mathcal O_4/\mathcal O_5\simeq0.22$ ordering) is thereby inverted.
(2) **O1 and O6 are the same scalar as defined**, so the advertised "rank four with a
two-dimensional null space" rests in part on a definitional tautology. (3) The **fourteen-entry
barrier catalog — the paper's central claim — carries no citations and no derivations** for
twelve of its fourteen entries, and defers them to a non-refereed repository draft; it is not
evaluable from this paper plus the public literature. (4) The paper **never engages the
specific published claim it exists to refute** (Popławski's torsion/quark cosmological
constant), which a no-go paper must.

None of these is fatal to the physics. The no-go conclusion — that every dimension-four
parity-odd density in minimal ECH is topological, Fierz-basis-reducible, or vanishing, and
that the surviving class is uniformly $M_{\rm Pl}^{-2}$-bounded — survives every finding
below unchanged, because the $8\pi$ error is a substitution slip in a coefficient whose
$M_{\rm Pl}^{-2}$ scaling is unaffected, and the O1$\equiv$O6 collapse *reduces* the list
without adding an escape operator. That is why this is major-revisions and not reject: the
result stands, the presentation and sourcing of it do not.

---

## PART A — Verification of the 19 canonical R1 items

Method: each item was checked against the current `main.tex` (line numbers cited), against the
300-DPI render where the item concerns typeset output, and against the restoration source
(P1C v1C.0.16 / P1A v1A.0.127 / the theory-audit artifacts) where the item is a regression.

### A.1 The three regressions

| ID | Verdict | Evidence |
|---|---|---|
| **DP1N-01** — (O1,O6) on-shell-branch statement | **CLOSED — VERIFIED** | `main.tex:764–778`. The branch split is present and explicit: O1, O6 vanish "identically on the *torsion-free* branch only … but the on-shell ECH torsion is nonzero, so that identity does not apply on shell", and the on-shell value is stated as $\mathcal O_1^{[4]}=\mathcal O_6^{[4]}=-\mathcal O_2^{[4]}+\tfrac12\mathcal O_4^{[4]}$. This is content-faithful to **P1C v1C.0.16 `main.tex:2084–2098`** (compared line by line). It is now *self-consistent* with the paper's own Eq. (11) second relation $2\mathcal O_1+2\mathcal O_2-\mathcal O_4=0\Rightarrow\mathcal O_1=\tfrac12\mathcal O_4-\mathcal O_2$ (`main.tex:752–753`) — the v1N.0.1 self-contradiction is gone. |
| **DP1N-02** — dual $\mathcal O_5$ normalization | **CLOSED — VERIFIED** | The normalization is declared once, at `main.tex:201–207`: "This is the paper's single normalization, used throughout (READING-I; the Freidel–Minic–Takeuchi Eq. 17/23 solution above) … none is restated in a second, silently different one." $\mathcal O_5^{[4]}=-3\kappa[\gamma^2/(1+\gamma^2)](J^5\!\cdot\!J^5)$ occurs exactly once (`main.tex:782`); a repository-wide grep for a second normalization (`3/2`, `\frac{3}{2}`, `3\kappa/2`) returns **nothing**. Matches **P1C `main.tex:351–358`** ("CONVENTION FIXED"). I additionally verified this value *from the paper's own $\alpha$*: my explicit $\varepsilon$-contraction gives $\mathcal O_5^{[4]}=-6\alpha(J^5\!\cdot\!J^5)$, and $-6\cdot\kappa\gamma^2/[2(1+\gamma^2)]=-3\kappa\gamma^2/(1+\gamma^2)$ exactly. The regression is genuinely repaired, not merely deduplicated. |
| **DP1N-03** — R13-M3 P-even / trace-vector clause | **CLOSED WITH DEFECT** | Both restored elements are present and correct: the trace-vector density Eq. (14), $T^a{}_{ab}J^{5b}=3\beta(J^5\!\cdot\!J^5)$ with $\beta=\kappa\gamma/[4(1+\gamma^2)]$ (`main.tex:809–812`), which I verified independently ($\eta^{ac}T_{cab}$ kills the axial irrep and gives $4J^5_b-J^5_b=3J^5_b$); and the "not in the excluded set" statement (`main.tex:815–824`). **However** the P-even clause was restored with an added and incorrect qualifier — see **MINOR 1**. Restoration is otherwise faithful to P1C `main.tex:2100–2110`, `2132–2136`. |

**Regression verdict: 2 of 3 fully restored, 1 restored with an introduced wording error.**

### A.2 The sixteen genuinely-new-real items

| ID | Verdict | Evidence (verified this round) |
|---|---|---|
| DP1N-04 — Popławski over-claim | **CLOSED — VERIFIED** | The identification is now scoped to $\gamma\to\infty$ at **every** occurrence: abstract `main.tex:70–72` ("in the Einstein–Cartan limit $\gamma\to\infty$, reduces to the Hehl–Datta term"); Intro `140–143`; Sec. II `218–232`; Discussion `845–849`; Conclusions `925–929`. The words "identical", "the same contact term", "algebraically identical" no longer appear unqualified. The $0.053$ suppression and the $2.11$ trace-vector ratio are stated in abstract, Sec. II and Discussion, so the reader is told the finite-$\gamma$ theory is *not* Popławski's. The signature disclaimer is present verbatim in the abstract (`115–117`). **This is at exact evidential strength**, with one residual sentence flagged as MINOR 8. |
| DP1N-05 — Hehl–Datta attribution | **CLOSED — VERIFIED** | `main.tex:212–220`: `\cite{HehlDattaNJL1971,Hehl1976}` at Eq. (3), plus `Kibble1961`, `Sciama1964`, `Shapiro2002` (review), `BoehmerBurnett2008` (torsion cosmology). All five are in the bibliography and render as [4], [5], [6], [7], [18] on p. 9–10. |
| DP1N-06 — standalone evaluability | **PARTIAL** | Genuinely closed: Route-2 arithmetic in-paper (Eq. 8 + the numeric chain, `main.tex:604–621`); Route-3 $\beta$-function and integration in-paper (Eq. 9, `632–652`); O1–O6 defined explicitly (Eq. 10); Fierz exchange row displayed (Eq. 5). All eight SHA-pinned `\artifact` targets **resolve** — I verified each with `git cat-file -e ded46bc5…:<path>`, all OK, and the commit is on `main` and on `origin/main`. **Not closed:** the barrier catalog remains unsourced and underived (**MAJOR 3**), Route 3's propagation step remains a black box (**MAJOR 6**), the NJL gap equation remains deferred (**MAJOR 7**), and the SHA-pin was applied to the `\artifactbase` macro but **not** to the `.bib` entries (**MINOR 4**). |
| DP1N-07 — O1–O6 undefined | **CLOSED — VERIFIED** | Eq. (10) `main.tex:727–737`, rendered legibly on p. 6 (300 DPI, checked). Dimensions audited: $\mathcal O_{1,2,4,6}$ carry explicit $M_{\rm Pl}^2$ and $\mathcal O_{3,5}$ sit at dimension 4 bare, exactly as the accompanying sentence claims. But see **MAJOR 2** — the definitions given make two entries coincide. |
| DP1N-08 — meta/provenance language | **PARTIAL** | In `main.tex` the closure is clean: a grep for `supersed*`, `earlier draft`, `earlier catalog`, `merges`, `this Note`, `version histor*`, `theory-audit record` returns **zero hits**, and `\date{\paperTimestamp}` (`main.tex:63`) prints "September 2, 2026" only — confirmed on the p.1 render. **But the language survives in `references.bib` and is printed on p. 10** — see **MINOR 5**. |
| DP1N-09 — Eq. (4) drops the $\gamma$ factor | **CLOSED — VERIFIED** | Eq. (7), `main.tex:296–298`: $G_s=-\frac{3\kappa}{16}\frac{\gamma^2}{1+\gamma^2}<0$, with the explicit limit clause "(Einstein–Cartan limit $\gamma\to\infty$: $G_s\to-3\kappa/16$, the value used for the order-of-magnitude benchmark above)" and the P1A declared-interaction citation at `293–295`. Confirmed on the p. 1 render (abstract) and in-body. |
| DP1N-10 — the $\propto$ pair mis-divides | **CLOSED — VERIFIED** | `main.tex:237–248` now states the defect explicitly and correctly: the two bare $\propto$ statements alone give $1/\gamma$, and $1/(2\gamma)$ follows only from the explicit constants. I checked the algebra: $\beta/\alpha=[\kappa\gamma/4]/[\kappa\gamma^2/2]=1/(2\gamma)$. Correct. |
| DP1N-11 — $s_H$ unfixed | **CLOSED — VERIFIED** | `main.tex:199–201`: "$s_H=+1$ fixed by the Holst-sign convention of Eq. (1) (the ratio would carry the opposite sign under $s_H=-1$)". Consistent with the artifact `[L10]`,`[L13]`,`[L46]`,`[L47]`. |
| DP1N-12 — trace-vector size understated | **CLOSED — VERIFIED** | $2.11$ at $\gamma=0.2375$ stated in abstract (`102–104`), Sec. II (`245–248`), Discussion. Recomputed: $1/(2\times0.2375)=2.105$. The word *larger* is italicized in all three places, so the reader cannot miss the ordering. |
| DP1N-13 — $3.6\times10^{-69}$ inconsistent | **CLOSED — VERIFIED** | Eq. (6) and `main.tex:256–273`. I recomputed the whole chain from scratch: with $\hbar c=1.97327\times10^{-5}\,$eV·cm, $n_\psi=100\,$cm$^{-3}=7.684\times10^{-13}\,$eV$^3$; $\kappa=8\pi/M_{\rm Pl}^2=1.686\times10^{-55}\,$eV$^{-2}$; $\kappa n_\psi^2=9.957\times10^{-80}\,$eV$^4$ (paper: $9.954\times10^{-80}$, agrees to 3 sf); $\rho_\Lambda=(2.25\,$meV$)^4=2.563\times10^{-11}\,$eV$^4$; ratio $=3.885\times10^{-69}$ (paper: $3.884\times10^{-69}$). The parenthetical explanation of the superseded $3.6\times10^{-69}$ also checks: $(2.29/2.25)^4=1.073$ and $3.884/1.073=3.62$. **Fully correct.** "$\approx68$ orders" is right. |
| DP1N-14 — $\rho_{\rm crit}$ undefined | **CLOSED — VERIFIED** | B12, `main.tex:557–568`, restores the window inline *and* explains its provenance more carefully than P1A did. Recomputed $\rho_{\rm crit}/\rho_{\rm Pl}=\sqrt3/(32\pi^2\gamma^3)$: at $\gamma=0.2375\to0.4094$; at $\gamma=0.274\to0.2666$. Squares: $0.168$ and $0.0711$ → the quoted $0.07$–$0.17$. Correct, and the scheme-dependence caveat is a genuine improvement. (It does, however, collide with B7 — **MAJOR 5**.) |
| DP1N-15 — Table I "Src." legend | **CLOSED WITH DEFECT** | Legend present in the caption, `main.tex:428–439`, and legible at 300 DPI. But it misidentifies a symbol — **MINOR 2**. |
| DP1N-16 — "closed operator-level" vs Table II | **CLOSED — VERIFIED** | `main.tex:623–628`: "closed at the operator level *modulo the spanning assertion of Sec. VI* (Tier-II, per Table II — not a Tier-I closure)". Verified against Table II's R2 row, which reads "(III) birefringence leg; (II) dark-energy leg (both branches)" — consistent. |
| DP1N-17 — `\artifact{}` filenames invisible | **CLOSED — VERIFIED** | `\artifactbase{path}{filename}` (`main.tex:50`) prints the filename as the link text, and the four artifacts are in an un-floated `itemize` (`953–972`). Verified on the p. 9/10 render: filenames visible, list sits with its introducing sentence, no float displacement. |
| DP1N-18 — unused bib entries | **CLOSED — VERIFIED** | Machine-checked: `references.bib` has exactly **27** `@` entries; the set of `\cite` keys in `main.tex` is exactly **27** and the two sets are identical (no unused, no undefined). `main.log` reports **0 undefined citations/references**. |
| DP1N-19 — $\beta_{\rm obs}$ significances | **CLOSED — VERIFIED** | `main.tex:662–669`, rendered p. 6: "$\approx3.6\sigma$ for WMAP+Planck and $\approx2.9\sigma$ for ACT DR6 … statistical indications rather than established detections", plus the non-comparability caveat. Arithmetic checks: $0.342/0.094=3.64$; $0.215/0.074=2.91$. |

### A.3 The page/venue decision

| ID | Verdict | Evidence |
|---|---|---|
| DP1N-20 — page budget / venue form | **PARTIAL** | Grown to 10 pp / 7725 words (from 6 pp / 4144), by real content, not padding — I read the added material and it is substantive (Eq. 10 definitions, Eqs. 8–9 route arithmetic, Eq. 5 Fierz row, the second-order verification subsection, the "what is established" subsection). CQG **Paper** form is correct: 7725 words is far above the Note ceiling. But the R1 audit's diagnosis was that the page budget is the *mechanism* producing the evaluability defects, and MAJOR 3, 6 and 7 below show that mechanism is still operating. See §C on adequacy. |

### A.4 R1 closure tally

| Class | Count |
|---|---|
| **Closed — verified** | **16** (DP1N-01, 02, 04, 05, 07, 09, 10, 11, 12, 13, 14, 16, 17, 18, 19 = 15, plus DP1N-03's two restored elements counted under "with defect" below) |
| **Closed with defect** (substance restored, wording/label wrong) | **2** (DP1N-03, DP1N-15) |
| **Partial** (real progress, item not discharged) | **2** (DP1N-06, DP1N-08) — plus DP1N-20 partial |
| **Not closed** | **0** |
| Regressions restored faithfully | **2 of 3** (DP1N-01, DP1N-02); DP1N-03 restored with an introduced error |
| Falsified R1 claims re-checked and still falsified | **3 of 3** (Gemini sign, Gemini Fierz factor 2, Grok "future date") |

Counting DP1N-01 and DP1N-02 under "verified" and DP1N-03 under "with defect": **15 verified, 2 with defect, 2 partial** across DP1N-01–19, i.e. **no R1 item was closed dishonestly or by dismissal.** Every closure I checked was a real edit backed by real content. That is worth stating plainly: the closure round was performed in good faith and to a high standard.

---

## PART B — Fresh referee read (independent of the R1 board)

Findings are numbered and ordered by severity. Every equation-level finding was recomputed
before being asserted.

### MAJOR

---

**MAJOR 1 — Eq. (13) is wrong by exactly a factor $8\pi$, and the size ordering it is used to establish is consequently inverted.**

*Location:* `main.tex:796–799`; PDF p. 7, Eq. (13). Reused at `main.tex:802–804` (the $0.22$ ratio).

*The claim.*
$$\mathcal O_4^{[4]}=-24\,M_{\rm Pl}^2\,\alpha\beta\,(J^5\!\cdot\!J^5)=-\frac{3\kappa\gamma^3}{(1+\gamma^2)^2}(J^5\!\cdot\!J^5)$$

*The defect.* The two sides are not equal under this paper's own conventions. The paper fixes
$\kappa=8\pi G=8\pi/M_{\rm Pl}^2$ (`main.tex:180`), hence $M_{\rm Pl}^2\kappa^2=8\pi\kappa$,
not $\kappa$. With the paper's own $\alpha=\kappa\gamma^2/[2(1+\gamma^2)]$ and
$\beta=\kappa\gamma/[4(1+\gamma^2)]$ (`main.tex:198–199`):
$$-24\,M_{\rm Pl}^2\alpha\beta=-24\,M_{\rm Pl}^2\frac{\kappa^2\gamma^3}{8(1+\gamma^2)^2}=-3\,M_{\rm Pl}^2\kappa^2\frac{\gamma^3}{(1+\gamma^2)^2}=-24\pi\kappa\frac{\gamma^3}{(1+\gamma^2)^2}.$$
The printed right-hand side is $-3\kappa\gamma^3/(1+\gamma^2)^2$. The two differ by
$8\pi=25.132741\ldots$

*Evidence.* Computed in exact arithmetic: LHS$/$RHS $=25.13274122871835$ against
$8\pi=25.132741228718345$. The discrepancy is the substitution step alone, not the tensor
algebra: I verified the structural coefficient $-24\alpha\beta$ **independently and it is
correct**, by contracting $\varepsilon^{\mu\nu\rho\sigma}T^\lambda{}_{\mu\nu}T_{\lambda\rho\sigma}$
numerically with $T_{abc}=\alpha\varepsilon_{abcd}J^{5d}+\beta(\eta_{ab}J^5_c-\eta_{ac}J^5_b)$
in a flat mostly-plus frame with $\varepsilon_{0123}=+1$, $\varepsilon^{\mu\nu\rho\sigma}=-\varepsilon_{\mu\nu\rho\sigma}$
and generic $\alpha,\beta,J^5$: the result is exactly $-24\alpha\beta(J^5\!\cdot\!J^5)$. The
same computation confirms the paper's two adjacent structural claims — $\mathcal O_4$
vanishes on pure-axial torsion and on pure-trace-vector torsion alike, and is carried
entirely by the cross term. Only the $\kappa$ substitution fails.

*Consequence.* The stated ratio is wrong and its qualitative import reverses. With the
corrected coefficient,
$$\frac{\mathcal O_4^{[4]}}{\mathcal O_5^{[4]}}=\frac{8\pi\gamma}{1+\gamma^2}=5.65\ \text{at }\gamma=0.2375,$$
not the printed $\gamma/(1+\gamma^2)\simeq0.22$. So $\mathcal O_4$ is roughly $5.7\times$
**larger** than $\mathcal O_5$ at the benchmark, not $4.5\times$ smaller. This is precisely
the kind of size statement the paper elsewhere (correctly, and to its credit) insists on
getting right — cf. the $\beta/\alpha=2.11$ discussion, where the paper italicizes *larger*.

*Provenance (for the authors, not a defence).* The identical error is in the restoration
source, **P1C v1C.0.16 `main.tex:2118–2122`**, which additionally quotes a "bare invariant"
$-192\pi^2G^2[\gamma^3/(1+\gamma^2)^2]$ — dimensionally inconsistent, since $(J^5\!\cdot\!J^5)$
has mass dimension 6 and a dimension-4 density therefore requires a coefficient of dimension
$-2$, i.e. one power of $G$, not two. The correct value by the route above is
$-192\pi^2G\,\gamma^3/(1+\gamma^2)^2$. The error is therefore inherited rather than
introduced in v1N.0.2, but it is now printed in a manuscript being submitted, and the
inherited status is invisible to a referee.

*What the paper should do.* Correct Eq. (13) to $-24\pi\kappa\gamma^3/(1+\gamma^2)^2$ (or
equivalently $-192\pi^2G\gamma^3/(1+\gamma^2)^2$), correct the ratio to $8\pi\gamma/(1+\gamma^2)\simeq5.65$,
and adjust the surrounding sentence, which currently reads as though $\mathcal O_4$ were a
small correction to $\mathcal O_5$. Also re-run and re-commit
`dim4_parityodd_enumeration.py` / `operator_basis_adjudication_2026_08_07.py` against the
corrected value so the artifact and the manuscript agree. **The physical conclusion is
unaffected**: both operators remain in the same Fierz-closed $(J^5\!\cdot\!J^5)$ class at the
same $M_{\rm Pl}^{-2}$ power, and the corrected $\mathcal O_4$ still $\to0$ as
$\gamma\to\infty$ (it scales as $\gamma^3/(1+\gamma^2)^2\sim1/\gamma$), so the statement that
$\mathcal O_4$ switches off in the Einstein–Cartan limit survives. But a displayed equation
in which the two sides differ by $8\pi$ cannot go to press.

---

**MAJOR 2 — O1 and O6 are the same scalar as defined, so the first null-space relation is a definitional identity and the "six-member spanning list / rank four" framing is partly an artifact of the presentation.**

*Location:* Eq. (10), `main.tex:727–737` (PDF p. 6); Eq. (11), `main.tex:749–751`; the rank
claim at `main.tex:744–748`; restated in the abstract (`main.tex:92–98`) and the Conclusions
(`main.tex:937–941`).

*The defect.* The paper defines
$$\mathcal O_1^{[4]}=M_{\rm Pl}^2\varepsilon^{\mu\nu\rho\sigma}e^I_\mu e^J_\nu R_{IJ\rho\sigma},\qquad
\mathcal O_6^{[4]}=M_{\rm Pl}^2\varepsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma},$$
where (`main.tex:739–740`) "$R$ is the curvature of the full torsionful connection". The
connection varied in Eq. (1) is an $\mathfrak{so}(1,3)$ (metric-compatible) spin connection,
so the tetrad converts frame to coordinate indices exactly: $e^I_\mu e^J_\nu R_{IJ\rho\sigma}\equiv R_{\mu\nu\rho\sigma}$
identically, off shell and on shell, torsion or no torsion. **$\mathcal O_1^{[4]}$ and
$\mathcal O_6^{[4]}$ are therefore literally the same object, written twice.**

*Consequences.* (i) The first null-space relation $\mathcal O_1^{[4]}-\mathcal O_6^{[4]}=0$
in Eq. (11) is a tautology, not a result — yet the text attributes both relations to
"Independent symbolic adjudication … expanding all six over a common basis of independent jet
monomials in exact rational arithmetic" (`main.tex:744–748`), which invites the referee to
read a trivial identity as a computational finding. (ii) The advertised "six-member spanning
list" has five distinct members. (iii) "Rank four … with a two-dimensional null space" is
then half bookkeeping: one null direction is the duplicate, only the second
($2\mathcal O_1+2\mathcal O_2-\mathcal O_4=0$) carries content. (iv) The abstract and
Conclusions both sell "a six-member spanning list … rank four", so the overstatement is in
the paper's most-read sentences.

*Note this is a presentation defect, not a physics error.* Removing the duplicate makes the
list *smaller* without opening any escape channel; every disposal statement in Sec. VI
survives verbatim, with "O1, O6" read as one operator. The closure is not weakened. But the
novelty claim attached to the enumeration is.

*What the paper should do.* Either (a) distinguish the two — if $\mathcal O_6$ was intended
as the *Riemannian* single-curvature density $\varepsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\mathring\Gamma)$
(which would be a genuinely different object on shell, and would make the O1$\neq$O6
distinction meaningful and the relation non-trivial), say so explicitly in Eq. (10); or (b)
drop $\mathcal O_6$, present a five-member list of rank four with a one-dimensional null
space, and restate the abstract and Conclusions accordingly. Option (a) is likely what the
underlying computation actually did — the transparency section (`main.tex:374–381`) already
turns on exactly this Riemannian-vs-torsionful distinction — but as printed, Eq. (10) does
not say it.

---

**MAJOR 3 — The barrier catalog, which is the paper's headline contribution, is neither derived nor sourced: twelve of fourteen entries carry no citation and no calculation.**

*Location:* Sec. IV, `main.tex:463–589` (PDF pp. 4–5). Abstract `main.tex:85–92`; Conclusions
`main.tex:934–936`.

*The defect.* The abstract promises "fourteen distinct mechanism-class constraints … that
jointly close the four enumerated channels", and this is the paper's principal novelty claim.
I extracted every `\cite` in the barrier section: there are exactly **four citation
instances, all inside B12** (`Golden2026P1a`, `Ashtekar2011`$\times2$, `GhoshMitra2005`).
**B1–B11 and B13–B14 contain no citation at all**, and none contains a derivation. Concretely,
the following are asserted in one or two sentences with no support a referee can check:

- **B1** — the Poincaré-gauge-theory ultralight-torsion mass spectrum and the scaling
  $g_{\rm eff}\sim1/(M_{\rm Pl}\sqrt{|t_3|})$, $\sqrt{|t_3|}\sim m_T^{-1}$. The paper honestly
  labels this "a labeled scaling ansatz … not a derived equality", but $t_3$ is a PGT
  Lagrangian parameter whose provenance is a substantial literature (Hayashi–Shirafuji,
  Yo–Nester, Blagojević–Hehl) that is nowhere cited. A CQG referee cannot check the ansatz.
- **B2** — a claimed *iff* ("mass protection $\iff$ no geometric fingerprint") in metric-affine
  gravity. A biconditional is a strong logical claim; here it has neither proof nor reference.
- **B3** — "diffeomorphism invariance forces the torsion fluctuation to couple to the
  curvature invariants like any other scalar" and "torsion decouples from the FRW background
  precisely at the bounce density". The second clause is a sharp dynamical statement
  ("precisely at") presented without a calculation.
- **B9** — Liouville/phase-space conservation forbidding irreversible post-bounce selection.
  Correctly flagged heuristic, but with no reference and no statement of the measure being
  conserved.
- **B10, B11, B13** — generic/specific dilemma, universal gauge decoupling, gravitational
  democracy: all plausible, all unsupported.

*Why this is MAJOR rather than a style point.* The paper's own Sec. IV opening concedes that
five entries "are general naturalness or classification arguments rather than sharp
ECH-specific calculations" and one is heuristic — which is exactly the honesty this programme
is right to insist on. But honesty about evidentiary tier does not substitute for evidence.
As it stands the central claim of the paper is a list of fourteen assertions, and the reader
is directed for the derivations to `Golden2026P1cArxiv` — a GitHub-hosted, non-refereed,
explicitly "not independently submitted" repository draft by the same author (ref. [26], p.
10). That is not an acceptable evidentiary base for a CQG Paper's principal claim.

*What the paper should do.* For each of B1–B13 supply *either* a literature citation that
establishes the mechanism *or* two to four lines of derivation in-paper (an appendix is the
natural home). Barriers that can be supported by neither should be demoted out of the
"fourteen distinct mechanism-class constraints" headline and presented as conjectural. This
is the single largest source of the page-budget pressure identified in DP1N-20, and the
reason 10 pp is still short (see §C).

---

**MAJOR 4 — The paper never analyses the published claim it exists to refute.**

*Location:* Popławski's dark-energy proposal is cited only twice: Intro `main.tex:145–147`
(`\cite{Poplawski2011,Poplawski2012}`) and the Acknowledgments. It is never stated, never
quantified, and never mapped to any of Routes 1–4.

*The defect.* The paper's thesis is a no-go: minimal ECH torsion cannot source the observed
$\rho_\Lambda$. The most prominent published claim to the contrary is Popławski's own —
Ref. [10] in this bibliography, *Gen. Rel. Grav.* **44**, 491 (2012), "Cosmological constant
from quarks and torsion", which the introduction paraphrases in a single subordinate clause
as a "proposed link from bounce-scale torsion to a late-time vacuum energy". The manuscript
then proceeds to enumerate *its own* four routes (NJL contact, one-loop Holst, Immirzi
running, parity-odd CMB) and close those. At no point does it (a) state Popławski's
mechanism, (b) identify which of R1–R4 it corresponds to (it is closest to R1, but the
correspondence is nowhere asserted), or (c) show where it fails.

A referee — and any reader who knows the literature — will ask the obvious question: *does
this paper actually refute Popławski's cosmological constant, or does it refute four routes
of the authors' own devising that may or may not include his?* As written the manuscript
cannot answer. This is especially conspicuous given that the paper builds its entire positive
half on identifying its contact term with Popławski's bounce term: the identification is made
carefully and at exact evidential strength for the *bounce* (DP1N-04, verified above), and
then simply not made at all for the *dark energy*, which is the half the paper is claiming to
close.

*What the paper should do.* Add a subsection — half a page would do — stating Popławski's
proposed torsion/quark-condensate route to $\Lambda$ in its own terms with its own equation,
mapping it onto the route taxonomy of Secs. V–VI, and identifying which barrier(s) close it
and at what evidentiary tier. If it maps onto R1, the NJL result of Sec. II already does most
of the work and the paper is simply failing to claim its own strongest result. If it does not
map onto R1–R4, then the enumeration "the four enumerated channels" is incomplete and the
abstract's closure claim is too strong.

---

**MAJOR 5 — B7 and B12 contradict each other on whether $\gamma$ is uniquely fixed, and B7's supporting cross-reference points to a section that contains no such content.**

*Location:* B7, `main.tex:511–517` (PDF p. 5); B12, `main.tex:555–573` (PDF p. 5).

*The defect.* B7 closes the cyclic-vacuum-selection escape by asserting that "$\gamma$ is
fixed at a single universal value by the loop-quantum-gravity area spectrum
(Sec.~\ref{sec:theory}), so minimal ECH provides no landscape of $\gamma$ values for a
selection mechanism to operate on." Two problems, both checkable:

1. **The cross-reference is empty.** Sec. II (`sec:theory`) contains no discussion of the LQG
   area spectrum, of black-hole entropy counting, or of how $\gamma$ is fixed. I grepped the
   full source: "area" occurs at exactly two lines, `main.tex:515` (this very sentence) and
   `main.tex:561` (inside B12). Sec. II introduces $\gamma$ as "constant" and nothing more. So
   B7 forwards the reader to a section that does not support it, and supplies no reference of
   its own.
2. **B12 asserts the opposite.** Twelve entries later the paper writes that $\rho_{\rm crit}/\rho_{\rm Pl}\simeq0.27$–$0.41$
   arises because the $0.41$ endpoint uses "the standard area-gap choice $\gamma=0.2375$" while
   the $0.27$ endpoint "substitutes the SU(2) black-hole-entropy value $\gamma\approx0.274$ …
   an internal extrapolation across entropy-counting schemes … so the window is
   **scheme-dependent** rather than a single published LQC value." That is a direct statement
   that the theory does *not* fix $\gamma$ to a single universal value — it fixes it to
   different values under different counting schemes. B7's closure rests on exactly the
   premise B12 denies.

*Assessment.* I want to be careful not to overstate this: the two statements are about
different things at the level of intent (B7 is about $\gamma$ not being a *dynamical
landscape variable* across cycles; B12 is about *theoretical* uncertainty in its value within
one universe), and both can be true. But the paper never draws that distinction, and as
printed a referee reads "fixed at a single universal value" on p. 5 and "scheme-dependent" on
the same page. Since B7 is one of the fourteen load-bearing barriers and its entire content is
this uniqueness claim, the ambiguity is disqualifying as written.

*What the paper should do.* Cite the area-spectrum / entropy-counting result that fixes
$\gamma$ (Ashtekar–Singh is already in the bibliography; Ghosh–Mitra likewise), state in B7
that the relevant point is that $\gamma$ is a *fixed parameter of the theory rather than a
field with cycle-to-cycle dynamics* — which is the actual argument and is a good one — and
explicitly note that residual scheme-dependence in its numerical value (per B12) does not
supply the cycle-varying landscape a selection mechanism would require. Fix the
`Sec.~\ref{sec:theory}` cross-reference to point at B12 or at the added citation.

---

**MAJOR 6 — Route 3's closure number is not derivable from the paper: the propagation step is an unnamed "scaling relation" and the quoted range is unexplained.**

*Location:* `main.tex:645–652` (PDF p. 6).

*The defect.* The first half of Route 3 is now genuinely in-paper and genuinely checkable —
credit where due. I integrated Eq. (9) myself: with
$\mu\,\partial_\mu\gamma^2=-(\gamma^2-1)\frac{\mu^2\tilde\kappa^2}{(8\pi)^2}(23\gamma^2+5)$
and $\tilde\kappa^2=16\pi G$, the prefactor is $\mu^2/(4\pi M_{\rm Pl}^2)$, and integrating
from $\mu_{\rm UV}=10^{16}\,$GeV at $\gamma=0.24$ gives
$\Delta\gamma^2=(1-\gamma^2)(23\gamma^2+5)\mu_{\rm UV}^2/(8\pi M_{\rm Pl}^2)=1.59\times10^{-7}$,
hence $|\Delta\gamma/\gamma|=\tfrac12\Delta\gamma^2/\gamma^2=1.38\times10^{-6}$ — **the
paper's $1.4\times10^{-6}$ reproduces exactly.** Good.

Then the paper writes: "Propagated to the dark-energy channel through the mass-dimension
scaling relation between $\gamma$-running and $\rho_\Lambda$, this leaves the derived
torsion/Immirzi contribution 61–67 orders of magnitude below $\rho_{\Lambda,\rm obs}$." The
"mass-dimension scaling relation" is never written down, never cited, and never defined; and
a single input number ($1.4\times10^{-6}$) is mapped to a **six-order-wide output range**
($61$–$67$) with no explanation of what varies across the range. This is the load-bearing
number for Route 3 — it is what "closes" the route — and it is the one step of Route 3 the
referee cannot check.

*What the paper should do.* Display the scaling relation as an equation with its inputs,
state what is varied to produce the $61$–$67$ spread (presumably the choice of $\mu_{\rm UV}$
or of the operator through which $\Delta\gamma$ feeds the vacuum energy), and label its tier.
Table II already labels R3 "(II)+(III)", so a Tier-III dimensional estimate is admissible —
but it must be *shown*.

---

**MAJOR 7 — The paper's result (i) is asserted without its derivation, and defers it to a non-refereed deposit.**

*Location:* `main.tex:300–307` (PDF p. 2); abstract `main.tex:75–82`.

*The defect.* The abstract's item (i) and the Conclusions both headline that the NJL scalar
projection "is repulsive, $G_s=-(3\kappa/16)[\gamma^2/(1+\gamma^2)]$, so the real homogeneous
gap equation for this condensate channel has no nonzero solution". The body establishes
$G_s<0$ properly — Eq. (5)'s Fierz row is displayed, its scalar coefficient $+1$ is
independently sourced to the Fierz artifact (which I re-checked: the artifact solves the full
$5\times5$ Fierz matrix in both signatures and returns SS coefficient exactly $+1$, so
Gemini's R1 "factor 2" claim remains correctly falsified), and Eq. (7) follows. But the step
from $G_s<0$ to "no nonzero solution" is **stated, not shown**: the gap equation is never
written, its regulator is never specified beyond the phrase "hard-four-momentum-cutoff", and
the full derivation is deferred to `Golden2026P1a`, which the bibliography itself describes
(p. 10, ref. [15]) as "not an arXiv preprint and not peer reviewed".

*Why this matters.* The argument is short and entirely respectable — for the standard
mean-field gap equation $M=2G_sM\,I(M,\Lambda)$ with $I>0$, a negative $G_s$ makes
$2G_sI=1$ unsatisfiable, so $M=0$ is the only real homogeneous solution — and it would
occupy three lines. Leaving it out means the paper's most quotable result is, from the
referee's chair, an assertion backed by a self-deposited file. Given the effort spent
elsewhere in this version on bringing derivations in-paper (Eqs. 8, 9, 10, 5), this omission
looks like an oversight rather than a choice.

*What the paper should do.* Write the gap equation, state the regulator, give the three-line
no-solution argument, and keep the citation to the deposit for the full regulated treatment.

---

### MINOR

**MINOR 1 — "parity-even off shell" is the wrong qualifier and contradicts the same sentence; it was introduced in this version.**
*Location:* `main.tex:786–789`. The text reads: "This density is parity-*even* off shell — a
Lorentz-scalar product of two axial currents is P-even (B8) — the parity-odd label belongs to
the pre-reduction $\varepsilon$-contracted density, not to its on-shell value". The two halves
contradict: $\mathcal O_5^{[4]}=\varepsilon^{\mu\nu\rho\sigma}T^I{}_{\mu\nu}e_{I\rho}J^5_\sigma$
is $\varepsilon$-contracted and therefore parity-**odd** off shell — that is the construction
rule that admits it to the list in the first place (`main.tex:721–723`). It is the *on-shell*
value $-3\kappa[\gamma^2/(1+\gamma^2)](J^5\!\cdot\!J^5)$ that is parity-even. The restoration
source, **P1C v1C.0.16 `main.tex:2104–2106`**, carries no "off shell" qualifier — it reads
"…contact operator … — itself parity-even, since a Lorentz-scalar product of two axial
currents is P-even" — so the qualifier was added during the DP1N-03 restoration and is an
introduced error. Delete "off shell", or replace with "on shell, after reduction".

**MINOR 2 — Table I caption misnames the Barbero–Immirzi symbol.**
*Location:* `main.tex:435–439`; PDF p. 4. The caption explains that sequence letters I and K
are skipped "to avoid confusion with the imaginary unit and the Barbero–Immirzi symbol
$\kappa$." The Barbero–Immirzi parameter in this paper is $\gamma$ throughout; $\kappa$ is the
gravitational coupling $8\pi G$ (Eq. 1, `main.tex:180`). Reword to "…and the gravitational
coupling $\kappa$."

**MINOR 3 — Table II cites a bound that does not exist in the paper.**
*Location:* `main.tex:696–698`; PDF p. 7. The R3 row reads "mass-dimension lock is structural;
the **chiral-count bound** is a loose Tier-III ceiling." No chiral-count bound appears anywhere
in the manuscript — grep returns this one occurrence. It is an orphan carried over from the
source survey. Either import the bound or delete the clause.

**MINOR 4 — The SHA pin was applied to the `\artifact` macro but not to the bibliography, so five references still point at a mutable branch.**
*Location:* `references.bib:279, 287, 295, 303`; rendered as refs. [14], [23], [26] and others
on PDF p. 10. `\artifactbase` correctly pins commit `ded46bc5df8d39bbaac7bfbee16b07f0376bab34`
(I verified all eight pinned paths resolve at that commit via `git cat-file -e`, and that the
commit is on `main` and `origin/main`). But `Golden2026P1cArxiv`, `FierzAdj2026`,
`TorsionOnshell2026`, and `OperatorBasisAdj2026` still carry `.../tree/main/...` and
`.../blob/main/...` URLs, which resolve to whatever `main` contains at read time. Since these
four are the sole support for the Fierz coefficient, the on-shell irrep content, the rank-four
result, and the whole barrier catalog, the mutability matters. Pin them to the same SHA, and —
better — mint Zenodo version DOIs for all four artifacts and for P1C, as the R1 audit
recommended. A SHA-pinned GitHub URL is still a single-host, deletable reference; CQG will
prefer a DOI.

**MINOR 5 — Version-history / supersession language survives in the bibliography and is printed.**
*Location:* `references.bib:280`, rendered as ref. [26] on PDF p. 10: "…repository draft
**superseded by this Note** as the single submission target for the closed ECH dark-energy
line; not independently submitted." Also `references.bib` for `TorsionOnshell2026`: "…
**corrects an earlier purely-axial reading** valid only in the Einstein–Cartan limit". The
main text was cleaned thoroughly (grep for `supersed*|earlier draft|this Note|merges` over
`main.tex` returns zero hits) but the `.bib` was missed, so the internal-provenance narration
DP1N-08 set out to remove is still visible to the reader — and, incidentally, the manuscript
still calls itself "this Note" there while being submitted as a Paper. Rewrite both `note`
fields to describe what the artifact *is*, not what it corrects or supersedes.

**MINOR 6 — Route 2's quoted suppression does not match the quantity Eq. (8) actually defines.**
*Location:* `main.tex:604–621`; PDF p. 6. Eq. (8)'s left-hand side is
$\Delta\theta_{\rm one\text{-}loop}/(\beta_{\rm obs}[M_{\rm Pl}(\alpha/M)])$ — normalised by
$\beta_{\rm obs}$ *and* by $M_{\rm Pl}(\alpha/M)\sim10^{-2}$. The numeric chain
$10^{-3}\cdot10^{-61}/(10^{-2}\cdot6\times10^{-3})\approx1.7\times10^{-60}$ is correct (I
checked), but the text then calls this "the quoted suppression of $\gtrsim58$ orders of
magnitude **relative to the observed birefringence amplitude**". Relative to $\beta_{\rm obs}$
alone the suppression is $10^{-62}$, i.e. two orders *more*. The error is conservative and
does not weaken the claim, but the sentence misdescribes its own equation. State which ratio
the order count refers to.

**MINOR 7 — Eq. (8) is asserted rather than derived from the reference it is anchored to.**
*Location:* `main.tex:598–607`. Route 2 is "anchored in the published one-loop renormalization
of the Holst-plus-fermion sector [18]", but the paper never states what Shapiro–Teixeira's
result is, nor how $\alpha_{\rm em}/4\pi$ and $H_0/M_{\rm Pl}$ come to appear in the induced
shift. Table II honestly labels this leg Tier-III, so an ansatz is admissible — but a referee
must be able to see the anchoring. One or two sentences quoting the relevant renormalization
result would close this.

**MINOR 8 — One sentence in Sec. II simultaneously asserts and disclaims a signature-level statement.**
*Location:* `main.tex:223–231`. "…it carries the same repulsive sign at every finite $\gamma$:
a positive spin-density correction to the effective energy density would deepen, not halt,
gravitational collapse, so the sign identification with Popławski's mechanism is
signature-independent even though no formal signature bridge … is asserted." The DP1N-04
scoping is otherwise exemplary, but "signature-independent" *is* a signature-level claim, and
the argument supporting it (a statement about $\rho+3p$ in FRW) is gestured at rather than
shown. Either display the one-line $\rho+3p<0$ argument, or end the sentence at the
disclaimer.

**MINOR 9 — Route/barrier tags are used before they are defined.**
The tags `[R1]`–`[R4]` first appear in the B1 entry on p. 4 (`main.tex:463`), but Routes 1–4
are only introduced in Sec. V on p. 5. The abstract names the four channels but never maps
them to the R-numbers. Add a one-line definition of R1–R4 at the head of Sec. IV.

**MINOR 10 — The abstract is 435 words and fills page 1.**
Measured directly from the source. CQG's guidance is ~300 words; PRD-style abstracts of this
length are unusual and this one carries body-level numerics ($0.053$, $2.11$, $\beta/\alpha$,
the coefficient of Eq. 2). Cutting to ~250 words would strengthen it — the structural
dichotomy that is the paper's real selling point is currently buried in the last third.

**MINOR 11 — The paper's only rigorous result is not set as a theorem.**
*Location:* Sec. III, `main.tex:312–357`. The Tier-I result is introduced as "The catalog's
sole Tier-I rigorous result is the following", runs as prose, and is followed by an italic
"*Proof.*". For a result the paper leans on this heavily (it is B14, it is the sole Tier-I
leg, it is abstract item (ii)), give it a numbered `Theorem` environment with the hypotheses
enumerated (H1)–(H5) and the excluded cases listed as such. The mathematical content is
correct — I checked the key step, that $\tfrac12\varepsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}(\mathring\Gamma)=0$
follows pointwise from $R_{\mu[\nu\rho\sigma]}=0$ for any torsionless connection, and that this
is genuinely order-independent — but the presentation undersells it.

**MINOR 12 — Novelty of the transparency theorem needs an explicit positioning sentence.**
That the Holst term vanishes identically on a torsion-free connection is standard and dates to
Holst (1996); the paper's contribution is the packaging (all classical orders, matched-data
hypotheses, the explicit Nieh–Yan and Pontryagin disambiguation, and the corollary that
minimal ECH generates no GW birefringence or $TB$/$EB$ cross-power). That packaging is
genuinely useful and cleanly done, but the paper should say in one sentence what is new
relative to the standard statement, rather than leaving the referee to infer it. (Holst 1996
is not in the bibliography and should be.)

**MINOR 13 — `\paperVersion` is defined and never used.**
`main.tex:51`. Harmless dead macro left after the DP1N-08 `\date` fix; remove before submission.

---

### Positive verifications worth recording

These were checked and are **correct**; they should not be re-litigated by a later round.

1. **Bibliography integrity.** 27 `@` entries; 27 distinct `\cite` keys; the sets are
   identical. `main.log`: 0 undefined references, 0 undefined citations. 22 of 27 entries
   carry DOIs; the five without are the four repository artifacts and the P1C draft (see
   MINOR 4). DP1N-18 is genuinely and completely closed.
2. **All artifact targets resolve.** Eight `\artifactbase` paths plus the P1C source verified
   present at commit `ded46bc5df8d39bbaac7bfbee16b07f0376bab34`, which is on `main` and
   `origin/main`.
3. **Compile hygiene.** 0 undefined refs/citations; exactly one `Overfull \hbox` at
   4.50 pt (line 737, the Eq. 10 `align`), well under a 10 pt gate. 300-DPI renders of
   pp. 1, 4, 6, 8, 10 show no column escape, no float displacement, no clipped table; Tables I
   and II sit inside their bounds; the Data & Code list is un-floated and adjacent to its
   introducing sentence.
4. **Every numeric claim I could independently recompute reproduces**, to the precision quoted:
   $\gamma^2/(1+\gamma^2)=0.0534\to0.053$; $\beta/\alpha=1/(2\gamma)=2.105\to2.11$;
   $\kappa n_\psi^2=9.957\times10^{-80}\,$eV$^4$ vs $9.954$; ratio $3.885\times10^{-69}$ vs
   $3.884$; the $(2.29\,$meV$)^4\to3.62\times10^{-69}$ cross-check; $\rho_{\rm crit}/\rho_{\rm Pl}=0.409, 0.267$
   and squares $0.168, 0.071$; Route 2's $1.7\times10^{-60}$; Route 3's $1.38\times10^{-6}$;
   $\beta_{\rm obs}$ significances $3.64\sigma$ and $2.91\sigma$. **The single exception is
   MAJOR 1.**
5. **Structural tensor algebra verified from scratch**, in a flat mostly-plus frame with
   generic $\alpha,\beta,J^5$: $\mathcal O_5^{[4]}=-6\alpha(J^5\!\cdot\!J^5)$ (trace-vector
   piece drops out exactly, as claimed); $\mathcal O_4^{[4]}=-24M_{\rm Pl}^2\alpha\beta(J^5\!\cdot\!J^5)$
   with vanishing pure-axial and pure-trace-vector contributions (as claimed);
   $T^a{}_{ab}J^{5b}=3\beta(J^5\!\cdot\!J^5)$ (as claimed). The paper's operator reductions are
   right; only the $\kappa$ substitution in Eq. (13) is not.
6. **R1's three FALSIFIED claims re-examined and still falsified.** Gemini's "Eq. (2) sign is
   attractive" — the frozen artifact solves the connection equation from scratch in this
   paper's own conventions and reproduces the printed sign; the physical argument (a positive
   spin-density correction deepens rather than halts collapse) is also correct as far as it
   goes. Gemini's "Fierz factor 2" — the artifact's solved $5\times5$ Fierz matrix gives SS
   coefficient exactly $+1$ in both signatures. Grok's "future date" — 2026-09-02 is today.
   None should be re-opened.
7. **No fabricated result found.** Every claim I traced to a source reproduces that source, and
   where the paper's own value disagrees with a superseded one it says so explicitly and
   explains the discrepancy (the $3.6$ vs $3.884\times10^{-69}$ note is a model of how to do
   this). The scoping language throughout — "channel-level, not operator-level", "asserted
   from the construction rule, not proved by exhaustive enumeration", "never used as a
   stand-alone closure", "a labeled scaling ansatz, not a derived equality" — is accurate
   rather than defensive, and is the manuscript's strongest feature.

---

## PART C — Is 10 pp adequate, and what is still missing?

**No — 10 pp is not yet adequate, and the shortfall is specific rather than general.** The R1
audit recommended 12–16 pp; this version reached 10, and every one of MAJOR 3, 4, 6 and 7 is a
place where the missing pages would have gone. The added content in v1N.0.2 is real and
well-chosen, but it went to Secs. II, V and VI, while Sec. IV — which carries the paper's
headline claim — is unchanged in character: fourteen one-paragraph assertions in two pages.

Concretely, the following material is still missing and is what would take the paper to
roughly 14–15 pp:

| Missing material | Where it belongs | Est. |
|---|---|---|
| Citations and/or 2–4-line derivations for B1–B11, B13 (MAJOR 3) | Sec. IV, or an appendix | 2–3 pp |
| The Popławski dark-energy proposal stated, mapped to R1–R4, and closed (MAJOR 4) | new subsection in Sec. V or VI | 0.5 pp |
| The regulated NJL gap equation and its three-line no-solution argument (MAJOR 7) | Sec. II | 0.25 pp |
| Route 3's mass-dimension scaling relation, displayed, with the source of the 61–67 spread (MAJOR 6) | Sec. V B | 0.25 pp |
| The Shapiro–Teixeira one-loop result Eq. (8) is anchored to (MINOR 7) | Sec. V A | 0.15 pp |
| Theorem environment + enumerated hypotheses + novelty positioning (MINOR 11, 12) | Sec. III | 0.25 pp |

That totals ~3.5–4.5 pp of genuinely load-bearing content, landing the paper at 13.5–14.5 pp —
squarely inside the R1 audit's 12–16 pp recommendation, and comfortable for a CQG Paper. The
corrections in MAJOR 1, 2, 5 and MINOR 1–6, 8–10, 13 are edits, not additions, and cost no
pages.

**On venue form:** CQG **Paper** is correct and should not be revisited. At 7725 words the
manuscript is three times the Note ceiling already, and the additions above will take it
further.

---

## Summary of findings

| Severity | Count |
|---|---|
| **MAJOR** | **7** |
| **MINOR** | **13** |

**MAJOR:** (1) Eq. (13) wrong by $8\pi$, inverting the $\mathcal O_4/\mathcal O_5$ ordering;
(2) O1 $\equiv$ O6 as defined, making the first null-space relation a tautology and the
"six-member rank-four" claim partly presentational; (3) barrier catalog unsourced and
underived in 12 of 14 entries; (4) the target claim (Popławski's torsion cosmological
constant) never analysed; (5) B7 contradicts B12 on the uniqueness of $\gamma$ and its
cross-reference is empty; (6) Route 3's propagation to "61–67 orders" is a black box;
(7) the NJL no-condensate result is asserted, its derivation deferred to a non-refereed
deposit.

**R1 closure verification:** 15 of 19 canonical items **closed and verified**, 2 **closed with
a defect** (DP1N-03 wording, DP1N-15 label), 2 **partial** (DP1N-06 evaluability, DP1N-08
bibliography), **0 not closed**, plus DP1N-20 partial. Of the three regressions, **2 restored
faithfully** (DP1N-01, DP1N-02 — both independently re-verified against P1C v1C.0.16 *and*
against the underlying algebra), **1 restored with an introduced wording error** (DP1N-03,
MINOR 1). The single READING-I normalization **is** used consistently everywhere — verified by
grep and by re-deriving $\mathcal O_5$ from the paper's own $\alpha$. The Popławski sentence
**is** at exact evidential strength in all five places it appears.

**Verdict: major-revisions.**

The science is sound and the scoping is unusually honest; the no-go conclusion survives every
finding above. What blocks acceptance is that the paper's central contribution — the
fourteen-barrier catalog — is not yet evaluable from the manuscript and the public literature,
that it does not engage the published claim it refutes, and that one displayed equation is
wrong by $8\pi$. All seven MAJORs are addressable within ~4 pp of added content and a set of
targeted corrections; none requires new physics or weakens the result. I would expect to
recommend acceptance on a revised version that closes them.
