# P3 auto-2026-06-05_1717pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (6702 chars)
**Wall time**: 64.7s

---

P3-E1 (ESSENTIAL) – Global (multiple pages, esp. abstract p.1, Table I p.7, Conclusions p.14)  
**Problem:** The paper repeatedly claims specific “× improvement” factors relative to Liang et al.  without any verifiable quantification in . Examples:  
- Abstract: “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase.”  
- Conclusions §VII (p.14): “This is ∼ 141× the largest prior single-survey catalog ; DESI-only is a ∼ 73× like-for-like increase.”  
Liang et al. 2023 MNRAS 525, 1078 (“Outlier detection in the DESI Bright Galaxy Survey”) report 2,685 anomalies from DESI BGS EDR (∼250k spectra). The present DESI catalog has 195,829 anomalies from 22.5M spectra. The ratio 195,829 / 2,685 ≈ 73 (consistent with the “73×” claim), but the paper nowhere justifies “141× the largest prior single-survey anomaly catalog.” Even if one used the *total* multi-survey anomalies (378,080 or 378,280) divided by 2,685, the ratio is ∼140–141, but this is not “single-survey.” The claim as written is internally inconsistent, and the “largest prior” assertion is not supported by a systematic survey of the literature (e.g. large-scale anomaly / outlier catalogs in SDSS not cited).  
**Required fix:**  
- Reword all “141× … largest prior single-survey catalog” statements to reflect what is actually being compared (multi-survey vs prior single-survey DESI BGS catalog). E.g. “Our multi-survey point-source catalog (378,080 objects) is ∼141× larger in object count than the DESI BGS anomaly catalog of Liang et al. .”  
- Remove “single-survey” or justify it with a clear argument that  is indeed the largest prior single-survey anomaly catalog in astronomy (including a brief literature scan).  
- Ensure that every numerical “×” factor is explicitly recomputed and checked in the text, and that the quantity being compared (DESI-only vs DESI-only, total multi-survey vs single-survey baseline) is stated unambiguously each time.

---

P3-E2 (ESSENTIAL) – Abstract p.1, §V (Cosmological Applications) pp.10–11, §VII p.14  
**Problem:** σ(fNL) forecasts from different procedures are juxtaposed without *explicit, repeated* “not directly comparable” caveats wherever they appear side-by-side, violating the review instruction requirement. Example in abstract:  
- “An empirical Landy–Szalay bias measurement … yields αjk = 0.19 ± 0.65 (< 1σ from null); inserting this into the Fisher-positivity-respecting form 1/σ(fNL )2 = F0 + c α2 gives a central forecast σ(fNL ) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at < 1σ; σ(fNL )std = 8.98 single-tracer baseline).”  
In §V the same σ(fNL) numbers are used: empirical αjk forecast, GS subset forecast, a “standard” DESI QSO baseline, and a SPHEREx multi-tracer forecast, with mixed approximations and different nuisance/systematics assumptions. The paper acknowledges some caveats but does not *every time* it juxtaposes σ(fNL) values from different assumptions explicitly state that these σ values are not directly comparable as independent constraints. This is precisely the kind of comparison the user instructions require to be flagged.  
**Required fix:**  
- For every instance where σ(fNL) values from two different forecast configurations are presented in the same sentence, figure, or table (e.g. σ(fNL)=8.14 vs σ(fNL)std=8.98; GS subset vs baseline; SPHEREx forecast vs DESI-only), add explicit language such as: “These σ(fNL) values are forecasts under different modeling assumptions and are not directly comparable as independent measurements.”  
- Clarify, at first occurrence in §V and again wherever numbers are compared, which forecasts include or neglect which systematics (fiber assignment, GR projection, shot noise, priors on nuisance parameters).  

---

