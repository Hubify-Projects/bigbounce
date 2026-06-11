# P1A R29 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.57.pdf` md5=958587c7 pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7686 chars)
**Wall time**: 297.5s

---

Referee report (PRD methodology review) — Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes …”

Scope of this report
- Focus: methodological rigor, derivation chains, dimensional analysis, internal arithmetic, statistical claims, reproducibility.
- I read all 27 pages, figures, tables, equations, captions, references. I recomputed the displayed ratios and key numbers and checked dimensional consistency where possible.

Overall assessment
The manuscript contains a large amount of careful caveating (ansätze labeled, dimensional caveats stated, limits of scope noted). However, several methodological issues prevent PRD acceptance at this stage:
- The paper is not self-contained; many load-bearing quantitative statements and figures rely on “companion papers in preparation/concurrently posted,” with no reproducible artifacts bundled here.
- The data/code availability does not cover what is actually used in text/tables/figures; the repository tag is out-of-sync with the manuscript version.
- There is visible version-history/log language in the body (explicitly disallowed by PRD style).
- Some key closures (e.g., Route 2) are benchmarked using a coupling fitted in Route 4 rather than an independent bound; this invites circularity. Provide a parameter-independent upper bound.
- Several quantitative robustness claims (washout Γwash > H, “3–5σ realistic” forecasts, RG-running plot) are uncomputed in this paper and lack deposited artifacts.
- Figures 5–6 present quantitative curves not derived or reproducible from this manuscript.

Below I list findings categorized by severity.

ESSENTIAL (must fix before acceptance)
P1A-E1
- Section I (Abstract), p.1; Sec. X G (p.19), Fig. 1 caption (p.5)
- Problem: Load-bearing numbers and claims are imported from “companion papers” rather than established here. Examples:
  - “PTA real-KDE reanalysis γ = 2.567 ± 0.382 (Sec. X G)” relies on Paper III [47].
  - “SPHEREx 3–5σ realistic significance” relies on Paper II [2] with no calculation here.
  - MCMC ΛCDM+ΔNeff posterior values used in Table I, Appendix A, and several places are from Paper I(b) [6] “in preparation,” with no artifacts provided here.
- Required fix: Make the present paper fully stand-alone. Either:
  - Remove all load-bearing uses of results from companion works (PTA γ, MCMC posteriors, SPHEREx forecast curves), or
  - Include, in this paper, the full methodology, parameter settings, priors, samplers, convergence metrics, masks, and exact outputs for each quoted number, and deposit the corresponding chains, codes, and inputs with frozen release tags (DOI or immutable commit hashes). Do not rely on “in preparation” items for claims appearing in this manuscript.

P1A-E2
- Data and Code Availability (p.23)
- Problem: Repository version mismatch and missing artifacts. The paper is v1A.0.57 dated 2026-06-10 (title block), but the repository bundle is labeled v1A.0.56-bundle (resynced 2026-06-10). Moreover, “MCMC chains, NaMaster pipeline, and ALP parameter fitting are documented in companion Paper I(b) [6] and are not duplicated” — yet results from those analyses appear in Table I, Appendix A, Secs. III, VII, XIII, XV.
- Required fix: Synchronize the repository tag to the paper version (v1A.0.57) and include all artifacts for every quantitative result actually used in the paper (chains, configs, covariance matrices, masks, power spectra, figure scripts). Provide immutable commit hashes and expected SHA256 sums for the figures/tables produced here. If these artifacts are to remain in the companion, then delete the dependent results from this paper.

P1A-E3
- Throughout; examples: p.2 footnote a; Sec. X D footnote 5 (p.18–19); Acknowledgments (p.23)
- Problem: Version-history and earlier-draft language present in the scientific text (“Earlier versions of this manuscript erroneously…”, “the correction preserves…”, “supersedes the earlier synthetic-Gaussian…”, “bundle v1A.0.56…resynced 2026-06-10”). PRD style prohibits including versioning/audit-log verbiage in the body.
- Required fix: Remove all version-history commentary from the scientific narrative and footnotes. If a correction is substantive, cite an erratum or state the corrected result cleanly without internal-draft provenance.

