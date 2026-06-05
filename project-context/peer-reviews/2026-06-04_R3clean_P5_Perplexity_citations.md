# P5 2026-06-04_R3clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.3s

---

The manuscript as provided cannot yet be meaningfully audited for citation correctness, because most of the “citations” are to the author’s own internal drafts, pipelines, or to future/companion papers whose arXiv/ADS entries do not exist. Where it cites external literature, some items are real and check out, but several show problems or unverifiable claims. Below I focus strictly on what can be checked against arXiv/ADS and standard databases.

I use “P5-Ex” = ESSENTIAL, “P5-Mx” = MAJOR, “P5-mx” = MINOR, “P5-nx” = NIT.

---

### 1. Global issues with the reference list

**P5-E1 (ESSENTIAL)**  
**Location:** References [3], [4]; throughout text (Paper II/IV mentions, first page & §II, §VIII, Appendix B).  
**Problem:** References [3] and [4] are not standard literature references but are effectively internal version-controlled notes. They explicitly lack arXiv IDs and peer review, yet the paper uses them as if they were citable sources of key quantitative results:

- [3] “A Survey-Scale Chirality Catalog of 8.47M Galaxies… companion paper (Paper IV), in preparation; manuscript and reproducibility artifacts at pipelines/p2_chirality/… Internal companion artifact; an arXiv identifier will be assigned upon Paper IV submission.”
- [4] “fN L = −35/8 Forecast… companion paper (Paper II)… Internal companion artifact; an arXiv identifier will be assigned upon Paper II submission.”

No arXiv or journal identifiers exist, and the “pipelines/…” paths are internal repository paths, not public data products. The entire analysis in P5 assumes as input the catalog and monopole values from Paper IV, yet that work is not externally accessible in the way required by PRD/MNRAS standards.

**Required fix:**  
- Either (a) post Paper IV and Paper II to arXiv (with stable versions) and update the references to proper arXiv IDs, or (b) reframe P5 as fully self-contained: include a concise but complete description of the chirality catalog generation, and explicitly reproduce the monopole calculations within P5, so that no unpublished, inaccessible work is load-bearing.  
- Remove all internal path references (“pipelines/p2_chirality/…”) from the references section; if you want to provide code/data, describe a public repository (e.g. GitHub/Zenodo/DOI).  
- Until Paper IV is public, clearly state that the catalog and monopole calibration are not independently verifiable, and adjust claims in the abstract/introduction to reflect that P5’s conclusions are conditional on that unreviewed input.

---

**P5-M1 (MAJOR)**  
**Location:** References  and ; §IX B, §X, abstract robustness discussion.  
**Problem:** You cite two “concurrent” DESI DR1/EDR cosmic-web papers:

-  “H. I. Ullah et al., ‘Cosmic-web quenching with DESI DR1: T-Web environments…’ preprint (2026), arXiv:2604.02463.”
-  “D. C. Zapata-Zuluaga et al., ‘The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,’ (2026), arXiv:2604.01456.”

At the time of this review, neither arXiv:2604.02463 nor arXiv:2604.01456 resolves; the IDs are in the future and not present on arXiv/ADS. I cannot verify titles, authors, or claims. These look like **fused / fabricated future metadata**.

**Required fix:**  
- Replace these with real, existing arXiv IDs and check that the titles/authors/claims match what you say. If these works are not actually online, you must label them explicitly as “private communication” or “in preparation” and avoid treating them as public validation.  
- Remove any specific numerical comparisons to  and  unless they can be traced to a published or publicly archived preprint. At best these should be described qualitatively as “preliminary independent DR1/EDR cosmic-web analyses (private comm.)” with no arXiv IDs.

---

**P5-M2 (MAJOR)**  
**Location:** References section; [5], [6], , , , , .  
**Problem:** For the genuine external references, you do not give full bibliographic information systematically, and it is not clear in several places that the numbers you quote are traceable to those papers.

Cross-check (using arXiv/ADS):

- [5] Hahn et al. 2007 MNRAS 375, 489 (“Properties of dark matter haloes in clusters, filaments, sheets and voids”). ✔ Title, venue, year, page, arXiv:astro-ph/0610280: correct.
- [6] Hoffman et al. 2012, MNRAS 425, 2049, arXiv:1201.3367: kinematic classification of the cosmic web. ✔ The title and use are consistent.
-  Cautun et al. 2014, MNRAS 441, 2923, arXiv:1401.7866: cosmic web evolution. ✔
-  Planck 2018 results VI, A&A 641 A6 (2020), arXiv:1807.06209: cosmological parameters; H0 ≈ 67.4, Ωm ≈ 0.315. ✔ Your cited H0, Ωm values are consistent.
-  Shamir 2022, MNRAS 516, 2281, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” arXiv:2208.13866: ✔ Title and quoted amplitude (~2–4% asymmetry) are qualitatively consistent with the paper’s abstract and conclusions.
-  Tempel et al. 2014, A&A 566, A1, arXiv:1402.1350: FoF groups/clusters for SDSS; group multiplicity environment classification. ✔
-  Rincón et al. 2025, ApJ 982, 38, “DESI-VAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” arXiv:2411.00148: This does not yet exist on ADS/arXiv. DESI DR1 (18M objects) is real[4][5], but “DESI-VAST” void catalog ApJ 982, 38, arXiv:2411.00148 is not findable. This is another apparently fabricated or at least currently nonexistent reference.

