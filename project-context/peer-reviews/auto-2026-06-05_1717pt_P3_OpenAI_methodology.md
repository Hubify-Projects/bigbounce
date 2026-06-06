# P3 auto-2026-06-05_1717pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8829 chars)
**Wall time**: 411.0s

---

Referee report (methodology, statistics, internal consistency)

Overall scope
- I reviewed all 20 pages, figures, tables, equations, captions, and the abstract.
- I recomputed the principal rates, ratios, and sigma-level claims where inputs were given.
- The paper contains several methodological and internal-consistency issues that must be corrected before it can be considered for PRD. The most serious are a hard mathematical error in the Fisher “positivity-respecting” formula (misdefined F0), unresolved figure cross-references, an internally inconsistent “aggregate SIMBAD-unmatched” fraction, and a data/code availability plan that does not meet PRD standards.

Findings

ESSENTIAL

ID: P3-E1
Section V and Table IV (i); pages 10–11 and 13
Problem: Misdefinition of F0 in the Fisher “positivity-respecting” relation. The paper states “1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747.” If the single-tracer baseline is σstd = 8.98, then F0 must equal 1/σstd^2 = 1/(8.982)^2 ≈ 0.01240, not 1/8.982 ≈ 0.1113. The numerical results (σ = 8.14 for α = 0.19) in the text match F0 = 1/(8.982)^2, not 1/8.982, so the displayed formula is dimensionally wrong as printed.
Required fix: Replace every occurrence of “F0 = 1/8.982” with “F0 = 1/(8.982)^2” and audit every location where F0 is used or discussed (Section V text, Table IV (i), Appendix C) to ensure dimensional and numerical consistency. State explicitly that F0 ≡ 1/σstd^2.

ID: P3-E2
Section IV A (Fig. 5 and text); page 9
Problem: The “aggregate SIMBAD-unmatched fraction” is reported as 58.8% but is not reproducible from the shown per-survey fractions and counts, and the basis set is unclear (DESI “top 10k” vs. full DESI, inclusion/exclusion of ACT/Planck patches, weighting scheme). A weighted average using the numbers actually quoted in the paper (e.g., DESI top-10k at 99%, SDSS cross-transfer 90%, LAMOST cross-transfer 50%, eROSITA 68%, NEOWISE 45%, Gaia 27%) does not yield 58.8% under any obvious weighting.
Required fix: Provide the exact computation of the 58.8% value: which surveys, which sample sizes for each, the matching radius, whether duplicates were de-duplicated first, and the weighting. If this number is from a different pool than the bars in Fig. 5, state that explicitly and present the companion aggregate for the sample actually plotted, or remove the aggregate line.

ID: P3-E3
Section II B (definition of S) vs. Section III F (Planck); pages 2–3 and 6
Problem: The paper declares “Throughout this paper, ‘S’ refers without exception to the per-survey standardized (‘z-scored’) reconstruction residual.” Yet the Planck-native result reports “Top-200 native anomaly patches (score range [0.558, 0.621])” for a top-1% selection. For a standardized z-score, a top-1% tail typically lies at S ≳ 2.33; S ≈ 0.6 is inconsistent with the stated definition unless the “validation” population differs drastically from the scored population and produces a compressed scale. As written, it is unclear whether the Planck “score” is the same S or a raw/alternate metric.
Required fix: Clarify the Planck scoring scale explicitly: (i) confirm whether Planck scores are the same z-scored MSE S defined in Eq. (2), and if so, explain why the top-1% lies near S ≈ 0.6; or (ii) rename the Planck quantity to “raw MSE” (or another symbol) and do not call it S. In either case, add a histogram or descriptive statistics for the Planck score distribution to make the selection transparent.

ID: P3-E4
Multiple places; pages 2, 5
Problem: Unresolved figure cross-references: “Fig. ??” appears at least three times (architecture schematic; per-band residuals; DESI z≈6 cutouts). PRD cannot accept with unresolved references.
Required fix: Resolve all “Fig. ??/Table ??” placeholders with actual figure numbers and include the referenced figures in the PDF.

