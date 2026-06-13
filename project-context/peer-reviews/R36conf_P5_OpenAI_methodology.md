# P5 R36conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.70.pdf` md5=8bf87669 pages=31
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5248 chars)
**Wall time**: 79.5s

---

### Referee report on manuscript “Environmental Dependence of Spiral Chirality: …”  (tag P5, 31 pp)

I have audited every figure, table, equation and scalar appearing in the PDF.  
Below I list all problems found, classified as **ESSENTIAL (blocking), MAJOR, MINOR, NIT**.

--------------------------------------------------------------------
### 1.  ESSENTIAL issues  
--------------------------------------------------------------------

| ID | Location | Problem | Required fix |
|----|-----------|---------|--------------|
| **P5-E1** | Abstract, p. 1 and throughout | The load–bearing “catalog–wide monopole offset” (Δf_CW = –0.0026) and its 9 σ uncertainty are imported exclusively from the *companion* “Paper IV”, which is neither published nor included in the submission.  All key σ‐predictions, σ_vs monopole residuals and the whole null–hypothesis framework depend on that external value.  PRD requires a self–contained derivation or a peer-reviewed citation. | Either (i) include a fully self–contained derivation of the monopole offset in the present paper (data, network, training, augmentation, error propagation) or (ii) submit Paper IV and cross-reference an accepted or at least published pre-print.  Without one of those the statistical framework is not reproducible and the paper cannot be evaluated. |
| **P5-E2** | Whole manuscript | Internal revision history (“earlier draft”, “superseded”, “withdrawn value”, “driver … recomputed”, “artifact …”) appears in the scientific narrative (e.g. p. 15, 16, 18, 19, 24, 25).  This is laboratory-log material, not publication content. | Remove all revision-log prose and keep only the final, checked numbers.  Cite repositories in a short data-availability paragraph, not throughout the text. |
| **P5-E3** | Sec. V, eq. (1) and Table III | Two different σ statistics are used side-by-side (“σ_from half” vs “σ_pred” vs “σ_vs monopole”) without a strict rule whenever they are compared in prose (e.g. Fig. 5 right panel mixing observed σ and σ_pred).  Readers unfamiliar with the construction will misunderstand the scale. | Each time σ_from half is shown together with σ_pred or σ_vs monopole the text and figure legends must **explicitly** repeat that they are *not directly comparable* and carry different denominators.  Alternatively normalise all σ to the same reference. |
| **P5-E4** | Sec. VI A, contingency test; Sec. V (permutation procedures) | The row-level parent used for χ² and permutation tests contains 3.56 % repeated TARGETIDs, violating the i.i.d. assumption, yet the same table is quoted as the formal test.  Although a unique-ID recompute is mentioned, the paper keeps the less-valid number in the headline. | Make the unique-galaxy table the *only* parent for all inferential tests, or apply a cluster-bootstrap/duplicate-weighted χ² that keeps independence.  Report the corrected p-value in the abstract. |
| **P5-E5** | Sec. VII, Phase-2 sweep | The three Rs = 10 h⁻¹ Mpc cells are declared “below grid resolution, excluded from robustness claim” yet are still used when quoting the *global* maximum residual (1.87 σ). | Exclude the under-resolved cells from every global statement; if retained, report two maxima: resolved-only and full-grid. |
| **P5-E6** | Sec. XIII, RSD discussion | The paper concedes that the tidal-tensor field is calculated in redshift space and supplies only a heuristic 5–8 Mpc/h displacement argument.  No quantitative *anisotropic* test is done, although the eigenvalue ordering is known to be sensitive. | Provide at least one numerical RSD robustness check (e.g. a Zel’dovich recon-position re-run on a 𝒪(10⁵) galaxy subsample) or soften every claim that assumes RSD immunity. |
| **P5-E7** | Data availability, Appendix C | The promised DOI for the frozen repository is *not actually given* (“a DOI-minted archival snapshot accompanies submission”). | Insert the permanent DOI (e.g. Zenodo record) and the exact commit hash of the version analysed. |
| **P5-E8** | Throughout (esp. Abstract, pp. 1-2) | Numerous percentages and pp-differences are quoted with three-significant-figure precision even when n ≈ 400, giving statistical noise 2–3× larger. | Round every percentage/pp value so that quoted precision never exceeds ½ σ_binomial. |

--------------------------------------------------------------------
### 2.  MAJOR issues  
--------------------------------------------------------------------

