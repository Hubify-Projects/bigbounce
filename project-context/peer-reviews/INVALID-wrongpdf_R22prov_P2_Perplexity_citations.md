# P2 R22prov — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13434 chars)
**Wall time**: 90.6s

---

P2-E1 (ESSENTIAL) – Missing and placeholder citations in Introduction  
- **Location:** Sec. 1, p.1  
- **Problem:** Multiple references are written as `?` instead of proper citations:  
  - “The Planck HFI analysis [?] reported β = 0.35 ± 0.14◦ (2.5σ)…”  
  - “The ACT DR6 analysis confirmed the signal…” has no explicit citation.  
- **Required fix:**  
  - Replace `?` with the correct Planck HFI birefringence analysis reference (e.g. Minami & Komatsu, Planck 2018 HFI polarization rotation paper) and ensure the quoted value β = 0.35 ± 0.14° and 2.5σ appear in that source.  
  - Add explicit ACT DR6 birefringence reference with the quoted β value and significance, and verify that “comparable significance” and “Combined, the evidence exceeds 3.5σ” follow from the cited numbers (you will need to show the combination explicitly or quantify it with a reference).  
  - All `?` placeholders must be replaced by fully specified citations with arXiv IDs or journal references, checked against arXiv.org/ADS.  

P2-E2 (ESSENTIAL) – Missing standard-coupling reference and fused notation  
- **Location:** Sec. 2.2, p.2  
- **Problem:**  
  - Equation (2) defines \(g_{a\gamma} = \alpha_{\rm EM} C_{a\gamma}/(2\pi f_a)\) “in the conventions of ?” with `?` a missing citation. This is a load‑bearing convention for a central observable and must be traceable to a standard reference (e.g. standard ALP reviews).  
  - The abstract uses **C₀**, the body uses **Cₐγ**, and later sections introduce **C** without careful definition. This is a fused/inconsistent notation for the same physical anomaly coefficient.  
- **Required fix:**  
  - Insert a specific, verified reference for the ALP–photon coupling conventions (e.g. a standard axion/ALP review on arXiv with the same normalization) and check the normalization matches Eq. (2) exactly.  
  - Unify the notation: pick one symbol (e.g. **Cₐγ**) and use it consistently in the abstract and all sections; if **C₀** is retained, clearly state once that \(C_0 \equiv C_{a\gamma}\). Ensure the MCMC table “ALP (C = 8 fixed)” also uses the same symbol.  

P2-E3 (ESSENTIAL) – LiteBIRD forecast citation missing  
- **Location:** Sec. 4, p.4  
- **Problem:**  
  - “LiteBIRD is projected to achieve σ(β) ≈ 0.03◦ on the isotropic birefringence angle [?]…” again uses `?` and no bibliographic information.  
- **Required fix:**  
  - Insert a specific LiteBIRD forecasting paper or mission overview that explicitly quotes or supports σ(β) ≈ 0.03°. Verify this number (and its dependence on calibration strategy) is traceable to that work.  

P2-E4 (ESSENTIAL) – Companion papers cited with `?` and “Paper I(a)” with no bibliographic entry  
- **Location:** Sec. 5, p.4; Sec. 6, p.5; Sec. 7, p.6  
- **Problem:**  
  - Multiple references to a “companion Paper I(a) [?]” and “the companion paper [?]” and “14‑barrier catalog” exist, but no concrete reference (title, authors, year, arXiv ID) is provided. This is not acceptable for PRD; “Paper I(a)” is internal bookkeeping.  
- **Required fix:**  
  - Replace “Paper I(a)” and “companion paper [?]” with finalized, citable references: give the exact title, authors, and status (submitted/accepted/published) and arXiv ID if available. Ensure the bibliography includes these entries.  
  - Remove version‑style labelling (“Paper I(a)”) from the main text; use descriptive titles instead (e.g. “the companion ECH‑gravity analysis by Golden [ref]”).  

P2-E5 (ESSENTIAL) – Missing references for “matter‑bounce non‑Gaussianity” and ALP literature claims  
- **Location:** Sec. 7, p.6  
- **Problem:**  
  - “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [?].” No reference is given for this specific value or its derivation.  
  - “We emphasize that the ALP birefringence model class is well-studied in the literature [?]. Fujita, Murai, Nakatsuka & Tsujikawa (2021)… and Namikawa, Murai & Naokawa [?]…” contain either `?` or incomplete citation information.  
- **Required fix:**  
  - Provide fully specified references for the matter‑bounce fNL result (authors, title, arXiv ID or journal) and confirm that fNL = −35/8 is explicitly stated there.  
  - Give complete citations for Fujita et al. (2021) and Namikawa et al. with correct author lists, titles, journal/arXiv IDs. Ensure that the claims you make (e.g. “Planck‑scale ALP naturally produces β ∼ 0.3°”; “superior ALP mass constraints using the full Planck EB spectrum”) are explicitly supported by the cited papers.  