P3-E3 (ESSENTIAL) – Bibliography entry  p.19 and its use  
**Problem:** Citation  is: “Y. Liang et al., ‘Outlier detection in the DESI Bright Galaxy Survey,’ Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664.” This matches the real paper: MNRAS 525, 1078–1094 (2023), arXiv:2307.07664. However, the text attributes statistics without clear traceability:  
- Introduction p.1: “Liang et al.  applied a normalizing-flow autoencoder to ∼ 250,000 DESI EDR spectra, finding 2,685 anomalies (1.07%).”  
This matches the abstract and tables of , which report BGS sample size ≃250k and 2,685 outliers (1.07%).  
However, in §III E / §VI E the paper later states: “Our DESI anomaly rate of 0.87% is consistent with the 1.07% rate reported by Liang et al.  on the DESI EDR, despite differences in model architecture and a ∼90× increase in sample size.” The “∼90×” factor refers to sample size (22.5M vs 250k ≈ 90), but the sentence construction can be read as “90× increase in anomaly counts,” which is incorrect (it is ~73×; see P3-E1).  
**Required fix:**  
- Clarify in §VI E that the ∼90× refers explicitly to total *sample size*, not to anomalies. E.g. “…and a ∼90× increase in *spectral sample size* (22.5M vs ~0.25M).”  
- Ensure every mention of comparison to  separately states sample-size factor and anomaly-count factor, consistent with recomputed values from .  

---

P3-E4 (ESSENTIAL) – Reference  p.19  
**Problem:** Reference  reads: “C. Nicolaou et al., ‘Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,’ Mon. Not. Roy. Astron. Soc. (2026, in press).” The authorship and title correspond to known arXiv work “Anomaly detection in DESI Early Data Release spectra with Astronomaly” (Nicolaou et al.), but as of the paper’s stated date (“June 2026”) there is no evidence that it is “in press” at MNRAS; the arXiv version is from 2025 and not yet accepted (this would need to be confirmed at the time of PRD review via ADS/arXiv). Marking a paper as “in press” in a specific journal without an accepted-manuscript record is unacceptable for PRD.  
**Required fix:**  
- Verify via arXiv/ADS whether the paper is accepted and “in press” at MNRAS.  
  - If yes, update the reference with correct year, journal, volume, page, and DOI.  
  - If not, change the citation to an arXiv reference only, e.g. “arXiv:25xx.xxxxx (submitted to MNRAS)” or “(2025, submitted).”  

---

P3-E5 (ESSENTIAL) – Internal version-history wording p.15, Reference   
**Problem:** In ref. , the text reads:  
“J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].”  
This is clearly internal bookkeeping/version-history commentary (“bibkey label retained as … continuity”), which should not appear in a PRD bibliography. It is not standard reference formatting and looks like internal notes that leaked into the manuscript.  
**Required fix:**  
- Remove the bracketed explanatory note from the reference and adopt standard PRD reference style; e.g.:  
  “C. Heinrich, O. Doré, and E. Krause, J. Cosmol. Astropart. Phys. 04, 074 (2024), arXiv:2311.13082.”  

---

P3-E6 (ESSENTIAL) – Internal bookkeeping / review-log language p.15, p.13  
**Problem:** Several places contain internal-audit or version-tracking prose explicitly disallowed by the review instructions:  
- Table IV caption p.13 refers to “Ceffyl KDE chain; §V A” and “resolved in paper; derivations in companion data repository”. That is acceptable, but Table IV entry (d) explicitly uses “Ceffyl KDE chain; §V A” as an audit tag; borderline but probably acceptable.  
- Appendix F p.16–17: “The 8-way-with-ACT dedup variant, which would have produced 388,693 − 10,213 = 378,480 unique objects (+200 relative to the headline), is preserved as a sensitivity-check artifact in the companion data repository.” The use of “artifact” here is not accessibility-related; it is internal-variant language, but not clearly version history.  
More clearly problematic:  
- Acknowledgment of a HuggingFace dataset: “… (private pending arXiv acceptance; public upon acceptance).” This is explicit version/acceptance conditioning.  
- Multiple mentions: “Path-C-final catalog,” “Path-C protocol forbids retain- ing a survey on a checkpoint that fails both gate criteria,” etc. These look like internal project nomenclature; acceptable as long as clearly defined.  
The strongest violation per instructions is the dataset access note: conditioning data release on acceptance is *review-log* style meta-commentary.  
**Required fix:**  
- Remove or rephrase “private pending arXiv acceptance; public upon acceptance” to a neutral data-availability statement (e.g. “will be made public after journal publication; current access details provided in the cover letter”).  
- Scan the manuscript once more to eliminate any residual internal “R-round”, “superseded”, or review-log markers (none of the explicit forms appear now, but PRD will expect no acceptance-conditioned phrasing).  

