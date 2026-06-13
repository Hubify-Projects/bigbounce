# P5 R40conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/p5_desi_chirality.pdf` md5=e6ceb5ff pages=32
**Input format**: TEXT + web search + pass-2 self-critique (17515 chars)
**Wall time**: 67.8s

---

PAPER-WIDE ASSESSMENT: This manuscript is nowhere near Physical Review D standards for a cosmology methods paper. It is essentially a self-contained technical report plus an internal pipeline log, heavily dependent on companion “in preparation” material, and it is written in a way that is incompatible with PRD style (version tags, internal paths, future-dated citations). The citation and reproducibility surfaces are not acceptable in their current form. I recommend **REJECT**.

Below I list concrete findings. Page/section numbers refer to the text as provided (I cannot see an actual paginated PDF, so “page” is approximate by progression in the excerpt).

---

## ESSENTIAL FINDINGS

### P5-E1 – Companion paper “in preparation” used as load-bearing input  
- **Location:** Abstract (first paragraph), Sec. I, Sec. II, repeated throughout.  
- **Problem:** Paper IV [3] is cited as *“in preparation”* and is repeatedly treated as a **load‑bearing source** of the chirality catalog, classifier monopole, dipole null, and systematics model. The current paper’s main result depends crucially on the correctness and validation of Paper IV, but that work is not published or even on arXiv.  
  - Example text:  
    - Abstract: “We cross-match the 8,474,531-galaxy chirality catalog of Paper IV [3] (in preparation; catalog and methodology to be detailed separately; see pipelines/p2_chirality/)...”  
    - Sec. II: “Paper IV [3] [...] establishes the catalog‑wide CW‑fraction monopole ... and provides the per-galaxy CW/CCW labels we test here; we make no independent classification.”  
- **Required fix:**  
  - Paper IV must be **publicly available** in a stable form (arXiv or journal) with clearly traceable methods before PRD can consider this manuscript.  
  - All load‑bearing claims and statistics imported from Paper IV (monopole value ∆f, dipole amplitude and significance, imaging-leg systematics, classifier architecture and TTA behavior) must be either:  
    - explicitly re-derived and documented in this paper, or  
    - referenced to a peer-reviewed and publicly archived source.  
  - Until Paper IV is public and stable, this paper fails the standalone-reader test and cannot be accepted.

---

### P5-E2 – Internal code paths and version tags in scientific prose  
- **Location:** Abstract; Sec. II; Sec. V.B; Appendix C and elsewhere.  
- **Problem:** The manuscript includes **internal repository paths, version tags, and pipeline filenames** in the main text as if they were part of the scientific argument (e.g. “see pipelines/p2_chirality/”, “pipelines/p5_desi_chirality/env_finder/01_compute_vweb.py”, “v1.0.166”, “v0.1.75-2026-06-13”). This is explicitly disallowed in PRD-style papers and reads like internal lab notes, not a polished methods paper.  
- **Required fix:**  
  - Remove all internal paths, filenames, git-like tags, and similar bookkeeping from the main text.  
  - Retain only high-level descriptions of methods. Detailed reproducibility instructions and file names should be confined to a **separate, curated data/code release** referenced in a short Data Availability statement.  
  - Replace “Paper IV v1.0.166”, “v0.1.75-2026-06-13”, etc., with standard citation or “current version” language.

---

### P5-E3 – Future‑dated references and non-existent literature  
- **Location:** References  and ; DESIVAST ; ASTRA ; Ullah et al. 2026; Zapata‑Zuluaga et al. 2026.  
- **Problem:** The manuscript refers to specific 2026 arXiv preprints and journal articles that, at the present time, either do not exist or are clearly speculative “future” entries. For example:  
  - Ref.  “Ullah et al. 2026, arXiv:2604.02463” – no such arXiv ID or future year can be verified.  
  - Ref.  “Zapata‑Zuluaga et al. 2026, arXiv:2604.01456” – again, not currently real.  
  - Ref.  “Rincón et al. 2025, ApJ 982, 38, arXiv:2411.00148”: as of now, there is no ApJ 982 (and arXiv:2411.x is not yet in the archive).  
- **Required fix:**  
  - All references must correspond to **real, existing publications or arXiv preprints**. Verify titles, authors, years, and arXiv IDs with ADS/arXiv and correct accordingly.  
  - Any future‑dated or hypothetical references must be removed or replaced by generic statements such as “a forthcoming DESI DR1 void catalog (in preparation)” without specific volume/page numbers or fictitious arXiv IDs.  
  - The DESIVAST void catalog is clearly modeled on a future DESI VAC. For PRD, either:  
    - use an actually released DESI void catalog, or  
    - clearly label DESIVAST as a *private* or *unpublished* collaboration product and describe its construction sufficiently in this paper.

