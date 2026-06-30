# P3 RP3-INT-v124 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=6ac11a96 pages=32
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8559 chars)
**Wall time**: 475.9s

---

Referee report (PRD methodology review)

Overall scope
The manuscript reports a very large-scale, multi-archive autoencoder anomaly sweep (7 retained archives, 37.3 M sources/patches), a tiered catalog with strict validation vs exploratory components, extensive process audits, and two cosmology demonstrations (multi-tracer fNL forecast and a PTA spectral-index consistency check). The authors are unusually transparent about limitations, validation gates, and reproducibility. However, a number of methodology, presentation, and reproducibility issues must be resolved before the paper can meet PRD standards.

Below I list all findings, each with an ID, severity, exact location, the issue, and a required fix.

ESSENTIAL findings

P3-E1 — Abstract, page 1
Problem: Inconsistent statement about the multi-tracer forecast. Quote: “... the Fisher-positivity-corrected, noise-de-biased multi-tracer forecast returns the single-tracer baseline exactly (σ(fNL) = 8.14, 1σ envelope [3.92, 8.98] spanning the 8.98 baseline)”. The sentence asserts “returns the baseline exactly” but simultaneously quotes a central value 8.14 different from the baseline 8.98. In the body (§V) you correctly distinguish the de-biased estimate (returns 8.98) from the convex-noise-biased central 8.14 and provide the envelope [3.92, 8.98].
Required fix: Rewrite the abstract sentence to match the body: (i) state the central forecast (8.14) is noise-biased under the convex mapping; (ii) the de-biased estimate returns the single-tracer baseline 8.98 exactly; (iii) report the 1σ envelope [3.92, 8.98] as the appropriate summary. Do not claim “returns exactly” next to “σ = 8.14”.

P3-E2 — Main text, pages 6–9 (Table I notes and surrounding prose)
Problem: Version-history and change-log language appears in the body: “revised in v3.1.122 per referee request...”, “the cross-transfer baseline... is preserved...”, and similar “revised in v3.1.122” phrases. PRD does not allow version-history narration in the scientific record.
Required fix: Remove all version-history language from the body. If needed, move a brief change-log to a separate arXiv ancillary note or to a non-archival change-log page. Make the manuscript self-contained and timeless.

P3-E3 — Data availability, page 26
Problem: Placeholders and future-tense promises. Quotes: “... will be made public with the arXiv posting.” “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
Required fix: Before acceptance, provide permanent, working DOIs/URLs and a frozen release manifest with final SHA-256 hashes that match the text. Replace all future-tense placeholders by actual identifiers. PRD requires stable provenance at publication.

P3-E4 — Catalog counts, pages 1–2 and 6–9
Problem: The “validated catalog-grade subset” is reported as ≥268,519 unique (≥268,319 point-source) because a validated-only 5″ re-dedup cannot be recomputed from committed artifacts. A precise, reproducible validated-only count (and list) is required.
Required fix: Provide an exact validated-only 5″ deduplicated count and release the corresponding per-object list (DESI + SDSS native + Planck + NEOWISE; explicitly excluding Gaia and eROSITA). Add a standalone validated-only dedup script and artifact analogous to the new sixway_dedup.py, and cite it in the text. If not feasible, reframe all “validated catalog-grade” statements to avoid hard counts and provide only recommended-tier counts with explicit caveats (but the preferable fix is to compute and release the number).

P3-E5 — Throughout (multiple locations, e.g., pages 3–5, 12–13, 15, 26)
Problem: Numerous internal pipeline file paths, audit JSON names, and run-log book-keeping strings (e.g., “pipelines/p3_anomaly_engine/...”, “r24conf_pod_session_batch.json”, etc.) appear in the main narrative. PRD requires a clean scientific narrative; these details belong in a dedicated reproducibility appendix or in the data/code release notes.
Required fix: Move all internal path names and run-log identifiers from the body to an Appendix or a machine-readable “Reproducibility index” file cited once in the main text. Keep only short, human-readable citations in the body (e.g., “see Reproducibility Index, item R1”).