P2-E6 (ESSENTIAL) – Abstract’s quoted “Eskilt et al. joint Planck+ACT” number does not match text body, and no citation is given  
- **Location:** Abstract, p.1; Sec. 3.1, p.2–3  
- **Problem:**  
  - Abstract: “βobs = 0.342 ± 0.094◦ from the Eskilt et al. joint Planck + ACT analysis” is quoted, but no explicit reference is given anywhere for “Eskilt et al.”  
  - Sec. 3.1 later: “we use the Eskilt et al. joint analysis value βobs = 0.342 ± 0.094◦ , which differs because it fits the full EB cross-spectrum…”—again with no citation.  
- **Required fix:**  
  - Insert the full reference (Eskilt’s first name, collaborators, paper title, arXiv ID/journal) in the references section and cite it at both locations.  
  - Check the exact values in that paper: confirm that the quoted βobs and error bar exactly match the chosen dataset/analysis combination in Eskilt et al.; if not, correct the numbers and their stated significance.  

P2-E7 (ESSENTIAL) – Arithmetic inconsistency in combined β and stated σ (significance)  
- **Location:** Sec. 3.2, Eq. (4), p.3  
- **Problem:**  
  - Input values: Planck NPIPE β = 0.30 ± 0.11°, ACT DR6 β = 0.215 ± 0.074°. From standard inverse-variance weighting, the combined estimate is  
    \[
    \sigma_{\rm comb} = (1/0.11^2 + 1/0.074^2)^{-1/2} \approx 0.062°,
    \]
    which matches the quoted ±0.061°.  
    The combined mean is  
    \[
    \beta_{\rm comb} \approx (0.30/0.11^2 + 0.215/0.074^2)/(1/0.11^2 + 1/0.074^2) \approx 0.243°,
    \]
    consistent with 0.242°.  
  - However, the significance from zero is then \(\beta_{\rm comb}/\sigma_{\rm comb} ≈ 0.242/0.061 ≈ 3.97σ\), not “3.9σ” if rounded consistently. This is minor numerically but you should clarify how the significance is computed (e.g. using more precise internal numbers).  
  - More importantly, the abstract claims: “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061◦ (3.9σ from zero)” but clearly both datasets used here are *already* birefringence analyses; you must show they are precisely consistent with the cited underlying Eskilt et al. analysis and that your summary-likelihood treatment does not double-count any information or mix incompatible null procedures.  
- **Required fix:**  
  - Explicitly state the formula used to obtain the 3.9σ, and verify that rounding is consistent across text and abstract.  
  - State clearly whether the Planck NPIPE value and the ACT DR6 value are independent measurements with compatible systematics and null procedures; if different null tests are used, you must explicitly note that their significances are *not directly comparable* whenever juxtaposed, in compliance with the instruction on non‑comparable σ’s.  

P2-E8 (ESSENTIAL) – σ values from different procedures juxtaposed without explicit “not directly comparable” caveat  
- **Location:** Abstract, p.1; Sec. 1, p.1–2; Sec. 3.1–3.3, pp.2–3; Fig. 2 caption, p.4  
- **Problem:**  
  - Multiple σ‑level significances are placed side by side or referenced in the same context, with different datasets and analysis pipelines:  
    - Planck HFI: 2.5σ; Planck NPIPE: 2.7σ; ACT DR6: 2.9σ; combined summary likelihood: 3.9σ; Eskilt joint analysis: 3.6σ; hypothetical LiteBIRD: 9σ.  
  - Nowhere in the text is there a clear statement every time they are juxtaposed that these significances are not directly comparable due to differing data cuts, foreground modeling, calibration strategies, and priors.  
- **Required fix:**  
  - Add a brief sentence each time you place different σ‑values side by side (e.g. in Sec. 1 and in Sec. 3) explicitly noting that “these significances use different analysis pipelines and null procedures and are therefore not directly comparable; we quote them for rough orientation only.”  

P2-E9 (ESSENTIAL) – Internal‑audit language and version‑history artifacts  
- **Location:** Sec. 5, p.4; Sec. 6, p.5; Sec. 7, p.6  
- **Problem:**  
  - Phrases like “companion Paper I(a)”, “14-barrier catalog”, “companion paper” with no explicit reference are clearly internal project labels and version bookkeeping rather than stable literature references, violating PRD style.  
- **Required fix:**  
  - Replace all internal naming (e.g., “Paper I(a)”) with proper published or arXiv’d citations; remove any version‑log flavour (“Paper I(a)”) and instead refer to “the companion ECH paper [ref]”.  

