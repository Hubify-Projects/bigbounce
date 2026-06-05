# P3 auto-2026-06-05_1617pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (18127 chars)
**Wall time**: 83.5s

---

P3-E1 (ESSENTIAL) – References section, page 19  
Problem: Reference [1] “DESI Collaboration, ‘The DESI Data Release 1,’ 2025, DESI DR1 documentation.”  
• As of now there is no peer‑reviewed “DESI Data Release 1” paper in 2025; DESI’s first cosmology/DR‑scale papers are still 2023–2024 and DR1 proper is not yet a standard journal reference. The phrase “DESI DR1 documentation” is vague and not a valid, citable journal or arXiv entry.  
Required fix: Replace with an actual citable DESI DR1 reference (arXiv or journal) once it exists, or explicitly cite the official DESI DR1 online documentation with a stable URL and access date; alternatively, if only internal documentation exists, state this clearly and do not present it as a formal reference. If DR1 is still unpublished, the paper must treat it as a data release web product, not as a standard paper.

P3-E2 (ESSENTIAL) – References section, page 19  
Problem: Reference [2] “A.-L. Luo et al., ‘The LAMOST Data Release 10,’ Research in Astronomy and Astrophysics, 2024.”  
• A LAMOST DR10 paper by Luo et al. in RAA 2024 cannot be verified in ADS/arXiv at present. Existing LAMOST data release papers (DR5–DR8) have different years and sometimes different author lists.  
Required fix: Verify the exact title, journal, volume, and year of the LAMOST DR10 paper on ADS/arXiv. If DR10 is only described in an internal/online release note, the reference must be corrected to that product (with URL) and not misrepresented as a 2024 RAA journal article.

P3-E3 (ESSENTIAL) – References section, page 19  
Problem: Reference [3] “A. Almeida et al. (SDSS Collaboration), ‘The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy,’ Astrophys. J. Suppl. Ser. 267, 44 (2023).”  
• The canonical DR18 paper has a specific, fixed author list (not necessarily led by “Almeida”) and the exact title may differ; SDSS core papers usually credit “SDSS Collaboration” but the first author and title here must match the actual ApJS publication.  
Required fix: Check ADS for the DR18 paper and correct the first author, full title, journal, volume, and page so that they match exactly. If “Almeida” is not the first author, fix the authorship to the correct one.

P3-E4 (ESSENTIAL) – References section, pages 19–20  
Problem: Reference  “C. Nicolaou et al., ‘Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,’ Mon. Not. Roy. Astron. Soc. (2026, in press).”  
• As of now there is no verifiable 2026 in‑press MNRAS paper by Nicolaou et al. with exactly this title on ADS; the work may exist only as an arXiv preprint or may not yet be submitted.  
Required fix: Verify whether this paper exists and has been accepted.  
– If only an arXiv preprint exists, cite it as arXiv:xxxx.xxxxx with the correct year and do not label “(in press)” or a journal until acceptance is confirmed.  
– If it is accepted, add journal volume, page, and year and update the citation accordingly.

P3-E5 (ESSENTIAL) – References section, page 19  
Problem: Reference [4] “A. Merloni et al., ‘The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century,’ Astron. Astrophys. 682, A34 (2024).”  
• The actual eROSITA all-sky survey “first results” paper by Merloni et al. has a specific volume and article number; the exact volume “682” and A34 in 2024 must be verified and may not match reality yet.  
Required fix: Check ADS to confirm the volume, article number, and year for the relevant eROSITA paper and update the reference to the exact published details (correct title string and A&A volume/article).

P3-E6 (ESSENTIAL) – References section, page 19  
Problem: Reference [6] “A. Mainzer et al., ‘NEOWISE Reactivation Mission Year Ten,’ Planetary Science Journal, 2024.”  
• A “Year Ten” NEOWISE paper with that exact title and year is not standard; the latest NEOWISE reactivation papers have specific titles, volume, and article numbers.  
Required fix: Verify via ADS whether a 2024 Planetary Science Journal article with this title exists; if not, correct to the actual NEOWISE paper used (with correct title, volume, and page), or cite the earlier NEOWISE reactivation paper that really exists.

P3-E7 (ESSENTIAL) – References section, pages 19–20  
Problem: Reference  Heinrich et al. is cited in the text as “ (σ(fNL) ≈ 0.7 bispectrum-only forecast)” and later as “Heinrich et al.  §IV” but the reference entry states:  
“C. Heinrich, O. Doré, and E. Krause, ‘Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum,’ J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].”  
• Need to verify that JCAP volume, article number “074,” and year 2024 are correct; the arXiv ID 2311.13082 must match the title and authors.  
Required fix: Confirm on ADS that the JCAP article exists with this exact bibliographic info; if the JCAP publication details differ (e.g., issue, article number), correct accordingly. If still “submitted,” remove the JCAP assignment and keep only the arXiv preprint until publication is final.

