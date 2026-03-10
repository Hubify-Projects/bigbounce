# Paper Content Snapshot — BigBounce v1.2.0

**Generated:** 2026-03-09
**Source:** arxiv/main.tex (canonical)
**Version:** v1.2.0 (+ uncommitted galaxy spin provenance edits)

---

## Title

**Geometric Dark Energy from Spin-Torsion Cosmology: Phenomenological Constraints and Correlated Signatures**

## Author

Houston Golden (Independent Researcher, Los Angeles, California, USA)

## Abstract (summary)

Framework combining LQG + Einstein-Cartan torsion for dark energy. MCMC fits yield:
- H₀ = 69.2 ± 0.8 km/s/Mpc (reduces Hubble tension from ~4.9σ to 2.9σ)
- σ₈ = 0.785 ± 0.016, S₈ = 0.80 ± 0.02 (reduces S₈ tension to ~1σ)
- Fine-tuning reduced from 10¹²⁰ to ~10⁵
- Three correlated signatures: galaxy spin asymmetry, cosmic birefringence, correlated axes

---

## Section List (13 main + 10 appendices)

### Main Sections
1. **Introduction** — Hubble/σ₈ tensions, theoretical pillars (LQC, Einstein-Cartan, BH origin)
2. **Theoretical Framework** — ECH action, Holst term, parity-odd derivation, bounce, cosmic rotation
3. **Observational Signatures and Evidence** — CMB E-B, galaxy spin (contested anomaly), H₀/σ₈
4. **Enhanced Theoretical Derivations** — One-loop parity-odd coefficient, vacuum energy, Λ_eff
5. **Data Methods: Galaxy Spin Analysis** — Sample selection, hierarchical Bayesian, dipole fitting
6. **Data Methods: CMB E-B Analysis** — Birefringence measurements, systematics, null tests
7. **Cosmological Fits and Model Comparison** — Datasets, MCMC config, Bayesian model comparison
8. **Systematic Analysis** — Combined significance, CMB/galaxy systematics, null tests, audit
9. **Falsification Criteria** — 5 independent falsification channels
10. **Related Work** — Rotating cosmologies, torsion, parity violation, galaxy spin, birefringence
11. **Discussion** — Inflationary suppression, theoretical implications, distance measures
12. **Limitations and Future Directions** — Current limitations, robustness, future prospects
13. **Conclusions** — Summary + data/code availability

### Appendices
A. Notation and Conventions
B. Complete Parameter Summary
C. Galaxy Spin Hierarchical Bayesian Fitting
D. Joint Likelihood Analysis
E. Loop Nieh-Yan Treatment
F. Covariant Rotation Framework
G. Error Analysis
H. Dimensional Analysis and Operator Normalization
I. Reproducibility Materials
J. Claims Classification

---

## Figure List (7 embedded)

| Fig | File | Caption Summary |
|-----|------|----------------|
| 1 | figure1_lqg_holst_derivation_enhanced.png | Energy density hierarchy Planck→dark energy |
| 2 | figure2_galaxy_spin_comprehensive.png | Galaxy spin A(z) dipole with Bayesian fit |
| 3a | figure_3a_tension_resolution.png | H₀ tension overview |
| 3b | figure3b_tensions_resolution_comprehensive.png | H₀ and σ₈ tension comprehensive |
| 4 | figure4_distance_impact.png | Distance impact of rotation-induced Λ_eff |
| 5 | figure5_rotation_expansion.png | Rotation effect on expansion |
| 6 | figure6_parameter_naturalness.png | Parameter naturalness comparison |

Additional figures exist but not embedded: figure7 (observational timeline), figure8 (detection forecast)

## Table List (8 tables)

1. Executive summary of key results (H₀, σ₈, fine-tuning)
2. Galaxy spin survey data properties
3. Parameter constraints table
4. Prior/configuration table
5. MCMC datasets table
6. Information criteria / model comparison
7. Fine-tuning comparison
8. Systematics/null tests summary

---

## Current Data/Reproducibility Wording

### Data Availability (Sec. 13)
> "All materials necessary to reproduce the cosmological and galaxy spin results are publicly available at [GitHub URL]"

