# P4 auto-2026-06-08_1632pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 56.2s

---

The manuscript’s bibliography and quantitative claims contain numerous issues that do not meet Physical Review D standards. Below I list all problems found, with IDs, locations, and required fixes. I also flag a few structural/scientific‐presentation problems that would need revision for PRD.

Because only partial references [1]–[7], [8]–, –, –, –, –, – are visible in the excerpt, my audit is necessarily limited to those. For each, I checked against arXiv.org and NASA ADS where possible.

---

### 1. Reference and citation forensics

#### P4-E1 — Mis-cited Shamir 2022 paper and duplicate numbering  
- **Section/page:** References [2], [3],  block, p. 10  
- **Problem:**  
  - In the main text, “Shamir (2022) [3]” is associated with “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866.[3]  
  - In the reference list, [2] is given as “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” PASJ 74, 1114 (2022), DOI:10.1093/pasj/psac058.[2]  
  - [3] is given as “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866.[3]  
  - However, earlier text (“Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples (‘nearly 1.3 × 10^6 spiral galaxies’ per the published abstract).” p. 2) attributes to [3] the DESI Legacy analysis with “nearly 1.3 × 10^6 spiral galaxies.”  
  - NASA ADS shows that the “DESI Legacy Survey” spin paper is indeed MNRAS 516, 2281 (2022) with arXiv:2208.13866, as cited.[3] The PASJ 74, 1114 paper is a different Shamir 2022 paper.[2]  
  - There is no direct error in the titles/DOI themselves, but the text conflates the PASJ 2022 paper (general patterns) and the MNRAS 2022 DESI-specific paper under “Shamir (2022)” in some places.  
- **Required fix (ESSENTIAL):**  
  - Disentangle and clearly distinguish the two 2022 Shamir papers in text (e.g. “Shamir 2022a [2]” for PASJ 74, 1114 and “Shamir 2022b [3]” for MNRAS 516, 2281), and ensure statements about DESI Legacy sample size and asymmetry refer only to the correct paper.  
  - Audit all “Shamir (2022)” mentions to ensure they point to the appropriate reference number.

#### P4-M1 — Ambiguous or composite citation of Shamir DESI Legacy result  
- **Section/page:** Sec. I, p. 2 (“Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples (‘nearly 1.3 × 10^6 spiral galaxies’ per the published abstract).”)  
- **Problem:**  
  - The sentence combines results from Shamir 2020 (SDSS + Pan-STARRS; not DESI Legacy) and Shamir 2022 (DESI Legacy) into a single “DESI Legacy samples” description. Shamir (2020) [1] is a SDSS/Pan-STARRS spin paper, not DESI Legacy.[1] Shamir (2022) [3] is DESI Legacy.[3]  
  - The quoted “nearly 1.3 × 10^6 spiral galaxies” appears to be from the DESI Legacy MNRAS paper only, not from the 2020 work. Combining them is misleading.  
- **Required fix (MAJOR):**  
  - Split the discussion: attribute SDSS/Pan-STARRS amplitudes and σ-levels strictly to [1], and DESI Legacy amplitudes and sample size strictly to [3].  
  - Change wording so that only Shamir (2022) is described as “DESI Legacy Survey” and “nearly 1.3 × 10^6 spiral galaxies,” and ensure the 2–4% numbers are accurate for each paper separately (with explicit values if possible).

#### P4-E2 — Mis-stated numerical result for Jia et al. (CE-ResNet)  
- **Section/page:** Sec. I, p. 2 (“Jia et al. [7] introduced CE-ResNet … yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.”)  
- **Problem:**  
  - Jia et al. (2023) “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32, arXiv:2210.04168.[7] According to the abstract and results, the reported metric is an accuracy/fraction close to 0.998 (99.8%), but “cw/ccw = 0.998” is ambiguous: it could be interpreted as a ratio of counts rather than a success fraction.  
  - The manuscript uses “cw/ccw = 0.998” without defining whether this is an accuracy metric or a class-balance metric. In Jia et al., 0.998 refers to classification performance, not to an observed CW/CCW fraction in the universe.[7]  
