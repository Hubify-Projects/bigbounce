# EXT2 P5 — ChatGPT in-thread delta review
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064
**PDF**: p5_desi_chirality_v0.1.62.pdf · **Harvested**: 2026-06-10 ~21:30 PDT
**Mode**: same-thread re-review (closure verification + fresh pass + updated verdict)

---

Show more
Thought for 8m 4s
Referee report on Paper 5 v0.1.62

Updated recommendation: MAJOR REVISIONS.
The paper moved toward publishability: several quantitative closures are real, especially the DESIVAST count correction, target-program effect-size accounting, and the improved Phase 2/statistical bookkeeping. However, the primary DESIVAST control-sample/mask issue and the continued use of approximate k=20 VoidFinder membership as the reported primary statistic remain publication-level obstacles.

1. Closure verification of original BLOCKERS
Original issue	Status	Verification
B1. DESIVAST primary non-void control not restricted to DESIVAST usable angular/radial footprint.	PARTIAL	The paper now discusses the problem more explicitly, but the primary table is still not re-tabulated with a formal DESIVAST angular/randoms mask. The text still says the non-void control consists of z ≤ 0.24 galaxies not inside a DESIVAST hole, and explicitly admits those galaxies are “not required” to be in the same survey-mask support; the footprint-mask retabulation is still queued, not done. This remains a blocker. 

p5_desi_chirality_v0.1.62


B2. DESIVAST ApJ void counts wrong.	CLOSED	v0.1.62 now quotes the final ApJ counts 1,489 / 389 / 297 and notes the earlier 1,461 / 420 / 295 values were preliminary. This matches the published DESIVAST record. 

p5_desi_chirality_v0.1.62

 
OSTI

B3. Known-insufficient k=20 VoidFinder membership retained as primary statistic after exact rerun.	NOT ADDRESSED	The manuscript still reports 56,981 as the DESIVAST VoidFinder headline and still says it retains the k=20 catalog statistics “for continuity,” despite the exact k-unbounded rerun moving 100 galaxies into the void class and giving nvoid=57,081. That is exactly the original blocker. 

p5_desi_chirality_v0.1.62


B4. Paper IV chirality labels and monopole are load-bearing but companion is not independently reviewable.	PARTIAL	The paper now states more clearly that Paper IV is a companion, not yet peer-reviewed, and propagates finite monopole uncertainty. But the per-galaxy chirality labels and classifier-monopole correction remain external load-bearing inputs; the Paper IV validation still is not reproduced here, and no immutable catalog DOI/revision is actually given in the PDF.
B5. V-Web/T-Web classifier over-promoted despite selection-function domination.	PARTIAL	The title and primary/secondary declarations are improved, and DESIVAST is now clearly designated primary. However, the paper still devotes the abstract and much of the conclusions to V-Web/T-Web language, while §IX.A says completeness weighting rewrites the environment field wholesale: only 44% of cells and 26.6% of matched spirals retain their class. This is now less damaging, but not fully fixed.
2. Closure verification of original MAJORS
Original issue	Status	Verification
M1. Use correct nomenclature: T-Web, not V-Web.	PARTIAL	The title now says “T-Web (Hahn 2007)” and the footnote clarifies that no Hoffman velocity-shear V-Web is used. But the implementation and prose still repeatedly call the classifier “V-Web.” For a journal article, this remains unnecessarily confusing. 

p5_desi_chirality_v0.1.62


