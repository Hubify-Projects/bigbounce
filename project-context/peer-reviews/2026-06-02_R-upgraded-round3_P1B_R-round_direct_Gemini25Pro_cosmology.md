# P1B R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 70.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=32004, completion=827, total=40689

---

No blocker-grade findings. The paper's extensive, explicit disclaimers and caveats correctly wall off the scope of each analysis, and the core numerical work appears sound. The following MAJOR and minor findings address remaining theoretical inconsistencies and presentation issues.

## PAPER-GEM-B1: BLOCKER
**Section:** VI and Appendix C
**Issue:** The "spectator" ALP model with $f_a \sim \MPl$ and $m \sim H_0$ is inconsistent with its assumed spectator status. Its energy density, $\rho_a \sim \frac{1}{2} m^2 (f_a \theta_i)^2 \sim H_0^2 \MPl^2$, is of the order of the critical density today, meaning it must be the dark energy, not a spectator. This contradicts the entire framing of the analysis, which treats the ALP as a decoupled component and uses separate MCMC runs for the background cosmology.
**Fix:** Re-frame the analysis to treat the ALP as a dark energy candidate and perform a single, self-consistent MCMC fit that simultaneously constrains the ALP parameters using both the expansion history data (Planck, BAO, SN) and the birefringence data. Alternatively, explicitly restrict the parameter space (e.g., $\theta_i \ll 1$) to ensure the ALP energy density is dynamically negligible, and acknowledge this constitutes fine-tuning.

## PAPER-GEM-M1: MAJOR
**Section:** VI, L898
**Issue:** The claim that the required coupling $C_{a\gamma} \sim 9$ "sits within standard GUT-scale / DFSZ benchmark ranges" is incorrect. Standard QCD axion models (KSVZ, DFSZ) predict $|C_{a\gamma}| \sim \mathcal{O}(1)$; a value of 9 is significantly larger and requires non-minimal model building.
**Fix:** Rephrase to state that $C_{a\gamma} \sim 9$ is larger than typical benchmark values but can be accommodated in certain classes of extended models. Remove the misleading reference to "standard GUT-scale / DFSZ" ranges.

## PAPER-GEM-m1: minor
**Section:** V (L867-872), VIII (L974-979), Appendix A (L1019-1022)
**Issue:** The text contains multiple instances of meta-commentary on the paper's internal review and version history (e.g., "removed in v1B.0.7 per the 3-vendor convergent R2 BLOCKER"). This audit-trail language is inappropriate for the body of a scientific paper.
**Fix:** Remove all references to internal version numbers, review rounds, and vendors from the main text and footnotes. State the scientific rationale for choices without referencing the revision process.

## PAPER-GEM-m2: minor
**Section:** VII, Table II
**Issue:** The cross-paper status table is severely outdated. It lists the current paper (P1b) as v1B.0.13, while the document's preamble and title block correctly identify it as v1B.0.38.
**Fix:** Update all version numbers and readiness percentages in Table II to be current at the time of submission.

## PAPER-GEM-m3: minor
**Section:** IV, L805
**Issue:** The NaMaster pipeline validation, performed on a Planck map, uses Monte Carlo realizations with ACT-level noise, which is higher than Planck's. The justification "conservative worst-case bias check" is unclear, as the noise model should typically match the data to accurately characterize the pipeline's performance on that specific dataset.
**Fix:** Clarify the rationale for using a mismatched noise model. Alternatively, and preferably, re-run the MCs with a noise model representative of the Planck Commander map.
