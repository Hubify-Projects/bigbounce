# P2 R23conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.45.pdf` md5=d421f116 pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7717 chars)
**Wall time**: 399.4s

---

Referee report for Physical Review D (methods/statistics) — Manuscript: “Testing the Matter Bounce with Primordial Non‑Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook” (22 pp)

Scope of review
I evaluated statistical methodology, derivation chains, dimensional consistency, internal arithmetic, figure/table consistency, and whether the abstract and conclusions are quantitatively supported by the body. All sigma values and quoted ratios were recomputed from the text. Findings below reference the rendered PDF’s section titles and page numbers seen in this submission.

ESSENTIAL ISSUES

P2-E1 (Appendix A pp. 18–19; Abstract p. 1; Sec. IV p. 8): Inconsistent bispectrum normalization conventions (c = 2 vs c = 6/5) for Bζ
Problem:
- Appendix A defines Bζ(k1,k2,k3) = c fNL [Pζ(k1)Pζ(k2)+2 perms] and states that the “Planck/Komatsu–Spergel convention” has c = 2 for Pζ. In contrast, the text elsewhere (Abstract, Sec. IV and the Heinrich et al. 2024 forecast it recasts) uses the local template Bζ = (6/5) fNL [Pζ Pζ + 2 perms], i.e., c = 6/5 for curvature ζ. These are not the same convention for the same field; c = 2 is the convention often used for the Bardeen potential Φ, not ζ. The manuscript switches conventions midstream while keeping Pζ in A1, which undermines the “convention” resolution and the claims that Cai’s −35/8 is the Planck normalization.
Required fix:
- Choose one normalization consistently (preferably the one used in Heinrich et al. 2024, i.e., Bζ = (6/5) fNL [Pζ Pζ + 2 perms]) or explicitly switch to BΦ with c = 2 and adjust all formulas and text accordingly. State clearly which field the power spectrum P(·) refers to in every equation.
- Re-derive the mapping between the Cai/Li normalizations and the survey estimator in that single convention. Show that all quoted σ(fNL), r, and detection significances are unchanged once the correct field and c are consistently applied. Update Appendix A accordingly.
Classification: ESSENTIAL

P2-E2 (Abstract p. 1 vs. Sec. III.B pp. 6–7 and Sec. IV p. 8): Inconsistent “5.2–5.5σ” optimistic headline range w.r.t. ε-correction
Problem:
- Abstract claims “5.2–5.5σ” before GR and bϕ degradation, explicitly stating the range reflects both r = 0.84 ± 0.02 and the ε-correction. Using the stated ranges yields a minimum pre-systematic significance below 5.2σ if the 8% ε-shift is realized: with fNL = −4.02 (8% less negative than −4.375) and r = 0.83, |f|/σ × r = (4.02/0.7) × 0.83 ≈ 4.76σ. Sec. IV sometimes fixes fNL = −4.375 and reports 5.2–5.5σ, omitting ε.
Required fix:
- Provide one consistent pre-systematic range with explicit endpoints for the full stated ranges of r and ε. Either:
  a) keep fNL fixed at −4.375 and quote 5.19–5.48σ (r=0.83–0.876), or
  b) include the ε uncertainty and quote the true envelope, which reaches as low as ≈4.76σ at (r=0.83, fNL=−4.02).
- Reflect this consistent range in the Abstract, Sec. III.B, and Sec. IV.
Classification: ESSENTIAL

P2-E3 (Sec. IX.D p. 16): Version-history language in the body of the paper
Problem:
- The manuscript includes “Correction note: an earlier version of this analysis quoted substantially tighter joint constraints … those values could not be reproduced … are withdrawn.” PRD does not permit version-history annotations in the main text.
Required fix:
- Remove all version-history/correction-note prose from the main text. Present only the final, validated results. If needed, a short methodological footnote can say “we verified our pipeline against [Doré et al.] and obtained …”; no references to withdrawn values or earlier drafts.
Classification: ESSENTIAL

