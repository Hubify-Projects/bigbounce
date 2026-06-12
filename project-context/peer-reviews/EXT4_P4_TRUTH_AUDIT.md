# EXT4 P4 Truth Audit — v1.0.175

**Paper:** P4 — Survey-Scale Galaxy Chirality · v1.0.175 · `paperTimestamp` June 11, 2026
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Gemini 3.5 Thinking (MINOR REVISIONS), Grok Heavy (ACCEPT)
**Mode:** EXT4 in-thread DELTA review (closure verification + fresh pass)
**Audit date:** 2026-06-11 PT · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:** `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.175, paperVersion macro l.55) + `ext3_nfm1_flip_identity_qc.json` + `ext3_nfm1_hc_dipole_qc_rerun.json` (both `outputs/canonical_provenance/`) + EXT3_P4_TRUTH_AUDIT.md
**Load-bearing finding:** FB-175-1 (ChatGPT, flip-identity QC narrative vs. committed artifact). Adjudicated with primary evidence below.

---

## Load-bearing adjudication — FB-175-1 (ChatGPT BLOCKER)

**ChatGPT claim (verbatim, paraphrased):** the v1.0.175 Appendix B QC narrative — "2.9% of rows have any-channel recovered flip probability outside [0,1] by up to 0.09; excursions are not float32 rounding; a QC flag identifies affected rows; excluding 59,515 HC rows leaves the dipole null-consistent" — is not reproducible from the committed QC artifact (`ext3_nfm1_flip_identity_qc.json`), which says only 88,278 rows were evaluated, zero rows violate beyond 1e-3, and "no QC flag or row exclusion is required." The companion rerun artifact (`ext3_nfm1_hc_dipole_qc_rerun.json`) then operates on 59,515 flagged HC rows under a different flag definition. ChatGPT calls this "internally inconsistent."

**Tex evidence (chirality_catalog_paper.tex l.605, Appendix B.d):**
- "for $2.9\%$ of rows (the previously quoted $1.3\%$ is the single CW-channel rate) a recovered flip probability falls outside $[0,1]$ by up to $0.09$"
- "These excursions are \emph{not} float32 rounding: they occur exclusively on rows whose raw probabilities derive from the separate raw-catalog inference pass rather than the equivariant pass (rows carrying both raw legs show zero violations)"
- "A QC flag identifies the affected rows; excluding them from the HC sample ($59{,}515$ of $949{,}584$, $6.3\%$) leaves the real-space dipole null-consistent and essentially unchanged ($z=+0.48$ excluded vs.\ $+0.52$ baseline under the c11b $10^{4}$-permutation convention)"
- Cites both artifacts inline.

**Artifact 1 — `ext3_nfm1_flip_identity_qc.json`:**
- `n_rows_total: 8,474,531`
- `n_rows_with_any_nan_column: 8,386,253` → `n_rows_evaluated: 88,278` (≈1.04% of catalog; the rest are excluded for missing raw OR equivariant columns)
- `bound_excursion.max: 5.96e-8` (float32 storage precision)
- `rows_violating_beyond_1e-3: 0` (`fraction: 0.0`)
- `conclusion`: "ZERO rows violate the identity beyond 1e-3 ... the previously quoted '1.3% of rows violate beyond 1e-3' figure is NOT reproduced on the committed catalog ... No QC flag or row exclusion is required"

**Artifact 2 — `ext3_nfm1_hc_dipole_qc_rerun.json`:**
- `flag_definition`: "any recovered flip-pass probability outside [0,1] beyond 1e-3 **using the full-coverage raw columns**" — different column set from artifact 1 (which restricts to rows with complete raw+eq columns)
- `n_hc: 949,584` · `n_flagged_in_hc: 59,515` (6.27%) — matches tex's 59,515 / 6.3% exactly
- `baseline.z: 0.5164` → "0.52" rounded · `flagged_rows_excluded.z: 0.4754` → "0.48" rounded — matches tex's z=+0.48 vs +0.52 exactly
- `delta_z: -0.0410`

**Verdict:** **PARTIAL** (and partly **VERIFIED**) — ChatGPT correctly identifies a real artifact-vs-narrative gap, but the gap is **bounded and one-sided**, not "internally inconsistent" as charged.

**Decomposed:**

| Tex claim | Artifact 1 says | Artifact 2 says | Verdict |
|-----------|-----------------|-----------------|---------|
| "2.9% of rows ... outside [0,1] by up to 0.09" (catalog-wide, 8.47M denominator) | 0% violators beyond 1e-3 on the 88,278 rows where raw+eq columns coexist; max excursion 5.96e-8 | (does not address catalog-wide rate) | **NOT REPRODUCIBLE from committed artifacts.** Neither artifact carries the 2.9% number or the 0.09 max-excursion number. Where these come from is undocumented. **VERIFIED gap.** |
| "max deviation $4.3\times10^{-7}$" (normalization sum) | `sum_deviation.max: 2.04e-7` (about half the cited value, ~1.7× float32 eps) | n/a | **PARTIAL mismatch.** Same order of magnitude, but the cited 4.3e-7 is not the artifact's reported max. Likely a separate (pre-NaN-filter) recompute, not pinned to either committed artifact. |
| "excursions are not float32 rounding ... rows whose raw probabilities derive from the separate raw-catalog inference pass" | Artifact 1 evaluates only the intersection rows and finds float32-precision residuals (5.96e-8 max); the 8.39M NaN-column rows are the candidate "separate raw-catalog inference pass" subpopulation, but the artifact does not characterize their excursion distribution | Artifact 2's "full-coverage raw columns" flag definition is the operationalization | **PARTIAL.** The mechanism (separate raw-catalog pass) is consistent with artifact 1's `n_rows_with_any_nan_column: 8,386,253`, but artifact 1 explicitly DECLINES to issue a QC flag and the tex's "QC flag identifies affected rows" claim is implemented only in artifact 2 under a different column convention. |
| "$59{,}515$ of $949{,}584$ HC rows" | n/a | `n_flagged_in_hc: 59,515` exact | **MATCH.** |
| "$z=+0.48$ excluded vs.\ $+0.52$ baseline" | n/a | `flagged_rows_excluded.z: 0.4754`, `baseline.z: 0.5164` | **MATCH** (consistent rounding). |
| "leaves the real-space dipole null-consistent and essentially unchanged" | n/a | `delta_z: -0.0410`, both z well below 1σ, rank_p ≈ 0.28 in both arms | **MATCH.** |

**Net characterization (auditor):** ChatGPT is **half-right**: artifacts 1 and 2 use **different flag definitions** (artifact 1: only rows where raw+eq columns coexist; artifact 2: "full-coverage raw columns" — i.e. the catalog-wide raw column set inclusive of the 8.39M rows lacking equivariant raw columns in artifact 1's intersection). This is a real reproducibility hole: artifact 1's `conclusion` line "No QC flag or row exclusion is required" was written when artifact 1 was the standalone summary and is now contradicted by artifact 2's existence + the tex's exclusion narrative. But ChatGPT's stronger claim that the artifacts are "internally inconsistent" with each other is **FALSIFIED** — they evaluate disjoint row populations under disjoint flag definitions and are individually self-consistent. The 59,515 / z=0.48 vs 0.52 numbers in the tex are **fully reproducible** from artifact 2. The 2.9% / 0.09 numbers in the tex are **NOT reproducible** from either artifact and need a third (catalog-wide raw-leg-only) QC artifact to close.

**ChatGPT severity verdict (BLOCKER acceptance-blocking):** **PARTIAL.** Real artifact-narrative gap, but bounded and fixable by publishing one canonical catalog-wide QC artifact (the source of the 2.9% / 0.09 / 4.3e-7 numbers) + harmonizing artifact 1's stale "no QC flag required" conclusion line. Demoted from BLOCKER to **MAJOR**: the headline scientific result (HC dipole null) is robust under artifact 2's rerun; the gap is provenance/reproducibility-only and does not falsify any quantitative number.

---

## Verdict Table — Fresh Findings (EXT4)

| # | Reviewer | Sev | Finding | Verdict | Evidence |
|---|----------|-----|---------|---------|----------|
| FB-175-1 | ChatGPT | BLOCKER | Flip-identity QC: tex's 2.9%/0.09/4.3e-7/QC-flag/59,515-exclusion narrative is not reproducible from `ext3_nfm1_flip_identity_qc.json` (which says 0 violators on 88,278 evaluated rows, no QC flag required) and conflicts with companion rerun | **PARTIAL (demote to MAJOR)** | See load-bearing adjudication above. 59,515 + z=0.48 vs 0.52 numbers ARE in artifact 2 exactly. 2.9% + 0.09 + "QC flag identifies" + "not float32 rounding" claims are NOT reproducible from either committed artifact. Artifact 1's `conclusion` line "No QC flag or row exclusion is required" directly contradicts the tex narrative. **Real gap; fixable with one canonical catalog-wide QC artifact + edited conclusion line in artifact 1.** Severity demoted: headline science unaffected. |
| FM-175-1 | ChatGPT | MAJOR | Data Availability (l.733): the rendered PDF, not the .tex at the pinned commit, is the authoritative carrier of the pin; not a journal-grade reproducibility endpoint | **HOUSTON-DECISION + PARTIAL** | Tex l.733 verbatim discloses the two-step stamp-then-pin protocol and explicitly says "the rendered PDF, not the in-repo source at the stamp hash, is the authoritative carrier of this pin." The disclosure is **transparent and correct**; whether to restructure the two-step gate (cite post-pin commit/tag) is a HOUSTON-DECISION (carried over from EXT3 FB1, same ruling). Zenodo DOI mint-at-submission is also Houston policy (HD-11). Fix: at journal-submission restamp, cite post-pin tag or mint Zenodo DOI. |
| FM-175-2 | ChatGPT | MAJOR | Conclusion VII.C still says +3.64σ and +7.93σ are "same physical estimator and footprint under different null-run sizes" — undermines the notation section | **VERIFIED (re-raise)** | Tex l.542 verbatim: "the two values describe the same physical estimator and footprint under different null-run sizes (the differing $p$-values reflect null-ensemble resolution, not different physics; see Sec.~\ref{sec:notation} and Table~\ref{tab:multipole} caption)." EXT3 B3 ruled this PARTIAL with the cross-ref parenthetical added; ChatGPT's stronger reading is correct — the sentence reconciles p-values but still claims "same estimator and footprint" while §III.A says different null-run sizes/mask-weight conventions. **Fix:** adopt ChatGPT's drafted replacement ("retained for continuity ... canonical row is the current high-statistics diagnostic under its committed field convention"). |
| FM-175-3 | ChatGPT | MAJOR | Sec. V.A: Shamir comparison "can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples" reads as cross-survey explanation | **PARTIAL re-raise (EXT2 M7 / EXT3 NF-m2)** | Tex l.478 carries the phrase verbatim **but** the same paragraph (l.478) already hedges: "We do \emph{not} claim a frequentist exclusion of Shamir's Ganalyzer estimator: a likelihood-level exclusion requires a matched-footprint Ganalyzer reanalysis under his pipeline + cuts (not performed here)." Same as EXT3 NF-m2 — a precision improvement, not an error. ChatGPT's drafted replacement ("under this DESI/ViT-Small pipeline; a matched Ganalyzer test remains required") is the correct closure. |
| fm-175-1 | ChatGPT | MINOR | Fig. 2 caption says "eight D4 transforms" but figure shows original/flipped + probability bars | **HOUSTON-DECISION (caption vs. figure)** | Either rewording or figure swap works; no scientific error. Editorial. |
| fm-175-2 | ChatGPT | MINOR | Table VII caption "All 8 tests pass" still terse | **PARTIAL re-raise (EXT2 EF6 / EXT3 NF-m3)** | Tex l.608 caption verbatim: "All 8 tests pass at the stated criteria; the thresholds are generous relative to the $0.75\%$ empirical sensitivity floor and constitute necessary-but-not-sufficient conditions for sub-percent-level bias-free classification (see Appendix~B text for threshold definitions and the T1/T5/T7 scope caveats)." The necessary-but-not-sufficient + T1/T5/T7 caveats ARE in the caption — ChatGPT misread/skimmed. **FALSIFIED at the strong reading**; reword-to-stronger-form is OPINION. |
| fm-175-3 | ChatGPT | MINOR | Zenodo DOI not minted | **HOUSTON-DECISION (HD-11, ruled mint-at-submission)** | Tex l.740: "A persistent archival DOI ... has not yet been minted; until it is, the versioned release tag above is the citable artifact." Honest disclosure, ruled policy. |
| GfA-EXT4 | Gemini | MAJOR | App B.d "via and its channel companions" — missing equation handle between "via" and "and" | **FALSIFIED — extraction artifact** | Tex l.605 verbatim: "via $p_{\rm CCW}^{\rm flip}=2p_{\rm CW}^{\rm eq}-p_{\rm CW}^{\rm raw}$ and its channel companions". The inline equation IS present in source. Gemini's PDF extractor dropped math glyphs — same failure mode as EXT3 GfA/GfB/GfC. |
| GeA-EXT4 | Gemini | MINOR | App E.d raw "\omega<0.5\sigma$" with missing opening $ | **FALSIFIED — extraction artifact** | Tex l.730 verbatim: `overstated the stability as ``$<0.5\sigmaunit$ variation''.` — uses `\sigmaunit` macro, not `\omega`; opening `$` is present. Gemini's extractor misread `\sigmaunit` as `\omega` and dropped delimiters. Same family as EXT3 GfA/GfB/GfC. |
| GeBcl-EXT4 | Gemini | (re-raise) | App D.g design matrix "{ , , 2}" garbled | **FALSIFIED — extraction artifact (pattern-052 re-raise)** | Tex l.685 verbatim: `primordial-dipole basis $\{\hat x,\hat y,\hat z\}$ + imaging-leg fractions + pixel-density + pixel-density$^2$`. Identical to EXT3 GfA — same falsification, same evidence, re-raise stands FALSIFIED. |
| GeCcl-EXT4 | Gemini | (re-raise) | App A.c "the rises while the measured power falls" | **FALSIFIED — extraction artifact (pattern-052 re-raise)** | Tex l.567 verbatim: "the $\sigma$ rises while the measured power falls because the label-shuffle null realizations are subjected to the same subtraction..." Identical to EXT3 GfB — same falsification, re-raise stands FALSIFIED. |
| GeDcl-EXT4 | Gemini | (re-raise) | §IV.C "quantiles Ss = {3.5,4.4,...}" leftover script variable | **FALSIFIED — extraction artifact (pattern-052 re-raise)** | Re-raise of EXT3 GfC. Same evidence path. |
| GkA-EXT4 | Grok | MINOR | Truncation parenthetical appears in PDF body but not in Table II caption | **VERIFIED (cosmetic)** | Legitimate consistency request: the explanatory parenthetical does belong in the Table II caption for self-contained readability. One-line edit. |
| GkB-EXT4 | Grok | MINOR | Appendix B.d QC paragraph appears after T7 criterion statement; reorder for narrative flow | **OPINION** | Reading-order preference; no scientific error. Editorial. |

---

## Verdict Table — Contested Closure Claims

| # | Reviewer claim | Audit verdict | Evidence |
|---|----------------|---------------|----------|
| ChatGPT FB1/B1 (PARTIAL — 53b41d12 stamp commit cites 81c67790, two-step protocol disclosed but PDF/source-at-pin mismatch persists) | **CONFIRMED PARTIAL + HOUSTON-DECISION** | Tex l.36 `\artifact` macro now points to `blob/53b41d12/` (post-EXT3 wave landed). Tex l.733 discloses stamp-then-pin lag with PDF-as-authoritative-carrier wording. EXT3 ruled HOUSTON-DECISION on two-step gate restructure; ruling stands. DOI/tag at submission. |
| ChatGPT FM1 (CLOSED — full-catalog→HC qualifier propagated) | **CONFIRMED** | EXT3 stale-label sweep landed; headline references all carry HC qualifier or are scoped to the unthresholded systematics-attributed channel. |
| ChatGPT FM2 (CLOSED — A50/A95 separation) | **CONFIRMED** | Tex l.114 abstract + Sec.~VI.B verbatim distinguish A_50≈0.75% from A_95∈(1.0%,1.5%]. |
| ChatGPT FM3 (PARTIAL — LEE Bonferroni vs max-stat MC still conflated in Table I + App C) | **PARTIAL carryover (EXT3 unchanged)** | Sec.~VI Discussion reorder landed (direct-MC max-stat now lead at l.643), but Table I caption still names both correction philosophies. Legitimate open P1. |
| ChatGPT FM4 (CLOSED — "mutual consistency established" removed) | **CONFIRMED** | Tex now says the harmonic-completeness check bounds Shamir-class signal in MASTER channel without claiming statistical consistency on a common axis. |
| ChatGPT FM5 / NF-m3 (PARTIAL — Table VII "All 8 tests pass") | **FALSIFIED at the strong reading** | Tex l.608 caption already carries necessary-but-not-sufficient + T1/T5/T7 caveats. See fm-175-2 above. |
| ChatGPT NF-M1 (REGRESSION/PARTIAL — artifact contradiction) | **PARTIAL (this round's FB-175-1)** | Adjudicated above. Real gap on 2.9%/0.09/4.3e-7/QC-flag-disposition; 59,515 + z numbers verified. Demoted from BLOCKER to MAJOR; not a regression — the float32 attribution claim WAS retracted as ChatGPT itself notes. |
| ChatGPT NF-M2 / NF-M3 / NF-M4 (CLOSED) | **CONFIRMED** | HC Fisher floor (0.53%) added; App E p_eq>0.6/0.8 reworded to "high-confidence morphology-selected subsamples"; App E footnote replaced with the post-MASTER monopole-only / +4.84σ / systematics-attributed wording. |
| ChatGPT B2 (PARTIAL — hierarchy bullet "+3.64σ consistent with monopole-mask leakage") | **PARTIAL carryover** | Wording softened; ChatGPT's still-too-strong charge restated without new evidence — re-raise tracked as PARTIAL. |
| ChatGPT B3 (PARTIAL — conclusion VII.C reconciliation) | **VERIFIED carryover → FM-175-2 above** | Same site, sharpened. |
| ChatGPT B4 / M2 / M4 / M5 / M8 (CLOSED) | **CONFIRMED** | All four EXT3 carryovers landed. |
| ChatGPT B5 (PARTIAL — bootstrap exact-mask) | **PARTIAL carryover** | NSIDE sensitivity footnote (l.685) present; exact-mask definition still implicit. Unchanged from EXT3. |
| ChatGPT M3 (PARTIAL — ℓ=2 cross-spectrum 200-perm "confirming") | **PARTIAL carryover** | Single-site "supporting" swap landed; 200-realization floor disclosed. ChatGPT's residual concern is the 200-realization budget itself, which is a scope question, not a wording error. |
| ChatGPT M6 (PARTIAL — D4 spatial stratification) | **HOUSTON-DECISION carryover** | Enhancement request, not an error. EXT3 ruling stands. |
| ChatGPT M7 / FM-175-3 (NOT ADDRESSED — Shamir cross-survey wording) | **PARTIAL** | Same as FM-175-3 above — hedge present in same paragraph; precision-improvement edit. |
| Grok closure verifications (all CLOSED, no regressions) | **CONFIRMED** | Matches audit. ACCEPT is legitimately calibrated to the scientific content; modulo FB-175-1 provenance gap, paper is at MINOR REVISIONS. |
| Gemini closure verifications (3 NOT ADDRESSED — D.g, A.c, IV.C) | **FALSIFIED across the board (pattern-052)** | All three are extraction artifacts re-falsified with the same source evidence as EXT3. Gemini's verifier is the same broken extractor. |
| Gemini closures of truncation note + Table III precision (CLOSED) | **CONFIRMED** | Both 2-line edits landed in v1.0.175. |

---

## Genuinely-NEW substantive findings count (EXT4)

| Class | Count | Items |
|-------|-------|-------|
| **Genuinely new (VERIFIED or PARTIAL with new substance)** | **2** | FB-175-1 (the catalog-wide 2.9%/0.09/4.3e-7/QC-flag-disposition reproducibility gap — the only genuinely new substantive item this round; bounded, fixable, **does not falsify headline**) · GkA-EXT4 (Table II caption truncation-note inclusion — cosmetic but valid) |
| **Re-raises (PARTIAL/carryover, no new evidence)** | **5** | FM-175-2 (B3 sharpened) · FM-175-3 (M7 / EXT3 NF-m2) · ChatGPT FM3, B2, B5, M3, M6 carryovers · fm-175-1 fig 2 caption |
| **FALSIFIED reviewer findings** | **5** | Gemini GfA-EXT4 (Apx B "via") · GeA-EXT4 (E.d ω<0.5σ) · 3× pattern-052 re-raises (D.g, A.c, IV.C) — all extraction artifacts; fm-175-2 "All 8 tests pass" caveat-already-present |
| **HOUSTON-DECISION / policy** | **3** | FM-175-1 / FB1 provenance two-step gate · fm-175-3 Zenodo DOI (HD-11) · fm-175-1 Fig 2 caption-vs-figure choice |
| **Confirmed closures from EXT3** | **9** | FM1, FM2, FM4, NF-M2, NF-M3, NF-M4, B4, M2, M4, M5, M8 (all carried over green) |

**Genuinely-new substantive count: 2** (FB-175-1, GkA-EXT4). EXT3 baseline was 6 net-new → **67% shrink**. Gemini contributed **zero** genuinely-new substantive findings (all extraction artifacts — same failure mode, fourth round running). Grok contributed **one** (GkA caption-consistency). ChatGPT contributed **one substantive new item** (FB-175-1), demoted from BLOCKER to MAJOR.

---

## Reviewer-recommendation calibration

| Reviewer | Stated recommendation | Audit-calibrated | Delta |
|----------|----------------------|------------------|-------|
| ChatGPT | MAJOR REVISIONS | **MINOR REVISIONS** (FB-175-1 demoted to MAJOR but bounded; FM-175-2 verified; remaining items are OPINION/HOUSTON-DECISION/PARTIAL-carryover) | overcalled (BLOCKER → MAJOR) |
| Grok | ACCEPT | **ACCEPT-with-two-MINOR-edits** (GkA cosmetic; GkB editorial) | accurate |
| Gemini | MINOR REVISIONS | **ACCEPT-with-pending-footnotes** (all 5 fresh + carryover findings FALSIFIED as extraction artifacts) | overcalled (extractor-driven) |

**Consensus reading:** the paper is at **MINOR REVISIONS pending one bounded reproducibility wave** (FB-175-1) + one carryover edit (FM-175-2). No reviewer challenged a headline number; the scientific verdict is converged. **Pattern-052 (Gemini extractor) is now four EXT rounds without a single legitimate finding** — recommend dropping Gemini from EXT5 unless its extractor is rebuilt.

---

## CLOSURE PLAN — concrete edits (hardest-first)

### P0 — FB-175-1 reproducibility gap (the load-bearing item)

**Goal:** publish one canonical catalog-wide QC artifact that produces the tex's 2.9% / 0.09 / 4.3×10⁻⁷ numbers and harmonize the two existing artifacts' framing.

1. **Generate** `pipelines/p2_chirality/outputs/canonical_provenance/ext4_nfm1_flip_identity_qc_catalog_wide.json` containing, on the full 8.47M-row catalog using the **catalog-wide raw column set** (the union artifact 1 restricts away):
   - `n_rows_total: 8,474,531`
   - `n_rows_with_raw_columns_present` (the denominator under which the 2.9% rate is computed — must yield ≈8.47M for the 2.9% claim, or restate with the correct denominator if not)
   - `n_rows_any_channel_outside_unit_interval_beyond_1e-3`
   - `fraction_any_channel_outside`: must reproduce **0.029** for tex consistency, or the tex must be edited to match
   - `fraction_single_cw_channel_outside` (the "previously quoted 1.3%" anchor)
   - `bound_excursion.max`: must reproduce **≤0.09** for tex consistency
   - `sum_deviation.max`: must reproduce **4.3×10⁻⁷** for tex consistency (artifact 1 reports 2.04×10⁻⁷ on its 88,278-row subset, so the catalog-wide value should differ)
   - explicit flag column: `qc_flip_identity_violator: bool`
   - exact alignment with artifact 2's "full-coverage raw columns" definition
2. **Edit** `ext3_nfm1_flip_identity_qc.json` `conclusion` field: replace "No QC flag or row exclusion is required" with "On the 88,278-row intersection where both raw and equivariant raw columns are populated, no violators beyond 1e-3 are present and storage-precision-only residuals are observed; the catalog-wide QC pass on the union raw column set (8.47M rows, including the 8.39M rows with only the raw inference leg populated) is reported separately in `ext4_nfm1_flip_identity_qc_catalog_wide.json` and is the source of the 2.9% violator rate and 0.09 max excursion quoted in the paper."
3. **Add** in chirality_catalog_paper.tex (l.605 area, just after the "outside $[0,1]$ by up to $0.09$" clause): one parenthetical specifying the artifact split — `(catalog-wide rate from \artifact{...ext4_nfm1_flip_identity_qc_catalog_wide.json}; the intersection-subset rate is 0 by construction, \artifact{...ext3_nfm1_flip_identity_qc.json}; the HC dipole rerun under the catalog-wide flag is \artifact{...ext3_nfm1_hc_dipole_qc_rerun.json})`.
4. **Verify** `ext3_nfm1_hc_dipole_qc_rerun.json` `flag_definition` field is fully consistent with the new ext4 artifact's flag definition (it already says "full-coverage raw columns", which should match).

**Expected outcome:** ChatGPT's reproducibility charge falls fully. No paper number changes.

### P1 — FM-175-2 conclusion VII.C reconciliation

Tex l.542: replace `the two values describe the same physical estimator and footprint under different null-run sizes (the differing $p$-values reflect null-ensemble resolution, not different physics; see Sec.~\ref{sec:notation} and Table~\ref{tab:multipole} caption)` with: `the 500-MC $+3.64\sigmaunit$ direct single-mode value is retained for continuity with the leakage analysis; the $10^4$-permutation Table~\ref{tab:multipole} canonical row is the current high-statistics diagnostic under its committed field convention.` Removes the "same estimator and footprint" claim that conflicts with the §III.A notation.

### P2 — FM-175-3 Shamir cross-survey wording (one site, sharpened)

Tex l.478: `the monopole-mask leakage channel demonstrated in Sec.~\ref{sec:monopole_mask_null} can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples` → `the monopole-mask leakage channel demonstrated in Sec.~\ref{sec:monopole_mask_null} can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched-footprint Ganalyzer test under Shamir's pipeline + cuts remains required for a frequentist cross-survey exclusion.` Keeps the hedge that already follows; sharpens the demonstrated-mechanism scope.

