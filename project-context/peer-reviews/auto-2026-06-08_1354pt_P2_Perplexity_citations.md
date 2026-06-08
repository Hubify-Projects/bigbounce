# P2 auto-2026-06-08_1354pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13660 chars)
**Wall time**: 77.3s

---

P2-E1 (ESSENTIAL) – Global: Missing actual PDF / unverifiable claims  
- **Location:** Entire manuscript (no page numbers beyond those in user paste)  
- **Problem:** I only have access to the text pasted in the prompt, not the actual rendered PRD-style PDF with figure axes, tables, and full reference metadata. I therefore **cannot** check: (i) axis labels, units, and numbers on Figures 1–2; (ii) table layout beyond the textual stub of Table 1; (iii) typographical details in equations; (iv) full reference entries (journal volume, pages) as they would appear in the PDF. This violates the review instructions to “examine every figure, table, equation, caption…”.  
- **Required fix:** Editorial/logistical: provide the full rendered PDF (or ensure that it matches exactly the text provided) for a final citation/consistency audit before acceptance. The scientific findings below assume the pasted text is an accurate representation of the manuscript.

Below I proceed with what *can* be checked from the supplied text and real-time searches of arXiv/ADS.

---

## 1. Citation forensics and reference accuracy

### 1.1 Minami & Komatsu (2020)

P2-E2 (ESSENTIAL) – Incorrect / incomplete statistic for Minami & Komatsu result  
- **Location:** p.1, Introduction  
- **Text:** “The Planck HFI analysis [Minami and Komatsu, 2020] reported β = 0.35 ± 0.14◦ (2.5σ)….”  
- **Check:** Minami & Komatsu, Phys. Rev. Lett. 125, 221301 (2020) report a birefringence angle \( \beta = 0.35 \pm 0.14^\circ\), consistent with a 2.5σ deviation from zero (0.35/0.14 ≈ 2.5), matching the manuscript’s numbers and significance.[1]  
- **Finding:** Numerically consistent and traceable. No fix needed.

P2-N1 (NIT) – Journal field abbreviated inconsistently  
- **Location:** References  
- **Text:** “Physical Review Letters, 125:221301, 2020. doi: 10.1103/PhysRevLett.125.221301.”  
- **Problem:** PRD typically uses “Phys. Rev. Lett.”; elsewhere “Physical Review D” is written out.  
- **Required fix:** Harmonize journal abbreviations to PRD style (e.g., “Phys. Rev. Lett. 125, 221301 (2020)”).

### 1.2 Eskilt & Komatsu (2022)

P2-M1 (MAJOR) – Possibly inaccurate description of data set and numbers  
- **Location:** p.1, Introduction; p.2–3, Data and Inference; References  
- **Text:**  
  - “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11◦ (2.7σ)”  
  - “For the MCMC parameter estimation (Sec. 3.3), we use the Eskilt et al. joint analysis value βobs = 0.342 ± 0.094◦ …”  
  - Reference entry: “J. R. Eskilt and E. Komatsu. Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data. Physical Review D, 106:063503, 2022.”  
- **Check:** The cited paper is Phys. Rev. D 106, 063503 (2022), “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data.” The abstract quotes \( \beta = 0.342^\circ \pm 0.091^\circ\) for the joint analysis; the main text also contains values around 0.30° with ~0.11° uncertainty for certain subsets.[2]  
- **Findings:**  
  - The joint-analysis value in the manuscript is \(0.342 \pm 0.094^\circ\); the published value is \(0.342 \pm 0.091^\circ\).[2] The difference is small but **not identical** to the canonical number and should be justified or corrected.  
  - The “Planck NPIPE” number \(0.30 \pm 0.11^\circ\) is plausible and close to values in Eskilt & Komatsu, but the exact origin (which combination, which multipole cuts) is not explained.  
- **Required fix:**  
  - Either (a) use the exact published numbers from Eskilt & Komatsu (e.g., \(0.342 \pm 0.091^\circ\)) and specify which data subset produces \(0.30 \pm 0.11^\circ\), with exact citation to the table/figure and sub-data-set used, or (b) explicitly state that you re-analyzed their publicly released likelihoods and obtained slightly different error bars, and document that procedure.  
  - If you are not reanalyzing, do not round or alter reported uncertainties without explanation.

### 1.3 ACT DR6 “Diego-Palazuelos and Komatsu, 2025”

P2-E3 (ESSENTIAL) – Likely non-existent / future-dated citation with fused metadata  
- **Location:** p.2, Sec. 3.1; References  
- **Text:**  
  - Dataset bullet: “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074◦ (2.9σ)”  
  - Reference entry: “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”  
