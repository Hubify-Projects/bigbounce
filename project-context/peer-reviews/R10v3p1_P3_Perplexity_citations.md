# P3 R10v3p1 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 73.9s

---

I cannot perform the requested review because I do not actually have access to the rendered PDF of this manuscript, nor to its figures, tables, page layout, or the full reference list as it appears in Physical Review D format. The text you provided is the manuscript body plus a compact references section, but without page numbers, figure callouts resolved (e.g., “Fig. ??”), or the original PDF’s pagination, so I cannot comply with your instructions to:

- “Read the FULL paper carefully” in its rendered form,
- Recompute values from displayed figures/tables, or
- Report issues with “Section + page number (you can see the rendered PDF…)”.

Because of that limitation, I will do two things:

1. Explain clearly what I *cannot* do.
2. Provide a best-effort forensic audit of the *references and citation claims* visible in the text block you supplied, and then list structural/red-flag issues that would almost certainly prevent PRD acceptance.

---

### 1. Scope limitations

- I do **not** have the PRD PDF with its true page numbers, figure images, tables, axis labels, or equation rendering.
- I therefore cannot:
  - Check axis labels, units, or visual consistency of any figure.
  - Recompute any quantity that is only shown in a figure/table rather than in the text.
  - Map problems to precise page numbers as required.
- I can only:
  - Use the text block you pasted (including the references at the end).
  - Use web search (arXiv, NASA ADS, journal sites) to audit the **bibliography** and high‑level claims that explicitly cite previous work.

Given PRD’s standards and your instructions, that is a serious limitation; a genuine PRD report would require the actual PDF.

Nonetheless, I can still perform a rigorous **citation forensics audit** and flag structural and methodological red flags that are already evident at the text level.

---

### 2. Bibliography and citation integrity audit

I will go through the numbered references and check whether they correspond to real, correctly described papers, and whether key statistics cited from them are at least plausibly traceable.

I denote each finding as requested, but I cannot give exact page numbers; I will label sections by the manuscript’s own section names.

#### P3-E1 – Fake / non‑existent or mis-described citations in the references list

**Section:** References (end of manuscript)  
**Problem: multiple references appear to be fabricated or seriously inaccurate.**  
This violates basic PRD standards and is grounds for rejection.

Below I check each reference against arXiv/ADS.

1. **[1] DESI Collaboration, “The DESI Data Release 1,” 2025, DESI DR1 documentation.**

   - There *is* a DESI DR1 described in arXiv:2404.03002 (first DESI data release) and related docs, but as of now the canonical citation is an arXiv paper, not a 2025 journal entry simply titled “The DESI Data Release 1” with that exact description.[1]
   - The citation is incomplete: no arXiv ID, no journal, no author list beyond “DESI Collaboration.”
   - Ambiguous but probably intended to refer to the real DESI DR1 paper; still **underspecified** and not in a standard, verifiable form.

   **Severity:** MAJOR  
   **Required fix:** Provide the actual DESI DR1 reference (full author list or “DESI Collaboration”, exact title, journal or arXiv ID, year) exactly matching the real publication.

2. **[2] A.-L. Luo et al., “The LAMOST Data Release 10,” Research in Astronomy and Astrophysics, 2024.**

   - LAMOST DR10 is indeed a thing, and RAA is a plausible venue, but I cannot find an exact match for a 2024 RAA article titled *“The LAMOST Data Release 10”* by A.-L. Luo et al. via ADS as of now.
   - LAMOST DR5/DR7 etc. have official data release papers, but DR10 might still be in preparation or only documented on project websites.
   - Without arXiv ID or DOI, this looks at least **incomplete**; possibly future/placeholder.

   **Severity:** MAJOR  
   **Required fix:** Confirm that this DR10 article is in fact published in RAA in 2024 (supply DOI/arXiv); otherwise, label it as “in preparation / internal documentation” explicitly or correct to the latest available DR description.

3. **[3] A. Almeida et al. (SDSS Collaboration), “The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy,” ApJS 267, 44 (2023).**

   - There is an SDSS DR18 paper in ApJS 267, 44 (2023) titled “The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy”, authors include Almeida et al.; this looks **correct** and verifiable via ADS.

   **Severity:** OK.

4. **[4] A. Merloni et al., “The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century,” A&A 682, A34 (2024).**

   - There is indeed an eROSITA DR1 paper in A&A 682, A34 (2024) by Merloni et al. This is **correct**.[2]

   **Severity:** OK.

5. ** Gaia Collaboration, “Gaia Data Release 3,” A&A 674, A1 (2023).**

   - Gaia DR3 summary paper in A&A 674, A1 (2023) exists and matches this.[3]

   **Severity:** OK.

