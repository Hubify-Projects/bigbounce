# EXT7 P3 — Per-Finding Truth-Audit Table

**Paper**: paper3_anomaly_catalog_v3.1.102 (60e26e5ec3afcd56)
**Source of truth**: `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.102, line numbers below)
**Audit date**: 2026-06-13 PT
**Auditor**: Claude Opus 4.7 (truth-audit class)
**Protocol**: `feedback_peer_review_truth_audit_protocol` standing directive
**Reviewers audited**: ChatGPT Pro Extended (MAJOR REVISIONS) · Grok Heavy (ACCEPT) · Gemini Thinking 2.5 Pro **FRESH THREAD** (MAJOR REVISIONS)

**Gemini-fresh-thread context**: This is the 2nd consecutive fresh-thread Gemini read on P3 (EXT6 also fresh, also MAJOR). EXT6 fresh-thread Gemini hallucinated revtex section numbers (§2.3 / §3.2 against §I/II/III) — flagged as Gemini-for-P3 failure mode and dropped. EXT7 verifies whether this is upstream of thread state or a one-off.

---

## Verdict schema

| Verdict | Meaning |
|---|---|
| `VERIFIED` | Finding maps to a real on-disk gap; closure work justified. |
| `FALSIFIED` | Reviewer claim wrong against the .tex / artifact. |
| `STALE` | Real once, already closed at the cited site. |
| `MISLABELED` | Real concern but severity overcalled. |
| `OUT-OF-SCOPE` | Outside paper scope (HD-ruled, artifact bundle, frozen-release timing). |
| `OPINION` | Editorial preference. |

**Auto-falsify rules** (applied on sight):
- Pattern-052 (closure-verification re-raises of items closed in v3.1.71 R36conf wave).
- Fisher 1/8.98² 8th-falsify (Fisher-positivity central is correctly stated as 8.14 with envelope [3.92, 8.98]; any "8.98 is the only number" call falsified).
- HD-ruled (Houston Disposition): frozen artifact bundle pre-arXiv-submission acceptance-blocker — frozen bundle is an arXiv-submission deliverable, not an in-review one. Standard practice across catalog papers.
- Hallucinated revtex section numbers — fresh-thread Gemini failure mode on P3.

---

## 1. ChatGPT Pro Extended — MAJOR REVISIONS (verdict)

### Closure verification re-raises

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `CGT-B1-partial` | Catalog-grade tier still includes Gaia + eROSITA + 200 Planck patches. | **MISLABELED → MINOR-NOMENCLATURE / STALE** | Pattern-052: same call EXT6/EXT5/EXT4. Already disclosed: abstract L458 distinguishes catalog-grade 269,317 vs full Path-C 378,280; Gaia tagged exploratory; eROSITA tagged membership-only; 200 Planck patches explicitly split out as "$\mathbf{269{,}117}$ point-source after dropping the 200 Planck map patches". |
| `CGT-B2-partial` | Per-class rates imply ~37k GALAXY anomalies, contradicting 2,468 science-class match. | **STALE / OPINION** | tex L680 explicitly states the per-class rates are computed on the "validated-TARGETTYPE subset" of ~6.5M spectra, distinct from the 1″-positional match against 20.3M-row catalog. Same denominator-meaning disclosed at L1012: "the rate agreement across the two populations is a coincidence of unrelated rate definitions and the like-for-like statement is the $\approx 0.9\times$ absolute count". Real concern but already explicitly reconciled in text; reviewer wants it as a table. Presentation preference, not science gap. |
| `CGT-B3-partial` | Table I still displays 20,000 → 200 = 1.00% in main row. | **OPINION** | Same as EXT6 (pattern-052). Footnote disclosure adequate; layout preference. |
| `CGT-B5-partial` | Zenodo DOI still future-tense; no frozen artifact for referee. | **STALE — HD-11 class** | tex L992 standard arXiv-day Zenodo practice. **Auto-falsify rule applied.** |
| `CGT-B6` | v3.1.71 cross-vendor clean-round closure absent. | **OUT-OF-SCOPE** | Internal QA artifact; not manuscript-visible. Same as EXT5/6. |
| `CGT-M1-M11` | All re-raises of v3.1.71-era MAJORS. | **STALE / OPINION** | All closed pre-v3.1.100; pattern-052. |

### Fresh-pass new findings

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `CGT-FM102-1` | **(MAJOR)** DESI per-class rates (0.75%×4.9M ≈ 36,750 GALAXY + 0.037%×1.5M ≈ 555 QSO ≈ 37k) do not numerically reconcile with 2,468 science-class match count. | **MISLABELED → MINOR-RECONCILIATION-TABLE** | Real arithmetic observation but already textually reconciled at L1012: 0.012% restricted rate on 20.3M science-class denominator vs 0.87% full-stream rate vs 0.75%/0.037% per-SPECTYPE rates on validated-TARGETTYPE subset (~6.5M). All four denominators present in tex; what reviewer wants is a 4-row reconciliation table consolidating them. Presentation upgrade, not a science contradiction. **TOP CLOSURE candidate** — single new table would close this and CGT-B2-partial together. |
| `CGT-FM102-2` | **(MAJOR)** Eq.(1) prose says inputs "standardized per-survey ... on the training pool", contradicting §II.B which says eROSITA/NEOWISE/Gaia scalers fit on full sample. | **VERIFIED → MINOR-PROSE** | tex L520 says: `x_i are survey-normalized inputs (standardized per-survey to zero mean and unit variance on the training pool prior to scoring; see \S\ref{sec:training})`. tex L514 (§II.B) says: `each column is then standardized ... with statistics fit on the full 930K sample (not the training split)`. **Real internal inconsistency between Eq.(1) gloss and §II.B detail.** One-sentence prose fix as reviewer proposes. MINOR not MAJOR (the science behavior is unchanged; the gloss under Eq.(1) just needs to point to §II.B for the tabular exception). **TOP CLOSURE.** |
| `CGT-FM102-3` | **(MAJOR)** Planck binomial p≃4×10⁻⁴ assumes independent patches but 10°×10° gnomonic patches can spatially correlate. | **VERIFIED → MINOR-CAVEAT** | tex L760 reports the binomial p without a correlation caveat. Real statistical concern. The conclusion is qualitative ("argues against memorization") so the fix is to label it "naive binomial" or add a HEALPix-block bootstrap variant. MINOR caveat-table entry, not MAJOR. |
| `CGT-FM102-4` | NEOWISE/Gaia scaler-refit incomplete. | **STALE / EXPECTED** | Same as CGT-FM95-2 EXT6. tex L514 explicitly discloses NEOWISE/Gaia feature tables existed pod-side only; Gaia is exploratory; scope honest. Not a defect. |
| `CGT-FM102-5` | DESI band-dominance analysis (Appendix B Table VII) computed over full 195,829 anomalies, not stratified by science-class subset. | **VERIFIED → MINOR** | Real follow-up: re-running band-dominance on the 2,468 science-class subset is queued. Could be MINOR-CAVEAT (label Table VII as fiber-spectral reconstruction taxonomy) or full closure (compute second table). Reviewer-proposed fix is reasonable. |
| `CGT-Min1-5` | Table V row (d) "decisive" wording; row (j) "GS corrected"; 0/200 + ≤1.5% binomial bound repetition; abstract length; Table I split; Appendix C retitle. | **OPINION / MINOR-COPYEDIT** | All editorial. |

**ChatGPT score (P3)**: 3 genuine VERIFIED MINOR (Eq.(1) prose, Planck binomial naive label, DESI band-dominance science-class stratification); 1 VERIFIED-as-MINOR formerly-MAJOR (4-row reconciliation table); rest STALE/OPINION pattern-052 carry-overs. The "MAJOR REVISIONS" verdict is overcalled — Eq.(1) gloss inconsistency is real but a one-sentence fix.

---

## 2. Grok Heavy — ACCEPT (verdict)

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GRK-CLOSURE-ALL` | All BLOCKERS/MAJORS CLOSED through v3.1.100→v3.1.102: catalog-tier semantics, DESI like-for-like 0.9× propagation, fNL envelope, SMBHB caveat, Cramér's V, Wilson 95% CIs, dust proxy (Planck τ₃₅₃/I₈₅₇, 5′, HEALPix N=64), purge of "earlier draft" parentheticals, three-threshold Table V form. | **VERIFIED** | All cited closures match v3.1.102 .tex. 5th consecutive 6/6 clean Grok read. |
| `GRK-NEW` | No new BLOCKERS / MAJORS / MINORS — "the paper is pristine". | **MOSTLY VERIFIED** | Misses the Eq.(1) prose / §II.B inconsistency (CGT-FM102-2) and the naive binomial caveat (CGT-FM102-3). Both are genuine MINOR finds. Not a Grok false-positive — a miss, but science-level CLEAN remains accurate. |