- **Check:** Searching arXiv/ADS for “Diego-Palazuelos birefringence ACT” and “Cosmic birefringence from the Atacama Cosmology Telescope” returns no such preprint or publication.[3] The closest real works include ACT polarization analyses but not a birefringence paper with these authors and year.  
- **Finding:** As of the current date, no arXiv/ADS record exists for this claimed work. The arXiv ID is not given, but the reference strongly resembles a fabricated or anticipated preprint. The numerical value \(0.215 \pm 0.074^\circ\) has no verifiable source.  
- **Required fix:**  
  - Either provide a valid arXiv ID and confirm that the title, authors, and year exactly match the cited preprint, and that the number \(0.215 \pm 0.074^\circ\) is explicitly present in that paper’s tables/abstract; or  
  - If the work is not yet on arXiv/ADS, **it cannot be cited as an “arXiv preprint”** and its numbers cannot be used as a load-bearing data point in PRD. Remove this reference and all uses of its numbers from the analysis until it is publicly available.  
  - If internal collaboration numbers were used, the paper must clearly state they are private communication, and PRD will typically not allow them to be used as primary data.

### 1.4 LiteBIRD Collaboration (2023)

P2-M2 (MAJOR) – Forecast value must be traceable to specific statement  
- **Location:** p.3–4, Sec. 4; References  
- **Text:** “LiteBIRD is projected to achieve σ(β) ≈ 0.03◦ on the isotropic birefringence angle [LiteBIRD Collaboration, 2023]…”  
- **Check:** The cited paper is: “LiteBIRD science goals and forecasts: a full-sky CMB polarization survey,” Prog. Theor. Exp. Phys. 2023, 042F01.[4] That paper contains various forecast errors for birefringence-like parameters depending on calibration assumptions; however, there is no standard “σ(β) = 0.03°” quoted as a single robust number. Values depend on self-calibration vs external angle calibration, sky fraction, and systematics.[4]  
- **Finding:** A single σ(β) ≈ 0.03° is at best a representative value; as written, it suggests a definitive forecast.  
- **Required fix:**  
  - Cite the exact table or equation from the LiteBIRD paper (or related technical forecast) from which 0.03° is derived, and clarify the assumptions (e.g., external calibrator, no residual systematics).  
  - If 0.03° is your own forecast using LiteBIRD sensitivity numbers, not the collaboration’s, say so explicitly: “Using LiteBIRD’s forecast noise levels from [LiteBIRD Collab. 2023], we estimate σ(β) ≈ 0.03° under XYZ assumptions.”

### 1.5 Fujita et al. (2021)

P2-M3 (MAJOR) – Misrepresented novelty and parameter choices  
- **Location:** p.5, Discussion; References  
- **Text:** “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3◦ …” and “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy. Physical Review D, 103:043509, 2021.”  
- **Check:** Fujita et al., Phys. Rev. D 103, 043509 (2021) indeed study ALPs with photon coupling and show that the reported cosmic birefringence can be explained for certain ALP parameter ranges, including Planck-scale decay constants in some scenarios.[5] They discuss ALPs as dark energy–like fields; the exact phrasing “Planck-scale ALP naturally produces β ∼ 0.3°” is an interpretation, not a literal quote.  
- **Finding:**  
  - The bibliographic info and DOI (10.1103/PhysRevD.103.043509) are correct.  
  - The manuscript’s novelty claim must be more precise: Fujita et al. already consider Planck-scale \(f_a\) and use cosmic birefringence as a probe. Your claim that your contribution is “not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0)” should explicitly explain how this differs from their parameter space and whether they already included similar mass scales.  
- **Required fix:**  
  - Tighten the novelty statement, making clear exactly what is new relative to Fujita et al. and ensuring you do not overstate originality. Provide explicit parameter ranges from Fujita et al. to show the difference, or rephrase to: “Our work is conceptually similar to Fujita et al. [2021] but focuses on the special case \(m \sim H_0\) with spectator dynamics and provides a tailored summary-likelihood inference.”

### 1.6 Namikawa et al. (2025) – “In preparation”

P2-E4 (ESSENTIAL) – Fabricated or non-verifiable “in preparation” reference  
- **Location:** p.5, Discussion; References  
- **Text:** “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints…”, reference: “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  
- **Check:** Searches on arXiv and ADS for “Constraints on axion-like particles from cosmic birefringence” with these authors show a 2025 arXiv preprint “Planck constraints on axion-like particles through isotropic cosmic birefringence,” which is actually authored by a different set of authors and is not by Namikawa et al.[1][4][5] There is no arXiv record matching the given author list and title. “Naokawa” appears to be a misspelling of Namikawa in the manuscript itself.  
- **Finding:**  
  - The reference appears to be a placeholder for a non-public or non-existent manuscript (“in preparation”), with mis-spelled author names and no arXiv ID.  
  - PRD does not accept “in preparation” as a basis for quantitative comparison, especially for *constraints* that you rely on to set context.  
- **Required fix:**  
  - If such a paper exists by the time of publication, replace “in preparation” with the actual arXiv ID and full journal details, correct the title and authors, and ensure that the mass constraints you describe are explicitly present there.  
  - If not, remove this reference or demote it to “private communication” *without* quoting numerical constraints that cannot be checked.  
  - Correct the typo “Naokawa” → “Namikawa” in any case.

### 1.7 Golden (2026a, 2026b) – Companion “submitted simultaneously”

P2-E5 (ESSENTIAL) – Unverifiable companion papers used as scientific support  
- **Location:** p.5, Discussion; p.5, Relationship to Bounce Cosmology; References  
- **Text:**  
  - “see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog.”  
  - “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”  
  - References:  
    - “Houston Golden. Spin-torsion cosmology and the search for geometric dark energy: Structural barriers, perturbation transparency, and surviving predictions. Companion paper, submitted simultaneously, 2026a.”  
    - “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.”  
