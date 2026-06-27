# P2 R54 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R54_P2/02_full_draft.pdf` md5=e87fdb7c pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5890 chars)
**Wall time**: 258.9s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope and role
I reviewed the full 28‑page manuscript (text, equations, tables, figures, captions, appendix, references, and Data & Code Availability) for methodological rigor: estimator definitions, derivation chains, dimensional checks, arithmetic, uncertainty propagation, and internal consistency across the abstract, body, figures, and tables. Below I list all issues found, each tagged ESSENTIAL, MAJOR, MINOR, or NIT, with page references and required remedies.

Global assessment of contribution
The paper is a sensitivity recast (not an independent Fisher forecast) of SPHEREx and MegaMapper for testing the matter‑bounce prediction flocalNL = −35/8. The core technical components are:
- a normalization audit of the Cai et al. vs. Li et al. bispectrum derivations (Appendix A),
- a template‑mismatch factor r between a “bounce” bispectrum and the local template,
- a propagation of r into published SPHEREx σ(fNL) to yield significance ranges, plus a systematic “budget” treated additively in quadrature,
- a closed‑form Bayes‑factor comparison under stated priors.

The paper is detailed and careful in many places, with multiple “not directly comparable” caveats where appropriate. However, several load‑bearing numerical claims in the abstract and headline depend on partially specified weighting choices, scenario‑based (not covariance‑derived) uncertainty stacking, and a code repository that currently lacks a frozen DOI. These must be fixed for PRD standards.

Findings

P2-E1 (ESSENTIAL)
- Location: Abstract (pp. 1–2), Sec. III.B (pp. 8–9), Eq. (5) and surrounding text
- Problem: The amplitude‑recovery factor r is central to all headline significance numbers, but the paper does not give a mathematically explicit definition of the “SPHEREx‑like” and “LSS/SDB” Fisher weights w(k1,k2,k3) and the corresponding integration measure over triangle space. The text only states “under 10 physically motivated weighting schemes … SPHEREx‑like … scale‑dependent bias … CMB Fisher …” and references code artifacts. Without a precise, on‑paper definition of w and the domain/normalization, the reported r = 0.84 ± 0.02 cannot be reproduced from the PDF alone.
- Required fix: Provide explicit analytic expressions for each weighting used to compute r, including:
  - the measure on triangle space (e.g., integration in ln k bins; ordered triangles; any Jacobians),
  - the exact w(k1,k2,k3) for each scheme (CMB Fisher, SPHEREx‑like, SDB 1/k^2, “flat”), and how survey noise enters w,
  - the squeeze cut x3,min definition and whether any kmax truncation appears,
  - the normalization convention for the weighted average in Eq. (5).
  Include, in the PDF or SI, a small table that reproduces the four reported central r values from these formulas to the stated precision.

P2-E2 (ESSENTIAL)
- Location: Abstract (pp. 1–2), Sec. IV (pp. 9–10), Table IV (p. 20), Sec. VII (pp. 16–20), Fig. 2 (p. 11)
- Problem: The abstract’s “realistic ∼ 2.6–5σ” claim is adopted as a “headline forecast,” but the derivation relies on an ad hoc additive‑in‑quadrature stacking of heterogeneous systematics (GR projection, PNG bias bϕ priors, photo‑z degradation, ε‑correction, and a basis‑dependent null‑space scatter) not obtained from a joint Fisher/covariance analysis. The text acknowledges this scoping assumption in several places, but the abstract still presents the 2.6–5σ band as a realistic headline. For PRD, a headline must either (i) be supported by a survey‑appropriate covariance treatment or (ii) be explicitly labeled as a scenario‑based illustration, not a derived forecast.
- Required fix: Rephrase all occurrences of “realistic ∼ 2.6–5σ” as an explicitly scenario‑based illustration. State, in the abstract and Sec. IV/VII captions, that the combined number is not a derived Fisher result but a scoping exercise; list the exact additive‑quadrature ingredients used. Alternatively, provide a joint Fisher/covariance calculation (even simplified) showing the net σeff under simultaneous marginalization over the stated nuisance parameters, in which case the number can remain as a forecast.

