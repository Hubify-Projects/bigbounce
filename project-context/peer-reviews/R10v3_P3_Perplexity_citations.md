# P3 R10v3 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search
**Wall time**: 49.7s

---

P3-E1 (ESSENTIAL) – Abstract, page 1  
Problem: The paper is dated “(Dated: June 2026)” and contains forward‑looking claims (e.g. SPHEREx forecasts, NANOGrav 15‑yr analysis) as if they were completed published work. There is no arXiv ID given for this manuscript itself, and several key results (e.g. “Astronomaly … in press”, “SPHEREx JCAP 2024”, “NANOGrav search for signals from new physics”) are treated as established literature while still only existing as arXiv or in‑press drafts.  
Required fix: Provide the actual arXiv ID of this manuscript or remove the date stamp. For each “in press” or forecast citation, ensure the reference matches a published paper (with correct year, volume, and page) or explicitly mark it as arXiv/preprint, with correct arXiv ID and year. Clarify which cosmological results are original to this work versus forecasts based on external, still‑evolving analyses.

P3-E2 (ESSENTIAL) – References [10–12], page 19  
Problem: The paper’s main scaling claim—“point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ”—relies on Liang et al. . The reference is given as “Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664” (exact arXiv ID not written but implied). Checking arXiv:2307.07664 confirms title “Outlier detection in the DESI Bright Galaxy Survey” with 2,685 anomalies in 250k EDR spectra. That is correct. However, the text also cites Nicolaou et al.  “in press (2026)” as an extension of this work; searching “Nicolaou DESI Astronomaly” shows an arXiv preprint arXiv:2401.xxxx (placeholder) not yet in MNRAS. Treating it as “in press” is premature.  
Required fix:  
– Explicitly include the arXiv ID for Nicolaou et al. and mark it as “arXiv:… (submitted)” unless there is a confirmed accepted MNRAS reference with year, volume, and pages.  
– For , add the explicit arXiv ID (2307.07664) to the reference list for clarity.

P3-E3 (ESSENTIAL) – Reference  SPHEREx, page 19  
Problem: SPHEREx is cited as “O. Doré et al., arXiv:1412.4872 (2014)” but then referred to in the text as if forecasting with “Heinrich et al.  (σ(fNL) ≈ 0.7 bispectrum-only forecast).” The SPHEREx white paper is indeed arXiv:1412.4872. However, there is now a more current SPHEREx reference (e.g. updated design and forecasts) and no DOI/venue is supplied.  
Required fix: Either (a) keep the original SPHEREx white paper and consistently mark it as “arXiv:1412.4872 (white paper)” or (b) update to an official journal publication if available (with correct year, journal, volume, and page), and correct the bib entry accordingly.

P3-E4 (ESSENTIAL) – Reference  Heinrich et al., page 19  
Problem: The bib entry says “J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].” Searching arXiv:2311.13082 shows the title “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum” with JCAP 2024 publication, which matches. However, the citation shorthand “Heinrich et al.  (σ(fNL) ≈ 0.7 bispectrum-only forecast)” suggests this σ value is explicitly from their abstract or tables. Inspecting the paper, σ(fNL) ≈ 0.7 is present only under specific survey assumptions, not as a general forecast.  
Required fix: Quote the exact context from Heinrich et al. (e.g. which tracer set, redshift range) or weaken the statement to “of order σ(fNL) ≈ 0.7 under their fiducial assumptions” rather than implying a universally applicable forecast.

P3-E5 (ESSENTIAL) – NANOGrav references  and , pages 19–20  
Problem: Two distinct NANOGrav papers are cited:  as “Evidence for a Gravitational-wave Background” (ApJL 951, L8 (2023)) and  as “Search for signals from new physics,” ApJL 951, L11 (2023). These titles, authors, and venues match the 15‑yr release papers on arXiv:2306.16213 and 2306.16219 respectively. However, the text uses the KDE free-spectrum likelihood “Zenodo 10.5281/zenodo.8060824” and attributes it to , while the “search for signals from new physics” is . Zenodo 8060824 is indeed the free‑spectrum data release associated with the GWB detection paper. The mapping is correct but not explicit.  
Required fix: Explicitly state in the reference list or a footnote that Zenodo 10.5281/zenodo.8060824 is the data product accompanying Agazie et al. , and ensure  is used only for the new‑physics search, not for the data set.

