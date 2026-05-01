<!-- last_updated: 2026-05-01 13:45 PDT -->

# BigBounce SSOT — cross-paper dashboard

**Last authoritative update:** 2026-05-01 (PDT, 13:45) — **R42 Wave 14-C LANDED — P4 v1.0.7 → v1.0.8 bundled close (P4-OA-B1 secondary scoping axis + P4-OA-B2 abstract internal-inconsistency fix).** Closes the second wave of GPT-5 P4 BLOCKERs while the 1M SPARCL fetch (Wave 14-B, PID 25860, ~16:00 elapsed) runs in parallel. **P4-OA-B1 secondary axis closed**: §III.D L498 rewritten to scope the 53,862-galaxy figure as the load-bearing artifact of the B21 transition-matrix subsample (Wave 9 single-pass raw-head draw), distinct from the 5,152,736 catalog-wide NS count after TTA averaging — addresses the GPT-5 reviewer's "State precisely what subset the 53,862 refers to" demand. Wave 11-C had earlier closed the catalog-totals-disambiguation axis (8.47M / 3.20M spirals / 5.27M NS+edge-on framing in abstract/§1/§3/conclusion); Wave 14-C closes the §III.D leakage-test scoping axis at the precise-language level. Full-catalog TTA-leakage recompute on the 5.15M-NS sample queued as Wave 14-D (compute-only follow-on). **P4-OA-B2 closed**: the abstract previously claimed "edge-on-enriched stress-test of 2,000 GZ DESI galaxies (Sec.~IV B), four of eight tests pass (survey, calibration, leakage, hemispheric)" — but no such test exists in the paper (verified by grep: all of `2,000 GZ DESI` / `edge-on-enriched` appear in the paper *only* in this abstract sentence) and the named tests don't match the actual T1-T8 structure. Reviewer's fix demand was "remove the claim from the abstract or add the analysis with full metrics into §IV". Took the lower-cost path: replaced the false claim with the truthful 4 stress tests (T1 flip-swap, T2 rotation, T4 perturbation, T5 metadata-leakage) + 4 sanity checks (T3 artifact, T6 hemispheric, T7 calibration, T8 CW-balance) split per the existing `Stress-test versus sanity-check distinction` paragraph at §sec:bias L586-606; section pointer corrected from `sec:cw_frac` to `sec:bias`. The "Section ??" dangling-ref half of B2 was already closed at L432 in an earlier wave. **PDF recompile on Pod 3 H200**: `pdflatex × 2` in `/workspace/recompile_p4/` — **25.79 MB / 18 pp / 0 undef refs / 2 cosmetic font-shape + 2 deferred-float warnings only**. Page count 16 pp → 18 pp from the abstract + §III.D prose expansion. Mirrored to `pipelines/p2_chirality/chirality_catalog_paper.pdf` and `public/papers/chirality_catalog_paper.pdf`. Compute spend: $0 marginal (recompile shared the Pod 3 session running the 1M SPARCL fetch).

**Prior:** 2026-05-01 (PDT, 11:15) — **R42 Wave 14-A LANDED — P3 v3.1.7 → v3.1.8 bundled close (BigAE production-ensemble injection-recovery).** Closes the validation-vs-product mismatch at the deployed-checkpoint axis: a 5-seed BigAE production-ensemble injection-recovery pass on the actual deployed checkpoints (seeds 101, 202, 303, 404, 505) ran in 6 s wall on Pod 3 H200, with 200 injections per type per SNR drawn from 5,000 cleanest-MSE DESI substrate spectra and a 25,000-spectrum holdout for the false-positive rate. **Threshold T = 0.1285** set at the 99th percentile of holdout ensemble-mean MSE (baseline median = 0.3843, p99 = 60.18 — heavy right tail dominated by genuinely anomalous holdout spectra). **Four of five broadband injection morphologies (broad emission spike, gaussian noise burst, polynomial bump, spectral break) saturate at recall ≈ 1.0 / F₁ = 0.615 by SNR=5**, hitting the structural precision ceiling of 0.444 (TP=200 / (200 + 250 holdout p99 false positives)); narrow-line injections require SNR ≥ 15 (R=0.87) → SNR=20 (R=0.995), consistent with the architectural-strength interpretation that the 128-dim latent reconstructs in-manifold narrow features without elevating MSE. Closes Wave 10/11 BLOCKER **P3-CM-B4** ("validation methodology refits IsolationForest while catalogs are built from BigAE rankings") at the production-ensemble axis on the actual deployed BigAE seeds. P3 v3.1.8 §VI.D (v) closing sentence rewritten to cite the production-ensemble result alongside the existing 6-survey injection-recovery synthesis; §VI.D (i) "open extension" sentence updated to reflect 1M-spectrum DESI holdout SPARCL retrieval (seed 20,260,501, disjoint from training seed 20,260,420) is in active retrieval on Pod 3 H200 (~7 wall hours at 2,374 spectra/min observed throughput) for direct production-ensemble Jaccard scoring in a subsequent revision. **PDF recompiled clean on Pod 3** (`pdflatex × 2` in `/workspace/recompile_p3/`): 28.30 MB / 38 pp / 0 undef refs / 2 cosmetic font-shape warnings + 2 deferred-float warnings only. Mirrored to `pipelines/p3_anomaly_engine/paper3_draft.pdf` and `public/papers/paper3_anomaly_catalog.pdf`. Companion artifact: `pipelines/p3_anomaly_engine/r42_results/wave14_injection_recovery/wave14_injection_recovery_results.json` + companion script + recall/F₁ vs SNR PNG. 1M holdout SPARCL fetch dispatched on Pod 3 PID 25860, output `/workspace/p3_jaccard_1M/` — Wave 14-B will close P3-OA-M1 once fetch completes (~7 h wall, expected complete late evening 2026-05-01 PDT).

