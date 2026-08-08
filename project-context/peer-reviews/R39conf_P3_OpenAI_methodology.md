# P3 R39conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper3_anomaly_catalog.pdf` md5=8533c5a7 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7684 chars)
**Wall time**: 356.0s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies …”

Scope of review
I reviewed the full manuscript (29 pp.), all figures, tables, equations, and appendices. I audited quantitative claims (rates, fractions, σ’s, counts, overlaps), checked derivation chains and dimensional consistency, and verified that abstract and conclusions reflect what is supported in the body. Below I list all issues found, classified by severity, with page-level localization, the specific problem, and a required fix.

ESSENTIAL (paper cannot be accepted without these fixes)

P3-E1 (Sec. V.b, p. 18): Incorrect formula for F0 (missing square)
- Text: “Under the Fisher-positivity-respecting asymptotic form 1/σ2(fNL) = F0 + c α2 with F0 = 1/8.982 = 0.01239 …”
- Problem: 1/8.98 ≈ 0.111, not 0.01239. The stated numerical value 0.01239 corresponds to 1/(8.98)2. The algebraic expression must match the number.
- Required fix: Replace “F0 = 1/8.982 = 0.01239” with “F0 = 1/(8.98)2 = 0.01239”. Audit the manuscript to ensure every occurrence uses the squared baseline consistently.

