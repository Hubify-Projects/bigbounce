# INT Claude-subscription Review — P1U v1U.0.15 — claude-opus-4-8
paper: P1U  version: v1U.0.15  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T07:32:15Z
context-note: wave on v1U.0.15: Holst factor corrected to the script's 14.3x (2 sites); NJL exclusion otherwise verified sound

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the NJL closure (the load-bearing new content in this wave), the committed script, and its results JSON, and recomputed the key ratios. Here is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR] The "sign" exclusion (leg A) is not channel-complete, so "two independent exclusions" overstates it.** `arxiv/paper1_unified.tex:2682-2690` and `:5089-5095` present argument (A) as decisive: the scalar coupling is repulsive ($G_{\rm scalar}=-\tfrac{3}{64}\kappa<0$) so "no condensate forms at *any* coupling strength or cutoff." But the paper's own Fierz identity `eq:AAdecomp` (`:5008`, $(J^5\!\cdot\!J^5)\to+\tfrac14 SS+\tfrac12 VV-\tfrac12 AA-\tfrac14 PP$) makes the **AA channel attractive** ($-\tfrac{3}{16}\kappa\times(-\tfrac12)=+\tfrac{3}{32}\kappa>0$) and the **PP (pseudoscalar) channel attractive** ($+\tfrac{3}{64}\kappa>0$). Leg (A) only excludes the scalar $\chi$SB channel where $\langle\bar\psi\psi\rangle$ lives; a pseudoscalar/axial condensate in the attractive channels is excluded *only* by the magnitude leg (B), not by sign. The overall conclusion survives (B covers them, since $|G_{PP}|=|G_{\rm scalar}|$ is equally sub-critical), but (A) should be restricted to the scalar channel and (B) credited with disposing of the attractive channels.

2. **[MINOR] "Far sub-critical … in every case scanned" is an overstatement for the padded worst case.** `:2691` and the verdict at `:5112-5114` say "far sub-critical"; but the worst scanned ratio is $0.156$ (`:2696`, `:5107`), only a factor $\approx6.4$ below critical. Because $|G_{\rm eff}|/G_{\rm crit}=(3/64)(N_fN_c/\pi^2)(\Lambda/M_{\rm Pl})^2$ scales as $\Lambda^2$, the margin is genuinely large ($4.7\times10^{-3}$) only for the physical single-species ($N_fN_c=1$, $\Lambda=M_{\rm Pl}$) case; at the paper's own upper cutoff with the QCD-like padding it is $O(6)$. The phrase "comfortably sub-critical" used at `:5108` is accurate; "far … every case scanned" is not. Recommend tempering.

3. **[MINOR] Cutoff sensitivity not made transparent.** Neither `app:njl_gap` nor the script states that the ratio grows as $\Lambda^2$, so a reader cannot see that a cutoff only $\sim2.5\times$ above $\Lambda_{\rm strong}$ (at $N_fN_c=9$) would reach criticality. The choice $\Lambda_{\rm strong}=M_{\rm Pl}/\sqrt{\gamma_{\rm BI}}$ as the UV ceiling is asserted (`:5107-5108`, script L42-43) rather than justified. State the $\Lambda^2$ scaling and motivate the ceiling explicitly.

**Wave-specific verification (the Holst factor fix):** confirmed correct. $1/[\gamma^2/(\gamma^2+1)] = 1/0.06983 = 14.32$ with $\gamma_{\rm BI}=0.274$, and every EC-vs-Holst pair in `njl_gap_equation_route1_results.json` (e.g. $0.004749/0.0003317$, $0.156/0.01089$) confirms $14.3\times$. Both edited sites (`:2697`, `:5109`) now read "$\sim14\times$"; the prior "$\sim30\times$" was wrong. The fix preserves the conservative direction (Holst only strengthens sub-criticality). $G_{\rm scalar}=-3/64$, $G_{\rm crit}=\pi^2/(N_fN_c\Lambda^2)$, the closed-form ratios ($4.7\times10^{-3}$, $4.3\times10^{-2}$), and the leg-(i) finite-density number ($\rho_{\rm NJL}\approx4\times10^{-81}$ eV$^4\approx1.4\times10^{-70}\rho_\Lambda$) all recompute correctly against the artifacts.

**(3)** The central claim — Route-1 vacuum condensate excluded, and the four-route channel-level closure — is supported within the explicitly stated mean-field NJL scope; the three items above are presentation/rigor refinements, not defeaters.
