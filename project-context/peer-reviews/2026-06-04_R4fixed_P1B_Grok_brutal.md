# P1B 2026-06-04_R4fixed — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 11.2s

---

**Referee Report: P1B (Technical Verification Companion to the ECH Spin-Torsion Program)**

**P1B-E1 (ESSENTIAL) — Abstract, p. 1**  
Problem: The abstract states that the three analyses “support and contextualize” the ECH structural-closure results of Paper I(a), yet the body repeatedly declares that none of the three analyses actually tests the ECH framework (stock CAMB with no torsion modifications; birefringence identical in GR+ALP; spectator status requires fine-tuning unrelated to ECH).  
Required fix: Rewrite the abstract to state only what is actually demonstrated: two null-consistency tests in unmodified ΛCDM and one pipeline-validation exercise. Remove all language implying support for the ECH program.

**P1B-E2 (ESSENTIAL) — Throughout (multiple instances)**  
Problem: Internal review artifacts and version-history language remain in the body prose despite the “R4 fixed” claim. Examples: “the nested-sampling ln B recompute is queued”, “an earlier count erroneously quoted ‘98.6% quintom-B’”, “the 0.032° bias was initially characterized as strictly ‘stable across all three injections’ but…”, explicit chain dates (“2026-05-18 07:53 UTC”), file names (“stale.csv”, “latest.csv”, “iter2”), and reproducibility paths containing version tags (“paper1b-v1B.0.36”).  
Required fix: Remove every such phrase, date, filename, and “queued/recompute” reference. The manuscript must contain no audit tags or version history.

**P1B-E3 (ESSENTIAL) — Sec. III, p. 3 and Sec. V, p. 6**  
Problem: Multiple σ values derived from qualitatively different procedures (Metropolis-Hastings marginal-tail extrapolation at >4σ unsampled points, pipeline MC recovery SNR, literature 2.4–2.9σ sky detection) are presented without qualification that they are not on the same statistical scale.  
Required fix: Either remove all cross-comparisons of these σ figures or add an explicit statement that they cannot be compared directly.

**P1B-M1 (MAJOR) — Paper length and scope**  
Problem: The manuscript is 10 pages and consists entirely of (a) a stock-ΛCDM null test already known to be consistent with ΔN_eff = 0, (b) a NaMaster pipeline validation whose SNR figures are explicitly disclaimed as non-sky measurements, and (c) a GR+ALP consistency check whose result is also not ECH-specific. No new methodology, catalog, or ECH prediction is delivered.  
Required fix: Either expand to a genuine methods paper (≥15 pages) that contains novel, self-contained technical content, or withdraw and resubmit the material as a short technical note or appendix to Paper I(a).

**P1B-M2 (MAJOR) — Sec. VI and fn. 4**  
Problem: The spectator-ALP “consistency check” requires an explicit ∼25× fine-tuning of θ_i to remain in the spectator regime; the text acknowledges this but still presents the exercise as supportive of the ECH program. The same birefringence arises in standard GR.  
Required fix: Remove all framing that this check supports or is motivated by ECH; present it strictly as an external GR+ALP exercise with its tuning caveat stated in the abstract and conclusion.

**P1B-M3 (MAJOR) — Sec. V B and Appendix A**  
Problem: Model-comparison statistics (AIC, BIC, ln B) are repeatedly declared “deferred/queued/omitted” while the text still claims a “quintom-B signature” at +4.3σ / −3.6σ. No controlled evidence ratio is provided.  
Required fix: Either perform and report a proper nested-sampling evidence calculation on the identical likelihood stack, or remove every claim of preference or exclusion relative to ΛCDM.

**P1B-N1 (MINOR) — Table I caption and text**  
Problem: The caption and surrounding prose still contain reconciliation footnotes about burn-in fractions, getdist thinning, and exact post-burn-in counts that belong in supplementary material.  
Required fix: Move all such numerical bookkeeping to the reproducibility manifest; retain only the final posterior values in the table.

**P1B-N2 (NIT) — Multiple sections**  
Problem: Repeated use of the phrase “NOT a spin-torsion theory module” (or equivalent) functions as defensive boilerplate rather than scientific clarification.  
Required fix: Delete the repeated disclaimers; state the scope limitation once in Sec. I and once in the conclusions.

**P1B-N3 (NIT) — References and cross-citations**  
Problem: The manuscript cites four “in preparation” companion papers (I(a), II, III, IV) whose content is required to understand the present claims.  
Required fix: Make the present submission self-contained or clearly label it as a supplementary technical note to a single primary paper.

## Summary recommendation
**REJECT**

The manuscript is a 10-page collection of null tests and pipeline checks whose only positive results are already known (ΔN_eff consistent with zero, NaMaster recovers injected signals) and whose connection to the claimed ECH framework is explicitly disclaimed throughout. It contains multiple internal review artifacts, version-history language, and unqualified σ comparisons that violate PRD standards. The central claim that these analyses “support” the ECH program is not substantiated by the body. The paper cannot be rendered publishable by minor revision; it would require either wholesale removal of all ECH framing or merger into a single, substantially longer primary paper that actually delivers new ECH methodology.