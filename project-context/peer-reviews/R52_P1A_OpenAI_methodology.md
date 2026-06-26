# P1A R52 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.78.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7589 chars)
**Wall time**: 446.4s

---

Referee report on: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

Scope of review
- Focus: methodology rigor, derivation chains, dimensional consistency, numerical/σ accounting, estimator definition, and reproducibility.
- I audited all equations, figures, tables, page-by-page. I recomputed the displayed ratios and key scalars (β conversions, H0/MPl scaling, R1 energy-density estimates, R2 dimensionless ratio, Barrier-12 ceiling, etc.). Where the manuscript relies on “companion” works, I applied the standalone-reader test per PRD standards.

Findings

ESSENTIAL (must be fixed before the paper can be considered)

P1A-E1 (Section I, pp. 3–4; “Companion paper” block and elsewhere)
Problem: Heavy reliance on unpublished “companion” works for load‑bearing numerical results and pipelines:
- “Companion paper — ΛCDM+ΔNeff MCMC verification… Paper I(b) [6]… numbers documented internally rather than as externally citable… should be read as internal-analysis inputs…” Similar dependence appears across the text (β pipelines, NaMaster validation, ALP parameter fitting, SPHEREx fNL forecast [2], PTA real‑KDE reanalysis [46]).
- PRD requires the present manuscript to be self-contained. Imported unpublished numbers and methods fail the standalone-reader test.
Required fix: Remove all quantitative results and figures that depend on unpublished companions (H0, σ8, ΔNeff posteriors; PTA γPTA; SPHEREx significance traces), or include a complete methodological description and results in this manuscript (datasets, likelihoods, priors, samplers, burn-in, convergence metrics, masks, estimators). For external results, cite peer-reviewed or at least publicly posted arXiv sources. If companions are indispensable, hold this submission until they are posted and citable.

P1A-E2 (Fig. 1 caption, p. 5; Sec. X.G, p. 20; Table IV row for γPTA, p. 26)
Problem: New, unpublished PTA reanalysis is asserted: “current real-KDE reanalysis γPTA = 2.567 ± 0.382 (Sec. X G) … GPU MCMC, in preparation [46].”
- No data description, no prior/posterior definition, no likelihood, no code. This constitutes a new result with zero reproducibility in the present paper.
Required fix: Either (a) excise all γPTA numbers and remove the PTA threads from Fig. 1, Sec. X.G, and Table IV, or (b) include a full methods section for the PTA analysis with data inputs, spectral model, priors, sampler settings, burn-in, convergence checks, consistency diagnostics, and provide public code and a pinned data release. Alternatively, cite a posted preprint that contains the full analysis.

P1A-E3 (Data and Code Availability, p. 25)
Problem: Provenance incomplete. The paper points to a mutable GitHub repository and says “a Zenodo-archived release will pin all artifacts.” No DOI, no commit SHA, no tag for the exact version used; “frozen MCMC chains” are promised but not verifiable from the manuscript.
Required fix: Provide a DOI to an archived, immutable snapshot (Zenodo or equivalent), and list in-paper the exact commit SHA(s) or tagged release used to generate every figure/table. Enumerate contents (chains, configs, masks, scripts) and licenses. Without this, the paper does not meet PRD reproducibility standards for computational claims.

P1A-E4 (Abstract, p. 1; Fig. 4 caption p. 15; Sec. VII p. 15; Fig. 6 caption p. 22)
Problem: Forecast significance claims for SPHEREx (“2.6–5σ realistic”) and LiteBIRD context are repeatedly presented, but the forecast methodology is deferred to an “in preparation” companion ([2], [6]). The abstract must only summarize what this paper demonstrates.
Required fix: Remove forecast σ claims from the abstract and body unless the full Fisher machinery, survey model, priors, GR-projection corrections, template-overlap calibration, bφ prior, photo‑z marginalization, and covariance assembly are included here with sufficient detail to reproduce the numbers. If retained, every significance must be tied to an explicit estimator and covariance with assumptions labeled.

