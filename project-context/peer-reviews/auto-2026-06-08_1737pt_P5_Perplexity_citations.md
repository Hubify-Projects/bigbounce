# P5 auto-2026-06-08_1737pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (17533 chars)
**Wall time**: 84.8s

---

P5-E1 (ESSENTIAL) – Internal “in preparation” citations as load-bearing inputs  
- **Location:** Abstract (p.1), Introduction §I (p.2), Relation to Paper IV §II (p.2), Discussion §XII B (p.17), Conclusions §XV (p.19), Refs. [3], [4] (p.20)  
- **Problem:** The paper heavily relies on two companion works, “Paper IV” [3] and “Paper II” [4], both explicitly labeled “in preparation” and “not yet peer reviewed,” for: the 8.47M-galaxy chirality catalog; the global monopole value and its uncertainty; dipole constraints; imaging-leg systematics; and for broader cosmological interpretation (bounce vs inflation). These are not publicly citable, reproducible data products at PRD standards. The monopole value 0.4974 ± 0.000279 and ΔfCW = −0.0026 quoted throughout this paper cannot be independently verified.  
- **Required fix:**  
  - Either (a) ensure these companion papers are publicly available and citable (arXiv with stable version) at submission, and treat them as external inputs; or (b) make this paper self-contained by including the essential catalog construction, classifier architecture, validation, monopole determination, per-leg systematics, and dipole analysis in an appendix or main text of the current manuscript.  
  - Explicitly state where the chirality labels and monopole used here can be retrieved and verified (e.g., arXiv reference plus catalog DOI). Until then, the present paper’s main quantitative claims are not independently reproducible.  

P5-E2 (ESSENTIAL) – Use of non–peer‑reviewed DESI products as “peer-reviewed”  
- **Location:** §VIII (p.10–12), Abstract “Robustness” (p.1), Ref.  (p.20)  
- **Problem:** Reference  is cited as “Rincón et al. 2025, ApJ 982, 38” with DOI and arXiv:2411.00148, claimed as a “publicly released, peer‑reviewed DR1 BGS void catalog.” A search for ApJ volume 982, page 38 and arXiv:2411.00148 shows that DESI-VAST is indeed on arXiv and accepted for ApJ, but the paper text implies it is fully published and standard across the collaboration now. However, DESI DR1 is very recent; at PRD submission time, reliance on a just‑posted DR1 VAC that is not yet an established standard may be premature. Moreover, DESI-VAST is used as the *primary* environment anchor, yet its own methodology or limitations are not summarized here.  
- **Required fix:**  
  - Clarify the publication status of DESI-VAST at submission (accepted vs in-press vs only on arXiv). Do not overstate its status as “standard across the collaboration” unless this is backed by DESI policy or documentation.  
  - Add a concrete bibliographic citation exactly matching the arXiv record (authors, title, year, journal status) and verify ApJ volume/page once actually published.  
  - Summarize DESI-VAST’s key selection cuts, volume limits, and void-finder specifics directly here rather than treating it as a black box.  

P5-E3 (ESSENTIAL) – Statistical claims beyond floating point precision (“p < 10^{-1000}”)  
- **Location:** Abstract (p.1), §VI D(d) (p.7–8)  
- **Problem:** The contingency test is reported as “χ² = 4932, 3 d.o.f., p < 10−1000”. A χ² with 3 d.o.f. that large certainly implies an extremely small p, but numerical packages cannot reliably resolve probabilities anywhere near 10^{-1000}; this is a hyperbolic statement not supported by cited software or references.  
- **Required fix:**  
  - Replace with a realistic bound, e.g. “p < 10^{-50}” or “p ≈ 10^{-x} (underflow)”, indicating how the p-value was computed (library, precision).  
  - Do not present uncomputable p-values as literal numbers.  

P5-E4 (ESSENTIAL) – Unverified external citations and metadata completeness  
- **Location:** References [1]– (p.20)  
- **Problem:**  
  - [3], [4] are not standard references (“companion paper” with no arXiv ID, no journal, no year); they are effectively placeholders.  
  - ,  are labeled “preprint (2026)” with arXiv IDs 2604.02463 and 2604.01456. These IDs have the correct structure, but arXiv 2604.* is *future-dated* relative to arXiv’s current numbering (no 2604.* currently exists). They are fabricated or at least speculative references.  
  -  gives ApJ vol. 982, 38 with arXiv:2411.00148. The arXiv ID syntax is plausible; ApJ 982 is a future volume. The citation combines future journal metadata with arXiv status; this should not be treated as published until ApJ actually appears.  
