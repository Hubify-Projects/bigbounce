# P2 auto-2026-06-09_0025pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 34172.7s

---

P2-E1 (ESSENTIAL) – Global (all pages, especially abstract, Sec. 1, 3, 7, 8)  
**Problem:** You repeatedly quote specific numerical results and references (e.g. Planck HFI birefringence “β = 0.35 ± 0.14° (2.5σ)”, “Eskilt et al. joint Planck + ACT analysis βobs = 0.342 ± 0.094° (3.6σ)”, ACT DR6 “β = 0.215 ± 0.074° (2.9σ)”, LiteBIRD “σ(β) ≈ 0.03°”, Fujita et al. (2021) Planck‑scale ALP produces β ∼ 0.3°, Namikawa et al. mass constraints, Minami-Komatsu method, etc.) but **no explicit, verifiable citations** are provided anywhere in the text or in a bibliography. The placeholder “[?]” appears repeatedly instead of actual references. There is **no reference list at all**.  
**Required fix:** Provide a complete, properly formatted reference list with full bibliographic information (authors, title, journal, year, volume, page, arXiv ID/DOI) for every “[?]” and every load‑bearing external result used in the paper. Replace each “[?]” in the text with the correct citation. The following specific references must be unambiguously identifiable and correctly cited (not exhaustive):  
- Planck HFI birefringence measurement (β ≈ 0.35 ± 0.14°).  
- ACT DR6 birefringence measurement and its exact β, σ result.  
- Eskilt et al. joint Planck+ACT analysis (βobs = 0.342 ± 0.094° and “3.6σ” claim).  
- Planck NPIPE birefringence result.  
- LiteBIRD birefringence forecast / σ(β) ≈ 0.03° source.  
- Minami–Komatsu self‑calibration method.  
- Fujita, Murai, Nakatsuka & Tsujikawa (2021) ALP birefringence paper.  
- Namikawa, Murai & Naokawa ALP mass‑constraint paper.  
- ECH gravity / Holst action / Barbero–Immirzi pseudoscalar / “14‑barrier catalog” companion paper.  
- Matter‑bounce non‑Gaussianity fNL = −35/8 paper.  
All quoted statistics (central values and errors) must be checked against the primary reference and corrected if necessary.

---

P2-E2 (ESSENTIAL) – Abstract & Sec. 3.1–3.2 (pp. 1–3)  
**Problem:** Numerical inconsistencies and incomplete description of the data combination:  
- Abstract says “Eskilt et al. joint Planck + ACT analysis” gives βobs = 0.342 ± 0.094° with “3.6σ”, but in Sec. 3.1 you also use Planck NPIPE (0.30 ± 0.11°) and ACT DR6 (0.215 ± 0.074°) and then in Sec. 3.2 construct a **different** combined constraint βcombined = 0.242 ± 0.061° (3.9σ). These are distinct estimators and are presented side‑by‑side without any explicit warning that they are not directly comparable.  
- You do not specify whether there is overlap or correlation between Planck NPIPE and the data used in the Eskilt joint analysis, nor between ACT DR6 and that analysis.  
**Required fix:**  
- Explicitly distinguish the **summary‑likelihood combination** (Planck NPIPE + ACT DR6) from the **Eskilt full‑spectrum joint fit**, in the abstract and main text, and state clearly wherever numbers are juxtaposed that the significances and β values are **not directly comparable** because they use different likelihoods and data processing.  
- State what data are included in each analysis and discuss possible correlations. If there is overlap, justify the assumption of independence or adjust the combination procedure.  
- Re‑compute and confirm that βcombined = 0.242, σ = 0.061, and significance 0.242/0.061 ≈ 3.97σ are correct; if you continue to quote “3.9σ” in the abstract, clarify that this refers to the summary‑likelihood combination and not to Eskilt et al.

---

P2-E3 (ESSENTIAL) – Eq. (2), Sec. 2.2 (p. 2)  
**Problem:** Possible dimensional and definitional confusion in the birefringence formula. You write  
\[
\beta = \frac{g_{a\gamma}}{2}\,\Delta\phi = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi f_a}\Delta\phi
\]  
with \(g_{a\gamma} = \alpha_{\rm EM} C_{a\gamma}/(2\pi f_a)\) “in the conventions of ?”. Without a proper citation, the reader cannot verify that your factors of 2 and π are consistent with the literature conventions you later compare to. The standard result in the cosmic‑birefringence literature is typically β = ½(Δφ/f_a)×(Cα/π) or variants.  
**Required fix:**  
- Provide the **explicit reference** and equation number where this convention is defined.  
- Check carefully that your numerical predictions (e.g., β ≈ 0.29° for C = 8, Δφ/f_a = 1.07) are consistent with that convention. If you are using a nonstandard normalization, state this clearly and propagate it consistently throughout the paper and in all comparisons to existing constraints on \(g_{a\gamma}\).  
- Show the dimensional analysis explicitly (in words or a short derivation) to verify that β is dimensionless and independent of the field normalization.