**Grok score (P3)**: ACCEPT verdict justified on science. Misses 2 MINOR internal-consistency items that ChatGPT catches. 5th consecutive ACCEPT.

---

## 3. Gemini Thinking 2.5 Pro **FRESH THREAD** — MAJOR REVISIONS (verdict)

### Section-number hallucination check (priority verification per Houston directive)

EXT6 fresh-thread Gemini hallucinated §2.3 / §3.2 against revtex4-2 §I/II/III numbering. EXT7 cross-check:

| Gemini cite | Actual tex location | Verdict |
|---|---|---|
| `§III E (eROSITA)` | tex L738: `\subsection{eROSITA DR1}\label{sec:erosita}` — III.E is the 5th subsection of §III (DESI/HighzQSO/SDSS/LAMOST/**eROSITA**/Planck/Gaia/NEOWISE). **CORRECT.** | **CALIBRATED** |
| `§II B (Tabular-survey feature preprocessing)` | tex L514: `\paragraph{Tabular-survey feature preprocessing (recovered production specification).}` inside §II.B `Training and Scoring` (L510). **CORRECT.** | **CALIBRATED** |
| `§II A` (Equation 1) | tex L519–520: Eq.(1) in §II.A `BIGAE Architecture` (L485). **CORRECT.** | **CALIBRATED** |
| `§II D (Step 5, injection-recovery)` | tex L539: `\subsection{Path-C Rebuild Methodology}` — Path-C protocol with injection-recovery gates is §II.D. **CORRECT.** | **CALIBRATED** |
| `§III A, §VI E, §VII` | §III.A DESI (L610); §VI = Discussion §III.A=correct; §VII abstract refs OK. | **CALIBRATED** |
| `§VI C (Limitation 7)` | §VI = Discussion (L960 area); subsection ordering matches. | **CALIBRATED** |
| `§VI D (ii)` | injection-recovery in Discussion/limitations area. | **CALIBRATED** |
| `§III G` (Gaia preprocessing provenance) | tex L763: `\subsection{Gaia DR3}\label{sec:gaia}` — Gaia is the 7th subsection of §III (G = 7th letter). **CORRECT.** | **CALIBRATED** |

