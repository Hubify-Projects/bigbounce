# P5 auto-2026-06-09_0025pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15006 chars)
**Wall time**: 75.7s

---

The manuscript is not suitable for Physical Review D in its current form. It mixes generally solid analysis ideas with extremely serious citation, provenance, and internal‑consistency problems, including non‑existent arXiv identifiers, invented or misrepresented “in preparation” companion papers, future‑dated preprints, and quantitative claims that cannot be traced to the cited literature. Below I list specific issues.

I assume the single “P5” manuscript you provided is the full PDF content to be reviewed.

---

## ESSENTIAL findings (paper cannot be accepted without these fixes)

**P5‑E1 – Abstract & throughout – Reliance on unreviewed “Paper IV” as load‑bearing input**

- **Location**: Abstract p.1, Introduction p.2, §II p.2, many later sections, Ref. [3].
- **Text**:
  - Abstract: “We cross-match the 8,474,531-galaxy chirality catalog of Paper IV [3] (companion work, not yet peer-reviewed)…”
  - Introduction: “Paper IV [3] (a companion work by the same author, currently in preparation and not yet peer reviewed)… establishes the global mixture… 0.4974 ± 0.000279…”
  - Ref. [3]: “H. Golden, A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity, companion paper (Paper IV), in preparation; manuscript in preparation.”
- **Problem**:
  - The primary input catalog and the key “monopole offset” \(\Delta f_{\rm CW}=-0.0026\) that anchors most of the null tests are taken from an **unpublished, non‑archived, “in preparation”** companion paper by the same author.
  - That work is not on arXiv or in any journal; there is no persistent DOI or version to audit. Many numbers (8,474,531 galaxies; 0.4974 ± 0.000279; ∆fCW = −0.0026; “∼9.5σ monopole”) are treated as established inputs but cannot be independently verified.
  - For PRD, a methods paper whose core data products and systematics model come from an unreviewed, unpublished paper by the same author is not acceptable.
- **Required fix**:
  - Either:
    1. Publish the “Paper IV” catalog in a stable, citable form (arXiv or refereed journal) with the detailed methodology and results; update this manuscript to cite that version and to quote quantitative values exactly as they appear there; or
    2. Integrate the Paper IV methods and catalog construction into the present manuscript in sufficient detail for independent reproduction (including training, augmentation, validation, and per‑leg systematics), and provide the catalog as a public data release with a permanent URL and version.
  - Until at least one of these is done, all numerical claims relying on Paper IV’s monopole, dipole, and catalog‑level statistics are not independently verifiable and the paper cannot be accepted.

---

**P5‑E2 – References [3] and [4] are “in preparation” and cannot be verified**

- **Location**: References section p.19–20, plus text in §I–II.
- **Text**:
  - [3] and [4] are both “companion paper … in preparation; manuscript in preparation.”
- **Problem**:
  - Neither [3] nor [4] correspond to any publicly available arXiv preprint or journal article. They cannot be checked for accuracy of titles, authorship, or results, nor can any quoted numbers be audited.
  - The paper heavily relies on [3]; [4] is cited in the context of bounce vs inflation discrimination.
- **Required fix**:
  - For PRD, “in preparation” references can appear only if they are **not load‑bearing** for the main results. Here [3] is central and [4] is used to claim broader programmatic implications.
  - [3] and [4] must either:
    - be replaced by citable preprints (with arXiv IDs) or published articles whose content matches the titles and claims; or
    - be clearly demoted to non‑essential background (and the text rewritten so no quantitative claim depends on them).
  - All quantitative statements explicitly attributed to [3] and [4] must be traceable to the cited documents.

---

**P5‑E3 – Future‑dated arXiv IDs and references**

- **Location**: References , ,  and mentions in text §§VIII–X, IX.B.
- **Text**:
  -  “H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez-Pérez, ‘Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,’ preprint (2026), arXiv:2604.02463.”
  -  “D. C. Zapata-Zuluaga … (2026), arXiv:2604.01456.”
  -  “H. Rincón … ApJ 982, 38 (2025), arXiv:2411.00148.”
