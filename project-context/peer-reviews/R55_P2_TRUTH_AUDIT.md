# R55 P2 — Truth Audit (convergence-confirmation)

**Paper:** P2 — Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx
Sensitivity Recast with a MegaMapper Outlook
**Source:** `research/focused_paper_source_integration/02_full_draft.tex`
**Round:** R55 (post R52/R53/R54 + EXT21/22)
**Date:** 2026-06-26
**PDF:** `/tmp/R55_P2/02_full_draft.pdf` md5=6420ec92 (pre-fix) / recompiled post-fix, 28 pp, 0 undef
**Reviewers:** OpenAI gpt-5 (high effort, pass-2 self-critique) OK; Gemini 2.5 Pro OK;
Grok 4.3 (rasterized) OK; Perplexity quota-failed (401); no Anthropic leg. + own Opus read.

---

## NET VERDICT: CONVERGED — 0 BLOCKER / 0 genuine MAJOR

Independent Opus arithmetic re-derivation reproduced every headline number:
- Template-corrected baseline: 4.375 × r / 0.7, r ∈ [0.829,0.876] → **5.18–5.47σ** ✓ (paper: 5.2–5.5σ)
- GR-only floor: 4.375 × 0.84 / √(0.49+1.0) = 3.675/1.221 = **3.01σ** ✓
- bφ30%+GR1.0: 3.675/√(0.81+1.0) = 3.675/1.345 = **2.73σ** ✓
- bφ50%+GR1.0: 3.675/√2 = 3.675/1.414 = **2.60σ** ✓
- bφ30%: 3.675/0.9 = 4.08σ ✓; bφ50%: 3.675/1.0 = 3.68σ ✓; GR0.5: 3.675/0.860 = 4.27σ ✓
- Null-space 16th-pctile floor: 4.375×0.70/0.7 = 4.375 → **4.4σ** ✓
- Planck PR4 recast: −0.1±5.0 / 0.876 → ±5.7; |−4.375+0.1|/5.71 = **0.75σ** ✓; 0.02σ from zero ✓
- τ_NL (SY): (36/25)(35/8)² = **27.56** ✓
- |fnl|/|fnl_inf| = 4.375/0.015 ≈ **292 ≈ 290** ✓
- Bayes: δ/broad σ_eff=0.7 → 17.1; rebooked σ_eff=0.833 → 14.4 ✓

All internally consistent. Paper is a declared **sensitivity recast** (adopts Heinrich σ=0.7
rather than recomputing the Fisher) — explicitly stated; not flagged.

---

## VERIFIED DO-NOW closed (1, NIT-tier, no headline change)

**R55-1 (OpenAI P2-E7, pass-2) — CLOSED.** Sec III.A scale-dependent-bias prose (L735) read
"The explicit k² in the denominator of M" but Eq.(eq:Mkz) defines
M(k,z) = 2k²T(k)D(z)/(3Ω_m H0²) — k² sits in the **numerator** of M. The conclusion
Δb ∝ 1/M ∝ 1/k² is correct; only the explanatory mechanism phrase was backwards.
Fix: "Since Δb ∝ 1/M and M ∝ k² on ultra-large scales (where T(k)→1), the signal grows as
Δb ∝ 1/k² as k→0". Equation, all numbers, and headline unchanged.

---

## FALSIFIED / STALE / OPINION (no edit)

| Finding | Verdict | Evidence |
|---|---|---|
| Gemini P2-E1 (App A "18/25 ≠ 6/5", flawed derivation) | **FALSIFIED** | Paper chain (5/3)³(3/5)⁴·2 = (3/5)·2 = 6/5 is algebraically correct (L1125). Gemini used (5/3)² for B_ζ/B_Φ; its own "required fix" B_ζ=(−5/3)³B_Φ is exactly what the paper uses. Reviewer arithmetic error. |
| Gemini P2-m2 (missing pages 4/22) | **FALSIFIED** | PDF-render artifact; 28 pp present, compiles 0 undef. |
| OpenAI P2-E8 (weighting direction reversed) | **STALE** | R53-2 already grounded r_LSS<r_CMB in the numerical Fisher integration (null_space_analysis.py). Reviewer conflates per-k weight with squeezed-triangle-shape weight. |
| OpenAI P2-E6 (x3 squeezed relabel) | **OPINION/NIT** | Squeezed limit is permutation-symmetric (any one mode soft); r symmetric under relabel; no number affected. Notation, not error. |
| OpenAI P2-E9/M8 (IR-safety, dimensionless-grid bridge) | **OPINION** | Recast adopts Heinrich σ=0.7 by design; r is shape-cosine-stable (basis-independent floor r_cos>0.95). Methods-wish, not defect. |
| OpenAI P2-E1, Gemini/Grok DOI | **DOI-DEFERRED** | Zenodo DOI inserted at submission (per scope). |
| OpenAI P2-E2/M2, Grok P2-E1/M3 (abstract "realistic"/MegaMapper) | **OPINION/STALE** | Abstract already labels optimistic 5.2–5.5σ vs realistic 2.6–5σ; MegaMapper labeled proposed/unfunded/illustrative throughout. |
| OpenAI P2-E3 (anomaly 10–20%) | **STALE** | Explicit upper bound; headline does not rely on it. |
| OpenAI P2-E4/E5/M1/M3/M4/M5/M6/M7 | **OPINION** | Fuller-methods requests against a declared recast; r and budget already have released artifacts. |
| Grok P2-E2, Gemini P2-E2 (BF prior qualifier) | **FALSIFIED** | Abstract states "recommended σ_theory=1.0, broad [−15,+15]" → BF≈9–14 and "curvaton-natural [−5,+5] → BF≈4–7". Qualifier present. |
| Grok P2-M1, Gemini P2-M1 (assumption-(d) / ε-quadrature) | **STALE/OPINION** | Assumption (d) already flagged "weakest link"; Li stress-test branch in App A.2 already halves significances. ε-correction ≲0.4σ, labeled transparent scoping choice. |
| Grok P2-M2 (full r posterior) | **STALE** | 16–84 band 4.4–6.2σ already propagated (L679); per-sample artifact released. |
| Grok P2-N1, Gemini P2-m1 (date June 19 2026) | **OUT-OF-SCOPE** | Date intentional; it IS June 2026. Recurring false-positive ("submitted 2025" assumption wrong). |
| Grok P2-N2/NIT1/NIT2, Gemini P2-m3/N1, OpenAI P2-m1..m9/n1/n2 | **COSMETIC** | r/r_t/r_cos disambiguation already present; folded-row footnote present; notation/length preferences. |

---

## COMPILE / OVERFLOW
- 3× pdflatex + bibtex, post-fix: **0 undefined references/citations**.
- Overfull hboxes: 2, both sub-3pt math-mode (2.95pt @ tab:benchmarks line; 1.23pt @ commutator
  eq line) — pre-existing, within tolerance, not material. No column/figure overflow.

## CONVERGENCE STATEMENT
P2 is **CONVERGED**. After R52/R53/R54 + EXT21/22, R55's 3-vendor native-PDF round produced
zero BLOCKERs and zero genuine MAJORs. The single actioned item (R55-1) is a NIT-tier
source-verified prose fix with no equation/number/headline impact. All headline significances,
Bayes factors, and the Planck/DESI recast independently re-derive to the printed values. The
two highest-severity vendor "ESSENTIALs" (Gemini's appendix-algebra and missing-pages claims)
are reviewer-side errors, not paper defects. No further science work required.
