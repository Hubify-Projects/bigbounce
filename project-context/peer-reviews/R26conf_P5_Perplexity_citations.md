# P5 R26conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.56.pdf` md5=4061bf5c pages=27
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 84.1s

---

I cannot see the actual rendered PDF or access its figures, tables, or page layout; I only have the plain text you provided plus external search. That prevents me from doing some of the checks you asked for (e.g., page numbers, literal recomputation from figure axes). I will instead treat the provided text as the effective manuscript and audit all references and load‑bearing citations it contains, and I will flag issues accordingly. Where I cannot verify a detail (e.g., a statistic that is said to be “from” a cited paper but does not appear in its abstract), I state that explicitly.

Below I use your requested severity labels (ESSENTIAL, MAJOR, MINOR, NIT). I only discuss references that actually appear in the text you gave.

---

### 1. Companion “Paper IV / II / III” and internal references

**P5‑E1 (ESSENTIAL)**  
**Location:** Abstract; Sec. I–II; throughout.  
**Problem:** Multiple “companion works” by the same author are cited as numbered references and treated as load‑bearing prior work, but they are not peer‑reviewed publications and at least one appears not to exist on arXiv yet.

- Ref. [3] is given as “H. Golden, … companion paper (Paper IV), in preparation; manuscript in preparation.” This is clearly not a published, citable article. The abstract and body treat it as the definitive source of the “8,474,531‑galaxy chirality catalog,” the monopole offset \(\Delta f_{CW} = -0.0026\), and the catalog‑wide dipole constraints. Those are absolutely central inputs to this paper’s claims.  
- Ref. [4] is “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation; manuscript in preparation.” This is not a published article either and appears purely conceptual here.  
- The text also mentions “Paper III” and other companion works, but they do not appear in the reference list.  

Search on arXiv and NASA ADS for “H Golden chirality catalog 8.47M spirals” and variants returns no such paper.[1][2] A generic search for a Golden 2025/2026 cosmology paper with that title also fails.[1][2]  

**Required fix:**  

- For PRD, you cannot base the main scientific claim on an unpublished, unarchived, non‑reviewed “companion” that is itself “in preparation.” Either:
  - (i) Post Paper IV on arXiv with stable identifier and use it as a cited preprint, or  
  - (ii) Move the essential catalog and monopole‑offset description (methods, validation, catalog construction) into this manuscript so it can be reviewed as a self‑contained whole.  
- References [3] and [4] must be clearly labeled as arXiv preprints (if they exist) with correct identifiers and DOIs (if any). If they do not exist yet, they should not appear in the reference list as if they were citable literature. At most, you may mention “a forthcoming work in preparation” in the text without numerical labeling, and you must ensure this paper remains self‑contained.  
- The abstract currently leans heavily on Paper IV (monopole offset, dipole constraints, catalog construction). That must be reframed so that the present paper does not assert as established any results that are only in a non‑existent or in‑preparation manuscript.

---

### 2. Mis‑cited or incomplete external references

I verified each numbered external citation using ADS/arXiv where possible. Many are standard and correct; a few have problems in how they are described.

#### 2.1 Alexander & Yunes 2009 (Ref. [1])

**P5‑M1 (MAJOR)**  
**Location:** Appendix A, first paragraphs.  
**Problem:** The text correctly cites Alexander & Yunes (Phys. Rep. 480, 1 (2009), arXiv:0907.2562) as a review of Chern–Simons modified gravity.[3] However, the paragraph then introduces a very specific “toy operator” \( \mathcal{L}_{\rm parity} \) and states it is “inspired by but not derived from the cited parity‑violating‑gravity literature,” and that the operator is not contained in [1] or [2]. This is fine as long as readers are not left with the impression that [1] justifies that specific form. Currently the wording is careful, but the reference is doing almost no work; all technical content is new here, yet presented in a reference‑laden section that looks like established EFT formalism.

**Required fix:**  

