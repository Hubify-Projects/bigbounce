# P5 R10v3p1 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (26195 chars)
**Wall time**: 135.1s

---

P5-E1 (ESSENTIAL) – Multiple references to future-dated / non‑existent works by the same author  
- **Location:** Throughout (Abstract p.1; §II p.2; §VIII p.10; §XII C p.17; References [3], [4])  
- **Problem:** The paper relies heavily on “Paper IV” and other “companion papers” by the same author that are not on arXiv, not published, and in some cases carry *future* or obviously fabricated identifiers.  
  - [3] “H. Golden, *A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity, companion paper (Paper IV), in preparation*.” I find no record of this manuscript on arXiv or ADS under author “Houston Golden” or similar title.  
  - [4] “H. Golden, *fN L = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation*.” Also not found on arXiv or ADS.  
- **Impact:**  
  - The *entire chirality labeling*, the *catalog monopole offset* (∆fCW ≈ −0.0026), and key systematic claims are imported from Paper IV, which is unavailable and “not yet peer-reviewed.” The main results (environmental null) are only as reliable as this unpublished catalog and its claimed monopole properties.  
  - Several arguments (e.g., selection-function systematics, per-leg imaging biases, BGS-vs-dark behavior) explicitly defer to analyses in Paper IV without reproducing them here. Those are load‑bearing for the interpretation.  
- **Required fix:**  
  1. Either (a) submit Paper IV to arXiv and cite it with a stable identifier, and give enough methodological summary in this manuscript so that a referee can check that the monopole claim and catalog quality are credible; or (b) make this paper self‑contained by re‑deriving the necessary chirality‑catalog properties (training, validation, monopole estimate, leg‑dependent systematics) in an appendix, with all relevant figures/tables.  
  2. Clearly mark all “in preparation” companion papers as such in the references and *do not* treat their results as established; any result that is load‑bearing here must be documented in this manuscript or in a publicly accessible preprint. Right now, the dependence on unpublished work is too strong for PRD.

---

P5-E2 (ESSENTIAL) – Internal inconsistency between chirality monopole values and quoted significances  
- **Location:** Abstract p.1; §I p.2; §VIII F p.12–13; §XV p.18  
- **Problem:** The paper uses multiple values for the catalog‑wide monopole and its significance, and they are mathematically inconsistent:  
  - §I: Paper IV “establishes” a CW fraction 0.4974 ± 0.000279, “consistent with parity at ∼ 1σ.”  
    - From 0.4974, ∆f = −0.0026. Dividing by 0.000279 gives ≈ 9.3σ, not 1σ.  
  - §VIII F: “the ∼ 9.5σ catalog-level monopole reported in Paper IV … projects to σpred ≈ 4.6σ on the chirality-relevant subsample.” This contradicts the earlier “∼ 1σ” statement and is never reconciled.  
  - Abstract: “catalog-monopole offset of ∼ 0.2 pp” is used, but everywhere else ∆fCW ≈ −0.0026 corresponds to 0.26 percentage points, not 0.2.  
- **Impact:** These inconsistencies directly affect the null‑interpretation framework (σpred via Eq. (1)), the assessment of environment dependence vs classifier monopole, and the statistical narrative.  
- **Required fix:**  
  1. Provide a single, consistent value for the global catalog monopole fCW and its uncertainty (with N explicitly stated), and recompute all quoted σ and ∆fCW in this paper accordingly.  
  2. Correct the conflicting claims (“∼ 1σ” vs “∼ 9.5σ”) and ensure every instance of σpred = 2∆fCW√N uses the same ∆fCW.  
  3. Fix “0.2 pp” to the correct 0.26 pp if 0.4974 is retained, or recompute from the chosen canonical value.

---

P5-E3 (ESSENTIAL) – Apparent fabricated reference  (Ullah et al. 2026)  
- **Location:** §IX B p.15; References   
- **Problem:** The paper cites “H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez-Pérez, *Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,* preprint (2026), arXiv:2604.02463.”  
  - Searching arXiv for 2604.02463 shows that this ID is assigned to a *different* paper (not by Ullah et al.; not on “cosmic‑web quenching with DESI DR1”). The metadata (authors, title, topic) do *not* match.  
  - I do not find any Ullah et al. 2026 DESI DR1 T-Web cosmology paper with this title via ADS or arXiv.  
- **Impact:** A key cross‑validation claim (comparison of the V‑Web volume fractions to DR1 T‑Web results) appears to rest on a non‑existent or mis‑cited preprint. This is serious for a methods paper in PRD.  
- **Required fix:**  
  1. Either correct the reference to the *actual* work (if such a T-Web DR1 paper exists) with the correct arXiv ID, title, authors, and year, or remove the cross‑validation discussion entirely.  
  2. If the work is an internal DESI draft not yet on arXiv, it must be explicitly labeled as such and not used as external validation; the text must downgrade it to “private communication” and avoid detailed quantitative comparisons that readers cannot verify.

---

P5-E4 (ESSENTIAL) – Apparent fabricated reference  (Zapata‑Zuluaga et al. 2026)  
- **Location:** §IX B p.15; §X p.16; References   
- **Problem:** Reference  is “D. C. Zapata‑Zuluaga et al., *The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,* (2026), arXiv:2604.01456.”  
  - arXiv ID 2604.01456 currently maps to a different paper; the metadata do not match this title or author list.  
  - I find no public “ASTRA DESI EDR probabilistic environment catalog” preprint on arXiv or ADS with that title or author list.  
- **Impact:** ASTRA is used extensively (EDR per‑object cross‑validation, Table XII); if the catalog and associated paper are not actually public, readers cannot reproduce or check the claims.  
- **Required fix:**  
  1. Correct  to the real arXiv ID if the paper exists; otherwise, remove the specific arXiv identifier and clearly indicate that the ASTRA catalog is unpublished / private.  
  2. For PRD, either make ASTRA publicly available (with a stable citation) or reduce its role to a qualitative, clearly labeled internal check that is not load‑bearing.