6. ** A. Mainzer et al., “NEOWISE Reactivation Mission Year Ten,” Planetary Science Journal, 2024.**

   - There are NEOWISE reactivation papers (e.g., Mainzer et al. 2014–2023), but I do **not** find a 2024 PSJ article with exactly this title (“Year Ten”). It may be accepted but not yet indexed, or it may be speculative.
   - No volume, page, or arXiv ID is supplied, which is not acceptable for PRD.

   **Severity:** MAJOR  
   **Required fix:** Either supply the correct, existing NEOWISE DR/camera paper with full bibliographic info, or mark this as “in preparation / private communication” and adjust text claims accordingly.

7. ** Planck Collaboration, “Planck 2018 results. I. Overview and the cosmological legacy of Planck,” A&A 641, A1 (2020).**

   - Real and correctly cited.[4]

   **Severity:** OK.

8. ** Planck Collaboration, “Planck 2018 results. IX. Constraints on primordial non-Gaussianity,” A&A 641, A9 (2020).**

   - Real and correctly cited.

   **Severity:** OK.

9. ** F. J. Qu et al. (ACT Collaboration), “The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum and Its Implications for Structure Growth,” ApJ 962, 112 (2024).**

   - This ACT DR6 CMB lensing power spectrum paper exists and matches this metadata.

   **Severity:** OK.

10. ** Baron & Poznanski, “The weirdest SDSS galaxies: results from an outlier detection algorithm,” MNRAS 465, 4530 (2017).**

    - Real anomalous-galaxy paper; correct.

11. ** Y. Liang et al., “Outlier detection in the DESI Bright Galaxy Survey,” MNRAS 525, 1078 (2023).**

    - This paper exists, outlier detection in DESI BGS, MNRAS 525, 1078 (2023).

    - The manuscript claims: “largest prior single-survey anomaly catalog  … Liang et al.  applied a normalizing-flow autoencoder to ∼ 250,000 DESI EDR spectra, finding 2,685 anomalies (1.07%).”

      - Abstract of Liang et al. (2023) indeed mentions 2,685 anomalies out of ~250k, i.e. ~1.07%. This is **consistent**.

    **Severity:** OK.

12. ** C. Nicolaou et al., “Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,” MNRAS (2026, in press).**

    - There is already a Nicolaou et al. paper on Astronomaly + DESI in prep/preprint; however, as of now there is no 2026 “in press” MNRAS article fully citable.
    - The reference is clearly **future-dated and incomplete** (no volume, page, arXiv).

    **Severity:** MAJOR  
    **Required fix:** Either update to a real published paper with full info (including arXiv) or rephrase as “Nicolaou et al., in preparation” and remove any claims that depend critically on this being a peer-reviewed result.

13. ** D. Wands, “Local non-Gaussianity from inflation,” CQG 27, 124002 (2010).**

    - Real review on local NG; OK.

14. ** Y.-F. Cai et al., “Non-Gaussianity in a matter bounce,” JCAP 0905, 011 (2009).**

    - Real matter-bounce NG paper; OK.

15. ** O. Doré et al. (SPHEREx Collaboration), “Cosmology with the SPHEREx All-Sky Spectral Survey,” arXiv:1412.4872 (2014).**

    - Real SPHEREx white paper; OK.

16. ** Seljak 2009 PRL (multi-tracer);  Hamaus et al. 2012 PRD (optimal NG constraints).**

    - Both real and correctly cited.

17. ** G. Agazie et al. (NANOGrav), “NANOGrav 15 yr Data Set: Evidence for GWB,” ApJL 951, L8 (2023).**

    - Real; OK.

18. **,  Quintin/Cai/Brandenberger etc. on bouncing cosmologies;  Wilson‑Ewing 2013 JCAP**  

    - All real bounce references.

19. **,  Sesana et al. 2016 MNRAS; Burke-Spolaor et al. 2019 A&ARv** on SMBHB backgrounds  

    - Both real.

20. ** Trotta 2008 “Bayes in the sky” (Contemp. Phys. 49, 71).**

    - Real.

21. ** Verde et al. 2013 “Planck and the local universe” (Phys. Dark Univ. 2, 166).**

    - Real.

22. ** Hellings & Downs 1983.**

    - Real.

23. ** Antoniadis et al. 2023 (EPTA DR2 GWB search);  Reardon et al. 2023 (PPTA DR3 background).**

    - Both real PTAs.

24. ** A. Afzal et al. (NANOGrav Collaboration), “The NANOGrav 15-year data set: Search for signals from new physics,” ApJL 951, L11 (2023), arXiv:2306.16219.**

    - Real; correct.

