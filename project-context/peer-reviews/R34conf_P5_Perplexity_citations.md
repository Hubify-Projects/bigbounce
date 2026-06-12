# P5 R34conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.66.pdf` md5=46f419a3 pages=31
**Input format**: TEXT + web search + pass-2 self-critique (14252 chars)
**Wall time**: 69.5s

---

I cannot complete the requested **forensic verification against arXiv/ADS and the rendered PDF** because I do not actually have live web-search access in this environment, and the prompt provides only the manuscript text, not the external citation metadata needed to verify every reference. I can still give a **paper-text audit** of internal consistency, arithmetic, and bibliography risks based on the text you supplied.

The manuscript is **not PRD-ready as written**: it contains multiple internal inconsistencies, stale draft remnants, contradictory sample definitions, and several statistically overclaimed or underqualified comparisons that would require revision before acceptance.

- **P5-E1** — **Abstract / p. 1**  
  **Problem:** The abstract says the “headline result” is based on the DESIVAST-anchored void cross-check and also on the V-Web four-class analysis, but the paper later demotes the V-Web path to a secondary diagnostic and says the primary analysis is the DESIVAST void-vs-non-void contrast. The abstract’s ordering is stronger and less qualified than the body.  
  **Fix:** Rewrite the abstract so the primary statistic is the DESIVAST void-vs-non-void contrast, and explicitly label V-Web as secondary/diagnostic.

- **P5-E2** — **Abstract / p. 1**  
  **Problem:** The abstract states “no environment dependence beyond” the catalog monopole and counting floor, but the body repeatedly notes residual structures at the \(\sim 2\sigma\) level in tracer-program splits and several secondary scans. Those are later argued to be systematics, not environment, but they are still nontrivial residuals.  
  **Fix:** Add the caveat that secondary residuals exist and are interpreted as selection-function/systematic structure rather than environment dependence.

- **P5-E3** — **Introduction / p. 2**  
  **Problem:** “Paper IV [3] … currently in preparation and not yet peer-reviewed” is cited as a load-bearing input while also serving as the source of key numerical claims. This is a self-inconsistent provenance chain for a result that depends on the unpublished companion.  
  **Fix:** Either make the paper self-contained without relying on unpublished results, or move those inputs to a fully archived, citable release with frozen versioning.

- **P5-M1** — **Introduction / p. 2**  
  **Problem:** The paper states Paper IV “establishes the global mixture … as a CW fraction of 0.4974±0.000279 — a −0.26 pp monopole offset … statistically significant in pure counting terms (≈9σ)” and later uses both 0.4974 and 0.4972 as “monopole” references. The paper does not cleanly distinguish the 0.4974 Paper IV value from the 0.49719 matched-sample value.  
  **Fix:** Separate the two references everywhere and standardize the notation; one is the Paper IV catalog monopole and the other is the matched-sample monopole.

- **P5-M2** — **Section II / p. 3**  
  **Problem:** The text says Paper IV’s “real-space full-sky dipole null at +0.43σ (p = 0.30)” and also that an “earlier harmonic-space subsample-mask MASTER-deconvolved \(\ell=1\) statistic was withdrawn.” This is history-of-analysis material that reads like internal audit prose.  
  **Fix:** Remove the draft-history narrative or isolate it in a reproducibility note; it should not appear in the main argument.

- **P5-M3** — **Section III.B / p. 3**  
  **Problem:** The DR1 selection is described as “ZWARN==0, SPECTYPE ∈ {GALAXY, QSO}, and 0.01 ≤ z ≤ 4,” yielding 16,361,731 rows, but elsewhere the “DR1 input rows” are described as “ZWARN=0 input rows” without repeating the QSO inclusion caveat.  
  **Fix:** Use one consistent definition of the parent DR1 input sample throughout.

- **P5-M4** — **Section III.C / p. 3**  
  **Problem:** “Duplicates on the chirality side are resolved by nearest-separation winner; after this dedup the chirality-relevant subsample carries one row per DESI TARGETID (791,635 unique TARGETIDs — no many-to-one matches survive the join).” Later, the environment join is said to produce repeated rows per coadd entry. These two deduplication conventions are easy to conflate.  
  **Fix:** State explicitly, at first mention, which tables are one-row-per-TARGETID and which are row-per-coadd.

