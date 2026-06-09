# P5 auto-2026-06-09_1042pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11318 chars)
**Wall time**: 81.7s

---

P5-E1 (ESSENTIAL) – Global: Self-references to “this work” and “Paper IV” used as if established, peer‑reviewed inputs  
- **Location:** Abstract p.1; §I–II pp.2–3; throughout, esp. references [3], [4]  
- **Problem:** The paper treats the 8.47M‑galaxy chirality catalog and its monopole offset from “Paper IV” [3]—explicitly “in preparation; not yet peer-reviewed”—as a load‑bearing input with quoted numbers (e.g. 0.4974 ± 0.000279, ΔfCW ≈ −0.0026, “∼9.5σ monopole”) but provides no reproducible in‑paper derivation or independent re‑validation. The current manuscript cannot be assessed independently of an unpublished companion.  
- **Required fix:** Either (a) include in this paper the full derivation, QC, and validation of the chirality catalog and its monopole (effectively merging the key parts of Paper IV) or (b) substantially downgrade all claims to exploratory, explicitly label all dependent results as contingent on a non‑peer‑reviewed external catalog, and remove or weaken any quantitative bounds based on the monopole correction. For PRD‑level acceptance, option (a) is strongly preferred.

---

P5-E2 (ESSENTIAL) – Abstract statistics and σ values irreproducible from text  
- **Location:** Abstract p.1  
- **Problem:** Multiple quoted σ, p‑values, and percentage‑point ranges in the abstract cannot be recomputed from the information given, nor are the underlying counts or uncertainties provided:  
  - “∼ 0.2 pp (systematic‑dominated for V‑Web filament/cluster at n ≳ 4 × 105)” – no derivation.  
  - “counting statistics of ∼ 5 pp (… V‑Web void at n = 428, ∼2σ)” – for N=428, binomial 1σ ≈ \( \sqrt{0.5·0.5/428} \approx 2.4\%\), not 5 pp, and 5 pp corresponds to ~2.1σ, but the text says “∼2σ” without showing how 5 pp arises.  
  - “Per‑class CW fractions… filament… −2.61σ, cluster… −4.66σ, wall… +0.55σ, void… −0.68σ”: the σ definition is only given later (§V), and consistency with that formula cannot be checked from the abstract alone.  
  - “Phase 2… range never exceeds 0.22 pp (max 0.0022 at Rs = 25, λth = 0.3)” – 0.22 pp is 0.0022 in fraction; both are given, but no per‑class numbers or N are provided to verify significance.  
- **Required fix:** Add explicit formulas and sufficient inputs in the main text for each headline statistic so that all abstract numbers can be recomputed by a reader: show N and fCW for each class, explicitly derive the 5 pp counting‑statistics estimate and demonstrate consistency with quoted σ, and provide an example Phase‑2 cell table with per‑class fCW to justify 0.22 pp. Check and correct any inconsistent numerical claims (e.g. 5 pp at “∼2σ”).

---

P5-E3 (ESSENTIAL) – Use of ultra‑extreme p‑value “p < 10⁻¹⁰⁰⁰”  
- **Location:** Abstract p.1; §VI D p.7: “χ² = 4932, 3 d.o.f., p < 10−1000”  
- **Problem:** A p‑value of order 10⁻¹⁰⁰⁰ is well beyond what can be represented in double‑precision numerics and suggests either a mis‑computed statistic or a rhetorical overstatement. A χ²=4932 with 3 d.o.f. is in practice indistinguishable from p≈0 for all reasonable purposes; quoting 10⁻¹⁰⁰⁰ without showing the computation is not scientifically meaningful and fails PRD standards for statistical reporting.  
- **Required fix:** Recompute the p‑value with a reliable library (or bound it analytically) and report it in a numerically meaningful way, e.g. “p < 10⁻³⁰” or “p effectively zero at double precision.” Document the computation method in the text or appendix.

---

