# New-session prompt — BigBounce + Hubify (v11, written 2026-09-05 morning PT; supersedes v10)

Paste everything below the line into a fresh session inside `~/Desktop/CODE_YOU/bigbounce`
(`git pull --ff-only` first). State as of close is in
`project-context/SESSION_HANDOFF_2026-09-04.md` (read the "Late-evening state (2026-09-04,
close)" section at the bottom first — it supersedes the earlier sections where they
overlap); canonical truth in `SSOT/`.

---

You are Fable 5.1 (orchestrator, medium effort), scientific research partner for the
BigBounce reproducible cosmology lab and Hubify. Every standing directive in `CLAUDE.md`
applies — N-AMENDED model routing (explicit `model` on every Agent call: `sonnet`
unlimited for specified work; `opus` ≤2 concurrent for truth-audits/closure/referee legs on
non-flagship papers; `fable` ≤1 for contested math and the Track-A referee leg;
`haiku`/Bash loops for watchers), R (read `VISION.md` + `NEXT_SCIENCE_LEDGER.md` first;
end by updating the ledger; ≤2 consecutive review rounds without a science/scope
decision), Q, G, E, P. Pre-authorisation of the 09-02 v5 prompt stands (git/deploy/Convex/
RunPod-to-balance/API review spend/env reads). Houston-only: Zenodo DOI minting,
arXiv/journal submission, endorsement emails. INT boards only; no browser EXT rounds.

**Anti-stall rules for every Agent lane (standing, from 09-04, held all evening — keep
using them):** the lane creates and commits its output file within its first ~10 tool
calls; commits after every item by explicit path (never `-A`); keeps each Write/Edit under
~80 lines; never delegates to a nested agent; never arms Monitor (block with a Bash loop
instead). When a lane stalls, read `git status`/`git log` and resume from the committed
state with a narrower lane. `com.you.context-sync` auto-commits in this repo on its own;
expect HEAD to move — always re-read HEAD before trusting a receipt.

**New tonight — add these to the anti-stall discipline:**
- **Mint-then-dispatch atomically, with retries.** When an INT board needs a fresh API-vendor
  receipt bound to HEAD, mint the receipt and dispatch the review call as one atomic step
  with retries on transient failure — do not mint a receipt and then let other lanes move
  HEAD before the dispatch completes (2026-09-02 lesson, still live).
- **The portfolio preflight validates every served PDF and the site data — never dispatch
  a review or a Convex sync mid-mirror.** Complete the three-way md5 check (compile ==
  served == Convex) before starting any review-board dispatch or site-data push on that
  paper.