**Required fix:**  
- For [5–10], add full bibliographic fields (journal, volume, page, year) systematically and ensure every quantitative statement is traceable: e.g. when you quote “Cautun et al. geometric default λth = 0”, make sure that choice is indeed recommended there (it is, but you should cite the page/section and, ideally, say “following Cautun et al.’s λth = 0 default” instead of implying it is a universal standard).  
- For , either provide the correct existing ApJ/ arXiv entry OR clearly label it as “in preparation” / “submitted” with no volume/page, and remove the DOI and volume if they are speculative. You cannot use a non-existent ApJ paper as a peer-reviewed anchor.

---

### 2. Claims about prior work’s statistics

Where you quote statistical values from prior papers, I checked for consistency with abstracts and main texts where possible.

**P5-m1 (MINOR)**  
**Location:** Abstract, first paragraphs of §II and §VIII F.  
**Problem:** You state for Paper IV:

- Global CW fraction 0.4974 ± 0.000279, “consistent with parity at ~1σ,” and a “catalog-wide ∆fCW ≈ −0.0026” (−0.26% vs 0.5).  
- A “∼9.5σ catalog-level monopole” in Paper IV feeding a −5σ on the DESI-matched subset.

Paper IV is not public and cannot be inspected; these numbers are not verifiable. Within P5 itself, there is an internal consistency check (the simple binomial scaling from ∆f ≈ −0.0026 over 8.47M objects gives ~9σ, and the propagation to 8×10^5 objects gives ~5σ), but the original claim is not externally traceable.

**Required fix:**  
- Mark all Paper IV-derived numerical statements as internal to this project and not externally verifiable, e.g. “Paper IV (unpublished, internal) finds…”.  
- If possible, add a short self-contained derivation of the monopole-level significance in an appendix of P5, based only on the publicly released HF catalog you plan to publish; that way the numerical values become checkable from P5 itself, even if Paper IV lags.

---

**P5-m2 (MINOR)**  
**Location:** §IX A, Tempel FoF cross-validation; Table XI and the surrounding text.  
**Problem:** You give a 4-class mapping from Tempel group multiplicities to environment types and then report CW fractions and σ-values per class. The mapping is your choice, not specified in Tempel et al. 2014, and the Tempel paper does not provide any chirality statistics (they are not about morphology). That is fine, but you then talk about a “0.026 pp concordance spec” for the filament class and describe the agreement as “within spec.”

This “spec” appears to be your own internal threshold, not something derived from Tempel et al. or any external standard.

**Required fix:**  
- Rephrase: explicitly state that the 0.026 pp is simply the measured difference, not something like “within the 0.2 pp spec,” unless you clearly define that spec earlier as a purely internal heuristic tolerance.  
- Make clear that Tempel et al. do not specify any chirality-related metrics; all such statistics are computed in this work.

---

### 3. Non-standard / internal “references” and versioning language

The manuscript is full of internal audit tags and version/path artifacts, which PRD/MNRAS will not accept as references.

**P5-M3 (MAJOR)**  
**Location:** Throughout: first page “pipelines/p5_desi_chirality/…”, §III, §IV, §V, §VIII A–F, Appendix B “REPRODUCIBILITY CHECKLIST”.  
**Problem:** Many “references” are actually Git paths or internal pipeline paths, e.g.

- “pipelines/p5_desi_chirality/scripts/02_fetch_desi_dr1.py”  
- “pipelines/p5_desi_chirality/env_finder/reports/01_volume_fractions.json”  
- “pipelines/p5_desi_chirality/results/analysis_cosmic_web/desivast_three_algorithm_void_chirality.json”  
- And the explicit “REPRODUCIBILITY CHECKLIST” listing config filenames and seeds.

These are fine for an internal reproducibility note but not as part of the main scientific literature record; they cannot be resolved or cited via ADS, and they function like version-control logs rather than references.

**Required fix:**  
- Strip all internal paths from the main narrative and references section.  
- If you want to support reproducibility, place these details in a “Data/Code Availability” paragraph that points to a public repository (with a DOI or permanent URL), not to a local directory tree.  
- Remove the “REPRODUCIBILITY CHECKLIST” as a numbered list at the end; instead, summarise in a short “Code and data availability” paragraph using standard language.

---

**P5-M4 (MAJOR)**  
**Location:** References [3], [4]; Appendix B; various places in the body.  
**Problem:** There is explicit version-history and internal-log style language embedded in citations:

- “(v1.0.139, 2026-05-28)”  
- “(v1.7.37, 2026-05-24)”  
- “immutable revision paper4-v1.0.122”  
- “Internal companion artifact; an arXiv identifier will be assigned upon Paper IV submission.”

These are **review-log artifacts and version-control metadata**; they should not appear in a formal reference list in this form.