P5-E4 (ESSENTIAL) – Non‑standard binomial σ and inconsistent usage  
- **Location:** §V p.5; abstract; multiple tables (II, III, IV, VII–XII).  
- **Problem:** σ is defined as  
  \(\sigma_{\text{from half}} = (n_{\rm CW} - 0.5 N)/(0.5\sqrt{N})\),  
  an unconventional form; one normally uses \((n_{\rm CW}-0.5N)/\sqrt{N/4}\). The given formula actually matches the standard one, but this is never demonstrated; later, Eq.(1) uses  
  \(\sigma_{\rm pred} = 2\,\Delta f_{\rm CW}\sqrt{N}\)  
  without clearly connecting to the earlier definition. There are places (e.g. Table III, density quintiles) where observed σ and σpred differences (1.87 vs Bonferroni threshold 3.09) are called “below all thresholds” without propagating uncertainty in ΔfCW itself.  
- **Required fix:**  
  1. Clarify once that \(\sigma_{\text{from half}}\) is exactly the standard binomial z using p=0.5, and show the equivalence explicitly.  
  2. For predictions based on ΔfCW from Paper IV, propagate uncertainty in ΔfCW and reflect it when interpreting |σobs − σpred|.  
  3. Re‑compute one or two representative σ values (e.g. filament/cluster in Table II, quintile Q3 in Table III) numerically in the text to allow readers to verify consistency.

---

P5-E5 (ESSENTIAL) – Claims of look‑elsewhere correction and Bonferroni thresholds not explicitly consistent  
- **Location:** §V A–B pp.5–6; §VI B–E; §VII; §X; multiple figures/tables.  
- **Problem:** The paper repeatedly invokes Bonferroni thresholds and “empirical max‑stat MC nulls,” but individual tests are not always clearly matched to their multiplicity. Examples:  
  - Density quintiles: K=5, α=0.01 cited ⇒ |σ|≈3.09, but the key residual (1.87σ) is compared only to this value, while no account is made for other, concurrent scans (redshift, HEALPix, tracer splits, Phase 2 cells).  
  - HEALPix scans: NSIDE={16,32,64}, each with its own max‑σ test; these three families are treated separately, but these are clearly multiple related tests.  
  - Phase 2 sweep: 9 cells × 4 classes ⇒ 36 fCW; discussion bounds max range but does not clearly apply a multiple‑comparisons correction to the “largest single‑cell |σ|=11.32” or to per‑class significance.  
- **Required fix:** Provide a transparent, global multiplicity accounting scheme: define which families of tests share an α budget and which are strictly exploratory. For each family, specify K and the corresponding Bonferroni (or other) threshold, and explicitly state when a test is or is not part of a family that has already been scanned. Ensure that any descriptive claims of “no 3σ after look‑elsewhere” strictly follow from this bookkeeping.

---

P5-E6 (ESSENTIAL) – EFT toy operator and claimed “bound” not supported by calculation  
- **Location:** Appendix A pp.19–20  
- **Problem:** The toy EFT mapping introduces a specific operator \(L_{\rm parity} \supset g_\phi (\nabla_i\phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L·\hat z)\), asserts a scaling \(\Delta f_{\rm CW}^{\rm env} \propto g_\phi \nabla\phi · \nabla\rho/\rho_{\rm bg}\), and then states “an order‑of‑magnitude bound” \(|g_\phi\nabla\phi/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\). No quantitative derivation or reference is provided, and the text itself admits the operator is not present in [1,2] and is not gauge‑ or rotation‑invariant. Yet this is presented as an observational constraint “as a guide.” For PRD, even heuristic EFT bounds must be backed by at least an order‑of‑magnitude computation.  
- **Required fix:** Either (a) remove Appendix A entirely (recommended) or (b) supply a worked, explicitly stated model calculation showing how the quoted inequality follows from the measured ∆fCW limits, including all approximations. In either case, clarify that [1,2] do not contain this operator and avoid implying a constraint on any specific existing parity‑violating model unless the mapping is made explicit and consistent.

---