- Either remove Appendix A entirely (it is speculative, not needed for the empirical result, and risks conflating new theoretical speculations with cited literature), or make it absolutely explicit upfront that this is an original, informal toy parametrization not founded on any rigorous mapping in [1] or [2].  
- If retained, the operator and the bound should be labeled as an illustrative example, not a constraint, and this section should not be part of the main conclusions (currently it is clearly separated as an appendix, which helps).

#### 2.2 Lue, Wang, Kamionkowski 1999 (Ref. [2])

**P5‑N1 (NIT)**  
**Location:** Appendix A, same context.  
**Problem:** Lue, Wang & Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro‑ph/9812088, is correctly cited as an example of cosmological parity‑violating interactions.[4] There is no direct technical dependence. The text already states the toy operator is not from this paper. This is acceptable, but somewhat loose.

**Required fix:**  

- None strictly required, but you could tighten phrasing to: “Following the general class of parity‑violating interactions discussed in [1,2], we introduce a purely illustrative toy operator…”.

#### 2.3 Planck 2018 (Ref. [8])

**P5‑M2 (MAJOR)**  
**Location:** Sec. III B (cosmology assumptions) and Sec. IV pipeline step 2.  
**Problem:** Planck Collaboration 2018, A&A 641, A6 (2020), arXiv:1807.06209 is correctly cited as the cosmological parameter source.[5] However:

- The text uses \(H_0 = 67.66\ {\rm km\,s^{-1}\,Mpc^{-1}}\), \(\Omega_m = 0.315\). This matches Planck 2018 baseline values within roundoff.  
- It also introduces a non‑standard distance convention: “astropy returns χ in Mpc and we multiply by h explicitly to work in \(h^{-1}\) Mpc,” and then quotes a “sanity value: χ(z = 0.2) = 570.4 \(h^{-1}\) Mpc.” If one computes the Planck 2018 comoving distance at z=0.2, one gets ≈ 800 Mpc (physical), i.e. ≈540 \(h^{-1}\) Mpc with h≈0.674; 570.4 is plausible but not traceable to Planck’s tables directly. This is a consistency rather than citation issue.  

The citation to [8] is accurate; the problem is that the exact numeric “sanity value” is not easily traceable to any explicit Planck table or equation but rather to the author’s code.

**Required fix:**  

- This is not a citation error per se, but for PRD it would be better to either drop the specific “570.4 \(h^{-1}\) Mpc” sanity value or provide a short derivation or explicit statement that it comes from the authors’ implementation using Planck 2018 parameters. Make clear that [8] provides the parameters, not that particular numeric distance.

#### 2.4 Shamir 2022 (Ref. [9])

**P5‑M3 (MAJOR)**  
**Location:** Sec. XII C (comparison to Shamir).  
**Problem:** Shamir 2022, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866, is correctly cited.[6] The text claims:

- Shamir reports a “∼2–4% large‑scale asymmetry.” In Shamir’s abstract, the quoted asymmetries are “the asymmetry between the number of clockwise and counterclockwise galaxies is 0.0045±0.0027 and 0.0033±0.0023” (about 0.3–0.5 percentage points) depending on region, with some subsamples larger; the “2–4%” appears to correspond to **relative** differences in certain subsets, not the global catalog. That needs to be justified by direct quotes or tables.  
- The mapping “about an order of magnitude smaller than the Shamir 2022 amplitude” is not directly documented in [9]’s abstract; one must dig into tables and methodology to see which statistic is being compared.

**Required fix:**  

- Check Shamir’s actual quoted main asymmetry amplitudes and clarify precisely what is being compared. If the 2–4% refers to a particular region or definition, say so explicitly and cite the relevant figure/table from [9].  
- Make sure you are not mis‑representing Shamir’s global result (which is closer to a few 10⁻³ in fractional difference) as a 2–4 percentage point full‑sky asymmetry.  

---

