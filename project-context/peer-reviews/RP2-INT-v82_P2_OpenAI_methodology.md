# P2 RP2-INT-v82 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=db185208 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7958 chars)
**Wall time**: 787.7s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
I assessed methodology rigor: statistical validity, derivation chains, dimensional consistency, internal arithmetic, error propagation, estimator definitions, and figure/table consistency. I re-computed all headline numbers. Below I list all findings, with severity class, location, quoted text/equation, and required fix.

ESSENTIAL ISSUES

P2-E1 — Data/code DOI placeholder and frozen release missing
- Location: Data and Code Availability (p. 25–26)
- Text: “archived at Zenodo (DOI inserted at submission).”
- Problem: The DOI is a placeholder. PRD requires a citable, immutable archive for all analysis artifacts referenced in text (scripts, JSON outputs).
- Required fix: Provide a working, final Zenodo (or equivalent) DOI corresponding to the exact code/data used for this submission, including a frozen commit hash. Ensure all file names referenced in the manuscript exist in that archive.

P2-E2 — Meta editorial language in the body
- Location: Sec. IX.D, “Channel hierarchy and sub-labeling note” (p. 23)
- Text: “(Sec. IX.D in the standard Physical Review D sectioning of the submitted manuscript)”
- Problem: Meta-reference to the submission and PRD sectioning belongs neither in body text nor in a published article.
- Required fix: Remove all meta-editorial language about the submitted manuscript’s structure or journal processes.

P2-E3 — Ambiguity in the Bayes-factor competitor model class and priors
- Location: Sec. VI.C (pp. 12–16), Table II (p. 16), Table III interplay
- Text: Repeated references to “tuned multifield competitor,” with priors [−15,+15] or [−5,+5].
- Problem: The “tuned multifield competitor” is not precisely defined (which physical class and likelihood/shape?). BF values are highly prior-sensitive; without a precise competitor definition the BF headline can be misleading.
- Required fix: Precisely define the competitor model class (e.g., local-shape multifield with uniform prior on amplitude only, no running, no shape variation) and justify prior ranges with citations. State explicitly that competitor likelihood uses the same (local-template) likelihood as the bounce recast and carries no template mismatch. If shape/scale dependence differs, show the exact likelihood assumed or limit the BF claims to the stated local-amplitude-only competitor.

P2-E4 — Abstract/conclusions wording implies “after systematics” upper endpoint includes cases without GR degradation
- Location: Abstract (p. 1–2), Sec. IV (p. 10–11), Table IV (p. 21)
- Text (abstract): “bispectrum-only 5.2–5.5σ … reducing to a realistic ∼2.6–5.5σ after the systematic budget…”
- Problem: The “5.5σ after systematics” endpoint corresponds to the case omitting GR and bϕ degradations (i.e., optimistic). The phrase “after the systematic budget” reads as if all listed systematics have been applied.
- Required fix: Rephrase everywhere to “a post-systematics envelope spanning ∼2.6–5.5σ, from a conservative case (bϕ-widened + GR-marginalized) to an optimistic case (minimal additional systematics).” This must be consistently reflected in the abstract and conclusions.

P2-E5 — Heinrich et al. σ(fNL)=0.7 used at nonzero fiducial fNL: covariance invariance claim needs support
- Location: Sec. IV (p. 10), Eq. (7)
- Text: “the fractional covariance correction … ≲ 5×10−4, well below the percent level.”
- Problem: The statement is justified by a heuristic primordial-field scaling and not by a galaxy-bispectrum covariance re-derivation. It is load-bearing for using σ=0.7 at fNL≠0.
- Required fix: Either (i) provide a literature citation demonstrating negligible covariance change for multi-tracer galaxy bispectra at |fNL|≈4, or (ii) relegate this to a clearly labeled heuristic check, softening language (“likely negligible under standard assumptions”) and removing the firm “≲5×10−4” unless backed by an explicit galaxy-field covariance estimate. State explicitly that your headline remains a sensitivity recast conditioned on this assumption.

