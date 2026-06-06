# P5 auto-2026-06-05_1817pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 65.6s

---

The manuscript is **not suitable for publication in Physical Review D in its current form**. It relies heavily on a non‑peer‑reviewed “Paper IV” for its core input catalog, contains numerous claims of precision that are not independently verifiable, and includes multiple citation and consistency issues that fall below PRD standards.

Below I list specific findings. Page numbers refer to the provided text pages (1–20).

---

## ESSENTIAL issues

### P5-E1 – Reliance on unreviewed Paper IV catalog  
**Location:** Abstract p.1, §I–II p.2–3, throughout; Ref. [3].  
**Problem:** The core data product (8.47M‑galaxy chirality catalog, monopole offset ∆fCW≈−0.0026, global fCW=0.4974±0.000279, dipole constraints, per‑leg systematics) all come from “Paper IV”, explicitly “in preparation and not yet peer reviewed.” The present paper assumes those labels and their quoted uncertainties as established facts and builds its main null result on them. There is no independent cross-check of the chirality labels or monopole within this manuscript.  
**Required fix:**  
- Either (a) ensure Paper IV is accepted in a peer‑reviewed journal and update this manuscript to cite the published version, or (b) move all critical classification and monopole‑estimation methodology into the present paper with full derivations, tests, and uncertainty quantification, so that the chirality catalog’s reliability can be evaluated by PRD referees directly.  
- Clarify explicitly in the abstract and conclusions that the main null result is conditional on the correctness of this external, non‑reviewed classifier.

---

### P5-E2 – Unsupported numeric claims from Paper IV  
**Location:** §I p.2 (“0.4974 ± 0.000279”, “σ = 0.43, p=0.30”, “−0.12σ”), §II p.2, §XI p.17–18 (per‑leg |σ|<3, ∼9.5σ monopole), §VIII F p.12–13.  
**Problem:** Numerous precise statistics attributed to Paper IV (monopole magnitude and significance, dipole amplitude and p‑values, imaging‑leg systematics amplitudes, “∼9.5σ catalog‑level monopole” etc.) are quoted without reproducible definitions or any way to confirm from a public source. Since Paper IV is “in preparation”, these numbers cannot be verified against arXiv or a journal. PRD standards require that critical external inputs be checkable.  
**Required fix:**  
- Either remove all quoted numerical values from Paper IV that materially affect the present inferences, or reproduce the methods and re‑derive them on‑the‑fly in this paper using publicly released data, including sufficient detail that a referee can recompute them.  
- Any remaining reliance on unpublished numbers must be clearly labeled as provisional and must not be used as quantitative anchors for the main science conclusions.

---

### P5-E3 – Citation [3] (Paper IV) bibliographic form  
**Location:** References p.19–20, [3].  
**Problem:** Ref. [3] is given as a kind of title plus “companion paper (Paper IV), in preparation; manuscript in preparation.” This is not standard bibliographic practice and gives no arXiv ID, journal, or year. It is impossible to look up.  
**Required fix:**  
- Provide a standard citation (authors, title, arXiv:ID if posted, or journal details if accepted). If not yet on arXiv or accepted, say “unpublished” and provide a persistent repository (e.g., arXiv). PRD almost never accepts core results that depend on unpublished work; this connects back to P5‑E1.

---

### P5-E4 – Internal consistency and recomputation of key σ values  
**Location:** Abstract p.1, Table II p.5, Table VII–VIII p.11–12, Table X p.13, Table XII p.16.  
**Problem:** Many quoted “σfrom half” values and ranges are claimed to be consistent with catalogue‑wide monopole predictions, yet there is no explicit error propagation or clear distinction between σ from half‑parity vs. σvs monopole. At several points, differences between predicted σ and observed σ are described as “within order unity” or “within ∼1σ” without a defined metric. For PRD, statistical claims must be precisely defined and reproducible.  
**Required fix:**  
- For every load‑bearing σ in the abstract and headline tables (e.g., −2.61, −4.66, −0.68, +0.55, −1.71, etc.), explicitly define which null is used (parity 0.5 or monopole f̄ from Paper IV), and show the formula and input N used.  
- Provide a compact table (or clear pointer to existing tables) where each quoted σ and |∆fCW| in the abstract can be directly recomputed from nCW and N shown in the paper.  
- Remove imprecise language such as “within order-unity” and replace by quantitative statements (“difference 0.7σ under this null”).

---