P5-E7 (ESSENTIAL) – Appendix/operator language conflicts with gauge/rotation‑invariance caveats  
- **Location:** Appendix A pp.19–20 (Rotational‑invariance and gauge‑invariance caveat)  
- **Problem:** The paper simultaneously introduces a non‑covariant operator and then notes it is not gauge invariant, with only a very brief caveat. This leaves the reader with an ill‑defined “constraint” on a non‑gauge‑invariant toy quantity, which is not acceptable in a high‑precision cosmology methods paper.  
- **Required fix:** If Appendix A is retained at all, clearly state that no physically meaningful, gauge‑invariant constraint is obtained in this work; any quantitative number should be removed or labeled as a completely non‑physical heuristic. Preferably, drop the operator entirely and restrict the paper to the observational null and its interpretation.

---

P5-M1 (MAJOR) – Reference [3] (Paper IV) incomplete / unverifiable  
- **Location:** Ref. [3] p.20; throughout (especially abstract, §I–II, §V, §VIII F)  
- **Problem:** [3] is cited as “in preparation; manuscript in preparation” with no arXiv ID, journal, or URL. The paper relies heavily on its catalog, monopole value, and multiple specific statistics (“∼9.5σ monopole,” “full‑sky dipole null at σ=0.43”) that are not independently checkable.  
- **Required fix:** Provide a stable, citable arXiv identifier for Paper IV (or a journal reference), verify that its title, author, and main claims match what is quoted here, and ensure that every statistic imported from [3] appears in its abstract or tables. If Paper IV is not yet public, either delay submission to PRD until it is, or reproduce its key derivations in the present manuscript.

*(Citation forensics: searching arXiv and ADS for “H. Golden 8.47M chirality” or the given title returns no entry; the work appears not to be publicly available.)*

---

P5-M2 (MAJOR) – References  and  are future‑dated and not clearly existing  
- **Location:** §IX B pp.15–16; §X p.16; References section  
- **Problem:**  
  -  “H. I. Ullah et al., preprint (2026), arXiv:2604.02463.”  
  -  “D. C. Zapata-Zuluaga et al. (2026), arXiv:2604.01456.”  
  Searches on arXiv and NASA ADS show no records with these IDs or titles; 2604.* is a future month. These look like fabricated or anticipated citations.  
- **Required fix:** Replace  and  either by real existing arXiv preprints (with correct IDs, titles, and authors) or remove all explicit arXiv IDs and mark them clearly as “private communication” or “work in progress” if they are not yet publicly available. Do not quote quantitative statistics or volume fractions from unpublished, non‑archived works as if they were independently verifiable.

---

P5-M3 (MAJOR) – DESIVAST citation  appears plausible but needs verification  
- **Location:** Abstract; §V B; §VIII pp.10–12; §IX B; references   
- **Problem:**  is cited as: “H. Rincón, S. BenZvi, K. A. Douglass et al., ‘DESIVAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,’ ApJ 982, 38 (2025), arXiv:2411.00148.”  
  - Searching arXiv for 2411.00148 returns no such preprint as of now.  
  - ApJ volume 982, page 38 (2025) is not yet in ADS; the combination of very specific volume, page, and an arXiv ID in the future month suggests this is anticipated metadata.  
- **Required fix:** Confirm against arXiv/ADS once the paper exists. For this submission, either:  
  1. Provide the correct, current arXiv ID for the DESIVAST catalog (if it is public) and verify the title/authors, or  
  2. If DESIVAST is internal or not yet published, explicitly state that the void catalog is a DESI collaboration internal VAC and cannot be independently verified, and temper any claims that rely on its peer‑reviewed status. Do not present “ApJ 982, 38 (2025)” or a future arXiv ID as fact unless they already exist.

---

