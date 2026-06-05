# P3 auto-2026-06-05_1517pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13047 chars)
**Wall time**: 87.5s

---

P3-E1  
Section: Abstract, page 1  
Problem: The abstract claims “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog .” Liang et al. 2023 (MNRAS 525, 1078; arXiv:2307.07664) report 2,685 anomalies from ~250,000 DESI EDR spectra (1.07%). The point-source tier here is 378,080 anomalies, which is ≈ 140.8× larger than 2,685. Numerically this is correct, but the “largest prior single-survey anomaly catalog” assertion is not justified: Baron & Poznanski 2017 do large-scale SDSS anomaly detection, and there may be more recent large catalogs; no evidence is provided that  is the largest to date.  
Required fix: Either (a) provide a systematic comparison demonstrating that  is indeed the largest prior single-survey anomaly catalog (including survey sizes and anomaly counts for other works, especially  and any post‑2023 DESI anomaly work) or (b) weaken the claim to something like “∼ 141× larger than the DESI EDR anomaly catalog of Liang et al. ” without implying it is the global largest.  

P3-E2  
Section: Abstract, page 1  
Problem: “the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase” is ambiguous and poorly justified. Relative to Liang et al.  (2,685 DESI EDR anomalies), 195,829/2,685 ≈ 73, so the factor is arithmetically correct. But “like‑for‑like” is misleading because this work uses DR1 (22.5M spectra) with a different architecture, training set, and threshold, whereas Liang et al. use EDR with a normalizing-flow autoencoder and different selection functions.  
Required fix: Explicitly state what “like‑for‑like” means (e.g., “for DESI spectra, comparing anomaly counts irrespective of survey size and architecture”) or remove that wording and simply report the numerical ratio without implying methodological equivalence.  

P3-E3  
Section: Abstract, page 1  
Problem: “Extended archival cross-matching of the top-1,000 DESI anomalies against 20 curated all-sky catalogs via CDS X-Match yields a genuine novelty fraction of ∼ 17.8%” is a central quantitative claim, but no citation is given to any method paper or CDS X-Match documentation, and the internal consistency needs checking. Later, Section IV A states 822/1,000 have archival IDs, i.e. 178 “novel,” exactly 17.8%, consistent with the abstract. However, the methodology (which 20 catalogs, matching radii, handling of ambiguous matches) is not formally referenced and is only briefly described in text.  
Required fix: Add a citation to an authoritative CDS X-Match description (e.g. CDS or VizieR documentation) and in the main text provide a concise, explicit list of the 20 catalogs and the matching criteria used, so that the 17.8% figure can be independently reproduced. Clarify in the abstract that this is a *single-sample point estimate at the top‑1,000 stratum* and not a global catalog rate (the body already says this).  

P3-E4  
Section: Abstract & Section V, pages 1 and 10–11  
Problem: The NANOGrav analysis claims use of “the NANOGrav 15-yr HD-correlated KDE free-spectrum likelihood  (Zenodo 10.5281/zenodo.8060824; 30 Fourier bins; …),” while reference  is the main NANOGrav 15‑yr GWB detection paper (Agazie et al. 2023, ApJL 951, L8, arXiv:2306.16213 for the HD‑correlated background). The specific KDE free‑spectrum product is a dedicated Zenodo dataset and is not identified by DOI or arXiv ID in the bibliography. The claim “real-KDE free-spectrum MCMC yields γ = 2.567 ± 0.382” and the Savage–Dickey Bayes factors depend entirely on that external product.  
Required fix: Add a separate bibliographic entry for the KDE free-spectrum dataset (author list or collaboration, title, Zenodo DOI 10.5281/zenodo.8060824) distinct from , and clearly cite that new reference wherever the KDE free-spectrum likelihood is used. Ensure that the quoted posterior mean, error bar, and Bayes factors are traceable to the public dataset and to a reproducible pipeline.  