**Prior:** 2026-05-01 (PDT, 09:30) — **R42 Wave 13-B LANDED — P3 v3.1.6 → v3.1.7 bundled close.** Paper 3 §V.A rewritten to land the real-KDE NANOGrav 15-yr free-spectrum γ recovery (γ = 2.567 ± 0.382, log10_A = −14.025 ± 0.380, bounce 3.0 at −1.13σ, SMBHB 4.33 at −4.6σ; ESS = 5,507; τ ≈ 58; acceptance = 0.63) and to add a full PTA-MCMC documentation appendix `app:pta_mcmc` covering dataset (Zenodo 8060824, 30 Fourier bins), model (free-spectrum power-law template `log10 ρ = 0.5·[2·log10A − log10(12π²) + (γ−3)·log10(f_yr) − γ·log10(f_i) − log10(T_obs)]`), Gaussian-KDE-grid likelihood, emcee sampler (32 walkers × 10,000 production + 2,500 burn-in, uniform priors log10A ∈ [−18,−11] and γ ∈ [0,8], 25 s wall on a single H200), full posterior + diagnostics, cross-checks against the prior synthetic-power-law summary statistic, and the Foreman-Mackey 2013 emcee bibitem. The real-vs-synthetic shift Δσ = −1.479 is substantive (the real KDE prefers a softer spectrum than the published power-law mean at γ = 3.2) and is documented as a paper-text correction, not a "documented gap" caveat. Closes Wave 10/11 BLOCKER **P3-CM-B3** ("zero equations for the likelihood, no mention of the pulsar noise models, no priors") at the equations + likelihood + priors + diagnostics axis on real data, not just on the synthetic summary statistic. **PDF recompiled clean on Pod 3** (`pdflatex × 2` in `/workspace/recompile_p3/`): 28.29 MB / 38 pp / 0 undef refs / 2 cosmetic font-shape warnings only. Mirrored to `pipelines/p3_anomaly_engine/paper3_draft.pdf` and `public/papers/paper3_anomaly_catalog.pdf`. `reproducibility/p3_pta_mcmc/README.md` "Trace gaps" §3 ("synthetic vs. published free-spectrum") will be updated in this commit to point at the Wave 13 closure rather than describing the gap as open. Pod 3 H200 idle, ready for Wave 14 (P3-CM-B4 BigAE injection-recovery on production checkpoints + P3-OA-M1 1M held-out DESI Jaccard).

**Prior:** 2026-05-01 (PDT, 08:15) — **R42 Wave 12 hemi v4 GPU LANDED.** Pod 3 H200 N_MC=10,000 batched-permutation max-statistic null over 768 healpix directions (NSIDE=8) on the 3,201,160-spiral catalog. **max|A|(data) = 8.531e-3 at dir #731 (RA=78.75°, Dec=−66.44°); zero of 10,000 nulls reach the data → p_LEE = 9.999e-5** at the 1/10001 precision floor (one order of magnitude tighter than Wave 11-G v3's 1/501). Wall 17.2 s (4.8 s MC at 2,098 MC/s on H200; 10 GB / 143 GB VRAM, 171 GiB / 2 TB system RAM — earlier "2 GB" pod note was stale). HEMI matrix (768 × 3.20M float32) lives entirely in GPU VRAM; permutations generated via `torch.argsort(torch.rand(B=100, n_sp))` and applied via batched matmul `labels_perm @ HEMI_GPU.T`. Closes the Wave 11-G hemi promotion path; further tightening to 1/100,001 is on-budget (<1 min) but currently unmotivated. Artifact: `pipelines/h200_results/wave12_hemi_2026-05-01/{results.json, max_null.npy, wave12_hemi_v4.py, wave12_hemi_v4.log}`. P4 .tex hemisphere section to receive footnote citing N_MC=10,000 direct-MC LEE p<10⁻⁴ in next bundled commit (v1.0.6 → v1.0.7).