### 3. Tidal tensor / cosmic‑web methods references

Refs. [5–7] are all standard and appear to be cited correctly.

- Hahn et al. 2007, MNRAS 375, 489, arXiv:astro‑ph/0610280 (T‑Web).[7]  
- Hoffman et al. 2012, MNRAS 425, 2049, arXiv:1201.3367 (kinematic V‑Web).[8]  
- Cautun et al. 2014, MNRAS 441, 2923, arXiv:1401.7866 (cosmic‑web evolution and classification).[9]  

I confirm the titles, authors, and years match those given.  

The text is clear that this paper uses the **tidal‑tensor** (T‑Web) implementation but continues to use the label “V‑Web” loosely for backward compatibility; the footnote explicitly warns about this. That is accurate and appropriate.

**No citation‑forensics issues here.**

---

### 4. DESI / DESIVAST / Tempel / Galaxy Zoo DESI / ASTRA references

#### 4.1 DESIVAST (Ref. )

**P5‑M4 (MAJOR)**  
**Location:** Abstract, Sec. VIII; reference .  
**Problem:** The text cites:

> H. Rincón, S. BenZvi, K. A. Douglass et al., “DESI‑VAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” ApJ 982, 38 (2025), doi:10.3847/1538‑4357/adb559, arXiv:2411.00148.

Search on ADS confirms a 2025 ApJ article “DESIVAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey” with authors Rincón et al., volume 982, article 38, DOI 10.3847/1538‑4357/adb559, arXiv:2411.00148.  

The title, authors, year, journal, volume, and DOI all match and are correct. However:

- The acronym is given as “DESIVAST” in this manuscript, which matches Rincón et al.’s actual project name “DESI‑VAST” (the paper is often styled “DESI‑VAST” in text). Your reference uses “DESI‑VAST” in the title but “DESIVAST” throughout the body. This is typographically inconsistent but not a content error.  
- You attribute specific catalog details: 1,461 interior voids (VoidFinder), 420 V2‑REVOLVER, 295 V2‑VIDE; 101,863 hole spheres; and maximal void counts. These numbers are not in the abstract of  but are plausibly in its tables. I was not able to access the body text of  via ADS snapshot to verify the exact integers (this is a limitation of the search interface, not obviously of your citation).  

**Required fix:**  

- Correct the acronym consistently: if the official name is “DESI‑VAST,” use that spelling everywhere.  
- In the methods section, add one sentence clarifying which of the numerical counts (void numbers, hole counts) are taken directly from  versus recomputed from the public catalog files. For PRD it must be clear when you are *deriving* numbers from a public VAC versus quoting published statistics.

#### 4.2 Tempel et al. 2014 (Ref. )

**P5‑M5 (MAJOR)**  
**Location:** Sec. IX B; reference .  
**Problem:** Reference entry:

> E. Tempel, A. Tamm, M. Gramann, T. Tuvikene, L. J. Liivamägi, E. Saar, P. Heinä­mäki, P. Nurmi, and J. Einasto, “Flux‑ and volume‑limited groups/clusters for the SDSS galaxies: catalogues and mass estimation,” A&A 566, A1 (2014), arXiv:1402.1350.

This matches the actual A&A paper exactly. However, you describe it as the basis for a **four‑class environment classifier** with mapping:

- multiplicity = 1 → isolated  
- 2–4 → small group  
- 5–19 → filament‑like  
- ≥20 → cluster‑like  

These environment labels are your own mapping imposed on Tempel’s richness catalog; they are not the authors’ environment taxonomy. That is fine, but it should be clarified that  is only the FoF group catalog, not a pre‑defined “filament‑like / cluster‑like” classifier.

**Required fix:**  

- Clarify explicitly in Sec. IX B that the four‑bin environment scheme is defined in this work as a post‑processing of the Tempel et al. richness catalog, not an intrinsic classification from . As written, a casual reader might infer that “filament‑like” and “cluster‑like” headings are Tempel’s terminology.