P3-E5  
Section: Section V (Cosmological applications), pages 10–11  
Problem: Claims about the matter-bounce prediction fNL = −35/8 and γ = 3.0 are attributed to [13,14,35]. Reference  (Cai et al. 2009, JCAP 0905:011) and  (Wilson‑Ewing 2013, JCAP 1303:026) do discuss non‑Gaussianity in a matter bounce and loop quantum cosmology, but the precise value fNL = −35/8 for the local template is model‑dependent. Reference  (Wands 2010) is a review on local non‑Gaussianity from inflation and does not derive this bounce value. There is some conflation between a specific w=0 matter-bounce realization and the broader class of bouncing cosmologies.  
Required fix: Tighten the attribution: explicitly state which paper derives fNL = −35/8 in the *specific* model used (likely  and/or ) and remove or rephrase  if it does not contain this prediction. Clarify that the quoted fNL and γ refer to a particular scalar‑only w=0 matter bounce rather than to bounce cosmologies in general.  

P3-E6  
Section: Section I (Introduction) & references, pages 1 and 19  
Problem: “Heinrich et al.  (σ(fNL ) ≈ 0.7 bispectrum-only forecast).” Reference  is listed as “Heinrich, Doré, & Krause, JCAP 2024, arXiv:2311.13082” with a note “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity.” The paper indeed is “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum” (arXiv:2311.13082). Their forecast values depend on specific survey/fiducial assumptions and are not a single universal “σ(fNL) ≈ 0.7.” Without a citation to a specific table or figure, this σ value is difficult to verify and risks misrepresenting their result.  
Required fix: Cite the exact table/figure and cosmological/tracer configuration in  from which σ(fNL) ≈ 0.7 is taken, and phrase the text accordingly (e.g., “for their fiducial SPHEREx configuration, Heinrich et al. find σ(fNL) ≈ 0.7”). Confirm that 0.7 matches their published numbers for the cited configuration; if not, correct the value.  

P3-E7  
Section: Section V (Fisher forecast), pages 10–11  
Problem: The text contrasts “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement…; σ(fNL)std = 8.98 single-tracer baseline).” The baseline σ(fNL)std = 8.98 is not clearly tied to an external reference; it appears to be a result of the author’s own Fisher calculation, but no external benchmark (e.g. DESI collaboration fNL forecasts) is cited. For a methods paper, the external comparability of this σ(fNL)std matters.  
Required fix: Either (a) explicitly state that σ(fNL)std = 8.98 is the internal single‑tracer DESI forecast from this work, not taken from the literature, or (b) if it is intended to match a forecast from an external source, add a citation and verify agreement with the corresponding table in that source. Do not imply literature validation unless such a match is demonstrated.  

P3-E8  
Section: Section IV A, Figure 5, pages 8–9  
Problem: The “SIMBAD-unmatched fractions” rely on SIMBAD as a reference catalog, cited as  (Wenger et al. 2000, A&AS 143, 9). The text claims a 100% archival ID rate for the SDSS DR18 top‑20 SIMBAD-unmatched anomalies in NED+VizieR and similar 100% for small subsamples of eROSITA, NEOWISE, Gaia, but no NED or VizieR references appear in the bibliography. The methods for these cross-matches (matching radius, catalogs used) are also not documented beyond prose.  
Required fix: Add explicit references for NED and VizieR, and give enough methodological detail (radius, catalogs, query modes) to make the stated 100% identification results independently verifiable. Clarify that these are small‑sample checks and do not define a global completeness rate.  

P3-E9  
Section: Section IV B (spatial analysis), page 9  
Problem: The χ² and correlation statements rely on Planck dust maps and HEALPix; Planck is cited ([7] and ) but HEALPix and the specific Planck dust product are not. The text claims “no correlation with Planck dust intensity (Pearson r = 0.006, p = 0.21).” To be reproducible, the exact map (e.g. Planck 2018 Commander/SMICA dust, Nside, unit) should be identified and the HEALPix reference included.  
Required fix: Add a bibliographic entry for HEALPix and specify the exact Planck dust map used (frequency, product name, reference [7] or companion paper). State the Nside resolution used for the correlation, so that the χ² and correlation tests can be checked.  