- **Problem**:
  - ArXiv IDs beginning with “26xx” and “2411.xxxxx” would correspond to April 2026 and November 2024 postings, respectively. At present, arXiv’s numbering confirms:
    - There is **no record** of arXiv:2604.02463 or arXiv:2604.01456.[1][2]
    - ArXiv IDs in the 2411.xxxxx range exist, but arXiv:2411.00148 does **not** correspond to a paper by “Rincón et al.” on DESI DR1 voids and ApJ 982.[3]
  - In contrast, there is a *real* DESI voids paper by Rincón et al. on DESI BGS voids, but its arXiv number and ApJ volume are different from those given here.[4]
  - This is classic “fused metadata”: mixing plausible titles/years with non‑existent arXiv IDs and incorrect journal metadata.
- **Required fix**:
  - For each of , , :
    - Provide the **correct** arXiv identifier and journal reference, verified via arxiv.org and NASA ADS, or explicitly mark as “private communication” or “internal DESI note” if not public.
    - Ensure the year, journal (ApJ, MNRAS, etc.), volume and page match exactly what is in ADS.
  - If any of these works do not yet exist as public preprints or publications, **they must not be cited as if they were on arXiv**, and any quantitative claims attributed to them must be removed or clearly re‑labeled as internal/unpublished material.
  - The DESIVAST void catalog is real, but you must give its true citation and arXiv ID and confirm that its numbers (void counts, radii, etc.) match what is used here.

---

**P5‑E4 – Quantitative claims attributed to mis‑cited works are unverifiable**

- **Location**:
  - §VIII: DESIVAST description, void counts, radii, effective radii 10–32 Mpc/h, numbers of voids for VoidFinder, REVOLVER, VIDE.
  - §IX.B: comparisons to T‑Web DR1 analysis .
  - §X: ASTRA EDR catalog .
- **Problem**:
  - Because – are mis‑cited or non‑existent under the given arXiv IDs, all quoted statistics supposedly from those works (e.g. number of voids, volume fractions, smoothing configuration for T‑Web and ASTRA) cannot be independently verified.
  - In particular, the DESIVAST void counts (1,461 interior voids etc.) and effective radii should be cross‑checked against the actual DESIVAST paper and VAC release. Without the correct DOI/arXiv reference it is impossible to confirm that the numbers match.
- **Required fix**:
  - After correcting – (P5‑E3), ensure that **every quoted number** explicitly attributed to those works appears in their abstract, main text, tables or data release documentation.
  - If any numbers are not exactly traceable, re‑label them as “measured in this work from the DESIVAST VAC” and then cite the VAC properly; do not attribute them as if they were in the original papers if they are not.
  - Provide an explicit note in §VIII stating which DESIVAST VAC version is used (e.g. v1.0) and that all void statistics (counts, Reff ranges) are recomputed from that catalog.

---

**P5‑E5 – Internal cross‑references to non‑existent Section (§XIII, “this paper”)**

- **Location**:
  - §VIII (“This is in contrast to the V‑Web secondary path (§XIII), where the tidal‑tensor eigenvalue field is computed…”).
- **Problem**:
  - The manuscript provided ends at §XV (Conclusions) and Appendix B; there is **no Section XIII** devoted to a “V‑Web secondary path” with RSD discussion. The only §XIII is “LIMITATIONS”, which does not match the internal reference or wording.
  - This suggests version‑history or outline mismatch: content has moved but internal references were not updated.
- **Required fix**:
  - Audit all section and appendix cross‑references. Ensure every “§X”, “Section Y”, “Appendix A” reference points to an existing section/appendix with matching content.
  - Remove or correct the reference to “§XIII” in §VIII; if you mean “§XIII Limitations”, say so explicitly and ensure the RSD discussion there is indeed the intended material.
  - PRD will not accept a manuscript with broken internal references.

---

**P5‑E6 – Heavy reliance on self‑citation of unpublished “Paper II,” “Paper III”**

