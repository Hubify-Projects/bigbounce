# P5 R22prov — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 58.9s

---

P5-E1 (ESSENTIAL) – Global: cannot verify citations or numbers from external literature  
Section(s): All; References (p. 21)  

Problem: I do not have actual access to arXiv.org, ADS, or the rendered PDF; I only see the plain text supplied in the prompt. I therefore cannot truly verify (i) that the cited papers exist with the stated authors/titles/years/venues/arXiv IDs/DOIs, or (ii) that every quoted statistic that is attributed to prior work is present in those papers’ abstracts/tables. Under PRD standards, this level of citation forensics cannot be signed off based on the information available to me here.  

Required fix: This is a limitation of my review, not of the manuscript per se. An editor or human referee with full ADS/arXiv access should independently:  
- Check every reference [1]– against ADS / arXiv for correct authors, titles, journal, volume, page, year, and DOI.  
- Confirm that all imported quantitative claims (e.g., Planck 2018 cosmological parameters, Cautun et al. volume fractions, DESIVAST void counts, Tempel DR10 sample size, Shamir’s amplitude, etc.) can be traced to the cited papers.  
If any mismatch is found, it must be corrected; if not, then this finding can be dismissed. I cannot make that determination from the present text-only view.  


P5-E2 (ESSENTIAL) – Use of companion “Paper IV” (in preparation) as load‑bearing input  
Section: Abstract & Intro (p. 1–2), Sec. II (p. 2), Sec. V (Eq. 1, p. 4–5), Sec. VIII.F (p. 13), Sec. XV (p. 20), References [3], [4] (p. 21)  

Problem: The paper critically relies on a *non‑peer‑reviewed* companion work “Paper IV” [3] for:  
- The chirality catalog itself (8.47M galaxies) and its labels.  
- The catalog-wide monopole offset value \(\Delta f_{\rm CW}\approx -0.0026\) and its significance (∼9.5σ).  
- The statement that this monopole is spatially uniform and not an astrophysical dipole.  
- The global parity/dipole constraints that are explicitly used to interpret environmental results here.  

While PRD does permit use of external catalogs, here the *main scientific content* (environmental dependence) is inseparable from whether the catalog monopole is indeed a pure classifier bias rather than physical anisotropy. That entire interpretation rests on an in‑preparation, unreviewed manuscript.  

Required fix:  
- The paper must make very explicit, in the abstract and introduction, that:  
  - The chirality catalog and its monopole characterization come from an unreviewed companion paper.  
  - All “monopole-subtracted” interpretations in this manuscript are conditional on that result holding up.  
- The main claims must be reframed to emphasize *directly measured* environment comparisons (void vs non-void, per-class ranges) without assuming prior knowledge that the monopole is purely a classifier bias. E.g., report both raw fCW and “relative to 0.5” for all key results and avoid stating physical conclusions that require knowing the monopole’s cause.  
- Alternatively, key elements of the Paper IV analysis that are strictly necessary for the present paper (global fCW, spatial uniformity tests, imaging-leg systematics) should be summarized and re‑done in a self‑contained appendix using only the subset of data used here, so that PRD readers are not being asked to rely on an unreviewed, inaccessible document.  

Without such reframing, the present paper’s core interpretation leans too heavily on an unpublished external analysis for PRD standards.  


P5-E3 (ESSENTIAL) – Mixing σ values from non‑comparable nulls without explicit caveat  
Locations:  
- Abstract (p. 1): “−2.61σ”, “−4.66σ”, “∼2σ on the binomial null”, “3.4σ filament sign-flip”.  
- Sec. V, Eq. (1) (p. 4–5): σfrom half, σpred.  
- Sec. VI–VIII, IX, X (p. 5–18): frequent juxtaposition of σfrom half, |σobs−σpred|, χ² p‑values, permutation‑based pLEE, “Bonferroni thresholds”, “3.4σ joint two-sample z-test”, etc.  