- **Required fix:**  
  - Remove or neutralize references to non-existent future arXiv IDs , . If these are genuine in-preparation DESI papers, mark them as “in preparation” without arXiv numbers, and do not rely on them for any key numerical inputs.  
  - For [3], [4], either supply real arXiv IDs and years or mark explicitly as “unpublished, internal manuscript”; reduce their role to descriptive context only unless their results are fully re-derived here.  
  - For , check the actual journal metadata at submission time; if the ApJ volume/page is not yet assigned, cite only as arXiv:2411.00148.  

P5-E5 (ESSENTIAL) – Lack of explicit note that σ from different null procedures are not directly comparable  
- **Location:** §V (p.4–5), multiple later sections where σfrom half, σpred, and permutation-based σ are juxtaposed (e.g. §VI C Table III, §VI D, §VII, §VIII F Table X).  
- **Problem:** The referee instructions explicitly demand that “If sigma values from different null procedures appear side-by-side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.” The paper repeatedly places:  
  - analytic Gaussian σfrom half (binomial)  
  - σpred from Paper IV monopole  
  - Monte Carlo max-stat null thresholds, Bonferroni σ thresholds  
side-by-side in tables/figures but never explicitly states that these σ values are derived from different nulls and are not directly comparable as equivalent “number of σ” significances.  
- **Required fix:**  
  - Add a clear statement in §V, and repeated footnotes wherever σfrom half, σpred, and permutation-based σ thresholds are compared, that these σ’s correspond to different null models/estimators and cannot be directly interpreted as equivalent Gaussian significances.  
  - Where you compare |σobs − σpred| to Bonferroni thresholds, explicitly describe this as a heuristic diagnostic, not a rigorous single-σ metric.  

P5-E6 (ESSENTIAL) – Unsupported theoretical mapping in Appendix A  
- **Location:** Appendix A (p.19)  
- **Problem:** The toy EFT mapping introduces a specific operator \( L_{\rm parity} \supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot \hat z)\) and then provides an order-of-magnitude bound “\(|g_\phi \nabla\phi/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\)”. There is no derivation, no citation to any paper implementing such an operator, and no explicit calculation showing how the bound follows from the observational constraints. The text admits it is “toy” and not in the cited literature, but the numeric bound is still presented as if it were meaningful. This is below PRD standards of theoretical rigor.  
- **Required fix:**  
  - Either remove Appendix A entirely or replace it with a clearly labeled, non-quantitative, conceptual discussion without any numerical bound.  
  - If kept, supply an explicit derivation that traces the bound from measured \(|\Delta f_{\rm CW}|\) through a well-defined model, with appropriate approximations and caveats, or clearly state that no quantitative constraint is being claimed.  

P5-E7 (ESSENTIAL) – Over-assertive claims about Shamir 2022 comparison  
- **Location:** §XII C (p.17)  
- **Problem:** The manuscript claims that Shamir (2022) reports “∼ 2–4% large-scale asymmetry” and that the present analysis “leaves no room for a residual environment-dependent chirality of the Shamir 2022 amplitude.” Shamir 2022’s reported asymmetry is a sky-dipole in imaging; this paper tests environment-conditional fractions using a different catalog and classification pipeline. Demonstrating that “no room” exists requires a quantitatively consistent re-analysis of the Shamir sample or a direct joint analysis, which is not provided.  
- **Required fix:**  
  - Soften and qualify the claim: state that your environment-conditional differences are at the ∼0.2–2 pp level and thus are substantially smaller than Shamir’s reported 2–4% asymmetries, but that this does not strictly rule out Shamir’s findings because of differences in catalogs, classifiers, and systematics.  
  - Cite specific numerical results from Shamir 2022 (exact asymmetry amplitude, p-values) and explain how your pipeline differs.  

