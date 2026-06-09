# P5 auto-2026-06-08_1737pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `claude-opus-4-7` [FALLBACK to Claude]
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 315.2s

---

# Meta-Review of Paper P5

I have audited the manuscript against the union of the five prior reviews and looked specifically for issues that systematically slipped past all of them. Below are findings that NONE of Reviews 1–5 caught.

---

## NEW ESSENTIAL findings

### P5-META-E1. Table II range (1.98 pp) and Phase 2 canonical cell (0.165 pp) report different "ranges" for the SAME hyperparameters
**Section:** Table II (p. 5) vs Table VI (p. 8), Phase 2 cell (Rs = 25 Mpc/h, λth = 0)
**Why missed:** Reviewers attacked each table on its own merits; none compared the canonical cells of the two tables against each other.
**Problem:** Table II (canonical V-Web at Rs = 25, λth = 0) reports CW fractions {0.4836, 0.5034, 0.4980, 0.4963} with range = 0.5034 − 0.4836 = **0.0198 (1.98 pp)**. Table VI Phase 2 sweep at the SAME (Rs = 25, λth = 0) reports range = **0.165 pp** — an order of magnitude smaller. The filament−cluster difference alone is 0.4980 − 0.4963 = 0.17 pp, which matches Phase 2's 0.165 pp almost exactly. The Phase 2 sweep appears to silently drop the void and wall classes from the "range across four classes" statistic, yet §VII and the abstract both explicitly claim "the per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points." Either (a) the Phase 2 "range" computes over only 2 classes despite claiming 4, or (b) Phase 2 uses a different sample/weighting than canonical, in which case the canonical cell is not in fact reproduced. Either way, the Phase 2 robustness statement — quoted in the abstract — does not survive a direct check against Table II.
**Required fix:** Print the full per-cell {void, wall, filament, cluster} fCW table for all 9 sweep cells. Confirm that the canonical (25, 0) cell reproduces Table II. If "range" is implicitly restricted to high-n classes, say so explicitly in the abstract and §VII.

### P5-META-E2. Reference monopole used in σpred is inconsistent with the matched-subsample's actual catalog mean
**Section:** Eq. (1) p. 4; Tables III, IV (pp. 6–7); §VIII F (pp. 12–13).
**Why missed:** Reviewers focused on whether Δf = −0.0026 is from an unpublished source (R1, R3, R5); none recomputed it on the matched subsample.
**Problem:** From Table I: nCW = 393,592 of N = 791,635 ⇒ fCW = 0.49718, i.e., Δf_subsample = **−0.00282**. The paper uses Paper IV's catalog-wide value Δf = −0.0026 throughout for σpred (Tables III, IV, Fig. 3, §VI A interpretation, §VII A). Section §VIII F acknowledges in passing that the matched-subsample monopole is "∼8% larger" than the Paper IV value but does NOT propagate this correction backwards. The σpred values in Table III are computed with the wrong Δf; at N = 158,327 per quintile this shifts σpred by ≈ 0.16, which propagates into the per-quintile residuals. More importantly: σpred is being used to test whether residuals are environmental, but it is anchored on the wrong (external) monopole, not on the local null. The correct test is σ_pred = 2 Δf_subsample √N, not 2 Δf_PaperIV √N.
**Required fix:** Recompute every σpred and |σobs − σpred| using the matched-subsample-internal Δf = −0.00282 ± (binomial). Re-derive the Bonferroni passes; quintile 3 currently quoted at |σobs − σpred| = 1.87 will move.

### P5-META-E3. Global look-elsewhere multiplicity is uncounted across the analysis tree
**Section:** §V A (p. 4), §V B (p. 5) "Multiplicity bookkeeping."
**Why missed:** R1, R3, R5 criticized the post-hoc primary designation but none added up the total number of tests performed.
**Problem:** The paper applies Bonferroni only within individual scans (Bonferroni-5 for density quintiles, Bonferroni-4 for V-Web classes, Bonferroni-9 for Phase 2 cells, Bonferroni-1054 for HEALPix at NSIDE = 16). But the analysis tree contains: 4 V-Web classes × 9 Phase 2 cells × 5 density quintiles × 4 redshift quartiles × 4 target programs × 3 NSIDE choices × 3 acceptance radii × 3 confidence thresholds × 5 DESIVAST estimators × 4 Tempel classes × 3 ASTRA classifiers × 4 HEALPix void-density bins ≈ **tens of thousands of effective comparisons**. The 3.4σ filament bright/dark sign-flip — flagged in the abstract as "the strongest single residual structure" — has not been corrected against this full tree. A correct global LEE would suppress it well below 2σ. The "Multiplicity bookkeeping" paragraph treats only the 5 DESIVAST estimators as a family; it does not address the secondary tree.
**Required fix:** Either (a) tabulate the full set of tests and apply a global LEE correction (FDR or Bonferroni), or (b) demote the 3.4σ sign-flip to a hypothesis-generating observation and remove its prominence from the abstract.