P2-E4 (Abstract p. 1; Sec. II pp. 4–5; Sec. III.B p. 7): Mixing non-comparable validation channels without explicit caveats at the point of juxtaposition
Problem:
- The abstract’s validation triad (“ℓ-space Fisher overlap, 200 injection–recovery realizations, 10,000-sample null-space scan”) is presented as a single validation block for the r overlap. Only later in the body do you qualify that the injection–recovery test uses isotropic Gaussian noise and a KSW-type estimator (CMB-like weighting), not the SPHEREx LSS noise model. The reader is led to compare CMB-Fisher, LSS noise-weighted r, and KSW-injection numbers side-by-side.
Required fix:
- At every place where these three channels are presented together (Abstract and Sec. III.B), add a one-sentence explicit disclaimer that the CMB-Fisher and KSW injection validations are not directly comparable to the LSS/SPHEREx noise-weighted overlap r, and that only the LSS-weighted r enters the SPHEREx recast.
Classification: ESSENTIAL

P2-E5 (Appendix A p. 18): “Detection significance is convention independent” assertion requires proof in this context
Problem:
- The text states that |fNL|/σ(fNL) is convention-independent because σ scales inversely with c and fNL scales with c. This only holds if the survey’s quoted σ(fNL) is computed in exactly the same convention and field variable. Given the c=2 vs c=6/5 inconsistency for Bζ in this manuscript (P2-E1), the claim must be demonstrated explicitly in the convention used by Heinrich et al. (and SPHEREx).
Required fix:
- After resolving P2-E1, show algebraically that the Heinrich σ(fNL) rescales exactly with c in your chosen convention, or avoid the absolute claim and state the narrower fact: “in our chosen normalization (…., with Pζ), the forecast σ(fNL) = 0.7 applies and the detection significance reported is consistent.” Remove the broad invariance claim if not proven.
Classification: ESSENTIAL

P2-E6 (Table III p. 14 and Sec. VI.C pp. 9–11): Bayes factor against SSFSR — contradictory description and over-precision
Problem:
- Table III lists precise numbers for “BF vs. SSFSR” (e.g., 3.3×10^6, 4.1×10^4, 329), while the text says these are “prior-width dependent and quoted to order of magnitude only.” For a point prediction (SSFSR fNL ≈ 0), there is no prior width in the null; BF reduces to a likelihood ratio (possibly marginalized over GR nuisance). The current presentation is contradictory and suggests spurious precision.
Required fix:
- Either: (i) present the analytic likelihood-ratio calculation used for SSFSR and keep only one significant figure (e.g., 3×10^6), or (ii) remove the table entries and state “BF vs SSFSR is O(10^6) in the ideal case and O(10^2–10^3) when GR degradation is marginalized,” making clear there is no prior dependence for the SSFSR point hypothesis. Define P(BF>3) precisely, including the sampling distribution used.
Classification: ESSENTIAL

MAJOR ISSUES

P2-M1 (Sec. II pp. 4–5): Injection–recovery methodology uses a 2D KSW-type estimator for a 3D LSS problem
Problem:
- The injection–recovery test claims to validate amplitude recovery for SPHEREx using a KSW-type (CMB) estimator on flat-sky tiles, with Gaussian noise taken from SPHEREx photometric-z power spectra. This mixes a 2D CMB bispectrum estimator with a 3D galaxy bispectrum context; the mapping is unclear.
Required fix:
- Either replace this test with a 3D galaxy-bispectrum estimator on mock catalogs (or remove the injection test as a validation of r for SPHEREx), or explicitly downgrade it to a qualitative cross-check and state its limitations prominently.
Classification: MAJOR

P2-M2 (Sec. III.B p. 7; Sec. II pp. 3–4): Quantify the impact of null-space scatter in r on the detection significance
Problem:
- You report a broad null-space range r = 0.55–1.14 (median 0.85, IQR 0.75–0.94) but then state this “does not materially affect” the forecast. In worst cases the significance would drop to ≈3.4σ pre-systematics.
Required fix:
- Provide a quantitative propagation: e.g., show the 16–84% range of |fNL| r / σ over the 10,000 coefficient samples under your LSS/SPHEREx-like weighting. Include this range in the “3–5σ” post-systematics envelope and state clearly which statistic (median, percentile) is used for the headline.
Classification: MAJOR

