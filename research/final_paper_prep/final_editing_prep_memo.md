# Final Editing Prep Memo — BigBounce Paper 1

**Date:** 2026-03-09
**Current version:** v1.2.0
**Target:** arXiv submission (gr-qc / astro-ph.CO / hep-th)

---

## A. READY FOR FINAL EDITING NOW

These sections can be polished to submission quality immediately:

### 1. Introduction (Sec. 1)
Complete. Theoretical pillars, tension numbers, contributions list, paper organization — all stable. Only change needed: update H₀/σ₈/ΔNeff numbers once final chains converge (placeholder values clearly identified).

### 2. Theoretical Framework (Sec. 2)
Complete. ECH action, Holst term derivation, bounce mechanism, cosmic rotation formalism, inflationary suppression — all stable. No dependence on MCMC results.

### 3. Galaxy Spin Section (Sec. 3.2, Sec. 5, App. C)
Complete. "Contested anomaly" framing is honest and defensible. Data provenance updated to published aggregate counts (Shamir 2024) + Galaxy Zoo DECaLS build script. Hierarchical Bayesian model documented. Null results acknowledged. Ready for final polish.

### 4. CMB E-B Section (Sec. 3.1, Sec. 6)
Complete. References Minami & Komatsu, Eskilt, Diego-Palazuelos, SPIDER 7σ. Systematic considerations and null tests documented. No MCMC dependence.

### 5. Enhanced Derivations (Sec. 4)
Complete. One-loop parity-odd coefficient, vacuum energy, Λ_eff derivation — all stable theoretical content.

### 6. Falsification Criteria (Sec. 9)
Complete. Five independent falsification channels defined with quantitative thresholds. No MCMC dependence.

### 7. Related Work (Sec. 10)
Complete. Properly positioned against rotating cosmologies, torsion cosmology, parity violation, galaxy spin studies, cosmic birefringence.

### 8. Limitations and Future Directions (Sec. 12)
Complete. Honest disclosure of theoretical and observational limitations. Robustness arguments documented.

### 9. Systematic Analysis Framework (Sec. 8)
Structure complete. Null test definitions, systematic error budgets — stable. Quantitative results need updating with final chains.

### 10. All 10 Appendices
Mostly complete. Notation, parameter summary (needs final numbers), galaxy spin model (complete), joint likelihood (complete), Nieh-Yan (complete), rotation framework (complete), error analysis (needs final numbers), dimensional analysis (complete), reproducibility (updated with galaxy spin changes), claims classification (complete).

### 11. Reproducibility Infrastructure
All code artifacts exist and are documented:
- 4 Cobaya YAMLs (working with v3.6.1)
- Stan galaxy spin fit (verified data path)
- Galaxy Zoo DECaLS build script (from Zenodo DOI)
- IMPLEMENTATION_MAP.md and KNOWN_GAPS.md

### 12. Bibliography
64 entries (66 with uncommitted Shamir2024 + Walmsley2022). All citations resolve. No missing references. Recent additions include DESI DR2, ACT DR6, SPIDER 7σ, Liu et al. torsion-DESI.

---

## B. WAITING ON FINAL CHAIN CONVERGENCE

These items require the full_tension MCMC science freeze (estimated ~3.5 days, ~2026-03-13):

### 1. Final Parameter Values
Current paper quotes: H₀ = 69.2 ± 0.8, σ₈ = 0.785 ± 0.016, S₈ = 0.80 ± 0.02
These will be replaced by the converged full_tension posterior means ± 1σ.
Affected locations: Abstract, Table 1, Sec. 7, Sec. 13, App. B.

### 2. Final ΔNeff Constraints
Current: "ranging from ~0.4 (CMB-only) to ~0.1 (full multi-probe)"
Final values from all 4 datasets will sharpen this. The dataset-dependent nature is already documented.

### 3. Final Posterior Plots (Corner Plots)
Not yet generated. Need converged chains to produce:
- H₀ vs ΔNeff posterior (main diagnostic)
- Full parameter corner plot
- Per-dataset comparison overlay

