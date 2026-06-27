# R54 P1B Truth Audit — convergence-confirmation round

**Paper:** P1B (Technical Verification Companion), `arxiv/paper1b_mcmc_companion.tex` v1B.0.76
**Round:** R54 (convergence test after R52/R53 + EXT21/22; 0 BLOCKER / 0 genuine MAJOR expected)
**PDF:** `/tmp/R54_P1B/paper1b_mcmc_companion.pdf` md5=0b4a8768, 21 pages
**Compile:** pdflatex ×3, 0 undefined refs/citations, 0 overfull hbox/vbox (>0pt)
**Vendor legs returned:** OpenAI gpt-5 (calibrated, native PDF + pass-2), Gemini 2.5 Pro (native PDF + pass-2), Grok 4.3 (rasterized + pass-2). **Perplexity FAILED** (401 insufficient_quota).

## Net verdict: CONVERGED. Zero new VERIFIED DO-NOW defects.

Every vendor finding triages to FALSIFIED (extraction artifact), STALE/OPINION (scope/framing/length), or TRULY-BLOCKED (compute reruns explicitly out-of-scope this round). The two findings with genuine arithmetic substance both independently CONFIRM the paper is correct.

---

## Verdict-first triage

### FALSIFIED — false positives (MUST NOT "fix"; pattern-061/063 extraction artifacts)

| ID | Claim | Verdict |
|----|-------|---------|
| **Gemini P1B-M1** | HEALPix Ω_pix=47.21 arcmin² "wrong by ~13%, should be 41.8" | **FALSIFIED.** Verified two ways: 4π/(12·512²)=3.9947e-6 sr × 11,818,102 arcmin²/sr = **47.210 arcmin²**; and total-sphere 148,510,656 arcmin² / 3,145,728 pix = **47.210**. Paper is exactly right; σ_pix=10/√47.21=1.455 µK correct. Gemini's 41.8 is its own arithmetic error. NO EDIT. |
| **OpenAI P1B-E1** | LiteBIRD significance "misprints variances: √(0.032+0.0942)" | **FALSIFIED.** Source L2650 reads `\sqrt{0.03^2+0.094^2}` — squares correctly typeset. OpenAI flattened the superscripts in PDF text extraction. Value 0.072/0.0987=0.73σ≈0.7σ correct. NO EDIT. |
| **Grok P1B-N1** | "June 20 2026 chronologically impossible for a 2025 submission" | **FALSIFIED.** Paper date 2026 is correct; "2025" is Grok's own hallucinated review date. |
| **Grok P1B-M3** | "fold NaMaster pipeline bias into β_obs 3.6σ uncertainty" | **FALSIFIED.** Foreground-free deconvolution-algebra MC bias is explicitly NOT a real-sky systematic; folding it into the literature β would be wrong. Paper states this repeatedly. |

### STALE / OPINION — framing, length, scope (no source-verified defect)

- **Grok P1B-E1/E2/E3, M1, M2; OpenAI M5, M6, length note** — "retitle/remove ECH framing", "standalone-reader fails", "21pp too long → Letter", "no Δχ²/evidence ratio", "abstract numbers un-auditable". All recurring Grok pattern-009 calibration items (documented low audit weight on this paper). Companion-paper-by-design, exhaustively scope-walled; PRD has no length cap for companions; paper explicitly claims no model-selection. STALE.
- **OpenAI m1–m5, n1–n4, P1B-M6 (cite external code file/line)** — clarification/rounding/typeset polish; post-burnin count already in fn:sample_stratification (216,432); σ_b clarification optional. OPINION-tier.
- **Gemini N1–N3, T1–T2** — ΔNeff agreement "0.04σ vs 0.027σ": paper explicitly uses single-reported-std convention (0.007/0.179=0.039≈0.04σ, per changelog v1B.0.67 "in units of either reported std"); Gemini used quadrature. Both defensible — convention difference, not error. Remainder cosmetic (χ²/X notation, sentence length).
- **OpenAI m6** — "∼3.6σ" SH0ES tension: full-tension=3.61σ (exact), Planck+BAO+SN=3.49σ. The hedged "∼3.6σ" binds to the full-tension H0 headline (67.68±1.06) and to the body ΔNeff=−0.020±0.169 result (L1581/1590), both 3.61σ. Tilde covers the 0.1σ spread. Defensible approximation, not a defect. NO EDIT.

