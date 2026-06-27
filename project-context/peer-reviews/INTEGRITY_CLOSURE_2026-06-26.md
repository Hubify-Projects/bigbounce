# Integrity-Audit Closure — Honest-Reporting Fixes

**Date:** 2026-06-26
**Driver:** INTEGRITY_AUDIT_2026-06-26.md (independent audit; verdict: convergence GENUINE on substance, MILD self-favoring OPINION-vs-MINOR bias on 5/19 sampled dismissals)
**Action:** the 5 UNCERTAIN / mild-real-issue items were re-opened as MINOR and the paper reporting was made more conservative/complete. None alters a scientific conclusion; every change makes the headline reporting LESS self-favoring. No fabrication — every number is grounded in the committed source/artifacts.

| # | Paper | Item (audit) | Honest fix made | New class |
|---|-------|--------------|-----------------|-----------|
| 1 | P5 | Bonferroni threshold printed 4.05 for K=1054, two-sided α=0.05 (slightly liberal); audit's "convention-dependent/OPINION" framing was inaccurate — the formula is unambiguous. | `p5_desi_chirality.tex` L1051 `\|\sigma\|^{Bonf}_{0.05,1054}≈4.05` → **4.07** (recomputed: `norm.ppf(1−0.05/(2·1054))=4.0679`). Single computable factual correction. | MINOR (closed-by-real-action) |
| 2 | P4 | Abstract headlined the larger **secondary-implementation** label-shuffle null z=0.70; the same-generator **primary** is z=0.58 (body L606). Reporting-emphasis. | `chirality_catalog_paper.tex` abstract: headline now `z=0.58` (same-generator primary; an independent re-implementation gives z=0.70) in both the result sentence and the diagnostic Note. Abstract now matches body provenance. | MINOR (closed-by-real-action) |
| 3 | P3 | Abstract headlined 269,317 "catalog-grade" entries; the "two components carry exploratory validity flags" carve-out was only at L1177. | `paper3_draft.tex` abstract: the 269,317 catalog-grade headline now carries the carve-out that two components (Gaia DR3 + eROSITA DR1) hold per-object exploratory validity flags and are not robustly validated detections (see §eROSITA). | MINOR (closed-by-real-action) |
| 4 | P2 | The entire 5.2–5.5σ headline rests on one external number σ(f_NL)≈0.7 (Heinrich 2023); provenance foregrounded only once. | `02_full_draft.tex` abstract: the "We adopt … 5.2–5.5σ … as the headline forecast" sentence now restates that both ranges rest on the single imported Heinrich+2023 σ≈0.7 baseline recast for template mismatch (sensitivity recast, not an independent cross-Fisher forecast). | MINOR (closed-by-real-action) |
| 5 | P1B | SN-overlap (~20% shared SNe) robustness of the w0wa quintom cross-check "not demonstrated quantitatively" (body L1611); control chains deferred — could reopen if follow-up never posts. | `paper1b_mcmc_companion.tex` §physics-interpretation lead (≈L1506): the cross-check headline now states plainly that robustness against the SN-overlap systematic has **not** been demonstrated quantitatively in this manuscript (control chains deferred to a follow-up note), and is reported as an exploratory compatibility check only — promoting the L1611 caveat to the result headline. | MINOR (closed-by-real-action) |

**P1A:** not among the 5 — no honest-reporting fix required (its 3 sampled dismissals all held up AGREE in the audit).

## Build / mirror / version (all 5 touched papers)

| Paper | New version | PDF md5 (full) | Pages | Undef-refs |
|-------|-------------|----------------|-------|-----------|
| P1B | v1B.0.78 | 57f27be76f5ee739c1ee6098a3cc976f | 22 | 0 |
| P2  | v1.7.73 | fdd0e85d743f6884534a517e39872998 | 28 | 0 |
| P3  | v3.1.115 | a711267bfb7c739c8f4ddbc7f6788ddd | 30 | 0 |
| P4  | v1.0.190 | 83ee79616fc3a23ecc77a46570f1a68d | 23 | 0 |
| P5  | v0.1.85-2026-06-26 | 4efb89a22a67d7029e9e1d6b5791f471 | 33 | 0 |

- Each PDF recompiled (3× pdflatex + bibtex), 0 undefined references, and re-mirrored byte-identical to every served path (public/papers versioned+alias, site/public/papers versioned+alias, site/public root aliases, source dir, plus an OLD-md5 sweep refreshing all prior-version mirrors).
- `site/src/data/papers.ts` updated for all 5 (version + pdfMeta + Read/Download href; P1B pages 21→22).
- Convex `paperVersions:bump` posted for all 5 (datestamp 2026-06-26, texCommit c6982e66, changelog "integrity-audit honest-reporting fixes"). Mutation IDs: P1B k578jp7d…, P2 k57a19e9…, P3 k577rwe2…, P4 k57cag4z…, P5 k575qevm….

## Note on the structural recommendation (audit §RECOMMENDED FIXES #1–2)
The EXT-prompt de-biasing (`ExternalReviewPanel.tsx` L58–59 "Default to MAJOR only when…" / "MINOR REVISIONS or ACCEPT is the appropriate verdict") is a **skill/prompt** change, not a paper fix, and is left for a separate `kind:"skill-improvement"` round per the standing CLAUDE.md timeline rule. This closure covers only the 5 paper-level honest-reporting items.
