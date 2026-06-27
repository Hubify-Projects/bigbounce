# P1A R56 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R56_P1A/paper1a_ech_nogo.pdf` md5=? pages=?
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 NO_NEW
**Wall time**: 213.1s

---

Referee report for Physical Review D (methods/statistics focus)

Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”
Length: 29 pages, 4 main figures, 4 tables, 3 appendices

Scope of my review
- I audited statistical/methods rigor, dimensional analysis, derivation chains, internal arithmetic, and error accounting.
- I recomputed all quoted scalars that are numerically checkable.
- I enforced a standalone-reader standard: the paper must be readable and verifiable without relying on unpublished “companion” works.

Overall assessment
The paper makes a largely theoretical, operator/dimensional-analysis argument that four enumerated “minimal ECH” routes to dark energy are closed, with a principal structural result that the Holst sector is perturbation-transparent for canonical scalar matter. Many statements are properly caveated as ansatz-level. However, the manuscript interweaves non-load-bearing but prominent numerical and forecast claims (MCMC posteriors, ALP fits, PTA spectral indices, SPHEREx forecasts) that rely on in-preparation “companion” papers. There are also figure-label inconsistencies, juxtaposition of σ-levels from different null procedures without a local caveat, and a few quantitative assertions that are not derived or sourced.

Below are findings categorized by severity. I quote the exact page/section and the offending text/formula, and specify the required fix.

ESSENTIAL (must be fixed for PRD acceptance)

P1A-E1 (Comparability of σ’s; combined significance construction)
- Location: Fig. 4 and caption, p. 16; y-axis “Detection Significance (σ)” with curves “CMB E-B”, “Galaxy Spins”, and “Combined (ρ=0, 0.3, 0.5)”.
- Problem: Side-by-side plotting of σ-values from disparate null procedures (LiteBIRD β detection vs SPHEREx fNL detection) with additional “combined significance” curves parameterized by an assumed cross-estimator correlation ρ, without a local and prominent explicit statement that these σ’s are not directly comparable and without a demonstrated joint covariance model. The “combined (ρ=0.3,0.5)” lines are not supported by any derived covariance and are misleading.
- Required fix: (i) Remove the “combined” significance curves entirely unless you provide a derived joint-covariance and an estimator-combination derivation (with data model and shared modes) in the main text or an appendix. (ii) Replace the legend entry “Galaxy Spins” with “Galaxy bispectrum (fNL)” (see P1A-E2). (iii) Add a local caption sentence: “The σ’s in this panel derive from different null procedures (cosmic birefringence β≈0 vs bispectrum fNL≈0) and are not directly comparable; no joint-covariance combination is attempted.” This caveat must appear immediately wherever σ’s from different nulls are juxtaposed.

P1A-E2 (Figure label inconsistency)
- Location: Fig. 4 legend, p. 16 (“Galaxy Spins”).
- Problem: The curve labeled “Galaxy Spins” actually refers to a SPHEREx fNL bispectrum forecast elsewhere in the text. A “galaxy spin” program is separately discussed and found null; plotting “Galaxy Spins” here is incorrect.
- Required fix: Change the legend label to “Galaxy bispectrum (fNL)” and check all places (including Fig. 7 if applicable) for consistent labeling.

P1A-E3 (Standalone-reader failure: reliance on “in preparation” companions for load-bearing numbers)
- Locations:
  - Sec. I, p. 4–5 (“Companion paper— … MCMC verification … NaMaster … spectator-ALP MCMC … in preparation [6] … none of these values is used in the channel-level closure proof…”)
  - Fig. 3, p. 8 (H(z) curves using specific H0, Ωm, ΔNeff values attributed to the companion chains)
  - Table IV, p. 27 (parameter summary with posteriors labeled † from the companion)
  - Sec. X G, p. 21 (PTA γPTA = 2.567 ± 0.382 from “real-KDE GPU MCMC”, Paper III [46])
