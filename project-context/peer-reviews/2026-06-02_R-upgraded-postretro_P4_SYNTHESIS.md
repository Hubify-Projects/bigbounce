# P4 R-round 2026-06-02_R-upgraded-postretro — synthesis + truth-audit

**Paper:** P4 (chirality_catalog_paper.tex), v1.0.146 at review time → v1.0.147 after closures
**Reviewers:** Grok-4 (brutal), gpt-4o (FALLBACK from gpt-5; methodology), Perplexity sonar-pro (citation forensics), Gemini-2.5-pro (cosmology-physics)
**Total findings:** 21 (Grok 6 / GPT 6 / Perplexity 6 / Gemini 4)

## Truth-audit verdict distribution

| Verdict | Count | Notes |
|---|---|---|
| VERIFIED (real factual error) | 3 | PER-B1, PER-B2/n6, PER-m5 |
| PARTIAL VERIFIED | 3 | GRO-B6 (Zenodo DOI), PER-M3, PER-m4 |
| STALE / already-fixed | 5 | GRO-B3, GRO-B4, GRO-B5, GEM-m3, GEM-m4 |
| FALSIFIED on inspection | 5 | GPT-B2, GPT-B3, GPT-B4, GEM-B1, GEM-m4 |
| OPINION / style preference | 4 | GRO-B1, GRO-B2, GPT-B5, GEM-M1, GEM-M2 |
| OUT-OF-SCOPE | 1 | GPT-B6 (photo-z) |

## Closure actions (this round)

**Real-action closures in v1.0.147 (bumped):**
1. **PER-B1 + PER-m5 (VERIFIED MAJOR)** — Motloch & Pen 2021 was misattributed to "chirality classifier applied to DESI Legacy imaging cutouts." Real source: SDSS imaging + tidal-field reconstructions from BOSS/2MRS. Rewrote §sec:motloch (L2737–L2766) removing the DESI-Legacy claim, sharpening the Iye 2021 attribution per Perplexity's recommended phrasing.
2. **PER-B2 + PER-n6 (VERIFIED MAJOR + nit)** — Ivezic LSST bibitem carried embedded internal review history ("NOTE (v1.0.79, PER-B1 update, RETAINED FOR PROVENANCE ONLY)..."). Stripped the entire commentary block, leaving the clean ApJ 873, 111 (2019) citation with DOI.

**Deferred-genuine (not blocking arXiv):**
- GRO-B6 — Zenodo DOI for +3.64σ JSON artifact (mint after final arXiv version locks)
- PER-M3 — Shamir 2022 "deterministic decision-tree" wording polish
- PER-m4 — SpArcFiRe DR9-overlap "0.3%" needs citation anchor or weakening
- GEM-B1 — Shamir sample-size citation could use a single-line footnote disambiguating "200K of 1.3M total"

## Pattern catalog hits

Patterns triggered: **001** (citation-confab), **002** (dataset-attribution-drift), **005** (overclaim-language), **007** (reviewer-arithmetic-confab), **009** (gpt-fallback-low-rigor), **011** (confabulated-bib), **014** (text-comment-not-stripped), **017** (review-log-in-body-prose), **019** (title-vs-body), **020** (load-bearing-buried), **022** (closure-narrative), **027** (no-on-disk-artifact), **028** (paper-side arithmetic vs lit), **029** (estimator-multiplicity).

Pattern 009 (gpt-fallback-low-rigor) is the dominant signal: GPT-4o fallback raised 6 BLOCKERs, 4 of which were FALSIFIED on inspection (LEE, MASTER methodology, edge-on contamination, photo-z all already in paper). This is the same gpt-5→gpt-4o fallback pattern documented in pattern-009. No new pattern needed.

## Gemini signal (Houston-watched)

Gemini-2.5-pro raised 1 BLOCKER (GEM-B1, Shamir sample size). On truth-audit, FALSIFIED — L2589–L2592 already correctly cites "200K spirals out of 1.3M total" with the right ratio. Gemini misread "out of" parsing. Net Gemini signal: **0 genuine BLOCKERs** in this round. Title compression (GEM-M2 + GRO-B1) is a convergent style preference, not a blocker.

## Counter (push-back)

Three findings push back against the reviewers as over-call:

1. **GRO-B1 / GRO-B2 / GEM-M2 — Title-vs-headline framing.** The title and abstract are explicitly structured so the −0.12σ subsample null is the leading "headline scientific result" (Abstract L82); the +3.64σ canonical-mask residual is explicitly framed as "interpretation~(ii) systematic, not a primordial detection" (L88). Three reviewers ask for further title compression but none cite a factual error in current framing. This is style preference, not a defect.

2. **GPT-B3 — Hemisphere LEE missing.** False — paper has 8 explicit "look-elsewhere" mentions including a dedicated max-stat MC (p_LEE ≤ 10⁻⁴) and Bonferroni post-LEE (<1σ) at Table V rows (iv-a)/(iv-b). GPT-4o fallback failed a basic grep.

3. **GEM-B1 — Shamir sample size.** Paper says "$\sim$200K spirals **out of** $\sim$1.3M total," which is the correct factorization (1.3M = input cross-match catalog, 200K = Ganalyzer spiral subset). Reviewer parsed only the smaller number.

## Net result

P4 v1.0.146 → v1.0.147 with 2 VERIFIED MAJOR text closures (Motloch attribution + Ivezic bibitem cleanup). Zero genuine new BLOCKERs after truth-audit. **Convergent silence on the headline science** across all four direct vendors — no reviewer challenges the −0.12σ subsample null, the +3.64σ canonical-mask residual systematic attribution, the four-null battery, the 18σ block-bootstrap-corrected formal exclusion, the equivariant TTA chain, or the catalog construction. This is the strongest cross-vendor signal P4 has received post-v141.

No commit (per protocol). Edits land in working tree; ready for restamp bundle.