P2-E3 (ESSENTIAL)
- Location: Data and Code Availability (p. 24)
- Problem: The repository DOI is missing: “Zenodo (DOI inserted at submission)” is a placeholder. PRD requires a permanent, citable record for reproducibility.
- Required fix: Archive a frozen release of the exact code/data used for this paper, provide a DOI, and record the commit hash and tag in the manuscript. Ensure that the archived package contains all artifacts referenced in the text (e.g., phase3 bispectrum shape overlap.json, c9g bf table recompute.py, appendix A1 wick doubling.py, etc.) and that paths/names match the manuscript.

P2-E4 (ESSENTIAL)
- Location: Sec. VI.C (pp. 12–16), Table II (p. 15)
- Problem: Bayes‑factor values for the Gaussian bounce prior (σtheory = 1.0, 0.5, 2.0) are quoted (e.g., 9.80) but the closed‑form used for the Gaussian‑prior numerator is not written in the PDF. Eq. (9) only treats the delta‑prior numerator (point hypothesis). The text says “replace the bounce likelihood by the prior‑convolved marginal,” but the formula is not given, preventing on‑paper reproduction of the BF=9.80 etc.
- Required fix: Add the explicit analytic expression for the Bayes factor when the “bounce” model has a Gaussian prior N(−35/8, σ2theory) and the competitor has a uniform prior [fmin, fmax]. Show the integral reducing to a Gaussian convolution and state the final CDF form used for the denominator. Include one fully worked numerical example in the PDF reproducing BF = 9.80 at σeff = 0.7, W = 30.

P2-E5 (ESSENTIAL)
- Location: Throughout; examples: Sec. II.A (pp. 3–5, footnote on p. 4), Sec. III.B (pp. 8–9), Sec. VI (pp. 12–16), Data & Code Availability (p. 24)
- Problem: The manuscript repeatedly embeds internal artifact and script names from the codebase (e.g., “artifact c9i epsilon ratio check.json”, “null space analysis.py”, “phase3 bispectrum shape overlap.json”). This is acceptable if and only if a frozen DOI/archive is provided (see P2‑E3) and if the text clearly maps each quoted number in the PDF to an artifact in the archive. Currently, without a DOI, these references are not verifiable and degrade reproducibility.
- Required fix: After providing the DOI (P2‑E3), add a single consolidated table (or SI section) that maps each load‑bearing scalar in the paper to the exact archived artifact (filename, path, and line or key). Alternatively, remove inline artifact names from the main text and move them to a Reproducibility Note in the appendix.

P2-E6 (ESSENTIAL)
- Location: Sec. IV (pp. 9–10), “Anomaly‑detected tracers” paragraph
- Problem: The paper claims a “∼ 10–20% improvement in σ(fNL)” from anomaly‑selected tracers based on a “preliminary Fisher forecast,” but no Fisher setup or numbers are shown or archived; this is a new claim not substantiated in the manuscript.
- Required fix: Either (i) remove the 10–20% quantitative claim, or (ii) provide a short SI with the Fisher setup (number densities, bias, redshift distribution, k‑range, shot‑noise model) and a single table that reproduces the %‑improvement quoted. Clearly flag this as illustrative if still preliminary.

P2-M1 (MAJOR)
- Location: Sec. II.A (p. 5, “injection/recovery test… rmeasured = 0.90 ± 0.01”), Sec. III.B (pp. 8–9)
- Problem: The injection–recovery cross‑check uses a 2D, flat‑sky KSW‑type estimator with isotropic Gaussian noise and no Galactic mask, labeled as “SPHEREx Gaussian noise covariance,” yielding rmeasured ≈ 0.90. This is not the SPHEREx 3D galaxy‑bispectrum weighting; the paper says this is a consistency check only, but the wording and the label “SPHEREx Gaussian noise covariance” risk misinterpretation as a survey‑matched validation.
- Required fix: Move the injection–recovery test to an appendix, rename the noise model to “toy diagonal Gaussian covariance,” and add a one‑line warning in the main text that this test is not survey‑commensurate and serves only to check the CMB‑Fisher style overlap endpoint.

