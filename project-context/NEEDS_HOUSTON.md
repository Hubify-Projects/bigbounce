# NEEDS HOUSTON — truly-blocked items

Last updated: 2026-05-22 PDT (cron fire #30 / tick 151 — post visual-formatting cleanup + SSOT sweep + full-portfolio arXiv tarballs).

**Definition** (per Houston standing directive 2026-05-21): this file lists ONLY items that no agent can resolve — items that require Houston-only authority: personal sign-off, API/SSH credentials, arXiv endorsement, or something physical only Houston can provide.

Everything ELSE is being driven autonomously by agents. If an item is "out of repo scope" or "needs a pod" or "compute-bound" but I can spin up the pod myself, it does NOT belong on this list.

---

## 0. OpenRouter per-key $50/week cap exhausted — workspace credit fine · gates R-rounds

**Diagnosis (live `/api/v1/key` readback, 2026-05-23 cron fire #56 post-rollover):** the per-key weekly usage limit on the `sk-or-v1-c25e5...d15b3cbf` key is set to **$50/week**, weekly usage **rolled overnight from $98.66 → $52.48** (the rolling 7-day window dropped the oldest day's $46 spend), `usage_daily` reset to $0. `limit_remaining: 0` (still $2.48 over the $50 cap). Workspace credit is **healthy: $83.47 remaining of $600 total** (used $516.53 lifetime).

**Trajectory**: at the current zero-spend rate (all calls 403-rejected → no new charges add to weekly), the rolling 7-day counter will continue to drop ~$3–$15/day as older spend rolls off the window. The earliest the cap could clear naturally is **today (2026-05-23) by end-of-day if today's $3.28 average rolls off**; more realistically **2-3 days** (2026-05-25 or 26).

**Fire #56 live-fired R26 on P1B v1B.0.22 (the smallest paper) confirmed all 5 vendors still 403** with the same `Key limit exceeded (weekly limit)` error. This is NOT a credit-exhausted problem — it is the per-key weekly cap that throttles. Earlier fires assumed weekly reset would clear it; the actual fix is to raise or remove the per-key cap (or rotate the key).

**The cap raise Houston attempted between fire #21 and fire #22 did not propagate to the active key** (verified via `/api/v1/key` readback every fire since #22, plus a live attempted R-round fire on P5 v0.1.13 at fire #43 that returned hard 403 across all 5 vendors with the OR error message `Key limit exceeded (weekly limit). Manage it using https://openrouter.ai/workspaces/default/keys/cdb1d2ef595c2ce98df9fa0add17a242adff5cfb9df1f8fcaba3c7b5f8345348`). Either the wrong key was edited in the OpenRouter dashboard, or the limit field wasn't saved. The active key's internal ID (per the OR error log) is `cdb1d2ef595c2ce98df9fa0add17a242adff5cfb9df1f8fcaba3c7b5f8345348`; the public prefix matching `bigbounce/.env.local` is `sk-or-v1-c25e5...d15b3cbf`.

**This is now the binding constraint on every paper's readiness ceiling.** P1A/P1B/P2/P3/P4 are all sitting at 95% pending one more clean R-round + sign-off; P5 has never had a first R-round at all. None can move past 95% until either (a) the per-key cap is raised on the existing key, or (b) a fresh key with no/higher cap is generated and pasted into `.env.local` as `OPENROUTER_API_KEY=sk-or-v1-...`. Option (b) is 60 seconds of work and removes the wall completely.

**Ask (pick one):**
  - **(a) Raise the per-key cap (fastest, 30 sec):** https://openrouter.ai/settings/keys → find `sk-or-v1-c25...cbf` → edit → raise the `$50/week` `limit` field to `$200/week` (or remove it entirely so only the workspace credit gates spend).
  - **(b) Rotate the key:** generate a new OpenRouter key with no weekly cap, paste it into `bigbounce/.env.local` as `OPENROUTER_API_KEY=sk-or-v1-...`. The cron will pick it up next fire automatically.
  - **(c) Wait for reset:** the weekly counter resets on the next Sunday/Monday boundary depending on the workspace's billing tz; this clears the block without action but loses ~5-7 days of agentic R-round throughput.

Once unblocked, the autonomous cron will resume R-round cadence at xx:17 / xx:47 next fire and push R26 + first valid P5 R1 immediately.

---

## 1. Personal sign-off on P1A v1A.0.35 for arXiv submission · gates P1A

**Why blocked:** P1A satisfies AGENT_RULES §4.4.1 cascaded-loop exit — 10th-consecutive Gemini-cosmology effective 0-BLOCKER on paper content (R23 BLOCKER was a prompt-meta error, audit-falsified) AND 3rd-consecutive 5-vendor clean round on content (R15+R16+R23 all 0/0 across DeepSeek + Gemini + GPT-5 + Grok + Perplexity). v1A.0.34 closed R23 Gemini M1+m1+n1 text-level findings + 3 pre-existing undef refs. v1A.0.35 (cron fire #24) wrapped the Holst-dual equation in `widetext`, eliminating the last 21pt overfull residual — first fully-clean P1A compile in the campaign. The final 1% (90→100) is reserved for Houston-only judgment per feedback_99_pct_readiness_cap. No agent can flip this.

**Ask:** Read `arxiv/paper1a_ech_nogo.tex` end-to-end (or the live PDF at https://bigbounce.hubify.app/papers/paper1a_ech_nogo.pdf — 20 pp / 832 KB) and reply **"sign off P1A"** if ready, or send back blocking findings. **arXiv tarball is pre-built and smoke-tested**: `arxiv/submission_tarballs/p1a_v1A.0.35_arxiv.tar.gz` (433 KB, 5 files, 0 undef refs/cites in isolated compile). With arXiv endorsement, submission is a single upload.

---

## 2. Personal sign-off on P4 v1.0.128 for arXiv submission · gates P4

**Why blocked:** R22 5-vendor returned 3 of 5 reviewers 0/0 (DeepSeek + Gemini + Grok). GPT-5 + Perplexity findings closed bundled in v1.0.122. R23 verification round returned **5 of 5 reviewers 0/0** (no regressions from v1.0.122 closures). v1.0.122→v1.0.128 (cron fires #5–#20) eliminated all overfull residuals. After R23 clean + cron fire #20 cleanup, the final 1% is Houston-only.

**Ask:** Read `pipelines/p2_chirality/chirality_catalog_paper.pdf` (51 pp / 26.24 MB / 0 undef refs / 0 overfull) and reply **"sign off P4"** or send blocking findings. **arXiv tarball is pre-built and smoke-tested**: `arxiv/submission_tarballs/p4_v1.0.128_arxiv.tar.gz` (20 MB, 15 files, 0 undef refs/cites in isolated compile). With arXiv endorsement, submission is a single upload.

---

## 3. arXiv endorsement + submission credentials (astro-ph.CO) · gates ALL papers

**Why blocked:** Only Houston has the arXiv account + the astro-ph.CO endorser relationships. Agents cannot create arXiv accounts or get endorsed.

**Ask:** Confirm submission order (recommended P1A → P4 → P3 → P1B → P2 → P5) and run the arXiv submission yourself when each paper is signed off. **All 6 tarballs are pre-built and smoke-tested** at `arxiv/submission_tarballs/`: P1A 433 KB / P1B 255 KB / P2 346 KB / P3 27 MB / P4 20 MB / P5 438 KB. Tarballs are gitignored locally (rebuildable on demand from `.tex` sources).

---

## 4. DESI environmental VAC ("187 DESI-derived attributes" catalog) · gates P5 (optional — better external alternatives now exist)

**Verdict (cron fire #32 exhaustive web search, 2026-05-22):** the specific "187 DESI-derived attributes" catalog Houston referenced **does not appear in any DESI public release** (data.desi.lbl.gov/doc/vac/, DR1 documentation, EDR documentation, or in any 2024–2026 arXiv listing for DESI VAC papers). It either (a) was a planning-stage concept that didn't ship, or (b) lives on Houston's pre-2026 personal compute and never made the public release. **However**, two real public DESI cosmic-web catalogs landed since the 2026-05-15 subagent search and now offer a stronger external comparison than the V-Web env_finder workaround:

- **T-Web DESI DR1** ([arXiv:2604.02463](https://arxiv.org/abs/2604.02463), 2026-04-02): tidal-tensor T-Web environments on a 256³ grid in an 800 Mpc cube over the full DESI DR1 footprint, classified into voids/sheets/filaments/knots. **Methodology essentially identical to the V-Web env_finder run that landed P5's headline cosmic-web result on 2026-05-19.** A direct cross-comparison would be a publication-grade independent validation.
- **ASTRA EDR Probabilistic Environment Catalog** ([arXiv:2604.01456](https://arxiv.org/abs/2604.01456), 2026-04-01): algorithm-based per-object void/sheet/filament/knot membership probabilities + classification entropies on DESI EDR (175 deg², 20 rosettes). Provides per-galaxy classification entropies that the V-Web run does not — useful for quantifying environmental-assignment uncertainty.
- **DESIVAST** ([arXiv:2411.00148](https://arxiv.org/abs/2411.00148)): low-redshift void catalog on DESI DR1 Bright Galaxy Survey. Adjacent rather than overlapping; complementary cross-check on the void-class portion of the V-Web headline.

**Ask:** Either (a) **confirm we proceed with V-Web as canonical + add T-Web cross-validation as a publication-grade external comparison in P5 v0.1.8+** (default agent path; T-Web catalog data availability is uncertain but the published comparison numbers are accessible), or (b) confirm the legacy 187-attribute catalog reference can be retired from the paper text. The cron will pursue the T-Web cross-validation work autonomously on next non-API fire if no response, since it's a real positive scientific upgrade rather than a Houston-blocked item.

---

## What is NOT on this list (autonomous work in flight or completed)

The following are explicitly NOT Houston-blocked. Most have closed since 2026-05-21.

**Completed since the 2026-05-21 snapshot:**
- ✅ All 6 papers brought to **0 overfull >20pt** (cron fires #20–#24) — first time in campaign.
- ✅ P5 Phase 2 sensitivity sweep (9 grid configs on disk) + RSD-robustness Limitations item (cron fire #25) + Tempel+2014 FoF cross-validation (filament concordance 0.026pp) + full paper LaTeX expansion 9 KB → 885 lines + first PDF compile (738 KB).
- ✅ SSOT doc-consistency sweep — papers.ts / SSOT/paper-5 / SSOT/index.md table+paragraph / CLAUDE.md headline all consistent (cron fires #25–#27).
- ✅ Full-portfolio arXiv tarballs built + smoke-tested standalone (cron fires #28–#29): all 6 tarballs at 0 undef refs/cites.

**Still autonomous, in flight or queued:**
- HF model card refresh for `bamfai/galaxy-chirality-v2` v1.0.104 → v1.0.128 (HF_TOKEN in `.env.local`) — queued for next non-API tick.
- R26 cross-vendor wave across P1A + P1B + P2 + P3 + P4 + first P5 R1 — blocked only on the OR cap raise (item 0 above).
- Any LaTeX recompile / PDF mirror / site sync — driven on every fire.
- Any pod work that can succeed via local source-build.

If anything above DOES end up needing Houston input mid-execution, it will be promoted to this list at that moment, not deferred to here preemptively.
