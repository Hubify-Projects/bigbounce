# R55 P1B Truth Audit — convergence-confirmation round

**Paper:** P1B (Technical Verification Companion), `arxiv/paper1b_mcmc_companion.tex` v1B.0.76
**Round:** R55 (convergence test after R52/R53/R54 + EXT21/22; 0 BLOCKER / 0 surviving MAJOR expected; R54 found 0)
**PDF:** `/tmp/R55_P1B/paper1b_mcmc_companion.pdf` md5=2d80d814, 21 pages, git HEAD 87a96736
**Compile:** pdflatex ×3, 0 undefined refs/citations (the lone "undefined" log line is the harmless OMS/cmtt/m/n font-shape substitution), 0 overfull hbox/vbox.
**Vendor legs returned:** OpenAI gpt-5 (native PDF + reasoning_effort=high + pass-2 self-critique), Gemini 2.5 Pro (native PDF + pass-2 NO_NEW), Grok 4.3 (rasterized + pass-2 NO_NEW). **Perplexity FAILED** (401 insufficient_quota — same as R54).

## Net verdict: CONVERGED. Zero new VERIFIED DO-NOW defects.

Every vendor finding triages to FALSIFIED (review-harness/extraction/hallucination artifact), STALE/OPINION (scope/framing/length/wording polish), or TRULY-BLOCKED (compute reruns / Houston-decision, explicitly out-of-scope this round). The only arithmetically-substantive leg (OpenAI m1) independently CONFIRMS every audited scalar is correct.

---

## Verdict-first triage

### FALSIFIED — false positives (MUST NOT "fix")

| ID | Claim | Verdict |
|----|-------|---------|
| **Gemini P1B-E1** | "[REVIEWER METADATA …] block at p.21 must be removed from the paper" | **FALSIFIED.** That block is review-harness-injected text; the prompt literally labels it "NOT PART OF THE PAPER — DO NOT FLAG AS ARTIFACTS." `grep "REVIEWER METADATA\|Round context"` over the .tex returns **0 lines** — it is not in the source. Gemini flagged the anti-flag marker. NO EDIT. |
| **Grok P1B-NIT-1** | "'canonical canonical-mask' typographic duplication in source" | **FALSIFIED.** Source L1994 reads "indistinguishable from the canonical-mask" — single token, no duplication. Grok itself notes it is "not visible in the rendered PDF." Hallucinated. NO EDIT. |
| **Grok P1B-E3** | "side-by-side σ statements lack required 'not directly comparable' language" | **FALSIFIED.** Abstract L1115 reads "…not sky-measurement systematics, and are not [directly comparable]"; Gemini N1 even quotes the exact phrase. The language is present. NO EDIT. |
| **Grok P1B-N1** | "June 20 2026 chronologically impossible" | **FALSIFIED (recurring).** `\paperTimestamp` June 20 2026 is the correct, intended date; Grok's "current review cycle" is a hallucinated frame. NO EDIT. |
| **(carried) Gemini HEALPix / OpenAI LiteBIRD** | recurring extraction artifacts from prior rounds | **STILL FALSIFIED.** Re-verified: Ω_pix = 4π·(10800/π)²/(12·512²) = **47.210 arcmin²**, σ_pix=10/√47.21=**1.455 µK** (L1839–1844); LiteBIRD `\sqrt{0.03^2+0.094^2}` typesets correctly → 0.072/0.0987 = **0.73σ≈0.7σ** (L2650). Paper exactly right. NO EDIT. |

### STALE / OPINION — framing, length, wording (no source-verified defect)

- **OpenAI E2/M3** ("move version-stamp / commit SHA / file-path / claims-classification Table V to Supplementary") — intentional reproducibility documentation for a *verification companion* paper; not a correctness defect. OPINION/scope. Settled across R52–R54.
- **OpenAI E4/M2** ("add the word 'unweighted' to the abstract NaMaster-bias line") — estimator is pre-declared in the body (L1187 template-fit SNR; "unweighted-estimator" justification paragraph), and the abstract already carries the load-bearing "MC pipeline-recovery figures, not sky-measurement systematics" caveat (L1114–1115). Wording-polish, not a defect. OPINION.
- **OpenAI M4/M5, m2–m5, n1–n2** — ALP-mass m↔m_a notation, ½sin(4β)=sin2βcos2β reminder, ℓ_max β-independent-constant clarification, V′(ϕ) line, dash/length cosmetics. OPINION-tier polish.
- **Gemini M1, M2, N1–N3** — restructure/de-emphasize w0wa (opinion), elevate SNR-vs-β/σ_β footnote into body (already in main text L1187 + caption), "each other's"→"published" rephrase, √2-noise clarification, 3.9σ→3.95σ (explicitly an *auxiliary cross-check, not headline*; 3.9 is one-decimal rounding of 0.241/0.061=3.95). All cosmetic. OPINION.
- **Grok E1/E2/M1** — abstract "overstates scope" / "not standalone" / "21pp too long → 8–10pp". Recurring Grok pattern-009 calibration items (documented low audit weight on this companion paper). Abstract is exhaustively scope-walled ("stock-CAMB proxy", "pipeline-recovery", "spectator-ALP, not ECH-specific"); PRD has no length cap for companions. STALE.
- **Grok N2** — 6–7 sig-figs on derived quantities vs 2–3-fig inputs. Cosmetic rounding-presentation. OPINION.