P2-M3 (Sec. IV p. 8): “10–20% improvement from anomaly-selected tracers” lacks a supporting forecast
Problem:
- A “preliminary Fisher forecast” is cited with no details, inputs, or figure/table. As written, this reads as speculation.
Required fix:
- Either include a brief, reproducible Fisher calculation (number densities, bias, redshift distribution, and marginalization assumptions) or remove the improvement claim.
Classification: MAJOR

P2-M4 (Sec. VIII.B p. 15, Eq. 8–9): κ1 ∈ [5.6, 80] bound is asserted without a derivation or citation
Problem:
- A 14× range is substantive and is later used to motivate σtheory choices. No derivation or reference for the upper bound (≈80) is provided.
Required fix:
- Provide a short derivation in an appendix (even schematic) or cite a published calculation justifying both endpoints. Otherwise, state only the qualitative uncertainty and do not use this numeric range to set priors.
Classification: MAJOR

P2-M5 (Sec. VI.C pp. 9–11; Table II p. 11): Monte Carlo ensembles and BF precision
Problem:
- You report results from 3 ensembles of 10^5 realizations each but present only single BF values (“~9.80”, “~13.91”). No convergence or uncertainty on BF is given; mixing analytic and MC results blurs what the ± spread represents.
Required fix:
- Report BF medians with 68% intervals across realizations (and/or analytic values only). State clearly whether quoted spreads come from prior sampling or noise draws. Include at least a basic convergence check (e.g., stability vs. sample size).
Classification: MAJOR

P2-M6 (Sec. II.C p. 5): “Bounce contribution δfNL ∼ 10^−3” near the LQC bounce not referenced
Problem:
- A semi-analytic estimate is quoted without a concrete derivation or citation.
Required fix:
- Provide a reference with this quantitative estimate, or rephrase to “plausibly suppressed by (kηbounce)^2; a full third-order computation is needed.”
Classification: MAJOR

P2-M7 (Sec. VIII.B p. 15): Notation collision between κ1 (fNL–ns slope) and c1 (bispectrum polynomial)
Problem:
- Despite a parenthetical warning, re-using κ1 and c1 in the same paper is error-prone.
Required fix:
- Rename one of the symbols (e.g., use α1 for the fNL–ns slope) to avoid confusion.
Classification: MAJOR

P2-M8 (Sec. VIII.A p. 14): Planck PR4 recast arithmetic
Problem:
- From fNL = −0.1 ± 5.0 (local), dividing by r = 0.876 gives ±5.71. Distance to bounce prediction is |−4.375 − (−0.1)|/5.71 = 4.275/5.71 ≈ 0.75σ, not 0.7σ as stated.
Required fix:
- Correct to 0.75σ (or 0.8σ), and ensure consistent rounding throughout.
Classification: MAJOR

P2-M9 (Sec. II.C pp. 5–6): “0.5000 ratio” check for the ϵ-decomposition is asserted but not shown
Problem:
- You claim an exact 0.5000 ratio at three bench points but provide no numbers.
Required fix:
- Add a small table in an appendix listing the intermediate and full-polynomial values at the three configurations, demonstrating the 0.5000 ratio to the stated precision.
Classification: MAJOR

P2-M10 (Figures pp. 4, 8, 12, 16): Axes/units/definitions
Problem:
- Several figures appear without explicit axis units or definitions (e.g., what exact normalization of BNL is plotted, how k is scaled, etc.).
Required fix:
- Ensure every figure has fully labeled axes (symbols and units) and captions define all plotted quantities and normalizations.
Classification: MAJOR

MINOR ISSUES

P2-m1 (Sec. II.A p. 3–4): Typo/garbling in text: “0.T heradiusanduniformsampling…”
Required fix: Correct the broken text and ensure footnote formatting is proper.
Classification: MINOR