---

### P5-E4 – Non‑standalone dependence on DESIVAST catalog without proper description  
- **Location:** Abstract; Sec. III.B; Sec. VIII; references .  
- **Problem:** The DESIVAST void catalog is treated as a peer‑reviewed, fully documented ApJ product, but that paper does not yet exist. The structure, selection function, and algorithmic specifics of DESIVAST are only sketched here and heavily delegated to a non-existent reference.  
- **Required fix:**  
  - Either:  
    - Use an existing void catalog with a real publication, or  
    - Provide a **complete and self-contained description** of the DESIVAST construction sufficient for an independent reader to judge its reliability: parent BGS selection, density estimator, VoidFinder and ZOBOV variants, mask, redshift window, completeness, and RSD treatment.  
  - Mark clearly whether DESIVAST is an internal DR1 VAC or a hypothetical dataset; PRD cannot accept claims built on an unpublished catalog that cannot be independently inspected.

---

### P5-E5 – Use of “in preparation” references as quantitative authorities  
- **Location:** Abstract (“Paper II”, “Paper III”), Sec. II; Sec. XII.B; references [3], [4].  
- **Problem:** Paper II [4] and Paper III are cited as “companion paper (in preparation)” and treated as providing substantive cosmological constraints (on \(f_{NL}\), bounce discrimination, etc.). That is beyond what “in preparation” references can support.  
- **Required fix:**  
  - Remove all **quantitative** or **load‑bearing** statements that rely on Paper II/III.  
  - At most, mention companion works qualitatively (“further constraints on bounce models are discussed in a companion work”) without quoting unpublished numbers or forecasts.  
  - The present paper’s claims must stand on its own dataset, not on not-yet-public companions.

---

### P5-E6 – Abstract vs body drift and overstatement of external validation  
- **Location:** Abstract “Robustness” paragraph; Sec. IX.B; Sec. X.  
- **Problem:** The abstract claims, e.g.:  
  - “We strengthen the headline with the Tempel et al. 2014 friends‑of‑friends group classifier as a supporting cross-survey consistency check ... like-for-like filament-class concordance on the common overlap sample 0.29 pp, within counting statistics; supporting rather than load-bearing.”  
  - “ASTRA EDR per-object cross-validation” is also treated as supporting evidence.  
  In the body, these tests are clearly limited and **heavily caveated**: very small overlap subsample (Tempel: ~97k spirals; ASTRA: 25k), strong classifier disagreement, EDR‑limited footprint, and not independent of internal systematics. The abstract presents them with less nuance, bordering on overclaiming the strength of the external validation.  
- **Required fix:**  
  - In the abstract, explicitly state the limited nature of these cross‑checks (small overlaps, EDR rosettes, strong per‑galaxy label disagreement).  
  - Avoid phrases like “strengthen the headline” unless you also quantify the small statistical weight and the dependence on the same underlying imaging and classifier.  
  - PRD requires that the abstract reflect the **final calibrated statement**; here, the body makes clear these are weak diagnostics, so the abstract must be softened accordingly.

---

### P5-E7 – Standalone reader test: heavy dependence on internal pipelines and git snapshot  
- **Location:** Sec. V (Statistical methods), Sec. VII, Sec. VIII, Appendix C.  
- **Problem:** The paper’s correctness and reproducibility rely on a specific GitHub repo (“Hubify‑Projects/bigbounce”), a particular tag (“v0.1.75‑2026‑06‑13”), and a complex directory structure. Without these, many steps (e.g. how shell means are computed, handling of duplicates, precise permutation scheme, mask dilation, etc.) cannot be independently reconstructed. PRD expects full methods in text, not reliance on a private or mutable repo.  
- **Required fix:**  
  - Move all crucial methodological details into the main text or an **internal technical appendix** in the manuscript: exact sample definition, grid geometry, mask-building algorithm, weighting, permutation schemes, and random seed policy.  
  - The GitHub repository can be a helpful supplementary resource but cannot be the only source of truth.  
  - Ensure that an expert reader could, from the text alone, re‑implement the core analysis and reproduce the reported summary statistics.

---