- **Check:** Searches on arXiv/ADS for these titles and author yield no records. The papers are not on arXiv and are not identifiable as submitted to any journal.  
- **Finding:** These are internal companion manuscripts “submitted simultaneously”, not public. Their results are invoked for ECH gravity context and for the matter-bounce fNL = −35/8 statement.  
- **Required fix:**  
  - If these companion papers are not yet publicly available (arXiv or journal), you cannot rely on them for key theoretical support (e.g., “14-barrier catalog” or “fNL = −35/8” test) beyond a brief qualitative remark. For any quantitative prediction (such as the exact value of fNL = −35/8), either derive it in this paper or refrain from quoting it as an established result.  
  - At minimum, clearly state that these are unpublished works “in preparation” and remove any impression that their results are established or peer-reviewed. PRD may request that you upload them to arXiv as companion papers or remove them entirely.

---

## 2. Numerical and statistical consistency

### 2.1 Abstract: βobs = 0.342 ± 0.094° (3.6σ), βcombined = 0.242 ± 0.061°

P2-M4 (MAJOR) – Inconsistent significance quoted vs recomputed values  
- **Location:** Abstract and throughout Sec. 3  
- **Text:**  
  - Abstract: “βobs = 0.342 ± 0.094◦ from the Eskilt et al. joint Planck + ACT analysis” and “3.6σ isotropic birefringence signal.”  
  - Eq. (4): “βcombined = 0.242 ± 0.061◦ (3.9σ from zero).”  
- **Check:**  
  - From the manuscript’s own numbers: 0.342 / 0.094 ≈ 3.64, so “3.6σ” is consistent with the quoted mean/σ in the text of the paper.  
  - For the combined estimate: 0.242 / 0.061 ≈ 3.97, which rounds to ~4.0σ. The manuscript says 3.9σ, which is acceptable rounding.  
- **Finding:** Internal consistency holds between quoted means and significances; however, the slight deviation from the canonical Eskilt uncertainty (±0.091°) needs justification (see P2-M1).  
- **Required fix:** Clarify whether 0.094° is your own rederived uncertainty vs the published 0.091°, and specify how it was obtained.

### 2.2 Summary-likelihood combination

P2-M5 (MAJOR) – Combined β and σ not explicitly traced to individual inputs  
- **Location:** Sec. 3.2, Eq. (3)–(5)  
- **Text:**  
  - Inputs: β1 = 0.30 ± 0.11°, β2 = 0.215 ± 0.074°.  
  - Output: “βcombined = 0.242 ± 0.061°.”  
  - Coupling: “fphoton × C0 = 1.73 ± 0.44.”  
- **Check:** Using standard inverse-variance weighting for β1 = 0.30 ± 0.11, β2 = 0.215 ± 0.074:  
  - \(w_1 = 1/0.11^2 ≈ 82.64\), \(w_2 = 1/0.074^2 ≈ 182.5\). Total weight ≈ 265.1.  
  - Combined β: \((0.30 w_1 + 0.215 w_2)/ (w_1 + w_2) ≈ (24.8 + 39.2)/265.1 ≈ 0.2414°\).  
  - Combined σ: \(1/\sqrt{w_1 + w_2} ≈ 1/\sqrt{265.1} ≈ 0.0613°\).  
  These match Eq. (4) well.  
- **Finding:** Mathematically consistent given the two input measurements. The issue is the *second input* is unverified (P2-E3). Hence βcombined and fphoton × C0 are not reliably supported.  
- **Required fix:** Once the ACT DR6 result is correctly referenced (or removed), recompute βcombined and fphoton × C0 and update Eq. (4)–(5) accordingly. If only Planck data are used, state that clearly.

### 2.3 βALP and βfree posteriors vs βobs

P2-M6 (MAJOR) – Precision claims vs small MCMC sample sizes  
- **Location:** Sec. 3.3–3.4, Table 1, Eqs. (6)–(8)  
- **Text:**  
  - “We acknowledge that these sample sizes (720–6,840 accepted samples) are modest…”  
  - “The posterior on β from the ALP model (Run 1): βALP = 0.336 ± 0.107◦; βfree = 0.344 ± 0.096◦ and βobs = 0.342 ± 0.094◦.”  
- **Check:** The differences between βALP, βfree, and βobs are ~0.006–0.008°, which is an order of magnitude smaller than the quoted 1σ uncertainties (~0.1°). Given Neff ~ 1000, the statistical precision of the *posterior mean* is fine, but the reliability of tails and evidence (ln B = 5.17) is weaker, as the author notes.  
- **Finding:** The consistency statements are correct (all within 0.1σ), but the evidence calculation may be under-resolved.  
- **Required fix:**  
  - Temper statements about Bayes factor significance (e.g., “indicative evidence”) and explicitly note that ln B = 5.17 is subject to ~O(1) uncertainty given limited chain lengths.  
  - Provide at least an approximate error on ln B or repeat the computation with longer chains, or use a simpler analytic approximation from the Gaussian summary-likelihood to cross-check.

