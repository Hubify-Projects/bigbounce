# P3 auto-2026-06-05_1517pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10584 chars)
**Wall time**: 456.6s

---

Referee report (methodology/statistics) — P3

I read the full 20‑page manuscript, all figures, tables, equations, captions, appendices, and the abstract. Below I itemize all methodological/statistical issues I found, with severity, precise location, the specific problem (quoting the paper), and the required fix.

ESSENTIAL

P3-E1
- Location: Section V, p.10; Table IV (caveat (i)), p.13; Abstract, p.1; Conclusions, p.14
- Problem: Dimensional inconsistency and a wrong numerical constant in the Fisher forecast formula. The paper states “Under the Fisher-positivity‑respecting asymptotic form 1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982 and c = 0.0747 … gives σ(fNL) = 8.14.” If F0 = 1/8.982 ≈ 0.111, then σ = 1/√F0 ≈ 3.0 at α = 0, contradicting the quoted σstd = 8.98. To reproduce the stated baseline and numbers, F0 must be 1/(8.982)^2 ≈ 0.01238.
- Required fix: Correct F0 everywhere it appears to F0 = 1/[σstd]^2 = 1/(8.982)^2, and re-derive all quoted σ(fNL) values, envelopes, and any dependent numbers. Explicitly state the unit/normalization of F0 and c so that 1/σ^2 has consistent dimensions across the text, Table IV (caveat (i)), Abstract, and Conclusions.

P3-E2
- Location: Section III.C, p.5; Table I footnote ♡, p.7
- Problem: Contradictory SDSS thresholds and counts. The text says “The Path‑C native retrain … re‑scores 1,925,279 spectra; the top‑77,905 native slice at S ≥ 0.1060 supersedes the cross‑transfer count.” Table I footnote ♡ then calls “77,905 at S ≥ 0.1060 … the top‑1% continuity slice” on the 1,925,279 spectrum set. But 1% of 1,925,279 is 19,253, not 77,905 (≈4.05%). In the same footnote you also state “the same … sample yields 19,253 anomalies at the harder top‑1% … S ≥ 0.2051,” using “top‑1%” for two different counts.
- Required fix: Unambiguously define the SDSS thresholds. Correct the “top‑1%” label for 77,905 (it is ≈4.05% of 1,925,279). State clearly which count/threshold is used for each analysis (continuity baseline, catalog release, SIMBAD cross‑matching), and correct every place where “top‑1%” is misapplied.

P3-E3
- Location: Multiple — Section II.A, p.2 (“Fig. ??” twice); Section III.B, p.5 (“Figure ??”)
- Problem: Unresolved figure cross‑references “Fig. ?? / Figure ??” remain in the text.
- Required fix: Replace all “??” with the correct figure numbers or remove the references. Ensure every in‑text pointer resolves to an existing figure and that the figure actually shows the referenced quantity (e.g., per‑band residuals rB,rR,rZ).

P3-E4
- Location: Abstract, p.1; Conclusions point 5, p.14; Section V–V.A, pp.10–11
- Problem: Different “sigma” statements from non‑comparable procedures are juxtaposed without a clear “not directly comparable” disclaimer each time. Examples: the forecasted σ(fNL) improvement (a Fisher‑matrix forecast) is presented alongside NANOGrav “+1.13σ” and “+4.61σ” significance statements (posterior Z‑scores from an MCMC). The Abstract and Conclusions place them side‑by‑side.
- Required fix: At every juxtaposition, explicitly state that these σ values come from different statistical frameworks (forecast vs posterior significance) and are not directly comparable. Add one sentence in the Abstract and another in the Conclusions that makes this explicit.

P3-E5
- Location: Section IV.B, p.9
- Problem: HEALPix degrees of freedom inconsistent with Nside without a stated mask. You write “A spatial uniformity test across 38,330 HEALPix pixels (Nside = 64) … χ^2 = 143,936, dof = 38,329.” For Nside = 64, the full sky has 12 Nside^2 = 49,152 pixels. The paper does not define which sky mask yields 38,330, nor how many empty/zero‑count pixels were excluded.
- Required fix: Specify the exact mask/selection yielding 38,330 pixels, and justify dof = Npix − 1 under that mask. If any pixels were excluded (e.g., outside survey footprints), state the criterion. If a weighted test was used, specify it. Otherwise recompute χ^2 with a clearly defined mask and degrees of freedom.

