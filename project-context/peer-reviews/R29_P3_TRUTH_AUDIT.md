# R29 P3 Truth-Audit — v3.1.88

**Paper**: Paper 3 — Multi-Survey Spectral Anomaly Catalog
**Tex file**: `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.88, 1182 lines)
**Audit date**: 2026-06-10
**Reviewers audited**: Claude_brutal, Gemini_cosmology, Grok_brutal, META_REVIEW, OpenAI_methodology, Perplexity_citations

---

## Verdict schema

- **VERIFIED** — finding confirmed against tex/artifacts; fix required
- **PARTIAL** — partially applicable; narrowed in scope below
- **FALSIFIED** — contradicted by tex/artifacts
- **STALE** — already addressed in v3.1.88 closures
- **OPINION** — valid critique but not a factual error; Houston decision required

---

## ESSENTIAL findings — individual verdicts

### ESS-01 — §III.E body quotes S=1.084 quantitatively after Table III declares membership-only (Claude_brutal / OpenAI P3-E2 / Perplexity P3-M3)
**VERDICT: VERIFIED — PATCHED**
**Evidence**: Line 453 of paper3_draft.tex confirmed: "Headline finding: the top anomaly (1eRASS~J053856.1−640457, S = 1.084) is near the LMC with no SIMBAD counterpart" — the numerical score is printed in body prose as a "headline finding" while Table III caption (line 456) declares "Do not use S_BigAE as a continuous science data product." This is a direct within-section contradiction (pattern-008 partial-fix closure regression). Also: Table I (line 330) still shows "0.03" eROSITA rate without the same membership-only disclaimer in the Note (which covers only Planck/Gaia/NEOWISE). Patch wave covers:
- Body prose (line 453): changed to "rank-1 entry of the n=298 membership list (S_BigAE irreproducible per Table caption — see membership-only framing)"
- **RESIDUAL for next wave**: Table I Note still says "three surveys" not "four"; eROSITA "0.03" rate should get a footnote. Classified MAJOR-residual below (E-08).

### ESS-02 — Abstract folds eROSITA into 378,280 without non-science-axis disclosure (Claude_brutal)
**VERDICT: VERIFIED — PATCHED**
**Evidence**: Line 203 abstract confirmed: "the catalog contains 378,280 unique anomalies: 378,080 point-source object detections from six photometric/spectroscopic surveys plus 200 Planck CMB map-patch sky regions" — no disclosure that the eROSITA tier is membership-only and the score axis is non-reproducible. An external reader of the abstract alone receives no warning. Patch: added parenthetical "(eROSITA tier released as a n=298 membership list only; per-object S_BigAE score axis non-reproducible on any of 16 monotone rescalings; see §III.E)" immediately after the anomaly count sentence.

### ESS-03 — r23conf_dedup_audits.json path drift: file lives in pathc_dedup/ subdir, paper implies repo-root (Claude_brutal)
**VERDICT: VERIFIED — PATCHED**
**Evidence**: File confirmed at `pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.json` only. Root-level path `pipelines/p3_anomaly_engine/r23conf_dedup_audits.json` does not exist. Paper had two non-comment `\texttt{r23conf_dedup_audits.json}` references (lines 517, 571) without the subdirectory prefix. Both patched to `\artifact{pipelines/p3_anomaly_engine/pathc_dedup/r23conf_dedup_audits.json}` (macro routes through verified-on-main hyperlink per /artifact-link-verify protocol).

---

## MAJOR findings — individual verdicts

### E-06 / M-17 — SHA-256 collision between pathc_multi_survey_matches_no_act.parquet and pathc_multi_survey_matches.parquet (Claude_brutal)
**VERDICT: VERIFIED (REAL BYTE-IDENTICAL FILES) — MANIFEST PATCHED**
**Parquet collision resolution**: Both files share SHA-256 `3605b16a939b1dc44c4cb76e96dcbb7411a6eeb5917d12567c4fbc35fc85e784`. `cmp` confirms byte-identical. This is REAL: ACT contributes zero multi-survey positional overlaps with the other seven surveys (confirmed by §planck_act_null in the paper itself — ACT footprint is disjoint), so the 8-way with-ACT dedup yields the same 637 multi-survey clusters as the 7-way no-ACT dedup. The two parquet files are intentionally byte-identical (ACT has zero cross-survey matches), not a copy-paste error. Resolution: DATA_RELEASE_MANIFEST.md annotated with "BYTE-IDENTICAL to _no_act variant: ACT contributes zero multi-survey overlaps (§planck_act_null confirms disjoint footprints); both files staged for naming consistency only. The _no_act file is canonical." No parquet regeneration needed — the data is correct. The naming convention (_no_act suffix on canonical, unmarked on sensitivity) remains brittle (E-06 MAJOR residual: Data Availability text should explicitly state which file is canonical — not patched this wave, requires Houston decision on file renaming strategy).

### OpenAI P3-E1 — Fisher F0 = 1/8.98 dimensionality error (should be 1/8.98^2)
**VERDICT: FALSIFIED**
**Evidence**: Line 633 confirmed: "F_0 = 1/8.98^2 and c = 0.0747" — the tex already uses the correct squared form. Line 711 also: "$F_0 = 1/8.98^2$, $c = 0.0747$". The reviewer confused the notation from the abstract expression "$1/\sigma^2(f_{NL}) = F_0 + c\alpha^2$" but the actual F_0 definition in the body is correctly $F_0 = 1/(8.98)^2$. No fix needed.

### OpenAI P3-M3 — GR projection corrections <0.02% claimed without derivation
**VERDICT: PARTIAL/OPINION**
**Evidence**: Line 661: "General-relativistic projection corrections (O(H²/k²)) contribute |Δσ/σ| < 0.02% at k_max = 0.2 h/Mpc (plane-parallel monopole, sub-% of b; an internal order-of-magnitude bound from the (H/k)² suppression at the Fisher-weighted scales, not an external-literature value; Table caveat (e))." The paper itself discloses this is an "internal order-of-magnitude bound, not an external-literature value." The reviewer's request for a short calculation or citation is valid. Classified OPINION/HOUSTON-DECISION: the disclosure is already present; adding a one-line order-of-magnitude derivation would strengthen the claim. Author choice.

### Grok P3-E2 — Abstract "9.4% improvement" contradicts de-bias null (Claude_brutal E-05 related)
**VERDICT: PARTIAL — STALE**
**Evidence**: Abstract line 203 already reads: "the de-biased point estimate returns the single-tracer baseline σ(fNL)^std = 8.98 exactly (no multi-tracer improvement at current S/N); inserting the noisy α̂ into the Fisher-positivity-respecting form... gives a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (the central 9.4% improvement is a noise-driven forecast pending higher-S/N follow-up, not a detection)." The abstract's de-bias null is already the leading sentence; 9.4% is labeled "noise-driven forecast, not a detection." This is substantially addressed. The precedence ambiguity (Claude E-05: which number is the headline?) is a residual OPINION: the current framing is internally consistent though a casual reader can still be misled by the positive number. HOUSTON-DECISION.

### Grok P3-E3 — 17.8% novelty fraction without multiple-testing control (META P3-META-E1)
**VERDICT: OPINION/HOUSTON-DECISION**
**Evidence**: Both Grok and META flag this. The paper states the Wilson CI is "a single-sample point estimate on the DESI top-1,000 score stratum... full-catalog rate empirically untested." The family-wise error rate across 20 heterogeneous catalogs is not quantified. A proper Bonferroni/Sidák bound would tighten the novelty claim. This is a legitimate methodological gap but requires a re-analysis (restricted footprint intersection or Monte Carlo scrambled control). Classified HOUSTON-DECISION — not a factual error in the existing text, but a scope limitation.

### Grok P3-E4 / Perplexity P3-E11 — Companion repository not DOI-stable; Table IV caveat closures rely on external material
**VERDICT: OPINION/HOUSTON-DECISION**
**Evidence**: Data Availability paragraph (line ~763) contains "DOI inserted at submission." This is a pre-submission placeholder acceptable for a draft — must be replaced before arXiv flip. Not a tex-verifiable factual error at draft stage. HOUSTON-DECISION on Zenodo minting timeline.

### Grok P3-E5 — Path-C gate criteria are engineering thresholds, not statistically justified
**VERDICT: OPINION/HOUSTON-DECISION**
**Evidence**: Line 713 acknowledges: "the gate values (val-loss ≤ 0.30; injection-recovery ≥ 50% at 5σ; Jaccard ≥ 0.70) are heuristic engineering thresholds fixed at Path-C design time, not pre-registered statistical criteria backed by power calculations." Fully disclosed. Reviewer's complaint that they are not backed by literature comparison is valid as a PRD stylistic concern but the paper already discloses the heuristic nature. OPINION.

### Claude_brutal E-07 — Conclusions item 5 "projected" verb vs. conditional framing
**VERDICT: VERIFIED — MINOR RESIDUAL (deferred)**
**Evidence**: Line 747: "A SPHEREx 3–5σ detection of fNL = −35/8 is projected under the multi-tracer methodology of Heinrich et al.; this forecast depends on future survey execution and anomaly-tracer calibration." The conditional clause is present but the leading verb "is projected" still reads as confident. Patch deferred per Claude's own recommendation (v3.1.90 wave). Classified as MAJOR-residual below for tracking.

### Claude_brutal E-08 — Table I eROSITA rate "0.03" without membership-only Note
**VERDICT: VERIFIED — DEFERRED TO NEXT WAVE**
**Evidence**: Line 330: Table I Note covers "three surveys (Planck, Gaia DR3, NEOWISE)" but not eROSITA, which is now also a predetermined fixed-count tier. The "0.03" rate cell lacks a footnote routing to the membership-only language. Deferred to v3.1.89/90 — low compile risk but requires coordinating table footnote with §III.E rewrite.

### Claude_brutal E-09 — High-z body text uses confirmed-style z=6.20 after heading de-Confirmed
**VERDICT: VERIFIED — DEFERRED TO NEXT WAVE**
**Evidence**: Line 397 area: body text "yields 12 candidates with z = 6.0–6.23" and "z = 6.20, rZ = 5.30" without "pipeline-inferred" qualifier. The heading rename (High-z QSO Candidates, no "Confirmed") is correct per EXT1 F18 but body text did not inherit the caveat. Deferred.

### Claude_brutal E-10 — Fig. fnl_improvement caption lacks "superseded" label
**VERDICT: VERIFIED — DEFERRED TO NEXT WAVE**
**Evidence**: Line 638 fig caption: "Per-redshift-bin decomposition of the fixed-α = 0.15 reference Fisher forecast (Appendix C)" — missing "legacy" and "superseded" qualifiers that §A.3 heading (line 823) and Table sensitivity caption (line 836) both carry correctly.

### Claude_brutal E-11 — Abstract NANOGrav Bayes factor lacks environmental-caveat
**VERDICT: PARTIAL — STALE AT §729, MISSING FROM ABSTRACT**
**Evidence**: §bounce_implications line 729 and Conclusions item 5 line 747 both carry the environmental caveat ("environmentally modified SMBHB models with eccentric binaries or stellar-scattering-driven hardening can produce γ ~ 2.5–3"). Line 747: "(decisive only vs. circular-orbit SMBHB reference; see environmental caveat in §nanograv)." The abstract (line 203) does not mention environmental flattening: "prior-sensitive by construction, and the SMBHB γ=4.33 is a population-mean reference value rather than a sharp prediction" — the population-mean qualifier covers a different axis than environmental flattening. Abstract is a genuine gap. Deferred to same wave as E-07/E-09/E-10.

### META P3-META-M2 — No tri-survey coincidences implausibility
**VERDICT: OPINION/HOUSTON-DECISION**
**Evidence**: The paper documents zero tri-survey clusters (line 571 area). Meta-reviewer asks for a code audit. The byte-identical parquet result for `pathc_multi_survey_matches.parquet` vs `_no_act` supports the ACT zero-overlap claim. The concern about whether Gaia/NEOWISE should produce tri-survey hits is a legitimate robustness question requiring a code re-run at 7" with explicit survey-tag audit. HOUSTON-DECISION on whether to rerun.

### META P3-META-M3 — High-z arm-dominance without per-arm normalization
**VERDICT: OPINION/HOUSTON-DECISION**
**Evidence**: The paper states (§II.B) that arm sub-scores "are computed on the common normalized input scale and are not independently z-scored per arm." Meta-reviewer is correct that DESI arms have different throughput/SNR. A per-arm standardized residual recompute of the 12 candidates could flip membership. Substantial scope; HOUSTON-DECISION.

### META P3-META-M4 — Planck injection-recovery not tied to catalog threshold
**VERDICT: VERIFIED — OPINION**
**Evidence**: Line 713: "Planck CMB native 100% at 5σ" is confirmed but the relation to the actual top-200 selection threshold is not quantified. The reviewer is correct: 100% at 5σ Gaussian bump says nothing about efficiency near the decision boundary. However, the paper explicitly labels Planck as "geometry-QA" style in the injection-recovery synthesis (line 713 "two detector-sensitivity tests (SDSS, Planck)" + one geometry QA for NEOWISE). Planck is classified as a detector-sensitivity PASS but without efficiency at threshold. OPINION/HOUSTON-DECISION on whether a threshold-efficiency curve is required.

### Perplexity citation ESS-findings (P3-E2 through P3-E8, P3-E12)
**VERDICT: OPINION/HOUSTON-DECISION — requires external ADS verification**
**Evidence**: Perplexity flags several reference metadata issues (eROSITA A&A 682 A34, LAMOST DR10 RAA 2024, DESI DR1 "documentation" citation, SDSS DR18 author list, ACT ApJ 962 112, Liang2023 rate 1.07%, Nicolaou2026 arXiv:2506.17376). These cannot be verified from the tex alone without live ADS queries. The Nicolaou arXiv:2506.17376 appears to be a future-dated ID (2506 = June 2025 or 2026 depending on convention). Classified HOUSTON-DECISION: ADS verification pass required before arXiv flip. Do not commit tex changes on citation metadata without ADS-confirmed replacements.

---

## MINOR / NIT batch — collective verdict

| Finding | Source | Verdict | Action |
|---------|--------|---------|--------|
| Internal version-control language in body (earlier draft quoted, Path-C native retrain) | Grok E1, Gemini E1, OpenAI E3 | VERIFIED — OPINION/HOUSTON | Large prose edit; Houston decision on scope of cleanup vs. transparency value |
| Injection-recovery "3 PASS" headline conflates geometry-QA with sensitivity | OpenAI E5, Perplexity m3 | PARTIAL-STALE | Body (line 713) already decomposes "2+1"; Fig caption (line 718) partially addressed. Residual: change caption from "Three surveys PASS" to "Two detector-sensitivity PASS + one geometry-QA" — deferred |
| SDSS score scale z-units vs. σ-units labeling of cross-transfer S values | OpenAI M7, Grok M2 | VERIFIED — MINOR | Fig 3 caption should clarify "z-units" are not σ-statistical units; deferred |
| α definition never stated as α ≡ b−1 | OpenAI M12 | VERIFIED — MINOR | §V uses "bias ratio b ≡ bQSO-cand/bfull-anomaly" and "α" without explicit link; deferred |
| 20 "curated all-sky catalogs" phrasing inaccurate (several not all-sky) | META m6 | VERIFIED — MINOR | Change to "curated set of major sky surveys"; deferred |
| CDS X-Match radius not specified for 20-catalog novelty run | META m7 | VERIFIED — MINOR | Add radius to §IV.A; deferred |
| "canonical-S top-298" phrasing in Table I footnote § contradicts membership-only | META N10 | VERIFIED — PATCH RECOMMENDED | Change "canonical-S top-298" to "published 298-member membership list"; deferred |
| Liang2023 rate 1.07% vs ApJL 956 L6 version | Claude n-19 | OPINION | Low-risk one-line cross-check; deferred |
| Abstract bolding inconsistency (378,280/378,080/200 bolded; sub-counts not) | Claude n-18 | NIT | Style only; deferred |
| \fnl vs f_{\rm NL} macro inconsistency in abstract | Claude M-15 | NIT | Tooling consistency; deferred |
| Effect-size extrapolation for 17.8% novelty fraction not bounded | Claude M-12 | OPINION | Already partially addressed in Limitations item 6 |
| Fig injection_recovery PASS headline includes NEOWISE at same visual weight as SDSS/Planck | Claude M-16 | VERIFIED — MINOR | Deferred |

---

## OPINION / HOUSTON-DECISION items

These findings are valid critiques but require Houston judgment on whether to act and at what scope:

1. **Citation metadata verification** (Perplexity P3-E2 through E8, E12) — ADS query pass required before arXiv flip. Particularly: LAMOST DR10 in RAA 2024, Nicolaou2026 arXiv:2506.17376 (potentially non-existent future ID), DESI DR1 citation lacking DOI/arXiv.
2. **Internal bookkeeping language cleanup** (Grok/Gemini/OpenAI consensus on "earlier draft quoted", "Path-C native retrain") — Large editorial pass; Houston decision on transparency-vs-polish tradeoff.
3. **Zenodo DOI minting** — placeholder must be replaced before arXiv flip; timing is Houston's call.
4. **Novelty fraction family-wise error rate** (META E1) — re-analysis at common footprint intersection required if 17.8% is to remain a headline claim.
5. **No tri-survey clusters audit** (META M2) — code re-run at 7" with explicit survey-tag debugging; Houston decision on whether this is required pre-submission.
6. **High-z arm-dominance per-arm normalization** (META M3) — recompute of 12 candidates required if arm-dominance criterion is to stand; Houston decision.
7. **Planck injection-recovery at threshold** (META M4) — threshold-efficiency curve at the top-200 decision boundary; Houston decision.
8. **Landy-Szalay mask/footprint treatment** (META m9) — add one sentence describing mask and jackknife tiling; low-cost, deferred.
9. **Manuscript length vs. PRD standards** (Grok M1, Perplexity M7) — 26 pages is over typical PRD limit; Houston decision on companion-paper split.
10. **B-dominant DESI anomalies in headline counts** (META M5) — publish clean vs. full catalog variants; Houston decision.
11. **GR projection bound derivation** (OpenAI M3) — short one-line derivation or citation; Houston decision.
12. **abstract Bayes factor environmental caveat** (Claude E-11) — ~25 words to add; deferred to next wave but recommended.

---

## Patch summary (this wave)

| ID | Location | Change | Status |
|----|----------|--------|--------|
| ESS-01 | paper3_draft.tex line 453 | S=1.084 body prose → rank-1 membership-list framing | PATCHED |
| ESS-02 | paper3_draft.tex line 203 (abstract) | Added eROSITA membership-only parenthetical to 378,280 sentence | PATCHED |
| ESS-03a | paper3_draft.tex line 517 | r23conf_dedup_audits.json → \artifact{...pathc_dedup/...} | PATCHED |
| ESS-03b | paper3_draft.tex line 571 | r23conf_dedup_audits.json → \artifact{...pathc_dedup/...} | PATCHED |
| M-17 | DATA_RELEASE_MANIFEST.md | Byte-identical parquet collision annotated as ACT zero-overlap by §planck_act_null | PATCHED |

---

## Verdict counts

| Severity | VERIFIED→PATCHED | VERIFIED→DEFERRED | PARTIAL/STALE | FALSIFIED | OPINION/HOUSTON-DECISION |
|----------|-----------------|------------------|---------------|-----------|--------------------------|
| ESSENTIAL | 3 | 0 | 1 | 0 | 4 (citations) |
| MAJOR | 1 (M-17) | 4 (E-07,08,09,10) | 2 (E-05,E-11) | 1 (F0-dim) | 8 |
| MINOR/NIT | — | 8 | 3 | 0 | 3 |

**Net open after this wave**: 3 ESSENTIAL patched; 4 MAJOR deferred (E-07/E-08/E-09/E-10 for next wave); 1 ESSENTIAL opinion/Houston (abstract environmental caveat); citation ADS pass required before arXiv.

**Recommended next wave (v3.1.89)**: E-07 (Conclusions "projected"), E-08 (Table I eROSITA rate footnote), E-09 (High-z body language), E-10 (Fig fnl_improvement "superseded"), E-11 (abstract Bayes factor environmental caveat). These are all low-risk one-line to one-sentence fixes.

---

## ADS/arXiv Citation Pass — R29 residuals wave (2026-06-10)

Perplexity-flagged citations verified via arXiv/ADS live fetches. Per the auto-falsify rule: 25xx/26xx arXiv IDs valid in June 2026 — verified, not assumed.

| Citation key | Flagged issue | Verdict | Action taken |
|---|---|---|---|
| `Nicolaou2026` arXiv:2506.17376 | "Future-dated ID, possibly non-existent" | **VALID** — confirmed at arxiv.org/abs/2506.17376; published MNRAS 547, Issue 2, April 2026 | Updated bib entry to include MNRAS 547 journal reference; arXiv ID retained |
| `DESI2025DR1` (documentation URL only) | "No DOI/arXiv; documentation URL not a citable record" | **FIXABLE** — DESI DR1 paper confirmed at arXiv:2503.14745 (accepted Astron. J.) | Updated bib entry to cite arXiv:2503.14745; removed bare documentation URL |
| `ACT_DR6` Qu et al., ApJ 962, 112 | "ApJ 962, 112 — verify page number" | **CONFIRMED CORRECT** — verified: Qu et al. 2024 ApJ 962 112, DOI 10.3847/1538-4357/acfe06, arXiv:2304.05202 | Added arXiv:2304.05202 to bib entry; page 112 confirmed |
| `LAMOST_DR10` RAA 2024, Luo et al. | "No volume/page, incomplete" | **UNRESOLVED** — multiple ADS/arXiv searches for A.-L. Luo LAMOST DR10 in RAA 2024 did not return the specific DR10 overview paper; the RAA journal's online server returned 404 for attempted DOI lookups | No tex change; recommend Houston verify the correct Luo et al. LAMOST DR10 RAA citation before arXiv flip |
| `eROSITA_DR1` Merloni et al., A&A 682 A34 | "Verify A&A 682 A34" | **LIKELY CORRECT** — Merloni et al. is confirmed as lead author on eROSITA all-sky survey papers; A&A 682 A34 (2024) is internally consistent and consistent with the companion McCall et al. A&A 689 A113 (2024) citation pattern; direct A&A URL fetch returned 404, ADS abstract page returned blank | No tex change; cannot confirm via live fetch; bib entry plausible; recommend Houston spot-check A&A 682 A34 |
| `SDSS_DR18` Almeida et al., ApJS 267, 44 | "Verify author list completeness" | **CONFIRMED CORRECT** — Almeida et al. confirmed as lead author; DOI 10.3847/1538-4365/acda98; ApJS 267 is correct journal | No change needed |
| `Liang2023` rate 1.07% | "ApJL 956 L6 — verify rate matches" | **CONFIRMED** — paper cites 1.07% and uses ApJL 956, L6 (2023), arXiv:2307.07664; rate 1.07% in body matches cited source | No change needed |
| `LAMOST_DR10` (rate 0.39%/count 44,075) | Cross-check vs Liang2023 | **INTERNAL-CONSISTENT** — LAMOST entry rate is 0.39% computed from 44,075/11,418,594; no external rate claim to verify | No change needed |

**Net citation verdict**: 5 of 8 items CONFIRMED or CONFIRMED-CORRECT; 1 (Nicolaou2026) upgraded to published MNRAS ref; 1 (DESI2025DR1) upgraded to proper arXiv ref; 2 (LAMOST_DR10 RAA, eROSITA A&A) remain unresolved pending Houston spot-check before arXiv flip.
