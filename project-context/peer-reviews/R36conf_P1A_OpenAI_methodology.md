# P1A R36conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.66.pdf` md5=5dff8674 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4655 chars)
**Wall time**: 123.4s

---

# Referee report on P1A (Round R36conf)

I have read the full 28-page manuscript, every equation, figure, table and foot-
note, and verified all numerical claims that can be reproduced from the text.  
Below I list the problems that must be fixed before the paper can be considered
by *Physical Review D*.  Findings are grouped by severity.

--------------------------------------------------------------------
### ESSENTIAL (must be fixed for further consideration)

| ID | Location | Problem | Required fix |
|----|----------|---------|--------------|
| **P1A-E1** | p. 3, col. 2 “Companion paper — ΛCDM+∆N_eff … documented separately in companion work in preparation [6]” and similar statements on pp. 4, 10, 15, 24 | Several load-bearing results (MCMC posteriors for H₀, σ₈, ∆N_eff; NaMaster validation; ALP parameter inference; SPHEREx Fisher matrices; GPU PTA chain) are outsourced to companion papers that are “in preparation” and not available to the reader.  The conclusions of the present paper (e.g. the 2.6–5 σ f_NL forecast and the LiteBIRD 9 σ β claim) are not reproducible from the material actually contained in this manuscript. | Either (i) supply *all* numerical analyses, chain settings, and convergence diagnostics **within this manuscript or its supplementary material**, or (ii) wait until the companion papers are published and cite their exact arXiv numbers so the reader can verify every result. |
| **P1A-E2** | p. 19, Eq. (23) & discussion | The “perturbation-transparency” theorem is stated but not proved.  The text claims that ½ ε^{μνρσ}R_{μνρσ}(Γ̄)=0 “by the first Bianchi identity”, but gives no explicit demonstration in the scalar-vector-tensor decomposition, no treatment of boundary terms, and no check that the statement survives when metric perturbations are kept to higher order. | Provide a **complete derivation** (or a published reference) showing that the Holst dual vanishes identically for *all* scalar and tensor perturbations around a FLRW background, including any surface terms.  Specify the gauge used and show the vanishing mode-by-mode. |
| **P1A-E3** | p. 13, Route 4 | The paper claims that matching β_obs with the operator −(α/4M) θ F F̃ “requires m_θ ≈ H₀” and that therefore the model “re-imports the cosmological-constant problem”.  The argument ignores the fact that β∝ α/M while ρ_θ∝(α/M)⁻².  An α/M *different* from the one-loop estimate would allow simultaneous matching of β and ρ_Λ at arbitrary m_θ. | Either (i) demonstrate that α/M is *fixed* (not just estimated) by the one-loop calculation used, including a quantified uncertainty band, or (ii) downgrade the “closure” of Route 4 to a conditional statement that applies **only** if α/M is restricted to the stated value. |
| **P1A-E4** | p. 1 abstract, last sentence | “The two predictions discussed below as ‘surviving’ are accordingly not predictions of ECH itself, but … we report them here because they remain testable signatures …” — In the abstract the same two observables are presented as **results** of the paper.  This overstates what is actually derived. | Rewrite the abstract so that it distinguishes clearly between results **proved** in the paper and external class-level predictions that the present work merely does not exclude. |
| **P1A-E5** | Figures 4 & 6 and associated text | The LiteBIRD “∼9 σ” claim is obtained by dividing 0.27° by 0.03°, i.e. by assuming β₀ = 0 as the null.  In the same sentence the paper compares that number to the WMAP+Planck central value 0.342° ± 0.094°, which corresponds to only 2.9 σ from zero.  Mixing significances from **different null procedures** without an explicit warning violates the PRD statistical-rigour guideline. | 1. State *explicitly* which null hypothesis each σ refers to every time the numbers are juxtaposed.  2. Remove the phrase “∼9 σ detection” unless you also quote the σ with respect to the current central value (≈0.7 σ). |
| **P1A-E6** | Data & Code Availability (p. 25) | The promised Zenodo DOI is “to be inserted”.  GitHub master branch can mutate after publication; PRD requires an immutable archived release for reproducibility. | Archive the exact code and data used for the paper on Zenodo (or equivalent) and include the permanent DOI in the manuscript. |

--------------------------------------------------------------------
### MAJOR (significant revision required)

