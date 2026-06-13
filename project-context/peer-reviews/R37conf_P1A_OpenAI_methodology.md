# P1A R37conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.68.pdf` md5=0de277bf pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10416 chars)
**Wall time**: 330.1s

---

Referee report for Physical Review D (methodology focus)

Manuscript: “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter” (28 pages)

Overall scope and main claims
- Claims channel-level amplitude closure (under stated assumptions) of four enumerated minimal-ECH dark-energy routes; not an operator-basis theorem.
- Central technical result: perturbation-transparency for canonical scalar matter (Holst sector decouples; Holst dual vanishes identically at T = 0 via the algebraic Bianchi identity).
- R1–R3 amplitude-suppressed; R4 closed by a naturalness objection (mθ ~ H0).
- Provides a catalog of 14 “barriers” (13 logically independent).
- Presents several numerical benchmarks (βobs from WMAP+Planck and ACT DR6; SPHEREx σ(fNL) forecasts) and some internal MCMC outputs hosted in a “companion” (in preparation).

I read the full manuscript line by line, audited every dimensionful relation, recomputed the displayed numerical ratios and uncertainties, and checked the consistency of the abstract and figure captions with the body.

Below are all findings, organized by severity.

ESSENTIAL (must fix before PRD consideration)

P1A-E1. Data/code availability: placeholder DOI and reproducibility incompleteness
- Location: “Data and Code Availability”, p. 25
- Text: “a Zenodo-archived release (DOI to be inserted at submission) will pin all artifacts…”
- Problem: A placeholder (“to be inserted”) appears in the main text. For PRD, the data/code statement must be final at submission. In addition, there is no immutable commit hash/tag for the GitHub bundle, nor a fully specified environment (pinned dependencies, Python version, packages) enabling re-execution of any numbers that are actually used in the paper (even if only for illustration).
- Required fix: Replace the placeholder with a working DOI; add an immutable Git tag/commit hash and an environment specification (requirements.txt/conda-lockfile/dockerfile) that reproduces all artifacts cited in this paper (figures, tables). If some artifacts are produced in the “companion” papers, remove their appearance here or provide a minimal, frozen, self-contained archive adequate for this paper’s claims.

P1A-E2. Version-string/round-tracking language in the manuscript
- Location: Title block, p. 1
- Text: “(Dated: June 13, 2026 PDT — v1A.0.68)”
- Problem: Internal version-string (“v1A.0.68”) is not appropriate for a PRD camera-ready manuscript and violates the journal’s style; it reads as internal bookkeeping (pattern-046).
- Required fix: Remove all version tags (“v1A.0.68”), round-tracking, “posted concurrently”, etc., from the main text. Retain only the date in PRD format.

P1A-E3. Standalone-reader test: load-bearing numbers and methods deferred to “companion” papers in preparation
- Location: Multiple (pp. 2–5, 10, 15–16, 21–23, Table IV)
- Problems:
  - Several numerical claims (e.g., H0 = 67.68 ± 1.06, ∆Neff ≈ 0, the NaMaster pipeline validation, β benchmark fitting, γPTA = 2.567 ± 0.382) are sourced to “companion works in preparation” [2, 6, 46]. 
  - These are presented as inputs or context, but they appear in tables/figures and are not reproducible from this manuscript alone.
- Required fix: Either (i) remove all quantitative results that are not essential to this paper’s argument and that depend on unpublished companions, or (ii) include the minimal, complete methods and results needed to make the statements self-contained here (data cuts, priors, likelihoods, sample sizes, convergence diagnostics, etc.). At a minimum, delete Table IV’s MCMC posterior entries and all text implying verification results if the companion is not yet public.

P1A-E4. Inconsistent cosmological-constant hierarchy (10^120 vs 10^122) and normalization conventions
- Locations: 
  - p. 4 Table I note (“fine-tuning-score” bar for ΛCDM at 10^120),
  - p. 21 Fig. 5 bottom panel shows ΛCDM at 10^120,
  - Appendix B, p. 26: “The genuine cosmological-constant hierarchy is … ~10^122” (explicitly correcting an “earlier draft”).
