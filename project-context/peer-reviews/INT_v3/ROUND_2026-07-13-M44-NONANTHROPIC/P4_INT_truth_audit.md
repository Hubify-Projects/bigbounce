# P4 M44 non-Anthropic INT truth audit

**Audit date:** 2026-07-14  
**Reviewed manuscript:** P4 v1.0.240, `pipelines/p2_chirality/chirality_catalog_paper.pdf`  
**Scope:** ledger-first, source-and-artifact adjudication of every OpenAI/Grok/Gemini finding. No paper, artifact, SSOT, site, Convex, or release mutation was performed.

## Input integrity and verdict preservation

All three raw responses were read verbatim. No `[FALLBACK`, `Reviewer call FAILED`, or `ROUND DEGRADED` marker occurs.

| Reviewer file | Actual in-text verdict | Finding count |
|---|---:|---:|
| `API_P4_openai.md` (`gpt-5.5`) | **REJECT** | **12 MAJOR + 4 MINOR = 16** |
| `API_P4_grok.md` (`grok-4.3`) | **ACCEPT** | **3 MINOR = 3** |
| `API_P4_gemini.md` (`gemini-3.1-pro-preview`) | **MINOR REVISIONS** | **4 MINOR = 4** |
| **Total** | **1 REJECT / 1 ACCEPT / 1 MINOR REVISIONS** | **12 MAJOR + 11 MINOR = 23** |

The current source is stamped v1.0.240 and the local compile is dated July 13, 2026, 36 pages, MD5 `7dcf5eaf447d50f3bbbe30952f140981`. The raws identify v1.0.240 and quote its distinctive 18.8% edge-on correction and Stage-A material; no wrong-paper substitution was found.

## Ledger-first pass

Commands:

```bash
python3 tools/ledger_match.py API_P4_openai.md P4
python3 tools/ledger_match.py API_P4_grok.md P4
python3 tools/ledger_match.py API_P4_gemini.md P4
```

Results:

- OpenAI: **6/16 MATCHED, 10 UNMATCHED**.
- Grok: **3/3 MATCHED**.
- Gemini: the parser emitted two header artifacts (`REVISIONS ... RAW RESPONSE` and `REVISIONS ISSUES: 1.`), then found the four real rows. Its raw output is **0/6 MATCHED**; the scientifically meaningful result is **0/4 real findings auto-matched**, with **2 parser artifacts that are not findings**.

`UNMATCHED` is lexical only. All 23 real findings were source-audited below.

## Source-verification basis

Principal checks:

```bash
rg -n '<claim signatures>' pipelines/p2_chirality/chirality_catalog_paper.tex
jq . pipelines/p2_chirality/outputs/canonical_provenance/e2e_fullrun/e2e_transfer_function_full.json
sed -n '1,120p' pipelines/p2_chirality/outputs/canonical_provenance/e2e_fullrun/RUN_SUMMARY.md
jq . pipelines/p2_chirality/outputs/canonical_provenance/c9/c9b_injection_completeness.json
jq . pipelines/p2_chirality/outputs/canonical_provenance/monopole_mask_null_results.json
pdfinfo pipelines/p2_chirality/chirality_catalog_paper.pdf
md5 pipelines/p2_chirality/chirality_catalog_paper.pdf site/public/papers/paper4_chirality_catalog.pdf
```

Verified anchors include: the primary HC sample and cut (`N=949,584`, `p_eq>0.6`) at source line 971; full Catalog C `N=3,201,160`; unthresholded `z=4.2–4.4`; confidence-sweep transition; harmonic `+7.28`, `+7.93`, and `+3.64`; the explicit 47% open remainder; 66.5% CE-ResNet pseudo-labels; GZ1 accuracy 69.91%, kappa 0.40, and coarse human-only floors; ECE lower bounds; observed-label-only A50/A95 scope; the block-bootstrap caveat; 99.32% pre-MASTER-only scope; parity-even/no-transfer-function caveat; the 2.9%/59,515 mismatch; and submission-gated DOI/hash language.

## Per-finding adjudication