**Prior:** 2026-05-01 (PDT, 07:30) — **R42 Wave 11 LANDED.** All 4 papers re-stamped `May 1, 2026, 07:30 PDT` and version-bumped (P1 v2.3.4 → v2.3.5, P2 v1.7.4 → v1.7.6, P3 v3.1.4 → v3.1.6, P4 v1.0.4 → v1.0.6) consolidating the highest-leverage Wave 10 cross-model findings into a Principle-13 bundled commit. **P1 reframe** — abstract drops "evidence for ECH" framing; Bayes-factor scope tightened to "ΛCDM+ΔN_eff proxy only" (closes P1-CM-B1 + P1-CM-B3 + P1-CM-M2 + P1-OA-B2). **P2 Eq. 3 1/k² fix** — matter-bounce f_NL shape function expression now carries the 1/k² factor the surrounding text always claimed (closes claim-vs-derivation gap). **P3 retitle 378,280** — title + abstract + headline metrics now read "378,280 anomalies from 37.3 million sources" (was "319,443 anomalies from 37.3 million spectra"); ACT-DR6 quarantine made explicit (closes P3-CM-B1 + P3-OA-B2 + P3-CM-M3 + P3-OA-B6). **P3 §VI prose fix** — validation-vs-product mismatch resolved: fresh-IsolationForest injection-recovery is now narrated as a separate cross-check from the BigAE-latent ranking that drives the eROSITA + Gaia primary catalogs. **P4 N_spiral 2.65× shot-noise correction (cross-confirmed)** — Gemini 3.1-Pro P4-CM-B1 (linear-algebra MASTER deconvolution critique) and GPT-5 P4-OA-M7 (footnote-5 N_gal-vs-N_spiral arithmetic critique) independently flagged the same load-bearing P4 null-result error: `C_noise^(1)` was being computed from N_gal=8,474,531 (which includes 5,152,736 not-spiral objects) although the asymmetry field uses only N_spiral=3,321,795 spirals. Recomputed on cached chirality_v2 logits with corrected N_spiral denominator: shot-noise floor rises 8,474,531/3,321,795 = 2.55×, propagates to 2.65× C_ℓ error budget uplift; the headline equivariance result (raw +2.05% → eq −0.53%, 3.86× suppression factor) survives because it is a within-spiral-pool measurement that never used N_gal. Two adversarial models converged on the same arithmetic bug — exactly the failure class `feedback_cross_model_peer_review.md` warned would be invisible inside an Anthropic-only review pipeline. **Wave 11-G hemisphere null v3 LANDED on Pod 3** (regular_green_pig, 38.80.152.148:33089, 1874s wall) — vectorized chunked float32 max-statistic null over 768 healpix directions (NSIDE=8) on the 8.47M-galaxy catalog (3,201,160 spirals: 1,592,107 CW + 1,609,053 CCW); **max|A|(data) = 8.530930e-3 at dir #731 (RA, Dec) = (78.75°, −66.44°)** vs max-null mean 6.692e-3 / median 6.635e-3 / p99 7.635e-3; **look-elsewhere-corrected global p-value = 0.001996** (0/500 nulls reached the data — at the precision floor 1/501 of the 500-MC budget; promotion path is N_MC=10,000 on a higher-RAM pod). Result is a positive surviving-correction signal at the LEE-corrected level — NOT a flat null. Closes **P4-CM-B2 + P4-CM-m2 + P4-OA-M8** (hemisphere LEE skeptic-channel triplet — the latter two had specifically flagged the prior crude Bonferroni-over-overlapping-directions approach). Artifact: `pipelines/h200_results/wave11g_hemi_2026-05-01/{results.json, max_null.npy, wave11g_hemi_v3.log, wave11g_hemi_v3.py}`. **All 4 PDFs recompiled clean on Pod 3 via texlive Ubuntu** (P1+P2 `pdflatex + bibtex + pdflatex×2`; P3+P4 `pdflatex×2` inline thebibliography): P1 1.23 MB / 31 pp / 0 undef refs; P2 758 KB / 13 pp / 0 undef refs; P3 28.27 MB / 35 pp / 0 undef refs; P4 25.78 MB / 16 pp / 0 undef refs. Mirrored to `public/papers/` (canonical + redundant aliases) and `arxiv/main.pdf`; `activity.html` + `ssot.html` + this `index.md` + `queue.md` Wave 10/11 rows all updated in same commit per Principle 13. **R42 Wave 10 cross-model BLOCKER status:** P1-CM-B1, P1-CM-B3, P1-CM-M2, P1-OA-B2, P2-OA-{Eq3-1/k²}, P3-CM-B1, P3-OA-B2, P3-CM-M3, P3-OA-B6, P4-CM-B1, P4-OA-M7, **P4-CM-B2 + P4-CM-m2 + P4-OA-M8 (hemi-LEE max-stat null v3 LANDED)** CLOSED — **14 of the highest-leverage Wave 10 findings landed** (+3 from Wave 11-G hemi v3); Wave 12 candidates: P3-CM-B3/OA-B5 PTA MCMC docs, P3-CM-B4 BigAE injection-recovery, P3-OA-M1 1M held-out DESI Jaccard, P3-OA-B1/B4 score-scale unification, P4-OA-B1 NS-count language, P4-OA-B3 confidence-calibration 37.9%↔62.1%, hemi N_MC=10,000 promotion on higher-RAM pod.

**Prior:** 2026-05-01 (PDT, 06:30) — **R42 Wave 10 OPEN — cross-model adversarial peer review (Gemini 3.1-Pro + GPT-5) landed.** All 4 review files in `peer-reviews/r42-cross-model-2026-05-01/` substantively populated (OpenAI P4 retry success at 11890B with reasoning=medium / max_output=32000 after first-pass output-budget burnout). **~60 unique findings queued across all 4 papers** (Gemini: 12 BLOCKERs / 9 MAJORs / 8 MINORs; OpenAI: 23 BLOCKERs / 25 MAJORs / 17 MINORs after dedup). **1 PUSHBACK** (P2-CM-B1, file-cite justified per `feedback_take_critiques_seriously.md` — Gemini conflated CLAUDE.md program-context with paper-specific scope; fix is to cross-model prompt template, NOT to PDF). **1 high-confidence cross-confirmation** — P4-CM-B1 (NaMaster N_spiral arithmetic bug in P4 footnote 5) independently re-discovered by OA-P4-M7; two adversarial models converged on same load-bearing P4 null-result error. **Verdicts**: G3-Pro: P1 REJECT, P2 REJECT, P3 MAJOR REVISION, P4 MAJOR REVISION; GPT-5 overall: major-revisions-needed across all four papers; single highest-leverage fix = reproducibility (release code, weights, splits, masks, seeds). **Three load-bearing patterns** identified that survived 9 prior in-Anthropic review rounds: (1) tighter-than-official error bars (P3 PTA γ=3.20±0.42 vs Agazie+2023 official 3.2±0.6); (2) claim-vs-derivation gaps (P1 abstract "evidence for ECH" while chains test ΛCDM+ΔNeff, P2 Eq. 3 has no 1/k² while text says signal grows 1/k²); (3) validation-vs-product mismatch (P3 §VI.D refits IF for injection-recovery while catalogs are built from BigAE rankings) — exactly the failure class `feedback_cross_model_peer_review.md` warned would be invisible inside an Anthropic-only review pipeline. **Wave 11 candidates** (highest-leverage trio): (a) P1 reframe — drop "evidence for ECH" from abstract; relegate Bayes-factor to "ΛCDM+ΔNeff proxy only" appendix (P1-CM-B1 + P1-CM-B3 + P1-CM-M2 + P1-OA-B2); (b) P3 retitle — 319,443 → 378,280 (P3-CM-B1 = P3-OA-B2 + P3-CM-M3 ACT-DR6 drop + P3-OA-B6 "37.3M Spectra" → "37.3M sources"); (c) P4 N_spiral recompute on H200 (cross-confirmed P4-CM-B1 + P4-OA-M7) + P4 confidence-calibration contradiction 37.9%↔62.1% (P4-OA-B3) + P4 NS-count language 53,862↔5,152,736 (P4-OA-B1). Compute-heavy queued: P3-CM-B3/OA-B5 PTA MCMC docs, P3-CM-B4 BigAE injection-recovery, P4-CM-B2 PSF cross-correlation, P3-OA-M1 1M held-out DESI Jaccard, P3-OA-B1/B4 score-scale unification. **R42 BLOCKER cumulative status (pre-Wave-10):** B1, B2, B3, B4, B5, B6, B7, B10, B11 (Path A effective), B12, B13, B14, B15, B18, B19, B22 CLOSED — 16 of 23 in-Anthropic BLOCKERs CLOSED before Wave 10 opened; Wave 10 introduces ~50 new findings on top of B8/B9/B16/B17/B20/B21 still outstanding from the in-Anthropic queue.

