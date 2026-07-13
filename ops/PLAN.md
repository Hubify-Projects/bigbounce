# PLAN — bigbounce review-program

Mission, terminal criteria, current state, phase plan, decision log. Live paper
state is canonical in `project-context/SSOT/index.md` — this doc links to it and
never restates per-paper readiness numbers as truth.

---

## 1. Mission + terminal-criteria stack

**Mission:** prove bounce cosmology beats ΛCDM + inflation by driving six papers
(P1A/P1U, P1B, P2, P3, P4, P5) to ACCEPT from every reviewer, honestly — never by
prompt-gaming, never by watering down science.

The exit bar tightened over four directives (all in repo-root `CLAUDE.md`); **M
governs** and supersedes the earlier ones as the terminal criterion:

| Directive | Date | Bar | Role now |
|-----------|------|-----|----------|
| **J** | 2026-07-09 | literal 0 MAJOR / 0 MINOR / 0 REJECT from every reviewer; never-idle loop | honesty tool, not exit |
| **K** | 2026-07-10 | two consecutive full waves with 0 genuinely-new findings | CHECKPOINT (proven repeatedly) |
| **L** | 2026-07-11 | ALL-ACCEPT via the OPEN-COMPUTE science queue (not more text waves) | the *path* |
| **M** | 2026-07-12 | **/reviews grid CURRENT column = 100% ACCEPT across every paper × reviewer** | **TERMINAL — the only exit** |

Nothing less than M's all-A grid exits the loop. The cron never stops and no
paper's work pauses until then; all papers get parallel work every tick.

---

## 2. Current state snapshot

> **Live state is `project-context/SSOT/index.md` + Convex `readinessMetrics` —
> read those, not this snapshot.** Numbers below are a point-in-time read for
> orientation (as of the M39-EXT tick, 2026-07-13).

Caps: **P1A 68 · P2 74 · P3 56 · P4 80 · P5 80.**
Clean-wave streaks: **P1U 14 · P2 13 · P3 5 · P4 12 · P5 2.**

Every paper is past directive-K's two-clean-waves checkpoint. None is at the
all-A grid (directive M). See the honest floor analysis below for why.

### Honest verdict-floor analysis (pattern-066)

The residual gap is **not a content gap** — content is converged (every reviewer
finding across ~M9→M39 truth-audits to a source-cited `DISPOSITIONS/<P>.md` id,
an OPEN-COMPUTE item, or a disclosed scope limitation; genuinely-new real defects
now surface ~1 per 10 waves, last two closed + verified held: P2 v1.7.112, P5
v0.1.127). The gap is the **pattern-066 verdict-word floor**: the *same
byte-identical PDF* draws different verdict words each sweep.

- P4 Grok: ACCEPT → MINOR → MAJOR → MINOR on byte-identical v1.0.239 (M21→M33).
- ChatGPT: REJECT ↔ MAJOR on P4/P5, with **concede-inside-REJECT** tells (P2 M31
  ChatGPT REJECT literally says its own double-counting crux "may nevertheless be
  correct" — and that "fix" was falsified by re-running committed
  `p2_vertex_check.py` + the convention-free Li et al. closed form).

**What moves the verdict word, in measured order of effect:**
`compute/science closures  >  venue matching (P3-ApJS proven)  >  presentation
overhaul targeting the REJECT raw's own words  ≫  text-only re-review waves
(measured: text waves DO NOT move it, 15+ waves).`

Full catalog + evidence: `project-context/PROCESS_AUDIT_2026-07-14.md` §3.

---

## 3. Phase plan

### Phase 1 — loop-as-regression-net (RUNNING, autonomous)
The cron + watchdog keep waves flowing on every paper. Its job is now to **keep
measuring** (catch any regression / genuinely-new defect and close it) — NOT to
farm verdicts. A genuinely-new finding resets that paper's clean-wave streak and
is closed with a real edit/science before re-test. Runs unattended; the exit
levers are in Phase 2.

