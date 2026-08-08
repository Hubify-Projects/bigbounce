# P2 truth-audit — M41 EXT (2026-07-13)

**Paper:** P2 (matter-bounce f_NL SPHEREx forecast), byte-unchanged **v1.7.116** (no edit
this wave). Raws read verbatim before any verdict: `M41/P2_grok_M41.md` (+ `.png`) and
`M41/P2_chatgpt_M41.md` (+ `.png`).

## Verdicts (from raw line 1, verified)
- **Grok = MINOR REVISIONS** (2 in-MINOR MAJOR-tagged / 3 MINOR; the MAJOR tags sit under a
  MINOR-REVISIONS header = in-MINOR emphasis, pattern-066 band). Closing AFFIRMS the central
  claim: "the corrected matter-bounce f_NL = −35/16 yields a realistic SPHEREx sensitivity …
  is supported by the explicit template-overlap calculation, the Heinrich et al. recast, the
  independent surrogate Fisher validation, and the closed-form Bayes-factor cross-checks."
- **ChatGPT = REJECT** (11 MAJOR / 2 MINOR) — documented maximal-harsh-referee floor (DP2-24);
  item set 1:1 with M15/M23/M31/M34/M37 REJECTs. Closing concedes "the canonical c_s=1
  contracting-phase vertex sum supports f_NL^local = −35/16."

## Provenance
Both raws review the correct f_NL SPHEREx-forecast paper (−35/16 vertex sum, r=0.84, Heinrich
covariance, Bayes factors, δf_NL≲10⁻³, App-A Cai–Li all present).

