# P4 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-v133verify_P4_v1_0_133
**Wall time**: 128.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=101269, completion=6951, reasoning=5771, total=108220

---

## PAPER-GPT-B1

- **Class:** BLOCKER  
- **Section:** v1.0.133 systematics-preserving-null paragraph / round-context values  
- **Issue:** Arithmetic is wrong: with data $C_1=6.55\times10^{-6}$, null mean $3.44\times10^{-6}$, std $3.07\times10^{-6}$, the z-score is $(6.55-3.44)/3.07=+1.01$, not $+3.80$. The stated $p_{\rm MC}=2/500$ is also incompatible with those moments unless a different data $C_1$ was used.  
- **Fix:** State the actual data $C_1$ used for the density-stratified null. If the intended data is $1.51\times10^{-5}$, replace the stale $6.55\times10^{-6}$ everywhere; if $6.55\times10^{-6}$ is correct, retract the “density-stratification does not absorb residual” claim.

## PAPER-GPT-B2

- **Class:** BLOCKER  
- **Section:** Conclusions, “Canonical-$N$ MASTER $\ell=1$ direct compute”; NaMaster appendix  
- **Issue:** The canonical $+3.64\sigma$ residual is numerically inconsistent. The listed values $C_1^{\rm decoupled}=2.298\times10^{-5}$, null mean $8.004\times10^{-6}$, null std $8.097\times10^{-6}$ give $z=+1.85$, not $+3.64$; elsewhere corrected values $1.51\times10^{-5}$, $3.12\times10^{-6}$, $3.31\times10^{-6}$ give $\sim+3.62$.  
- **Fix:** Replace all stale pre-correction canonical-MASTER numbers or explicitly label them legacy. Provide one canonical table with data, null mean, null std, empirical rank $p$, map definition, mask, and monopole treatment.

## PAPER-GPT-B3

- **Class:** BLOCKER  
- **Section:** Abstract/§Dipole vs §Edge-On “High-confidence robustness rerun,” Table `face_on`  
- **Issue:** The primary real-space dipole is reported as $+0.43\sigma$ with $p=0.30$, but the same “Catalog C full” sample in Table `face_on` gives $+4.31\sigma$ / $p=0.001$ under a monopole-preserving null. The explanation “different estimator” is not enough; this is an order-of-magnitude contradiction in a load-bearing null result.  
- **Fix:** Define both estimator equations and nulls side-by-side, run them on the same mask/data vector, and explain or remove the discrepant statistic. Until reconciled, the real-space null cannot be used as headline support.

## PAPER-GPT-M1

- **Class:** MAJOR  
- **Section:** Abstract; Table I footnotes; Conclusions canonical-mask discussion  
- **Issue:** Moment-z values are repeatedly framed as detection-like “$\sigma$” even when empirical ranks do not support them. Example: canonical $+3.64$ moment-z has empirical $p_{\rm MC}=15/500=0.030$, i.e. not a Gaussian $3.64\sigma$ tail; the density-stratified $p=2/500$ also needs finite-MC uncertainty / plus-one handling.  
- **Fix:** Report empirical rank $p$ as primary for MC-calibrated nulls and convert to Gaussian-equivalent only from that $p$ with MC-resolution caveats. Remove “$3.64\sigma$ residual” language from abstract-level claims unless Gaussianity is demonstrated.

## PAPER-GPT-M2

- **Class:** MAJOR  
- **Section:** v1.0.133 systematics-preserving null; §Conclusions  
- **Issue:** The “density-stratified systematics-preserving null” is not systematics-preserving. Permuting $A_p$ within density deciles preserves only the one-point $A_p|n$ distribution; it destroys spatial coherence, imaging-leg structure, PSF/depth gradients within deciles, and morphology correlations.  
- **Fix:** Rename it “density-conditioned shuffle null” and limit the claim to density-marginal conditioning. Claims about full depth/PSF/morphology systematics require the promised template-regression or nuisance-marginalized model.

## PAPER-GPT-M3

- **Class:** MAJOR  
- **Section:** §Sensitivity; Conclusions falsification criterion  
- **Issue:** The amplitude convention remains internally inconsistent: the text alternates among $0.2\%$, $0.29\%$, $0.4\%$, and $0.75\%$ as “floor”/“sensitivity,” while mixing half-modulation $A/2$, full amplitude $A$, Fisher limits, and empirical recovery thresholds. LSST projections also conflict ($0.08\%$ vs $0.04\%$).  
- **Fix:** Add a single table with rows for full catalog and HC subsample, columns for $1\sigma(A/2)$, $3\sigma(A/2)$, $1\sigma(A)$, $3\sigma(A)$, empirical 50%-recovery threshold, and systematic assumptions. Use only the empirical $0.75$–$1.5\%$ range for present-pipeline falsification claims.
