# P1B 2026-06-04_R2pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 264.1s

---

## Referee Report: Confabulation and Reproducibility Audit

### ESSENTIAL REVISIONS  
**P1B-E1: Abstract (p.1), Section VIII (p.8)**  
- **Problem**: Abstract claims ∆N<sub>eff</sub> = -0.020 ± 0.169 (full-tension) and +0.065 ± 0.17 (Planck+BAO+SN), but no script/output in reproducibility materials directly generates these values. Repository requires full MCMC regeneration (4–12 hours) without a summary script.  
- **Fix**: Provide standalone script in `reproducibility/` that outputs posterior summaries (e.g., `getdist` table) for all headline ∆N<sub>eff</sub>/H<sub>0</sub> values.  

**P1B-E2: Section III (p.3), Table II (p.4)**  
- **Problem**: w<sub>0</sub> = -0.812 ± 0.044 and w<sub>a</sub> = -0.667 ± 0.186 (Table II) presented as "departing from ΛCDM at +4.3σ/-3.6σ" but σ values are marginal-tail extrapolations, not formal significances. Unsafe to label as "σ" without qualification.  
- **Fix**: Clarify these are *approximate* tail distances, not rigorous statistical σ. Add: "Unsampled ΛCDM point prevents formal tension calculation; nested sampling required for robust evidence."  

**P1B-E3: Section VI (p.6), Abstract (p.1)**  
- **Problem**: Pipeline-recovery SNR (20.32σ for β-injection) conflated with sky-detection significance (2.4–2.9σ). Abstract states SNR refers to MC recovery, but "20.32σ" risks misinterpretation as sky significance.  
- **Fix**: Relabel "SNR" as "MC recovery significance" in all instances. Add bold disclaimer in Abstract: "**Pipeline SNR ≠ sky significance**."  

---

### MAJOR REVISIONS  
**P1B-M1: Section III (p.2–4)**  
- **Problem**: Internal audit tags ("corrected fire #25", "shoes yaml audit.md", "R8 GEM-B3 nit") in body prose. Unprofessional and confuses readers.  
- **Fix**: Remove all version-control artifacts. Replace with neutral descriptions (e.g., "previous calculation error").  

**P1B-M2: Section VI (p.6–7)**  
- **Problem**: ALP birefringence consistency claim (β ≈ 0.27°) lacks traceable code. Appendix C describes parameters but no script for β = 0.336° ± 0.107° output.  
- **Fix**: Add script `reproducibility/ALP_fit/analyze_ALP_chains.py` to compute β posterior from MCMC chains.  

**P1B-M3: Section IV (p.5)**  
- **Problem**: NaMaster bias (0.032°–0.040°) derived from 500 MC realizations, but driver script (`pipelines/h200_results/pod1_namaster_umap_2026-04-29/`) not linked to outputting these values.  
- **Fix**: Include script in reproducibility manifest that computes bias/SNR from MC outputs.  

**P1B-M4: Abstract (p.1), Section VIII (p.8)**  
- **Problem**: "25× misalignment tuning" for spectator ALP (θ<sub>i</sub> ~ 0.1 vs. θ<sub>i</sub> ~ 0.5) unsupported by code. Calculation (θ<sub>i</sub><sup>2</sup> scaling) stated but no script.  
- **Fix**: Add script `reproducibility/ALP_tuning/theta_tuning.py` computing Ω<sub>a</sub> ∝ θ<sub>i</sub><sup>2</sup> and tuning factor.  

---

### MINOR REVISIONS  
**P1B-m1: Section III (p.3), Table I (p.3)**  
- **Problem**: Sample-count arithmetic (176,240 × 0.7 ≈ 123,368) cannot be verified without raw chain files. Repository only provides regeneration instructions.  
- **Fix**: Include `post_burnin_samples.csv` with sample counts after burn-in removal.  

**P1B-m2: Section V (p.6)**  
- **Problem**: Bayes factors (∆AIC/BIC/ln B) omitted pending nested sampling, but paper uses posterior departures (+4.3σ) as evidence. Overstates conclusiveness.  
- **Fix**: State prominently in Results: "Bayesian evidence pending; current σ distances provisional."  

**P1B-m3: Section II (p.2)**  
- **Problem**: "ECH spin-torsion framework alone does not resolve tensions" contradicts Paper I(a)’s claims. No cross-reference to Paper I(a) § clarifying scope.  
- **Fix**: Explicitly cite Paper I(a) section (e.g., "§Structural Tension") where limitations are discussed.  

---

### NITPICKS  
**P1B-N1: Abstract (p.1)**  
- **Problem**: Redundant "spectator-ALP" in "spectator-ALP consistency check" and "spectator-ALP model."  
- **Fix**: Remove second "spectator-ALP": "a consistency check with a spectator-ALP model."  

**P1B-N2: Section III (p.3)**  
- **Problem**: "Converged iter2 posterior" has no iter1 reference. Jargon unclear.  
- **Fix**: Define "iter2" at first use: "second iteration of MCMC chains."  

**P1B-N3: Appendix A (p.10)**  
- **Problem**: HuggingFace datasets mentioned but no URLs in repository README.  
- **Fix**: Add direct dataset links to `reproducibility/README.md`.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

The paper’s core technical claims (MCMC posteriors, pipeline validation, ALP consistency) are scientifically sound but lack complete traceability in reproducibility materials. Internal audit tags and version-history artifacts (e.g., "fire #25", "v1B.0.7") must be purged from prose. Headline figures (∆N<sub>eff</sub>, H<sub>0</sub>, β-bias) require dedicated output scripts—not just regeneration instructions—to permit independent verification. Statistical significances for w<sub>0</sub>/w<sub>a</sub> departures must be rigorously qualified to avoid overstatement. With these revisions, the paper will meet PRD’s standards for reproducibility and clarity. Page count (12 pp) is appropriate for the scope.