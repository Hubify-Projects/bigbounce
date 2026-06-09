# P3 auto-2026-06-08_2353pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12716 chars)
**Wall time**: 102.4s

---

P3-E1 (ESSENTIAL)  
Section: Abstract, page 1  
Problem: The abstract claims “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase.” The cited  is Liang et al. 2023, “Outlier detection in the DESI Bright Galaxy Survey,” MNRAS 525, 1078, arXiv:2307.07664. Liang et al. report 2,685 anomalies in DESI EDR out of ~250,000 BGS spectra (1.07%). 195,829 / 2,685 ≈ 72.9, consistent with the ∼73× DESI-only factor, but 378,080 / 2,685 ≈ 141 is only valid if one compares a multi-survey point-source catalog to a single-survey DESI catalog and assumes no larger anomaly catalogs exist in other surveys (e.g., SDSS-wide photometric outlier catalogs). The paper does not justify that Liang et al. is “the largest prior single-survey anomaly catalog,” and no cross-check is provided; this “largest” claim is not supported by the citation.  
Required fix: Either (a) restrict the comparison explicitly to DESI spectroscopic anomaly catalogs and state “largest prior DESI anomaly catalog” or “largest prior DESI spectroscopic anomaly catalog,” or (b) perform and document a systematic literature search (SDSS, Gaia, etc.) showing that Liang et al. indeed represents the largest prior single-survey anomaly catalog and update the citation list accordingly. Without that justification, remove or soften the “largest” claim.

P3-E2 (ESSENTIAL)  
Section: Abstract, page 1; Section IV.A, pages 8–9  
Problem: Abstract states “genuine novelty fraction of ∼ 17.8% … (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested).” In §IV.A the 17.8% comes from cross-matching DESI top-1,000 anomalies to “20 curated all-sky catalogs via CDS X-Match,” including a list with specific surveys (Gaia DR3, SDSS DR12/DR16, DESI Legacy DR9, DES DR2, PS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS). None of these works is cited; the “20 curated all-sky catalogs” procedure and its performance are entirely uncited and thus not externally verifiable. This statistic is heavily load-bearing (discovery fraction) but not linked to any reference or permanent data publication beyond the author’s own “companion data repository,” which is not a PRD-citable archive.  
Required fix: Provide precise citations for each external catalog (e.g., Pan-STARRS1, DES DR2, AllWISE, CatWISE2020, GALEX, Chandra catalogs, 4XMM, NVSS, VLASS, APASS, etc.) using their standard survey references, and specify the exact CDS X-Match configuration (epoch, radii). Alternatively, deposit the cross-match tables in a citable data repository (e.g., CDS/VizieR, Zenodo) and cite that DOI. Without traceable external references, this 17.8% statistic must be clearly labeled as an internal, non-archival result, not a robust discovery fraction.

P3-E3 (ESSENTIAL)  
Section: Abstract, page 1; Section V, pages 11–12  
Problem: Abstract gives “αjk = 0.19 ± 0.65 (< 1σ from null)” and “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] … σ(fNL)std = 8.98 single-tracer baseline,” attributed to “inserting this into the Fisher-positivity-respecting form 1/σ(fNL)² = F0 + c α².” The derivation of F0 and c is not traceable to any cited external work. Heinrich et al. (cited as ) is a SPHEREx multi-tracer bispectrum forecast, but it does not provide this specific 2-parameter quadratic parameterization F0,c for this survey/sample; the paper only states that “5-α refit” was done internally. Thus the quoted σ(fNL) improvement is entirely based on non-reproducible internal Fisher calculations.  
Required fix: Either (a) fully document the Fisher-matrix derivation in the main text or a dedicated appendix, including the exact input power spectra, bias and number densities, k-range, and numerical method, and deposit code or tables in a citable repository, or (b) remove the quantitative σ(fNL) improvement numbers from the abstract and relegate them to a clearly labeled, exploratory forecast with full methodological disclosure. As it stands, the key cosmological σ(fNL) numbers are not grounded in any external reference and are not independently reproducible.

