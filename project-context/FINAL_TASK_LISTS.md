# Final task lists for all 6 papers

**Last refreshed: 2026-05-26 PDT (drive-to-100 portfolio-§4.4.1 milestone)** — supersedes the 2026-05-22 cron-fire #30 refresh.

🎯🎯🎯 **PORTFOLIO MILESTONE 2026-05-26**: All 6 papers formally satisfy AGENT_RULES §4.4.1 cascaded-loop-exit (3+ consecutive 5/5 PERFECTLY CLEAN cross-vendor R-rounds). The autonomous loop's first STOP-CRITERIA half is now met portfolio-wide. **The remaining gate per paper is Houston sign-off** (the final 1% per `feedback_99_pct_readiness_cap` is Houston-only and cannot be satisfied by the autonomous loop).

Houston standing rule: **eat the frog, do the hard thing, no deferrals** — items appear here only because they are genuinely the next step.

**OpenRouter status:** active key is funded and operational; cap-raise propagated. Dozens of 5-vendor cross-vendor R-rounds executed cleanly throughout 2026-05-26.

---

## Research-node context tasks — 2026-06-16

This is a docs/context track, not a paper-readiness track. It must not mutate papers, PDFs, tarballs, pods, GPU runs, or generated artifacts.

| # | Task | Owner | Status |
|---|------|-------|---|
| RN-2026-06-16 | Implement the Mac mini research-node setup safely: capture the direct BigBounce repo + `bigbounce.hubify.app` source-of-truth contract, inventory Hermes/OpenClaw/Claude Code/Codex/Pi runners, define You.md/h.computer/SMS routing contract, add approved h.computer status hooks, add local fake-SMS no-live-runs smoke test, and draft the multi-model/multi-UI review-method paper protocol as a candidate workflow paper. See `project-context/mac-mini-research-node-2026-06-16.md`. | agent | queued; source-of-truth contract captured in `project-context/bigbounce-source-of-truth-contract-2026-06-16.md`; runtime inventory captured in `project-context/agent-runtime-inventory-2026-06-16.md`; MCP config inventory captured in `project-context/mcp-config-inventory-2026-06-16.md`; OpenClaw/Hermes/Pi are not runnable or authorized for BigBounce yet; Hubify auth restored via `RTW6-E8D9` but current research truth remains local `bigbounce` plus `bigbounce.hubify.app`; no live runs started |

---

## P1A — ECH Structural Closure (no-go theorem) — v1A.0.35

**Status: 95% / 99% cap · external-review-ready · §4.4.1 SATISFIED (tick 102 + R-ext-strict + R-ext-strict-v2 today, all 5/5 PERFECTLY CLEAN).**

R-round history: R15 + R16 + R24 + R-ext-strict + R-ext-strict-v2 — all 5/5 PERFECTLY CLEAN across all 5 vendors.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v1A.0.35** | Houston | ⏳ ONLY remaining gate |
| 2 | Build arXiv tarball | agent | ✅ DONE fire #28 (`arxiv/submission_tarballs/p1a_v1A.0.35_arxiv.tar.gz`, 433 KB, smoke-tested 0 undef refs/cites) |
| 3 | arXiv submission (astro-ph.CO + astro-ph.IM) | Houston | needs Houston's arXiv endorsement |

PDF is 20 pp / 832 KB / 0 overfull >20pt / 0 undef refs / 0 undef cites. 4 mirrors byte-identical.

---

## P1B — MCMC Companion paper — v1B.0.30

**Status: 95% / 99% cap · external-review-ready · §4.4.1 SATISFIED today (R27 + R28 + R29 all 5/5 PERFECTLY CLEAN across v1B.0.28/29/30).**

R-round history: R16 4-of-5 clean (1 BLOCKER FALSIFIED via stale-comment audit) → R23 5-of-5 clean → R27 5/5 clean on v1B.0.28 → R28 5/5 clean on v1B.0.29 → R29 5/5 clean on v1B.0.30 (after body-text reviewer-ID scrub from P4 v1.0.132 pattern).

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v1B.0.30** | Houston | ⏳ ONLY remaining gate |
| 2 | Rebuild arXiv tarball for v1B.0.30 (current was built on v1B.0.22) | agent | queued |
| 3 | arXiv submission (astro-ph.CO) | Houston | needs Houston endorsement |

---

## P2 — f_NL Forecast — v1.7.37

