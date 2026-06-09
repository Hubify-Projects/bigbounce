# P5 auto-2026-06-08_2353pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (12072 chars)
**Wall time**: 467.1s

---

# Referee Report: P5 — Environmental Dependence of Spiral Chirality

## Overall assessment

This is a null-result paper claiming no environmental dependence of spiral chirality at DESI DR1 resolution. The core empirical work — cross-matching ~8.5M chirality labels with DESI DR1 and running V-Web/DESIVAST stratification — is legitimate. However, the paper has serious structural problems that preclude acceptance at PRD: (1) the headline depends critically on a companion Paper IV that is explicitly stated to be in preparation and not peer-reviewed, (2) the abstract is wildly bloated and contains review-log artifacts, (3) several σ values and arithmetic claims do not survive recomputation, (4) the bibliography contains references to unpublished companion works and what appear to be fabricated/future-dated arXiv IDs, and (5) the paper is far too long for a null result.

---

## ESSENTIAL findings

### P5-E1 — Headline result depends on an unpublished companion paper
**Section: Abstract, §II, throughout.** The abstract states: "We cross-match the 8,474,531-galaxy chirality catalog of Paper IV [3] (companion work, not yet peer-reviewed)." Reference [3] is: "H. Golden, A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals)… in preparation; manuscript in preparation." The entire paper's chirality labels, the ∆fCW = −0.0026 monopole, and the σpred prescription (Eq. 1) derive from a paper that does not exist in citable form. PRD cannot publish a result whose load-bearing input is a non-existent companion paper. **Required fix:** Either Paper IV must be submitted and posted to arXiv prior to acceptance, or this paper must reconstruct the chirality catalog and monopole bound self-contained.

### P5-E2 — References [11] and [12] have arXiv IDs in the future and/or fabricated form
**Bibliography, page 20.** Refs [11] (arXiv:2604.02463) and [12] (arXiv:2604.01456) carry arXiv identifiers with the "2604" YYMM prefix, indicating April 2026 — the same month/year as the paper's stated date. These citations are described in the body as "concurrent literature" and "currently in submission to MNRAS". Either these arXiv IDs are fabricated, or they refer to preprints posted essentially simultaneously and cannot be verified independently by a referee in 2025. **Required fix:** Provide verifiable arXiv IDs and abstracts; if these works do not exist, remove them. The §IX B "concurrent literature overlay" subsection is load-bearing for the cross-classifier robustness argument and cannot stand on unverifiable references.

### P5-E3 — Review-log / round-tag artifacts present in body text
**§VIII F, page 12.** The text contains: "the 21,158-row excess (2.7%) over the 791,635-spiral headline subsample is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter…" — this reads as internal audit prose justifying a row-count discrepancy that should never have appeared in a clean manuscript. **§X, page 17:** "We list it alongside (i) DESIVAST per-galaxy cross-match, §IX B; (ii) within-class density quartile null, §VI D; (iii)…" — this is a bookkeeping enumeration, not paper prose. **Required fix:** Remove all internal-audit bookkeeping language; resolve the 791,635 vs 812,793 sample size ambiguity in a single clean methods paragraph.

### P5-E4 — Abstract is unreadable and contains over-claims
**Abstract, pages 1–2.** The abstract is ~1100 words, contains internal subsections labeled "Robustness", quotes 4-decimal CW fractions in running text, cites by-section numbers (§IX B, §VIII), enumerates points (i)–(iv), and includes hedge constructions like "not load-bearing", "methodologically correlated by construction", "supporting rather than load-bearing". A PRD abstract should be ≤250 words. The current abstract is an executive summary with internal disclaimers. **Required fix:** Cut to ≤250 words stating the data, method, headline number with uncertainty, and one robustness claim.

### P5-E5 — σpred formula appears to be miscomputed in the body
**§VI A, page 6.** Text states: "predicting σpred from ∆fCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28". Using Eq. (1), σpred = 2·∆fCW·√N:
- Filament (N=408,187): 2·(−0.0026)·√408187 = −0.0052·638.9 = **−3.32**, not −3.16.
- Cluster (N=397,505): 2·(−0.0026)·√397505 = −0.0052·630.5 = **−3.28** ✓.
The cluster value is consistent; the filament value disagrees. Later in §VII A the values quoted are 3.27σ (cluster) and 3.32σ (filament) — these contradict the §VI A values. **Required fix:** Reconcile the σpred values across §VI A and §VII A; one of the two sections is wrong.

