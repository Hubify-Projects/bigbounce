# P5 auto-2026-06-08_1737pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13229 chars)
**Wall time**: 536.0s

---

# Referee Report — Paper P5

## Overview

This paper is a null-detection environment-dependence test of spiral-chirality labels from an as-yet-unpublished companion catalog (Paper IV), cross-matched with DESI DR1 and stratified by a V-Web tidal classifier (secondary) and DESIVAST void catalogs (declared primary post-hoc). The central empirical result — that no environment-dependent chirality signal is found above a ~0.2 pp catalog-monopole floor — is plausibly correct, but the manuscript as submitted has multiple internal-audit leaks, arithmetic inconsistencies, narrative overreach in the title and abstract, post-hoc primary-path selection, and dependency on three unpublished companion papers. Several findings are individually disqualifying for PRD.

---

## ESSENTIAL findings

### P5-E1. Internal pipeline tag "P5" leaked throughout body text
Page 12–13 and elsewhere: "P5 matched-spiral catalog monopole f^P5_CW", "f^P5_CW", "σ^P5_pred", "P5 headline subsample", "the primary P5 environment-independence claim", "P5 environment-independence claim, anchored on the DESIVAST Δf_CW ≈ 0.0007 null". The reviewer-metadata block confirms "P5" is the internal paper tag. This is internal bookkeeping that must not appear in a PRD submission.
**Fix:** Strip every occurrence of "P5" and replace with "this paper" / explicit section reference. Similarly audit "P4" usage and replace with "Paper IV [3]" consistently.

### P5-E2. Arithmetic contradiction: "dark" sample sizes do not sum
§VI Dc page 7 states "filament dark (n = 21,203) σ = +2.85" and the abstract states "cluster_dark n = 4,234". But §VI Db page 7 states the *catalog-level* dark sample is "n = 14,782". 21,203 (filament dark) alone already exceeds the catalog total of 14,782; adding 4,234 cluster-dark to filament-dark yields 25,437, which is 1.7× the asserted total dark population. This is an internal contradiction that breaks the load-bearing "3.4σ bright-vs-dark filament sign-flip" claim made in the abstract and §VI Dc.
**Fix:** Reconcile the n values. Either the §VI Db tracer totals are mislabelled, or the per-V-Web-class dark counts are. The "3.4σ filament sign-flip" cannot be defended without this reconciled.

### P5-E3. Phase 2 single-cell n = 3,696,152 inconsistent with chirality-relevant sample
§VII page 8: "The largest single-cell |σ_from half| across the entire sweep is 11.32 (filament at R_s = 10, λ_th = 0, n = 3,696,152)." The chirality-relevant matched sample is 791,635. A single V-Web class cannot contain 3.7M chirality-relevant spirals from a 791,635 parent. Either the n is wrong, or the analysis silently switched to the full 14.6M spectro sample (which has no chirality labels). Either way, the σ = 11.32 cited as evidence of "monopole leaking through" is unsupported.
**Fix:** Either correct n and σ or document precisely which sample was used and how σ_from_half was computed without chirality labels on 3.7M objects.

### P5-E4. Title misrepresents the scope of the "Three-Algorithm Test"
Title: "A DESIVAST Three-Algorithm Test on 56,981 Void Spirals". But Table VIII shows that 56,981 is the VoidFinder result only; V2-REVOLVER returns n = 102,911 and V2-VIDE returns n = 81,354 (sphere-based) or 86,276 and 64,514 (catalog-native). The 56,981 number applies to ONE of the three algorithms. The title conflates a single algorithm's sample size with a "three-algorithm test."
**Fix:** Rewrite title. Either drop the specific number or use a range.

### P5-E5. Post-hoc primary/secondary designation
§V B page 5 explicitly admits "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc". The paper then declares DESIVAST as primary because it returns the cleanest null. This is exactly the garden-of-forking-paths failure mode that PRD demands papers avoid. The honest admission does not remove the problem; it documents it. The headline-level null claim cannot survive PRD review on this footing.
**Fix:** Either (a) submit as an explicitly exploratory analysis with all classifiers given equal weight and a properly LEE-corrected meta-statistic across the full analysis tree, or (b) re-cast the headline as "consistent with no environment dependence across all five classifiers tested" without designating any one as primary.

