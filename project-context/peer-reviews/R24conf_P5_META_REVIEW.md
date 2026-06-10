# P5 R24conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 304.4s

---

Meta-referee report (focus: blind spots across all five prior reviews)

Below are issues I found that none of the five reviewers explicitly caught. I concentrate on deep-chain, conditioning, comparability, and analysis-design details that are easy to miss but can move inferences if unaddressed.

ID: P5-META-E1
Severity: ESSENTIAL
Section + page: §IV.A (Algorithm), steps 1–4, p. 4; §VIII.F (parent reconciliation), p. 16
Why others missed it: Prior reviews discussed duplicates only at the join/analysis stage, not at the stage where the density field that drives the classifier is constructed.
Specific problem (quote the text):
- “Filter DESI DR1 zall … yields 14,622,283 galaxies.” (§IV.A.1)
- “…the V-Web environment table inherits one row per DESI zall survey–program coadd entry (14,622,283 rows over 14,100,704 unique TARGETIDs)…” (§VIII.F)
The T-Web density field (CIC deposit, steps 4–7) is built from the 14,622,283 “rows” rather than the ~14,100,704 unique TARGETIDs. That means repeat survey–program coadd rows for the same galaxy are counted multiple times in ρ and δ, subtly overweighting multiply-observed targets and potentially distorting the eigenvalue field near regions with more coadds.
Required fix:
- Rebuild the T-Web field with a unique-TARGETID parent (or weight each TARGETID’s repeated coadds by 1/ncoadd before deposit), and re-join the environments; report the change in per-class volumes and the chirality-by-class fCW. If negligible, state the bound; if not, adopt the deduplicated/weighted version as canonical.

ID: P5-META-M1
Severity: MAJOR
Section + page: §IV.A (Algorithm), steps 4–11, p. 4–5; §IX.A, p. 17–18
Why others missed it: Reviewers focused on redshift-shell corrections and boundary buffers but did not address angular completeness/tiling explicitly.
Specific problem (quote the text):
- The pipeline constructs δ on a masked cube (“survey-footprint mask by dilation of occupied cells…”) and later shows a z-shell correction and an “interior-buffer” excision. Nowhere is an angular selection function or spectroscopic tiling/completeness correction (e.g., DESI random catalogs or FKP-like weighting) applied when building δ.
Required fix:
- Add an angular completeness control: either (i) weight counts by the per-cell completeness estimated from DESI “RANDOMS” or a depth/tiling completeness map, or (ii) demonstrate via a re-run that applying such weighting leaves class volumes and fCW by class unchanged within quoted precision. Document this in one consolidated subsection.

ID: P5-META-M2
Severity: MAJOR
Section + page: Fig. 3 and Table II (row-level env-labeled parent), p. 6–7
Why others missed it: Reviewers checked σ and χ² arithmetic but not the appropriateness of Jeffreys CIs under duplication.
Specific problem (quote the text):
- “Bars show the observed fCW per class; black error bars are 95% Jeffreys binomial credible intervals.” (Fig. 3 caption)
But these intervals are drawn on the 812,793-row env-labeled parent, which includes 2.7% duplicate TARGETIDs. That violates the i.i.d. Bernoulli model underpinning the Jeffreys interval and makes the intervals slightly too narrow.
Required fix:
- Either (a) redraw Fig. 3 and any CIs on the 783,820 unique-TARGETID parent, or (b) inflate the interval widths by the (measured) design effect due to duplication and state both versions in the caption. Keep the homogeneity χ² on the unique-target table (you already report that test).

ID: P5-META-M3
Severity: MAJOR
Section + page: §V (Eq. 1), §VI.A, §VII/Table VI, §VIII.F/Table X
Why others missed it: They recommended using the matched-sample monopole but did not quantify its uncertainty’s impact on residual tests.
Specific problem (quote the text):
- “We explicitly compare each σfrom half against the Paper IV–predicted classifier-monopole offset σpred = 2·ΔfCW·√N…” (§V)
- “Replacing the fCW − 0.5 null with fCW − fP5CW gives the residual environment signal…” (§VIII.F)
All σpred and σvs-monopole residuals are treated as if the monopole reference were exact (either ΔfCW from Paper IV or fP5CW from this work). But fP5CW has finite uncertainty: se(fP5CW) ≈ √(0.25/Ntot) ≈ 0.00055 on N≈8.1×10^5, which propagates to an uncertainty in σpred for a class with N≈4×10^5 of δσpred ≈ 2·se(fP5)·√N ≈ 0.7σ. That is a non-negligible fraction of your reported “max |σobs − σpred| = 1.87” and should be folded into any formal interpretation.
Required fix:
- Propagate the uncertainty of the monopole reference (preferably fP5CW measured here) into σpred and σvs-monopole. Either report error bands on σpred and show that |σobs − σpred| remains < 2σ after this propagation, or include this uncertainty in the permutation framework by shuffling labels under a fixed total CW count equal to the observed (which you already do) and evaluating residuals relative to that randomization rather than a fixed σpred line.