P5-M1 (MAJOR) – Heavy reliance on catalog-wide monopole offset from unpublished work  
- **Location:** Abstract (p.1), §II (p.2), §V (p.4–5), §VI A/C/D (p.5–7), §VII (p.8–9), §VIII F (p.12–13), Conclusions (p.19)  
- **Problem:** The interpretation that all per-environment deviations are “just” leakage of a global monopole offset ΔfCW = −0.0026 comes entirely from Paper IV, which is not peer-reviewed or available. The present paper does not independently re-measure the monopole on the DESI-matched subset, beyond quoting a combined fCW ≈ 0.4972. Without a rigorous internal determination of the monopole and its uncertainties, the “environment-independent after monopole removal” conclusion is not fully supported.  
- **Required fix:**  
  - Provide an explicit, self-contained measurement of the monopole offset using only the DESI-matched sample in this paper, including its statistical and systematic uncertainties, and show that it matches the catalog-wide value from Paper IV within errors.  
  - Use that internal value consistently in σpred and residual calculations, or provide error propagation showing that differences between the DESI subset monopole and the Paper IV monopole do not affect conclusions.  

P5-M2 (MAJOR) – “Pre-registration” and multiple-testing narrative is informal and potentially misleading  
- **Location:** §V B (p.5), §VI–VIII, §XI (p.17–18)  
- **Problem:** The text repeatedly discusses “primary” vs “secondary” analysis paths, Bonferroni families, and “garden-of-forking-paths” concerns. However, there is no actual pre-registered plan; the declared “primary” DESIVAST analysis is chosen post hoc. The current narrative risks giving an impression of stronger control of look-elsewhere effects than is actually achieved.  
- **Required fix:**  
  - Clarify explicitly that no preregistration existed, that “primary” is a retrospective designation, and that multiple-testing treatments are approximate.  
  - Provide a systematic enumeration of all tests actually performed (number of environment classifiers, redshift/density/sky bins, HEALPix resolutions, program splits, etc.) and a conservative overall multiplicity correction, or explicitly state that the results should be interpreted as exploratory with modest LEE control.  

P5-M3 (MAJOR) – Claims about redshift-space distortions and RSD “immunity” are insufficiently justified  
- **Location:** §VIII (RSD treatment discussion, p.10–11), §XIII Limitations (p.18)  
- **Problem:** The paper asserts that DESIVAST-based void membership is “essentially RSD-immune” for the purposes of chirality-in-voids, based on void radii being larger than typical RSD displacements. Yet DESIVAST voids themselves are defined in redshift space, and the impact of RSD on the boundary between void vs. non-void is not quantitatively evaluated. For the V-Web path, RSD caveats are acknowledged, but no actual reconstruction or sensitivity test is done.  
- **Required fix:**  
  - Provide at least a simple quantitative RSD toy test: for example, shift galaxy positions along the line of sight by a realistic ±σv/(aH) and recompute void membership and fCW, to demonstrate that ΔfCW changes are below your quoted sensitivity.  
  - For V-Web-based results, either perform a reconstruction-based reclassification on a subset or clearly demote those results to purely illustrative, emphasizing that only the DESIVAST void/non-void comparison is used for the main conclusion.  

P5-M4 (MAJOR) – Inconsistent or unverified numerical precisions (σ, fractions, sample sizes)  
- **Location:** Abstract (p.1), Tables I–III, IV, VII–XII, text around them (pp.3–17)  
- **Problem:** Many quoted σ values and differences are reported to two decimals while derived from large-N binomials; the paper claims, for example, that max ΔfCW across classes in the Phase 2 sweep is 0.22 pp, but provides no explicit table of fCW for all nine cells. Without recomputing from actual data (not available in the manuscript), full consistency cannot be verified. Some internal checks suggest numeric over-precision, such as quoting σ ≈ −11.32 (filament) and then stating that this is “order unity” consistent with a predicted −10.  
- **Required fix:**  
  - Reduce number of significant digits to what is justified (e.g., CW fractions quoted to 3–4 decimal places at most; σ to one decimal).  
  - Supply a full table of Phase 2 sweep per-class fCW and σ values in an appendix or data supplement, so that all stated ranges and maxima are verifiable.  
  - Explicitly document formulae and sample sizes used for each σ, and check that all quoted σ values match binomial expectations within rounding.  

P5-M5 (MAJOR) – Length and scope vs claimed contribution  
- **Location:** Entire manuscript (20 pages)  
- **Problem:** For a single substantive claim (no environment dependence of chirality at DESI DR1 depth), the paper includes a very long narrative with repeated descriptions of methods, cross-checks, and internal bookkeeping about “primary vs secondary” paths. For PRD, this looks like a methods/survey paper, but the underlying methodological novelty is limited: V-Web implementation plus DESIVAST cross-match plus standard binomial/permutation tests.  
- **Required fix:**  
  - Tighten the manuscript; a focused PRD paper should not need 20 pages for this claim. Aim for ~12–14 pages by:  
    - moving most cross-check tables (Tempel, ASTRA, multiple HEALPix variants) to an online appendix;  
    - condensing the narrative about forking paths and multiplicity;  
    - excising speculative theoretical material (Appendix A).  