### P5-E6. Headline result depends on a non-peer-reviewed companion catalog (Paper IV) plus two further "in preparation" companion papers
References [3] (Paper IV — supplies all chirality labels), [4] (Paper II), and a "Paper III" cited in §XII B but not in the bibliography at all, are all "in preparation; manuscript in preparation" (duplicated phrase in refs [3], [4]). The numerical anchor of this paper — the monopole offset Δf_CW = −0.0026 used in σ_pred — comes from Paper IV. PRD will not accept a paper whose load-bearing systematic correction is sourced from an unpublished companion.
**Fix:** Either Paper IV must be on the arXiv with a publicly checkable monopole derivation, or this paper must re-derive Δf_CW internally with full uncertainty propagation.

### P5-E7. "Paper III" cited but not in the bibliography
§XII B page 17: "Paper II [4] and Paper III (both companion, not-yet-published works by the same author)". No bibliography entry exists for Paper III. This is a missing reference.
**Fix:** Either add the reference or remove the citation.

### P5-E8. σ_pred for filament does not match its formula
§VI A page 6: "predicting σ_pred from Δf_CW = −0.0026 gives σ_pred(filament) ≈ −3.16". With N = 408,187, σ_pred = 2 · 0.0026 · √408,187 = 3.32, not 3.16. The cluster value (−3.28) reproduces. The filament value is wrong by ~5%. Given σ_pred is used to anchor the no-environment-signal interpretation, this is a non-cosmetic error.
**Fix:** Recompute and correct.

### P5-E9. Table II row counts inconsistent with caption / §VI A subsample size
Table II page 5 reports per-class n that sum to 428 + 6,673 + 408,187 + 397,505 = 812,793, but §VI A explicitly says these come from "the 791,635 chirality-relevant matched spirals". The 21,158 excess is acknowledged buried in §VIII F as a "relaxed env-label confidence" subset, but Table II is not labelled this way. As written, the table is mislabelled.
**Fix:** Either restrict Table II to the 791,635 subset or relabel the caption.

### P5-E10. Two independent σ procedures juxtaposed without "not directly comparable" qualification
The body routinely mixes (i) σ_from_half against fCW = 0.5, (ii) σ_pred from the catalog monopole, (iii) σ_vs_monopole residuals, (iv) bright-vs-dark two-sample z, and (v) Bonferroni-corrected LEE σ from label-shuffle nulls. These appear side-by-side in Tables III, IV, V, VII, VIII, X without the per-juxtaposition reminder that they are not measuring the same quantity. The reader must constantly track which σ definition applies. Per PRD reviewer instruction 7, this is essential.
**Fix:** At every juxtaposition, label the σ procedure explicitly; add a key/glossary in §V.

---

## MAJOR findings

### P5-M1. Length grossly disproportionate to the contribution
The paper is 20 pages including a 20-citation bibliography to deliver a null result. The DESIVAST primary path (Δf_CW = 0.0007 on n = 56,981) fits naturally in 4–6 pages. The remainder is exploratory diagnostics, Phase 2 sensitivity sweeps, and dependency-tracking on Paper IV. Recommended cap: **8 pages** for the central result with the rest moved to supplementary material.

### P5-M2. Title oversells with "Three-Algorithm" and "V-Web Cross-Check"
Beyond the n = 56,981 issue (P5-E4), the title presents V-Web as a "cross-check" while the body designates V-Web as a "secondary diagnostic" and then runs five sections of V-Web analysis. The title structure inverts the body's stated primary/secondary hierarchy.

### P5-M3. Duplicated phrasing in references [3] and [4]
"companion paper (Paper IV), in preparation; manuscript in preparation" (ref [3]) and equivalent in ref [4]. The phrase "in preparation" appears twice in each entry.

### P5-M4. The "0/6 V-Web void spirals inside DESIVAST holes" result is prominently quoted including in the abstract
Abstract: "supplemented by an n = 6 per-galaxy classifier-disagreement check showing 0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes". n = 6 is not a result; it is a sample of 6 galaxies whose binomial 95% CI on disagreement rate spans roughly [54%, 100%]. Reporting "0/6" in the abstract gives a false impression of statistical content.
**Fix:** Remove from abstract or properly bracket the 95% CI.

### P5-M5. Pearson r = +0.006 at p = 0.88 marketed as "statistically indistinguishable from zero"
§VIII F page 13: "r(N_voids/pix, σ_pix) = +0.006, p = 0.88, indistinguishable from zero". This is correct as far as it goes, but the body then says "a direct single-statistic confirmation in this paper that the catalog-level −5σ is not environment-driven". An r = 0 result has finite power; the paper does not quote the power to detect, e.g., a 0.05-amplitude correlation at this n_pix = 727.

