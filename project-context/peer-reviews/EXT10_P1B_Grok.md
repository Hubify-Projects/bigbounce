# EXT10 Harvest — P1B — Grok
- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=6fede933-742f-423b-b1d8-bbbf7254d6c1
- PDF md5: 06410d7c
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report: MNRAS / Phys. Rev. D / JCAP standards (methods/verification companion category)

**Manuscript:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model (v1B.0.68, 18 pp., arXiv-equivalent June 13 2026)

---

**Recommendation: MINOR REVISIONS**

The manuscript is a model technical-verification companion: it delivers exactly what the title promises, with gold-standard reproducibility, exhaustive scoping language, and zero over-claims on any of the three analyses. All load-bearing numerical results are supported by committed artifacts (frozen chains, 500-MC outputs, ALP grids, YAMLs). Under the calibration instructions for catalog/methods papers and the explicit "deliberate transparency" policy, the paper requires no substantive scientific rework and is publication-ready after light polishing and final housekeeping. It comfortably meets MNRAS/PRD/JCAP standards for a reproducibility-focused companion.

---

**BLOCKERS (0 — nothing must be fixed before acceptance)**

---

**MAJORS (0 — nothing "should" be fixed for scientific integrity)**

---

**MINORS (polish — all optional but recommended for final production)**

- Abstract / p. 1, line ~25 (NaMaster sentence): The parenthetical "both are MC pipeline-recovery figures…" is already clear, but shorten the long em-dash clause by one sentence for flow.
- Sec. III, fn. 1 & p. 3–4 burn-in reconciliation paragraphs: Excellent transparency, but the two-sigma-level sample-count minutiae could be moved to Appendix A (reproducibility) with a one-line pointer in the main text.
- Sec. VI, p. 10–11 (spectator caveat blocks): The ~25× tuning is already stated in abstract/main/fn6; consider consolidating the three near-identical restatements into a single bolded sentence at the start of Sec. VI with cross-references.
- Data/Code Availability (p. 14) & App. A: Insert the pending HuggingFace DOIs and Zenodo mints (or note "DOI assignment pending at submission"); tag the exact v1B.0.68 commit SHA in the GitHub README as promised.
- References: All cited works (including 2025/2026 preprints per calibration) are treated correctly; no action required.
- General: Run a final pdflatex pass to resolve any remaining extraction artifacts in displayed equations.

---

**Strengths (≥3)**

- **Gold-standard open-science infrastructure:** full frozen chains + diagnostics on HuggingFace/GitHub, exact YAMLs, reproduce_*.sh scripts, IMPLEMENTATION_MAP.md, and KNOWN_GAPS.md — this is genuinely best-in-class for a cosmology verification paper and sets a benchmark for the series.

- **Exceptional intellectual honesty:** every analysis is explicitly scoped (stock-CAMB proxy ≠ theory module; synthetic-sky MC ≠ sky detection; ALP check = consistency-not-prediction; ~25× θ_i tuning disclosed in abstract + main text + fn6 + posterior-subset readout). No reviewer will be surprised by limitations.

- **Rigorous treatment of all scrutinized elements:** combined with clear null-consistency framing makes the paper a reliable reference for future ECH-related work and for the broader community checking birefringence pipelines or extra-radiation proxies.

---

**Specific scrutiny on the four requested points (all pass cleanly)**

- **309,189 MCMC samples (176,240 full-tension + 132,949 Planck+BAO+SN):** Fully reconciled in fn. 1, convergence reports (R̂⁻¹ ≤ 0.003, min ESS ~4,700), GetDist vs. conservative 30% burn-in discussion, and committed CORRECTED.json artifacts. Reproducibility is airtight; no concern.

- **ΔN_eff ≈ 0 result (+0.058 ± 0.179 Planck+BAO+SN, chain-recomputed EXT2; full-tension –0.020 ± 0.169):** Correctly framed as proxy-only (stock CAMB, BBN-consistent Y_He, no torsion Boltzmann module), one-sided 95% limits supplied, independent re-run cross-check (0.04σ agreement), and explicit non-resolution of H_0 tension. Solid null-consistency statement.

- **NaMaster pseudo-C_ℓ 500-MC recovery at SNR=20.32σ:** Explicitly and repeatedly labeled as "pipeline-validation figure on synthetic skies, NOT a sky-detection significance." Bias floor (worst-case |Δβ̂| = 0.040°), robustness battery (6 configs), and sign-symmetry check are all documented with artifacts. Excellent.

- **Spectator-ALP carved-out regime (f_a ∼ M_Pl, m ∼ H_0; explicit Ω_φ ≪ Ω_crit restriction):** The ~25× θ_i tuning is disclosed in the abstract, main text, fn. 6, posterior-subset readout (13% mass for Ω_a < 0.01, β consistent at 0.5σ), and continuous-prior Caγ scan. The framing "accommodates but does not naturally predict" is honest and load-bearing.

---

**Overall assessment**

This is the kind of careful, reproducible companion paper the field needs. With the minor polishing items above (all straightforward), the manuscript is ready for publication. I recommend acceptance after MINOR REVISIONS.

Confidential comments to the editor: Strongly support coordinated submission of the full ECH series. The reproducibility standard set here raises the bar for the entire package. No ethical or competing-interest concerns.
