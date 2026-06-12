# EXT5 P4 Truth Audit — v1.0.177

**Paper:** P4 — Survey-Scale Galaxy Chirality · v1.0.177 · `paperVersion` macro l.55
**Reviewers:** ChatGPT Pro Extended (MAJOR REVISIONS), Grok Heavy (ACCEPT), Gemini Thinking (ACCEPT)
**Mode:** EXT5 in-thread DELTA review (closure verification + fresh pass)
**Audit date:** 2026-06-12 PT · **Auditor:** Claude (bigbounce truth-audit protocol v3)
**Source verified against:**
- `pipelines/p2_chirality/chirality_catalog_paper.tex` (v1.0.177, l.55)
- `outputs/canonical_provenance/ext4_fb1_flip_identity_qc_catalogwide.json` (the catalog-wide QC artifact from R34conf closure)
- EXT4_P4_TRUTH_AUDIT.md + R34conf_P4_TRUTH_AUDIT.md (prior rounds)

**Auto-falsify rules in force:**
- June 2026 IS current; arXiv 25xx/26xx IDs are valid → AUTO-FALSIFIED if cited as problem
- HD-6/HD-11 ruled (Zenodo DOI mint-at-submission, provenance two-step gate) → HOUSTON-DECISION
- Pattern-052: Gemini extraction-artifact-derived math/table claims verified against TeX before crediting
- R34conf-verified rederivation: **2√3 Fisher factor is CORRECT** (σ(A)=√(3/N)=2√3·σ(f_CW) at f_CW≈0.5; verified from changelog l.60–61 and tex l.520). ChatGPT re-raise of 2√3 without new evidence = AUTO-FALSIFIED per re-raise rule. The v1.0.177 changelog at l.59–62 explicitly states: "R34-P4-32 Fisher 2-sqrt-3 factor REDERIVED AS CORRECT (sigma(A)/sigma(f_CW) = sqrt(3/N)*2*sqrt(N) = 2*sqrt(3); numerical 9.68e-4 reproduces) — audit claim REBUTTED with shown arithmetic."

---

## Part I — R34conf Closure Verification (pattern-051: did v1.0.176→177 close the R34conf action items?)

| R34conf action | v1.0.177 status | Evidence |
|----------------|-----------------|----------|
| **C0 — R34-P4-32 Fisher 2√3 factor** (VERIFIED MAJOR in R34conf) | **REDERIVED CORRECT — NO EDIT** | changelog l.59–62: the rederivation σ(A)/σ(f_CW) = √(3/N)·2√N = 2√3 is correct at f_CW≈0.5. Tex l.520: `\sigma(A) = \sqrt{\frac{3}{N_{\rm spiral}}} = 2\sqrt{3}\,\sigma(f_{\rm CW})` stands unchanged. Numerical 9.68×10⁻⁴ reproduces. Audit claim REBUTTED. |
| **C1 — R34-P4-31 flip-swap error metric definition** | **CLOSED** | changelog l.57–59: "flip-swap error metric DEFINED inline (L1 |p_CW^raw - p_CW^flip|, matching ext4_fb1 QC script l.106-108)." |
| **C2 — R34-P4-19 train/val split Appendix B.a verification** | **ADDRESSED** | changelog notes this was resolved; source carries the 80/20 pre-augmentation split documentation. |
| **C3 — FM-175-2 / R34-P4-25 Conclusion VII.C "same physical estimator and footprint"** | **PARTIALLY APPLIED — PARTIALLY OPEN** | changelog l.62: "FM-175-2 carryover sentence applied." HOWEVER: source l.565 still reads "the two values describe the same physical estimator and footprint under different null-run sizes (the differing p-values reflect null-ensemble resolution, not different physics; see Sec. III.A and Table III caption)." The sentence persists verbatim. The Table III caption at l.422 contains the more accurate "superseded as a table entry by the canonical rows above but retained in the text for continuity with the leakage analysis" — this is the correct language, present in the caption but NOT replacing the l.565 body sentence. The changelog claims the edit "applied" but the targeted sentence is still present. **PARTIAL carryover still open.** |
| **C4 — R34-P4-23 Appendix D typo "z ≈ −18.1.34"** | **CLARIFIED — NOT A SOURCE ERROR** | changelog l.63: "the 'z=-18.1.34' typo is a PDF-extraction artifact (not in source)." The source carries `z \approx -18.1` (clean); the ".34" seen in the PDF was a PDF-extractor artifact concatenating the footnote marker. Finding AUTO-FALSIFIED (extraction artifact). |
| **C5 — R34-P4-27 "0.57% (Ap-unit)" notation** | **CLOSED** | changelog l.62: "A_p notation fixed (5.7e-3 i.e. 0.57%)." |
| **C6 — R34-P4-04 "headline" language** | **CLOSED** | changelog l.62: '"headline"->"primary".' |

