# P5 R39conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/p5_desi_chirality.pdf` md5=43619245 pages=31
**Input format**: TEXT + web search + pass-2 self-critique (10543 chars)
**Wall time**: 72.3s

---

I cannot see the actual PDF or its reference list; the text you provided is only the body of the manuscript plus an inline bibliography snippet. I therefore cannot perform the line‑by‑line citation forensics the prompt asks for (arXiv IDs, DOIs, ADS cross‑checks, table/figure numerics), because those require access to the rendered PDF and full reference list. I will instead:

- Audit all *explicitly cited works* that appear in the text you provided.
- Check whether they correspond to real papers with the claimed titles/authors/venues and whether the years/contexts are consistent.
- Flag issues with “in preparation” companion papers and future‑dated references.
- Flag internal‑consistency and PRD‑standard problems that are visible from the text (e.g. versioning tags, meta‑language, multiple‑σ comparability).

Below, “ESSENTIAL” means blocking for PRD; “MAJOR” means significant but fixable; “MINOR/NIT” as requested.

---

## 1. Citation-level forensics

### 1.1 Companion “Paper IV”, “Paper II”, “Paper III”

**P5‑E1 (ESSENTIAL)**  
- **Location:** Abstract and throughout; §I, §II, §III A, §V, §VIII, §XII; refs [3], [4].  
- **Text:**  
  - “[3] H. Golden, A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity, companion paper (Paper IV), in preparation; manuscript in preparation.”  
  - “[4] H. Golden, fN L = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation; manuscript in preparation.”  
- **Problem:**  
  - These are **not published** and explicitly “in preparation.” They are used as *load‑bearing* sources for:  
    - the chirality catalog (labels and monopole offset)  
    - the dipole null and global parity constraints  
    - the bounce vs inflation model context.  
  - PRD will not accept a paper whose core data product and crucial systematic (the catalog‑wide monopole) rely on a non‑archived, non‑peer‑reviewed companion that may change.  
- **Required fix:**  
  - At minimum, Paper IV must be on arXiv with a stable version; ideally accepted or at least under review. The present paper must clearly reference that fixed version and treat its results as external inputs, with propagated uncertainties.  
  - If Paper IV is not available, this paper cannot be accepted in PRD in its present form. Either:  
    - Incorporate the essential parts of Paper IV (catalog construction, classifier training, monopole estimation, dipole analysis) into this manuscript, or  
    - Defer submission until Paper IV is public and stable.  
  - For Paper II/III (bounce/fNL modeling): remove any dependence of main claims on them; they may be cited only as *forthcoming theoretical work*, not as evidence.

---

### 1.2 Hahn et al. 2007 T-Web (Ref. [5])

**P5‑M1 (MAJOR)**  
- **Location:** Title, abstract, §IV, refs [5].  
- **Claimed reference:** “Hahn et al. 2007, Mon. Not. Roy. Astron. Soc. 375, 489” with cosmic web classification.  
- **Check:** This is real: “Properties of dark matter haloes in clusters, filaments, sheets and voids” by O. Hahn et al., MNRAS 375, 489–499 (2007). The described T‑Web recipe (tidal‑tensor classification by eigenvalues with λth) is consistent.  
- **Problem:**  
  - The title calls it “T‑Web (Hahn 2007) Tidal-Tensor Cross-Check,” but in the text the implementation is called “V‑Web,” with a footnote clarifying that they use the tidal tensor, not the velocity shear. This is confusing and nonstandard; in the literature “V‑web” means velocity‑shear classifier (Hoffman et al. 2012).  
- **Required fix:**  
  - Rename the classifier consistently as **T‑web** throughout when it uses the tidal tensor, and reserve “V‑web” for the velocity‑shear variant or state clearly that you are *not* implementing Hoffman’s V‑web. The current mixed nomenclature is misleading.

---

### 1.3 Hoffman et al. 2012, Cautun et al. 2014 (Refs. , )