P2-E10 (ESSENTIAL) – Naturalness and “no fine‑tuning” claims presently unsubstantiated by citations  
- **Location:** Abstract, p.1; Sec. 2.2, p.2; Sec. 7, p.6  
- **Problem:**  
  - Repeated strong claims: “no fine‑tuning”, “order-unity, no fine-tuning”, “Planck-scale ALP naturally produces β ∼ 0.3◦”, “cosmological-constant-class tuning rather than an ALP-specific one” are made with no clear quantitative or literature‑context support. In a PRD methods paper, such statements must either be rigorously quantified (e.g. priors, p‑values for fine‑tuning, references to existing measures) or softened and clearly labelled as interpretive.  
- **Required fix:**  
  - Either (a) supply specific references where these naturalness assessments are quantified and show that your parameter choices fall within those measures, or (b) rephrase claims to be descriptive and modest (“we find that order‑unity θi and Cₐγ produce the observed β without requiring extremely small or large dimensionless parameters, aside from the standard m ~ H₀ tuning”) and drop “no fine‑tuning” rhetoric.  

P2-M1 (MAJOR) – LiteBIRD forecast: simplified significance statement and dependence on systematics  
- **Location:** Sec. 4, Eq. (10), p.4; Abstract  
- **Problem:**  
  - You treat the forecasted LiteBIRD significance as simply 0.27/0.03 = 9σ with no discussion of systematics, potential covariance with other parameters, or the self-calibration degeneracies you discuss earlier. The text says “depending on the self-calibration strategy and systematic error budget”, but Eq. (10) and the 9σ claim effectively ignore these issues.  
- **Required fix:**  
  - Clarify that the “9σ” is a *pure Gaussian statistical* forecast assuming the quoted σ(β), and explicitly state that the true detection significance could be lower if systematic uncertainties or self‑calibration degeneracies degrade the effective sensitivity. Tie this explicitly to the LiteBIRD reference you provide.  

P2-M2 (MAJOR) – Energy-density constraint algebra and stated tuning factor  
- **Location:** Sec. 5, Eq. (11), p.4–5  
- **Problem:**  
  - Eq. (11) gives
    \[
    \rho_\phi(z=0) \approx \frac12 m^2 f_a^2 \theta_i^2 \Rightarrow \Omega_\phi(z=0) \approx \frac16 \left(\frac{m}{H_0}\right)^2 \left(\frac{f_a}{M_{\rm Pl}}\right)^2\theta_i^2.
    \]
    For \(m \sim H_0\), \(f_a \sim M_{\rm Pl}\), and θᵢ ~ 1, you claim Ωϕ ∼ 0.17. This is an order‑of‑magnitude statement, but the factors 1/6 and numerical relation between MPl and ρcrit need to be checked and justified. Right now no reference or derivation is provided; it is stated as if obvious.  
  - You then state that satisfying “strict spectator regime” Ωϕ ≪ 1 implies θᵢ suppressed to “∼ 0.05 θnat ≈ 0.22 (a ∼ 25× fine-tuning)”—but 0.22 is ~1/4.5, not 1/25. The “25×” seems inconsistent with the quoted factor of 0.05.  
- **Required fix:**  
  - Provide the derivation of Eq. (11) from ρcrit = 3 H₀² MPl² and show explicitly how the numerical factor 0.17 arises for θᵢ = 1.  
  - Correct the tuning factor: if θnat ≈ 1 and θᵢ ≈ 0.22, this is ~4.5× suppression, not 25×. If you intend a 25× energy‑density suppression rather than amplitude suppression, state that unambiguously and show the math.  

P2-M3 (MAJOR) – MCMC description incomplete for reproducibility and for citation of underlying data  
- **Location:** Sec. 3.3, p.3; Table 1  
- **Problem:**  
  - You describe three MCMC runs and quote R̂ − 1 < 0.01 and Neff ~ 1000, but provide no details of the likelihood implementation: which exact data vector, covariance, and theoretical model were used, and how they relate to the Planck/ACT/Eskilt analyses you cite. There is no explicit reference for the data likelihood or for the covariance matrix you used. PRD will expect enough detail that another group can reproduce these posteriors.  
- **Required fix:**  
  - Add explicit references to the Planck and ACT birefringence-likelihood implementations you rely on (or specify if you built a Gaussian summary-likelihood from the quoted β values only).  
  - If you use only Gaussian summary-likelihoods, say so clearly for each run, and state that this is an approximation to the full EB-spectrum likelihood used in Eskilt et al. Provide a short justification.  