### P5-E5 – Claims of “first” / “largest” / “strongest” without literature support  
**Location:** Abstract p.1 (“largest controlled sample”, “strongest single residual structure in the paper”), §VIII B p.11 (“largest matched-sample environmental-dependence test … to date”), §XII C p.17 (comparison to Shamir), various.  
**Problem:** Assertions of being “largest” or “strongest” in the literature or in DESI are made without a systematic survey or comparison, and some phrases are ambiguous (e.g., “largest … in this paper” mingled with “to date”). PRD requires novelty claims be clearly supported or constrained to the paper’s own scope.  
**Required fix:**  
- Restrict claims to clearly supported scope, e.g. “largest in this analysis” or “largest in this DESI DR1‑based sample we construct.”  
- Remove any implication that this is the largest or first environment‑dependent chirality test globally, unless a literature survey is added and supports that claim.

---

### P5-E6 – Ambiguous statistical comparability of σ across different nulls  
**Location:** Abstract p.1–2 (“none reach 3σ after look-elsewhere correction”), §V A–B p.4–5, §VI–VII p.5–9.  
**Problem:** The paper juxtaposes σfrom half, σpred from monopole, and |σvs monopole|, often in close proximity, without always explicitly warning that they are different statistics. The instructions require an explicit “not directly comparable” qualification wherever σ from different nulls are shown side‑by‑side.  
**Required fix:**  
- In every place where σfrom half and σvs monopole are both discussed for the same bin or set of bins (notably Table II, Table III, the Phase 2 discussion, and §VIII F), add explicit language that these σ values are defined under different nulls and are not directly comparable; only differences under a fixed null have standard significance interpretation.  
- Consider standardizing to one main null (parity‑0.5) and treating monopole subtraction as a shift in the mean, to simplify the interpretation.

---

### P5-E7 – Ambiguity and partial circularity in “primary/secondary” analysis designation  
**Location:** §V B p.4–5, §VIII p.10–13, §IX–X p.13–17.  
**Problem:** The paper labels the DESIVAST‑based void analysis as “primary” post hoc, but then leans heavily on V‑Web and other diagnostics for interpretation (e.g., survey‑edge systematics, BGS/dark‑sample decomposition). There is no formal preregistration, and the “garden of forking paths” is acknowledged but not fully controlled. From a PRD methodology standard, the statistical treatment is too ad‑hoc for the claimed precision.  
**Required fix:**  
- Clarify which one or two statistics are the formal “tests” of environment‑dependent chirality (e.g., DESIVAST VoidFinder void vs non‑void ∆fCW, maybe with three‑algorithm average), and specify them in advance as the only load‑bearing tests.  
- Treat all V‑Web, Tempel, ASTRA, density/redshift/HEALPix stratifications as clearly exploratory; this means not using them to qualify or reinterpret the nulls without a defined multiple‑testing framework.  
- Either add a rigorous multiple‑testing control (e.g., clearly defined family‑wise procedures for all scans) or tone down interpretive claims based on secondary paths.

---

### P5-E8 – EFT “toy operator” goes beyond cited literature  
**Location:** Appendix A p.19, Ref. [1]–[2].  
**Problem:** The text acknowledges that the specific operator \(L_\text{parity}\supset g_\phi (\nabla_i\phi)(\nabla_i \rho/\rho_{bg})(\hat L\cdot\hat z)\) is not actually present in refs [1] or [2], but only “inspired by” them. In a PRD methods paper, introducing a novel operator should involve at least basic consistency checks (symmetries, dimensional analysis, typical magnitude) and ideally be justified from an underlying action. Here it is essentially freehand.  
**Required fix:**  
- Either move Appendix A to a short, clearly speculative paragraph in the discussion or delete it.  
- If retained, (i) make it explicit that this is a purely schematic parametrization, (ii) define the mass dimension and expected scale of \(g_\phi\), and (iii) provide at least a dimensional estimate consistent with standard EFT conventions. The present “bound” is too vague to be meaningful.

---

### P5-E9 – Reproducibility and code/data availability not adequate at PRD standard  
**Location:** Appendix B p.19, scattered references to a “companion data repository”.  
**Problem:** The paper refers repeatedly to “companion data repository” but gives no DOI or stable identifier, only vague references. PRD strongly prefers that key code and data be hosted in stable archives with DOIs (Zenodo, institutional repositories, etc.).  
**Required fix:**  
- Provide a specific repository URL (not just a general phrase), with a version tag/DOI that contains: (a) the matched catalogue(s) used for analysis (or reproducible scripts to generate them from public DESI + chirality catalog), (b) the V‑Web classification outputs, (c) the DESIVAST membership cross‑matches, and (d) scripts to recompute all main tables and figures.  
- Ensure the repository is public at submission time so refs can be checked.

