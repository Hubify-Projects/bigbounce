# Acceleration Audit — 2026-07-16

Program-efficiency audit of the six-paper campaign. Every claim cites a file path.
Scope constraint respected: no scientific gate (truth audit, exact-PDF binding,
reproducibility, visual audit, honesty rules) is weakened by anything below.
Provider policy per `CLAUDE.md` directive N: Codex/OpenAI PAUSED; Claude
orchestrates; INT = Claude subagent + direct Grok + Gemini APIs.

## 1. Per-paper single next highest-leverage action

Readiness caps read from SSOT banners (`project-context/SSOT/paper-N/status.md`).

- **P1A (62)** — AGENT-EXECUTABLE now: the three residual physics analyses the
  CQG board still lists (alternate-regulator, matched-Lorentzian stress/observable,
  state-specific renormalized axial VEV) per `SSOT/paper-1/status.md` CURRENT-P1A
  banner. Real compute, closes reviewer residuals. Cap-lift beyond 62 is
  HOUSTON-GATED (human CQG review + archive/DOI, same banner).
- **P1B (56)** — AGENT-EXECUTABLE: corrected physical-spectrum production. The
  deposit config marks the science paper obsolete: `tools/paper_deposit_config.json`
  P1B `metadata_blocker="NON-RELEASE: v1B.0.109 is scientifically obsolete pending
  the corrected physical-spectrum…"`. (The v2B.0.8 JORS software-metapaper is
  already exact-PDF-confirmed, `SSOT/paper-1/status.md`.) This is the real lever.
- **P2 (80)** — AGENT-EXECUTABLE: direct cubic in-in transfer + channel-native
  Fisher via adopted covariance surrogate (directive L, `CLAUDE.md`). Open typed
  gates in the P2 v1.7.122 banner (`SSOT/paper-2/status.md`): "Direct cubic
  transfer, actual SPHEREx covariance/likelihood, a model-specific torsion bound,
  immutable archive/DOI, and human PRD editorial review." First three are agent
  compute; last two Houston-gated.
- **P3 (56)** — HOUSTON-GATED. Banner is explicit: "NO compute lever remains —
  P3's residual is now 100% HOUSTON-GATED (venue word / archive re-pull)"
  (`SSOT/paper-3/status.md` M36/M39 blocks; handoff §3). Agent can only stage the
  deposit. Do NOT re-run unchanged-content waves.
