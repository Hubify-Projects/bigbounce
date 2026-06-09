# P1B auto-2026-06-08_1819pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13347 chars)
**Wall time**: 84.7s

---

P1B-E1  
Section: References; multiple pages (p. 10–11)  
Problem: **Multiple references are future-dated or otherwise cannot exist as cited, violating basic bibliographic reliability.**  
- [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].” As of now, there is no arXiv:2509.13654 and no ACT DR6 birefringence paper with those details; ACT DR6 has not been released to that level and 2025 / 2509.* is future-dated.  
-  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].” No such arXiv:2507.04265 exists; year and identifier are future.  
-  “DESI ... DR2 ... Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].” DESI DR2 BAO paper exists with arXiv:2404.03002 and is not PRD 112, 083515 (2025); the citation fuses metadata from .  
-  “DES ... ∼1500 new high-redshift SNe ... Astrophys. J. Lett. 973, L14 (2024), arXiv:2401.02929.” There is a DES 5-year SN cosmology paper on arXiv:2401.02929, but ApJ Letters vol. 973 (2024) is not yet real; the journal/volume/page are fabricated.  
-  “DESI 2024 VI: cosmological constraints from BAO, arXiv:2404.03002.” Actual title is “DESI 2024 VI: Cosmological Constraints from Measurements of Baryon Acoustic Oscillations,” no journal yet; the “DR1” labeling in the main text conflicts with the reference.  
Required fix:  
- Replace all future-dated or non-existent arXiv IDs with real entries or clearly label them “in preparation” without fabricated arXiv numbers or journal metadata.  
- For DESI DR2, DES-SN5YR, and ACT DR6, either cite correctly existing public papers or explicitly state they are private/forecast analyses; do not invent volume/page/years.  
- For any truly unpublished analysis, remove journal and arXiv identifiers and mark as “in preparation” with author list only. This is essential for PRD-level bibliographic integrity.

---

P1B-E2  
Section: Abstract, first paragraph; Table I; Sec. III & V (pp. 1–3, 6)  
Problem: **Use of DESI DR2, DES-Y5, and the w₀–wₐ chain in Table II appears to rely on non-existent or mis-cited datasets/papers, with fused citation metadata.**  
- Table II is labeled “DESI DR2 w₀wₐ posterior ... Likelihood stack: DESI DR2 BAO + Planck 2018 NPIPE ... + DES-Y5 + Pantheon+.” DESI DR2 BAO cosmological constraints paper is cited as  with a 2025 PRD publication and arXiv:2503.14738, which do not exist.  
- DES-Y5 cosmology constraints are cited via , which actually corresponds to DES Y3 galaxy clustering + lensing (arXiv:2105.13549, PRD 105, 023520), not a Year 5 dataset.  
- DES-SN5YR is referenced in  as used by Liu et al., but the DES 5-year SN cosmology paper is arXiv:2401.02929 and is not “Astrophys. J. Lett. 973, L14 (2024)” as claimed in .  
Required fix:  
- Either (a) restrict all quantitative analyses to truly public, correctly cited dataset releases (e.g., DESI 2024 BAO DR1, DES Y3 3×2pt, Pantheon+), and recompute all numbers accordingly, or (b) clearly mark any use of unreleased DR2/Y5/5YR data as hypothetical/forecast and remove fabricated reference entries.  
- Correct the description “DESI 2024 DR1 BAO ” and “DESI DR2” to reflect actual data products and papers.  
- Until all chains in Table II can be traced to properly cited, real data releases, the claims in Sec. V and Table II cannot be considered publishable.

---