P2-M4 (MAJOR) – Novelty claims vs. prior literature not fully cross‑checked  
- **Location:** Sec. 7, p.6; Conclusion, p.6  
- **Problem:**  
  - You claim: “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.”  
  - However, you also state that Fujita et al. (2021) already showed Planck‑scale ALPs can naturally produce β ∼ 0.3°, and Namikawa et al. have superior mass constraints. Without carefully checking those works (titles, models, parameter choices, statistical methods), it is not yet demonstrated that your identification is new. In the present manuscript, this remains an unsupported claim of novelty.  
- **Required fix:**  
  - Carefully compare your parameter choices and inference pipelines to those of Fujita et al., Namikawa et al., and any other relevant ALP‑birefringence papers. Explicitly state what is different—e.g., “we use Planck NPIPE + ACT DR6 in a combined summary-likelihood analysis, whereas Fujita et al. use only Planck 2018 HFI, and we focus specifically on fa ~ MPl and m ~ H₀ rather than scanning a broad parameter space.”  
  - Remove or soften any novelty/largest/first claims that cannot be clearly distinguished from those prior works.  

P2-M5 (MAJOR) – Abstract vs body alignment on datasets and σ levels  
- **Location:** Abstract, p.1; Sec. 3, pp.2–3  
- **Problem:**  
  - Abstract states: “We perform a Gaussian summary-likelihood inference using Planck HFI and ACT DR6 data, finding β = 0.242 ± 0.061◦ (3.9σ from zero)…”.  
  - Body: Sec. 3.1 actually uses Planck NPIPE (β = 0.30 ± 0.11°) and ACT DR6, and Eskilt et al. for the MCMC. “Planck HFI” in the abstract is too vague and potentially misleading, since multiple Planck HFI birefringence analyses exist.  
- **Required fix:**  
  - Make the abstract consistent with the body by explicitly stating that the summary likelihood uses the Planck NPIPE birefringence result and ACT DR6, and that the MCMC uses the Eskilt joint Planck+ACT EB-spectrum analysis.  

P2-M6 (MAJOR) – Data/procedure for ACT DR6 not clearly linked to a specific paper  
- **Location:** Sec. 3.1, bullet list, p.2  
- **Problem:**  
  - “ACT DR6 [?]: β = 0.215 ± 0.074◦ (2.9σ)” is not accompanied by a full citation.  
- **Required fix:**  
  - Provide the exact ACT DR6 birefringence reference, and verify that β and σ match the quoted numbers and that your use of a Gaussian approximation is justified.  

P2-M7 (MAJOR) – Overreliance on summary β values rather than original EB spectra, but stated as if fully general  
- **Location:** Abstract and Sec. 3  
- **Problem:**  
  - The analysis combining Planck NPIPE and ACT DR6 uses only 1D β summary statistics and assumes Gaussian errors and independence. This is a much weaker and more assumption‑laden treatment than using the full EB spectra with their covariances. Yet the abstract and main text present the result almost as an equivalent alternative to the Eskilt full‑spectrum analysis.  
- **Required fix:**  
  - Make explicit in both abstract and Sec. 3 that your summary‑likelihood approach uses only the reported β and uncertainties and is an approximation that neglects possible non‑Gaussianity or correlations in the errors.  

P2-M8 (MAJOR) – Article length vs. contribution  
- **Location:** Whole manuscript (7 pages)  
- **Problem:**  
  - For a methods paper whose primary new element is a simple parameter identification in an already studied model plus a straightforward Gaussian combination of published β estimates, 7 pages is at the upper end of what is warranted. Some sections (e.g. extended naturalness rhetoric, qualitative bounce-cosmology motivation, and repeated restatement of the β ~ 0.27° claim) feel verbose relative to the technical content.  
- **Required fix:**  
  - Consider tightening the text by ~1–2 pages: focus on the concrete new calculation/forecast and remove redundant prose and long qualitative motivation paragraphs, especially in Sec. 6–7, preserving only what directly supports your quantitative claims.  

P2-m1 (MINOR) – Notation consistency (C vs C₀ vs Cₐγ vs Caγ)  
- **Location:** Abstract, Sec. 2.2, Sec. 3.3, Fig. 1 caption, Sec. 7  
- **Problem:**  
  - The anomaly coefficient is referred to variously as C₀, Caγ, C, and Cₐγ, which is confusing.  
- **Required fix:**  
  - Choose a single notation and stick to it; clarify once that it is an integer anomaly coefficient of O(1–10).  

P2-m2 (MINOR) – Units and axis-label audits  
- **Location:** Figures 1–2 (pp.3–4)  
- **Problem:**  
  - Figures are referenced but their axis labels and units are not described in the text. The captions are brief; they do not specify the parameter units used in the triangle plot or the β distribution. PRD typically expects self-contained captions.  
