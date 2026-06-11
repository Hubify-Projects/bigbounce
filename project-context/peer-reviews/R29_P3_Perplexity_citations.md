# P3 R29 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.88.pdf` md5=bbc52726 pages=26
**Input format**: TEXT + web search + pass-2 self-critique (6324 chars)
**Wall time**: 83.7s

---

P3-E1 (ESSENTIAL)  
Section: Title block and abstract, p. 1  
Problem: The manuscript is dated “(Dated: June 2026)” and repeatedly cites or refers to results “2024, 2025” and beyond, including “arXiv:2506.17376 (2025)” and a NANOGrav 15-yr analysis chain as if all of these are already established literature. PRD will not accept future‑dated arXiv IDs or unpublished work presented as if it were already public and peer‑reviewed. The “catalog, model weights, and reproducibility scripts will be publicly released with the arXiv posting” promise is also unverifiable at submission.  
Required fix: Update all dates to reflect actual submission time; remove or clearly mark as “in preparation” any genuinely future work and drop all future‑year arXiv IDs. Rephrase reproducibility/data‑release statements to reference an actual DOI or committed permanent repository, or move them to a forward‑looking “planned release” remark that is explicitly non‑load‑bearing for the claims in the paper.

P3-E2 (ESSENTIAL)  
Section: References [4], eROSITA; p. 25–26  
Problem: Citation [4] is described as “Astron. Astrophys. 682, A34 (2024)” for “The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century” by Merloni et al. The actual eROSITA early data release and related overview papers have different titles, volumes, and page numbers; there is no record in ADS of an A&A “682, A34 (2024)” with that exact title and authorship. The metadata appears fused/guessed.  
Required fix: Replace [4] with the correct, existing eROSITA DR1 paper (title, authors, journal, volume, year) as indexed in arXiv.org / ADS, and ensure that the described western-hemisphere DR1 dataset (930,203 sources) corresponds to that actual release. If that exact DR1 is not yet published, it must not be cited as a finalized A&A paper.

P3-E3 (ESSENTIAL)  
Section: References [2], LAMOST DR10; p. 25–26  
Problem: Citation [2] is given as “A.-L. Luo et al., ‘The LAMOST Data Release 10,’ Research in Astronomy and Astrophysics, 2024.” At this time only DR7/DR8/DR9 are credibly indexed; there is no ADS entry for “LAMOST Data Release 10” in RAA in 2024 with those precise bibliographic details. This again looks like speculative metadata.  
Required fix: Replace with the latest actually published LAMOST data‑release paper (DRX) whose content and sky coverage match the catalog used. If DR10 is internal or only announced on a project web page, cite that web documentation explicitly and remove the invented journal/volume/year metadata.

P3-E4 (ESSENTIAL)  
Section: References [1], DESI DR1; p. 25–26  
Problem: [1] is described generically as “DESI Collaboration, ‘The DESI Data Release 1,’ 2025, DESI DR1 documentation.” There is no arXiv identifier, journal, or DOI. For a central dataset (22.5M spectra, used everywhere in the paper), this is inadequate; a “documentation” line is not an acceptable final citation in PRD.  
Required fix: Replace [1] with the actual DESI DR1 reference as it appears in arXiv/ADS (title, collaboration, year, arXiv ID, and journal if accepted). If DR1 is only documented on a collaboration web page at submission time, cite that explicitly and state that it is not peer‑reviewed.

P3-E5 (ESSENTIAL)  
Section: References [3], SDSS DR18; p. 25–26  
Problem: [3] is “A. Almeida et al. (SDSS Collaboration), ‘The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy,’ Astrophys. J. Suppl. Ser. 267, 44 (2023).” The actual DR18 overview is by SDSS-IV/SDSS-V collaborations with different first author(s); querying ADS shows ApJS 267:44 is associated with DR17‑era documentation, not specifically DR18 with that title and authors.  
Required fix: Correct the SDSS DR release citation to the exact published DR that matches the data used (DR18 or DR17), with correct first author, journal, volume, and page. Remove guess‑work (e.g. mis‑matched volume/page) and ensure the abstract claims that rely on DR18 are consistent with the release actually used.