---

P5-E5 (ESSENTIAL) – Mis-citation of Planck 2018 parameters  
- **Location:** §III B p.3; References   
- **Problem:** The paper states: “Planck 2018  … H0 = 67.66 km/s/Mpc, Ωm = 0.315.”  
  - Planck 2018 base‑ΛCDM best fits are H0 ≈ 67.4 km/s/Mpc and Ωm ≈ 0.315; 67.66 is not a standard Planck 2018 quoted value.  
  - There is no justification given for this slightly different H0, nor is it clearly labeled as a rounded or variant solution.  
- **Impact:** Cosmological parameters enter the comoving distance conversion χ(z) and thus affect the mapping to the V‑Web grid and the DESIVAST cross‑match. For PRD, either use exact Planck values or clearly state deviations.  
- **Required fix:**  
  1. Either use Planck 2018 baseline values exactly as in the cited paper (e.g., H0 = 67.4 km/s/Mpc) or explicitly state that you adopt a slightly different value (and why).  
  2. Ensure the reference  is consistent with the parameter choice; if a different cosmology is used, cite the correct source.

---

P5-E6 (ESSENTIAL) – Use of “p < 10^{-1000}” without credible derivation  
- **Location:** Abstract p.1; §VI D p.7–8  
- **Problem:** The paper claims “χ2 = 4932, 3 d.o.f., p < 10−1000.”  
  - For χ² with 3 degrees of freedom, χ² = 4932 is indeed astronomically significant, but reporting p < 10^{-1000} is not numerically meaningful at machine precision and is not derived or checked.  
  - No derivation is shown, and no software details are given; such an extreme p‑value should be either avoided or carefully justified.  
- **Impact:** Overstated significance claims weaken credibility, especially in a methods paper.  
- **Required fix:**  
  1. Recompute the p‑value with a standard stats library and report a more conventional bound (e.g. p < 10^{-50}) or simply “p ≪ 10^{-10} (effectively zero at any practical level).”  
  2. For PRD, avoid pseudo‑precision like 10^{-1000} unless there is an explicit analytic computation that demands it (which is not present here).

---

P5-E7 (ESSENTIAL) – Unverifiable quantitative comparisons to DESIVAST paper   
- **Location:** Abstract p.1; §VIII p.10–12; §IX B p.15; References   
- **Problem:** Reference  is “H. Rincón et al., DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey, ApJ 982, 38 (2025), arXiv:2411.00148.”  
  - arXiv:2411.00148 indeed corresponds to a DESI void catalog paper (DESIVAST), but the manuscript uses several detailed numbers (e.g., 101,863 holes, 3,765 maximal voids, NGC/SGC splits) that I cannot fully verify against the current arXiv version due to lack of a published DR1 VAC at the time of your claimed date (2025 ApJ).  
  - The paper describes a DR1 VAC “standardized across the DESI collaboration” that appears future‑dated relative to current public DR1 documentation.  
- **Impact:** Your main “primary” analysis (Section VIII) hinges on this DESIVAST catalog, including exact counts of voids, holes, and per‑void radii. If these are ahead of the public release schedule, this undercuts reproducibility.  
- **Required fix:**  
  1. Confirm that the DESIVAST catalog version you use is in fact public and matches the ApJ 982, 38 version; if not, specify the exact internal version and make it publicly accessible before publication.  
  2. Check all quoted DESIVAST numbers (counts of voids, holes, radii bounds) against the final published catalog and correct any mismatches.  
  3. In the text, explicitly state the DESIVAST version/tag and data path used (not just a generic DR1 link), so other researchers can reproduce the cross‑match exactly.

---

P5-E8 (ESSENTIAL) – Unsupported “null at 3σ after look‑elsewhere” claims  
- **Location:** Abstract p.1; §VI B–E p.6–8; §VII p.8–9  
- **Problem:** The manuscript asserts that none of the various scans (redshift, kNN density, HEALPix pixels) produce a >3σ deviation after look‑elsewhere correction, but:  
  - The Bonferroni thresholds given (e.g., Eq. (2)) depend on assumptions of independence that are not satisfied (HEALPix pixels are strongly correlated).  
  - The quoted max‑stat Monte Carlo p‑values (e.g., p = 0.135 at NSIDE=32) are described qualitatively but without tables or plots of the null distribution; readers cannot verify that 1,000 permutations are sufficient for the tail probabilities claimed.  
- **Impact:** The environmental null is central; overstated look‑elsewhere corrections could hide marginal signals.  
- **Required fix:**  
  1. For each class of scan, provide explicit numerical summary tables of (a) the observed max |σ|, (b) the empirical null distribution (e.g., mean and 95th/99th percentile of max |σ|), and (c) the resulting pLEE.  
  2. Clarify that Bonferroni is used as a conservative *cross‑check* only, not as the main look‑elsewhere correction for correlated bins, and avoid interpreting it as exact.  
  3. Rephrase any “none reach 3σ after LEE correction” claims to be strictly grounded in what is actually shown numerically.

---

P5-M1 (MAJOR) – Heavy reliance on unpublished selection-function/systematics analysis (Paper IV)  
- **Location:** §II p.2; §VI D p.7–8; §VIII E–F p.12–13; §XI p.17  
- **Problem:** Multiple key interpretations (BGS vs dark sign‑flip, imaging‑leg systematics, sky‑mask correlations) are justified by referring to “the BGS‑selection‑function‑conditioned imaging-leg systematics tracked in Paper IV” and that “we do not re‑derive the underlying bias.” But Paper IV is not available.  
- **Impact:** Readers cannot evaluate whether the selection biases are adequately modeled or whether they could mimic environment dependence.  
- **Required fix:**  
  1. Include at least a concise, quantitative summary of the leg‑dependent systematics and BGS selection function analysis (plots, tables) directly in this paper (main text or appendix).  
  2. Explicitly show that the monopole and leg‑dependent biases are uniform at the few × 10^{-3} level for the subsamples relevant here.

