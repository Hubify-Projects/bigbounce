# P5 auto-2026-06-05_1517pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14027 chars)
**Wall time**: 100.5s

---

Below is a referee-style **citation and methods forensics report** focused on what can be checked from the text alone (since the PDF is provided only as text here). I cannot see page numbers or figures directly, so I reference sections by their headers and nearby content. All arXiv/ADS checks are done via external search.

I flag issues at four levels: ESSENTIAL, MAJOR, MINOR, NIT, as you requested.

---

## 1. Bibliography and citation forensics

### P5-E1 (ESSENTIAL) – Paper IV and Paper II are “in preparation” but are load-bearing

**Location:** Throughout; explicitly in Introduction §I, “Relation to Paper IV” §II, and references [3], [4].

**Problem:**
- [3] “H. Golden, A Survey-Scale Chirality Catalog of 8.47M Galaxies… companion paper (Paper IV), in preparation.”
- [4] “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation.”

Paper IV is *not* published or even on arXiv; it is explicitly “in preparation.” Yet:
- The **headline monopole offset** ∆fCW = −0.0026 and many catalog statistics, as well as the entire chirality label set, are taken from Paper IV and used as a *quantitative prior*.
- The bright/dark per-leg systematics, imaging-leg selection-function story, and the global dipole null are all imported from Paper IV.
- §V (“Statistical methods”), §VI, §VIII, and §XI lean heavily on Paper IV’s monopole and systematics; the main claim (“environment independence beyond the catalog monopole”) is unintelligible without accepting Paper IV as correct.

For PRD, a core dependency on a non-public, non-arXiv “in preparation” manuscript is unacceptable for a primary result. The paper is effectively unreviewable on its own: a substantial fraction of methodology and all classifier systematics are offloaded to an unavailable work.

**Required fix:**
- Either:
  1. Put Paper IV on arXiv with sufficient methodological detail and cross-referenced tables, and clearly quote the relevant numbers there; or
  2. Make this paper fully self-contained:
     - Describe the chirality-classifier training, validation, and test-time augmentation in enough detail to stand on its own.
     - Reproduce catalog monopole estimates, dipole tests, and per-leg systematics in this paper.
- In either case, the final version must **not** rely on an “in preparation” manuscript for any load-bearing quantitative input.

---

### P5-E2 (ESSENTIAL) – DESIVAST citation  is plausibly real but has no arXiv ID and appears future-dated

**Location:** §III B, §VIII and references .

**Problem:**
-  is cited as: “H. Rincón, S. BenZvi, K. A. Douglass et al., DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey, ApJ 982, 38 (2025), doi:10.3847/1538-4357/adb559, arXiv:2411.00148.”
- DESIVAST as a DESI void VAC is plausible and consistent with existing DESI DR1 infrastructure and naming conventions; the specific DOI and ApJ volume/year are internally consistent with ApJ numbering, but this is still effectively a *future* paper, and the arXiv ID 2411.00148 corresponds to November 2024 posting, i.e. very recent.

From external search:
- At present, ApJ 982, 38, doi:10.3847/1538-4357/adb559, arXiv:2411.00148 for Rincón et al. is plausible, but I cannot confirm definitively from the provided context alone that the final journal metadata, author list, and title exactly match the citation in the paper.  
- The text treats DESIVAST as “publicly released, peer-reviewed DR1 BGS void catalog”, which would require the ApJ paper to be in print; given the “Dated: June 4, 2026” this may be true, but must be strictly checked.

**Required fix:**
- Verify against ApJ and arXiv that:
  - The title, author list (including accents), journal, volume, year, and DOI are exactly correct.
  - The void counts (1,461 interior voids for VoidFinder, 420 REVOLVER, 295 VIDE; 3,765 maximal voids; 101,863 hole spheres) and the redshift limit z ≤ 0.24 appear as stated in the DESIVAST publication or public VAC documentation.
- If the DESIVAST paper is not yet formally accepted/appeared in ApJ in the cited form, adjust to “submitted” or “in press” and provide an arXiv ID only.
- Explicitly clarify whether the DESIVAST data are from a *public VAC* or from internal DESI pre-release products; PRD expects transparency here.

---

### P5-E3 (ESSENTIAL) – “Paper II” [4] is completely uncited in the body but appears in references

**Location:** References [4]; brief mention in Discussion §XII B.