ID: P3-E5
Table I footnote for eROSITA; page 7
Problem: The footnote states “equivalent to S > 0.259 on the eROSITA-native IsolationForest raw-score axis,” conflating the canonical BigAE z-scored MSE S with the IsolationForest raw isolation score, which the paper elsewhere says lies on a ∼0–3.5×10^4 scale (Table III). Threshold “0.259” cannot be simultaneously on the IF-raw axis and be meaningful given that raw-IF scores are O(10^3–10^4).
Required fix: Correct the footnote to say the 298-source headline is defined on the canonical BigAE S axis (SBigAE > 0.259). If any IF-based cut is also used, state its numeric value unambiguously on the IF-raw scale and show the mapping or overlap explicitly.

ID: P3-E6
Abstract, Section V; pages 1, 10–11
Problem: Inconsistent improvement percentage. Using the corrected F0, α = 0.19, c = 0.0747 gives σ = 8.14. The fractional improvement relative to σstd = 8.98 is (8.98 − 8.14)/8.98 = 9.36%, not 7.9% as claimed in the abstract and Section V text.
Required fix: Update the stated improvement to 9.4% (or recompute c so that the central σ and the quoted percentage agree; do not mix an approximate linearization with the exact σ reported).

ID: P3-E7
Data and code availability; page 14 (Data availability)
Problem: The primary data/code are stated as “private pending arXiv acceptance; public upon acceptance.” This does not meet PRD reproducibility standards. Reviewers and readers must have access at acceptance time, with stable identifiers (DOIs) and immutable versioning.
Required fix: Deposit the catalog, training/validation splits, model weights, and all analysis scripts used to generate every figure/table into a public repository with a DOI (e.g., Zenodo, institutional archive) and include commit hashes and exact environment details. Alternatively, provide them as PRD Supplemental Material. Replace “private pending…” language throughout.

ID: P3-E8
Abstract and Section V; pages 1, 10–11
Problem: The “1σ envelope [3.92, 8.98]” for σ(fNL) is described as “1σ” in Section V, while Table IV (i) describes a “95% envelope [3.92, 8.98].” These cannot both be true. The endpoints [3.92, 8.98] correspond to α = 0.19 ± 0.65 inserted into the quadratic form, i.e., a ±1σ range on α under your prescription.
Required fix: Use a single, consistent labeling. If the envelope is derived from α ± 1σ, call it “1σ envelope.” If you intend a 95% envelope, recompute using α ± 1.96σ and report the resulting σ(fNL) range.

ID: P3-E9
Section IV A (novelty fraction); page 9
Problem: The “genuine novelty fraction” 17.8% for the DESI top-1,000 sample is a central number in the abstract, but the exact cross-match protocol is underspecified. The set of “20 curated all-sky catalogs,” the angular radii used per catalog, handling of multi-catalog duplicates, and false-match control are not documented in enough detail to reproduce the 82.2% archival-ID rate and the 17.8% residual.
Required fix: Provide a reproducible protocol: list all 20 catalogs (with versions), the matching radius per catalog, the de-duplication order, how multi-band positional systematics are handled, and an expected false-match calculation for the multi-catalog procedure. Include a machine-readable list of the 1,000 objects and their cross-match outcomes.

MAJOR

ID: P3-M1
Section V (Landy–Szalay bias measurement); page 10
Problem: The LS bias-ratio measurement lacks critical methodological details: exact footprint and mask, random catalog generation (size, angular selection function, veto masks), redshift distribution or angular-only treatment, treatment of systematics (depth, seeing, fiber assignment), and binning/jackknife geometry. Without these, αjk = 0.19 ± 0.65 and the derived Fisher inputs are not reproducible or auditable.
Required fix: Provide the full LS workflow: survey footprint, masks, randoms (generation and validation), pair-count codes, binning, jackknife regionization, and covariances. Include a schematic of the mask and a table of angular bins and measured w(θ) for both samples with errors.

