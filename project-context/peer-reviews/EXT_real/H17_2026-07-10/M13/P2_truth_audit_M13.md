# P2 M13-EXT truth-audit (2026-07-12) — STRICT, ledger-first

**Raws (verbatim, read before any disposition):**
- `M13/P2_grok_M13.md` = **MINOR REVISIONS** (1 MAJOR + 5 MINOR) — l.1 `VERDICT: MINOR REVISIONS`
- `M13/P2_chatgpt_M13.md` = **REJECT** (13 MAJOR + 2 MINOR) — l.1 `VERDICT: REJECT`

Both on byte-unchanged **v1.7.116** (`\date{July 12, 2026}`, headline $\fnl^{\rm local}=-35/16$).
Pre-triage: `tools/ledger_match.py` (Grok 4/7, ChatGPT 12/15 MATCHED); every UNMATCHED +
every low-score MATCHED given a full §3 source-cited disposition below.

## VERDICT: 0 genuinely-new reader-visible editable findings

### EXT-Grok MINOR (1 MAJOR + 5 MINOR) — all re-flags
- **[MINOR] 1.3–2.75σ conflates distinct procedures; abstract must flag the 1.3σ floor as conservative proxy** → **DP2-04 / DP2-07 / DP2-33** (scoping envelope + 0.8σ/1.3σ proxy-floor disclosure landed in the abstract v1.7.112; channel-native floor 2.32σ > proxy, DP2-34/-35). Disclosed verbatim.
- **[MAJOR] App-A must display explicit four-vertex contributions + side-by-side Cai/Li so the factor-of-two is independently verifiable** → **DP2-01 / DP2-02 / DP2-16 / DP2-25**. `tab:vertexwalk` + `tab:vertices` + `eq:order_grouped` + `eq:collapsed_vertexsum` give the explicit per-vertex algebra; −35/16 quadruple-certified. Cai's separately-published −35/8 remains an unreproduced literature value (DP2-25, OPEN-COMPUTE, Houston-gated). Placement/self-containedness = DP2-30 OPINION. Not a numeric defect.
- **[MINOR] internal filenames/JSON/script names clutter the narrative; move to a single Data Availability statement** → **DP2-30** (presentation-scope, Houston-gated; directive-M restructure already consolidated). PROCESS-NIT.
- **[MINOR] state quantitatively how much the 1.3–2.75σ range shifts under the full Heinrich non-Gaussian covariance vs the Gaussian surrogate** → **DP2-22 / DP2-26**. Reproduction-vs-Heinrich limitation list disclosed (§spherex); full per-triangle Cov_B is external (DP2-26 OPEN-COMPUTE, confirmed not public). Disclosed.
- **[MINOR] MegaMapper "uncalibrated/illustrative" needs a dedicated caveat paragraph** → **DP2-30** (the uncalibrated-projection caveat is present verbatim in the paper; directive-M relegated it with the caveat retained). Disclosed.
- **[MINOR] Bayes-factor 9–14 "illustrative" qualifier must appear at abstract prominence** → **DP2-18** ("illustrative … not definitive model-selection evidence" already in abstract + conclusion + scope-summary). Disclosed.

Grok's own one-sentence CREDITS the central claim ("supported by the explicit overlap calculation, independent Fisher validation, and closed-form Bayes-factor cross-checks"). **0 genuinely-new.**

