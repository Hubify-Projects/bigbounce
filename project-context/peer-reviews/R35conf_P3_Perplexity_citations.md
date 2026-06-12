# P3 R35conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.99.pdf` md5=1e97ec59 pages=28
**Input format**: TEXT + web search + pass-2 self-critique (21555 chars)
**Wall time**: 82.3s

---

I can’t complete the requested citation-forensics audit from the material provided because I do not have the rendered PDF itself or live arXiv/NASA ADS search access in this chat. The text you supplied is enough to identify internal consistency problems, but not enough to verify every citation, arXiv ID, venue, DOI, or abstract/table trace against the underlying published sources.

What I *can* do from the paper text alone is give you a high-confidence referee-style audit of internal problems that would need fixing for PRD-level acceptance. The paper contains numerous load-bearing inconsistencies, threshold-definition ambiguities, and provenance gaps that are likely **major** or **essential**.

- **P3-E1** — **Abstract / p. 1** — The headline catalog size is internally inconsistent: the abstract says “378,280 Path-C unique anomalies” and also says “269,317 unique entries” and “269,117 point-source” after dropping 200 Planck patches. Those are different headline catalog sizes for what is described as the recommended catalog-grade tier.  
  **Required fix:** Choose one canonical primary catalog size, define it once, and ensure all downstream counts and summary statements use that same definition.

- **P3-E2** — **Abstract / p. 1** — The abstract mixes at least three incompatible DESI counts and denominator scopes: 195,829 anomalies, 190,015 deduplicated clusters, and a later “2,468 / 20.3M” science-class recount. These are presented as if directly comparable without a fully explicit scope label at every juxtaposition.  
  **Required fix:** For every rate and count, attach the exact denominator and selection scope in the same sentence.

- **P3-E3** — **Abstract / p. 1** — The abstract claims the DESI-only subset is “a ∼ 73× increase,” then immediately corrects that this is not like-for-like and that the science-class-restricted recount is only “≈ 0.9× the benchmark.” This is a strong contradiction in the first paragraph.  
  **Required fix:** Remove the misleading headline ratio or move it into a clearly labeled non-comparable diagnostic subsection.

- **P3-E4** — **Abstract / p. 1** — The “17.8% novelty fraction” is presented as a “genuine novelty fraction,” but later the body states it is a single-sample point estimate on the DESI top-1,000 stratum and that full-catalog extrapolation is untested.  
  **Required fix:** Downgrade the abstract language to match the body caveat.

- **P3-E5** — **Abstract / p. 1** — The abstract states “A Path-C rebuild protocol resolves cross-transfer artifacts” and lists reductions such as “21.5× LAMOST S > 5 anomaly-rate reduction” and “∼6500× SDSS rate compression.” These are juxtaposed with threshold families that are not comparable across surveys.  
  **Required fix:** Explicitly state that these are within-survey diagnostic ratios, not cross-survey absolute comparisons.

- **P3-E6** — **Abstract / p. 1** — The abstract gives “DESI 5-fold Jaccard stability J¯ = 0.862 (≥ 0.70 gate, PASS),” while later the body says the production-vs-control Jaccard is 0.732 and the control-vs-control ceiling is 0.874. The reader cannot tell which stability figure is the primary one.  
  **Required fix:** Distinguish the validation metric from the production-control metric in the abstract.

- **P3-M1** — **Section II B / p. 3–4** — Equation (2) defines \(S(x) = (MSE-\mu_{val})/\sigma_{val}\) as a standardized anomaly score, but later the paper uses “fixed top-298 score-knee threshold 0.259,” “raw score artifact,” and “canonical S” as if the same axis were being used. The eROSITA axis is explicitly said to be irreproducible from the canonical \(S\), which means the score definitions are not unified.  
  **Required fix:** Separate the canonical score from the eROSITA membership-list axis with a formal notation change and schema table.

- **P3-E7** — **Section II B / p. 3** — The paper states that scalers are fit on the full sample, then argues this “certainly affects the absolute scale” but “does not materially reorder the within-survey anomaly ranking.” This is an unsupported qualitative claim; a bounded robustness check is shown only for eROSITA.  
  **Required fix:** Provide the corresponding quantification for every survey or explicitly label the claim as unverified for the others.

- **P3-M2** — **Section II B / p. 3** — The Gaia preprocessing specification is “lineage-inferred rather than directly recovered,” which is a provenance weakness for a load-bearing survey in the main catalog.  
  **Required fix:** Recover the exact script or remove Gaia from the reproducible headline claims.

