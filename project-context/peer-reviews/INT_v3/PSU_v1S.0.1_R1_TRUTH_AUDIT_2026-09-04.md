# PSU v1S.0.1 — R1 truth audit (2026-09-04)

**Auditor stance**: skeptical, verdict-first, told no expected outcome. Patterns 061–066 +
directive H-refined. Every dismissal below carries a source citation checked against the
committed artifact; no finding is dispositioned "non-real" on assertion.

**Exact artifact**: `arxiv/paper_su_criterion/main.pdf` == `site/public/papers/paper_su_criterion_v1S.0.1.pdf`,
sha256 `cc0dfb84a232967c45ea359d5de18f642af0727c2907512b289931854ed7c48e`, 4 pp.
Text checked against `arxiv/paper_su_criterion/main.tex` at HEAD.

**Sources of truth consulted** (committed, read directly):
- `research/theory_audit/separate_universe_failure_criterion_2026_09_04.{md,py,json}`
- `research/theory_audit/threading_map_second_order_2026_09_04.{md,py,json}`
- `research/theory_audit/fnl_monopole_adjudication_2026_09_03.md`
- `research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.md`
- own sympy re-derivations (recorded inline below)

**Classes**: (a) GENUINELY-NEW REAL · (b) RE-FLAG of an already-dispositioned item ·
(c) FALSIFIED against the committed source · (d) OPINION / genre / venue ·
(e) OUT-OF-SCOPE, honestly disclosed.
This is the paper's FIRST board, so class (b) is empty by construction; items land in (a), (c),
(d) or (e).

## Plan (executed below)

1. Fingerprint every finding from all three legs; merge duplicates into canonical PSU-#N items.
2. Adjudicate the five Fable MAJORs against the theory-audit notes first (they are the
   load-bearing physics), then the Grok and Gemini items against the same sources.
3. Emit per-class counts per leg.
4. Emit the two-part CLOSURE PLAN: (i) editorial / real edits for v1S.0.2 with exact lines,
   (ii) SCIENCE items requiring a derivation before the note may claim them.
5. Write `project-context/peer-reviews/DISPOSITIONS/PSU.md`.

## Own re-derivations (sympy, run 2026-09-04)

With `λ=1-ε/3`, `f_in-in = (5/12)(ε²μ²-ε²+6ε-12)` (SU note §2.2 / Table, line 168) and the
paper's Eq. (3) `f_map = -(5ε/4)(1-μ²)`:

| expression | symbolic result | at ε=3/2 |
|---|---|---|
| `f_in-in/λ + f_map` (paper's composition) | `15(-εμ²-ε+4)/(4(ε-3))` | `-25/4 + (15/4)μ²` |
| `f_in-in/λ² - f_map/λ` (Gemini's proposed fix) | `15(2ε²μ²-2ε²-3εμ²+9ε-12)/(4(ε-3)²)` | `-5` |
| `f_in-in` monopole at ε=3/2 | — | `-15/8` |

These three lines decide items PSU-1, PSU-3 and the Gemini fix below.

## Canonical findings

Legend: **class** (a) genuinely-new real · (c) falsified · (d) opinion/genre/venue ·
(e) out-of-scope, disclosed. "Legs" lists which reviewers raised the item.

### PSU-1 — the second-order composition returns the FINAL-position-label value, Table I prints the INITIAL-label value
**Legs**: Grok M6 · Gemini F1 (ESSENTIAL) · Fable M2. **Class (a) GENUINELY-NEW REAL.**
All three legs independently substituted the dust case and got a μ²-dependent number where
Table I prints the isotropic −5. My sympy confirms `f_in-in/λ + f_map = -25/4 + (15/4)μ²`.
**Verdict citation**: `threading_map_second_order_2026_09_04.md` §3 "Totals" (l. 102–103) —
"Final-position label: f_map = −5ε/4 + 5ε/4 μ² … Initial-position label (the separate-universe
label): monopole again −5ε/6; the quadrupole changes by the translation term only" — and §4
Eq. (4) (l. 115–119), which prints exactly `−25/4 + (15/4)μ²` as the **final**-label value at
ε=3/2 and −5 as the **initial**-label value. The paper's Eq. (3) is therefore the final-label
f_map; Table I's −5 is the initial-label f_δN; the note composes them without saying so.
The equation is not "wrong" — the two sides carry different worldline labels, and the paper
never defines the label. The referees are right that as printed the note's own numbers refute
its own equation.
**Gemini's proposed fix is FALSIFIED**: `f_in-in = λ²f_δN + λf_map` reproduces −5 only at
ε=3/2 (see table above); at symbolic ε it does not return the label-independent −5 that
`threading_map_second_order` §4 establishes "exactly, isotropic, for every constant ε".
Do not adopt it. **Closure**: SCIENCE item S1.

### PSU-2 — Fig. 1 caption "Both vanish at w=−1" is false for λ
**Legs**: Grok M5 (pass-2) · Gemini B1 (pass-2). **Class (a) REAL.** λ(−1)=(1−(−1))/2=1.
`main.tex` l. 141–142 caption vs. the correct body sentence at l. 135–137 ("λ→1, f_map→0 at
w=−1"). Body right, caption wrong. **Closure**: editorial E1.

### PSU-3 — the headline 8/3 is not derivable from anything printed in the body
**Legs**: Grok E1, E6 · Fable m1. **Class (a) REAL (traceability).**
The factor itself is CORRECT: `separate_universe_failure_criterion_2026_09_04.md` l. 179 —
"5ε(9−ε)/18 in the monopole — 25/8 at ε=3/2, i.e. a factor 8/3 in f_NL"; equivalently
(−5)/(−15/8)=8/3. But −15/8 (the angle-averaged in-in monopole) appears nowhere in the paper.
**Grok's counter-arithmetic is FALSIFIED**: his "16/7" divides by −35/16, the constant term of
the μ-resolved kernel, not by the monopole −15/8 (my sympy: monopole at ε=3/2 = −15/8).
**Closure**: editorial E3 — print the monopole in Table I and state the ratio once.

### PSU-4 — Cai, Xue, Brandenberger & Zhang (2009) is neither cited nor reconciled
**Legs**: Fable M1 (+Q2). **Class (a) REAL as a citation and robustness-statement gap; the
physics threat is FALSIFIED.**
**Verdict citation**: `fnl_matter_contraction_adjudication_2026_09_02.md` l. 26 — "−35/16
(Li et al. 2016 Eq. 5.1 at c_s=1; BigBounce Paper 2). Cai et al. 2009's −35/8 is exactly a
factor 2 too large" — and l. 32/101: Cai's shape function Eq. (37) is reproduced monomial by
monomial; all three of their quoted amplitudes are uniformly 2× the from-scratch values; the
slip is located in their amplitude step (their Eqs. 38–40), "not in any vertex, not in
Wick/commutator bookkeeping". So the lab's input stands and is independently derived twice.
**But the dependence is real and load-bearing**: if Cai's −35/8 were the monopole, the gap
would be −5−(−35/8) = **−5/8** and the factor **8/7 ≈ 1.14** — the O(1) headline would collapse
to a ~14% effect. A PRD referee must be told this in the paper, not in a repo note.
**Closure**: editorial E4 (cite + state the ×2 location + state the dependence).

### PSU-5 — load-bearing derivations exist only in unpublished self-cited GitHub markdown
**Legs**: Grok E3, E7 · Gemini F2 (ESSENTIAL). **Class (a) REAL.** Refs [18] `Golden2026Monopole`
and [19] `Golden2026Threading` supply the in-in kernel, the −5, and the whole second-order map;
none is derived in the 4-page note. This is a hard PRD standalone-reader failure, not a matter
of taste. **Closure**: SCIENCE/packaging item S4.

### PSU-6 — internal audit strings rendered into the PDF
**Legs**: Grok E5 · Gemini F4 · Fable m7 (same lines, line-break complaint).
**Class (a) REAL, editorial.** `main.tex` §III l. ~184 "(script:
\texttt{separate\_uni\-verse\_failure\_criterion\_2026\_09\_04.py}, exact sympy)" and the
reproducibility statement's `reproducibility/manifests/experiments/lift2-…json`. Both break
mid-token in the rendered two-column PDF. **Closure**: editorial E2.

### PSU-7 — Table I column header says "the in-in monopole" but the dust entry is angle-dependent
**Legs**: Gemini F3. **Class (a) REAL.** `main.tex` Table I caption l. ~168 vs the dust entry
`−35/16 + (15/16)μ²`. The actual monopole is −15/8 (my sympy). Same fix as PSU-3.
**Closure**: editorial E3.

### PSU-8 — the δN_c ↔ separate-universe δN identification is asserted, and "initial-position label" is never defined
**Legs**: Fable M3 (+Q1). **Class (a) REAL.** The paper's §II carries the identification in one
sentence ("The zero-shift threading computed by the separate universe is the fluid (normal)
congruence") and Table I tags the −5 "(initial-position label)" with no definition anywhere.
**Verdict citation**: the lab notes DO derive it — `threading_map_second_order` §3 row
`lab_init` (+`wl_initextra`), "rigid translation x_f → x_i (initial-position label)", and
`separate_universe_failure_criterion` l. 133 (lane (B)'s N(φ,π) ODE system gives −5) — so the
content is real; it is the paper that is silent. After PSU-1 the label is load-bearing, so this
is no longer a minor omission. **Closure**: SCIENCE item S1 + packaging S4.

### PSU-9 — "exact for any history" drops the horizon-crossing gradient term, and ⟨X⟩_ζ is 0/0 on two Table I rows
**Legs**: Fable M4 (+Q5). **Class (a) REAL.** The super-Hubble reduction is
`∂_iN^i = −(1/a²H)∇²ζ + (ε/c_s²)ζ̇`; the paper's Eq. (2) keeps only the second term while the
integral in Eq. (1) runs from t=−∞ with ζ_L(−∞)=0, i.e. through horizon crossing where the
dropped term is not negligible. Worse, with the normalization `⟨X⟩_ζ = ∫X dζ_L / ζ_L(t_f)` and
ζ̇_L=0, the attractor and ekpyrosis rows of Table I are literally 0/0. Neither committed source
note defines the initial slice (checked: no such definition in either `.md`). This is a genuine
definitional defect in the note's central linear claim. **Closure**: SCIENCE item S2.

### PSU-10 — "failure" framing contradicts the committed source note's own conclusion
**Legs**: Fable M5. **Class (a) REAL — the most serious framing item on the board.**
The paper's title and abstract assert a failure ("fails by a factor of 8/3", "a second,
independent failure mode"). **Verdict citation**: `threading_map_second_order_2026_09_04.md`
§4 l. 120–122 — "the two methods agree exactly once the variable is matched; **there was never
a discrepancy in the physics, only in the variable**." An explicit, exact, invertible map is a
change of variable, not a failure. The paper must either supply the argument that δN_c is the
wrong variable for the contraction-to-expansion observable, or reframe. Directive R6
(claims stated at exactly their evidential strength) applies. **Closure**: SCIENCE/decision S3.

### PSU-11 — the NLO gradient-expansion literature is missing from §IV
**Legs**: Fable M6. **Class (a) REAL.** The −(1/3)∂_iN^i term in the local expansion is the
standard next-to-leading gradient-expansion term; the genuine novelty is that it is O(k⁰) when
ζ grows with ε=O(1). Papers to add (Fable's own integrity note says these are from reviewer
memory and MUST be confirmed before citing): Takamizu, Mukohyama, Kobayashi & Tanaka,
JCAP 1006:019, arXiv:1004.1870; Naruko, Takamizu & Sasaki, JCAP 1304:037, arXiv:1210.6525.
Already cited and adjacent: Lyth–Malik–Sasaki, Salopek–Bond, Artigas–Grain–Vennin [11].
**Closure**: SCIENCE/lit item S5.

### PSU-12 — "the criterion is just a restatement of the known initial-data requirement"
**Legs**: Grok M1. **Class (c) FALSIFIED.** `main.tex` §III states the two requirements as
logically distinct: "(i) N(φ,π), to capture the growing mode as an independent initial
datum~\cite{Namjoo2013}; (ii) ⟨ε/c_s²⟩_ζ→0, so that the threading map is the identity", and
gives the mechanism by which USR satisfies (ii) while (i) is maximal. Refs [3,4]
(Namjoo2013, Chen2013) contain no ⟨ε/c_s²⟩_ζ criterion. Fable's independent M6 reaches the
same structural conclusion from the opposite direction (the term is a known NLO object). The
residual — that the novelty is narrower than "second independent failure mode" — is real and
is tracked as PSU-11, not here.

### PSU-13 — "USR validation uses ε∝a⁻⁶, violating the constant-ε assumption"
**Legs**: Grok M3. **Class (e) OUT-OF-SCOPE, HONESTLY DISCLOSED.** `main.tex` §V (Limits):
"The USR second-order statement in Sec. III is structural …, not a re-solve with a
time-dependent ε(t)=ε_s(a/a_s)⁻⁶; a full time-dependent-ε second-order calculation was not
attempted." Grok read §III without §V. Not an internal inconsistency.

### PSU-14 — Fig. 1 presents two curves on two ordinates with no units/normalization stated
**Legs**: Grok M2, N4. **Class (a) REAL, minor presentational.** Both quantities are
dimensionless; the caption never says so and never defines the right-hand scale.
**Closure**: editorial E5.

### PSU-15 — "no new observable prediction; three of four validations are known results"
**Legs**: Grok M4. **Class (d) OPINION / genre / venue.** A validation table is supposed to
reproduce known results; the note nowhere claims the four cases are new. This is a
significance judgment about a PRD Letter, not a defect. It does, however, share a root with
PSU-10 (what is actually being claimed), which IS actionable — tracked there.

### PSU-16 — no frozen DOI / archival release for the cited scripts and JSON
**Legs**: Grok E4 (first half). **Class (a) REAL.** No Zenodo (or equivalent) deposit exists
for `research/theory_audit/*_2026_09_04.{py,json}`; the paper cites live repo paths.
**Closure**: editorial/packaging E9.

### PSU-17 — "future date September 4, 2026"; "no institutional address"; "self-citations post-date the submission window"
**Legs**: Grok N1, N2, N3. **Class (c) FALSIFIED, single root cause.** The reviewer assumed a
past submission window. `\paperTimestamp` is today's date (2026-09-04) and the cited 2026-09
notes are contemporaneous, not future-dated. On N2: `main.tex` carries `\email{houston@hubify.com}`,
an ORCID `\altaffiliation`, and `\affiliation{Independent Researcher, Los Angeles, California, USA}`
— PRD accepts exactly this. No action.

### PSU-18 — "the 'exact threading identity' is not exact once ε=O(1)"
**Legs**: Grok E2. **Class (c) FALSIFIED as stated.** The abstract already separates the two
exactness claims: "The linear result is exact for any history; the second-order result is exact
at constant ε, c_s=1, with a closed general equation-of-state form." Eq. (1) is a nonlinear
identity along the worldline; ε=O(1) does not touch it. The REAL residual in the neighbourhood
of this complaint is the dropped gradient term, tracked as PSU-9 — not the ε-dependence Grok
names.

### PSU-19 — "'at w=1 the in-in monopole itself vanishes' is unsupported"
**Legs**: Fable m2. **Class (c) FALSIFIED, with an editorial residual.**
**Verdict citation**: the general-ε in-in monopole in
`separate_universe_failure_criterion_2026_09_04.md` l. 123 / `threading_map` §4 is
`−5(ε−3)(ε−6)/18`, which vanishes at ε=3, i.e. w=1. The claim is derived, but the formula that
makes it checkable is not printed in the paper. **Closure**: editorial E6 (print the general-ε
monopole).

### PSU-20 — λ_USR assumes ζ∝a³ from ζ=0 at a_s
**Legs**: Fable m3. **Class (a) REAL, minor.** In a slow-roll→USR transition ζ_L(a_s) is the
frozen slow-roll value, not zero. State the pure-USR / a³-mode-dominance assumption.
**Closure**: editorial E7.

### PSU-21 — the ekpyrosis row tests the definition, not the criterion
**Legs**: Fable m5. **Class (a) REAL, minor.** With ζ̇=0 the criterion is trivially satisfied.
Mark the row a consistency check, or add the two-field/entropic case where ζ is sourced on
super-Hubble scales. **Closure**: editorial E7.

### PSU-22 — "every one of the five geometric contributions carries a factor ε" — the five are never listed
**Legs**: Fable m6. **Class (a) REAL, minor.** They exist and are auditable:
`threading_map_second_order_2026_09_04.md` §3 table — `zlap`, `psi2`, `grad`, `wl_fin`,
`lab_init` (+`wl_initextra`). One footnote closes it. **Closure**: editorial E7.

### PSU-23 — reference style; [18]/[19] presented as citable works
**Legs**: Fable m8. **Class (a) REAL, minor.** Label them unpublished notes with commit hashes;
give Ref. [12] its full author list and journal. **Closure**: editorial E8.

### PSU-24 — the AI-usage disclosure overclaims what the scripts verify
**Legs**: Fable m9. **Class (a) REAL, minor.** Scripts verify algebra, not the δN_c ↔ δN
identification (PSU-8). Rephrase. **Closure**: editorial E8.

### PSU-25 — notation: ⟨ε⟩_ζ vs ⟨ε/c_s²⟩_ζ; Θ defined only in passing
**Legs**: Fable m10. **Class (a) REAL, minor.** **Closure**: editorial E8.

### PSU-26 — Eq. (2) is claimed "for any c_s" without naming the matter class
**Legs**: Fable Q4. **Class (a) REAL.** `∂_iN^i=(ε/c_s²)ζ̇` follows from the P(X) momentum
constraint; a genuine fluid with non-adiabatic pressure adds a term. §V discloses the c_s≠1
limitation for the SECOND-order map only; the linear claim is unqualified.
**Closure**: editorial E10 (state the P(X) class).

### PSU-27 — "USR: agree to O(ε)" is a statement about the map, not a test against NFS
**Legs**: Fable m4. **Class (a) REAL, minor.** NFS's 5/2 is itself leading order in ε, so the
row cannot constrain the O(ε) correction; it currently reads as if it does.
**Closure**: editorial E7.

### PSU-28 — "future-dated filenames and commit hashes"
**Legs**: Grok E4 (second half). **Class (c) FALSIFIED.** Same root cause as PSU-17.

## Per-class counts

| leg | verdict word (raw) | findings | (a) real | (b) re-flag | (c) falsified | (d) opinion | (e) oos-disclosed |
|---|---|---|---|---|---|---|---|
| Claude Fable 5.1 (INT) | major-revisions | 16 (+5 Q) | 15 (+1 from Q4) | 0 | 1 | 0 | 0 |
| Grok brutal (API) | REJECT | 17 | 10 | 0 | 5 | 1 | 1 |
| Gemini cosmology (API) | MAJOR REVISIONS | 5 | 5 | 0 | 0 | 0 | 0 |
| **canonical, de-duplicated** | — | **28** | **21** | **0** | **5** | **1** | **1** |

Class (b) is empty by construction: this is the paper's first board.
**21 genuinely-new real findings.** Under directive K this is wave 0 for `paper-su`; the
clean-wave clock cannot start until the (a) items are closed and the note re-tested.

## CLOSURE PLAN

### (i) Editorial / real edits for v1S.0.2 — exact locations in `arxiv/paper_su_criterion/main.tex`

| id | items | edit |
|---|---|---|
| E1 | PSU-2 | Fig. 1 caption, l. 141–142: replace "Both vanish at $w=-1$ (attractor limit)" with "At $w=-1$ (attractor limit, $\eps=0$) $f_{\rm map}^{\rm mono}$ vanishes and $\lambda\to1$, so the map is the identity". |
| E2 | PSU-6 | §III l. ~184: delete "(script: \texttt{separate\_uni\-verse\_...py}, exact sympy)". Reproducibility statement: delete the inline manifest path. Move both into one data-availability footnote using `\url{}`. |
| E3 | PSU-3, PSU-7 | Table I (l. ~166–176): rename the column to $f^{\rm in\text{-}in}(\mu)$ and add a column $f^{\rm in\text{-}in}_{\rm mono}$ with $-15/8$ for the dust row. In §III add one sentence: "the monopole gap is $-5-(-15/8)=-25/8$, a factor $8/3$." |
| E4 | PSU-4 | §I, immediately after `\cite{Golden2026Monopole}` (l. ~85): cite Cai, Xue, Brandenberger & Zhang, JCAP 0905:011 (arXiv:0903.0631); state that their squeezed $-35/8$ is uniformly $2\times$ the from-scratch value, that their shape function (their Eq. 37) is reproduced monomial-by-monomial and the $\times2$ sits in their amplitude step (their Eqs. 38–40), and that $-35/16$ agrees with Li, Quintin, Wang & Cai (2016) Eq. (5.1) at $c_s=1$. Add the dependence sentence: "were the monopole $-35/8$, the gap would be $-5/8$ and the factor $8/7$; the $O(1)$ claim rests on $-35/16$." |
| E5 | PSU-14 | Fig. 1 caption: state that both ordinates are dimensionless and give the right-axis normalization. |
| E6 | PSU-19 | §II: print the general-$\eps$ in-in monopole $-5(\eps-3)(\eps-6)/18$ so the $w=1$ vanishing is checkable in-paper. |
| E7 | PSU-20, PSU-21, PSU-22, PSU-27 | §II: state the pure-USR / $\zeta\propto a^3$ assumption behind $\lambda_{\rm USR}$. Table I: mark the ekpyrosis row a consistency check; reword the USR row so it does not read as an NFS-constrained test. Footnote listing the five geometric pieces (`zlap`, `psi2`, `grad`, `wl_fin`, `lab_init`). |
| E8 | PSU-23, PSU-24, PSU-25 | Bibliography: full author list + JCAP 2024 for Ref. [12]; label [18]/[19] unpublished notes with commit hashes. Rephrase the AI-usage disclosure (scripts verify algebra, not the identification). Unify $\langle\eps/c_s^2\rangle_\zeta$ notation; define $\Theta$ where introduced. |
| E9 | PSU-16 | Mint a Zenodo deposit for `research/theory_audit/*_2026_09_0{3,4}.{py,json,md}` and cite the DOI. |
| E10 | PSU-26 | §II: state that Eq. (2) holds for the $P(X)$ class; a genuine fluid with non-adiabatic pressure adds a term. |

E1–E3, E5–E8, E10 are pure text and can land in one v1S.0.2 bundle under directive G
(bump `\paperVersion`+`\paperTimestamp`, recompile 0 undef-refs, `/latex-audit`, re-mirror
byte-identical to all served paths). E4 and E9 need the Cai reconciliation sentence and the
DOI respectively, but no new computation. **None of E1–E10 closes the board.**

### (ii) SCIENCE items — a derivation is required before the note may claim these

| id | items | computation required | tier |
|---|---|---|---|
| **S1** | PSU-1, PSU-8 | **Label-resolved second-order composition.** Re-run `threading_map_second_order_2026_09_04.py` §3 with BOTH worldline labels and export the initial-position-label $f_{\rm map}^{\rm init}(\eps,\mu)$ in closed form (the final-label total $-\tfrac{5\eps}{4}(1-\mu^2)$ is what the paper currently prints). Verify symbolically that $f^{\rm in\text{-}in}/\lambda + f_{\rm map}^{\rm init} = -5$ for every constant $\eps$, and that the monopole is label-independent at $-5\eps/6$. Then define "initial-position label" in the paper and print both totals. | **Fable** — contested: three referees derived a contradiction from the printed numbers, and Gemini proposed a composition that fits only at $\eps=3/2$. |
| **S2** | PSU-9 | **Normalization of $\langle X\rangle_\zeta$ and the dropped gradient term.** Derive the super-Hubble reduction keeping $-(1/a^2H)\nabla^2\zeta$; bound its worldline integral as $O(k^2/a^2H^2)$ from a super-Hubble initial slice $t_i$; redefine $\langle X\rangle_\zeta=\int X\,d\zeta_L/[\zeta_L(t_f)-\zeta_L(t_i)]$; restate the attractor and ekpyrosis rows under that definition (they are currently $0/0$). Decide whether "exact for any history" survives or becomes "exact on super-Hubble scales for any history". | **Fable** — it decides the survival of the note's central linear claim. |
| **S3** | PSU-10, PSU-15 | **Failure vs change-of-variable adjudication.** Written argument for which variable is physical for the contraction-to-expansion observable, reconciled against `threading_map_second_order` §4's own "there was never a discrepancy in the physics, only in the variable". Outcome is either a supplied argument that $\delta N_c$ is the wrong variable, or a retitle/reframe as a threading map with a quantified $\delta N$-usage caveat. | **Fable + Houston decision** (directive R6: claims at exactly their evidential strength; a retitle is a lineup change under R3). |
| **S4** | PSU-5, PSU-8 | **Self-containedness.** Reproduce in an appendix (a) the in-in $-35/16+(15/16)\mu^2$ kernel and (b) the second-order map derivation — or post the two companion notes as an arXiv preprint and cite that. No contested math once S1 lands. | **sonnet** (packaging), gated on S1. |
| **S5** | PSU-11 | **Literature positioning.** Confirm that Takamizu–Mukohyama–Kobayashi–Tanaka (arXiv:1004.1870) and Naruko–Takamizu–Sasaki (arXiv:1210.6525) carry the NLO gradient term as claimed, then rewrite §IV as "the known NLO term is LO in a non-attractor contraction". Fable's integrity note flags both refs as from memory — do not cite unverified. | **opus** (literature verification). |

**Ordering**: S1 → S2 → S3 gate the paper's claims; E1–E10 can land in parallel but must not be
presented as closing the board. S4 and S5 follow S1/S3. Directive R2 applies: no further review
round on `paper-su` until at least S1 and S3 have produced a science or scope decision.
