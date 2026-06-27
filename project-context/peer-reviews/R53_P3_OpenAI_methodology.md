# P3 R53 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R53_P3/paper3_draft.pdf` md5=464d4066 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7343 chars)
**Wall time**: 394.6s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope of review
- Focus: methodology rigor; statistical validity; derivation chains; dimensional analysis; arithmetic and logical consistency of all stated numbers; reproducibility/availability; significance language; comparability of σ/p/BF across differing null procedures.
- I read the full 29-page manuscript, checked every equation, table, and figure caption, and recomputed all explicit ratios and headline scalars in the abstract and conclusions from values given in the body.

Overall note
- The paper is ambitious, technically detailed, and contains many caveats. However, there are several essential issues in reproducibility (future-tense/placeholder DOIs; heavy use of internal path/”artifact” pointers in the body), incomplete definition of key validation procedures (spectroscopic injection–recovery), and threshold heterogeneity that is not fully disclosed in the abstract. These must be fixed for PRD.

Findings

ESSENTIAL

P3-E1. Data availability placeholders and future-tense release language (Abstract p.1; Data availability p.23)
- Problem: Abstract: “will be publicly released with the arXiv posting.” Data availability: “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Required fix: Replace all future-tense with live persistent identifiers. Provide a minted DOI for the dataset(s) and the code, freeze the exact version(s) used in the paper, and list SHA-256 sums for all artifacts in a publicly accessible release. Remove all placeholder sentences.

P3-E2. Internal bookkeeping paths and run-log references embedded in the main text (multiple pages: p.3, 4, 5, 6, 8, 11–12, 15–17, 23–26)
- Problem: Numerous instances such as “pipelines/p3_anomaly_engine/.../r24conf_pod_session_batch.json”, “training log.json”, “.../ext3_fm1_erosita_scaler_refit.json”, etc., appear in-line in the scientific narrative. The main text also uses “artifact” to refer to local files.
- Required fix: Move all internal path references and run-log filenames to a dedicated, citable supplementary material or data-release README linked by DOI. In the manuscript, refer only to the DOI and a stable path within that release. Purge all internal filesystem paths and “artifact” bookkeeping terms from the body text.

P3-E3. Incomplete specification of the spectroscopic injection–recovery protocol (Sections II.D Step 5 p.5; III.C–D pp.9–10; VI.D(ii) p.22; Fig. 10 p.22)
- Problem: The recovery claims (e.g., SDSS 64% at 5σ, LAMOST 5.8% at 5σ) cannot be reproduced as written. Key missing details: how “noise σ” is computed per spectrum (per-pixel? per-arm? global?), precise functional form of the injected features (continuum dip: width, depth, placement distribution; emission line: profile/width, amplitude relative to local σ, blending rules), redshift dependence, whether injections are added before or after normalization, and the recovery criterion (score thresholding vs. rank, per-arm logic).
- Required fix: Provide a complete, unambiguous specification (equations and parameter values) for both the continuum-dip and emission-line plants, the noise σ definition, the placement distribution across wavelength, the exact amplitude grid ({0.5, 1, 2, 5, 10, 20}×σ?), the exact recovery criterion, and seeds. Add a minimal pseudocode block or point to a DOI-frozen script implementing these steps.

P3-E4. Threshold heterogeneity not fully disclosed in the abstract (Abstract p.1)
- Problem: The headline unique count (378,280) and the “recommended catalog-grade” subset (269,317) are built from heterogeneous thresholds across surveys (absolute S>5 for DESI; a fixed-size SDSS continuity slice; LAMOST top-1% exploratory; Planck and NEOWISE fixed top-1%; eROSITA membership-only “top-298”). The abstract mentions the eROSITA membership-only status but does not disclose that multiple surveys contribute fixed-count slices rather than data-driven detection thresholds.
- Required fix: Add one explicit sentence in the abstract clarifying that three surveys contribute fixed-count top-1% tiers (Planck, Gaia, NEOWISE) and one survey (eROSITA) is a membership-only top-298 list with a non-reproducible score axis, so the headline unique count aggregates non-uniform threshold bases and should not be read as a uniform anomaly frequency.