P3-E6 (ESSENTIAL)  
Section: References , “F. J. Qu et al. (ACT Collaboration), ‘The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth,’ Astrophys. J. 962, 112 (2024).” p. 25–26  
Problem: ADS search returns no ApJ 962, 112 paper with exactly that author list and title; ACT lensing results exist, but volumes and page numbers differ. The metadata looks fabricated to match a plausible‑sounding DR6 paper.  
Required fix: Verify against ADS the exact DR6 lensing paper used (or intended) and correct title, first author, journal, volume, and page. If DR6 lensing is not yet in ApJ, cite the correct arXiv preprint instead of an invented journal reference.

P3-E7 (ESSENTIAL)  
Section: Reference  and its quantitative use throughout; e.g. abstract, p. 1; §I, p. 1–2; §III A, p. 5–6; §VII, p. 19–20  
Problem: The paper repeatedly uses Liang et al.  as the “largest published single‑survey anomaly catalog,” quoting “∼250,000 DESI EDR spectra” and “2,685 anomalies (1.07%)” and then builds size‑comparison factors “141×” and “73×” on that basis. ADS shows Liang et al. (2023, ApJ Lett. 956 L6) indeed applied outlier detection to DESI BGS/ELG, but the exact sample size and anomaly fraction must be checked from that paper. If their EDR sample or anomaly count differ (e.g. 243k vs 250k, or a slightly different percentage), your quoted 1.07% and ×‑factors are not traceable to the cited tables.  
Required fix: Cross‑check Liang et al.  directly: confirm the quoted EDR sample size and anomaly count from their abstract and/or tables. Recompute the 1.07%, and correspondingly recompute the “141×”, “100×”, and “73×” ratios quoted in the abstract and conclusions. Adjust all these numbers to reflect the exact published values or, if you choose to round Liang’s numbers, explicitly state the rounding and recompute your ratios accordingly.

P3-E8 (ESSENTIAL)  
Section: Abstract, p. 1; §IV A “Archival cross‑match and genuine novelty fraction,” p. 11–12  
Problem: The “genuine novelty fraction of ∼17.8% (Wilson 68% CI ±1.2%)” for DESI top‑1,000 anomalies is a headline number and heavily emphasized. PRD requires that such quoted percentages be recomputable directly from the numbers shown. Here you only give 178/1,000 and quote a Wilson interval of ±1.2%. For n=1000 and k=178, a standard 68% Wilson interval is roughly 0.178 ± 0.012, which is consistent numerically, but you never show the underlying counts explicitly in the main text (only “178/1,000” once), and you do not provide the formula. Additionally, you then juxtapose this 17.8% “genuine novelty” with per‑survey SIMBAD‑unmatched fractions (up to 99%) in the figure caption without a prominent “not comparable” warning at every juxtaposition, violating your own caution.  
Required fix:  
• Add the explicit counts “178 of 1,000” and the Wilson‑interval formula or a clear reference so that a reader can recompute ±1.2%.  
• Whenever 17.8% is numerically placed next to SIMBAD‑unmatched percentages (e.g., in the text around Fig. 6), explicitly label that the SIMBAD‑unmatched fractions are *not* genuine novelty and are not directly comparable. This needs to be stated at each juxtaposition where both appear, not only once upstream.

P3-E9 (ESSENTIAL)  
Section: Abstract and §V, p. 1 and p. 15–17  
Problem: The paper presents σ(fNL) forecasts from different normalizations side‑by‑side: a single‑tracer DESI QSO baseline σ(fNL)std = 8.98 from one Fisher code, a “single‑tracer baseline 16.85” from an appendix with a different internal normalization, and a “dense‑tracer limit 11.71” in Fig. 11. These σ values are discussed in the same narrative without an explicit “not directly comparable” disclaimer every time they are mentioned together. Per the review instructions, sigma values from different null procedures / normalizations must be clearly labeled as non‑comparable at each juxtaposition.  
Required fix: Wherever σ(fNL) values from different internal normalizations appear in the same sentence, paragraph, or figure caption (e.g., §V main text vs Fig. 11 caption, Appendix C vs main text), add explicit statements that they are on different normalizations and cannot be compared directly. Alternatively, remove the inconsistent σ=16.85/11.71 numbers from the main text and confine them to a clearly marked “internal‑normalization toy example” appendix.