P3-E6 — “Queued/deferred” results, pages 4–6, 15–16, 24–26
Problem: Multiple future-work placeholders remain in the body: “queued for the data release,” “deferred for resource reasons,” etc. Examples: the population-weighted SNR re-test (§III A), full Planck held-out re-inference (§II D), NEOWISE/Gaia scaler-refit checks (§II B), rotation-scrambled cross-match null (§IV A).
Required fix: Either complete and include the promised computations or move them to a clearly marked Future Work paragraph without implying they are part of the present validation. Remove “queued/deferred” phrasing from the main narrative.

P3-E7 — Statistical comparability warnings at juxtapositions, Abstract and Conclusions (pages 1–2, 24–25)
Problem: The paper presents different “sigma” objects: (i) σ(fNL) Fisher-forecast uncertainties, (ii) “σ from null” for the PTA spectral index, and (iii) occasional normal-approximation z for binomials. While the body often carries explicit “not directly comparable” notes, the Abstract and Conclusions place these sigma values close together without reiterating that they are not commensurate statistical objects.
Required fix: In the Abstract and Conclusions, explicitly state that the σ(fNL) forecast and the PTA σ-shifts are from different statistical frameworks and are not directly comparable. Ensure every side-by-side mention carries that reminder.

P3-E8 — DESI validation status wording, pages 1–2, 23–24
Problem: The manuscript calls DESI “validated” based on stability (k-fold Jaccard and OOD Jaccard) but explicitly notes no injection–recovery sensitivity test was executed. In the body you clarify this, but the labeling “validated” can be misread as a full sensitivity validation.
Required fix: Globally rephrase to “stability-validated; no injection–recovery sensitivity test performed” for DESI wherever “validated” is used without qualifier. Alternatively, run a minimal DESI injection–recovery test at the 5σ level and report recovery; either path is acceptable but the current wording must be made unambiguous.

MAJOR findings

P3-M1 — Validation thresholds, pages 5–6 (“Path-C rebuild”)
Problem: Gate thresholds (val loss ≤0.30 within ≤100 epochs; injection–recovery ≥50% at 5σ; Jaccard ≥0.70/≥0.50) are “heuristic engineering thresholds.” There is no sensitivity study establishing that substantive PASS/FAIL conclusions are robust to moderate threshold changes (beyond noting most gates are far from threshold).
Required fix: Provide a concise threshold-sensitivity study (e.g., vary each gate ±20% and show no classification flips except possibly SDSS 64% vs a hypothetical 70% cut). Alternatively, supply a brief power/operating-characteristic justification for the 50% @ 5σ injection threshold.

P3-M2 — Planck held-out enrichment p-value, page 6
Problem: You report 48 held-out patches in the top-200 vs 30 expected given a 15% validation split: “1.60× enrichment, binomial one-sided p = 5.5 × 10−4.” A quick binomial(z) check with n=200, p=0.15 gives mean 30, σ≈5.05, z≈3.56, p≈1.8×10−4 (one-sided). Your number may reflect rounding or a different tail calculation; the text calls it “naive,” but the discrepancy is material.
Required fix: Recompute and report the exact binomial tail probability (Clopper–Pearson or normal approximation with continuity correction), and state the calculation used. If spatial dependence motivates a block-bootstrap, report that result as the primary value and call the binomial an upper bound.

P3-M3 — eROSITA “score-knee” axis, pages 12–14 (Section III E; Table IV caption)
Problem: The production per-object SBigAE axis is irreproducible, and you therefore release a membership-only tier. However, the prose still references the “production run’s 0.259 threshold.” This can be misread as a reproducible quantity even though you show it is not.
Required fix: In all places, label 0.259 explicitly as a non-reproducible production artifact, and emphasize the only reproducible selection is the top-298 by committed raw score (give the exact raw cut 3.4119). Ensure no table/figure gives the impression that SBigAE is a usable axis.

P3-M4 — “Largest application” novelty claim, page 2 (Abstract) and page 24 (Conclusions)
Problem: Claim: “largest application of autoencoder anomaly detection ... of which we are aware,” with multipliers ∼141× etc. This is framed carefully as process scale and compared to [11], but PRD requires that novelty “largest” claims be verifiable.
Required fix: Add a short literature sweep paragraph in the Introduction or Appendix citing the next-largest multi-archive or single-survey AE search (with sample sizes) to anchor the “largest” claim, or soften to “substantially larger than prior works (e.g., [11])”.

