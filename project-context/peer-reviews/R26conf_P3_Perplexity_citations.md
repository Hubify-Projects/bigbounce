# P3 R26conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.84.pdf` md5=2539e13c pages=25
**Input format**: TEXT + web search + pass-2 self-critique (12343 chars)
**Wall time**: 98.6s

---

The paper’s references and in‑text citation usage do not meet Physical Review D standards in their current form. Several key citations are incorrect or incomplete, there are internal inconsistencies in quoted results and statistics, and the bibliography is not at PRD level. Below I list all findings I can identify from the provided text, organized as requested.

Because I only see the manuscript text (not the rendered PDF), I refer to locations by section and the nearest unique phrase rather than an absolute page number. For PRD, all of these would need to be checked against the actual typeset pages.

---

### ESSENTIAL FINDINGS

**P3‑E1 – Incorrect or misleading citation for Liang et al. (DESI anomaly catalog size benchmark)**  
- **Location:** Abstract (“largest published single‑survey anomaly catalog ; §VI”), §I (“Liang et al.  applied a normalizing‑flow autoencoder to ∼ 250,000 DESI EDR spectra, finding 2,685 anomalies (1.07%).”), §VI E, references .  
- **Problem:**  
  - The manuscript uses  as *the* size benchmark “largest published single‑survey anomaly catalog.” In the reference list,  is: “Y. Liang et al., ‘Outlier detection in the DESI Bright Galaxy Survey,’ Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664.” This BGS paper indeed studies DESI, but the abstract of Liang et al. focuses on BGS galaxies and does not obviously state the 2,685 / 1.07% numbers as quoted here; the paper you *describe* (normalizing‑flow autoencoder on ∼250k DESI *EDR* spectra) is more closely matched by other anomaly‑detection work, and may be a different Liang et al. paper or an earlier arXiv version.[1]  
  - The text claims “∼ 250,000 DESI EDR spectra, finding 2,685 anomalies (1.07%)”. I cannot confirm those exact numbers from the cited BGS paper’s abstract or tables based on search alone; they look like they may refer to a specific experiment in that paper, or to a different paper.  
  - Calling  “the largest published single‑survey anomaly catalog” also appears doubtful: there are more recent large‑scale anomaly lists and catalogs from, e.g., LSST precursor surveys and other machine‑learning anomaly searches; if you want to make this claim, it must be supported by a systematic literature check and clearly time‑bounded (e.g., “as of early 2025”).  
- **Required fix:**  
  - Verify precisely which Liang et al. paper you mean, and correct the citation metadata (title, journal, year, arXiv ID). If the numbers 2,685 anomalies / 1.07% are taken from a specific table or section, cite that precisely and ensure they are accurate.  
  - Either (i) provide a defensible argument, with citations, that  is indeed the largest single‑survey anomaly catalog to date (e.g., by comparing counts and dates with other anomaly‑detection surveys) or (ii) weaken the claim to something supported, such as “representative previous large‑scale single‑survey anomaly catalog” or “one of the largest published single‑survey catalogs.”  
  - Make sure the EDR vs BGS scope in your prose matches the actual scope in the cited paper.

---

**P3‑E2 – Nicolaou et al.  metadata and arXiv status**  
- **Location:** §I (“Nicolaou et al.  extended this with the Astronomaly active‑learning framework on 208,000 EDR spectra.”), references .  
- **Problem:**  
  - Reference  is given as: “C. Nicolaou et al., ‘Identifying Anomalous DESI Galaxy Spectra with a Variational Autoencoder,’ arXiv:2506.17376 (2025).” I can find an arXiv preprint with that identifier and approximate title, but the current arXiv metadata lists a slightly different title and possibly different wording around “Astronomaly”; the manuscript text states “extended this with the Astronomaly active‑learning framework on 208,000 EDR spectra”, which may be a conflation of two works (one on Astronomaly, one on VAEs) or may not exactly match the abstracted contribution.  
- **Required fix:**  
  - Check arXiv:2506.17376 directly and ensure you reproduce the exact title, author list and year from arXiv, and make sure that the description in the introduction (sample size, method, and survey used) matches what Nicolaou et al. actually report in their abstract and main text.  
  - If the Astronomaly work is a separate paper (for example a Nicolaou et al. application using Astronomaly on DESI EDR), cite *both* papers separately with accurate metadata and clearly distinguish them: one for Astronomaly+active learning, one for VAE.

---