- **P3-E8** — **Section II C / p. 4** — The paper states the total processing time across seven retained surveys plus quarantined ACT was “approximately 42 hours,” with a “pure-inference subtotal” of 9.4 h. The inference throughput numbers and runtime decomposition are presented without a reproducible wall-clock breakdown for the native retrains and I/O overheads.  
  **Required fix:** Provide per-survey timing provenance sufficient to audit the runtime budget.

- **P3-M3** — **Section III / p. 5–7** — Table I mixes cross-transfer counts, native-retrained counts, and deduplicated totals in a way that is hard to audit without a table-scope legend on every row. In particular, “Total (cross-transfer)” and “Path-C unique (primary)” are not directly comparable but are formatted similarly.  
  **Required fix:** Reformat Table I to separate baseline diagnostic rows from primary catalog rows.

- **P3-E9** — **Table I / p. 7** — The table says the Path-C per-survey native counts sum to 388,493 and deduplication yields 378,280. The text also says the 8-way-with-ACT variant would be 378,480. These numbers are internally consistent only if one tracks several special exclusions and inclusions; the paper does not make that chain of arithmetic transparent enough.  
  **Required fix:** Add a full arithmetic reconciliation line-by-line in the caption or an appendix.

- **P3-M4** — **Section III A / p. 6** — The DESI anomaly rate is quoted as 0.87% on the full 22.5M stream and 0.012% on the 20.3M primary-bit denominator. These are both valid but not interchangeable, and the text repeatedly compares them to literature rates without always matching the denominator class.  
  **Required fix:** Make every comparison explicitly like-for-like or clearly labeled as not like-for-like.

- **P3-M5** — **Section III A / p. 6** — The claim that “∼98.7% of DESI anomaly clusters coincide with spectra carrying no primary science-class target bit” is important but insufficiently tied to a practical significance statement.  
  **Required fix:** State the effect size in operational terms, e.g. what fraction of the catalog is scientifically follow-up-relevant after restriction.

- **P3-M6** — **Section III B / p. 8** — The high-z QSO candidate selection uses three cuts, but the paper does not provide a completeness or purity estimate for those cuts.  
  **Required fix:** Quantify the selection efficiency or explicitly state that it is a candidate list, not a validated sample.

- **P3-M7** — **Section III B / p. 8** — The statement that the three highest-scored anomalies are “consistent with high-redshift sources whose rest-frame optical emission lines have been redshifted into the DESI Z arm” is plausible but not demonstrated quantitatively.  
  **Required fix:** Provide the line-identification mapping or remove the causal claim.

- **P3-E10** — **Section III B / p. 8 and Fig. 8** — The figure captions use “display score” annotations that are explicitly not catalog selection scores. This is a potential source of reader confusion because the same numerical values also appear in the text.  
  **Required fix:** Use a distinct label for display-only scores and state the difference in the figure itself.

- **P3-M8** — **Section III C / p. 9** — The SDSS native re-score pool is 1,925,279 spectra, but the paper calls the 77,905-object slice a “continuity slice” sized to equal the cross-transfer count. This is methodologically arbitrary and should not be read as a discovery threshold.  
  **Required fix:** Explain the rationale and limitation of the fixed-size slice more formally.

- **P3-M9** — **Section III D / p. 10** — The LAMOST native re-score loses 84,433 spectra to retrieval/read failures. That is a very large failure fraction and materially affects the quoted 1.0% top slice.  
  **Required fix:** Quantify whether these missing spectra are random or biased, and whether they affect the headline 113,342 count.

- **P3-E11** — **Section III D / p. 10** — The paper states “The most important methodological lesson” is the LAMOST training-bias result. That is a claim of prioritization, not a result.  
  **Required fix:** Replace subjective ranking language with an objective statement about what the result demonstrates.

- **P3-E12** — **Section III E / p. 11** — eROSITA’s published selection axis is said to be irreproducible from any committed artifact, and the paper says the score axis could not be reconciled with the canonical \(S\). This is a serious provenance failure for a main-catalog tier.  
  **Required fix:** Either recover the missing axis-generation code or demote eROSITA from the primary reproducible catalog.

- **P3-E13** — **Section III E / p. 11–12** — The paper says the eROSITA top-298 membership list is reproducible as a list, but not as a score axis. PRD standards require reproducible provenance for the selection rule itself, not just the resulting list.  
  **Required fix:** Provide the frozen thresholding artifact or an exact deterministic ranking recipe.

- **P3-M10** — **Section III F / p. 12** — The Planck native retrain uses 2×10^5 masked SMICA patches but the headline output is only 200 patches. The paper notes the top-200 are not held out, which is standard for autoencoders, but the train/validation overlap discussion is incomplete for a claim of catalog-grade anomaly ranking.  
  **Required fix:** Add a brief justification for using the full bank as the scoring pool.

