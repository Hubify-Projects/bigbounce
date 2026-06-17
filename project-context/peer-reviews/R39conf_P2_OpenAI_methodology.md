# P2 R39conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper2_fnl_forecast.pdf` md5=406af9f8 pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6967 chars)
**Wall time**: 338.5s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
- Focus: methodology rigor, derivation chains, dimensional/arithmetical consistency, error propagation, estimator declarations, reproducibility.
- I read the full 27-page manuscript, including figures, tables, equations, appendices, and the abstract. I recomputed all explicitly quoted numbers that can be reconstructed from the text.

Overall assessment
- The paper presents a recast of published SPHEREx/MegaMapper sensitivities to a specific matter-bounce prediction, with extensive discussion of template mismatch, null-space ambiguities in the bispectrum polynomial, and a Bayesian model-comparison framing.
- There are some strong aspects (clear statement that this is a sensitivity recast rather than a de novo Fisher forecast; explicit operator-identity for the in-in doubling; transparent acknowledgment of systematic fragilities).
- However, I identify several essential methodological and arithmetic issues that must be resolved before publication in PRD. In particular: a definitional error in the “squeezed” ratio, internal inconsistencies in reported Bayes factors (off by 20–40% compared to the stated closed-form), and missing reproducibility artifacts (placeholder DOI) all require correction. In addition, some conclusions depend on an ad hoc quadrature “systematics budget” without sufficient survey-specific justification, and certain numerical claims (e.g., shot-noise degradation “15–30%” after noting a 3.3× Poisson limit) are unsupported by documented calculations.

Findings

ESSENTIAL

P2-E1 (Sec. III.B, p. 8): Incorrect definition of the “squeezed-limit” ratio
- Offending text: “squeezed cutoffs (x3,min from 0.001 to 0.2, where x3 ≡ k3/k1 is the squeezed-limit ratio with x3 → 0 corresponding to the squeezed limit k3 ≪ k1 ≈ k2).”
- Problem: With the stated ordering k1 ≤ k2 ≤ k3, the squeezed limit is k1 ≪ k3 and therefore k1/k3 → 0, not k3/k1 → 0. As written, x3 ≡ k3/k1 ≥ 1 by construction and cannot approach 0. This is a definitional error that affects the description of the cutoff study.
- Required fix: Correct the definition and discussion. Either define xsq ≡ k1/k3 with xsq → 0 in the squeezed limit (consistent with your ordering), or explicitly remove the k1 ≤ k2 ≤ k3 ordering when defining x3 = k3/k1 and adjust subsequent statements. Verify that all occurrences and the code/figures use a consistent definition.

P2-E2 (Sec. VI; Table II p. 14; Table III p. 17): Inconsistent Bayes factors for the narrow competitor prior
- Offending claims:
  - Table III “BF vs. Tuned” (narrow competitor [−5,+5], delta bounce prior) lists: 7.0 (no GR), 6.1 (σGR = 0.5), 4.7 (σGR = 1.0).
  - Table II footnote a repeats “4.7–7.0” across GR scenarios for the same configuration.
- Problem: For a point prediction at the observed mean (“ˆfNL = −35/8,” your assumption for Table III), the closed-form Bayes factor for a delta bounce prior vs a uniform competitor of width W is B = W/(√(2π) σeff), with σeff = √(0.7^2 + σGR^2) for your setup. Using your own inputs and W = 10 for [−5,+5], the correct values are:
  - No GR (σeff = 0.700): B = 10/(2.506×0.700) = 5.70 (not 7.0)
  - σGR = 0.5 (σeff = 0.860): B = 10/(2.506×0.860) = 4.65 (not 6.1)
  - σGR = 1.0 (σeff = 1.2207): B = 10/(2.506×1.2207) = 3.27 (not 4.7)
  - The reported 7.0 appears consistent with W ≈ 12 (or σeff ≈ 0.57), which contradicts the stated prior width and σeff.
- Required fix: Recompute all Bayes-factor entries in Table II and Table III from a single, stated closed-form expression using the declared priors and σeff, and update the text to match. If a different prior width or a different σeff was actually used, state it explicitly and correct all references. Provide a compact derivation of Eq. (8) and the special cases used for the table entries, or add a short appendix outlining the algebra. Ensure the “template-mismatch rebooking” is applied consistently where claimed.

