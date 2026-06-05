# P5 auto-2026-06-05_1418pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (14753 chars)
**Wall time**: 477.6s

---

# Referee Report — Paper P5

## Overall assessment

This paper attempts to use a chirality catalog from a *non-peer-reviewed companion paper* (Paper IV) and re-projects it through a V-Web tidal-tensor classifier and a DESIVAST void cross-check to claim environment-independence of spiral handedness. The headline null is plausible, but the paper has *severe* problems: (i) the entire foundation rests on three unpublished companion papers by the same author; (ii) the abstract and body contain internal arithmetic inconsistencies; (iii) the paper acknowledges a 3.4σ bright/dark sign-flip and an unresolved cluster −4.66σ deviation, then dismisses both without sufficient evidence; (iv) the multiplicity of tests is enormous and no pre-registration exists; (v) the manuscript is heavily padded with secondary diagnostics, narrative repetition, and post-hoc justification; (vi) several references appear to be future-dated. Length (20 pages) is roughly 2× what the science actually contains.

---

## ESSENTIAL findings

### P5-E1 — Foundation rests on unpublished, non-peer-reviewed companion papers (multiple)
**Sections II, XII; references [3], [4]; pp. 2, 17, 20.**
The chirality labels come entirely from "Paper IV [3] (companion work … not yet peer-reviewed)" and Paper II [4] is also "in preparation; manuscript in preparation," and an unnumbered "Paper III" is invoked in Sec. XII B with no reference. PRD cannot accept a paper whose central per-galaxy classification is sourced from a manuscript that does not yet exist publicly. The "0.4974 ± 0.000279" monopole, the ∆f_CW = −0.0026 systematic, and the dipole nulls quoted in Sec. II are all unverifiable.
**Required fix:** Paper IV must be posted to arXiv and accepted (or at least posted) before this submission is reviewable; alternatively, all Paper IV-derived inputs must be reproduced *in this paper* with the catalog construction, training, TTA procedure, and monopole derivation made standalone.

### P5-E2 — Internal arithmetic inconsistency between filament class totals and bright/dark decomposition
**Sec. VI A (Table II); Sec. VI D ("Filament-class within-class decomposition"); pp. 5, 7.**
Table II reports n_filament = 408,187. In Sec. VI D the filament tracer-program decomposition states "filament bright (n = 416,701) σ = −2.80 vs filament dark (n = 21,203) σ = +2.85." But 416,701 + 21,203 = 437,904 > 408,187 — impossible if the filament class has 408,187 galaxies. Furthermore, the paper claims the per-class bright/(bright+dark) ratio is 0.966 for filament; but 416,701/(416,701+21,203) = 0.9516, not 0.966. The numbers are internally inconsistent at least three different ways.
**Required fix:** Reconcile the filament class population across §VI A, §VI A.d, and §VI D, including the cluster bright/dark totals (cluster dark = 4,234 + ratio 0.989 implies cluster_bright ≈ 380,582 for a total of 384,816, but Table II says n_cluster = 397,505).

### P5-E3 — Abstract and body disagree on what is "no environment dependence"
**Abstract p. 1 vs Sec. VI A p. 5.**
Abstract states "no environment dependence above the sensitivity floor." Body reports cluster −4.66σ and filament −2.61σ deviations; the paper hand-waves these as the "−0.0026 catalog monopole leaking through," but the predicted σ_pred(cluster) = −3.28 vs observed −4.66 leaves a residual of 1.38σ, and the paper acknowledges in §VI A.d a 3.4σ bright-vs-dark filament sign-flip that "the current data do not allow us to cleanly partition between … selection-function-origin … and a residual target-program-conditioned astrophysical signal." A 3.4σ unresolved signal cannot be reconciled with an abstract that says "no environment dependence."
**Required fix:** Either (a) demonstrate the 3.4σ filament sign-flip is fully selection-function in origin with a quantitative model, or (b) re-write the abstract to acknowledge the residual.

### P5-E4 — Future-dated references that do not exist
**References [11], [12]; p. 20.**
[11] arXiv:2604.02463 and [12] arXiv:2604.01456 use the "26MM" prefix that would correspond to April 2026. The paper is dated June 4, 2026. These arXiv identifiers do not exist in the public arXiv at any normal review time. If they are genuine future papers, they cannot be cited as published; if they are placeholders, that is misrepresentation.
**Required fix:** Replace with real arXiv IDs and verify accessibility.

