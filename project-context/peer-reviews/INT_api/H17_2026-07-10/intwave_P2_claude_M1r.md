I've now read the full manuscript (abstract, all nine sections, both appendices, and the vertex-certification tables). Here is my referee report, fresh to PRD standard.

---

## Referee Report — "Testing the Matter Bounce with Primordial Non-Gaussianity" (P2, v1.7.116)

**(1) VERDICT: MAJOR REVISIONS**

The science is correct and internally consistent — I found **no computational error** on a fresh read (I re-checked the vertex-sum fractions, the ε-order grouping, the −305/64 spurious-term arithmetic, the BF closed forms, the σ-quadrature rows, and the Planck/DESI recasts; all reconcile exactly). The −35/16 certification is genuinely solid. My MAJOR verdict is driven by presentation/length and significance-framing for the PRD venue, not by any error in the physics. The path to acceptance here is editorial and framing work, not re-derivation.

**(2) ISSUES**

1. **[MAJOR] Length and density exceed PRD norms even after the consolidation round.** The abstract (`02_full_draft.tex:975`) is a single ~330-word paragraph carrying ~10 distinct hedges; the Introduction "Scope and conventions" paragraph (`:984`) is a single ~600-word block; the independent-Fisher paragraph (`:1167`) and the Systematics up-front paragraph (`:1332`) are each 400–700-word single paragraphs. For the incremental scientific content (a recast of one external forecast + an arithmetic correction), this is well beyond PRD crispness expectations. Trimming to PRD standard is substantive rework, not a one-line fix — hence MAJOR.

2. **[MAJOR] Significance/venue: the entire quantitative forecast is a marginal, doubly single-sourced recast.** The headline sensitivity is ~1.3–2.75σ (dropping to ~0.8σ under the GR bracket), obtained by rescaling the single Heinrich et al. σ(f_NL)≈0.7 (`:1160`, `:1169`), whose per-triangle Cov_B is non-public (`:1332`). The "independent Fisher" validation (`:1167`) reproduces σ to 2–11% but uses the authors' own tree-level Gaussian covariance surrogate — so both the diagonal and off-diagonal rest on in-house surrogates. This is disclosed honestly (Caveat (vi)/single-source, `:1512`), but a fresh referee must weigh whether a sub-3σ (often ~1.3σ) recast of one number meets the PRD significance bar. Flagged as a genuine editorial concern the authors should address in framing.

3. **[MINOR] Residual overstatement in the "arithmetic error confined to Cai Eq. 37" framing.** Line `:1620` states definitively "It IS a genuine arithmetic error confined to Cai et al.'s last algebraic combination step (their Eq. 37)," yet the appendix itself admits (`:1556`, `:1618`) that the transcribed printed polynomial squeezed-reduces to a *third* value (−305/64), not to Cai's published −35/8, and "we do not claim a complete term-by-term reconstruction of Cai's published −35/8." The confident "arithmetic error confined to Eq. 37" language is in tension with the appendix's own hedge that the −35/8 cannot be reproduced. Reconcile: what is certified is −35/16; the −35/8 provenance is not pinned. The headline framing should match the appendix's honesty.

4. **[MINOR] Birefringence appendix (`app:birefringence`, `:1712`) is explicitly independent of every result** ("none of the headline f_NL forecasts of this paper depend on it"). Relegating it (directive-M) is an improvement over an in-body paragraph, but a fresh referee will ask why it is in the paper at all; consider cutting it entirely rather than carrying an outlook pointer (`:1521`) + appendix for a channel with no bearing on the manuscript's claims.

5. **[MINOR] Abstract compresses away the load-bearing conditional on assumption (d).** The abstract (`:975`) states (d) is "closed to a bounded δf_NL≲10⁻³ systematic via single-clock nonlinear ζ-conservation" but omits that this closure is conditional on the dressed-metric quantization and is "plausible but not derived" in the deformed-algebra scheme (`:1076`). Given this is repeatedly called the "load-bearing caveat," one clause noting the quantization-conditionality belongs in the abstract.

6. **[MINOR] Citation key/name mismatch may confuse a fresh reader.** The relativistic-projection references are keyed `Jolicoeur:2025` but named "Addis et al." throughout (`:1186`, `:1188`, `:1360`). This is internally justified (first author = Addis) but reads as an inconsistency on first encounter; a one-line note or a key rename would remove the friction.

**(3) Is the central claim supported?** Yes, conditionally: the matter-bounce prediction f_NL^local = −35/16 is convincingly certified four independent ways with committed, auditable scripts, and the claim that SPHEREx can test it at a *marginal* ~1.3–2.75σ is honestly supported as a disclosed single-source sensitivity recast — the science is sound; what needs work is presentation length/tone and the significance-framing for PRD.

---

Best Next Steps
- Route the two MINOR framing fixes (issues 3 and 5 — reconcile the "Eq. 37 arithmetic error" overstatement with the appendix hedge; add the quantization-conditional clause to the abstract) to a closure agent, since they are one-paragraph edits with zero number change.
- Log this verdict + raw report to `project-context/peer-reviews/` and update `site/src/data/reviewTimeline.ts` in the same bundle (per the standing review-round site-sync directive).
- Do NOT record this as ACCEPT — it is a genuine MAJOR (presentation + significance), and the grid must reflect that honestly.

Say `continue` and I will take the next best scoped step.
