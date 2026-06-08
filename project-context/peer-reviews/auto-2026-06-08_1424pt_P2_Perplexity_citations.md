# P2 auto-2026-06-08_1424pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12147 chars)
**Wall time**: 86.7s

---

P2-E1 (ESSENTIAL) – Abstract & multiple sections, p.1–4  
Problem: The paper repeatedly cites a “3.6σ” or “>3.5σ” joint Planck+ACT birefringence detection and uses the specific value β_obs = 0.342 ± 0.094° attributed to an “Eskilt et al. joint Planck + ACT analysis,” but no such published joint analysis exists in the cited literature. The only Eskilt & Komatsu paper in the references is Eskilt & Komatsu, PRD 106, 063503 (2022), which uses WMAP+Planck and reports β = 0.342 ± 0.094° as a WMAP+Planck result, not a Planck+ACT joint analysis.[1] The ACT DR6 birefringence paper “Diego-Palazuelos and Komatsu, 2025” is not yet on arXiv/ADS (see P2-E8), and there is no public Planck+ACT joint β constraint with that quoted value and error bar. The 3.6σ figure in the abstract is not traceable to any cited, publicly available paper.  
Required fix:  
- Clarify precisely which dataset combination gives β_obs = 0.342 ± 0.094° and 3.6σ; if this is WMAP+Planck (as in Eskilt & Komatsu 2022 PRD), state that accurately and remove any reference to ACT from that number.  
- If there is an internal or in-preparation Planck+ACT joint analysis, it must not be used as if it were a published, citable result. Either (a) drop it, (b) move it to clearly marked “private communication/unpublished” status with explicit caveats and do not base quantitative inferences on it, or (c) add a properly citable, publicly available preprint and ensure all quoted numbers match that preprint.  
- All σ-significances in the abstract and body must be recomputed from clearly identified, published values; remove or rephrase any claims that currently rely on non-public or misattributed results.

---

P2-E2 (ESSENTIAL) – Bibliography entry, p.6 (“P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.”)  
Problem: This reference is incomplete and not verifiable as cited. There is no arXiv ID, journal, or DOI. A search on arXiv and ADS for a 2025 “Cosmic birefringence from the Atacama Cosmology Telescope” preprint with authors Diego-Palazuelos and Komatsu returns no match.[1][5] The paper is treated as if it were a completed arXiv preprint, but that status cannot be confirmed.  
Required fix:  
- Provide the correct arXiv identifier and ensure the title and author list match exactly what is on arXiv/ADS, or  
- If the work is still in preparation or under collaboration internal review and not on arXiv, re-label it as “in preparation” and clearly state that the β = 0.215 ± 0.074° number is a private communication or internal preliminary result, and do not treat it as an independent, citable published constraint.  
- If the preprint does not exist yet, you cannot use it as a basis for a summary-likelihood combination as if it were public; you must either remove those results, or defer the present paper until the ACT paper is public and citable.

---

P2-E3 (ESSENTIAL) – Bibliography entry, p.6 (“Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.”)  
Problem: This reference is explicitly marked “In preparation” with a generic “arXiv e-prints, 2025” tag, but there is no arXiv ID, and the wording “arXiv e-prints, 2025. In preparation” is internally inconsistent: a paper cannot both be on “arXiv e-prints” and “in preparation.” A search on arXiv and ADS for this title and author combination returns no 2025 preprint.[1][2] The paper is used as if it provided “superior ALP mass constraints,” but the claims are not traceable.  
Required fix:  
- Either (a) replace this with a real, public preprint entry including arXiv:ID and correct metadata that can be verified, or (b) if the work is genuinely in preparation, change to “in preparation” or “private communication” without referencing “arXiv e-prints” and soften any comparison claims to explicitly note that they rely on unpublished work.  
- You must not base any quantitative or comparative statements on an unpublished “in preparation” paper without giving the reader enough information to access the result; limit yourself to what is in the published literature.

---

P2-E4 (ESSENTIAL) – In-text claim about Namikawa et al., Section 6, p.5  
Offending text: “Namikawa, Murai & Naokawa [Namikawa et al., 2025] provide superior ALP mass constraints using the full Planck EB spectrum.”  
Problem: As in P2-E3, this asserts specific “superior ALP mass constraints” from a work that is not publicly available and has no verifiable arXiv entry. This is an unsupported claim of specific scientific content of an unpublished, in-preparation work.  
Required fix:  
- Either delete this sentence or rephrase to avoid any quantitative or qualitative scientific claims based on the unpublished work. You can at most say “ongoing work (Namikawa et al., in preparation) aims to constrain ALP masses using Planck EB,” but you may not claim their constraints are “superior” without a public record.  
- Do not use these unseen constraints to support or contextualize your results.

---