P1A-E4
- Sec. IV B Route 2 (p.10–11), Eq. (15)
- Problem: The closure of Route 2 uses the coupling MPl·(α/M) taken from the Route-4-fitted value (leading to MPl·(α/M) ≈ 10−2), i.e., it depends on an external fit that may not be implied by the one-loop Holst/NY physics itself. This creates a circularity risk.
- Required fix: Provide a parameter-independent inequality for Route 2 using only first-principles upper bounds from Eq. (7). For example, adopt the largest plausible g^2, ln(Λ/μ), γ, and M = MPl/√γ to compute a conservative maximum of (α/M)MPl directly from the one-loop expression and redo Eq. (15) entirely from Route-2 premises. Show that the resulting ∆θone-loop/∆θobs is still ≪ 1 (by ≥ 50 orders) without invoking the R4 fit.

P1A-E5
- Figs. 5–6 (pp.15, 21) and related text (Sec. IX; Sec. XIII)
- Problem: Quantitative curves are shown (RG running of α/M vs log10 μ; Detection significance forecast vs year) without any derivation, equations, or data in this paper. Axes lack the defining formulae; no parameter values are given for the running; the SPHEREx forecast is not replicated here.
- Required fix: Either remove these figures from this manuscript or provide the full derivations and inputs (RG equations, initial conditions, stepper, grid, survey specs, redshift-bin assumptions, nuisance priors) and deposit the plotting scripts plus inputs in the repository, with a precise pointer in the caption.

P1A-E6
- Sec. II C 1 “Reheating thermal-reset barrier” (pp.7–8)
- Problem: Strong robustness assertion (“Γwash(Treh) > H(Treh)… expected… then the coherent axial component is thermally reset”) is made without a calculation. The mechanism is then used to bolster the closure narrative. As written, it is qualitative and uses order-of-magnitude hand waves for Γsph, Γy, etc.
- Required fix: Provide at least one explicit numerical estimate at Treh for Γwash/H with actual parameter values (e.g., αW, y_t, Treh, Hreh). Show the inequality is satisfied by concrete numbers, or clearly demote this to a conditional scenario labeled as a hypothesis, not as supporting evidence for closure.

P1A-E7
- Standalone-reader test: multiple places (Table I p.4; Sec. III B p.9; Sec. V p.13; Sec. X G p.19; Appendix A p.24)
- Problem: Key claims about the galaxy spin null (sample sizes, p-values), PTA γ inference, MCMC posteriors, and SPHEREx forecast depend on companion works. A PRD paper must be self-contained.
- Required fix: Either delete those results from this paper or fully include the relevant methods, data, and results (classifier architecture and training, validation metrics, test-time augmentation, masks; PTA likelihood definition; MCMC settings; forecast Fisher matrices) so a reader can reproduce the numbers without any external paper.

P1A-E8
- Abstract (p.1), multiple claims that mix non-equivalent σ references
- Problem: The abstract juxtaposes literature detections at different significance levels (WMAP+Planck ~3.6σ and ACT DR6 ~2.9σ) alongside a forecast (LiteBIRD ~0.03°) and then states a benchmark β≈0.27° as “inside the 1σ band” without an explicit reminder that forecast sigmas are not directly comparable to published ones.
- Required fix: Add an explicit phrase in the abstract clarifying that forecast significances are not directly comparable to present-data significances and that the β≈0.27° benchmark is within current 1σ but is not a prediction of ECH.

MAJOR
P1A-M1
- Sec. IV D (p.12–13), Eq. (17) inversion and overshoot discussion
- Problem: The “natural ALP mass range 10−22–10−15 eV” used to quantify 22–36 OOM overshoot is asserted without citation. The overshoot logic itself is sound, but the “natural range” needs sourcing.
- Required fix: Cite standard references (e.g., ALP parameter-space reviews/constraints) that delimit this range, and clearly state that the overshoot estimate assumes the one-loop-matched α/M; show a sensitivity table or one plot varying α/M and mθ.

