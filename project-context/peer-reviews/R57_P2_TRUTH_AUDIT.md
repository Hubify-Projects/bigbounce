# R57 P2 — Truth Audit (hardened de-biased re-review)

**Round:** R57, hardened PRD/MNRAS bar (no severity-defaulting; self-favoring / unstated-assumption / internal-inconsistency = real finding, MINOR min, NOT OPINION; patterns 061–064 + calibration filter genuine false-positives only).
**Source:** `research/focused_paper_source_integration/02_full_draft.tex` (compiled `/tmp/R57_P2/02_full_draft.pdf`, md5 7df88149, 28 pp, 0 undef).
**Vendor coverage:** OpenAI gpt-5 (native PDF, high-effort, pass-2) + Grok 4.3 (rasterized PDF). Gemini fork-crashed the parallel dispatcher; Perplexity quota-failed. Backbone = own Opus read + full arithmetic re-derivation.
**Integrity-fix status:** abstract single-Heinrich-baseline restatement (v1.7.73) + R56 closures (E6/M3/M6/E8) VERIFIED INTACT — not re-opened.

## NET VERDICT: MAJOR REVISIONS (both vendors) → on audit, NO BLOCKER, NO genuine MAJOR. 3 verified MINOR (all internal-consistency/cross-ref) CLOSED.

## Own-Opus arithmetic re-derivation — ALL headline numbers reproduce
- SPHEREx optimistic 5.5σ = 4.375×0.876/0.7 = 5.47 ✓; 5.2σ = 4.375×0.84/0.7 = 5.25 ✓
- GR-only floor 3.0σ = 4.375×0.84/√(0.7²+1.0²) = 3.01 ✓
- All-combined 2.7σ = 3.675/1.35 ✓; 2.6σ = 3.675/1.41 ✓
- σ_eff table: √0.74=0.86, √1.49=1.22, √1.81=1.35, √2=1.41 ✓
- MegaMapper 7.4–7.7σ = 4.375×(0.84–0.88)/0.5 ✓
- Planck PR4 recast: 5.0/0.876=5.71; tension |−4.375+0.1|/5.71 = 0.75σ ✓
- BF four-corner grid 17/10/7/4; r=0.84 rebooking 14.4/9.2/6.2/4.0 ✓; abstract 9–14 ✓

## Vendor ESSENTIAL/MAJOR — verdicts (de-biased)
| ID | Verdict | Evidence |
|----|---------|----------|
| Grok E1 (5.2-5.5σ pre-systematic in abstract) | STALE | Abstract already labels 5.2-5.5σ "optimistic" and 2.6-5σ "realistic"; both stated. |
| Grok E2 (BF 9-14 prior-dependent, uncaveated) | STALE | Abstract+body label BF "illustrative … not definitive model-selection evidence" with exact prior. |
| Grok M1 (28pp too long) | OPINION | Length is editorial, not a defect. |
| Grok M2 (quadrature not joint Fisher) | STALE | Already "transparent scoping choice whose conservatism a full joint Fisher would need to confirm". |
| Grok M3 (not-directly-comparable labels) | STALE | Fig2/TblIV captions already carry the label. |
| Grok M4 (BF prior robustness) | STALE | Continuous hyperprior marginalization shown (L884, c9l script). |
| OpenAI E1 (DOI placeholder) | EXCLUDED | DOI item, skipped per round scope. |
| OpenAI E2/E6 (recast vs "forecast" language) | STALE | "sensitivity recast rather than independent cross-Fisher forecast" stated ×4 in abstract. |
| OpenAI E3/M2/m9 (r-weighting defs not in text) | KNOWN-MINOR (not load-bearing) | Same as R56 "SPHEREx-like weight not formula-defined"; headline r=0.84 bracketed by defined schemes. |
| OpenAI E4 (BF r→1 vs r=0.84 bookkeeping mix) | STALE | L939 bookkeeping paragraph + L905 reading guide explain both conventions. |
| OpenAI E5/E14/M1 (figure Fisher not described) | STALE | MegaMapper SDB curves already labeled illustrative; captions disclose. |
| OpenAI E7/m6 (inj-recovery ±0.01 from N=200) | NOT-A-VERIFIED-ERROR | ±0.01 plausibly SEM (s≈0.14); reproducibility-detail ask, not an internal inconsistency; not load-bearing. Skip (no source fix without rerun). |
| OpenAI E8 (ε-corr 0.42 vs 0.50σ) | **FALSIFIED** | Reviewer dropped the r=0.84 factor. Significance shift = Δf×r/σ = 0.35×0.84/0.7 = 0.42σ (TblIV header: sig = \|f\|×r/σ). R56-2 closure (0.42σ) CORRECT — NOT re-opened. |
| OpenAI E10 (abstract cross-check comparability) | OPINION/polish | Body has the qualifier; not load-bearing. |
| OpenAI E11 (Gaussian-prior BF convolution not explicit) | NOT-A-VERIFIED-ERROR | Numbers validated; analytic structure given. Reproducibility enhancement. Skip. |
| OpenAI M3/M5/M7/m5/m7/m8/nt* | OPINION/already-caveated/PDF-artifact | No source defect. |

