# P1B EXT19 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=135fdfb4 pages=21
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 71.2s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (P1B)

**Journal target:** Phys. Rev. D

**Date of review:** Round EXT19

**Overall assessment:** The manuscript is a 21-page defensive technical appendix whose primary function is to document null results and to repeatedly disclaim that the reported signals are *not* predictions of the ECH framework. It does not meet the standard for a standalone PRD article.

**ESSENTIAL findings (must be fixed before any further consideration)**

**P1B-E1**  
Section: Title page (unnumbered)  
Problem: Header contains “(Dated: June 14, 2026)”. This is a future date relative to any possible submission.  
Required fix: Remove or correct the date. Internal version-control strings have no place in a submitted manuscript.

**P1B-E2**  
Abstract, lines 4–6 and §III (p. 3)  
Problem: The abstract states that both frozen dataset combinations “find \(\Delta N_{\rm eff}\) consistent with zero (−0.020 ± 0.169 …)”. The one-sided 95 % upper limit quoted later in the same paragraph (\(\Delta N_{\rm eff} < 0.31\)) is obtained only after an ad-hoc renormalization of the posterior that discards the negative tail. No such renormalization is mentioned in the abstract.  
Required fix: Either remove the one-sided limit from the abstract or state the renormalization procedure in the abstract itself.

**P1B-E3**  
§IV (p. 6) and Fig. 3 caption  
Problem: The pipeline-recovery bias \(\hat\beta - \beta_{\rm inj}\) is reported as −0.032° to −0.040° and is carried forward as “the observed NaMaster pipeline bias”. The text simultaneously states that this bias “is not a competitive sky measurement”. The two statements are in direct logical conflict; a number cannot be both “the observed bias” that must be subtracted and “not a measurement”.  
Required fix: Remove all quantitative use of the recovered angle as a sky observable or explicitly label it an upper bound on systematic floor only.

**P1B-E4**  
§VI (p. 10–13) and Table IV  
Problem: The spectator-ALP “consistency check” is performed inside a parameter subspace that requires a \(\sim 25\times\) fine-tuning of the initial misalignment angle relative to the natural prior midpoint (\(\theta_i \sim 0.1\) vs. 0.5). The paper never quantifies the prior volume penalty or the look-elsewhere effect incurred by this tuning.  
Required fix: Either drop the claim that the model “accommodates” the observed signal or supply the Occam factor / Savage–Dickey ratio for the tuned subspace.

**P1B-E5**  
Abstract + §I (p. 2)  
Problem: The abstract headline result (“both frozen dataset combinations find \(\Delta N_{\rm eff}\) consistent with zero”) is presented without the explicit qualifier that appears in the body: “NOT a spin-torsion theory module”. A reader of the abstract alone cannot know that the calculation does not test the actual ECH Boltzmann hierarchy.  
Required fix: Insert the scope limitation into the abstract or remove the \(\Delta N_{\rm eff}\) result from the abstract.

**MAJOR findings**

**P1B-M1**  
Length vs. claimed contribution (entire manuscript)  
The paper is 21 pages of “we did not detect anything new and the signals we recovered are not unique to ECH”. PRD length guidelines for a methods/verification companion are normally \(\leq 10\) pages. No new observable, no new constraint stronger than existing literature, and no positive detection are presented.

**P1B-M2**  
§V.B (p. 9) and Table I  
The headline statement “the \(\Delta N_{\rm eff}\) extension does not resolve the Hubble tension” is supported only by two frozen chains whose \(H_0\) posteriors are Planck-dominated. The paper never shows the joint posterior when the SH0ES likelihood is given equal weight. The claim is therefore an artifact of the chosen weighting, not a robust result.

**P1B-M3**  
Fig. 1 and Fig. 2  
The corner plot and \(\Delta N_{\rm eff}\) marginals are shown only for the two frozen combinations. The full-tension chain (119 617 post-burn-in samples) is never displayed. A reader cannot judge whether the reported consistency with zero survives the inclusion of the SH0ES anchor that drives the tension the paper claims to test.

**MINOR / NIT findings (selected)**

**P1B-N1**  
Multiple instances of the phrase “not a distinctive ECH prediction” (pp. 2, 10, 14) constitute repetitive defensive framing rather than scientific content.

**P1B-N2**  
Table III lists “Status” column entries that include internal repository paths (“reproducibility/…”) visible to the reader; these should be removed from the published version.

**P1B-N3**  
Equation (1) uses an unweighted \(\chi^2\) even though the text later demonstrates that an inverse-variance weighting changes the recovered angle by 0.006°. The choice is not justified.

**Summary recommendation: REJECT**

The manuscript is a methods appendix masquerading as a journal article. Its central results are either null findings already bounded by existing data or are obtained inside subspaces whose prior penalties are never quantified. The repeated, explicit disclaimers that the calculations do not test the actual ECH theory remove the only conceivable motivation for publication. The combination of excessive length, future-date artifact, abstract–body mismatch on scope limitations, and absence of any positive, reproducible advance places the paper well below the acceptance threshold of Physical Review D.