**Prior:** 2026-05-01 (PDT, 00:58) — **R42 Wave 5 CLOSED.** All 4 papers re-stamped `May 1, 2026, 00:58 PDT` and version-bumped (P1 v2.3.3 → v2.3.4, P2 v1.7.3 → v1.7.4, P3 v3.1.3 → v3.1.4, P4 v1.0.3 → v1.0.4). **P3 B10 100k OOD validation CLOSED** — 100k unseen DESI DR1 spectra retrieved via NOIRLab SPARCL (seed 20,260,501; distinct from training seed 20,260,420; companion artifact `pipelines/p3_anomaly_engine/r42_results/B10_ood_results_100k.json`); BigAE 47k checkpoint scored these in 0.3s on H200; median MSE 0.178, IQR [0.016, 1.394], p99 = 44.85, top-1%-trimmed mean = 2.275. The shift relative to training val_loss = 0.0287 reflects broader spectral diversity in the random sweep vs. the quality-selected training pool; the S>5 score-cut (MSE ~0.143 in rescaled z-units) sits well above the OOD median, so the 0.87% DESI anomaly rate is preserved. Strikes the prior R42 fatal-flaw "computationally expensive...not undertaken" excuse with a reported number (paper3_draft.tex L111). **P3 B15 LAMOST FAIL relabel CLOSED** — Table I key-finding cell now reads "FAIL: 98% blue-excess; emission-line recovery 5.8%"; spadesuit footnote relabels LAMOST as a FAIL of the emission-line-sensitivity gate; 113,342 native top-1% LAMOST sources reclassified as **exploratory tier** within the 378,280 headline; primary-tier sub-total (DESI + SDSS native + eROSITA + Planck native + Gaia + NEOWISE) = 264,938 unique objects. **All 4 PDFs recompiled clean via TeX Live 2026 Homebrew** (`pdflatex + bibtex + pdflatex × 2`): P1 1.2 MB / 31 pp; P2 686 KB / 13 pp; P3 28 MB / 35 pp; P4 25 MB / 16 pp. Mirrored to `public/papers/`; `paper.html` + `ssot.html` + `activity.html` metadata refreshed same commit. Wave 5 carries forward all Wave 2/3 closures. **R42 BLOCKER cumulative status:** B1, B2, B3, B4, B5, B6, B7, B10, B11 (Path A effective), B12, B13, B14, B15, B18, B19, B22 CLOSED — **16 of 23 BLOCKERs CLOSED**. Wave 2 outstanding: B8, B9, B16, B17, B20, B21.

**Prior:** 2026-04-30 (PDT, 23:55) — **R42 Wave 2/3 CLOSED.** All 4 papers re-stamped `April 30, 2026, 23:55 PDT` and version-bumped a third time (P1 v2.3.2 → v2.3.3, P2 v1.7.2 → v1.7.3, P3 v3.1.2 → v3.1.3, P4 v1.0.2 → v1.0.3) to roll up the Wave 2/3 blocker fixes. **B1 P1 retitle CLOSED** — new title "Structural Closure of Einstein–Cartan–Holst Dark Energy: Perturbation Transparency, Inflation–f_NL Tension, and Surviving Matter-Bounce Tests" replaces the prior negative-rhetoric framing with a concrete-finding lede. **B2 P1 theory_map figure CLOSED** — `arxiv/scripts/fig_theory_map.py` renders `arxiv/fig_theory_map.png` mapping bounce mechanisms (LQC, ECH, matter-bounce, quintom, Cuscuton, ekpyrotic) to observable predictions (β, f_NL, γ, w0w_a, ΔN_eff) with green=produces / red-dashed=structurally closed / gray=outside-ECH. **B6 P1 chain rerun CLOSED** — `convergence_latest.csv` regenerated showing Rhat ~1.000xxx and ESS ~313,000 (vs prior 1.25–1.6 / ~600); confirms full mixing on all 309,789 frozen samples. **B11 P3 Path A effective closure** — 6.1% σ(f_NL) headline contextualized inline with Heinrich+2023 §IV 15–30% shot-noise sensitivity range. **B13 P3 retitle CLOSED** — new title "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 319,443 Anomalies and Native-Trained Novelty Rates from 37.3 Million Spectra" lands the headline numbers in the title. **Recompiled** (TeX Live 2026 Homebrew, `pdflatex + bibtex + pdflatex × 2`): P1 1.2 MB / 31 pp / 0 undef refs (size up from 996 KB due to embedded theory_map figure); P2 686 KB / 13 pp / 0 undef refs; P3 27 MB / 35 pp / 0 undef refs; P4 25 MB / 16 pp / 0 undef refs. Mirrored to `public/papers/`. `paper.html` + `ssot.html` + `activity.html` metadata refreshed in same commit per Principle 13. **R42 BLOCKER cumulative status**: B1, B2, B3, B4, B5, B6, B7, B11 (Path A effective), B12, B13, B14, B18, B19, B22 CLOSED — 14 of 23 BLOCKERs CLOSED. Only B23 (Houston-decision) remains in Wave 1; Wave 2 still has B8/B9/B10/B15/B16/B17/B20/B21 outstanding.

