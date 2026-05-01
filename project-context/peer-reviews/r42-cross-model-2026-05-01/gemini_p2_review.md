---
model: gemini-3.1-pro-preview
paper: p2
paper_title: f_NL Forecast (Paper 2)
pdf_path: /Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf
date: 2026-05-01
prompt_tokens: 8096
completion_tokens: 2332
total_tokens: 13786
review_type: cross-model adversarial peer review
reviewer: Google Gemini (cross-model check vs Anthropic Claude pipeline)
---

## Summary verdict
REJECT. The manuscript is a trivial algebraic recast of a published forecast (Heinrich et al. 2023) masquerading as a novel analysis, and the author's provided context claims the existence of a data pipeline and QSO sample (5,384 candidates, Landy-Szalay estimators) that are entirely absent from the submitted PDF.

## BLOCKERS (paper cannot ship as-is)

- **B-1: Complete disconnect between claimed context and actual PDF content**
- Section / equation / figure citation: Entire manuscript vs. Author Context
- Defect: The author's provided context claims this paper contains a Fisher forecast yielding $\sigma(f_{NL})$ from 16.85 down to 11.71, and a "Pipeline 1" analysis of 5,384 QSO candidates using Landy-Szalay estimators. Absolutely none of this exists in the PDF. The PDF is entirely a literature recast adopting $\sigma(f_{NL}) = 0.7$ from Heinrich et al. 2023 (Sec. IV). 
- What would fix it: Submit the actual paper you are describing. If this PDF is the intended paper, remove all claims of novel data pipelines and QSO clustering analysis, as they are fabricated.

- **B-2: Mathematically invalid bispectrum template projection**
- Section / equation / figure citation: Sec. III.B, Eq. 4 and Eq. 5
- Defect: You cannot apply a primordial shape overlap factor $r$ (calculated via simple $k$-space integrals) multiplicatively to a multi-tracer galaxy bispectrum forecast $\sigma(f_{NL})$. The galaxy bispectrum covariance matrix includes non-linear bias ($b_2, b_{s^2}$), redshift-space distortions, and tracer-specific shot noise. The template projection does not commute with the Fisher matrix inversion. Your "noise-weighted" $r \approx 0.83$ is a toy approximation that completely ignores the actual covariance structure of the Heinrich et al. multi-tracer analysis.
- What would fix it: You must compute the Fisher matrix from scratch using the exact matter-bounce shape function inside the full galaxy bispectrum covariance, including all marginalizations over $b_1, b_2$, and shot noise.

- **B-3: Fundamental misunderstanding of "convention" vs. "physics error"**
- Section / equation / figure citation: Appendix A, Table IV
- Defect: You claim the factor of 2 discrepancy between Cai et al. ($-35/8$) and Li & Brandenberger ($-35/16$) is a "convention difference." It is not. You explicitly show in Appendix A.1 that Li & Brandenberger omitted the second time-ordering in the in-in commutator. Omitting a time-ordering in quantum field theory is a mathematical error that changes the physical expectation value of the observable by a factor of 2. It is not a "dual-normalization" choice.
- What would fix it: Stop calling this a convention. State clearly that Li & Brandenberger's calculation is incomplete/incorrect due to the missing commutator term. Remove Table IV, which legitimizes a physics error as a valid alternative hypothesis.

## MAJOR concerns (must address before resubmission)

- **M-1: Artificially inflated Bayes factors via delta-function priors**
- Section / equation / figure citation: Sec. VI.C, Eq. 6, Table II
- Defect: You use a delta-function prior for the bounce model's $f_{NL}$ while using a broad uniform prior for inflation. This mathematically guarantees a massive Bayes factor in favor of the bounce if the data lands near the prediction. You admit the bounce prediction has a 1-8% $\epsilon$-correction uncertainty (Sec. II.C) and polynomial ambiguity. A delta-function prior is therefore physically unjustified and highly misleading.
- What would fix it: The baseline Bayes factor must be calculated using a prior width that reflects the actual theoretical uncertainty of the bounce model (at least $\sigma_{theory} = 1.0$, as you briefly mention but relegate to a caveat). Update the abstract and Table II to reflect this realistic prior, not the $10^5$ fantasy number.

- **M-2: False claim of $b_\phi$ independence in the bispectrum**
- Section / equation / figure citation: Sec. VII.B, Fig. 5 caption
- Defect: You claim the SPHEREx bispectrum constraint is "nearly independent of $b_\phi$". This is false. Primordial non-Gaussianity enters the tree-level galaxy bispectrum not just through the primordial shape $B_\zeta$, but through cross-terms involving the scale-dependent linear bias $\Delta b(k) \propto f_{NL} b_\phi$. Marginalizing over $b_\phi$ absolutely degrades bispectrum constraints.
- What would fix it: Remove the claim that the bispectrum is independent of $b_\phi$. If you are relying on Heinrich et al., state explicitly how they handled $b_\phi$ (they likely fixed it via universality), and acknowledge that relaxing this would severely degrade your recasted 5.25$\sigma$ headline.