**P3‑E3 – Cai/Wands/Wilson‑Ewing bounce references [13,14,35] not matching described claim**  
- **Location:** §I: “Second, the quasi‑matter bounce model predicts fNL = −35/8 = −4.375 [13, 14, 35]”. References [13–15, 35].  
- **Problem:**  
  -  is listed as “D. Wands, ‘Local non‑Gaussianity from inflation,’ Class. Quant. Grav. 27, 124002 (2010).” This is an inflation review, not a matter‑bounce paper and does not itself present the fNL = −35/8 prediction.  
  -  is listed as “Y.-F. Cai et al., ‘Non‑Gaussianity in a matter bounce,’ JCAP 0905, 011 (2009), arXiv:0903.0631.” That is indeed a matter‑bounce non‑Gaussianity paper and is an appropriate source for the fNL prediction.[2]  
  -  is “E. Wilson‑Ewing, ‘The Matter Bounce Scenario in Loop Quantum Cosmology,’ JCAP 1303, 026 (2013), arXiv:1211.6269.” This discusses matter bounce scenarios but the specific value fNL = −35/8 is not the main focus; you need to check that the claimed number actually appears or is derived there.  
  - Thus at least one of the three references () does not support the precise quantitative claim “predicts fNL = −35/8”.  
- **Required fix:**  
  - Restrict the “predicts fNL = −35/8” claim to the papers that actually compute that number (likely Cai et al. 2009 and slightly later detailed bounce calculations). Remove  from this specific bracket or clarify its role (e.g., “for a review of local non‑Gaussianity in general see ”).  
  - Explicitly indicate where in  and/or  the numerical prediction is taken from (section or equation) and check that the value and its sign agree with the original derivation.  
  - If additional bounce references are needed (e.g., Quintin/Cai/Brandenberger 2014), add them with correct metadata and arXiv IDs.

---

**P3‑E4 – SPHEREx primordial non‑Gaussianity forecast mis‑cited and mis‑quoted**  
- **Location:** §I: “testable at 3–5σ with SPHEREx  under the multi‑tracer methodology of Heinrich et al.  (σ(fNL) ≈ 0.7 bispectrum‑only forecast).” References , .  
- **Problem:**  
  -  is the SPHEREx overview “Cosmology with the SPHEREx All‑Sky Spectral Survey,” arXiv:1412.4872. That paper gives multiple forecasts; the quoted σ(fNL) ≈ 0.7 “bispectrum‑only” would need to be traceable to a specific table or figure. Heinrich et al.  is a separate later paper on SPHEREx multitracer redshift‑space bispectrum forecasting.  
  - The text as written conflates: (a) the original SPHEREx mission paper, and (b) the more recent Heinrich et al. forecasting paper. It attributes “σ(fNL) ≈ 0.7 bispectrum‑only forecast” collectively to  and/or  without specifying which result is from which paper.  
- **Required fix:**  
  - Check Heinrich et al. (Phys. Rev. D 109, 123511 (2024), arXiv:2311.13082) for their forecast values; they quote specific σ(fNL) for local PNG with realistic SPHEREx‑like survey parameters. Make sure the number 0.7 is actually present, and state clearly which paper it comes from.  
  - If 0.7 is from Heinrich et al. and not from the original Dore et al. SPHEREx overview, adjust the citation accordingly: e.g., “following Heinrich et al. , who forecast σ(fNL) ≃ 0.7 for SPHEREx using the multitracer redshift‑space bispectrum.”  
  - Remove any implication that 0.7 is a “bispectrum‑only” forecast from  if that exact characterization is not in the SPHEREx overview.

---

**P3‑E5 – NANOGrav 15‑yr KDE “free‑spectrum” product and likelihood description does not match the cited NANOGrav paper**  
- **Location:** Abstract (NANOGrav 15‑yr KDE free‑spectrum MCMC, γ = 2.567 ± 0.382; Bayes factor 7.14×10³), §V A, Appendix E; references , , .  
- **Problem:**  
  -  is “G. Agazie et al. (NANOGrav Collaboration), ‘The NANOGrav 15 yr Data Set: Evidence for a Gravitational‑wave Background,’ ApJ Lett. 951, L8 (2023).” That paper does not itself present a “KDE free‑spectrum likelihood” nor a Zenodo DOI 10.5281/zenodo.8060824 in its main abstract. The free‑spectrum data products and ceffyl likelihood come from separate NANOGrav data‑release artifacts (often documented in companion or data‑release papers).  
  - The manuscript states: “Dataset: NANOGrav 15‑yr HD‑correlated KDE free‑spectrum product (30f_fs{hd}_ceffyl), Zenodo 10.5281/zenodo.8060824 .” That Zenodo DOI is not actually part of Agazie et al. (2023) but of a separate data product.  
  - The Bayes factor B_MB/SMBHB = 7.14×10³ is claimed from a Savage–Dickey computation using that KDE likelihood. There is no citation to a methodological reference (e.g. Lentati et al. 2013 ) explaining the KDE method;  is indeed Lentati et al. on Bayesian PTA analysis, but the connection between that and the specific free‑spectrum KDE product is not spelled out.  