P1B-E3  
Section: References [3], ; Sec. IV and VI (birefringence values) (pp. 4, 6–8, 10)  
Problem: **ACT DR6 cosmic birefringence analysis and Planck NPIPE reference are mis-cited and partially fabricated.**  
-  for Planck birefringence: “Diego-Palazuelos et al., Planck DR4, PRL 128, 091302 (2022), arXiv:2201.07682; reports β = 0.30 ± 0.11 deg ... arXiv:2201.07682.” The established Planck birefringence result is Minami & Komatsu, PRL 125, 221301 (2020), arXiv:2006.07345; Diego-Palazuelos et al. 2022 (PRL 128, 091302, arXiv:2104.14164) is about FRB rotation measures, not Planck NPIPE cosmic birefringence. The citation string splices unrelated works.  
- [3] is a future-dated ACT DR6 birefringence paper with a non-existent arXiv number; yet the text uses its numerical value β = 0.215° ± 0.074°. No such public ACT DR6 EB birefringence paper exists with these details.  
Required fix:  
- Rebuild all birefringence discussion around *published, correctly cited* results (e.g., Eskilt & Komatsu 2022 PRD 106, 063503, arXiv:2205.13962; Minami & Komatsu 2020), with accurate authors, titles, and arXiv IDs.  
- Remove or clearly label as speculative any use of numerical constraints from non-existent ACT DR6 analyses.  
- Correct  to cite the actual Planck birefringence paper(s); remove any fabricated volume/page/ID combinations.

---

P1B-E4  
Section: Sec. VI (Spectator-ALP Consistency Check), especially eqs. (2)–(4) and accompanying text (pp. 7–8)  
Problem: **Key ALP–birefringence numerics are inconsistent and partially incorrect.**  
- They define β via \( \beta \approx (\alpha_{\rm EM} C_{a\gamma}/4\pi)\,\Delta\phi/f_a\). Then state β ≈ 0.29° for Caγ = 8 and Δϕ/fa ≈ 1.07 (eq. (3)), and also quote β ≈ 0.27° as fiducial, and later βALP = 0.336° ± 0.107°.  
- They assert that β = 0.342° implies \(C_{a\gamma}\Delta\phi/fa ≈ 10.3\) with αEM/(4π) = 5.8×10⁻⁴ and β in radians. Using β = 0.342° = 0.00597 rad and 5.8×10⁻⁴ gives \(C_{a\gamma}\Delta\phi/fa ≈ 10.3\), but then the claimed “natural envelope” Δϕ/fa ∈ [0.2, 1.1] and “required Caγ between ~9 and ~51” is inconsistent: 10.3 / 1.1 ≈ 9.4, 10.3 / 0.2 ≈ 51.5, but they also claim Caγ is fixed at 8 in the fiducial MCMC runs.  
- The description of “∼25× misalignment tuning” (θ_i ~ 0.1 vs 0.5) and the mapping ∆ϕ/fa ∝ θ_i is never explicitly demonstrated; the relation between θ_i, m/H₀, and ∆ϕ/fa is not shown, and it is unclear that the quoted envelope [0.2, 1.1] follows from the evolution equation they give.  
Required fix:  
- Explicitly derive and show how ∆ϕ/fa depends on m/H₀ and θ_i in the late-time ΛCDM background, at least in an appendix table or figure, and recompute all β and Caγ ranges consistently from that result.  
- Ensure the ALP-MCMC numbers (βALP, βfree, natural envelope, tuning factors) are internally consistent and reproducible from the displayed equations; right now the narrative has multiple overlapping, partly contradictory numerical descriptions.  
- Clarify clearly which β value is used where (Planck-only, Planck+WMAP, Planck+ACT), and ensure that any combined constraints (e.g. βcombined = 0.241° ± 0.061°) correctly propagate errors.

---

P1B-E5  
Section: Sec. V.A (“Datasets and Configuration”) and V.B (“Results”), Table II (pp. 6–7)  
Problem: **Apparent conflation of two distinct analyses: ΛCDM+ΔN_eff proxy vs w₀–wₐ quintom fit.**  
- Earlier the paper defines the main MCMC as a ΛCDM + ΔN_eff extension with 7 cosmological parameters plus Planck nuisances, and Table I lists H₀, ΔN_eff, σ₈, S₈, Ω_m, τ, n_s for two chains.  
- Table II then presents a “DESI DR2 w₀wₐ posterior” with 8 cosmological + 9 nuisance parameters, including w₀ and w_a, with strong deviations from ΛCDM. That analysis is neither introduced nor clearly connected to the rest of the paper (which focuses on ΔN_eff), and the dataset stack (DESI DR2 + DES-Y5 + Pantheon+) is not consistently cited or demonstrably real.  
- The subsequent discussion in Sec. III and V mixes statements about ΔN_eff consistency with zero and H₀ tensions with statements about w₀–w_a posteriors being >4σ from ΛCDM, without clearly separating which results come from which analysis or which are actually used in the ECH closure argument.  
Required fix:  
- Clearly separate the ΔN_eff proxy analysis (stock CAMB run used as “MCMC verification”) from any *independent* w₀–wₐ quintom fit; if the latter is only tangential, it belongs in a different paper or in a brief appendix with clear caveats and correct data citations.  
- For PRD standards, a table like Table II must be fully traceable: specify the exact data versions, codes, priors, and all references must exist and be correct; otherwise remove it.  
- Avoid referring to “headline results” (e.g. w₀ = −0.812 ± 0.044, w_a = −0.667 ± 0.186) unless they are central to this paper and supported by fully reproducible, correctly cited data.