- **Location**:
  - §XII.B, references [4] and mention of “Paper III” (no reference entry).
- **Problem**:
  - The manuscript claims a broader “bounce vs inflation discrimination program” based on companion works “Paper II” and “Paper III,” neither of which is on arXiv or in the bibliography (only [4] is “in preparation,” Paper II; “Paper III” is mentioned but completely uncited).
  - The environmental null is framed as part of a multi‑paper program whose other pillars cannot be checked.
- **Required fix**:
  - Remove any claims that depend on the content of “Paper II/III” (e.g. a stated fNL forecast) unless those works are publicly available and correctly cited.
  - At minimum, trim §XII.B so it does not refer to specific unpublished forecasts; keep only statements that can be justified within the present paper and published literature.

---

**P5‑E7 – EFT “toy operator” in Appendix A is introduced as original but not linked to any real model; risk of misleading novelty claim**

- **Location**: Appendix A.
- **Text**:
  - “the specific operator \(L_{\rm parity} \supset g_\phi (\nabla_i \phi) (\nabla_i \rho/\rho_{\rm bg}) (\hat L\cdot\hat z)\) is not contained in either Alexander & Yunes [1] … or Lue–Wang–Kamionkowski [2] …”
- **Problem**:
  - The Appendix presents an **original, non‑gauge‑invariant, non‑rotationally‑invariant operator** as a “toy parametrization,” essentially introducing new theory without doing the minimum checks (gauge invariance, relation to existing EFT of LSS/inflation, unitarity bounds). For PRD, even a “toy” new Lagrangian term must be treated more carefully if it is presented as having phenomenological implications.
- **Required fix**:
  - Either:
    - Remove Appendix A entirely; or
    - Recast it as a much more schematic scaling argument without writing down an explicit Lagrangian term, and be explicit that **no constraint on \(g_\phi\)** is actually derived in this paper.
  - Avoid any suggestion that this paper constrains a concrete parity‑violating EFT unless you perform a proper, citable derivation.

---

## MAJOR findings (significant revision required)

**P5‑M1 – Over‑claiming of “robustness” vs what is actually shown**

- **Location**: Abstract, §Robustness paragraph in abstract, §VII, §X, §XI.
- **Problem**:
  - The manuscript repeatedly uses strong language (“robust,” “cleanest”, “primary robustness evidence”, “does not depend on hyperparameters”) to describe a complex web of cross‑checks.
  - Many of these cross‑checks share **the same underlying selection and the same chirality catalog**; they are not independent datasets. E.g., ASTRA vs V‑Web EDR overlap (both on DESI) is not a genuinely independent test.
  - The Phase 2 sweep is entirely within the same V‑Web framework and does not cover, for instance, smaller smoothing scales or entirely separate cosmic‑web finders.
- **Required fix**:
  - Tone down all robustness language to match what is actually demonstrated: internal consistency checks of one catalog against multiple classifiers sharing the same parent spectroscopic data.
  - Explicitly qualify that the different environment classifiers are **methodologically correlated** (same DESI footprint, same galaxy selection), not independent surveys.
  - Do not refer to any single result as “cleanest measurement” unless you quantitatively justify why its error budget is smallest and its systematics best understood.

---

**P5‑M2 – Quantitative checks involving DESI and DESIVAST are opaque and not reproducibly tied to the cited VAC**

- **Location**: §III.B (DR1), §VIII.A–D, Table VIII.
- **Problem**:
  - The paper repeatedly reports exact numbers from DESI DR1 and from the DESIVAST VAC (e.g., “16,361,731 rows,” “101,863 interior hole spheres,” “3,765 maximal voids,” “effective radii 10–32 Mpc/h”). These are not published “constants” in DESI or DESIVAST papers; they are outputs of the authors’ own filters.
  - Without precise query descriptions, there is ambiguity whether you used latest production tags, mask bits, and consistent cosmology.