MAJOR

P3-M1
- Location: Section V, p.10; Appendix C/Table VII, p.15; Table IV (caveat (i)), p.13
- Problem: The constant c = 0.0747 used in 1/σ^2 = F0 + c α^2 is asserted but not derived or documented. The text mentions a “5‑α refit” but gives no inputs, volumes, fiducial binning, tracer densities, or the baseline Fisher block from which c was obtained. Without this, the σ(fNL) numbers are not reproducible.
- Required fix: Provide a derivation or full specification sufficient to reproduce c, including: (i) the exact Fisher setup (k‑range, binning, redshift bins, tracer densities, bias models, survey volumes, shot‑noise terms), (ii) the baseline F0 computation, and (iii) the regression or fit procedure that yields c. Ideally, deposit the Fisher code or a notebook and cite a DOI.

P3-M2
- Location: Section IV.D, p.10
- Problem: Over‑generalized claim from a single null cross‑correlation. You conclude “This null result demonstrates that CMB patch anomalies from autoencoder analysis are dominated by survey‑specific systematics rather than primordial cosmological signals.” The analysis uses one under‑trained ACT cross‑transfer checkpoint (explicitly quarantined) and one Planck native model; no quantitative cross‑correlation statistic or p‑value is provided.
- Required fix: Rephrase to limit the claim to “in our specific pipelines and selections …” and provide a quantitative test: define the overlap metric, the random‑overlap expectation and variance, and report a p‑value or Z‑score for the null. Alternatively, move the statement to a “caveat” framing.

P3-M3
- Location: Section III.A, p.4
- Problem: Paragraph duplication. The paragraph beginning “Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE…” appears twice (verbatim or near‑verbatim) on the same page.
- Required fix: Remove the duplicate and keep a single, clean version.

P3-M4
- Location: Table I (main table and long footnotes), pp.7–8
- Problem: Threshold taxonomy is unclear across surveys (absolute S > 5, top‑percentile, IsolationForest knee, fixed top‑1%). The table’s footnotes attempt to clarify but also conflate cross‑transfer and native cuts and (for SDSS) mislabel the “top‑1%” count (see P3‑E2).
- Required fix: Provide a compact, unambiguous threshold summary per survey in the table (e.g., “DESI: S>5; SDSS(native): S≥0.2051 (top‑1% of 1.925M); SDSS(cross‑transfer): S>5 (12 objects)” etc.). Ensure the table body and footnotes are internally consistent and numerically correct.

P3-M5
- Location: Data availability, p.14
- Problem: Data/code are stated to be “private pending arXiv acceptance; public upon acceptance.” PRD requires availability at publication and strongly prefers stable DOIs for archival artifacts used in the analysis.
- Required fix: Provide stable, public DOIs for the catalog, weights, and scripts at submission (e.g., Zenodo, institutional repository) or commit to an OSF/Zenodo DOI upon acceptance with an embargo lifted before publication. Clarify licensing.

P3-M6
- Location: Section II.D (Step 1), p.3; Section III.F, p.6
- Problem: Gate criterion (a) “validation loss ≤ 0.30 after ≤ 100 epochs” is very loose relative to actual convergences (≈0.03 for spectroscopic; 0.4437 for Planck). As written, criterion (a) could pass extremely poor models in other domains; the Planck model actually fails (a) but passes (b). The loss definitions also differ across modalities (FC vs CNN).
- Required fix: Justify the 0.30 threshold numerically or replace it with a domain‑normalized criterion (e.g., relative to training‑set variance) that is comparable across modalities. State explicitly that CMB uses a different loss scale and thus only criterion (b) applies; or standardize losses.

P3-M7
- Location: Section II.B, p.2
- Problem: Incomplete definition of the DESI S > 5 cut. You write “For DESI DR1, μval ≈ 0.0287 and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143.” This is tautological and omits the actual σval used.
- Required fix: Report the numerical σval (≈(0.143 − 0.0287)/5 ≈ 0.02286) and the training/validation sample sizes used to estimate (μval, σval). State whether σval is the sample SD of MSE over the validation set or a robust estimator.