- Problem: The manuscript alternates between 10^120 and 10^122 for MPl^4/ρΛ. The difference is two orders of magnitude and stems from convention (unreduced vs reduced Planck mass, and the precise ρΛ). The paper must adopt one convention, state it up front, and ensure global consistency in text and figures. The current text simultaneously states both and even references “earlier drafts,” which is out of scope for a polished submission.
- Required fix: Choose a single convention (e.g., unreduced MPl with ρΛ ≈ (2.3 meV)^4 → ~8×10^122) or reduced M̄Pl and stick to it. Update Fig. 5, Table I, Sec. XII A and Appendix B so all fine-tuning scores and sentences reference the same order of magnitude. Remove all “earlier draft” language.

P1A-E5. Sphaleron washout threshold misestimated by ~2 orders of magnitude
- Location: Sec. II C 1, “Reheating thermal-reset barrier”, p. 9
- Text: “electroweak-sphaleron … Γsph ∼ αW^5 T … gives Γsph/H ∼ αW^5 MPl/T ≫ 1 only for T ≲ 10^12 GeV.”
- Problem: Taking αW ~ 1/30 → αW^5 ≈ 3–4×10^−9. Γsph/H ≈ αW^5 MPl/T. Setting Γsph/H = 1 gives T ≈ αW^5 MPl ≈ (3–4)×10^−9 × 1.22×10^19 GeV ≈ (3–5)×10^10 GeV. Thus Γsph/H ≫ 1 for T below ~10^10–10^11 GeV, not 10^12 GeV. The manuscript’s “only for T ≲ 10^12 GeV” overstates the temperature range by roughly 1–2 orders of magnitude.
- Required fix: Correct the threshold estimate to T ≲ few × 10^10 GeV (or present a calculation with the coefficient appropriate to the high-T symmetric-phase rate with the correct prefactor). State clearly that at Treh ~ 10^15 GeV, Γsph/H < 1, but becomes > 1 once T drops below ~10^10–10^11 GeV.

P1A-E6. Notation collision for F in Eq. (6) (gravitational curvature vs electromagnetic field strength)
- Location: Sec. II A 2, Eqs. (5)–(6), p. 7
- Text: “Seff = α/M ∫ eI ∧ eJ ∧ FIJ[K, R̊], … In components … εµνρσ eIµ eJν FIJρσ,” then “The calligraphic F is reserved for this gravitational curvature; the electromagnetic field strength … is written Fµν.”
- Problem: The component Eq. (6) uses F without a calligraphic font, creating an actual collision with the later electromagnetic Fµν (Sec. IV D, Appendix C). This is confusing in a methods paper where operator bookkeeping is central.
- Required fix: Use a distinct symbol consistently (e.g., calligraphic script ℱIJ for curvature two-form throughout and reserve Fµν exclusively for electromagnetism). Update Eqs. (5)–(6) and associated text so the distinction is unambiguous in the rendered PDF (not just described in prose).

P1A-E7. Pattern-048 quantitative support: “definitively erased” fNL claim needs a computable bound
- Location: Abstract (p. 1) and Sec. XIV D (pp. 23–24)
- Text: “definitively erased at SPHEREx-accessible wavenumbers” with heuristic reasoning (Ntot − Nexit ≈ 32, “Ncoh ∼ O(few)”).
- Problem: The paper asserts decisiveness (“definitively erased”) without a quantitative suppression factor or transfer-function bound. While the authors say this is a “consistency check” rather than an additional closure, the phrasing is categorical. Under PRD methodology standards, a quantitative inequality or explicit labeled-ansatz bound is needed for such language.
- Required fix: Replace “definitively erased” with a conditional statement and provide either (i) a minimal quantitative suppression factor (e.g., S < 10^−X for k in [10^−4, 10^−1] h/Mpc given Ntot − Nexit = 32 under an explicit mode-transfer model), or (ii) reword to clearly state this is a qualitative scale-bookkeeping argument pending a future transfer-function calculation.

MAJOR (significant revisions)

