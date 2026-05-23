# Houston sign-off brief — 6-paper portfolio status

**Generated:** 2026-05-22 PDT (tick 177, cron fire #55).
**Purpose:** Single-page summary for Houston's sign-off review across all 6 papers.

This document is a derivative of the SSOT — the canonical state lives in
`project-context/SSOT/index.md` and `project-context/SSOT/paper-N/status.md`.

---

## TL;DR

**5 of 6 papers at the 95% external-review-ready bar; P5 at 90%, gap closes on first R-round (OR-cap-blocked).**

| Paper | Version | Readiness | What it needs from you |
|---|---|---:|---|
| P1A | v1A.0.35 | 95% | **Sign off → arXiv submission** |
| P1B | v1B.0.22 | 95% | **Sign off → arXiv submission** |
| P2 | v1.7.33 | 95% | **Sign off → arXiv submission** |
| P3 | v3.1.62 | 95% | **Sign off → arXiv submission** |
| P4 | v1.0.128 | 95% | **Sign off → arXiv submission** |
| P5 | v0.1.19 | 90% | OR per-key cap raise → first R-round → sign-off |

**Two ways to sign off**: (1) commit message containing `sign off PNX` for the relevant paper(s); or (2) message me directly. Either triggers arXiv submission readiness.

**All 6 arXiv tarballs are pre-built + smoke-tested standalone** at `arxiv/submission_tarballs/` — submission is a single upload to https://arxiv.org/submit once you sign off.

**OpenRouter cap blocker** — see `NEEDS_HOUSTON.md` item 0; 60-second fix unblocks R26 wave across P1A/P1B/P2/P3/P4 + first P5 R1.

---

## P1A — ECH Structural Closure (no-go theorem) — v1A.0.35

**Readiness 95%** · arXiv-tarball `p1a_v1A.0.35_arxiv.tar.gz` 433 KB · 20 pp / 832 KB PDF.

**Why ready**: cascaded-loop exit confirmed — R15+R16+R24 all 5/5 clean across DeepSeek-V4-Pro + Gemini-3.1-Pro + GPT-5 + Grok-4.3 + Perplexity-Sonar-Pro. 10th-consecutive Gemini-cosmology 0-BLOCKER on paper content. AGENT_RULES §4.4.1 satisfied. First fully-clean P1A compile in entire campaign (0 overfull / 0 undef refs / 0 undef cites).

**arXiv categories**: astro-ph.CO + astro-ph.IM.

**To sign off**: read `arxiv/paper1a_ech_nogo.tex` end-to-end (or live PDF at https://bigbounce.hubify.app/papers/paper1a_ech_nogo.pdf) and commit "sign off P1A".

---

## P1B — MCMC Companion paper — v1B.0.22

**Readiness 95%** · arXiv-tarball `p1b_v1B.0.22_arxiv.tar.gz` 255 KB · 11 pp / 694 KB PDF.

**Why ready**: R16 4-of-5 + R23 5-of-5 clean (Grok-only B1+B2 BLOCKERs at R16 audit-falsified via stale-comment direct-file inspection). First fully-clean P1B compile in entire campaign (`tab:mcmc_inventory` → `table*` closure landed at fire #23).

**arXiv category**: astro-ph.CO.

**To sign off**: read `arxiv/paper1b_mcmc_companion.tex` and commit "sign off P1B".

---

## P2 — f_NL Forecast (SPHEREx) — v1.7.33

**Readiness 95%** · arXiv-tarball `p2_v1.7.33_arxiv.tar.gz` 346 KB · 21 pp / 817 KB PDF.

**Why ready**: R23 5-of-5 reviewers 0/0 (first all-5-clean P2 round in campaign). Heinrich+2023 σ(f_NL)=0.7 externalization reviewer-accepted. First fully-clean P2 compile.

**arXiv category**: astro-ph.CO.

**To sign off**: read `research/focused_paper_source_integration/02_full_draft.tex` and commit "sign off P2".

---

## P3 — Multi-Survey Anomaly Catalog — v3.1.62

**Readiness 95%** · arXiv-tarball `p3_v3.1.62_arxiv.tar.gz` 27 MB · 47 pp / 28.4 MB PDF.

**Why ready**: R16 4-of-5 (Grok BLOCKERs truth-audited and falsified) + R23 5-of-5 clean. v3.1.56 closed the multi-round 9,576 dedup-shortfall MAJOR via on-disk union-find artifact. First fully-clean P3 compile in entire campaign (NANOGrav widetext + §pathc_caveats paragraph-split + Posterior align widetext).

**arXiv categories**: astro-ph.CO + astro-ph.IM.

**To sign off**: read `pipelines/p3_anomaly_engine/paper3_draft.tex` and commit "sign off P3".

---

## P4 — Galaxy Chirality Catalog (8.47M / 3.2M spirals) — v1.0.128

**Readiness 95%** · arXiv-tarball `p4_v1.0.128_arxiv.tar.gz` 20 MB · 51 pp / 26.24 MB PDF.

**Why ready**: R22 3-of-5 reviewers 0/0 + R23 5-of-5 verification clean (no regressions). All overfulls eliminated. HF model card `bamfai/galaxy-chirality-v2` synced to v1.0.128 (HF sha 5cb8df76e1b8).

**arXiv categories**: astro-ph.GA + astro-ph.CO.

**To sign off**: read `pipelines/p2_chirality/chirality_catalog_paper.tex` and commit "sign off P4".

---

## P5 — Environmental Dependence of Spiral Chirality (DESI LSS) — v0.1.19

**Readiness 90%** · arXiv-tarball `p5_v0.1.19_arxiv.tar.gz` 446 KB · 27 pp / 786 KB PDF · **first R-round still OR-cap-blocked**.

**Headline finding**: galaxy chirality is statistically independent of cosmic-web environment within DESI DR1.

### 5 independent positive-evidence lines for the headline (each from a different statistical test):

| # | Evidence line | Result | n |
|---|---|---|---:|
| 1 | DESIVAST per-galaxy 0/6 cross-match at z≤0.24 | V-Web "voids" not in DESIVAST voids → V-Web low-z void class is survey-edge artifact | 6 |
| 2 | DESIVAST-anchored void classifier | f_CW^void = 0.4964 vs non-void 0.4971, Δ=0.0007 statistically indistinguishable | 56,981 |
| 3 | 3-algorithm DESIVAST robustness (VoidFinder/V2-REVOLVER/V2-VIDE) | All three \|Δf_CW\| < 0.002 | 56k-103k |
| 4 | Catalog-native V2-REVOLVER GALZONE membership | σ = **−0.24** near-perfect null | 86,276 |
| 5 | MAXIMAL voids HEALPix sky-position stratification | −5σ concentrated in **0-voids-per-pixel** bin; pixels with voids σ ∈ [−2.04, −0.09]; signal tracks survey-mask geometry NOT environment density | 378k-258k |

**Why 90% and not 95%**: P5 has never been through a 5-vendor R-round. The first R-round is blocked on the OpenRouter per-key weekly cap (see `NEEDS_HOUSTON.md` item 0). Once unblocked, R1 closes findings → bundled hard-fix wave → next round trajectory matches the other 5 papers' R23-clean pattern → 95%.

**arXiv categories**: astro-ph.CO + astro-ph.GA.

---

## The OR cap unblock (one action unblocks the final 5pp on P5 + ongoing R-round cadence on P1A/P1B/P2/P3/P4)

**Active key**: `sk-or-v1-c25e5...d15b3cbf` · internal ID `cdb1d2ef595c2ce98df9fa0add17a242adff5cfb9df1f8fcaba3c7b5f8345348`.

**Live state**: `limit=$50/week, usage_weekly=$98.66, remaining=$0`. The cap raise you attempted between cron fires #21 and #22 didn't propagate to the active key (verified via `/api/v1/key` readback every fire since #22, and via a live-fired 5-vendor R1 attempt on P5 at fire #43 which returned hard 403 across all 5 vendors).

**Two options, either fixes it permanently** (60 seconds either way):

- **(a) Raise the cap on the existing key**: https://openrouter.ai/workspaces/default/keys/cdb1d2ef595c2ce98df9fa0add17a242adff5cfb9df1f8fcaba3c7b5f8345348 → edit `limit` to $500/week (or remove entirely so only workspace credit gates spend).
- **(b) Rotate the key**: generate fresh OR key with no cap, paste into `bigbounce/.env.local` as `OPENROUTER_API_KEY=sk-or-v1-...`. Cron picks it up on next fire automatically.

Workspace credit is healthy at $83.47 remaining of $600 lifetime, so this isn't a credit problem — it's a per-key throttle.

---

## Submission workflow (recommended order)

1. **Sign off P1A** (cleanest paper, loop-exit milestone) → upload `arxiv/submission_tarballs/p1a_v1A.0.35_arxiv.tar.gz` to https://arxiv.org/submit
2. **Sign off P4** (R22+R23 cleanest P4 history) → upload `p4_v1.0.128_arxiv.tar.gz`
3. **Raise OR cap** → unblocks R26 across all 5 papers + first P5 R1
4. After R26 confirms 5/5 clean holds (~30 min after cap raise) → sign off P1B, P2, P3 → batch arXiv submissions
5. After P5 R1 closes → sign off P5 → arXiv submission

All 6 PDFs live at `public/papers/` and at https://bigbounce.hubify.app/papers/.
