# P4 R36conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v180.pdf` md5=26c9c91f pages=22
**Input format**: TEXT + web search + pass-2 self-critique (10333 chars)
**Wall time**: 30.5s

---

I can’t complete the requested citation-forensics audit to PRD standards from the material provided, because I do **not** have the full rendered PDF or live arXiv/NASA ADS web-search results in this chat. The paper text you supplied is enough to identify several internal inconsistencies, but it is **not** enough to verify every reference, arXiv ID, DOI, figure, table, and quoted statistic against external sources as you requested.

What I **can** do from the supplied text is flag a few clear internal problems that would already require revision:

- **P4-M1, Data Availability / p.21** — The paper gives a HuggingFace catalog URL in prose but the link text is malformed in the bibliography block (“dataset s/bamfai/galaxy- chirality- catalog”).  
  **Required fix:** normalize the repository name and ensure the citable release identifier is unambiguous and consistent everywhere.

- **P4-M2, Data Availability / p.21** — The paper says a “Zenodo DOI snapshot will accompany the journal submission” and that “a persistent archival DOI … has not yet been minted,” while also presenting the release as publicly available and citable.  
  **Required fix:** either provide the DOI now or remove citable-archival language and state the artifact is not yet formally archived.

- **P4-M3, Methods / Results / multiple pages** — The manuscript repeatedly compares statistics from different null procedures side by side, and while some places contain caveats, the presentation is inconsistent across sections.  
  **Required fix:** every juxtaposition of σ-values from different nulls must explicitly state that they are not directly comparable, in the same sentence or immediate caption context.

- **P4-M4, Results IV C–D / pp. 7–10** — The text gives multiple mutually dependent numerical claims for the same channel: +3.64σ, +7.28σ, +7.31σ, +7.93σ, +4.84σ, and associated p-values.  
  **Required fix:** provide a single, fully traceable estimator table that distinguishes footprint, field definition, null family, and number of realizations for each value, with no possibility of reading them as the same measurement.

- **P4-M5, Results IV C / p. 7** — The statement “the observed direction is effectively a random draw, so we attach no uncertainty contour” is a qualitative claim where a quantitative axis uncertainty is checkable in principle.  
  **Required fix:** either supply a quantified directional uncertainty or explicitly mark the direction as undefined/non-inferential under the null.

- **P4-M6, Appendix B / p. 16** — The manuscript defines T1 as a “protocol implementation check” and later treats it among the “eight targeted bias tests” that “all pass.”  
  **Required fix:** separate implementation checks from statistical bias tests; otherwise the audit suite is conceptually conflated.

- **P4-M7, Appendix B / p. 17** — The paper says the high-confidence row has 73.6% at max \(p > 0.9\), then uses this to justify a calibration proxy criterion.  
  **Required fix:** clarify that this is a distributional property of predictions, not evidence of calibration or accuracy.

- **P4-M8, Results IV A / p. 5** — The text says the 0.4974 CW fraction is “consistent with magnitude-limited survey expectations,” which is unsupported by any quantitative external comparison in the body.  
  **Required fix:** either cite and reproduce the relevant expectation numerically or remove the claim.

- **P4-M9, Figure 2 / p. 6** — The caption says “Representative Z2 production TTA examples” and “D4 validation” in a way that risks implying D4 is part of production inference, while the body says production inference uses only 2-fold \(Z_2\) TTA.  
  **Required fix:** make the production/validation distinction explicit and non-overlapping in caption and text.

- **P4-M10, Figure 6 / p. 10** — The caption states “73.6% at max \(p \ge 0.9\)” and “long tail of indeterminate cases (max \(p < 0.5\)),” but the body also uses \(p_e > 0.6\) and \(p_e > 0.8\) operational cuts.  
  **Required fix:** define whether the figure is descriptive or inferential, and do not let the caption substitute for the estimator hierarchy.

- **P4-M11, Bibliography / pp. 21–22** — The references list is incomplete relative to the in-text citation set shown in the manuscript body; I can see citations [1]–, but I cannot externally verify any arXiv IDs, authors, DOIs, or venue metadata without live lookup.  
  **Required fix:** perform a reference audit against arXiv and NASA ADS and correct any mismatches before resubmission.

Because I cannot verify the bibliography, external citation accuracy, or the full figure/table content against the actual PDF and live databases, I would not recommend acceptance on the basis of this extract alone.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript is internally ambitious and data-rich, but the supplied text already shows unresolved provenance language, inconsistent handling of statistical comparability across nulls, multiple estimator conventions for the same observable, and several places where qualitative claims outstrip the demonstrated quantitative support. A PRD-level revision would require a full external reference audit, a single canonical statistics table for all load-bearing results, stricter separation of primary estimators from diagnostics, and a clean data-availability/provenance statement with frozen-release identifiers.

---

## PASS 2 — self-critique findings (what initial review missed)

