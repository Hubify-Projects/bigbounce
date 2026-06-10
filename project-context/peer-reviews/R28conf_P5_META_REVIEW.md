# P5 R28conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 542.5s

---

META-REVIEW (focus: blind spots none of the 5 referees caught)

P5-META-E1 (ESSENTIAL) — Misuse of a “2σ counting floor” to validate inter-class ranges
- Location: §VII.A Per-cell significance framework, p.13–14; Table VI caption; text: “the per-cell range stays within 1.01× the void-class 2σ counting floor 1/√nvoid… no (Rs, λth) cell shows an inter-class range that exceeds the counting noise of the class that produces it by more than 1%.”
- Why it slipped past others: Reviewers checked the permutation LEE p-values but did not audit the logic of comparing a four-bin range against a single-bin 2σ.
- Problem: The statistic being bounded (max range across four classes) is not distributed like 2×(1σ of a single bin). Under the null, the spread of multiple binomial estimates depends on all bin sizes via √(1/n_i+1/n_j) and the extremal distribution of max–min over K=4 bins; a single-bin 2σ yardstick is not a valid bound and can understate the expected range. The correct control is the empirical null of the range (or max-|σ|) under permutation, not a single-bin 2σ surrogate.
- Required fix: Drop the “within 1.01× the void 2σ floor” claim. Replace with an explicit MC calibration of the range statistic per (Rs, λth) cell: report the empirical mean/95th percentile of the range under the same label-shuffles already drawn for pLEE, and state where the observed range falls relative to that null. Keep the pLEE column as primary.

P5-META-M1 (MAJOR) — Pixel-level σ distribution: explanation of std>1 is not mathematically sound
- Location: §VIII.F, p.18; text: “per-pixel σvs monopole… std 1.050… The unit standard deviation… the mild excess over unity is consistent with pixel-to-pixel N variation (heteroscedastic σ)…”
- Why it slipped past others: Reviewers focused on permutation p-values and not on the stated rationale for overdispersion.
- Problem: If each pixel’s statistic is normalized by its own binomial standard error (you use 0.5/√N, or nearly identical √[p0(1−p0)/N]), then under the null each z is approximately N(0,1). A mixture of mean‑zero unit‑variance normals across heterogeneous N still has variance 1. Heteroscedastic N alone does not inflate the variance to 1.05. The stated rationale is incorrect; 1.05 suggests mild overdispersion or spatial correlation not captured by the simple independent-binomial model.
- Required fix: Quantify this with a label-shuffle ensemble: report the distribution of the sample std of per-pixel σ under permutation for the same pixel set. If 1.05 lies within the permutation envelope, say so; if not, acknowledge a small overdispersion and, if relevant, adjust sky-coherence tests using block- or pixel-cluster–robust errors or a spatially aware null.

P5-META-M2 (MAJOR) — Permutation nulls treat duplicate coadd rows as independent units
- Location: §V (Statistical Methods), §VI.A, §VI.E, multiple permutation-based results
- Why it slipped past others: Reviewers noted overlaps for bright/dark z-tests but not their impact on the permutation calibration itself.
- Problem: Label-shuffle and position-shuffle are run on the row-level env‑labeled parent (812,793 rows) that includes 2.7% duplicate TARGETIDs. These duplicates carry identical chirality labels and, occasionally, differing environment labels. Shuffling at the row level violates exchangeability and effectively gives duplicated objects more weight and/or creates correlated “blocks” that narrow the null distribution. This can miscalibrate pLEE and any MC-derived thresholds.
- Required fix: Recompute all permutation-based nulls on the unique‑TARGETID parent (783,820), or perform cluster‑wise shuffles that keep all rows of a given TARGETID together (or weight each TARGETID by 1/mi where mi is its multiplicity). Report whether pLEE and other MC diagnostics change.

P5-META-M3 (MAJOR) — RSD “FoG Monte Carlo” perturbs only galaxy positions but holds void geometry fixed
- Location: §VIII (RSD treatment for DESIVAST), p.14–15
- Why it slipped past others: Prior reviews asked for algorithmic clarity but not this specific modeling asymmetry.
- Problem: The DESIVAST void catalog is defined in redshift space. The FoG MC perturbs each spiral’s line-of-sight distance by ± Gaussian σv/(aH) while keeping published void centers/radii unchanged. This mixes coordinate frames and does not model the dominant effect that void boundaries themselves (defined from galaxy positions) shift under RSD. As a result, the reported ∆fCW stability under ±5 Mpc/h perturbations is not an RSD-robustness test of the binary void/non‑void classification: it is a stress test of membership to a fixed redshift‑space mask under extra noise.
- Required fix: Either (a) perform a group-compressed variant (FoG compression) and recompute membership against the same published voids, and/or (b) generate a perturbed galaxy field and rerun a minimal watershed/sphere-growing step locally (on a subvolume) to show that boundary motion at FoG scales does not induce |∆fCW| ≳ 0.002. Alternatively, clearly relabel the current experiment as a “fixed‑mask sensitivity check,” not an RSD robustness test.