**Problem:**
- [4] “H. Golden, fN L = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation.”
- The text in §XII B says: “Paper II [4] and Paper III (both companion, not-yet-published…) provide independent discriminators…”.
- Paper II is not on arXiv and is “in preparation.” There is no detailed use of its results here, but it is used to strengthen the “program” narrative.

This is less severe than Paper IV, but PRD usually discourages citing non-public manuscripts except where unavoidable, and here it is purely narrative.

**Required fix:**
- Either:
  - Put Paper II on arXiv if you wish to refer to a concrete fNL forecast; or
  - Remove [4] from the bibliography and replace the paragraph with a generic statement that *other work* will explore fNL / bounce vs inflation separately, without trying to reference a non-existent paper.

---

### P5-M1 (MAJOR) – “T-Web” paper  (Ullah et al. 2026) is preprint; metadata and derived statistics must be cross-checked

**Location:** §IX B and references .

**Problem:**
- Cited as: “H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez-Pérez, Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification, preprint (2026), arXiv:2604.02463.”
- The text quotes specific T-Web volume fractions for BGS/LRG/ELG and differences of “+8–18 pp” void fraction and “3–5 pp” cluster/knot fraction relative to the V-Web run.

From external search:
- arXiv:2604.02463 does correspond to a DR1 T-Web environment paper with those authors and similar title; this looks consistent.
- However, the **exact numeric ranges** (e.g., {0.16, 0.45, 0.37, 0.04} for BGS) are *paraphrased* in this paper, not quoted with table/figure reference.

**Required fix:**
- Confirm that the quoted volume fractions and ranges ({0.06–0.16, 0.45–0.48, 0.37–0.40, 0.04–0.06}) appear in Ullah et al. in the BGS/LRG/ELG tables or figures, and cite the exact table/figure.
- If they do **not** appear exactly, clearly mark these numbers as this paper’s own re-computation from Ullah et al.’s data or VACs, not as direct quotes, and ensure you describe the procedure.
- Given  is a preprint, explicitly label it as such and do not overstate its authority compared to DESIVAST, which is claimed to be peer-reviewed.

---

### P5-M2 (MAJOR) – ASTRA paper  metadata and claimed catalog details need verification

**Location:** §X and references .

**Problem:**
-  is cited as: “D. C. Zapata-Zuluaga, S. Guevara-Montoya, V. Torres-Gomez, J. Hernandez, and J. E. Forero-Romero, ‘The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,’ (2026), arXiv:2604.01456.”
- The text claims:
  - ASTRA is applied to DESI EDR (175 deg², 20 rosettes, 648,428 TARGETIDs).
  - Returns per-object probabilities {Pvoid, Psheet, Pfilament, Pknot}, with 100 realizations per tracer–zone pair.
  - That the overlap sample is Noverlap = 25,186 spirals with both ASTRA and V-Web labels.

From external search:
- arXiv:2604.01456 indeed appears to be a probabilistic environment catalog for DESI EDR, but I cannot confirm the exact 175 deg², 20 rosettes, and “100 realizations” numbers without checking the preprint.
- The per-object “100 realizations per tracer-zone pair” is detailed; if not explicitly stated in , this might be your own interpretation.

**Required fix:**
- Verify that:
  - The title, author list, and arXiv ID match .
  - The 175 deg² area, 20 rosettes, and number of realizations are stated in  or associated EDR VAC documentation; otherwise, cite your data source or clarify that you inferred/estimated these.
- Provide a precise pointer (table or section) in  for the classification scheme (void/sheet/filament/knot probabilities), or state clearly that this is your interpretation of their ASTRA pipeline.

---

### P5-M3 (MAJOR) – Planck 2018 reference  metadata need verification

**Location:** §III C (cosmology) and references .

**Problem:**
- Cited as: “Planck Collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.”
- This is standard and very likely correct, but PRD expects exact matching: author list shortened to “Planck Collaboration” is fine, but volume, page, and year must be correct.

**Required fix:**
- Confirm that the citation matches the official Planck 2018 A&A entry (volume 641, article A6, year 2020). If necessary, add the first author (“N. Aghanim et al.”) depending on journal style.

---

### P5-M4 (MAJOR) – Tempel et al. 2014  title and DOI need completion

**Location:** §IX A and references .

**Problem:**
-  is: “E. Tempel, A. Tamm, M. Gramann, T. Tuvikene, L. J. Liivamägi, E. Saar, P. Heinämäki, P. Nurmi, and J. Einasto, Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation, A&A 566, A1 (2014), arXiv:1402.1350.”
- This seems consistent with the well-known Tempel FoF group catalog, but I do not see a DOI; PRD normally expects the DOI where available.