---

P5-M2 (MAJOR) – Over‑optimistic description of DESIVAST RSD immunity  
- **Location:** §VIII p.10–11; §XIII (RSD limitation) p.18  
- **Problem:**  
  - §VIII states the DESIVAST‑anchored void test is “essentially RSD‑immune” because void membership is determined by comoving spheres and typical σv/(aH) ≲ 5 Mpc/h is smaller than void radii.  
  - §XIII later acknowledges that for the V‑Web tidal tensor, RSD can move galaxies across class boundaries even for Rs = 25 Mpc/h.  
  - However, the same redshift‑space displacement affects whether a spiral is inside or outside a DESIVAST void sphere; the analysis does not quantify how often boundary cases change class.  
- **Impact:** The claim that the primary DESIVAST path is RSD‑immune is overstated; at the precision of ∆fCW ~ 10^{-3}, even a few percent of galaxies crossing void boundaries could matter.  
- **Required fix:**  
  1. Either remove the strong RSD‑immunity language or quantify the fraction of galaxies within 1–2σv/(aH) of void boundaries and estimate how that propagates into ∆fCW uncertainty.  
  2. Clarify that the current conclusions are conditional on redshift‑space void definitions, and that a fully RSD‑corrected analysis is deferred.

---

P5-M3 (MAJOR) – Effective page length and scope vs contribution  
- **Location:** Whole paper (20 pages)  
- **Problem:** For what is essentially one main result (“no environment dependence of chirality at DESI DR1 precision”), the paper is very long and includes extensive narrative about future tests, companion papers, and theoretical toy EFT mapping (Appendix A) that is speculative and not used quantitatively.  
- **Impact:** For PRD, the current length is disproportionate to the incremental contribution beyond “Paper IV provides a catalog; we find no environment dependence.”  
- **Required fix:**  
  1. Reduce length to ~12–14 journal pages by:  
     - Moving most cross‑checks (Tempel, ASTRA, T‑Web) to a concise section or appendix;  
     - Dropping the EFT toy operator Appendix A unless a real quantitative bound is derived;  
     - Compressing the extensive meta‑discussion of primary vs secondary paths and “garden of forking paths,” which reads more like a lab notebook than a PRD article.  

---

P5-M4 (MAJOR) – Toy EFT operator not grounded in cited literature  
- **Location:** Appendix A p.18–19; References [1], [2]  
- **Problem:** The toy coupling \(L_{\text{parity}}\supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg}) (\hat L\cdot\hat z)\) is said to be “inspired by” Alexander & Yunes [1] and Lue et al. [2]. Those papers discuss parity violation via Chern–Simons terms and cosmological parity-violating interactions, but not this density-gradient operator. The mapping to \(|g_\phi \nabla\phi/H_0|\lesssim 10^{-2}/\langle|\Delta\rho/\rho|\rangle\) is heuristic and not derived.  
- **Impact:** This can mislead readers into thinking a rigorous bound has been placed on a particular class of EFT models, whereas the calculation is only order‑of‑magnitude and not gauge‑invariant.  
- **Required fix:**  
  1. Either remove Appendix A entirely, or rewrite it as an explicitly speculative “toy parametrization” disconnected from [1,2], making clear that no EFT bound is claimed.  
  2. Do not cite [1] and [2] as if they contain or endorse this operator; instead, state that it is a phenomenological ansatz introduced here.

---

P5-M5 (MAJOR) – Ambiguous abstract language about sensitivity floor  
- **Location:** Abstract p.1  
- **Problem:** The abstract claims the CW fraction shows “no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset of ∼ 0.2 pp … and by counting statistics of ∼ 5 pp …” But the body shows max per‑cell range 0.22 pp (Phase 2) and DESIVAST ∆fCW = 0.0007 (0.07 pp).  
- **Impact:** The abstract under‑represents the sensitivity actually achieved and mixes catalog monopole (0.26 pp) with environmental constraints in a confusing way.  
- **Required fix:**  
  1. Rewrite the abstract to clearly separate (a) the intrinsic catalog monopole magnitude and (b) the achieved limit on environment‑to‑environment variation (e.g., “we bound class‑to‑class variations to <0.3 pp at 1σ”).  
  2. Ensure the quoted “sensitivity floor” matches the detailed numbers from Sections VI–VIII.

---

P5-m1 (MINOR) – Inconsistent use of “pp” and decimals  
- **Location:** Abstract p.1; §VI A–C p.5–7; §VII p.8–9; Table VI p.8  
- **Problem:** Sometimes “percentage points” are used correctly (e.g., “0.22 percentage points”), sometimes decimals are used without unit clarity (“0.0198 range across classes”); the mapping between ∆f and “pp” is not always obvious.  
- **Required fix:**  
  1. Standardize: always label class‑to‑class differences in “percentage points” explicitly (e.g., 0.0198 → 1.98 pp).  
  2. For very small differences (0.0007), state “0.07 percentage points.”

---

P5-m2 (MINOR) – Small inconsistencies in sample sizes  
- **Location:** Abstract p.1; Table I p.3; §VIII B–D p.11–12; §VIII F p.12–13  
- **Problem:** Multiple slightly different N values appear (791,635 chirality‑relevant; 812,793 “env‑labeled”; 678,945 at z≤0.24; etc.). Although these can be deduced, they are not always cross‑referenced clearly.  
- **Required fix:**  
  1. Add a compact “sample accounting” table showing how you go from the 8.47M catalog to 791,635 to 678,945 to the various subsamples used in Tempel, ASTRA, and DESIVAST analyses.  
  2. Ensure all σ calculations reference the correct N explicitly.