---

P3-E7 (ESSENTIAL) – Duplicate phrase / possible copy-paste artifact p.2  
**Problem:** §II D, Path-C Rebuild, last sentence of the paragraph:  
“The native retrains, systematics masks, and dedup pipeline are all deterministic and documented in reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”  
“reproducibility scripts shipped … (reproducibility scripts shipped …)” is a clear duplicated phrase.  
**Required fix:**  
- Remove the duplicated phrase; e.g. “…documented in reproducibility scripts shipped with the companion data repository.”  

---

P3-M1 (MAJOR) – Equation and dimensional consistency for NANOGrav template (Appendix E, eq. (E1) p.16)  
**Problem:** The template  
\[
\log_{10} \rho_i = \tfrac{21}{2}\log_{10} A - \log_{10}(12\pi^2) + (\gamma - 3)\log_{10} f_{\mathrm{yr}} - \gamma \log_{10} f_i - \log_{10} T_{\mathrm{obs}}
\]  
is intended to represent the strain/background spectral density parametrization used by NANOGrav (Phinney 2001, NANOGrav 15yr). However:  

- The factor 21/2 ≈ 10.5 is unusual; standard GW background expressions use terms like \(2\log_{10} A\) or \(5\log_{10} f/f_{\rm ref}\), not 10.5.  
- The paper does not specify what ρi is (energy density per unit log f? strain PSD?).  
- Without explicit definition and units, dimensional consistency cannot be checked, and PRD readers cannot reproduce the likelihood.  

Given the central role of this expression in the reported γ = 2.567 ± 0.382 and Bayes factors, this is below PRD standards.  
**Required fix:**  
- Explicitly define ρi (and whether it is dimensionless energy-density per logarithmic frequency, strain PSD, or another derived quantity).  
- Derive eq. (E1) step-by-step from a standard expression (e.g. Phinney 2001 or the NANOGrav 15yr methods paper), making clear how the coefficient 21/2 arises and that the expression is dimensionally consistent.  
- If the current equation is a shorthand, either replace it with the standard, verifiable form (e.g. using ΩGW or hc) or provide a reference equation number from  that matches it.  

---

P3-M2 (MAJOR) – fNL Fisher formalism description and numeric consistency (§V p.10–11, Appendix C p.15–16)  
**Problem:** The paper uses a nonstandard “Fisher-positivity-respecting” parametrization  
\[
1/\sigma(f_{\rm NL})^2 = F_0 + c\,\alpha^2
\]  
with F0 = 1/8.982 and c = 0.0747, and claims that simply “inserting αjk = 0.19” yields σ(fNL)=8.14 and 1σ envelope [3.92, 8.98]. However:  
- The relation between F0, c, and the quoted errors is not demonstrated. From the stated values, a reader cannot trivially reproduce σ=8.14 and the bounds 3.92 and 8.98.  
- Appendix C then presents a linear scaling formula (“fractional improvement scales as (6.1%/0.15) α”) which is conceptually inconsistent with the α^2 Fisher form and could mislead readers about the regime of validity.  
- These forecasts are central to the claimed “7.9% improvement,” but the derivation is under-documented; PRD expects fully auditable Fisher steps or a precise reference to a prior calculation.  

**Required fix:**  
- Add a brief derivation of the Fisher expression, showing explicitly how F0 and c were obtained (e.g. from a baseline Fisher matrix and reweighting of a biased tracer sample).  
- Show explicitly how plugging in αjk and its uncertainty produces σ(fNL)=8.14 and the stated confidence interval [3.92,8.98]; if approximations are made (e.g. Gaussian in α, error propagation), state them.  
- In Appendix C, clearly distinguish the α^2-based exact Fisher treatment from the approximate linear scaling and mark the latter as a small-α expansion, with a range of validity.  