P2-E6 — Definition of SPHEREx-like and LSS weighting for r is underspecified
- Location: Sec. III.B (pp. 8–9)
- Text: “SPHEREx-like weighting,” “scale-dependent-bias weighting (1/k^2),” “CMB Fisher (k^2).”
- Problem: The exact Fisher weights, k-ranges, triangle grids, and survey window functions behind each weighting are not fully specified, yet r=0.84±0.02 is load-bearing.
- Required fix: Provide explicit mathematical definitions of the weights used for each case (including k-range, binning, and any window/mask factors) or move these definitions into an appendix/Supplement with equations sufficient to reproduce r. The reader must be able to implement and obtain the stated r values.

P2-E7 — Injection–recovery statistic lacks definition of uncertainty measure
- Location: Sec. II (pp. 5–6)
- Text: “rmeasured = 0.90 ± 0.01”
- Problem: It is unclear whether ±0.01 is the standard deviation across 200 realizations or the standard error on the mean. The noise/covariance specification (diagonal Gaussian noise, photometric-z power spectra) is also too terse to reproduce.
- Required fix: Specify whether the quoted ±0.01 is SD or SEM; provide the exact noise covariance used (units, bandpower binning, patch tiling, and normalization). Clarify that this 2D flat-sky CMB-style test is only a qualitative cross-check (not PRD-load-bearing) and is not used in any quantitative SPHEREx forecast.

P2-E8 — File-name and artifact references in body must be moved to Supplement/DA
- Location: Throughout (e.g., pp. 3–5, 8–9, 12–16)
- Text: e.g., “artifact c9i epsilon ratio check.json”; “null space analysis.py”; “phase3 bispectrum shape overlap.json”
- Problem: PRD style discourages implementation details in the main narrative. These hinder readability.
- Required fix: Move all file-name/path references to the Data Availability or a Supplementary Material section. In the body, replace with generic “see Supplemental Material.”

P2-E9 — Figures must show units and axis labels explicitly
- Location: Fig. 1 (p. 6), Fig. 2 (p. 11), Fig. 4–6 (pp. 18–22)
- Problem: From the captions and visible axes, units/labels are not fully specified (e.g., k-units; whether the y-axis in Fig. 1 is dimensionless; significance units in later figures).
- Required fix: Ensure every axis has label and units (e.g., k in h Mpc−1; “Detection significance (σ)”; “BNL (dimensionless)”), and that captions specify weighting/assumptions used for each bar/curve.

MAJOR ISSUES

P2-M1 — Prior-sensitivity of Bayes factors needs a compact, reproducible summary table with exact assumptions
- Location: Sec. VI.C (pp. 12–16), Table II (p. 16)
- Problem: The BF narrative is long and technically dense. A concise summary table listing, for each BF entry: likelihood σeff, bounce prior type/width, competitor prior/width, and whether template rebooking is applied is needed for clarity and reproducibility.
- Required fix: Add a one-page appendix table with these columns and the exact numerical BF values (both r→1 and r=0.84), then shorten the main-text narrative accordingly.

P2-M2 — SVD/null-space analysis: matrix and basis not provided
- Location: Sec. II.A (pp. 3–5)
- Text: “We constructed the 3×6 constraint matrix… SVD… σ3/σ1 ≈ 0.3…”
- Problem: The actual 3×6 matrix (with your monomial basis ordering) is not given, so the claim cannot be checked.
- Required fix: Provide the explicit 3×6 matrix entries (numerical) and the basis monomials (in order), either inline or in an appendix/Supplement. Include the three benchmark triangles used.

P2-M3 — Sub-percent numeric assertions without uncertainties
- Location: Sec. III.B (p. 9): “varying x3,min … changes r by < 0.0002”; Sec. VI.C (p. 13): “approximation error 0.14%…”
- Problem: Statements with four significant figures are not meaningful in the absence of a full numerical error budget and fixed code revision.
- Required fix: (i) Attach the immutable archive (E1) and report these as reproducible outputs from that release, or (ii) soften language to “changes are numerically negligible at the 10−3 level for our grid” and remove the superfluous precision.

