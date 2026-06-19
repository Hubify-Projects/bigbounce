# P2 D2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=4667e9e2 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4365 chars)
**Wall time**: 542.1s

---

Production/visual D2 check (camera-ready confirmation)

- Overall: The previously flagged D1 issues (squished tables, cramped/missing figures, overflows, colorbar/label overlap, dense abstract) appear resolved. Tables span appropriate widths, figures are properly placed with readable captions, no text/equation spill into margins, and float placement is sane with no half-blank pages or orphaned headings that I can see.
- New/remaining visual issues:
  - Page 17 (Fig. 4, both panels): the horizontal axis label shows “kmin [hMpc]”. It should read h Mpc^-1. Please correct units. Same check for any other k-axes (scan shows the right panel also missing “^-1”).
  - Minor legibility: all legends and axis fonts look adequate at print scale; no overlaps detected.

Methodology and rigor review (Physical Review D standards)

I read the full manuscript, audited equations, recomputed the quoted numbers, and checked internal arithmetic. Below are all issues found, categorized by severity.

ESSENTIAL

P2-E1 (Data/code provenance), Data and Code Availability, p. 24
- Problem: “archived at Zenodo (DOI inserted at submission)” is a placeholder. PRD requires a frozen, citable archival DOI. Multiple code artifacts are referenced by filename throughout the paper.
- Required fix: Provide the permanent Zenodo (or equivalent) DOI and a tag/commit hash corresponding exactly to the version used for the results in this paper. State that DOI and hash in the Data and Code Availability section. Ensure the repository contains every artifact named in the text and an environment file sufficient to reproduce the runs.

P2-E2 (Reproducibility of r weighting), Sec. III.B, pp. 8–9 and Eq. (6)
- Problem: The headline template-overlap result r = 0.84 ± 0.02 (and the specific values 0.829, 0.830, 0.835, 0.876) is load‑bearing for every significance quoted, but the “SPHEREx‑like” and “LSS/SDB” Fisher weights are only described qualitatively. The exact weight formula, k-range, triangle weighting, and noise model that define these numbers are not explicitly written in the paper.
- Required fix: Explicitly define each weighting used to compute r in closed form in the manuscript: w(k1,k2,k3), the triangle domain and cuts (kmin,kmax, x3,min), the survey noise model entering w, and any redshift weighting. Add the exact k-range used for the SPHEREx and LSS cases. Provide a one-line pointer to the code function that implements each, but the mathematical definitions must be present in the paper.

P2-E3 (Injection–recovery precision statement), Sec. II (end), p. 5
- Problem: Claim “rmeasured = 0.90 ± 0.01” from 200 Monte Carlo realizations is given only with an SEM-like error bar; the sample standard deviation across realizations is not reported, nor are the estimator details sufficient to verify the ±0.01 precision.
- Required fix: Report both the sample mean and sample standard deviation of the recovered amplitude across the 200 realizations, and explicitly state the estimator form (KSW filter kernels), k/ℓ range, and the exact noise covariance used. If ±0.01 is the SEM, say so and give the SD. Otherwise increase N_MC or relax the precision claim.

P2-E4 (Figure units), Fig. 4, p. 17
- Problem: Axes labeled “kmin [hMpc]” omit the “^-1”. This is a units error.
- Required fix: Change to “kmin [h Mpc^-1]” on both panels of Fig. 4 (and check all other figures for the same omission).

MAJOR

P2-M1 (Systematics combination methodology), Sec. IV, VII, Table IV, pp. 10, 18–20
- Problem: The 2.6–5σ “realistic” headline stacks heterogeneous systematics (GR, bϕ, photo-z) by adding a single σGR in quadrature with σ(fNL) and replacing σ(fNL) under widened bϕ priors. While you flag this as a “transparent scoping choice,” PRD usually expects at least a minimal joint-marginalization demonstration or a sensitivity analysis to the combination rule.
- Required fix: Add a short quantitative sensitivity check comparing the quadrature rule to (i) linear sum and (ii) a small joint Fisher with bϕ priors and a single GR-amplitude nuisance. Report the resulting significance range alongside Table IV to show that your 2.6–5σ envelope is not overly optimistic due to choice of combination rule.