P2-M2 (MAJOR)
- Location: Sec. II.A (pp. 4–5), Fig. 1 caption (p. 5)
- Problem: The paper reports null‑space scans (10,000 coefficient sets) and propagates their 16th–84th r percentiles into significance ranges (e.g., “4.4–6.2σ”) even while noting the basis‑dependence of the scan measure. This is appropriately caveated later but appears as quantitative statements near other σ values, risking misread equivalence.
- Required fix: When reporting any σ inferred from the null‑space scan, explicitly prefix with “basis‑dependent illustrative” and avoid juxtaposing those with the Fisher‑derived σ without an explicit “not directly comparable” disclaimer at the point of comparison.

P2-M3 (MAJOR)
- Location: Sec. V (p. 11), MegaMapper forecast paragraph
- Problem: The 7.4–7.7σ ideal significance (σ=0.5, r=0.84–0.88) is arithmetically fine, but the paragraph subsequently mixes this with the SPHEREx systematic budget (GR, bϕ at z≈1–2) to quote “2.6–5σ after the same GR marginalization and bϕ uncertainty budget,” which is not calibrated to the higher‑z MegaMapper regime and could be misleading.
- Required fix: Remove the “2.6–5σ after the same budget” statement for MegaMapper, or replace it with a clearly labeled placeholder (“illustrative only; not calibrated to z = 2–5 systematics”) and avoid reporting a combined number.

P2-M4 (MAJOR)
- Location: Sec. IX.D (pp. 21–23), joint (fNL, nfNL) Fisher
- Problem: The joint SDB Fisher results (σ(nfNL)=0.295/0.596; σmarg(fNL)=3.08/7.06; ρ=−0.87/−0.969) are useful but currently not reproducible from the PDF. The precise binning (six z bins), k‑cuts, tracer biases b1(z), number densities n(z), survey area fsky, and P(k) cosmology are not given in the paper.
- Required fix: Provide a table with: z‑bin edges, fsky, n(z), b1(z), kmin, kmax, shot‑noise model, and the fiducial cosmology used to compute P(k), T(k), D(z). This can be placed in SI but must be present for a reader to reproduce the joint Fisher numbers without the code.

P2-M5 (MAJOR)
- Location: Sec. II.C (pp. 6–7)
- Problem: The cubic‑order “bounce‑transfer” correction is quoted as δfNL ∼ 10−3 from a superhorizon scaling estimate. This number is not derived in the manuscript and is repeated in a way that looks like an estimate specific to the chosen LQC bounce scale.
- Required fix: Either provide the explicit scaling steps (with the assumed ηbounce and k‑range that give (k ηbounce)^2 ∼ 10−4 and hence δfNL ∼ 10−3), or restate this as an order‑of‑magnitude back‑of‑the‑envelope with no numerical value (e.g., “parametrically suppressed by (kηbounce)^2 for observable modes”).

P2-M6 (MAJOR)
- Location: Sec. VII.D (p. 18), bullets on photo‑z outliers and shot noise
- Problem: Several quoted %‑level degradations (e.g., “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼ 5%”, “shot‑noise degradation ∼ 15–30% at z ∼ 1–2”) are not derived in the paper and do not point to a concrete artifact (in contrast to most other numbers).
- Required fix: Either remove these specific percentages or supply a short derivation/estimate (or exact literature pointer) with numbers that lead to the stated %.

