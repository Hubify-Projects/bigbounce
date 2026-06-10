# P1B 2026-06-04_1814pt — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 12.3s

---

**Referee Report: HUBIFY-2026-001B**

**P1B-B1 (ESSENTIAL)**  
Section: Entire manuscript (title page through Conclusions, multiple instances)  
Problem: The manuscript contains pervasive version-history language, internal audit tags, review-log artifacts, and development-state prose that are incompatible with a journal submission. Examples include “Dated: 2026-06-03 PDT — v1B.0.42”, “R-upgraded-round4 GEM-m2”, “corrected fire #25”, “queued for v1B.0.15+”, “audit on-record at shoes yaml audit.md”, “R12 GEM-M2 closure”, “CONVERGED … log marker MCMC DONE ITER2 OMP6 written at 2026-05-18 07:53 UTC”, “in flight for Paper I(a) Table II”, and repeated references to “wave-14 cross-paper snapshot.”  
Required fix: Remove every such phrase, date stamp, version tag, file-path reference, and “queued/in-flight/pending” statement. The text must read as a finished, static scientific document.

**P1B-B2 (ESSENTIAL)**  
Section: Abstract and Sec. I (Introduction)  
Problem: The abstract and introduction frame the work as “technical verification material for the ECH spin-torsion cosmology no-go program,” yet the body repeatedly states that none of the three analyses tests the ECH framework, modifies the Boltzmann equations, or produces an ECH-specific prediction. The abstract therefore misrepresents what the paper actually proves.  
Required fix: Rewrite the abstract and introduction to state unambiguously that the paper reports three null-consistency and pipeline-validation exercises performed in standard GR/ΛCDM, none of which constitutes a test or prediction of the ECH model.

**P1B-B3 (ESSENTIAL)**  
Section: Sec. V B and Table II  
Problem: The paper presents marginal-tail extrapolations labeled “+4.3σ” and “−3.6σ” from the LCDM point while simultaneously stating that the LCDM point lies outside the sampled region and that no robust Bayes factor or Savage-Dickey ratio can be computed. Presenting these figures as headline departures without the required model-comparison statistic is misleading.  
Required fix: Remove or clearly qualify all σ-departure claims from the unsampled LCDM point; report only the actual posterior means and credible intervals until a proper nested-sampling run supplies a controlled evidence ratio.

**P1B-M1 (MAJOR)**  
Section: Overall manuscript length and scope  
Problem: At 12 pages the paper is almost entirely occupied by scope disclaimers, convergence diagnostics, and cross-paper status tables whose content is either null results or pipeline checks already qualified as non-competitive. This length is disproportionate to the claimed contribution.  
Required fix: Condense to a concise methods note (maximum 6–7 pages) or withdraw and incorporate only the essential numerical results into Paper I(a).

**P1B-M2 (MAJOR)**  
Section: Sec. VI and footnotes 3–4  
Problem: The spectator-ALP consistency check is presented as supporting the observed birefringence while the text simultaneously discloses that the spectator regime requires ∼25× fine-tuning of θᵢ and that the same signal arises in ordinary GR. The net scientific content is therefore a parameter-space consistency statement, not a new result.  
Required fix: Reframe the section as a brief parameter-range check with explicit tuning caveat; remove any implication that the exercise validates or motivates the ECH program.

**P1B-M3 (MAJOR)**  
Section: Sec. VII and Table III  
Problem: The cross-paper verification table and associated prose contain live development tracking (“74 %”, “67 %”, “readiness”, “Houston external review ongoing”) that belongs in an internal project log, not a journal article.  
Required fix: Delete the entire table and subsection; any necessary cross-references must be limited to static citations of published or accepted companion papers.

**P1B-N1 (MINOR)**  
Section: Table I caption and footnote a  
Problem: The convergence footnote mixes diagnostic details (“stale.csv”, “gpu 20260305”) with scientific results.  
Required fix: Move all diagnostic file names and intermediate R̂ values to supplementary material or delete.

**P1B-N2 (MINOR)**  
Section: Multiple footnotes (e.g., footnote 1, 2, 4)  
Problem: Several footnotes contain lengthy arithmetic reconciliations and prior-version error corrections that interrupt the scientific narrative.  
Required fix: Shorten or remove; retain only information essential to the final reported numbers.

**P1B-N3 (NIT)**  
Section: Reference list and appendix headings  
Problem: Appendix labels and some reference strings contain internal project tags (“hUBIFY-2026-001A”).  
Required fix: Normalize to standard journal format.

## Summary recommendation
**REJECT**

The manuscript is an internal technical-verification log rather than a finished journal article. It contains extensive version-control language, audit artifacts, and “queued” items that must be expunged before any editorial consideration. Even after such cleaning, the scientific content consists of three explicitly null or non-competitive exercises whose scope limitations are stated so strongly that they negate the rationale for a separate 12-page PRD submission. The work should either be withdrawn or reduced to a short methods paragraph inside Paper I(a).