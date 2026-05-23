# Final task lists for all 6 papers — post cron fires #21–#29

**Last refreshed: 2026-05-22 PDT (tick 151, cron fire #30)** — supersedes the 2026-05-21 R23 snapshot.

The R23-era snapshot of this file lived through the visual-formatting-cleanup wave (cron fires #20–#24) that brought **all 6 papers to 0 overfull > 20pt**, the SSOT/CLAUDE.md doc-consistency sweep (fires #25–#27), and the full-portfolio arXiv-tarball preparation (fires #28–#29). This refresh marks all autonomous items that closed in those waves and lists what's actually open right now.

Houston standing rule: **eat the frog, do the hard thing, no deferrals** — items appear here only because they are genuinely the next step.

**OpenRouter status:** active key (`sk-or-v1-c25...cbf`) is at `limit=$50/week, usage=$98.66, remaining=$0`. Workspace credit healthy ($83.47 / $600). Cap raise still has not propagated to the active key. **All "fire next R-round" items below are blocked on this.** See `NEEDS_HOUSTON.md` item 0 for the 3 unblock paths.

---

## P1A — ECH Structural Closure (no-go theorem) — v1A.0.35

**Status: 90% / 99% cap · external-review-ready · cascaded-loop exit holds.**

R-round history: R15 + R16 + R24 all 0/0 across all 5 vendors on paper content (R23 Gemini BLOCKER was prompt-meta-error, falsified; M1+m1+n1 closed in v1A.0.34). Cron fire #24 wrapped the Holst-dual equation in `widetext` and bumped to v1A.0.35 — first fully-clean P1A compile in the campaign.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v1A.0.35** | Houston | ✅ ONLY remaining gate |
| 2 | Build arXiv tarball | agent | ✅ DONE fire #28 (`arxiv/submission_tarballs/p1a_v1A.0.35_arxiv.tar.gz`, 433 KB, smoke-tested 0 undef refs/cites) |
| 3 | arXiv tarball clean-revtex smoke test | agent | ✅ DONE fire #28 |
| 4 | arXiv submission (astro-ph.CO + astro-ph.IM) | Houston | needs Houston's arXiv endorsement |

**Nothing else is open.** PDF is 20 pp / 832 KB / 0 overfull >20pt / 0 undef refs / 0 undef cites. 4 mirrors byte-identical.

---

## P1B — MCMC Companion paper — v1B.0.22

**Status: 90% / 99% cap · external-review-ready per R16+R23 convergence + cron-fire-#23 first fully-clean compile.**

R-round history: R16 had 4-of-5 reviewers 0/0 (Grok-only B1+B2 BLOCKERs FALSIFIED via stale-comment audit). R23 returned 5-of-5 reviewers 0/0 (fully clean — no findings of any class). Cron fire #23 closed the last 40pt residual (`tab:mcmc_inventory` → `table*`) — first fully-clean P1B compile in the campaign.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | Bump P1B readiness in SSOT + papers.ts to reflect R23 5/5 clean | agent | ✅ DONE fire #23 / #27 (papers.ts at 90; SSOT entry refreshed) |
| 2 | **Houston sign-off on v1B.0.22** | Houston | gate |
| 3 | Build arXiv tarball | agent | ✅ DONE fire #29 (`p1b_v1B.0.22_arxiv.tar.gz`, 255 KB, 0 undef refs/cites) |
| 4 | Fire next R-round (R26) to confirm 5/5 clean holds at v1B.0.22 | agent | ⏳ BLOCKED on OR cap |
| 5 | arXiv submission | Houston | endorsement |

---

## P2 — f_NL Forecast (SPHEREx) — v1.7.33

**Status: 95% / 99% cap · external-review-ready · R23 5/5 clean confirmed.**

R-round history: R23 returned 5-of-5 reviewers 0/0 (first all-5-clean round on P2). Heinrich+2023 σ(f_NL)=0.7 externalization is reviewer-accepted. Cron fire #21 closed the 2495pt `\date{}` blob, table wide-floats, and the last 83pt residual — first fully-clean P2 compile.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | Bump P2 readiness to 95 in SSOT + papers.ts | agent | ✅ DONE fire #21 / #27 |
| 2 | Compile fresh PDF on the latest .tex | agent | ✅ DONE fire #21 (21 pp / 817 KB / 0 overfull) |
| 3 | Site-sync paper PDFs to all mirrors | agent | ✅ DONE fire #21 |
| 4 | **Houston sign-off on v1.7.33** | Houston | gate |
| 5 | Build arXiv tarball | agent | ✅ DONE fire #29 (`p2_v1.7.33_arxiv.tar.gz`, 346 KB) |
| 6 | Fire next R-round (R26) to confirm 5/5 clean holds | agent | ⏳ BLOCKED on OR cap |
| 7 | arXiv submission (astro-ph.CO) | Houston | endorsement |

---

## P3 — Multi-Survey Anomaly Catalog — v3.1.62

**Status: 95% / 99% cap · external-review-ready · R23 5/5 clean confirmed.**

R-round history: R16 4-of-5 (Grok BLOCKERs truth-audited). R23 5-of-5 0/0. v3.1.56 closed the multi-round 9,576 dedup-shortfall via union-find. Cron fire #24 closed the last 4 residual overfulls (NANOGrav widetext + caveats paragraph-split + `\allowbreak`-injected paths + Posterior align widetext) — first fully-clean P3 compile.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | Bump P3 readiness to 95 in SSOT + papers.ts | agent | ✅ DONE fire #24 / #27 |
| 2 | Verify 7-survey dedup arithmetic propagation | agent | ✅ DONE pre-R23 (matches abstract + Table 1 + §6) |
| 3 | Compile fresh P3 PDF | agent | ✅ DONE fire #24 (47 pp / 28.4 MB / 0 overfull / 0 undef) |
| 4 | **Houston sign-off on v3.1.62** | Houston | gate |
| 5 | Build arXiv tarball | agent | ✅ DONE fire #29 (`p3_v3.1.62_arxiv.tar.gz`, 27 MB, 23 figures) |
| 6 | Fire next R-round (R26) to confirm 5/5 clean holds | agent | ⏳ BLOCKED on OR cap |
| 7 | arXiv submission (astro-ph.CO + astro-ph.IM) | Houston | endorsement |

---

## P4 — Galaxy Chirality Catalog (8.47M / 3.2M spirals) — v1.0.128

**Status: 95% CAP · external-review-ready · R22 3/5 + R23 5/5 clean.**

R-round history: R22 3-of-5 reviewers 0/0; GPT-5 + Perplexity closed bundled in v1.0.122. R23 verification 5-of-5 0/0 (no regressions from v1.0.122 closures). Cron fires #5–#20 brought v1.0.122 → v1.0.128 with all overfulls eliminated.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v1.0.128** | Houston | ✅ ONLY remaining gate |
| 2 | Push HF model card `bamfai/galaxy-chirality-v2` to v1.0.128 | agent | ✅ DONE fire #31 (HF sha 5cb8df76e1b8; 13 v1.0.125 → v1.0.128 + 7 paper4-v1.0.125 → paper4-v1.0.128) |
| 3 | Build arXiv tarball | agent | ✅ DONE fire #28 (`p4_v1.0.128_arxiv.tar.gz`, 20 MB, 15 files, smoke-tested 0/0) |
| 4 | arXiv submission (astro-ph.GA + astro-ph.CO) | Houston | endorsement |

---

## P5 — Environmental Dependence of Spiral Chirality (DESI LSS) — v0.1.18-2026-05-22

**Status: 85% · paper fully drafted + three-VAC validation + DESIVAST per-galaxy + 6-decomposed cluster-boundary-leakage + DESIVAST-anchored void-class clean null + 3-algorithm DESIVAST robustness + catalog-native V2 GALZONE + filament-class within-class decomposition reproducing bright-vs-dark sign-flip on 2nd V-Web class (26 pp) · first R-round still blocked on OR cap.**

The R23-era task list called P5 "the biggest lift remaining" with a 9 KB scaffold paper; cron fires #1–#11 closed Phase 2 + Tempel + LEE + paper expansion; cron fires #33–#36 added §sec:tweb_compare with the T-Web DR1 + ASTRA EDR + DESIVAST DR1 BGS three-VAC concurrent-literature cross-validation (+5pp readiness, fire #33); cron fire #40 added DESIVAST per-galaxy cross-match (0/6 V-Web void spirals inside DESIVAST holes at z≤0.24); cron fire #41 added §sec:results_within_class_density (−4.7σ cluster signal is boundary-leakage NOT clean density effect, +5pp readiness); fires #43+#44 added z-quartile-uniform + tracer-program bright-vs-dark sign-flip decompositions; **fire #45 added DESIVAST-anchored void classifier at n=56,981 = 133× V-Web void sample, returning cw_fraction=0.4964 vs non-void 0.4971 (Δ=0.0007 statistically indistinguishable) — strongest single piece of positive evidence for headline environment-independence, +5pp readiness**.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | Phase 2 sensitivity sweep (R_s × grid × λ_th) | agent | ✅ DONE pre-#21 (9 configs on disk at `env_finder/reports/02_phase2_*`) |
| 2 | RSD correction | agent | ✅ DONE fire #25 (RSD-robustness item added to Limitations: σ_v/(aH) ≲ 5–8 Mpc/h is 3–5× smaller than R_s=25 Mpc/h smoothing → headline null robust to RSD) |
| 3 | Tempel+2014 cross-validation | agent | ✅ DONE pre-#21 (filament concordance 0.026pp on disk) |
| 4 | Paper LaTeX expansion 9 KB → full first-draft | agent | ✅ DONE pre-#21 (885 lines covering Intro/Data/V-Web/Stats/Results/Phase 2/Tempel/Systematics/Discussion/Limitations/LSST/Conclusions) |
| 5 | First P5 PDF compile + mirror to 3 sites | agent | ✅ DONE fire #25 (738 KB / 0 overfull / 0 undef, byte-identical 3 mirrors) |
| 6 | First R-round on P5 (5-vendor cross-vendor) | agent | ⏳ BLOCKED on OR cap |
| 7 | Bundled hard-fix wave closing R-round findings | agent | gated on #6 |
| 8 | (OPTIONAL) DESI environmental VAC | Houston | optional fallback; V-Web is canonical without it |
| 9 | Houston sign-off on first publishable version | Houston | gate |
| 10 | Build arXiv tarball | agent | ✅ DONE fire #29 + REBUILT fires #36/#40/#41/#43/#44/#45/#47/#49/#51 (`p5_v0.1.18_arxiv.tar.gz`, 445 KB, smoke-tested 0 undef refs/cites in isolation) |
| 11 | arXiv submission (astro-ph.CO + astro-ph.GA) | Houston | endorsement |

---

## Cross-cutting open items

- ✅ Visual-formatting cleanup (cron fires #20–#24): **all 6 papers now at 0 overfull > 20pt** — first time in campaign.
- ✅ SSOT doc-consistency sweep (fires #25–#27): papers.ts / SSOT/paper-5/status.md / SSOT/index.md table row + program paragraph / CLAUDE.md headline all consistent at the current 6-paper readiness state.
- ✅ Full-portfolio arXiv tarballs (fires #28–#29): all 6 tarballs standalone-smoke-tested 0 undef refs/cites; gitignored locally; rebuildable on demand.
- ⏳ OpenRouter per-key cap raise: blocking R26 wave + first P5 R1. Listed in `NEEDS_HOUSTON.md` item 0 with 3 unblock paths.
- ✅ HF model card refresh for `bamfai/galaxy-chirality-v2` v1.0.125 → v1.0.128 (fire #31, HF sha `5cb8df76e1b8`).

## Eat-the-frog priority order (current)

1. **Houston: sign off P1A v1A.0.35** (cleanest paper, loop-exit milestone, arXiv-tarball pre-built).
2. **Houston: sign off P4 v1.0.128** (R22+R23 cleanest P4 history, arXiv-tarball pre-built).
3. **Houston: raise OR per-key cap or rotate key** — unblocks R26 wave across P1A/P1B/P2/P3/P4 + first P5 R1.
4. Agent: once OR unblocked, fire R26 wave in parallel + first P5 R1; expect ≥3 of 5 to be 5-of-5 clean per the R23-era trajectory.
5. Houston: sign off P1B / P2 / P3 after R26 confirms the 5/5 clean streak holds.
6. Houston: sign off P5 after first R-round closes.
7. Houston: arXiv submissions in batches as sign-offs land.
