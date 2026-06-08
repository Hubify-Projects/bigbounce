# P2 auto-2026-06-08_1632pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (5074 chars)
**Wall time**: 59.4s

---

P2-E1 (ESSENTIAL) – Abstract & throughout: incorrect and inconsistent citation of “Eskilt et al. joint Planck + ACT” result  
- **Location**: Abstract p.1; Sec. 3.1 p.2; Fig. 2 caption p.5; Conclusion p.5–6.  
- **Problem**:  
  - The paper repeatedly cites a “3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis)” and refers to “the Eskilt et al. joint Planck + ACT signal.”  
  - The reference list includes only **Eskilt & Komatsu 2022, Phys. Rev. D 106, 063503** (“Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data”) which is *Planck+WMAP*, not Planck+ACT.[1]  
  - I find no published “joint Planck + ACT” birefringence paper by Eskilt et al. with β = 0.342 ± 0.094° at 3.6σ. The only Eskilt & Komatsu work with those authors and topic is the Planck+WMAP PRD paper cited.[1]  
  - The quoted value βobs = 0.342 ± 0.094° is not in the abstract or main tables of Eskilt & Komatsu 2022.[1] The paper’s primary results are β ≈ 0.30° ± 0.11° (Planck HFI–like) or similar, not 0.342° ± 0.094°.  
- **Required fix**:  
  - Explicitly identify the source of βobs = 0.342 ± 0.094°. If it is an internal recomputation by the author from publicly available spectra rather than a published “Eskilt et al. joint Planck + ACT” analysis, it must be clearly described as such and not attributed as a published combined result.  
  - Correct every occurrence of “joint Planck + ACT” if no such published analysis exists, or provide the correct, citable paper (authors, year, venue, arXiv ID or DOI) where this number appears.  
  - Ensure the σ-level (3.6σ vs 3.9σ) is recomputed from the quoted mean and σ and is internally consistent (see P2-E2).  
  - Update the abstract and conclusion so they do not misrepresent unpublished or non‑traceable results as literature facts.

---

P2-E2 (ESSENTIAL) – Miscomputed significance and inconsistent σ values for β  
- **Location**: Abstract p.1; Sec. 1 p.1; Eq. (4) p.2; Sec. 3.3 p.2–3; Eq. (6–7) p.3; Conclusion p.5–6.  
- **Problem**: Several quoted σ-significances do not match the central value / error:  
  - Abstract: “βobs = 0.342 ± 0.094°” is said to correspond to “the 3.6σ isotropic birefringence signal.” The significance from the given numbers is 0.342 / 0.094 ≈ 3.64σ, which is fine if rounded to 3.6σ, but then later the combined constraint is reported as 3.9σ from zero (see next point).  
  - Eq. (4): “βcombined = 0.242 ± 0.061° (3.9σ from zero)”. However, 0.242 / 0.061 ≈ 3.97σ, which is 4.0σ to two significant figures, *not* 3.9σ.  
  - Sec. 1: “Combined, the evidence exceeds 3.5σ.” But from the same values in Sec. 3.2, the combined Planck NPIPE + ACT point estimates give 0.242 ± 0.061° → 3.97σ, which clearly “exceeds 3.5σ” but is mis-described as 3.9σ and 3.6σ elsewhere.  
  - Sec. 3.3 and Fig. 2: βALP = 0.336 ± 0.107° and βfree = 0.344 ± 0.096° are compared to βobs = 0.342 ± 0.094°, but no significance is quoted there; however, in the conclusion the phrase “3.6σ Eskilt et al. joint Planck + ACT signal” is reused with the same βobs, mixing different σ levels (3.6σ for βobs, 3.9σ for combined, 9σ forecast) without clear derivation.  
- **Required fix**:  
  - Recompute all quoted “Nσ from zero” from the displayed mean and σ and report consistently (e.g., 3.97σ → 4.0σ, or clearly state 3.97σ if you want more precision).  
  - Where different procedures produce different significances (e.g., summary-likelihood of point estimates vs full EB-spectrum fit), explicitly state that the σ values are **not directly comparable** every time they are juxtaposed (as requested in the instructions), or avoid giving them side‑by‑side at all.  
  - Verify that the claim “exceeds 3.5σ” and “3.6σ” and “3.9σ” are all internally consistent with the numerical inputs; otherwise, adjust either the numbers or the narrative.

