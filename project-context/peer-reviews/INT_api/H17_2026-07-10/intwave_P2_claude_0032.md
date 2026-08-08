# INT Claude-subscription Review — P2 v1.7.115 — claude-opus-4-8
paper: P2  version: v1.7.115  tex: research/focused_paper_source_integration/02_full_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-12T07:32:15Z
context-note: wave on v1.7.115: c15 GR-leg space-mismatch bug fixed (S_GR x M123) — corrected rho=-0.42/-0.49, sigma_marg=2.32sigma, still above the retained 1.30sigma proxy floor; -35/16 unchanged

======================================================================
RAW RESPONSE (verbatim):
======================================================================

The vertex-certification agent has now independently re-derived **every** Appendix-A number by exact-fraction arithmetic and confirms all match: the four per-vertex squeezed contributions (−25/16, −5/32, 0, −15/32) sum to −35/16; equilateral sums to −255/128; the −(99/128)∑kᵢ³ discrepancy and the −305/64 reduction of the printed polynomial both check out; and Li's formula gives −35/16 at c_s=1. This independently corroborates my own hand-derivation of the spurious term.

So the −35/16 certification is now confirmed **two independent ways** (my hand-check of `cai_vertices.py` + the agent's full term-by-term re-derivation). This strengthens the correctness leg but does not move the verdict: the physics core is sound and all numbers reproduce, yet the paper still needs major revision for length/over-hedging, the in-house-Fisher reliability caveat, and the softened "resolution" framing.

**Final verdict stands: MAJOR REVISIONS.** The central claim is *arithmetically* supported but *scientifically* only weakly so — a ~1.3–2.75σ recast of a single external forecast, conditional on an unverified cubic-transmission assumption.

Best Next Steps
1. Compress the abstract (≤180 words) and cut the Scope paragraph + repeated −35/8 bookkeeping — top PRD-readiness blocker.
2. Add the c13/c14 r_eff reliability caveat referencing the c15 basis-bug correction.
3. Soften "resolves the 8-year discrepancy" → "confirms −35/16, identifies one spurious term; Cai's −35/8 not reproduced."
4. Run `/latex-audit` to clear the 3 overfull hboxes and refresh the stale `phase3` JSON version string.

Say `continue` and I will take the next best scoped step.