- **Required fix:**  
  - Add a separate, correct reference for the NANOGrav KDE free‑spectrum data product (the Zenodo entry itself or a NANOGrav methods paper that explicitly describes it). Do not attribute the Zenodo DOI or ceffyl‑style product to Agazie et al.  if it is not formally cited there.  
  - In §V A and Appendix E, clearly distinguish between: (i) the main 15‑yr background detection paper , and (ii) the specific KDE free‑spectrum likelihood product you actually use.  
  - Make sure the numerical results (γ = 2.567 ± 0.382; Bayes factors) do not contradict values quoted in NANOGrav’s own analyses of “tilt” or spectral index. If they do differ, you must discuss why (different priors, approximations, or data products) and provide explicit equations and citations supporting your setup.

---

**P3‑E6 – Heinrich et al.  and multi‑tracer Fisher implementation: missing explicit correspondence to their equations**  
- **Location:** §V (“Under the Fisher‑positivity‑respecting asymptotic form 1/σ²(fNL) = F0 + c α²”), Appendix C and figure captions for σ(fNL) vs α, Table VII. References [16,17,33–41].  
- **Problem:**  
  - The multi‑tracer Fisher formalism is attributed to Seljak , Hamaus et al. , and Heinrich et al. . However, the paper gives a very specific parameterization 1/σ²(fNL) = F0 + c α² with fitted numerical constants F0 = 1/8.982 and c = 0.0747, but never shows the explicit mapping from the standard Fisher expressions in [16,17,33] to that reduced parameterization.  
  - For PRD, a claim of “Fisher‑positivity‑respecting form” and the derivation of c must be traceable to explicit equations and approximations. At present, the citation to  is not sufficient to verify that your compressed two‑parameter model is consistent with their full forecast, nor that the 6.1% or 9.4% improvements you quote are not artifacts of normalization.  
- **Required fix:**  
  - Add a short derivation or at least a precise pointer (equation numbers in , , ) showing how your effective F0 and c are obtained from the full Fisher matrix for your specific tracer set and redshift binning.  
  - Make clear that “8.98” and “16.85” are not directly comparable to Heinrich et al.’s absolute σ(fNL), and state their normalization explicitly; otherwise the reader cannot cross‑check your numbers against the cited works.  
  - Where you compare to Heinrich et al., give numeric comparisons that can be verified (e.g., “for a DESI‑like QSO sample with bias b(z) = …, Heinrich et al. find σ(fNL) ≃ X; our single‑tracer baseline 8.98 uses the same conventions but a simplified power‑spectrum model”).

---

**P3‑E7 – Use of “largest‑scale application of autoencoder anomaly detection across multiple astronomical archives” and “largest multi‑archive anomaly search” not convincingly supported by citations**  
- **Location:** Abstract first sentence, §VII Conclusions (“largest multi‑archive anomaly detection campaign to date”), Table I caption “largest multi‑archive anomaly search reported to date.”  
- **Problem:**  
  - These are strong novelty claims (“largest‑scale”, “largest multi‑archive anomaly search”) but the only quantitative comparison given is to . There is no systematic survey or citation of multi‑survey anomaly‑detection efforts (e.g., previous cross‑survey anomaly or outlier catalogs) to justify the “largest” qualifier.  
  - PRD requires that such claims be either demonstrably true or hedged appropriately (e.g., “to our knowledge, based on a literature search as of early 2026”).  
- **Required fix:**  
  - Either provide a brief literature review demonstrating that no prior work has produced a multi‑survey anomaly catalog with more than ~10⁵ sources, with explicit references, or weaken the claim everywhere it appears to something like “a large‑scale application” or “among the largest multi‑archive anomaly searches so far”.  
  - The abstract should not state “largest‑scale” as a hard fact unless you can defend it rigorously.

---