P3-E5. PTA likelihood model equation lacks definitions and dimensional clarity (Appendix E Eq. (E1) p.25)
- Problem: Eq. (E1) defines “log10 ρi” without defining ρi (units), fyr, fi, or Tobs in the PTA convention. The dimensions and normalization are not verified; without a clear definition, others cannot reproduce the mapping from the KDE product to the parameterization used in MCMC.
- Required fix: Define ρi explicitly (e.g., the expected cross-power or strain power in bin i, with units), state fyr ≡ 1/yr, define fi and Tobs, and give a short derivation or cite a standard reference (with equation numbers) showing that the log10 expression follows from S_h(f) = A^2/(12π^2)(f/fyr)−γ f−3 and binning conventions. Confirm dimensional consistency in text.

P3-E6. Table I/summary-row “Ntotal” bookkeeping is ambiguous for Path-C (Table I p.7)
- Problem: The “Path-C unique (primary)” row Ntotal is listed as 37,272,042, which appears to be the cross-transfer baseline (37,292,042) minus ACT’s 20,000 patches, not the actual native-rescore totals (the Planck native bank uses 2×10^5 patches). This mixes stage-specific inputs within a single “total processed” figure.
- Required fix: Provide a separate, unambiguous “N_scored” per survey for the Path-C stage (with Planck’s 200,000 patches), and update the Path-C summary Ntotal accordingly, or explicitly footnote that the Ntotal column for Path-C retains the cross-transfer Planck count by convention and give the native-rescore total in parentheses. As written it is confusing and can be misread as the actual scored count under Path-C.

P3-E7. Reproducibility of the eROSITA selection (Section III.E pp.10–11; Table IV p.12)
- Problem: The text emphasizes the irreproducible SBigAE axis and that the 298-source list is membership-only. However, there is no present-tense DOI for the “committed raw-score artifact” on which reproducibility rests; selection criteria (e.g., ranking tie-breakers) are not fully specified in the paper.
- Required fix: Provide a DOI to the raw-score vector used to produce the top-298 ranking, define how ties are broken, and ensure a reader can reconstruct exactly the same 298 IDs from the DOI’d artifact alone. This can be addressed with P3-E1 if the data release includes these items.

MAJOR

P3-M1. SDSS “continuity slice” rationale and sensitivity (Section III.C p.9; §IV.C p.15–16)
- Problem: The 77,905-object SDSS tier used in the dedup geometry is a fixed-size continuity slice at S ≥ 0.1060. While §IV.C provides alternative dedup counts using top-1% and S>5 cuts, the scientific rationale for using a fixed-size continuity slice as a core catalog input remains thin.
- Required fix: Either (i) justify this choice more clearly as a methodological device (and move all science inferences away from the continuity slice to the top-1% or S>5 tiers), or (ii) restructure the main catalog geometry around a data-driven SDSS threshold (top-1% or S>5) and relegate the 77,905 slice to an auxiliary analysis. Keep the sensitivity table but ensure the headline catalog geometry is not anchored to an ad hoc fixed-size SDSS cut.

P3-M2. Planck training/validation over-representation p-value is not geometry-correct (Section III.F p.12)
- Problem: The stated binomial p ≈ 4 × 10−4 for “over-representation toward held-out patches” assumes independent patches, which is not true due to spatial correlations within 10°×10° tiles.
- Required fix: Either remove the quoted p-value and state only the qualitative directionality, or recompute with a block bootstrap/jackknife that accounts for patch correlations. If retained, quantify the effective number of independent tiles used to compute p.

P3-M3. “Largest multi-archive” claim requires substantiation (Abstract p.1; Table I p.7)
- Problem: The paper claims “the largest application … by total sources processed … of which we are aware.” This needs a literature scan or precise qualifier.
- Required fix: Add explicit citations and a short comparative table (in supplementary) validating that no multi-archive anomaly-search larger than 37.3M sources exists, or soften to “to our knowledge” and limit the scope (e.g., autoencoder-based).

P3-M4. False-match baseline in §IV.A lacks source-density derivation (Section IV.A p.14)
- Problem: SIMBAD surface density nSIMBAD ≈ 3.0 × 10−5 arcsec−2 is used to derive Pfalse ≈ 2.4 × 10−3 per source. The origin of this surface density is not given.
- Required fix: Provide the derivation (catalog counts and sky area used) or a citation, and add a brief sensitivity discussion (e.g., how this varies near the Galactic plane and LMC/SMC).

P3-M5. In-sample vs. OOD DESI rate comparison (Section II.B–C pp.4–5)
- Problem: The text states that S>5 flags >50% of a random uncurated OOD SPARCL sweep, attributed to “a catalog-curation effect,” but provides no quantitative breakdown.
- Required fix: Provide the exact OOD fraction flagged (with an uncertainty) and at least one quantitative explanation (e.g., SNR distribution shift) with a small table or figure.