- Problem: The manuscript displays and relies on numerical results from unpublished, in-preparation companions as if they were available artifacts (H0, σ8, ΔNeff, EB pipeline, ALP MCMC, “real-KDE” PTA analysis). This violates PRD’s standalone and reproducibility standards.
- Required fix: Either (a) excise all numerical values, figures, and claims that depend on these companions (Fig. 3, all “†” rows in Table IV, PTA γPTA lines in the text and Fig. 1 caption), or (b) include full, self-contained derivations, pipeline descriptions, and results in this manuscript with archival links (arXiv DOIs) and frozen chains/artifacts in the Data Availability. Soft pointers to “in preparation” are not acceptable for published claims.

P1A-E4 (R4 “fitted α/M” without a declared estimator)
- Location: Sec. IV D, p. 13–14 (“Setting the present-day rotation-rate amplitude equal to the published … bounds α/M at ∼ 10−21 GeV−1 … the R4-fitted coupling…”)
- Problem: The paper calls α/M “fitted” to βobs, but no estimator, dataset selection, or likelihood is defined here. Without an explicit fit description or a pointer to an archived analysis, calling α/M “fitted” is not reproducible.
- Required fix: Either (i) treat α/M as an illustrative parameter (not “fitted”) and remove all language implying a fit, or (ii) provide the exact estimator and dataset used to infer α/M (with a likelihood formula, priors, and a numerical result derived within this paper or a public companion with DOI). If you retain α/M≈10−21 GeV−1 as a “benchmark,” label it explicitly as such throughout.

P1A-E5 (Unsupported “>100 orders of magnitude” claim for galaxy-spin asymmetry)
- Location: Sec. II C 2, p. 10 (“The parity-odd operator coupling α/M ∼ 10−21 GeV−1 underpredicts any plausible spin asymmetry by > 100 orders of magnitude.”)
- Problem: No quantitative calculation is given for how this operator maps into an observable A0 spin asymmetry amplitude, nor the scaling with α/M. A number of “> 100 OOM” requires a derivation or a bound calculation.
- Required fix: Provide a back-of-the-envelope but explicit computation linking the operator strength to a predicted A0 (with all assumptions stated), or remove the quantitative “> 100 orders” claim. It is acceptable to state “far below detectability” with an actual computed bound.

P1A-E6 (Immirzi running magnitude claim not derived)
- Location: Sec. IV C, p. 13 (“In the Standard Model … numerically, Δγ/γ ∼ 10−2 over the running from the GUT scale to the IR.”)
- Problem: No derivation is provided. A quick estimate from the displayed one-loop ansatz with SM chiral asymmetry suggests an O(0.1–few) multiplicative change over ln(μ)∼O(30–40), not necessarily 10−2. Given Benedetti & Speziale [27] find a more intricate β-function (including sign changes), the 10−2 number needs clear justification or removal.
- Required fix: Either provide a concrete derivation for Δγ/γ ∼ 10−2 under a specific field-content and scale choice, or remove the numeric magnitude and keep the qualitative “mass-dimension lock” argument.

P1A-E7 (σ-comparability caveat missing at every juxtaposition)
- Locations: Fig. 4 caption (p. 16) and main text around Figs. 4 and 7.
- Problem: The abstract correctly notes that β-significances and ACT follow-ups “arise from different null procedures and are not directly comparable,” but this required caveat is not repeated in Fig. 4’s caption (where the reader is most likely to compare σ curves).
- Required fix: Insert a clear comparability caveat directly in the Fig. 4 caption (and anywhere else σ curves from different nulls are plotted together), per the journal’s standards for statistical communication.

P1A-E8 (Dimension of δNY term in Eq. 7)
- Location: Eq. (7), p. 7.
- Problem: The additive term δNY is introduced with no dimensional statement. Since α/M has mass dimension −1, δNY must carry mass dimension −1 as well; this is not stated.
- Required fix: State explicitly that δNY carries mass-dimension −1 and briefly motivate its origin (finite Nieh–Yan piece/scheme dependence), or remove the symbol if not used quantitatively.

