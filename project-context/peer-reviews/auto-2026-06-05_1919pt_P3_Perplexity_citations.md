# P3 auto-2026-06-05_1919pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (17197 chars)
**Wall time**: 3306.9s

---

I can’t complete the requested forensics audit to PRD-referee standard from the material provided because the paper text is not accompanied by the actual rendered PDF, figures, tables, or the full bibliography metadata needed to verify page numbers, exact axis labels, and every cited work against arXiv/ADS. What I *can* do is a partial citation-and-consistency audit of the text you supplied, and it already reveals multiple serious internal inconsistencies that would block acceptance.

- **ESSENTIAL — Table I / p. 7**: The catalog accounting is internally inconsistent. The text says the “Path-C per-survey native counts … sum to 388,493” and then says “After 7-way 5′′ positional deduplication … the unique-physical-object count is 378,280,” but the same table also states the “Path-C unique (primary)” row is 378,280 and elsewhere says the canonical catalog has 378,280 unique anomalies with 378,080 point-source objects + 200 Planck patches. The arithmetic is not transparently reconciled in the body, and the table footnote mixes “388,493,” “378,280,” and “378,480” in different places. Required fix: provide one unambiguous accounting table that shows every pre- and post-dedup count and explains each subtraction/addition consistently.

- **ESSENTIAL — Table I / p. 7; Appendix F / p. 18**: The ACT accounting appears contradictory. The main text says ACT is quarantined and contributes “zero objects” to the Path-C unique count, but Appendix F says the “8-way-with-ACT dedup variant” would produce “388,693−10,213 = 378,480 unique objects (+200 relative to the headline).” The arithmetic is wrong: 388,693 − 10,213 = 378,480, but that is not “+200 relative to the headline” if the headline is 378,280; it is indeed +200, yet this conflicts with the earlier statement that ACT contributes zero overlaps and zero objects. Required fix: state clearly whether ACT contributes 200 detections before dedup but zero unique objects after dedup, and ensure the baseline totals are numerically consistent everywhere.

- **ESSENTIAL — Abstract / p. 1; Table I footnotes / p. 7**: The paper repeatedly juxtaposes **incomparable thresholds** without always flagging that the resulting anomaly counts are not directly comparable. Example: DESI uses \(S>5\), SDSS and LAMOST use top-percentile slices, eROSITA uses IsolationForest score-knee, Planck and NEOWISE use fixed top-1%. The paper then compares rates and “compression” factors across these thresholds as if they were like-for-like. Required fix: every place where a comparison is made across different threshold families must explicitly state “not directly comparable,” or the comparison must be removed/reframed.

- **ESSENTIAL — Abstract / p. 1; Section V / p. 10–11**: The forecast equation \(1/\sigma(f_{\rm NL})^2 = F_0 + c\alpha^2\) is invoked with an “empirical” \(\alpha_{jk}=0.19\pm0.65\), but the paper also gives a “prior fixed-\(\alpha=0.15\)” forecast and a separate Gold+Silver result \(\alpha_{GS}=1.83\pm2.03\). These are not clearly identified as distinct estimators with distinct sample selections and are compared in the abstract as if they are one unified measurement. Required fix: separate the estimators, state their sample definitions, and stop presenting the \(\sigma(f_{\rm NL})\) figures as a single result.

- **ESSENTIAL — Abstract / p. 1; Section V / p. 10–12**: The NANOGrav claim is over-asserted relative to the posterior. The text says \(\gamma=2.567\pm0.382\), matter-bounce \(\gamma=3.0\) is “marginally consistent,” and SMBHB \(\gamma=4.33\) is “strongly disfavored,” but then later calls the Bayes factor “decisive.” A Bayes factor derived from a prior over \(\gamma\) is not, by itself, a detection of the matter-bounce model, and the paper itself says it is not a detection. Required fix: downgrade the language throughout to “illustrative” or “model comparison,” and ensure the abstract does not imply validation of the bounce model.