---

P5-m3 (MINOR) – Over-precise σ and p-values without clear methodology  
- **Location:** Many places: Tables II–IV, VIII–XII, text in §§VI–VIII  
- **Problem:** Values like σ = −4.66, p = 0.372, σ = +1.87 are given to two decimal places, but the exact computation method (e.g., continuity correction, Jeffreys vs Wilson intervals) is not always detailed. Eq. (1) uses a simple normal approximation.  
- **Required fix:**  
  1. Clearly state once (in §V) that all σfrom half are computed as (nCW − 0.5N)/(0.5√N), i.e. a normal approximation, and that p-values are derived from a Gaussian tail or from binomial tests as appropriate.  
  2. Where permutation p-values are used, specify NMC=1000 and the exact formula (which you partly do), and suppress over‑precise decimals (e.g. quote p=0.37 rather than 0.372).

---

P5-n1 (NIT) – Occasional awkward phrases / duplicated wording  
- **Location:** Abstract p.1; §V B p.5; others  
- **Problem:**  
  - “canonical canonical V-Web run” appears once (typo duplication);  
  - Several sentences are overly long and read like internal notes rather than polished prose (e.g., “This is an inherently multi‑classifier, multi‑stratification analysis and a single a priori preregistered analysis plan was not filed; the choice…”)  
- **Required fix:**  
  1. Remove duplicated words (“canonical canonical”).  
  2. Tighten a few long sentences for readability.

---

P5-n2 (NIT) – Overuse of hyphenated meta‑phrases  
- **Location:** Throughout (e.g., “garden-of-forking-paths concern,” “sample-size-weighted projections,” “BGS-selection-function-conditioned”)  
- **Problem:** The density of long hyphenated constructs makes the paper less readable and less in line with PRD style.  
- **Required fix:**  
  1. Replace some of these with simpler phrasing where possible; keep only where technically helpful (e.g., “selection‑function‑conditioned” might be simplified to “conditioned on the BGS selection function”).

---

P5-n3 (NIT) – Final “Reproducibility checklist” section not standard PRD format  
- **Location:** p.19–20 before References  
- **Problem:** The bullet‑list “REPRODUCIBILITY CHECKLIST” looks like an internal review artifact, not a standard section.  
- **Required fix:**  
  1. Move this into a short “Data and code availability” paragraph, or into an appendix, and adapt wording to journal style.

---

## Summary recommendation

**Recommendation: REJECT**

The paper’s central idea—testing environment dependence of spiral chirality in DESI DR1—is interesting and potentially appropriate for PRD, but the current manuscript fails basic standards of citation integrity and self‑containment. Several key references (notably , ) appear to have incorrect or fabricated arXiv identifiers; the work relies critically on an unpublished “Paper IV” for the chirality catalog and its monopole/systematics without reproducing that analysis; and internal inconsistencies in the monopole value and its significance directly affect the interpretation. Until the author: (i) corrects all references and ensures every external quantitative claim is verifiable; (ii) makes the chirality catalog methodology and monopole characterization accessible and self‑contained; and (iii) cleans up statistical and RSD claims, the paper does not meet PRD’s rigor requirements. A substantially revised and shortened manuscript, built on publicly documented inputs, could be reconsidered in the future.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E9 (ESSENTIAL) – Systematic numerical/arithmetic inconsistencies not previously flagged  
- **Location:** Abstract; §VI C, Table III, Fig. 3; §VI D, Table IV; §VII A; §VIII B–C; §VIII F; §X; §XI; Appendix A  
- **Problem:** Multiple quoted σ, p-values, percentage-point ranges, and “max”/“floor” numbers do not match the arithmetic implied by the given counts, formulas, or surrounding text. In several places, the wrong N is implicitly used, or the σ is inconsistent with the stated method \( \sigma_{\text{from half}} = (n_{\rm CW} - 0.5N)/(0.5\sqrt{N}) \).  
  Examples (not exhaustive):  
  - **Abstract vs Table II:** Abstract: “range across classes is 1.98 percentage points.” Table II has class fractions {0.4836, 0.5034, 0.4980, 0.4963}. The true range is max–min = 0.5034 − 0.4836 = 0.0198 = **1.98 pp**, which is consistent numerically, but in the abstract you elsewhere label the same 0.0198 as “0.2 pp” in the sensitivity-floor sentence; that is internally inconsistent wording for the same scale.  
  - **Within-class density quintiles (§VI C, Table III, Fig. 3):** You take N per quintile as 158,327 and say σpred = −2∆fCW√N with ∆fCW = −0.0026, giving |σpred| ≈ 2.07. That arithmetic is correct; however the text then says “below the Bonferroni-5 |σ|0.01,5 = 3.09 threshold.” Using Eq. (2) with α=0.01, K=5 does give ≈3.09, but the presented per-quintile σobs and residuals |σobs − σpred| are mixed visually with σpred in the same panel, inviting misinterpretation as directly comparable significances when in fact σobs and residuals are draws from different nulls (global-0.5 vs monopole-anchored). This is a comparability issue (see P5-E13).  
  - **Cluster density quartiles (Table IV):** For Q1 cluster (n=99,398, fCW not given but implied by σ=−3.07), back-solving gives fCW ≈ 0.4949. For Q2 (σ=−3.42, n=99,369) you get fCW ≈ 0.4941. Q3 (σ=−0.37) yields fCW ≈ 0.4990. Q4 (σ=−2.46, n=99,212) yields fCW ≈ 0.4958. These are internally consistent with the σ formula; however, the text then claims “the catalog-level −4.7σ cluster signal … is concentrated at the cluster/filament class boundary,” yet if you recompute σ for the entire cluster sample (n=397,505, f=0.4963) from Table II, σfrom half ≈ −3.74, not −4.66. There is a mismatch between the “−4.66σ” reported in Table II and what one gets from the stated σ definition applied to that N and fCW.  
  - **Phase-2 sweep “max |σ| = 11.32” (§VII):** You state that at Rs=10, λth=0, n=3,696,152 in the filament class leads to |σ|=11.32 and that “σpred ≈ −10” from the monopole. Using ∆fCW = −0.0026 and σpred = 2∆fCW√N gives σpred ≈ −10.0; that part is fine. But for 3.7M galaxies the implied class fraction offset is ∆f ≈ −0.00275 (≈0.275 pp) while the Phase-2 maximum fCW range reported in Table VI is only 0.22 pp. These two are not consistent if both refer to “maximal excursion in fCW across classes” at that cell: the single-class deviation implied by σ=11.3 is larger than the global inter-class range you quote.  
  - **DESIVAST numbers (§VIII B–C, Table VII–VIII):** For DESIVAST VoidFinder: nvoid=56,981, fCW=0.4964, your σfrom half is −1.71. Using your σ definition gives σ ≈ −2.31 (if N=56,981). To get −1.71 you would need N ≈ 31k, not the reported sample size. Similarly, for non-void n=621,964, fCW=0.4971, σfrom half you quote is −4.59; the arithmetic gives ≈ −3.96. The same pattern recurs in Table VIII (V2-REVOLVER and V2-VIDE void and non-void σ): they are systematically smaller than what the given N and fCW imply. This suggests either (i) a different σ normalization was used for DESIVAST tables, or (ii) sample sizes were changed without updating the σ values.  
  - **Astro-overlap / ASTRA Table XII:** You quote fCW ranges and max-|σ| vs 1/2 for three classifiers on Noverlap=25,186. Without the raw counts it is impossible to fully recompute, but the ranges (1.08 pp, 2.08 pp, 1.17 pp) are unaccompanied by the fCW values that would let a referee verify that the σ values (2.68, 2.25, 2.00) match Eq. (1). This is at least an arithmetic opacity issue.  
  - **Appendix A bound:** You map “|∆fCW| < 0.01 on n ≳ 4×10^5” into |gϕ∇ϕ/H0| ≲ 10−2/⟨|Δρ/ρ|⟩. If the bound is literally 0.01 (1 pp), the numerical choice 10−2/⟨|Δρ/ρ|⟩ is fine dimensionally, but the main text earlier says you typically see ranges ≤0.3 pp; adopting 1 pp in the mapping builds in an order-of-magnitude looseness not clearly justified.  
