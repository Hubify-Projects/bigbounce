# P1A R40conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1a_ech_nogo.pdf` md5=fd4707e3 pages=28
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 150.6s

---

Here is a referee report for the provided paper.

---
## Referee Report: P1A

**To the Editor of Physical Review D,**

This manuscript, "Channel-Level Closure of Four Minimal Einstein-Cartan-Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter," presents a systematic assessment of four potential channels through which Einstein-Cartan-Holst (ECH) gravity could source late-time dark energy. The author concludes that all four minimal channels are closed, either by amplitude suppression or by naturalness objections. A key secondary result is a "perturbation-transparency" theorem for canonical scalar matter in ECH, showing that its perturbation theory is identical to that of General Relativity.

The paper is ambitious, well-structured, and tackles a complex and relevant topic with a systematic, barrier-based approach. The author is often commendably transparent about the assumptions and ansätze underpinning the analysis. The two central results—the channel-level closure and the perturbation-transparency theorem—are potentially significant contributions to the literature on modified gravity and cosmology.

However, the manuscript suffers from several major issues that preclude its publication in Physical Review D in its current form. These include a critical dimensional inconsistency in the core dark-energy scaling ansatz, a flawed proof of the central perturbation-transparency theorem in the main text, and a heavy reliance on results from multiple companion papers that are not yet peer-reviewed, rendering the present work not self-contained.

I recommend **MAJOR REVISIONS**. The manuscript has the potential to be a valuable and impactful paper, but the essential and major issues detailed below must be thoroughly addressed.

---
### ESSENTIAL Revisions

**P1A-E1**
*   **Section:** Appendix B (p. 25), Figure 2 (p. 6)
*   **Problem:** There is a critical dimensional inconsistency in the core phenomenological scaling ansatz that underpins the entire dark-energy mapping. Equation (B2) on page 25 states: `ρ_bounce ~ (α/M) M_Pl^3 ~ 10^-2 M_Pl^4`. The coupling `α/M` has mass dimension `[M]^-1`. Therefore, the term `(α/M) M_Pl^3` has mass dimension `[M]^2`. This is equated to `10^-2 M_Pl^4`, which has mass dimension `[M]^4`. An energy density (`ρ`) must have dimension `[M]^4`. The equation as written is dimensionally incorrect and invalidates the subsequent numerical estimates for `N_tot`. While Figure 2 presents a dimensionally correct version (`ρ_vac ~ [(α/M) M_Pl] M_Pl^3`), this contradicts the explicit formula in Appendix B, which is the formal statement of the ansatz.
*   **Required Fix:** The author must resolve this dimensional inconsistency. If the intended formula is `ρ_bounce ~ [(α/M) M_Pl] M_Pl^3`, this must be stated clearly and used consistently throughout the manuscript, and Eq. (B2) must be corrected. The derivation of the required number of e-folds (`N_tot`) must be re-verified based on the corrected, dimensionally-sound formula. This is an essential fix as the dark-energy closure argument depends critically on it.

### MAJOR Revisions

**P1A-M1**
*   **Section:** X.B (p. 19), XV (p. 24)
*   **Problem:** The proof of the central "perturbation-transparency" result presented in the main text is incorrect. Step 4 of the proof (p. 19) claims that the Holst dual contraction `ε^μνρσ R_μνρσ` vanishes for a torsion-free connection due to the first (algebraic) Bianchi identity, `R_μ[νρσ] = 0`. This is not correct. The contraction of the Riemann tensor with the epsilon tensor is the Pontryagin density, which is a total derivative but is not identically zero pointwise. The author correctly notes in footnotes (e.g., footnote 7 on p. 20) that the actual reason for the vanishing is the Nieh-Yan identity, which shows the Holst term is equivalent to torsion-squared terms and a boundary term, all of which vanish when torsion `T=0`. The correct proof is relegated to a footnote while an incorrect one stands in the main text.
*   **Required Fix:** The proof in Section X.B must be replaced with the correct argument based on the Nieh-Yan identity (as outlined in footnote 7). All references to the "first Bianchi identity" as the reason for the vanishing of the Holst term (including in the abstract and conclusions) must be corrected.

