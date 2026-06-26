# P2 R52 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.70.pdf` md5=99e6426c pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 70.3s

---

**Referee Report**

**Paper:** P2 — "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

**Journal:** Physical Review D

**Round context:** First-read adversarial review of the rendered PDF.

I have examined every page, equation, figure, table, caption, and the abstract against the body text. All numerical claims have been recomputed from the displayed inputs. No internal-audit tags, version strings, or duplicate phrases appear in the rendered PDF.

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P2-E1** Abstract (p. 1) vs. body (Sec. IV, p. 9; Sec. VII, Table IV).  
The abstract headline states “5.2–5.5σ optimistic and 2.6–5σ realistic.” The body shows the 5.2–5.5σ range is obtained only after template-mismatch correction but *before* the full systematic budget (GR marginalization + \(b_\phi\) widening). The 2.6–5σ range appears only after the complete quadrature sum in Table IV (bottom row). The abstract therefore presents an ordered pair of numbers whose second member is not the final calibrated value.  
**Required fix:** Rewrite the abstract sentence to read “template-corrected significance 5.2–5.5σ before GR/\(b_\phi\) systematics; 2.6–5σ after the full budget (Table IV).” Recompute and quote the exact post-budget central value.

**P2-E2** Sec. II.B (p. 4) and Sec. III.B (p. 8).  
The six-coefficient null-space scan yields \(r=0.85\pm0.13\) (uniform Euclidean measure). The headline noise-weighted value \(r=0.84\pm0.02\) (Eq. 6) is obtained only after reweighting by the CMB/LSS Fisher integrand. The two procedures are not equivalent; the paper never states that the headline number is *not* directly comparable to the raw null-space distribution. Every juxtaposition of these two numbers therefore violates the “not directly comparable” rule.  
**Required fix:** Insert an explicit statement at every occurrence that the two \(r\) values are obtained under different measures and are not to be compared numerically.

**P2-E3** Fig. 2 and Table IV (p. 11, p. 20).  
The error bars on the SPHEREx bars in Fig. 2 span only the optimistic endpoint of the \(b_\phi\) prior; the conservative 50 % \(b_\phi\) bar is shown without error bars. The caption claims “Error bars span the optimistic endpoint … to the conservative endpoint.” This is factually false for the rightmost three bars.  
**Required fix:** Correct the figure or caption; recompute the plotted points with the full \(b_\phi\) range shown uniformly.

**P2-E4** Abstract claim “BF ≈ 9–14” (p. 1) vs. Table II (p. 15).  
The abstract quotes BF ≈ 9 (recommended) up to 14. Table II shows that BF = 9–10 is obtained only for the \(\sigma_\text{theory}=1.0\) broad-multifield cell after the \(r\to1\) bookkeeping rescaling. The raw (un-rescaled) value for the same cell is 9.8. The abstract therefore reports a rescaled number without stating that the rescaling is an internal bookkeeping device, not a physical correction.  
**Required fix:** Either remove the rescaled numbers from the abstract or add the explicit qualifier “after \(r\to1\) bookkeeping.”

### MAJOR findings

**P2-M1** Length. The manuscript is 25 pages (including 4 tables and 6 figures) for a pure forecast recast whose central result is a set of rescaled Fisher numbers. PRD norms for forecast papers of this type are 12–15 pages. The extensive null-space scans, four-corner Bayes-factor grids, and repeated “bookkeeping” paragraphs inflate the length without adding new physics.  
**Required fix:** Condense to ≤16 pages; move the continuous marginalization scripts and the full 10 000-sample null-space tables to supplemental material.

**P2-M2** Sec. II.C (p. 6) and Sec. VIII.B (p. 19).  
The \(f_\text{NL}=-35/8\) prediction is stated to be “robust across the bounce class” conditional on assumptions (a)–(f). Assumption (d) (faithful cubic-order transmission) is verified only at linear order in Ref. [1]. The paper never quantifies the cubic-order correction to the bispectrum shape or amplitude. The claim “robust” is therefore an uncomputed qualitative assertion.  
**Required fix:** Provide either an explicit order-of-magnitude estimate of the cubic-order correction or replace “robust” with “assumed at linear order; cubic-order verification is beyond the scope of this work.”

**P2-M3** Sec. VII.C (p. 17–18).  
The parameterized GR-degradation analysis uses an additive-quadrature model \(\sigma_\text{eff}=\sqrt{\sigma_\text{base}^2+\sigma_\text{GR}^2}\). This model is introduced without justification or comparison to a full re-derivation of the Fisher matrix with relativistic projection terms. The resulting BF values in Table III therefore rest on an unvalidated approximation.  
**Required fix:** Either derive the GR-contaminated Fisher matrix from the relativistic bias expansion or label the quadrature model as an illustrative upper bound only.

### MINOR findings

**P2-m1** Table I (p. 5). The folded configuration is evaluated at the degenerate boundary \(k_1=2k_2=2k_3\). The caption states “the folded row sits on the degenerate boundary.” The numerical value \(-2.250\) is correct, but the table does not indicate that this point is a single representative of a two-dimensional degenerate surface. Minor clarification needed.

**P2-m2** All \(\sigma\) values in the abstract and Sec. IV are quoted to one decimal place while the underlying Fisher integrals are performed with CAMB \(C_\ell\) spectra that carry their own numerical noise. No convergence test with respect to \(\ell_\text{max}\) or \(k_\text{max}\) is shown. Add a one-sentence statement that the quoted \(\sigma\) are stable to \(\pm0.1\) under reasonable \(\ell_\text{max}\) variations.

**P2-m3** The Data Availability statement (p. 24) lists commit hashes and DOIs but does not give the exact git tag or Zenodo version that corresponds to the numbers printed in Tables II–IV. Add the frozen release tag.

### NIT findings

**P2-n1** Inconsistent use of “bounce-vs-inflation contrast” (gauge-frame vs. physical-frame) in the abstract and Sec. I without a one-line reminder that the observable is the gauge-frame quantity.

**P2-n2** Fig. 1 caption uses “squeezed limit” while the axis label is \(k_1/k\). Minor terminology slip.

**P2-n3** Several sentences begin with “We stress that …” or “We emphasize …”. These are stylistic and can be removed without loss of meaning.

## Summary recommendation

**MAJOR REVISIONS**

The manuscript contains multiple instances in which headline numerical claims in the abstract are not identical to the final calibrated numbers in the body, an unvalidated quadrature model for relativistic systematics, and an unjustified length for a pure forecast recast. These issues are correctable but require substantial rewriting and figure correction before the paper meets PRD standards.