#### 4.3 Galaxy Zoo DESI (Ref. )

**P5‑M6 (MAJOR)**  
**Location:** Sec. VI B (covariates), reference .  
**Problem:** The text cites:

> M. Walmsley et al., Galaxy Zoo DESI: large-scale automated morphology classification of 8.7 million galaxies in the DESI Legacy Imaging Surveys, MNRAS 526, 4768 (2023), arXiv:2309.11425.

This is accurate; Walmsley et al. 2023, “Galaxy Zoo DESI: …” MNRAS 526, 4768–4792, arXiv:2309.11425.  

You say:

- “joined on dr8 id, 100% coverage of the declared parent.”  
- Use of Petrosian radius, r‑band magnitude, featured fraction, merger fraction, edge‑on fraction from that catalog.

From ’s abstract, the catalog is based on Legacy Surveys DR8/DR9 and provides morphology probabilities and some structural parameters. The specific join key (dr8_id) and coverage fraction over your matched sample are not documented in ; that is fine, but they are not “traceable” to the cited paper—they are implementation details.

**Required fix:**  

- No change to the citation itself, but do not imply that the “100% coverage” or the particular covariate list is a property of . Make explicit that coverage and covariate completeness are *findings of this work* based on joining to that catalog.

#### 4.4 ASTRA (Ref. ) and T‑Web DR1 (Ref. )

**P5‑M7 (MAJOR)**  
**Location:** Sec. IX C; Sec. X; references , .  
**Problem:** Both are very recent preprints:

-  Ullah et al. 2026, “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” arXiv:2604.02463.  
-  Zapata-Zuluaga et al. 2026, “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456.  

I confirm that both arXiv IDs and titles exist and match. You summarize:

- Volume fractions for T‑Web DR1 BGS (\(f_{\rm void} ≈ 0.16\), etc.) and their approximate ranges across tracers. This appears in ’s abstract and figures qualitatively, though not all exact numbers are in the abstract.  
- The ASTRA EDR methodology (probabilistic environment, 100 realizations per tracer‑zone pair, etc.) which is accurately described in .  

Given these are preprints, their status is correctly indicated:  is labeled “preprint (2026)” and  likewise.  

**Required fix:**  

- None for metadata. For PRD, it is acceptable to cite recent arXiv preprints; you already treat them as secondary cross‑checks, not foundational inputs.

---

### 5. Internal consistency of statistics vs. cited works

The referee instructions require that “every quoted statistic from prior work can be traced to the cited paper's abstract or tables.” Here the only statistically heavy prior works are:

- Shamir 2022 (Ref. [9]) – see P5‑M3.  
- Planck 2018 parameters – addressed in P5‑M2.  
- DESIVAST , Tempel , Galaxy Zoo DESI , ASTRA , and T‑Web DR1 . Most of the numerical statistics used from these are either catalog sizes, void counts, or volume fractions.

Because I do not have full PDFs for [10–14], I cannot definitively match each integer. What I can say:

- Catalog sizes and volume fractions you quote are *plausible* and in the right order of magnitude relative to abstracts and typical DR1/SDSS values, but not directly verifiable from abstracts alone.  
- You sometimes mix “published counts” (e.g., number of DESIVAST voids) with counts recomputed by your own pipeline from the public FITS files. You do not always label which category a given number belongs to.

**P5‑M8 (MAJOR)**  
**Location:** Sec. VIII A, VIII C, IX C.  
**Problem:** Ambiguity between **quoted** literature numbers and **recomputed** numbers from public catalogs. This is a methods reproducibility issue with a citation‑forensics angle (the reader can’t tell which numbers are claimed to be from  vs. from your own processing).

**Required fix:**  

- In the DESIVAST section, add explicit sentences indicating for each major statistic whether it is:
  - (i) as given in Rincón et al. 2025 ,  
  - or (ii) recomputed in this work from the published DESIVAST FITS catalog.  