P3-M8
- Location: Section III.E, p.6–8; Table I footnote §, p.7–8
- Problem: The eROSITA cross‑validation enrichment is given as “hypergeometric two‑sided p ≈ 0; enrichment 95.3×.” “p ≈ 0” is imprecise for a high‑profile result.
- Required fix: Report the exact hypergeometric p‑value (or a tight numerical bound, e.g., p < 10^−x) and the full parameters used (population N, class sizes, overlap). Include uncertainty on the 95.3× factor if appropriate.

P3-M9
- Location: Section III.G; Table I footnote ⋆, p.8
- Problem: Gaia DR3 cross‑validation stability (41.0%) lacks sufficient methodological detail to reproduce (sampling, seeds, contamination parameter choice, features used).
- Required fix: Provide the precise protocol: size and selection of the 500k sample, random seed(s), IF hyperparameters (n_estimators, max_features), contamination, and the exact thresholding and overlap computation.

P3-M10
- Location: Section IV.C, p.9–10
- Problem: Expected random coincidences for 7‑way 5″ deduplication stated as “≲ 10” without a derivation.
- Required fix: Provide the calculation (surface density per survey, sky area, pairwise match area πr^2, and a Bonferroni or union‑bound treatment across pairs), or give a conservative numeric bound.

MINOR

P3-m1
- Location: Section II.D, p.3
- Problem: Repetition/typo: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)”.
- Required fix: Remove the duplicated parenthetical.

P3-m2
- Location: Section II.C, p.3
- Problem: Throughput/compute timings are given without uncertainty or hardware specifics for all runs; photometric surveys “each required < 10 seconds of GPU time” is unusually fast and might mislead readers about reproducibility on typical hardware.
- Required fix: Add a short note that timings are on an H200 80 GB GPU and give wall‑clock times per survey (already partially present) plus any relevant I/O bottlenecks or variance.

P3-m3
- Location: Figure 2 (right), p.5
- Problem: The “Anomaly score S” axis spans to 10^11; although explained as a cross‑transfer artifact, the axis label does not remind readers that S here uses the DESI scale applied to SDSS.
- Required fix: Add a caption note that SDSS panel uses the DESI‑trained scale (cross‑transfer), and that these S are not comparable to native SDSS S.

P3-m4
- Location: Section IV.A, Fig. 5, p.9
- Problem: The label “Aggregate 58.8%” could be misread as a discovery rate.
- Required fix: Bold the existing disclaimer in caption/paragraph that this is a database‑coverage measurement, not a discovery rate.

P3-m5
- Location: Section III.F, p.6
- Problem: “val loss ≈ 2×10^4” for the cross‑transfer CMB checkpoint is extreme; readers may wonder if the loss is normalized.
- Required fix: State the loss definition/scale used for the FC CMB autoencoder to avoid confusion.

P3-m6
- Location: Appendix E, p.16
- Problem: Equation (E1) lacks an explicit pointer/citation to the likelihood definition used by the “KDE free‑spectrum” product (e.g., cf. the NANOGrav paper or ceffyl docs).
- Required fix: Add a citation or brief derivation context for Eq. (E1) so a reader can trace the parametrization.

P3-m7
- Location: Various (e.g., p.6 “gate FAIL-with-diagnostic”, p.13 Fig. 7 legend)
- Problem: All‑caps PASS/FAIL and asterisks in running text/legends are informal.
- Required fix: Standardize to journal style (e.g., “passes/does not pass” or “meets/does not meet the gate”).

NITS

P3-N1
- Location: Title/Abstract, p.1; Section VII, p.14
- Problem: Strong novelty/scale claims (“largest-scale”, “∼141×… largest prior catalog”) are not referenced at the claim point.
- Required fix: Add an inline citation ([11]) next to each “largest” or “×” claim, and ensure the comparison (dataset type, thresholding) is like‑for‑like.

P3-N2
- Location: Section I, p.1
- Problem: “ACT DR6 quarantined as a cross‑transfer artifact” reads like version‑history language.
- Required fix: Rephrase to “We exclude ACT DR6 from the primary analysis; see Appendix F for methodological details.”

P3-N3
- Location: Typographic
- Problem: Occasional hyphenation artifacts (e.g., “sur￾vey”, “re￾trained”).
- Required fix: Clean the PDF text flow.

Arithmetic/consistency spot checks (passed)

