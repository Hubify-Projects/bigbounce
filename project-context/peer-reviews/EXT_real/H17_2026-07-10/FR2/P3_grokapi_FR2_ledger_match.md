# ledger_match DRAFT — P3 — API_P3_grok.md

> DRAFT for the Opus truth-auditor, NOT a replacement. Conservative threshold (prefers UNMATCHED over a false match). Every UNMATCHED finding — and every low-score MATCHED — still needs a human/Opus source-cited disposition per §3.
>
> ledger: `project-context/peer-reviews/DISPOSITIONS/P3.md` (18 D-ids)  |  findings parsed: 7  |  threshold: 0.3

| # | sev | finding (first 120 chars) | best match | score | status |
|---|-----|---------------------------|-----------|-------|--------|
| 1 | MAJOR | REVISIONS ====================================================================== RAW RESPONSE (verbatim): ============== | — | 0.00 | **UNMATCHED** |
| 2 | MAJOR | REVISIONS (2) ISSUES: | — | 0.00 | **UNMATCHED** |
| 3 | MAJOR | Abstract and §I: The primary deliverable is repeatedly labeled a “validated catalog-grade subset of 268,519” while the t | DP3-07 | 0.99 | MATCHED |
| 4 | MAJOR | §III (three-tier structure) and §III E: The eROSITA tier is excised from every count because its production score axis i | DP3-08 | 0.50 | MATCHED |
| 5 | MAJOR | §II B and §VI D (i): The DESI robustness claim rests on a single production-ensemble injection-recovery gate (99–100 % a | DP3-01 | 0.47 | MATCHED |
| 6 | MINOR | Table II and footnotes ♡/♠/‡/⊗: Multiple mutually inconsistent denominators and threshold definitions (fixed-size contin | DP3-09 | 0.21 | **UNMATCHED** |
| 7 | MINOR | §II B: Full-sample feature scalers for tabular surveys leak validation-set tail information into the normalization; the  | DP3-07 | 0.28 | **UNMATCHED** |

**Match rate: 3/7 = 43% MATCHED, 4 UNMATCHED.**

Exit 2 — 4 finding(s) need a full §3 truth-audit (genuinely-new candidates or too-weak fingerprint overlap).