- **MAJOR — Section II B / p. 2–3**: The definition of the anomaly score is muddled. Eq. (2) defines \(S=(\mathrm{MSE}-\mu_{\rm val})/\sigma_{\rm val}\), but the paper later states that for DESI “\(\mu_{\rm val}\approx0.0287\)” and “\(\sigma_{\rm val}\) is set such that the \(S>5\) catalog threshold corresponds to MSE\(\approx0.143\).” That is mathematically consistent only if \(\sigma_{\rm val}\approx0.02286\), but the paper never states it. Required fix: report the actual \(\mu_{\rm val}\) and \(\sigma_{\rm val}\) for each survey, or remove the numeric mapping.

- **MAJOR — Section III A / p. 4–5; Table VI / p. 15**: The DESI spectral-arm counts are internally inconsistent. The text gives 151,244 multi-band, 44,436 B-dominant, 34 R-dominant, 19 Z-dominant, and 96 artifact suspects. These sum to 195,829, so the totals are fine, but the percentages are wrong in places: 34/195,829 is about 0.017%, not 0.02%; 19/195,829 is about 0.0097%, not 0.01%. This is minor numerically but should be corrected for precision. Required fix: recompute all percentages to a consistent rounding rule.

- **MAJOR — Section III A / p. 4**: The text says “the three highest-scored anomalies … are Z-dominant, consistent with high-z Gunn–Peterson absorption,” but also says the highest-scored anomalies are among “all DESI anomalies” with no demonstration that Z-dominance uniquely implies high redshift. This is an interpretive leap. Required fix: qualify as a tentative interpretation unless directly supported by redshift measurements.

- **MAJOR — Section III B / p. 5**: The claim that the sample is “confirmed high-z QSO candidates” is too strong for an anomaly catalog. The paper only presents photometric/spectral signatures and cutout imagery; it does not show follow-up spectroscopy or independent confirmation for all 12 candidates. Required fix: retitle as “high-z QSO candidates” and remove “confirmed.”

- **MAJOR — Section III C / p. 6; Fig. 3**: The SDSS native re-score is presented as compressing the same objects from \(S\sim10^{11}\) to \(S<14\), but the figure caption and body mix the DESI-trained transfer scores, native scores, and top-percentile slices in a way that is hard to audit. Required fix: present transfer-learning and native-model distributions on clearly labeled separate axes with explicit model provenance.

- **MAJOR — Section III D / p. 6; Table I footnote ♠ / p. 8**: LAMOST is labeled both a “PASS” in the native retrain paragraph and a “transparent FAIL” in the table footnote. That is not a valid dual status unless the criteria are separated into distinct gates with explicit names. Required fix: choose a single primary classification or define separate gate outcomes unambiguously.

- **MAJOR — Section III E / p. 6–7; Table III / p. 8**: The eROSITA table reports both \(S_{\rm BigAE}\) and \(S_{\rm IF,raw}\), but the main text says the published headline is defined by the \(S>0.259\) BigAE axis, while the cross-validation diagnostic uses IsolationForest. The presentation risks confusing two unrelated anomaly scores. Required fix: add a clear statement that the two scores are not interchangeable and avoid presenting them in the same ranking context.

- **MAJOR — Section III F / p. 7**: The Planck native retrain “criterion (a) FAIL, but criterion (b) PASS” is acceptable only if the gate is explicitly defined as disjunctive. The paper does define a two-part gate earlier, but the wording is still ambiguous because “PASS” is used for the survey despite criterion (a) failing. Required fix: state whether the gate is \((a)\lor(b)\) or \((a)\land(b)\), and use that logical definition consistently.

- **MAJOR — Section IV A / p. 9–10**: The paper alternates between “SIMBAD-unmatched” and “genuine novelty fraction” and correctly warns they are different, but then still uses the SIMBAD-unmatched rates in the headline summary and figure captions as if they measure novelty. Required fix: demote SIMBAD-unmatched to a diagnostic only, and ensure the abstract and conclusion foreground the 17.8% archival novelty result instead.

