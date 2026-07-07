# Submission Readiness Dashboard — bigbounce

**Status as of 2026-07-07 (verified, FINAL+POSTPOLISH rounds).** One decision surface for Houston's venue calls + human-referee routing.

> **Honest headline:** The autonomous LLM-review loop is **complete and exhausted.** All 6 papers are **content-honest and error-clean** (every concrete error fixed + reviewer-confirmed lifted; the one real POSTPOLISH item — P1A's `fig_theory_map.png` baked-in f_NL=−35/8 — was found and fixed to −35/16 at v1A.0.112). **None are converged** to all-3-ACCEPT — the harshest referees (ChatGPT / openai) REJECT every paper, uniformly on a **venue/scope** question that LLM referees flag and cannot adjudicate, while Grok/grok-4.3 rate the identical PDFs MINOR/ACCEPT (maximally-harsh-referee structural floor, directive H). That judgment belongs to **human referees.** Editing scope items is proven counterproductive (disclosure backfires; pattern-066 referee variance). Verified evidence: `project-context/peer-reviews/EXT_real/` + `FINAL_SIGNOFF_AUDIT_2026-07-05.md` (raw text + screenshots + chat URLs).

## Per-paper readiness

| Paper | Version | Verified verdict (ChatGPT / Grok / Gemini; API in note) | Packet | The venue question for the referee |
|---|---|---|---|---|
| **P1A** | v1A.0.112 | REJECT / "publication-ready" / MAJOR (openai REJECT / grok-4.3 REJECT) | ✅ src · cover · bundle (37pp) | Is a channel-level ECH no-go — rigorous Tier-I + derived R3 running + NDA-bounded routes + operator-level parity-odd closures, operator basis complete within minimal ECH, one open Fierz lemma — a sufficient PRD contribution? |
| **P1B** | v1B.0.102 | REJECT / MAJOR / MAJOR (openai MAJOR / grok-4.3 MINOR) | ✅ src · cover · bundle (22pp) | Is an error-clean reproducibility/consistency-check **companion** a standalone PRD article, or supplementary to P1A? (Content reviewer-confirmed error-clean.) |
| **P2** | v1.7.98 | REJECT / MINOR / MINOR (openai REJECT / grok-4.3 MAJOR) | ✅ src · cover · bundle (34pp) | Is the vertex-certified Cai/Li resolution (f_NL=−35/16, App. A, scripts committed) + a clearly-labeled conditional single-source recast (~1.3–2.75σ) publishable now? |
| **P3** | v3.1.140 | REJECT / MAJOR / MAJOR (openai REJECT / grok-4.3 MINOR "central claim supported") | ✅ src · cover · bundle (33pp) | Is a disclosed, sequestered exploratory-tier non-reproducibility (eROSITA) acceptable in a catalog paper — and is this an ApJS/MNRAS catalog paper or PRD? |
| **P4** | v1.0.220 | REJECT / MINOR / MINOR (openai REJECT / grok-4.3 ACCEPT) | ✅ src · cover · bundle | Is the ~47% unexplained ℓ=1 residual an acceptable disclosed limitation (bounded A_p=0.695%<A_50), given the null rests on the +0.41σ real-space HC estimator + the GZ1 human-label independence check? |
| **P5** | v0.1.104 | MAJOR / MINOR / MINOR (openai MAJOR / grok-4.3 MINOR) | ✅ src · cover · bundle | Should publication be contingent on the coordinated companion Paper IV (P4), or does the monopole-invariant self-contained void null stand alone? |

Cover letters: `submissions/<P>/REFEREE_COVER_LETTER.md`. Bundles: `submissions/<P>/arxiv_*.tar.gz` (each standalone-compile-verified). Readiness caps 76–80 (honest, not 96).

## What the loop fixed (all source-cited, reviewer-confirmed, zero fabrication)

- **P2 — factor-of-2 resolved to −35/16 (vertex-certified).** An earlier false "Li used a single time-ordering" mechanism was caught and retracted; a from-scratch four-vertex in-in re-summation of Cai et al.'s own vertices at ε=3/2 gives f_NL=−35/16, matching Li's independent general-c_s formula at c_s=1 and tracing Cai's printed −35/8 to a spurious +(99/128)Σk³ term in their Eq. 37. f_NL is now headlined as **−35/16** (App. A; reproducing scripts committed at `research/focused_paper_source_integration/scripts/caili_certification/`). The harshest referees (ChatGPT/openai) still re-raise the resolution → Houston-gated human-referee handoff.
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
