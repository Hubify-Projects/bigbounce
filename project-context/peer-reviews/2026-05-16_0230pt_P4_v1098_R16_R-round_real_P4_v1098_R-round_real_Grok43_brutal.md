# P4_v1098 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0230pt_P4_v1098_R16_R-round_real
**Wall time**: 38.0s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=74922, completion=3414, reasoning=2450, total=78336

---

**PAPER-GRO-B1**  
**Section:** Abstract (multiple instances) + Sec. 1 (Introduction) + Sec. 9 (Conclusions)  
**Issue:** Persistent framing of the \(\ell=1\) dipole as a "parity-violation" or "parity-violating" observable/test despite the explicit symmetry caveat in Sec. 2.5 that the dipole is parity-EVEN (isotropy test only). Examples: "parity-violation observable is the dipole", "cosmologically interesting parity violation", "parity-violation signature of interest is the large-scale dipole".  
**Fix:** Replace all dipole-specific instances with "isotropy-breaking axial-vector dipole" or "axial dipole (isotropy test, not parity test)". Retain "parity-violating sectors" only for the broader implication paragraph.

**PAPER-GRO-B2**  
**Section:** Sec. 9 (Conclusions) + Sec. 6.1 (Comparison with Shamir)  
**Issue:** Overstated claim that the result "disfavors the Shamir 2020/2022 \(\sim2\)--\(4\%\) class of detection claims at the amplitude level" without performing the required matched-footprint Ganalyzer reanalysis. The factor-of-6--12 amplitude difference is pipeline-dependent and does not constitute a statistical exclusion.  
**Fix:** Change to: "Under the present ViT-Small + DESI Legacy pipeline the measured amplitude is a factor of \(\sim6\)--\(12\) smaller than Shamir's reported values. A like-for-like reanalysis with Shamir's exact Ganalyzer pipeline, magnitude/redshift cuts, and footprint is required for a formal \(\sigma\)-level exclusion."

**PAPER-GRO-B3**  
**Section:** Multiple (abstract, Table 1, Sec. 5.3, Sec. 9, monopole null table)  
**Issue:** Inconsistent canonical-mask \(f_{\rm sky}\) values (0.494, 0.49005, 0.4938, 0.491) across text, tables, and artifacts. The monopole null table anchors on 0.49005 while other sites use 0.494/0.4938.  
**Fix:** Adopt a single canonical value (0.49005 from the artifact) and propagate it uniformly; add a footnote in the first table stating the adopted value and the source artifact.

**PAPER-GRO-B4**  
**Section:** Sec. 6.1 (Comparison with previous work)  
**Issue:** Citation to Iye:2026P6 still carries "the paper remains in preparation at the time of this version freeze" language even though the bibitem now lists the public arXiv:2605.05570.  
**Fix:** Update the sentence to: "Iye \& Yagi (2026) arXiv:2605.05570 is anticipated to extend..." and remove the "in preparation" clause.

**PAPER-GRO-B5**  
**Section:** Table 1 caption + Sec. 5.3 + Sec. 9 + artifact references  
**Issue:** Nomenclature drift on the high-confidence cut: "HC-broad-0.6", "HC-spiral (p>0.6)", "HC-spiral_p>0.6", and "HC-broad max(p_CW,p_CCW,p_NS)>0.6" are used interchangeably for the same \(N=949{,}584\) selection.  
**Fix:** Standardize everywhere to "HC-broad-0.6" (with footnote defining \(\max(p_{\rm CW,eq},p_{\rm CCW,eq})>0.6\), spiral-only) and update all artifact filenames/references in the next patch.

**PAPER-GRO-B6**  
**Section:** Abstract + Sec. 5.3 (sensitivity)  
**Issue:** The 99.3% pre-MASTER reproduction and the post-MASTER null are presented as a single "this-pipeline demonstration" without sufficient emphasis that the 99.3% figure applies only to the pre-MASTER stage on the un-subtracted map; readers may misread it as applying to the headline result.  
**Fix:** Add one clarifying sentence in the abstract after the 99.3% clause: "The 99.3% figure applies exclusively to the pre-MASTER pseudo-\(C_1\) on the un-monopole-subtracted map; the headline post-MASTER result on the subsample mask is \(-0.12\sigma\)."

No additional findings. The paper is otherwise converged on the 11 prior closures with no new regressions at BLOCKER/MAJOR level.