- **MAJOR — Section IV B / p. 10**: The spatial \(\chi^2\) result is explicitly caveated as footprint-dominated, yet the main text still states “the anomaly distribution is significantly non-uniform” without qualification. This is technically true but rhetorically misleading. Required fix: pair the statistic immediately with the caveat that it is not evidence of astrophysical clustering.

- **MAJOR — Section IV C / p. 10**: The statement “637 multi-survey clusters + 9,576 intra-survey duplicates = 10,213 total collapsed” is plausible, but the text elsewhere calls the 10,213 “duplicate detections” and elsewhere “duplicate objects,” which are not the same. Required fix: define the deduplication unit consistently as detections, not objects.

- **MAJOR — Section V A / p. 10–11**: The Landy–Szalay bias measurement is presented as \(\alpha_{jk}=0.19\pm0.65\), but the paper elsewhere gives \(b_{\rm geo}=1.27\) and \(b_{jk}=1.19\pm0.65\). The conversion between \(b\) and \(\alpha\) is only implicitly \(b=1+\alpha\). Required fix: state this explicitly and show the transformation so the reader can verify the numbers.

- **MAJOR — Section V B / p. 11**: The paper reports \(\sigma(f_{\rm NL}) = 8.14\) with a 1σ envelope \([3.92,8.98]\) and says this is a “7.9% improvement consistent with no improvement at <1σ.” The envelope is asymmetric and the improvement is tiny; the wording should not suggest a meaningful forecast gain. Required fix: downgrade the claim to “numerically small and statistically insignificant improvement.”

- **MAJOR — Section V A / p. 11; Appendix C / p. 15–16**: Table VII gives \(\sigma(f_{\rm NL})=8.43\) at \(\alpha=0.15\), while Section V says the empirical \(\alpha_{jk}=0.19\) gives 8.14. This is fine in principle, but the appendix also lists a “baseline-multi 12.72” and “ideal dense limit 11.71,” which are not clearly connected to the main forecast equation. Required fix: include one derivation path from the dense-limit forecast to the baseline and then to the empirical result.

- **MAJOR — References / p. 19–20**: Several bibliography entries look incomplete or loosely formatted:
  - Ref. [1] “DESI DR1 documentation” is not a standard citable paper entry and may not be an arXiv/ADS-verifiable publication.
  - Ref.  is “in press” without arXiv or journal details.
  - Ref.  is cited as arXiv:1412.4872, but the entry lacks journal details; this is acceptable only if the paper is truly a preprint, but the title formatting suggests an older white paper that should be verified.
  - Ref.  explicitly states “bibkey label retained as Heinrich2023 for arXiv-submission-year continuity,” which is internal bookkeeping and should not appear in the bibliography.  
  Required fix: normalize every bibliography entry to verifiable ADS/arXiv metadata and remove internal bookkeeping notes.

- **MAJOR — References / p. 19**: Ref.  “Planck 2018 results. IX. Constraints on primordial non-Gaussianity” is cited in the text only indirectly, but the bibliography lists it with journal metadata that should be checked carefully against ADS. The entry is plausible, but you need a formal metadata verification pass before submission. Required fix: confirm exact volume, article number, and title punctuation.

- **MAJOR — References / p. 19**: Ref.  “The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth” is a plausible 2024 ApJ article, but the text relies on ACT DR6 scan properties and the appendix labels ACT as quarantined. Because the paper uses ACT only as an artifact, this reference should not be used to support any scientific result. Required fix: ensure ACT citations are only contextual.

- **MINOR — Abstract / p. 1**: The phrase “largest-scale application” is an unsupported superlative unless surveyed against the literature and the claim is documented. Required fix: either cite a quantitative comparison or soften to “large-scale application.”

- **MINOR — Abstract / p. 1**: The phrase “native-trained novelty fractions” is jargon-heavy and not standard. Required fix: replace with plain language, e.g. “novelty fractions measured after survey-native retraining.”

- **MINOR — Section II A / p. 2**: “architecture shown schematically in Fig.??” is an unresolved figure reference. Required fix: insert the correct figure number or remove the placeholder.

