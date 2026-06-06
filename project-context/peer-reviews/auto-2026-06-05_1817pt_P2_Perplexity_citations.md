# P2 auto-2026-06-05_1817pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12860 chars)
**Wall time**: 92.7s

---

The manuscript contains multiple serious citation, numerical, and methodological issues that are below PRD standards; several results and references cannot be verified in the current literature record.

Below I list all findings, organized as requested.

---

### ESSENTIAL findings

**P2-E1 – Abstract & throughout – use of future / non‑existent references and data**

- **Location:** Abstract p.1; Sec. 1 p.1; Sec. 3.1 p.2; References p.6.  
- **Problem:** The paper treats several results as established when they are not yet in the literature or are mis‑cited:  
  - “3.6σ isotropic birefringence signal (βobs = 0.342±0.094° from the Eskilt et al. joint Planck + ACT analysis).” There is a real Eskilt & Komatsu PRD paper in 2022 on Planck+WMAP birefringence, not Planck+ACT, and it does not quote 3.6σ with β = 0.342°±0.094°.[1]  
  - Sec. 3.1 cites “ACT DR6 [Diego‑Palazuelos and Komatsu, 2025]” with β = 0.215±0.074° and 2.9σ. No such paper exists as of mid‑2026 in arXiv, ADS or journal databases; the only related work is talks, but not a 2025 arXiv or journal article.[2]  
  - References list “P. Diego‑Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” This preprint cannot be found on arXiv or ADS.[2]  
  - References list “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” The actual paper is “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence” by **Namikawa, Murai, and Fumihiro Naokawa**, arXiv:2506.20824 (2025), published in Phys. Rev. D as 111, 043514 (2025).[1][3][4] The author list, title, and venue are all wrong in the manuscript.  
- **Required fix:**  
  - Remove or clearly mark as *forecast* any numerical results that come from non‑existent or unpublished analyses (e.g., ACT DR6 birefringence measurement, “Eskilt et al. joint Planck + ACT analysis” if not yet a public paper or public likelihood).  
  - Correct the Namikawa et al. reference to the real paper (title, full author list, journal, year, DOI) and ensure that any quoted “superior ALP mass constraints” actually match that paper’s reported results.  
  - If Eskilt & Komatsu Planck+ACT constraints exist only in private communication or internal notes, this must be stated explicitly, and such results cannot be used as a primary load-bearing input for claims of a 3.6σ detection in a PRD paper.

---

**P2-E2 – Sec. 3.2 p.2 – numerical inconsistency in combined β and significance**

- **Location:** Eq. (4), Sec. 3.2 p.2  
- **Text:** “The combined constraint is: βcombined = 0.242 ± 0.061° (3.9σ from zero).”  
- **Problem:** From the two listed inputs in Sec. 3.1:  
  - Planck NPIPE: β₁ = 0.30±0.11°,  
  - ACT DR6: β₂ = 0.215±0.074°,  
  assuming independent Gaussian errors, the inverse-variance weighted mean is:
  \[
  \sigma^2 = (1/0.11^2 + 1/0.074^2)^{-1} \approx 0.0041\ \text{deg}^2 \Rightarrow \sigma \approx 0.064°
  \]
  \[
  \beta_\text{comb} = \sigma^2 \left(\frac{0.30}{0.11^2} + \frac{0.215}{0.074^2}\right) \approx 0.242°
  \]
  So the **mean 0.242° is consistent** with the quoted value, but the 1σ error is ≈0.064°, not 0.061°. The corresponding significance is β/σ ≈ 0.242/0.064 ≈ 3.8σ, not 3.9σ.  
- **Required fix:** Recompute and report βcombined and σ with consistent rounding; if 0.242° is kept, then the error bar should be 0.064° (or 0.06° if rounding) and the significance ≈3.8σ, not 3.9σ. Also make explicit that this is just the combination of two Gaussian point estimates, and not directly comparable to full-spectrum analyses.

---

**P2-E3 – Abstract & Sec. 3 – mixing σ from different procedures without explicit warning**

- **Location:** Abstract p.1; Sec. 1 p.1; Sec. 3.1–3.3 pp.1–3; Fig. 2 p.4; Conclusion p.5.  
- **Text examples:**  
  - Abstract: “βobs = 0.342±0.094° … 3.6σ isotropic birefringence signal” and “We perform a Gaussian summary-likelihood inference … finding β = 0.242 ± 0.061° (3.9σ from zero).”  
  - Sec. 3.3: “βALP = 0.336 ± 0.107° … compared to … βfree = 0.344 ± 0.096° and the observed value βobs = 0.342 ± 0.094°.”  