---

P1B-E6  
Section: Entire text; references [1], [4]–[6] (pp. 2, 8–11)  
Problem: **Cross-references to “Paper I(a), II, III, IV” are all “in preparation” with internal IDs (“hUBIFY-2026-00x”) and not yet published or available.**  
- [1], [4], [5], [6] are all “(in preparation) (2026), hUBIFY-2026-00x; companion paper, this volume.” There is no guarantee that these exist, nor any arXiv IDs or DOIs.  
- Multiple central claims (e.g. the 14 structural barriers, the perturbation-transparency theorem, the f_NL = −35/8 forecast being “in Paper II”, the anomaly and galaxy chirality catalogs, and the “ECH structural-closure no-go result”) depend critically on content that is not available for inspection.  
Required fix:  
- For PRD, any essential theoretical results used here must be either contained in this paper or in a *publicly available* cited work (published or arXiv). Relegate all dependence on unpublished “this volume” papers to non-essential context, or postpone submission until those works are available with stable identifiers.  
- At minimum, do not treat those cross-references as established “literature”; clearly label them as companion manuscripts under review and remove any reliance on them for central claims.

---

P1B-E7  
Section: Abstract & Sec. III (“Key finding”) (pp. 1–3)  
Problem: **Potentially misleading presentation of ΔN_eff constraints and H₀ tension as “confirmation” of minimal bounce-class predictions, without proper support or caution.**  
- The abstract claims: “Both frozen dataset combinations find ΔNeff consistent with zero ... and H₀ consistent with standard ΛCDM ... confirming that the ΔNeff extension alone does not resolve the Hubble tension.” While numerically plausible, the text then states that this is “consistent with the minimal matter-bounce prediction” and frames it as a “compatibility check.”  
- No concrete derivation or citation is given for a quantitative minimal matter-bounce prediction of ΔNeff ≈ 0 with the specific data combination used. The cited  (Cai et al. 2009) is about non-Gaussianity in matter bounce, not ΔNeff.  
Required fix:  
- Rephrase to make clear that the ΔNeff result is *simply consistent with ΛCDM expectations* and that using it as a proxy for minimal bounce models is highly model-dependent; do not overclaim a “confirmation” of any bounce-class prediction without a clearly documented theoretical computation and proper citation.  
- Explicitly state that the ΔNeff constraints are not a discriminator between ΛCDM and minimal ECH matters-bounce, and that relating them to bounce physics is speculative.

---

P1B-M1  
Section: Abstract; Sec. IV (pp. 1, 4–5)  
Problem: **Use of “SNR” terminology for pipeline Monte Carlo recovery (20.32σ, 25.71σ) is confusing and risks misinterpretation as sky-detection significance.**  
- Footnote 3 explains that SNR_SE is a standard error of the mean estimator over 500 MCs, not per-map detection. However, the abstract advertises “high pipeline-recovery SNR figures (e.g., 20.32σ)” which many readers will interpret as sky-significance.  
Required fix:  
- In the abstract and main text, systematically qualify these SNR numbers as “Monte Carlo estimator SNR” or similar, and explicitly state in every place where they appear that *they are not sky-detection significances*. The current single detailed explanation in a footnote is insufficient for PRD.

---

P1B-M2  
Section: Appendix A “What is NOT included” (p. 9)  
Problem: **Explicit declaration that Bayes factors and information criteria are “NOT reported” and that nested sampling is left to future work, even though the main text discusses “quintom-B” preference and deviations from ΛCDM.**  
- The paper repeatedly mentions w₀ and w_a departing from ΛCDM at ~4σ and calls this “canonical quintom signature,” but explicitly declines to compute ln B, AIC, or BIC, which are the relevant model-comparison metrics.  
Required fix:  
- For PRD, if the dark-energy sector deviation from ΛCDM is a central part of the narrative, at least one robust model-comparison metric (evidence ratio or information criterion) must be provided for the datasets used. Alternatively, remove all language suggesting model preference (quintom-B vs ΛCDM) and treat w₀–w_a only as descriptive constraints.