P3-E10  
Section: Section IV D / Appendix F (Planck × ACT), pages 11 and 16–18  
Problem: ACT DR6 is referenced via  (Qu et al., “The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum…”, ApJ 962, 112, 2024). This is an ACT DR6 lensing paper, not a general DR6 data release description; the maps used (e.g. DR6 CMB temperature maps, resolution, filters) are not specified or cited to a dedicated data release paper. The text also uses approximate val‑loss numbers (“val loss ≈ 2×10⁴”, “≈ 2.2×10⁴”) inconsistently.  
Required fix: (a) Add a reference to the ACT DR6 data release or map description appropriate for the temperature maps actually analyzed, if available; otherwise clearly state that DR6 maps are taken from the products described in  and specify which. (b) Use consistent, precise values for the validation loss, not two slightly different approximations.  

P3-E11  
Section: Section II A (BigAE Architecture), pages 2–3  
Problem: The Planck and ACT input description “CMB surveys (Planck, ACT), the input is a 64×64 pixel patch flattened to 4,096 features” and later the Planck CMB subsection’s autoencoder description (“3 conv layers + 128‑dim FC bottleneck, 1.1×10⁶ parameters”) are consistent internally, but the ACT cross‑transfer architecture (“32‑dim latent… 540K parameters”) is only described in Appendix F and not referenced in the main text. Since ACT is quarantined, this is methodological but still part of the scientific narrative.  
Required fix: Either briefly summarize the ACT cross‑transfer architecture in the main text where ACT is first mentioned, with a pointer to Appendix F, or clearly signal in Section II A that ACT uses a different latent dimension/parameter count, detailed only in Appendix F because it is quarantined. This avoids ambiguous conflation of the Planck and ACT CMB architectures.  

P3-M1  
Section: References [1]–, –, –, –, –, , pages 19–20  
Problem: Several references are missing explicit arXiv IDs even when they exist and are standard in cosmology, reducing auditability of claims that depend on them. For example:  
- [1] DESI DR1 is “DESI Data Release 1, 2025, DESI DR1 documentation,” but no arXiv or journal.  
- [2] “LAMOST Data Release 10” is “Research in Astronomy and Astrophysics, 2024” with no arXiv listed; RAA DR10 paper (Luo et al.) has an arXiv preprint.  
- [3] SDSS DR18 ApJS 267, 44 (2023) likely has an arXiv (e.g., arXiv:2208.11516 or similar for DR17/18).  
-  Planck 2018 NG constraints (A&A 641, A9) has arXiv:1905.05697.  
-  Baron & Poznanski 2017 MNRAS 465, 4530 has arXiv:1607.01025.  
-  Liang et al. 2023 MNRAS 525, 1078 has arXiv:2307.07664.  
-  Nicolaou et al. Astronomaly/ DESI EDR, described as “2026, in press,” but no arXiv is supplied; by the time of a PRD decision, an arXiv ID may exist.  
Required fix: For each refereed cosmology/astrophysics paper in the bibliography that has an arXiv version, add the arXiv identifier. For preprints or “in press” works (e.g. ) ensure the arXiv ID is correct and up to date, and that no “future‑dated” placeholders are used.  

P3-M2  
Section: References , , , , , , pages 19–20  
Problem: Some references are only given as arXiv preprints or as general reviews, but are used in the text in a way that suggests more specific numerical results. For instance:  
-  SPHEREx white paper (arXiv:1412.4872) is somewhat dated relative to later SPHEREx design/fisher updates; yet the text states “testable at 3–5σ with SPHEREx ” without reference to those more recent forecasts.  
-  Verde et al. 2013 is cited generically on tensions but not obviously used in any concrete calculation.  
Required fix: Where specific numerical claims (e.g. SPHEREx detection significance) are made, add and use the most recent, quantitative SPHEREx forecast reference(s) (if different from ) and ensure the quoted significance range matches those works. If  etc. are not actually used to support a specific statement, consider removing them to avoid “bibliography padding.”  

