# P1A R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P1A_v1A_0_35
**Wall time**: 87.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=30160, completion=5145, reasoning=4130, total=35305

---

## PAPER-GPT-B1 — BLOCKER

**Section:** LaTeX preamble comments; Sec. IV “Four-Route No-Go”; Sec. XII; Appendix B; Table `bounce_disc` footnote.  
**Issue:** Manuscript contains extensive audit-trail / AI-vendor / version-history prose: “OpenRouter unified API”, “GPT-5.5 / Gemini / Grok / Perplexity”, “R23 Gemini… closure”, “v1A.0.29 R8+R9”, “queued”, “running on a dedicated MPI pod”. This is not journal text and contaminates the scientific record.  
**Fix:** Purge all review-round, vendor, version, pod, queue, and “closure” prose from the body, appendices, tables, captions, and source comments before submission; retain only scientific derivations and reproducibility metadata.

## PAPER-GPT-B2 — BLOCKER

**Section:** Secs. II.A–II.C; Appendix B, Eq. `\ref{eq:onshell_rho}`.  
**Issue:** The central dark-energy scaling rests on an admitted non-EFT dimensional ansatz: the parity-odd operator has Lagrangian dimension `+1`, then is promoted by hand to `(\alpha/M) M_Pl^5` or `\alpha M_Pl^3/M`. The claimed `N_tot≈92`, `Xi≈10^-123`, and dark-energy “closure” are therefore not derived from ECH.  
**Fix:** Either construct a valid dimension-4 operator basis with explicit matching and coefficients, or demote all numerical `Λ_eff`, `Xi`, and `N_tot` claims to speculative dimensional estimates and remove theorem-level language.

## PAPER-GPT-B3 — BLOCKER

**Section:** Sec. IV, Route 2, Eq. after `\ref{eq:oneloop_parity_odd}`.  
**Issue:** The one-loop birefringence suppression calculation is not dimensionally or physically closed: the manuscript gives two “dimensionless” reductions differing by ~25–27 orders of magnitude (`10^-58–10^-60` vs `10^-33`) and never derives the photon Chern–Simons coupling from the Holst/fermion axial-current term. Using the R4-fitted `\alpha/M` in the denominator is not a derivation of the R2 amplitude.  
**Fix:** Derive the actual effective `\theta F\tilde F` coefficient and line-of-sight rotation with units fixed, then quote one unique marginalized amplitude ratio; otherwise remove Route-2 quantitative closure.

## PAPER-GPT-B4 — BLOCKER

**Section:** Abstract; Sec. IV “Scope” and “Closure summary”; Conclusions.  
**Issue:** The paper explicitly admits it is not an operator-basis closure and omits Jackiw–Pi gravitational Chern–Simons and parity-odd four-fermion operators, yet later says R1–R4 “exhaust” the minimal-ECH channels and “close every minimal-ECH dark-energy route.” This is a direct overclaim.  
**Fix:** Replace all “exhaust”, “every route”, “no-go theorem”, and “structural closure” wording with “the four enumerated channels considered here,” unless a complete diffeomorphism-invariant parity-odd/torsion EFT basis is actually enumerated and closed.

## PAPER-GPT-M1 — MAJOR

**Section:** Sec. X “Perturbation-Transparency Result”.  
**Issue:** The theorem is only proven for canonical scalar matter with zero spin density, but it is used rhetorically as a broad ECH perturbation closure even though minimal ECH effects require fermionic spin and the paper itself invokes reheating fermion baths and axial currents. Also, the Levi-Civita Holst contraction vanishes identically by Bianchi identity; calling it “topological”/“total derivative” is sloppy and misleading.  
**Fix:** State this as a conditional scalar-sector lemma only; add a separate spin-fluid/fermion perturbation analysis or remove its use as a general barrier for realistic SM cosmology.

## PAPER-GPT-M2 — MAJOR

**Section:** Abstract; Secs. VII, XIII, XIV; Conclusions.  
**Issue:** The SPHEREx `3–5σ` and “definitively erased” `f_NL` claims are imported without the Fisher data vector, covariance, nuisance marginalization, or bounce-to-inflation transfer calculation in this paper. The heuristic `e^{32}` physical-scale argument is insufficient to prove erasure of the bispectrum or to support model-discrimination significance.  
**Fix:** Either include the full forecast/mode-transfer calculation with nuisance propagation here, or cite it as external motivation only and remove “definitively”, “rules out”, and headline-significance language from this manuscript.