ID: P3-M2
Abstract and Table I footnotes; pages 1, 7
Problem: “Catalog-grade subset is ∼265,000 unique objects” is not derived in the paper. The footnote says “the catalog-grade tier … is 264,938 unique objects” but defers the precise partition to a README in a companion repository.
Required fix: Include in the paper the explicit accounting that leads to 264,938: the per-survey native counts used, the deduplication overlaps removed (especially those involving LAMOST), and the resultant exact unique-object count. Present the number in the body, not only in an external README.

ID: P3-M3
Section II D and Table I; pages 3–7
Problem: Threshold heterogeneity and reuse of the same “77,905” count for SDSS both as a cross-transfer anomaly count and as the “native top-77,905 slice” are potentially confusing. It is not clear which SDSS set feeds the 7-way dedup and how comparisons are made across the mixed “S > 5.0” and “top-1% continuity” cuts.
Required fix: Standardize and tabulate, per survey: (i) the training and scoring pool sizes, (ii) the primary catalog cut used for dedup (S-threshold or fixed top-N), and (iii) the exact number of objects passed to dedup. For SDSS, explicitly state that the “top-77,905 native slice” is chosen to match the cross-transfer count for continuity, not because S > 5 identified that many, and confirm that this is the set used for the multi-survey dedup.

ID: P3-M4
Section III B; page 5
Problem: The SDSS “native re-score compresses the same objects to S < 14, eliminating the 10^4–10^11 tail.” This is a critical diagnostic, but no figure/table for the native SDSS S distribution is shown. The right panel of Fig. 2 is the cross-transfer distribution only.
Required fix: Add a panel (or a new figure) showing the SDSS native-retrained S distribution (same axes) so the claimed compression is visible and auditable.

ID: P3-M5
Section III H (NEOWISE) and Fig. 4; page 8
Problem: The top anomaly “Score = 11.5” uses the word “score” without specifying whether this is S (the z-scored MSE) or another metric. Ambiguity persists across several photometric-survey statements.
Required fix: State unambiguously for NEOWISE and Gaia whether “score” is S per Eq. (2) or an alternate detector output. If S, report the per-survey μval and σval values or provide a histogram to make the scale interpretable.

ID: P3-M6
Section V (SPHEREx forecast); page 11
Problem: The claim “SPHEREx 3–5σ detection of fNL = −35/8 is projected” is carried over from prior literature while this paper’s empirical α constraint is consistent with α = 0 at <1σ and the shot-noise discussion admits 15–30% Fisher-information penalties. The presentation risks overclaiming given the present work’s limited empirical support.
Required fix: Rephrase as a conditional/illustrative forecast clearly tied to assumptions (dense anomaly tracers, specific α, shot-noise penalties), and separate what is demonstrated here from what is projected under external assumptions.

MINOR

ID: P3-N1
Section III A; page 4
Problem: Duplicate content. The paragraph starting “Across the 6.5 million spectra in DESI DR1 that carry…” repeats material already stated immediately above (galaxy vs. QSO rates, peak redshifts, Z-dominant top anomalies).
Required fix: Remove redundancy or consolidate into a single clear paragraph.

ID: P3-N2
Introduction; page 2
Problem: Awkward range “Sections II–II D describe the method.”
Required fix: Replace with “Sections II A–D describe the method” (or “Section II”).

ID: P3-N3
Notation; multiple pages
Problem: Nonstandard character rendering such as “˚A” for Å appears a few times (wavelength ranges).
Required fix: Use proper Å symbols consistently.

ID: P3-N4
Bibliography note [33]; page 19
Problem: In-text note “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity” is internal bookkeeping language that should not appear in a PRD manuscript.
Required fix: Remove the bracketed remark; cite the paper in standard format.

ID: P3-N5
Section III F; page 6
Problem: ACT DR6 appears in the legend of Fig. 1 while being quarantined, which is fine, but ensure that every place ACT appears in figures/tables is clearly labeled as “cross-transfer diagnostic only; not part of Path-C results” to prevent misinterpretation.
Required fix: Verify all occurrences are clearly labeled (Fig. 1 is fine); add a caption clarifier wherever else ACT appears.