ID: P5-META-M4
Severity: MAJOR
Section + page: §VII/Table VI (Phase-2 sweep), p. 11–12
Why others missed it: They checked pLEE per cell and the Rs=10 caveat, but not stratification or global multiplicity across scan families.
Specific problem (quote the text):
- “For each cell, the label-shuffle permutation null… returns pLEE = 0.13–0.56…”
The Phase-2 pLEE is run as a single-family max-stat per (Rs, λth) cell. However: (i) you do not stratify these shuffles by imaging leg and DESI program (as you correctly do for HEALPix), and (ii) across the entire study, multiple scan families are run (HEALPix at 3 NSIDEs, density quintiles, redshift, and the 9 hyperparameter cells). Reporting only per-family LEE ignores the global multiplicity across families.
Required fix:
- Re-run the Phase-2 pLEE with label-shuffle stratified by imaging leg × program. In addition, provide a “global” max-stat p across all scan families (or at least across the 9 hyperparameter cells) so readers see the family-wise error under the union of tested configurations. If you prefer to keep families separate (reasonable), state explicitly that p-values are family-corrected, not globally corrected.

ID: P5-META-M5
Severity: MAJOR
Section + page: §VIII.B–§VIII.C (DESIVAST membership rules), p. 14–15
Why others missed it: They focused on RSD and the sphere vs watershed duality, not on VoidFinder membership fidelity specifically.
Specific problem (quote the text):
- “Performing a point-in-sphere test against all 101,863 DESIVAST VoidFinder hole spheres… returns nvoid = 56,981…”
VoidFinder voids are constructed from sets of overlapping maximal holes aggregated into voids; “inside any hole” is a permissive criterion that can differ from “inside a void” and can over- or under-count edge/overlap regions relative to the catalog’s intended geometry. You do use catalog-native GALZONE membership for V2 (watershed), but not an equivalent VoidFinder-native membership.
Required fix:
- Where possible, use the catalog’s own VoidFinder per-galaxy membership (if available), or at least quantify the difference between “inside-any-hole” and the catalog’s interior-void mask using the DESIVAST per-void polygons/spheres. Report how fCW and ∆fCW change under these two VoidFinder definitions, as you did for V2 (GALZONE).

ID: P5-META-M6
Severity: MAJOR
Section + page: §IX.A (z-shell correction), p. 17
Why others missed it: They asked for per-shell counts but not for sensitivity to the topmost shell-lumping.
Specific problem (quote the text):
- “21 thin redshift shells (Δz=0.05 for z<0.5, Δz=0.1 for 0.5≤z<1.5, one merged 1.5–1.7 shell into which the sparse 1.7<z≤2.0 tail is also clamped, so the top shell effectively covers 1.5≤z≤2.0)…”
Lumping 1.7<z≤2.0 objects into the 1.5–1.7 shell alters both the top-shell mean and the T-Web labels for those galaxies; the population there is small but non-zero and systematics-weighted (LRG/ELG-heavy). You do not test whether excluding 1.7<z≤2.0 entirely changes the environment fractions or fCW-by-class.
Required fix:
- Add a sensitivity run dropping 1.7<z≤2.0 from the T-Web build (or placing them into their own shell) and show that class volumes and the fCW-by-class null are unchanged within your quoted precision.