P2-M4 — GR-systematics parameterization and linkage to literature
- Location: Sec. VII.C, Table III (pp. 18–20)
- Text: σGR ∈ {0,0.5,1.0} as a stress-test grid; claims of “∼3σ” and “∼20σ” biases in Addis et al. citations.
- Problem: While you clearly state this is a stress test, the normalization is not traceably connected to a SPHEREx-like analysis. The values are used to produce the “realistic” envelope.
- Required fix: Add a dedicated paragraph making explicit that σGR is an abstract nuisance amplitude calibrated only at the order of magnitude to Addis et al., not a forecast for SPHEREx; reiterate that the 2.6–5.5σ “after systematics” is an envelope across σGR realizations rather than a single post-marginalized forecast.

P2-M5 — rcos heuristic and “projection noise is subdominant” assertion
- Location: Sec. III.B (pp. 8–9)
- Text: “1 − rcos^2 ≈ 0.03 … confirms projection noise is subdominant…”
- Problem: rcos is computed in an unweighted shape metric; concluding subdominance for the survey estimator is not rigorous.
- Required fix: Reword to: “rcos computed in an unweighted shape metric is high (≥0.97), suggesting projection noise is likely subdominant; a full estimator-covariance calculation would be required to demonstrate this rigorously.” Remove the definitive “confirms.”

P2-M6 — Move AI-tooling acknowledgement to acknowledgments or remove
- Location: Acknowledgments (p. 28)
- Text: “AI-assisted software tooling (Anthropic Claude) was used…”
- Problem: PRD style typically does not include tool brand names unless strictly necessary; it may raise questions about authorship or provenance.
- Required fix: Either remove this sentence or generalize it to “automated code-assistance tools were used for drafting and consistency checks; all scientific claims are the author’s responsibility.”

P2-M7 — SPHEREx-like vs SDB redshift samples and bins
- Location: Sec. IX.D (p. 23)
- Text: “six SPHEREx low-redshift bins (z = 0.1–1.5…) … different tracer selection from the z≈0.5–2 emission-line sample…”
- Problem: The exact bin edges and number densities are not specified, but the quoted σ(fNL) values depend on them.
- Required fix: Provide a table of the six bins (z-range, n̄, b1) and the sky fraction used for the SDB Fisher; include whether bϕ is fixed or marginalized for each run.

P2-M8 — Heinrich bispectrum forecast and bϕ-degradation mapping
- Location: Sec. VII.B and Fig. 5 (pp. 17–18)
- Problem: The statement that relaxing UMF universality degrades the SPHEREx bispectrum σ(fNL) from 0.7 to 0.9–1.0 is not derived within your Fisher and not cited.
- Required fix: Provide a quantitative derivation or a literature citation specific to bispectrum forecasts (not only SDB) showing the stated 20–50% widening, or qualify this as a heuristic extrapolation.

P2-M9 — Long narrative; consider restructuring/condensing
- Location: Whole manuscript
- Problem: For a sensitivity recast of a single imported baseline plus template-overlap and BF framing, 30 pages (main text + appendices) is excessive for PRD.
- Required fix: Move implementation details (null-space methodology, file references, extended BF derivation) to a Supplement. Target ≤ 20 pages main text without loss of scientific content.

MINOR ISSUES

P2-N1 — Clarify estimator status in abstract and conclusions
- Location: Abstract (p. 1–2), Conclusions (p. 25)
- Problem: Although the abstract opens with “sensitivity recast,” later sentences could be read as “forecasted measurement precisions.”
- Required fix: In both places, add “sensitivity envelope (recast of Heinrich et al. 2024) rather than an independent forecast” at the end of the main significance sentence.

P2-N2 — Terminology consistency: “bookkeeping / rebooking”
- Location: Sec. VI.C (pp. 15–16)
- Problem: “bookkeeping” and “rebooking” are nonstandard terms and may confuse.
- Required fix: Replace with “rescaling” and “effective-σ rescaling by 1/r” language throughout.

P2-N3 — Units statement for H0
- Location: Eq. (4) (p. 8)
- Text: “we… express H0 in h Mpc−1”
- Problem: Unusual but acceptable; add a parenthetical reminder that H0 = 100 h km s−1 Mpc−1 and c=1 implies H0 has dimensions of inverse comoving distance.
- Required fix: Add a one-sentence clarification to avoid confusion.

