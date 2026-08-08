# P1B R54 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R54_P1B/paper1b_mcmc_companion.pdf` md5=0b4a8768 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 254.8s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (Houston Golden)

**Journal target:** Phys. Rev. D

**Date of review:** 2025 (simulated)

**P1B-E1 (ESSENTIAL, Abstract + p. 1)**  
The abstract states “the \(\Delta N_{\rm eff}\) extension does not reduce the residual \(\sim 3.6\sigma\) tension” and quotes specific posteriors (\(-0.020\pm0.169\), \(+0.058\pm0.179\)). These numbers are only traceable to the frozen chains in Table I (p. 5). No independent recomputation or covariance propagation from the quoted Planck+BAO+SN likelihoods is supplied. The abstract therefore presents derived numbers whose provenance cannot be audited from the text alone.  
**Required fix:** Move the numerical results out of the abstract or supply an explicit one-line derivation from the GetDist output files cited in the reproducibility section.

**P1B-E2 (ESSENTIAL, p. 1–2 and throughout)**  
The entire scientific framing (“ECH spin-torsion program”, “Paper I(a)”) is imported by citation to a companion that is not supplied. The standalone-reader test fails for every claim that begins “the ECH framework provides motivation…”. Undefined symbols (\(f_{\rm NL}\), Holst sector, \(\alpha_{\rm EM}\)) appear before they are defined.  
**Required fix:** Either embed the minimal theoretical definitions or reduce the manuscript to a pure technical note whose title and abstract make no reference to un-supplied theory.

**P1B-E3 (ESSENTIAL, p. 3, §III scope statement)**  
The paper repeatedly asserts “NOT a spin-torsion theory module” and “NOT a competitive sky detection”. These disclaimers are required because the title and abstract still advertise the ECH program. The resulting rhetorical structure is internally inconsistent.  
**Required fix:** Retitle and re-scope the manuscript as “Technical verification of two public pipelines on synthetic CMB data” and remove all ECH framing.

**P1B-M1 (MAJOR, p. 21)**  
21 pages for a verification companion whose headline results are null (no \(\Delta N_{\rm eff}\) detection, pipeline bias \(\sim0.03^\circ\)) violates PRD length norms for methods notes. The recommended maximum is 8–10 pages.  
**Required fix:** Condense to a Letter or withdraw and resubmit as a shorter Methods note.

**P1B-M2 (MAJOR, Fig. 1 & Table I)**  
The corner plot and Table I report \(\Delta N_{\rm eff}\) posteriors under two different dataset combinations whose likelihoods differ only by the addition of the SH0ES \(M_B\) anchor. No \(\Delta\chi^2\) or evidence ratio is given; the reader cannot judge whether the shift from \(-0.020\) to \(+0.058\) is statistically meaningful.  
**Required fix:** Add a quantitative model-comparison statistic or state explicitly that none is claimed.

**P1B-M3 (MAJOR, p. 9–10, NaMaster validation)**  
The pipeline-recovery bias (\(\Delta\hat\beta=-0.032^\circ\) to \(-0.040^\circ\)) is presented as a “systematic floor”. No propagation of this bias into the final \(\beta\) uncertainty budget is performed, nor is it folded into the quoted 3.6\(\sigma\) literature value.  
**Required fix:** Supply a revised uncertainty on \(\beta_{\rm obs}\) that includes the measured pipeline bias.

**P1B-N1 (MINOR, p. 1 header)**  
The date “June 20, 2026” is chronologically impossible for a 2025 submission.  
**Required fix:** Correct.

**P1B-N2 (MINOR, multiple tables)**  
Several tables quote “worst \(\hat R-1\)” and “min ESS” but never define the convergence threshold used to declare the chains “frozen”.  
**Required fix:** State the numerical threshold once.

**P1B-N3 (NIT)**  
Inconsistent use of “full-tension” vs. “Planck+BAO+SN” column labels between Table I and the text on p. 4. Cosmetic.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript is a conscientious but over-long technical appendix whose central results are null or negative. In its present form it cannot stand alone, exceeds reasonable length for a verification note, and imports its scientific motivation from an unavailable companion. The required changes (self-contained scope, drastic length reduction, explicit propagation of pipeline bias, removal of un-auditable abstract numbers) are structural rather than cosmetic. After those revisions the work might be publishable as a short Methods or Data Release note, but not in its current 21-page companion-paper format.