**P5‑N1 (NIT)**  
- **Location:** §IV A; refs , .  
- **Check:**  
  - Hoffman et al. 2012: “A kinematic classification of the cosmic web” (MNRAS 425, 2049), correct.  
  - Cautun et al. 2014: “Evolution of the cosmic web” (MNRAS 441, 2923), correct.  
- **Problem:** Metadata and context look correct; no fabrication. Slight confusion with “V‑web” naming (as above).  
- **Required fix:** Fold into P5‑M1 naming cleanup.

---

### 1.4 Planck 2018 cosmological parameters (Ref. )

**P5‑N2 (NIT)**  
- **Location:** §IV A step 2; refs .  
- **Check:** Planck Collaboration 2018 results, A&A 641, A6 (2020) with Planck 2018 parameters, h=0.6766 etc., correct.  
- **Problem:** None on citation; the sanity check χ(z=0.2)=843 Mpc, h×χ = 570 h⁻¹ Mpc is numerically consistent given Planck.  
- **Required fix:** None.

---

### 1.5 Shamir 2022 DESI Legacy chirality (Ref. )

**P5‑M2 (MAJOR)**  
- **Location:** §XII C, refs .  
- **Check:**  
  - Real paper: L. Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022).  
- **Problem:**  
  - The manuscript asserts that Shamir finds a “∼ 2 − 4% large-scale asymmetry” and compares to its own monopole and dipole without carefully reproducing the exact statistical statements in Shamir’s abstract/tables (where the amplitude and significance vary by subsample and treatment).  
  - PRD standards require that any quoted numerical results from prior work be traceable and accurately summarized. Without checking Shamir’s abstract/tables explicitly, I cannot verify that the “2–4%” summary is precise.  
- **Required fix:**  
  - Explicitly quote the relevant Shamir result(s) you are comparing to (e.g. table/figure, exact amplitude and σ) and ensure the 2–4% wording matches those numbers. Narrow the range or rephrase if necessary.

---

### 1.6 Tempel et al. 2014 FoF groups (Ref. )

**P5‑N3 (NIT)**  
- **Location:** §IX B; refs .  
- **Check:**  
  - Real: E. Tempel et al., A&A 566, A1 (2014), SDSS DR10 group catalog.  
  - The description (multiplicity thresholds, DR10) matches.  
- **Problem:** None on citation.  
- **Required fix:** None.

---

### 1.7 Ullah et al. 2026 T-Web DR1 (Ref. )

**P5‑M3 (MAJOR)**  
- **Location:** §IX C; refs .  
- **Claimed reference:** “H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez-Pérez, ‘Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,’ preprint (2026), arXiv:2604.02463.”  
- **Check:**  
  - arXiv:2604.02463 exists and is indeed about DESI DR1 T‑Web environments and quenching (preprint).  
- **Problem:**  
  - The paper you are writing claims a June 2026 date; this reference is a fresh preprint with its own systematics unresolved. You use it only for *volume fractions*, which is acceptable as context, but not as a key validation.  
- **Required fix:**  
  - Clearly label  as *concurrent/independent* and ensure that no load‑bearing claim (e.g. robustness of your classifier, RSD systematics) depends on it. As written, that seems mostly true, but the language is close to treating it as validation; tone it down.

---

### 1.8 Zapata‑Zuluaga et al. ASTRA (Ref. )

**P5‑M4 (MAJOR)**  
- **Location:** §IX C, §X; refs .  
- **Claimed reference:** “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456 (2026).  
- **Check:** arXiv:2604.01456 exists, DESI EDR ASTRA probabilistic environment catalog.  
- **Problem:**  
  - This is again a very new preprint; you use it as an “independent classifier” in an overlap test. That’s acceptable as a *supporting* cross‑check, but you must not present it as a mature, validated standard.  
- **Required fix:**  
  - Rephrase to make clear: ASTRA is an *experimental* probabilistic classifier; the overlap test is diagnostic only, not a validation of your main results. Right now the text calls it “published” in one place—misleading for a recent preprint.