P2-m2 (Sec. III.B p. 7; Appendix A p. 20): Internal file names in prose
Problem: References to “phase3 fisher overlap.json” and “appendix A1 wick doubling.py” belong in the Data/Code section, not the main text.
Required fix: Move these mentions to the Data and Code Availability section, or remove.
Classification: MINOR

P2-m3 (Sec. II.A p. 3): Missing numerical choices for kmin, kmax, cosmology
Required fix: State the k-range and cosmological parameters used in Fisher and overlap computations.
Classification: MINOR

P2-m4 (Conclusion p. 18): Frame nomenclature
Required fix: Tighten language to avoid implying that the CFC statement is an observable; ensure consistent “gauge-frame observable vs CFC theoretical point” phrasing everywhere.
Classification: MINOR

P2-m5 (Eq. (1), Abstract template statement): Clarify what P(k) is
Required fix: State explicitly whether P denotes a curvature (Pζ) or potential (PΦ) power spectrum, and the epoch of evaluation.
Classification: MINOR

P2-m6 (General): Tone and wording
Required fix: Replace colloquialisms (“headline,” “bookend,” “optimistic”) with standard scientific phrasing.
Classification: MINOR

P2-m7 (Sec. IV p. 8; Conclusion p. 18): Mission timeline language
Required fix: Soften time-dependent statements (“launched March 2025; data through ∼2027”) to avoid rapid obsolescence; cite mission documentation instead.
Classification: MINOR

P2-m8 (Sec. IX.E p. 17): Cosmic birefringence paragraph is off-scope
Required fix: Remove or move to a brief “context” sentence in the discussion; it is not methodologically relevant here.
Classification: MINOR

P2-m9 (Sec. III.B p. 7): Define weighting schemes quantitatively
Required fix: Provide equations or detailed descriptions for “SPHEREx-like,” “LSS weighting,” and “CMB Fisher weighting.”
Classification: MINOR

P2-m10 (Throughout): Define error bars
Required fix: Clarify whether “±” denote standard deviations over realizations, standard errors of the mean, or 68% credible intervals, for r, rcos, injection tests, and BF.
Classification: MINOR

NITS

P2-n1 (General): Overuse of “∼” and informal qualifiers; standardize formatting.
P2-n2 (General): Hyphenation consistency (e.g., multi-tracer, bispectrum-only).
P2-n3 (General): The paper is long for a sensitivity recast. Recommended maximum length ≲16 pages by moving ancillary material (e.g., QSFI excursus, birefringence) and lengthy priors discussion to an appendix.
P2-n4 (Sec. VI.C): Replace library-specific mentions (e.g., scipy.stats.norm) with generic “Gaussian integral evaluation.”
P2-n5 (Figures): Provide higher-resolution images and, where possible, numerical tables backing the plotted curves.

Additional arithmetic/consistency checks
- |f_bounce|/|f_inf| ratio: 4.375/0.015 ≈ 291.7 — “≈ 290” acceptable.
- Degradation factors: 1/r for r = 0.876, 0.83, 0.829 → 1.141, 1.205, 1.206 — numbers in text consistent.
- τNL ≥ (6 fNL/5)^2 with fNL = −4.375 gives τNL ≥ 27.56 — consistent.
- Li–Brandenberger halved significance entries (2.63σ) match 2.1875×0.84/0.7 = 2.63 — consistent.

Novelty claims
- “We quantify for the first time the template mismatch …” is stated. Please soften to “We quantify the template mismatch …; to our knowledge, this has not been quantified previously for the matter-bounce bispectrum,” or provide a literature check citation.

## Summary recommendation
MAJOR REVISIONS

The paper presents a potentially useful sensitivity recast and shape-overlap analysis, but it contains several essential issues that must be corrected before it can meet PRD standards. Chief among them are a normalization inconsistency (c = 2 vs 6/5 for Bζ) that affects the convention-resolution argument, an optimistic significance range that is inconsistent with the stated ε-uncertainty, and version-history language in the main text. Additional methodological clarifications (3D vs 2D estimator use, quantitative propagation of r scatter into significance, and a documented derivation or citation for the κ1 range) are required. Addressing these points, tightening the presentation, and consolidating conventions should resolve the major concerns.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