P1A-M1. Juxtaposition of σ values from different null procedures needs local caveats whenever side-by-side
- Locations: Abstract (p. 1; good caveat included), Sec. III A (p. 10), Sec. XIII and Fig. 6 (p. 22)
- Problem: The abstract correctly warns that significances from different null procedures are “not directly comparable.” Elsewhere, WMAP+Planck (3.6σ) and ACT DR6 (2.9σ) are listed side-by-side without re-stating the caveat. PRD requires such warnings at every juxtaposition to avoid misinterpretation.
- Required fix: Add a brief parenthetical caveat at each location where the two significances appear adjacently (e.g., “(different null procedures; not directly comparable)”). This is minimal text but necessary for methodological clarity.

P1A-M2. Fig. 3 caption and design: mixed cosmological parameters across curves and “central observable” language
- Location: Fig. 3 and caption, p. 8
- Problem: The ECH curve uses H0 = 69.2, Ωm = 0.310, and an “enhanced radiation density” proxy; the ΛCDM reference uses Planck-VI best-fits (H0 = 67.36, Ωm = 0.315). Then the caption states “The dark-energy mechanism is therefore the Ξ MPl^2 term … the central observable of this paper.” Mixing different baseline cosmologies while calling ΔH/H the “central observable” is methodologically confusing and risks overstating the meaning of the plotted deviation (which partly reflects different baseline parameters rather than an ECH effect per se).
- Required fix: Either plot both curves with the same baseline cosmology to isolate the effect of Ξ (preferred), or make the caption explicitly state that the difference is dominated by distinct baseline parameter choices and that the figure is illustrative only (not used in any inference). Also label axes with units (H(z) in km s^−1 Mpc^−1; redshift z) explicitly in the caption.

P1A-M3. Γsph/H estimate and Treh example need consistent numbers
- Location: Sec. II C 1, p. 9
- Problem: After correcting P1A-E5, ensure the stated Hreh ∼ Treh^2/MPl ∼ 10^11 GeV (for Treh ≈ 10^15 GeV) is consistent with the Γy/H and Γsph/H statements and the subsequent “washout” narrative. As written, Γt/H ≫ 1 at Treh is fine; Γsph/H ≪ 1 at Treh is also fine; but the text suggests both could exceed H at Treh, which is not accurate for sphalerons at 10^15 GeV.
- Required fix: Clarify the temperature regimes: explicitly say that top-Yukawa washout operates already at Treh ∼ 10^15 GeV (Γt/H ≫ 1), while sphaleron processes become dominant only when the plasma cools below ~10^10–10^11 GeV (still in the symmetric phase). This maintains the intended conclusion (thermal reset) without conflating rates at Treh.

P1A-M4. Clarify Eq. (7) numerical choices and the “factor of 2” remark
- Location: Sec. II A 2, Step 4, p. 7
- Text: “…the full Planck-to-TeV logarithm ln(ΛUV^2/µ^2) ≈ 74, the first term used here absorbs the factor of 2…”
- Problem: It is unclear what “absorbs the factor of 2” means (ΛUV^2/µ^2 vs (ΛUV/µ)^2). For methodological clarity, specify the actual values used: ΛUV = MPl, µ = 1 TeV → ln[(MPl/TeV)^2] = 2 ln(10^16) ≈ 73.7. Then show the arithmetic that leads to [(α/M) MPl] ≈ 3×10^−3 with all numerical factors.
- Required fix: Expand the sentence into a one-line calculation so a reader can reproduce the 3×10^−3 value from g^2, γ, ln(Λ/µ), and M = MPl/√γ.

P1A-M5. Notation collision: γ used for Barbero–Immirzi parameter and for PTA spectral index
- Locations: Throughout; explicitly called out in Fig. 1 caption, p. 5; Sec. X G, p. 20
- Problem: Although the paper notes the distinction, using γ for both quantities in the same figures/text is avoidably confusing in a methods paper.
- Required fix: Rename the PTA spectral slope as γPTA → nPTA or κPTA (or another symbol) throughout figures/captions to avoid symbol reuse.

P1A-M6. Reproducibility of internal MCMC numbers included in the text
- Locations: Sec. II (p. 4), Sec. III B (p. 10), Table IV (p. 26)
- Problem: Chain sizes and posterior numbers are quoted but cannot be reproduced from this manuscript (companions are “in preparation”). Even if these numbers are not “load-bearing,” their presence requires either full methods or removal.
- Required fix: Remove the quoted posterior numbers and chain statistics from this paper, or include the necessary details (data sets, likelihoods, priors, nuisance treatment, yml configs, convergence diagnostics) and a static archive enabling re-run. Since the authors assert these values are not used in the closure proof, the simplest resolution is to remove them here and move them fully into the companion when published.