### P5-E6 — σ from half values in Table II do not match recomputation
**Table II, page 5.** Recomputing σ = (nCW − 0.5N)/(0.5√N):
- Void: (207 − 214)/(0.5·√428) = −7/10.344 = **−0.677** ✓ (≈ −0.68).
- Wall: (3359 − 3336.5)/(0.5·√6673) = 22.5/40.847 = **+0.551** ✓ (≈ +0.55).
- Filament: (203261 − 204093.5)/(0.5·√408187) = −832.5/319.45 = **−2.606** ✓ (≈ −2.61).
- Cluster: (197284 − 198752.5)/(0.5·√397505) = −1468.5/315.27 = **−4.658** ✓ (≈ −4.66).

Table II passes. However Table VII (DESIVAST) page 11: void (28284 CW / 56981) → fCW = 0.4964, σ = (28284 − 28490.5)/(0.5·√56981) = −206.5/119.35 = **−1.730**, paper says −1.71 (close, within rounding of unstated nCW). Non-void: fCW = 0.4971, σ = (0.4971−0.5)·2·√621964 / 1 = −0.0058·788.65 = **−4.57**, paper says −4.59 (consistent within rounding). These pass within rounding. **Recommendation:** Provide nCW explicitly in Table VII/VIII so σ is reproducible.

### P5-E7 — Within-class density-stratified arithmetic inconsistency
**Table IV, page 6.** For cluster Q1 (n=99,398, σ=−3.07), this implies fCW = 0.5 + (−3.07)/(2·√99398) = 0.5 − 3.07/630.99 = 0.5 − 0.004866 = **0.49513**. For Q2 (n=99,369, σ=−3.42): fCW = 0.5 − 3.42/630.90 = **0.49458**. The paper does not list fCW per quartile, only σ. The Q3 value σ=−0.37 implies fCW = 0.49941 — i.e. the "most-typical-cluster-density quartile" returns essentially parity. **However**, the average of the four quartile σ should reconcile to the overall cluster σ ≈ −4.66 on n=397,505. Combining four independent binomial samples: σ_combined = Σ(nCW,i − 0.5ni)/(0.5·√ΣN). The implied excess CW deficit summed across quartiles: Q1: 99398·(0.5−0.49513)= 484, Q2: 99369·0.005418= 538, Q3: 99526·0.000585= 58, Q4: 99212·0.003901= 387. Total excess = 1467, vs cluster nCW deficit = 1468.5. **Passes within rounding.** But the description "Q3 returns σ = −0.37, statistically null after Bonferroni-4 correction" combined with Q1+Q2 both at |σ| > 3 is read by the authors as "boundary-misclassification" — this is an unfalsifiable post-hoc explanation. **Required fix:** Either commit to the boundary-misclassification interpretation with a quantitative test (e.g., re-run V-Web at higher λth to verify the Q1/Q2 deficit moves to filament), or retract the interpretation and report the within-class result as descriptive only.

### P5-E8 — Bright vs dark sign-flip is buried and contradicts the headline
**§VI A item d, pages 7–8, and abstract.** The paper reports a 3.4σ filament-class sign-flip between BGS-bright (σ=−2.80) and LRG/ELG/QSO-dark (σ=+2.85). The abstract says this is "best read as a real residual structure that the current data do not allow us to cleanly partition between a pure BGS-selection-function-origin… and a residual target-program-conditioned astrophysical signal." This is the most significant single signal in the paper, yet it is hidden behind "headline environment-independence statement of this paper is anchored on the DESIVAST primary analysis below". A 3.4σ residual that the authors cannot explain is not a null result. **Required fix:** Either rewrite the headline as "no environmental dependence except for a 3.4σ target-program-conditioned residual that we cannot explain", or demonstrate via direct test that it is a BGS systematic.

### P5-E9 — Sigma values from incompatible null procedures juxtaposed without warning
**Abstract and §VI E.** The abstract lists "label-shuffle p=0.372", "|σ|max = 3.94 across density quintiles, pre-monopole-subtraction", "label-shuffle nulls p=0.61/0.135/0.413". These are quoted side-by-side with the binomial σfrom_half values (e.g., −4.66σ for cluster). Binomial σfrom_half is a parametric statistic against fCW=0.5 with **no monopole subtraction**; the label-shuffle p-values are from a different null (CW/CCW exchangeability conditioned on positions). The reader is left to infer which σ is comparable to which. This violates instruction #7 of the review: σ values from different null procedures cannot appear side-by-side without explicit "not directly comparable" qualification. **Required fix:** At every juxtaposition, label the null procedure and add an explicit comparability statement.