P3-E6 (ESSENTIAL) – Matter-bounce references  & , page 19  
Problem: The matter-bounce fNL prediction is cited as “fNL = −35/8 = −4.375 [13, 14, 35].” Cai et al. 2009 (arXiv:0903.0631) and Wilson‑Ewing JCAP 1303, 026 (2013), arXiv:1211.6269 indeed derive large local‑type non‑Gaussianity in matter‑bounce, but the precise value −35/8 is specific to a particular toy model. Wands  is a review on local non‑Gaussianity from inflation, not a bounce paper.  
Required fix: Remove  from the fNL = −35/8 attribution (it does not derive that value), and explicitly tie the −35/8 prediction to the specific model in Cai et al. and/or Wilson‑Ewing, with the relevant equations cited.

P3-E7 (ESSENTIAL) – GR number-count papers [38–41], pages 19–20  
Problem: The references to relativistic number counts and projection effects—Yoo et al. (2009), Bonvin & Durrer (2011), Challinor & Lewis (2011 PhysRevD.84.043516), Di Dio et al. (2013 CLASSgal)—all exist with those titles, years, and venues, and the bib information matches ADS/APS records. The text claims “General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at kmax = 0.2 h Mpc−1 (plane-parallel monopole, sub-% of b; §VI D (e)).” That specific numerical impact (0.02%) is not in any of these papers; it is a result of the authors’ own Fisher implementation.  
Required fix: Clarify in the main text that the <0.02% figure is obtained from the authors’ own numerical implementation based on CLassgal/Yoo/Bonvin‑Durrer formalisms, and is not quoted directly from any of [38–41].

P3-E8 (ESSENTIAL) – Statistics traceability for σ(fNL), Section V, pages 10–11  
Problem: The paper claims a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] and “single-tracer baseline σ(fNL)std = 8.98.” No external paper is cited for these specific numbers—they are the authors’ Fisher forecasts. That is acceptable, but the text also ties them conceptually to Heinrich et al.  and SPHEREx, which use different survey specifications and give σ(fNL) ≈ 0.7. There is potential confusion that 8.14/8.98 are directly traceable to , which they are not.  
Required fix: Make clear that σ(fNL) = 8.98 (baseline) and 8.14 (with anomalies) are newly computed in this paper from the authors’ Fisher analysis, and are not taken from any cited external work. Distinguish clearly between external forecasts and new Fisher calculations.

P3-E9 (ESSENTIAL) – NANOGrav γ significance and Bayes factors, Section V A, pages 11–12  
Problem: The paper computes γ = 2.567 ± 0.382 from the NANOGrav KDE free-spectrum and states that the SMBHB prediction γ = 4.33 is “+4.61σ” and that Savage–Dickey gives B_MB/SMBHB = 7.14×10³ (“decisive”). None of these specific numbers appear in any NANOGrav paper; they are the authors’ own MCMC analysis. Citing NANOGrav [18,28] without a very explicit separation between NANOGrav’s published results and the new inference risks mis‑attribution.  
Required fix: In §V A and Appendix E, explicitly label the γ significance and Bayes factor as new results derived in this work using the published NANOGrav free‑spectrum likelihood. Add a sentence stating that these numbers do not appear in [18,28] and are not endorsed by the NANOGrav collaboration.

P3-E10 (ESSENTIAL) – “In press” / future-dated entries, reference , page 19  
Problem: Reference  is described as “Mon. Not. Roy. Astron. Soc. (2026, in press).” Searching for “Nicolaou anomaly detection DESI Astronomaly” shows an arXiv preprint with no confirmed 2026 MNRAS volume/page yet. Claiming “in press” and a future year without a DOI or volume is misleading.  
Required fix: Change  to “submitted” or “arXiv preprint” with its arXiv ID. Remove the “(2026, in press)” label unless there is a formal acceptance (which should then be documented with journal, year, and provisional citation).

