# P2 R22prov — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 NO_NEW
**Wall time**: 224.3s

---

# Referee Report — Paper P2

**Title:** *Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts*

---

## Overall assessment

This paper does not meet the PRD bar. The headline "naturalness" framing collapses under the paper's own bookkeeping; the central observational value quoted in the abstract is mis-attributed; the MCMC posterior actually disfavors the regime the paper claims to live in; the bibliography is broken (every citation renders as `[?]`); and at least two load-bearing scalar quantities (`fphoton × C0 = 1.73 ± 0.44`, `Caγ × θi = 3.4 ± 1.1`) are arithmetically inconsistent with the surrounding numbers and undocumented in their derivation. The author also acknowledges the analysis used AI research assistants, which is fine, but it does not exempt the manuscript from internal consistency.

I list every finding below; nothing is suppressed.

---

## ESSENTIAL findings

### P2-E1 — Bibliography is broken throughout the rendered PDF
**Location:** Every numbered citation in the body (pp. 1, 2, 4, 5, 6).
**Problem:** Every reference renders as `[?]`. Examples: "Planck HFI analysis [?]", "Planck NPIPE [?]", "ACT DR6 [?]", "LiteBIRD [?]", "companion paper [?]", "Namikawa, Murai & Naokawa [?]", "complementary and independent test [?]", "well-studied in the literature [?]". There is no bibliography list at all (the paper ends at the Acknowledgments on p. 7).
**Required fix:** A PRD submission cannot ship without resolved references and a bibliography. Reinstate the bibliography and verify every cited paper, year, arXiv ID, journal, and quoted statistic.

### P2-E2 — Section 5 contains a mathematical error that destroys the naturalness claim
**Location:** Sec. 5, p. 5.
**Quoted text:** *"We adopt option (a) (θ_i ∼ 0.22, with f_a ∼ M_Pl retained for spectator-EFT consistency) as the headline parameter point, in which case the β ∼ 0.27° prediction continues to hold by the cancellation above."*
**Problem:** The cancellation invoked is the *fa* cancellation (Sec. 2.2 / abstract scope note): `β = (gaγ/2) Δϕ` with `gaγ ∝ 1/fa` and `Δϕ ∝ fa · θi · F(m/H0)`, so fa drops out — but θi does **not** drop out. The amplitude scales linearly with θi. Suppressing θi from 1 → 0.22 reduces β by a factor ~4.5 (for a quasi-linear ALP), giving β ≈ 0.06° for the C=8, m=H₀ fiducial — not 0.27°. Recovering 0.27° then requires C ≈ 35, which is not O(1). The entire "no fine-tuning" claim breaks here.
**Required fix:** Either (i) honestly state that the spectator regime requires C_aγ ∼ 35 (and abandon the "natural O(1)" framing), or (ii) abandon the strict Ω_ϕ ≪ 1 spectator framing and admit Ω_ϕ ∼ 0.17 dark-energy-like component (and confront the cosmological-parameter constraints), or (iii) retract the headline naturalness claim.

### P2-E3 — Mis-attribution of the Eskilt et al. value as a "joint Planck + ACT" analysis
**Location:** Abstract, p. 1; Sec. 3.1, p. 2.
**Quoted text:** *"βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis"* and *"the Eskilt et al. joint analysis value βobs = 0.342 ± 0.094°."*
**Problem:** Eskilt's joint analyses (Eskilt 2022; Eskilt & Komatsu 2022) combine **Planck (NPIPE) + WMAP**, not Planck + ACT. The 0.342 ± 0.094° value is the Planck+WMAP joint result. This mis-attribution is not minor: the entire data-combination story in the paper hinges on it.
**Required fix:** Correct the attribution. Then re-examine the double-use of data in Sec. 3.1 (which combines Planck NPIPE and ACT DR6 independently) versus the headline use of a Planck+WMAP value.

### P2-E4 — Internal inconsistency in the fiducial parameter point for β = 0.27°
**Location:** Abstract vs. Sec. 2.2.
**Quoted abstract:** *"f_a ∼ M_Pl and mass m ∼ H₀ … β ≈ 0.27°."*
**Quoted Sec. 2.2:** *"For C_aγ = 8 …, θ_i = 1, m ≈ 2 H₀: the numerical integration gives Δϕ/f_a ≈ 1.07, yielding β ≈ 0.29°."*
**Problem:** The fiducial that achieves β ≈ 0.29° uses **m = 2H₀**, not m ~ H₀. Sec. 2.1 separately states that m = H₀, θ_i = 1 gives Δϕ/f_a ≈ 0.65, which plugged into Eq. (2) with C_aγ = 8 yields β = (α_EM·8/4π) × 0.65 × (180/π) ≈ 0.17°, **not** 0.27°. The abstract's headline number is therefore not the m ~ H₀ prediction.
**Required fix:** Pick one fiducial and propagate it consistently through abstract, Sec. 2.1, Sec. 2.2, Sec. 4, and Sec. 8.