P3-E4 (ESSENTIAL)  
Section: Abstract, page 1; Section V.A / Appendix E, pages 11–12, 16–17  
Problem: The NANOGrav analysis claims “A NANOGrav 15-yr KDE free-spectrum MCMC yields γ = 2.567 ± 0.382; … SMBHB γ = 4.33 at +4.61σ (Savage-Dickey BMB/SMBHB = 7.1×10³).” Reference  is Agazie et al. (NANOGrav 15-yr GW background, ApJL 951 L8, 2023). The paper states use of “KDE free-spectrum likelihood (Zenodo 10.5281/zenodo.8060824)”—this Zenodo record is indeed provided by NANOGrav, but it is not a peer-reviewed paper; the matter-bounce template and the mapping from the NANOGrav posterior to the “Savage-Dickey Bayes factor” are entirely constructed here. No external reference is given for the matter-bounce gravitational-wave spectral index prediction γ = 3.0; , ,  concern matter-bounce cosmology but do not explicitly define a pulsar-timing-band γ in the PTA conventions. The precise prior used on γ is flat in [0,7]; the Bayes factor and σ-shifts are highly prior dependent, but this sensitivity is not discussed or referenced.  
Required fix: Cite a PTA-appropriate reference (if it exists) that derives the predicted PTA-band spectral index γ = 3 for matter-bounce in the same convention used by NANOGrav (or else provide a derivation in an appendix). Explicitly justify the choice of prior on γ and explain its impact on the Savage-Dickey Bayes factor. The Bayes factor BMB/SMBHB = 7.1×10³ must be shown to be stable under reasonable prior variations; otherwise, it should be presented as strongly prior-dependent and not as “decisive” evidence. As written, the cosmological inference claims go beyond what is justified by the cited NANOGrav paper.

P3-E5 (ESSENTIAL)  
Section: Method, Eq. (2), page 2; Section II.B, Section III.A  
Problem: The definition of canonical anomaly score \( S(x) = ( \text{MSE}(x) - \mu_\text{val}) / \sigma_\text{val} \) is internally consistent, but in the DESI DR1 example the text claims: “For DESI DR1, µval ≈ 0.0287 (validation MSE) and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.” For a true z-score, σval is fixed by the validation set, not “set such that” a threshold lines up with a particular MSE; this language suggests σval is chosen ad hoc to adjust the S scale. That undermines the statistical interpretation of “S = 5 is 5σ above typical.”  
Required fix: Clarify whether σval is the actual standard deviation of the validation MSE distribution or an adjustable scaling. If σval is adjusted, the authors must stop calling S a “z-scored” residual and avoid the “5σ” language; instead describe S as a rescaled score. If σval is the true standard deviation, replace the “σval is set such that…” sentence with the actual σval value and demonstrate that MSE = 0.143 corresponds numerically to S = 5 with that σval.

P3-E6 (ESSENTIAL)  
Section: Table I and footnotes, page 6; Sections II.B, II.D, III  
Problem: The thresholds and anomaly counts are inconsistent between the main text, Table I, and the “Path-C unique” description. Table I lists Nanom as the cross-transfer counts, but these are labeled in the header as “Number of anomalies above survey-specific threshold” without clearly separating cross-transfer vs native values. Footnotes attempt to explain that DESI uses S>5 while SDSS/LAMOST use top-1% with S≥0.1060 and S≥0.4613 respectively, but those S thresholds are defined on different score scales (DESI-trained vs native-trained BigAE) without explicit recalibration. It is not clear which thresholds are used for the final 378,280 catalog per survey, and readers cannot reproduce the counts from the given information alone.  
Required fix: Provide a clean summary table of the *final* native-trained thresholds and counts (one row per survey) separate from the historical cross-transfer baseline. For each survey, specify: (i) whether scores are from the DESI-trained or native-trained BigAE (or IF for eROSITA), (ii) the exact numerical threshold on that survey’s native score, and (iii) the resulting anomaly count. Remove ambiguity where a single symbol “S” is used on multiple incompatible scales. PRD-level methods papers require reproducibility from the published text and tables alone.

P3-E7 (ESSENTIAL)  
Section: References, page 19–20  
Problem: Multiple references in the list appear misaligned with the in-text usage. For example:  
•  is cited in the introduction as “the quasi-matter bounce model predicts fNL = −35/8 = −4.375 [13,14,35],” but  is “D. Wands, ‘Local non-Gaussianity from inflation’, Class. Quant. Grav. 27, 124002 (2010).” Wands (2010) is a review of inflationary non-Gaussianity, not a matter-bounce fNL = −35/8 calculation.  
•  is Cai et al. 2009, “Non-Gaussianity in a matter bounce,” JCAP 0905, 011;  is Wilson-Ewing 2013, “The Matter Bounce Scenario in Loop Quantum Cosmology,” JCAP 1303, 026. Those two indeed discuss matter-bounce non-Gaussianity, but the precise value fNL = −35/8 is not easy to locate in their abstracts; it may be model-specific.  
Required fix: Verify that the exact prediction fNL = −35/8 is clearly stated in at least one of  or  in the same convention as Planck/Heinrich (local fNL, CMB/LSS convention). If not, add or replace references with a matter-bounce paper that explicitly gives this value, or derive it in an appendix with clear equations and assumptions. Also, adjust  so that it is not cited as providing the matter-bounce prediction, but perhaps as general background on local fNL.