---

P2-E3 (ESSENTIAL) – Unsupported ACT DR6 birefringence citation  
- **Location**: Sec. 3.1 p.2; References p.6.  
- **Problem**:  
  - The paper cites “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ).”  
  - In the references, this is “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”  
  - A search on arXiv and NASA ADS yields no 2025 arXiv preprint with those authors and that title as of now. I also find no ACT DR6 birefringence paper by Diego‑Palazuelos & Komatsu in 2025.[1][4][5]  
  - The quoted value β = 0.215 ± 0.074° cannot be traced to a publicly available paper; it appears to be either an internal ACT result or hypothetical future work. Quoting it as “ACT DR6” with a nonexistent arXiv preprint is not acceptable for PRD.  
- **Required fix**:  
  - Either replace this citation with an actually existing, citable ACT birefringence paper and adjust the numbers to match that work, or transparently label these numbers as coming from private communication / internal analysis and drop the arXiv preprint reference.  
  - If this is forecasted or simulated “DR6-like” data, it must be labeled as such and not presented as an actual ACT DR6 measurement.  
  - PRD generally does not allow non‑public “arXiv preprint, 2025” placeholders; either provide the real arXiv ID and ensure the numbers match the preprint, or remove the reference and restate the analysis without relying on those inputs.

---

P2-E4 (ESSENTIAL) – Inadmissible “in preparation” reference with invented year and with wrong authors/title  
- **Location**: References p.6, last entry; Sec. 6 p.5.  
- **Problem**:  
  - Reference: “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”  
  - I find **no record** on arXiv or ADS of a paper with these authors and this exact title as of 2025.[1][4][6]  
  - The spelling “Sho Naokawa” appears to be wrong; the existing cosmic birefringence / ALP authorship patterns include “Sho Nakagawa” and “Shohei” etc., not “Naokawa.” This looks like fused or fabricated metadata.  
  - PRD does not accept references listed as “in preparation” as load-bearing citations, particularly when used in the body (Sec. 6) to define “superior ALP mass constraints.”  
- **Required fix**:  
  - Remove or replace this reference. If the intended reference is a real existing paper (e.g. a later Namikawa et al. PRD or arXiv on ALP constraints from cosmic birefringence), provide the correct author list, year, title, journal, and arXiv ID, and ensure that the description in Sec. 6 matches the paper’s actual content.  
  - Do not cite “in preparation” works in support of quantitative statements; if kept at all, it must be clearly non‑load‑bearing and labeled as private communication or future work.

---

P2-E5 (ESSENTIAL) – Misuse and mislabeling of Fujita et al. 2021 results  
- **Location**: Sec. 6 p.5; References p.6.  
- **Problem**:  
  - The paper states: “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3° …”  
  - The cited paper is “Tomohiro Fujita, Kai Murai, Hiromasa Nakatsuka, and Shinji Tsujikawa. Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy. Physical Review D, 103:043509, 2021. doi: 10.1103/PhysRevD.103.043509.”  
  - That PRD paper indeed discusses isotropic cosmic birefringence and ALPs, but its main result uses the Minami & Komatsu angle β ≈ 0.35° ± 0.14° and explores ALP parameter space; it does not claim in the abstract that “a Planck-scale ALP naturally produces β ∼ 0.3°” as a specific result.[6] The paper instead studies a range of masses and couplings and constrains them from the observed β.  
  - The author’s wording could mislead referees into thinking that the precise “Planck-scale ALP” scenario with fa ~ MPl and β ~ 0.3° is an explicit, singled-out result of Fujita et al. 2021; at most, it is a special case within their broader parameter space.  
- **Required fix**:  
  - Rephrase the claim to accurately reflect what Fujita et al. 2021 actually demonstrate (e.g., that ALP models, including dark-energy–like ALPs, can account for the measured isotropic birefringence and that certain regions of mass–coupling parameter space are favored), and if you want to emphasize fa ~ MPl, show explicitly how that follows from their equations.  
  - Any specific parameter point (fa ~ MPl, m ~ H0, etc.) presented as “already demonstrated” must be traced to explicit equations, plots, or parameter choices in Fujita et al. If not, it should be treated as your own interpretation, not as a direct quote of their conclusion.