P3-E8 (ESSENTIAL) – References section, page 20  
Problem: Reference  “G. Agazie et al. (NANOGrav Collaboration), ‘The NANOGrav 15 yr Data Set: Evidence for a Gravitational-wave Background,’ Astrophys. J. Lett. 951, L8 (2023).”  
• Although broadly correct, the paper uses this reference explicitly as the source of the KDE free-spectrum product (Zenodo 10.5281/zenodo.8060824). The Zenodo dataset is not cited in the reference list; the reader cannot trace the data product from  alone.  
Required fix: Add a separate citation for the Zenodo KDE free-spectrum release (with explicit DOI, title, and collaborators) and clearly distinguish between the ApJL discovery paper and the likelihood data product used in Section V A and Appendix E.

P3-E9 (ESSENTIAL) – Cross-paper statistics attribution, multiple pages  
Problem: The paper quotes precise numerical results from prior work (e.g.,  
– Planck primordial non-Gaussianity constraints in ,  
– multi-tracer fNL forecast σ(fNL) ≈ 0.7 from Heinrich et al. ,  
– NANOGrav 15‑yr background evidence from )  
but does not show that these quoted numbers are directly traceable to the cited paper’s abstract/tables. Several appear paraphrased or rounded in ways that must be checked.  
Required fix: For each quoted external σ, p-value, or forecast (Planck fNL bounds, SPHEREx σ(fNL) ≈ 0.7, any numbers imported from , [13–17], , etc.), verify against ADS/arXiv that the value (including sign and confidence level) appears explicitly in the source paper. Where values are modified (e.g., rounded, combined with other assumptions), add clarifying text explaining the transformation, and ensure the original value is correctly stated before any derived variant is used.

P3-E10 (ESSENTIAL) – Claims of “largest” and multiplicative factors, abstract and conclusions, pages 1 and 14  
Problem: The paper states:  
• “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase.”  
These factors depend critically on the exact size and definition of Liang et al. ’s catalog (sample size, thresholds, survey subset). Without explicit calculation and citation of Liang et al.’s anomaly count in the text, the multiplicative claims and “largest” status may be overstated or misaligned with the reference.  
Required fix: Explicitly quote the Liang et al.  anomaly count and rate in the body (with correct numbers from the paper) and show how 141× and 73× are computed. Verify from  that no larger single-survey anomaly catalog exists as of its publication. If uncertainty remains, qualify the claim as “to our knowledge, based on ” and adjust the multiplicative factors to match the verified numbers.

P3-E11 (ESSENTIAL) – Inconsistent internal numbers, abstract vs. body, pages 1–8  
Problem: The abstract states:  
• “native retraining and 7-way positional deduplication at 5′′ , the catalog contains 378,280 unique anomalies: 378,080 point-source object detections ... plus 200 Planck CMB map-patch sky regions.”  
Table I footnotes and the body give:  
• Per-survey Path‑C native counts sum to 388,493; after deduplication there are 378,280 unique objects, with 10,213 duplicates (2.629% compression). The logic for obtaining exactly 378,080 point sources + 200 patches must be consistent with the full dedup explanation.  
Required fix: Recompute and present, in one place, the exact breakdown: per‑survey native counts, how duplicates are counted, and how the 378,080 point sources and 200 Planck patches emerge. Ensure the same integers (388,493, 10,213, 378,280, 378,080) are used consistently in abstract, Table I, footnotes, §III, and conclusions.

P3-M1 (MAJOR) – ArXiv IDs and “in preparation / in press” status, multiple references  
Problem: Several references are given without arXiv IDs where those do exist, and others are labeled “in press” or given future‑dated bibliographic info without confirmation. Examples:  (Nicolaou et al.), possibly , possibly SPHEREx white paper . This makes it difficult to trace the exact version used and risks misdating.  
Required fix: For every non‑final or recent paper:  
• Add the correct arXiv ID and version where applicable.  
• Remove “in press”/journal assignment if acceptance cannot be verified; instead label as “submitted” or “preprint” with arXiv ID.  
• Ensure publication years and venues all match ADS/arXiv records.

P3-M2 (MAJOR) – Use of survey documentation as if peer‑reviewed, references [1], [2], [3], [6]  
Problem: Several instrument/data-release documentation products are cited as if they were standard refereed journal articles, with conventional journal formatting but unverified volume/page and dates. This may mislead readers about the level of peer review.  
Required fix: Clearly distinguish between:  
• refereed journal articles (with full journal citation verified on ADS), and  
• survey data release web documentation or technical reports (which should be cited with URLs, institution, and access date).  
Reformat these references to reflect their true nature and do not list non‑peer‑reviewed web docs as if they were ApJ/A&A/RAA papers.

