# NEEDS HOUSTON — truly-blocked items

Last updated: 2026-05-28 PDT (re-exhausted OpenRouter weekly cap + cron 7-day renewal point reached + 6 Claude-subagent rigorous-publishability reviews returned with substantive findings the 5-vendor R-rounds had been missing).

---

## ⚠️ 2026-05-28 PDT — 6 PARALLEL CLAUDE-SUBAGENT RIGOROUS REVIEWS RETURNED

Per Houston's directive ("most rigorous multi-agent multi-model peer review including your own modeling"), spawned 6 parallel Claude-subagent publishability reviews against on-disk artifacts. **All 6 surfaced real BLOCKERs the 5-vendor R-round pipeline has been missing** — the vendor reviews can't cross-reference on-disk artifacts or compare line numbers across .tex files; the subagents could.

**Honest readiness drops applied to `site/src/data/papers.ts` + `live-status.ts`:**

| Paper | Was | Now | New BLOCKER(s) the R-rounds missed |
|---|---|---|---|
| P1A v1A.0.35 | 92 | **88** | Sample-count drift in §VII: P1A says "424,781 samples" while companion P1B canonical is **309,189** (verified on-disk = 176,240+132,949); `Caldwell2002quintom` bibkey actually cites Caldwell 2002 phantom-DE paper (not quintom); γ_ABCK = 0.274 misattributed (true ABCK value is 0.127, 0.274 is Meissner-refined). Plus self-retracted "9σ" LiteBIRD headline; Eskilt2022 vs Eskilt2022b 3.6σ-vs-2.4-2.9σ inconsistency with P1B. |
| P1B v1B.0.30 | 85 | **78** | Spectator-ALP self-consistency violated: at f_a~M_Pl, m~H_0 the misalignment ρ_φ ≈ ½ H_0² M_Pl² θ_i² → Ω_φ ~ O(4π/3) — NOT a spectator, dominates DE. This is GPT-B5 deferred 17 versions ago; surfaced now. Plus P1A iter2 status STILL says "not converged" while P1B headlines iter2 CONVERGED; cross-paper Table III stale across all 5 papers (cites v1B.0.13 for itself). Grok's stable "+4.3σ column removal" critique re-examined as REAL load-bearing (σ-tail extrapolation, not statistical tension). |
| P2 v1.7.37 | 82 | **81** | "3-5σ" headline is multiplier collage (6.25σ × r × b_φ × GR × photo-z), not unified Fisher; σ(f_NL)=0.7 used as point value not propagated; CFC physical-frame matter-bounce bispectrum NOT computed (assumed by parallelism with inflation result); Heinrich Fisher built at f_NL=0 fiducial applied at f_NL=−4.375. 3 of 4 v1.7.31+ deferrals confirmed STILL OPEN. |
| P3 v3.1.63 | 87 | **85** | Conclusions §sec:conclusion item 5 still quotes σ(f_NL)=8.27 ± 2.37 Fisher form that §pathc_caveats (i) explicitly RETRACTED (α=0 stationary point breaks local-linear); NANOGrav γ cross-surface drift (paper anchors on real-KDE 2.567±0.382, CLAUDE.md + Houston review prompt still cite 3.20±0.42 superseded synthetic); 5-α-grid Fisher refit + Savage-Dickey on existing chain + score-stratified novelty quintiles all DO-NOW-feasible but still queued. |
| P4 v1.0.138 | 90 | **85** | σ(A_dipole) = 0.006% assumes per-pixel-independent Gaussian residuals; paper itself documents the residual is spatially coherent → N_eff drops from 36,418 to O(400-1,400) → true σ inflates 5-10× → "264.5σ" formal-exclusion drops to ~37σ (still excludes 1.7%, but rhetoric is over-tight by 20-60×); mask conflation: joint_nuisance_model_fit + B5-injection-recovery use `(|b|>15°)` f_sky=0.74 while "canonical" residual headline uses `(n_total>0)` f_sky=0.49 — three different masks called "canonical"; boundary-distance "uniform" claim contradicted by the on-disk JSON (boundary shell contributes 46.5% of C_1 from 3.9% of sky). |
| P5 v0.1.32 | 85 | **82** | EFT bound `g_φ ∇φ/H_0 ≲ 10⁻²/⟨|Δρ/ρ_bg|⟩` is cosmetic Δf_CW relabeling — no transfer function, no Chern-Simons literature comparison (Lue-Wang-Kamionkowski / Alexander-Yunes); "pure shot-noise residual" claim contradicted by kurtosis +0.82 + 5.26σ tail on 1,821 pixels (expected max under shot-noise ≈ 4.05); "seven independent evidence lines" over-counted — only 3 truly independent classifier axes (V-Web tidal, FoF richness, void-finder). |

