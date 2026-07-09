VERDICT: major-revisions

CENTRAL CLAIM: The paper presents a large multi-survey autoencoder anomaly catalog spanning 37.3 million spectra/map patches, argues that a validated subset of 268,519 anomalies is reproducible and scientifically usable, and demonstrates secondary cosmological applications; the catalog construction is substantially documented, but several core validation and methodological issues prevent the strongest claims from being fully supported. 

r9_P3

ISSUES:

[MAJOR] Validation remains heterogeneous across surveys. The headline "validated catalog-grade" combines detector-sensitivity validation (DESI, SDSS, Planck), a geometry-only QA (NEOWISE), while excluding eROSITA and relegating LAMOST to exploratory status. These are fundamentally different validation standards. A single catalog-grade label overstates the uniformity of evidence. The manuscript should either separate validated detector-sensitive catalogs from QA-only products or justify why these validation modes are equivalent. 

r9_P3

[MAJOR] DESI headline statistics still rely on in-sample scoring. Although the manuscript now includes k-fold stability, OOD Jaccard tests, and injection-recovery, the published anomaly catalog is still generated on

--- [continuation] ---

VERDICT: major-revisions

CENTRAL CLAIM: The manuscript presents a reproducible multi-survey autoencoder anomaly catalog built from 37.3 million spectra and map patches, yielding a validated subset of 268,519 anomalies and demonstrating potential downstream cosmological applications; the catalog itself is substantially supported, but several methodological choices and some downstream scientific claims require stronger validation before publication. 

r9_P3

ISSUES:

[MAJOR] Validation standards are not uniform across the catalog. The "validated catalog-grade" subset combines surveys validated by detector-sensitivity injection tests (DESI, SDSS, Planck) with NEOWISE, whose validation is explicitly a masking-geometry QA rather than detector-sensitivity. The manuscript acknowledges this distinction, but the catalog presentation still risks implying equivalent validation across all retained components. The validation hierarchy should be reflected more explicitly in the headline catalog description and conclusions. (§III, §VI D, Fig. 10) 

r9_P3

 

r9_P3

[MAJOR] DESI headline results remain based on in-sample scoring. The paper appropriately documents k-fold stability, OOD Jaccard overlap, and injection-recovery, which substantially strengthen confidence. However, the published 22.5 million-spectrum anomaly catalog is still produced by scoring a dataset containing the training examples. The authors are transparent about this, but PRD would ideally expect the released headline catalog itself to originate from a fully held-out or ensemble-trained workflow rather than relying on indirect validation. (§II B, §VI D(i)) 

r9_P3

 

r9_P3

[MAJOR] Cosmological applications remain substantially weaker than the catalog itself. The manuscript appropriately states that neither the multi-tracer forecast nor the NANOGrav analysis constitutes a detection, but these sections remain much more speculative than the anomaly catalog. Because they rely on relatively small tracer samples, idealized Fisher forecasts, and simplified likelihood assumptions, they should be presented more clearly as demonstrations rather than scientific results of comparable weight to the catalog. (§V, Conclusions) 

r9_P3

 

r9_P3

[MAJOR] Multiple threshold definitions complicate interpretation. DESI uses a fixed S>5 threshold, SDSS uses a continuity slice, LAMOST uses a top-1% cut, Planck and NEOWISE use fixed-percentile selections, while eROSITA ultimately becomes a membership list. Although every choice is documented carefully, the resulting catalog is not based on a unified anomaly definition. This limits interpretation of cross-survey anomaly rates and should be emphasized earlier and more prominently. (Table I; §II B) 

r9_P3

 

r9_P3

[MAJOR] Survey-specific validation metrics prevent straightforward comparison of anomaly quality across archives. The manuscript repeatedly cautions that scores are normalized independently and validation differs between surveys, yet many aggregate statistics (overall catalog size, overall novelty, total anomaly counts) naturally invite direct comparison. Additional summary metrics describing relative confidence by survey would improve interpretability. (§II B; Table I) 

r9_P3

[MINOR] The manuscript remains considerably longer than necessary. Many methodological clarifications, provenance discussions, reproducibility audits, threshold justifications, and historical explanations interrupt the scientific narrative. A substantial fraction of these could move to appendices or supplementary material without reducing reproducibility.

[MINOR] The historical evolution of failed components is described in excessive detail. Extended discussion of removed Gaia products, quarantined ACT analyses, unrecoverable eROSITA score axes, and historical cross-transfer baselines demonstrates commendable transparency, but repeatedly revisiting these topics distracts from the final validated product.

[MINOR] The terminology surrounding "validated", "exploratory", "membership-only", "catalog-grade", and "inclusive" occasionally becomes difficult to follow. A single summary diagram showing which surveys contribute to which catalog products would improve clarity.

[MINOR] Some figures primarily document engineering rather than science. Numerous figures illustrate validation pipelines, threshold behavior, and reconstruction diagnostics that are valuable for reproducibility but could be condensed in the main text.

[MINOR] Several conclusions depend on heuristic engineering thresholds. The authors explicitly acknowledge that gates such as Jaccard ≥0.70 or injection recovery ≥50% were engineering choices rather than statistically optimized thresholds. This disclosure is appropriate and sufficient, but readers should be reminded that these thresholds were not externally calibrated.

[MINOR] The extensive reproducibility discussion is a major strength, but occasionally overwhelms the scientific presentation. Nearly every caveat is accompanied by provenance scripts, JSON artifacts, and reproducibility checks. This greatly strengthens confidence but also makes the manuscript read partly like software documentation rather than a physics paper.

[MINOR] The DESI science-target recount substantially improves the comparison with prior literature. The authors appropriately correct earlier process-volume comparisons and clearly distinguish full-stream from science-target analyses. This issue appears adequately addressed and should not be considered a remaining weakness. (§III A)

[MINOR] The treatment of failed analyses is unusually transparent. Rather than removing problematic tiers, the manuscript documents why Gaia, ACT, LAMOST, and eROSITA fail various validation criteria. This level of disclosure is exemplary and strengthens confidence in the remaining validated catalog.

[MINOR] The manuscript appropriately avoids overstating cosmological implications. The authors repeatedly state that neither the SPHEREx forecast nor the NANOGrav consistency test constitutes evidence for new physics. Those caveats appear adequate and should not be viewed as flaws in themselves.

Final verdict: major-revisions. The catalog construction, validation effort, and reproducibility standards are unusually thorough and represent a significant technical contribution. However, the heterogeneous validation criteria across surveys, reliance on in-sample DESI scoring for the released headline catalog, non-unified anomaly definitions, and comparatively weak cosmological applications prevent acceptance in PRD without further revision.

--- MANIFEST: P3 (v3.1.145) | ChatGPT GPT-5 | native PDF | chat 6a4f50ee-5a78-83e8-aada-784d7669552f | verdict major-revisions | continued once | 2026-07-09