P1A-E9 (Data/code availability not frozen)
- Location: Data and Code Availability, p. 26.
- Problem: Only a mutable GitHub branch is cited; a “Zenodo-archived release will pin…” is future tense. For PRD, artifacts must be frozen at acceptance and citable with a DOI. There is also no commit hash or tag to reproduce the exact version used to generate the paper’s figures and numbers.
- Required fix: Provide a persistent DOI (Zenodo or equivalent) for the exact version used, include a Git commit hash/tag, and list the minimal steps to reproduce any figure/numeric result that remains in the paper after addressing P1A-E3. If companions remain “in preparation,” do not cite their artifacts as if available.

P1A-E10 (Use of unpublished PTA result)
- Locations: Fig. 1 caption, p. 5 (“current real-KDE reanalysis γPTA = 2.567 ± 0.382”); Sec. X G, p. 21.
- Problem: A new PTA spectral index result is quoted from a “real-KDE GPU MCMC” companion that is not public. This is not acceptable in a PRD paper focused on different science questions.
- Required fix: Remove the unpublished PTA result or replace it with a published reference value. If you wish to retain a PTA discussion, clearly state that no analysis is performed here and avoid quoting unpublished numbers.

MAJOR (significant but fixable)

P1A-M1 (Overlength and redundancy)
- Location: Entire manuscript (29 pages).
- Problem: The core results (four-route channel closure, perturbation-transparency) could be conveyed more concisely. Large portions repeat caveats and programmatic statements that belong in a project overview, not a PRD methods paper.
- Required fix: Condense to ≤22 pages by (i) removing all non-load-bearing MCMC/PTA/galaxy-spin material (per P1A-E3), (ii) moving long convention footnotes to an appendix, and (iii) focusing the main text on the four-route closures and the transparency proof.

P1A-M2 (Eq. 15 dimensional reduction clarity)
- Location: Eq. (15), p. 12.
- Problem: The path to the dimensionless ratio Δθone-loop/Δθobs includes a non-obvious insertion of MPl to make units match, leading to reader confusion. You then mention “an alternative ordering … ∼10−33 upper bound, not used”; this invites questions about robustness.
- Required fix: Provide a clean, step-by-step dimensional reduction (with units on each factor) to the 10−60 estimate in a short appendix paragraph, and remove the “alternative ordering” aside unless fully derived.

P1A-M3 (Clarify Marea-gap normalization)
- Location: Sec. II A 2, p. 7; footnotes on M = MPl/√γ ≈ 1.9 MPl.
- Problem: The numerical factor “≈1.9 MPl” appears in a footnote later (Sec. IV D), not where M is introduced. This is easy to miss.
- Required fix: When first defining M = Marea-gap, include the numerical mapping M ≈ MPl/√γSU(2) ≈ 1.9 MPl (γSU(2) ≈ 0.274), to anchor later numerical uses.

P1A-M4 (Astrophysical constraints context for α/M)
- Location: Sec. IV D, p. 13–14.
- Problem: The discussion briefly notes “strong tension” with stellar-cooling/helioscope limits for large α/M at ultralight mθ, but this deserves a quantitative one-liner to anchor orders of magnitude.
- Required fix: Add a sentence giving a representative published limit on gaγ at ultralight masses (e.g., HB stars, CAST) and a clear mapping to α/M (including your normalization choice), so readers see the parametric relation at a glance.

P1A-M5 (Clarity on Λeff vs ρΛ and Ξ)
- Location: Sec. II C, Eq. (10), p. 7–8.
- Problem: The relation Λeff = Ξ M2Pl and ρΛ = Λeff M2Pl = Ξ M4Pl is correct but can momentarily confuse readers unfamiliar with the “Λ as curvature” convention.
- Required fix: Add a brief parenthetical “(Λ carries curvature units [mass]2; multiplying by M2Pl gives the energy-density ρΛ)” where Eq. (10) first defines Λeff and ρΛ.

MINOR (address during revision cycle)

P1A-n1 (Typographic consistency)
- Location: Throughout (e.g., “Domaga la–Lewandowski” with a space).
- Problem: Several author names include stray spaces or missing diacritics (Domagała–Lewandowski).
- Required fix: Standardize names and diacritics per journals/citations.