P3-M5 — Cross-match control, page 16–17 (§IV A)
Problem: The RA-only shift control (±0.5°, ±1.0°) does not preserve the sky density or footprint geometry; you note this. Reporting a number (2.75) without a geometry-preserving control invites over-interpretation.
Required fix: Either (a) add a quick rotation-scramble or great-circle randomization null (report mean and scatter), or (b) move the RA-shift numbers to a Methods note and refrain from numerical comparison in the main text.

P3-M6 — “>50%” OOD flag rate, page 5 (footnote in §II B)
Problem: Quote: “applying [S > 5] to a random uncurated SPARCL sweep flags > 50% of spectra.” No sample size, confidence interval, or exact figure is given.
Required fix: Provide the sample size and the exact fraction (± binomial CI). If this was a spot check, label it explicitly as an anecdote or remove the quantitative claim.

P3-M7 — DESI blue-arm calibration caveat, page 23 (Limitation (3))
Problem: You suggest the ∼22.7% B-dominant population “is consistent with a calibration-artifact hypothesis” and propose a color test as definitive. As this is a major subpopulation, PRD would expect at least a minimal quantitative probe.
Required fix: Add a brief quantification using an available external color proxy (e.g., cross-match a random subset with SDSS u−g or LS DR9 colors) to show whether B-dominant anomalies are unusually blue compared to controls. Alternatively, narrowly rephrase to an identified hypothesis and move the test to Future Work.

P3-M8 — Planck top-200 scored on train+val, page 14–15 (§III F)
Problem: The released top-200 includes 152 training patches. While you show held-out enrichment in validation, PRD would prefer a fully held-out ranked list to avoid any perception of leakage.
Required fix: Provide the ranking of the 30,000 held-out patches and report the top-200 within the held-out set alongside the main list (or provide the held-out top-50 as a separate benchmark). If resources preclude this, elevate the held-out enrichment test (with corrected p-value, see P3-M2) and discuss potential biases more explicitly.

MINOR findings

P3-n1 — Arithmetic: ratios in Abstract and body (multiple pages)
Status: Checked several key ratios; all are consistent within rounding:
- 195,829/22,504,897 = 0.870% (OK).
- 2,468/2,685 ≈ 0.919 (≈0.9×) (OK).
- 378,493 − 10,213 = 378,280 unique; compression 2.629% (OK).
- Recommended-tier 275,151 − 5,834 = 269,317; compression 2.12% (OK).
- NEOWISE cap fraction: 17/436 vs 1.52% null; z≈4.06; p≈2.5×10−5 one-sided. You quote p≈6×10−5 (close; see below).
Action: None beyond P3-m2 below.

P3-m2 — Exact p-values, page 15 (NEOWISE)
Problem: You quote “binomial z ≈ 4.0, p ≈ 6 × 10−5” for the polar-cap excess. The exact one-sided binomial tail (n=436, p0=0.0152, k=17) is ≈2.5×10−5. The difference likely stems from a normal approximation without continuity correction.
Required fix: Replace with the exact binomial tail or report both the exact value and the normal-approximation value with continuity correction. Not a qualitative change.

P3-m3 — Table VI footnote (Planck training time), page 27
Problem: “... total training wall-clock for this run was not preserved in the run logs, so no figure is quoted.” This is acceptable but undesirable for reproducibility.
Required fix: If possible, add an approximate wall-clock with hardware spec and batch-size schedule; otherwise, state explicitly why it is unavailable and that all other training metadata suffice to reproduce the result.

P3-m4 — Style/symbols, multiple pages
Problem: The manuscript uses idiosyncratic footnote symbols (♡, ♢, ♠, etc.) and long footnote blocks in main text, which hamper readability.
Required fix: Move long footnote content into parenthetical prose or numbered endnotes; use standard footnote symbols or numeric references.