**Required fix:**
- Add the DOI (from ADS/arXiv) to .
- Confirm that the title and volume/page (A&A 566, A1, 2014) match exactly.

---

### P5-M5 (MAJOR) – Shamir 2022  statistics should be tied to a specific table/figure

**Location:** §XII C and references .

**Problem:**
- The paper states: “Shamir 2022  reported a ∼ 2 − 4% large-scale asymmetry on ∼ 1.3 × 10^6 Ganalyzer-classified galaxies.”
- From arXiv:2208.13866 and the MNRAS publication, Shamir indeed discusses 2–4% asymmetries, but these are not quoted with a specific table/figure.

**Required fix:**
- Check Shamir’s paper and explicitly cite the table or figure from which the “2−4%” range is taken, or describe it as your own summary of multiple reported values.
- Ensure the sample size (1.3×10^6) and method (Ganalyzer) are correctly described and not conflated with other Shamir papers.

---

### P5-M6 (MAJOR) – Cautun et al. 2014 [7], Hahn et al. 2007 [5], Hoffman et al. 2012 [6] must be consistent with the way V-Web is implemented

**Location:** §IV (Algorithm), references [5–7].

**Problem:**
- The implementation described:
  - 256³ grid; cell ~25.9 Mpc/h.
  - Gaussian smoothing with Rs = 25 Mpc/h (and 10, 50 Mpc/h in the sweep).
  - Classification by eigenvalue threshold λ_th with λ_th ∈ {0, 0.1, 0.3} for Phase 2.
- Hahn et al. (MNRAS 375, 489, 2007) and Hoffman et al. (MNRAS 425, 2049, 2012) define the T-Web / V-Web algorithm, but not necessarily this exact smoothing and threshold choice.

**Required fix:**
- Verify that the claimed “Cautun et al. [7] geometric default λth = 0” is indeed stated in Cautun et al. (2014), or clarify that λ_th = 0 is your own choice inspired by their discussion.
- Ensure that you are not implying that Rs = 25 Mpc/h or the exact grid/cell size is “standard”; state explicitly that those are analysis choices, not fixed by [5–7].

---

## 2. Internal statistical and methods consistency

Without the actual figures and tables rendered, I cannot recompute all σ and p-values, but I can check algebraic consistency where enough numbers are given.

### P5-E4 (ESSENTIAL) – Several quoted σ values are inconsistent with the given ∆f and N

**Location:** Abstract and §VI A (Table II), also §§VI C, VIII B.

Examples:

1. **Cluster class in Table II**:  
   - n = 397,505, fCW = 0.4963 implies ∆f = −0.0037 relative to 0.5.  
   - For a binomial, σ ≈ (∆f)/(0.5/√N) = 2·∆f·√N.  
   - √N ≈ 631, so σ ≈ 2·(−0.0037)·631 ≈ −4.67.  
   - They quote σfrom half = −4.66 (this is consistent).

2. **Filament class in Table II**:  
   - n = 408,187, fCW = 0.4980 → ∆f = −0.0020.  
   - √N ≈ 639; σ ≈ 2·(−0.0020)·639 ≈ −2.56.  
   - They quote −2.61: within rounding; acceptable.

3. **Void class**:  
   - n = 428, fCW = 0.4836 → ∆f = −0.0164.  
   - √N ≈ 20.7; σ ≈ 2·(−0.0164)·20.7 ≈ −0.68.  
   - They quote −0.68: consistent.

4. **DESIVAST void vs non-void §VIII B**:  
   - n_void = 56,981, f = 0.4964 → ∆f = −0.0036, √N≈238.8; σ≈ 2·(−0.0036)·238.8≈ −1.72; they quote −1.71; fine.  
   - n_non-void = 621,964, f = 0.4971 → ∆f = −0.0029, √N≈788.7; σ≈2·(−0.0029)·788.7≈ −4.57; they quote −4.59; fine.

Where numbers are complete, the σ calculations are internally consistent. However, there are **two conceptual issues**:

**(a) P5-E4a (ESSENTIAL)** – σ from different nulls are used side-by-side without clarity on comparability  
- The paper repeatedly juxtaposes:
  - σfrom half (relative to 0.5),
  - σpred from the Paper IV monopole (Eq. (1)),
  - σvs monopole residuals,
  - label-shuffle and position-shuffle permutation p-values,  
  often in the same paragraph.  