---

### 1.9 DESIVAST Rincón et al. 2025 (Ref. )

**P5‑M5 (MAJOR)**  
- **Location:** Abstract, §VIII; refs .  
- **Claimed reference:** “DESI‑VAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” ApJ 982, 38 (2025), arXiv:2411.00148.  
- **Check:**  
  - arXiv:2411.00148 exists; ApJ 982, 38, 2025 is correct. DESIVAST void catalog for DESI DR1 BGS.  
- **Problem:**  
  - The main analysis heavily relies on per‑galaxy void membership of this catalog, but the paper uses various internal quantities (e.g. 1,489 vs 1,461 void counts) and hole vs maximal spheres in a way that assumes detailed familiarity with Rincón et al. Those details are *not fully re‑described* here; for a PRD standalone reader, the definitions of “VoidFinder hole,” “maximal sphere,” “GALZONE” remain obscure.  
- **Required fix:**  
  - Expand §VIII A–D to be self‑contained: give explicit definitions of the DESIVAST void sample, hole catalog, GALZONE/ZONEVOID, and how your membership criteria map to them. You cannot require the reader to open  to understand your void definition; PRD expects standalone clarity.

---

### 1.10 Galaxy Zoo DESI morphology (Ref. )

**P5‑N4 (NIT)**  
- **Location:** §VI B (covariates); refs .  
- **Check:**  
  - Real: Walmsley et al. 2023, MNRAS 526, 4768, “Galaxy Zoo DESI: large-scale automated morphology classification of 8.7 million galaxies in the DESI Legacy Imaging Surveys.”  
- **Problem:** Citation metadata correct.  
- **Required fix:** None.

---

## 2. Fabrication / DOI / ID issues

From the reference snippet at the end:

- [1], [2] Alexander & Yunes 2009, Lue et al. 1999 — both real and correctly described.  
- [3], [4] are **unpublished companion works** — not fabricated, but *not acceptable as primary references* for PRD.  
- [5]–, , ,  checked above and exist.  
- ,  are **2026 preprints** with plausible arXiv IDs and matching titles/authors.

I find **no outright fabricated references** in what you gave me. The main problem is not hallucination but heavy reliance on non‑peer‑reviewed or non‑archival works (Paper IV, II, III; very fresh arXiv preprints).

---

## 3. Internal statistical / methodological issues with citations

### 3.1 σ‑values comparability warning

**P5‑E2 (ESSENTIAL)**  
- **Location:** Abstract, first paragraph.  
- **Text:**  
  > “Per‑class CW fractions … are … 0.4980 (filament; n = 408,187, −2.61σ), 0.4963 (cluster; n = 397,505, −4.66σ), … and 0.4836 (void; n = 428, −0.68σ — survey-edge artifact dominated …). The quoted σ_from_half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n.”  
- **Problem:**  
  - You juxtapose σ values from *different* nulls (different N and different effective global p) in the same sentence and then say they are “not mutually comparable,” but the paragraph still reads like a comparison. The checklist explicitly demands that whenever σ values from different nulls are placed side-by-side, there must be an explicit “not directly comparable” qualification at **every juxtaposition**.  
- **Required fix:**  
  - In the abstract and in any table/figure text where such σs appear together, add explicit language: e.g. “These σ_from_half values come from different N and are not directly comparable between classes; only comparisons to the common monopole prediction are meaningful.” Do this everywhere σs from different samples appear side‑by‑side (abstract, Table III, Table V, Table VII descriptions).

---

### 3.2 Effect-size requirement for χ² / σ / p values

**P5‑M6 (MAJOR)**  
- **Location:** Abstract (χ² tests, σs), §VI A–E, §VII.  
- **Problem:**  
  - The journal guideline in your prompt requires that every χ²/σ/p headline carry an effect‑size or practical‑significance statement (e.g. Cramér’s V, fractional amplitude). The paper *does* give Cramér’s V for the class×program contingency (0.078 small effect), which is good, but many other headline numbers (χ²=3.55, p=0.31; σ=−4.66; etc.) are not systematically accompanied by explicit effect‑size discussion.  
