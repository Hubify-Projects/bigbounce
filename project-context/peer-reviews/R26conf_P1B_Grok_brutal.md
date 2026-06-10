# P1B R26conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.53.pdf` md5=86261d4b pages=16
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 88.6s

---

**Referee Report**

**P1B-E1 (ESSENTIAL)**  
**Section:** Abstract (p. 1) + Table I (p. 4)  
**Problem:** Abstract states “\(\Delta N_{\rm eff}=-0.020\pm0.169\) (full-tension)” and “\(+0.065\pm0.17\) (Planck+BAO+SN)”. These numbers are reproduced in Table I, but the table caption and surrounding text explicitly label the run “stock CAMB … *no torsion modifications*” and “Not a Spin-Torsion Theory Module” (repeated in Sec. III, p. 3). The abstract therefore presents a null-consistency test as though it were a verification of the ECH framework.  
**Required fix:** Rewrite abstract to state unambiguously that the \(\Delta N_{\rm eff}\) run is a *standard-radiation* proxy test only; remove any implication that it constrains the spin-torsion sector.

**P1B-E2 (ESSENTIAL)**  
**Section:** Multiple locations (pp. 2, 3, 9, 10, 11)  
**Problem:** Repeated internal editing language: “Correction note: an earlier quoted…”, “an earlier draft paired \(\Delta\phi/f_a\approx1.0-1.07\)”, “Correction note: an earlier draft described the model-dependent fits as…”, “an earlier draft quoted [0.17,0.43]°”. These are version-control artifacts that have no place in a submitted manuscript.  
**Required fix:** Delete every sentence containing “earlier draft”, “correction note”, or equivalent revision history.

**P1B-E3 (ESSENTIAL)**  
**Section:** Sec. VI (pp. 9–11) and Appendix C (p. 14)  
**Problem:** The headline birefringence result \(\beta_{\rm ALP}=0.336^\circ\pm0.10^\circ\) (\(C_{a\gamma}=8\)) is obtained only after imposing the *ad-hoc* spectator cut \(\theta_i\le0.1\) (fn. 5 and text on p. 10). The paper simultaneously states that this cut is required to keep the ALP “spectator” and that the same numerical value arises in ordinary GR+ALP. The claim that the result constitutes a “consistency check with a Spectator-ALP model” for the ECH program is therefore unsupported.  
**Required fix:** Either (a) remove the spectator-consistency claim or (b) demonstrate that the \(\theta_i\le0.1\) cut follows from the ECH action rather than being inserted by hand.

**P1B-M1 (MAJOR)**  
**Section:** Sec. IV (pp. 6–8) and Fig. 3  
**Problem:** The NaMaster pipeline-recovery bias is reported as \(-0.032^\circ\) (at \(\beta_{\rm inj}=0.27^\circ\)) and \(-0.040^\circ\) (at \(0.342^\circ\)). The text asserts this bias is “amplitude-independent at \(\sim12\%\)”. The two quoted biases give \(0.032/0.27=0.119\) and \(0.040/0.342=0.117\), but the paper never shows that the *same* fractional bias holds across the full range of injected amplitudes or masks used in the literature. The 12 % figure is therefore an extrapolation, not a demonstrated result.  
**Required fix:** Provide a table or plot of recovered bias versus injected amplitude over at least five values, or qualify the 12 % statement as an interpolation valid only inside the two tested points.

**P1B-M2 (MAJOR)**  
**Section:** p. 16 (bibliography) + text on p. 1  
**Problem:** The paper cites “Eskilt & Komatsu 2022” (arXiv:2205.13962) for the 3.6\(\sigma\) birefringence detection, yet simultaneously states that the present analysis uses the *same* public likelihood and does *not* re-analyze the EB spectra. The citation is therefore used to claim a detection significance that the present work never recomputes.  
**Required fix:** Either recompute the significance on the exact likelihood employed here or remove the 3.6\(\sigma\) claim from the abstract and introduction.

**P1B-M3 (MAJOR)**  
**Section:** Entire manuscript length (16 pages)  
**Problem:** The paper is a “technical verification companion” whose principal results are three null or consistency tests, each accompanied by explicit disclaimers that it does *not* test the ECH spin-torsion sector. Sixteen pages is disproportionate to the incremental contribution.  
**Required fix:** Condense to \(\le8\) pages or justify the length by adding a genuine, non-null test of the Holst-sector predictions.

**P1B-N1 (MINOR)**  
**Section:** Table I footnote a (p. 4)  
**Problem:** Footnote states “the \(\pm0.018\) width could not be traced to any committed analysis”. This is an internal bookkeeping remark.  
**Required fix:** Delete or rephrase as a standard erratum note.

**P1B-N2 (MINOR)**  
**Section:** Fig. 1 caption (p. 6)  
**Problem:** Caption claims “\(\Delta N_{\rm eff}\) posterior is consistent with zero”, yet the plotted 1\(\sigma\) interval is \([-0.189,+0.149]\). The statement is technically correct but visually misleading because the posterior visibly peaks away from zero.  
**Required fix:** Add “within 1\(\sigma\)” to the caption.

**P1B-NIT1 (NIT)**  
**Section:** Multiple “Scope of …” paragraphs  
**Problem:** Overuse of defensive scope statements (“Not a spin-torsion theory module”, “Not a competitive sky detection”, etc.). These are repetitive and interrupt the scientific narrative.  
**Required fix:** Consolidate into a single, short “Scope and limitations” paragraph at the end of the introduction.

**Summary recommendation**  
**REJECT**

The manuscript contains multiple instances of internal editing artifacts (“earlier draft”, “correction note”) that are unacceptable in a submission to *Physical Review D*. In addition, the central framing—presenting a stock-CAMB null test and a spectator-ALP consistency check as technical verification of the ECH spin-torsion program—is misleading, as the paper itself repeatedly states that neither analysis actually probes the Holst sector. The length is excessive for the incremental, heavily caveated content. These are first-read grounds for rejection; even after removal of the editing artifacts, the scientific contribution would still require major reframing and condensation before resubmission.