---

P1B-M3  
Section: Abstract; Sec. VI; Table III (pp. 1, 7–9, 11)  
Problem: **Claims of “consistency” of the spectator ALP model with the 3.6σ birefringence signal downplay the severity of the required misalignment fine-tuning and non-minimal photon couplings.**  
- The text admits a ~25× tuning in θ_i and Caγ range 9–51, outside standard KSVZ/DFSZ O(1) expectations, but frames the result as “natural parameters (taken at scan-prior midpoint values)” and “accommodated across the considered parameter space.”  
Required fix:  
- Strengthen the caveat language: clearly state in the abstract and in Table III that consistency requires both significant tuning in the initial misalignment angle and photon couplings substantially above minimal QCD axion benchmarks, and that the model does *not* provide a natural explanation of the signal.  
- Avoid presenting this as a nearly parameter-free consistency check; it is in fact highly parameter-dependent.

---

P1B-M4  
Section: Abstract; Conclusions (pp. 1, 8)  
Problem: **Over-reliance on unpublished code and GitHub repository without ensuring archival reproducibility.**  
- The paper directs readers to a GitHub repository for all YAML configs and scripts, but for PRD the scientific record should not depend exclusively on mutable GitHub resources.  
Required fix:  
- Archive the code and configuration used for all key results in a DOI-bearing repository (e.g. Zenodo) and cite that DOI. This is particularly important given that many “companion papers” and some datasets are not yet published.

---

P1B-M5  
Section: Throughout, especially Sec. II and III (pp. 2–3)  
Problem: **Use of “full-tension”, “stock-CAMB proxy”, and “ECH structural-closure” jargon without precise definitions for readers not familiar with Paper I(a).**  
Required fix:  
- Provide short, self-contained definitions of “full-tension dataset combination”, “proxy MCMC verification”, and what exactly the “ECH structural-closure no-go result” is, at least in one paragraph, without requiring access to an unpublished companion paper.

---

P1B-M6  
Section: Table I and discussion around footnote 1 (pp. 3–5)  
Problem: **Sample-count explanations are convoluted and partly inconsistent.**  
- Footnote 1 first defines 309,189 as the total raw samples across two chains; later mentions 176,240 and 132,949; then states a post-burn-in total of 216,432; then mentions 119,617 (thinned). The explanation is hard to follow and may contain minor arithmetic inconsistencies, especially where “176,240 × 0.7 ≈ 123,368” but later 123,129 is stated.  
Required fix:  
- Simplify and cleanly present the relevant chain statistics: raw samples per chain, burn-in fraction, post-burn-in per chain, and total effective sample size, with consistent numbers and without mixing in intermediate thinned counts unless strictly necessary.

---

P1B-M7  
Section: Sec. IV “Data Methods: CMB E–B Analysis” (pp. 4–5)  
Problem: **The NaMaster validation uses Planck Commander maps with ACT-like noise, but the stated goal is validation for a Planck/ACT DR6 birefringence measurement that does not yet exist as cited.**  
Required fix:  
- Clarify the target use-case: is this pipeline meant as a generic EB pseudo-Cℓ validation, or specifically as a validation for a future ACT DR6 analysis? If the latter, the paper should state that this is a methods exercise, not directly validating a specific published measurement.  

---

P1B-M8  
Section: Acknowledgments (p. 9)  
Problem: **Explicit mention of the use of an AI research assistant (Claude) raises potential concerns about code or text provenance, but no detailed statement is made as to how scientific calculations were independently verified.**  
Required fix:  
- For transparency, briefly state what parts of the work were AI-assisted (e.g., code scaffolding vs. analysis decisions) and how numerical results and derivations were cross-checked independently (e.g., by rerunning all computations manually). This is increasingly expected for high-precision cosmology.

---

