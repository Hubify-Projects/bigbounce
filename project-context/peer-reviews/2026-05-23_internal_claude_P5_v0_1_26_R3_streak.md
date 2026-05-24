# P5 (v0.1.26-2026-05-23) — R3 Streak Pass

**Reviewer**: Claude (Opus 4.7), adversarial third-pass review
**Date**: 2026-05-23
**Paper**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (29 pp, 1,486 lines, v0.1.26-2026-05-23)
**Scope**: Verify closure of the 3 v0.1.25 → v0.1.26 corrections (R2 #N1 row-total reconciliation, #N2 stale "fifth independent", #N3 missing cluster-side joint z artifact) and adversarial third-pass sweep for any NEW findings.
**Method**: Full re-read of abstract + §V + §VI.A/D + §VII.D (DESIVAST + P4-monopole residual block + Pearson-r robustness) + §VII.E + Conclusions; independent recompute of cluster bright-vs-dark joint z from `cluster_within_class_decomposition.json`; per-class n_CW / 812,793 row-total arithmetic; abstract-vs-body enumeration cross-check of the four DESIVAST cross-checks; stale-token sweep for any remaining "fifth"/"five independent" residue.
**Time budget**: ~3 min, target 0–5 new findings.

---

## Verification of v0.1.25 → v0.1.26 corrections

| # | R2 finding | v0.1.26 edit | Verdict |
|---|---|---|---|
| 1 | R2 #N3 — cluster-side joint z=3.4σ unverifiable from on-disk artifacts; either persist `cluster_within_class_decomposition.json` or qualify the abstract | (a) `pipelines/p5_desi_chirality/results/analysis_cosmic_web/cluster_within_class_decomposition.json` is now committed (cluster_n_total=397,505 = 696+392,342+4,234+233 ✓; bright n=392,342 f=0.49622 σ=−4.74, dark n=4,234 f=0.50024 σ=+0.03; persisted `bright_vs_dark_joint_z = −0.5201746`). (b) Abstract L141–149 now honestly attributes joint significance to filament class alone (`|z|≈3.4σ on the filament class`) and qualifies the cluster-class joint as `|z|≈0.5σ … null at counting-statistics noise because the cluster-restricted dark sample n=4,234 is too small to power the test`. | **CLOSED CORRECTLY.** Independent recompute: pooled SE on (n_b=392,342, n_d=4,234, Δf=−0.004019) gives z=−0.5202, matches persisted value to 4 dp; abstract `≈0.5σ` is honest rounding of |−0.52|. The qualifier "cluster-restricted dark sample n=4,234 is too small to power the test" is the right framing — sample size is the rate-limiter, not a contradictory environmental signal. R1 MAJOR #4 is now fully closed (filament joint z=−3.40σ stands, cluster joint z=−0.52σ honestly null). |
| 2 | R2 #N1 — row-total reconciliation arithmetic is correct but the verbal explanation at L1161–1166 was self-contradictory ("CW/CCW spirals excluded from the high-confidence chirality sample at the p_cls_eq^max cut" reads as a logical contradiction) | §VII.D P4-monopole paragraph at L1163–1175 rewritten: "the 21,158-row excess (2.7%) over the 791,635-spiral headline subsample is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter; the per-class n_CW values on the 812,793 superset sum to 404,111 giving f_CW = 0.49719, matching the 791,635-spiral monopole 0.4972 to 4 decimals…". Also folds in R2 #N4 dual-denominator clarification ("The same monopole shows up as −5.00σ on the 791,635-spiral chirality-relevant sample; the two σ values are sample-size-scaled projections of the same underlying offset"). | **CLOSED CORRECTLY.** Independent recompute: 404,111/812,793 = 0.49719 ✓; 2(0.49719−0.5)√812,793 = −5.07 ✓; 2(0.49719−0.5)√791,635 = −5.00 ✓. The causal story now traces the 21,158-row excess to the env-label confidence filter rather than the chirality-label filter, which removes the v0.1.25 self-contradiction. R2 #N4 dual-denominator footnote folded in cleanly. |
| 3 | R2 #N2 — body L1138 self-numbered as "a fifth independent line of evidence" contradicting abstract's "four complementary cross-checks" (R1 MAJOR #3 closure) | L1141 changed to "This is a fourth catalog-anchored cross-check (sky-position stratification axis, complementary to the per-galaxy / DESIVAST-classifier / catalog-native-GALZONE axes)…". `grep "fifth\|five independent\|five complementary"` returns 0 hits across the entire paper. | **CLOSED CORRECTLY** — but introduces R3 minor #N7 below (the body's "fourth" enumeration axes do not exactly match the abstract's (i)–(iv)). The closure is good; the per-class axis labeling is a separate cosmetic issue. |

**3 v0.1.25 → v0.1.26 corrections: 3 / 3 verified correct.** All three are arithmetic-clean and self-consistent on independent recompute. The cluster-side persisted JSON is now load-bearing for the abstract claim and the row-total reconciliation no longer contradicts itself.

---

## R2 nits still present (deferred, not closed — expected per R2 verdict)

- **R2 #N4 (dual-denominator clarification)**: closed by the rewrite of #N1, since the −5.00σ on 791,635 vs −5.07σ on 812,793 footnote is now folded into the same paragraph at L1173–1175. **Closed as a side-effect of #N1**, no longer present.
- **R2 #N5 (missing `voids_vs_chirality_robustness_grid.json` for the 3×3 NSIDE × spiral-cut Pearson-r grid)**: still present. L1245 still reads "verified by reanalysis on the same artifact set" with no companion JSON. Houston-Method-v2 reproducibility receipt for the parenthetical 9-cell robustness claim is still verbal. Deferred — fine.
- **R2 #N6 (figure float run-on at L454 `\end{figure} The negative`)**: still present (line 454, same source as v0.1.25). Cosmetic LaTeX hygiene; below the project PDF-formatting bar. Deferred — fine.

---

## New findings (third-pass)

### Finding #N7
**Class**: minor
**Section/line**: Abstract L109–135 (the (i)–(iv) DESIVAST cross-check enumeration) vs §VII.D L1141 maximal-void HEALPix sentence (the body "fourth catalog-anchored cross-check" with its parenthetical axis listing).

**Claim flagged**: Abstract enumerates four cross-checks as (i) DESIVAST per-galaxy void classifier; (ii) three-algorithm DESIVAST robustness (VoidFinder + V2-REVOLVER + V2-VIDE) including the catalog-native GALZONE membership check inline; (iii) HEALPix sky-position stratification by maximal-void density; (iv) per-pixel Pearson r between maximal-void density and chirality σ. Body L1141 closes the maximal-void HEALPix paragraph with "This is a **fourth catalog-anchored cross-check** (sky-position stratification axis, complementary to the per-galaxy / DESIVAST-classifier / catalog-native-GALZONE axes)…" — i.e. body enumerates 4 axes as {per-galaxy, DESIVAST-classifier, catalog-native-GALZONE, sky-position}.

**Issue**: The two enumerations don't match. Abstract (ii) bundles `three-algorithm DESIVAST` + `catalog-native GALZONE` into a single cross-check; body L1141 splits them into separate axes (DESIVAST-classifier and catalog-native-GALZONE). That makes the body's four axes one short of abstract's four cross-checks (the per-pixel Pearson r at §VII.D L1227 is then a fifth axis under body's enumeration). Per-pixel Pearson r is then orphaned — it's abstract item (iv) but is not listed in body's L1141 quartet.