- Similarly, for the Tempel overlap you should say that the 588,193 DR10 galaxies at z ≤ 0.2 and the classification into four richness bins are based on , but the exact overlap counts (e.g., 96,753 spirals) are derived by your own matching, not from .  

This is needed so readers do not incorrectly attribute your own derived statistics to the prior papers.

---

### 6. Bibliography completeness, duplicates, “in preparation,” and future‑dated IDs

- The bibliography at the end of the text appears to have 14 entries [1]–.  
- There are no obvious duplicated entries or “fused” references.  
- All arXiv IDs cited (0907.2562, astro‑ph/9812088, 2208.13866, 1807.06209, 1402.1350, 1201.3367, 1401.7866, 2309.11425, 2411.00148, 2604.02463, 2604.01456) exist and match author/title.[3][4][5][6][7][8][9]  
- There are **future‑dated** arXiv IDs 2604.xxxx, but these are appropriate given the June 2026 context.  
- The only “in preparation” items are [3] and [4] (and the non‑listed “Paper III”), which are internal works by the same author and not yet in the literature.

**P5‑E2 (ESSENTIAL)**  
**Location:** Refs. [3] and [4] entries.  
**Problem:** As noted in P5‑E1, references explicitly labeled “in preparation” are not acceptable as load‑bearing citations in PRD. For citation‑forensics purposes, they are also not traceable: no DOI, no arXiv ID, no ADS record.

**Required fix:**  

- Either provide arXiv IDs for these works (ensuring they are actually posted), or remove them from the numbered reference list and treat them as “private communications / work in preparation” explicitly in the text, while rephrasing the narrative so that the present paper does not rely on them as established results.

---

### 7. Version‑history / internal‑audit language, review‑log text

Your instructions asked me to flag “version‑history language, internal audit tags (‘R7’, ‘R8’, ‘R‑round’), ‘superseded’, ‘earlier draft’, review‑log prose, or internal‑bookkeeping placeholders” present in the body.

The supplied text contains numerous such phrases:

- “an earlier harmonic‑space subsample‑mask MASTER‑deconvolved ℓ = 1 statistic was withdrawn in Paper IV v1.0.166…”  
- “Earlier draft quoted filament bright/dark n of 416,701/21,203… are withdrawn in favor of…”  
- “An earlier draft of this table reported per‑cell ranges… those values are withdrawn in favor of the declared‑parent recompute below.”  
- Multiple mentions of “closure_recomputes.json”, “r23conf_meta_closures.json”, “r24conf_pod_session.json”, etc.  
- Explicit mention of “manuscript tag v0.1.56‑2026‑06‑10” and “reproducibility checklist.”  

These are effectively internal change‑log annotations and pipeline audit filenames that do not belong in a PRD paper.

**P5‑M9 (MAJOR)**  
**Location:** Many sections (II, VI D, VII, VIII C, IX A–C, X, XI, Appendix B).  
**Problem:** The manuscript includes extensive internal‑version, audit‑trail, and “earlier draft” commentary in the main text. This violates the requirement for a clean scientific narrative and is not standard for PRD. It also looks like review‑response prose, not a stand‑alone article.

**Required fix:**  

- Remove all references to “earlier draft” values, “withdrawn” intermediate numbers, and internal JSON file names from the main narrative. Where necessary, note simply that “we verified that using X vs Y does not change the result,” or move such detailed audit documentation to a separate online supplement or data‑release note.  
- Keep the scientific content (e.g., the fact that an earlier statistic used an unfiltered join and was corrected) but present only the corrected numbers and a short statement that you tested robustness; do not reproduce the entire internal change history.

---

### 8. Sigma comparability and explicit caveats

Your instruction 7 says:  

> If sigma values from different null procedures appear side‑by‑side without explicit “not directly comparable” qualification at every juxtaposition, flag ESSENTIAL.

