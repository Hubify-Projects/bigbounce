# INT API Review — P3APJS v3.1.157-apjs — gemini (gemini-3.1-pro-preview)
paper: P3APJS  version: v3.1.157-apjs  model: gemini-3.1-pro-preview
modality: native-PDF (inline_data base64)
UTC: 2026-07-12T17:52:49.154611Z  |  latency: 34.5s  |  attempt: 1
usage: {"promptTokenCount": 21494, "candidatesTokenCount": 691, "totalTokenCount": 23879, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 174}, {"modality": "IMAGE", "tokenCount": 21320}], "thoughtsTokenCount": 1694, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**
1. **[MAJOR] Scope and Focus (Section 5):** The inclusion of primordial non-Gaussianity ($f_{\rm NL}$) forecasts and NANOGrav MCMC bounce cosmology (Sections 5 and 5.1) is highly disjoint from the core focus of a multi-wavelength anomaly detection catalog. While explicitly caveated as "secondary methodological demonstrations," these sections read like an entirely separate theory paper grafted onto a data release. I strongly recommend either removing Section 5 (reserving it for a follow-up letter) or drastically condensing it into a brief "Future Applications" discussion. If retained, the physical link between the *specific* morphological properties of the anomaly-selected QSOs and the multi-tracer $f_{\rm NL}$ constraints must be justified more clearly.
2. **[MAJOR] Validation Heterogeneity (Abstract & Section 3):** The headline "validated catalog-grade subset" (268,519 sources) bundles surveys that passed rigorous detector-sensitivity injection-recovery tests (DESI, SDSS, Planck) with NEOWISE, which only passed a mask-geometry QA test. While the author is highly transparent about this in the text, grouping them under a single "validated" headline number in the abstract and conclusion risks misleading downstream users. The NEOWISE component should either be moved to an exploratory tier, or the abstract/conclusion must explicitly separate the "sensitivity-validated" count from the "geometry-validated" count. 
3. **[MINOR] Formatting of Reproducibility Artifacts:** The author's commitment to absolute reproducibility—including exact git hashes, datasets, and scripts—is highly commendable and exactly what ApJS encourages. However, the inclusion of dozens of inline, raw file paths (e.g., `pipelines/p3_anomaly_engine/outputs/reproduce_headline_dedup.json`) severely disrupts the readability of the manuscript. Please move these file paths to footnotes, or better yet, consolidate them into a structured "Reproducibility Mapping" table in the Appendix.
4. **[MINOR] Stylistic Tone:** The manuscript frequently employs a hyper-defensive, conversational, or instructional tone (e.g., "(READ THIS BEFORE TABLE 2)", "Honest limitation:", "What this appendix is not."). AAS journals rely on clear structural organization rather than inline admonitions to guide the reader. Please revise the text to adopt a more standard, objective scientific tone, allowing the robust methodology to speak for itself.
5. **[MINOR] Table Redundancy (Tables 1, 2, and 6):** The manuscript contains overlapping tables and dense inline text attempting to reconcile process-volume counts, native counts, and cross-transfer counts. Tables 1 and 2 are highly redundant. Consider merging them into a single, clean master table that clearly stratifies the final data release into "Catalog Grade", "Exploratory" (LAMOST), and "Excised/Separate" (eROSITA, Gaia, ACT) tiers to reduce reader confusion. 

**Summary:**
The central claim—the generation, validation, and release of a massive, multi-survey anomaly catalog with unprecedented provenance and reproducibility—is robustly supported, highly valuable to the community, and an excellent fit for ApJS.