P2-N4 — Explicitly state whether r>1 is never used in σeff rescaling
- Location: Sec. III.B, paragraph around Eq. (5) (p. 8)
- Problem: You note r can exceed 1 for some null-space choices. It would help to state that all headline σeff use r in [0.829, 0.876] from physically motivated weighting schemes, not r>1 draws.
- Required fix: Add a one-sentence statement to that effect.

P2-N5 — Trispectrum aside
- Location: Sec. IX.D, end (p. 24)
- Problem: You give a back-of-envelope τNL value. Good to note; consider adding “not used elsewhere in this paper.”
- Required fix: Add the clarifying sentence.

P2-N6 — Reference details check
- Location: Refs. [6], [32]–[38]
- Problem: Ensure final journal names/volume/pages match published versions (several are “arXiv e-prints” or have future-year tags).
- Required fix: Update to final bibliographic details where available at revision.

NITS (cosmetic)

P2-NT1 — Consistent hyphenation and en-dashes
- Location: Throughout
- Problem: Mixed usage of “post-bounce,” “post bounce”; “bispectrum-only,” etc.
- Fix: Standardize hyphenation.

P2-NT2 — Numerical precision
- Location: Multiple
- Problem: Replace excessive significant figures (e.g., 0.0002) with fewer sig figs unless tied to archived code.
- Fix: Round to appropriate precision.

P2-NT3 — Typographical cleanups
- Location: Various
- Problem: Occasional doubled spaces, long em-dash spacing, and mixed italics in variable names.
- Fix: Copyedit pass.

Arithmetic, dimensional, and internal-consistency audit highlights
- r-corrected significance: 4.375×0.84/0.70 = 5.25σ (matches 5.2–5.5σ range for r∈[0.829,0.876]).
- GR-only floor: σeff = sqrt(0.7^2+1.0^2)=1.2207 ⇒ 3.675/1.2207=3.01σ (matches ∼3.0σ).
- “All-combined” (bϕ=1.0, GR=1.0): σeff=1.4142 ⇒ 3.675/1.414=2.60σ (matches ∼2.6σ).
- MegaMapper ideal: r∈[0.84,0.88], σ=0.5 ⇒ 7.35–7.70σ (matches 7.4–7.7σ).
- Planck PR4 recast: σCMB/r = 5.0/0.876 ≈ 5.71; |−4.375+0.11|/5.71 ≈ 0.75σ (as stated).
- BF delta, broad prior: 30/(√(2π)×0.7)=17.1 (as in text); r=0.84 rescale to σeff=0.833 ⇒ 14.36 (as stated).
- BF delta, narrow prior: exact CDF correction raises 5.69 to ≈7.0 (as stated).
- τNL ≈ (36/25)fNL^2 = 27.6 (as stated).
- Dimensional analysis: Eqs. (3)–(4) consistent; M(k,z) dimensionless in stated units.

Abstract-last drift check
The abstract generally reflects the body with the important caveat that “after the systematic budget” can be misread as “all listed systematics applied simultaneously.” See P2-E4: rephrase to an “envelope spanning optimistic to conservative cases.” All other headline scalars trace back correctly.

Stand-alone-reader test
The manuscript is mostly self-contained. However, the following require added detail for a stand-alone reader:
- Exact Fisher weights used to compute r (P2-E6).
- The 3×6 constraint matrix for the SVD (P2-M2).
- A precise competitor definition for BF (P2-E3).
- Redshift bins and biases for the SDB Fisher (P2-M7).

## Summary recommendation
MAJOR REVISIONS

Justification
The paper is careful about its “sensitivity recast” scope and the core numerics check out. However, several methodology/provenance items must be corrected for PRD standards: a real DOI and frozen archive; removal of meta-editorial language; explicit specification of weighting schemes and SDB bins; a clearer, unambiguous definition of the BF competitor/prior; and rewording of the “after systematics” envelope to avoid overstatement. With these addressed and some condensation of implementation detail to Supplementary Material, the manuscript can meet PRD’s rigor and clarity requirements.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