---

P2-E4 (ESSENTIAL) – Sec. 2.2, numerical example and quoted range (p. 2)  
**Problem:** The numbers quoted have not been derived or shown, and consistency with Eq. (2) cannot be checked:  
- You claim: “For Caγ = 8, θi = 1, m ≈ 2 H0: numerical integration gives Δϕ/fa ≈ 1.07, yielding β = (αEM × 8/4π) × 1.07 ≈ 0.29°.”  
- You then state: “The prediction spans β ≈ 0.17–0.43° across the natural parameter range m/H0 ∈ [1, 3], θi ∈ [0.5, 2], Caγ ∈ [4, 12]”.  
No table, figure, or intermediate numbers are shown, and there is no way to verify that the stated β range is actually obtained from Eq. (2) and your stated parameter ranges; moreover, the dependence on m/H0 is only implicitly encoded via a numerical integration.  
**Required fix:**  
- Provide either a small table or a figure showing Δϕ/fa and β as functions of m/H0 and θi for representative Caγ values, so the reader can verify the β range 0.17–0.43°.  
- Show one explicit numerical computation for the fiducial point (Caγ = 8, Δϕ/fa = 1.07, αEM ≈ 1/137) that leads to β in degrees, including the conversion from radians. Check that your 0.29° number is correct to within a percent.  
- Clarify whether the 0.17–0.43° range is a strict extremum over the parameter box or just “order‑of‑magnitude”; if approximate, state this explicitly.

---

P2-E5 (ESSENTIAL) – Sec. 3.2, Eq. (3)–(5) (p. 3)  
**Problem 1 (reproducibility):** The combined β result and the “effective photon coupling” are not fully reproducible from information in the text. You define the likelihood Eq. (3) but do not show the explicit values of βi, σi used or any covariance; you then assert  
\[
\beta_{\rm combined} = 0.242 \pm 0.061^\circ
\]  
and  
\[
f_{\rm photon} \times C_0 = 1.73 \pm 0.44
\]  
without defining what “fphoton” is, how it relates to \(g_{a\gamma}\), or how it is derived from βcombined.  
**Problem 2 (units):** “fphoton × C0” is dimensionless in your writing, but it is implicitly some dimensionless re‑scaling of 1/fa times constants; however, you never give the precise definition.  
**Required fix:**  
- Explicitly define “fphoton” in terms of fa, αEM, and any other constants, and show the formula that connects βcombined and fphoton × C0.  
- Provide a short derivation or intermediate step so that a reader can recompute fphoton × C0 = 1.73 from βcombined = 0.242°.  
- Confirm that the numeric 1.73 ± 0.44 follows from propagating the error on βcombined, and state whether any prior on C0 is used in this mapping.

---

P2-E6 (ESSENTIAL) – Sec. 3.3 & Fig. 1 (p. 3–4)  
**Problem:** The MCMC analysis is described only schematically and is **not reproducible** at the level PRD requires:  
- No likelihood function is written for the MCMC analysis; only βobs is referenced.  
- There is no explicit statement of whether the MCMC uses the full Eskilt EB likelihood, a Gaussian likelihood on βobs, or something else.  
- You quote specific posteriors: βALP = 0.336 ± 0.107°, βfree = 0.344 ± 0.096°, Caγ × θi = 3.4 ± 1.1, and sample numbers (2,160, 6,840, 720) with R̂ − 1 < 0.01, but no details of chain length, burn‑in, proposal distribution, or code (e.g., emcee/PolyChord/etc.) are given.  
- Fig. 1 is referenced as a triangle plot but is not shown in the text you provide; in any case, without axes labels, priors, and likelihood, the reader cannot verify the quoted posteriors.  
**Required fix:**  
- Fully specify the MCMC likelihood used: give the functional form and data vector; if a Gaussian likelihood on βobs is used, write it explicitly.  
- Provide more details of sampling: code used, number of chains, total steps, burn‑in fraction, and how R̂ was computed.  
- Ensure Fig. 1 includes clearly labeled axes with units and explicit prior ranges.  
- Clarify whether the quoted means and σ values (βALP, βfree, Caγ×θi) are posterior means with 68% credible intervals; verify they numerically agree with simple Gaussian propagation from βobs where appropriate.