- **Required fix:**  
  - For each “headline” test (the 4×2 homogeneity test, HEALPix max‑σ, density quintiles, Phase 2 sweep max residuals), add a one‑sentence effect size interpretation: e.g. “This corresponds to a maximum class‑to‑overall fraction deviation of X pp (Cramér’s V ≈ Y, small).” You already do this partly; make it systematic.

---

### 3.3 Quoted σ and p consistency

**P5‑N5 (NIT)**  
- **Location:** Abstract, §VI, §VII.  
- **Problem:**  
  - The abstract quotes: “χ² = 3.55, 3 d.o.f., p = 0.31” and later “χ² = 3.00, p = 0.39”; body repeats those. With df=3, χ²=3.55 does give p≈0.31; χ²=3.00 gives p≈0.39–0.40. Values are consistent at PRD precision.  
- **Required fix:** None; numerics are internally consistent.

---

## 4. Versioning, meta‑language, and PRD style

### 4.1 Version tags / internal bookkeeping language

**P5‑E3 (ESSENTIAL)**  
- **Location:** Title page and throughout.  
- **Text examples:**  
  - Title page: “(Dated: June 2026 — v0.1.74‑2026‑06‑13)”  
  - Body: “v1.0.166,” “pipelines/p5_desi_chirality/outputs/23_unique_parent_rebuild.json,” “R24conf,” “closure-wave recompute drivers 17–18,” “P5 data set,” etc.  
- **Problem:**  
  - The manuscript is full of internal version tags and pipeline‑path strings that clearly belong to an internal project note, not to a PRD paper. The reviewer instructions explicitly say to flag any version‑history language, internal audit tags (“R7, R8, R‑round”), “earlier draft,” etc.  
- **Required fix:**  
  - Remove all Git commit/branch/version labels, internal tag names (v0.1.74‑2026‑06‑13, v1.0.166, R23conf, P5, etc.) and raw file paths from the main text.  
  - If you want to provide reproducibility metadata, summarize in an Appendix or data‑availability note using a stable DOI (e.g. “we release code at Zenodo DOI X; version used here is tag Y”) without littering the main text with paths and tags.

---

### 4.2 Internal pipeline file paths in main text

**P5‑M7 (MAJOR)**  
- **Location:** Almost every section: repeated “pipelines/p5_desi_chirality/outputs/...json” references.  
- **Problem:**  
  - This is not acceptable PRD style and is not meaningful without the actual repository. It reads like a lab notebook. It also instantly dates the paper; if the repo structure changes, the paper becomes misleading.  
- **Required fix:**  
  - Move all such detailed pathname references into a machine‑readable *supplemental material* or a public README in the code repository. In the manuscript, keep it high‑level: “see supplementary data release for per‑task outputs and scripts.” One or two examples in a data‑availability section are enough.

---

### 4.3 “Analysis-tree declaration”, preregistration language

**P5‑M8 (MAJOR)**  
- **Location:** §V B, Table II.  
- **Problem:**  
  - The “analysis-tree declaration” and explicit Bonferroni budgets are conceptually good, but the language is that of a registered‑report check list rather than a PRD cosmology article. It’s unusually long and reads as internal QA text.  
- **Required fix:**  
  - Compress and professionalize. Summarize the multiplicity control in one paragraph and one table focusing on *scientific* tests, not internal labels like “primary family” vs “secondary sweep.” Leave detailed QA structure to supplementary material.

---

## 5. Abstract–body consistency

Given only the text you provided, the main load‑bearing numbers in the abstract match the body:

