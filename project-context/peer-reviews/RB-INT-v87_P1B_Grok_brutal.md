# P1B RB-INT-v87 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=ce73d67c pages=24
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 68.9s

---

**Referee Report**

**Paper**: Technical Reproducibility and Consistency-Check Companion to the ECH Spin-Torsion Program (P1B)

**Journal target**: Physical Review D

**Overall assessment**: The manuscript is a 24-page technical note whose explicit purpose is to document three null-consistency exercises that the authors repeatedly state do *not* test the Einstein–Cartan–Holst spin-torsion sector. The scientific payload is therefore limited to (i) a stock-CAMB \(\Delta N_{\rm eff}\) run, (ii) a synthetic-sky NaMaster pipeline bias measurement, and (iii) a spectator-ALP birefringence consistency check whose result is already known to arise in ordinary GR. No new physics, no new methodological advance, and no verification of the theory advertised in the title are claimed.

**P1B-E1 (ESSENTIAL)** — Page 1, abstract, lines 3–5  
The title and opening sentence advertise a “Spin-Torsion Program” while the body (abstract, §I, §III scope statement, §VI) repeatedly disclaims any test of that sector. This framing mismatch is unacceptable for PRD.  
*Required fix*: Retitle and rewrite the abstract to remove all reference to spin-torsion verification; the paper must stand as a pure technical-methods note.

**P1B-E2 (ESSENTIAL)** — Page 1–2, length vs. contribution  
24 pages (plus appendices) for three null cross-checks exceeds any reasonable PRD allocation for a reproducibility note. The literature frontier for pipeline-validation or spectator-ALP papers is typically 4–8 pages (e.g., Alonso et al. 2019, NaMaster papers).  
*Required fix*: Condense to Letter length (<8 pages) or withdraw and deposit as supplementary material to Paper I(a).

**P1B-E3 (ESSENTIAL)** — Abstract, Table I, Fig. 2  
The abstract quotes \(\Delta N_{\rm eff} = -0.020 \pm 0.169\) and \(+0.058 \pm 0.179\) as headline numbers. These are one-sided 95 % upper limits after post-processing truncation of the negative tail; the raw two-sided means are statistically consistent with zero at <0.2\(\sigma\). The abstract therefore presents a derived bound as a primary result without stating the truncation.  
*Required fix*: Remove the numerical values from the abstract or qualify them explicitly as “post-processed one-sided 95 % limits.”

**P1B-M1 (MAJOR)** — Page 7, Fig. 3 and §IV  
The NaMaster pipeline-recovery bias (\(\Delta\hat\beta \approx -0.032^\circ\) to \(-0.040^\circ\)) is presented beside the published 3.6\(\sigma\) sky measurement without a single sentence stating that the two numbers are *not* directly comparable (different foreground content, different mask, different noise). The paper elsewhere uses the phrase “not directly comparable,” but not at the critical juxtaposition.  
*Required fix*: Add an explicit, repeated qualifier at every location where pipeline SNR and sky significance appear together.

**P1B-M2 (MAJOR)** — Page 2, §I and all references to Paper I(a)  
The argument is not self-contained. Multiple load-bearing statements (“the 13 mechanism-class barriers,” the \(f_{\rm NL}=-35/8\) prediction, the four dark-energy channels) are imported by citation only. A standalone reader cannot evaluate the consistency-check claims without the companion.  
*Required fix*: Either make the paper fully self-contained or withdraw as a companion-only supplement.

**P1B-M3 (MAJOR)** — Page 5, Table I, footnote a  
The convergence metric \(\hat R-1\) values (0.001 and 0.003) are quoted after discarding the first 30 % of each chain. The raw pre-burn-in \(\hat R-1\) values are not shown. Standard PRD practice requires reporting both.  
*Required fix*: Add the pre-cut \(\hat R-1\) values and the Gelman–Rubin diagnostic on the full chains.

**P1B-N1 (MINOR)** — Page 1, header  
“(Dated: June 30, 2026)” is a future date. Cosmetic but must be corrected.

**P1B-N2 (MINOR)** — Page 8, Eq. (1)  
The \(\chi^2\) estimator is written without the conventional \(1/\sigma_b^2\) weighting factor that appears in the public NaMaster driver scripts. The text claims the form is “identical” to the public code; it is not.  
*Required fix*: Either restore the divisor or state the deliberate deviation.

**P1B-NIT1–NIT3**  
- Duplicate phrasing “canonical canonical-mask” does not appear.  
- No internal version tags (“R7”, “v1B.0.87”) are visible in the rendered body.  
- All arXiv IDs and years in the reference list match the cited papers’ metadata.

**Summary recommendation**  
**REJECT**

The manuscript is a defensive reproducibility note whose central claim is that it does *not* test the theory named in its title. The combination of (i) extreme length, (ii) framing mismatch, (iii) non-self-contained argument, and (iv) headline numbers that require post-processing caveats makes the paper unsuitable for PRD in its present form. The technical artifacts may be useful to the collaboration, but they belong in a repository or as supplementary material, not as a standalone 24-page article.