- Totals: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493; minus 10,213 deduplicated detections = 378,280 unique (correct). Compression = 10,213/388,493 = 2.629% (correct).
- Point‑source unique = 378,280 − 200 Planck = 378,080 (correct).
- DESI anomaly rate = 195,829/22,504,897 = 0.870% (correct).
- LAMOST cross‑transfer → native S>5 compression: 44,075/2,054 ≈ 21.46× (correct).
- SDSS cross‑transfer → native S>5 compression: 77,905/12 ≈ 6,492× (≈6,500× as stated).
- NEOWISE polar caps: observed 17/436 = 3.90%; expected two 10° caps = 1 − cos 10° ≈ 1.52%; ratio ≈ 2.57× (rounded to 2.6× as stated).
- SIMBAD false‑match: π(5″)^2 × 3×10^−5 ≈ 2.36×10^−3 per source; for 195,829 sources ≈ 462 (≈460 as stated).
- χ^2ν = 143,936/38,329 = 3.757 (≈3.76 as stated).
- NANOGrav Z‑scores: (3.0 − 2.567)/0.382 ≈ +1.13σ; (4.33 − 2.567)/0.382 ≈ +4.61σ (correct).
- Bayes factor: 3.23/(4.52×10^−4) ≈ 7.14×10^3 (correct).

Length and scope

The manuscript is long (20 pages main text) relative to the core methodological contribution. Much of Sections III–IV and Table I footnotes are devoted to survey‑by‑survey catalog narration and cross‑transfer baselines that are not part of the final “Path‑C” result. For a PRD readership focused on methodology, I recommend tightening to ≲15 pages by:
- Moving cross‑transfer baseline plots/details to an appendix;
- Consolidating threshold descriptions into one succinct table;
- Focusing the main text on the validated native‑retrain protocol, validation gates, uncertainty propagation, and cosmological forecast methodology.

## Summary recommendation
MAJOR REVISIONS

The paper contains several essential methodological errors/omissions: a dimensionally incorrect Fisher constant (F0), contradictory SDSS threshold/count statements (“top‑1%” mislabeling), unresolved “Fig. ??” references, and juxtaposition of non‑comparable σ statements without explicit disclaimers. There are also major issues with reproducibility of the Fisher constant c, over‑generalized claims from a single CMB cross‑correlation, and a duplicated paragraph. These must be corrected before the manuscript can meet PRD’s standards for methodological rigor and internal consistency.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh pass)

ESSENTIAL

P3-E6
- Location: Section III.F (Planck CMB), p.6
- Problem: Score scale inconsistency for Planck. The paper defines a single canonical anomaly score S as the z-scored MSE (Eq. 2), where typical anomaly cuts are S > 5. For Planck, you report “Top‑200 native anomaly patches (score range [0.558, 0.621]).” Those values are sub‑1σ on the canonical S scale and cannot be “top‑1% anomalies” if S is used. This implies a different, non‑z‑scored metric was plotted/reported for Planck.
- Required fix: State explicitly what score was used for Planck (raw MSE, normalized MSE, or a different z‑score), how µval and σval were computed (if at all), and reconcile with the global definition of S. If a different metric is used, rename it throughout and do not call it “S”; add the exact conversion or leave Planck on its native metric with a clear disclaimer.

P3-E7
- Location: Abstract, p.1; Table I footnote ♠, p.7–8; Conclusions, p.14
- Problem: Inconsistent “catalog‑grade subset” definition and count. The Abstract recommends a point‑source “catalog‑grade subset ≈265,000 (DESI + SDSS + eROSITA + Gaia + NEOWISE).” Table I footnote ♠ then gives “catalog‑grade tier … 264,938 unique objects” but explicitly includes Planck (200 CMB patches), which are not point sources. The two definitions differ (5 point‑source surveys vs the 5+Planck set), yet the number (~265k) is reused.
- Required fix: Provide the exact deduplicated unique count for the 5 point‑source surveys only (DESI + SDSS native + eROSITA + Gaia + NEOWISE), and report the Planck‑included figure separately. Use the same definition consistently in Abstract, body, and Conclusions.

