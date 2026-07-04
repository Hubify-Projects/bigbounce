# P2 value-headlining integrity fix — 2026-07-03 (v1.7.86 → v1.7.87)

## Finding (verified re-test, Grok #1 MAJOR)
> "Adopting the Li value halves every quoted significance, YET the abstract continues
> to promote the Cai value."

The paper headlined the optimistic **Cai** f_NL = −35/8 significances (bispectrum-only
5.2–5.5σ; realistic 2.6–5.5σ) as **the** takeaway, while the conservative **Li** −35/16
halves every significance (to ~1.3–2.75σ) and the Cai/Li factor-of-2 is unresolved.
Headlining the more-favorable value while a factor-of-2 is open violates **integrity
directive F** ("papers don't headline the more-favorable of multiple values").

## Fix (honest reframe — NO number changed, NO fabrication)
Both values and the linear significance scaling were already in the paper (final abstract
paragraph + Conclusion + Appendix A). The fix foregrounds the honest **amplitude-conditional
Li–Cai range** wherever a single favorable value led the reader's takeaway:

1. **Abstract, headline-forecast sentence (para 4).** Was: "We adopt the bispectrum-only
   5.2–5.5σ optimistic and 2.6–5.5σ realistic ranges as the headline forecast." Now leads
   with `f_NL^local ∈ [−35/16, −35/8] (Li–Cai)`: bispectrum-only **2.6–5.5σ** (Li lower
   endpoint → Cai upper endpoint) and realistic post-budget **1.3–5.5σ**, lower bound
   reflecting conservative Li, upper reflecting optimistic Cai. Explicitly states we do
   **not** headline the Cai-only 5.2–5.5 / 2.6–5.5 alone while the factor-of-2 is open
   (Cai = upper edge / fiducial input; Li = genuine downward robustness branch).

2. **Abstract, null-forecast sentence.** Exclusion now quoted as **~1.3–5.5σ** across the
   Li–Cai amplitude range (was Cai-only ~2.6–5.5σ).

3. **Conclusion.** "SPHEREx can test this prediction at …" now leads with the realistic
   **1.3–5.5σ** amplitude-conditional Li–Cai range; the Cai-input 5.2–5.5σ optimistic is
   demoted to "the Cai-input case reaches 5.2–5.5σ optimistically."

**Retained as-is (honest, not headline promotion):** the abstract's earlier *derivation*
sentence ("after template-mismatch correction we obtain bispectrum-only 5.2–5.5σ at
f_NL = −35/8 … reducing to a realistic 2.6–5.5σ") is legitimate computation at the adopted
Cai fiducial. Body forecast/systematics/discussion sections compute at the adopted Cai
fiducial with the Li robustness branch + factor-of-2 disclosure carried throughout — that
is disclosed computation, not favorable-value headlining.

## What this does and does NOT do
- **Does:** removes Grok's specific value-headlining complaint; the conservative/range now
  leads the reader's takeaway in the abstract and conclusion.
- **Does NOT:** resolve the factor-of-2 MAJOR. The reviewers want the Cai/Li discrepancy
  **resolved**, which requires a full four-vertex in-in re-derivation across an explicit
  bounce (our stated #1 follow-up). This fix does not claim resolution and will not lift
  that MAJOR. Stated honestly.

## Directive-G hygiene
- Recompiled 4-pass (pdflatex + bibtex): **0 undefined refs/citations, 0 overfull hboxes >5pt.**
- Pages: **31.** New PDF md5: **c36426aa22a52c0c330ba641d84a348d**, sizeBytes 959477.
- Mirrored byte-identical to all 15 served paths (public/papers, site/public/papers,
  site/public, public + versioned v1.7.87 aliases); three-way md5 match verified.
- Page 1 renders new date "July 3, 2026" and the amplitude-conditional Li–Cai abstract
  framing; no column overflow.
- Convex `paperVersions:bump` paper-2 → v1.7.87, datestamp July 3 2026, real md5/pages.

NO fabrication. NO number changed.