P3-E8 (ESSENTIAL)  
Section: Section III.A “DESI DR1”, pages 4–5; Table II; cross-reference to   
Problem: The paper claims: “Our DESI anomaly rate of 0.87% is consistent with the 1.07% rate reported by Liang et al.  on the DESI EDR, despite differences in model architecture and a ∼90× increase in sample size.” Liang et al.  explicitly report 2,685 anomalies out of 250,000 BGS spectra (1.07%). The current work’s 0.87% is over 22.5M spectra, but includes unclassified filler and sky fibers. The “like-for-like” comparison is not supported: Liang’s sample is BGS-only, while the current numerator/denominator includes multiple target classes and many unclassified spectra, and this is not made precise.  
Required fix: Redo the comparison strictly for DESI BGS or other matching subsamples, using counts restricted to the same target selection as Liang et al., and explicitly state the matched sample sizes and anomaly rates. Alternatively, drop the “consistent with 1.07%” quantitative comparison and simply note that the absolute rate is of the same order, without implying a like-for-like agreement.

P3-E9 (ESSENTIAL)  
Section: Section II.D “Path-C Rebuild Methodology”, Figure 7; Injection-recovery description  
Problem: The injection-recovery tests are central to the claimed robustness, but the *nature* of the injected signals (continuum-dip vs emission-line, amplitude units, localization in wavelength/feature space) is only sketched in prose and never specified mathematically. No paper is cited describing this methodology. Therefore, the reported PASS/FAIL statuses at 5σ cannot be independently reproduced or evaluated.  
Required fix: Provide a quantitative definition of the injected signals (e.g., for continuum dips, spectrum modifications \( F(\lambda) \to F(\lambda)(1 - A \exp[-(\lambda-\lambda_0)^2/2\sigma^2])\) with given \(\lambda_0,\sigma\); for emission lines, analogous additive Gaussians) and define precisely what “A = 5σ” means (σ of what noise estimate). Either cite a prior anomaly-detection paper that uses an identical injection methodology or fully specify it in a new appendix with pseudo-code or equations.

P3-M1 (MAJOR)  
Section: Multiple places (e.g., Section II.A, II.B, III.F, Table V)  
Problem: Model-architecture descriptions and parameter counts are given without citations to any standard autoencoder or anomaly-detection references in astronomy or ML. For instance, BigAE is introduced as a “symmetric fully connected autoencoder” with particular dropout and latent size, but there is no reference to any previous autoencoder-based anomaly detection framework in astronomy beyond Baron & Poznanski (2017) . The “BigAE” name appears to be internal, with the only repository being the author’s GitHub. PRD typically requires sufficient external context and references to assess methodological novelty vs reuse.  
Required fix: Either clearly state that BigAE is an original architecture and motivate deviations from standard architectures or, if it is closely based on prior work (ML or astronomy), add those references and explain the relationship. For anomaly detection pipelines, include at least one methodological citation for autoencoder-based anomaly detection (beyond ) and, if using specific ML techniques like IsolationForest, cite the original IF paper.

P3-M2 (MAJOR)  
Section: Section IV.C, page 10; “Dedup-radius choice and per-survey astrometric heterogeneity”  
Problem: The deduplication radius of 5″ is justified qualitatively (e.g., Gaia sub-arcsecond, NEOWISE PSF ∼ 6″), but no external references for astrometric performance of each survey are provided. Also, the text states that the unique-object count 378,280 is robust at the ≲0.1% level to plausible radius changes, but no numbers are shown for 3″ and 7″.  
Required fix: Add citations for astrometric precision and PSF FWHM of DESI, SDSS, LAMOST, eROSITA, Gaia, NEOWISE (and Planck) from their survey papers ([1]–[7] largely cover some, but e.g. PSF and astrometry must be specifically cited). Provide (even briefly) the dedup counts at 3″ and 7″ to justify the robustness claim quantitatively.

