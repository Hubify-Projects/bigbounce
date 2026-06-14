# EXT12 Harvest — P5 — ChatGPT Pro Extended

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc684-5918-83e8-b53e-28fde5fca69a
- PDF md5: e5a3999a (p5_desi_chirality_v0.1.77.pdf)
- Submitted: ~17:31 PDT 2026-06-13
- Harvested: 2026-06-13 18:39 PDT
- EXT11 baseline: MINOR REVISIONS
- EXT12 verdict: **MINOR REVISIONS**

## Headline Verdict

Recommendation: MINOR REVISIONS, very light. "I would not require another full referee round
after these are corrected."

## EXT12 Progress (Items CLOSED)

1. T-Web rename: substantially closed (main method now correctly labelled T-Web, key figures
   corrected — Fig. 2, 3, 9 now show T-Web titles in rendered PDF)
2. Adversarial unit-convention footnote: closed ("Any reviewer claim..." / "FALSIFIED" removed)
3. DESIVAST primary analysis: scientifically closed
4. Footprint-restricted DESIVAST control: closed
5. ASTRA-DESI framing: closed (correctly framed as diagnostic)
6. Dual-parent ledger: closed (Appendix B exact 4×2 contingency tables)
7. Conditional-permutation framing: closed

## Remaining Open Items (4 minor — all production-level)

**O1. Residual non-historical V-Web tokens** (main remaining production issue):
- §VIII A, p. 17: "+8–18 pp V-Web-vs-T-Web void-fraction discrepancy" → "P5 T-Web vs Ref.[11] T-Web"
- §IX B, p. 25: f^V-Web_CW and n_V-Web in Tempel concordance → f^T-Web_CW and n_T-Web
- Appendix C: "V-Web/T-Web grid pipeline" → "T-Web grid pipeline, with legacy vweb filenames"
- Primary/secondary list says "T-Web / ... / T-Web" → second T-Web should be "external T-Web [11]"

**O2. Fig. 8 still has visible overlap** (colorbar overlaps bottom-panel title on p. 22)

**O3. "Verdict." paragraph label in §IX B** → rename to "Summary" or "Result" (referee-report
language leaked into article prose)

**O4. Final archival DOI placeholder** (Zenodo — replace with actual DOI before publication)

## Auto-Falsify Checks

- P5 V-Web→T-Web figure regeneration (EXT11 auto-rule): Figs 2/3/9 are CONFIRMED fixed.
  ChatGPT explicitly says "Fig. 2 and Fig. 3 now show T-Web titles in the rendered PDF, and
  Fig. 9 now reads 'T-Web vs Tempel FoF' rather than 'V-Web vs Tempel.'"
- P5 Table I "MS" = pdftotext artifact: EXT11 auto-rule confirmed — not flagged by ChatGPT.
- Residual stale V-Web tokens in §VIII/§IX: NEW pattern, ~3 token replacements + §IX label

## EXT13 Closure Effort

~30 min: 4 token replacements + Fig. 8 rerender + "Verdict." → "Result." rename.
High confidence ChatGPT → ACCEPT in EXT13.