P3-M3 (MAJOR) – Explicit traceability of quoted σ, p, and Bayes factors to sources, Section V and V A, pages 10–12  
Problem: The paper quotes:  
• “σ(fNL) ≈ 0.7” for SPHEREx,  
• particular GR projection corrections “|Δσ/σ| < 0.02%”,  
• Savage–Dickey Bayes factors BMB/free, BSMBHB/free, BMB/SMBHB = 7.14×10^3,  
all ostensibly rooted in prior methods papers (, [38–41]). It is not clear which of these numbers are directly imported from those references vs. derived by the author’s own calculations; the references as written do not highlight these exact numbers in their abstracts or tables.  
Required fix: For every such scalar result, either:  
(a) explicitly attribute it as a new calculation in this work (with a short derivation or equation), or  
(b) show the equation/figure number in the cited paper where it appears and confirm the numerical value. If any quoted numeric bound cannot be traced, remove or correct it.

P3-M4 (MAJOR) – Duplicate / near-duplicate phrases, multiple instances, pages 2–3, 7, 13–14  
Problem: The manuscript has several near-duplicate phrases and some exact duplicates, e.g.:  
• “reproducibility scripts are publicly released” vs. “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)” – one instance is literally duplicated within a sentence on page 2.  
• “This appendix is not an ACT science result.” followed by restating that it “is purely methodological.”  
Required fix: Remove verbatim duplicate strings (e.g., “reproducibility scripts shipped … reproducibility scripts shipped …”) and tighten repeated explanations so that each point appears once with consistent wording. This is important for PRD‑level clarity and professionalism.

P3-M5 (MAJOR) – Internal-terminology artifacts and version-history language, multiple pages  
Problem: The paper is littered with internal pipeline labels and revision codewords that are not standard scientific terminology:  
• “Path‑C rebuild,” “Path‑C native retrain,” “R7”, “P2 §IV penalty” style wording, and in multiple places “Path‑C-final catalog”. These read like internal audit tags / version labels.  
Required fix: Either (a) define Path‑C clearly once and use it sparingly as a named method, or (b) replace it everywhere with neutral scientific descriptions (“our native‑retraining protocol”). Remove any internal‑round or audit code style language that is not necessary to understand the science. Ensure there is no residual version-history phrasing (“final”, “baseline”, “R-round”) in the main text.

P3-M6 (MAJOR) – Use of “largest”, “first”, “unprecedented”, multiple locations including abstract and conclusions  
Problem: Strong novelty claims:  
• “largest-scale application of autoencoder anomaly detection across seven astronomical archives”  
• “largest multi-archive anomaly search reported to date”  
are not rigorously justified. There is no systematic survey of all prior multi-survey anomaly catalogs, and [10–12] are single-survey. Other work (e.g., photometric anomaly catalogs, Gaia‑scale searches) may rival the claimed scale.  
Required fix: Either provide explicit bibliographic justification that no larger multi-survey anomaly catalog exists as of submission (with at least a brief comparative discussion of other large anomaly programs), or soften to “to our knowledge” and restrict the claim to better-defined scope (e.g., “largest autoencoder-based spectroscopic anomaly catalog across these specific seven archives”).

P3-M7 (MAJOR) – Ambiguous use of thresholds and comparability across surveys, abstract and Table I  
Problem: The abstract and main text present σ, anomaly rates, and counts side‑by‑side across surveys without sufficiently emphasizing at *each juxtaposition* that the thresholds differ (S>5, top‑1%, S>0.259, etc.), which makes rates not directly comparable. The instructions you provided include a strict requirement to flag when σ values from different null procedures are juxtaposed without explicit “not directly comparable” disclaimers.  
Required fix: Wherever anomaly fractions or σ(fNL) improvements from different thresholds/surveys are placed side by side (e.g. in abstract, Table I caption, §III and §V), add explicit language that these rates/sigma values are not directly comparable because thresholds and scoring procedures differ.

P3-M8 (MAJOR) – Cosmology application scope vs. method paper scope, Section V, pages 10–12  
Problem: The cosmological applications (multi-tracer fNL forecasts, NANOGrav bounce consistency) are quite extensive, including a dedicated MCMC analysis, Bayes factors, and detailed Fisher forecasts. This is heavy for what is primarily a methods/data‑catalog paper and risks overclaiming given the limited completeness and systematics control of the anomaly sample.  
Required fix: Either (a) trim this section substantially, focusing on high-level illustrative potential and moving most detailed forecasts and Bayes-factor results to an external cosmology‑focused paper, or (b) expand the systematics treatment (selection functions, completeness, bias modeling) to PRD standards if a serious cosmology claim is to be made here. Presently it sits in an awkward middle ground for PRD.