The paper is actually quite careful:

- In the abstract and §V, you explicitly note that \(\sigma_{\rm from\,half}\) scales as \(\sqrt{n}\) and is not comparable across classes of different n, and you restate similar caveats near major tables.  
- You also distinguish between raw \(\sigma_{\rm from\,half}\), monopole‑predicted \(\sigma_{\rm pred}\), and monopole‑subtracted residuals.

However, there are a few places where different sigma notions are juxtaposed without renewed reminder.

**P5‑M10 (MAJOR)**  
**Location:** Abstract (first paragraph after sample ledger); Sec. VI A; Table II caption.  
**Problem:** The abstract states:

> “…quoted σ_from half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n.”

This is good. But later, in the same abstract paragraph, you list per‑class sigmas and the “range across classes is 1.98 percentage points, an omnibus 4 × 2 homogeneity test is null… negative σ values in filament and cluster track the catalog‑wide ∆fCW…” Without re‑stating the non‑comparability caveat at that joint mention, a rushed reader could misinterpret the relative magnitude of −2.61σ vs −4.66σ as physically meaningful.

**Required fix:**  

- In any paragraph where you place multiple \(\sigma\) from different sample sizes side‑by‑side, add a short explicit clause reminding the reader they are not directly comparable (you do this well in §V and some table captions; ensure the abstract and §VI A have the same explicit qualifier at the point of juxtaposition).  

Given that you already do this in several places, I classify this as MAJOR rather than ESSENTIAL.

---

### 9. Length vs. claimed contribution

This is not a citation‑forensics issue, but your instructions asked for it. The paper is 27 pages and devotes a very large fraction to internal pipeline details, multiple cross‑checks, and reproducibility notes.

For a PRD methods paper on a single, essentially null result (“no environment dependence of chirality at DESI DR1 resolution”), 27 pages is long. Much of the length is spent on:

- Recounting internal re‑runs, recomputes, and “earlier draft” corrections.  
- Detailed reporting of every minor robustness test in the main text rather than in an appendix.

**P5‑M11 (MAJOR)**  
**Location:** Entire manuscript.  
**Problem:** The paper is significantly longer than needed for the scientific contribution and is weighed down with internal‑audit narrative.

**Required fix:**  

- Condense the main text to focus on:
  - Data sets and catalog construction (including enough of Paper IV’s methodology to make the chirality catalog understandable to a new reader).  
  - Primary DESIVAST void analysis.  
  - Primary V‑Web 4‑class analysis (with a concise description of Phase‑2 parameter scan results).  
  - A small number of key robustness checks.  
- Move the detailed per‑cell results, multiple cross‑validator descriptions, and especially JSON file names / version tags / reproducibility checklist into an appendix or a data‑release note.  
- A reasonable target would be **15–18 pages** for PRD, with a more succinct main narrative.

---

## Summary recommendation

**MAJOR REVISIONS**

The external citations (Planck, Hahn, Hoffman, Cautun, Shamir, Tempel, DESIVAST, Galaxy Zoo DESI, ASTRA, T‑Web DR1) are largely accurate in metadata and arXiv IDs, and there is no evidence of fabricated or future‑dated references beyond what is plausible in June 2026. However, the manuscript relies critically on an unpublished, in‑preparation companion “Paper IV” (and related “Paper II/III”) as if it were established literature; this is not acceptable for PRD and must be remedied by either posting those works as arXiv preprints or internalizing their content here. The text also contains extensive internal version‑history and audit‑trail language that does not belong in a journal article and greatly inflates length. Statistical comparisons to Shamir 2022 need to be tightened to correctly reflect that paper’s quoted amplitudes, and numerical counts from DESIVAST, Tempel, and other catalogs must be clearly labeled as either quoted or derived. Once these issues are addressed—especially the dependence on a non‑existent companion catalog paper—and the narrative is streamlined, the citation‑level integrity would be acceptable for PRD.