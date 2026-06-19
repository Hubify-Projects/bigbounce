# P1A D2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=fad68a47 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5985 chars)
**Wall time**: 394.3s

---

Referee report (PRD methodology + D2 camera-ready visual confirmation)

Part A — Camera-ready visuals (D2 confirmation)

- Overall: The PDF is generally clean. The D1 issues (squished tables, cramped/missing figures, text/equation overflow, overlapped colorbars/labels, dense abstract) appear resolved. Tables I/II/IV render full-width and readable; Figs. 1–5,7 are present with legible axes/captions; equations do not intrude into margins; float placement is reasonable; no half-blank pages or orphaned headings detected.

- New visual defects/regressions to fix:
  • Page 1/throughout: Accented characters and diacritics are not rendering properly: “ans¨atze” should be “ansätze”; “G¨odel” should be “Gödel”; “Domaga la–Lewandowski–Meissner” should be “Domagała–Lewandowski–Meissner”; “Pop lawski” should be “Popławski.” These appear multiple times (pp. 1–3, 6, 23, 29). Fix TeX diacritics or ensure correct font encoding.
  • Minor ligature/hyphen artifacts in line-breaks (e.g., contribu￾tion) in the text extraction are likely not present in the PDF; if they are visible in the rendered PDF, reflow to eliminate hyphenation artifacts.

If the above diacritic encoding issues are corrected, the paper is visually camera-ready.

Part B — Methodology and statistical/derivational audit (PRD rigor)

I audited equations, dimensional analysis, arithmetic, and sigma claims. Load-bearing numerics in the abstract and conclusions were recomputed from body text; dimension and unit consistency checked; figure/table content cross-checked.

Findings

ESSENTIAL

P1A-E1 (Abstract + Sec. III, pp. 1, 10–11, 23): Reliance on unpublished “companion” papers for load-bearing claims in the abstract and body
- Problem: The abstract and body cite quantitative results that depend on “Paper I(b) [6] (in preparation)” and other in-prep works (e.g., MCMC chain sizes and posteriors; NaMaster validation; ACT/WMAP processing context; real-KDE PTA reanalysis “Paper III [46]”; SPHEREx forecast “Paper II [2]”). The manuscript claims that these numbers are not used for the closures, but they still appear as quantitative support in abstract/figures/tables (e.g., Table IV, Fig. 4/7 timelines, γPTA = 2.567 ± 0.382, MCMC summary on p. 4).
- Required fix: Remove all quantitative results that depend on unpublished/in-prep companions from the abstract and any section where they are load-bearing OR supply a self-contained appendix/Supplementary with full methods and results sufficient for independent verification (including masks, priors, chains, burn-in, post-processing, goodness-of-fit metrics). For γPTA, either cite a peer-reviewed source with the stated values or drop the number. For SPHEREx forecasts, restrict to Heinrich et al. (2024) with your explicit transformation to “2.6–5σ,” or move your forecast to an appendix with complete methodology. The abstract must not depend on unpublished work.

P1A-E2 (Data and Code Availability, p. 26; Appendix C p. 28): Missing frozen-release DOI and stable artifact pointers
- Problem: The paper promises a Zenodo-archived release “will pin all artifacts” but provides only a GitHub path. Appendix C references an internal path (“research/branch_R_alp_birefringence/.../alp_ode.py”). For PRD reproducibility, a frozen DOI and tag/commit for all artifacts used in this manuscript are required at acceptance.
- Required fix: Provide a permanent DOI (Zenodo or equivalent) with a tagged commit matching the submitted version, list the exact commit hash in the paper, and ensure all analysis scripts, configs (Cobaya YAMLs), and data products referenced in the text and appendices are included. Replace internal path references by stable repository-relative paths and DOI.

MAJOR

P1A-M1 (Route 2 derivation clarity, Sec. IV B, p. 12–13): Dimensionless reduction and coefficient provenance
- Problem: The one-loop induced birefringence estimate (Eq. 15) is presented as an amplitude bound, but the insertion of MPl in the denominator/normalization is not derived from a single consistent effective action. Although you note an “alternative ordering,” the reader needs a clean, single derivation chain to the displayed dimensionless ratio.
- Required fix: Provide a compact, self-contained derivation of Eq. (15) from the stated operator normalization, carrying dimensions throughout, and explicitly showing how the electromagnetic anomaly maps into the angle rotation. Keep the conservative bound but eliminate the “alternative ordering” aside. State assumptions (e.g., ∂μϑNY ∼ H0) in the equation line.