| ID | Location | Problem | Suggested fix |
|----|----------|---------|---------------|
| **P1A-M1** | Throughout (e.g. abstract, p. 10, p. 16) | The paper repeatedly asserts that it “closes” four routes “at amplitude-budget granularity”, but two of the closures (Routes 2 and 3) rely only on **order-of-magnitude** estimates labelled “phenomenological ansatz”. | Re-word all such statements to “constrain under specified scaling assumptions”.  Provide a sensitivity analysis showing how many OOMs of head-room remain if the ansatz coefficients vary within 1-loop theoretical uncertainty. |
| **P1A-M2** | p. 16, Table II | Several “barriers” (5, 6, 10, 11, 13) are qualitative or philosophical, with no quantitative bound.  Presenting them in the same table as quantitative constraints is misleading. | Separate strictly quantitative constraints from purely conceptual points, or provide equations that translate each barrier into an explicit numerical limit. |
| **P1A-M3** | p. 5 Fig. 1, p. 17 Fig. 5 | Axes lack units, tick values or error bars.  Figure 5 bottom panel shows “Fine-Tuning Score” without defining how the score is computed for f(R) or quintessence. | Add complete axis labels, units and a methodological footnote explaining the computation for every bar shown. |
| **P1A-M4** | p. 6, Eq. (6) and Appendix B | The operator Seff has mass dimension 1; the paper concedes this but still inserts it into a 4-D action without showing how to cure the mismatch. | Either (i) promote the operator to dimension 4 by inserting the required M_P³ factor and repeat all subsequent estimates, or (ii) show explicitly (with a cited EFT treatment) that the operator is to be viewed as a *density* that acquires additional factors when evaluated on the bounce background. |
| **P1A-M5** | p. 12, Route 3 | The RG equation dγ/d ln μ = (N_L−N_R)γ/(12π²) is quoted without derivation or citation, but Ref. [27] gives a **different** β-function that is γ-dependent and non-linear. | Provide the derivation or quote the exact equation from the cited reference, then recompute the ∆γ/γ figure with that equation. |
| **P1A-M6** | p. 20, Sect. XI | Seven “loophole” models are declared but dismissed without any calculation or reference.  Claiming that all seven offer no new content is unsupported. | Either drop the paragraph or supply at least order-of-magnitude estimates showing why each loophole fails. |
| **P1A-M7** | Whole manuscript | The draft still contains internal-process language (“earlier version”, “correction”, “convention note”, “our approach builds on three pillars” etc.).  PRD requires polished final prose. | Remove all version-history and self-review remarks; keep only scientific content. |

--------------------------------------------------------------------
### MINOR (should be addressed)

| ID | Location | Issue | Fix |
|----|----------|-------|-----|
| **P1A-m1** | Abstract & p. 1 footnote a | The footnote mixes three different conventions in one paragraph. | Move detailed differential-form remarks to an appendix; keep only the convention actually used in the main text. |
| **P1A-m2** | p. 11 par. 2 | “≳ 30 orders of magnitude” → the calculation gives 10⁻⁶⁰ / (10⁻²×6×10⁻³)=1.7×10⁻⁵⁶, i.e. 56 orders, not “30”. | Correct the text. |
| **P1A-m3** | p. 23, Table III | The table mixes forward predictions (γ_PT A) and post-fit quantities (w₀wₐ) without indicating which are data-driven. | Add a column “derived / forecast / input”. |
| **P1A-m4** | References | Several arXiv links are missing the leading “arXiv:”.  Example: Ref. [45]. | Standardise all bibliography entries. |
| **P1A-m5** | p. 24, Conclusions | “Positive structural result” is jargon. | Replace by “We conclude that…”. |

--------------------------------------------------------------------
### NIT (cosmetic / typographic)

| ID | Location | Nit |
|----|----------|-----|
| **P1A-n1** | p. 17, Fig. 5 caption | “10120” should be “10¹²⁰”. |
| **P1A-n2** | Multiple | Replace “e-fold” by “e-folds” (plural) when a number is given. |
| **P1A-n3** | p. 8 Eq. (11) | First factor is *abounce/areh*, not its reciprocal (sign already carried by the exponential). |

--------------------------------------------------------------------
## Summary recommendation
**MAJOR REVISIONS**

The manuscript contains interesting ideas, but the principal quantitative
claims (route closures, perturbation transparency, forecast significances) are
either not fully derived or rely on unpublished companion work.  Essential
proofs and reproducibility artefacts are missing, several statistical statements
mix incomparable σ values, and the operator‐dimension issue is unresolved.
Once the Essentials and Majors above are addressed and the paper becomes
self-contained, I will be happy to review a revised version.

---

## PASS 2 — self-critique findings (what initial review missed)

### ADDITIONAL FINDINGS (Round R36conf – second reading)

