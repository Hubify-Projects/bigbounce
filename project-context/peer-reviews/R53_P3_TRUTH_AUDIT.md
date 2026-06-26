# R53 P3 — Truth Audit (verdict-first vs source)

**Paper:** P3 — Multi-survey anomaly catalog. Source: `pipelines/p3_anomaly_engine/paper3_draft.tex`.
**Compiled PDF:** `/tmp/R53_P3/paper3_draft.pdf` md5=464d4066, 29 pages, 0 undef refs.
**Legs:** Claude (Opus full read) + Grok 4.3 (OK) + Gemini 2.5 Pro (OK) + OpenAI gpt-5 high (OK). Perplexity FAILED (API quota 401). 3/4 vendor legs returned.
**Prior state:** R52+EXT21+EXT22 polish-tier convergence (0 BLOCKER / 0 genuine MAJOR).

## Net verdict: ACCEPT (polish-tier). 0 BLOCKER, 0 MAJOR. 2 genuine MINOR closed.

OpenAI's own arithmetic spot-audit independently re-derived and CONFIRMED every
headline scalar (378,080+200=378,280; 269,317−200=269,117; 141×/100×/73×/0.9×
Liang ratios; Wilson ±1.2%; Fisher F0/σ=8.14/envelope[3.92,8.98]; α 0.29σ;
NEOWISE z≈4.07; Cramér V 0.0064; dedup 388,493→378,280 @2.63%). My independent
recompute of ~40 arithmetic claims across abstract/body/tables/appendices: all pass.

## Closed this round (2 VERIFIED MINOR)

| ID | Tier | File:area | Old → New | Basis |
|----|------|-----------|-----------|-------|
| CLAUDE-1 (own find) | MINOR | paper3_draft.tex Fig.6 novelty caption (~L941) | "factor of ~5.6× relative to the SIMBAD-unmatched aggregate" → "...relative to that same DESI top-stratum's ~99% SIMBAD-unmatched fraction (the stratum on which the 17.8% is measured; the 58.8% four-survey aggregate is a separate pooled population)" | Internal inconsistency: 5.6 = 99.8/17.8 (DESI top-1000 unmatched), NOT 58.8/17.8 = 3.30. "Aggregate" is defined in the SAME caption (L930) as 58.8%. Number 5.6 correct; referent mislabeled. Fix preserves verified number, corrects referent to value already stated in caption ("DESI DR1, 99% of top-10K"). |
| OAI-E8 | MINOR | paper3_draft.tex Fig.3 caption (L768, L776-780) | (L768) "cross-transfer for SDSS, native for DESI/LAMOST" → "native for DESI, cross-transfer for SDSS and LAMOST"; (L776-780) "Important: S axis of DESI and LAMOST on different native-retrain scales..." → rewritten to state the LAMOST curve is the pre-Path-C cross-transfer scan (44,075 objects, DESI-trained model + DESI val normalization), superseded by native re-score (113,342 top-1% on separate scale, not plotted) | VERIFIED via `generate_figures.py:578-589`: figure plots DESI native count (195,829) but LAMOST at the **cross-transfer** count (44,075) on the DESI-trained S∈[5,26] scale (native LAMOST top-1% is at S≥0.4613, a different range). Caption "native for LAMOST" contradicted the plotted curve. Fix aligns caption with figure AND with the Fig.8 caption, which already calls Fig.3's SDSS axis "cross-transfer." |

## FALSIFIED / OUT-OF-SCOPE / OPINION (not closed)

**Grok (REJECT) — all findings falsified, opinion, or out-of-scope:**
- E1 (abstract 9.4% as positive): FALSIFIED — abstract verbatim says "noise-driven forecast... not a detection."
- E4 (29pp too long): OUT-OF-SCOPE — catalog-class; size not a defect (Houston directive).
- M1 (LAMOST in catalog-grade tier): FALSIFIED — paper EXPLICITLY excludes LAMOST from the 269,317/269,117 catalog-grade tier (exploratory only, L565).
- M2 (Fig.2 caption omits ACT exclusion): FALSIFIED — skymap caption (L678) states ACT 200 patches "should not be interpreted as anomaly detections," contributes zero.
- E2/E3/E5/M3/M4/M5/m-*: OPINION/already-caveated (17.8% fully caveated; SIMBAD-novelty distinction explicit; DOI = at-submission).