### 4. Final Convergence Table
Need to report R-hat, ESS, chain length for each dataset.
This goes in App. I (reproducibility) or Sec. 7 (MCMC config).
Current cohort_main diagnostics (from live audit):
- full_tension: 6/8 gates, Rm1(H0) = 0.004
- planck_only: 5/8 gates, Rm1(H0) = 0.004
Best to wait for all 8/8 gates on full_tension.

### 5. Model Comparison Table (ΔNeff vs ΛCDM)
Need CPU2 (ΛCDM controls) to converge for proper Bayesian model comparison.
Current: CPU2 R-hat looks good (all < 0.01) but ESS is still low.
Required: converged evidence ratios (ln B) for each dataset.

### 6. Final Abstract Numbers
The abstract contains specific numbers that must match the final chains.
Update simultaneously with parameter values.

### 7. Updated Figure 3a/3b (Tension Plots)
If final H₀/σ₈ values shift meaningfully, the tension resolution figures need regenerating.

### 8. ΔNeff Viability Figure
Currently exists as supplementary (public/images/dneff_viability.png).
Decision: embed in paper or keep as supplementary? Depends on final ΔNeff values.

---

## C. LIKELY FINAL NARRATIVE DIRECTION

Based on the current evidence (live chain audit, 2026-03-09):

### The Emerging Picture

**full_tension (Planck + BAO + SN)** is the primary result dataset, now at 62,080 cohort_main samples with excellent R-hat convergence (all params < 0.01). The physics story will likely be:

1. **H₀ tension partially reduced** — from ~4.9σ to ~2.5-3σ via ΔNeff. The exact residual depends on the final posterior mean. The current 69.2 ± 0.8 gives 2.9σ. A shift to ~69.5 would give ~2.7σ.

2. **σ₈/S₈ tension largely resolved** — S₈ brought to ~1σ from DES Y3. This remains one of the strongest selling points.

3. **ΔNeff is small but nonzero for full multi-probe** — the dataset-dependent nature is already honestly documented. The full_tension ΔNeff will likely be 0.05–0.15, consistent with the ACT DR6 constraint.

4. **Galaxy spin section is stable** — "contested anomaly" framing is correct and defensible regardless of outcome. The honest provenance upgrade strengthens the paper.

5. **Cosmic birefringence provides the strongest independent evidence** — 2.4–2.9σ from Planck/ACT, with SPIDER 7σ total rotation. This is independent of MCMC chains.

6. **Model comparison** — once CPU2 converges, we'll have ΔNeff vs ΛCDM evidence ratios. The expectation is that ΔNeff is weakly preferred for CMB-only but comparable to ΛCDM for full multi-probe (the "dataset-dependent" story).

### Estimated Timeline

- **March 13:** full_tension science freeze (6/8 → 8/8 gates)
- **March 14-15:** Generate final posterior plots, update parameter values
- **March 16-18:** CPU2 convergence for model comparison table
- **March 18-20:** Final editing pass (update all numbers, regenerate figures)
- **March 20-22:** Internal review + website sync
- **March 22-25:** arXiv submission

### Key Risk

The main risk is **full_tension ESS** not growing fast enough. Current ESS(H0) = 781 needs to reach 2000. If sampling slows, the timeline pushes out. Mitigation: the paper can be submitted with current convergence levels + honest reporting of chain status, since R-hat is already excellent.

---

## EDITING STRATEGY

**Phase 1 (now):** Polish all chain-independent sections (theory, galaxy spin, CMB E-B, falsification, limitations, related work, appendices). Fix any remaining language issues. This can proceed immediately.

**Phase 2 (after freeze):** Update all MCMC-dependent numbers. Generate final figures. Write final abstract. Update Table 1.

**Phase 3 (final):** Full document review. Check all cross-references. Recompile PDF. Sync website. Submit.
