# P3 auto-2026-06-05_1617pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7317 chars)
**Wall time**: 278.6s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies …”

Scope of review
I evaluated the paper for statistical-methods rigor, derivation chains, dimensional consistency, internal arithmetic, and consistency of reported scalars across the abstract, figures, tables, and main text. I re-computed the ratios, percentages, and significance values stated in the abstract and conclusions and audited all load‑bearing equations, captions, and table entries.

Overall assessment
The study presents a large-scale, multi-archive anomaly-detection effort and contains many useful technical details. However, there are multiple essential issues: a dimensional/definition error in the Fisher-forecast formula used throughout the cosmology section, contradictory claims about cross-survey “anomaly” matches, unresolved figure placeholders (“Fig. ??”), inconsistent definitions of the “catalog-grade” subset size and composition, an unexplained HEALPix pixel count used in a χ2 uniformity test, and a mismatch between the claimed “20 curated catalogs” and the 18 actually listed. There is also threshold/estimator ambiguity for SDSS across the manuscript. Given PRD’s standards, these must be corrected before the work can be considered.

Findings (ESSENTIAL / MAJOR / MINOR / NIT)

ESSENTIAL

P3-E1 (Section V, p.10; Abstract p.1; Sec. VI.D(i), p.12; Table IV, p.13)
Problem: The Fisher “positivity-respecting” formula is written as 1/σ(fNL)^2 = F0 + c α^2 with F0 = 1/8.982. This is dimensionally inconsistent with 1/σ^2. Using F0 = 1/8.982 gives σ ≈ 2.96, not the reported 8.14. The reported 8.14 is obtained only if F0 = 1/(8.982)^2 ≈ 0.0124.
Required fix: Correct F0 everywhere to F0 = 1/σstd^2 = 1/(8.982)^2. Propagate this correction consistently in the text, Table IV, and any derived envelopes. State explicitly how the [3.92, 8.98] “1σ envelope” is computed (what prior on α, and are α<0 and α>0 treated symmetrically through α^2?). If a Gaussian prior α ~ N(0.19, 0.65^2) is used and envelopes are drawn by plugging α ±1σ into the α^2 term, state that explicitly.

P3-E2 (Sec. IV.C, p.10–11; Fig. 6)
Problem: The text claims “Known QSO at z ≈ 1.55: independently flagged by both surveys,” but Fig. 6 panels (a,b) show anomaly scores 3.2 and 2.8, below the survey’s S>5 anomaly threshold. These are not anomalies as defined.
Required fix: Correct the claim. Either (i) show a cross-survey pair both meeting the anomaly threshold, or (ii) rephrase to make clear that this example is a non-anomalous cross-match displayed only to validate reconstructions (and then remove it from “highest-confidence cross-survey detections” phrasing).

P3-E3 (Multiple locations: Sec. II.A p.2 “Fig. ??”; Sec. II.B p.2 “Fig. ??”; Sec. III.B p.4–5 “Figure ??”.)
Problem: Unresolved internal placeholders (“Fig. ??”) remain in the text.
Required fix: Replace all “Fig. ??” with correct figure references, or remove the sentences that reference figures that are not present.

P3-E4 (Abstract p.1; Table I footnote ♠ p.7; Sec. II.D p.3; Conclusions p.14)
Problem: Inconsistent definition and composition of the “catalog-grade subset.” Abstract: “recommended catalog-grade subset is ∼265,000 unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE), which excludes LAMOST.” Table I footnote ♠ states “catalog-grade tier (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) is 264,938 unique objects,” which appears to include Planck contrary to the abstract and to the point‑source-only guidance elsewhere. There is no worked dedup accounting showing how 264,938 is obtained.
Required fix: Provide a single, unambiguous definition of the “catalog-grade” subset, list which surveys it includes/excludes (Planck? LAMOST?), and provide the exact unique-object count after dedup within that subset. Show the arithmetic from per-survey counts to the deduped unique number (and whether Planck patches are included in this count). Ensure the abstract matches this final definition.

P3-E5 (Sec. IV.B, p.9–10)
Problem: The spatial uniformity test states “across 38,330 HEALPix pixels (Nside=64).” For Nside=64, full-sky pixel count is 12×Nside^2 = 49,152. The manuscript does not define the mask or explain why only 38,330 pixels are used, yet uses dof = 38,329 in the χ2 test.
Required fix: Specify the sky mask (union of footprints? coverage mask?) and the exact number of pixels used after masking. Adjust the dof accordingly and recompute χ2 and χ2_ν. If the mask is irregular, explain how expected counts per pixel were computed (accounting for varying survey footprints) or retract the χ2 claim and restrict to the more robust latitude/dust correlations only.

