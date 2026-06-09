# P2 R22prov2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 63.4s

---

**Referee Report**

**P2-E1** (Abstract, p. 1)  
The abstract states a “realistic range ∼3–5σ” and “BF∼10–17” as headline results. These numbers are assembled from multiple distinct weighting schemes, an ad-hoc 0.84 template-overlap factor, a 1–8 % 𝒪(𝜖) correction, and separate GR/bₒ marginalizations that are never combined into a single Fisher matrix in the text. The abstract therefore reports a composite figure that cannot be recomputed from any single table or equation.  
**Required fix:** Replace the composite headline with the single most conservative number that follows from one explicitly defined Fisher matrix (or remove the numerical claim).

**P2-E2** (Abstract & §IV, p. 1 & p. 7)  
The abstract quotes 𝜎(𝑓_NL)≃0.7 from the bispectrum alone. The body (§IV) shows that this value is taken from Heinrich et al. (2024) after an external template-overlap rescaling 𝑟=0.84 that is never re-derived inside the present Fisher matrix. The abstract therefore presents an external forecast as an internal result.  
**Required fix:** Either recompute the full multi-tracer Fisher matrix with the bounce template inside the code or qualify the number as “rescaled from Heinrich et al.”

**P2-E3** (p. 16, §VIII A)  
The SDB joint channel is now reported with 𝜎(𝑛_𝑓NL)=0.295/0.596 and 𝜎_marg(𝑓_NL)=3.08/7.06. These numbers appear only after the metadata note that a previous 9.9𝜎 claim was withdrawn. No derivation or code commit for the new numbers is supplied; the paragraph simply states the values. This is an unsupported numerical claim.  
**Required fix:** Provide the explicit Fisher matrix or Monte-Carlo script that produces 0.295/0.596.

**P2-M1** (entire manuscript)  
The paper is 22 pages. PRD forecast papers on similar topics (e.g., Doré et al. 2014, Heinrich et al. 2024) are 10–14 pages. The length is driven by an extended appendix on the Cai vs. Li-Brandenberger convention and by repeated self-audits of the same three benchmark triangles.  
**Required fix:** Reduce to ≤14 pages by moving the convention audit to a short appendix or a separate note.

**P2-M2** (§II A, p. 3)  
The six-coefficient polynomial is under-determined (rank-3 null space). The authors scan 10 000 random coefficient sets inside a ball of radius 50 and report 𝑟=0.85±0.13. No justification is given for the radius choice or for the uniform sampling measure; both affect the quoted scatter.  
**Required fix:** Demonstrate that the reported uncertainty is stable under changes of ball radius and sampling measure, or adopt the explicit minimum-norm solution.

**P2-M3** (Fig. 2 & §IV, p. 8)  
Error bars on the detection-significance histogram are labeled “optimistic-to-conservative” but are never defined. The reader cannot tell whether they include the full systematic budget quoted in §VII.  
**Required fix:** State explicitly which systematics are folded into each bar.

**P2-N1** (p. 1 header)  
“(Dated: June 9, 2026)” is a future date.  
**Required fix:** Replace with submission or revision date.

**P2-N2** (multiple pages)  
Section, equation, and table numbers appear inside red boxes (e.g., [II C], [II]). These are production artifacts, not scientific content.  
**Required fix:** Remove highlighting before final submission.

**P2-N3** (bibliography)  
Several arXiv numbers are given without journal references even though the papers have been published (e.g., arXiv:2209.04322 is now JCAP).  
**Required fix:** Update to published citations where they exist.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript contains multiple unsupported numerical claims in the abstract and §VIII, an unjustified 22-page length, and at least one Fisher-matrix result whose provenance is not traceable inside the supplied text. These are not cosmetic issues; they prevent a reader from reproducing the headline forecasts. A substantially shortened version that derives every quoted significance from a single, committed Fisher matrix would be reconsiderable, but the present draft does not meet PRD standards.