### P5-M6. RSD section is honest but its quantitative claim is incomplete
§XIII page 18 admits that the scalar σ_v/(aH) ≲ 5–8 Mpc/h bound is "necessary but not sufficient" and that the propagated per-class ΔfCW under anisotropic eigenvalue deformation is not separately quantified. The conclusion section nevertheless asserts robustness "under nine (R_s, λ_th) Phase 2 sweep cells (max CW-fraction range 0.22 pp)" without flagging that all nine cells use redshift-space positions.

### P5-M7. Bonferroni-5 LEE threshold conflates correlated DESIVAST estimators as independent
§V B page 5: "Treating the five DESIVAST estimators as a Bonferroni-5 family at α = 0.05, the per-test threshold is |σ|^Bonf_0.05,5 ≈ 2.81". But three of the five estimators are the same underlying matched-spiral subsample relabelled by three different (algorithm-correlated) void definitions; this is explicitly acknowledged in the abstract ("methodologically correlated by construction"). Bonferroni assumes independence; the effective number of independent tests is < 5. Stating a Bonferroni threshold and then claiming "no DESIVAST estimator crosses it" without an estimator-correlation correction overstates rigor.

### P5-M8. Abstract σ values not all matching body to required precision
Abstract: "Paper IV catalog-monopole offset of ∼0.2 pp" but body uses 0.26 pp. Abstract: "HEALPix scans...p = 0.61/0.135/0.413" but Table V shows 0.607. These are rounding-tier but warrant a single consistent convention.

### P5-M9. Reference [11] is "in submission to MNRAS" and [12] is on Zenodo; both are 2026-April arXiv preprints used as concurrent-literature validation
The paper itself is dated June 2026, and uses these two-month-old preprints as concurrent validation for the V-Web ↔ T-Web volume-fraction comparison. The text correctly hedges, but the body still says "consistent at the survey-shell-systematic level" with a ~8–18 pp void-fraction discrepancy — an 18 pp discrepancy is not consistency.

### P5-M10. The "primary path is essentially RSD-immune" claim is asserted not derived
§VIII page 10 RSD treatment paragraph asserts immunity because the typical RSD displacement is "several times smaller than the void effective radii", but no per-void-membership flip-rate is computed. The argument is plausible but unquantified.

### P5-M11. "Largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date" (§VIII B)
DR1 has been public for ~1 year. "Largest to date" within a 12-month window of a single survey release is true by construction (no prior DR1 paper on this question exists). The phrasing inflates significance.

---

## MINOR findings

### P5-mn1. Figure 1 wall+filament percentage
Caption: "wall+filament fraction (74.5%)". 41.3 + 33.3 = 74.6%. Off by one decimal.

### P5-mn2. Figure 5 cell label "0.13" appears under R_s = 50, λ_th = 0
Verify against Table VI which says 0.127. Truncation vs rounding inconsistency.

### P5-mn3. Reproducibility section says "Single config file (available in companion data repository)" without a URL or DOI
Companion data repository is referenced ~10 times in the manuscript with no location. PRD requires a citable DOI or URL.

### P5-mn4. Figure 3 caption truncation
Page 7 Figure 3 right panel x-axis tick labels appear visually overlapped/run-together ("[42, 1...]Den ∈ ..."). Axis label appears mangled.

### P5-mn5. "Hahn 2007 recipe, sometimes called the T-Web variant" footnote
Footnote a page 2: notes that paper retains "V-Web" label "for backward compatibility with prior analyses" although it actually implements the T-Web. This naming inversion is acceptable but should be flagged explicitly in §IV A title (e.g. "Tidal-tensor T-Web classifier (this work labels V-Web for backward compatibility)") to avoid confusion when comparing to Ref. [11] which actually says T-Web.

### P5-mn6. "Bonferroni-4 |σ| = 2.498" and "|σ| = 2.50" used interchangeably
§IX A page 15: "formally just crossing the Bonferroni-4 |σ|^Bonf_0.05,4 = 2.498 threshold at α = 0.05 by 0.04σ" — but 2.54 − 2.498 = 0.042σ, then "well below... |σ|^Bonf_0.01,4 = 3.02". Pick one decimal convention.

