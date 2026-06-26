# Referee report — P5 v0.1.82 "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test"

**Recommendation: MINOR REVISIONS**

Reviewer: Claude/Opus leg, internal review round R52 (fresh adversarial round following the 2026-06-21 live-external 99→92 roll-back).
Basis: full end-to-end read of the 32-page compiled PDF (`p5_desi_chirality_v0.1.82-2026-06-18.pdf`) plus truth-audit of the cited committed artifacts under `pipelines/p5_desi_chirality/`.

## Summary judgment

This is a careful, multiply-cross-validated **null result**: spiral-galaxy chirality (CW fraction) shows no environment dependence at the ~25 Mpc/h T-Web smoothing scale. The load-bearing claim — environment *independence* — is tested as the cross-class fraction *difference* Δf_CW, which is mathematically independent of the catalog-wide classifier monopole the paper subtracts elsewhere. That primary contrast (DESIVAST void vs non-void, Δf_CW = +0.0007, z_Δ = +0.31, p = 0.76, n = 56,981) is clean, is robust across three independent void-finders (Table X, all |Δf_CW| ≤ 0.002) and two catalog-native GALZONE definitions, and survives Phase-2 hyperparameter sweep, redshift/density/sky-position stratification with LEE correction, Tempel FoF cross-validation, and ASTRA EDR cross-validation.

I verified the headline integer counts against the committed JSON: Tables XVI/XVII (`31_ext5_appendixB_tables.json` ← `17_v0151_closure_recomputes.json`) reproduce exactly (filament 203261/204926, cluster 197284/200221, wall 3359/3314, void 207/221; class×program bright/dark cells all match). All σ_from_half and σ_pred values I spot-checked (Tables III, VIII, X, XII) recompute correctly from the stated counts and Eq. (1). No fabricated or internally inconsistent statistic was found. The reproducibility artifact tree is complete and present on disk.

There is no BLOCKER and no MAJOR: no load-bearing claim is unsupported, no critical control is missing (the n=428 T-Web void weakness is explicitly superseded by the n=56,981 DESIVAST anchor), and the result is reproducible from committed artifacts. The remaining items are presentation/clarity and scope-statement refinements, hence MINOR REVISIONS.

## BLOCKERS

None.

## MAJORS

None. (The RSD and Paper-IV-monopole items below were considered for MAJOR and deliberately downgraded — see MINORS M1, M2 — because each is explicitly scoped, the null is conservative under RSD dilution, and the cross-class contrast is monopole-independent.)

## MINORS

- **M1 — RSD classification carried as order-of-magnitude bound (§XIII, Appendix A; pp. 28–30).** The entire T-Web tidal-tensor classification is performed on redshift-space positions with no real-space deprojection; the quantitative contamination bound (~0.2 pp per-class Δf_CW) is explicitly order-of-magnitude (scalar-displacement heuristic), and the proper Zel'dovich-reconstructed re-classification is deferred to a companion. For a *null* this is acceptable (RSD dilutes rather than manufactures an environment signal, so the bound is conservative), and the limitation is carried prominently. Fix: state once, near the abstract Scope line, that the headline is explicitly a *fixed-redshift-space* statement and that the RSD bound is heuristic, so a reader cannot mistake it for a deprojected result.

- **M2 — Primary monopole reference inherits from a companion in preparation (§II, §VIII F; Paper IV [3]).** The Δf_CW = −0.0026 catalog-wide classifier monopole that every σ_pred subtracts is sourced from Paper IV ("in preparation"). The environment-independence headline is robust to this (it lives in the cross-class contrast), but the *interpretation* of the −5σ catalog-wide offset as a benign classifier systematic rests on Paper IV. Fix: add one sentence making explicit that if Paper IV's monopole value moves, the σ_pred rows (Tables XII, IV, V) move with it, while the Δf_CW null does not — so the headline is insulated by construction.

