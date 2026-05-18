# P4_v1_0_113_R_INTERNAL R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1815pt
**Wall time**: 101.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=91301, completion=6472, reasoning=5498, total=97773

---

## PAPER-GPT-B1 — BLOCKER

**Section:** Abstract; §III.A/Table I; §IX.J Sensitivity/Table XI; Conclusions item 1  
**Issue:** Injection-recovery sample is internally contradictory: the abstract first anchors the $A\simeq0.75\%$ threshold to $N=471{,}049$ ($p>0.9$), then says the released JSON was actually $p_{\rm eq}>0.6$ with $N=2{,}107{,}494$; the body/table still claim $N=471{,}049$. The empirical threshold, Fisher comparison, and systematic budget are not auditable.  
**Fix:** Treat the JSON manifest as authoritative or rerun both samples. Update every $N$, mask, $f_{\rm sky}$, Fisher floor, and table/caption; quote $0.75\%$ only for a pinned matched sample.

## PAPER-GPT-B2 — BLOCKER

**Section:** §XIII NaMaster config, “Monopole-subtraction note”; Abstract; Table I; Conclusions “Canonical-$N$ MASTER”  
**Issue:** The σ-reconciliation arithmetic is internally consistent, but the manuscript still uses obsolete $+1.85\sigma$ as “canonical” and “sub-detection-threshold” while §XIII says corrected monopole-subtracted $+3.64\sigma$ supersedes it paper-wide. This changes the canonical-mask status from subthreshold to $>3\sigma$ under the binomial null.  
**Fix:** Make $+3.64\sigma$ the corrected canonical-mask result everywhere; label $+1.85\sigma$ as historical/unsubtracted only. Recompute the headline summary and verdict text accordingly.

## PAPER-GPT-B3 — MAJOR

**Section:** Abstract; §IV.C Monopole+Mask; Fig. 6 caption; §IX.B Hemisphere Discussion  
**Issue:** Bootstrap scrub failed. The abstract still says the bootstrap pixel-resample null gives $-0.22\sigma$, “consistent with null,” and later text still uses “disappears under bootstrap” rhetorically, despite the audit showing a real injected $A=1.7\%$ dipole also gives bootstrap $\sigma\approx0$.  
**Fix:** Remove bootstrap from abstract/verdict logic. State only: “bootstrap is a sampling-variance diagnostic and is not a cosmological-dipole null test.”

## PAPER-GPT-B4 — MAJOR

**Section:** §IV.C “Honest scientific verdict”; Abstract/Conclusions three-discriminator claims  
**Issue:** The three discriminators do not rigorously prove interpretation (ii). $\ell=2>\ell=1$ lacks a calibrated distribution under masked injected dipoles; $p_{\rm eq}$ quartile washout lacks a joint power/likelihood calculation; the $r_{\ell=2}=-0.65$, $-2.89\sigma$ cross-spectrum has no LEE over multipoles/proxies and directly addresses only the quadrupole.  
**Fix:** Downgrade to “favours a depth/sampling-correlated systematic.” For a rigorous claim, fit a joint model with dipole amplitude/axis plus depth/PSF/morphology templates and quote a marginalized LR/Bayes factor or predeclared simulation p-values.

## PAPER-GPT-B5 — MAJOR

**Section:** Title; Abstract; Introduction; Conclusions item 1; §IX.G Parity translation  
**Issue:** The paper still frames the result as “No Evidence for Parity Violation,” but its own symmetry derivation says the $\ell=1$ chirality dipole is parity-even and tests isotropy, while the parity-odd monopole is nonzero and attributed to labels. The title and several conclusion statements overclaim what the estimator tests.  
**Fix:** Retitle/reframe as “No evidence for a large-scale projected chirality dipole / isotropy-breaking axial-vector signal.” Reserve “parity violation” for parity-odd monopole, 3D spin-vector, or polarization observables.

## PAPER-GPT-B6 — MAJOR

**Section:** Abstract throughout  
**Issue:** The abstract is still a defensive changelog, not an abstract: >2000 words, version tags, reviewer names, artifact paths, repeated caveats, and malformed prose such as “Under this three-discriminator framework).” It also exposes contradictory numbers in the most visible text.  
**Fix:** Rewrite to <400 words: scope, catalog, primary estimators, empirical sensitivity, main leakage result, and matched-pipeline caveat. Move provenance/reconciliation logs to an appendix.