P3-E6 (Sec. IV.A, p.9)
Problem: The text claims “20 curated all-sky catalogs via CDS X-Match,” but the list contains 18 items (Gaia DR3; SDSS DR12/DR16; DESI Legacy DR9; DES DR2; Pan-STARRS1; AllWISE; CatWISE2020; 2MASS; unWISE; GALEX; Chandra; 4XMM; NVSS; VLASS; USNO-B; UCAC5; APASS).
Required fix: Provide the complete list of the 20 catalogs actually used (with names/versions), or correct the count to the actual number searched.

P3-E7 (Sec. II.B p.2; Table I p.7, footnotes ♡, ♠; Sec. III.C p.5)
Problem: Estimator/threshold ambiguity for SDSS. Early text claims SDSS DR18 uses a fixed “canonical-S cut at S > 5.0 anchored by each survey’s (µval, σval)” while later sections and table footnotes introduce a “three-threshold disclosure” for SDSS native scoring (12 objects at S>5; 19,253 at top‑1%; 77,905 at S≥0.1060 continuity slice). It is unclear what is the pre-declared, primary SDSS anomaly definition used for catalog statistics and cross-survey deduplication.
Required fix: Pre-declare and enforce a single primary SDSS anomaly definition for headline statistics (e.g., S>5 if comparability to DESI is the goal). If auxiliary slices (top‑1% or continuity-matched counts) are retained for diagnostic purposes, move them to an appendix and clearly mark them as secondary. Ensure Table I shows only the primary SDSS anomaly count, with any alternates relegated to a separate table/note.

MAJOR

P3-M1 (Sec. V and Appendix C, p.10 and p.15–16)
Problem: Inconsistent σ(fNL) baselines across sections. Section V uses a single-tracer baseline σstd = 8.98, while Appendix C Fig. 8 states a “single-tracer baseline” of 16.85 and a “baseline multi-tracer” of 12.72 with an “ideal dense limit” 11.71. It is unclear if these refer to different experiments, different kmax, different tracer sets, or different Fisher blocks. This undermines interpretability of the fNL forecast.
Required fix: Consolidate the Fisher-forecast framework into a single, clearly specified configuration (tracer definitions, number densities, bias model, k-range, survey volume, systematics block). If Appendix C explores a different configuration, label it explicitly as such and explain its relationship to the Section V baseline. Remove or reconcile contradictory baselines.

P3-M2 (Sec. IV.A, p.9)
Problem: The 17.8% “genuine novelty fraction” is presented as “the primary novelty metric for this catalog,” but it is based on a single top‑1,000 DESI stratum point estimate without uncertainty or replication across surveys/score quantiles.
Required fix: Provide an uncertainty estimate for the 17.8% (e.g., binomial 68% and 95% CIs), and clearly qualify it as a top‑1,000 DESI‑only point estimate. Either (i) replicate on additional score strata/surveys, or (ii) explicitly state that its generalization to the full catalog is unknown and should not be assumed.

P3-M3 (Sec. III.C, p.5; Fig. 2 caption, p.5; Table I text, p.7)
Problem: SDSS cross-transfer scoring and standardization. The paper alternates between saying S is standardized “per survey” using that survey’s validation MSE and using a DESI‑trained BigAE applied to SDSS (where no SDSS-native validation of that DESI-trained model exists). It is not explicit what µval, σval are used to compute S for SDSS cross-transfer panels and counts, nor how this affects the extreme S values (up to 1.9×10^11).
Required fix: Precisely state which µval and σval are used for SDSS cross-transfer S (DESI validation or SDSS validation of a DESI‑trained model). Make the SDSS standardization and thresholds fully consistent across the text/figures/tables or move cross-transfer results to a clearly demarcated diagnostic appendix.

P3-M4 (Sec. IV.B, p.9–10)
Problem: χ2 uniformity analysis likely dominated by heterogeneous survey footprints. The text acknowledges this but still quotes χ2_ν = 3.76 with dof tied to an unexplained pixel count (see P3-E5). Without modeling angular selection functions, this χ2 is not interpretable as evidence for/against clustering.
Required fix: Either remove the χ2 claim entirely or supply a per-survey selection-function model and expected counts per pixel under the null.