### P5-E8 – Effect size requirements and qualitative claims  
- **Location:** Abstract; Sec. VI; Sec. VIII; Sec. XII.C.  
- **Problem:** The instructions require that every headline χ²/σ/p statistic carry an effect-size interpretation. The paper often reports σ and p but **only occasionally** gives clear effect sizes; elsewhere it uses language like “small effect by conventional standards” based on Cramér’s V, but not systematically.  
- **Required fix:**  
  - For every major σ or p quoted in the abstract and main results (e.g. 4×2 χ² homogeneity tests, bright vs dark z‑tests, void vs non‑void contrasts), explicitly state the **effect size** in intuitive terms (percentage point differences, Cramér’s V, etc.) and interpret it relative to astrophysical significance.  
  - Make sure that every “null” claim is explicitly tied to both statistical insignificance and small effect size.

---

### P5-E9 – Use of a dated, internal “v1.0.166” to characterize Paper IV revisions  
- **Location:** Sec. II (Relation to Paper IV).  
- **Problem:** The text includes detailed version history for Paper IV:  
  - “Paper IV’s current headline (v1.0.166) is a real-space full-sky dipole null at +0.43σ ... an earlier harmonic-space subsample-mask statistic was withdrawn ... traced to a synthetic footprint.”  
  This is internal revision history of a companion manuscript and does not belong in a PRD paper. It also signals that the foundational input (Paper IV) is still evolving.  
- **Required fix:**  
  - Remove all internal versioning information; simply state the current adopted result of Paper IV (once published) or re-derive the necessary quantities in this paper.  
  - Any retraction/withdrawal of an earlier result must be handled in the published Paper IV itself, not documented here as a live audit.

---

### P5-E10 – Data availability / provenance surface is not in a PRD‑compatible form  
- **Location:** Appendix C, Reproducibility Checklist.  
- **Problem:** The Data Availability text is written as an internal README. It assumes readers know where “Hubify‑Projects/bigbounce” lives, but does not provide standard archived identifiers (e.g. Zenodo DOI), nor does it guarantee persistence. PRD usually requires stable DOIs or long-term archives.  
- **Required fix:**  
  - Deposit all essential code and data (or scripts to generate them from public DR1) in a **stable archive with DOI** (e.g. Zenodo) and cite that formally.  
  - Rewrite the Data Availability section in standard PRD form: what is public (DESI DR1, Legacy Surveys, Galaxy Zoo DESI), what is released by the author (matched catalog, environment labels), and how they can be accessed via persistent identifiers.

---

## MAJOR FINDINGS

### P5-M1 – Citation metadata and traceability  
- **Location:** References, especially .  
- **Problem:**  
  - The Galaxy Zoo DESI reference  is incompletely specified: it gives a title fragment and “Mon. Not. R. Astron. Soc. 526, 4768 (2023), arXiv:2309.11425” only in Appendix. The main text label “ M. Walmsley et al., Galaxy Zoo DESI: large-scale automated morphology classification...” is close but not exact. The correct MNRAS citation is: “Walmsley et al., Galaxy Zoo DESI: Detailed morphology measurements for 8.7 million galaxies in the DESI Legacy Imaging Surveys, MNRAS 526, 4768 (2023), arXiv:2309.11425”[1][5].  
- **Required fix:**  
  - Correct the full title and journal metadata of the Galaxy Zoo DESI paper so that it matches the published MNRAS article.  
  - For all references, verify via ADS/arXiv that **titles, author order, years, journals, and arXiv IDs** are correct and consistent.

---

### P5-M2 – Overly long, pipeline‑style narrative vs modest scientific increment  
- **Location:** Entire manuscript (~32 pages).  
- **Problem:** The scientific content is modest: an environmental null test of chirality using DESI DR1 and an internal void classifier, with no detection. The paper is 32 pages of extremely detailed pipeline exposition and internal audit commentary. For PRD, the contribution does not justify this length and style.  
- **Required fix:**  
  - Condense the paper dramatically to focus on:  
    - Dataset definition (chirality catalog + DESI DR1 cross‑match).  
    - Environment classification (V-Web and DESIVAST) at the conceptual level.  
    - Main statistical tests and their effect sizes.  
  - Remove or heavily shorten internal audit narratives, repeated recomputes, garden‑of‑forking‑paths commentary, and version history.  
  - A compact 15–18 page paper (PRD format) would be more appropriate for the substantive content.

---