**P1A-M2**
*   **Section:** Throughout (e.g., Abstract, Sec. III, Sec. IV, Table IV)
*   **Problem:** The manuscript is not self-contained and relies heavily on crucial results from at least four companion papers ([2], [6], [23], [46]) that are cited as "in preparation" or "posted concurrently." This includes: the primary evidence for the galaxy spin null result (Paper IV [23]), the MCMC-derived cosmological parameter values (Paper I(b) [6]), and the detailed forecast for the `f_NL` signature (Paper II [2]). A publication in a peer-reviewed journal cannot be contingent on unpublished work. Readers cannot verify the claims, and the results presented here lack the necessary foundation.
*   **Required Fix:** The author must make the paper self-contained. For each result imported from a companion paper, the author must either (a) include a summary of the methods and the derivation of the result within an appendix of the present manuscript, sufficient for a reader to understand and verify it, or (b) remove the quantitative claims that rely on the un-reviewed work and re-scope the paper's conclusions accordingly. Simply citing "in preparation" is not acceptable for load-bearing claims.

**P1A-M3**
*   **Section:** Abstract (p. 1), Table I footnote b (p. 4), Sec. VII footnote 6 (p. 15)
*   **Problem:** The quoted `2.6-5σ` realistic significance for the SPHEREx forecast of `f_NL = -35/8` is not derived or sufficiently explained. The footnotes provide values for `σ(f_NL)` (`≈ 0.7` ideal, `≈ 1.0` degraded) and the predicted value `f_NL = -4.375`. These numbers yield significances of `4.375/1.0 = 4.4σ` and `4.375/0.7 = 6.25σ`. The quoted range of `2.6-5σ` does not appear to follow from the information given and its origin is opaque.
*   **Required Fix:** Provide a clear, step-by-step derivation of the `2.6-5σ` range, explaining all inputs and systematic effects (e.g., GR projection, template overlap, photo-z degradation) that lead to this specific numerical window. If this derivation is in a companion paper, it must be summarized here per P1A-M2.

### MINOR Revisions

**P1A-m1**
*   **Section:** Title page (p. 1)
*   **Problem:** The paper is dated "June 13, 2026," which is a future date.
*   **Required Fix:** Correct the date to the actual submission date.

**P1A-m2**
*   **Section:** X, footnote 8 (p. 20)
*   **Problem:** The footnote contains the sentence: "An earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density." This is an internal review artifact and is not appropriate for a final publication.
*   **Required Fix:** Remove this sentence from the footnote.

**P1A-m3**
*   **Section:** Abstract (p. 1)
*   **Problem:** The abstract states: "...the SPHEREx forecast 2.6-5σ quoted above...". The quote does not appear "above" this sentence in the abstract. This is a dangling forward reference.
*   **Required Fix:** Rephrase to avoid the forward reference, or ensure the number is actually quoted earlier in the abstract.

### NITs (Typographical/Cosmetic)

**P1A-N1**
*   **Section:** XIV.D (p. 23)
*   **Problem:** Typo in the expression for physical scales: `k_phys^bounce ~ k_SPHEREx e^(N_tot-N_exit) ~ e^32 k_SPHEREx`. The text has `e^32 k_phys^SPHEREx`.
*   **Required Fix:** Correct `k_phys^SPHEREx` to `k_SPHEREx`.

---
## Summary recommendation

**MAJOR REVISIONS**

This manuscript presents a valuable and systematic investigation into ECH as a source for dark energy. The structural approach of identifying and closing specific physical channels is powerful, and the perturbation-transparency result is an elegant finding. However, the work is currently undermined by a critical dimensional error in its central scaling ansatz, a flawed proof of its key transparency theorem, and an unacceptable reliance on unpublished companion papers for its main observational touchstones. Once these foundational issues are thoroughly addressed, the paper could represent a significant and rigorous contribution to the field.