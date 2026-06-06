# P2 auto-2026-06-05_1919pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12052 chars)
**Wall time**: 2533.9s

---

P2-E1 (ESSENTIAL) – Global: Missing PDF / cannot verify internal consistency  
- **Location:** Entire manuscript (0 pages indicated; only excerpted text provided)  
- **Problem:** The review instructions state I am “looking at” the rendered PDF, but only a text block is provided, with no pagination, figure rendering, or full reference details (e.g., volume/page for some items). I therefore cannot: (i) assign accurate page numbers, (ii) inspect actual figures/tables/axes, or (iii) verify whether equations and numbers in the excerpt match those in the full submitted PDF version.  
- **Required fix:** The authors (or editorial office) must ensure the full PRD submission PDF (with page numbers, figures, tables, and complete reference formatting) is used for the final citation and consistency audit. This report is necessarily limited to the textual content shown in the prompt.

Below I treat “pages” as the logical pages of the provided text (1–6). All page numbers are therefore approximate and must be mapped to the actual PDF before action.

---

## 1. Abstract and numerical/statistical consistency

P2-E2 (ESSENTIAL) – Abstract σ discrepancy and unsupported “3.6σ”  
- **Location:** Abstract, page 1  
- **Problem:**  
  - Abstract: “βobs = 0.342 ± 0.094◦ from the Eskilt et al. joint Planck + ACT analysis” and “3.6σ isotropic birefringence signal.”  
  - In the body, the same value βobs = 0.342 ± 0.094◦ is quoted (Sec. 3.1, 3.3), but no explicit σ-significance for the Eskilt-only analysis is recomputed; 0.342/0.094 ≈ 3.64σ, so “3.6σ” is numerically consistent. However, the paper also states “Combined, the evidence exceeds 3.5σ” in the Introduction, and a different combined analysis later yields 3.9σ (Eq. 4), which is not clearly distinguished from the “3.6σ” Eskilt result.  
  - The wording “3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094◦ from the Eskilt et al. joint Planck + ACT analysis)” implies that the 3.6σ value is taken from Eskilt et al., not recomputed by the present work. In the actual Eskilt & Komatsu paper, the main Planck-only detection is ≈2.4–2.6σ, and with WMAP+Planck the significance is ≈3σ; a 3.6σ figure is not prominently quoted in the abstract or main tables.[2][1] (The exact number depends on the particular combination; I do not see a clearly labeled “3.6σ” isotropic detection in their abstract or headline results.)  
- **Required fix:**  
  - Explicitly state whether the 3.6σ value is (a) directly quoted from Eskilt et al. or (b) recomputed by the author from their reported mean and error; if (b), do not attribute the significance number to Eskilt et al. as a quoted result.  
  - Verify in Eskilt & Komatsu [Phys. Rev. D 106, 063503 (2022)] the exact significance associated with βobs = 0.342 ± 0.094° for the *joint* Planck + ACT analysis, and correct the referenced σ-level and wording so it matches what they actually publish. If Eskilt et al. do not quote “3.6σ” themselves, the text should say “corresponding to 3.6σ, computed as β/σβ” and not imply this is their stated headline significance.  
  - Clarify in the Introduction which σ values refer to (i) Planck HFI, (ii) ACT, (iii) Eskilt joint analyses, and (iv) the author’s own combined analysis, and caution that different analyses are not strictly identical.

P2-M1 (MAJOR) – Abstract “natural prediction” numerical estimate not transparently derived  
- **Location:** Abstract, page 1; Sec. 2.2, page 2  
- **Problem:**  
  - Abstract claims: “this minimal setup naturally accommodates a birefringence rotation angle β ≈ 0.27◦ … For order-unity inputs…”  
  - Sec. 2.2 states: “For C0 ∼ 1, θi ∼ 1: the cosmological field evolution gives ∆ϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27◦.”  
  - Numerically: 5×10−3 rad ≈ 0.286° (not 0.27°), and 10−2/2 ≈ 5×10−3 is fine, but the “cosmological field evolution gives ∆ϕ/fa ∼ 10−2” is asserted without any explicit calculation or reference to a worked example in the literature. Fujita et al. and related ALP-birefringence works do not present this specific 10−2 number as a generic, model-independent factor; it depends on detailed dynamics.[6][1]  
- **Required fix:**  
  - Provide a short, explicit derivation or at least a numerical estimate in an appendix demonstrating that for m ∼ H0, fa ∼ MPl, θi ∼ 1, the integrated field motion produces ∆ϕ/fa ≈ 10−2 in the ΛCDM background used; specify cosmological parameters and show robustness to variations.  
  - Correct the decimal: “5×10−3 rad ≈ 0.29◦” or change to “≈0.3◦” if a rough estimate is intended; do not present 0.27° as more precise than the calculation supports.  
  - If the 0.27° value is instead chosen to match Fujita et al. or another reference, say explicitly that the number is taken from that work.

---

## 2. Internal numerical checks, σ-levels, and Bayes factors

