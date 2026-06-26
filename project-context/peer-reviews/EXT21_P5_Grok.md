# EXT21 P5 Grok — chat: https://grok.com/c/837045e7-29a1-403e-beff-4383b313600a

Referee Report: MNRAS-style (for MNRAS / PRD / JCAP consideration)
Paper: Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample
Author: Houston Golden
Date of report: 26 June 2026
Recommendation: MINOR REVISIONS

Summary

This is a careful, statistically rigorous null-result paper testing whether spiral-galaxy handedness (CW/CCW fraction) shows residual dependence on large-scale environment after the global classifier monopole offset established in Paper IV is accounted for. The primary analysis path uses the public DESIVAST DR1 BGS void catalog (three algorithms: VoidFinder + V2-REVOLVER + V2-VIDE) on the volume-limited z ≤ 0.24 matched-spiral subsample (n_void = 56,981), yielding |Δf_CW| ≲ 0.002 (null at |z_Δ| ≤ 1.25 across all five Bonferroni-5 estimators). Secondary T-Web tidal-tensor classification (Rs = 25 Mpc/h, λ_th = 0 default; Phase-2 sweep over nine (Rs, λ_th) cells) on the full matched sample (812,793 env-labeled rows covering 783,820 unique chirality-relevant spirals) returns an omnibus 4×2 homogeneity χ² null (p ≈ 0.31–0.39) and per-class residuals consistent with the catalog monopole after subtraction. Multiple orthogonal null tests (redshift, projected density, HEALPix sky position, within-class density stratification, tracer-program splits) and robustness checks (Tempel FoF overlap, ASTRA EDR, external T-Web literature overlay, RSD Monte-Carlo membership perturbation) are reported transparently. The paper explicitly declares the DESIVAST-anchored void test as primary (with pre-registration caveat) to bound garden-of-forking-paths concerns and scopes the result as a redshift-space statement providing an empirical upper bound for future bounce-chirality models.

The analysis is well-powered for the void test, statistically conservative, and reproducible in principle via the committed pipeline artifacts. No load-bearing claim lacks support, and no critical control is missing. The work is a valuable complement to Paper IV's global dipole null.

BLOCKERS
None.

MAJORS
None. (No unsupported load-bearing claim; the primary DESIVAST Δf_CW null is directly supported by the tabulated counts, two-sample z-statistics, and label-shuffle/LEE controls. The ~2σ bright/dark filament sign-flip is correctly flagged as a diagnostic residual rather than a headline result and does not affect the volume-limited BGS-dominated primary path.)

MINORS (constructive suggestions; none require new data or re-analysis)

Primary-path emphasis and bright/dark residual (abstract + §VI D + §VIII B). The abstract and §VI D correctly note that the DESIVAST primary path is constructed on the volume-limited z ≤ 0.24 BGS sample (99.1% bright-program spirals in the void class) and is therefore insensitive to the ~2σ filament bright/dark sign-flip seen in the full T-Web secondary path. A single explicit sentence in the abstract (or a short clause in the final sentence of §VIII B) reiterating that "the primary DESIVAST-anchored |Δf_CW| ≲ 0.002 null is insensitive to target-program mixing because the void definition restricts to the BGS volume-limited regime where bright targets dominate at 99%" would remove any residual reader ambiguity. This is a clarity/polish item only.

RSD boundedness quantification (§VIII opening + §XIII). The Monte-Carlo FoG-scale perturbation test (§VIII) already demonstrates that Δf_CW remains stable (|Δf_CW| shifts < 0.4 pp) under 5 Mpc/h line-of-sight displacements. Adding one sentence giving the maximum |z_Δ| across the 200 realizations (currently stated only as "every realization's void/non-void two-sample |z| stays below 2σ (maximum 1.93)") would make the robustness statement even tighter for readers concerned about redshift-space effects. Minor.