P2-E3 (Data and Code Availability, pp. 23–24): Missing permanent archival and frozen release details
- Offending text: “archived at Zenodo (DOI inserted at submission).”
- Problem: The submission provides only a GitHub URL and a placeholder for the DOI. PRD requires reproducibility at acceptance; a frozen, citable archival release with a DOI and an exact version (commit hash/tag) is needed. Several “named artifacts” are referenced throughout (JSON outputs, scripts) but cannot be verified without a fixed release.
- Required fix: Provide a permanent DOI for an archived repository snapshot that exactly matches the paper version, include a top-level manifest of all artifacts referenced in the text (filenames, sizes, checksums), and name the commit hash or tag used to generate the results. If any results rely on external data products (e.g., CAMB Cℓ, SPHEREx public products), specify versions and access URLs.

P2-E4 (Abstract and Sec. IV, pp. 1 and 10): “Realistic 2.6–5σ” headline depends on an ad hoc quadrature systematics budget not tied to a survey-specific covariance
- Offending text (abstract): “reducing to a realistic ∼ 2.6–5σ after the systematic budget (mismatch, ϵ-correction, polynomial-null-space scatter ±0.13 … photometric-z degradation, PNG-bias bϕ marginalization, and relativistic projection); these systematics are combined additively in quadrature …”
- Problem: The quoted “realistic range” is driven by adding heterogeneous systematics in quadrature under assumed amplitudes (σGR up to 1.0; per-bin bϕ prior widening to 0.9–1.0, etc.), with no joint covariance modeling or SPHEREx-specific validation of σGR. This combination rule is acknowledged as a “transparent scoping choice,” but the same numbers are used as a headline in the abstract and figures.
- Required fix: Either (a) move the 2.6–5σ range out of the headline and clearly label it as a scoping illustration pending a proper joint Fisher or covariance analysis, or (b) provide a compact survey-specific calculation (or literature-backed calibration) justifying the adopted σGR and bϕ priors for SPHEREx and recompute a joint-marginalized constraint. At minimum, in the abstract explicitly state “illustrative scoping estimate via quadrature addition; not a joint Fisher forecast.”

MAJOR

P2-M1 (Sec. VII.C p. 16–17; throughout): GR-projection “σGR ∈ [0,1]” stress test not survey-calibrated
- Problem: σGR is introduced as a free nuisance amplitude, motivated by Addis et al. (Euclid/MegaMapper), but it is then used to headline-degrade SPHEREx constraints. No SPHEREx-specific estimate is given and the values are carried into the main “realistic range.”
- Required fix: Either tie σGR to a SPHEREx-like modeling study or move the σGR-driven figures out of the headline and mark them as exploratory stress tests. Provide at least one reference or calculation that maps SPHEREx’s redshift range and depth to a plausible σGR range.

P2-M2 (Sec. IV p. 10–11): Shot-noise degradation inconsistency and unsupported “15–30%” claim
- Offending text: A “simple Poisson estimate” gives √(1+1/nP0) ≈ 3.3× degradation for n ≈ 10−5 h^3 Mpc−3 and P0 ≈ 10^4 h−3 Mpc^3, yet the bispectrum estimator “effective degradation … is moderate, 15–30%.”
- Problem: The 3.3× estimate and the 15–30% statement are numerically incompatible without a calculation bridging from power-spectrum shot noise to the actual bispectrum estimator weighting and triangle selection. No such calculation is shown or referenced.
- Required fix: Provide a documented bispectrum Fisher calculation (or a demonstrative toy model) quantitatively showing why the degradation reduces from 3.3× to 15–30% in the squeezed-dominated regime, and give the exact assumptions. Otherwise, remove the 15–30% claim.

P2-M3 (Sec. VI, pp. 12–15; Tables II–III): Bayes-factor framework needs a compact derivation and a single, explicit formula for all entries
- Problem: The text invokes Eq. (8) and quotes scipy.stats.norm results, but does not show the explicit closed-form expressions for the delta-vs-uniform and Gaussian-vs-uniform priors nor the effect of σtheory (Gaussian bounce prior). Given the inconsistencies flagged above, a concise derivation is necessary to avoid ambiguity.
- Required fix: Add a short appendix deriving the evidences and Bayes-factor expressions used to populate Tables II–III, including the σeff rebooking. Then audit and update every table entry accordingly.