### P5-E10 — The "interpret this as no evidence" statement is over-strong given the −4.66σ cluster result
**Abstract.** The abstract states "We interpret this as no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity." But the −4.66σ cluster deviation is reported without rigorous monopole subtraction in the headline; the post-hoc Table X "σ vs monopole" residuals require accepting Paper IV's ∆fCW = −0.0026 as input, which is itself unpublished (see E1). The chain is: unpublished Paper IV → ∆fCW → σpred → residual = null. If any link in this chain fails, the "null" verdict collapses. **Required fix:** Either present the headline without the monopole subtraction (in which case it is NOT a null), or publish Paper IV first.

### P5-E11 — Appendix A toy EFT mapping is not a physics result and should be removed
**Appendix A, page 19.** The "toy EFT mapping" introduces an operator Lparity ⊃ gφ(∇iφ)(∇iρ/ρbg)(L̂·ẑ) that the authors themselves admit "breaks rotational invariance via the fixed coordinate-system unit vector ẑ", is "not contained in either Alexander & Yunes or Lue-Wang-Kamionkowski", "is a heuristic parametrization", and is "not a covariant EFT operator". This is not physics; it's hand-waving with disclaimers. PRD is a physics journal. **Required fix:** Remove Appendix A entirely, or replace with a properly-derived covariant operator.

---

## MAJOR findings

### P5-M1 — Length grossly disproportionate to contribution
The paper is 20 pages for a null result whose central claim ("CW fraction is the same across V-Web classes within counting statistics") could be made in 4–6 pages. The bulk of the page count is consumed by post-hoc robustness checks against criticisms the paper anticipates. **Recommendation:** Cut to ≤8 pages: data, V-Web method, DESIVAST primary result, three robustness checks, conclusion.

### P5-M2 — "Primary vs secondary" declaration is post-hoc
**§V B, page 5.** "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc, and we declare it explicitly here". This is honest but fatal: when 5+ classifiers are run and the most convincing null is declared primary after the fact, the multiplicity is uncontrolled. The Bonferroni-5 correction the authors apply does not cover the full garden of forking paths (V-Web Phase 2 sweep × DESIVAST × Tempel × ASTRA × T-Web × stratifications). **Required fix:** Either pre-register, or report all classifiers with a proper meta-multiplicity correction.

### P5-M3 — DESIVAST sample-size claim of "130×" larger than V-Web is misleading
**Abstract and §VIII.** "n=56,981 DESIVAST-defined void galaxies… ∼130× larger than the V-Web void class (n=428)". This comparison is unfair: the V-Web void at n=428 is restricted to z ≤ 0.24 chirality-relevant V-Web "void"-labeled spirals; the DESIVAST sample includes the entire low-z BGS sample falling into a sphere. They measure different quantities. **Required fix:** State explicitly that DESIVAST and V-Web "void" labels are not the same physical population (the paper does say "0/6 V-Web 'void' spirals fall inside any DESIVAST hole" — this is fatal to the comparison and should be foregrounded).

### P5-M4 — DESIVAST "0/6" cross-match disagreement is buried
**§VIII A, page 10.** "0/6 V-Web 'void' spirals inside any DESIVAST hole; minimum spiral-to-nearest-hole separations span 28.7–158.1 Mpc/h." A 0% concordance between two void definitions at z ≤ 0.24 is a methodological catastrophe for the V-Web classifier. The paper acknowledges this then proceeds to use V-Web results in the headline. **Required fix:** If V-Web void at low z is 0% correlated with DESIVAST void, the V-Web void σ=−0.68 result must be removed from the headline table.

### P5-M5 — Tempel mapping is ad hoc and uninformative
**§IX A.** The mapping of FoF multiplicity {1, 2–4, 5–19, ≥20} to {void, wall, filament, cluster} is described as the authors' construction and acknowledged to be "not exact". The 0.026 pp filament concordance is then claimed as "supporting" robustness. With four mapping choices and four V-Web classes, the chance of one pair matching at 0.026 pp is non-trivial. **Required fix:** State the chance probability of a single-class match at this level under the null, or remove the Tempel cross-check as load-bearing.

### P5-M6 — Phase 2 sensitivity sweep does not test what it claims
**§VII.** The sweep varies (Rs, λth) but reports "max fCW range across env classes" — a descriptive statistic. The "largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs=10, λth=0)" is then explained away as monopole leakage. If the monopole prediction always tracks the observed σ regardless of (Rs, λth), this is not robustness against environmental dependence — it is a consistency check on the monopole prediction. **Required fix:** Report the per-class σvs_monopole residual at each (Rs, λth) cell, not the inter-class range.