P2-M7 (MAJOR)
- Location: Appendix A (pp. 24–27), factor‑of‑two audit
- Problem: The operator‑algebra identity i⟨[ζ^3, L]⟩ = −2 Im⟨ζ^3 L⟩ is correctly stated. However, the text says “verified symbolically” without showing a minimal explicit worked example at the vertex level demonstrating how the single‑ordering expressions (Eqs. 34–36 of Cai et al.) map to half of the full in‑in result for one specific vertex or configuration. Given the centrality of this correction to the −35/8 vs −35/16 normalization, PRD readers will expect at least one concrete, textual calculation beyond the identity.
- Required fix: Add a compact worked example in the appendix: pick one vertex (e.g., Lζ(∂i∂jχ)^2), write explicitly the single‑time‑ordered Wick contractions for the equilateral configuration, and show how the commutator doubling produces the full result. Keep it short but explicit, so the factor of two is demonstrated not only by identity but via a concrete contraction count.

P2-M8 (MAJOR)
- Location: Table II (p. 15), Table III (p. 19), Sec. VI.C (pp. 12–16)
- Problem: Extremely large Bayes factors vs. SSFSR (e.g., 3.5×10^8) are quoted. While mathematically unsurprising for a point hypothesis at ~0 vs. −4.375 with σ≈0.7, the paper should avoid over‑emphasizing these as evidential since they are prior‑ and model‑class dependent (point vs. spread) and hinge on the assumption that the measured quantity is the gauge‑frame flocalNL.
- Required fix: Add an explicit sentence where these numbers appear saying that “these BFs vs. SSFSR are driven by the point‑hypothesis choice and the adopted observational (gauge‑frame) fNL; they should be interpreted as order‑of‑magnitude only, not robust evidence ratios across model classes.”

P2-N1 (MINOR)
- Location: Sec. III.A (p. 7), Eqs. (3)–(4)
- Problem: Dimensional analysis: Confirm the stated units explicitly. Δb is dimensionless; with M(k,z) = 2 k^2 T(k) D(z)/(3 Ωm H0^2) and Δb = 2 fNL (b1 − 1) δc / M, the units are consistent. Suggest writing “k in h Mpc−1 throughout; H0 in h 100 km s−1 Mpc−1; T→1 as k→0” one more time here to avoid ambiguity.
- Required fix: Add a one‑line note on units beneath Eq. (4) or in Sec. III.A text.

P2-N2 (MINOR)
- Location: Sec. II.A (pp. 4–5), null‑space radius discussion
- Problem: The basis‑dependence warning is good; however, “radius 50 is approximately 0.7×||cref||” would benefit from a numeric: ||cref||≈73 → 0.7×||cref||≈51, close to the chosen 50.
- Required fix: Add the numeric confirmation in a parenthetical.

P2-N3 (MINOR)
- Location: Sec. VIII.A (p. 18), Planck PR4 recast
- Problem: Recast arithmetic: rCMB = 0.876 leads to σ ≈ 5.71; |−4.375 + 0.1|/5.71 = 0.75σ. This is correct. Consider adding the actual σ number (5.71) in the text for transparency.
- Required fix: Add “σrecast = 5.71” explicitly.

P2-N4 (MINOR)
- Location: Sec. IV (pp. 9–10), “per‑bin SPHEREx σ(fNL) to ≈ 0.9–1.0”
- Problem: “per‑bin” is confusing in the bispectrum context (bins vs. tracer samples). Clarify what is per‑bin here.
- Required fix: Replace “per‑bin SPHEREx σ(fNL)” with “effective σ(fNL) after relaxing the bϕ universality prior per tracer/redshift bin.”

P2-N5 (MINOR)
- Location: Fig. 2 caption (p. 11), Fig. 4 (p. 17), Fig. 5 (p. 17)
- Problem: Axes appear to be clear from context, but the captions should explicitly state units (kmin in h Mpc−1; σ in dimensionless; significance in σ). Ensure all axes in the final PDF are labeled with units.
- Required fix: Add explicit units to all axes/captions.

P2-N6 (MINOR)
- Location: Appendix A.2 (p. 27), Table V
- Problem: Good to include both rows; add a brief parenthetical in the caption: “These two rows are not related by a Komatsu–Spergel normalization change; they differ by physical time‑ordering content.”
- Required fix: Add that sentence.