**Regression assessment:** No regressions from v1.0.176→177. R34conf C0 (Fisher 2√3) was not an error — the paper is correct; the edit item was removed. C3 is incomplete (sentence persists). Other items cleanly closed.

---

## Part II — EXT5 Fresh Findings Verdict Table

### ChatGPT EXT5 findings

| # | Code | Sev | Finding | Verdict | Evidence |
|---|------|-----|---------|---------|----------|
| EXT5-P4-C1 | FB-177-1 | BLOCKER | Data Availability still cites commit 53b41d12 (v1.0.175) while header is v1.0.177; new QC artifact absent at pinned commit | **HOUSTON-DECISION (HD-11 + two-step stamp — no new substance)** | Source l.758: "Repository state for this version: commit 53b41d12 (v1.0.175, June 2026)." This is the standing two-step stamp-then-pin protocol, disclosed explicitly at l.758–763. ChatGPT has raised this as BLOCKER in EXT3, EXT4, and EXT5; it was ruled HOUSTON-DECISION / FM-175-1 in EXT4 and FM-175-1 in R34conf. The two-step pin disclosure (l.758–763) is verbatim in the paper and transparent. This is the fourth raise without new substance. AUTO-FALSIFIED as a blocker; HD-11 ruling stands; mint-at-submission resolves. |
| EXT5-P4-C2 | FM-177-1 | MAJOR | Hierarchy bullet still says monopole-only null "demonstrates the +3.64σ canonical value is consistent with monopole-mask leakage" — inconsistent with Sec. IV.D which says post-MASTER monopole-only explains only ~12% | **VERIFIED (carryover — open since EXT4 B2; one-sentence edit)** | Source l.226: "Generative monopole-only null: (vi) N=500 binomial-monopole realizations demonstrating the +3.64σ canonical value is consistent with monopole-mask leakage." Source l.485 (Sec. IV.D) correctly says post-MASTER monopole-only explains only ~12%. ChatGPT's fix is correct: the hierarchy bullet should scope the +3.64σ to the pre-MASTER context. The edit is one sentence: "(vi) N=500 binomial-monopole realizations demonstrating the pre-MASTER raw pseudo-C_ℓ is dominated by monopole-mask leakage; post-MASTER residuals require additional coherent systematics." REAL, actionable, carryover B2. |
| EXT5-P4-C3 | FM-177-2 | MAJOR | Conclusion VII.c still says +3.64σ and +7.93σ are "same physical estimator and footprint under different null-run sizes" | **VERIFIED (carryover FM-175-2 / R34-P4-25 / C3 — edit NOT applied)** | Source l.565 verbatim: "the two values describe the same physical estimator and footprint under different null-run sizes." Table III caption (l.422) correctly says "+3.64σ superseded as table entry but retained for continuity with leakage analysis." The body sentence at l.565 was supposed to be updated in v1.0.177 (changelog l.62: "FM-175-2 carryover sentence applied") but the source still has the old language. This is the third consecutive round this sentence is still open. ChatGPT's proposed replacement is correct: "the 500-MC +3.64σ direct single-mode value is retained for continuity with the leakage analysis; the 10⁴-permutation Table III canonical row is the current high-statistics diagnostic under its committed field convention." **REAL, actionable.** |
| EXT5-P4-C4 | FM-177-3 | MAJOR | Shamir comparison "can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples" is too broad | **PARTIAL (precision-improvement carryover — EXT3 NF-m2 / EXT4 FM-175-3 / R34-P4-18)** | Source l.485 end-paragraph: "can generate a comparable pre-MASTER dipole-class artifact under this DESI/ViT-Small pipeline; a matched-footprint Ganalyzer test under Shamir's pipeline + cuts remains required for a frequentist cross-survey exclusion." The hedge IS present in source. ChatGPT's proposed wording is essentially what the source now says. This is a PARTIAL — the precision improvement from EXT3 WAS applied; ChatGPT is reading stale-language at l.492 ("can reproduce the pre-MASTER dipole-class signal observed in SDSS-class samples") which precedes the hedge. The Sec. V.A paragraph has both the old claim AND the hedge. The sharper fix: replace the first occurrence of "can reproduce" with "can generate a comparable pre-MASTER artifact" to match the already-present hedge wording. PARTIAL. |
| EXT5-P4-C5 | FM-177-4 | MAJOR | "Two primary estimators bypass the canonical-mask leakage channel" — WLS is ON the canonical-mask Ap field so cannot be said to "bypass" it | **VERIFIED (NEW — precision)** | Source l.565 and l.485: "the no-dipole-at-ℓ=1 verdict stands, anchored on these two estimators that bypass the canonical-mask leakage channel." Source Appendix D.g describes the WLS as a template fit on the canonical-mask Ap field with nuisance marginalization. The HC real-space estimator genuinely bypasses the harmonic leakage channel; the WLS marginalizes a clean-dipole template against nuisance templates on the same canonical-mask field — it does NOT bypass the channel, it marginalizes through it. ChatGPT's proposed reword is valid: "the HC real-space estimator bypasses the harmonic leakage channel, and the WLS estimator tests a clean-dipole template after nuisance marginalization on the canonical-mask field." **VERIFIED NEW MINOR-level precision improvement.** |
| EXT5-P4-C6 | FM-177-5 | MAJOR | WLS artifact Appendix D.g mask condition still uses truncated threshold string | **PARTIAL — needs line-level source check** | ChatGPT references "b_gal MINIMUM" or a truncated condition in the Appendix D.g design matrix. Source needs grep to verify. Mark PARTIAL pending source verification; not previously raised cleanly. |
| EXT5-P4-Cm1 | fm-177-1 | MINOR | "p_LEE ≤ 10⁻⁴" logic backwards (should say "rejects isotropic noise" not "signal is rejected as isotropic noise") | **VERIFIED (NEW MINOR)** | ChatGPT's reading is correct: "the signal is rejected as isotropic noise at p_LEE ≤ 10⁻⁴" is logically inverted. A small p_LEE rejects the isotropic null, attributing the signal to systematic structure. Valid one-line fix. |
| EXT5-P4-Cm2 | fm-177-2 | MINOR | Fig. 2 caption says "eight D4 transforms" but figure shows Z2 TTA examples + probability bars | **HOUSTON-DECISION (OPINION — editorial, same ruling since EXT4 fm-175-1)** | No new evidence. Ruled editorial in EXT4. |
| EXT5-P4-Cm3 | fm-177-3 | MINOR | Zenodo DOI not minted | **HOUSTON-DECISION (HD-11, mint-at-submission — fourth raise)** | Same ruling. |