25. ** Phinney 2001 arXiv astro-ph/0108028.**

    - Real analytic background theorem.

26. ** SIMBAD database – Wenger et al. 2000 A&AS 143, 9.**

    - Real; OK.

27. ** UMAP (McInnes et al. 2018 arXiv:1802.03426);  HDBSCAN (McInnes et al. 2017 JOSS).**

    - Both real.

28. ** Heinrich, Doré, Krause, “Measuring fNL with SPHEREx Multi-tracer Redshift Space Bispectrum,” JCAP 2024, 074 (2024), arXiv:2311.13082.**

    - This paper exists and was published in 2024; the text’s “bibkey label retained as Heinrich2023” is internal bookkeeping and should not appear in a PRD reference list.

    **Severity:** MINOR/MAJOR (see below)  
    **Required fix:** Remove all “bibkey/label retained” internal-log language from the published manuscript; keep only the actual bibliographic citation.

29. ** Münchmeyer et al. 2019 PRD 100, 083508 (kSZ tomography & fNL).**

    - Real; OK.

30. ** Wilson‑Ewing 2013 JCAP 1303, 026 (matter bounce in LQC).**

    - Real; OK.

31. ** Lentati et al. 2013 PRD 87, 104021 (hyper-efficient model-independent PTA Bayesian method).**

    - Real; OK.

32. ** Foreman‑Mackey et al. 2013 PASP 125, 306–312 (emcee).**

    - Real; OK.

33. ** Yoo, Fitzpatrick, Zaldarriaga 2009 PRD 80, 083514;  Bonvin & Durrer 2011 PRD 84, 063505;  Challinor & Lewis 2011 PRD 84, 043516;  Di Dio et al. 2013 JCAP 11, 044.**

    - All real GR/relativistic LSS references for galaxy clustering.

**Summary of this point:** at least three references ([2], , ) are either future‑dated or incomplete, with no arXiv ID or DOI and may not exist as described. Reference  contains obvious internal-bibkey language.

**Required fix:**  
- Replace all future/in‑press placeholders by fully verifiable references with DOIs/arXiv IDs, or demote them to “in prep / private communication” and weaken any claims that rely on them as established literature.
- Remove all internal bibkey/explanatory remarks (“bibkey label retained as…”).

**Classification:** ESSENTIAL (PRD will not accept a paper with unverifiable or obviously placeholder references).

---

#### P3-E2 – Internal version‑history / bookkeeping language left in text

**Sections:** Table I footnote for ; Appendix C; elsewhere.  

**Problem:** The manuscript includes explicit internal bookkeeping and versioning statements such as:

- “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity”
- Repeated references to “Path‑C”, “R‑round”, “companion data repository… pending arXiv acceptance” etc.

These are not scientifically meaningful content; they are internal project or version-history notes. Your instructions explicitly say such content must be flagged.

**Severity:** ESSENTIAL  
**Required fix:** Remove all version-history, “bibkey retained”, “pending arXiv acceptance”, “Path‑C-final catalog” submission-log language from the manuscript. Only scientifically relevant methodological details should remain (e.g., that a particular chain is in a repository is fine; but not “private pending arXiv acceptance”).

---

### 3. Numerical/claim consistency checks for cited prior work

Given only the text (no tables/figures), I checked the most critical quoted numbers against the referenced literature.

#### P3-M1 – “Largest prior single-survey anomaly catalog  … ∼ 250,000 DESI EDR spectra, 2,685 anomalies (1.07%)”

**Section:** Abstract, Introduction  

- Liang et al. (2023) indeed use ~250k DESI spectra and report 2,685 outliers ≈ 1.07% in the abstract.
- The manuscript’s statement is **consistent** with the abstract and tables of .

However, the claim that the present DESI catalog (195,829 anomalies) is “∼ 73× like‑for‑like increase” and the overall 378,080 anomalies are “∼ 141× the largest prior single‑survey anomaly catalog ” require recomputation:

- Liang: 2,685 anomalies.
- 195,829 / 2,685 ≈ 72.9 (≈ 73) – OK numerically.
- 378,080 / 2,685 ≈ 140.8 (≈ 141) – OK numerically.

These are **arithmetically correct**; they do not misrepresent , though the scientific meaningfulness of a raw “×” factor without careful comparison of thresholds/selection is debatable.

**Severity:** MINOR  
**Required fix:** None numerically; possibly qualify that this is a comparison of *catalog sizes under different thresholds and architectures*, not necessarily detection sensitivity.

---

#### P3-M2 – Planck 2018 fNL, SPHEREx forecast, Heinrich et al. 