P1A-M2 (SPHEREx forecast claim, Table I, Fig. 4/7, Sec. VII, XIII; pp. 4, 15–16, 23): Forecast-to-significance mapping not shown
- Problem: The 2.6–5σ SPHEREx claim is attributed to “Heinrich+2024 σ(fNL)≈0.7 ideal; degraded to ≈1.0 after systematics” plus your multi-bin/multi-tracer strategy “in preparation.” But the manuscript contains no explicit mapping from σ(fNL) to the stated global detection significance with your systematics model; readers cannot reproduce 2.6–5σ from what is present.
- Required fix: Either (a) remove the 2.6–5σ range from the abstract/figures and confine the statement to “σ(fNL) ≈ 0.7–1.0 (Heinrich+2024) implies |fNL|/σ ≈ 4.4–6.3 (ideal) before systematics” with no further sharpening, or (b) add a short, explicit calculation (one paragraph + equation) showing how GR-projection, bφ uncertainty, and photo-z marginalization degrade σ to your quoted range. Ensure each factor is numerically specified and multiplies/adds correctly.

P1A-M3 (Standalone-reader test, multiple places, pp. 3–5, 10, 15–16, 21–25): Excessive dependence on internal, non-public results and “in preparation” placeholders
- Problem: Key sections repeatedly mention non-public artifacts as if they were established (Paper I(b) MCMC, Paper II Fisher, Paper III PTA, Paper IV galaxy chirality). While you often clarify that these are not used for the closure, the manuscript still mixes them into tables/figures and narrative as quantitative anchors, which fails PRD’s standalone-reader criterion.
- Required fix: Audit the entire text and (i) excise all non-essential “in preparation” quantitative claims from figures/tables/abstract; (ii) where needed for context, restate conservatively using only public sources; (iii) postpone companion-dependent numbers to a short Outlook paragraph without numerics.

MINOR

P1A-m1 (Diacritic/encoding issues, multiple pages incl. p. 1, 3, 6, 23, 29): Visual/typographic correctness
- Problem: Improper rendering of diacritics: “ans¨atze,” “G¨odel,” “Domaga la,” “Pop lawski.”
- Required fix: Correct to “ansätze,” “Gödel,” “Domagała–Lewandowski–Meissner,” “Popławski” (or use ASCII if journal style prefers, consistently).

P1A-m2 (Definition of δNY, Sec. II A 2, Eq. 7, p. 7): Unspecified finite part
- Problem: δNY appears as an “unestimated” finite part with no definition or expected scale.
- Required fix: Add a one-sentence definition (finite renormalization tied to the Nieh–Yan counterterm; scheme-dependent) and an order-of-magnitude expectation or reason why it can be neglected in bounds.

P1A-m3 (Rotation-energy bound arithmetic, Fig. 3 caption, p. 8): Clarify normalization
- Problem: The sentence “(ω/H)0 < 5×10−11 ... dividing by 3ΩΛ ≈ 2.1 gives ∼1.2×10−21 of ρobsΛ)” compresses several steps and constants; the factor “3ΩΛ ≈ 2.1” is unconventional as written.
- Required fix: Rewrite the bound explicitly, e.g., “ρrot/ρΛ ≲ (ω/H)^2/(3ΩΛ) ≲ 2.5×10−21/(3×0.7) ≈ 1.2×10−21,” to make the normalization unambiguous.

P1A-m4 (Barrier 12 ceiling, Eq. 20, p. 19): Add provenance
- Problem: ΩGW ceiling ∼ (ρcrit/ρPl)^2 is introduced as an ansatz without a citation or 1–2 line rationale.
- Required fix: Provide a brief justification or a reference supporting the quadratic scaling as an energy-fraction ceiling, and emphasize it is only used as a global ceiling, not a measurement.

P1A-m5 (Notation collision, γ vs γPTA, multiple pages incl. Fig. 1 caption, pp. 5, 21): Ensure first disambiguation appears at first use
- Problem: You disambiguate γPTA in Fig. 1 caption and later text; ensure the first instance in the main text also states “γPTA denotes the GWB spectral index, distinct from the Barbero–Immirzi parameter γ.”
- Required fix: Add the parenthetical disambiguation at the first main-text mention.

P1A-m6 (Length and focus): 29 pages for a channel-level closure
- Problem: The central technical content (closure via scaling arguments and perturbation transparency) could be presented more concisely.
- Required fix: Consider condensing Sections III–VIII and XIV (discussion/roadmap material) by ~5–7 pages, or move extended programmatic content to an appendix.

NIT

P1A-n1 (Appendix C code path, p. 28): Non-standard citation of internal path
- Problem: The path “research/branch_R_alp_birefringence/...” is too specific to a local repo structure.
- Required fix: Replace with a repository-relative path and DOI/tag, e.g., “See scripts at repo/phase2_mcmc/alp_ode.py (DOI: …, tag vX.Y).”