P2-E5 (ESSENTIAL) – Bibliography entry and in-text claim, Section 6 & References, p.5–6 (Fujita et al., 2021)  
Offending text: “Fujita, Murai, Nakatsuka & Tsujikawa (2021) already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3◦ …” with reference “Tomohiro Fujita, Kai Murai, Hiromasa Nakatsuka, and Shinji Tsujikawa. Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy. Phys. Rev. D 103, 043509, 2021.”  
Problem: Fujita et al. 2021 PRD 103, 043509 considers ALPs as dark energy and derives constraints on the ALP parameter space consistent with an isotropic birefringence signal, but they do not “demonstrate that a Planck-scale ALP naturally produces β ∼ 0.3°” in the strong sense implied here.[7] Their parameter choices and discussion include a wider range of decay constants and masses. The phrase “already demonstrated that a Planck-scale ALP naturally produces β ∼ 0.3°” overstates and mischaracterizes the conclusions of Fujita et al. (they solve for allowed ranges, not a unique Planck-scale, naturally predicted β). This is not a pure citation-metadata error but a misrepresentation of the cited work.  
Required fix:  
- Re-read Fujita et al. 2021 and align the summary with their actual statements. For instance, you could say “Fujita et al. (2021) showed that ALPs can explain a β ∼ 0.3° signal for appropriate choices of mass and coupling, including cases where the decay constant is near the Planck scale,” if that is directly supported by their parameter scans.  
- Remove or soften the language “already demonstrated” and “naturally” unless you can quote or paraphrase specific passages from Fujita et al. that clearly support those exact claims. Explicitly distinguish between your specific choice m ∼ H0, f_a ∼ M_Pl and their broader parameter ranges.

---

P2-E6 (ESSENTIAL) – Mixing different β determinations without caveat, Sections 1, 3.1, 3.3, p.1–3  
Problem: The text juxtaposes multiple β estimates derived by **different analysis pipelines and data combinations** without explicit caveats that they are not directly comparable, violating instruction (7):  

- Introduction p.1: “The Planck HFI analysis [Minami and Komatsu, 2020] reported β = 0.35 ± 0.14° (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.” The “combined” statement merges Planck-HFI (Minami & Komatsu) and a separate ACT analysis.  
- Section 3.1 p.2: “We use… Planck NPIPE [Eskilt & Komatsu 2022]: β = 0.30 ± 0.11°; ACT DR6: β = 0.215 ± 0.074°… For the MCMC… we use the Eskilt et al. joint analysis value β_obs = 0.342 ± 0.094°, which differs because it fits the full EB cross-spectrum rather than combining point estimates.”  
- Section 3.3 p.2–3: compares β_ALP, β_free, and β_obs without explicitly warning that β_obs is derived from a different procedure than the point-estimate combination used elsewhere.  

These are different estimators (self-calibration EB fit vs. summary point-estimate combination) and in some cases different dataset combinations. Placing their σ-values side by side and saying e.g. “Combined, the evidence exceeds 3.5σ” or “The ALP model reproduces the observed birefringence with no tension” implicitly treats them as directly comparable measures of the same quantity without explicitly flagging their distinct systematics and null procedures.  
Required fix:  
- At every place where β values from different pipelines are compared or combined (Introduction, Section 3.1 Eq. (4), Section 3.3 around Eqs. (6)-(7), and Fig. 2 caption), add explicit text noting that the significances are not strictly comparable because they arise from different analysis methods, likelihoods, and data combinations.  
- Replace “Combined, the evidence exceeds 3.5σ” with language like “Different analyses (Planck HFI, WMAP+Planck, and ACT DR6) independently report ~2.5–3σ preferences for β ≠ 0; however their significances are not directly comparable because of different pipelines, calibration assumptions, and data splits.”  
- When quoting the 3.9σ in Eq. (4) from the summary-likelihood, explicitly state that this is an internal Gaussian-combination estimate and should not be directly compared with the significances quoted in the original Planck/ACT analyses.

---

P2-E7 (ESSENTIAL) – Use of “companion paper, submitted simultaneously, 2026a/2026b” with claims of forecasts and “14-barrier catalog”, Section 5 & References, p.4–6  
Problem: There are two self-citations: “Houston Golden. Spin-torsion cosmology… Companion paper, submitted simultaneously, 2026a.” and “Houston Golden. Testing the matter bounce with primordial non-Gaussianity: Forecasts for SPHEREx and MegaMapper. Companion paper, submitted simultaneously, 2026b.” These have no arXiv IDs, DOIs, or journal information. They are not traceable on ADS or arXiv as of now. Yet the text makes substantive claims based on them:  

- “…see the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog.”  
- “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].”  