---

P3-M3 (MAJOR) – NANOGrav Bayes factor interpretation (§V A p.11, Appendix E p.16)  
**Problem:** The paper quotes Bayes factors derived via Savage–Dickey:  
“BMB/free = 3.23 and BSMBHB/free = 4.52 × 10−4, giving BMB/SMBHB = 7.14×103 (log10 B = +3.85, ‘decisive’ on Jeffreys’ scale).”  

Concerns:  
- It is not clearly specified what prior range/shape on γ is used in the Savage–Dickey ratio—only “flat priors γ∈[0,7]” is stated. Readers cannot reproduce the Bayes factors without additional detail on the parameterization, normalization, and the effective prior mass at the nested models’ γ values (3.0 and 4.33).  
- The same NANOGrav 15yr data set has been analyzed by NANOGrav and others; those papers do not claim decisive exclusion of SMBHB in favor of any bounce model. Using the same likelihood to claim a Bayes factor of ~7×10^3 in favor of bounce vs SMBHB requires very careful cross-check; otherwise it risks over-interpretation.  

**Required fix:**  
- Provide a concise formula for the Savage–Dickey ratio used, including explicit prior on γ and how the nested-model parameter values were evaluated (e.g. kernel density estimate at γ=3.0 and 4.33).  
- Compare the derived Bayes factors qualitatively with existing PTA literature (e.g. NANOGrav 15yr companion papers , EPTA, PPTA) and clarify that this is an illustrative re-analysis with strong dependence on prior choice, not a community consensus.  
- Soften the language: avoid “decisive” and instead phrase as “under our chosen priors, the posterior favors the bounce spectral index over the canonical SMBHB index by a Bayes factor B ≈ 7×10^3; this is prior-dependent and not a standard result of the PTA collaborations.”  

---

P3-M4 (MAJOR) – Bibliography , –,  cross-check  
**Problem:**  
-  Doré et al., SPHEREx white paper: arXiv:1412.4872, citation is correct.  
-  Quintin et al., “Matter creation in a nonsingular bouncing cosmology,” Phys. Rev. D 90, 063507 (2014), arXiv:1406.6049; your reference omits the arXiv ID and only gives a general description.  
-  Cai, “Exploring bouncing cosmologies with cosmological surveys,” Sci. China Phys. Mech. Astron. 57, 1414 (2014), arXiv:1405.1369; again, the arXiv ID is omitted.  
-  Heinrich et al., JCAP 04, 074 (2024), arXiv:2311.13082: bibliographic info is essentially correct but formatting is nonstandard as noted in P3-E5.  

While these are not fatal, PRD expects meticulous bibliographic completeness, especially for methods forecasts imported into your analysis.  
**Required fix:**  
- Add missing arXiv identifiers for  and .  
- Normalize formatting of  as in P3-E5.  
- Scan all cosmology-methods references via NASA ADS or arXiv to ensure titles, volumes, years, page numbers, and arXiv IDs are accurate and consistent with PRD style.  

---

P3-M5 (MAJOR) – “Largest multi-archive anomaly search” novelty claims (Table I caption p.7, Conclusions p.14)  
**Problem:** The paper states:  
- Table I caption: “The total represents the largest multi-archive anomaly search reported to date.”  
- §VII: “We have presented the largest multi-archive anomaly detection campaign to date…”  

These strong novelty claims are not supported by any quantitative survey of related work beyond [10–12]. For example, there are other large anomaly/outlier projects in SDSS, time-domain surveys, and multi-wavelength cross-matches that may approach similar scales. Without an explicit comparison (e.g. a table listing previous multi-survey anomaly searches and their sizes), this “largest” claim is unsubstantiated.  
**Required fix:**  
- Either:  
  - Provide a short subsection or paragraph in the Introduction comparing your 37.3M sources / 378k anomalies against the most relevant previous *multi-survey* anomaly searches (not only [10–12]), citing at least a few such efforts if they exist, and justifying the “largest” statement.  