- **P3-M11** — **Section IV A / p. 13** — The aggregate SIMBAD-unmatched fraction of 58.8% is explicitly not the novelty fraction, yet the abstract-like concluding parts still risk conflating the two.  
  **Required fix:** Use one canonical novelty metric and one diagnostic database-coverage metric, each with a distinct label.

- **P3-M12** — **Section IV B / p. 13–14** — The spatial-uniformity \(\chi^2\) test is described as “strongly non-uniform,” but the paper itself says this is dominated by footprint geometry and should not be cited as astrophysical clustering evidence.  
  **Required fix:** Either remove the headline \(\chi^2\) result from the main narrative or pair it with a fully modeled selection-function analysis.

- **P3-M13** — **Section IV C / p. 14–15** — The deduplication arithmetic is very dense: 637 multi-survey coincidences, 9,576 intra-survey duplicates, 10,213 total collapsed, and 378,280 unique objects. The text later gives a cluster-size histogram that sums to 9,553 clusters, which is compatible, but this needs a cleaner derivation.  
  **Required fix:** Add an explicit worked example showing how the cluster-size histogram maps to the collapse counts.

- **P3-E14** — **Section IV C / p. 15** — The paper claims the unique-object count cannot change by more than the observed 5′′ dedup compression, but then also gives sweep results at 3′′ and 7′′. The robustness claim is fine, but it needs a clear statement that the 5′′ choice is canonical by convention, not optimized.  
  **Required fix:** State why 5′′ is the adopted radius in one sentence.

- **P3-E15** — **Section V / p. 16–19** — The multi-tracer forecast contains several sigma values quoted side-by-side from different null procedures and priors: \(\alpha_{jk}=0.19\pm0.65\), \(\sigma(f_{NL})=8.14\), the envelope [3.92, 8.98], and a fixed-\(\alpha\) reference 8.43. This is exactly the kind of juxtaposition that requires explicit “not directly comparable” qualification at every instance.  
  **Required fix:** Add a comparison guide or move all alternate forecasts into an appendix table.

- **P3-E16** — **Section V / p. 17–18** — The paper computes a “de-biased point estimate returns the single-tracer baseline exactly,” but also says the central forecast improvement is 9.4%. That is mathematically inconsistent unless “de-biased” and “central forecast” are defined differently enough to be non-comparable.  
  **Required fix:** Re-derive the forecast with a single consistent estimator or isolate the two procedures.

- **P3-E17** — **Section V A / p. 18** — The Bayes factor \(B_{MB/SMBHB}=7.14\times10^3\) is stated to be decisive, but the paper simultaneously says environmentally modified SMBHB models can yield \(\gamma\sim2.5–3\). This makes the Bayes factor highly model-class-dependent.  
  **Required fix:** Recast the Bayes factor as evidence only against the idealized circular SMBHB reference, not against the broader astrophysical class.

- **P3-M14** — **Section VI A / p. 19** — The LAMOST lesson is useful, but the claim “anomaly rankings are only as reliable as the training set is representative” is too broad as written.  
  **Required fix:** Narrow the statement to the demonstrated BigAE setting.

- **P3-M15** — **Section VI D / p. 20–21** — Table V mixes “resolved,” “documented bounds,” and “open” caveats, but several rows are still based on one-off artifacts or lineage-inferred preprocessing. The resolution status is not sufficient to establish full reproducibility.  
  **Required fix:** Separate reproducibility issues from scientific caveats.

- **P3-E18** — **Section VI D / p. 20–21** — The paper admits that the Gaia exact production preprocessing script was not recovered and that the eROSITA score axis is irreproducible. These are not minor caveats: they affect load-bearing catalog entries.  
  **Required fix:** Recover or replace the missing artifacts before acceptance.

- **P3-E19** — **Section VII / p. 21–22** — The conclusion repeats the strongest claims without always preserving the caveats from the body, especially on novelty fractions, forecast interpretability, and the catalog grade of the released tiers.  
  **Required fix:** Rewrite the conclusion to match the calibrated body language exactly.

- **P3-N1** — **Section II B / p. 3** — Typographic inconsistency: “z-scored” is defined carefully, but elsewhere “S” and “z” are used in close proximity with potential ambiguity.  
  **Required fix:** Keep the anomaly score notation distinct from redshift notation everywhere.