### P5-E5 — Multiplicity of tests is enormous, no pre-registration, and "primary path" is chosen *post hoc*
**Sec. V B p. 4–5.**
The paper itself admits: "a single a priori pre-registered analysis plan was not filed; the choice of which classifier to report as 'primary' is therefore made post-hoc." The tests include: 3 void algorithms × 2 zone definitions × 9 (R_s, λ_th) cells × 5 density quintiles × 3 HEALPix NSIDEs × 4 redshift quartiles × 4 density quartiles × 4 tracer programs × 5 classifiers (V-Web/Tempel/ASTRA/DESIVAST/T-Web). The Bonferroni-5 correction on DESIVAST estimators is wholly insufficient given the full forking-path budget. PRD requires either pre-registration or a proper false-discovery-rate accounting across the *full* tree of tests reported, not just the chosen primary subset.
**Required fix:** Either pre-register and re-run (the proper fix), or produce a comprehensive multiplicity accounting covering every test enumerated in the paper. Without this, the headline null is not statistically defensible at PRD standard.

### P5-E6 — Conflating σ-from-half values from different procedures without "not directly comparable" caveats
**Sec. VI A, Sec. VIII, Sec. IX A.**
The σ_from_half values are computed against three different null hypotheses without explicit caveats: against parity (0.5) in Table II, against parity in Tables VII/VIII (DESIVAST), and against the catalog monopole in Table X. The DESIVAST void σ = −1.71 and the V-Web void σ = −0.68 are reported side-by-side in the abstract as if directly comparable, even though they refer to different samples (z ≤ 0.24 vs full-z), different classifier bases, and the DESIVAST σ inherits the −5σ catalog monopole at much larger n. A naive reader concludes "DESIVAST null is stronger," but the σ values are *not* directly comparable.
**Required fix:** At every juxtaposition of σ values, state explicitly whether they are computed against the same null and at the same N; flag the catalog-monopole inheritance for the DESIVAST σ.

---

## MAJOR findings

### P5-M1 — Cluster −4.66σ is not satisfactorily attributed to the monopole
**Sec. VI A, p. 5.**
σ_pred = −3.28; σ_obs = −4.66; residual = 1.38σ. The paper says "within order-unity of observation" and moves on. But Sec. VI D shows cluster Q1+Q2 quartiles at σ = −3.07 and −3.42, with Q3 at −0.37 — this is not consistent with a uniform monopole leakage. The "boundary leakage from filament" hypothesis is asserted without a quantitative cross-bin leakage estimate.
**Fix:** Quantify the predicted leakage and demonstrate the residual is consistent with it.

### P5-M2 — DESIVAST cross-check is heavily caveated as "methodologically correlated"
**Abstract; Sec. VIII.**
The DESIVAST primary path is described in the abstract as the controlling constraint, but the abstract also admits "methodologically correlated by construction because they reuse the same matched-spiral subsample." Reusing the same labeled subsample across V-Web and DESIVAST means the two "independent" cross-checks are not actually independent measurements of the chirality monopole, only independent partitions. This should be more honestly framed.
**Fix:** Strengthen the language around correlation; acknowledge that DESIVAST cross-check is a *partition robustness* test, not an *independent* test.

### P5-M3 — V-Web RSD treatment is acknowledged inadequate but headline not appropriately weakened
**Sec. XIII (Limitations), p. 18.**
The paper concedes: "A quantitative RSD bound therefore requires a reconstructed-position re-classification cross-check (Zel'dovich or BAO reconstruction), not the scalar σ_v/(aH) comparison alone" and "we explicitly do not quantify the propagated uncertainty in the present paper." Yet the V-Web headline σ values are quoted to 2 decimals in the abstract and Table II, and the 0.22 pp Phase 2 max range is quoted as a robustness statistic. If RSD-induced anisotropic eigenvalue deformation is not quantified, the V-Web headline cannot be reported at sub-percent precision.
**Fix:** Either run the reconstructed-position re-classification, or downgrade the V-Web results to "approximate" with appropriate error bars.

