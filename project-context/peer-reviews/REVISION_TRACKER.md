# BigBounce Manuscript Revision Tracker

**Paper:** Geometric Dark Energy from Spin-Torsion Cosmology
**Author:** Houston Golden
**Current version:** v1.6.0
**Target:** arXiv-ready manuscript

---

## How This Works

Every peer review / audit gets saved in `project-context/peer-reviews/` with the naming convention:
```
YYYY-MM-DD_HHMMtz_description.md
```

This tracker logs each revision round and which issues have been addressed.

---

## Revision Rounds

### P3 v3.2.0-r6: Exact-PDF ApJS control confirmation (2026-07-14)

**Input:** exact 15-page PDF from closure commit `064b06bdbc2a5844837dbd92d5fafbc58c44328b`, reviewed at repository commit `c6277107cb8d705d6b2c1b675269f507fa54ab9a`; TeX SHA-256 `723d25080fa0e192c225105d42cf7ead233d5ec5cc3956b30630e5601268fc89`; PDF SHA-256 `a16c217930a31ba799b68a88b2477b020ad5e309ff79626e49b2b69a715fdd5a`.

**Panel:** Grok 4.3 **ACCEPT** (4 hidden MINOR tags) / Gemini 3.1 Pro Preview **MINOR REVISIONS** (3 MINOR) / OpenAI GPT-5.5 **MAJOR REVISIONS** (5 MAJOR / 6 MINOR). Immutable `APJS-CATALOG` packets, all first-attempt concurrent native-PDF legs, no Anthropic/Claude. Evidence manifest 9/9 PASS.

**Truth audit:** all three support the deterministic public-DESI positional-rejoin computation. The new chance, warned-population, and original-member controls are real and reproducible, but OpenAI identifies bounded catalog-contract and provenance work that prevents a minor-only board.

| Finding | Status | Required action/evidence |
|---|---|---|
| 170 core versus 11 tail | **OPEN — ACCEPTANCE-RELEVANT CONTRACT** | Make the <0.1" core and chance-compatible 0.1–1" association tier explicit; preserve all 181 rows; infer no purity |
| Shifted-position control | **CLOSED BY COMPUTE** | Parent 2,468 vs 86.69+/-14.42; strict 181 vs 76.19+/-13.30; tail 11 vs 75.56+/-13.01 |
| Original-member sensitivity | **CLOSED BY COMPUTE** | 180/181 retained; only P3-DESI-000030 removed at 1.979009" |
| Warning-population comparison | **CLOSED BY EXACT PRODUCT** | Exact warned `original_score` median is 5.841820; the prior audit's different value is superseded |
| TARGET_RA/DEC coordinate lineage | **OPEN — BOUNDED PROVENANCE** | Recover immutable upstream semantics or explicitly bound the result to coordinate association |
| Definitive submission bundle | **OPEN — WORKFLOW MAJOR** | One manifest-led checksum-bound primary/auxiliary/AAS-table bundle; DOI remains pending |
| Legacy scores / warning-free / viewer hierarchy | **STALE/CLOSED** | Existing text already labels legacy metadata, ZWARN=0, and viewer evidence as subordinate |
| Historical dataset name / example caption | **OPEN — PRESENTATION MINOR** | Name the prior catalog early and restate deterministic excerpt rule |

Critical path was 59.7 seconds versus 100.6 seconds summed (40.7% reduction). No readiness uplift; P3 remains capped at 56. Full audit/raws: `INT_v3/ROUND_2026-07-14-P3-v3.2.0-r6-EXACTPDF-a16c2179-APJS-NONANTHROPIC-CONFIRM/`.

### P4 v1.0.243: Exact-PDF ApJS confirmation panel (2026-07-14)

**Input:** exact 27-page PDF from manuscript commit `22818453cbd9445b26f2e04de39aef03319a2609`, reviewed at repository commit `36badcbdf498123413031aa0a9504127d48f2054`; TeX SHA-256 `6affe4205a49a7954716f09ef11f31e1c17da1cbd778c195f8966c25c0127ed0`; PDF SHA-256 `9e73fd888699058d421043b0dd2de5d37d2aeb36fe37e8dd1c0bf5409e947d19`.

**Panel:** OpenAI GPT-5.5 **MAJOR REVISIONS** (12 MAJOR / 6 MINOR tags) / Gemini 3.1 Pro Preview **MINOR REVISIONS** (0/4) / Grok 4.3 **MAJOR REVISIONS** (3/2). Immutable `APJS-CATALOG-METHODS` packets, all first-attempt concurrent native-PDF legs, no Anthropic/Claude.

**Truth audit:** all three reviewers support the narrow HC observed-label null (`+0.55 sigma`, `p=0.265`) under the declared estimator and isotropic pixel-permutation null. The panel does not support a physical/primordial upper bound.

| Finding | Status | Required action/evidence |
|---|---|---|
| Immutable release/DOI/commit links | **OPEN — WORKFLOW GATE** | Freeze catalog, code, artifacts, and PDF; verify checksums/routes; insert real identifiers |
| Reconstructed raw/flip probabilities | **OPEN — CATALOG-INTEGRITY GATE** | Rebuild/remove or machine-quarantine unsafe columns; never call them calibrated probabilities |
| Catalog user contract | **OPEN — APJS UTILITY GATE** | Machine-readable schema, units, flags, filters, example query, and minimal reproduction |
| DP4-15/16/17/21 | **OPEN — DISCLOSED SCIENCE/HISTORY GATES** | Preserve transfer, matched-estimator, covariance/selection, and no-formal-preregistration limits |
| Pixel-null exchangeability | **OPEN — BOUNDED METHODS CLARITY** | Print existing per-galaxy shuffle and weight/mask cross-null results compactly |
| Mask-count/harmonic contradictions | **MOSTLY STALE** | Distinct supports/nulls are already mapped; normalize terminology only |
| Injection/calibration overclaim | **STALE/CLOSED** | v1.0.243 repeatedly rejects physical thresholds and labels scores as rankings |
| DP/path/WLS/MASTER density | **OPEN — EDITORIAL** | Compress project language while preserving reproducibility mapping |

Critical-path wall time was 86 seconds versus 183.0 seconds summed (53.0% reduction). No readiness uplift; P4 remains capped at 80. Full audit/raws: `INT_v3/ROUND_2026-07-14-P4-v1.0.243-EXACTPDF-9e73fd88-APJS-NONANTHROPIC-CONFIRM/`.

### P2 v1.7.121: Exact-PDF PRD positioning confirmation (2026-07-14)

**Input:** exact 10-page PDF from manuscript commit `86b38a0c2f31b1b4afae166c04f6658a5ed6d83f`, reviewed at repository commit `36badcbdf498123413031aa0a9504127d48f2054`; TeX SHA-256 `caf63ccd839e22935fd9737e243161e2fcf67a868b9f6a827e54e7b30f29169a`; PDF SHA-256 `d75d7bfa2f7b8b9ba006137ed7b3da3f099475ba60f1db4886168750866f127e`.