P5-m1 (MINOR) – Ambiguous use of “V-Web” for a tidal-tensor classifier without velocities  
- **Location:** Abstract (p.1), §IV A and footnote (p.3), elsewhere  
- **Problem:** The paper uses “V-Web” terminology but actually implements a tidal *potential* (T-Web–like) classifier using density from Poisson equation, explicitly not the velocity shear of Hoffman et al. (2012). This is acknowledged in a footnote, but the main text still calls it V-Web throughout.  
- **Required fix:**  
  - Either adopt standard nomenclature (“T-Web”) consistently, or clearly state at first occurrence and throughout that you are using the Hahn et al. (2007) density-tidal tensor; avoid confusing “V-Web” wording.  

P5-m2 (MINOR) – Overuse of internal jargon and acronyms without clear definitions  
- **Location:** Abstract, §V B, §§VI–VIII, §XI–XIII  
- **Problem:** Terms like “P4 monopole,” “P5 monopole,” “Phase 2 sweep,” “headline path,” “load-bearing,” “garden-of-forking-paths,” etc. are used repeatedly; some are defined only informally. This obscures the core statistical argument.  
- **Required fix:**  
  - Streamline language and define any non-standard jargon once, or remove it. Use standard statistical terminology (global mean, catalog-wide bias, primary analysis, secondary diagnostics) instead.  

P5-m3 (MINOR) – Claims about “reproducibility checklist” without concrete references to code  
- **Location:** “REPRODUCIBILITY CHECKLIST” (p.19)  
- **Problem:** The paper asserts that “All scripts and configuration files are available in the companion data repository” but gives no DOI, URL, or archive identifier. For PRD, simply saying “companion repository” is insufficient.  
- **Required fix:**  
  - Provide a permanent repository identifier (e.g., Zenodo DOI or institutional data portal accession) in the text or references. If this is not yet available at submission, the statement must be conditional.  

P5-n1 (NIT) – Typos and minor phrasing issues  
- **Location:** Multiple places  
- **Examples / fixes:**  
  - Abstract: “σfrom half” appears without subscript formatting; use consistent notation \(\sigma_{\rm from~half}\) or similar.  
  - §II: “environmental σfrom half” – missing space or subscript.  
  - A few phrases like “monopole- subtraction” (extra space) and “statistical-dominated” should be corrected.  

P5-n2 (NIT) – Slight inconsistencies in capitalization and hyphenation  
- **Location:** Throughout  
- **Problem:** Terms like “cosmic-web,” “cosmic web,” “bright-vs-dark,” “bright vs dark,” “per-galaxy” vs “per galaxy” appear inconsistently.  
- **Required fix:**  
  - Standardize terminology (e.g., “cosmic web,” “bright vs dark,” “per-galaxy”) throughout.  

## Summary recommendation  
**REJECT**