- **P5-M5** — **Section IV.A / p. 4**  
  **Problem:** The text says “V-Web” names a T-Web implementation while “T-Web” refers to external implementations “e.g. the concurrent DR1 analysis of Ref. .” That is terminology-confusing and nonstandard.  
  **Fix:** Define the classifier labels once and use them consistently; do not repurpose V-Web/T-Web ambiguously.

- **P5-M6** — **Section IV.A, step 9 / p. 4**  
  **Problem:** The sign convention for the tidal tensor is overexplained and potentially self-contradictory: \(\Phi(k)=-\delta_k/k^2\), then \(T_{ij}(k)=-k_i k_j \Phi(k)\), then “this gives \(T_{ij}(k)=+k_i k_j\delta_k/k^2\).” This is fine algebraically, but the manuscript treats the sign choice as if it were a validation result.  
  **Fix:** Keep the convention, but remove the self-congratulatory “matching the title-footnote convention” claim; simply state the adopted convention.

- **P5-M7** — **Section V / p. 5**  
  **Problem:** The manuscript defines \(\sigma_{\rm pred}\) using the Paper IV monopole and then elsewhere uses the matched-sample monopole \(f_{\rm CW}^{P5}\). The distinction is important because the two are not numerically identical.  
  **Fix:** Introduce a table of symbols and enforce strict usage of \(\sigma_{\rm pred}^{P4}\) versus \(\sigma_{\rm pred}^{P5}\).

- **P5-M8** — **Section V.A / p. 5**  
  **Problem:** The claim that the label-shuffle and position-shuffle nulls are “the same permutation null” is only true for the particular per-bin count statistic, not generally.  
  **Fix:** Add the restriction “for the per-bin count statistics used here” directly in the claim and avoid generalized wording.

- **P5-M9** — **Section V.B / p. 6**  
  **Problem:** “The choice of which classifier to report as primary is therefore made post hoc” is an admission of garden-of-forking-paths concerns. That is fine as transparency, but it undermines the evidentiary hierarchy unless the primary estimator was specified before examining outcomes.  
  **Fix:** Either pre-register the primary endpoint in a revision or explicitly downgrade the primary/secondary language as retrospective.

- **P5-M10** — **Table II / p. 7**  
  **Problem:** The primary family is labeled “Bonferroni-5,” but the table lists the V2-REVOLVER and V2-VIDE catalog-native contrasts as primary, while the body elsewhere says the primary result is the DESIVAST-anchored void-vs-non-void contrast.  
  **Fix:** Make Table II match the prose exactly, or revise the prose. Right now the paper’s primary endpoint is not stable across sections.

- **P5-M11** — **Section VI.A / p. 7**  
  **Problem:** The manuscript says the void bin is sample-size limited and “survey-edge artifact dominated,” but the environment conclusion is then stated as a general null for the full V-Web analysis. That overstates what the V-Web void class can support.  
  **Fix:** Narrow the claim: the V-Web void class is not decisive; the null is supported by the DESIVAST primary analysis and the V-Web secondary analyses collectively.

- **P5-M12** — **Section VI.A / p. 7**  
  **Problem:** The phrase “the quoted \(\sigma\)from half values scale as \(n\) at fixed fractional offset” is mathematically incorrect as written; the scaling is \(\propto \sqrt{n}\), not \(n\).  
  **Fix:** Correct the sentence to say \(\sigma_{\rm from\,half}\propto \sqrt{n}\) at fixed fractional offset.

- **P5-E4** — **Section VI.B / p. 8**  
  **Problem:** “A logistic regression of the CW indicator on {z, |sin δ|, cos α, confidence} gives a z-coefficient …” is presented without effect size interpretation.  
  **Fix:** Report the corresponding odds ratio and practical significance, not just the coefficient and p-value.

- **P5-M13** — **Section VI.C / p. 9**  
  **Problem:** The paper claims the \(k=5\) density proxy is “mildly endogenous” and then uses it anyway, but does not clearly separate the endogenous and exogenous versions in the main figure caption.  
  **Fix:** Explicitly label which density proxy is endogenous and which is exogenous in Fig. 5 and Table IV.

- **P5-M14** — **Section VI.C / p. 9–10**  
  **Problem:** The text says “no quintile deviates from the prediction by more than \(\sim 2\sigma\),” but Table IV contains a residual of 1.87 and another of 1.01. This is consistent, but the paper should state the maximum residual numerically and not “\(\sim 2\sigma\).”  
  **Fix:** Replace qualitative language with the exact maximum residual and the corresponding bin.