- **Problem:** The manuscript repeatedly juxtaposes:  
  - a *summary-likelihood* combination of two compressed measurements (Eq. 4),  
  - full-spectrum MCMC results (Eq. 6–7), and  
  - an “observed value” βobs from a different analysis (Eskilt et al. joint analysis),  
  presenting their respective σ-significances side-by-side without an explicit, repeated qualification that these σ values are **not directly comparable** because they come from different likelihoods, data sets, and treatments of systematics. This violates the instruction to explicitly flag such non‑comparability at every juxtaposition.  
- **Required fix:**  
  - Whenever two or more significances from different analysis methods are compared or listed near each other (abstract, Sec. 1, Sec. 3.2–3.3, Fig. 2 caption, Conclusion), add an explicit statement that these σ-values are not directly comparable because they arise from different data/likelihood constructions and priors.  
  - In the abstract, the sentence about “3.6σ isotropic birefringence signal” must be tied explicitly to the specific analysis and clearly separated from the 3.9σ value from the author’s own summary-likelihood inference.

---

**P2-E4 – Sec. 3.4 p.3 – Bayes factor computation underdocumented / potentially inconsistent with chain statistics**

- **Location:** Sec. 3.4 p.3, Eq. (9)  
- **Text:** “ln B = 5.17 … computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°,1°].” Sample sizes listed earlier: Neff ~ 1000.  
- **Problem:**  
  - The paper gives **no quantitative description** of how the posterior density at β = 0 was estimated from MCMC chains with O(10³) effective samples, which is critical for Savage–Dickey ratios.  
  - There is also no cross-check that the Bayes factor implied by the summary-likelihood Gaussian (β=0.242±0.061°) is consistent with ln B ≈ 5.17. For a simple Gaussian model, a 3.8–3.9σ detection typically corresponds to lnB of order 6–7 depending on priors; the quoted values (~4.5–5.9 for differing priors) may be reasonable but the method is under-specified and not reproducible from provided information.  
- **Required fix:**  
  - Provide a precise description of how the posterior density at β = 0 was estimated (binning, kernel density estimate, parametric fit, etc.), and demonstrate robustness of lnB to histogram/binning choices.  
  - Include a simple analytic cross-check (e.g., Gaussian evidence with the same priors) and show numerical agreement within uncertainties.  
  - If this cannot be made quantitatively robust given current chain lengths, the Bayes-factor claims should be downgraded to illustrative and removed from the abstract and main conclusions.

---

**P2-E5 – References p.6 – incorrect / fused metadata for Namikawa et al.**

- **Location:** References p.6  
- **Text:** “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  
- **Problem:**  
  - The real paper is “Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence” by **Toshiya Namikawa, Kai Murai, and Fumihiro Naokawa**, arXiv:2506.20824, Physical Review D 111, 043514 (2025).[1][3][4][6]  
  - The manuscript mis-spells the third author (“Sho Naokawa”), mis-states the title, omits the journal, and marks it “In preparation” despite the work being public and published.  
- **Required fix:** Correct the bibliographic entry to the actual paper (authors, title, arXiv ID, journal, volume, page, year, DOI). Remove the “In preparation” qualifier.

---

**P2-E6 – References p.6 – non‑existent “Diego‑Palazuelos and Komatsu, 2025” preprint**

- **Location:** References p.6  
- **Text:** “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”  
- **Problem:** There is no arXiv preprint or ADS entry with this title and author list as of 2025–2026.[2] Any ACT birefringence results in talks or internal notes cannot be cited as an “arXiv preprint” unless an actual arXiv ID exists.  
- **Required fix:**  
  - Either replace this with a correct, existing ACT paper (with accurate title, authors, arXiv ID, and journal), or explicitly cite talks/ACT collaboration internal results as “private communication” or conference proceedings, *without inventing an arXiv status or year*.  
  - If no public ACT DR6 birefringence paper yet exists, the use of its numerical result in Sec. 3.1–3.2 is not acceptable for a PRD methods paper and should be removed or clearly demoted to a speculative forecast that does not enter the main quantitative claims.

---

**P2-E7 – References p.6 – mischaracterization of Golden (2026a, 2026b) as “companion paper, submitted simultaneously”**

- **Location:** References p.6; Sec. 5 p.4; Sec. 6 p.5  
- **Text:**  
  - “Houston Golden. Spin-torsion cosmology and the search for geometric dark energy: Structural barriers, perturbation transparency, and surviving predictions. Companion paper, submitted simultaneously, 2026a.”  
  - “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”  
- **Problem:** These are unpublished, self‑cited manuscripts without arXiv IDs, DOIs, journal, or accessible status. PRD generally expects that key companion works be at least on arXiv; also the use of “submitted simultaneously” is version-history language.  
- **Required fix:**  
  - Provide arXiv IDs and current status for these works if they exist. If not publicly available, their role in the argument must be strictly limited; e.g., they should not be used to support concrete quantitative claims (such as “fNL = −35/8” being a robust prediction).  
  - Remove “submitted simultaneously” and “companion paper” phrasing; instead, use standard bibliographic description once they are public, or remove them from the reference list if they remain private notes.