P3-M3 (MAJOR)  
Section: Section IV.B, page 9; spatial χ² test  
Problem: A HEALPix χ² per pixel is reported: χ²=143,936 for 38,329 dof, χ²ν=3.76, and the paper says this is “dominated by the inhomogeneous footprints” and “should not be cited as evidence of astrophysical clustering.” However, no method is given for how expected counts per pixel are computed (uniform? weighted by survey footprints?), and no external reference is given for a standard treatment of multi-survey selection functions. The number is thus opaque and potentially misleading.  
Required fix: Either remove the χ² figure or fully specify the expected model (e.g., Poisson with mean proportional to combined survey coverage map) and how the dof are computed. If omitted, make clear that any rigorous clustering analysis awaits a detailed selection-function model and drop the quantitative χ².

P3-M4 (MAJOR)  
Section: Section V.B/C, Appendix C, Figure 8, Table VII  
Problem: The dependence of σ(fNL) on anomaly bias factor α and number density n is based on a custom Fisher implementation with heuristic choices for systematic-penalty (“15–30% degradation” from Heinrich et al.). No external validation of this pipeline is cited; the only quantitative link to published multi-tracer fNL forecasts is a general citation to , which is about SPHEREx bispectrum, not necessarily the same regime or modeling. For a journal like PRD, ad-hoc scaling relationships “∆σ/σ ≈ (6.1%/0.15)α” without demonstration of linearity across the range are not sufficient.  
Required fix: Provide direct comparison between your Fisher results and a published forecast with similar tracers (e.g., reproduce a result from  or related work) to demonstrate correctness. Alternatively, reframe the Fisher results as illustrative estimates with explicit caveats, and move the detailed α-scaling and sparse-tracer curves to an appendix, making clear they are not precision forecasts.

P3-M5 (MAJOR)  
Section: NANOGrav application, Appendix E  
Problem: The matter-bounce GWB template used for PTA analysis (Eq. E1) is introduced without reference to a standard PTA prediction pipeline; the treatment of the KDE likelihood is effectively custom. PRD would expect either a close mapping onto an existing PTA Bayesian framework (e.g., enterprise-based analyses cited by NANOGrav) or a detailed methodology description sufficient to reproduce the analysis. As-is, the description is too compressed to be replicable from the paper alone.  
Required fix: Expand Appendix E to give enough detail for another group to rerun the PTA analysis: priors, parameterization, mapping between γ and the strain spectrum in NANOGrav’s conventions, and any transformations applied to the KDE product. Reference at least one PTA methods paper (e.g., Lentati et al. 2013  or a NANOGrav methods paper that uses KDE likelihoods) to anchor the approach.

P3-M6 (MAJOR)  
Section: Bibliography, overall  
Problem: Several references lack arXiv identifiers that are standard and easily available:  
•  Liang et al. 2023 has arXiv:2307.07664.  
•  Heinrich et al. 2024 is given as JCAP 2024, 074, arXiv:2311.13082; the label in the reference text says “[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]” which is an internal bookkeeping note inappropriate for a PRD reference list.  
Required fix: Add missing arXiv IDs where available to all references and remove internal notes (e.g., “bibkey label retained” comments) from the bibliography. PRD references should be clean and free of internal LaTeX or group-labelling commentary.

P3-M7 (MAJOR)  
Section: Internal version-history / bookkeeping language, multiple pages  
Problem: The manuscript includes numerous internal-process phrases that must not appear in a PRD submission, e.g.:  
• “P2 §IV penalty (15–30%)”, “P3 anomaly_gold n=8.5e-06” in Figure 8 caption.  
• “P3  …” tags in the last figure and in captions.  
• “Path-C final” vs “cross-transfer baseline” language is fine, but internal labels like “P2”/“P3” referencing earlier project stages are not explained and appear to be internal audit tags.  
Required fix: Remove all internal labels (P2, P3, etc.) that do not refer to published papers or clearly defined stages in this manuscript. If some refer to previous submissions, either cite those submissions if they are published or rephrase in neutral language (“previous analysis in [ref]”).