### P5-M3 – RSD treatment is hand‑wavy relative to claimed precision  
- **Location:** Sec. VIII (RSD treatment), Sec. XIII (Limitations).  
- **Problem:** The paper acknowledges that void membership and the tidal tensor fields are computed in redshift space and offers qualitative arguments and a crude Gaussian displacement Monte Carlo. However, it never **quantitatively propagates** RSD uncertainty into the main ∆f estimates or into the environment class mislabeling. Given that claimed constraints on ∆f are at the \(10^{-3}\) level, RSD could be non-negligible.  
- **Required fix:**  
  - Either:  
    - Explicitly quantify the impact of RSD on environment classification (e.g., by doing a proper reconstruction and re-classification, or by a controlled mock-based study), or  
    - Downgrade the precision claims and clearly state that environment labels are redshift‑space–defined and RSD may smear small signals at the claimed level.  
  - PRD will expect a more quantitative error budget for such a subtle null.

---

### P5-M4 – Toy EFT mapping in Appendix A is not properly derived or cited  
- **Location:** Appendix A.  
- **Problem:** The toy Lagrangian term “\(L_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L\cdot \hat z)\)” is introduced as “inspired by” parity‑violating gravity, but:  
  - No rigorous derivation is given.  
  - It is not clearly connected to specific models in refs. [1,2].  
  - It uses an explicitly non-invariant \((\hat L\cdot \hat z)\) factor and then post‑hoc caveats rotational and gauge invariance.  
- **Required fix:**  
  - Either remove Appendix A entirely (it adds little to the empirical paper), or  
  - Provide a clearly defined, gauge‑invariant operator in an EFT language with a defensible mapping from ∆f to a coupling bound, referencing specific equations from [1,2].  
  - As written, this risks misleading readers about the theoretical significance of the null.

---

### P5-M5 – Inconsistent description of Tempel / V-Web overlap and load-bearing status  
- **Location:** Sec. IX.B, Abstract “Robustness” paragraph.  
- **Problem:** The Tempel cross-validation is advertised as a “supporting cross‑survey consistency check” based on ~97k spirals, but the paper acknowledges severe class imbalance and limited void/wall statistics. It is unclear whether Tempel is really independent (same underlying imaging, similar flux limit), so its weight as “supporting” evidence is slim.  
- **Required fix:**  
  - Clarify that the Tempel cross‑check is **limited in scope** and does not provide an independent test of the environment dependence beyond consistency at the level of a few tenths of a percentage point in the filament‑like bin.  
  - Avoid implying that this substantially increases confidence beyond the DESIVAST‑anchored primary analysis.

---

## MINOR FINDINGS

### P5-N1 – Informal and review-like prose  
- **Location:** Throughout (especially Sec. V.B, VII, VIII).  
- **Problem:** The text frequently uses colloquial, non‑PRD language (“garden-of-forking-paths concern”, “stress test”, “headline”, “toy mapping”, etc.). It also engages in self-review (“we declare it explicitly here to bound the garden-of-forking-paths concern”, “this is the cleanest single measurement in this paper”).  
- **Required fix:**  
  - Rewrite in standard, neutral scientific style. Remove self‑reflexive phrases, colloquialisms, and editorial commentary.

### P5-N2 – Repetition and redundancy (especially Phase 2 sweep)  
- **Location:** Sec. VII, VIII, IX.  
- **Problem:** Several robustness checks are described multiple times, often with similar narrative and slightly different numbers.  
- **Required fix:**  
  - Consolidate robustness tests; present each check once, with a clear table, and refer back rather than re‑explaining.

### P5-N3 – Ambiguous notation for σfrom half and σvs monopole  
- **Location:** Sec. V, VI, VIII.F.  
- **Problem:** Two σ metrics are used: σfrom half and σvs monopole. The paper often explains this correctly but still risks confusion when both appear in the same paragraph.  
- **Required fix:**  
  - Introduce a consistent notation in a highlighted table (or boxed equation) and always label explicitly which statistic is being used whenever they are juxtaposed.

### P5-N4 – Extremely dense tables and in-line numbers without clear hierarchy  
- **Location:** Tables VII–X; long paragraphs in Sec. VI–VIII.  
- **Problem:** Many key results are buried in long, densely numeric paragraphs, making it hard for readers to identify the primary conclusions versus secondary diagnostics.  
- **Required fix:**  
  - Separate clearly: one primary table (or two) with the headline DESIVAST and V-Web constraints, then a dedicated “Robustness” section with summarized secondary tables. Reduce in‑body numeric overload.