MINOR (address but not blocking)

P1A-m1. EB-based β relation: specify that Eq. (12) is for small, spatially uniform rotation and note modern estimators include lensing B explicitly
- Location: Sec. III A, p. 10
- Fix: Add “valid in the small-angle, spatially uniform limit; modern β estimators include lensing B explicitly (as in [3,4])”.

P1A-m2. Unit conversions and numerical ratios audited (all correct, but document one more step)
- Locations:
  - Sec. IV D, p. 14: ρθ = 2 mθ^2 β^2/(α/M)^2 numerical example → the 6 ρΛ result checks out if α/M = 10^−21 GeV^−1 = 10^−30 eV^−1 is made explicit. 
- Fix: Add the explicit conversion “10^−21 GeV^−1 = 10^−30 eV^−1” inline so the back-of-envelope check is one line.

P1A-m3. Fig. 1, 4, 6 axes and units
- Locations: Figs. 1, 4, 6 (pp. 5, 15, 22)
- Fix: Ensure all axes have units and that all plotted quantities are defined in the captions (e.g., significance units, years on x-axis). If the figures are illustrative only, say so.

P1A-m4. Typos and style
- Locations: Multiple
- Examples: “ans¨atze” (p. 1) → “ansätze”; stray en/em dashes; “Pop lawski” → “Popławski” consistently.
- Fix: Full proofread to correct diacritics and hyphenation.

P1A-m5. Remove internal narrative about “earlier drafts”
- Location: Appendix B, p. 26 (“not the ∼ 35 misstated in earlier drafts”)
- Fix: Delete such meta-references; PRD manuscripts should not discuss draft history.

P1A-m6. Clarify that the EB/TB “achromatic uniform rotation” prediction is not unique to ECH
- Location: Sec. XIII, p. 22–23
- Fix: The text already notes this, but one explicit sentence in Sec. III A would aid standalone readers: “This EB/TB pattern arises in generic ALP models in GR; it is not specific to ECH.”

NIT (cosmetic)

P1A-n1. PACS numbers
- Location: p. 2
- Comment: PACS have been de-emphasized; PRD often prefers keywords. Check journal requirements.

P1A-n2. Footnote markers
- Location: p. 2 and elsewhere
- Comment: Ensure footnote asterisks/letters match PRD style.

P1A-n3. Reference formatting
- Location: Refs. [5], [41]–[45]
- Comment: Some references are listed as “(2025)” or “(2026)” preprints; ensure current arXiv numbers and journal IDs are correct at submission; verify years match titles.

Methodology/statistical checks performed
- Recomputed βobs angle in radians: 0.342° = 5.97×10^−3 rad (matches).
- Recomputed |0.342 − 0.215|/sqrt(0.094^2 + 0.074^2) = 1.06 (matches).
- Verified H0/MPl ~ 1.2×10^−61 (consistent).
- Verified αem/(4π) ≈ 5.8×10^−4 (consistent).
- Verified MPl·(α/M) with α/M = 10^−21 GeV^−1 is 1.22×10^19 × 10^−21 ≈ 1.2×10^−2 (matches).
- Verified NJL mean-field estimate example: ρNJL ≈ 4×10^−81 eV^4; ratio to (10^−3 eV)^4 = 10^−12 eV^4 → 4×10^−69 ρΛ (as stated). Using ρΛ ≈ (2.3 meV)^4 gives ~1.4×10^−70, still consistent with the conclusion.
- Verified LQC ρcrit formula in Eq. (9) and quoted 0.27–0.41 ρPl from γ = 0.274–0.2375 (correct).
- Verified Barrier 12 square window 0.27–0.41 → 0.073–0.168 (correct).
- Checked Appendix C birefringence derivation: the helicity dispersion and factor 1/2 in β mapping are correct at leading WKB order.
- Dimensional consistency checks: Eqs. (1), (3), (4), (10), (14) all pass under the stated conventions. The authors appropriately flag the off-shell dimension +1 issue for Eq. (6) and label it an ansatz.