**P3‑E8 – Internal inconsistency in “genuine novelty fraction” vs SIMBAD fractions; missing explicit reference support**  
- **Location:** Abstract (“genuine novelty fraction of ∼17.8% (Wilson 68% CI ±1.2%)”), §IV A (novelty assessment), Fig. 6 caption.  
- **Problem:**  
  - The 17.8% novelty fraction is claimed as “genuine novelty fraction … against 20 curated all‑sky catalogs via CDS X‑Match.” No actual list of the 20 catalogs is given in the references; some are named in text (Gaia, SDSS, DESI Legacy Imaging, DES, Pan‑STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO‑B, UCAC5, APASS), but not all 20 are tied to specific references.  
  - SIMBAD cross‑matches are referenced to  (Wenger et al.), but the deeper VizieR/NED cross‑matches that underpin the 17.8% figure have no explicit references.  
  - The paper asserts that random false‑match rates are negligible at 5″ given a SIMBAD surface density n ≈ 3×10⁻⁵ arcsec⁻², but this is not tied to an external source; PRD level requires an explicit citation or a clearly self‑contained derivation.  
- **Required fix:**  
  - Add references for the main “curated all‑sky catalogs” used in the CDS X‑Match (e.g., Gaia DR3 [5], AllWISE, 2MASS, Pan‑STARRS1) so that the 20‑catalog baseline is well‑defined and reproducible.  
  - Provide enough quantitative detail in the text or an appendix so that a reader can reproduce the 17.8% result: number of matches in each catalog, matching radius, and handling of multiple matches.  
  - Clarify that 17.8% is derived from *only* the DESI top‑1000 subset and explicitly state that this is a single‑sample estimate not guaranteed to generalize to the full catalog.

---

### MAJOR FINDINGS

**P3‑M1 – Incomplete or non‑standard bibliographic metadata for several references**  
- **Location:** References [1–9], [18–22], etc.  
- **Problem:**  
  - Many references omit arXiv IDs where these are standard in cosmology (e.g., DESI DR1 documentation [1], LAMOST DR10 [2], SDSS DR18 [3], Planck 2018 results [7,8], ACT DR6 , NANOGrav [18,28], EPTA , PPTA ).  
  - Reference [1] (“DESI Collaboration, ‘The DESI Data Release 1,’ 2025, DESI DR1 documentation.”) is not in a standard journal/proceedings format; you should either cite the official DESI DR1 paper (if published by 2025–2026) with journal and arXiv, or clearly mark it as an internal documentation with URL/DOI.  
  - Reference [6] (“A. Mainzer et al., ‘NEOWISE Reactivation Mission Year Ten,’ Planetary Science Journal, 2024.”) lacks volume and page/article number and arXiv ID.  
  - Several references (e.g., [4] eROSITA,  Sesana et al. 2016,  Burke‑Spolaor et al. 2019) are missing arXiv identifiers, which are standard for PRD‑level cosmology papers.  
- **Required fix:**  
  - For every reference, supply full journal metadata (journal name, volume, page or article number, year) and arXiv ID where available. Use the style consistent with PRD (Phys. Rev. D formatting).  
  - For data‑release “documentation” items such as DESI DR1 and LAMOST DR10, either cite the official data‑release journal or arXiv paper, or clearly specify that this is a technical report / documentation with a stable URL.  
  - Ensure that every survey used (DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, ACT, NEOWISE) has at least one canonical reference with correct metadata.

---

**P3‑M2 – Future‑dated or unverified arXiv IDs and years**  
- **Location:** References [4], [6], , , possibly others labeled 2024/2025 with specific arXiv numbers.  
- **Problem:**  
  - You give some references as 2024–2025 publications and sometimes assign arXiv IDs and journal data that may correspond to preprints not yet accepted in a specific journal. As of mid‑2026, you **can** cite arXiv:2307.07664 and similar, but you must not misrepresent the journal status (e.g., “Mon. Not. Roy. Astron. Soc. 525, 1078 (2023)” is fine if the paper is indeed published there; for eROSITA DR1 [4] and NEOWISE missions you need to confirm the exact volume and page as of your submission date).  
- **Required fix:**  
  - For each 2023–2025 reference, verify on arXiv and ADS that the journal, volume, and year match the latest published status, and correct any mismatches.  
  - If a paper is only on arXiv and not yet in a journal, cite it as an arXiv preprint (arXiv:xxxx.xxxxx) without inventing a future journal citation.

---

**P3‑M3 – Planck and ACT references incomplete for CMB autoencoder discussion**  
- **Location:** §III F, Appendix F; references [7–9].  
- **Problem:**  
  - You use Planck 2018 results [7,8] and ACT DR6  as data sources for CMB patches. However, there is no explicit reference to the specific Planck SMICA map product (e.g., Planck 2018 component‑separated CMB map paper) or to ACT DR6 data‑release documentation beyond one Qu et al. 2024 lensing paper.  
  - For reproducibility, PRD will expect explicit references for the exact CMB maps and masks used.  
