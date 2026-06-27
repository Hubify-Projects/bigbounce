# R57 P1B — Truth Audit (HARDENED / de-biased re-review)

Source: `arxiv/paper1b_mcmc_companion.tex` @ v1B.0.78
PDF: `/tmp/R57_P1B/paper1b_mcmc_companion.pdf` (22 pp, md5 653da036), pdflatex ×3 → 0 undef refs/citations
(lone log "undefined" = harmless `OMS/cmtt/m/n` font-shape substitution), 0 overfull hbox/vbox.
Vendors returned: OpenAI gpt-5 (native PDF, reasoning_effort=high + pass-2, MAJOR REV — calibrated leg),
Gemini 2.5 Pro (native PDF + pass-2, MAJOR REV), Grok 4.3 (rasterized + pass-2, REJECT),
Perplexity (FAIL — 401 quota), + own Opus read with direct figure-render inspection.
Standard: high PRD/MNRAS bar; no severity-defaulting. Self-favoring / unstated-assumption /
internal-inconsistency = real finding (MINOR min). Patterns 061-064 + calibration filter used for
genuine false-positives only. Prior history: R54 / R55 / R56 each 0-new.

## Verdict-first adjudication (this round's candidate items)

| # | Vendor finding | Tier asked | Verdict | Evidence |
|---|----------------|-----------|---------|----------|
| 1 | Fig. 2 (`fig:dneff_viability`) x-axis labeled "Neff" + "SM (Neff=0)" while caption says ΔNeff; SM Neff=3.046 not 0 (OpenAI **E3**, calibrated-leg ESSENTIAL) | ESSENTIAL | **FALSIFIED (direct visual inspection)** | Rendered the committed `figures/fig_dneff_viability_two_frozen.pdf` at 150 dpi: panel-(a) x-axis reads **`ΔN_eff`**, legend reads **`SM (ΔN_eff = 0)`** — exactly matching the caption. ΔNeff=0 ⟺ Neff=3.046 is correct. The calibrated leg misread the rasterized render. No defect. |
| 2 | Fig. 1 corner: "8" instead of σ8 on axes; ambiguous labels (OpenAI **M5**) | MAJOR | **FALSIFIED (direct visual inspection)** | Rendered `figures/paper1_corner_full_tension.pdf`: all seven axes correctly labeled `H_0`, `Ω_m`, `σ_8`, `S_8`, `n_s`, `τ`, `ΔN_eff` — σ8/S8 properly subscripted, no bare "8". Misread render. No defect. |
| 3 | "≳100× fine-tuning … (equivalently ∼25× …; quantitative derivation in fn 6)" — fn derives only 25×, ≳100× undECHrived (OpenAI **E2**) | ESSENTIAL | **OPINION / wording-precision; NOT a closable DO-NOW** | The "≳100×" (L2205, single occurrence) is the energy-density tuning Ωₐ∝θi² (the scaling fn:theta_backreaction *does* derive) measured against the cosθi-flat-prior natural value θi≈π/2≈1.57: (1.57/0.1)²≈246× ≳100×. The "∼25×" is the same θi² law against the ad-hoc 0.5 midpoint: (0.5/0.1)²=25×. Both derive from the one disclosed scaling, against two baselines; "equivalently" is loose (they are not literally equal) but reconstructable. Decisively **anti-self-favoring**: it reports a *larger* fine-tuning penalty against the author's own model — the opposite of a concealed self-favoring choice. Honest residual: tighten "(equivalently …)" → "(or ∼25× relative to the θi≈0.5 midpoint)". Optional polish, not an integrity defect. |
| 4 | Abstract cross-references fn 3 / Sec IV (not self-contained) (OpenAI **E1**, Gemini, Grok N2) | ESSENTIAL | **OPINION (editorial/style)** | Abstract L1122 carries an in-line pointer "(PR3-vs-PR4/NPIPE disambiguation is given in fn … in Sec IV)"; the load-bearing fact (PR3+WMAP9 published) is *in* the abstract. EXT5-B2 already relocated the footnote *out* of the abstract; only the pointer remains. PRD abstract-reference style preference, not a correctness/integrity defect. |
| 5 | 0.040° NaMaster bias estimator-specific; qualify in all headline sites (OpenAI **M2**) | MAJOR | **STALE / already-disclosed** (R56 #2 FALSIFIED) | Body robustness battery discloses inverse-variance fit → β̂=0.264° (bias −0.006°), "removing ≈80% of the bias" (L2025); abstract labels it "pipeline-recovery bias … not sky-measurement systematics" (L1113-1117). Headlining the *larger* unweighted bias is the conservative direction. No new action. |
| 6 | c15 release-pairing rerun R−1=0.0147 (>0.01 target) used for 0.04σ claim (OpenAI **M4**) | MAJOR | **OPINION / already-disclosed** | Paper prints R−1=0.0147 explicitly (L2146) and frames c15 as a "release-pairing robustness rerun … empirical bound on pairing-induced bias", not a headline. 0.04σ ≪ any sub-convergence noise; the check *agrees* (anti-self-favoring). Disclosed limitation. |
| 7 | LiteBIRD √ term "0.032" missing square (OpenAI **E5** pass-2) | ESSENTIAL | **FALSIFIED — recurring extraction artifact (directive: stays FALSIFIED)** | Source L2655 = `\sqrt{0.03^2+0.094^2}` → 0.0987, 0.072/0.0987=0.73σ≈0.7σ. Typesets correctly; PDF-text extraction drops the superscript. Re-verified, held FALSIFIED. |
| 8 | Ω_pix=47.21 vs "exact 47.28" arcmin² (OpenAI **m6** pass-2) | MINOR | **FALSIFIED — recurring HEALPix artifact (directive: stays FALSIFIED)** | 4π/(12·512²)=3.995×10⁻⁶ sr × (10800/π)² arcmin²/sr = **47.21**. Paper exact; vendor's 47.28 wrong. Held FALSIFIED. |
| 9 | "0.01σ" S8 agreement is an arithmetic typo (values differ by 0.013→0.96σ) (Grok **m1** pass-2) | MAJOR | **FALSIFIED (misread)** | The comparison is full-tension chain S8=0.814±0.008 vs the *naive combination* 0.827⊗0.776=**0.814**±0.009 — i.e. 0.814 vs 0.814 → ~0σ ("0.01σ level", correct). Grok compared 0.814 to 0.827 (one input of the combination), not to the combination's 0.814 result. No defect. |
| 10 | "June 26 2026" / "April 2026" future-date placeholder (Gemini E1, Grok N1/N3) | ESSENTIAL/MINOR | **FALSIFIED — recurring date artifact (R55 N1)** | `\paperTimestamp` = the correct intended date; "current review cycle" is a hallucinated frame. No edit. |
| 11 | Rescope/re-title as methods note; not ECH-specific; pipeline bias not propagated to real-sky budget (Grok **E1/E2/E3**, REJECT) | BLOCKER | **OPINION — recurring Grok pattern-009 (documented low audit weight)** | The paper *explicitly* scopes itself "NOT a spin-torsion theory module / NOT a competitive sky detection / NOT a distinctive ECH prediction" at abstract + intro + every section head; bias labeled "not a real-sky bias bound" at every site. Grok REJECT rests on disagreeing with disclosed scope, not on any source-verified defect. |
| 12 | Restructure (separate 3 analyses); expand intro for self-containment; move Claims-table/Appendix B to Supplementary (Gemini M1/M2/m2/m3, OpenAI n1) | MAJOR/MINOR | **OPINION (editorial/structure)** | Recurring structural-preference items; companion-paper layout is intentional. No correctness/integrity content. |
| 13 | m vs m_a notation; χ² naming for unweighted dimensionful SSR; Table IV triplet legend; various typography (OpenAI M1/M6/M3/m1-m5/n1-n2) | MINOR/NIT | **OPINION / polish** | All cosmetic or already-disclosed (χ²: paper states "no σ_b² divisor … unweighted to match public drivers", L1871-1877). No defect. |
| 14 | Permanent DOIs / frozen Zenodo release; purge commit-SHA/version/paths from body (OpenAI E4) | ESSENTIAL | **TRULY-BLOCKED (Houston-decision) + OPINION** | "DOI assignment pending (inserted at submission)" — standard pre-arXiv state, disclosed. Frozen archival release is a publication-stage action, not a surgical .tex fix. Skipped per task (no covariance/compute closures). |

## Recurring false-positives (held FALSIFIED, per directive)
- HEALPix Ω_pix=47.21 arcmin² → correct (re-derived). LiteBIRD √(0.03²+0.094²) → extraction artifact.
  Both re-raised by OpenAI pass-2 this round; both re-verified and held FALSIFIED.
- "Future date" (Gemini/Grok) → recurring frame hallucination; FALSIFIED.

## Independent Opus arithmetic spot-checks (all PASS — paper correct)
- H0 tension (73.04−67.68)/√(1.06²+1.04²)=3.61σ → "∼3.6σ" ✓
- S8: 0.827±0.010 ⊗ 0.776±0.017 = 0.814±0.0086 → "0.814±0.009" ✓; DES-Y3 tension 0.051/0.0197=2.59σ → "2.6σ" ✓
- w0 +4.31σ, wa −3.58σ; w_pivot=−0.952±0.019 → +2.5σ from −1 ✓ (Cov=−0.00729, 1−a_p=0.210, z_p=0.27 all reproduce)
- z_cross (−1−w0)/wa=0.282 → z×=0.39 ✓; H(z=0.5) CPL/ΛCDM = +1.7% ✓
- β=(α/4π)·8·1.06=0.28° ✓; C_aγ·Δφ/fa for 0.342° = 10.3 ✓; σ_pix=10/√47.21=1.455 µK ✓
- NaMaster under-recovery 0.238/0.27=0.302/0.342=0.88 ✓; Liu H0 0.55σ, S8 1.29σ ✓
- "≳100×" reconstructs as (1.57/0.1)²≈246× under the cosθi-flat-prior natural θi≈π/2 ✓ (derivable from disclosed θi² law)

## Net result
- **NEW VERIFIED DO-NOW: NONE.** No finding survives the hardened, de-biased truth-audit as a closable
  integrity defect. The two figure-internal-inconsistency claims from the calibrated OpenAI leg (E3, M5) —
  the only items that, if true, would have been MINOR-min real findings — were FALSIFIED by direct
  render inspection of the committed figure PDFs.
- **Self-favoring item under the hardened bar? NONE.** The closest candidate (E2 "≳100×") is the *opposite*
  of self-favoring: it reports a larger fine-tuning penalty against the author's own model, derivable from
  the disclosed Ωₐ∝θi² scaling. The two historically-favorable headline sites (w0wa σ-distances; 0.040°
  bias floor) remain reported in the conservative/de-rated direction with full in-paper disclosure.
- **Closures applied: NONE** (no verified DO-NOW exists). No .tex edit made; PDF unchanged.
- **TRULY-BLOCKED (skipped per task):** frozen Zenodo/DOI release (E4); overlap-aware DES-SN5YR×Pantheon+
  joint-covariance w0wa refit; N_MC sufficiency sweep — all compute/publication-stage, correctly deferred.
- Integrity-fix (w0wa SN-overlap caveat) VERIFIED INTACT, not reopened.
- Honest optional polish (non-blocking, NOT a defect): tighten the L2205 "(equivalently ∼25× …)" wording
  to name the two tuning baselines distinctly.

## Overflow audit: CLEAN (0 overfull hbox/vbox, 0 undef refs/citations, 22 pages; no edits this round).

## CONVERGENCE STATEMENT
P1B is **CONVERGED at R57** — third consecutive 0-new round (R54/R55/R56 = 0-new). Under a hardened,
de-biased, severity-no-default PRD/MNRAS bar with three substantive vendor legs (incl. the calibrated
OpenAI gpt-5 leg with pass-2 self-critique) plus a full Opus read with direct figure-render inspection,
zero new source-verifiable integrity defects surface. The only items that *could* have qualified as
MINOR-min real findings under the hardened rule — two figure-label internal-inconsistency claims — were
falsified by rendering the committed figures (axes are correct). Every other ESSENTIAL/MAJOR is a falsified
misread, a recurring extraction/date artifact (HEALPix 47.21, LiteBIRD √, future-date — held FALSIFIED per
directive), an already-closed/disclosed item, a Grok pattern-009 scope-disagreement (documented low weight),
or a pre-submission/editorial OPINION (DOI freeze, restructure, abstract style). No regressions, no novel
BLOCKER/MAJOR. The manuscript is at galley-proof readiness; no closure wave warranted.