- **Required fix:**  
  - For Figure 1, specify what each axis represents (e.g., θᵢ (dimensionless), log10(m/eV), Cₐγ, and Caγ×θᵢ) and the units.  
  - For Figure 2, label the axes more explicitly (posterior density of β, showing normalized probability) and state that all β values are in degrees.  

P2-m3 (MINOR) – Minor numerical rounding  
- **Location:** Sec. 3.2 Eq. (4), Sec. 4 Eq. (10)  
- **Problem:**  
  - Some derived significances are quoted with 2–3 significant figures (3.9σ, 9σ) without indicating the precision of the underlying inputs. This is acceptable but could be made more transparent.  
- **Required fix:**  
  - Add “≈” where appropriate (e.g., “≈ 3.9σ”, “≈ 9σ”) to emphasize these are approximate Gaussian significances.  

P2-m4 (MINOR) – Claim “no external funding” and “AI assistants” are acceptable but unusual; should comply with journal policy  
- **Location:** Acknowledgments, p.7  
- **Problem:**  
  - The statement “The author acknowledges the use of AI research assistants during the analysis and manuscript preparation” is fine but PRD may have specific disclosure requirements for AI‑generated content.  
- **Required fix:**  
  - Check PRD’s latest author‑responsibility and AI‑use policy; adjust wording if necessary to match their recommended disclosure format.  

P2-n1 (NIT) – Repetition and stylistic redundancy  
- **Location:** Abstract; Sec. 2.2; Sec. 7  
- **Problem:**  
  - The statement that “fa cancels in β, leaving the prediction dependent only on θi and C0” appears multiple times in nearly identical language.  
- **Required fix:**  
  - Keep the clearest occurrence (probably in Sec. 2.2) and streamline others to refer back to that section.  

P2-n2 (NIT) – Minor phrase duplication  
- **Location:** Sec. 7, first bullet under “The ALP birefringence prediction β ≈ 0.27◦ has three notable features”  
- **Problem:**  
  - Some redundancy in phrasing around “mθ ∼ H0 ultralight-mass tuning” and “cosmological-constant-class tuning shared with all ultralight-ALP cosmic-birefringence proposals.”  
- **Required fix:**  
  - Condense to a single clear statement; avoid repeated jargon.  

P2-n3 (NIT) – Clarify “spectator” terminology  
- **Location:** Sec. 5 and 6  
- **Problem:**  
  - You redefine “spectator” operationally as Ωϕ ≪ 1 with θi ~ 0.22, but earlier text loosely refers to a spectator ALP with θi ~ O(1). This could be confusing to new readers.  
- **Required fix:**  
  - Add a brief clarifying sentence early in Sec. 5 explaining that “in the rest of this work, we reserve the term ‘spectator’ for Ωϕ ≪ 1, which implies θi ~ 0.2 when fa ~ MPl and m ~ H0, as derived below.”  

## Summary recommendation  
**MAJOR REVISIONS**

The manuscript has a potentially publishable core idea (a specific ALP parameter choice plus a LiteBIRD test), but it currently falls short of PRD standards due to missing and placeholder citations, internal bookkeeping references, inconsistent notation, and insufficient clarity about data provenance and comparability of quoted σ‑values. The author must supply full, verified bibliographic information for all cited works (Planck HFI, Planck NPIPE, ACT DR6, Eskilt et al., LiteBIRD forecasts, ALP birefringence papers, matter‑bounce fNL, companion ECH work), ensure all quoted numbers can be traced to those references, correct the energy‑density tuning discussion, and make the methodology and novelty positioning more precise. Once these issues are addressed and the paper tightened, it could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E11 (ESSENTIAL) – Inconsistent use of θᵢ between prediction, energy-density constraint, and “headline” point  
- **Location:** Abstract, Sec. 2.2, Sec. 5, Sec. 7, Conclusion  
- **Problem:**  
  - The abstract claims that for **θᵢ ∼ O(1)** and **C₀ ∼ O(1)** the minimal setup yields **β ≈ 0.27°**, and it repeatedly characterizes the match as occurring with “order‑unity” θᵢ and C₀ and “no fine-tuning.”  
  - Sec. 2.2’s explicit example uses **θᵢ = 1, Cₐγ = 8, m ≈ 2H₀**, giving β ≈ 0.29°, consistent with the abstract narrative of θᵢ ∼ 1.  
  - Sec. 5 then shows that with **θᵢ ∼ 1, fₐ ∼ Mₚₗ, m ∼ H₀**, one obtains **Ωϕ ∼ 0.17**, i.e. not a spectator; to enforce the “spectator” condition it adopts **θᵢ ≈ 0.22 ≈ 0.05 θ_nat**, calling this a “∼ 25× misalignment tuning.” The text explicitly says: “Throughout the rest of this paper, ‘spectator’ refers to the Ωϕ ≪ 1 regime obtained at θᵢ ∼ 0.22.”  
  - However, the abstract, Sec. 7, and Conclusion continue to describe the model as a **spectator ALP with θᵢ ∼ O(1), no fine-tuning**, and to associate the β ≈ 0.27° prediction with that regime, even though the only internally consistent spectator configuration in the text uses **θᵢ ≈ 0.22**, not O(1).  
