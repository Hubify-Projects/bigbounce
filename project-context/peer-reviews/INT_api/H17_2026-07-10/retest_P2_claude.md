Agents are done. I have everything needed to referee. Here is my report.

---

## Referee Report — Paper P2 (v1.7.109), `02_full_draft.tex`

**Verification method note:** Python/sympy execution was permission-blocked this entire session (for me and delegated subagents alike), so the four flagged closures were verified by (a) reading the committed artifact JSONs directly, (b) reading the certification-script *source*, and (c) hand-arithmetic on the per-vertex table and BF chain — not by live re-execution. Every numeric cross-check below passed.

### (1) VERDICT: **MINOR REVISIONS**

The four claimed closures all landed coherently. Remaining items are minor (one sign-gloss in the abstract, one number that disagrees with its own committed script, provenance-annotation staleness). None are blocking.

### (2) ISSUES

**Confirmation the closures landed (not issues):**
- *Spurious-term sign* — Eq. (spurious) `02_full_draft.tex:1455` states `A_T − Σ(vertices) = −(99/128)Σkᵢ³`, and the parenthetical correctly notes `cai_vertices.py` computes the negative, `Σ − A_T = +(99/128)Σkᵢ³` (self-consistent). Arithmetic chain checks: `−35/16 − (10/3)(99/128) = −2.1875 − 2.578 = −4.7656 = −305/64` ✓. Per-vertex table `tab:vertexwalk:1490-1494` sums to `−35/16` squeezed (`−25/16−5/32+0−15/32 = −70/32`) and `−255/128` equilateral ✓. Framing is honest: `−35/8` is stated as *not reproduced by the transcribed coefficients* and retained only as an erroneous literature value.
- *SSFSR Bayes recompute* — `tab:gr:1268-1271` values (`1.4×10²/27/5`, tuned `5.7/4.6/3.3`, `P(BF>3) 88.8/80.2/61.5%`) match `outputs/c9g_bf_table_recompute.json` `scans` block **exactly** at σ_eff = 0.700/0.860/1.221. Continuous-marg SSFSR `≈19` matches `c9k` (`1.939e+01`). `tab:bayes` SSFSR column `~5–1.4×10²` consistent. ✓
- *FoG wording* — `02_full_draft.tex:1067` now reads "omitting it is therefore **optimistic, not conservative, for the absolute significance** … largely cancels in the recovery ratio r_eff." Correct. ✓
- *Envelope subordination* — abstract headlines the single central Fisher result (`2.6–2.75σ` / `1.3–2.75σ`); the independent Fisher `r_eff≈0.99` is explicitly "validation, not … the headline range," SDB is "subordinate cross-check," MegaMapper "illustrative envelope." ✓

**Issues requiring revision:**

1. **[MINOR]** Abstract sign-gloss, `02_full_draft.tex:867`. The abstract says "the transcribed printed polynomial **exceeds** the vertex sum **by this amount**" where "this amount" = `−(99/128)Σkᵢ³` (a negative quantity). "Exceeds by a negative amount" literally means "is less than," contradicting the sign it quotes (and `A_T` is indeed the *more negative* one → `−305/64`). Eq. (spurious) and the script are internally consistent; only this verbal gloss is garbled. Reword to "differs from the vertex sum by" or "the vertex sum exceeds the printed polynomial by (99/128)Σkᵢ³."

2. **[MINOR]** Committed-artifact number mismatch, `02_full_draft.tex:1258`. Text states the continuous-σ_GR marginalization "gives **BF ≈ 4.8** vs. the tuned narrow competitor," but the cited `outputs/c9k_gr_continuous_marginalization.json` reports `continuous_marginal.BF_vs_tuned_narrow = 4.615` (≈4.6). The SSFSR ≈19 in the same sentence matches (19.4); the 4.8 does not reproduce from its own artifact. Reconcile to 4.6 (or re-run and update).

3. **[MINOR]** Stale provenance metadata in the recompute artifacts. (a) `c9k_gr_continuous_marginalization.json` `"conventions"` field still says *"evaluated at central mock detection fhat = −35/8,"* though every value in the file is at −35/16 (`1.412e+02`, not the −35/8-era `3.5×10⁸`). (b) `c9g_bf_table_recompute.json` retains a top-level `table_iii_claims` block with the superseded, self-admittedly non-reproducible values (`bf_vs_ssfsr 3.3e6`, `bf_vs_tuned 10.9`, `p_gt3 0.98`) that contradict the paper's `tab:gr`; only the `scans` block is authoritative. A reproducibility reviewer opening these files hits contradictory metadata. Update the annotation strings / drop or clearly quarantine the legacy block.

4. **[MINOR]** Superseded `−35/8` SSFSR reference values are slightly off. `tab:gr` caption `02_full_draft.tex:1274` quotes the discarded `−35/8` figures as `3.5×10⁸/4.5×10⁵/6.4×10²`; `exp[(35/8)²/(2·0.7²)] ≈ 3.0×10⁸`, so the first is ~15% high. These are explicitly "order-of-magnitude only" discarded references, so tolerable, but tighten if retained.

### (3) Central-claim support

The central claim — corrected `f_NL^local = −35/16`, SPHEREx sensitivity `1.3–2.75σ`, `BF ≈ 9–14` — **is supported and honestly scoped**: the −35/16 correction is certified four independent ways with the `−35/8` explicitly demoted to erroneous-literature status, and every headline number I could cross-check matches its committed artifact; the paper is careful to present this as a modest-significance sensitivity *recast*, not a discovery-level independent forecast.

**Best Next Steps**
1. Fix the abstract "exceeds … by [negative]" sign-gloss (Issue 1) — one-line reword.
2. Reconcile the `4.8` vs committed `4.615` continuous-marg BF (Issue 2).
3. Refresh the stale `c9k`/`c9g` JSON metadata + legacy block (Issue 3).
4. Re-run `/latex-audit` + `/artifact-link-verify` after the edits, then directive-G re-mirror.

Say `continue` and I will take the next best scoped step.