These statements invoke non-public results (“14-barrier catalog”, specific f_NL prediction) without any verifiable reference.  
Required fix:  
- Either (a) provide proper arXiv identifiers for both companion papers and ensure what you claim here is exactly supported by them, or (b) if these are not yet public, change the wording to “in preparation” or “work in progress” and remove any quantitative or catalog-like claims tied to them.  
- Specifically, do not state “fNL = −35/8 provides a complementary… test [Golden, 2026b]” unless that exact prediction is accessible and checkable; otherwise phrase it as “Our separate work (in preparation) explores matter-bounce models with characteristic fNL values” without relying on it as an established result.

---

P2-E8 (ESSENTIAL) – Existence and status of “ACT DR6 birefringence” result used in Section 3.1 p.2  
Offending text: “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ). These produce the combined constraint in Eq. 4.”  
Problem: As of the present search, there is no public ARXIV/ADS preprint or journal article with these authors and title corresponding to ACT DR6 cosmic birefringence.[1][5] Using a non-public or internal analysis as if it were a finalized, citable “ACT DR6” result is not acceptable for PRD, especially when it is central to the combined constraint β_combined = 0.242 ± 0.061°.  
Required fix:  
- Confirm whether the ACT birefringence result is now publicly available (e.g., ACT DR6 birefringence paper with a citable preprint or journal entry). If yes, update the reference with the correct arXiv ID, title, author list, and year, and check that the quoted β and σ match exactly what is in that paper.  
- If the ACT DR6 birefringence result is still internal, unpublished, or not finalized, you must not use β = 0.215 ± 0.074° in a quantitative combined constraint. Either remove ACT DR6 from the analysis (restrict to published Planck/WAMP+Planck results only) or clearly label this as an illustrative combination using preliminary ACT numbers provided by private communication, and downgrade any strong claims of detection significance.

---

P2-M1 (MAJOR) – Numerical consistency of significance statements, Abstract vs. Eq. (4), p.1–2  
Problem: The abstract claims “β = 0.242 ± 0.061° (3.9σ from zero)” and later “consistent with the 3.6σ isotropic birefringence signal (β_obs = 0.342 ± 0.094°…)”. From simple division, 0.342/0.094 ≈ 3.64σ and 0.242/0.061 ≈ 3.97σ. These are numerically consistent, but the text gives 3.6σ in the abstract for the “Eskilt et al. joint Planck + ACT analysis” and 3.9σ for the combined constraint without explaining that the 3.6σ refers to WMAP+Planck and the 3.9σ is your own Gaussian combination of Planck NPIPE + ACT DR6. The linkage is opaque and potentially misleading.  
Required fix:  
- Explicitly state in the abstract and Section 3.2 that 3.9σ is your internal combination of Planck NPIPE and ACT DR6 point estimates, whereas 3.6σ is the significance reported by Eskilt & Komatsu (WMAP+Planck) for β = 0.342 ± 0.094°.  
- Remove the phrase “Eskilt et al. joint Planck + ACT analysis” unless a real Planck+ACT joint paper exists and you cite it correctly (see P2-E1).  

---

P2-M2 (MAJOR) – Use of “naturalness” and “no fine-tuning” claims without quantitative support, Sections 2 & 6, p.1–2,5  
Problem: The text repeatedly asserts that the model is “natural” and “requires no fine-tuning”:  

- Abstract: “order-unity inputs… naturally accommodates β ≈ 0.27°… no fine-tuning.”  
- Section 2.2: “The key feature: this prediction involves no small or large numbers beyond the cosmological integration factor. Every input is O(1) in natural units.”  
- Section 6: “All input parameters … are at their natural scales. No tuning is required… Caγ × θi = 3.4 ± 1.1, consistent with O(1) values… The ALP model requires no fine-tuning of dimensionless parameters.”  

However, the parameter priors (θ_i on [0.01, π], C_aγ on [1, 30]) and the posterior value C_aγ×θ_i ≈ 3.4 ± 1.1 do not automatically establish absence of tuning. For PRD, “no fine-tuning” claims should be supported by at least a minimal quantitative explanation (e.g., fraction of prior volume yielding β within observed range, sensitivity of β to small parameter variations). Currently, these are qualitative judgments not backed by analysis in the manuscript.  
Required fix:  
- Either provide a quantitative measure of “naturalness” (e.g., show that a large fraction of prior volume leads to β in the observed range, or that the sensitivity ∂β/∂θ_i etc. is modest), or soften the language to “uses order-unity parameters” without claiming “no fine-tuning.”  
- Make clear what you mean by “natural” (e.g., by reference to widely used EFT power-counting or symmetries) and ensure the cited literature (e.g., Fujita et al. 2021) uses compatible terminology.

---

