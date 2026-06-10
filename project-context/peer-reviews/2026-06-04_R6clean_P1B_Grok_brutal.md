# P1B 2026-06-04_R6clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 8.7s

---

**Referee Report**

**P1B-B1 (ESSENTIAL, Sec. I, p. 2)**  
Problem: The manuscript is a 10-page “technical verification companion” whose sole positive results are (i) a stock-CAMB \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) MCMC that recovers \(\Delta N_{\rm eff}=0\) at \(\lesssim0.4\sigma\) and (ii) a NaMaster pipeline that recovers an injected angle with a 0.032–0.040° bias. No new Boltzmann solver, no new likelihood, no new sky measurement, and no ECH-specific prediction is demonstrated. Ten pages for three null-consistency exercises exceeds any reasonable page allocation for a methods companion.  
Required fix: Condense to a 4-page (maximum 5-page) technical note. All narrative framing, repeated scope disclaimers, and appendix material that does not directly support the three numerical tests must be removed.

**P1B-M1 (MAJOR, Abstract & Sec. III, p. 2–3)**  
Problem: The abstract and introduction repeatedly state that the MCMC “is reported as a null-consistency test … not as evidence for or against the ECH spin-torsion framework.” This framing is honest but also reveals that the calculation supplies no new constraint on the theory the companion is meant to support. The paper therefore contains no load-bearing result for the ECH program.  
Required fix: Either (a) move the MCMC to a short appendix of Paper I(a) or (b) demonstrate that the same run with torsion-modified Boltzmann equations yields a distinguishable posterior. The present text does neither.

**P1B-M2 (MAJOR, Sec. IV, p. 5)**  
Problem: The NaMaster validation is explicitly labeled “a pipeline-validation figure, not a sky-detection significance claim.” The quoted 20.32\(\sigma\) and 25.71\(\sigma\) figures are MC recovery SNRs, not cosmological detections. Presenting these numbers in a cosmology journal paper without a dedicated “Methods” subsection that isolates them from sky results invites mis-citation.  
Required fix: Remove all SNR numbers from the main text and tables; retain only the bias values (0.032–0.040°) and state once that these are internal pipeline diagnostics.

**P1B-M3 (MAJOR, Sec. VI, p. 6–7)**  
Problem: The spectator-ALP section shows that \(\beta\approx0.27^\circ\) can be fit in standard GR+ALP with \(C_{a\gamma}\in[9,51]\) and a \(\sim25\times\) tuning of \(\theta_i\). The text correctly notes that this is “not a distinctive ECH prediction.” The calculation therefore adds no new evidence for the ECH framework and simultaneously highlights that the required photon coupling lies well outside KSVZ/DFSZ benchmarks.  
Required fix: Either delete the section or reframe it as an explicit upper limit on how much the ECH scenario can claim credit for the birefringence signal.

**P1B-M4 (MAJOR, Sec. V B, p. 6)**  
Problem: The \(w_0wa\) posterior is reported with marginal-tail departures of +4.3\(\sigma\) and −3.6\(\sigma\) from \(\Lambda\)CDM, yet the authors defer any Bayes-factor or \(\ln B\) calculation because the \(\Lambda\)CDM point lies outside the sampled region. A 4\(\sigma\) tension claim without a proper evidence ratio is not journal-ready.  
Required fix: Remove the \(\sigma\) tension language or supply a nested-sampling run that yields a controlled \(\ln B\).

**P1B-N1 (MINOR, Table I caption & text, p. 3)**  
Problem: The bias is first stated as “stable … at 0.032°” and later corrected to 0.040° for the \(\beta=0.342^\circ\) injection. The text does not propagate this amplitude dependence into the quoted systematic floor.  
Required fix: Adopt a single conservative floor (0.040°) and update all references.

**P1B-N2 (MINOR, throughout)**  
Problem: The manuscript contains an unusually large number of parenthetical scope disclaimers (“NOT a spin-torsion theory module,” “not a competitive sky detection,” etc.). While technically accurate, the defensive tone is excessive for a PRD article.  
Required fix: Reduce to one scope paragraph in the introduction; delete all subsequent repetitions.

**P1B-N3 (NIT, p. 2 & p. 8)**  
Problem: Footnote a and the reproducibility section contain minor date/version inconsistencies (“2026-04-29” vs. “April 2026”).  
Required fix: Standardize dates.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript is an honest but extremely thin technical appendix. Its three numerical exercises are correctly labeled as null results or pipeline checks and supply no new constraint on the ECH spin-torsion scenario. The present 10-page length is disproportionate to the scientific increment. A drastically shortened (≤5 page) version that removes all repeated disclaimers, marginal-tail tension language, and non-load-bearing appendices could be acceptable as a companion note; the current version is not.