P2-E7 (Abstract p. 1; Sec. II.C pp. 5–6; Table I p. 4): “0.500±0.001 ratio” claimed to be “reported individually in Sec. II C and Table I,” but Table I contains no such ratios
Problem:
- The abstract says the intermediate ε-order decomposition reproduces “approximately half the full polynomial at each of the three benchmark configurations (per-configuration ratios 0.500 ± 0.001 …; reported individually in Sec. II C and Table I).” Table I lists only BNL values, not the 0.500 ratios. Sec. II C also does not tabulate or numerically display those ratios per configuration.
Required fix:
- Either add a table (in Sec. II C or an appendix) listing both the intermediate and full-polynomial values and their ratios for the three benchmarks, or remove the claim that these are “reported individually” in those sections.
Classification: ESSENTIAL

P2-E8 (Abstract p. 1; Sec. IX.C p. 16): “SPHEREx null would disfavor the quasi-dust matter bounce … at >4σ” conflicts with the paper’s own conservative envelope
Problem:
- The body repeatedly states a post-systematics significance range of ~3–5σ. A “null” centered at zero with the low end of the ε-shift (fNL ≈ −4.02) and the adopted noise-weighted r ≈ 0.83 is only ≈4.8σ pre-systematics and can fall below 4σ after the full systematic budget (as the paper elsewhere allows). The unqualified “>4σ” statement is therefore not robust against the paper’s own conservative settings.
Required fix:
- Qualify the sentence to match the stated systematic envelope (e.g., “typically >4σ under our baseline assumptions; can fall to ~3–4σ in the conservative GR/bϕ scenario”). Provide the explicit parameter choices that give >4σ.
Classification: ESSENTIAL

P2-E9 (Appendix A p. 19–21; Table IV p. 21): Internal contradiction — “detection significance is convention independent” vs. Table IV’s 5.25σ vs. 2.63σ entries
Problem:
- Appendix A asserts |fNL|/σ(fNL) is convention-independent. Table IV then computes 5.25σ (Cai convention) and 2.63σ (Li–Brandenberger convention) using the same σ(fNL)=0.7, i.e., a convention-dependent significance. This directly contradicts the claimed invariance and stems from mixing a changed c with a fixed σ(fNL) taken from a different convention.
Required fix:
- After resolving the Bζ convention (see P2-E1 from the initial report), either (i) rescale σ(fNL) consistently with c so that Table IV shows identical significance in both rows, or (ii) remove the “convention independent” claim. The table, if kept, must demonstrate internal consistency under the chosen convention.
Classification: ESSENTIAL

P2-M11 (Eq. (1) p. 3; Abstract template statement): Notation collision — P used both for the degree‑9 polynomial and for a power spectrum elsewhere
Problem:
- Eq. (1) defines P(k1,k2,k3) as a degree‑9 polynomial in wavenumbers, while elsewhere P(k) denotes a power spectrum (e.g., in the abstract’s local template Bζ = (6/5) fNL [P(k1)P(k2)+…]). This dual use of P in the same manuscript is confusing, especially given Appendix A’s explicit Pζ.
Required fix:
- Rename the degree‑9 polynomial to a distinct symbol (e.g., 𝒫9 or Q), and reserve P for power spectra with clear subscripts (Pζ, Pm). Update all occurrences for clarity.
Classification: MAJOR

P2-M12 (Sec. II.A p. 3): Scan radius arithmetic error — “radius 50 is approximately 7× ∥cref∥” is false
Problem:
- The text claims radius 50 is “approximately 7×” the Euclidean norm of cref = (2,7,3,−12,−69,19), which has ∥cref∥ ≈ √5328 ≈ 73. Radius 50 is ~0.68×, not 7×. The sentence is also visibly garbled (“0.T heradius…”), making intent ambiguous.
Required fix:
- Correct the arithmetic (likely intended “~0.7×”) and fix the garbled text. If the intended point is “radius is O(∥cref∥)”, state it quantitatively and consistently with the subsequent radius 10/100/500 scans.
Classification: MAJOR