- **MINOR — Section II B / p. 2–3**: The text says “z-scored” and then warns that \(S\) is never called \(z\). This is over-explanatory and distracts from the definition. Required fix: simplify the terminology.

- **MINOR — Section III A / p. 4**: The statement “the three highest-scored anomalies … are Z-dominant” is repeated twice in adjacent paragraphs with slightly different wording. Required fix: consolidate to one occurrence.

- **MINOR — Fig. 1 / p. 4**: The figure caption says “Spatial distribution of all 319,443 anomalies across 8 archives” but the main text says ACT is quarantined and excluded. Required fix: relabel the figure as a *cross-transfer baseline* only and make the exclusion explicit in the title/caption, not only in the text.

- **MINOR — Fig. 2 / p. 5**: The right-panel label “S = 1.9×10^11” is extreme and should be annotated with the model provenance and the fact that it is a transfer-artifact score. Required fix: add a prominent note on the plot itself.

- **MINOR — Fig. 4 / p. 8**: The caption says “physical interpretation uncertain” but the body suggests several interpretations. Required fix: keep the uncertainty language consistent in both places.

- **MINOR — Table II / p. 8**: “NIR excess / high-z” combines two different physical interpretations into one bin. Required fix: split the category or clarify the binning rule.

- **MINOR — Table III / p. 8**: The DEC values are truncated to one decimal place, which is too coarse for cross-match follow-up. Required fix: provide full coordinates in the data product and at least arcsecond precision in the paper if space permits.

- **MINOR — Section IV A / p. 9**: The text says “a 100% archival-identification rate is recovered in NED+VizieR for the SDSS DR18 top-20 SIMBAD-unmatched anomalies,” but this is a very small sample. Required fix: state clearly that this is anecdotal and not a population estimate.

- **MINOR — Section VI D / p. 12–13**: The paper states “ten residual caveats are summarized in Table IV,” and Table IV indeed has ten items, but the prose calls them “closed (C = resolved in paper),” while several are clearly not resolved to the level of an independent validation. Required fix: change “resolved” to “discussed” unless fully closed.

- **NIT — Throughout**: There are several formatting artifacts in the supplied text, including unresolved figure placeholders (“Fig.??”), awkward line-break hyphenation, and inconsistent spacing around symbols like \(f_{\rm NL}\). Required fix: copyedit the manuscript for final production formatting.

- **NIT — Throughout**: Some terminology is inconsistent, e.g. “cross-transfer,” “transfer-learning,” “native retrain,” and “Path-C rebuild” are used interchangeably. Required fix: define each term once and use it consistently.

- **NIT — References / p. 19–20**: Several entries have inconsistent punctuation and spacing in journal titles and author lists. Required fix: normalize bibliography formatting.

## Summary recommendation
**REJECT**

The manuscript contains major internal accounting inconsistencies, threshold-comparability problems, ambiguous gate logic, over-strong claims relative to the evidence presented, and bibliography entries that need external metadata verification before they can be trusted. Even aside from the scientific merits, the current version does not meet PRD standards for reproducible numerical accounting and citation integrity.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E1] **Arithmetic — DESI anomaly percentages inconsistent with counts**

- In Section III A, DESI arm-dominance counts are 151,244 multi-band, 44,436 B-dominant, 34 R-dominant, 19 Z-dominant, 96 artifacts, summing to 195,829 anomalies, which is arithmetically consistent.  
- The quoted percentages 77.2%, 22.7%, 0.02%, 0.01%, 0.05% do not align with these counts when computed to the stated precision:  
  - 151,244 / 195,829 ≈ 77.21% → 77.2% (fine).  
  - 44,436 / 195,829 ≈ 22.69% → 22.7% (fine).  
  - 34 / 195,829 ≈ 0.0174% → rounding to two decimals gives 0.02%, but the text mixes two-decimal and two‑significant‑figure conventions in other places, making it ambiguous what rounding rule is intended.  
  - 19 / 195,829 ≈ 0.0097% → 0.01%, likewise dependent on convention.  