P1A-M2
- Sec. II A 1 (p.4), Eq. (1): Action includes +(1/4) TabcTabc with a subsequent note that it is “not independently specified kinetic term and is not varied independently.”
- Problem: Including a torsion-squared piece inside S_ECH while stating it’s not varied is unconventional and confusing (risk of double-counting when also integrating out torsion in Sec. II A 2 / Sec. IV A).
- Required fix: Rewrite the action to the standard EC+Holst+Dirac form with no explicit T^2 term; perform variation once; then show how the four-fermion emerges upon elimination. If you keep Eq. (1), show explicitly (perhaps in an appendix) how the variation avoids double counting and reconcile normalizations.

P1A-M3
- Sec. X B–D (pp.18): Holst decoupling proof
- Problem: The proof is concise and likely correct, but a key identity is stated in words; the mapping eI ∧ eJ ∧ RIJ = −NY + T I ∧ T I is written without a citation and the precise form of NY used.
- Required fix: Add a precise reference (or a short derivation) for the 4-form identity used, with conventions. Explicitly define NY in your conventions so that the T = 0 implication is transparent.

P1A-M4
- Sec. IV E (p.13): “The condensate mechanism yields a vacuum energy that is parametrically too large…”
- Problem: This sentence is not quantified in the paper. Parametrically how large? What channels/parameters were assumed?
- Required fix: Provide a one-line quantitative estimate (with numbers) or remove the claim.

P1A-M5
- Table I (p.4), Appendix A (p.25)
- Problem: The table lists posterior values (H0, σ8, Ωm, ∆Neff) and makes claims about ΛCDM consistency, but all are from a companion chain and not reproducible here. Including these numbers invites confusion since they are labeled as “verified” in Appendix A.
- Required fix: Either drop these from this manuscript or include the full MCMC setup and deposit the chains used. Otherwise, rephrase as “not used in this paper; see companion” and remove any “verified value” label here.

P1A-M6
- Reproducibility of numeric constants and conversions
- Problem: The paper uses several unit conversions (e.g., H0 ≈ 1.5×10−33 eV, 330 cm−3 ≈ 2.5×10−12 eV^3, (α/M) = 10−21 GeV−1 → 10−30 eV−1), but does not provide a short unit-convention block.
- Required fix: Add a brief appendix table with the exact conversion constants used (1 cm = 5.06773×10^4 eV−1, 1 GeV = 10^9 eV, MPl = 1.221×10^19 GeV, etc.) so the reader can reproduce your numeric estimates quickly.

P1A-M7
- Sec. IX “13 logically-independent barriers” (pp.14–17)
- Problem: The logical independence of the 13 barriers is asserted but not demonstrated. B8 is acknowledged as subsumed by B14; for the others, several appear to rely on shared assumptions (minimal matter, Planck suppression, no non-minimal couplings).
- Required fix: Provide a short independence matrix or paragraph for each barrier, explicitly listing the assumptions it uses and why it does not follow from (or imply) the others.

P1A-M8
- Fig. 1 caption (p.5): “PTA annotation reflects … γ = 2.567 ± 0.382 (Sec. X G).”
- Problem: This figure annotates an external analysis in a schematic overview figure. It is not needed for the ECH channel-closure result and depends on a companion analysis.
- Required fix: Remove this annotation from Fig. 1 in this paper or move the PTA discussion entirely to a separate section with methods and data; otherwise, it fails the stand-alone reader test.

MINOR
P1A-m1
- Sec. IV A Eq. (13) (p.10) and the surrounding text
- Observation: The numerical example at recombination (nb ≈ 330 cm−3 → ρNJL ≈ 4×10−80 eV^4) checks out; the ratio to ρΛ ≈ 10−69 is correct. Good. Suggest adding ρΛ ≈ 2.8×10−11 eV^4 explicitly for clarity.

P1A-m2
- Sec. II B Eq. (9) (p.7)
- Comment: The expression ρcrit/ρPl = √3/(32π^2γ^3) reproduces the 0.41 value at γ = 0.2375 and 0.27 at γ = 0.274; a short footnote showing this substitution would help the reader.