- **Required fix:**  
  - Add a reference specifically for the Planck SMICA 2018 component‑separated maps (part of [7,8] or the Planck component separation paper) and, if applicable, for the ACT DR6 CMB maps and data release (beyond the lensing‑power‑spectrum paper).  
  - Explicitly state in the methods which data‑release versions and map products you use, with corresponding references.

---

**P3‑M4 – Unsupported or under‑cited methodological claims**  
- **Location:** §II A–B, §III (taxonomies with UMAP/HDBSCAN), §IV B (GR projection corrections), multi‑tracer systematics discussion with GR terms; references [31–41].  
- **Problem:**  
  - You use UMAP and HDBSCAN extensively. They are cited (, ), which is good, but some algorithmic behavior claims (e.g., trustworthiness thresholds, expected failure of cross‑seed Spearman stability for “sparse high‑dimensional outlier clouds”) have no external references to back them and are not obviously derivable from first principles.  
  - Your GR projection‑effect estimate (“|Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹”) cites [38–41] but does not show enough detail to verify that your number is consistent with those papers’ formulas.  
- **Required fix:**  
  - For important algorithmic behavior (e.g. how UMAP trustworthiness is interpreted, how HDBSCAN handles noise points), add explicit references and, ideally, a short formula or argument showing your usage is consistent with the cited methods papers.  
  - Either provide a short derivation or at least a clear citation to an equation in [38–41] that justifies your GR projection “< 0.02%” statement; otherwise tone down this claim to a more qualitative one.

---

### MINOR FINDINGS

**P3‑m1 – Inconsistent naming and referencing of “matter‑bounce” and “bounce cosmology” literature**  
- **Location:** §V, Appendix E (“matter‑bounce prediction γ = 3.0”), [19,20,35].  
- **Problem:**  
  - You refer to “matter‑bounce prediction γ = 3.0 [19,20]” but  and  are not both straightforward derivations of the gravitational‑wave background spectral index; one is “Matter creation in a nonsingular bouncing cosmology,” the other is a review “Exploring bouncing cosmologies with cosmological surveys.” You need to ensure that γ = 3.0 is actually computed in those references or in another one; otherwise the exact value should be attributed to the appropriate paper.  
- **Required fix:**  
  - Check which paper actually derives γ_GW = 3.0 in the specific scenario you use, and cite that paper explicitly alongside [19,20] or instead of them.  

---

**P3‑m2 – Baron & Poznanski  description vs original title**  
- **Location:** §I: “Baron & Poznanski  demonstrated autoencoder anomaly detection on SDSS spectra, finding unusual white dwarfs and cataclysmic variables.” Reference .  
- **Problem:**  
  -  is “D. Baron and D. Poznanski, ‘The weirdest SDSS galaxies: results from an outlier detection algorithm,’ MNRAS 465, 4530 (2017).” That paper indeed uses anomaly detection and finds unusual galaxies, but your text emphasizes white dwarfs and CVs, which are not the main focus of the galaxy‑oriented paper. That characterization may be partially based on other work by Baron & Poznanski.  
- **Required fix:**  
  - Re‑check  and adjust the description to match the main content (unusual galaxies), or add additional Baron & Poznanski references if you intend to highlight stellar anomalies.

---

**P3‑m3 – “Qu et al. (ACT Collaboration)” metadata**  
- **Location:** reference .  
- **Problem:**  
  - You list “F. J. Qu et al. (ACT Collaboration), ‘The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth,’ Astrophys. J. 962, 112 (2024).” Check that the author order, journal, volume and page match ADS; if Qu is not the first author in the official citation, adjust accordingly.  
- **Required fix:**  
  - Verify via ADS and correct the author formatting to match the collaboration’s standard form (e.g. “ACT Collaboration: F. J. Qu et al.” or similar), and ensure year/volume/page match.

---

**P3‑m4 – Repeated reference to the same work with different emphasis without cross‑linking**  
- **Location:** SPHEREx and Heinrich et al. appear both in §I and §V without cross‑links.  
- **Problem:**  
  - This is not incorrect, but for clarity, PRD prefers consistent naming (e.g., always “Heinrich, Doré & Krause (2024)” rather than sometimes just “Heinrich et al.”) and consistent numeric results when the same forecast is cited in multiple sections.  
- **Required fix:**  
  - Make the SPHEREx forecast numbers and the way you refer to Heinrich et al. consistent across the abstract, introduction, and cosmology section.

---

**P3‑m5 – Some survey references do not point to the canonical data‑release paper**  
- **Location:** references [1–6].  
- **Problem:**  
  - For DESI DR1, SDSS DR18, Gaia DR3, eROSITA DR1, NEOWISE, there are well‑established “data release” papers. Your references sometimes point generically to “documentation” or to survey overviews rather than these canonical data‑release papers. This isn’t fatal, but PRD readers will expect the canonical references.  