### P2-E5 — The MCMC posterior contradicts the "m ~ H₀" narrative
**Location:** Fig. 1, p. 4 ("log₁₀(m_a/eV) = −31.4 ⁺¹·⁴₋₁·²").
**Problem:** H₀ ≈ 1.43 × 10⁻³³ eV. The MCMC central value m_a ≈ 10⁻³¹·⁴ eV ≈ 4 × 10⁻³² eV gives **m/H₀ ≈ 28**, deep in the oscillating regime, not the slow-rolling "m ~ H₀" regime that frames Secs. 2.1, 2.2, 5, and 8. In the oscillating regime the late-time field amplitude is not given by the slow-roll formulas the paper uses, the energy-density formula in Eq. (11) (the slow-rolling formula) does not apply, and the entire physical picture changes. The paper never reconciles the data-preferred regime with the theoretical regime.
**Required fix:** Either restrict the prior to the regime where the model is defined and re-run, or show that the slow-rolling formulas remain valid at m ≈ 28 H₀ (they don't).

### P2-E6 — "fphoton × C0 = 1.73 ± 0.44" is undocumented
**Location:** Eq. (5), p. 3.
**Problem:** This number is asserted without derivation. It is not the ratio of any combination of β-values that I can reconstruct from the paper's own formulas:
- 0.242°/0.27° = 0.90 — not 1.73
- For C_aγ = 8, θ_i = 1, m = 2H₀ fiducial: β_unit (per unit C_aγ·θ_i) = 0.0356°; then β_obs/β_unit = 6.79 — not 1.73
- For C_aγ = 8, θ_i = 1, m = H₀ fiducial: β_unit ≈ 0.022°; ratio ≈ 11 — not 1.73
**Required fix:** Derive Eq. (5) from displayed equations, or remove it. As written it appears to be a free-floating quantity.

### P2-E7 — Eq. (8) and Fig. 1 marginals are arithmetically inconsistent
**Location:** Eq. (8) (p. 3); Fig. 1 marginals (p. 4).
**Problem:** Fig. 1 shows medians θ_i = 1.33 and C_aγ = 13.4, giving a product 13.4 × 1.33 ≈ 17.8. The text reports `C_aγ × θ_i = 3.4 ± 1.1` (Eq. 8). A factor-of-~5 discrepancy cannot be explained by anti-correlation of the marginals; a non-pathological joint posterior whose median(product) differs from product(medians) by 5× would have to be a sharply curved banana that the contours in Fig. 1 do not show. Either the marginals in Fig. 1 are mislabeled or the product in Eq. (8) is wrong. Worse, the C_aγ × θ_i product is the *single* quantity used to argue the model survives — so this is load-bearing.
**Required fix:** Recompute C_aγ × θ_i directly from the MCMC chain and reconcile with the marginals. Show the joint 2D contour of the product as a 1D posterior.

### P2-E8 — Double counting / inconsistent observational inputs across sections
**Location:** Sec. 3.1 (Eq. 3, p. 3) vs. Sec. 3.3 vs. Abstract.
**Problem:** Sec. 3.1 combines Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°) as if independent, producing β = 0.242 ± 0.061° (3.9σ). Sec. 3.3 instead uses "Eskilt et al." 0.342 ± 0.094° as `βobs`. The abstract leads with **both** the 3.6σ Eskilt value **and** an inferred β = 0.242 ± 0.061° at 3.9σ, treating them as compatible. Recompute: (0.342 − 0.242)/√(0.094² + 0.061²) = 0.89σ — these are formally compatible at ~1σ, but they sit on overlapping data (NPIPE is in Eskilt 2022) and cannot be presented as independent corroboration. Also, the 3.9σ summary likelihood and the 3.6σ Eskilt analysis must not be quoted side-by-side without "not directly comparable" qualifications — the procedures are different.
**Required fix:** Choose a single observational anchor for the headline; explain explicitly whenever a second one is quoted that it shares data.

---

## MAJOR findings

### P2-M1 — MCMC chains are far too short for reported Bayes factor precision
**Location:** Table 1, p. 3; Sec. 3.4, p. 3.
**Problem:** Run 1: 2,160 samples; Run 3: 720 samples. The paper itself concedes "modest by modern standards" and "N_eff ∼ 1,000." Yet it reports ln B = 5.17 with three-digit prior-sensitivity scans (4.48, 5.86). A Savage–Dickey ratio computed from a ~1,000-sample chain has uncertainty in ln B of order ±0.3–0.5 from sampling noise alone; this is not stated.
**Required fix:** Re-run with ≥10⁵ samples, or remove the precise ln B values and replace with order-of-magnitude bands.