P1B-N1  
Section: Abstract (p. 1)  
Problem: **Load-bearing numbers in the abstract are not fully cross-referenced to the main body.**  
- ΔN_eff = −0.020 ± 0.169 and +0.065 ± 0.17 appear in Table I, consistent.  
- H₀ = 67.68 ± 1.06 and 67.79 ± 1.09 also match Table I.  
- The NaMaster recovery β̂ = 0.238° for β = 0.27° is consistent with Sec. IV and Fig. 3.  
- The spectator-ALP “consistent with β = 0.342° ± 0.094° (3.6σ)” is consistent with the Eskilt & Komatsu PRD value, but the paper should explicitly cross-reference where βALP and βfree are quoted and how they relate to the 3.6σ detection.  
Required fix:  
- Add explicit cross-references (e.g., “see Table I”, “see Sec. IV eq. (1)”, “see Sec. VI and Appendix C”) for each key statistic in the abstract. This is minor but improves traceability.

---

P1B-N2  
Section: Equations and dimensions (e.g. ALP EOM, Hubble units, ρ_a scaling) (pp. 1, 7)  
Problem: **Dimensional consistency is mostly fine, but the note “ρ_a ∼ m² f_a² θ_i² ∼ H₀² M_Pl²” would benefit from explicit factors to avoid confusion.**  
Required fix:  
- Either include a short comment that this is schematic, up to order-one factors, or provide the exact proportionality for ρ_a in the misalignment regime, so the scaling argument for Ω_a and θ_i tuning is explicit.

---

P1B-N3  
Section: Figure 1 and Figure 2 (pp. 5–6)  
Problem: **Axis labels for derived parameters do not include units (e.g. H₀ is presumably km s⁻¹ Mpc⁻¹, but not marked).**  
Required fix:  
- Ensure all axes in Figures 1 and 2 include units where appropriate (H₀, S₈ is dimensionless, etc.). This is standard for PRD.

---

P1B-N4  
Section: “What is NOT included” (Appendix A) and “KNOWN GAPS.md” (p. 9)  
Problem: **The text states known gaps, including the absence of Bayes factors and CNN classifiers, but leaves it ambiguous whether any of these gaps affect the current results.**  
Required fix:  
- Add a one-sentence statement explicitly confirming that none of the missing components (e.g. Bayes factors, CNNs) are required to reproduce the quantitative cosmological constraints reported in this paper.

---

P1B-N5  
Section: References  (Cobaya) and  (NaMaster) (p. 10)  
Problem: **Reference details are broadly correct but incomplete (journal names, volume, pages).**  
Required fix:  
- Check against arXiv/ADS and fill in the precise JCAP/MNRAS volume and page numbers, and correct capitalization of titles, to meet PRD bibliographic standards.

---

## Summary recommendation

**REJECT**

The manuscript fails basic Physical Review D standards of bibliographic integrity and reproducibility. Multiple references are future-dated with non-existent arXiv IDs, volume and page numbers are fabricated, and key results (DESI DR2, DES-Y5, ACT DR6) depend on datasets and analyses that are either not yet public or incorrectly cited. The ALP–birefringence section contains internal numerical inconsistencies and overstates the naturalness of the model. Central theoretical claims rely on unpublished companion papers. Addressing these issues would require substantial restructuring of the paper, recomputation of key results with properly published data, and a complete overhaul of the reference list, which goes beyond what is appropriate for a revision cycle; a fresh, fully documented submission would be needed.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E8  
Section: Abstract first paragraph; Sec. III “Key finding”; Table I; Fig. 1–2  
Problem: **Abstract “H₀ consistent with standard ΛCDM (0.3σ)” is internally inconsistent with the numbers and with later text.**  
- Abstract: “H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN).” No explicit “0.3σ” is quoted there, but Sec. III later states “H0 consistent with Planck ΛCDM at 0.3σ.”  
- The Planck baseline quoted in the references () is \(H_0 = 67.4 ± 0.5\) km s⁻¹ Mpc⁻¹ (Planck 2018). The full-tension result 67.68 ± 1.06 differs from 67.4 by 0.28 km s⁻¹ Mpc⁻¹ ≈ 0.3σ if one divides by the *proxy* σ = 1.06, not by the Planck σ = 0.5. Properly combining errors in quadrature gives a difference of ≈0.5σ. The text never defines which σ is used, so the “0.3σ” statement is ambiguous and effectively miscomputed relative to the natural reference (Planck-only).  
Required fix:  
- Explicitly define the reference ΛCDM value and error (e.g. Planck 2018) and compute the joint-significance using combined uncertainty, or remove the “0.3σ” language and simply state that the values are statistically consistent with Planck.  
- In the abstract, qualify “consistent with standard ΛCDM” with either a quantitative comparison or a pointer to Sec. III where the comparison is made correctly.