Below I list *only* issues **not** already contained in items P1A-E1…n3 of my first
report.  Numbering continues the established scheme.

--------------------------------------------------------------------
### ESSENTIAL

| ID | Location | Problem | Required fix |
|----|----------|---------|--------------|
| **P1A-E7** | p. 19, first paragraph of Sec. X D | The parenthetical cross-reference “see Sec. X footnote for the e∧e∧R = −NY + T∧T decomposition” points to a non-existent footnote.  No footnote appears anywhere in Sec. X. | Insert the missing footnote **or** delete the pointer and move the decomposition into the text.  As written the reference is dangling and prevents the reader from verifying the key algebraic identity. |

--------------------------------------------------------------------
### MAJOR

| ID | Location | Problem | Suggested fix |
|----|----------|---------|---------------|
| **P1A-M8** | Throughout Sec. X (esp. p. 18 col. 2 lines 13-18) | The proof outline for the “perturbation-transparency” theorem still switches between tetrad-form and component notation but never shows the explicit scalar-vector-tensor (SVT) mode expansion promised in item E2.  In particular, it does *not* demonstrate that ε^{μνρσ}R_{μνρσ} vanishes **mode-by-mode** once first-order (let alone second-order) metric perturbations are kept. | Either supply an **SVT-level calculation** (e.g. show the k-space expression for the dual curvature and verify it vanishes for every Fourier mode) or give a published reference where that calculation is performed. |
| **P1A-M9** | p. 22, Fig. 6 top panel & text on p. 22 col. 2 | Fig. 6 caption claims the SPHEREx bispectrum will give a 2.6–5 σ test *after* all systematics, whereas the body text immediately below quotes 4.4 σ (“|f_NL|/σ=4.375”).  No explanation is given for the additional degradation from 4.4 σ to 2.6 σ or for the lower end of the range. | State explicitly which systematic terms are included in the plotted 2.6 σ point, give the numerical σ value used, and reconcile the apparent 4.4 σ vs 2.6 σ mismatch. |
| **P1A-M10** | p. 6 Eq. (7) & surrounding paragraph | β(γ) is introduced as a “slowly varying function of γ” but is thereafter *re-identified* with the fixed numerical factor α_em/(4π) in all numerical estimates (Route 2).  The text never supplies β(γ) itself or its error band. | Provide the explicit β(γ) expression (or a reference plus table) and propagate its uncertainty in the Route 2 amplitude estimate.  Otherwise, downgrade the claimed numerical precision. |

--------------------------------------------------------------------
### MINOR

| ID | Location | Issue | Fix |
|----|----------|-------|-----|
| **P1A-m6** | p. 18, Fig. 4 curves labelled “ρ = 0, 0.3, 0.5” | The correlation coefficient ρ is first defined only in the caption of Fig. 4.  The main text never states what two estimators are being correlated. | Add one sentence in §VII (Falsifiability Criteria) explaining that ρ is the assumed cross-correlation between the joint **f_NL** and **β** estimators. |
| **P1A-m7** | Fig. 2 y-axis | The vertical axis “This work ρ” is unit-less in the plot but the text (p. 6 col. 2) describes densities in GeV⁴. | Add units (GeV⁴) or make clear that the axis is expressed in *log₁₀(ρ/GeV⁴)*. |
| **P1A-m8** | p. 7 col. 2 last line | “The *c*ω ω² entry is a phenomenological bookkeeping bound …” mixes an italic *c* with the roman ω. | Use consistent math font for both symbols. |
| **P1A-m9** | p. 17, first full paragraph | The symbol “β(γ)” is overloaded: once for the one-loop coefficient in Eq. (14) and again for the cosmic-birefringence angle. | Add a brief note clarifying the two distinct quantities and use a different symbol (e.g. **β_CS** for the coupling or revert to the standard “b(γ)”). |

--------------------------------------------------------------------
### NIT

| ID | Location | Nit |
|----|----------|-----|
| **P1A-n4** | Throughout | In several places “Hehl–Datta” is misspelled “Hehl–Data”. |
| **P1A-n5** | p. 14, Eq. (17) footnote | “dimensionless angle θ ≡ ϕ/fa” — the slash is missing a thin space before *fa*. |

--------------------------------------------------------------------
### Summary

Only one new **Essential** problem (a broken internal reference) was uncovered,
plus three substantive **Majors** concerning the transparency proof, the
SPHEREx-σ inconsistency, and the undefined β(γ) factor.  A handful of minor
clarifications and typos remain.  Once these are addressed in addition to the
first-round items, the manuscript will be much closer to PRD standards.