P2-M4 (Sec. VII.B p. 15–16; Fig. 5): Dependence on bϕ priors without sufficient methodological detail
- Problem: The degradation of σ(fNL) with widened bϕ priors is asserted and shown schematically, but details of the Fisher setup (tracer bins, redshift distributions, bias model, k-range, covariance) are insufficient for reproducibility in the text.
- Required fix: Provide, at minimum, a table of the assumed binning, biases, redshift windows, and k-cuts, and an explicit expression for how bϕ enters the bispectrum Fisher (cross-terms) in the adopted model. Clarify whether Heinrich et al.’s universality prior is replaced per bin or globally in your variants.

P2-M5 (Sec. VII.D pp. 18): Additional systematics summarized without quantitative support
- Problem: Integral constraint, lensing magnification, and mask-induced couplings are cited as “10–30%” order-of-magnitude degradations without calculations or references applicable to the SPHEREx bispectrum analysis used here.
- Required fix: Either provide minimal quantitative estimates tied to your bispectrum estimator and SPHEREx-like survey geometry, or clearly state that these are qualitative caveats not included in the final numbers.

P2-M6 (Sec. II.A p. 5; Fig. 1): Notation clarity around “k” in the squeezed-limit statement
- Offending text: “as k1/k → 0” with “k” not defined in that sentence; the figure uses BNL(k1, k, k).
- Required fix: Define k explicitly in-text the first time (e.g., “evaluate along the line (k1, k2, k3) = (k1, k, k) and take k1/k → 0”), and ensure consistent usage in the caption.

P2-M7 (Sec. II–III; throughout): Heterogeneous r values and estimator weightings
- Problem: r is reported under multiple weightings (CMB-Fisher, SPHEREx-like, SDB), and an injection–recovery study is presented using a 2D CMB KSW estimator on flat-sky patches with isotropic Gaussian noise. While caveats are stated, this can still confuse readers about which r is operative in which forecast.
- Required fix: Centralize the operative r used in each quantitative forecast in a small summary table (weighting, value, uncertainty) and move the KSW injection–recovery demonstration to an appendix or clearly label it as a CMB-style cross-check not directly applicable to the 3D galaxy bispectrum.

MINOR

P2-n1 (Fig. 4 p. 15; Fig. 5 p. 16; Fig. 2 p. 10): Axis labels and units
- Problem: The captions do not state the axis units (e.g., kmin axis in h Mpc−1?). PRD expects unambiguous axes.
- Required fix: Add axis units and ranges (e.g., kmin in h Mpc−1) to all figures and ensure y-axis labels indicate whether values are 1σ errors or significance.

P2-n2 (Sec. IV p. 10): Mix of “naive” 6.25σ and “template-corrected” 5.2–5.5σ
- Problem: You do state the naive value is “shown only for reference,” but consider adding “not directly comparable to template-corrected values” to meet PRD’s clarity standards when different null procedures are juxtaposed.
- Required fix: Add an explicit “not directly comparable” tag at each such juxtaposition.

P2-n3 (Sec. VIII.A p. 18): Planck PR4 recast “0.02σ from zero”
- Check: With r = 0.876, σ ≈ 5.71; −0.1/5.71 ≈ −0.0175σ, consistent with ~0.02σ. Consider showing the simple arithmetic in a footnote for clarity.
- Required fix: Optional, but a one-line computation would help readers.

P2-n4 (Sec. V p. 11): MegaMapper “3–7σ” envelope wording
- Problem: You do say “illustrative … reflects design uncertainty,” but tightening the language in the abstract to prevent misreading as a forecast would help.
- Required fix: Add “illustrative only” in the abstract near the MegaMapper envelope.

P2-n5 (Sec. II.C p. 6–7): “Mechanism-independent” vs “UV-completion-independent”
- Problem: The distinction is carefully made. Consider moving one of the repeated clarifications to a footnote to tighten the main flow.

NIT

P2-z1 (Throughout): Minor typos and hyphenation artifacts likely from PDF-to-text parsing (e.g., “per￾cent,” “bispec￾trum”).
- Required fix: Standard copyedit pass on the final PDF.

P2-z2 (Sec. A.2 p. 26–27): Table V caption slightly verbose
- Required fix: Condense to the essential point: rows differ only by central |fNL|; all else equal.