P1A-n2 (Acknowledgment of AI assistant, p. 26): Journal policy check
- Problem: The acknowledgment of “Claude (Anthropic) as an AI research assistant” may require a policy note.
- Required fix: Confirm PRD policy; if needed, rephrase to “The author used generative AI tools for language editing; all scientific content is the author’s.”

Arithmetic and dimensional spot-checks (passed)

- Eq. (7) one-loop magnitude: (α/M) MPl ≈ 3×10−3 — consistent with g^2 ≈ 0.092, γ ≈ 0.274, ln ≈ 74, M = MPl/√γ. Implies α/M ≈ 2.5×10−22 GeV−1; adoption of 10−21 GeV−1 as a benchmark is within O(×4) and carried as a fit parameter.
- Route 2 ratio, Eq. (15): (αem/4π)×(H0/MPl)/(MPl(α/M)βobs) ≈ 10−60 (using α/M = 10−21 GeV−1, βobs ≈ 6×10−3) — consistent.
- Route 1 density estimate: ρNJL ≈ n^2/MPl^2 with n ≈ 100 cm−3 gives ≈ 4×10−81 eV^4; relative to (10−3 eV)^4 = 10−12 eV^4 this is ≈ 4×10−69 — matches text.
- R4 inversion: ρθ = 2 m^2 β^2/(α/M)^2 with m = H0, β ≈ 6×10−3, α/M = 10−21 GeV−1 (≈ 10−30 eV−1) gives 1.6×10−10 eV^4 ≈ 6 ρΛ for ρΛ ≈ 2.8×10−11 eV^4 — consistent.
- Fig. 3 caption: (Treh/MGUT)3/2 with 1015/1016 → 0.0316 — consistent.

Sigma-comparability hygiene

- The manuscript repeatedly flags non-comparability of σ from different null procedures (abstract, Sec. III A, Fig. 5 caption). No unqualified side-by-side σ claims detected. PASS.

Abstract–body alignment (pattern-045)

- The abstract states the closure is channel-level, not operator-basis; that R1–R3 are amplitude-suppressed under stated ansätze; R4 closes by naturalness; perturbation transparency holds for canonical scalar matter; Ntot ≈ 92 is required by the phenomenological ansatz; fNL and β “surviving” are class-level and not ECH predictions. These are consistent with the body. However, the abstract also includes several companion-dependent numerics (e.g., SPHEREx 2.6–5σ; ACT DR6 β with σ; internal MCMC counts) — see ESSENTIAL P1A-E1.

Bibliography/provenance

- Citations appear accurate; ensure that all 2025–2026 preprints cited for numerical claims are clearly marked as such where used (and avoid relying on them for load-bearing conclusions in this paper).

## Summary recommendation
MAJOR REVISIONS

The physics content is carefully caveated and the arithmetic/dimensional analyses for the headline bounds check out. However, the manuscript currently fails PRD’s standalone-reader and reproducibility standards due to heavy reliance on unpublished companion papers for quantitative claims in the abstract/body, and lacks a frozen DOI for code/data. Addressing the essential items (removing or fully supplying the companion-dependent results; adding a stable DOI; tightening the Route 2 derivation clarity) plus minor diacritic fixes will make the submission suitable for PRD review. The D2 visual presentation is otherwise camera-ready aside from diacritics.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh pass)

ESSENTIAL

P1A-E3 (Operator dimensions, Sec. IV B Eq. 14; cascade into Eq. 15)
- Problem: The one-loop “Nieh–Yan–axial-current” operator is written with an overall 1/MPl: Γ ⊃ −(1/16π^2)[β(γ)/MPl] ∫√−g (∂μϑNY) J5μ. With ϑNY treated as a pseudoscalar (dimensionless in the text), ∂μϑNY has mass dimension +1 and J5μ has +3, so the integrand has dimension +4 already. The extra 1/MPl lowers the Lagrangian density to mass^3, i.e., the action is not dimensionless. This dimensional mismatch undermines the normalization that feeds Eq. (15).
- Required fix: Provide a self-consistent normalization for Eq. (14) with explicit mass dimensions for ϑNY (or absorb MPl into the definition of ϑNY or β(γ)) so that the Lagrangian density is mass^4. Then re-derive Eq. (15) from that consistent action in one clean chain (no “alternative ordering”), carrying units to the final dimensionless ∆θ ratio.

P1A-E4 (Internal cross-reference error: “parameter-budget table (Appendix B)”, p. 6)
- Problem: The text refers to “the parameter-budget table (Appendix B),” but the parameter table is in Appendix A (Table IV). This misdirects readers trying to verify γ’s scheme range and other inputs.
- Required fix: Correct all such references to point to Appendix A/Table IV (and audit the manuscript for any other mis-pointed appendix refs).

