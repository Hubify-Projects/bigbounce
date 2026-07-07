# PUBLISH PATH — all 6 papers → 100% publish-ready (2026-07-05)

**Goal (Houston, explicit):** all 6 papers 100% ready to publish TODAY. Nothing deferred,
no caveats-as-excuses, no lazy science. Real compute (local CPU/GPU or RunPod) wherever a
result needs it. Fable-5 orchestrates; Opus/Sonnet workers execute; the DRIVE-TO-ACCEPT
cron (`98fd7458`, :17/:47) keeps the loop alive.

**The key structural unlock (corrects an earlier mis-read):** the "in-prep companion
papers" ARE THE OTHER PAPERS IN THIS REPO. P5's "Paper IV" = P4 (v1.0.217). P1A's
companions = P1B (+P2/P3/P4/P5 as cited). Nothing new needs writing. The dependency
closes with **coordinated submission**: wave 1 posts P4+P1B+P3+P2, their arXiv IDs are
assigned immediately at submission, wave 2 (P5+P1A) inserts the real IDs and posts the
same day.

---

## The two-wave submission plan (same day)

**Wave 1 (no dependencies):** P4 → P1B → P3 → P2
**Wave 2 (same day, after wave-1 IDs exist):** P5 (cites P4's ID) → P1A (cites companions' IDs)

Houston is the only human gate: he holds the arXiv account. Everything else below is
agent-executable and in flight.

---

## Per-paper: current verified state → remaining items → owner → done-today criterion

### P4 — chirality catalog (v1.0.217) — WAVE 1, FIRST
- **State:** Grok+Gemini MINOR, central claim "robustly supported"; INT ACCEPT (every
  number reproduces file:line); GZ1-human-only independence PROVEN (N=46,017, z=−0.54σ);
  residual EXCLUDED as cosmological (0.695% < A_50); tie-break leg-systematic.
- **Remaining:** (1) final fresh-eyes audit+fix ▸ *audit agent af6085f6, running*;
  (2) edge-on-ISOLATED coherence — catalog_production.parquet IS in local HF cache ▸
  *data agent a23da8f0*; (3) full per-pixel residual attribution — DR8 morphology via
  HF download or RunPod ▸ *data agent; spin pod if needed*.
- **Done today:** audit clean + packet verified; (2)/(3) fold in if data lands, else the
  committed exclusion bound already makes them non-blocking strengthening — the paper is
  submittable on its verified null either way. **→ Houston submits.**

### P1B — MCMC/NaMaster/ALP companion (v1B.0.100) — WAVE 1
- **State:** content error-clean (INT: all chains/numbers match; dimensional + M_Pl
  convention fixed); derived torsion→ΔN_eff bound is a real standalone result.
- **Remaining:** (1) audit + standalone-value framing + P1A-cross-ref placeholders ▸
  *audit agent a4c29bb7, running*.
- **Done today:** audit clean + packet verified. **→ Houston submits.**

### P3 — anomaly catalog (v3.1.138) — WAVE 1
- **State:** INT ACCEPT (byte-identical reproduction); anomalies proven real high-z
  quasars (198 at z>6, Mann-Whitney p~1e-103); headline 268,519 dedup exact.
- **Remaining:** (1) final audit+fix ▸ *audit agent abab4801, running*; (2) DESI
  score-vs-z extension — desi_zall.parquet via HF ▸ *data agent*.
- **Done today:** audit clean + packet verified; (2) folds in if data lands (strengthening,
  not blocking — SDSS demonstration already carries the claim). **→ Houston submits.**

### P2 — f_NL forecast + Cai/Li resolution (v1.7.94) — WAVE 1
- **State:** factor-of-2 RESOLVED to −35/16 (vertex-certified 3 ways — a genuine
  literature contribution); cubic transmission DERIVED; budget = computed-degeneracy
  bracket 0.8–1.3σ honestly disclosed; r=0.84 robust.
- **Remaining:** (1) audit + honest-forecast framing (leads with the two real
  contributions) ▸ *audit agent aa8cd57f, running*; (2) channel-native σ — Heinrich
  Cov_B if publicly available ▸ *data agent*.
- **Done today:** audit clean + packet verified; (2) folds in or is documented
  definitively unavailable (an honest final answer). **→ Houston submits.**

### P5 — DESI environmental chirality (v0.1.101) — WAVE 2
- **State:** INT verified every number exact; headline Δf_CW monopole-shift INVARIANT
  (depends only on public labels — refereeable independent of P4 internals).
- **Remaining:** (1) audit + Paper-IV→coordinated-submission reframe + GZ1-full-N cite ▸
  *audit agent a0bb92fe, running*; (2) insert P4's real arXiv ID after wave 1 (mechanical).
- **Done today:** audit clean + packet with ID-placeholder verified. **→ Houston submits
  same day, after P4.**

### P1A — ECH no-go (v1A.0.109) — WAVE 2
- **State:** every physics objection closed with real derivation: R3 derived (BS
  β-function, Δγ/γ=1.4e-6), ρ_Λ = single-scale NDA no-go (dim+1 → M_Pl⁴), operator basis
  proven complete, Route 2 one-loop-grounded (Shapiro-Teixeira) + NDA-bounded.
- **Remaining:** (1) audit + companion-imported numbers re-cited to THIS repo's committed
  artifacts (making them refereeable NOW) + coordinated-submission placeholders + NDA
  significance framing ▸ *audit agent ac425628, running*; (2) insert companion arXiv IDs
  after wave 1 (mechanical).
- **Done today:** audit clean + packet verified. **→ Houston submits same day, after wave 1.**

---

## Cross-cutting (all in flight)

- **Data/compute unlock** ▸ agent a23da8f0: HF inventory (HF_TOKEN), local cache check,
  RunPod (RUNPOD_API_KEY) spin-up authorized if a dataset genuinely can't come local.
  Targets: P4 DR8 morphology + edge-on-isolated, P3 desi_zall, P2 Heinrich Cov_B.
  Every result committed + verified; /backup-3plus on any pod.
- **No new MCMC required:** no reviewer item on any paper asks for new chains; the
  committed frozen chains are verified against the papers (INT). If any audit surfaces a
  chain-level gap, RunPod GPU is authorized — report before spinning.
- **After final versions land:** Convex bumps (done per-edit by directive-G) + site sync
  + this file updated with final versions/md5s + reviewTimeline entry for the publish round.
- **Referee-variance boundary (honest):** ChatGPT structurally REJECTs everything
  (directive H — not the gate). Grok/Gemini oscillate ±1 level on unchanged content
  (pattern-066). The gate is Grok+Gemini + INT-clean + verified science — P4 is there;
  the others' remaining items are listed above, all closing today.

## Definition of 100% (per paper)
1. Fresh full audit clean (this round) ✅→ in flight ×6
2. Every reviewer finding: closed by real science, or artifact-cited, or coordinated-
   submission-resolved — zero silent deferrals
3. Recompile 0 undef-refs, /latex-audit clean, three-way md5 (compile=served=Convex)
4. arXiv bundle standalone-verified + metadata + cover letter current
5. Houston's sign-off + submission (the one human step)
