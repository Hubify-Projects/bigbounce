# P2 RB-INT — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5503a196 pages=29
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 208.4s

---

## Referee Report: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook

This paper presents a detailed sensitivity forecast for testing the matter-bounce cosmological scenario using upcoming data from the SPHEREx survey. The primary observable is the local-type primordial non-Gaussianity parameter, `f_NL`, for which the scalar-only matter-bounce class of models predicts a specific value of `f_NL = -35/8`. The work is framed as a "sensitivity recast" of a published SPHEREx bispectrum forecast by Heinrich et al. (2024), but it includes several significant original contributions that go well beyond a simple application of a new signal amplitude. These include a thorough resolution of a factor-of-two discrepancy in the theoretical literature, a detailed analysis of the template mismatch between the bounce and local shapes, a comprehensive and transparent systematic budget, a new joint forecast for `(f_NL, n_fNL)` from the scale-dependent bias channel, and a robust Bayesian model comparison.

The paper is exceptionally well-written, theoretically sound, and observationally rigorous. The authors demonstrate a deep command of the subject matter, from the subtleties of the in-in formalism to the practical challenges of large-scale structure analysis. The clear separation of different analysis channels, the explicit statement of assumptions, and the transparent, heuristic nature of the systematic budget are all commendable. The provision of detailed, reproducible code and data artifacts meets the highest standards of modern scientific practice.

The analysis finds that SPHEREx can test the matter-bounce prediction at a significance of `~2.6-5.5σ`, where the range represents a sensitivity envelope spanning from a conservative, all-systematics-included scenario to an optimistic, systematics-free baseline. The paper correctly identifies the bispectrum as a more robust channel than the scale-dependent bias due to its resilience to systematics like photometric redshift outliers and uncertainties in the PNG bias parameter `b_phi`. The Bayesian analysis finds that a SPHEREx detection would favor the bounce model over tuned multifield inflationary alternatives with a Bayes factor of `BF ≈ 9-14`, providing a quantitative measure of the model's discriminatory power.

The paper is of a quality suitable for publication in Physical Review D. I have only a few minor suggestions for improvement.

### Findings

#### MINOR

**P2-M1: Section I, Page 2 — Clarification of "mechanism-independent" terminology**
*   **Problem:** The paper correctly re-scopes the term "mechanism-independent" to mean UV-completion independence *within a restricted bounce class* and conditional on faithful cubic-order transfer. This is an important clarification of language used in earlier literature. However, the sentence "The term 'mechanism-independent' as it appears in earlier matter-bounce literature refers to UV-completion independence..." could be slightly strengthened to more explicitly state that the earlier, stronger usage was imprecise and that this paper's usage is the more technically correct one.
*   **Fix:** Consider a minor rephrasing, for example: "We note that the term 'mechanism-independent' as it appears in some earlier matter-bounce literature should be interpreted as UV-completion independence within the restricted bounce class defined here (assumptions (a)-(f), Sec. IIC), and is conditional on faithful cubic-order bispectrum transmission through the bounce (assumption (d)). It does not imply genuine model independence across the full landscape of bounce cosmologies." This makes the clarification even more direct.

**P2-M2: Section VII, Page 16 — Presentation of the SDB `(f_NL, n_fNL)` result**
*   **Problem:** The paper presents a new and significant result regarding the `f_NL-n_fNL` degeneracy in the SDB channel, finding a `4.6x` degradation when biases are marginalized. This result is important enough that it could almost be its own short paper. While the authors correctly subordinate it to the main bispectrum forecast, the motivation for its inclusion could be stated more directly at the beginning of the paragraph.
*   **Fix:** Add a sentence at the start of the second paragraph of Sec. VII to frame the analysis. For example: "To assess the robustness of constraints against scale-dependence, which provides another potential discriminator between bounce and inflationary models, we performed a dedicated joint Fisher analysis for `(f_NL, n_fNL)` in the SDB channel. While the bispectrum is the more sensitive channel for the `f_NL` amplitude alone, the SDB channel is the primary probe of the running `n_fNL`. We find that the strong degeneracy between the two parameters..." This helps contextualize why this separate, new calculation is being presented.

#### NIT

**P2-N1: Section I, Page 2 — Author email address**
*   **Problem:** The corresponding author's email address, `houston@hubify.com`, uses a non-institutional, commercial-sounding domain. While not a formal error, it is unconventional for an academic publication and may raise questions for some readers.
*   **Fix:** No action is required if this is the author's stable, preferred contact address. This is merely an observation.

**P2-N2: Section IV, Page 10 — Typo in `δσ/σ` scaling**
*   **Problem:** The text states: "The propagated fractional shift in `σ(f_NL)` follows from `δσ/σ ~ 1/2 δC/C` and is therefore `≤ 5×10^-4`...".
*   **Fix:** The factor of `1/2` is correct as `σ` is related to the square root of the Fisher matrix (inverse of covariance `C`). The text is correct as written. Retracting this point upon re-reading. No fix needed.

**P2-N3: Section IX.D, Page 23 — Minor phrasing**
*   **Problem:** The sentence "The two channels use distinct Fisher matrices, distinct survey samples, and distinct sufficient statistics; they are complementary rather than competing." is slightly repetitive with the word "distinct".
*   **Fix:** Consider rephrasing slightly for style, e.g., "The two channels are complementary rather than competing, as they rely on different Fisher matrices, survey samples, and sufficient statistics."

---

## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an excellent paper that provides a definitive forecast for testing the matter-bounce scenario with SPHEREx. It is thorough, rigorous, and transparent. The original contributions—including the resolution of the Cai/Li discrepancy, the null-space and systematic analyses, and the new SDB joint forecast—are significant and of high quality. The paper is a model of how a sensitivity recast should be performed, adding substantial value beyond the original forecast. After addressing the minor points above, the manuscript will be ready for publication.