P2-E3 (ESSENTIAL) – Combined β significance and abstract consistency  
- **Location:** Abstract, page 1; Sec. 3.2, Eq. (4), page 2  
- **Problem:**  
  - Sec. 3.2 quotes: βcombined = 0.242 ± 0.061° (3.9σ from zero). 0.242/0.061 ≈ 3.97σ, so “3.9σ” is slightly rounded down, which is acceptable.  
  - The abstract states: “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061◦ (3.9σ from zero) with an effective photon coupling fphoton × C0 = 1.73 ± 0.44 …” This matches Eq. (4) and Eq. (5) numerically and is internally consistent.  
  - However, Section 3.1 lists the two inputs as β = 0.30 ± 0.11° and β = 0.215 ± 0.074°. The inverse-variance weighted combination of these two measurements is:  
    - σ1 = 0.11, σ2 = 0.074 ⇒ w1 = 1/σ1² ≈ 82.64, w2 ≈ 182.76, total w ≈ 265.40 ⇒ σcomb ≈ 1/√w ≈ 0.0613°.  
    - βcomb = (0.30·w1 + 0.215·w2)/w ≈ (24.79 + 39.33)/265.4 ≈ 0.2417°.  
    - So Eq. (4) is numerically correct, but the text does not show this calculation.  
- **Required fix:**  
  - Add a short sentence in Sec. 3.2 explicitly showing the inverse-variance combination leading to Eq. (4), or move this simple calculation to a short appendix. This is a core scalar used in the abstract and should be fully transparent.  
  - State explicitly that the 3.9σ significance is just β/σβ, not an independent null test result with different systematics.

P2-M2 (MAJOR) – Bayes factor prior dependence and traceability  
- **Location:** Sec. 3.4, page 3  
- **Problem:**  
  - The paper quotes ln B = 5.17 “computed via the Savage-Dickey density ratio with a flat prior β ∈ [0◦ , 1◦]” and provides alternative values for different priors. However, no explicit expression for the prior density or posterior density at β = 0 is given, nor is the posterior from Eq. (4) directly used.  
  - Using the Gaussian posterior N(0.242°, 0.061°) with a uniform prior on β over [0,1°], an approximate Savage–Dickey Bayes factor can be estimated as:  
    \( B ≈ \frac{\pi(β=0)}{p(β=0|d)} ≈ \frac{1/1°}{\frac{1}{\sqrt{2\pi}\,σ}\exp[-(β/σ)^2/2]} \).  
    This yields numbers comparable to but not exactly equal to those stated; without the full posterior (e.g., non-Gaussian tails from MCMC), I cannot reproduce ln B = 5.17 exactly.  
  - Since ln B is used as a key evidence metric in the abstract and conclusions, PRD standards require that it be reproducible from the information given or from data stored in a repository.  
- **Required fix:**  
  - Provide either (a) a brief analytic approximation using Eq. (4) that reproduces the quoted ln B within a stated numerical accuracy, or (b) a reference to a data/chain repository where the posterior samples used for the Savage–Dickey computation are stored, so that ln B can be independently verified.  
  - Clarify in detail how the prior on β interacts with the model priors on θi, m, and Caγ in Run 1/2 (if at all), and whether the Bayes factor is computed in the reduced one-parameter space or in the full ALP parameter space.

P2-M3 (MAJOR) – LiteBIRD 9σ forecast logic is over-simplified  
- **Location:** Sec. 4, Eq. (10), page 3  
- **Problem:**  
  - The forecast significance is given as Significance = 0.27/0.03 = 9σ, assuming σ(β) ≈ 0.03° from the LiteBIRD forecast paper.[4] This treats the future measurement as a single Gaussian with variance fixed at the fiducial forecast and ignores (i) potential systematics, (ii) the fact that the forecast σ depends on self-calibration strategy, (iii) correlation with other parameters.  
  - The LiteBIRD science paper typically gives sensitivity under several assumptions; the connection between those and the specific “σ(β) ≈ 0.03°” used here is not explained beyond a brief mention.[4]  
- **Required fix:**  
  - Qualify in the text that the 9σ number is a *naive Fisher-style forecast* assuming Gaussian likelihood, no additional systematics beyond those captured in σ(β), and that the LiteBIRD collaboration’s quoted σ refers exactly to the same isotropic β parameter used here.  
  - Ideally include a short Fisher-matrix–style derivation or citation to an existing forecast for isotropic birefringence in LiteBIRD that explicitly reports σ(β) ≈ 0.03°. If such a number is not stated explicitly in the cited LiteBIRD paper, correct the claimed σ or provide a more accurate reference.

---

## 3. Methodological clarity and comparability of σ-values

P2-E4 (ESSENTIAL) – Comparability of σ-values from different analyses  
- **Location:** Introduction, page 1; Sec. 3.1–3.3, pages 2–3; Figures 1–2  
- **Problem:**  
  - The paper juxtaposes several σ significances:  
    - Planck HFI: 0.35 ± 0.14° (2.5σ) from Minami & Komatsu.[1]  
    - ACT DR6: 0.215 ± 0.074° (2.9σ).  
    - Combined summary likelihood: 0.242 ± 0.061° (3.9σ).  
    - Eskilt et al. joint analysis: βobs = 0.342 ± 0.094° (≈3.6σ).  
    - Eskilt+Planck+ACT joint context in introduction “Combined, the evidence exceeds 3.5σ.”  
  - These σ-levels are derived from different pipelines, likelihoods, masks, and systematics treatments; they are **not directly comparable** in the strict statistical sense.  
  - The journal instructions in this prompt explicitly require that “If sigma values from different null procedures appear side-by-side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.” This condition is violated: the paper does not repeatedly emphasize non-comparability; at most it hints at differences in data usage.  
- **Required fix:**  
  - At every major place where different σ values are listed in the same paragraph or figure (Introduction, Sec. 3.1, caption of Fig. 2), add explicit phrases such as: “These significances are derived from different analysis pipelines and are not directly comparable; they are quoted here only as rough benchmarks.”  
  - In the abstract, clarify that 3.6σ (Eskilt joint) and 3.9σ (this work’s combined analysis) involve different data combinations and likelihood assumptions.  