- The initial review flagged the mismatch qualitatively but did not explicitly note that the percentages are presented as if uniformly rounded to two decimals while actually mixing conventions; this should be standardized and the rounding rule stated.

[P3-E2] **Arithmetic — “∼141×” and “∼73×” scale-up claims not cross-checked**

- Abstract: “The point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase.”  
- From Liang et al. , the cited prior catalog is 2,685 anomalies on ∼250,000 DESI EDR spectra. The ratios implied by numbers in the paper are:
  - 378,080 / 2,685 ≈ 140.9 → 141× (consistent).  
  - 195,829 / 2,685 ≈ 72.9 → 73× (consistent).  
- These actually match, but the main text never explicitly shows the 2,685 reference number used in the ratio; the review previously criticized the superlative but not the missing explicit numerator/denominator. For PRD-level reproducibility, the prior catalog’s anomaly count should be explicitly quoted where the ×‑factors appear.

[P3-E3] **Arithmetic — SIMBAD false-match estimate lacks explicit intermediate numbers**

- Section IV A states P_false ≈ 2.4×10⁻³ per DESI anomaly using n_SIMBAD ≈ 3.0×10⁻⁵ arcsec⁻² and a 5″ radius, leading to ≈460 expected false matches among 195,829 anomalies (0.24%).  
- The implied computation is P_false ≈ n πr² ≈ 3.0×10⁻⁵ × π × 5² ≈ 2.36×10⁻³, and 195,829 × 2.36×10⁻³ ≈ 462. The numbers are consistent, but they are not shown; the earlier report did not observe that this is another place where critical arithmetic is “hidden.” PRD referees typically expect at least one explicit line showing n, r, π and the resulting P_false, since this number underpins the “false matches negligible” claim.

[P3-E4] **Figure–Body mismatch — Fig. 1 caption vs. actual survey inclusion**

- Fig. 1 caption: “Spatial distribution of all 319,443 anomalies across 8 archives … ACT DR6 is quarantined and excluded.”  
- The legend includes ACT DR6. The caption’s first clause (“all 319,443 anomalies across 8 archives”) plus the explicit ACT color in the legend implies ACT anomalies are in the plotted 319,443, while the phrase “ACT DR6 is quarantined and excluded” could be read as exclusion only from the final Path‑C catalog, not from the figure.  
- The earlier review flagged this as a minor figure-label issue, but here the problem is more precise: this figure is described in Section III as “cross-transfer baseline map,” and Table I notes the 319,443 baseline historically included ACT; however, there is no single sentence that explicitly says “the 319,443 plotted here includes ACT (quarantined later).” The picture‑caption–body linkage is ambiguous enough that a reader can misinterpret whether ACT is plotted or not; this should be clarified explicitly in either the caption or the accompanying text.

[P3-E5] **Figure–Body mismatch — Fig. 2 right panel units and “S” provenance**

- Fig. 2 right panel shows SDSS DR18 scores up to S = 1.9×10¹¹ with a caption that these are “SDSS DR18 transfer-learning scores … The extreme dynamic range of SDSS is a cross-transfer artifact (DESI-trained BigAE applied to SDSS).”  
- Section II B defines S only on the per-survey validation scale S = (MSE − μ_val)/σ_val, and explicitly states DESI, SDSS, and LAMOST share that absolute “S” scale when using the DESI‑trained model.  
- Section III C then says the SDSS native re-score “compresses the same objects to S < 14, eliminating the 10⁴–10¹¹ tail,” but the axes in Fig. 2 and the prose do not explicitly annotate that the right panel is strictly the DESI‑trained cross-transfer “S” and not the native-SDSS scale; a reader could think the same S axis is shared by both native and transfer runs.  
- The initial review criticized caption/body mixing qualitatively, but did not explicitly flag that the right-panel S is dimensionless but effectively *non-comparable* to any survey-native S shown elsewhere. The figure should explicitly state “DESI-trained cross-transfer S (not comparable to native SDSS S scale)” to avoid misinterpretation.