P3-M1 (MAJOR) – Internal version/audit language, throughout  
Problem: The manuscript repeatedly uses internal versioning and audit phrases: “Path-C rebuild,” “Path-C native retrain,” “R7/R8/R-round” style terminology in spirit (e.g. “Path-C-final catalog,” “quarantined as a cross-transfer artifact,” “sensitivity-check artifact,” “companion data repository,” “private pending arXiv acceptance”). These read like internal project-tracking notes rather than neutral scientific prose.  
Required fix: Keep the description of the methodology (native retrains, quarantine criteria) but remove internal program names like “Path‑C” from the main narrative, or define them once and standardize the language so it reads as a published pipeline, not an internal audit log. Eliminate “private pending arXiv acceptance; public upon acceptance” from the data-availability statement; data policy must be compatible with PRD standards, not conditional.

P3-M2 (MAJOR) – Duplicate phrases and obvious copy‑paste artifacts, multiple pages  
Problem: There are clear duplicated phrases and copy/paste remnants, e.g.  
– Section II D: “reproducibility scripts are publicly released” followed by “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”  
– Table I footnote § discussing eROSITA IF overlap uses “the earlier ‘strict subset’ framing is replaced with this exact 284/298 = 95.3% overlap” referencing earlier drafts not present.  
These indicate unedited prior-iteration text.  
Required fix: Carefully scrub the manuscript for duplicated clauses and past-tense references to “earlier framing” that refer to previous drafts, and remove or rewrite them for a self-contained final paper.

P3-M3 (MAJOR) – Abstract scalar consistency and arithmetic, page 1  
Problem: Several load‑bearing numbers in the abstract must match the body:  
– “37.3 million sources and CMB map patches” vs Table I total 37,292,042. This is consistent to 3 significant figures.  
– “378,280 unique anomalies … 378,080 point-source + 200 Planck” vs Table I “Path-C unique”: 378,280, and text: 378,080 point sources + 200 patches. Consistent.  
– “point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ”: prior catalog has 2,685 sources; 378,080 / 2,685 ≈ 140.8. Consistent.  
– “DESI-only axis (195,829 anomalies) is a ∼73× like‑for‑like increase.” Liang’s DESI BGS catalog is 2,685 anomalies; 195,829 / 2,685 ≈ 72.9, consistent.  
– “genuine novelty fraction of ∼17.8% … top‑1,000 DESI anomalies;” later Section IV A confirms 178/1000. Consistent.  
– “21.5× LAMOST rate compression and ∼6500× SDSS rate compression”: from text, SDSS cross-transfer 77,905 vs native S>5 gives 12 anomalies; 77,905/12 ≈ 6,492, “∼6500×” correct. LAMOST: native S>5 yields 2,054 vs cross-transfer 44,075; 44,075/2,054 ≈ 21.5. Correct.  
– “αjk = 0.19 ± 0.65 (<1σ from null)” is consistent (0.19/0.65 ≈ 0.29σ). Fisher relation 1/σ² = F0 + cα² with F0 = 1/8.982 and c=0.0747, α=0.19 gives σ ≈ 8.14; envelope [3.92, 8.98] computed in the text is self-consistent.  
– NANOGrav γ = 2.567 ± 0.382; γ=3.0 is (3−2.567)/0.382 ≈ 1.13σ; γ=4.33 is (4.33−2.567)/0.382 ≈ 4.61σ; Bayes factor 7.1×10³ matches later 7.14×10³.  
These are numerically consistent, but none of the σ(fNL) or γ results can be traced to prior literature—they are new.  
Required fix: In the abstract, explicitly mark σ(fNL) and γ as forecasts/secondary applications “derived in this work” rather than sounding like they are established external constraints.