Arithmetic/consistency spot-checks (passed)
- |f_bounce|/|f_inf| ≈ 4.375/0.015 ≈ 291.7 → “≈ 290” OK.
- Naive SPHEREx significance 4.375/0.7 = 6.25 OK.
- Template-corrected significance with r = 0.829–0.876 → 5.18–5.47σ → “5.2–5.5σ” OK.
- GR quadrature σeff = √(0.7^2 + 1.0^2) = 1.221 → 4.375×0.84/1.221 ≈ 3.01σ → “≈ 3.0σ” OK.
- Combined bϕ (0.9) + GR(1.0): σeff = √(0.9^2 + 1.0^2) = 1.345 → 2.73σ, and with (1.0, 1.0): 1.414 → 2.60σ → matches text.
- Planck PR4 recast: σ ≈ 5.71; distance to −4.375 is 4.26/5.71 = 0.75σ OK.
- τNL estimate: (36/25) f^2 ≈ 27.6 OK.
- Broad-prior Bayes factors: with W = 30 and σeff = 0.7, B ≈ 17.1; with σeff = √(0.7^2 + 1^2) ≈ 1.221 yields B ≈ 9.82; with σeff = 0.833 (r-rebooked), B ≈ 14.4/9.2; all these match the corresponding “broad” entries.

Length and focus
- The manuscript runs 27 pages for what is primarily a sensitivity recast. I recommend reducing main-text length to ≈ 18–20 pages by moving the operator-identity derivation details and some survey-operations digressions (e.g., anomaly-tracer aside, KSW flat-sky test) to appendices. The main thread (template mismatch, forecast recast, and Bayes factors) should remain front-and-center.

## Summary recommendation
MAJOR REVISIONS

The paper contains two essential corrections (squeezed-limit ratio definition; inconsistent Bayes-factor numbers for the narrow competitor) and a critical reproducibility gap (missing DOI/frozen release). In addition, several key headlines rely on an ad hoc quadrature systematics model without SPHEREx-calibrated inputs, and some numerical claims are currently unsupported by calculations. Once the definitional and arithmetic inconsistencies are corrected, the code/data are archived with a DOI, and the scoping nature of the “realistic 2.6–5σ” range is clearly labeled (or replaced by a joint Fisher/covariance treatment), the submission could be reconsidered. The technical core is promising, but PRD’s methodological standards require these issues to be addressed.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second-pass audit)

Note: These are new issues not listed in my initial review. Items are labeled by severity: Essential (E), Major (M), Minor (m), Nit (N).

ESSENTIAL

P2-E5 (Sec. IV; Table IV caption; also Abstract cross-refs): Mis-citation of Eq. (7) as a “quadrature convention”
- Offending text examples:
  - Abstract: “…these systematics are combined additively in quadrature … cf. Sec. VII and Eq. (7) …”
  - Table IV caption: “…using Eq. 7’s quadrature convention.”
- Problem: Eq. (7) in the manuscript defines a heuristic δC/C scaling for the covariance shift; it does not encode nor motivate an “add in quadrature” combination rule for heterogeneous systematics. Referring to Eq. (7) as a “quadrature convention” is a cross-reference error and risks misleading readers about the basis for the quadrature budget used throughout.
- Required fix: Correct the references. State explicitly that quadrature addition is an external scoping assumption, not derived from Eq. (7). Remove “Eq. 7’s quadrature convention” language from Table IV and anywhere else it appears, and either (a) justify quadrature with a survey-specific covariance argument, or (b) mark it clearly as a purely illustrative assumption (no equation reference).

MAJOR

P2-M8 (Sec. II–III; Sec. II A injection–recovery paragraph, p. 5): 2D KSW injection–recovery uses a 3D photometric-z power spectrum as a “diagonal noise covariance”
- Offending text: “adds isotropic Gaussian noise with the published SPHEREx photometric-z power spectra as the diagonal noise covariance, and applies a KSW-type optimal linear estimator on tiled flat-sky patches…”
- Problem: The KSW estimator used here is a 2D CMB-style bispectrum estimator on flat-sky patches. Feeding a 3D galaxy P(k) (with units and k-space weighting appropriate to a 3D field) as a “diagonal noise covariance” for a 2D map is dimensionally and procedurally inconsistent, even if the result is only used as a “Fisher-space test.” This can bias the recovered amplitude overlap rmeasured and the implied weighting. The text flags caveats but does not show how the 3D-to-2D mapping was effected or normalized.
- Required fix: Either remove the 2D KSW injection–recovery result as a validation artifact not germane to a 3D galaxy bispectrum forecast, or supply a compact derivation/mapping (and units) that shows how the 3D P(k) was converted into an effective 2D noise power for the flat-sky KSW estimator, including the angular-kernel and redshift selection used. Explicitly state that this 2D cross-check is not used quantitatively in any SPHEREx forecast number (if so).