P3-M5 (Sec. V, p.10)
Problem: Landy–Szalay/α measurement is underspecified. The report lacks details on random-catalog construction, survey masks, completeness weights, and jackknife partitioning choices—these can materially affect α and its uncertainty.
Required fix: Provide methodological details (random density, mask definition, treatment of angular systematics, pair-count normalization, and jackknife region definition) and a validation showing stability of α under reasonable variations of these choices.

P3-M6 (Abstract p.1; Sec. III.C p.5)
Problem: “∼6500× SDSS rate compression after native retraining” mixes thresholds (77,905 cross-transfer vs. 12 native at S>5) while separately advocating a different native “continuity” slice (77,905 at S≥0.1060). This is potentially misleading.
Required fix: Rephrase to say explicitly: “Under the field‑defining S>5 criterion, the SDSS anomaly count drops from 77,905 (cross-transfer, DESI‑trained scale) to 12 (native SDSS‑scored), evidencing domain shift.” Avoid language implying a native re-train produced 6,500× compression while elsewhere adopting a differently thresholded 77,905‑object “continuity slice.”

MINOR

P3-n1 (Sec. II.D p.3)
Problem: Redundant wording: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”
Required fix: Remove duplication and standardize the data/code availability statement.

P3-n2 (Sec. III.A p.4)
Problem: Paragraph duplication: the galaxy vs. QSO anomaly-rate sentence block appears twice with minor rephrasing.
Required fix: Remove duplication and keep the definitive version.

P3-n3 (Table I, p.7)
Problem: Heavy footnotes (♡,♠,⋆,§,∥) blur core results and mix diagnostics with headline numbers.
Required fix: Move most diagnostic notes to the appendix and keep the table concise with one primary number per survey and a clean “Path-C unique” row. Reserve detailed threshold variants to a supplemental table.

P3-n4 (Sec. III.F p.6)
Problem: Planck CMB anomaly score range [0.558, 0.621] is reported without restating the definition of the score for the convolutional AE (is this the same canonical-S z-scored MSE?).
Required fix: Clarify the score definition for Planck (is it z-scored MSE on a held‑out validation of the conv‑AE?), and confirm comparability to S used elsewhere.

P3-n5 (Figures)
Problem: Some axes/captions omit units (e.g., Fig. 6 wavelength axis has Å but normalization definition is only in caption text; Fig. 2 left uses “Probability density” on log scale without specifying normalization).
Required fix: Ensure all axes include units and captions clearly define any normalization.

NIT

P3-z1 (General)
Problem: Informal/colloquial phrasing appears in the main text and table footnotes (e.g., “transparent FAIL,” “lessons-learned,” “gate FAIL,” “quarantined artifact”).
Required fix: Replace with formal scientific language.

P3-z2 (Data availability, p.14)
Problem: The dataset is “private pending arXiv acceptance.” PRD requires data/code accessibility upon publication.
Required fix: Commit to a persistent, public DOI (Zenodo/Dataverse) to be activated upon acceptance.

Arithmetic and consistency checks (selected)

- 141× larger than [11]: 378,080 / 2,685 ≈ 140.8 ✓
- DESI-only 73×: 195,829 / 2,685 ≈ 72.9 ✓
- Dedup compression: (388,493 − 378,280)/388,493 = 2.629% ✓
- SIMBAD random false‑match rate at 5": nsimbad ≈ 3×10^−5 arcsec^−2, area π(5")^2 ≈ 78.54 arcsec^2 → 0.00236/source; ×195,829 ≈ 463 ✓
- NEOWISE polar caps: expected area fraction two caps = 2(1 − cos 10°) ≈ 1.52%; observed 17/436 = 3.90%; ratio ≈ 2.57× ✓
- SDSS “rate compression” (diagnostic): 77,905/12 ≈ 6,492×; but see P3‑M6 on threshold comparability.
- fNL forecast central value: with corrected F0 = 1/8.982^2 = 0.0124 and c=0.0747, α=0.19 → 1/σ^2 = 0.0124 + 0.0747×0.0361 = 0.0151; σ = 8.14 ✓ (but requires corrected F0).
- NANOGrav γ distances: (3.0 − 2.567)/0.382 = 1.13σ; (4.33 − 2.567)/0.382 = 4.61σ ✓
- Bayes factor ratio: 3.23/(4.52×10^−4) ≈ 7.14×10^3 ✓

Length and scope
The manuscript is dense (20 pages) and mixes a resource‑release catalog with multiple methodological diagnostics and two largely independent cosmology applications. For PRD, I recommend refocusing on:
- The per‑survey native‑retrain methodology, validation gates, and dedup pipeline (core methods contribution).
- A clean, single-threshold primary catalog description (with secondary diagnostics in appendices).
- One well‑specified cosmology use case (either fNL or PTA spectral index), not both, or move the PTA result to a brief appendix as an illustration.

