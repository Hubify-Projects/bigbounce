# P1B R10v3p1 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 57.0s

---

**Referee Report**

**P1B-E1** (ESSENTIAL)  
Section I (p. 2) and §III (p. 3): “Not a spin-torsion theory module. … no torsion modifications … The MCMC therefore tests whether the data prefer an extra radiation-like degree of freedom, treated as a generic phenomenological proxy … It does not verify the spin-torsion theory module itself.”  
The manuscript is submitted as the technical companion to an ECH spin-torsion program yet contains no ECH-modified Boltzmann solver, no photon-torsion coupling, and no derived ECH prediction. All reported chains are stock CAMB. A paper whose central claim is “we did not test the theory” fails PRD’s requirement for substantive original contribution.

**P1B-E2** (ESSENTIAL)  
Abstract (p. 1) and §VI (p. 6): The 3.6σ birefringence signal is taken verbatim from Eskilt & Komatsu (2022) and is reproduced by a spectator ALP in ordinary GR. The text states explicitly that the same β ≈ 0.27° “arises in any GR+ALP setup” and “is not a distinctive ECH prediction.” The only numerical result offered for the ECH program is therefore known to be theory-independent. This directly contradicts the framing that the work verifies the ECH program.

**P1B-E3** (ESSENTIAL)  
Abstract (p. 1) and Table I (p. 3): Both ΔN_eff posteriors are reported as “consistent with zero.” The paper simultaneously claims these runs constitute a “null-consistency test” for the ECH framework. Because the runs contain no ECH physics, the consistency with zero cannot be interpreted as a test of ECH. The abstract therefore misrepresents what has been tested.

**P1B-M1** (MAJOR)  
§IV (p. 5) and Eq. (1): The NaMaster pipeline recovery is performed on a foreground-cleaned Commander map with an injected MC signal; the recovered SNR values (20.32, 25.71) are stated to be “not competitive sky measurements.” The section is labeled a “bias-injection Monte Carlo validation,” not a cosmological result. Its inclusion as a numbered section in a PRD article is disproportionate to its methodological-check character.

**P1B-M2** (MAJOR)  
Table II (p. 4) and surrounding text: The w0wa posterior is obtained from a 17-parameter chain whose LCDM point (w0, wa) = (−1, 0) lies >4σ outside the sampled region. The Savage-Dickey ratio is therefore unusable, and the paper defers all Bayes-factor or information-criterion comparisons to a future nested-sampling run that is not performed. No quantitative model-comparison statistic is supplied for the central claim.

**P1B-M3** (MAJOR)  
Page-count vs. content: The manuscript is 10 pages long (plus appendices) yet consists almost entirely of (a) disclaimers that nothing tests ECH, (b) reproduction of a published 3.6σ ALP result, and (c) a stock-CAMB radiation-proxy run whose null outcome was expected a priori. PRD standards for a 10-page article are not met.

**P1B-N1** (MINOR)  
Fig. 1 caption (p. 5) and Table I footnote a: The post-burn-in count is given as 119,617 in the figure and 123,368 in the table footnote; the two numbers are not reconciled in the text.

**P1B-N2** (MINOR)  
Abstract (p. 1): “Dated: 2026-06-03 PDT.” A future date appears in the header of a manuscript under review.

**P1B-N3** (NIT)  
Multiple instances of “full-tension” and “Planck+BAO+SN” labels are used without an explicit statement that the two dataset combinations are not statistically independent, so the two ΔN_eff numbers cannot be averaged or directly compared.

**Summary recommendation**  
REJECT

The manuscript is a technical appendix that repeatedly and explicitly states it performs no test of the Einstein-Cartan-Holst theory it purports to support. All quantitative results are either (i) null outcomes from unmodified CAMB, (ii) reproductions of previously published ALP birefringence constraints, or (iii) pipeline-validation exercises whose authors themselves label non-competitive. Under PRD’s acceptance criteria this does not constitute a sufficient original contribution.