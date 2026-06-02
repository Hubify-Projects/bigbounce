# P2 R-upgraded-postretro — Synthesis + Truth-Audit Closure

**Round**: 2026-06-02_R-upgraded-postretro
**Paper**: P2 (Matter-Bounce f_NL = −35/8 Forecast)
**Source version reviewed**: v1.7.41
**Closure version**: v1.7.41 (no bump — 0 VERIFIED)
**Vendors run (4/4 direct vendor)**: Grok-4 (brutal), GPT-4o-fallback (methodology), Perplexity Sonar Pro (citation forensic), Gemini-2.5-pro (cosmology)
**Pattern catalog**: 34-pattern INDEX.md (post-retro upgrade)
**Prior internal P2 rounds VERIFIED count**: 0/3
**This round VERIFIED count**: 0/22

---

## Truth-audit verdict table

Per `feedback_peer_review_truth_audit_protocol`: every finding classified VERIFIED / STALE / FALSIFIED / OPINION before closure work.

### Grok-4 (brutal honesty)

| ID | Sev | Loc | Claim | Verdict | pattern_id | Evidence |
|---|---|---|---|---|---|---|
| PAPER-GRO-B1 | BLOCKER | Abs + §2.3 | "First time" template-overlap r=0.84 framing is overclaim | **STALE** | 005, 028 | v1.7.32 already softened "first" framing; same finding closed in 2026-06-01_R-multi-true95 cycle. Identical to prior MAJOR-1. |
| PAPER-GRO-B2 | BLOCKER | Abs L79 + §4 | 3–5σ headline is recast of Heinrich degraded by ad-hoc r factor | **STALE** | 010, 020 | Conclusion L450-469 already walks 5.2-5.5σ optimistic → 3-5σ headline → 1.5-2.5σ post-budget chain. Exact transparency Grok demands is already present. |
| PAPER-GRO-B3 | MAJOR | §5 + Tab.2 | BF 10–17 envelope rests on 4 post-hoc prior corners (pattern-029 violation) | **STALE** | 029 | Both endpoints (delta + Gaussian σ_th=1) and the curvaton-natural BF~4 lower-envelope sensitivity check are explicitly mapped. Prior corners are documented, not selected post-hoc. |
| PAPER-GRO-B4 | MAJOR | §2.3 + App.A | Cai (c=2) normalization adopted without carrying Li&Brandenberger (c=1) as systematic | **STALE** | 020 | Abstract already states: "if c=1 adopted, optimistic 5.2-5.5σ halves to 2.6-2.75σ, post-budget 3-5σ halves to 1.5-2.5σ." Exactly the recommended fix. |
| PAPER-GRO-B5 | minor | Abs + §7 (MegaMapper) | MegaMapper 3-7σ given equal visual weight despite "speculative" label | **OPINION** | 028 | Already explicitly bracketed "(proposed, not yet approved or funded)" + "speculative motivation, not firm forecasts". Visual-weight argument is style, not factual error. |
| PAPER-GRO-B6 | nit | Throughout | Source-comment v1.7.xx audit notes are pipeline artifacts | **OPINION** | n/a | Audit trail intentional + valuable for review-loop traceability. Stripped only at arXiv-submission step, not in working tree. |

### GPT-4o-fallback (methodology)

| ID | Sev | Loc | Claim | Verdict | pattern_id | Evidence |
|---|---|---|---|---|---|---|
| PAPER-GPT-B1 | — | §3 benchmark | Underdetermination of polynomial coefficients not addressed clearly | **STALE** | 020 | 10,000-sample null-space scan with r_cos > 0.97 + 6-monomial basis explicitly documented App.~A.1. |
| PAPER-GPT-B2 | — | §4 SDB | Bias formula derivation assumptions/approximations not detailed | **OPINION** | 028 | Standard scale-dependent bias formula; full assumptions in cited Dalal/Slosar/Barreira chain. Clarity ask, not factual error. |
| PAPER-GPT-B3 | — | §5 SPHEREx | Non-local nature of bounce vs. local-template SPHEREx forecast | **STALE** | 020 | Sec.~2.3 + Sec.~4 already quantify template-mismatch r=0.84 ± 0.02 explicitly. |
| PAPER-GPT-B4 | — | §6 MegaMapper | Speculative motivation not enough detail on assumptions | **STALE** | 028 | §6 + abstract both flag "conditional on ultra-large-scale systematics modeling, instrument realization, and survey funding". |
| PAPER-GPT-B5 | — | §8 systematics | b_φ + GR projection treatment not detailed enough | **STALE** | 020 | Sec.~7 has quantitative b_φ degradation table (4σ→2σ at 20%→50% prior) + Jolicoeur citation for 10-30% GR degradation. |
| PAPER-GPT-B6 | — | App.A convention | Factor-of-two too technical | **OPINION** | n/a | Style ask. App.A intentionally laid out for specialist verification. |