`CORRECT` means the factual limitation is real. `RE-FLAG-DISCLOSED` means it is already ledgered/disclosed rather than newly discovered. `MISLABELED` means the requested severity exceeds the verified defect. None of these labels changes a reviewer's actual verdict.

| ID | Reviewer / severity | Finding preserved | Ledger/source result | Truth-audit disposition |
|---|---|---|---|---|
| O1 | OpenAI MAJOR | Primary null is HC `p_eq>0.6`, `N=949,584`; full sample has `z~4–4.4` without adequate nuisance justification. | DP4-07/-15/-17. Source L971 states all counts, the transition, and that the cut selection is not propagated into WLS covariance. | **CORRECT limitation; RE-FLAG-DISCLOSED.** The narrow selected-field null is supported; survey-wide physical-null generalization is not closed. |
| O2 | OpenAI MAJOR | Large harmonic residuals and ~47% unexplained remainder undermine a sub-percent cosmological null. | DP4-17 OPEN-COMPUTE. L996/L1066/L1537 preserve all residuals and call 47% open. | **CORRECT open limitation.** The a-fortiori amplitude argument is not a joint likelihood or provenance attribution. |
| O3 | OpenAI MAJOR | Multiple nulls, masks, weights, fields, and sigma conventions are rhetorically combined. | DP4-13/-17. Decision-tree tables and L996 explicitly separate them and prohibit cross-sigma comparison. | **PARTLY CORRECT, RE-FLAG-DISCLOSED.** No arithmetic combination was found, but the manuscript still leans on multiple non-joint diagnostics. |
| O4 | OpenAI MAJOR | 66.5% pseudo-labels, 69.91%/kappa=.40 validation, and coarse GZ1-only A95 cannot test sub-percent inheritance. | DP4-08/-15. L732 and L1116 state exactly this ceiling. | **CORRECT, RE-FLAG-DISCLOSED; DP4-15 remains open.** The GZ1 null corroborates but cannot close sub-percent bias. |
| O5 | OpenAI MAJOR | Severe miscalibration plus a hard confidence cut can create spatial selection. | DP4-07/-15. L886 states ECE >=.25-.36, hard labels' limited immunity, and the remaining spatial-selection duty. | **CORRECT standing limitation.** Monotone recalibration alone is not the remedy; conditional spatial selection remains unclosed. |
| O6 | OpenAI MAJOR | A50/A95 inject only into the hard-label field, not images/classifier/triage/cut/spatial confusion. | DP4-09/-15. L1140ff states this explicitly. Stage-A artifact measures mirror-pair behavior only. | **CORRECT. Stage B is still required.** See dedicated section below; current “full image-level end-to-end mirror-flip injection” wording overstates what Stage A did. |
| O7 | OpenAI MAJOR | WLS `z~-7.6` is uncalibrated, uses full Catalog C, and omits HC selection propagation. | DP4-14/-07. L971 and L1513 state exactly those limitations. | **CORRECT, RE-FLAG-DISCLOSED.** It is a template-disfavor statistic, not frequentist exclusion. |
| O8 | OpenAI MAJOR | 99.32% applies only pre-MASTER; post-MASTER residual remains. | DP4-11/-17. Artifact defines a pre-MASTER ratio; source says post-MASTER reproduction is ~12%. | **CORRECT, RE-FLAG-DISCLOSED.** It cannot be exported to prior pipelines; manuscript already requires matched Ganalyzer. |
| O9 | OpenAI MAJOR | Shamir comparison is over-interpreted without matched Ganalyzer selection/likelihood. | DP4-11/-12. Abstract and Sec. V call it amplitude-level only and require matched reanalysis. | **CORRECT standing scope limit.** Strong “would have been detected/tension” language remains pipeline-conditional, not formal exclusion. |
| O10 | OpenAI MAJOR | Physical/PRD interpretation is weak because l=1 is parity-even and no primordial transfer exists. | DP4-12. L1263 states both facts. | **CORRECT, RE-FLAG-DISCLOSED.** No quantitative primordial constraint is established. |
| O11 | OpenAI MAJOR | Raw/equivariant pass mismatch affects 2.9% and 59,515 HC rows; precision release needs regeneration. | DP4-08/-21. L886/L1381/L1562 disclose the flag, separate-pass cause, and null-stable filtered test. | **CORRECT catalog-quality concern; standing.** Hard-label null is robust, but probability-column consistency is not repaired by a flag. |
| O12 | OpenAI MAJOR | Sharp cut transition shows selection-function domination without marginalization. | DP4-07/-15/-17. L971 preserves `4.3,4.1,4.0 -> .41,1.14,.51`. | **CORRECT standing limitation.** This is the same conditional-selection closure frontier as O1/O5. |
| O13 | OpenAI MINOR | Manuscript is long/repetitive/defensive. | DP4-13, presentation half closed in v1.0.237. | **EDITORIAL / residual re-flag.** Not a new scientific defect. |
| O14 | OpenAI MINOR | A/Ap/fCW/pseudo-Cl/MASTER normalizations are error-prone. | DP4-13. Source supplies explicit conversion and estimator tables. | **CORRECT presentation risk, RE-FLAG-DISCLOSED.** No new factor-of-two error found. |
| O15 | OpenAI MINOR | DOI and immutable archive are deferred; live paths are not publication-ready. | DP4-21 OPEN-VENUE. L1557/L1562 explicitly defer minting. | **CORRECT and OPEN.** Must be closed at submission; no DOI/hash may be fabricated. |
| O16 | OpenAI MINOR | AI statement increases need for concise independent spec. | DP4-13. | **EDITORIAL judgment.** It adds no distinct technical defect. |
| G1 | Grok MINOR | Inject observed 47% residual template into real-space estimator instead of inferring an Ap mapping. | DP4-17. Current mapping is analytical; no committed residual-template cross-estimator injection was found. | **CORRECT targeted closure test; standing DP4-17, not a new class.** It is useful but does not replace joint covariance. |
| G2 | Grok MINOR | Archive exact prereg commit and one-line selection diff in supplement. | DP4-07/-21. Source L971 already names commit `94113e5`; supplement placement/diff is absent. | **PROCESS-NIT / standing archive task.** |
| G3 | Grok MINOR | Report exact axis draws and 16–84% spread. | DP4-09. L1140ff already reports 10 fixed axes x100, 16–84% `.49–.58`; c9b reports 1,000 per amplitude per coordinate axis and per-axis p16/p84. | **SUBSTANTIVELY PRESENT; table-placement MINOR only.** |
| M1 | Gemini MINOR | Move paths/scripts/JSON names out of narrative. | DP4-13/-21. | **EDITORIAL presentation request, not a science defect.** |
| M2 | Gemini MINOR | Consolidate repeated Shamir caveats. | DP4-11/-13. | **EDITORIAL; standing.** The caveat itself is scientifically necessary. |
| M3 | Gemini MINOR | Bullet the dense but mathematically sound 47% bound. | DP4-17/-13. Gemini explicitly accepts the mathematics. | **EDITORIAL clarity request; no new defect.** The unresolved covariance remains scientific. |
| M4 | Gemini MINOR | Abstract should state CE-ResNet pseudo-label dependence. | DP4-08/-13. Abstract does not name CE-ResNet; Introduction L688 and Data L732 do. | **CORRECT small transparency edit; not a new science class.** |

