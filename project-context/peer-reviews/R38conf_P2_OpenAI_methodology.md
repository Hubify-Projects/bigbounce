# P2 R38conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.61.pdf` md5=6b413c94 pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6452 chars)
**Wall time**: 82.5s

---

# Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity:  
  A SPHEREx Sensitivity Recast with a MegaMapper Outlook’’

The paper presents a detailed discussion of the local–type bispectrum predicted by a matter-dominated contracting phase and recasts published SPHEREx and MegaMapper forecasts to assess the detectability of the benchmark value  
\(f_{\mathrm NL}=-35/8\).  The topic is interesting and relevant, but before the manuscript can be considered for publication in *Physical Review D* a large number of methodological and presentation problems must be fixed.  
Below I list all issues found after a full‐document audit, following the requested classification.

--------------------------------------------------------------------
## 1 Essential issues  – must be fixed for the paper to be reviewable
--------------------------------------------------------------------

| ID | Section / page | Problem | Required fix |
|----|----------------|---------|--------------|
| **P1-E1** | Sec. IV, Table IV, p. 19 | The effective uncertainty is obtained by **adding in quadrature a list of heterogeneous systematics (GR projection, \(b_\phi\) prior widening, photo-\(z\) outliers, template mismatch, ϵ-correction)** without demonstrating that the individual terms are uncorrelated.  | Either (i) supply a full joint Fisher (or likelihood) marginalisation that shows the correlations are negligible, or (ii) present a conservative **linear** sum.  The present quadrature treatment artificially tightens \(\sigma_{\rm eff}\) and inflates the quoted 2.6–5 σ headline. |
| **P1-E2** | Secs. II & III B, Eq. (5), p. 8 | The “template-overlap’’ correction multiplies the signal by \(r\) but leaves the variance at the **local-template** value \(\sigma(f_{\rm NL})=0.7\).  This is only valid if the estimator is re-optimised for the bounce shape or if the off-template variance gain is negligible, neither of which is shown. | Provide a Fisher matrix computed **with the bounce template itself**, or include the extra variance term arising from the mismatch.  The current treatment almost certainly over-states the detection significance. |
| **P1-E3** | Sec. IV, p. 10 & Abstract | All main σ values rely on Heinrich et al. (2024) without re-running their pipeline at the **bounce fiducial**.  The authors claim the linear-response approximation is good to <0.05 %, but the argument (Eq. 7) is only a dimensional estimate and not evaluated for the galaxy field. | Re-compute the Heinrich forecast with \(f_{\rm NL}=-35/8\) in the fiducial vector (or supply a fully quantitative six-point covariance correction) and update every σ and Bayes factor that uses σ = 0.7. |
| **P1-E4** | Sec. VI C, Table II, pp. 12-14 | The Bayes factors are quoted to 1-digit precision but are **extremely prior-dependent** (uniform width, Gaussian width, template re-scaling).  Several values differ by a factor > 2 when bookkeeping choices change. | Report Bayes factors only as *ranges* with an explicit dependence on each hyper-prior.  Remove the verbal claim “favours the bounce” unless you fix the priors from first principles. |
| **P1-E5** | Throughout (e.g. pp. 4, 6, 15) | Dozens of **internal bookkeeping tags** remain: e.g. *“artifact c9i epsilon ratio check.json’’*, *“c9g_bf_table_recompute.py’’*, *“artifact released with the paper’s code’’*.  These are not scientific prose. | Delete every internal path, file name, or development note from the PDF.  Provide a single DOI or Zenodo tag in the Data-availability section. |
| **P1-E6** | Abstract & Sec. I | The statement “forecast 5.2–5.5 σ (optimistic) reduced to 2.6–5 σ realistic’’ mixes σ obtained with different noise weightings and different systematic budgets **in the same sentence without the mandated “not directly comparable’’ warning**. | Split the statements and insert an explicit disclaimer whenever incompatible σ values are juxtaposed. |
| **P1-E7** | Sec. A.1, p. 24 | The derivation of the factor-of-two commutator doubling is said to be “verified symbolically’’ but only the *operator* identity is shown.  **No explicit numerical re-integration of the conformal-time integrals is provided.** | Plot or table the full bispectrum obtained with both orderings for at least one non-benchmark triangle and show numerical convergence to \(-35/8\). |
| **P1-E8** | Figs. 1 & 5 | The axes lack units and tick labels; Fig. 5 left panel has two curves but only one legend entry. | Add full axis labels, units, and legends. |
| **P1-E9** | Data & Code Availability, p. 23 | The repository path is a **moving GitHub branch** with no release tag or DOI.  PRD requires an immutable archive. | Deposit all material in Zenodo (or equivalent) with a versioned DOI and cite that DOI in the paper. |
| **P1-E10** | Refs. [27],[40] | Reference [27] is dated “2025”, [40] “2025”, but both arXiv IDs are **place-holders that do not exist yet**. | Replace with published or publicly available papers, or remove the citations. |