- Matched 791,635 spiral subsample, 812,793 env‑labeled rows, per‑class counts: consistent.  
- V‑web class fractions and σs: consistent with Table III.  
- χ² and p: consistent with §VI A.  
- Phase‑2 ranges, p‑values: numbers in abstract match Table VII.  
- DESIVAST void numbers: n_void ≈ 56,981, Δf≈0.0007, p≈0.76: consistent with Table VIII–X.

The only serious **abstract‑body mismatch** is in *tone* and *reliance on Paper IV*:

**P5‑E4 (ESSENTIAL)**  
- **Location:** Abstract, §I–II.  
- **Problem:**  
  - The abstract phrases the main result as if Paper IV’s monopole is a fully established systematic with negligible uncertainty. In the body you admit that Paper IV is “in preparation” and that its monopole uncertainty is nontrivial.  
  - PRD cannot accept an abstract whose main calibration rests on unpublished work.  
- **Required fix:**  
  - Either fully internalize the monopole estimation and catalog construction (make the paper self‑contained) or defer submission until Paper IV is public. Then rewrite the abstract to state clearly: “Using the chirality catalog of [3], we…” with [3] being a citable arXiv/journal article. Right now this is not satisfied.

---

## 6. Data‑availability and provenance

**P5‑M9 (MAJOR)**  
- **Location:** Appendix C.  
- **Problem:**  
  - Data/code availability is described via a GitHub organization “Hubify‑Projects/bigbounce” and internal directories. There is mention of “DOI-minted archival snapshot” but no actual DOI is given.  
- **Required fix:**  
  - Provide a concrete, persistent DOI (Zenodo or similar) for the exact version used in the analysis.  
  - In the main text, replace long path lists with a concise statement: “All analysis scripts and outputs necessary to reproduce our results are available at DOI:XXXX.”

---

## 7. Stand‑alone‑reader test

**P5‑E5 (ESSENTIAL)**  
- **Location:** Throughout.  
- **Problem:**  
  - The paper repeatedly relies on “Paper IV” for:  
    - definition of the chirality catalog (what images, classifier architecture, TTA scheme)  
    - the catalog‑wide monopole and its uncertainty  
    - the selection‑function systematics by DESI imaging leg.  
  - It also assumes DESIVAST and ASTRA details without fully defining them. A reader who cannot open any companion paper or VAC would not be able to reconstruct the argument.  
- **Required fix:**  
  - Add a self‑contained “Chirality catalog” subsection that defines: data source, magnitude limit, classifier, label definition, quality cuts, and gives the monopole estimate with uncertainties.  
  - Add a concise but complete description of DESIVAST void membership and of your point‑in‑sphere tests.  
  - Strip out dependence on internal labels like “Paper II/III” for the physical interpretation; keep the interpretation generic.

---

## 8. Length vs. contribution

**P5‑M10 (MAJOR)**  
- **Location:** Whole manuscript (31 pages).  
- **Problem:**  
  - For the scientific contribution—essentially a null test of chirality vs environment using one catalog and standard binomial and χ² statistics—the paper is extremely long and cluttered with internal QA and pipeline details. PRD expectations for methods papers are high, but the core science could be presented in ~15–18 pages.  
- **Required fix:**  
  - Compress:  
    - Move most of the QA “closure wave,” file‑path references, and detailed z‑shell and Phase‑2 grid tests into a supplementary document.  
    - Keep in the main text only what is necessary to persuade a cosmology reader: data sets, main classification, primary void test, key cross‑checks, and systematics.  
  - Aim for **≤ 18 pages main text** plus appendices.

---

## 9. Miscellaneous style / minor issues

- **P5‑N6 (NIT):** There are occasional awkward phrasings and long parenthetical clauses that make the paper hard to read. A language polish pass is advisable.  
- **P5‑N7 (NIT):** Several places mention specific NSIDE, seed values, and exact Monte‑Carlo standard errors in excruciating detail. This is useful for an internal note but overkill for the main paper.

I did not see obvious duplicate phrases like “canonical canonical-mask” in your text, nor explicit future‑dated arXiv IDs beyond 2604.* which are valid for April 2026.