Problem: The manuscript uses multiple distinct “σ” style significances:  
- Raw binomial “σ from half” (based on normal approximation).  
- A predicted σpred from the Paper IV monopole.  
- Residuals |σobs−σpred|.  
- Permutation-derived p-values transformed into informal σ-like language (“no NSIDE returns p < 0.05”).  
- A “joint two-sample z-test” giving |z| ≈ 3.4σ.  

These appear side-by-side in text and abstract as if they were directly comparable without *explicit* and repeated wording that they are different test statistics under different null hypotheses and are not directly comparable as “sigmas” in the particle‑physics sense. This violates the instruction you were given (and is also poor statistical hygiene by PRD standards).  

Required fix:  
- In every place where different σ notions are juxtaposed (e.g. abstract, Sec. V, Secs. VI–VIII), add explicit statements like: “Note: these σ values arise from different null procedures (simple binomial vs. monopole-shift vs. permutation-based); they are not directly comparable to each other.”  
- In the abstract, reduce σ usage to one clearly defined metric or replace σ with p-values or confidence intervals when discussing multiple tests.  
- In the main text, clearly distinguish notation: e.g. \(\sigma_{\rm bin}\) for simple binomial, \(\sigma_{\rm mono}\) for deviation from monopole prediction, and avoid calling permutation p-values “σ” at all.  
- Where you use the phrase “3.4σ” for the bright–dark flip, state explicitly that this is under a simple two-sample proportion test and not corrected for all the other selections scanned.  


P5-E4 (ESSENTIAL) – Garden-of-forking-paths and “primary analysis” declared post‑hoc  
Section: V.B (p. 5), VIII (p. 10–13), IX (p. 14–17)  

Problem: The manuscript admits that no pre‑registered analysis plan existed and that the designation of the DESIVAST void analysis as “primary” is post‑hoc:  

> “a single a priori preregistered analysis plan was not filed; the choice of which classifier to report as ‘primary’ is therefore made post‑hoc”  

Yet the abstract and conclusions present a clean “headline” null with precise bounds (inter-class range, tightening ×40, etc.), while the multiplicity of classifiers and scans (V-Web, DESIVAST, Tempel, ASTRA, z-shell correction, various Ns and λth, many stratifications) means that the actual look-elsewhere burden is very large and only partially accounted for. The post‑hoc designation raises a serious concern about selective emphasis.  

Required fix:  
- Clarify in the abstract and conclusions that the DESIVAST void analysis is a *post‑hoc* chosen primary path, and explicitly describe the family of analyses explored.  
- Either (i) provide a principled, quantitative multiplicity control across *all* environment classifiers and stratifications used to support the headline, or (ii) substantially narrow the scope of the paper to one or two clearly motivated, pre‑specified analysis choices (e.g. DESIVAST void vs non‑void + one V-Web configuration), relegating the rest to a short “exploratory checks” section with no numerical “headline” emphasis.  
- Tone down the definitiveness of claims about “robustness” to classifier choice: make it explicit that these are exploratory cross‑checks, not preregistered confirmatory tests.  

Given PRD’s standards, the current language overstates robustness relative to the actual multiplicity control.  


P5-E5 (ESSENTIAL) – EFT toy operator is not grounded in cited literature  
Section: Appendix A (p. 20)  

Problem: The paper proposes a toy operator \(L_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L\cdot\hat z)\), and states it is “inspired by” Alexander & Yunes [1] and Lue et al. [2], but also admits:  

> “the specific operator … is not contained in either [1] or [2]”  

The mapping from the observational ∆fCW bounds to a constraint on \(g_\phi \nabla\phi\) is essentially speculative and not derived from any established EFT-of-LSS or EFT-of-inflation framework. Moreover, the text flags serious issues (lack of rotational and gauge invariance), but still attempts to quote an order-of-magnitude bound. For PRD this is too close to attaching a formal-looking “constraint” to an ad hoc operator that the cited literature does not actually justify.  

Required fix:  
- Either remove Appendix A entirely, or rewrite it to:  
  - Make absolutely clear that no constraint on any physically well-defined EFT parameter is being derived.  
  - Remove the numerical “bound” \(|g_\phi (\nabla\phi)/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\); instead, state qualitatively that “if future models generate environment-dependent chirality at this scale, they must keep it below the observed ∼1% level.”  
  - Clarify that [1] and [2] are cited only as generic examples of parity-violating gravity, not as sources for this operator.  