### P2-M2 — Spectator condition "25× fine-tuning" terminology is ambiguous
**Location:** Sec. 5, p. 5.
**Quoted:** *"suppressing θ_i to ~ √0.05 θ_nat ≈ 0.22 (a ~25× fine-tuning of the initial misalignment relative to the natural prior midpoint)"*.
**Problem:** θ_i goes from 1 → 0.22, a factor of ~4.5, not 25×. The "25×" is in θ_i², not θ_i. State this explicitly. Also, the paper compares this tuning to a "cosmological-constant-class tuning" — but a 4.5× misalignment tuning is nothing like the ~10¹²⁰× CC tuning, even quoted as θ_i². The rhetorical equivalence is misleading.
**Required fix:** Clarify whether the "25×" refers to amplitude or energy density, and drop the CC analogy or carefully qualify it.

### P2-M3 — "C_aγ = 8 is a natural DFSZ-type value" — but 8 is not O(1)
**Location:** Sec. 2.2, p. 2; abstract.
**Problem:** The abstract sells the model as "C₀ ~ O(1)". The body's fiducial uses C_aγ = 8. The MCMC posterior (Fig. 1) centers on C_aγ = 13.4. An order-unity claim cannot survive central values of 8–13. The "DFSZ-type" justification is a UV-completion choice, not naturalness.
**Required fix:** Be honest: this is an O(10) coefficient, and the "no fine-tuning" claim should be reframed accordingly.

### P2-M4 — Companion-paper dependence on speculative "ECH gravity" / "14-barrier catalog"
**Location:** Sec. 6, p. 5–6.
**Quoted:** *"see the companion paper [?] for the full ECH framework and 14-barrier catalog"*, plus the "Paper I(a)" references in Sec. 5.
**Problem:** A PRD paper cannot lean on a companion paper introducing a non-standard framework that is not yet in the literature without at least citing it with a verifiable preprint identifier (and currently all references are broken — see P2-E1). The "ECH gravity," "Barbero-Immirzi pseudoscalar sector," and "14-barrier catalog" are not standard terminology in cosmology and require either a citation chain to a published paper or explicit acknowledgment that these are part of an unpublished framework.
**Required fix:** Provide arXiv IDs and journal references for the companion papers, or drop these passages.

### P2-M5 — Original contribution is unclear given Fujita et al. (2021) and Namikawa et al.
**Location:** Sec. 7, p. 6.
**Quoted:** *"Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°, and Namikawa, Murai & Naokawa provide superior ALP mass constraints…"*
**Problem:** The paper concedes that the model is well-studied, the β ~ 0.3° result is published, and stronger mass constraints exist elsewhere. The stated novelty — "specific parameter identification (f_a ~ M_Pl, m ~ H₀)" — is exactly the Fujita et al. identification. The "inference framework demonstrating internal consistency" is undercut by the MCMC issues above. The remaining originality is therefore unclear, and this should not occupy 7 PRD pages.
**Required fix:** Sharpen the claimed contribution, or reframe as a Brief Report / Letter, or merge with the companion papers.

### P2-M6 — Abstract overstates LiteBIRD significance
**Location:** Abstract; Sec. 4.
**Problem:** "9σ" comes from 0.27/0.03, where 0.27° is the *theory prediction* with C = 8, θ_i = 1, m = 2H₀ — i.e., one specific point in a stated 0.17°–0.43° natural range. The 9σ claim implicitly assumes that one specific point is the truth. If the true β were 0.17° (also in the natural band), the LiteBIRD significance is ~5.7σ, not 9σ. The abstract should quote the *range* of LiteBIRD significance.
**Required fix:** Replace "9σ" with "~5.7–14σ across the natural-prior band."

### P2-M7 — Eq. (11) ⇒ Ω_ϕ ≈ 0.17 quoted as ~17% but spectator framing requires ≪ 1
**Location:** Eq. (11) and surrounding text, p. 5.
**Problem:** 0.17 is not ≪ 1; it is comparable to Ω_DE × 0.25. Asserting that this is "allowed under ΛCDM at the ~10% level" is too casual; a 17% non-Λ contribution to the present-day energy budget changes the late-time expansion history at the % level and is in tension with cosmological-parameter constraints. The body needs an explicit citation showing this is in fact allowed.
**Required fix:** Show explicitly with current cosmological-parameter constraints (DESI / Planck-2018 + SNe) that an Ω_ϕ ≈ 0.17 ultralight ALP background is allowed.

---

## MINOR findings

### P2-N1 — Figure 2 caption omits the shaded green band identification
**Location:** Fig. 2, p. 5.
**Problem:** The caption identifies three curves but not the green vertical band. Presumably it's β_obs ± 1σ, but state this.

