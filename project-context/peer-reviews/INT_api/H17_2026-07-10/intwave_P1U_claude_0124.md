# INT Claude-subscription Review — P1U v1U.0.16 — claude-opus-4-8
paper: P1U  version: v1U.0.16  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T08:24:50Z
context-note: wave on v1U.0.16: NJL leg-A scope precision (scalar chi-SB channel only; attractive AA/PP via leg B) — DP1U-26 closed

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've verified all the load-bearing numbers against the committed script/JSON. My arithmetic (done by hand against the JSON, which the sandbox blocks me from re-executing but whose values match): Holst factor = 0.0698 (⇒ 1/0.0698 = 14.3×); scalar worst-case ratio 0.156; amplitude ρ_NJL ≈ 4×10⁻⁸¹ eV⁴ ≈ 1.4×10⁻⁷⁰ ρ_Λ. All consistent with the text. The one genuinely-new issue is in the wave's own edit.

---

(1) **VERDICT: MINOR REVISIONS**

(2) **ISSUES:**

1. **[MINOR]** App. `app:njl_gap` / Route-1, leg (B) disposition of the *attractive* channels (`arxiv/paper1_unified.tex:5106-5112` and the mirror at `:2695-2699`). The v1U.0.16 scope-precision edit correctly restricts the sign exclusion to the scalar (SS) channel and concedes that AA/PP are attractive — but the magnitude-leg justification it offers is **incomplete for the AA channel**. The text disposes of both AA and PP "since $|G_{\rm PP}|=|G_{\rm scalar}|$ is equally sub-critical," yet by the paper's own Eq. `eq:AAdecomp` the coefficients are $G_{\rm AA}=+\tfrac{3}{32}\kappa$ and $G_{\rm scalar}=-\tfrac{3}{64}\kappa$, i.e. $|G_{\rm AA}| = 2\,|G_{\rm scalar}|$. The quoted worst-case ratio $|G_{\rm eff}|/G_{\rm crit}=0.156$ (and the closed-form $(3/64)N_fN_c/\pi^2$) is computed with $|G_{\rm eff}|=\tfrac{3}{64}\kappa$ in `njl_gap_equation_route1.py:177`, so it demonstrates sub-criticality for SS/PP but **not** for AA. The AA channel's worst-case ratio is $\approx 0.31$ ($=2\times0.156$; still $<1$, so the exclusion survives), but as written the paper cites a number that does not cover the very channel the sentence claims to dispose of. Fix: state the $G_{\rm AA}$ magnitude explicitly and give its ratio (worst case $\approx0.31$, sub-critical), rather than folding it under "$|G_{\rm PP}|=|G_{\rm scalar}|$." The committed script should also emit the AA ratio so the artifact backs the claim.

2. **[MINOR]** App. `app:njl_gap:5123-5127` states "the worst case is $|G_{\rm eff}|/G_{\rm crit}=0.156$ ... **across all cutoffs and flavor counts scanned**." Given issue #1, this "worst case" is only the worst case for the scalar/PP magnitude; the genuinely worst attractive-channel ratio in the model is the AA value ($\approx0.31$). The wording "across all ... scanned" overstates coverage. Either scan/report the AA channel or qualify "worst case" as scalar-channel.

(3) The central claim — channel-level closure of the four minimal-ECH dark-energy routes, and specifically the Route-1 vacuum-condensate exclusion — **is supported**: every load-bearing number verifies against the committed artifact, the mean-field framework is honestly scoped, and even the under-stated AA channel remains sub-critical (≈0.31 < 1), so no condensate forms; the two flagged items are precision/completeness gaps in the newly-added justification prose, not a defect in the conclusion.