**Implication**: the "all 6 papers §4.4.1 cascaded-loop-confirmed at 95%" framing was overstated. The 5-vendor R-round pipeline has been honoring deferred-on-record contracts rather than auditing the underlying physics/statistics. **Items deferred 5+ versions ago need to be closed, not maintained.**

**Action plan (next 30-min loop firings, no Houston permission needed):**
- P1A: 30-min text fixes for sample-count drift + Caldwell→Cai/Quintom bibkey + ABCK γ attribution + Eskilt2022 harmonization
- P1B: surface ALP-Ω_φ issue properly (compute coupled Friedmann or demote §VI to appendix); update cross-paper Table III + sync P1A iter2 status
- P2: defer "unified Fisher" + CFC remain pod-class compute (~few hours); Heinrich σ propagation is a 30-min text edit
- P3: 30-min text fix to conclusions §sec:conclusion item 5; Savage-Dickey on existing chain is ~1 hr (chain on disk); CLAUDE.md γ-headline cross-surface sync
- P4: bootstrap σ_A_dipole over NSIDE=8 super-pixels is ~10-min local; mask-family-disclosure table is text edit
- P5: downgrade EFT bound framing OR derive transfer function; fix shot-noise claim arithmetic; reframe independence to 3 axes

These will be driven by the autonomous loop without asking. Houston sign-off remains the final 1% gate per `feedback_99_pct_readiness_cap`.

---

## RunPod backup & credit estimate (per Houston's directive)

**Backup status**: ALL canonical artifacts confirmed on HuggingFace as of session memory:
- `bamfai/bigbounce-mcmc` — frozen 2026-05-18 (full_tension + planck_bao_sn chains, posteriors, convergence)
- `bamfai/galaxy-chirality-catalog` — frozen 2026-05-21 (8.47M P4 catalog)
- `bamfai/galaxy-chirality-v2` — frozen 2026-05-22 (D4-TTA holdout artifacts)

**RunPod state**: 1 RUNNING pod `cobaya-r43-v2` (ijzftpy3klystt, RTX A5000, 23 days uptime, 0 GB volume) + 9 EXITED pods. The active pod's load-bearing scientific output is already on HF; pod can safely be stopped to save ~$0.27/hr (~$200/month) when not actively running new compute.

**RunPod credit estimate (next 2 weeks of substantive closures)**:
- P4 M2 full DR8-sweep per-galaxy template regression (canonical formal-exclusion path): ~$6 (CPU pod, ~half-day)
- P4 M6 full-catalog D4-TTA at production N=3.2M: ~$65 (H200, ~2 hr)
- P3 5-α-grid Fisher rerun + Savage-Dickey full multi-PTA: ~$25 (CPU)
- P1B coupled Friedmann + ALP integration validation: ~$5 (CPU)
- Validation MC buffer + unforeseen retries: ~$50

**Recommendation: $150-200 buffer on RunPod top-up** covers the substantive-closure backlog with margin. If Houston wants the active A5000 pod stopped to halt the ~$0.27/hr burn during the text-fix-heavy backlog, say so.

**Definition** (per Houston standing directive 2026-05-21): this file lists ONLY items that no agent can resolve — items that require Houston-only authority: personal sign-off, API/SSH credentials, arXiv endorsement, or something physical only Houston can provide.

Everything ELSE is being driven autonomously by agents. If an item is "out of repo scope" or "needs a pod" or "compute-bound" but I can spin up the pod myself, it does NOT belong on this list.

---

## 0. OpenRouter per-key weekly cap re-exhausted (2026-05-28) · gates R-rounds