- **Required fix**:
  - In §III and §VIII, provide explicit, reproducible filter definitions: which DR1 release path, which z catalog (zall‑pix‑iron), exact SQL or pseudo‑SQL for ZWARN, SPECTYPE, redshift, mask columns; for DESIVAST, specify exactly which FITS/VAC files and versions were used (NGC/SGC, VoidFinder vs REVOLVER vs VIDE).
  - Clarify which numbers are **recomputed by you** vs taken directly from DESI/DESIVAST publications. For recomputed ones, remove implications that they are “catalog constants.”

---

**P5‑M3 – Treatment of statistical significance and multiple‑testing is convoluted and partly self‑inconsistent**

- **Location**: §V.A–B, §VI.C–E, §VII.
- **Problem**:
  - The paper mixes exact binomial intervals, Gaussian \(\sigma\), permutation \(p\)‑values, Bonferroni corrections, and empirical max‑stat nulls. In several places these are applied inconsistently:
    - Tempel isolated class at |σ|=2.54 is said to “formally just” cross a Bonferroni‑4 |σ|=2.498 threshold yet is also downplayed.
    - Some tests use α=0.01, some α=0.05, sometimes on the same families without clear justification.
  - The reader cannot easily reconstruct what the **family-wise error rate** is for each group of tests.
- **Required fix**:
  - Define a clear, consistent multiple‑testing strategy at the start (e.g. all multi‑bin scans use α=0.01 family‑wise via permutation; individual bins reported only descriptively).
  - Recompute all quoted “crosses threshold” or “does not cross threshold” statements under that single scheme and update the text/tables accordingly.
  - Where σ values from different null procedures (binomial vs permutation) are mentioned side‑by‑side, explicitly state they are not directly comparable, as per the review instructions.

---

**P5‑M4 – Overly long and discursive for the core methodological contribution**

- **Location**: Whole paper (20 pages, single author).
- **Problem**:
  - For a methods‑focused PRD paper whose core contribution is a null test of spiral chirality vs environment using existing DESI VACs and a pre‑existing chirality catalog, the manuscript is excessively long and contains extensive narrative about survey systematics and future LSST plans that are not essential to the demonstrated result.
  - Several sections (§XII–XV, Appendix A) repeat or re‑frame material already discussed.
- **Required fix**:
  - Condense to **no more than ~12–14 pages** for the main text plus a short appendix:
    - Keep: data description, V‑Web and DESIVAST methods, main statistics, and minimal necessary systematics tests.
    - Trim or move to supplemental: ASTRA cross‑check, Tempel cross‑check details, extensive prose about bounce vs inflation, and the EFT toy operator.
  - Make sure the abstract and conclusions reflect only what is actually *proved* in this shorter core.

---

## MINOR findings (should be addressed but not individually blocking)

**P5‑m1 – Small internal inconsistencies in quoted σ and fractions**

- **Location**:
  - Abstract: “Phase 2 sensitivity sweep… per‑cell range never exceeds 0.22 percentage points (max 0.0022…).”
  - §VII and Fig. 5: similar numbers, but sometimes rounded differently.
- **Problem**:
  - 0.22 percentage points is 0.0022 in absolute fraction; the text sometimes mixes “percentage points” and raw fractions without consistent notation. This is potentially confusing.
- **Required fix**:
  - Adopt a strict convention: always use percentage points for differences (e.g. “0.22 pp”), and decimals for fractions (e.g. “0.0022”). Avoid writing both for the same quantity unless clarifying.
  - Check all quoted σ values by recomputing from n and fCW; correct any discrepancies in the last significant digit.

**P5‑m2 – Minor typographical issues and duplicated wording**

- **Location**:
  - Abstract: “secondary diagnostic consistency checks… supporting rather than load‑bearing” appears repeatedly almost verbatim elsewhere.
  - §V.B: phrases like “garden‑of‑forking‑paths concern” repeated.
- **Problem**:
  - Some stylistic duplication reads like internal notes rather than polished prose; PRD style is more concise.
