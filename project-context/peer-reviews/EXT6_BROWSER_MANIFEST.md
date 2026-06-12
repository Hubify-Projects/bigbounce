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

## Harvest

Open from ~03:35 PT. Reports → `EXT6_<paper>_<Provider>.md` → truth-audit → gap metric vs EXT5 (19, ~5 self-inflicted).