P2-M3 (MAJOR) – Equation (1) derivation and use of Bessel function, Section 2.1 p.1  
Offending text/equation:  
\[
\Delta\phi \approx f_a \theta_i \left(1 - \frac{J_0(m/H_0)}{J_0(0)}\right) \approx f_a \theta_i \times O(1).
\]  
For m/H_0 ∼ 1, “1 − J_0(1) ≈ 0.24”.  
Problems:  
- J_0(0) = 1, so the fraction J_0(m/H_0)/J_0(0) is just J_0(m/H_0); writing the denominator this way is unnecessary at best and potentially confusing.  
- There is no derivation or reference showing that the cosmological solution for a massive scalar with m ∼ H_0 produces this exact Bessel-function form for Δφ between recombination and today; it appears heuristic, especially since H(z) is not constant, and the matter+Λ background is not described by simple Bessel solutions.  
- The “O(1)” label is then used downstream to assert Δφ/f_a ∼ 10^-2 in Section 2.2, which is not clearly derived from Eq. (1). The link between 0.24 and “∼10^-2” is not transparent.  
Required fix:  
- Either provide a brief derivation or a precise reference demonstrating that the field displacement has the stated form involving J_0(m/H_0), or replace Eq. (1) with a numerically integrated expression over H(z) that you actually used to get β ≈ 0.27°.  
- Clarify how the number 10^-2 for Δφ/f_a follows from the cosmological evolution (e.g., show a numerical estimate or a robust scaling argument) instead of leaving it as an asserted “ratio of field displacement to decay constant over the Hubble time.”  
- Clean up the notation by dropping redundant J_0(0) in the denominator or explicitly explain why it appears.

---

P2-M4 (MAJOR) – Dimensional consistency and definition of “f_photon × C0”, Eq. (5), p.2  
Offending text: “The effective photon coupling parameter: f_photon × C0 = 1.73 ± 0.44 (order-unity, consistent with the ALP prediction without fine-tuning).”  
Problem: The usual ALP-photon coupling is g_{aγ} = C_0 / f_a with dimension [mass^-1]. Here, the paper introduces “f_photon × C0” as dimensionless but gives no clear prior definition. If f_photon is meant to be f_a in units of 10^17 GeV or similar, that needs to be spelled out. Otherwise, the dimensional analysis is obscure: a product of a decay constant and a dimensionless C0 should have dimensions of mass, not be dimensionless O(1).  
Required fix:  
- Explicitly define f_photon, including its units and normalization convention (e.g., f_photon ≡ (M_Pl / f_a) or f_a / 10^19 GeV).  
- Rewrite Eq. (5) to use a clearly dimensionless parameter (like g_{aγ} × M_Pl or f_a / M_Pl) if you want to talk about order-unity values, and ensure the text uses consistent notation.  
- Check that the numerical value 1.73 ± 0.44 is consistent with the β combination in Eq. (4) and the assumed normalization.

---

P2-M5 (MAJOR) – Status and reproducibility of MCMC analysis, Section 3.3 and Table 1, p.2–3  
Problem: The MCMC analysis is central to claims about the posterior on β, C_aγ×θ_i, and the Bayes factor. However:  
- Sample sizes are very small by PRD standards (720–6840 samples), yet used to quote percent-level uncertainties on β and C_aγ×θ_i and a Bayes factor ln B = 5.17±(not given), suggesting high precision.  
- There is no reference to a specific sampler or code (e.g., emcee, Cobaya, etc.), no mention of number of chains, burn-in removed, or effective sample size per parameter.  
- The Bayes factor is computed via Savage-Dickey with an assumed flat prior on β; this needs careful treatment given the modest sample size and potential sensitivity to binning.  
Required fix:  
- Provide more detailed methodological information: sampler, number of chains, steps, burn-in fraction, and effective sample sizes per parameter.  
- At least briefly discuss the expected numerical uncertainty on ln B given the sample sizes and show that the quoted values (5.17, 4.48, 5.86) are stable under reasonable changes in prior range and binning.  
- Consider either running longer chains (as you yourself suggest) or downgrading claims about the robustness of the Bayes factor, explicitly noting that ln B values are indicative and may shift with more thorough sampling.

---

P2-M6 (MAJOR) – Abstract and conclusions overselling what is “proved”, p.1,5–6  
Problem: Instructions request that the abstract should summarize what the paper *proves*, not what it hopes to prove. Currently, the abstract states:  

- “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061° (3.9σ from zero)… The Bayes factor in favor of nonzero rotation is ln B = 5.17 (indicative; prior-dependent…). We forecast that LiteBIRD… will test this prediction at 9σ significance.”  

But (i) the ACT DR6 result is not verifiably published (P2-E2/E8), (ii) part of the 3.9σ significance and Bayes factor rely on that unpublished ACT number, and (iii) systematic uncertainties on the Minami-Komatsu method are recognized in Section 6 as potentially ∼0.1–0.3°. Under those conditions, the paper does not *prove* a 3.9σ detection from robust, fully public data; it demonstrates that such a detection would be obtained if one accepts certain preliminary ACT inputs and specific modeling assumptions.  
Required fix:  
- Reword the abstract and conclusion to clearly distinguish between empirical results based solely on published data (e.g., WMAP+Planck from Eskilt & Komatsu) and those dependent on preliminary ACT inputs or new combinations.  
- Qualify the 3.9σ and ln B claims as conditional on both the adopted dataset combination and the assumed Gaussian summary-likelihood, and explicitly mention the systematic caveats upfront (not only in Section 6).  