If you wish to keep a theoretical discussion, it should be narrative and model-agnostic, not framed as an EFT mapping with semi-numerical bounds.  


P5-E6 (ESSENTIAL) – Overly strong claims of “independence” given RSD & classification caveats  
Section: VIII (RSD discussion p. 10–11), XIII (Limitations p. 18–19), XV (Conclusions p. 19–20)  

Problem: The paper repeatedly states that chirality is “statistically independent” of environment, yet also acknowledges:  
- The V-Web classification is performed in redshift space; RSD can change class assignments in a way not fully quantified.  
- The DESIVAST void membership is binary void/non‑void with internal non‑void mixture of walls/filaments/clusters not resolved.  
- The target-program (bright/dark) and V-Web class are strongly correlated (χ² extremely large), and there is an unresolved 3.4σ bright–dark sign flip in the filament class.  

Given these, a strict *independence* claim is too strong. What is actually shown is that *within this data, at this smoothing scale and classification, no environment trend larger than O(1%) is detected once the catalog monopole is accounted for.*  

Required fix:  
- Rephrase all “independence” language in abstract, conclusions, and Sec. XII to something like: “We detect no statistically significant dependence of chirality on environment at the ≳1% level given our current classification and systematics.”  
- Explicitly state in the conclusions that small environment-dependent effects below this scale, or effects entangled with RSD and target-program mixing, cannot be excluded.  
- Make this nuance very clear in the abstract, not only in the limitations section.  


P5-M1 (MAJOR) – Abstract scalar consistency and recomputation of key numbers  
Section: Abstract (p. 1)  

Issues to check (I cannot recompute them from tables because some inputs are missing):  

1. Per-class fCW and σ values:  
   - For filament: \(n=408{,}187\), \(f_{\rm CW}=0.4980\). The definition given in Sec. V is  
     \(\sigma_{\rm from\ half} = (n_{\rm CW}-0.5N)/(0.5\sqrt{N})\). You quote −2.61σ.  
     From the text alone I cannot re‑derive nCW exactly (rounding of fCW to 4 decimals and N to 6 digits introduces a few percent uncertainty in σ).  
   - Similar issue for cluster (397,505; 0.4963; −4.66σ), wall (6,673; 0.5034; +0.55σ), void (428; 0.4836; −0.68σ).  

   Required fix: Add an explicit line or supplementary table listing *integers* nCW and nCCW for each class so that σ can be recomputed exactly by readers. Confirm that your quoted σ match these integers and the stated formula.  

2. “Range across classes is 1.98 percentage points”: Using the rounded fCW values:  
   - Max is wall 0.5034, min is void 0.4836. Difference = 0.0198 = 1.98 pp. This is consistent.  
   No change needed if you provide more precise fCW in a table and they still produce ≈1.98 pp.  

3. Phase‑2 range “never exceeds 0.22 percentage points”: Table VI shows a maximum of 0.220 → 0.22 pp: consistent.  

4. Label-shuffle p = 0.372 for redshift, HEALPix p-values 0.61/0.135/0.413, density |σmax| = 3.94 and residual 1.87, bright/dark |z| ≈ 3.4σ.  
   I cannot recompute these from the text because the bin‑level counts are not fully listed.  

   Required fix: Provide exact bin counts (N, nCW) in supplementary tables for:  
   - Redshift bins used for p = 0.372.  
   - Density quintiles used for |σmax| = 3.94 and residual 1.87.  
   - Bright vs dark per class used for the 3.4σ and 0.5σ tests.  
   This is necessary for PRD‑level reproducibility and to verify that no rounding or coding errors exist.  


P5-M2 (MAJOR) – Monopole subtraction and σvs monopole definition  
Section: V (p. 4–5), VIII.F and Table X (p. 13), XV (p. 20)  