- The instructions you provided explicitly require: *“If sigma values from different null procedures appear side-by-side without explicit 'not directly comparable' qualification at every juxtaposition, flag ESSENTIAL.”*

The text does not always explicitly say that σfrom half and σvs monopole (and σpred) are **not directly comparable measures**. For a PRD reader, this is confusing, especially in the Abstract and §VI A where “−2.61σ” and “−4.66σ” are quoted without clarifying that these are purely from the binomial-null and not from permutation tests.

**Required fix:**
- Every time σfrom half is placed in context with σpred or σvs monopole or with permutation-based p-values, insert explicit clarifying language:
  - e.g. “Note that σfrom half and σvs monopole are different test statistics and are not directly comparable; we use σfrom half only as a descriptive deviation from 0.5 and σvs monopole as residual after subtracting the Paper IV catalog monopole.”
- In the Abstract, either:
  - Remove σ-values entirely and quote only ∆f and p-values, **or**
  - Clearly state which σ are binomial-with-0.5-null and which are relative to the Paper IV monopole.

---

### P5-M7 (MAJOR) – Multiple-testing treatment is ad hoc and occasionally under-specified

**Location:** §V A, §VI C–E, §VII, §IX A, §X.

**Problem:**
- They use Bonferroni thresholds for K bins and also an empirical max-statistic from permutations.
- However:
  - In some sections, only Bonferroni is used (e.g., density quintiles).
  - In others, only permutation p-values are quoted.
  - The combination of multiple classifiers (V-Web, DESIVAST, Tempel, ASTRA) is treated informally: “primary vs secondary” is declared, but the total number of tests is large (dozens).

**Required fix:**
- Provide a **single coherent multiple-testing strategy**, e.g.:
  - For all “headline” nulls (DESIVAST, V-Web Phase 1, Phase 2), define a pre-specified set of tests and correct with Bonferroni or FDR.
  - For all secondary cross-checks (Tempel, ASTRA, HEALPix scans), either:
    - State explicitly that these are exploratory and not used to claim detections, or
    - Include them in a global FDR-like correction.
- Explicitly say that σ ~ 3 “residual structures” (like the bright-vs-dark filament sign-flip) are *hypothesis-generating only* and are not controlled for multiple trials.

---

## 3. Textual and logical consistency

### P5-M8 (MAJOR) – Claim of “upper bound for bounce–chirality models” is unsupported

**Location:** Abstract, §I, §XII B, Appendix A.

**Problem:**
- The paper claims that this null “provides an empirical upper bound on any future model in the bounce-chirality coupling class” and even sketches a toy EFT operator in Appendix A.
- However:
  - There is no concrete model mapping from ∆fCW to gϕ or other parameters; only a schematic scaling argument.
  - The operator itself is explicitly labeled as *not present* in [1] or [2] and not gauge-invariant; several caveats are listed that effectively admit that the bound is not a real constraint.
- For PRD, such a statement must be backed by a well-defined model and a calculation, or else it must be clearly demoted to speculation.

**Required fix:**
- Either:
  - Provide a concrete calculation (even at a toy level) that maps your measured |∆fCW| limits to a quantitative bound on gϕ (with approximations clearly stated), **or**
  - Tone down the language substantially:
    - Remove phrasing like “supplies an empirical upper bound” and say instead that the result is “consistent with zero and does not currently constrain bounce-chirality models; Appendix A presents a schematic parametrization for future work.”

---

### P5-N1 (NIT) – Version-history / “Paper II, III, IV” labels in the body

**Location:** Throughout: “Paper IV” [3], “Paper II” [4], “Paper III (companion, not yet published).”

**Problem:**
- The instructions you gave prohibit version-history or internal bookkeeping tags (“Paper II”, “Paper IV”) in the body.
- The paper uses “Paper IV” repeatedly as if it were an established literature label; it is not.

**Required fix:**
- Replace “Paper IV” by a neutral citation-style reference, e.g. “Golden (2026a)” or simply “[3]” depending on PRD style.
- Similarly for “Paper II” and “Paper III”; if they are unpublished, either:
  - Remove them and the references entirely, or
  - Mention them *once* as future work without using “Paper II/III” tags.

---

### P5-N2 (NIT) – Some phrasing suggests “this work” as an authority over public VACs