A streamlined main text of ≤15 pages is achievable by moving threshold variants, domain‑shift diagnostics, and extensive footnotes to appendices.

## Summary recommendation
REJECT

The paper presents interesting large‑scale anomaly‑detection results, but multiple essential issues prevent acceptance at PRD: (1) a definition/dimensional error in the Fisher forecast formula used to obtain the headline σ(fNL)=8.14 and its envelope, (2) a contradictory “independently flagged by both surveys” claim for a cross‑survey match that does not meet either anomaly threshold, (3) unresolved “Fig. ??” placeholders, (4) inconsistent and undocumented arithmetic for the “catalog‑grade subset” size and composition, (5) an unexplained HEALPix pixel count used in a χ^2 uniformity claim, and (6) a mismatch between the stated “20” catalogs and the 18 listed. There are further major clarity issues around SDSS thresholds/standardization and inconsistent fNL baselines across sections. I encourage resubmission after a thorough methodological and editorial revision that corrects these errors, consolidates definitions and thresholds, and streamlines the presentation.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh read)

ESSENTIAL

P3-E8 (Sec. III.H p.8; Table I footnote † p.7; Fig. 4 context)
Arithmetic error in NEOWISE polar-cap expectation. The text claims the observed 3.90% polar-cap fraction (17/436) is 2.6× the uniform-sphere expectation “1.52%.” For two polar caps of angular radius 10°, the uniform area fraction is 2(1 − cos 10°) ≈ 2 × 0.0152 = 0.0304 = 3.04%, not 1.52%. The correct enrichment is 3.90/3.04 ≈ 1.28×, not 2.6×. This materially weakens the evidence for scan-pattern contamination as quantified. Required fix: Correct the expected fraction to 3.04% and recompute the enrichment and any p-value/claim tied to “2.6×.”

P3-E9 (Appendix C §1, Fig. 8 p.16; main text Sec. VII item 5 references)
Shot-noise “penalty” produces a better σ(fNL) in text (sign error). The text states “With a 15% Fisher-info penalty, σ(fNL) = 12.56 (+1.27% over the baseline‑multi 12.72); with a 30% penalty, σ(fNL) = 13.35 (−4.97% vs. baseline‑multi).” A reduction in Fisher information must increase σ, not decrease it. Here 12.56 < 12.72 indicates an improvement, contradicting “penalty.” Either the 12.56 value is wrong or the “15% penalty” label is. Required fix: Recompute σ(fNL) under your stated information-loss model; ensure monotonic worsening with larger penalties. Correct the signs and percentages relative to the stated baseline (12.72). If these σ values correspond to a different baseline/configuration than Sec. V (already flagged in the initial review), label that explicitly and keep signs consistent.

P3-E10 (Sec. II.C p.3; Table V p.15)
Wall-clock runtime accounting is inconsistent with reported throughputs. You state “total processing time … ≈ 42 hours (wall‑clock), dominated by the DESI DR1 scan (19,705 s) and the LAMOST DR10 scan.” Using your throughputs: DESI 22.5M/1,142 ≈ 19,705 s (5.47 h); LAMOST 11.4M/950 ≈ 12,000 s (3.33 h); SDSS 2.3M/1,100 ≈ 2,091 s (0.58 h); others add < 0.1 h. In total, inference sums to ≲ 9.5 h, not 42 h. If the 42 h includes data I/O, preprocessing, or retrain time, state and break it down; else correct the wall‑clock figure.

MAJOR

P3-M7 (Table V p.15)
Training-time units/values are not credible or are unlabeled. The table reports native retrain “Train time (s)” of 10.6 s for the Planck conv‑AE trained on 2×10^5 patches, and single‑digit seconds for catalog‑sized tabular models (eROSITA 7.6 s, Gaia 1.2 s, NEOWISE 1.6 s). These are implausible for 100–200 epoch trainings described earlier. Required fix: Clarify whether these are per‑epoch times, single‑pass fits, or total wall‑clock; provide hardware, batch size, epochs actually run, and confirm units (seconds vs minutes/hours). If these are inference rather than training times, correct the column header and text.

