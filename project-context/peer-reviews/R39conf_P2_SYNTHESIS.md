# P2 R39conf — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations

## ⛔ ROUND DEGRADED — reviewer leg(s) FAILED: Claude_brutal
Failed legs are API errors, NOT zero-finding clean reviews. This round
MUST NOT count toward any clean-round counter; re-run after the failure
(e.g. API credit top-up) is resolved.
**Total findings (across all reviewers)**: 24
**Distinct consensus groups**: 3

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 0 | 0 | 0 | 0 |
| Grok_brutal | 0 | 0 | 0 | 0 |
| OpenAI_methodology | 5 | 9 | 9 | 1 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `table_ii` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P2-E2/ESSENTIAL]**: P2-E2 (Sec. VI; Table II p. 14; Table III p. 17): Inconsistent Bayes factors for the narrow competitor prior - Offending claims:   - Table III “BF vs. Tuned” (narrow competitor [−5,+5], delta bounce prior) lists: 7.0 (no GR), 6.1 (σGR = 0.5), 4.7 (σGR = 1.0).   - Table II footnote a repeats “4.7–7.0” across GR scenarios for the same configuration. - Problem: For a point prediction at the observed mean (“ˆfNL = −35/8,” your assumption for Table III), the closed-form Bayes factor for a delta bounce prior vs a uniform competitor of width W is B = W/(√(2π) σeff), with σeff = √(0.7^2 + σGR^2) for y…

### `table_iv` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P2-E5/ESSENTIAL]**: P2-E5 (Sec. IV; Table IV caption; also Abstract cross-refs): Mis-citation of Eq. (7) as a “quadrature convention” - Offending text examples:   - Abstract: “…these systematics are combined additively in quadrature … cf. Sec. VII and Eq. (7) …”   - Table IV caption: “…using Eq. 7’s quadrature convention.” - Problem: Eq. (7) in the manuscript defines a heuristic δC/C scaling for the covariance shift; it does not encode nor motivate an “add in quadrature” combination rule for heterogeneous systematics. Referring to Eq. (7) as a “quadrature convention” is a cross-reference error and risks misleadin…

## Other findings (22)

