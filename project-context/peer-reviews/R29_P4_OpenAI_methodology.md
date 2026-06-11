# P4 R29 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v172.pdf` md5=f6c1f145 pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8881 chars)
**Wall time**: 429.3s

---

Referee report for Physical Review D (methods/statistics)

Paper: Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)

Scope of review
I assessed the statistical methodology, estimator declarations, null constructions, significance reporting, internal arithmetic, dimensional consistency, and traceability of all headline numbers from the abstract and conclusions to the body. I additionally audited figures/tables, checked effect sizes against quoted σ/p values, and looked for version-history/provenance text in the body.

Overall remarks
The paper presents a large-scale chirality catalog and a careful null analysis with multiple null constructions and a bias-hardening workflow. However, the manuscript, as written, contains extensive version-history/provenance prose, internal run-log pointers, and audit language inappropriate for a PRD manuscript, and several methodological and presentation issues must be addressed. Some central inferences rely on a block-bootstrap whose coherence-length choice is not stress-tested; multiple σ values from different nulls are juxtaposed without immediate caveats in some locations; and the data/code availability lacks a frozen DOI.

Findings and required actions

ESSENTIAL

P4-E1
Section: Abstract (page 1)
Problem: Abstract contains version-history/provenance language inappropriate for a PRD abstract: “An earlier version of this paper reported … that result is withdrawn (Appendix A) and no conclusion rests on it.”
Required fix: Remove all references to earlier versions/withdrawn results from the abstract. If necessary, keep a brief one-sentence footnote in an appendix noting a provenance correction, not in the abstract. Abstract should summarize current methods/results only.

P4-E2
Section: Throughout the main text (pages 1–20; multiple places)
Problem: Numerous instances of version-history and audit-log prose in the body: “Correction note: an earlier version printed…”, “withdrawn subsample-mask null…”, “an earlier rendering…”, “an earlier text misprinted…”, and many explicit artifact file paths (e.g., pipelines/.../c11_meta_m4_slab_stats.json).
Required fix: Remove all version-history prose from the main text. Move any necessary provenance details (including audit artifacts and run-log file paths) to a single consolidated Supplemental Material or data repository README. The PRD paper must read as a stable, final analysis without in-line development history.

P4-E3
Section: Data Availability (page 20) and elsewhere
Problem: No frozen, citable DOI for catalog/code/models. Text says: “A persistent archival DOI (Zenodo deposit) has not yet been minted; until it is, the versioned release tag above is the citable artifact.” PRD requires durable, citable artifacts.
Required fix: Mint DOIs (e.g., Zenodo) for (i) the catalog release used in this paper, (ii) the model weights, and (iii) the code snapshot reproducing the analysis (with the exact commit hash). Replace “will accompany” statements with the actual DOIs and confirm that the commit hash matches the paper’s version.

P4-E4
Section: Sec. IV C Fig. 7 caption (page 10) and Sec. VI first paragraph (page 12)
Problem: Different σ values from different estimators/nulls are juxtaposed without an immediate local caveat: “2.31σ real-space dipole + +6.48σ pre-MASTER ℓ=1 artifact” (Fig. 7 caption) and “(2.31σ real-space; +6.48σ pre-MASTER)” (Sec. VI). Instruction 7 requires explicit “not directly comparable” whenever σ from distinct nulls/estimators appear side-by-side.
Required fix: Add a local, explicit sentence in both places: “These σ values are from different estimators and nulls and are not directly comparable.” Alternatively, report amplitudes/effect sizes and relegate σ to the text that defines the null.

P4-E5
Section: Appendix D, item g (pages 18–19)
Problem: The primary exclusion result (block-bootstrap WLS template-fit disfavoring Aref = 1.7% at z ≈ −18) relies on a block-bootstrap with fixed block scale NSIDE = 8 and Nboot = 1000, but the block-size/coherence-length dependence is acknowledged and not tested (“No sensitivity test at alternative NSIDE values has been computed.”).
Required fix: Provide robustness of the block-bootstrap covariance to block size by repeating the analysis at alternative blockings (e.g., NSIDE = 4 and 16) and/or with a spatial Gaussian-process (or HAC/sandwich) covariance. Report the resulting σboot and z vs Aref across these settings. If results vary materially, justify the adopted block scale. This is load-bearing for the claimed exclusion.

P4-E6
Section: Abstract (page 1) and Sec. IV C (page 7)
Problem: The headline real-space dipole amplitude is given as 4.4 × 10−3 in Ap units (body) but not converted to a human-readable percentage in the abstract. PRD requires clear effect sizes accompanying σ.
Required fix: Add the equivalent percentage amplitude in the abstract: e.g., “amplitude 0.44%” (explicitly noting Ap = full-amplitude A). Keep consistent units.