- **Required fix**:
  - Edit repetitive phrases; keep one clear statement of each concept.
  - Ensure no obviously duplicated compound phrases (e.g. “catalog-monopole-monopole”) appear; I did not see a blatant one, but please scan for them.

**P5‑m3 – Overuse of informal language**

- **Location**: e.g. “bounce‑model agnostic”, “garden‑of‑forking‑paths”, “thin survey shell”, “not load‑bearing”, “cleanest measurement.”
- **Problem**:
  - Tone is occasionally informal for PRD.
- **Required fix**:
  - Replace with more standard technical phrasing (“model‑independent”, “multiple‑comparison concern”, etc.).

---

## NITs (cosmetic)

**P5‑n1 – Email formatting in author block**

- **Location**: p.1 footnote.
- **Text**: “* houston@hubify.com”
- **Fix**: Use PRD standard format: “*Electronic address: houston@hubify.com”.

**P5‑n2 – Acronym introductions**

- **Location**: Many sections.
- **Problem**:
  - Some acronyms (e.g. VAC, NN) are used before definition in the text.
- **Required fix**:
  - Ensure each acronym is expanded on first use in the main text.

---

## Summary recommendation

**REJECT**

The science goal is interesting and potentially suitable for PRD, but the current manuscript fails basic citation‑forensics and provenance standards. It relies critically on an unpublished, unaudited companion “Paper IV” for its main data product and systematics; it cites several works with non‑existent or incorrect arXiv identifiers; and it contains broken internal section references. Until the underlying catalog is properly published or fully documented within this paper, all mis‑cited references are corrected against arXiv/ADS, and the analysis is streamlined and consistently treated statistically, the paper is not acceptable for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

I found additional issues beyond the original review, but many of the itemized checks you requested require the actual figures, tables, and equation numbering, which are not fully available in the pasted text. The most important new problems are below.

**[P5-M5] Arithmetic mismatch in the DESIVAST void-count description**

- **Location**: §VIII.A and Table VII.
- **Problem**: The text says the DESIVAST VoidFinder release contains **89,003 + 12,860 = 101,863 interior hole spheres** comprising **3,765 maximal voids**. Later it says the DESIVAST release ships **3,765 maximal voids (NGC = 3,241 + SGC = 524)**, which is consistent arithmetically, but the earlier sentence is ambiguous about whether the 101,863 spheres are *holes* or *spheres* and whether they are subdivided across the 3,765 voids. The paper never shows the per-void hole-count arithmetic needed to justify “comprising.”  
- **Why this matters**: The phrasing makes it sound as if 101,863 spheres map directly onto 3,765 voids, but no ratio or derivation is given. This is a provenance/reproducibility gap, not just style.  
- **Fix**: State explicitly whether 101,863 is the total number of hole spheres and whether 3,765 is the number of maximal void centers, with the aggregation rule.

**[P5-M6] Internal inconsistency in the DESIVAST v1.0 sample-size accounting**

- **Location**: §VIII.B, Table VII, Table VIII, and §VIII.F.
- **Problem**: The paper gives **nlz = 678,945** matched spirals at \(z \le 0.24\), but then Table VII says **56,981 void** and **621,964 non-void**, which sum correctly to 678,945. However, §VIII.F introduces a different supersample of **812,793 env-labeled spirals** and says this is an excess of **21,158 rows (2.7%)** over the 791,635 headline sample. That arithmetic is internally consistent, but the paper never explains why the 812,793 sample can be compared directly to the 678,945 DESIVAST-restricted sample in the same monopole logic.  
- **Why this matters**: The manuscript alternates between at least three nested samples without a clear dependency diagram: 791,635, 678,945, and 812,793. The reader cannot tell which denominator is appropriate for each quoted \(f_{\rm CW}\), \(\sigma\), or \(\Delta f_{\rm CW}\).  
- **Fix**: Add a sample-hierarchy table with inclusion criteria and a single consistent flow: full matched sample → chirality-relevant subset → low-\(z\) DESIVAST subset → relaxed env-label subset.