- Or:  
  - Soften the claim to something like “to our knowledge, one of the largest multi-archive anomaly searches to date” or “a large-scale multi-archive anomaly search,” which is accurate without requiring an exhaustive census.  

---

P3-M6 (MAJOR) – Data release conditioning in Acknowledgments / Data Availability p.14–15  
**Problem:** Data availability note:  
“The Path-C catalog … is deposited on HuggingFace at [URL] (private pending arXiv acceptance; public upon acceptance).”  
Conditioning public release on “arXiv acceptance” is not appropriate for PRD and hinders reproducibility during peer review and after publication. PRD expects data and code to be available upon publication regardless of arXiv listing.  
**Required fix:**  
- Commit to making the dataset and code publicly available upon PRD publication (or sooner), independently of arXiv status, and state this clearly.  
- Provide a stable DOI-based or repository-based identifier if possible (e.g. Zenodo), instead of a private HuggingFace link with conditional access.  

---

P3-M7 (MAJOR) – Internal consistency of counts and percentages (multiple places)  
**Problem:** I recomputed several key reported fractions from the numbers appearing in the text:  

- DESI anomaly rate: 195,829 / 22,504,897 ≈ 0.870%, consistent with 0.87% (okay).  
- Cross-transfer total: 319,443 anomalies over 37,292,042 sources ⇒ 0.856%, stated as 0.86% (okay).  
- Path-C de-dup compression: 388,493 – 378,280 = 10,213; 10,213 / 388,493 ≈ 2.63%, stated 2.629%, consistent.  
- NEOWISE polar-cap fraction: 17 / 436 ≈ 3.9%; uniform-sphere expectation for |b_ecl|>80° is ≈1.52%; 3.9 / 1.52 ≈ 2.57, consistent with 2.6× (okay).  

However, some key numbers are under-documented:  
- The claim “top-1,000 DESI anomalies against 20 catalogs yields 178 unmatched ⇒ 17.8%” is not reproducible from within the paper; the 20-catalog list is given, but matching radius, handling of blended matches, and inclusion rules for multiple catalogs are left to the companion repository. PRD usually requires enough in-text detail to reproduce the calculation at least conceptually.  

**Required fix:**  
- Add a concise but explicit description of the matching procedure for the 20-catalog cross-match: radius, catalog list (already given), and the rule for declaring a match (≥1 catalog with a source within 5″).  
- State that 178/1000 was computed under exactly these conditions, so readers can cross-check if needed.  

---

P3-M8 (MAJOR) – Overly long and diffuse for claimed contribution  
**Problem:** The manuscript is 20 pages, densely packed, and attempts to cover: a very large anomaly catalog, methodological audits (Path-C), survey-by-survey astrophysical results, multi-tracer fNL forecasts, and a NANOGrav re-analysis. As a PRD *methods* paper, the core contribution is the catalog methodology and its cosmological applications via multi-tracer fNL. The detailed survey-level astrophysical taxonomy, exhaustive injection-recovery discussions, and full PTA appendix risk diluting the central message.  
**Required fix:**  
- Consider reducing the main text to ~14–16 pages by:  
  - Moving the PTA re-analysis (Appendix E) to a separate companion paper or significantly compressing it to a brief illustrative paragraph with a reference to a dedicated analysis.  
  - Condensing some of the survey-by-survey descriptive material (e.g. detailed UMAP/cluster taxonomies and image galleries) to supplemental material.  
- This will make the main PRD article sharper and better focused on the cosmology-methods contribution.  

---

P3-m1 (MINOR) – Equation numbering and referencing  
**Problem:** Some equations are referenced inconsistently:  
- Eq. (2) is referred to as “Eq. 2” in some places, “Eq. (2)” in others. PRD expects consistent formatting.  
- Appendix E’s eq. (E1) is not explicitly cited in the main text when discussing the NANOGrav fit; readers must infer the connection.  
**Required fix:**  
- Normalize equation references to PRD style (e.g. “Eq. (2)”).  
- When introducing the NANOGrav fit in §V A, explicitly refer to eq. (E1) in Appendix E.  