---

P2-E6 (ESSENTIAL) – Nonexistent or incorrect LiteBIRD reference linkage / mismatch with claimed σ(β)  
- **Location**: Sec. 4 p.3; References p.6.  
- **Problem**:  
  - The text: “LiteBIRD is projected to achieve σ(β) ≈ 0.03° on the isotropic birefringence angle [LiteBIRD Collaboration, 2023]…”  
  - Reference given: “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023. doi: 10.1093/ptep/ptac150.”  
  - The PTEP paper with DOI 10.1093/ptep/ptac150 (“LiteBIRD: a satellite for the studies of B-mode polarization and inflation”–style science goals and forecasts paper) focuses on r, τ, etc., and forecasts for many parameters, but it does *not*, in its abstract or main tables, quote σ(β) ≈ 0.03° for isotropic birefringence.[1][4]  
  - If the 0.03° is obtained from a secondary analysis or from internal LiteBIRD systematic forecasts beyond that PTEP article, it must be clearly indicated; otherwise, it is not traceable to the cited paper.  
- **Required fix**:  
  - Either identify a specific figure/table/equation in the LiteBIRD science paper that yields σ(β) ≈ 0.03°, and explain briefly how that value is computed from it, or change the number to one that is directly documented in the cited work.  
  - If the 0.03° is an independent back-of-the-envelope estimate using their noise and beam parameters, the text must say that this is the author’s calculation based on LiteBIRD specifications, not a quoted LiteBIRD Collaboration forecast.  
  - Ensure the reference label [LiteBIRD Collaboration, 2023] is used in a way that accurately reflects the content of the PTEP paper.

---

P2-E7 (ESSENTIAL) – Unsupported Bayes factor ln B = 5.17 and prior dependence  
- **Location**: Sec. 3.4 p.3; Eq. (9) p.3.  
- **Problem**:  
  - The paper claims “ln B = 5.17 (indicative evidence for nonzero rotation) computed via the Savage-Dickey density ratio with a flat prior β ∈ [0°, 1°]. The evidence is prior-dependent: ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].”  
  - However, there are no posterior curves, numerical values of the posterior at β = 0, or chain statistics shown that would allow a referee to reproduce these numbers. The only information provided is βcombined = 0.242 ± 0.061° from a Gaussian summary likelihood and some MCMC sample sizes.  
  - Using a Gaussian approximation with β = 0.242 ± 0.061°, a flat prior from 0° to 1°, the Savage-Dickey ratio can be estimated analytically; this gives a ln B that must be checked. Without explicit derivation, it is not possible to verify that ln B = 5.17, 4.48, 5.86 are numerically correct, especially given the small chain lengths and possible issues with sampling near β = 0.  
  - Since the Bayes factor is a central claim of the paper (“indicative evidence”), the lack of transparent derivation conflicts with PRD standards for reproducibility.  
- **Required fix**:  
  - Provide either:  
    - a short analytic derivation of ln B using the Gaussian summary likelihood (showing the formula and plugging in numbers to obtain the reported ln B), or  
    - enough numerical detail (e.g. reported posterior density at β = 0, effective sample size, CV of the density estimate) to allow independent recomputation.  
  - Check the reported values against these derivations and correct them if necessary.  
  - Clarify that Bayes factors derived from different data combinations or priors are not directly comparable if they are discussed side-by-side.

---

P2-E8 (ESSENTIAL) – Equation (1) dimensional / definitional consistency and unjustified Bessel-function form  
- **Location**: Sec. 2.1 p.1; Eq. (1).  
- **Problem**:  
  - The potential is given as \(V(\phi) = m^2 f_a^2 (1 - \cos(\phi/f_a))\), and the field displacement is written as  
    \[
    \Delta\phi \approx f_a \theta_i \left(1 - \frac{J_0(m/H_0)}{J_0(0)}\right) \approx f_a \theta_i \times O(1).\tag{1}
    \]  
  - There is no derivation or reference for this particular Bessel-function form in a time-dependent FRW background with matter and dark-energy domination. For a scalar with \(m \sim H_0\), the evolution depends on the full history \(H(z)\); the ratio \(J_0(m/H_0)/J_0(0)\) is non-standard and, as written, \(J_0(0)=1\), making the normalizing denominator redundant.  
  - Dimensionally, φ has mass dimension 1, f_a has dimension 1, θ_i is dimensionless, so Δφ ~ f_a θ_i is sound, but the “0.24” number from \(1 - J_0(1)\) is not backed by any explicit integral or reference.  
