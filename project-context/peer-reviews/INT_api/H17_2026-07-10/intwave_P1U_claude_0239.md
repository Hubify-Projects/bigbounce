# INT Claude-subscription Review — P1U v1U.0.16 — claude-opus-4-8
paper: P1U  version: v1U.0.16  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T09:39:33Z
context-note: rebuild wave 2 on v1U.0.16; no changes since NJ3 (0-new adjudicated; NJL leg-A decisive per convention-independent sign)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have enough to complete the review. I hand-verified every number I could reach (the committed `njl_gap_equation_route1_results.json` matches the paper; the S·S identity is correct; the transparency argument is standard). Python execution is walled in this session, so the Fierz/dim-4 assertion runs are taken from committed artifacts, but the load-bearing NJL arithmetic I checked independently.

---

**Referee report — `arxiv/paper1_unified.tex` (v1U.0.16), PRD**

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR] NJL leg-(B) does not literally cover the AA channel it claims to exclude** — App. `app:njl_gap`, `arxiv/paper1_unified.tex:5108-5112` (and the same wording in the main text, `:2695-2699`). The text concedes that after Fierz projection the axial channel is *attractive* with $G_{\rm AA}=+\tfrac{3}{32}\kappa$ — i.e. **twice** the magnitude of $|G_{\rm scalar}|=|G_{\rm PP}|=\tfrac{3}{64}\kappa$ — and asserts AA and PP "are disposed of by leg (B) below, since $|G_{\rm PP}|=|G_{\rm scalar}|$ is equally sub-critical." But leg (B)'s ratio (`eq:ratio`, `:5116-5122`, worst case $0.156$) is evaluated with $|G_{\rm eff}|=\tfrac{3}{64}\kappa$; that number, and the committed script, never evaluate $G_{\rm AA}/G_{\rm crit}$. The justification given ("$|G_{\rm PP}|=|G_{\rm scalar}|$") explicitly covers only PP and is silent on AA. The AA worst-case ratio is actually $\approx 2\times0.156=0.31$ — still sub-critical, so the *conclusion is unchanged* — but as written the "belt-and-suspenders" magnitude leg does not demonstrate AA sub-criticality, and the v1U.0.16 changelog claim (`:58`, "attractive AA/PP channels ... excluded by magnitude leg (B)") overstates what leg (B) shows. Fix: state the AA worst-case ratio ($\approx 0.31$) explicitly, or add $G_{\rm AA}/G_{\rm crit}$ to the committed script's scan.

2. **[MINOR] Physically, AA/PP are not the dark-energy-relevant condensate — the sign leg on the scalar channel is already decisive** — `arxiv/paper1_unified.tex:2695-2699`, `:5106-5112`. The appendix sets out to exclude a chiral condensate $\langle\bar\psi\psi\rangle\neq0$ (a scalar $\sigma$-condensate), which leg (A) decisively kills via the repulsive scalar sign. An AA "condensate" $\langle\bar\psi\gamma^\mu\gamma_5\psi\rangle$ is a Lorentz-violating axial-vector vacuum, and PP is $\langle\bar\psi i\gamma_5\psi\rangle$ (parity-breaking); neither is the scalar condensate at issue nor sources a coherent $w=-1$ term. Noting this would make the exclusion airtight and remove the reliance (Issue 1) on a magnitude bound that does not quite cover AA. Presentation, not a correctness bug.

3. **[MINOR] Residual "far sub-critical" wording vs the tempered appendix** — abstract `:1236` and discussion `:4322` still read "far sub-critical," while the v1U.0.16 edit tempered the appendix (`:5126`, `:5131`) to "comfortably sub-critical" precisely because the worst scanned case ($0.156$) is only an order of magnitude below unity, not far below. The headline single-species/QCD-like values ($4.7\times10^{-3}$, $4.3\times10^{-2}$) do justify "far," so this is only a wording-consistency nit, but the two surfaces should use one phrasing to avoid a reviewer reading a $0.156$ worst case as "far."

Verified clean (no action): the NJL arithmetic (`eq:ratio` values, Holst $1/0.0698\approx14\times$) matches `njl_gap_equation_route1_results.json` and my hand recomputation; the $S_{abc}S^{abc}=-\tfrac38(J^5\!\cdot\!J^5)$ identity (`:1844`, `:1992`, `:4948`) is correct and now self-consistent across all three sites; the perturbation-transparency result (`sec:transparency`, εR vanishing on Levi-Civita by the first Bianchi identity) is standard and honestly scoped; the $e^{32}$ e-fold tension ($92-60$) is consistent. No fabrication detected; the title/abstract are honestly hedged to "channel-level, not operator-level."

**(3)** Yes — the central claim (channel-level amplitude closure of R1–R3, naturalness closure of R4, plus the perturbation-transparency result) is supported *within the paper's explicitly stated scope*, with only a minor completeness gap in the NJL AA-channel magnitude bookkeeping that does not alter any conclusion.