ID: P3-N6
Section IV C; page 10
Problem: “Expected random coincidence contribution is ≲ 10 across all survey pairs against 637 observed multi-survey clusters” has no derivation in text.
Required fix: Add a one-line derivation or reference to a supplemental note (assumed sky area, surface densities, match radius, pair counting).

NIT

ID: P3-T1
Typos and style; multiple pages
- “galactic-plane-masked (|b| ≥ 20◦)” should be “Galactic-plane masked.”
- “Rosatom proprietary control” is unnecessary editorializing; shorten to “under proprietary control.”
- Ensure consistent spacing around units and multiplication signs (e.g., “1.1 × 10^6 parameters”).
Required fix: Copy-edit throughout.

ID: P3-T2
Figure labeling checks
- Fig. 2 left/right axes are labeled; units and thresholds are clear. For completeness, add “Probability density” normalization method in caption (kernel/histogram).
Required fix: Minor caption additions.

Arithmetic and consistency checks (selected)

- DESI anomaly rate: 195,829 / 22,504,897 = 0.00870 = 0.87% (consistent).
- LAMOST cross-transfer rate: 44,075 / 11,418,594 = 0.00386 = 0.39% (consistent).
- LAMOST rate compression at S > 5: 44,075 / 2,054 = 21.46× (consistent with “21.5×”).
- SDSS cross-transfer vs S > 5 native: 77,905 / 12 ≈ 6,492× (consistent with “∼6500×”).
- Sum of native-retrained survey-level counts (excluding ACT): 388,493; minus 10,213 duplicates = 378,280 (consistent).
- Dedup compression: 10,213 / 388,493 = 2.629% (consistent).
- NEOWISE mask retention: 419/436 = 96.1% (consistent). Polar-cap excess: 3.9% / 1.52% = 2.57× (consistent with “2.6×”).
- False-match estimate for SIMBAD at 5″: π(5″)^2 × 3.0×10^−5 arcsec^−2 ≈ 2.36×10^−3 per source; ×195,829 ≈ 462 (consistent with “∼460”).
- NANOGrav σ-levels: (3.00−2.567)/0.382 = 1.13σ; (4.33−2.567)/0.382 = 4.61σ (consistent).
- Bayes factor: 3.23 / 4.52×10^−4 ≈ 7.14×10^3; log10 B ≈ 3.85 (consistent).
- Fisher central σ for α = 0.19 using corrected F0 and c: σ = 8.14 (consistent), but the stated “7.9% improvement” is not.

Length and focus

- The paper is long (20 pages) relative to the core methodological contribution. If the primary claim is the construction of the Path-C catalog and its validation protocol, consider moving several extended application sections (PTA MCMC Appendix E, some of Appendix D galleries) to a supplementary document to keep the PRD manuscript within ~15 pages, focusing on methods, validation, and the essential cosmology forecast.

Summary recommendation
MAJOR REVISIONS

Justification: The manuscript contains a critical mathematical misstatement (F0) in the key Fisher relation, unresolved figure references, an internally inconsistent central novelty statistic (58.8% aggregate), and insufficient methodological detail for reproducing the LS bias-ratio measurement and the 17.8% novelty fraction. Data/code availability as stated does not meet PRD standards. These are fixable, but they must be corrected and documented rigorously.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

ID: P3-E10
Table V vs. Section II B; pages 15 and 2–3
Problem: Implausible/incorrect training times. Table V lists “Train time (s)” as 10.6 s for the 1.1×10^6–parameter Planck CAE trained on 2×10^5 patches, and similarly tiny times for other surveys, while Section II B states training up to 200 epochs with early stopping. Training 200k 64×64 patches cannot complete in 10.6 s. This appears to conflate inference times, per-epoch times, or placeholder numbers with wall-clock training.
Required fix: Report true wall-clock training times per survey, with number of epochs, batches, and dataset sizes. If times are per epoch or for a small subset, label them explicitly. Ensure consistency with the “up to 200 epochs” schedule.