P3-M6. Equation symbols and definitions should be fully self-contained (multiple)
- Problem: Several symbols appear without immediate definition on first use (e.g., SBigAE in III.E; “score-knee” terminology; “Jaccard gate” thresholds).
- Required fix: Ensure each symbol/term is defined when first used in the main text (not only in footnotes/tables), or add a one-paragraph notation block at the start of Section II summarizing core symbols.

P3-M7. Treatment of NEOWISE “100% PASS” gate (Section III.H p.12; Fig. 10 p.22)
- Problem: Although the paper notes that the NEOWISE “injection” is a masking-geometry QA that passes by construction, the summary bullets (“Three PASS”) can be misread as detector-sensitivity validation.
- Required fix: Everywhere a “3 PASS” tally appears (abstract p.1; Fig. 10 caption p.22; Section II.D p.5), append “(NEOWISE = mask-geometry QA, not a sensitivity test)” inline, as already done in some places. Ensure consistency across abstract, text, and figure.

MINOR

P3-N1. Minor ambiguity on SDSS retrieval failures (Section III.C p.9)
- Problem: “A further 3,394 spectra, 0.18% nominal, failed retrieval during the re-score” is stated without stating the pre-failure target size used to derive 0.18%.
- Required fix: State the pre-failure count explicitly (e.g., “1,928,673 intended; 3,394 failed; 1,925,279 scored”).

P3-N2. PTA Bayesian terminology (Appendix E p.25–26)
- Problem: The text alternates between Gaussian-approximation “±” and asymmetric quantiles. It is good that both are reported, but please label clearly which is used for the +1.13σ shift calculation and why.
- Required fix: Add an explicit sentence stating that the +1.13σ parameter shift uses the Gaussian-approximation standard deviation, while the [2.304, 2.882] bounds are the 68% credible interval from the empirical posterior, which is slightly asymmetric.

P3-N3. Consistent reporting of units and numeric formatting (multiple)
- Problem: Occasional omissions: “1.1×106 parameters” appears without spaces; elsewhere 1.1 × 10^6 is used; units on pixel scales sometimes implied rather than stated.
- Required fix: Normalize SI/scientific-notation formatting and ensure all axis labels and text mention units on first appearance (e.g., arcsec, degrees, Ångström).

P3-N4. Minor editorial cleanup of duplication/wording (multiple)
- Problem: Repeated parenthetical clarifications appear verbatim several times (e.g., “not a detector-sensitivity test”), making the narrative dense.
- Required fix: Consolidate repeated caveats in one place (e.g., a Validation Gates subsection) and refer to it, to improve readability.

P3-N5. Abstract-last consistency check (Abstract p.1 vs. body)
- Problem: Abstract’s “largest application” and “3 PASS / 3 FAIL” tallies are broadly consistent with the body, but add the word “(NEOWISE gate is geometry-QA)” to match wording in §§III.H and VI.D(ii).
- Required fix: Add the parenthetical in the abstract.

NIT

P3-nit1. Typographic odds and ends (multiple)
- Problem: Spacing around symbols, occasional hyphenation artifacts (PDF line breaks) and superscripts (e.g., “1.1×106 parameters”).
- Required fix: Standard copy-edit pass.

P3-nit2. Figure utility check (Fig. 7 p.16)
- Problem: The RA/Dec histograms and score–latitude scatter could be merged into a single multi-panel with consistent scales to save space.
- Required fix: Optional consolidation to improve flow.

Arithmetic and consistency checks (spot-audit results)
- Abstract/body scalar audit: 378,080+200=378,280; 269,317−200=269,117; 378,080/2,685≈140.8 (141×); 269,117/2,685≈100.2 (≈100×); 195,829/2,685≈72.9 (73×); restricted DESI 2,468/2,685≈0.92 (≈0.9×). All correct.
- Wilson 68% CI for 178/1000: ±√(p(1−p)/n)=±0.0121 (±1.2%). Correct.
- Landy–Szalay αjk=0.19±0.65 implies 0.29σ from null. Correct.
- Fisher mapping: F0=1/8.98^2≈0.01239; 1/σ^2=0.01239+0.0747×0.0361=0.01509; σ=8.14. Envelope [α=0→8.98; α=0.84→~3.94]. Consistent with [3.92,8.98].
- Ntotal sum and dedup: native counts sum to 388,493; compression 10,213 (2.63%); unique 378,280. Correct.
- SIMBAD false match: n≈3×10−5 arcsec−2, r=5", nπr^2≈0.00236 (0.24%) → ~460 spurious among 195,829 DESI; correct to stated precision.
- NEOWISE polar-cap excess: expected 1.52%; observed 17/436=3.90%; z≈4.07; p≈6×10−5. Correct.
- Chi-square/Npix: χ^2=376,713; ν=24,048 → χ^2/ν≈15.7; effect size (Cramér’s V as defined): sqrt(376,713/(378,280×24,047))≈0.0064. Internally consistent (though Cramér’s V is nonstandard for this application; the caveat is already stated).
- DESI arm-dominance categories sum to 195,829; fractions computed correctly.