- **Required fix:**  
  - Where possible, update [1–6] to cite the official DR1/DR18/DR3 etc. data‑release papers with full metadata and arXiv IDs.

---

### NITS / COSMETIC

**P3‑N1 – Reference ordering and grouping**  
- **Location:** Reference list.  
- **Problem:**  
  - References are essentially grouped by topic but not strictly alphabetical or by order of citation. PRD style usually uses numerical order of first citation, which you mostly follow, but the block  plus  and  for NANOGrav/PTA seems somewhat ad hoc.  
- **Required fix:**  
  - Make sure references are ordered exactly by first appearance in the text and renumber consistently if you move citations around during revision.

---

**P3‑N2 – Slight title mismatch for some references**  
- **Location:** [4], [6], , , etc.  
- **Problem:**  
  - Titles are sometimes abbreviated or paraphrased; for example,  “Outlier detection in the DESI Bright Galaxy Survey” should match exactly the journal title;  “Measuring fNL with the SPHEREx multitracer redshift‑space bispectrum” may have slightly different capitalization in the official record.  
- **Required fix:**  
  - Bring titles into exact agreement with ADS/arXiv, including capitalization as per journal style.

---

**P3‑N3 – Repeated explanations in body vs figure captions**  
- **Location:** Several figures and tables re‑explain the canonical S score, novelty fraction, etc., and re‑state the same references.  
- **Problem:**  
  - This is not wrong, but occasionally verbose; PRD strongly prefers concision.  
- **Required fix:**  
  - Consider trimming repeated full definitions in captions if they are already clearly defined in the main text, leaving only a brief pointer to the earlier definition.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific content is interesting and the methods are potentially impactful, but the citation practice and quantitative cross‑referencing are not yet at PRD standards. Several key external results (Liang et al. anomaly counts, bounce‑model fNL prediction, SPHEREx forecasts, NANOGrav KDE likelihood) are either mis‑cited, insufficiently supported by the referenced papers, or entangle multiple sources without clear attribution. You must systematically verify and correct all references against arXiv/ADS, ensure that every quoted number is traceable to a specific equation, table, or abstract in the cited work, and moderate or justify strong novelty claims. With these corrections and a cleaned‑up bibliography, the paper could reach PRD’s rigor expectations.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E9] **Figure 1 caption and body disagree on the number of “gold-tier” anomalies.**  
- **Location:** Abstract/§I mentions “83 gold-tier anomalies,” while Fig. 1 caption says the 83-object set is a ranked visual-display sample from the companion pipeline and is “distinct from the 116-object GOLD QSO-candidate confidence tier used in the §V Gold+Silver forecast.”  
- **Problem:** The body treats the 83-object set as a visualization sample, but the abstract’s wording makes it sound like a core catalog subset. This is an internal scope inconsistency: one paragraph uses the 83-object set as a descriptive example, while the abstract’s compression can be read as if it were part of the main scientific catalog or selection tier.  
- **Required fix:** Rewrite the abstract sentence so it clearly identifies the 83-object set as a *visualization sample* only, and keep the 116-object Gold tier reserved for the cosmology forecast.  

[P3-E10] **The quoted DESI “0.87%” anomaly rate and the 195,829 count are only internally consistent under the stated denominator, but the paper also describes alternative DESI subsets that can mislead readers.**  
- **Location:** §II B, §III A, Table I, Abstract.  
- **Problem:** The paper reports 195,829 DESI anomalies out of 22,504,897 spectra, which gives \(195{,}829 / 22{,}504{,}897 \approx 0.8700\%\), matching the quoted 0.87%. However, the paper repeatedly mixes that full-catalog denominator with the smaller “validated TARGETTYPE” subset of ~6.5 million spectra, for which the same count would not correspond to 0.87%.  
- **Required fix:** State much more explicitly that the 0.87% rate is computed on the full 22.5M DESI scan, not on the validated-TARGETTYPE subset, and avoid juxtaposing the two denominators without a warning that the rates are not comparable.  

[P3-E11] **The SDSS rate in Table I is arithmetically correct, but the text implicitly compares a fixed-size continuity slice to a true top-1% cut without flagging the mismatch early enough.**  
- **Location:** Table I footnote ♡; §III C.  
- **Problem:** The Table I SDSS line gives 77,905 anomalies out of 2,304,830 spectra, which is \(77{,}905 / 2{,}304{,}830 \approx 3.38\%\), consistent with the table. But the paper later emphasizes that 77,905 is *not* a top-1% selection; the actual top-1% set is 19,253 objects. Readers are likely to misread the headline SDSS count as a percentile cut because Table I lists it alongside genuine top-1% selections for other surveys.  
- **Required fix:** Move the “fixed-size continuity slice” caveat into the table body or the main text before Table I is introduced, so the SDSS row is not mistaken for a percentile-selected sample.  