**Panel:** OpenAI GPT-5.5 **MAJOR REVISIONS** / Gemini 3.1 Pro Preview **MINOR REVISIONS** / Grok 4.3 **MINOR REVISIONS**. Immutable `PRD-RESEARCH` packets, three concurrent native-PDF legs, no Anthropic/Claude. Independent Codex is a typed `NOT_RUN` quota gap.

**Truth audit:** v1.7.121 successfully demoted the survey arithmetic and removed UV-completion independence. All three reviewers support the central contraction-phase algebra in substance. OpenAI's MAJOR verdict retains real external gates but misreads several already printed appendix elements as absent.

| Finding | Status | Required action/evidence |
|---|---|---|
| Central four-vertex derivation absent | **MOSTLY STALE** | Appendix already prints vertices, per-vertex limits, multiplicities, normalization, collapsed polynomial, epsilon grouping, and Li check |
| Title/observational prominence | **OPEN — BOUNDED POSITIONING** | Remove `Testing`/SPHEREx prominence; retain conditional map as secondary material |
| Ordered sums / product / epsilon scope | **OPEN — MINOR** | Define at first use and make the vertex-table caption internally consistent |
| Polynomial `P` notation | **OPEN — MINOR** | Rename to a distinct degree-nine symbol |
| Primordial-to-LSS convention | **OPEN — BOUNDED CLARITY** | Print the no-extra-factor convention bridge after checking the existing convention artifact |
| UMF response versus free `b_phi` | **OPEN — BOUNDED CLARITY** | State `b_phi=2 delta_c(b_1-1)` as the specialization of the general response |
| Cubic transfer / survey covariance | **OPEN — EXTERNAL SCIENCE/DATA GATES** | Direct third-order calculation and actual covariance/likelihood; text cannot substitute |
| Fermion torsion / archive DOI | **OPEN — MODEL/WORKFLOW GATES** | Model-specific bound and verified immutable release before submission |
| Future-date citation warning | **FALSIFIED** | Review date is 2026-07-14; 2025--2026 sources are not future-dated |

Critical-path latency was 98.1 seconds versus 193.3 seconds summed (49.2% reduction). A first launch with an incorrect full commit id failed closed before any reviewer call. No readiness uplift; P2 remains capped at 74. Full audit/raws: `INT_v3/ROUND_2026-07-14-P2-v1.7.121-EXACTPDF-d75d7bfa-PRD-NONANTHROPIC-CONFIRM/`.

### P1A v1A.0.121: Exact-PDF CQG Note minor-only confirmation panel (2026-07-14)

**Input:** exact 7-page PDF from manuscript commit `b587cb7bb8e075aa9d0245ba8257fcef7ff196b8`, reviewed at repository commit `15f2e6af98daec7f9634e50961c7c1f7375c87fe`; TeX SHA-256 `4bf3a979fa214a06c29c474fe7a49f3d032150769d505de16647b0854701a650`; PDF SHA-256 `adfaf5e9fec12dc89857ea947b06d2923d49a8a0b3e45880b278b79bd22dab77`.

**Panel:** OpenAI GPT-5.5 **MINOR REVISIONS** / Gemini 3.1 Pro Preview **MINOR REVISIONS** / Grok 4.3 **MINOR REVISIONS**. No report contains an internally MAJOR-tagged item. Immutable `CQG-NOTE` packets, three concurrent native-PDF legs, no Anthropic/Claude. Independent Codex is a typed `NOT_RUN` quota gap.

**Truth audit:** all three reviewers support the central narrow result. Remaining work is bounded and does not require new science.

| Finding | Status | Closure |
|---|---|---|
| "Observational consequence" density wording | **OPEN — MINOR** | Use dimensional coefficient benchmark and explicit non-constraint wording |
| Cartan source/coefficient bridge | **OPEN — MINOR** | One convention-pinned intermediate line/cross-reference |
| Coefficient-one vs contact/Holst/state factors | **OPEN — MINOR** | Tighten first benchmark statement; no numerical change |
| Cutoff ceiling and `R_A` | **MOSTLY CLOSED — PRESENTATION** | Repeat existing non-threshold/regulator-bound caveat in table caption |
| Boundary-data scope | **OPEN — MINOR** | Define matched background/initial/boundary data and boundary contribution assumption |
| Fierz ordering reference | **OPEN — MINOR** | Cross-reference Appendix A at first scalar-coupling use |
| Running/TB-EB/PACS/provenance | **OPEN — COPYEDIT/WORKFLOW** | Narrow Lorentzian barrier, expand cross-power terminology, remove PACS, bind immutable code version |

This is the first exact three-vendor minor-only board of the current campaign. Critical-path latency was 63.5 seconds versus 103.4 seconds summed (38.6% reduction). Public readiness remains capped at 62 until the bounded v1A.0.122 closure, independent Codex gap, and external confirmation are resolved. Full audit/raws: `INT_v3/ROUND_2026-07-14-P1A-v1A.0.121-EXACTPDF-adfaf5e9-CQG-NOTE-NONANTHROPIC-CONFIRM/`.

### P5 v0.1.130: Exact-PDF AJ confirmation panel (2026-07-14)

**Input:** exact 38-page PDF from manuscript commit `0842dfc60dec137ee30c92e44af26600feaaf058`, reviewed at repository commit `b08f46b6d85cdf796d39b08c1e90d0cc58c4dee7`; TeX SHA-256 `ea5613818ad2f60386658acc76b3f60f108fee5237e68de9dafbf26dbf4981b4`; PDF SHA-256 `f5b7a1bb5e7bbd565baac6b21aeab4e18611aec03b18dbf8e298de04d719fe17`.

**Panel:** OpenAI GPT-5.5 **REJECT** / Gemini 3.1 Pro Preview **MINOR REVISIONS** (two internally MAJOR-tagged findings) / Grok 4.3 **MINOR REVISIONS** (two internally MAJOR-tagged findings). Immutable `AJ-OBSERVATIONAL` packets, three concurrent native-PDF legs, no Anthropic/Claude. Independent Codex is a typed `NOT_RUN` quota gap.

**Truth audit:** the narrow catalog-specific exploratory non-detection is plausible/supported, but P5 is not submission-ready.

| Finding | Status | Required evidence/action |
|---|---|---|
| Paper IV labels/weights/provenance | **OPEN — EXTERNAL PUBLICATION GATE** | Coordinated review or accepted Paper IV; final independently reviewable release; rerun P5 on final labels |
| Immutable P5 tag/archive/DOI | **OPEN — WORKFLOW BLOCKER** | Public frozen bundle; A1--A40 verification; final identifier |
| Post-hoc "designated primary" | **OPEN — POSITIONING MAJOR** | Rename focal estimate as descriptive/exploratory; no confirmatory language |
| GALZONE parent / `OUT=0` / VoidFinder arm | **OPEN — CLARITY MAJOR** | One exact flow explaining released quality parent versus hole-union void membership |
| Covariance/model specification | **OPEN — REPRODUCIBILITY MAJOR** | Print A37 formula, 50 sky clusters, 78 columns, finite-sample correction, and 3,750-region sensitivity |
| DESIVAST selection matching | **OPEN — EXTERNAL-DATA/SCOPE GATE** | Exact mask/random products or continued non-selection-matched scope; do not substitute nonidentical products |
| Environment-dependent label bias | **OPEN — POWER GATE** | Void-arm CI is +/-3.7 pp, too wide to exclude the observed contrast scale |
| Secondary-analysis length/order | **OPEN — EDITORIAL MAJOR** | Focal result first; detailed T-Web/Tempel/ASTRA diagnostics moved/condensed |
| Uniform monopole objection | **MOSTLY STALE** | Two-sample contrast is invariant; keep separate from environment-dependent label bias |
| Match-radius dedup objection | **STALE/CLOSED** | Caption already distinguishes pre-dedup radius rows from deduped rows |