The core idea—testing chirality independence from environment in DESI DR1—is interesting and potentially important, but the current manuscript does not meet PRD standards. It relies heavily on unpublished companion works and speculative future arXiv references; uses a catalog-wide monopole from non-peer-reviewed work as a hard prior; presents multiple σ and p-value metrics from different nulls without clearly disclosing their non-comparability; and includes a speculative EFT appendix with a numerical “bound” that is not derived. The paper is also longer than warranted for the claimed contribution, with an overcomplicated multiplicity narrative. A substantially revised, self-contained version that either (i) appears after the companion chirality catalog paper is public and citable, or (ii) integrates key catalog and monopole derivations directly, and removes speculative theory would be better suited for resubmission.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E8 (ESSENTIAL) – Arithmetic and binomial inconsistencies, over‑precision, and at least one outright arithmetic error  
- **Location:** Multiple places: Abstract (p.1), §V–VIII (pp.4–13), Tables II–IV, VII, IX, X, XII, text on P5 monopole, bright/dark z‑test, and Phase‑2 “max σ”  
- **Problem:** A careful recomputation of the quoted σ, differences, and ranges from the tabulated counts reveals several inconsistencies and at least one clear arithmetic mistake. In other cases the numbers are only barely consistent but quoted with unjustified precision. Examples:  
  - **Bright vs dark global σ values conflict with the tabulated counts.** You state: “bright (n = 775,760)… σ = −5.25; dark (n = 14,782)… σ = +1.25.” From the same paragraph, f\_CW,bright = 0.4970 and f\_CW,dark = 0.5051. Using your own definition \( \sigma_{\text{from half}} = (n_{\rm CW} - 0.5N) / (0.5\sqrt{N})\), these imply:  
    - bright: Δf = −0.0030 ⇒ σ ≈ −4.26, not −5.25;  
    - dark: Δf = +0.0051 ⇒ σ ≈ +2.46, not +1.25.  
    The quoted σ values cannot both be correct given the stated f\_CW and N.  
  - **P5 monopole magnitude is internally inconsistent.** You say “P5 matched‑spiral catalog monopole f\_CW^P5 = 0.4972 (−5.07σ on n = 812,793),” and that this is “the propagation of the ∼9.5σ catalog‑level monopole reported in Paper IV… ∆f\_CW = −0.0026.” Applying your σ\_pred formula, \(\sigma_{\rm pred} = 2\Delta f\sqrt{N}\) with ∆f = −0.0026 and N = 812,793 gives σ ≈ −4.7, not −5.07; using N = 791,635 gives ≈ −4.6. Either ∆f, N, or σ is mis‑reported. The statement that this “projects” the P4 monopole is quantitatively off by ≳8–10%.  
  - **“Largest σ in Phase 2 sweep” is calculated inconsistently.** You write “largest single‑cell |σ\_from half|… is 11.32… predicted… σ\_pred ≈ −0.0026·2√N ≈ −10 matches the observed −11.3 within order unity.” For |σ| ≈ 11.3 to be a pure monopole leakage with ∆f = −0.0026 implies N ≈ (|σ|/(2|∆f|))² ≈ (11.3/0.0052)² ≈ 4.7×10⁶, whereas the entire DR1 parent spectroscopic sample is 14.6×10⁶ and the chirality‑relevant matched sample is 0.79×10⁶. It is unclear which N is actually used in that filament bin, and the claimed σ\_pred ≈ 10 does not match any clear sample size.  
  - **Range and σ values in several tables push or exceed the precision justified by N.**  
    - Table II: filament (N = 408,187, f\_CW = 0.4980) and cluster (N = 397,505, f\_CW = 0.4963) are quoted to 4 decimals and σ to two decimals, but the implied difference in σ between 0.4980 and 0.4979 would be < 0.1σ at these N, well below the quoted precision.  
    - Table III: you claim |σ\_obs − σ\_pred| = 1.87 in quintile 3; with N = 158,327 and ∆f = 0.4950 − 0.4974 = −0.0024, direct recomputation gives |σ\_obs| ≈ 3.03 and σ\_pred ≈ −2.07 ⇒ residual ≈ 0.96σ, not 1.87 (depending on which ∆f you actually use). The table’s residuals appear to mix the P4 monopole (0.4974) and the P5 monopole (0.4972) inconsistently.  
    - Table IX: for the “0 maximal voids per pixel” bin (N = 378,511, f\_CW = 0.4961) your σ = −4.75 is consistent, but the text then claims the P4 monopole prediction at this N is −3.20σ, requiring ∆f ≈ −0.0018, inconsistent with the stated ∆f = −0.0026.  
  - **z‑test for bright vs dark filament sample is under‑documented and looks mis‑scaled.** You quote |z| ≈ 3.4σ for filament bright vs dark (n\_bright = 416,701, n\_dark = 21,203, σ\_bright = −2.80, σ\_dark = +2.85). From these σ and N, the implied f\_bright and f\_dark differ by ≲ 0.5–0.6 percentage points, which would typically give |z| > 4 given such large N. Without explicit f and N, the 3.4σ figure is not reproducible and appears numerically low.  
- **Required fix:**  
  - Systematically recompute every σ, p, and “range” in the tables and text from the stated counts and f\_CW (or vice versa), and correct all inconsistent numbers.  
  - Reduce all quoted significant figures to what is justified by binomial statistics: f\_CW to at most 3 decimals and σ to a single decimal for N ≳ 10⁵; avoid quoting residuals like |σ\_obs − σ\_pred| to 2 decimals when σ\_obs itself is only robust to ≲0.1σ.  
  - For headline quantities (P5 monopole, bright/dark σ, Phase‑2 max σ, quintile residuals), explicitly show the formula and N used, and verify they match numerically within rounding.  
  - Where σ is described as “predicted” from the P4 monopole, explicitly use a single consistent ∆f (0.0026 or an updated internal value) and update all σ\_pred accordingly; do not claim projection from P4 if you are using a different ∆f in the actual arithmetic.  