### P5-mn7. Appendix A toy EFT operator
Honestly admitted not gauge-invariant, not derived from cited literature, and the bound is "order-of-magnitude estimate only, not a quantitative ALP-coupling exclusion." Given those caveats, the appendix adds nothing and should be cut. Including it invites future citation as a "bound" when it explicitly is not one.

### P5-mn8. Table I "p99 separation 0.30″" — but 1.0″ acceptance allows tail
99th-percentile separation 0.30″ inside a 1.0″ radius is fine, but the table does not state how many matches sit in the 0.30″–1.0″ tail. Disclose.

### P5-mn9. The "−5σ" in the abstract is used colloquially
Abstract: "the catalog-level −5σ signal concentrated entirely in the '0 maximal voids per pixel' bin". The body shows this is actually −4.75σ (Table IX). Round to "−5σ" only after explicit statement.

### P5-mn10. Logistic regression "z-coefficient of 0.0059 with no significant intercept (0.000652)"
§VI B page 6. Units, fitting library, regularization, and standard errors not given. As written, this is unverifiable.

---

## NITS

### P5-N1. "filament_like_vs_filament" vs "filament like vs filament" notation inconsistency
Page 14–15: Table XI uses "filament_like" (underscored) but bullet list uses "filament like" (spaced). Pick one.

### P5-N2. "BGS-selection-function-conditioned imaging-leg systematics" is a 7-word hyphenated noun phrase repeated ~10 times
Acceptable in a single paper but consider abbreviating after first use.

### P5-N3. Figure 7 right-panel annotation "← filament_like 0.4982" partially overlaps the credible-interval bracket
Cosmetic.

### P5-N4. Bibliography ref [11] arXiv:2604.02463 and [12] arXiv:2604.01456
These post-April-2026 arXiv numbers are plausible given the June 2026 manuscript date but verify they exist before final submission.

### P5-N5. "Within ∼1σ of |σ_pred|" is used as the consistency criterion in §V
Pick "1σ" or "1.0σ" consistently.

---

## Summary recommendation

**REJECT**

The empirical content is plausibly correct and the paper is unusually candid about its limitations (post-hoc primary-path selection, dependence on unreviewed Paper IV, RSD bound only at the scalar level, BGS-selection-function-conditioned residual). However, in its current form the manuscript is disqualified for PRD by a combination of (i) an internal pipeline tag "P5" left throughout the body text, (ii) at least one hard arithmetic contradiction in the bright-vs-dark dark sample sizes that undermines the load-bearing 3.4σ filament sign-flip, (iii) a Phase 2 single-cell n = 3,696,152 that is incompatible with the 791,635 chirality-relevant subsample, (iv) load-bearing systematic corrections (Δf_CW = −0.0026, full-sky dipole nulls) imported from a companion paper that is not yet on the arXiv, (v) a title that quotes an n from a single algorithm while branding the test as three-algorithm, and (vi) self-acknowledged post-hoc primary-path designation in lieu of pre-registration. Each of E1–E10 is independently sufficient to require a major rewrite. The paper should be resubmitted only after Paper IV is publicly available, the arithmetic inconsistencies are resolved, the internal tags are stripped, the analysis is either pre-registered or fully LEE-corrected across the entire classifier-and-stratification tree, and the manuscript is shortened to approximately 8 pages befitting a null result of this scope.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Paper P5 (Second Pass, Fresh Eyes)

I re-examined the manuscript with attention to arithmetic, cross-references, null-procedure comparability, and abstract faithfulness. I recomputed every σ, fCW, and threshold I could verify from displayed inputs. Several **new** findings emerged, including one additional self-contradicting claim and at least one outright incorrect Bonferroni threshold that materially affects an inference in the body.

---

## NEW ESSENTIAL findings

### P5-E11. False claim that "none individually" crosses the Bonferroni-4 threshold (§VI D, page 7)
The redshift-stratified cluster decomposition lists z-quartile σ values "−2.33, −1.73, −3.14, −2.12" and then asserts: "**none individually crossing the Bonferroni-4 |σ| = 3.02 threshold at α = 0.01**". But |−3.14| = 3.14 > 3.02. The Z3 cluster quartile *does* cross the stated threshold. This is a direct factual error in the body, and it is load-bearing: the paragraph uses this claim to justify "the deviation is approximately uniform across redshift, consistent with a stationary classifier-bias monopole."
**Fix:** Either restate as "all but Z3" or rerun with a corrected threshold and re-derive the conclusion. The current sentence is false as written.