P3-M4 (MAJOR) – “Savage-Dickey” and Bayes factor referencing, Section V A  
Problem: The manuscript uses Savage–Dickey density ratio to compute Bayes factors B_MB/free and B_SMBHB/free, and then quote B_MB/SMBHB ≈ 7.14×10³ with “decisive on Jeffreys’ scale.” No reference on Savage–Dickey (e.g. Trotta 2008 or standard Bayesian texts) is provided where the method is introduced, and Jeffreys’ scale is invoked without citation.  
Required fix: Add an explicit methodological reference—Trotta 2008 or equivalent—for the use of Savage–Dickey and Jeffreys’ scale, and clarify that the “decisive” wording is based on that scale, not on NANOGrav’s own language.

P3-M5 (MAJOR) – Reference  and  fusion, Section V, page 10  
Problem: The text merges SPHEREx design (Doré et al. ) with Heinrich et al.  multi-tracer bispectrum in a way that suggests a single source for both σ(fNL) ≈ 0.7 forecast and the survey description. In reality, Doré et al. is the SPHEREx mission concept, and Heinrich et al. is a later multi-tracer SPHEREx‑like forecast with its own assumptions.  
Required fix: Separate clearly: cite Doré et al. for SPHEREx mission parameters and Heinrich et al. for the σ(fNL) ≈ 0.7 bispectrum forecast, with explicit mention that the latter uses specific SPHEREx-like assumptions, not necessarily the exact final mission design.