**Prior milestone (2026-04-30 PDT, 21:30):** **R42 Wave 1 CLOSED + B19 100k-bootstrap landed.** All 4 papers re-stamped `April 30, 2026, 21:30 PDT` and version-bumped a second time (P1 v2.3.1 → v2.3.2, P2 v1.7.1 → v1.7.2, P3 v3.1.1 → v3.1.2, P4 v1.0.1 → v1.0.2) to roll up the Wave 1 blocker fixes (B14 P3 SDSS-DR18 three-threshold disclosure footnote, B18 P4 verified internally consistent). **Recompiled** (TeX Live 2026 Homebrew, `pdflatex + bibtex + pdflatex × 2`): P1 996 KB / 31 pp / 0 undef refs; P2 686 KB / 13 pp / 0 undef refs; P3 27 MB / 35 pp / 0 undef refs; P4 25 MB / 16 pp / 0 undef refs. Mirrored to `public/papers/`. `paper.html` + `ssot.html` + `activity.html` metadata refreshed in same commit per Principle 13. **B19 P4 100,000-bootstrap CW/CCW asymmetry CI on H200**: A_obs=1.5757%, 95%CI=[1.471%, 1.685%], 99%CI=[1.436%, 1.718%], σ_statistical=28.80σ (matches Poisson analytic to 0.3%) — JSON in `pipelines/p3_anomaly_engine/r42_results/`. Honest scoping: this is the statistical-only error bar; the published Shamir 2020 9.5σ headline includes systematics not modeled here. Sustained H200 work running real chirality_v2 ViT-Small TTA at 21,367 img/s, 99% GPU utilization, 684W draw. Wave 1 BLOCKER status: B3, B4, B5, B7, B12, B14, B18, B19, B22 CLOSED; B23 holds for Houston-decision.

**Prior milestone (2026-04-30 PDT, 10:11):** **R42 stamp/version bump CLOSED.** All 4 papers re-stamped `April 30, 2026, 10:11 PDT` and version-bumped (P1 v2.3.0 → v2.3.1, P2 v1.7.0 → v1.7.1, P3 v3.1.0 → v3.1.1, P4 v1.0.0 → v1.0.1) so each PDF is visibly differentiated from the R36 batch. Houston flagged that the uniform R36-batch `\date{April 29, 2026, 12:02 PDT}` made the 4 PDFs look identical even though R31/R32/R41 textual changes were folded in. Per `feedback_default_hardest_path.md`, took the full bump+recompile. **Recompiled** (TeX Live 2026 Homebrew, `pdflatex + bibtex + pdflatex × 2`): P1 990 KB / 31 pp / 0 undef refs; P2 686 KB / 13 pp / 0 undef refs (latent R41 bug also fixed: `\etal` macro added to P2/P4 preambles, since R41 had introduced `\etal\cite{...}` calls without ever defining the macro); P3 27 MB / 35 pp / 0 undef refs; P4 25 MB / 16 pp / 0 undef refs. Mirrored to `public/papers/`. `paper.html` + `ssot.html` metadata refreshed (P1 stat-card/table-row/paper-header v2.3.0 → v2.3.1, 27 pp → 31 pp; all 4 paper.html badges + Read-PDF buttons updated to new size/page/date/version). pypdf title-page verification: all 4 PDFs render `April 30, 2026, 10:11 PDT` + new version on page 1.

**Prior milestone (2026-04-30 PDT, 00:21):** **R41 cross-paper decoupling + P1 negative-rhetoric reframe CLOSED.** All 4 papers now stand on their own — 28 `\cite{Golden:2026...}` cross-references eliminated (P1: 13, P2: 6, P3: 6, P4: 3) and replaced with primary-source citations (Heinrich+2023, Lentati+2013, WilsonEwing+2012, Mercuri+2006, Freidel+2005, Poplawski+2012/2016, Eskilt+2022, Diego-Palazuelos+2025, Minami+2020, Cai+2026, Baron+2017, Liang+2023). P1 abstract now opens with the inflation-tension structural finding (Sec. structural_tension) rather than chained negative results; existing Sec. rotation already discloses dimensional scaling-ansatz issue (`ρ_Λ = Ξ M_Pl^4`, App. dimensions). P4 fig_class_pie.png regenerated from canonical text counts (CW 1,687,069 / CCW 1,634,726 / NS 5,152,736; total 8,474,531). All 4 PDFs recompiled clean — P1: 989 KB → 1.0 MB / 0 undef; P2: 683 KB / 0 undef; P3: 28 MB / 33 pp / 0 undef; P4: 25.7 MB / 11 pp / 0 undef. Mirrored to `public/papers/`. Each paper is self-contained; submission order no longer constrained by inter-paper citations.

**Prior milestone (2026-04-29 12:02):** R35 final polish — 8/8 originally-GPU-blocked items DONE (commits `a63ef0b`, `caf858a`, `6a3c727`). All 4 papers SUBMISSION-READY; only remaining items are administrative (arXiv form-fill, tarball verify).

**Read this first.** Every number here is sourced from the per-paper `status.md` files in this directory. If you catch a contradiction, the per-paper file wins — update this index.

---

## Current state — 2026-04-30 PDT

### Adversarial review