P1A-m3
- Sec. III A Eq. (12) (p.9)
- Suggestion: Add a citation or a short derivation line for CℓEB ≈ 2β(CℓEE − CℓBB) and note explicitly that this is the small-angle limit and uniform rotation case (you say it, but a reference would help).

P1A-m4
- Sec. XV “LiteBIRD will detect non-zero β at ~9σ… the relevant discrimination is differential against current central value…” (p.23)
- Comment: This calibrated statement is excellent; consider moving an abbreviated version to the abstract to avoid any impression of “9σ” as a model discrimination statement there.

P1A-m5
- Notation: G vs GN, MPl vs M̄Pl
- Suggestion: Make GN consistently GN (or just G) everywhere and add a one-line note that you use the unreduced MPl.

P1A-m6
- Bibliography consistency
- Minor typos in author names (e.g., “Pop lawski” split across lines) and occasional spacing inconsistencies; fix on proof.

NIT (cosmetic/editorial)
P1A-n1
- PACS numbers on p.2 are not necessary in current PRD style; consider removing.

P1A-n2
- Hyphenation/spacing artifacts (e.g., “Domaga la” split, “Holst/Nieh-Yan” spacing) due to line breaks; clean up.

P1A-n3
- Acknowledgment of AI tool “Claude (Anthropic)” is unusual but not a blocker. If kept, confine to Acknowledgments and ensure no proprietary or non-reproducible steps relied on it.

Technical cross-checks performed (and found consistent)
- Eq. (7) OOM: [(α/M) MPl] ≈ 3×10−3 with g^2 = 4παem, γ = 0.274, ln(Λ/μ) ≈ 74; consistent.
- R2 suppression: ∆θone-loop/∆θobs ∼ αem/(4π) × (H0/MPl) / [MPl(α/M) βobs] ≈ 10−60 using MPl(α/M) ≈ 10−2 and βobs ≈ 6×10−3 rad; consistent.
- R4 inversion: ρθ = 2 m^2 β^2/(α/M)^2 with m = 1.5×10−33 eV, β = 0.006, α/M = 10−21 GeV−1 = 10−30 eV−1 gives ρθ ≈ 1.6×10−10 eV^4 ≈ 6 ρΛ; consistent.
- NJL density estimate: nb(z≈1100) ≈ 330 cm−3 = 2.5×10−12 eV^3; ρNJL ∼ n^2/MPl^2 ≈ 4×10−80 eV^4; ratio to ρΛ ≈ 10−69; consistent.
- ρcrit formula produces 0.41 and 0.27 within cited γ choices; consistent.
- LiteBIRD discrimination computation: |0.342°−0.27°|/√(0.03°)^2+(0.094°)^2 ≈ 0.72–0.73σ; consistent.

Page-length
- The current paper (27 pages) is long relative to its core, which is a channel-level amplitude closure plus the perturbation-transparency statement. With the companion materials removed, this could be reduced to ~18–20 pages by eliminating non-self-contained forecasts/plots and moving lengthy contextual program summaries to an appendix or to the companions.

## Summary recommendation
MAJOR REVISIONS

The core theoretical content (dimensional analysis; the Bianchi-identity-based perturbation transparency; amplitude estimates closing R1–R3; the R4 fine-tuning observation) is promising and mostly sound. However, the manuscript, as submitted, is not self-contained, includes non-reproducible figures/numbers imported from companions “in preparation,” contains version-history prose, and uses a Route-4-fitted coupling to close Route 2 (circularity risk). Address the essential items (self-containedness/reproducibility, removal of versioning language, independent Route-2 bound) and the major items (clarifications, citations, action normalization, independence matrix). Once these are resolved and the figures are either derived in-text or removed, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

The items below are NEW relative to my initial report. I focus on A–J checks you requested.

ESSENTIAL

