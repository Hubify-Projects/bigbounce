# P2 M20-EXT truth-audit (2026-07-13, vs byte-unchanged v1.7.116) — STRICT ledger-first

Raws read verbatim BEFORE any disposition:
- `EXT_real/H17_2026-07-10/M20/P2_grok_M20.md` = **MAJOR REVISIONS** (l.1 `VERDICT: MAJOR REVISIONS`; 2 MAJOR + 3 MINOR)
- `EXT_real/H17_2026-07-10/M20/P2_chatgpt_M20.md` = **REJECT** (l.1 `(1) VERDICT: REJECT`; 10 MAJOR + 2 MINOR)

Byte-unchanged **v1.7.116** — identical file audited at M4/M7/M10/M13/M15/M18/M19. `ledger_match.py`
pre-match (Grok 5/6 auto-MATCHED, ChatGPT 10/12 auto-MATCHED) + full §3 Opus truth-audit vs
`research/focused_paper_source_integration/02_full_draft.tex` + `DISPOSITIONS/P2.md`.

## Grok MINOR→MAJOR SLIP (pattern-066) — verify vs M18/M19

Prior P2 EXT read (M18-EXT, SAME byte-unchanged v1.7.116) = Grok **MINOR** (closing "supported").
M20 = Grok **MAJOR** on the IDENTICAL file → referee run-to-run variance, NOT a content
regression. This is the documented DP2 Grok oscillation (MINOR@M4→MAJOR@M7→MINOR@M10/M13/M15/M18
→MAJOR@M20; INT-Grok MAJOR@M19). Both Grok M20 MAJORs quote the paper's OWN honestly-disclosed
limitations (verified below), consistent with DP2-24 harsh-referee floor.

## EXT-Grok MAJOR (2 MAJOR + 3 MINOR) — D-id mappings

- **[MAJOR] G1** App-A −35/16 correction: collapsed polynomials / discrepant −(99/128) term /
  four-way cross-check "not reproduced in sufficient algebraic detail … without the author's
  private code; expand with the key collapsed polynomials side-by-side" → **DP2-01/-02/-16/-25**.
  −35/16 quadruple-certified (per-vertex sum, ε-grouped `eq:order_grouped` L1535, Li Eq.(5.1)@c_s=1,
  collapsed degree-9 `eq:collapsed_vertexsum` L1527, `tab:vertexwalk` L1505, `tab:benchmarks` L986).
  In-in operator algebra A7–A12 present since v1.7.104. "Expand/elevate App A / show side-by-side"
  = placement OPINION = **DP2-30**. Cai's separately-published −35/8 = unreproduced literature value
  = **DP2-25 OPEN-COMPUTE** (Houston-gated). **0 genuinely-new.**
- **[MAJOR] G2** headline 1.3σ floor / 0.8σ GR-bracket edge rests on transferred proxy
  ρ≈−0.868 (Cov_B not public); in-house surrogate gives ~2.3σ; "mixes proxy and surrogate
  without a single fully-native marginalized Fisher, lower edge heuristic" → **DP2-04/-07/-26/-34/-35**.
  Channel-native Fisher on the adopted Cov_B surrogate WAS computed (v1.7.114/-115, `c15`):
  ρ(f_NL,A_GR)=−0.42/−0.49 (moderate), σ_marg=0.9417→**2.32σ** > proxy 1.30σ; proxy −0.868 retained
  as a conservative cross-check strictly BELOW the computed floor (no headline loosened). Grok's
  ask ("compute channel-native once a surrogate is adopted") is exactly what DP2-34/-35 did. The
  proxy/surrogate disclosure is present in abstract L892 + §systematics. **0 genuinely-new.**
- **[MINOR] G3** 37pp length / condense null-space SVD, monomial-basis sampling, c9i ε-ratio to
  supplemental → **DP2-30** (presentation-scope, Houston-gated; DP2-M1 restructure actioned the class).