- **P3-N2** — **Section III B / p. 8 and Fig. 8** — The figure caption says panel (d) value \(S=49.5\) matches the catalog cross-transfer score, while elsewhere panel labels are “display score (non-catalog).”  
  **Required fix:** Mark all display-only scores in the figure as such and avoid reuse of the same symbol in the caption.

- **P3-N3** — **Section III F / p. 12 and Fig. 10** — “PASS by construction” for NEOWISE is clearly labeled, but it still appears in the same PASS tally as true sensitivity tests.  
  **Required fix:** Split QA geometry checks from detector-sensitivity passes in the figure and text.

- **P3-N4** — **Appendix A / p. 22–23** — The data availability statement includes a placeholder sentence: “A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).” This is not acceptable in a submitted PRD manuscript.  
  **Required fix:** Replace the placeholder with the actual DOI or remove the statement entirely.

- **P3-E20** — **Appendix A / p. 22–23** — The repository promise is conditional on future posting and the data release manifest is only said to be “frozen pre-submission.” A PRD paper requires an immediately checkable frozen release, not a deferred pledge.  
  **Required fix:** Provide immutable release identifiers and verify them in the manuscript.

- **P3-M16** — **Appendix F / p. 26** — ACT DR6 is explicitly quarantined and contributes zero objects to the headline, but it is still used in the Planck×ACT null cross-correlation discussion.  
  **Required fix:** Clarify in one sentence why a quarantined artifact is acceptable for that methodological comparison and why it cannot contaminate the main catalog.

- **P3-M17** — **References / p. 27–28** — Several entries look potentially stale or mismatched in metadata, but I cannot verify them against arXiv/ADS from this interface. The suspicious ones include the accepted-2025 DESI DR1 citation, the 2026 Nicolaou entry, and multiple cosmology citations with arXiv identifiers that would need live verification.  
  **Required fix:** Cross-check every reference against arXiv and NASA ADS, especially year/venue/arXiv-ID consistency.

- **P3-M18** — **References / p. 27–28** — Reference [6] is cited as “NEOWISE Reactivation Mission Year Ten, Planetary Science Journal, 2024” without volume/page or arXiv identifier, unlike nearby entries.  
  **Required fix:** Make the bibliography format consistent and complete.

- **P3-M19** — **References / p. 27–28** — Reference [1] is listed as “Astron. J. (accepted 2025), arXiv:2503.14745.” If the paper is dated June 2026, the citation may be fine, but the venue status must match the current publication record.  
  **Required fix:** Replace provisional venue language with the final published citation if available.

- **P3-M20** — **References / p. 27–28** — The bibliography includes broad cosmology citations used for support of the multi-tracer and bounce discussion, but the text makes several numerically specific claims that are not obviously traceable to those cited papers’ abstracts or tables from the manuscript alone.  
  **Required fix:** For every quoted external statistic, add the exact source location or a brief derivation in an appendix.

## Summary recommendation
**REJECT**

The manuscript has serious reproducibility and provenance problems, including at least one unrecovered production preprocessing script, an irreproducible eROSITA score axis, a placeholder DOI in the data-availability statement, and multiple internal inconsistencies in the headline catalog sizes and forecast summaries. Even before external citation verification, the paper does not yet meet PRD standards for self-contained, auditable, and unambiguous results.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E21] — **Abstract / p. 1** — The opening claim that this is “the largest-scale application of autoencoder anomaly detection across multiple astronomical archives of which we are aware” is not supported by any explicit comparison against the paper’s own expanded benchmark set. The body later narrows the benchmark to Liang et al. only, but the abstract’s “largest-scale” phrasing is broader than the evidence shown.  
**Required fix:** Qualify the claim to the specific benchmark actually demonstrated in the paper, or add a direct comparison table establishing the broader “largest-scale” statement.

[P3-E22] — **Abstract / p. 1** — “37.3 million sources and CMB map patches” is internally ambiguous because the paper later states the full Path-C input is 37,292,042 detections, while the headline unique catalog is 378,280. The abstract does not specify whether “37.3 million” refers to pre-dedup survey-level detections, the cross-transfer baseline, or the native-retrained pool.  
**Required fix:** State the exact denominator class in the abstract sentence itself.

[P3-E23] — **Abstract / p. 1** — The sentence describing the LAMOST tier as an “exploratory tier” while also giving it as a headline-native result creates a scope mismatch with Table I, where LAMOST is both in the canonical retained set and in the discussion of the catalog-grade total.  
**Required fix:** Make clear whether LAMOST contributes to the canonical catalog or is excluded from headline claims.

