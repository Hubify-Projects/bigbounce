# Houston sign-off packet — 2026-09-22

**Supersedes:** `project-context/HOUSTON_SIGNOFF_PACKET_2026-09-19.md` (still on
disk for history — do not delete). Everything below is re-verified fresh in
this session, not copied forward.

**Prepared by:** campaign lane `bb-L6c-verify-signoff` (Sonnet), campaign
`project-context/campaigns/CAMPAIGN_2026-09-18_publication_push.md`, criterion
A9 — a re-run of the tail of `bb-L6b-verify-signoff`, which established the
underlying hash/recompile evidence (see
`project-context/PORTFOLIO_VERIFICATION_2026-09-22.md` for the full per-paper
ledger this packet summarizes).

**Readiness semantics (directive P, `CLAUDE.md`):** 95 = every agent gate done
(science 25 + evidence/reproducibility 25 + automated review convergence 25 +
packaging/PDF hygiene 20); **100 only via Houston's literal per-paper
sign-off**, recorded as a quoted `APPROVE` in that paper's SSOT status file.
There is no 96. Venue/submission clicks, arXiv endorsement, and Houston's own
independent scientific read are a separate "publishing phase," never
subtracted from the 95 score.

**Convex is DOWN.** The deployment exceeded its spending limit as of
2026-09-21; the live site and every readiness/version write through it are
currently unreadable and unwritable by any agent. All figures below are the
last-computed SSOT/site-data values (hash-verified against files on disk this
session), **not** a live Convex read. Every intended Convex mutation since the
outage is queued in `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`,
ready to replay once you raise the limit.

---

## 0. One-screen summary

| # | Item | State |
|---|---|---|
| 1 | **Lineage choice (still yours, unchanged since 09-19)** | P1A vs P1N; P4+P5 vs P4P — both options preserved and functional, see §1 |
| 2 | **Papers at readiness 95, awaiting your literal APPROVE** | P1A, P1B, P2, P4, P5 (the historical five) |
| 3 | **Papers past 95** | P1N at 99 (D/P-round complete); everything else below 95 (A3M 75, AF 77, P-SU 72 — in-progress, not sign-off candidates yet) |
| 4 | **Hash integrity** | 12 of 13 SSOT papers verified clean end-to-end this session (served bytes internally consistent + content-identical to a fresh recompile). 1 real defect: A3M's *working tree* (not the committed/served bytes) is dirty with live uncommitted edits — see §6 |
| 5 | **Convex** | DOWN (spending limit) — **this is the current hard blocker for the live site and every readiness write**, not a paper-content issue |
| 6 | **arXiv endorsement (D4)** | Still open — codes emailed to `houston@bamf.ai`, need forwarding to qualified endorsers |
| 7 | **ORCID (D5)** | `0009-0008-5616-5994` — confirm public visibility |
| 8 | **GPU go/no-go** | Row-16(ii) mirror-injection GPU step RETIRED (exact algebraic identity found instead, $0); row-16(iii) D4-equivariant-retraining recommendation still in flight (lane `bb-LS6-row16-tta`, not done) |

---

## 1. Lineage reconciliation — READ THIS FIRST (unchanged choice, still yours)

Five papers currently carry SSOT readiness 95 and are the historical "sign-off
five": **P1A, P1B, P2, P4, P5**. Since `PAPER_LINEAGE_2026-08-05.md`'s
2026-09-02 portfolio restructure, **two of the five have been superseded by
newer, differently-scoped papers that also exist and are also live** (`P1N` at
99, `P4P` at 95). Nothing was deleted — this is a live choice about which
manuscript is the actual submission target. Both options remain fully
functional (tarballs, portal kits, DOIs all present for the originals):

