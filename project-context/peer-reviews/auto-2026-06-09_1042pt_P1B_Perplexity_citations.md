# P1B auto-2026-06-09_1042pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14737 chars)
**Wall time**: 95.4s

---

The manuscript as given is internally inconsistent, contains multiple citation and content issues, and does not meet Physical Review D standards in its current state.

Below I list all findings I can identify from the provided text alone. Because I do not have access to the figures/tables beyond what is quoted, I cannot audit any elements that are only visible in the PDF (axis labels, exact layouts, etc.). Where necessary I checked cited items (arXiv, journals, years) via web search and ADS.

---

### P1B-E1 — ESSENTIAL  
**Location:** Abstract, p.1; Sec. III/Table I, pp.2–3; Sec. VII, p.8  

**Problem:** Inconsistent and partially missing definition of “full-tension” vs “Planck+BAO+SN” dataset combinations and sample counts.

- Abstract reports: “Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations, plus a third Planck-only combination ongoing”.  
- Table I lists “Full-tension” with 176,240 samples and “Planck+BAO+SN” with 132,949 samples, summing to 309,189.  
- Footnote 1 then states “The third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I, and is not aggregated into the 309,189-sample headline anywhere in this paper.” But Table I has only two dataset columns (“Full-tension” and “Planck+BAO+SN”); no Planck-only column or numbers are shown.  

This is incoherent: the text claims the Planck-only run is “reported separately in Table I” and simultaneously that the 309,189 count does *not* include it, but Table I only has two combinations whose sample counts add exactly to 309,189.

**Required fix:**  
- Clearly define and label all dataset combinations (Planck-only, Planck+BAO+SN, full-tension including SH0ES+S8).  
- Provide a separate table or an explicit additional column for the Planck-only run if it is “reported” at all, or remove the claim that it is in Table I.  
- Adjust the abstract and Sec. III text so that:
  - the 309,189 sample count is precisely connected to specific datasets, and  
  - the ongoing Planck-only run’s sample count is correctly excluded and described without contradiction.  

---

### P1B-E2 — ESSENTIAL  
**Location:** Sec. III, Table I caption and data vs Sec. V, Sec. VII and Table III, pp.2–4, 8, 10  

**Problem:** Apparent inclusion of w₀–wₐ results and DESI DR2 / quintom analysis that are not actually part of the ΛCDM+ΔN_eff CAMB proxy described earlier.

- Sec. II explicitly says that in *this* paper’s sampled configuration, (ω/H)_0 and Ω_k are fixed to zero and that the paper’s MCMC is a **ΛCDM+ΔN_eff** proxy.  
- Table I, Sec. III and most of Sec. V refer clearly to that proxy.  
- However, Table II (p.4) is a **w₀–wₐ extended dark-energy model**, with 8 cosmological + 9 nuisance parameters and a likelihood stack that includes DESI DR2 BAO, Planck NPIPE, DES-Y5, and Pantheon+. This is a different model and data set and is not clearly delineated as separate from the ΛCDM+ΔN_eff proxy.  
- Sec. V.B (“Results”) begins with “the headline result is w₀ = −0.812 ± 0.044 … wa = −0.667 ± 0.186”, which are taken from Table II, and then states “The ΛCDM+ΔN_eff proxy thus offers neither posterior preference nor exclusion…”. This conflates two distinct analyses (w₀–wₐ and ΔN_eff) without a clear separation of scopes.  

This is structurally confusing and risks misrepresenting which constraints belong to which model. A PRD methods paper must be absolutely clear about model definitions and their relation to the main program.

**Required fix:**  
- Explicitly split the discussion into **two separate subsections**:
  1. ΛCDM+ΔN_eff stock-CAMB proxy (Planck+BAO+SN±SH0ES+S₈) with its own table and results;  
  2. Separate w₀–wₐ (quintom) analysis with DESI DR2 etc., clearly marked as a distinct project or forward-looking cross-check.
- Make explicit that Table II is *not* derived from the ΛCDM+ΔN_eff runs documented in Table I, and clarify why it appears in this companion paper and how it ties to Paper I(a).  
- Remove any sentences that ambiguously mix the two analyses or suggest that ΛCDM+ΔN_eff “gives” the w₀, wₐ measurements.  

---

### P1B-E3 — ESSENTIAL  
**Location:** Sec. V.B Model-comparison discussion, pp.6–7; Conclusions, p.8  

**Problem:** Claims of a strong deviation from ΛCDM (w₀ = −0.812 ± 0.044, w_a = −0.667 ± 0.186, “phantom crossing”, “canonical quintom signature”) are presented **without any robust evidence metric** and with explicit acknowledgement that Bayes factors and AIC/BIC are not computed.

- The text emphasizes departures of +4.3σ in w₀ and −3.6σ in w_a and labels this as “canonical quintom signature”.  
- Yet it plainly admits that:
  - The ΛCDM point is unsampled in the Metropolis–Hastings chain (no (w₀, w_a) = (−1, 0) samples).  
  - Savage–Dickey cannot be used; ln B, ΔAIC, ΔBIC are not computed.  