P3-E8
- Location: Section II.B (threshold summary), p.2; Section III.E (eROSITA), p.6–8; Table I footnote §, p.7–8
- Problem: eROSITA selection metric contradicts itself. Section II.B states “eROSITA uses a data‑driven IsolationForest score‑knee threshold,” but Section III.E defines the released catalog as “298 at SBigAE > 0.259” and later treats IsolationForest as a cross‑validation check. The two descriptions conflict on whether BigAE S or IF is the primary selection axis.
- Required fix: Unify the eROSITA description: state unambiguously which score defines the 298‑source headline set (BigAE S or IF), how the threshold was determined (“score‑knee”), and then describe the other detector as a cross‑validation. Update Section II.B and Table I text/footnotes to match.

P3-E9
- Location: Appendix D, Fig. 8 caption (and y‑axis), p.16 vs Section V, p.10
- Problem: Inconsistent single‑tracer baseline. Fig. 8 labels the “single‑tracer baseline” as σ(fNL) = 16.85, whereas Section V repeatedly uses σstd = 8.98 as the single‑tracer baseline. This is a major, unexplained discrepancy.
- Required fix: Reconcile the two baselines. If Fig. 8 uses a different survey volume/redshift range/binning than the DESI QSO baseline (8.98), say so and label it accordingly (e.g., “toy baseline for canonical 5‑tracer mock”). Otherwise correct the figure and any text derived from it.

MAJOR

P3-M11
- Location: Section II.A–B (all surveys), p.2
- Problem: Missing feature scaling/normalization details across heterogeneous inputs. MSE on raw inputs mixes units (e.g., magnitudes, colors, counts, astrometric quantities) and will be dominated by large‑variance features unless standardized. No pre‑processing pipeline (per‑feature z‑scaling, transformations, clipping) is documented for eROSITA, Gaia, NEOWISE, or even for spectral flux normalization across B/R/Z arms.
- Required fix: Document the exact preprocessing per survey: feature list, transformations (e.g., log/flux/mag conversions), per‑feature standardization (mean/SD, robust scaling), training/validation statistics used to scale inference, and publish the scalers with the code.

P3-M12
- Location: Section II.D Step 5; Fig. 7; Sections III C–H; Table I gates, pp.3, 6–8, 13
- Problem: Inconsistent/undefined “injection amplitude in units of noise σ” across modalities. The 5σ gate is applied to very different plants (continuum dips, emission lines, Gaussian bumps in CMB maps, “variability‑axis” in Gaia, “mask injection” in NEOWISE), but “σ” is not consistently or rigorously defined (per‑pixel, per‑feature, per‑spectrum noise? local vs global?).
- Required fix: For each survey, define the noise model and σ used for injections, how it is estimated per object/patch, the plant functional form, duration/width, placement, and the detection criterion. Provide code/notebooks to reproduce the curves in Fig. 7.

P3-M13
- Location: Section III.A, p.4
- Problem: “0% artifact rate in the top 200” lacks protocol. A strong claim is made without describing the vetting procedure (number of raters, blinding, criteria for “artifact,” inter‑rater reliability, how disagreements were resolved, whether spectra and reconstructions were both shown).
- Required fix: Describe the vetting protocol and provide a small, de‑identified gallery (or audit log) demonstrating what was considered an artifact vs genuine anomaly.

P3-M14
- Location: Section V and Appendix C/D, pp.10, 15–16
- Problem: Forecast configuration mismatch (5‑tracer vs 7‑bin). Section V and Appendix D refer to a “canonical 5‑tracer Fisher,” while Appendix C repeatedly mentions a “full 7‑bin Fisher” used for the α‑scaling table. The paper never defines these tracers/bins or how they map to the data.
- Required fix: Precisely define the Fisher setups: list tracers, redshift bins, n(z), bias models, volumes, k‑ranges, and which setup underlies each reported number (tables, figures). Ensure consistency of terminology (tracers vs bins).

P3-M15
- Location: Section II.D Step 6; Section IV.C, pp.3, 9–10
- Problem: Friends‑of‑friends (FOF) dedup at 5″ can chain sources to separations >5″. A union‑find FOF with radius r links chains; cluster members can end up ≫ r apart, inflating multi‑survey coincidences and potentially biasing the “≲2% contamination” statement.
- Required fix: Specify the exact dedup algorithm (single‑linkage FOF vs center‑based clustering), report the maximum intra‑cluster separation distribution, and recompute the random‑coincidence expectation under that algorithm. Consider switching to a center‑within‑r rule to prevent chaining.