P3-M3  
Section: Throughout; especially Sections V & V A, pages 10–11  
Problem: The paper makes nontrivial use of Bayesian model comparison (Savage–Dickey Bayes factors, “decisive on Jeffreys’ scale”, etc.) relying on Trotta 2008 but does not specify priors in sufficient detail nor cross‑check with contemporary PTA analyses beyond citing EPTA/PPTA. Precision cosmology claims in PRD require unambiguous priors.  
Required fix: Explicitly write down the priors used for γ and log10 A (bounds are given, but prior *shape* must be clearly stated as uniform), and clarify that the Bayes factors BMB/free and BSMBHB/free are conditional on these choices. Optionally, compare qualitatively with NANOGrav’s own model‑comparison results in  to show consistency in order of magnitude.  

P3-M4  
Section: Section VII (Conclusions) & Data availability, page 14  
Problem: The data release URLs are given as literal HTTPS links to GitHub and HuggingFace. PRD typically does not allow or encourage production references to mutable GitHub branches as the primary archival record, and the URLs are not accompanied by DOIs. Also, one release is described as “private pending arXiv acceptance; public upon acceptance,” which is circular for refereeing.  
Required fix: Provide a stable DOI-based archive (e.g. Zenodo) for the catalog, code, and MCMC chains, and cite it in the references. During referee stage, ensure that the referees have anonymous access (e.g. via a private link) and note this in the cover letter rather than in the main text. Remove “pending arXiv acceptance” phrasing from the paper body.  

P3-M5  
Section: Appendix C (sensitivity of σ(fNL) to α), pages 15–16  
Problem: Table VII shows σ(fNL) as a function of α via “linear scaling from the fiducial 7‑bin Fisher result at α = 0.15.” However, earlier in the main text a more accurate Fisher fit “1/σ(fNL)² = F0 + cα²” is given. Direct linear scaling in α is inconsistent with the quadratic form in the main text and may confuse readers about the correct scaling.  
Required fix: Recompute Table VII using the same quadratic Fisher‑positivity fit used in the main text, or explicitly label the table as a crude linearized approximation and make sure the numbers are consistent (within acceptable approximation) with the quadratic relation. Best is to avoid any contradictory scaling claim.  

P3-M6  
Section: General, multiple pages  
Problem: Several citations are used for broad, qualitative statements (“GR projection corrections contribute |Δσ/σ| < 0.02%… [38–41]”) but no explicit calculation or citation to a specific code run (e.g. CLASSgal) is given. PRD‑level methodology requires either explicit derivation or a clear, specific literature reference where the same calculation is done.  
Required fix: For the GR projection fraction (<0.02%), either provide enough detail (equations, k‑range, redshift range, bias, and magnification slopes) to reproduce it or reference a paper that does so for equivalent configurations. Cite the CLASSgal paper explicitly where relevant and state which settings were used.  

P3-N1  
Section: Various; wording of claims of novelty and scale, pages 1, 14  
Problem: Phrases like “the largest multi-archive anomaly search reported to date,” “largest prior single-survey anomaly catalog,” and “extends prior single‑survey anomaly studies [10–12] to a multi-survey framework” are strong novelty claims whose truth is difficult to audit comprehensively. While [10–12] are relevant, the literature search for other large anomaly catalogs (e.g. in LSST simulations, other DESI analyses, or transient pipelines) is not documented.  
Required fix: Soften novelty language to “to our knowledge” and clarify that the comparison is explicitly to [10–12] for spectroscopic archives. Alternatively, add a short paragraph in the introduction surveying the known large‑scale anomaly catalog literature and explicitly justifying the “largest” claim.  

