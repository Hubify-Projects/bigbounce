# P5 M22-EXT truth-audit (2026-07-13) — STRICT, ledger-first

**Paper:** P5 (DESI chirality) v0.1.126 — byte-UNCHANGED (served md5 4458e760, 8 paths; no edit this wave).
**Raws read verbatim before any verdict:** `M22/P5_grok_M22.md` (MINOR REVISIONS), `M22/P5_chatgpt_M22.md` (REJECT).
**Pre-triage:** `tools/ledger_match.py` — Grok 5/6 MATCHED (#1 header artifact), ChatGPT 11/13 MATCHED, 2 UNMATCHED. All UNMATCHED Opus-adjudicated below.

## Grok EXT = MINOR REVISIONS (5 minors)
Closing sentence l.11: "The central claim of no detectable environment dependence of spiral chirality … is supported by the data, statistical framework, and robustness checks." All 5 source-cited re-flags:
1. §V.B post-hoc designated-primary / garden-of-forking-paths → **DP5-13** (disclosed exploratory §V B l.1668 + abstract l.729-730).
2. §VIII RSD fixed-void-geometry / Zel'dovich reconstruction bound ≲0.37pp on unrestricted not exact-footprint sample → **DP5-22 / DP5-12** (first-order Zel'dovich bound is the CLOSED-BY-COMPUTE v0.1.122 content; membership-stability under the exact footprint is the disclosed residual, §XIII).
3. Abstract/§I de-attenuated 2.26pp physical-chirality bound / one-sentence self-contained (2a−1) derivation → **DP5-21 / DP5-09** (Paper-IV dependency + symmetric-error approximation disclosed abstract l.749-757).
4. §VI.A T-Web n=428 low statistical power, state retained-for-consistency-only → **DP5-14** (T-Web secondary/diagnostic/not-load-bearing, disclosed).
5. §II/§VIII.F global monopole systematic / no residual env correlation test → **DP5-02** (matched-sample f_CW^P5=0.49719 internal corroboration; monopole enters σ_pred only, disclosed).

**0 genuinely-new reader-visible editable.** #1 "REVISIONS ISSUES:" = parser-header artifact.

## ChatGPT EXT = REJECT (12 MAJOR + 1 MINOR)
**PATTERN-066: THIRD consecutive REJECT on byte-identical v0.1.126** (H17H → M17 → M19 → M22). The M22 item set is 1:1 with the M17/M19 REJECT reads — identical disclosed-content set, 0 genuinely-new. **Modal-floor assessment: ChatGPT's P5 verdict-word floor has shifted from MAJOR-modal (M3b/M6/M9/M12/M14 all MAJOR) to REJECT-modal (H17H, M17, M19, M22 = four of the last five reads REJECT).** This is a stable maximal-harsh-referee floor at REJECT on unchanged content, NOT new findings — the structural harsh-referee floor moved down a tier and is now stable there. Cap contribution already 0 since M17; no further cap effect.

11 MATCHED map to DP5-01/-04/-06/-08/-10/-11/-13/-16/-21/-22 + DP5-11 (dup). 2 UNMATCHED Opus-adjudicated RE-FLAG:
- **UNMATCHED #9 (score 0.27) "§§IV/IX A/XII A T-Web field not a validated independent env measurement; randoms-rebuild changes void fraction 17.6%→0.75%, 26.6% same-class; cannot substantiate ≳25 Mpc/h scale"** → **RE-FLAG of DP5-14** (+ DP5-06). Source-verified: T-Web is explicitly secondary/diagnostic/not-load-bearing (abstract l.718; Conclusions); the ~73% reassignment / ~23× void-fraction change under randoms-weighting IS the paper's OWN disclosure driving the T-Web demotion (DP5-14 body). The 25 Mpc/h scale belongs only to the T-Web construction the paper already relegates. Matcher below threshold only because prose is diluted; semantically identical to the standing DP5-14 re-flag matched every prior wave (M14/M17/M19). Disclosed limitation.
- **UNMATCHED #11 (score 0.25) "§XII B/App B parity-violating bounce/inflation connection not established; ∇φ·∇ρ and L·∇ρ both parity-odd → product parity-even; coupling dimensionally undefined; remove or replace App B"** → **RE-FLAG of DP5-20** (speculative EFT/App-B). Source-verified: App B + Conclusions already label the mapping "speculative … outside the empirical scope … not a derived constraint" (DP5-20 body); the parity-terminology objection is the same class flagged M14 UNMATCHED#10 (parity-even/no-forward-model), dispositioned to DP5-20 there and identically here. Disclosed/relegated, not a new editable defect.

**0 genuinely-new real+editable across ChatGPT** (identical disclosed-content mapping to M17/M19).

## Net + integrity
- **0 genuinely-new reader-visible editable findings across both legs.** clean-wave streak 8→9. No bump; v0.1.126 stands. `directive_g.sh` NOT run (no edit).
- Cap HOLDS 74 (Grok MIN 12 + ChatGPT REJECT 0 + latest-Gemini MIN 12 = 50+24; `post_verdict.sh` recomputed).
- **Integrity:** Grok MINOR + ChatGPT REJECT recorded as-is; no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.
