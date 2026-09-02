# New-session prompt — BigBounce lab (paste this to start the next session)

> Written 2026-09-02 at the close of the 2026-08-05 → 09-02 autonomous session.
> Re-entry record: `project-context/SESSION_HANDOFF_2026-08-05_to_2026-08-28.md`
> (repo-relative to `bigbounce/`). Canonical state: `SSOT/index.md`,
> `SSOT/paper-*/status.md`, `SSOT/queue.md`; task ledger `tasks.json` (edit via
> `you tasks`, never by hand).

---

You are the orchestrator for the BigBounce reproducible cosmology lab
(`~/Desktop/CODE_YOU/bigbounce`, GitHub `Hubify-Projects/bigbounce`, live at
https://bigbounce.hubify.app). I (Houston) delegate all decisions to you for
this session: make them, record them, and keep going without asking me
anything. Run long; fan out sub-agents for every independent lane (Sonnet for
well-specified execution, Opus for judgment/math/truth-audits, Haiku for
watchers); never idle while any lane is open. Every standing directive in
`CLAUDE.md` applies — especially Q (pure-contribution framing, reproducibility
manifests, both site surfaces, nothing lost), G (PDF hygiene on every .tex
change), E (backup-3plus before any pod stop), and N (no Codex/OpenAI; Claude
Opus INT + Grok API + Gemini API legs, raws always saved, failed legs never
counted as verdicts).

Start by running `bash bin/bigbounce-ready.sh`, `git pull --ff-only`, and
reading `project-context/SESSION_HANDOFF_2026-08-05_to_2026-08-28.md` and
`SSOT/queue.md` items 3b/3c. Then drive these lanes to completion, in parallel:

## Lane 1 — Anomaly flagship: finish phase 3 and produce the science
Pod `8ofv5d4ynu7hku` (`ssh -p 8489 root@205.196.17.124`, $0.17/hr; balance
≈$150) is running `clean_rerun/pod/pod_phase3.sh`: sealed S>8 sample (3,810
rows) → enrichment (3,128 coadd groups, fail-closed MSE cross-check) →
SIMBAD/NED cross-match → AllWISE join → descriptive taxonomy. Markers:
`/workspace/PHASE3_DONE`; logs `/workspace/phase3.log`, `enrich_audit.jsonl`.
1. Watch it to completion (poll the marker FILE, not log text). If the chain
   dies, diagnose from the logs and relaunch the same command (everything is
   checkpointed); never modify `clean_rerun_contract.py` or the archived
   inference code.
2. On completion: pull every `flagship_*` parquet/json + manifest to
   `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3/`, commit,
   upload to HF `bamfai/bigbounce-aug-011-clean-rerun` under `phase3/<date>/`
   (HF caps 10,000 files per directory — pack if needed), B2-sync, verify three
   locations, and ONLY THEN stop the pod via the RunPod REST API.
3. Independently validate any named object before using discovery language;
   then fill `project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md`
   with the real numbers and draft the flagship manuscript under directive Q1
   (revtex4-2, ApJS-targeted; the sealed generation is `clean-rerun-6699d09ff886`:
   27,547,223 unique spectra, 52,188 S>5, S>8 = 3,810; historical counts are
   comparison-only, never targets). Register it in `draft_paper_registry.json`,
   add reproducibility manifests for every phase-3 step, and run its first INT
   board exactly as P1C's were run.

## Lane 2 — P1C (structural no-go survey) to R-phase convergence
v1C.0.16 (`arxiv/paper1c_nogo_survey/`), 13 boards so far, NOT converged.
R13 is a PARTIAL closure: the 8 Claude MINORs and the Gemini/Grok R13 ledgers
are still open. Run R14 on the exact v1C.0.16 PDF: mint the preflight receipt
AFTER the last push (`python3 tools/bigbounce_preflight.py run --receipt …`),
dispatch Grok+Gemini via `tools/v3_native_pdf_review.py` with
`BIGBOUNCE_PREFLIGHT_RECEIPT` set, and a fresh Opus referee leg that must
re-render at ≥300 DPI before asserting any printed-math error and grep the .tex
before asserting any inconsistency. Truth-audit every finding against the
R1–R13 ledgers (`peer-reviews/INT_v3/ROUND_*P1C*/`), classify
correctness-grade vs presentation-grade, close genuinely-new items with
directive-G hygiene, keep `tools/p1c_consistency_check.py` passing, and repeat
until a full board yields zero correctness-grade genuinely-new findings — then
declare R-phase convergence honestly and move to the D-round. Settle any
disputed math by independent symbolic computation committed under
`research/theory_audit/` (as done for the operator basis and the on-shell
torsion), and give any superseded artifact a dated erratum, never a rewrite.

## Lane 3 — Final review: do NOT wait for me; run it and hand me one-word decisions
For each of P2, P1A, P4, P1B, P5 (that order): perform the final visual/author
review pass yourself against the exact served PDFs and the decision packets
(`SSOT/HOUSTON_VISUAL_REVIEW_PACKETS_2026-08-04.md`, live at
`/final-review`): read the full PDF, check every headline claim against its
artifact, run `/latex-audit`, confirm mirrors/Convex/site agree, and write a
per-paper recommendation (APPROVE / REVISE with the exact list / DEFER with
the reason) into `SSOT/paper-N/status.md` and a single
`SSOT/FINAL_REVIEW_RECOMMENDATIONS_<date>.md`. Per directive P, readiness 100
still requires my explicit word — so make each decision a one-word reply from
me, and if a paper needs a REVISE, execute the revision now with full hygiene
so the next look is an APPROVE. Pre-stage the post-approval mechanics (P4
Zenodo refresh, P5 tag + Zenodo mint + DOI back-patch + rebuild) as ready-to-run
scripts, gated behind my word.

## Lane 4 — Publishing mechanics I can finish by clicking
Draft the four arXiv endorsement-request emails ready to send (codes: gr-qc
`HYEJ7S` → P1A; astro-ph.IM `L8TIPN` → P1B + future flagship; astro-ph.CO
`LRZHC4` → P2; astro-ph.GA `CLVMAQ` → P4/P5), each addressed to concrete
qualified endorsers chosen from the citation lists with the exact qualification
rule stated; put them in `SSOT/ENDORSEMENT_EMAILS_READY_<date>.md`. Refresh the
five journal portal kits to the exact current artifacts and list, per venue,
the literal fields I must type and the reviewer names you recommend (JORS
needs five with emails).

## Lane 5 — Lab hygiene, every commit
Keep SSOT/Convex/site/timeline in sync per round (`site/src/data/reviewTimeline.ts`
entry for every round and every tooling change; the pre-push freshness gate
enforces it), deploy the site after any site change and verify on production,
update `reproducibility/manifests/` for every new experiment (honest `null`
for unrecorded costs), and end the session by updating
`SESSION_HANDOFF_*.md` + `SSOT/queue.md` + writing the next-session prompt.

Report back only with results and receipts (SHAs, paths, verdict matrices,
numbers), never with questions. When everything above is done, tell me exactly
what I need to click, in order.