### P2-N2 — "Acknowledges the use of AI research assistants"
**Location:** Acknowledgments, p. 7.
**Problem:** Per PRD policy, AI assistance should be specified (which tools, for what purpose: drafting? numerical analysis? code generation?). A blanket acknowledgment is not sufficient.

### P2-N3 — The 3.6σ/3.9σ values are quoted side-by-side without "not directly comparable"
**Location:** Abstract.
**Problem:** Standard PRD practice requires explicit qualification when two σ values from different null procedures appear together. Here 3.6σ (Eskilt EB-spectrum fit, including dust marginalization) and 3.9σ (Gaussian summary-likelihood combination of NPIPE and ACT point estimates) are presented in the same paragraph. Add a "(not directly comparable due to different likelihood procedures)" tag.

### P2-N4 — Inverse-variance combination of NPIPE + ACT DR6 reproduces only with displayed sigfigs
**Location:** Sec. 3.2, Eq. (4).
**Check:** w₁ = 1/0.11² = 82.6, w₂ = 1/0.074² = 182.6 ⇒ β = (0.30·82.6 + 0.215·182.6)/(82.6+182.6) = 0.2414°, σ = 1/√265.2 = 0.0614°. Matches 0.242 ± 0.061°. OK — this finding is "passes audit."

### P2-N5 — Δϕ/f_a numbers across Sec. 2.1 and 2.2
**Check:** Sec. 2.1: m = H₀, θ_i = 1 ⇒ Δϕ/f_a ≈ 0.65. Sec. 2.2: m = 2H₀, θ_i = 1 ⇒ Δϕ/f_a ≈ 1.07. These are not obviously consistent: a heavier mass should lead to *less* late-time amplitude (it begins oscillating earlier and damps), not more. A larger Δϕ/f_a for m = 2H₀ is suspicious.
**Required fix:** Confirm the numerical integration; if correct, explain the physical mechanism.

### P2-N6 — Sec. 2.1 says rolling starts when H(z) ~ m around z ~ O(1), but for m = 28 H₀ (the MCMC-preferred value), rolling started at H ~ 28 H₀ ⇒ z ~ 9 (radiation/matter era), not z ~ 1
**Location:** Sec. 2.1, p. 2; Fig. 1 (m posterior).
**Problem:** Yet another inconsistency between narrative and data-preferred region. Tied to P2-E5.

### P2-N7 — Quoted significance "3.6σ" for Eskilt is 0.342/0.094 = 3.638 — fine.

### P2-N8 — Sec. 7 calibration-systematics paragraph is good practice but does not propagate into the headline σ values
**Problem:** The paper acknowledges that residual ~0.1–0.3° systematics may exist, then ignores this when quoting 3.9σ. A 0.2° systematic comparable to the signal would not give 3.9σ.

### P2-N9 — The phrase "fphoton × C0" is never defined
**Location:** Eq. (5), p. 3; abstract.
**Problem:** Earlier the paper uses C_aγ, then "C₀", then "f_photon × C₀". These three notations are not unified. What is f_photon? Is it the photon-coupling combination α_EM/4π? Is it 1/f_a in units of M_Pl⁻¹? The reader cannot tell.
**Required fix:** Define f_photon explicitly with units.

---

## Page count

The substantive content (model in Sec. 2 + data combination in Sec. 3) fills <3 pages. Sections 5–6 (spectator condition, ECH motivation) are largely caveats. Given the model's prior existence in the literature (Fujita et al.), this work is at best a Brief Report / Comment, not a full PRD paper. **Recommended maximum: 4 pages as a Comment, or merge into the companion paper.**

---

## Summary recommendation
**REJECT**

The paper contains a fatal mathematical error in the central naturalness argument (P2-E2: θ_i suppression for spectator consistency is *not* a free fa cancellation, but the paper claims it is). It mis-attributes the Eskilt et al. measurement as a Planck+ACT analysis when in fact it is Planck+WMAP (P2-E3). The MCMC posterior on m_a corresponds to m ≈ 28 H₀, contradicting the slow-rolling "m ~ H₀" framing used throughout (P2-E5). The headline-supporting quantities `f_photon × C₀ = 1.73 ± 0.44` and `C_aγ × θ_i = 3.4 ± 1.1` are arithmetically inconsistent with the marginals shown (P2-E7) and undocumented in their derivation (P2-E6). The entire bibliography is missing (P2-E1). Even after these are fixed, the originality bar for a full PRD paper is not met given that Fujita et al. (2021) already published the f_a ~ M_Pl, m ~ H₀ ALP-birefringence identification. The author should fix the technical errors, sharpen the claimed contribution, and resubmit either as a Brief Report or as part of the companion-paper series, with verifiable references and a complete MCMC analysis.