# P3 R10v3 — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations
**Total findings (across all reviewers)**: 50
**Distinct consensus groups**: 9

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 0 | 0 | 0 | 0 |
| Grok_brutal | 0 | 0 | 0 | 0 |
| OpenAI_methodology | 6 | 6 | 5 | 3 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `audit_artifact` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P3-E6/ESSENTIAL]**: P3-E6   Multiple sections.  Version-history language inside main text     • “v3 native-PDF cross-vendor review”, “v3.1.75”, “R7”, “R8”, “Path-C-final” appear in body and figure captions.     • Fix: remove all internal revision tags; journal policy forbids exposing the review history to the archival record.  -------------------------------------------------------------------------------

### `table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P3-E2/ESSENTIAL]**: P3-E2   Abstract & Sec. V, p. 10.  Confusion of σ units propagates throughout     • The baseline “single-tracer σ(fNL)_std = 8.98” is dimensionally inconsistent with F₀ = 1/8.982 used in Eq. (…)  (see E1).  Every downstream envelope (e.g. “[3.92, 8.98]”) inherits the same error.     • Fix: Propagate the corrected Fisher algebra globally (abstract, conclusions, Table IV, Fig. 8, Appendix C).

### `length` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P3-M6/MAJOR]**: P3-M6   Whole manuscript.  Page count is excessive for a catalog description; many paragraphs repeat the same caveats verbatim.     • Recommend ≤ 15 journal pages; move appendices F and most of §VI D to Supplementary Material.  -------------------------------------------------------------------------------

### `table_ii` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P3-m2/MINOR]**: P3-m2  Table III, p. 8.  Declination column mis-labelled “Dec” but numbers are negative latitudes (should be degrees).  Add units.

### `companion` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P3-M2/UNKNOWN]**: P3-M2 (MAJOR) – Duplicate phrases and obvious copy‑paste artifacts, multiple pages   Problem: There are clear duplicated phrases and copy/paste remnants, e.g.   – Section II D: “reproducibility scripts are publicly released” followed by “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”   – Table I footnote § discussing eROSITA IF overlap uses “the earlier ‘strict subset’ framing is replaced with this exact 284/298 = 95.3% overlap” referencing earlier drafts not present.   These indicate unedited prior-iteration text.  …
- **[Perplexity_citations/P3-M8/UNKNOWN]**: P3-M8 (MAJOR) – Internal “earlier framing” and “sensitivity-check artifact” language, Sections II D, III, IV   Problem: Phrases like “the earlier ‘strict subset’ framing is replaced with this exact 284/298 overlap” and “the 8‑way‑with‑ACT variant … is preserved as a sensitivity-check artifact” are traces of internal version tracking. They may confuse readers into thinking a previous published version exists.   Required fix: Rewrite these to neutral, present-tense descriptions (“We find 284/298 overlap”, “We also computed an 8‑survey variant including ACT, documented in the Supplement”) and rem…

### `companion,audit_artifact` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P3-M1/UNKNOWN]**: P3-M1 (MAJOR) – Internal version/audit language, throughout   Problem: The manuscript repeatedly uses internal versioning and audit phrases: “Path-C rebuild,” “Path-C native retrain,” “R7/R8/R-round” style terminology in spirit (e.g. “Path-C-final catalog,” “quarantined as a cross-transfer artifact,” “sensitivity-check artifact,” “companion data repository,” “private pending arXiv acceptance”). These read like internal project-tracking notes rather than neutral scientific prose.   Required fix: Keep the description of the methodology (native retrains, quarantine criteria) but remove internal p…

### `companion,duplicate_phrase` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P3-N2/UNKNOWN]**: P3-N2 (NIT) – Duplicate phrase “reproducibility scripts shipped…” Section II D   Problem: The clause “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)” is clearly duplicated.   Required fix: Remove the repeated phrase.

### `sigma_mixing` — UNKNOWN — _single-reviewer_ (1 reviewer)

Reviewers: Perplexity_citations

- **[Perplexity_citations/P3-E4/UNKNOWN]**: P3-E4 (ESSENTIAL) – Reference  Heinrich et al., page 19   Problem: The bib entry says “J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].” Searching arXiv:2311.13082 shows the title “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum” with JCAP 2024 publication, which matches. However, the citation shorthand “Heinrich et al.  (σ(fNL) ≈ 0.7 bispectrum-only forecast)” suggests this σ value is explicitly from their abstract or tables. Inspecting the pap…