---

P2-M7 (MAJOR) – Claim about “matter-bounce non-Gaussianity fNL = −35/8” being “complementary and independent test”, Section 6 p.5  
Problem: The statement “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].” references a specific numeric fNL = −35/8 that is not traceable to any published paper; the only reference is Golden 2026b, which is labeled as a “Companion paper, submitted simultaneously” with no arXiv ID. There is no way to verify that this predicted fNL actually exists or that it is indeed a robust matter-bounce prediction.  
Required fix:  
- Either provide a public reference (arXiv ID) where this fNL prediction is derived, or remove the specific value −35/8 and merely state that “matter-bounce models often have characteristic non-Gaussianity signatures; see separate work in preparation.”  

---

P2-M8 (MAJOR) – Length relative to contribution  
Problem: The manuscript is 6 pages and fairly concise, so overall length is not excessive. However, some sections (Bounce cosmology, ECH motivation, matter-bounce non-Gaussianity) rely on non-public companion papers, diluting the main contribution (ALP birefringence prediction and forecast) with largely speculative context.  
Required fix:  
- For PRD, the paper would be stronger if it focused tightly on the ALP birefringence prediction and data analysis. Consider shortening or heavily condensing Section 5 and the parts of Section 6 that discuss ECH gravity and matter-bounce non-Gaussianity unless you can fully ground them in published literature. A 5-page version focusing on ALP + birefringence + LiteBIRD forecast would likely be sufficient.

---

P2-m1 (MINOR) – Typographical inconsistency: “Caγ” vs “C_aγ” vs “C0”, p.2–3  
Problem: The coupling is variously denoted as gaγ, Caγ, C0, and “C free” in different parts of the text and Table 1. This is not strictly a citation issue but creates ambiguity when interpreting Eq. (2) and Run 2 priors.  
Required fix:  
- Standardize notation. For example, use C_γ or C_0 consistently for the anomaly coefficient and g_{aγ} = C_0/f_a for the coupling, and explicitly define “C” in “Run 1 (C = 8 fixed)”.  

---

P2-m2 (MINOR) – Citation format inconsistency for LiteBIRD Collaboration, p.3,6  
Problem: The LiteBIRD reference is given as “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky cmb polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023. doi: 10.1093/ptep/ptac150.” The title capitalization is slightly off compared to the published version (“CMB” rather than “cmb”). Also check exact author/collaboration name; ADS lists a specific collaboration author list.  
Required fix:  
- Align the title capitalization and collaboration citation with ADS or the journal version and confirm the DOI (10.1093/ptep/ptac150) is correct (it is).[4]  

---

P2-m3 (MINOR) – Self-calibration method attribution, Section 6 p.5  
Problem: The text attributes “Minami-Komatsu self-calibration method” but only cites Minami & Komatsu 2020 PRL, which is correct for the methodology, but other follow-ups (e.g., Eskilt & Komatsu 2022 PRD) refine or extend it. The phrase “self-calibration method” might be better documented with both references when discussing limitations.  
Required fix:  
- When explaining systematic caveats of the self-calibration method, add a citation to Eskilt & Komatsu 2022 PRD, which discusses some of the method’s assumptions in more detail.

---

P2-m4 (MINOR) – Figure 1 & 2 captions lacking explicit dataset/source description, p.4–5  
Problem: The figures are described qualitatively, but the captions do not explicitly restate which data (Planck NPIPE, ACT DR6) and priors go into the plotted posteriors. For reproducibility and clarity, PRD typically expects captions to be self-contained.  
Required fix:  
- Amend the figure captions to specify which datasets and priors were used for each run and what likelihood form was assumed (Gaussian summary-likelihood vs. full EB spectrum).  

---

P2-n1 (NIT) – Redundant phrasing “generic initial misalignment θi ∼ O(1) is generic”, Abstract p.1  
Offending text: “…and the initial misalignment angle θi ∼ O(1) is generic.”  
Problem: Mild redundancy (“∼ O(1)” and “generic” convey similar ideas).  
Required fix:  
- Rephrase to “and a generic initial misalignment angle θ_i ∼ O(1).”

---

P2-n2 (NIT) – Minor typographical issues: “coeﬀicient” with ligature artifact, p.2,7  
Problem: “coeﬀicient” appears with a ligature artifact instead of “coefficient” in several instances.  
Required fix:  
- Replace with standard ASCII “coefficient” throughout.

---