- **P5-M15** — **Section VI.D / p. 11**  
  **Problem:** The bright/dark split is described as approximate because rows are not disjoint, but the paper still quotes a two-sample z-value as if it were inferentially meaningful.  
  **Fix:** Demote this to a descriptive diagnostic unless the overlap-free unique-targetid version is used consistently.

- **P5-M16** — **Section VI.D / p. 11**  
  **Problem:** “Earlier draft quoted filament bright/dark n of 416,701/21,203 with a 3.4σ two-sample split; those values were computed on an unfiltered nearest-label join … and are withdrawn.” This is internal-draft history in the body.  
  **Fix:** Remove the withdrawn-draft narrative from the main text or quarantine it in a changelog, not the manuscript.

- **P5-M17** — **Section VI.E / p. 12**  
  **Problem:** Table VI reports p-values for NSIDE 16, 32, 64, but the body also states stratified re-draws and stream-to-stream fluctuations. The paper does not clearly say whether the reported p-values are from the same RNG stream as the main analysis or a different one.  
  **Fix:** Specify the exact RNG stream provenance for each p-value family and note whether results are stable to stream choice.

- **P5-M18** — **Section VII / p. 13–14**  
  **Problem:** The manuscript says the Rs = 10 Mpc/h cells are retained “for completeness only” because they are below the 25.9 Mpc/h grid scale, but they still appear in the main sweep table and influence the max statistic.  
  **Fix:** Either remove them from the main robustness table or clearly separate “reported for completeness” from the claim-bearing resolved subset.

- **P5-M19** — **Section VII.A / p. 14**  
  **Problem:** The phrase “the empirical max-stat permutation null is therefore consistent with the parametric reading” is fine, but the manuscript then treats the descriptive range-floor comparison as if it were inferential.  
  **Fix:** Keep the permutation p-value as the inferential statement and explicitly label the range-floor comparison as descriptive only.

- **P5-M20** — **Section VIII.A / p. 15–16**  
  **Problem:** The DESIVAST cross-match uses both an approximate k=20 KDTree query and an “exact rerun,” with the result changing from 56,981 to 57,081 void galaxies. The paper treats this as negligible, but the change is not negligible in a methodological audit.  
  **Fix:** Present the exact rerun as the canonical result and relegate the approximate version to a sensitivity check.

- **P5-M21** — **Section VIII.A / p. 16**  
  **Problem:** “0/6 disagreement … 0% concordance” is too strong for a six-object example. The text itself admits the sample is too small for formal purity constraints.  
  **Fix:** State this only as an illustrative sanity check, not as a purity statement.

- **P5-M22** — **Section VIII.B / p. 17**  
  **Problem:** The DESIVAST primary result is repeatedly stated as “clean null,” but the void class itself has \(f_{\rm CW}=0.4964\), which is not parity exactly and is only null after considering sampling error.  
  **Fix:** Use “consistent with null” or “statistically indistinguishable from null,” not “clean null” without qualification.

- **P5-M23** — **Section VIII.C / p. 18**  
  **Problem:** The catalog-native V2-REVOLVER and V2-VIDE counts in Table X differ from the earlier prose values in a way that requires care. The text says one earlier draft had values 86,276/64,514 and that these were due to a defect, but the corrected counts are 104,912 and 74,111; the paper should show the corrected counts are the final canonical numbers everywhere, including captions.  
  **Fix:** Normalize all captions and prose to the corrected catalog-native counts only.

- **P5-M24** — **Section VIII.D / p. 18–19**  
  **Problem:** The footprint-mask retabulation says “all 57,081 exact-membership void spirals fall inside the footprint,” yet immediately afterward it discusses a non-void control restricted to the same footprint and an outside-footprint residual. The logic is easy to misread.  
  **Fix:** Add a short schematic sentence clarifying that only the non-void sample has an outside-footprint complement in that retabulation.

- **P5-M25** — **Section VIII.E / p. 19**  
  **Problem:** The manuscript describes “0 maximal voids per pixel” as a proxy for being outside coverage, but then says some in-coverage pixels can stochastically contain zero maximal voids. That means the class is only a proxy, not a coverage indicator.  
  **Fix:** Stop calling it a coverage region and call it a proxy bin throughout.

