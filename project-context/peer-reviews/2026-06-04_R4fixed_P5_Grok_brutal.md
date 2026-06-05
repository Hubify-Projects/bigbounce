# P5 2026-06-04_R4fixed — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 11.2s

---

**Referee Report: P5**

**P5-E1 (Title page / header, p. 1)**  
Problem: The manuscript contains explicit version-history language: “(Dated: June 4, 2026)”.  
Required fix: Delete the date entirely. No version or round metadata may appear in the body or header.

**P5-E2 (Abstract, first paragraph, p. 1)**  
Problem: The abstract states a clean headline null (“the CW fraction shows no environment dependence above the sensitivity floor…”) while the body repeatedly qualifies the result as anchored on a secondary DESIVAST re-projection, reports a 3.4σ bright/dark filament sign-flip, and treats the V-Web void class as survey-edge dominated. The abstract therefore misrepresents what the body actually proves.  
Required fix: Rewrite the abstract to state only what is demonstrated after all primary/secondary distinctions, multiplicity corrections, and residual structures are acknowledged.

**P5-E3 (Abstract and §V B, p. 1 and p. 5)**  
Problem: The manuscript designates the DESIVAST path as “primary” only after the fact and explicitly notes that “a single a priori preregistered analysis plan was not filed.” This is an unhedged admission of post-hoc path selection presented as a controlled analysis.  
Required fix: Either remove the primary/secondary framing or demonstrate that the DESIVAST result was the sole pre-specified statistic; otherwise delete all language claiming a pre-specified primary path.

**P5-E4 (Throughout, e.g. §III C, §IV A, §VI, §VIII, etc.)**  
Problem: The text is saturated with internal pipeline paths, provenance sidecars, SHA-256 anchors, config-file references, and driver scripts (“pipelines/p5_desi_chirality/scripts/…”, “.provenance.json”, “iron-reduction snapshot”, etc.). These are review-log artifacts, not journal prose.  
Required fix: Remove every pipeline path, script name, JSON artifact citation, and reproducibility tag from the narrative. Move all such material to a separate reproducibility statement or supplementary archive.

**P5-E5 (Abstract and §VI A, p. 1 and p. 6)**  
Problem: σ values obtained from label-shuffle, density-quintile, HEALPix, and V-Web vs. DESIVAST procedures are presented on the same numerical scale and compared directly (e.g., “−2.61σ”, “−4.66σ”, “|σobs − σpred| = 1.87”) without qualification that the null distributions and effective degrees of freedom differ.  
Required fix: Either (a) demonstrate that all quoted σ values are drawn from identically distributed nulls or (b) replace all cross-procedure σ comparisons with properly calibrated p-values or effect-size measures that do not assume commensurability.

**P5-E6 (§II and throughout)**  
Problem: The entire analysis treats the monopole offset, labels, and uncertainty budget of “Paper IV” (explicitly “not yet peer-reviewed”) as fixed external inputs whose systematic floor is propagated without re-derivation. A manuscript cannot rest its central statistical claim on an unpublished companion by the same author.  
Required fix: Either (a) make Paper IV publicly available with an arXiv identifier before submission or (b) re-derive the monopole offset and its uncertainty from the matched sample inside this paper.

**P5-M1 (§V B, p. 5)**  
Problem: The multiplicity bookkeeping for the five DESIVAST estimators is declared post-hoc and the Bonferroni threshold is applied only after the data are examined.  
Required fix: Pre-specify the exact family of tests and correction procedure in a registered analysis plan or remove the claim that the DESIVAST family has been properly multiplicity-controlled.

**P5-M2 (§VI D and §XI, p. 7–8 and p. 17)**  
Problem: The 3.4σ bright/dark filament sign-flip is reported as a “real residual structure” yet is simultaneously dismissed as consistent with selection-function systematics; the text never quantifies how much of the residual can be attributed to each.  
Required fix: Provide a quantitative partition (or demonstrate that the data cannot support one) and adjust the strength of the environment-independence conclusion accordingly.

**P5-M3 (Abstract and §VIII, p. 1 and p. 10)**  
Problem: The controlling void constraint is shifted to the DESIVAST re-projection (n = 56 981) because the V-Web void bin (n = 428) is “survey-edge artifact dominated.” The abstract nevertheless presents the V-Web numbers as part of the headline result.  
Required fix: Remove the V-Web void σ value from the headline summary or state explicitly that it is discarded.

**P5-N1 (Throughout)**  
Problem: Repeated use of the phrase “statistically indistinguishable from zero” for p-values that are merely > 0.05 after correction.  
Required fix: Replace with precise statements of the measured p-value or upper limit.

**P5-N2 (§XIII)**  
Problem: The limitations section lists several unquantified systematics (RSD eigenvalue deformation, gauge invariance of the toy EFT operator, etc.) but does not propagate them into the final error budget.  
Required fix: Either quantify the additional uncertainty or state that the quoted precision does not include these contributions.

**Summary recommendation**  
MAJOR REVISIONS

The manuscript is not journal-clean: it contains version metadata, extensive internal pipeline prose, and an unpublished companion paper treated as a fixed input. The abstract misrepresents the body’s qualified and post-hoc nature. Multiple σ values from incommensurate null procedures are compared directly. Until these ESSENTIAL items are corrected, the paper cannot be evaluated on scientific grounds.