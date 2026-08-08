# P3 R38conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.104.pdf` md5=359a733d pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6853 chars)
**Wall time**: 669.2s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies …” (29 pages)

Scope of review
- Role: methodology referee (statistical validity, derivation chains, internal arithmetic consistency, error propagation, comparability of σ’s, figure/table audit).
- I read the full manuscript, including figures, tables, and appendices, and recomputed all headline scalars that can be checked from what is printed.

Overall assessment
The paper presents a very large multi-archive anomaly sweep with extensive internal diagnostics and unusually transparent caveats. However, several methodology-critical inconsistencies and placeholders must be corrected before this is suitable for PRD. Most importantly: a dimensionally incorrect expression for F0 in the fNL forecast, a miscomputed Cramér’s V by about a factor of three, unresolved data/code-release placeholders, and several unquantified “robustness” assertions. There are also a few numerical inconsistencies (DESI per-class confidence interval), and reproducibility gaps (eROSITA tier) that require tightening.

Findings

ESSENTIAL

P19–P18-E1 (Section V; also echoed in conclusions): dimensional/notation error in Fisher baseline F0
- Text: “1/σ2(fNL) = F0 + c α2 with F0 = 1/8.982 = 0.01239 …”
- Problem: F0 must have units of 1/σ2. The printed “1/8.982” is dimensionally wrong; 1/8.98 ≈ 0.111, not 0.01239. The numerical 0.01239 corresponds to 1/(8.98)2. As written, F0 is inconsistent.
- Required fix: Replace everywhere with F0 = 1/(8.98)2 = 0.01239 and state explicitly that F0 is the inverse-variance baseline from the single-tracer σ(fNL)std = 8.98. Audit all downstream numeric instances for consistency.