- **Required fix (ESSENTIAL):**  
  - Clarify the quantity: e.g. “achieving **0.998 classification accuracy** on chirality labels for ∼1.95 million galaxies, with exact equivariance under flips.” Ensure that this matches Jia et al.’s stated metric (e.g. top-1 accuracy or F1; double-check in the paper).  
  - If any numerical value (0.998, sample size 1.95M) is not exactly what Jia et al. report in the abstract or main tables, correct it.

#### P4-M2 — Incomplete/uncited “Shamir 2012, 2020, 2022” σ and amplitude claims  
- **Section/page:** Sec. I, p. 2 (“Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼ 5–20% using ∼ 1.27 × 10^5 SDSS galaxies. Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries on DESI Legacy samples…”)  
- **Problem:**  
  - For PRD, all quoted σ ranges and percent asymmetries should be traceable to specific tables or figures in the cited works. I cannot verify exact numbers here without full access, but the text collapses multiple different samples and methodologies (SDSS 2012, SDSS/Pan-STARRS 2020, DESI 2022) into blended σ and % ranges.  
  - No uncertainties or exact statistics from the original tables are given; the manuscript uses broad ranges (2–4σ, 2–4%, 5–20%) that could be cherry-picked or imprecise.  
- **Required fix (MAJOR):**  
  - For each cited Shamir paper, quote the *specific* main statistic with its uncertainty and context (e.g. “Shamir (2012) reports an asymmetry \(A = X \pm Y\%\) in the northern hemisphere, corresponding to Zσ, for N galaxies; table/figure number.”).  
  - Clearly separate which numbers come from which paper, and avoid pooled ranges across distinct analyses.

#### P4-N1 — Missing arXiv IDs for several core cosmology references  
- **Section/page:** References –, p. 10  
- **Problem:**  
  - For Phys. Rev. D, arXiv identifiers are expected when available for cosmology/HEP theory papers. Several references beyond [1], [3], [7] lack arXiv IDs in the provided snippet (e.g., Lue et al. 1999 PRL , Cabass et al. 2023 PRD , Philcox 2022 PRD , Eskilt & Komatsu 2022 PRD , Eskilt et al. 2023 A&A , Hou et al. 2023 MNRAS , Cahn et al. 2023 PRL , Komatsu 2022 Nat. Rev. Phys. ). All have arXiv postings.  
- **Required fix (NIT, but PRD style):**  
  - Add arXiv IDs for all references where available, matching ADS/arXiv.  

#### P4-N2 — Data/code repository URLs in text conflict with “no URLs” guideline  
- **Section/page:** Data Availability, p. 9:  
  - “Catalog: https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog …”  
  - “Model: https://huggingface.co/bamfai/galaxy-chirality-v2 …”  
  - “Code: https://github.com/Hubify-Projects/bigbounce …”  
- **Problem:**  
  - PRD generally allows URLs in Data Availability statements, but the journal has specific format expectations. Here, repository names include hyphens and spaces (e.g., “galaxy- chirality- catalog”) which look like line-break artifacts; a referee should flag that these URLs as printed are likely uncopyable and do not exactly match real repository paths (extra spaces).  
- **Required fix (MINOR):**  
  - Ensure URLs match actual repositories exactly and are formatted without spurious spaces or hyphen breaks. Confirm that all three repositories exist and contain the promised artifacts.

#### P4-N3 — Potential duplicate reference topic / missing citation for Iye et al. spiral catalog  
- **Section/page:** Sec. I, p. 2 (“Iye et al. (2021) [5]… Tadaki et al. [6] likewise found null results.”)  
- **Problem:**  
  - Iye et al. (2021) and Tadaki et al. (2020) are correctly cited as spin-parity analyses with null results.[5][6] However, the “∼80,000 face-on spirals” language for Tadaki appears in [6]’s title and abstract.[6] The text here references “a catalogue of ∼80,000 face-on spirals” for Tadaki, which is consistent but should be numerically matched.  
- **Required fix (NIT):**  
  - Double-check the quoted “∼80,000” and the sample counts in Iye and Tadaki; if exact numbers (e.g. 80,249) are given in those papers, quote them precisely or state explicitly that the numbers are approximate.

---

### 2. Quantitative consistency and σ / p-value handling

Most quoted numbers in the text appear internally consistent, but several require explicit recomputation or are stated in ways that are ambiguous for PRD.