### P5-META-E4. QSO targets in the matched catalog receive V-Web class labels from a tidal field that excluded QSOs
**Section:** Table I (p. 3) shows SPECTYPE QSO = 17,180 in matched primary; §IV A step 1 (p. 3) restricts V-Web parent to SPECTYPE = GALAXY only.
**Why missed:** R2 (P5-m4) flagged the QSO/GALAXY filtering mismatch as a wording inconsistency; nobody traced its statistical consequence.
**Problem:** 17,180 QSOs (≈ 2.2% of chirality-relevant spirals — actually most QSOs are not "spirals" so this is a strange match, but they remain in the table) are cross-matched to environment labels derived from a density field they did not contribute to. The same QSOs are presumably present in the V-Web class assignments propagated through Tables II, III, IV. The fraction is small but non-zero, and at high z the QSO/galaxy ratio rises so the per-class systematic is z-dependent.
**Required fix:** Either remove QSO spectra from the matched catalog before V-Web class assignment, or include them in the V-Web parent. Document which choice and recompute headline numbers.

---

## NEW MAJOR findings

### P5-META-M1. Matched spirals at z > 2 receive V-Web labels by NN extrapolation outside the tidal-field domain
**Section:** §III B (z ≤ 4 acceptance), §IV A step 1 (V-Web parent restricted to 0.01 ≤ z ≤ 2.0), Table I (z_max = 3.83).
**Why missed:** Reviewers focused on the z = 3.83 cap as a selection-validity issue, not as a tidal-field-domain issue.
**Problem:** The V-Web cube is built on 0.01 ≤ z ≤ 2.0 (per step 1, p. 3). Matched spirals span 0.01 ≤ z ≤ 3.83 (Table I). Galaxies at z > 2 are outside the V-Web tidal-field domain. Step 12 says "NN-interpolate the per-cell label to each galaxy" — for z > 2 galaxies this presumably picks up edge cells, producing class assignments that have no physical meaning. The number of such galaxies is not reported.
**Required fix:** Cut matched spirals at z ≤ 2.0 to match the V-Web parent or extend the V-Web cube. Document how many were silently extrapolated and whether they cluster in any single V-Web class.

### P5-META-M2. DESIVAST point-in-sphere uses 101,863 INTERIOR holes, not the 3,765 MAXIMAL voids — overlapping holes inflate void membership
**Section:** §VIII A (p. 10): "testing point-in-sphere membership against all 101,863 holes."
**Why missed:** R2 (P5-m5, P5-m12) asked about VoidFinder hole radii; no reviewer noticed the methodology question of interior vs. maximal.
**Problem:** Each of the 3,765 maximal voids comprises ~27 interior holes (101,863 / 3,765). Interior holes overlap inside a maximal void. The "in any of 101,863 holes" test is geometrically equivalent to "in the union of maximal voids" only if the holes' union exactly tiles each maximal void, which is the construction of VoidFinder. Fine. But the membership test is then NOT independent across holes, and the chosen k = 20 NN bound is based on hole radius, not maximal-void radius. A galaxy near the boundary of a maximal void may be assigned to multiple overlapping interior holes. The fCW of n_void = 56,981 is therefore computed by a methodology distinct from the maximal-void definition used in the HEALPix stratification (§VIII E). The two paths in §VIII are not parallel.
**Required fix:** Reproduce §VIII B using the 3,765 maximal-void effective-radius spheres only. Document whether n_void changes and whether ΔfCW ≈ 0.0007 survives.

