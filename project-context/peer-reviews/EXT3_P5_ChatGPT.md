# EXT3 P5 — ChatGPT in-thread delta review (round 3)
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e6e9-b9a4-83e8-9624-ec9291ae8064
**PDF**: p5_desi_chirality_v0.1.64.pdf · **Harvested**: 2026-06-11 ~02:50 PT

---

Show more
Thought for 13m 24s
Referee report on Paper 5 v0.1.64

Updated recommendation: MAJOR REVISIONS.
The paper moved toward publishability since v0.1.62: the abstract sample ledger, label-shuffle wording, ASTRA scoping, and T-Web volume-fraction relabel are real improvements. However, the two central publication obstacles remain: the DESIVAST non-void control is still not demonstrably restricted to the DESIVAST usable footprint, and the paper still publishes the known-approximate k=20 VoidFinder membership as the primary statistic despite having the exact rerun.

1. Closure verification of original BLOCKERS
Original blocker	Status	Verification
B1. DESIVAST primary non-void control not restricted to DESIVAST usable angular/radial footprint.	PARTIAL	v0.1.64 acknowledges the issue more explicitly, but it still says the non-void control contains z≤0.24 galaxies not inside a DESIVAST hole and is “not required” to lie inside/outside the survey mask; the explicit footprint-mask retabulation is still queued, not performed. This remains a publication blocker because the primary control may still include galaxies outside the DESIVAST usable support. 

p5_desi_chirality_v0.1.64


B2. DESIVAST published counts wrong.	CLOSED	The manuscript now quotes 1,489 / 389 / 297 and identifies 1,461 / 420 / 295 as preliminary. Those values match the final ApJ/ADS/OSTI record. 

p5_desi_chirality_v0.1.64

 
ADS Astronomy Database
+1

B3. Known-insufficient k=20 VoidFinder membership retained after exact rerun.	NOT ADDRESSED	The manuscript still uses 56,981 k=20 VoidFinder void spirals in the title/abstract/table path and explicitly says it retains k=20 statistics for continuity, even though the exact k-unbounded rerun gives nvoid=57,081 and moves 100 galaxies. This is still not acceptable as the published primary statistic. 

p5_desi_chirality_v0.1.64


B4. Paper IV chirality labels and monopole are load-bearing but not independently reviewable here.	PARTIAL	The text is clearer that Paper IV is companion work and propagates finite monopole uncertainty, but the per-galaxy chirality labels and classifier-monopole correction remain external load-bearing inputs. The data/code appendix still promises an archival snapshot at journal submission rather than giving a DOI in this draft.
B5. V-Web/T-Web over-promoted despite selection-function domination.	PARTIAL	The paper now clearly declares DESIVAST primary and V-Web secondary, which is a major improvement. However, the title/conclusions still foreground the V-Web/T-Web cross-check and the text retains “V-Web” for a Hahn T-Web implementation, even while showing that completeness weighting rewrites the environment field and that only 26.6% of matched spirals retain class under the weighted rebuild.
2. Closure verification of original MAJORS
Original major	Status	Verification
M1. Use correct nomenclature: T-Web, not V-Web.	PARTIAL	The title now says “T-Web (Hahn 2007),” and the footnote explains that no Hoffman velocity-shear V-Web is used. But the implementation and much of the prose still call it “V-Web.” For journal clarity, the paper should use “T-Web tidal-tensor classifier” in the text and reserve vweb for code paths. 

p5_desi_chirality_v0.1.64


M2. Primary/secondary declaration and analysis tree incomplete.	CLOSED	Table II now explicitly separates the Bonferroni-5 DESIVAST primary family, the Phase 2 secondary sweep, and descriptive diagnostics. 

p5_desi_chirality_v0.1.64


