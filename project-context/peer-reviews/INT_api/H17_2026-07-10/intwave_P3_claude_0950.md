# INT Claude-subscription Review — P3 v3.1.155 — claude-opus-4-8
paper: P3  version: v3.1.155  tex: pipelines/p3_anomaly_engine/paper3_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T16:50:28Z
context-note: rebuild wave 2/2 on v3.1.155; no changes since FR4 (DP3-19 verified at all sites)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've verified the load-bearing numbers against committed artifacts (recomputed, not just read): the 268,519 headline dedup (`reproduce_headline_dedup.json`: 274,353→268,519 exactly), the full NANOGrav chain (`savage_dickey_2026-05-29.json`), the f_NL Fisher arithmetic, and the DESI injection-recovery curve. Nearly everything reproduces. Here is my review.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR]** §sec:nanograv, `paper3_draft.tex:1562` (and repeated at L1003, L1626, L1645). The displayed posterior γ = 2.567 ± 0.382 does not reproduce the quoted parameter-shifts to the stated last digit: a reader recomputing gets (3.0−2.567)/0.382 = **1.13σ** (paper says +1.14σ) and (4.33−2.567)/0.382 = **4.62σ** (paper says +4.63σ). The paper's values are in fact *correct* — they come from the full-precision chain (`savage_dickey_2026-05-29.json`: γ=2.5665, σ=0.3818, z_dist 1.1354 and 4.627) — but the rounded display values shown to the reader round the other way. Fix by displaying one more digit (γ = 2.5665 ± 0.3818) or quoting the shifts as +1.13σ/+4.62σ. This is the one residual instance of the display-vs-chain-precision class the changelog's own DP3-19 "consistency" pass otherwise closed.

2. **[MINOR]** Compile hygiene: `paper3_draft.log` reports 3 Overfull \hbox warnings in table alignments (L1122–1132 ≈1.8pt; L1592–1605 ≈6.9pt; L1856–1863 ≈4.7pt). Sub-7pt column overflow — cosmetic but should be cleared by a `/latex-audit` pass (`table*`/`makecell` width fix) before submission. (Otherwise clean: 0 undefined references, 37 pages, figures embedded.)

3. **[MINOR]** Presentation density. The abstract and §sec:fnl/§III carry an unusually high concentration of parenthetical caveats and repeated "process-volume" disclaimers (e.g. the abstract states the process-volume caveat three times). The disclosure is scrupulously honest — this is a readability, not correctness, issue — but a PRD editor will likely request condensation so the load-bearing result (the recomputable 268,519 catalog) is not buried. Consider consolidating the repeated process-volume framing into a single statement.

4. **[MINOR]** §III / §sec:pathc_caveats(i): the "validated catalog-grade" language is honestly qualified in-text (one production-ensemble injection-recovery gate on *re-pulled* SPARCL spectra after the original production spectra were lost; the two Jaccard gates run on short-trained proxy models that fail the paper's own `val_loss≤0.30` retain gate and are explicitly labeled "correlated stability probes, not independent confirmations"). This is disclosed thoroughly and is not an error, but the residual tension between the word "validated" and a single genuine production-model sensitivity gate is the one point a PRD referee is most likely to press on; no additional edit is strictly required, but a one-line reiteration of "single production-ensemble gate" at the first use of "validated catalog-grade" would preempt it.

**(3)** Yes — the central claim (a reproducible, honestly-scoped catalog-grade subset of 268,519 multi-survey reconstruction-outlier anomalies, with the two cosmological applications explicitly presented as null/non-detections) is supported: I reproduced the 268,519 dedup, the injection-recovery 5σ→99–100% broad-class PASS, and the full NANOGrav/f_NL numeric chain directly against the committed artifacts, and found no genuinely-new factual error — only the minor display-precision and presentation items above.