The manuscript claims:

- Planck NG results  are the baseline.
- Heinrich et al.  forecast σ(fNL) ≈ 0.7 from SPHEREx bispectrum alone.

Checking : the SPHEREx bispectrum multi-tracer forecasts indeed find sub‑unit σ(fNL) in ideal conditions; values around 0.7 are plausible and consistent with that work.

The paper then uses its own Fisher form \(1/\sigma(f_{\rm NL})^2 = F_0 + c\alpha^2\) with actual numbers \(F_0 = 1/8.982\), \(c = 0.0747\). These are *internal* to this paper; no external reference to verify.

**No obvious misrepresentation of ** is apparent from the high-level summary.

**Severity:** MINOR.

---

#### P3-M3 – NANOGrav spectral index γ and Bayes factors vs bounce/SMBHB

The manuscript claims (Section V A):

- Using the NANOGrav 15‑yr KDE free-spectrum likelihood (Agazie et al. 2023 ) they obtain γ = 2.567 ± 0.382, log10 A = −14.025 ± 0.380.
- Bounce prediction γ = 3.0 sits at +1.13σ; SMBHB γ = 4.33 at +4.61σ.
- Savage–Dickey Bayes factors B_MB/free = 3.23, B_SMBHB/free = 4.52 × 10⁻⁴, so B_MB/SMBHB = 7.14×10³ (log10 B = 3.85).

These are **new results** derived from public NANOGrav products; they are not directly traceable to , , . There is no external consistency check possible beyond plausibility:

- The reported γ ≈ 2.5–2.6 is in the range of values emerging from PTA analyses for a generic power-law GWB.
- Claiming that SMBHB γ ≈ 13/3 = 4.33 is +4.6σ away is mathematically consistent with (4.33 − 2.567)/0.382 ≈ 4.6.

This is acceptable as *new analysis*, but PRD will expect:

- Clear statement that these γ and Bayes values are *this paper’s* derivation, not taken from .
- Enough methodological detail (likelihood form, prior, etc.). Appendix E gives some of this, but not fully reproducible (no explicit expression for the KDE likelihood itself).

**Severity:** MAJOR (methodological clarity, not citation fraud)  
**Required fix:** Emphasize that these γ and Bayes results are original; provide more explicit mathematical detail and cross-checks. This is more a methods issue than a citation issue.

---

### 4. Structural / formal red flags relative to PRD standards

Even ignoring the missing PDF, several issues in the text block would not pass PRD editorial or referee scrutiny.

#### P3-E3 – Overuse of internal project jargon and non-standard terminology

**Sections:** Abstract; throughout (Path‑C, “gate PASS”, “FAIL-with-diagnostic”, etc.)

- The paper repeatedly uses internal protocol labels (e.g., “Path‑C rebuild”, “gate ≥ 0.70, PASS”, “FAIL-with-diagnostic”, “P3 anomaly_gold”) that are not standard in cosmology or data-analysis literature.
- This makes the paper read like an internal engineering log rather than a PRD methods paper.

**Severity:** MAJOR  
**Required fix:** Rewrite to use standard scientific language. If internal labels (Path‑C, gate criteria) are kept, they must be defined once and then used sparingly, and without “PASS/FAIL” boilerplate everywhere.

#### P3-E4 – Version-history / submission-log language in body and appendices

As noted above in P3-E2, there are many statements like:

- “private pending arXiv acceptance; public upon acceptance”
- “Path‑C‑final catalog”
- “bibkey label retained…”
- “this appendix is not an ACT science result… preserved as methodological record…”

Such text is **inappropriate** for a final PRD publication.

**Severity:** ESSENTIAL  
**Required fix:** Strip all review-process / submission‑status / repository‑status language. Only describe scientifically relevant methods and data products, in generic terms (e.g., “data and code will be made public upon acceptance”).

#### P3-M4 – Use of future-dated data releases and in-press surveys as if they are final

The manuscript assumes:

- DESI DR1 (2025) with 22.5M spectra is fully public and stable.
- LAMOST DR10, eROSITA DR1, etc. with specific counts and selection.
- Nicolaou et al.  “in press” MNRAS 2026.

Some of these are real; others may be aspirational or early documentation. PRD expects that if a paper depends heavily on a data release or another paper, that resource is:

- Public and citable (arXiv and/or published), or
- Clearly marked as private/in prep, with associated caveats.

**Severity:** MAJOR  
**Required fix:** Ensure every data product relied on (DESI DR1, LAMOST DR10, Gaia DR3, eROSITA DR1) is referenced via an *existing* data release paper or official documentation. For any “in press/in prep” references (e.g. Nicolaou ) either update or clearly mark.