P2-n3 (NIT) – Section 4 equation formatting, p.3  
Offending text:  
“Significance = 0.27 / 0.03 = 9σ.”  
Problem: Dimensions are implicit; this is clear but could be slightly more explicit (e.g., the ratio of central value to forecasted σ).  
Required fix:  
- Optionally clarify as “Significance = β_pred / σ(β) = 0.27° / 0.03° ≈ 9σ.”

---

## Summary recommendation

REJECT

The manuscript’s central quantitative claims depend critically on (i) ACT DR6 birefringence results that are not yet verifiably published or citable, and (ii) a mischaracterized “Eskilt et al. joint Planck + ACT analysis” that does not correspond to any existing paper. Several key references are in preparation or missing arXiv IDs, and some claims about prior work (Fujita et al., Namikawa et al.) and about a specific f_NL prediction are not traceable to public literature. In combination with the improper juxtaposition of significance values from different pipelines and the reliance on non-public “companion” papers, this falls short of PRD’s standards for citation integrity and evidentiary rigor. The conceptual idea may be of interest, but a substantially cleaned-up and better documented version, based solely on fully public datasets and properly citable analyses, would be required as a fresh submission.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-M7 (MAJOR) – Arithmetic and σ-counts for combined β (Eq. 4, Abstract, Sec. 3.2, Sec. 6)  
Problem: Multiple σ and “consistency” statements are either arithmetically off or presented without the corresponding quantitative comparison.  
Findings:  
- Eq. (4) gives β_combined = 0.242 ± 0.061°. The text says “(3.9σ from zero).” 0.242/0.061 ≈ 3.97, i.e., ~4.0σ, not 3.9σ. If 3.9σ is from a more exact internal computation, this should be stated; otherwise the number is just rounded down inconsistently.  
- In Sec. 6, claim (2) says: “The prediction matches the combined Planck + ACT measurement at 1σ.” The “prediction” is β ≈ 0.27°, and the “combined measurement” is 0.242 ± 0.061°. The difference is |0.27 − 0.242| = 0.028°, so the pull is 0.028/0.061 ≈ 0.46σ; that is within 0.5σ, not “at 1σ.” This is a quantitative overstatement of the tension and should be either corrected (“within 0.5σ”) or the actual Δ/σ explicitly quoted.  
- Throughout, “consistent with the 3.6σ isotropic birefringence signal (β_obs = 0.342 ± 0.094°)” is used, but 0.342/0.094 ≈ 3.64σ. If “3.6σ” is rounded from the Eskilt & Komatsu value, that is fine, but you should state clearly in the body that the consistency between β ≈ 0.27° and β_obs = 0.342 ± 0.094° corresponds to a difference of |0.27 − 0.342| = 0.072°, i.e. 0.77σ, and not just use vague “consistent with” language.  
Required fix:  
- Recompute and state σ-counts with explicit Δ/σ wherever claims like “consistent” or “at 1σ” are made; correct “3.9σ” to the properly rounded value or explain the origin.  
- Replace “matches … at 1σ” with a precise quantitative statement (e.g., “differs by 0.46σ”).  
- In at least one place in the body, spell out the numerical difference between your prediction (0.27°) and both β_combined and β_obs with the corresponding σ-units, rather than only qualitative language.

---

P2-M8 (MAJOR) – Arithmetic and logic of LiteBIRD forecast exclusion (Sec. 4, Eq. 10)  
Problem: The forecast section mixes two distinct hypotheses and σ-counts without clearly stating which null is being tested.  
Findings:  
- Eq. (10) correctly computes 0.27/0.03 = 9; that is fine for “If the signal is real, LiteBIRD will detect it at 9σ.”  
- However, the next sentence: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.” Strictly speaking, if the true model prediction is β = 0.27° and an experiment measures 0 ± 0.03° (assuming Gaussian errors), the discrepancy is |0.27 − 0|/0.03 = 9σ, so the arithmetic is consistent. The issue is that this is not stated as a *model–data tension,* but as “excluded at 9σ” without acknowledging that the quoted σ is again relative to the *experimental error*, not a joint model+measurement uncertainty. As written, the text implicitly uses the same 9σ twice but for different null hypotheses (β = 0 vs. β = 0.27°) without making that logical structure explicit.  
Required fix:  
- Clarify that both 9σ statements are relative to LiteBIRD’s projected σ(β) ≈ 0.03°, and explicitly say “the measurement would lie 9σ away from the model prediction β = 0.27° under Gaussian errors,” so it is clear you are talking about a single-σ benchmark, not a fully propagated model+data uncertainty.

---