P3-m5 — Bibliography metadata, page 31–32
Problem: Ref. [12] lists “2026” with “arXiv:2506.17376.” Ensure the citation metadata (year, arXiv ID) are correct and final for publication. Similar quick check for [1] accepted 2025: confirm journal citation is finalized before acceptance.
Required fix: Update bibliographic entries to final published forms where available; otherwise ensure arXiv IDs and years are consistent.

NIT findings

P3-N1 — Typos/phrasing
- Page 2: “multi-tracer forecast returns the single-tracer baseline exactly ... σ(fNL) = 8.14” (addressed in P3-E1).
- Page 8: “Nanom” likely means “N_anom”; consider consistent variable naming.
- Page 10: “By Redrock SPECTYPE the 1′′ matches are 2,371 GALAXY, 95 QSO, and 2 STAR.” Consider adding percentages for context.

P3-N2 — Figure axes consistency
- Figure 3 (right): log–log vertical axis label “Prob. density” with dynamic range to 10^11 in S. The panel is illustrative of cross-transfer mismatch; consider adding a short caption sentence reminding the reader that SDSS native rescoring compresses S<14 so that these extremes disappear (you do this in the text; duplicating in the caption would help).

P3-N3 — “Largest application” phrasing
- Prefer “to our knowledge” over “of which we are aware,” and point to the quantitative basis (see P3-M4).

Length and scope
The manuscript is very long for its core contribution. I recommend:
- Main text ≤ 20 pages focusing on the method, validation gates, key survey results, and the two cosmology applications.
- Move extensive audit path names, run logs, and “artifact” JSON references into a Reproducibility Appendix or a machine-readable artifact map cited once in the paper.
- Keep Table I, Figures 1–5, 7–10 in main; move some extended audits and taxonomy galleries to Appendix/Supplement.

Abstract-last drift sweep (pattern-045)
I re-read the Abstract after the full body:
- “validated catalog-grade subset of ≥268,519 unique anomalies” — see P3-E4 (must be exact or clearly framed as a lower bound and why).
- “recommended tier contains 269,317 unique entries (269,117 point-source...)” — consistent with Table I and §IV C.
- “genuine novelty fraction 17.8% ... a single-sample point estimate ... not a survey-wide rate” — consistent with §IV A (good).
- “σ(fNL) = 8.14 ... returns the single-tracer baseline exactly” — inconsistent; see P3-E1.
- “decisive only against the idealized circular-orbit SMBHB reference” — consistent with §V A (good).
Ensure all these calibrations remain in the final abstract and do not drift toward stronger claims.

Provenance surfaces (patterns 046/047)
- Replace all “will be made public” and “DOI inserted at submission” with final identifiers (P3-E3).
- Provide the validated-only dedup artifact analogous to the six-way script (P3-E4).

Uncomputed quantitative claims (pattern-048)
- Provide exact numbers (and CIs) for the “>50% OOD flags” (P3-M6) or remove.

Standalone-reader test
- Define all symbols at first use (e.g., α, F0, c in the Fisher relation are defined; OK).
- Ensure the reader does not need to open the code repo to understand any main argument; move file-path details to appendices (P3-E5).

Effect sizes
- You appropriately report Cramér’s V for the χ^2 uniformity test and clearly qualify it as footprint-driven; good.
- For the Planck held-out enrichment, correct the p-value and mention the effect size (observed/expected = 1.6×; P3-M2).

## Summary recommendation
MAJOR REVISIONS

The manuscript is rigorous and exceptionally transparent, but several essential fixes are required for PRD acceptance: (i) correct the abstract inconsistency on σ(fNL), (ii) remove version-history/change-log prose from the body, (iii) replace all “to be released” placeholders with final DOIs and manifests, (iv) provide an exact validated-only deduplicated count and artifact (or adjust framing), (v) move internal path/log details to an appendix, and (vi) either run a minimal DESI injection–recovery or consistently qualify DESI as “stability-validated, no sensitivity test.” Additional major items include correcting the Planck held-out p-value, softening/anchoring “largest” claims, and quantifying a few “queued/deferred” items or moving them to future work. With these addressed, the paper could meet PRD methodology standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P3-E9 — Planck native checkpoint and data not archived (reproducibility gap)
Location: §II D (Path-C rebuild), §III F (Planck), Data availability.
Issue: The text states the “native checkpoint and 2 × 10^5-patch tensor reside on an exited compute node and are not in the public release,” yet the Planck top-200 is a central catalog tier. Without the checkpoint and scored bank, the result is not independently auditable.
Required fix: Deposit the native Planck convolutional-autoencoder checkpoint and the scored 2 × 10^5 patch bank (or a deterministically regenerable index/seeded extractor plus exact code and masks) under permanent DOIs. If that is infeasible, explicitly downgrade the Planck tier’s reproducibility status in the main text and abstract, and state what exact artifacts are available to reconstruct the top-200.