### P5-M4 — The σ = +1.25 dark-sample null is taken as evidence of selection-function origin without justification
**Sec. VI A.b, p. 7.**
The argument "bright = −5.25σ, dark = +1.25σ → headline is selection-function" requires that a genuine astrophysical environmental signal would propagate identically through bright and dark samples. But the dark sample has different redshift coverage (z̄ = 0.255 vs 0.145), different target type composition (LRG/ELG/QSO vs BGS), and 50× fewer galaxies. The asymmetric statistical power alone makes this comparison weak. The paper then admits in §VI A.d that V-Web class and target program are *not* independent (χ² = 4932), undermining the entire selection-function inference.
**Fix:** A proper joint model or matched-sample comparison is needed; the current "bright drives all the signal" framing is statistical sleight-of-hand.

### P5-M5 — Phase 2 sensitivity sweep does not test what it claims
**Sec. VII, p. 8–10.**
The Phase 2 sweep reports per-cell *range* of f_CW across the four classes (0.22 pp max). This is not a sensitivity test of the headline conclusion; it is a test that the *spread between classes* does not change much. The headline claim is no environment dependence; the proper sensitivity test is whether the σ_obs − σ_pred residual per class survives across (R_s, λ_th). The paper acknowledges this obliquely ("we do not separately report per-cell σ_vs monopole tables for each of the nine sweep cells") and waves it away.
**Fix:** Report the per-cell σ_vs_monopole residual table for all nine cells.

### P5-M6 — Tempel cross-validation is misleadingly framed
**Sec. IX A; Fig. 7.**
"filament_like vs filament: 0.026 pp (✓ within spec)" is presented as the headline concordance, but the other three pairs disagree by 0.62, 0.66, 1.11 pp — all *above* the 0.2 pp "spec." The paper hand-waves this as "classifier-definition mismatch" but does not show the discrepancy is genuinely within counting statistics. Tempel covers only 588k SDSS DR10 galaxies with a 110k overlap, and uses richness rather than tidal-tensor — calling this "supporting" the V-Web result is generous.
**Fix:** Report a proper concordance test (e.g. a contingency χ² on class assignments) and remove the cherry-picked filament-only comparison from the abstract.

### P5-M7 — ASTRA EDR cross-validation has poor per-galaxy concordance but is reported as supporting
**Sec. X, p. 16–17.**
The paper notes that V-Web puts 0% of EDR-overlap spirals in void+wall while ASTRA argmax puts 43.6% there. Per-galaxy classifier disagreement is essentially total on the EDR overlap. The paper then claims "EDR overlap recovers the same null result under either classifier" — but this is because both classifiers recover the catalog monopole regardless of how they bin, not because they agree on environment.
**Fix:** Either downgrade the ASTRA section to a methodology footnote or perform a proper joint classification cross-validation.

### P5-M8 — Density-quintile residuals reported "below all Bonferroni thresholds" but the test is post-hoc
**Sec. VI C, p. 6.**
σ_obs vs σ_pred subtraction is performed *after* observing the maximum residual; the |σ_obs − σ_pred| = 1.87 quoted is the maximum of 5 residuals, not a pre-specified statistic. The "Bonferroni-5 threshold 3.09" applies to raw σ-from-half, not to monopole-subtracted residuals. The framing conflates two different tests.

### P5-M9 — The 8% monopole enhancement is buried
**Sec. VIII F, p. 12.**
The paper notes "∆f_CW^P5 ≈ −0.0028, ∼8% larger than the P4 catalog-mean" and dismisses it as "BGS-bright leg ... not an additional environmental signal." But this 8% enhancement is exactly the magnitude that would correspond to a genuine residual environmental signal, and the paper offers no quantitative test that the enhancement is purely selection-function.

### P5-M10 — Length is excessive for the contribution
**Whole paper.**
The paper is 20 pages plus appendices. The core scientific content (DESIVAST null at n = 56,981 with ∆f_CW = 0.0007, V-Web null with monopole subtraction) fits in 8–10 pages. The remaining 10+ pages are post-hoc diagnostics, narrative repetition (the "selection-function" interpretation appears in at least four sections), and an EFT appendix the paper itself disclaims as "not a derived constraint" and "schematic."
**Fix:** Cut to ~10 pages PRD format. Remove Appendix A (it adds nothing PRD would publish; the authors themselves admit it is not gauge-invariant and not derived from any cited literature). Consolidate the redundant tracer-program discussion.

