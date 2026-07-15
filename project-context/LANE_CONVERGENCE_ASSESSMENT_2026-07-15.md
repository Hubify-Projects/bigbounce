# Lane convergence assessment — 2026-07-15

**Author:** Claude lane orchestrator (Fable 5). **For:** Houston decision.

## What happened
The two-lab parallel setup you asked for is running for real — but the **Codex
lane has become the primary driver of the entire pipeline**, faster and deeper
than the Claude lane, to the point where continued parallel operation of the
Claude lane now creates more contention than value.

Evidence (all observed this session):
- **Papers:** Codex drove P4 v1.0.240 → **v1.0.255** (~15 closure iterations:
  morphology contract, release-integrity board), P3 → **v3.2.0-r8** (new DESI
  science-catalog rebuild), P1B RunPod launcher + pod lifecycle, and created
  **P1A** as a new Classical & Quantum Gravity Note (**v1A.0.123**) distinct from
  the Claude lane's P1U (`paper1_unified.tex`, v1U.0.20).
- **Tooling:** Codex rebuilt the INT system — `review_packet.py` "canonical
  packets," "exact waves," **preflight receipts** (`bigbounce_preflight.py`,
  SHA-pinned artifact binding), Codex-subscription receipts. The Claude lane's
  `int_wave.sh` old path now errors (`--preflight-receipt` required).
- **Browser:** both lanes toggle one gstack browser; it keeps reverting to
  headless (Codex driving it too) → Claude-lane EXT effectively blocked.
- **Git:** Codex commits every ~1–2 min; Claude-lane pushes lose the race
  repeatedly.

## Claude lane's verified state (preserved, honest)
P1U streak 18 · P2 streak 19 (ChatGPT floor-lifted REJECT→MAJOR, stable 2 rounds,
cap 80) · P5 streak 9 (ChatGPT 7th consecutive MAJOR). These are real, recorded,
committed. **P2's floor-lift is the campaign's best honest verdict-gap movement.**

## Why the Claude lane is now blocked (all external, none fabricated)
1. ChatGPT daily rate limit exhausted (auto-resets).
2. Browser contention with Codex (no lease wired in).
3. INT tooling superseded by Codex's packet/preflight system.

## The decision (yours)
The `MULTI_LAB_DESIGN.md` blueprint anticipated this — it needs the coordination
layer that isn't wired in yet. Pick one:

- **(A) Consolidate to one lane (Codex primary).** Codex is doing the deeper
  science + integrity work; let it own the pipeline. Claude lane stands down from
  active driving, remains available for orchestration/synthesis/review-of-Codex.
  Simplest; ends contention immediately.
- **(B) True partition per MULTI_LAB_DESIGN.md.** Wire `lab_lease.sh` into BOTH
  lanes' browser path + add Convex `labId` so each lane has its own grid columns
  and can't overwrite the other. Enables genuine independent-replication (the
  strongest evidence class). Needs Codex to honor the lease — a cross-lane change
  only you can mandate.
- **(C) Explicit ownership split, shared taxonomy.** Codex owns P1A/P1B/P3/P4
  science closures; Claude owns P1U/P2/P5 review rotation; reconcile whether P1A
  (CQG Note) replaces or supplements P1U. Keeps both lanes but removes the
  double-count + browser fight.

**Recommendation: (A) now, (B) later.** Consolidate to the Codex lane immediately
to stop the contention and let the strongest driver run unblocked; revisit true
labId-partitioned replication (B) once the papers stabilize and you want the
independent-replication evidence for the venue critique.

Until you decide, the Claude lane holds its verified state, keeps the heartbeat
alive, and does NOT fabricate activity or fight superseded/contended tooling.