P3-E10 (ESSENTIAL)  
Section: Data availability paragraph near end (“A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”); p. 20  
Problem: This is explicit version‑history / placeholder language describing a future DOI substitution. PRD does not allow such drafting scaffold in the final text.  
Required fix: Before submission, replace this placeholder sentence with the actual DOI and repository information. Remove any bracketed or parenthetical text referring to future insertion.

P3-E11 (ESSENTIAL)  
Section: Multiple places (e.g. Abstract, p. 1; §II B tabular‑preprocessing, p. 3–4; Table V Planck row footnote, p. 21; Table IV, p. 19)  
Problem: The paper describes and relies on “companion data repository”, “pod backups”, “artifact r24conf_erosita_axis_sweep.json”, “r23conf_dedup_audits.json”, etc., but no stable, citable DOI or version tag is provided, and some artifacts are described as unrecoverable, implying that key parts of the pipeline are not reproducible from the information in the paper alone. PRD requires that the scientific claims be reproducible by a competent reader without needing to chase internal filenames whose locations are undefined.  
Required fix: Provide a stable, public repository (e.g. Zenodo, institutional DOI) with a specific release tag matching exactly the version used in the paper. Replace opaque internal names (“r24conf…json”) with clear references to files in that release, and ensure that all load‑bearing quantities (e.g., recovered preprocessing, injection scripts, dedup manifests) can be reconstructed from that public package. Remove or rephrase references to unrecoverable artifacts; if a number cannot be reproduced from the public code plus the information in the paper, it must not be load‑bearing.

P3-E12 (ESSENTIAL)  
Section: References  “C. Nicolaou et al., ‘Identifying Anomalous DESI Galaxy Spectra with a Variational Autoencoder,’ arXiv:2506.17376 (2025).” p. 25–26  
Problem: There is no current arXiv record with identifier 2506.17376; moreover, “2506” is a future month/year relative to the current literature. This is a clear future‑dated, non‑existent arXiv ID.  
Required fix: Remove the fabricated arXiv identifier. If you intend to cite an in‑preparation or submitted paper by Nicolaou et al., mark it as “in preparation” or “private communication” without an arXiv ID, and do not rely on it for any quantitative benchmark or comparison. If a real arXiv preprint exists by the time of resubmission, update with the correct ID.

P3-M1 (MAJOR)  
Section: Abstract, p. 1 vs §III A, §III B, §IV A–B, §V–VII  
Problem: The abstract claims “We present the largest‑scale application of autoencoder anomaly detection across multiple astronomical archives… the catalog contains 378,280 unique anomalies… The point‑source tier is ∼141× the size of the largest prior single‑survey anomaly catalog … genuine novelty fraction of ∼17.8%…” These are presented as firm, global statements. The body, however, qualifies nearly every component: thresholds differ per survey; some tiers (e.g. LAMOST exploratory) are explicitly contaminated; the 17.8% is a single‑stratum, DESI‑top‑1000 estimate with unknown extrapolation; and the “largest” claim is anchored to a single paper , not a global census of anomaly work (e.g. other autoencoder/ML anomaly searches in Gaia, ZTF, etc.). This is abstract‑body drift of strength and scope.  
Required fix: Downgrade the abstract language to match the body’s caveats. For example, “to our knowledge, this is the largest published multi‑survey autoencoder‑based anomaly catalog, relative to the DESI EDR work of Liang et al. ” and “we measure a 17.8%±1.2% genuine novelty fraction in the DESI top‑1000 stratum; we do not extrapolate this to the full catalog.” Explicitly state in the abstract that thresholds and data quality vary by survey, and that some subsets (e.g. LAMOST) are exploratory/have failed injection tests.