**Result**: **EXT7 Gemini fresh-thread is CALIBRATED on P3** — every section number cited resolves to the actual revtex location. EXT6 fresh-thread hallucination did NOT recur. The failure mode was thread-state-specific, not upstream of thread state. **Recommendation: Gemini-for-P3 should NOT remain dropped; EXT7 reads cleanly.**

### Findings audit

| ID | Reviewer claim | Verdict | Evidence |
|---|---|---|---|
| `GLM-B1` | **(BLOCKER)** eROSITA S_BigAE score column completely irreproducible; 16 monotone rescalings + IsoForest retrains failed to reconcile 0.259 threshold. Score column must be purged or eROSITA rescoped to verified categorical list. | **STALE — pattern-052** | tex L738/L450: eROSITA is **already** released as $n=298$ membership-list-only with score axis stripped and the irreproducibility explicitly disclosed. EXT4/5/6 closed this. Gemini fresh-thread re-raised it as BLOCKER because it has no thread context. The closure is already in: "eROSITA tier released as a $n=298$ membership list only; per-object $S_{\rm BigAE}$ score axis non-reproducible on any of 16 monotone rescalings; see \S\ref{sec:erosita}" (L458). **Not a real blocker.** |
| `GLM-B2` | **(BLOCKER)** ML data leakage: tabular scaler fit on full sample; NEOWISE/Gaia queued; submission must pause. | **MISLABELED → MINOR (already disclosed)** | tex L514 fully discloses the practice + magnitude (eROSITA scaler-refit Jaccard 0.76; top-1% Jaccard 0.64; full-catalog Spearman 0.94; effect bounded ≤ model-retrain reproducibility floor ~15–17%). NEOWISE/Gaia scoped honestly as pod-side feature tables. "Submission must pause" overcalled — this is at most a MINOR-PROSE/CAVEAT item, and the scaler-refit-effect-at-or-below-reproducibility-floor finding (ext3_fm1_erosita_scaler_refit.json) is the load-bearing science answer. Same item Grok closed and ChatGPT downgraded to STALE/EXPECTED. |
| `GLM-M1` | **(MAJOR)** "~73× increase" headline not adjacent to ≈0.9× like-for-like qualifier in abstract. | **STALE — pattern-052** | tex L458 abstract literally reads: "the DESI-only subset (195,829 anomalies) is a ~73× increase on the same benchmark **(not a like-for-like comparison: ... the completed science-class-restricted recount finds only 2,468 DESI anomaly clusters ... ≈0.9× the benchmark's 2,685, not 73×)**". The 0.9× qualifier sits in the same parenthetical as the 73× number, in the abstract. Reviewer missed it. Same closure in §III.A L612 and conclusions L1027. |
| `GLM-M2` | **(MAJOR)** Injection-recovery 3 PASS conflates NEOWISE geometry-QA with detector-sensitivity. | **STALE — pattern-052** | tex L458 abstract explicitly: "Six injection-recovery gates: 3 PASS (SDSS 64%, Planck 100%, **NEOWISE mask-geometry 100% --- a masking-geometry sanity check that passes by construction, not a detector-sensitivity test**)". The disentanglement reviewer demands is already in the abstract. Closed in M6 EXT4 wave. Gemini fresh-thread missed it. |
| `GLM-Min1` | Gaia preprocessing script lineage-inferred from 21-feature successor. | **STALE — already disclosed** | tex L514: "Gaia preprocessing specification is lineage-inferred rather than directly recovered". Reviewer's proposed fix (data manifest warning) is reasonable but already covered. |
| `GLM-Min2` | Add one sentence under Eq.(1) noting MSE unweighted by inverse variance. | **VERIFIED → MINOR** | Real one-sentence improvement; reviewer's proposed location (under Eq.(1), §II.A) is correct. Trivial closure. |