MAJOR

P1A-M4 (Fig. 4 “combined significance” curves: no combination rule, inputs, or covariance, pp. 16, 23)
- Problem: The figure shows joint significance curves (“Combined (ρ=0,0.3,0.5)”) but the paper never specifies the per-channel σ inputs, the exact combination formula, nor how ρ is defined/estimated between EB and large-scale structure estimators. This is separate from (and in addition to) your SPHEREx σ(fNL) mapping issue flagged previously.
- Required fix: State the per-channel σ used, define the joint test statistic, and give the explicit formula for the combined significance as a function of ρ (with a sentence on how ρ would be estimated in practice). If you cannot supply this, remove the “combined” curves and keep the single-channel projections only.

P1A-M5 (Fine-tuning scores in Fig. 5 bottom panel lack provenance, p. 18)
- Problem: The bars “quintessence: 10^60” and “f(R): 10^40” appear as quantitative fine-tuning scores with no derivation or citation. They are presented alongside the canonical 10^122 ΛCDM hierarchy and your 10^5 residual, so readers will treat them as quantitative.
- Required fix: Add citations or a 1–2 sentence derivation sketch for these two numbers (what tuning metric, what assumptions), or relabel the panel as “schematic/illustrative” and replace the numeric values with qualitative ordering.

MINOR

P1A-m7 (σ comparability warning missing in Fig. 4, p. 16)
- Problem: The y-axis is “Detection Significance (σ)” for heterogeneous channels (CMB EB vs galaxy bispectrum), plotted together and even “combined.” Unlike elsewhere, the caption does not include your usual “different null procedures — not directly comparable” caveat.
- Required fix: Add the comparability warning to the Fig. 4 caption and text where you discuss joint curves, or remove the joint curves per P1A-M4.

P1A-m8 (Appendix C cites “companion’s §VI8”; non-standalone reference, p. 28)
- Problem: The sentence “the convention block of the companion’s §VI8” is meaningless to a standalone PRD reader.
- Required fix: Remove this pointer or replace it with a self-contained statement of the convention in the present paper (or a public citation). Do not depend on companion section numbering.

P1A-m9 (Eq. 6 epsilon normalization ambiguity; units, p. 7)
- Problem: Seff = ∫ d^4x √−g (α/M) εμνρσ eIμ eJν FIJρσ uses ε with lower indices together with √−g. It is unclear whether ε is the Levi-Civita symbol or tensor-density; this can double-count √−g or introduce a sign error.
- Required fix: State explicitly whether you use the symbol (ϵ̄μνρσ) or tensor (εμνρσ=√−g ϵ̄μνρσ), and adjust Eq. (6) accordingly so the measure and ε are not redundant. Confirm the mass-dimension counting with the clarified choice.

P1A-m10 (“>100 orders” galaxy-spin underprediction claim lacks back-of-envelope, p. 10)
- Problem: You assert the spin-asymmetry amplitude is underpredicted by “>100 orders of magnitude” from α/M ∼ 10^−21 GeV^−1 without showing even a scaling estimate to an observable asymmetry A0.
- Required fix: Add a 1–2 line back-of-envelope showing how the relevant parity-odd operator feeds into a galaxy-scale chirality dipole and the numerical suppression, or rephrase to a qualitative “utterly negligible” without a quantitative “>100 orders” claim.

NIT

P1A-n3 (Ambiguous symbol reuse for H in Eq. 21, p. 20)
- Problem: You do define H ≡ a′/a as the conformal Hubble rate in Eq. (21), but H is used elsewhere as the physical Hubble rate. This is easy to miss.
- Required fix: Consider switching to the standard calligraphic ℋ for the conformal rate in Eq. (21) (or restate more prominently that here H means ℋ).

P1A-n4 (Sign convention for β in Eq. C4, p. 28)
- Problem: You note the sign “matches the WMAP+Planck convention” but give no reference. This is purely a documentation nit.
- Required fix: Cite a standard reference for the β sign convention (e.g., Minami & Komatsu 2020 methods appendix) or show the mapping from helicity basis to Stokes Q/U explicitly in one sentence.

Explanation
The fresh pass focused on unit-carrying derivations, figure/body consistency, and cross-references. The most consequential newly found issue is the mass-dimension inconsistency in the Route-2 one-loop operator (Eq. 14), which needs a clean, unit-consistent normalization and a single derivation path to Eq. (15). Additional gaps concern the unmotivated “combined significance” curves (no combination rule or inputs) and unproven quantitative entries (fine-tuning scores and the “>100 orders” spin underprediction). The appendix and internal cross-references also need cleanup for a standalone PRD submission.