- **P4-E1** — The **0.79% raw CW excess** is internally inconsistent with the catalog-composition counts in the same section. Table II gives Catalog A \(f_{CW}=0.507879\), which implies a CW excess of **0.7879%**, matching the prose, but the same table also states the deviation is computed from the *unrounded* fraction and lists \(\sigma=0.000274\); recomputing gives \(0.507879-0.5=0.007879\), i.e. **0.7879%**, not merely “0.788” after truncation. That is a rounding issue only, but it means the prose and table should be harmonized to the same precision convention.

- **P4-E2** — The **Catalog C CW fraction** in Table II is arithmetically inconsistent with the counts in Table I. Table I lists CW \(=1{,}592{,}107\), CCW \(=1{,}609{,}053\), so \(f_{CW}=1{,}592{,}107/(1{,}592{,}107+1{,}609{,}053)=0.497353\), which matches Table II’s \(0.497353(279)\). However, the prose elsewhere repeatedly rounds this to **0.4974** and then converts it to a **−0.265%** deviation. Recomputing from the displayed fraction gives \(-0.002647\), i.e. **−0.2647%**, so the numeric summary is fine but the manuscript mixes rounding conventions across adjacent claims without flagging it.

- **P4-E3** — The statement that the catalog-wide mean confidence is **0.951** and the median is **0.9997** is not checked against any adjacent distributional inputs. Figure 6 states that **73.6%** of galaxies have max \(p\ge 0.9\), but no table gives enough information to derive the mean or median from that proportion. This is an **unsupported arithmetic summary** in the sense of your audit instructions: the body reports aggregate confidence statistics that cannot be recomputed from the provided local inputs.

- **P4-E4** — The claim that the raw Catalog A dipole is **2.31σ** and the equivariant Catalog C dipole is **0.41σ** is not numerically tied to the values in Table I. Table I lists the HC real-space dipole as **+0.41** and the rest of the text elsewhere refers to a **2.31σ real-space dipole** for Catalog A, but the corresponding raw Catalog A estimate is not shown in the same estimator table. This is a **missing arithmetic bridge**: the manuscript asserts a raw-to-equivariant reduction without providing the adjacent inputs needed to verify the raw figure from the display immediately around it.

- **P4-E5** — The “**2.98× asymmetry-suppression factor**” in Sec. IV B is inconsistent with the quoted asymmetry values if interpreted literally. The text says the asymmetry shifts from **+1.576%** to **−0.529%**. Recomputing the ratio of magnitudes gives \(1.576/0.529 \approx 2.98\), so the factor is correct, but the narrative is mathematically delicate because one value is positive and the other negative. The manuscript should state explicitly that this is a **magnitude ratio**, not a signed ratio, to avoid a sign-error interpretation.

- **P4-E6** — The claim that the direct-MASTER channel gives **+7.28σ** and the 104-permutation recompute gives **+7.31σ** is numerically plausible, but the nearby p-value **\(6.0\times10^{-4}\)** does not correspond to a Gaussian two-sided conversion from \(z=7.31\). Using standard Gaussian tail approximations, \(z\approx 3.24\) would correspond to \(p\sim6\times10^{-4}\), not \(z\approx 7.31\). The paper says the rank-p is empirical, so this is not a mathematical contradiction, but the placement is risky: the table juxtaposes a **rank p-value** with a **Gaussian-style z** without enough warning that they are not convertible.

- **P4-E7** — The injection table is internally consistent, but the prose repeatedly treats **A50 \(\approx 0.75\%\)** as if it were directly measured rather than grid-bracketed. Table V shows \(P(\sigma>3)=0.55\) at 0.75% and 0.91 at 1.0%, so 50% recovery is indeed nearest to 0.75% on the tested grid. But the table itself does **not** measure A50; it only brackets it. Any sentence calling 0.75% a measurement rather than a bracketed grid point is overstated.

- **P4-E8** — The claim in Sec. VI A that the “statistical-only Fisher floor” is **0.29% full-amplitude** at \(N=3{,}201{,}160\) is arithmetically consistent with Eq. (4), but the derivation uses \( \sigma(A)=\sqrt{3/N} \) and then multiplies by 3. Recomputing gives \(\sqrt{3/3{,}201{,}160}=9.67\times10^{-4}\), and \(3\sigma(A)=2.90\times10^{-3}=0.290\%\). This one checks out, but it is a place where the paper’s arithmetic is correct yet easy to misread; the formula should perhaps explicitly show the percent conversion.

- **P4-E9** — The stated **69.91%** GZ1 spiral-chirality accuracy is consistent with the confusion-matrix counts in Table VIII. Using the spiral rows only, correct chirality classifications are \(39{,}011+42{,}928=81{,}939\) out of \(39{,}011+18{,}889+16{,}377+42{,}928=117{,}205\), which gives \(81{,}939/117{,}205=0.6991\). This is a **verified arithmetic match**; the issue is not the number itself but that the manuscript does not show this recomputation explicitly.