- **[OpenAI_methodology/P2-E1/ESSENTIAL]**: P2-E1 (Sec. III.B, p. 8): Incorrect definition of the “squeezed-limit” ratio - Offending text: “squeezed cutoffs (x3,min from 0.001 to 0.2, where x3 ≡ k3/k1 is the squeezed-limit ratio with x3 → 0 corresponding to the squeezed limit k3 ≪ k1 ≈ k2).” - Problem: With the stated ordering k1 ≤ k2 ≤ k3, the squeezed limit is k1 ≪ k3 and therefore k1/k3 → 0, not k3/k1 → 0. As written, x3 ≡ k3/k1 ≥ 1 by c…
- **[OpenAI_methodology/P2-E3/ESSENTIAL]**: P2-E3 (Data and Code Availability, pp. 23–24): Missing permanent archival and frozen release details - Offending text: “archived at Zenodo (DOI inserted at submission).” - Problem: The submission provides only a GitHub URL and a placeholder for the DOI. PRD requires reproducibility at acceptance; a frozen, citable archival release with a DOI and an exact version (commit hash/tag) is needed. Severa…
- **[OpenAI_methodology/P2-E4/ESSENTIAL]**: P2-E4 (Abstract and Sec. IV, pp. 1 and 10): “Realistic 2.6–5σ” headline depends on an ad hoc quadrature systematics budget not tied to a survey-specific covariance - Offending text (abstract): “reducing to a realistic ∼ 2.6–5σ after the systematic budget (mismatch, ϵ-correction, polynomial-null-space scatter ±0.13 … photometric-z degradation, PNG-bias bϕ marginalization, and relativistic projectio…
- **[OpenAI_methodology/P2-M1/MAJOR]**: P2-M1 (Sec. VII.C p. 16–17; throughout): GR-projection “σGR ∈ [0,1]” stress test not survey-calibrated - Problem: σGR is introduced as a free nuisance amplitude, motivated by Addis et al. (Euclid/MegaMapper), but it is then used to headline-degrade SPHEREx constraints. No SPHEREx-specific estimate is given and the values are carried into the main “realistic range.” - Required fix: Either tie σGR t…
- **[OpenAI_methodology/P2-M2/MAJOR]**: P2-M2 (Sec. IV p. 10–11): Shot-noise degradation inconsistency and unsupported “15–30%” claim - Offending text: A “simple Poisson estimate” gives √(1+1/nP0) ≈ 3.3× degradation for n ≈ 10−5 h^3 Mpc−3 and P0 ≈ 10^4 h−3 Mpc^3, yet the bispectrum estimator “effective degradation … is moderate, 15–30%.” - Problem: The 3.3× estimate and the 15–30% statement are numerically incompatible without a calcula…
- **[OpenAI_methodology/P2-M3/MAJOR]**: P2-M3 (Sec. VI, pp. 12–15; Tables II–III): Bayes-factor framework needs a compact derivation and a single, explicit formula for all entries - Problem: The text invokes Eq. (8) and quotes scipy.stats.norm results, but does not show the explicit closed-form expressions for the delta-vs-uniform and Gaussian-vs-uniform priors nor the effect of σtheory (Gaussian bounce prior). Given the inconsistencies…
- **[OpenAI_methodology/P2-M4/MAJOR]**: P2-M4 (Sec. VII.B p. 15–16; Fig. 5): Dependence on bϕ priors without sufficient methodological detail - Problem: The degradation of σ(fNL) with widened bϕ priors is asserted and shown schematically, but details of the Fisher setup (tracer bins, redshift distributions, bias model, k-range, covariance) are insufficient for reproducibility in the text. - Required fix: Provide, at minimum, a table of …
- **[OpenAI_methodology/P2-M5/MAJOR]**: P2-M5 (Sec. VII.D pp. 18): Additional systematics summarized without quantitative support - Problem: Integral constraint, lensing magnification, and mask-induced couplings are cited as “10–30%” order-of-magnitude degradations without calculations or references applicable to the SPHEREx bispectrum analysis used here. - Required fix: Either provide minimal quantitative estimates tied to your bispect…
- **[OpenAI_methodology/P2-M6/MAJOR]**: P2-M6 (Sec. II.A p. 5; Fig. 1): Notation clarity around “k” in the squeezed-limit statement - Offending text: “as k1/k → 0” with “k” not defined in that sentence; the figure uses BNL(k1, k, k). - Required fix: Define k explicitly in-text the first time (e.g., “evaluate along the line (k1, k2, k3) = (k1, k, k) and take k1/k → 0”), and ensure consistent usage in the caption.
- **[OpenAI_methodology/P2-M7/MAJOR]**: P2-M7 (Sec. II–III; throughout): Heterogeneous r values and estimator weightings - Problem: r is reported under multiple weightings (CMB-Fisher, SPHEREx-like, SDB), and an injection–recovery study is presented using a 2D CMB KSW estimator on flat-sky patches with isotropic Gaussian noise. While caveats are stated, this can still confuse readers about which r is operative in which forecast. - Requi…
- **[OpenAI_methodology/P2-n1/MINOR]**: P2-n1 (Fig. 4 p. 15; Fig. 5 p. 16; Fig. 2 p. 10): Axis labels and units - Problem: The captions do not state the axis units (e.g., kmin axis in h Mpc−1?). PRD expects unambiguous axes. - Required fix: Add axis units and ranges (e.g., kmin in h Mpc−1) to all figures and ensure y-axis labels indicate whether values are 1σ errors or significance.
- **[OpenAI_methodology/P2-n2/MINOR]**: P2-n2 (Sec. IV p. 10): Mix of “naive” 6.25σ and “template-corrected” 5.2–5.5σ - Problem: You do state the naive value is “shown only for reference,” but consider adding “not directly comparable to template-corrected values” to meet PRD’s clarity standards when different null procedures are juxtaposed. - Required fix: Add an explicit “not directly comparable” tag at each such juxtaposition.
- **[OpenAI_methodology/P2-n3/MINOR]**: P2-n3 (Sec. VIII.A p. 18): Planck PR4 recast “0.02σ from zero” - Check: With r = 0.876, σ ≈ 5.71; −0.1/5.71 ≈ −0.0175σ, consistent with ~0.02σ. Consider showing the simple arithmetic in a footnote for clarity. - Required fix: Optional, but a one-line computation would help readers.
- **[OpenAI_methodology/P2-n4/MINOR]**: P2-n4 (Sec. V p. 11): MegaMapper “3–7σ” envelope wording - Problem: You do say “illustrative … reflects design uncertainty,” but tightening the language in the abstract to prevent misreading as a forecast would help. - Required fix: Add “illustrative only” in the abstract near the MegaMapper envelope.
- **[OpenAI_methodology/P2-n5/MINOR]**: P2-n5 (Sec. II.C p. 6–7): “Mechanism-independent” vs “UV-completion-independent” - Problem: The distinction is carefully made. Consider moving one of the repeated clarifications to a footnote to tighten the main flow.
- **[OpenAI_methodology/P2-M8/MAJOR]**: P2-M8 (Sec. II–III; Sec. II A injection–recovery paragraph, p. 5): 2D KSW injection–recovery uses a 3D photometric-z power spectrum as a “diagonal noise covariance” - Offending text: “adds isotropic Gaussian noise with the published SPHEREx photometric-z power spectra as the diagonal noise covariance, and applies a KSW-type optimal linear estimator on tiled flat-sky patches…” - Problem: The KSW es…
- **[OpenAI_methodology/P2-M9/MAJOR]**: P2-M9 (Sec. VI; Tables II–III vs Abstract): Bayes-factor bookkeeping across r→1 vs r≈0.84 cases is not labeled consistently in tables - Observation: The abstract headlines BF ≈ 9–14 after “noise-weighted r ≈ 0.84 bookkeeping,” while Tables II–III report r→1 endpoint values (e.g., “∼ 10–17” in the prose and table). The body text does explain both conventions, but the tables themselves do not carry …
- **[OpenAI_methodology/P2-m8/MINOR]**: P2-m8 (Sec. VI, “template-mismatch bookkeeping” paragraph): “Broad-competitor cells are unchanged” under alternate bookkeeping is not literally true - Offending text: “The alternative fully measured-space bookkeeping … gives a similar modest reduction (7.0 → 5.9 at the delta/narrow corner; the broad-competitor cells are unchanged).” - Problem: Even for a broad uniform prior, evaluating at rfNL rat…
- **[OpenAI_methodology/P2-m9/MINOR]**: P2-m9 (Sec. III.B, literature note): Unsupported novelty claim on template-overlap quantification - Offending text: “a literature search confirming no prior quantification of this overlap exists (2009–2024).” - Problem: This is a novelty claim without a supporting citation trail (search terms, scope) or a clear boundary (e.g., for “matter bounce template vs local” in LSS/CMB contexts). - Required …
- **[OpenAI_methodology/P2-m10/MINOR]**: P2-m10 (Typography/notation; multiple locations): Ambiguous “105” vs “10^5” - Offending text: “three independent 105-realization Monte Carlo ensembles” (and variants). - Problem: The superscript is easy to miss; “105” can be read as one-hundred-and-five. Use “10^5” or “100,000” consistently. - Required fix: Standardize to “10^5” (or 100,000) throughout.
- **[OpenAI_methodology/P2-m11/MINOR]**: P2-m11 (Sec. A.1, Eq. (A7) narrative): Symmetry-factor placement unclear - Offending text/equation: “Bζ = −2 Im Σv Σσ (1/Sv) Iv(…); Sv is the symmetry factor…” - Problem: It’s not stated earlier whether the Wick counting already includes or excludes identical-field permutations per vertex. Readers could misinterpret whether the 1/Sv is double-counting or compensating. This is a documentation clari…
- **[OpenAI_methodology/P2-N3/NIT]**: P2-N3 (Sec. II A; Appendix A mode functions): Phase/sign convention for the matter-contraction mode functions - Offending text: ζk ∝ (1 − ikη) e^{ikη}/(kη)^3 appears in a few places. - Problem: Many references write e^{−ikη} for the BD choice (sign conventions vary). Since only relative phases enter Im parts, this likely does not affect any result, but a parenthetical note on convention (or a cita…