P4-E7
Section: Throughout (pages 1–20)
Problem: The manuscript repeatedly cites internal “artifact” file paths in the prose (e.g., pipelines/p2_chirality/outputs/...json), which are not suitable for the PRD body text.
Required fix: Move all such internal path references to Supplemental Material, and replace in-text references with standard figure/table numbers or a Supplemental reference (e.g., “see SM Sec. S2, Fig. S3, Table S4”). Provide a compact index of artifacts in the SM.

MAJOR

P4-M1
Section: Sec. V and VII (pages 12–14)
Problem: Amplitude-comparison claim vs Shamir is inconsistent across the paper. One place compares Shamir’s ∼3% to the HC-broad A50 ≈ 0.75% (factor ≈ 4), another to full-sample A50 ≈ 0.36% (factor ≈ 8.3), yet the text claims “factor of ∼6–12”. The chosen estimator for the comparison is unclear.
Required fix: Choose a single, estimator-consistent comparison (clearly state which estimator and injection floor: HC-broad 0.75% or full-sample 0.36%). Quote the factor(s) precisely for 2% and 3% claims (e.g., 2%/0.75%=2.7; 3%/0.75%=4.0) and remove “6–12” unless justified explicitly. Alternatively, present both factors in a table with estimator labels.

P4-M2
Section: Abstract and Sec. IV C,b; Table III (pages 1, 8–11)
Problem: The paper uses several σ conventions (moment-z, rank-p, Gaussian-equivalent), which are typically well labeled; however, in a few places (e.g., Table III caption and discussion) the narrative mixes them quickly, and a standalone reader may not track which σ is quoted. 
Required fix: Add a one-sentence reminder in each place where σ is quoted for the first time in a section (e.g., “z here is (Cdata − ⟨C⟩null)/σnull for this row’s null; values across rows/footprints are not comparable”) and explicitly label “Gaussian-equivalent” where conversion of rank p is discussed. Ensure every quoted σ is immediately tied to its null definition.

P4-M3
Section: Sec. VI A (pages 12–13), Table V
Problem: Injection–recovery uses θ-uniform axis draws for the tabulated thresholds, which is not area-uniform on the sphere. The text later states a full re-run with area-uniform draws reproduces the thresholds, but this is embedded mid-paragraph without a clear table or summary.
Required fix: Provide a small table (or a parenthetical numeric line) reporting P(σ > 3) at A = {0.5%, 0.75%, 1.0%, 1.5%} for both θ-uniform and area-uniform axis draws, to demonstrate equivalence within MC errors. This removes ambiguity for readers not following the long paragraph.

P4-M4
Section: Sec. IV C (page 7)
Problem: The observed real-space dipole amplitude is given as Adip = 4.4 × 10−3 in Ap units, but no uncertainty on Adip is reported (only z and rank-p are reported).
Required fix: Report an estimator-level 68% interval (e.g., via the permutation null or bootstrap) for Adip itself (not only a z-score). This provides an effect-size uncertainty consistent with PRD standards for a null result.

P4-M5
Section: Appendix D, items d–h (pages 18–19)
Problem: The “eight-anchor” systematics analysis is qualitative or semi-quantitative in places. For example, the leg-proxy partial closure “∼ 25% of ℓ=1 amplitude” is asserted without an explicit quantitative error bar; the cross-spectrum significance is reported, but the fraction of variance explained (R^2) is not.
Required fix: Quantify the fraction of the ℓ=1 power explained by each nuisance template (with uncertainties), and provide a simple cumulative variance-explained summary. If exact variance decomposition is not stable due to collinearity, state that and provide a robust alternative (e.g., ridge-regularized projection with λ→0 limit, with uncertainty). This will solidify the systematics interpretation.

P4-M6
Section: III.B Declared Analysis Hierarchy (page 4)
Problem: The hierarchy is declared, but it refers back to provenance timing (“predates the provenance audit...”), which is development history language.
Required fix: Remove timing/provenance remarks. Keep only the hierarchy itself and its rationale (cosmological estimator vs diagnostic channels).

MINOR

P4-m1
Section: Sec. IV C (page 7)
Problem: The upper-limit construction AUL95 is defined as the 95th percentile of the permutation null amplitudes. This is descriptive but the text meanders about “no frequentist coverage guarantee.”
Required fix: Present AUL95 succinctly as a descriptive estimator-level bound and move the extended discussion to Supplemental Material. Optionally add a brief note that a Feldman–Cousins or CLs-style treatment is out of scope.

