# INT Claude-subscription Review — P1U v1U.0.14 — claude-opus-4-8
paper: P1U  version: v1U.0.14  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T06:44:58Z
context-note: v1U.0.14 directive-L UPGRADE: the Route-1 vacuum-condensate item (prior out-of-scope concession in sec:r1_njl, DP1U-05/-19) is now a DERIVED exclusion. New Appendix app:njl_gap presents a regulated NJL gap equation on the paper's own operator -(3/16)kappa(J5.J5): (A) Fierz-projecting to the scalar (SS) condensate channel via eq:AAdecomp gives G_scalar=-(3/64)kappa<0 = REPULSIVE, so M=0 is the only effective-potential minimum at any coupling/cutoff (no condensate forms); (B) even |G_eff| is far sub-critical vs the derived G_crit=pi^2/(N_f N_c Lambda^2), |G_eff|/G_crit=(3/64)N_f N_c/pi^2 ~ 4.3e-2 at Lambda=M_Pl (worst case 0.156 scanned; Holst ~30x smaller). All numbers verified against arxiv/scripts/njl_gap_equation_route1.py. Abstract/intro/conclusion R1 claims upgraded to this two-pronged exclusion, mean-field NJL framework assumption stated explicitly. Please assess whether this closure is sound and whether the Route-1 claim is now correctly scoped.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have verified the core closure. Let me confirm the Holst factor arithmetic once more against the committed JSON values (EC vs Holst-dressed ratios) to be certain of the discrepancy.

The committed `njl_gap_equation_route1_results.json` gives, at Λ=M_Pl, N_f N_c=1: EC-maximal ratio = 0.0047494, Holst-dressed = 0.00033167. The ratio is 0.0047494/0.00033167 = **14.3×**, and `holst_factor` is recorded as 0.0698 (= γ²/(γ²+1) = 0.274²/1.075 = 1/14.3). This is consistent across every row of the JSON.

---

**Referee report — `arxiv/paper1_unified.tex` v1U.0.14 (Route-1 NJL closure, Appendix `app:njl_gap`)**

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR] "Holst-dressed values ∼30× smaller" is inconsistent with the paper's own committed script.** `arxiv/paper1_unified.tex:5099` (and the identical claim at `:2687`, and the version comment at `:64`) states the Holst-dressed couplings are "${\sim}30\times$ smaller." The Holst prefactor is $\gamma^2/(\gamma^2+1)$ with $\gamma_{\rm BI}=0.274$, giving $0.0698$ — i.e. a factor of $1/0.0698 = 14.3\times$, not $30\times$. This is exactly what the committed artifact reports: `njl_gap_equation_route1_results.json` records `holst_factor = 0.0698`, and every EC-vs-Holst row differs by 14.3× (e.g. `0.0047494 / 0.00033167 = 14.3`). The conservative direction is preserved (Holst only strengthens the exclusion), so the conclusion is unaffected, but the specific number in the body text contradicts the paper's own script and must be corrected to $\sim\!14\times$.

2. **[MINOR] Effective-potential-monotonicity wording is slightly stronger than the hard-cutoff calculation strictly licenses.** At `:5083–5084` and `:2679–2680` the text asserts a repulsive channel makes $\Omega(M)$ "monotone-increasing from $M=0$" so $M=0$ is "the only minimum." With a hard 4-momentum cutoff the loop term renders $\Omega(M)$ unbounded at large $M$ regardless of sign; the rigorous, and correct, statement is the standard one that a repulsive scalar channel supports no *chiral-symmetry-breaking* minimum (no $M\neq0$ bifurcation, which the derived $G_{\rm crit}>0$ with $G_{\rm scalar}<0$ already establishes). Recommend tightening the phrasing to the "no non-trivial gap-equation solution / no near-vacuum $\chi$SB minimum" formulation the mean-field framework actually proves. (The paper's explicit "within the standard mean-field NJL framework" hedge at `:5107` mostly covers this, so this is optional-strengthening, not a blocker.)

*Verified and found correct (no action needed):* the scalar-channel coefficient $G_{\rm scalar}=(-\tfrac{3}{16})(+\tfrac14)\kappa=-\tfrac{3}{64}\kappa$ (`eq:gscalar`) — the $+\tfrac14$ SS weight is the 4th **column** of the Fierz matrix $F$ (`eq:fierzmatrix`), which reproduces `eq:AAdecomp` exactly; the derived $G_{\rm crit}=\pi^2/(N_fN_c\Lambda^2)$ matches the textbook slope; and the sub-critical ratios $4.7\times10^{-3}$ (single species), $4.3\times10^{-2}$ ($N_fN_c=9$), and worst-case $0.156$ (strong-EFT, $N_fN_c=9$) all reproduce by hand from $(3/64)N_fN_c/\pi^2$ and $/\gamma_{\rm BI}$. The prior out-of-scope concession text has been fully removed (no stale contradiction remains), and the "mean-field NJL framework" scoping in the abstract (`:1223`) and verdict (`:5108–5111`) is honest.

**(3)** Yes — the central claim (the Route-1 vacuum chiral condensate is excluded, not merely deferred) is soundly supported: the decisive sign argument ($G_{\rm scalar}=-\tfrac{3}{64}\kappa<0$, repulsive) and the belt-and-suspenders sub-critical-magnitude argument both reproduce against the committed script, and the closure is correctly scoped to the mean-field NJL framework — the only fix needed is the erroneous "∼30×" Holst factor, which should read ∼14×.