---

## MAJOR issues

### P5-M1 – Paper II (Ref. [4]) and other companions unverified  
**Location:** Ref. [4], §XII B p.17.  
**Problem:** Paper II is again “in preparation; manuscript in preparation” with no arXiv ID. It is mentioned as part of a “bounce vs inflation” discrimination program. While not central to the environment result, this interlocks with the scientific motivation.  
**Required fix:**  
- As with Paper IV, either provide an arXiv ID or remove specific dependence on the result. Motivation can cite unpublished ideas but should not rely on them quantitatively.

---

### P5-M2 – Reference  and  status and metadata  
**Location:** Refs  and , §IX B–§X p.14–16.  
**Problem:**  
- : “preprint (2026)” with arXiv:2604.02463 – this looks like a correctly formed arXiv ID and title “Cosmic-web quenching with DESI DR1: T-Web environments…”, consistent with the text.  
- : “(2026), arXiv:2604.01456” – again appears syntactically valid.  
However, the paper uses these as “concurrent DESI DR1 cosmic‑web” references but then mixes their results with its own in a way that may be confusing. It is not always clear which numbers or qualitative statements (e.g., void fraction discrepancies) are directly from / vs inferred here.  
**Required fix:**  
- For each quantitative statement that comes from  or  (e.g. T‑Web volume fractions, ASTRA footprint size and fraction ranges), cite explicitly at the sentence where it is used and distinguish clearly from your own recomputations.  
- Check that the stated fractions and descriptions match the latest versions of those preprints; if those preprints change, update accordingly.

---

### P5-M3 – Non‑standard notation and naming (“P5”, “Paper IV”, “Paper II”)  
**Location:** Title page, abstract (Paper IV), §II, §VIII F, §XIII, Conclusions.  
**Problem:** Internal paper numbering (P5, Paper IV, Paper II, etc.) is used extensively in the prose (“primary P5 environment‑independence claim,” “Paper II,” “Paper III not yet published”). This reads like a multi‑paper project document, not a self‑contained PRD article, and makes it harder to read in isolation.  
**Required fix:**  
- Remove all internal project tags (P5, “Paper II”, “Paper III”, “Paper IV”) from the main text except maybe a brief remark in the introduction. Refer to specific works by author and year (e.g. “Golden 2026a”, “Golden 2026b”) and give standard citations.  
- Ensure the paper is intelligible as a stand‑alone article.

---

### P5-M4 – Overly long and repetitive presentation for the actual result  
**Location:** Entire manuscript (20 pages main text, repeated expansions of the same null).  
**Problem:** For a single key result (no detectable environment dependence at current sensitivity), the paper is very long and includes many expansions of essentially the same point (V‑Web null, DESIVAST null, multiple null tests). The length is not in itself fatal but makes it difficult to identify the core method and result and obscures where the real statistical power lies.  
**Required fix:**  
- Streamline by moving some of the diagnostic cross‑checks (e.g. detailed density quartiles, some HEALPix variants, ASTRA overlap, repeated rephrasings of the same null) to an Appendix or companion note.  
- Keep the main text to ≲15 pages by focusing on: data, V‑Web method, DESIVAST void analysis, and the key robustness checks, clearly separating secondary explorations.

Recommended maximum main‑text page count: **15 pages**.

---

### P5-M5 – RSD discussion: partially quantitative, partially hand‑waving  
**Location:** §VIII (RSD treatment) p.10, §XIII p.18.  
**Problem:** The paper mixes a qualitative statement (“essentially RSD‑immune”) with a rough σv/(aH) estimate and acknowledges that proper reconstruction is needed. This is too informal for PRD for a potential systematic that could in principle shift galaxies across environment boundaries.  
**Required fix:**  
- Either (a) perform a simple quantitative mock test demonstrating that likely RSD displacements at DESI BGS redshifts do not shift a significant fraction of galaxies across the void/non‑void boundaries used in the DESIVAST analysis, or (b) explicitly downgrade the RSD discussion to a limitation, making clear that the result is conditional on uncorrected redshift‑space positioning and that future work should include reconstruction.  
- Clarify that this is not treated as a controlled systematic in the present analysis.

---

## MINOR issues