#### P4-E3 — Inconsistent “9.5σ from 0.5000” vs. tabulated uncertainty  
- **Section/page:** Sec. IV.B, p. 4 and Table II, p. 4  
  - Table II: Catalog C: cw/(cw + ccw) = 0.4974 ± 0.000279.[Table II]  
  - Text: “The Catalog C residual (9.5σ from 0.5000, Table II) is spatially uniform…”  
- **Problem:**  
  - From Table II, the deviation from 0.5 is \(|0.4974 - 0.5| = 0.0026\). With σ = 0.000279, the significance is \(0.0026/0.000279 \approx 9.33σ\), not precisely 9.5σ.  
  - A 0.2σ discrepancy is small but PRD expects exactness when numbers are used as “headline” significance. Elsewhere “9.5σ” is used as a “global monopole” descriptor; consistency matters.  
- **Required fix (MINOR):**  
  - Recompute and either quote 9.3σ, or recompute σ and p exactly and adjust both Table II and the text so the ratio matches to at least two significant figures.

#### P4-M3 — σ values from different nulls compared without repeating “not directly comparable” caveat  
- **Section/page:** Throughout, including Abstract p. 1, Declared Analysis Hierarchy p. 3, Sec. IV.C–D p. 4–5, Table I p. 4, Table III & IV p. 5  
- **Problem:**  
  - The manuscript states in the abstract: “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I…” This is good.  
  - However, multiple later juxtapositions directly compare σ’s from different nulls without re-stating non-comparability at the point of comparison, e.g.:  
    - “The post-MASTER canonical-mask direct-MC residual is +3.64σ … (empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent).” (abstract)  
    - “the canonical-mask post-MASTER residual is +3.64σ, a non-headline, systematics-attributed value…” (p. 5)  
    - Discussion of the “3.05σ hemisphere signal” vs. “0.43σ” simple dipole and “+6.48σ pre-MASTER” on the same page.  
  - Instruction 7 in the user prompt (and essentially PRD-level standards of clarity) requires strong, explicit caveats where σ’s from heterogeneous nulls are juxtaposed, not only once upfront.  
- **Required fix (ESSENTIAL):**  
  - At every location where σ’s from different null procedures are placed side-by-side in the same sentence or paragraph (e.g., “+3.64σ canonical… vs −0.122σ subsample-mask… vs 0.43σ real-space”), explicitly restate that these are relative to different nulls and not directly comparable.  
  - Alternatively, convert all such comparisons to p-values or Gaussian-equivalent σ referenced explicitly to each null, and state distinct nulls in the same sentence.

#### P4-M4 — Injection sensitivity numbers not transparently recomputable from visible inputs  
- **Section/page:** Sec. VI.A, p. 6 (“empirical injection-recovery sweep… gives P(σ > 3) = 0.55 at A = 0.75% and P(σ > 3) = 0.15 at A = 0.5%… headline 50%-recovery-3σ threshold A ≈ 0.75%… true-underlying threshold ∼ 1.88% using GZ1 dilution factor g ≈ 0.398.”)  
- **Problem:**  
  - The stated Fisher Poisson floor (0.29% full-amplitude) is given without showing the precise formula or plugging numbers; the reader must accept the arithmetic without reproduction.  
  - The mapping from catalog-level amplitude A to “true underlying threshold” 1.88% uses \(g = 2a - 1\) with a = 0.6991, but the text does not show the exact formula used (likely \(A_{\rm true} = A_{\rm obs}/g\)). From A = 0.75% and g ≈ 0.398, the implied underlying amplitude is \(0.75/0.398 ≈ 1.88\%\), which is consistent, but the chain of assumptions is not quantitatively shown.  
- **Required fix (MAJOR):**  
  - Add an explicit equation for the Fisher floor estimate and for the mapping between observed A and underlying true A via g, with all numerical values and errors stated.  
  - Include at least a small table or figure in Appendix C or VI.A showing the injection results for several amplitudes (0.5%, 0.75%, 1%, etc.) so that the 50% recovery at 3σ can be traced.

#### P4-M5 — Hemisphere look-elsewhere correction numbers partially opaque  
- **Section/page:** Sec. VI, p. 6; Appendix C, p. 8  
  - “3.05σ local maximum; after look-elsewhere correction via Bonferroni/BH across ∼ 650 directions, the post-LEE significance drops below |σ| < 1; the direct-MC pLEE ≤ 10−4 rejection is attributed to…”  