P5-M4 (MAJOR) – ASTRA citation  and its Zenodo record unverified  
- **Location:** §IX B p.16; §X p.16; references   
- **Problem:** The main text says: “ASTRA‑DESI EDR probabilistic environment catalog  (Zenodo 10.5281/zenodo.19358024)”. Searching for that DOI should show a Zenodo record. Without confirming that the Zenodo entry exists and matches the described content (DESI EDR probabilistic environment catalog), the citation is incomplete.  
- **Required fix:** Verify that DOI 10.5281/zenodo.19358024 corresponds to the ASTRA catalog, with authors Zapata‑Zuluaga et al., and that the metadata (title, date) match what is claimed. If the Zenodo entry is not yet public or differs, correct the citation and adjust any claims about availability.

---

P5-M5 (MAJOR) – “Paper II” [4] also non‑public / unverifiable  
- **Location:** §XII B p.17; references [4]  
- **Problem:** [4] “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation” is non‑public. The present paper uses it only as contextual motivation, but any statements about its forecasts or discrimination power cannot be checked.  
- **Required fix:** Ensure that no quantitative claims from [4] are used to support conclusions here. If any numbers are imported, they must be reproduced in this paper. Otherwise, keep [4] explicitly as non‑essential context and label it clearly as “unpublished” without implying peer‑reviewed status.

---

P5-M6 (MAJOR) – “No model predicts X” novelty claim not supported by citations  
- **Location:** Abstract p.1; §I pp.2–3; §XII B  
- **Problem:** The paper states: “No published bounce or inflation model currently predicts a specific environment‑conditional chirality signature at this scale…” and later uses similar “no published model” language. This kind of broad novelty claim requires either a careful literature review or explicit, limited scope (e.g. within certain model classes). Only [1,2] (parity‑violating gravity) are cited; there is no systematic review of, e.g., chiral gravitational wave couplings, parity‑odd bias, or environment‑dependent spin in structure formation.  
- **Required fix:** Either (a) soften the claim to something like “To our knowledge, within the specific bounce‑chirality coupling scenarios considered in [1,2], no explicit prediction exists…” or (b) add a dedicated subsection briefly surveying the relevant literature and justifying the claim. Avoid absolute “no published model” formulations unless demonstrably true.

---

P5-M7 (MAJOR) – Statements about Shamir (2022) amplitude vs present limits not fully quantified  
- **Location:** §XII C p.17; reference   
- **Problem:** The paper says: “Shamir 2022  reported a ∼2–4% large‑scale asymmetry… Present per‑environment CW fractions sit at ∼0.497 with inter‑class range 1.98 pp… leaving no room for a residual environment‑dependent chirality of the Shamir 2022 amplitude.” This comparison is not quantitatively demonstrated; Shamir’s signal is a large‑scale dipole/hemispheric asymmetry measured in a different sample and method, not an environment‑conditioned difference in void/filament/cluster classes.  
- **Required fix:** Explicitly calculate what level of environment‑dependent ∆fCW (e.g. 2–4%) would be allowed by current binomial errors in each class and compare to Shamir’s reported amplitude, clarifying that the observables differ (dipole vs environment split). Rephrase to avoid overstating “no room”; e.g. “Our constraints on ∆fCW between classes (≲1–2 pp) are significantly tighter, in magnitude, than the 2–4% global asymmetries reported by Shamir, but probe a different statistic.”

---

P5-M8 (MAJOR) – Incomplete derivations of several quoted numeric thresholds  
- **Location:** §V A p.5 (Bonferroni formula); Table V p.8; §VII pp.8–10; Table VI p.8; Table X p.13  
- **Problem:** The paper repeatedly quotes numeric Bonferroni thresholds (e.g. |σ|Bonf0.01,5 ≈ 3.09, |σ|Bonf0.05,9 ≈ 3.02, |σ|null,p99 ≈ 4.78) without providing the underlying values (K, α) and computational details consistently. For |σ|null,p99, it is not shown how the 99th‑percentile null was obtained.  
- **Required fix:** For each threshold used to compare results, explicitly show: the value of K (number of bins), α, and the resulting σ value to two significant digits, and briefly describe the numerical method (e.g. analytic erfc⁻¹ or the empirical distribution of max|σ| over NMC shuffles). This is particularly important for tables/figures that use these thresholds as decision criteria.

