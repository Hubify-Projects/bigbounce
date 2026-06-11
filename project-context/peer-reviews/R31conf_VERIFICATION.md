# R31conf — Post-EXT2-Closure Confirmation Sweep (6 papers)

**Date:** 2026-06-11 · **Auditor:** Claude (R31conf, read-only)
**Base:** `fbef87e7` (R30conf) → HEAD `8ec4febc` · **Protocol:** pattern-051 changed-regions-first; full hunk review of all six diffs; residual greps; math self-checks; mechanical battery (`tools/artifact_crosscheck.py` ×6); pattern-045 abstract-vs-body spot-checks.
**Question answered:** can EXT3 fire on the restamped six? **Answer: NOT YET — P3 (multi-item), P2 (1 line), P5 (1 label) are NOT-CLEAN; P1A, P1B, P4 are CLEAN.**

---

## P1A — `arxiv/paper1a_ech_nogo.tex` v1A.0.59 — **CLEAN**

| EXT2 item | Status | Evidence |
|---|---|---|
| F1 confabulated Ref [22] | **HOLDS** | `references.bib` `MercuriCapozziello2008` → `ShapiroTeixeira2014` (CQG 31, 185002, arXiv:1402.4854); both citing sentences (§II.C thermal-factor, §IV.B R2 motivation) rewritten to what Shapiro–Teixeira actually compute. Zero residual cites (changelog comment only). |
| F10 pair-exchange sign error | **HOLDS** | "Equivalently … = −ε^{μνρσ}R_{μνρσ}=0" chain DELETED at both sites (intro footnote ~L432; §X.B step 4 ~L1991). Bianchi-contraction route retained alone; metric-compatibility caveat kept. Remaining text re-derived: correct. |
| F4 WKB estimate | **HOLDS — arithmetic verified** | 10⁻³⁰ eV⁻¹ × f_a(1.22×10²⁸ eV) × H₀(1.44×10⁻³³ eV) ≈ 10⁻³⁵ eV ✓; k=6×10⁻⁴ eV / 10⁻³⁵ ≈ 10³¹⁻³² ✓; "~30 orders" ✓; conformal-time φ′ pinned. (L1447/L1458 `10⁻⁶³` hits are the *Immirzi-running* ratio — a different quantity, correct as-is.) |
| F5/F13 reheating | **HOLDS** | Top-Yukawa now leads (Γ/H≫1 at T_reh∼10¹⁵ GeV ✓); sphalerons correctly scoped to symmetric phase, Γ_sph/H≫1 only T≲10¹² GeV, exponential suppression only below EWPT; ν-osc recast model-dependent. Internally consistent. |
| F3/F6/F7 overclaim sweep | **HOLDS w/ 1 residual** | L513, L628 (paporg), L1190 (§IV intro), §XII.B "All four yield clean" → per-route scoping; "mechanism-independent" → "ECH-independent class tests" at all unqualified sites (only the two *qualified* concessions remain, L585/L2303); Fig. 8 caption decisive-claim split (SPHEREx vs f_NL=0 decisive; LiteBIRD 0.27 vs 0.342 at ~0.7σ). **Residual:** Fig. 7 (obs-timeline) caption still ends "…or leaves it as the unique survivor" — an F3-listed site only partially swept; mild tension with the adjacent 0.73σ-separation statement. Non-blocking; 1-clause fix at next touch. |
| F8 live w₀wₐ chain footnote | **HOLDS** | Table III ‡ replaced with static no-claim sentence. |
| F9 Ref [48] upon-request | **HOLDS** | Parity-assessment argument inlined in §XII.B (NY-pseudoscalar/axial-current, anomaly-chain as budget bound); `Golden2026supplement` no longer cited. |
| F2 bundle resync | **HOLDS** | `reproducibility/README.md` values table → frozen-chain Table IV values (67.68±1.06 / 0.8034±0.0084 / −0.020±0.169); β 0.30°→0.27°; "no pre-computed chains" → frozen-chains-committed clarification; labels v1A.0.59-bundle. |
| F21/F22/F15 minors | **HOLD** | γ_PTA header ✓; acknowledgements → responsibility statement ✓; "Falsifiability Criteria" ✓. |