P3-M8 (MAJOR)  
Section: “Data availability”, page 15  
Problem: The text references a HuggingFace dataset “private pending arXiv acceptance; public upon acceptance” and a GitHub repository for code. PRD’s standards typically require that essential data and code be accessible at acceptance, but “private pending” and GitHub-only links are not archival. Also, URLs are explicitly given; the journal may not want direct URLs in text.  
Required fix: Replace “private pending acceptance” phrasing with a commitment to deposit data in a long-term archival repository with a DOI (Zenodo, CDS, etc.) at acceptance. Ensure that any code repository is mirrored or tagged with a DOI (e.g., via Zenodo integration). Follow PRD style regarding URLs and DOIs for data and code.

P3-M9 (MAJOR)  
Section: Section III.C “SDSS DR18”, Figure 2 right panel  
Problem: The extreme anomaly scores shown for SDSS cross-transfer (up to 1.9×10¹¹) are labeled in the figure and text as a “cross-transfer artifact,” but the exact mechanism producing such enormous S values is not mathematically described. Given S = (MSE - µval)/σval, achieving 10¹¹ implies either catastrophic MSE or extremely tiny σval; if σval is fixed from DESI-validation, this suggests wild MSE outliers that might indicate numerical instability or preprocessing errors. This places doubt on the robustness of the autoencoder scoring.  
Required fix: Provide a brief quantitative explanation of how such large S values arise (e.g., typical MSE range and σval values for cross-transfer SDSS scores) and confirm that they are not numerical artifacts (overflow, missing normalization). If they are partly due to preprocessing mistakes (e.g., mis-scaled flux), either correct the scores or clearly state that those cross-transfer values are not used in any further analysis and are shown for illustration only.

P3-m1 (MINOR)  
Section: Abstract & Sections II–III; use of “σ” terminology  
Problem: The paper uses “5σ” terminology for anomaly thresholds, but S is not necessarily a true Gaussian-distributed standardized variable. While the authors explain “z-scored in the statistical sense,” the repeated “5σ” claim may mislead readers into equating S with Gaussian significance.  
Required fix: Add an explicit warning near Eq. (2) that S is not guaranteed to follow a standard normal distribution, so “5σ” refers only to 5 standard deviations of the validation MSE distribution, not a Gaussian tail probability.

P3-m2 (MINOR)  
Section: Several figures and captions (e.g., Fig. 1, Fig. 3–4, Fig. 9); axes and units  
Problem: Some figures mention quantities in text but do not show axis labels in the manuscript transcript (e.g., Fig. 4 shows NEOWISE anomaly with no visible W1/W2 axis; Fig. 9 shows images only). While that may be an artifact of the text extraction, PRD will require that all figures have clear axes and units where quantitative.  
Required fix: Ensure, in the actual submitted PDF, that all plots have labeled axes with units (e.g., “Wavelength [Å]”, “Anomaly score S”, “Probability density”). If already present in the real PDF, no further action; if not, update the figure graphics.

P3-m3 (MINOR)  
Section: Section IV.A, Figure 5  
Problem: The y-axis label in Figure 5 is described as “SIMBAD novelty fraction (%)” but the text describes this as “SIMBAD-unmatched fractions,” which is the complement of “novelty” if novelty is defined relative to the union of many catalogs. The figure could be misinterpreted as showing true astrophysical novelty.  
Required fix: Rename the axis to “SIMBAD-unmatched fraction (%)” and emphasize in the caption that this is not the genuine catalog novelty rate.

P3-n1 (NIT)  
Section: Various; duplication and awkward phrases  
Problem: Some duplicated or awkward wording:  
• “reproducibility scripts are publicly released … reproducibility scripts shipped with the companion data repository” (repetition).  
• A long sentence in Table I footnotes includes “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”  
Required fix: Remove duplicated phrases and streamline the text.

P3-n2 (NIT)  
Section: References  and   
Problem: The note “[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]” is internal.  
Required fix: Delete this note; leave a standard reference with journal, volume, page, year, and arXiv ID.

P3-n3 (NIT)  
Section: Use of “BigAE” naming  
Problem: The architecture is called “BigAE” without expansion of the acronym; in a PRD methods paper, first use should spell out “Big Autoencoder (BigAE)” or similar.  
Required fix: Expand the acronym on first use in the Introduction.

P3-n4 (NIT)  
Section: Appendix labels and cross-references  
Problem: Some internal cross-references are slightly confusing (e.g., “P2 §IV penalty” in Fig. 8 caption).  
Required fix: Replace any cross-reference to “P2” or “P3” with neutral references to sections in this paper or to published work.