---

**P2-E8 – Sec. 6 p.5 – unsupported claim about “matter-bounce non-Gaussianity fNL = −35/8”**

- **Location:** Sec. 6 p.5  
- **Text:** “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”  
- **Problem:** The paper gives no derivation of this number, no error bar, and no reference to an established published source; it depends solely on an unpublished “companion paper” (Golden 2026b). PRD cannot accept such a load-bearing numerical prediction solely on the authority of an unpublished internal manuscript.  
- **Required fix:** Either:  
  - Provide a published or at least arXiv-posted derivation of this value and summarize the key steps/assumptions, or  
  - Rephrase this sentence to something like “A specific matter-bounce model can yield a characteristic non-Gaussianity of order |fNL|∼O(1–10) (see e.g. [X,Y]), providing a conceptually independent test” without quoting a precise numerical value tied only to an unpublished work.

---

**P2-E9 – Abstract vs. body – mismatch between stated σ for LiteBIRD**

- **Location:** Abstract p.1; Sec. 4 p.3; Ref. “LiteBIRD Collaboration, 2023” p.6  
- **Text:**  
  - Abstract: “We forecast that LiteBIRD, with σ(β) ≈ 0.03°, will test this prediction at 9σ significance…”  
  - Sec. 4: “LiteBIRD is projected to achieve σ(β) ≈ 0.03° on the isotropic birefringence angle [LiteBIRD Collaboration, 2023]…”  
- **Problem:** The cited LiteBIRD PTEP 2023 paper does forecast polarization sensitivities but does not, as far as visible in its abstract and summary tables, quote a **direct forecast σ(β) ≈ 0.03°** on isotropic birefringence.[4] Typical forecasts for global polarization-angle calibration in similar literature are of order 0.1° unless special assumptions are made. The author does not show any derivation of 0.03° from LiteBIRD noise and systematics, nor give a reference that explicitly quotes this number.  
- **Required fix:**  
  - Either demonstrate explicitly (with a forecast calculation) how 0.03° is obtained from LiteBIRD’s sensitivity and sky coverage, or quote a **published forecast value** from the LiteBIRD collaboration (with page/section reference) that matches 0.03°.  
  - If such a derivation or citation is not available, relax the claim to a range (e.g. 0.03–0.1°) with appropriate justification, and adjust the quoted 9σ “decisive” significance accordingly.

---

**P2-E10 – Sec. 2.2 p.1 – dimensional and numerical inconsistency in β prediction**

- **Location:** Sec. 2.2 p.1, Eq. (2) and following paragraph.  
- **Text:**  
  - Equation (2): “β = gaγ ∆ϕ / 2 = C0 ∆ϕ / (2fa)” which is dimensionally correct.  
  - Then: “For C0 ∼ 1, θi ∼ 1: the cosmological field evolution gives ∆ϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.”  
- **Problem:** If ∆ϕ/fa ∼ 10⁻² and C₀ θᵢ ∼ 1, then
  \[
  β = \frac{C_0}{2} \frac{Δϕ}{f_a} \sim \frac{1}{2}\times10^{-2} = 5\times10^{-3}\ \text{rad} \approx 0.29°,
  \]
  which matches the text’s 5×10⁻³ rad and ≈0.27° but contradicts Eq. (2) as written where β = (C0/2) Δϕ; the intermediate phrase “β ≈ C0 θi × 5 × 10−3 rad” omits the 1/2 factor and replaces Δϕ/fa by “5×10⁻³” itself. The logic is muddled: either Δϕ/fa ≈ 10⁻² and β ≈ (C0/2)θi×10⁻² rad, or β ≈ C0 θi×5×10⁻³ rad; both cannot simultaneously be the *definition* of Δϕ/fa.  
- **Required fix:** Rewrite this paragraph carefully:  
  - Explicitly state the numerical estimate used for Δϕ/fa from the cosmological integration (e.g. 1.0×10⁻²), then show the conversion to β with the 1/2 factor included.  
  - Avoid mixing dimensionless ratios and angle values in radians in the same symbolic factor “5×10⁻³ rad”.

---

**P2-E11 – Abstract & Sec. 3 – “Bayes factor ln B = 5.17” used as headline claim without robust support**

- **Location:** Abstract p.1; Sec. 3.4 p.3  
- **Text:** “The Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).”  
- **Problem:** Given that:  
  - The chain lengths are modest (Neff ~ 10³) and the author already admits “limit the precision of tail estimates and evidence calculations.”  
  - No robustness checks or alternative evidence estimators are presented.  
  - The combination of data itself is based on at least one non-public or mis‑cited measurement (ACT DR6).  
  Using ln B = 5.17 as an abstract-level headline for “evidence” is not justified by the methods described.  