ID: P5-META-M7
Severity: MAJOR
Section + page: §X/Table XII (ASTRA), p. 21–22
Why others missed it: They accepted the entropy-weighted variance formula but did not check cross-class dependence.
Specific problem (quote the text):
- “each galaxy contributes Pclass fractional count and Pclass·⊮CW fractional CW count to each class, with sub-class variance Σi P_i^2/4 under the Bernoulli-0.5 null…”
This variance model assumes independence across objects (fine) and ignores cross-class dependence within the same object (the four Pclass sum to 1). When you report “max |σ| vs 1/2” for ASTRA, the within-object negative correlation between class-weights slightly alters the effective variance structure if you compare classes or combine them. It’s minor but becomes relevant when quoting “max |σ| vs 1/2” across four classes as a family statistic.
Required fix:
- State this independence approximation explicitly and, if feasible, validate it via a quick Monte Carlo using the actual per-object {Pvoid,Psheet,Pfilament,Pknot} to confirm that the classwise variance used for σ is accurate at the 0.1–0.2σ level you care about.

ID: P5-META-m1
Severity: MINOR
Section + page: §VI.C (projected density quintiles), p. 8–9
Why others missed it: They focused on endogeneity (which you checked), not boundary definition.
Specific problem (quote the text):
- You compute k=5 NN density quintiles on the full-sky projected sphere. Because the DESI footprint is a highly structured mask, the quintile boundaries are defined on the masked sky; a nontrivial fraction of galaxies near mask edges have upward-biased kNN distances. While you show an “exogenous” redefinition using the full matched-primary set, you do not include a mask-edge buffer (analogous to the T-Web interior buffer).
Required fix:
- Recompute the kNN density quintiles after dropping galaxies within a fixed angular buffer of the mask edge (e.g., the 95th-percentile kNN distance for the lowest quintile), or show numerically that including such a buffer does not materially change Fig. 5.

ID: P5-META-m2
Severity: MINOR
Section + page: §V (Permutation null), p. 5
Why others missed it: They accepted the deterministic seed and null outline.
Specific problem (quote the text):
- “Both nulls draw NMC=1000 independent permutations from a deterministic-seeded NumPy default rng (seed fixed in the pipeline config)…”
Using the same fixed seed across multiple, distinct permutation families (HEALPix, density, redshift, Phase‑2) can accidentally induce correlations across reported p-values if the code initializes the RNG identically per run. You do mention re-draws with distinct streams in one place, but not as a global practice.
Required fix:
- State (and enforce) that each permutation family uses an independent RNG stream/seed, and archive the seeds per-family. If this was already the case, say so once in §V and remove per-section ad hoc statements.

ID: P5-META-N1
Severity: NIT
Section + page: §VIII.F last paragraph (per-pixel σ distribution), p. 16
Why others missed it: They accepted the “near shot-noise residual” phrasing.
Specific problem (quote the text):
- You report per-pixel σ distribution (NSIDE=32, ≥200 spirals) with std=1.050. This is close to 1 but not exact; a one-sentence note that the slight >1 value is consistent with heteroscedastic σ and residual selection-function structure would preempt over-interpretation.
Required fix:
- Add a parenthetical: “std=1.050 is consistent with pixel-to-pixel N variation (heteroscedastic σ) and small residual selection-function structure; not evidence for non-shot-noise tails.”

Meta-review recommendation
MAJOR REVISIONS

Rationale: The science result (no environment-dependent chirality within DR1 sensitivity; robust DESIVAST-anchored void null) appears sound, but there are analysis-design gaps that affect the environmental labels and uncertainty calibration: (i) duplicates entering the T-Web density field, (ii) absence of an angular completeness/tiling correction in δ, (iii) CIs drawn on a non-i.i.d. row-level parent, and (iv) unpropagated uncertainty in the monopole reference when quoting σ vs. σpred and “max |σobs − σpred|.” These are fixable but require reruns or added sensitivity studies. Phase‑2 p-values also need leg×program stratification and a brief global-multiplicity note.

Union of all six reviews: blocker count and survivability
Combining all six reports, there are multiple ESSENTIAL/MAJOR items: dependency on an unpublished companion (others), missing bibliography (others), internal audit/draft language (others), T-Web density-field duplication (this review), lack of angular completeness weighting (this review), and uncertainty propagation for the monopole (this review). Addressing these will likely require a modest rebuild of the T-Web field and targeted re-analyses, plus substantial editorial cleanup. My confidence the paper would ultimately survive external peer review is moderate-to-high once these items are corrected: the null result is robustly supported by independent DESIVAST/Tempel/ASTRA cross-checks, and the requested fixes primarily improve label construction, uncertainty accounting, and presentation.