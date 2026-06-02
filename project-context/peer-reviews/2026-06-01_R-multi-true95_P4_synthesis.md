# P4 v1.0.142 → v1.0.143 — R-multi-true95 multi-vendor R-round synthesis + truth-audit

**Round label**: `2026-06-01_R-multi-true95`
**Paper**: P4 (chirality_catalog_paper) v1.0.142 (June 1, 2026 PDT) → v1.0.143
**Reviewers dispatched**: 4 direct-vendor (no OpenRouter); 3 returned, Gemini failed with billing 403 (same dunning as v141 round).
**Cumulative reviewer time**: ~86s
**Cost**: ~$0.36 (Perplexity dominant at $0.34)

## Vendor verdicts at a glance

| Reviewer | Model | Status | B / M / m / n |
|---|---|---|---|
| Grok | `grok-4` | OK | 2 / 3 / 1 / 0 |
| GPT-5 | `gpt-4o` (fallback again) | OK | 6 / 0 / 0 / 0 |
| Perplexity | `sonar-pro` | OK | 2 / 2 / 1 / 1 |
| Gemini | `gemini-2.5-pro` | FAIL | 403 PERMISSION_DENIED (billing dunning, same as v141) |

**Net headline**: zero convergent BLOCKERs across vendors; round is dominated by STALE re-flags of v141/v142 closures and a 4-finding **confabulated citation split** from Perplexity that is FALSIFIED on direct arXiv verification.

## Truth-audit table

| Finding | Reviewer claim | Verdict | Evidence | Closure |
|---|---|---|---|---|
| GRO-B1 | Subsample-mask null vs canonical +3.64σ framing | **STALE** | Abstract L82: "headline scientific result is a null ℓ=1 chirality-dipole on the analysis subsample mask...−0.12σ"; L88 Scope: "subsample-mask null is the load-bearing scientific result; canonical-mask residual is interpretation (ii) systematic, not a primordial detection". Already at title-region of abstract. | None — closed v1.0.139. |
| GRO-B2 | Shamir factor 6-12 amplitude claim needs matched-Ganalyzer | **STALE** | Abstract L88: "A like-for-like matched-footprint Ganalyzer reanalysis under Shamir's pipeline + cuts is required for a likelihood-level exclusion under his estimator; we do not perform that reanalysis here." Already verbatim. | None — closed v1.0.139. |
| GRO-B3 | 0.29% Fisher vs 0.75% empirical threshold conflict | **STALE** | Abstract L88: "$\\gtrsim\\!0.75\\%$ (the demonstrated 50%-recovery-at-3σ threshold on the present HC subsample injection sweep; 0.5% is a tested non-detection point at the present pipeline, not the operational floor)". The Fisher 0.29% is statistical-only and tagged as such in §IV.A. | None — closed v1.0.142 PER-M3. |
| GRO-B4 | Joint nuisance-marginalized fit z=-18.1 needed as headline | **STALE** | §VI.D prose has z_boot=-18.07σ block-bootstrap as headline formal-exclusion number; v1.0.142 explicitly bumped from 264σ → 18σ. | None — closed v1.0.139. |
| GRO-B5 | Parity-EVEN parenthetical in abstract | **STALE** | Abstract L82: "this ℓ=1 observable is the isotropy-breaking axial-vector channel and is parity-EVEN: it is NOT a direct parity-violation test (the parity-odd analog requires 3D spin-vector or polarization-rotation cross-correlation observables outside this paper's scope)." Already verbatim what Grok proposed. | None — closed v1.0.139. |
| GRO-B6 | MC ensemble sizes inconsistent (500/1000/10000) | **OPINION** | Different MC sizes are intentional per estimator cost; 500-MC convergence for MASTER is documented in §V.C. Not a defect. | None — opinion. |
| GPT-B1 | Fisher floor vs empirical 0.75% — overclaim | **STALE** | Duplicate of GRO-B3. Already differentiated in L88 + sensitivity table §IV. | None. |
| GPT-B2 | Monopole-subtraction pre/post-MASTER inconsistency | **OPINION** | No specific defect cited. NaMaster appendix documents monopole-removal as part of mask-deconvolution kernel. | None — opinion. |
| GPT-B3 | Canonical residual not quantitatively explained | **STALE** | Joint 9-template (dipole + leg + density + density²) WLS fit added v1.0.139 §VI.D; depth/PSF/morphology decomposition in Table VI. | None — closed v1.0.139. |
| GPT-B4 | Injection-recovery on full catalog, not subsample | **OPINION / compute-bound** | HC subsample is the calibrated injection-recovery sample by construction; full-catalog injection would mix-in low-confidence regimes that the load-bearing null doesn't depend on. | None — OPINION; would over-engineer. |
| GPT-B5 | Full-catalog D4-TTA needed (21.4% flip rate) | **STALE/OPINION** | Table caption L533 explicitly: "the load-bearing subsample-mask post-MASTER ℓ=1 null (−0.12σ) is computed on the p_CW-weighted asymmetry map A_p (not on hard argmax labels), so the 21.4% per-galaxy argmax-flip rate is not a primary source of uncertainty on the headline". 1.21× empirical widening + 1.29× independence upper bound documented at L803-810. | None — closed v1.0.142 (GRO-m1). |
| GPT-B6 | Quantitative parity-violation transfer function | **OPINION / out-of-scope** | Paper explicitly defers parity-odd transfer-function modeling per Scope statement L88 — parity-odd analog requires 3D spin/polarization observables. | None — out-of-scope by design. |
| PER-B1 | bib `Shamir:2022DESI` mixes metadata: claims arXiv:2208.13866 is PASP 134 104501, MNRAS 516 2281 is arXiv:2207.10634 SDSS paper | **FALSIFIED** | Verified directly at arxiv.org: **arXiv:2208.13866 IS "Analysis of spin directions of galaxies in the DESI Legacy Survey", Lior Shamir, MNRAS, DOI 10.1093/mnras/stac2372** — exactly as our .bib states. arXiv:2207.10634 is a string-landscape paper by Guleryuz, not Shamir SDSS. Perplexity confabulated a PASP citation that does not exist. | None — Perplexity confabulation. |
| PER-B2 | "Shamir 2022" used ambiguously across SDSS + DESI | **FALSIFIED** | Predicated on PER-B1 being true; since PER-B1 is FALSIFIED (there is no separate Shamir 2022 SDSS MNRAS paper at arXiv:2207.10634), the ambiguity claim collapses. Our `Shamir:2022` (PASJ 74, 1114, methodology) and `Shamir:2022DESI` (MNRAS 516, 2281, DESI Legacy) are correctly distinguished. | None — Perplexity confabulation. |
| PER-M3 | "MNRAS 516 2281" wrong venue for DESI paper | **FALSIFIED** | Same as PER-B1: MNRAS 516, 2281 IS the DESI Legacy Shamir paper. | None — Perplexity confabulation. |
| PER-M4 | Sample-size sentences ambiguous after correcting refs | **FALSIFIED** | Predicated on PER-B1; collapses since there is no correction to make. ~1.3M DESI input galaxies traces correctly to arXiv:2208.13866. | None — Perplexity confabulation. |
| PER-m5 | SpArcFiRe 99.983%/85.8% needs Table-specific qualifier | **OPINION** | Reads cleanly in context of §VII.B (SpArcFiRe subsection); fully cited to Davis & Hayes 2014. | None — opinion. |
| PER-n6 | LSST bib comment block internally confusing | **STALE** | Bib L4522 already explains the arXiv:0805.2366 / ApJ 873, 111 split with explicit "citation flag closed in an earlier revision" provenance. Working as intended. | None — closed in earlier revision. |