P3-N1 (MINOR) – Internal duplication of words, e.g. “reproducibility scripts shipped ... reproducibility scripts shipped”, page 2  
Problem: Exact duplicate phrase within a single sentence indicates careless editing.  
Required fix: Remove the duplicated phrase and rephrase once.

P3-N2 (MINOR) – Unlabeled “Fig. ??” placeholders, e.g. pages 2–3, 5, 13, 17  
Problem: Multiple instances of “Fig. ??” remain in the text, indicating missing or mislinked figure references. PRD will not accept this.  
Required fix: Assign consistent figure numbers to all figures, verify that all “Fig. ??” are replaced by correct references, and that the numbering matches the actual list of figures.

P3-N3 (MINOR) – Equation labeling and dimensional clarity, Equation (2), page 2  
Problem: The canonical anomaly score S(x) in Eq. (2) is dimensionless by construction, but the text also discusses MSE thresholds in physical units; the mapping from raw MSE to S is defined only for DESI (“σval is set such that S>5 corresponds to MSE≈0.143”), not for other surveys.  
Required fix: Clarify that S is always dimensionless and that σval is computed directly from the validation distribution for each survey (not “set”). Replace “σval is set such that ... corresponds to MSE≈0.143” with a description of the actual empirical σval. Provide an explicit example for one other survey or state that the analogous mapping is used but not shown.

P3-N4 (MINOR) – Abstract vs. body consistency on novelty fraction, pages 1 and 9  
Problem: The abstract advertises “genuine novelty fraction of ∼17.8% ... (single-sample point estimate at the top‑1,000 score stratum; full-catalog rate empirically untested).” The body later repeats this but adds more nuance about SIMBAD vs. NED+VizieR. There is a non‑negligible risk that readers will mistake 17.8% as a global catalog-wide novelty rate.  
Required fix: In the abstract, add explicit language that 17.8% refers only to the top‑1,000 DESI anomalies and *not* the full catalog, and that this is a lower-dimensional demonstration rather than a global estimate.

P3-N5 (MINOR) – Appendix labels and consistency, pages 16–18  
Problem: Appendix C and D discuss Fisher forecasts and taxonomy images, but the references in the main text to these appendices must be checked for consistency (letter and title). Any mismatch between “Appendix C: Sensitivity to Bias Enhancement” in the appendix and “Appendix C” in the body should be avoided.  
Required fix: Verify all cross‑references to appendices (letters and titles) and make them consistent.

P3-N6 (MINOR) – Use of colloquial phrases in a PRD context, various pages  
Problem: Phrases like “headline finding”, “this provides the single most important methodological lesson”, “not a science result”, “gold and silver subset” are somewhat informal for PRD style and can obscure the precise scientific content.  
Required fix: Replace with more neutral, standard phrasing (e.g., “key result”, “most significant methodological implication”, “diagnostic only, not used in quantitative conclusions”, “high‑confidence and medium‑confidence subsets”).

P3-N7 (MINOR) – Units and symbols, page 4 and elsewhere  
Problem: Wavelength ranges are given as “3600–6200 Å” etc.; PRD usually prefers consistent LaTeX formatting (\( \mathrm{\AA} \)). Similarly, some redshifts and σ-values appear without consistent spacing or uncertainty notation.  
Required fix: Standardize units (e.g., use Å consistently via LaTeX macros), and ensure all uncertainties are in the form “x ± y (1σ)” with clear indication of confidence level.

P3-N8 (MINOR) – Overlong manuscript relative to core contribution  
Problem: For a methods/data‑catalog paper, 20 pages of dense text plus multiple long appendices and extensive cosmology forecasts is more than needed to establish the core contribution.  
Required fix: Tighten the text by removing redundant explanations of the same protocol (e.g., Path‑C steps, injection‑recovery described in both §II D and §VI D) and condensing cosmology Section V into a shorter illustrative subsection. A target length of 14–16 pages of main text (excluding appendices and references) would be more appropriate.

P3-N9 (MINOR) – Typos and grammar, scattered  
Problem: There are scattered minor typos (e.g., “autoen coder”, extra spaces, occasional subject–verb mismatches).  
Required fix: Run a careful language pass or professional copy‑edit to correct all typographical and minor grammatical errors.

