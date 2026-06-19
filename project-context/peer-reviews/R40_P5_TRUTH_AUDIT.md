# R40 P5 — Truth Audit (final pre-arXiv)

**Paper:** P5 DESI spiral-chirality environmental dependence, v0.1.80
**Source:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (32 pp, 0 overfull, 0 undef)
**Lead:** truth-audit + synthesis (Opus)
**Date:** 2026-06-18 (America/Los_Angeles)
**Reviewers ingested:** OpenAI o3/gpt-5 (methodology), Gemini 2.5 Pro (cosmology), Grok 4.3 (brutal), Perplexity (citations — **FAILED**, 100KB limit, 0 findings), Claude Opus leg (MINOR, 2 verified findings)

Per the standing peer-review-truth-audit protocol, every finding is grounded against on-disk tex/scripts before a verdict. Reviewers see the rendered PDF without repo context and over-call on stale/mislabeled artifacts.

---

## Verdict table

| ID | Reviewer | Claim | On-disk verification | Verdict |
|----|----------|-------|----------------------|---------|
| **E1-h** | OpenAI | "χ[h⁻¹Mpc]=h·χ[Mpc] is wrong; divide-by-h (≈1246) is right" | tex L829–834 gives the correct dimensional derivation `D/(h⁻¹Mpc)=h·D[Mpc]`; multiply-by-h → χ(z=0.2)=570 h⁻¹Mpc is the convention used; divide-by-h (≈1246) is explicitly labeled "not used here" (L840–842). Repo block L24–30 already documents this auditor inversion. | **FALSIFIED** (auditor inverted the identity; paper is correct) |
| E2-paperIV | OpenAI/Gemini/Grok | Non-self-contained: leans on "Paper IV (in preparation)" for labels, monopole Δf_CW=−0.0026, σ_pred | Real cross-vendor convergence (3/4). tex imports labels + monopole from unpublished companion. Genuine standalone-reader concern, but **arXiv-blocked not tex-fixable** — resolves when Paper IV (P4) posts to arXiv; reference becomes a live ID. Self-contained summary of P4 method is a real DO-NOW add. | **VERIFIED-OPEN (program-level)** — not a v0.1.80 line edit; tracked for P4-arXiv linkage |
| E2-sign | Gemini | Tidal-tensor sign inconsistency (deformation vs tidal); "title-footnote convention" ambiguous | Title footnote L395 + algo L875–880 both consistently give Φ_k=−δ_k/k², T_ij=−k_i k_j Φ_k=+k_i k_j δ_k/k². Gemini's own derivation concludes "appears correct"; volume fractions standard. Residual ambiguity is the *old* ∂²Φ form at L426. | **MISLABELED** (presentation, not a sign error; one-line clarification optional) |
| M3-tableIV | Gemini | Table IV residual sign wrong; 1.87 should be −1.87 | tex L1390 column header is already `$|\sigma_{\rm obs}-\sigma_{\rm pred}|$` (abs value); 1.87=|−3.94−(−2.07)|. Abstract matches. | **STALE** (column already abs-valued) |
| m1-typo | Gemini | "0.01 ≤ x ≤ 4" — x should be z | tex L711/773/822 all read `$0.01 \le z \le 4$` / `\le 2.0`. No `x` variable exists. PDF-render misread. | **FALSIFIED** |
| m2-rowcount | Gemini | Abstract "16.36×10⁶" vs body "16,361,731" | Style choice (approx in abstract, exact in body); both traceable. | **OPINION** |
| E3-abstract | OpenAI/Grok | Abstract must flag Rs=10 under-resolution + 428 T-Web void-bin n + confirmatory pathway | Real polish. tex L1275 already disambiguates the n=428 vs 56,981 denominators in body; abstract caveat sentence is a defensible add. Not a correctness defect. | **OPINION (polish)** |
| M-length | OpenAI/Gemini/Grok | 32pp too long for a null; restructure DESIVAST-first | Editorial preference; convergent but non-blocking. PRD null methods papers of this length exist. | **OPINION** |
| M4/E7/M6 rounding | OpenAI | σ-from-half rows off ~0.03–0.06 from printed f at given n | Cosmetic display rounding (f to 4 dp); Claude-leg verified χ²=3.55 p=0.315 and ledgers exact. Carry one extra dp or recompute-from-displayed. | **OPINION (display)** |
| M7-symbol | OpenAI | Δf_CW overloaded (monopole offset vs env contrast) | Real notation-hygiene nit; distinct symbols (Δf_mono / Δf_env) would help. Non-blocking. | **OPINION (polish)** |
| N1-date | Gemini/Grok | "June 13, 2026" is a future date | tex L401 `\date{June 13, 2026}`; today 2026-06-18 → **past** date. Reviewers assumed 2025. v0.1.80 restamp updates it anyway. | **STALE** |
| N2-paths | Gemini/OpenAI | Raw `\artifact{}`/file paths in body | Intentional repro provenance via `\artifact{}` macro; PRD-acceptable as footnotes. | **OPINION** |
| AppA | Gemini | Remove speculative toy-EFT Appendix A | Author already brackets it with strong caveats; keep-or-cut is judgment, not error. | **OPINION** |
| **CL-A** | Claude leg | tex L809–810 nomenclature note inverted: "earlier preprint versions used ``T-Web''" is self-nullifying, contradicts title footnote L431–433 + changelog (earlier = **V-Web**) | Confirmed. L809–810 reads `used \`\`T-Web'' for the same implementation`; title footnote L431–433 says earlier versions used `\`\`V-Web''` loosely. The reminder negates its own point. | **VERIFIED-OPEN** |
| **CL-B** | Claude leg | tex L2900–2901 math subscripts `n_{\rm V\mbox{-}Web}=23/145` label the T-Web side "V-Web", contradicting adjacent prose "T-Web side" L2902 (pattern-059 residual; escapes naive grep via `\mbox{-}`) | Confirmed. L2900–2901 carry `n_{\rm V\mbox{-}Web}`; L2902–2903 prose reads "the T-Web side has essentially no void/wall population." | **VERIFIED-OPEN** |

Perplexity returned no findings (call failed). No unique citation findings to audit.

---

## Merged VERIFIED-OPEN (v0.1.80 line edits)

Two MINOR labeling-consistency fixes, both from the Claude leg, both confirmed against tex:

1. **`p5_desi_chirality.tex:809-810`** — change
   `earlier preprint versions used \`\`T-Web'' for the same implementation`
   → `earlier preprint versions used \`\`V-Web'' for the same implementation`
   (restores the intended meaning; matches title footnote L431–433 and the EXT10 V-Web→T-Web rename changelog).

2. **`p5_desi_chirality.tex:2900-2901`** — change both `n_{\rm V\mbox{-}Web}`
   → `n_{\rm T\mbox{-}Web}` (subscripts label the T-Web overlap side; pattern-059 residual hidden behind `\mbox{-}`).

**Program-level (not a v0.1.80 tex edit):** E2-paperIV — add a self-contained P4-method summary + live arXiv ID once P4 posts. Tracked for the P4→P5 arXiv-linkage gate, not blocking this restamp.

All ESSENTIAL/MAJOR severity calls from the four vendors are FALSIFIED, STALE, MISLABELED, or OPINION on grounding. No new BLOCKER/MAJOR correctness defect survives the audit. N3 novelty intact.