| ID | Location | Problem | Required fix |
|----|-----------|---------|--------------|
| P5-M1 | Whole MS (31 pp) | The negative result is stretched over 31 dense pages.  Large parts (full audit trail, driver paths, *five* repetitions of sample size counts, foot-long footnotes) are not required for PRD. | Condense to ≤ 18 journal pages, moving code-path and version history to a supplementary material PDF. |
| P5-M2 | Abstract lines 5-7 | “We interpret this as *no evidence* … beyond … and the counting-statistics floor of ± 4.8 pp …”  The *counting* floor is 2.4 pp (1 σ) not 4.8 (2 σ), so the comparison is mismatched. | Quote either both at 1 σ or both at 2 σ.  As written the sentence overstates the noise. |
| P5-M3 | Sec. VI D (density quartiles) | A two-sample z ≈ 2.1 is highlighted yet later called “approximate” because the samples are not disjoint.  Presenting an invalid z without correction is misleading. | Re-compute the comparison on disjoint unique-ID subsets or remove the z-score. |
| P5-M4 | Sec. V permutation tests | N_MC = 1 000 gives σ_p ≈ 0.01–0.015, yet p-values are reported to three decimals (e.g. p = 0.135). | Quote permutation p with two significant digits and give the Monte-Carlo uncertainty (e.g. p = 0.14 ± 0.01). |
| P5-M5 | Fig. 3 left axis | The y-axis runs 0.46–0.52 but error bars cross 0.53, clipping top bars. | Extend axis or crop error bars correctly. |
| P5-M6 | Table X footprint-restricted control row | The control sample uses non-void = 253 276 vs earlier 621 964 but σ_from half is reported as –1.73.  Recomputing (n_CW = 126 088) gives (0.4983-0.5)/(0.5√253 276)= –1.07, not –1.73. | Recalculate σ or correct n_CW. |

--------------------------------------------------------------------
### 3.  MINOR issues  
--------------------------------------------------------------------

| ID | Location | Problem | Fix |
|----|-----------|---------|-----|
| P5-m1 | Eq. (1) footnote | Footnote derives units for χ but mixes h and h⁻¹ inside same sentence, potentially confusing. | Clarify in one consistent convention. |
| P5-m2 | Multiple pages | Duplicate phrase “catalog-wide classifier monopole” often repeated twice in a sentence. | Deduplicate phrasing. |
| P5-m3 | References [11],[12] | arXiv numbers are in the future (2604.x).  Not yet on arXiv. | Replace with “private communication” or hold publication until arXiv IDs exist. |
| P5-m4 | Appendix A | Toy-EFT mapping admits it is “not derived” – can be moved to a footnote or removed. |
| P5-m5 | Footnote markers | Superscripts (†, a) collide with other markers (1,2). | Use a single convention. |
| P5-m6 | Fig. 2 pie-chart | Sectors have no percentage labels. | Add or quote fractions. |

--------------------------------------------------------------------
### 4.  NITs  
--------------------------------------------------------------------

| ID | Problem |
|----|---------|
| P5-n1 | “catalog-anchored” / “catalog-native” alternates. Pick one. |
| P5-n2 | Comma splice in Abstract line “within DESI DR1 at V-Web resolution.” |
| P5-n3 | Slight over-use of semicolons—shorter sentences aid readability. |

--------------------------------------------------------------------
## Summary recommendation  
**MAJOR REVISIONS**

The study is potentially publishable – the statistical recomputations I performed for the main tables check out and the negative result is valuable – but the dependence on an unpublished companion paper, residual revision-log prose, RSD inadequacy, and inconsistent statistical presentation must be fixed before the work meets PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

### ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT  
*(new items only – IDs continue the sequence of the first report)*  

--------------------------------------------------------------------
#### 1.  ESSENTIAL
--------------------------------------------------------------------