P2-M4 (MAJOR) – Summary-likelihood vs. full EB-spectrum analyses  
- **Location:** Sec. 3.1–3.2, page 2  
- **Problem:**  
  - The author mixes point-estimate combination (Eq. 3–4) with reference to a “full EB cross-spectrum” fit in Eskilt et al., and later with MCMC EB-based fits. These are distinct analyses.  
  - The text does not clearly articulate that the combined β = 0.242 ± 0.061° is *not* the same as the Eskilt et al. full-spectrum best fit, which yields βobs = 0.342 ± 0.094°, and the difference in means (≈0.1°) is not discussed.  
- **Required fix:**  
  - Add a short discussion of why the combined point-estimate summary likelihood gives a lower central value than the full EB-spectrum fit, and whether this difference is within expected statistical scatter (it is ≈1σ).  
  - Clearly distinguish between (i) the summary-likelihood combination used for “βcombined” and (ii) the βobs used in MCMC, and state that they are derived using different methods and therefore are not identical by construction.

---

## 4. Equations and dimensional consistency

P2-M5 (MAJOR) – Eq. (1) derivation and meaning of J₀(m/H₀)  
- **Location:** Sec. 2.1, Eq. (1), page 1  
- **Problem:**  
  - Eq. (1) states:  
    \( \Delta\phi \approx f_a \theta_i \left(1 - \frac{J_0(m/H_0)}{J_0(0)}\right) \approx f_a \theta_i \times O(1). \)  
    Here J0 is presumably the Bessel function of the first kind. However:  
    - J0(0) = 1, so the ratio J0(m/H0)/J0(0) = J0(m/H0) makes the expression look artificially complicated.  
    - No derivation is provided for why a Bessel function appears in the exact solution for a slowly rolling ALP in a ΛCDM background, especially across radiation, matter, and dark energy eras. For m ∼ H0, the equation of motion in standard FRW does not generically lead to such a simple analytic Bessel form; it is at best an approximation in a matter-only or de Sitter background.  
    - The later statement “For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24; the precise value depends on the cosmological integration” is numerically correct (1 − J0(1) ≈ 0.235), but the dependence on cosmological parameters is not demonstrated, and the J0 approximation is not justified.  
- **Required fix:**  
  - Either provide a derivation (perhaps in an appendix) showing that the field evolution can indeed be approximated by a Bessel function with argument m/H0 under the cosmological assumptions used, *or* replace Eq. (1) with a more general numerical result (e.g., “we solve the background evolution equation numerically, finding Δφ ≈ 0.24 f_a θ_i for m ≈ H0”).  
  - Remove the unnecessary J0(0) in the denominator or explain why it is kept.  
  - Clarify that 1 − J0(1) ≈ 0.24 is an approximate numerical factor specific to the chosen cosmology.

P2-N1 (NIT) – Eq. (2) minor notation inconsistency  
- **Location:** Sec. 2.2, Eq. (2), page 2  
- **Problem:**  
  - Eq. (2) writes: “β = gaγ Δϕ/2 = C0 Δϕ/(2fa) = C′0 θi/2 × O(1)” (the last factor uses C′0, presumably same as C0). The notation “C 0” and “C0” appears in the text; it may just be a typesetting artifact in the excerpt, but PRD will require consistent notation.  
- **Required fix:**  
  - Use a single symbol consistently (C0) and avoid C′0 unless intentionally introducing a new parameter. Ensure the LaTeX matches this.

---

## 5. MCMC configuration and statistical rigor

P2-M6 (MAJOR) – MCMC sample sizes and effective sample size (Neff) claims  
- **Location:** Sec. 3.3, page 2; Table 1, page 2  
- **Problem:**  
  - Table 1 lists: 2,160; 6,840; and 720 “Samples” with R̂ − 1 < 0.01 and the text states: “small effective sample sizes (Neff ∼ 1,000).” From the raw sample counts given, it is impossible to obtain Neff ≈ 1,000 for Run 3 (720 samples). Even for the longer chains, Neff values near 1,000 require quite low autocorrelation, which is not substantiated.  
  - No details are provided on the number of chains, thinning, or the calculation of Neff, so the claim “Neff ∼ 1,000” cannot be independently validated.  
- **Required fix:**  
  - Provide explicit Neff values per parameter for each run, as computed by a standard package (e.g., emcee, GetDist, or similar), and make sure they are consistent with the “Samples” counts. If 720 refers to post-thinning samples with Neff ≈ 500–700, say so explicitly.  
  - If Neff is smaller than 1,000 for some parameters, correct the text and qualify the precision of posterior tail and Bayes factor estimates accordingly.

P2-M7 (MAJOR) – Prior definition: Caγ vs. C, C0 vs. Caγ  
- **Location:** Sec. 3.3, page 2; Table 1, page 2; Sec. 2.2, page 2  
- **Problem:**  
  - Section 2.2 defines gaγ = C0/fa and uses C0 for the anomaly coefficient.  
  - In Sec. 3.3, the prior is stated as “Caγ flat on [1,30] (Run 2 only).” Table 1 uses “C” and “C free”. Later, Sec. 3.3 states “Caγ × θi = 3.4 ± 1.1”.  
  - This introduces three notations (C0, Caγ, C) for what appears to be essentially the same coupling parameter, and the relationship among them is not clarified.  