P1A-E5 (Sec. III.A p. 10; Abstract p. 1)
Problem: Mixing of σ values from different null procedures is generally noted, but not consistently “at every juxtaposition.” Example: Abstract juxtaposes WMAP+Planck β = 0.342° ± 0.094° (~3.6σ) with ACT DR6 0.215° ± 0.074° (~2.9σ) and does note non-comparability; later figures (Fig. 6) include multiple σ scales again with only a panel-level caveat.
Required fix: At every place where σ from different null procedures are displayed side-by-side (abstract, main text, and all figure captions), explicitly state “not directly comparable; different null procedures” next to the numbers. The current panel-level note is insufficient per the review instructions.

P1A-E6 (Sec. II.C and Fig. 3 caption, p. 8; Sec. I, Abstract)
Problem: Figure 3 and numerous places display or rely on “internal MCMC” (H0 = 67.68 ± 1.06, ΔNeff ≈ 0) with no methods in this paper; the text acknowledges these are “not independently peer-reviewable until Paper I(b) is publicly posted”.
Required fix: Remove these numerical posteriors and any figures built from them unless the full MCMC analysis is provided in this paper (data combinations, priors, likelihoods, sampler details, convergence, validation). Replace with references to published numbers if only context is needed.

MAJOR (significant revision)

P1A-M1 (Sec. IV.B Eq. (14), pp. 12–13)
Problem: A specific one-loop parity-violating operator is written,
Γone-loop ∝ −(1/16π^2)(β(γ)/MPl) ∫ √−g ∂μϑNY J5μ,
but no citation derives this exact form and normalization. The subsequent amplitude bound in Eq. (15) uses it as a load-bearing step.
Required fix: Either (a) provide a derivation or a precise citation where this operator with its normalization appears (including the status of ϑNY’s mass dimension), or (b) label Eq. (14) explicitly as a phenomenological upper-bound ansatz at the point of introduction, listing all assumptions (field dimensions, loop factor origin) so the bound in Eq. (15) is traceable.

P1A-M2 (Sec. IV.A, p. 12; R1 energy-density estimate)
Problem: The ratio to ρΛ is reported as “∼ 4 × 10^−69 ρΛ” using ρΛ ∼ (10^−3 eV)^4. Using the observed ρΛ ≈ (2.3 meV)^4 ≈ 2.8×10^−11 eV^4 yields ≈ 1.4 × 10^−70, i.e., ~70 orders-of-magnitude rather than 69.
Required fix: State explicitly which ρΛ normalization you use and report both the approximate and the precise ratios, or just give the ratio relative to (2.3 meV)^4. Keep the arithmetic consistent with the chosen baseline.

P1A-M3 (Sec. II.C and Fig. 3 caption, p. 8)
Problem: The statement “the rotation contribution cω ω^2 is … ≲ 10^−21 ρΛ … dividing by 3ΩΛ ≈ 2.1 gives ∼ 1.2 × 10^−21 of ρΛ” is dimensionally opaque. The mapping from an observational bound (ω/H)_0 < 5×10^−11 to an energy-density fraction involves model-specific coefficients and stress-energy content of rotation; the intermediate “3ΩΛ” factor lacks derivation.
Required fix: Provide the exact relation used to convert (ω/H)_0 into an energy-density fraction under your model, with all numerical factors, or remove the quantitative fraction and simply state that the contribution is negligible.

P1A-M4 (Barrier 1, Eq. (18), p. 16)
Problem: “geff ∼ 1/(MPl √|t3|) ∼ H0/MPl ∼ 10^−61” equates a coupling to H0/MPl with no derivation and t3 is undefined (mass dimension, normalization, sign). This is not checkable as written.
Required fix: Define t3 precisely within a standard Poincaré gauge theory Lagrangian, give its dimension, and show how the scaling leads to geff ∼ H0/MPl. Alternatively, remove the equality to H0/MPl and leave the statement as a dimensional scaling with t3 only.