P1A-n2 (Acknowledgment of AI use)
- Location: Acknowledgments, p. 26.
- Problem: “The author acknowledges the use of Claude (Anthropic)…” is unusual but not prohibited. Some journals ask for explicit statements about AI not being credited with authorship; PRD’s policy may require a phrasing change.
- Required fix: Ensure wording complies with APS/PRD guidance on AI-assisted writing (e.g., clarify that AI did not contribute scientific ideas or analysis and that the author is solely responsible).

P1A-n3 (Move long convention footnotes)
- Location: Footnote at Eq. (3), p. 6; long operator-normalization footnote in Sec. IV D, p. 13.
- Problem: These are lengthy and interrupt flow.
- Required fix: Move the long convention clarifications into a short appendix subsection titled “Conventions,” with a forward pointer in the main text.

P1A-n4 (Minor lexical consistency)
- Location: A few instances of British “programme.”
- Required fix: Use US spelling “program” unless quoting specific project names.

Arithmetic and dimensional spot-checks (passed)
- Eq. (9): ρcrit/ρPl = √3/(32π2 γ3) gives 0.41 at γ=0.2375 and 0.27 at γ=0.274 (consistent with the stated 0.27–0.41 range).
- Eq. (7): With g2=4παem≈0.092, γ≈0.274, ln(Λ2/μ2)≈74, and M=MPl/√γ, [(α/M)MPl]≈3×10−3 (reproduced).
- R4 energy density inversion: ρθ=2 m2θ β2/(α/M)2 with mθ=1.5×10−33 eV, β≈6×10−3 rad, α/M=10−21 GeV−1=10−30 eV−1 gives ρθ≈1.6×10−10 eV4≈5.7 ρΛ (consistent with the text’s “∼6 ρΛ”).
- NJL mean-field bound: For n≈102 cm−3, n≈7.66×10−13 eV3, ρNJL≈n2/M2Pl≈4×10−81 eV4≈1.4×10−70 ρΛ (recomputed).

Abstract-last drift sweep
- The abstract’s main claims (four-route channel closure under stated ansatz; perturbation-transparency for canonical scalar matter; two surviving class-level tests; “not directly comparable” caveat for β significances) match the body. However, the abstract references “SPHEREx forecast 2.6–5σ” and “ΛCDM+ΔNeff MCMC verification” that depend on unpublished companions. If P1A-E3 is implemented (removing these dependencies or fully documenting them here), the abstract should be edited to avoid relying on non-archived results.

Provenance surfaces
- Data/code availability must include a frozen DOI and explicit version/commit. “Will pin” is insufficient (P1A-E9).
- Remove all references to unpublished chain sizes (“309,189 frozen accepted samples…”) unless the artifacts are provided here with DOI.

Uncomputed quantitative claims (require numbers or explicit assumption tags)
- “>100 orders” for galaxy spins (P1A-E5).
- “Γwash > H at Treh is the expectation” is fine as a conditional statement; if used to support a closure, add at least a simple order-of-magnitude rate vs H0 comparison for the dominant channel (top-Yukawa) with a citation.

Effect sizes
- Where σ’s are quoted (LiteBIRD σ(β)≈0.03°, SPHEREx σ(fNL)≈0.7–1.0), the paper sometimes provides useful effect-size context (e.g., a 0.27° vs 0.342° difference is only ~0.7σ once Planck error is included). Keep this pattern and add the comparability caveat locally at the figures (P1A-E1/E7).

Recommended maximum page count
- 22 pages after removing non-essential material and consolidating convention footnotes.

## Summary recommendation
MAJOR REVISIONS

The central theoretical result (perturbation-transparency of the Holst sector for canonical scalars) and the channel-level closure logic are potentially publishable in PRD after significant restructuring. However, the manuscript currently blends non-reproducible, unpublished numerical results (MCMC posteriors, PTA reanalysis, ALP fits) and presents a figure with misleading combined σ-curves. It also contains several unsupported quantitative assertions and lacks a frozen artifact DOI. If the authors refocus the paper on the analytic closures, remove or fully document all data-dependent claims, correct figure labeling and σ-comparability issues, and provide a frozen reproducibility bundle, the work could meet PRD standards.