**Status: 95% / 99% cap · external-review-ready · §4.4.1 SATISFIED today (R-ext-strict + R-ext-strict-v2 + R-ext-strict-v3 all 5/5 PERFECTLY CLEAN on v1.7.37).**

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v1.7.37** | Houston | ⏳ ONLY remaining gate |
| 2 | Rebuild arXiv tarball for v1.7.37 (current was built on v1.7.30) | agent | queued |
| 3 | arXiv submission (astro-ph.CO) | Houston | needs Houston endorsement |

---

## P3 — Multi-Survey Anomaly Catalog — v3.1.63

**Status: 95% / 99% cap · external-review-ready · §4.4.1 RE-SATISFIED (R-ext-v63verify + v63verify-v2 + v63verify-v3 all 5/5 PERFECTLY CLEAN on v3.1.63 after GEM-B1+B2 truth-audit closure).**

R-round history: R-ext-strict + R-ext-strict-v2 on v3.1.62 were 5/5 clean; R-ext-strict-v3 had a Gemini-3.1-Pro 2-BLOCKER regression. Truth-audit verdicts: GEM-B2 (matter-bounce γ=3.0) FALSIFIED via Quintin2014 + Cai2014; GEM-B1 (Fisher α² Taylor) PARTIALLY ALREADY ADDRESSED — closed in v3.1.63 polish with exact multi-tracer Fisher formula note. Three R-ext-v63verify rounds on the polished v3.1.63 all 5/5 clean.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v3.1.63** | Houston | ⏳ ONLY remaining gate |
| 2 | Rebuild arXiv tarball for v3.1.63 (current was built on v3.1.56) | agent | queued |
| 3 | arXiv submission (astro-ph.CO + astro-ph.IM) | Houston | needs Houston endorsement |

PDF is 48 pp / 28.44 MB / 0 undef refs / 2 carry-over overfulls (both pre-existing < 50pt). 5 mirrors byte-identical.

---

## P4 — Galaxy Chirality Catalog (8.47M / 3.2M spirals) — v1.0.138

**Status: 95% / 99% cap · external-review-ready · §4.4.1 DOUBLY EXCEEDED (7 consecutive 5/5 PERFECTLY CLEAN R-rounds across v1.0.132/133/134/135/136/137/138).** Most-converged paper in the campaign.

Substantive Phase-3 closures landed this session (v1.0.122 → v1.0.138):

| v | Closure |
|---|---|
| v1.0.131 | ChatGPT-M3 (MC≥10⁴) + M5 (data-vector table) |
| v1.0.132 | GRO-B1 (title scrub) + GRO-B4 (Table II row v MC count) |
| v1.0.133 | **ChatGPT-M1**: systematics-preserving density-stratified null executed LOCALLY (3.4s, no pod) |
| v1.0.134 | Body-text reviewer-ID scrub + **Gemini-Major1** boundary-distance variance + softened "rules out" → "disfavors" + release-tag scrub + broken `\ref` fixes |
| v1.0.135 | **ChatGPT-B5** full-catalog injection-recovery sweep (50%-recovery-3σ ≤ 0.50% on full catalog vs 0.75% HC subsample) |
| v1.0.136 | **Gemini-Major2** 1.21× hard-label variance algebraic derivation |
| v1.0.137 | **Joint nuisance-marginalized model fit FORMAL EXCLUSION**: A_dipole = 0.23% f_CW vs 1.7% reference → z = −264.5 → **interpretation (i) FORMALLY EXCLUDED at 99% confidence** |
| v1.0.138 | **Gemini-Major4** extended 24-template joint fit with leg × confidence interactions (dipole posterior robust, ≥10–26σ structure on multiple interaction cells) |

ALL Houston-shared v1.0.132 external review findings (Gemini MAJOR REVISIONS + Grok MINOR + ChatGPT REJECT) CLOSED in this session.

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v1.0.138** | Houston | ⏳ ONLY remaining gate (most-converged paper) |
| 2 | Rebuild arXiv tarball for v1.0.138 (current was built on v1.0.128) | agent | queued |
| 3 | Push HF model card `bamfai/galaxy-chirality-v2` to v1.0.138 | agent | queued (last refresh v1.0.128) |
| 4 | arXiv submission (astro-ph.GA + astro-ph.CO) | Houston | endorsement |
| 5 | (OPTIONAL) M2 full DR8-sweep per-galaxy template regression | future | genuinely pod-bound; the v1.0.138 24-template fit already formally excludes interpretation (i) at 99% so this is no longer load-bearing |
| 6 | (OPTIONAL) M6 full-catalog D4-TTA | future | GPU-bound |