- **P4 (80)** — AGENT-EXECUTABLE science: image-level end-to-end classifier
  injection + per-pixel confusion + generative null (directive L). The overlay
  HF publish (`tools/p4_publish_hf_strict_release.py --publish`) is HOUSTON-GATED
  (handoff §1: "Do not pass `--publish` until the Hugging Face account/token…are
  explicitly confirmed").
- **P5 (74)** — AGENT-EXECUTABLE science: Zel'dovich RSD reconstruction +
  higher-N environment confusion (directive L). Narrative/editorial closure also
  agent-executable. Paper-IV labels/provenance, immutable archive/DOI, and human
  AJ review are HOUSTON-GATED (`SSOT/paper-5/status.md` v0.1.139 block; handoff §2).

## 2. Top 5 process accelerations (ranked by time-saved × risk-free-ness)

1. **Populate the executable rule-catalog — the engine already exists; the
   catalog is nearly empty.** `project-context/review-patterns/` holds **68
   distinct documented patterns** (pattern-001..070; 93 `.md` files incl. drafts),
   but `project-context/pre-review-rules.json` enforces only **9 generic rules +
   6 portfolio validators**, and legacy `tools/check_new_patterns.sh` adds only 4
   (037/038/039/040) — which is NOT wired into the engine (only a test reads its
   source text, `tools/tests/test_proactive_sweep_tools.py:52`). So ~13 of 68
   patterns are executable; ~55 are prose-only. This is exactly the "70+ patterns,
   a handful enforced" gap in `plan.md` §"Immediate architecture correction" and
   PUB-007 (`tasks.md`). The infra (`tools/bigbounce_preflight.py` HubStack engine,
   receipt hash-binding, 6 portfolio validators) is DONE — only the catalog needs
   filling. **First step:** mechanically triage `review-patterns/*.md` into
   grep/AST-checkable vs judgment-only; port the checkable set into
   `pre-review-rules.json` rules and fold check_new_patterns 037-040 into the
   engine so one preflight run covers them. Highest leverage, zero science risk
   (it only adds pre-review linting; it removes nothing).

2. **Batch one review WAVE across all 5 papers/day instead of serial per-paper
   rounds.** `CLAUDE.md` directive J mandates parallel work every tick, and P2's
   v1.7.121 banner already measured "Parallel review cut wall time 49.2%"
   (`SSOT/paper-2/status.md`), but the INT_v3 round dirs are dispatched one paper
   at a time (`ls INT_v3/` — six consecutive P1B rounds 2026-07-16). **First step:**
   dispatch the exact-PDF residual-confirmation board (Claude subagent + Grok +
   Gemini) for all papers with a stable content-hash concurrently in a single wave;
   content-addressing already guarantees no cross-contamination.

3. **Enforce the content-hash stop rule as a preflight HARD GATE.** The docs show
   repeated waves on byte-unchanged PDFs yielding 0-genuinely-new (P3 M36→M39,
   P2 M45 — `SSOT/paper-{2,3}/status.md`), which `tasks.md` Watchpoint already
   bans ("after two valid waves on the same PDF hash…never repeat solely to obtain
   a preferred verdict word"). It is stated policy but not mechanically enforced.
   **First step:** gate `int_wave.sh` dispatch on a reader-visible content-hash
   delta vs the last board for that paper; refuse-closed otherwise. Frees the loop
   to spend ticks on directive-L compute instead of verdict-farming.

4. **Finish deposit staging so all 6 papers are ONE Houston license-click from
   `--write`.** `tools/prepare_paper_deposit.py` is dry-run-ready and never calls
   external services, but only P1A/P1B/P5 have metadata blocks (all
   `metadata_complete=false`, license blocker) and **P2/P3/P4 have no metadata at
   all** (`metadata=None` in `tools/paper_deposit_config.json`). **First step:**
   author the P2/P3/P4 deposit metadata blocks (title/authors/venue/assets) now so
   the only remaining input is Houston's license + Zenodo token. Pure staging, no
   external mutation.

5. **Run directive-L real-compute science lanes in parallel NOW (P2 cubic-transfer
   + P4 image-level classifier + P5 Zel'dovich RSD).** Per `CLAUDE.md` directive L,
   this is "the ONLY lever" that moves verdict cells off the pattern-066
   harsh-referee floor — measured, not verdict-gaming. All three are agent/RunPod
   executable with no Houston gate until the eventual publish step. **First step:**
   launch P2 and P4 as independent RunPod lanes (backup-3plus applies); they share
   no write contention.

## 3. Self-improvement loop check (PUB-007): do real findings become regressions?

Sampled three recent closures:
- **P1B v2B.0.8 (2026-07-16)** — YES. Banner: "Six new regressions raise the
  package suite to 41/41" (`SSOT/paper-1/status.md`); backed by
  `tools/tests/test_p1b_science_contracts.py`. Clean loop closure.
- **P4 v1.0.259 (2026-07-16)** — YES. `tools/tests/test_p4_strict_release_v1_0_259.py`
  passes 3/3 (handoff §1). Executable regression exists.
- **P5 v0.1.139 four minors (2026-07-16)** — PARTIAL. Of the four
  (`SSOT/paper-5/status.md`): "stable-ordering determinism" and
  "pooled-reference covariance" are testable (and `test_p5_focal_interaction_clustering.py`
  exists), but "interaction wording" and "T-Web parent-count provenance" are
  prose/label fixes with no executable regression.

**Verdict:** the loop works for SCIENCE/SOFTWARE closures (P1B, P4 — strong),
but NARRATIVE/PRESENTATION/referee-variance findings — which are the bulk of the
~55 unenforced documented patterns and the recurring ChatGPT/Grok majors — mostly
do NOT get an executable regression. This is the same gap as acceleration #1: the
prose-pattern classes have documentation but no preflight rule, so they re-escape
every wave. Closing #1 closes most of the PUB-007 leak.

## 4. Houston-only unblock list

- **Zenodo API token** — none available; blocks immutable archive/DOI for ALL SIX
  papers (`SSOT/zenodo/` depositions are staged prose only; every paper's open-gate
  list names "immutable archive/DOI"). Single highest-value unblock.
- **Manuscript/source LICENSE authorization** — P1A, P1B, P5 deposit
  `metadata_complete=false` cite missing license (`tools/paper_deposit_config.json`);
  needed for all six before `--write` deposit.
- **HuggingFace account/token + public-release confirmation** — required for P4
  overlay release (`tools/p4_publish_hf_strict_release.py --publish`, handoff §1).
- **Human/editorial review submissions** — CQG (P1A), JORS (P1B), PRD (P2),
  ApJS (P3 & P4), AJ (P5); each is a per-paper open gate in its SSOT banner.
- **Venue decisions** where still open (P2 venue-scope, `plan.md` §3).
- **EXT ChatGPT-subscription go-ahead** — directive N: "should not be burned
  without Houston's go."