P3-N10 (NIT) – Styling of references, pages 19–20  
Problem: Some references include explanatory notes in square brackets within the bibliography (e.g.,  with “[publication-year 2024; bibkey label retained as Heinrich2023 ...]”). This is unusual for PRD style.  
Required fix: Move such explanatory notes into footnotes or the main text; keep the reference list itself in standard PRD format.

## Summary recommendation

REJECT

The data set and anomaly-detection pipeline are potentially interesting, but the citation metadata and external-statistics usage are not yet at PRD standards: several key references appear mis-specified or unverifiable, external numbers are imported without fully transparent traceability, internal counts and “largest/×‑factor” claims require more careful justification, and the cosmology applications are overextended for a catalog/methods paper. A thorough overhaul of the bibliography, external-statistics auditing, and manuscript structure is needed before this work could be reconsidered for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P3-E12 (ESSENTIAL) – Arithmetic and internal consistency of reported fractions and σ-values (Sections III, IV, V, VI, Table I, abstract)  
Problem: Several quoted percentages, σ-values, and improvements do not match the numbers implied by the text, or mix incompatible approximations.  
New issues include:  
• DESI anomaly rate: 195,829/22,504,897 = 0.8700%, consistent with “0.87%”; OK.  
• SDSS cross-transfer rate: 77,905/2,304,830 = 3.38%; OK. DESI-vs-SDSS “3.9 times higher” rate: 3.38/0.87 ≈ 3.89; OK.  
• LAMOST cross-transfer rate: 44,075/11,418,594 = 0.386%; OK.  
• NEOWISE polar-cap excess: uniform-sphere expectation quoted as 1.52%, observed 17/436 = 3.899%; ratio 3.899/1.52 ≈ 2.57, matching “2.6×”; OK.  
• SIMBAD-unmatched aggregate: the text states 58.8% as the “aggregate SIMBAD-unmatched fraction” and repeats 58.8% in Fig. 5 label, but the underlying per-survey anomaly counts and fractions are never shown in a way that allows a reader to recompute 58.8%; this aggregate cannot be independently verified and appears to be a derived number that must be documented (e.g., weighted over anomalies) to be auditable.  
• Deduplication: Path-C per-survey native counts sum is given explicitly: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493, and 388,493 − 10,213 = 378,280 unique; this checks. The decomposition 637 multi-survey clusters + 9,576 intra-survey duplicates = 10,213 also checks; OK.  
• Fractional compression: 10,213/388,493 = 2.629%; this matches the stated “2.629% compression”; OK.  
• Jaccard stability: 399/546 = 73.1% (text: 73%); OK.  
• Cross-match Δ counts: DESI×SDSS expected random coincidences “∼ 2.3” at 3″ is not explicitly derived; since the text gives neither surface densities nor the exact search area, the number is not independently checkable. This is a minor issue but should be supported with the explicit nsource values somewhere.  
• fNL Fisher “7.9% improvement”: the text defines the standard DESI-only baseline as σ(fNL)std = 8.98 and gives the anomaly-enhanced central forecast σ(fNL) = 8.14 with an “envelope [3.92, 8.98].” The fractional improvement should be computed relative to 8.98: (8.98 − 8.14)/8.98 ≈ 0.0936 (9.4%), not 7.9%. The 7.9% appears to be a stale number from an earlier forecast (e.g., σ ≈ 8.27) that was not updated when σ(fNL) was changed to 8.14.  
• Fisher “6.1% improvement” for α = 0.15 (Appendix C / Table VII): Table VII says σ(fNL)std = 8.98 and σ(fNL) = 8.43 at α = 0.15, giving (8.98 − 8.43)/8.98 ≈ 6.1%, consistent internally. But this “6.1% at α = 0.15” is later contrasted with the empirical αjk result, without ever reconciling that the empirical 8.14 forecast implies ~9.4% improvement, not 7.9%. There is thus an internal inconsistency among the three quoted improvement percentages (6.1%, 7.9%, 9.4% implied).  
• Bounce NANOGrav σ-separations: “γ = 2.567 ± 0.382; the matter-bounce prediction γ = 3.0 sits at +1.13σ” – if 2.567 is a mean and 0.382 is a 1σ standard deviation, then (3.0 − 2.567)/0.382 ≈ 1.13; OK. “SMBHB γ = 4.33 at +4.61σ”: (4.33 − 2.567)/0.382 ≈ 4.61; OK.  
Required fix:  
– Recompute all improvements and fractions explicitly and harmonize the text: state clearly that the empirical αjk forecast implies ~9.4% improvement (or adjust σ(fNL) if that is the stale quantity), and ensure the 7.9% number is either removed or updated.  
– Make the computation of the 58.8% aggregate SIMBAD-unmatched fraction explicit (e.g., as a weighted sum over anomalies per survey, with the counts), so readers can reproduce it.  
– For cross-match “expected random coincidence” counts (e.g., DESI×SDSS “∼ 2.3”), either provide the underlying catalog surface densities and area so the numbers can be checked, or move such expected-count numbers to an appendix with derivations.  