Below are only NEW issues not listed in my first report. I keep the same taxonomy and severity labeling.

ESSENTIAL ISSUES

P2-E10 — Mis-cited equation for σeff quadrature in Table IV caption
- Location: Table IV caption (p. 21)
- Text: “The effective denominator σeff is defined in Sec. IV (Eq. 5) as the quadrature combination…”
- Problem: Eq. (5) defines the template-projection mapping (fmeas = r fbounce and σ(fbounce) = σ(local)/r). The quadrature combination σeff = sqrt(σbase^2 + Σ σi^2) is introduced in Sec. VII (Systematics), not in Eq. (5).
- Required fix: Correct the cross-reference: point to Sec. VII (and the equation where σeff is first defined), and keep Eq. (5) cited only for the r-projection rule.

P2-E11 — Planck PR4 “recast” procedure lacks a precise mapping statement
- Location: Sec. VIII.A (p. 20)
- Text: “Recasting the Planck PR4 constraint with the CMB Fisher template mismatch factor r = 0.876 gives fbounceNL = −0.1 ± 5.7… (recasting the central value as well, −0.1/0.876 = −0.11…)”
- Problem: The mapping from a local-template estimate to a bounce-amplitude estimate should be stated explicitly (f̂bounce ≈ f̂local/r, σbounce ≈ σlocal/r), and a brief justification given (linear estimator response under template overlap). As written, it reads as an ad hoc division of both mean and σ by r.
- Required fix: Add a one-line equation showing the recast (f̂bounce, σbounce) = (f̂local/r, σlocal/r), and state that correlations with other parameters are neglected in this simple recast. This is minor scientifically (numbers are consistent) but should be explicit.

MAJOR ISSUES

P2-M10 — Unsubstantiated novelty claim about the absence of prior overlap quantification
- Location: Sec. III.B (p. 9), cross-check item (iii)
- Text: “a literature search confirming no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024).”
- Problem: This is a novelty claim without citation support (e.g., a review or negative-result survey). PRD typically avoids uncited “we found nothing” assertions.
- Required fix: Either add a supporting citation/review explicitly stating that no such overlap quantification exists, or soften to “we are not aware of a prior quantification…”.

P2-M11 — Inconsistent Monte Carlo realization counts
- Locations: Abstract (p. 1–2), Sec. VI.C (pp. 12–16), Table III note (p. 20)
- Text: Abstract/VI.C: “three independent 10^5-realization ensembles”; Table III note: “2 × 10^5 mock-detection realizations.”
- Problem: The ensemble size varies across the paper without explanation. This invites confusion about which BF numbers use which N.
- Required fix: State clearly where 10^5 vs 2×10^5 are used and why (e.g., separate ensembles for different checks). Make the counts consistent or briefly justify differences in the table footnotes and main text.

P2-M12 — Ambiguity/notation error in Eq. (2) numerator
- Location: Sec. II.A, Eq. (2) (p. 3)
- Text: “BNL = (10/3) Σi AT / Σi k^3i → −35/8…”
- Problem: The numerator appears as a sum over AT, but AT already depends on (k1,k2,k3) and is not an indexed object per-leg. This looks like a stray Σ. The dimensional argument that follows only requires a single AT in the numerator.
- Required fix: Clarify the exact definition; if the intended expression is BNL = (10/3) AT / (k1^3 + k2^3 + k3^3), remove the Σ in the numerator and fix the surrounding prose. If a permutation-average of AT was intended, write it explicitly.

P2-M13 — Figure 4 labeling vs body claim could confuse readers
- Location: Fig. 4 caption (p. 18) and associated text
- Text: Caption emphasizes MegaMapper and SPHEREx SDB curves; the body text states the “SPHEREx bispectrum channel (σ = 0.7, dotted) is less sensitive to the ultra-large-scale fragility.”
- Problem: The figure must unmistakably show which curve is the bispectrum constant-σ reference (and that this line is not part of the SDB curves). As written, a casual reader could conflate SDB and bispectrum channels.
- Required fix: Ensure the legend explicitly includes “SPHEREx bispectrum (σ = 0.7, reference)” and that the caption states this dotted line is a constant-σ reference, not derived from the SDB kmin sweep.