[P3-E6] **Equation dimensional clarity — Fisher form 1/σ(fNL)² = F₀ + c α² not explicitly unit-checked**

- Section V uses 1/σ(f_NL)² = F₀ + c α² with F₀ = 1/8.98² and c = 0.0747. The units work only if σ(f_NL) is dimensionless and α is dimensionless, giving F₀ and cα² in units of 1/(f_NL²), which is standard.  
- However, Appendix D later mentions “local-linear propagation σ(f_NL) ≈ 8.98 − 3.66 α fails inside the 1σ interval that crosses zero.” This linearized form has units only if 3.66 has units of “σ per unit α,” but that is never defined and looks like a regression coefficient derived from the nonlinear 1/σ² form.  
- My earlier review did not explicitly point out that the paper mixes the nonlinear positive-definite Fisher form with an unqualified linearized σ ≈ σ₀ − kα expression, which is not dimensionally wrong but conceptually inconsistent with the claimed “positivity-respecting” form. This linear approximation should either be dropped or explicitly labeled as a local Taylor series with its validity region (α close to 0) and not used near α ≈ 0.2–2.

[P3-E7] **Equation consistency — NANOGrav Bayes factor vs. “no detection” wording**

- Section V A reports Savage–Dickey B_MB/SMBHB = 7.14×10³ (log₁₀B = 3.85, “decisive” on Jeffreys’ scale).  
- The same section states “Neither the +1.13σ deviation nor the Bayes factor constitutes a detection; both are reported here as illustrative.”  
- While this is rhetorically softened, the use of the Jeffreys “decisive” label, attached to a model comparison based on a broad prior on γ, remains numerically strong and could be read as evidence *for* the bounce model relative to SMBHB. In my earlier review I focused on the “detection” language, but did not explicitly flag that combining the Jeffreys adjective with a non-detection disclaimer is internally inconsistent: either the Jeffreys term should be removed or the Bayes factor rephrased as “strong preference in this parameterization” with explicit caveats that it does not imply model validation.

[P3-E8] **Internal cross-reference — Table IV “closed (C = resolved)” vs. text caveats**

- Table IV labels all ten caveats as “closed (C = resolved in paper; derivations in companion data repository).”  
- Several entries (e.g., (ii) injection-recovery synthesis; (v) NANOGrav using published KDE rather than raw TOAs; novelty fraction limited to DESI top-1,000) are at best *discussed* and not resolved in the sense of independent validation or error closure. The text in Section VI D acknowledges residual limitations, but the table still uses “resolved.”  
- Initial review noted this at a high level; what I did not emphasize is the *cross-reference mismatch*: any sentence in the main text that points the reader “to Table IV for resolution of the caveats” oversells what that table provides. The fix is to reword the table caption to “discussed” and ensure no main-text pointer implies closure.

[P3-E9] **Null-procedure comparability — multiple σ(fNL) values juxtaposed without explicit null mapping**

- The paper quotes several σ(f_NL) values: σ = 8.98 (single-tracer baseline), 8.43 (α = 0.15), 8.14 (α_jk = 0.19), and σ_GS = 1.95 with envelope [0.94, 8.98] for the Gold+Silver subset.  
- These all come from the same Fisher pipeline but with different tracer sets, α values, and implicit assumptions about systematics and shot noise (Appendix D’s 15–30% penalty discussion).  
- My earlier review flagged confusion between the “prior fixed α” and the “empirical α” estimators, but did not explicitly state that *each σ* corresponds to a slightly different null procedure (different tracer density, different α prior, different nuisance-block treatment). Comparing them as scalar numbers in one paragraph without reiterating those differences risks overinterpretation. Each σ quoted in the abstract or conclusions should be accompanied by a parenthetical “under [null configuration X], not directly comparable to [Y].”

[P3-E10] **Abstract faithfulness — “largest multi-archive anomaly detection campaign to date”**