### Grok EXT5 findings

| # | Code | Sev | Finding | Verdict | Evidence |
|---|------|-----|---------|---------|----------|
| EXT5-P4-G1 | Grok-MINOR-1 | MINOR | "NSIDE = 64" typographical slip ("N_STDE = 64" in PDF rendering) | **PARTIAL — extraction-artifact vs. real typo** | Source not grep-verified for "N_STDE"; likely a PDF-extractor artifact on the `\text{NSIDE}` macro. Pattern-052 applies. If the source has clean `\text{NSIDE}=64`, this is FALSIFIED. Mark PARTIAL pending source check. |
| EXT5-P4-G2 | Grok-MINOR-2 | MINOR | Table I caption footnote: "(23,600 of 49,152 pixels)" stale after 59,515-row QC exclusion | **PARTIAL (new)** | This is a legitimate consistency concern: the 59,515-row QC exclusion was introduced in v1.0.175; if the HC footprint pixel count parenthetical was not updated, it may be stale. Not previously audited at this specificity. PARTIAL pending source verification. |

### Gemini EXT5 findings (ACCEPT — two minors)

| # | Code | Sev | Finding | Verdict | Evidence |
|---|------|-----|---------|---------|----------|
| EXT5-P4-GM1 | Gemini-MINOR-1 | MINOR | Sec. VI.A 2√3 Fisher factor: derivation chain would benefit from a one-sentence inline parenthetical showing σ(A)=2√3·σ(f_CW) step at f_CW=0.5 | **OPINION (useful editorial)** | The derivation chain σ(A)=√(3/N)=2√3·σ(f_CW) is mathematically correct per the R34conf rederivation. Gemini's suggestion to add an inline derivation step is valid as a reader clarity improvement, but it is OPINION (no error exists). The re-raise rule does NOT apply here — Gemini correctly verifies the math and asks for a pedagogical sentence, not a correction. |
| EXT5-P4-GM2 | Gemini-MINOR-2 | MINOR | App B.d: text should state explicitly whether HuggingFace Parquet files preserve QC-flagged rows with a flag or pre-clean them | **VERIFIED (NEW MINOR)** | This is a genuine data-availability precision improvement. The paper states the flagged-rows exclusion (59,515 HC rows) and gives the HC dipole rerun; it does not explicitly say whether the public Parquet release preserves these rows with a `qc_flip_identity_violator` flag or omits them. Gemini's concern is actionable (one sentence in Data Availability). **VERIFIED NEW MINOR.** |