- **Required fix:**  
  - Define a single coupling parameter symbol at the beginning (e.g., Cγ or C), stick to it throughout, and clearly state how it relates to gaγ.  
  - Ensure table labels (“C = 8 fixed”; “C free”) are unambiguously mapped to Caγ in the prior description and to C0 in the theoretical definition, or rename them to match.

---

## 6. Claims of novelty and literature consistency

P2-M8 (MAJOR) – Claim of “our contribution” vs. existing ALP CB literature  
- **Location:** Sec. 6, page 5  
- **Problem:**  
  - The author states: “We emphasize that the ALP birefringence model class is well-studied in the literature [Fujita et al., 2021]. Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3◦ … Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.”  
  - Fujita et al. indeed discuss ALP-induced birefringence and explore parameter regimes including Planck-scale decay constants and cosmic-acceleration-scale masses; they show that certain parameter ranges naturally produce β ∼ 0.3°.[6] Recent Planck-based constraints on ALPs via birefringence (e.g., 2506.20824) also explore similar mass ranges m ∼ H0.[1][2]  
  - The present paper needs to be much more precise in claiming *what is new*: e.g., is the combination fa ∼ MPl and m precisely equal to H0 qualitatively different from previous works? Or is the novelty mainly the particular data combination and the “naturalness” framing? As it stands, the novelty claim is vague and risks overstating originality.  
- **Required fix:**  
  - Carefully compare the parameter choices in this paper against those in Fujita et al. (2021) and later ALP CB constraints (including ALP mass ranges around H0).[6][1][2]  
  - Explicitly state what aspects are *not* present in those works (e.g., the exact Planck+ACT summary-likelihood combination, the specific forecast for LiteBIRD within this parameter regime, or the connection to the ECH framework).  
  - Soften and sharpen the novelty claim to avoid overlap: for example, “Previous works (Fujita et al. 2021; Planck-ALP analyses 2025) have already shown that Planck-scale ALPs with Hubble-scale masses can naturally yield β ∼ 0.3°. Here we [do X that is qualitatively new].”

P2-M9 (MAJOR) – “Superior ALP mass constraints” claim for Namikawa et al. (in preparation)  
- **Location:** Sec. 6, page 5; References, page 6  
- **Problem:**  
  - The text: “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum.”  
  - Reference: “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  
  - As of now there is an arXiv paper 2506.20824 “Planck constraints on axion-like particles through isotropic cosmic birefringence” by a different author list.[1][2] I cannot locate a record of “Namikawa, Murai & Naokawa” with this exact title; it appears to be an intended future submission (“In preparation”) rather than an existing arXiv e-print.  
  - PRD standards do not allow heavy reliance on “in preparation” citations for core comparative claims, especially when the reference is used to support “superior mass constraints.”  
- **Required fix:**  
  - Either (a) replace the “in preparation” Namikawa et al. reference with an actual, citable arXiv or journal publication (if it exists), or (b) remove the claim that they provide “superior” constraints and instead phrase it as “ongoing work suggests improved mass constraints may be possible using the full Planck EB spectrum (private communication)” if appropriate—though even this should be used sparingly.  
  - If the “in preparation” reference is speculative or not yet publicly available, delete it from the references list and text, or move it to a brief “Note added” once/if it appears.

---

## 7. Bibliography accuracy and citation forensics

P2-M10 (MAJOR) – Diego-Palazuelos & Komatsu (ACT DR6) incomplete and future-dated  
- **Location:** References, page 6; Sec. 3.1, page 2  
- **Problem:**  
  - The reference is: “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”  
  - As of now, there is an arXiv preprint 2506.20824 on Planck constraints on ALPs (not ACT) by different authors.[1][2] I cannot find an arXiv preprint with exactly that title and author combination in 2025 via NASA ADS or arXiv.  
  - The ACT DR6 birefringence analysis may indeed be in preparation or presented in talks, but if it is not publicly available with stable bibliographic information, it should not be treated as a fully citable arXiv preprint.  
  - The β = 0.215 ± 0.074° (2.9σ) number is attributed to “ACT DR6,” but without a traceable arXiv ID or journal reference I cannot confirm the value from the literature.  
- **Required fix:**  
  - Provide the actual arXiv ID (e.g., arXiv:25xx.xxxxx) and verify that the title and author list match the citation.  
  - If no such preprint exists yet, change the reference to “in preparation” or “private communication,” and clearly flag in the main text that the 0.215 ± 0.074° measurement comes from non-public or preliminary ACT DR6 results.  
  - PRD may require that the analysis not rely critically on non-public data; either ensure a published/posted public reference exists or treat this measurement more cautiously.

P2-M11 (MAJOR) – LiteBIRD citation: verify title and journal metadata  
- **Location:** References, page 6; Sec. 4, page 3  
- **Problem:**  
  - Cited as: “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023. doi: 10.1093/ptep/ptac150.”  
  - The actual title is slightly different: “LiteBIRD science goals and forecasts: a space-borne CMB polarization experiment” (or similar; the precise wording needs verification) and the DOI 10.1093/ptep/ptac150 corresponds to a 2023 PTEP article on LiteBIRD science goals.[4] The given title “a full-sky cmb polarization survey” may not exactly match the published one.  
- **Required fix:**  
  - Verify the exact title as recorded in the journal and update the reference accordingly (capitalization of CMB, hyphenation, and subtitle).  
  - Ensure that the volume, article number 042F01, and DOI all match the PTEP record.