### EXT-ChatGPT REJECT (13 MAJOR + 2 MINOR) — all re-flags
- **[MAJOR] Wilson–Ewing model combines incompatible c_s=1 vs c_s≪1 realizations** → **DP2-19 / DP2-02** (assumption (a) fixes the c_s=1 quasi-dust benchmark explicitly; low-c_s is a separate qualitative note). Disclosed scope.
- **[MAJOR] App-A "internally contradictory" ordered-sum vs single-time-ordered** → **DP2-16** (ordered-sum convention stated explicitly; in-in operator-algebra identity A7–A12, −2Im doubling via Hermiticity). Disclosed.
- **[MAJOR] −(99/128)Σk³ diagnosis depends on unresolved permutation convention** → **DP2-01 / DP2-25** (sign corrected to −(99/128), A_T→−305/64 in v1.7.108; the single discrepancy is traced, Cai's full −35/8 mechanism remains OPEN-COMPUTE/Houston-gated). Disclosed.
- **[MAJOR] null-space fitting 6 coeffs to 3 benchmarks = arbitrary interpolants; 10⁴ sets have no physical meaning, remove** → **DP2-15** (amplitude-invariant shape-basis stress band that NEVER enters σ_eff; reparametrization-invariance caveat present verbatim L966). Methodological-interpretation, not a numeric error.
- **[MAJOR] uses the "erroneous" printed shape for overlap after renormalizing; additive local term shifts B_NL** → **DP2-01 / DP2-16** (overlap computed from the corrected vertex sum; the −(99/128) term is the identified discrepancy, not a renormalization). Disclosed.
- **[MAJOR] "cubic-order closure" through the bounce not derived; δf_NL≲10⁻³ an assumption** → **DP2-13 / DP2-32.6** (explicitly-flagged load-bearing caveat (★); closed at cubic order by dof-counting, now stated conditional on the dressed-metric quantization). Disclosed open item.
- **[MAJOR] r=0.84 template-recast not established; needs marginalized cross-Fisher** → **DP2-14 / DP2-17 / DP2-34** (r=0.84 = conservative flat-weight cosine headline; channel-native cross-Fisher α=0.992 computed v1.7.114/-115). Disclosed + computed.
- **[MAJOR] "independent Fisher validation" not end-to-end; 0.42–0.45 vs 0.63–0.69 unexplained** → **DP2-22** (reproduction-vs-Heinrich limitation list disclosed; labeled a validation, not an independent forecast). Disclosed.
- **[MAJOR] Table-V systematic construction combines incommensurate quantities; ρ values not interchangeable; 1.3σ not a "conservative floor"** → **DP2-04 / DP2-07 / DP2-34 / DP2-35** (channel-native ρ≈−0.42 computed, floor 2.32σ > proxy 1.30σ retained as conservative cross-check). Computed + disclosed.
- **[MAJOR] b_φ treatment: Heinrich uses the universal relation, not a 20% Gaussian prior; assignments asserted** → **DP2-04 / DP2-34** (b_φ-widening prior sweep is the disclosed marginalization; ρ(f_NL,b_φ)=+0.99 computed). Disclosed.
- **[MAJOR] quasi-dust κ_ε∈[2.8,40] schematic; 0.6–8% uncertainty not derived; lower endpoint 2.38σ≠2.6σ** → **DP2-20** (κ_ε labeled a single-prefactor-derivative estimate; post-shift bracket value not the headline). Disclosed indicative.
- **[MAJOR] Bayes factors = prior-volume ratios; remove BF≃9–14 from abstract** → **DP2-18** (labeled illustrative/prior-dominated; four-corner prior grid in tab:bayes). Disclosed.
- **[MAJOR] MegaMapper: no MegaMapper-specific Fisher; uncalibrated scenario** → **DP2-30 / DP2-14** (MegaMapper labeled illustrative/uncalibrated verbatim; disclosed). Disclosed.
- **[MINOR] bare comoving-gauge f_NL≃0.015 shouldn't be called the "on-sky quantity"** → **DP2-21** (gauge-frame framing dispute; physical-frame statement confined to its proper role). Disclosed non-real.
- **[MINOR] scope/presentation: ECH/anomaly/birefringence/running-f_NL/AI-narrative not needed; split the paper** → **DP2-30** (presentation-scope, Houston-gated; directive-M relegated birefringence to app:birefringence). PROCESS-NIT.

ChatGPT's own conclusion concedes "the canonical algebra may favor f_NL=−35/16" — the central certification withstands the challenge; the REJECT rests on survival-through-bounce + forecast-scope (disclosed venue DP2-13/-17/-29). ChatGPT structural harsh-referee floor (directive-H). **0 genuinely-new.**

## Streak / Cap
- **Streak 4→5.** Prior M10-EXT was the 0-new wave that took the streak 3→4; M13-EXT = SECOND consecutive 0-new on byte-unchanged v1.7.116 → **4→5** (directive-K).
- **Cap 74 HOLDS.** Grok EXT MINOR (12) + ChatGPT EXT REJECT (0) + Gemini EXT MAJOR carry-forward (6); verdict words unchanged from M10 → no cap motion. 50 + 12 + 0 + 6 reconciles to the prior Convex-recorded 74 (Gemini EXT carry-forward per prior reporting).

## Integrity
Both raws read verbatim (Grok l.1 `VERDICT: MINOR REVISIONS`, ChatGPT l.1 `VERDICT: REJECT`) before any disposition. No ACCEPT faked. Every finding source-cited to an existing D-id + tex line/section. No un-sourced dismissal. No math fabricated. No version bumped. `directive_g.sh` NOT run (no reader-visible edit). ChatGPT −35/16 concession recorded verbatim.
