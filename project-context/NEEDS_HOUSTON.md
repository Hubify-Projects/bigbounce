# NEEDS HOUSTON — truly-blocked items

Last updated: 2026-05-21 (cron fire #2 close — OpenRouter weekly key limit hit).

**Definition** (per Houston standing directive 2026-05-21): this file lists ONLY items that no agent can resolve — items that require Houston-only authority: personal sign-off, API/SSH credentials, arXiv endorsement, or something physical only Houston can provide.

Everything ELSE is being driven autonomously by agents. If an item is "out of repo scope" or "needs a pod" or "compute-bound" but I can spin up the pod myself, it does NOT belong on this list.

---

## 0. OpenRouter weekly key-limit reached · gates further R-rounds on all papers

**Why blocked:** Cron fire #2 hit `HTTP 403: Key limit exceeded (weekly limit)` from OpenRouter on all 5 P5 R1 reviewer calls (test attempt for first P5 R-round on the just-compiled v0.1.0 draft). Earlier in the session R23 (25 calls) and R24 (25 calls) and R25 (20 calls) all succeeded — the weekly bucket emptied between R25 and the P5 R1 attempt. The session has spent ~$3 of usable budget per call estimate; the weekly limit is on the API key itself, not the workspace balance. Agents cannot bump key limits.

**Ask:** Either (a) raise the weekly limit on the OpenRouter key referenced at https://openrouter.ai/workspaces/default/keys/cdb1d2ef595c2ce98df9fa0add17a242adff5cfb9df1f8fcaba3c7b5f8345348 — or (b) wait for the weekly reset (~7 days). The autonomous cron will continue firing every 30 min but will execute non-API-dependent work only (PDF recompiles, mirrors, site polish, P5 paper expansion, Tempel cross-validation) until the limit clears. Once clear, the next fire automatically resumes R-round cadence and pushes R26 + first valid P5 R1.

---

## 1. Personal sign-off on P1A v1A.0.34 for arXiv submission · gates P1A

**Why blocked:** P1A satisfies AGENT_RULES §4.4.1 cascaded-loop exit — 10th-consecutive Gemini-cosmology effective 0-BLOCKER on paper content (R23 BLOCKER was a prompt-meta error, audit-falsified) AND 3rd-consecutive 5-vendor clean round on content (R15+R16+R23 all 0/0 across DeepSeek + Gemini + GPT-5 + Grok + Perplexity). v1A.0.34 closed R23 Gemini M1+m1+n1 text-level findings + 3 pre-existing undef refs. The final 1% (90→100) is reserved for Houston-only judgment per feedback_99_pct_readiness_cap. No agent can flip this.

**Ask:** Read `arxiv/paper1a_ech_nogo.tex` end-to-end (or the live PDF at https://bigbounce.hubify.app/papers/paper1a_ech_nogo.pdf — 20 pp / 813 KB) and reply **"sign off P1A"** if ready, or send back blocking findings. After sign-off I build the arXiv tarball + smoke-test + (with arXiv endorsement) queue submission.

---

## 2. Personal sign-off on P4 v1.0.122 for arXiv submission · gates P4

**Why blocked:** R22 5-vendor returned 3 of 5 reviewers 0/0 (DeepSeek + Gemini + Grok). GPT-5 + Perplexity findings closed bundled in v1.0.122. R23 verification round returned **5 of 5 reviewers 0/0** (no regressions from v1.0.122 closures). After R23 clean, the final 1% is Houston-only.

**Ask:** Read `pipelines/p2_chirality/chirality_catalog_paper.pdf` (51 pp / 26.26 MB / 0 undef refs / 0 overfull) and reply **"sign off P4"** or send blocking findings. arXiv-tarball + submission queued behind sign-off.

---

## 3. arXiv endorsement + submission credentials (astro-ph.CO) · gates ALL papers

**Why blocked:** Only Houston has the arXiv account + the astro-ph.CO endorser relationships. Agents cannot create arXiv accounts or get endorsed.

**Ask:** Confirm submission order (recommended P1A → P4 → P3 → P1B → P2 → P5) and run the arXiv submission yourself when each paper is signed off. I prepare the tarballs.

---

## 4. DESI environmental VAC ("187 DESI-derived attributes" catalog) · gates P5 (optional — workaround exists)

**Why blocked:** Exhaustive sub-agent search (2026-05-15, reconfirmed tick 114) cannot locate this file in the repo or via any DESI public release. We have built a workaround (V-Web env_finder Phase 1 MVP, 104s laptop run on 14.6M spectro galaxies, headline result intact: chirality is statistically independent of LSS environment within DESI DR1 at V-Web resolution) but a published VAC is the gold-standard reference for the paper. If you do not have access to one, the V-Web workaround is sufficient and we proceed; if you do, share the path/DOI.

**Ask:** Either (a) provide the path/URL/DOI to the 187-attribute DESI VAC, or (b) confirm we proceed with the V-Web env_finder workaround as the paper's canonical environmental classifier. Option (b) is the default if no response.

---

## What is NOT on this list (autonomous work in flight)

The following are explicitly NOT Houston-blocked. Agents are driving them:

- HF model card refresh for `bamfai/galaxy-chirality-v2` (HF_TOKEN in `.env.local`).
- P5 Phase 2 sensitivity sweep + RSD correction + Tempel+2018 cross-validation (laptop-runnable).
- P5 paper draft expansion from 9 KB scaffold to first compiled PDF.
- Any further cross-vendor R-rounds (OpenRouter $99 credit available).
- Any LaTeX recompile / PDF mirror / site sync.
- Any pod work that can succeed via local source-build (e.g. the pymaster Apple Silicon build that closed P4 GPT-5 BL-4 last tick).

If anything above DOES end up needing Houston input mid-execution, it will be promoted to this list at that moment, not deferred to here preemptively.