P2-M12 (MAJOR) – Companion papers “submitted simultaneously” with no venues or arXiv IDs  
- **Location:** Sec. 5, page 4; Sec. 6, page 5; References, page 6  
- **Problem:**  
  - Two companion papers by Golden are cited:  
    - “Spin-torsion cosmology and the search for geometric dark energy: Structural barriers, perturbation transparency, and surviving predictions. Companion paper, submitted simultaneously, 2026a.”  
    - “Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”  
  - No arXiv IDs, no journal names, and no DOIs are provided. Such citations are acceptable only if the companion papers are genuinely submitted to PRD simultaneously and cross-referenced in the submission system; otherwise, they function as “in preparation” references that cannot be traced.  
  - The second companion paper is invoked for “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].” This is a specific load-bearing numerical statement (fNL = −35/8) that cannot be verified in the literature if the companion paper is not publicly accessible.  
- **Required fix:**  
  - If both companion papers are indeed part of a coordinated PRD submission, clearly indicate this in a footnote and ensure the editorial office has access to them. Otherwise, provide arXiv IDs or published references.  
  - For the fNL = −35/8 claim, either (a) briefly sketch the derivation in this paper (e.g., in an appendix) or (b) restrict the statement to “A matter-bounce model can yield fNL ≈ −4.4 (see Golden 2026b for details)” and ensure Golden 2026b is at least on arXiv.  
  - PRD typically disfavors core results being supported only by non-public companion manuscripts.

P2-M13 (MAJOR) – Namikawa et al. reference metadata  
- **Location:** References, page 6  
- **Problem:**  
  - “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  
  - As noted earlier, I cannot find such a record in arXiv or ADS at present; “In preparation” contradicts “arXiv e-prints,” which implies it is already posted.  
- **Required fix:**  
  - Correct the reference classification: either “in preparation” (no arXiv) or “arXiv:25xx.xxxxx” (publicly posted). It cannot be both.  
  - If it is genuinely in preparation, remove “arXiv e-prints” and do not treat it as a fully citable work.

P2-N2 (NIT) – Minami & Komatsu and Eskilt & Komatsu metadata  
- **Location:** References, page 6  
- **Problem:**  
  - The Minami & Komatsu PRL reference is correct in title, volume, page, and DOI.  
  - Eskilt & Komatsu: “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data. Physical Review D, 106:063503, 2022. doi: 10.1103/PhysRevD.106.063503.” This is consistent with ADS and APS metadata.[2]  
  - However, the reference lacks an arXiv ID (for completeness) and some style guides prefer including it.  
- **Required fix:**  
  - Optionally, add the arXiv IDs (e.g., arXiv:2010.XXXX and arXiv:2209.XXXX) if PRD style permits. This is minor and not required for acceptance.

---

## 8. Unsupported or under-supported statements

P2-M14 (MAJOR) – “No fine-tuning” and “naturalness” claims not quantitatively argued  
- **Location:** Abstract, page 1; Sec. 2.2, page 2; Sec. 6, page 5; Conclusion, page 6  
- **Problem:**  
  - The paper repeatedly states that the ALP scenario is “natural,” “requires no fine-tuning,” and that “Every input is O(1) in natural units.”  
  - However, the field displacement factor 1 − J0(m/H0) ≈ 0.24 and the ∆φ/fa ≈ 10−2 factor are quite specific; the initial misalignment θi is essentially a free phase on [0,π], and the anomaly coefficient C0 is model-dependent. Some degree of coincidence (C0θi/π times a factor ≈10−2 giving exactly 0.27°) is needed.  
  - No quantitative measure of fine-tuning (e.g., a sensitivity measure) is given. The discussion remains qualitative.  
- **Required fix:**  
  - Either remove the strongest formulations (“no fine-tuning,” “every input is O(1)”) or support them by a more detailed discussion: e.g., show that for θi uniformly distributed, a large fraction (say >20%) of the prior volume yields β in the observed range, which would support the “naturalness” claim.  
  - Explicitly quantify how sensitive β is to order-unity variations in C0 and θi, perhaps with a small figure showing β as a function of θi for C0 ∼ 1.

P2-M15 (MAJOR) – “Independent of bounce cosmology” vs. ECH gravity motivation  
- **Location:** Sec. 5, page 4; Conclusion, page 6  
- **Problem:**  
  - The paper claims: “This birefringence prediction is independent of bounce cosmology … The prediction holds in any cosmological background where the ALP field begins rolling at z ∼ 1.”  
  - Yet, Sec. 5 ties the ALP to an ECH gravity framework and the Barbero–Immirzi pseudoscalar sector of the Holst action, which is associated with specific gravitational dynamics and possibly with a bounce scenario.  
  - While the field dynamics equation given is generic, the independence claim is stronger than what is demonstrated: only a ΛCDM-like expansion with H0-scale mass is used. No demonstration is given that other exotic cosmologies preserve the same Δφ/fa factor.  
- **Required fix:**  
  - Soften the statement to something like: “Although here we motivate the ALP in the context of ECH gravity and bounce cosmology, the birefringence prediction depends only on the late-time rolling of the ALP field and therefore applies to any cosmology sharing the same late-time expansion history.”  
  - If truly independent of bounce cosmology, explicitly show that altering early-time behavior (with a bounce) does not affect the late-time Δφ relevant to β.

---

## 9. Figures and tables (as far as can be inferred)

P2-M16 (MAJOR) – Figure 1 and Figure 2 not fully audit-able, captions oversimplified  
- **Location:** Figure 1, page 3; Figure 2, page 4  
- **Problem:**  
  - Only captions, not the images, are provided. I cannot check axes labels, units, or whether the plotted numbers match the reported posterior means and uncertainties.  
  - Figure 1 caption: “The posterior on the coupling-misalignment product Caγ × θi is centered at 3.4 ± 1.1…” This matches Eq. (8).  
  - Figure 2 caption: “Comparison of β posteriors across all three model configurations … All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.” The text does not quantify the degree of consistency (e.g., overlap of 68% credible intervals) or whether the plotting uses normalized posteriors.  