- **P5-M26** — **Section VIII.F / p. 20**  
  **Problem:** The formulae for subtracting the P5 matched-sample monopole are mixed with the P4 monopole language. This is a provenance ambiguity for the central effect-size claim.  
  **Fix:** Explicitly denote which monopole is being subtracted in each table and figure.

- **P5-M27** — **Section IX.A / p. 21–23**  
  **Problem:** The “selection-corrected classifier” rebuild changes the class populations dramatically, but the paper then says this “strengthens” the null. That may be true, but it also indicates the classifier is not stable to the correction.  
  **Fix:** Treat the selection-corrected build as a stress test, not as strengthening evidence; emphasize that the canonical result is the primary one.

- **P5-M28** — **Section IX.A / p. 23**  
  **Problem:** The sentence “the corrected class volume fractions and spatial coherence remain cosmologically plausible” is vague and unquantified.  
  **Fix:** Either supply a quantitative criterion or remove the statement.

- **P5-M29** — **Section IX.B / p. 23–24**  
  **Problem:** The Tempel FoF mapping from multiplicity bins to V-Web classes is ad hoc and classifier-mismatched. The paper acknowledges this but still presents the comparison as validation.  
  **Fix:** Recast as a very weak consistency check, not a validation of the tidal-tensor classifier.

- **P5-M30** — **Section IX.C / p. 24–25**  
  **Problem:** The text says Ref.  is “currently in submission to MNRAS” while also citing its 2026 arXiv preprint metadata. The venue status is therefore stale/duplicative and should be cleaned up.  
  **Fix:** Use the arXiv preprint citation consistently unless a peer-reviewed venue exists.

- **P5-M31** — **Section X / p. 26**  
  **Problem:** The ASTRA overlap is heavily label-disagreeing, small, and explicitly “best read as a descriptor of consistency … not as load-bearing robustness evidence,” yet it is still counted among the paper’s headline cross-validations.  
  **Fix:** Demote ASTRA to a minor consistency check, not a robustness pillar.

- **P5-M32** — **Section XI / p. 27**  
  **Problem:** The systematics section admits an earlier statement “agreed within ±0.001” was stale. Internal-draft correction language should not appear in the body of a submitted paper.  
  **Fix:** Delete the stale-draft sentence and keep only the corrected result.

- **P5-M33** — **Section XII.C / p. 28**  
  **Problem:** The comparison to Shamir 2022 mixes amplitudes and percentages in a way that invites confusion: “2–4% large-scale asymmetry” versus “catalog-wide CW-fraction offset is −0.26%.”  
  **Fix:** Clearly distinguish the observables and their units before comparing magnitudes.

- **P5-M34** — **Section XIII / p. 28–29**  
  **Problem:** The limitations section correctly notes that the V-Web is in observed redshift space and not real space, but the main results sometimes read as if the environmental labels are physically exact.  
  **Fix:** Carry the redshift-space limitation into the abstract and conclusions more explicitly.

- **P5-M35** — **Section XIII / p. 29**  
  **Problem:** The RSD discussion ends by saying the headline null “is reported at fixed-redshift-space classification,” which is correct, but it should not be conflated with a real-space environmental null.  
  **Fix:** Clarify that the null is classification-space dependent and not a real-space theorem.

- **P5-M36** — **Appendix A / p. 29–30**  
  **Problem:** The toy EFT operator \(L_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L \cdot \hat z)\) is explicitly non-covariant and not gauge invariant. This is acceptable only as a toy model, but the presentation is too prominent for something not theoretically controlled.  
  **Fix:** Move this further into an appendix note and label it as purely heuristic.

- **P5-M37** — **Appendix B / p. 30–31**  
  **Problem:** The reproducibility section references a “versioned GitHub repository” and a DOI-minted snapshot, but no frozen DOI, commit hash, or archival identifier is actually given in the text you supplied.  
  **Fix:** Provide the exact frozen-release identifier, commit hash, and archival DOI in the paper.

- **P5-M38** — **Appendix B / p. 30–31**  
  **Problem:** The “Reproducibility checklist” mentions deterministic seed 20260515, but the body also references multiple distinct RNG streams and re-draws. The seed alone is insufficient provenance.  
  **Fix:** Record all seeds and stream derivations for every permutation family and sensitivity rerun.