- **Problem:**  
  - The 3.05σ local maximum significance vs. pLEE ≤ 10−4 from MC appears contradictory if interpreted as Gaussian-equivalent p. A 3.05σ local maximum corresponds to p ~ 0.0023 (one-sided), while pLEE ≤ 10−4 implies ~3.9σ global. The text then claims that after Bonferroni/BH across ~650 directions, post-LEE significance is <1σ. It is not clear which statistic each p refers to, and how the sample of 650 directions maps to the 10,000 random-label shuffles.  
- **Required fix (MAJOR):**  
  - Carefully define:  
    - the “local” σ and its p-value;  
    - the exact “global” pLEE from MC;  
    - the Bonferroni or BH correction applied (what is “∼650 directions,” what constitutes a “test”).  
  - Present a single coherent LEE-corrected significance, or clearly separate “local statistic” vs “global maximum under null,” with explicit Gaussian-equivalent σ for each.

---

### 3. Internal consistency, text/logical issues

#### P4-E4 — Ambiguous sentence about “3.2×10^6 spirals (30× extension)”  
- **Section/page:** Sec. V.A, p. 5 (“These conclusions corroborate and extend the methodological critique of Iye et al. (2021) [5] with 3.2×10^6 spirals (30× extension).”)  
- **Problem:**  
  - It is unclear whether “3.2×10^6 spirals (30× extension)” refers to the current paper’s sample relative to Iye et al.’s, or to Iye’s own sample. Iye et al. have a face-on catalog of ~80,000 spirals.[6] 3.2×10^6 vs ~80,000 is ∼40×, not 30×.  
- **Required fix (MAJOR):**  
  - Explicitly state what the “30× extension” is relative to (Iye et al.’s 80k sample, Tadaki’s 80k, etc.), and recompute the factor accurately (e.g. “3.2×10^6 vs ~80,000 is ~40× larger”).  
  - If 30× refers to something else (e.g. relative to Shamir’s 10^5 sample), clarify that explicitly.

#### P4-M6 — Confusing reuse of “canonical” in multiple contexts  
- **Section/page:** Abstract; Declared Analysis Hierarchy (Sec. III.A, p. 3); Sec. IV.D, p. 4–5; Table III & IV, p. 5; Appendices C–D  
- **Problem:**  
  - “Canonical mask,” “canonical-N MASTER,” “canonical-N direct-MC,” etc. are used to refer to a specific patchy mask and its associated MASTER run. However, the term “canonical” is also used elsewhere (e.g. “canonical-mask diagnostic of the leakage mechanism,” “canonical-MASTER recompute”) without a precise definition on first use.  
  - This risks confusion for readers not following every appendix, and makes it hard to see which mask is the *primary* scientific mask vs. a diagnostic.  
- **Required fix (MAJOR):**  
  - Define “canonical mask” clearly once in Sec. II Data or early in Methods, and use one consistent label (“canonical mask” or “patchy DESI Legacy DR8 mask”) throughout.  
  - Avoid using “canonical” also for the “strict-superset subsample mask”; choose a different adjective for one of them.

#### P4-M7 — Overly long and methods-heavy relative to main scientific result  
- **Section/page:** Whole manuscript (11+ pages)  
- **Problem:**  
  - For a paper whose central claim is “a null dipole at ℓ=1 with −0.122σ (plus a diagnostic mask-systematic channel),” the text devotes many pages to detailed descriptions of internal diagnostics, code paths, and pipeline settings that might be better suited to a companion methods paper or supplemental material.  
  - PRD generally expects that the main text focus on the physical observable, the core estimators, and key systematics; deeply detailed pipeline engineering (e.g. specific PyTorch configs, seed=42, directory names, etc.) can be shortened or moved to appendices.  
- **Required fix (MAJOR):**  
  - Condense the main text to ≤ 8 pages for the claimed contribution. Move much of Appendices B–E (classifier training hyperparameters, extensive dipole diagnostics, leg-proxy regressions) to supplemental material or a separate methods paper. In particular:  
    - Appendix B (training schedule, λ=0.5, etc.) can be summarized in ∼1 paragraph.  
    - Appendix C–E diagnostics can be referenced more briefly, keeping only the most essential tests in the main paper.

