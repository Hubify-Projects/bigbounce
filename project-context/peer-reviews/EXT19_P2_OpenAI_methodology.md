# P2 EXT19 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=dbcc5834 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6528 chars)
**Wall time**: 101.9s

---

# Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity:  
A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

I have examined the full 29-page manuscript, all equations, tables, figures and the
companion arguments that lead to the quoted detection significances and Bayes
factors.  Below I list the problems I found, each classified as ESSENTIAL,
MAJOR, MINOR or NIT according to PRD methodology standards.

------------------------------------------------------------------
## ESSENTIAL problems  – must be fixed before the paper can be considered
------------------------------------------------------------------

| ID | Section / page | Problem | Required fix |
|----|----------------|---------|--------------|
| **P2-E1** | Abstract & p.10 (Fig. 2) | Multiple σ values that come from mutually incompatible null procedures (6.25 σ naïve / 5.2–5.5 σ template–corrected / 2.6–5 σ “realistic”) are juxtaposed without an explicit “NOT COMPARABLE” warning every time they are plotted or quoted.  Fig. 2 shows the three bars side-by-side and only the hatched comment in the caption attempts a disclaimer.  PRD guideline #7 demands a disclaimer at every juxtaposition. | Wherever different σ’s appear together (Abstract, §IV first paragraph, Fig. 2 caption and body text) add an **explicit sentence** stating they are derived from different likelihoods and cannot be compared quantitatively.  Alternatively drop the 6.25 σ bar entirely. |
| **P2-E2** | §IV pp. 8–10 | The adopted σ(fₙₗ)=0.7 from Heinrich et al. is *re-used* at the bounce fiducial without demonstrating the Fisher matrix is invariant under a 6.3 σ shift in the parameter.  The manuscript supplies only a heuristic Eq.(7).  This is not an acceptable proof for PRD. | Supply a *proper* Fisher‐matrix recalc (or an analytic bound) that shows the covariance changes by <1 % when the fiducial is moved from fₙₗ = 0 to −4.375.  Otherwise inflate σ(fₙₗ) by the calculated correction and propagate through the whole paper. |
| **P2-E3** | §III B p.8 | The 0.84 ± 0.02 template-overlap factor r is obtained from only four ad-hoc weighting schemes, none of which reproduces the actual SPHEREx multi-tracer Fisher weight.  Yet r is the leading multiplicative factor in every σ estimate. | Derive r directly from the SPHEREx Fisher matrix (or supply the cross-Fisher projection) rather than from heuristic weights.  Quote the resulting mean and uncertainty and propagate it throughout. |
| **P2-E4** | §III B p.7 | The “null-space” sampling that produces r = 0.85 ± 0.13 uses an *arbitrary* Euclidean measure in coefficient space and a fixed radius R=50.  No argument is given that the induced prior is physically meaningful. | Provide a physically‐motivated prior (e.g. derived from an action-level amplitude bound) **or** show that alternative priors (radius, metric) change r by < 2 %. |
| **P2-E5** | §VII C, Table III | Systematics are combined purely in quadrature even though several of them are strongly correlated (bφ with GR projection, photo-z with k-min).  No covariance matrix is presented. | Either (i) provide the full joint Fisher including all nuisance parameters, or (ii) present evidence that the neglected covariances change the final σ by < 10 %.  Otherwise all quoted 2.6–5 σ “realistic” numbers are unsupported. |
| **P2-E6** | Data & code availability p.24 | A permanent archive DOI is promised (“DOI inserted at submission”) but **no DOI or commit hash is given**.  PRD reproducibility policy requires a *frozen* reference. | Deposit the exact code and data set used to produce the figures in a public archive and cite its DOI and commit hash in the manuscript. |
| **P2-E7** | Throughout (e.g. p.6 footnote 2, p.17 first col.) | Several internal audit file names (“c9i epsilon ratio check.json”, “phase3 fisher overlap.json”, …) and review-process prose remain in the body of the paper. | Delete all residual internal file-path references, audit tags and review comments from the published version. |