- **[MINOR] G4** assumption (d) cubic transmission δf_NL≲10⁻³ a scaling argument not a direct
  in-in integration; flag as largest remaining model-dependence → **DP2-13/-32.6** (disclosed
  load-bearing caveat ★; "verified only at linear order"; softened v1.7.112). **0 genuinely-new.**
- **[MINOR] G5** BF≈9–14 illustrative + prior-sensitive; state BF not robust evidence → **DP2-18**
  (already "illustrative … not definitive model-selection evidence"; four-corner grid `tab:bayes` L1236).

Grok's closing CREDITS the central claim verbatim ("The central claim … is supported by the
explicit overlap calculation (r=0.84±0.02), the independent in-house Fisher validation
(r_eff≈0.99), and the recast of the Heinrich et al. baseline"). **0 genuinely-new.**

## EXT-ChatGPT REJECT (10 MAJOR + 2 MINOR) — D-id mappings

- **[MAJOR] #1** App-A four-way certification "does not resolve at the standard required for a
  published correction … self-contained in-in derivation from the cubic action required" →
  **DP2-01/-02/-03/-16** (−35/16 quadruple-certified; A7–A12 convention-fixed; framing reframed
  v1.7.108 "unreproduced erroneous literature value"). ChatGPT CONCEDES "−35/16 may be a
  plausible canonical-limit result." **DP2-25** OPEN-COMPUTE for Cai's −35/8 trace.
- **[MAJOR] #2** polynomial reconstruction: Eq.(A4) uniquely determines the polynomial → "no
  physical 3-D null space"; adopted (2,7,3,−12,−69,19) gives uncorrected values; correction is an
  additive −165/64 shift not a factor-of-two rescale; "null-space scan, Fig 1, r/r_cos, template
  projections must be discarded" → **DP2-01/-03/-15/-16**. Source-verified: this is precisely the
  underdetermination-scope the paper documents (L1028 "Important scope of the underdetermination
  claim"; orbit-dependent Wick-permutation absorption, `c9i_epsilon_ratio_check.json`;
  amplitude-invariant shape band NEVER enters σ_eff L987); reparametrization caveat verbatim L966.
  Methodological-interpretation disagreement, not a numeric error. **0 genuinely-new.**
- **[MAJOR] #3** IIC–D "viable model" combines incompatible ingredients (−35/16 = c_s=1 vs
  low-c_s escape → f_NL^local=−165/16+65/8c_s²; Wilson-Ewing canonical vs low-c_s DM) → **DP2-19/-02**
  (assumption (a) fixes c_s=1 quasi-dust benchmark §954; low-c_s is a separate qualitative note).
- **[MAJOR] #4** cubic-order transmission δf_NL≲10⁻³ "not derived" (holonomy gradient 1−2ρ/ρ_c<0;
  mode mixing; ζ̇=0 not implied) → **DP2-13/-32.6** (disclosed load-bearing caveat ★; deformed-algebra
  signature-change window flagged v1.7.112 as where the gradient expansion is least controlled).
- **[MAJOR] #5** quasi-dust κ_ε≃2.8–40 / "0.6–8%" "not calculations"; 14× enhancement unexplained →
  **DP2-20** (κ_ε labeled single-prefactor-derivative estimate, four-vertex cancellations acknowledged).
- **[MAJOR] #6** template-mismatch map / SPHEREx significance: α=F_local,bounce/F_local,local not the
  r=0.84 "ad hoc geometry"; surrogate gives r_eff≈0.99; 2.6–2.75σ "not a defensible recast" →
  **DP2-14/-17/-34** (reconciled §spherex L888/L892: r=0.84 = conservative flat-weight cosine headline,
  r_eff≈0.99 = validation cross-check, channel-native α=0.992).
- **[MAJOR] #7** Heinrich baseline nuisance treatment misstated (b_01=2f_NLδ_c(b_10−1) exact;
  0.7→0.9→1.0 not derived from the cited forecast) → **DP2-22** (reproduction-vs-Heinrich limitation
  list disclosed §spherex L1045-area; labeled validation not independent forecast).