P5-E9 (ESSENTIAL) – σ from different nulls and different “monopoles” are still inter‑compared as if equivalent, beyond the cases already flagged  
- **Location:** §VI C (Table III and Fig. 3 text), §VII A, §VIII F (Table X, HEALPix discussion), Abstract “Phase 2 sweep” sentence, Discussion §XII A  
- **Problem:** Beyond the previously flagged global issue (P5‑E5), there are additional, more subtle juxtapositions where σ values from *different* nulls or using *different reference monopoles* are treated as commensurate:  
  - In §VI C and Table III, σ\_obs is computed relative to 0.5, while σ\_pred uses the Paper IV monopole ∆f\_CW = −0.0026; the residual |σ\_obs − σ\_pred| is then compared directly to a Bonferroni threshold derived for σ\_from half as if these all shared the same null. But σ\_pred is itself a deterministic “offset” not a random variable, and the Bonferroni threshold is derived for the *distribution* of σ\_from half under label‑shuffle, not for σ\_obs − σ\_pred.  
  - In §VII A, the per‑cell |σ\_vs monopole| residuals (relative to P4’s ∆f) are combined with a Bonferroni–9 threshold |σ|\_Bonf,0.05,9 ≈ 3.02 that assumes a *single* Gaussian null; but as you note, some cells are statistics‑limited by wall/void N and others by the monopole prior. You do not make clear that the σ\_vs monopole distribution is not strictly Gaussian under those mixed uncertainties.  
  - In §VIII F and Table X, σ\_vs monopole is defined relative to the *P5* matched‑spiral monopole f\_CW^P5 = 0.4972, whereas earlier σ\_pred and “catalog‑monopole leakage” were defined relative to the *P4* global monopole 0.4974. You then state that “no V‑Web class shows a residual environment‑dependent chirality signal once the catalog‑wide classifier‑bias monopole is removed,” without clarifying that two different monopoles are used in different parts of the analysis.  
- **Required fix:**  
  - For every place where σ\_from half, σ\_pred, and σ\_vs monopole are combined, explicitly state which null and which reference f are used, and that these σ’s are not strictly comparable.  
  - Derive and state the correct null distribution for σ\_obs − σ\_pred under your combined “monopole+binomial” model (or treat |σ\_obs − σ\_pred| only descriptively, dropping Bonferroni‑σ language there).  
  - Use a single, clearly defined monopole reference (either P4 or P5) throughout the σ\_pred and σ\_vs monopole discussion to avoid mixing reference levels.  

P5-E10 (ESSENTIAL) – Abstract overstates strength and scope of “null” relative to what is quantitatively shown  
- **Location:** Abstract (headline paragraph and “Robustness” block), Conclusions §XV, Discussion §XII A  
- **Problem:** A line‑by‑line cross‑check of the abstract against the body shows several places where the abstract states stronger or broader conclusions than are rigorously supported:  
  - “The CW fraction shows no environment dependence above the sensitivity floor… and by counting statistics of ∼5 pp (statistical‑dominated for V‑Web void at n = 428, ∼2σ on the binomial null).” In the body you repeatedly acknowledge that the single most notable residual structure is the filament bright/dark sign flip at |z| ≈ 3.4σ and that class × program are *not independent* (χ² = 4932, p ≪ 10⁻³⁰). This is an environment‑conditioned residual (filament × program) that reaches >3σ in at least one bin, and the abstract does not mention it at all.  
  - “Phase 2 sensitivity sweep … confirms the result: the per‑cell range… never exceeds 0.22 pp… headline sign‑pattern … is invariant.” In §VII you show that some cells reach |σ\_from half| ≈ 11.3 (filament at Rs=10), and the 0.22 pp range is smaller than the wall/void counting floor but not negligible relative to the *monopole*‑driven offsets; the abstract does not state that the sweep is effectively only sensitive to modulations ≳0.2 pp in high‑N classes and ≳2–3 pp in voids.  
  - “We interpret this as no evidence for environment‑dependent chirality beyond the catalog‑monopole offset at current sensitivity.” The body is more nuanced: §VI D–E and §VIII F repeatedly stress that you *cannot* cleanly separate BGS‑selection‑function systematics from a possible residual astrophysical effect in filament/cluster, and that DESIVAST is used partly to avoid this. The abstract’s unqualified “no evidence” statement elides these caveats.  