### P5-E12. Wrong Bonferroni-9 threshold quoted in §VII A (page 9)
The paper writes "the Bonferroni-9 (α = 0.05) threshold |σ|^Bonf_0.05,9 ≈ 3.02". Recomputed: for K=9 at two-sided α=0.05, σ = √2·erfc⁻¹(0.05/9) = √2·erfc⁻¹(5.56×10⁻³). Numerically erfc(1.96) ≈ 5.5×10⁻³, giving σ ≈ √2·1.96 ≈ **2.77**, not 3.02. The 3.02 value is actually the K=4, α=0.01 threshold (correctly given in §IX A). The author appears to have copy-pasted the wrong threshold into the Phase 2 significance framework.
**Consequence:** The Phase 2 robustness statement "zero produces a per-class |σ_vs_monopole| residual above the Bonferroni-9... threshold |σ|^Bonf_0.05,9 ≈ 3.02" is computed against the wrong threshold. The correct threshold (2.77) is more restrictive; whether the conclusion survives is not derivable from what is printed. **Re-derive.**

### P5-E13. Third independent demonstration that the §VI D bright/dark filament numbers are arithmetically impossible
Beyond P5-E2 (catalog dark total 14,782 vs filament-dark alone 21,203), Table II reports filament total n = 408,187, while §VI Dc states filament_bright = 416,701 and filament_dark = 21,203, summing to **437,904 — 29,717 more than the filament class itself**. This is independent confirmation that the 3.4σ bright/dark filament sign-flip — which the abstract elevates to a load-bearing diagnostic and explicitly flags for "future Rubin/LSST + DESI DR2 follow-up" — is computed from numbers that cannot all be from the same matched-spiral subsample. The cluster decomposition reconciles (cluster_bright + cluster_dark = 393,271 + 4,234 = 397,505 = cluster total ✓); the filament decomposition does not. The "real residual structure" interpretation in §VI Dd is therefore unsupportable until the sample-membership inconsistency is fixed.

### P5-E14. §VI Dd bright/(bright+dark) ratio 0.966 for filament does not match any consistent component count
§VI Dd states: "The per-V-Web-class bright/(bright+dark) ratio is {0.981, 0.962, 0.966, 0.989} across {void, wall, filament, cluster}". Cluster: 393,271/(393,271+4,234) = 0.9893 ✓. **Filament**: with the §VI Dc numbers 416,701/(416,701+21,203) = 0.9516, not 0.966. Inverting 0.966 with dark=21,203 implies bright = 602,392; with bright=416,701 implies dark = 14,665. No self-consistent triple exists. This is a fourth independent contradiction in the same paragraph cluster.

### P5-E15. §VI Dd "overall matched-spiral ratio 0.978" inconsistent with §VI Db component sums
§VI Dd: "against the overall matched-spiral ratio 0.978". From §VI Db component sums (bright 775,760 + dark 14,782): 775,760/(775,760+14,782) = **0.9813**, not 0.978. Combined with the 811,609 contingency-table total that does not match any quoted subsample size, this paragraph has multiple internally inconsistent denominators.

### P5-E16. §VIII vs §VIII A: VoidFinder/V2-REVOLVER/V2-VIDE void counts inconsistent between paragraphs
§VIII opening (page 10): "1,461 interior voids with VoidFinder, **420** with V2-REVOLVER, and 295 with V2-VIDE." §VIII C (page 11): "V2-REVOLVER (n_catalog_void = **1,992** effective voids... and V2-VIDE (n_catalog_void = 1,478, max 55.9 Mpc/h)". So V2-REVOLVER is reported as having 420 voids in one paragraph and 1,992 in the next, and V2-VIDE as 295 vs 1,478. The relationship between "interior voids" and "effective voids" is not defined; the reader cannot reconcile a factor-of-five discrepancy. The reader also cannot tell which catalog row count the chirality-relevant n_void = 56,981 / 102,911 / 81,354 sphere-membership counts in Table VIII map to.
**Fix:** Define each void taxonomy explicitly and reconcile the per-algorithm numbers.

---

## NEW MAJOR findings

