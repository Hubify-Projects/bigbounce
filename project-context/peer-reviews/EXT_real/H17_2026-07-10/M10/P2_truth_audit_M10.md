# P2 M10-EXT truth-audit (v1.7.116) — verdict-first, source-cited, ledger-first

Raws (read verbatim): `P2_grok_M10.md` (VERDICT: MINOR REVISIONS, md5 3e840dd7cfa6126b3514b085ae768596)
· `P2_chatgpt_M10.md` (VERDICT: REJECT, md5 ae0a1e9bb73263124383848a64118cf1).
Ledger: `DISPOSITIONS/P2.md` (29 D-ids). ledger_match DRAFT: Grok 4/5 MATCHED, ChatGPT 12/13 MATCHED
(conservative dilution false-negatives resolved below).

Note: P2 bumped to v1.7.116 (directive-M presentation restructure, ZERO content change) since the
last P2 EXT (M7, v1.7.112). Raws are on v1.7.116.

## Grok M10 — MINOR REVISIONS (4 MINOR)

| # | sev | verdict | source-cited justification |
|---|-----|---------|-----------------------------|
| G1 | MINOR | RE-FLAG DP2-01/-03 | Side-by-side Cai printed-vs-vertex tabulation requested; `tab:vertices`+`tab:vertexwalk` already give the four-vertex algebra + column sums; −(99/128)Σkᵢ³ stated L1025 + App-A `eq:spurious`. Placement = DP2-30 opinion. |
| G2 | MINOR | RE-FLAG DP2-04/-14/-34 | "Give channel-native Fisher (σ≈0.94, 2.3σ) equal/primary weight." Native floor computed+disclosed (DP2-34/-35, ρ≈−0.42, σ_marg=0.94→2.32σ); proxy retained strictly below computed floor (abstract L975). |
| G3 | MINOR | RE-FLAG DP2-14/-31.4 | r-notation density; canonical "Notation for the overlap factor" clause already unifies r/r_cos/r_eff/ρ (DP2-31.4, v1.7.111+). |
| G4 | MINOR | RE-FLAG DP2-30 | MegaMapper "one explicit envelope sentence"; disclosed verbatim L1120/L1186 ("illustrative … uncalibrated projection … not calibrated forecasts"). |

## ChatGPT M10 — REJECT (11 MAJOR + 2 MINOR)

| # | sev | verdict | source-cited justification |
|---|-----|---------|-----------------------------|
| C1 | MAJOR | RE-FLAG DP2-02/-16 | App-A "internally contradictory (−35/8/−305/64/−35/16)"; all three are distinct labeled quantities reconciled L1025 + App-A; −35/16 quadruple-certified. |
| C2 | MAJOR | RE-FLAG DP2-01/-03 | "Discrepancy additive not multiplicative → invalidates Table-I halving." Premise false: L1025 states the term "is not itself a naive additive shift … does not by itself produce −35/8"; overlap uses printed shape only via amplitude-invariant shape ratios — no per-triangle-halving claim exists. |
| C3 | MAJOR | RE-FLAG DP2-15 | Null-space "no physical 3D null space"; disclosed amplitude-invariant stress band, reparametrization caveat L966, never enters σ_eff. |
| C4 | MAJOR | RE-FLAG DP2-13 | δfNL≲10⁻³ "not established"; load-bearing caveat (d), disclosed conditional on dressed-metric quantization (DP2-32.6). |
| C5 | MAJOR | RE-FLAG DP2-19 | c_s=1 vs c_s≪1; assumption (a) fixes c_s=1 quasi-dust benchmark, low-c_s a separate qualitative note. |
| C6 | MAJOR | RE-FLAG DP2-14 | r=0.84 "ad hoc"; reconciled: 0.84=flat-weight conservative headline, r_eff≈0.99=survey-optimal validation. |
| C7 | MAJOR | RE-FLAG DP2-22 | Independent Fisher "not validation-grade"; limitation list disclosed (bias-fixed, diagonal Gaussian, no FoG); labeled validation not forecast. |
| C8 | MAJOR | RE-FLAG DP2-07/-26/-34 | ρ=−0.868 transfer "category error"; channel-native ρ≈−0.42 now computed (DP2-34/-35); proxy = disclosed conservative cross-check. |
| C9 | MAJOR | RE-FLAG DP2-18 | Bayes = prior-volume ratio; labeled "illustrative … not definitive"; four-corner prior grid `tab:bayes`. |
| C10 | MAJOR | RE-FLAG DP2-20 | κ_ε not calculated; labeled single-prefactor-derivative estimate; fNL–n_s relation "indicative." |
| C11 | MAJOR | RE-FLAG DP2-04 | 1.3–2.75σ "not a confidence interval"; disclosed scoping envelope, endpoints "not directly comparable." |
| C12 | MINOR | RE-FLAG DP2-21 | Gauge-frame/factor-146 framing; disclosed as gauge-frame template-amplitude comparison. |
| C13 | MINOR | PROCESS-NIT (DP2-30/-27/-29) | "Archived code release / stable DOI required" + repetition; code-release/DOI = repo-process, not paper-content defect → does NOT reset streak. |

## COUNTS
- genuinely-new reader-visible = **0**
- re-flags = **16** (Grok 4 + ChatGPT 12)
- process-nits = **1** (ChatGPT C13)

## New D-ids: **None.** Every finding maps to an existing D-id with a source-cited disposition.

## VERDICT: CLEAN — 0 genuinely-new reader-visible.
Grok M4 MINOR → M7 MAJOR → M10 MINOR = textbook pattern-066 run-to-run variance on identical content.
ChatGPT held its structural REJECT floor. No v1.7.117 bump; directive_g.sh not warranted (no reader-visible edit).
Both raws read verbatim; no faked accept, no un-sourced dismissal, no fabrication.
P2 clean-wave streak 3→4; cap 74 HOLDS.