### TRULY-BLOCKED — compute reruns, explicitly out-of-scope this round (task: "skip TRULY-BLOCKED covariance refit")

- **OpenAI E2, M9** — re-run both frozen ΛCDM+ΔNeff combos + iter2 w0wa with PR4-consistent low-ℓ/lensing. Already disclosed (c15 release-pairing robustness rerun, 0.04σ ΔNeff bound). Compute-bound; not a surgical .tex fix.
- **OpenAI E3** — w0wa SN-overlap control runs. Already caveated (caveat (e), fn:wcaveat, "diagnostic only, not model selection"). Settled R52/R53; do not re-open.
- **OpenAI M1, M2, M3, M7, M8, M10, M11** — EOM-vs-full-integration error bound, prior-robustness table, beam-mismatch MC, free-YHe control, free-Σmν control, ℓ-range sweep, H0-marginalization point checks. All disclosed limitations / deferred robustness additions, not corrections of existing errors.
- **OpenAI M4** — finalize DOIs / Zenodo. Houston-decision; paper honestly states "DOI assignment pending".

### Verification of prior-round closures (per task: confirm still correct, do not re-open)

- **Anharmonic O(θ²/12)** (EXT19 / R52/R53): L2522, L2472 read `O(θ_i²/12)`. Correct: 1−cosθ = θ²/2 − θ⁴/24, fractional anharmonic correction = θ²/12 (≈8% at θ~1). **STILL CORRECT.**
- **w0wa Table II caveat + w_pivot footnote** (v1B.0.50): L1476 fn:wpivot internally consistent — Cov=−0.00729 (ρ=−0.90), 1−a_p=0.210, a_p=0.790, z_p=0.266≈0.27, σ_wp=0.0193≈0.019, w_p=−0.952, +2.5σ. All arithmetic verified. **STILL CORRECT.** Not re-opened.

### Independent Opus arithmetic spot-checks (all PASS)

ρ_crit,0=3H₀²M_Pl²=3.7e-11 eV⁴ (EXT18 fix); β=αEM/(4π)·8·1.06=4.93e-3 rad=0.28°; C_aγ·Δφ/fa=β/[αEM/(4π)]=10.3; inverse-variance combine 0.241±0.061=3.9σ; S8 two-Gaussian 0.827±0.010 ⊗ 0.776±0.017 = 0.814±0.009; NaMaster SNR √fsky scaling 20.32·√(0.85/0.32)=33.12 vs artifact 32.98 (0.5%); Ω_a≈m²θ²/(6H₀²(1+z)³) derivation correct; LiteBIRD 0.73σ.

### Future-work sweep (body, post-L1075)

All hits TRULY-BLOCKED: nested-sampling lnB (compute-bound, disclosed); Papers II/III/IV "in preparation" (separate papers); beam-mismatch MC "deferred to future sky-measurement-level analysis" (appropriate scope-walling for a validation paper). **Zero DO-NOW.**

---

## Closures applied: NONE (no verified DO-NOW item exists)

## Overflow audit: CLEAN (0 overfull hbox/vbox, 0 undefined refs/citations, 21 pages)

## CONVERGENCE STATEMENT
P1B is **CONVERGED at R54**. Three substantive vendor legs (incl. the calibrated OpenAI gpt-5 leg with pass-2 self-critique) produced zero source-verifiable defects. The only two arithmetically-substantive findings (Gemini pixel-area, OpenAI LiteBIRD formula) are both vendor extraction/arithmetic errors confirming the paper is correct — they are false positives and were NOT actioned. All remaining items are framing/length OPINION (recurring Grok calibration) or compute-bound robustness reruns already disclosed as limitations. Prior-round closures (anharmonic O(θ²/12), w0wa/w_pivot) re-verified intact. No regressions, no novel BLOCKERs. Recommend exit at galley-proof readiness.