- **Required fix:**  
  - Remove the Bayes-factor value from the abstract, or clearly demote it to a secondary, illustrative check, emphasized as not robust and strongly prior- and method-dependent.  
  - Provide at least one robustness test (e.g. repeating with different chains, or using effective analytic approximations) if a Bayes factor is to be retained in the main text.

---

### MAJOR findings

**P2-M1 – Sec. 3.1 & References – Planck and ACT values partially inconsistent with literature and poorly documented**

- **Location:** Sec. 1 p.1; Sec. 3.1 p.2; References p.6.  
- **Text:**  
  - “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11° (2.7σ).”  
  - “An earlier Planck HFI analysis [Minami and Komatsu, 2020] reported β = 0.35 ± 0.14° (2.5σ).”  
- **Problem:**  
  - Minami & Komatsu (2020) indeed report β ≈ 0.35±0.14° (2.4–2.5σ) in PRL 125, 221301.[7] That is correctly cited.  
  - Eskilt & Komatsu (PRD 106, 063503, 2022) perform an improved birefringence analysis using Planck and WMAP and obtain values around β ≈ 0.30° with smaller error; the exact quoted numbers must be checked against their abstract and tables. Their central value and σ in the manuscript (0.30±0.11°) appear plausible but the paper doesn’t specify which exact data combination (e.g. with WMAP, Planck NPIPE only, etc.).[1]  
  - The reference is listed simply as “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data. Physical Review D, 106:063503, 2022.” which is correct; but the text calling this specifically “Planck NPIPE” is somewhat misleading, as the real analysis is more complex.  
- **Required fix:**  
  - Clarify which exact Eskilt & Komatsu measurement is used (e.g. “WMAP+Planck EB-based method, Main Result X in Table Y”).  
  - Check that the quoted 0.30±0.11° matches a specific entry in that paper; if the value was approximated, adjust to exactly match their reported numbers and clearly label any approximation.

---

**P2-M2 – Sec. 3.3 p.2 – underspecified priors and parameterization (Caγ vs C0)**

- **Location:** Sec. 3.3 p.2; Eq. (8).  
- **Text:** Priors: “Caγ flat on [1, 30] (Run 2 only).” Eq. (8): “Caγ × θi = 3.4 ± 1.1”  
- **Problem:** The earlier text introduces the anomaly coefficient as **C0** (Eq. 2, abstract) and the ALP–photon coupling as gaγ = C0/fa. In Sec. 3.3 the symbol “Caγ” appears without definition or connection to C0 or gaγ. This is ambiguous and could confuse the mapping between priors and physical couplings.  
- **Required fix:**  
  - Define Caγ clearly when it first appears, and explicitly relate it to C0 and gaγ.  
  - Ensure consistent notation throughout (either C0 or Caγ, not both, unless physically distinct).  
  - Clarify whether the flat prior [1,30] is on the anomaly coefficient or on a rescaled coupling and justify these bounds.

---

**P2-M3 – Figures 1 and 2 – missing quantitative details in captions**

- **Location:** Fig. 1 p.3; Fig. 2 p.4.  
- **Problem:**  
  - Fig. 1 caption references “Triangle plot from the extended ALP MCMC (Run 2, C free).” but does not specify which exact parameters are plotted on the axes, what priors were used, or any credible intervals beyond the one value 3.4±1.1.  
  - Fig. 2 caption: “Comparison of β posteriors across all three model configurations … All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.” No axis labels or units are described in the caption (though presumably the figure itself may be labeled), and no details on how KDE/bins were chosen.  
- **Required fix:**  
  - Expand captions to specify: axis definitions and units, what data/priors each posterior uses, and any smoothing or binning choices.  
  - Confirm that axes in the actual figures include units (degrees for β, etc.). If not, they must be added.

---

**P2-M4 – Sec. 3.3 p.2 – small sample sizes vs claimed precision**

- **Location:** Table 1 p.2; Sec. 3.3 text p.2.  
- **Text:** Sample sizes 720–6,840 accepted samples, Neff ~ 1000. Yet the paper quotes posteriors like βALP = 0.336 ± 0.107° and Caγ×θi = 3.4 ± 1.1 without any estimated Monte Carlo error on these statistics.  
- **Problem:** For a methods paper aiming at PRD, relying on such modest MCMC chains to quote ~30% level constraints with no MC-error estimate is weak. The author acknowledges this qualitatively but does not quantify how large the uncertainty from finite sampling is, nor provide convergence diagnostics beyond a single R̂.  
- **Required fix:**  
  - Provide estimates of Monte Carlo errors on key posterior means and standard deviations (e.g., via repeated chains or batch means).  
  - Alternatively, significantly extend the chains and rerun the analyses to reach Neff ≫ 10³.

