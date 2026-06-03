# P5 R-upgraded-round7 synthesis (2026-06-02)

**Input version**: v0.1.42-2026-06-02
**Output version**: v0.1.43-2026-06-02 (BUMP — 2 VERIFIED real-action closures)
**Vendors**: Gemini-2.5-Pro (cosmology), GPT-4o fallback (methodology), Grok-4 (brutal), Perplexity Sonar Pro (citations)
**Counter going OUT**: counter RESET (2 VERIFIED real-action closures → not a clean round; not a 3/3 EXIT)
**Gemini convergence**: STILL HELD on P5 (R5 + R6 + R7 — zero VERIFIED Gemini findings; all 5 Gemini findings this round are STALE/OPINION). Convergent silence streak from Gemini now spans 3 consecutive rounds.

## Per-finding truth-audit

| Finding | Vendor | Sev | Verdict | Action |
|---|---|---|---|---|
| GEM-B1 (toy EFT parity-even) | Gemini | BLOCKER | STALE / partially-WRONG | No change — gauge-invariance + rotational-invariance caveats (v0.1.41) already disclaim operator as schematic / non-covariant; Gemini's pseudoscalar argument itself has an ALP-vs-scalar sign ambiguity. |
| GEM-B2 (monopole subtraction methodology) | Gemini | BLOCKER | STALE | Paper already reports bright/dark separately and discusses 3.4σ flip in §VI.A. Monopole is a benchmark, not a hidden assumption. |
| GEM-M1 (V-Web reliability) | Gemini | MAJOR | STALE | §X.B + §VI.A already warn on V-Web/T-Web volume-fraction discrepancy. |
| GEM-M2 (gauge caveat extension to V-Web) | Gemini | MAJOR | OPINION | Polish wording. |
| GEM-M3 (RSD eigenvalue re-ordering) | Gemini | MAJOR | OPINION | One-sentence polish; not load-bearing. |
| GPT-B1 (abstract significance) | GPT | BLOCKER | FALSIFIED | Abstract already quantifies every σ + Bonferroni thresholds + max-stat MC. |
| GPT-B2 (Bonferroni vs FDR) | GPT | BLOCKER | STALE | Closed v0.1.36 — empirical max-stat MC is primary; Bonferroni is secondary benchmark. |
| GPT-M1/M2/M3/min1 | GPT | MAJOR/minor | OPINION/STALE | All previously addressed; phrasing nits. |
| GRO-B1 (forking paths / DESIVAST primary post-hoc) | Grok | BLOCKER | OPINION/STALE | Houston-mandated structural framing per v0.1.34+. Paper is transparent that no pre-registration existed and multiplicity is reported. |
| GRO-B2 (DESIVAST not independent dataset) | Grok | BLOCKER | STALE | Paper explicitly states "methodologically correlated by construction because they reuse the same matched-spiral subsample" in abstract. No independence claim made. |
| GRO-M1 (V-Web×target non-independence) | Grok | MAJOR | OPINION | Paper already attributes sign flip to BGS-selection-function-conditioned imaging-leg systematics. |
| GRO-M2 (delete Appendix A) | Grok | MAJOR | STALE | Houston rejected per v0.1.34. |
| GRO-m1/n1 (title length / changelog comments) | Grok | minor/nit | OPINION | Stylistic. |
| **PER-B1 (DESIVAST author order)** | **Perplexity** | **minor** | **VERIFIED** | **CLOSED.** WebFetch arXiv:2411.00148 confirms order Rincón / BenZvi / Douglass. Bib reordered (was Rincón / Douglass / BenZvi). |
| **PER-M1 (T-Web tracer-mix range)** | **Perplexity** | **MAJOR** | **VERIFIED** | **CLOSED.** §X.B rewritten to flag T-Web fractions as tracer-dependent, quote BGS explicitly, and weaken "strong concordance" → "approximate concordance". |
| PER-m1/n1/n2/n3 | Perplexity | minor/nit | OPINION/polish | Phrasing nits. |

## Closures (this round)

1. **PER-B1**: DESIVAST2025 bibitem author order corrected (Rincón, BenZvi, Douglass) — bib line 2450.
2. **PER-M1**: §X.B T-Web paragraph rewritten — tracer mix explicit, BGS quoted, concordance language weakened (lines ~1915-1944).

## Recompile + mirror

- 21 pp / 963,548 bytes / 0 undef refs / 0 undef cites / md5 `bc95a1199aec0bb741f925107ec68a11`.
- Mirrored byte-identical to `public/papers/`, `site/public/papers/`, `site/out/papers/`.

## Counter / exit

- R7 returned 2 VERIFIED real-action findings → not a clean round → counter RESET (was 2/3, now 0/3).
- Not the 3/3 EXIT yet. Next cycle (R8) target: if 4-vendor returns 0 VERIFIED on v0.1.43, counter → 1/3.
- Gemini convergence streak intact (R5/R6/R7 — zero VERIFIED). Grok and GPT continue to recycle FALSIFIED/STALE BLOCKERs; Perplexity remains the only vendor producing real bib/citation closures.