### P5-M12. Abstract logically inverts the redshift regime of the V-Web "survey-edge artifact"
Abstract: "0.4836 (void; n = 428, −0.68σ — **survey-edge artifact dominated at z ≲ 0.24**, see DESIVAST-anchored re-projection below)". But §VIII A shows that of the 428 V-Web "void" spirals, **only 6 are at z ≤ 0.24**, with the remaining 422 (98.6%) at z > 0.24. The −0.68σ deviation is therefore overwhelmingly driven by spirals at *z > 0.24*, not z ≲ 0.24. The survey-edge artifacts in the V-Web run are at high z (near the survey-shell outer boundary), not at the low-z DESIVAST regime. The DESIVAST re-projection at z ≤ 0.24 cannot "resolve" the V-Web void σ that lives at z > 0.24 — it samples a different redshift volume entirely. The abstract conflates two distinct regimes.
**Fix:** Either correctly attribute the V-Web void artifact to z ≳ 0.24, or clarify which artifact the DESIVAST cross-check actually addresses.

### P5-M13. §VIII F refers to "1,821 valid pixels" at NSIDE=32; other NSIDE=32 pixel counts in the paper are 3,303 (Table V) and 727 (Figure 6 caption). Three different "valid" definitions, none reconciled
Within a single section (§VIII F), the NSIDE=32 valid-pixel count moves from 3,303 (Table V, all occupied pixels) to 1,821 (σ_vs_monopole distribution, §VIII F) to 727 (Pearson correlation pixels with both ≥200 spirals and ≥1 maximal void, Figure 6). The reader cannot determine which "valid" cut applies where. The skewness +0.044 and kurtosis +0.825 claims rest on 1,821 pixels of unknown construction.

### P5-M14. §VIII references §XIII as the "V-Web secondary path"; §XIII is "LIMITATIONS"
Page 10: "This is in contrast to the V-Web secondary path (§XIII), where the tidal-tensor eigenvalue field is computed from redshift-space galaxy positions..." §XIII is in fact the LIMITATIONS section. The V-Web *analysis* is §IV (algorithm) and §VI A (headline result). The reference is mislabelled, suggesting the author is using §XIII as a shorthand for "the V-Web RSD discussion" but the formal cross-reference is incorrect.

### P5-M15. The Phase 2 "below counting-statistics floor" argument is selective on which classes' floor
§VII A: "The maximum sweep-cell range across cells is 0.22 pp; this is **below the wall- and void-class counting-statistics floors** at all nine cells". True (floors 0.6 pp and 2.4 pp respectively). But the filament + cluster classes have floors of ~0.08 pp, and 0.22 > 0.08. The selected comparison is to the *least* informative classes. A reader who applies the floor argument to the dominant classes would conclude the inter-class range is *above* their floor by a factor 2.7×. The paragraph is technically true but cherry-picks the favourable comparison.

### P5-M16. §VIII A "1,461 interior voids with VoidFinder" vs §VIII A second paragraph "3,765 maximal voids"
Within ten lines, VoidFinder produces 1,461 interior voids (sentence 2) and 3,765 maximal voids (NGC 3,241 + SGC 524, sentence 5). These are presumably different taxonomies (maximal = top-level Voronoi cell; interior = ?), but the relationship is not explained. The point-in-sphere test runs against 101,863 *interior hole spheres* which "comprise the 3,765 maximal voids" — meaning ~27 holes per maximal void, not per interior void. The 1,461 number is left orphaned.

### P5-M17. Bonferroni-4 stated as 2.498 in §IX A, used as 2.50 elsewhere — but §IX A then says Tempel isolated σ=2.54 "formally just crossing" by 0.04σ
Numerical: 2.54 − 2.498 = 0.042 ≈ 0.04σ ✓. But this is a "crossing" of a multiplicity-corrected threshold and is presented as not a detection because of the empirical max-stat null. The body relies on the empirical null but does not give the empirical max-stat p value at this NSIDE — the reader has to infer.

---

## NEW MINOR / NIT findings

### P5-mn11. Eq (1) display has redundant left form
"σ_pred = ΔfCW/(0.5/√N) = 2·ΔfCW·√N". The first form is algebraically equal to the second; displaying both is harmless but unusual.

### P5-mn12. §VII A claims 1/(2√n_void) at n=400 is "~2.4 pp"
1/(2√400) = 1/40 = 0.025 = **2.5 pp**, not 2.4. Minor.

### P5-mn13. Table III labels "Quintile 1 (lowest)" through "5 (highest)"; the right-panel of Figure 3 caption says "predicted σ_pred = −2Δf_CW√N"
Sign matches text only because Δf_CW is negative. The figure caption strips the sign convention; reader has to deduce.