P3-E13 (ESSENTIAL) – Figure–text inconsistencies: anomaly-score units and scales (Fig. 2 and surrounding text)  
Problem: Figure 2 (SDSS anomaly score distribution) and the surrounding text use SDSS scores spanning “twelve orders of magnitude” up to S = 1.9×10^11 for cross-transfer, but elsewhere the canonical S is defined as a per-survey z-score S = (MSE − μval)/σval that is dimensionless and expected to be O(1–10) for realistic tails.  
Specific issues:  
• Eq. (2) defines S(x) as a z-scored residual based on μval and σval per survey; for DESI that produces scores in [5, 25.2].  
• In Fig. 2, right panel, SDSS cross-transfer scores span from S = 5 up to 1.9×10^11 and the y-axis is labeled “Probability density” on log–log axes, but the text then states “the SDSS native re-score (§III C) compresses the same objects to S < 14, eliminating the 10^4–10^11 tail.” This implies that the cross-transfer S is not actually the same canonical S defined in Eq. (2), or that its μval,σval were wildly pathological.  
• The body later uses SDSS “Path-C native retrain” scores with S ≥ 0.1060 (top-1%) and 12 sources at S > 5, explicitly described as being on “the DESI-trained BigAE score scale (Eq. 2).” This overlaps notation with the cross-transfer scale without clearly distinguishing the two, yet the figure uses the “S” symbol for both.  
Required fix: Clarify in the text and caption of Fig. 2 that the extreme cross-transfer S values (up to 1.9×10^11) are *not* directly comparable to the canonical z-scored S used for native retrains and forecasts, and that the cross-transfer S scale for SDSS is numerically ill-conditioned because μval and σval were computed on a DESI-training distribution. Either:  
(a) relabel the cross-transfer SDSS score axis with a different symbol (e.g., S̃) and explain the relationship to the canonical S, or  
(b) explicitly state that those numbers are on a raw-MSE-rescaled axis that is only used diagnostically and is not used in any quantitative cross-survey comparison.  

P3-E14 (ESSENTIAL) – Equation dimensional consistency for NANOGrav model (Appendix E)  
Problem: Equation (E1) for the PTA energy-density spectrum is written as  
\[
\log_{10}\rho_i = \tfrac{21}{2}\log_{10}A - \log_{10}(12\pi^2) + (\gamma-3)\log_{10}f_{\rm yr} - \gamma\log_{10}f_i - \log_{10}T_{\rm obs}.
\]  
• The notation ρi is never given explicit units (strain spectral density, energy density, etc.).  
• fi is defined as (i+1)/Tobs with Tobs in years, and fyr is a reference frequency “fyr” whose units are not defined. As written, log10 fi and log10 fyr are being combined; to be dimensionally consistent, fi/fyr must be dimensionless.  
• The formula as written suggests log10(fyr) and log10(fi) are taken directly, which is incomplete; the standard PTA practice uses log10(fi/fyr). Likewise, Tobs must be in units consistent with fi for the final expression to be dimensionless.  
Required fix: Explicitly define:  
– what ρi represents and its units;  
– that fi and fyr are used only in the ratio fi/fyr (so that the argument of any logarithm is dimensionless);  
– that Tobs is expressed in seconds or years consistently, and that the combination of factors yields a dimensionless log10 ρi.  
Rewrite Eq. (E1) in a visibly dimensionally consistent form, e.g.  
\[
\log_{10}\rho_i = \tfrac{21}{2}\log_{10}A - \log_{10}(12\pi^2) - 3\log_{10}f_{\rm yr} + (\gamma-3)\log_{10}\frac{f_i}{f_{\rm yr}} - \log_{10}T_{\rm obs},
\]  
and state the unit conventions explicitly.  

