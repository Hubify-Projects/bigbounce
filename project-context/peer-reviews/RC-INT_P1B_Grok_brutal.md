# P1B RC-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=0b1108a9 pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 194.0s

---

**Referee Report for P1B (RC-INT)**

**P1B-E1 (ESSENTIAL)**  
Section: Abstract (p. 1) + §III (p. 3)  
Problem: Abstract states “\(\Delta N_{\rm eff}\) consistent with zero (−0.020 ± 0.169 full-tension)” and presents this as a load-bearing verification result. Body (§III, scope statement) explicitly declares the run “NOT A SPIN-TORSION THEORY MODULE” and uses unmodified CAMB with \(\Delta N_{\rm eff}\) as a free parameter only. The quoted number therefore tests nothing claimed by the ECH framework.  
Required fix: Remove the numerical claim from the abstract or qualify it at every occurrence with the explicit statement that the exercise has zero sensitivity to the ECH sector.

**P1B-E2 (ESSENTIAL)**  
Section: Abstract + §I (p. 2–3)  
Problem: Abstract and introduction repeatedly cite “Paper I(a)” for the 13 mechanism-class barriers, the perturbation-transparency theorem, and the \(f_{\rm NL}=-35/8\) prediction. No derivation or even schematic appears here. Standalone-reader test fails.  
Required fix: Either embed the minimal derivations or withdraw the paper as supplementary material.

**P1B-E3 (ESSENTIAL)**  
Section: §VI (p. 13–16) + Fig. 4  
Problem: The “spectator-ALP consistency check” recovers \(\beta\approx0.28^\circ\) only after imposing \(\theta_i\le0.1\) (a \(\sim25\times\) fine-tuning relative to the natural midpoint) and fixing \(C_{a\gamma}=8\). The text itself states this is “not a distinctive ECH prediction.” The 3.9\(\sigma\) combined figure (Eq. 5) is therefore an upper bound under an ad-hoc prior, not evidence.  
Required fix: Delete all language implying the result supports or tests ECH; report only the tuned-subspace posterior.

**P1B-M1 (MAJOR)**  
Section: §IV (p. 8–11) + Fig. 3  
Problem: Pipeline bias of \(|\Delta\hat\beta|=0.040^\circ\) (worst-case) is presented as “not a competitive sky detection.” The published Planck/ACT value is \(0.342^\circ\pm0.094^\circ\) (3.6\(\sigma\)). The bias is 43 % of the reported uncertainty; the paper never quantifies how this systematic shifts the final significance.  
Required fix: Provide a direct propagation of the 0.040° floor into the final \(\beta\) posterior or retract the claim that the pipeline validation is adequate.

**P1B-M2 (MAJOR)**  
Section: Table I (p. 5) + §II (p. 3)  
Problem: Two frozen chains (176 240 and 132 949 raw samples) are merged into a headline 309 189-sample result. The text notes a 0.04\(\sigma\) shift when the lensing likelihood is swapped, yet reports only the merged posterior. No Gelman–Rubin or ESS comparison between the two chains is shown.  
Required fix: Publish separate posteriors or demonstrate convergence to <0.01 in every parameter before merging.

**P1B-M3 (MAJOR)**  
Section: §V.C (p. 12) + Table II  
Problem: DESI DR2 \(w_0w_a\) chain is overlap-uncorrected. The paper states the \((w_0,w_a)=(-1,0)\) point is unsampled and that a Savage–Dickey ratio is “not viable.” No \(\ln B\) or \(\Delta\)AIC is reported, yet the abstract and introduction treat the run as a “cross-check.”  
Required fix: Either perform the nested-sampling analysis or remove all model-comparison language.

**P1B-N1 (MINOR)**  
Section: p. 3, “What is NOT in this paper” paragraph  
Problem: Duplicate phrasing (“the full derivations … are in Paper I(a)”) appears twice in consecutive sentences.  
Required fix: Consolidate.

**P1B-N2 (MINOR)**  
Section: Fig. 1 caption (p. 7)  
Problem: “119 617 post-burnin samples” vs. Table I footnote “123 368 post-burnin.” Inconsistency in reported sample count.  
Required fix: Correct the caption.

**P1B-NIT1 (NIT)**  
Section: Title (p. 1)  
Problem: 28-word title violates PRD style guidance on conciseness.  
Required fix: Shorten.

**Summary recommendation**  
REJECT

The manuscript is a set of null-consistency checks performed with unmodified public codes, accompanied by repeated explicit disclaimers that none of the exercises actually probe the ECH spin-torsion sector. The only quantitative results that survive the paper’s own scope statements are (i) a pipeline bias measurement that is 43 % of the claimed detection significance and (ii) a spectator-ALP posterior obtained after a 25× fine-tuning that the authors themselves label non-distinctive. Because the work is neither self-contained nor a direct test of the theory it claims to verify, it does not meet the threshold for a standalone PRD article.