--------------------------------------------------------------------
## 2 Major issues  – significant revision needed
--------------------------------------------------------------------

| ID | Location | Problem | Suggested fix |
|----|----------|---------|---------------|
| **P2-M1** | Abstract & body | The phrase “minimally parameterised” is used, yet six undetermined polynomial coefficients remain.  | Re-phrase to “has a three-parameter null space in the chosen monomial basis’’ and quantify the resulting uncertainty in all final σ values. |
| **P2-M2** | Sec. III B, p. 8 - 9 | The “null-space’’ scan quotes \(r=0.85\pm0.13\) but then discards the ±0.13 in all subsequent forecasts. | Propagate the full scatter or demonstrate statistically that tails outside 0.84 ± 0.02 are negligible for the Fisher weights actually used. |
| **P2-M3** | Sec. IV, “Shot-noise caveat’’ | The shot-noise degradation is estimated with the heuristic \(\sqrt{1+1/(\bar n P_0)}\) but no numbers are shown for the SPHEREx photo-\(z\) selection. | Provide the actual \(\bar n P_0\) values per redshift bin and show the quantitative impact on σ. |
| **P2-M4** | Sec. VII C, Table III | GR marginalisation is implemented by adding \(\sigma_{\rm GR}\) in quadrature, but relativistic corrections are **shape-dependent**, not pure amplitude nuisances. | Either use the full relativistic transfer functions in the Fisher matrix or downgrade the GR row to a qualitative caveat. |
| **P2-M5** | Sec. D (Joint \(f_{\rm NL},n_{f_{\rm NL}}\)) | The joint Fisher uses only SDB information, yet the bispectrum is the dominant channel elsewhere.  The relevance of the nfNL constraint is therefore unclear. | Clarify whether you intend the joint constraint to *replace* or merely *supplement* the bispectrum result. |

--------------------------------------------------------------------
## 3 Minor issues
--------------------------------------------------------------------

| ID | Location | Problem | Fix |
|----|----------|---------|-----|
| **P3-m1** | Eq. (4), p. 7 | \(M(k,z)\) is missing a factor of \(g(z)\) or an explicit normalisation statement at \(z=0\). | Add the normalisation convention. |
| **P3-m2** | Table I, caption | “Folded (k1=2k2=2k3)” should read “\(k_1=2k,\;k_2=k_3=k\)”. | Edit caption. |
| **P3-m3** | Sec. II C | Assumption (f) mixes Hehl–Datta torsion with \(\Delta N_{\rm eff}\) limits in one sentence, making it hard to parse. | Split into two sentences. |
| **P3-m4** | Fig. 2 caption | “template-corrected optimistic bispectrum forecast 5.2–5.5 σ’’ – specify that this is **for SPHEREx only**. | Clarify. |
| **P3-m5** | Repeated text | Duplication: “shape cosine exceeds 0.97 for all 10 000 samples” written twice (pp. 3 & 4). | Remove duplicate. |

