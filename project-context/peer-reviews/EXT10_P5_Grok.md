# EXT10 Harvest — P5 — Grok
- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=52437983-41f2-4016-ac45-ad392572ce46
- PDF md5: 43619245
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report (MNRAS / PRD style)

**Manuscript:** Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample (v0.1.74, 30 pp)
**Author:** Houston Golden
**Date:** 13 June 2026

---

**1. Recommendation**

**MINOR REVISIONS** (acceptance after author response to the items below; the science is sound, reproducible from committed artifacts, and the null result is robustly supported).

---

**2. BLOCKERS (must fix before publication)**

None. All load-bearing claims are supported, controls are present, and the primary/secondary framing plus artifact pipeline allow full reproduction.

---

**3. MAJORS (should fix)**

**§V B & Table II (analysis-tree declaration), line ~170–190:** The post-hoc designation of DESIVAST as "primary" (v0.1.39+) is correctly disclosed and Bonferroni-5 gated, but the text should explicitly state the exact version at which the primary/secondary split was frozen (already in abstract; add one sentence cross-referencing the Git commit/tag for the tree). Proposed fix: "The primary/secondary split and Bonferroni families were frozen at v0.1.63 (see pipelines/.../analysis_tree_v0.1.63.json)."

**§X (ASTRA cross-validation), p. 26–27 & Table XIV:** The 25,186-overlap caveat is noted, but add one clarifying sentence quantifying the V-Web vs ASTRA argmax label-disagreement fraction (~96% on filament/cluster) and confirm that the entropy-weighted Monte-Carlo (10^4 draws) reproduces the analytic σ to <0.02 as already done in artifact. This strengthens the "supporting diagnostic" label without new computation.

---

**4. MINORS (polish)**

- Abstract & §I: "V-Web secondary" nomenclature is clear in context, but add the footnote sentence from p. 4 to the abstract for first-time readers (already perfect in body).
- §IV A nomenclature reminder: Explicitly flag the v0.1.63 label migration (V-Web → consistent T-Web usage) as "implemented as V-Web prior to v0.1.63; now aligned with community T-Web label while retaining identical Hahn et al. 2007 recipe."
- §VI D & §VIII F (dual-parent ledger 678,945 vs 783,820/812,793): Already reconciled with duplicate-row impact quantified (3.56%, χ² invariant); add one cross-reference to the exact closure artifact and a short sentence confirming unique-TARGETID monopoles agree to four decimals.
- §V & multiple permutation sections: A one-sentence reminder in the look-elsewhere paragraph that the conditional-permutation approach is the standard for fixed-margin tests suffices.
- Figures 3, 5, 7 & Tables III, VII, VIII, X, XIV: Standardize "pp" vs "percentage points" in captions and ensure every σ column carries the explicit "from half vs monopole-subtracted" parenthetical on first use.
- Zenodo/artifact statement (Appendix C / §XIII): Mint the tagged v0.1.74 release DOI before resubmission and insert the permanent link (trivial submission-day action).

---

**5. Strengths**

- **Exceptional thoroughness and transparency:** primary DESIVAST analysis (n=56,981 voids, three independent algorithms + GALZONE native, program-split independence) is powered, Bonferroni-controlled, and RSD-bounded via explicit MC; every secondary path is correctly labelled "supporting" with multiplicity bookkeeping and committed artifacts.

- **Rigorous, reproducible statistics:** label-shuffle + position-shuffle nulls, Jeffreys intervals, explicit σ_pred monopole subtraction, empirical max-stat LEE, and full pipeline/outputs/JSON closure suite set a high bar for catalog/methodology papers.

- **Honest scoping and systematics control:** bright/dark residual, survey-edge artifacts, classifier monopole, duplicate rows (3.56%), RSD bound, and EDR-overlap caveats are quantified and shown not to drive the null; the paper explicitly bounds future bounce/inflation models without over-claiming.

- **Clear separation of primary (DESIVAST Δf_CW = +0.0007, |z_Δ| ≤1.25 across five estimators) vs secondary results**, with dual-parent ledger reconciled and invariance demonstrated.

---

**6. Specific scrutiny (all pass cleanly)**

- **DESIVAST void cross-classifier (56,981 voids; primary since v0.1.39):** Fully load-bearing, correctly implemented (point-in-sphere + exact k-unbounded rerun, Table VIII, three-algorithm Table X, GALZONE native §VIII D), program-independent (§VIII B Table IX), and sky-stratified (§VIII E). Null is robust (|Δf_CW| ≲0.004, all p_Δ >0.21 after Bonferroni-5).

- **T-Web tidal-tensor classification (14.6M DESI DR1; replaced V-Web at v0.1.63):** Implementation of Hahn et al. 2007 (Tij = ∂²Φ/∂xi∂xj, λth=0 default, 256³ grid, Rs sweep) is detailed; nomenclature footnote transparent. Phase-2 sweep + grid-convergence confirm invariance.

- **ASTRA-DESI per-object cross-validation (25,186 spirals):** Supporting diagnostic correctly caveated (EDR-only, strong per-galaxy label disagreement ~96% on dense classes, small overlap). Table XIV shows identical null conclusion under argmax/entropy-weighted/V-Web-on-overlap.

- **Dual-parent sample ledger (678,945 vs 783,820 unique TARGETID counts):** Explicitly reconciled; DESIVAST low-z parent is the powered primary; V-Web row-level superset used only where noted. All conclusions invariant.

- **Conditional-permutation framing correction (v0.1.63):** Label-shuffle correctly conditions on observed total CW count (standard for fixed-margin tests); every permutation p-value and LEE is computed this way, with stratified variants and distinct-stream re-draws confirming robustness. Framing is conservative and transparent.

The paper is a strong, reproducible contribution that sets a methodological standard for future DESI environmental analyses of the chirality catalog. The null is convincingly established at current sensitivity. Accept after the minor items above.