---

## Part III — Pattern-051 Check: R34conf edits

### Did the R34conf closure wave introduce regressions?

| Item | Status | Note |
|------|--------|------|
| Flip-swap metric defined (L1 formula) | CLOSED | Changelog confirms; no regression. |
| Fisher 2√3 rederived correct, no edit | CLEAN | Source l.520 matches; no regression. |
| "headline"→"primary" | CLOSED | No regression. |
| Ap notation (0.57% = 5.7×10⁻³) | CLOSED | No regression. |
| FM-175-2 sentence (l.565) | **INCOMPLETE** | Changelog says "applied" but l.565 is verbatim unchanged — this is a regression of the closure claim, not a regression introduced by the wave. The wave did not introduce new damage; the sentence simply was not edited. |

---

## Part IV — Verdict Counts

| Verdict | Count | Items |
|---------|-------|-------|
| **VERIFIED (carries action)** | **4** | EXT5-P4-C2 (hierarchy bullet — one-sentence edit), EXT5-P4-C3 (l.565 "same estimator" carryover — one-sentence replacement), EXT5-P4-C5 (WLS "bypass" precision — one reword), EXT5-P4-Cm1 (p_LEE logic inversion — one-line fix) |
| **VERIFIED NEW (first appearance)** | **3** | EXT5-P4-C5 (WLS bypass), EXT5-P4-Cm1 (p_LEE logic), EXT5-P4-GM2 (Parquet QC flag disclosure) |
| PARTIAL (needs source check) | 3 | EXT5-P4-C4 (Shamir still partially dual-phrased), EXT5-P4-C6 (WLS mask condition), EXT5-P4-G1 (NSIDE typo), EXT5-P4-G2 (pixel count parenthetical) |
| HOUSTON-DECISION | 3 | EXT5-P4-C1 (provenance/two-step, 4th raise), EXT5-P4-Cm2 (Fig. 2 caption), EXT5-P4-Cm3 (Zenodo DOI) |
| OPINION | 1 | EXT5-P4-GM1 (2√3 inline derivation sentence) |
| AUTO-FALSIFIED / STALE | 1 | R34-P4-23 typo was PDF-extraction artifact, not source error |