P1A-E9
- Location: Sec. IV B, Eq. (14), p.10–11
- Issue: Dimensional inconsistency (or undefined conventions). You write Γone-loop ⊃ −(1/16π^2)[β(γ)/MPl] ∫√−g ∂µϑNY J5
µ. With ϑNY called a “pseudoscalar” (dimension not specified), ∂µϑNY has mass dimension +1 if ϑNY is dimensionless, and J5
µ has +3, so the integrand is +4 and needs a dimensionless coefficient. The explicit 1/MPl then lowers it to +3 (inconsistent). This is fixable if ϑNY is a canonical dim-1 field (then ∂ϑNY has dim +2 and the 1/MPl restores +4), but that is not stated. Required fix: Define the mass dimension of ϑNY unambiguously and adjust the prefactor accordingly (or remove 1/MPl if ϑNY is dimensionless), including a brief derivation or citation for this specific operator normalization.

P1A-E10
- Location: Throughout; Fig. 1 caption (p.5), Sec. X G (p.19), Table IV (p.25)
- Issue: Symbol collision for γ. The manuscript uses γ both for the Barbero–Immirzi parameter (γ ≈ 0.274) and the PTA power-law index (γPTA ≈ 2.567). Even with “PTA” qualifiers in places, the reuse is confusing, especially in Fig. 1 which annotates “γ = 2.567 ± 0.382” next to ECH context. Required fix: Change the PTA slope symbol everywhere (e.g., to γPTA or nGW) and update all captions/labels to eliminate ambiguity.

MAJOR

P1A-M9
- Location: Fig. 2 caption (p.6), Sec. XII A (p.19–20), Appendix B (p.24)
- Issue: Inconsistency in the dilution factor Dinf. Fig. 2 says Dinf ∼ 10−121 with Ntot ≈ 92; Appendix B’s “genuine” hierarchy requires Dinf ∼ 10−122 with Ntot ≈ 94. The body text mentions both numbers and calls the ∼2% offset immaterial, but the figure hardcodes 10−121. Required fix: Harmonize the value or annotate the figure caption explicitly that 10−121 (Ntot ≈ 92) comes from the on-shell ansatz (Eq. B2), while 10−122 (Ntot ≈ 94) comes from the true MPl
4/ρΛ hierarchy. As-is, it looks like a stale figure number.

P1A-M10
- Location: Sec. IV D (p.12–13), last paragraph
- Issue: Unsupported statement “The mθ ∼ H0 window where both observables are simultaneously matched has fractional width Δmθ/mθ ∼ 10−1.” No derivation or plot is provided. Required fix: Add a small sensitivity calculation (e.g., linearize β and ρθ about mθ = H0 with the adopted α/M and show the tolerance that keeps both within 1σ or a stated tolerance), or remove the 10% figure.

P1A-M11
- Location: Sec. II A 2 (p.5–6), Eqs. (5)–(6), and Sec. X D (p.18)
- Issue: Curvature notation and mapping. You introduce F IJ[K,˚R] as the gravitational curvature 2-form in Eq. (5) (reserving calligraphic F for curvature and Fµν for electromagnetism later), then switch to Rµνρσ in Sec. X D for the Holst dual. While standard, the reuse of F and R without a one-line summary of the map (F IJ ↔ Rµνρσ via tetrads) makes it hard to follow which symbol is curvature where, particularly because F later denotes the EM field strength. Required fix: Add a crisp notation block stating “gravitational curvature two-form ℛIJ (or Rµνρσ) vs electromagnetic Fµν,” and reconcile Eq. (6)’s “F IJρσ” with Sec. X D’s “Rµνρσ.”

P1A-M12
- Location: Sec. II C 1, “Order-of-magnitude matching” paragraph (p.7–8)
- Issue: Misleading phrasing and unclear origin of (Treh/MGUT)3/2. The text says “the cube of the fermion bilinear scales as the cube of the fermion number density,” which is not standard (J5 is a bilinear; no cube appears naturally here). The additional “parity-odd density-of-states” factor √(Treh/MGUT) is introduced without a calculation or a clear statistical-mechanics argument. Required fix: Remove the “cube of the bilinear” phrasing (use nψ ∝ a−3 only) and either (i) derive (Treh/MGUT)3/2 from a concrete phase-space integral or (ii) clearly label it a phenomenological ansatz with an uncertainty band and show that your main conclusions do not depend on the precise exponent.