M2. Primary/secondary declaration and analysis tree incomplete.	CLOSED	v0.1.62 adds an explicit analysis-tree table separating the Bonferroni-5 DESIVAST primary family, the Phase 2 secondary family, and descriptive diagnostics. That satisfies the requested fix in substance.
M3. Target-program contingency needs effect size, log p, and unique-target splits.	PARTIAL	Cramér’s V=0.078 and log10 p≈−1069 are now included, and the effect is correctly framed as small but sample-size-amplified. However, the per-class bright/dark split is still row-level and the manuscript explicitly states that a per-class unique-TARGETID program split is not available in the committed artifacts.
M4. DESIVAST independence from target-program residuals asserted, not demonstrated.	PARTIAL	A DESIVAST bright/dark table was added, which is a real improvement. But the text evaluates σ from half within each cell, whereas the relevant conditional test is void vs non-void within each program. From Table IX itself, the dark split has fCW=0.4584 in voids versus 0.5056 in non-voids, a 4.7 pp contrast at about 2σ using the tabulated counts. This is not decisive after multiplicity and small-n caveats, but it cannot be summarized simply as “no sign.”
M5. Phase 2 range statistic overstated.	PARTIAL	The global max-stat correction and Rs=10 grid-resolution caveat are now present. Still, §VII.A continues to say the counting-floor and monopole-subtracted significance “control the false-positive rate”; the empirical max-stat controls that, not the descriptive range/floor comparison.
M6. DESIVAST RSD sensitivity claim too strong.	PARTIAL	The text is improved: it now says “RSD-bounded rather than strictly immune” and labels the Monte Carlo as a fixed-void-geometry sensitivity test. But the same section still leans heavily on a scalar displacement argument while the Monte Carlo changes void membership from 57,081 to 76,490±161, a large membership change even if ∆fCW is stable. 

p5_desi_chirality_v0.1.62


M7. Use DESI primary redshifts/targets or justify row-level zall.	PARTIAL	A unique-TARGETID density-field rebuild was added and is helpful. But there is still no ZCAT_PRIMARY-based rebuild/comparison; the default field is still built from zall survey-program coadd rows.
M8. Tempel and ASTRA over-described as robustness evidence.	PARTIAL	Tempel is now better framed as supporting, not load-bearing. ASTRA is also caveated, but §X still calls the result a “strong robustness result” despite only 25,186 EDR-overlap spirals and strong V-Web/ASTRA per-object label disagreement.
M9. Theoretical/bounce framing disproportionate.	PARTIAL	The appendix now clearly labels the EFT mapping as toy/heuristic, non-covariant, and not a derived constraint. That is a substantial improvement. I would still shorten or move it for MNRAS, but it is no longer a scientific blocker. 

p5_desi_chirality_v0.1.62

3. Fresh pass — new findings only
New BLOCKERS

None beyond the unresolved original blockers above. The remaining blockers are not new: the DESIVAST footprint/control-sample definition and the retained k=20 primary statistic.

New MAJORS

Abstract sample ledger conflates the DESIVAST primary parent with the V-Web environment-labeled parent.
Location: Abstract p.1; §VIII.B p.17.
The abstract says the “headline DESIVAST void test” is anchored on 56,981 void spirals drawn from 783,820 unique chirality-relevant matched spirals and carried on 812,793 environment-labeled coadd rows. But §VIII.B defines the DESIVAST analysis on the z≤0.24 low-z matched-spiral parent, nlz=678,945, and does not require a V-Web environment row. The 783,820 / 812,793 numbers belong to the V-Web environment join, not the DESIVAST primary parent.
Proposed fix: Rewrite the abstract ledger as two separate parents: “DESIVAST primary: 56,981 k=20 VoidFinder void spirals out of 678,945 z≤0.24 matched spirals,” and “V-Web secondary: 812,793 env-labeled coadd rows covering 783,820 unique spirals.” If the exact VoidFinder rerun is promoted, use 57,081 instead.

Primary DESIVAST tables still do not report the actual primary estimand with uncertainty: ∆fCW.
Location: §VIII.B–C, Tables VIII and X, pp.17–18.
The tables give per-class fCW and σ-from-half, but the primary scientific claim is the void–non-void difference. The paper reports ∆fCW textually but does not give its SE, confidence interval, or two-sample p-value in the primary table. From the tabulated VoidFinder counts, ∆fCW = +0.00068 has SE≈0.00219, z≈0.31, p≈0.76, 95% CI≈[−0.0036,+0.0050]. That is the publishable primary null statistic.
Proposed fix: Add columns to Tables VIII–X: ∆fCW, SE(∆), z∆, p∆, and 95% CI for every DESIVAST algorithm and for the bright/dark program split.