Parallel dispatch took 37.6 seconds on the critical path versus 96.0 seconds summed (60.8% reduction). An earlier short-SHA launch failed closed before dispatch. No readiness uplift; verified cap remains 74. Full audit and raw reports: `INT_v3/ROUND_2026-07-14-P5-v0.1.130-EXACTPDF-f5b7a1bb-AJ-NONANTHROPIC-CONFIRM/`.

### P2 v1.7.120: Exact-PDF PRD confirmation panel (2026-07-14)

**Input:** exact 10-page PDF at source commit `411c59e01673ede79bf4a93fa97af011d032a426`, source SHA-256 `e9df08c5e46aa91bde70dd8ccc72a7adb5af23b7d4e2099780401b1092f2fa5c`, PDF SHA-256 `2111e62f6eb2423dc1880fad5fa90c8da1feac75ff4b44891573f6d90762cc06`

**Panel:** OpenAI GPT-5.5 **MAJOR REVISIONS** / Gemini 3.1 Pro Preview **MINOR REVISIONS** / Grok 4.3 **MAJOR REVISIONS**. All three successful native-PDF legs were concurrent. Grok required a second file-ingestion attempt; the failed first attempt was not scored. No Anthropic/Claude dispatch or fallback. Independent Codex `gpt-5.6-sol` high is a declared `NOT_RUN` gap because its weekly subscription allowance was exhausted.

**Truth audit:** the central contraction-phase `-35/16` result is supported; the exact appendix already includes the four vertices, per-vertex limits, six-Wick convention, collapsed polynomial, epsilon-order grouping, in-in sign convention, and Li closed-form check. Real remaining gates are publication positioning and external evidence, not an invitation to invent missing calculations.

| Finding | Status | Required action/evidence |
|---|---|---|
| `2.63 sigma` promoted as observational headline | **OPEN — POSITIONING MAJOR** | Demote to illustrative conditional mapping; no survey-level claim without external covariance and third-order transfer |
| "UV-completion independence" | **OPEN — POSITIONING MAJOR** | Limit claim to the contraction-phase coefficient under the specified cubic action |
| Cubic-order bounce transmission | **OPEN — EXTERNAL SCIENCE GATE** | Direct third-order calculation or keep every late-time statement explicitly conditional |
| SPHEREx per-triangle covariance/likelihood | **OPEN — EXTERNAL DATA GATE** | Published covariance/likelihood and justified nuisance model; do not fabricate forecast precision |
| Free-`b_phi` limit | **OPEN — INTERPRETIVE** | Center prior-sensitivity discussion on the evidenced `0.42 sigma` free limit |
| Cai/Li expression provenance | **OPEN — BOUNDED CLARITY** | Compact trusted-expression summary; preserve disclosed printed-polynomial tension |
| Prior-volume section | **OPEN — EDITORIAL** | Condense or move out of main narrative; no evidential language |
| Rough FoG degradation percentage | **REJECTED — UNSAFE** | No paper-specific bound; keep omission explicit instead |
| Immutable archive/DOI | **OPEN — WORKFLOW** | Verified citable bundle and final identifier before submission |

The legacy manifest says `review_commit=worktree` because unrelated repository files were dirty; the reviewed P2 files were clean and exactly committed at `411c59e0`. The content-addressed packet migration is the closure for that harness ambiguity. No readiness uplift is inferred; P2 remains capped at 74. Full audit and typed gap record are in `INT_v3/ROUND_2026-07-14-P2-v1.7.120-EXACTPDF-2111e62f-PRD-NONANTHROPIC-CONFIRM/`.

### P1A v1A.0.120: Exact-PDF CQG Note and PRD venue-control panels (2026-07-14)

**Input:** exact 8-page PDF at source commit `438ce8ec79cb13d7cfa5233671966a30f5b5e45c`, SHA-256 `6472db7741deebd4100fe3191d5ef23a9b0b7960c4284cf53e9e4761f62f535b`

**CQG Note panel:** OpenAI GPT-5.5 **MAJOR REVISIONS** / Gemini 3.1 Pro Preview **MINOR REVISIONS** (one internally MAJOR-tagged item) / Grok 4.3 **ACCEPT**.

**PRD venue-control panel:** OpenAI GPT-5.5 **MAJOR REVISIONS** / Gemini 3.1 Pro Preview **MINOR REVISIONS** (one internally MAJOR-tagged item) / Grok 4.3 **ACCEPT**.

All six legs received the identical native PDF concurrently; the boards are not averaged. No Anthropic/Claude dispatch or fallback. Independent Codex `gpt-5.6-sol` high is a declared NOT_RUN gap because its weekly subscription allowance was exhausted; no substitute verdict was synthesized.

**Truth audit:** the narrow central algebra is supported in essence by all six reports, but several real closures remain. CQG Note is the primary route; PRD's significance concern is an editorial venue-control result.

| Finding | Status | Required evidence |
|---|---|---|
| Unify/focus the Note around algebraic Cartan elimination | **OPEN — STRUCTURAL MAJOR** | Shorter title/abstract/body; standard identities and actual contribution stated plainly |
| Explicit zero-source connection and kernel step | **OPEN — MAJOR** | Display sourced Cartan equation and `e^[I]∧T^[J]=0 => T^I=0` proof for invertible tetrad |
| Above-Planck NJL stress rows | **OPEN — MAJOR** | Delete uncontrolled rows and dependent prose; retain only controlled sub-Planck diagnostics |
| Local all-orders/classical claim conditions | **OPEN — MAJOR** | Initial/boundary/global/quantum exclusions at each broad claim; reduced-vs-off-shell distinction |
| Density motivation/precision | **OPEN — BOUNDED** | Parameterized scaling, illustrative normalization, honest rounding |
| Fierz clarity bridge | **OPEN — BOUNDED** | One conventional-bilinear intermediate line; existing full matrix/sign audit retained |
| Companion/running/NY material and notation | **OPEN — EDITORIAL** | Remove undefined Route-2/3 and pipeline detail; shorten; fix `R R e` artifacts |

No readiness uplift is inferred; the verified external cap remains 62. Raw reports, manifests, declared-gap records, and the full audit are in the two `INT_v3/ROUND_2026-07-14-P1A-v1A.0.120-EXACTPDF-6472db77-*` directories.