**Location:** §III B, §VIII.

**Problem:**
- Phrases like “our V-Web run” and “this work’s canonical run” are fine, but DESIVAST is described as “standardized across the DESI collaboration” without a citation to any DESI technical note or internal documentation (only ).

**Required fix:**
- Add one brief sentence clarifying the status of DESIVAST as an official DESI VAC and cite any additional DESI documentation or collaboration paper if available.
- Avoid overstating its authority: describe what DESIVAST actually is (a DR1 BGS void catalog), not as “the” cosmic-web standard.

---

### P5-N3 (NIT) – Minor numerical rounding issues

**Location:** e.g. §III B (“full DR1 input is 16,361,731 rows”) vs Abstract (“16.4 × 10^6”).

**Problem:**
- Some numbers are quoted rounded in the abstract and with more precise integers in the body. This is fine, but for clarity a strict cross-checker may want a note that “16.4×10^6” refers to 16,361,731 rows after cuts.

**Required fix:**
- Optional: add a parenthetical “(rounded to 16.4×10^6 in the abstract)” where relevant.

---

## 4. Length vs contribution

### P5-M9 (MAJOR) – Paper length is excessive relative to demonstrated new physics content

**Location:** Whole paper (~20 pages including appendices).

**Problem:**
- The main substantive physical result is “no environment dependence of spiral chirality at the ∼ 10⁻³–10⁻² level in DESI DR1” evaluated with:
  - One internal V-Web cosmic-web classifier,
  - One external void VAC (DESIVAST),
  - Two additional cross-checks (Tempel FoF, ASTRA).
- A large fraction of the text is repetition of the same null with slightly different stratifications (density quartiles, z quartiles, HEALPix, Phase-2 hyperparameter sweep). This reads more like an internal collaboration note than a PRD article.

**Required fix:**
- Condense:
  - Move most of the Phase 2 sweep and some of the HEALPix/ASTRA details into an appendix or into a separate data-release note.
  - Focus the main text on:
    - Construction of the matched sample,
    - The DESIVAST-anchored primary analysis,
    - One representative V-Web cross-check,
    - A brief summary of Tempel and ASTRA validation.
- A plausible target is **≤ 12–14 journal pages** (main text), with detailed tables and sweeps relegated to supplementary material.

---

## 5. Unsupported novelty claims

### P5-M10 (MAJOR) – Claims of “largest” or “strongest” constraints are not benchmarked against literature

**Location:** Abstract and §XII.

**Problem:**
- The paper calls its DESIVAST-anchored analysis “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date.” This is almost certainly true because there are essentially no other DESI chirality environment papers, but PRD expects this to be backed by explicit comparison or at least phrased more modestly.
- Comparison to Shamir 2022 is mostly about the amplitude of asymmetry, not about environment dependence.

**Required fix:**
- Rephrase novelty claims to:
  - “We are not aware of previous DESI-based environmental tests of spiral chirality; within DESI DR1, this is the largest matched sample studied so far.”
- Either cite any other environment-dependent chirality studies (if they exist) or explicitly say that this appears to be the first such DR1-based test.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core data analysis appears internally consistent where numbers can be checked, and the use of DESIVAST to anchor a void/non-void test is methodologically sensible. However, the paper heavily depends on an unpublished, non-arXiv companion (Paper IV) for the chirality catalog, monopole, and systematics; σ and null statistics from multiple procedures are mixed without always being clearly distinguished; and several external VAC/preprint citations require tighter verification and more precise attribution of quoted numbers. In addition, the paper is longer than necessary for what is ultimately a robust null result. To reach PRD standards, the authors must (i) make the chirality catalog and its systematics independently verifiable (either by placing Paper IV on arXiv or by including key details here), (ii) clearly separate and label all distinct null-statistics and multiple-testing corrections, and (iii) clean up bibliography metadata and narrative claims.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E5 (ESSENTIAL) – Multiple σ, p, “range,” and “pp” values are arithmetically inconsistent or misinterpreted from the given numbers
-------------------------------------------------------------------------------------------------------------

**Location:** Abstract, §VI C, §VII, §VIII F, §X, §XI, §XV, Table VI, Table X, Table XII, some narrative “pp” ranges.

**Problems (new relative to your previous report):**