P2-M2 (Photo-z degradation consistency), Sec. VII.D, p. 18
- Problem: The text presents an 0.8% dilution estimate from fcat^2/(1+fcat)^2 (for fcat=0.1) and then states “dominant effect is … ~5%,” without a derivation that bridges from 0.8% to 5%.
- Required fix: Either remove the 0.8% formula here (if not used) or provide a step-by-step derivation of the 5% net Fisher degradation, including the mechanism (cross-bin smearing), assumptions, and a back-of-the-envelope computation to support the 5% figure.

P2-M3 (Heinrich et al. baseline specificity), Sec. IV, p. 10
- Problem: The entire forecast hinges on σ(fNL)=0.7 from Heinrich et al. (bispectrum). The manuscript should summarize the key configuration of that Fisher (redshift bins, k-range, triangle cuts, priors marginalised) so the recast is traceable without opening the paper.
- Required fix: Add a concise paragraph listing the Heinrich et al. inputs relevant to σ(fNL)=0.7 (z-bin edges, k_min/k_max, shot-noise model, nuisance set) and confirm that your recast uses the identical setup.

P2-M4 (CMB Fisher overlap definition), Sec. III.B, p. 9
- Problem: The ℓ-space Fisher overlap r = 0.878 ± 0.012 is quoted without the explicit inner-product definition, ℓ-range, or noise model parameters.
- Required fix: Provide the explicit Fisher overlap integral you use (inner product, covariance), the ℓ-range, and the Planck noise curves assumed. A one-sentence math definition suffices.

P2-M5 (Squeezed-enhanced grid specification), Sec. II, p. 4
- Problem: The “log-weighted squeezed-enhanced grid” changes r by ~0.01, but its precise sampling measure is not defined.
- Required fix: Specify exactly how the squeezed-enhanced sampling is implemented (weight as function of x3 and any normalization), or remove the 0.01 shift claim.

P2-M6 (Dispersed code references in main text), multiple pages
- Problem: Numerous file names and internal artifact paths (e.g., null space analysis.py, c9i epsilon ratio check.json) are scattered through the main text. This hampers readability.
- Required fix: Move all file/path references into the Data and Code Availability section (or an appendix), leaving in-text only brief pointers (e.g., “see repository artifact A1”). Keep the body focused on methods and results.

MINOR

P2-m1 (Axis units), Fig. 5, p. 17
- Problem: Check both panels’ axes. If any k-axis is labeled without “^-1,” fix to h Mpc^-1.
- Required fix: Ensure all k-axes in Fig. 5 (and throughout) have correct units.

P2-m2 (Notation clarity for local-template constant), Appendix A, p. 24
- Problem: The “c” normalization constant discussion mixes Φ- and ζ-field conventions. It is correct but dense.
- Required fix: Add a single-line reminder that the paper’s forecasts and the predicted −35/8 both refer to the ζ-field 6/5 convention to eliminate any lingering ambiguity.

P2-m3 (Hyphenation consistency), throughout
- Problem: “multi-tracer,” “multitracer,” “multi tracer” variants appear.
- Required fix: Standardize to “multi-tracer” throughout.

P2-m4 (Length/editorial)
- Observation: 28 pages is on the long side for a sensitivity recast. The scientific content is substantial, but readability would improve if most internal code-artifact prose moves to the Data/Code section and some repeated caveats are consolidated.

Technical cross-checks and arithmetic audit (selected)