P3-length1 (MAJOR)  
Section: Entire manuscript (20 pages of dense text plus many appendices)  
Problem: For the claimed contributions—a large multi-survey anomaly catalog and exploratory cosmology applications—the manuscript is very long and includes extensive, somewhat tangential material (e.g., full PTA MCMC derivation, detailed multi-tracer Fisher exploration) that could be separated into companion papers. The length and density make it harder to assess and reproduce the core catalog and method, which is the main claimed contribution.  
Required fix: Consider shortening the paper to focus on the catalog, autoencoder methodology, and the most robust astrophysical findings (e.g., DESI anomalies, multi-survey matches). The PTA and detailed fNL Fisher forecasts (Appendix C, E) could be split into a separate, more focused cosmology paper. A target length of ~12–14 journal pages for the main paper (excluding appendices) would better match the primary contribution.

## Summary recommendation

MAJOR REVISIONS

The paper presents an ambitious and potentially valuable multi-survey anomaly catalog and explores interesting cosmological applications, but multiple load-bearing claims (novelty fraction, σ(fNL) improvements, PTA Bayes factors) rest on internal pipelines without adequate external referencing or methodological transparency. There are also issues with reference accuracy (matter-bounce fNL citation), internal bookkeeping language, and clarity of threshold definitions. These shortcomings do not appear fatal, but they must be rigorously addressed, with clearer derivations or reduced claims, before the work reaches PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

[P3-E10] **Abstract faithfulness issue: the abstract cites a “companion data repository” and “publicly released” artifacts as if they already exist, but the body only promises release or says the data are in a *private pending* repository.** The abstract’s final sentence, “The catalog, model weights, and reproducibility scripts are publicly released,” is not supported by the Data availability section, which states the catalog is on HuggingFace in *private pending arXiv acceptance* and the code is on GitHub. That is a direct main-text/body mismatch in release status, and the abstract overstates availability relative to the paper’s own data policy. [5][6]

[P3-E11] **Abstract faithfulness issue: the abstract’s “largest-scale application” claim is not consistently supported by the body’s own counts because the paper itself later frames several results as exploratory or quarantined.** The introduction and conclusions describe ACT DR6 as quarantined and excluded from the main science result, and the body also labels LAMOST as an exploratory tier and the NANOGrav result as illustrative rather than a detection. The abstract nevertheless packages the full 378,280-object catalog, discovery fractions, cosmological forecasts, and PTA inference together as if they are all equally validated headline results, which is not faithful to the paper’s own caveats. [2][5]

[P3-E12] **Equation-dimension / normalization issue: Eq. (2) is not a pure z-score if \(\mu_{\text{val}}\) and \(\sigma_{\text{val}}\) are not the actual validation-set mean and standard deviation used at scoring time.** The body defines \(S(x)=(\mathrm{MSE}(x)-\mu_{\text{val}})/\sigma_{\text{val}}\) and says \(\mu_{\text{val}}\) and \(\sigma_{\text{val}}\) are the mean and standard deviation of validation MSE, but later text says \(\sigma_{\text{val}}\) is “set such that” \(S>5\) corresponds to a chosen MSE threshold. Those two descriptions are not mathematically equivalent: a z-score requires \(\sigma_{\text{val}}\) to be measured from the validation distribution, not tuned to a catalog cut. This is a dimensionless-normalization inconsistency that directly affects every quoted \(S\) threshold. [5][6]

[P3-M10] **Internal cross-reference mismatch: Figure 2 says the SDSS native re-score “compresses the same objects to \(S<14\), eliminating the \(10^4\)–\(10^{11}\) tail,” but Table I and the SDSS section later imply the same objects can reach \(S=49.5\) and other large values in cross-matched cases.** The figure caption is specifically about the SDSS cross-transfer artifact, while the body’s later cross-match example shows an SDSS score of 49.5 for TIC 374313355. That means the reader is asked to treat “native re-score \(<14\)” and “SDSS score 49.5” as if they were on the same scale, but they are not clearly distinguished by score type, making the figure-caption/body linkage ambiguous. [5]

[P3-M11] **Figure-caption/body mismatch: Figure 3’s caption says the dominant SDSS cluster is “∼84% of objects” and contains ultra-cool dwarfs, but the body later states the SDSS anomaly population is summarized by an emission-line classification table where the dominant category is “Uncategorized” at 52.7%.** These are different summaries of the same SDSS anomaly set, but the manuscript never explicitly reconciles them as *cluster membership* versus *semantic category*. Without that clarification, the caption and body appear to give conflicting dominant populations for the same catalog. [5]