P3-E2 (Sec. IV.B, p. 15): Cramér’s V miscomputed
- Text: “Cramér’s V = sqrt(χ2/(N·(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.020 …”
- Problem: The given expression omits the square root in the numeric evaluation. Using χ2 = 376,713, N = 378,280, k − 1 = 24,048 gives χ2/(N(k−1)) ≈ 4.14×10−5; taking the square root yields V ≈ 0.0064, not 0.020. As written, the numeric value is inconsistent with the displayed formula.
- Required fix: Recompute and report the correct Cramér’s V (≈ 0.0064) or explicitly justify a different statistic; ensure the formula, the numbers, and the interpretation are consistent. If a variant definition was intended, state it and adjust all numbers.

P3-E3 (Sec. V.b, p. 18): Numerical error in de-biasing term
- Text: “max(0, αˆ2 − σ2
α) = max(0, 0.192 − 0.652) = 0 …”
- Problem: αˆ2 = 0.19^2 = 0.0361, and σ2
α = 0.65^2 = 0.4225. The numbers 0.192 and 0.652 are incorrect.
- Required fix: Replace with “max(0, 0.0361 − 0.4225) = 0”. Check for any propagation of this typo elsewhere.

P3-E4 (Data availability, p. 23): Placeholders instead of actual archival identifiers
- Text: “will be made public with the arXiv posting … A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: PRD requires persistent, citable identifiers at acceptance. Placeholders are not acceptable.
- Required fix: Provide working DOIs (and/or SWHIDs) for the datasets, model weights, and code; include frozen commit hashes and file checksums that match the cited release. Remove all placeholder language.

P3-E5 (Table I, pp. 7–8 caption and table body): Ambiguous and inconsistent Ntotal for Path-C versus cross-transfer
- Text: The “Total (cross-transfer, ACT-incl.)” row lists Ntotal = 37,292,042. The “Path-C unique (primary)” row lists Ntotal = 37,272,042 (20,000 fewer), while the text elsewhere states the native Planck re-score used 2×105 patches (10× the cross-transfer 20,000).
- Problem: The Ntotal values in the Path-C row are carried over from the cross-transfer inputs (and subtract ACT’s 20,000), but the Planck native re-score used 200,000 patches not reflected in Ntotal. This mixes definitions within the same table and confuses what Ntotal represents for the primary results.
- Required fix: Either (a) replace Ntotal in the Path-C row with the actual processed counts for the native (primary) results (including 200,000 Planck patches), or (b) remove/relocate Ntotal from the Path-C row and add an explicit note that Ntotal is shown only for the cross-transfer baseline; provide a separate per-survey table listing native-run Ntotal. Ensure rate bookkeeping and captions clearly reflect which Ntotal is used.

P3-E6 (Table II footnote, p. 9): Internal tracker jargon in the main text
- Text: “… closes the FB103-1 / EXT9 denominator-reconciliation ask.”
- Problem: This is internal process language and must not appear in a PRD manuscript.
- Required fix: Remove internal tracker labels (“FB103-1”, “EXT9”) and rephrase in scientific prose.

P3-E7 (Abstract and throughout, pp. 1–2, multiple pages): Version-control file paths and “artifact … .json” labels in the main text without durable archival pointers
- Text examples: “artifact pipelines/p3_anomaly_engine/ext3_fm1_erosita_scaler_refit.json”; “r24conf_pod_session_batch.json”; “r23conf_dedup_audits.json”, etc.
- Problem: The manuscript relies on internal file paths and ephemeral labels (“r23conf”, “r24conf”) without stable archival identifiers. Such references impede reproducibility from the published record.
- Required fix: Move these artifacts to a public, versioned archive (e.g., Zenodo) and replace all in-text paths with standard references (DOIs, filenames, and checksums). Alternatively, consolidate them into a Supplementary Material with a single DOI. Remove all run-internal labels from the main text.

P3-E8 (Table I, p. 7): “SIMBAD-unmatched (%)” 58.8% in “Total (cross-transfer …)” row is not commensurate with the inputs
- Text: Total-row unmatched fraction 58.8% is quoted.
- Problem: The 58.8% aggregate was computed from a separate pooled top-100 per-survey exercise at 3″ on four surveys (Sec. IV.A), not from the “Total” cross-transfer set. Placing 58.8% in the “Total” row invites misinterpretation.
- Required fix: Remove the 58.8% from the Total-row cell or annotate it with a footnote placed directly in the table stating precisely how it was computed (top-100 of four surveys at 3″), and that it is not the unmatched fraction of the total row.

MAJOR (significant revision required)

P3-M1 (Sec. IV.C, p. 15): “Expected random coincidence is ≲10 across all survey pairs” lacks a quantitative derivation
- Text: “… the expected random coincidence contribution is ≲10 across all survey pairs against 637 observed …”
- Problem: No derivation, simulation, or reference is given. This is a checkable, load-bearing statement in support of the dedup-robustness claim.
- Required fix: Provide an explicit calculation or Monte Carlo simulation (with sky masks and source densities per survey) that yields the ≲10 figure, including uncertainties. Alternatively, remove the claim.

P3-M2 (Sec. V.a, p. 18): Insufficient methodological detail for the Landy–Szalay bias-ratio measurement
- Text: “Landy–Szalay … 30-region jackknife … θ ∈ [0.04°, 0.25°] … αjk = 0.19 ± 0.65 …”
- Problem: Critical details are missing: the exact sky mask, treatment of survey edges and completeness, integral constraint handling, cross-survey systematics (e.g., fiber-assignment for DESI), and the precise definition of “full anomaly” tracer used for normalization. Without these, the estimator and its uncertainties are not auditable.
- Required fix: Provide a full methodological specification: masks, random catalog construction, angular weights, binning, estimator definition, jackknife regionization, and validation tests (e.g., null tests and robustness to varying θ-ranges). Supply the number of randoms per tracer and demonstrate stability of αjk to binning and masking choices.

P3-M3 (Sec. V.b, p. 18; Appendix C, pp. 23–24): Derivation of c = 0.0747 not documented
- Text: “c = 0.0747 from the 5-α refit of §VI D caveat (i) …”
- Problem: The procedure to obtain c is not shown (no figure/table of the fit, no uncertainties).
- Required fix: Add a brief derivation: show the five α points, the fitted relation 1/σ2 = F0 + cα2, the resulting c with uncertainty, and a goodness-of-fit. Alternatively, move a plot/table to the Supplement.

P3-M4 (Sec. IV.A, pp. 13–14; Table I p. 7): Mixed radii and samples for SIMBAD unmatched fractions
- Text: Per-survey unmatched fractions reported at 5″, while the “aggregate 58.8%” is from a different pooled run at 3″.
- Problem: Although you note this in the text, the table and figure risk confusion. For a methods paper, harmonized definitions are expected.
- Required fix: Standardize the radius (5″) for all unmatched fractions or explicitly give both radii in a consistent side-by-side presentation with clear labeling. If retaining the 3″ pooled statistic, print it only in its own clearly labeled context.

P3-M5 (Sec. III.E, pp. 11–12; Table IV p. 12): eROSITA selection relies on an irreproducible score axis
- Text: “the selection is therefore best read as the fixed top-298 cap … per-object Table IV scores … axis is irreproducible; membership list itself is the committed, reproducible selection …”
- Problem: Primary catalog content is acceptable as a membership list only, but any analysis that depends on the eROSITA scores (thresholds, rank weights) is irreproducible.
- Required fix: Explicitly deposit the raw scoring artifact (the monotone axis used to form the top-298), with an archival pointer (DOI) and its exact sort order. Remove any use of the published SBigAE column for eROSITA analyses, and confine all eROSITA discussions to membership-only statements. Make this limitation prominent in the abstract and conclusions where eROSITA is mentioned.

P3-M6 (Sec. III.F, p. 12): Planck top-200 contains training-set patches; assess selection bias more rigorously
- Text: “152/200 in the training split, 48 in validation; p ≈ 4 × 10−4, opposite to memorization …”
- Problem: Although the direction argues against memorization, the selection is not held-out. A methods paper should quantify the potential bias introduced by including training data in the scored set (beyond the binomial count).
- Required fix: Provide a control in which you (i) retrain on a disjoint patch bank and re-rank the full set, reporting top-200 overlap, or (ii) score only the held-out validation split and report how the top-200 changes. Include a brief stability analysis.

P3-M7 (Table I caption, pp. 7–8; Abstract pp. 1–2): “Largest multi-archive anomaly search of which we are aware”
- Problem: This strong novelty claim should be supported by a broader literature scan (beyond [11]) or softened.
- Required fix: Either add citations to comparable-scale multi-archive anomaly searches showing your work is larger, or change to a softer phrasing such as “to our knowledge” and limit the comparative quantifier to the explicitly cited benchmark.

MINOR (address but paper can proceed)

P3-m1 (Sec. II.B, p. 4; elsewhere): Occasional missing exponent formatting (10^4 vs 104)
- Text examples: “≈ 2.2 × 104”; “10
4–10
11 tail …”
- Problem: In multiple places, exponents render as plain 104, which is ambiguous.
- Required fix: Ensure all scientific notation uses clear exponent formatting (10^4) throughout the PDF.

P3-m2 (Sec. IV.C, p. 15): RA-shift control for DESI×SDSS matches could be strengthened
- Text: “RA-only shifts … do not exactly preserve sky density … expected 2.75 …”
- Problem: You correctly caveat the RA-shift limitation. A simple great-circle rotation or shuffle within survey footprints would be more geometry-preserving.
- Required fix: Add a brief check with a rotation-scramble or footprint-aware randomization to confirm the 2.75 expectation is representative.

P3-m3 (Sec. III.A, p. 8): Wilson intervals quoted somewhat coarsely
- Text: “GALAXY 0.75% ± 0.02% (95% CI)”
- Problem: A quick calculation gives ±≈0.008% (normal approximation). Your ±0.02% is conservative but imprecise.
- Required fix: Either report exact Wilson intervals (with endpoints) or adjust the ± figures to reflect an accurate computation (and state the method used).

P3-m4 (Fig. 3 caption, p. 10): Extreme SDSS cross-transfer S values (10^11) deserve a one-line sanity note
- Problem: Even with cross-transfer scaling, S at 10^11 is extraordinary for a quantity standardized by a validation set.
- Required fix: Add a one-sentence note in the caption clarifying why such extremes are possible (DESI-trained scale applied to SDSS spectra completely out-of-distribution) and, if possible, cap axes in the main panel while showing the full range in an inset.

P3-m5 (Sec. III.H, p. 13): NEOWISE “mask-injection” test
- Problem: You already note this is a geometry QA and not a sensitivity test. Make that limitation explicit in the Figure 10 caption as well (currently it is, but a stronger parenthetical note “(not a detector sensitivity test)” would help readability).

P3-m6 (Data availability, p. 23): Code repository permanence
- Problem: GitHub URLs can change; PRD prefers archival mirrors.
- Required fix: Archive the code release (exact version used) to an immutable archive (e.g., Zenodo Software Heritage), include DOIs/SWHIDs, and the precise commit hash aligned to results.

NITS (cosmetic/editorial)

P3-n1 (General): The paper is long for the claimed contribution (29 pages with many run-path details in the main text).
- Recommendation: Move run-specific file paths, audit-artifact filenames, and secondary operational details to Supplementary Material. A 22–24 page main text would be more appropriate.

P3-n2 (Sec. II.B, p. 3): “z-scored” vs. redshift z
- You are already careful; consider consistently writing “standardized” in prose to avoid any residual ambiguity.

P3-n3 (Consistency): Ensure uniform use of arcsec notation (′′) and primes—already mostly consistent; fix any lingering plain quotes.

P3-n4 (Typos): Scan for small typographical slips (e.g., unmatched parentheses, occasional doubled spaces).

Abstract–body consistency audit (pattern-045)
- The abstract’s key numbers are traceable, with two exceptions fixed above:
  - DESI-only “~73×” vs. like-for-like recount “~0.9×” is properly caveated in body (Sec. III.A).
  - Novelty fraction 17.8% ± 1.2% appears in Sec. IV.A and is consistent.
  - Jaccard values (0.862, 0.732) and gate outcomes are supported.
  - fNL forecast σ = 8.14 with envelope [3.92, 8.98] is reproducible once F0 is corrected to 1/σ^2 baseline.
  - NANOGrav γ result (2.567 ± 0.382), σ-shifts, and Bayes factor are consistent with Appendix E.
- Required: Implement E1–E3 corrections; otherwise the abstract aligns with the calibrated statements in the body.

Provenance surfaces (patterns 046/047)
- Placeholders and internal labels (E4, E6, E7) must be resolved before acceptance.

Uncomputed quantitative claims (pattern-048)
- The ≲10 expected coincidences (M1) needs a computation or must be removed.

Standalone-reader test
- The narrative is largely self-contained for methods. Add the missing details for the Landy–Szalay setup (M2) and the c-fit (M3) to meet PRD rigor.

Effect-size statements (requirement 19)
- You provide an effect-size (Cramér’s V) but it is miscomputed (E2). Fix it and keep the caveat that footprint dominates.

Additional cross-checks performed
- Percentages and ratios: Verified DESI 195,829/22.5M ≈ 0.87%; SDSS cross-transfer 77,905/2,304,830 ≈ 3.38%; LAMOST 44,075/11,418,594 ≈ 0.39%; eROSITA 298/930,203 ≈ 0.032%; compression 10,213/388,493 ≈ 2.629%; NEOWISE polar-cap excess 17/436 ≈ 3.90% vs null 1.52% → ×2.57; novelty fraction 178/1000 = 17.8% with σ ≈ 1.21% (68%).
- σ comparisons: You consistently warn when quantities are not directly comparable (e.g., σ(fNL) vs NANOGrav γ in Conclusions bullet 5); keep these warnings after edits.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript is ambitious and generally careful, but several methodology-rigour issues must be corrected for PRD standards. The most serious are internal numerical inconsistencies (F0 missing square; Cramér’s V), placeholder provenance (absent DOIs), reliance on run-internal filenames in the main text, and insufficient methodological detail for the bias-ratio measurement and Fisher constant c derivation. The ambiguous Ntotal presentation in Table I also needs reworking to avoid confusion. Once these are addressed, and the minor clarifications applied, the work will be substantially strengthened for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E9 (Sec. IV.B, p. 15): Dust-correlation p-value inconsistent with plausible sample size
- Text: “no correlation with Planck dust intensity (Pearson r = 0.006, p = 0.21; proxy … HEALPix Nside = 64 … 24,049 occupied pixels).”
- Problem: If the correlation is computed across 24,049 pixels (as implied), t ≈ r√(n−2) ≈ 0.006×√24,047 ≈ 0.93 → two-sided p ≈ 0.35, not 0.21. If computed per-source (n ≈ 3.78×10^5), p would be ≪ 0.01 for r = 0.006. The reported p = 0.21 does not reconcile with either sample size.
- Required fix: State explicitly the sample on which r was computed (pixels vs. objects), give n, and recompute p accordingly. Ensure the body and caption use the same level (per-pixel vs per-object) and update text if the p-value changes.

P3-E10 (Fig. 2, p. 6 and body): Quarantined ACT DR6 anomalies shown in a main-text figure
- Text: “ACT DR6 points are shown for completeness … ACT DR6 is formally quarantined … contributes zero objects to the Path-C headline.”
- Problem: Displaying quarantined detections in a main figure invites misinterpretation, contradicting the paper’s own “not a science result” stance for ACT. PRD typically requires that non-science artifacts not be visually co-equated with results.
- Required fix: Move the ACT layer to an Appendix-only figure (Appendix F) or watermark/grey it and explicitly annotate “Quarantined (not part of catalog).” Add a caption note that the canonical Path-C map excludes ACT.

MAJOR

P3-M8 (Sec. II.B, pp. 3–4; Sec. III.G, p. 12): Train/test leakage in tabular scalers not fully mitigated; missing robustness checks for two surveys
- Text: For eROSITA, NEOWISE, Gaia, “scalers are fit on the full sample rather than the training split” (leakage acknowledged). A bounded robustness check is provided only for eROSITA; “corresponding checks for NEOWISE and Gaia remain queued.”
- Problem: Using full-sample scalers can alter tail rankings; without quantitative checks for NEOWISE and Gaia, catalog reproducibility and score stability remain unquantified.
- Required fix: Provide the same train-split-only vs full-sample-scaler robustness experiment for NEOWISE and Gaia (overlap, Jaccard at top-1%, Spearman ranks). Alternatively, re-train both with train-split-only scalers and report deltas to the released tiers.

P3-M9 (Sec. III.C, p. 10; Table III, p. 9): SDSS spectral-category assignment lacks reproducible rule specification
- Text: Ten categories are reported (e.g., “NIR excess,” “Unusual continuum,” “Artifact”), with fractions in Table III, but the rule set (residual-arm thresholds, line windows, decision tree) is not documented in the main text.
- Problem: Readers cannot reproduce the category census from the paper as written.
- Required fix: Specify, at minimum in Supplementary Material, the deterministic classification rules: per-arm residual definitions, thresholds, line-window masks, precedence/tying rules, and any SNR cuts. Include a small confusion table for quality control.

P3-M10 (Sec. V.A, p. 19; Appendix E, pp. 25): Bayes-factor robustness to prior and likelihood assumptions not shown
- Text: Bayes factors computed under a flat γ ∈ [0, 7] prior and a factorized KDE likelihood (inter-bin covariance neglected).
- Problem: BMB/SMBHB can be prior-sensitive and may change if modestly varying the prior (e.g., [0, 6], or weak Gaussian) or if mild inter-bin correlations are included/excluded.
- Required fix: Provide a sensitivity table/figure for BMB/SMBHB under at least two alternate priors (e.g., [0, 6], and a broad Gaussian centered at 3) and discuss any change in conclusions. If feasible, quote an uncertainty on the Bayes factor via posterior reweighting or bootstrap over KDE bins.

P3-M11 (Sec. III.A, p. 8): DESI headline still includes training spectra; a held-out only count is needed
- Text: “The DESI DR1 anomaly catalog is scored on the full 22.5M … which includes the 47,000 training spectra.” Cross-validation stability is reported, but no headline count excluding train members is given.
- Problem: Including training spectra can inflate the headline count if any training objects cross the S > 5 threshold.
- Required fix: Report the DESI S > 5 count excluding training spectra (and its fraction of the 22.5M), and the number of training spectra that satisfy S > 5. This does not replace the k-fold but complements it.

P3-M12 (Sec. IV.B, p. 15): “No correlation with Galactic latitude” — clarify unit-of-analysis and rate definition
- Text: “the anomaly rate shows no correlation with Galactic latitude (Spearman r = 0.0005, p = 0.92).”
- Problem: It is unclear whether the correlation is computed per object, per HEALPix pixel count, or per HEALPix rate (counts normalized by footprint/coverage). Without stating the denominator/weighting, the statistic is ambiguous.
- Required fix: State explicitly: correlation of what vs. what (e.g., per-pixel anomaly density normalized by survey exposure mask), sample size, and weighting. Recompute r and p at that level and document the mask/completeness treatment.

MINOR

P3-m7 (Sec. III.F, p. 12; Table VI footnote): Planck “range [0.558, 0.621]” MSE units not explicitly tied to standardized-patch convention
- Text: “Top-200 native anomaly patches (per-patch reconstruction-MSE … range [0.558, 0.621]).”
- Problem: Readers could misread these as raw K_CMB^2 units. While the footnote explains per-patch standardization, the body text omits the unit convention.
- Fix: Add “in standardized patch units (mean-subtracted, unit-variance per patch; see Table VI footnote).”

P3-m8 (Sec. III.H, p. 13; Fig. 10 caption, p. 22): Strengthen the “mask-geometry QA” caveat for NEOWISE
- Text: You note the pole-cap test “passes by construction.”
- Problem: The caption already mentions this, but a clearer parenthetical would prevent misreading it as a sensitivity test.
- Fix: Amend Fig. 10 caption to read “NEOWISE ecliptic-pole mask (PASS, by construction; geometry QA, not a detector-sensitivity test).”

P3-m9 (Sec. IV.C, p. 15): Radius-sweep sensitivity — add the shared Ntotal/Nunique context inline
- Text: 3″/5″/7″ sweep gives unique 378,604/378,280/378,145; compression 2.55%/2.63%/2.66%.
- Problem: Helpful but slightly terse for standalone reading.
- Fix: Add one sentence clarifying that all three runs use the same seven-input survey lists (canonical Path-C tiers) and the only change is the matching radius.

P3-m10 (Appendix B, p. 24): UMAP/HDBSCAN stability claims — provide seeds or DOI for the exact configuration
- Text: “trustworthiness 0.9797 ± 5×10^−5 across 20 independent seeds; kNN-preservation and cross-seed Spearman FAIL …”
- Problem: For reproducibility, the seed list or a pointer to the exact config would help.
- Fix: Provide the list of seeds or archive the config as a supplement and cite its DOI.

NITS

P3-n5 (Fig. 6 caption vs. bars): The dashed-line aggregate (3″ pooled top-100 per survey) coexists with per-survey 5″ bars
- Recommendation: Add “Per-survey bars computed at 5″; dashed-line aggregate at 3″ (pooled top-100 of four surveys).”

P3-n6 (Sec. II.B, p. 4): Notation nicety for per-arm residuals
- Recommendation: Clarify that rB, rR, rZ are mean absolute residuals (not z-scored), used only for within-object dominance calls, not cross-object significance.

Explanation
I focused on fresh arithmetic checks, figure/body consistency, unit-of-analysis clarity, and missing reproducibility details not covered in my first report. Most quantitative rates/ratios re-check, but I found a new p-value inconsistency (E9) and several methodological clarity/reproducibility gaps (M8–M12) that PRD typically requires before acceptance.