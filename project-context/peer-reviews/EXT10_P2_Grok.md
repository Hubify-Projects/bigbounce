# EXT10 Harvest — P2 — Grok
- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=1d8e1fbc-6a0e-4917-b1a5-cf389b307141
- PDF md5: 406af9f8
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report for MNRAS (or equiv. PRD/JCAP)

**Manuscript:** Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook (v1.7.62, 25 pp., dated 13 June 2026)

---

**Recommendation: MINOR REVISIONS**

The manuscript is a meticulously executed, reproducible sensitivity recast that materially advances the literature on bounce-cosmology discriminants. It delivers (i) a source-to-source audit fixing the Cai et al. normalization, (ii) a transparent template-overlap + null-space quantification with committed code artifacts, (iii) a headline 5.2–5.5σ (optimistic) / 2.6–5σ (realistic post-budget) SPHEREx forecast anchored squarely on the published Heinrich et al. bispectrum pipeline, and (iv) a closed-form + MC-validated Bayesian comparison whose prior grid and continuous marginalization are fully reproducible. All load-bearing claims are either derived, cross-checked at multiple independent levels, or explicitly scoped with labeled conservatism/heuristics. The work meets MNRAS standards for methodological depth in forecast papers and requires only clarifications, minor scoping tightenings, and publication-readiness housekeeping.

---

**BLOCKERS (must fix before publication)**

None. All scrutinized elements (f_NL prediction scoping, Heinrich externalization, forecast numbers, continuous-GR BF=6.0 calibration) are internally consistent, disclosed, and supported by the committed artifacts.

---

**MAJORS (should fix)**

**Sec. II C, line ~280 & Abstract line 4:** The phrase "mechanism-independent across all matter-bounce variants" appears once in the abstract but is qualified everywhere else in the body (UV-completion independence within the Wilson-Ewing/scalar-only class, conditional on (a)–(f)). Replace abstract occurrence with "UV-completion-independent within the scalar-only Wilson-Ewing class (conditional on assumptions (a)–(f) of Sec. II C)" or move the full qualifier to the abstract's first sentence for consistency.

**Sec. IV, Table IV caption & Sec. VII E:** The σ(f_NL)≈0.36 Fisher / 0.93 conservative phrasing in the referee prompt does not appear verbatim; the paper correctly uses the Heinrich baseline 0.7 with explicit widenings to ~0.9–1.41. Add one sentence cross-referencing the effective σ_eff column to avoid any external mis-mapping.

**Sec. VII C & Table III:** The continuous marginalization (BF=6.0 narrow competitor) is correctly reported and the ~23% inflation for σ_GR=0.5 is explicit; add "(15%→23% effective widening calibrated to the quadrature model)" in the caption for the exact calibration phrasing.

---

**MINORS (polish)**

- Abstract & Sec. I: "Heinrich et al. 2024 [6]" vs. "Heinrich+2023" — standardize to the paper's citation (already correct in body).
- Fig. 2 caption & Table IV: Minor axis-label / row-order consistency tweaks (e.g., align "all-combined" rows).
- Data/Code Availability paragraph: Insert Zenodo DOI placeholder or "will be minted on acceptance" (standard).
- Typos/LaTeX: ~6 minor (e.g., "f inf NL" spacing, one "ˆfNL" render).
- References: Confirm [6] Heinrich et al. matches the arXiv/ADS entry (valid per calibration); companion placeholders are deliberate and acceptable.

---

**Strengths**

- **Exceptional transparency:** every heuristic, scoping allowance, and unverified step is explicitly labeled and bounded; the systematic budget (Table IV) is one of the cleanest seen in a forecast paper.

- **Reproducibility gold standard:** 10,000-sample null-space scan, 3×10^5 MC ensembles, symbolic in-in verification, injection-recovery, and released scripts (c9i, c9k, c9g, etc.) make independent replication trivial.

- **Rigorous handling of the f_NL = −35/8 claim:** correctly labeled "minimally parameterized … conditional on (a)–(f)", with full discussion of fermion/ECH caveat, ϵ-correction, and polynomial null space — avoids overclaim while preserving the kinematic prediction's power.

- **Heinrich externalization is flawless:** sensitivity recast explicitly stated; no independent Fisher pretended. The 2.6–5σ envelope flows directly from the published 0.7 anchor + disclosed degradations.

- **Bayesian section is a model of care:** continuous marginalization, prior-grid worked example, and GR-calibration (~15%→23% → BF=6.0) are all present and correctly implemented.

---

**Specific scrutiny responses**

- **f_NL = −35/8 parameter-free claim:** Handled with precision (abstract "minimally parameterized … scalar-only class"; Sec. II C lists (a)–(f) and explicitly retracts stronger "mechanism-independent" language to UV-completion independence within the restricted class). No overstatement.

- **SPHEREx forecast (2.6–5σ):** The paper uses the correct Heinrich 0.7 bispectrum baseline; effective σ_eff values in Table IV produce exactly the quoted envelope after r, ϵ, b_ϕ, photo-z, and GR additions.

- **Heinrich+2023/24 anchor:** Correctly externalized as recast; σ=0.7 (bispectrum) and 0.5 (joint) both cited accurately; no independent computation claimed.

- **Continuous-GR marginalization (c9k, BF=6.0, 15%→23%):** Explicitly present (p. 16), with quadrature calibration matching the prompt; table and script reference confirm reproducibility.

The science is sound, the presentation is already near-publication quality, and the community will benefit immediately from this work. I recommend acceptance after the listed minor clarifications (one round).

Confidential comments to the editor: Strong candidate for "Editor's Suggestion" or rapid-track handling; the methodological rigor and code artifacts set a new bar for PNG-forecast papers. No ethical or priority issues.