P3-N2  
Section: Section II B (definition of S), page 2  
Problem: The definition “S(x) ≡ (MSE(x) − μval)/σval” is clear, but the DESI example “μval ≈ 0.0287… and σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143” is not fully self‑consistent numerically: if μ ≈ 0.0287 and S=5 at MSE≈0.143, then σ ≈ (0.143−0.0287)/5 ≈ 0.0229; this should be explicitly spelled out so that readers can check consistency.  
Required fix: Add a brief sentence explicitly giving σval for DESI (e.g., “σval ≈ 0.023, so S = 5 corresponds to MSE ≈ 0.143”) to make the example numerically transparent.  

P3-N3  
Section: Bibliography formatting, pages 19–20  
Problem: Reference  is labeled as arXiv:1412.4872 (2014) with no journal, which is acceptable but may be outdated;  has a parenthetical note about “bibkey label retained as Heinrich2023,” which is an internal bookkeeping comment and not standard reference formatting.  
Required fix: Remove internal key‑management notes from the references and adhere to PRD style. If  has since been published or updated, consider citing the most recent or journal version.  

P3-N4  
Section: Internal repetition, pages 2 and 4  
Problem: The sentence about reproducibility scripts is effectively duplicated: in Section II D (“reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)”) there is a duplicated phrase. This appears to be an editing artifact.  
Required fix: Remove the duplicated parenthetical and streamline the sentence to a single clear statement.  

P3-N5  
Section: Section III, Table I caption and footnotes, pages 7–8  
Problem: The table uses multiple symbols (♡, ♠, ¶, †, ‡, ∥, §) and lengthy footnotes. Some of the explanatory text in the footnotes restates material from the main text and includes phrases like “the earlier ‘strict subset’ framing is replaced with this exact 284/298 = 95.3% overlap,” which read like internal revision notes rather than final exposition.  
Required fix: Simplify the footnotes to the minimum needed to interpret the table. Remove meta‑phrases referring to “earlier framing” and present only the final, self‑contained description.  

P3-N6  
Section: Miscellaneous typos / phrasing, multiple pages  
Problem: Several small stylistic or typographical issues (e.g. “BigAE is a deterministic autoencoder (not variational)” could be clarified to “non‑variational autoencoder”; a few sentences in the caveats list read like lab notes). None affect the science but reduce polish.  
Required fix: Perform a careful language pass to standardize technical terminology and remove informal or revision‑history phrasing.  

## Summary recommendation

MAJOR REVISIONS  

The paper’s core technical content and many internal numbers are largely self‑consistent, and most external references correspond to real, appropriate works with correct basic metadata. However, the cosmological forecasting and NANOGrav sections lack sufficiently precise referencing and prior specification for PRD standards; several novelty and “largest” claims are under‑justified; and some key external datasets (CDS X‑Match catalog set, NANOGrav KDE product, NED/VizieR use) are not properly cited. These issues do not require a new analysis but do require careful, explicit correction and clarification of citations, attributions, and scaling relations, especially for the fNL and γ claims, before the paper could be considered at PRD’s rigor level.

---

## PASS 2 — self-critique findings (what initial review missed)

P3-E12  
Section: Abstract vs. Section III / Table I  
Problem: The abstract states “Six injection-recovery gates: 3 PASS (SDSS 64%, Planck 100%, NEOWISE 100%) and 3 FAIL-with-diagnostic at 5σ (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%; eROSITA cross-validation stability 81.5%).” In the body, the only explicit 64% figure is for SDSS continuum-dip recovery in Fig. 7, but “Planck 100%, NEOWISE 100%” are described as 500/500 and 1000/1000 recoveries in text, not as percentages; the Gaia and eROSITA injection fractions are only given later in §VI D(ii), not in §III. This is more of a consistency-of-narrative issue: the abstract compresses a mix of Section III and Section VI D numbers without any direct pointer to where *each* percentage is derived, which makes them hard to audit from the survey-by-survey section alone.  
Required fix: In the main text, ensure that all six percentages quoted in the abstract are explicitly written in the relevant survey subsections (not only in the caveats section) and numerically connected to their underlying counts (e.g., “500/500 = 100%”). Add a sentence in §II D or §III explicitly referencing Fig. 7 as the source for the “3 PASS / 3 FAIL-with-diagnostic” summary quoted in the abstract.

