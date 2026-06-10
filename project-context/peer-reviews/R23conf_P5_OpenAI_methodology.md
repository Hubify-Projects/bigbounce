# P5 R23conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.52.pdf` md5=cc7c3390 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6960 chars)
**Wall time**: 350.9s

---

Referee report (Methodology/Statistics)

I reviewed all 24 pages, all tables/figures, equations, captions, and the abstract. I recomputed all binomial σ, ranges, and key ratios from the displayed counts; where MC p-values are quoted I checked they are compatible with NMC = 1000 precision. Below I itemize all issues that require attention.

ESSENTIAL

P5-E1 (Sec. V, p. 5): Mis-specified Equation (1) algebra and dimensions
- Offending text: “σpred = ∆fCW 0.5/√N = 2 · ∆fCW · √N, (1)”
- Problem: As typeset, the left-hand factor reads “∆fCW 0.5/√N” (which is 0.5·∆fCW/√N) but is asserted to equal 2∆fCW√N. The correct identity is σpred = (∆fCW/0.5)√N = 2∆fCW√N. As printed, the equation is dimensionally and algebraically inconsistent.
- Required fix: Correct Eq. (1) to σpred = (∆fCW/0.5) √N = 2 ∆fCW √N. Ensure this corrected form is used consistently wherever σpred is invoked.