P4-m2
Section: Sec. II A (page 2)
Problem: The parent dataset “Smith42/galaxies” on HuggingFace is cited informally.
Required fix: Provide a formal citation (authors, title, year, URL/DOI). Confirm license and persistence.

P4-m3
Section: Sec. B. d (Appendix B; page 16–17)
Problem: Test T5 (metadata leakage) uses linear Pearson correlation with RA, a circular variable. While the limitation is acknowledged, the test is nonetheless listed in the pass table.
Required fix: Replace T5 with an appropriate circular-correlation or spherical-harmonic regression-only assessment for directional leakage, or clearly mark T5 as informational and non-binding, and rely solely on the low-ℓ regression reported.

P4-m4
Section: Sec. VII Conclusions (page 14)
Problem: “Harmonic-channel completeness … z ≈ 68–218 at Ap = 1.7%” is stated without even a single numeric quantile in the main text.
Required fix: Provide a median and [16, 84]% range for z over axes (e.g., “median 108 [68, 218]” or similar), with the axis selection protocol (equatorial or area-uniform) clearly stated.

P4-m5
Section: Many figures (Figs. 4, 7; pages 8–10)
Problem: Effect sizes are visible only via colorbars; no in-panel amplitude summary appears.
Required fix: Add a brief inline annotation of the global monopole and the fitted dipole amplitude on the map panels, e.g., “A_dip = 0.44% (null-consistent).”

NITS

P4-n1
Section: Title page and Appendix A (pages 1, 15–16)
Problem: The paper versioning (“v1.0.172”, “June 2026”) appears in the title page and is referenced in Appendix A.
Required fix: Remove internal version labels in the manuscript body. Keep only standard PRD submission/acceptance dates when available.

P4-n2
Section: Acknowledgments (page 20)
Problem: “AI tool usage…” sentence is not standard in PRD acknowledgments and is not necessary.
Required fix: Remove or move to a footnote in Data/Code availability if the journal permits; otherwise drop.

P4-n3
Section: Minor typographical issues
Problem: Occasional hyphenation artifacts (“ℓ= 1”, “C 2 2 ◦” spacing) and repeated spaces.
Required fix: Clean typographical spacing and hyphenation, ensure consistent “ℓ = 1”, “C2 2°”, etc.

Arithmetic/consistency checks (spot audit)

- Spiral counts/fractions: NCW = 1,592,107; NCCW = 1,609,053; Nspiral = 3,201,160. fCW = 0.497353; deviation −0.002647 (−0.265%). Binomial σ ≈ 0.000279; Dev = −9.49σ (table shows −9.47σ). OK.

- Asymmetry suppression factor: A_raw = +1.5758%; A_eq = −0.5294%; |A_raw|/|A_eq| = 2.98. OK.

- Injection Fisher floor: σ(A) = sqrt(3/N) = 9.68e−4 for N = 3.20116e6; 3σ floor ≈ 0.29%. OK.

- Injection mapping to true amplitude: a = 0.6991 ⇒ g = 2a − 1 = 0.398; 0.75%/0.398 ≈ 1.88%. OK.

- MASTER ℓ = 1 (apodized, Wp = Nall): (24.74 − 1.93)/3.12 = 7.31σ; rank p = 6/10001 = 6.0 × 10−4. OK.

- Canonical MASTER ℓ = 1 (unapodized): (7.27 − 0.57)/0.84 ≈ 7.98σ (vs. 7.93 quoted). Within rounding.

- Monopole+mask leakage (Table IV): Ratio 1.6846e−2 / 1.6961e−2 = 0.9932 (99.32% reproduction). z = (1.6961 − 1.6846)/0.0068 ≈ 1.69. OK.

- Hemisphere max statistic (Table IV): (3.484 − 1.693)/0.405 ≈ 4.42σ. OK.

Dimensional/notation consistency
- Equations (2) and (3) are dimensionless and consistent. 
- Cℓ units are clearly stated relative to field conventions (Ap vs fCW – 0.5) and ×10^6 scaling is used in Table III; consistent.

Length and focus
The manuscript is overly long for the central methodological contribution and is encumbered by internal audit/path references. It could be reduced by 20–30% by moving run-log details, artifact paths, and provenance narratives to Supplemental Material. Recommended maximum length: 14–16 pages for the main text, with an SM containing audit artifacts and extended diagnostics.

Standalone-reader test
Most symbols are defined, and declared estimator hierarchy is given. However, the reliance on many “artifact” paths in the text and the absence of a frozen DOI currently impede reproducibility for a typical PRD reader.