- **M3 — Abstract is a single ~1.5-page dense block (p. 1).** The headline (DESIVAST Δf_CW = +0.0007, n = 56,981, null) is buried mid-paragraph behind the full sample ledger and the monopole-systematic discussion. MNRAS will want this compressed to a structured ~250-word abstract leading with the result. Fix: lead with recommendation-level finding, move the ledger/conventions into §III.

- **M4 — Residual bright/dark target-program sign-flip (~2.1σ) under-signposted in the abstract (§VI D, §XI; pp. 11–12, 28).** This is the most notable residual structure in the paper (filament bright vs dark |z| ≈ 2.1σ, opposite sign) and is handled transparently in the body, but the abstract folds it into the general "no signal beyond the classifier monopole" statement. Fix: one explicit abstract clause flagging the ~2σ filament bright/dark residual as a diagnostic to be disentangled with DESI DR2, mirroring the body's honesty.

- **M5 — Figure 8 top panel labeling (p. 22).** In the rendered PDF the "voids/pixel" colorbar of the top (maximal-voids count) panel sits very close to the bottom-panel "Chirality σ_from_half per pixel" caption text; verify at print resolution that the two colorbar labels do not visually collide. Cosmetic only.

- **M6 — Two membership-count layers (sphere-PIS vs catalog-native GALZONE) invite confusion (§VIII C/D, Table X vs §VIII D text; pp. 18–19).** V2-REVOLVER n_void = 102,911 (sphere point-in-sphere, Table X) vs 104,912 (catalog-native GALZONE, text), and V2-VIDE 81,354 vs 74,111, are both correct under their respective definitions and are explained — but a reader scanning the two passages will read it as a discrepancy. Fix: a one-line footnote at Table X stating that catalog-native GALZONE counts differ by membership definition and pointing to §VIII D.

- **M7 — "σ_from_half not comparable across rows of different n" caveat is correct but repeated inconsistently.** It appears in Tables III, V, VI, IX, XIII captions and the §V text. Recommend a single canonical statement in §V and a short cross-reference elsewhere, to reduce the impression that the σ columns might be over-interpreted.

## Strengths

- **The null is framed on the correct, monopole-independent statistic.** Testing environment independence as the cross-class Δf_CW contrast (rather than the monopole-contaminated per-class σ_from_half) is the methodologically right choice, and it insulates the headline from the largest systematic in the data. The primary DESIVAST anchor (n = 56,981, ~130× the T-Web void bin) directly fixes the obvious weakness (n=428 T-Web void) instead of hand-waving past it.

- **Exceptionally thorough cross-validation and transparent multiplicity bookkeeping.** Three independent DESIVAST void-finders, two catalog-native zone definitions, a 9-cell hyperparameter sweep, redshift/density/sky-position stratifications with both empirical max-stat and parametric Bonferroni LEE corrections, Tempel FoF and ASTRA EDR external-classifier cross-checks, and an explicit pre-registration / garden-of-forking-paths declaration (Table II) with a stated primary/secondary family split. Every secondary >3σ-looking excursion is chased to a benign origin (boundary misclassification, survey-shell selection, BGS-bright leg).

- **Reproducibility is real, not asserted.** Every numeric claim I sampled (Tables III, IV, V, VIII, X, XII, XVI, XVII) reconciles to four decimals against the committed `outputs/*.json` artifacts, the per-output provenance JSON tree is present on disk, drivers are named per result, and the manuscript is pinned to tag v0.1.82-2026-06-18. The Appendix B contingency tables are committed as a referee-facing reproduction anchor.

- **Honest negative-result discipline.** The paper resists over-claiming: it states plainly that no published bounce or inflation model predicts an environment-conditional chirality signal at this scale, positions the result as an observational upper bound on the bounce-chirality coupling class, and carries the ~2σ bright/dark residual and the RSD limitation as open items rather than burying them.

---

*Verdict rationale (honest calibration): MNRAS/PRD rigor applied. No unsupported load-bearing claim, no missing critical control, full reproducibility from committed artifacts → the bar for MAJOR is not met. The minors are genuine but are clarity/scope/presentation, consistent with MINOR REVISIONS on a catalog/methodology null paper of this size.*