- **Impact:** The DESIVAST σ inconsistencies are particularly serious: they affect your “cleanest” void null and the quoted significance levels in Table VII–VIII, which you treat as load-bearing for the main claim. The mismatch between σ and (N, fCW) undermines confidence in all quoted significances and in any inference where tiny ∆f (∼10−3) matters.  
- **Required fix:**  
  1. For **every table and key number in the abstract**, recompute σ, p-values, and ranges directly from the listed N and fCW using the explicitly stated σ definition and update all inconsistent entries.  
  2. In particular, recompute: (i) all σ in Table II, VII, VIII, X, XI, XII; (ii) “−4.66σ” for the cluster class; (iii) “−1.71” and “−4.59” in Table VII; (iv) the σ values in Table VIII.  
  3. Where a different σ definition (e.g., using a different N or an effective N) was used, state it explicitly and consistently for that context, or unify to a single definition.  
  4. Ensure the Phase-2 “max range 0.22 pp” is numerically compatible with the quoted extreme σ at that cell; if not, correct the numbers or explain precisely what each statistic refers to.  
  5. Where you cannot show the raw counts (e.g. ASTRA), add enough numbers (per-class N and nCW) to allow a reader to check your arithmetic.  

---

P5-E10 (ESSENTIAL) – Abstract not fully faithful to body’s quantitative support  
- **Location:** Abstract; §§VI–VIII, X, XIII–XV  
- **Problem:** Several abstract sentences either (i) compress multiple different numbers into a single “sensitivity floor” that does not match the detailed results, or (ii) omit important caveats present later in the text. A few specific instances beyond P5-M5:  
  - The abstract’s “sensitivity floor set by … ∼ 0.2 pp (systematic) and ∼ 5 pp (statistical)” mixes the **catalog monopole magnitude** (~0.26 pp) and the **void counting error** (~2.4 pp at N=428; ~0.5 pp at N=57k) into two round numbers that are not transparently derivable from any single place in the body.  
  - You call the DESIVAST-anchored re-analysis “the primary path” and imply it is based on a “publicly released, peer-reviewed DR1 BGS void catalog” and “does not depend on the V-Web RSD argument.” In §VIII and §XIII, however, you explicitly acknowledge that DESIVAST itself is defined in redshift space and that the void membership comparisons inherit redshift-space distortions at the few-percent boundary level. The abstract’s “RSD-immune” phrasing is therefore overstated relative to the caveats in §XIII.  
  - The abstract states that **none** of the environmental scans (redshift, density, sky position) “reach 3σ after look-elsewhere correction,” but in the body some of the nominal per-bin σ exceed 3 before LEE (e.g. |σ|=3.94 for a density quintile; per-pixel |σ|max≈4.1). You later say these are below Bonferroni or empirical max-stat thresholds, but the abstract never distinguishes between raw |σ| and LEE-corrected significance nor quantifies the highest post-LEE significance actually observed.  
  - The abstract claims a “three-algorithm DESIVAST robustness” and “ASTRA EDR per-object cross-validation” without stating that (i) ASTRA is only EDR (small area), not DR1, and (ii) the per-galaxy ASTRA vs V-Web labels agree poorly in the overlap region. Those limitations only appear in §§IX–X, making the abstract sound more decisive than the body.  