ID: P3-E11
Fig. 9 vs. Section III B; pages 17 and 5
Problem: “AE” values in Fig. 9 are numerically incompatible with the stated meaning of per-band residuals. The text says panel labels report the Z-arm sub-score rZ (typical ⟨rZ⟩ ≈ 3.9 for the z≈6 candidates), but the figure shows AE values up to 83,518 for DESI anomalies, which is impossible for either S or any per-arm standardized residual on the DESI-native scale. Units are undefined and contradict the text.
Required fix: Clarify what AE in Fig. 9 actually denotes, ensure it matches a defined quantity (rZ or S) on a consistent scale, and correct the numeric values and caption accordingly.

ID: P3-E12
Section V, Fig. 8, Appendix C; pages 10–11 and 16
Problem: Inconsistent σ(fNL) baselines used without clear comparability. The main text uses σstd = 8.98 as the single-tracer baseline, while Fig. 8 introduces “baseline multi-tracer = 12.72,” “ideal (dense) = 11.71,” and “single-tracer baseline = 16.85,” with no statement that these refer to different survey/tracer configurations. Mixing these baselines alongside the 8.98 baseline invites misinterpretation.
Required fix: Add a table summarizing each σ baseline (input samples, tracer sets, redshift bins, volumes, shot noise assumptions), and explicitly state in text that these baselines are not directly comparable.

ID: P3-E13
Section IV B; page 10
Problem: HEALPix pixel count/dof mismatch. For Nside = 64, Npix = 49,152, yet the test is reported “across 38,330 HEALPix pixels (Nside = 64), dof = 38,329.” The mask/footprint selection that reduces 49,152 to 38,330 is not described, so dof and χ^2ν cannot be reproduced.
Required fix: Specify the exact sky mask/footprint used, the number of retained pixels, and how dof was computed. Provide the list or a bitmap of the unmasked pixels.

ID: P3-E14
Section IV D; page 10
Problem: Planck × ACT cross-correlation “null result” lacks methodology. No estimator, masks, matching resolution, or significance calculation are provided. Given the strong claim that systematics dominate, the null needs a documented test.
Required fix: Describe the cross-correlation procedure (map pixelization, masks for each experiment, estimator, null tests, and uncertainty), and show the measured cross-correlation with error bars or a p-value.

MAJOR

ID: P3-M7
Section III C, Table I; pages 6–7
Problem: The reused SDSS count “77,905” yields inconsistent percentages. Cross-transfer rate 77,905/2,304,830 = 3.38% (as printed). The “top-77,905 native slice” comes from 1,925,279 spectra, i.e., 4.05%, but this rate is not stated and can be mistaken for the 3.38% figure.
Required fix: State the native-slice rate explicitly (77,905/1,925,279 = 4.05%) and clearly distinguish cross-transfer vs. native denominators anywhere “77,905” appears. Confirm which set feeds the 7-way dedup (this complements P3-M3 but focuses on the rate arithmetic).

ID: P3-M8
Table I footnote (§VI D (v)) vs. methods; pages 7 and 12–13
Problem: Gaia cross-validation uses a “10×-expanded 500,000-source sample,” while the main Gaia input is 50,000 sources. The construction of the 500,000-sample (selection, features, contamination assumption) is not described in methods.
Required fix: Document how the 500,000-source Gaia sample was built (data release, features, selection cuts), the contamination prior used for IF refits, and how it relates to the 50,000-source set.

ID: P3-M9
Section II D (Step 6), §IV C; pages 3 and 10
Problem: Fixed 5″ dedup radius across heterogeneous surveys (e.g., eROSITA, NEOWISE, Gaia) is not justified relative to survey-specific astrometric uncertainties. A uniform 5″ may under-merge true matches (eROSITA) and over-merge crowded fields.
Required fix: Justify 5″ per survey pair or adopt per-survey error-aware/probabilistic matching. Quantify expected missed/false merges and their effect on the 637 multi-survey coincidences.