Lists:
- 4 Cobaya YAML configs (planck, planck_bao, planck_bao_sn, full_tension)
- `spin_fit_stan.py` — hierarchical Bayesian fit to published aggregate CW/CCW counts
- `build_galaxy_spin_dataset.py` — downloads Galaxy Zoo DECaLS from Zenodo (DOI: 10.5281/zenodo.4573248)
- CW/CCW aggregate counts from Shamir (2024)
- IMPLEMENTATION_MAP.md and KNOWN_GAPS.md

### Reproducibility Appendix (App. I)
Same content as data availability, formatted for appendix. Includes Cobaya v3.6.1 compatibility note.

---

## Current Galaxy-Spin Wording

### Section 3.2: "Galaxy Spin Asymmetry: A Contested Anomaly"
- Framed as **contested** — acknowledges null results from Patel & Desmond (2024) and Philcox (2025)
- Signal: A₀ ~ 0.003, axis at (l~52°, b~68°) from Shamir
- Hierarchical Bayesian fit to published aggregate CW/CCW counts
- Framework survives null outcome: CMB birefringence provides independent evidence
- Figure 2 caption updated to reference "published aggregate CW/CCW counts from Shamir"

### Section 5: Data Methods: Galaxy Spin
- Sample selection, hierarchical Bayesian framework, dipole fitting procedure
- Stan model: A(z) = A₀(1+z)^{-p} e^{-qz}

### Appendix C: Galaxy Spin Hierarchical Bayesian Fitting
- Full model specification, label-noise correction, survey offsets

---

## Current WP4/WP5/P6 Integration Status

**WP4 (ΔNeff microphysics):** Not directly in Paper 1. The ΔNeff parameter is treated as phenomenological. Paper mentions "dataset-dependent, ranging from ~0.4 (CMB-only) to ~0.1 (full multi-probe)."

**WP5 (Galaxy spin amplitude):** Integrated as Sec 3.2, Sec 5, App C. Uses published aggregate counts. Object-level catalog (Galaxy Zoo DECaLS) built but CW/CCW not available — documented as future work.

**P6 (CMB E-B pipeline):** Integrated as Sec 3.1, Sec 6. References Minami & Komatsu (2020), Eskilt (2022), Diego-Palazuelos (2025). SPIDER 7σ result cited. Systematic considerations and null test requirements documented.

---

## Current Limitations/Caveat Language

### Section 12: Limitations and Future Directions

**Theoretical limitations (explicit):**
- Late-time w = -1 behavior is *assumed*, not derived
- Parity-odd coefficient treated as phenomenological parameter, not first-principles
- Inflationary suppression is a scaling estimate, not controlled calculation
- Order-of-magnitude gap in galaxy spin amplitude remains unresolved

**Observational limitations (explicit):**
- Galaxy spin signal is contested (null results acknowledged)
- ΔNeff is dataset-dependent, not unique prediction
- ACT DR6 (Neff = 2.86 ± 0.13) represents "most stringent challenge"
- Framework cannot currently derive birefringence rotation angle

**Robustness to null results (Sec 12.2):**
- Explicitly argues framework survives if galaxy spin signal is null
- CMB birefringence and cosmological tensions provide independent evidence
- "A null result would simplify the model (removing one prediction) rather than invalidating it"

---

## Key Numbers in Current Paper

| Quantity | Value | Source |
|----------|-------|--------|
| H₀ | 69.2 ± 0.8 km/s/Mpc | MCMC fit |
| σ₈ | 0.785 ± 0.016 | MCMC fit |
| S₈ | 0.80 ± 0.02 | Derived |
| ΔNeff | ~0.1–0.4 (dataset-dependent) | MCMC fit |
| H₀ tension residual | 2.9σ vs SH0ES | Computed |
| S₈ tension residual | ~1σ vs DES Y3 | Computed |
| Fine-tuning | ~10⁵ (vs 10¹²⁰ in ΛCDM) | Framework |
| Galaxy spin A₀ | ~0.003 | Empirical |
| Birefringence | 2.4–2.9σ (Planck + ACT DR6) | Literature |
| Bibliography | 64 entries (66 with uncommitted) | references.bib |

**NOTE:** These are the v1.2.0 numbers. Final chain convergence may update H₀, σ₈, ΔNeff values.
