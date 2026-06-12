# EXT5 P5 — Grok Heavy (in-thread delta round 5)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a
**PDF**: p5_desi_chirality_v0.1.67.pdf · harvested 2026-06-12 00:50 PT
---
Thought for 15s

Referee Report Update — Paper 5 v0.1.67 (revised 2026-06-11)

1. CLOSURE VERIFICATION (original BLOCKERS/MAJORS only)
M1 (DESIVAST program-split table + logistic regression, §VI D / p. 17 in v0.1.64): CLOSED. The declared-primary Δf_CW two-sample contrast statistics are now explicitly computed from the tabulated counts and printed for all five Bonferroni-5 estimators (three sphere-PIS rows in Table X; two GALZONE catalog-native rows in §VIII D with V2-REVOLVER zΔ = −1.25, pΔ = 0.21 and V2-VIDE zΔ = +0.72, pΔ = 0.47). The footprint retabulation remains committed as a clean null (Δf_CW = +0.0018, z = +0.78, p = 0.43).
M2 (headline terminology + primary/secondary declaration, §V B): CLOSED. Sample-ledger disambiguation, multiplicity bookkeeping, and the declared primary estimand (void-vs-non-void contrast) are now fully coherent across the five-row family; the abstract regression has been fixed to “|∆f_CW| ≤ 0.004 across all five void definitions”.
M3 (Phase 2 per-cell significance framework, §VII A): CLOSED. No changes required; the framework was already self-contained and is untouched.

All prior concerns are fully addressed with no regressions. The internal R34conf audit (42 further items) and the added 4×2 contingency appendix plus h⁻¹ Mpc derivation footnote are welcome but outside the scope of my original report.

2. FRESH PASS — new findings only

I have re-read the full revised PDF end-to-end (31 pp., v0.1.67). All previously verified items remain closed. New findings only:

MINORS (polish)

Table VIII caption (p. 17): The k-sufficiency guard is now present and accurate (“the k = 20 KDTree query yields conclusions identical to the exact k-unbounded rerun at the 0.18 % membership level”). However, the caption still reads “TABLE VIII. Chirality fraction in DESIVAST-anchored vs non-void classes” while the body text now calls this “the declared primary estimand”.
Fix: Update the caption to read “TABLE VIII. Declared-primary two-sample contrast Δf_CW (void vs non-void) on the DESIVAST-anchored z ≤ 0.24 matched-spiral subsample (point-in-sphere test …)”.
§VIII D (catalog-native V2 membership cross-check, p. 18): The new two-sample contrasts for the GALZONE rows are correctly tabulated and tied to the Bonferroni-5 family. One minor formatting inconsistency: the non-void complement is defined parenthetically but the exact row counts for the complement (n_non-void = 40,877 for V2-REVOLVER; 71,678 for V2-VIDE) appear only in the pipeline artifact, not in the prose.
Fix: Add the explicit complement counts to the paragraph (one sentence) so readers do not need to consult the artifact for the full 5-row family arithmetic.

No BLOCKERS or MAJORS. The manuscript is now publication-ready at the level of a final proofs check.

3. UPDATED RECOMMENDATION

ACCEPT.

The paper has moved decisively toward (and has now reached) full publishability: the estimand-family coherence across all five Bonferroni-5 rows plus the abstract regression fix eliminate the last quantitative transparency items. This version satisfies the highest MNRAS/PRD/JCAP standards of statistical rigour and reproducibility.