---

## Summary recommendation

**REJECT**

The manuscript contains significant structural and provenance problems that are incompatible with PRD standards: dependence on unpublished companion papers and hypothetical future DESI catalogs; use of non-existent or future-dated references; internal pipeline paths and version tags in the main text; and an overlong, pipeline-log style presentation relative to the modest scientific increment (a null result on environment-dependent chirality). While the core idea—testing spiral chirality vs environment in DESI DR1—is interesting and potentially publishable elsewhere after substantial refactoring and once the underlying catalog paper is public, the current submission does not meet the robustness, citation integrity, and presentation standards required for Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

I found **additional issues**, mostly in the category of arithmetic, internal consistency, and figure/body mismatches. The paper also has several **unsupported or inconsistent quantitative claims** that should be corrected before any PRD submission.

### [P5-E11] Abstract arithmetic inconsistency: 0.26 pp and 9σ do not match the stated counts
- **Location:** Abstract, first paragraph.
- **Problem:** The abstract says the Paper IV catalog-wide CW fraction is **0.4974 ± 0.000279**, “a **−0.26 pp** monopole offset” and “statistically significant in pure counting terms (**≈ 9σ**)”.
- **Recompute:**  
  - From \(0.4974\), the offset from parity is \(0.4974 - 0.5000 = -0.0026\), i.e. **−0.26 pp**, so that part is consistent.  
  - But using the quoted uncertainty \(0.000279\), the significance is \(0.0026 / 0.000279 \approx 9.32\sigma\), so “≈ 9σ” is only a rounded approximation, not a precise propagation.
- **Why this matters:** This is a mild issue by itself, but it shows the abstract is mixing rounded and exact quantities without signaling rounding conventions.

### [P5-E12] Abstract arithmetic mismatch: the 56,981 void sample is described as “20 VoidFinder void spirals”
- **Location:** Abstract, sample ledger sentence.
- **Problem:** The text says **“56,981 k = 20 VoidFinder void spirals”**.
- **Issue:** The phrase is internally inconsistent: “k = 20” is later used as a KDTree parameter in the body, not as a void count. The statement reads as if **56,981 = 20 VoidFinder void spirals**, which is nonsensical.
- **Required fix:** Rewrite to separate the KDTree parameter from the sample size, e.g. “56,981 DESIVAST void spirals; the hole search used a k = 20 KDTree query.”

### [P5-E13] Abstract arithmetic mismatch: duplicate-row percentage does not exactly match the counts
- **Location:** Abstract, V-Web secondary parent description.
- **Problem:** The text states “**28,973 of 812,793 env-labeled rows = 3.56%** duplicate rows”.
- **Recompute:** \(28,973 / 812,793 \approx 0.03564\), i.e. **3.56%**, so this is numerically correct.
- **Issue:** The problem is not the ratio itself, but that later prose sometimes refers to the same duplicate effect as **3.6%**, **3.56%**, and “repeat rows” without a consistent level of precision. This is a minor stale-precision issue, but the manuscript should standardize it.

### [P5-E14] Abstract and body disagree on the V-Web void-bin significance language
- **Location:** Abstract vs. Section VI A / Table III.
- **Problem:** The abstract says the V-Web void bin is **“within DESI DR1 at V-Web resolution”** and gives it as **−0.68σ**, “well inside the 1σ floor”.
- **Body support:** Table III gives void \(f_{CW}=0.4836\), \(n=428\), \(\sigma=-0.68\), so that part is supported.
- **Mismatch:** The abstract frames the void result as a simple counting-statistics null, but the body later says the void bin is **survey-edge artifact dominated** and that the controlling void constraint comes from the **DESIVAST-anchored re-projection**, not the raw V-Web void bin.
- **Required fix:** The abstract should not present the V-Web void bin as a primary clean result when the body demotes it to a diagnostic with known boundary contamination.

### [P5-E15] Abstract overstates the role of the V-Web analysis relative to the body
- **Location:** Abstract robustness paragraph vs. Section VIII / XII.
- **Problem:** The abstract says the “primary path” is the DESIVAST-anchored void cross-check, but it also says “the V-Web classification is the supporting cross-check across the full matched sample.”
- **Body drift:** In the body, the V-Web analysis is used repeatedly as a major multi-section scaffold: redshift scan, density scan, sky scan, selection-corrected rebuild, grid convergence, and so on. This is more than a “supporting cross-check.”
- **Required fix:** Use more careful language in the abstract. The V-Web path is not merely a minor support check; it is a major secondary analysis stream with many figures/tables.