---

P3-m2 (MINOR) – Minor wording / clarity issues  
**Problems & required fixes:**  
- “Path-C rebuild Methodology: Native Retrains as Core Protocol” – initial mention in abstract/intro should include a very short gloss (“Path-C is our six-step catalog rebuild and validation pipeline; details in §II D”).  
- A few informal phrases detract from PRD tone, e.g. “This result provides the single most important methodological lesson of this work” (§VI A). Prefer more neutral wording.  

---

P3-m3 (MINOR) – Reference cross-checks  
**Problem:** Most references (DESI DR1, LAMOST DR10, SDSS DR18, eROSITA DR1, Gaia DR3, NEOWISE, Planck 2018, NANOGrav 15yr, PTA references) are accurate. However, a few have minor stylistic issues (e.g. missing journal abbreviations for some).  
**Required fix:**  
- Run the entire bibliography through ADS or arXiv, then align entries with PRD reference style, including consistent journal abbreviations (Phys. Rev. D, Astron. Astrophys., Mon. Not. R. Astron. Soc., etc.), years, volume and page/article numbers, and arXiv IDs where appropriate.  

---

P3-n1 (NIT) – Typographical / stylistic issues  
**Problems:**  
- Minor hyphenation and spacing issues (e.g. line breaks splitting “astro- physics” / “variab. IF”).  
- Occasional use of “≃” vs “≈”; PRD typically allows either but consistency is preferable.  
**Required fix:**  
- Clean up hyphenations and line-break artifacts in the final typeset version.  
- Standardize approximate-equality notation.  

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper is ambitious and technically detailed, with largely correct and verifiable citations to DESI/SDSS/LAMOST/eROSITA/Gaia/NEOWISE/Planck and NANOGrav literature. However, the cosmological forecasts and NANOGrav re-analysis need clearer derivations and caveats; some novelty and “× improvement” claims are presently muddled, one reference is incorrectly labeled “in press,” and internal bookkeeping language leaks into the bibliography and data-availability statements. These issues, while fixable, require substantial revision to meet PRD’s standards for methodological rigor and clarity.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E8] **Abstract-to-body mismatch:** the abstract says the catalog contains **378,280 unique anomalies** and a **378,080 point-source tier**, but the results section’s Table I and §III report **388,493 survey-level detections** before deduplication and **378,280** after deduplication, while the body also says the **point-source tier** is the recommended subset for downstream use. The abstract does not explicitly state that the 378,280 headline count includes **200 Planck CMB patches**, so the “unique anomalies” wording is slightly misleading unless the stratification is stated there as it is later in Table I and §VII.[paper text]

[P3-E9] **DESI arm-count arithmetic is inconsistent in the narrative:** the DESI section says **151,244 multi-band + 44,436 B-dominant + 34 R-dominant + 19 Z-dominant + 96 artifact suspects**. Those counts sum to **195,829**, which matches the headline DESI total, but the text later states “the three highest-scored anomalies are Z-dominant,” while Table VI shows only **19 Z-dominant** objects overall. That is fine, but the body’s claim that “the multi-band majority indicates that most anomalies deviate across the full wavelength range” is not supported by any quantitative comparison beyond the raw fraction **77.2%**; no uncertainty or null baseline is given.[paper text]

[P3-E10] **Figure 2 caption/body mismatch on SDSS scores:** the caption says the SDSS native re-score “compresses the same objects to **S < 14**, eliminating the 10^4–10^11 tail,” but the SDSS subsection states the native retrain yields a **top-77,905 native slice at S ≥ 0.1060**. These are not the same thresholding convention, and the paper does not clearly explain that the figure is showing a *different score normalization* or a *different slice definition*. Readers are left to infer that one is the native score axis and the other is the DESI-trained transfer axis, but that distinction should be made explicit in the caption or body.[paper text]