### P5-M11 — Appendix A toy EFT mapping is mathematically incoherent and self-disclaimed
**Appendix A, p. 19.**
The operator L_parity ⊃ g_φ (∇_iφ)(∇^iρ/ρ_bg)(L̂·ẑ) (i) breaks rotational invariance (paper acknowledges), (ii) is not gauge-invariant (paper acknowledges), (iii) is "not contained in either [Alexander–Yunes] or [Lue–Wang–Kamionkowski]" (paper acknowledges), (iv) is described as "schematic" and "an order-of-magnitude guide" with "not a quantitative ALP-coupling exclusion." This appendix contributes no information.
**Fix:** Delete entirely.

---

## MINOR findings

### P5-N1 — Abstract "≳2σ on the binomial null" for void is confusing
**Abstract p. 1.**
The void σ_from_half = −0.68 in Table II, but abstract says "n = 428, ∼2σ on the binomial null." Likely refers to the binomial counting-statistics width (1/(2√N) ≈ 2.4 pp), not a deviation. Clarify.

### P5-N2 — "DESIVAST Three-Algorithm Test on 56,981 Void Spirals" overstates
**Title.**
56,981 is the VoidFinder count; the other two algorithms give 102,911 and 81,354. The title implies one number across three algorithms.

### P5-N3 — Table I separation values
"p50 separation 0.0066″, p99 0.30″" — verify these are derived; rare values that should have a histogram.

### P5-N4 — "Approximately uniform across redshift" claim
**Sec. VI D.a.**
Cluster z-quartile σ values range −1.73 to −3.14. A 1.4σ range is then called "approximately uniform." Soft.

### P5-N5 — Figure 3 axis labels mangled
**Fig. 3, p. 7.**
The left-panel x-axis label appears to be "Den ∈ [42, 1...]" partially overlapping with quintile labels Q1–Q5. Illegible in the rendered PDF.

### P5-N6 — Figure 6 Mollweide axes are unlabeled
**Fig. 6, p. 14.**
Both panels show axis ticks at 0.0–1.0 instead of RA/Dec. A Mollweide should show angular coordinates.

### P5-N7 — Repeated "BGS-selection-function-conditioned imaging-leg systematics"
This 8-word phrase appears at least 5 times verbatim across §VI A, §VI A.b, §VI A.c, §VIII E, and the abstract.

### P5-N8 — "supporting, not load-bearing" qualifier appears twice in figure 7 caption and §IX A
Stylistic redundancy.

### P5-N9 — Sec. V "deterministic-seeded NumPy default_rng (seed fixed in the pipeline config)" but Reproducibility Checklist says "Deterministic seed: 20260515"
Specify in main text.

### P5-N10 — Figure 1 caption volume fractions don't sum cleanly
{0.244, 0.413, 0.333, 0.010} sums to 1.000 ✓, but figure shows "Wall 41.3%, Filament 33.3%, Void 24.4%, Cluster 1.0%" with rounding that sums to 100.0 — OK, but caption gives "wall+filament fraction (74.5%)" while 41.3+33.3 = 74.6%.

### P5-N11 — Bibliography style inconsistency
[5–7] use "Mon. Not. Roy. Astron. Soc." but [9, 10] uses same with different formatting; minor.

### P5-N12 — "fNL = −35/8" in [4] title is unusual and undefined
Reader cannot evaluate the companion-paper claim.

### P5-N13 — "812,793 env-labeled spirals" vs "791,635 chirality-relevant" never properly reconciled
**Sec. VIII F p. 12.**
The "21,158-row excess" footnote is opaque. Why does the relaxed env-label cut admit 2.7% more spirals when the headline cut is described as a stricter filter on env-class? Explain.

### P5-N14 — "0/6 V-Web 'void' spirals fall inside any of the 101,863 DESIVAST VoidFinder holes" — n = 6 is too small to support the abstract claim
The abstract uses this 0/6 statistic as a *cross-check* of the V-Web vs DESIVAST disagreement. n = 6 has no statistical power to distinguish 0/6 from a chance event under any classifier-purity hypothesis.