P5-E2 (Multiple sections, many pages): Presence of version-history/editorial process language and file-path placeholders in the main text
- Offending examples (non-exhaustive):
  - Sec. V A, p. 5: “Analysis drivers are available in the companion data repository (defined in Appendix B).”
  - Sec. V B, pp. 5–6: Long “Primary vs secondary analysis paths (pre-registration caveat).”
  - Sec. VI A, p. 6: Inline references to internal JSON artifacts.
  - Sec. VI D, pp. 8–9: “An earlier draft quoted… are withdrawn… recomputes.json”
  - Sec. VII, pp. 10–11: “An earlier draft of this table reported… withdrawn…”
  - Sec. VIII B–F and IX–X: Numerous “pipelines/.../outputs/*.json” and “recompute” notes inside results narrative.
- Problem: PRD articles must not contain version-control commentary, retraction notes about prior drafts, or internal pipeline file paths in the main narrative. These belong, if anywhere, in a Supplement or Data availability appendix.
- Required fix: Remove all “earlier draft/withdrawn/recompute” prose and all inline path references from the main text and figure captions. Keep a concise Data and code availability section (Appendix B is fine) with a single pointer to the repository/DOI and version tag; move any operational details there.

P5-E3 (Sec. IV A, p. 4–5): Incomplete specification of the footprint mask dilation
- Offending text: “Build a survey-footprint mask by dilation of occupied cells: 2,417,697 occupied → 3,150,086 in-mask (18.8% of the cube); …”
- Problem: The dilation operator (kernel size/shape, number of iterations) is not specified. The mask definition can materially affect the tidal field near the boundary and the environment counts; omitting the parameters prevents reproducibility and independent validation.
- Required fix: Specify the dilation scheme unambiguously (e.g., morphological dilation by one grid cell using a 3×3×3 structuring element; or radius in cells; number of iterations). Provide a sensitivity statement that the main environment fractions and class-level σ are stable to reasonable dilation choices.

P5-E4 (Global; Abstract p. 1, throughout): Use of post-hoc “primary analysis path” as headline anchor
- Offending text: “Primary path… we designate the DESIVAST-anchored void cross-check as the primary environment-dependent chirality analysis…”
- Problem: The paper explicitly states the primary was chosen post hoc. PRD requires that headline inferences not rely on an analysis choice made after inspecting the data unless the language is reframed as exploratory. The abstract currently elevates a post-hoc choice to headline status.
- Required fix: Either (a) supply a pre-registered analysis plan demonstrating that the DESIVAST test was designated ex ante; or (b) reframe the abstract and conclusions to state clearly that all analyses are post-hoc robustness checks with convergent null results, without privileging one as “primary”. The current presentation must be revised.

MAJOR

P5-M1 (Sec. VIII, p. 12): Overstatement “RSD-immune” for DESIVAST membership
- Offending text: “The DESIVAST primary path is essentially RSD-immune… typical σv/(aH) ≲ 5 Mpc/h… several times smaller than the void effective radii.”
- Problem: While the displacement scale argument is plausible, “RSD-immune” is too strong. The binary in/out test against many overlapping spheres near edges can still flip a non-negligible fraction of galaxy memberships, especially for smaller effective radii. No quantitative bound on the induced ∆fCW is provided.
- Required fix: Tone down to “RSD-suppressed” and provide a quantitative bound on the maximum fraction of spiral memberships that can change under typical RSD displacements (e.g., Monte Carlo shift test with σv/(aH) realized along LoS) and the induced bound on ∆fCW, or remove the immunity claim.

P5-M2 (Sec. VII A, p. 10–11): Multiple-testing control narrative is scattered; tie the test statistic to the null explicitly
- Offending text: Mixed use of “per-cell range” as a descriptive statistic and separate σvs-monopole residuals; both are discussed, but the logical link to a controlled family-wise error rate is not crisp.
- Problem: The paper uses range as a descriptive, then uses a max |σobs−σpred| and an empirical max-stat pLEE. This is acceptable, but the text should clearly define the primary inferential statistic for each sweep cell and apply the same LEE control consistently (e.g., state that the decision rule is “reject if pLEE < 0.05”).
- Required fix: Add a concise statement defining the inferential decision rule per sweep cell (e.g., empirical max-stat pLEE on the per-class σfrom half, adjusted for nine cells), and move the descriptive range to secondary status.

P5-M3 (Sec. XI, p. 20): Confidence-threshold sweep text vs. table mismatch
- Offending text: “drifts by at most −0.24 pp from the full-sample value at pmax_cls ≥ 0.7…”
- Problem: Table XIII reports thresholds at 0.4/0.6/0.8 (no 0.7 row). The largest reported drift is −0.219 pp at ≥ 0.8. The prose mentions ≥ 0.7 and −0.24 pp, which is not documented in the table.
- Required fix: Either include the ≥ 0.7 row in Table XIII with its fCW and n, or adjust the text to match the shown thresholds and the actual maximum drift.

P5-M4 (Sec. IX B, p. 17–19): Clarify “like-for-like” concordance calculation and state the exact two-sample z
- Offending text: “filament like vs filament: 0.29 pp… ∼0.5σ two-sample…”
- Problem: The text is correct by my recomputation (z ≈ 0.49), but please show the explicit two-sample z-value in the text or caption, and confirm the variance model used (pooled vs. unpooled at p≈0.5; both are virtually identical but state it).

P5-M5 (Throughout): Terminology consistency: “V-Web” label used for a T-Web (tidal-tensor) implementation
- Offending text: Footnote defines this use, but the body sometimes contrasts to “T-Web concurrent-literature overlay.”
- Problem: This can confuse readers. You are using the Hahn et al. (2007) tidal-tensor (often called T-Web) on density fields; “V-Web” is often reserved for velocity-shear classifiers.
- Required fix: Either uniformly rename your classifier “T-Web (Hahn 2007 tidal tensor)” throughout, or keep “V-Web” but add an explicit, brief disclaimer in the main text at first mention (not a footnote) that this is the T-Web density Hessian, not velocity-shear.

MINOR

P5-m1 (Sec. III D, Table I, p. 4): Arithmetic/consistency check
- Sum checks OK: CW+CCW = 791,635; adding NS = 2,232,212; SPECTYPE counts sum to catalog; leg counts sum to catalog. Note: Please define “NS” on first use in the table caption (“not spiral” or “not scored”).
- Required fix: Add a one-sentence definition of NS in the caption.

P5-m2 (Sec. VI A, p. 6): Comparability of σ across bins is flagged here but not always reiterated later
- Offending text: “σfrom half scales as √n… and is not comparable across rows of different n.”
- Problem: Later sections sometimes quote per-quartile or per-class σ values adjacent to each other without restating non-comparability (though you do use σvs-monopole elsewhere).
- Required fix: Where multiple σfrom half values are juxtaposed (e.g., Table IV), add a brief note that raw σfrom half are not cross-bin comparable; the relevant inferential comparison is σvs-monopole or two-sample tests.

P5-m3 (Sec. VII, Table VI, p. 11): Clarify that “range (pp)” is dominated by the void-bin counting error
- Problem: You note this in prose; consider adding a parenthetical in the table caption: “range is dominated by the void-bin binomial error at these nvoid.”

P5-m4 (Sec. IX C, p. 18): Comparison to concurrent T-Web fractions
- Problem: You report tracer-dependent fractions from Ref. [11] on an 800 Mpc cube, then compare to your all-spectro, shell geometry. This is fine as a qualitative check; please add one sentence that no direct per-galaxy cross-match is attempted here and the comparison is purely on volume fractions.

P5-m5 (Sec. VIII E, Table IX, p. 14): State whether the HEALPix pixel areas are equal-area (they are) and that Nside=16 implies ~3.66 deg2 per pixel for reader orientation.
- Required fix: Add a short note in the caption.

P5-m6 (Figures 2, 3, 5–8; multiple pages): Notation “2563” for grid size
- Problem: “2563” is ambiguous; PRD style uses 256^3.
- Required fix: Replace “2563” with “256^3” throughout figures/captions/text.

P5-m7 (Sec. VIII B, p. 13): Provide integer counts nCW or exact fCW ± Jeffreys 95% CI
- Problem: Table VII lists fCW only. For completeness and transparency, add either nCW or 95% Jeffreys CI for both void and non-void classes.

P5-m8 (Sec. XIII, p. 21–22): RSD floor inconsistencies
- Offending text: σv/(aH) ≲ 5 Mpc/h (p. 12) vs. 5–8 Mpc/h (p. 22).
- Required fix: Use a single consistent bound (with a brief justification for the number/range) across the manuscript.

P5-m9 (Sec. XII C, p. 21): “largest matched-sample environmental-dependence test … to our knowledge”
- Problem: “largest” claims require a citation or removal.
- Required fix: Either add a citation/comparison table to prior works to substantiate “largest,” or soften to “a large matched-sample …”.

NITS

P5-n1 (Abstract and throughout): Define “pp” at first occurrence as “percentage points”.
P5-n2 (Typographic): Replace unicode primes in arcseconds with ″ (or spell out arcsec) consistently (“1′′” appears OK, ensure it renders).
P5-n3 (Consistency): Use either h−1 Mpc or Mpc/h consistently (prefer PRD style h−1 Mpc).
P5-n4 (Style): Several very long parenthetical asides (e.g., Sec. VI D) reduce readability; consider moving lengthy qualifiers to footnotes or appendix.

Arithmetic/statistical spot checks (passed)

- Table II σfrom half recomputed from counts: void −0.676, wall +0.551, filament −2.605, cluster −4.659. Matches within rounding.
- Abstract binomial 2σ half-width for N=428: ±4.83 pp; matches “±4.8 pp”.
- Paper IV monopole predictions σpred = 2∆fCW√N check: filament (−3.32), cluster (−3.28); matches.
- Density quintiles Table III: σpred ≈ 2.07 per quintile; residuals |σobs−σpred| match table within rounding.
- DESIVAST void vs non-void (Table VII): σvoid ≈ −1.72, σnon-void ≈ −4.57; consistent.
- Bright vs dark whole-catalog difference 0.81 pp: two-sample z ≈ 1.95–2.0; as stated.
- Tempel like-for-like filament difference 0.29 pp: two-sample z ≈ 0.49; as stated.

Comments on scope/length

The manuscript is long (24 pages) relative to the contribution (a carefully executed null with multiple cross-checks). A substantial fraction of the text is housekeeping about prior drafts, pipeline paths, and internal recomputes. I strongly recommend trimming the main text to ≤16–18 pages by:
- Removing all version-history/editorial remarks from the main text (Essential fix above).
- Moving ancillary cross-check details (e.g., some HEALPix variants, minor z-shell geometry variant) to a Supplement/Appendix.
- Keeping one clear, compact Methods section and one compact Results section, with the detailed numbers retained in tables.

## Summary recommendation
MAJOR REVISIONS

The core statistical methodology is largely sound, and the arithmetic checks out. However, (i) Eq. (1) must be corrected; (ii) all version-history/path artifacts must be excised from the main text; (iii) the mask-dilation parameterization must be specified; and (iv) the post-hoc designation of a “primary” analysis must be reframed or pre-registration provided. Several smaller clarity and consistency fixes are also needed. Once these are addressed, the paper would present a rigorous, well-documented null result suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E5 (Sec. III B vs. Sec. IV A): Inconsistent SPECTYPE filter for the tidal-field parent sample
- Offending text:
  - Sec. III B (p. 3–4): “restricted to ZWARN==0, SPECTYPE ∈ {GALAXY, QSO}, and 0.01 ≤ z ≤ 4.”
  - Sec. IV A, step 1 (p. 4–5): “Filter … ZWARN==0, SPECTYPE = GALAXY, 0.01 ≤ z ≤ 2.0 (yields 14,622,283 galaxies).”
- Problem: The first states GALAXY+QSO to z ≤ 4; the algorithm actually uses GALAXY-only to z ≤ 2 for V-Web. This is a core reproducibility ambiguity about which objects source the density field.
- Required fix: State unambiguously that the V-Web density field uses only SPECTYPE=GALAXY and 0.01 ≤ z ≤ 2.0, and confine the GALAXY+QSO, z ≤ 4 description to the initial DR1 ingest only. Adjust any language elsewhere that suggests QSO were included in the tidal-tensor estimation.

P5-E6 (Sec. XI, Table XIII, p. 20): Match-radius sweep counts inconsistent with baseline
- Offending text: Table XIII shows for “Match radius 0.5″” n = 820,266, while the baseline “full sample” (1″ acceptance) is n = 791,635; the 5.0″ row is 868,165.
- Problem: Tightening the acceptance to 0.5″ cannot yield more chirality-relevant matches than at 1″ if the same deduplication is used. Either the rows are mislabeled or n refers to a different parent. This undermines the stated conclusion “flat to 0.02 pp.”
- Required fix: Correct the n values (and labels) for the match-radius rows, explicitly state the parent used (chirality-relevant after dedup), and re-state the drift relative to the corrected 1″ baseline. If a different parent was used, say so and provide the 1″ number on that same parent for apples-to-apples comparison.

P5-M6 (Sec. VII A, p. 10–11): Bonferroni-9 threshold miscomputed
- Offending text: “far below the Bonferroni-9 threshold |σ|Bonf0.05,9 ≈ 3.02”
- Problem: For a two-sided Gaussian, |σ|Bonf0.05,9 = √2 erfc−1(0.05/9) ≈ 2.77, not 3.02. The 3.02 figure corresponds to α/K ≈ 0.002 (i.e., α=0.01, K=5).
- Required fix: Correct the threshold to ≈ 2.77 and re-check that all claims “below Bonferroni-9” still hold (they should, since the largest residual is 1.87). Ensure all other Bonferroni numbers use the correct α and K.

P5-M7 (Sec. VI E, p. 10): Deterministic-seed reproducibility vs. quoted p-values
- Offending text: The HEALPix scan first reports free-shuffle p = 0.607/0.135/0.413 (NSIDE 16/32/64). A few lines later: “p = 0.63/0.089/0.41 stratified vs 0.64/0.10/0.42 free-shuffle re-draws.”
- Problem: With a fixed deterministic seed (Appendix B), the free-shuffle p-values for the same dataset should not change between mentions. Differences of ~0.03–0.04 at NSIDE=32 exceed the ~0.01 MC error for NMC=1000 and suggest either a different parent, a seed change, or a bug.
- Required fix: Re-run with a single, documented seed and parent; report one set of free-shuffle and one set of stratified-shuffle p-values, and reconcile any prior discrepancies.

P5-M8 (Sec. V, p. 5; results sections): Position-shuffle null mentioned but not reported
- Offending text: “we run two complementary nulls: (i) label-shuffle …; (ii) position-shuffle …”
- Problem: Only label-shuffle outcomes are shown throughout; the position-shuffle results are never presented.
- Required fix: Either (a) add the position-shuffle outcomes (p-values or a statement of concordance with label-shuffle) for each analysis where label-shuffle is reported, or (b) remove the position-shuffle from Methods to avoid a methods/results mismatch.

P5-M9 (Sec. V A, p. 5): “within ~10%” agreement claim for Bonferroni vs. empirical LEE not substantiated
- Offending text: “the two [Bonferroni and empirical max-stat] agree to within ∼10% on all scans in this paper at α = 0.01.”
- Problem: No quantitative comparison is shown. Moreover, within the same section, p-values for analogous tests vary by more than 10% between different draws/variants, making the claim ambiguous.
- Required fix: Either show a small summary table quantifying the Bonferroni threshold vs empirical max-stat percentile for each multi-bin scan (redshift, density, HEALPix) to justify the “within 10%” statement, or soften/remove that claim.

P5-m10 (Sec. X, Table XII, p. 20): Incomplete reporting for ASTRA cross-check
- Problem: The table lists ranges/max |σ| but no per-class n or counts, preventing verification of the σ and the Bonferroni evaluation.
- Required fix: Add per-class n (and preferably nCW) for the ASTRA argmax and entropy-weighted variants; optionally include Jeffreys 95% CIs for fCW.

P5-m11 (Sec. VIII B, p. 13): Ambiguous denominator in “+0.18%” shift
- Offending text: “moves 100 galaxies (+0.18%) into the void class …”
- Problem: It is unclear whether 0.18% is relative to nvoid (56,981) or to the full z ≤ 0.24 matched sample (678,945).
- Required fix: Specify the denominator explicitly (it appears to be relative to nvoid).

P5-m12 (Sec. III B vs. IV A): Redshift window consistency for parent sample
- Problem: Sec. III B describes ingest to z ≤ 4, while IV A (correctly) applies z ≤ 2 for the V-Web parent. The “tighter window” phrasing is easy to miss.
- Required fix: Add a one-sentence clarifier in Sec. III B that the V-Web parent is subsequently restricted to 0.01 ≤ z ≤ 2.0 (SPECTYPE=GALAXY), so that readers do not confuse ingest scope with analysis scope.

P5-m13 (Sec. VI E, Table V, p. 10): Clarify npix definition
- Problem: Table V lists npix = 1,054/3,303/7,208 at NSIDE 16/32/64, which are not the full-sky pixel counts. It likely reflects “occupied” pixels under the survey mask.
- Required fix: Add “npix = number of occupied (data-containing) pixels used in the scan” to the caption.

P5-m14 (Sec. VII A, p. 10–11; Table VI): Substantiation of the |σvoid| ≤ 1.35 claim
- Problem: The statement that the void bin’s |σ| never exceeds 1.35 across nine cells is not tabulated.
- Required fix: Add an extra column to Table VI with |σvoid| per cell (or provide a one-line supplementary table), so readers can verify this bound.

P5-m15 (Sec. IX A, p. 16–17): Selection-corrected rebuild lacks per-class counts
- Problem: You give fCW values and the range collapse (0.05 pp), but not the per-class n, preventing readers from reproducing the χ2 = 0.11 (p = 0.99) claim.
- Required fix: Provide per-class n (and optionally nCW) for the z-shell-corrected run in a small table or in the caption of the relevant figure.

P5-n5 (Notation): χ2 formatting
- Problem: χ2 appears as “χ
2” in multiple places.
- Required fix: Typeset as χ^2 consistently per journal style.

Explanation
I focused on new issues not covered in my initial report, emphasizing internal consistency, arithmetic/combinatorics, and methods/results alignment. The items above include concrete numeric inconsistencies (Bonferroni-9 threshold; match-radius n), a sample-definition ambiguity (GALAXY vs GALAXY+QSO), reproducibility/sloppy seeding in the HEALPix p-values, and several places where minimal added counts or clarifications would let readers fully verify the claims.