Data-availability / artifact statement (standard MNRAS requirement). The paper repeatedly references committed pipeline paths (pipelines/p5_desi_chirality/…, outputs/*.json, desi_env/phase2_sweep/ parquets, etc.) and states that analysis drivers are available in the companion data repository. A concise "Data Availability" paragraph (or expansion of the existing footnote) giving the public repository URL/DOI (or confirming that the exact membership-query code, deterministic RNG seeds, and per-cell parquets are released with the paper) would satisfy journal policy and aid reproducibility. This is a submission-day item.

Minor phrasing / table consistency.
- In the abstract and Table III caption, the phrase "the quoted σ_from half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n" is correct but could be parenthetically glossed once as "(hence we rely on monopole-subtracted residuals |σ_obs − σ_pred| and the omnibus χ² for cross-class inference)".
- A few table captions (e.g., Table VII) use "max |σ_obs − σ_pred|" while the text sometimes writes "|σ_obs − σ_pred|"; a single consistent symbol or short definition in §V would eliminate any micro-ambiguity. These are typographic polish only; the underlying numbers are consistent.

Optional but recommended (future-work / scoping). The paper already scopes the result as providing "an empirical upper bound on any future model in the bounce-chirality coupling class … at the ≳25 Mpc/h smoothing scale." A one-sentence quantification in the conclusions (e.g., "the 95% CI on the primary DESIVAST Δf_CW of [−0.0036, +0.0050] therefore bounds any environment-dependent chirality contrast at the current DESI DR1 sensitivity") would be helpful for model-builders without changing any conclusion.

All of the above are style, clarity, or journal-compliance items. None alter the scientific conclusions or require re-running pipelines.

Strengths (at least three; the list is not exhaustive)

- Explicit primary/secondary path declaration with pre-registration caveat. By designating the DESIVAST-anchored void cross-check (n_void = 56,981, three independent void-finding algorithms, five Bonferroni-5 estimators) as the load-bearing primary analysis and relegating the full T-Web 4-class, density, redshift, and sky-position scans to secondary/diagnostic status, the paper transparently bounds p-hacking / garden-of-forking-paths concerns. The multiplicity bookkeeping (Bonferroni-5 primary family, Bonferroni-9 Phase-2 sweep, descriptive LEE corrections elsewhere) is exemplary for a multi-path cosmological data-analysis paper.

- Statistical rigor and conservatism. Use of Jeffreys binomial credible intervals, label-shuffle permutation nulls (N_MC = 1,000, deterministic seeding, stratified variants), empirical max-stat LEE correction, monopole-referenced residuals |σ_obs − σ_pred| (propagating Paper IV Δf_CW uncertainty), and explicit treatment of the 3.56% duplicate rows (recomputed on unique-spiral subset) demonstrates best-practice frequentist care. The Phase-2 (Rs, λ_th) sweep and within-class density stratification further show that no result is an artifact of a single hyperparameter choice or class-boundary definition.

- Robustness to void definition and systematics. The primary result is reproduced across three independent void-finding algorithms (VoidFinder sphere-growing + two watershed prunings) and two catalog-native zone definitions (GALZONE), with |Δf_CW| ≤ 0.0037 in all cases and all contrasts below the Bonferroni-5 |z| = 2.58 threshold. The explicit per-galaxy cross-match purity check (0/6 T-Web "void" spirals inside DESIVAST holes at z ≤ 0.24) and the RSD Monte-Carlo membership-perturbation test quantify the survey-shell systematic that contaminates the small T-Web void bin and confirm that the DESIVAST re-projection (the controlling constraint) is stable. Target-program (bright/dark) splits are reported in full; the primary path is shown to be insensitive because it is BGS volume-limited.

- Transparency and reproducibility scaffolding. The paper supplies exact pipeline paths, output JSON/parquet artifacts, and per-cell rebuild instructions. The honest scoping (redshift-space statement only; T-Web void bin deprecated in favor of DESIVAST primary; ~2σ filament bright/dark sign-flip flagged as diagnostic rather than cosmological) and the explicit statement that "no conclusion in this paper depends on a residual threshold finer than [the propagated monopole uncertainty band]" are models of scientific candor.

- Scientific complementarity to Paper IV. By converting the global real-space dipole null of Paper IV into an environment-conditional test at the ~25 Mpc/h scale (and finding consistency with the catalog monopole), the work supplies a clean empirical upper bound for any future bounce or inflation model that might predict environment-dependent chirality. The null is therefore not merely "no detection" but a positive constraint on the bounce-chirality coupling class at currently accessible scales.

Overall assessment

This is a high-quality, methodologically sound null-result paper that meets the standards of MNRAS / PRD / JCAP for a data-analysis cosmology study. The primary DESIVAST-anchored claim is directly supported by the data and statistics; secondary paths are transparently labeled and do not affect the headline. With the minor clarifications and journal-compliance items above addressed, the manuscript will be ready for acceptance. I recommend MINOR REVISIONS.

Referee signature
External referee (cosmology / large-scale structure / galaxy morphology)
26 June 2026