[P3-E11] **Table I percentage arithmetic should be made explicit for the aggregate row:** the table gives **37,292,042 total** and **319,443 anomalies**, which indeed yields **0.8569%**, rounded to **0.86%**. The Path-C unique row gives **37,272,042** and **378,280**, which is **1.014%**, rounded to **1.01%**. Those are correct, but the table does not show the arithmetic, and because the unique row is the main catalog result, the rounding could be misread as a “rate increase” rather than a change in denominator after deduplication. A short note that the rate is computed as **nanom / Ntotal** after deduplication would remove ambiguity.[paper text]

[P3-E12] **Cross-survey match count in §IV A is not fully auditable from the text:** the body says the DESI top-1,000 cross-match against 20 catalogs yields **822/1,000** archival IDs and **178/1,000** genuinely novel objects. Those numbers are internally consistent, but the text also says the SIMBAD-unmatched headline should not be interpreted as a novelty fraction because a deeper NED+VizieR sweep resolves **20/20** randomly selected SIMBAD-unmatched objects. This makes the “17.8% genuine novelty fraction” a *sample-stratum point estimate*, not a catalog-wide rate, yet the main text and conclusions still present it with the same visual weight as the more stable survey-level percentages. The distinction should be repeated more forcefully wherever 17.8% appears.[paper text]

[P3-E13] **Appendix C contradicts the main-text Fisher scaling language:** Appendix C says the fractional improvement scales as \((6.1\%/0.15)\alpha\), while the main text and Appendix D use the positivity-respecting form \(1/\sigma(f_{\rm NL})^2 = F_0 + c\alpha^2\). Those are not equivalent beyond a local approximation near the fiducial point. The appendix itself says the linear scaling is “consistent with the linear-bias regime,” but it does not explicitly warn that it is only an approximation and should not be used to reproduce the quoted central forecast **σ(fNL)=8.14**. This is an internal-method mismatch, not just a presentation issue.[paper text]

[P3-E14] **Table VII contains an arithmetic inconsistency relative to §V:** the table claims the “boldface row” at **α = 0.15** matches the Section V baseline exactly and gives **σ(fNL)=8.43** with **6.1% improvement**, while §V’s empirical forecast gives **σ(fNL)=8.14** with **7.9% improvement**. The manuscript does say Appendix C is a sensitivity study and §V is the empirical result, but Table VII does not clearly state that the 8.43 value is an *older fixed-α forecast* rather than the current headline forecast. That stale-number distinction should be made explicit in the table caption or the table itself.[paper text]

[P3-E15] **Figure 7 / Table IV gating language is not fully aligned:** Figure 7 labels the Planck CMB native retrain as **PASS, 500/500 = 100% at 5σ Gaussian-bump amplitude**, while Table IV describes the same item only as “**inert at σδfiber = 0.05**” for a different caveat row and elsewhere lists the Planck result under the general residual-caveat framework. Because the figure mixes different plant families and the table mixes multiple validation axes, the reader can lose track of which gate criterion is being referenced. The numerical results themselves are consistent, but the paper should explicitly name the gate family each time to prevent apples-to-oranges reading.[paper text]

[P3-E16] **Stale count in the ACT appendix:** Appendix F says the 8-way-with-ACT variant would have produced **388,693 − 10,213 = 378,480** unique objects, but elsewhere the paper’s primary Path-C unique count is **378,280** and the cross-transfer baseline is **319,443**. The arithmetic inside Appendix F is fine, but the appendix does not explicitly remind the reader that **378,480** is a *sensitivity-check artifact* and not a catalog result. Because the number is very close to the headline count, it is easy to mistake it for an updated main result; it needs stronger labeling as non-canonical.[paper text]

[P3-E17] **Figure 6 caption vs. body on the TIC 374313355 score:** the body says TIC 374313355 is a DESI×SDSS match and “strong follow-up candidate,” while the figure caption gives the SDSS epoch score as **49.5** and the DESI epoch score as **8.1**. The main text does not explicitly explain why the same source can have such a large inter-epoch score shift beyond calling it “dramatically elevated continuum and emission-line flux.” That is plausible, but the paper should state the exact reason for the score discrepancy in one sentence because the figure is otherwise vulnerable to being interpreted as a scoring inconsistency rather than a genuine variability signal.[paper text]