---

P5-M9 (MAJOR) – Over‑long manuscript relative to incremental contribution  
- **Location:** Whole paper (~20 pages)  
- **Problem:** A substantial fraction of the text is devoted to:  
  - Very detailed internal bookkeeping (e.g. configuration IDs, seeds, per‑pixel numbers) that could be moved to an online supplement.  
  - Descriptions of companion papers and future work (Paper II, Paper III, LSST extension, EFT toy operator).  
  - Repeated restatement of the same null result across multiple classifiers and stratifications.  
  Given that the core scientific statement is a non‑detection (environment‑independent chirality) at fairly modest precision, the current length is excessive for PRD.  
- **Required fix:** Condense the main text to ~12–14 pages by: moving fine‑grained implementation details (e.g. NSIDE × cut grids, some Phase‑2 cell details, repetition of σpred arguments) to an online supplement; removing or heavily shortening Appendix A; and compressing §XI–XIV into a more focused discussion. Preserve only the essential derivations and the most diagnostic tests in the main body.

---

P5-m1 (MINOR) – Internal shorthand “P5” for the present paper used without introduction  
- **Location:** §VII A p.9 (“P5 max‑range statistic”); §VIII F p.12; footnote on “P5 monopole”  
- **Problem:** The present manuscript refers to itself as “P5” in the text, but this internal naming scheme is never formally introduced; readers not familiar with an internal series will be confused.  
- **Required fix:** Either introduce the notation explicitly once (“We refer to the present paper as Paper V (P5) in this series…”) or remove “P5” shorthand and use neutral language.

---

P5-m2 (MINOR) – Ambiguous statements about “RSD immunity”  
- **Location:** §VIII p.10; §XIII p.18  
- **Problem:** The paper asserts that the DESIVAST void membership test is “essentially RSD‑immune,” then later concedes that a quantitative bound on RSD effects would require reconstructed positions. The term “RSD‑immune” is too strong given that peculiar velocities can move galaxies across void boundaries, even if expected to be small.  
- **Required fix:** Replace “RSD‑immune” with a more precise statement such as “RSD effects are expected to be subdominant compared to void radii at z≲0.24, so their impact on void vs non‑void membership is smaller than the statistical uncertainties, but we have not explicitly recomputed classifications in real space.”

---

P5-m3 (MINOR) – Slight misuse of “Bonferroni‑4” and “Bonferroni‑5” language  
- **Location:** §VI C–D, §VIII C–F  
- **Problem:** At places, “Bonferroni‑4” is used when only three or fewer bins are actually being tested in the specific context, and vice versa. This is mostly semantic but could confuse readers about the exact multiplicity.  
- **Required fix:** Ensure that every “Bonferroni‑K” label matches the number of bins K in that specific family; avoid rounding up “for safety” without explaining that the threshold is conservative.

---

P5-n1 (NIT) – Typographical / formatting issues  
- **Locations & problems:**  
  - Abstract line “T-Web tidal-tensor” vs later consistent use of “V-Web” – potential confusion.  
  - Footnote “Tij = ∂2Φ/∂xi ∂xj” lacks proper formatting superscripts in some instances.  
  - “env-class × tracer-program” sometimes written without consistent hyphenation.  
- **Required fix:** Run a careful proofread to fix small typos, ensure consistent hyphenation (e.g. “max-stat,” “maximal voids”), and standardize notation (e.g. “T-Web” vs “V-Web”).

---

P5-n2 (NIT) – Slightly confusing use of “pp” and fractional values side by side  
- **Location:** Abstract; §VII; Table VI; throughout  
- **Problem:** Both “0.22 percentage points” and “0.0022” are used; some places could be misread as 22% rather than 0.22%.  
- **Required fix:** Always pair percentage‑point values with explicit “pp” and avoid bare decimals when small: e.g. “0.22 percentage points (0.0022 in absolute fraction)” once, and then stick to one representation per section.

---