### P5-M7 — Figure 5 heat-map values inconsistent with Table VI
**Figure 5, page 10 vs Table VI, page 8.** Table VI lists the 9 sweep values: 0.066, 0.088, 0.149, 0.165, 0.146, 0.220, 0.127, 0.052, 0.102. Figure 5 caption says "max range across all nine cells is 0.22 pp (at Rs=25 Mpc/h, λth=0.3)" — this matches. But the heat-map cell labels visible in the figure (per the rendered PDF text "0.07, 0.09, 0.15 / 0.17, 0.15, 0.22 / 0.13, 0.05, 0.10") match Table VI in different cell ordering. Verify the (Rs, λth) axis ordering in Figure 5 matches the table — the Rs=10 row in Figure 5 appears to read "0.07, 0.09, 0.15" but Table VI lists Rs=10 values as 0.066, 0.088, 0.149. The middle value 0.088 rounds to 0.09 ✓. Passes — but cell labels show 2 decimals while table shows 3; standardize.

### P5-M8 — HEALPix Mollweide projection (Figure 4 caption vs Figure 6)
**Figure 6, page 14.** Caption claims "HEALPix NSIDE=32 Mollweide projection. Top: count of DESIVAST maximal voids per pixel (885 occupied pixels, median 4 voids/pix). Bottom: per-pixel chirality σfrom half…" The figure as rendered shows what appears to be a heavily masked sky with a colorbar that runs 0–20 voids on top and −6 to +6 σ on bottom, with most pixels gray. The Pearson r=0.006, p=0.88 claim is statistically defensible but the figure itself is largely uninformative — it shows mostly empty space. **Required fix:** Replace with a scatter plot of σ vs void count per pixel, which would directly visualize the Pearson correlation claim.

### P5-M9 — RSD treatment is hand-waved
**§VIII, page 10 and §XIII, page 18.** The paper invokes "anisotropic eigenvalue deformation" then concludes the effect is "sub-percent (∼ 0.2 pp), the same order of magnitude as the Phase 2 sweep max-range of 0.22 pp rather than negligible relative to it." A systematic that is the same magnitude as the headline upper bound IS the headline upper bound. **Required fix:** Run reconstructed-position V-Web; the paper defers this to "a companion follow-up" but the present null cannot be quoted without it.

### P5-M10 — The "void bin n=428" headline is statistically uninformative
**Table II.** With n=428 the 95% credible interval brackets parity by ±0.05 in fCW. Reporting this as a headline result alongside n=397,505 cluster is misleading; the void result has ~30× larger uncertainty than the cluster result. **Required fix:** Drop the n=428 void row from the headline; the DESIVAST n=56,981 result is the only meaningful void number.

### P5-M11 — Eq. (2) Bonferroni threshold formula
**§V A, page 4.** "|σ|_Bonf_α,K = √2 erfc⁻¹(α/K)". For α=0.01, K=5: erfc⁻¹(0.002) ≈ 2.185, so √2 · 2.185 = 3.09 ✓. For α=0.05, K=1054: erfc⁻¹(4.74e-5) ≈ 2.864, √2·2.864 = 4.05 ✓. Formula is correct.

### P5-M12 — "8% larger than P4 catalog-mean" is post-hoc rescue
**§VIII F, page 12.** "the observed −5.00σ corresponds to ∆fP5 ≈ −0.0028, ∼8% larger than the P4 catalog-mean. This residual 8% enhancement is consistent with the spectroscopically-confirmed subsample being more strongly weighted to the BGS-bright leg…" — this is a post-hoc explanation of a 1.5σ discrepancy between P4 and P5 monopoles. **Required fix:** Either jointly fit the monopole with P4 and P5 data, or acknowledge that the P5 monopole is independently measured and slightly different.

---

## MINOR findings

### P5-Min1 — Figure 1 cluster fraction reads 1.0% in caption but pie shows "Cluster 1.0%"
Caption: "cluster volume fraction (1.0%)". Body §IV B: "{void 0.244, wall 0.413, filament 0.333, cluster 0.010}". Consistent ✓ but state explicitly 0.010 = 1.0%.