------------------------------------------------------------------
## MAJOR problems – important but do not automatically block acceptance
------------------------------------------------------------------

| ID | Section / page | Problem | Recommended fix |
|----|----------------|---------|-----------------|
| **P2-M1** | §IV p.9 | The injection/recovery test that reports r_meas = 0.90 ± 0.01 uses only **200** Monte-Carlo realisations but claims a ±0.01 precision (0.6 %).  With σ≈0.03 the formal error should be ≈0.0022N^-½ ≈0.002, so the test is *shot-noise-limited* and does not validate the 0.84–0.90 spread. | Increase the number of MC realisations by at least an order of magnitude *or* downgrade the claimed precision. |
| **P2-M2** | §V p.11 | MegaMapper significance 7.4–7.7 σ is quoted although the paper concedes the GR and bφ systematics at z = 2–5 are “not independently calibrated”. | Either remove the 7 σ figure from the conclusions or provide a quantitative error budget calibrated to a Stage-V high-z survey. |
| **P2-M3** | §VI p.13 | The Bayes factor calculation assumes a *uniform* prior of width W but later switches to a Gaussian prior for the bounce without re-normalising the evidence on the same parameter space. | Give the complete marginal likelihood with identical support for both models, or explicitly justify why the evidences are comparable despite different prior families. |
| **P2-M4** | Fig. 1 & Table I | The polynomial coefficients (2, 7, 3, −12, −69, 19) are stated to fit *all* Cai benchmarks but the numerical value −3.984 in Table I differs from the exact −255/64 ≈ −3.984375 quoted in the same row at the 4th decimal place. | Provide the exact double-precision evaluation or round consistently. |
| **P2-M5** | §VIII p.21 Eq.(12) | The range κ_ε ∈ [5.6, 80] spans more than an order of magnitude but is later treated as a 0.6–8 % uncertainty in fₙₗ.  The arithmetic gives Δfₙₗ ≈ κ|Δε| ≈ 80 × 0.0045 ≈ 0.36 → 8.2 %.  The lower bound gives 0.025.  The paper should state the *full* possible excursion (0.03–0.36). | Quote the full numeric range and propagate the larger ±8 % uncertainty through the Bayes-factor and σ budgets. |
| **P2-M6** | §III A Eq.(3) | ∆b(k,z) is written with numerator “2 fₙₗ(b₁−1) δ_c / M(k,z)” but *M* already contains the growth factor *D(z)* in the denominator.  The displayed Eq.(4) divides by *D(z)* again, introducing D(z)² in ∆b. | Correct the dimensional inconsistency and re-check all SDB Fisher numbers that depend on ∆b. |

------------------------------------------------------------------
## MINOR issues
------------------------------------------------------------------

| ID | Section / page | Problem | Fix |
|----|----------------|---------|-----|
| **P2-m1** | Abstract line 17 | “MegaMap­per” mis-capitalised once (“MegaMap­per … could reach …”). | Use the official “MegaMapper”. |
| **P2-m2** | §III B footnote 3 | Claim “r ≤ 1 holds strictly” then immediately notes r > 1 realisations.  The logical sequence is confusing. | Rephrase footnote. |
| **P2-m3** | §VI C p.13 | Two different notations  W  and  Δ  are used for the same prior width. | Harmonise. |
| **P2-m4** | Several figures | y-axis unit missing in Fig. 4 right panel (σ units?). | Add axis labels and units. |
| **P2-m5** | Bibliography | Refs. [37] & [38] list publication years 2025 & 2025 but the cited documents are still arXiv drafts. | Update or mark “arXiv e-prints”. |

------------------------------------------------------------------
## NITs
------------------------------------------------------------------