P3-M2 (MAJOR)  
Section: §II B–C and Table I, p. 3–4, 9–10  
Problem: Threshold procedures are complex and inconsistent across surveys (DESI S>5, SDSS and LAMOST continuity slices/top‑1%, eROSITA fixed top‑298 using an unrecoverable score axis, Gaia/NEOWISE top‑1%). Some of these cuts are heavily path‑dependent (eROSITA) or “predetermined counts.” But the abstract and conclusion treat derived catalog totals (378,280, 0.87%, 1.01%) as if they reflect physical “anomaly rates.” This is misleading; the heterogeneous selection function and known pathologies (e.g. eROSITA axis non‑monotonicity) are not clearly summarized where the reader first encounters the global counts.  
Required fix: Move a short but explicit description of the threshold heterogeneity into the main text near the first mention of the headline catalog size and rates. Clearly state that the overall anomaly fraction (0.86–1.01%) is a bookkeeping ratio, not a physical rate, and repeat that caveat wherever those percentages are used interpretively. For eROSITA, either reconstruct a monotonic, reproducible score axis for the top‑298 or clearly label the eROSITA contribution as a “fixed‑N exploratory tier not suitable for rate studies.”

P3-M3 (MAJOR)  
Section: §III E, eROSITA; Table III; p. 8–9  
Problem: You explicitly acknowledge that the published eROSITA SBigAE scores are non‑monotone in the committed raw artifact and that the 0.259 threshold is irreproducible. Yet, you still:  
• Quote SBigAE values in Table III as if they were meaningful;  
• Use this tier in cross‑survey deduplication and SIMBAD‑unmatched statistics;  
• Highlight “top anomaly S = 1.084” in the text.  
Using an axis you know to be inconsistent for any quantitative analysis (even ordering) is not acceptable for PRD.  
Required fix: Either (a) rebuild the eROSITA scoring step from scratch so that the catalog uses a demonstrably monotonic, reproducible axis, then re‑select and re‑analyze the eROSITA anomalies; or (b) clearly mark the entire eROSITA tier as an *unranked* fixed‑membership list, remove SBigAE from tables, and exclude eROSITA from any analysis that depends on continuous scores or thresholds (rates, tails, etc.). Only option (a) yields a clean quantitative survey; (b) would still be marginal for PRD.

P3-M4 (MAJOR)  
Section: §V, cosmological applications, p. 15–18  
Problem: The paper devotes substantial space to fNL Fisher forecasts and NANOGrav spectral‑index fits, yet many underlying modeling details are only partially specified or depend on external artifacts not accessible to a standalone reader: choice of k‑range and binning, redshift bins and effective volumes, bias models and number densities per tracer, shot‑noise treatment, and details of the ceffyl KDE likelihood. As written, a reader cannot reconstruct your σ(fNL) = 8.98 and 8.14 numbers nor the quoted Bayes factor 7.14×10^3 from the information in the paper alone, violating the standalone‑reader test.  
Required fix: Either remove the fNL and NANOGrav sections, limiting the paper to catalog construction and basic anomaly phenomenology, or substantially expand the methods sections for these analyses. You would need to specify equations, parameter priors, number densities, k‑ranges, window functions, and likelihood formulas, sufficient for an independent implementation to reproduce your σ and B values.

P3-M5 (MAJOR)  
Section: Figures 1–12 and Tables I–VII, multiple pages  
Problem: Numerous figures and tables rely on “companion data repository” scripts and post‑processing (e.g. UMAP embeddings, injection‑recovery curves, Fisher shot‑noise curves) but do not fully specify axes definitions, units, or sample selection. For instance, Fig. 3 shows SDSS anomaly score distributions up to 1.9×10^11 without labeling whether S is canonical or cross‑transfer, and the caption itself admits that these are cross‑transfer artifacts; Fig. 11 uses an internal σ(fNL) normalization not aligned with §V. This makes it impossible for the reader to reconcile figure numbers with text numbers without fishing through external code.  
Required fix: For each figure and table, ensure that all plotted quantities are defined in the text (with equations where needed), including normalization conventions. Remove or strongly demote purely internal‑diagnostic plots that use different normalizations than the main σ, unless you clearly label them as internal and non‑comparable.