### P5-Min2 — Median z reported as 0.168 in Table I, ¯z values in §VI D, page 7
"z-quartile-marginalized ¯z = 0.045, 0.083, 0.122, 0.190 for cluster; ¯z = 0.067, 0.139, 0.205, 0.320 for filament". The filament Z4 mean 0.320 is well above the table median 0.168 — filament class has a tail to high z. Note this explicitly.

### P5-Min3 — Footnote "a" on page 2 explains the V-Web naming
The footnote acknowledges "We use the tidal-tensor formulation… sometimes called the T-Web variant… for backward compatibility with prior analyses we retain the 'V-Web' label." This is a known terminological abuse and the authors flag it correctly, but it would be clearer to use "T-Web" throughout.

### P5-Min4 — Table I imaging-leg counts do not sum to total
Leg BASS+MzLS (688,608) + DECaLS (1,538,880) + DES (4,724) = **2,232,212** ✓ matches "Matched primary after dedup".

### P5-Min5 — Table I CW+CCW+NS sum check
393,592 + 398,043 + 1,440,577 = **2,232,212** ✓ matches.

### P5-Min6 — fCW = 393,592 / (393,592 + 398,043) = 393,592 / 791,635 = 0.49718
Quoted as 0.4972 ✓. σ = (393592 − 395817.5)/(0.5·√791635) = −2225.5/444.9 = **−5.00** ✓.

### P5-Min7 — Reference [9] Shamir 2022 citation
"L. Shamir, … Mon. Not. Roy. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866". The cited "2–4% large-scale asymmetry" claim should be checked against the abstract of Shamir 2022; the comparison "an order of magnitude smaller" assumes the Shamir result is comparable in amplitude metric, which requires a specific computation.

### P5-Min8 — Tempel filament_like n=14,317 (Table XI) vs body "only ∼14k galaxies in the filament-like bin"
Abstract: "only ∼14k galaxies in the filament-like bin" ✓ matches Table XI.

### P5-Min9 — Ref [13] Rincón et al. 2025 ApJ 982, 38
This is a real, peer-reviewed reference. ✓.

### P5-Min10 — "auto-2026-06-08_2353pt" round tag
The reviewer metadata block at the top of the prompt mentions this; the rendered PDF does not contain this tag. Per the instruction, only flag what appears in the PDF — this is internal-only and OK.

### P5-Min11 — Figure 3 axis label
The "Den ∈ [42, …]" notation in the x-axis label is unreadable in the rendered figure. **Required fix:** Use density quintile bin labels Q1–Q5 only; move numeric ranges to a table or caption.

### P5-Min12 — "Dated: June 2026"
Paper is dated June 2026 but cites April 2026 arXiv preprints as "concurrent". For a 2026 paper this is plausible but the referee cannot verify in 2025.

### P5-Min13 — Bonferroni-4 threshold cited as both 2.498 and 2.50 and 3.02
"the maximum |σfrom half| across the four Tempel classes is 2.54 (Tempel isolated), formally just crossing the Bonferroni-4 |σ|^Bonf_0.05,4 = 2.498 threshold at α=0.05 by 0.04σ but well below… |σ|^Bonf_0.01,4 = 3.02 at α=0.01." Two different α — clarify. For α=0.05, K=4: √2·erfc⁻¹(0.0125) = √2·1.7647 = **2.497** ✓. For α=0.01, K=4: √2·erfc⁻¹(0.0025) = √2·2.1352 = **3.020** ✓.

### P5-Min14 — Reproducibility checklist
"Single config file (available in companion data repository)" — no URL given. **Required fix:** Provide a Zenodo DOI or GitHub URL.

---

## NITs

### P5-N1 — Duplicate/repeated phrasing
"matched primary" and "matched primary after dedup" used repeatedly without consolidation.

### P5-N2 — "f^void_CW = 0.4964 vs f^non-void_CW = 0.4971" formatting
LaTeX superscripts/subscripts render inconsistently across the abstract and body.

### P5-N3 — Sentence in §VI D footer
"the class boundary is verifiable quantitatively from the table: cluster Q1 (¯ρ=1.55) is less dense than filament Q4 (¯ρ=1.86)" — awkward; the authors are making a methodological point about V-Web's λth=0 boundary that should be in §IV not embedded in a results subsection.

### P5-N4 — "Pre-cell label-shuffle null"
**§VII A, page 9.** "Pre-cell" should be "Per-cell".

### P5-N5 — Acronym density
"BGS, LRG, ELG, QSO, NGC, SGC, FoF, NN, NSIDE, HEALPix, ZWARN, GALZONE, ZONEVOID" — define each at first use.

---

## Summary recommendation

