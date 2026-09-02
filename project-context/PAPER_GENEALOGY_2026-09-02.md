# Paper genealogy — dated lineage of the Big Bounce paper lineup

**Date:** 2026-09-02
**Scope:** Complete dated genealogy of every paper/manuscript identifier the
program has ever carried, from the first commit (`36cfb8d7`, 2025-07-22) to
today. This document records **facts and citations only** — it does not
judge scientific value, correctness, or publication-worthiness of any
version. That judgment is a separate agent's job.

**Method:** mined from `git log --all` (4,033+ commits across the full
history), `project-context/PAPER_LINEAGE_2026-08-05.md`,
`project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`,
`project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md`,
`project-context/bounce_portfolio_strategy.md`,
`project-context/FUTURE_PAPERS.md`,
`project-context/peer-reviews/INT_v3/ROUND_2026-07-13-M44-NONANTHROPIC/P1_SPLIT_CLOSURE.md`,
`project-context/SSOT/index.md` (and its full historical append-only ledger),
`project-context/paper_registry.json` history, `research/paper1_salvage_alp/`,
`project-context/HOUSTON_SIGN_OFF_BRIEF.md`, `project-context/CURRENT_STATUS.md`,
and every `\title{...}` line found via `git show <sha>:<path>` across every
`.tex` file ever committed.

---

## 1. Timeline table