#### P4-N4 — “Earlier paper versions” language and internal-code filenames in body  
- **Section/page:** Sec. IV.D, footnote on p. 4; Sec. VII, Appendix A, p. 7  
- **Problem:**  
  - The generative-null footnote references “earlier paper versions,” “scripts/monopole_null_generative.py.” This is internal workflow language and file naming that should not appear in a final PRD manuscript.  
- **Required fix (MINOR):**  
  - Remove references to “earlier paper versions” and internal script paths from the main text and footnotes; replace with a neutral description (“In our implementation, we use the spiral per-pixel counts as trial numbers… The public code reproduces this choice.”).

#### P4-N5 — Strong claims of “falsify the present null” need wording adjustment  
- **Section/page:** Abstract, p. 1 (“A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.”); Conclusions, Sec. VII, p. 7  
- **Problem:**  
  - The phrase “would falsify the present null” is stronger than justified: a future signal could also indicate that the present pipeline underestimates systematics or is not sensitive to the same redshift or galaxy population. PRD typically prefers weaker language (e.g. “would be in tension with” or “would be inconsistent with our null under the same pipeline and assumptions”).  
- **Required fix (MINOR):**  
  - Replace “would falsify the present null” with more careful wording: e.g. “would be inconsistent with our null result under the same pipeline assumptions,” or “would challenge the present null at high significance.”

---

### 4. Checks for unsupported novelty claims

The manuscript makes several novelty/scale claims; I checked the main ones where possible.

#### P4-M8 — “largest galaxy chirality catalog to date” claim needs explicit support  
- **Section/page:** Conclusions, Sec. VII, p. 7 (“We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies…”).  
- **Problem:**  
  - Jia et al. (2023) report ∼1.95M galaxies classified with CE-ResNet.[7] Shamir’s various catalogs are of order 10^5–10^6.[1][3][4] Iye/Tadaki ∼ 10^5.[5][6] On that basis, 8.47M does appear to be the largest *publicly documented* chirality catalog. However, the claim is not explicitly hedged and does not state the comparison set.  
- **Required fix (MINOR):**  
  - Add a qualifier “to our knowledge” and explicitly mention comparison to the CE-ResNet and Shamir catalogs (with their sample sizes), or provide a short sentence citing relevant works to support the claim that no larger chirality-labeled dataset exists in the literature.

---

### 5. Miscellaneous style / minor consistency issues

These are mostly cosmetic but worth addressing.

#### P4-N6 — Mixed use of “3.2 M”, “3,201,160”, “3.2×10^6”  
- **Section/page:** Abstract; Sec. I, II, IV.A; Conclusions  
- **Problem:**  
  - Spiral sample size is reported variously as “3,201,160,” “3.2 M,” and “3.2×10^6.” This is common but can be tightened for CR clarity.  
- **Required fix (NIT):**  
  - Choose one notation in the main text (e.g. always quote exact 3,201,160 on first mention, then “3.2×10^6” elsewhere) and stick to it.

#### P4-N7 — Hyphenation/spacing in dataset URLs and names  
- **Section/page:** Title page; Sec. II.A; Data Availability  
- **Problem:**  
  - “Smith42/galaxies dataset on HuggingFace (https://huggingface.co/datasets/ Smith42/galaxies)” — likely a linebreak artifact between “datasets/” and “Smith42”.  
  - Similarly, “galaxy- chirality- catalog” in the Data Availability URLs shows spaces after hyphens.  
- **Required fix (NIT):**  
  - Clean up all URLs and dataset names so that hyphens/spaces are correctly placed, and ensure they reflect the actual web paths.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper’s core physical result (a null dipole at ℓ=1 with explicit null-procedure mapping) is potentially suitable for PRD and the methods are generally careful, but the manuscript in its current form has multiple issues: mis-structured references to prior Shamir work, imprecise or ambiguous numerical statements for prior results, several places where σ values from disparate nulls are compared without sufficient caveats, a somewhat opaque handling of look-elsewhere corrections and injection-recovery thresholds, and an overlong methods-heavy presentation relative to the modest headline result. These need to be corrected and clarified before the work would meet PRD’s standards for citation accuracy, statistical transparency, and presentation focus.