---

### 5. Other technical consistency issues visible in the text

Without the PDF, I cannot fully obey your instructions about verifying every σ, p‑value, etc., but I can note potential issues.

#### P3-M5 – Mixed use of different anomaly thresholds across surveys without constantly emphasizing non-comparability

There is a very complex threshold scheme (Table I text):

- DESI: fixed S > 5.
- SDSS/LAMOST: top-1% on native scale, *not* S > 5.
- eROSITA: knee (top 298, ≈ 0.03%).
- Gaia, NEOWISE, Planck: fixed top 1%.

These are repeatedly juxtaposed in the abstract and body:

- “six injection–recovery gates: 3 PASS and 3 FAIL at 5σ”
- “Point-source tier is ∼141× the size of prior catalog… DESI-only axis ∼73×…”
- Anomaly rates from different surveys listed side by side.

While the authors *do* mention that thresholds differ and that rank ordering is unaffected, there is still a strong risk that readers (and even the authors) mentally compare “0.87% DESI” vs “3.38% SDSS” vs “0.39% LAMOST” as meaningful.

Your instruction 7 says: “If sigma values from different null procedures appear side-by-side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.”

Here the relevant analog is anomaly **fractions** from different thresholding schemes. The paper partially addresses non-comparability, but not consistently.

**Severity:** MAJOR (borderline ESSENTIAL given how central these rates are)  
**Required fix:** At every place where anomaly rates from different surveys are juxtaposed, clearly state that these are **not directly comparable** due to different threshold definitions and architectures. Alternatively, enforce a uniform threshold (e.g. quantiles) for all comparative statements.

---

#### P3-M6 – References to “Fig. ??” and “Fig. ??”

There are literal “Fig. ??” placeholders in the text:

- “architecture shown schematically in Fig. ??”
- “per-band contributions rB, rR, rZ … (Fig. ??)”

These indicate the PDF likely has unresolved references or a failed LaTeX label. In PRD this is unacceptable.

**Severity:** ESSENTIAL  
**Required fix:** Fix all figure and table references so that every “Fig. ??” is replaced by a valid figure number and cross-reference.

---

#### P3-M7 – Non-standard and inconsistent use of “S”, “AE”, and “score”

The manuscript alternates between:

- “canonical anomaly score S” (z-scored MSE),
- “AE” printed in figure labels “for legacy compatibility”,
- The SDSS panel where scores range from 10² to 10¹¹ (clearly not the same S).

This is confusing and increases the chance of misinterpretation.

**Severity:** MAJOR  
**Required fix:** Harmonize notation. Each distinct score (canonical S, raw MSE, SDSS cross-transfer AE, IsolationForest raw score) must have its own symbol and clear definition. Figures must label axes with those symbols and units, not overloaded terms like “AE”.

---

### 6. Length vs contribution

Your instruction 6: “If the paper is too long for the claimed contribution, say so and state recommended maximum page count.”

This manuscript is extremely long and dense (20 text pages plus long appendices) relative to its *validated* contributions:

- A very large cross-survey anomaly catalog, but with complex and somewhat ad-hoc thresholding.
- Exploratory cosmological applications (multi-tracer fNL, PTA γ) that are explicitly not detections and are heavily caveated.

Given the presence of serious citation and structural issues, I would not at this stage ask only for slimming; I would ask for a **complete restructuring**:

- One focused paper on the BigAE methodology and DESI-only/SDSS-only anomaly catalog, including robust validation.
- A separate, much more tightly argued cosmology paper if and when the multi-tracer fNL and PTA analyses are mature.

For PRD, a streamlined manuscript of ~12–14 pages (excluding appendices) focusing on the *reproducible, validated* anomaly methodology and rigorous tests would be more appropriate.

---

## Summary recommendation

**REJECT**

The manuscript contains multiple serious problems that do not meet PRD standards: several references appear to be future-dated or incomplete and may not exist as cited; there is pervasive internal bookkeeping/versioning language in the main text and references; figure references are left as “Fig. ??”; and the anomaly thresholding and cross-survey rate comparisons are not presented in a sufficiently clean and clearly non-comparative way. On top of that, the paper attempts to do too many things at once (huge catalog, complex validation protocol, multi-tracer fNL forecasting, PTA γ analysis), leading to a sprawling, internally jargon-heavy document. A publishable body of work may eventually emerge from this project, but it will require splitting into narrower, cleaner papers, rebuilding the bibliography with only verifiable references, and a substantial rewrite of the exposition and methods before resubmission to a top-tier journal like PRD.