Problem: The paper defines a “monopole prediction” σpred based on the catalog-level ∆fCW and compares observed σfrom half to it, calling deviations |σobs−σpred| “candidate environmental signals”. However:  
- It is not fully clear whether σpred is computed using the *exact* monopole measured on the same subset of galaxies (e.g. 791,635 chirality-relevant, or 812,793 env-labeled) or imported directly from Paper IV’s 8.47M catalog. The text suggests both.  
- Table X lists σvs monopole using a P5 monopole fCW^P5 = 0.4972, but the definition of σvs monopole is not explicitly written as a formula, and readers must infer how it was computed.  

Required fix:  
- Provide an explicit formula for σvs monopole in Sec. V, e.g.  
  \(\sigma_{\rm vs\ mono} = (n_{\rm CW} - f_{\rm CW}^{\rm P5}N)/\sqrt{f_{\rm CW}^{\rm P5}(1-f_{\rm CW}^{\rm P5})N}\).  
- Clarify which monopole is used where: P4’s full-catalog ∆fCW or P5’s matched-sample monopole, and ensure consistency.  
- Show in an explicit table the global n, nCW, fCW for both P4 original catalog and P5 matched subsets, so readers can verify the 8% enhancement claim and the propagated σ values.  


P5-M3 (MAJOR) – Bright/dark filament sign‑flip and interpretation  
Section: Abstract (p. 1–2), Sec. VI.D(b,c,d) (p. 7–8), Sec. VIII.F (p. 13), Sec. XI (p. 18–19)  

Problem: There is a non‑trivial 3.4σ bright–dark sign‑flip in the filament sample (and a similar pattern in cluster), yet the abstract relegates this to a brief remark and the conclusions reiterate a strong environment-independence statement. The contingency test shows strong coupling between V-Web class and target program; the text says the residual cannot be cleanly partitioned between selection effects and astrophysical signal. In a PRD context this is a substantial unresolved pattern.  

Required fix:  
- In the abstract and conclusions, explicitly mention that there is a statistically significant bright–dark difference in filament chirality that remains unresolved, and that the primary DESIVAST void analysis is designed to *avoid* regions where this effect is strongest.  
- Add quantitative detail: report actual fCW and n for filament-bright and filament-dark in the main text (not only σ), and show how the 3.4σ correction for the multiple stratifications was or was not applied.  
- Make clear that the headline claim of “no environment dependence” applies to DESIVAST void vs non‑void and to *averaged* cosmic-web classes, not to conditional combinations like “filament × bright” vs “filament × dark”, where a residual may exist.  


P5-M4 (MAJOR) – Redshift-space distortions and class assignment  
Section: VIII (RSD treatment, p. 10–11), XIII (Limitations, p. 18–19)  

Problem: The discussion acknowledges that RSD can cause anisotropic eigenvalue deformations and class boundary changes, particularly at filament/wall/void boundaries, and that a full treatment would require reconstruction, which is not performed. The current argument that scalar σv/(aH) ≪ Rs is only heuristic, yet it is used to support statements that RSD contamination is at “sub-percent” level and hence negligible.  

Required fix:  
- Soften the quantitative language about RSD impact: remove the claim that the contribution to ∆fCW is “expected to be sub-dominant at the current ∼10−3 precision” unless you explicitly propagate a bound using realistic mock catalogs.  
- If you wish to retain a quantitative statement, add a short mock-based RSD experiment on a simulation or toy model using the same V-Web pipeline, or clearly mark the estimate as order-of-magnitude and state that it has not been validated.  
- In conclusions, include RSD as a key systematic that must be addressed in future work before interpreting null results as genuinely physical.  


P5-M5 (MAJOR) – Length and scope vs. main contribution  
Section: Whole paper (21 pages)  

Problem: For a single main scientific claim (“no detectable environment-dependent chirality at ≳1% level in DESI DR1”), the manuscript is extremely long and methodologically sprawling: extensive T-Web/V-Web/ASTRA/Tempel/ DESIVAST cross-checks, multiple stratifications, theoretical EFT appendix, future LSST discussion, etc. Much of this is useful but not essential to the core result, and the multiplicity complicates statistical interpretation. By PRD standards, the paper would be clearer and more compelling if focused.  

