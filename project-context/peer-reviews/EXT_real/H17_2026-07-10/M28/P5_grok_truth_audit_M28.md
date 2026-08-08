# P5 Grok EXT truth-audit — M28 (2026-07-13)

**Raw:** `M28/P5_grok_M28.md` (read verbatim) · screenshot `M28/P5_grok_M28.png`
**Verdict:** MINOR REVISIONS (3 MAJOR / 2 MINOR)
**Version reviewed:** v0.1.126 — submitted BEFORE the v0.1.127 DP5-26 artifact-range fix.
This wave is INFORMATIONAL (pre-fix version); the post-fix streak is determined by M29.

**Provenance:** verdict word MINOR REVISIONS confirmed on line 1 of the raw; the closing
paragraph (line 11) credits the central null. Grok is EXT / PDF-only, so it does NOT
see the source-level artifact-index range strings that DP5-26 concerns.

## ledger_match + Opus adjudication (5 findings + 1 scaffold)

| # | sev | disposition | verdict |
|---|-----|-------------|---------|
| 1 | MINOR | scaffold-header parse artifact ("REVISIONS (2) ISSUES:") — NOT a finding | — |
| 2 | MAJOR | DP5-13 (post-hoc designated-primary / Bonferroni-5 forking-paths) | RE-FLAG-DISCLOSED (§V B `sec:primary_path` l.1668, `tab:analysis_tree` l.1848; abstract l.729-730 label bounds exploratory) |
| 3 | MAJOR | DP5-11 (≈0.9pp quadrature systematic envelope) + DP5-12 (RSD first-order recon) | RE-FLAG-DISCLOSED (§VIII term list √0.886=0.94pp; RSD closed first-order v0.1.122, `outputs/27_rsd_void_recon_bound.json`; dedicated sensitivity table = OPINION on presentation) |
| 4 | MAJOR | DP5-09 (2a−1 de-attenuation to ≈2.26pp; environment-independence assumption) | RE-FLAG-DISCLOSED (abstract l.749-757 flags symmetric-error approx; DP5-08 void-stratum measured, void arm ±3.7pp under-powered so caveat STAYS) |
| 5 | MINOR | DP5-14 (T-Web bright/dark ∼2.1σ sign-flip = survey-selection diagnostic) | RE-FLAG-DISCLOSED (abstract l.718 T-Web secondary/diagnostic; §VI D χ²=4933 sign-flip is the paper's OWN disclosure) |
| 6 | MINOR | DP5-21 (companion Paper-IV dependence / placeholder arXiv) + DP5-18 (DAS/inputs) | RE-FLAG-DISCLOSED (§I "Independence from Paper IV internals" + §XIII + App A; DAS present §data_code) |

**0 genuinely-new findings.** Every substantive item fingerprint-matches a standing DP5
disposition; the lone UNMATCHED (#1) is a parser scaffold header, not a reviewer finding.
No bump. directive_g.sh NOT run. Pre-fix version → no streak effect (M29 governs).
Cap HOLDS 74 (Grok MIN 12 + ChatGPT MAJ 6 + Gemini MAJ 6 = 50+24; post_verdict.sh recomputed).

Integrity: no faked accept, no un-sourced dismissal, no fabrication.