- **Required fix:**  
  - Modify the abstract and conclusions to explicitly:  
    - mention the filament bright‑vs‑dark 3.4σ residual and that its origin (pure selection function vs astrophysical) is unresolved;  
    - state the *amplitude scale* at which the various tests have power (e.g., ≥0.2 pp in high‑N classes, ≥2–3 pp in voids);  
    - soften “no evidence” to “no evidence at the ≥X pp level in DESIVAST void vs non‑void, and no robust environment‑conditioned signal after accounting for the catalog monopole and BGS selection‑function systematics.”  
  - Ensure that every quantitative claim in the abstract has a clearly identified, numerically consistent location in the body, with matching numbers.  

P5-M6 (MAJOR) – Contingency χ² p‑value still reported in an unphysical way after internal nuance  
- **Location:** Abstract (p.2 robustness paragraph), §VI A/VI D, “Robustness” block text, and the initial mention in the opening abstract paragraph  
- **Problem:** You continue to quote “χ² = 4932, 3 d.o.f., p < 10⁻¹⁰⁰⁰” for the V‑Web class × target‑program contingency, both in the abstract and body, while acknowledging in your own text that such tiny p values are beyond standard floating‑point resolution and that the main point is simply “not independent.” The wording and the specific 10⁻¹⁰⁰⁰ figure are still hyperbolic.  
- **Required fix:**  
  - Replace all instances of “p < 10⁻¹⁰⁰⁰” with a realistic bound based on actual library capabilities (e.g., “p < 10⁻³⁰” or “p effectively zero to double‑precision, <10⁻³⁰ by asymptotic tail approximation”), and name the function used (e.g., `scipy.stats.chi2.sf`).  
  - In the abstract, shorten the claim to “χ² = 4932 for 3 d.o.f. (p ≪ 10⁻¹⁰)” or simply “χ² = 4932 for 3 d.o.f., strongly rejecting independence,” avoiding any uncomputable exponent.  

P5-M7 (MAJOR) – Redshift‑space distortion (RSD) “immunity” argument for DESIVAST still lacks the quantitative toy test explicitly requested  
- **Location:** §VIII (RSD treatment paragraph), §XIII “Limitations” (RSD subsection)  
- **Problem:** You substantially elaborated the qualitative RSD discussion but still do not perform the simple quantitative test requested: perturb galaxy line‑of‑sight positions by ±σ\_v/(aH) and recompute void memberships and f\_CW to show that ∆f\_CW shifts are below your sensitivity. Instead you restate the heuristic that σ\_v/(aH) ≲ 5–8 Mpc/h is small compared to void radii and infer “essentially RSD‑immune.” That is not a substitute for an actual numerical test.  
- **Required fix:**  
  - Implement a toy RSD test on the DESIVAST primary sample: shift galaxy line‑of‑sight positions by a Gaussian with σ\_v ≈ 300–400 km/s, recompute comoving positions and point‑in‑sphere memberships, and re‑measure f\_CW(void) and f\_CW(non‑void) for, e.g., ≥50 realizations.  
  - Report the distribution of ∆f\_CW(void) and ∆f\_CW(non‑void) across these realizations. If the induced scatter is ≪ 0.0007, you can then honestly claim RSD‑induced contamination is sub‑dominant to your statistical and monopole floors.  

P5-M8 (MAJOR) – Abstract and body still label DESI‑VAST as “peer‑reviewed, standardized” in a way that overstates its status at submission time  
- **Location:** Abstract (“DESIVAST… publicly released, peer‑reviewed DR1 BGS void catalog”), §V B (Primary path description), §VIII opening paragraph, Ref.   
- **Problem:** DESI‑VAST is arXiv:2411.00148 and accepted to ApJ, but at the time frame implied by your own references (mid‑2026), ApJ volume 982, 38 may still be “in press” rather than fully published, and DR1 is very recent. The text still reads as if DESI‑VAST is an established, collaboration‑standard VAC whose methodology need not be summarized. You have added some detail, but the language “standardized across the DESI collaboration” and “peer‑reviewed DR1 BGS void catalog” still over‑asserts its maturity.  
- **Required fix:**  
  - In §V B and §VIII, explicitly state DESI‑VAST’s status as “accepted to ApJ, in press” (or whatever is current at submission) rather than using a future‑dated volume/page, and remove “standardized across the collaboration” unless this is backed by a formal DESI VAC policy you can cite.  
  - In the main text, briefly characterize key DESI‑VAST choices (volume limits, magnitude cuts, void‑finder configuration) so that a reader does not have to treat it as a black box, even if they can look up the arXiv paper.  