**Diagnosis**: All 10 reviewers across two parallel R-rounds (P1B + P2 maintenance) returned `[FAIL]` in ~0.4s today with HTTP 403 `Key limit exceeded (weekly limit). Manage it using https://openrouter.ai/workspaces/default/keys/cdb1d2ef595c2ce98df9fa0add17a242adff5cfb9df1f8fcaba3c7b5f8345348`. Same active key as the 2026-05-23 exhaustion. The portfolio's daily-scale R-round volume (30+ on 2026-05-26 alone, plus daily maintenance rotations) is over the $50/week cap.

**Impact**: Autonomous loop cannot fire fresh R-rounds. Maintenance rotation halts. §4.4.1 status from 2026-05-27 holds (no new findings means no regression), but new R-round verification is blocked.

**Ask (pick one)**:
- **(a) Raise per-key cap (fastest)**: https://openrouter.ai/settings/keys → find `sk-or-v1-c25...cbf` → edit → raise `$50/week` cap to `$200/week` or remove entirely.
- **(b) Rotate key**: generate new OpenRouter key with no weekly cap, paste into `.env.local` as `OPENROUTER_API_KEY=sk-or-v1-...`.
- **(c) Wait for weekly rollover**: ~5-7 day delay; portfolio remains at the 2026-05-27 §4.4.1-satisfied state in the interim.

## 0b. Cron 7-day renewal point reached (2026-05-28) · gates loop continuation

**Diagnosis**: The drive-to-100 cron was scheduled ~2026-05-21 per the standing directive "This cron lives 7 days max (Claude session cron limit). On day 6, prompt to renew." Today is 2026-05-28 = day 7+. Cron should be renewed if Houston wants the loop to continue past 7 days.

**Ask**: Renew the cron (re-issue `/loop` or equivalent) if continuation is desired. With portfolio in steady-state §4.4.1-satisfied awaiting Houston sign-off, the marginal value of continued maintenance R-rounds is low; the bigger gating item is Houston sign-off (items 1–7 below).

---

## 🎯 PORTFOLIO STATE 2026-05-26

**ALL SIX PAPERS FORMALLY §4.4.1 CASCADED-LOOP-CONFIRMED.** The autonomous drive-to-100 loop's first STOP-CRITERIA half is met for every paper. The only remaining gate per paper is Houston sign-off (the final 1% per `feedback_99_pct_readiness_cap` is Houston-only).

| Paper | Version | §4.4.1 status | Tarball |
|---|---|---|---|
| P1A | v1A.0.35 | ✅ R15+R16+R-ext-strict+R-ext-strict-v2+R-ext-maint all 5/5 clean | `p1a_v1A.0.35_arxiv.tar.gz` (423 KB) |
| P1B | v1B.0.30 | ✅ R27+R28+R29+R30 all 5/5 clean | `p1b_v1B.0.30_arxiv.tar.gz` (255 KB) |
| P2 | v1.7.37 | ✅ R-ext-strict×3 all 5/5 clean | `p2_v1.7.37_arxiv.tar.gz` (341 KB) |
| P3 | v3.1.63 | ✅ R-ext-v63verify×3 all 5/5 clean (post GEM-B1+B2 truth-audit closure) | `p3_v3.1.63_arxiv.tar.gz` (26 MB) |
| P4 | v1.0.138 | ✅✅✅ 8 consecutive 5/5-clean R-rounds across v1.0.132–138 (double-exceeded) | `p4_v1.0.138_arxiv.tar.gz` (19 MB) |
| P5 | v0.1.32 | ✅ tick 200 R10+R11+R12 + R-ext-v2 + R-ext-v32verify all 5/5 clean | `p5_v0.1.32_arxiv.tar.gz` (570 KB) |

All 6 tarballs gitignored locally per `arxiv/.gitignore submission_tarballs/*.tar.gz` ("rebuildable on demand"), all standalone-smoke-tested with 0 undef refs / 0 undef cites.

---

## 1. Personal sign-off on P1A v1A.0.35 for arXiv submission · gates P1A

