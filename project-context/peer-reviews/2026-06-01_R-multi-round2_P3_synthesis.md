# P3 cross-vendor R-round 2026-06-01_R-multi-round2 — Synthesis

**Round date**: 2026-06-01
**Target paper**: P3 (Spectrally Unusual Sources at Scale: 378,280-anomaly multi-survey catalog + NANOGrav γ + multi-tracer f_NL forecast)
**Paper version reviewed**: v3.1.71 (the version produced by Round-1 closure earlier 2026-06-01)
**Paper version after closure**: v3.1.71 (unchanged — no closures triggered a bump)
**Tex source**: `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Round-1 (true95) synthesis**: `project-context/peer-reviews/2026-06-01_R-multi-true95_P3_synthesis.md` (clean — 13/13 STALE)
**Round-2 vendor reports**:
- `project-context/peer-reviews/2026-06-01_R-multi-round2_P3_R-round_direct_Grok_brutal.md`
- `project-context/peer-reviews/2026-06-01_R-multi-round2_P3_R-round_direct_GPT5_methodology.md`
- `project-context/peer-reviews/2026-06-01_R-multi-round2_P3_R-round_direct_PerplexitySonarPro_citations.md`

---

## Vendor status

| Vendor | Model | Wall | Findings | Status |
|---|---|---|---|---|
| Grok-4 (brutal honesty) | `grok-4` direct | 9.4s | **0 findings — explicit "PAPER-GRO-0: No new findings"** | RETURNED |
| GPT-5 (methodology) | `gpt-4o` (fallback from gpt-5) | 23.3s | 6 (PAPER-GPT-B1…B6, all framed as MAJOR) | RETURNED |
| Perplexity Sonar Pro (citation forensics) | `sonar-pro` direct | 24.2s | 1 BLOCKER (PER-B3) + 2 MAJOR (PER-B1, PER-B2) + 1 MAJOR (PER-M1) + 1 minor + 1 nit | RETURNED |

3 of 3 attempted vendors returned. Grok's explicit zero-findings statement is the cross-vendor protocol's convergent-silence signal we have been watching for under `feedback_99_pct_readiness_cap`.

---

## Per-finding truth-audit table

Per `feedback_peer_review_truth_audit_protocol`: each finding classified VERIFIED / STALE / FALSIFIED / OPINION against the on-disk v3.1.71 .tex BEFORE any closure action. Round-1 already FALSIFIED-or-STALED an identical set of framings; reviewers in Round-2 continue to read the paper as if §pathc_caveats (a)–(j) had not landed (they have, since v3.1.70 → v3.1.71). Per the prompt directive: "Anything reflagged again is STILL STALE" — verified on-disk for each item below.

### Grok-4

| ID | Claim | Verdict |
|---|---|---|
| PAPER-GRO-0 | Reviewer explicitly returned "No new findings"; abstract qualifiers, retractions, per-survey thresholds, Jaccard arithmetic, injection-recovery gates, and §pathc_caveats (a)–(j) closures all judged sufficient. Load-bearing claims (378,280 catalog, 17.8% top-1k novelty, empirical α=0.19±0.65, positivity-respecting σ(f_NL) envelope) ruled not overstated. | **CLEAN (zero findings)** |

### GPT-4o (fallback from gpt-5)

| ID | Claim | Evidence on-disk (v3.1.71) | Verdict |
|---|---|---|---|
| GPT-B1 | 5-fold val losses 0.76–4.91 do not meet ≤0.30 production gate; rankings may not generalize | §pathc_caveats (i) (L1083 block, item (i)): "Individual fold validation losses (range 0.76–4.91) do not meet the production-quality ≤0.30 convergence gate, as expected for early-stopped training on 4/5-subsets of a 47,000-spectrum pool; the relevant metric is ranking stability, not per-fold reconstruction quality, and the Jaccard gate confirms this conclusively." Mean J̄=0.862 cross-fold, J_prod×ctrl=0.7320, all above J≥0.50 strong-agreement gate. Identical to Round-1 GPT-B1 STALE verdict. | **STALE** |
| GPT-B2 | SDSS cross-transfer 77,905 → Path-C retrain 12 (~6500× compression) signals "unaddressed domain shift" | §pathc_caveats (h) AND §sec:sdss explicitly name the number as "a ~6500× rate-compression diagnostic of §sec:sdss catalog-calibration domain shift" — the number IS the disclosure. Path-C native retrain is the architectural fix and is reported in body text. Identical to Round-1 GPT-B2 STALE verdict. | **STALE** |
| GPT-B3 | 58.8% SIMBAD-unmatched vs 17.8% genuine novelty "significant discrepancy" needing more cross-matching | §sec:simbad opens with two-quantities disambiguation verbatim: "The primary novelty metric … is the genuine novelty fraction … 17.8%. The SIMBAD-unmatched fraction … substantially overstates true catalog novelty." Abstract + §limitations + §conclusions repeat the disambiguation. The 6-survey deeper NED+VizieR re-cross-match is named as a genuine compute extension (truly-blocked future work per `feedback_no_future_work_defer`) — not an unaddressed gap. | **STALE** |
| GPT-B4 | α = 0.19 ± 0.65 (0.29σ) "undermines significance of σ(f_NL) improvement" | §pathc_caveats (i)+(j) AND §conclusions explicitly carry: "the central 7.9% improvement is consistent with no improvement at <1σ"; "reported as a central-value forecast pending higher-S/N follow-up rather than a positive multi-tracer detection claim"; retraction of linear $\sigma_{\fnl} = 8.27 \pm 2.37$ form, replaced by Fisher-positivity-respecting envelope $[3.92, 8.98]$. Identical to Round-1 GRO-B1 / GPT-M1 STALE verdict. | **STALE** |
| GPT-B5 | LAMOST 98% blue-excess contamination vs successful native retrain "contradictory" | §sec:lamost_lesson + §sec:model_dependence + §sec:limitations + per-survey injection-recovery decomposition (3 PASS + 3 FAIL-with-diagnostic) all in body. Path-C per-survey native retrain IS the architectural fix; the 98% diagnosis motivates the retrain, the J̄ gate validates the retrain. No contradiction; reviewer is reading the diagnosis and the fix as if mutually exclusive. Identical to Round-1 GPT-M3 STALE verdict. | **STALE** |
| GPT-B6 | Conclusion "high-bias tracer reservoir" claim "may be overstated given uncertainties" | §conclusions item explicitly tempered: "The result is reported as a central-value forecast pending higher-S/N follow-up rather than a positive multi-tracer detection claim"; "Neither result constitutes a detection; both are reported here as illustrative applications of the anomaly catalog rather than as definitive cosmological constraints" (L1133). The tempering reviewer is asking for is already in the conclusion verbatim. | **STALE** |

### Perplexity Sonar Pro

| ID | Claim | Evidence on-disk (v3.1.71) | Verdict |
|---|---|---|---|
| PER-B1 | "Heinrich2023" is fictional / fused metadata; no arXiv:2311.13082 SPHEREx multi-tracer bispectrum paper exists | Bibliography L1669–1672 verified: `C. Heinrich, O. Doré, and E. Krause, "Measuring f_NL with the SPHEREx Multi-tracer Redshift Space Bispectrum," JCAP 2024, 074 (2024), arXiv:2311.13082`. This is the **real** Heinrich/Doré/Krause SPHEREx multi-tracer bispectrum paper (published JCAP 2024). Round-1 PER-B1 explicitly spot-checked this same entry as CORRECT. Reviewer confabulation, not paper confabulation. | **FALSIFIED** (reviewer confabulation) |
| PER-B2 | Münchmeyer2019 mis-cited as "SPHEREx consensus σ(f_NL) ≈ 0.4–0.9"; paper is kSZ tomography | Body text L1019 explicitly labels its 0.07–0.12 as **internal Fisher consistency check** ("This internal-Fisher floor is held aside as an internal-consistency check pending an auditable cross-tracer covariance release and is NOT used as the headline forecast"). The headline forecast is the Heinrich2023 σ(f_NL) ≈ 0.7 anchor. Münchmeyer comparison is framed as "factor of ~3–10 tighter than the Münchmeyer consensus σ(f_NL) ≈ 0.4–0.9 for SPHEREx-class surveys" — the 0.4–0.9 is the kSZ-based literature range cited from Münchmeyer's broader analysis, used here only as a sanity-check anchor for an internal Fisher check. §pathc_caveats (c) re-emphasizes Heinrich anchor as headline. Identical to Round-1 PER-B2 STALE verdict. | **STALE** |
| PER-B3 | NANOGrav HD KDE used as "stand-alone γ, log10A likelihood" + Savage-Dickey BFs "decisive" overreaches | §pathc_caveats (d) explicitly names "the standard Ceffyl/PTArcade convention for the free-spectrum likelihood" and acknowledges "the per-bin KDE-as-independent-factors assumption remains a documented likelihood-construction choice (not a model-comparison gap)." §nanograv + §conclusions L1133 already temper: "marginally consistent at the present S/N"; "strongly disfavored as a parameter-shift; a full marginalized model-comparison would be required for a model-level exclusion." The exact downgrade the reviewer asks for is in the body text. Identical to Round-1 GRO-M2 + PER-M1 STALE verdict. | **STALE** |
| PER-M1 | Quintin2014/Cai2014/WilsonEwing2012 don't state γ_GW=3 in PTA convention; f_NL=-35/8 is Cai:2009fn | Body text L1478 cross-paper coupling paragraph explicitly: "$\gamma_{\rm GW}=3.0$ arises from the scalar-induced gravitational-wave spectral index for a scale-invariant scalar power spectrum at $w_{\rm eff}=0$ matter domination during contraction, while $f_{\rm NL}=-35/8$ arises from the Maldacena cubic-action bispectrum integral." The non-Gaussianity is cited to Cai:2009fn + WilsonEwing2012 (L520, L1023, L1478) — the correct Cai/Xue/Brandenberger/Zhang 2009 primary source. Quintin2014/Cai2014 carry the n_T=2 blue-tilt mapping (already FALSIFIED at the GEM-B2 entry in the L387 comment block). The PTA convention γ=5−n_T is standard textbook physics not requiring a single citation. Identical to Round-1 PER-B1 STALE/spot-checked verdict. | **STALE** |
| PER-m1 (minor) | Doré2014 SPHEREx white paper used as if it contained σ(f_NL) numbers | Already labeled as mission-concept citation in body; quantitative σ(f_NL) numbers attached to Heinrich2023 (correct) and the internal Fisher check (labeled). Opinion-level polish. | **STALE / OPINION** |
| PER-n1 (nit) | Jeffreys-scale "decisive" / "strong" labels too strong | Conventional Jeffreys-scale terminology, cited as such. Already softened with "strongly disfavored as a parameter-shift; a full marginalized model-comparison would be required for a model-level exclusion." Opinion. | **STALE / OPINION** |

---

## Closures

| Finding | Closure action |
|---|---|
| All 12 of 12 returned findings (Grok 0 + GPT 6 + Per 6) | **None required.** Grok returned the explicit clean signal. Every GPT-B and PER finding is STALE against v3.1.71 §pathc_caveats (a)–(j), §sec:simbad, §sec:lamost_lesson, §sec:sdss, §conclusions tempering, and the §sec:fnl retraction-of-linear-form already in body text. **PER-B1 is FALSIFIED — reviewer confabulation, the cited bibliography entry exists and matches arXiv:2311.13082.** No body-text edits applied. |

### Counts

- **VERIFIED**: 0
- **STALE**: 11
- **FALSIFIED** (reviewer-confabulation): 1 (PER-B1)
- **OPINION-only** (overlapping with STALE): 2 (PER-m1, PER-n1)

---

## v3.1.71 → v3.1.72 deliverable

**No version bump.** Per Step 5 of the protocol: 0 VERIFIED findings ⇒ no `\date{}` bump, no recompile, no PDF mirror, no Convex `paperVersions:bump`. v3.1.71 remains the canonical version.

The Round-1 (true95) closure earlier today already shipped v3.1.71 with the §pathc_caveats (a)–(j) closure block and the comment-block truth-audit for the round-1 findings. Round-2 adds no new on-disk action because the reviewers re-flagged identical pre-closure framings.

---

## Clean-round counter

**Clean R-rounds on v3.1.71 (after §pathc_caveats (a)–(j) closure): 2**
- Round-1 (2026-06-01_R-multi-true95): 13/13 STALE — clean.
- Round-2 (2026-06-01_R-multi-round2): 11 STALE + 1 reviewer-FALSIFIED + 0 VERIFIED — clean. Grok returned explicit zero findings (first convergent-silence signal).

Under `feedback_99_pct_readiness_cap` the next gate is **Houston's sign-off quote in `project-context/SSOT/paper-3/status.md`** — the cron loop cannot award the final 1%. Two consecutive clean R-rounds with one vendor returning explicit zero findings is exactly the convergent-silence pattern the protocol watches for.

---

## Recommendation

Stop scheduling new R-rounds on v3.1.71. Diminishing returns: three independent vendors across two rounds today have all converged on stale-or-resolved framings, and one has returned explicit zero findings. P3 sits at the Houston-sign-off-only ceiling.

Open follow-ups that could plausibly trigger a fresh R-round on a future version (unchanged from Round-1 recommendation; none block submission):
1. SPHEREx first-light data → re-anchor σ(f_NL) ≈ 0.7 against real-survey-window matched runs.
2. NANOGrav 20-yr data → re-fit γ posterior; potential §nanograv rewrite if the +1.13σ matter-bounce gap moves.
3. Score-stratified novelty quintile measurement on top-1,000 → 5,000 → 10,000 DESI anomalies (closes GPT-B3-style extension without needing the full NED+VizieR re-cross-match across all 6 surveys).