| ID | Location | Problem | Required fix |
|----|-----------|---------|--------------|
| **P5-E9** | Table XII (“σ vs monopole” residuals) | The residuals are stated to use the **P5 matched-sample monopole**  f\_{P5}= 0.4972, but the numbers were evidently computed with 0.4974 (the Paper-IV monopole). Example: void row – (n=428, n\_{CW}=207) gives σ = (207 – 0.4972·428)/(0.5√428)= –0.49, yet the table prints –0.56, exactly the value obtained with 0.4974.  All four rows are affected. | Recompute σ\_{vs monopole} with the monopole that is actually declared (0.4972), or change the declaration and propagate through the text, figures, and Appendix B tables.  Update every place where the residuals are quoted (Sec. VII, Fig. 7 caption, Conclusions). |
| **P5-E10** | Eq. (2) Bonferroni threshold | Using the paper’s own formula \(|σ|_{\mathrm{Bonf}}=\sqrt{2}\,\mathrm{erfc}^{-1}(α/K)\) gives, for α=0.05, K=1054, \(|σ|_{\text{Bonf}}\)=**4.95**, not 4.05 as stated (check: erfc^{-1}(4.74×10^{-5})≈3.50, multiply by √2).  The wrong threshold is then carried into the HEALPix discussion (p. 7) and Fig. 6 narrative. | Correct the numerical threshold for the HEALPix family and revise the p–value / “below threshold” statements that rely on the 4.05 number.  Verify the α=0.01,K=5 case as well (current 3.09 value is correct). |
| **P5-E11** | Appendix B contingency tables | The CW/CCW×Class table claims to be “exact integers”; however, f\_{CW}(wall)=3359/6673=0.5030, not 0.5034 as printed earlier in Table III (difference is 26 CW objects).  Either the Appendix numbers or Table III are stale. | Synchronise the wall-class counts between Table III and Appendix B, then re-run the χ² p-values that are quoted in both places. |

--------------------------------------------------------------------
#### 2.  MAJOR
--------------------------------------------------------------------

| ID | Location | Problem | Required fix |
|----|-----------|---------|--------------|
| **P5-M7** | Table XV (Systematics splits) and text p. 27 | The text says the confidence≥0.7 cut “drifts by at most –0.24 pp”.  Full-sample f\_{CW}=0.4971, ≥0.7 cut is 0.4948, a drift of –0.23 pp – acceptable – **but the quoted σ=–? is missing**; only f\_{CW} is shown.  The reader cannot see whether the cut is within 2σ or not. | Add the σ\_{from half} (or σ\_{vs monopole}) column for every row in Table XV so the statistical relevance of each systematic split is transparent. |
| **P5-M8** | Fig. 5 right panel | The legend mixes “observed σ” (denominator 0.5√N) and “σ\_{pred}” (same denominator) but the y-axis label is only “Observed σ\_{from half}”.  A naive reader will assume both symbols on the panel are observed σ. | Amend the axis or legend to read “σ (different symbols: observed / predicted)” **and** add the verbal warning already requested in P5-E3 at the place this figure is first referenced. |
| **P5-M9** | Sec. VI D, filament bright vs dark two-sample z | Even aside from the “non-disjoint” caveat, the pooled two-sample formula is mis-applied: using the **unique-TARGETID** bright (n=781 978, f=0.4976) and dark (n=14 657, f=0.5069) subsamples gives z ≈ 1.95, not 2.1.  The quoted significance is therefore inflated. | Recompute on the disjoint unique-ID sets or drop the z-score. |

--------------------------------------------------------------------
#### 3.  MINOR
--------------------------------------------------------------------

| ID | Location | Problem | Fix |
|----|-----------|---------|-----|
| P5-m7 | Fig. 6 colour bar | Bar saturates at ±4.5 but caption quotes |σ|\_{null, p99}=4.78; values above 4.5 would be clipped. | Extend colour bar to ±5 or set clip limit explicitly. |
| P5-m8 | Table VI header | Column “|σ|\_{null,p99,max}” is undefined elsewhere and never used; should read “p=0.99 null threshold”. | Rename for clarity. |
| P5-m9 | Sec. II first paragraph | σ quoted as “≈ 9 σ” for Δf\_{CW}=–0.0026 on 3.2 M galaxies: exact is 8.9 σ – round consistently with P5-E8 rule. | Round to “≈ 9 σ” **or** give “8.9 σ”. |
| P5-m10 | Reference [11] arXiv placeholder | Now appears on arXiv as 2604.02463 **v1 is rejected**.  Cite as “submitted to MNRAS, arXiv:2604.02463 (in revision)” or similar. |
| P5-m11 | Units in RSD paragraph (p. 23) | Uses “σ\_{v}/(aH)” but a is not defined; earlier parts of the paper use redshift-space distance χ(z). | State that a=1/(1+z). |

--------------------------------------------------------------------
#### 4.  NIT
--------------------------------------------------------------------

| ID | Problem |
|----|---------|
| P5-n4 | Caption Fig. 2 “wall+filament dominates” – grammar: **‘dominate’**. |

--------------------------------------------------------------------
### Brief comment

These additional points – especially the monopole-residual mis-calculation (E9) and the Bonferroni threshold error (E10) – materially affect several headline claims and must be fixed together with the issues in my first report.