### 2.4 Bayes factor and priors

P2-M7 (MAJOR) – Incomplete description of prior choice and dependence  
- **Location:** Sec. 3.4, Eq. (9)  
- **Text:** “ln B = 5.17…computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°]. The evidence is prior-dependent: ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].”  
- **Check:** For a Gaussian likelihood centered at β = 0.242° with σ = 0.061°, naive Bayes factor estimates for H1 (β free) vs H0 (β = 0) typically yield ln B of order a few, depending on prior width. The reported numbers are plausible.  
- **Finding:** Qualitatively consistent but not traceable to a specific analytic formula in the text. The word “indicative” is present, which is appropriate.  
- **Required fix:**  
  - Provide the explicit formula used for the Savage–Dickey ratio in this 1D Gaussian case and show the numbers briefly, so readers can reproduce ln B without access to your MCMC code.  
  - Clarify whether β was sampled in degrees or radians in the MCMC, as this affects the prior normalization.

### 2.5 LiteBIRD 9σ forecast

P2-N2 (NIT) – Simple ratio correct  
- **Location:** Sec. 4, Eq. (10)  
- **Text:** “Significance = 0.27 / 0.03 = 9σ.”  
- **Check:** 0.27 / 0.03 = 9 exactly; consistent.  
- **Finding:** No issue with the simple arithmetic. The caveat is the underlying σ(β) assumption (see P2-M2).

---

## 3. Equations and dimensional consistency

### 3.1 Eq. (1): Field displacement

P2-M8 (MAJOR) – Use of Bessel J0(m/H0) without derivation or reference  
- **Location:** Sec. 2.1, Eq. (1)  
- **Text:**  
  - “The field displacement from recombination to today is: Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) ≈ fa θi × O(1). For m/H0 ∼ 1, 1 − J0(1) ≈ 0.24.”  
- **Check:**  
  - J0(0) = 1, J0(1) ≈ 0.765, so 1 − J0(1) ≈ 0.235, consistent with “≈ 0.24”.  
  - However, no derivation is shown for why the solution for Δϕ in a time-varying Hubble background yields precisely this Bessel function combination.  
- **Finding:**  
  - The dimensional form is fine (Δϕ has dimension of field, fa θi has same), but the explicit J0 dependence is nonstandard and not referenced to any prior work.  
- **Required fix:**  
  - Either supply a short derivation in an appendix or explicitly reference a paper where this Bessel-function solution is derived for an ALP with \(m \sim H_0\) in a ΛCDM background.  
  - If this is a heuristic approximation, label it as such and avoid presenting it as an exact expression.

### 3.2 Eq. (2): Rotation angle

P2-M9 (MAJOR) – Ambiguous definitions of C0, Caγ, C, fphoton  
- **Location:** Sec. 2.2, Eq. (2); Sec. 3.3; Table 1; Eq. (5)  
- **Text:**  
  - “β = gaγ Δϕ / 2 = C0 Δϕ / (2 fa).”  
  - Later: Priors include “Caγ flat on [1, 30] (Run 2 only)”.  
  - Eq. (5): “fphoton × C0 = 1.73 ± 0.44.”  
  - Table 1: “ALP (C = 8 fixed)” but C is never defined in the main text.  
- **Check:** The standard ALP-photon coupling is L ⊃ (gϕγγ / 4) ϕ F F̃, with gϕγγ ∝ C / fa. Here, the notation alternates between C0, Caγ, C and fphoton without clear definitions or mapping.  
- **Finding:** Notation is internally inconsistent and will confuse readers. It also obscures how Eq. (5) is derived from Eqs. (2) and (4).  
- **Required fix:**  
  - Introduce **one consistent notation**: e.g., \(g_{\phi\gamma\gamma} = C_\gamma / f_a\) and define fphoton if different.  
  - Explicitly define: C0, Caγ, C, and fphoton, and explain their relationships (e.g., is fphoton simply fa, or fa in units of 10^18 GeV?).  
  - Show the explicit algebra relating β, Δϕ/fa, and the inferred coupling so that \(f_{\text{photon}} \times C_0 = 1.73 \pm 0.44\) is reproducible from the preceding numbers.

### 3.3 Eq. (3): Likelihood

P2-N3 (NIT) – Minor typographical clutter in Eq. (3)  
- **Location:** Sec. 3.2, Eq. (3)  
- **Text:** The product over i and exponent are correct but formatted awkwardly: \( \prod_i \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp[-(β_i^{obs} − β)^2 / (2 σ_i^2)]\).  
- **Finding:** Dimensionally correct, standard Gaussian combination.  
- **Required fix:** Optionally simplify notation (drop redundant parentheses) for readability.

---

## 4. Figures, tables, and axes

Because I cannot see the actual rendered Figures 1–2, I can only flag issues evident from the captions and surrounding text.

### 4.1 Figure 1: Triangle plot

P2-M10 (MAJOR) – Missing explicit axis labels and units in text description  
- **Location:** Figure 1 caption, p.4  
- **Text:** “Triangle plot from the extended ALP MCMC (Run 2, C free). The posterior on the coupling-misalignment product Caγ × θi is centered at 3.4 ± 1.1…”  
- **Finding:**  
  - The caption does not mention β, m, or priors; the text suggests that only Caγ × θi is highlighted.  
  - It is not clear whether axes are labeled with units (e.g., log10(m/eV)) and whether priors vs posteriors are indicated.  