### P5-META-M3. Tempel multiplicity → V-Web class mapping is dimensionally inappropriate; the "concordance" comparison is fundamentally apples-to-oranges
**Section:** §IX A (pp. 13–14).
**Why missed:** R1, R2 flagged the 0.026 pp vs 0.02 pp arithmetic; nobody questioned the underlying mapping's validity.
**Problem:** Tempel multiplicity (galaxy count in a FoF group) is a richness statistic that scales with halo mass and observational sensitivity. V-Web class is a deterministic Tidal-eigenvalue-count statistic. The two have no monotone bijection. The mapping {multiplicity = 1 → void, [2,5) → wall, [5,20) → filament, ≥20 → cluster} is a guess. The "concordance" 0.026 pp on the filament class — even at face value — measures CW fractions in two different selections, not the same physical environment. It cannot validate the V-Web classifier; it merely shows that two unrelated selections of ~filament-like galaxies have similar parity. The Tempel cross-check should be presented as a one-sided null check (do CW fractions exceed 0.5? no), not as a classifier-concordance validation.
**Required fix:** Rewrite §IX A to drop the concordance framing. State only that an independent (FoF) selection returns no |σ| > 3 environment-conditional chirality signal.

### P5-META-M4. Cross-match duplicate resolution discards label-disagreement information
**Section:** §III C (p. 3): "Duplicates on the chirality side are resolved by nearest-separation winner."
**Why missed:** Reviewers checked the duplicate count (2,349,908 → 2,232,212 = 117,696 drops, 5.0%); none asked whether the duplicates had consistent CW/CCW labels.
**Problem:** 117,696 duplicate matches were dropped. If a duplicate pair had {CW, CCW} disagreeing labels, the nearest-separation winner choice produces a biased fCW. The disagreement rate at 117k duplicates is presumably small but is a direct measure of catalog noise. Not reported. If e.g. 5% of duplicates disagree, the catalog's effective per-galaxy reliability is ≤ 97.5%, which sets a noise floor independent of the binomial uncertainty.
**Required fix:** Report (i) the fraction of duplicates with disagreeing chirality labels, (ii) the change in fCW under alternative dedup rules (highest-confidence winner, random winner, both-discarded), and (iii) whether the 0.4972 catalog monopole is invariant under those choices.

### P5-META-M5. Cloud-in-Cell deposit with no n(z) selection weight creates artificial radial-shell density spikes at LRG/ELG/QSO redshifts
**Section:** §IV A steps 4–6 (p. 3).
**Why missed:** R2 (P5-E6) flagged the absence of selection-function correction in general; nobody quantified the specific shell-structure problem.
**Problem:** DESI's BGS / LRG / ELG / QSO programs each have distinct redshift selection peaks (~0.2, ~0.8, ~1.2, ~1.5). Without an n(z)-corrected ρ̄(z), the CIC deposit places galaxy "shells" at each tracer's peak. After Gaussian smoothing at Rs = 25 Mpc/h, these shells appear as concentric thick spherical density peaks. The tidal field gradient is then dominated by line-of-sight artifacts, not by transverse cosmic structure. This biases the V-Web class assignment globally — not just at the survey edge — and explains why the V-Web cluster class concentrates 98.9% bright (the BGS shell) while the matched-spiral-overall is 97.8% bright. The "survey-shell systematic" the paper attributes only to void-class edge effects is in fact pervasive.
**Required fix:** Reconstruct δ with FKP-like n(z) weighting (use random catalogs) and rerun. If unfeasible, demote V-Web to a purely illustrative diagnostic.

---

## NEW MINOR findings

### P5-META-m1. Phase 2 sweep n = 3,696,152 (filament at Rs = 10, λth = 0) is the entire parent V-Web sample, not the chirality-relevant subsample — confirming the sweep does NOT compute fCW on matched spirals
**Section:** §VII (p. 8): "n = 3,696,152."
**Why missed:** R1 (P5-E3) flagged the number as impossible on 791,635; no reviewer realized this confirms the sweep silently uses the 14.6 M parent — which has no chirality labels at all.
**Problem:** The 14.6 M parent doesn't carry CW/CCW labels. So the σ = 11.32 value cannot be a fCW deviation from 0.5 on 3.7 M objects. Either (a) the sweep computes σ on a quantity other than fCW (and we are not told what), or (b) it cross-matches at each cell back into 791,635 and the n = 3,696,152 is a typo. Combined with P5-META-E1, this confirms the Phase 2 sweep methodology is undocumented to the point of being unreproducible.

### P5-META-m2. Deterministic seed 20260515 is a future calendar date used in the analysis pipeline
**Section:** Reproducibility checklist (p. 19): "Deterministic seed: 20260515."
**Why missed:** R3, R4 caught future arXiv dates but not this seed.
**Problem:** Pipeline seeds frequently embed run dates as integers, but 2026-05-15 post-dates the alleged submission date of June 2026 only by a month, suggesting the analysis was run with a fixed-but-self-referential ID. It signals the same future-dating problem propagated into the configuration.
**Required fix:** Replace with a neutral integer seed.