P5-META-M4 (MAJOR) — Jeffreys CIs drawn on row-level data with duplicates; “design-effect” bound is not justified
- Location: Fig. 3 caption, p.7; text: “the 2.7% duplicate rows violate strict i.i.d., but the worst-case design-effect inflation of the interval widths is √(812,793/783,820)=1.018…”
- Why it slipped past others: Others flagged overlap issues for tests but not for the confidence intervals and their stated correction.
- Problem: Row-level CIs are computed as if rows are i.i.d. Bernoulli, but duplicated TARGETIDs introduce intracluster correlation (chirality labels are identical within a TARGETID; environment rows can differ for 79 cases). The ad hoc width inflation factor √(Nrows/Nunique) neither follows from a cluster-sampling design‑effect formula (1+(m−1)ρ) nor accounts for per‑class reweighting and cross‑class reallocations that duplicates can cause.
- Required fix: Report per-class fCW and Jeffreys CIs on the unique‑TARGETID sample as primary. If row-level numbers are retained (for consistency with joins), use either (i) per‑TARGETID weights 1/mi when forming counts, or (ii) a simple cluster bootstrap over TARGETIDs for CI estimation. Drop the √(Nrows/Nunique) design‑effect claim.

P5-META-M5 (MAJOR) — Tempel multiplicity→cosmic‑web mapping lacks validation and can bias “like‑for‑like” comparison
- Location: §IX.B, p.21–22; mapping bullets: multiplicity=1→“isolated(=void)”, 2–4→“small group(=wall)”, 5–19→“filament‑like”, ≥20→“cluster‑like”.
- Why it slipped past others: Reviewers accepted the coarse mapping without probing its impact.
- Problem: FoF group richness is not a validated proxy for T‑Web class on an object‑by‑object basis; the stated mapping can misclassify e.g., isolated galaxies embedded in sheets or filaments, and poor groups in filaments vs walls. The “like‑for‑like” filament concordance (0.29 pp) is reported without any quantitative check that the mapped bins correspond to similar tidal environments in the overlap region.
- Required fix: Provide evidence that the richness bins correlate with T‑Web class on the overlap (e.g., a small confusion matrix between Tempel richness bins and your T‑Web labels, or a density/eigenvalue signature per richness bin). Otherwise, present the Tempel comparison explicitly as a cross‑survey, different‑definition consistency check rather than a like‑for‑like test.

P5-META-M6 (MAJOR) — Conditioning embedded in permutation nulls is under‑specified
- Location: §V (Statistical Methods), p.5–6
- Why it slipped past others: Others criticized pre‑registration and family‑wise control but not this assumption.
- Problem: The label-shuffle null “fixes the total CW count at its observed value” and thus implicitly conditions on the catalog‑level monopole. That is consistent with testing environment‑independence “given the monopole,” but the paper also draws interpretive weight from raw σfrom‑half panels before explicitly stating this conditioning. The null as used is not the unconditional p=0.5 null.
- Required fix: State upfront that all permutation tests are conditional on the matched‑sample monopole (fixed number of CW labels), and that the unconditional p=0.5 null is examined only via analytic σfrom‑half displays. Where raw σfrom‑half is shown, add a sentence reminding the reader that the formal tests are conducted under the conditional permutation null.

P5-META-m1 (MINOR) — Minor unit clarity: “per-galaxy density covariate” notation and values
- Location: §IV.A step 12; §VI.D/Table IV, p.10; captions
- Why it slipped past others: This is a small presentation nit.
- Problem: The per-galaxy covariate is log10(1+δsmooth) (dimensionless), yet Table IV lists quartile means “ρ̄ = 1.55, 1.80, 2.01, 2.21” without repeating that these are means of log10(1+δ) (or of 1+δ). As written, the symbols ρ̄ and the numeric values look like linear overdensity factors and can be misread.
- Required fix: Clarify in Table IV (and first mention) that ρ̄ denotes the mean of 1+δsmooth (linear) or of log10(1+δsmooth), and keep notation consistent between text and table. If listing linear means, avoid overbars over ρ to prevent confusion with mass density.

P5-META-m2 (MINOR) — Internal consistency of “position-shuffle equals label-shuffle” claim with duplicates
- Location: §V, p.5–6
- Why it slipped past others: They focused on general null calibration, not equivalence.
- Problem: The statement “for the per-bin count statistics used in this paper the two are the same permutation null” is strictly true only if there are no duplicate labels or structural constraints. With duplicated TARGETIDs and class-correlated observation programs, position‑shuffles can induce slightly different nulls from label‑shuffles at the row level.
- Required fix: Soften to “induce very similar nulls at our binning resolution; we verified equivalence numerically,” or restrict permutations to unique‑TARGETIDs where the equivalence is exact by construction.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential/major blockers: (i) extensive in‑text version/audit prose and file paths; (ii) reliance on an unpublished catalog (Paper IV) and non‑standard/future‑dated citations; (iii) statistical misstatements (confidence-threshold σ; Bonferroni α; signed/absolute residual confusion); (iv) inconsistent terminology (T‑Web vs V‑Web); (v) overlaps/duplicates affecting tests; and (vi) the additional issues above (invalid “2σ floor” range argument; mis-explained pixel‑σ variance; permutation calibration with duplicates; RSD MC modeling asymmetry; row-level CI treatment; unvalidated Tempel mapping). My confidence that the core null will survive external peer review is reasonably high once these are addressed, but the blocker count is large and touches both presentation and methods. A thorough rewrite with corrected statistical framing, duplicate‑aware inference, and streamlined presentation is required before acceptance.