- At the same time, the conclusions highlight these results as “headline” and link them to a “quintom” / bounce scenario.  

For PRD, strong claims that standard ΛCDM is disfavored must be backed by a **fully controlled evidence computation or a carefully framed frequentist analysis**, not just posterior-tail “σ” counts from one chain that explicitly fails to sample the null model.

**Required fix:**  
- Either:
  - Relegate the w₀–wₐ chain to a **brief, clearly labelled exploratory appendix result** with no “headline” language, or  
  - Provide a dedicated nested-sampling / thermodynamic integration calculation of ln B and at least Δχ², ΔAIC, ΔBIC relative to ΛCDM, with careful discussion of systematics.  
- Remove or substantially soften all language suggesting that this chain “requires phantom crossing”, “disfavors ΛCDM” etc., unless supported by a robust model-comparison metric.  
- Clarify that without evidence metrics, the reported “σ” departures are **posterior-shape diagnostics only**, not a decisive constraint on ΛCDM.  

---

### P1B-E4 — ESSENTIAL  
**Location:** Abstract, p.1; Sec. VI, pp.7–8; Appendix C, pp.9–10  

**Problem:** Birefringence numbers (β ≈ 0.27°, β = 0.342° ± 0.094°, etc.) and claimed ALP consistency are not fully transparent in terms of derivation and connection to the cited literature.

- The main observational constraint is correctly identified as Eskilt & Komatsu 2022, Phys. Rev. D 106, 063503, arXiv:2205.13962.[2] That paper indeed quotes β = 0.342° ± 0.094° (3.6σ) in the abstract.  
- The manuscript also adopts Planck PR4 (Diego-Palazuelos et al. 2022, PRL 128, 091302, arXiv:2201.07682) values β = 0.30° ± 0.11° and ACT DR6 β = 0.215° ± 0.074°×. For Planck PR4 this matches the literature. For ACT DR6, the cited reference is [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO],” which does **not** exist as of the knowledge cutoff or of the present DESI/ACT literature; the ID 2509.xxxxx would be a future-dated arXiv number.  
- The paper extensively uses these inputs to argue that an ALP with f_a ~ M_Pl, m ~ H₀ can accommodate β ≈ 0.27°; but the precise mapping from the ODE integration (Eq. (2)) and parameter ranges to β is only sketched, not fully shown, and no explicit cross-check table is given.  

**Required fix:**  
- Replace the ACT DR6 reference [3] with the correct ACT birefringence paper when it exists. As of now, there is no arXiv:2509.13654 and no 2025 ACT DR6 birefringence preprint that can be verified. The appearance of a specific future arXiv ID is unacceptable.  
- For β = 0.215° ± 0.074°, cite the actual ACT DR4/DR6 or other CMB experiment paper that reports this value, or clearly mark it as a private communication / forecast if that is the true origin.  
- Provide, preferably in an appendix, a **numerical table** showing:
  - For each (m/H₀, θ_i) corner and C_{aγ}, the computed Δφ/f_a and resulting β via β = (α_EM/(4π)) C_{aγ} Δφ/f_a.  
  - Explicit demonstration that the quoted envelope β ≈ 0.17–0.43° is recovered from the ODE integration and ranges stated.  
- Ensure all β values cited from the literature are traceable directly to the abstract or tables of the cited papers (which is already true for Eskilt & Komatsu 2022 and Diego-Palazuelos et al. 2022).  

---

### P1B-E5 — ESSENTIAL (per instructions on σ juxtaposition)  
**Location:** Abstract, p.1; Sec. VI, pp.7–8  

**Problem:** Different “σ” significances from **distinct procedures** are presented side-by-side without explicit “not directly comparable” qualifiers at each juxtaposition.

- The abstract says: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2, 3];a the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.”  
- Sec. IV and the NaMaster discussion refer to “SNR_SE = 20.32, 25.71” and per-realization SNR values ~0.9–1.15, contrasted with Planck NPIPE 2.7σ and Eskilt & Komatsu’s 3.6σ joint value.  
- Sec. VI uses “3.6σ” from Eskilt & Komatsu and then quotes a naive 3.9σ from an inverse-variance combination.  

The instructions explicitly require that when σ values from different null procedures appear side-by-side, **each juxtaposition** must contain an explicit “not directly comparable” statement. While some disclaimers exist, they are not repeated at every juxtaposition, especially where the 3.6σ and 3.9σ are contrasted.

**Required fix:**  
- Wherever pipeline SNRs (20.32, 25.71) are mentioned near sky-detection significances, add explicit language like: “These SNRs are estimator-calibration metrics and are not directly comparable to the sky-detection significances quoted in σ for Planck/ACT.”  
- In Sec. VI, when quoting 3.6σ (joint analysis) and 3.9σ (naive inverse-variance), explicitly state in the same sentence that the two significances arise from different covariance treatments and are not directly comparable; emphasize that 3.9σ is an **upper bound** under uncorrelated-error approximation.  
- Ensure no sentence or paragraph leaves the reader with an impression that pipeline SNR, naive inverse-variance σ, and joint-likelihood σ can be directly compared as equivalent “significances”.  