| ID | Section / page | Problem | Fix |
|----|----------------|---------|-----|
| **P2-n1** | p.5 col.1 l.15 | Duplicate phrase “pre-systematic baseline baseline”. | Remove duplicate word. |
| **P2-n2** | Figure 3 caption | “legend label ‘bounce excluded’” – legend actually reads “bounce excluded”.  Capitalise consistently. | Tweak caption. |
| **P2-n3** | Several places | “Higuchi bound which applies to spin-2 fields” appears twice verbatim. | Delete duplicate sentence. |

------------------------------------------------------------------
## Summary recommendation  
**MAJOR REVISIONS**

The manuscript contains an impressive amount of technical work, but several
core quantitative results (template-overlap factor, Fisher re-centring, combined
systematics) are not demonstrated with sufficient methodological rigour for
PRD.  In its current form the detection significances and Bayes factors are not
fully supported.  If the authors address the ESSENTIAL points listed above and
supply the requested calculations, the paper may become suitable for
publication, but a substantial methodological revision is required.

---

## PASS 2 — self-critique findings (what initial review missed)

Additional findings after second‐pass audit
===========================================

The items below are **new** – none of them appeared in my first report.  
Numbering continues the same scheme (E = ESSENTIAL, M = MAJOR, m = MINOR,
n = NIT).

------------------------------------------------------------------
## ESSENTIAL problems discovered on the second reading
------------------------------------------------------------------

| ID | Section / page | Problem | Required fix |
|----|----------------|---------|--------------|
| **P2-E8** | §III A Eq.(4) + surrounding text | The transfer kernel is written  
`M(k,z)=2 k² T(k) D(z)/(3 Ωₘ H₀²)` **and nowhere in the paper is the scale
factor a(z) carried**.  But in Eqs.(3)–(4) the authors use comoving
wavenumbers `k` while the Poisson equation that produces the `2/3ΩₘH₀²`
factor is in *physical* coordinates.  The correct kernel therefore contains an
extra factor `1/a²(z)` (or, equivalently, `D(z)/a(z)` if the growth factor is
normalised to unity today).  With the scale factor missing the bias
correction picks up an un-physical `(1+z)⁻²` error which directly enters every
SDB Fisher number (σ(fₙₗ), Fig. 4 & 5, Table IV). | Insert the missing
`a⁻²(z)` factor (or re-define `D(z)` accordingly), recompute ∆b(k,z), *re-run
all Fisher matrices that use SDB weights* and propagate the corrected σ(fₙₗ)
through the whole paper.  A statement that the sign error is negligible is
not sufficient – the Fisher elements scale as ∆b². |
| **P2-E9** | §VI Eq.(9) | The closed-form Bayes-factor numerator is
written as `W / (√2π σ_eff)` but it should be
`W × exp[ –(Δf)²/(2σ_eff²) ] / (√2π σ_eff)`.  
The exponential factor was lost when copying the Gaussian value from Eq.(8).  
The numerical example in the paragraph that follows (giving BF = 17.10 for
W = 30, σ = 0.7) is therefore wrong by a factor  
`exp[(Δf)²/(2σ²)] = exp[0] = 1` *only because the worked example happens to
evaluate at Δf = 0*.  Everywhere else (e.g. the narrow-prior column and the
GR-marginalised rows) the missing exponential **changes BF by up to a factor
≈ 1.5–2**. | Restore the exponential factor to Eq.(9), recompute every BF in
Table II & III and in the abstract. |
| **P2-E10** | Abstract, p.3 (Table I), p.20 (Table IV) | The paper claims a
“0.6–8 % ε-correction” but uses ±0.02 (≈ ±2 %) when it is propagated in
Table IV.  With κ_ε ≈ 80 (upper range given in §VIII) the full shift is
Δfₙₗ ≈ 0.36 → **±8 %**, not 2 %. | Replace the ±0.1 σ entry in Table IV by the
correct ±0.35 σ, widen all affected σ bands and update every quoted
detection/BF range that depends on that row. |
| **P2-E11** | Fig. 5 right panel vs. caption | Caption says the y-axis is
“Detection significance”, body text (p.17 col. 1) quotes the same curve as
σ(fₙₗ).  The plotted values (e.g. 4 at 20 %) match *σ* not *significance*.
| Fix the axis label and the caption, and ensure the numbers in the main
text match the corrected plot. |
| **P2-E12** | §IV first paragraph & Fig. 2 | Numbers quoted for the
“all-combined conservative endpoint” are 2.6–2.8 σ in the text but the bar in
Fig. 2 is drawn with an *upper* value ≈ 3.0 σ. | Harmonise figure and text and
state explicitly which σ_eff row in Table IV the bar corresponds to. |