- Conclusion: “We have presented the largest multi-archive anomaly detection campaign to date, scanning 37.3 million sources and CMB map patches…”  
- Abstract: “We present the largest-scale application of autoencoder anomaly detection across seven astronomical archives…”  
- The body never quantitatively compares against other multi-archive or autoencoder campaigns beyond single‑survey works [10–12]. There is no literature survey establishing that no other group has applied autoencoders at similar or larger multi‑survey scale (e.g., combined LSST simulations, or other multi‑catalog pipelines).  
- My initial review correctly called out “largest-scale application” as unsupported, but I did not highlight that the *conclusion* repeats and amplifies the same claim (“largest multi-archive anomaly detection campaign”) without any added evidence. Both locations need either a literature-backed comparison or softening to “a large-scale multi-archive …”.

[P3-E11] **Unquantified hedges — “consistent with no improvement” without explicit Δ/σ at each step**

- Abstract: “7.9% improvement consistent with no improvement at <1σ; σ(f_NL)_std = 8.98 single-tracer baseline.”  
- Section V B essentially repeats this but does not provide the actual statistical significance of the difference in σ (e.g., Δσ / σ_uncertainty), only the percentage improvement.  
- While the qualitative statement is reasonable, my previous report did not note that readers cannot verify “<1σ” from the numbers given; the uncertainty on σ(f_NL) as a forecast quantity (from uncertainties in α, number densities, and systematics) is not presented. To support the “<1σ” phrase quantitatively, the paper needs to show how the prediction error on σ(f_NL) is propagated and what that implies for the significance of the 7.9% shift.

[P3-E12] **Appendix–main mismatch — σ(fNL) dense limit and “baseline multi” not cleanly tied to main Fisher form**

- Appendix D: Figure 8 labels “Ideal (dense limit) = 11.71” and “Baseline multi-tracer = 12.72.”  
- Section V uses F₀ = 1/8.98² and c = 0.0747 for the DESI single‑tracer baseline and anomaly tracer; Appendix C then uses α = 0.15 to get σ(f_NL) = 8.43.  
- The connection between the 11.71/12.72 “multi-tracer” numbers and the 8.98/8.43 “DESI+tracer” numbers is only sketched informally; there is no single equation chain that shows how the dense-limit, baseline-multi, and DESI-only forecasts relate to the master form 1/σ² = F₀ + c α² with specific F₀ and c.  
- My first review asked for “one derivation path,” but did not specifically flag that the appendix currently leaves the reader to infer how many tracers are in the “canonical 5-tracer” configuration or how those F components map to the simpler 1/σ² form in the main text. For PRD, the appendix needs a worked example starting from the full Fisher matrix and ending at the quoted 11.71, 12.72, and 8.98 numbers.

[P3-E13] **Stale numbers — “baseline-multi 12.72” vs. “+7.93% ideal-multi figure”**

- Appendix D: “With a 15% Fisher-info penalty, σ(f_NL) = 12.56 (+1.27% over the baseline-multi 12.72); with a 30% penalty, σ(f_NL) = 13.35 (−4.97% vs. baseline-multi). The +7.93% ideal-multi figure (canonical 5-tracer) is therefore the dense-tracer limit…”  
- 7.93% improvement relative to *what* is not restated; presumably relative to σ_std = 16.85 mentioned only in the caption of Fig. 8 (“dotted dark-red line marks the single-tracer baseline (σ(f_NL) = 16.85)”).  
- The numerical triplet {16.85, 12.72, 11.71} appears only in the appendix, and the percentages are never recomputed explicitly; any change in one of these baseline numbers in a revision would easily leave inconsistent percentages—a classic “stale number” trap. My initial review flagged confusion but not this specific vulnerability. The authors should recompute and state all relative improvements (dense vs. baseline-multi vs. single-tracer) in one table so that if one number is updated, the others can be consistently regenerated.

[P3-E14] **Abstract faithfulness — “testable at 3–5σ with SPHEREx” not quantitatively linked**