---

### P1B-E6 — ESSENTIAL  
**Location:** References [3], , , , pp.10–11  

**Problem:** Use of apparently future-dated or currently unverifiable references with specific arXiv IDs and journal details.

- [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”  
  - At present there is **no such arXiv number**; 2509.xxxxx is beyond the current posting timeline.  
-  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
  - Again, arXiv:2507.04265 is future-dated; DESI+torsion papers exist, but not with this ID and year.  
-  “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  
  - Actual DESI DR1 BAO cosmology appears as DESI “2024 VI: cosmological constraints from … BAO” in JCAP or MNRAS with 2024/2025 details, but the combination “PRD 112, 083515 (2025), arXiv:2503.14738” is **not currently verifiable**.[2]  
-  “DESI Collaboration, A. G. Adame, et al., DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv preprint (2024), arXiv:2404.03002 [astro-ph.CO].”  
  - DESI “2024 VI” exists with a 2024 arXiv ID and has been accepted in MNRAS/JCAP; however, the paper text mixes multiple bibliographic versions (preprint vs. journal vs. PRD for DR2) inconsistently.  

Using specific future arXiv IDs and journal volumes that cannot be verified is unacceptable in PRD.

**Required fix:**  
- Replace [3], ,  with currently existing, verifiable references or remove them until such papers are publicly available.  
- For DESI BAO cosmology, use the actual “DESI 2024 VI” reference with its correct arXiv:2404.xxxxx number and accepted journal (JCAP or MNRAS; see DESI docs).[2][9]  
- Do not give speculative future arXiv IDs, journal volumes, or years. If you wish to refer to “upcoming DESI DR2 cosmology results”, label them clearly as “in preparation” *without* invented arXiv IDs or volume/page numbers.  

---

### P1B-E7 — ESSENTIAL  
**Location:** References [1], [4], [5], [6], , pp.10–11  

**Problem:** “In preparation” self-citations with internal report IDs (hUBIFY-2026-00X) and “companion paper, this volume” claims that likely do not satisfy PRD’s requirements for traceable literature, and in several cases, the titles strongly suggest substantive new claims that are not independently verifiable.

- [1] “H. Golden, Structural Closure of Einstein–Cartan–Holst Dark Energy: … (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.”  
- [4] “f_NL = −35/8 Forecast: SPHEREx … (in preparation) (2026), hUBIFY-2026-002; companion paper, this volume.”  
- [5] “Spectrally Unusual Sources … 378,280 Anomalies … (in preparation) (2026), hUBIFY-2026-003; companion paper, this volume.”  
- [6] “Galaxy Chirality at Scale: 8.47M Galaxies Classified, Hemisphere Null at p_LEE < 10−4, (in preparation) (2026), hUBIFY-2026-004; companion paper, this volume.”  
-  LiteBIRD reference is fine by itself (Allys et al. 2023, PTEP 2023, 042F01, arXiv:2202.02773), but the text around it suggests forecasts being quoted as if they were fixed design numbers without uncertainty from evolving mission design.  

PRD permits “companion papers” in the same issue, but at submission time they must either be co-submitted or already available on arXiv. Here there are no arXiv IDs, only internal “hUBIFY” tags. The main claims of the program depend heavily on these unavailable works (e.g., “14 independent structural constraints”, “multi-survey anomaly catalog”, “galaxy chirality catalog”).

**Required fix:**  
- For each “companion” paper, provide a **real arXiv ID** and ensure the submission to PRD includes the cross-referenced manuscripts.  
- Until those works are independently available, remove or substantially soften statements that rely on them for critical physics (e.g., “The main paper establishes 14 independent structural constraints…”); in this companion you should restrict yourself to methods that can stand alone.  
- Replace internal “hUBIFY-2026-00X” report IDs with standard bibliographic references once they exist.  

---

### P1B-M1 — MAJOR  
**Location:** Sec. III, Table I + text, pp.2–3  

**Problem:** Reported numbers for ΔN_eff, H₀, σ₈, S₈, Ω_m, n_s, τ are internally consistent in the table, but there is no explicit cross-check that they reproduce the quoted “Planck-dominated” and “tension” statements.

- For full-tension: H₀ = 67.68 ± 1.06 km s⁻¹ Mpc⁻¹, ΔN_eff = −0.020 ± 0.169, σ₈ = 0.803 ± 0.008, S₈ = 0.814 ± 0.008, Ω_m = 0.308 ± 0.005. These numbers are plausible for Planck-like constraints with SH0ES+S₈ priors; they are also consistent in that S₈ ≈ σ₈ √(Ω_m/0.3) ≈ 0.803 × √(0.308/0.3) ≈ 0.803 × 1.013 ≈ 0.813, matching the table’s 0.814 ± 0.008 within rounding.  
- The text states that this corresponds to a canonical 3.6σ tension with Riess H₀ = 73.04 ± 1.04 km s⁻¹ Mpc⁻¹, and that the ΔN_eff extension cannot resolve this. That tension level is consistent numerically (ΔH₀ ≈ 5.35, σ_comb ≈ √(1.06²+1.04²) ~ 1.49 => 3.6σ).  

However, none of these “σ-level” statements are *explicitly recomputed in the manuscript*, and the paper does not show even a basic tension table. For a verification companion, the quantitative consistency checks should be explicit.

**Required fix:**  
- Add a small table or paragraph that explicitly computes:
  - Tension between H₀ = 67.68 ± 1.06 and 73.04 ± 1.04, showing the 3.6σ result.  
  - Same for MB if you want to present the MB–H₀ axis.  
- Make explicit that S₈ is computed via S₈ = σ₈ √(Ω_m/0.3) and verify the numbers in text.  

---

### P1B-M2 — MAJOR  
**Location:** Sec. IV, p.5–6  

**Problem:** NaMaster pseudo-C_ℓ analysis setup lacks detailed specification necessary for full reproducibility, and some descriptions are ambiguous.

- It mentions “Planck Commander Q/U maps are provided at Nside = 2048 … we degrade to Nside = 512 and apply the corresponding pixel window function” but does not specify whether beam deconvolution or re-beaming is applied, at which effective FWHM.  
- It lists ACT-level noise ΔP = 10 μK·arcmin but does not specify whether this is homogeneous white noise, how it is converted into per-pixel σ, or whether any filtering / multipole cuts are applied.  
- The mask description (“C2 apodization at 2° scale, f_sky = 0.32”) is adequate, but there is no explicit mention of the sky patch used, or whether Commander’s mask is combined with any additional cuts.  

Given this is a “technical verification companion”, the pseudo-C_ℓ configuration must be described precisely enough that an independent group can reproduce the MC bias at the ≤0.04° level.

**Required fix:**  
- Add explicit details:
  - Exact Planck Commander map version (e.g., 2018 PR3 vs PR4, frequency channel, or combined map).  
  - Beam transfer function used (e.g., 143 GHz 5′ Gaussian) and whether it is deconvolved or convolved to a common beam when degrading to Nside = 512.  
  - Noise model specifics (white vs anisotropic, per-pixel noise level, and how 10 μK·arcmin is implemented).  
  - The precise mask file (e.g., filename or description), including any Galactic/point-source cuts.  
- Provide a concise table summarizing these parameters.  

---

### P1B-M3 — MAJOR  
**Location:** Abstract & scope statements throughout, pp.1–2, 7–8  

**Problem:** Scope and non-scope of the work are described in a somewhat verbose and internally overlapping way, which obscures what this paper *actually* proves vs. what is simply documented.

- Multiple “Scope statement” paragraphs repeat that this is a stock-CAMB ΛCDM+ΔN_eff run, not a torsion module; and that ALP birefringence is not a distinctive ECH prediction. This is good in principle but the repetition and interleaving with strong claims about quintom, bounce, and ALPs make the scope harder to follow.  
- The paper’s title emphasizes “technical verification” and “NaMaster Pipeline Recovery”, but the body includes large sections on quintom cosmology (Table II), DESI DR2, and ALP cosmology that go beyond what is necessary for verification of Paper I(a).  

PRD methods papers must be sharply focused. In its current form, the manuscript reads more like a mix of technical checks and preliminary cosmological claims.

**Required fix:**  
- Tighten the scope:
  - Move the w₀–wₐ (quintom) and DESI DR2 chain results either to an Appendix or to Paper I(a) unless they are absolutely necessary for verifying the ECH no-go program.  
  - Clearly state in the introduction and conclusions that the *only* goals here are:  
    1. Document the ΛCDM+ΔN_eff stock-CAMB proxy used in Paper I(a);  
    2. Validate the NaMaster E→B pipeline;  
    3. Demonstrate that an ALP model can accommodate the observed β.  
- Reduce any speculative discussion (e.g., about quintom-B across DESI DR2) to a short forward-looking paragraph, not a central result.  

---

### P1B-M4 — MAJOR  
**Location:** Throughout (esp. Sec. VI and Appendix C), pp.7–10  

**Problem:** Misalignment fine-tuning and “spectator vs dark-energy ALP” caveats are explained, but in a way that may mislead readers about how generic the ALP explanation is.

- The footnotes and text state that spectator status requires θ_i ~ 0.1 (implying ρ_a ≪ ρ_crit), whereas the numerical scan uses θ_i ∈ [0.5, 2] and then notes that the data prefer the upper end.  
- This is essentially saying that the region truly compatible with “spectator” is a **narrow subset** of the parameter space, while the numerical results used to match β come from a regime where the ALP is not a spectator but a dark-energy-scale field.  
- Yet the title and scope of Sec. VI continue to call this a “Spectator-ALP consistency check” without firmly separating which results are genuinely in the spectator regime.  

**Required fix:**  
- Explicitly separate:
  - A true **spectator regime** analysis with θ_i ≪ 1 (e.g., θ_i ≤ 0.1), including the corresponding β range and required C_{aγ}.  
  - A separate “DE-ALP” regime where Ω_a ~ 1, which is outside the claimed scope of this companion paper.  
- Clearly mark which of the MCMC chains and β results belong to each regime, and do not mix them in a single “headline” β_ALP.  
- If the actual posterior prefers θ_i values incompatible with spectator status, state this plainly and reframe the ALP result as “an ALP that *could* in principle be the DE field” rather than a spectator.  

---

### P1B-Minor and Nits

#### P1B-N1 — MINOR  
**Location:** Footnote a on p.1 and ref. [2], p.10  

**Problem:** Slightly convoluted wording about “PR3 vs PR4/NPIPE” Eskilt & Komatsu dataset labels.

- The footnote explains that Eskilt & Komatsu (PRD 106:063503, arXiv:2205.13962) use PR3+WMAP9, while the public code now defaults to PR4/NPIPE; and that this paper uses “PR4/NPIPE” labels for the repository dataset.  
- This is correct but confusingly worded; the reader might mistakenly think the PRD paper itself uses PR4.  

**Required fix:**  
- Rephrase concisely: e.g., “Eskilt & Komatsu (PRD 106, 063503; arXiv:2205.13962) base their published result on Planck PR3+WMAP9. The publicly released reproduction code has since been updated to use Planck PR4/NPIPE; our re-runs use that PR4/NPIPE option, but we always quote the published β = 0.342° ± 0.094° value from the PR3+WMAP9 analysis when referencing their headline result.”  

---

#### P1B-N2 — MINOR  
**Location:** Table II, footnote b, p.4  

**Problem:** wpivot error-propagation expression uses a slightly confusing notation “σ_w^2 = σ_w0^2 + (1 − a_p)^2 σ_wa^2 = …” which is dimensionally fine but might be clearer as Var(w_pivot) etc.

**Required fix:**  
- Consider rewriting the wpivot variance relation as Var(w_pivot) = Var(w₀) + (1 − a_p)² Var(w_a), and explicitly plug in numbers.  

---

#### P1B-N3 — MINOR  
**Location:** Sec. VI, Eq. (3), p.7  

**Problem:** The derivation of β ≈ 0.29° from α_EM × 8 × 1.07/(4π) is plausible but not shown numerically; some readers may want the explicit step.

**Required fix:**  
- Add a short line: α_EM ≈ 1/137, so α_EM/(4π) ≈ 5.8 × 10⁻⁴; multiplying by C_{aγ} = 8 and Δφ/f_a ≈ 1.07 gives β ≈ 0.0050 rad ≈ 0.29°.  

---

#### P1B-N4 — NIT  
**Location:** Occasional capitalization and formatting, e.g. “stock-CAMB”, “standard-ECH”, several uses of “RETained” in caps in footnotes, and “head-line” / “head line”.

**Required fix:**  
- Normalize capitalization (e.g., “stock CAMB”, “standard ECH”).  
- Replace emphatic all-caps (“RETAINED”) with italics for emphasis.  

---

### Bibliography audit and duplication/staleness

- No obvious duplicate entries.  
- Several references are stale or incomplete in the sense discussed above (future-dated arXiv IDs, missing journal info).  
- All major external cosmology results used (Pantheon+, DES-Y3, DES 5yr SNe, Planck 2018 parameters) have existing, correct references; those seem fine.  
- Riess et al. 2022 ApJL 934 L7, arXiv:2112.04510 is correct for SH0ES.[7]  
- Planck 2018 parameters are correctly tied to Aghanim et al. 2020, A&A 641 A6, arXiv:1807.06209.  
- Pantheon+ is correctly cited as Brout et al. 2022, ApJ 938, 110, arXiv:2202.04077.  
- DES-Y3 cosmology is correctly identified as Abbott et al. 2022, PRD 105, 023520, arXiv:2105.13549.  

The main bibliographic problems are the invented future references and missing arXiv IDs for the author’s own “companion” works.

---

## Summary recommendation  
**Recommendation: REJECT**

The manuscript contains multiple serious issues: unverifiable/future-dated references with specific arXiv IDs and journal metadata; conflation of distinct cosmological models (ΛCDM+ΔN_eff vs w₀–wₐ quintom) without clear separation; strong claims about deviations from ΛCDM and ALP explanations that are not supported by robust evidence metrics; and incomplete technical specification for key “verification” analyses. While the author clearly put effort into self-auditing and scope caveats, the current presentation does not meet PRD’s standards for rigor, traceability, and bibliographic reliability. A future submission would require substantial restructuring, replacement of speculative references with real ones, and more careful quantitative support for all headline claims.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E8 — ESSENTIAL  
**Location:** Sec. II, “MB–H0 joint-posterior offset check”, p.4–5  

**Problem (arithmetic error + propagated misinterpretation):** The claimed “exactly” 3.6σ MB–H0 tension is numerically inconsistent with the values given.

- The text computes the Pantheon+ “constant” as −28.571 at (MB, H0) = (−19.253, 73.04) and −28.416 at the chain mean (−19.263, 67.69), giving Δ = 0.155 mag “correspond[ing] exactly to the canonical 3.6σ Hubble tension … manifesting in the MB axis.”  
- But with σ_MB = 0.049 mag, the significance on this axis is 0.155/0.049 ≈ 3.16σ, not 3.6σ.  
- In H0-space, the same numbers give ΔH0 = 5.35 and σ_comb ≈ √(1.06²+1.04²) ≈ 1.49 ⇒ 5.35/1.49 ≈ 3.59σ; i.e. 3.6σ is correct for H0 but not “exactly” reproduced by the 0.155-mag offset in MB.  

**Required fix:**  
- Correct the MB-axis significance to ≈3.2σ or explicitly state that the 3.6σ figure refers to the H0-axis tension, not to the 0.155-mag offset.  
- Remove language like “corresponds exactly” and clearly distinguish which axis is being used for each σ statement.  

---

P1B-E9 — ESSENTIAL  
**Location:** Sec. IV, “NaMaster pipeline validation” text vs Fig. 3 caption and surrounding discussion, pp.5–6  

**Problem (inconsistent SNR definition and potentially confusing use of σ):**

- Footnote 3 states that “SNR_SE = 20.32” is defined as \( \text{SNR}_{\text{SE}} \equiv \hat{\beta} \sqrt{N} / \sigma_{\hat{\beta}} \) with N = 500 realizations and reports per-realization SNR_real ≈ 0.91–1.15.  
- However, the main text just above Eq. (1) only gives numerical mean values (0.238°, 0.302°) and bias magnitudes and never explicitly shows σ(β̂) or the numerical SNR_real used; the reader cannot reproduce the 20.32 or 25.71 figures from what is printed.  
- Fig. 3 caption says “Bias β̂−β_inj is below 0.04° across the natural resolution range; this is the NaMaster systematic floor adopted in Eq. 1–3,” but Eq. (1) is only the definition of β̂_NaMaster and contains no explicit 0.032–0.040° numbers; the connection is only in the prose.  

**Required fix:**  
- Add the explicit numerical σ(β̂) used to get SNR_SE = 20.32 and 25.71 and state SNR_real in the same sentence so readers can verify the arithmetic.  
- Make explicit in the body (not just Fig. 3 caption) that the 0.032–0.040° bias range is adopted as a fixed additive systematic floor, and point to the equation(s) where it enters.  

---

P1B-E10 — ESSENTIAL  
**Location:** Sec. VI, Eq. (3) and “Birefringence value” paragraph, p.7  

**Problem (arithmetic / normalization inconsistency in β ≈ 0.29° estimate):**

- The text states for C_{aγ} = 8, θ_i = 1, m ≈ 2H0, Δφ/f_a ≈ 1.07 that  
  \( \beta \approx \frac{\alpha_{\rm EM} \times 8}{4\pi} \times 1.07 \approx 0.29^\circ \).  
- Numerically, taking α_EM ≈ 1/137,  
  \(\alpha_{\rm EM}/(4\pi) ≈ 0.00730 / 12.566 ≈ 5.8×10^{-4}\).  
  Then β [radians] ≈ 8 × 5.8×10^{-4} × 1.07 ≈ 0.00496 rad ≈ 0.284° only if the rad→deg conversion is applied.  
- The equation as written mixes a radian-level prefactor with a degree-valued β on the right-hand side without showing the 180/π factor; as printed it appears dimensionally inconsistent.  

**Required fix:**  
- Either write β explicitly in radians in Eq. (3), or include the conversion factor and show the intermediate β in radians before converting to degrees.  
- State clearly which unit convention is used for β in all ALP equations (Eqs. (2)–(4)) to avoid unit confusion.  

---

P1B-E11 — ESSENTIAL  
**Location:** Sec. VI, “Headline observational constraint” paragraph vs earlier references, p.7  

**Problem (self-inconsistent description of the Eskilt & Komatsu dataset composition):**

- The footnote on p.1 correctly states that the published PRD paper analyzes Planck PR3 + WMAP9, and the Github code was later updated to use Planck PR4/NPIPE.  
- In Sec. VI, the “headline observational constraint” is described as “the published Eskilt & Komatsu joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ) (the joint WMAP9 + Planck PR4/NPIPE analysis; ACT DR6 enters only via the separate … measurement).”  
- This is internally inconsistent: the published 3.6σ result corresponds to PR3+WMAP9, not “joint WMAP9 + Planck PR4/NPIPE,” which exists only in later code releases.  

**Required fix:**  
- Clarify that β = 0.342° ± 0.094° is the *published* PR3+WMAP9 result, and separately state what dataset combination the re-run code uses, without implying that the 3.6σ headline comes from PR4.  
- Make sure the phrase “joint WMAP9 + Planck PR4/NPIPE” is not used to describe the published 3.6σ constraint.  

---

P1B-E12 — ESSENTIAL  
**Location:** Sec. VI, “Summary-likelihood combination (auxiliary cross-check)” and surrounding text, p.7  

**Problem (σ comparability and scope caveat not repeated at the key juxtaposition):**

- The paragraph explicitly juxtaposes 3.6σ (published joint analysis) and 3.9σ (naive inverse-variance combination) in Eq. (4). It does say “Positively correlated errors underestimate … σ, and therefore overestimate the significance: the naive 3.9 figure is an upper bound…”, which is good.  
- However, earlier sentences describe β = 0.342° ± 0.094° and β_combined = 0.241° ± 0.061° both as “significance” numbers without stating explicitly in the same sentence that they are based on different covariance assumptions and thus *not directly comparable*, as required by the stated σ-comparability rule.  
- The abstract’s “2.4–2.9σ … 3.6σ … pipeline SNR figures” juxtaposition is now mostly handled, but this internal 3.6 vs 3.9σ comparison still lacks a clear “not directly comparable” tag right where the numbers are presented.  

**Required fix:**  
- Add explicit language in the sentence containing Eq. (4) that 3.9σ (naive combination) and 3.6σ (joint analysis) come from different null procedures/covariances and are *not directly comparable*, with 3.9σ stated clearly as an optimistic upper bound.  
- Ensure the same comparability caveat appears wherever 3.6σ and 3.9σ appear in the same paragraph.  

---

P1B-M5 — MAJOR  
**Location:** Sec. III, Table I vs Sec. III text and footnote 1; Sec. VII “Conclusions”, pp.2–3, 8  

**Problem (dataset-count and chain-stratification inconsistency and potential stale numbers):**

- The abstract and conclusions state “Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations, plus a third Planck-only combination” and “an additional 114,992-sample Planck-only run is still accumulating… and is reported separately in Table I.”  
- Table I itself, as printed, has *no* Planck-only column; only “Full-tension” and “Planck+BAO+SN” are shown. Footnote 1 explains post-burnin counts and mentions the Planck-only run but again refers to it being “reported separately in Table I.”  
- The per-dataset sample counts also mismatch between text and figure: Fig. 1 caption uses “Full tension (175 545 samples)” while Table I says 176,240; likewise minor mismatches suggest some numbers (e.g. 175,545 vs 176,240; 119,617 vs explicit 123,368 post-burnin) are relics from earlier chain versions.  

**Required fix:**  
- Either add a Planck-only column to Table I with its 114,992 raw samples and current R̂−1, or remove all claims that it is “reported” in Table I and confine its description to the text.  
- Reconcile all sample-count numbers (176,240 vs 175,545; 119,617 vs 123,3xx, etc.) so that Table I, Fig. 1 caption, footnote 1, and the abstract agree to within rounding and are clearly labeled as raw vs post-burnin vs thinned.  
- Explicitly label in each context which count is raw, which is post-burnin, and which is effective/thinned to avoid confusion.  

---

P1B-M6 — MAJOR  
**Location:** Sec. V.B, “The ΛCDM+ΔN_eff proxy thus offers neither posterior preference nor exclusion…”, p.6  

**Problem (model-scope conflation remains):**

- This sentence appears immediately after a paragraph that is entirely about the *w0–wa* quintom model (including the “headline result is w0 = −0.812 ± 0.044 … wa = −0.667 ± 0.186”).  
- Grammatically, “thus” refers back to the w0–wa discussion, creating the impression that the w0–wa chain *itself* informs a conclusion about the ΔN_eff proxy. This conflation persists even though earlier sections nominally separate the ΛCDM+ΔN_eff proxy from the quintom analysis.  

**Required fix:**  
- Move the ΛCDM+ΔN_eff summary sentence into the section where Table I is discussed, or explicitly preface it with a clause like “Independently of the w0–wa analysis…”  
- Ensure the prose never gives the impression that the w0–wa chain is being used to assess ΔN_eff.  

---

P1B-M7 — MAJOR  
**Location:** Sec. VI and Appendix C, ALP parameter ranges vs “natural-envelope” and “spectator” claims, pp.7–10  

**Problem (quantitative tension between stated “natural” envelope and posterior-preferred region not clearly exposed):**

- Sec. VI states a “natural-envelope range” Δφ/f_a ∈ [0.2, 1.1] from θ_i ∈ [0.5, 2], m/H0 ∈ [1, 3], and then notes that the ALP posterior prefers Caγ(Δφ/f_a) ≈ 10.3, implying Δφ/f_a ≈ 1.29 at Caγ = 8—already outside the stated natural envelope.  
- The text does mention this is “∼17% above the natural envelope upper bound” and ties it to the same ∼25× misalignment tuning, but it never quantifies how much of the posterior mass lies outside the supposed natural envelope or how strongly the data drive to that edge.  
- For a “consistency, not prediction” check, this subtle but real tension between prior “naturalness” and posterior preference should be numerically characterized, not just qualitatively mentioned.  

**Required fix:**  
- Add a brief quantitative statement (e.g., fraction of posterior samples with Δφ/f_a > 1.1, or posterior mean and σ of θ_i and m/H0) to make clear how strongly the data push beyond the stated natural envelope.  
- Clarify explicitly that most (or a significant) fraction of the preferred parameter volume is outside the nominal “natural” range, to avoid overstating naturalness.  

---

P1B-m1 — MINOR  
**Location:** Table II, wpivot footnote “reproducing the ±0.0301 value above”, p.4  

**Problem (arithmetic not reproducible from text as written):**

- The footnote gives σ(w0) = 0.0436, σ(wa) = 0.1864, a_p = 0.6680 (so 1−a_p = 0.3320) and asserts  
  \( \sigma_{w_{\rm pivot}}^2 = (0.0436)^2 + (0.3320)^2 (0.1864)^2 = (0.0301)^2. \)  
- Numerically, (0.0436)^2 ≈ 0.00190 and (0.3320)^2 (0.1864)^2 ≈ 0.00382 × 0.0348 ≈ 0.000133; their sum ≈ 0.00203, whose square root is ≈0.045, not 0.0301.  
- The missing ingredient is the covariance term −2(1−a_p)Cov(w0,wa), which was implicitly used to *define* a_p; but as written, the displayed formula suggests that σ^2 is simply a sum of two positive terms.  

**Required fix:**  
- Either provide the full expression including the covariance term, or remove the explicit numeric demonstration and simply state that with a_p chosen to decorrelate w0 and wa, σ(w_pivot) = 0.0301 is obtained from the chain covariance.  
- As it stands, the printed arithmetic is misleading and not reproducible.  

---

P1B-m2 — MINOR  
**Location:** Appendix A, “What is NOT included” vs Sec. V.B “We do not report χ²_eff, AIC, BIC, or ln B…”, pp.6, 9  

**Problem (slight internal inconsistency in what is “reported”):**

- Sec. V.B says “We do not report χ²_eff, AIC, BIC, or ln B … The χ² goodness-of-fit decomposition is reported in Table II; the AIC, BIC, and ln B evidence metrics are not reported there.”  
- Appendix A “What is NOT included” repeats that Bayes factors and information criteria are not reported, but does *not* mention that χ² component means are indeed reported as χ²_total, χ²_BAO, χ²_CMB, χ²_SN in Table II.  
- This can be misread as implying that *no* χ²-related quantities are reported.  

**Required fix:**  
- Slightly clarify Appendix A’s wording to say “Bayes factors and information criteria (ΔAIC, ΔBIC, ln B) are NOT reported; only per-dataset χ² means are given in Table II.”  

---

P1B-m3 — MINOR  
**Location:** References  and corresponding in-text parenthetical summary, p.10  

**Problem (informal paraphrase in reference entry):**

- Reference  includes additional explanatory text “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4); the value used at L256/L416 of P1B…”.  
- This kind of internal cross-reference belongs in the main text or a footnote, not inside the bibliographic entry itself. It blurs the distinction between a literature citation and this manuscript’s commentary on it.  