P3-E15 (ESSENTIAL) – Incomplete description and internal consistency of DESI injection-recovery arithmetic (Fig. 7 and text)  
Problem: Fig. 7 shows multiple recovery curves, but the body text only summarizes “3 PASS” and “3 FAIL-with-diagnostic.” For some surveys, the exact numerical recovery at 5σ is given; for others (Planck, NEOWISE) the axes in Fig. 7 imply 100% but the main text uses a different injection configuration (Gaussian bumps vs mask injection) without clearly aligning numerical values. This creates arithmetic and interpretational ambiguity:  
• For SDSS, LAMOST, Gaia, eROSITA, numerical values at 5σ are given explicitly.  
• For Planck and NEOWISE, the text gives 100% recovery at 5σ, but Fig. 7 re-plots them together with other surveys and the legend mixes morphologies (“Gaussian-bump”, “mask”) without giving the exact 5σ points in the main text.  
• The caption notes “paired emission-line variants” for SDSS and LAMOST but the abstract only quotes the continuum-dip numbers; readers cannot reconstruct from the main text alone which curve corresponds to which numerical gate value.  
Required fix: In §II D and §VI D, tabulate explicitly, in a single table, the 5σ recovery fraction for each survey and each injection morphology used (continuum-dip, emission-line, Gaussian-bump, mask), and ensure the abstract only quotes numbers that appear in that table. Align Fig. 7’s labels with the table (e.g., same colors and line styles) so that every percentage value used in the narrative can be visually and numerically checked.  

P3-M9 (MAJOR) – Abstract vs. body mismatch on “largest” and multiplicative factors after path-C vs cross-transfer distinction  
Problem: The abstract and conclusions repeat the claims:  
• “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase.”  
The body, however, never explicitly shows the Liang et al.  sample size or anomaly count in a way that allows reconstruction of 141× and 73×. The earlier review already flagged the need to quote Liang’s numbers; the new issue is that the *definition* of the comparison set is now ambiguous given the path-C pipeline:  
• The text emphasizes that LAMOST’s main released tier (113,342 anomalies) is an “exploratory” layer with a 98% training-bias artifact. Including this tier in the 141× factor implicitly weights a non–catalog-grade layer equally with the DESI+SDSS+eROSITA+Gaia+NEOWISE “recommended catalog-grade subset ∼ 265,000 unique objects.”  
• If the “recommended catalog-grade subset” rather than the full 378,080 point-source tier is used as the main science product, the multiplicative factor relative to Liang et al. should be recomputed accordingly; otherwise the 141× number is anchored to a population the body explicitly labels as non-catalog-grade.  
Required fix:  
– Explicitly quote Liang et al.’s anomaly count (and survey size) in §VI E and show the calculation that yields 141× and 73×.  
– Decide which population you intend to compare to : the full 378,080 point-source tier (including LAMOST exploratory anomalies) or the ∼265,000 “recommended catalog-grade subset.” Use that definition consistently in both the abstract and the conclusions, and recompute the multiplicative factors accordingly. If you insist on using the full tier while warning that part of it is methodologically contaminated, add an explicit caveat that the “141×” factor includes an exploratory LAMOST component heavily affected by training bias.  

P3-M10 (MAJOR) – Abstract claims vs. body support for “largest-scale application” and multi-archive scope  
Problem: The abstract states:  
• “We present the largest-scale application of autoencoder anomaly detection across seven astronomical archives…”  
• “The total represents the largest multi-archive anomaly search reported to date.”  
The body provides detailed per-survey counts and references [10–12] for SDSS and DESI single-survey anomaly work, but does not actually provide any quantitative comparison against other large-scale anomaly efforts beyond those three papers. Nothing in §VI E or elsewhere systematically surveys the literature on multi-archive or multi-survey anomaly catalogs (e.g., photometric surveys, Gaia-scale or LSST-precursor anomaly searches).  
Required fix: Either:  
(a) add a short subsection in §VI E explicitly comparing your scale (37.3M sources, 378k anomalies across seven archives) to other large anomaly programs (with numbers from the literature) and explain why no larger multi-archive autoencoder-based anomaly search exists as of submission; or  
(b) soften the claims to “to our knowledge, this is the largest autoencoder-based spectroscopic anomaly catalog across these specific seven archives,” and avoid phrasing that implies an exhaustive search over all possible anomaly pipelines and data types.  

P3-M11 (MAJOR) – Non-comparable σ and “improvement” values reused across different Fisher setups (Section V, Appendix C, D)  
Problem: The paper now uses *three* different σ(fNL) contexts:  
1. A DESI-only baseline σ(fNL)std = 8.98 (single-tracer);  
2. A DESI + anomaly-tracer Fisher forecast using the “positivity-respecting form” 1/σ^2 = F0 + cα^2 with F0 = 1/8.982, c = 0.0747, and empirical αjk;  
3. A more complex 5-tracer SPHEREx-like Fisher configuration in Appendix C and Fig. 8 (with σ ranges 11.71–16.85 etc.).  
The text occasionally juxtaposes improvement percentages from different configurations without clearly labeling which σ refers to which model:  
• §V first uses σ(fNL)std = 8.98 (DESI single-tracer) for the anomaly-tracer improvement, then §VI F and Appendix C discuss multi-tracer SPHEREx forecasts with very different baselines (σ ≈ 11.7–16.8), and Fig. 8 refers to a “baseline multi-tracer=12.72, single-tracer baseline=16.85.”  
• The improvement percentages are not always tied to their underlying σ. For instance, “The projected SPHEREx multi-tracer forecast yields 3–5σ detection significance for the matter-bounce fNL = −35/8 prediction” is presented immediately after a DESI-only Fisher discussion, without a clear partition between the two forecast regimes.  
Required fix: In §V and Appendix C/D, clearly segment the different Fisher setups and always identify which σ(fNL) and which “improvement” percentage belong to which configuration (DESI-only, DESI+anomaly, SPHEREx multi-tracer). Avoid reusing symbols (σstd, σmulti) without redefinition when switching contexts, and ensure that no improvement percentage is quoted without its specific baseline and experiment.  

