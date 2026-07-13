# P4 M35-EXT Truth-Audit (INFORMATIONAL) — 2026-07-13

**Version read:** v1.0.239 (SUPERSEDED — v1.0.240 is current; DP4-22 edge-on
Fisher→linear fix integrated 39b7aed1/52deba02; P4 clean-wave streak already
honestly reset 12→0 by that commit).
**Status:** informational. Verdicts recorded as-is — both raws are real reads of
the immediately-prior version. Ledger-first (`tools/ledger_match.py`) + Opus §3.

## Provenance

| Leg | Raw | Screenshot | Verdict | Counts |
|-----|-----|-----------|---------|--------|
| Grok | `P4_grok_M35.md` | `P4_grok_M35.png` present | **MINOR REVISIONS** (raw l.1 `VERDICT: MINOR REVISIONS`) | 0 MAJOR / 5 MINOR |
| ChatGPT | `P4_chatgpt_M35.md` | `P4_chatgpt_M35.png` present | **MAJOR REVISIONS** (raw l.1 `VERDICT: MAJOR REVISIONS`) | 11 MAJOR / 3 MINOR |

Both raws READ verbatim before any verdict recorded (directive I4). Content is
P4 chirality (p_eq>0.6 HC dipole, MASTER ℓ=1, injection-recovery, Shamir
comparison) — provenance CONFIRMED P4.

## ledger_match (strict, threshold 0.3)

- Grok: 4/7 MATCHED (2 header/footer noise rows + 1 low-score → §3 below).
- ChatGPT: 7/13 MATCHED (1 header noise + 5 low-score fingerprint-weak → §3).

## §3 Opus disposition — every finding

### Grok (MINOR, 5 real findings)
1. p_eq>0.6 primary-threshold justification not stated explicitly → **DP4-07** (outcome-dependent post-selection / preregistration). RE-FLAG.
2. MASTER ℓ=1 +3.64σ residual ~47% unexplained, caveat more prominently → **DP4-17** (joint real-space×harmonic covariance / 47% remainder, OPEN-COMPUTE). RE-FLAG.
3. GZ1-human null (z=−0.54σ) coarser floor A_95≈4.5–6.8% should be quantified → **DP4-09/-10** (injections bypass classifier; GZ1 low power). RE-FLAG.
4. Shamir comparison: matched-footprint Ganalyzer reanalysis still required; avoid phrasing as direct exclusion → **DP4-06/-01** (block-bootstrap z≈−7.6 not an exclusion statistic; matched-Ganalyzer caveat disclosed). RE-FLAG.
5. Presentation: consolidated flowchart / executive summary of estimator→claim map → **DP4-14** (presentation harmonization). RE-FLAG.

### ChatGPT (MAJOR, 11 MAJOR + 3 MINOR)
- p_eq>0.6 not preregistered / trials accounting → **DP4-07**. RE-FLAG.
- Uniform A_p permutation assumes exchangeable pixels / forward-sim needed → **DP4-15/-16** (spatially-resolved confusion matrix / generative survey-systematics null). RE-FLAG.
- Unresolved non-null structure (4.2–4.4σ, p_LEE≤1e-4, 47% harmonic) not "diagnostic" → **DP4-17**. RE-FLAG.
- Injection into hard-label field bypasses classifier → **DP4-15/-09**. RE-FLAG.
- Classifier-dilution transfer factor g≃0.398, 1.7%→0.68% observed → **DP4-12** (transfer-function / bound framing). RE-FLAG.
- z≃−7.6 block-bootstrap not a calibrated test / direction not handled → **DP4-06/-01**. RE-FLAG.
- 66.5% CE-ResNet pseudo-labels, GZ1 69.91%, disjointness not shown → **DP4-08/-15**. RE-FLAG.
- GZ1-human cross-check has no power to validate sub-percent → **DP4-10/-09**. RE-FLAG.
- +3.64σ vs +7.93σ inconsistent convention / moment-z not Gaussian σ → **DP4-10/-13**. RE-FLAG.
- A_95 detection-efficiency threshold ≠ confidence/credible upper limit → **DP4-09/-17**. RE-FLAG.
- (MINOR) ECE Jensen bound population mismatch → **DP4-13**. RE-FLAG.
- (MINOR) mutable branch / DOI placeholder → **DP4-21**. RE-FLAG.

## SPECIAL CHECK — DP4-22 pre-echo (edge-on 8.98%-vs-18.8%)

**NOT FOUND in either raw.** `grep -in "edge-on|edge on|8.98|18.8|f_edge|0.158|1.188|1.090|cramér|fisher"` over BOTH raws = **0 hits**. Neither Grok nor
ChatGPT independently flagged the Appendix-E Fisher-CRB-sqrt-vs-linear penalty
internal inconsistency that DP4-22 (M24-EXT ChatGPT #10) closed. **M35 is
therefore NOT a pre-integration confirmation of DP4-22** — it is pure
pattern-066 verdict-word variance on disclosed standing content.

## Verdict

**0 genuinely-new reader-visible editable findings** across both M35 P4 legs.
Every finding = source-cited standing DP4 disposition (all already OPEN-COMPUTE
/ referee-variance / disclosed-limitation on the superseded v1.0.239). All
substantive items are ALSO already carried in / superseded by v1.0.240.

- **Cap HOLDS 80** (50 + Grok MINOR 12 + ChatGPT MAJOR 6 + Gemini-latest MINOR 12; post_verdict.sh recomputed both legs = 80).
- **Streak stays 0** (already reset 12→0 by DP4-22; an informational read of a superseded version neither advances nor resets the clean-wave clock).
- **No bump** (both raws read superseded v1.0.239; v1.0.240 current); directive_g.sh not run.

Integrity: never faked an accept, never dismissed a finding without a
source-cited verdict, never fabricated.
