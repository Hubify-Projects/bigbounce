# RA-INT P2 — Round A Truth Audit (verdict-first, neutral)

**Paper:** P2 `research/focused_paper_source_integration/02_full_draft.tex` (v1.7.78 → v1.7.79)
**Date:** 2026-06-29
**Engine:** `tools/v3_native_pdf_review.py` native-PDF. Legs: OpenAI gpt-5 (methodology), Gemini 2.5 Pro (cosmology), Grok 4.3 (brutal, rasterized). Perplexity quota-failed (401); no Anthropic leg in config.
**Framing:** P2 is a deliberate sensitivity RECAST of the Heinrich+2023 σ(fNL)=0.7 bispectrum forecast — judged as such (recast-framing complaints = OPINION).

## Vendor verdicts (actual)
- **OpenAI_methodology:** MAJOR REVISIONS. "Most arithmetic checks out... abstract conforms to 'sensitivity recast' framing." Checks-passed section independently reproduces 6.25, 5.19–5.48σ, σ_eff=1.221→3.01σ, bφ→4.08σ, combined 2.73σ, 49% variation, SDB 3.08/7.06, τNL 27.6.
- **Gemini_cosmology:** MAJOR REVISIONS. Flagship "BF 9.8→9.2 discrepancy" — Gemini itself confirms "the number is correct according to the author's code." Rest = restructure/shorten.
- **Grok_brutal:** MAJOR REVISIONS. Claims new Table IV arithmetic mismatch (P2-E4).

## Verdicts vs source

### VERIFIED → CLOSED (real fixes, NO numbers changed)
- **P2-E6 (OpenAI) — squeezed-ratio index convention.** Sec II (L690) + grid `k1≤k2≤k3` (L699) make k1 the long/squeezed mode; Sec III.B (L776) defines the squeezed cutoff as x3≡k3/k1 with x3→0 ⟺ k3≪k1 (k3 long) — opposite index assignment, impossible under k1≤k2≤k3. Checked `null_space_analysis.py`: benchmark eval uses k1-long `(eps,1,1)` but the overlap-scan grid fixes k1 hard and uses k3 long (`x3=k3/k1→0`, k3≤k2≤k1). Both labelings physical (BNL permutation-symmetric). FIX: added an Index-labeling note at L776 stating the scan interchanges index roles vs the benchmark convention and r is unchanged — resolves the reader-facing contradiction without misrepresenting the code (no relabel, no number change).
- **P2-M12 (OpenAI) — σ(fNL)=0.7 mislabeled "per-bin".** 0.7 is the Heinrich+2023 full multi-tracer COMBINED-sample forecast (paper's own Sec V L800: "full SPHEREx sample"), but Sec V (L802), MegaMapper §(L819), and Fig.5 caption (L974) called it the "per-bin baseline". FIX: "per-bin σ(fNL)=0.7/0.9" → "combined-sample baseline σ(fNL)" at 3 sites; kept "per-tracer-bin b_φ prior" (correctly per-bin). No number change.

### FALSIFIED (no edit)
- **Grok P2-E4 ("Table IV arithmetic mismatch", pass-2 flagship).** Grok computes 4.375/1.345≈3.25, 4.375/1.41≈3.10 and calls the table inconsistent. He omits the r=0.84 NUMERATOR the caption mandates ("Significance = |fNL|×r/σ_eff with r=0.84"): 4.375×0.84/1.345=2.73σ≈2.7 ✓; 4.375×0.84/1.41=2.61σ≈2.6 ✓. OpenAI's Checks-passed section independently reproduces both. Table IV is correct.
- **Grok P2-M1 / m1 ("BF 9–14 vs r→1 never reconciled").** Abstract L648 + dedicated "Template-mismatch bookkeeping" paragraph (L944) explicitly map 17.1→14.4, 9.8→9.2 etc. Fully reconciled.
- **Grok N4 / "June 28 2026 in future".** Date intentional (it IS June 2026); now bumped to June 29.
- **Gemini "BF 9.2 wrong".** Self-withdrawn by Gemini ("correct according to code"); independently 9.2 from scipy at σ_eff=0.833.

### OPINION / OUT-OF-SCOPE (no edit — it IS a recast)
- All three vendors' headline MAJOR-REVISIONS = (a) length / "condense to ≤15pp" (Grok E3, OpenAI m7, Gemini), (b) "recast vs forecast" / "downgrade detection-significance to sensitivity-estimate" (OpenAI E1, Grok E2) — the paper already labels everything "sensitivity recast / additive-quadrature heuristic / not a joint-covariance forecast" throughout (abstract L646, Sec VII L954, conclusion L1135), (c) reproducibility asks: in-paper SVD/Fisher/weighting-kernel ledgers (OpenAI E3/E5/M4/M5), bispectrum-level joint covariance (OpenAI E1, Grok E2), 3-D injection-recovery (OpenAI M1, Grok M3). These are augment-now/future requests, not internal contradictions. DOI placeholder = deferred to camera-ready (calibration).
- OpenAI m1 "290 → 291.67": rounding preference; 290 is an accepted benchmark round. OPINION.
- OpenAI E7/E8/M11 (figure axis units, Fig.5 caption context, folded-boundary SVD): figure-internal / methodological-robustness asks, not number contradictions; figures are PNG artifacts. Deferred (not DO-NOW for Round A; re-examine Round B if re-raised).

## Compile
4-pass pdflatex + bibtex: **0 undefined references**, 29 pages, page-1 date = "June 29, 2026". Overflow audit PASS: 2 overfull hboxes (2.95pt Table I, 1.23pt appendix eq.) byte-identical to pre-edit baseline, both <3pt, neither introduced by edits.

## Outcome
2 VERIFIED internal-consistency items closed with real no-number fixes; 0 fabricated. Convex tracks v1.7.79 (orchestrator). Did NOT commit/mirror per instruction.