P2-M9 (Sec. VI; Tables II–III vs Abstract): Bayes-factor bookkeeping across r→1 vs r≈0.84 cases is not labeled consistently in tables
- Observation: The abstract headlines BF ≈ 9–14 after “noise-weighted r ≈ 0.84 bookkeeping,” while Tables II–III report r→1 endpoint values (e.g., “∼ 10–17” in the prose and table). The body text does explain both conventions, but the tables themselves do not carry a clear “r→1 endpoint” label in their headers, inviting confusion when compared to abstract values.
- Required fix: Add an explicit line or footnote at the top of Tables II–III stating that the listed Bayes factors are the r→1 bookkeeping endpoint (σeff = 0.7), and give in-table parenthetical values for the r ≈ 0.84 bookkeeping (e.g., “(rebooked: …)”) for the same entries that the abstract headlines draw from. This avoids cross-referencing ambiguity.

MINOR

P2-m8 (Sec. VI, “template-mismatch bookkeeping” paragraph): “Broad-competitor cells are unchanged” under alternate bookkeeping is not literally true
- Offending text: “The alternative fully measured-space bookkeeping … gives a similar modest reduction (7.0 → 5.9 at the delta/narrow corner; the broad-competitor cells are unchanged).”
- Problem: Even for a broad uniform prior, evaluating at rfNL rather than fNL shifts the denominator integral slightly (through the truncated normal mass over [fmin, fmax]); “unchanged” is only approximately correct. Given the paper’s emphasis on exact closed-form Bayes factors, this claim should be qualified or quantified.
- Required fix: Replace “unchanged” with a quantified statement, e.g., “changes by <1% for [−15,+15] at σ=0.7; numerically negligible at the reported precision,” and show the quick computation (or add to the released recompute script).

P2-m9 (Sec. III.B, literature note): Unsupported novelty claim on template-overlap quantification
- Offending text: “a literature search confirming no prior quantification of this overlap exists (2009–2024).”
- Problem: This is a novelty claim without a supporting citation trail (search terms, scope) or a clear boundary (e.g., for “matter bounce template vs local” in LSS/CMB contexts).
- Required fix: Either soften to “we are not aware of a prior quantification…” or provide at least one or two representative searches/citations that delineate the claim’s scope. Not critical to results, but PRD typically asks that novelty statements be conservatively phrased.

P2-m10 (Typography/notation; multiple locations): Ambiguous “105” vs “10^5”
- Offending text: “three independent 105-realization Monte Carlo ensembles” (and variants).
- Problem: The superscript is easy to miss; “105” can be read as one-hundred-and-five. Use “10^5” or “100,000” consistently.
- Required fix: Standardize to “10^5” (or 100,000) throughout.

P2-m11 (Sec. A.1, Eq. (A7) narrative): Symmetry-factor placement unclear
- Offending text/equation: “Bζ = −2 Im Σv Σσ (1/Sv) Iv(…); Sv is the symmetry factor…”
- Problem: It’s not stated earlier whether the Wick counting already includes or excludes identical-field permutations per vertex. Readers could misinterpret whether the 1/Sv is double-counting or compensating. This is a documentation clarity point, not a physics error.
- Required fix: Add one sentence clarifying whether Iv has already summed over identical legs inside each operator and whether the 1/Sv is needed to avoid double counting, consistent with your Wick-permutation convention.

NIT

P2-N3 (Sec. II A; Appendix A mode functions): Phase/sign convention for the matter-contraction mode functions
- Offending text: ζk ∝ (1 − ikη) e^{ikη}/(kη)^3 appears in a few places.
- Problem: Many references write e^{−ikη} for the BD choice (sign conventions vary). Since only relative phases enter Im parts, this likely does not affect any result, but a parenthetical note on convention (or a citation) will head off reader questions.
- Required fix: Add a brief note citing the convention used (e.g., Cai et al. App. B) and that the overall phase choice does not affect the final bispectrum after taking −2 Im.

Explanation of scope
- I focused on arithmetic rechecks, caption–body consistency, unit/normalization checks, cross-references, null-procedure comparability, and abstract fidelity. I did not repeat any issues from my first report; the items above are newly identified on a second pass.