Length and focus
- The paper is long for its core contribution (no-go plus perturbation-transparency proof). The extensive survey/pedagogy, companion-paper scaffolding, and speculative figures could be trimmed without loss.
- Recommended maximum page count after consolidation: ~18–20 pages (excluding references), if all ESSENTIAL/MAJOR fixes are addressed.

## Summary recommendation
MAJOR REVISIONS

Justification: The central theoretical result (perturbation-transparency via the algebraic Bianchi identity at T = 0) is sound and well presented; the channel-level closures are carefully caveated. However, the manuscript, as submitted, does not meet PRD methodology standards due to (i) unresolved reproducibility (placeholder DOI; reliance on in-prep companions for reported numerical outputs), (ii) internal consistency issues (10^120 vs 10^122 hierarchy) and a concrete quantitative misestimate of the sphaleron washout threshold, (iii) a notational collision, and (iv) several instances where categorical language is used without a quantitative bound. These are all fixable. If the authors address the ESSENTIAL and MAJOR points above, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P1A-E8. Unrealistic post-recombination baryon density used in NJL estimate
- Location: Sec. IV A, paragraph beginning “A naive order-of-magnitude estimate…”
- Issue: Uses nψ ∼ O(10^2) cm−3 as a “post-recombination” mean density. The cosmic mean baryon number density at recombination is ≲ 0.3 cm−3 (today ≈ 2 × 10−7 cm−3 scaled by (1 + zrec)^3 ≈ 1100^3), not 10^2 cm−3. The example overstates nψ by ~2–3 orders of magnitude (and thus ρNJL by ~4–6 orders, since ρ ∝ n^2).
- Required fix: Replace with a physically correct nψ (e.g., ≈ 0.3 cm−3 at recombination or a clearly labeled “dense ISM” example if intended), and specify the redshift/context. Note that the conclusion (negligible vs ρΛ) becomes even stronger numerically; the point is methodological correctness.

P1A-E9. Ambiguous reuse of ρcrit (LQC bounce vs. present-day FRW critical density)
- Locations: Sec. II B (ρcrit as LQC critical density); Sec. IX L (Barrier 12 uses the same ρcrit symbol for LQC); elsewhere the caption of Fig. 3 and text discuss fractions “of ρobsΛ,” including a division by “3ΩΛ ≈ 2.1”.
- Issue: The symbol ρcrit is overloaded in cosmology. In this manuscript it denotes the LQC bounce critical density (Sec. II B), but readers will naturally associate ρcrit with the present-day FRW critical density 3H0^2 MPl^2. This is a high-risk confusion in a methods paper that mixes early-universe and late-time densities.
- Required fix: Rename the LQC quantity everywhere to ρc,LQC (or ρ⋆) and, if needed, denote today’s FRW critical density explicitly as ρc,0 = 3H0^2 MPl^2. Audit every occurrence to ensure unambiguous usage.

P1A-E10. Levi-Civita object in Eq. (6) notationally inconsistent with √−g
- Location: Sec. II A 2, Eq. (6)
- Issue: The integrand uses √−g εμνρσ … The Levi-Civita tensor density vs. symbol distinction matters when √−g appears explicitly. As written, it is unclear whether ε is the antisymmetric symbol (density) or the tensor. This is important in a paper emphasizing operator bookkeeping.
- Required fix: State explicitly whether ε is the symbol or the tensor. If using the symbol, write √−g ϵμνρσ; if the tensor, drop √−g and denote Eμνρσ. Make this convention consistent in all formulas (including Appendices).

MAJOR

P1A-M7. Fig. 5 (top) “RG running of α/M” is not reproducible
- Location: Fig. 5 top panel and caption
- Issue: The plot shows α/M vs. scale with no RGE equation, initial condition, or parameters given. The text does not provide a β-function for α/M, only a one-loop, order-of-magnitude motivation (Eq. 7). As a result, the figure is not reproducible and risks being perceived as decorative rather than methodological.
- Required fix: Either (i) provide the explicit RGE used (d(α/M)/d ln μ with all coefficients) and input values so the curve can be regenerated, or (ii) remove the panel or relabel it clearly as a schematic, not a computed running.