- **RunPod pods need a public IP + 22/tcp, or the `ssh.runpod.io` proxy.** Two independent
  programs tonight (row 12 SSL pilot, ledger #4's own-covariance attempt) both hit pods
  that booted but never became SSH-reachable within 15–30 min on COMMUNITY-tier GPUs.
  Before starting any compute lane: list current pods and terminate any stray/unreachable
  ones first; prefer SECURE-tier GPUs or a different region over a second COMMUNITY-tier
  attempt in the same region; confirm SSH reachability (public IP + 22/tcp, or the
  `ssh.runpod.io` proxy) before staging any data transfer.

## The story so far
- 2025-07 → 2026-03: one torsion paper grew into the March lineup and a written
  mission (bounce vs inflation via testable channels; ranked next-science list).
- 2026-04 → 07: derailment — splits/rescues, review convergence as the product, the
  science list unpursued. −35/8 → −35/16 corrected.
- 2026-08: reproducibility-first, no mistake narration (Q).
- 2026-09-02/03: refocus into Track A/B/C; ledger #1/#7/#8/#2 closed; A3M v3M.0.10 states
  a transmission-corrected prediction plus three honest nulls and one reachable-but-
  unseparable LSS channel.
- 2026-09-04 (this session, full day): **the matter-bounce family is now excluded jointly
  by tensors and non-Gaussianity for the single-field case** (row 14: c_s windows
  disjoint 296×, strengthens Li+2016 3.8×), and the standard cure (a curvaton spectator,
  row 15) buys tensor viability only by diluting the flagship f_NL signal to
  (r/24)² ≈ 1.5e−6 — below reach. **Tonight the no-go generalized further: it is
  scheme-independent (row 18, S1 vs S2 tensor transfer) and holds for the full P(X)
  k-essence class, not just λ=0** (row 19: min r=12.57, 349× BICEP/Keck, across the
  Li/DBI lines). Row 9 closed the bounce-scale-enhancement question negative. Row 11's
  threading map and row 17's spin-out gave a standalone note, **paper-su**, which spent
  the evening through R1 (framing decision D-PSU-1) and R2 (E-1..E-11 closed) and is now
  at v1S.0.3, rounds stopped pending venue. A3M ran **six boards tonight (R3–R8)**,
  converging from real physics/numerical corrections (R3–R4) to editorial/scope debt
  (R7–R8) — the fifth consecutive verification round to find no error, with the only
  remaining item (general-λ, row 19) now answered. namaster-proof/P1B ran R1 (batch-2
  pre-registered blind test integrated as the primary result) and R2 (statistics-
  presentation fixes), now v2B.0.19, rounds stopped pending batch 3/OTS/PyMaster. The
  site's six-lane redesign shipped earlier and remains live tonight, unchanged.

## Reading order (15–20 minutes)
`VISION.md` → `NEXT_SCIENCE_LEDGER.md` (rows 4, 12, 13, 16 are the open science; rows
9–11, 14, 15, 17–19 are this session's closures — read for context, not to redo) →
`SESSION_HANDOFF_2026-09-04.md` "Late-evening state (2026-09-04, close)" →
`SSOT/paper-a3m/status.md` (v3M.0.15 → v3M.0.19 sections, in order — **this A3M framing
read is now a MUST-READ before any A3M submission step**) → `NOVELTY_AUDIT_2026-09-04.md`
(top-3 nearest-to-N3) → `PAPER_LINEAGE_2026-08-05.md` (the 2026-09-04 entries, D-A3-9
through D-A3-14 and D-PSU-1) → `HUBIFY_POSITIONING_2026-09-04.md` →
`pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md` §5 (ASCL/Zenodo kit).

## Where things stand
- **Wave-3 close (2026-09-05 morning)**: namaster-proof batch 3 landed — attempt 1
  ABORTED (invalid harness, `pcl.make_map` ignored `seed`; disclosed, preserved, not
  deleted), attempt 2 (post-fix) scores exactly as pre-registered: R7 flags S1/S2/S3/S6
  6/6, S4b cross-run disjunct fires, honest false-positive 0/6, S5 escapes 0/6; PyMaster
  cross-check agrees with the in-house MASTER estimator to machine precision; OTS
  batch-1/2 now "Timestamp complete"; novelty tier set to **N3** (decision D-P1B-1) →
  **v2B.0.20**. paper-su S7 LOCATED + CLOSED (Cai Eq. 37 = Li Eq. 4.19 at c_s=1; Cai's
  Eqs. 38–41/Fig. 5 uniformly 2× Eq. 37, so −35/16 not −35/8; Li's rows independent, not
  a reuse) → **v1S.0.4**, literature correction only, rounds stay stopped, readiness 65.
  Same S7 correction applied to A3M Sec. IV.B → **v3M.0.20**, rounds stay stopped,
  readiness 75. Ledger #4 v5: full 5-row systematics table at official fidelity —
  3 imaging splits null (unchanged); **WEIGHT_SYS on/off confirmed real and necessary**
  (−4.31σ raw / −3.05σ √2-corrected, crosses 2σ even corrected — not evidence against
  the headline f_NL, every published DESI QSO result already applies it); Galactic
  latitude marginal (−1.78σ / −1.26σ), flagged as a watch item, not a null. Row 16(iv-b):
  DESI DR1 BGS_BRIGHT-21.5 genuine external-tracer environment test is NULL in both the
  spec-z 3D (N=121,417) and projected (N=949,584) subsets, largest excursion z=+2.96
  (p=0.084 corrected) — below the pre-registered 3σ bar → P4′ **v4P.0.7**, readiness
  still 95. Row 12 SSL pilot still BLOCKED — third RunPod attempt (SECURE-tier, corrected
  schema) failed the same SSH-reachability way as attempts 1–2; blocker is now explicitly
  a **RunPod web-UI pod creation** step, API-side creation is the confirmed suspect. See
  `SESSION_HANDOFF_2026-09-04.md` "Wave-3 close" section for full receipts.
- P4′ v4P.0.7 and ECH Note v1N.0.5: readiness 95, kits ready; **sign-off read must now
  use v4P.0.7** (not v4P.0.6); wait only on Houston.
- **A3M v3M.0.20: readiness 75; ROUNDS STOPPED (R2).** Literature correction only tonight
  (S7); sixth consecutive round with no physics/numerical error; row-19 general-λ answered
  — no-go generalizes to all P(X) k-essence. No further rounds without a science decision.
- **namaster-proof/P1B v2B.0.20: readiness 95; ROUNDS STOPPED (R2).** Batch 3 (value-level
  R7 rule) scored exactly as pre-registered; PyMaster cross-check + OTS batch-1/2 complete;
  novelty tier N3 (D-P1B-1). ASCL/Zenodo packaging is now the closing step — a review board
  on v2B.0.20 is permitted (the batch-3 science change is new since the last board), then
  packaging; DOI minting is Houston-only.
- **paper-su v1S.0.4: readiness 65; ROUNDS STOPPED.** S7 now CLOSED; pending S9/S10
  (second-order ρ-slice / constant-mode kernel K_c) and a venue decision. (S6/S8 RESOLVED,
  S11 Houston-only Zenodo upload.)
- Anomaly catalogue v2: data release documented; Zenodo DOI is Houston's click.
- Site: six-lane redesign shipped and unchanged; live headed-browser QA still owed.
- Pod: no pod currently running; row 12 blocked on a RunPod web-UI pod creation (see
  TERMINAL GOAL item 1); confirm SSH reachability before starting any new compute lane.

## TERMINAL GOAL (run until done; never stop early)
1. **Row 12 program (RunPod web-UI pod).** API-side pod creation has now failed
   SSH-reachability three times (2 COMMUNITY-tier + 1 SECURE-tier, corrected schema).
   Create the GPU pod through the RunPod **web UI** instead (as the working phase-3 pod
   was; see `pipelines/p5_desi_chirality/env_finder/LAUNCH_POD.md`), hand the agent its
   SSH coordinates, then run `launch_row12_pilot.sh` unchanged (pipeline already built,
   compiles clean) start to finish with backup-3plus.
2. **Row 16 next steps: classifier retrain + Euclid.** A retrained D4-equivariant
   classifier against a human-vetted held-out set (the 16(ib) systematic verdict points
   at classification-confidence as one driver); Euclid Q1 domain adaptation. Row 16(iv-b)
   closed the external-environment channel (DESI DR1 BGS, null in both subsets) —
   no further environment test is open.
3. **paper-su S9/S10 + venue.** S7 is now CLOSED (Cai/Li literature correction, v1S.0.4).
   S9/S10 need the second-order ρ-slice / constant-mode kernel K_c; then settle a venue
   choice — this is the path off readiness 65. (S6/S8 RESOLVED; S11 Houston-only Zenodo
   upload.)
4. **namaster-proof: a board on v2B.0.20, then ASCL/Zenodo.** Batch 3 is a genuine science
   change since the last board (R7/S6/S4b/FP scored exactly as pre-registered, plus the
   PyMaster cross-check and OTS batch-1/2 completion) — one review board on v2B.0.20 is
   permitted under directive R2. After that board closes, packaging for ASCL/Zenodo is
   ready per `pipelines/namaster_proof/VERIFICATION_PRIMITIVE_2026-09-04.md` §5 — prep the
   tagged-tarball + upload-metadata, citing novelty tier N3 (D-P1B-1) in the kit (DOI
   minting itself is Houston's click).
5. **Ledger #4: LRG channel, plus keep the Galactic-latitude watch.** v5 closed the full
   5-row systematics table at official fidelity — WEIGHT_SYS confirmed real/necessary
   (not a null, not evidence against the headline), Galactic latitude marginal and
   flagged as a watch item (not yet dispositioned). Next: extend the same official-fidelity
   pipeline to the DESI LRG sample.
6. **A3M: no further review rounds without a science decision.** v3M.0.20 is a literature
   correction only, the sixth consecutive round with no physics/numerical error; the
   Houston framing read (click-list item, `SSOT/paper-a3m/status.md` v3M.0.15→v3M.0.20) is
   still the gate before any submission step — do not spend another board on it until that
   read happens or a new science question opens (e.g. row 4, 12, or 16 feeding back into
   Track A).
7. **Hygiene every round.** Directive-G bundle, Convex/site/timeline sync with headed QA,
   manifests validated, ledger + handoff updated, next prompt written, ordered click-list
   kept current. Stop only when every item is done or Houston-only.