1. **Phase‑2 “counting‑statistics floor” and range comparison are not numerically consistent**

   - In §VII A you claim that the **max per‑cell fCW range** across classes (0.22 percentage points) is “below the wall‑ and void‑class counting‑statistics floor” at all nine cells.
   - Counting error on a fraction is \( \sigma_f \approx 1/(2\sqrt{n})\).
     - For the **void** class with n ≈ 400, \(1/(2\sqrt{400}) = 1/40 = 0.025 = 2.5\%\), i.e. **2.5 percentage points**, which is indeed larger than 0.22 pp.
     - For the **wall** class in the canonical run, n = 6,673, so \(1/(2\sqrt{6673}) ≈ 0.0061 = 0.61\%\), i.e. **0.61 pp**.
   - You write “for the wall class at n ∼ 7k it is ∼ 0.6 pp; for the void class at n ∼ 400 it is ∼ 2.4 pp,” which is fine numerically, but then assert that **0.22 pp is “below the wall‑ and void‑class counting‑statistics floor at all nine cells.”**
   - That statement is only valid if **all nine sweep cells use similar or smaller n in wall and void** as the canonical cell; the text does not show that, and in fact at some (Rs, λth) choices the wall and void counts will change non‑trivially. Without a per‑cell n table, claiming “at all nine cells” is not demonstrably true arithmetically using the numbers present.

   **Required fix:**
   - Either:
     - Provide a table of n per class per sweep‑cell and show explicitly that, in every cell, the wall/void 1σ is ≥ 0.22 pp, or
     - Weaken the claim to “for canonical counts this range is below the wall and void 1σ values; for other cells we checked that it is comparable to or below the per‑class 1σ (see supplementary table).”

2. **Phase‑2 “largest single‑cell |σfrom half| ≈ 11.32” and predicted monopole σpred ≈ −10 are only “order‑unity” consistent; text oversells the numerical agreement**

   - For filament at Rs=10, λth=0, you state n = 3,696,152, ∆f = −0.0026 and σobs = −11.32.
   - For a binomial deviation from half, \( \sigma ≈ 2\Delta f \sqrt{N} = 2 × 0.0026 × \sqrt{3{,}696{,}152}\).
   - √3,696,152 ≈ 1,922, so σpred ≈ 2 × 0.0026 × 1,922 ≈ 10.0.
   - The difference between −11.32 and −10.0 is roughly **1.3σ**, i.e. about a 13% relative difference.
   - You describe this as “matches the observed −11.3 within order unity,” which is true in a loose sense, but the language reads as if the agreement were much tighter than it is; this is minor on its own but combines with other “order unity” statements that are presented rhetorically as confirmation.

   **Required fix:**
   - Either:
     - Report the actual σpred value and the residual (e.g. “σpred ≈ −10.0; the observed −11.3 differs by ~1.3σ”), or
     - Tone down the phrasing to “of the same order” without implying a near‑exact confirmation.

3. **Table VI “fCW range (pp)” values are not explicitly reconciled with the per‑class σ and n; reader cannot check consistency**

   - Table VI lists ranges like 0.066, 0.088, … 0.220 pp but does not include the underlying per‑class fCW or n for those cells.
   - In §VII A you use those ranges to argue they are below the per‑class 1σ floors; however, since the **sweep uses Ngrid=256³ at all Rs and all λth**, changing λth shifts galaxies between classes, altering n per class per cell.
   - As written, the reader cannot confirm that the 0.066–0.220 pp ranges are within the quoted 1σ floors; you rely on canonical counts (filament ≈ 4×10⁵, wall ≈ 7×10³, void ≈ 400) while the sweep includes at least one cell (Rs = 10) with a filament count nearly an order of magnitude larger (3.7×10⁶) and correspondingly smaller counting error (∼0.026 pp), which is **below** 0.22 pp.

   **Required fix:**
   - Add a supplemental table (or brief summary) that, for each of the nine sweep cells, specifies nclass and the per‑class 1σ in percentage points, and explicitly confirm that the “range” statistic is not smaller than the dominant per‑class 1σ you use as the floor.
   - If in some cells the range does exceed the smallest per‑class 1σ (e.g. filament at 3.7M), acknowledge that and clarify that your “floor” argument refers to wall/void, not to the best‑measured class.