- **[MAJOR] #8** Table V systematic-error envelope: σ_marg=σ_cond/√(1−ρ²) applies only same-Fisher;
  ρ=−0.868 transferred from SDB power-spectrum; surrogate gives ρ≈−0.42, 2.3σ → **DP2-04/-07/-26/-34/-35**
  (channel-native ρ≈−0.42 floor 2.32σ COMPUTED; proxy retained as conservative cross-check below).
- **[MAJOR] #9** Bayes factors "principally prior-volume ratios"; tuned competitor only a uniform
  interval; B≃W/(√2πσ) → **DP2-18** ("illustrative"-labeled; four-corner prior grid).
- **[MAJOR] #10** "gauge-frame survey observable" f_NL≃0.015 "incorrect"; ratio 2.1875/0.015≃146
  disputed → **DP2-21** (comoving-gauge consistency-term interpretation dispute; 146× disclosed as a
  gauge-frame template-amplitude comparison, physical-frame confined to its proper role).
- **[MINOR] #11 [ledger_match UNMATCHED, score 0.09]** Data/Code Availability: mutable repo, internal
  JSON/script paths, promised Zenodo DOI does not yet exist → **DP2-11/-27/-30 PROCESS-NIT**.
  Source-verified: c9k/c9g artifacts already −35/16 (DP2-11); DAS real GitHub pointer + Zenodo
  pending-at-camera-ready disclosed (DP2-31.5); per-vertex print loop / immutable release = DP2-27
  hygiene. Repo-hygiene outside the manuscript text — closes WITHOUT reset.
- **[MINOR] #12 [ledger_match UNMATCHED, score 0.17]** "excessively long, internal-review language,
  unsupported tangential material (anomaly-selected tracers, birefringence, future facilities, AI
  workflow); reorganize around one derivation + one forecast" → **DP2-30/-02 OPINION**. Source-verified:
  birefringence relegated to Appendix `app:birefringence` per DP2-M1.2; the exact structural items are
  those the v1.7.116 DP2-M1 restructure actioned; residual length = venue/scope floor, Houston-gated.

ChatGPT's own close: "The contraction-era algebraic indication that −35/16 may replace the published
−35/8 is plausible" — central certification withstands direct challenge; REJECT rests on
survival-through-bounce (DP2-13, disclosed) + forecast/venue scope (DP2-17/-29, disclosed).
Structural harsh-referee floor (directive-H). **0 genuinely-new.**

## Verdict

**0 genuinely-new reader-visible editable findings** across both legs (all re-flags +
CLOSED-BY-COMPUTE re-flags + OPEN-COMPUTE/VENUE + PROCESS-NIT + presentation OPINION). Prior
M19-INT rebuilt streak to 8. **M20-EXT = 0 genuinely-new on byte-unchanged v1.7.116 →
clean-wave streak 8→9** (directive-K). No content bump; **v1.7.116 stands; `directive_g.sh` NOT run.**

## Cap 74→68

M20 EXT Grok slipped MINOR→MAJOR. EXT formula latest-per-reviewer = 50 + Grok-EXT MAJOR (6) +
ChatGPT-EXT REJECT (0) + Gemini-latest MINOR (12, the M19-INT fresh Gemini row) = **68**. Grok's
EXT contribution drops 12→6 → cap **74→68**, recomputed honestly by `post_verdict.sh`
(`_creationTime`-latest, root-fixed cd02c991). A pattern-066 verdict-word slip on byte-unchanged
content moves the honest formula cap but does not reset the clean-wave streak (0 genuinely-new).

## Integrity

Both raws read verbatim before any disposition (Grok l.1 `VERDICT: MAJOR REVISIONS`, ChatGPT l.1
`(1) VERDICT: REJECT`). No ACCEPT faked. Every finding source-cited to an existing DP2 D-id + tex
line; every ledger_match-UNMATCHED finding (#11/#12) source-verified against the live
`02_full_draft.tex`. Grok MINOR→MAJOR slip diagnosed pattern-066 (each MAJOR quotes the paper's own
disclosure). No un-sourced dismissal; no math fabricated; no version bumped. Both reviewers'
−35/16 credit/concession quotes recorded verbatim above.