### Phase 2 — Houston-gated conversions (the only levers past the floor)
None are code-fixable; all require Houston:
- **arXiv wave-1 submission clicks** — P4→P3→P2 then P5+P1U; bundles re-verified against final versions (`submissions/WAVE1_SUBMIT_WALKTHROUGH.md`).
- **P3 venue word** — greenlight the ApJS variant (flip is proven; `submissions/P3_VENUE_DECISION.md`).
- **Zenodo DOI** — mint the P2 dataset/analysis DOI so channel-native Fisher + artifact citations resolve.
- **Cai email** — the P1U/P2 −35/16 vs Cai −35/8 companion coordination.
- **Billed Gemini API key** — converts the throttled browser-Gemini leg into an instant parallel API leg.

### Phase 3 — human referees
Route the floor papers (P1A/P1U, P2, P3) to human expert referees; LLM-referee
variance is exhausted as a signal. Briefing: `submissions/HUMAN_READ_BRIEFING.md`.

### Phase 4 — optional deep compute levers (directive L science queue)
Each is a *real computation*, not a text edit; each is followed by a full re-test wave.

| Lever | Paper | Effort (human-team) | Effort (CC+gstack) | Compression |
|-------|-------|---------------------|--------------------|-------------|
| Image-level classifier injection + per-pixel confusion + generative null | P4 | ~1 week | ~4 h (GPU-gated) | ~10x |
| Channel-native Fisher via adopted covariance surrogate + full cubic in-in | P2 | ~1 week | ~6 h | ~10x |
| Held-out end-to-end re-inference (22.5M archive re-pull) | P3 | ~3 days | Phase-1 DONE ($0, CPU-local, `2c52a1d2`); full re-pull structurally bounded (only ~1.31% re-pullable) — Houston-gated | — |
| Zel'dovich RSD reconstruction + higher-N env confusion | P5 | ~4 days | ~4 h | ~15x |
| Regulated NJL gap equation (operator-level) | P1U | ~1 week | ~1 day | ~5x |

Effort style per CLAUDE.md "AI effort compression"; the P3 full archive re-pull is a *structural* ceiling (`P3_REINFERENCE_PLAN.md` §3: 86.6% of released rows carry hashed negative tids with no archive linkage), not a compute ceiling.

---

## 4. Decision log

The big calls already made (date · sha where applicable):

| Date | Decision | Provenance |
|------|----------|------------|
| 2026-07-01 | Convergence gate recalibrated: Grok+Gemini ACCEPT + every ChatGPT MAJOR truth-audited non-real (ChatGPT literal ACCEPT no longer required — structural harsh-referee floor) | directive H, `CLAUDE.md` |
| 2026-07-01 | pattern-066 refinement: operative test = "0 genuinely-new real findings", not a literal single-sweep ACCEPT | directive H-refined |
| 2026-07-10 | Two-clean-waves checkpoint adopted | directive K |
| 2026-07-11 | ACCEPT-bar restored via OPEN-COMPUTE queue (text waves proven not to move verdict words) | directive L |
| 2026-07-11 | **P3 ApJS venue flip** — ApJS-framed reviews are legitimate reviews of the same science (the one lever that measurably moved a verdict word) | `submissions/P3_VENUE_DECISION.md` |
| 2026-07-12 | All-A grid is the terminal criterion | directive M |
| 2026-07-13 | **DP3-15 end-to-end re-inference at structural ceiling** — full-catalog archive re-pull is Houston-gated (hashed-tid majority unrecoverable), no compute lever remains for P3 | `e70e418e` + `2c52a1d2` |
| 2026-07-13 | **DP4-22 closure** — edge-on sensitivity penalty sqrt→linear (v1.0.240) | `39b7aed1` |

Integrity across every decision is absolute and unchanged: never fake an ACCEPT,
never prompt-game, every leg saves its raw, dispositions stay source-cited.