PDF is 54 pp / 26.26 MB / 0 undef refs / 3 carry-over overfulls. 3 mirrors byte-identical.

---

## P5 — Environmental Dependence of Spiral Chirality (DESI LSS) — v0.1.32

**Status: 95% / 99% cap · §4.4.1 SATISFIED (tick 200 R10+R11+R12 cross-model rotation + R-ext-v2 + R-ext-v32verify all 5/5 PERFECTLY CLEAN).**

v0.1.32 bundled-closure wave today: Gemini-3.1-Pro flagged 3 MAJORs in R-ext-v3 — all truth-audited as REAL substantive findings, all closed:
- **GEM-M1**: RSD anisotropy caveat paragraph in §XII Limitations (anisotropic Kaiser+FoG vs scalar displacement; full anisotropic robustness deferred to Zel'dovich-reconstructed rerun)
- **GEM-M2**: ALP-density gradient EFT parameterization in §XI.B (`L_parity ⊃ g_φ(∇_i φ)(∇^i ρ/ρ_bg)(L̂·ẑ)`; first-order bound `|g_φ ∇φ/H_0| ≲ 10⁻² / ⟨|Δρ/ρ_bg|⟩`)
- **GEM-M3**: Alexander & Yunes 2009 (Phys.Rep. 480 — Chern-Simons review) + Lue–Wang–Kamionkowski 1999 (PRL 83 — cosmological parity-violating interactions) added to bibliography

| # | Task | Owner | Status |
|---|------|-------|---|
| 1 | **Houston sign-off on v0.1.32** | Houston | ⏳ ONLY remaining gate |
| 2 | (OPTIONAL) Zel'dovich-reconstructed V-Web rerun | future | needs DESI DR1 LSS catalog acquisition + pyrecon; would tighten the anisotropic RSD bound |
| 3 | Rebuild arXiv tarball for v0.1.32 (current was built on v0.1.26+) | agent | queued |
| 4 | arXiv submission (astro-ph.CO + astro-ph.GA) | Houston | endorsement |

PDF is 17 pp / 928 KB / 0 undef refs / 0 overfull. 3 mirrors byte-identical.

---

## Cross-cutting open items

- ✅ **Portfolio-wide §4.4.1 satisfaction milestone landed 2026-05-26 fire xx:47.**
- ✅ All 6 papers at 0 overfull > 20pt.
- ✅ All 6 papers at 0 undef refs / 0 undef cites.
- ⏳ **Rebuild arXiv submission tarballs for all 6 papers at current versions** (the 2026-05-22 fire #28/#29 tarballs are 5–10 minor versions behind):
  - P1A v1A.0.35 (tarball up-to-date)
  - P1B v1B.0.22 → v1B.0.30 (rebuild needed)
  - P2 v1.7.30 → v1.7.37 (rebuild needed)
  - P3 v3.1.56 → v3.1.63 (rebuild needed)
  - P4 v1.0.128 → v1.0.138 (rebuild needed)
  - P5 v0.1.26 → v0.1.32 (rebuild needed)
- ⏳ HF model card refresh for `bamfai/galaxy-chirality-v2` v1.0.128 → v1.0.138 (HF_TOKEN in `.env.local`).

## Eat-the-frog priority order (current)

1. **Houston: sign off all 6 papers** — the autonomous loop's first STOP-CRITERIA half is met (≥3 consecutive 5/5 clean R-rounds per paper); the final 1% per `feedback_99_pct_readiness_cap` is Houston-only.
2. **Houston: arXiv endorsement** for each paper's primary category (astro-ph.CO / GA / IM).
3. Agent: rebuild arXiv tarballs for v1B.0.30 / v1.7.37 / v3.1.63 / v1.0.138 / v0.1.32 ahead of Houston sign-off so submissions are zero-friction.
4. Agent: HF model card refresh once Houston signs off P4.
5. Agent: continue maintenance R-rounds to keep streaks alive while waiting for Houston sign-off (1–2 per fire is plenty; convergence is robust).

## Summary

**6 papers / 6 §4.4.1-satisfied / portfolio readiness 95% / final 1% Houston-only.** The autonomous drive-to-100 loop has done its job through the structural verification gate; Houston's read-and-sign is the bottleneck.