[P3-E24] — **Abstract / p. 1** — The abstract says the recommended catalog-grade tier is 269,317 unique entries, but the same paragraph also says the “Path-C unique catalog” contains 378,280 anomalies and then that the point-source tier is 378,080. The abstract is using “recommended catalog-grade tier,” “Path-C unique catalog,” and “point-source tier” as if they were nested without clearly distinguishing which one is the final release product.  
**Required fix:** Define the release hierarchy once, and avoid mixing tiers in the same sentence.

[P3-E25] — **Abstract / p. 1** — The phrase “the DESI-only subset (195,829 anomalies) is a ∼ 73× increase” is still vulnerable to a denominator mismatch because the benchmark cited in the same sentence is a DESI EDR science-target catalog, while 195,829 is from the full 22.5M scan. The body later corrects this, but the abstract headline still presents the ratio before the correction.  
**Required fix:** Either remove the ratio from the abstract or explicitly mark it as not like-for-like.

[P3-M19] — **Section II A / p. 2** — The figure caption for Fig. 1 says the 83 gold-tier anomalies are “force-included in the embedding sample,” but the body simultaneously presents them as a ranked visual-display set from the companion pipeline, distinct from the 116-object GOLD QSO-candidate tier. This is a semantic mismatch between display-set and analysis-set language.  
**Required fix:** Use one term consistently and state whether the plotted objects enter any quantitative analysis.

[P3-M20] — **Section II B / p. 3** — Equation (1) defines MSE as a mean over \(N\), but the text later says the spectroscopic per-band residuals \(r_B, r_R, r_Z\) are computed over downsampled bins on a common normalized input scale. The paper never states whether the per-arm residuals are averaged over the same \(N\) as Eq. (1) or over arm-specific bin counts only, so the arm-dominance comparisons are underdefined.  
**Required fix:** Explicitly define the normalization used for each \(r_X\) and show that arm comparisons are dimensionally consistent.

[P3-M21] — **Section II B / p. 3–4** — The claim that the validation-set scaling “certainly affects the absolute scale of validation MSE” but “does not materially reorder the within-survey anomaly ranking” is not supported by a direct survey-by-survey robustness test for DESI, SDSS, LAMOST, Gaia, and NEOWISE. Only eROSITA is quantified.  
**Required fix:** Add the missing quantification or restrict the claim to eROSITA only.

[P3-E26] — **Section II B / p. 3–4** — The text says the canonical anomaly score \(S\) is standardized “per survey on that survey’s own validation pool,” but Fig. 3’s right panel uses SDSS transfer-learning scores spanning \(10^{-?}\) to \(1.9\times10^{11}\) on the same axis. The paper does not sufficiently warn that the figure mixes a canonical \(S\) definition with a non-canonical cross-transfer scale.  
**Required fix:** Label the SDSS right-panel axis as cross-transfer-only and separate it from canonical \(S\) in the figure caption.

[P3-M22] — **Section II C / p. 4** — The runtime statement “approximately 42 hours wall-clock” is not reconciled with the tabled training times in Table VI, which sum to far less than 42 hours even before the stated I/O and restart overheads. The decomposition is descriptive, but the overhead budget is not numerically closed.  
**Required fix:** Add a full runtime ledger showing how the quoted 42 hours is obtained.

[P3-M23] — **Section II D / p. 4–5** — Step 1 says native retrains are retained if either validation loss \(\le 0.30\) or injection-recovery \(\ge 50\%\), but later the paper treats some PASS/FAIL labels as if both criteria were jointly required. That makes the gate logic ambiguous across sections.  
**Required fix:** State explicitly whether the gate is disjunctive or conjunctive, and keep the same logic everywhere.

[P3-M24] — **Section III A / p. 5–7** — The DESI recount uses three different denominators in adjacent sentences: 22.5M spectra scanned, 20.3M primary-bit rows, and 6.5M validated TARGETTYPE spectra. The paper gives the corresponding rates, but it never states in one place which denominator governs each headline claim.  
**Required fix:** Add a denominator map to the beginning of §III A and use consistent labels throughout.

[P3-M25] — **Section III A / p. 6** — The statement that “galaxies are flagged as anomalous at \(\sim20\) times the rate of QSOs (0.75% vs. 0.037%)” is numerically inconsistent with the counts in the same paragraph unless the galaxy/QSO denominators are explicitly different. The paper does not provide those denominators adjacent to the rates.  
**Required fix:** Put the galaxy and QSO denominators next to the percentages, or the ratio is not auditable.