M3. Target-program contingency needs effect size, log p, and unique-target splits.	PARTIAL	Cramér’s V=0.078 and log10 p≈−1069 are now quoted, and the effect is correctly described as small but sample-size-amplified. The per-class bright/dark split is still row-level, with the manuscript itself noting that galaxies observed under both programs enter both splits and that the overlap-free per-class split is not available.
M4. DESIVAST independence from target-program residuals asserted, not demonstrated.	PARTIAL	The added DESIVAST bright/dark table is useful, and the BGS-bright dominance is now explicit. But the table still tests each cell mainly against 0.5 rather than reporting the conditional void–nonvoid contrast within each programme. In the dark split, Table IX gives fCW=0.4584 for void dark versus 0.5056 for non-void dark, a nominal ≈1.97σ contrast before multiplicity; it is likely small-n noise, but it must be reported as such, not summarized as “no sign.” 

p5_desi_chirality_v0.1.64


M5. Phase 2 range statistic overstated.	PARTIAL	The Phase 2 table now includes global max-stat information and Rs=10 is properly marked grid-unresolved. However, §VII.A still calls the range a “headline robustness statistic” and says the counting floor and monopole-subtracted significance “control the false-positive rate.” The empirical max-stat controls false positives; the range/floor comparison is descriptive. 

p5_desi_chirality_v0.1.64


M6. DESIVAST RSD claim too strong.	PARTIAL	The language is improved to “RSD-bounded rather than strictly immune.” Still, the FoG Monte Carlo raises the void count from 57,081 to 76,490±161, so it is not correct to suggest membership sensitivity is negligible. The conclusion should be limited to “∆fCW is stable under this fixed-void-geometry perturbation.” 

p5_desi_chirality_v0.1.64


M7. Use DESI primary redshifts/targets or justify row-level zall usage.	PARTIAL	A unique-TARGETID density-field rebuild is now included and is useful. But the default redshift and density-field construction still use zall survey-program coadd rows; no ZCAT_PRIMARY-based rebuild/comparison is shown.
M8. Tempel and ASTRA over-described as robustness evidence.	CLOSED	ASTRA is now explicitly scoped as a supporting diagnostic consistency check on the EDR overlap, with the small overlap and strong V-Web/ASTRA label disagreement stated clearly. This satisfies the requested reframing. 

p5_desi_chirality_v0.1.64


M9. Theoretical/bounce framing disproportionate.	PARTIAL	The toy EFT mapping remains, but it is now labelled heuristic, non-covariant, and not affecting the empirical bounds. That is acceptable for a broad phenomenological appendix, but I would still shorten it for MNRAS. 

p5_desi_chirality_v0.1.64

3. Additional closure verification from my v0.1.62 fresh-pass findings
v0.1.62 finding	Status	Verification
Sample ledger conflated DESIVAST and V-Web parents.	CLOSED	The abstract now separates DESIVAST primary: 56,981 k=20 void spirals from 678,945 z≤0.24 matched spirals, and V-Web secondary: 783,820 unique env-matched spirals carried on 812,793 rows. 

p5_desi_chirality_v0.1.64


Conditional permutation-null wording was wrong.	CLOSED	The manuscript now says the permutation null is conditional on the observed matched-sample CW count and propagates monopole uncertainty separately in analytic comparisons. 

p5_desi_chirality_v0.1.64


ASTRA still sounded load-bearing.	CLOSED	ASTRA is now described as a supporting diagnostic consistency check, not load-bearing robustness evidence. 

p5_desi_chirality_v0.1.64


Table II called concurrent T-Web a “void-class overlap.”	CLOSED	Table II now labels it as a T-Web concurrent-literature volume-fraction comparison. 

p5_desi_chirality_v0.1.64


Primary DESIVAST tables lacked the actual ∆fCW uncertainty/p-value.	NOT ADDRESSED	Tables VIII–X still report class fractions and raw σfrom half but do not give SE(∆), z∆, p∆, or CI for the declared primary void–nonvoid estimand.
DESIVAST program split tested the wrong null.	PARTIAL	The table remains useful, but the text still summarizes by cell-vs-half rather than reporting void–nonvoid contrasts within bright and dark. 

p5_desi_chirality_v0.1.64

4. Fresh pass on v0.1.64 — new findings only
New BLOCKERS

None beyond the unresolved carry-over blockers above. The paper is still blocked by the DESIVAST footprint/control definition and by retention of the k=20 headline statistic.

New MAJORS