## Per-finding disposition (ledger_match draft + Opus adjudication)
ledger_match: Grok 5/6 auto (#1 scaffold-header non-finding), ChatGPT 10/13 auto; 3 UNMATCHED
Opus-adjudicated below. All source-cited standing DP2 re-flags.

**Grok (2 MAJOR / 3 MINOR):**
- Headline 1.3–2.75σ envelope mixes 3 procedures; prioritize/justify one or table all three → **DP2-04/-34** (CLOSED-BY-EDIT envelope subordinated + channel-native Fisher).
- −35/16 correction: print discrepant polynomial coefficients in main text → **DP2-01/-02/-16** (RE-FLAG-DISCLOSED; App-A four-vertex + `tab:vertexwalk` present; −35/16 quadruple-certified).
- Independent Fisher fixes b2/bs2, omits non-Gaussian covariance; quantify r_eff shift → **DP2-14/-22** (RE-FLAG-DISCLOSED; reproduction limitation list disclosed §spherex).
- MegaMapper 1.5–3.5σ + BF≈9–14 illustrative but presented as targets; add prior-sensitivity → **DP2-30/-18** (OPEN-VENUE presentation + illustrative-BF disclosed).
- Six r-like symbols + σ floors: add notation table → **DP2-04** / DP2-31.4 (r-notation clause added v1.7.111). Presentation.

**ChatGPT (11 MAJOR / 2 MINOR):**
- #1 App-A Cai–Li narrative "algebraically incorrect", −99/128 term, not −305/64 → **DP2-01** (CLOSED-BY-EDIT v1.7.108; the −305/64 / +99/128-sign is the disclosed distinction; re-falsified by re-running committed `p2_vertex_check.py` + Li formula; headline −35/16 unaffected).
- #2 §II A polynomial reconstruction / null-space uncertainty, vertex-sum coefficients fixed → **DP2-15** (RE-FLAG-DISCLOSED; amplitude-invariant stress band, never enters σ_eff, reparametrization caveat present verbatim L951).
- #3 §III B r=0.84 template-recovery not established without full Fisher projection → **DP2-14** (RE-FLAG-DISCLOSED; r=0.84 flat-weight cosine = deliberately conservative headline).
- #4 §IV independent Fisher uses same coefficient vector, doesn't validate corrected template → **DP2-14/-22** (RE-FLAG-DISCLOSED; validation-not-forecast, disclosed).
- #5 **UNMATCHED (0.23)** §II C-D Wilson-Ewing consistency: c_s=1 cubic action vs c_s≪1 matter → **Opus RE-FLAG: DP2-19 (c_s=1 = the quasi-dust benchmark, assumption (a) §assumptions L954; low-c_s viability a separate qualitative note) + DP2-13.** Identical to M34/M37 "Wilson-Ewing scope=DP2-13/-19." NOT genuinely-new.
- #6 §II C cubic-order transmission bound δf_NL≲10⁻³ "assertions not derived" → **DP2-13** (RE-FLAG-DISCLOSED; load-bearing caveat (d), OOM single-clock scaling, honestly disclosed open item).
- #7 §II C/§VIII B quasi-dust κ_ε∈[2.8,40] not from controlled expansion → **DP2-20/-19** (RE-FLAG-DISCLOSED; κ_ε labeled single-prefactor-derivative estimate, cancellations acknowledged).
- #8 §VII GR-projection template not relativistic kernel, squeezed→0 → **DP2-07** (RE-FLAG-DISCLOSED; proxy → 0.8σ lower edge tabulated, ρ=−0.868 structural reason disclosed).
- #9 §VII E/Table V 1.3–2.75σ mixes procedures, not joint forecast → **DP2-04** (CLOSED-BY-EDIT envelope subordinated).
- #10 §VI C Bayes factors = prior-volume, not model discrimination → **DP2-18** (RE-FLAG-DISCLOSED; labeled illustrative, prior-width grid `tab:bayes`).
- #11 **UNMATCHED (0.27)** §IV Eq.(7)/§VII D unmodelled covariance + photo-z claims (δC/C∼f_NL²Δζ²/N not a derivation; 5%/10–20% not from documented Fisher) → **Opus RE-FLAG: DP2-22 (in-house Fisher reproduction-vs-Heinrich limitations disclosed) + DP2-26 (channel-native GR-marg ρ cannot be pinned in-repo without Heinrich Cov_B — OPEN-COMPUTE/external-data-gated) + DP2-04.** Identical to prior-wave "covariance=DP2-22/-26" mapping. NOT genuinely-new.
- #12 **UNMATCHED (0.17)** (MINOR) MegaMapper outlook transferred budget, 1.5–3.5σ not a forecast result → **Opus RE-FLAG: DP2-30 (presentation-scope MegaMapper, disclosure verbatim L1120: "no finalized instrument design … illustrative … uncalibrated … design-uncertainty envelopes, not calibrated forecasts").** NOT genuinely-new.
- #13 (MINOR) §VI A/IX/App B gauge-frame observable + 37pp repetition/off-scope material → **DP2-21/-02/-30** (RE-FLAG-DISCLOSED gauge-frame framing + presentation-scope).

## Genuinely-new count: 0
Every finding fingerprint-matches a canonical DP2 disposition; the two MINOR PROCESS-NITs
(Zenodo DOI / immutable archive) → DP2-30 (no reset). The ChatGPT REJECT crux (#1 Cai–Li
"algebraically incorrect") was re-falsified by re-running the committed derivation +
convention-free Li formula this wave — NOT hand-waved. Headline −35/16 unaffected.

## Recording
- clean-wave streak **15 → 16** (M35/M36 had no P2 leg; this is P2's first re-test since M37).
- No bump (byte-unchanged v1.7.116); directive_g.sh NOT run.
- cap HOLDS **74** = 50 + Grok MIN 12 + ChatGPT REJECT 0 + latest-Gemini MIN 12 (post_verdict.sh
  recomputed, verified in Convex).
- post_verdict.sh: `M41-Grok` minor-revisions, `M41-ChatGPT` reject (EXT bare labels).
- record_wave.sh P2 M41: genuinelyNew 0, streak 16.

## Integrity
No ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.