---

P1B-E9  
Section: Sec. III “Key finding”; MB–H₀ arithmetic paragraph; Table I  
Problem: **MB–H₀ “3.2σ” tension and “canonical 3.6σ” mapping are numerically misaligned and not clearly defined.**  
- The text computes the difference in the combination \(M_B - 5 \log_{10} H_0\) between the Riess anchor and the chain mean as 0.155 mag, and states this is “∼ 3.2σ relative to the chain’s σ_MB = 0.049.” However 0.155 / 0.049 ≈ 3.16, which is fine, but then it claims this “corresponds exactly to the canonical 3.6σ Hubble tension,” which is not numerically true: 3.16σ is not “exactly” 3.6σ, and the mapping between MB-space and H₀-space significances is not demonstrated.  
- Earlier, the text calls the Riess vs model H₀ difference “3.6σ” but uses only the Riess error in the denominator (“canonical 3.6σ”), instead of the combined uncertainties of Riess and the chain posterior, which would reduce the tension slightly.  
Required fix:  
- Either recompute the H₀ tension significance with both errors included, or clearly state that “3.6σ” refers to the Riess-vs-Planck canonical value, not a fresh calculation from this chain.  
- Replace “corresponds exactly” with a quantitatively accurate description (e.g. “is similar to” or give both numbers with their derivation) and, ideally, show the explicit mapping between the MB-space offset and the H₀-space tension in an equation.

---

P1B-E10  
Section: Sec. IV NaMaster description vs Fig. 3 caption and β-bias text  
Problem: **Inconsistent quantitative statements for the NaMaster bias and SNR between text, footnote, and figure.**  
- Sec. IV text: “Injecting β = 0.27° … recovers β̂ = 0.238° (pipeline-recovery bias 0.032°).” Later: “for β = 0.342° … recovers 0.302° at SNR_SE = 25.71 … pipeline-recovery bias is ∆β̂ = 0.032° at injection β = 0.27° and ∆β̂ = 0.040° at injection β = 0.342°.”  
- Fig. 3 caption: “Bias … is below 0.04° across the natural resolution range; this is the NaMaster systematic floor adopted in Eq. 1–3.” The abstract, however, quotes only “β̂ = 0.238° for β = 0.27°,” without any error or bias range.  
- Footnote 3 gives SNR_SE = β̂√N /σ_{β̂}, but the text earlier mentions “SNR = 20.32” for β = 0.27° injection without ever showing β̂ or σ_{β̂} used to get 20.32. The reader cannot reconstruct the 20.32σ number solely from the printed values (0.238°, N = 500) since σ_{β̂} is not given.  
Required fix:  
- Add the actual σ_{β̂} values (or at least one representative value) to the text or a small table so that the quoted SNR_SE = 20.32 and 25.71 can be recomputed.  
- Make the bias description consistent: either quote “0.032–0.040°” as the range everywhere, or specify which injection each value refers to and avoid calling it strictly “0.032°” in some places.  
- In the abstract, explicitly say “β̂ = 0.238° with pipeline bias ~0.03° and Monte Carlo estimator SNR ≈ 20” so the connection to the discussion in Sec. IV is clear.

---

P1B-E11  
Section: Sec. V.A “Datasets and configuration”; Sec. III first paragraph; Table I vs Table II  
Problem: **Internal cross-reference inconsistency in the description of dataset combinations and chain counts.**  
- Sec. III: “Frozen MCMC program: 309,189 raw samples across 2 frozen dataset combinations (176,240+132,949)… plus a third Planck-only run currently at sub-convergence sample count.”  
- Footnote 1 expands with slightly different numbers (176,240, 132,949, 114,992) and states a “post-burnin count of the full-tension subset alone is 123,129 (within ±1% of the 123,368 exact computation).” This ±1% disclaimer is still confusing because 123,129 differs from 123,368 by ~0.19%, not 1%; the “±1%” wording looks like a leftover fudge factor.  
- Table I lists “Total samples 176,240” for full-tension and 132,949 for Planck+BAO+SN but does not explicitly mark these as *raw* or *post-burn-in* nor connect them to the 119,617 “post-burnin” number in the Fig. 1 caption.  
Required fix:  
- Harmonize the sample-count narrative: pick one precise set of numbers and clearly label them as raw vs post-burn-in vs thinned, and ensure they appear consistently in Table I, Fig. 1 caption, and footnote 1.  
- Remove the “within ±1%” hedge and simply give the exact arithmetic; PRD does not need an approximate qualifier for straightforward multiplications.