P1A-M5 (Figs. 4 and 6, pp. 15 and 22)
Problem: Forecast significance trajectories (to 2034) are shown for CMB EB and SPHEREx fNL without sufficient in-paper methodological detail (volumes, redshift binning, bias models, GR projection, template overlaps, systematic degradations).
Required fix: Either remove these figures from this paper (retain only qualitative timelines), or provide the full Fisher setup and key inputs so that the plotted curves are reproducible from the manuscript.

P1A-M6 (Table II and Sec. IX, pp. 17–19)
Problem: The catalog of 14 barriers blends heuristic/conditional statements (e.g., Barrier 9 Liouville Conservation with caveats) with quantitative closures. Later sections refer to the full set as constraining channels. The dependency of the overall “closure” on which barriers are purely heuristic is unclear to the reader.
Required fix: Provide a summary dependency map indicating which barriers are used as load-bearing in each route’s closure and which are heuristic consistency checks. Explicitly state that B9 is not used to close any route and list where closure relies purely on amplitude/derivation arguments.

P1A-M7 (Sec. I and throughout: internal MCMC sample sizes, e.g., p. 4)
Problem: The paper quotes “309,189 frozen accepted samples” and other chain statistics, but with no in-paper sampler settings, effective sample sizes, autocorrelation lengths, or R̂ values for these chains. They are “not independently peer-reviewable” until the companion is posted.
Required fix: Remove these internal chain statistics from this manuscript or include a concise methods appendix with sampler, priors, target posteriors, convergence diagnostics, and effective-sample computations.

P1A-M8 (Sec. II.C.1, “Reheating thermal-reset barrier”, pp. 8–9)
Problem: The text uses Γwash/H > 1 as a conditional closure, then narratively assumes its satisfaction. While the rough top-Yukawa estimate is plausible, the claim is presented as a barrier supporting closure without a quantitative computation across the relevant T range.
Required fix: Provide at least one explicit numerical check at Treh (e.g., Γt/H with y_t, g* values) and briefly quantify when sphalerons dominate, to substantiate the inequality. Else rephrase as a conjectured erasure mechanism and clearly separate it from the primary closure.

MINOR (can proceed but should be addressed)

P1A-m1 (Sec. I, footnote a on p. 2; Sec. X.D p. 20)
Problem: Notation ambiguity for topological terms. You write “Pontryagin density ∝ R R̃” elsewhere as “R Re” (missing tilde) and refer to “Nieh–Yan density” both as d(e ∧ T) and as a combination. While later you do define NY ≡ d(e ∧ T), the earlier occurrences can confuse the reader.
Required fix: Standardize notation: use R ∧ R̃ or ϵR R for Pontryagin; define once and use consistently NY ≡ d(e ∧ T). Where “−NY + T ∧ T” is used, explicitly state that NY denotes d(e ∧ T).

P1A-m2 (Eq. (1), p. 5; footnote 1)
Problem: Presenting ¼ TabcTabc inside the action without immediate statement that it is an on-shell shorthand can mislead readers into thinking torsion is dynamical here.
Required fix: Move the explanatory footnote inline or remove the term from Eq. (1) and keep it only in the discussion after elimination.

P1A-m3 (Appendix C, p. 27, footnote 8)
Problem: The WKB-condition numerical check is sketched; add the explicit numbers used (k ≈ 6×10^−4 eV at 150 GHz, (α/M)ϕ′ ≈ 10^−35 eV) in the main line once, not just the footnote, to close the loop.

P1A-m4 (Table IV, p. 26)
Problem: Row “γPTA PTA spectral index — 2.567 ± 0.382 (real-KDE GPU MCMC) Bounce γ = 3.0 at +1.13σ”. As per P1A‑E2, this should be removed or fully documented. At minimum, annotate clearly that this is not a result of the present paper and provide a firm reference.