### P3 v3.2.0-r5: Venue-correct exact-PDF ApJS panel (2026-07-14)

**Input:** exact 14-page PDF at source commit `7cf60218b521a8154f9ad6ed3b58c0bbc420ab59`, SHA-256 `024931a40e88124f75f2f6872549936e909db0a3b504dbd2e4e68e91878a39dc`

**Panel:** OpenAI GPT-5.5 **MAJOR REVISIONS** / Gemini 3.1 Pro Preview **MINOR REVISIONS** (one internally MAJOR-tagged item) / Grok 4.3 **MINOR REVISIONS**. All three received the native PDF concurrently. No Anthropic/Claude dispatch or fallback. Independent Codex `gpt-5.6-sol` high is a declared NOT_RUN gap because its weekly subscription allowance was exhausted; no substitute verdict was synthesized.

**Truth audit:** three substantive closure classes survive: chance-association/random-shift control; accepted-versus-warning-bearing population comparison using the exact 2,267-row auxiliary product; original-member-separation sensitivity. Final immutable archive/DOI packaging is a workflow gate. Grok's claimed 20,299,153 denominator is an OCR false positive (source/PDF use 20,299,155 throughout), and 7.33% correctly rounds `181/2468`.

| Finding | Status | Required evidence |
|---|---|---|
| Chance-association/random-shift control | **OPEN — MAJOR** | Deterministic script, artifact, radius curve, and tail-row interpretation |
| Warned-versus-accepted comparison | **OPEN — MAJOR** | Script-generated descriptive table/figure; no bias-correction claim |
| Original-member 1-arcsec sensitivity | **OPEN — BOUNDED** | Explicit one-row counterfactual and machine-readable tier/expression |
| Final citable package/DOI | **OPEN — WORKFLOW** | Immutable primary/auxiliary assets, manifests, dictionaries, and final identifier |
| Denominator/7.33% Grok flags | **FALSE / CLOSED** | Direct exact-source/PDF inspection and arithmetic |

No readiness uplift is inferred. Raw reports, manifest, and full source-cited audit are in `INT_v3/ROUND_2026-07-14-P3-v3.2.0-r5-EXACTPDF-024931a4-APJS-NONANTHROPIC-CONFIRM/`; SSOT and the Next.js review timeline were updated with this round.

### P2 v1.7.119: Exact-PDF truth-audit scientific closure (2026-07-14)

**Input:** exact v1.7.118 PDF at commit `9089d65c64752e3a2c69778b72d97ef7c45b4443`, SHA-256 `01107b3d731b945b2aa9ea04ce4e8188282770a87b495c4a1f7ad5b71a4db71a`

**Panel:** OpenAI GPT-5 **MAJOR** / Grok 4.3 **MINOR** / Gemini 2.5 Pro **MINOR** / Codex ChatGPT-subscription `gpt-5.6-sol` high **MAJOR**. No Anthropic/Claude dispatch or fallback.

**Truth audit:** Codex's mixed-orbit counterexample is source-invalid: it breaks Cai's own equal vertex forms and the six-Wick multiplicity. Two genuine manuscript defects were verified (Hamiltonian in-in sign presentation; unsupported `1--8%` quasi-dust band), along with an overstatement, an orbit-wording imprecision, and a stale webform abstract.

| Closure | Status | Result |
|---|---|---|
| Define Hamiltonian integral and use `+2 Im` consistently | **DONE** | Sign-correct; equivalent Lagrangian convention stated |
| Remove unsupported quasi-dust numeric band | **DONE** | Correction explicitly unquantified pending four-vertex calculation |
| Constrain orbit statement to six-Wick convention | **DONE** | Mixed 3-term/6-term convention identified as source-inconsistent |
| Neutralize prior-dependent Bayesian-preference wording | **DONE** | Illustration no longer promoted as established preference |
| Sync `abstract_for_webform.txt` | **DONE** | `-35/16`, conditional `2.63 sigma` recast, no stale `3--5 sigma` claim |

**Output:** v1.7.119, 10 pages, PDF SHA-256 `4434dc8b26ed84324e3fdcf486a9205e49989e5e4dda5efd18436a68ccfd0590`.

Four-pass REVTeX compile and mandatory PDF audit passed: zero errors, undefined references/citations, overfull boxes, raw path-like `\texttt{}` strings, broken HTTP(S) links, or visual collisions across pages 1--10. Full matrix and reproducible SymPy evidence are in `INT_v3/ROUND_2026-07-14-P2-v1.7.118-EXACTPDF-9089d65c-NONANTHROPIC/`.

No verdict improvement is inferred until v1.7.119 receives a fresh exact-PDF panel. Shared site/SSOT/Convex/root-version/mirror updates and git integration were outside this lane.

### P2 v1.7.118: Fresh non-Anthropic editorial closure (2026-07-14)

**Input:** exact 10-page v1.7.117 PDF, SHA-256 `be2a0ba90126feeb896b553f9f9be9128925f75f177260b5c74f829ab940f9cf`

**Raw verdicts preserved:** Grok **REJECT** / Gemini **MAJOR REVISIONS** / OpenAI **MAJOR REVISIONS**

**Truth-audit result:** 0 new scientific/numerical defects; 6 distinct non-scientific closures

**Output:** v1.7.118 PDF, SHA-256 `01107b3d731b945b2aa9ea04ce4e8188282770a87b495c4a1f7ad5b71a4db71a`

| Closure | Status | Scientific/numeric change |
|---|---|---|
| Define $A_{\rm GR}$ and $b_\phi$ | **DONE** | None |
| Pin Cai source to arXiv:0903.0631v2 + retrieval provenance | **DONE** | None |
| Remove Ref. 14 bibliography commentary | **DONE** | None |
| Identify 34.7\% as bias-marginalized $0.687\to0.449$ | **DONE** | None |
| Remove unused $r_t$ | **DONE** | None |
| Clarify separate primordial-transfer-only run | **DONE** | None |

Full BibTeX + three-pass compile and the mandatory 10-page PDF audit passed: zero compile errors, undefined references/citations, overfull boxes, raw `\texttt` paths, broken links, or visual collisions. Open gates remain direct cubic transfer, external Heinrich $\mathrm{Cov}_B$/likelihood, and the camera-ready DOI. No acceptance/minor verdict or readiness increase is inferred. Shared SSOT/site/Convex/version/mirror state and git integration were outside this scoped lane.

### Round 1: Comprehensive Audit (2026-03-02 19:17 PST)

**Files:**
- `2026-03-02_1917PST_comprehensive-audit.md` — Full 10-issue audit with severity ranking
- `2026-03-02_1917PST_claims-table.md` — Derived vs Assumed vs Fit classification

**Issues Identified:** 10 critical/major issues
**Status:** ALL PHASES COMPLETE