| Date | Lineup at that time | What changed vs previous | Recorded reason (quote/cite) | Driver |
|---|---|---|---|---|
| **2025-07-22** | 1 paper: *"Geometric Dark Energy from Spin-Torsion Cosmology: A Comprehensive Framework with Observational Validation"* — single sprawling manuscript claiming H₀ tension resolution, σ₈ tension resolution, a black-hole-universe origin, JWST 65/35% galaxy-spin evidence, CMB E-B correlations at 2.8σ, galaxy spin asymmetry at 3.2σ | Program origin | Genesis document. Abstract: "potentially addressing the Hubble and σ₈ tensions... universe originated from the interior of a rotating black hole... Recent JWST observations showing a 65-35% galaxy spin asymmetry... provide compelling preliminary evidence" | Houston-authored initial draft (`bigbounce.md`, commit `36cfb8d7`, 2025-07-22) |
| **2025-11-10 → 2025-11-11** | Still 1 paper, same broad claim set | "Major scholarly revisions: rigor, accuracy, and transparency" | Commit `e94dca76` message; ArXiv-submission editing pass, mobile/HTML cleanup | Houston-directed editing cycle (PR merges #2–#5) |
| **2026-02-13 → 2026-02-18** | Still 1 paper (site regeneration cycle via "Astrophysics Paper Squad" agents: astro-atlas/astro-tensor/astro-sage/astro-keane/astro-nova) | Literature survey, math validation, observational-constraints passes, peer-review-agent pass; no title/scope change recorded | Commits `c51ef0ab`…`f6c506b1` ("Literature Review," "Mathematical Validation," "Peer Review — Methodology and Mathematical Rigor Assessment") | Hubify multi-agent "Astrophysics Paper Squad" workflow |
| **2026-02-26** | Still 1 paper | First LaTeX-formal version: `research/paper_1_01_archive/main.tex`, title *"Geometric Dark Energy from Spin-Torsion Cosmology: Phenomenological Constraints and Correlated Signatures"* | Commit `b4d4c601` "feat: arXiv-ready LaTeX paper + preview page" | Program conversion to arXiv-style LaTeX |
| **2026-03-17** | Still nominally 1 paper, but internal salvage audit begins | `research/paper1_salvage_alp/final_verdict.md`: *"Can Paper 1 be salvaged honestly? YES. But only by removing roughly half its claims."* Retained: ECH bounce cosmology, "13 barriers" DE-derivation closure, spectator-ALP birefringence (β≈0.27°), MCMC constraints, falsification program. Removed: all DE-derivation claims (Λ_eff formula), H₀=69.2/σ₈=0.785 tension-reduction claims, galaxy-spin predictions (9+ OOM gap), ALP-as-DE interpretation, fine-tuning claim (10¹²⁰→10⁵), correlated-axes prediction | `research/paper1_salvage_alp/final_verdict.md` (2026-03-17), commit `af25f807` "v1.6.0 — complete project intelligence dossier, 17 research branches, structural closure" | Internal self-audit — first documented claim-narrowing event |
| **2026-03-19** | 3 papers appear: Paper 2 (f_NL forecast), Paper 3, Paper 5 all compiled/deployed | New paper family created from the salvage split: `research/focused_paper_source_integration/` (P2 lineage) and early P3/P5 material | Commit `7e9a9363` "Papers 2, 3, 5 all compiled — PDFs deployed to website"; commit `88794c9b` "compiled focused paper" | Program split from salvage audit |
| **2026-03-24** | Portfolio-strategy framing introduced (still working toward P1/P2/P3/P4 lineup) | `bounce_portfolio_strategy.md` written: *"Old framing: 'Our ECH Model B predicts f_NL = -35/8. Single point of failure.' New framing: 'Bounce cosmology has a portfolio of testable predictions across multiple models...'"* Introduces Tracks A–D (f_NL forecast, quintom bounce-DE, PBH+GW, cuscuton) | `project-context/bounce_portfolio_strategy.md` (2026-03-24) — **earliest explicit statement of the "prove bounce cosmology beats inflation, not one model" mission**, cited verbatim in `CLAUDE.md` today | Houston's "strategic realization" per the doc's own header |
| **2026-03-28 → 2026-04-03** | P3 (anomaly), P4 (chirality) drafted | `caaa0618` "Paper 3 draft + gold anomalies"; `202af495` "chirality paper draft"; `b1648585` "Paper 4 chirality (798 lines)"; `ee91bbab` "Paper 3 draft — 735 lines, multi-survey anomaly catalog" (`pipelines/p3_anomaly_engine/paper3_draft.tex`, title *"A Multi-Survey Autoencoder Anomaly-Candidate Catalog: 268,519 Reconstruction-Outlier Sources and CMB Map Patches"*) | New commits, no retirement doc yet | Discovery-science expansion |
| **2026-04-17** | **4-paper board**: Paper 1 (Spin-Torsion Cosmology, v2.3.0), Paper 2 (f_NL Forecast), Paper 3 (Multi-Survey Anomaly Catalog: "8 surveys · 37.3M sources · 319,443 anomalies"), Paper 4 (Galaxy Chirality Catalog: "8.47M galaxies") | First SSOT dashboard created: `project-context/SSOT/index.md` restructured from ad hoc status files | Commit `ae21ac55` "SSOT: restructure paper status into project-context/SSOT/ tree"; SSOT header: "Last authoritative update: 2026-04-17" | Program-management reorganization |
| **2026-05-01** | Still 4 papers, reproducibility deposit round | `a3cb2c27` "reproducibility deposit — NaMaster 500MC scripts/seeds/masks + chirality_v2 weights..." | pre-split reproducibility hardening | — |
| **2026-05-05** | **P1 splits into P1A + P1B** → 5-paper board | `599144b2` "feat(R43-P1-split): add P1A ECH no-go + P1B MCMC companion split files v1A.0.1 v1B.0.1" | R43 review round decision to separate the algebraic no-go result (P1A) from the computational/MCMC companion (P1B) | Internal R43 review-round recommendation |
| **2026-05-15** | **P5 bootstrapped** → 6-paper board reached | `059c3458` "feat(p5): bootstrap — first matched chirality × DESI DR1 catalog + analyses" | New standalone downstream analysis of P4's chirality labels vs. DESIVAST void environment | Discovery-driven expansion from P4 |
| **2026-05-22 → 2026-05-26** | 6-paper board formalized: P1A, P1B, P2, P3, P4, P5 all at "95% / external 5-vendor clean" milestone | `project-context/HOUSTON_SIGN_OFF_BRIEF.md` created (tick 177) then refreshed (tick 210): *"ALL 6 PAPERS HAVE REAL EXTERNAL 5-VENDOR R-ROUNDS LANDED"* | `HOUSTON_SIGN_OFF_BRIEF.md` (now superseded, marked "May-vintage… DO NOT USE FOR SUBMISSION") | Autonomous drive-to-100 review-loop cron |
| **2026-07-08** | **P1A + P1B merge into unified "P1U"** — board temporarily drops to 5 identifiers (P1U, P2, P3, P4, P5) | `cc2b7f88` "feat(paper-1 unified v1U.0.1): P1B merged into P1A per unanimous reviewer recommendation (Houston-approved) — 58pp self-contained... kills companion-reliance + standalone-scope rejection classes." Title: *"Channel-Level Constraints on Four Enumerated Minimal Einstein–Cartan–Holst Dark-Energy Routes Under Stated Assumptions..."* (`arxiv/paper1_unified.tex`) | Commit message; unanimous reviewer recommendation to eliminate the two-paper "companion-reliance" rejection class | Internal reviewer-board recommendation, Houston-approved |
| **2026-07-11** | P1U still live, campaign compute-heavy phase | Directive L: "the bar be that all papers are pushed to Accepted by all reviewers" — restores the accept-bar and opens the "open-compute campaign" (P4 e2e injection, P2 channel-native Fisher, P3 re-inference, P5 RSD reconstruction, P1U NJL gap equation) | `CLAUDE.md` standing directive L (2026-07-11, Houston explicit) | Houston directive |
| **2026-07-14** | **P1U splits back into P1A + P1B** (restoring the six-paper topology) — P1A narrowed to 3 retained results; the 14-barrier no-go catalog, R2/R3 DE closures, ALP/MCMC material, galaxy payload all retired from the reader-visible paper | `project-context/peer-reviews/INT_v3/ROUND_2026-07-13-M44-NONANTHROPIC/P1_SPLIT_CLOSURE.md`: *"The M44 P1U reviews were most persuasive where they identified a mismatch between the manuscript's broad four-route rhetoric and its actually derived results. The closure therefore removes the unsupported claim surface rather than relabeling it."* P1A output `v1A.0.116`; P1B `v1B.0.105`. `arxiv/paper1_unified.tex` explicitly "was not edited" — content preserved, not deleted | M44 non-Anthropic external review round | External (non-Anthropic) review board finding |
| **2026-07-14 (same day)** | **P3 narrows**: multi-survey autoencoder draft (268,519 outliers / 37.3M scanned) → focused DESI public-ID recovery note | `913f5033` "feat(p3): narrow ApJS catalog submission" then `3f5582c2` "docs(p3): publish focused DESI catalog manuscript" — 2,387 lines cut to a public-ID-first, provenance-first note (net 813 insertions replacing 1,777 deletions) | `PAPER_LINEAGE_2026-08-05.md` §3.3: "provenance reconciliation issues (LAMOST released-but-excluded rows, Gaia excision, '37.3M vs 36.93M' read/scored mismatches) kept surfacing" across multiple review rounds | Sustained internal/external review pressure on provenance |
| **2026-07-16** | **P1B pivots identity again**: from "MCMC companion" to standalone software metapaper `namaster-proof` | `7c8bd0ca` "feat(p1b): release namaster-proof software metapaper" | Software-paper rescue architecture (`b52f1515` "docs(p1b): define software-paper rescue architecture") | Editorial decision — old MCMC companion content moved out to `arxiv/paper1b_mcmc_companion.tex` (kept alive as a separate artifact), P1B re-registered as `arxiv/paper1b_namaster_proof.tex` |
| **2026-07-24** | 6-paper board, wave-1 arXiv-kit prep. Paper titles now stable: P1A *"Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity"*; P1B *"namaster-proof: Exact pseudo-Cℓ Window Inference and Tamper-Evident Provenance..."*; P2 *"The Exact Matter-Contraction Non-Gaussian Amplitude..."*; P3 *"Public-ID Recovery for a Historical DESI DR1 Anomaly List"*; P4 *"An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals"*; P5 *"A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1"* | Convex sync, target-journal assignment (CQG, JORS, PRD, ApJS, ApJS, AJ) | `project-context/paper_registry.json` schema v2, per-paper `target_journal`/`review_profile` fields | Journal-route matching |
| **2026-08-03** | **Publication-architecture reset**: six-equal-papers framing declared invalid | `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`: *"The current six-paper count is not a scientific result and should not govern what gets submitted. It is the residue of earlier splits, rescue operations, and downstream dependencies."* New framing: **3 research programs** (bounce theory / survey discovery / galaxy chirality) with primary + specialist + supporting-release roles. P3 demoted from standalone-submission to "Supporting Data Release · DESI Public-ID Recovery," not a standalone paper | `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` (Houston decision draft, approved 2026-08-04 with "continue all best next steps") | Houston-approved architecture reset |
| **2026-08-04** | Three-program map approved; `CLAUDE.md` updated to require reading the reset doc before any paper work | `f71eb6b4` "docs: define publication and release architecture"; `accf62f3` "docs(plan): record production architecture release"; `b68e714e` "docs(plan): approve three-program publication architecture" | `project-context/PUBLICATION_AND_RELEASE_MASTER_MAP_2026-08-04.md` | Houston approval |
| **2026-08-05** | **P1C created**: 14-barrier no-go catalog resurrected as a standalone 7th manuscript, extracted from the frozen `arxiv/paper1_unified.tex` | `c1b6258c` "feat(p1c): resurrect no-go barrier survey as standalone draft (extraction from paper1_unified)". Title: *"A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology"* | `project-context/PAPER_LINEAGE_2026-08-05.md` §4(a) resurrection recommendation + Decision record: "Houston granted full decision authority... 1. No-go survey paper: RESURRECT... Working id: P1C" | Directive Q4 audit ("nothing viable gets lost") + Houston's delegated decision authority |
| **2026-08-05 (same day)** | P1B-MCMC companion surfaced as first-class supporting link (not a full paper) | `cbe93641` "feat(site): surface MCMC validation companion as first-class bounce-theory supporting work" | `paper_registry.json` `companion_manuscripts.P1B-MCMC` note: "Not one of the six campaign papers... surfaced 2026-08-05 as a first-class supporting validation dossier under the bounce-theory research program" | Same Q4 audit, resurrection recommendation §2 |
| **2026-08-06** | **P1C given first-class review infrastructure** (auxiliary draft-paper registry, portfolio receipts) so it can be reviewed without being counted among "the canonical six" | `833474a7` "feat(review): auxiliary draft-paper registry so the engine can review P1C without touching the canonical six"; `d5e247bc` "feat(preflight): first-class draft-paper records in portfolio receipts (P1C reviewable)" | Commit messages | Infrastructure decision to keep P1C's review cycle separate from the six-paper campaign accounting |
| **2026-08-08 → 2026-09-02** | P1C undergoes its own R-round cycle (R12, R13...) while the anomaly-flagship rebuild proceeds in parallel under `pipelines/p1_highz_tracers/` / `projects/desi-dr1-anomalies/` | R12 (2026-08-08): 15 genuinely-new-real findings closed in v1C.0.15, including a load-bearing correction to the on-shell torsion computation — *"THE REFEREE WAS CORRECT... THE PHYSICS CONCLUSION SURVIVES."* R13 (2026-09-02): "PARTIAL closure," erratum note added, version at v1C.0.16 | `project-context/SSOT/paper-1c/status.md`; commits `0a550340`, `cda7c913` (2026-09-02) | Ongoing multi-vendor review board (Claude INT, Grok API, Gemini API) |
| **2026-08-26** | Anomaly-flagship rebuild ("AUG-011" sealed-contract clean rerun) reaches a selected characterization sample: 3,810 TARGETIDs at `anomaly_score >= 8.0` out of 27,547,223 unique TARGETIDs universe | `project-context/ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md`: "This is a characterization cohort, not a discovery list and not a claim that every row is astrophysical." Contract sealed commit `568a33bf` (2026-08-05); completed 2026-08-07 per `PAPER_LINEAGE_2026-08-05.md` | `project-context/ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md`, `project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md` | Compute result — deterministic post-dedup selection replay |
| **2026-09-02 (today)** | **Current state**: 6 campaign papers (P1A, P1B, P2, P3-as-support, P4, P5) at readiness 95 pending Houston sign-off, per `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`'s three-program hierarchy; **P1C** a live 7th draft manuscript in its own review pipeline (v1C.0.16, R13 partial closure); the rebuilt DESI anomaly-discovery flagship still mid-manuscript (characterization sample selected, manuscript claims pending); the P1B-MCMC companion alive as a supporting artifact, not a standalone paper; "Paper 7" (self-improving-review meta-paper) still idea-only | `project-context/SSOT/index.md` "Preserved six-candidate board" table; `project-context/SSOT/paper-1c/status.md`; `project-context/NEXT_SESSION_PROMPT_2026-09-02.md` | Ongoing autonomous review loop + Houston directives |

---

## 2. Per-paper evolution threads

### P1 lineage: original → salvage → P1U → P1A/P1B split → P1U merge → P1A/P1B re-split → P1C spinoff

This is the single most-forked identifier in the program. Full title history,
in chronological order of the source file's first appearance:

1. **2025-07-22, `bigbounce.md`** — *"Geometric Dark Energy from Spin-Torsion Cosmology: A Comprehensive Framework with Observational Validation."* Claim: unified DE derivation + H₀/σ₈ tension resolution + black-hole-universe origin + CMB E-B correlation + galaxy-spin dipole, "compelling preliminary evidence" cited from JWST 65/35% asymmetry claims. Commit `36cfb8d7`.
2. **2026-02-26, `research/paper_1_01_archive/main.tex`** — *"Geometric Dark Energy from Spin-Torsion Cosmology: Phenomenological Constraints and Correlated Signatures."* First LaTeX/arXiv-formatted version, same broad program. Commit `b4d4c601`.
3. **~2026-03 (undated but pre-salvage), `research/paper_1_2_archive/paper_1_2_draft.tex`** — *"Geometric Dark Energy: Phenomenological Viability, Systematic Closures, and Requirements for Completion."* An intermediate draft already signaling internal awareness of "systematic closures" needed.
4. **2026-03-17, salvage audit** — `research/paper1_salvage_alp/final_verdict.md` narrows the paper to 3 parts: ECH bounce cosmology, 13-barrier structural closure, spectator-ALP birefringence. Explicitly strips DE-derivation, H₀=69.2/σ₈=0.785, galaxy-spin predictions (9+ OOM gap), ALP-as-DE claim, fine-tuning claim, correlated-axes prediction. Quote: *"This is a net improvement. The remaining paper is smaller, sharper, and more honest."*
5. **`arxiv_v2/main.tex` (undated, post-salvage)** — *"Spin-Torsion Bounce Cosmology: Fourteen Structural Barriers and One Surviving Prediction."* This is the direct output of the salvage: the 13-barrier survey grows to 14 with the ALP birefringence framed as the one surviving positive prediction.
6. **2026-05-05, P1 splits** — `599144b2`: P1A ("ECH no-go") + P1B ("MCMC companion") v1A.0.1 / v1B.0.1.
7. **2026-07-08, P1U merge** — `cc2b7f88`: P1A+P1B merge into `arxiv/paper1_unified.tex`, title *"Channel-Level Constraints on Four Enumerated Minimal Einstein–Cartan–Holst Dark-Energy Routes Under Stated Assumptions (Amplitude Closure for R1–R3, Naturalness Closure for R4), and Perturbation Transparency for Scalar Matter."* This is the fullest, most complex title the program ever carried for this thread — 58pp, self-contained. Reason (commit message): "per unanimous reviewer recommendation... kills companion-reliance + standalone-scope rejection classes."
8. **2026-07-14, P1U re-split** — M44 non-Anthropic review finds the broad four-route rhetoric outran what was tightly derived (`P1_SPLIT_CLOSURE.md`). P1A narrows to *"Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity: Spin-Sourced Contact and Zero-Spin Scalar Branches"* — retaining only torsion elimination, the axial contact operator, and a classical transparency identity. Everything else (barrier catalog, R2/R3 closures, ALP/MCMC, galaxy payload) explicitly retired from the reader-visible paper but preserved unedited in `arxiv/paper1_unified.tex`.
9. **2026-07-16, P1B re-identity** — P1B stops being the MCMC companion and becomes *"namaster-proof: Exact pseudo-Cℓ Window Inference and Tamper-Evident Provenance for Reproducible Spin-2 Analyses"* — a software metapaper (`arxiv/paper1b_namaster_proof.tex`), routed to JORS instead of JCAP. The old MCMC-companion content survives as a separate file, `arxiv/paper1b_mcmc_companion.tex` (title: *"Reproducible Cosmological Proxy and Pipeline Checks: Stock-CAMB ΛCDM+ΔN_eff MCMC, Synthetic NaMaster Recovery, and a Generic Spectator-ALP Birefringence Fit"*), which is neither deleted nor promoted — it becomes an orphan-flagged companion manuscript (`paper_registry.json` → `companion_manuscripts.P1B-MCMC`).
10. **2026-08-05, P1C spinoff** — the 14-barrier catalog, still fully intact and unedited inside `arxiv/paper1_unified.tex`, is extracted into a standalone draft: *"A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and Bounce Phenomenology"* (`arxiv/paper1c_nogo_survey/main.tex`). Working id P1C. Status as of 2026-09-02: v1C.0.16, mid-review (R13 partial closure), not yet in the six-paper campaign roster.

**Where the claims went:**
- Black-hole-universe origin, H₀/σ₈ tension resolution, 65/35% JWST claim, correlated-axes prediction — **dropped entirely** at the 2026-03-17 salvage; no surviving paper carries them. No separate retirement doc exists for this step beyond `final_verdict.md` itself.
- Torsion elimination / axial contact operator / transparency identity — **P1A** today.
- 14-barrier no-go survey — **P1C** today (drafted, mid-review).
- MCMC/CAMB/synthetic-NaMaster/spectator-ALP validation — split across **P1B-MCMC companion** (orphan-flagged, alive but not a campaign paper) and folded verification machinery inside **P1B/namaster-proof**.
- Galaxy-spin dipole test (Shamir CW/CCW) — the actual analysis migrated to **P4**, cited (not duplicated) from P1U's now-retired barrier section (`PAPER_LINEAGE_2026-08-05.md` §3.2).

### P2 (f_NL forecast) — comparatively stable

- **2026-03-19 / 2026-03-24**, first compiled as part of the salvage-driven expansion (`7e9a9363`, `88794c9b`); sourced from `research/focused_paper_source_integration/`.
- Earlier working title inside that directory: `02_full_draft.tex` and `paper2_alp_birefringence.tex` (*"Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts"*) show the P2 slot briefly also held ALP-birefringence content before the program's final split settled the ALP material with the P1 thread (companion manuscript) and P2 with the non-Gaussianity result.
- Current (2026-07-24 onward) title: *"The Exact Matter-Contraction Non-Gaussian Amplitude: Four-Vertex Derivation and Conditional Large-Scale-Structure Mapping"* (`research/focused_paper_source_integration/02_full_draft.tex`). f_NL = −35/8 became −35/16 after an "exact four-vertex rederivation" (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`: *"An exact four-vertex rederivation of f_NL^local = -35/16"*) — note this is a **narrower, more exact value** than the `bounce_portfolio_strategy.md` (2026-03-24) flagship number f_NL = −35/8; the change is visible in `CLAUDE.md` directive-I6's own trap note about a stale `-35/8` PNG figure surviving "TWO review rounds" past the text's move to `-35/16` (fixed v1A.0.112, 2026-07-06).
- Never split or retired — the only identifier that has run continuously as "P2" since the 2026-04-17 SSOT founding.

### P3 (anomaly survey) — three distinct scopes under one label

1. **2026-03-28 → 2026-04-03**, first draft: `pipelines/p3_anomaly_engine/paper3_draft.tex`, title *"A Multi-Survey Autoencoder Anomaly-Candidate Catalog: 268,519 Reconstruction-Outlier Sources and CMB Map Patches."* SSOT (2026-04-17) records it as "8 surveys · 37.3M sources · 319,443 anomalies."
2. **2026-07-14**, narrowed twice same day: `913f5033` then `3f5582c2` replace it with `pipelines/p3_anomaly_engine/paper3_apjs.tex`, title *"Public-ID Recovery for a Historical DESI DR1 Anomaly List: 170 High-Coordinate-Consistency Core and 11 Lower-Confidence Positional Associations."* Reason cited (`PAPER_LINEAGE_2026-08-05.md` §3.3): sustained provenance-reconciliation problems (LAMOST released-but-excluded rows, Gaia excision, 37.3M-vs-36.93M mismatch) across review rounds.
3. **2026-08-03**, demoted from standalone submission to **Supporting Data Release · DESI Public-ID Recovery** for a not-yet-written rebuilt anomaly-discovery flagship (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`). `paper_registry.json` schema v2 sets `"standalone_submission": false` and `"integration_target": "Rebuilt DESI anomaly-science flagship"`.
4. **2026-08-05 → 2026-09-02**, the actual discovery-science line lives separately under `pipelines/p1_highz_tracers/` and `projects/desi-dr1-anomalies/`, rebuilt under a sealed-contract clean rerun ("AUG-011," sealed 2026-08-05, completed 2026-08-07: 36,634 verified receipts). Selected characterization sample fixed 2026-08-26 at 3,810 TARGETIDs (`anomaly_score >= 8.0`). This flagship manuscript is not yet written; its architecture is `project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md`.

### P4 (galaxy chirality) — stable core, growing catalog

- First drafted 2026-03-28/29 (`202af495`, `b1648585`), title work culminating in the current *"An Observed-Label Chirality-Dipole Null in 890,069 Quality-Controlled High-Confidence DESI Spirals and an 8.5-Million-Galaxy Catalog"* (`pipelines/p2_chirality/chirality_catalog_paper.tex`). Grew from 798 lines at draft to an 8.47-million-row catalog (per SSOT 2026-04-17: "8.47M galaxies · 8/8 bias tests · 0.43σ null dipole · Shamir refuted 7×").
- Never split; absorbed the Shamir CW/CCW galaxy-spin-dipole test that P1U's now-retired barrier catalog cited as motivation (§3.2 above) — P4 carries the primary analysis, not P1.
- 2026-07-11: subject of a major compute closure (image-level end-to-end classifier injection, `6a09f8e1` "e2e flip pilot final — n=2500, T_raw=0.650±0.010, g_img=0.358 vs paper 0.398").

### P5 (chirality vs. environment) — downstream spinoff, never split

- Created 2026-05-15 as a bootstrap catalog cross-match (`059c3458`), depends entirely on P4's chirality labels.
- Current title: *"Environmental Dependence of Spiral Chirality: A DESIVAST Catalog-Native Void Non-Detection with Secondary Cosmic-Web Cross-Checks"* (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`).
- 2026-08-03 disposition: kept as **Standalone Companion · Chirality–Environment Null Test** to P4 (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`), not merged into P4 and not demoted like P3.

### "Paper 7" — self-improving review-loop meta-paper

- Idea-only since 2026-06-26 (`project-context/FUTURE_PAPERS.md`, "Created 2026-06-26"). Two working-title variants: an academic framing ("A Self-Improving Internal/External Review Loop for Scientific Papers: Closing the Gap to Zero") and a Hubify marketing case-study framing. No manuscript has ever been drafted. Status unchanged as of 2026-09-02 per `PAPER_LINEAGE_2026-08-05.md` §3.5.

### Salvage/ALP paper — absorbed, never independently published

- `research/paper1_salvage_alp/` (2026-03-17) proposed a standalone 3-part paper (ECH bounce + 13-barrier closure + spectator-ALP birefringence, ~17pp). This exact 3-part structure was never published as its own paper; instead its three parts fissioned across the P1 thread over the following five months: bounce/torsion physics → P1A; barrier closure → P1C (2026-08-05); ALP birefringence → shipped inside the P1B-MCMC companion (`PAPER_LINEAGE_2026-08-05.md` §3.1 table row: "Survived and shipped into P1B").

### Barriers/transparency PDF — standalone write-up, folded and refolded

- `research/focused_paper_source_integration/paper3_barriers_ech_transparency.tex`/`.pdf` (dated 2026-06-26), title *"Structural Barriers to Geometric Dark Energy and the Perturbation-Transparency of Einstein-Cartan-Holst Gravity."* This is an independent standalone write-up of the same barrier-catalog content that lived inside P1U's `sec:barriers`. Per `PAPER_LINEAGE_2026-08-05.md` §3.6, it was "superseded — content folded into P1U's sec:barriers, then retired with it at the P1 split," and is now cited as one of the two source documents (alongside `arxiv/paper1_unified.tex` itself) for the P1C extraction.

### Golden 2026 geometric-dark-energy PDF — untraceable file, content accounted for

- Public download `golden-2026-geometric-dark-energy-spin-torsion.pdf`, described in two snapshot docs (`research/final_paper_prep/website_data_snapshot.md`, dated as "v1.2.0, current" as of March 4) as version "v2.1.0" per a later audit brief. A full-tree search (`PAPER_LINEAGE_2026-08-05.md` §3.6) could not locate the file anywhere in the current repo tree, in `public/downloads/`, `backups/`, or `versions/`. Verdict recorded there: *"its scientific content (bounce cosmology + DE routes + galaxy spin) is already accounted for elsewhere... nothing independently at risk here — just a filesystem gap worth noting."* This genealogy report independently confirms the file is absent from the working tree as of 2026-09-02; it was not re-searched in packfile blobs beyond what `PAPER_LINEAGE_2026-08-05.md` already did.

---

## 3. Vision drift

**Earliest recorded statement of project goal** — two candidate "origin" documents exist, at different altitudes:

1. **Mission-level (per-paper) origin**, `bigbounce.md` (2025-07-22, commit `36cfb8d7`), abstract: *"We present a theoretical framework for dark energy arising from quantum gravitational effects in spin-torsion cosmology, potentially addressing the Hubble and σ8 tensions in modern cosmology... Our framework proposes that our universe originated from the interior of a rotating black hole in a parent universe... Recent JWST observations showing a 65-35% galaxy spin asymmetry in deep fields provide compelling preliminary evidence for cosmic parity violation, consistent with our rotating universe model predictions."*

2. **Program-strategy-level origin**, `project-context/bounce_portfolio_strategy.md` (2026-03-24): *"Old framing: 'Our ECH Model B predicts f_NL = -35/8. Single point of failure.' New framing: 'Bounce cosmology has a portfolio of testable predictions across multiple models, each optimized for different observational channels.'"* And `CLAUDE.md`'s current "Research stance": *"Bounce-model agnostic. Goal: prove bounce cosmology beats ΛCDM + inflation, not prove one specific bounce model."*

**Original claim vs. current claim, per surviving paper (facts only):**

| Paper | Original claim (earliest doc) | Current claim (2026-09-02) |
|---|---|---|
| **P1A** | (2025-07-22) One unified framework deriving dark energy from spin-torsion, resolving H₀ (→68.1) and σ₈ (→0.823) tensions, positing a rotating-black-hole universe origin, citing JWST 65/35% galaxy-spin asymmetry as "compelling preliminary evidence" | (v1A.0.127, 2026-07-24 onward) Narrow algebraic result: eliminate the non-propagating Cartan connection in minimal ECH gravity and state a Planck-suppressed axial contact operator and a classical transparency identity on one branch. `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`: "It is not a new dark-energy model, a complete no-go theorem for torsion cosmology, or an empirical discovery. The manuscript says this honestly." |
| **P1B** | (2025-07-22, same source doc) Same unified framework, no separate software identity existed | (v2B.0.16) A software verification library (`namaster-proof`) for exact pseudo-Cℓ window inference and tamper-evident computational receipts — "not a cosmological measurement or a second bounce physics result" (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`) |
| **P1B-MCMC companion** | Same origin claim (H₀/σ₈ tension resolution via spin-torsion) | Reclassified as a "generic GR+ALP accommodation/prior-volume study" and a "stock-CAMB generic extra-radiation proxy" — explicitly stated to be **not** ECH evidence, a bounce test, or support for P1A (`P1_SPLIT_CLOSURE.md`) |
| **P1C** | The 2026-03-17 salvage's "13 barriers, honest negative result" was originally one section supporting a larger DE-derivation paper | Standalone paper whose entire thesis is the negative result itself — a "structural no-go survey," reframed under directive Q1 to not reference the paper it was cut from at all (`PAPER_LINEAGE_2026-08-05.md` §4(a)) |
| **P2** | Not present in the 2025-07-22 document at all — f_NL was not yet the flagship metric | f_NL^local = −35/16 (exact four-vertex rederivation), positioned by `bounce_portfolio_strategy.md` (2026-03-24) as *the* flagship cross-model-agnostic prediction, testable by SPHEREx |
| **P3 (current, support role)** | Original 2026-03-28 draft claimed 268,519 outliers from 37.3M scanned sources across 8 surveys, framed as a discovery paper | Current P3 makes no discovery/detection claim at all — it is a provenance/public-ID recovery note for 181 TARGETIDs, explicitly stated to not "run or validate the anomaly detector, measure an anomaly rate, demonstrate novelty or purity, classify the discoveries" (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`) |
| **P4** | Not present in the 2025-07-22 document (galaxy-spin claims there were theoretical/aspirational, citing JWST as "preliminary evidence") | An empirical 890,069-object catalog paper reporting a **null** dipole result, explicitly refuting the Shamir CW/CCW asymmetry claim by a factor of ~6–12 |
| **P5** | Not present at origin | A downstream, catalog-native, exploratory null test of chirality vs. void environment, explicitly "not... a physical handedness measurement" (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`) |
| **Anomaly flagship (unwritten)** | Original P3 draft's 268,519-outlier claim | A characterization cohort of 3,810 TARGETIDs selected 2026-08-26, explicitly stated to be "not a discovery list" (`ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md`) |

The drift is monotone in one direction across every surviving thread: **from one
unified, high-magnitude, multi-tension-resolving theoretical claim in July 2025
to a portfolio of narrow, individually bounded, mostly negative-or-null results
by September 2026.** Every current paper explicitly disclaims the kind of
claim the origin document made in its abstract.

---

## 4. Counts over time ("how many papers")

| Date | Count | Identifiers | Source |
|---|---|---|---|
| 2025-07-22 | 1 | (unnamed, later "Paper 1") | `bigbounce.md` |
| 2026-03-17 | 1 (under audit) | Paper 1 | `research/paper1_salvage_alp/final_verdict.md` |
| 2026-03-19–24 | ~3 (P1, P2, P3/P5 material appearing) | Paper 1, Paper 2, early P3/P5 drafts | commits `7e9a9363`, `88794c9b` |
| 2026-04-03 | 4 | P1, P2, P3, P4 | commit history (`ee91bbab`, `b1648585`) |
| 2026-04-17 | 4 (first formal SSOT count) | Paper 1, Paper 2, Paper 3, Paper 4 | `SSOT/index.md` founding version |
| 2026-05-05 | 5 | P1A, P1B, P2, P3, P4 | commit `599144b2` |
| 2026-05-15 | 6 | P1A, P1B, P2, P3, P4, P5 | commit `059c3458` |
| 2026-05-22 | 6 (formalized) | P1A, P1B, P2, P3, P4, P5 | `HOUSTON_SIGN_OFF_BRIEF.md` |
| 2026-07-08 | 5 (temporary merge) | P1U, P2, P3, P4, P5 | commit `cc2b7f88` |
| 2026-07-14 | 6 (re-split) | P1A, P1B, P2, P3, P4, P5 | `P1_SPLIT_CLOSURE.md` |
| 2026-08-03 | 6 candidates / 3 "research programs" (framing change, not a count change) | P1A, P1B, P2, P3(support), P4, P5 grouped into Bounce theory / Survey discovery / Galaxy chirality | `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` |
| 2026-08-05 | 6 campaign papers + 1 draft (P1C) + 1 orphan-flagged companion (P1B-MCMC) | P1A, P1B, P2, P3(support), P4, P5, P1C(draft), P1B-MCMC(companion) | `PAPER_LINEAGE_2026-08-05.md` decision record |
| 2026-09-02 (today) | 6 campaign papers (readiness 95, sign-off pending) + P1C (live draft, v1C.0.16) + 1 unwritten anomaly flagship (characterization sample selected) + 1 idea-only "Paper 7" | Same as above, P1C now mid-R13 | `SSOT/index.md`, `SSOT/paper-1c/status.md`, `ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md`, `FUTURE_PAPERS.md` |

---

## Summary (plain English)

The program started in July 2025 as a single ambitious paper claiming a
spin-torsion black-hole-universe model could resolve both major cosmology
tensions and cited early galaxy-asymmetry data as supporting evidence. An
internal self-audit in March 2026 found roughly half of that paper's claims
weren't defensible and cut them, keeping only the bounce physics, a catalog
of failed dark-energy derivation routes, and one surviving testable
prediction (axion-like-particle birefringence). From that salvage, the
program grew outward into new papers on non-Gaussianity, an anomaly survey,
and a galaxy-chirality catalog, reaching four papers by April 2026. Paper 1
then split into a theory note and a computation companion (five papers), a
follow-on chirality-environment paper was added (six papers), briefly
re-merged into one 58-page paper in July, and split apart again within a
week after an external review found its claims too broad for what was
actually proven — that same split also narrowed the anomaly paper from a
268,000-object discovery claim to a small provenance note, after
sustained data-reconciliation problems. In August 2026, the team formally
declared that "six papers" had never been a scientific target, just the
residue of splits and rescues, and reorganized around three research
questions; the retired 14-barrier catalog was resurrected as its own
seventh manuscript (P1C), and the original 268,000-object anomaly claim is
being independently rebuilt from scratch under a sealed, auditable
compute contract rather than revived. As of today, every surviving paper
makes a narrower, more disclaimed claim than the one document this program
started from fourteen months ago.