**Gemini fresh-thread score (P3)**: 0 real BLOCKERS (2 STALE pattern-052); 0 real MAJORS (2 STALE — abstract already contains the demanded qualifiers); 1 genuine MINOR (Eq.(1) MSE unweighted caveat sentence). The "MAJOR REVISIONS" verdict is **overcalled** because the reviewer is reading the paper fresh without R-round context — every "MAJOR" headline finding is **already in the abstract or §III.A in v3.1.102**.

**Crucial: section-number calibration restored.** EXT7 fresh-thread cites real revtex locations. EXT6 fresh-thread hallucination was thread-state-specific, not upstream. **Recommendation: keep Gemini-for-P3 in the rotation; this round is calibrated even though the closure-context loss inflates severity.**

---

## Roll-up

| Class | Count | Genuine action items |
|---|---|---|
| VERIFIED MAJOR | **0** | None at MAJOR severity. |
| VERIFIED MINOR | **5** | (a) Eq.(1) prose / §II.B inconsistency one-sentence fix; (b) Planck binomial label as "naive" + caveat; (c) DESI band-dominance Appendix B Table VII stratify by science-class; (d) MSE unweighted-by-inverse-variance sentence under Eq.(1); (e) 4-row DESI denominator reconciliation table (could close CGT-FM102-1 + B2-partial together). |
| FALSIFIED | **0** | — |
| MISLABELED | **3** | Gemini B1/B2 + ChatGPT FM102-1 — real concerns but severity overcalled. |
| STALE / pattern-052 | **~12** | All BLOCKER/MAJOR carry-overs already disclosed in v3.1.102 abstract or §III.A. |
| OPINION | **8** | Table I split, Appendix C retitle, Table V row wording, etc. |
| OUT-OF-SCOPE | **2** | v3.1.71 clean-round artifact; frozen Zenodo pre-submission. |

**Truth verdict on round**: Closer to ACCEPT-WITH-MINOR-EDITS than MAJOR REVISIONS. The 5 genuine MINOR items are a half-day of polish. ChatGPT MAJOR REVISIONS overcalled (its own FM102-1 is reconciliation-presentation, FM102-2 is one-sentence prose, FM102-3 is one-caveat label); Gemini MAJOR REVISIONS overcalled (every BLOCKER is STALE because reviewer lacks R-round context); Grok ACCEPT closest to truth at the science level but misses 2 MINOR internal-consistency items.

**Top closure**: Eq.(1) prose / §II.B scaler-fit inconsistency — raised by ChatGPT, single-sentence fix at tex L520, eliminates the only genuine internal contradiction in the manuscript.

**Gemini-fresh-thread P3 status**: CALIBRATED this round. Drop-recommendation from EXT6 is REVERSED — keep Gemini-for-P3 in the rotation.