P2-M9 (MAJOR) – Dimensional consistency and normalization in Eq. (2) and the 0.27° prediction (Sec. 2.2)  
Problem: The passage connecting Eq. (2) to β ≈ 0.27° is dimensionally and numerically opaque.  
Findings:  
- Eq. (2) is written as  
  \( \beta = \frac{g_{a\gamma}}{2}\Delta\phi = \frac{C_0}{2f_a}\Delta\phi \approx \frac{C_0 \theta_i}{2} \times O(1).\)  
  If \(g_{a\gamma} = C_0/f_a\) has dimensions [mass\(^{-1}\)], then \(\Delta\phi\) has dimension [mass], β is dimensionless, and \(\Delta\phi/f_a\) must be dimensionless. However, in Sec. 2.1 you effectively set \(\Delta\phi \approx f_a \theta_i \times O(1)\), so \(\Delta\phi/f_a \approx \theta_i \times O(1)\). This would give β ≈ (C0 θ_i/2) × O(1), which is *order unity in radians.*  
- Immediately after, the text says: “For C0 ∼ 1, θi ∼ 1: the cosmological field evolution gives Δφ/fa ∼ 10^-2 … yielding β ≈ C0 θi × 5 × 10^-3 rad ≈ 0.27°.” That implicitly assumes \(\Delta\phi/f_a \approx 10^{-2}\), in contradiction with the preceding heuristic \(\Delta\phi \approx f_a \theta_i × O(1)\), which would give \(\Delta\phi/f_a = O(1)\). The “O(1)” factors in Sec. 2.1 and the “10^-2” in Sec. 2.2 cannot both be correct without further explanation.  
- There is no explicit parameterization of the “cosmological integration factor” that turns O(1) into 10^-2. As written, the derivation of “5 × 10^-3 rad” is not reproducible: the reader cannot see how the combination of m ∼ H0 and cosmological evolution produces a suppression of two orders of magnitude.  
Required fix:  
- Make the scaling of \(\Delta\phi/f_a\) explicit: either replace Eq. (1)–(2) with the actual integral you evaluate numerically and quote a concrete value (e.g., \(\Delta\phi/f_a ≈ 1.0 × 10^{-2} θ_i\) for m = H0), or add a short derivation showing how the H(z)-weighted evolution gives the 10^-2 factor.  
- Remove or reconcile the conflicting “O(1)” description for \(\Delta\phi/f_a\). If the cosmological integral gives a suppression, state that explicitly (e.g., “\(\Delta\phi ≈ 0.02 f_a θ_i\)”) and keep the same factor consistently between Sec. 2.1 and 2.2.

---

P2-M10 (MAJOR) – Dimensional and definitional opacity of “f_photon × C0” (Eq. 5, Sec. 3.2) beyond earlier critique  
Problem: In addition to the baseline issue that the product of a decay constant and a dimensionless anomaly coefficient is not dimensionless, there is a further internal inconsistency with the parameter ranges used in the MCMC.  
Findings:  
- Eq. (5) defines “The effective photon coupling parameter: f_photon × C0 = 1.73 ± 0.44.” But in Sec. 3.3 you state priors “C_aγ flat on [1, 30] (Run 2 only)” and then quote \(C_{a\gamma} × θ_i = 3.4 ± 1.1\) as an “order-unity” parameter. There is no clear mapping given between “C0” used in Eq. (2) and “C_aγ” used in the MCMC, nor between “f_photon” and the decay constant f_a.  
- Numerically, if β_combined = 0.242° ≈ 4.22 × 10^-3 rad and your “prediction” is β ≈ C0 θ_i × 5 × 10^-3 rad (Sec. 2.2), then matching these implies C0 θ_i ≈ 0.844. The value “f_photon × C0 = 1.73 ± 0.44” is not obviously related to this combination; without a definition of f_photon’s normalization, the reader cannot reconstruct how Eq. (5) is derived from Eq. (4).  
Required fix:  
- Explicitly define the relationship between C0 and C_aγ, and between f_photon and f_a, including all unit normalizations (e.g., f_photon ≡ f_a/10^18 GeV or similar).  
- Show the step that connects β_combined and the theoretical expression β ≈ (C0 θ_i/2)(Δφ/f_a) to the inferred “f_photon × C0 = 1.73 ± 0.44”; i.e., give an explicit formula and plug in the numbers in the text so that the reader can verify the arithmetic.

---

P2-M11 (MAJOR) – β-posterior comparisons across models and to “β_obs” without quantitative pulls (Fig. 2 caption vs. body, Sec. 3.3)  
Problem: The comparison of β posteriors in Sec. 3.3 and Fig. 2 overuses qualitative phrases like “no tension” and “consistent with” without quoting the actual differences in σ units.  
Findings:  
- Sec. 3.3: “The posterior on β from the ALP model (Run 1) β_ALP = 0.336 ± 0.107° compared to the model-independent fit β_free = 0.344 ± 0.096° and the observed value β_obs = 0.342 ± 0.094°. The ALP model reproduces the observed birefringence with no tension.”  
  The differences are:  
  • β_ALP vs β_obs: Δ = 0.336 − 0.342 = −0.006°, combined σ ≈ √(0.107² + 0.094²) ≈ 0.142°, pull ≈ 0.04σ.  
  • β_free vs β_obs: Δ = 0.002°, pull ≈ 0.01σ.  
  These are indeed negligible, but the text never shows these explicit pulls; it simply asserts “no tension.”  