| Original (still on disk, still ≥95, still has its own submission kit) | Superseding paper (also live, actively being finished) | What superseding means |
|---|---|---|
| **P1A** — `arxiv/paper1a_ech_nogo.tex` v1A.0.127, CQG Note, standalone algebraic no-go | **P1N** — `arxiv/paper1bc_ech_note/main.tex` v1N.0.6, readiness **99**, merges P1A + the frozen P1C no-go survey into one ≤12pp CQG/gr-qc Note. D/P-round complete (lane L3, DONE 2026-09-18). | If you submit P1N, P1A itself is not separately submitted — its content lives inside P1N. The CQG kit for standalone P1A (`SSOT/CQG_SUBMISSION_KIT_P1A_2026-07-24.md`) still exists if you'd rather ship it alone. |
| **P4** — `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.274, ApJS, 8.47M-galaxy catalog + observed-label dipole null | **P4P** — `pipelines/p4prime_chirality_test/paper/main.tex` v4P.0.10, readiness 95, folds P4 + P5 into one ≤15pp Poplawski spin-axis-exclusion test. Since 09-19: closed 6 further genuinely-new-real MAJOR + 4 MINOR (lane L4b), then propagated the row-16(ii-b) PA-parity-transfer result (lane L4d, withdrew an invalid pixel-injection tension claim, adopted a measured direct dilution bound) → v4P.0.10. | Submitting P4P means P4 and P5 are not separately submitted as standalone manuscripts. |
| **P5** — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.147-2026-08-03, AJ, DESIVAST void/non-void chirality null | *(same P4P as above)* | — |
| **P1B** — `arxiv/paper1b_namaster_proof.tex` v2B.0.23, JORS, namaster-proof software metapaper | *(no superseding paper — P1B stands alone)* | Not affected by the lineage decision. |
| **P2** — `research/focused_paper_source_integration/02_full_draft.tex` v1.7.130, PRD, f_NL = −35/16 derivation | *(folded as a theory section into A3M — but P2 itself was NOT retired; still a standalone PRD target. A3M is a separate flagship paper, readiness 75, R11 board in flight, not part of this packet's sign-off set.)* | Not affected by the lineage decision for sign-off purposes. |

**Recommendation (not a substitute for your call):** submit the
merged/folded versions (**P1N**, **P4P**) — that's what the 2026-09-02
portfolio restructure already decided editorially, and it's why this campaign
is actively finishing P1N (done, 99) and P4P (mid-confirmation) in parallel.
Submitting the older P1A/P4/P5 kits instead remains fully possible.

---

## 2. Per-paper evidence — the five sign-off candidates

All hashes below computed fresh this session (`shasum -a 256`, `pdfinfo`)
against files on disk. Convex cross-check is UNAVAILABLE (see header); the
"Convex" line for each paper below states that explicitly rather than a
stale-but-plausible-looking number.

### P1A — ECH algebraic Note
- **Version:** v1A.0.127 (unchanged since 09-19). **Served sha256** (5 paths, all match): `210be8f0b285…`, 8pp.
- **Convex:** UNAVAILABLE (was readinessComputed 95, houstonSignOff null, 0/0/0/0 open, as of 09-19's live check — not re-read live this session).
- **Open items:** `DISPOSITIONS/P1A.md` — 3 items, all disclosed scope-outs ("REMOVED FROM CLAIM SET; OPEN RESEARCH"), not hidden defects.
- **Submission target:** CQG. Zenodo DOI PUBLISHED `10.5281/zenodo.21481838`.
- **Superseded by:** P1N (§1).

### P1B — namaster-proof
- **Version:** v2B.0.23 (unchanged since 09-19). **Served sha256** (5 paths checked, all match): `c7cac6c9f16c…`, 16pp.
- **Convex:** UNAVAILABLE.
- **Open items:** 4 legacy rows in `DISPOSITIONS/P1B.md`, all CLOSED; current closure trail lives in `SSOT/paper-1/status.md` instead (DEFECT: DISPOSITIONS file stale relative to SSOT — routed, not fixed, see `PORTFOLIO_VERIFICATION_2026-09-22.md` §3.2).
- **Submission target:** JORS (needs 5 reviewer names + emails + fee/waiver decision from you). Software DOI PUBLISHED `10.5281/zenodo.21481753`.
- **Not affected by lineage** — stands alone.

### P2 — f_NL forecast
- **Version:** v1.7.130 (unchanged since 09-19). **Served sha256** (5 paths, all match): `d3afe79fe70c…`, 12pp.
- **Convex:** UNAVAILABLE.
- **Open items:** `DISPOSITIONS/P2.md`'s open-item count is not machine-countable (file predates the class:OPEN/CLOSED convention) — same routed defect as P1B.
- **Submission target:** PRD (APS account/ORCID/DAS checks needed from you). Zenodo DOI PUBLISHED `10.5281/zenodo.21461881`.
- **Not affected by lineage for sign-off purposes** — remains its own PRD target even though its theory content also echoes inside A3M.

### P4 — Observed-label chirality-dipole null + 8.5M-galaxy catalog
- **Version:** v1.0.274 (unchanged since 09-19). **Served sha256** (5 paths, all match): `2641a228af1e…`, 32pp.
- **Convex:** UNAVAILABLE.
- **Open items:** `DISPOSITIONS/P4.md` — 4 standing items, the two live ones (DP4-15/DP4-17) are disclosed OPEN-COMPUTE gates, exactly what the row-13/16 GPU program targets (§7).
- **Submission target:** ApJS. DOI PUBLISHED `10.5281/zenodo.21461899`.
- **Superseded by:** P4P (§1).

### P5 — DESIVAST catalog-native void non-detection
- **Version:** v0.1.147-2026-08-03 (unchanged since 09-19). **Served sha256** (5 paths, all match): `3c1c484118d2…`, 46pp.
- **Convex:** UNAVAILABLE.
- **Open items:** `DISPOSITIONS/P5.md` — 1 item; the target-program-by-environment interaction remains an honestly-disclosed systematic limitation, not an open defect.
- **Submission target:** AJ. **Zenodo DOI NOT yet minted** — explicitly gated to come *after* your sign-off (the one paper in this packet where sign-off unlocks a further irreversible agent action).
- **Superseded by:** P4P (§1).

---

## 3. P1N and P4P — the superseding papers, for context (not yet at your sign-off gate the same way)

- **P1N** — v1N.0.6, readiness **99** (highest in the portfolio). Served sha256 `1bb5ade7a9b7…`, 11pp, both mirrors match. `DISPOSITIONS/P1N.md`: 0 open. D-round + P-round both complete. This is the one paper where "Houston sign-off" is the *only* remaining gate (99→100), full stop — no further agent work pending.
- **P4P** — v4P.0.10, readiness 95. Served sha256 `054b63f8a739…`, 15pp, both mirrors match **and match the sha256 SSOT's own status file claims exactly** (independently re-verified, not just copied). `DISPOSITIONS/P4P.md` has 15 open R1-board items, but readiness 95 reflects the agent gates being complete via the row-16(ii-b) science propagation (which *withdrew* an invalid claim rather than closing findings item-by-item) — directive R2's review-round budget was refreshed by that intervening science decision; a fresh confirmation board is authorized next but has not run yet.

---

## 4. A3M, AF, P-SU — below 95, not yet sign-off candidates, included because your brief asked for all 12 SSOT papers

- **A3M** (Track A3 flagship) — v3M.0.27, readiness **75**. Committed/served bytes are clean and byte-identical across all mirrors. **R11 board is in flight**: its two raw reviewer legs (Gemini, Grok) are already saved to disk (`project-context/peer-reviews/INT_v3/ROUND_2026-09-21-A3M-v3M.0.27-EXACTPDF-3e49f29b-R11/`) but not yet truth-audited or closed — lane `bb-L1c-a3m-row9-r11` has not logged DONE as of this packet (checked multiple times; see `PORTFOLIO_VERIFICATION_2026-09-22.md` §4). `DISPOSITIONS/A3M.md` carries 15 open items pending that closure. Not a sign-off candidate yet.
- **AF** (anomaly flagship) — vAF.0.5, readiness 77. Spot-checked fresh and fully clean this session (fresh isolated recompile, 0 undef refs, content-identical to served bytes). R1 board closed 17/20 findings; 3 honestly disclosed open (OT-1 selection function [GPU], Zenodo DOI [Houston-only], plus the training-corpus/dedup/taxonomy items named in SSOT). Directive R2: round 1 of 2 spent. Not a sign-off candidate yet.
- **P-SU** (S12/S13/S15 criterion paper) — v1S.0.12, readiness 72. Clean, both mirrors match. R4 board complete, directive R2 budget spent — new gates S13/S15 carried as open, non-blocking science gates (not machine-tagged in DISPOSITIONS, same routed defect as P1B/P2). Not a sign-off candidate yet.

---

## 5. Cross-cutting notes

- **The "exact-version confirmation board" gap persists for all five sign-off papers**, same as 09-19: each paper's most-recently-*confirmed* multi-vendor board ran on a version several patch bumps behind current canonical bytes. Every intervening bump is individually closure-evidenced (real truth-audited findings or disclosed text/metadata-only edits), and every DISPOSITIONS ledger reads 0 live-open MAJOR for these five — but none has had a board run on its literal current PDF. If your bar requires a board on the exact final artifact, that hasn't happened for any of the five; if your bar is "every known finding closed/disclosed, agent gates complete," all five already meet it (readiness 95 encodes exactly that).
- **arXiv endorsement (D4) — still open.** Codes: gr-qc `HYEJ7S` (P1A/P1N), astro-ph.IM `L8TIPN` (P1B, P3), astro-ph.CO `LRZHC4` (P2), astro-ph.GA `CLVMAQ` (P4/P4P, P5) — emailed to `houston@bamf.ai`. Draft arXiv submission #7859751 parked at Start. Does not block journal submission (CQG/JORS/PRD/ApJS/AJ portals don't require arXiv; all DOI'd papers already have a citable permanent Zenodo record).
- **ORCID (D5):** `0009-0008-5616-5994` (correcting an earlier typo'd ID recorded 2026-07-21). Confirm PUBLIC visibility at `pub.orcid.org/0009-0008-5616-5994` before journal submission — several portals require it at account setup. Not re-verified live this session (no network fetch performed).
- **Convex spending limit — THE current blocker, new since 09-19.** The live bigbounce.hubify.app site and every readiness/version write have been down since 2026-09-21. This is purely an infrastructure/billing gate, not a science or paper-content issue — raising the limit lets the agent side replay the full `CONVEX_BACKFILL_QUEUE_2026-09-21.md` (paperVersions:bump, activityFeed:add, rRounds:create entries queued by every lane since the outage) in one pass.
- **RunPod GPU program — row 16 mirror-injection step RETIRED, no GPU spend needed.** Lane `bb-LS5-row16-finalize` found the row-13/16(ii) mirror-injection-at-larger-N step is resolvable by an exact algebraic identity instead of GPU compute ($0, 2026-09-21 17:22 PT). Its output (dilution bound D≤0.7166±0.0047, physical floor A₉₅^phys≥1.37%) is what lane L4d propagated into P4P v4P.0.10 (§3). The successor step, row-16(iii) D4-equivariant retraining, is a **new go/no-go still forming**: lane `bb-LS6-row16-tta` is mid-run (pre-registration + TTA-recovery + catalogue-wide d(180) + S6 dipole stages, last file write 2026-09-22 00:04 PT, no DONE logged) — its recommendation is not ready to present to you yet. Nothing here requires a decision from you this round; flagging so you know a GPU ask may follow once LS6 lands.

---

## 6. The one real defect this packet surfaces

`research/track_a3_multichannel/paper/main.tex` and `main.pdf` are currently
**dirty in the working tree** (uncommitted, real wording differences from the
committed v3M.0.27 — not just a recompile timestamp shift). This is almost
certainly live in-progress work by lane `bb-L1c-a3m-row9-r11` on the R11
board's closure (consistent with its raw legs already being saved but not yet
audited, §4). The committed and served PDF bytes are unaffected and internally
consistent across every mirror. **No action needed from you** — this resolves
itself when that lane commits its work; flagging only so you're not surprised
if `git status` looks busy on A3M when you check.

---

## 7. Exact Houston-only action list

Nothing below requires further agent work — every item needs your literal
input, click, or decision.

1. **Lineage choice (§1):** for P1A vs P1N, and for P4+P5 vs P4P, tell the
   agent side which manuscript(s) to carry to actual submission.
   (Recommended: P1N and P4P.)
2. **Per-paper sign-off (95/99 → 100).** For each paper you want moved to 100,
   record your literal `APPROVE` (or equivalent explicit sentence) in that
   paper's `project-context/SSOT/paper-N/status.md`:
   - **P1N** (readiness 99 — the one paper with nothing else pending) or P1A, per your §1 choice
   - P1B
   - P2
   - **P4P** (readiness 95, one board still pending — see §3) or P4, per your §1 choice
   - P5
3. **arXiv endorsement (D4):** forward the four endorsement-code emails
   (already sent to `houston@bamf.ai`) to qualified endorsers — 4+ astro-ph.*
   submissions in the last 3mo–5yr covers all three astro-ph codes; gr-qc
   needs 4+ gr-qc papers from the endorser. Only needed for arXiv preprints in
   addition to journal submission.
4. **ORCID (D5):** confirm `0009-0008-5616-5994` is flipped to PUBLIC
   visibility (`pub.orcid.org/0009-0008-5616-5994` should return your
   profile).
5. **Journal portal clicks** (after step 2's sign-off):
   - P1A/P1N → CQG
   - P1B → JORS (five reviewer names + real emails, fee/waiver decision needed from you)
   - P2 → PRD (APS account/ORCID/DAS checks)
   - P4/P4P → ApJS (confirm AAS acceptance of the declared HF-hosted dataset/model assets)
   - P5 → AJ (after sign-off, the agent side still needs to mint the immutable Zenodo tag/DOI and back-patch it before final AJ upload)
6. **Convex spending limit:** raise it so the live site and readiness writes
   resume; the agent side will replay `CONVEX_BACKFILL_QUEUE_2026-09-21.md` in
   one pass once it's back.
7. **RunPod GPU program:** no decision needed this round (§5) — the
   row-16(iii) retraining go/no-go is still being formed by an in-flight lane;
   expect a follow-up ask once it lands.