[P3-E12] **The LAMOST headline rate and count are arithmetically consistent, but the paper’s own narrative mixes three different LAMOST counts.**  
- **Location:** Abstract, §III D, Table I, §VI A.  
- **Problem:** The paper cites 113,342 as the native LAMOST slice, 44,075 as the cross-transfer count, and 2,054 as the S > 5 native-retrained count. Those numbers are internally coherent, but the surrounding prose alternates between them without always making clear which one is the “catalog” count versus the “diagnostic” count versus the “released set.”  
- **Required fix:** Explicitly define in one place which LAMOST number is the headline catalog, which is the before/after diagnostic, and which is the strict-threshold result. Otherwise the same survey appears to have three competing anomaly totals.  

[P3-E13] **The 637 multi-survey clusters and 10,213 total collapsed detections do not fully reconcile with the per-survey totals unless the reader tracks the exclusion/inclusion of ACT very carefully.**  
- **Location:** Table I footnote ∥; §IV C; Appendix F.  
- **Problem:** Table I says the retained-survey native counts sum to 388,493 and, after 10,213 collapsed detections, produce 378,280 unique objects. The footnote also states that excluding ACT subtracts exactly 200 from both the 8-way input sum and the deduplicated total. This is numerically consistent only if one continuously tracks whether ACT is in or out of the sum. The paper’s own wording switches between “7 retained surveys,” “8-way-with-ACT,” and “canonical headline” in a way that makes the arithmetic hard to audit.  
- **Required fix:** Present one canonical arithmetic chain with all included surveys listed explicitly, and a separate sensitivity line for the ACT-inclusive variant. That would make the 378,280 and 378,480 branches easier to verify.  

[P3-E14] **The “2.6×” NEOWISE polar-cap excess is numerically plausible but not derived cleanly from the stated baseline in the prose.**  
- **Location:** §II D step 4, §III H, Table I footnote †, §VI D (ii).  
- **Problem:** The paper says 17 rejected objects in the 10° polar caps correspond to a 2.6× excess over the uniform-null expectation. The table footnote also says 17/436 = 3.9% and a uniform-sphere baseline of 1.52%, which indeed gives \(3.9 / 1.52 \approx 2.57\). But the narrative alternates between 17 rejected objects, 419 retained objects, and 436 raw anomalies without always carrying the same denominator.  
- **Required fix:** Show the arithmetic explicitly in the main text: \(17/436\), \(1.52\%\), and the ratio \(3.9/1.52\). As written, the check is only recoverable by hunting across the caption, footnote, and methods section.  

[P3-E15] **The 58.8% pooled SIMBAD-unmatched fraction and the 17.8% DESI novelty fraction are juxtaposed without enough emphasis that they come from different denominators and different radii.**  
- **Location:** Abstract, §IV A, Fig. 6 caption.  
- **Problem:** The paper reports 58.8% as a pooled unmatched fraction over the top-100 anomalies of four surveys at 3″, while the 17.8% figure is a DESI top-1,000 rate against 20 curated catalogs at 5″. These are not directly comparable, but the text and figure caption place them in the same novelty narrative.  
- **Required fix:** Add an explicit “not directly comparable” sentence wherever the 58.8% and 17.8% figures are mentioned together. Otherwise the reader may incorrectly infer that the pooled fraction is a stricter version of the same measurement.  

[P3-E16] **The paper’s own “largest” claims are vulnerable because the comparison class changes midstream.**  
- **Location:** Abstract first sentence; Table I caption; §VII.  
- **Problem:** The paper claims “largest-scale application,” “largest multi-archive anomaly search,” and “largest prior single-survey catalog” in different places, but the baseline changes between single-survey and multi-archive comparisons, and the comparison target is not always the same kind of object count. The 141× and 73× factors are also computed relative to different baselines.  
- **Required fix:** Use one comparative standard per claim: either largest *single-survey* anomaly catalog, largest *multi-archive* anomaly search, or largest *point-source tier*. Right now the novelty language shifts enough that a skeptical reviewer could treat the claim as overbroad.  