P2-N7 (MINOR)
- Location: References (pp. 27–28)
- Problem: Several 2025/2026 references (e.g., Addis et al. 2025 arXiv:2511.09466; Diego‑Palazuelos 2025) are forward‑dated and unverified at acceptance time. PRD accepts arXiv references, but please ensure each citation’s year, arXiv ID and title match and that preprints are publicly accessible.
- Required fix: Double‑check arXiv IDs and bibliographic fields; correct if needed.

P2-N8 (MINOR)
- Location: Throughout
- Problem: Some long parenthetical clarifications could move to footnotes to improve readability (e.g., the detailed Komatsu–Spergel c mapping in Appendix A is excellent; some inline references to code artifacts could be footnoted).
- Required fix: Editorial polish as desired.

P2-N9 (MINOR)
- Location: Sec. IX.C (p. 21), Decision thresholds
- Problem: The figure shows colored bands; consider adding a legend or a line in the caption defining the bands numerically (e.g., “dark green: |fNL+4.375| ≤ 1σ,” etc.) to make the thresholds exact.
- Required fix: Amend caption accordingly.

P2-N10 (NIT)
- Location: Minor typography
- Problem: A few hyphenation/spacing issues (“multi‑tracer”, “per‑configuration”, “order‑of‑magnitude”) are inconsistent.
- Required fix: Consistency pass.

Arithmetic and internal‑consistency audit highlights
- Template mismatch significance: 4.375×0.829/0.7 = 5.18σ; 4.375×0.876/0.7 = 5.47σ. The quoted 5.2–5.5σ band is consistent.
- GR‑degraded floor: σeff = √(0.7^2 + 1.0^2) = 1.2207; 4.375×0.84/1.2207 = 3.01σ. Matches text.
- “All‑combined” illustrative case: σeff = √(0.9^2 + 1.0^2) = 1.345; 4.375×0.84/1.345 = 2.73σ. Within the stated 2.6–2.8σ.
- Li single‑ordering stress test: 2.1875×0.84/0.7 = 2.63σ. Matches Table V.
- PR4 recast: with rCMB=0.876, σ=5.71 and offset |−4.375+0.1|=4.275, gives 0.75σ. Matches.
- τNL estimate: (36/25) f^2 = 1.44 × 19.14 = 27.6. Matches.
- Joint (fNL, nfNL): σmarg(fNL) ≈ σunmarg/√(1−ρ^2). For fixed‑bias: 1.53/√(1−0.87^2)=≈3.10 (text: 3.08). For bias‑marginalized: 1.75/√(1−0.969^2)=7.03 (text: 7.06). Consistent.

Length
The manuscript is dense; for a sensitivity recast (vs. a full new forecast) 28 pages is long. Much of the length is due to careful caveating and the detailed Bayesian section. If the authors implement the above fixes, the length is acceptable; otherwise, consider moving some of Sec. VI details and null‑space scan discussion to SI to keep the main text within ~22–24 pages.

Abstract‑last drift check (pattern‑045)
- “We audit … establish … that their intermediate … is exactly half the full result” → backed by Appendix A identity; add one worked example (P2‑M7).
- “Local estimator recovers 83%–88% … validated via …” → r endpoints appear in Sec. III.B; but formal weighting definition is missing (P2‑E1).
- “We adopt bispectrum‑only 5.2–5.5σ optimistic and 2.6–5σ realistic ranges as the headline forecast.” → must be softened to “illustrative” or supported by a joint Fisher (P2‑E2).
- “Bayes factor BF ≈ 9…14” → requires adding the explicit Gaussian‑prior formula (P2‑E4) and the DOI (P2‑E3).
- “A SPHEREx null would disfavor … at same ∼ 2.6–5σ” → same headline caveat as P2‑E2.

Provenance surfaces (patterns 046/047)
- DOI missing (P2‑E3).
- Multiple artifact names in text (P2‑E5).
- Ensure final archive matches names and contains the claimed outputs.

