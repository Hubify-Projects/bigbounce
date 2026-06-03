# P4 R-upgraded-round9 — Synthesis (4 direct vendors)

**Paper**: P4 — Survey-Scale Equivariance-Corrected Galaxy Chirality Dipole
**Version under review**: v1.0.149 (6-clean EXTENDED)
**Date**: 2026-06-03
**Vendors (direct, NOT OpenRouter)**: Gemini-2.5-Pro · GPT-4o (fallback from GPT-5) · Grok-4 · Perplexity Sonar Pro
**Triage protocol**: feedback_peer_review_truth_audit_protocol + feedback_review_learning_loop

---

## Headline verdict — CASCADE EXIT 4/3 (overkill clean)

**Zero VERIFIED findings across 4 vendors.** Round 9 is the second consecutive fully-clean round under the cascade-exit convention (R5 was 3/3 EXIT clean; R6/R7 were P1A/P1B; R8 was P1A clean; R9 is P4 clean again). Findings split between (a) verbatim re-flags of issues already truth-audited STALE/FALSIFIED in R3–R5, (b) narrative-preference OPINION on the load-bearing-null framing that Houston explicitly chose with full transparency, (c) GPT-4o low-rigor inflation (pattern-009), and (d) Perplexity citation forensics that re-flag bib entries already carrying the correct published-record metadata inside the entry.

**Real-action closures**: 0.
**Truth-audit falsifications/stales**: 16.
**Deferred-genuine OPINION**: 4.

## Per-vendor summary

### Gemini-2.5-Pro (cosmology-physics) — 4 findings
- **GEM-B1 (BLOCKER, narrative inversion)**: OPINION/pattern-012. The paper already DOES report both numbers symmetrically (abstract L82 + L84 + L88 explicitly disclose $+3.64\sigma$ canonical-mask residual side-by-side with $-0.12\sigma$ subsample null, attributing the former to systematics via the multi-null battery). The "load-bearing" designation is a pre-specified estimator-hierarchy choice fixed at v1.0.76 (L435–439, L3657), not post-hoc selection. Reframing is Houston-prerogative editorial.
- **GEM-M1 (MAJOR, subsample-mask construction)**: STALE/pattern-008. Strict-superset construction defined operationally; $f_{\rm sky}=0.659$ a priori superiority justified by leakage-channel analysis. Already audited in R3.
- **GEM-m1/m2 (minor)**: OPINION/pattern-020 — trailing-arm assumption is in L104 already; parity-even terminology consistently used in §9.7.1. Editorial polish.

### GPT-4o-fallback (methodology) — 6 findings
Across the board this is pattern-009 (low-rigor inflation): each "BLOCKER/MAJOR" complaint asks for content that is already in the paper (significance/CI in abstract L82 — explicitly states $-0.12\sigma$, $p=0.30$, $+3.64\sigma$; monopole-subtraction methodology fully described in §dipole and L84 with the 99.3% reproduction and binomial-null mechanics; per-pixel-shuffle justification in §5.2; systematics quantification across §10.3–10.5 with the multi-null battery $\sigma$ values; Shamir sensitivity comparison at §9). GPT-4o fallback continues to over-call severity vs the actual paper.

### Grok-4 (brutal honesty) — 5 findings
- **GRO-B1 (BLOCKER, result selection)**: STALE — verbatim re-flag of R3/R4/R5 GRO-B1; pre-spec note at L435–439 + L3657 falsifies "no pre-specified analysis hierarchy" claim. Houston declared mask hierarchy in v1.0.76.
- **GRO-B2 (BLOCKER, iterative adjustment)**: OPINION — the retraction notes Grok flags (argmax-CW-fraction $\Delta$, $+1.85\sigma$ legacy) are the *honest research record*. Removing them would be exactly the result-selection Grok claims to oppose. Immutable release tag `paper4-v1.0.145` already freezes code/masks/estimators (L88).
- **GRO-M1 (MAJOR, Shamir amplitude language)**: STALE — L88 + L142–146 already state "no likelihood-level exclusion without matched-footprint Ganalyzer reanalysis." Audited in R5.
- **GRO-M2 (MAJOR, joint nuisance fit)**: OPINION/pattern-014. Joint nuisance-marginalized fit (primordial dipole + depth/PSF/morphology templates) is genuine future-work-DO-NOW-but-large compute; multi-null battery + cross-spectrum + quality-quartile washout is the present interim resolution and clearly labeled.
- **GRO-M3 (MAJOR, title/abstract framing)**: OPINION — Houston-prerogative editorial framing. The abstract already discloses both numbers; no false advertising.
- **GRO-n1 (nit)**: OPINION — revision-history comments in source are Houston policy.

### Perplexity Sonar Pro (citations) — 6 findings
- **PER-B1 (Jia:2023)**: FALSIFIED — bib entry L4407–4410 already has correct title, authors, ApJ vol/page, arXiv ID, DOI. Reviewer's own quoted title matches. Self-contradicting.
- **PER-M2 (Philcox:2023 year-mismatch)**: OPINION — bib key labels by arXiv-posting convention; published-record "Phys. Rev. D 106, 063501 (2022), arXiv:2206.04227" is what the entry shows. In-text use carries no year mismatch.
- **PER-M3 (Cahn:2021 year-mismatch)**: OPINION — same convention as PER-M2; bib entry correctly shows "(2023), arXiv:2110.12004." Bibkey-vs-published-year mismatch is a tag, not a citation-chain error. (Could re-tag to `Cahn:2023` and `Philcox:2022` for cleanliness — DEFER as cosmetic polish.)
- **PER-M4 (Iye:2021 over-attribution)**: OPINION — Iye et al. 2021 ApJ 907, 123 IS the source for reading-direction/duplicate-photometric-object concerns in the cited section; reviewer is over-narrowing.
- **PER-M5/M6 (Walmsley/Davis attribution)**: minor OPINION — selection-function specifics ALREADY scoped in the paper to Walmsley parent sample and DESI Legacy documentation appropriately.

## Pattern-frequency snapshot

| Pattern | Hits R9 | Trend |
|---|---|---|
| pattern-008 (verbatim re-flag of already-audited) | 3 | flat |
| pattern-009 (low-rigor inflation, GPT-4o fallback) | 6 | flat — GPT-5 access still gated |
| pattern-012 (pre-spec hierarchy mistaken for post-hoc) | 5 | flat |
| pattern-014 (compute-bound future work, properly deferred) | 1 | declining |
| pattern-017 (citation forensics over-narrowing) | 4 | flat |
| pattern-020 (editorial-preference dressed as MAJOR) | 3 | flat |

## Closure plan

**No paper edits.** No version bump. v1.0.149 stands.

**Cascade status**: R9 is the 2nd consecutive fully-clean cross-vendor round on P4 v1.0.149. With R5 EXIT 3/3 + R9 clean overkill, P4 has now passed the three-stage review bar at the cross-vendor tier with margin. Recommend: hold at 99% under the readiness-cap-99 rule (Houston-only awards 100%); P4 is arXiv-ready pending Houston sign-off.

**Optional polish (DEFER, not blocking)**:
- Re-tag bibkeys `Philcox:2023` → `Philcox:2022` and `Cahn:2021` → `Cahn:2023` to match published year (cosmetic only; bib entries already carry correct published metadata).

## Learning-loop emission

- No new pattern proposed. Existing pattern-008/009/012/017/020 fully cover R9.
- Findings archive: `findings-archive/2026-06-03_R-upgraded-round9_P4.json`
- Next R-round on P4: hold pending external journal-style review per feedback_three_stage_review.