---

**P2-M5 – Sec. 2.1 p.1 – use of Bessel J₀(m/H₀) without derivation or reference**

- **Location:** Eq. (1) p.1.  
- **Text:** “Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1)”.  
- **Problem:** The appearance of J0(m/H0) in this context (field displacement from recombination to today for m~H0) is non-trivial. No derivation is shown, and no reference is given where this approximate form is derived. The ratio J0(m/H0)/J0(0) is formally ill-defined since J0(0)=1 is fine, but the integral over cosmic history is not obviously captured by a simple Bessel function of m/H0 without approximations.  
- **Required fix:**  
  - Provide a short derivation (or at least a sketch) in an appendix, or cite a specific paper where this J0 form is derived and shown to be accurate for m~H0.  
  - Clarify what underlying cosmological model (ΛCDM parameters) is assumed in deriving the numerical factor (~0.24).

---

**P2-M6 – Length vs. contribution**

- **Location:** Whole paper (6 pages, but relatively light on technical details).  
- **Problem:** For a claimed “prediction, constraints, and forecast” paper, there is no explicit derivation of the ALP solution, no full likelihood description, and very limited numerical details. Yet the text repeats qualitative statements (naturalness, 9σ test, “no fine-tuning”) multiple times. The paper is arguably long for the actual quantitative content, but paradoxically still under‑documents the key computations.  
- **Required fix:** Either:  
  - Shorten the paper to ~4–5 pages by trimming repeated qualitative discussion and speculative bounce‑cosmology material, and clearly present only robust, well-documented results; or  
  - Expand the methods section significantly with explicit equations, derivations, and numerical checks to justify the constraints and forecasts.

---

### MINOR findings

**P2-m1 – References – missing arXiv IDs and DOIs where available**

- **Location:** References p.6  
- **Problem:** Some entries omit arXiv IDs where they clearly exist (e.g., Minami & Komatsu 2020, Eskilt & Komatsu 2022, Fujita et al. 2021, LiteBIRD Collaboration 2023). Including these is expected at PRD.  
- **Required fix:** Add arXiv IDs and DOIs consistently for all applicable references.

---

**P2-m2 – Sec. 5 p.4 – “14-barrier catalog” is unexplained jargon**

- **Location:** Sec. 5 p.4  
- **Text:** “…see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog.”  
- **Problem:** “14-barrier catalog” is undefined jargon in this paper and depends on a non-public companion manuscript.  
- **Required fix:** Either remove this phrase or briefly explain what this refers to in self-contained terms, or wait until the companion paper is public and properly cited.

---

**P2-m3 – Sec. 6 p.5 – claim of novelty vs Fujita et al.**