Uncomputed quantitative claims (pattern‑048)
- “10–20% improvement” (P2‑E6).
- “5% degradation with 10% photo‑z catastrophics” and “15–30%” shot‑noise degradation (P2‑M6).
- “δfNL ∼ 10−3” (P2‑M5).

Standalone‑reader test
- Many results are reproducible with added formulas; key missing pieces are the explicit r weighting, Gaussian‑prior BF expression, and the SDB Fisher inputs (P2‑E1, P2‑E4, P2‑M4).

Primary estimator pre‑declaration
- The paper clearly states it recasts Heinrich et al. (bispectrum Fisher, local template), and does not present a new estimator. This is fine.

Figures and tables audit
- Table I matches numbers in body; Fig. 1 benchmarks are consistent.
- Table II and III are internally consistent with Sec. VI, but require the Gaussian‑prior formula (P2‑E4) and a caution vs. SSFSR (P2‑M8).
- Table IV arithmetic is consistent with the reported numbers and uses the stated combination rules; headline caveat needed (P2‑E2).
- Table V is arithmetically consistent.

## Summary recommendation
MAJOR REVISIONS

The central idea (recasting SPHEREx sensitivity to a specific bounce prediction, and clarifying the Cai vs. Li factor‑of‑two) is valuable. However, several load‑bearing quantitative claims in the abstract and headline rely on (i) an incompletely specified r‑weighting, (ii) a scenario‑stacked “realistic” significance not derived from a joint covariance, (iii) missing on‑paper formulae for the Gaussian‑prior Bayes factors, and (iv) an unfrozen code archive. These are fixable. With the explicit weighting formulas, a toned‑down headline (or a proper joint Fisher), the Gaussian‑prior BF expression, and a frozen DOI, the paper would meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second‑pass audit)

P2-E7 (ESSENTIAL)
- Location: Sec. II.A (pp. 3–5), Eq. (2) and surrounding text
- Problem: The normalization factor 10/3 in BNL = (10/3) [∑ AT]/[∑ k_i^3] is never derived. Readers cannot reconstruct how the Maldacena-type shape function AT (Eq. 1) maps to the dimensionless, local‑normalized amplitude BNL in Eq. (2). This constant is load‑bearing for Table I values and for the “squeezed → −35/8” limit.
- Required fix: Provide the explicit normalization chain from the cubic action to Bζ(k1,k2,k3) and then to BNL, showing where 10/3 comes from and how it relates to the Planck local template Bζ = (6/5) fNL [PζPζ + perms]. Include a one‑line check at equilateral or squeezed that reproduces the numerical entries in Table I.

P2-M9 (MAJOR)
- Location: Fig. 6 caption (p. 21) and panel text
- Problem: The figure shows a “MegaMapper conservative (σ = 1.5)” bar, but σ = 1.5 for MegaMapper is not defined or justified anywhere in the body. Sec. V quotes σ ≈ 0.5 ideally and then an illustrative 3–7σ envelope, explicitly warning that it is design‑dependent; no “σ = 1.5 conservative” value is documented.
- Required fix: Remove the “σ = 1.5” bar or justify it with a cited forecast or a self‑contained calculation. If kept as an illustration, label it “illustrative only; not calibrated to z = 2–5 systematics” in the caption and in the text where Fig. 6 is discussed.

P2-M10 (MAJOR)
- Location: Sec. III.B (pp. 8–9), Eq. (6) and bullet list of r values
- Problem: The declared “noise‑weighted central value r = 0.84 ± 0.02” is not supported by the enumerated “noise‑weighted” examples given in the text: 0.829 (SDB), 0.830 (SPHEREx‑like), 0.835 (flat/uniform). Their simple average is 0.831, not 0.84; “flat/uniform” is not a noise‑weighted scheme, yet it is grouped with them. Without the full set of 10 weightings and their combination rule, 0.84 appears inflated relative to the list provided.
- Required fix: State precisely how the “central” r is formed (which subset of weightings, what averaging/weighting rule). If the 10‑scheme average is used, list those schemes and reproduce the 0.84 ± 0.02 from them. Otherwise, change the central value to match the documented subset or clearly separate noise‑weighted vs. non‑noise‑weighted cases.