- Abstract ratio |f_bounce|/|f_inf|: 4.375 / 0.015 = 291.7 ≈ 290, OK.
- Template-corrected SPHEREx significance: 4.375/0.7=6.25; times r=0.83→5.19σ, r=0.876→5.48σ. Reported 5.2–5.5σ, OK.
- Conservative GR-only floor: 4.375×0.84 / sqrt(0.7^2+1.0^2) = 3.675/1.220 = 3.01σ, matches ~3.0σ.
- All-combined examples: with σ=0.9 and σGR=1.0 → σeff=1.35; significance = 3.675/1.35 = 2.72σ, OK. With σ=1.0 and σGR=1.0 → σeff=1.41; 3.675/1.41=2.61σ, OK.
- MegaMapper ideal: 4.375×(0.84–0.88)/0.5 = 7.35–7.70σ, OK.
- Planck PR4 recast: σloc=5.0, rCMB=0.876 → σbounce=5.71; distance from bounce |−4.375+0.114|/5.71=0.746σ; from zero 0.114/5.71=0.02σ, OK.
- Bayes factor delta-prior, broad [−15, +15]: B≈W/(√(2π)σ)=30/(2.5066×0.7)=17.1; with r‑rebooking σeff=0.833→14.36; Gaussian bounce prior σtheory=1.0, broad competitor → ~9.80 at r→1 and ~9.2 after rebooking; narrow [−5,+5] competitor and σtheory=1.0 → 4.01. All match text/Table II.
- Joint (fNL, nfNL): σmarg(fNL)=σunmarg/√(1−ρ^2): 1.53/√(1−0.87^2)=3.10 (reported 3.08) and 1.75/√(1−0.969^2)=7.08 (reported 7.06), OK.

Abstract-last drift sweep

- The abstract’s claims (5.2–5.5σ optimistic; 2.6–5σ realistic; Bayes factors ≈ 9 with [−15, +15] competitor; ≈ 4–7 for [−5, +5]) are each backed in the body with explicit calculations and caveats. The “r→1 endpoint” vs “noise-weighted rebooking” distinction is stated in-body and echoed in the abstract. No overclaim detected.
- One editorial improvement: add “(σeff=σ/r bookkeeping)” when quoting the ≈14 delta-prior maximum in the abstract to mirror the precision you use later.

Bibliography spot-check

- Key citations (Maldacena 2003; Planck 2018/PR4; Heinrich et al. 2024; Dalal et al. 2008; Barreira 2022; Addis et al. 2025) appear consistent in year and content with the quoted numbers. No obvious mismatches found.

Standalone-reader test

- The paper is largely self-contained for a recast, but please add the specific Heinrich et al. Fisher setup (P2-M3) and the explicit r-weight definitions (P2-E2); this will make the presentation truly standalone.

Effect sizes

- You consistently report effect sizes as σ-levels and the fractional recovery r; the “1/k^2” scale dependence in Δb is clearly stated. This is adequate.

## Summary recommendation
MAJOR REVISIONS

The paper is careful and internally consistent in its calculations; the numbers I recomputed match the text. However, before PRD acceptance, the authors must (i) fix the missing archival DOI and consolidate reproducibility details, (ii) define precisely the weighting and domains used to compute the crucial template-overlap r, (iii) report fuller statistics for the injection–recovery claim, (iv) correct units on figure axes, and (v) add a brief sensitivity check justifying their quadrature systematics combination. These are achievable but necessary changes to meet PRD’s rigor and reproducibility standards. The D2 production items are largely clean aside from the small units fix.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes pass)

ESSENTIAL

P2-E5 (Definition/dimensions of BNL), Eq. (2), p. 3
- Problem: As written, BNL = (10/3) P/AT / Σi k_i^3. This makes BNL scale as k^3 (since AT ∝ P/k^6), not dimensionless. It also implies a cancellation of P between numerator and AT, contradicting the adjacent text (“no cancellation of P occurs…”).
- Required fix: Correct the definition to the standard, dimensionally consistent form, e.g. BNL(k1,k2,k3) = (10/3) AT(k1,k2,k3)/Σi k_i^3 (or equivalently specify the exact normalization you use that yields a dimensionless quantity), and ensure the surrounding explanation matches. Recheck all places where this BNL is used (including r and rcos computations) to confirm consistency.