- **Location:** Sec. 6 p.5  
- **Text:** “We emphasize that the ALP birefringence model class is well-studied… Fujita et al. (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°, and Namikawa et al. (2025) provide superior ALP mass constraints… Our contribution is … specific parameter identification (fa∼MPl, m∼H0)… and the inference framework…”  
- **Problem:** The distinction between this work and Fujita et al./Namikawa et al. remains somewhat vague. Given that Fujita et al. already study ALP-like dark energy with Planck-scale decay constants and β∼0.3°, the precise novelty of fixing m~H0 and presenting a “natural” β appears modest.  
- **Required fix:** Sharpen and narrow the novelty claim; explicitly state how the current work’s assumptions and analysis differ in substance from Fujita et al. and Namikawa et al., and remove phrases that might overstate novelty.

---

**P2-m4 – Axis labeling and units (to be checked in figures)**

- **Location:** Figs. 1–2.  
- **Problem:** The text does not explicitly state whether β axes are labeled in degrees or radians in the plots. For clarity and to avoid confusion, this must be obvious.  
- **Required fix:** Ensure plot axes show “β [deg]” (or similar) and that captions refer to degrees consistently.

---

**P2-m5 – Slight inconsistency in Eskilt/Komatsu naming**

- **Location:** References p.6; main text.  
- **Problem:** The main text refers to “Eskilt and Komatsu, 2022” and “Eskilt et al. joint analysis”, but the reference is listed as “J. R. Eskilt and E. Komatsu. Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data.” This is correct, but using “Eskilt et al.” when only two authors are listed is a bit odd.  
- **Required fix:** Use consistent phrasing (“Eskilt & Komatsu”) unless there truly are additional co-authors in the specific analysis you refer to, in which case update the reference.

---

### NIT findings

**P2-n1 – Typographical / stylistic issues**

- **Location:** Multiple places.  
- **Examples:**  
  - “coeﬀicient” (with ligature artifact) instead of “coefficient”.  
  - “HFI analysis” vs “Planck HFI analysis” inconsistent capitalization across mentions.  
- **Required fix:** Run a thorough spell-check and carefully clean up ligature artifacts and capitalization.

---

**P2-n2 – Repeated phrasing**

- **Location:** Abstract, Sec. 1, Sec. 6, Conclusion.  
- **Problem:** Phrases like “natural prediction,” “no fine-tuning,” “sharp falsifiability,” “Planck-scale decay constant and Hubble-scale mass” are repeated multiple times almost verbatim.  
- **Required fix:** Streamline and consolidate these points to avoid redundancy and improve readability.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper has a potentially interesting focus—linking Planck-scale ALPs with cosmic birefringence—but the current manuscript does not meet PRD standards. Key numerical inputs rely on non‑existent or mis‑cited references (ACT DR6, Namikawa et al.), significance levels are slightly inconsistent, the Bayes factor is methodologically under-supported, and multiple claims depend on unpublished “companion” manuscripts. Substantial corrections to the bibliography, explicit derivations or citations for the ALP dynamics and LiteBIRD forecast, and clearer, more cautious presentation of evidence and novelty are required before the work can be considered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E12 – Arithmetic inconsistency in combined significance in Introduction and Discussion  
- **Location:** Introduction p.1; Discussion p.5  
- **Text:**  
  - Intro: “Combined, the evidence exceeds **3.5σ**.”  
  - Discussion: “The prediction matches the combined Planck + ACT measurement at **1σ**.”  
- **Problem:** Using the two quoted inputs (0.30±0.11° and 0.215±0.074°), the inverse‑variance weighted combination gives βcombined ≈ 0.242° with σ ≈ 0.064°, i.e. ≈3.8σ, not “exceeds 3.5σ” in the intro nor “matches … at 1σ” in the discussion (difference between 0.27° and 0.242° is ≈0.44σ, and between 0.27° and 0.342° is ≈0.77σ). Both textual claims are numerically sloppy/inaccurate relative to the paper’s own numbers.  
- **Required fix:**  
  - Replace “exceeds 3.5σ” with a quantitatively correct statement like “≈3.8σ from zero” (or whatever value results from a consistently recomputed combination).  
  - Replace “matches … at 1σ” with a more accurate phrasing (e.g. “within ∼0.5–0.8σ”) or explicitly show the numerical deviation and its ratio to σ.

---

P2-E13 – Arithmetic inconsistency in Bayes factors vs quoted significance  
- **Location:** Sec. 3.4 p.3, Eq. (9)  
- **Text:** “ln B = 5.17 … ln B = 4.48 for β ∈ [0°,2°] and ln B = 5.86 for β ∈ [0°,0.5°].”  
- **Problem:** For a Gaussian likelihood with β = 0.242° and σ ≈ 0.064° (≈3.8σ), the approximate Bayesian evidence for β≠0 versus β=0 with a flat prior of width Δβ is roughly lnB ≈ (β/σ)²/2 − ln(Δβ/(√{2π}σ)). For Δβ = 1°, this gives lnB ≳ 6–7, not 5.17; for Δβ = 2° it should be smaller by ln2 ≈ 0.69, and for Δβ = 0.5° larger by ≈0.69, but the quoted triplet (5.17, 4.48, 5.86) is not consistent with a single underlying Gaussian evidence calculation. The ratios between these lnB values do not match the simple prior‑width scaling implied by the stated method.  
- **Required fix:**  
  - Recompute lnB analytically for the 1D Gaussian summary‑likelihood with the stated priors, and either (a) replace the numerical values with consistent ones, or (b) show explicitly why the MCMC‑estimated Savage–Dickey values differ (e.g. due to non‑Gaussianity of the posterior or numerical issues).  
  - Ensure the three lnB values scale with prior width in a manner consistent with the underlying likelihood, or state clearly if a different model/likelihood is used for each.

---

P2-E14 – Arithmetic mismatch in “order‑unity, no fine‑tuning” statement for fphoton×C0  
- **Location:** Abstract p.1; Sec. 3.2 p.2  
- **Text:** “fphoton × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning).”  
- **Problem:** This parameter evidently comes from mapping βcombined into an effective coupling, but no explicit formula is given; moreover, with βcombined ≈ 0.242° ≈ 4.22×10⁻³ rad and ∆ϕ/fa ≈ 10⁻², one would infer C0 θi ≈ 2β /(∆ϕ/fa) ≈ 0.84 (for θi ∼1). The quoted “1.73±0.44” is roughly twice that naive value, and the paper gives no calculation showing how “fphoton” is defined such that this number emerges. Also, the uncertainty on fphoton×C0 is not propagated from any explicitly stated inputs.  
- **Required fix:**  
  - Add the explicit algebraic relation between βcombined, ∆ϕ/fa, and fphoton×C0, then recompute the central value and error bar transparently.  
  - Confirm that the result is consistent with the assumed ∆ϕ/fa ∼10⁻² and β, or adjust those assumptions accordingly.