## Stage A versus required Stage B

### What Stage A actually establishes

`e2e_transfer_function_full.json` is internally explicit:

- `stage: "A"`, 192/192 shards, 8,474,531 galaxies, actual production ViT;
- raw mirror flip-recovery `T_raw=0.230267 +/- 0.000231`;
- production Z2-TTA `T_eq=0.9997376`, with exact probability antisymmetry by construction and the residual due to argmax ties;
- North/South raw transfer differs (`0.2178` vs `0.2510`).

`RUN_SUMMARY.md` states that translating A50/A95 to true physical amplitude is **Stage B + paper integration work**, and ends: **“Stage B (hybrid image→field injection-recovery) consumes these precomputed flip labels.”** Thus Stage A is a full-catalog image-level *mirror-pair/equivariance characterization*. It is real evidence that the symmetrized probability protocol obeys mirror antisymmetry. It does not inject a known sky-varying physical chirality population, traverse NS triage and the `p_eq` selection, and estimate the recovered dipole under depth/PSF/morphology-dependent confusion.

### Stage B is still required

**Yes. Stage B hybrid image→field injection-recovery remains required** to close the physical-sensitivity part of DP4-15/O6. Exact required scope:

1. define injected physical handedness amplitudes and sky axes before inference;
2. use Stage-A mirror pairs/labels to construct controlled image-level population perturbations without claiming an unvalidated continuous morphology transform;
3. rerun production ViT, Z2-TTA, NS triage, hard argmax, and every `p_eq` cut;
4. condition recovery/confusion on imaging leg, depth, PSF/seeing, morphology, confidence, and sky position;
5. propagate the recovered field through the same HC real-space estimator and null;
6. publish A50/A95 distributions across axes/strata with uncertainty, failure modes, and immutable provenance.