### P5-N15 — Page count of references appears inflated by self-citations
3 of 13 references are author's own in-preparation companion papers.

---

## Reproducibility / data availability

### P5-N16 — "Companion data repository" is referenced repeatedly but never named
Every appendix item points to a "companion data repository" with no URL, DOI, or Zenodo handle. PRD requires a permanent identifier.

---

## Summary recommendation

**REJECT**

The paper cannot be accepted in its current form. The most serious problems are (i) the foundational chirality catalog is in an unpublished, not-yet-peer-reviewed companion paper, making the central claim externally unverifiable; (ii) internal arithmetic inconsistencies in the filament and cluster bright/dark decompositions (P5-E2) that directly affect the headline "no environment dependence" claim; (iii) an explicitly acknowledged 3.4σ residual bright/dark sign-flip that the abstract glosses; (iv) post-hoc selection of the "primary" analysis path with no pre-registration and no proper multiplicity accounting for the full forking-path tree; (v) future-dated references that cannot be verified; and (vi) excessive length with a Toy-EFT appendix the authors themselves disclaim as non-derived, non-covariant, and non-gauge-invariant. The core scientific finding (chirality null in DESI DR1 voids at n ≈ 57k) is potentially publishable in a much shorter paper, but only after Paper IV is independently posted and reviewed, the arithmetic is reconciled, and the multiplicity is properly bounded. Resubmission as a substantially rewritten manuscript would be appropriate.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — Paper P5 (Second-Pass Findings)

Fresh re-examination focused on arithmetic, internal cross-references, figure/body consistency, and stale numbers. Substantial new findings were uncovered, including a **catalog-level labeling error** that affects the headline table.

---

## NEW ESSENTIAL findings

### P5-E7 — Table II is computed on the wrong sample; abstract and §VI A both misattribute it
**Table I (p. 3); Table II (p. 5); abstract (p. 1); §VIII F (p. 12); conclusions §XV (p. 18).**
The abstract states "Per-class CW fractions **on the 791,635 chirality-relevant spirals** are…" and §VI A says "Table II reports CW fraction by cosmic-web class on the 791,635 chirality-relevant matched spirals." But:

- Sum of n across Table II rows: 428 + 6,673 + 408,187 + 397,505 = **812,793**, not 791,635.
- Sum of n_CW across Table II rows: 207 + 3,359 + 203,261 + 197,284 = **404,111**.
- 404,111 / 812,793 = **0.49719** — which §VIII F explicitly identifies as "the P5 matched-spiral catalog monopole f_CW^P5 = 0.4972 (−5.07σ on n = 812,793 env-labeled spirals)."

So Table II is **demonstrably on the 812,793-row env-labeled superset**, not on the 791,635 headline subsample. The 21,158-row mismatch is the same one §VIII F notes parenthetically. This means:
- the abstract per-class σ values (−2.61, −4.66, +0.55, −0.68) are computed on a *different sample* than the one named in the abstract;
- the conclusions section's "CW fractions per V-Web class on the 791,635 chirality-relevant matched spirals (canonical run) are {0.484, 0.503, 0.498, 0.496}" repeats the same misattribution.

This is not a rounding issue. It is the *headline table* citing the wrong N. The numerical values may or may not change much when computed on the actual 791,635 subsample, but PRD cannot accept a paper in which the headline table is attributed to a sample 2.7% smaller than the one used.
**Required fix:** Recompute Table II (and the abstract and conclusions per-class quotes) on the actual 791,635 sample, or correctly attribute the existing numbers to the 812,793 superset.

### P5-E8 — Filament-class "dark" count exceeds total dark-program count: impossible
**§VI A.b (p. 7); §VI A.c (p. 7).**
§VI A.b reports the tracer-program decomposition: "**dark** (LRG, ELG, QSO; **n = 14,782**, z̄ = 0.255)." This is the total dark-program count on the headline matched-spiral catalog.

§VI A.c then reports "**filament dark (n = 21,203)** σ = +2.85." The filament-class dark count **exceeds the total dark count by 6,421 galaxies**, which is arithmetically impossible.