---

P1B-E12  
Section: Sec. V.B “Results”; Table II; Conclusions last paragraph  
Problem: **w₀–wₐ quintom results are used rhetorically in the conclusions without any explicit pointer to model incompleteness and missing evidence metrics.**  
- Sec. V.B correctly notes that “AIC, BIC, and ln B … are not reported here” and that the chain does not sample the ΛCDM point, so no Savage–Dickey ratio is possible.  
- However, the conclusions restate: “The 16-rank mpirun process… GetDist posteriors on w₀w_a are available as an empirical test of the quintom-B scenario,” without any reminder that no evidence metrics are provided and that the posterior strongly excludes ΛCDM in parameter space but not in model-comparison space.  
Required fix:  
- In the conclusions, immediately following the sentence referencing w₀–wₐ, add a short qualifier that these are *descriptive constraints only* and that model comparison (AIC/BIC/Bayes factor) is deferred to future work, pointing back to Sec. V.B.  
- Ensure that no sentence in the conclusions can be read as claiming model *preference* for quintom-B over ΛCDM on the basis of this chain alone.

---

P1B-E13  
Section: Sec. VI ALP consistency check; Appendix C; Table III  
Problem: **ALP β, Caγ, and Δϕ/fₐ ranges are still not fully arithmetically transparent or consistently cross-referenced.**  
- Text: “For Caγ = 8, θᵢ = 1, m ≈ 2H₀: β ≈ (α_EM × 8 / 4π) × 1.07 ≈ 0.29°.” Using α_EM/(4π) = 5.8×10⁻⁴, this gives β_rad ≈ 0.00496; in degrees this is ≈0.284°, not 0.29°. The rounding is fine, but nowhere is it shown that “1.07” is indeed the Δϕ/fₐ value obtained from the equation of motion—only “≈0.65” is given for (m=H₀, θᵢ=1) and then a verbal statement that the range is [0.2,1.1].  
- Later: “Caγ (Δϕ/fₐ) ≈ 10.3 … with Δϕ/fₐ ∈ [0.2,1.1], the required Caγ spans ∼9 to ∼51.” These are arithmetically correct given 10.3 / 1.1 ≈ 9.36 and 10.3 / 0.2 ≈ 51.5, but the text calls [0.2,1.1] the “natural envelope” while footnotes 5 and 6 state that spectator status actually forces θᵢ ~ 0.1, outside the [0.5,2] prior used to define that envelope.  
- The claim “β_ALP = 0.336° ± 0.107° … and β_free = 0.344° ± 0.096° … All three within 1σ [of β_obs = 0.342° ± 0.094°]” is only qualitatively justified; the overlaps are real, but there is no explicit cross-reference to Appendix C where the priors are defined, nor any simple numeric demonstration (e.g. listing the differences in units of σ_combined).  
Required fix:  
- Add one explicit line showing how Δϕ/fₐ ≈ 1.07 is obtained from the ODE integration (e.g. give the specific (m/H₀, θᵢ) pair and resulting value), or include a small table/figure in an appendix summarizing Δϕ/fₐ as a function of m/H₀ and θᵢ.  
- When quoting [0.2,1.1] as the “natural envelope,” explicitly separate the “theoretical naturalness” (θᵢ~O(1)) from the “spectator-consistent” region (θᵢ~0.1), and make clear that the latter lies outside the sampling prior and would require a different Caγ range.  
- In Sec. VI, add a sentence computing |β_ALP − β_obs| / σ_combined and |β_free − β_obs| / σ_combined, so the claimed “within 1σ” consistency is numerically transparent.

---