- Fig. 2 caption: “All three are consistent with each other and with the observed value β_obs = 0.342 ± 0.094°.” Again, no numbers are shown; the reader must infer consistency from overlapping curves.  
Required fix:  
- Add a short quantitative statement in Sec. 3.3, e.g., “the difference between β_ALP and β_obs is 0.04σ,” to make the “no tension” claim precise.  
- Optionally, indicate in the figure caption or body where these numerical pulls are discussed so that the qualitative “consistent” language is backed by explicit calculations.

---

P2-m1 (MINOR) – Internal cross-reference: Bayes factor section and notation (Sec. 3.4 vs Abstract)  
Problem: The abstract says “ln B = 5.17 (indicative; prior-dependent, see Sec. 3.4).” Sec. 3.4 indeed gives ln B = 5.17 and shows the dependence on the β prior. The cross-reference is basically correct but could be clearer about what aspect is “prior-dependent.”  
Finding:  
- Sec. 3.4: “The evidence is prior-dependent: ln B = 4.48 for β ∈ [0°, 2°] and ln B = 5.86 for β ∈ [0°, 0.5°].” There is no mention of any numerical uncertainty from finite sampling, which was noted earlier as a limitation. The abstract’s “indicative; prior-dependent” phrasing partly walks this back, but only w.r.t. priors, not numerical noise.  
Required fix:  
- In Sec. 3.4, add one sentence noting that, in addition to prior-dependence, ln B carries a numerical uncertainty due to finite sampling (as you already acknowledge in Sec. 3.3), so the values 5.17, 4.48, 5.86 should be interpreted with that caveat. This will better align the abstract’s “indicative” language with the detailed discussion.

---

P2-m2 (MINOR) – Figure-body consistency and labeling (Fig. 1 & Fig. 2 vs. text)  
Problem: The captions qualitatively describe what the figures show, but some parameter labels and priors used in Sec. 3.3 are not explicitly mirrored in the figures, which can hinder reproducibility.  
Findings:  
- Fig. 1 caption: “Triangle plot from the extended ALP MCMC (Run 2, C free). The posterior on the coupling-misalignment product Caγ × θi is centered at 3.4 ± 1.1…” This matches Eq. (8). However, the text in Sec. 3.3 uses “Caγ flat on [1, 30]” and “θi flat on [0.01, π]” but the figure as described does not indicate these prior ranges.  
- Fig. 2 shows β posteriors “across all three model configurations.” The caption correctly names them, but the body uses both C and C0/C_aγ notation, which could confuse the correspondence between “ALP with C = 8 fixed” in the figure and the parameters described in the text.  
Required fix:  
- Ensure the figure legends/axis labels (not shown in the text excerpt) use exactly the same parameter names as in Sec. 3.3 (C_aγ, θ_i, β), or add a clarifying sentence to the captions tying the plotted parameters explicitly to the equations (e.g., “C in the legend corresponds to C_aγ in Eq. (8)”).  
- Optionally note in the captions or in Sec. 3.3 that the plotted posteriors incorporate the priors given (e.g., “flat prior on θ_i ∈ [0.01, π]”), to improve transparency.

---

P2-m3 (MINOR) – Abstract faithfulness and strength of claims about “no fine-tuning” vs. body (Abstract vs. Sec. 2.2 & 6)  
Problem: Beyond the earlier flagged need for quantitative support, there is a smaller internal mismatch between the nuanced discussion in Sec. 3.3 and the stronger abstract language.  
Findings:  
- Abstract: “f_photon × C0 = 1.73 ± 0.44 (order-unity, no fine-tuning).”  
- Sec. 3.3 acknowledges that the combined constraints on Caγ × θ_i (3.4 ± 1.1) derive from modest sample sizes and that “Neff ∼ 1,000 limit the precision of tail estimates and evidence calculations.” There is no quantitative measure of how large a fraction of prior volume yields values near 3.4, only the statement “consistent with O(1) values.”  
Required fix:  
- Either soften the abstract to “order-unity values, suggestive of no strong fine-tuning” or add in the body a very brief quantitative explanation (e.g., approximate posterior fraction in the prior range) that justifies stating “no fine-tuning” in the abstract. Without that, the abstract overstates what the body has actually quantified.

If you want, I can now go through each equation one-by-one for a more exhaustive dimensional analysis, but the main new issues above are the ones most likely to draw attention in a rigorous PRD review beyond your initial set.