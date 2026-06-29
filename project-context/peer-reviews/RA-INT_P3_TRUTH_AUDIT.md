# RA-INT P3 — Truth Audit (Round A, INT leg)

**Paper:** P3 — "Spectrally Unusual Sources at Scale" (v3.1.120, PDF md5=24ac287f, 30 pp)
**Date:** 2026-06-29
**Reviewers (native-PDF v3 engine):** OpenAI gpt-5 (methodology, reasoning_effort=high + pass-2), Gemini (cosmology), Grok 4.3 (brutal, rasterized), Perplexity (FAILED — 401 quota).
**Stance:** Neutral journal referee. Verdict-first; patterns 061-064 + June-2026 calibration.

## Vendor verdicts (actual)
- **OpenAI gpt-5 — MAJOR REVISIONS.** 6 ESSENTIAL + 2 pass-2 ESSENTIAL + MAJORs/MINORs. NOTE: its own "Arithmetic and statistical spot checks" section independently reconciled EVERY headline number (DESI rate, SDSS slice, NEOWISE excess, 388,493→378,280 totals, LAMOST 108,963, Wilson ±1.2%, Fisher σ=8.14 + envelope, NANOGrav 1.13σ/4.61σ, Cramér numeric) — all "OK".
- **Gemini — MAJOR REVISIONS.** 2 ESSENTIAL, 2 MAJOR, minors/nits.
- **Grok — REJECT.** 5 ESSENTIAL, 4 MAJOR.
- **Perplexity — FAILED** (insufficient_quota; no content).

## Truth-audit verdicts

### FALSIFIED
- **Grok E3 / Gemini E1 — "future date June 28 2026."** Today is 2026-06-29; June 28 is *yesterday*, not future. June-2026 is current per calibration. FALSIFIED. (No date bump warranted — nothing else closed.)
- **Gemini T3 — DESI ref [1] "arXiv:2503.14745 likely a typo for 23/24."** 2503 = March 2025; this is the real, correct DESI DR1 ID; bib already says "(accepted 2025)". FALSIFIED.
- **OpenAI E5 — "Cramér's V equation written incorrectly (√ equated to unsquared ratio)."** Source line 1002 actually reads `V = \sqrt{χ²/(N(k−1))} = \sqrt{376713/(378280×24048)} ≈ 0.0064` — the outer √ is present on BOTH sides; equation is correct (fixed in v3.1.106). OpenAI dropped the second radical when reading the rasterized PDF; its own spot-check computed √[...]≈0.0064 and called it OK (internal contradiction). FALSIFIED.
- **OpenAI E2 / Grok E2 / Gemini E2 — "abstract overstates 9.4% Fisher improvement / should lead with de-biased null."** Abstract §4 already LEADS: "the de-biased point estimate returns the single-tracer baseline σ_std=8.98 exactly (no multi-tracer improvement at current S/N)" before the 9.4%, which is labeled "a noise-driven forecast … not a detection." Ordering already satisfies the request. FALSIFIED/STALE.

