# R53 P1B — Truth Audit (convergence pass)

**Paper:** P1B — "Technical Verification Companion to the ECH Spin-Torsion Program"
**Source:** `arxiv/paper1b_mcmc_companion.tex` (v1B.0.76 base)
**PDF:** `/tmp/R53_P1B/paper1b_mcmc_companion.pdf` md5=9a4aa5f5, 21 pp.
**Vendor legs:** OpenAI gpt-5 (OK, calibrated), Gemini-2.5-pro (OK), Grok-4.3 (OK), Perplexity (FAIL — 401 quota). Plus Opus full-PDF read (Claude leg).
**Calibration:** standard. Patterns applied: 061 (in-text verdict), 062 (already-fixed), 063 (math = extraction-artifact until source-checked), 064 (per-Grok-reason audit).
**Net verdict:** MAJOR-REVISIONS verdicts from all 3 legs are NOT supported. 0 BLOCKER, 0 genuine MAJOR. One genuine MINOR found+closed (gpt-5 M3) + 2 polish closures. **P1B CONVERGED.**

---

## VERIFIED → CLOSED this round

| ID | Tier | Source | Old → New | File:line |
|----|------|--------|-----------|-----------|
| OVF-1 (own find) | MINOR (visual) | latex-audit: 92.2pt overfull hbox, visible column overflow | display eq with long `\text{}` parenthetical → parenthetical moved to lead-in prose; eq now short | `arxiv/paper1b_mcmc_companion.tex:2243-2245` |
| Gem-m2 | MINOR | β–α degeneracy disclaimer present in abstract but absent from §IV Scope note | added one sentence reiterating the β–α / foreground-free limitation, grounded verbatim in abstract content | `:1784` (§IV Scope note) |
| gpt5-M3 | MINOR | "anharmonic ≲5% for θ_i∼1" inconsistent with cited O(θ_i²/12)=1/12≈8.3% at θ_i=1 | "≲5% for θ_i∼1" → "≲8% at θ_i∼1 and ≲1% over the Ω_a≤0.01 spectator-safe subset (θ_i≲0.3)" | `:2472` |

All recompiled ×3: 0 undef refs/cites, **0 overfull hboxes**, 21 pp.

---

## FALSIFIED (math/extraction artifacts — pattern-063; NOT acted on)

- **gpt5-E1** (LiteBIRD "variance combination wrong / 0.7σ"): source L2641 = `\sqrt{0.03^2+0.094^2}` (correct); "0.032/0.0942" is pdftotext dropping the `^`. 0.072/0.0987=0.73 → 0.7σ. Paper correct.
- **gpt5-E2** (alleged factor-of-10 in m/H₀ lower bound): 10⁻³⁵/(1.44×10⁻³³)=6.94×10⁻³≈7×10⁻³ — **paper is correct**; gpt-5 itself computed 6.94×10⁻² (dropped a decade). Critical non-fix.
- **gpt5-M8** (per-realization SNR 5.2 "should be 5.9"): paper consistently uses |β̂|/σ_β (0.238/0.046=5.2; 0.237/0.029=8.1). gpt-5 misread β̂ as β_inj.
- **gpt5-m3** (add β_obs=5.97×10⁻³ rad): already in text L2387.
- **gpt5-m4** (Fig.4 caption has Galaxy-Zoo DOI): false — that DOI is in App A, not the caption.
- **gpt5-M9** (m≈3.9H₀ outside box unflagged): in-box equivalent (θ_i≈1.4, m≈3H₀) already given L2299; posterior-outside-box stated repeatedly.
- **Grok-E1/E4** (0.04σ c15 claim "unrecomputable / =0.32σ"): 0.04σ is c15(+0.0514±0.171) vs frozen(+0.058±0.179) → |Δ|/σ=0.04; Grok compared the wrong pair (the two frozen chains).
- **Grok-E2** (abstract overstates scope): abstract already says "not as evidence for or against ECH"; matches §III.
- **Grok-E3/E5** ("not directly comparable" missing / 0.34-vs-0.425 ratio): qualifier present at every juxtaposition; the "0.34" ratio is Grok's own invention.
- **Grok-M4/N3** (119,617 unrecoverable / 20%-vs-30% burn-in unreconciled): fn:sample_stratification reconciles both in full.
- **Grok-N1** ("June 20 2026 is a future date"): today is 2026-06-26; date is in the past. Model-clock artifact.
- **Grok-N2** ("canonical canonical-mask" duplication): `grep` finds no such string. Hallucination.
- **Gem-N3** (§IV "characterize." missing period): period present at L1811.
- **gpt5-E4** (Eq.1 "χ² dimensionally inconsistent → rename SSR"): deliberate disclosed choice (EXT7 Path A: matches script `np.sum((...)**2)`, "unweighted" stated ×3). Re-litigation.

## OPINION / TRULY-BLOCKED / already-disclosed (NOT acted on)

- gpt5-E3/M1/M7, Grok-M1 (DOI-pending, mixed Planck release, repo-internals, ≤12pp): pre-submission/Houston-design/scope choices; release-pairing already bounded at 0.04σ (c15). Joint-covariance SN refit (Gem-m1) = TRULY-BLOCKED (deferred follow-up, caveat (e)).
- gpt5-M2/M4/M5/M6, Gem-E1/M1/M2/m3 (estimator nomenclature, ℓ≤1024 number, burn-in consolidation, S8 recipe, w0wa "σ" notation, abstract forcefulness, restructure, claims-table format): all already substantially disclosed/caveated in body; tone/structure preferences, not defects.
- gpt5-m8 (H₀-marg ≲3% ignores z_osc): second-order; Ω_a∝H₀⁻² dominant. NIT.
- nits n1/n2/n4 (hyphenation, 0.28-vs-0.2825 rounding, χ² typeset): cosmetic; 3rd-sig-fig sensitivity already explained at L2283-2286.

**Note (per directive):** w0wa Table II overlap caveat + NaMaster scope (R52) re-verified — still correct, not re-opened.

**CONVERGENCE STATEMENT: P1B CONVERGED.** 0 BLOCKER / 0 genuine MAJOR; 3 MINOR closed (1 visual overflow, 2 prose); all vendor MAJOR-REVISIONS verdicts falsified or opinion-tier.
