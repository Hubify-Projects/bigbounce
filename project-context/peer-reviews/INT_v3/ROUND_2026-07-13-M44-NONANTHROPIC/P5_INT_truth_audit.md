# P5 M44 non-Anthropic internal-review truth audit

**Paper:** P5, *Redshift-Space Environmental Null Tests of Spiral-Galaxy Chirality with DESI DR1 and DESIVAST*
**Audited manuscript:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, v0.1.127-2026-07-13
**Audited PDF:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`, 42 pages, SHA-256 `0461b4dc286d5a5713cfcf515f9e0549befe746085ca41adea250649f4fb2e40`
**Review round:** `ROUND_2026-07-13-M44-NONANTHROPIC`
**Audit date:** 2026-07-14
**Scope:** truth-audit only. No manuscript, ledger, SSOT, site, or shared-state changes are made by this document.

## Audit rule

Every reviewer finding below is reproduced verbatim and retains the reviewer's exact severity. The audit then separates: (a) factual support in the current manuscript/artifacts, (b) whether the issue is genuinely new or already represented by a standing DP5 disposition, and (c) what, if anything, the new DP5-10 cluster-bootstrap computation closes. A reviewer verdict is never silently upgraded, downgraded, or averaged with another model's verdict.

## Inputs read verbatim

- `API_P5_openai.md` — OpenAI `gpt-5.5`, native PDF, attempt 1.
- `API_P5_grok.md` — xAI `grok-4.3`, native PDF, attempt 1.
- `API_P5_gemini.md` — Google `gemini-3.1-pro-preview`, native PDF, attempt 1.
- Current P5 TeX/PDF, P5 disposition ledger, manuscript-referenced result artifacts, M44 provenance files, and the new DP5-10 compute artifacts.
- No Anthropic model or service was used in this audit.

## Exact review outcomes

| Reviewer | Exact overall verdict | Exact tagged findings | Central-claim statement |
|---|---:|---:|---|
| OpenAI / `gpt-5.5` | **REJECT** | **10 MAJOR + 4 MINOR = 14** | The narrow classifier-labelled null is broadly supported; stronger physical, real-space, and model-constraining claims are not. |
| xAI / `grok-4.3` | **MINOR REVISIONS** | **0 MAJOR + 3 MINOR = 3** | The controlled null at approximately 25 Mpc/h and above is supported. |
| Google / `gemini-3.1-pro-preview` | **MINOR REVISIONS** | **1 MAJOR + 3 MINOR = 4** | The central null is strongly supported. |

Gemini's overall **MINOR REVISIONS** verdict coexists with a finding explicitly tagged **[MAJOR]**. That internal tension is preserved exactly; this audit does not reinterpret the major tag as minor.

## Provenance and quantitative checks

The M44 manifests/logs identify the intended P5 v0.1.127 PDF, models, modalities, attempts, and verdicts. The reports discuss the correct manuscript and show no evidence of cross-paper contamination. The raw report hashes recorded for this audit are OpenAI `199d5781…`, Grok `751ae74f…`, and Gemini `99f1de38…`.

| Quantity or claim | Independent check | Audit result |
|---|---|---|
| Historical primary parent | Artifact 29 and DP5-10 inputs give `N=678,945`. | **Verified.** |
| Primary void result | `N_void=57,081`, `N_CW=28,339`, `f_CW=0.4964699287`. | **Verified.** |
| Footprint non-void control | `N_nonvoid=253,276`, `N_CW=126,202`, `f_CW=0.4982785578`. | **Verified.** |
| Primary contrast | `Delta f_CW = f_nonvoid-f_void = +0.0018086291`; binomial SE `0.0023165873`; `z≈0.781`, two-sided `p≈0.435`; normal 95% CI `[-0.0027318,+0.0063491]`. | **Verified from integer counts.** |
| Advertised systematic quadrature | Terms `[0.44,0.37,0.60,0.37,0.11,0.24,0.02,0.02]` pp give `sqrt(sum term^2)=0.9476` pp. | **Arithmetic verified.** This does **not** establish that heterogeneous and correlated terms form a calibrated confidence interval. |
| Classifier attenuation | Accuracy floor `a=0.6991` gives `kappa=2a-1=0.3982`; `0.9/0.3982=2.2602` pp. | **Arithmetic verified.** The quoted 2.26 pp uses the rounded 0.9 pp envelope; using 0.94 pp would give about 2.36 pp. Symmetric-error identifiability remains a stated limitation. |
| First-order RSD check | Artifact 27 reports an absolute primary shift of about `0.02397` pp and MC `0.0260±0.0485` pp. It does not rerun VoidFinder on reconstructed positions. | **Verified and correctly limited.** This is a first-order/fixed-geometry sensitivity check, not a real-space reconstruction. |
| FoG fixed-geometry test | The manuscript reports 34% membership contamination with contrast shifts bounded approximately `[-0.34,+0.37]` pp in its MC. | **Quantified within the stated proxy.** Grok overstates this component as wholly unquantified; anisotropic T-Web RSD remains unquantified. |
| Environment-stratified classifier confusion | GZ1 validation: void `N=933`, asymmetry `-0.02291`, 95% CI `[-0.05947,+0.01366]`; non-void `N=5,778`, `-0.00506`, CI `[-0.01962,+0.00950]`; difference `-0.01785`, `z=-0.889`, `p=0.374`. | **Verified.** This closes the availability of the requested check, not the stronger physical de-attenuation assumption. |
| Paper IV dependency | The TeX still contains `arXiv:XXXX.XXXXX` and explicitly conditions acceptance/verification on the companion work. | **Verified open venue dependency.** |
| Post-hoc status | Abstract/methods explicitly state the primary designation is exploratory and not preregistered. | **Verified and disclosed, not eliminated.** |
| Redshift-space scope | Current title says “Redshift-Space”; abstract states fixed redshift-space labels, first-order RSD sensitivity, and an unquantified anisotropic T-Web channel. | **Verified.** No real-space environmental bound is established. |
| Toy EFT | Appendix B explicitly calls the operator a noncovariant, gauge-sensitive toy parametrization and says it is not derived from the data. | **Verified as disclosed speculation.** Venue suitability remains editorial judgment. |
| Artifact availability | Current data-availability text enumerates A1–A34; the earlier artifact-range defect is fixed. DOI/archive timing remains pending. | **Partly closed, partly venue-timed.** |
| PDF integrity | 42-page current PDF; no overfull-box or undefined-reference warning was found in the available log scan. | **No objective compilation defect found.** Density/crowding concerns remain presentation judgments. |

## OpenAI / `gpt-5.5` — 14 findings

### OAI-1 — MAJOR

> 1. [MAJOR] Section II / Appendix A / Paper IV dependency: the analysis depends critically on a concurrently submitted, unpublished companion catalog paper with placeholder arXiv identifiers, unpublished/conditional provenance, and classifier-label systematics that cannot be fully refereed within this manuscript; a PRD paper cannot make acceptance conditional on another unreviewed paper.

**Truth audit:** Factually supported. The companion citation is still a placeholder, and the classifier/catalog validation cannot be fully re-refereed from P5 alone. The manuscript discloses this dependency and makes co-review/acceptance sequencing explicit, but disclosure does not close a venue dependency. **Standing DP5-21, OPEN-VENUE; not genuinely new.**

### OAI-2 — MAJOR

> 2. [MAJOR] Sections V B and XV / post-hoc primary designation: the “primary” DESIVAST path is explicitly selected after inspecting multiple environment classifiers and stratifications, so the quoted Bonferroni-5 family does not account for the full analysis tree or for estimator selection, and the resulting upper bounds are exploratory rather than confirmatory.

**Truth audit:** Supported. The Bonferroni-5 correction is arithmetically correct for the declared five-test family but cannot retroactively cover the full exploratory analysis tree. The current manuscript now labels the designation post-hoc/exploratory, resolving earlier contradictory “predeclared” wording without converting the result to confirmatory evidence. **Standing DP5-13; DP5-24 wording contradiction closed; not genuinely new.**

### OAI-3 — MAJOR

> 3. [MAJOR] Section VIII / DESIVAST footprint and control sample: the “footprint-restricted” non-void control is based on a union of void-sphere angular discs and radial spans, not the DESIVAST/BGS angular completeness mask or DESI random catalog, so the void/non-void contrast is not demonstrably selection-function matched.

**Truth audit:** Supported. The manuscript explicitly distinguishes its geometric footprint proxy from a survey selection/completeness function. This is an honest disclosed limitation, not a matched-randoms closure. **Standing DP5-06, RE-FLAG-DISCLOSED; not genuinely new.**

### OAI-4 — MAJOR

> 4. [MAJOR] Section VIII / void membership definition: the primary VoidFinder membership is an author-constructed point-in-sphere/hole-union proxy rather than an official per-galaxy DESIVAST membership; the manuscript acknowledges large changes under maximal-sphere and GALZONE definitions, but still quotes a tight headline envelope whose statistical interpretation is unclear.

**Truth audit:** Supported in substance. The point-in-hole-union label is a reproducible author proxy, not an official DESIVAST per-galaxy release product. Alternative definitions are computed and disclosed. The roughly 0.9 pp number is a sensitivity envelope, not a rigorously calibrated interval. **Standing DP5-16 plus DP5-11, RE-FLAG; not genuinely new.**

### OAI-5 — MAJOR

> 5. [MAJOR] Sections IV, VI, IX, XIII / T-Web reliability: the T-Web classification is shown by the authors’ own tests to be strongly affected by radial selection, footprint geometry, redshift-space distortions, and randoms-weighted reclassification, so its extensive results are not physically interpretable and should not be used as support for large-scale-structure environmental claims.

**Truth audit:** The empirical premise is supported; the manuscript itself restricts T-Web to a redshift-space diagnostic and does not make it the primary cosmological bound. Whether it should be shortened or removed is editorial. It cannot independently support a real-space physical environment claim. **Standing DP5-14, RE-FLAG-DISCLOSED; not genuinely new.**

### OAI-6 — MAJOR

> 6. [MAJOR] Sections VIII, XIII, XV / redshift-space versus real-space bound: the manuscript repeatedly presents model-relevant constraints while the environment labels are in redshift space; the first-order DESIVAST reconstruction does not rerun the void finder on reconstructed positions and therefore does not establish a real-space environmental chirality constraint.

**Truth audit:** Supported. The title and abstract now say redshift-space, and the first-order calculation is correctly described as a sensitivity bound. It does not establish a real-space constraint because the void catalog/geometry is not re-derived. **Standing DP5-12 residual (also tracked in scope/readability cleanup); not genuinely new.**

### OAI-7 — MAJOR

> 7. [MAJOR] Sections V, VIII, XI / statistical error budget: the advertised “honest effective 2σ systematic envelope” is an ad hoc quadrature of counting intervals, maximum excursions, membership-definition shifts, footprint effects, confidence cuts, and RSD estimates, many of which are correlated and not sampling errors; it is not a rigorously defined confidence interval.

**Truth audit:** Supported. The quadrature arithmetic is correct, but its terms do not share one probability model and are not demonstrated independent. The new cluster bootstrap quantifies one missing spatial-sampling covariance channel only; it cannot calibrate the combined heterogeneous envelope. **Standing DP5-11, with DP5-10 now a computed subcomponent; not genuinely new and not closed by DP5-10.**

### OAI-8 — MAJOR

> 8. [MAJOR] Appendix A / classifier-labelled versus physical chirality: the classifier has a low conservative binary accuracy floor and the de-attenuation relies on symmetric-error assumptions that are not constrained at the quoted sub-percent environmental scale, so the claimed physical-chirality/model-builder bounds are much weaker and less secure than stated.

**Truth audit:** Supported as a limitation. The environment-stratified GZ1 computation exists and finds no significant differential confusion, but its sample does not identify sub-percent asymmetric physical-label error in the full DESI parent. De-attenuation remains explicitly conditional on symmetric errors and the conservative accuracy floor. **Standing DP5-08 CLOSED-BY-COMPUTE for the requested stratified test; DP5-09 RE-FLAG for physical interpretation; not genuinely new.**

### OAI-9 — MAJOR

> 9. [MAJOR] Sections XII–XV / theoretical relevance to PRD: the bounce/inflation discussion is speculative and no published model predicts the tested signal; Appendix B explicitly introduces a non-covariant toy operator not derived from the data, so the manuscript’s connection to fundamental physics is too weak for PRD in its present form.

**Truth audit:** The factual characterization of the toy operator and lack of a published quantitative target is supported and already disclosed. “Too weak for PRD” is a venue/editorial judgment, not an empirical contradiction. **Standing DP5-20 plus venue judgment; not genuinely new.**

### OAI-10 — MAJOR

> 10. [MAJOR] Appendix D/E / reproducibility: many results are delegated to artifact IDs, pending Zenodo DOI snapshots, and repository paths rather than fully specified, archived data products available at review time; this is insufficient for independent verification of a 42-page data-intensive null analysis.

**Truth audit:** Mixed. Delegation to artifacts is real, but current A1–A34 paths and integer seams are enumerated and auditable; the previous artifact-range defect is closed. A permanent DOI/archive snapshot is still a submission-time dependency. **Standing DP5-18 CLOSED for the data-availability statement, DP5-26 CLOSED for the range, and DP5-21 OPEN-VENUE for immutable archive timing; not genuinely new.**

### OAI-11 — MINOR

> 11. [MINOR] Throughout / presentation: the manuscript is excessively long, repetitive, and difficult to audit, with many caveats embedded in captions and parentheticals rather than cleanly separated into methodology, results, and limitations.

**Truth audit:** Subjective but credible presentation feedback for a 42-page manuscript. It does not identify a false quantitative claim. **Standing DP5-22, RE-FLAG; not genuinely new.**

### OAI-12 — MINOR

> 12. [MINOR] Tables and figures / consistency and readability: several figures have crowded or overlapping labels, and the manuscript contains many near-duplicate counts, parent definitions, and sign conventions that make independent verification unnecessarily difficult.

**Truth audit:** The readability concern is credible but nonspecific; no page/figure-level overlap was identified by the reviewer, and the available compile log contains no objective overflow warning. Exact-row/count and sign seams have been independently reconciled. **Standing DP5-22 presentation issue; DP5-01 and DP5-03 quantitative seams closed; not genuinely new.**

### OAI-13 — MINOR

> 13. [MINOR] Sections V–VIII / notation: the proliferation of σfrom half, σpred, σvs monopole, z∆, pLEE, and multiple parent samples should be simplified; the current notation obscures which tests are inferential and which are diagnostic.

**Truth audit:** Presentation judgment, consistent with the manuscript's density. The distinction between inferential and diagnostic quantities is stated but can be made easier to follow. **Standing DP5-19/DP5-22, RE-FLAG; not genuinely new.**

### OAI-14 — MINOR

> 14. [MINOR] Title and abstract: the title and abstract overstate the maturity and definitiveness of the result relative to the explicitly post-hoc, classifier-labelled, redshift-space, companion-paper-dependent analysis.

**Truth audit:** Partly stale relative to the current text. The title now explicitly says redshift-space, and the abstract explicitly says exploratory/not preregistered, classifier-labelled, first-order RSD bounded, and T-Web anisotropy unquantified. Companion-paper dependence remains. Further rhetorical softening is editorial, not a newly demonstrated correctness defect. **Standing DP5-13/DP5-09/DP5-12/DP5-21 and DP5-22; not genuinely new.**

## xAI / `grok-4.3` — 3 findings

### GROK-1 — MINOR

> [MINOR] §V B (and Table IV): The designated-primary DESIVAST path is explicitly post-hoc with no timestamped pre-registration, leaving a residual garden-of-forking-paths exposure that the Bonferroni-5 family statement only partially mitigates.

**Truth audit:** Supported and explicitly disclosed. Bonferroni-5 does not turn the exploratory selection into preregistered confirmation. **Standing DP5-13, RE-FLAG; not genuinely new.**

### GROK-2 — MINOR

> [MINOR] §VIII (RSD treatment paragraph and Monte-Carlo description): The fixed-void-geometry membership test and first-order Zel’dovich reconstruction bound coherent outflow but leave the stochastic finger-of-god residual and anisotropic tidal channel unquantified, so the quoted ≈0.9 pp envelope is not yet demonstrated to be fully RSD-immune.

**Truth audit:** The conclusion is supported, but the premise is partly overstated. The anisotropic T-Web tidal channel is unquantified. The FoG residual is not wholly unquantified: the fixed-geometry MC reports 34% membership contamination and a contrast-shift range of about `[-0.34,+0.37]` pp. That proxy still does not make the heterogeneous 0.9 pp envelope RSD-immune or establish a real-space result. **Standing DP5-12/DP5-11/DP5-14; not genuinely new.**

### GROK-3 — MINOR

> [MINOR] Abstract and §I: arXiv placeholders (arXiv:XXXX.XXXXX) for the companion Paper IV catalog remain unresolved, preventing independent verification of the monopole offset and accuracy floor that propagate into every σ_pred diagnostic.

**Truth audit:** Supported as a venue/provenance dependency. The catalog and summary validation are exposed, but the companion manuscript's placeholder prevents stable bibliographic and co-review closure. **Standing DP5-21, OPEN-VENUE; not genuinely new.**

## Google / `gemini-3.1-pro-preview` — 4 findings

### GEM-1 — MAJOR

> 1. [MAJOR] Section II & Appendix A (Dependence on unpublished companion paper): The foundational data of this manuscript—the per-galaxy chirality labels and the catalog-wide monopole calibration—are derived entirely from an unpublished companion manuscript ("Paper IV"). Although the author transparently provides a summary in Appendix A, links to the public catalog, and explicitly states this dependency, *Physical Review D* policy generally requires that such intimately linked companion papers be co-reviewed. The scientific validity of the null result here cannot be fully established until the methodology of the classifier in Paper IV passes peer review; acceptance of this manuscript must be strictly contingent on the acceptance of Paper IV.

**Truth audit:** Supported as an unresolved co-review/venue dependency. The wording about PRD policy is the reviewer's policy judgment; the underlying dependency and placeholder are factual. **Standing DP5-21, OPEN-VENUE; not genuinely new.**

### GEM-2 — MINOR

> 2. [MINOR] Appendix B (Toy EFT mapping): The inclusion of a manifestly non-covariant, non-gauge-invariant operator as a "toy parametrization" for future model builders is out of place for PRD, even with the extensive disclaimers provided. Presenting an operator of the form $g_\phi (\nabla_i \phi) (\nabla^i \rho / \rho_{bg}) (\hat{L} \cdot \widehat{\nabla \rho})$ invites theoretical confusion. The author should either formalize this into a proper covariant and gauge-invariant EFT framework (e.g., using comoving-gauge density fluctuations properly contracted) or remove the appendix entirely. The paper's empirical bounds ($\sim 0.9$ pp effective systematic envelope) are rigorous and stand perfectly well on their own without this speculative mapping.

**Truth audit:** The operator's noncovariant/toy status is factual and already explicit. Removal versus formalization is editorial. The reviewer's statement that the 0.9 pp envelope is “rigorous” conflicts with OpenAI's statistically well-founded objection: its arithmetic is reproducible, but it is not a calibrated confidence interval. **Standing DP5-20 and DP5-11; not genuinely new.**

### GEM-3 — MINOR

> 3. [MINOR] Section XIII & Section VIII (Redshift Space Distortions): The manuscript correctly identifies that the T-Web classification is fundamentally limited by uncorrected anisotropic eigenvalue deformation due to Redshift Space Distortions (RSD). While the author bounds the RSD impact for the primary DESIVAST void analysis using a first-order Zel'dovich reconstruction, the T-Web results remain uncorrected. The abstract and introduction should more clearly state that the T-Web analysis is strictly a redshift-space diagnostic and that only the DESIVAST void/non-void contrast serves as a robust cosmological bound against real-space environment dependence.

**Truth audit:** The first two sentences are supported and already stated prominently. The suggested final wording would overclaim: DESIVAST is first-order RSD-bounded but is not a re-derived real-space void analysis, so it should **not** be presented as a robust real-space bound. **Standing DP5-14/DP5-12; not genuinely new.**

### GEM-4 — MINOR

> 4. [MINOR] Manuscript formatting and readability: The text is exceptionally dense and heavily saturated with defensive phrasing (e.g., "honest disclosure," "garden-of-forking-paths") and inline reproducible artifact tags (e.g., [A10], [A33]). While the author's commitment to radical transparency and computational reproducibility is highly commendable, the current formatting severely disrupts the physical narrative. The author should move the specific script/artifact IDs to footnotes or consolidate them entirely in Appendix E/Table XXII to improve the flow of the main text.

**Truth audit:** Credible presentation judgment, not a quantitative or provenance contradiction. Consolidation can improve the narrative while retaining auditable artifact mapping. **Standing DP5-22; DP5-26 artifact-range defect already closed; not genuinely new.**

## New-versus-standing adjudication

| Category | Count | Result |
|---|---:|---|
| Raw finding instances | **21** | 14 OpenAI + 3 Grok + 4 Gemini. |
| Genuinely new issue classes | **0** | Every finding maps to an existing DP5 disposition, already-closed seam, open venue dependency, or standing presentation judgment. |
| Entire M44 findings newly closed by DP5-10 | **0** | The bootstrap answers one subcomponent of OAI-7 only. |
| Review verdicts changed by this audit | **0** | Exact reviewer verdicts and severities are preserved. |

Repeated findings are evidence of reviewer convergence, not new classes. The strongest convergence is on DP5-21 (unpublished companion/co-review), DP5-13 (post-hoc selection), DP5-12/14 (redshift-space scope), DP5-11 (interpretation of the 0.9 pp envelope), and DP5-22 (density/readability).

## DP5-10 cluster-bootstrap assessment

New artifacts:

- `pipelines/p5_desi_chirality/scripts/35_desivast_cluster_bootstrap.py`
- `pipelines/p5_desi_chirality/outputs/35_desivast_cluster_bootstrap.json`
- `project-context/peer-reviews/INT_v3/P5_DP5-10_DESIVAST_CLUSTER_BOOTSTRAP_2026-07-14.md`

The computation assigns galaxies to their nearest 3D DESIVAST maximal-void center and resamples the 3,756 nonempty cluster units. With seed `20260714` and 20,000 replicates it gives:

- point contrast `+0.0018086291`;
- cluster-bootstrap SE `0.0023280689` and percentile 95% CI `[-0.002715063,+0.006353868]`;
- naive binomial SE `0.0023165873` and normal 95% CI `[-0.002731799,+0.006349057]`;
- SE ratio `1.0049563`, variance design effect `1.0099371`;
- leave-one-cluster-out jackknife SE `0.0023275805`, CI `[-0.002753345,+0.006370603]`;
- stable-tie sensitivity changes the point by only `-0.000030932` and the SE by `+0.000003115`.

The rerun produced byte-identical JSON, SHA-256 `352fff9671351f42bea89a1a81386767f8ded1f915aee11179b2f3248fce83c8`.

**What it establishes:** within this nearest-maximal-void clustering scheme, spatial/void-region sampling covariance changes the primary standard error by about 0.5% and does not change the null inference. This is strong local compute evidence for the formerly absent DP5-10 sensitivity check.

**What it does not establish:** it does not prove the heterogeneous 0.9 pp envelope is a confidence interval; it does not make the footprint proxy selection-function matched; it does not validate the author-constructed void-membership proxy as official; it does not reconstruct real-space voids; and it does not resolve classifier systematics or Paper IV co-review.

**Provenance limit:** the run reproduces all released historical integer gates, but the current local DESI FITS byte hash differs from the May sidecar raw hash and the remote object reports a later modification date. Historical per-row byte identity therefore cannot be independently proved from the currently available file. DP5-10 should be treated as a **computed closure candidate pending integration/provenance recording**, not silently marked closed in the ledger by this audit.

Accordingly, DP5-10 supplies partial closure evidence for the spatial-covariance subcomponent of **OAI-7**. It closes **no entire M44 finding** because OAI-7's central objection is the uncalibrated combination of correlated, heterogeneous systematic terms (DP5-11).

## Truth-audit conclusion

The multi-model evidence supports the narrow, explicitly scoped result: no statistically significant **classifier-labelled, redshift-space** environment dependence is detected for the declared DESI/DESIVAST contrasts at the tested scales. It does not establish a confirmatory preregistered result, a selection-function-matched comparison, a reconstructed real-space environmental bound, or an unconditional physical-chirality/model constraint.

The M44 result is therefore not honestly reducible to a consensus “minor revisions” outcome: OpenAI's **REJECT** verdict and ten major findings remain part of the evidence, even though all map to known standing items. The actionable state is **zero genuinely new issue classes, one newly computed covariance sensitivity, and no whole finding closed by that computation**. Publication readiness still depends most directly on DP5-21 venue/co-review closure and editorial decisions about DP5-11, DP5-20, and DP5-22, with the other disclosed limitations kept scoped rather than overclaimed.