Battery: artifact_crosscheck **PASS (0)**. 045: abstract claims (per-route scoping, 2.6–5σ cross-ref, N_tot≈92 erasure) all consistent with body.

## P1B — `arxiv/paper1b_mcmc_companion.tex` v1B.0.57 — **CLEAN**

| EXT2 item | Status | Evidence |
|---|---|---|
| F1 release claims | **HOLDS** | Root `CHANGELOG.md` exists; v1B.0.57 pinned to real stamp commit `63931207` (+ pin commit `d68edd89`); tex Data-Availability/App. A/Table IV repointed to version-stamp-commit + CHANGELOG mechanism — no unbacked git-tag claim remains; HF DOI pointer → CHANGELOG entry. |
| F2 diagnostics | **HOLDS — chain-verified** | `freeze_diagnostics_CORRECTED.json` `total_accepted_samples: 176240`; **direct count: 176,246 chain lines − 6 headers = 176,240 exact** ✓. `planck_bao_sn…/diagnostics/` now has `parameter_summary_CORRECTED.json` + units README; JSON (H₀ 67.784±1.092, ΔN_eff +0.0578±0.1787, σ₈ 0.812, S₈ 0.827, Ω_m 0.312) matches tex Table I to printed precision ✓. Stamp-wave rebooking +0.065±0.17→+0.058±0.179, 67.79→67.78 propagated at all 5 tex sites ✓. |
| F3 Vincenzi citation | **HOLDS** | `Vincenzi2025SNcompare` (MNRAS 541, 2585, arXiv:2501.06664) added + cited at the overlap caveat; DES2024SN5YR retained for likelihood. |
| F4/C1 control chains | **HOLDS (documented deferral)** | "unlikely to be reversed" → "plausibly robust … not demonstrated quantitatively"; two control chains disclosed as queued in-tex; deferred-to-compute section appended to the truth audit. Compute-queue row open by design. |
| F5 "not pre-computed" | **HOLDS** | Rewritten as included-vs-regenerable with both frozen dirs + chains/ enumerated. |
| F6 "natural" ×3 | **HOLDS** | All 3 flagged sites (abstract, §VI note, Discussion) → scan-prior-midpoint + tuned-misalignment-subspace framing. *Cosmetic:* unflagged "natural parameter range m/H₀∈[1,3]" survives at L1708 (scan-range descriptor, not the headline claim). |
| F8/F9/F10/F12/F13/F18/F19 | **HOLD** | Abstract Planck-only parenthetical dropped (body site kept) ✓; L1681 PR3-as-published relabel ✓; CMB-S4 "phenomenological ΔN_eff proxy" both sites ✓; Table IV "Internally verified" + pending-release caption ✓; C_aγ [9,51] = posterior-supported band (69%), kinematic box →160 ✓; GetDist 106,361 provenance parenthetical ✓; recomputed-from-chains sentence ✓ (true after F2 fix). |

Battery: crosscheck reports **FAIL 1 = false positive** — it resolves the in-sentence relative sub-path `diagnostics/parameter_summary_CORRECTED.json` (L2138) from repo root; both absolute targets exist (verified by ls). Consider absolute-path rewording at next restamp to keep the gate green.
Non-blocking notes: (i) Mahalakshmi-comparison 0.5σ now computes 0.554 with 67.78 (rounds to 0.6 at 1 d.p.) — one-token tweak; (ii) action-3c `table1_reproduction.json` CI artifact not created (enhancement, open).

## P2 — `research/focused_paper_source_integration/02_full_draft.tex` v1.7.51 — **NOT-CLEAN (1 blocking line)**

