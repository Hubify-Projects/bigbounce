# EXT10 Harvest — P2 — ChatGPT
- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5f2-5e8c-83e8-9318-b7aefa847ee0
- PDF md5: 406af9f8
- Harvested: 2026-06-13 15:16 PDT

---

## Referee report — MNRAS / PRD / JCAP style

**Manuscript:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook, v1.7.62.

---

**Recommendation: MINOR REVISIONS**

The paper is publishable after targeted revisions. I do not see a remaining publication-blocking scientific error. The central framing has been substantially tightened: the matter-bounce prediction is now explicitly conditional, the SPHEREx result is described as a sensitivity recast rather than an independent Fisher forecast, and the Bayes factors are presented as illustrative and prior-dependent. The remaining issues are mostly clarity, consistency, and ensuring that a reader cannot overinterpret the headline 2.6–5σ and BF numbers.

---

**BLOCKERS — must fix before publication**

None.

I do not find a blocker requiring rejection or major scientific reconstruction. In particular:
- The use of f_NL^local = −35/8 is anchored in Cai et al.; the original paper explicitly gives the local/squeezed amplitude as −35/8 and notes that the shape is only "loosely local."
- The Heinrich et al. SPHEREx anchor is real and appropriate for a recast.
- SPHEREx mission status is not an issue: NASA lists SPHEREx as launched on March 11, 2025, with a planned two-year all-sky spectral survey.

---

**MAJORS — should fix**

**1. Clarify whether the null-space amplitude scatter is included in the quoted 2.6–5σ headline**
Location: Abstract p. 1 lines 41–49; Sec. II p. 4–5; Table IV p. 19.
Issue: The abstract says the realistic range includes "polynomial-null-space scatter ±0.13 in r" and that systematics are combined in quadrature. However, Table IV treats the null-space scatter as "distributional," not as a cumulative denominator. The paper already partly explains this distinction, but the abstract and Table IV could still be read as saying that the null-space scatter is already folded into the 2.6σ lower bound.
Proposed fix: Change the abstract wording to something like: "GR, b_ϕ, photo-z, and related denominator-level effects are combined in quadrature; the coefficient-null-space spread is reported separately as a distributional uncertainty in r, not included in the 2.6σ floor."

**2. Strengthen or soften the Cai/Li factor-of-two claim**
Location: Abstract p. 1 lines 25–28; Sec. II C p. 6–7; Appendix A p. 23–27, Table V.
Issue: The claim that Li et al.'s −35/16 is a "single-time-ordering intermediate" and "not a physical alternative" is a strong claim about a published calculation. Table V shows that the difference halves the significance.
Proposed fix: Add a compact table mapping: Cai equation / Li equation / local-template convention / factor applied / resulting f_NL. If this mapping is not fully reproducible from printed equations, change "Li is a single-time-ordering intermediate, not a physical branch" to "we adopt the Cai/Planck normalization; the Li-normalized value is treated as a stress-test branch and is not used in the headline."

**3. Make the exact bispectrum shape used for r=0.84 maximally reproducible**
Location: Sec. II A p. 3–5; Sec. III B p. 7–9; Data and Code Availability p. 23.
Issue: The paper says Cai et al.'s printed coefficients are not directly transplantable into the manuscript's symmetrized basis and that the working coefficients are fixed by three benchmark configurations. A reader should be able to see exactly why that reference shape is the correct physical shape.
Proposed fix: Add either an explicit coefficient-map appendix or a short "forecast shape definition" box that states the exact polynomial coefficients used for the central r=0.84, how they are obtained from Cai et al. or from the released artifact, and which part of the result is benchmark-fixed vs representation/null-space uncertainty.

**4. Resolve the σ(f_NL)≃0.36/0.93 inconsistency if it exists in the source manuscript**
Location: PDF p. 1 lines 37–50, Sec. IV p. 9–10, Table IV p. 19.
Issue: The PDF reviewed does not contain a headline σ(f_NL)≃0.36 Fisher or ≃0.93 conservative claim. The PDF uses Heinrich's σ=0.7 bispectrum-only anchor. If the .tex source or abstract elsewhere still contains σ≃0.36/0.93, remove or reconcile those numbers.

---

**MINORS — polish**

1. Replace residual "parameter-free" language with "minimally parameterized" wherever possible (Abstract p. 1; Introduction p. 2; Conclusion p. 22–23).
2. Move the 2D CMB-style injection/recovery validation out of the main evidentiary chain; call it a "toy Fisher-space amplitude-recovery check" in the abstract or move the detailed description to an appendix.
3. Figure readability: enlarge fonts, simplify legends, consider splitting Fig. 2 into SPHEREx-only and MegaMapper-only panels.
4. Float placement of Table V: force Table V to appear before the bibliography or move it into the appendix.
5. Add one-sentence summary near the start of Sec. IV: "The headline 2.6–5σ SPHEREx result is the multi-tracer bispectrum recast; the SDB and joint-running Fisher calculations are secondary cross-checks."
6. Tighten the cosmic-birefringence paragraph (Sec. IX E p. 22); move it to a footnote or delete unless the target journal welcomes speculative consistency comments.

---

**Strengths**

- The manuscript is unusually transparent about scope: it repeatedly states that the result is a sensitivity recast, not an independent SPHEREx Fisher forecast.
- The f_NL = −35/8 claim is now properly conditional on the scalar-only, no-prolonged-post-bounce-inflation, faithful-cubic-transfer matter-bounce class.
- The external Heinrich et al. anchor is correctly identified and used: the bispectrum-only σ(f_NL)≃0.7 and power-spectrum-combined ≃0.5 figures match the published forecast.
- The paper gives a valuable template-mismatch analysis rather than naively equating the matter-bounce bispectrum with the local template.
- The systematic budget is consolidated in Table IV, which makes the optimistic, realistic, and conservative endpoints auditable.
- The Bayes-factor section is better calibrated than many forecast papers: it states the prior dependence, reports narrow and broad competitor priors, and does not claim definitive model selection.

---

**Specific scrutiny requested**

**f_NL = −35/8 = −4.375:** The paper's present formulation is acceptable provided it stays conditional. The manuscript correctly narrows the claim to assumptions (a)–(f) and should not say or imply "mechanism-independent across all matter-bounce variants." The current draft mostly avoids that; the remaining edits are wording-level.

**SPHEREx forecast and 2.6–5σ:** The printed PDF's arithmetic is internally consistent: 4.375×0.84/0.7 ≃ 5.25σ, and the all-combined conservative endpoint matches Table IV. The only required fix is clarity about whether the null-space r-scatter is separate or included in the lower endpoint.

**Heinrich+2023/2024 anchor:** This is handled well. The manuscript explicitly adopts Heinrich et al.'s local-template SPHEREx bispectrum forecast and degrades it by template mismatch rather than recomputing the full SPHEREx Fisher matrix. The external source supports the σ=0.7 bispectrum-only and σ=0.5 combined target values.

**Continuous-GR-recovery marginalization and calibration 15%→23%:** The PDF reflects the corrected calibration: p. 16 states that σ_GR=0.5 gives σ_eff/0.7 = 0.860/0.700 ≃ 1.23, i.e. a ~23% inflation, not ~15%. The continuous marginalization result BF=6.0 against the tuned narrow competitor is also presented consistently. No fix needed beyond perhaps making the table caption slightly shorter.