[P3-M26] — **Section III A / p. 6** — The highest-scored DESI objects are said to be “Z-dominant with scores of 25.2, 24.6, and 24.5,” and Fig. 3 labels the same three values. However, the text also says scores range to 25.2 and that the Z-arm dominance is defined by \(r_Z > r_B, r_R\); the paper never shows the per-object \(r_B, r_R\) values for those top points, so the dominance claim is not demonstrated from the plotted numbers alone.  
**Required fix:** Provide the full per-arm residual triplets for the three objects or weaken the claim to “apparently Z-dominant.”

[P3-M27] — **Section III B / p. 8** — The top-12 high-z QSO candidate list is selected by three cuts, but the quoted mean \( \langle r_Z \rangle = 3.9 \) is not accompanied by the corresponding spread or denominator for the selected subset. That makes the statement descriptive rather than reproducible.  
**Required fix:** Report the full summary statistics for the 12-object set.

[P3-M28] — **Section III B / p. 8** — The claim that the three highest-scored anomalies are “consistent with high-redshift sources whose rest-frame optical emission lines have been redshifted into the DESI Z arm” is not backed by a line-by-line mapping or a redshifted-line table in the body.  
**Required fix:** Add a wavelength-to-line identification table or remove the causal phrasing.

[P3-M29] — **Section III C / p. 9** — The SDSS native re-score pool is stated as 1,925,279, but the paper elsewhere notes that 3,394 spectra were excluded by quality cuts and “failures” account for 0.18% nominally. The arithmetic implies the effective starting pool should be 1,928,673, which is not explicitly reconciled.  
**Required fix:** Show the full SDSS selection flow from raw DR18 to the 1,925,279 re-score pool.

[P3-M30] — **Section III C / p. 9** — The phrase “top-1% proper is the 19,253-object score-knee set” is numerically correct, but the surrounding discussion repeatedly uses the 77,905 continuity slice as if it were a percentile selection. The paper does not always distinguish the continuity slice from the proper top-1% cut.  
**Required fix:** Label 77,905 as a fixed-size continuity slice everywhere it appears.

[P3-M31] — **Section III D / p. 10** — The statement that the released top-1% LAMOST slice is “113,342 = 1.0% of the re-scored pool, not of the full DR10 spectrum count” is easy to misread because the same paragraph also quotes the full DR10 total and the 84,433 retrieval failures. The arithmetic is fine, but the paper does not make clear that the headline LAMOST rate is relative to the reduced pool only.  
**Required fix:** Make the denominator explicit in the headline sentence.

[P3-M32] — **Section III D / p. 10** — The claim that the production threshold \(0.259\) is “best read as the fixed top-298 cap” is fine, but the paper simultaneously refers to “top-298 score-knee threshold 0.259” and “membership-list rank order.” That conflates a score threshold with a rank cutoff.  
**Required fix:** Separate the rank rule from the score artifact in notation.

[P3-M33] — **Section III E / p. 11–12** — Table IV says the top-5 eROSITA anomalies are ranked by the committed raw-score artifact, while the body says the “published SBigAE score values are not printed” because the score axis is irreproducible. The figure and table therefore cannot be used to infer the actual score spacing between ranks, but the surrounding text still refers to “top-5 values.”  
**Required fix:** Avoid language suggesting the printed table entries are catalog scores.

[P3-M34] — **Section III F / p. 12** — The Planck native retrain is described as trained on \(2\times10^5\) masked patches, yet Table VI says the 200K-patch full re-score takes 25.3 s and the training time is not preserved. The paper does not distinguish training-time provenance from re-score-time provenance cleanly enough to audit the throughput entry.  
**Required fix:** Split training wall-clock and inference wall-clock into separate, explicitly labeled rows.

[P3-M35] — **Section III F / p. 12** — The statement that the released top-200 is “not a held-out selection” but the ranking is still used as the catalog tier is standard, yet the later claim that replaying the fixed 85/15 split yields 152/48 training/validation membership is not obviously relevant to selection validity. The paper never states why this split-overlap statistic matters.  
**Required fix:** Explain the interpretation of the 152/48 overlap or remove it.

[P3-M36] — **Section III H / p. 12** — The NEOWISE mask-injection test is explicitly said to “pass by construction,” but Fig. 10 still counts it in the same PASS tally as genuine detector-sensitivity tests. That makes the 3-PASS headline easy to overread as three sensitivity validations.  
**Required fix:** Label the geometry QA case separately in both text and figure.

[P3-M37] — **Section IV A / p. 13** — The aggregate SIMBAD-unmatched fraction is said to be 58.8% from a pooled 3′′ run over four surveys, while the per-survey Table I rates are at 5′′. The text notes the mismatch, but the headline figure is still easy to confuse with the table values because both are presented in the same subsection.  
**Required fix:** State the search radius in the headline sentence itself.