## VERIFIED MINOR — CLOSED (3, source-edited; no headline/number change)
- **R57-1 (OpenAI P2-E9, bφ wording):** Sec VII.B said Heinrich "marginalize over b_φ … which fixes b_φ" — self-contradictory and clashing with Sec IV "treats b_φ with a fixed universality relation". Rewritten to "fix b_φ via the UMF relation … rather than marginalizing it", consistent across §IV/§VII.
- **R57-2 (OpenAI P2-E12, cross-ref):** §IV DBI deferral pointed the "joint (f_NL,n_fNL) subsection parenthetical" to \ref{sec:bayesian} (§VI); that subsection is in the Discussion (§IX.D, per paper's own L1107). Added `\label{sec:joint_running}` and retargeted; aux now resolves IX.D. ✓
- **R57-3 (OpenAI P2-E13, mis-citation):** TblIV caption attributed the "quadrature combination" definition to Eq projection (§5), which defines only the rebooking σ(f_bounce)=σ(f_local)/r. Caption split: rebooking→Eq projection, quadrature ⊕→§VII.

## Self-favoring check: NO NEW self-favoring item this round. (R56's lone ε-rounding 0.42σ remains correctly closed; OpenAI E8 attempt to reopen it FALSIFIED.)

## Recompile: ×3 incl bibtex, 0 undef, 0 reference warnings, 2 negligible overfull hboxes (2.95pt/1.23pt, unchanged by edits), 28 pp. Overflow audit clean.

## CONVERGENCE STATEMENT
P2 is CONVERGED under the hardened de-biased standard. Both native-PDF vendors nominally returned MAJOR REVISIONS, but every ESSENTIAL/MAJOR is STALE/already-caveated (Grok in full; OpenAI E1-E7/E10-E11/M*), the excluded DOI, the known non-load-bearing r-weighting-definition MINOR, a reproducibility-detail ask (inj-recovery ±0.01), or the FALSIFIED ε-correction reopening (reviewer omitted r=0.84). The genuine residue is polish-tier: 3 MINOR internal-consistency/cross-reference fixes, all closed by source edit. Zero BLOCKER, zero genuine MAJOR, zero open self-favoring item. Science, headline numbers (5.2–5.5σ / 2.6–5σ / BF 9–14 / 0.75σ / σ(n_fNL)=0.295), and the integrity fix are intact.

## f_NL forecast values for P1A cross-ref (internally consistent + clearly stated)
- f_NL^bounce = −35/8 = −4.375 (squeezed limit); f_NL^inf ≈ +0.015 (contrast ≈ 290)
- Imported baseline σ(f_NL^local) ≈ 0.7 (Heinrich+2023 bispectrum-only); 0.5 with power spectrum
- Template overlap r = 0.84 ± 0.02 (noise-weighted central; range 0.829–0.876)
- **SPHEREx forecast: 5.2–5.5σ optimistic (template-corrected, pre-systematic), 2.6–5σ realistic (post full systematic budget)**
- MegaMapper (proposed, unfunded): σ(f_NL) ≈ 0.5 ideal → illustrative 3–7σ envelope
- Bayes factor: BF ≈ 9 recommended (σ_theory=1.0, broad [−15,+15]); up to ≈14 delta-prior max