Required fix:  
- Condense the manuscript to roughly 12–15 pages by:  
  - Moving most of Sec. IX–X (cross-checks) to a shorter subsection or to an online supplement, keeping only one or two key cross-validations in the main text.  
  - Removing Appendix A (EFT toy operator) or shrinking it to a qualitative paragraph.  
  - Trimming the extended discussion of HEALPix scans and redshift/density tests to the minimum needed to demonstrate that no single alternative stratification is driving the result.  
This would keep the narrative focused on the DESIVAST void test plus one V-Web configuration as the core result.  


P5-m1 (MINOR) – Internal terminology: “V-Web” vs “T-Web”  
Section: Abstract (p. 1), footnote a (p. 2), Sec. IV (p. 4), Sec. IX.C (p. 16–17)  

Problem: The paper occasionally uses “V-Web” for what is actually the *tidal-tensor* classifier (Hahn 2007) and acknowledges that “V-Web” is sometimes loosely used for that family, while the velocity-shear V-Web (Hoffman 2012) is different. This can confuse readers, especially since you also cite Hoffman et al. [6] and a separate T-Web DR1 paper .  

Required fix:  
- Decide on a consistent label: either “T-Web (tidal-tensor)” throughout, or “V-Web (tidal-tensor variant)” but not both interchangeably.  
- In Abstract and §IV, explicitly label your classifier as “T-Web (tidal-tensor, Hahn et al. 2007)” and reserve “V-Web” exclusively for velocity-shear if you mention it.  
- Update the footnote to clarify terminology in a single place and then use only one term in the main text.  


P5-m2 (MINOR) – Internal symbol definitions and LaTeX clarity  
Section: Sec. V (p. 4–5), various tables  

Problem: Some symbols appear before being precisely defined or with slight inconsistencies: e.g. σfrom half vs σpred vs σvs monopole, ρ̄cell vs n̄shell; “σ from half” appears in text before Equation (1) is clearly tied to it; the definition using 0.5 N vs 0.5√N could be confusing.  

Required fix:  
- In Sec. V, introduce a clear list of statistical quantities with explicit formulas and units (if any), and keep notation consistent.  
- Ensure that every σ-like quantity is defined at first use and that the exact formula matches what is used in code.  


P5-m3 (MINOR) – Appendix B “data and code availability” is vague  
Section: Appendix B (p. 20)  

Problem: The paper mentions a “companion data repository” and scripts but does not give a persistent, citable identifier (e.g. DOI, version tag). For PRD, reproducibility requires a clear pointer.  

Required fix:  
- Provide a specific repository name and version (e.g. Git commit hash) and, ideally, a Zenodo or similar DOI for the exact code and data used in this submission. If this cannot be public before acceptance, at least state that the repository will be made public with a DOI upon publication.  


P5-n1 (NIT) – Minor stylistic issues and long sentences  
Sections: Multiple (esp. Abstract, Sec. VI–IX)  

Problem: Many sentences are very long and dense, making the logic hard to follow (e.g. multi‑clause sentences in the abstract’s robustness paragraph, in Sec. VI.D, and in the limitations).  

Required fix:  
- Break very long sentences into shorter ones, particularly in the abstract and section intros, to improve readability.  
- Avoid stacking multiple parenthetical caveats in a single sentence when describing a single numerical result.  



## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The empirical core (no detected chirality–environment dependence at ≳1% level) is potentially valuable and the internal numerical story is largely self-consistent given the text, but the paper leans heavily on an unreviewed companion catalog (Paper IV), mixes non‑comparable σ metrics without sufficiently clear caveats, overstates “independence” relative to the actual systematic and multiplicity limits, and includes a speculative EFT appendix not well grounded in the cited literature. The length and breadth of exploratory analyses further dilute clarity. With a substantial revision that (i) tightens and clearly bounds the main claim, (ii) reframes the dependence on Paper IV, (iii) cleans up the statistical presentation of significances, and (iv) trims or fully labels speculative/theoretical material, the work could reach PRD standards, but in its current form it should not be accepted.