### STALE (already-disclosed; no caveat-stacking)
- **Grok E1 / OpenAI E3 — "validated-only ≥268,519 is a non-recomputable lower bound."** This IS the disclosed transparency statement (abstract + §erosita): ≥ is conservative because exact validated-only 5″ re-dedup is not recomputable from committed *aggregate* artifacts; subtraction can only undercount. Honest disclosure, not an error; recompute needs pod-side per-object data. STALE.
- **OpenAI E2(tier)/Grok-implied / Gemini M1 / OpenAI E2 — "recommended tier contains failed Gaia+eROSITA."** v3.1.120 reframe already leads with the *validated catalog-grade subset* (≥268,519, excludes Gaia+eROSITA), bolds it in abstract sentence 1, and distinguishes "recommended" (269,317) from "validated." Catalog-grade relabel is DONE per calibration. STALE.
- **Gemini M1 — Gaia "lineage-inferred" provenance.** Already stated verbatim §training; Gaia carries per-object exploratory flags, excluded from validated subset, reported as exploratory addendum. STALE.
- **Gemini M2 / OpenAI(implied) — full-sample scaler leakage; do NEOWISE/Gaia robustness check.** Already disclosed (§training); eROSITA bounded check computed (257/298, J=0.76, ρ=0.94 — verified vs artifact); NEOWISE/Gaia checks explicitly stated as queued (feature tables pod-side only). STALE.
- **OpenAI E1/E7 — Planck Ntotal/rate basis (20,000 vs 2×10⁵; 1.00% vs 0.10%).** Footnote ♢ + ‖ already disclose both bases; 37.3M is the primary-sweep processed-source count; native re-score is selection-only. Internally consistent on stated basis. STALE/OPINION.
- **OpenAI E8 / M8 — 58.8% SIMBAD-unmatched in totals row incommensurate.** Already carries PP marker distinguishing the pooled 3″ top-100 exercise (v3.1.106 E5/E8). STALE.
- **OpenAI M7 — Planck binomial p≈4×10⁻⁴ needs correlation correction.** Already labeled "naive binomial … indicative rather than definitive" (v3.1.103). STALE.
- **Grok E5 / OpenAI M6 — SDSS cross-transfer score not interpretable.** Already disclosed extensively (S>5→12 sources, ~6500× compression, "not directly comparable," continuity slice). STALE.
- **Grok M1 — 17.8% novelty only on top-1000.** Already stated "single-sample point estimate … not a survey-wide rate"; Limitation (6): "no bound on full-catalog extrapolation, empirically untested." STALE.
- **Grok M3 — NANOGrav BF doesn't quantify survival under environmental SMBHB.** §nanograv environmental caveat already states BF "decisive only relative to idealized circular-orbit reference," not exclusive. STALE.
- **OpenAI E4 / Gemini(implied) — DOI/persistent-ID placeholders.** DOI deferred per standing calibration. OUT-OF-SCOPE/deferred.
- **Grok m2 / OpenAI M5 — ACT in Fig 2 baseline map.** Caption already labels formally quarantined, zero contribution. STALE.

### OPINION (presentation preference; no factual defect, not an unbacked number)
- OpenAI E6 / Grok m1 — internal \artifact{} file paths in main text (deliberate lab reproducibility convention).
- OpenAI M1 / Grok M2 — totals-row "Rate (%)" bookkeeping (already footnoted as not-a-frequency).
- OpenAI M2 — "largest of which we are aware" (already softened).
- OpenAI M3 — injection-recovery binomial CIs (polish; gates resolve far from threshold, disclosed).
- OpenAI M4 — "score-knee" wording (already "top-298 of committed raw-score artifact").
- Grok M4 / OpenAI scope — 30 pp length. Catalog-class; size is not a defect (task directive).
- Gemini N1-N4, T1-T2 / OpenAI m1-m10 — caption/notation/figure-style polish on companion-data figures.

## Independent number spot-checks (Opus, vs committed artifacts)
- eROSITA scaler refit: paper 257/298, J=0.76, top-1% J=0.64, ρ=0.94, anchor 247 == `ext3_fm1_erosita_scaler_refit.json` EXACT. ✓
- DESI recount: paper 2,468/2,531/3,390; SPECTYPE 2371/95/2; denom 20,299,155; control 189,675 == `ext3_b2_targettype_recount.json` EXACT. ✓
- Fisher: F₀=1/8.98²=0.01239; +0.0747×0.19²=0.01509 → σ=8.14; de-bias max(0,0.0361−0.4225)=0; 9.4%. ✓
- NANOGrav BF: 3.23/4.52e-4 = 7.14×10³; log₁₀=3.85. ✓
- Native sum 388,493; −10,213 = 378,280; −200 = 378,080; LAMOST 108,963. ✓
- χ²/dof 376,713/24,048 = 15.7; Cramér √(4.14e-5)=0.0064. ✓
**0 unbacked / fabricated numbers.** OpenAI's independent spot-check section corroborates.

## Disposition
**0 new VERIFIED items.** Every ESSENTIAL across all legs is STALE (already-disclosed), FALSIFIED, OPINION, or DOI-deferred. No real fix required. Paper **UNCHANGED** at v3.1.120. Compile clean (0 undef-refs). The two MAJOR-REVISIONS + one REJECT are driven entirely by re-raises of the v3.1.120 honest-reframe caveats (validated-vs-recommended tier, non-recomputable lower bound, scaler leakage, eROSITA axis) plus three falsified items (future-date, arXiv typo, Cramér equation).