---

## Summary recommendation

**Recommendation: REJECT**

The central scientific idea—testing chirality independence from environment with DESI DR1 and DESIVAST—is sound and the internal numerics you present are reasonably consistent. However, the manuscript as given does **not meet PRD standards** because:

1. It depends critically on an **unpublished companion catalog paper (Paper IV)** for its data product and main systematic calibration.  
2. It is written as a **pipeline QA report**, not a concise PRD article: heavy use of internal tags, file paths, and version labels; overlong analysis‑tree exposition; and lack of standalone exposition of core ingredients.  
3. Several stylistic and methodological issues (σ comparability, effect-size statements, self‑contained definitions) require substantial restructuring.

I would encourage resubmission *after* Paper IV is publicly available and after a substantial rewrite that internalizes the catalog description, removes internal bookkeeping language, and compresses the presentation.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E6 (ESSENTIAL)  
- **Issue type:** Arithmetic / σ and p‑value recomputation  
- **Location:** Abstract, first long sentence on DESIVAST void bin; §VIII B, Table VIII context.  
- **Text:**  
  - Abstract: “…the counting-statistics floor of ±2.4 pp (the 1σ binomial half-width of the n = 428 V-Web void bin; 2σ half-width ±4.8 pp), whose observed 1.64 pp offset is well inside the 1σ floor (−0.68σfrom half )…”  
- **Problem (new):**  
  - For \(n=428\), a 1σ binomial “half‑width” is \(\sqrt{0.5\cdot0.5/n}\approx 0.0241\), i.e. **2.41 pp**, so the statement “±2.4 pp” is arithmetically fine, but the *observed offset* is not 1.64 pp:  
    - Observed fraction: 0.4836 vs 0.5 → offset is \(-0.0164 = -1.64\) **percentage points**.  
    - In σ units: \(-1.64 \text{ pp}/2.41 \text{ pp} \approx -0.68σ\).  
  - The sentence “whose observed 1.64 pp offset is well inside the 1σ floor (−0.68σfrom half)” is numerically correct *only* if the “floor” is defined as 2.4 pp; but saying “well inside” is overstated: 1.64/2.4 ≈ 0.68, i.e. **only 0.68σ**, not “well inside” in any strong sense.  
- **Required fix:**  
  - Either rephrase to a purely σ‑based comparison (“whose observed −0.68σ deviation is below 1σ”) or state the ratio explicitly (“~0.7σ below half”). Avoid the “well inside” language, which over‑interprets a 0.68σ deviation.  

---

P5‑M11 (MAJOR)  
- **Issue type:** Arithmetic consistency across related σ / ∆f statements  
- **Location:** §II, first paragraph; §VIII F (cross‑survey P4 monopole residual).  
- **Text:**  
  - §II: Paper IV monopole: “0.4974±0.000279 — a −0.26 pp monopole offset from exact parity … ≈ 9σ.”  
  - §VIII F: “the P4 monopole ∆fCW = −0.0026 … projects to σpred ≈ 4.6σ on the chirality‑relevant subsample; the observed −5.00σ corresponds to ∆fCW ≈ −0.0028, ∼8% larger than the P4 catalog-mean.”  
- **Problem (new):**  
  - Using the Paper‑IV numbers as written:  
    - σ of the monopole: \(0.000279\) corresponds to 0.0279 pp.  
    - 0.26 pp / 0.0279 pp ≈ 9.3σ → consistent with “≈ 9σ”.  
  - On the DESI‑matched subsample (n = 791,635 unique spirals, §VIII F):  
    - A ∆f = −0.0028 gives σ ≈ \(−0.0028 / \sqrt{0.25/791{,}635} ≈ −5.0\), consistent with text.  
    - But if the underlying monopole is really −0.0026 as “global” and if selection into DR1 were unbiased, you would expect something closer to −4.6σ; the paper attributes the offset to stronger weighting of the BGS leg, but never quantifies what shift is expected **from that selection**.  
  - As written, it is arithmetically consistent but *interpretively incomplete*: the reader has to infer that an 8% monopole enhancement is expected from BGS weighting; there is no back‑of‑envelope “expected” enhancement shown.  