P3-M12 (MAJOR) – Abstract faithfulness: cross-transfer vs. native scores for SDSS and LAMOST  
Problem: The abstract summarizes the sample size and some rate-compression factors but does not clearly distinguish, at the *first mention*, which SDSS and LAMOST numbers are cross-transfer diagnostics and which are path-C native results:  
• The abstract says: “A Path-C rebuild protocol resolves cross-transfer artifacts: 21.5× LAMOST rate compression and ∼6500× SDSS rate compression after native retraining; DESI 5-fold Jaccard stability …” but never actually quotes the *native* SDSS anomaly count (12 objects at S>5) in the abstract.  
• For a reader who only scans the abstract and Table I, it is easy to confuse the cross-transfer SDSS 77,905 anomalies and LAMOST 44,075 anomalies with “catalog-grade” objects, even though the body repeatedly insists those are baseline diagnostics.  
Required fix: In the abstract, explicitly name the *native* SDSS and LAMOST anomaly counts at the canonical S>5 threshold (12 and 2,054, respectively) alongside the compression factors, and add one sentence making clear that 77,905 (SDSS) and 44,075 (LAMOST) are cross-transfer diagnostics, not catalog-grade native results. This ensures the abstract cannot be misread as implying that 77,905 SDSS cross-transfer anomalies are part of the main catalog.  

P3-M13 (MAJOR) – Null-procedure comparability gaps beyond those already flagged (σ(fNL), σ values across surveys, and GR corrections)  
Problem: There remain several places where σ values from different null procedures are juxtaposed without fully explicit caveats, beyond those already identified:  
• The abstract now partly qualifies the fNL improvement (“consistent with no improvement at < 1σ”), but the later conclusions (§VII, item 5) repeat “Fisher-positivity-corrected σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement)” without again reminding the reader that this forecast is based on an idealized Fisher with zero observational systematics and an empirically noisy αjk.  
• In §V and §VI D, the GR projection corrections are summarized as “|Δσ/σ| < 0.02%” but there is no explicit equation showing how this was computed from [38–41]; it is difficult to judge how comparable this σ is to the primary Fisher σ used for fNL (different modeling approximations, survey geometry, kmax).  
Required fix: Wherever σ values from different approximations/assumptions are placed side-by-side (e.g., 8.14, 8.98, 11.71, 16.85, “|Δσ/σ| < 0.02%”), explicitly state which null procedure and modeling approximations each σ uses, and add a one-line reminder that they are not directly comparable. For GR corrections, either show the equation used from [38–41] (with parameters) or relegate the |Δσ/σ| < 0.02% statement to an appendix with a short derivation.  

P3-N10 (MINOR) – Typos / formatting in equations and units not previously flagged  
New instances:  
• Eq. (2) text: “σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143” still uses “is set” rather than “is computed from the validation distribution”; this was flagged conceptually before, but the exact wording remains misleading in the present text.  
• Several occurrences of “Å” vs “Å” remain mixed (some in plain text, some in LaTeX math) in the main text (e.g., “3600–6200 Å” and “9800 Å”) and in figure labels; this is inconsistent with journal style.  
• A few remaining colloquialisms: “headline finding” appears multiple times in the body (e.g., SDSS, LAMOST, eROSITA, NEOWISE subsections) despite earlier guidance to replace it with more neutral phrasing.  
Required fix:  
– Replace “σval is set” with “σval is computed from the validation MSE distribution” and make the DESI example clearly illustrative.  
– Standardize all Ångström units to a LaTeX form \( \mathrm{\AA} \) throughout.  
– Remove or rephrase remaining “headline finding” and similar colloquialisms to neutral, PRD-style language (“key result,” “main outcome”).  

If you address these new issues together with the ones from your initial review, the manuscript’s arithmetic, internal consistency, and abstract–body alignment will be substantially closer to PRD’s expectations for rigor.