[P3-E17] **The 319,443 cross-transfer baseline and the 378,280 Path-C headline are arithmetically consistent, but the paper does not make the relationship transparent enough.**  
- **Location:** Abstract, Table I, §III.  
- **Problem:** The cross-transfer baseline total is 319,443, while the Path-C native-retrained unique count is 378,280. The difference is 58,837. The paper explains this as a combination of LAMOST native recovery and dedup effects, but it never gives a single compact arithmetic decomposition showing how the total rises from the baseline to the final catalog.  
- **Required fix:** Add a one-line decomposition, e.g. “+LAMOST native retrain, +Planck native retrain, +native SDSS slice adjustment, −dedup compression,” with the actual deltas. That would let the reader verify the headline jump without reconstructing it from multiple sections.  

[P3-M5] **Figure 3’s SDSS dynamic range claim is internally consistent, but the caption and body use different semantic meanings for the same score axis.**  
- **Location:** Fig. 3 caption; §III C.  
- **Problem:** The caption says the SDSS right panel spans “more than ten orders of magnitude” from \(S=5\) to \(S=1.9\times10^{11}\), and the body later says the same tail is a cross-transfer artifact compressed to \(S<14\) after native rescoring. That is fine numerically, but the same letter \(S\) is being used as both a DESI-trained cross-transfer score and a native SDSS score family. The paper warns about this, but the warning comes after the figure has already introduced the notation.  
- **Required fix:** In the figure caption itself, label the SDSS axis as “DESI-trained cross-transfer score \(S_{\mathrm{XT}}\)” and the native rescored axis as \(S_{\mathrm{native}}\). That avoids a notation collision that otherwise looks like a genuine inconsistency.  

[P3-M6] **The Planck injection-recovery “500/500 = 100%” is not comparable to the failed LAMOST/Gaia/eROSITA gates, but the figure groups them as if they were the same test.**  
- **Location:** §III F, §VI D (ii), Fig. 10.  
- **Problem:** The paper is careful in prose that the Planck test uses Gaussian-bump patches and the NEOWISE test is a mask-geometry QA check, yet Fig. 10 places all six curves on the same gate axis. That makes the 100% Planck result and the 5.8% / 5.2% / 1.2% failures look directly comparable, even though the injected signals and success criteria differ materially.  
- **Required fix:** Add a stronger caption note or separate panels for “true sensitivity tests” and “QA-by-construction tests,” because the current grouped display risks overstating comparability.  

[P3-M7] **The Appendix C “linear scaling” statement conflicts with the main-text convex Fisher update.**  
- **Location:** §V b; Appendix C; Fig. 9 caption; Table VII.  
- **Problem:** The main text says the primary forecast uses the Fisher-positivity-respecting form \(1/\sigma^2(f_{\rm NL}) = F_0 + c\alpha^2\), which is nonlinear in \(\alpha\). But Appendix C says the table values are “computed by linear scaling of the fiducial 7-bin Fisher result at \(\alpha=0.15\),” and Fig. 9 caption describes the 6.1% improvement as a reference configuration. Those are not the same procedure. The appendix then reuses the same improvement language as if the two were equivalent.  
- **Required fix:** Separate “reference linear-scaling illustration” from “primary quadratic Fisher model” in the appendix title or table caption. Otherwise the reader cannot tell which reported \(\sigma(f_{\rm NL})\) values are actual recomputations and which are rescaled placeholders.  

[P3-M8] **The NANOGrav posterior summary is internally coherent, but the paper mixes Gaussian and quantile summaries without specifying which uncertainty is being used in each downstream comparison.**  
- **Location:** §V A; Appendix E.  
- **Problem:** The paper gives \(\gamma = 2.567 \pm 0.382\) as a Gaussian approximation and \(\gamma = 2.591^{+0.291}_{-0.287}\) as a quantile summary. It then uses the Gaussian form to quote the +1.13σ comparison to the matter-bounce prediction. That is okay, but it should be stated explicitly that the sigma-shift comparison uses the Gaussian approximation, not the credible-interval half-width.  
- **Required fix:** Add a sentence in the main text: “The quoted σ-shift uses the Gaussian-approximation posterior standard deviation, not the asymmetric 68% credible interval.” Without that, the reader may assume the two summaries are interchangeable.  

[P3-M9] **The quoted “three DESI×SDSS cross-matches” are visually shown as three objects, but one panel is explicitly an internal consistency check, not a scientific match.**  
- **Location:** §IV C; Fig. 8.  
- **Problem:** The text says the three highest-confidence cross-survey detections are the known QSO, TIC 374313355, and the BAL QSO. But Fig. 8 and its caption explicitly state that the known QSO is “an internal consistency check … not a statistically meaningful validation sample.” That means it should not be counted alongside the other two as a scientific discovery match.  
- **Required fix:** Split the discussion into “one validation-only match” and “two scientifically interesting matches.” As written, the paper blurs those categories in the same three-item list.