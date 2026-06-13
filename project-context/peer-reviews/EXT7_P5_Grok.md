# EXT7 P5 — Grok Heavy (in-thread delta round 7; Gemini = fresh thread)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=edd1963e-cc7e-4a86-b288-1a7834c9e45a
**PDF**: p5_desi_chirality_v0.1.71.pdf (d2b33c8a376f93b8) · harvested 2026-06-13 ~03:26 PT
---

Referee Report Update — Paper 5 v0.1.71 (revised 2026-06-13)

1. CLOSURE VERIFICATION (original BLOCKERS/MAJORS only)
M1 (DESIVAST program-split table + logistic regression, §VI D / p. 17 in v0.1.64): CLOSED. The declared-primary Δf_CW two-sample contrast statistics are now explicitly computed from the tabulated counts and printed for all five Bonferroni-5 estimators (three sphere-PIS rows in Table X; two GALZONE catalog-native rows in §VIII D with V2-REVOLVER zΔ = −1.25, pΔ = 0.21 and V2-VIDE zΔ = +0.72, pΔ = 0.47). The footprint retabulation remains committed as a clean null (Δf_CW = +0.0018, z = +0.78, p = 0.43).
M2 (headline terminology + primary/secondary declaration, §V B): CLOSED. Sample-ledger disambiguation, multiplicity bookkeeping, and the declared primary estimand (void-vs-non-void contrast) are now fully coherent across the five-row family; the abstract regression has been fixed to “|∆f_CW| ≤ 0.004 across all five void definitions”.
M3 (Phase 2 per-cell significance framework, §VII A): CLOSED. No changes required; the framework was already self-contained and is untouched.

All prior concerns are fully addressed with no regressions. The R36conf 4-vendor audit, the Table X cell-count fix (now 126,202 matching the committed f_CW arithmetic), Fig 3 regeneration, Tab XV σ column, R_s=10 global-max update, ±4.8 pp floor rewrite, bright/dark z=1.95 correction, and struck RSD sentence are all welcome but outside the scope of my original report.

2. FRESH PASS — new findings only

I have re-read the full revised PDF end-to-end (31 pp., v0.1.71). All previously verified items remain closed. New findings only:

MINORS (polish)

Table VIII caption (p. 17): The k-sufficiency guard and footprint-restricted control row are now present and accurate. The caption now reads “TABLE VIII. Chirality fraction in DESIVAST-anchored vs non-void classes ... (the hole-support-footprint-restricted control row restricts the non-void sample ...)” — exactly as needed.
Fix: None required.
§VIII D (catalog-native V2 membership cross-check, p. 18): The two-sample contrasts for the GALZONE rows are correctly tabulated with explicit complement counts and tied to the Bonferroni-5 family.
Fix: None required.

No BLOCKERS or MAJORS. The manuscript is now publication-ready at the level of a final proofs check.

3. UPDATED RECOMMENDATION

ACCEPT.

The paper has moved decisively toward (and has now reached) full publishability: the estimand-family coherence, Appendix B contingency tables, duplicate-row clarification, and the final typo/figure updates eliminate the last quantitative transparency items. This version satisfies the highest MNRAS/PRD/JCAP standards of statistical rigour and reproducibility.