**Severity / impact**: The headline conclusion is invariant — five vs four is the same closure round-tripping #N2 fixed last round, and arithmetic on every individual cross-check stands. But a careful reader will notice that "fourth" at L1141 plus the still-present §VII.D L1227–1247 Pearson-r subsection appears to undercount the body's cross-checks vs the abstract's enumeration. Houston is right to flag this class of stale-cross-reference (it's the same failure mode as R2 #N2, just at a finer grain).

**Fix**: Either (a) align body L1141 parenthetical to read "(sky-position stratification axis, complementary to the per-galaxy / 3-algorithm-DESIVAST / per-pixel-Pearson-r axes; cf. abstract items (i)–(iv))" so the body's quartet equals the abstract's enumeration; or (b) demote L1141's "fourth catalog-anchored cross-check" wording to "an additional catalog-anchored cross-check on the sky-position axis" without committing to a specific cardinality. Option (b) is the lower-edit-footprint fix and prevents future drift.

**Verifiable**: trivially, by text grep + reading abstract enumeration.

---

### Finding #N8
**Class**: nit
**Section/line**: §VII.D L1163–1175 (the rewritten P4-monopole paragraph closing R2 #N1).

**Claim flagged**: The reconciliation now reads "$f_{\rm CW}^{\rm P5} = 0.4972$ ($-5.07\sigma$ on $n = 812{,}793$ env-labeled spirals --- the $21{,}158$-row excess (2.7\%) over the 791,635-spiral headline subsample is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter; the per-class $n_{\rm CW}$ values on the 812{,}793 superset sum to $404{,}111$ giving $f_{\rm CW} = 0.49719$, matching the 791{,}635-spiral monopole $0.4972$ to 4 decimals, so the headline conclusion is invariant. The same monopole shows up as $-5.00\sigma$ on the $791{,}635$-spiral chirality-relevant sample; the two $\sigma$ values are sample-size-scaled projections of the same underlying offset), which is the propagation of the $\sim\!9.5\sigma$ catalog-level monopole reported in Paper~IV~\cite{golden_chirality_2026}…".

**Issue**: This is a single 13-line parenthetical inside an already long sentence. The clause "($-5.07\sigma$ on $n=812{,}793$ env-labeled spirals --- the 21,158-row excess … is the population … so the headline conclusion is invariant. The same monopole … offset)" reaches 11 lines and contains a sentence break (period followed by capital "The") inside the parenthetical, which is a typographic smell — the inner sentence should either close the parenthetical first or use a semicolon. As written this is correct LaTeX but reads as a wall-of-clauses on the rendered PDF. The arithmetic and causal story are correct.

**Severity / impact**: pure cosmetic. The 11-line parenthetical is exactly the kind of "wall-of-math/text" pattern the global PDF-formatting protocol calls out (`feedback_pdf_visual_formatting.md`). Recommend breaking the parenthetical into a dedicated explanatory sub-sentence on its own line.

**Fix**: Pull the parenthetical out of the outer sentence: replace "($-5.07\sigma$ … same underlying offset),which" with "($-5.07\sigma$ on $n = 812{,}793$ env-labeled spirals; see footnote). The footnote/inline-clarification then carries the 21,158-row reconciliation, the 404,111/812,793 = 0.49719 cross-check, and the dual-denominator −5.00/−5.07 split as three short sentences rather than a 13-line clause. Net edit: replace one comma with a period and add a footnote command. Below Houston's PDF-readability bar but worth tidying on the next compile.

**Verifiable**: yes — visual inspection of the rendered PDF would confirm the wall-of-clause smell.

---

## Summary

| Class | v0.1.25 → v0.1.26 closures | New findings |
|---|---|---|
| BLOCKER | 0 (none open) | 0 |
| MAJOR | R1 MAJOR #4 cluster-side now fully closed; R1 MAJOR #2 row-total reconciliation now self-consistent; R1 MAJOR #3 "fifth independent" stale residue now zero | 0 |
| minor | R2 #N1 closed; R2 #N2 closed; R2 #N3 closed (cluster JSON persisted + abstract qualified); R2 #N4 closed as side-effect of #N1 | 1 (#N7 abstract-vs-body enumeration axis mismatch) |
| nit | R2 #N5 still present (deferred — fine); R2 #N6 still present (deferred — fine) | 1 (#N8 11-line parenthetical at §VII.D L1163–1175) |

**Total new findings: 2** (0 BLOCKER, 0 MAJOR, 1 minor, 1 nit).

**Single most important new finding**: **#N7** — body L1141's "fourth catalog-anchored cross-check (sky-position stratification axis, complementary to the per-galaxy / DESIVAST-classifier / catalog-native-GALZONE axes)" axes do not match abstract's (i)–(iv) enumeration. The Pearson-r at §VII.D L1227 is abstract item (iv) but is missing from L1141's body quartet, which makes the body quietly carry a fifth cross-check that the abstract closure of R1 MAJOR #3 was supposed to eliminate. 1-line edit fix; same failure-mode class as R2 #N2.

**Overall verdict — does P5 v0.1.26 establish a 3-consec-clean-rounds streak per AGENT_RULES §4.4.1?**

**YES.** Per §4.4.1 the cascaded-loop-exit criterion for a clean R-round is ≤1–2 polish MAJORs (with 0 BLOCKERs preferred). R1 returned 0 BLOCKER + 4 MAJOR (all closed by R2); R2 returned 0 BLOCKER + 0 MAJOR + 3 minor + 3 nit (all 3 minors closed by R3, 1 nit closed as side-effect of #N1, 2 nits deferred); R3 returns **0 BLOCKER + 0 MAJOR + 1 minor + 1 nit**. The streak is:

| Round | BLOCKER | MAJOR | minor | nit | Verdict |
|---|---|---|---|---|---|
| R1 (v0.1.22) | 0 | 4 | 4 | 4 | not clean (MAJORs open) |
| R2 (v0.1.25) | 0 | 0 | 3 | 3 | **clean** (0 MAJOR) |
| R3 (v0.1.26) | 0 | 0 | 1 | 1 | **clean** (0 MAJOR) |

**R2 + R3 = 2 consecutive clean rounds.** P5 still needs one more clean R-round (cross-vendor or internal) to hit the 3-consec-clean streak required by §4.4.1 for external-review release. The remaining findings (#N5, #N6, #N7, #N8) are all 5–10 min editing fixes that can ride a single R4 compile without re-running any pipeline. **Recommend**: close #N7 (1-line axis-alignment fix at L1141), close #N8 (break the 11-line parenthetical), persist #N5 (5-min `voids_vs_chirality_robustness_grid.json` companion), close #N6 (blank line after `\end{figure}` at L454), bump to v0.1.27, recompile, and run R4 as the third-consec-clean attempt. No retraining, no MCMC rerun, no fresh artifact generation needed.
