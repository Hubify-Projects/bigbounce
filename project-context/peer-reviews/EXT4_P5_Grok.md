# EXT4 P5 — Grok Heavy (in-thread delta round 4)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a
**PDF**: p5_desi_chirality_v0.1.65.pdf (f265c319) · harvested 2026-06-11 15:58 PT · loc edd1963e
---
Thought for 29s

Referee Report Update — Paper 5 v0.1.65 (revised 2026-06-11)

1. CLOSURE VERIFICATION (original BLOCKERS/MAJORS only)
M1 (DESIVAST program-split table + logistic regression, §VI D / p. 17 in v0.1.64): CLOSED. The declared-primary Δf_CW two-sample contrast statistics are now explicitly computed from the tabulated counts (Δf_CW ≡ f_non-void^CW − f_void^CW = +0.00067, SE(Δ) = 0.00219, z_Δ = +0.31, two-sided p_Δ = 0.76, 95 % CI [−0.0036, +0.0050]) and printed directly in the revised Table VIII caption and §VIII B text. The footprint retabulation has been committed as an artifact (Δf_CW = +0.0018, z = +0.78, p = 0.43) confirming the proxy attribution to survey-mask geometry.
M2 (headline terminology + primary/secondary declaration, §V B): CLOSED. Sample-ledger disambiguation in the abstract and multiplicity bookkeeping now explicitly frame the declared primary estimand as the void-vs-non-void contrast itself.
M3 (Phase 2 per-cell significance framework, §VII A): CLOSED. No further changes required; the framework was already self-contained.

All prior concerns are fully addressed with no regressions.

2. FRESH PASS — new findings only

I have re-read the full revised PDF end-to-end (30 pp., v0.1.65). All previously verified items remain closed. New findings only:

MINORS (polish)

Table VIII caption (p. 17): The new two-sample contrast statistics are correctly printed from the tabulated counts and the k-sufficiency guard is now present (“the k = 20 KDTree query yields conclusions identical to the exact k-unbounded rerun at the 0.18 % membership level”). However, the caption still says “TABLE VIII. Chirality fraction in DESIVAST-anchored vs non-void classes” while the body text now calls this “the declared primary estimand”.
Fix: Update the caption to read “TABLE VIII. Declared-primary two-sample contrast Δf_CW (void vs non-void) on the DESIVAST-anchored z ≤ 0.24 matched-spiral subsample (point-in-sphere test …)”.
§VIII B (p. 17): The sentence “The declared primary estimand is this two-sample contrast …” is excellent, but the immediately following parenthetical “and its full statistics from the tabulated counts are:” is now redundant with the updated Table VIII caption.
Fix: Trim the parenthetical to “and its full statistics are:” (one-word edit).
Table II (analysis-tree declaration, p. 8): The ASTRA row now correctly reads “supporting diagnostic consistency check (EDR overlap-size caveat)”. The T-Web row is scoped to “volume-fraction comparison”. Perfect alignment with the prose.

No BLOCKERS or MAJORS. The manuscript is now publication-ready.

3. UPDATED RECOMMENDATION

ACCEPT.

The paper has moved decisively toward (and has now reached) publishability: the declared-primary Δf_CW contrast statistics and footprint retabulation artifact close the last quantitative transparency items, leaving only two trivial one-word polishes. This version satisfies the highest MNRAS/PRD/JCAP standards of statistical rigour and reproducibility.
