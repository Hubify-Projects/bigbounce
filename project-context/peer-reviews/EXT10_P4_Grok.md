# EXT10 Harvest — P4 — Grok
- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=9b06db9f-adeb-4928-8b88-8b17655b095d
- PDF md5: 414048af
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report for MNRAS (submitted as v1.0.185, 22 pp., 8.47 M-galaxy catalog paper)

---

**Recommendation: MINOR REVISIONS**

The manuscript presents a high-quality, reproducible catalog and analysis of galaxy chirality on the full DESI Legacy DR8 footprint. The work is methodologically rigorous, transparently documented (with extensive committed artifacts), and constitutes a substantial advance in sample size, bias controls, and null-testing depth relative to prior literature. The primary cosmological claim (null real-space dipole at sub-percent sensitivity on the HC subsample) is robustly supported and cleanly separated from the explicitly-labeled systematics diagnostics in the MASTER channel. No load-bearing scientific claim is unsupported, and reproduction from the released HuggingFace assets + scripts appears straightforward. The paper meets MNRAS standards for a catalog/methodology contribution and requires only targeted clarifications and polish before acceptance.

---

**1. BLOCKERS (none)**

No changes required before publication. All scrutinized claims (real-space headline, template exclusion, MASTER framing, ℓ=2 cross-spectrum, Shamir citations) are accurately presented and internally consistent with the text, tables, figures, and referenced artifacts.

---

**2. MAJORS (should fix; 2 items)**

**Sec. III B + Table I (lines ~120–150):** The declared estimator hierarchy is clear in principle but buried; readers scanning for the primary cosmological result may miss that the real-space HC dipole (row i) and block-bootstrap WLS template exclusion (row ii) are the sole anchors for the "null verdict," while MASTER rows (iii–iv) are explicitly non-primary diagnostics. Add one short declarative sentence immediately after the bullet list: "Cosmological conclusions rest exclusively on estimators (i) and (ii); all MASTER results are systematics diagnostics only (see Sec. IV D and Appendix D)."

**Appendix D (canonical-mask 8-anchor audit, ~page 19):** The joint nuisance-marginalized WLS template fit (z ≈ −18) and the ℓ=2 auto-/cross-spectrum evidence (r_ℓ=2 = −0.65, −2.89σ vs. depth proxy) are strong but currently split across text and artifacts. Consolidate into a single summary table (or expanded caption) listing the three discriminators that rule out interpretation (i) "clean cosmological dipole at ~1.7%" (ℓ=2 > ℓ=1 structure, quality-quartile washout, negative cross-spectrum).

---

**3. MINORS (polish; 4 items)**

- Abstract and Sec. IV C opening: The real-space headline ("+0.41σ (moment-z), empirical-rank p=0.31, A_dip < 6.8×10^{-3} at 95% UL") and earlier v1.0.166 withdrawal note are correctly disclosed per policy, but the sentence could more explicitly cross-reference the fixed null generator and Appendix A provenance audit for completeness.

- Fig. 9 + Table VI caption: Clarify once that the harmonic-channel completeness (P(≥3σ)≥0.999 at A_p=0.75%) is estimator-specific and "not interchangeable with the real-space A_{95} falsification boundary (Sec. VI A)".

- Sec. V A (Shamir comparison): The split between Shamir (2020/2022) references with arXiv IDs is accurate and appropriately caveated. Minor re-phrasing to "Shamir (2022e; arXiv:2212.04044, published MNRAS 516, 2281)" for explicitness.

- Data Availability + Acknowledgments: Add explicit Zenodo DOI placeholder and confirm HF CC-BY-4.0 license + model weights are live. Trivial submission-day action.

---

**4. Strengths (5 bullets)**

- Largest publicly released chirality-labeled catalog to date (8.47 M galaxies, 3.20 M spirals) with three tiers (raw/Platt/equivariant), full provenance JSONs, and HuggingFace distribution + reproducibility scripts — an immediate community resource.

- Exemplary bias-hardening: 2-fold flip-TTA enforcing exact equivariance (flip-swap correlation=1.000), dedicated NOT_SPIRAL class, 8-test audit suite (T1–T8 all pass), GZ1 cross-match floor (69.91% chirality accuracy), and explicit propagation of this floor into all isotropy bounds.

- Crystal-clear separation of primary cosmological estimators (real-space HC dipole + block-bootstrap WLS template exclusion at z≈−18) from MASTER diagnostics, with a generative monopole-only null reproducing 99.32% of pre-MASTER ℓ=1 power and an 8-anchor Appendix D audit convincingly attributing residuals to depth/morphology systematics.

- Empirical injection-recovery floors (A_{50}≈0.75%, A_{95} bracketed 1.0–1.5% on HC subsample) and harmonic-channel completeness curve provide quantitative falsification criteria rather than vague "null" statements.

- Exceptional transparency: correction notes, withdrawn earlier results, over-confidence caveat, and queued follow-ups are all explicitly flagged; this is model referee behavior for a complex multi-estimator analysis.

---

**5. Specific scrutiny on the requested items**

- **Real-space ℓ=1 dipole headline (+0.41σ, p=0.31, A_dip<6.8×10^{-3} 95% UL):** correctly stated, robust under label-shuffle/per-galaxy shuffle/weighting/mask-threshold variants, and the low-confidence-tail excess is transparently attributed and shown to collapse with the HC cut. The v1.0.166 synthetic-footprint MASTER null withdrawal is properly noted with provenance link.

- **Joint nuisance-marginalized template fit:** excludes a clean 1.7% dipole at z≈−18 (block-bootstrap, NSIDE=8 super-pixels, N_boot=1000) with residual spatially coherent — fully supported by Appendix D.

- **MASTER channel is explicitly labeled "systematics diagnostic"** (+7.28σ apodized footprint, unchanged under depth-stratified nulls); the monopole-only generative null and interpretation (ii) "depth/morphology survey systematic" are unambiguous.

- **ℓ=2 cross-spectrum r=−0.65 (σ=−2.89)** vs. pixel-density proxy is correctly used as supporting the systematic interpretation and is part of the 8-anchor battery.

- **Shamir 2020 vs 2022 split with arXiv IDs:** handled fairly and accurately; the factor-of-6–12 amplitude tension is clearly pipeline-specific.

All calibration notes were respected. The paper is ready for acceptance after the minor items above.
