# M37-EXT truth-audit — P2 (v1.7.116, byte-unchanged)

**Round:** M37-EXT (2 legs) · **Version:** v1.7.116 (byte-unchanged; no edit this round)
**Verdicts (literal, read from each raw before any adjudication):**
`P2_grok_M37.md` = **MINOR REVISIONS** (0 MAJ / 5 MIN) · `P2_chatgpt_M37.md` = **REJECT** (7 MAJ / 2 MIN).

**Raws READ VERBATIM (both, fully) before any verdict.** `ledger_match.py` run on each raw as a DRAFT
matcher; every finding re-adjudicated below with a source-cited D-id, matched or not.

**Provenance ✓:** Both raws review the correct f_NL SPHEREx-forecast paper — −35/16 squeezed vertex sum
(vs printed −35/8), r=0.84 template overlap, Heinrich et al. covariance, BF≈9–14, δf_NL≲10⁻³ cubic
transmission, ρ=−0.868 proxy floor. Same manuscript as M15/M23/M31/M34.

---

## Grok (MINOR REVISIONS, 0 MAJ / 5 MIN) — ledger_match 4/6 MATCHED (2 UNMATCHED adjudicated)

The header ("REVISIONS ISSUES:") is parsed as finding #1 by ledger_match — a scaffolding line, NOT a
finding. Closing paragraph CREDITS the central claim verbatim ("The central claim … is supported by the
multi-way amplitude verification, noise-weighted overlap calculation, independent tree-level Fisher
cross-check (r_eff ≈ 0.99), and closed-form Bayes-factor evaluation"). All 5 real MINORs re-flag standing
disclosed classes.

| # | sev | finding (abridged) | verdict | D-id (source-cited) |
|---|-----|--------------------|---------|---------------------|
| — | — | "REVISIONS ISSUES:" (header, ledger_match #1, score 0.07) | NON-FINDING | scaffolding line, not a reviewer finding |
| 1 | MIN | Sensitivity envelopes (∼2.6–2.75σ / ∼1.3–2.75σ incl. 0.8σ edge) mix qualitatively different null procedures (CMB-Fisher signal-only vs LSS noise weighting; proxy ρ=−0.868 vs channel-native ρ≈−0.42–0.49); no compact summary table mapping each endpoint to its assumptions | RE-FLAG | **DP2-04** ("scoping sensitivity envelope … not a joint-covariance forecast," abstract L892, `tab:systematics` caption; endpoints labeled non-comparable) + **DP2-34** (channel-native ρ≈−0.42, DP2-CN1-01 fixed v1.7.115). Grok EXPLICITLY notes distinctions "are disclosed in the text." |
| 2 | MIN | −35/16 (vs published −35/8) rests on the −(99/128)∑kᵢ³ discrepancy; Appendix A should display the explicit side-by-side monomial comparison (Cai printed vs exact vertex sum) | RE-FLAG | **DP2-01/-02** (99/128 sign + −35/16 quadruple-certified; `tab:vertices` L1482 + `tab:vertexwalk` L1505 already give explicit four-vertex algebra) + **DP2-16** (App-A ordered-sum convention stated verbatim). Display-preference OPINION on already-present content, NOT a new math error. |
| 3 | MIN | 10 000-sample null-space scan r=0.85±0.13 (range 0.55–1.14); headline uses only noise-weighted r=0.84±0.02; null-space uncertainty not propagated into the systematic budget/abstract | RE-FLAG | **DP2-15** (amplitude-invariant shape-basis stress band; NEVER enters σ_eff, §spherex L987; reparametrization-non-invariance caveat verbatim L966). ledger_match 0.98. |
| 4 | MIN | MegaMapper (§V) illustrative; at z=2–5 relativistic projection effects grow steeply so adopted degradation factors may be optimistic; add a quantitative high-z remark | RE-FLAG | **DP2-30** (MegaMapper "illustrative … uncalibrated projection … relativistic projection effects … grow steeply … become dominant"—the exact high-z caveat Grok requests is ALREADY present verbatim L1120, `\cite{Jolicoeur:2025}`) + **DP2-14**. ledger_match called this #5, best-match DP2-18 @ 0.22 UNMATCHED — Opus-adjudicated to DP2-30 (disclosure is verbatim). |
| 5 | MIN | Presentation/flow: dense parentheticals, .json/.py cross-refs, reproducibility detail; relocate a subset to Supplemental | RE-FLAG | **DP2-30** + **DP2-M1** (directive-M presentation restructure actioned v1.7.116; residual length = OPEN-VENUE / OPINION). |

**Grok: 0 genuinely-new.** MINOR↔MAJOR band across M15/M25/M28/M31/M34 = documented pattern-066; every
closing AFFIRMS −35/16.

---

## ChatGPT (REJECT, 7 MAJ / 2 MIN) — ledger_match 7/9 MATCHED (2 UNMATCHED adjudicated)

Closing statement (3): "−35/16 is a plausible exact-dust amplitude" — again concedes the headline value;
disputes the polynomial-error mechanism, nonlinear transmission, and forecast scope (all disclosed classes).
Item set 1:1 with M15/M23/M31/M34 REJECT floor (DP2-24 maximal-harsh structural floor).

| # | sev | finding (abridged) | verdict | D-id (source-cited) |
|---|-----|--------------------|---------|---------------------|
| 1 | MAJ | §II.A/App A: "artificial polynomial null space" used in place of derived bispectrum; exact vertex (5,2,2) orbit → (3,1,−9,5,−33,9) not the fitted (2,7,3,−12,−69,19); Fig.1/r/nonlocal decomposition must be recomputed; "multiplying printed Cai by ½ cannot correct an additive local error" | RE-FLAG | **DP2-15/-01/-03/-16/-25**. Re-flag of the M31/M34-FALSIFIED convention claim: re-running committed `p2_vertex_check.py`, the paper's 6-perms convention → squeezed −35/16 (=Li c_s=1, convention-FREE) + equilateral −255/128 (=Table I); ChatGPT's proposed distinct-monomial convention → −285/128/−65/32, CONTRADICTS both cross-checks. The (2,7,3,…) reference vector is the amplitude-invariant null-space stress band (DP2-15, never enters σ_eff), NOT the physical bispectrum. Headline UNAFFECTED. ledger_match 0.33. |
| 2 | MAJ | **App A.1(d): Cai–Li resolution "internally inconsistent" — −99/128∑kᵢ³ discrepancy disappears under distinct-monomial counting; asserts Cai (34)–(36) precede in-in commutator doubling; says the same polynomial reduces to −305/64 on one page and −35/8 on another** | RE-FLAG (**NOT a new math error**) | **DP2-01/-03/-16/-25** (ledger_match 1.00, confirmed). This is the STANDING −35/16-vs-−35/8 / +(99/128)-sign disposition, not a fresh defect: DP2-01 already states the vertex sum exceeds the transcribed printed polynomial by +(99/128)∑kᵢ³ → printed polynomial squeezed-reduces to **−305/64** (this IS the "−305/64" page ChatGPT cites); Cai's separately-published **−35/8** is retained ONLY as a non-reproducible literature reference (DP2-03/-25), NOT claimed to be reproduced from his coefficients — so the "−305/64 vs −35/8 on different pages" ChatGPT flags is the DELIBERATE, disclosed distinction between the transcribed-polynomial reduction and Cai's separately-printed value, not a self-contradiction. The distinct-monomial-convention "fix" is DP2-15/-25 (the convention that FAILS Li c_s=1 + Table I). ChatGPT's own raw concedes "Li et al.'s independent c_s=1 formula supports −35/16." Convention verdict re-derived by re-running the committed script + convention-free Li formula, not hand-waved. |
| 3 | MAJ | §III.B–IV: SPHEREx recast not statistically defined in the imported covariance; r=0.84 is neither α=F(local,bounce)/F(local,local) nor F(bounce,bounce); own surrogate gives r_eff≃0.99 → metric-dependent; Heinrich sets local baseline not bounce rescaling | RE-FLAG | **DP2-14/-17/-22** (r=0.84 = deliberately-conservative flat-weight shape cosine; r_eff≈0.99 = survey-optimal validation; reconciled §spherex L888; recast scope disclosed abstract L888; reproduction-vs-Heinrich limitation list L1045). ledger_match 0.76. |
| 4 | MAJ | **§II.C/IX.E/Conclusion: cubic-order δf_NL≲10⁻³ "not derived" — counting one dof doesn't establish ζ̇→0 or nonlinear conservation; ζ∝|η|⁻³ outside horizon; Wilson-Ewing is linear only; need 2nd/3rd-order dressed-metric or separate-universe proof** | RE-FLAG | **DP2-13** (+ softened **DP2-32.6/-19**). The explicitly-flagged load-bearing caveat (★): bound is an OOM single-clock scaling estimate verified at LINEAR order (Wilson-Ewing), closed at cubic order by dof-counting, DISCLOSED as "not a full 3rd-order in-in" and (v1.7.112) as "plausible but not derived in the deformed-algebra scheme," conditional on dressed-metric quantization. ChatGPT restates the disclosed limitation as a defect. ledger_match 0.23 UNMATCHED — Opus-adjudicated to DP2-13 (the load-bearing-caveat class explicitly names this bound). NOT genuinely-new. |
| 5 | MAJ | §II.C/VIII.B: quasi-dust correction is an estimate presented as controlled prediction; w≃−0.003 vs exact w=0 amplitude; κ_ε=2.8–40 schematic (14× upper endpoint); differentiating one prefactor can't justify 0.6–8%/f_NL–n_s curve | RE-FLAG | **DP2-20** (κ_ε single-prefactor-derivative estimate with four-vertex cancellations acknowledged; f_NL–n_s "indicative") + **DP2-19** (c_s=1 quasi-dust benchmark, assumption (a)). ledger_match 0.55. |
| 6 | MAJ | §VII/Table V: "post-systematic" interval not one coherent likelihood — mixes uncalibrated σ_GR, b_φ-mimic replacements, transferred SDB ρ, unweighted shape cosine in σ/√(1−ρ²); 0.8/1.3/1.5/2.3σ not one posterior; "1.3σ floor vs 0.8σ edge" contradictory | RE-FLAG | **DP2-04/-07/-26** (heterogeneous-endpoint disclosure; proxy-floor DP2-07/-33 + 0.8σ edge disclosed in abstract v1.7.112; channel-native surrogate DP2-34/-CN1-01). ledger_match 0.55. |
| 7 | MAJ | §VI.C: Bayes factors are prior-volume calculations; multifield competitor = uniform interval so BF≈W/√(2π)σ set by arbitrary width; no inflationary Lagrangian/likelihood; remove BF≈9–14 headline | RE-FLAG | **DP2-18** ("illustrative … not definitive model-selection evidence"; four-corner prior grid `tab:bayes` L1236; prior-sensitivity mapped). ledger_match 0.44. |
| 8 | MIN | §VI.A/Table II: gauge-frame quantity mis-identified as direct survey observable; f_NL≃0.015 "on-sky" needs full observable derivation; factor-146 should be replaced by "single-field predicts no measurable SDB at SPHEREx precision" | RE-FLAG | **DP2-21** (gauge-frame / factor-146 framing dispute; comoving-gauge consistency-term interpretation disclosed, conclusion L1448; no numeric error). ledger_match 0.89. |
| 9 | MIN | §IV–V/App B/DAS: unsupported tangential projections (anomaly-tracer, 5% photo-z, MegaMapper envelope, spectator-ALP birefringence) should be removed/separated; shorten; point to a frozen commit + archival DOI available DURING review, not a promised camera-ready DOI | RE-FLAG + PROCESS-NIT | **DP2-30** (presentation-scope: length, birefringence/MegaMapper relegation — actioned by **DP2-M1** directive-M restructure v1.7.116) + **DP2-11/-27** (frozen-commit repro) + Zenodo-DOI = PROCESS-NIT (OPEN-VENUE editorial; real GitHub repo cited, DOI pending-at-camera-ready per DP2-31.5). No content correction. ledger_match 0.25 UNMATCHED — Opus-adjudicated. NOT genuinely-new. |

**ChatGPT: 0 genuinely-new.** REJECT on byte-unchanged v1.7.116 = maximal-harsh structural referee floor
(DP2-24). Closing again concedes −35/16 is "plausible." Item set 1:1 with M15/M23/M31/M34.

---

## Bottom line

- **Genuinely-new findings this round: 0** (Grok 5 MIN → all re-flag/nit; ChatGPT 7 MAJ + 2 MIN → all re-flag/nit).
  - Grok: 0 GENUINELY-NEW · 5 RE-FLAG · 0 PROCESS-NIT (+ 1 parsed header non-finding).
  - ChatGPT: 0 GENUINELY-NEW · 8 RE-FLAG · 1 RE-FLAG+PROCESS-NIT (#9 Zenodo-DOI leg).
- The two task-flagged cruxes CONFIRMED NON-NEW: **ChatGPT #2** = the standing −35/16-vs-−35/8 / +(99/128)-sign
  disposition (DP2-01/-03/-16/-25), the "−305/64 vs −35/8 different pages" is the DELIBERATE disclosed
  distinction (transcribed-polynomial reduction vs Cai's separately-printed literature value), NOT a new
  math error. **ChatGPT #4** = DP2-13 load-bearing cubic-transmission caveat, a disclosed OOM estimate, NOT
  a newly-surfaced correctness gap.
- **No bump** (v1.7.116 stands); `directive_g.sh` NOT run (no edit).
- **Clean-wave streak 14 → 15 HOLDS.** (M34 closed at 13→14; M35/M36 had no P2 leg, so M37 is the next P2
  wave — a clean M37 advances 14→15.)
- **Integrity:** both raw verdicts (Grok MINOR / ChatGPT REJECT) READ verbatim before recording; every
  finding dispositioned with a source-cited D-id; the ChatGPT convention crux re-falsified by RE-RUNNING
  the committed `p2_vertex_check.py` + convention-free Li formula. No ACCEPT faked, no finding dismissed
  without a source-cited verdict, no math fabricated.