------------------------------------------------------------------
## MAJOR problems newly detected
------------------------------------------------------------------

| ID | Section / page | Problem | Recommended fix |
|----|----------------|---------|-----------------|
| **P2-M7** | Eq.(10) derivation, p.13 | The “large-W approximation”
`B≈W/(√2πσ)` is used later in the text for W = 10, σ = 0.7 even though
W/σ ≈ 14 is **not** in the asymptotic regime (tail CDF terms contribute
≈ 18 %). | Do not use Eq.(10) for W/σ < 25, or quote the resulting ≥ 15 %
systematic in the BF column. |
| **P2-M8** | Fig. 4 left axis | Units are labelled “σ(fNL)” but the numbers
(0.5, 1, 2) correspond to σ(fNL) **squared** as used in the Fisher element
`1/σ²`. | Relabel the axis or replot the correct σ values. |
| **P2-M9** | §III B footnote 3 | States that r ≤ 1 holds “strictly for
canonical single-field bispectra” but Fig. 1 already shows r > 1 for the same
single-field limit configuration.  The logical contradiction is not merely a
phrasing issue. | Clarify that the monotonicity statement applies to shapes
monotonic in the squeezed-limit *amplitude*, not to the Fisher-weighted r
defined here. |
| **P2-M10** | Appendix A Eq.(A7) | Symmetry factor S_ζẋζ² is listed as 2,
but the vertex has two identical **time-ordered** ẋζ legs *and* an
identical-field external contraction, giving S = 4 in the doubled (–2 Im)
integrand. | Re-evaluate the prefactor: if S = 4 the –35/8 normalisation is
affected by ½ at this vertex.  Show the numeric cancellation explicitly. |

------------------------------------------------------------------
## MINOR issues newly found
------------------------------------------------------------------

| ID | Section / page | Problem | Fix |
|----|----------------|---------|-----|
| **P2-m6** | Abstract l.22 | “parameter **free** single-field slow-roll” –
standard SR has ns and A_s as free parameters; better “parameter‐fixed *fₙₗ*
prediction”. | Rephrase. |
| **P2-m7** | §II p.4 last ¶ | Claims the null-space scan is “basis-independent” after previously warning it is basis-dependent. | Remove contradiction or add qualifier. |
| **P2-m8** | Table II header | “BF vs **SSFSR**” acronym never defined in
the text. | Define on first use. |
| **P2-m9** | Ref.[40] | Year is given as 2025 but arXiv ID shows 2024. |
Correct bibliographic year or mark “submitted 2024”. |

------------------------------------------------------------------
## NITs
------------------------------------------------------------------

| ID | Section / page | Problem | Fix |
|----|----------------|---------|-----|
| **P2-n4** | p.6 col. 1 line 9 | “unweighted distribution has an *asymmetric*
tail” – grammatically “has asymmetric tails”. | Grammar. |
| **P2-n5** | p.11 Fig. 2 legend | “All-combined conservative endpoint
2.6–2.8 σ” – en-dash should be “2.6–2.8 σ”. | Typography. |

------------------------------------------------------------------
### Overall
Several numerical and methodological inconsistencies were uncovered on this
second pass, most importantly the missing scale-factor in ∆b(k,z) and the
omitted exponential in the Bayes-factor formula.  These directly affect every
quoted σ and BF and must be resolved before the manuscript can be considered
further.