- **Required fix:**  
  - Clearly distinguish between the **θᵢ ∼ 1, Ωϕ ∼ 0.17 dark-energy-like regime** and the **θᵢ ≈ 0.22 spectator regime**, and state explicitly which parameter point underlies the quoted β ≈ 0.27° “headline” prediction.  
  - Adjust the abstract, Sec. 7, and Conclusion so that the “no fine-tuning” / “θᵢ ∼ O(1)” claims are consistent with the actual choice needed for Ωϕ ≪ 1, or else explicitly label the θᵢ ∼ 1 case as non‑spectator and drop the spectator phrasing there.  
  - Quantify the tuning consistently (see also P2-M2): if the working spectator point is θᵢ ≈ 0.22, the β formula should be re‑evaluated with that value, and the naturalness discussion should be updated accordingly.

P2-E12 (ESSENTIAL) – Bayes factor ln B = 5.17 inconsistent with quoted σ and prior, and insufficiently documented  
- **Location:** Abstract, Sec. 3.3–3.4  
- **Problem:**  
  - Sec. 3.3 gives the data-level constraint β_obs = 0.342 ± 0.094° (Eskilt et al.) and model‑dependent posteriors β_ALP = 0.336 ± 0.107° and β_free = 0.344 ± 0.096°.  
  - Sec. 3.4 reports ln B = 5.17 for a flat prior β ∈ [0°, 1°], with alternative values for [0°, 2°] and [0°, 0.5°], but gives no intermediate quantities (e.g. posterior density at β = 0) or numerical method details. The abstract states the same ln B = 5.17 as a central result.  
  - For a near‑Gaussian posterior with mean μ ≈ 0.34° and σ ≈ 0.095°, the Savage–Dickey ratio with a flat prior width Δβ = 1° would naively give ln B significantly larger than 5 (order 6–7), unless the posterior at β = 0 is inflated relative to the Gaussian approximation; the manuscript does not show how the quoted 5.17 was obtained, nor whether it uses the ALP posterior, the β_free posterior, or the Gaussian summary likelihood.  
- **Required fix:**  
  - Explicitly state **which posterior** (Run 1, Run 2, Run 3, or the summary likelihood) is used for the Savage–Dickey calculation, and provide the formula and numerical inputs (prior width, posterior mean, posterior σ, and posterior density at β = 0) so that ln B can be reproduced.  
  - Check that ln B = 5.17 is consistent with those inputs; if the correct value differs, update all mentions (including the abstract) and use “≈” for approximate values.  
  - Clarify that the Bayes factor is being computed for a **β parameter** (not the full ALP parameter space) and explain how model dimensionality is treated, or else re‑cast the evidence comparison in a way that is consistent with the structure of Runs 1–3.

P2-E13 (ESSENTIAL) – “Order‑unity, no fine‑tuning” claim for f_photon × C₀ lacks definition and dimensional clarity  
- **Location:** Abstract, Sec. 3.2, Sec. 7, Conclusion  
- **Problem:**  
  - Eq. (5) defines an “effective photon coupling parameter” **f_photon × C₀ = 1.73 ± 0.44**, which is described in the abstract as “order-unity, no fine-tuning.” No explicit definition of **f_photon** is provided anywhere (units, relation to g_{aγ}, fₐ, or α_EM), and C₀ is elsewhere identified as a dimensionless integer anomaly coefficient.  
  - As written, **f_photon × C₀** is dimensionless and of order unity by construction; however, without a clear mapping to the fundamental coupling g_{aγ} or fₐ, its physical meaning is opaque, and labeling it as “no fine-tuning” is not justified quantitatively.  
- **Required fix:**  
  - Define **f_photon** explicitly in Sec. 3.2 (e.g. as a rescaled coupling \(\tilde g_{a\gamma}\) or a dimensionless combination of fundamental parameters) and give its units.  
  - Show how Eq. (5) is derived from Eq. (2) and the combined β constraint (Eq. (4)), including any assumed values of θᵢ and m/H₀.  
  - Once the meaning is clear, either justify quantitatively why f_photon × C₀ = 1.73 ± 0.44 constitutes “no fine-tuning” (e.g. relative to a prior range) or tone down the language and describe it as “compatible with O(1) values” without a fine‑tuning claim.

