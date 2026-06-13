# EXT6 — in-thread delta round 6 · manifest

**Round**: EXT6 (2026-06-12 ~02:35–03:03 PT; versions v1A.0.65 / v1B.0.62 / v1.7.57 / v3.1.100 / v1.0.179 / v0.1.69)
**Round headline**: first external read of the R35conf wave — the chains-recomputed ΔNeff < 0.40, the root-caused P5 duplicate rate (3.56%), the P1A sign rederivation, the Chaussidon fix, and the honest removal of the unsupported 0.27° prediction.
**Thread policy change**: Gemini P3 moved to a **FRESH thread** (full referee prompt, not delta) after its old thread read stale v3.1.91 content for three consecutive rounds.

## Submissions (all 18 verified: chip/version-presence + model/effort + generation + growth gate)

| Paper | Version (md5) | ChatGPT Pro Extended | Grok Heavy | Gemini Thinking |
|---|---|---|---|---|
| P1A | v1A.0.65 (418777c6) | ✅ | ✅ Heavy | ✅ (same thread) |
| P1B | v1B.0.62 (e0066b42) | ✅ | ✅ Heavy | ✅ (same thread) |
| P2 | v1.7.57 (cb95f253) | ✅ | ✅ Heavy | ✅ (same thread) |
| P3 | **v3.1.100** (39c00ff6) | ✅ | ✅ Heavy | ✅ **FRESH thread** [chat](https://gemini.google.com/app/2b33106610ec2401) — first response held-to-completion per the persistence rule; full MNRAS-format report rendered |
| P4 | v1.0.179 (3ba688c1) | ✅ | ✅ Heavy | ✅ (same thread) |
| P5 | v0.1.69 (8a6e800f) | ✅ | ✅ Heavy | ✅ (same thread) |

All other chat URLs identical to EXT1–EXT5 manifests. PDFs md5-verified byte-exact against local mirrors. Pre-send screenshots `/tmp/ext6_*_pre.png`.

## Operational notes

- Second consecutive zero-retry Gemini run under the hardened recipe.
- Fresh-thread protocol exercised for the first time since EXT1: model defaults must be verified at harvest (header shows the serving model); the version-in-turn + held-to-completion gates passed.

## Harvest — COMPLETE (2026-06-12 20:00 PT)

All 18 reports harvested. Zero URL mismatches, zero still-generating chats, zero retries required. Files: `EXT6_<paper>_<Provider>.md`.

## Verdicts (EXT5 → EXT6)

| Paper | ChatGPT Pro Ext | Grok Heavy | Gemini Thinking |
|---|---|---|---|
| P1A | MAJOR → **MAJOR** (NJL wrong-sign still in closure summary; Sec IV/Fig 4 overstate closure) | ACCEPT → **ACCEPT** (minors on equation label clarity) | MINOR → **ACCEPT WITH MINOR REVISIONS** (fine-tuning score phrasing) |
| P1B | MAJOR → **MAJOR** (artifact-layer pinning; frozen artifact vs text mismatch) | ACCEPT → **ACCEPT** (no revisions required — model companion paper) | MINOR → **ACCEPT** (fully cleared, moved decisively past remaining roadblocks) |
| P2 | MAJOR → **MAJOR** (narrowly; null-space interpretation + fresh numerical issues) | ACCEPT → **ACCEPT** (every prior concern closed; journal-ready, zero issues) | ACCEPT → **MINOR REVISIONS** (Eq 3 variable mismatch + Table IV header) |
| P3 | MAJOR → **MAJOR** (catalogue-tier semantics, DESI denominator, frozen data release) | ACCEPT → **ACCEPT** (landmark catalog; one trivial minor fixable in proof) | MAJOR → **MAJOR** (fresh thread; calibration/instrumental artifacts, notation) |
| P4 | MAJOR → **MAJOR** (monopole interpretation, +3.64σ taxonomy residuals) | ACCEPT → **ACCEPT** (exemplary catalog paper; immediate acceptance recommended) | ACCEPT → **MINOR REVISIONS** (misplaced imaging-leg paragraph block in appendix) |
| P5 | MAJOR → **MAJOR** (GALZONE estimand-family, 3.56% duplicate tracking) | MINOR → **ACCEPT** (estimand-family coherence + Appendix B tables cleared) | MINOR → **MINOR REVISIONS** (appendix labeling layout sync needed) |

**Grok: FOURTH consecutive clean external round, 6/6 ACCEPT.** Gemini posts 2 ACCEPT + 2 MINOR REVISIONS + 2 MAJOR (P3 fresh thread resets to MAJOR). ChatGPT holds MAJOR ×6 with P2 "narrowly". Gemini P3 fresh thread served by Gemini Thinking (2.5 Pro, confirmed via "Thinking" UI dropdown).

**Bytes per report** — range: 1,953 bytes (Grok P2, terse ACCEPT) to 14,489 bytes (ChatGPT P1B, detailed); Grok 1.9–3.7 KB, Gemini 3.7–6.8 KB, ChatGPT 9.1–14.5 KB.