Effect sizes
Most σ claims are accompanied by amplitudes; two places need explicit effect sizes added (P4-E6, P4-m5).


## Summary recommendation
MAJOR REVISIONS

The core methodology appears sound and many internal numbers check out. However, the manuscript contains substantial version-history/audit language unsuitable for PRD, lacks frozen DOIs for data/code, juxtaposes σ from different nulls without local caveats at a few key points, and the block-bootstrap exclusion requires a robustness study to block size/coherence length. Addressing the essential and major points above, and streamlining run-log details into Supplemental Material, will bring the paper to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P4-E8
Section: III.A (Notation and Significance Conventions), bullet “MASTER ℓ = 1 moment-z”
Problem: The definition of z is written as “σ = Cdata1/σnull vs. the label-shuffle null mean and width,” which omits the subtraction of the null mean. The paper elsewhere correctly uses z = (Cdata − ⟨C⟩null)/σnull.
Required fix: Correct the definition to z = (Cdata − ⟨C⟩null)/σnull, and ensure this is consistent everywhere MASTER z is quoted.

P4-E9
Section: Sec. IV D; Table III; Appendix A
Problem: Irreconcilable σ values for the same “canonical unapodized ℓ = 1 MASTER” channel: +3.64σ (500-MC direct run) vs +7.93σ (10^4 run in Table III). The manuscript attributes the difference to “different null-run sizes/mask/weight conventions,” but both are labeled “canonical unapodized, label-shuffle null,” making the 2× jump in z implausible to be due to MC size alone. Field normalization and monopole-subtraction conventions appear to differ between the two computations, but this is not made explicit where the numbers are juxtaposed.
Required fix: Provide a side-by-side reconciliation table for the canonical-unapodized ℓ = 1 computation showing, for each variant: field definition (Ap vs fCW−0.5), whether galaxy-weighted mean subtraction is applied, mask/weight, and the null’s ⟨C1⟩ and σnull. Show that the +3.64σ result transforms into +7.93σ only by a defined change in estimator/normalization (not by MC size). Otherwise, remove one of the values or relabel it to the correct estimator.

P4-E10
Section: Abstract; Sec. IV C (a)
Problem: Abstract cites “robust under a per-galaxy label-shuffle null, z = 0.70,” while the body’s canonical run reports z = 0.58 (rank-p = 0.26) and an independent implementation gives z = 0.70 (rank-p = 0.23). This reads as cherry-picking the larger z in the abstract.
Required fix: Choose a single canonical label-shuffle result (the one used elsewhere in the paper) for the abstract. If you wish to mention both implementations, report both together with a sentence explaining the implementation difference.

P4-E11
Section: Abstract; Sec. VII Conclusions
Problem: Abstract/Conclusions claim “harmonic-channel completeness P(≥3σ) ≥ 0.999 at Ap = 0.75%,” referencing only an internal artifact (“c9b”) with no figure/table in the paper or SM.
Required fix: Add an in-paper figure or SM table documenting the MASTER ℓ = 1 injection results (axis protocol, Ninj, null, median and [16,84]% z). Without this, remove the completeness claim from the abstract.

MAJOR

P4-M7
Section: III.A (Notation and Significance Conventions), first bullet list
Problem: Three σ values from different estimators and nulls (+3.64, +7.93, +7.28) are juxtaposed in one sentence without a local, explicit “not comparable” caveat (only a generic remark appears elsewhere).
Required fix: Add an immediate caveat at this first appearance: “These z values arise from different estimators/fields and null procedures and are not comparable.” Or split into sub-bullets, each with its null explicitly re-stated.

P4-M8
Section: Table II (Catalog B calibrated row)
Problem: Reported Dev = +14.6σ for f = 0.504 ± 0.0003 appears inconsistent with the displayed numbers (0.004/0.0003 ≈ 13.3). The table footnote says deviations use the unrounded fraction, but that value is not shown, preventing verification.
Required fix: Provide the unrounded calibrated fraction and its binomial σ used to compute Dev. If the unrounded values do not yield 14.6, correct the Dev entry.

P4-M9
Section: Appendix C (hemisphere look-elsewhere paragraph)
Problem: The analysis first uses a direct-MC max-statistic null (correct way to incorporate trials), then applies an additional Bonferroni/BH correction over the same grid, explicitly acknowledging this is a “second, deliberately conservative penalty.” Double-penalizing is confusing and non-standard.
Required fix: Report the direct-MC max-statistic pLEE as the primary, principled result. If you wish to add Bonferroni/BH as a heuristic cross-check, present it clearly as secondary and do not let it override or “downgrade” the direct-MC result.