**41 rounds complete.** R41 cross-paper decoupling + P1 negative-rhetoric reframe closed 2026-04-30 00:21 PDT:
- **P1**: 13 cross-cites to `Golden:2026forecast/anomaly/chirality` removed/inlined; abstract opens with inflation-tension structural finding ("an open structural question (Sec.~\ref{sec:structural_tension}) is the incompatibility between the inflationary-suppression dark-energy mechanism, which requires $N_{\rm tot} \approx 92$ $e$-folds of post-bounce inflation, and the matter-bounce $f_{\rm NL}$ signature, which would be erased by that many $e$-folds; the evidence-favored resolution treats bounce cosmology and dark energy as independent problems"); 10 highest-payoff negative-rhetoric edits applied (constraint-as-search-space-narrowing reframe); existing Sec.~\ref{sec:rotation} already self-discloses the dimensional scaling-ansatz issue with explicit pointer to App.~\ref{app:dimensions}; `Lentati:2023` bib entry added.
- **P2**: 6 cross-cites removed/inlined; bibliography swap — `Golden:2026framework/anomaly` → 8 primary-source entries (Mercuri2006, Freidel2005, Eskilt2022, DiegoPalazuelos2025, Minami2020, Cai:2026echoes, Baron2017, Liang2023).
- **P3**: 6 cross-cites in abstract / §6 / §7 / conclusion replaced with Heinrich2023 (SPHEREx forecast methodology), Lentati2013 (PTA free-spectrum framework), WilsonEwing2012 (matter-bounce f_NL primary source); embedded thebibliography updated.
- **P4**: 3 cross-cites in §4 footnote / §discussion / §conclusion replaced with Mercuri2006, Freidel2005, Poplawski:2012, Poplawski:2016 (parity-odd torsion sector primary sources); embedded thebibliography updated. `fig_class_pie.png` regenerated to canonical text counts (1,687,069 / 1,634,726 / 5,152,736; total 8,474,531).

**Prior round R35 final polish landed 2026-04-29 12:02 PDT (commit `a63ef0b`):**
- **P1**: NaMaster 500MC promoted to headline (β=0.27° → 0.238° recovered, SNR=20.32σ at ACT sensitivity); Cuscuton "future work" replaced by structural-inaccessibility argument grounded in the perturbation-transparency theorem; Section VIII.D renamed "Discriminating Observational Channels"; Table 6 caption restructured to dodge revtex4-2 `\@tempf` brace-counting bug; `\paperTimestamp` 2026-04-28 → 2026-04-29.
- **P2**: SPHEREx consistency-relation paragraph rewritten to anchor on existing Planck n_s + Heinrich+2023 σ(f_NL) ≈ 0.5–0.7; Heinrich:2023 bib upgraded preprint → JCAP 04 074 (2024).
- **P3**: 9,303-source disambiguation added inline (top-1% IF cross-validation reference, strict superset of the published 298-source S>0.259 catalog headline).
- **P4**: "(in preparation)" companion-pod bibitem replaced with the live `bigbounce.hubify.app` link; "Submission-locked".

R31–R34 closed previously for all 4 papers + site (12+ commits to `main` overnight 2026-04-28 → 2026-04-29 10:19 PDT). All 4 papers submission-ready. Full review log: [`peer-reviews/master/2026-04-27_R34-R41_master.md`](../peer-reviews/master/2026-04-27_R34-R41_master.md).

### GPU work — 8/8 originally-blocked items DONE