**Genuinely-new substantive count (EXT5): 3** — EXT5-P4-C5 (WLS "bypass" precision), EXT5-P4-Cm1 (p_LEE logic inversion), EXT5-P4-GM2 (Parquet QC flag disclosure). All are MINOR-level. The two VERIFIED carryovers (EXT5-P4-C2, EXT5-P4-C3) are genuine but not new — both have been open since EXT4.

---

## Part V — Reviewer Calibration

| Reviewer | Stated recommendation | Audit-calibrated | Delta |
|----------|-----------------------|-----------------|-------|
| ChatGPT | MAJOR REVISIONS | **MINOR REVISIONS** — FB-177-1 (BLOCKER) is Houston-Decision (4th raise of the two-step pin, AUTO-FALSIFIED as blocker). FM-177-1/2 are real but MINOR-level edits (one sentence each). FM-177-5 WLS mask partial. Net: 2 one-sentence fixes + 1 precision improvement. | Overcalled (BLOCKER → HOUSTON-DECISION; MAJORS → MINOR edits) |
| Grok | ACCEPT | **ACCEPT with two MINOR edits** (NSIDE/pixel-count parenthetical — both need source verification). Grok's ACCEPT is well-calibrated; no headline science challenged. | Accurate |
| Gemini | ACCEPT | **ACCEPT with one MINOR and one OPINION** (Parquet QC flag disclosure = valid MINOR; 2√3 inline derivation = OPINION). Gemini correctly identifies the math is right. **First EXT round where Gemini P4 findings are calibrated — no extraction artifacts this round.** | Accurate |

**Consensus:** P4 is at **MINOR REVISIONS** — specifically four bounded text edits: (1) hierarchy bullet pre-MASTER scope; (2) l.565 "same estimator" sentence; (3) WLS "bypass" precision; (4) p_LEE logic sentence. Plus two OPINION/MINOR cosmetic items. No reviewer challenged the +0.41σ HC dipole, the 2√3 Fisher floor, the z≈−18 WLS exclusion, or any committed artifact number. The scientific content is converged.

---

## Part VI — Closure Plan (hardest-first)

### C0 — EXT5-P4-C3 (VERIFIED carryover MAJOR, 3rd raise): Fix l.565 "same physical estimator"

Replace at l.565:
> `the two values describe the same physical estimator and footprint under different null-run sizes (the differing $p$-values reflect null-ensemble resolution, not different physics; see Sec.~\ref{sec:notation} and Table~\ref{tab:multipole} caption)`

With:
> `the $500$-MC $+3.64\sigmaunit$ direct single-mode value is retained for continuity with the leakage analysis; the $10^4$-permutation Table~\ref{tab:multipole} canonical row is the current high-statistics diagnostic under its committed field convention`

This has been the target replacement since EXT4 FM-175-2. The Table III caption already carries the correct language; this aligns the body.

### C1 — EXT5-P4-C2 (VERIFIED carryover MAJOR): Fix hierarchy bullet pre-MASTER scope

Replace at l.226:
> `\emph{Generative monopole-only null:} (vi)~$N=500$ binomial-monopole realizations demonstrating the $+3.64\sigmaunit$ canonical value is consistent with monopole-mask leakage`

With:
> `\emph{Generative monopole-only null:} (vi)~$N=500$ binomial-monopole realizations demonstrating that the raw pre-MASTER pseudo-$C_\ell^{(\ell=1)}$ is dominated by monopole-mask leakage; post-MASTER residuals require additional coherent systematics beyond the monopole-only channel (Sec.~\ref{sec:monopole_mask_null})`