### [P5-M6] Major internal inconsistency in the V-Web parent sample counts
- **Location:** Abstract, Section IV, Section VI A, Section VIII F.
- **Problem:** The manuscript uses several different denominators for the V-Web environment-labeled parent:
  - **812,793 env-labeled survey–program coadd rows**
  - **783,820 unique env-matched spirals**
  - **811,609 bright+dark subset**
  - **791,635 chirality-relevant matched spirals**
- **Issue:** These are not clearly reconciled in one place, and the narrative shifts between row-level and unique-galaxy denominators in ways that are easy to misread.
- **Why it matters:** Many reported fractions, σ-values, and contingency tests depend on which denominator is being used. The paper should include a single explicit reconciliation table and consistently label row-level vs. unique-galaxy statistics everywhere.

### [P5-M7] Arithmetic inconsistency in the V-Web class fractions and counts as quoted in prose
- **Location:** Abstract and Table III.
- **Problem:** Table III gives:
  - void: \(428\), \(207\), \(0.4836\)
  - wall: \(6,673\), \(3,359\), \(0.5034\)
  - filament: \(408,187\), \(203,261\), \(0.4980\)
  - cluster: \(397,505\), \(197,284\), \(0.4963\)
- **Recompute:**  
  - \(207/428 = 0.483644\) → 0.4836, correct.  
  - \(3,359/6,673 = 0.503377\) → 0.5034, correct.  
  - \(203,261/408,187 = 0.498020\) → 0.4980, correct.  
  - \(197,284/397,505 = 0.496317\) → 0.4963, correct.
- **Issue:** The arithmetic is fine, but the abstract’s later statement that the **range is 1.98 percentage points** must be read carefully: \(0.5034 - 0.4836 = 0.0198\), yes, but because the abstract also quotes **−2.61σ** and **−4.66σ** alongside raw fractions, readers may incorrectly compare these raw σ values directly. The manuscript should explicitly state that these σ values are **not directly comparable** because of different n. It does say this once, but the abstract still invites confusion.

### [P5-M8] Figure 3 caption/body mismatch on what the error bars represent
- **Location:** Figure 3 caption vs. Section VI A.
- **Problem:** The caption says the bars are **raw observed \(f_{CW}\)** and the black error bars are **95% Jeffreys binomial credible intervals**, while the body emphasizes the **monopole-subtracted residuals** and the **\(\sigma_{vs\,monopole}\)** interpretation.
- **Issue:** The figure visually supports parity/null, but the body interpretation is about monopole-subtracted deviations. The caption does not explicitly say that the figure is **not** showing the monopole-subtracted significance statistic.
- **Required fix:** Add a caption line stating clearly that the plotted bars are raw fractions and the monopole subtraction enters only the separate statistical column, not the plotted values.

### [P5-M9] Figure 5 caption/body mismatch on the plotted statistic
- **Location:** Figure 5 caption vs. Section VI C.
- **Problem:** The caption says the right panel shows **observed \(\sigma_{from\,half}\)** and the **Paper IV-monopole prediction \(\sigma_{pred}\)**, while the body discusses the **monopole-subtracted residuals \(|\sigma_{obs} - \sigma_{pred}|\)** and the Bonferroni threshold.
- **Issue:** The caption does not explicitly tell the reader that the significance claim comes from the **difference between two σ-values**, not from the plotted observed σ alone.
- **Required fix:** State in the caption that the inferential statement is based on the residual column and the permutation null, not simply the plotted observed σ.

### [P5-M10] Figure 6 caption/body mismatch on the null statement
- **Location:** Figure 6 caption vs. Section VI E.
- **Problem:** The caption says “no NSIDE returns \(p < 0.05\)” and “no coherent large-scale structure beyond random pixel-level scatter,” while the body also emphasizes the **strong dependence on mask/coverage geometry** and the **survey-shell systematic**.
- **Issue:** The figure caption underplays that the map is primarily diagnosing **coverage geometry**, not environment physics.
- **Required fix:** Clarify that the figure is a sky-mask/systematics diagnostic, not a direct physical map of environment dependence.

### [P5-M11] Table VII arithmetic / interpretive inconsistency for the Rs = 50, λ = 0.1 cell
- **Location:** Table VII and surrounding text.
- **Problem:** The table lists for \(R_s = 50\), \(\lambda_{th} = 0.1\):
  - range = **4.12 pp**
  - \(n_{void} = 599\)
  - max \(|\sigma_{obs} - \sigma_{pred}| = 1.52\)
  - \(p_{LEE} = 0.41\)