| EXT2 item | Status | Evidence |
|---|---|---|
| F1 App. A.2 contradiction | **HOLDS** | "or equivalently the full-ordering result in the c=1 convention" deleted; Li −35/16 demoted to *incomplete single-ordering intermediate* at abstract, App. A.2, dual-norm table caption+rows, and conclusion; halved-significance kept as robustness remark only, not propagated. |
| F2 3.0σ floor | **HOLDS — arithmetic verified** | Floor defined explicitly: 4.375×0.83/√(0.7²+1.0²)=2.98≈3.0 ✓ (recomputed 2.975); "widened b_φ" mislabel removed; all-combined endpoint 2.6–2.8σ stated (3.63/√(0.9²+1²)=2.70, /√(1²+1²)=2.57 ✓); headline rebooked **2.6–5σ at all sites — zero "3–5σ" residuals in any of the six papers**; Fig. 2 caption per-bar σ_eff added (F11). |
| F5 percentile vs floor | **HOLDS** | Comparison repinned to pre-systematic band; 4.4σ×(0.7/1.22)≈2.5σ propagation shown ✓. |
| F3 Hankel "diverges" | **HOLDS** | Both sites → finite ν=3/2, sensitivity via A_T∝1/ε³ + |η|^{−ν} channels; κ_ε∈[5.6,80] relabeled schematic. |
| F6/C1 τ_NL | **HOLDS** | Paragraph replaced: no trispectrum derived; r<1⇒inequality inference dropped; single-source clarification included. |
| F7 "would tighten" | **HOLDS** | → "whose conservatism a full joint Fisher would need to confirm" + sign-of-covariance caveat. |
| F4/F17/C2 Eq. (7) status | **HOLDS** | "Heuristic primordial-field scaling check, not a galaxy-covariance derivation" — identical label in abstract ¶3 and §IV. |
| F8/F16/F19/F20 minors | **HOLD** | "Addis et al." ✓; ρ defined on reduced 2×2 post-marginalization sub-covariance ✓; Fig. 5 caption 30%→σ≈0.9–1.0 ✓; DBI cross-ref in §IV ✓. |
| **BLOCKER (051 residual)** | **REGRESSION-class** | **L677:** "…do not qualitatively change the conclusion that SPHEREx can test f_NL=−35/8 at **>3σ** significance." directly precedes the sentence quoting the 2.6–5σ realistic window — the new honest all-combined endpoint (2.6–2.8σ) sits *below* 3σ. Incomplete sweep of the headline rebooking. One-line fix: ">3σ" → "at ≈2.6–5σ (>2.5σ even at the all-combined endpoint)" or equivalent. |

Battery: crosscheck **PASS (0)**.

## P3 — `pipelines/p3_anomaly_engine/paper3_draft.tex` v3.1.90 — **NOT-CLEAN (multi-item)**

The v3.1.90 wave closed only a subset of the EXT2 action plan. The queue.md claim "implemented every same-day-closable VERIFIED/PARTIAL finding" is **inaccurate for P3** — six VERIFIED text-only items are missing.