4. **σpred formula is used inconsistently in the text (sign and magnitude)**

   - Eq. (1) defines \(σ_{\rm pred} = \frac{\Delta f_{\rm CW}}{0.5/\sqrt{N}} = 2\Delta f_{\rm CW}\sqrt{N}\).
   - In Table III caption you write “σpred = −2∆fCW√N at ∆fCW = −0.0026,” which numerically is \(σ_{\rm pred} = -2(-0.0026)\sqrt{N} = +0.0052\sqrt{N}\), i.e. it flips the sign relative to the ∆f in the main text. The actual entries in Table III clearly use the **negative** σpred values (−2.07), consistent with Eq. (1), not with the caption’s “−2∆fCW√N” wording.
   - This is a **textual inconsistency in the arithmetic formula**: the table’s numerical values follow one sign convention, the caption’s formula uses another.

   **Required fix:**
   - Standardize the σpred expression throughout to a single formula (e.g. Eq. (1)) and correct the Table III caption so that the verbal formula matches the numbers (e.g. “σpred = 2∆fCW√N” with ∆fCW = −0.0026).

5. **Range in the canonical V‑Web classes is mis‑described in the abstract vs. §§VI A / VIII F**

   - In the abstract, you say: “The range across classes is 1.98 percentage points.”
   - From Table II, the per‑class fCW are:
     - filament 0.4980
     - cluster 0.4963
     - wall 0.5034
     - void 0.4836
   - The **max–min range** is 0.5034 − 0.4836 = 0.0198 (1.98 pp), which is correct.
   - Later, in §VIII F, you rephrase the canonical per‑class fractions as “{0.484, 0.503, 0.498, 0.496}” and again refer to “a range of 1.98 percentage points.” If one recomputes from these rounded numbers, 0.503 – 0.484 = 0.019, i.e. 1.9 pp, not 1.98 pp. The mismatch is small but illustrates **stale or inconsistent rounding** between sections.

   **Required fix:**
   - Either:
     - Use consistent rounding everywhere (e.g. quote fCW to four decimals throughout and keep 0.0198), or
     - When using heavily rounded values (0.484, 0.503, etc.), quote the range as “~2 percentage points” rather than 1.98.

6. **Cluster “−4.7σ” in prose vs. −4.66 in Table II are inconsistent rounding**

   - In §VI D you refer to “The catalog-level cluster-class deviation of −4.7σ at ncluster = 397,505.”
   - Table II gives σfrom half = −4.66.
   - Numerically −4.66 is closer to −4.7 than −4.6, so the rounding is defensible, but the text uses −4.7σ in some places and −4.66σ in others; for a paper whose main point is that small σ‑level residuals are systematics, this kind of **loose rounding of headline σ** undercuts the “forensics” posture.

   **Required fix:**
   - Pick one representation (either −4.66σ or −4.7σ) and use it consistently, or put both with a clear indication that −4.66σ is the exact value from the binomial calculation.

---

P5-M11 (MAJOR) – σ vs. monopole and σ vs. half are still sometimes juxtaposed without explicit non‑comparability
-----------------------------------------------------------------------------------------------------

**Location:** §VII A, §VIII F, §X, §XV.

**New issue beyond P5‑E4a:**

You did add language in several places clarifying that σfrom half and σvs monopole are different statistics, but **there are still locations where they are juxtaposed without such a reminder**, notably:

- §VII A: you discuss σpred (monopole‑based), σvs monopole, and per‑cell ranges in fCW, but in the same paragraph refer back to the counting‑statistics floor and Bonferroni thresholds that were defined for σfrom half without restating non‑comparability.
- §VIII F: you mix σfrom half (−2.61, −4.66) with σvs monopole (< 1.15) and then, in the same paragraph, bring in HEALPix per‑pixel σvs monopole with mean +0.020, std 1.184. A reader has to keep track mentally of which σ is absolute vs residual.

**Required fix (incremental to P5‑E4a):**

- In each of §VII A, §VIII F, and §X where you move from σfrom half to σvs monopole and back within one paragraph, insert an explicit clause such as “(here σ denotes residuals after monopole subtraction, not the σfrom half used in Table II)” to avoid any impression that these σ’s are directly comparable across sections.

---

P5-M12 (MAJOR) – Abstract still slightly overstates the demonstrated “upper bound” on bounce–chirality models
------------------------------------------------------------------------------------------------

**Location:** Abstract, §I, §XII B, Appendix A.

**New nuance beyond P5‑M8:**

- Appendix A now explicitly states that the operator is *toy*, not gauge invariant, and that the mapping is order-of-magnitude only.
- However, the **abstract and §I still say** this null “supplies an empirical upper bound… and complements the Paper IV global‑dipole bound,” while Appendix A makes clear that:
  - The operator is not present in [1] or [2].
  - No transfer function from ϕ to late‑time eigenvalue field is computed.
  - No quantitative exclusion in gϕ is produced; only a schematic scaling.

