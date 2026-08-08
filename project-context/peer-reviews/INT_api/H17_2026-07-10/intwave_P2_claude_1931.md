# INT Claude-subscription Review — P2 v1.7.112 — claude-opus-4-8
paper: P2  version: v1.7.112  tex: research/focused_paper_source_integration/02_full_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T02:31:03Z
context-note: Wave-1 stability re-test at current version; no changes since last review

======================================================================
RAW RESPONSE (verbatim):
======================================================================

Verification is complete. The subagent confirmed (against committed JSON outputs + exact hand-arithmetic) that **every Fisher and Bayes-factor number the paper prints matches its committed artifact exactly**, and I independently hand-verified the vertex sums (−35/16, −255/128), Li's formula (−165/16+65/8=−35/16), the −305/64 spurious-term reduction, and the full BF/significance chain. The four sympy vertex scripts couldn't be *executed* (shell blocked this session), but their results are corroborated by hand-arithmetic and the committed `final_check`/JSON. No fabrication; no genuinely-new correctness finding.

---

**(1) VERDICT: MAJOR REVISIONS**

The verdict is driven entirely by presentation and scope/novelty. On scientific-correctness grounds the manuscript is clean and stable: the central value is certified by multiple independent routes, no printed number diverges from its committed artifact, the compile is clean (0 undefined refs), the served PDF is current (v1.7.112, July 10), and nothing is overclaimed. A real PRD referee would nonetheless return it for substantial rework before acceptance, for the reasons below.

**(2) ISSUES**

1. **[MAJOR] Excessive length and repetitive, defensive register.** The manuscript restates the same handful of caveats many times over — the "r vs r_eff" reconciliation appears at `02_full_draft.tex:935`, `:1054`, `:1060`, `:1118`, and `:1463(iv)`; the "recast, not an independent forecast" disclaimer at `:935`, `:1120`, `:1463(i)`, `:1480`; the "additive-quadrature is a heuristic, not a joint Fisher" caveat at `:1283`, `:1353`, `:1360`, `:1385`, `:1463(v)`. The 330-word single-paragraph abstract (`:926`) and the ~40-page body read as accreted referee-response residue. A PRD referee would require compressing to roughly half length and converting the rebuttal-style prose to declarative exposition.

2. **[MAJOR] Thin novelty for PRD; headline is a single-source recast.** Every headline significance rescales one external forecast (Heinrich et al., `:1120`, `:1463` "Single-source limitation"). The in-house Fisher (`c13`/`c14`) that would establish independence is itself heavily caveated — tree-level, Gaussian covariance, `b2/bs2` held fixed, single proxy correlation (`:1118`, JSON `limitations` block). The durable new contribution is really the Appendix-A −35/16 correction; the editor should be told plainly whether a single-forecast sensitivity recast clears the significance bar, and the framing should foreground the theory result over the recast.

3. **[MINOR] Title/abstract "Resolution of the Cai–Li factor of two" is stronger than what is shown.** The transcribed printed Cai polynomial squeezed-reduces to −305/64 (`:1509`, `:1584`), which is neither the correct −35/16 nor Cai's stated −35/8 (−280/64); the paper cannot reproduce Cai's −35/8 from his printed coefficients and honestly labels it "an unreproduced erroneous literature value." That is the correct disposition, but the *title* (`:27`) and abstract (`:926`) claim to *resolve* Cai's specific error, whereas the demonstrated result is only that −35/16 is independently certified and differs from Cai's number. Soften the title's "Resolution" framing to match the appendix's careful wording.

4. **[MINOR] Headline conservative floor rests on a proxy correlation, not a channel-native one.** The 1.3σ (and 0.8σ) endpoints use ρ=−0.868 transferred from the power-spectrum SDB channel because the Heinrich per-triangle Cov_B is not public (`:1283`, `tab:systematics` last two rows `:1381`–`:1382`). This is disclosed thoroughly, but it means the quoted conservative significance is not derived from the bispectrum channel it describes; the abstract should carry that qualifier as prominently as it carries the 1.3σ number (it currently does, at `:926`, which is good — keep it).

5. **[MINOR] Three overfull hboxes** (2.5pt, 10.3pt, 1.2pt) at `02_full_draft.log:427/1081/1119`, the largest in the vertex-contribution table `tab:vertices` (`:1516`–`:1524`). Cosmetic, but worth clearing before camera-ready.

**(3)** The central claim — that the corrected matter-bounce prediction f_NL^local = −35/16 is well-certified and testable by SPHEREx at a realistic, marginal ~1.3–2.75σ that is honestly bounded and not overstated — **is supported** by the manuscript and its committed artifacts; the remaining objections are presentation and scope, not correctness.