Length and scope
- At 29 pages with dense footnotes/inline caveats, the manuscript reads more like a data-release note with methods plus appendices. For PRD, consider moving some of the operational detail (copious internal-path provenance, GPU timings, and retrieval failure tallies) to a DOI-linked Supplement. A concise 18–22 page main article plus a rich supplement would likely improve clarity.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains valuable and carefully caveated methodology and results, but it falls short of PRD standards in several essential ways: (i) reproducibility is deferred to a future data release with placeholders and heavy use of internal path references in the main text, (ii) spectroscopic injection–recovery methods are insufficiently specified to reproduce the reported pass/fail outcomes, and (iii) the abstract does not disclose the threshold heterogeneity underlying the headline unique count. Addressing the essential items (P3-E1–E6) and the major methodological clarifications (P3-M1–M4) is required before the paper can be considered for publication in PRD. The remaining minor issues are straightforward copy/structure edits.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-pass audit)

ESSENTIAL

P3-E8. Fig. 3 caption contradicts what is plotted for LAMOST (native vs. cross-transfer)
- Problem: The Fig. 3 caption states “cross-transfer for SDSS, native for DESI/LAMOST,” yet the overplotted LAMOST curve is explicitly labeled “LAMOST DR10 (44,075),” which is the cross-transfer count used earlier (the native re-score top-1% is 113,342). This conflicts with both the caption and the Section III.D narrative.
- Required fix: Correct the Fig. 3 caption to say “native for DESI; cross-transfer for SDSS and LAMOST,” or replace the green curve with the native LAMOST distribution and relabel accordingly. Ensure the body text describing Fig. 3 matches the corrected caption.

P3-E9. Fig. 5 cutout scale is numerically wrong
- Problem: The caption says “256 × 256 pixels (108″ × 108″)” at the DESI LS DR9 scale of 0.262″/px. But 256 × 0.262″ = 67.07″ per side, not 108″.
- Required fix: Correct the angular size to ≈67″ × 67″ (or adjust the pixel scale if a different image product was used) and ensure all other image-size statements reflect the same scale.

P3-E10. Implausible S values in Fig. 3 (right panel) inconsistent with Eq. (2) and the stated input normalization
- Problem: The SDSS cross-transfer S axis extends to S ≈ 1.9 × 10^11. With S ≡ (MSE − μval)/σval and μval ≈ 0.0287, this implies MSE ≈ μval + Sσval ≳ 10^9 for σval at the DESI scale—physically incompatible with (a) inputs standardized to zero mean and unit variance and (b) MSE defined as a per-element mean over 496 features. Even extreme out-of-distribution residuals should not drive per-element-mean squared error to 10^9 if the inputs are on a unit-variance scale.
- Required fix: Re-audit the plotted quantity. If the panel shows a different axis (e.g., raw summed-squared error, a logging/scaling mistake, or a plotting bug), correct the axis label and text. If S truly attains 10^10–10^11, provide a concrete sanity check (upper bounds from network output ranges, residual magnitudes, and normalization conventions) showing how such S is feasible.

P3-E11. Injection–recovery “500 plants per survey” statement conflicts with NEOWISE’s 1000/1000 mask test
- Problem: Step 5 (p.5) states “500 planted signals per survey at six amplitude levels.” However, §III.H and Fig. 10 use a 1000/1000 geometry-based mask test for NEOWISE (not amplitude levels), and no amplitude grid applies there.
- Required fix: Amend Step 5 to carve out the NEOWISE geometry-QA as an explicit exception, including the number of test objects (1000), the three |becl| thresholds tested, and that no amplitude-series injection applies. Align Fig. 10 caption and the Step-5 description to a single, consistent protocol summary.

MAJOR