## Other findings (41)

- **[Grok_brutal/P3-E1/UNKNOWN]**: **P3-E1 (ESSENTIAL)**   Section: Abstract (p. 1)   Problem: The abstract states “a genuine novelty fraction of ~17.8%” for the top-1,000 DESI anomalies after CDS X-Match against 20 catalogs. The body (p. 9, §IV A) shows this 17.8% (178/1,000) is obtained only after the 7-way 5″ deduplication and only for the DESI top-1,000 stratum; it is never recomputed for the final 378,280-object catalog.   Req…
- **[Grok_brutal/P3-E2/UNKNOWN]**: **P3-E2 (ESSENTIAL)**   Section: Abstract + §V B (p. 10)   Problem: Abstract quotes \(\sigma(f_{\rm NL})=8.14\) (with 1\(\sigma\) envelope [3.92,8.98]) and states “7.9% improvement.” The body derives this from inserting an empirical \(\alpha_{jk}=0.19\pm0.65\) into the Fisher form. No statement appears that this \(\sigma\) is not directly comparable to the single-tracer baseline \(\sigma(f_{\rm NL…
- **[Grok_brutal/P3-E3/UNKNOWN]**: **P3-E3 (ESSENTIAL)**   Section: Abstract + Table I (p. 7)   Problem: Abstract headline number 378,280 is the Path-C unique count after native retrains and 7-way deduplication. Table I footnote ¶ shows the cross-transfer baseline was 319,443 detections; the 378,280 figure therefore includes objects that only survive after per-survey native retraining. The abstract presents 378,280 as the primary r…
- **[Grok_brutal/P3-M1/UNKNOWN]**: **P3-M1 (MAJOR)**   Section: §II D & §III D (pp. 3–4)   Problem: The Path-C “native retrain” protocol is presented as the core methodological advance, yet 98% of the LAMOST anomalies are later shown to be blue-excess training artifacts (p. 4). The paper therefore simultaneously claims the retrain solves cross-survey bias and demonstrates that the same retrain fails catastrophically on one of the s…
- **[Grok_brutal/P3-M2/UNKNOWN]**: **P3-M2 (MAJOR)**   Section: Fig. 1 & §III (p. 4)   Problem: The spatial map shows strong concentration of eROSITA anomalies at the LMC and of Planck/ACT anomalies along the Galactic plane. No per-survey selection-function weights or completeness maps are supplied, so the reader cannot judge whether the reported anomaly surface density is astrophysical or an artifact of survey depth and masking.  …
- **[Grok_brutal/P3-M3/UNKNOWN]**: **P3-M3 (MAJOR)**   Section: §V A (p. 10)   Problem: The NANOGrav 15-yr KDE posterior \(\gamma=2.567\pm0.382\) is compared with the matter-bounce prediction \(\gamma=3.0\) and labeled “+1.13\(\sigma\) (marginally consistent).” The same paragraph reports the SMBHB index \(\gamma=4.33\) at +4.61\(\sigma\). No joint posterior or model-comparison statistic is given; the two statements are therefore no…
- **[Grok_brutal/P3-N1/UNKNOWN]**: **P3-N1 (NIT)**   Section: Title page (p. 1)   Problem: “(Dated: June 2026)” appears in the author block.   Required fix: Replace with the actual submission or revision date.
- **[Grok_brutal/P3-N2/UNKNOWN]**: **P3-N2 (NIT)**   Section: Throughout   Problem: Repeated use of the non-standard abbreviation “Path-C” without an explicit expansion on first use in the abstract.   Required fix: Define on first appearance.  **Summary recommendation**
- **[OpenAI_methodology/P3-E1/ESSENTIAL]**: P3-E1   Sec. V, p. 10.  Fisher forecast arithmetic error     • Text: “inserting this into the Fisher-positivity-respecting form 1/σ(fNL)² = F₀ + c α² … gives … σ(fNL)=8.14 … (7.9 % improvement consistent with no improvement).”     • Problem: With the published F₀ = 1/8.982 = 0.1113 and c = 0.0747 the insertion α = 0.19 gives        1/σ² = 0.1113 + 0.00270 = 0.1140 ⇒ σ = √(1/0.1140)=2.96, not 8.14.…
- **[OpenAI_methodology/P3-E3/ESSENTIAL]**: P3-E3   Sec. IV A, p. 9.  “Genuine novelty fraction = 17.8 % … SIMBAD-unmatched = 58.8 %” juxtaposed without warning     • The paper requires, per journal policy, an explicit statement each time heterogeneous “novelty” metrics are placed side-by-side that they are not directly comparable (§8 of the review instructions).  The first paragraph of IV A does this correctly, but the abstract and Fig. 5 …
- **[OpenAI_methodology/P3-E4/ESSENTIAL]**: P3-E4   Sec. II D, p. 3.  Training-sample leakage     • The DESI DR1 autoencoder is scored on the 47 000 spectra that were used for training.  Although k-fold Jaccard is provided, this still violates standard unsupervised OOD protocol and the leakage is not disclosed in the abstract.     • Fix: (i) state prominently in abstract and method that the production DESI scores include the training set; (…
- **[OpenAI_methodology/P3-E5/ESSENTIAL]**: P3-E5   Sec. III C, p. 5.  SDSS threshold S ≥ 0.1060 (top-1 %) is only 0.11 σ above the mean     • At such a low threshold >10 % of the training distribution are by definition “anomalous”.  This contradicts the claim that the detector isolates outliers and undermines the cross-survey comparison.     • Fix: justify statistically why 0.11 σ constitutes an anomaly or raise the cut to a demonstrably o…
- **[OpenAI_methodology/P3-M1/MAJOR]**: P3-M1   Abstract & Sec. II B.  Number rounding mismatch     • 0.87 % of 22 504 897 should be 195 793, not 195 829 (36 objects difference).  Check all later re-uses.
- **[OpenAI_methodology/P3-M2/MAJOR]**: P3-M2   Table I, footnote ♡, p. 7.  Three incompatible SDSS anomaly counts (77 905, 19 253, 12) are all labelled “headline” at different points.     • Provide one clearly defined catalog count; relegate exploratory cuts to appendix.
- **[OpenAI_methodology/P3-M3/MAJOR]**: P3-M3   Sec. III D, p. 6.  “LAMOST native 113 342 … retained as exploratory tier” but the same objects are included in the 378 280 headline unique count.     • Either exclude exploratory tiers from the headline or create two clearly separated catalog products.
- **[OpenAI_methodology/P3-M4/MAJOR]**: P3-M4   Fig. 7, p. 13.  The same “FAIL” label is applied to surveys that meet none of the gate criteria (LAMOST 5.8 %, Gaia 5.2 %) and to emission-line variants that were never part of the official gate.  The legend is misleading.     • Replot with separate symbols for gate-tests and informal diagnostic variants.
- **[OpenAI_methodology/P3-M5/MAJOR]**: P3-M5   Sec. V A, p. 11.  Bayes factors quoted without prior specification     • The prior on γ is said to be flat in [0,7], but the choice on log₁₀A is not given.  Provide full prior listing and numerical evidence for Savage–Dickey ratios.
- **[OpenAI_methodology/P3-m1/MINOR]**: P3-m1  Abstract.  “seven retained archives … ACT DR6 quarantined” – but ACT figures are still shown in Fig. 1 caption (“8 archives”).  Remove ACT from graphics or mark it “quarantined”.
- **[OpenAI_methodology/P3-m3/MINOR]**: P3-m3  Sec. III E, p. 6.  “top-1” should read “top-1 %”.
- **[OpenAI_methodology/P3-m4/MINOR]**: P3-m4  Eq. (2), p. 2.  The σ_val symbol is not defined until later in the paragraph; add definition immediately after Eq. (2).
- **[OpenAI_methodology/P3-m5/MINOR]**: P3-m5  Appendix E, p. 15.  The symbol “ρ_i” is undefined.  -------------------------------------------------------------------------------
- **[OpenAI_methodology/P3-n1/NIT]**: P3-n1  Multiple pages.  “cross-transfer” is hyphenated and un-hyphenated inconsistently.
- **[OpenAI_methodology/P3-n2/NIT]**: P3-n2  Page 10: “positivity-respecting” appears twice in one sentence.
- **[OpenAI_methodology/P3-n3/NIT]**: P3-n3  References [33] and [34] year mismatch (2024 in body, 2023 in bibkey).  ------------------------------------------------------------------------------- ## Summary recommendation
- **[Perplexity_citations/P3-E1/UNKNOWN]**: P3-E1 (ESSENTIAL) – Abstract, page 1   Problem: The paper is dated “(Dated: June 2026)” and contains forward‑looking claims (e.g. SPHEREx forecasts, NANOGrav 15‑yr analysis) as if they were completed published work. There is no arXiv ID given for this manuscript itself, and several key results (e.g. “Astronomaly … in press”, “SPHEREx JCAP 2024”, “NANOGrav search for signals from new physics”) are …
- **[Perplexity_citations/P3-E2/UNKNOWN]**: P3-E2 (ESSENTIAL) – References [10–12], page 19   Problem: The paper’s main scaling claim—“point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ”—relies on Liang et al. . The reference is given as “Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664” (exact arXiv ID not written but implied). Checking arXiv:2307.07664 confirms title “Outlier detection in…
- **[Perplexity_citations/P3-E3/UNKNOWN]**: P3-E3 (ESSENTIAL) – Reference  SPHEREx, page 19   Problem: SPHEREx is cited as “O. Doré et al., arXiv:1412.4872 (2014)” but then referred to in the text as if forecasting with “Heinrich et al.  (σ(fNL) ≈ 0.7 bispectrum-only forecast).” The SPHEREx white paper is indeed arXiv:1412.4872. However, there is now a more current SPHEREx reference (e.g. updated design and forecasts) and no DOI/venue is su…
- **[Perplexity_citations/P3-E5/UNKNOWN]**: P3-E5 (ESSENTIAL) – NANOGrav references  and , pages 19–20   Problem: Two distinct NANOGrav papers are cited:  as “Evidence for a Gravitational-wave Background” (ApJL 951, L8 (2023)) and  as “Search for signals from new physics,” ApJL 951, L11 (2023). These titles, authors, and venues match the 15‑yr release papers on arXiv:2306.16213 and 2306.16219 respectively. However, the text uses the KDE fre…
- **[Perplexity_citations/P3-E6/UNKNOWN]**: P3-E6 (ESSENTIAL) – Matter-bounce references  & , page 19   Problem: The matter-bounce fNL prediction is cited as “fNL = −35/8 = −4.375 [13, 14, 35].” Cai et al. 2009 (arXiv:0903.0631) and Wilson‑Ewing JCAP 1303, 026 (2013), arXiv:1211.6269 indeed derive large local‑type non‑Gaussianity in matter‑bounce, but the precise value −35/8 is specific to a particular toy model. Wands  is a review on local…
- **[Perplexity_citations/P3-E7/UNKNOWN]**: P3-E7 (ESSENTIAL) – GR number-count papers [38–41], pages 19–20   Problem: The references to relativistic number counts and projection effects—Yoo et al. (2009), Bonvin & Durrer (2011), Challinor & Lewis (2011 PhysRevD.84.043516), Di Dio et al. (2013 CLASSgal)—all exist with those titles, years, and venues, and the bib information matches ADS/APS records. The text claims “General-relativistic proj…
- **[Perplexity_citations/P3-E8/UNKNOWN]**: P3-E8 (ESSENTIAL) – Statistics traceability for σ(fNL), Section V, pages 10–11   Problem: The paper claims a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] and “single-tracer baseline σ(fNL)std = 8.98.” No external paper is cited for these specific numbers—they are the authors’ Fisher forecasts. That is acceptable, but the text also ties them conceptually to Heinrich et al.  and SPHE…
- **[Perplexity_citations/P3-E9/UNKNOWN]**: P3-E9 (ESSENTIAL) – NANOGrav γ significance and Bayes factors, Section V A, pages 11–12   Problem: The paper computes γ = 2.567 ± 0.382 from the NANOGrav KDE free-spectrum and states that the SMBHB prediction γ = 4.33 is “+4.61σ” and that Savage–Dickey gives B_MB/SMBHB = 7.14×10³ (“decisive”). None of these specific numbers appear in any NANOGrav paper; they are the authors’ own MCMC analysis. Cit…
- **[Perplexity_citations/P3-E10/UNKNOWN]**: P3-E10 (ESSENTIAL) – “In press” / future-dated entries, reference , page 19   Problem: Reference  is described as “Mon. Not. Roy. Astron. Soc. (2026, in press).” Searching for “Nicolaou anomaly detection DESI Astronomaly” shows an arXiv preprint with no confirmed 2026 MNRAS volume/page yet. Claiming “in press” and a future year without a DOI or volume is misleading.   Required fix: Change  to “sub…
- **[Perplexity_citations/P3-M3/UNKNOWN]**: P3-M3 (MAJOR) – Abstract scalar consistency and arithmetic, page 1   Problem: Several load‑bearing numbers in the abstract must match the body:   – “37.3 million sources and CMB map patches” vs Table I total 37,292,042. This is consistent to 3 significant figures.   – “378,280 unique anomalies … 378,080 point-source + 200 Planck” vs Table I “Path-C unique”: 378,280, and text: 378,080 point sources…
- **[Perplexity_citations/P3-M4/UNKNOWN]**: P3-M4 (MAJOR) – “Savage-Dickey” and Bayes factor referencing, Section V A   Problem: The manuscript uses Savage–Dickey density ratio to compute Bayes factors B_MB/free and B_SMBHB/free, and then quote B_MB/SMBHB ≈ 7.14×10³ with “decisive on Jeffreys’ scale.” No reference on Savage–Dickey (e.g. Trotta 2008 or standard Bayesian texts) is provided where the method is introduced, and Jeffreys’ scale i…
- **[Perplexity_citations/P3-M5/UNKNOWN]**: P3-M5 (MAJOR) – Reference  and  fusion, Section V, page 10   Problem: The text merges SPHEREx design (Doré et al. ) with Heinrich et al.  multi-tracer bispectrum in a way that suggests a single source for both σ(fNL) ≈ 0.7 forecast and the survey description. In reality, Doré et al. is the SPHEREx mission concept, and Heinrich et al. is a later multi-tracer SPHEREx‑like forecast with its own assum…
- **[Perplexity_citations/P3-M6/UNKNOWN]**: P3-M6 (MAJOR) – Data availability and GitHub/HuggingFace links, page 18   Problem: The data-availability section hardcodes URLs (“https://huggingface.co/datasets/...”; “https://github.com/...”), which PRD generally discourages in the body text. Also, the dataset is “private pending arXiv acceptance; public upon acceptance,” which conflicts with PRD’s preference for available or embargoed but citab…
- **[Perplexity_citations/P3-M7/UNKNOWN]**: P3-M7 (MAJOR) – Multiple threshold families and footnotes, Table I, pages 7–8   Problem: The paper uses survey‑dependent thresholds (S>5, top‑1%, score‑knee cuts) and explains this in a complicated multi‑paragraph footnote to Table I. This makes it hard to compare surveys and to trace which threshold controls which headline number.   Required fix: Promote the threshold definitions from the table f…
- **[Perplexity_citations/P3-N1/UNKNOWN]**: P3-N1 (NIT) – Typographical consistency   Problem: Small stylistic issues: sporadic “fNL ” with a trailing space before the closing parenthesis, inconsistent use of “CMB” vs “CMB ”, extra spaces in “1/σ(fNL )2”, and hyphenation inconsistencies (“multi-survey”, “multi survey”).   Required fix: Run a careful typography and LaTeX pass, standardizing all equations (e.g. \(1/\sigma^2_{f_{\rm NL}}\)), r…
- **[Perplexity_citations/P3-N3/UNKNOWN]**: P3-N3 (NIT) – “Jeffreys’ scale” capitalization, Section V A   Problem: “Jeffreys’ scale” should capitalize the proper name; currently capitalization is inconsistent.   Required fix: Standardize to “Jeffreys’ scale” everywhere.
- **[Perplexity_citations/P3-N4/UNKNOWN]**: P3-N4 (NIT) – “Quasi-matter bounce” vs “matter-bounce” terminology   Problem: Both “quasi-matter bounce” and “matter-bounce” are used in the Introduction and cosmology sections without defining whether they refer to the same class.   Required fix: Add a one-sentence definition early on clarifying whether “quasi-matter bounce” is a subset or a synonym of the matter-bounce models referenced in [14,3…