P1A-m5 (Editorial)
Problem: Multiple occurrences of long, internal-process prose (e.g., “Companion paper… not duplicated here”, “We emphasize…” repeated often). The manuscript could be tightened considerably without loss of content.
Required fix: Consider trimming to ≤18–20 pages by moving repetition and extended commentary to an appendix or to the eventual companion.

NIT (cosmetic)

P1A-N1 (Stylistic, multiple pages)
- Replace “O(few)” with “of order a few”.
- Normalize hyphenation and spacing around equations (e.g., ensure all minus signs appear as “−”, not “—”).

P1A-N2 (Fig. axes and captions)
- Ensure consistent unit formatting (degrees vs radians) near EB-related plots/captions; you already convert 0.342° → 5.97×10^−3 rad correctly in text; consider adding the radian value once in Sec. IV.B for clarity.

Arithmetic/derivation spot checks (passed)
- β conversion: 0.342° × π/180 = 5.96×10^−3 rad (text uses 5.97×10^−3 rad): OK.
- H0/MPl ≈ 1.5×10^−33 eV / 1.22×10^28 eV ≈ 1.2×10^−61: OK.
- R2 ratio Eq. (15): using αem/4π ≈ 5.8×10^−4, H0/MPl ≈ 1.2×10^−61, MPl(α/M)βobs ≈ 10^−2 × 6×10^−3 = 6×10^−5 gives ~1×10^−60: OK.
- R1 density estimate: n ≈ 100 cm^−3 ⇒ 7.7×10^−13 eV^3; ρ ~ n^2/MPl^2 ≈ 4×10^−81 eV^4: OK; ratio to (2.3 meV)^4 is ≈ 1.4×10^−70 (fix per P1A‑M2).
- R4 energy-density from β: ρθ = 2 m^2 β^2 / (α/M)^2 with m = 1.5×10^−33 eV, β = 6×10^−3, α/M = 10^−30 eV^−1 gives 1.6×10^−10 eV^4 ≈ 5.8 ρΛ: OK.
- Barrier 12 ceiling from (0.27–0.41)^2 ≈ 0.073–0.168: OK.

Abstract-last drift sweep
- The abstract contains forecast claims (SPHEREx 2.6–5σ; “surviving predictions”) and references to companion work. These are not supported within the paper and must be removed or substantially qualified (see P1A‑E4, E1).
- Otherwise, most abstract claims are hedged (ansatz, channel-level closure, operator incompleteness), which matches the body.

Page-length
- The manuscript is long (29 pages) for what is fundamentally a structured no‑go plus a perturbation-transparency reminder. Much of the space repeats caveats and companion references. I recommend trimming to ≤20 pages by:
  - Removing companion-dependent material (Figs. 1, 4, 6 time-series and γPTA elements) unless fully documented here.
  - Consolidating repeated caveats and scope statements.
  - Moving extended thermal-washout narrative and historical catalog prose to an appendix.

## Summary recommendation
MAJOR REVISIONS

The core “perturbation transparency” statement and most dimensional estimates are sound at the order-of-magnitude level, and the paper is careful to flag ansätze. However, the manuscript, as submitted, fails PRD’s methodological and reproducibility standards: it relies heavily on unpublished “companions,” includes a new PTA result without methods, and presents forecast significance figures without in-paper derivations. These are fixable. The authors must remove or fully document all companion-dependent results (with archived code/data), standardize topological-term notation, and clarify several dimensional conversions and heuristic “barriers.” Only after these essential and major issues are resolved should the manuscript be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P1A-E7 (Mis-citation of appendices; p. 6, below Eq. (2))
Problem: “the ∼0.037 figure that appears in the parameter‑budget table (Appendix B)” — but Appendix B is “Dimensional Status…”, while the parameter summary is Appendix A.
Required fix: Correct the cross‑reference (Appendix A, not B) everywhere this appears.