**Required fix:**  
- Remove version numbers and internal revision tags from references, or move them into a separate “code repository” note. References should be of the form “Author, Title, arXiv:xxxx.xxxxx [astro-ph] (year)” or journal-style.  
- For HF models or datasets where versioning is scientifically relevant, mention it in the data section (“we use HF dataset bamfai/galaxy-chirality-catalog, snapshot ‘paper4-v1.0.122’”), but do not treat these as numbered literature references.

---

### 4. σ-scale consistency and null procedures

You specifically asked to flag any place where σ values from different null procedures are combined without qualification.

In this manuscript, you:

- Define σ_from_half = (n_CW − 0.5N)/(0.5√N) and use it consistently for binomial deviations.  
- Use permutation-based p-values and Bonferroni-based σ thresholds but, for the most part, keep them distinct.

I do not see a place where different σ-scales are incorrectly treated as directly comparable *without* any explanation. The σ values used are all binomial or Gaussian approximations to binomial, and you explicitly derive the predicted σ as σ_pred = 2∆fCW√N. You do not, for example, mix a σ from a T-Web analysis with a σ from a completely different statistic on the same footing.

Therefore I do not raise an ESSENTIAL flag under your point 7: the σ scaling is internally coherent and clearly defined.

---

### 5. Duplicate phrases and artifacts

I scanned for obvious duplicated phrases like “canonical canonical-mask” and did not find such clear typographical duplicates. There are repeated patterns (e.g. “catalog-monopole offset”) but they are not literal duplicated errors.

No specific duplicated phrase that clearly looks like a textual glitch needs to be flagged on that basis.

---

### 6. Abstract accuracy vs. what is actually shown

**P5-M5 (MAJOR)**  
**Location:** Abstract vs. main text (e.g. §VI A–F, §VIII).  
**Problem:** The abstract claims, among other things:

- “Headline result: the CW fraction shows no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset of ∼ 0.2 pp ... and by counting statistics of ∼ 5 pp (statistical-dominated for V-Web void at n = 428, ∼2σ on the binomial null).”  
- “Phase 2 sensitivity sweep across nine cells… confirms the result: the per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points… headline sign-pattern is invariant.”  
- “We interpret this as no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity; the V-Web void class… is sample-size limited… so the controlling void constraint comes from the DESIVAST-anchored re-projection (n = 56,981, ∆fCW = 0.0007)…”

These statements are largely consistent with the detailed tables and with your own σ-from-half calculations, *conditional on accepting Paper IV’s monopole as given*. However, because the catalog and its monopole are not externally verifiable, the abstract slightly overstates what is “proved”:

- It speaks of “no environment dependence” without always qualifying that this is “beyond the Paper IV catalog monopole.”  
- It treats DESIVAST  as “peer-reviewed DR1 BGS void catalog (Rincón et al. 2025, ApJ 982, 38)” when that paper cannot be found in ADS.

**Required fix:**  
- Adjust the abstract to explicitly state that all constraints are **conditional on the Paper IV classifier calibration**, which is currently unpublished.  
- Soften language like “no evidence for environment-dependent chirality beyond the catalog-monopole offset” to “within this dataset and assuming the classifier monopole from Paper IV, we find no statistically significant environment-dependent chirality signal at the ≳ 25 h⁻¹ Mpc scale.”  
- Avoid implying that DESIVAST is already a peer-reviewed ApJ product unless it truly is; otherwise call it “a DR1 BGS void catalog described in Rincón et al. (in prep.)” and reposition its status.

---

### 7. Length vs. contribution

**P5-m3 (MINOR)**  
**Location:** Overall structure.  
**Problem:** The paper is quite long for what is, at core, a null environmental dependence test using one main chirality catalog and a void catalog plus a V-Web classifier. The sheer amount of pipeline and configuration detail (Phase 2 sweep CSV paths, SHA-256 sidecars, seeds, etc.) inflates length without additional scientific insight.

PRD/MNRAS methods/catalog papers can run 15–30 pages, so 21 pages is not intrinsically a problem, but here a substantial fraction is internal pipeline bookkeeping not normally retained in a journal article.

**Required fix:**  
- Move most of the pipeline internal details (script filenames, JSON artifact names, SHA-256 sidecars, etc.) to a separate online repository or a short “data/code availability” section.  
- Aim to reduce the main text to ~15–18 pages by pruning reproducibility audit language and keeping only what is scientifically essential.  

---

## Summary recommendation

**MAJOR REVISIONS**

The core methodological work appears internally consistent and the use of existing cosmology references (Planck 2018; Hahn, Hoffman, Cautun; Tempel; Shamir) is broadly correct. However, the dependence on unpublished internal companion papers (Paper IV, Paper II), the use of non-existent arXiv/ApJ references (, ,  as currently written), and the extensive use of internal pipeline paths and versioning in the main text and reference list are not acceptable in a PRD/MNRAS submission. These must be cleaned up, with all fabricated or future metadata replaced by real citable items or clearly labeled as “in preparation/private comm.,” and the abstract must be rephrased to reflect that all results are conditional on the unreviewed classifier catalog. Once those issues are resolved and the narrative is streamlined, the paper can be reconsidered.