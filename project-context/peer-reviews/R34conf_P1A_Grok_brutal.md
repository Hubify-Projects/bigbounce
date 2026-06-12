# P1A R34conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.62.pdf` md5=9a1a725b pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 78.0s

---

**Referee Report for Physical Review D**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Manuscript metadata visible in rendered PDF:** Dated June 11, 2026; v1A.0.62; 28 pages; PACS 98.80.-k etc.

I have examined every page, equation, figure, table, footnote, and caption in the rendered PDF. The following findings are exhaustive.

**P1A-E1 (ESSENTIAL)**  
Section I, p. 3 (and repeated in Sec. IV, p. 10 and abstract): “the four enumerated minimal-ECH dark-energy routes … are not proven to be a complete diffeomorphism-invariant operator basis”. The paper simultaneously claims a “channel-level amplitude closure” under 14 constraints while explicitly disclaiming operator-level completeness. These two statements are in direct logical tension; the title and abstract framing are therefore stronger than the body.  
**Required fix:** Rewrite title, abstract, and all closure claims to state only what is actually shown (amplitude-level no-go under stated assumptions, not route closure).

**P1A-E2 (ESSENTIAL)**  
Footnote a, p. 2: “Earlier versions of this manuscript erroneously identified the two pieces…”. Internal draft-history language appears in the published manuscript.  
**Required fix:** Remove all language referring to prior manuscript versions.

**P1A-E3 (ESSENTIAL)**  
Abstract and p. 1: date “June 11, 2026”. A submission date in the future is impossible.  
**Required fix:** Correct date and version string.

**P1A-E4 (ESSENTIAL)**  
Abstract claims \(f_{NL}=-35/8\) and \(\beta\approx0.27^\circ\) as “surviving predictions”. Both numbers are imported from companion papers (explicitly stated on p. 4 and p. 9). No derivation or numerical pipeline appears in the present manuscript. Standalone-reader test fails.  
**Required fix:** Either reproduce the calculations or remove the numerical claims from the abstract.

**P1A-E5 (ESSENTIAL)**  
Abstract and Sec. X (p. 18): “perturbation-transparency result”. The result is explicitly restricted to “canonical scalar matter” and excludes “propagating torsion, dynamical Immirzi field, fermion-loop, and non-minimal-matter sectors” (p. 3). The abstract does not carry this scope limitation.  
**Required fix:** Add the full scope restriction to the abstract sentence.

**P1A-M1 (MAJOR)**  
The entire argument (Secs. IV, IX, X) rests on 14 “logically independent structural barriers” whose justification is distributed across seven “foundation studies” and six “observational branches”, most of which cite companion papers. The manuscript is not self-contained.  
**Required fix:** Supply all missing derivations or reduce the paper to the single new result (Bianchi vanishing of the Holst dual contraction) that can be verified from the present text.

**P1A-M2 (MAJOR)**  
Table II lists 14 barriers; Barrier 8 (parity-even interaction) and Barrier 14 (perturbation transparency) are flagged as “subsumed”. The text never demonstrates logical independence of the remaining 12 after subsumption.  
**Required fix:** Provide an explicit independence proof or reduce the catalog to the number actually shown to be independent.

**P1A-M3 (MAJOR)**  
Fig. 3 lower panel shows \(\Delta H/H_{\Lambda\mathrm{CDM}}\) at the percent level while the caption states the rotation contribution is “completely invisible”. The plotted curve is visibly nonzero; the caption is internally inconsistent.  
**Required fix:** Correct caption or replot.

**P1A-M4 (MAJOR)**  
Eq. (15) and surrounding text on p. 11–12 compare one-loop \(\Delta\theta\) to observed \(\beta_{\mathrm{obs}}\) using \(\alpha_{\mathrm{em}}/(4\pi)\approx5\times10^{-4}\). The numerical factor that converts this ratio into the quoted 60-order suppression is never shown; only the final exponent appears.  
**Required fix:** Insert the explicit arithmetic.

**P1A-N1 (MINOR)**  
Multiple figure captions (Figs. 1, 4, 5) contain parenthetical remarks that duplicate text already in the body.  
**Required fix:** Trim captions.

**P1A-N2 (MINOR)**  
Table I footnote “a” states “Reparameterized as sensitivity to \(N_{\mathrm{tot}}\)”. The table itself never displays the reparameterized values.  
**Required fix:** Either add the column or delete the footnote.

**P1A-NIT1**  
Inconsistent use of “one-loop” vs. “one loop” throughout.

**Additional observations (no classification required but noted for completeness)**  
- The paper is 28 pages for a single technical result (Bianchi identity vanishing of the Holst dual on a torsion-free connection). PRD norms for a methods note of this scope are ~10–12 pages.  
- All \(\sigma\) values and MCMC posteriors are imported from companions; no independent verification is possible from the supplied PDF.  
- No effect-size statement accompanies any \(\chi^2\) or significance claim.

**Summary recommendation**  
**REJECT**

The manuscript contains internal draft language, a future date, an abstract whose quantitative claims cannot be verified from the supplied text, and a logical tension between its title and its explicit scope disclaimers. It is not self-contained. These defects are fatal on first read. A drastically shortened, self-contained version limited to the Bianchi-identity result might be reconsiderable after major revision, but the present document does not meet PRD standards.