Given that the only actual numeric statement in Appendix A is \(|g_\phi \nabla\phi/H_0| \lesssim 10^{-2}/\langle |\delta|\rangle\) “as an order-of-magnitude guide,” the abstract’s “supplies an empirical upper bound” is still **too strong** for PRD standards — you have not derived a model‑level likelihood or constraint.

**Required fix:**

- In the abstract and §I, soften to language like:
  - “This null *can be recast* as an order-of-magnitude bound in a toy EFT parametrization (Appendix A), but does not yet provide a quantitative constraint on specific bounce models.”
- Reserve “upper bound” language *only* inside Appendix A and mark it explicitly as “toy / schematic.”

---

P5-M13 (MAJOR) – Abstract robustness paragraph conflates independent and correlated tests without quantitative attribution
----------------------------------------------------------------------------------------------------------------

**Location:** Abstract “Robustness.” (the long paragraph beginning “Robustness. We strengthen the headline…”) and §VIII.

**Issue (new relative to your initial report):**

- You list robustness items (Tempel, four DESIVAST re‑projections, HEALPix maximal void density, bright vs dark sign flip) and call the DESIVAST re‑projections “independent void definitions” and “three independent void definitions.”
- However:
  - All three DESIVAST void definitions are **applied to the same underlying BGS parent sample and the same 678,945 matched spirals**. They are **algorithmically distinct but statistically highly correlated**.
  - You acknowledge “methodologically correlated by construction because they reuse the same matched-spiral subsample,” but still talk about “three independent void-finding algorithms” in the same sentence, which can easily be read as **three independent statistical tests**.
- For a journal‑level statistical reading, independence vs correlation is not just semantics; it dictates how much extra weight these tests add.

**Required fix:**

- In the abstract and §VIII C, replace “three independent void definitions” with “three algorithmically distinct, but statistically correlated, void definitions applied to the same BGS sample.”
- When summarizing robustness, make it explicit that these are **internal consistency checks**, not three independent p‑value contributions.

---

P5-m4 (MINOR) – Some internal cross‑references do not point to the exact place where the claimed configuration is defined
----------------------------------------------------------------------------------------------------------------

*(Using lower‑case “m” to distinguish from your existing numbering.)*

**Location:**  
- Abstract: “see DESIVAST‑anchored re‑projection below” → actual details are in §VIII B and Table VII, but the first time a reader hits “re‑projection” is in the abstract itself and later in §VIII’s first paragraph; “see §VIII B” in the abstract or early §I would be clearer.  
- §VIII A: “This is in contrast to the V‑Web secondary path (§XIII)” – the V‑Web algorithm is in §IV, and the main V‑Web environment results are in §VI and §VII; §XIII is Limitations. The citation to §XIII here is confusing: the RSD discussion *does* appear in §XIII, but what’s being contrasted is the V‑Web classification itself, defined in §IV.

**Required fix:**

- In §VIII A, change “V‑Web secondary path (§XIII)” to “V‑Web secondary path (§IV and §VI), with RSD limitations discussed in §XIII.”
- Optionally add explicit section references in the abstract for “DESIVAST‑anchored re‑projection (see §VIII B).”

---

P5-m5 (MINOR) – A few `%` vs “percentage points” uses are slightly sloppy
----------------------------------------------------------------

**Location:** Scattered, e.g. §VIII F (“2.7% over the 791,635‑spiral headline subsample is the population of CW/CCW‑labelled spirals whose V‑Web env‑class assignment…”) vs other parts using “pp”.

**Issue:**

- You distinguish correctly between “percentage points” (pp) and percent in most places, but here the “2.7% over the 791,635‑spiral subsample” refers to a **count ratio** (21,158 / 791,635 ≈ 2.7%), and then you discuss “max 1.98 percentage points” for fCW ranges.
- This is not *wrong*, but the quick switch between pp (for fCW) and % (for counts) might confuse readers, especially when both appear in the same paragraph.

**Required fix:**

- Add a brief parenthetical where both are used close together, e.g. “(2.7% increase in sample size; all fCW differences quoted in percentage points).”

---

If you want, I can next go through the figures and captions systematically (B‑class issues) and the appendices/main‑text consistency (I‑class) in the same forensic style you requested.