P3-E13  
Section: §III E / Fig. 7 / Table VII  
Problem: The fNL forecast scaling is internally inconsistent across the paper. Section V uses a Fisher-positivity relation \(1/\sigma(f_{\rm NL})^2 = F_0 + c\alpha^2\), while Appendix C states that Table VII is “derived by linear scaling from the fiducial full 7‑bin Fisher result at α = 0.15,” and Fig. 7’s caption refers to a “canonical 5-tracer Fisher of §V.” The numbers in Table VII indeed follow an empirical linear law in α (the “Improvement” column is exactly 40.7%×α for all rows), which contradicts the quadratic α² dependence in the main text. This is a new inconsistency not covered by P3-M5: the body claims quadratic scaling, while the Appendix uses strictly linear scaling and a different Fisher configuration (5-tracer vs 7‑bin) without reconciling the two.  
Required fix: Decide on a single, self-consistent scaling prescription and configuration (either the 7‑bin quadratic Fisher or the simplified 5-tracer linear approximation) and apply it everywhere. If you retain the quadratic form, recompute Table VII from \(1/\sigma^2 = F_0 + c\alpha^2\) and adjust the “Improvement” column accordingly, and revise Fig. 8’s caption so that it explicitly uses the same Fisher setup as §V. If you instead keep a linearized approximation, clearly flag it as such in both §V and Appendix C, and remove any formulas that suggest a strictly quadratic α² dependence.

P3-E14  
Section: §II B (definition of S), §III A (DESI numbers)  
Problem: The DESI anomaly rate arithmetic and σval back-solve are not shown explicitly and the numbers are borderline inconsistent. The text gives μval ≈ 0.0287 and says “σval is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143,” implying σval ≈ (0.143 − 0.0287)/5 ≈ 0.0229. Later §III A reports “val loss = 0.0287 (MSE) on a held-out 20% validation split and identifies 195,829 anomalies… anomaly rate 0.87% … Scores range from 5.0 to 25.2.” That rate is consistent with 195,829 / 22,504,897 ≈ 0.87%, but σval is never actually given numerically, making it impossible to check that the reconstructed S distribution (with minimum S = 5.0) truly matches the quoted μval and threshold MSE. This leaves a small but avoidable arithmetic opacity around the fundamental S definition.  
Required fix: Explicitly state σval for DESI (e.g., “σval ≈ 0.023, so S = 5 corresponds to MSE ≈ 0.143”) and, ideally, mention the minimum observed MSE among anomalies to confirm that S ≥ 5 in the catalog is consistent with that (e.g., “the lowest-anomaly MSE is 0.143 by construction”). This closes the arithmetic loop for the central score definition.

P3-E15  
Section: §III E, Table III (eROSITA scores), §III E text  
Problem: Table III lists SBigAE values (e.g. 1.084, 0.815, etc.) for eROSITA anomalies, stating that “the 298-source catalog headline (S > 0.259) is defined” on the canonical S axis. However, the main text earlier describes the 298 anomalies as “0.03% (top 0.03%; data-driven score-knee threshold)” without explicitly linking that 0.259 knee to the reported SBigAE values. Since the SBigAE column in the table spans 0.439–1.084, the reader is forced to infer that 0.259 is indeed the S threshold used to down-select from a larger IF+BigAE pool, but the arithmetic path (how many sources lie between S=0.259 and, say, S=0.439) is never shown. This is a minor but real gap between the headline “S > 0.259” claim and the table’s numerical content.  
Required fix: Add a sentence in §III E explicitly connecting the knee S = 0.259 to the 298-object subset represented in Table III (e.g., “Among 9,303 IF‑selected candidates, 298 objects have SBigAE ≥ 0.259; Table III lists five such sources with SBigAE ranging from 0.439 to 1.084”). That makes clear how the threshold relates to the values shown and to the 0.03% rate.

