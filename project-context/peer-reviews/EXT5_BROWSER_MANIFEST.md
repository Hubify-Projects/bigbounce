# EXT5 — in-thread delta round 5 · manifest

**Round**: EXT5 (2026-06-11 23:35 – 2026-06-12 00:10 PT, same 18 threads; versions v1A.0.63 / v1B.0.60 / v1.7.55 / v3.1.98 / v1.0.177 / v0.1.67)
**Round headline**: first external read of the R34conf wave — the internal tier's 42 closures, including the P5 abstract regression fix, the P4 Fisher rebuttal-by-rederivation, the P1A NJL unit-chain removal, and the two computed additions (P1B ESS, P5 contingency tables).
**Delta-prompt**: references/delta-prompt-template.md with two calibration additions (superscript flattening example + version-decimal collision example "z=−18.1.34").

## Submissions (all 18 verified: chip/version-presence + model/effort + generation + growth gate)

| Paper | Version (md5) | ChatGPT Pro Extended | Grok Heavy | Gemini Thinking |
|---|---|---|---|---|
| P1A | v1A.0.63 (ec5815a6) | ✅ | ✅ Heavy | ✅ ver+gen+growth |
| P1B | v1B.0.60 (bb15ceae) | ✅ | ✅ Heavy | ✅ ver+gen+growth |
| P2 | v1.7.55 (ec1f7b83) | ✅ | ✅ Heavy | ✅ ver+gen+growth |
| P3 | v3.1.98 (a04a2d65) | ✅ | ✅ Heavy | ✅ ver+gen+growth |
| P4 | v1.0.177 (d0eca770) | ✅ | ✅ Heavy | ✅ ver+gen+growth |
| P5 | v0.1.67 (01afe6ed) | ✅ | ✅ Heavy | ✅ ver+gen+growth |

Chat URLs identical to EXT1–EXT4 manifests (same 18 threads). PDFs downloaded from the live site and md5-verified byte-exact against local mirrors. Pre-send screenshots `/tmp/ext5_*_pre.png`.

## Operational notes

- Zero Gemini retries this round — the EXT4-hardened recipe (frontmost-guard + Escape-first + version-presence as the authoritative gate) ran 6/6 clean overnight.
- One cosmetic learning: the chip text-check can race the chip render; the version-in-user-turn check is authoritative (encoded).

## Harvest

Open from ~00:45 PT 2026-06-12 (Pro Extended/Heavy are slow). Reports → `EXT5_<paper>_<Provider>.md` → truth-audit → gap metric vs EXT4 (13).