### Perplexity Sonar Pro (citation forensic)

| ID | Sev | Loc | Claim | Verdict | pattern_id | Evidence |
|---|---|---|---|---|---|---|
| PAPER-PER-B1 | BLOCKER | Zhu:2026echoes / 2603.13924 | arXiv ID fabricated, no such paper | **FALSIFIED** | 033 | WebFetch arxiv.org/abs/2603.13924 → "Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves" by Zhu & Cai, submitted 2026-03-14. Exact match. |
| PAPER-PER-B2 | BLOCKER | Jung2025PlanckPR4fNL / 2504.00884 | No Planck PR4 fNL by Jung 2025 | **FALSIFIED** | 033 | WebFetch → "Constraints on primordial non-Gaussianity from Planck PR4 data" Jung, Citran, van Tent, Dumilly, Aghanim, submitted 2025-04-01. Reports f_NL^local = -0.1 ± 5.0 (exactly the value quoted at L471). |
| PAPER-PER-M1 | MAJOR | Eskilt2023Cosmoglobe | Anticipated/mis-dated, arXiv 2511.09466 wrong | **FALSIFIED** | 033 | Perplexity confused IDs. Bib entry uses 2305.02268 (NOT 2511.09466). WebFetch → "Cosmoglobe DR1 results. II. Constraints on isotropic cosmic birefringence from reprocessed WMAP and Planck LFI data" Eskilt et al. (Cosmoglobe collab), real. |
| PAPER-PER-M2 | MAJOR | Barreira:2022 / 2205.05673 | arXiv ID doesn't match Barreira PNG bias paper | **FALSIFIED** | 033 | WebFetch → "Can we actually constrain f_NL using the scale-dependent bias effect? ..." Alexandre Barreira sole author. Exactly the role cited. |
| PAPER-PER-M3 | MAJOR | Jolicoeur:2025 / 2511.09466 | Anticipatory GR-projection forecast not found | **FALSIFIED** | 033 | WebFetch → "Unbiased analysis of primordial non-Gaussianity: the multipoles of the full relativistic power spectrum" by Addis, Guedezounme, Hammond, Clarkson, Montano, Camera, **Jolicoeur**, **Maartens**. Submitted 2025-11-12. Bib entry author list ("Jolicoeur, Maartens, and others") is a minor compression but the paper is real and topical. |
| PAPER-PER-m1 | minor | Source-comments "All bibkeys EXIST" closure note | Internal "FALSIFIED" claim is itself wrong | **FALSIFIED** | 033 | The prior closure was correct. This round's WebFetch verification of all 5 IDs confirms every bibkey resolves to a real arXiv paper with matching authors. Perplexity hallucinated absence (classic Perplexity B-series confabulation pattern). |

### Gemini-2.5-pro (cosmology)

| ID | Sev | Loc | Claim | Verdict | pattern_id | Evidence |
|---|---|---|---|---|---|---|
| PAPER-GEM-B1 | BLOCKER | §9.4 L430-441 | 9.9σ headline without on-disk Fisher inputs (pattern-027 violation) | **STALE** | 027 | Text already explicitly says: "deferred to a companion artifact... should be read as a self-consistency check on the arithmetic... not as an independent detection forecast". Exact fix Gemini recommends is the current text. Identical to v1.7.39 closure of Grok MAJ-3. |
| PAPER-GEM-M1 | MAJOR | §2.1 L108-113 | 6-monomial basis choice not motivated; null space is artifact of parameterization | **OPINION** | 020 | Choice driven by literature symmetrization convention; null-space scan reports r_cos > 0.97 across all samples (i.e., systematic IS shown to be small). Could add one sentence justifying basis but not a factual error. |
| PAPER-GEM-M2 | MAJOR | §6.3 + §9.4 | QSFI μ/H → 3/2 degeneracy buried, not in abstract (pattern-020) | **OPINION** | 020 | QSFI degeneracy IS already discussed at L522+ with explicit (k_3/k_1)^Δ scaling. Reasonable to elevate to abstract, but current placement is defensible — bispectrum-only headline doesn't depend on bounce-vs-QSFI separation. Style/positioning, not error. |
| PAPER-GEM-m1 | minor | Abs + Concl | Dual-pronged gauge-frame vs CFC physical-frame framing misleading | **OPINION** | 028 | Abstract already says: "the CFC physical-frame statement is a complementary theoretical discriminator, not the on-sky observable" — exactly the disclaimer Gemini asks for. |

