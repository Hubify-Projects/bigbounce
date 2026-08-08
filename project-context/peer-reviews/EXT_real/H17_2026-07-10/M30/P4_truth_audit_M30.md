# P4 truth-audit — M30-EXT (2026-07-13, vs byte-unchanged v1.0.239)

Raws (verified — raw text READ + screenshot inspected before any verdict recorded):
- `P4_grok_M30.md` + `.png` — Grok, project "BigBounce - Papers", "Thought for 24s", **VERDICT: MAJOR REVISIONS**, 2 MAJOR / 3 MINOR. Screenshot matches raw (ℓ=1 residual + pseudo-labels lead items). VERIFIED.
- `P4_chatgpt_M30.md` + `.png` — ChatGPT "Big Bounce Book" (recovered orphan; send landed server-side, review completed), **VERDICT: MAJOR REVISIONS**, 12 MAJOR / 2 MINOR. Screenshot shows item-13 [MINOR] + concl. "1.7% galaxy-chirality dipole" tail matching raw. VERIFIED. (SOFTER than the M26 REJECT — the documented ChatGPT REJECT↔MAJOR band.)

## Grok — per-finding disposition (0 genuinely-new)
| # | sev | finding | verdict | D-id |
|---|-----|---------|---------|------|
| 1 | MAJOR | Sec IV D/App D: ℓ=1 +3.64σ only ~53% reproduced, ~47% unmodeled | RE-FLAG (OPEN-COMPUTE) | DP4-17 |
| 2 | MAJOR | 66.5% pseudo-labels; GZ1-human-only null ~4.5× coarser | RE-FLAG-DISCLOSED | DP4-08 / DP4-15 |
| 3 | MINOR | p_eq>0.6 blinding/post-unblinding status | RE-FLAG-DISCLOSED | DP4-07 |
| 4 | MINOR | block-bootstrap z≈−7.6 model-dependent; matched-Ganalyzer caveat → abstract | RE-FLAG-DISCLOSED | DP4-01 / DP4-11 |
| 5 | MINOR | density/artifact-paths — key anchors self-contained in main text | RE-FLAG (presentation) | DP4-13 |

Grok closing sentence: "The central claim … is supported by the primary estimator, injection-recovery calibration, and multiple robustness tests." (central-null-supported)

## ChatGPT — per-finding disposition (0 genuinely-new; 14 findings 1:1 with M26 set)
p_eq>0.6 post-selection → DP4-07 (×2); injection-not-end-to-end / A50-A95 output-floors → DP4-09 (×2); image-level end-to-end ≠ population injection / spatial confusion → DP4-15; pixel-permutation exchangeability → DP4-16; σ vs moment-z non-Gaussian (z=7.31 vs p=6e-4) → DP4-10; block-bootstrap z≈−7.6 not calibrated → DP4-01/-14; 47% residual coherent non-null structure → DP4-17; GZ1-only under-powered A50≈3.4% → DP4-09; 21.4% D4 flips / rotational stability → DP4-08; +3.64 vs +7.93 harmonic inconsistency → DP4-10; recovery-thresholds-as-bounds → DP4-09/-17; MINOR birefringence/Chern-Simons → DP4-12; MINOR DOI placeholder + regenerate catalog from single pass → DP4-21.

ledger_match: Grok 3/6 auto (header row #1 = parser noise), ChatGPT 9/16 auto; all UNMATCHED Opus-adjudicated to the D-ids above.

## Pattern-066 verdict on the Grok slip
Grok read this **byte-identical** v1.0.239 as **M21-ACCEPT → M24/M26-MINOR → M30-MAJOR**. The two M30 MAJORs (47% harmonic residual = DP4-17; pseudo-labels/GZ1 = DP4-08/-15) are the exact disclosed-content set Grok accepted at M21 and flagged MINOR at M24/M26 — a maximally-harsh referee oscillating ACCEPT↔MINOR↔MAJOR on unchanged, honestly-disclosed content. Textbook pattern-066 referee variance, NOT a genuinely-new finding.

## Result
0 genuinely-new editable findings on either leg. clean-wave streak **10→11**. cap: Grok MAJOR 6 + ChatGPT MAJOR 6 + latest Gemini MINOR 12 = 50+24 = **74** (ChatGPT +6 vs its M26 REJECT-0; honest up-move). No bump (byte-unchanged v1.0.239); directive_g.sh NOT run. No faked accept, no un-sourced dismissal, no fabrication.

## P1U M30 note (grok-only-pending-chatgpt)
`P1U_grok_M30.md` = 360-byte prompt-echo only (NO reviewer response); `P1U_grok_M30.png` shows a still-GENERATING ChatGPT session (mislabeled screenshot, no verdict). Manifest verdict:"MAJOR REVISIONS" is UNSUPPORTED by the raw → recorded as Grok:EXT:**failed** per directive I4 (no-output leg = FAILED, never a verdict). ChatGPT M30 P1U leg still generating at recovery (manifest status:submitted, url …6a54e861) → next ext_harvest. No valid P1U M30 verdict this wave; P1U streak HOLDS **12** (M28-INT), cap HOLDS.