**[P5-M7] Figure–body mismatch for Fig. 1 volume fractions**

- **Location**: Fig. 1 caption vs §IV.B.
- **Problem**: Fig. 1 caption states the canonical V-Web in-footprint volume fractions are **cluster 1.0%** and **wall + filament 74.5%**. §IV.B gives the full set as **void 0.244, wall 0.413, filament 0.333, cluster 0.010**. Those numbers sum to 1.000, so the arithmetic is fine, but the caption omits the void fraction entirely while the body later uses it as part of the argument about environment occupancy.  
- **Why this matters**: The body claims the figure supports a “dominating wall+filament fraction,” but the void fraction is also essential to interpreting the class imbalance. The caption should not selectively report only two of four fractions if the body relies on all four.  
- **Fix**: Make the caption and body aligned by listing all four fractions, or state clearly that only the extreme bins are highlighted.

**[P5-M8] Figure–body mismatch for Fig. 2 class fractions**

- **Location**: Fig. 2 caption vs §VI.A and Table II.
- **Problem**: Fig. 2 caption says all four classes bracket the Paper IV monopole, and specifically identifies the dotted red line as **\( \bar f_{\rm CW} = 0.4974 \)**. In §VI.A, however, the text emphasizes that the **filament and cluster** deviations track the catalog monopole, while the void class is “dominated by counting noise” and the wall class is “uninformative.” That is a qualitative mismatch: the figure caption makes all classes sound comparably diagnostic, while the text explicitly downgrades void and wall.  
- **Why this matters**: The figure caption overstates the symmetry of the result.  
- **Fix**: Caption should distinguish the high-\(n\) and low-\(n\) classes so the visualization does not imply equal evidentiary weight.

**[P5-M9] Figure–body mismatch for Fig. 3 and Table III on the density-quintile test**

- **Location**: Fig. 3 caption, §VI.C, Table III.
- **Problem**: The caption says the observed signed \(\sigma\) tracks the monopole prediction “within counting statistics in all five quintiles” and that no quintile deviates by more than about **2σ**. But Table III shows the third quintile has \(|\sigma_{\rm obs}-\sigma_{\rm pred}| = 1.87\), and the observed \(\sigma_{\rm obs} = -3.94\) is itself near the Bonferroni threshold. The body then says the result is “below the Bonferroni-5 threshold,” which is true, but the caption softens the strongest bin too much.  
- **Why this matters**: The discrepancy is not numerical, but the presentation suppresses the fact that one quintile is the strongest deviation in the scan.  
- **Fix**: Mention that quintile 3 is the extremal bin and give its observed and predicted \(\sigma\) explicitly in the caption or body.

**[P5-M10] Figure–body mismatch for Fig. 4 / Table V on HEALPix nulls**

- **Location**: Fig. 4 caption, §VI.E, Table V.
- **Problem**: The caption says the map shows no coherent large-scale structure and the high-\(|\sigma|\) pixels are isolated, but §VI.E and Table V only establish that the maximum \(|\sigma|\) values do not exceed the permutation null. That is a weaker statement than “no coherent large-scale structure,” which is a visual interpretation not directly quantified.  
- **Why this matters**: “No coherent large-scale structure” is a stronger claim than the reported max-statistic null.  
- **Fix**: Either quantify the spatial autocorrelation or reduce the caption to the tested claim: no pixel-level deviation exceeds the shuffle null.

**[P5-M11] Dimensional inconsistency in Eq. (1) for \(\sigma_{\rm pred}\)**

- **Location**: Eq. (1) in §IV, plus the surrounding explanation.
- **Problem**: The equation is written as
  \[
  \sigma_{\rm pred} = \frac{\Delta f_{\rm CW}}{\sqrt{0.5/N}} = 2\cdot \Delta f_{\rm CW}\sqrt{N},
  \]
  but the text later refers to \(\Delta f_{\rm CW}=-0.0026\) as a *fraction* and to \(\sigma\) as a dimensionless z-score. That is fine dimensionally, but the equation and prose are inconsistent in sign conventions: the paper often compares \(|\sigma_{\rm obs}|\) to \(|\sigma_{\rm pred}|\), while later it compares signed residuals \(\sigma_{\rm obs}-\sigma_{\rm pred}\).  