- **Required fix:**  
  - Ensure axes in the actual figure have clear labels (including units) for all plotted 1D marginals: θi (dimensionless), log10(m/eV), Caγ (dimensionless), Caγ θi (dimensionless), and β (degrees).  
  - Add to the caption a brief mention of all parameters shown and the priors used so the triangle plot is interpretable.

### 4.2 Figure 2: β posterior comparison

P2-M11 (MAJOR) – Potential side-by-side comparison of non-comparable σ values (PRD requirement 7)  
- **Location:** Figure 2 caption, p.5  
- **Text:** “Comparison of β posteriors across all three model configurations (ALP with C = 8 fixed, ALP with C free, and model-independent β). All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094◦.”  
- **Finding:**  
  - The three β posteriors are derived from different models with different priors and nuisance parameters. By the journal’s review instruction, **sigma values from different null procedures shown side-by-side must be explicitly noted as not directly comparable wherever juxtaposed.**  
  - The caption and text simply say “consistent,” but do not warn that the widths and shapes of these posteriors are prior/model dependent and should not be naively compared as pure “significance” metrics.  
- **Required fix (ESSENTIAL under instruction 7):**  
  - In both the caption and the main text around Eqs. (6)–(7), explicitly state something like: “These σ values arise from different model assumptions and priors and are therefore **not directly comparable** as measures of detection significance.”  
  - Make clear that βobs is from a different analysis pipeline (Eskilt & Komatsu), so its quoted σ should not be directly compared to your model σ without this caveat.

### 4.3 Table 1: MCMC run configurations

P2-N4 (NIT) – Limited usefulness  
- **Location:** p.2–3  
- **Text:** Table 1 with Runs, Samples, R̂ − 1, Status.  
- **Finding:** The table provides useful diagnostics but no units or information about burn-in length or proposal distributions. This is acceptable but somewhat bare-bones.  
- **Required fix:** Optionally add a note clarifying that “Samples” denotes post–burn-in accepted samples per chain (or total across chains).

---

## 5. Claims of novelty, “naturalness,” and “no fine-tuning”

### 5.1 “Natural prediction without fine-tuning”

P2-M12 (MAJOR) – Overstated “no fine-tuning” claim  
- **Location:** Abstract; Sec. 2.2; Sec. 6; Conclusion  
- **Text:**  
  - Abstract: “order-unity inputs… naturally accommodates β ≈ 0.27°… no fine-tuning.”  
  - Sec. 2.2: “no small or large numbers beyond the cosmological integration factor. Every input is O(1)…”  
  - Sec. 6: “The ALP birefringence prediction β ≈ 0.27◦ has… Naturalness: All input parameters… are at their natural scales. No tuning is required.”  
- **Finding:**  
  - While fa ~ MPl and m ~ H0 are aesthetically appealing, **naturalness** is a concept with multiple technical definitions. The requirement that θi ∼ O(1) but not extremely close to π, and that the ALP begins rolling near z ~ 1 to yield the observed β, does represent a selection in parameter space.  
  - Other works have considered similar parameter ranges and do not always claim “no fine-tuning” unconditionally.  
- **Required fix:**  
  - Soften the language: instead of “no fine-tuning” say “no apparent extreme fine-tuning of dimensionless parameters is needed; \(f_a \sim M_{\rm Pl}\), \(m \sim H_0\), and \(\theta_i \sim \mathcal{O}(1)\) suffice to reproduce the observed β.”  
  - Acknowledge that this is an *order-of-magnitude* naturalness argument, not a rigorous Bayesian naturalness measure.

### 5.2 “Our contribution is not the model itself…”

P2-M13 (MAJOR) – Novelty claim vs existing ALP birefringence literature  
- **Location:** Sec. 6, last paragraph  
- **Text:** “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction…”  
- **Check:** Fujita et al. (2021) and other ALP birefringence works have already highlighted that Planck-scale ALPs with dark-energy-like masses can explain the observed β.[5][6] Later works (including 2025 arXiv/PRD articles) also perform detailed constraints on ALP mass vs coupling using full EB spectra.[1][6]  
- **Finding:** This statement risks overstating novelty.  
- **Required fix:**  
  - Revise to something like: “In line with Fujita et al. [2021] and related work, we emphasize the particularly simple parameter choice \(f_a \sim M_{\rm Pl}, m \sim H_0\) and demonstrate via a summary-likelihood combination of Planck and (putative) ACT constraints that this choice provides a good fit without extreme parameter tuning.”  
  - Acknowledge that the qualitative idea—Planck-scale ALP explaining β—is not new.

---

## 6. Miscellaneous issues

### 6.1 Duplicate / odd phrases

P2-N5 (NIT) – Repetition of “prediction is independent”  
- **Location:** Abstract; Sec. 5  
- **Text:** Abstract: “This birefringence prediction is independent of bounce cosmology and can be tested regardless…” Sec. 5 repeats essentially the same statement.  
- **Finding:** Slight redundancy; not the “canonical canonical-mask” type duplication but stylistically repetitive.  
- **Required fix:** Optionally consolidate to a single clear statement of independence from the bounce scenario.