P2-M9 (MAJOR) – Arithmetic / consistency of β ≈ 0.27° prediction with quoted parameter ranges  
- **Location:** Abstract, Sec. 2.2, Sec. 5, Sec. 7  
- **Problem:**  
  - Eq. (1) states that for m/H₀ ∈ [0.5, 3] and θᵢ = 1, the numerical integration yields ∆ϕ/fₐ ≈ 0.2–1.1. For the fiducial m = H₀, θᵢ = 1, ∆ϕ/fₐ ≈ 0.65.  
  - Sec. 2.2 then chooses m ≈ 2H₀, θᵢ = 1, Cₐγ = 8, and quotes β ≈ 0.29°. Using ∆ϕ/fₐ = 1.07 from the text and the coupling normalization in Eq. (2), this number is plausible, but there is no explicit check that the **same β ≈ 0.27°** follows at the “headline” spectator point with **θᵢ ≈ 0.22** adopted in Sec. 5.  
  - The Discussion section and Conclusion repeatedly treat β ≈ 0.27° as the unique model prediction in the “spectator” setup, but that value was derived for θᵢ = 1, not θᵢ ≈ 0.22; for a linear dependence β ∝ θᵢ, reducing θᵢ by ~4.5 would naively reduce β by the same factor. This indicates either (i) an implicit re‑tuning of Cₐγ or m that is not spelled out, or (ii) an inconsistency in how the “prediction” is defined across sections.  
- **Required fix:**  
  - Re‑compute β explicitly at the **actual adopted spectator parameter point** (θᵢ ≈ 0.22, fₐ ∼ Mₚₗ, specific m/H₀ and Cₐγ) and state the resulting β with uncertainty.  
  - If maintaining β ≈ 0.27° at θᵢ ≈ 0.22 requires adjusting Cₐγ or m relative to the earlier “natural” values (e.g. Cₐγ > 8), make those adjustments explicit and discuss their impact on “naturalness.”  
  - Ensure that the abstract’s “β ≈ 0.27°” and the later “prediction matches the combined Planck + ACT measurement at 1σ” statements refer to the same, well‑defined parameter point.

P2-M10 (MAJOR) – Incomplete description of how β from MCMC (Runs 1–3) relates to the summary-likelihood β_combined  
- **Location:** Sec. 3.2–3.3, Fig. 2, Discussion  
- **Problem:**  
  - Sec. 3.2 reports β_combined = 0.242 ± 0.061° from a Gaussian summary likelihood built from Planck NPIPE and ACT DR6. Sec. 3.3 then adopts β_obs = 0.342 ± 0.094° from Eskilt et al. for the MCMC runs and obtains β_ALP = 0.336 ± 0.107° and β_free = 0.344 ± 0.096°.  
  - Fig. 2 and Sec. 7 claim “consistency with data” and “prediction matches the combined Planck + ACT measurement at 1σ,” but it is not clearly stated which β is being compared to which, and whether the differences between 0.242 ± 0.061°, 0.342 ± 0.094°, and 0.336 ± 0.107° have been quantitatively assessed.  
  - The numerical difference between β_combined and β_obs is ≈ 0.10°, which is of order 1σ of the tighter combined constraint. There is no explicit calculation of the **tension** (e.g. ∆β/σ_eff) between summary‑likelihood and full EB results.  
- **Required fix:**  
  - Add a short subsection or paragraph in Sec. 3 explicitly comparing β_combined, β_obs (Eskilt full EB), β_ALP, and β_free: compute ∆β and the combined uncertainty for each pair and state the resulting significance of any differences.  
  - Clarify in the abstract and Sec. 7 which measurement (summary β_combined vs. Eskilt β_obs) is being referred to when claiming “matches the combined Planck + ACT measurement at 1σ.”  
  - Explicitly state that the MCMC runs are based on **Eskilt’s joint full-EB likelihood**, whereas the Gaussian summary likelihood is constructed from published 1D β estimates, and comment on any non‑negligible discrepancy.

P2-M11 (MAJOR) – Dimensional consistency and normalization in Eq. (11) not fully transparent  
- **Location:** Sec. 5  
- **Problem:**  
  - Eq. (11) is written as  
    \[
    ρ_ϕ(z=0) ≈ \tfrac12 m^2 f_a^2 θ_i^2 \Rightarrow Ω_ϕ(z=0) ≈ \tfrac16 \left(\frac{m}{H_0}\right)^2 \left(\frac{f_a}{M_{\rm Pl}}\right)^2 θ_i^2.
    \]  
    However, the printed equation has the unusual “1/2 → 1/6” mapping with no derivation and uses a compact notation that can be misread (as currently typeset, the factor 1/6 is easily confused with a missing 3).  
  - The text claims Ω_ϕ ∼ 0.17 for m ∼ H₀, fₐ ∼ Mₚₗ, θᵢ ∼ 1, but this numerical factor (0.17 vs. 1/6 ≈ 0.167) is not shown explicitly, and it is not clear whether reduced Planck mass or unreduced Planck mass is used, or whether factors of 8π have been absorbed. This undermines dimensional clarity.  
