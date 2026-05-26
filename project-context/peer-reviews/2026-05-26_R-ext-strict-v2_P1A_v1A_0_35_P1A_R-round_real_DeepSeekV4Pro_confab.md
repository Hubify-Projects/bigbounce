# P1A R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v2_P1A_v1A_0_35
**Wall time**: 125.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=28546, completion=6046, reasoning=4612, total=34592

---

# Peer Review Findings — Traceability Audit

## Finding PAPER-DEE-B1 (MAJOR)
**Section:** Abstract, §II.C, §XII.A  
**Scalar:** \(N_{\rm tot} \approx 92\)  
The abstract and conclusions present \(N_{\rm tot} \approx 92\) as the number of e‑folds required for the dark‑energy suppression mechanism—a load‑bearing figure supporting the structural‑tension claim. The paper does not cite or provide any JSON, script, notebook, or explicit step‑by‑step arithmetic that solves for \(N_{\rm tot}\) from the displayed ingredients (\(\rho_\Lambda \approx (2.3\,\text{meV})^4\), \([(\alpha/M)\MPl]\sim 10^{-2}\), \((T_{\rm reh}/M_{\rm GUT})^{3/2}\approx 0.03\)). The value is called “a fitted parameter” without a fitting procedure, and the repository URL points only to general reproducibility materials, not to a file that produces \(N_{\rm tot}=92\). This makes the number unreproducible from the paper’s own information and breaks provenance for a central claim.  
**Fix:** Add an appendix or a linked script (e.g., `compute_Ntot.py` within the reproducibility directory) that performs the matching calculation with explicit input values, or provide the full arithmetic in a transparent table that readers can verify.

---

## Finding PAPER-DEE-B2 (minor)
**Section:** §VII, §XIII (Conclusions)  
**Scalar:** \(3\,\text{--}\,5\sigma\) realistic SPHEREx significance for \(f_{\rm NL} = -35/8\)  
The paper asserts that SPHEREx will test the matter‑bounce prediction at \(3\,\text{--}\,5\sigma\) realistic significance, but the derivation of this range is spread across footnotes, references to Heinrich+2024, and qualitative estimates of GR‑projection, \(b_\phi\) uncertainty, and photo‑\(z\) degradation. No single table or script shows how the raw Fisher‑ideal \(6.25\sigma\) is degraded step‑by‑step to the claimed \(3\,\text{--}\,5\sigma\) interval; the numbers in footnote~\ref{fn:spherex_range} are hand‑wavy and cannot be reproduced without replicating the full Paper~II Fisher forecast.  
**Fix:** Either move the exact sensitivity derivation to an appendix with a transparent calculator, or restrict the abstract to the Fisher‑ideal \(\sigma(f_{\rm NL})\approx 0.7\) and defer the coherent significance calculation to Paper~II, quoting only the bound that is directly derivable from the cited Heinrich forecast.

---

## Finding PAPER-DEE-B3 (minor)
**Section:** §XIII (Conclusions), §II.C  
**Scalar:** \(\beta \approx 0.27^\circ\)  
The spectator‑ALP birefringence value \(\beta\approx 0.27^\circ\) is repeatedly stated as a consistency check. No script, inline calculation, or parameter input listing (ALP mass, decay constant, coupling) is given to produce \(0.27^\circ\); the companion Paper~I(b) is cited for ALP MCMC fitting, but a traceable provenance should at least point to the exact file or commit that yields this central value. As it stands, a reader cannot confirm that \(0.27^\circ\) follows from the stated setup without guessing the ALP parameters.  
**Fix:** Add a brief appendix or a cross‑reference to the specific script/commit in the repository (e.g., `albiref/run_spectator_alp.py`) that outputs \(\beta=0.27^\circ\), with the associated parameter values.

---

## Finding PAPER-DEE-B4 (minor)
**Section:** §II.C.3 (Reheating thermal‑reset and \(\Dinf\) prefactor)  
**Scalars:** \(T_{\rm reh} \approx 10^{15}\,\text{GeV}\), \(M_{\rm GUT} \approx 10^{16}\,\text{GeV}\), \((T_{\rm reh}/M_{\rm GUT})^{3/2} \approx 0.03\)  
The numerical estimates for reheating temperature and GUT scale are asserted without citation or provenance; they directly enter the prefactor that scales \(\Dinf\) and therefore \(N_{\rm tot}\). The paper acknowledges the prefactor is an order‑of‑magnitude aesthetic, but the specific numbers \(10^{15}\,\text{GeV}\) and \(10^{16}\,\text{GeV}\) are not linked to any theoretical or observational source.  
**Fix:** Provide a reference for the canonical GUT‑scale and reheating‑temperature ranges, or replace the single numerical example with a parametric expression and demonstrate that the resulting \(N_{\rm tot}\) is insensitive to the precise choice within the regime.

---

## Finding PAPER-DEE-B5 (nit)
**Section:** §II.D  
**Scalar:** “underpredicts \(A_0\) by \(>100\) orders of magnitude”  
The claim that the ECH coupling underpredicts galaxy spin asymmetry by more than 100 orders of magnitude appears without any supporting numeric estimate of the expected asymmetry amplitude. No arithmetic or script computes this factor; it is presented as a qualitative comparison. This does not affect the core argument, but if a quantitative bound is claimed, it should be traceable.  
**Fix:** Either provide the order‑of‑magnitude calculation (parity‑odd coupling strength, typical spin‑density at galaxy scales, and resulting asymmetry) as a footnote or remove the specific “\(>100\)” quantification, keeping only the statement that the observed null is consistent with the suppressed coupling.

---

## Finding PAPER-DEE-B6 (nit)
**Section:** Abstract (line “13 logically‑independent mechanism‑class constraints”)  
**Scalars:** number of constraints (13 independent / 14 catalogue entries)  
The abstract and body describe the barrier catalogue as containing 14 entries but only 13 logically‑independent constraints because B8 is subsumed by B14. The counting is explained, but no machine‑readable artefact (e.g., a dependency graph file or a script that asserts independence) is referenced to verify that exactly 13 constraints are logically independent. This is a cosmetic provenance gap that does not affect the physics.  
**Fix:** Optionally add a small JSON/YAML file in the reproducibility folder that lists the barriers and their dependence relationships, or simply accept that the counting is transparent enough as prose.

---

*No BLOCKER‑grade findings. The most pressing issue is the untraceable derivation of the headline e‑fold number; all other numerical claims are either recoverable from cited literature or could be made traceable with modest additions.*
