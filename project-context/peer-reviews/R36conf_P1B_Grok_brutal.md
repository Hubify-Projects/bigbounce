# P1B R36conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.63.pdf` md5=e00d5028 pages=20
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 63.7s

---

**Referee Report**

**P1B-E1**  
**Section:** I (Introduction), p. 2  
**Problem:** The paper opens by declaring its scope as three “verification analyses” whose primary purpose is to document *null* results and *non*-tests (“Not a spin-torsion theory module”, “not a competitive sky detection”, “Not a distinctive ECH prediction”). No positive, theory-specific prediction of the ECH framework is derived or tested.  
**Required fix:** Either (a) withdraw and resubmit as a technical note/appendix to Paper I(a), or (b) supply a self-contained, falsifiable ECH prediction whose verification actually constitutes the scientific payload.

**P1B-E2**  
**Section:** Abstract-equivalent opening paragraph + §III (p. 3)  
**Problem:** The headline claim “\(\Delta N_{\rm eff}\) consistent with zero (−0.020 ± 0.169 …)” is presented as a load-bearing result. The body immediately states that the run uses unmodified CAMB with \(\Delta N_{\rm eff}\) as a free parameter and solves *no* torsion-modified Boltzmann equations. The number therefore tests nothing about ECH.  
**Required fix:** Remove the \(\Delta N_{\rm eff}\) posterior from every abstract-level claim and from Table I; retain only as an internal convergence diagnostic.

**P1B-E3**  
**Section:** §IV (p. 5–8) and Fig. 3  
**Problem:** The NaMaster pipeline-recovery exercise recovers injected \(\beta\) with a systematic floor \(|\Delta\hat\beta|\leq0.040^\circ\). The published observational value is \(\beta=0.342^\circ\pm0.094^\circ\) (3.6\(\sigma\)). The pipeline bias is therefore 43 % of the reported central value, yet the text repeatedly juxtaposes the two numbers without the explicit qualifier “not directly comparable” required by the review instructions.  
**Required fix:** Add the qualifier at every juxtaposition and recompute the effective significance after subtracting the measured bias floor in quadrature.

**P1B-E4**  
**Section:** §VI (p. 9–12) and Fig. 4  
**Problem:** The spectator-ALP consistency check is performed in standard GR + ALP; the text states explicitly that “the same birefringence arises in standard GR” and “is not a distinctive ECH prediction.” The entire section is therefore irrelevant to the ECH program it claims to support.  
**Required fix:** Delete §VI or move it to an appendix labeled “Illustration that the observed rotation is reproducible by a non-ECH model.”

**P1B-M1**  
**Section:** Throughout (especially pp. 2, 3, 9, 13)  
**Problem:** The manuscript is 20 pages long yet contributes only three null/technical checks. PRD page limits for Letters/Articles are routinely enforced; a 20-page verification note exceeds any reasonable allocation for this incremental content.  
**Required fix:** Reduce to ≤8 pages or withdraw.

**P1B-M2**  
**Section:** Data Availability (p. 13) and Appendix A  
**Problem:** Frozen-chain DOIs and commit hashes are listed as “pending.” The reproducibility manifest therefore cannot be audited by a standalone reader.  
**Required fix:** Supply permanent DOIs and exact git SHAs before resubmission.

**P1B-M3**  
**Section:** §II (p. 2) and Table I  
**Problem:** The two frozen dataset combinations are stated to give \(\Delta N_{\rm eff}\) posteriors “consistent with zero at <1\(\sigma\)”. The one-sided 95 % upper limits (0.40 and 0.31) are never reported in the table or abstract, violating the requirement that every quantitative claim carry its effect-size statement.  
**Required fix:** Add the one-sided limits to Table I and the abstract.

**P1B-N1**  
**Section:** Multiple figure captions (Figs. 1–3)  
**Problem:** Axis labels omit units on several derived quantities (e.g., \(\Delta N_{\rm eff}\) marginals).  
**Required fix:** Add explicit units.

**P1B-N2**  
**Section:** References  
**Problem:** Several citations (e.g., [5], [18]) quote numerical results whose provenance is the companion papers rather than the cited works themselves.  
**Required fix:** Either cite the companion papers directly or recompute the numbers from the public data.

**Summary recommendation**  
**REJECT**

The manuscript is a defensive technical appendix, not a self-contained scientific article. It repeatedly emphasizes that none of its numerical exercises actually test the ECH spin-torsion framework, contains no falsifiable ECH prediction, and is 2–3× longer than its incremental content warrants. These defects are structural and cannot be repaired by minor revision.