P3-E16  
Section: §IV B (spatial analysis) vs. §III F / Table V / Appendix F  
Problem: The spatial statistics use “38,330 HEALPix pixels (Nside = 64)” and discuss correlations with Planck dust intensity, but elsewhere the CMB analyses use different resolutions: Planck anomalies are extracted from 64×64 patches and ACT uses Nside = 256 patches in Appendix F. It is not stated whether the HEALPix Nside=64 map of anomalies was constructed by counting anomalies per pixel from all surveys (which have very different native resolutions) or by some resampling/weighting. The omission makes it unclear how the count-per-pixel map used in the χ² and correlation tests relates to the CMB patch geometry and survey footprints, i.e. a dimensional consistency / construction issue for the spatial statistic.  
Required fix: In §IV B, briefly describe how the Nside=64 anomaly map is constructed (e.g., “we bin all point-source anomalies into an Nside=64 HEALPix map by simple counts per pixel; Planck patches are assigned to the Nside=64 pixel containing their central coordinate; ACT is excluded”). Specify that this aggregation ignores differences in survey resolution and uses only sky position, so that the reader can understand what the χ² and correlation refer to.

P3-M7  
Section: §IV A (novelty), Fig. 5, Conclusions §VII  
Problem: The paper repeatedly juxtaposes the aggregate 58.8% SIMBAD-unmatched fraction with the 17.8% “genuine novelty fraction” from the DESI top‑1,000 sample, but there is no explicit quantified statement of how these two relate statistically (e.g., confidence intervals, expected selection bias when going from full catalog to top‑1,000). In §IV A you say “Extended archival cross-matching reduces the headline novelty pool by a factor of ∼ 5.6×,” but the reader never sees a formal uncertainty estimate on the 17.8% as an estimator of the novelty rate at that score stratum, nor a clear warning against extrapolating it to the full catalog beyond a qualitative “no upper/lower-bound status.” This is a subtle but important missing rigor point in how the rates are compared.  
Required fix: Add a short quantitative discussion in §IV A that treats 178/1,000 as a binomial proportion: quote its standard error (≈1.2%) and a 68% or 95% confidence interval for the top‑1,000 stratum. Explicitly state that, because the sample is selected by score, this interval is not a valid confidence interval for the full catalog’s novelty rate and should not be extrapolated. This will make the “5.6× reduction” and the non-comparability with 58.8% quantitatively precise rather than only qualitative.

P3-M8  
Section: §V A (NANOGrav bounce consistency), Appendix E  
Problem: The paper gives a single NANOGrav-based γ measurement, γ = 2.567 ± 0.382, and then compares γ=3.0 and 4.33 as +1.13σ and +4.61σ deviations, and quotes a Bayes factor BMB/SMBHB = 7.14×10³. However, no explicit check is made that the σ used for the ±1.13σ is the same as the one used in the Bayes factor calculation, or how sensitive these numbers are to the choice of prior bounds [0,7] and [−18, −11]. Since the Bayes factor is a null-procedure quantity sensitive to the prior volume, comparing “σ‑shifts” and B values side‑by‑side without an explicit “not directly comparable” qualifier risks overinterpreting the consistency between them.  
Required fix: In §V A, add one sentence clarifying that the σ‑based significance levels (1.13σ, 4.61σ) refer to the marginal posterior for γ, whereas the Bayes factors depend additionally on the adopted uniform priors over γ and log10A and are not directly comparable to simple σ distances. Explicitly note that alternative prior ranges would change BMB/free and BSMBHB/free, even if the posterior mean and σ remain nearly unchanged.