P1A-M13
- Location: Sec. II C (p.7), Eq. (10), Fig. 3 caption (p.7)
- Issue: Using cω ω2 as an “isotropic Λeff” contribution is physically only a bookkeeping bound because vorticity sources anisotropic stress. You say this in the text, but then quote a fractional contribution “∼1.2×10−21 of ρΛ” using (ω/H)2/(3ΩΛ). The 3ΩΛ factor is not explained and the mapping from ω to an “effective Λ” is not defined. Required fix: Add one sentence explaining the 3ΩΛ normalization and that you’re only bounding magnitudes, not asserting an isotropic vacuum mapping.

MINOR

P1A-m7
- Location: Multiple places beyond the abstract — Table I (p.4), Sec. XIII (p.21), Fig. 6 (p.21)
- Issue: Additional instances of forecast σ juxtaposed with published σ without an explicit “not directly comparable” caveat (e.g., “3–5σ realistic” SPHEREx forecasts shown next to current CMB β detections). You do this well in the abstract after revision; please also add a brief qualifier in Table I caption and near Fig. 6 that forecasts vs detections are not directly comparable.

P1A-m8
- Location: Sec. XV, last paragraph (p.23)
- Issue: Typographical ambiguity in the LiteBIRD-vs-Planck combination: “|0.342−0.27|/√0.032+0.0942 ≈ …” should read √[(0.03°)2+(0.094°)2]; as written “0.032” can be misread. Please fix the notation.

P1A-m9
- Location: Sec. II C 1, “Reheating thermal-reset barrier” (p.7–8)
- Issue: Sphaleron-rate regime statement is misleading. You write “dominant chirality-flipping process below the EW phase transition,” but the standard result is that sphalerons are unsuppressed in the symmetric phase (above TEW) and exponentially suppressed below TEW. Your inequality Γsph/H ∼ αW
5 MPl/T shows Γsph/H ≫ 1 only for T ≲ O(1011 GeV). At your nominal Treh ≈ 1015 GeV, Γsph/H ≪ 1; the top-Yukawa channel (Γy/H ∼ y2MPl/T ≫ 1) can still drive washout, but the sphaleron clause should be corrected. Please correct the temperature-range statement and keep the explicit numerical estimate (you already give one for Hreh ∼ T2/MPl).

P1A-m10
- Location: Sec. III A, Eq. (12) and surrounding text (p.9)
- Issue: While you note the small-angle and uniform-rotation limit, you do not cite a standard derivation. Add a brief reference (e.g., Lue–Wang–Kamionkowski 1999; or a CMB polarization rotation review) to support Cℓ
EB ≈ 2β(Cℓ
EE − Cℓ
BB).

P1A-m11
- Location: Sec. IV A (p.10)
- Issue: For completeness, add ρΛ ≈ 2.8×10−11 eV4 explicitly when giving the NJL estimate (you already have all ingredients; this helps readers reproduce the ρNJL/ρΛ ratio immediately).

J (stale numbers/notation)

P1A-J1
- Location: Fig. 2 (p.6) vs Appendix B (p.24)
- Issue: As noted in P1A-M9, the Dinf value and corresponding Ntot differ between the figure and the appendix. Either annotate the difference explicitly in the figure caption or update the figure to reflect the “genuine hierarchy” number used in Appendix B.

P1A-J2
- Location: Notation block, entire manuscript
- Issue: In addition to P1A-E10 (γ reuse), the curvature symbol F is used for gravity in Eq. (5) and for electromagnetism elsewhere. You do flag this once, but it is easy to miss. Please include a one-line global notation table early in Sec. II to prevent confusion.

Explanation
I did not repeat issues from my initial report (self-containedness, repository mismatch, circularity in Route-2 closure, figures without derivations, independence matrix, etc.). The new items here arose from a stricter dimensional check of Eq. (14), a consistency scan of dilution factors across figure/appendix, symbol-collision hazards (γ), a closer look at the thermal-washout temperature regimes, and several clarity/notation issues that can cause reader error even if the main results are unaffected.