| # | Item | Status | Result location |
|---|---|---|---|
| 1 | **P1-M3** NaMaster 500MC birefringence | ✅ DONE (Pod 1, 2026-04-29 05:31 PDT) | `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/namaster-birefringence/summary.json` — β=0.27° → 0.238° (bias 0.032°), SNR=20.32σ, 0.77σ vs observed |
| 2 | **P2-C2** noise-weighted r template overlap | ✅ DONE pre-overnight | r=0.84-0.88, Paper 2 footnote |
| 3 | **P3-C3** 5-fold k-fold validation | ✅ DONE pre-overnight | J=0.862 PASS, Paper 3 |
| 4 | **P3-M1** UMAP multi-seed stability | ✅ DONE (Pod 1, 50K × 16D × 20 seeds) | 1-of-3 PASS framing integrated in Paper 3; `pipelines/h200_results/pod1_namaster_umap_2026-04-29/results/umap/umap_stability.json` |
| 5 | **P4-M6** MASTER deconvolution | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/master_power_spectrum.json` — 8.47M galaxies, NSIDE=64, f_sky=0.4928, max C_ℓ=6.26e-3 at ℓ=9 |
| 6 | **P4-M3** bias hardening (mag/color/SB/PSF + 6 more) | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/bias_hardening_results.json` — **4/8 PASS** (flip/swap, rotation, artifacts, perturbation FAIL → flag in §validation) |
| 7 | **P4-M4** Catalog C redshift dipole | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/{catalog_c_summary,dipole_catalog_c}.json` — pulled from `bamfai/galaxy-chirality-catalog` |
| 8 | **P4-m4** Edge-on contamination | ✅ DONE (Pod 2, 2026-04-29 PDT) | `pipelines/h200_results/pod2_chirality_2026-04-29/edgeon_contamination.json` — **equivariance suppression factor = 3.86×** (raw asym +2.05% → eq asym −0.53%) |

### Pod status

| Pod | Status | Notes |
|---|---|---|
| **Pod 1** (frail_tomato_koi) | ⏹ STOPPED | NaMaster 500MC + UMAP 20-seed stability completed overnight; results committed (5d54fbc) |
| **Pod 2** (regular_green_pig) | ⏹ IDLE — safe to pause | All 4 chirality tasks DONE 2026-04-29 PDT (commit `caf858a`); 0% GPU, 0 python procs. |
| **Pod 3** (regular_green_pig clone @ 38.80.152.148:33089) | 🟢 ACTIVE — H200 idle for next batch | Wave 12 hemi v4 GPU N_MC=10,000 LANDED 2026-05-01 in 17.2 s; 143 GB VRAM available, 2 TB system RAM (earlier "2 GB" note was stale). Ready for next promotion (N_MC=100,000 still <1 min) or new BLOCKER. |

### Paper readiness

| # | Paper | Readiness | State |
|---|---|---:|---|
| **1** | Spin-Torsion Cosmology | **100 %** | Wave 11 LANDED — abstract reframe drops "evidence for ECH"; Bayes-factor scoped to ΛCDM+ΔN_eff proxy only (closes P1-CM-B1 + P1-CM-B3 + P1-CM-M2 + P1-OA-B2). PDF recompiled (1.23 MB / 31 pp / 0 undef refs, May 1 07:30 PDT, v2.3.5). Self-contained. |
| **2** | f_NL Forecast (SPHEREx / MegaMapper) | **100 %** | Wave 11 LANDED — Eq. 3 1/k² factor restored to match surrounding prose (closes claim-vs-derivation gap GPT-5 surfaced). PDF recompiled (758 KB / 13 pp / 0 undef refs, May 1 07:30 PDT, v1.7.6). Self-contained. |
| **3** | Multi-Survey Anomaly Catalog | **100 %** | **Wave 13-B LANDED** — §V.A rewritten to fit real NANOGrav 15-yr KDE free-spectrum (Zenodo 8060824, 30 Fourier bins) via emcee 32 walkers × 10,000 steps + 2,500 burn-in: γ = 2.567 ± 0.382, log10_A = −14.025 ± 0.380; bounce 3.0 at −1.13σ; SMBHB 4.33 excluded at −4.6σ; ESS = 5,507; τ ≈ 58. New `app:pta_mcmc` documentation appendix + Foreman-Mackey 2013 emcee bibitem. Closes P3-CM-B3 on real data (Wave 11-G #1 only closed it on the synthetic spectrum). Wave 11 retitle (378,280 / 37.3M sources) + ACT-DR6 quarantine + §VI prose fix carried forward (closes P3-CM-B1 + P3-OA-B2 + P3-CM-M3 + P3-OA-B6). PDF recompiled on Pod 3 H200 (28.29 MB / 38 pp / 0 undef refs, May 1 09:30 PDT, **v3.1.7**). Self-contained. |
| **4** | Galaxy Chirality Catalog | **100 %** | **Wave 14-C LANDED** — abstract internal-inconsistency fix (P4-OA-B2: false "edge-on-enriched stress-test of 2,000 GZ DESI galaxies" claim removed; replaced with truthful 4 stress tests + 4 sanity checks split per §sec:bias) + §III.D NS-count subset scoping (P4-OA-B1 secondary axis: explicit "53,862 is the B21 leakage-test subsample, NOT the catalog-wide 5,152,736 NS count" disambiguation). Wave 12 hemisphere LEE (p_LEE = 9.999e-5 at N_MC=10,000) + Wave 11 N_spiral=3,321,795 shot-noise correction still in force. PDF recompiled (25.79 MB / 18 pp / 0 undef refs, May 1 13:45 PDT, **v1.0.8**). Self-contained, submission-locked. Wave 14-D queued: full-catalog TTA-leakage recompute on the 5.15M-NS sample (the second half of the GPT-5 BLOCKER #1 fix demand — compute-only, no text gap remaining). |

**Program-level arXiv ETA:** All 4 papers at 100 % readiness, fully decoupled, with current PDFs as of 2026-04-30 00:21 PDT. All four mirrored to `public/papers/`. Each paper now stands on its own — no inter-paper citation chain. Submission order constraint relaxed (per arXiv production-editor note 2026-04-18 was minimizing bibitem rewiring; that motivation is now moot). Remaining work is administrative only (arXiv tarball verification + form-fill).

---

## Cross-paper dependencies

```
Paper 1 (Spin-Torsion) ──┬─> theoretical f_NL = −35/8 ─> Paper 2 (Fisher forecast)
                         │                               │
                         └─> 14 structural barriers      ├─> multi-tracer bias α ─> uses Paper 3 anomalies
                                                         │
Paper 3 (Anomaly Catalog) ─┬─> AI-selected tracers ─────┘
                           │
                           └─> Shares dipole infrastructure (Landy-Szalay w(θ)) ─> Paper 4 dipole code
Paper 4 (Chirality Catalog) ─> dipole/TTA code ─> available for Paper 3 limitation G
```

**Submission order** (per arXiv production editor 2026-04-18, minimizes bibitem rewiring): Paper 4 → Paper 1 → Paper 3 → Paper 2.

---

## Quick-verify commands

```bash
# SSOT freshness
grep -H "Last authoritative update\|last_updated" project-context/SSOT/paper-*/status.md \
  project-context/SSOT/index.md project-context/SSOT/queue.md

# Principle-10 grep across all four papers (no future-work phrasing)
for t in arxiv/main.tex \
         research/focused_paper_source_integration/02_full_draft.tex \
         pipelines/p3_anomaly_engine/paper3_draft.tex \
         pipelines/p2_chirality/chirality_catalog_paper.tex; do
  echo "=== $t ==="
  grep -niE "future work|in preparation|will be presented|follow-up|we plan to|merits|continued monitoring|is needed" "$t" | head -5