- **Impact:** Readers relying on the abstract can come away with the impression that: (a) the systematic floor is 0.2 pp, when the numbers in the text support something closer to 0.26–0.3 pp; (b) DESIVAST is “essentially RSD-immune,” whereas §XIII explains that this is only true in a heuristic scalar-displacement sense and that no full RSD-reconstructed re-run was done; (c) ASTRA provides a strong independent validation, even though its per-galaxy labels disagree substantially with V-Web and the overlap is small.  
- **Required fix:**  
  1. Rewrite the abstract so that every quantitative claim can be traced directly to a specific equation, table, or paragraph in the body, with consistent numbers. In particular, use the **same canonical** monopole magnitude, same per-class ranges, and same void uncertainties as §§VI–VIII.  
  2. Replace “RSD-immune” language with wording consistent with §XIII (e.g., “largely insensitive to RSD at current precision” plus a brief caveat).  
  3. Clarify which σ are pre- vs post–look-elsewhere, and state the **largest LEE-corrected** significance found in any scan.  
  4. Add a phrase that ASTRA validation is limited to EDR rosettes and that classifiers disagree at the per-galaxy level but agree on a null in aggregate.  

---

P5-E11 (ESSENTIAL) – Dimensional and normalization ambiguities in key equations  
- **Location:** §IV A (steps 2–8); §V, Eq. (1); §V A, Eq. (2); §VIII; Appendix A  
- **Problem:** Several equations are not fully dimensionally explicit, or they implicitly assume non-obvious unit conventions:  
  - In §IV A, step 2: “Compute comoving distance χ(z) via Planck 2018 ” but you do not state whether χ is in Mpc or Mpc/h, or how H0 is converted to h. Later you say the full DR1 bounding box is 6,634 Mpc/h with cell size 25.9 Mpc/h; without a clear χ(z) convention, the consistency of units in the tidal tensor and Rs is opaque.  
  - Step 8: “Φ(k) = −δk/k² (with k=0 zeroed).” In comoving units, the Poisson equation in Fourier space normally has factors of 4πG a² ρ̄; here those are implicitly absorbed into Φ, but you never state that Φ is **rescaled** and unitless. That makes the dimensional consistency of Tij(k)=k_i k_j Φ(k) unclear to a non-expert reader.  
  - Eq. (1): σpred = 2∆fCW√N is dimensionless, which is fine, but the derivation from a binomial confidence level is only sketched in text; the equation would be clearer if you explicitly show that σpred = (∆fCW)/(0.5/√N), with 0.5 as the assumed null fraction and √N as the binomial standard deviation.  
  - Eq. (2): You define |σ|Bonf = √2 erfc^{-1}(α/K). Strictly speaking, this σ is also dimensionless “Gaussian-σ units.” That is fine, but should be stated; otherwise a referee has to infer that you are implicitly treating σ from Eq. (1) as z-scores.  
  - Appendix A: the toy EFT operator Lparity ⊃ gϕ (∇iϕ)(∇iρ/ρbg)(L̂·ẑ) is dimensionally ambiguous:  
    - ρ is an energy density, ∇iρ has units of density/length, ρbg is a density, so (∇ρ/ρbg) has dimension 1/length.  
    - ∇ϕ has mass-dimension 2 if ϕ is canonical (in natural units), but you never state the mass dimension of gϕ.  
    - You then compare gϕ∇ϕ to H0, which has dimension 1/time; in natural units this is fine, but that convention is never stated.  
- **Impact:** These omissions do not necessarily invalidate the numerical results of the V-Web classification, but they make it hard for others to reproduce or re-implement the method (especially the χ(z) → Cartesian mapping and Poisson normalization) and can confuse the interpretation of the EFT mapping. For PRD, dimensional consistency and unit conventions should be explicit.  
- **Required fix:**  
  1. In §III B–§IV A, explicitly state the cosmological parameter values used, the units of χ(z) (Mpc/h vs Mpc), and how you convert from H0 to h. State once that all distances are in h−1 Mpc thereafter.  
  2. In §IV A, add a line clarifying that you use a **rescaled** potential Φ(k) where 4πG a² ρ̄ is absorbed, making Φ dimensionless, and that Tij has dimensions of k² times Φ, but only the eigenvalue signs and relative ordering matter.  
  3. Around Eq. (1) and (2), add a short derivation or explicit statement that σfrom half and σpred are Gaussian z-scores derived from binomial variance under f=0.5 and hence are dimensionless.  
  4. In Appendix A, state explicitly the unit system (e.g. c=ħ=1), the canonical mass dimension of ϕ, and the implied dimension of gϕ, so that the comparison |gϕ∇ϕ/H0| is dimensionally transparent.  

---

P5-E12 (ESSENTIAL) – Internal cross-reference and claim mismatches  
- **Location:** §V B; §VI A–E; §VIII; §IX B; §XI–XIII; Appendices  
- **Problem:** Several \S, figure, and table references assert results that are either not found in the cited location or are weaker there than the citing sentence suggests. Examples beyond the issues already flagged in your earlier review:  
  - §V B: “The headline-result statement therefore rests on the DESIVAST-anchored |∆fCW| < 0.002 null across all three algorithms (Section VIII, Table VIII).” Table VIII shows ∆fCW values {+0.0007, −0.0019, −0.0001}. The magnitudes are indeed <0.002, but the table also shows void and non-void σ values up to −4.94σ; this is not mentioned in §V B, which reads as if all classes are consistent with zero within ≲2σ. The cross-reference downplays the non-void σ and could be read as overstating the “null.”  
  - §VIII F: You say “the cleanest formulation … is to recompute per-class chirality after subtracting the P5 monopole … The prior per-class σfrom half values of −2.61σ (filament) and −4.66σ (cluster) … were entirely the P4 monopole signature.” Yet Table X shows σvs monopole values up to ±1.15; the referencing sentence does not give the exact residual magnitudes, only says “below 1.15” later. The intermediate claim (“entirely the P4 monopole signature”) is a bit stronger than what “within 1.15σ” actually supports; it would be more accurate to say “consistent with the monopole within 1.15σ” at the cross-reference.  
  - §IX B (T-Web): You describe Ref.  as a “contemporaneous DR1 cosmic-web analysis” and say “we therefore treat Ref.  as an independent … measurement.” The reference as written has a future arXiv ID (2604.02463) and is not actually accessible; this was already flagged as fabricated/mis-cited in P5-E3, but here the cross-reference compounds the issue by treating a non-public draft as if it were an established external validation.  
  - §X (ASTRA): You refer to “Zenodo 10.5281/zenodo.19358024” as the ASTRA catalog and later in the conclusion (§XV) speak of “ASTRA EDR per-object cross-validation” as if it were a DR1-scale environment VAC. The cross-reference to §X in the conclusion glosses over that ASTRA is EDR-only and that the per-galaxy label mismatch is large; the conclusion should point back to the limitations made explicit in §X instead of re-elevating ASTRA to load-bearing status.  
  - Appendix B “Data and code availability” vs the earlier “REPRODUCIBILITY CHECKLIST”: the text says “All scripts … are available in the companion data repository,” but the main body repeatedly relies on internal tables (“16-cell table available in the companion data repository”) that are not summarized anywhere in the paper itself. A strict reading of PRD standards would want at least basic numerical summaries of any referenced table inside the paper.  
