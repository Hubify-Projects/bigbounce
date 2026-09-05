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