Until then, the defensible sensitivity claim is **observed hard-label field/estimator conditional**, not a sub-percent physical galaxy-chirality threshold.

### Reader-visible wording mismatch

Current source L1171–L1207 calls Stage A a “full image-level end-to-end mirror-flip injection” and says the prior operative next step is “performed,” while the authoritative artifact calls itself Stage A and says Stage B remains. This is a **real provenance/claim-scope mismatch**. It is adjacent to standing DP4-15 rather than a new scientific mechanism, but it is a newly identified reader-visible correctness edit: rename the performed run to a full-catalog mirror-pair transfer/equivariance sweep and state unambiguously that hybrid physical-signal injection-recovery is unperformed.

## Genuinely new versus standing findings

- The **23 reviewer findings introduce no new scientific defect class** beyond DP4-07 through DP4-17 and DP4-21. OpenAI's harsh verdict nevertheless correctly identifies that the broad physical-null claim is not closed by the current conditional estimator.
- **DP4-15, DP4-16, and DP4-17 remain genuinely open compute**, not closure-by-disclosure items.
- The Stage-A/Stage-B wording conflict above is a **newly identified reader-visible scope error** tied to DP4-15.
- DP4-21 remains a real submission gate.

## Independent operational blocker: PDF mirror drift

The canonical local v1.0.240 compile is MD5 `7dcf5eaf...` and dated July 13. The exact site overview path `site/public/papers/paper4_chirality_catalog.pdf` is MD5 `df384089...`, dated July 12, and corresponds to the earlier v1.0.237 compile. `public/papers/paper4_chirality_catalog.pdf` is the same stale hash, while `site/public/papers/chirality_catalog_paper.pdf` has the current hash. This split naming surface can cause the site to serve a stale P4 PDF and is a **new live release-state defect**. No mirror was modified during this audit.

## Final disposition and closure scope

- **Verdicts preserved:** OpenAI REJECT; Grok ACCEPT; Gemini MINOR REVISIONS.
- **Findings:** 23/23 adjudicated, 0 TBD.
- **Narrow supported claim:** the pre-specified HC (`p_eq>0.6`) observed hard-label field is null-consistent under the declared real-space estimator/permutation framework.
- **Not yet supported as closed:** survey-wide physical sub-percent chirality null; formal Shamir/Ganalyzer exclusion; quantitative primordial parity constraint.
- **Required compute:** Stage B hybrid image→field injection-recovery (DP4-15), generative hierarchical survey null (DP4-16), joint real-space/harmonic covariance plus residual-template cross-estimator injection (DP4-17).
- **Required non-compute:** correct Stage-A wording, add CE-ResNet provenance to abstract, regenerate internally consistent probability columns or narrow the precision-catalog claim, mint immutable archive/DOI at submission, and repair all PDF mirrors.
- **Release readiness:** **NOT READY for an unqualified physical/cosmological-null claim.** The conditional HC observed-label null can be published only with the above scope explicit; 95–99% readiness requires the open compute or a deliberate, venue-accepted claim narrowing.

No ACCEPT verdict, physical transfer function, calibrated exclusion, closed spatial-confusion model, DOI, or Stage-B result was fabricated.