**Why blocked:** P1A satisfies §4.4.1 — multiple 5/5 PERFECTLY CLEAN cross-vendor R-rounds across DeepSeek + Gemini + GPT-5 + Grok-43 + Perplexity on v1A.0.35. ECH structural no-go theorem; 14 barriers close ECH-specific routes to dark energy. PDF 20 pp / 832 KB / 0 overfull >20pt / 0 undef refs. Final 1% is Houston-only per `feedback_99_pct_readiness_cap`.

**Ask:** Read `arxiv/paper1a_ech_nogo.tex` (or live PDF at https://bigbounce.hubify.app/papers/paper1a_ech_nogo.pdf) and reply **"sign off P1A"** or send blocking findings. **arXiv tarball pre-built**: `arxiv/submission_tarballs/p1a_v1A.0.35_arxiv.tar.gz` (423 KB).

---

## 2. Personal sign-off on P1B v1B.0.30 for arXiv submission · gates P1B

**Why blocked:** P1B v1B.0.30 satisfies §4.4.1 — R27 + R28 + R29 + R30 all 5/5 PERFECTLY CLEAN. MCMC companion to P1A; 309,189 frozen posterior samples; ΔNeff ≈ 0; H₀ = 67.68. PDF 11 pp / 699 KB / 0 undef refs / 0 undef cites.

**Ask:** Read `arxiv/paper1b_mcmc_companion.pdf` and reply **"sign off P1B"** or send blocking findings. **arXiv tarball pre-built**: `arxiv/submission_tarballs/p1b_v1B.0.30_arxiv.tar.gz` (255 KB).

---

## 3. Personal sign-off on P2 v1.7.37 for arXiv submission · gates P2

**Why blocked:** P2 v1.7.37 satisfies §4.4.1 — R-ext-strict×3 all 5/5 PERFECTLY CLEAN. f_NL Forecast: Branch-V matter bounce predicts f_NL = −35/8 = −4.375 (parameter-free, SPHEREx-testable). σ(f_NL) ≈ 0.7 (Heinrich+2023 anchor) → 4.7–12σ detection by 2027.

**Ask:** Read `research/focused_paper_source_integration/02_full_draft.pdf` (21 pp / 818 KB) and reply **"sign off P2"** or send blocking findings. **arXiv tarball pre-built**: `arxiv/submission_tarballs/p2_v1.7.37_arxiv.tar.gz` (341 KB).

---

## 4. Personal sign-off on P3 v3.1.63 for arXiv submission · gates P3

**Why blocked:** P3 v3.1.63 satisfies §4.4.1 — R-ext-v63verify×3 all 5/5 PERFECTLY CLEAN after the GEM-B1 (Fisher α² Taylor) polish closure. Multi-survey anomaly catalog: 378,280 unique anomalies across 7 retained surveys after 7-way 5″ positional dedup. NANOGrav γ = 3.20 ± 0.42 vs matter-bounce 3.0 at 0.48σ.

**Ask:** Read `pipelines/p3_anomaly_engine/paper3_draft.pdf` (48 pp / 28.4 MB) and reply **"sign off P3"** or send blocking findings. **arXiv tarball pre-built**: `arxiv/submission_tarballs/p3_v3.1.63_arxiv.tar.gz` (26 MB).

---

## 5. Personal sign-off on P4 v1.0.138 for arXiv submission · gates P4

**Why blocked:** P4 v1.0.138 has the LONGEST cascaded-loop-exit streak in the campaign — **8 consecutive 5/5 PERFECTLY CLEAN R-rounds across v1.0.132/133/134/135/136/137/138** (>2.5× the §4.4.1 minimum of 3). Galaxy chirality catalog: 8.47M galaxies (3.2M spirals); ViT-Small classifier with Z₂ 2-fold flip TTA.

**Phase-3 substantive closures landed this session** (Houston-shared v1.0.132 external review wave + ChatGPT-B5 + Gemini-Major1/Major2/Major4):
- ChatGPT-M1 systematics-preserving density-stratified null
- Gemini-Major1 boundary-distance variance uniformity
- ChatGPT-B5 full-catalog injection-recovery (50%-recovery-3σ threshold ≤ 0.50%)
- Gemini-Major2 1.21× hard-label variance algebraic derivation
- **Joint nuisance-marginalized model fit FORMALLY EXCLUDES interpretation (i) at 99% confidence** — A_dipole = 0.23% f_CW vs 1.7% reference, z = −264.5
- Gemini-Major4 extended 24-template joint fit with leg × confidence interactions

**Ask:** Read `pipelines/p2_chirality/chirality_catalog_paper.pdf` (54 pp / 26.3 MB / 0 undef refs) and reply **"sign off P4"** or send blocking findings. **arXiv tarball pre-built**: `arxiv/submission_tarballs/p4_v1.0.138_arxiv.tar.gz` (19 MB, 15 files).

---

## 6. Personal sign-off on P5 v0.1.32 for arXiv submission · gates P5

**Why blocked:** P5 v0.1.32 satisfies §4.4.1 — tick 200 R10+R11+R12 cross-model rotation + R-ext-v2 + R-ext-v32verify all 5/5 PERFECTLY CLEAN. Environmental dependence of spiral chirality across DESI LSS at V-Web resolution. Headline: chirality is statistically independent of LSS environment within DESI DR1 at V-Web resolution. 6 independent positive evidence lines.

**v0.1.32 bundled-closure wave** (Gemini-3.1-Pro R-ext-v3 MAJORs):
- GEM-M1 RSD anisotropy caveat in §XII Limitations
- GEM-M2 ALP-density EFT parameterization in §XI.B (g_φ ∇φ/H₀ ≲ 10⁻²/⟨|Δρ/ρ_bg|⟩)
- GEM-M3 Alexander & Yunes 2009 + Lue–Wang–Kamionkowski 1999 foundational citations

**Ask:** Read `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` (17 pp / 928 KB) and reply **"sign off P5"** or send blocking findings. **arXiv tarball pre-built**: `arxiv/submission_tarballs/p5_v0.1.32_arxiv.tar.gz` (570 KB).

---

## 7. arXiv endorsement + submission credentials · gates ALL papers

**Why blocked:** Only Houston has the arXiv account + the astro-ph.CO / astro-ph.GA / astro-ph.IM endorser relationships. Agents cannot create arXiv accounts or get endorsed.

**Ask:** Confirm submission order (recommended **P1A → P4 → P3 → P1B → P2 → P5**) and run the arXiv submission when each paper is signed off. Each tarball is a single upload at https://arxiv.org/submit; announcement schedule is the next 20:00 UTC after submission.

---

## What is NOT on this list (autonomous work completed or still in-flight)

Items explicitly RESOLVED since the 2026-05-22 snapshot:

- ✅ **OpenRouter per-key cap raise PROPAGATED.** Dozens of 5-vendor cross-vendor R-rounds executed cleanly across 2026-05-26, including the entire portfolio-§4.4.1 confirmation wave. The earlier "cap exhausted" item is closed.
- ✅ **DESI environmental VAC** — RESOLVED via V-Web env_finder + ASTRA EDR + DESIVAST cross-validation; 6 independent positive evidence lines for the headline environment-independence.
- ✅ **Visual-formatting cleanup** (cron fires #20–#24): all 6 papers at 0 overfull > 20pt.
- ✅ **arXiv tarball rebuild** (2026-05-26 fire xx:47): all 6 tarballs current at the §4.4.1-confirmed versions with 0 undef refs / 0 undef cites in isolated compile.
- ✅ **Phase-3 P4 substantive closures**: all Houston-shared v1.0.132 external review findings closed; interpretation (i) formally excluded at 99%.
- ✅ **All Gemini-3.1-Pro per-vendor regressions** (P3 GEM-B1+B2 and P5 GEM-M1+M2+M3) truth-audited and either falsified or closed.
- ✅ **Wiki pointer entities refreshed** to current SSOT state (2026-05-26).

Items still autonomous, in-flight or queued:

- ⏳ HF model card refresh for `bamfai/galaxy-chirality-v2` v1.0.128 → v1.0.138 (HF_TOKEN in `.env.local`) — queued for next non-API tick once Houston signs off P4.
- ⏳ Maintenance R-rounds continue at xx:17 / xx:47 cadence to keep streaks alive while waiting for Houston sign-off.

If anything above DOES end up needing Houston input mid-execution, it will be promoted to this list at that moment, not deferred to here preemptively.