### P5-m1 – Slight mismatch with DESI BGS depths  
**Location:** §XI p.17 (“flux-limited at r ≤ 17.8 in the DESI Legacy regime”).  
**Problem:** The established DESI BGS main limit is r < 19.5 for BGS BRIGHT, per actual DESI BGS target selection papers.[4][6] The catalog here may use r ≤ 17.8 for classification quality, but this is not clearly defined and could be misread as the DESI BGS limit.  
**Required fix:**  
- Clarify that 17.8 refers to the chirality catalog’s training/selection limit (if so) and distinguish from DESI BGS targeting limits. Cite the DESI BGS target selection paper properly for the survey limit.

---

### P5-m2 – Tempel  metadata  
**Location:** Ref. .  
**Problem:** The citation appears accurate: “Astron. Astrophys. 566, A1 (2014), arXiv:1402.1350.” That matches NASA ADS and arXiv metadata. No correction needed, but note that you refer to it as “FoF group classifier” in the text and “Flux- and volume-limited groups/clusters…” in the reference – consistent but perhaps worth one clarifying clause when introduced.  
**Required fix:**  
- When first mentioning Tempel et al. 2014, explicitly note it is an FoF group catalog based on SDSS DR10, to connect the method name to the reference.

---

### P5-m3 – DESIVAST  citation  
**Location:** Ref. .  
**Problem:** The reference metadata (“ApJ 982, 38 (2025), doi:10.3847/1538‑4357/adb559, arXiv:2411.00148”) matches published information about DESI void catalogs. The description in the text is consistent.  
**Required fix:**  
- None on metadata. Maybe add the phrase “DESI value‑added catalog DESIVAST” at first use, to make clear it is a VAC.

---

### P5-m4 – Small numerical typos or sloppy rounding  
Examples:  
- Abstract p.1: “range across classes is 1.98 percentage points” – from 0.4836 to 0.5034, difference 0.0198 = 1.98 pp, correct; but void is later rounded to 0.484 in conclusions.  
- §VIII E Table IX: 0.4961 with σ=−4.75; for N=378,511, this corresponds to ∆f≈−0.0039; √(0.25/N)≈0.00081; ∆f/σ≈−4.8 – consistent within rounding.  
No clear numerical inconsistencies stood out on recomputation, but the text often jumps between two decimal and four decimal precision without a consistent rule.  
**Required fix:**  
- Adopt a uniform precision rule for fCW (e.g., 4 decimals) and σ (two decimals) in all headline tables. This improves clarity and makes auditing easier.

---

### P5-m5 – Slightly informal language  
**Location:** Scattered (“garden-of-forking-paths,” “not load‑bearing but supporting,” “this is the strongest sign,” “near‑perfect null”).  
**Problem:** Wording is informal for PRD style.  
**Required fix:**  
- Replace with more formal phrasing: “multiple testing concern,” “diagnostic but not central,” “largest residual structure,” “statistically consistent with zero within 1σ.”

---

### P5-m6 – Repeated mention of “companion data repository” without identifier  
**Location:** §V, §VI D, §VIII A, §IX A, §X, Appendix B.  
**Problem:** Repetitive and vague.  
**Required fix:**  
- Mention it once in Methods with a precise identifier; in later sections just refer back to that location.

---

## NITPICKS

### P5-n1 – Formatting of units  
**Location:** §IV A p.3–4 (25 Mpc/h, 256³), figures.  
**Problem:** Some units like “2563” instead of “256^3”; “25 Mpc/h” is fine but occasionally “Mpc/h×{0.0,0.1,0.3}” without spacing.  
**Required fix:**  
- Standardize as \(256^3\) and “Mpc h\(^{-1}\)” in math mode.

---

### P5-n2 – Occasional duplicated wording  
**Location:** e.g., Abstract: “supporting rather than load‑bearing: the primary robustness evidence is the on-DESI DESIVAST cross-classifier and Phase 2 V-Web sensitivity analyses” (slightly redundant).  
**Required fix:**  
- Minor tightening for readability; no scientific change needed.

---

## Summary recommendation

**RECOMMENDATION: MAJOR REVISIONS**

The core scientific idea – testing spiral chirality vs environment using DESI DR1 and DESIVAST – is interesting and potentially useful. However, the analysis presently depends critically on an unpublished, unverified chirality catalog “Paper IV”, mixes several different σ‑based nulls without consistently clarifying comparability, and is framed with project‑internal labels and exploratory analyses that do not yet meet PRD’s standards for methodological clarity and independence. The paper requires substantial revision to (i) either internalize or properly publish and document the classification catalog, (ii) cleanly define and present the main statistical tests with rigorous error control, and (iii) streamline and formalize the presentation before it can be considered for PRD.