- **P5-M39** — **Bibliography / refs. [3], [4]**  
  **Problem:** References [3] and [4] are explicitly “in preparation” and not peer-reviewed, yet they are used as major numerical and theoretical supports. That is not acceptable as supporting literature for a PRD claim unless the necessary data are independently archived.  
  **Fix:** Replace load-bearing use of unpublished companion papers with public, citable releases or remove the dependency.

- **P5-M40** — **Bibliography / refs. , , , **  
  **Problem:** Several citations are metadata-rich but not fully verified here; given the manuscript’s strong reliance on exact counts and publication status, these should be checked for arXiv ID, year, title, and venue consistency before submission.  
  **Fix:** Audit each citation against arXiv/ADS and correct any fused metadata or venue/date mismatches.

- **P5-N1** — **General / multiple pages**  
  **Problem:** The manuscript repeatedly uses phrases like “headline,” “clean null,” “best read as,” “load-bearing,” and “diagnostic” in a way that reads like internal review prose rather than polished journal prose.  
  **Fix:** Tighten language and remove meta-commentary.

- **P5-N2** — **General / multiple pages**  
  **Problem:** There are many explicit draft-history notes: “earlier draft,” “withdrawn,” “stale,” “pre-registration caveat,” “corrected join,” “superseded,” “legacy,” “manuscript tag,” “RNG re-draw,” and similar bookkeeping language in the body. These are not acceptable in the final manuscript body.  
  **Fix:** Move all revision history and internal audit notes to an external change log.

- **P5-N3** — **General / multiple pages**  
  **Problem:** The paper is long for the apparent contribution. Much of the length is consumed by repeated robustness checks, draft-errata discussion, and provenance narration.  
  **Fix:** For a PRD-style article, I would recommend cutting to roughly **20–25 pages** of main text, with the long provenance and sensitivity machinery moved to appendices or supplementary material.

## Summary recommendation
**MAJOR REVISIONS**

The paper has a potentially publishable null result, but the current draft is not ready for PRD because the primary endpoint shifts across sections, internal provenance is inconsistent, multiple draft-history notes remain in the body, and several quantitative claims are presented with either insufficient qualification or ambiguous denominator/convention handling. The main statistical conclusions may survive revision, but the manuscript needs substantial restructuring, de-duplication of systematics text, strict stabilization of notation and sample definitions, and removal of unpublished/load-bearing dependency chains before it can be considered for acceptance.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E5 — Abstract (first paragraph, environment‑dependence / σ claims)  
**Issue (A & E – arithmetic + null comparability):** The abstract states the V‑Web void bin has \(n=428\), “observed offset is \(-0.68\sigma_{\rm from\,half}\),” and the “counting‑statistics floor of ±4.8 pp (the 2σ binomial half‑width of the \(n=428\) V‑Web void bin).” In Table III, the void row has \(n=428\), \(f_{\rm CW}=0.4836\), \(\sigma_{\rm from\,half}=-0.68\). The implied absolute deviation from 0.5 is \(0.5-0.4836=0.0164=1.64\) pp. A binomial 1σ half‑width for \(n=428\) at \(p=0.5\) is \(\approx 0.5/\sqrt{428}=0.0242\) (2.42 pp), so 2σ ≈ 4.84 pp, which is consistent with the stated “±4.8 pp,” but that floor is the *uncertainty* on \(f\), not on the deviation. The actual deviation (1.64 pp) is **inside** the 1σ half‑width, not merely “inside the 2σ floor.” So referring to ±4.8 pp as “the floor” for that observed deviation is misleading and numerically over‑generous.  
**Fix:** Phrase it precisely: the void bin’s 95% binomial half‑width is ≈4.8 pp while the observed deviation is only 1.6 pp (≈0.68σ). Make clear that the 4.8 pp is the 2σ confidence half‑width for the *estimate*, not the magnitude of the observed offset.