Title still uses the wrong parent count for the T-Web/V-Web cross-check.
Location: Title and abstract, p.1.
The title says the T-Web cross-check is “Across 791,635 DR1 Matched Spirals,” but the corrected abstract says the V-Web secondary path has 783,820 unique environment-matched spirals, carried on 812,793 coadd rows; 7,815 of the 791,635 chirality-relevant matched spirals lack an environment row. 

p5_desi_chirality_v0.1.64


Proposed fix: Change the title to “... T-Web cross-check across 783,820 environment-matched DR1 spirals” or “... across the 791,635 chirality-relevant DR1 matched sample,” avoiding the implication that all 791,635 have T-Web labels.

The primary-family bookkeeping says “void vs non-void” but still evaluates mainly one-sample void σ.
Location: §V.B / Table II, p.8; §VIII.B–D, pp.17–18.
The declared primary tests are “void vs non-void fCW,” but the multiplicity paragraph says all five return |σvoid|<2, which is a one-sample test against half, not the primary environmental contrast. The actual VoidFinder contrast is ∆fCW=+0.0007; from Table VIII its SE is about 0.00219, z≈0.31, p≈0.76, 95% CI≈[−0.0036,+0.0050]. That is the clean primary null and should be tabulated.
Proposed fix: For each DESIVAST estimator, report ∆fCW, SE(∆), z∆, p∆, and a 95% CI. Use those ∆ tests, not |σvoid|, for the Bonferroni-5 primary family.

The randoms-weighted “completeness-corrected” V-Web rebuild is still too strong as phrased.
Location: §IX.A, pp.21–22.
The rebuild uses BGS BRIGHT clustering randoms in 0.01<z<0.50 and is therefore a valuable BGS-window stress test, not a full DESI-all-tracer completeness correction. The text mostly caveats this, but phrases like “completeness weighting rewrites the environment field wholesale” and “no-environment-dependence holds under completeness-corrected environment definitions” can be read too broadly. 

p5_desi_chirality_v0.1.64


Proposed fix: Rename this throughout to “BGS-randoms-weighted low-z stress test,” and avoid calling it a full DESI completeness-corrected V-Web result.

New MINORS

Figure 3’s rendered title still disagrees with its caption.
Location: Fig. 3, p.7.
The rendered title says n=791,635 chirality-relevant matched spirals, while the caption/table use the 812,793 row-level env-labeled parent and 783,820 unique env-matched spirals. 

p5_desi_chirality_v0.1.64


Proposed fix: Retitle as “CW fraction per cosmic-web class, env-labeled parent” or put both unique and row-level counts in the title.

§VII.A typo: “Pre-cell label-shuffle null.”
Location: §VII.A, p.15.
Proposed fix: Change to “Per-cell label-shuffle null.”

Section X cross-reference is wrong.
Location: §X, p.26.
It lists “DESIVAST per-galaxy cross-match, §IX C,” but the DESIVAST per-galaxy cross-match is §VIII.A; §IX.C is the concurrent-literature comparison. 

p5_desi_chirality_v0.1.64


Proposed fix: Correct to “§VIII.A.”

Data availability still lacks the actual archival DOI.
Location: Appendix B, p.29.
The text says a DOI-minted snapshot accompanies journal submission, but no DOI appears in this draft. 

p5_desi_chirality_v0.1.64


Proposed fix: Insert the DOI before submission, or state explicitly that it will be minted on acceptance.

The conclusion should foreground the DESIVAST primary null before the V-Web secondary null.
Location: Conclusions, p.28.
The conclusion opens with the V-Web-resolution null and only then gives the broader result. The manuscript’s own analysis-tree says DESIVAST is primary. 

p5_desi_chirality_v0.1.64


Proposed fix: Start the conclusion with the DESIVAST void/non-void result and then summarize the V-Web/T-Web diagnostics.

5. Recommendation

MAJOR REVISIONS.
v0.1.64 is a better and more disciplined manuscript than v0.1.62, but it is not yet publishable because the primary DESIVAST control-sample support and exact-membership statistic still have not been fixed.

Sources

Pro Extended

