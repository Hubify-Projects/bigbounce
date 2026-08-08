# INT Claude-subscription Review — P2 v1.7.116 — claude-opus-4-8
paper: P2  version: v1.7.116  tex: research/focused_paper_source_integration/02_full_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T19:09:21Z
context-note: M4 wave on v1.7.116; no changes since M1 (0-new)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the full manuscript and verified the load-bearing numbers against the committed artifacts (the c15 channel-native Fisher JSON, the Bayes-factor closed-form formulas, the proxy-floor arithmetic, and the vertex-sum/per-vertex/order-grouped certifications of −35/16). Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR] Central deliverable is a marginal-sensitivity recast, and the title oversells it.** Title (`02_full_draft.tex:27`) "Testing the Matter Bounce with Primordial Non-Gaussianity" vs. the actual bottom line in the abstract (`:975`): ~2.6–2.75σ optimistic, reducing to ~1.3–2.75σ post-systematics and ~0.8σ under the GR bracket. SPHEREx alone cannot *decisively* test this signal; the abstract discloses this honestly, but "Testing" in the title implies a discriminating test the forecast does not deliver. Recommend softening to "Forecasting"/"Sensitivity to."

2. **[MINOR] Over-hedging materially impairs readability — the single biggest barrier to acceptance.** The Introduction "Scope and conventions" paragraph (`:984`) is a ~450-word single paragraph; the Systematics up-front scope paragraph (`:1332`) is a ~700-word single paragraph nesting proxy-floor, channel-native, and availability disclosures. The v1.7.116 changelog itself is a "presentation restructure." A PRD referee will still find the prose reads as a rebuttal-hardened document rather than a clean manuscript. Compress the repeated r/r_cos/r_eff/ρ and proxy-vs-channel-native restatements to one canonical statement each.

3. **[MINOR] The forecast rescales a *single* external forecast (Heinrich et al.), and the conservative floor still rests on a transferred proxy.** `:984` and `:1332`: the quoted GR floor uses ρ=−0.868 transferred from the power-spectrum SDB channel because Cov_B is not public. The channel-native c15 computation (verified: `outputs/c15_channel_native_fisher.json` gives σ_marg=0.9417→2.32σ, ρ_2×2=−0.425, ρ_3×3=−0.494, matching `:984`) is explicitly *not* claimed to close the objection. This is honest, but the headline sensitivity is therefore conditional on an external, non-reproducible covariance — a structural limitation the reader must be able to locate in one place.

4. **[MINOR] "Discrimination" rests on prior-dependent, self-described *illustrative* Bayes factors of a shape-degenerate signal.** `:1038` r_cos>0.97 to local; `:1324` the QSFI μ/H→0 endpoint is shape-degenerate with the bounce; `:1291`/`:1316` the BFs "should be interpreted as upper bounds… not as robust model-selection evidence." A detected f_NL≈−2 does not uniquely point to a bounce. (The BF arithmetic checks out: `:1248` 30/(√2π·0.7)=17.10 ✓; `:1316` exp[(35/16)²/(2·0.7²)]=132 ✓.) The disclosure is adequate; the concern is that the paper's discrimination narrative leans on numbers it simultaneously disowns.

5. **[MINOR] MegaMapper section is an admittedly uncalibrated placeholder.** `:1183`/`:993` label MegaMapper as unapproved/unfunded and the systematic budget as transferred, not calibrated to z=2–5. Consider relegating to a short outlook to avoid implying a second independent forecast.

6. **[MINOR] Strong claim that a published PRD result contains an arithmetic error — well-supported but should state reproduction status precisely.** `:1541`–`:1633` (App. A). The −35/16 certification is internally airtight and I confirmed every fraction: per-vertex column sums (−25/16, −5/32, 0, −15/32) = −35/16 and equilateral = −255/128 (`:1588`–`:1592`); order-grouped −5/2+5/16+0=−35/16 (`:1611`); spurious −(99/128)Σk³ maps −35/16→−305/64 = −4.766 (`:1553`). The paper correctly narrows the claim to "one identified discrepancy" and does *not* claim to reconstruct Cai's −35/8. Good. Only caveat: the certification scripts require the two arXiv source tarballs (not redistributed, per `scripts/caili_certification/README.md`), so full independent reproduction depends on external inputs — state this in Data & Code Availability so a referee isn't surprised.

**(3)** Yes — the central claim (matter bounce predicts a corrected local f_NL=−35/16, and SPHEREx delivers a ~1–3σ *sensitivity* to it) is supported: every load-bearing number I recomputed reproduces exactly from the committed artifacts, and the −35/16 correction is genuinely and reproducibly certified; the remaining issues are presentation, scope-framing, and the marginal (non-detection) strength of the deliverable, not computational error.

Consistent with the M4-wave note, I found **no genuinely-new finding** — no new computational or physics error surfaced; all issues above are the same presentation/scope class already tracked in prior dispositions.