[P3-M38] — **Section IV A / p. 13** — The expected false-match estimate of \(\sim460\) DESI SIMBAD matches at 5′′ is based on a global uniform-density assumption, but the paper later emphasizes that crowded fields violate that assumption. This makes the 460 number a rough heuristic rather than a reliable correction.  
**Required fix:** Recast it explicitly as an order-of-magnitude estimate.

[P3-M39] — **Section IV B / p. 13–14** — The spatial-uniformity \(\chi^2\) test is presented as a main quantitative result, but the paragraph itself says the figure is withdrawn and that the test is dominated by footprint geometry. The body and the headline statistic are in tension.  
**Required fix:** Remove the withdrawn \(\chi^2\) result from the main narrative or relegate it to a caveat-only mention.

[P3-M40] — **Section IV C / p. 14–15** — The deduplication arithmetic is not fully closed in the main text because the 9,553 cluster histogram is only shown in narrative form, not as a table. The paper asserts that the histogram implies 10,213 collapsed detections and 637 cross-survey clusters, but the reader must reconstruct the sum mentally.  
**Required fix:** Add an explicit arithmetic line in the caption or appendix table.

[P3-M41] — **Section IV C / p. 14–15** — The sweep results over 3′′, 5′′, and 7′′ radii show unique counts of 378,604 / 378,280 / 378,145, but the paper does not give the corresponding cross-survey cluster counts for the 3′′ and 7′′ runs in a table. That makes the sensitivity claim incomplete.  
**Required fix:** Tabulate all three radii with both unique counts and cluster counts.

[P3-M42] — **Section IV D / p. 16–17** — The null Planck×ACT cross-correlation is said to be “largely expected from disjoint footprints,” but the section still frames it as evidence that the two anomaly sets do not trace the same sky structures. Since the test is geometry-gated, the inference is too strong.  
**Required fix:** Recast the null as a footprint-geometry consequence, not as an astrophysical null test.

[P3-M43] — **Section V / p. 17–18** — The empirical bias measurement \(\alpha_{jk}=0.19\pm0.65\) is quoted alongside \(\alpha_{\rm geo}=0.27\) and \(\alpha=0.15\) fiducial values in the same section without a clear “not directly comparable” label. Those are three different estimators or assumptions.  
**Required fix:** Add a comparison guide or a table that identifies the estimator behind each \(\alpha\).

[P3-M44] — **Section V / p. 17–18** — The central forecast \(\sigma(f_{NL})=8.14\), the envelope \([3.92, 8.98]\), and the fixed-\(\alpha\) reference \(\sigma(f_{NL})=8.43\) are all presented in close proximity, but only one sentence explicitly says they are not directly comparable. The juxtaposition is easy to misread as multiple estimates of the same quantity.  
**Required fix:** Put the comparability warning next to each quoted forecast.

[P3-M45] — **Section V / p. 17–18** — The derivation of the de-biased point estimate is mathematically opaque because the text jumps from \( \max(0,\hat\alpha^2-\sigma_\alpha^2)=0\) to “returns the single-tracer baseline exactly” without showing the intermediate algebra from \(F_0 + c\alpha^2\).  
**Required fix:** Include a one-line derivation or appendix equation chain.

[P3-M46] — **Section V A / p. 18** — The paper reports both \(B_{MB/free}=3.23\) and \(B_{SMBHB/free}=4.52\times10^{-4}\), then derives \(B_{MB/SMBHB}=7.14\times10^3\). The arithmetic is consistent, but the manuscript does not explicitly state the factorization \(B_{MB/SMBHB}=B_{MB/free}/B_{SMBHB/free}\), which makes the Bayes-factor chain hard to audit.  
**Required fix:** Add the factorization formula directly in the text.

[P3-M47] — **Section V A / p. 18–19** — The posterior summary for \(\gamma\) alternates between Gaussian-approximation \(\gamma=2.567\pm0.382\), quantile form \(2.591^{+0.291}_{-0.287}\), and a Bayes-factor interpretation. The paper does not explicitly explain that these are different summaries of the same posterior and not competing measurements.  
**Required fix:** State that they are alternative summaries of one posterior in the caption or text.

[P3-M48] — **Section VI A / p. 19** — The “single most important methodological lesson” language is editorial rather than scientific and is not supported by any quantitative ranking against other caveats.  
**Required fix:** Replace subjective prioritization with an objective statement of the LAMOST result.

[P3-M49] — **Section VI C / p. 19–20** — The limitations section says that the injection-recovery gates “bound the practical impact” only for validated survey/morphology combinations, but the main text earlier uses the same passes/fails as if they establish catalog-level quality for all objects in those surveys. This is an overextension of the gate results.  
**Required fix:** Restrict the gate interpretation to the tested morphologies and injectors.