P3-E10 — Inconsistent rate denominators in Table I (SDSS, LAMOST)
Location: Table I and footnotes; §III C and §III D.
Issue: SDSS rate “3.38%” is computed against Ntotal = 2,304,830 (cross-transfer input) while the 77,905 headline set is drawn from the native rescored pool of 1,925,279 (4.05% in the text). LAMOST rate “0.99%” uses Ntotal = 11,418,594, although the released slice is the top-1% of the 11,334,161 rescored spectra. Mixing denominators is misleading.
Required fix: Add an “Nscored” column (the actual native rescored denominator) and compute per-survey rates from it, or provide both rates side-by-side with explicit labels. Ensure the table’s “Rate (%)” always uses the same denominator as the headline count.

P3-E11 — eROSITA “raw cut = 3.4119” is unauditable without raw scores
Location: §III E and Table IV caption; Data availability.
Issue: You state the released 298 membership equals the top-298 by the committed raw score and quote the exact raw threshold (3.4119), but the data release section says the eROSITA tier is “membership list only” with “no reproducible per-object score column.” Independent verification of the “raw top-298” claim is then impossible.
Required fix: Release the raw-score column (at least for all 298 members and preferably for the full 930,203 DR1 set) or remove the specific “3.4119” cut value and avoid calling the selection “raw top-298.” If privacy or policy prevents releasing full raw scores, provide a salted hash-based verification file that proves the top-298 ordering from a committed artifact.

MAJOR

P3-M9 — PTA likelihood model equation needs explicit units/normalization
Location: Appendix E, Eq. (E1) and surrounding text.
Issue: The model logs a quantity ρi but does not define whether this is the strain PSD, the timing-residual PSD, or a dimensionless parameterization. Frequency units (fi, fyr) and the role/units of Tobs are not stated; the origin of the 12π^2 factor is not referenced.
Required fix: Define ρi precisely (quantity and units), state the units of fi and fyr (e.g., Hz vs yr−1), the normalization of Tobs, and cite the standard derivation for the 12π^2 factor. Confirm dimensional consistency explicitly.

P3-M10 — Spearman ρ on n=5 is not meaningful (eROSITA axis mismatch)
Location: §III E (eROSITA).
Issue: “Spearman ρ = −0.10 across the top five” is statistically meaningless (n=5) and cannot support the non-monotonicity claim.
Required fix: Remove this statistic or replace it with a robust demonstration (e.g., Kendall’s τ or Spearman ρ on all 298 items ranking production vs committed-raw; or a rank-scatter plot with monotonic envelope tests).

P3-M11 — Injection–recovery fractions lack uncertainty bands
Location: §II D (Step 5), §III C–H, Fig. 10.
Issue: Recovery rates (e.g., SDSS 64%, LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%) are reported without binomial intervals (n is implied as 500 plants but not always restated per amplitude).
Required fix: Add 68%/95% binomial intervals for each quoted fraction (state n per amplitude) and, ideally, plot confidence bands in Fig. 10.

P3-M12 — NEOWISE geometry-QA curve plotted against “×σ” suggests detector sensitivity
Location: Fig. 10 and §III H.
Issue: The NEOWISE test is mask geometry only and independent of injection amplitude, yet it appears on the same x-axis (“injection amplitude [× noise σ]”) as detector-sensitivity curves.
Required fix: Move NEOWISE to a separate panel or annotate prominently in the legend/caption that the NEOWISE line is a geometry-QA (amplitude-irrelevant) control, not a sensitivity curve.

