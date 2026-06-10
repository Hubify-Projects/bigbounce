# P5 R24conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.53.pdf` md5=b86b03f9 pages=25
**Input format**: NATIVE PDF (inline or Files API) + pass-2 NO_NEW
**Wall time**: 165.1s

---

Here is a referee report for the submitted manuscript.

## Referee Report: "Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals"

This manuscript presents a detailed investigation into the potential dependence of spiral galaxy chirality on the large-scale structure environment. The authors cross-match a large catalog of spiral galaxies with spectroscopic data from DESI Data Release 1, classify their environments using multiple cosmic-web finders (primarily a V-Web tidal-tensor classifier and the DESIVAST void catalog), and perform a rigorous statistical analysis. The headline result is a null detection: the fraction of clockwise (CW) spirals is found to be independent of environment (void, wall, filament, or cluster) down to the sensitivity limits of the data, once a small, global, catalog-wide monopole bias (attributed to the chirality classifier and quantified in a companion paper) is accounted for. The paper's strength lies in its comprehensive suite of robustness checks, including sensitivity sweeps of algorithm parameters, cross-validation against independent classifiers (Tempel+2014 FoF, ASTRA), and detailed systematics tests.

The analysis is thorough, the statistical methods are sound, and the conclusions are well-supported by the evidence presented. The authors demonstrate a sophisticated understanding of potential systematics, from redshift-space distortions to survey-edge effects, and address them transparently. The explicit declaration of primary and secondary analysis paths, along with the open documentation of superseded calculations from earlier drafts, is a commendable example of scientific rigor and transparency. The paper is a significant contribution, providing a strong empirical constraint on any physical models that might predict an environment-dependent parity violation at these scales.

While the paper is of high quality, I have identified a few points that require clarification or minor correction before publication.

---
### Findings

#### ESSENTIAL

None.

#### MAJOR

None.

#### MINOR

**ID: P5-M1**
- **Location:** Section V A, page 5, Equation (2)
- **Problem:** The description of the parametric Bonferroni correction is slightly ambiguous. The text states "for K independent bins tested at the nominal two-sided per-bin significance α", but the calculation `|σ|Bonf ≈ 3.09` for K=5, α=0.01 corresponds to a threshold where the *family-wise error rate* is α=0.01. If α were the per-bin significance, the family-wise rate would be approximately Kα = 0.05.
- **Fix:** Please clarify the text to state that α is the desired family-wise error rate for the set of K tests. For example: "For K independent bins, to achieve a family-wise error rate of α under a Bonferroni correction, the per-bin two-sided significance threshold on the maximum-absolute-σ statistic is..."

**ID: P5-M2**
- **Location:** Section VI A, page 6
- **Problem:** The text states that the negative σ values in filament and cluster "track the catalog-wide classifier-monopole offset", predicting `σ_pred(filament) ~ -3.32` and `σ_pred(cluster) ~ -3.28`. The observed values are -2.61 and -4.66, respectively. While the filament value is reasonably close, the cluster value deviates by ~1.4σ from the simple prediction. The text qualifies this by saying they are "both within order-unity of observation", which is a bit imprecise. The crucial point, which is made clearly in Table X, is that the formal monopole-subtracted residual is small (`|σ_vs_monopole| < 1.15`).
- **Fix:** To strengthen the argument, I suggest slightly rephrasing this paragraph to de-emphasize the raw prediction and more quickly point to the formal residual test as the definitive one. For instance, after presenting the predicted values, add a sentence like: "While the raw values are of the expected sign and magnitude, the formal test of the residual signal after monopole subtraction, presented in Sec. VIII F and Table X, provides the most precise test and confirms the absence of a significant environmental signal."

**ID: P5-M3**
- **Location:** Section IX C, page 20
- **Problem:** The comparison of V-Web and T-Web (Ref. [11]) volume fractions notes that "V-Web's void fraction is higher than T-Web's by +8-18 pp" and "V-Web's cluster fraction is lower than T-Web's knot fraction by 3-5 pp". The text correctly attributes this to survey-shell systematics. However, the V-Web volume fractions are {0.244, 0.413, 0.333, 0.010} and the T-Web (BGS) fractions are {0.16, 0.45, 0.37, 0.04}. The differences are: void +8.4 pp, wall/sheet -3.7 pp, filament -3.7 pp, cluster/knot -3.0 pp. The quoted ranges in the text seem to cover multiple tracer samples from Ref [11].
- **Fix:** For clarity, please explicitly state the V-Web vs T-Web (BGS) differences directly, as calculated here, before giving the broader range from the other tracer samples in Ref [11]. This makes the primary comparison more direct.

#### NIT (Nitpick/Cosmetic)

**ID: P5-N1**
- **Location:** Abstract, page 1
- **Problem:** The abstract states "The quoted σ_from_half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n." This is a correct and important statistical point. However, the sentence is slightly long and could be more direct.
- **Fix:** Suggest rephrasing for conciseness, e.g., "Note that σ_from_half values are not directly comparable across classes due to their √n scaling; formal comparisons use monopole-subtracted residuals."

**ID: P5-N2**
- **Location:** Section VIII F, page 16
- **Problem:** The text states "the P4 monopole Δf_cw = -0.0026 projects to σ_pred ~ 4.6σ on the chirality-relevant subsample; the observed -5.00σ corresponds to Δf_cw ~ -0.0028". The calculation is `σ = 2 * Δf_cw * sqrt(N)`. For N=791,635, `2 * (-0.0026) * sqrt(791635) = -4.62`. This matches the `~4.6σ` claim. The observed -5.00σ implies `Δf_cw = -5.00 / (2 * sqrt(791635)) = -0.00281`. This also matches. The text is correct, but the symbol `f_P4` is used for the catalog-level value, while the text later introduces `f_P5` for the matched-sample value. The naming could be slightly confusing.
- **Fix:** This is a very minor point, but consider clarifying the P4/P5 notation slightly earlier or ensuring it is used consistently to refer to the Paper IV catalog value vs. the DESI matched-subsample value. The current explanation is sufficient but requires careful reading.

**ID: P5-N3**
- **Location:** Throughout
- **Problem:** The manuscript is quite long (25 pages). While the extensive cross-checks justify the length, the density of information can be challenging.
- **Fix:** No change is required, as the structure is logical and the detail is necessary to support a null claim. However, the authors might consider if any of the secondary cross-checks in Section IX could be briefly summarized in the main text and detailed further in an appendix to improve readability, though the current structure is acceptable.

---
## Summary recommendation

**ACCEPT WITH MINOR CORRECTIONS**

This is an exceptionally thorough and well-executed study. The authors present a convincing null result for the environmental dependence of spiral chirality, supported by an exhaustive set of robustness and systematics checks that should serve as a model for similar studies. The paper is transparent about its methodology, limitations, and even its own analysis history. The minor issues identified are primarily for clarification and do not detract from the validity of the work. After these small corrections are addressed, the paper will be an excellent addition to the literature and is highly suitable for publication in Physical Review D.