P5‑E6 — Abstract (Phase‑2 p‑values vs Table VII)  
**Issue (A & B):** The abstract says “per‑cell label‑shuffle look‑elsewhere p‑values span 0.13–0.56 (no cell below 0.05).” Table VII gives \(p_{\rm LEE}\) of 0.56, 0.42, 0.38, 0.13, 0.14, 0.23, 0.34, 0.41, 0.48. The minimum is 0.13 and maximum is 0.56, so the stated 0.13–0.56 band is arithmetically correct, but the wording “per‑cell look‑elsewhere” is ambiguous: each p is corrected over *classes* within a cell, not over *cells*; only a later parenthetical notes that these are not globally corrected.  
**Fix:** In the abstract, explicitly say these p‑values are *within each four‑class family per cell* and that a separate global max‑statistic correction gives \(p_{\rm global}=0.27\)–0.36, as later in Table VII. This avoids over‑stating how aggressively LEE is treated in the headline.

P5‑M41 — Abstract / §V (σ scaling language – already fixed locally, still present globally)  
**Issue (A & H):** In the abstract, “The quoted \(\sigma_{\rm from\,half}\) values scale as \(\sqrt{n}\) at fixed fractional offset and are therefore not mutually comparable across classes of different \(n\)” is correct. Later in §V the text broadens this point into a stronger, qualitative hedge that “raw σ values are not comparable across bins of different \(n\); only the monopole‑subtracted residuals are,” and then interprets several comparisons using *non‑subtracted* σ’s (e.g. calling cluster’s −4.7σ “the strongest single‑class signal” in §VI.D). The logic is inconsistent: if raw σ’s are “not comparable,” they should not then be used rhetorically as if they defined strength.  
**Fix:** Either (i) be consistent and *never* interpret magnitudes of raw σ across different \(n\), restricting “strongest signal” language to σ vs monopole, or (ii) soften the earlier statement to “less directly comparable” and always pair any cross‑row σ comparison with the corresponding \(|σ_{\rm obs}−σ_{\rm pred}|\).

P5‑M42 — Abstract vs. §VIII.C (DESIVAST “|ΔfCW|≲0.002 at all three algorithms”)  
**Issue (A & F):** Abstract: “three‑algorithm DESIVAST robustness (VoidFinder + V2‑REVOLVER + V2‑VIDE) returns \(|Δf_{\rm CW}|\lesssim 0.002\) at all three independent void definitions (largest |Δ| = 0.0019, V2‑REVOLVER…).” Table X lists the three sphere‑PIS contrasts: +0.0007, −0.0019, −0.0001. Section VIII.C then adds the GALZONE‑native contrasts, one of which is \(\Delta f_{\rm CW} = -0.0037\) (V2‑REVOLVER catalog‑native) with 95% CI [−0.0094, +0.0021]. The abstract’s “all three” phrasing is unqualified, but within the body “three‑algorithm” is sometimes used to mean “three sphere‑PIS definitions” and sometimes “three DESIVAST algorithms including catalog‑native variants.” The abstract as written will be read as “no DESIVAST void definition shows |ΔfCW|>0.002,” which is no longer true once catalog‑native GALZONE is included.  
**Fix:** Clarify in the abstract that the |ΔfCW|≲0.002 statement refers specifically to the *sphere‑PIS* definitions in Table X, and separately note that catalog‑native zone definitions give slightly larger |Δ| but still nonsignificant.

P5‑E7 — Abstract vs. §VI.C / Table IV (density‑quintile residual)  
**Issue (A, B & H):** Abstract: “density (|σ|max = 3.94 across density quintiles, pre‑monopole‑subtraction; the corresponding monopole‑subtracted residual is \(|σ_{\rm obs}-σ_{\rm pred}| = 1.87\), below all Bonferroni thresholds)”. Table IV confirms the maximum residual 1.87 in quintile 3 and gives |σobs|=3.94 and σpred=−2.07. Numerically consistent, but the abstract compresses two different thresholds:  
- primary family: Bonferroni‑5 at α=0.05 (|σ|≈2.58) applies to DESIVAST, not to this density scan;  
- density quintiles are treated with Bonferroni‑5 at α=0.01 (|σ|≈3.09) in §V.A and Fig. 5.  
The phrase “below all Bonferroni thresholds” is too vague; someone could incorrectly infer this is controlled at the same level as the primary family.  
**Fix:** Say explicitly “below the Bonferroni‑5 threshold |σ|≈3.09 for the five density quintiles at α=0.01” instead of “all Bonferroni thresholds.”