The new DESIVAST program-split closure tests the wrong null.
Location: §VIII.B, Table IX, p.17.
Table IX is framed as confirming DESIVAST independence from target-program residuals because each void cell is individually <2σ from half. But the relevant environmental test is not “each cell versus 0.5”; it is “void versus non-void within the same program.” In the dark split, Table IX gives void dark fCW=0.4584 and non-void dark fCW=0.5056, a 4.7 pp contrast. Using the table counts, this is z≈1.97 before multiplicity correction. It is probably small-n noise, but the paper must report it honestly. 

p5_desi_chirality_v0.1.62


Proposed fix: Add conditional void–nonvoid contrasts separately for bright and dark. State that bright is null and dominates the DESIVAST sample; dark is low-n and shows a nominal ~2σ contrast that does not survive the DESIVAST family/multiplicity budget.

The conditional permutation-null language is statistically inaccurate.
Location: §V, p.6.
The text says the label-shuffle null “incorporates the matched-sample monopole uncertainty by construction.” It does not. A label shuffle conditional on the observed total CW count removes uncertainty in the global CW fraction; it tests association with environment conditional on the observed monopole. That is fine, but it is not propagation of classifier-monopole uncertainty. 

p5_desi_chirality_v0.1.62


Proposed fix: Replace that sentence with: “The permutation tests are conditional on the observed matched-sample CW count; uncertainty in the Paper IV classifier monopole is propagated separately in the analytic σpred comparisons.” For a stronger fix, add a beta-binomial or bootstrap layer over the global monopole.

The analysis-tree row “T-Web concurrent-lit void-class overlap” is inconsistent with §IX.C.
Location: Table II p.8; §IX.C p.24.
Table II labels the concurrent T-Web diagnostic as a “void-class overlap,” but §IX.C explicitly says no per-galaxy cross-match is attempted and that the comparison is purely on volume fractions.
Proposed fix: Rename the Table II row to “T-Web concurrent-lit volume-fraction comparison” or actually perform and report a per-object overlap.

New MINORS

The abstract still uses too much ledger detail.
Location: Abstract p.1.
Fix: Move most of the sample-accounting prose to a table; keep only primary DESIVAST parent, V-Web parent, and headline null.

Figure 8 still has visible label/title overlap.
Location: Fig. 8 p.21.
The top-panel colorbar label and bottom-panel title overlap in the rendered PDF.
Fix: Split Fig. 8 into two figures or increase vertical spacing.

Data availability still promises, rather than provides, an archival DOI.
Location: Appendix B p.29.
Fix: Replace “accompanies journal submission” with the actual DOI/Zenodo record before submission, or state “will be archived upon acceptance” if not yet minted. 

p5_desi_chirality_v0.1.62

The wording “strong robustness result” remains too strong for ASTRA.
Location: §X p.26.
Fix: Use “supporting diagnostic” or “EDR-overlap consistency check,” since the same paragraph notes the sample is only 25,186 spirals and that V-Web/ASTRA labels disagree strongly. 

p5_desi_chirality_v0.1.62

Use one journal-facing name for the internal classifier.
Location: Title, abstract, §IV.
Fix: Use “T-Web tidal-tensor classifier” in the paper text and reserve “vweb” for code/artifact path names.

4. Updated verdict

MAJOR REVISIONS.
The revision is materially stronger than the previous version, especially on target-program accounting, DESIVAST counts, and analysis-tree transparency, but it is still not ready for publication until the DESIVAST primary control sample is footprint-supported and the exact VoidFinder membership replaces the known-approximate k=20 headline statistic.

Sources

Pro Extended