[P3-M12] **Arithmetic inconsistency: the paper’s own count sums in Table I do not match the text’s stated subtotaling in one place.** Table I says the Path-C per-survey native counts sum to 388,493 before deduplication, and that 10,213 objects are collapsed to yield 378,280 unique objects. That arithmetic is correct because \(388{,}493-10{,}213=378{,}280\). However, the same table also says the “cross-transfer baseline total” is 319,443 and the ACT-including variant “would have produced 388,693 − 10,213 = 378,480 unique objects,” which is internally inconsistent with the previous 388,493 subtotal and the stated “+200 relative to the headline.” The quoted 388,693 subtotal is not reconciled with the nearby 388,493 subtotal. [5]

[P3-M13] **Arithmetic inconsistency: the NEOWISE polar-cap calculation is numerically off in the body/figure caption.** The paper says the 17/436 rejected objects correspond to a “2.6× excess over the uniform-sphere null expectation (1.52%).” But \(17/436 \approx 3.90\%\), and \(3.90\%/1.52\% \approx 2.57\), so the 2.6× factor is consistent; the problem is that the stated expected fraction 1.52% is not derived or shown, and the paired statement in the later discussion uses \(10^\circ\)-radius polar caps rather than the \(|b_{\rm ecl}|<80^\circ\) mask in the main text. This is a body-vs-caption inconsistency in the geometry used to justify the same percentage. [5]

[P3-M14] **Arithmetic inconsistency: the “3 PASS / 3 FAIL-with-diagnostic” injection-recovery summary is not matched by the later figure description.** The abstract says “3 PASS (SDSS 64%, Planck 100%, NEOWISE 100%) and 3 FAIL-with-diagnostic (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%) at 5σ,” while Figure 7’s caption adds additional variants: SDSS emission-line 7.2%, LAMOST emission-line 0.6%, and NEOWISE at \(|b_{\rm ecl}| > \{85^\circ,82^\circ,80.5^\circ\}\). Those added variants change the implied denominator of what counts as “the full 6-survey injection-recovery outcome,” so the 3/3 headline is not fully supported by the figure caption as written. [5]

[P3-M15] **Unsupported novelty claim: “largest multi-archive anomaly search reported to date” is asserted without a comparison table or literature scan.** The paper compares against Liang et al. for DESI and a few astronomy anomaly papers in the references, but it does not provide a systematic benchmark across multi-survey anomaly catalogs, all-sky photometric outlier searches, or large-scale Gaia-based anomaly work. Because the claim is superlative and cross-domain, it needs explicit comparative evidence rather than a single single-survey comparator. [5]

[P3-M16] **Unsupported novelty claim: “largest-scale application of autoencoder anomaly detection across seven astronomical archives” is not established by the paper’s own data-product framing.** The manuscript includes ACT DR6 only as a quarantined cross-transfer artifact and excludes it from the main per-survey block, while the headline 37.3 million count mixes retained catalogs, exploratory tiers, and a map-patch class that is not comparable to point-source objects. The paper therefore demonstrates a *heterogeneous* multi-archive application, but not cleanly the “largest-scale” single-method application in a like-for-like sense. [5]

[P3-M17] **Null-procedure comparability issue: the paper juxtaposes multiple “\(\sigma\)” quantities from different procedures without a sufficiently explicit non-comparability warning.** Examples include the DESI \(S=5\) catalog threshold, the empirical \(\alpha_{jk}=0.19\pm0.65\) from a jackknife Landy–Szalay measurement, the forecast \(\sigma(f_{\rm NL})=8.14\) from a Fisher model, and the NANOGrav \(\gamma=2.567\pm0.382\) posterior width from an MCMC. These are all standard deviations or sigma-like summaries, but they come from different nulls, estimators, and likelihoods; the manuscript compares them in adjacent prose as if they were directly interchangeable significance measures. [5]

[P3-M18] **Null-procedure comparability issue: the paper compares the 0.87% DESI anomaly rate, the 3.38% SDSS rate, and the 0.39% LAMOST rate as if they were directly meaningful cross-survey rates, but the body itself says SDSS and LAMOST are transfer-learning artifacts and later redefines their native thresholds.** Because these rates arise from different score scales and threshold families, the juxtaposition is not a fair statistical comparison unless the manuscript explicitly states the null procedures are not comparable. The paper partly does this later, but the abstract and conclusions still present the rates in a way that invites direct comparison. [5]