| # | Issue | Severity | Status | Resolved In |
|---|-------|----------|--------|-------------|
| 1 | Inflationary dilution vs bounce relic contradiction | FATAL | **DONE** | Phase 2 commit (Option A: keep dilution, drop bounce relic Ω_k/ΔN_eff claims) |
| 2 | $w=-1$ freezing logic not derived | FATAL | **DONE** | Phase 2 commit (downgraded to assumption, logical gap acknowledged) |
| 3 | Parity-odd action dimensional inconsistency | FATAL | **DONE** | Phase 2 commit (abstract formula fixed, Appendix E.4 reconciled) |
| 4 | CMB birefringence: no photon-sector coupling | FATAL | **DONE** | Phase 3 commit (reframed as consistency, not prediction; f(τ_rec) removed) |
| 5 | $f(\tau_{\rm rec})$ undefined / hides 10^120 enhancement | FATAL/MAJOR | **DONE** | Phase 3 commit (formula removed, honest statement about missing coupling) |
| 6 | H0 tension sigma arithmetic wrong (1.4sigma vs 2.9sigma) | MAJOR | **DONE** | `cfeba36` |
| 7 | Fits labeled as "predictions" | MAJOR | **DONE** | Phase 3 commit (all Tables, captions, body text relabeled) |
| 8 | Bayes factor table/equation inconsistency | MAJOR | **DONE** | `cfeba36` |
| 9 | JWST JADES on global dipole plot | MAJOR | **DONE** | `cfeba36` |
| 10 | Marketing tone (Detection Timeline, Discovery Era, fine-tuning scoreboards) | MAJOR | **DONE** | Phase 4 commit (Sec renamed "Observational Forecast", all captions softened, reproducibility honest) |

**Revision phases:**
- [x] Phase 1: Arithmetic / internal consistency (Issues 6, 8, 9, ref [37]) — commit `cfeba36`
- [x] Phase 2: Theory coherence (Issues 1, 2, 3 — Option A adopted)
- [x] Phase 3: Remove unsupported predictions (Issues 4, 5, 7)
- [x] Phase 4: Reproducibility and tone (Issue 10, code release honesty)

### Phase 1 Changes Summary (commit `cfeba36`, 2026-03-02)

**1A — H0 tension sigma arithmetic:**
- 1.4σ → 2.9σ (vs SH0ES) in Abstract, Table I, Table fullcomp, Conclusions
- σ8: 0.8σ → 1.5σ (vs Planck)
- Table I: "Our Solution" → "MCMC Fit", added calculation footnotes
- Sec I.B: "End-to-end derivation" → "Dark energy scale motivation"
- Abstract: "Key predictions" → "accommodates three correlated observational signatures"

**1B — Model-comparison bookkeeping:**
- Table V: clarified as "full tension dataset", defined χ²_eff
- Eq.(38): explicit dataset names
- Table VI: explains χ² magnitude difference vs Table V
- Table fullcomp: ln B footnoted with Planck+BAO caveat

**1C — JWST JADES:**
- Table II: JWST separated below rule, "Not included in dipole fit"
- Fig 2 caption: explicitly excludes JWST
- Conclusions: JWST removed from evidence list

**1D — Stouffer citation:**
- Stouffer 1949 → PDG Statistics Review 2024
- "Discovery Era" → "Full Operations"
- Conclusions: "Detection timeline" paragraph removed, "Known limitations" added

### Phases 2-4 Changes Summary (2026-03-02)

**Phase 2A — Inflation vs bounce relic (Issue 1, Option A):**
- Sec I.B: "values follow from bounce physics" → "motivated by—but not uniquely predicted by—the bounce scenario"
- Sec III.C: Three mechanisms rewritten — ΔN_eff and Ω_k explicitly labeled as phenomenological parameters fit to data; added note that Ω_k~10^{-3} cannot survive 92 e-folds as a direct bounce relic
- Sec VII.D: "not phenomenological degrees of freedom" → honest statement about phenomenological extensions
- Sec X (Falsification): Removed "closed bounce geometry" language for Ω_k
- Table params (Appendix B): "Closed bounce geometry" → "Phenomenological"; "Bounce production" → "Phenomenological"
- Sec IV.A: "from bounce physics" → "phenomenological parameters"