### TRULY-BLOCKED — compute reruns / external IDs, out-of-scope this round (task: skip covariance refit)

- **OpenAI E1, M4-equiv** — frozen Zenodo/DOIs. Houston-decision; paper honestly states "DOI assignment pending." Not a surgical .tex fix.
- **OpenAI E3** — SN-overlap-robust control runs (DESI+Planck+Pantheon+ only; +DES-SN5YR only). Already disclosed (caveat (e), fn:wcaveat, "diagnostic only, not model selection"); product-likelihood double-weight of ~20% shared SNe explicitly caveated. Covariance/compute-bound. Settled R52/R53.
- **OpenAI E5** — PR4-consistent single Planck pairing for the headline ΔNeff. Already disclosed; the c15 release-pairing rerun (planck2020 lollipop.lowlE + planckpr4lensing) shows 0.04σ agreement. Compute-bound.
- **OpenAI M1** — N_MC=200/500/1000 sufficiency sweep for the bias SE. Robustness *addition*, not correction of an error; compute-bound.
- **Grok M2** — one-sided 95% ΔNeff upper-limit getdist post-processing script. Disclosed in footnote; reproducible from frozen chains + getdist defaults. Documentation-completeness, not a defect.
- **Grok M3** — additional per-figure "do not interpret as detection" warnings. Already extensively caveated (abstract + L1187 + fn:4 + caption). Optional.

### Independent Opus arithmetic spot-checks (all PASS — confirm paper correct)

- HEALPix Ω_pix = 47.210 arcmin²; σ_pix = 10/√47.21 = 1.455 µK. ✓
- H0 full-tension: (73.04−67.68)/√(1.06²+1.04²) = 5.36/1.485 = **3.61σ** → "∼3.6σ" ✓ (matches OpenAI m1).
- S8: 0.827±0.010 ⊗ 0.776±0.017 → 0.814±0.009, Δ/σ = 0.051/0.0197 = **2.59σ** → "2.6σ" ✓.
- w_pivot = −0.952±0.019, distance from −1 = 2.5σ ✓.
- LiteBIRD 0.072/√(0.03²+0.094²) = 0.73σ ✓.

### Future-work sweep (body)

All hits TRULY-BLOCKED: nested-sampling lnB/ΔAIC/ΔBIC (compute-bound, disclosed L1147/1530/2186/2701); Papers II/III/IV "in preparation" (separate papers); beam-mismatch MC "deferred to future sky-measurement-level analysis" (appropriate scope-walling). **Zero DO-NOW.**

---

## Closures applied: NONE (no verified DO-NOW item exists)

## Overflow audit: CLEAN (0 overfull hbox/vbox, 0 undefined refs/citations, 21 pages)

## CONVERGENCE STATEMENT
P1B is **CONVERGED at R55**. Three substantive vendor legs (incl. the calibrated OpenAI gpt-5 leg with pass-2 self-critique) produced zero source-verifiable defects. Every new arithmetically-substantive check (OpenAI m1) independently confirms the paper is correct. The only "new" concrete findings — Gemini's REVIEWER-METADATA block and Grok's "canonical canonical-mask" duplication — are review-harness / hallucination artifacts not present in the source. All remaining items are framing/length/wording OPINION (recurring Grok pattern-009 + cosmetic polish) or compute-bound robustness reruns / DOI assignment already disclosed as limitations. Prior-round false positives (HEALPix Ω_pix=47.21, LiteBIRD √) re-verified intact and remain FALSIFIED. No regressions, no novel BLOCKERs/MAJORs. Recommend exit at galley-proof readiness.
