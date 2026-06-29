# RA-INT P5 — Round A INT Truth Audit (neutral, verdict-first)

- **Date:** 2026-06-29
- **Paper:** P5 DESIVAST/T-Web chirality (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`)
- **Pre-audit version:** v0.1.91-2026-06-28 → **post-close v0.1.92-2026-06-29**
- **Inputs:** RA-INT multi-vendor (Grok grok-4.3, Gemini-2.5-pro, OpenAI gpt-5 methodology; Perplexity quota-failed; Anthropic leg not run) + own Opus end-to-end read.
- **Compile:** 0 undefined refs/citations, 34 pages, 0 overfull hboxes. `\mbox{-}` renders as hyphen (verified "non-void" in PDF text).

## Vendor recommendations (actual lines)
- **Grok_brutal — REJECT.** Drivers: post-hoc primary path (P5-E1), n=428 void under-power (P5-E2), Paper IV in-prep dependence (P5-E3), abstract overstates scope (P5-E4), σ-juxtaposition (M1).
- **Gemini_cosmology — major-revisions.** ESSENTIAL: Paper IV in-prep dependence (E1). MAJOR: dense abstract (M1), "largest test" scoping (M2), effect-size framing (M3). MINOR: σ_from_half notation, V2-REVOLVER abstract citation, tidal-tensor normalization.
- **OpenAI_methodology — major-revisions.** "Internal arithmetic largely checks out." ESSENTIAL: Paper IV monopole dependence. MAJOR: row-level duplicate-TARGETID parent; GALZONE complement underspecified (M6). MINOR: **P5-m7 interior-buffer count mismatch**, **P5-m6 h-units divide-by-h**, P5-m8 RSD flips ambiguity, P5-m9 Clopper-Pearson exponent, P5-m10 σ-rounding note.

## Verdicts
| Item | Verdict | Action |
|---|---|---|
| OAI P5-m7: "1,862 spirals removed" vs "retains 782,015 of 783,820" (→1,805) | **VERIFIED** | CLOSED — 1,862→1,805; artifact `21_r23conf_meta_closures.json` META_M2 n_all=783,820/n_interior=782,015 ⇒ removed=1,805 |
| Own/Opus: abstract dark σ=+1.25 conflated with filament-class dark σ=+1.61 | **VERIFIED** | CLOSED — disambiguated: +1.25 program-wide (n=14,782, all classes, body §VI.D l.1697-98); +1.61 filament-class (n=13,759, l.1729-31) |
| OAI P5-m6: h-unit footnote "alternative convention χ[h⁻¹Mpc]=χ[Mpc]/h" | **VERIFIED** | CLOSED — relabeled "incorrect divide-by-h operation"; contradicts dimensional relation derived two lines above (internal inconsistency) |
| Post-hoc primary DESIVAST path (Grok E1, all) | **OUT-OF-SCOPE/disclosed** | LEAVE — declared post-hoc + robust across 5 void-finders (calibration) |
| n=428 void under-power (Grok E2, M2, M3) | **OUT-OF-SCOPE/disclosed** | LEAVE — MDE ±4.8pp explicitly stated; structural |
| Paper IV in-prep dependence (all 3 ESSENTIAL) | **OUT-OF-SCOPE** | LEAVE — companion paper; DOI deferred; monopole-shift-invariant headline reduces dependence to per-galaxy labels |
| σ-from-half juxtaposition not comparable (Grok M1) | **FALSIFIED** | LEAVE — caveat present at l.552-554 ("not mutually comparable across classes") |
| Date "June 28/29 2026 = future placeholder" (Grok m1, Gem N1) | **FALSIFIED** | LEAVE — June 2026 is current |
| Clopper-Pearson 0.05^{1/6} typeset (OAI m9) | **FALSIFIED** | LEAVE — source correct (l.1839 proper braces); prior-adjudicated PDF-render false positive |
| Dense abstract / notation / "largest" / tidal normalization / σ-rounding | **OPINION** | LEAVE — style/clarity, not error |
| GALZONE complement / row-level parent / RSD flip ambiguity (OAI M6/MAJOR/m8) | **OPINION/structural** | LEAVE — disclosed construction; clarify-requests, no wrong number |

## Closed: 3 VERIFIED, all with real artifact/source-backed fixes. No science change.
