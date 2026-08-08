# RREXT P3 ChatGPT
VERDICT: MAJOR REVISIONS

Provider: ChatGPT (default)
PDF: RREXT_P3.pdf (md5: e83a4a6668e5c9ff324205267f8c46b8)
Chat: https://chatgpt.com/c/6a44401e-5170-83e8-a758-73fe833f7bfa
Harvested: 2026-06-30
RCEXT baseline: MAJOR REVISIONS (no change)

Thought for 9s1. Recommendation: MAJOR REVISIONS
This is an ambitious and unusually transparent multi-survey anomaly-catalog paper. The paper has a potentially valuable core result: a large-scale, per-survey native-retrained anomaly search across DESI, SDSS, Planck, NEOWISE, and exploratory Gaia/eROSITA/LAMOST components, with substantial caveat accounting and validation diagnostics. However, at the current standard required for MNRAS/PRD/JCAP, the manuscript is not yet publishable as a top-journal catalog/data-product paper because its headline catalog framing still over-mixes validated, exploratory, methodological-failure, fixed-threshold, fixed-percentile, and membership-only components. Several “headline” numbers are therefore not yet cleanly tied to a reproducible, uniformly validated scientific object class. The cosmology applications are secondary and mostly framed conservatively, but they add cognitive load and still risk distracting from the main catalog-quality issues. RREXT_P3
I would support publication after major revision if the paper is reframed around the genuinely validated/recommended subset, with failed or irreproducible components moved out of the headline catalog claims and with a fully public, reproducible data/code release available at review/submission.
2. BLOCKERS
B1. Headline catalog size is not publication-clean because it mixes validation statuses
Severity: Blocker
The paper repeatedly distinguishes: full Path-C unique catalog = 378,280; recommended tier = 269,317; validated catalog-grade subset ≥268,519 unique; exploratory Gaia/eROSITA = 798; LAMOST methodological-failure tier ≈113,000. This transparency is good, but the abstract, conclusions, and title still lead with a very large “378,280 total” result while explicitly admitting that LAMOST is a 98% blue-excess training-bias artifact and fails injection recovery, and that Gaia/eROSITA fail injection recovery. For a catalog paper, the primary catalog should be the validated catalog-grade set, not the union of validated + exploratory + methodological-failure tiers.
Required fix: Title, abstract, Table I, conclusions, and all “largest catalog” language should make the validated catalog-grade count the primary result. The 378,280 total should be described only as a full audit/product including exploratory and failure-mode components, not as a science catalog.
B2. eROSITA tier is not a reproducible score-based catalog
Severity: Blocker
The paper states that the eROSITA production score axis is irreproducible under 16 monotone rescalings and that the production Table IV scores are non-monotone relative to the committed raw artifact. The paper then releases eROSITA as an n=298 membership list only. That may be acceptable as an exploratory appendix, but it is not acceptable as part of a recommended or catalog-grade headline tier. The manuscript already mostly acknowledges this, but Table I and the “recommended tier” structure still include eROSITA in a way that can be misread as a usable anomaly-score catalog.
Required fix: Remove eROSITA from the recommended headline tier unless the exact production scoring pipeline is recovered and reproduced. Otherwise, clearly label it as an exploratory membership-only appendix, not a recommended catalog component.
B3. DESI headline anomaly count is dominated by non-primary science targets
Severity: Blocker
The paper’s most important survey, DESI, has 195,829 full-stream anomalies, but the science-class-restricted recount finds only 2,468 anomaly clusters on validated science-target spectra, about 0.9× the prior Liang et al. benchmark. The manuscript discloses that ∼98.7% of DESI anomaly clusters fall on sky-fiber/filler/non-primary spectra. This fundamentally changes the interpretation of the DESI contribution and undermines any headline comparison that emphasizes “73×” or “141×” without equal prominence to the science-target recount.
Required fix: Make the DESI science-class result the primary DESI catalog claim. Full-stream DESI counts can remain as an engineering/process-scale result, but not as the main astrophysical catalog-size claim.
B4. Reproducibility is promised but not demonstrated in the paper package
Severity: Blocker
The data availability section says catalogs, model weights, scripts, hashes, and DOI will be released with arXiv/submission. That is fine procedurally, but for a catalog paper whose claims depend on many handoff artifacts, recovered pod scripts, unrecovered scripts, and exact dedup manifests, the data/code release is not optional.
Required fix: At acceptance, the referee/editor must have access to the frozen catalog tables, dedup manifests, score-axis schemas, training scripts, recovery-test artifacts, and hashes. “Will be released” is insufficient for final acceptance.
3. MAJORS
M1. Validation gates are heterogeneous and partly ad hoc
Severity: Major
The paper uses different validation logic across surveys: DESI uses k-fold/OOD Jaccard and visual inspection; SDSS/Planck pass detector-sensitivity injection recovery; NEOWISE passes a geometry QA by construction; Gaia/eROSITA fail injection recovery; LAMOST fails and is retained as a lesson. The manuscript discloses this, but the combined catalog framing still risks presenting unlike quantities as one coherent anomaly catalog.
Suggested fix: Add a single “catalog usability matrix” with columns: science-ready? score reproducible? detector-sensitivity validated? threshold type? recommended downstream use? This should be in the main text, not only footnotes.
M2. Threshold policy is too complicated for the main catalog
Severity: Major
The paper uses S>5 for DESI, fixed-size continuity slice for SDSS, top-1% for LAMOST/Gaia/NEOWISE/Planck, top-298 membership for eROSITA, and raw MSE for Planck. This is transparent, but it makes the combined count scientifically ambiguous.
Suggested fix: Provide one uniform secondary catalog cut, even if less complete, based on a common validation criterion. Keep survey-specific native rankings as auxiliary products.
M3. LAMOST should not contribute to any main total that sounds like a catalog
Severity: Major
The LAMOST section is actually one of the paper’s strongest methodological contributions: it demonstrates that a non-representative training set can produce a dominant artifact population. But including ∼113,000 LAMOST detections in the “full Path-C unique catalog” weakens the paper.
Suggested fix: Move LAMOST to a “failure-mode audit” appendix or separate table. Do not include it in the main catalog total except as a clearly marked non-science artifact component.
M4. DESI lacks injection-recovery validation
Severity: Major
DESI is the anchor survey and largest validated component, but the paper explicitly states DESI injection-recovery was not executed. The k-fold Jaccard, OOD Jaccard, and visual inspection checks are useful, but they do not measure detector sensitivity to controlled anomaly morphologies.
Suggested fix: Run DESI injection-recovery o