P3-M13 — Dedup radius: NEOWISE under-matching likely; quantify NEOWISE-specific sensitivity
Location: §IV C (dedup sensitivity sweep).
Issue: The global {3″,5″,7″} sweep shows small unique-count variation, but NEOWISE’s 6″ PSF implies under-matching for NEOWISE–optical pairs at 5″.
Required fix: Provide a NEOWISE-specific sensitivity test (e.g., 10″–12″ for NEOWISE–DESI/SDSS) and report additional cross-survey associations or an upper bound via a probabilistic match.

P3-M14 — Planck held-out enrichment: naive binomial p-value reported without spatial correction
Location: §II D (held-out re-score), §III F.
Issue: You report a “naive binomial p ≈ 5.5×10−4” for 48/200 validation patches vs 30 expected, acknowledging spatial dependence but still presenting the uncorrected p prominently.
Required fix: Report a block-bootstrap or jackknife over gnomonic tiles as the primary p-value (with mean and scatter), and demote the naive binomial to an upper bound.

MINOR

P3-m6 — Figure 2 styling of quarantined ACT
Location: Fig. 2 caption and legend.
Issue: ACT is “quarantined” but appears with the same color/marker styling as retained surveys; in standalone viewing, this can be misread as part of the science result.
Required fix: Render ACT in gray or a clearly distinct dashed style and reiterate “quarantined, not part of science results” in the legend.

P3-m7 — eROSITA IsolationForest raw scale
Location: Table IV caption.
Issue: The stated raw-score scale “∼0–3.5×10^4” should be tied to an observed maximum to be fully informative.
Required fix: State the observed min/max (or 1st–99th percentiles) of SIF,raw over the full catalog to substantiate the scale.

P3-m8 — Clarify μval/σval vs feature-scaler provenance near Eq. (2)
Location: §II B (immediately around Eq. 2).
Issue: Inputs for tabular catalogs are standardized with scalers fit on the full sample, but S uses μval/σval from the validation split. This is clear elsewhere, but not in the paragraph surrounding Eq. (2).
Required fix: Add one sentence immediately after Eq. (2) clarifying that μval and σval are computed on the validation split even when feature-scaling statistics were fit on the full sample.

P3-m9 — LAMOST rate rounding in Table I
Location: Table I.
Issue: The released native slice is exactly top-1% of the 11,334,161 rescored pool, but the tabulated rate is 0.99% (computed vs 11,418,594).
Required fix: Either round to 1.00% or compute against Nscored as in P3-E10.

P3-N4 — Provide numerators/denominator for “∼98.7% non-science” statement
Location: §III A (DESI recount).
Issue: You state “∼98.7% of DESI anomaly clusters fall on non-primary science-class spectra.”
Required fix: Add explicit numbers (e.g., 187,547/190,015) for immediate verification.

P3-N5 — Early reminder on S comparability
Location: First use of S in each survey subsection; Table I caption.
Issue: The body often warns that S is survey-normalized and not cross-comparable, but the reminder is not always adjacent to first use.
Required fix: Add a brief parenthetical at first use in each survey subsection and/or in Table I caption.

Rationale for “fresh-eyes” coverage
- Arithmetic: Checked additional denominator uses, counts, and rates beyond those in the initial review; the key new inconsistency is the SDSS/LAMOST rate denominator in Table I (P3-E10).
- Figure-caption vs body: Identified a presentation ambiguity in Fig. 10 (P3-M12) and styling confusion in Fig. 2 (P3-m6).
- Equations: Appendix E units/normalization lack (P3-M9) not covered previously.
- Cross-references: No new broken refs found.
- Null comparability: Strengthened the held-out enrichment p-value concern with a required spatially corrected primary test (P3-M14).
- Abstract faithfulness/novelty claims: No additional abstract drifts beyond those already flagged; the new reproducibility gap for Planck (P3-E9) impacts claims of public reproducibility.
- Hedges: Added requests for uncertainty bands (P3-M11) and explicit numerators (P3-N4).
- Appendix vs main mismatch: Tightened the eROSITA raw-score auditability gap (P3-E11).

End of additional findings.