| EXT2 item | Status | Evidence |
|---|---|---|
| NM5 "203 novel" | **HOLDS** | "203 SIMBAD-unmatched eROSITA membership-list sources" at all 3 sites + not-confirmed-discovery pointer; site/SSOT synced (62616303). Zero tex residuals. |
| NM7 Table caveats caption | **HOLDS** | "All ten items are closed" → "…and current handling". |
| M9 foreground wording | **HOLDS** | "establishing that there is no evidence for first-order Galactic latitude or dust correlation within the surveyed footprints". |
| M4 App. C α=0.05 | **HOLDS** | Forecast sentence replaced with reference-only framing pinned to α_jk=0.19±0.65. |
| NM8 App. E mis-cite | **HOLDS** | "[18]" → project repo path `reproducibility/nanograv_mcmc/`. |
| 2.6–5σ cross-paper sync | **HOLDS** | 5 sites rebooked. |
| **NB1 schema sentence** | **MISSING (BLOCKER)** | Data Availability (now l.798) still promises unqualified "per-object canonical-$S$ scores" — no "where applicable / Planck raw-MSE / eROSITA membership-only" exception, no schema-flag table. Same-day text fix, not applied. |
| **NM3 20-vs-18 list** | **MISSING** | l.548 enumerates 18 layers under "20 curated all-sky catalogs"; "20 curated" also at l.236 (abstract), l.541, l.567, l.776. |
| **NM4 QSO z provenance** | **MISSING** | l.431 "pipeline-inferred" vs l.433 "photometric-pipeline estimates" unreconciled; pipeline still unnamed. |
| **Gm2 LAMOST denominator** | **MISSING** | 11,418,594 (l.362/480) vs 1.13×10⁷ re-score pool (l.375) — ~84k gap still undisclosed (no SDSS-style retrieval/quality-cut sentence). |
| **NM6 TARGETTYPE/SPECTYPE** | **MISSING** | l.427 still reads "validated TARGETTYPE classification ('GALAXY','QSO','STAR' from the Redrock pipeline)" vs l.388's BGS/LRG/ELG/QSO/MWS definition. |
| **NM1 like-for-like** | **MISSING** | "~73× like-for-like" retained at l.236 (abstract) + l.774 (conclusions); neither recomputed on science-target subset nor dropped. (TARGETTYPE split query is a documented open compute-queue row — but the text fallback was available.) |
| NM2 SDSS clustering | **OPEN (PARTIAL)** | l.438 clustering/cool-dwarf claims still computed on the superseded cross-transfer set (labeled as such in-sentence; per-use labeling/recompute not done). |
| Minor batch | **MISSING** | B3 Planck rate-cell footnote; 0/200 binomial UL; conclusions 17.8%-first ordering (l.776 still leads 58.8%); fiber cross-ref clause; dedup-sweep footnote pointer; Fig. 2 PNG title regen; ref [1] record. |
| eROSITA Table III column strip | **HOUSTON-DECISION** | Warned column retained — consistent with the parked ruling; 2-reviewer consensus favoring strip still pending Houston. |

Battery: crosscheck **PASS (0)**. 045: abstract retains two cross-surface inconsistencies (73× like-for-like; 20-vs-18) — exactly the "same-fact, all-sites" class the EXT2 audit told the internal loop to sweep.

## P4 — `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.174 — **CLEAN**

| EXT2 item | Status | Evidence |
|---|---|---|
| EF2 HC-dipole mislabel | **HOLDS** | Both sites → "HC real-space dipole (p_eq>0.6, N=949,584) at +0.41σ"; **zero** "full-catalog real-space dipole" residuals in P4 or any other paper. |
| EF3 A50 vs A95 | **HOLDS** | "disfavors ≥0.75%" → 50%-recovery sensitivity at A≳0.75% with falsification boundary A₉₅∈(1.0%,1.5%] (Table V); Shamir 6–12× exclusion retained under-pipeline. |
| EF1 hash provenance | **HOLDS** | Data Availability pinned to `81c67790` = the v1.0.174 stamp commit (two-step pin via ea75de79); in-text design note explains the pin-not-HEAD policy; crosscheck emits the expected WARN-OLD-COMMIT (by design). |
| P1 clarifications (EF9/EF12, EF17, EF18, EF19) | **OPEN (non-blocking)** | Reconciliation parenthetical at l.532 not added (existing cross-ref to §III.A partially covers); 80/20-augmented-pool note, 18.787-rounding note, float-precision caption note not added. All one-liners; recommend bundling into the next restamp. |
| P2 polish (EF4/EF6/EF15/EF16) | **OPEN (non-blocking)** | As parked. |

Battery: crosscheck **PASS (0)** (+1 by-design WARN). 045: abstract (8.47M / 3.2M pairing, estimator-specific falsification criterion, +0.41σ HC labeling) consistent with body.

## P5 — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.63 — **NOT-CLEAN (1 blocking label)**

