# P4 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v136verify_P4_v1_0_136
**Wall time**: 149.4s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=104451, completion=15813, reasoning=14880, total=120264

---

## BLOCKER: Invalid Hard-Label Variance Derivation
**ID:** PAPER-GEM-B1
**Section:** §III.E, "Hard-label variance widening from the 21.4% argmax-flip rate"
**Issue:** The derivation $\sigma_{f_{\rm CW}} \to \sigma_{f_{\rm CW}} \sqrt{1 + p_{\rm flip}(1-p_{\rm flip})/[p(1-p)]}$ is mathematically invalid. By the Law of Total Variance, the variance of a binary label $x_{\rm obs} = x_{\rm true} \oplus f$ is exactly $p_{\rm obs}(1-p_{\rm obs}) \le 0.25$. Treating the flip noise as an additive continuous variance term that inflates the total variance beyond the binomial bound is a fundamental probability error. Furthermore, since the MC nulls shuffle the *observed* labels, their variance already exactly matches the observed binomial variance; multiplying MC sigmas by 1.21x artificially deflates significance.
**Fix:** Remove the algebraic derivation and the 1.29x/1.21x variance inflation factors entirely. The standard binomial variance $p_{\rm obs}(1-p_{\rm obs})/N$ fully captures the variance of the observed hard labels.

## MAJOR: Unformatted Run-On Block and Informal Prose
**ID:** PAPER-GEM-M1
**Section:** §IV.D, bullet point 2 ("MASTER decoupling removes...")
**Issue:** A massive ~1500-word run-on text block starting with "a dedicated canonical-mask injection sweep..." merges multiple distinct analyses without paragraph breaks. It starts several sentences with lowercase letters (e.g., "companion artifact...", "each of the three...") and contains informal internal-review prose (e.g., "live on the H200 pod backup and are not available locally", "the partial closure that IS executable").
**Fix:** Break this block into properly formatted paragraphs, fix the capitalization, and rewrite the informal internal-review prose into objective scientific language.

## minor: Incorrect EFT Operator Dimension
**ID:** PAPER-GEM-m1
**Section:** §VI.H, "(ii) Parity-odd galaxy-trispectrum amplitude"
**Issue:** The text states that $g_*$ parameterizes "dimension-7 operators in the EFT of Inflation". The leading parity-violating operator for the scalar trispectrum in the EFT of Inflation (Cabass et al. 2022) enters at dimension 8, not dimension 7.
**Fix:** Change "dimension-7 operators" to "dimension-8 operators".

## minor: Unformatted Editing Note in Main Text
**ID:** PAPER-GEM-m2
**Section:** §III.E, "Empirical bound on rotation-correlated CW-fraction excursion"
**Issue:** An unformatted editing note is left in the main text: `( scope restoration the mean-probability invariance ... hard-label D$_4$ closure is unperformed.)`.
**Fix:** Remove the "scope restoration" prefix and integrate the sentence properly, or delete the note entirely.

## minor: Missed Shamir Citation Update
**ID:** PAPER-GEM-m3
**Section:** §V.A, paragraph 1
**Issue:** The text cites `\cite{Shamir:2022}` (the PASJ methodology paper) for the 1.3 million DESI Legacy sample ("out of ~1.3 million total \cite{Shamir:2022}"), but it should cite `\cite{Shamir:2022DESI}` (the MNRAS DESI Legacy paper). The v1.0.134 changelog claimed to fix this, but this specific instance was missed.
**Fix:** Change `\cite{Shamir:2022}` to `\cite{Shamir:2022DESI}` in that sentence.

## nit: Stray Punctuation
**ID:** PAPER-GEM-n1
**Section:** §IV.D, "Direct cross-spectrum diagnostic for interpretation (ii)"
**Issue:** There is a stray parenthesis and comma: `anti-aligned (, not a global real-space`.
**Fix:** Remove the stray comma and space to read `anti-aligned (not a global real-space`.