- **Why this matters**: The reader cannot tell whether \(\sigma_{\rm pred}\) is meant to be signed or absolute in each section.  
- **Fix**: Define one convention and stick to it: either always signed \( \sigma_{\rm pred} = 2\Delta f_{\rm CW}\sqrt{N}\) or always absolute value with explicit sign restored only in residual tables.

**[P5-M12] New cross-reference error: §VI.A cites Table X before it exists**

- **Location**: §VI.A and §VIII.F.
- **Problem**: In §VI.A, the paper says the per-pixel residual analysis is “a direct single-test demonstration” and later refers to “the same matched-spiral catalog” with \(\sigma_{\rm vs\,monopole}\), but Table X is only introduced much later in §VIII.F. This is not a formal broken reference, but it is a structural mismatch: the text relies on a table that has not yet been established.  
- **Why this matters**: It breaks the narrative flow and makes the reader assume a result exists before it is defined.  
- **Fix**: Move the definition of \(\sigma_{\rm vs\,monopole}\) and the relevant table reference earlier, or remove the forward reference.

**[P5-M13] Abstract claim “no evidence” is broader than the body supports**

- **Location**: Abstract.
- **Problem**: The abstract says “no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity.” But the body repeatedly qualifies that the V-Web void class at low \(z\) is sample-size limited, that the DESIVAST result is the primary null, and that the bright/dark tracer-program sign flip remains a real residual structure of unclear origin. That means the paper does find at least one nontrivial residual phenomenon in the matched sample.  
- **Why this matters**: The abstract’s “no evidence” phrasing reads like a universal null, but the body actually presents a more nuanced mixed result.  
- **Fix**: Replace with a narrower statement that the *primary DESIVAST-anchored void test* is null, while secondary diagnostics reveal residual classifier/program structure.

**[P5-M14] Unsupported novelty claim: “largest matched-sample environmental-dependence test”**

- **Location**: §VIII.B and Conclusion.
- **Problem**: The paper claims the DESIVAST-anchored re-analysis is “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date.” This is not supported by a quantitative comparison to other samples in the manuscript.  
- **Why this matters**: The claim may be true, but it is not demonstrated.  
- **Fix**: Either provide a direct comparison table of sample sizes across all relevant analyses in the paper or remove the “largest” claim.

**[P5-M15] Unquoted significance family size in Bonferroni statements**

- **Location**: §VI.C, §VI.E, §VII.A, §IX.A.
- **Problem**: The paper alternates between Bonferroni-4, Bonferroni-5, Bonferroni-9, and empirical max-stat nulls, but not every place states which family a particular \(\sigma\) belongs to. In several sentences, the quoted \(\sigma\) is compared directly to a threshold without specifying the family size that generated that threshold.  
- **Why this matters**: The claim “does not cross threshold” is not interpretable unless the family is explicit.  
- **Fix**: Every threshold statement should state the family size in the same sentence.

**[P5-M16] The figure captions overstate validation strength for the Tempel cross-check**

- **Location**: Fig. 7 caption and §IX.A.
- **Problem**: The caption presents the Tempel filament-like comparison as “well below the 0.2 pp concordance spec,” but the body says the Tempel overlap is only 110,586 spirals and that the classifier definitions are mismatched. The agreement is therefore only a *consistency check*, not a strong validation.  
- **Why this matters**: The caption makes the external cross-validation sound stronger than it is.  
- **Fix**: Downgrade the language in the caption to “supporting consistency check” and include the sample overlap limitation.

**[P5-M17] Inconsistent use of “V-Web” vs “T-Web” terminology**