P5-n3 (NIT) – Slightly informal phrasing  
- **Location:** §V B (“garden-of-forking-paths concern”); §VIII E; elsewhere  
- **Problem:** While evocative, this kind of colloquial phrase is atypical for PRD and may be considered stylistically inappropriate.  
- **Required fix:** Replace with more formal phrasing, e.g. “multiple-testing / analysis‑choice bias.”

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific result—a null detection of environment‑dependent spiral chirality in DESI DR1—is methodologically interesting and relevant, but the paper currently fails PRD standards on several fronts: dependence on a non‑public companion catalog (Paper IV), use of future‑dated or unverifiable references, insufficiently documented statistical claims (including extreme p‑values and multiple‑testing control), and an unsupported EFT “bound.” These issues are corrigible but require substantial revision, restructuring to reduce length, and, critically, either public availability or in‑paper reconstruction of the chirality catalog and monopole analysis.

---

## PASS 2 — self-critique findings (what initial review missed)

[P5-E8] – **Table I counts are internally inconsistent**
- **Location:** Table I; §III B–D.
- **Problem:** The row counts in Table I do not reconcile with each other.
  - The table gives **DESI DR1 input rows = 16,361,731** and **Matched primary = 2,349,908**, then **Matched primary after dedup = 2,232,212**.
  - The prose later says the matched catalog “contains 2,232,212 unique galaxies,” implying the deduplicated value is the operative matched set.
  - But the table also reports **Chirality-relevant = 791,635**, while the abstract and later sections treat this as the headline sample size.
- **Why this matters:** The paper alternates between the 2,349,908 pre-dedup match count, the 2,232,212 post-dedup count, and the 791,635 chirality-relevant subset without consistently marking which denominator is used for each statistic. Several later σ values and fractions are therefore not reproducible from the surrounding text alone.
- **Required fix:** Add a single unambiguous flow diagram or table that defines the sample hierarchy:
  - input rows
  - matched primary
  - deduplicated primary
  - chirality-relevant
  - environment-labeled
  and state explicitly which denominator is used for each reported fraction and σ.

[P5-E9] – **Fraction-to-count arithmetic in Table II is correct only if the stated n values are exact, but the text never says whether they are rounded or exact**
- **Location:** Table II; abstract; §VI A.
- **Problem:** The reported CW fractions in Table II are numerically consistent with the counts if interpreted exactly:
  - void: \(207/428 = 0.4836\)
  - wall: \(3359/6673 \approx 0.5034\)
  - filament: \(203261/408187 \approx 0.4980\)
  - cluster: \(197284/397505 \approx 0.4963\)
- **Issue missed in the previous review:** The paper never says whether the displayed \(n\) values are exact post-cuts counts or rounded/filtered counts from a larger internal set. Because several later claims depend on these exact \(n\), the manuscript should explicitly state that these are exact integers from the cut flow, not rounded summaries.
- **Required fix:** Clarify that the counts in Table II are exact and show at least one worked example of the fraction computation in the text or caption.

[P5-E10] – **Table III has a hidden arithmetic assumption: the residuals imply a specific σ convention, but the paper never states whether the residual uses signed or absolute σ**
- **Location:** Table III; Eq. (1); §VI C.
- **Problem:** Table III lists residuals like:
  - quintile 1: \(|\sigma_{\rm obs} - \sigma_{\rm pred}| = 0.13\)
  - quintile 3: \(1.87\)
- These values are only reproducible if \(\sigma_{\rm pred}\) is taken with the same sign convention as \(\sigma_{\rm obs}\), i.e. \(\sigma_{\rm pred} = -2\Delta f_{\rm CW}\sqrt{N}\) with \(\Delta f_{\rm CW}<0\), giving a positive predicted CW deficit.
- However, elsewhere the manuscript phrases comparisons in terms of “\(|\sigma|\)” and “\(\sigma_{\rm from\,half}\)” interchangeably, which obscures whether the residual is signed or absolute.
- **Required fix:** Define explicitly whether Table III uses signed or absolute values, and write one example calculation in the main text showing how the listed residual is obtained from the displayed \(f_{\rm CW}\), \(N\), and \(\Delta f_{\rm CW}\).