## MINOR concerns (should fix, won't block)

- **m-1: Over-reliance on MegaMapper**
- Section / equation / figure citation: Sec. V, Fig. 2
- Defect: MegaMapper is an unfunded concept. Dedicating a full section and half your plots to it dilutes the paper's focus on near-term, realistic SPHEREx constraints.
- What would fix it: Condense Sec. V to a single paragraph in the Discussion.

- **m-2: Irrelevant shot-noise caveat**
- Section / equation / figure citation: Sec. IV, "Shot-noise caveat" paragraph
- Defect: You discuss shot noise degradation for "anomaly-selected tracers," but you never actually forecast anomaly-selected tracers in this paper (despite what your provided context claimed).
- What would fix it: Delete the paragraph. It belongs in the paper you described in your context, not this one.

## Statistics / methodology audit
*   **Is the chosen statistic the right one?** No. The Bayes factor is manipulated via an asymmetric prior choice (delta function vs. broad uniform).
*   **Are error bars consistent?** No. You mix frequentist Fisher forecasts (Heinrich et al.) with Bayesian model selection, treating the Fisher $\sigma$ as the width of a Bayesian likelihood without formally justifying the mapping.
*   **Are look-elsewhere corrections applied?** N/A for a forecast.
*   **Are MCMC convergence diagnostics reported?** You claim "> 6x10^5 Monte Carlo realizations" (Sec. VI.C), but this is a gross misuse of terminology. You are just drawing random numbers to evaluate an analytic formula (Eq. 6). This is not an MCMC sampling a posterior, and calling it "Monte Carlo discovery" is highly misleading.
*   **Are systematic uncertainties quantified?** Hand-waved. The GR degradation ($\sigma_{GR}$) is just a dial turned by hand (0.5 to 1.0) rather than a rigorous calculation of relativistic projection effects on the specific matter-bounce shape.
*   **Are claimed detection significances reproducible?** Yes, because they are trivial arithmetic ($4.375 \times 0.84 / 0.7 = 5.25$), not the result of an actual pipeline.

## Cosmology / physics sanity check
*   The $f_{NL} = -35/8$ prediction relies heavily on exact matter domination ($w=0$). The quasi-dust model has $w=-0.003$, which you claim introduces a 1-8% correction. This correction is large enough to shift the central value by $\sim 0.35$, which is half of your SPHEREx $1\sigma$ error bar. Treating the prediction as a delta function at exactly $-4.375$ is physically inconsistent with your own text.
*   The consistency relation (Eq. 8) gives bounds $c \in [-0.7, -10]$. This is an order-of-magnitude uncertainty on the slope. Calling this a "single-parameter curve" is a stretch when the parameter spans an order of magnitude.

## Reproducibility
*   **Are data products/code published?** A GitHub link is provided, but it only contains simple scripts for template overlap and analytic Bayes factors, not the Fisher matrix or QSO pipeline claimed in the context.
*   **Could a grad student reproduce the numbers?** Yes, using a pocket calculator.
*   **Are software versions pinned?** Yes (v1.7.0 tag).

## What an Anthropic-Claude review would have missed
*   **The Context/PDF Hallucination:** Claude's sycophancy often leads it to accept the user's prompt as ground truth. It would likely have praised your "innovative use of 5,384 QSO candidates" without noticing that the actual PDF contains zero data analysis and is just a literature recast.
*   **The Fisher Projection Fallacy:** Claude lacks the domain-specific intuition to realize that $r = \langle B_{bounce} \rangle / B_{squeezed}$ computed via simple $k$-space integrals cannot be multiplicatively applied to a multi-tracer galaxy bispectrum $\sigma(f_{NL})$. It would accept Eq. 4 as standard practice.
*   **The "Convention" Apologetics:** Claude is trained to be polite and mediate disputes. It would likely agree with your diplomatic framing in Appendix A that Li & Brandenberger vs. Cai et al. is a "convention difference," missing the hard physics reality that omitting a time-ordering in an in-in calculation is a fatal error, not a choice of normalization.
*   **Pseudo-MCMC:** Claude would praise your "robust 600,000 Monte Carlo realizations" without recognizing that you are just doing trivial random sampling of an analytic formula, not actual cosmological parameter inference.

## Bottom line for the author
You have submitted a paper that is fundamentally different from the one you described in your context prompt. If you want to publish a paper about 5,384 anomaly-detected QSOs and Landy-Szalay estimators, you need to actually put that analysis into the PDF. As it stands, this manuscript is a trivial algebraic recast of Heinrich et al. 2023. The single highest-leverage fix is to abandon the mathematically invalid $r$-factor approximation (Eq. 4) and write a real Fisher matrix code that evaluates the exact matter-bounce shape function against the full multi-tracer galaxy bispectrum covariance.