### P5-mn14. §VIII E "the survey-mask outside the BGS bright-side NGC+SGC coverage region" is asserted without showing the sky map of the 0-voids-per-pixel bin
The interpretation of the −4.75σ as a survey-mask artifact would be much more convincing if the paper showed the sky distribution of the 378,511 spirals in the 0-voids bin against the DESIVAST footprint. The interpretation is plausible but not demonstrated.

### P5-mn15. Reproducibility checklist says deterministic seed 20260515
20260515 (May 15, 2026) is plausibly the analysis run date as a seed, but choosing a date-coded seed *and* the manuscript date of June 2026 means the analysis was finalized one month before submission. Combined with E11/E12/E16 arithmetic errors, suggests internal-review time was inadequate.

### P5-N6. Footnote "a" reverses the standard taxonomy
The paper labels its tidal-tensor classifier "V-Web" while explicitly stating it implements what is "sometimes called the T-Web variant" of Hahn 2007. Yet Ref. [11] (concurrent literature) is correctly described as "T-Web". The result is that the paper's "V-Web vs T-Web concordance" comparison in §IX B is actually a "T-Web vs T-Web" comparison under different conventions. The footnote acknowledges this but the body continues to read as if comparing two distinct classifier families.

---

## Summary of arithmetic audit

| Quantity | Where stated | Recomputed | Status |
|---|---|---|---|
| σ_pred(filament), Δf=−0.0026 | −3.16 | **−3.32** | wrong (already E8) |
| σ_pred(cluster), Δf=−0.0026 | −3.28 | −3.28 | ✓ |
| Bonferroni-9 α=0.05 threshold | 3.02 | **2.77** | wrong (new E12) |
| Bonferroni-4 α=0.01 threshold | 3.02 | 3.02 | ✓ |
| Bonferroni-5 α=0.01 threshold | 3.09 | 3.09 | ✓ |
| Filament Q3 z-quartile σ vs Bonf-4 | "below 3.02" | **3.14 > 3.02** | false claim (new E11) |
| filament_bright + filament_dark | implicit ≤ 408,187 | **437,904** | impossible (new E13) |
| Overall bright/(bright+dark) | 0.978 | **0.9813** | inconsistent (new E15) |
| Filament class bright ratio | 0.966 | not reconcilable with stated components | impossible (new E14) |
| void counting-stat floor 1/(2√n) at n=400 | 2.4 pp | 2.5 pp | minor (mn12) |
| Figure 1 wall+filament | 74.5% | 74.6% | minor (mn1) |
| Density quintile fCW range to monopole agreement | ≈1σ | ✓ | ✓ |
| V2-REVOLVER catalog-native σ | −0.24 | −0.24 | ✓ |
| Tempel filament_like concordance | 0.026 pp | 0.026 pp | ✓ |
| HEALPix maximal-void bin σ's (Table IX) | as quoted | all ✓ | ✓ |
| Two-sample z filament bright vs dark | ≈3.4σ | 3.41σ from quoted n's | ✓ arithmetically, but the n's themselves are impossible (E13) |
| χ² = 4932 at 3 dof p < 10⁻¹⁰⁰⁰ | p<10⁻¹⁰⁰⁰ | p ≈ 10⁻¹⁰⁷⁰ | ✓ |

The pattern: the *primary DESIVAST analysis* (Table VII, Table VIII, Table IX, Figure 6) is arithmetically consistent throughout. The arithmetic failures concentrate in (i) the V-Web tracer-program decomposition §VI D, (ii) the Phase 2 / Bonferroni significance framework §V/§VII, and (iii) the void-taxonomy bookkeeping in §VIII A vs §VIII C. The headline DESIVAST null is robust to these errors, but the secondary V-Web diagnostics — including the prominently-featured "3.4σ filament bright/dark sign-flip" promoted to the abstract — are not currently supported by internally consistent numbers.

## Updated recommendation

**REJECT (strengthened)**. The first-pass review surfaced 10 essential findings; the second pass adds 6 more, including a direct false claim (P5-E11) and an incorrect Bonferroni threshold used to anchor the Phase 2 robustness statement (P5-E12). The bright/dark filament n contradiction (P5-E2) is now confirmed by two further independent component-arithmetic failures (P5-E13, P5-E14, P5-E15). The DESIVAST primary path is arithmetically clean and would survive as a much shorter standalone result; the V-Web secondary apparatus needs a full numerical audit before any version of this paper is resubmittable.