--------------------------------------------------------------------
## 4 Nits
--------------------------------------------------------------------

| ID | Location | Problem | Fix |
|----|----------|---------|-----|
| **P4-n1** | Abstract | Mixed en-dash and minus signs (e.g. “−35/8 = −4.375”). | Use en-dash only for ranges. |
| **P4-n2** | p. 6 | “which we do not use this scaling” – grammar. | “which we therefore do not use”. |
| **P4-n3** | Bibliography | Ref. [18] cites “2026” but paper not yet published. | Mark as “in preparation’’ or remove year. |

--------------------------------------------------------------------
## Summary recommendation
**MAJOR REVISIONS**

The manuscript contains interesting material but the statistical treatment of the forecast is not yet robust enough for publication in *Physical Review D*.  In particular, the simplistic handling of template mismatch, the ad-hoc quadrature of systematic errors, the missing recomputation of the Fisher matrix at the bounce fiducial, and the prior-sensitive Bayes factors must all be corrected or replaced by rigorous derivations.  I therefore recommend major revisions and a full re-review after the essential items above are addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

### ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT  
(The numbering continues the scheme of the first report.  Only **new** items appear below.)

--------------------------------------------------------------------
## 1 Essential issues  – additional blocking problems
--------------------------------------------------------------------

| ID | Section / page | Problem uncovered on second pass | Required fix |
|----|----------------|----------------------------------|--------------|
| **P1-E11** | Sec. III B, Eq. (6) vs. text pp. 8–9 | Eq. (6) quotes **\(r = 0.84\pm0.02\)**, i.e. the 1 σ interval [0.82, 0.86], but in the same paragraph the allowed noise–weighting range is stated as **0.829 – 0.876**.  The upper endpoint 0.876 lies **5 σ outside** the quoted uncertainty band, so either the band is wrong or it is not 1 σ. | Recompute the error bar from the actual weighting distribution and state *clearly* which confidence level it represents.  Update every place where \(\pm0.02\) is propagated into σ or Bayes factors. |
| **P1-E12** | Eq. (4), p. 7 | The Poisson kernel is written \(M(k,z)=2k^{2}T(k)D(z)/(3\Omega_m H_0^2)\).  The standard GR normalisation is \(M= \dfrac{2}{3}\dfrac{k^{2}T(k)D(z)}{\Omega_m H_0^{2}}\).  As written, the equation is larger by a factor **\(3/2\)** and therefore **changes the scale-dependent bias amplitude and every derived σ(f\_NL)**. | Restore the missing \(2/3\) normalisation or supply a derivation of the alternative convention, then recompute all SDB-based numbers. |
| **P1-E13** | Fig. 2 caption vs. body (p. 10) | Caption claims the **“template-corrected optimistic bispectrum forecast 5.2–5.5 σ’’** refers to SPHEREx only, but the body paragraph immediately to the left combines SPHEREx and MegaMapper bars in the same colour scheme with no “not directly comparable’’ warning. | Separate the two surveys in the caption and insert the PRD-required disclaimer that the σ values are derived from *independent* null procedures. |
| **P1-E14** | Abstract sentence 4 | States “\(r\) is applied as a shape-weighted degradation … making this a sensitivity *recast* rather than an independent forecast’’.  The body (Sec. III B) twice calls the same calculation an “*overlap validation*’’ and “*Fisher overlap*’’ implying a forecast. | Choose one description (recast **or** forecast) and use it consistently in the abstract, intro, and Sec. III B.  Otherwise the abstract mis-represents the work. |
| **P1-E15** | Cross-ref. “cf. Sec. VII and Eq. (7)” in Abstract & p. 1 | Eq. (7) is located in **Sec. IV**, not Sec. VII.  The cross-reference is wrong in two places (abstract and p. 1). | Correct all cross-references to Eq. (7). |