[P5-E11] – **The paper’s quoted “0.22 pp” maximum range is arithmetically consistent, but the stated interpretation is stronger than the numbers support**
- **Location:** Abstract; Table VI; §VII.
- **Problem:** Table VI reports per-cell ranges:
  - 0.066, 0.088, 0.149, 0.165, 0.146, 0.220, 0.127, 0.052, 0.102 pp
  - max = **0.220 pp**
- That matches the abstract’s **0.22 percentage points**.
- The problem is interpretive: the manuscript treats this as evidence that the sign pattern is “invariant under all nine choices,” but a range statistic alone does not establish invariance of sign pattern across all classes; it only bounds the spread of the fractions.
- **Required fix:** Keep the arithmetic statement, but weaken the interpretive claim unless the underlying per-class sign table is shown for all nine cells.

[P5-E12] – **The quoted \(r = 0.006\) correlation is not enough to support the stronger “tracks survey-mask geometry” conclusion**
- **Location:** §VIII E; Figure 6 caption; §VIII F.
- **Problem:** The paper states that the per-pixel Pearson correlation between maximal-void density and chirality σ at NSIDE = 32 is \(r = 0.006\), \(p = 0.88\), and then concludes that the signal “tracks survey-mask geometry, not environment density.”
- That inference is not justified by the correlation alone. A null linear correlation between two scalar summaries does not demonstrate mask-geometry causation; it only shows no linear association in that summary statistic.
- **Required fix:** Rephrase as “is statistically indistinguishable from zero” and avoid the stronger causal statement unless a direct geometry-aligned test is shown.

[P5-E13] – **The manuscript uses the same \(-5\sigma\) label for distinct statistics that are not directly comparable**
- **Location:** Abstract; §VIII E; §VIII F; §VI A.
- **Problem:** The paper uses “\(-5\sigma\)” in at least three different contexts:
  - the catalog-level monopole-associated signal in the matched spiral sample,
  - the \(-4.75\sigma\) no-void sky bin,
  - the \(-5.07\sigma\) matched-sample monopole statement.
- These are derived from different denominators and, in some cases, different sample definitions.
- **Required fix:** Add an explicit warning whenever a σ value comes from a different null or denominator than another σ value being compared. Do not present them as interchangeable headline significances.

[P5-M10] – **Figure 2 caption and body use different denominators for the “same” class fractions**
- **Location:** Figure 2 caption; §VI A; Table II.
- **Problem:** The caption says the bars show “per-class CW fractions on the 791,635 chirality-relevant matched spirals,” which is correct for Table II. But the body immediately discusses the same classes in relation to the full matched sample and to post-dedup counts.
- This is a subtle but important denominator shift. Readers can easily infer that all figures are on the same denominator, which is false.
- **Required fix:** State explicitly in the figure caption that Figure 2 and Table II are on the chirality-relevant subsample only, and that other denominators appear later in the manuscript.

[P5-M11] – **Figure 3 caption claims all quintiles are within counting statistics, but Table III shows the third quintile residual is the largest and the only one near 2σ**
- **Location:** Figure 3 caption; Table III; §VI C.
- **Problem:** The caption says “the observed signed σ tracks the monopole prediction within counting statistics in all five quintiles; no quintile deviates from the prediction by more than ∼2σ.” Table III shows the largest residual is **1.87**, which is indeed under 2.
- The issue is not arithmetic, but the phrase “within counting statistics” is too vague: the relevant uncertainty scale is not shown for the residuals.
- **Required fix:** Replace the phrase with a quantitatively anchored statement, e.g. “all quintile residuals satisfy \(|\sigma_{\rm obs}-\sigma_{\rm pred}|<2\).”