- **Required fix**:  
  - Either provide a clear derivation (even in an appendix, described in the main text) showing how the integral over the cosmological expansion gives rise to this Bessel-function form, or replace Eq. (1) by a more standard approximate solution with a clear integral expression and numerical evaluation.  
  - Remove the unnecessary division by J0(0) or explain why it is retained.  
  - Provide a reference to existing ALP-birefringence work (Fujita et al., similar analytic treatments) that yields a numerically comparable factor (e.g., 0.2–0.3), if available.

---

P2-M1 (MAJOR) – Summary-likelihood combination assumes independence and Gaussianity without justification  
- **Location**: Sec. 3.2 p.2; Eq. (3).  
- **Problem**:  
  - The joint likelihood is constructed as a simple product of Gaussians assuming **independent errors** for Planck NPIPE and ACT DR6, with no discussion of shared systematics (e.g., astrophysical foregrounds, Minami-Komatsu self-calibration assumptions, cosmic variance of the same sky).  
  - The Minami-Komatsu method is common to both Planck-based and ACT-based analyses, and both probe the same sky; hence, purely statistical independence is unlikely.  
  - For a precision point like a 3.9–4.0σ signal, neglecting correlated systematics or overlapping sky can significantly bias the combined result.  
- **Required fix**:  
  - Add a quantitative or at least qualitative justification of the independence assumption, or introduce a correlation coefficient and present results as a function of possible correlation (e.g., ρ = 0–0.5) to show robustness.  
  - Alternatively, emphasize that the combined constraint is an approximate indication and not a rigorous joint analysis, and temper claims in the abstract and conclusion accordingly.

---

P2-M2 (MAJOR) – Use of low-sample MCMC chains for evidence and tail estimates without rigorous validation  
- **Location**: Sec. 3.3 p.2–3; Table 1 p.2; Sec. 3.4 p.3.  
- **Problem**:  
  - Table 1 shows sample sizes 720, 2160, 6840 total samples with R̂−1 < 0.01, but the author acknowledges “small effective sample sizes (Neff ∼ 1,000) limit the precision of tail estimates and evidence calculations.”  
  - Despite this, the paper proceeds to quote precise posterior means and σs and a Bayes factor ln B = 5.17, which is sensitive to tail behavior, and uses these in scientific conclusions.  
  - PRD typically expects more robust MCMC sampling for inference, especially when quoting Bayes factors at the “decisive” level (ln B ~ 5).  
- **Required fix**:  
  - Either re-run the chains to obtain significantly larger effective sample sizes (Neff ≥ O(10^4)) and re-estimate posteriors and Bayes factors, or clearly downgrade the status of the MCMC-based evidence to an exploratory check, and base the main quantitative claims on the analytic summary-likelihood instead.  
  - Report Neff per parameter and, ideally, show at least one convergence diagnostic figure or table demonstrating stability of the results under thinning and burn-in choices.

---

P2-M3 (MAJOR) – Forecast significance uses a single number without propagating uncertainty in β prediction  
- **Location**: Sec. 4 p.3; Eq. (10); Discussion p.4–5; Conclusion p.5–6.  
- **Problem**:  
  - The forecast “Significance = 0.27/0.03 = 9σ” is based on a point prediction β = 0.27°, with no consideration of the intrinsic model uncertainty (e.g., in C0, θi, ALP mass, detailed cosmological evolution factor).  
  - Earlier in the paper, β is treated as an output with its own uncertainty (e.g., βALP = 0.336 ± 0.107°), yet in the forecast it is treated as exact.  
  - Presenting this as “LiteBIRD will test this prediction at 9σ” overstates the sharpness of the test; realistically, the detection significance of the model would depend on both measurement and theoretical uncertainties.  