ID: P3-M10
Section II B vs. Section II D (Step 1); pages 2–3
Problem: Gate definition vs. training schedule inconsistency. Step-1 gate requires ≤100 epochs for criterion (a), while Section II B says training runs “up to 200 epochs.” It is not shown whether each native retrain met the ≤100-epoch gate.
Required fix: Report the actual epoch counts per survey and confirm whether criterion (a) was satisfied within ≤100 epochs, or clarify that early stopping within 200 epochs is permitted and update the gate wording.

ID: P3-M11
Section III B; page 5
Problem: The z ≈ 6 QSO-candidate redshifts (6.0–6.23) are quoted without a documented redshift-measurement procedure (which lines, fitter, uncertainties, and QA). Given their prominence, this must be reproducible.
Required fix: Provide the redshift measurement method (line IDs, fitting code, priors), uncertainties per object, and a small table listing TARGETIDs, positions, z±σ, and line flags.

MINOR

ID: P3-N7
Fig. 2 (right) and caption; page 5
Problem: “Spanning twelve orders of magnitude from S = 5 to S = 1.9×10^11” is overstated. 1.9×10^11 / 5 ≈ 3.8×10^10 (≈10.6 orders).
Required fix: Correct to ~10.6 orders of magnitude (or rephrase as “∼11 orders”).

ID: P3-N8
Table IV (b) cross-reference; page 13
Problem: Table IV (b) says “reconciled in §II,” but the text points to §VI D (b) for the OOD reconciliation. Misleading pointer.
Required fix: Change the reference to §VI D (b), or add the reconciliation detail to §II and keep both references consistent.

ID: P3-N9
Figures of record
Problem: Fig. 1 maps the 319,443 cross-transfer baseline (including quarantined ACT in the legend) rather than the final Path-C 378,280 set. This can confuse readers about what is “the” catalog geometry.
Required fix: Add a companion figure showing the final Path-C anomalies, or clearly label Fig. 1 in the caption and body as “baseline diagnostic only; not the final result.”

ID: P3-N10
Notation overload; multiple places
Problem: “AE” is used for both the model name (BigAE) and, in figures/text, to denote a per-band residual label. This risks confusion.
Required fix: Reserve “BigAE” for the model and use rB, rR, rZ (or another explicit symbol) for per-band residuals in all figures/captions.

ID: P3-N11
Section IV A (b); page 9
Problem: SIMBAD surface density nSIMBAD ≈ 3.0×10^−5 arcsec^−2 used in the false-match estimate is not sourced.
Required fix: Cite the source or show how nSIMBAD was measured for the relevant sky region, or add a supplemental note.

ID: P3-N12
Section III A; page 4
Problem: SNR–score independence: the 2,670-spectrum subsample selection (“log-uniform in SNR”) and binning are not shown.
Required fix: Add a brief methods sentence or a small figure describing the SNR subsample construction and the test setup.

NIT

ID: P3-T3
Appendix E (Eq. E1); page 16
Problem: Dimensional clarity. The logarithmic template mixes A, frequencies fi, fyr, and Tobs; units/norms are not all specified, making dimensional consistency opaque.
Required fix: Define A and the frequency units explicitly (e.g., fi in Hz, fyr = 1 yr−1 in Hz, Tobs in seconds or years with the appropriate normalization) so all logarithms are of dimensionless quantities.

ID: P3-T4
Table I presentation; page 7
Problem: Mixed use of cross-transfer and native slices without a parallel “native rate” column where counts are re-used (e.g., SDSS 77,905).
Required fix: Add a column that reports the rate for the actual set fed into dedup (native or cross-transfer as applicable), to prevent denominator confusion.

Explanation
These issues were not covered in my initial review and mainly concern unrealistically small training times, a mislabeled/inconsistent figure quantity (AE), mixing of multiple σ(fNL) baselines without stating comparability, an undocumented mask underlying the HEALPix χ2 test, lack of method for the Planck×ACT null, arithmetic overstatement in Fig. 2, cross-reference and rate-denominator inconsistencies, undocumented Gaia sample expansion, fixed 5″ matching across heterogeneous astrometry, a missing redshift-measurement protocol for the z ≈ 6 candidates, and minor clarity/notation points.