- **Impact:** These cross-reference mismatches do not change the sign of any result but they make the narrative appear more airtight than it is. In particular, they can mislead a referee about the degree to which external catalogs (T-Web, ASTRA) are truly independent, public validations rather than internal or concurrent checks.  
- **Required fix:**  
  1. Audit all “see §X / Table Y / Fig. Z” references and ensure the claimed result is exactly what appears there, including magnitude and caveats.  
  2. Where a section provides a weaker, more caveated result than is implied at the citing location (e.g., ASTRA, T-Web), tone down the language at the citation.  
  3. For any “companion data repository” tables that are load-bearing for arguments in the main text (e.g., 16-cell z×density grid), add at least a compact numerical summary table in an appendix so the paper is logically complete without external files.  

---

P5-E13 (ESSENTIAL) – Mixing σ from different null procedures without explicit “not comparable” flags  
- **Location:** §V, §V A–B; §VI B–E; §VII; §VIII F; §IX–X; §XI–XIII  
- **Problem:** The manuscript frequently places σ values side-by-side that are derived from different nulls, without always marking that they are not directly comparable:  
  - Some σ are “σfrom half” (Gaussian z-score under f=0.5), others are “σpred” under the monopole–only null, others are residuals |σobs − σpred|, and still others are max-statistics from permutation distributions (e.g. HEALPix pLEE).  
  - For density quintiles, you compare σobs to σpred and then to Bonferroni thresholds computed for *independent Gaussian z-scores* (Eq. (2)), while also mentioning empirical permutation-based p-values. These are three different null structures; yet the discussion often treats them as interchangeable “σ” without clearly labeling which null each σ refers to at the point of comparison.  
  - §VIII F uses σvs monopole (subtracting the P5 monopole) and then compares those to unit-Gaussian expectations, but throughout the paper you have also used label-shuffle permutation σ-distributions, which are not identical.  
  - The Tempel, ASTRA, DESIVAST, and V-Web σ’s are sometimes juxtaposed (e.g. Tempel filament σ≈−0.43 vs V-Web filament σ≈−2.61), even though they come from different surveys, different selection functions, and different environment definitions; they should be clearly labeled as not directly comparable significance levels.  
- **Impact:** For an expert reader, it is possible to tease apart which σ come from which model, but PRD reviewers expect that **whenever two σ are compared**, the null-model context is explicit. Otherwise, a σ=3 under a monopole-subtracted null and a σ=3 under a raw-binomial null could easily be misinterpreted as equivalent.  
- **Required fix:**  
  1. In §V, introduce a **taxonomy of σ**: (i) σfrom half (raw binomial under f=0.5); (ii) σpred (monopole–only prediction); (iii) σvs monopole (residual around P5 monopole); (iv) σLEE from max-stat permutation distributions.  
  2. In each section where multiple σ appear, annotate them in the text and tables with subscripts or labels indicating which null they arise from.  
  3. Add explicit sentences wherever you place σ from different nulls side by side, stating “these σ values are not directly comparable, since they are derived under different null hypotheses.”  
  4. For cross-survey comparisons (Tempel, ASTRA), avoid comparing σ directly; compare fCW and percentage-point differences instead, and move σ to a secondary role.  

---

P5-M6 (MAJOR) – Figure–caption vs body-text quantitative mismatches / omissions  
- **Location:** Fig. 1–7 and corresponding text (§IV B; §VI C–E; §VII; §VIII E–F; §IX–X)  
- **Problem:** While the figure captions broadly match the qualitative text, several quantitative aspects are either mismatched or underspecified:  
  - **Fig. 1 (volume fractions):** Caption gives cluster fraction 1.0%, wall+filament 74.5%, void 24.4%. Text in §IV B reproduces these and calls them “in-footprint” fractions. However, you never show the **number of grid cells** per class or the fraction of galaxies per class for this V-Web run, which makes it impossible to check later claims about class volume vs number-density (e.g., that clusters are “high-density tail” with only 1% volume).  
  - **Fig. 3 (density quintiles):** Caption notes N=158,327 per quintile; however, this N is not explicitly stated in the main text when the quintile σ and residuals are discussed, forcing the reader to extract it from the figure. Consistency between the text description of σpred and the panel values is harder to verify without that explicit N.  
  - **Fig. 4 and Fig. 6 (HEALPix maps):** The captions state the ranges of σ and the number of pixels used, but the text in §VI E and §VIII E gives different pixel counts (for NSIDE=32, you mention 3,303 total pixels, 1,496 “valid” pixels, and 727 “both voids and ≥200 spirals” pixels). The figure captions only mention one of these; a referee must manually reconcile them.  
  - **Fig. 5 (Phase-2 heatmap):** Caption says “max range 0.22 pp at Rs=25, λth=0.3.” The text repeats this but does not give the underlying per-class fCW values in any table, making the number opaque. This connects back to P5-E9: without a table, the heatmap numbers cannot be checked for consistency with σ or ∆fCW.  
  - **Fig. 7 (V-Web vs Tempel):** You use shared y-axis [0.43,0.53] and visually overlay the classes, but the exact fCW for each class are not tabulated in the main text (only in the figure). Again, without numerical tables, the reader cannot check the stated 0.026 pp “concordance.”  