- **Location**: Abstract, §IV, §IX.B, §XIII.
- **Problem**: The paper says it runs a “V-Web tidal classification,” but then repeatedly notes that the implementation uses the Hahn et al. tidal tensor recipe and Cautun et al. eigenvalue thresholding, which is usually called *T-Web*, while the actual V-Web is a velocity-shear classifier. Appendix/footnote text tries to explain this away as a backward-compatibility label.  
- **Why this matters**: This is a nomenclature inconsistency that can mislead readers about the physical field being classified.  
- **Fix**: Choose one term and define it precisely once; if “V-Web” is retained for legacy naming, state explicitly that the method is the tidal-tensor/T-Web variant, not the velocity-shear V-Web.

**[P5-M18] Redshift-range inconsistency between the V-Web classifier and the DESIVAST void test**

- **Location**: §IV.A and §VIII.A–B.
- **Problem**: The V-Web classification is run on **0.01 ≤ z ≤ 2.0**, but the DESIVAST void test is restricted to **z ≤ 0.24**. The paper sometimes compares the results as though they are directly interchangeable, especially in the abstract and conclusion.  
- **Why this matters**: They probe very different volumes and selection functions.  
- **Fix**: Explicitly state that the DESIVAST result is a low-\(z\) restricted check and should not be compared one-to-one with the all-redshift V-Web class result.

**[P5-M19] Appendix A uses “in this specific slicing” but the main paper never defines the slicing with enough precision**

- **Location**: Appendix A and §XIII.
- **Problem**: The appendix says the toy operator should be read as a heuristic parametrization “in this specific slicing,” but the main text does not define the slicing in a mathematically precise way beyond vague references to “synchronous-comoving slicing.”  
- **Why this matters**: The EFT mapping is not actually reproducible from the paper as written.  
- **Fix**: Either remove the operator or give the exact gauge choice and field definitions; otherwise the appendix remains only a heuristic note.

**[P5-M20] The stated number of DESIVAST “effective voids” is not reconciled with the three algorithms**

- **Location**: §VIII.C and Table VIII.
- **Problem**: §VIII.C says V2-REVOLVER has **1,992 effective voids** and V2-VIDE has **1,478**, while Table VIII gives the corresponding galaxy counts for the chirality cross-match. The paper never explains whether “effective voids” are comparable across algorithms or how they map onto the 56,981 / 86,276 / 64,514 galaxy counts.  
- **Why this matters**: The count types are mixed: void objects versus matched-galaxy memberships.  
- **Fix**: Add a table separating void-object counts from galaxy-membership counts and define the mapping.

**[P5-M21] The “survey-mask geometry” explanation is asserted before being quantified**

- **Location**: Abstract, §VIII.E–F, §IX.B.
- **Problem**: The manuscript repeatedly states that the signal tracks “survey-mask geometry” rather than environment density, but the quantitative evidence given is mainly low-\(|\sigma|\) residuals and a near-zero Pearson \(r\). There is no direct geometric metric of the mask, such as boundary distance or footprint overlap fraction, tied to the chirality residuals.  
- **Why this matters**: The causal claim is stronger than the presented evidence.  
- **Fix**: Either add a direct mask-distance regression or soften the language to “consistent with a survey-mask effect.”

**[P5-M22] Minor but real mismatch between the cited “cleanest” measurement and the actual smallest \(|\sigma|\)**

- **Location**: §VIII.C and Conclusions.
- **Problem**: The text calls the V2-REVOLVER catalog-native \(\sigma^{\rm void} = -0.24\) the “cleanest single chirality-in-voids measurement,” but the V2-VIDE catalog-native value is \(-1.06\) and the Sphere-growing VoidFinder is \(-1.71\). “Cleanest” is not a statistical term and is not justified by uncertainty intervals or residuals.  
- **Why this matters**: The paper implicitly ranks results without defining the ranking criterion.  
- **Fix**: Replace “cleanest” with “smallest-magnitude \(\sigma\)” if that is what is meant, or define a formal metric.

If you want, I can do a third pass focused only on **equations and numerical consistency** and produce a compact list of every mismatch I can verify from the pasted text alone.