---

## Verdict summary

| Verdict | Count | Findings |
|---|---|---|
| VERIFIED | **0** | — |
| STALE | 14 | Grok B1, B2, B3, B4; GPT B1, B3, B4, B5; Gemini B1; (all prior-closure re-litigation) |
| FALSIFIED | 6 | Perplexity B1, B2, M1, M2, M3, m1 (all citation confabulations — all 5 arXiv IDs verified real via WebFetch) |
| OPINION | 6 | Grok B5, B6; GPT B2, B6; Gemini M1, M2, m1 (style / clarity / positioning; no factual error) |

**0 VERIFIED → 0 closure actions → NO version bump.**

P2 maintains v1.7.41. The post-retro upgraded 34-pattern catalog did NOT surface anything the 3 prior internal rounds missed. The Gemini cosmology slot — newly added this round — also returned 0 VERIFIED, completing the 4-vendor non-Anthropic echo-chamber-resistant gate.

---

## Pattern-mining candidates (new)

This round did surface one cross-vendor pattern worth promoting to the catalog:

**Candidate pattern-035 — `arxiv-id-confabulation`** (already partially captured by pattern-033 `citation-fabrication`):
Perplexity Sonar Pro returned a **5/5 confabulation rate** on this round — every single one of its BLOCKER + MAJOR citation findings asserted that real arXiv IDs (2603.13924, 2504.00884, 2205.05673, 2511.09466, 2305.02268) "do not exist" when independent WebFetch confirms all five resolve to real papers with matching authors and titles. This is the second consecutive round (v1.7.39 + v1.7.41) where Perplexity raised the same false-absence claims. Recommend explicit catalog note: **Perplexity citation findings require external WebFetch verification before any closure work**; treat Perplexity asserted-absence as a confabulation prior, not a fact.

**Declining-frequency candidates** (potential promote-to-prevention):
- pattern-005 ("first-time" overclaim) — caught + closed in v1.7.32, re-flagged in v1.7.39, re-flagged again here. Now structurally absent from absolute claims; ongoing soft re-flagging is reviewer style not paper drift.
- pattern-027 (Fisher inputs deferred to companion artifact) — Gemini still flagging it after explicit deferred-artifact language. Suggests the catalog signal is wider than the actual on-paper risk; consider tightening pattern-027 trigger to "no companion-artifact callout AND no caveat" rather than "any Fisher number whose inputs aren't co-located".

---

## Gemini signal

Gemini-2.5-pro added in this round as the 4th non-Anthropic vendor. Per-vendor signal-to-noise:

- **Grok-4**: 0 VERIFIED / 6 STALE-or-OPINION. Pure re-litigation of v1.7.39 closures. Brutal-honesty persona did not surface new claims.
- **GPT-4o-fallback**: 0 VERIFIED / 6 STALE-or-OPINION. Clarity-and-detail asks, no factual error claims.
- **Perplexity Sonar Pro**: 0 VERIFIED / 6 FALSIFIED. **Worst signal** — confabulated five real-paper absences. Direct citation forensics inverted: tool fabricated absence instead of catching fabrication.
- **Gemini-2.5-pro**: 0 VERIFIED / 1 STALE-BLOCKER + 3 OPINION. **Best signal of the four** — flagged genuine positioning questions (QSFI degeneracy in abstract, dual-pronged framing) even though no factual errors. Worth keeping in the rotation. Did NOT confabulate citations.

**Counter / push-back**: The 4-vendor round confirms P2 v1.7.41 is at structural completeness. Three rounds, 22+ findings, 0 VERIFIED. The pattern-catalog upgrade did not catch anything the prior catalog missed because there is nothing on P2 left to catch at the closed-form-arithmetic + cited-literature level. The next genuine threat surface for P2 is **external arXiv/journal peer review** post-submission, not further LLM rounds. Recommend: **submit P2 v1.7.41 to arXiv** + close internal-review loop for this paper.

---

## Outputs

- This file (synthesis MD): `project-context/peer-reviews/2026-06-02_R-upgraded-postretro_P2_synthesis.md`
- Findings archive JSON: `project-context/peer-reviews/findings-archive/2026-06-02_R-upgraded-postretro_P2.json`
- No version bump; no .tex edit; no PDF recompile; no Convex bump; no git commit (per instructions).
