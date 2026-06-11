# R29 P5 — TRUTH AUDIT
**Paper**: P5 v0.1.61 (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`)
**Date**: 2026-06-10
**Auditor**: in-session vs tex + JSON artifact cross-check
**Sources**: R29_P5_Claude_brutal.md, R29_P5_META_REVIEW.md, R29_P5_SYNTHESIS.md (+ Gemini/Grok/OpenAI/Perplexity legs)

---

## Verdict counts

| Severity | Consensus finding | Disposition |
|----------|-------------------|-------------|
| ESSENTIAL | E29-2 terminology half-sweep | FIXED — tex patched |
| ESSENTIAL | E29-3 abstract "confirmed" vs body "cannot partition" | FIXED — tex patched |
| MAJOR | M29-1 abstract drops "small effect" on Cramér's V=0.078 | FIXED — tex patched |
| MAJOR | M29-3 "≤0.01 SE" ~10× wrong for wall/cluster | FIXED — tex patched, true numbers stated |
| ESSENTIAL | Meta-E2 void volume fraction 0.1% vs 24.4% contradiction | OPINION — see below |
| ESSENTIAL | Meta-E1 HEALPix pixel count 297 vs 885 discrepancy | HOUSTON-DECISION |
| MAJOR | Meta-M1 Table VII resolved-cell heading includes Rs=25 rows | HOUSTON-DECISION |
| MAJOR | Meta-M3 row-level permutations break label/position equivalence for duplicate coadds | OPINION |
| MAJOR | Meta-M4 BGS-only randoms for mixed-program completeness rebuild | OPINION |
| MAJOR | Meta-M2 HEALPix Pearson p ignores spatial correlation | OPINION |
| ESSENTIAL | companion (4-reviewer consensus) — Paper IV unpublished dependency | OPINION — structural; cannot fix without re-submission strategy |

---

## Verified fixes applied to tex (PHASE 2 patches)

### E29-2 — Terminology sweep ("catalog-level" → "catalog-wide monopole offset")
**Claim**: EXT1 closure ledger said C1/F19/F21 was done; audit found 5 remaining `catalog-level` headline-equivalent instances.
**True remaining hits needing fix**: abstract line 267, body line 1077 (§density follow-up), line 1133 (multiplicity paragraph), line 2199 (sky-scan conclusion).
**Fixes applied**:
- Abstract: `the −5σ catalog-level signal` → `the −5σ catalog-wide monopole offset`
- Body §results_within_class_density: `The catalog-level cluster-class deviation` → `The catalog-wide-monopole-projected cluster-class deviation`
- Body multiplicity paragraph: `The catalog-level / −4.7σ cluster signal` → `The catalog-wide-monopole-projected / −4.7σ cluster signal`
- Body sky-scan conclusion: `catalog-level −5σ is not environment-driven` → `catalog-wide monopole offset is not environment-driven`
- Also: abstract "confirmed by a tracer-program decomposition showing the catalog-level −5σ is entirely driven" → "consistent with a tracer-program decomposition in which the catalog-wide monopole offset is dominated" (merged with E29-3 fix)
**Remaining legit uses**: Lines 1293 ("catalog-level bright-vs-dark difference"), 1844 ("carries the full catalog-level monopole signature"), 2092 ("~9.5σ catalog-level monopole reported in Paper IV") — these are not headline-equivalent and correctly refer to the broad monopole construct.

### E29-3 — Abstract overstates "confirmation" from program decomposition
**Claim**: Abstract said "this is confirmed by a tracer-program decomposition" but body §VI.A.d says data "cannot cleanly partition" the two interpretations.
**Fix applied**: Changed abstract to "consistent with a tracer-program decomposition in which the catalog-wide monopole offset is dominated by the BGS-bright sample" — removes "confirmed" claim, preserves the cannot-partition caveat already present at lines 298-302.

### M29-1 — Abstract drops "small effect" qualifier on Cramér's V=0.078
**Claim**: Body §VI.A.d (line 1274) correctly labels V=0.078 "small effect despite the enormous sample." Abstract presents same V naked next to log₁₀p≈−1069.
**Fix applied**: Added after V=0.078: "--- a small effect by conventional standards, with the χ² driven by sample size n=811,609 rather than effect magnitude ---"

### M29-3 — "≤0.01 SE" claim quantitatively wrong
**Verified SE shifts from `outputs/27_ext1_logistic_program_control.json`**:

| Class | M0 coef | M1 coef | M0 SE | Shift (SE units) |
|-------|---------|---------|-------|-----------------|
| void | −0.004607 | −0.003976 | 0.098467 | **0.0064** ✓ |
| wall | +0.022781 | +0.020276 | 0.024826 | **0.1009** ✗ (10× claim) |
| cluster | −0.005878 | −0.005370 | 0.004542 | **0.1118** ✗ (11× claim) |

The paper claimed "≤0.01 on their standard errors" — FALSE for wall and cluster. Joint Wald p shifts (0.43→0.52) still support the null; the error was transcription-level, not methodological.
**Fix applied**: Changed to "≤0.12 on their standard errors (void 0.006σ̂, wall 0.10σ̂, cluster 0.11σ̂; shifts computed as |β_{M1}−β_{M0}|/SE_{M0} from artifact JSON)."

---

## OPINION / HOUSTON-DECISION items (not patched)

### Meta-E2 — void volume fraction 0.1% vs 24.4% contradiction [OPINION — LIKELY FIXABLE]
Body §VI.A says "the small void volume fraction of ≈0.1% of in-footprint cells" but §IV.B gives cell-volume fractions {void 0.244, wall 0.413, filament 0.333, cluster 0.010}. These are different objects: 0.1% likely refers to the fraction of in-footprint *cells* occupied by DESIVAST VoidFinder holes (point-in-sphere membership on the 25.9 Mpc/h grid), not the V-Web tidal-classifier void class. The 24.4% is the V-Web void volume fraction. **This is a writing clarity issue, not an arithmetic error.** Fix: replace "≈0.1% of in-footprint cells" with "≈0.1% of in-footprint grid cells fall inside a DESIVAST VoidFinder hole (the V-Web void class occupies ≈24.4% of cell volume, §\ref{sec:vweb_algo})" — one sentence, no recompute. Recommend Houston approve the wording before patching.

### Meta-E1 — HEALPix pixel count 297 vs 885 discrepancy [HOUSTON-DECISION]
Body §VIII.E says "297 occupied pixels with median 14 maximal voids per occupied pixel" (NSIDE=16 interior voids). Fig. 8 caption says "885 occupied pixels, median 4 voids/pix." These almost certainly refer to different samples (interior-void subset vs all effective voids, or NSIDE=16 vs different nside, or different sky masks). Requires reading the actual figure-generation script to disambiguate. Cannot patch safely without verification.

### Meta-M1 — Table VII resolved-cell heading "Rs ≥ 25.9 Mpc/h" includes Rs=25 rows [HOUSTON-DECISION]
Grid cell is 25.9 Mpc/h; Rs=25 rows appear under "Resolved cells (Rs ≥ 25.9 Mpc/h)" heading. Either relax criterion to "Rs ≳ cell size" (consistent with body text using ≳) or move Rs=25 rows to unresolved block. Affects robustness narrative. Recommend Houston choose.

### Meta-M3 — row-level permutations and duplicate coadds [OPINION — RESEARCH DECISION]
Paper claims label-shuffle ≡ position-shuffle null. Meta-reviewer flags that ≈3.57% duplicate rows (28,973 extra rows from 812,793 total vs 783,820 unique TARGETIDs) break strict equivalence. The paper correctly notes the duplicate fraction and uses it consistently; the shuffle-equivalence claim needs a one-sentence clarification that permutations are label-conditioned (fixing total CW count). Not a methodological flaw — a sentence fix. Low risk; recommend fixing in next pass.

### Meta-M4 — BGS-randoms only for mixed-program completeness rebuild [OPINION — RESEARCH DECISION]
§IX.A uses 7.5×10^7 BGS BRIGHT clustering randoms to completeness-weight a mixed bright+dark sample. Strictly, dark-program spirals need dark-program randoms. Given dark fraction is ≈1.8% of the sample (14,482/782,710), the bias is likely small but unquantified. Recommend a one-sentence acknowledgment in §IX.A.

### Meta-M2 — spatial correlation in HEALPix Pearson tests [OPINION — RERUN NEEDED]
Pearson correlation r=+0.006 (p=0.88) between void-density-per-pixel and chirality-σ-per-pixel is computed assuming independent pixels. Meta-reviewer correctly identifies angular correlations violate i.i.d. assumption. A spatial permutation (rotation-based null) would be cleaner. This is a genuine methodological issue but not a verdict-changer given the near-zero r. Houston decision: add spatial-null permutation or flag as heuristic.

### companion finding (4-reviewer consensus) — Paper IV unpublished [STRUCTURAL]
All 4 consensus reviewers flag the entire analysis being load-bearing on unpublished Paper IV. This cannot be fixed within P5 tex without either (a) submitting P4+P5 as a co-submission pair or (b) making P5 fully self-contained by reproducing the monopole from the DESI DR1 data in P5 itself. Houston decision required on submission strategy.

---

## Remaining VERIFIED/PARTIAL findings not patched (MINOR/NIT, batched)

**Verified and real (recommend next-pass fix):**
- Gemini-M3: Table IV `σ_obs − σ_pred` sign errors (e.g. Q3: −3.94−(−2.07)=−1.87, table shows +1.87). Requires checking column definition — if absolute residual was intended, change header to |σ_obs − σ_pred|.
- Gemini-E1: Δf_CW sign: abstract states void=0.4964, non-void=0.4971, Δ=+0.0007 but 0.4964−0.4971=−0.0007. One number wrong.
- Gemini-E2: Table XII arithmetic errors in σ_vs_monopole column — requires recompute check against artifact.
- OpenAI-E1: Binomial formula rendering ambiguous: "1−0.05^{1/6}" typeset as "0.051/6" — add explicit parentheses.
- OpenAI-E5: Eq. (1) missing division notation for σ_pred formula — typeset as σ_pred = (Δf_CW)/(0.5/√N).
- M29-2: Cramér's V effect-size honesty for the catalog-wide monopole itself — add one parenthetical in §VI.A (no recompute).
- P5-m29-6: n=782,710 ≠ n=783,820 — add "(the 1,110-spiral BACKUP+OTHER subset is excluded)" in one half-sentence.
- Meta-M1 resolved-cell heading — see HOUSTON-DECISION above.
- Grok-P5-m2: Mollweide projection axis labels lack coordinate system and colorbar units.

**OPINION/low-priority (batch for pre-submission sweep):**
- Gemini-m1/OpenAI-M2/Grok-M1: abstract and paper length (30 pp for null result); recommend condensing, Houston decision.
- Perplexity-E2/OpenAI-E2: draft-status language in body ("earlier draft…withdrawn"); these are intentional transparency notes, Houston may keep or strip.
- OpenAI-M1/Perplexity-N1: "V-Web" vs "T-Web" nomenclature standardization.
- OpenAI-E3: Missing Zenodo DOI in Appendix B — cannot fabricate; generate and insert at submission time.
- Various MINOR σ-mixing, figure labeling, cross-reference, unit formatting NITs from all legs.