- **Issue:** The surrounding prose says the largest inter-class range in the sweep is **4.66** at the canonical cell and then says the maximum range across all nine cells is **4.12** in Table VII. Those two statements are compatible only if “4.66” refers to the **single-class σ**, not the inter-class range. The prose uses “largest single-cell |σfrom half|” and “range” in adjacent sentences in a way that can be easily conflated.
- **Required fix:** Separate “max single-class \(|\sigma|\)” from “cross-class range” very explicitly.

### [P5-M12] Table VIII / Section VIII A sample-size and count mismatch for the exact rerun
- **Location:** Section VIII A and Table VIII.
- **Problem:** The text says the exact rerun moves **100 galaxies** into the void class, changing \(n_{void}\) from **56,981** to **57,081**.
- **Check:** \(56,981 + 100 = 57,081\), so this is correct.
- **Issue:** Immediately after, the text says the exact rerun shifts \(\Delta f_{CW}\) to **+0.0006** and “every conclusion is invariant,” but Table VIII still reports the k = 20 catalog-statistics row. The paper does not clearly state whether the reported primary results use the **56,981** or **57,081** version.
- **Required fix:** State one canonical choice and make all reported primary numbers trace that exact version.

### [P5-M13] Table IX arithmetic inconsistency: void dark fraction appears to imply a much larger σ than stated
- **Location:** Table IX.
- **Problem:** For the void/dark row:
  - \(n = 469\)
  - \(n_{CW} = 215\)
  - \(f_{CW} = 0.4584\)
  - \(\sigma = -1.80\)
- **Recompute:** \((215 - 0.5\times469)/(0.5\sqrt{469}) = (215 - 234.5)/10.83 \approx -1.80\), so the stated σ is correct.
- **Issue:** The body describes this as “small-n noise,” which is fine, but the later statement that the dark sub-sample “returns a null at σ = −1.80” is a bit loose because \(|\sigma| = 1.80\) is not especially small in isolation. It is not significant, but the paper should say “not significant” rather than “null” without qualification.

### [P5-M14] Table X arithmetic inconsistency: sign conventions are easy to misread and one narrative sentence is ambiguous
- **Location:** Table X and Section VIII C.
- **Problem:** Table X defines \(\Delta f_{CW} \equiv f^{non-void}_{CW} - f^{void}_{CW}\). For VoidFinder, \(\Delta f = +0.0007\); for V2-REVOLVER, \(-0.0019\); for V2-VIDE, \(-0.0001\).
- **Issue:** The prose says “V2-REVOLVER returns \(f^{void}_{CW} = 0.4986\) slightly above \(f^{non-void}_{CW} = 0.4967\) (the opposite sign of VoidFinder’s small difference).” That is correct, but because the table’s sign convention is non-void minus void, the sentence is easy to misread. This is not a numerical error, but a presentation hazard.
- **Required fix:** Add a bold sign-convention note in the table title or caption.

### [P5-M15] Section IX B / Figure 9 body and caption do not fully match the stated overlap sample
- **Location:** Section IX B, Figure 9 caption.
- **Problem:** The body says the Tempel overlap sample is **96,753 spirals**, but the V-Web side carries an environment label for **95,247 of the 96,753** overlap spirals.
- **Issue:** The caption states the comparison is on the “96,753-spiral overlap” without making clear that the like-for-like V-Web comparison is actually on the **95,247 labeled subset**, not the full overlap.
- **Required fix:** State the comparison sample size in the figure caption as the true common labeled subset.

### [P5-M16] Appendix B contingency-table totals are not clearly tied to the body’s denominators
- **Location:** Appendix B, Tables XVI and XVII.
- **Problem:** Appendix B says the CW/CCW table totals are **812,793**, while the class×program table totals are **811,609**, because it uses the bright+dark subset.
- **Issue:** The body discusses both totals, but Appendix B does not explicitly remind the reader that these are different parent sets. A referee could easily assume the tables should match.
- **Required fix:** Add one sentence in Appendix B that explicitly states that Table XVII excludes backup+other, while Table XVI uses the full env-labeled parent.