P1A-M8. Dimensional assignment of ϑNY in Eq. (14) is not specified
- Location: Sec. IV B, Eq. (14) and surrounding text
- Issue: Dimensional consistency of S ∝ ∫ (∂μϑNY) J5μ/MPl requires [ϑNY] = +1 (so that [∂ϑNY] = +2). This is not stated. Without a declared normalization for ϑNY, the operator’s mass dimension is ambiguous.
- Required fix: Declare the normalization/dimension of ϑNY explicitly, and confirm that the chosen convention makes Γone-loop dimensionless. If ϑNY is taken dimensionless, adjust the prefactor accordingly (e.g., introduce an extra mass scale) to restore dimensional balance.

P1A-M9. Notational collision: H used for both physical and conformal Hubble rates
- Locations: Sec. X C (Eq. 21 defines H ≡ a′/a as the conformal rate), elsewhere H and H0 denote the usual physical Hubble rate.
- Issue: Using H for both ℋ ≡ a′/a and H ≡ ȧ/a invites confusion, especially in a paper that mixes early- and late-time dynamics. 
- Required fix: Use ℋ for the conformal Hubble rate throughout Eq. (21) and nearby text, and reserve H for the physical Hubble rate (with H0 today).

P1A-M10. Symbol M is overloaded (LQG area-gap scale vs. generic mass scale appearances)
- Locations: Sec. II A 2 (M ≡ Marea-gap), Sec. IV B and IV D (combinations like MPl(α/M)), figure captions
- Issue: M denotes the area-gap mass scale, but combinations like MPl(α/M) are used later without re-stating M’s meaning, which can be misconstrued as “some” mass scale. Given that α/M is central, this ambiguity is problematic.
- Required fix: Rename the area-gap mass to MΔ (or similar) and use it consistently. In all products MPl(α/MΔ), restate that M = MΔ to avoid confusion.

P1A-M11. Rotation-to-Λ mapping in Fig. 3 caption lacks a derivation
- Location: Fig. 3 caption (“dividing by 3ΩΛ ≈ 2.1 gives ∼ 1.2 × 10−21 of ρobsΛ”)
- Issue: The step that maps (ω/H)^2 to a fraction of ρΛ via a division by 3ΩΛ is not explained, and it is not obvious from Einstein’s equations how this mapping is performed for the anisotropic vorticity contribution. In a methods paper, readers must be able to reconstruct the algebra.
- Required fix: Provide a one-line derivation in the caption or nearby text (or move the derivation to an appendix and cite it) that explains the factor 3ΩΛ and the normalization used.

P1A-M12. EB small-angle relation: sign/convention and scope not fully specified
- Location: Sec. III A, Eq. (12)
- Issue: The formula CℓEB ≈ 2β (CEEℓ − CBBℓ) depends on the polarization/rotation conventions. While the small-angle caveat is now requested in P1A-m1, the sign convention and the assumption of no intrinsic parity-odd cosmology (and isotropic β) should be stated explicitly to avoid ambiguity, especially since the manuscript juxtaposes different experiments and pipelines.
- Required fix: Add a sentence stating the rotation and polarization convention adopted and cite a standard derivation that uses this exact convention.

P1A-M13. Mapping β ↔ ρθ assumes a quadratic potential near the minimum
- Location: Sec. IV D (Eq. 17) and Appendix C
- Issue: β ∝ Δϕ ∝ √(2ρθ)/mθ assumes ρθ ≈ ½ mθ^2 ϕ^2 (harmonic approximation) and a coherently displaced, slowly rolling field. The main text uses this mapping for naturalness arguments but only partially states the assumptions.
- Required fix: In the main text where Eq. (17) is used, explicitly state the harmonic approximation (valid for |θ| ≪ 1) and coherent-field assumption, and note how departures (e.g., mθ ≫ H0 oscillatory regime or non-quadratic regions of a cosine potential) would modify the mapping.