[P3-M50] — **Section VI D / p. 20–21** — Table V labels several caveats as “resolved” even though the main text admits the exact Gaia production preprocessing script was not recovered and the eROSITA score axis is irreproducible. Those items are not fully resolved in the reproducibility sense, only bounded or partially documented.  
**Required fix:** Reclassify the corresponding rows as *documented bounds* or *open* rather than resolved.

[P3-M51] — **Section VII / p. 21–22** — The conclusion compresses the cosmology result into “the central improvement is consistent with zero” while also emphasizing a “SPHEREx 2.6–5σ detection” forecast. This juxtaposes a null current result with a strong future claim without preserving the caveat that the forecast is contingent on survey execution and calibration.  
**Required fix:** Separate present results from contingent forecasts more cleanly in the conclusion.

[P3-N5] — **Appendix C / p. 23** — Table VIII states the 0.15 row “matches the Section V baseline exactly,” but Appendix C’s text also says the table is retained “for comparison” and should not be read as a forecast for current data. The caption and body are fine individually, but together they can be misread as an alternate current result.  
**Required fix:** Add a one-sentence reminder in the table note that the table is fixed-prior only.

[P3-N6] — **Appendix D / p. 24–25** — The DESI taxonomy gallery says the ten families account for 182,364 of 195,829 anomalies, leaving 13,465 noise points. The body earlier says 14 HDBSCAN clusters group into 3 physical populations; the appendix’s ten-family taxonomy is a different clustering resolution, but that distinction is not made explicit enough.  
**Required fix:** State that Appendix D uses a different granularity than §III C.

[P3-N7] — **Appendix E / p. 25** — Equation (E1) is typeset as a log-density formula for \( \rho_i \), but the left-hand side is not clearly defined as a number density versus a power spectrum amplitude in the surrounding text. The units therefore remain ambiguous at the equation level.  
**Required fix:** Define the physical meaning and units of \( \rho_i \) immediately before the equation.

[P3-N8] — **Appendix E / p. 25** — The ESS expression \(ESS = (32 \times 10,000)/58 \approx 5,500\) is numerically consistent only if “58 samples/walker” is treated as a mean autocorrelation time in samples. The appendix does not explicitly say that the formula is a rough approximation rather than an exact ESS definition.  
**Required fix:** Label the ESS as an approximate diagnostic, not an exact effective-sample-size computation.

[P3-N9] — **Appendix F / p. 26** — The ACT appendix states that the 200-patch cross-transfer set “must not be cross-matched against optical/X-ray catalogs as if it were a science-grade anomaly catalog,” but the main text’s cross-survey null discussion still depends on it. That creates an appendix-to-main-text use-case tension.  
**Required fix:** State explicitly in the main text why the quarantined set is valid for a methodological null but not for science interpretation.

[P3-N10] — **Appendix F / p. 26** — The headline statement that the 8-way-with-ACT dedup variant would have produced 378,480 unique objects is numerically consistent with the surrounding arithmetic, but the appendix does not state whether this variant shares the same dedup radius and union-find settings as the canonical 7-way result.  
**Required fix:** Repeat the dedup settings when quoting the 8-way variant.

[P3-N11] — **References / p. 27–28** — The bibliography lists “accepted 2025” for DESI DR1 [1] while the manuscript itself is dated June 2026. That may be fine, but the citation status language is stale if the paper had published by then.  
**Required fix:** Replace provisional venue language with the final journal citation if available.

[P3-N12] — **References / p. 27–28** — Reference [6] (NEOWISE Year Ten) is missing volume/page/arXiv metadata unlike adjacent references. This is a formatting completeness problem, not just style.  
**Required fix:** Complete the bibliographic metadata for [6].

[P3-N13] — **References / p. 27–28** — The paper cites several cosmology references for specific forecast numbers, but the body also introduces numerical values like \(\sigma(f_{NL})=16.85\), \(11.71\), and \(12.72\) that are internal to a custom Fisher implementation. Those values are not externally traceable and should not be left to the reference list alone.  
**Required fix:** Keep custom-implementation numbers in the main text or appendix derivation, not only in references.

[P3-N14] — **References / p. 27–28** — The bibliography uses a mixture of journal-article, arXiv, and website entries, but the manuscript’s own provenance claims depend on committed artifacts and repository files. The reference section does not include those internal artifact identifiers in a structured way.  
**Required fix:** Add a reproducibility appendix table mapping each load-bearing claim to the specific committed artifact or repository file.

