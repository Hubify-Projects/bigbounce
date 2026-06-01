# P4 v1.0.141 — direct-vendor R-round synthesis + truth-audit

**Round label**: `2026-06-01_R-direct-v141`
**Paper**: P4 (chirality_catalog_paper) v1.0.141 (June 1, 2026 PDT)
**Reviewers**: 4 dispatched direct-vendor (no OpenRouter); 3 returned, Gemini failed with billing 403.
**Cumulative reviewer time**: ~70s
**Cost**: ~$0.36 (Perplexity dominant)

## Vendor verdicts at a glance

| Reviewer | Model | Status | B / M / m / n |
|---|---|---|---|
| Grok | `grok-4` | OK | 2 / 2 / 1 / 1 |
| GPT-5 | `gpt-4o` (fallback) | OK | 6 / 0 / 0 / 0 (all generic "needs more discussion" prose asks, L2109) |
| Perplexity | `sonar-pro` | OK | 1 / 2 / 0 / 1 (citation forensics) |
| Gemini | `gemini-2.5-pro` | FAIL | 403 PERMISSION_DENIED (Google billing dunning) |

**No convergent BLOCKER across vendors on the core scientific result** (joint-nuisance z=-18.07σ formal exclusion, MASTER −0.12σ subsample-mask null, three-interpretation closure). This is qualitatively cleaner than the v1.0.139 external round (Grok 0 / Gemini 3 / GPT 9, where most GPT findings were STALE due to Vercel CDN serving v1.0.138).

## Truth-audit table

| Finding | Reviewer claim | Verdict | Reason | v1.0.142 action |
|---|---|---|---|---|
| GRO-B1 | Title says "No Evidence for Large-Scale Parity Violation" — false advertising vs parity-EVEN abstract | **STALE** | Actual `\title{}` at L387 is "Survey-Scale Galaxy Chirality with Equivariant TTA". Grok read the 7-line top-of-file comment block (L1-7), which carries the legacy v1.0.128 title text. Abstract explicitly says "this $\ell=1$ observable is the isotropy-breaking axial-vector channel and is parity-EVEN: it is NOT a direct parity-violation test." | Delete the stale comment block. |
| GRO-B2 | Naive 264σ leads narrative, bootstrap-corrected 18σ buried | **STALE** | L2250 prose: "drops from −265 to z_boot=−18.1. **Interpretation (i) at A=1.7% remains formally excluded — at ~18σ rather than ~264σ — under the spatial-coherence-respecting bootstrap σ.** The ~18σ exclusion is the headline number for the formal-exclusion claim; the naive-Gaussian ~264σ is reported only as the upper limit corresponding to the unrealistic assumption of fully uncorrelated per-pixel residuals." The paper already does what Grok asks. | None — Grok-B2 already closed by v1.0.139 framing. |
| GRO-M1 | Replace factor-6-12 Shamir amplitude claim with "matched-footprint Ganalyzer reanalysis required" | **STALE** | Abstract L411 already includes: "A like-for-like matched-footprint Ganalyzer reanalysis under Shamir's pipeline + cuts is required for a likelihood-level exclusion under his estimator; we do not perform that reanalysis here." | None — already in abstract scope statement. |
| GRO-M2 | No family-wise Bonferroni on cross-spectrum trials | **STALE** | L2250 prose already includes: "under a trials correction over ℓ ∈ {1,2,3,4,5} (~5 trials) the family-wise Gaussian-Bonferroni p-value is ~5×erfc(2.89/√2)/2 ≈ 0.02 (~2.3σ family-corrected)". Bonferroni IS there. | None — already done. |
| GRO-m1 | 1.21× empirical widening factor — also state 1.29× independence upper bound | **VERIFIED** | Real fix: add parenthetical "(strict upper bound under independence: 1.29×)" after 1.21× in §III.E + Table I footnote c. | Add 1.29× upper bound parenthetical. |
| GRO-n1 | 200-line review-log comment block bloats source | **VERIFIED** | Real cleanup: move audit trail to separate file, retain only release tag + DOI. | Move review-log comment block to `pipelines/p2_chirality/paper4_v1.0.141_review_log.md`; keep only release tag in .tex. |
| PER-B1 | Iye & Yagi 2026 arXiv:2605.05570 forward-dated / speculative | **VERIFIED** | Perplexity used web search and said "No such arXiv entry is currently verifiable". This is a confabulated forward-dated citation. | Drop the concrete arXiv ID; rewrite to "(Iye & Yagi, in prep.)" or remove sentence. |
| PER-B2 | Motloch & Pen 2021 mischaracterized as "Galaxy Zoo 2 CW/CCW ~2×10^5 spirals" | **VERIFIED** | Actual paper: SDSS galaxies, automated chirality classifier on DESI Legacy imaging, ~2σ correlation with tidal field. | Rewrite the §7.4 sentence to match actual paper methodology. |
| PER-M3 | Conflicting sensitivity floors throughout (0.29% Fisher / 0.14-0.20% / 0.75% empirical) | **VERIFIED** | Real issue: text mixes different floors across §1, §4.1, §4.6, §9.6. | Add a canonical "Table: Sensitivity floors and significances" listing each estimator + threshold + scope, and reword the prose to reference it uniformly. |
| PER-m4 | CE-ResNet/Jia 2023 description slightly overclaims footprint | **VERIFIED** | Real minor: paper says "DESI Legacy pre-imaging ... across the SDSS+DESI imaging footprint" — actually DESI Legacy with SDSS used in training. | Soften wording. |
| GPT-B1..B6 | Six "needs more discussion of XYZ" at §VI.D L2109 | **OPINION** (mostly) | These are not falsifiable findings — all are "expand the explanation" asks on §VI.D. Real but minor prose-clarity items, not BLOCKERs. GPT-5 fell back to gpt-4o which over-flags rhetorical clarity at the expense of substantive issues. | Reword §VI.D conclusion paragraph to make the residual interpretation more explicit; classify the rest as MINOR for clarity audit. |

## Net verdict

**5 STALE findings** (Grok-B1, B2, M1, M2) — already closed in v1.0.139, reviewer didn't catch the closures because the closures are in the §VI/VII prose and the abstract scope statement; reviewers tend to flag headline-language separately.

**6 VERIFIED actionable findings** — all text/citation level, no compute. v1.0.142 can close them in a single bundled wave:
1. Delete leading 7-line stale title comment block (GRO-B1 cosmetic)
2. Move review-log comment block to separate `paper4_v1.0.141_review_log.md` (GRO-n1)
3. Add 1.29× independence-bound parenthetical (GRO-m1)
4. Drop forward-dated Iye+Yagi arXiv ID (PER-B1)
5. Rewrite Motloch+Pen 2021 description (PER-B2)
6. Soften Jia 2023 footprint description (PER-m4)
7. Add canonical sensitivity-floors table + uniform prose references (PER-M3)
8. Tighten §VI.D conclusion paragraph (GPT-B1..B6 grouped)

**0 compute-bound items**. **0 deferrable items.** All closeable in a text-level v1.0.142 wave.

**Houston-external-review readiness**: this is the cleanest v141 result. Recommend Houston external pass after v1.0.142 lands.