## Net verdict

- **Total findings**: 17 across 3 reviewers.
- **0 VERIFIED** new findings requiring text edits.
- **8 STALE** (already closed in v1.0.139/v1.0.141/v1.0.142 prose; reviewers re-flagged because BLOCKER framing draws their eye to the topic even when the closure is in-text).
- **6 OPINION** (expand-prose / compute-bound / out-of-scope asks; no falsifiable defect).
- **4 FALSIFIED via direct arXiv verification**: Perplexity's PER-B1/B2/M3/M4 chain is built on a confabulated claim that arXiv:2208.13866 is a PASP paper. WebFetch of arxiv.org/abs/2208.13866 returns Shamir's MNRAS DESI Legacy paper, DOI stac2372 — exactly as our .bib says. The "alternate" arXiv:2207.10634 Perplexity cites for the "SDSS MNRAS 516 2281" paper is a Guleryuz string-landscape paper, not a Shamir paper at all. This is the cleanest external arXiv catch since v141 closure.

**Verification artifact**:
- arXiv:2208.13866 → "Analysis of spin directions of galaxies in the DESI Legacy Survey", Shamir, MNRAS, DOI 10.1093/mnras/stac2372 ✓
- arXiv:2207.10634 → "(Super)Universal Attractors and the de Sitter Vacua in String Landscape", Guleryuz, JCAP 05, 039 (2023) ✗ (not Shamir)

**0 compute-bound items**. **0 text-edit items**. **0 deferrable items**.

## v1.0.143 changelog

Round closure-only version bump:
- `\paperVersion v1.0.142 → v1.0.143` (L54)
- `\paperTimestamp June 1, 2026 PDT` (unchanged — same calendar day)
- `\artifact{paper4-v1.0.142}` → `paper4-v1.0.143` × 4 occurrences (L35, L88, L365, L4310)
- PDF: 55 pages, 26,256,301 bytes, md5 `8bfd8d1b370f081ac6c67f8e00351cf1`
- Mirrored to `site/public/papers/chirality_catalog_paper.pdf` + `chirality_catalog_paper_v143.pdf`
- Convex `papers:upsert` flips `sitePdfPath` → `/papers/chirality_catalog_paper_v143.pdf`
- Convex `paperVersions:bump` records the bump with `texCommit: WIP`

**Houston-external-review readiness**: P4 has now passed two consecutive direct-vendor R-rounds with **zero VERIFIED BLOCKERs**. The Perplexity confabulation catch demonstrates that the .bib metadata audit done in earlier revisions is correct against ground truth. Recommend Houston external pass next.