**REJECT**

The paper rests on an unpublished companion (Paper IV) for its central monopole bound, cites unverifiable future-dated arXiv preprints for key cross-classifier validation, contains internal-audit prose that should have been removed before submission, has a bloated 1100-word abstract with internal subsections, presents a "null" headline whose 3.4σ bright-vs-dark target-program sign-flip in the filament class is unresolved, and devotes 20 pages to a result that — if real — fits in 6. The arithmetic that can be checked is mostly correct (the binomial σ values in Table II reproduce), but the chain of inference depends on accepting an unpublished ∆fCW = −0.0026 monopole as input, post-hoc declaring DESIVAST the "primary" classifier after running five, and explaining away a 4.66σ cluster deviation as monopole leakage. The DESIVAST cross-check is the genuinely interesting piece of work and could form the basis of a substantially shorter, self-contained paper once Paper IV is published. As submitted, this manuscript does not meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Second Pass (Fresh-Eyes Re-examination)

After re-examining the manuscript with focus on the ten categories specified, I identify the following additional findings not present in the initial review.

---

## NEW ESSENTIAL findings

### [P5-E12] — Table II is computed on the 812,793-row env-labeled superset, NOT the headline 791,635 chirality-relevant subsample
**Table II, page 5; §VI A; abstract.** Summing the per-class counts in Table II:
$$428 + 6{,}673 + 408{,}187 + 397{,}505 = 812{,}793$$
This exceeds the headline "791,635 chirality-relevant spirals" by 21,158 (2.7%). §VIII F explicitly admits this: *"the per-class nCW values on the 812,793 superset sum to 404,111… the 21,158-row excess (2.7%) over the 791,635-spiral headline subsample is the population of CW/CCW-labelled spirals whose V-Web env-class assignment passes the relaxed env-label confidence used by the cosmic-web pipeline but is excluded from the headline by a stricter env-class-uncertainty filter."* But the abstract and §VI A introduce the headline result as being computed on the 791,635-spiral set:
> *"Per-class CW fractions on the 791,635 chirality-relevant spirals are…"*

The actual headline table is on a different (larger, more permissive) sample. The "monopoles match to 4 decimals" reconciliation in §VIII F does not rescue the framing: the σfrom-half values in Table II (−2.61, −4.66, etc.) are computed at N=408,187 etc. on the superset, not at the strict chirality-relevant N. **Required fix:** Either recompute Table II on the strict 791,635 sample, or change the abstract/headline to state the analysis is on the 812,793-spiral env-labeled superset.

### [P5-E13] — §VI A item c filament bright + dark exceeds total filament class by 29,717
**§VI A item c, page 7.** Text states "filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203)". Sum:
$$416{,}701 + 21{,}203 = 437{,}904$$
But Table II reports total filament class as 408,187, and §VI D quartile decomposition reconciles to 408,187 (102,050+102,065+102,033+102,039). Bright+dark filament cannot exceed total filament; the difference (29,717) is unaccountable. This makes the load-bearing 3.4σ bright-vs-dark sign-flip arithmetically inconsistent with the rest of the paper. The two-sample z = −3.4σ recomputation I performed *does* arrive at |z| ≈ 3.4 from the stated n and σ values internally, but those n values themselves contradict the parent filament count. **Required fix:** Reconcile filament-class sample counts across §VI A item c, Table II, and §VI D.

### [P5-E14] — Bonferroni threshold value mis-stated in §VII A
**§VII A, page 9.** Text states "zero produces a per-class |σvs monopole| residual above the Bonferroni-9 (α = 0.05) threshold |σ|Bonf 0.05,9 ≈ 3.02". Recomputing Eq. (2):
$$|\sigma|^{\text{Bonf}}_{0.05,9} = \sqrt{2}\,\text{erfc}^{-1}(0.05/9) = \sqrt{2}\cdot\text{erfc}^{-1}(0.00556) \approx \sqrt{2}\cdot 1.96 \approx 2.77$$
The value 3.02 corresponds to K=4 at α=0.01, **not** K=9 at α=0.05. This is the only Bonferroni-formula citation I found that is mis-computed; the §V A citations (3.09 at K=5/α=0.01; 4.05 at K=1054/α=0.05) and §VI D citations (2.50 at K=4/α=0.05; 3.02 at K=4/α=0.01) all check out. **Required fix:** Replace 3.02 with 2.77, and re-evaluate whether the §VII A conclusion ("zero of nine cells exceeds the threshold") changes.

---