Combined with the cluster-class dark count (§ Abstract and §VI A.d: "n_dark^cluster = 4,234"), filament + cluster alone give 21,203 + 4,234 = **25,437 dark galaxies**, against a total dark of 14,782. The minimum implied excess across just these two classes is 73% over the stated total.

This is the single most damaging internal contradiction in the paper because the **3.4σ bright-vs-dark filament sign-flip** highlighted in the abstract is computed from these numbers. If filament dark = 21,203 is wrong, the 3.4σ is unverifiable; if filament dark = 21,203 is right, the §VI A.b dark total is wrong. Either way, the abstract's "3.4σ filament sign-flip is flagged as a real diagnostic" claim rests on inconsistent inputs.
**Required fix:** Reconcile dark totals across §VI A.b, §VI A.c, §VI A.d, and the abstract. Recompute the bright/dark sign-flip σ on the corrected sample.

### P5-E9 — Filament bright/(bright+dark) ratio of 0.966 contradicts the filament bright (416,701) and dark (21,203) counts in the same subsection
**§VI A.c, §VI A.d (p. 7–8).**
§VI A.d states: "The per-V-Web-class bright/(bright+dark) ratio is {0.981, 0.962, 0.966, 0.989} across {void, wall, filament, cluster}." But:
- 416,701 / (416,701 + 21,203) = 0.9516, **not 0.966**.
- For the ratio to be 0.966, with bright = 416,701, the implied dark count is 14,690, not 21,203.