--------------------------------------------------------------------
## 2 Major issues  – additional significant problems
--------------------------------------------------------------------

| ID | Location | Problem | Suggested fix |
|----|----------|---------|---------------|
| **P2-M6** | Figs. 1 & 5; axis text | Units/tick marks absent (already flagged for Fig. 5 in first report) **and** the *body* describes Fig. 1 as “BNL vs \(k_1/k\)’’ whereas the x-axis in the PDF is simply “k/k”.  Likewise Fig. 5 caption says “σ(fNL) vs. b prior width’’ but the x-axis reads “b prior uncertainty [%]’’ with no label of the y-axis at all. | Fix axis labels so that they exactly match the body descriptions; add units. |
| **P2-M7** | Sec. VI C, Bayes-factor grid | The SSFSR Bayes factor is given as **3.5 × 10^8** in Table III but the body text directly above says the continuous σ\_GR hyper-prior gives **8.6 × 10^3** — a factor **40** discrepancy. | Identify where the arithmetic differs (fixed-σ vs. marginalised) and present the two numbers side-by-side with clear labels; otherwise the reader cannot reproduce the table. |
| **P2-M8** | Appendix A.1 vs. main text Sec. A.2 | Appendix derives the −2 Im commutator factor but **never shows a numerical integral** for a non-benchmark triangle, yet Sec. A.2 Table V claims confirmation.  No file or plot is included. | Provide the explicit numerical check requested in P1-E7 (plot or table) and reference it in both Appendix A and main text. |
| **P2-M9** | Eq. (10) consistency relation | Uses \(c'=\kappa_\epsilon/8\in[0.7,10]\).  Inserting \(c'=0.7\) and Planck \(n_s=0.965\) gives \(f_{\rm NL}=-4.35+0.028\approx -4.32\), contradicting the earlier statement that the correction is “0.6–8 %’’ (which would be −4.10 to −4.35). | Re-compute the numerical range or correct the quoted percentage. |

--------------------------------------------------------------------
## 3 Minor issues  – additional observations
--------------------------------------------------------------------

| ID | Location | Problem | Fix |
|----|----------|---------|-----|
| **P3-m6** | Sec. III A, sentence after Eq. (4) | Says “all downstream Fisher weightings … use Eqs. (3)–(4) as the canonical definition”.  Eq. (3) contains \(\delta_c\) but the text never states the numerical value adopted (1.686 or modified?). | State the exact value of \(\delta_c\) used in every Fisher run. |
| **P3-m7** | Table IV, row “\(ϵ\)-correction’’ | The row claims “\(\lesssim0.1σ\) effect’’ but no calculation is shown. | Add a one-line arithmetic showing how 8 % of 4.375 with \(σ=0.7\) yields the stated <0.1 σ. |
| **P3-m8** | Bibliography | Ref. [41] cites Cosmoglobe DR1 as “A&A 679”, but A&A volume 679 has not yet been assigned (as of 2026). | Mark as “in press’’ or leave volume blank. |

--------------------------------------------------------------------
## 4 Nits
--------------------------------------------------------------------

| ID | Location | Problem | Fix |
|----|----------|---------|-----|
| **P4-n4** | p. 6, last line | “the estimator is **a** CMB-estimator heuristic” – missing article. | Insert “a”. |
| **P4-n5** | Eq. (A7) | Final parenthesis after summation mismatched. | Add closing bracket. |

--------------------------------------------------------------------
## Summary of second-pass audit
A fresh arithmetic and cross-reference check uncovered **five additional essential problems** (incorrect r uncertainty, wrong normalisation in Eq. 4, conflicting cross-references, figure/body mismatches, and inconsistent description of the work), plus several major consistency and arithmetic errors.  These are *in addition* to the deficiencies listed in the first report and further reinforce the **major revision** recommendation.