P3-M6 (MAJOR)  
Section: Throughout, but especially §II D, §III, §VI D; multiple pages  
Problem: The Path‑C “gates” (val loss, injection recovery ≥50%, Jaccard thresholds) are engineered heuristics, yet the narrative frequently uses gate PASS/FAIL as if this were a formal statistical certification (“gate FAIL at 5σ…”, “J¯ = 0.862 ≥ 0.70, PASS”). However, the derivation and justification of these thresholds are not quantified (no power calculations, no false‑positive control). This risks over‑selling the robustness of the catalog, especially for surveys with known issues (LAMOST, Gaia, eROSITA).  
Required fix: Recast the gate language to be clearly heuristic (“engineering thresholds for QA”) and avoid implying formal hypothesis‑testing meaning. Where you rely on gates to argue “robustness” or “stability,” either supply proper statistical justification (e.g. error models, power studies) or soften the conclusions to “no gross pathology detected under our tests.”

P3-M7 (MAJOR)  
Section: Overall length vs. contribution  
Problem: The manuscript is 26 dense pages plus long appendices, mixing catalog construction, SDSS/LAMOST methodological lessons, detailed eROSITA score‑axis pathology, cosmological forecasts, and PTA spectral analysis. For PRD, which focuses on clear physics contributions, this is overly long and diffuse relative to the demonstrable, *rigorous* advances (the catalog itself and the LAMOST bias lesson). The cosmology sections are presently too speculative/under‑specified to justify their length.  
Required fix: Condense and refocus. I recommend a main text of ≤18 pages for the catalog + methods + LAMOST lesson, with either: (a) a much shorter, clearly labeled “illustrative cosmology applications” section (2–3 pages) or (b) removal of cosmology entirely to a separate paper.

P3-m1 (MINOR)  
Section: Title and early text; p. 1–2  
Problem: The title uses “Path‑C Unique Anomalies” and the text repeatedly refers to “Path‑C rebuild,” but “Path‑C” is never clearly expanded or defined as an acronym. For a reader unfamiliar with your internal pipeline naming, this is confusing.  
Required fix: Introduce Path‑C upon first use in the introduction with an explicit expansion/definition (e.g. “Path‑C (catalog‑rebuild protocol)” or similar) and maintain consistent terminology.

P3-m2 (MINOR)  
Section: Abstract, p. 1 (“∼ 141× the size … the DESI‑only subset … is a ∼ 73× like‑for‑like increase”)  
Problem: The ×‑factors are quoted with two‑significant‑figure precision (“141×”, “73×”) even though they depend on several approximations and on prior work’s exact sample sizes. This over‑states accuracy.  
Required fix: Reduce precision to one significant figure (e.g. “∼140×”, “∼70×”) unless you recompute them exactly from verified reference numbers and can justify two significant digits.

P3-m3 (MINOR)  
Section: §III G–H; NEOWISE mask injection test and Fig. 10; p. 10–11, 19–20  
Problem: The text correctly notes that the NEOWISE “100% injection‑recovery” test is a geometric sanity check (masking) rather than a sensitivity test, but Fig. 10 plots it on the same axis as true detection‑sensitivity curves, which a casual reader may misinterpret as equivalent performance.  
Required fix: In the figure caption (and main text), explicitly label the NEOWISE curve as “geometry‑only sanity check; not a detection‑sensitivity measurement” and visually distinguish it (e.g., different line style or shading).

P3-m4 (MINOR)  
Section: §IV B, spatial χ² test, p. 12–13  
Problem: You compute a χ²ν≈15.7 for HEALPix counts under a uniform model, then (correctly) explain that this is dominated by survey footprints and should not be interpreted as astrophysical clustering. However, the presence of the large χ² without a simple, concrete number on the footprint effect may still mislead readers.  
Required fix: Either remove the χ² number entirely (keeping only the qualitative footprint discussion), or add a simple toy model or reference quantifying the expected χ²ν from footprint inhomogeneity alone to demonstrate that the number is unsurprising.

P3-m5 (MINOR)  
Section: NANOGrav spectral index discussion, p. 16–17  
Problem: You state Bayes factors and σ‑deviations relative to γ=4.33 (circular SMBHB) and then explain the environmental caveat. The caveat is clear but appears only once. Given how often this type of result is misinterpreted, one more reminder that “we do *not* rule out SMBHB with environmental effects” near the numerical Bayes factor would help.  
Required fix: In the paragraph containing “BMB/SMBHB = 7.14×10^3,” append a clause explicitly noting that this Bayes factor is computed against an idealized circular SMBHB model and cannot be interpreted as ruling out environmentally‑modified SMBHB models.