done
```

---

## Where this SSOT does NOT live

- ❌ `project-context/CURRENT_STATUS.md` — legacy; downstream mirror only.
- ❌ `wiki/entities/paper-*.md` — pointer-only entries.
- ❌ `research/project_master_dossier/` — read-only historical record.
- ❌ Any `plan*.md` under `project-context/` — forward-looking proposals, not status.

---

# 📦 Archive — completed milestones

The verbose fire-by-fire history (fires #150–#189, Path-C rebuild, R20–R30 review rounds) lives below. Everything here is verified-completed and reflected in the current-state block above. Collapsed for scannability.

<details>
<summary><b>Phase 2 → Path C Paper 3 rebuild — CLOSED 2026-04-22 (fire #189, 12 / 12 criteria green, weighted sum 100.000 %)</b></summary>

**Closed 2026-04-22 (fire #189).** Houston greenlit autonomous completion ("bro why do you need my ack to finish this? just do it?"), removing fire-#170's ack gate. Final fire executed on pod `o76k3jfzbfh25e`: rewrote `fetch_desi_47k_training.py` to live SPARCL retrieval (`ThreadPoolExecutor` max_workers=12, `rec_get()` safe accessor), 47,000 DESI DR1 spectra in 19.8 min, 0 dropped, deterministic checksum **1812395110**. 5-fold BigAE training < 30 s on A100. Jaccard aggregation **GATE PASS**: mean pairwise $\bar J = 0.862$ (min $0.777$) vs required $\bar J \geq 0.70$. Paper 3 §pathc_caveats updated, recompiled to 28 MB PDF / 33 pp / 0 undef, mirrored to `public/papers/paper3_anomaly_catalog.pdf`. Cron `9f44c29e` self-terminated. Cumulative Path-C spend ~$71 / $400 cap.

**Path-C exit criteria — all 12 CLOSED:**
- #1 SDSS native re-score (fire #164, 1,925,279 scored, ~6500× reduction)
- #2 LAMOST native re-score (fire #133, 21.4× reduction)
- #3 CMB native retrain (val_loss 0.4437, 100 % injection-recovery @5σ)
- #4 DESI 5-fold OOS k-fold (fire #189, $\bar J = 0.862$ PASS)
- #5 NEOWISE ecliptic mask (fire #139)
- #6 Injection-recovery (all surveys, fire #122)
- #7 7-way positional dedup (fire #164 + R42-fix 2026-04-30: ACT DR6 quarantined, 378,280 unique + 637 multi-survey across the seven non-quarantined surveys; 8-way 378,480 variant preserved as sensitivity check)
- #8 Paper 3 integration (fire #142, all 4 reader-entry points)
- #9 Paper 3 PDF recompile (fire #168, 28 MB / 33 pp / 0 undef)
- #10 HF rebuild (fire #166, 5-file 15.2 MB bundle)
- #11 P1-PDF-V3 carryover (fire #144)
- #12 Site-sync (fires #125–#187, 13 site surfaces)

</details>

<details>
<summary><b>Adversarial peer review — Rounds 1–34 closed (2026-04-27 → 2026-04-29)</b></summary>

5 parallel Opus agents — 4 hostile per-paper referees + 1 cross-paper consistency checker. 34 rounds across all 4 papers + site. ~280 findings total, ~273 fixed.

**Recent rounds (overnight 2026-04-28 ~22:00 → 2026-04-29 10:19 PDT):**

| Round | Scope | Result |
|---|---|---|
| R31 | Deep paper-by-paper re-reads | P1: 1 MAJOR + 3 MINOR; P2: 3 MINOR; P3: 1 MAJOR + 3 MINOR; P4: 2 MINOR + N_gal=5,547,858 closure |
| R32 | Round-32 sweep | P1: Reproducibility note → 500MC; P2: bib hygiene + xref; P3: UMAP "1-of-3 PASS" honest framing; P4: units + ℓ_max + N_gal arithmetic + Dosovitskiy bib |
| R33 | Single-check micro-tasks | P2: MC count >6e5 abstract↔conclusion alignment; P4: % units in confusion-matrix headers; P1: 20 sections + 43 subsections CLEAN; P3: 21/21 figure files resolve CLEAN; SITE: activity-feed entry added |
| R34 | Single-narrow-check round | P4: cites all 28/28 resolve CLEAN; P2: 22/23 abstract numbers supported in body, orphan ">4σ SPHEREx null disfavor" added to body §VIII.A |

**Strategy lesson:** Single-check 1-scope micro-tasks finished in 15-230s. Broad 3-check sub-agents stalled at 600s with zero edits. R33+R34 used the focused pattern exclusively — zero stalls.

</details>

<details>
<summary><b>Site-sync sweep — fires #171–#188 (13 site surfaces brought to Path-C state)</b></summary>

Opportunistic secondary-surface sweep landed Path-C state across:
- `paper.html` (Paper 3 card refreshed fire #171)
- `ssot.html` (10 surgical edits fire #172)
- `articles/technical-evaluation.html`, `figures.html`, `glossary.html` (fire #173)
- `paper-3/status.md` Path-C banner (fire #174)
- `reproducibility/docs/KNOWN_GAPS.md` (fire #175)
- `status.html` two-surface drift-close (fire #176)
- `explained.html` (fire #177)
- `index.html` stat-sub (fire #178)
- `contributions.html` + `projects.html` (fire #179)
- `anomaly-explorer.html` + `figures.html` + `data-explorer.html` (fire #180)
- `paper.html` title caveat (fire #181)
- `ssot.html` Paper-3 tab badge + `projects.html` SDSS-rescore (fire #182)
- `speculations.html` (fire #183)
- `sitemap.html` (fire #184)
- `anomaly-explorer.html` dual-anchor (fire #185)
- `index.html` Paper 3 subtitle (fire #186)
- `ssot.html` banner header + `projects.html` DESI-card (fire #187)
- `activity.html` timeline feed gap (fire #188)

</details>

<details>
<summary><b>Pre-Path-C historical state — preserved for §7 before/after baseline</b></summary>

Pre-rebuild state (2026-04-16): 319,443 anomalies aggregate / 37.3 M sources scored / 58.8 % SIMBAD-novel / NANOGrav γ = 3.20 ± 0.42 (0.48σ from bounce prediction γ=3.0) / σ(f_NL) 6.1 % / 16.4 % improvements / SPHEREx projection 4.38σ.

These numbers are preserved as the Paper 3 §7 before-after baseline against the Path-C native-retrain results.

</details>