P5‑E8 — Figure 5 caption vs. text (Bonferroni threshold value)  
**Issue (A & B):** Fig. 5 caption: “dotted blue lines mark the Bonferroni‑5 thresholds at α = 0.01.” In §V.A the analytic formula is \(|σ|^{\rm Bonf}_{α,K} = \sqrt{2}\,\mathrm{erfc}^{-1}(α/K)\). Plugging α=0.01, K=5 gives |σ|≈3.09, consistent with what is implied near Table IV (“Bonferroni‑5 threshold |σ| = 3.09”). However, in §V.B the “Bonferroni‑5 primary family at α=0.05” is quoted with |z|≈2.58. Because both are “Bonferroni‑5,” the caption alone does not make clear that 3.09 is a *different α* from the primary DESIVAST family’s 2.58.  
**Fix:** Amend the figure caption to “Bonferroni‑5 thresholds at α=0.01 for these five density bins (note: different from the α=0.05 Bonferroni‑5 used for the DESIVAST primary family).”

P5‑M43 — Abstract vs. §IX.A / §XIII (RSD and “current sensitivity”)  
**Issue (F & H):** Abstract conclusion: “We interpret this as no evidence for environment‑dependent chirality beyond the catalog‑monopole offset at current sensitivity.” Section XIII later explains in detail that the V‑Web classifier operates in redshift space, that RSD induces anisotropic eigenvalue shifts, that ∼3–5% of cells may be near boundaries, and that no full Zel’dovich/reconstruction re‑run is done. In a strict sense, this means the absence of evidence applies to *redshift‑space classifications*, not to physical real‑space environment. The abstract’s “at current sensitivity” does not surface that classification‑space limitation.  
**Fix:** Qualify the abstract conclusion, e.g. “no evidence for environment‑dependent chirality in *redshift‑space V‑Web and DESIVAST classifications* beyond the catalog monopole” and echo that this is not yet a real‑space environmental theorem.

P5‑M44 — Null comparability: σ from different nulls juxtaposed (§VI.B, §VI.C, §VIII.F)  
**Issue (E):** Several places juxtapose σ values that are implicitly from different nulls without always reminding the reader that they are not directly comparable:  
- σfrom half (binomial against 0.5) for per‑bin deviations (e.g. Table III, Table IV).  
- σpred and σobs−σpred, where σpred is based on the Paper IV monopole, whose uncertainty is treated analytically.  
- permutation‑based max‑σ distributions (HEALPix, density, Phase‑2) which fix the observed global monopole and thus have a *conditional* null.  
These are put side‑by‑side in §VIII.F (“P4 monopole projects to σpred≈4.6σ… observed −5.00σ… residual 8%”) and elsewhere, with only a brief earlier caveat that “raw σ values are not comparable.” A careful reader can reconstruct the distinctions, but the text does not always flag when two σ’s shown together are from different null constructions.  
**Fix:** Add explicit phrases wherever both are used (e.g. “This σ is with respect to the half‑probability null, whereas σpred is under the Paper IV monopole null; they are not drawn from the same distribution and should not be interpreted as a single multi‑σ tension.”)

P5‑E9 — §VI.B logistic regression: missing odds‑ratio interpretation  
**Issue (E & H, more specific than P5‑E4):** §VI.B reports a logistic regression coefficient for redshift “0.0095±0.0229 (z‑score 0.41, p=0.68)” and later a similar statement about classifier confidence being “marginally significant (p≈0.02).” No odds ratio is given, and the practical magnitude is not translated (e.g. per unit‑z or per 0.1 increment). For confidence, which has its own scale, “p≈0.02” leaves the reader without a sense of whether the implied effect is <1 pp or larger.  
**Fix:** Convert both coefficients into odds ratios per relevant unit (e.g. per Δz=0.1 and per Δconfidence=0.1 or per SD) and quote the implied change in fCW with a rough magnitude, so that “no significant redshift dependence” and “confidence is a classifier property, not environmental” are quantitatively grounded.

P5‑M45 — §VI.B “env‑only Wald p=0.41 is therefore not expected to coincide with Pearson omnibus p=0.31”  
**Issue (D & H):** The text says the env‑only Wald p=0.41 on the unique‑spiral parent is “not expected to coincide” with the χ² p=0.31 from Table III on the row‑level parent. That is true but opaque: they are different samples *and* different statistics. There is no cross‑reference to where the χ² test is actually defined (Section VI.A) at that exact sentence, which makes this a slightly confusing internal reference.  
**Fix:** Add an explicit \S reference: “not expected to coincide with the Pearson omnibus p=0.31 from the row‑level 4×2 χ² test in §VI.A because they (i) use different parents and (ii) use different test statistics.”