---

P2-E15 – Figure 1 caption/body mismatch in parameter naming and content  
- **Location:** Fig. 1 caption p.3; Sec. 3.3 p.2  
- **Text:**  
  - Caption: “Triangle plot from the extended ALP MCMC (Run 2, C free) … Caγ × θi is centered at 3.4 ± 1.1.”  
  - Body: Priors: “Caγ flat on [1, 30] (Run 2 only).”  
- **Problem:** The main text never defines “Caγ” nor “C” in “C free” in terms of C0 or gaγ, and there is no explicit equation in Sec. 3 that shows how Caγ enters the birefringence prediction. This creates an internal mismatch: the figure purports to show a “coupling-misalignment product” that is central to the physics, but the reader cannot map it to the Lagrangian parameters defined earlier. This goes beyond the previously noted notation inconsistency (P2-M2) by directly impacting the interpretability of Figure 1.  
- **Required fix:**  
  - In Sec. 2 or at the start of Sec. 3.3, introduce Caγ explicitly (e.g. Caγ ≡ C0/fa in suitable units) and state that Run 2 samples Caγ and θi jointly, so that Caγ×θi is the relevant combination.  
  - Ensure that Figure 1’s caption explicitly ties Caγ to the earlier‑defined coupling and that the axes in the triangle plot are consistent with the stated priors.

---

P2-E16 – Figure 2 and body claims: missing quantitative comparison and implied σ‑level  
- **Location:** Fig. 2 caption p.4; Sec. 3.3 p.2; Discussion p.5  
- **Text:**  
  - Caption: “All three [posteriors] are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.”  
  - Body: “The ALP model reproduces the observed birefringence with no tension.”  
- **Problem:** Numerically, the three central values are βALP = 0.336±0.107°, βfree = 0.344±0.096°, and βobs = 0.342±0.094°. Pairwise differences are at the level of ≈0.01–0.008°, i.e. ~0.1σ given the quoted errors. The paper never quantifies this; instead it uses qualitative phrases (“no tension”, “consistent with”) without any explicit Δ/σ comparison. This falls under unquantified hedging and also a figure‑caption/body mismatch: the caption asserts consistency but does not provide numbers, and the body does not back the qualitative claim with a calculation.  
- **Required fix:**  
  - Add a short quantitative statement, e.g. “The differences between these central values are <0.1σ given their uncertainties,” both in the body text and (briefly) in the caption.  
  - This makes the “no tension” / “consistent” claim quantitatively transparent rather than purely qualitative.

---

P2-E17 – Equation (3) notation vs. text: undefined βobs, σi and implied likelihood construction  
- **Location:** Sec. 3.2 p.2, Eq. (3)  
- **Text:**  
  - Equation (3) uses “βobs” inside the product likelihood and “σi” in the denominator, but the text above simply says “combining the measurements under the assumption of independent errors” and does not define per‑experiment βiobs and σi.  
- **Problem:** As written, Eq. (3) is dimensionally and conceptually correct, but internally inconsistent in notation: it uses the scalar βobs (previously reserved for the joint Eskilt value) instead of βi, and never defines the index i on βobs. This could be read as using the same βobs for all terms, which would be wrong. It also obscures the fact that the combination uses two specific numbers (0.30±0.11°, 0.215±0.074°).  
- **Required fix:**  
  - Rewrite Eq. (3) using βi,obs (or similar) instead of βobs, and explicitly define i = {Planck, ACT} with β1,obs = 0.30°, σ1 = 0.11°, β2,obs = 0.215°, σ2 = 0.074°.  
  - This prevents confusion with the later βobs = 0.342±0.094°, and makes the likelihood construction reproducible.

---

P2-E18 – σ‑from‑different‑null‑procedures juxtaposed without qualifier in Sec. 3.3  
- **Location:** Sec. 3.3 p.2  
- **Text:** “The posterior on β from the ALP model (Run 1…) βALP = 0.336 ± 0.107◦ … compared to the model‑independent fit (Run 3) βfree = 0.344 ± 0.096◦ and the observed value βobs = 0.342 ± 0.094◦.”  
- **Problem:** These three σ values arise from different likelihoods and parameterizations (ALP model with fixed C, pure β‑only model, and an external Eskilt joint analysis). They are listed side‑by‑side with significance‑like interpretation (“reproduces … with no tension”), but there is no explicit statement here that their σ’s are not directly comparable, even after you already flagged a similar issue at higher level in P2-E3. This is a new, specific instance of exactly the comparability problem the journal wants explicitly addressed at each juxtaposition.  
- **Required fix:**  
  - Immediately after this sentence, add a clause such as: “Note that the quoted uncertainties arise from different likelihoods and prior choices and are therefore not strictly comparable in terms of σ‑significance.”  
  - Similar explicit caveats should be added anywhere these three β posteriors are directly compared (including Fig. 2 caption).