## NEW MAJOR findings

### [P5-M13] — Phase-2 sweep largest σ refers to n = 3,696,152 galaxies that cannot exist in the catalog
**§VII, page 8.** "The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152)." But the chirality-relevant matched sample is 791,635 and the matched-primary-after-dedup is 2,232,212. 3,696,152 is ~4.7× the chirality-relevant catalog and ~1.7× the dedup matched primary. The sample basis is not stated. If this is full DR1 spectro (14.6M) restricted to filament, then σfrom-half cannot be computed without per-galaxy CW/CCW labels. **Required fix:** Identify the sample basis explicitly; if this is a mass-binned or weighted estimate, state the procedure. As written, the headline robustness statement of §VII rests on a number whose definition is unrecoverable from the manuscript.

### [P5-M14] — Multiple inconsistent bright+dark sample-size denominators
**§VI A items b–d.**
- Item b (tracer breakdown): bright + dark = 775,760 + 14,782 = **790,542**; with backup + other = **791,635**.
- Item c (filament-class): filament bright + filament dark = 416,701 + 21,203 = **437,904** — exceeds parent class.
- Item d (contingency): "nbright+dark = **811,609** spirals" — different from item b by 21,067, neither matching the 21,158 superset excess nor the 791,635 strict total.

Four different sample sizes appear in three adjacent sub-items addressing the same bright/dark stratification. **Required fix:** Tabulate the four-by-two V-Web×program contingency explicitly; sample sizes must reconcile.

### [P5-M15] — "Approximate concordance" with Ref [11] T-Web hides 8–18 pp deviations
**§IX B, page 15.** "The sheet (V-Web wall) and filament classes agree to within ∼5 percentage points across both methodologies (allowing for the tracer- and volume-mismatch caveat above), which is approximate concordance for two independent classifiers… The void and knot/cluster classes deviate by larger margins: V-Web's void fraction is higher than T-Web's by +8–18 pp." A 5 pp difference in volume-filling fraction at the dominant population is large — for a 50% volume class, 5 pp is a 10% relative discrepancy. Calling 5 pp "approximate concordance" without a significance test is an unquantified hedge. The 8–18 pp void deviation is much larger than the 0.22 pp Phase-2 sweep range used as the headline robustness statistic in §VII; this directly undermines the §VII robustness framing. **Required fix:** Quote the significance of the inter-classifier disagreement, or remove "approximate concordance" language.

### [P5-M16] — §VIII F per-pixel σ-distribution dispersion is 18% above unity but not tested
**§VIII F, page 13.** "The unit standard deviation (within ∼18%, consistent with finite-pixel sample-size fluctuation), zero skewness, and modest positive kurtosis are all consistent with a pure shot-noise residual around the P4-monopole." Std = 1.184 on n = 1,821 valid pixels. The standard error of a sample std on Gaussian data is ~1/√(2n) ≈ 0.017, so a 18% deviation from unity (Δ=0.184) is ~11σ from expectation — emphatically NOT "within finite-pixel fluctuation". Either the σ statistic carries an additional dispersion source not modeled by Bernoulli null, or the residual is structured. **Required fix:** Compute the χ² goodness-of-fit of the σ-distribution to N(0,1) on n=1,821 pixels; quote the p-value.

### [P5-M17] — DESIVAST ∆fCW sign convention inconsistent between Table VIII and body
**Table VIII, page 12 vs §VIII C body.** Body says "V2-REVOLVER returns f^void_CW = 0.4986 slightly above f^non−void_CW = 0.4967 (the opposite sign of VoidFinder's small difference)". With void > non-void, the natural ∆ = f^void − f^non-void = +0.0019 for V2-REVOLVER and −0.0007 for VoidFinder. But Table VIII gives ∆fCW = +0.0007 (VoidFinder), −0.0019 (V2-REVOLVER), −0.0001 (V2-VIDE) — the opposite sign convention (∆ = f^non-void − f^void). The sign convention is never declared in the Table caption. **Required fix:** State the sign convention in Table VIII caption and harmonize with body prose.

---

## NEW MINOR findings

### [P5-Min13] — Tempel "isolated" fCW value rounding
**Table XI.** 28,962/58,539 = 0.49475..., standard rounding to 4 decimals gives 0.4948, but Table XI reports 0.4947. Minor but affects the 1.11 pp concordance distance with V-Web void.

### [P5-Min14] — Figure 1 caption "wall+filament = 74.5%" rounding
0.413 + 0.333 = 0.746 = 74.6%, not 74.5%. Minor rounding inconsistency between Figure 1 caption and the body-quoted volume fractions.

