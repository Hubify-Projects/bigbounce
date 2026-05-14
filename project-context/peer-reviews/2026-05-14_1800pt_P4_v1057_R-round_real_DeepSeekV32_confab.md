# P4_v1057 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_1800pt
**Wall time**: 42.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=53946, completion=1192, total=55138

---

# DeepSeek-V3.2 Adversarial Peer Review Findings

## PAPER-DEE-B1: Abstract L185 – Load-bearing scalar without provenance
**Classification:** BLOCKER  
**Issue:** The abstract states: "A real-space dipole fit yields σ_dipole=0.43 (p=0.30 at N_MC=10,000)". This is a headline null result, but there is no JSON/script/dataset cited in the abstract that produces this number. The provenance is buried in footnotes (fn:mc_count) and scattered references (outputs/dipole/summary.json) later in the paper.  
**Fix:** In the abstract, append a direct citation to the canonical result file: e.g., "σ_dipole=0.43 (p=0.30 at N_MC=10,000; canonical result outputs/dipole/summary.json)". This ensures the headline figure is traceable from the abstract itself.

## PAPER-DEE-B2: Fig 14 caption L1633 – Misleading pseudo-Cℓ significance
**Classification:** MAJOR  
**Issue:** Caption for Fig 14 (multipoles) states: "Note: the figure as plotted shows the original raw pseudo-Cℓ (ℓ=1 at 2.75σ relative to the original shot-noise floor). After the corrected N_spiral normalization the pseudo-Cℓ SNR is 6.48σ and the MASTER-decoupled value is 6.08σ". This conflates intermediate estimators. The 6.48σ and 6.08σ are pre-MASTER artifacts; the headline is -0.12σ post-MASTER. The caption should not present intermediate inflated values as "corrected" without immediate caveat that they are mask-coupling artifacts.  
**Fix:** Rewrite caption to clearly sequence: raw pseudo-Cℓ (6.48σ) → MASTER-decoupled (6.08σ) → full MASTER deconvolution (-0.12σ). State explicitly that 6.48σ/6.08σ are NOT the result and are removed by MASTER.

## PAPER-DEE-B3: §VIII.E enum L2070 – "0.29%" Fisher floor arithmetic inconsistency
**Classification:** MAJOR  
**Issue:** Conclusions enumerate: "the statistical-only Poisson floor is 0.2% and is retained as a theoretical asymptote (not as the user-facing sensitivity)." Earlier in §VIII.E deferral paragraph (L2070) states: "the analytic dipole sensitivity formula σ(A_dip) = 0.048% is the uncertainty on the CW-fraction modulation A/2 ... so the ideal 3σ amplitude floor ... is ~0.29%". The 0.2% vs 0.29% discrepancy is unresolved. The abstract uses "0.29%" Fisher floor, but conclusions say "0.2%".  
**Fix:** Standardize: either adopt 0.29% Fisher floor everywhere (abstract, sensitivity section, conclusions) and explain 0.2% is a rounded conservative cushion, or explicitly note the 0.2% is a rounded presentation of 0.29%. Do not leave two different numbers in adjacent sections without reconciliation.

## PAPER-DEE-B4: Abstract L185 – Hemisphere max-statistic p_LEE provenance missing
**Classification:** minor  
**Issue:** Abstract states: "A 3.05σ local hemisphere asymmetry ... under a 10,000-MC permutation null (random CW-label shuffles at NSIDE=8 / 768 directions) rejects the random-label null at p_LEE≤10^-4 (zero of 10,000 nulls reach the data)". The provenance for this p_LEE is only given later in §VIII.E (mc_seed_manifest.json). The abstract should cite the canonical result file.  
**Fix:** Add citation in abstract: "p_LEE≤10^-4 (canonical MC manifest outputs/canonical_provenance/mc_seed_manifest.json)".

## PAPER-DEE-B5: Table III (multipole) – Bandpower significance provenance incomplete
**Classification:** minor  
**Issue:** Table III cites companion artifacts for rows (master_results/master_power_spectrum.json, r42_results/wave_14_pp_namaster_verification.json) but does not cite the source for the "Joint χ^2/dof (38 bandpowers)" value (161.2/38). This joint statistic is load-bearing for mask-coupled monopole leakage claim.  
**Fix:** Add a footnote to the joint χ^2 row citing the exact result file (likely wave_14_pp_namaster_verification.json includes this). Ensure the joint value is reproducible from the cited JSON.

## PAPER-DEE-B6: §VIII.E deferral paragraph – Unresolved Shamir bibitem
**Classification:** nit  
**Issue:** The deferral paragraph notes Shamir (2022) arXiv ID removed pending verification, journal reference retained. This leaves the bibliography incomplete. The paper should either include a verified arXiv ID or note "no arXiv preprint available" explicitly.  
**Fix:** In bibliography, for Shamir (2022) entry, either add verified arXiv ID or state "Published in PASJ 74, 1114 (2022); no arXiv preprint available".

**BLOCKER count:** 1 (PAPER-DEE-B1).  
**Overall:** The reframe is correctly applied at the three sites (abstract, Fig 14 caption, §VIII.E). The new issues introduced are mainly provenance gaps and numerical inconsistencies, with one BLOCKER (abstract headline scalar without immediate provenance).
