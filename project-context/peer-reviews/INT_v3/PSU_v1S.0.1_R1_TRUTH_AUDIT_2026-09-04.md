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