P2-N11 (MINOR)
- Location: Sec. II.A (p. 5, long footnote and surrounding prose)
- Problem: Text refers to “the noise‑weighted central r = 0.84 of Table IV,” but Table IV does not define or derive r; it merely uses r = 0.84 in significance calculations.
- Required fix: Rephrase to “the r = 0.84 value used in Table IV” or add a small table that actually reports the r values and how the central figure was obtained.

P2-N12 (MINOR)
- Location: Sec. II.A (p. 4), line beneath Eq. (2)
- Problem: Notational glitch likely from typesetting: “… and k∑1 ≪ k is the squeezed (long‑wavelength) mode” is unclear. It seems to intend “k1 ≪ k with k ≡ k2 ≈ k3.”
- Required fix: Correct the notation to “k1 ≪ k with k ≡ k2 ≈ k3” to avoid ambiguity.

P2-N13 (MINOR)
- Location: Fig. 2 caption (p. 11)
- Problem: The caption mentions four MegaMapper bars (“template‑corrected ideal 7.4–7.7σ; the illustrative 3–7σ envelope; conservative; single‑tracer”) but the caption/body do not define the last two with numbers or inputs.
- Required fix: Define what “conservative” and “single‑tracer” correspond to (σ values and assumptions), or remove those bars. Make the caption self‑contained.

P2-B1 (BODY–FIGURE CONSISTENCY, MINOR)
- Location: Sec. V (p. 11) vs. Fig. 6 caption (p. 21)
- Problem: The body presents MegaMapper as “σ(fNL) ≈ 0.5 ideally” with a wide illustrative 3–7σ envelope; Fig. 6 adds a specific “σ = 1.5 conservative” without body support (see P2‑M9). This is a figure–body mismatch.
- Required fix: Align Fig. 6 content with Sec. V by either just showing the ideal and the illustrative envelope, or by adding body text that justifies the “σ = 1.5 conservative” number.

P2-C1 (DIMENSIONAL CONSISTENCY, MINOR)
- Location: Eq. (2), Eq. (1), surrounding text (pp. 3–5)
- Problem: While the text asserts degree counting for dimensionlessness, it never states the precise normalization of AT to a physical bispectrum Bζ (with the conventional factors of k−6 and power‑spectrum normalization). This ties back to P2‑E7: without an explicit Bζ ↔ AT map, dimensional consistency is opaque to readers unfamiliar with the specific “AT” convention used here.
- Required fix: Add one line tying AT to Bζ(k1,k2,k3) with units, making explicit how AT is defined (e.g., S(k) factors) so that Eq. (2)’s dimensionless nature follows immediately.

P2-F1 (ABSTRACT FAITHFULNESS, MINOR)
- Location: Abstract, sentence “We audit … establishing via the in‑in operator identity … that their intermediate ε‑order decomposition … is exactly half the full result …”
- Problem: The body (Appendix A) gives the operator identity and a qualitative mapping, but no explicit short vertex‑level worked example is shown to concretely demonstrate the 2× doubling for any single term (you already noted this as P2‑M7 in the first report; here the abstract claim slightly over‑promises the level of demonstration currently present).
- Required fix: Either tone down to “we show via the in‑in operator identity why the single time ordering is half of the full result” or add the requested short worked example (as already required in P2‑M7).

Explanation
This second pass focused on items typically missed on first review: normalization constants (10/3 in Eq. 2), figure–body coherence (MegaMapper “σ = 1.5” in Fig. 6), and internal numerical centering (the r = 0.84 “central value” vs. the listed 0.829/0.830/0.835). The earlier report already covered the major missing weight definitions, scenario‑stacked “realistic” headline, Gaussian‑prior Bayes‑factor formula, DOI, and several unsubstantiated percentages; I did not repeat those.