P3-M16
- Location: Section IV.A (“Archival cross‑match…”), p.9
- Problem: Reproducibility gap for the 17.8% novelty estimate. The CDS X‑Match run parameters (search radius, primary/aux catalog choice, proper motion handling, duplicate resolution, how the 20 catalogs were combined) are not given.
- Required fix: Document the exact X‑Match configuration (radius per catalog, epoch handling, positional error model), and publish the script/DOI for the run. Include a sensitivity test vs radius (e.g., 2″/3″/5″) to bracket the novelty fraction.

P3-M17
- Location: Fig. 5 and associated text, p.9
- Problem: The “Aggregate 58.8%” SIMBAD‑unmatched fraction pools surveys inconsistently (DESI is measured on the “top‑10K,” others on full anomaly sets), biasing the aggregate.
- Required fix: Recompute the aggregate with consistent denominators (either all anomalies per survey or matched‑size top‑N per survey), and report per‑survey sample sizes used to compute each bar.

P3-M18
- Location: Section III.E (eROSITA headline finding), p.6–8
- Problem: “203 novel X‑ray sources” is claimed from SIMBAD‑unmatched status, which the paper itself later cautions overstates novelty (Section IV.A). This is an over‑claim in a headline bullet.
- Required fix: Rephrase to “203 sources absent from SIMBAD” and move “novel” to the multi‑catalog novelty context only (after the CDS X‑Match procedure).

P3-M19
- Location: Table V (Planck CNN training time), p.15; Section III.F, p.6
- Problem: Implausible training times. The Planck native CNN is reported as training on 2×10^5 patches with 1.1M parameters in 10.6 s (A100). This is not credible by orders of magnitude given dataset size and model. Similar issue for ACT (7.0 s).
- Required fix: Verify and correct the units (seconds vs minutes/hours), provide epoch counts, batch size, optimizer settings, wall‑clock per epoch, and total wall time. If the table reports inference or a single epoch, label it clearly; otherwise this undermines reproducibility.

MINOR

P3-m8
- Location: Section II.B(b), p.2–3; Section VI.D(i) row (g), p.13
- Problem: OOD holdout size inconsistency: “100k unseen” in text vs “103,000‑spectrum OOD holdout” in caveats.
- Required fix: Use a single, exact number (and seed) in both places.

P3-m9
- Location: Section V (envelope statement), p.10; Table IV (caveat (i)), p.13
- Problem: Confidence‑level mismatch. Section V calls [3.92, 8.98] a “1σ envelope,” while Table IV labels it “95% envelope.”
- Required fix: Choose one CL, recompute if necessary, and standardize the label everywhere.

P3-m10
- Location: Fig. 9 caption and panels, p.17; Section III.B, p.5
- Problem: “AE” label ambiguity. Earlier, “AE” is said to denote the Z‑arm sub‑score rZ in a high‑z context, but Fig. 9 uses “AE” generically across families without defining whether it is total S or a band sub‑score.
- Required fix: Define “AE” in the caption (total anomaly score S vs a band‑specific residual), or replace “AE” with “S”/“rZ” as appropriate.

P3-m11
- Location: Section II.C, p.3; Table V, p.15
- Problem: Compute timing context still sparse for some entries (e.g., LAMOST inference wall‑clock not reported; photometric “< 10 s” blanket).
- Required fix: Add per‑survey wall‑clock inference times (as ranges with I/O notes) and specify hardware for training (A100) vs inference (H200), so results are reproducible on comparable hardware.

NITS

P3-N4
- Location: Appendix D Fig. 8 caption, p.16
- Problem: The caption mixes terms (“canonical 5‑tracer configuration of §V,” “baseline multi‑tracer = 12.72”) that are never defined in §V, compounding the baseline inconsistency noted in P3‑E9.
- Required fix: Align figure terminology with §V (or expand §V to define the “canonical 5‑tracer” setup), or adjust the caption to reference the correct subsection that defines these numbers.

Explanation of scope
These items were not covered in the initial review because they required cross‑checking figures against body text (e.g., Fig. 8 vs §V), verifying consistency of the globally defined score S in modality‑specific sections (Planck), and plausibility checks on training times and aggregate statistics. The new findings focus on arithmetic/plausibility mismatches, metric/threshold consistency, and reproducibility gaps that PRD reviewers will expect to be rectified.