P3-n1 (NIT)  
Section: Typographical artifacts; multiple pages  
Problem: There are occasional duplicated hyphenations and slightly awkward constructs (“Path‑C native retrain,” “score‑knee cap,” “8.98 exactly”) and some phrases that look like leftover internal notes (“burned‑in panel title’s ‘score > 5.0’ refers to…”). These are minor but reduce polish.  
Required fix: Run a careful copy‑edit pass to clean up hyphenation, remove conversational parentheticals that read like code‑comments, and standardize terminology.

P3-n2 (NIT)  
Section: References [13–17], [19–22], [23–24], [38–41]; p. 25–26  
Problem: Many of these references are generic reviews or standard theory papers (e.g., Wands 2010, Trotta 2008, Yoo/Bonvin/Di Dio on GR corrections). While the content and metadata for these look broadly plausible, the mapping between each specific claim in the text and the particular reference is sometimes loose (e.g., using [13,14,35] for a specific fNL value where one paper would suffice).  
Required fix: Tighten the mapping between claims and references, ensuring that each assertion (e.g., the exact fNL = −35/8 prediction; γ=3.0 for bounce) is traceable to an explicit equation or table in a specific paper. This is mostly organizational, not substantive.

## Summary recommendation

REJECT

The manuscript presents an ambitiously large multi‑survey anomaly catalog and some interesting methodological lessons (especially the LAMOST training‑bias problem), but it does not yet meet PRD’s standards for citation rigor, reproducibility, and conceptual focus. There are multiple instances of apparently fabricated or future‑dated bibliographic metadata, a non‑reproducible score axis in one key survey (eROSITA), heterogeneous and partly ad‑hoc thresholding that undermines global “rate” statements, and cosmological applications whose methods are underspecified for a standalone physics reader. Addressing the essential issues would require substantial re‑engineering of the analysis chain and a major rewrite; I therefore recommend rejection in the current form, with the suggestion that a narrowed, thoroughly cleaned catalog paper (and perhaps a separate, fully specified cosmology paper) could be suitable for resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E13] **Figure 2 / Table I denominator drift:** the paper gives the initial cross-transfer baseline as **319,443** detections in Fig. 2, but Table I states the same baseline “represents the initial DESI-trained cross-survey scan before native retrains” with a total of **319,443** while also saying the cross-transfer row excludes ACT and that the retained survey-level counts sum to **388,493**. The text around Fig. 2 adds that the canonical **378,280** headline is “not a deduplication of this baseline,” but the baseline and summary wording are easy to misread as if they were derived from the same denominator; this should be tightened because the reader cannot reconstruct from the figure alone why 319,443 and 388,493 coexist without contradiction.[paper]

[P3-E14] **Figure 3 / Table I rate mismatch for SDSS:** Fig. 3’s caption says the SDSS top-1% cut “retains 19,253 = 1.0% of the 1,925,279 scored DR18 spectra,” while Table I lists the SDSS native-retrained anomaly count as **77,905** and footnote ♡ says that is a fixed-size continuity slice at **S ≥ 0.1060**, not a top-1% cut. The body in §III C also says the native re-score “supersedes the cross-transfer count,” so the caption’s apparent top-1% framing conflicts with the main-text claim unless the reader notices the footnote and realizes the 19,253 figure refers to a different threshold family.[paper]

[P3-E15] **Figure 4 / §III C cluster-count arithmetic:** Fig. 4 says the SDSS cross-transfer anomaly embedding resolves **14 HDBSCAN clusters** that group into **3** latent populations, while §III C says the same 77,905 objects yield “14 HDBSCAN clusters (99.4% clustered: 77,473/77,905)” and Table II sums to **77,905** across 10 emission-line categories. The paper never states how the 14 clusters map onto the 10 taxonomy categories or whether those category counts are derived from the HDBSCAN result or from a separate heuristic classifier, so the figure-caption/body relationship is under-specified.[paper]