P2-M14 — Orbit-sum combinatorics not fully specified (beyond SVD matrix)
- Location: Sec. II.A (pp. 3–4)
- Text: Definitions of Σi≠j and Σi≠j≠l with ordered tuples and little-group comments.
- Problem: While you explain that the sums run over ordered permutations, the exact combinatorial prefactors per orbit (and how they feed into the polynomial P normalization) remain implicit. Given that basis normalization is central to your null-space claim, these factors should be pinned down numerically somewhere.
- Required fix: In the same appendix that will carry the 3×6 matrix (P2-M2), add a short table listing each monomial orbit, its ordered-term count, and the combinatorial factor used (before/after the in-in doubling). This will fully close the loop on normalization and underdetermination.

P2-M15 — Shot-noise degradation claim for bispectrum lacks a quantitative reference
- Location: Sec. IV, “Shot-noise caveat” paragraph (p. 11)
- Text: “the bispectrum-estimator effective degradation… is the more relevant ∼ 15–30% at z ∼ 1–2…”
- Problem: This figure is plausible but uncited and not derived from your Fisher. Since it’s used to temper the “10–20% improvement” suggestion for anomaly tracers, it should be backed.
- Required fix: Add a citation quantifying bispectrum shot-noise degradation at SPHEREx-like redshifts, or label it as a heuristic estimate and remove the specific 15–30% range.

MINOR ISSUES

P2-N7 — Exponent formatting typos (10^5 appears as “105”)
- Locations: Abstract (p. 1), Sec. VI.C (p. 12), Table II prose (p. 16)
- Problem: “105-realization” reads as 105, not 10^5.
- Required fix: Replace all with 10^5 to avoid ambiguity.

P2-N8 — Define SSFSR on first use
- Location: Table III header and caption (p. 20)
- Problem: “SSFSR” appears before being defined.
- Required fix: Expand to “standard single-field slow-roll (SSFSR)” on first use in the main text or table caption.

P2-N9 — k notation used in multiple roles in Sec. II
- Location: Sec. II.A–B (pp. 3–7)
- Problem: k is used both as the hard-mode scale (k ≡ k2 ≈ k3) and as a generic wavenumber elsewhere. This is understandable but can confuse.
- Required fix: Add a one-sentence reminder when first introducing k ≡ k2 ≈ k3 in Eq. (2) that elsewhere k denotes a generic modulus, and that the special use is local to the squeezed-limit discussion.

P2-N10 — Typo in squeezed-limit description
- Location: Sec. II.A (p. 3)
- Text: “k∑1 ≪ k”
- Problem: Typo; intended “k1 ≪ k.”
- Required fix: Correct the typesetting.

P2-N11 — Clarify the ℓ-space Fisher overlap setup
- Location: Sec. III.B (p. 9)
- Text: “ℓ-space Fisher overlap… r = 0.878 ± 0.012, stable across ℓref = 50–950”
- Problem: The ℓ-range, noise model, and exact weighting for this CMB-style cross-check are not specified (distinct from the LSS-weighting details requested in P2-E6).
- Required fix: Add a one-sentence specification (ℓmin, ℓmax, beam/noise model used) or move details to the Supplement and cite it here.

P2-N12 — Table III “P(BF > 3)” vs main-text ensemble size
- Location: Table III caption vs Sec. VI.C prose
- Problem: Table III uses 2×10^5 realizations; main text centers on 3×10^5 across ensembles. This is fine if explained, but currently readers must infer it.
- Required fix: Add “2×10^5 realizations for this table; other ensembles use 10^5 each” to the caption or a brief parenthetical in Sec. VI.C.

J. (Internal cross-reference/consistency) — already captured by P2-E10 above.

NO other clear arithmetic mismatches were found on re-computation: the numerical checks in my first report still hold. The new items here are primarily cross-reference accuracy, clarity/notation, novelty-claim support, and ensuring figures/captions cannot be misread.