P3-M8 (Sec. II.D Step 1 p.3 vs Sec. II.B p.2; Sec. III.A p.4)
Native-retrain “2–5×10^5 spectra” and “≤100 epochs” gate criteria conflict with earlier specifics. You state the Path‑C protocol trains on “2–5×10^5” per survey and is retained if val‑loss ≤ 0.30 after “≤100 epochs,” yet DESI’s native training used 47,000 spectra and training elsewhere is “up to 200 epochs.” Required fix: Make the gate criteria match what was actually done per survey (list the actual training-set sizes and epoch counts used in each native retrain) or restate the gate as a heuristic rather than a hard rule.

P3-M9 (Table I, “Path‑C unique (primary)” row p.7)
Headline “Rate (%) = 1.01” is not an interpretable anomaly frequency. The unique-object numerator mixes surveys with predetermined top‑1% selections (Planck, Gaia, NEOWISE) and ad‑hoc hard caps (eROSITA top‑298), then deduplicates across heterogeneous footprints. Presenting 378,280 / 37,272,042 = 1.01% as a “rate” risks misinterpretation as an intrinsic anomaly frequency. Required fix: Remove the “Rate (%)” entry for the deduplicated Path‑C row or explicitly state it is not an intrinsic anomaly rate and cannot be compared to per‑survey rates.

P3-M10 (Sec. III.B header p.4–5)
Terminology inconsistency: “Confirmed High‑z QSO Candidates.” The header says “Confirmed,” while the body speaks of “candidates” selected by AE cuts and “at least one detected emission line.” If redshifts are measured and confirmed, list the measurement pipeline; otherwise, drop “Confirmed.” Required fix: Use either “Confirmed high‑z QSOs” with an explicit redshift‑measurement description or “High‑z QSO candidates” consistently.

P3-M11 (Sec. IV.A p.9; Fig. 5 caption)
Aggregation method for the 58.8% SIMBAD‑unmatched “aggregate” is unspecified. It is unclear whether this is a simple fraction across all anomalies, a weighted average, or a median of per‑survey rates, and whether Planck (N/A) is excluded. Required fix: Specify the aggregation method and the denominator used; if surveys with predetermined top‑1% cuts bias the aggregate, say so.

MINOR

P3-m6 (Fig. 1 p.4)
Figure title vs. quarantine status is confusing. The title reads “Spatial distribution of all 319,443 anomalies across 8 archives,” and the legend includes ACT DR6. The caption says ACT “is quarantined and excluded,” but the plotted map clearly includes ACT (as a “before/after diagnostic”). Consider labeling the panel “Cross‑transfer baseline (includes quarantined ACT)” directly in the title to avoid misreading.

P3-m7 (Sec. II.B p.2)
Ambiguous phrasing for σval. You write “µval ≈ 0.0287 … and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143.” As defined, σval should be the validation‑set standard deviation of MSE, not “set” to hit a threshold. Required fix: Rephrase to “Given µval and σval (the validation mean and std), the S = 5 cut corresponds to MSE ≈ 0.143” or provide the actual σval number.

P3-m8 (Sec. III.C p.5 vs Table II p.8)
“84% cool dwarfs” claim is not directly supported by the provided classification table. The UMAP/HDBSCAN statement that 84% are ultra‑cool dwarfs is plausible but Table II reports categories like “Uncategorized” and “NIR excess” without linking them numerically to “M7–T2 dwarfs.” Required fix: Provide the quantitative mapping (counts/fractions) from the latent‑space clusters to astrophysical types to support “84%.”

P3-m9 (Sec. V.D bullets p.10–11; Sec. IV.D p.10)
Overinterpretation risk: “This null result demonstrates that CMB patch anomalies … are dominated by survey‑specific systematics.” A null cross‑correlation suggests non‑common origins, but “demonstrates … dominated by systematics” overstates what is shown. Required fix: Rephrase to “is consistent with dominance by survey‑specific systematics” unless you add quantitative systematics tests.

P3-m10 (Table/figure normalization details)
- Fig. 8 improvements vs. baselines use “+” and “−” signs without a stated convention (improvement vs. degradation). Clarify and ensure consistency with corrected numbers (see P3-E9).
- Several training/inference timings would benefit from explicit inclusion/exclusion of I/O and preprocessing for reproducibility (ties to P3-E10/M7).

NO REPEATS
I did not repeat items already covered in the initial review (e.g., Fisher F0 definition error, SDSS threshold ambiguity, unresolved figure placeholders, catalog‑grade subset inconsistency, HEALPix pixel count/doF mismatch, “20 catalogs” count mismatch, non‑anomalous cross‑survey pair labeled as “independently flagged,” etc.).