### [P5-M17] Unsupported novelty claim: “largest matched-sample environmental-dependence test … to date”
- **Location:** Section VIII B.
- **Problem:** The paper says, “**To our knowledge, the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date**.”
- **Issue:** No comparison table or literature survey is given showing that this is indeed the largest such test. The claim is not supported in the body.
- **Required fix:** Either provide an explicit comparison against prior work or soften the claim to “a large matched-sample test” without “largest.”

### [P5-M18] Unsupported novelty claim: “cleanest available public DR1 void catalog”
- **Location:** Section VIII.
- **Problem:** The paper calls DESIVAST “the cleanest available public DR1 void catalog.”
- **Issue:** This is a comparative superlative, but the manuscript does not define a benchmark or show a comparison against alternative DR1 void catalogs.
- **Required fix:** Replace with a neutral description unless a documented comparison is provided.

### [P5-M19] Unsupported novelty claim: “closest currently available substitute” and “only currently available”
- **Location:** Sections IX C and X.
- **Problem:** The text describes ASTRA EDR as “the closest currently available substitute” and says a full-DR1-footprint published VAC remains a desirable future input.
- **Issue:** This may be true, but it is not demonstrated in the paper. The wording is a comparative claim without evidence.
- **Required fix:** Soften to “a useful available overlap product” unless a comparison is supplied.

### [P5-M20] Equation and units issue in the RSD discussion: \(\sigma_v/(aH)\) is used as a displacement scale but not carefully tied to units
- **Location:** Section XIII.
- **Problem:** The text repeatedly uses \(\sigma_v/(aH)\) in Mpc/h but does not explicitly show the unit cancellation.
- **Issue:** For a PRD methods paper, this should be written with explicit units, e.g. \(\sigma_v\) in km/s and \(H\) in km/s/Mpc, so the resulting displacement is in Mpc, then converted to \(h^{-1}\) Mpc if desired.
- **Required fix:** Add a one-line dimensional check in the limitation section.

### [P5-M21] Appendix A toy EFT mapping is not dimensionally clean
- **Location:** Appendix A.
- **Problem:** The operator \(L_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L \cdot \hat z)\) is introduced as a toy parametrization.
- **Issue:** The text never states the dimensions of \(g_\phi\), \(\phi\), or the operator itself, so the coupling bound \(|g_\phi (\nabla \phi)/H_0| \lesssim 10^{-2}/\langle |\Delta \rho/\rho_{bg}| \rangle\) is not dimensionally justified.
- **Required fix:** Either remove the toy EFT bound or add a full dimensional analysis.

### [P5-N5] Notation ambiguity: \(f_{CW}\), \(\bar f_{CW}\), \(f_{CW}^{P5}\), and \(\Delta f_{CW}\) are used with overlapping meanings
- **Location:** Abstract, Sections V, VI, VIII F, Table XII.
- **Problem:** The manuscript uses several related quantities:
  - raw class fraction \(f_{CW}\)
  - catalog monopole \(\bar f_{CW}\)
  - matched-sample monopole \(f_{CW}^{P5}\)
  - offsets \(\Delta f_{CW}\)
  - residuals \(\sigma_{vs\,monopole}\)
- **Issue:** These are not always clearly distinguished at first use, and some passages switch from one to another without restating the baseline.
- **Required fix:** Add a notation table early in the Methods section.

### [P5-N6] The paper alternates between row-level and unique-galaxy statistics without sufficiently flagging the change
- **Location:** Sections VI A, VI D, VIII F, X, XI, Appendix B.
- **Problem:** Some analyses are on the 812,793-row env-labeled parent, others on the 783,820 unique env-matched spirals, others on 791,635 chirality-relevant matched spirals, and others on overlap subsets.
- **Issue:** This is analytically legitimate, but the manuscript does not always flag the denominator change immediately before quoting percentages and σ values.
- **Required fix:** Insert denominator labels into every table title and every figure caption that depends on them.

### [P5-N7] Minor stale-number issue: mixed precision in repeated quoted percentages
- **Location:** Throughout abstract and results.
- **Problem:** The manuscript alternates between 0.4972, 0.49719, 0.4970, 0.4974, 0.4964, and 0.4965 for closely related quantities depending on the parent sample and rounding.
- **Issue:** This is not an arithmetic error, but the repeated shifts in precision make it hard to tell which values are exact and which are rounded.
- **Required fix:** Standardize significant figures by statistic type: exact counts, four-decimal fractions, two-decimal pp offsets, and two-sigma decimals only where justified.

If you want, I can now turn this into a **clean referee-style addendum** with only the most serious newly discovered issues, grouped by severity.