P2-M13 (Sec. VII.D p. 13): Photometric‑z outlier degradation claims lack quantitative support or citation
Problem:
- The paper states that “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ~5% (from 0.70 to 0.74)” for the bispectrum channel, without a calculation, figure, or citation specific to SPHEREx bispectrum performance.
Required fix:
- Provide a quantitative derivation or simulation supporting the ~5% figure, or cite a published analysis with comparable instrument and estimator assumptions. Otherwise, soften to a qualitative statement without numbers.
Classification: MAJOR

P2-M14 (Eq. (2) p. 3): Ambiguous/possibly dimensionally inconsistent definition of BNL
Problem:
- Equation (2) prints “BNL = (10/3) P / AT_i k_i^3 → …” with unclear numerator/denominator grouping and undefined summation/index notation (“AT_i ki^3”). It is not evident how this ratio becomes dimensionless or how AT and P are normalized to produce the stated squeezed limit.
Required fix:
- Rewrite Eq. (2) with explicit definitions and parentheses (e.g., BNL ≡ (10/3) P(k1,k2,k3) / [AT(k1,k2,k3) Σi k_i^3] if that is intended). Ensure each quantity’s units are stated and the squeezed-limit normalization is shown transparently.
Classification: MAJOR

P2-M15 (Sec. II.C p. 6 vs. Sec. II overall): Cross‑reference mismatch — “four-vertex numerical evaluation” attributed to Sec. II.C (Assumptions)
Problem:
- The text refers to “evaluating all four cubic-action integrals … discussed in Sec. II C.” Sec. II C is the Assumptions section and does not contain that derivation or a numerical evaluation procedure.
Required fix:
- Correct the cross-reference to the section or appendix that actually discusses the four-vertex computation (or add a brief derivation there). Mislabeling obstructs verification.
Classification: MAJOR

P2-m11 (Sec. II.C p. 6 vs. Sec. II.A p. 4): Precision mismatch on the “half” check — “0.500±0.001” vs. “exact 0.5000”
Problem:
- Sec. II.A mentions 0.500±0.001; Sec. II.C claims an “exact 0.5000 ratio.” These statements are inconsistent in precision and leave unclear which is being claimed.
Required fix:
- Adopt one consistent numerical precision (with uncertainty) for this check, and provide the underlying numbers (see P2-E7).
Classification: MINOR

P2-m12 (Appendix A p. 20): Operator-formula typography and vacuum labels
Problem:
- Eq. (A2) mixes bracketed commutators and vacuum kets/bra annotations in a way that obscures the time-ordering and vacuum specification. While likely correct in spirit, the notation is hard to parse.
Required fix:
- Standardize the in–in expression to a conventional form (e.g., SK contour), define the states explicitly once, and remove dangling “0” subscripts/superscripts that are not used elsewhere.
Classification: MINOR

P2-m13 (Sec. IX.D p. 16): Mixed σ(fNL) provenance in the same paragraph can confuse readers
Problem:
- The paragraph interleaves the bispectrum-only σ(fNL)=0.7 (Heinrich et al.) with SDB-only joint Fisher numbers (σmarg values) and references a previously withdrawn tighter result. Although you add a “to avoid confusion” preface, the blend is dense and risks misinterpretation.
Required fix:
- Separate the two Fisher contexts into distinct bullets with explicit labels (“bispectrum-only” vs “SDB-only joint”), and remove any vestiges of version-history (already requested in P2-E3).
Classification: MINOR

Explanation
These items are new relative to the initial review. They focus on additional arithmetic/cross-reference inconsistencies, an internal contradiction between a claimed invariance and a worked example table, equation clarity/dimensions, and missing quantitative backing for a specific systematic claim. Addressing them, together with the previously flagged essential and major issues, will materially improve rigor and reproducibility.