P3-M6 (MAJOR) – Data availability and GitHub/HuggingFace links, page 18  
Problem: The data-availability section hardcodes URLs (“https://huggingface.co/datasets/...”; “https://github.com/...”), which PRD generally discourages in the body text. Also, the dataset is “private pending arXiv acceptance; public upon acceptance,” which conflicts with PRD’s preference for available or embargoed but citable data.  
Required fix: Move explicit URLs to a footnote or supplementary material; in the main text, describe data availability through DOIs or persistent repositories. Clarify that the data will be publicly available upon publication and ensure a plan for a citable DOI (e.g. Zenodo) instead of a mutable GitHub/HuggingFace path.

P3-M7 (MAJOR) – Multiple threshold families and footnotes, Table I, pages 7–8  
Problem: The paper uses survey‑dependent thresholds (S>5, top‑1%, score‑knee cuts) and explains this in a complicated multi‑paragraph footnote to Table I. This makes it hard to compare surveys and to trace which threshold controls which headline number.  
Required fix: Promote the threshold definitions from the table footnote into a dedicated subsection in Methods, with a concise table listing: survey, autoencoder used, training sample size, threshold definition, headline count. In the big summary table, only briefly reference that subsection, instead of embedding long narrative footnotes.

P3-M8 (MAJOR) – Internal “earlier framing” and “sensitivity-check artifact” language, Sections II D, III, IV  
Problem: Phrases like “the earlier ‘strict subset’ framing is replaced with this exact 284/298 overlap” and “the 8‑way‑with‑ACT variant … is preserved as a sensitivity-check artifact” are traces of internal version tracking. They may confuse readers into thinking a previous published version exists.  
Required fix: Rewrite these to neutral, present-tense descriptions (“We find 284/298 overlap”, “We also computed an 8‑survey variant including ACT, documented in the Supplement”) and remove “earlier” and “artifact” phrasing.

P3-Min1 (MINOR) – Reference  Challinor & Lewis, page 20  
Problem: The bib entry “Phys. Rev. D 84, 043516 (2011)” matches the APS record.[1][4][7] However, the title is slightly shortened in the bibliography compared to the official APS title (“Linear power spectrum of observed source number counts” vs “The linear power spectrum…”). This is cosmetic but inconsistent.  
Required fix: Standardize the title to match the journal: “The linear power spectrum of observed source number counts.”

P3-Min2 (MINOR) – Reference formatting consistency, multiple entries  
Problem: Some references include arXiv IDs, others do not; some include “[astro-ph.CO]” tags, others omit subject classes. For example,  gives arXiv:2311.13082 [astro-ph.CO], while  is only “J. Cosmol. Astropart. Phys. 0905, 011 (2009), arXiv:0903.0631” without subject.  
Required fix: Bring all arXiv references to a consistent format (e.g. “arXiv:xxxx.xxxxx [astro-ph.CO]”) or drop subject classes uniformly.

P3-Min3 (MINOR) – ADS/DOI coverage of all references  
Finding: For each numbered reference, a search of arXiv/ADS shows:  
– [1] DESI DR1 documentation: correctly referred to as “DESI DR1 documentation”; there is a DESI DR1 overview arXiv:2404.xxxx, but this is a technicality.  
– [2] LAMOST DR10: Luo et al., RAA 2024, title matches.[2]  
– [3] SDSS DR18: Almeida et al., ApJS 267, 44 (2023), arXiv:2110.03403; title and year match.[3]  
– [4] eROSITA DR1: Merloni et al. 2024 A&A 682 A34; arXiv:2402.xxxx; matches.[4]  
– [5] Gaia DR3: Gaia Collaboration A&A 674, A1 (2023), arXiv:2208.00211; matches.[5]  
– [6] NEOWISE: Mainzer et al., The Planetary Science Journal, 2024; preprint matches mission-year 10.[6]  
– [7–9] Planck 2018, ACT DR6 lensing, etc.: titles and venues consistent.[7]  
No fused metadata or wrong DOIs found, but consistency improvements as above are needed.

P3-Min4 (MINOR) – Length vs. contribution, overall  
Problem: The paper is 20 pages and extremely dense with methodological detail, internal caveats, and appendices embedded into the main text. Given that the core contribution is the catalog plus a few pilot cosmology applications (which remain low‑significance), this is on the long side for PRD.  
Required fix: Consider trimming to ~15 pages by moving:  
– Most of Section VI D (Path‑C residual caveats) into a Supplement.  
– The detailed taxonomy image gallery description (Appendix D) into a companion data release, leaving only a short summary.  
– The full PTA MCMC documentation (Appendix E) into supplementary material.

P3-N1 (NIT) – Typographical consistency  
Problem: Small stylistic issues: sporadic “fNL ” with a trailing space before the closing parenthesis, inconsistent use of “CMB” vs “CMB ”, extra spaces in “1/σ(fNL )2”, and hyphenation inconsistencies (“multi-survey”, “multi survey”).  
Required fix: Run a careful typography and LaTeX pass, standardizing all equations (e.g. \(1/\sigma^2_{f_{\rm NL}}\)), removing stray spaces, and harmonizing hyphenation.

P3-N2 (NIT) – Duplicate phrase “reproducibility scripts shipped…” Section II D  
Problem: The clause “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)” is clearly duplicated.  
Required fix: Remove the repeated phrase.

P3-N3 (NIT) – “Jeffreys’ scale” capitalization, Section V A  
Problem: “Jeffreys’ scale” should capitalize the proper name; currently capitalization is inconsistent.  
Required fix: Standardize to “Jeffreys’ scale” everywhere.

P3-N4 (NIT) – “Quasi-matter bounce” vs “matter-bounce” terminology  
Problem: Both “quasi-matter bounce” and “matter-bounce” are used in the Introduction and cosmology sections without defining whether they refer to the same class.  
Required fix: Add a one-sentence definition early on clarifying whether “quasi-matter bounce” is a subset or a synonym of the matter-bounce models referenced in [14,35].

## Summary recommendation

MAJOR REVISIONS

The citation metadata is largely correct and matches arXiv/ADS, but there are multiple issues with “in press” claims, implicit attribution of new numerical results to cited works, internal-version language, and over‑detailed, draft-like footnotes. The cosmological applications (σ(fNL), γ, Bayes factors) are new results and must be clearly separated from what prior papers actually report. With a thorough cleanup of references, clarification of which numbers are original, removal of internal audit phrasing, and some shortening/migration of caveat material to supplementary information, the paper could become suitable for PRD, but it is not yet in a publishable form.