---

P2-E19 – Abstract faithfulness: “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data”  
- **Location:** Abstract p.1 vs. Sec. 3.1–3.2  
- **Text:** Abstract claims use of “Planck HFI and ACT DR6 data”. Body uses two point‑estimate inputs: “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11°” and “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074°.”  
- **Problem:** The abstract wording suggests a direct analysis of the raw Planck HFI and ACT time‑ordered or map data, whereas the body only combines published (or in one case non‑published) summary point estimates via Eq. (3). This is a mismatch between abstract and methods: journals expect the abstract to state clearly that a **summary‑likelihood on literature β measurements** is used, not a new analysis of the original datasets.  
- **Required fix:**  
  - Rephrase the abstract to “We perform a Gaussian summary‑likelihood inference combining published Planck and ACT birefringence measurements” (or equivalent).  
  - Make explicit that the work does not re‑analyze raw Planck HFI or ACT DR6 data, but uses literature values only.

---

P2-E20 – Unquantified hedge: “The prediction is natural in the sense that …” vs. actual parameter ranges  
- **Location:** Abstract p.1; Sec. 2.2 p.1; Discussion p.5  
- **Text:** “The prediction is natural in the sense that fa ∼ MPl is the natural scale … m ∼ H0 ensures the field is rolling today … θi ∼ O(1) is generic.”  
- **Problem:** These statements assert naturalness and genericity but the paper never quantifies how wide a range of fa, m, and θi yield β in the observed band, nor does it show a posterior or prior‑to‑posterior comparison for these parameters. Calling the prediction “natural” without specifying how much tuning in m/H0 or θi is allowed is an unquantified claim of robustness/novelty.  
- **Required fix:**  
  - Provide at least an order‑of‑magnitude estimate of the allowed ranges (e.g. “for 0.3≲m/H0≲3 and 0.3≲θi≲3 the resulting β lies in [0.1°,0.5°]”), or similar.  
  - Alternatively, soften the language to a descriptive statement (“fa is chosen near MPl, m is chosen near H0, and θi is taken to be O(1)”) without asserting “natural” or “generic”.

---

P2-E21 – Stale number: β ≈ 0.27° repeated as prediction without documented update from m/H0 choice  
- **Location:** Abstract p.1; Sec. 2.2 p.1; Sec. 6 p.5; Sec. 7 p.5  
- **Text:** Multiple sentences assert “β ≈ 0.27°” as the model prediction.  
- **Problem:** The only semi‑quantitative derivation is in Sec. 2.2, which uses ∆ϕ/fa∼10⁻² and then jumps to β ≈ C0 θi ×5×10⁻³ rad≈0.27°. If future refinements (e.g. a more accurate cosmological integration) led the author to target β ≈0.24–0.30°, some parts of the text may have been left at “0.27°” while others use 0.242° and 0.336°. This specific numerical “0.27°” appears to be a stale representative number rather than a consistently propagated prediction with an uncertainty estimate.  
- **Required fix:**  
  - Decide on a consistent predicted range or central value for β from the model (including its theoretical uncertainty) and use that throughout the paper, or explicitly state that 0.27° is an approximate order‑of‑magnitude benchmark, not a precise prediction.  
  - Ensure that LiteBIRD forecasts and “matches the combined Planck+ACT measurement at 1σ” statements use the same, explicitly defined prediction value.

---

P2-E22 – Abstract faithfulness: “spectator ALP … mass m ∼ H0” vs. sampled prior range  
- **Location:** Abstract p.1; Sec. 3.3 p.2  
- **Text:** Abstract: “ALP with … mass m ∼ H0.” Body: “log10(m/eV) flat on [−35, −30].”  
- **Problem:** H0 in energy units is ≈10⁻³³ eV, so “m ∼ H0” corresponds to log10(m/eV)≈−33. The prior [−35, −30] spans two orders of magnitude above and below this value. The abstract language implies a sharply tuned m ≈ H0, but the main text reveals a broad prior that allows m ≫ H0. The paper does not show the posterior on m nor demonstrate that it actually peaks near H0.  
- **Required fix:**  
  - Either (a) show and discuss the posterior on m, verifying that it is indeed localized near H0 within the prior range, or (b) weaken the abstract language to “mass in the vicinity of H0 (within a few orders of magnitude)”.  
  - Clarify in Sec. 2 how sensitive β is to m/H0 across this prior range.

---

If you want, I can next go through the manuscript line‑by‑line to build a small table of every numerical claim (σ, percentage, ratio) with the recomputed value beside it, so you can systematically check for further stale or inconsistent numbers before resubmission.