### 6.2 “14-barrier catalog”

P2-M14 (MAJOR) – Unexplained specialized term  
- **Location:** Sec. 5, last sentence  
- **Text:** “…for the full ECH framework and 14-barrier catalog.”  
- **Finding:** The term “14-barrier catalog” is unexplained in this paper and refers to an unpublished companion work.  
- **Required fix:** Either briefly explain what “14 barriers” refers to or remove the phrase. Without the companion paper publicly available, this reads like opaque jargon.

### 6.3 Use of AI assistants

P2-N6 (NIT) – Acknowledgment wording  
- **Location:** Acknowledgments  
- **Text:** “The author acknowledges the use of AI research assistants during the analysis and manuscript preparation.”  
- **Finding:** This is acceptable, but some journals now request more specific description of AI use (e.g., which parts).  
- **Required fix:** Check PRD’s latest policy; if required, clarify whether AI tools were used only for language editing or also for data analysis.

---

## Summary recommendation

**MAJOR REVISIONS**

The current manuscript relies on at least one apparently non-existent ACT DR6 birefringence preprint and on multiple non-public “in preparation” works for both data input and theoretical context, which is incompatible with PRD standards. There are also notation inconsistencies, overstated naturalness/novelty claims, and incomplete documentation of how key numbers (e.g., βcombined, fphoton × C0, ln B) are derived from cited works. Once the unverifiable citations are either replaced with real published/preprint results or removed, the analysis recomputed accordingly, and the statistical and theoretical claims tightened and clearly linked to public sources, the core idea may be suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E6 (ESSENTIAL) – Figure 1 is described as a **triangle plot**, but the manuscript provides no accessible axis labels, parameter ranges, or contour levels to verify the caption-body match  
- **Location:** Figure 1 caption; Sec. 3.3 text  
- **Problem:** The caption says the figure is a “Triangle plot from the extended ALP MCMC (Run 2, C free),” and the body says the posterior on \(C_{a\gamma}\times\theta_i\) is centered at \(3.4 \pm 1.1\). However, the supplied manuscript text does **not** specify the plotted parameters, axis units, prior bounds, or whether the triangle plot shows 1D marginals and 2D contours in degrees, radians, or dimensionless variables.  
- **Required fix:** State the exact parameters on each axis, their units, and the contour credibility levels in the caption or main text so the figure can be checked against the claims.

P2-M8 (MAJOR) – Figure 1 claims a centered posterior value, but the caption’s wording slightly overstates what is shown  
- **Location:** Figure 1 caption  
- **Problem:** The caption says the posterior “is centered at \(3.4 \pm 1.1\), consistent with order-unity natural values.” A triangle plot typically shows a distribution, not a single centered value unless the posterior mean/median is overplotted or explicitly reported. The text does not say whether \(3.4 \pm 1.1\) is the posterior mean, median, or best fit.  
- **Required fix:** Identify the summary statistic used and, if the plot includes a point estimate or best-fit marker, say so explicitly.

P2-E7 (ESSENTIAL) – Figure 2 caption/body mismatch on what is being compared  
- **Location:** Figure 2 caption; Sec. 3.3 and Sec. 4 text  
- **Problem:** The caption says Figure 2 compares “all three model configurations (ALP with \(C=8\) fixed, ALP with \(C\) free, and model-independent \(\beta\)).” The body, however, only gives explicit posterior values for Run 1 (\(\beta_{\rm ALP}=0.336\pm0.107^\circ\)), Run 3 (\(\beta_{\rm free}=0.344\pm0.096^\circ\)), and the observed value \(\beta_{\rm obs}=0.342\pm0.094^\circ\). The manuscript never explicitly states the posterior summary for Run 2 in the same way, even though Figure 2 says it is included.  
- **Required fix:** Provide the Run 2 posterior summary in the body or clarify that Figure 2 includes the full distribution without a quoted 1D summary.

P2-M9 (MAJOR) – Figure 2 appears to compare posteriors derived from **different null procedures**, but the manuscript does not flag this as non-comparable  
- **Location:** Figure 2 caption; Sec. 3.1–3.3  
- **Problem:** The plotted quantities mix an MCMC-derived model posterior, a model-independent fit, and the externally quoted \( \beta_{\rm obs}\) from Eskilt et al. The manuscript does state that \(\beta_{\rm obs}\) “differs because it fits the full EB cross-spectrum rather than combining point estimates,” but the figure caption still describes them as directly comparable posterior curves.  
- **Required fix:** Explicitly state that the curves arise from *different inference pipelines* and are therefore not identical statistical objects, even if numerically close.

P2-M10 (MAJOR) – Equation (1) is dimensionally under-explained and the displayed Bessel form is not derived from the stated assumptions  
- **Location:** Sec. 2.1, Eq. (1)  
- **Problem:** The left-hand side \(\Delta\phi\) has field dimensions, and the right-hand side \(f_a\theta_i\left(1-J_0(m/H_0)/J_0(0)\right)\) also has field dimensions, so the equation is dimensionally consistent. But the manuscript gives no derivation for why the time evolution in a \(\Lambda\)CDM background should yield a \(J_0(m/H_0)\) factor, and the text says only that “the precise value depends on the cosmological integration through the matter and dark-energy eras.”  
- **Required fix:** Add a derivation, approximation scheme, or explicit citation for this Bessel-function expression. Without that, the formula reads like an asserted fit rather than a derived result.