### P5-META-m3. Figure 1 percentages do not arithmetically sum to claim in caption
**Section:** Fig. 1 caption (p. 4).
**Why missed:** R1 (P5-mn1) noted 74.5 vs 74.6 as cosmetic; meta-confirms the arithmetic.
**Problem:** 41.3 + 33.3 = 74.6, not 74.5. The Cluster + Void = 25.4%, so by complement the wall+filament must be 74.6%. The figure also shows numbers consistent with {24.4, 41.3, 33.3, 1.0} = 100.0%.

### P5-META-m4. The matched z-acceptance radius sensitivity figures monotonically grow with radius, showing the 1″ floor is not a saturating choice
**Section:** §III D (p. 3): "{2.34, 2.35, 2.37, 2.39, 2.44}×10⁶."
**Why missed:** Reviewers accepted "≤4% band" as adequate; none noted that monotone growth without saturation means physically distinct objects are being added.
**Problem:** A saturated cross-match would show {a, a, a, a, a}. Monotone growth means each radius step adds new physical objects, not residual associations of the same galaxy. At 5″, 4% of the catalog is mis-associated. The headline fCW is therefore noise-contaminated at the ≤4% level even at the 1″ floor.
**Required fix:** Cite the local angular density of spirals at the catalog's r ≤ 17.8 cut to demonstrate that 1″ is below the chance-association threshold.

### P5-META-m5. The TTA-equivariant classifier is asserted to remove parity bias by construction, yet imports a −0.0026 residual whose existence contradicts equivariance
**Section:** §II (p. 2): "post-test-time-augmentation equivariant classifier." Imports Δf = −0.0026 as monopole.
**Why missed:** Reviewers (R1, R3, R5) attacked dependence on Paper IV for the value of Δf; nobody noted the theoretical inconsistency.
**Problem:** If TTA enforces Z₂ equivariance, fCW is identically 0.5 on each mirror-pair. The −0.0026 residual proves TTA does NOT achieve true equivariance. The paper treats this residual as "classifier bias" then uses it as a noise floor without questioning why an equivariant classifier has it. Likely cause: the classifier is equivariant on individual mirror-pair predictions, but the test-set's CW vs CCW priors are unequal because non-equivariant pre-augmentation features (e.g. seeing PSF asymmetry) leak through.
**Required fix:** Explicitly state in §II that "equivariant" here means architecture-level equivariance only, not output equivariance. Paper IV must demonstrate that the −0.0026 is constant under sub-samples.

---

## NEW NIT

### P5-META-N1. The Pearson r = +0.006 at p = 0.88 (§VIII F) is reported without power-to-detect
**Section:** §VIII F (p. 13).
**Why missed:** R1 (P5-M5) flagged absence of power; meta confirms that at n_pix = 727 the 95% upper bound on |r| is ≈ 0.073, which means correlations up to that level remain compatible with the null. The "indistinguishable from zero" claim should bracket the upper bound.

---

## Meta-review recommendation
**REJECT**

Across the six reviews, the union contains roughly **15 ESSENTIAL findings** (E1–E11 from R1; E1–E8 from R2; E1–E3 from R3; E1–E2 from R4; E1–E9 from R5; plus 4 new META-Es), with substantial overlap on the post-hoc primary-path designation, Paper IV dependency, internal "P5" tag leakage, multiple arithmetic contradictions in the bright/dark and Tempel rows, and now (newly identified here) a direct disagreement between Table II and the Phase 2 sweep at the same canonical (Rs, λth). The blocker count after de-duplication is ≈ 18, of which at least 4 (Paper IV dependency, post-hoc primary, Phase 2 vs Table II inconsistency, global look-elsewhere) are independently sufficient to require a full rewrite. My confidence that this paper survives external (non-bigbounce) peer review at PRD in its current form is **below 5%**: the paper would be desk-rejected on a combination of future dates, "in preparation" load-bearing citations, internal-tag leakage, and at least one demonstrable internal arithmetic contradiction visible without recomputation. Even if all surface issues were fixed, the unaddressed methodological deficiencies (no selection-function correction, no global LEE correction, redshift-space tidal field with no reconstruction, post-hoc primary designation) would individually justify rejection by a standard cosmology referee. The empirical content — that DESI DR1 shows no environment-dependent spiral chirality at ~10⁻³ precision — is plausibly correct and publishable, but the manuscript that defends it requires reconstruction, not revision.