[P3-M19] **Stale-number issue: the manuscript’s internal count logic changes between the cross-transfer baseline and the Path-C rebuild, but the abstract still quotes the earlier 319,443-style baseline language indirectly through the release claims.** The body makes clear that 319,443 is only a before/after diagnostic and that the canonical count is 378,280, yet the Data availability section still refers to the “319,443-anomaly cross-transfer baseline” being preserved as an archival comparison artifact. That is fine as a diagnostic, but it is stale if presented in the same breath as the released catalog without a sharper separation between obsolete baseline and canonical result. [5]

[P3-M20] **Appendix-vs-main-text mismatch: Appendix C says the \(f_{\rm NL}\) improvement scales by linear interpolation from the fiducial 7-bin Fisher result at \(\alpha=0.15\), but the main-text Fisher section describes a quadratic positivity-respecting form \(1/\sigma(f_{\rm NL})^2=F_0+c\alpha^2\).** A linear \(\Delta \sigma/\sigma\) scaling and a quadratic-in-\(\alpha\) Fisher form cannot both be treated as exact without a derivation showing the regime in which the linear approximation is valid. The paper does not supply that derivation, so the appendix is not fully consistent with the main-text modeling assumption. [5]

[P3-M21] **Arithmetic inconsistency: the DESI top-1,000 novelty numbers do not reconcile cleanly with the “archival-identification rate of 82.2% (822/1,000)” and the earlier “genuine novelty fraction of 17.8% (178/1,000)” when the narrative also says the top-1,000 are cross-matched against 20 curated catalogs via CDS X-Match.** On its face those two percentages do sum to 100%, but the paper then states the SIMBAD-unmatched fractions “substantially overstate true catalog novelty” and that the deeper NED+VizieR sweep identifies counterparts for 100% of some samples. That means 17.8% is a single-cross-match lower bound, not a stable novelty fraction, and the abstract’s wording overstates its robustness. [5]

[P3-M22] **Figure-caption/body mismatch: Figure 8 caption says the dashed gray line marks the dense-tracer limit \(\sigma(f_{\rm NL})=11.71\) and the dotted dark-red line marks the single-tracer baseline \(\sigma(f_{\rm NL})=16.85\), but the main text and Table VII use \(\sigma(f_{\rm NL})^{\rm std}=8.98\) as the single-tracer baseline.** These cannot all be the same baseline quantity. The paper never explains whether 11.71 and 16.85 refer to a different tracer configuration, a different number density, or a different normalization, so the figure caption is numerically inconsistent with the main text. [5]

[P3-M23] **Arithmetic inconsistency: the NANOGrav section gives two different uncertainty summaries for the same posterior and does not reconcile them.** It reports \(\gamma=2.567\pm0.382\) and also an “equivalent quantile summary” \(\gamma=2.591^{+0.291}_{-0.287}\). Those are not equivalent uncertainty descriptions, since the implied symmetric width and the 68% credible interval differ materially. The body says this is because the posterior is non-Gaussian, but then the abstract still reports only the \(\pm0.382\) form without the corresponding caveat, making the significance comparison to \(\gamma=3.0\) look cleaner than the posterior actually is. [5]

[P3-M24] **Internal-reference issue: the paper cites Appendix E for the PTA analysis, but Appendix E’s equation E1 is partially typeset as a malformed expression and does not clearly define the strain-spectrum convention used to map \(\gamma\) into NANOGrav parameters.** The equation is presented as \( \log_{10}\rho_i = 21 2 \log_{10} A - \log_{10}(12\pi^2) + \dots \), which is not syntactically clean and appears to be missing multiplicative symbols or formatting. That makes the appendix unable to serve its claimed role as a reproducibility anchor for the main-text \(\gamma\) inference. [5]

[P3-M25] **Appendix-vs-main-text mismatch: Table IV lists caveat (j) as “GS corrected: \(\sigma(f_{\rm NL})^{GS}\in[0.94,8.98]\) central 1.95; prior \(\pm 7.43\) dropped,” but the main text’s gold+silver subsection says \(\sigma(f_{\rm NL})^{GS}=1.95\) central and then calls it “consistent with no improvement at <1σ.”** That central value is far below the baseline 8.98, so the prose about “no improvement” is only defensible if the envelope is dominated by a prior ceiling or a hard bound. The manuscript does not explain that suppression clearly enough, so the appendix and main text are not aligned on the practical meaning of the gold+silver forecast. [5]