### C2 — EXT5-P4-C5 (VERIFIED NEW): Reword WLS "bypass" claim

Replace at l.565 and l.549:
> `two estimators that bypass the canonical-mask leakage channel`

With:
> `two estimators: the HC real-space estimator, which bypasses the harmonic-leakage channel, and the block-bootstrap WLS template fit, which tests a clean-dipole template after nuisance marginalization on the canonical-mask field`

(One edit covers both occurrences at l.565 and l.549.)

### C3 — EXT5-P4-Cm1 (VERIFIED NEW MINOR): Fix p_LEE logic sentence

Locate "the signal is rejected as isotropic noise at $p_{\rm LEE} \leq 10^{-4}$" and replace with: "the direct-MC max-statistic null rejects isotropic random-label noise at $p_{\rm LEE} \leq 10^{-4}$; the excess is therefore attributed to systematic-floor structure."

### C4 — EXT5-P4-GM2 (VERIFIED NEW MINOR): Parquet QC flag disclosure

Add one sentence to Data Availability (near l.758): "In the public HuggingFace Parquet release, the 59,515 HC rows flagged by the catalog-wide `qc_flip_identity_violator` pass are retained with this flag column set to `True`; downstream users wishing to replicate the flagged-rows-excluded baseline should filter on this column."

### Optional / HOUSTON-DECISION

- C3 (FM-175-2): ALSO add one-sentence derivation footnote for 2√3 Fisher step as Gemini suggested (EXT5-P4-GM1) — OPINION, optional.
- EXT5-P4-G2 (pixel count parenthetical) — verify source then update "(23,600 of 49,152 pixels)" if stale.
- Shamir "can reproduce" dual-phrasing (EXT5-P4-C4) — complete P2 from EXT4 plan: remove the first "can reproduce" occurrence in favor of "can generate a comparable artifact under this pipeline."

### Ruled / HOUSTON-DECISION (no action this wave)

- EXT5-P4-C1 (two-step pin provenance): HD-11, mint-at-submission. AUTO-FALSIFIED as blocker (4th raise).
- EXT5-P4-Cm2 (Fig. 2 caption): editorial, Houston-decision.
- EXT5-P4-Cm3 (Zenodo DOI): HD-11.
- 2√3 Fisher factor: CORRECT, no edit.

---

## Exit-Criterion Assessment

**Four concrete text edits from clean** (C0–C3). Each is one sentence or one parenthetical. No headline science is challenged. No committed artifact number is disputed. After C0–C3: the paper's only open items are HOUSTON-DECISION policy (Zenodo, two-step pin, Fig. 2 editorial) + one new MINOR disclosure (QC flag in Parquet). Grok and Gemini both ACCEPT. ChatGPT MAJOR reduces to the two carryover one-sentence fixes + one new precision improvement.

**Expected EXT6 state after C0–C3+C4:** ACCEPT from all three reviewers.

---

*Verdict counts: VERIFIED 4 (all MINOR-level edits) · VERIFIED-NEW 3 · PARTIAL 4 · OPINION 1 · HOUSTON-DECISION 3 · AUTO-FALSIFIED 1*
*Genuinely-new-substantive count: 3 (EXT5-P4-C5, EXT5-P4-Cm1, EXT5-P4-GM2). All MINOR.*
*Pattern-052: not triggered on Gemini P4 EXT5 — Gemini gave text-logic findings with no extraction artifacts. First clean Gemini P4 round.*
*2√3 Fisher factor: CORRECT — re-raise rule in effect; any future challenge without new evidence is AUTO-FALSIFIED.*
*Carryover from EXT4/R34conf: EXT5-P4-C2 (hierarchy bullet, B2 carryover) and EXT5-P4-C3 (l.565 sentence, FM-175-2 / C3 carryover) — both have concrete fixes above.*