P1A-M14. Barrier 12 “vacuum amplification ceiling” lacks methodological support
- Location: Sec. IX L, Eq. (20) and discussion
- Issue: The ceiling ΩECH GW|bounce ≲ (ρc,LQC/ρPl)^2 ≈ 0.07–0.17 is introduced as an “order-of-magnitude ceiling ansatz” without a derivation or citation. Given its size, readers need more than a heuristic proportionality to accept it as a useful bound.
- Required fix: Either (i) provide a short derivation (even schematic) or a suitable literature reference justifying the quadratic scaling and its numerical range, or (ii) clearly label it as a non-binding schematic and remove any interpretive weight it currently carries.

P1A-M15. Action in Eq. (1) mixes in a TabcTabc shorthand; placement risks double-counting confusion
- Location: Sec. II A 1, Eq. (1) and adjacent footnote
- Issue: Including +¼ TabcTabc inside the gravitational bracket with 1/(16πG) and later stating it is an on-shell shorthand (not varied independently) is easy to misread as an independent kinetic term. This is at odds with the “vary EC+Holst+Dirac and integrate out torsion” narrative.
- Required fix: Remove TabcTabc from the displayed “fundamental” action to avoid confusion, and state it only at the point where the four-fermion contact is written after integrating out torsion (or move it to a separate displayed “effective” Lagrangian to distinguish the two levels).

MINOR

P1A-m7. Typographical inconsistency for the Chern–Simons contraction
- Locations: Multiple (e.g., “FFe” vs. “FF˜”)
- Fix: Standardize to Fµν F˜µν throughout.

P1A-m8. Script/file-name in caption
- Location: Fig. 3 caption (“see generate all figures.py”)
- Fix: Remove file names from captions; move this information to the Data/Code Availability section.

P1A-m9. Reference phrasing and years
- Locations: “Planck-VI best-fit” in Fig. 3 caption; refs [5], [41]–[45]
- Fix: Use the canonical “Planck 2018 results. VI…” phrasing, and ensure all arXiv numbers and years are correct and up-to-date at submission.

P1A-m10. Units in reheating estimate
- Location: Sec. II C 1 (“Hreh ∼ Treh^2/MPl ∼ 10^11 GeV”)
- Fix: Add units explicitly and the one-line calculation, e.g., Treh = 10^15 GeV → Hreh ≈ (10^15 GeV)^2/(1.22×10^19 GeV) ≈ 8×10^10 GeV.

P1A-m11. Symbol reuse for “β”
- Location: Sec. IV B (β(γ) as an RG function) vs. β as birefringence angle elsewhere
- Fix: Although you note β(γ) carries an explicit argument, it is still easy to confuse with β the angle. Consider renaming the RG function to b(γ) or βRG to further reduce cognitive load.

P1A-m12. Ωext r proxy
- Location: Fig. 3 caption (“enhanced radiation density Ωext r = Ωstd r (1 + 0.3·7/8·(4/11)4/3)”)
- Fix: Provide a one-line justification or citation for this specific numerical proxy for ∆Neff (or move it to an appendix). As written, it appears ad hoc.

P1A-m13. Cross-figure consistency of fine-tuning exponents
- Location: Fig. 2 (panel text Dinf ∼ 10−121) vs. Appendix B (Ntot ≈ 94 corresponding to ∼ 10−122)
- Fix: After you resolve P1A-E4 globally, ensure these illustrative labels in Fig. 2 are updated to the single chosen convention so readers do not encounter mixed exponents across panels.

P1A-m14. Clarify that “Holst term topological in vacuum” vs. “Bianchi-vanishing at T = 0” is not contradictory
- Location: Sec. IV B first paragraph; Sec. X D
- Fix: Add a bridging sentence noting that e ∧ e ∧ R = −NY + T ∧ T, hence at T = 0 it equals −NY, which in turn is d(e ∧ T) and therefore vanishes pointwise when T = 0; this reconciles the “topological” language with the “Bianchi-vanishing” statement.

NO DUPLICATES
- I did not repeat any items from the initial report. The new findings focus on numerical realism (P1A-E8), symbol/notation clarity (P1A-E9, E10, M8–M11), reproducibility of plots (P1A-M7), explicit assumptions behind key mappings (P1A-M12–M13), and one heuristic bound lacking support (P1A-M14), plus several minor presentation fixes.