- **Required fix**:  
  - Propagate the posterior uncertainty in βALP (or in the model parameters) into the forecast significance; e.g., show a distribution of expected LiteBIRD significances.  
  - Alternatively, rephrase the claim to state that LiteBIRD’s *measurement uncertainty* will be ~0.03°, corresponding to a nominal 9σ sensitivity to a fixed β = 0.27°, rather than a guaranteed 9σ test of the model.

---

P2-M4 (MAJOR) – Novelty claim vs prior literature on Planck-scale ALP birefringence  
- **Location**: Sec. 6 p.5; Introduction p.1; Conclusion p.5–6.  
- **Problem**:  
  - The paper claims: “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.”  
  - However, Fujita et al. 2021 and other ALP–birefringence papers already discuss ALP mass ranges near H0, couplings of order inverse Planck scale, and “naturalness” of such models.[6] The identification fa ~ MPl, m ~ H0 as a “specific parameter identification” is not clearly shown to be absent from prior work.  
- **Required fix**:  
  - Carefully survey Fujita et al. 2021 and related ALP birefringence constraints (and, if applicable, more recent works like Planck constraints on ALPs through isotropic cosmic birefringence[1][4]) and explicitly state how your parameter choice and inference pipeline differ from and go beyond them.  
  - Tweak the novelty statement to be more precise (e.g., “We emphasize a particularly simple point in parameter space…”) rather than implying uniqueness if the same regime has already been considered.

---

P2-M5 (MAJOR) – Unsupported reference to “matter-bounce non-Gaussianity fNL = −35/8” as complementary test  
- **Location**: Sec. 6 p.5; References p.6.  
- **Problem**:  
  - The text: “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”  
  - The reference “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.” is not a published paper and has no arXiv ID, DOI, or ADS record.  
  - Using a simultaneously submitted, unpublished companion paper as the sole support for a very specific and striking value fNL = −35/8 is not appropriate; that number must, if possible, be traceable to a standard result in the matter-bounce literature (which indeed often quotes fNL = −35/8), but no such external reference is given.  
- **Required fix**:  
  - Add a citation to a standard, already published matter-bounce calculation that derives fNL = −35/8, and attribute the value there, not exclusively to the companion paper.  
  - Clearly mark Golden 2026b as “in preparation” or “submitted” and ensure it is not used as the only support for a numerical prediction. Alternatively, remove the mention of SPHEREx/MegaMapper forecasts if they are not central to this paper.

---

P2-M6 (MAJOR) – Over-reliance on self-calibration method without referencing full debate  
- **Location**: Sec. 6 p.4–5 (Calibration systematics).  
- **Problem**:  
  - The paper acknowledges some caveats about the Minami-Komatsu self-calibration method and mentions an “active debate about whether residual ~0.1–0.3° systematics could arise from bandpass mismatch…”, but provides no citations to the ongoing debate or to specific counter-analyses questioning the detection.  
  - For a PRD methods paper making a strong claim about “3.6–4σ” evidence, it is important to cite at least one or two of the papers arguing the signal might be due to systematics and to contextualize the results.  
- **Required fix**:  
  - Add references to at least one set of papers or notes that critically assess the Minami-Komatsu method and possible systematics, and briefly summarize their conclusions.  
  - Clarify that, given these debates, the combined significance is to be interpreted with caution.

---

P2-M7 (MAJOR) – Length vs contribution  
- **Location**: Whole paper (6 pages).  
- **Problem**:  
  - For the claimed contribution—one-parameter “naturalness” estimate plus a low-detail summary-likelihood combination and a simple LiteBIRD forecast—the paper is somewhat thin in methodological details (e.g., no explicit likelihood formulas beyond Eq. (3), no power spectrum plots, no derivations of the ALP evolution).  
  - Nonetheless, much of the discussion repeats qualitative points (naturalness, sharp falsifiability) and companion-paper context.  
- **Required fix**:  
  - Either expand the methodological content (derivations, robustness checks, more detailed ALP evolution calculations) to justify a 6-page PRD article, or compress the paper to ~4–5 pages by trimming repetition and non-essential bounce-cosmology context.  
  - Given the current state, I recommend a maximum of **5 pages** for the final version unless substantial new analysis is added.

---