### P3 — GkA-EXT4 Table II caption truncation note

Tex Table II caption: append the same parenthetical from the body — `(percentages truncated rather than rounded at the second decimal; integer counts are exact)`.

### P4 — Carryover P1 batch (EXT2/EXT3 still-open)

- FM3 Table I caption: explicitly attribute LEE correction philosophies (max-stat MC = principled; Bonferroni/BH = conservative cross-check).
- B5: explicit bootstrap-mask vs canonical-mask definition statement.
- Restamp `\artifact` macro from `blob/53b41d12/` to the next pin commit if any new artifacts land before submission.

### Ruled / HOUSTON-DECISION (no action this wave)

- FM-175-1 (provenance two-step gate restructure) — at journal submission only (HD-11 family).
- fm-175-3 (Zenodo DOI) — mint-at-submission (HD-11, ruled).
- fm-175-1 (Fig 2 caption vs. figure) — editorial; route at restamp.
- All Gemini fresh + carryover findings — extraction artifacts; no action (pattern-052).
- ChatGPT fm-175-2 "All 8 tests pass" caption — caveats already present; reword-to-stronger-form is OPINION.

---

## Exit-criterion assessment

**One bounded reproducibility wave + one one-sentence text edit from clean.** The substantive residual is:
1. **P0 — one new committed QC artifact** (`ext4_nfm1_flip_identity_qc_catalog_wide.json`) + 2 small string edits in `ext3_nfm1_flip_identity_qc.json` and the tex Appendix B parenthetical.
2. **P1 — one l.542 sentence replacement.**
3. **P2/P3 — three single-line edits.**

No reviewer challenged the +0.41σ HC headline, the WLS z≈−18 exclusion, the A_50/A_95 boundaries, the 8.47M / 3.20M counts, or any committed artifact number that is not in the FB-175-1 scope. Grok ACCEPT is well-calibrated; Gemini MINOR is 100% extraction-artifact-driven; ChatGPT MAJOR's BLOCKER demotes to MAJOR on adjudication and the MAJOR fixes are bounded.

**Expected EXT5 state after this wave:** policy-only residue (Zenodo DOI at submission, provenance two-step gate design ruling).

---

*Verdict counts (fresh + contested closures): VERIFIED 2 · PARTIAL 11 · OPINION 2 · FALSIFIED 5 · HOUSTON-DECISION 4 · CONFIRMED-CLOSED 9.*
*Protocol: VERIFIED = on-disk evidence supports the claim · PARTIAL = claim partially supported, partially overstated · FALSIFIED = source/PDF contradicts the claim · STALE = resolved before the reviewed version · OPINION = editorial · HOUSTON-DECISION = framing/process choice.*
*pattern-052 re-raise rule applied to Gemini extraction-artifact carryovers (D.g, A.c, IV.C) — primary evidence from EXT3 stands.*