P2-M11 (MAJOR) – Eq. (2) uses an internal notation chain that is not fully defined, which breaks reproducibility  
- **Location:** Sec. 2.2, Eq. (2); Sec. 3.3; Table 1  
- **Problem:** The manuscript uses \(g_{a\gamma}=C_0/f_a\), then later introduces \(C\) in “ALP (\(C=8\) fixed)” and \(C_{a\gamma}\) in the prior list, and finally reports \(f_{\rm photon}\times C_0 = 1.73\pm0.44\). The notation is not mapped cleanly from one symbol to the next, so the relation between the plotted/inferred variables and the physical coupling is ambiguous.  
- **Required fix:** Define every coupling symbol once, state whether \(C\), \(C_0\), and \(C_{a\gamma}\) are identical or distinct, and show the algebra connecting them to the reported \(f_{\rm photon}\times C_0\).

P2-E8 (ESSENTIAL) – Table 1 contains a parameter label, “\(C\)”, that is never defined in the text  
- **Location:** Table 1; Sec. 3.3  
- **Problem:** Table 1 lists “ALP (\(C=8\) fixed)” and “ALP (\(C\) free),” but the manuscript’s equations and prior list use \(C_0\) and \(C_{a\gamma}\), not \(C\). This is not just stylistic; it obscures what was actually varied in the MCMC.  
- **Required fix:** Either rename the table entry to match the equations, or introduce \(C\) formally in the model section and explain its relation to the other coupling symbols.

P2-N4 (NIT) – The abstract’s “3.6σ” and “3.9σ” statements are arithmetically consistent with the quoted central values  
- **Location:** Abstract  
- **Check:** \(0.342/0.094 \approx 3.64\), which rounds to 3.6σ, and \(0.242/0.061 \approx 3.97\), which is reasonably summarized as 3.9σ.  
- **Required fix:** No arithmetic correction needed, but the manuscript should clarify that the 0.094 uncertainty is the one used for the significance claim.

P2-M12 (MAJOR) – The “order-unity” claim for \(f_{\rm photon}\times C_0\) is not justified without defining the units of \(f_{\rm photon}\)  
- **Location:** Sec. 3.2, Eq. (5); Abstract  
- **Problem:** The product \(f_{\rm photon}\times C_0 = 1.73\pm0.44\) is presented as “order-unity,” but the manuscript never states whether \(f_{\rm photon}\) is dimensionless, rescaled by \(10^{18}\,\mathrm{GeV}\), or normalized in some other way. Without that, “order-unity” is not interpretable.  
- **Required fix:** Specify the normalization of \(f_{\rm photon}\) and whether the product is dimensionless or expressed in a rescaled unit system.

P2-M13 (MAJOR) – The Bayes factor is presented as more precise than the chain lengths justify  
- **Location:** Sec. 3.3–3.4  
- **Problem:** The manuscript correctly notes that the accepted sample sizes are only 720–6,840 and that tail estimates and evidence calculations are limited. Nonetheless, it reports \(\ln B=5.17\) to two decimal places and then gives similarly precise prior-dependent alternatives (4.48 and 5.86) without any uncertainty estimate.  
- **Required fix:** Report an uncertainty or tolerance on \(\ln B\), or round it more conservatively and explicitly label it as approximate.

P2-E9 (ESSENTIAL) – The ACT DR6 citation remains unverifiable in the provided text and is used as a load-bearing input to the main combined result  
- **Location:** Sec. 3.1, Eq. (4)–(5), References  
- **Problem:** The paper’s combined estimate \(\beta_{\rm combined}=0.242\pm0.061^\circ\) depends directly on the ACT DR6 value \(0.215\pm0.074^\circ\). The manuscript still gives no arXiv ID, DOI, paper title with verifiable bibliographic metadata, or public record for the cited “Diego-Palazuelos and Komatsu, 2025” result.  
- **Required fix:** If this is a real/public result, cite the full bibliographic record; if not, remove it from the quantitative combination and recompute the summary likelihood from verifiable inputs only.

P2-M14 (MAJOR) – The combined result in Eq. (4) is mathematically correct, but the manuscript does not state that it is an inverse-variance weighted *summary-likelihood* estimate rather than a joint likelihood analysis  
- **Location:** Sec. 3.2  
- **Problem:** The paper combines two point estimates and error bars and reports a weighted mean. That is fine mathematically, but the wording can be mistaken for a full joint likelihood fit to the underlying data.  
- **Required fix:** Explicitly call Eq. (4) a *summary-likelihood combination* of published measurements, not a reanalysis of the underlying CMB likelihood.