- **Required fix:**  
  - Explicitly derive Eq. (11) step‑by‑step in the text or a short footnote: start from ρ_crit = 3H₀²Mₚₗ² (specifying reduced vs. unreduced Mₚₗ) and show how the coefficient 1/6 and the numerical 0.17 arise.  
  - Clarify the units and definitions of all constants (Mₚₗ, H₀) and ensure that dimensional consistency is evident on the page.  
  - Once clarified, make sure that the “∼ 0.17” value is consistent with the derivation; if not, update it and all subsequent numeric tuning statements that depend on it.

P2-M12 (MAJOR) – LiteBIRD “ruling out ALP explanation at 9σ” phrased too strongly given systematics caveats  
- **Location:** Abstract, Sec. 4  
- **Problem:**  
  - Abstract: “LiteBIRD, with σ(β) ≈ 0.03°, will test this prediction at 9σ significance—either confirming the signal or ruling out the ALP explanation decisively.”  
  - Sec. 4 notes that σ(β) ≈ 0.03° depends on self-calibration strategy and systematics, but Eq. (10) and the following sentence still assert a simple 0.27/0.03 = 9σ and state: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”  
  - This ignores the possibility that **systematic floor, self‑calibration degeneracies, or foreground modeling** could limit LiteBIRD’s effective sensitivity to β, even if the nominal statistical σ(β) is 0.03°.  
- **Required fix:**  
  - Qualify the language in the abstract and Sec. 4 to make clear that **“9σ” is a purely statistical forecast under idealized assumptions**, and that the *practical* ability to confirm or rule out the ALP explanation depends on the achieved systematic error control and calibration strategy.  
  - Explicitly connect this caveat to the LiteBIRD forecasting reference (once added) and to the discussion in Sec. 7 on calibration systematics.

P2-m5 (MINOR) – Figure 2 caption vs. Discussion wording on “all three” posteriors  
- **Location:** Fig. 2 caption, Sec. 3.3, Sec. 7  
- **Problem:**  
  - Fig. 2 caption: “Comparison of β posteriors across all three model configurations (ALP with C = 8 fixed, ALP with C free, and model-independent β).”  
  - Sec. 3.3 then says “All three are consistent with each other and with the observed value β_obs = 0.342 ± 0.094°.” While qualitatively reasonable, “consistent” is not quantified; the caption also does not specify whether Eskilt’s observational posterior is plotted, or just the model posteriors.  
- **Required fix:**  
  - In Sec. 3.3 or the caption, state explicitly whether the **observed β_obs posterior** is included in Fig. 2, and quantify consistency at least roughly (e.g. all posteriors overlap within 1σ).  
  - If only model posteriors are plotted, rephrase “with the observed value” as a textual comparison, not as a feature of the figure.

P2-m6 (MINOR) – Abstract “effective photon coupling” phrasing potentially misleading  
- **Location:** Abstract  
- **Problem:**  
  - The abstract states: “…finding β = 0.242 ± 0.061° (3.9σ from zero) with an effective photon coupling f_photon × C₀ = 1.73 ± 0.44 (order-unity, no fine-tuning).” As noted above, f_photon × C₀ is neither standard notation in the field nor defined in the abstract, making this a slightly opaque headline quantity for readers.  
- **Required fix:**  
  - Either briefly define f_photon (in a parenthetical in the abstract) in terms of the standard coupling g_{aγ}, or soften the abstract to say that the implied combination of misalignment and coupling is O(1) in the ALP model, with the precise definition given in Sec. 3.2.

P2-n3 (NIT) – Minor arithmetic / wording consistency in σ statements  
- **Location:** Abstract, Sec. 3.2, Sec. 4, Sec. 8  
- **Problem:**  
  - A mixture of exact‐looking and approximate σ claims is used: “3.9σ from zero,” “3.6σ signal,” “9σ significance,” “∼ 9σ statistical significance,” without a clear pattern.  
- **Required fix:**  
  - Use “≈” consistently for all σ values derived from rounded means and uncertainties (e.g. “≈ 3.6σ,” “≈ 3.9σ,” “≈ 9σ”), and reserve plain “=” for cases where an exact analytic expression is intended. This will reduce the impression of unwarranted numerical precision.