Either the bright count, the dark count, or the ratio is wrong. (The implied dark count 14,690 is suspiciously close to §VI A.b's total dark = 14,782, which suggests that the ratios were computed using the **stated dark total** as the per-class dark count — i.e. an error.)
**Required fix:** Recompute all four bright/(bright+dark) ratios on consistent per-class counts.

### P5-E10 — Phase 2 sweep cites filament n = 3,696,152, a number that does not appear anywhere else and cannot be reconciled with any sample defined in the paper
**§VII p. 8.**
"The largest single-cell |σ_from_half| across the entire sweep is 11.32 (**filament at R_s = 10, λ_th = 0, n = 3,696,152**)."

But:
- chirality-relevant matched-spiral sample = 791,635;
- env-labeled superset = 812,793;
- canonical filament n (Table II) = 408,187 at R_s = 25;
- in-mask 3D cells = 3,150,086.

3,696,152 is **9.1× the canonical filament count** at R_s = 25. A change of smoothing scale from 25 to 10 Mpc/h **cannot increase the count of chirality-labelled spirals classified as filament** by 9×, because the underlying labelled spiral count is fixed at ≤ 812,793; the filament *volume fraction* can shift by ~10–20%, not by ~900%.

The σ_pred ≈ 10 calculation in the text is self-consistent with N = 3.7M, so the number is being used internally; but it is incompatible with the rest of the paper's sample definitions. Either Phase 2 silently uses a different (and undocumented) sample (e.g. the entire 8.47M Paper IV catalog re-projected through V-Web — which would require photo-z for unmatched spirals and is methodologically distinct from the headline analysis), or 3.7M is a typo/stale number.
**Required fix:** State explicitly what sample Phase 2 operates on. If it differs from the headline matched-spiral catalog, the entire robustness conclusion of Phase 2 needs to be re-evaluated, because the Phase 2 sweep then is **not robustness against (R_s, λ_th) on the same sample** — it is robustness on a different (larger, photo-z?) sample.

---

## NEW MAJOR findings

### P5-M12 — ASTRA Table XII "range across four classes" is actually a range across two classes
**§X Table XII (p. 16).**
The body states (§X) that V-Web on the EDR-overlap subsample puts "essentially the entire sample into filament (31.7%) and cluster (68.3%), with only 3 spirals total in the V-Web void + wall classes." Table XII reports the f_CW range and max |σ| "filtered to classes with n ≥ 100."

With only 3 V-Web spirals across void+wall, the n ≥ 100 filter excludes both, so the V-Web "range across four classes" of 1.08 pp is **actually a range across two classes** (filament and cluster). The same likely applies to ASTRA-argmax (void 11.9% of 25,186 = 3,000 — passes; sheet, filament, knot all pass; OK 4 classes). But comparing V-Web's 2-class range to ASTRA's 4-class range as if they were the same statistic is methodologically incoherent.
**Required fix:** Report the actual class count contributing to each row of Table XII; do not compare a 2-class range to a 4-class range.

### P5-M13 — σ_pred(filament) quoted as −3.16 does not follow from ∆f_CW = −0.0026 and n = 408,187
**§VI A p. 5.**
The text says "predicting σ_pred from ∆f_CW = −0.0026 gives σ_pred(filament) ≈ −3.16 and σ_pred(cluster) ≈ −3.28." Applying Eq. (1):
- σ_pred(filament) = 2 · 0.0026 · √408,187 = **−3.32**, not −3.16.
- σ_pred(cluster) = 2 · 0.0026 · √397,505 = **−3.28** ✓.

The cluster prediction is correct but the filament prediction is off by ~0.16σ (5%). With ∆f = −0.0026 used consistently, the σ_pred values are 3.32 and 3.28, not 3.16 and 3.28. The discrepancy moves the "observed minus predicted" residual on the *highest-N* class — exactly where the test of monopole-subtraction is most sensitive. The asymmetric error suggests the filament σ_pred was hand-computed or copied from an earlier version with different ∆f.
**Required fix:** Recompute σ_pred consistently from a single ∆f value.

### P5-M14 — §VI A.d contingency-test sample size (811,609) is inconsistent with §VI A.b bright+dark sum (790,542)
**§VI A.b vs §VI A.d (p. 7–8).**
§VI A.b enumerates the matched-spiral tracer-program decomposition: bright (775,760) + dark (14,782) + backup (875) + other (218) = **791,635** ✓ matches headline. So bright + dark on the 791,635 sample = **790,542**.

§VI A.d states: "two-way contingency test (V-Web class × bright/dark, four-by-two on **n_bright+dark = 811,609 spirals**)" — 21,067 spirals more than the 791,635-sample bright+dark sum. This number is suspiciously close to the 21,158-row 812,793-vs-791,635 superset offset from §VIII F, suggesting §VI A.d is computed on the *superset* while §VI A.b is computed on the *headline subsample* — silently, without flagging the sample switch.
**Required fix:** Use a single sample throughout §VI A.

### P5-M15 — Phase 2 sweep claims hyperparameter-robustness on the 791,635 sample, but the largest-cell example uses n = 3.7M (see P5-E10), undermining the robustness claim
**§VII; §XV conclusions (p. 18).**
The conclusion: "The result is robust under nine (R_s, λ_th) Phase 2 sweep cells (max CW-fraction range 0.22 pp)" presupposes the same chirality-relevant sample is being repartitioned across the nine cells. If Phase 2 silently switches to a different (larger) sample at some or all cells (P5-E10), then the per-cell range "0.22 pp" is computed on a different statistic than the headline 1.98 pp range in Table II. The "robustness" claim is then ill-defined.
**Required fix:** clarify Phase 2 sample definition; re-state the robustness conclusion accordingly.

---

## NEW MINOR / NOMENCLATURE findings

### P5-N17 — "Maximum class-to-overall bright-fraction deviation 1.5 pp" should be 1.6 pp
**Abstract; §VI A.d.**
Overall bright/(bright+dark) ratio 0.978. Per-class ratios {0.981, 0.962, 0.966, 0.989}. |0.962 − 0.978| = **1.6 pp** (wall is the maximum deviator), not 1.5 pp. Off by one significant rounding step.

### P5-N18 — Fig. 7 caption cites 0.026 pp concordance while displaying values rounded to 4 decimals (0.4980 vs 0.4982 = 0.02 pp display)
**Fig. 7 (p. 16).**
The caption states the concordance is 0.026 pp; the values shown (rounded to 4 sig figs after the decimal) give 0.02 pp. The 0.026 pp value is computable from Table II + XI to 5+ decimals (0.49796 vs 0.49822 = 0.00026 = 0.026 pp) but the figure's labelling doesn't expose that precision. Either round the concordance value to match the display (0.02 pp) or expose one more decimal.

### P5-N19 — Sec. VI A.b lists tracer-program ratios on n=791,635 but per-class counts elsewhere (Sec. VI A.c) implicitly use n=812,793; the two are juxtaposed without flagging
**§VI A.b, §VI A.c.**
Same root cause as P5-E7/P5-M14; flagged separately because it propagates a "selection-function origin" argument that switches samples silently.

### P5-N20 — In §VIII E the "1–2" and "3–5" maximal-void HEALPix bins are not size-balanced and do not have stated bin-edge derivations
**Table IX p. 12.**
Bin boundaries (0, 1–2, 3–5, 6+) are stated post-hoc; there is no a priori bin-edge prescription, and these are not equal-count bins (19,247 vs 23,127 vs 258,060). The 6+ bin contains 13× more spirals than the 1–2 bin, suggesting the bin edges were chosen to produce a particular σ distribution. Pre-specify the bin-edge prescription or report the result over multiple binning choices.

### P5-N21 — Sec. §VIII E asserts the "asymmetry between the two bin residuals quantifies the sky-region-conditioned systematic" but residuals (−1.55σ, +0.60σ) are on different N values and different bin-construction populations
The two-residual juxtaposition treats −1.55 and +0.60 as comparable diagnostics of a single underlying systematic, but each is computed on a different sample (N = 378,511 vs 258,060) under different selection (mask edge vs void interior). The asymmetry could equally reflect bin-size-dependent variance rather than a sky-conditioned systematic. Quantitatively bound the alternative.

### P5-N22 — Reference [3] (Paper IV) is described in [3]'s entry as "in preparation; manuscript in preparation" — the phrase appears verbatim twice
Stylistic; trivially fixable.

### P5-N23 — Sec V/Reproducibility seed inconsistency
§V says "deterministic-seeded NumPy default_rng (seed fixed in the pipeline config)" with no value; Reproducibility Checklist says "Deterministic seed: 20260515" (15 May 2026), which is ~3 weeks before the paper date (4 June 2026), implying the entire analysis was finalized in 3 weeks. Either the date is wrong, or this is implausibly fast.

### P5-N24 — Tempel cross-validation overlap requires SDSS DR10 z ≤ 0.20 but matched-spiral z extends to 3.83
The overlap of 110,586 is reported but not decomposed; how many of the chirality-relevant 791,635 fall in the z ≤ 0.20 + Tempel footprint? Without this we cannot judge whether 110,586 is a high- or low-yield overlap, which affects how seriously to take the cross-validation.

---

## Reassessment of overall recommendation

The combination of:
- **P5-E7** (Table II citing the wrong sample — and this propagates to the abstract and conclusions),
- **P5-E8** (filament dark count exceeds total dark count — impossible),
- **P5-E9** (filament bright/dark ratio inconsistent with the per-class counts in the same subsection),
- **P5-E10** (Phase 2 filament n = 3.7M unexplained),
- **P5-M13** (σ_pred filament off by 5%),
- **P5-M14** (sample-size switch silently between §VI A.b and §VI A.d)

makes my initial REJECT recommendation **stronger, not weaker**. The paper has not merely structural problems (companion-paper foundation, multiplicity, post-hoc primary path) but **direct internal arithmetic contradictions** in the headline table, the headline abstract σ values, and the residual-analysis numbers that the paper itself relies on to defuse the cluster −4.66σ and filament bright/dark 3.4σ signals.

In particular, P5-E8 is fatal: the entire "BGS-selection-function origin" interpretation that the paper uses to neutralize its own 3.4σ filament sign-flip rests on filament-dark = 21,203, which **arithmetically cannot exist** on the 791,635 sample where the total dark count is 14,782. The author must either produce a corrected reconciliation or withdraw the BGS-origin interpretation — and in either case the abstract must be rewritten.

**Recommendation unchanged: REJECT.** A resubmission would require:
1. Paper IV publicly posted and reviewable.
2. A single consistent sample definition used throughout, with all per-class, per-program, and per-cell counts demonstrably summing to that sample.
3. Recomputation of Table II, abstract σ values, conclusion f_CW quotes, and all bright/dark decomposition σ values on the corrected sample.
4. Explicit pre-registration or full multiplicity accounting.
5. Length reduction to ≲ 10 PRD pages and removal of Appendix A.