P4-M10
Section: Appendix D, item g (block-bootstrap)
Problem: Only Nboot = 1000 is used; no bootstrap Monte Carlo error bar (on σboot) or seed/replicate stability is reported. Since the z ≈ −18 exclusion is load-bearing, bootstrap stability should be quantified in addition to the block-size test already requested (P4-E5).
Required fix: Increase Nboot (e.g., to 5000–10000) and report σboot with its bootstrap standard error. Show stability across at least two random seeds. Summarize z vs Aref for NSIDE = 4, 8, 16 and for both Nboot settings.

P4-M11
Section: Appendix B, d (bias-hardening suite), Test T7
Problem: T7 is counted as “pass” using all classes, but for the spiral-only subset (the analysis target) the ordering inverts (mean flip-swap error 0.698 vs 0.464). This weakens the relevance of the pass to the science sample.
Required fix: Either (i) redefine T7 to be spiral-focused (and report whether it then passes), or (ii) explicitly mark T7 as informational/non-binding and avoid counting it as a pass in Table VII for the spirals-only use case.

P4-M12
Section: Sec. IV C (a), dipole axis report
Problem: A specific axis (l, b) = (293°, 12°) is quoted, then the text immediately states the axis is unconstrained at this significance. Reporting a single direction without an uncertainty region can be misleading.
Required fix: Either omit the axis entirely (recommended for a null), or provide an angular uncertainty (e.g., 68% cone half-angle from permutations) and state that the axis is statistically consistent with random.

MINOR

P4-m6
Section: Appendix E (a), edge-on contamination
Problem: Claim “reduces effective sample size by ∼10–15%, corresponding to a ∼5–8% sensitivity penalty” is not derived.
Required fix: Provide a short calculation (e.g., fraction of b/a<0.3, their average peq distribution leading to an effective g-factor), or soften to a qualitative statement without specific percentages.

P4-m7
Section: Throughout (notation for A vs Ap)
Problem: The symbol A is used both for (i) the full-amplitude dipole parameter in pCW = 1/2(1 + A cos θ) and (ii) “asymmetry-A units” where A = 2(fCW − 1/2) (i.e., Ap). Although equivalence holds for pure dipoles, this dual use is confusing.
Required fix: Use distinct symbols (e.g., Adip for the injected full amplitude; Ap for the per-pixel field). Add a one-line notation box to disambiguate.

P4-m8
Section: Fig. 8 caption
Problem: Caption contains version-history/audit text (“an earlier rendering …”), which is inappropriate for a figure caption.
Required fix: Remove version-history from the caption. If needed, move to SM.

P4-m9
Section: Sec. IV B (monopole null generative test)
Problem: The text states the two null means differ by “a 0.39σ shift in the standard error of the difference” without giving N or the actual SE. This makes the statement hard to verify.
Required fix: Provide N and the SE used, or just state the two means and their 1σ errors, plus a simple p-value for their difference.

P4-m10
Section: Appendix A (effective sky fraction paragraph)
Problem: The alternative “mask-restricted normalization” is discussed at length but not used by any estimator; this is distracting in the main appendix.
Required fix: Condense to one sentence or move the detailed normalization algebra to SM.

NITS

P4-n4
Section: III.D / Appendix B (flip-equivariance remarks)
Problem: Main text claims “flip-swap correlation = 1.000 by construction,” while Appendix B later notes 1.3% of rows violate a flip/average identity beyond 10−3 due to float32 storage. This is not scientifically impactful but reads as an inconsistency.
Required fix: Clarify in one sentence that perfect protocol-level equivariance holds before float serialization; tiny stored-column inconsistencies are due to finite-precision I/O and do not affect any estimator.

P4-n5
Section: References to artifacts in Conclusions (Sec. VII)
Problem: “artifact c9b” is referenced in Conclusions. Even if artifacts are kept in SM, Conclusions should not cite internal file names.
Required fix: Replace with a standard pointer (“see SM Sec. Sx”) or add an in-paper figure/table.

Explanation
The items above are new and do not duplicate those in my initial review. The most consequential new issues are: (i) the incorrect z-definition in the significance conventions (P4-E8); (ii) the unresolved +3.64σ vs +7.93σ conflict for the canonical ℓ = 1 channel (P4-E9); and (iii) the abstract’s use of z = 0.70 for the label-shuffle robustness while the body’s canonical run is z = 0.58 (P4-E10). Addressing these, alongside adding proper documentation for the harmonic-channel completeness claim (P4-E11) and strengthening the bootstrap robustness (P4-M10), will materially improve clarity and rigor.