**Phase 2B — w=-1 freezing (Issue 2):**
- Sec II.C.2: Rewrote "Why w=-1" paragraph — now explicitly labeled as assumption, not derivation; logical gap acknowledged (if K_{ab}→0, why doesn't operator vanish?); flagged IR effective action derivation as open problem

**Phase 2C — Dimensional inconsistency (Issue 3):**
- Abstract: Λ_const = (α/M)D_inf → Λ_eff = Ξ M_Pl^2 with Ξ = [(α/M) M_Pl] D_inf (dimensionally correct)
- Sec I.B: Same formula fix
- Sec I.B item 6: Ξ definition corrected with M_Pl factor
- Appendix E.4: Reconciled with main text convention — clarified that M_Pl appears in energy density extraction, not in action coefficient

**Phase 3A — Birefringence coupling + f(τ_rec) (Issues 4, 5):**
- Sec III.A: Removed β = (α/M) D_inf × f(τ_rec) ≈ 0.30° formula entirely; replaced with honest statement that deriving β requires an explicit photon-torsion coupling not yet available; β treated as consistency with Planck, not a prediction
- Conclusions: Updated observational signatures paragraph to match

**Phase 3B — Fits vs predictions (Issue 7):**
- "predicted dipole amplitude" → "fitted dipole amplitude" (JWST paragraph)
- "predicted signal" → "observed/expected signal" (2× instances)
- "our model's predictions" → "our model's MCMC fits" (Fig 3b caption)
- "compared with our prediction" → "compared with our MCMC fit" (Table H0data caption)
- "Method: Theory" → "Method: MCMC fit" (Tables H0data, S8data)
- "predicted signatures" → "parity-odd signatures" (Discussion)
- "falsifiable predictions" → "testable outputs" (Related Work)
- "consistent with predictions" → "consistent with the framework" (Forecast Sec)

**Phase 4A — Timeline/scoreboards (Issue 10):**
- Sec IX title: "Detection Timeline" → "Observational Forecast"
- Fig 7 caption: Added "assuming signals exist at expected levels" + "illustrative" caveat
- Table X caption: Added "(illustrative; assumes signal exists at expected amplitudes)"
- Fig 8 caption: Added "conditional on assumed signal amplitudes" caveat
- Closing sentence: "decisively testable" → "within reach of planned experiments...not that detection is guaranteed"
- Fig 5 caption: "reduces fine-tuning by 115 orders" → "reparameterizes the fine-tuning...not a complete resolution"
- Reproducibility: "bundle in preparation and will be released" → "not yet available but is planned"
- Conclusions Known Limitations: Expanded to include Ω_k/ΔN_eff phenomenological status + code not available

---

## Verification Protocol

After each revision round:
1. Recompile PDF (3-pass + bibtex)
2. Verify 0 undefined references
3. Run dimensional consistency check on all equations
4. Grep for removed language patterns (e.g., "Discovery Era", "uniquely", "no other model")
5. Verify claims table accuracy against revised text
6. Sync website if applicable
7. Update this tracker with resolution status

---

### Round 2: arXiv-Readiness Audit (2026-03-03)

**Reviewer:** Houston Golden (manual PDF audit)
**Manuscript version:** v0.7.0 post-Phase 4
**Overall score:** Borderline → addressed in commit `1e97f96`

**Issues Identified:** 5 structural issues
**Status:** ALL ADDRESSED

| # | Issue | Status | Resolved In |
|---|-------|--------|-------------|
| R2-1 | Title "Comprehensive Framework with Observational Validation" too strong | **DONE** | → "Phenomenological Constraints and Correlated Signatures" |
| R2-2 | Dimensional appendix needed (action → ρΛ chain not shown) | **DONE** | New Appendix I with full dimensional audit |
| R2-3 | "emerges" language overreaches for assumed mechanism | **DONE** | → "is modeled as emerging" throughout |
| R2-4 | Reproducibility package missing | **DONE** | New Appendix J + arxiv/reproducibility/ skeleton |
| R2-5 | Forecast section (Sec IX) high-risk for skepticism | **DONE** | Moved to Appendix H; main text is 1-paragraph summary |

**Additional fixes:**
- "natural consequence of the effective action" → "consistent with a possible photon-sector extension"
- Explicit IR vacuum disclaimer: "This work does not derive the IR effective vacuum term from first principles"
- Table V: added compressed vs full-multipole χ² clarification
- "comprehensive framework" → "phenomenological framework" in Conclusions

**PDF:** 29 pages (up from 28 due to new appendices), 0 undefined references

---

### Round 3: Nuclear Option — Harsh Reviewer #2 Response (2026-03-03)

**Reviewer:** Simulated aggressive Reviewer #2 + Houston's directives
**Manuscript version:** v0.7.0 post-Round 2
**Approach:** Full nuclear option — maximum credibility, no overclaims

**Issues Addressed:** 10 critical issues (from two overlapping audits)

| # | Issue | Status | Resolution |
|---|-------|--------|------------|
| R3-1 | Abstract "deriving dark energy" oversells | **DONE** | → "modeling dark energy as arising from"; w=-1 assumption noted inline |
| R3-2 | Ω_k self-falsifying (92 e-folds kills it) | **DONE** | Ω_k REMOVED from MCMC; fixed to 0; caveat on existing fit values |
| R3-3 | w=-1 by fiat (already labeled assumption) | **DONE** | Already fixed Round 1; verified still in place |
| R3-4 | Galaxy spin 37-order gap | **DONE** | Explicit order-of-magnitude estimate added to Sec II.C.3 |
| R3-5 | β=0.30° in abstract without photon coupling | **DONE** | Numerical value removed from abstract; body text retains as Planck measurement |
| R3-6 | JWST on Figure 2 | **DONE** | Already excluded from fit Round 1; caption caveated |
| R3-7 | Forecast section (pseudoscience risk) | **DONE** | Section IX DELETED entirely; Appendix H DELETED entirely |
| R3-8 | CAMB diff is description not patch | **NOTED** | Disclosed in text; actual patch requires CAMB development |
| R3-9 | A(z) functional form arbitrary | **DONE** | Called "phenomenological" in abstract, body, conclusions |
| R3-10 | Abstract oversells vs body text | **DONE** | Rewrote abstract to match body text honesty |

**Additional changes:**
- Parameter count: 8 → 7 (Ω_k removed); effective 8 → 7
- Model comparison table: footnote explaining values need re-evaluation with Ω_k=0
- Falsification criteria: "Prediction" → "Expected signature" for CMB and galaxy spin
- Triple signature claim: softened to "if they can be connected to the theory quantitatively"
- Conclusions closing: now lists gaps (photon coupling, A_0, w=-1) as blocking issues
- All "resolves" → "partially reduces" for tensions
- "quantitative predictions" → "testable outputs" in intro
- Figure 5 caption: removed Ω_k reference
- Comprehensive comparison table: 8 → 7 parameters
- cobaya_config.yaml: Ω_k removed
- params_bestfit.ini: Ω_k removed

**PDF:** 28 pages (down from 29 — forecast section removed), 0 undefined references

---

### Round 4: Skeptical Coauthor Revision (2026-03-03)

**Reviewer:** Simulated skeptical physics coauthor
**Manuscript version:** v0.8.0 → v0.9.0
**Approach:** Maximum credibility, minimal crackpot heuristics

**Issues Addressed:** 8 task groups

| # | Issue | Status | Resolution |
|---|-------|--------|------------|
| R4-1 | "Geometric Dilution Parameter" trigger phrase | **DONE** | → "Inflationary Suppression Factor" (14 instances) |
| R4-2 | Affiliation implies academic authority | **DONE** | → "Independent Researcher, Los Angeles, California, USA" |
| R4-3 | No Data & Code Availability section | **DONE** | Added before Acknowledgments; rewritten in Round 5 to reference actual artifacts (4 Cobaya YAMLs, Stan model, no CAMB patch) |
| R4-4 | Galaxy spins not framed as contested | **DONE** | Sec III.B rewritten: "Contested Anomaly"; dedicated null-result paragraph (Patel & Desmond, Philcox & Ereza); explicit statement "if null, A0=0 and spin channel doesn't support model" |
| R4-5 | JWST JADES attribution/presentation | **DONE** | Removed from Table II; text clarified as single-field excess, not dipole amplitude; attributed to "Shamir (private communication / preprint)" |
| R4-6 | Appendix C.3 "Tidal Torque Derivation" title | **DONE** | → "Tidal Torque Hypothesis and Phenomenological Mapping"; added bullet list of what's NOT derived |
| R4-7 | Birefringence "natural" language | **DONE** | "natural candidate source" → "qualitatively consistent"; "natural origin" → "origin"; "natural mechanism" → "candidate mechanism" |
| R4-8 | ω² in abstract headline | **DONE** | Removed: $\Leff = \Xi\,\MPl^2 + c_\omega\omega^2$ → $\Leff \approx \Xi\,\MPl^2$ (rotation kept in body/appendix) |

**Additional changes:**
- Claims Classification Table added as Appendix K (Derived vs Assumed vs Fit/Inferred)
- "comprehensive theoretical framework" → "phenomenological framework"
- "Comprehensive Model Comparison" → "Model Comparison"
- "Comprehensive tension resolution" → "MCMC fits compared with nine published measurements"
- "smoking-gun signature" → "distinctive signature"
- "no alternative dark energy model currently reproduces" → "not readily explained by other current dark energy models"
- "detection timelines through 2034" → "tested with forthcoming data from LiteBIRD, CMB-S4, and LSST"
- Joint likelihood appendix projections caveated as "conditional on signal amplitudes not derived from first principles"
- "Simultaneous tension resolution" → "Simultaneous tension reduction"
- Forecast row in comparison table: "Testable by 2030s" → "Testable (amplitudes TBD)"
- "will be released in a companion data package" → removed (all materials now at GitHub)
- 10 appendices (up from 9)

**PDF:** 29 pages, 0 undefined references

---

### Round 5: Reproducibility Captain (2026-03-03)

**Reviewer:** Reproducibility audit (Claude)
**Manuscript version:** v0.9.0
**Approach:** Route 2 (Conservative) — remove claims that depend on non-existent artifacts

**Audit Findings:**
- CAMB "patch" (`camb_modifications.diff`) was prose description, NOT working code
- `cobaya_config.yaml` referenced fictional `SpinTorsionDE` class
- `params_bestfit.ini` values had no backing MCMC chains
- No CNN galaxy classifier exists
- No CMB polarization map analysis was performed
- Actual model IS standard ΛCDM + ΔN_eff, implementable with stock CAMB

**Deliverables Created:**

| File | Description |
|------|------------|
| `reproducibility/cosmology/cobaya_planck.yaml` | Planck-only, stock CAMB |
| `reproducibility/cosmology/cobaya_planck_bao.yaml` | Planck + BAO |
| `reproducibility/cosmology/cobaya_planck_bao_sn.yaml` | Planck + BAO + SN |
| `reproducibility/cosmology/cobaya_full_tension.yaml` | Full tension dataset |
| `reproducibility/cosmology/reproduce_cosmology.sh` | One-command reproduction |
| `reproducibility/galaxy_spins/spin_fit_stan.py` | Hierarchical Bayesian model |
| `reproducibility/galaxy_spins/galaxy_spin_data_DEPRECATED.csv` | DEPRECATED — replaced by GZ DECaLS + Shamir (2024) |
| `research/data_build/build_galaxy_spin_dataset.py` | GZ DECaLS spiral catalog build script |
| `reproducibility/galaxy_spins/reproduce_spins.sh` | One-command reproduction |
| `reproducibility/docs/IMPLEMENTATION_MAP.md` | Claim → code → output mapping |
| `reproducibility/docs/KNOWN_GAPS.md` | Honest gap disclosure |
| `reproducibility/README.md` | Quick start + structure |

**Paper Claims Downgraded:**

| # | Original Claim | Downgraded To |
|---|---------------|---------------|
| RC-1 | "modifies CAMB v1.5 with additional early dark energy" | "stock CAMB (no custom modifications)" |
| RC-2 | "CMB E-B spectra estimated from Planck HFI using SMICA" | "drawn entirely from published literature; we did not perform independent analysis" |
| RC-3 | "CNN classifier (ResNet-18)" in Data & Code Availability | Removed; uses published catalog labels |
| RC-4 | "CAMB patch should be treated as specification" | Removed; no CAMB patch exists |
| RC-5 | CMB null test results presented as original analysis | Attributed to literature (Minami & Komatsu, Eskilt) |
| RC-6 | CMB systematic error budget as original assessment | Attributed to literature |
| RC-7 | "Cobaya v3.3 with modified CAMB v1.5" in Appendix J | "Cobaya v3.5 with stock CAMB" |
| RC-8 | `cobaya_config.yaml` (single fictional file) | 4 real working Cobaya YAMLs |

**Old Files Removed:**
- `arxiv/reproducibility/camb_modifications.diff` (prose, not code)
- `arxiv/reproducibility/cobaya_config.yaml` (fictional SpinTorsionDE class)
- `arxiv/reproducibility/params_bestfit.ini` (values without backing chains)

**Verification:** 0 undefined references, 0 stale CAMB references, 0 claims of original CMB analysis, 29 pages

**Commit:** `dd22d06`, pushed to `origin/main`

---

### Round 6: v1.0 Final — Research Issues + New Citations (2026-03-04)

**Reviewer:** Comprehensive research agent sweep (148 papers, 9 equation checks, 5 cross-checks)
**Manuscript version:** v0.9.1 → v1.0.0
**Approach:** Address 6 substantive issues, add 4 new BibTeX entries, sync all HTML pages

**Issues Addressed:**

| # | Issue | Severity | Status | Resolution |
|---|-------|----------|--------|------------|
| R6-1 | Vacuum energy dilution mechanism framing | HIGH | **DONE** | Sec II.C.2 retitled "Inflationary Suppression of the Primordial Coefficient"; added clarification that Ξ sets primordial coefficient, not "dilutes vacuum energy" |
| R6-2 | H₀ tension baseline (4.4σ vs 4.9σ) | MEDIUM | **VERIFIED** | All references consistently use ~4.9σ; no stale 4.4σ found |
| R6-3 | σ₈ tension framing (CMB vs weak lensing) | MEDIUM | **DONE** | Added explicit weak lensing context in Sec III.C: KiDS-1000 (0.759) and DES Y3 (0.776) |
| R6-4 | MCMC = standard ΔNeff extension disclosure | MEDIUM | **DONE** | Added "Statistical equivalence" paragraph in Sec VII.B; explicitly states phenomenologically equivalent to any additional relativistic species model |
| R6-5 | N=92 motivation and breakdown | MEDIUM | **DONE** | Added specific decomposition: ~55-60 observable + ~30 pre-observable e-folds; labeled as fitted parameter |
| R6-6 | Conjunctive falsification criterion | LOW | **VERIFIED** | Already present in Sec VIII.F (lines 859-872); no changes needed |

**New Citations Added (4 BibTeX entries):**

| Citation | arXiv | Where Cited | Content |
|----------|-------|-------------|---------|
| Yin et al. 2026 | 2601.13624 | Sec III.A (birefringence), Sec XI (related work), Conclusions | Birefringence + EDE joint constraints |
| Diego-Palazuelos & Komatsu 2025 | 2509.13654 | Sec III.A, Sec XI, Conclusions | ACT DR6 β=0.215°±0.074° (2.9σ) |
| DESI DR2 2025 | 2503.14738 | Sec I (intro), Sec XII.4 (open questions), Conclusions | Strengthened dynamical DE evidence |
| Sanyal et al. 2026 | 2602.15924 | Sec XI (torsion cosmology) | Cosmic hysteresis in f(T) bounce |

**Also fixed:** Carroll1998 reference (was cited but missing from .bib)

**Version tracking:**
- `version.json` → v1.0.0
- `versions/manifest.json` → v1.0.0 entry added
- `main.tex` → \paperVersion{v1.0.0}, \date{March 4, 2026}
- Reproducibility URLs → tree/v1.0.0/reproducibility
- PDF recompiled: 31 pages, 0 undefined references, 51 bibliography entries

**Verification:**
- `grep "undefined" main.log` = 0
- All 4.9σ consistent throughout
- No "Geometric Dilution" anywhere
- All HTML pages synced

---

### Round 7: v1.5.0 — Manuscript Update with Frozen MCMC + Theory Audit (2026-03-12)

**Reviewer:** Internal (Claude + Houston Golden)
**Manuscript version:** v1.3.0 → v1.5.0
**Approach:** Integrate two frozen MCMC datasets + Monte Carlo sensitivity scan + theory audit results

**Frozen Datasets Used:**
- full_tension: 175,545 samples, 6 chains, R̂−1 < 0.001, ESS > 6,000 (frozen 2026-03-11)
- planck_bao_sn: 132,949 samples, 6 chains, R̂−1 < 0.003, ESS > 4,600 (frozen 2026-03-12)
- planck_only: [PENDING — running]
- planck_bao: [PENDING — paused]

**Changes Made:**

| # | Change | Location | Details |
|---|--------|----------|---------|
| R7-1 | Version/date update | Line 1, metadata | v1.3.0 → v1.5.0, March 9 → March 12 |
| R7-2 | Abstract updated | Abstract | Replaced "236,622 samples, 64 chains" with frozen dataset specifics; added Monte Carlo scan mention |
| R7-3 | Executive summary footnote | Table I | Added verification footnote: H0=67.68/67.79 from frozen chains |
| R7-4 | MCMC configuration updated | Sec VII.B | Added frozen dataset counts, Cobaya v3.6.1 verification details |
| R7-5 | New verification subsection | Sec VII (new \subsection) | `\subsection{Independent Verification Results}` with Table `\ref{tab:verification}`, two figures, narrative |
| R7-6 | New verification table | Table (new) | Both frozen dataset parameter values; [PENDING] markers for planck_only/planck_bao |
| R7-7 | ΔNeff viability figure inserted | Sec VII | `fig_dneff_viability_two_frozen.pdf` — posteriors + normalized shifts |
| R7-8 | Dataset comparison figure inserted | Sec VII | `cosmology_dataset_comparison_two_frozen.pdf` — 3-panel H0/dNeff/S8 |
| R7-9 | Fine-tuning section updated | Discussion | Added Monte Carlo scan quantification (100K samples, 2.2% viable, Spearman ρ=0.996) |
| R7-10 | Sensitivity figure inserted | Discussion | `vacuum_scale_sensitivity.pdf` — 4-panel parameter scan |
| R7-11 | Limit behavior subsection | Discussion (new) | Table `\ref{tab:limits}` with 5 limits; dimensional analysis summary (10/12 + 2 noted) |
| R7-12 | Conclusions updated | Conclusions | Observational context + fine-tuning paragraphs updated with frozen dataset results |
| R7-13 | Fisher-matrix caveat | Sec XIII (Limitations) | Updated to note full posteriors now available from verification |
| R7-14 | ΔNeff range updated | Sec XIV (Future) | Original 0.1–0.5 range noted as unsupported by full posterior; frozen results cited |
| R7-15 | Reproducibility URLs | Throughout (4 occurrences) | v1.3.0 → v1.5.0 |
| R7-16 | Appendix B parameter table | Table `\ref{tab:params}` | Added footnotes linking original Fisher-matrix values to frozen verification values |
| R7-17 | Appendix K claims table | Table `\ref{tab:claims}` | Updated ΔNeff and H0/σ8 entries with frozen verification values; added verification rows |

**Figures Created:**
- `paper/figures/cosmology_dataset_comparison_two_frozen.pdf` — 3-panel comparison
- `paper/figures/fig_dneff_viability_two_frozen.pdf` — 2-panel ΔNeff posteriors
- `paper/figures/vacuum_scale_sensitivity.pdf` — 4-panel Monte Carlo sensitivity scan

**Theory Audit Outputs Integrated:**
- `theory_claims_do_and_do_not_support.md` — 10 supported + 8 unsupported claims
- `theory_results_integration_note.md` — Guidance for connecting theory to MCMC
- Monte Carlo sensitivity scan (100K samples) results
- Dimensional audit (10/12 consistent + 2 noted)
- 5 limit behavior checks (all pass)

**Still Pending (waiting on running chains):**
- planck_only results (running, ~20-30h to convergence)
- planck_bao results (paused, will resume after planck_only freezes)
- Final cross-dataset comparison with all 4 datasets
- Complete Appendix B table with all 4 dataset columns
- Final abstract/conclusions with full quantitative summary

**PDF Status:** Compilation pending (Step 7)

---

### Round 8: v1.6.0 — Track C Integration + Early-Structure Future Work (2026-03-13)

**Reviewer:** Internal (Claude + Houston Golden)
**Manuscript version:** v1.5.0 → v1.6.0
**Approach:** Integrate audited Track C consistency check + honest early-structure future-work paragraph

**Preceding Audits:**
- Track C method audit: `research/extensions/track_C_parity_cmb/method_audit.md`
- Track C likelihood audit: `research/extensions/track_C_parity_cmb/likelihood_audit.md`
- Track C result classification: `research/extensions/track_C_parity_cmb/result_classification.md`
- Track C paper integration recommendation: `research/extensions/track_C_parity_cmb/paper_integration_recommendation.md`
- Early-structure scale mismatch: `research/extensions/early_structure_program/scale_mismatch_derivation.md`
- Early-structure no-go decision: `research/extensions/early_structure_program/no_go_or_narrow_window_decision.md`
- Early-structure paper integration: `research/extensions/early_structure_program/current_paper_bridge_integration.md`

**Changes Made:**

| # | Change | Location | Details |
|---|--------|----------|---------|
| R8-1 | New subsection: Cosmic Birefringence Consistency Check | Discussion (Sec 10, new subsection before Distance Measures) | 2 paragraphs + 1 figure; combines published Planck+ACT birefringence, translates to f_photon ≈ 1.7; explicitly labeled as consistency check, not inference |
| R8-2 | New figure: consistency_window_birefringence.pdf | Discussion | f_photon vs β with observational bands; caption calls it "phenomenological consistency check, not statistical inference" |
| R8-3 | Early-structure future-work paragraph | Sec 11.4 (Bounce-to-Inflation Transition Dynamics) | New bullet point: P(k) features at k ~ 10^15 Mpc^-1 from N_tot=92; sub-asteroid PBH window; perturbation calculation needed |
| R8-4 | Claims table update | Appendix K | New row: f_photon ≈ 1.7 classified as "Consistency check" |
| R8-5 | Conclusions update | Conclusions (Observational signatures paragraph) | Added sentence referencing Sec 10.X consistency check and f_photon ≈ 1.7 |
| R8-6 | Version bump | Throughout | v1.5.0 → v1.6.0, date → March 13, 2026 |

**Language Audit (all passed):**
- Track C: "consistency check" only, never "constraint" or "inference"
- Early structure: future work only, no SMBH/PBH claims
- ΔN_eff: "consistent with zero" maintained
- Galaxy spins: "contested anomaly" maintained
- f_photon: "requires" not "measures"
- Combined β: "combining published measurements" not "our analysis"

**What Was NOT Included (by design):**
- No phenomenological window analysis plots (SMBH/PBH direction is a no-go for framework)
- No beta_posterior or geff_posterior figures (labeled "posterior" but no inference performed)
- No EB shape comparison figure (forward model without data overlay)
- No MCMC for Track C (zero of 5 necessary conditions met)
- No SMBH/JWST/PBH claims in main text

**Still Pending:**
- planck_only chains (running, ETA ~March 19-20)
- planck_bao chains (paused, will resume after planck_only freezes)
- Final cross-dataset table with all 4 columns
- Referee-style external review

---

## Future Rounds

*Add new sections here as additional reviews are conducted.*