P2-E6 (AT prefactor ambiguity), Eq. (1), p. 3
- Problem: AT(k1,k2,k3) = 3 256 k1^2 k2^2 k3^2 P(k1,k2,k3) appears as a product. From the text that follows, AT should be proportional to P/(k1^2 k2^2 k3^2). As written, it increases degree by +6 instead of removing 6.
- Required fix: Add explicit parentheses/fraction bar: AT = (3/256) × P/(k1^2 k2^2 k3^2). Then the dimensional argument given in the paragraph below Eq. (2) is consistent.

P2-E7 (Squeeze-ratio definition inconsistent with ordering), Sec. III.B, p. 8
- Problem: You define x3 ≡ k3/k1 and state “x3 → 0 corresponds to the squeezed limit k3 ≪ k1 ≈ k2.” This conflicts with your earlier triangle ordering k1 ≤ k2 ≤ k3 (Sec. II, p. 4) and with the conventional definition where the long mode is the smallest wavenumber. If k1 is the smallest side, the squeezed limit is k1/k3 → 0, not k3/k1 → 0.
- Required fix: Define a single squeeze ratio consistently throughout, e.g. xL ≡ kL/kS = min(ki)/max(ki), and state clearly which index carries kL in all formulae (including Eq. (2) where k1 is used as the long mode). Update the “squeezed cutoffs” test accordingly.

MAJOR

P2-M7 (Unsubstantiated novelty claim), Sec. III.B, p. 9
- Problem: “A literature search confirming no prior quantification of this overlap exists (2009–2024).” This is a novelty claim without evidence in the manuscript.
- Required fix: Either provide concrete citations showing that comparable bounce–local-template overlap studies do not exist (scope, shapes, methods surveyed), or soften the language to “we are not aware of…” without implying a completed, exhaustive survey.

P2-M8 (Figure intent vs. body text on bϕ sensitivity), Fig. 5 caption vs. §VII.B, pp. 17–18
- Problem: The left panel shows SPHEREx bispectrum σ(fNL) as a horizontal line (red dashed), implying no dependence on bϕ prior width, while the text states that relaxing bϕ universality per tracer bin widens σ(fNL) by O(20–50%).
- Required fix: Clarify in the caption that the red dashed line is the baseline assuming a 20% bϕ prior (or UMF universality). Optionally add a second curve or band showing the expected degradation (30–50%) if bϕ is freely marginalized, to align the figure with the discussion.

MINOR

P2-m5 (Figure-caption precision and units consistency check), multiple figures
- Observation: After fixing the “h Mpc^-1” issue in Fig. 4 (already flagged in your first review), please also verify all remaining k-axes in Fig. 5 and any other figures use “h Mpc^-1” consistently, and that captions explicitly state when a plotted SPHEREx line assumes fixed bϕ prior (see P2-M8).

P2-m6 (Indexing hygiene in text), multiple pages
- Observation: The long/short-mode indexing alternates between using k1 as the long mode (Eq. 2) and k3 as the long mode (x3 definition in Sec. III.B). Even if you correct P2-E7, a brief “indexing convention” note (e.g., we always order k1 ≤ k2 ≤ k3 and take kL = k1) would help prevent reader confusion.

P2-m7 (Typo/notation), Sec. II.A, p. 3
- Problem: In the sentence around Eq. (2), “i k^3_i” appears with a stray “i”. It likely means Σi k_i^3.
- Required fix: Replace by Σi k_i^3 to avoid ambiguity.

Explanation for scope
- These additional issues were not included in the initial review because the pass focused on reproducibility and methodology. A second, equation- and units-focused read revealed two dimension/definition mistakes (E5–E6) and an inconsistent squeeze-ratio definition (E7) that directly affect interpretability and reproducibility of r and BNL-related statements, plus a figure/body mismatch (M8). All previously raised items remain valid and are not repeated here.