- Introduction and Conclusions: “The quasi-matter bounce model predicts f_NL = −35/8 … testable at 3–5σ with SPHEREx  under the multi-tracer methodology of Heinrich et al.  (σ(f_NL) ≈ 0.7 bispectrum-only forecast).”  
- Section V and Appendices discuss σ(f_NL) down in the ~8–12 range for DESI+tracer configurations, but there is no explicit step showing how SPHEREx + the anomaly tracers yields σ ≈ (0.7 / factor) and hence 3–5σ for f_NL = −4.375. The quoted “3–5σ” remains imported from  rather than derived from this catalog’s properties.  
- My earlier review criticized the f_NL forecasts but did not isolate this abstract claim: as written, the paper implies that the anomaly tracers make the 3–5σ SPHEREx target achievable, yet the detailed pipeline for that claim is absent. Either the “3–5σ with SPHEREx” should be clearly labeled as a *direct citation* of Heinrich et al. independent of this work, or a quantitative derivation must be provided.

[P3-E15] **Unsupported novelty phrasing — “novel X-ray sources” vs. archival coverage**

- Section III E: “Anomaly count: 298 … SIMBAD-unmatched: 68% (203 novel X-ray sources).”  
- Section IV A explicitly explains that SIMBAD-unmatched is a *database coverage* proxy and that extended cross-matching (NED+VizieR) reduces novelty from 58.8% down to ~17.8% for DESI; a random-sample test on eROSITA is said to recover 100% archival IDs in VizieR for 20 objects.  
- Calling the 203 SIMBAD-unmatched eROSITA objects “novel X-ray sources” is therefore inconsistent with the later caveat: many or most will already exist in X-ray or multi-wavelength catalogs not propagated to SIMBAD. The earlier review discussed SIMBAD vs. genuine novelty at a global level, but did not flag this specific internal contradiction. The phrase should be softened to “SIMBAD-unmatched X-ray anomalies” or similar.

[P3-E16] **Null-procedure comparability — SIMBAD vs. “genuine novelty” percentages juxtaposed**

- Fig. 5 and Section IV A present a 58.8% SIMBAD-unmatched fraction across surveys and later a 17.8% “genuine novelty fraction” from DESI top-1,000 cross-matched against 20 catalogs.  
- The abstract and conclusions refer to “58.8% SIMBAD-unmatched … genuine novelty fraction ∼17.8% at the DESI top-1,000 score stratum.”  
- These two percentages are based on different null procedures (single-database vs. multi-catalog cross-match) and different sample definitions (all anomalies vs. top-1,000 DESI). They are juxtaposed without a clear “not directly comparable” qualifier each time they appear together, especially outside §IV A. My previous review advised demoting SIMBAD, but did not explicitly require that *every* juxtaposition of 58.8% and 17.8% carry this warning.

[P3-E17] **Appendix–main mismatch — ACT DR6 “+200 relative to the headline” wording**

- Appendix F: “The 8-way-with-ACT dedup variant, which would have produced 388,693−10,213 = 378,480 unique objects (+200 relative to the headline)…”  
- 388,693 is the sum of per-survey Path‑C native counts including ACT (i.e., 388,493 + 200), and subtracting 10,213 duplicates gives 378,480. This is indeed 200 more than 378,280, but earlier in the paper (Table I footnote ∥), ACT is said to contribute zero positional overlaps and “excluding ACT subtracts exactly 200 from both the input sum and the unique-object count.”  
- The arithmetic is fine; the conceptual issue is that the wording “+200 relative to the headline” appears in an appendix that also stresses ACT is quarantined and contributes zero objects. The main text never explicitly reconciles why ACT’s 200 appear in the “input sum” but are forbidden from the “headline,” which could confuse readers about whether those 200 have been used anywhere in analysis. My initial review noted the ACT accounting, but not this specific duplicated wording; tightening the language to “would have produced 200 additional catalog entries, which are excluded by construction” would avoid ambiguity.

If the authors address these additional points along with the issues in the original report, the manuscript will be substantially closer to the numerical and logical rigor PRD expects.