P3-N7  
Section: Abstract and §VII (Conclusions)  
Problem: The abstract and conclusions both claim “the largest multi-archive anomaly search reported to date” and “This is ∼ 141× the largest prior single-survey catalog ,” but beyond Liang et al. and Baron & Poznanski no systematic literature survey is given for other recent large-scale anomaly efforts in spectroscopic or time-domain surveys (LSST simulations, ZTF, other DESI EDR/DR1 anomaly work, etc.). Your initial review flagged the “largest prior single-survey catalog” part (P3-E1, P3-N1), but not the parallel “largest multi-archive anomaly search” language, which is an even broader claim. There is no supporting comparison to any other multi‑archive or multi‑survey anomaly searches, so this remains unsubstantiated.  
Required fix: Soften or qualify the “largest multi-archive anomaly search reported to date” language. For example, change to “to our knowledge, the largest *spectroscopic+photometric multi-archive* anomaly search in the literature, explicitly extending the DESI EDR work of Liang et al. and Nicolaou et al.” Alternatively, add a short paragraph in the Introduction explicitly surveying multi-survey anomaly catalogs (if any) and arguing why this work exceeds them in scale; otherwise, avoid unqualified “largest” claims.

P3-N8  
Section: §V C (systematics) and §VI C (limitations)  
Problem: Statements such as “General-relativistic projection corrections contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1 (plane-parallel monopole, sub-% of b; §VI D(e))” and “the forecast assumes zero observational systematics” are presented without a numerical comparison to the size of the forecasted improvement (7.9%) and without a clear “not directly comparable” qualifier when σ values from different systematics assumptions are mentioned. For example, you describe a 4n+1 nuisance-parameter Fisher block, but do not actually show the σ(fNL) obtained with all systematics included, so the reader is left to mentally compare a “clean” σ=8.14 with statements about tiny ∆σ/σ from GR effects and fiber systematics. This can hide the fact that some σ values are for idealized configurations, others include nuisance parameters.  
Required fix: When quoting σ(fNL) in §V, explicitly state which σ includes which systematics (e.g., “σ(fNL)=8.14 in the no‑systematics Fisher; including the 4n+1 nuisance block with fiducial priors increases σ(fNL) by X%, to Y; GR projection corrections further change σ by <0.02%”). If you have not computed the full σ with all nuisance parameters, say so explicitly and add a short sentence warning that σ values shown for different systematics assumptions are not strictly comparable.

P3-N9  
Section: §III C (SDSS DR18), Fig. 2 right panel, Fig. 3 caption  
Problem: The SDSS cross-transfer description uses colloquial phrases like “extreme-score M7 and T2 dwarfs” and labels scores of S = 5.3×10⁷ and S = 1.9×10¹¹ in Fig. 2 (right panel), but the main text then immediately recommends using the native SDSS re-score (S < 14). The extreme tail values S ~10⁷–10¹¹ are never recomputed or cross-checked against any internal consistency test; they are understood as an artifact but still printed as seemingly precise numbers in the figure and caption. This is a subtle form of “stale numbers”: precise but meaningless artifacts from an explicitly disfavored configuration that might confuse readers who focus on the figure without reading the caveats.  
Required fix: Either (a) downplay the numerical precision of the extreme cross-transfer scores (e.g., by rounding them or labeling them clearly as “nonphysical, architecture‑artifact values”) or (b) remove the explicit 10⁷–10¹¹ labels from Fig. 2 and refer to the tail qualitatively in the text. Make sure that in §III C you explicitly state that these cross-transfer S values are not numerically interpretable and that all quantitative SDSS statements in the paper use the native re-score (S≲14).

If you address these additional points along with the earlier P3-E/M/N items, the manuscript will be materially closer to PRD‑level rigor in its internal arithmetic consistency, the comparability of σ values, and the precision of its novelty and “largest” claims.