P5‑M46 — Appendix B reproducibility checklist vs. usage in body (RNG / seeds)  
**Issue (D & I):** Appendix B lists a single “Deterministic seed: 20260515” and a path where Phase‑2 configs are persisted. The body, however, makes detailed claims about:  
- distinct RNG streams per scan family,  
- leg×program‑stratified shuffles,  
- stream‑to‑stream re‑draws (e.g. NSIDE=32 p changing 0.135→0.10),  
- a global max‑stat permutation across cells.  
There is no pointer from Appendix B back to the exact seed/stream specifications for these variants; the reader cannot check which seed produced which p‑value or how streams are derived. This is more than just “list all seeds” (your earlier P5‑M38): the *cross‑reference* from body claims to exact configs is missing.  
**Fix:** In Appendix B, add a short table mapping each permutation family mentioned in the text (redshift scan, density scan, each HEALPix NSIDE, Phase‑2 per‑cell, global max‑stat) to the exact config file, seed, and RNG‑derivation rule, and add a parenthetical in the main text (e.g. §VI.E, §VII.A) pointing to that table.

P5‑M47 — Appendix A operator notation vs. earlier footnote a (dimensional consistency / theoretical caveat)  
**Issue (C & D):** Footnote a in the introduction defines \(T_{ij} = \partial_i\partial_j \Phi\) with Φ obtained from Poisson’s equation, and states that only eigenvalue ordering matters for classification. Appendix A then introduces a toy operator \(L_{\rm parity}\supset g_\phi(\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)\), notes non‑covariance and gauge issues, but does not clearly connect back to the earlier definition of the density field used in the classification (δ vs ρ) or to the 25 Mpc/h smoothing scale. This is a dimensional‑consistency / notation‑consistency issue: if ρ is the physical matter density, ∇ρ/ρbg carries dimensions of inverse‑length, as does ∇φ in most EFT conventions; the text never states what units the implied coefficient \(g_\phi\) has, nor whether ρ here is the same smoothed field used for V‑Web.  
**Fix:** Explicitly state that ρ in the toy operator is the same *smoothed* density field used to define δ at Rs=25 Mpc/h, and give the dimensional analysis of \(g_\phi\) (e.g. “in these units \(g_\phi\) has dimensions of length, but we treat it as an effective dimensionless parameter by absorbing Rs”), making clear this is not a fully consistent EFT, just a heuristic mapping.

P5‑N4 — Abstract novelty / scope (“largest matched‑sample environmental‑dependence test…”)  
**Issue (G):** §VIII.B claims: “to our knowledge, the largest matched‑sample environmental‑dependence test of spiral chirality in DESI DR1 to date.” No explicit comparison to Shamir 2022, Galaxy Zoo DESI, or any other DR1 or Legacy DESI‑based chirality‑vs‑environment test is given beyond a brief mention that Shamir used Ganalyzer and saw 2–4% asymmetries. Strictly, this is an unsubstantiated novelty claim (no table or enumeration of sample sizes in competing works).  
**Fix:** Either (i) weaken this to “a large, well‑controlled matched‑sample test…” without “largest,” or (ii) add a short sentence comparing concrete sample sizes (e.g. Shamir’s effective n in DESI Legacy regions vs your 56,981 void spirals and 783,820 env‑labeled spirals) and state explicitly that you are not aware of any larger *matched‑sample environment* test in DR1.

P5‑N5 — Appendix B “DOI‑minted archival snapshot accompanies submission” (stale at pre‑submission stage)  
**Issue (D & J):** Appendix B says “A DOI‑minted archival snapshot of this directory accompanies journal submission.” In the text block you supplied, no DOI or archive identifier is present. For a referee at PRD, that is both a cross‑reference and a stale‑number problem: they cannot verify the DOI yet; at the same time, the language suggests the DOI already exists.  
**Fix:** Either add the actual DOI and citation if it is already minted, or rephrase to “will be deposited at acceptance; in the meantime the GitHub tag v0.1.66‑2026‑06‑11 contains the exact code and configs used.”

If you want, I can now go through tables one‑by‑one and explicitly recompute additional σ, p, and range numbers for a deeper arithmetic audit; I focused here on the most consequential mismatches and subtle comparability issues relative to your prior pass.