P14-E2 (Section IV.B, p. 14): Cramér’s V miscomputed
- Text: “χ2 = 376,713, dof = 24,048, Cramér’s V = √(χ2/(N·(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.020”
- Problem: Using the provided numbers and the stated formula, V = sqrt(376,713 / (378,280 · 24,048)) ≈ sqrt(4.145×10−5) ≈ 0.00644, not 0.020. The paper’s arithmetic is off by ~3×.
- Required fix: Recompute V correctly (≈0.0064 given the printed χ2, N, k) or correct the inputs and show the consistent calculation. Also state whether k or (k−1) is used, and maintain consistency between dof and k.

P22–P23-E3 (Data availability, pp. 22–23): release placeholders; no minted DOI
- Text: “will be publicly released with the arXiv posting … A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: PRD requires final, stable data/code availability at acceptance. The manuscript contains future-tense language and placeholders rather than permanent identifiers.
- Required fix: Replace all placeholders with a minted DOI for the frozen dataset (catalog and all artifacts), a DOI (or equivalent permanent tag) for the exact code version used, and provide SHA-256 checksums that match the released artifacts. Remove future-tense language. Ensure the release contains all files referenced by path in the manuscript.

P13–P15-E4 (Sections IV.A–IV.C): uncomputed random-coincidence claim
- Text (p. 14): “For the 7-way 5″ deduplication, the expected random coincidence contribution is ≲10 across all survey pairs against 637 observed multi-survey clusters (<2% contamination).”
- Problem: No computation, inputs, or method are provided to justify “≲10.” This is a load-bearing contamination statement.
- Required fix: Provide an explicit calculation (per-pair surface densities, areas, matching radius, independence assumptions) or remove the claim. If a simulation-based estimate is used, give the sampling details and uncertainty.

P11–P12-E5 (Section III.E; Table IV caption): irreproducible eROSITA score axis in mainline text
- Text: Multiple places state that the eROSITA SBigAE score axis is irreproducible from any committed artifacts; the selection is a fixed top-298 “membership-only” list.
- Problem: As written, the main text interleaves references to an irreproducible score axis with catalog claims. Even though the membership list is said to be exactly reproducible from a “committed raw-score artifact,” the paper does not provide a stable DOI and the section is easily misread as a score-calibrated result.
- Required fix: Move all SBigAE numeric references for eROSITA out of the main results into an explicit “membership-only” subsection. In the mainline tables, remove any per-object eROSITA SBigAE values and show only the stable selection key (rank by committed raw-score artifact) with a permanent DOI link. Include an explicit reproducibility protocol: given the released artifact X, sorting key Y, and seed Z, the top-298 list is exactly reproduced.

MAJOR

P8-M1 (Section III.A, p. 8): DESI per-class confidence interval inconsistency
- Text: “GALAXY 0.75% ± 0.02% (Wilson 95% … ~4.9×106), QSO 0.037% ± 0.003% (~1.5×106).”
- Problem: For n ≈ 4.9×106 and p = 0.0075, the 95% Wilson half-width should be ~0.0076% (1.96×sqrt(p(1−p)/n)), not 0.02%. The QSO CI is consistent; the GALAXY CI appears inflated by ≈2.6×.
- Required fix: Recompute the Wilson intervals and correct the reported uncertainties, or explain the different denominator/weighting used and reconcile with Table II’s denominators.

P20-M2 (Section VI.D/Table V (c,e)): unquantified robustness assertions (pattern-048)
- Text: “Fisher + fiber nuisance: |Δσ/σ| < 0.01% at σδfiber = 0.05” and “GR projection: |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1 … internal order-of-magnitude bound.”
- Problem: These quantitative claims lack derivations, inputs, or references sufficient for a reader to reproduce them. They affect headline cosmology statements.
- Required fix: Provide the explicit Fisher block, parameter definitions, priors, and numerical inputs used to obtain the quoted |Δσ/σ| values, or remove the quantitative claims. If they are internal estimates, move to an appendix with the actual matrices/numbers.

P4–P5-M3 (Section II.B and §II.B/a, p. 3–4): scaler fit on full sample introduces validation leakage; incomplete robustness
- Text: For eROSITA/NEOWISE/Gaia, scalers are “fit on the full sample rather than the training split.”
- Problem: Using full-sample normalization leaks validation-set information. Only eROSITA has a bounded robustness check; NEOWISE and Gaia are left “queued.”
- Required fix: Re-train NEOWISE and Gaia with scalers fit on the training split only and report top-1% overlap, rank Spearman ρ, and extreme-tail churn (as done for eROSITA). If irreproducible, state so and downgrade the corresponding tiers to exploratory with clear labels throughout.

P12-M4 (Section III.F, p. 12): Planck top-200 includes majority training patches
- Text: “152/200 in training split, 48 in validation; anomaly tail over-represented toward held-out patches (p ~ 4×10−4).”
- Problem: While the direction argues against memorization, the production top-200 are not from a held-out set. For a catalog product, the use of training data in the released anomaly list requires stronger evidence that the ranking is not biased by training exposure.
- Required fix: Provide a held-out top-200 (scored on the validation split only) alongside the production list, and report the overlap and rank correlations. Alternatively, re-score on a train/val disjoint patch bank and release anomalies from the holdout.

P6-M5 (Figure 2, p. 6): inclusion of quarantined ACT in a headline map
- Text: “ACT DR6 points are shown for completeness … formally quarantined … contributes zero objects.”
- Problem: Displaying ACT anomalies on the cross-transfer baseline map may confuse readers into treating them as part of the result.
- Required fix: Move ACT points to an inset panel explicitly labeled “quarantined cross-transfer artifact” or remove them from Figure 2.

P17-M6 (Figure 8, p. 17): potentially confusing “display score (non-catalog)” annotations
- Text: The panels annotate “display score,” not the catalog score; one panel (d) shows S = 49.5.
- Problem: This is easily misread as the catalog S. While you state the caveat in the caption, the appearance invites confusion.
- Required fix: Remove the numeric “display score” overlays or watermark them as “display-only, not catalog S.” Alternatively, add the catalog S alongside and reconcile differences.

MINOR

P11-m1 (Section III.E/Table IV, p. 12): clarify SIF,raw scale/units
- Text: “SIF,raw … anomaly score on a ~0–3.5×104 scale.”
- Required fix: State explicitly that SIF,raw is dimensionless, give the IsolationForest implementation details (contamination, random_seed), and confirm monotonicity with the ranking used for the membership list.

P10–P11-m2 (Section III.D, p. 10): LAMOST training-bias diagnosis not re-tabulated post-retrain
- Text: Attribution rests on 21.5× rate compression; no post-retrain arm-dominance re-tabulation.
- Required fix: Provide at least a small post-retrain arm-dominance sample audit (e.g., 1,000-object random subsample), or explicitly mark the blue-excess fraction statement as pre-retrain only.

P12-m3 (Section III.F, p. 12): missing Planck native training wall-clock
- Text: Footnote says “the total training wall-clock … was not preserved.”
- Required fix: Either provide the training wall-clock from logs or remove the line. If unavailable, give a point estimate with uncertainty and explain the basis.

P13-m4 (Section IV.A, p. 13): SIMBAD 3″ vs 5″ radii in different summaries
- Text: You note this explicitly, but a first-time reader may still miss it.
- Required fix: Add “(note: pooled 58.8% uses 3″; per-survey uses 5″)” to Figure 6 caption.

P15-m5 (Section IV.C, p. 15): dedicate a short paragraph to the RA/Dec shift control limitations
- Text: You note RA-only shifts are heuristic.
- Required fix: Provide the great-circle/rotation-scrambled control you already plan, or explicitly flag the RA-shift result as preliminary and not used for any quantitative contamination claim.

P7-m6 (Table I, p. 7): presentation density
- Problem: The footnotes have heavy cross-qualification that is hard to parse.
- Required fix: Split the most critical cross-qualifications into a short “Thresholding and gating summary” subsection immediately after Table I, with a compact bullet list.

NIT

P8–P26-N1: numerous hyphenation artifacts from line breaks (e.g., “compos￾ite,” “variab￾ility”)
- Required fix: Clean up PDF hyphenation/ligature artifacts before final submission.

P12-N2: Range for Planck per-patch MSE “[0.558, 0.621]” lacks unit label
- Required fix: Append “(dimensionless MSE on standardized patches).”

P23-N3 (Appendix C/Fig. 11): normalization note is good; add a sentence at the figure top reminding readers “absolute σ(fNL) values in this figure are not comparable to §V.”

Abstract-last drift audit (pattern-045)
- The abstract numerics (37.3 M total; 378,280 unique; 269,317 catalog-grade including 200 Planck; 269,117 point-source catalog-grade; 195,829 DESI; 2,468 science-class matches; 17.8% novelty ±1.2%; 21.5× LAMOST rate reduction; ~6500× SDSS rate compression; JCV = 0.862; Jprod×ctrl = 0.732; injections PASS/FAIL; αjk = 0.19 ± 0.65; σ(fNL) central 8.14 with envelope [3.92, 8.98]; NANOGrav γ = 2.567 ± 0.382; SMBHB +4.61σ; Bayes factor 7.14×103) are traceable to the body and correct, except:
  - ESSENTIAL mismatch E1: F0 notation error, fix.
  - The abstract appropriately caveats the non-comparability of some sigmas and the non-detection status.

Figure/table audit
- Figure 2: axes/labelling fine; ACT presence flagged under MAJOR M5.
- Figure 3: axes labelled; log scales consistent; thresholds match text; OK.
- Figure 4: UMAP/HDBSCAN; descriptive; OK.
- Figure 5: qualitative; OK.
- Figure 6: add radius note (MINOR).
- Figure 7: panels match text; OK.
- Figure 8: display-score caveat fix (MAJOR M6).
- Tables I–IV: arithmetic checks out except the global issues flagged; Table I totals and dedup math reconcile with §IV.C.
- Table VI–VIII: consistent with body; add missing Planck training time (MINOR).

Bibliography
- Spot checks look plausible. Verify [12] year (“2026” with arXiv:2506.x) at acceptance; ensure final bibliographic data are updated.

Length
- 29 pages is long for the claimed methodological contribution. With the above corrections, a modest condensation (e.g., move some path names and long footnotes to an online supplement, streamline Table I footnotes into main text) would improve readability, but I do not impose a hard page cap provided all essential fixes are addressed.

## Summary recommendation
MAJOR REVISIONS

The work is ambitious and potentially valuable, but cannot be accepted in its current form. At minimum, the Fisher-baseline notation error and the Cramér’s V miscalculation must be corrected; the data/code-release placeholders replaced with permanent identifiers; the unquantified “≲10 random coincidences” claim either computed or removed; the eROSITA tier presented as a reproducible membership-only product with stable artifacts; and the few remaining methodological inconsistencies (DESI per-class CI, scaler leakage, Planck holdout) must be addressed with concrete numbers. Once these are fixed and documented, I am prepared to reassess.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P7–E6 (Table I totals; Path-C “Ntotal” denominator mismatch for Planck)
- Text: Path-C unique row lists Ntotal = 37,272,042 (excludes ACT); Planck row notes the released tier is top-200 of a native 2×10^5 patch bank, while the table Ntotal column and the total-row bookkeeping still reflect the original 20,000 cross-transfer patch bank.
- Problem: The Path-C “processed total” undercounts by ≈180,000 patches relative to the actual native-trained Planck run used to generate the released tier. This is a stale denominator/inconsistent bookkeeping across the table and the prose.
- Required fix: Make Ntotal consistent with what was actually processed for the released catalog (i.e., 200,000 Planck patches) and propagate this to the Path-C total, or add a prominent footnote in the Path-C rows clarifying that Ntotal intentionally reflects the cross-transfer input for historical comparability while the released Planck tier is drawn from a 10× larger native bank. As written, the mixed denominators are confusing and likely to be misquoted.

MAJOR

P10–M7 (Section III.C; SDSS “z-scored” S percentiles numerically implausible and undocumented)
- Text: “top-1% score-knee cut S ≥ 0.2051,” and native continuity slice “S ≥ 0.1060.”
- Problem: S is defined as a per-survey z-score (Eq. 2). A 99th-percentile threshold of S ≈ 0.205 is highly atypical for a standardized residual (even allowing for heavy tails). Without the native SDSS (μval, σval) and the empirical S distribution summary, readers cannot tell whether S is truly standardized or whether these “S” values are on a different axis.
- Required fix: Report μval and σval for the SDSS native retrain, and tabulate median/95th/99th percentiles of S on the 1,925,279-spectrum pool. If S is not on a true z-scale for SDSS, rename the axis (e.g., S’), or explicitly state why the native S percentile cuts lie near 0.2. Do the same for the 4.05% continuity-slice threshold S ≥ 0.1060 to avoid misinterpretation.

P5–M11 (Section II.B.c; OOD “>50% flagged” claim lacks inputs)
- Text: “applying [S > 5] to a random uncurated SPARCL sweep flags > 50% of spectra (a catalog-curation effect, not a threshold artifact; see Table V caveat (b) for the full OOD reconciliation).”
- Problem: No sample size, μval/σval used, or basic distributional diagnostics are provided. This is used as a key justification for the DESI threshold behavior.
- Required fix: Provide the SPARCL sample size, the fraction flagged with binomial CI, and summary statistics of the OOD MSE (and S) distribution vs. the DESI in-catalog distribution. If this cannot be reproduced, soften or remove the quantitative “>50%” claim.

P14–M8 (Section IV.B; Cramér’s V denominator off-by-one in the displayed calculation)
- Text: “24,049 occupied HEALPix pixels … dof = 24,048; Cramér’s V = √(χ2/(N·(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.020.”
- Problem: You use 24,047 in the numeric denominator even though k − 1 = 24,048. This is a second, independent arithmetic mismatch in addition to the factor-≈3 error already flagged in the first review.
- Required fix: Use a consistent k − 1 factor (24,048) in both the dof and the V computation, and recompute V (and report the corrected value; see earlier essential finding for the magnitude error).

MINOR

P12–m6 (Appendix footnote for Planck injection; random-sign injections)
- Text: “Gaussian-bump … random sign and center … planted amplitude is exactly 5× the per-patch pre-injection noise standard deviation … 100% recovery.”
- Comment: Because MSE-based residuals are sign-insensitive, the random-sign convention does not invalidate recovery, but this is non-obvious. Add one sentence clarifying that sign is irrelevant under an MSE anomaly score, hence 100% recovery is not at odds with half of the injections being negative.

P7–m7 (Table I; mixed-rate presentation still risks misinterpretation)
- Text: Fixed-count/fixed-percentile tiers (Planck, Gaia, NEOWISE) are mixed with data-driven rates in the total rows.
- Problem: You note this in footnotes, but a casual reader can still misread the total-row “Rate.” 
- Required fix: Add an explicit “Not a measured rate” label directly in the “Rate (%)” cell of the total rows or move totals to a separate “bookkeeping only” line to prevent mis-citation.

P11–m8 (Table IV; eROSITA ranking key visibility)
- Text: Table shows SIF,raw but not the actual raw-score ranking key used to define the canonical top-298.
- Problem: For readers to validate ordering without fetching external artifacts, showing the actual sorting key (e.g., raw BigAE reconstruction score used in production) for these five rows would improve clarity.
- Suggestion: Add the committed raw-score value (the actual membership sorting key) alongside SIF,raw in Table IV (and in the full release table).

P8–m9 (Section III.A; DESI S-threshold back-of-envelope reproducibility)
- Text: “For DESI DR1 … μval ≈ 0.0287 … S > 5 at MSE ≈ 0.143.”
- Suggestion: Include σval explicitly (σval ≈ (0.143 − 0.0287)/5 ≈ 0.02286) for quick verification that the stated S-threshold maps to the quoted MSE.

P12–m10 (Planck tier; map-domain denominator clarification)
- Text: “Top-200 native anomaly patches … the 20,000-patch input quoted above (and as Ntotal in Table I) is the original cross-transfer patch budget … the native pipeline extracts 2 × 10^5 patches.”
- Problem: This is currently buried in a footnote-like paragraph.
- Required fix: Add an explicit parenthetical in the Planck row of Table I (“released tier selected from 200,000 native patches; Ntotal for historical cross-transfer comparability only”).

NIT

P16–N4 (Section IV.C; “none spans three or more surveys”)
- Text: “exactly 637 … none spans three or more.”
- Comment: Unusual but plausible. Consider adding a one-line table of “number of distinct surveys per multi-survey cluster” for transparency; otherwise readers may question whether triads were missed by the union-find settings.

P11–N5 (Figure 3 right; “ten orders of magnitude”)
- Text: The caption claims “more than ten orders of magnitude” from S = 5 to S = 1.9 × 10^11.
- Comment: That’s indeed ~10.6 decades; fine numerically, but consider mirroring this language in the body sentence that references the same extremes for easier consistency checking.

Explanation
I re-ran arithmetic checks on all easily verifiable quantities, traced caption/body consistency, re-checked equation dimensions, and scanned for stale denominators, off-by-one factors, and confusing scale definitions. The items above are new relative to my initial review; they focus on denominator consistency for processed totals, an undocumented and numerically implausible SDSS z-score percentile, an off-by-one in the Cramér’s V calculation, and a few clarity/robustness gaps that would otherwise invite misinterpretation.