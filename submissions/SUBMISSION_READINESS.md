# Submission Readiness Dashboard — bigbounce

**Status as of 2026-07-04 (verified).** One decision surface for Houston's venue calls + human-referee routing.

> **Honest headline:** The autonomous LLM-review loop is **complete and exhausted.** All 6 papers are **content-honest and error-clean** (every concrete error fixed + reviewer-confirmed lifted). **None are converged** to all-3-ACCEPT — every paper draws a real ChatGPT REJECT, but uniformly on a **venue/scope** question that LLM referees flag and cannot adjudicate. That judgment belongs to **human referees.** Editing scope items is proven counterproductive (disclosure backfires; pattern-066 referee variance). Verified evidence: `project-context/peer-reviews/EXT_real/` (raw text + screenshots + chat URLs).

## Per-paper readiness

| Paper | Version | Verified verdict (ChatGPT / Grok / Gemini) | Packet | The venue question for the referee |
|---|---|---|---|---|
| **P1A** | v1A.0.104 | REJECT / MAJOR / MAJOR | ✅ src · cover · bundle (36pp) | Is a tiered channel-level ECH assessment (rigorous Tier‑I + honestly-labeled ansatz-tier R2/R3/R4 bounds + companion deps) a sufficient PRD contribution? |
| **P1B** | v1B.0.99 | REJECT / MAJOR / REJECT | ✅ src · cover · bundle (22pp) | Is an error-clean reproducibility/consistency-check **companion** a standalone PRD article, or supplementary to P1A? (Content reviewer-confirmed error-clean.) |
| **P2** | v1.7.88 | REJECT / MAJOR / MAJOR | ✅ src · cover · bundle (31pp) | Is a clearly-labeled conditional single-source recast — with the **genuinely-unresolved Cai/Li factor-of-2** disclosed — publishable now as explicitly conditional? |
| **P3** | v3.1.136 | REJECT / MAJOR / REJECT | ✅ src · cover · bundle (34pp) | Is a disclosed, sequestered exploratory-tier non-reproducibility (eROSITA) acceptable in a catalog paper whose product is the reproducible 268,519 process-volume subset? |
| **P4** | v1.0.212 | REJECT / MAJOR / MINOR | ✅ src · cover · bundle | Is the ~47% unexplained ℓ=1 residual an acceptable disclosed limitation, given the null rests on independent estimators + the GZ1 human-label z=−0.04 independence check? |
| **P5** | v0.1.101 | REJECT / MINOR / MAJOR | ✅ src · cover · bundle | Should publication be contingent on the in-prep Paper IV, or does the monopole-invariant self-contained void null stand alone? |

Cover letters: `submissions/<P>/REFEREE_COVER_LETTER.md`. Bundles: `submissions/<P>/arxiv_*.tar.gz` (each standalone-compile-verified). Readiness caps 76–80 (honest, not 96).

## What the loop fixed (all source-cited, reviewer-confirmed, zero fabrication)

- **P2 — fabrication caught + retracted.** A false "Li used a single time-ordering" mechanism (unsupported by Li's paper, self-contradictory) was removed; a full four-vertex in-in re-derivation confirmed the factor-of-2 is a **genuine unresolved literature discrepancy** (not settleable from published work). f_NL now headlined as the honest range [−35/16, −35/8].
- **P1B — real dimensional bug fixed** (four-fermion coefficient κ→κ²); **§III.A thermal-average step added** (real Kapusta–Gale citation). Both reviewer-confirmed lifted; ΔN_eff unchanged.
- **P1A — T² variational concern** was a reviewer misread; principle verified sound, clarified.
- **P3 — §V cosmological** reframed to methodological-demonstration/no-detection; 268,519 = process-volume candidates (not detections).
- **P4 — null verified-robust** against an adversarial data audit (git-pre-specified cut, step-function systematic, GZ1 z=−0.04).

## The two-category model (proven 3× on verified evidence)

1. **Correctable errors** → our fixes lift them (reviewer-confirmed: P1B dim-bug, P1B thermal-average, P1A T²).
2. **Scope/venue/structural** → referee variance + disclosure backfire; **NOT editable** → human referees.

## Houston-gated forward path (the only remaining work)

1. **Venue decisions** — P1B (companion vs standalone), P2 (conditional-forecast venue), P1A (ansatz-tier venue).
2. **Human-referee routing** — use the drop-ready packets (cover letter + bundle) above.
3. **Publish companion papers** — P5's Paper IV, P1A's 4 companions — clears the largest structural-rejection class.
4. **Optional real research** — P4 ~47% residual (needs pod + DR8 sweeps: is it an unmodeled systematic or physical?).
5. **Cron** — recommend **pausing** the 30-min review loop; it has done its job and further sweeps backfire.

*No surface (git / Convex / site / SSOT) claims any ACCEPT that did not happen. Every verdict here is read from raw reviewer text in git.*