### [P5-Min15] — §VI A item c filament-bright fCW recomputation
With n=416,701 and σ=−2.80, fCW = 0.5 + (−2.80)/(2·√416701) = 0.4978. The implied filament-bright nCW = 207,464 — but the parent filament class only has 203,261 CW galaxies (Table II). nCW (filament bright) cannot exceed nCW (filament total). This is downstream of [P5-E13] but worth flagging as a separate inconsistency point.

### [P5-Min16] — Appendix B and Reproducibility Checklist reference unnamed repository
**Appendix B and reproducibility checklist, page 19.** Both refer to "companion data repository" multiple times but provide no URL, DOI, GitHub identifier, or Zenodo accession. The HuggingFace catalog ID is given (bamfai/galaxy-chirality-catalog) but the analysis scripts have no locator. PRD requires identified, locator-bearing repository references for data/code availability statements.

### [P5-Min17] — "Deterministic seed: 20260515"
Reproducibility checklist. A seed of the form YYYYMMDD = 2026-05-15 is consistent with the paper's "Dated: June 2026" but is worth flagging in case the date was forward-dated to allow concurrent-arXiv citations [11,12] (see [P5-E2] from initial review).

### [P5-Min18] — Shamir 2022 comparison metric not equalized
**§XII C, page 17.** "Shamir 2022 reported a ∼2−4% large-scale asymmetry… Paper IV finds the catalog-wide CW-fraction offset is −0.26% and the full-sky dipole amplitude |A| < 0.32%, about an order of magnitude smaller than the Shamir 2022 amplitude." The "2–4%" is Shamir's signed N-vs-S CW-CCW asymmetry on a directional axis; the 0.26%/0.32% are monopole and dipole amplitudes respectively. These are different statistics; "an order of magnitude smaller" requires equalizing the metric. **Recommendation:** Quote the dipole-amplitude-equivalent of Shamir's signal, or note that the comparison is metric-dependent.

---

## NEW NOTE-LEVEL findings

### [P5-N1] — §X ASTRA argmax class fractions sum to 100.1%
"11.9% void / 31.7% sheet / 35.2% filament / 21.3% knot" sums to 100.1% — rounding artifact, harmless but worth a typographical note.

### [P5-N2] — §VIII E "no void coverage" residual interpretation is rhetorical
The σ = −4.75 in the 0-voids/pixel bin minus monopole prediction −3.20 leaves a residual of −1.55σ. The text states this is "consistent with an imaging-leg systematic at the ∼1σ level". A 1.55σ residual without an independent confirmation channel is descriptive, not load-bearing; the framing "consistent with" should be paired with the actual 1.55σ p-value (~0.12) for transparency.

### [P5-N3] — Eq. (1) implicit assumption of fCW ≈ 0.5
The formula σpred = 2·∆fCW·√N derives from σ = (f − 0.5)/(0.5/√N) under the Bernoulli null variance p(1−p)/N = 0.25/N. At fCW = 0.4972 the true binomial variance is 0.24999/N rather than 0.25/N, a 0.005% effect — negligible. But the formula does assume the population is well-modeled by Bernoulli(0.5); under the alternative fCW ≠ 0.5 the correct denominator would be √(p(1-p)/N), not 0.5/√N. The distinction is numerically irrelevant here but is a hidden methodological choice. **Recommendation:** State the Bernoulli-null variance assumption explicitly where Eq. (1) is introduced.

---

## Summary of fresh-eyes pass

The most consequential new findings are:
- **[P5-E12]** — The Table II / abstract sample-size mismatch (812,793 vs 791,635) is a load-bearing presentation inconsistency.
- **[P5-E13]** — The §VI A item-c filament bright+dark sum exceeds the filament total, undermining the 3.4σ sign-flip finding.
- **[P5-E14]** — A Bonferroni threshold is mis-computed in §VII A.
- **[P5-M13]** — The Phase-2 sweep largest-σ cell references a sample size (3.7M) that cannot exist in the catalog.
- **[P5-M16]** — The §VIII F per-pixel σ-distribution std of 1.184 is ~11σ from unity, not "within finite-pixel fluctuation" as claimed.

Combined with the initial review's findings, my recommendation moves from "major revision" to "reject with invitation to resubmit after the load-bearing sample-size and arithmetic inconsistencies (E12, E13, E14, M13, M16) are resolved, and after the unpublished companion Paper IV (E1) is in citable form."