- **Required fix:**  
  - Add a short calculation or approximate argument quantifying the expected monopole shift from the BGS‑weighted subsample (e.g., from per‑leg fractions in Paper IV) and compare it numerically to the observed 8% enhancement, instead of only stating that it is “consistent” qualitatively.  

---

P5‑M12 (MAJOR)  
- **Issue type:** Abstract faithfulness / internal comparison to Shamir  
- **Location:** §XII C, last paragraph.  
- **Text:**  
  - “Shamir 2022  reported a ∼ 2 − 4% large-scale asymmetry … The present paper’s per-environment CW fractions sit at ∼ 0.497 with inter-class range 1.98 percentage points across the four V-Web classes (per Table III)… leaving no room for a residual environment-dependent chirality of the Shamir 2022 amplitude (2–4 pp would be required in at least one well-populated class).”  
- **Problem (new):**  
  - The argument silently assumes that any environment‑conditioned effect “of the Shamir amplitude” would show up as a ≥2 pp shift *in at least one single class* relative to the global monopole, but:  
    - You never specify any physical model that fixes such a pattern.  
    - A model could in principle distribute a 2–4% environment‑conditioned asymmetry over multiple classes in such a way that single‑class shifts are <2 pp but still generate a global 2–4% pattern.  
  - As written, “leaving no room…” is too strong given that you only bound **per‑class** ∆f and do not propagate this properly to a Shamir‑like global statistic.  
- **Required fix:**  
  - Soften to something like: “Our per‑class bounds imply that any environment‑conditioned component contributing to a 2–4% *global* asymmetry would have to be distributed across environments in a highly fine‑tuned way; we find no per‑class deviations at the 2–4 pp level.” Or, if you want a direct statement, explicitly derive a quantitative bound on any linear combination of class fractions that could mimic Shamir’s amplitude.  

---

P5‑M13 (MAJOR)  
- **Issue type:** σ comparability / null‑procedure comparability beyond headline tables  
- **Location:** §VI C (projected density); §VI D (within‑class density and redshift stratifications); §VII (Phase 2 sweep); §VIII E (maximal‑void HEALPix stratification).  
- **Text patterns:**  
  - “max class‑to‑overall bright-fraction deviation 1.5 pp”, “maximum |σobs − σpred| = 1.87”, “one of the four (Z3, −3.14) marginally exceeds the Bonferroni-4 |σ|=3.02 threshold…”, etc.  
- **Problem (new):**  
  - Your initial σ‑comparability disclaimer is given in the abstract and once in §V, but in several places you juxtapose different σ values that arise from **different effective nulls** (different N, different reference p, different selection) without restating the “not directly comparable” caveat. For example:  
    - In §VI D, you contrast raw σ for cluster z‑quartiles with the same 3σ Bonferroni threshold used elsewhere, but the reader might interpret −3.14σ in Z3 as “stronger” than −2.33σ without being reminded that these come from the same N but a different effective null (Paper‑IV monopole vs unique‑sample monopole).  
    - In §VII, single‑cell raw σ (e.g. 4.66) are compared side‑by‑side with monopole‑referenced residuals and with σpred values without reiterating that only σobs−σpred is meaningful.  
  - The reviewer checklist you are working against requires that **every time** such mixed σ values are put next to each other, the non‑comparability is explicit. You partially satisfied this for Tables III and V, but not consistently in the follow‑up prose.  
- **Required fix:**  
  - Add brief one‑line reminders at each of these multi‑σ juxtapositions, e.g. “Here again, σ values from different N and nulls are not directly comparable; the only meaningful comparison is to the appropriate monopole prediction or to the within‑family threshold.” This is editing, not new analysis, but it is required by the standard you said you were following.  

---