- **Required fix:**  
  - Ensure axes in Figure 1 and Figure 2 are clearly labeled (β in degrees, θi dimensionless, Caγ dimensionless, etc.) and units are consistent with the text.  
  - In the main text, briefly quantify the level of agreement (e.g., provide the difference in means in σ units) rather than only stating qualitative consistency.

P2-N3 (NIT) – Table 1 minimal but acceptable; check column labelling  
- **Location:** Table 1, page 2  
- **Problem:**  
  - Table 1 has run labels (“ALP (C = 8 fixed)” vs. “ALP (C free)” vs. “β free”) but the column “Model” could be more descriptive.  
- **Required fix:**  
  - Optionally, clarify in a table footnote which parameters are sampled in each model, for readers who consult only the table.

---

## 10. Duplicate phrases, internal tags, and stylistic issues

P2-N4 (NIT) – Internal-bookkeeping language and AI mention  
- **Location:** Acknowledgments, page 6  
- **Problem:**  
  - The Acknowledgments state: “The author acknowledges the use of AI research assistants during the analysis and manuscript preparation.” This is not a technical issue but may intersect with journal policy on AI usage disclosure.  
- **Required fix:**  
  - Check PRD’s current policy on AI tools; if disclosure is required, this is good. If additional detail (e.g., tool names, roles) is requested by APS, add it.  

P2-N5 (NIT) – “14-barrier catalog” unexplained  
- **Location:** Sec. 5, page 4  
- **Problem:**  
  - The phrase “14-barrier catalog” is introduced without explanation; presumably this is a concept introduced in Golden (2026a).  
- **Required fix:**  
  - Add a brief parenthetical explanation (“…14-barrier catalog (a classification of theoretical obstacles to ECH models, see Golden 2026a)”) or remove the phrase if not essential.

I did not find obvious duplicate-phrase glitches like “canonical canonical-mask” in the excerpted text.

---

## 11. Length vs. contribution

P2-M17 (MAJOR) – Paper length and scope vs. contribution  
- **Location:** Whole manuscript (6 pages in excerpt)  
- **Problem:**  
  - The core technical content is relatively modest: one phenomenological ALP model, a simple Gaussian summary-likelihood combination of two numbers, a small MCMC run, and a straightforward LiteBIRD forecast.  
  - The paper also attempts to connect to ECH gravity and a companion non-Gaussianity forecast, but those are only briefly sketched and rely on non-public companion papers.  
  - For PRD, the paper would benefit from either more depth (e.g., full EB-spectrum analysis, inclusion of systematics modeling, mass-dependence study comparable to Planck ALP constraints) or a more concise presentation focused on the main phenomenological point.  
- **Required fix:**  
  - Either (a) significantly expand the analysis (e.g., compare to current ALP mass constraints including 2506.20824, test sensitivity to cosmological parameters, provide a more robust MCMC exploration), or (b) shorten the manuscript to ≈4–5 pages, focusing tightly on the ALP prediction, the combined β constraint, and the LiteBIRD forecast, and omitting the ECH and matter-bounce tangents unless they are developed more fully.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper’s core idea—a Planck-scale ALP with Hubble-scale mass yielding a “natural” β ∼ 0.3° compatible with current birefringence hints—is interesting and relevant, but the current manuscript does not yet meet PRD standards. Several key citations (ACT DR6, Namikawa et al., companion papers) are incomplete or not verifiable; the Bayes factor and “naturalness” claims are under-documented; σ-values from different analyses are juxtaposed without adequate caveats; and the MCMC methodology is too thinly described for a high-precision inference paper. Substantial revision is needed to clarify the novelty relative to prior ALP-birefringence work, solidify the bibliographic and numerical foundations, and either deepen or streamline the analysis.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E5 (ESSENTIAL) – Incorrect σ-significance quoted for Planck NPIPE result  
- **Location:** Sec. 3.1, page 2  
- **Problem:**  
  - Text: “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11◦ (2.7σ).”  
  - Arithmetic check: 0.30 / 0.11 ≈ 2.73σ.  
  - If the author intends to quote the *rounded* significance corresponding to the given numbers, 2.7σ is consistent with 0.30 ± 0.11°. However, elsewhere the paper uses standard rounding (e.g., 0.242/0.061 ≈ 3.97 → “3.9σ”), and in the Introduction the earlier Planck HFI result is labeled 2.5σ for 0.35 ± 0.14°, where 0.35 / 0.14 = 2.50 exactly. This highlights that the σ labels are treated as derived quantities from β/σβ.  
  - The more serious issue is that the text *implicitly* mixes Eskilt’s quoted σ significance (based on their full likelihood) with a naïve β/σβ recomputation, but does not say which convention is used here. For Eskilt & Komatsu, the significance associated with 0.30 ± 0.11° may not be exactly 2.7σ, depending on the underlying posterior and any non-Gaussianity.  
- **Required fix:**  
  - State explicitly that “(2.7σ)” is computed as β/σβ from the quoted Gaussian error, not copied from Eskilt & Komatsu.  
  - Alternatively, if Eskilt & Komatsu quote a different σ for this exact result, adopt their σ and numbers consistently and say so.  
  - Add a short remark in Sec. 3.1 that “all σ values in this section are computed simply as β/σβ unless otherwise noted,” to avoid ambiguity.

