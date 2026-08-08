# INT Claude-subscription Review — P2 v1.7.113 — claude-opus-4-8
paper: P2  version: v1.7.113  tex: research/focused_paper_source_integration/02_full_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T15:03:00Z
context-note: FR1 fresh round on the July-11 restamped version (no content change since exit)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I have completed a full referee read and verified the load-bearing numbers against the committed artifacts (by exact hand-recomputation of every arithmetic reduction, and by reading the certification-script logic — direct Python execution was blocked by the sandbox, so I verified the transparent script structure plus the analytically tractable ε¹ piece rather than re-running sympy). My report follows.

---

**(1) VERDICT: MAJOR REVISIONS**

The manuscript is arithmetically clean and exceptionally transparent — I found *no* computational error, and every significance, Bayes-factor, and systematics-table value I recomputed matches to the quoted precision. The two MAJOR items below are not errors but concern whether the paper's two central claims are correctly *supported and headlined* to PRD standard.

**(2) ISSUES**

1. **[MAJOR] The "realistic" significance band headlines the more-favorable of two marginalized floors.** Abstract (`02_full_draft.tex:927`) and `sec:systematics` (`:1284`, tab:systematics caption `:1386`) quote the realistic post-systematic range as `1.3–2.75σ`, anchoring the lower bound on the ρ=−0.868 *proxy* floor (1.3σ) transferred from the power-spectrum SDB channel — while the paper's *own in-repo directly-computed* GR-projection shape overlap (ρ≈0.95, `c12_gr_projection_dBdAgr_probe.py`) gives `0.8σ` (`:1119`, `:1383`). The text itself calls ρ=−0.868 the "mild upper edge" and ρ≈0.95 the computed value, yet adopts the upper edge as the quoted endpoint and relegates 0.8σ to a "bracket." Verified: `2.1875×0.84/(0.7/√(1−0.868²)) = 1.30σ` vs `2.1875×0.84/(0.7/√(1−0.95²)) = 0.82σ`. This is a value-headlining concern (the project's own directive-F class): the honest realistic floor is plausibly sub-1σ, and the abstract's `1.3σ` "conservative floor" should not be the lower bound of the realistic band when the paper's best in-repo computation says 0.8σ.

2. **[MAJOR] The headline literature correction (−35/8 → −35/16) rests on the authors' own transcription of Cai et al.'s vertices.** In `app:convention` (`:1498`–`:1510`, `:1585`) the paper states that Cai's *published* −35/8 is reproduced by **neither** the exact vertex sum (→ −35/16) **nor** the transcribed printed polynomial (→ −305/64). The correction therefore depends entirely on the fidelity of the authors' transcription of Cai's four vertex expressions (Table tab:vertices) from the arXiv source, and the "independent" Li et al. cross-check is *formula-level only* (their Eq. 5.1) — the paper concedes Li's own printed polynomial *also* reduces to −305/64 (`:1510`, `:1585`). Correcting an 8-year-old published amplitude in PRD normally requires original-author acknowledgment or a fully independent third-party rederivation; the current certification, while internally self-consistent (I confirmed the ε¹ piece = −5/2, and that order-grouped, vertex-walk, and Li routes all sum to −35/16), is single-group. Strengthen with an external check or explicitly frame −35/16 as "our re-derivation, pending confirmation."

3. **[MINOR] The central testability claim leans optimistic for a ~1σ effect.** "SPHEREx can test this prediction" (`:1481`) and "will provide the first meaningful test" (`:1485`) describe a forecast whose honest marginalized significance is 0.8–1.3σ. This is caveated, but the conclusion's framing over-weights the pre-marginalization end.

4. **[MINOR] Every headline number is a recast of a single external forecast** (Heinrich et al. σ=0.7). The in-house independent Fisher (`c13`/`c14`) validates the recast but is explicitly *not* the headline source (`:936`, `:1119`); this leaves the result's evidentiary weight resting on one imported number, as the paper acknowledges.

5. **[MINOR] tab:gr BF-vs-SSFSR cell ("~27", `:1321`).** The closed form `exp[(35/16)²/(2σ_eff²)]` at σ_eff=0.860 gives 25.4, not 27 (I recompute 25.4). The column is labeled "order-of-magnitude only," so this is tolerable, but the cell is slightly high relative to its own stated formula.

6. **[MINOR] Length / caveat load.** ~30 pages, with the systematics/assumptions sections dominated by disclosure prose, is heavy for a literature-correction-plus-recast; consider consolidating for readability (editorial, not blocking).

**(3)** The literature correction to `fNL = −35/16` is well-supported (two independent formula-level derivations plus consistent internal cross-checks), but the paper's *observational* central claim — that SPHEREx can meaningfully test the matter bounce — is only marginally supported once the paper's own directly-computed GR-projection degeneracy (→0.8σ) is applied, so the forecast claim is honest but over-headlined rather than fully substantiated.

---

Note on process: I could not execute the sympy certification scripts (`p2_vertex_check.py`, `caili_certification/*.py`) — Python execution was denied by the sandbox — so the −35/16 vertex-sum squeezed limit is verified via script-logic inspection + the analytically tractable ε¹ term and all fraction reductions, not a full re-run. If you want machine-confirmed certification, approve a `python3 scripts/p2_vertex_check.py` run and I'll re-verify the degree-9 collapse directly.