P2-M15 (MAJOR) – The abstract’s statement that LiteBIRD will “rule out the ALP explanation decisively” overreaches the forecast actually shown  
- **Location:** Abstract; Sec. 4  
- **Problem:** The paper shows \(0.27/0.03=9\sigma\), which is a statistical forecast under one error assumption. But “ruling out the ALP explanation decisively” also depends on systematics, calibration degeneracies, and whether the true signal could be smaller than 0.27° while still consistent with the current data. The body acknowledges this dependence, but the abstract omits it.  
- **Required fix:** Qualify the claim with the same caveat used in the body: the 9σ forecast is contingent on the calibration strategy and systematic error budget.

P2-N5 (NIT) – The comparison to \( \beta_{\rm obs}=0.342\pm0.094^\circ \) is numerically consistent with the stated 1σ agreement  
- **Location:** Abstract; Sec. 3.3; Conclusion  
- **Check:** The difference between \(0.27^\circ\) and \(0.342^\circ\) is \(0.072^\circ\), which is within the quoted \(0.094^\circ\) uncertainty.  
- **Required fix:** None, but if “matches the observed signal” is meant quantitatively, say “within \(1\sigma\)” explicitly.

P2-M16 (MAJOR) – The novelty claim “independent of bounce cosmology” is qualitatively fine but under-supported relative to the later ECH/bounce discussion  
- **Location:** Abstract; Sec. 5; Conclusion  
- **Problem:** The abstract asserts independence from bounce cosmology, and the body indeed says the ALP is a spectator field that does not participate in bounce dynamics. However, the same section later motivates the model using ECH / Holst / Barbero-Immirzi language, which may suggest a hidden dependence on the bounce framework to readers.  
- **Required fix:** Add a sentence explicitly separating the *phenomenological ALP prediction* from the *optional theoretical motivation* so readers do not infer that the result relies on bounce assumptions.

P2-E10 (ESSENTIAL) – The reference to “Namikawa, Murai & Naokawa” is still not bibliographically valid as written  
- **Location:** Sec. 6; References  
- **Problem:** The paper invokes “Namikawa et al., 2025” for “superior ALP mass constraints,” but the provided reference has no arXiv ID, no publication venue, and even a likely author-name typo (“Naokawa”). This remains non-verifiable and is used to support a substantive comparison claim.  
- **Required fix:** Replace with a real, citable publication or remove the quantitative comparison.

P2-M17 (MAJOR) – The statement that “the ALP model reproduces the observed birefringence with no tension” is stronger than the reported uncertainties warrant  
- **Location:** Sec. 3.3  
- **Problem:** The model posterior \(0.336\pm0.107^\circ\) and the observed value \(0.342\pm0.094^\circ\) are indeed very close, but they are derived from different procedures and have uncertainties at the 0.1° level. “No tension” is plausible, but the manuscript does not compute a formal tension metric.  
- **Required fix:** Replace “no tension” with “consistent within the quoted uncertainties” unless a specific tension statistic is provided.

P2-M18 (MAJOR) – The paper’s comparison to “all three model configurations” is incomplete because Run 2 is never numerically summarized in the main text  
- **Location:** Figure 2 caption; Sec. 3.3  
- **Problem:** The figure caption says all three configurations are shown, but the text only gives the Run 1, Run 3, and observed-value summaries. Run 2 is discussed only indirectly through \(C_{a\gamma}\times\theta_i = 3.4\pm1.1\).  
- **Required fix:** Add a direct Run 2 posterior summary for \(\beta\), or amend the figure caption so it does not imply symmetry of summarization across all three runs.

P2-M19 (MAJOR) – The abstract’s “minimal setup naturally accommodates” claim is not fully supported by the parameter priors used in the MCMC  
- **Location:** Abstract; Sec. 3.3  
- **Problem:** The narrative says the model is minimal and natural, but the inference uses a broad prior on \(\log_{10}(m/\mathrm{eV})\in[-35,-30]\) and \(C_{a\gamma}\in[1,30]\) (Run 2). That is fine, but it means the statistical conclusions are prior-shaped over a wide range, not purely emergent from a tightly constrained minimal model.  
- **Required fix:** Clarify that “minimal” refers to the number of fields and interactions, not to sharply fixed parameter values.

P2-N6 (NIT) – The computation of \(1-J_0(1)\approx 0.24\) is correct  
- **Location:** Sec. 2.1  
- **Check:** \(J_0(1)\approx 0.7652\), so \(1-J_0(1)\approx 0.2348\), which rounds to 0.24.  
- **Required fix:** None.

P2-M20 (MAJOR) – The sentence “For C0 ∼ 1, θi ∼ 1 … yielding β ≈ … 0.27°” compresses several unstated numerical steps  
- **Location:** Sec. 2.2  
- **Problem:** The manuscript says \(\Delta\phi/f_a\sim 10^{-2}\) and then \(\beta \approx C_0\theta_i\times 5\times10^{-3}\,\mathrm{rad}\approx0.27^\circ\), but the intermediate algebra is not transparent. The reader cannot tell whether the result assumes \(C_0\theta_i\simeq1\), a particular choice of \(m/H_0\), or an additional numerical factor from cosmological integration.  
- **Required fix:** Show the explicit substitution chain, including which values are taken as fiducial and how \(5\times10^{-3}\,\mathrm{rad}\) is obtained from Eq. (1) and Eq. (2).