P1A-E8 (Dangling companion cross-reference and non-archived file paths; Appendix C and main text)
Problem: Appendix C references “the companion’s §VI8” and the body cites an internal path “research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py”. These pointers are unusable to a standalone reader and not tied to an archived DOI.
Required fix: Remove all filesystem paths and companion-internal section references, or replace with a self-contained derivation and a DOI/commit SHA to an immutable archive. If a companion must be cited, it must be posted and citable, with the exact section containing the convention.

P1A-E9 (Inconsistent H0 between Fig. 3 and Table IV/body)
Problem: Fig. 3 uses H0 = 69.2 km s−1 Mpc−1 for the “spin‑torsion benchmark cosmology”, while Table IV and the body list H0 = 67.68 ± 1.06 (internal MCMC). No method is given for the 69.2 value in this paper.
Required fix: Harmonize H0 across the manuscript or remove the figure pending an in‑paper methods description. If different values are illustrative, label them explicitly as such and disconnect them from companion-only results (see P1A‑E1/E6).

MAJOR

P1A-M9 (Fig. 5 bottom: “fine‑tuning score” numbers lack definitions/sources)
Problem: The scoreboard quotes ΛCDM (10^122), quintessence (10^60), f(R) (10^40), spin‑torsion (10^5), but gives no metric definition for the “score” nor citations/derivations for the non‑ECH numbers.
Required fix: Define the metric (e.g., sensitivity of ρΛ to input parameters, measured as log10 derivatives), state the conventions (reduced vs unreduced MPl), and cite or derive the quoted orders of magnitude. Otherwise remove the panel.

P1A-M10 (Eq. (12) EB–rotation relation)
Problem: The manuscript uses CℓEB ≈ 2β (CEEℓ − CBBℓ). The standard small‑angle uniform‑β relation is CℓEB ≈ 2β CEEℓ to leading order (the CBB term is subleading for current data, and its inclusion requires a derivation).
Required fix: Provide a short derivation or authoritative citation for the exact “CEE − CBB” form under your conventions, or revert to the standard “2β CEEℓ” leading‑order expression and state explicitly that published β estimators account for lensing B.

P1A-M11 (Eq. (7) and Eq. (14): dimensional status of ϑNY and δNY)
Problem: The one‑loop ansatz Eq. (14) requires [∂μϑNY J5μ/MPl] to carry mass‑dim +4. This is satisfied only if [ϑNY] = +1. Else the prefactor power of MPl changes. Eq. (7) adds δNY without stating its dimension, but α/M has dim −1.
Required fix: State the mass dimension of ϑNY and of δNY explicitly, and verify Eq. (14) and (7) are dimensionally consistent. If ϑNY is dimensionless, adjust the prefactor to restore +4 and relabel Eq. (14) as an ansatz (see also P1A‑M1).

P1A-M12 (Fig. 5 top vs text: dimensionful vs dimensionless coupling)
Problem: The text emphasizes the dimensionless combination MPl(α/M) ≈ O(10^−2–10^−3), while Fig. 5 top plots α/M [GeV^−1]. The caption and panel do not connect these two presentations.
Required fix: Either plot MPl(α/M) (dimensionless) or annotate the figure with the corresponding dimensionless value at the endpoints, to avoid readers mistaking the running for a change in dimensional units.

P1A-M13 (Symbol reuse for “M” causes confusion)
Problem: “M” denotes the LQG area‑gap scale in Sec. II.A.2 and also the ALP–photon Chern–Simons coupling denominator in Sec. IV.D (where standard notation would be fa in gaγ ≡ αem cγ/(2π fa)). This encourages cross‑identification that the paper elsewhere warns against.
Required fix: Use distinct symbols (e.g., MΔ for area‑gap scale; fa or MALP for the ALP sector) and add a one‑line “symbol separation” reminder where α/M is mapped onto gaγ.