| EXT2 item | Status | Evidence |
|---|---|---|
| EF1 dual-parent ledger | **HOLDS** | Abstract now separates DESIVAST primary (56,981 from n_lz=678,945 z≤0.24) from V-Web secondary (783,820 unique / 812,793 rows) with an explicit "drawn from the DESIVAST low-z parent, not from the full V-Web parent" sentence. |
| EF4 monopole language | **HOLDS** | "incorporates … by construction" → conditional-on-observed-CW-count framing, monopole uncertainty propagated separately via σ_from_half. Zero body residuals (changelog comment only). |
| EF9 "strong robustness" | **HOLDS** | → "supporting diagnostic consistency check" + 175 deg²/25,186-spiral overlap caveat + "not load-bearing robustness evidence". |
| EF12 "headline DESIVAST" | **HOLDS** | Phrase eliminated. |
| **EF5 Table II label** | **MISSING (P0)** | l.872 analysis-tree row still reads "T-Web concurrent-lit & **void-class overlap**" — contradicts §IX.C's explicit no-per-galaxy-cross-match / volume-fraction-only statement. One-word relabel ("volume-fraction comparison"); audit classified P0 must-fix. |
| EF3/EF11 dark-void co-report | **OPEN (consensus PARTIAL)** | Table IX has both cells (void dark −1.80; non-void dark +0.85) but the prose (l.1879) still cites only the void cell + non-void *bright*; Grok's one-line parenthetical not added. |
| EF14/EF19 dagger | **OPEN (minor)** | Caption text covers the Rs=10 exclusion substantively; formal "†" definition still absent. |
| EF18 f^V notation; EF2 ΔfCW columns; EF13/EF15/EF23 | **OPEN (non-blocking)** | As parked. |

Battery: crosscheck **PASS (0)**.

---

## Pattern-051 residual counts (all six .tex, body text; changelog comments excluded)

| Swept term | Count | Notes |
|---|---|---|
| "full-catalog real-space dipole" | **0** | |
| "incorporates the matched-sample monopole uncertainty" | **0** | |
| "natural parameter(s)" | **1** | P1B L1708 "natural parameter range" — unflagged scan-range usage, cosmetic |
| "203 novel" | **0** | |
| 3–5σ (`3--5$\sigma$` etc.) | **0** | swept in all six incl. P1A (10 sites) and P3 (5 sites) |
| "176,840" | **0** | artifacts clean (CORRECTED.json carries only a was-stale provenance note) |
| "MercuriCapozziello2008" | **0** | bib entry replaced |

## Math self-checks

- **P1A WKB:** 10⁻³⁰×10²⁸×10⁻³³ ≈ 10⁻³⁵ eV; 6×10⁻⁴/10⁻³⁵ ≈ 10³¹⁻³² (~30 orders) — **printed values correct**.
- **P2 floor:** 4.375×0.83/√(0.7²+1.0²) = 2.975 ≈ 2.98 ≈ 3.0 — **printed arithmetic correct**; 2.6–2.8 all-combined and 2.5σ percentile propagation also reproduce.
- **P1B count:** 176,246 raw chain lines − 6 header lines = **176,240 exact**; planck_bao_sn CORRECTED.json ↔ tex Table I match at printed precision.

## Mechanical battery

artifact_crosscheck: P1A PASS · P1B FAIL-1 (**false positive**, relative sub-path; targets exist) · P2 PASS · P3 PASS · P4 PASS (+by-design WARN) · P5 PASS.

## Verdicts & EXT3 gate

| Paper | Verdict | Blockers |
|---|---|---|
| P1A v1A.0.59 | **CLEAN** | none (1 residual clause: Fig. 7 "unique survivor") |
| P1B v1B.0.57 | **CLEAN** | none (crosscheck false positive to reword; 0.5σ→0.55 rounding token) |
| P2 v1.7.51 | **NOT-CLEAN** | L677 ">3σ" vs 2.6σ endpoint contradiction (1 line) |
| P3 v3.1.90 | **NOT-CLEAN** | NB1 schema sentence; NM3 20-vs-18; NM4 z-provenance; Gm2 LAMOST denominator; NM6 TARGETTYPE/SPECTYPE; NM1 like-for-like; + minor batch (all text-only) |
| P4 v1.0.174 | **CLEAN** | none (4 one-line P1 clarifications open) |
| P5 v0.1.63 | **NOT-CLEAN** | EF5 Table II "void-class overlap" relabel (one word); EF3/EF11 consensus parenthetical recommended same pass |

**EXT3 fires only after**: one P3 text wave (~6 fixes + minor batch), the P2 one-liner, the P5 relabel — then restamp the three and re-run this confirmation on the diffs. Open compute rows (P1B SN control chains, P3 TARGETTYPE query) remain correctly documented as deferred and do not block EXT3.