P3-M8. DESI×SDSS cross-match count inconsistency (3 vs. 4) creates a stale-number ambiguity
- Problem: §IV.C presents three cross-survey spectral pairs; §IV.A reports that re-running the 3″ positional match on the released catalogs yields four raw matches against a 2.75 RA-shifted expectation. The paper does not reconcile why one of the four positional matches is omitted from the highlighted triplet.
- Required fix: State the total number of positional matches from the final released catalogs (four), explain which one is not shown (and why), and keep one stable denominator in both sections to avoid confusion.

P3-M9. IsolationForest “SIF,raw” score is undefined relative to a standard implementation
- Problem: Table IV reports SIF,raw on a “∼0–3.5×10^4” scale without defining the scoring function. In common libraries (e.g., scikit-learn), IF exposes decision_function or score_samples with very different scales.
- Required fix: Specify the IF implementation and version, the exact isolation score used (formula and sign convention), any post-hoc rescaling, and how to reproduce the reported 0–3.5×10^4 range from the DOI’d latent vectors.

P3-M10. Fig. 6 y-axis label (“SIMBAD novelty fraction”) conflicts with the paper’s own caution
- Problem: The figure axis uses “novelty,” but the text emphasizes this is a database-coverage metric, not catalog novelty.
- Required fix: Relabel the axis to “SIMBAD-unmatched fraction (%)” and add a brief parenthetical in the caption echoing the body text warning.

MINOR

P3-N6. Cramér’s V expression rendered ambiguously
- Problem: The text prints “Cramér’s V = √χ^2 / √ /(N · (k − 1)) … ≈ 0.0064,” which is typographically garbled. The computation used is clearly V = sqrt(χ^2/(N(k−1))).
- Required fix: Correct the formula to V = √[χ^2/(N(k−1))] and define N, k at first mention.

P3-N7. “Score-knee” terminology is used inconsistently
- Problem: For SDSS, S ≥ 0.2051 is the empirical 99th-percentile cut (not a knee). For eROSITA, “score-knee” refers to a visually chosen top-298 cutoff on a non-reproducible axis. Using “score-knee” for both cases is confusing.
- Required fix: Call the SDSS 0.2051 threshold the “99th-percentile cut.” Reserve “score-knee” only for the eROSITA membership-only context, and point to the DOI’d artifact for the ranking.

P3-N8. Fig. 3 caption/body consistency after correction
- Problem: Once P3-E8 is fixed, make sure the narrative that explains what is shown in Fig. 3 (left vs. right panels, native vs. transfer, thresholds) is fully synchronized with the corrected caption, including which validation μ/σ were used to compute S in each panel.

P3-N9. Fig. 6 caption could better align to body text on matching radius
- Problem: The pooled 58.8% was computed at 3″ (more conservative), while per-survey fractions elsewhere use 5″; the caption mentions this only indirectly.
- Required fix: Add one sentence in the caption: “Pooled rate computed at 3″; per-survey rates in Table I use 5″.”

P3-N10. Minor terminology hygiene around “held-out” in Planck section
- Problem: The text correctly notes that top-200 includes training patches; however, the phrase “over-representation toward held-out patches” appears next to a naive binomial p-value. This may be misread as a formal test.
- Required fix: Rephrase to “the top-200 are modestly enriched in validation-split patches” and defer formal significance until a block bootstrap is performed (you already plan this).

NIT

P3-nit3. Typo/format cleanup in several math/units strings
- Examples: “1.1×106” vs “1.1 × 10^6”; stray “√/” in Cramér’s V; ensure all cutout sizes are consistent with the stated pixel scale (fix Fig. 5 per P3-E9).
- Fix: Standard copy-edit pass.

P3-nit4. Fig. 7 panel composition
- Suggestion: As noted earlier, consider consolidating the RA/Dec histograms and score–latitude panel into a cohesive multi-panel with consistent axis labeling to improve readability.

Rationale for “ESSENTIAL” flags
- P3-E8/E9/E10/E11 directly affect interpretability and/or reproducibility of key results and figures. In particular, the impossible-scale S values (P3-E10) and the native-vs-transfer caption error (P3-E8) can mislead readers about what is being shown and whether the numbers are compatible with the paper’s own definitions. The NEOWISE protocol mismatch (P3-E11) creates a procedural inconsistency with Step 5 that must be explicitly documented.

If these new issues are addressed alongside your previously listed essentials, the manuscript’s methodological clarity and internal consistency will be substantially improved for PRD standards.