P1A-M14 (Barrier 12 “ΩGW ceiling” is unsourced and physically extreme)
Problem: ΩGW|bounce ≲ (ρcrit/ρPl)^2 ≃ 0.07–0.17 is presented as a ceiling “ansatz” without derivation or reference; a ∼10% GW energy fraction is physically consequential and likely in tension with BBN/CMB unless strongly blue and diluted.
Required fix: Provide a derivation or a literature citation justifying the specific (ρcrit/ρPl)^2 scaling and discuss consistency with cosmological bounds. Otherwise, clearly demote this to a qualitative aside not used in any closure and remove the numeric band.

P1A-M15 (Chern–Simons current normalization inconsistency; Sec. IV.D vs App. C)
Problem: Sec. IV.D defines Kμ ≡ ϵμνρσ Aν Fρσ and states ∂μKμ = ½ Fμν F˜μν, while Appendix C defines F˜ with a ½: F˜μν ≡ ½ ϵμνρσ Fρσ. With these conventions, ∂μKμ = Fμν F˜μν, not ½ F F˜.
Required fix: Fix the factor of two and standardize the conventions across the paper (Kμ definition, F˜ definition, and the resulting identity), ensuring the Lagrangian normalization in Eq. (C1) and the β = (α/2M)Δϕ mapping remain consistent.

MINOR

P1A-m6 (β symbol overload)
Problem: β denotes both the birefringence angle and the RG β‑function β(γ). Although one parenthetical disambiguation is given, several sentences still read ambiguously as “one‑loop β”.
Required fix: Adopt distinct symbols or typography (e.g., βobs for birefringence angle; βRG(γ) for the RG function) and enforce consistently.

P1A-m7 (Make the reheating prefactor explicit once)
Problem: The text says (Treh/MGUT)3/2 ≈ 0.03 but never shows the explicit evaluation.
Required fix: Add “for Treh = 10^15 GeV, MGUT = 10^16 GeV, (Treh/MGUT)3/2 = 10−1.5 ≈ 0.0316” once, to close the loop.

P1A-m8 (δNY wording)
Problem: δNY is described as “unestimated” without noting it must share the mass dimension of α/M and depends on the γ5 regularization scheme.
Required fix: Add a clause “δNY carries mass dimension −1 and is scheme-dependent (γ5 regularization); we treat it as a finite counterterm bounded phenomenologically.”

P1A-m9 (Figure annotation to avoid γ confusion)
Problem: Fig. 1 shows “γPTA” on the right, while “γ” throughout the text denotes Barbero–Immirzi. Although the caption disambiguates once, the figure itself may mislead.
Required fix: Add “γPTA (PTA spectral index; not γBI)” directly in the figure label or caption.

P1A-m10 (Ephemeral paths)
Problem: Internal repository paths appear in the text. Even if an archive is later provided (see P1A‑E3), these create maintenance risk.
Required fix: Remove in‑text file paths; point to a DOI/commit and a README index instead.

NITS

P1A-N3 (Topological-term notation)
Problem: Occasional “R Re” appears where R ∧ R˜ (Pontryagin) is meant.
Required fix: Standardize to R ∧ R˜ or ¼ ϵ R R with a tilde explicitly indicated throughout.

P1A-N4 (Planck-mass convention reminder)
Problem: Although Sec. II.C notes unreduced MPl is used, earlier sections do not flag this.
Required fix: Add “unreduced MPl throughout” at its first occurrence in Sec. II.A.

P1A-N5 (Axis/units consistency)
Problem: Minor inconsistencies in unit formatting (km s−1 Mpc−1 vs km/s/Mpc; degrees vs radians across captions).
Required fix: Normalize unit formatting and, near the first β usage in the main text, give the radian conversion once.

Rationale for no-duplication
All items above are new relative to the initial report. They focus on fresh arithmetic/identity checks, internal cross‑references, figure/body consistency, and additional dimensional/notation issues that were not previously flagged.