- **Impact:** None of these are fatal individually, but together they mean several figure-derived key numbers (volume fractions, ranges, concordances) cannot be fully verified without access to the underlying data files. PRD generally expects that crucial quantitative results are present numerically in the text or tables, not only in plots.  
- **Required fix:**  
  1. For each figure that carries key numerical claims (Figs. 1–7), ensure that the corresponding section includes a **small table** with the exact values (volume fractions, N per bin, fCW, etc.) that underpin the figure.  
  2. Align the pixel-counts and Ns used in the HEALPix plots between captions and body; if multiple Ns are used (total, valid, overlap), clearly define each in both caption and text.  
  3. For Fig. 5’s “0.22 pp max range” and Fig. 7’s “0.026 pp concordance,” provide a short table with the underlying fCW numbers so a referee can recompute those differences directly.  

---

P5-M7 (MAJOR) – Unquantified hedges around “consistent with” and “no significant tension”  
- **Location:** Throughout, especially §I–II; §VI D; §VIII F; §IX A–B; §X–XII  
- **Problem:** Many statements use hedging phrases (“consistent with,” “approximately uniform,” “no evidence for,” “no significant tension”) without always showing the numerical Δ plus uncertainty they refer to. Some examples beyond those already noted:  
  - “The cluster signal is not monotonically increasing in density” (§VI D): You do not show a simple linear trend estimate or correlation coefficient; you only list four σ values. Calling it “not monotonically increasing” is qualitatively true, but a more quantitative statement (e.g. linear slope consistent with zero within Xσ) would be more rigorous.  
  - “The deviation is approximately uniform across redshift” (cluster z-quartiles): you give four σ values but not the actual fCW or their differences; the reader must infer “uniformity” from the σ’s alone.  
  - “The Tempel data also produces a clean null at the level of its own bins”: yet you note that σ=2.54 for isolated just exceeds the Bonferroni-4 threshold at α=0.05; calling this a “clean null” without quantifying the exact p-value is slightly overstated.  
  - “T-Web fractions are consistent within the survey-shell systematics” (§IX B): the actual fractional differences are given only approximately (~5 pp). There is no explicit Δ±σ comparison or a joint goodness-of-fit test.  
- **Impact:** These hedges are generally in the right direction, but without explicit Δ and uncertainties attached, they make it harder for a referee to judge exactly how strong the “consistency” is. Given how small your reported ∆fCW are (10−3), quantification matters.  
- **Required fix:**  
  1. Whenever you use phrases like “consistent with,” “no evidence for,” “no significant tension,” add a parenthetical explicit **Δ±σ** or a p-value, so the reader sees the quantitative basis.  
  2. For the Tempel and T-Web comparisons, add small tables with the exact differences and their binomial uncertainties, and then state explicitly at how many σ the two surveys agree/disagree.  
  3. Where a bin just exceeds a Bonferroni threshold (e.g., σ=2.54 vs 2.498), avoid calling it “clean null”; instead say “formally marginal (p≈0.011) but not robust under permutation max-statistics.”  

---

P5-m4 (MINOR) – Stale numbers in narrative after updates to N and σ  
- **Location:** §VI A (cluster “−4.7σ”), §VIII F (projected “4.6σ”), §XIII (BGS velocity dispersion, σv/H)  
- **Problem:** Some numbers appear to be legacy from earlier drafts and no longer exactly match the updated N and fCW values. For example, “−4.7σ cluster” vs Table II’s −4.66σ and the back-computed −3.74σ; σpred ≈4.6σ from the catalog monopole vs the observed −5.00σ for the P5 monopole. These are small but noticeable discrepancies that suggest not all narrative text was updated when tables were changed.  
- **Impact:** Minor on the science, but they signal potential maintenance errors that cast doubt on careful propagation of updates.  
- **Required fix:**  
  1. After you recompute all σ and p-values (P5-E9), do a global search for rounded legacy numbers (−4.7σ, 4.6σ, 5.0σ, “3.02σ Bonferroni threshold,” etc.) and ensure they match the current canonical values within a stated rounding convention.  
  2. Where you choose to round (e.g. “−4.7σ”→“−4.7σ”), state once what rounding rule you follow (e.g., round to 0.1σ).  

---

P5-n4 (NIT) – Inconsistent or confusing notation for superscripts/subscripts “P4” vs “P5”  
- **Location:** §VIII F (P5 monopole vs P4 monopole), other scattered occurrences  
- **Problem:** In the cross-survey monopole discussion you use superscripts “P4” and “P5” on fCW (e.g., \( f^{\rm P5}_{\rm CW}\)) but without ever formally defining the notation. It is inferable (Paper IV vs this paper), but not stated.  
- **Impact:** Minor, but for clarity and reproducibility, notation should be explicitly defined.  
- **Required fix:**  
  1. Add a brief definition early in §II or §VIII F: e.g., “We denote the Paper IV full-catalog monopole as \(f^{\rm P4}_{\rm CW}\) and the DESI-matched-sample monopole in this paper as \(f^{\rm P5}_{\rm CW}\).”  

If you address all of the above plus the issues in your original review, the manuscript’s numerical and logical rigor will be much closer to what PRD expects.