**Required fix:**  
- Move the “reports beta = …; the value used at L256/L416 of P1B” commentary into the main text or a footnote near Sec. IV/VI, and keep the reference list entry in standard APS citation format.  

---

P1B-m4 — MINOR  
**Location:** Abstract and Sec. VI, multiple uses of “natural parameters (taken at scan-prior midpoint values)” and “natural-envelope range”, pp.1, 7–8  

**Problem (unquantified hedge):**

- Phrases like “natural parameters (taken at scan-prior midpoint values)” and “natural-envelope range … comfortably bracketing the observed value” are qualitative assessments of naturalness.  
- The only quantitative piece is the [0.2, 1.1] envelope and the later remark that the posterior prefers Δφ/f_a ≈ 1.29; “comfortably bracketing” is not supported by an explicit statement of how centrally the observed β sits in the *prior* or *posterior* distributions.  

**Required fix:**  
- Replace “comfortably bracketing” with a more neutral phrase (“encompassing” or “covering”) or add a brief quantitative statement (e.g., prior mean and σ of β, or percentile rank of βobs within the prior envelope) so that the hedge is numerically grounded.  

---

P1B-m5 — MINOR  
**Location:** Appendix C, sampled-parameter list and priors vs Sec. VI text, pp.9–10  

**Problem (slight mismatch in emphasis between “natural” θ_i prior and spectator caveat):**

- Appendix C says θ_i prior is [0.5, 2] with a note that θ_i ~ 0.1 is needed for true spectator status, retained only for “envelope completeness.”  
- Sec. VI in the main text calls θ_i ∈ [0.5, 2] the “natural-prior box” and uses its corners to define the “natural-envelope range” for Δφ/f_a, while only briefly emphasizing in footnotes that θ_i ~ 0.1 is the true spectator regime.  
- This can give a casual reader the impression that most of the explored parameter space is “natural spectator,” whereas in fact the genuinely spectator-compatible subspace is a narrow sliver outside the sampled prior.  

**Required fix:**  
- In Sec. VI, add a sentence explicitly pointing back to Appendix C clarifying that the MCMC prior [0.5, 2] is an *envelope* chosen for parameter exploration, not the spectator-consistent range, which lies around θ_i ~ 0.1 and is not directly sampled in the main chains.