P2-E6 (ESSENTIAL) – Unsupported claim that prediction “matches the combined Planck + ACT measurement at 1σ”  
- **Location:** Sec. 6, page 5  
- **Problem:**  
  - Text: “The prediction matches the combined Planck + ACT measurement at 1σ.”  
  - The prediction: βpred ≈ 0.27°.  
  - The combined summary-likelihood result: βcombined = 0.242 ± 0.061° (Sec. 3.2, Eq. 4).  
  - The difference: |0.27 − 0.242| = 0.028°. In units of the quoted σcombined: 0.028 / 0.061 ≈ 0.46σ.  
  - This is indeed *within* 1σ, but the phrase “matches … at 1σ” is ambiguous and could be read as implying a ≈1σ offset rather than ≈0.5σ. This is a quantitative comparison and should be stated precisely to avoid over- or under-stating tension.  
- **Required fix:**  
  - Replace with a precise quantitative statement, e.g.: “The prediction β ≈ 0.27° lies ≈0.5σ above the combined Planck + ACT measurement β = 0.242 ± 0.061°, well within 1σ.”  
  - This directly shows the delta and uncertainty, satisfying the journal’s requirement to quantify “consistent with” language.

P2-M10 (MAJOR) – “9σ exclusion” claim for LiteBIRD is overstated and not symmetric  
- **Location:** Sec. 4, page 3  
- **Problem:**  
  - Equation (10) defines “Significance = 0.27/0.03 = 9σ” for detecting the predicted β = 0.27° with σ(β) = 0.03°.  
  - Immediately after: “If LiteBIRD measures β = 0 ± 0.03◦ , the ALP explanation is excluded at 9σ.”  
  - Strictly, if the true model prediction is 0.27° and LiteBIRD measures β = 0 ± 0.03°, the discrepancy is |0.27 − 0| / 0.03 = 9σ, but this assumes the forecast σ applies *both* to detection and exclusion, and that the prediction has no theoretical uncertainty. The text does not acknowledge that the *model prediction* itself is approximate, based on order-unity parameters (C0, θi) and an approximate cosmological factor.  
  - Earlier, Sec. 2.2 presents β ≈ 0.27° as an order-of-magnitude estimate using “∆ϕ/fa ∼ 10−2” and “5×10−3 rad,” not as a sharp, zero-uncertainty prediction. Using that approximate value to claim a 9σ *exclusion* overstates the precision of the theory.  
- **Required fix:**  
  - Rephrase to emphasize the forecasted *experimental* sensitivity rather than a formal 9σ exclusion, e.g.: “LiteBIRD’s projected σ(β) ≈ 0.03° implies it can distinguish β ≈ 0.27° from β = 0 at ∼9σ, assuming the theoretical prediction is exact.”  
  - Add a sentence quantifying theoretical uncertainty (e.g., variation in β when C0, θi vary within “order-unity” priors) and note that the exclusion significance is limited by both experimental and theoretical uncertainties.  
  - Alternatively, phrase the second sentence more cautiously: “If LiteBIRD finds β consistent with zero at the 0.03° level, the simple ALP scenario considered here would be strongly disfavored.”

P2-M11 (MAJOR) – Dimensional/normalization ambiguity in Eq. (3) likelihood  
- **Location:** Sec. 3.2, Eq. (3), page 2  
- **Problem:**  
  - Likelihood is written as  
    \[
      L(β) = \prod_i \frac{1}{\sqrt{2\pi} σ_i} \exp\left[-\frac{(β_i^{\rm obs}-β)^2}{2σ_i^2}\right].
    \]  
    (as implied by the text, with β and σ in degrees).  
  - The paper implicitly treats β in *degrees* everywhere (e.g., β = 0.242 ± 0.061°), but does not state whether the Gaussian is defined in degrees or radians. Strictly, the Gaussian measure is dimensionful; using β in degrees is fine as long as all β and σ values are consistently in degrees, but this convention is never stated explicitly.  
  - This becomes important when relating β to gaγ and ∆ϕ, which are naturally defined in radians in Eq. (2); the mapping from the Gaussian β posterior (in degrees) to the coupling fphoton×C0 is not spelled out, and conversion factors of π/180 are not shown.  
- **Required fix:**  
  - Explicitly state the units used for β and σβ in the likelihood, e.g., “All angles are expressed in degrees in this section; the Gaussian likelihood is defined in degrees.”  
  - When connecting Eq. (4) to Eq. (5), add a short sentence describing the conversion: “We convert β from degrees to radians when relating it to the ALP coupling via β = ∆ϕ/(2fa).”  
  - This avoids hidden unit conversions and ensures dimensional consistency between statistical and theoretical quantities.

P2-M12 (MAJOR) – Potential inconsistency between “spectator” assumption and implicit energy density  
- **Location:** Sec. 2.1–2.2, pages 1–2  
- **Problem:**  
  - The ALP is described as a “spectator” field that “does not participate in the bounce dynamics, does not generate perturbations, and does not require a contracting phase” (Sec. 5).  
  - However, the potential V(ϕ) = m²f_a²(1−cos(ϕ/fa)) with m ∼ H0 and fa ∼ MPl implies an energy scale comparable to the present critical density if θi ∼ O(1) and the field is still slowly rolling today. That is, for m ∼ H0, ρϕ ∼ m²f_a²θ_i² ∼ H0² MPl² ∼ ρcrit, making the ALP a dark-energy–like component rather than a negligible “spectator.”  
  - The text does not check or even comment on whether the assumed parameter values imply a non-negligible contribution to the background expansion. Calling the field a “spectator” without quantifying its fractional energy density is potentially misleading.  