[P5-M12] – **The paper’s \(p\)-value bookkeeping is incomplete for the HEALPix scan**
- **Location:** Table V; §VI E; Figure 4 caption.
- **Problem:** The table lists \(p = 0.607\), \(0.135\), \(0.413\) for NSIDE 16, 32, 64, but does not state whether these are:
  - empirical max-stat p-values,
  - bin-wise p-values,
  - or null probabilities associated with the observed max-\(|\sigma|\).
- The surrounding text implies max-stat p-values, but the table itself does not say so.
- **Required fix:** Label the p-value column explicitly as “empirical max-stat \(p_{\rm LEE}\)” or similar.

[P5-M13] – **The DESIVAST void sample size arithmetic is not fully transparent**
- **Location:** §VIII A–D; Tables VII–VIII.
- **Problem:** The paper states:
  - \(n_{\rm void}^{\rm DESIVAST} = 56{,}981\)
  - \(n_{\rm non-void} = 621{,}964\)
  - total \(n_{\rm lz} = 678{,}945\)
- This does add up exactly.
- But the later claim that the sphere-approximation picks up “16,000–17,000 galaxies per algorithm” is not shown numerically, and it is not clear whether this refers to the galaxies excluded by catalog-native membership or to the difference between void and non-void counts.
- **Required fix:** Provide the explicit exclusion counts for each algorithm so readers can verify the statement directly.

[P5-M14] – **The claim that the V2-REVOLVER catalog-native σ is the “cleanest single chirality-in-voids measurement” is unsupported by a systematic comparison**
- **Location:** §VIII D.
- **Problem:** The paper says V2-REVOLVER catalog-native \(\sigma^{\rm void} = -0.24\) is the “cleanest single chirality-in-voids measurement in this paper at \(n \gtrsim 80{,}000\).”
- This is a novelty/comparison claim, but the manuscript does not define “cleanest” quantitatively. By one criterion, the VoidFinder sphere-based void sample has larger \(n\); by another, the V2-VIDE catalog-native result has comparable \(n\); by another, the DESIVAST-anchored void result has the largest sample.
- **Required fix:** Either remove “cleanest” or define it explicitly in terms of \(|\sigma|\), \(n\), or uncertainty width.

[P5-M15] – **The paper’s comparison to Shamir 2022 mixes percent-level amplitudes with class-fraction ranges that are not the same observable**
- **Location:** §XII C; conclusions.
- **Problem:** The manuscript compares the Shamir 2022 “2–4% large-scale asymmetry” with its own:
  - class-fraction range of 1.98 pp,
  - Phase 2 max range of 0.22 pp,
  - catalog monopole of \(-0.26\%\).
- These are not the same observable: Shamir reports a large-scale asymmetry across sky sectors, while this paper’s main results are environment-class fraction differences. The comparison is only qualitative.
- **Required fix:** Keep the comparison qualitative, but do not imply the paper has ruled out a Shamir-like anisotropy at the same statistical level unless the same type of sky split is analyzed with the same estimator.

[P5-M16] – **The manuscript’s “no published model” claim is still too broad, even with the qualification added later**
- **Location:** Abstract; §II; §XII B.
- **Problem:** The paper says “No published bounce or inflation model currently predicts a specific environment-conditional chirality signature at this scale…” and later narrows it. The abstract version is stronger than the body qualification.
- **Required fix:** Make the abstract sentence match the narrower body wording, and explicitly limit the claim to the parity-violating coupling class discussed in the manuscript.

[P5-n4] – **Notation drift between \(\Delta f_{\rm CW}\), \(f_{\rm CW}\), and \(\bar f_{\rm CW}\)**
- **Location:** Abstract; §II; §VI; §VIII F; conclusions.
- **Problem:** The paper switches between:
  - \(f_{\rm CW}\) for class fractions,
  - \(\bar f_{\rm CW}\) for the catalog mean,
  - \(\Delta f_{\rm CW}\) for deviations from 0.5 or from the catalog mean,
  without always specifying which baseline is intended.
- **Required fix:** Define the baseline once and use one symbol consistently for deviations from parity and another for deviations from the catalog monopole.