---

P2-E7 (ESSENTIAL) – Sec. 3.4 (p. 3)  
**Problem:** The Bayes factor ln B = 5.17 is stated without sufficient methodological detail to verify it. You say it is computed via the Savage‑Dickey density ratio with a flat prior β ∈ [0°,1°] and give alternate values for other prior ranges. However:  
- You do not show the posterior density at β = 0 used in the Savage–Dickey ratio.  
- You do not state whether this posterior comes from Run 1 or Run 3 or a direct β‑only fit.  
- There is no cross‑check against the analytic Bayes factor for a Gaussian likelihood with a uniform prior, which would be trivial here.  
**Required fix:**  
- Explicitly state the analytic formula used for the Bayes factor in the Gaussian‑likelihood, uniform‑prior case, and show how plugging in βobs and σ gives ln B ≈ 5.17.  
- Identify which run’s posterior is used and demonstrate that your numerical Savage–Dickey result agrees with the analytic value to better than a few percent.  
- Add a sentence explaining that the evidence is computed in a 1‑parameter nested model and that correlations with other parameters are negligible (if this is your assumption).

---

P2-E8 (ESSENTIAL) – Sec. 4, Eq. (10) (p. 4)  
**Problem:** You compute the LiteBIRD significance as 0.27/0.03 = 9σ and then state: “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.” This is a simplistic Gaussian argument that ignores theoretical and systematic uncertainties in βpred as well as any forecast systematics in σ(β). It risks over‑stating the level of exclusion; PRD normally expects more nuance.  
**Required fix:**  
- Explicitly state the assumption: that βpred is treated as an exact value and that σ(β) is purely statistical.  
- Add at least a brief discussion of theoretical uncertainty in βpred (e.g. dependence on m/H0, θi, Caγ) and how that would reduce the effective σ of the model comparison.  
- Either soften the “excluded at 9σ” language to “of order 9σ in the Gaussian limit” or provide a proper likelihood‑ratio statistic that incorporates uncertainty in model parameters.

---

P2-E9 (ESSENTIAL) – Sec. 5, Eq. (11) and energy‑density discussion (pp. 4–5)  
**Problem 1 (inconsistency):** The text is self‑contradictory about the spectator regime and the value of θi used in the headline prediction:  
- Earlier, the abstract and Sec. 2–3 repeatedly emphasize **θi ~ O(1)** as “natural” and use θi = 1 in the example yielding β ≈ 0.27°.  
- In Sec. 5, you compute Ωϕ(z=0) ≈ (m^2/H0^2)(fa^2/MPl^2)(θi^2/6) and say that for fa ~ MPl, m ~ H0, θi ~ 1 you get Ωϕ ~ 0.17—*not* negligible. You then say the strict spectator regime requires θi ≈ 0.22 (a factor ∼25 tuning).  
- Despite this, you write: “We adopt option (a) (θi ∼ 0.22, with fa ∼ MPl retained for spectator‑EFT consistency) as the headline parameter point, in which case the β ∼ 0.27° prediction continues to hold by the cancellation above.” But your β examples earlier explicitly used θi = 1 and Δϕ/fa ≈ 1.07; if θi is reduced by 4–5×, β should change unless you retune m/H0 or C0. This is not demonstrated.  
**Problem 2 (quantitative check):** The “∼ 25× misalignment tuning” is vague and numerically off: going from θnat ≈ π/2 ≈ 1.57 to 0.22 is ≈ 7×, not 25×; going from θnat ≈ π ≈ 3.14 is ≈ 14×. You need to define what you mean by “natural prior midpoint”.  
**Required fix:**  
- Provide an explicit computation of β for the θi ≈ 0.22 spectator case, showing how m/H0 and Caγ are chosen to keep β ≈ 0.27°. If other parameters must be retuned, this affects your naturalness claim and must be discussed.  
- Correct the mis‑stated tuning factor: define clearly the “natural prior midpoint” for θi (e.g. π/2) and compute the actual tuning factor.  
- Clarify which parameter point is your **actual headline prediction** (θi ≈ 1 or θi ≈ 0.22) and ensure that this is consistent across the abstract, main text, and conclusion.  
- Quantify the fraction of prior volume (in θi) corresponding to the spectator regime and discuss whether calling this “cosmological‑constant‑class tuning” is justified.

---