- **Required fix:**  
  - Estimate the ALP energy density ρϕ for m ∼ H0, fa ∼ MPl, θi ∼ 1 and compare it to the critical density today, e.g., compute Ωϕ = ρϕ/ρcrit.  
  - Clarify whether the model assumes the ALP is (a) responsible for dark energy (Ωϕ ≈ 0.7) or (b) a subdominant component (e.g., Ωϕ ≪ 1) via some additional tuning (e.g., smaller θi or effective mass).  
  - If the ALP is truly spectator-level, state explicitly what range of θi or C0 is required to keep its energy density subdominant, and how that affects the birefringence prediction.

P2-M13 (MAJOR) – Internal cross-reference ambiguity for “Sec. 3.4” mention in abstract  
- **Location:** Abstract, page 1  
- **Problem:**  
  - Abstract: “The Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).”  
  - Sec. 3.4 indeed defines ln B and gives values for different priors, but does not explicitly label the quoted value as “indicative” or provide an error estimate on ln B. The wording “indicative; prior-dependent” appears only in the abstract, not in Sec. 3.4 itself.  
  - This creates a minor cross-reference mismatch: the reader is referred to Sec. 3.4 for the details underlying “indicative; prior-dependent,” but Sec. 3.4 only mentions prior dependence and provides alternative ln B values, without explaining *why* the quoted 5.17 should be viewed as “indicative” (e.g. due to finite chain length, prior range choice, or Gaussian approximation).  
- **Required fix:**  
  - In Sec. 3.4, explicitly echo the abstract’s qualifier, e.g.: “These Bayes factors should be regarded as indicative, since they depend on the chosen prior range for β and are computed from chains with modest effective sample size.”  
  - This makes the abstract’s description directly supported by the body at the referenced location.

P2-M14 (MAJOR) – Figure 2 caption vs. body claim lacks quantitative comparison  
- **Location:** Figure 2 caption, Sec. 3.3 text, page 4  
- **Problem:**  
  - Fig. 2 caption: “All three [posteriors] are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.”  
  - Sec. 3.3:  
    - βALP = 0.336 ± 0.107° (Run 1)  
    - βfree = 0.344 ± 0.096° (Run 3)  
    - Observed βobs = 0.342 ± 0.094° (Eskilt joint).  
  - The phrase “consistent with each other” is accurate, but the caption and body do not quantify the differences, which are small but non-zero. For example:  
    - |0.336 − 0.342| / √(0.107² + 0.094²) ≪ 1σ  
    - |0.344 − 0.342| / √(0.096² + 0.094²) ≪ 1σ  
  - Under the journal’s explicit guidance to scrutinize phrases like “consistent with” and “no tension,” these qualitative statements should be backed by basic Δ/σ estimates, at least once in the body where Fig. 2 is discussed.  
- **Required fix:**  
  - Add a quantitative comparison in Sec. 3.3 when introducing Fig. 2, e.g.: “The ALP and free-β posteriors differ from βobs by less than 0.1σ, confirming that all three are statistically indistinguishable at current precision.”  
  - This supports the caption’s claim with explicit numbers.

P2-N2 (NIT) – Abstract vs. Conclusion wording mismatch on “decisive” vs. “contingent” LiteBIRD test  
- **Location:** Abstract, page 1; Conclusion, page 6  
- **Problem:**  
  - Abstract: “LiteBIRD, with σ(β) ≈ 0.03◦ , will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.”  
  - Conclusion: “LiteBIRD will provide a decisive test at ∼ 9σ statistical significance, *contingent on the self-calibration strategy and systematic error budget*.”  
  - The abstract omits this contingency, presenting the 9σ test as unconditional, while the conclusion correctly notes dependence on systematics and calibration. This is a mild internal inconsistency between the two summaries of the same forecast.  
- **Required fix:**  
  - Insert a brief qualifier in the abstract mirroring the conclusion, e.g.: “…at 9σ significance, assuming LiteBIRD achieves σ(β) ≈ 0.03° under its planned self-calibration and systematic control.”  
  - This keeps the abstract faithful to the more nuanced statement in the conclusion.

P2-N3 (NIT) – “Naturalness” claim not quantitatively backed  
- **Location:** Abstract, Sec. 2.2, Sec. 6  
- **Problem:**  
  - Multiple statements assert that the prediction is “natural” and involves “no fine-tuning” because fa ∼ MPl, m ∼ H0, θi ∼ O(1), C0 ∼ O(1).  
  - However, the paper does not quantify how much variation in θi and C0 is allowed by the data (beyond the Run 2 product Caγ × θi = 3.4 ± 1.1), nor does it measure a fraction of parameter space that yields β in the observed range. Without some simple measure of allowed ranges, “no fine-tuning” remains qualitative.  
- **Required fix:**  
  - Add a brief quantitative statement, e.g., “For θi and C0 each uniformly distributed between 0.3 and 3, we find that X% of the parameter volume yields β in the observed range within 1σ.” Even a simple back-of-the-envelope estimate would make the “no fine-tuning” claim more concrete.  
  - Alternatively, soften the language slightly to “no apparent fine-tuning” or “no extreme tuning,” unless a quantitative argument is provided.

If you want, I can now go through each displayed equation one-by-one and do a more explicit dimensional check, but the items above are the new issues that stand out relative to the initial review.