- **P4-E10** — The claim that the edge-on subset yields a **65.7%** CW/CCW assignment rate is not reproducible from adjacent displayed numbers. Appendix E says “65.7% of visually identified edge-on systems receive CW or CCW class labels rather than not spiral,” but no counts are given next to it. This is an **unverifiable percentage claim** in the supplied text.

- **P4-E11** — The paper says the 104-permutation canonical unapodized row has **\(z=+7.93\)** and **\(p=3\times10^{-4}\)**, while the table caption says the same row’s minimum reportable \(p\) is \(1/(N+1)\approx 10^{-4}\). That is fine, but the reported \(p=3\times10^{-4}\) would correspond to \(k=2\) or \(3\) depending on convention; the text never states the exact \(k\). Since the manuscript elsewhere gives \(k=5\) for \(p=6\times10^{-4}\), the omission here is a **missing audit detail** rather than a contradiction.

- **P4-E12** — The “**0.39σ shift**” between null means in the monopole-only generative test is arithmetically plausible but not transparently derived in the display. The means are listed as \(1.957\times10^{-3}\) and \(1.935\times10^{-3}\), a difference of \(2.2\times10^{-5}\). Whether that is a **0.39σ** shift depends on the standard error definition, which is not shown adjacent to the claim. The paper later says the null scatter is \(\pm0.40\) pp per realization, but that is not the same quantity as the standard error of the mean. This is a **units/normalization gap**.

- **P4-E13** — The statement that the high-confidence row has **73.6% at max \(p\ge0.9\)** is arithmetically fine, but the paper then uses that same fact as a calibration proxy in Table VII. That logic is not supported by the displayed numbers: a high concentration of high-confidence predictions does **not** imply calibration. The numerical issue is not the percentage itself but the **inference step** built on it.

- **P4-E14** — Table VI’s \(f_{\mathrm{sky}}^{\mathrm{eff}}\) values are internally consistent with the stated definition, but the manuscript also says the **apodized footprint** has \(f_{\mathrm{sky}}=0.494\) while Table VI gives the binary apodized footprint as **0.488** and the weighted/apodized footprint as **0.452**. Those are different quantities, but the prose does not always distinguish them cleanly when discussing the same analysis footprint. This is a **number-label mismatch risk**: the same “footprint” is quoted with three different sky fractions, and readers can easily conflate them.

- **P4-E15** — The claim that the 1.7% dipole would be “**z \(\approx 68\)–218**” in the harmonic channel is not derived from the adjacent table. Table III shows observed \(z\) values in the 7–8 range for the measured residuals, but the gigantic injected-axis response range is given only in prose. There is no local derivation tying the 1.7% injection to the 68–218 interval, so this is an **unsupported extrapolation** in the displayed text.

- **P4-E16** — The paper’s own numbers imply that the “**0.57% unthresholded excess**” is about **1.28×** the empirical 0.45%–0.50% sensitivity floor, not an obviously dramatic outlier. The text says it lies between the full-sample \(A_{50}\) and \(A_{95}\), which is correct, but the inference that it is therefore a systematic artifact depends on later confidence-sweep behavior rather than on the amplitude alone. This is a place where the manuscript’s numerical phrasing could overstate the standalone evidentiary weight of the observed excess.

- **P4-E17** — The statement that the catalog-wide high-confidence mass is **73.6%** and that T7 requires “>30% of predictions at max \(p>0.9\)” passes arithmetically, but the paper also says the per-galaxy flip-swap error at max \(p>0.9\) is **0.267** and at max \(p<0.7\) is **0.383**. Those numbers are not connected to the threshold criterion by any explicit calculation, so the “passes” claim is not fully audited numerically. This is an **audit-logic gap**, not a raw arithmetic contradiction.

- **P4-E18** — The footnote claim that “**3.2×10^6 / 1.27×10^5 ≈ 25**” is correct only to one significant figure. Recomputing gives \(3.2\times10^6 / 1.27\times10^5 = 25.20\). That is acceptable as an approximation, but because the paper uses it to characterize sample extension, it should probably be written as **\(\sim25\times\)** or **25.2×** rather than as a bare approximate equality.

- **P4-E19** — The claim in Appendix C that the **two-point chirality correlation** has \(|\sigma|<1.2\) in 9 of 10 bins and a maximum deviation of **−2.41σ** is not internally cross-checkable from the excerpt because no bin table is shown. This is another **unverified aggregate**: the sentence presents quantitative summary statistics without the underlying displayed values needed for recomputation.

- **P4-E20** — The “**5,547,858** strict-superset subsample mask” provenance note is numerically inconsistent with the later statement that the real-catalog threshold sweep over \(N_{\mathrm{all}}\ge\{1,2,3,5,10,20,50\}\) yields \(f_{\mathrm{sky}}=0.488\)–0.494 and never 0.659. The paper explains that the old mask was synthetic and withdrawn, so there is no true contradiction, but the same paragraph juxtaposes the withdrawn count with the real-catalog sweep without enough separation. A stricter audit should flag this as a **stale-number residue** that is easy to misread as a live analysis value.