P2-E10 (ESSENTIAL) – Sec. 6 & Sec. 7, bounce cosmology references (pp. 5–6)  
**Problem:** You refer to “the companion paper [?] for the full ECH framework and 14‑barrier catalog” and to “companion Paper I(a) [?]” in Sec. 5, and to a matter‑bounce fNL prediction [?] in Sec. 7. None of these are identified or citable. PRD does not accept references to vague “companion papers” without arXiv numbers or journal info, especially when they are load‑bearing for claims about tuning and ECH motivation.  
**Required fix:**  
- Provide full citations for “companion paper” and “Paper I(a)” and the fNL = −35/8 bounce paper, including arXiv IDs and current publication status.  
- If these works do not yet exist on arXiv, you must either:  
  - remove the references and any claims that rely exclusively on them, or  
  - deposit them on arXiv (with stable identifiers) and update this manuscript accordingly.  
- Clearly separate what is proven in this paper from what is deferred to companion works.

---

P2-E11 (ESSENTIAL) – Abstract & Sec. 7 (pp. 1, 5–6): Novelty claims  
**Problem:** You claim:  
- “Our contribution is not the model itself, but rather the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal, and the inference framework demonstrating internal consistency.”  
At the same time, you acknowledge Fujita et al. (2021) already “demonstrated that a Planck‑scale ALP naturally produces β ∼ 0.3°” and Namikawa et al. provided improved constraints. Without a detailed comparison, it is unclear that your parameter choice or inference framework is novel at a level warranting a PRD article rather than a short note.  
**Required fix:**  
- Provide a more detailed, quantitative comparison to Fujita et al. and Namikawa et al.: show where in parameter space they focused, what their assumed priors were, what β they predicted, and how your treatment is substantively different (e.g., inclusion of ACT DR6, different priors, different treatment of energy‑density constraints).  
- Either tone down the novelty claim (“we provide an updated synthesis and explicit forecast for LiteBIRD given the Eskilt et al. measurement”) or show, with explicit equations and plots, what genuinely new theoretical or statistical ingredient you add.

---

P2-M1 (MAJOR) – Global: missing reference list and “[?]” placeholders  
**Problem:** As noted in P2‑E1, the entire bibliography is missing and placeholders “[?]” are present. This is both an essential and a major presentation failure.  
**Required fix:** Supply a full, properly formatted bibliography and replace all “[?]” with correct citations.

---

P2-M2 (MAJOR) – Abstract vs. main text β values and σ’s (pp. 1–3)  
**Problem:** The abstract states:  
- “β ≈ 0.27°” as the theoretical prediction.  
- “3.6σ isotropic birefringence signal (βobs = 0.342 ± 0.094° from Eskilt et al.).”  
- Your summary‑likelihood combination later yields βcombined = 0.242 ± 0.061° (3.9σ).  
These numbers are not clearly tied to each other, leading to potential confusion about which β and σ are the headline observables.  
**Required fix:**  
- In the abstract, clearly indicate which observational number is used for the main inference (e.g. “We adopt the Eskilt et al. βobs = … as our primary data point” or “we independently combine Planck NPIPE and ACT DR6 to obtain βcombined = …”).  
- Consistently name the different estimators (βEskilt, βcombined, etc.) and use that notation in the main text.

---

P2-M3 (MAJOR) – Naturalness discussion (Sec. 5 & 7, pp. 4–6)  
**Problem:** The naturalness discussion is mostly qualitative and occasionally imprecise. Statements like “mθ ∼ H0 ultralight‑mass tuning is a cosmological‑constant‑class tuning shared with all ultralight‑ALP proposals” are broad and do not cite comparative work or quantify the tuning in a standardized way (e.g., in terms of prior volume or likelihood sensitivity).  
**Required fix:**  
- Provide a more quantitative measure of “tuning” for both m and θi (e.g., fraction of prior volume that yields Ωϕ < 0.01 and β within 1σ of observation).  
- Cite at least one or two other ALP birefringence works and show that they suffer a similar or worse tuning in your metric.  
- Tighten language to avoid impressionistic statements that are not supported by calculations.

---

P2-M4 (MAJOR) – LiteBIRD forecast (Sec. 4, p. 4)  
**Problem:** The LiteBIRD forecast is trivialized to a one‑line signal‑to‑noise ratio. You neither reference a full Fisher analysis nor do you consider degeneracies with calibration systematics or other cosmological parameters. For PRD, this section is underdeveloped relative to its rhetorical weight in the abstract and conclusion.  
**Required fix:**  
- Either (a) expand the forecast section with at least a simple Fisher‑analysis description (noise levels, sky fraction, frequency channels, treatment of systematics) and corresponding references, or (b) clearly frame the 9σ statement as a **back‑of‑the‑envelope S/N estimate** and lower its emphasis in the abstract and conclusion.  
- Ensure that the LiteBIRD σ(β) you quote is explicitly traceable to a published design or forecast paper (with citation).