P5‑M14 (MAJOR)  
- **Issue type:** Abstract faithfulness / environment‑independence headline vs later caveats  
- **Location:** Abstract “Headline result” paragraph; §VI D bright/dark split; §XIII limitations.  
- **Text:**  
  - Abstract: “We interpret this as no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity…”  
  - §VI D, end: “this is the most notable residual structure in the paper after the catalog-monopole subtraction; … flagged as a diagnostic to be disentangled by future Rubin/LSST + DESI DR2 follow-up…”  
  - §XIII: RSD limitations and selection‑function caveats.  
- **Problem (new):**  
  - The abstract’s blanket “no evidence for environment‑dependent chirality” statement is too strong given that:  
    - You highlight a ≈2σ bright–dark sign‑flip within filament (and cluster) that correlates with V‑Web class and with program, and you explicitly state that the current data do not allow you to cleanly attribute this between selection function and astrophysics.  
    - In §XIII you admit that RSD and selection effects are not fully modeled.  
  - A literal reader could interpret the abstract as asserting that **no class of environment‑conditioned residuals remains at the 2σ level**, which is not what the body actually says.  
- **Required fix:**  
  - Qualify the abstract headline, for example: “We find no **statistically significant** evidence for environment‑dependent chirality at ≥3σ after accounting for the catalog‑wide monopole; a ∼2σ bright–dark residual correlated with V‑Web classes is present but consistent with selection‑function systematics and is left for future work.” This keeps the body and abstract in harmony.  

---

P5‑N8 (NIT)  
- **Issue type:** Dimensional clarity in EFT toy operator  
- **Location:** Appendix A.  
- **Text:**  
  - “Lparity ⊃ gϕ (∇i ϕ) (∇i ρ/ρbg ) (L̂ · ẑ)… with per-class |∆fCW| < 0.01 … an order-of-magnitude bound on the coupling gϕ |∇ϕ| in H0 units is …”  
- **Problem (new):**  
  - You never state the units of ϕ, gϕ, or ∇ϕ; “in H0 units” is vague. Without at least a schematic definition (e.g. “take ϕ dimensionless and measure ∇ϕ in units of H0, so gϕ is dimensionless”), the reader cannot assess whether the bound is on a dimensionless coupling, a mass scale, or something else. This is a dimensional‑consistency gap, even though the main paper does not depend on the EFT.  
- **Required fix:**  
  - Insert one sentence fixing a consistent dimensional convention (e.g. “For concreteness, treat ϕ as dimensionless and express ∇ϕ in units of H0, so gϕ is dimensionless; the combination gϕ|∇ϕ|/H0 is then dimensionless.”) or remove “in H0 units” entirely and state the constraint symbolically.  

---

P5‑N9 (NIT)  
- **Issue type:** Minor arithmetic precision in descriptive text  
- **Location:** §IX A, selection‑corrected classifier robustness; §VIII E, maximal‑void HEALPix stratification.  
- **Text examples:**  
  - “the in-window void volume fraction collapses from 17.6% to 0.75% (≈23×)”  
  - “the DESIVAST void definition restricts to the volume-limited z ≤ 0.24 BGS sample, where 98.8% of the z ≤ 0.24 spirals are in the bright program (nbright /nlz = 56,477/56,981 = 99.1% for void-assigned spirals…)”  
- **Problem (new):**  
  - 17.6/0.75 ≈ 23.5, so “≈23×” is fine but a bit under‑rounded; similarly 56,477/56,981 ≈ 0.992, i.e. 99.2%, not 99.1%. None of these affect conclusions, but they are easy to tighten.  
- **Required fix:**  
  - Adjust the leading digits or explicitly use “≈23.5×” and “≈99.2%” to avoid avoidable off‑by‑0.1% rounding noise in a paper that otherwise emphasizes numerical rigor.  

---

If you want, I can also step through one or two figures and tables explicitly (with assumed counts) to produce a concrete arithmetic audit checklist you can run against your code outputs.