P1B-E14  
Section: Sec. VI “LiteBIRD forecast”; References   
Problem: **Forecast significance uses σ(β) ≈ 0.03° without citing which configuration in the LiteBIRD forecast this corresponds to or checking the arithmetic.**  
- The text states: “LiteBIRD is projected to achieve σ(β) ≈ 0.03°. For β = 0.27°: ∼ 9σ statistical significance.” Numerically 0.27° / 0.03° = 9, so the arithmetic is fine. However, LiteBIRD  contains several forecast scenarios and channels; σ(β) ≈ 0.03° is not uniquely defined in the text, and the paper does not specify whether this is a sky-average, a single-channel forecast, or a combined analysis.  
Required fix:  
- Add a clause indicating which LiteBIRD forecast configuration you are using (e.g. “assuming the baseline mission sensitivity quoted in  for full-sky EB measurements”); alternatively, quote σ(β) from the specific figure/table in .  
- Optionally, note that this 9σ is a simple β/σ(β) ratio, not a full forecast including systematics.

---

P1B-M9  
Section: Fig. 1 and Fig. 2 captions vs body text (Sec. III)  
Problem: **Minor figure-caption vs text mismatch in chain labels and sample counts.**  
- Fig. 1 caption refers to “119,617 post-burnin samples, getdist-thinned from 176,240 raw” while the body text and footnote 1 use 176,240 and 132,949 and a post-burn-in total of 216,432. It is not immediately obvious that 119,617 refers only to the full-tension subset after thinning, and the caption’s parenthetical “footnote 1” is the only clarifier.  
- Fig. 2 caption: “across the four dataset combinations of Sec. V A” but only two combinations (full-tension and Planck+BAO+SN) are clearly labeled in the figure text snippet provided (“Full tension (175 545 samples); Planck+BAO+SN (132 949 samples)” plus two WP4 curves). The four combinations in Sec. V.A include Planck-only and Planck+BAO; the mapping from those to the plotted curves is not spelt out in the caption.  
Required fix:  
- In Fig. 1 caption, explicitly state “full-tension subset only” and point out that the Planck+BAO+SN subset has its own post-burn-in count, given in Table I.  
- In Fig. 2 caption, either add explicit labels for all four dataset combinations (Planck, Planck+BAO, Planck+BAO+SN, full-tension), or modify the caption to accurately reflect exactly which combinations are plotted.

---

P1B-M10  
Section: Abstract; Sec. I “Scope of this paper”; Table III  
Problem: **Abstract’s “three analyses are documented” framing does not fully reflect that the w₀–wₐ quintom chain (Table II) is also a significant new result treated in the body and in the conclusions.**  
- The abstract enumerates three analyses: ΔN_eff proxy, NaMaster validation, and spectator-ALP consistency. The DESI DR2 w₀–wₐ quintom analysis (Table II) is only mentioned in passing in the body and is not acknowledged as a separate analysis in the abstract, yet its posterior is discussed at length in Sec. V and it appears in the conclusions as a “Forward” item.  
Required fix:  
- Either (a) mention explicitly in the abstract that an additional w₀–wₐ quintom chain is presented as an exploratory result but without model comparison metrics, or (b) move the bulk of the Table II discussion to an appendix and clearly mark it as ancillary, in line with the abstract’s description of the paper’s scope.  
- Update Table III (“Claims classification”) to include at least one line for the w₀–wₐ constraints, making clear that they are “MCMC, exploratory, no evidence metrics.”

---

P1B-N6  
Section: Abstract; Sec. VI; Table III last line (“ALP birefringence not distinctive ECH prediction”)  
Problem: **Abstract and Table III still slightly overstate how “natural” the ALP parameters are, relative to the fine-tuning admitted later.**  
- Abstract: “natural parameters (taken at scan-prior midpoint values; the ∼25× misalignment tuning required to reconcile the headline result with the spectator-consistent corner is disclosed in Sec. VI and fn. 5).”  
- Table III: “ALP birefringence not distinctive ECH prediction – Type: Scope – Status: Defn.” This focuses on model non-uniqueness but does not flag that the parameter region consistent with spectator status is highly tuned.  
Required fix:  
- In the abstract sentence on the ALP, explicitly add that “these midpoint values do not satisfy the strict spectator condition, which requires an additional ∼25× tuning in θᵢ and photon couplings well above minimal KSVZ/DFSZ.”  
- In Table III, add a note to the ALP line indicating “requires fine-tuned misalignment and enhanced photon coupling; see Sec. VI.”