**Gemini (MAJOR REV) — all findings falsified, OCR artifact, blocked, or out-of-scope:**
- B1 (Fig.9 total 40,192 ≠ OCR sum 40,120): FALSIFIED — `generate_figures.py:747` n_ai=[174,61,2645,11853,**14781**,9328,1350] sums to EXACTLY 40,192. Gemini OCR-misread bar 5 as 14,709 (diff exactly 72). Caption correct.
- M1 (Table I footnote ♡ "self-reference"): FALSIFIED — phrase is in the table CAPTION (L689) forward-referencing footnote ♡ below; not a self-reference (rasterization conflated adjacent caption+footnote).
- D1 (§VIE broken ref): FALSIFIED — `sec:comparison` = §VI.E (Comparison with Prior Work); 0 undef refs confirm resolution. Gemini miscounted subsections.
- m1 (double-paren typo "((fnL)"): FALSIFIED — OCR of "(σ(f_NL) ≈ 0.7...)"; the inner paren is part of σ(f_NL) notation. Source correct.
- E1 (Gaia/NEOWISE scaler-refit "queued"): TRULY-BLOCKED — feature tables existed pod-side only; eROSITA load-bearing tier IS checked; existing caveat stands. Gaia already flagged exploratory.
- E2/N1 (DOI placeholder / date): deferred-genuine — DOI minted at arXiv submission; date = v3.1.113 version stamp (no-bump round). OUT-OF-SCOPE.
- M2 (length), m2/m3/m4: OPINION.

**OpenAI gpt-5 (MAJOR REV) — 1 genuine MINOR (E8, closed above); rest falsified/opinion/unverifiable:**
- E10 (SDSS S=1.9e11 "physically impossible"): FALSIFIED — caption already explains cross-transfer scaler inflation; OOD SDSS cool dwarfs are NOT unit-variance under the DESI scaler, so per-element MSE can be enormous; native re-score compresses to S<14. Mechanism sound.
- E9 (Fig.5 NEOWISE "256px×0.262=67″ not 108″"): UNVERIFIED → NOT changed. Cutout is an external DESI-Legacy product (not in `generate_figures.py`); 256px↔108″ is internally self-consistent at pixscale 0.422″/px. Caption does not assert 0.262″/px for this figure, so no internal contradiction; cannot confirm wrong without cutout metadata. Per "never fix a false positive," left as-is.
- E11 (Step 5 "500/survey" vs NEOWISE 1000/1000): borderline-MINOR, already substantially disclosed (NEOWISE flagged as geometry-QA "passes by construction" in 4+ places; the 500-amplitude-series statement plainly does not describe NEOWISE's geometry test). Not load-bearing; not closed.
- E1/E2/E7 (future DOI / \artifact paths in body): deferred-genuine / lab convention (\artifact verified by /artifact-link-verify). OUT-OF-SCOPE.
- E3/E4/E5/E6, M1-M10 (injection-recovery detail, abstract heterogeneity, PTA Eq dimensional, N_total convention, continuity-slice rationale, Fig.6 axis label, 3-vs-4 matches): OPINION / already-disclosed. M8 (3 vs 4): text already explains 3 spectroscopically-confirmed highlights vs 4 raw positional (4th consistent with 2.75 chance expectation, "no significance assigned").
- Pass-2 arithmetic spot-audit: independently CONFIRMS all headline scalars correct.

## Recompile + overflow
3× pdflatex, 29 pages, **0 undefined refs**, 0 rerun warnings. Overflow audit:
1 Overfull \hbox = **4.68pt** at L1369-1376 (PTA Bayes-factor table, UNTOUCHED, far below 50pt gate). Edited caption areas (Fig.3 p.10, Fig.6 p.14): **0 new overfull boxes**; visual render confirms both captions fill their column with no overflow/overlap.

## Convergence statement
P3 is at **polish-tier convergence**. This round found and closed **2 genuine MINOR caption/labeling inconsistencies** (1 self-found, 1 from OpenAI E8 — both VERIFIED against the figure-generation source). Three vendors returned REJECT/MAJOR-REV headline verdicts, but on source-cited audit **every** ESSENTIAL/MAJOR resolves to FALSIFIED (incl. 3 OCR/rasterization artifacts), OPINION, length (out-of-scope for catalog class), TRULY-BLOCKED (pod-side data), or deferred-genuine (DOI-at-submission). **0 BLOCKER, 0 genuine MAJOR, 0 unclosed VERIFIED DO-NOW.** No commit/bump/mirror performed per instructions.