---

P2-M5 (MAJOR) – Figures 1 & 2 (pp. 4–5)  
**Problem:** Only schematic descriptions are present; the actual content cannot be audited from the text. Potential issues:  
- Axes are not described in the text (units, linear/log, prior/posterior density).  
- It is not stated whether Figure 2 shows normalized posteriors or histograms, or if any smoothing is applied.  
- There is no check that the posteriors in Fig. 2 are consistent with the quoted summary statistics in Eqs. (6)–(7).  
**Required fix:**  
- Ensure that both figures include clear axis labels, units, and legends.  
- Explicitly state in the text what each panel shows (e.g., marginalized 1D posteriors with 68% and 95% credible intervals, 2D contours at 68% and 95%, etc.).  
- Confirm that the means and standard deviations read off from the figures match the quoted numbers in the main text.

---

P2-M6 (MAJOR) – Length vs. contribution  
**Problem:** The paper is 7 pages and yet the main theoretical content is a fairly minimal ALP model, a back‑of‑the‑envelope energy‑density estimate, a Gaussian combination of two β measurements, and a very simple LiteBIRD forecast. A large portion of the text is devoted to qualitative naturalness discussion and references to companion/bounce‑cosmology papers that do not directly affect the birefringence prediction. For the stated goal (Planck‑scale ALP birefringence prediction + LiteBIRD forecast), the paper is somewhat verbose.  
**Required fix:**  
- Streamline the narrative by focusing on: derivation of β, energy‑density constraints, data combination, and forecast.  
- Consider reducing the bounce‑cosmology and ECH‑framework discussion to a short paragraph unless you provide more quantitative results connecting them to birefringence.  
- A lean 5–6 pages should suffice for the material as currently developed.

---

P2-m1 (MINOR) – Typographical and style issues  
- “mθ ∼ H0” (abstract & Sec. 7) is confusing notation; presumably you mean “m ∼ H0” (the mass, not “mθ”).  
  - **Fix:** Replace “mθ ∼ H0” by “m ∼ H0” throughout.  
- Phrasing like “order‑unity, no fine‑tuning” in the abstract is somewhat colloquial.  
  - **Fix:** Rephrase in a more neutral, technical manner (e.g., “of order unity, consistent with natural expectations given the priors”).  

---

P2-m2 (MINOR) – Equation (1) range (p. 2)  
You quote  
\[
\Delta\phi/f_a \approx 0.2–1.1 \quad (m/H_0 \in [0.5,3],\ \theta_i=1)
\]  
without showing any computational detail. Although not an essential flaw, it would help readers to see how sensitive this is to m/H0 and the initial angle.  
**Required fix:** Add a sentence summarizing how the range was obtained (e.g., numerical integration in a ΛCDM background with specified initial condition) and perhaps a small inset figure showing Δφ/fa vs. m/H0.

---

P2-m3 (MINOR) – Clarify EB calibration method description (Sec. 7)  
The description of the Minami–Komatsu self‑calibration method is technically correct in spirit but may mislead non‑experts by not distinguishing between detector‑angle calibration and absolute rotation degeneracy.  
**Required fix:** Add one sentence explicitly stating that the method breaks the degeneracy between global detector angle and cosmic birefringence by exploiting TB/EB not expected from a parity‑conserving sky.

---

P2-N1 (NIT) – Internal cross‑references  
- “See Sec. 5” in the abstract and text are correct but could be more specific (e.g., “see Sec. 5 for the explicit energy‑density calculation and tuning discussion”).  
- “Through the rest of this paper, ‘spectator’ refers to…” is helpful but would benefit from a parenthetical reminder of the numerical θi value (0.22) for clarity.  

---

P2-N2 (NIT) – Minor repetition  
Some phrases are repeated verbatim, e.g., “does not participate in the bounce dynamics, does not generate perturbations, and does not require a contracting phase” could be shortened without loss of content.  
**Required fix:** Lightly edit for concision.

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript contains a potentially publishable idea—a simple Planck‑scale ALP explanation for the current birefringence hints with a clear upcoming test by LiteBIRD—but the present version is not yet at PRD standards. The absence of a proper bibliography, the use of “[?]” placeholders, incomplete and sometimes inconsistent quantification of the energy‑density and naturalness arguments, under‑specified MCMC and Bayes‑factor calculations, and over‑simplified LiteBIRD forecasting must be addressed. With a complete, carefully verified reference list, clearer separation of distinct β measurements and significances, a more rigorous treatment of the spectator constraint and tuning, and a better documented statistical methodology, the work could be considered again.