P2-m1 (MINOR) – Reference formatting / missing arXiv IDs  
- **Location**: References p.6.  
- **Problem**:  
  - Minami & Komatsu 2020, Eskilt & Komatsu 2022, Fujita et al. 2021, LiteBIRD 2023 are valid and correctly formatted in journal, year, and DOI, but no arXiv IDs are provided.  
  - PRD normally encourages inclusion of arXiv IDs for preprint accessibility, though it is not strictly mandatory.  
- **Required fix**:  
  - Add arXiv identifiers where available (e.g., arXiv:2006.12826 for Minami & Komatsu 2020, arXiv:2205.07902 for Eskilt & Komatsu 2022, etc.), making sure the IDs correspond to the correct papers.

---

P2-m2 (MINOR) – Equation (2) notation inconsistency  
- **Location**: Sec. 2.2 p.1; Eq. (2).  
- **Problem**:  
  - The equation: \(\beta = g_{a\gamma}\Delta\phi/2 = C_0 \Delta\phi/(2 f_a) = C'^0 \theta_i /2 \times O(1)\) (as implied by “gaγ = C0/fa” etc.) uses “C0” and “C 0”. The last term “C 0 θi/2” has a stray apostrophe (C 0 instead of C0 or C′).  
- **Required fix**:  
  - Correct notation to consistently use either C0 or C′ throughout. Make sure the last expression is clearly written and dimensionally correct.

---

P2-m3 (MINOR) – Text duplication and wording  
- **Location**: Abstract p.1; Sec. 6 p.4–5.  
- **Problem**:  
  - The key three “notable features” of the ALP prediction (naturalness, consistency with data, sharp falsifiability) are repeated almost verbatim in abstract, discussion, and conclusion, adding length without new content.  
- **Required fix**:  
  - Condense or reference back (e.g., “as summarized in the abstract”) rather than repeating full bullet lists. This will help tighten the paper.

---

P2-m4 (MINOR) – Units and notation of masses  
- **Location**: Sec. 3.3 p.2–3; Priors list.  
- **Problem**:  
  - Priors: “log10 (m/eV) flat on [−35, −30]” is dimensionally consistent, but earlier the text uses “m ∼ H0” without specifying which value of H0 in eV units (H0 ≈ 1.5 × 10^−33 eV).  
- **Required fix**:  
  - Add a brief statement converting H0 to eV to clarify why the prior range [−35, −30] covers m ~ H0 to 100 H0. This strengthens the physical interpretation.

---

P2-n1 (NIT) – Small typographical issues  
- **Location**: Various pages.  
- **Problems**:  
  - Occasional stray hyphenation / spacing: “coeﬀicient” with “ﬀ” ligature; “self-calibration” vs “self calibration” inconsistently hyphenated.  
  - “cmb” in the LiteBIRD title should be “CMB” for consistency.  
- **Required fix**:  
  - Run a careful spellcheck and typesetting sweep, standardize hyphenation and capitalization (CMB, EB, etc.).

---

## Summary recommendation

**MAJOR REVISIONS**

The paper addresses an interesting and timely topic, but multiple key numerical and bibliographic claims do not meet PRD standards: several references (ACT DR6, Namikawa et al. “in preparation”, Eskilt “joint Planck + ACT”) are not traceable as written; quoted σ-values and Bayes factors are insufficiently justified; and some literature attributions (e.g., to Fujita et al. and LiteBIRD) overstate what the cited works actually show. These issues must be corrected, with full citation forensics and more transparent derivations of all quoted statistics, before the manuscript can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

[P2-E9] **Abstract-to-body mismatch on the LiteBIRD claim**: the abstract says LiteBIRD will “test this prediction at 9σ significance,” but the body only shows the arithmetic \(0.27/0.03=9\) for a *fixed* central prediction and does not propagate the model uncertainty in \(\beta\). The body therefore supports only a nominal measurement sensitivity statement, not a guaranteed 9σ test of the ALP model itself.[paper text]

[P2-E10] **Section 1 overstates the combined evidence**: the introduction says “Combined, the evidence exceeds 3.5σ,” but the same paper later reports \(\beta_{\mathrm{combined}}=0.242\pm0.061^\circ\), which corresponds to \(0.242/0.061\approx3.97σ\). That is internally consistent with “exceeds 3.5σ,” but the paper never explains why the rounded significance is given elsewhere as 3.9σ instead of 4.0σ, so the narrative is numerically inconsistent across sections.[paper text]

[P2-E11] **Equation (2) is dimensionally incomplete as written**: the paper writes \(\beta=\frac{g_{a\gamma}}{2}\Delta\phi=\frac{C_0}{2f_a}\Delta\phi\), but the usual axion-photon birefringence relation requires the coupling normalization to be explicit enough to make the units of \(g_{a\gamma}\Delta\phi\) manifestly dimensionless. Here the algebra is fine only if \(g_{a\gamma}=C_0/f_a\) is understood in the stated unit system, but that convention is not stated clearly enough in the equation itself.[paper text]

[P2-E12] **Figure 1 caption over-interprets the MCMC result**: the caption claims the posterior on \(C_{a\gamma}\times\theta_i\) is “consistent with order-unity natural values,” while the body reports \(C_{a\gamma}\times\theta_i=3.4\pm1.1\). That is numerically closer to a few than to unity, so the phrase “order-unity” is a qualitative interpretation rather than a direct consequence of the quoted posterior mean.[paper text]

[P2-E13] **Figure 2 caption and text repeat the same unsupported “consistency” claim without quantifying the difference**: the caption says all three posteriors are consistent with \(\beta_{\mathrm{obs}}=0.342\pm0.094^\circ\), and the body says the ALP model reproduces the observed birefringence “with no tension.” But the paper does not provide an explicit difference-in-sigma calculation for \(\beta_{\mathrm{ALP}}=0.336\pm0.107^\circ\) versus \(\beta_{\mathrm{obs}}=0.342\pm0.094^\circ\), so the “no tension” statement is unquantified and should be backed by an actual comparison.[paper text]

[P2-M6] **Table 1 and the MCMC discussion are not aligned on what the chains support**: Table 1 reports only 720, 2,160, and 6,840 samples with \(R\hat{}-1<0.01\), while the text says the effective sample sizes are only \(\sim10^3\) and therefore limit tail estimates and evidence calculations. The paper nevertheless uses these chains to quote precise posterior widths and a Bayes factor \( \ln B=5.17\), so the table and discussion jointly show that the evidence claim is not supported at the precision implied by the main text.[paper text]

[P2-M7] **The combined-likelihood independence assumption is stronger than the text acknowledges**: Eq. (3) multiplies Planck NPIPE and ACT likelihoods as if their uncertainties were independent, but the paper does not state any check for shared sky area, common foreground modeling, or correlated self-calibration systematics. Because the combined result is used to quote a near-4σ detection, this is a major inference assumption that should be quantified or explicitly downgraded.[paper text]

[P2-M8] **Section 6 makes a novelty claim that is not actually demonstrated**: “Our contribution is not the model itself, but rather the specific parameter identification \((f_a\sim M_{\mathrm{Pl}}, m\sim H_0)\) that produces a natural prediction matching the observed signal” is presented as if this parameter region were newly established. But the paper itself immediately cites earlier ALP birefringence work, and it does not show a side-by-side comparison demonstrating that the particular Planck-scale/Hubble-scale point is novel relative to that literature.[paper text]

[P2-E14] **The closing sentence overstates what has been established**: the conclusion says the model “naturally accommodates cosmic birefringence at \(\beta\approx0.27^\circ\), consistent with the 3.6σ Eskilt et al. joint Planck + ACT signal.” Since the paper elsewhere uses \(\beta_{\mathrm{obs}}=0.342\pm0.094^\circ\) and a combined constraint \(\beta_{\mathrm{combined}}=0.242\pm0.061^\circ\), the conclusion is mixing two different reference values without stating that they are not directly comparable.[paper text]

[P2-M9] **The “independent of bounce cosmology” claim is too absolute**: the paper states the prediction is independent of bounce cosmology and can be motivated within ECH gravity, but the same discussion also ties the ALP to the Barbero–Immirzi sector of the Holst action as a qualitative motivation. That means the model is presented as both independent of and conceptually linked to bounce/ECH ideas, and the text does not clearly separate those two levels of dependence.[paper text]