P5-M9 (MAJOR) – Shamir (2022) comparison remains over‑assertive and under‑quantified  
- **Location:** §XII C, Abstract “Robustness” block (indirectly), Conclusions §XV  
- **Problem:** Your revised text still claims that the environment‑conditional ranges and sweep “leave no room for a residual environment‑dependent chirality of the Shamir 2022 amplitude,” without a quantitative like‑for‑like comparison:  
  - Shamir (2022) reports a sky‑dipole amplitude of order 2–4% in imaging asymmetry for a different classifier and catalog;  
  - You quote inter‑class ranges of 0.22–1.98 pp and a monopole of ≈0.26–0.28 pp, but you never propagate uncertainties to show that a 2–4% *sky dipole* cannot be realized as some combination of environment‑conditional and survey‑geometry effects in your sample.  
- **Required fix:**  
  - Replace “leaves no room” with a quantitative comparison: e.g., “our environment‑conditional differences are ≤0.22 pp in the Phase‑2 sweep and 1.98 pp across canonical V‑Web classes, an order of magnitude smaller than the 2–4% sky‑dipole amplitude reported by Shamir (2022), but given different catalogs, classifiers, and systematics we cannot claim to exclude Shamir’s result.”  
  - Explicitly quote Shamir’s key numbers (dipole amplitude and reported p‑value) and explain why your test (environment‑conditional with DESI‑matched spirals) is not a direct replication.  

P5-m4 (MINOR) – Remaining jargon and informal language in methods and “reproducibility checklist”  
- **Location:** §V B (“garden‑of‑forking‑paths”, “headline path”), §VIII F (“cleanest formulation”), “REPRODUCIBILITY CHECKLIST” at end, scattered throughout  
- **Problem:** Despite some streamlining, there is still substantial internal jargon and informal language: “headline path,” “load‑bearing,” “garden‑of‑forking‑paths,” “spec,” “null is not positive evidence,” etc. The “reproducibility checklist” reads like a lab‑note rather than a PRD‑style data‑availability statement, and still lacks a concrete DOI/URL for the “companion data repository.”  
- **Required fix:**  
  - Replace internal shorthand with standard statistical terminology (“primary analysis,” “secondary diagnostics,” “multiple comparison corrections,” “global mean bias”).  
  - Convert the “reproducibility checklist” into a formal Data and Code Availability section summarizing: (i) where the catalog is hosted (HuggingFace ID already given), (ii) where the analysis code and configs will be permanently archived (name the repository and DOI), and (iii) what version tags reproduce the current manuscript.  

P5-n3 (NIT) – Inconsistent reported sample sizes and labels between text and tables  
- **Location:** Abstract (791,635 DR1 matched spirals), §III D, §VIII F (812,793 env‑labeled spirals), §X (N\_overlap = 25,186), various table captions  
- **Problem:** Several counts are close but not identical, and the relationships among them are not always clear:  
  - Abstract: “the 791,635 chirality‑relevant subsample”; §VIII F: “812,793 env‑labeled spirals — the 21,158‑row excess (2.7%) over the 791,635‑spiral headline subsample….” But earlier, the matched chirality‑relevant sample was 791,635 total; it is not explicit where the extra 21,158 come from (relaxed env‑label quality cuts).  
  - Table VII and Table VIII use nlz = 678,945 as the z ≤ 0.24 matched sample; this is never clearly connected to the 791,635 and 812,793 counts used elsewhere.  
- **Required fix:**  
  - Add a small table or paragraph early in §III that defines *all* key sample sizes and how they relate (full chirality catalog; DESI DR1 parent; matched primary; chirality‑relevant; env‑labeled with strict cut; env‑labeled with relaxed cut; z ≤ 0.24 subset; DESIVAST void subset).  
  - Ensure that every time you reuse a number in text or tables, it refers to exactly one of these well‑defined samples, and cross‑refer to the definition.  

If all of these issues are addressed carefully—and in conjunction with the earlier P5‑E/M/m findings—the manuscript will be substantially closer to PRD’s standards of numerical rigor, clarity about nulls and σ, and faithful abstracting of the actual support provided by the body.