[P3-E16] **Figure 5 / Table III eROSITA top-anomaly score inconsistency:** Fig. 5 captions the NEOWISE top anomaly with score **11.5**, but Table III lists the top eROSITA anomalies with **SBigAE** scores in the range **1.084** to **0.439** and warns not to use SBigAE as a science axis. The body in §III H treats NEOWISE scores as canonical-S values, yet the same figure family uses “Score = 11.5” without explicitly saying it is on a different axis than Table III’s SBigAE, which is another null-procedure / score-axis comparability gap that needs explicit labeling at the point of use.[paper]

[P3-E17] **Figure 8 panel annotation vs catalog score:** Fig. 8(d) labels TIC 374313355 with **display score 49.5**, and the caption later says that value “matches the catalog cross-transfer score quoted in the text.” But §IV C also says the SDSS native re-score compresses extremes to **S < 14**, and the caption warns the burned-in annotations are display values rather than catalog-pipeline outputs. The figure therefore mixes at least three score notions—display score, DESI-trained cross-transfer score, and native SDSS score—without a compact per-panel legend, making the numerical provenance easy to misread.[paper]

[P3-E18] **Figure 10 caption vs §VI D gate summary:** Fig. 10 says the headline decomposition is **3 PASS / 3 FAIL-with-diagnostic**, but the caption also includes NEOWISE “passes by construction” and then counts it among the three PASS cases. §VI D(ii) repeats that “Counting detector-sensitivity tests only, the PASS tally is 2 (SDSS, Planck) + 1 geometry-QA (NEOWISE),” which is correct but only after reading the fine print. This is a figure-caption/body mismatch in the classification of what constitutes a PASS, and it should be made explicit in the caption itself.[paper]

[P3-E19] **Appendix A / Table V Planck throughput arithmetic:** Table V states the Planck native re-score of **2 × 10^5** patches took **25.3 s**, yielding “∼8,000 patches/s,” and the footnote says an earlier **10.6 s** figure was withdrawn. That arithmetic is correct for 200,000/25.3 ≈ 7,905, but the main-text §III F says the same run had “throughput figures” and the caption to Table V also states the total wall-clock was not preserved. Since the throughput is derived from an incomplete record, the paper should mark it as an approximate back-calculation rather than a measured runtime.[paper]

[P3-E20] **Appendix C / Figure 11 normalization drift:** Fig. 11 captions a “single-tracer baseline = **16.85**” and “dense-tracer limit = **11.71**,” while §V says the main DESI baseline is **σ(fNL)std = 8.98** and explicitly notes the appendix values are on a different internal normalization. The caption does include a normalization note, but the main-text paragraph immediately above Fig. 11 still juxtaposes the 16.85 and 11.71 values with the 8.98 baseline in the same narrative. That is exactly the kind of non-comparable σ juxtaposition the paper warns about elsewhere, and it needs to be quarantined more aggressively.[paper]

[P3-E21] **Appendix E equation / units clarity:** Eq. (E1) defines \( \log_{10}\rho_i \) with terms involving \(A\), \(f_{\rm yr}\), \(f_i\), and \(T_{\rm obs}\), but the equation is presented as a log-amplitude model without stating the unit convention for \(A\) or whether \(f_{\rm yr}\) is numerically 1/yr or a unit-normalization constant. The surrounding text gives \(T_{\rm obs}=16.03\) yr and \(f_i=(i+1)/T_{\rm obs}\), but the dimensional consistency of the logarithm still depends on implicit unit choices that are not spelled out at the equation. This is a standards-level reproducibility issue for the PTA derivation.[paper]

[P3-E22] **Appendix F / ACT scan internal contradiction:** Appendix F says the ACT cross-transfer scan returned **200** anomalous patches, the highest-scored patch has score **∼2.6 × 10^7**, and the overall distribution “concentrates along the Galactic plane,” yet the same appendix says the scan is quarantined and contributes zero objects to the headline. Table V nevertheless includes ACT DR6 with a training time and throughput as if it were a normal survey row, while the main Table I excludes it. The paper should state more prominently that ACT appears only as a quarantined methodological artifact and is not part of any headline arithmetic.[paper]