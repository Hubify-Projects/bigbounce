# INT Claude-subscription Review — P3 v3.1.152 — claude-opus-4-8
paper: P3  version: v3.1.152  tex: pipelines/p3_anomaly_engine/paper3_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T02:19:21Z
context-note: re-test on v3.1.152, no changes since last review — checking stability

======================================================================
RAW RESPONSE (verbatim):
======================================================================

Verified against committed artifacts (recomputed, not just read):

- `training_summary.json`: `best_val_mean = 1.9124` (≈1.91 ✓), `all_folds_pass_gate = false` ✓, and all five folds individually `gate_pass: false` — the §II.F "correlated fold-stability probes, not independent gates" disclosure (DP3-01) is faithful.
- `reproduce_headline_dedup.json`: `total_validated_survey_level_detections = 274,353 → VALIDATED_HEADLINE_unique = 268,519`, point-source 268,319 — matches the abstract chain exactly; DESI input 195,829 (DP3-05 base).
- Bookkeeping: 37,292,042 − 20,000 = 37,272,042 ✓ (DP3-03 footnote).

Version confirmed v3.1.152, `\date{July 10, 2026}`, unchanged. All disposition anchors (L984, L988, L1069, L1182) present in the .tex as the ledger claims.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MAJOR] End-to-end reproducibility is not achievable from the committed tree — §II.F, `paper3_draft.tex:1069`.** The full per-object held-out re-inference of the 22.5M-spectrum DESI catalog with the production 5-seed ensemble is blocked ("raw native score parquets are on an exited pod, not in the committed tree or HF release"); the committed `reproduce_headline_dedup.py` validates only dedup arithmetic (274,353→268,519), not the acquisition/scoring chain. This is honestly disclosed, not concealed, and the headline is recomputable — but for a catalog paper a PRD referee will still want a genuine re-inference path or an explicit Zenodo-hosted score release before final acceptance. **Disposition:** RE-FLAG of DP3-15 (OPEN-COMPUTE); no new defect, needs a GPU re-run, not an edit.

2. **[MAJOR] DESI robustness rests on a single production-ensemble gate — §II.F, `paper3_draft.tex:1069` / abstract `:988`.** Verified: the two Jaccard/tail-preservation checks are computed from the same short-trained k-fold vectors (`best_val_mean=1.91` vs the paper's own `val_loss ≤ 0.30` retain gate; all folds fail). The paper now states this verbatim ("correlated stability probes, not independent confirmations"). Honestly closed (DP3-01/DP3-02); flagged only because a referee would want the production ensemble itself subjected to a held-out injection-recovery beyond the broad/extended class. **Disposition:** RE-FLAG-DISCLOSED, closure verified intact.

3. **[MINOR] "Validated catalog-grade 268,519" vs 2,468 like-for-like benchmark and 98.7% sky/filler — abstract `paper3_draft.tex:984`.** The process-volume framing, the 2,468 science-target benchmark (≈0.92× Liang), and the 98.7% sky/filler fraction are all foregrounded in the first sentence and the §I reader's guide. Adequately disclosed (DP3-07); a referee may still prefer the science-target number as the headline.

4. **[MINOR] Heterogeneous, non-cross-comparable per-survey gates — §II, `paper3_draft.tex:1066`, Table `tab:survey_summary` footnote ♡.** S>5 vs continuity-slice (SDSS 77,905 vs 19,253 top-1% vs 12 at S>5) vs top-1% vs eROSITA knee vs NEOWISE mask-geometry are tabulated and explicitly labeled survey-specific/not cross-comparable. Disclosed by design (DP3-09/DP3-14).

5. **[MINOR] §V cosmology (f_NL forecast, NANOGrav) is null/secondary and uses no catalog output — §V, abstract `paper3_draft.tex:992`.** Correctly titled "Cosmological Applications (Secondary Demonstrations)," returns null (α_jk=0.19±0.65; σ(f_NL) envelope, not a detection; γ=2.567±0.382 a consistency statement only). A legitimate reviewer opinion that it should be trimmed/moved to appendices (DP3-10/DP3-16) — this is a Houston-gated venue/scope judgment, not an editable error.

**(3)** Yes — the central claim (a self-consistent, honestly-scoped multi-survey ML anomaly *catalog*, with cosmology explicitly secondary and returning null) is supported: every headline number I recomputed matches its committed artifact, the "validated" label is correctly qualified as mixed-validation, and the residual concerns are disclosed limitations (reproducibility, venue) rather than errors or overclaims.

**Stability confirmation:** v3.1.152 is unchanged since the last review; a fresh full-text pass plus artifact recomputation surfaces **0 genuinely-new editable findings** — every point above fingerprint-matches an existing DP3-xx disposition with closures verified intact. Consistent with the H17G ledger (ChatGPT REJECT / Grok MAJOR both map entirely to disclosed content; pattern-066 referee-variance floor). No version bump warranted.
