# P2 M15 EXT truth-audit (2026-07-12, vs byte-unchanged v1.7.116)

**Raws:** `P2_grok_M15.md` (MINOR REVISIONS) + `P2_chatgpt_M15.md` (REJECT).
Both read verbatim before disposition. Paper byte-unchanged since M13/M10
(directive-M presentation restructure; ZERO content change). `directive_g.sh`
NOT run (no EXT edit). No faked accept, no un-sourced dismissal, no fabrication.

## Grok — MINOR REVISIONS (5 MINOR)

| # | finding | verdict → D-id |
|---|---------|----------------|
| 1 | Assumption (d) cubic transmission δf_NL≲10⁻³ = gradient-expansion estimate, not full numerical Maldacena cubic; add "full numerical verification remains future work" | RE-FLAG → **DP2-13 / DP2-32.6** (load-bearing caveat ★ already flagged not-a-full-3rd-order-in-in; conditional-on-dressed-metric wording present) |
| 2 | ~1.3σ/0.8σ floor uses transferred proxy ρ=−0.868 (Cov_B not public); reiterate proxy dependence in abstract headline range | RE-FLAG → **DP2-07 / DP2-33 / DP2-26** (0.8σ + proxy-floor disclosure landed in abstract v1.7.112; Cov_B unavailability disclosed) |
| 3 | BF≈9–14 prior-dependent; qualify abstract as "prior-dependent illustrative … recommended baseline priors" | RE-FLAG → **DP2-18 / DP2-30** ("illustrative … not definitive model-selection evidence"; four-corner prior grid `tab:bayes`) |
| 4 | 37-page length; condense SVD / per-coefficient scatter / Wick algebra to supplement | RE-FLAG → **DP2-30** (presentation-scope, Houston-gated OPINION) |
| 5 | Appendix A: add one explicit Cai-Eq.37-vs-(A4) cross-reference for the −35/16 vs −35/8 verification | RE-FLAG → **DP2-01 / DP2-02 / DP2-25** (−35/16 quadruple-certified; Cai's −35/8 = unreproduced-from-transcribed-coefficients literature value; App A per-vertex table present) |

**Grok closing sentence AFFIRMS the central claim** ("the corrected prediction
−35/16 … is supported by the vertex-level re-derivation, independent Fisher
validation … conditional on the listed assumptions"). 0 genuinely-new.

## ChatGPT — REJECT (10 MAJOR + 2 MINOR)

| # | finding | verdict → D-id |
|---|---------|----------------|
| 1 | Cai–Li resolution: −(99/128) is a summation-convention artifact (3 vs 6 ordered (5,2,2) terms); manuscript hasn't demonstrated the printed-polynomial arithmetic error | RE-FLAG → **DP2-01 / DP2-03 / DP2-25** (sign −(99/128) + −305/64 already corrected v1.7.108; ordered-sum convention stated verbatim L1489; Cai's −35/8 held only as unreproduced literature value) |
| 2 | Coefficient set (2,7,3,−12,−69,19) vs App-A (3,1,−9,5,−33,9); "globally halving" inconsistent → null-space is an artifact | RE-FLAG → **DP2-15 / DP2-02** (amplitude-invariant shape-basis stress band r=0.85±0.13 NEVER enters σ_eff; reparametrization-non-invariance caveat present verbatim L966; −35/16 certified) |
| 3 | Cubic transmission δf_NL≲10⁻³: single-clock ≠ ζ̇→0 in non-attractor contraction; no 3rd-order action/matching/numerics; Wilson-Ewing uses 1−2ρ/ρ_c not dressed-metric c_s²=1 | RE-FLAG → **DP2-13 / DP2-32.6** (load-bearing caveat; conditional-on-dressed-metric; deformed-algebra signature-change window flagged as least-controlled) |
| 4 | c_s=1 cubic vs "viable" c_s≪1 model inconsistent given f_NL=−165/16+65/(8c_s²) | RE-FLAG → **DP2-19** (Assumption (a) fixes c_s=1 quasi-dust benchmark; low-c_s is a separate qualitative note) |
| 5 | r=0.84 template-mismatch: should be cross-Fisher F_local,bounce/F_local,local with full survey covariance; own r_eff≈0.99 shows 0.84 is a different statistic | RE-FLAG → **DP2-14 / DP2-22** (r=0.84 = deliberately-conservative flat-weight cosine headline; r_eff≈0.99 = survey-optimal validation cross-check; reconciled §spherex, different quantities by construction) |
| 6 | "Independent Fisher validation" matching one Heinrich number with simplified real-space calc doesn't validate covariance; RSD extension gives 0.42–0.45 | RE-FLAG → **DP2-22 / DP2-17** (labeled a validation not an independent forecast; limitation list disclosed §spherex L1045; reproduction 2–11%) |
| 7 | Systematic budget mixes incompatible ρ constructions; ρ=−0.868 is SDB-PS not bispectrum, |ρ|≃0.95 is a shape cosine; neither valid in σ_marg | RE-FLAG → **DP2-07 / DP2-04 / DP2-33** (envelope subordinated; 0.8σ/1.3σ both disclosed as marginal-sensitivity estimates not channel-native precisions) |
| 8 | Bayes factors not reparameterization-invariant; scaling σ→σ/r while retaining W changes 17.1→14.4 by coordinate choice | RE-FLAG → **DP2-18 / DP2-30** (BFs illustrative + prior-dominated; prior-width sensitivity mapped) |
| 9 | κ_ε∈[2.8,40] not derived; "~14×" mode-function enhancement unexplained; 0.6–8% correction / Eq.(13) don't follow | RE-FLAG → **DP2-20** (κ_ε = single-prefactor-derivative estimate, cancellations acknowledged, fNL–n_s relation labeled indicative) |
| 10 | MegaMapper outlook: SPHEREx nuisances transferred to z=2–5; 1.5–3.85σ not a controlled forecast; remove from abstract | RE-FLAG → **DP2-30** (disclosed verbatim L1120: "no finalized instrument design … illustrative … uncalibrated projection … relativistic projection effects grow steeply … design-uncertainty envelopes not calibrated forecasts") |
| 11 (MIN) | "gauge-frame survey observable" / factor-146 framing misleading | RE-FLAG → **DP2-21** (framing dispute over comoving-gauge consistency-term; 146× disclosed as gauge-frame template-amplitude ratio; no numeric error) |
| 12 (MIN) | Organization/reproducibility: 37pp restates caveats, mutable script/JSON filenames, DOI not yet supplied | **PROCESS-NIT** (no reset) → **DP2-30** (presentation-streamlining, Houston-gated) + real-GitHub-repo pointer present, Zenodo DOI pending-at-camera-ready (DP2-31.5) |

**ChatGPT closing** disputes framing/universality/significance but concedes
"−35/16 may be a plausible canonical-limit result" — i.e. no arithmetic defect in
the headline. This is the standing OpenAI/ChatGPT maximally-harsh referee floor
(directive-H, DP2-24) on honestly-scoped single-source-recast content whose
external per-triangle Cov_B is unavailable (venue/impact, Houston-gated), NOT an
editable correctness defect. **0 genuinely-new.**

## Verdict
**0 genuinely-new reader-visible editable findings on P2.** Every MAJOR/MINOR
across both legs is a source-cited re-flag of a standing DP2 D-id (or PROCESS-NIT).
Grok MINOR + closing-affirms; ChatGPT REJECT = structural floor. clean-wave
streak **5→6**; cap **74 HOLDS**. No bump; `directive_g.sh` not run.
