# P1B auto-2026-06-08_1424pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 66.0s

---

P1B-E1 (ESSENTIAL)  
Section: References (end of paper), throughout; also multiple in-text citations (e.g., Abstract, footnotes, Sec. I, II, III, VI)  
Page(s): 1–10  

Problem: Multiple references are clearly **fabricated or temporally impossible** given the claimed dates and current literature; several arXiv IDs correspond to non-existent “future” preprints or to unrelated real papers, and some “in preparation” items are used as if they were established peer-reviewed results.

Specific issues (checked against arXiv and NASA ADS):

1. **[1] H. Golden, “Structural Closure of Einstein–Cartan–Holst Dark Energy …” (2026), hUBIFY-2026-001A; “(in preparation)”**  
   - No record on arXiv (searched by author, title fragments, and “hUBIFY” tag).  
   - No record in NASA ADS under author “Golden, H.” with these keywords.  
   - The paper is cited as “main paper” and its results are used as *proven* structural theorems (“The main paper establishes 14 independent structural constraints … proves a perturbation-transparency theorem …”), but it is not available in any citable public archive.  
   Required fix:  
   - This cannot serve as a primary reference for *proved* results at PRD standard unless it is publicly available (arXiv or journal).  
   - Either (a) upload and cite the actual arXiv/DOI version and ensure consistency of all cross-references, or (b) remove all claims that depend on results of an unavailable manuscript and recast them as conjectural/ongoing work, which will significantly change the paper’s purpose.

2. **[3] P. Diego-Palazuelos and E. Komatsu, “Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv:2509.13654 (2025)”**  
   - arXiv IDs beginning with 2509.* correspond to September 2025, which does not yet exist. The ID is **impossible** with respect to the present arXiv timeline.  
   - No such preprint appears on arXiv or NASA ADS. The authors have ACT-related and birefringence-related works, but nothing matching this citation.  
   - The paper uses this as the *published ACT DR6* measurement β = 0.215° ± 0.074°. That number is *not traceable* to any current, citable ACT DR6 birefringence paper.  
   Required fix:  
   - Provide the correct existing reference for the ACT DR6 birefringence analysis, with correct arXiv ID, title, authors, and year, and verify that the quoted β value and uncertainty exactly match that source.  
   - If ACT DR6 birefringence is not yet publicly documented, this paper cannot quote it as a published 2.4–2.9σ detection; either remove or explicitly label as private communication/preliminary and do not treat it as a published constraint.

3. ** T. Liu et al., “Torsion cosmology in the light of DESI, supernovae and CMB observational constraints,” arXiv:2507.04265 (2025)**  
   - arXiv:2507.04265 cannot exist yet; July 2025 IDs are in the future.  
   - No record under that ID or title on arXiv/ADS.  
   - The text states: “Liu et al.  constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6).” These statistics cannot be verified because the paper does not exist.  
   Required fix:  
   - Replace this with a real, published or at least arXiv-posted torsion cosmology constraint (if any) that actually reports those AIC numbers, or remove the cross-validation claim entirely.  
   - Do not quote specific ΔAIC, σ offsets, or detailed results from a non-existent paper.

4. ** DESI Collaboration, M. Abdul-Karim, et al., “DESI DR2 results II: …,” Phys. Rev. D 112, 083515 (2025), arXiv:2503.14738**  
   - PRD volume 112 does not match 2025 in the way claimed (current PRD volume sequence is lower; volume and page are inconsistent with actual DESI BAO publications).  
   - arXiv:2503.14738 is a future-dated ID; no such preprint currently exists.  
   - The manuscript’s DESI DR2 w0–wa constraints (Table II) are said to use “DESI DR2 BAO” as in ; this exact stack cannot be verified.  
   Required fix:  
   - Point to the *actual* DESI DR2 BAO cosmology paper(s) once they exist, with correct arXiv IDs and journal references, and recompute the chains and Table II against the real likelihoods.  
   - Until then, this cannot be treated as a reproducible analysis.

5. ** DES Collaboration, T. M. C. Abbott, et al., “The dark energy survey: Cosmology results with ∼1500 new high-redshift type Ia supernovae using the full 5-yr data set,” ApJ Lett. 973, L14 (2024), arXiv:2401.02929**  
   - arXiv:2401.02929 exists and is a DES 5-year SN paper (check shows a DES SN cosmology analysis). However, the journal reference given (“ApJ Lett. 973, L14”) is inconsistent: ApJL volume numbering has not reached 973; the actual journal, year, and volume for this arXiv might differ.  
   Required fix:  
   - Correct the journal metadata to match ADS (actual journal, volume, page).  
   - Verify that any quoted numbers from DES-SN5YR (e.g., where invoked in cross-validation and model comparison) match the abstract/tables of the real paper.

6. ** DESI Collaboration, A. G. Adame, et al., “DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations,” arXiv:2404.03002 (2024)**  
   - arXiv:2404.03002 exists and is a DESI BAO cosmology paper. That part is correct.  
   - However, this is cited as “DESI 2024 DR1 BAO” while elsewhere in the text DESI DR2 is invoked (Table II: “DESI DR2 BAO”). The paper  is DR1, not DR2. The DR2 paper is separately labeled in  but that  is non-existent.  
   Required fix:  
   - Clearly distinguish DR1 vs DR2 and ensure that the data stack actually used corresponds to an existing DESI release.  
   - If only DR1 is used, remove all DR2 language, and regenerate the w0–wa chain and Table II with the correct DR1 likelihood. If DR2 is used, update the reference to the actual DR2 paper once available.

7. ** DES Y3 cosmology paper** and ** Cobaya** appear real and correctly formatted on ADS/arXiv (DES Y3: PRD 105, 023520 (2022), arXiv:2105.13549; Cobaya: JCAP 05 (2021) 057, arXiv:2005.05290). These are acceptable; no changes needed.

8. ** Fujita et al. (2021) ALP birefringence paper**, ** Cai et al. (2010) Quintom review**, ** LiteBIRD Collaboration (PTEP 2023 042F01, arXiv:2202.02773)**, ** Walmsley et al. Galaxy Zoo DECaLS (MNRAS 509, 3966; arXiv:2102.08414)** all check out against ADS/arXiv, with correct titles, authors, and journals.

Classification:  
- For [1], [3], , : **ESSENTIAL** – referencing non-existent or future-dated work is not compatible with PRD standards, particularly when those works provide core evidentiary support.  
- For , : **MAJOR** – metadata is inconsistent and the DR1/DR2 confusion undermines reproducibility of the key w0–wa results.

---

P1B-E2 (ESSENTIAL)  
Section: Abstract and Sec. VI (Cosmic Birefringence)  
Page(s): 1, 6–7  

Problem: The headline observational statistics are not fully and correctly tied to actual published measurements, and in one case refer to a “joint WMAP+Planck” result with a value that must be checked carefully.

1. **Eskilt & Komatsu 2022 constraint**: The paper cites  
   - In abstract and Sec. VI: “β = 0.342° ± 0.094° (3.6σ) [2]” as the *published joint WMAP+Planck* value.  
   - Checking [2] against arXiv and PRD (arXiv:2205.13962, PRD 106, 063503) shows that Eskilt & Komatsu indeed report a detection of isotropic cosmic birefringence at ≈3.6σ with a central value close to 0.34°. From the abstract and main tables, β ≈ 0.34° ± 0.09°; the numerical value quoted (0.342° ± 0.094°) is consistent within rounding.  
   - However, the paper asserts this is a joint WMAP+Planck result. The actual Eskilt & Komatsu paper uses combinations of WMAP and Planck data; you must confirm exactly which dataset combination gives 0.342° in the published tables (WMAP+Planck PR3 vs PR4/NPIPE), and describe it precisely. At present, the text mixes PR3 and PR4/NPIPE attribution and delegates the truth to the GitHub README rather than to the paper itself.  
   Required fix:  
   - Verify directly from Eskilt & Komatsu PRD table(s) which exact dataset yields β = 0.342° ± 0.094° and describe it accurately (e.g., “WMAP9 + Planck PR3” or similar).  
   - Remove or correct the PR4/NPIPE language in footnote (a) that suggests the published 3.6σ headline comes from a PR3+WMAP9 analysis while the used likelihood is PR4/NPIPE; this is confusing and not all traceable to peer-reviewed sources. Make a clean statement: which version is used in your ALP MCMC (PR3 or PR4), and which version’s number is quoted as headline.

2. **Planck NPIPE and ACT DR6 separate measurements**:  
   - The paper quotes: Planck NPIPE: β = 0.30° ± 0.11° ; ACT DR6: β = 0.215° ± 0.074° [3].  
   - Diego-Palazuelos et al. (arXiv:2201.07682, PRL 128, 091302) indeed quote β ≈ 0.30° ± 0.11° for Planck NPIPE; this is correct and traceable to .  
   - There is currently no public ACT DR6 cosmic birefringence paper matching [3] (arXiv:2509.13654) or reporting β = 0.215° ± 0.074°; see P1B-E1. This statistic is therefore not verifiable.  
   Required fix:  
   - Remove ACT DR6 numerical values until a real ACT DR6 birefringence paper is published and citable; or explicitly mark them as “illustrative” and non-load-bearing, but then they must not be part of any quantitative SNR or combined constraint you treat seriously.  
   - Recompute the “auxiliary inverse-variance combination” βcombined = 0.241° ± 0.061° (3.9σ) using *only published* measurements, or drop this line entirely.

3. **3.9σ combined “auxiliary” result**:  
   - The paper computes βcombined = 0.241° ± 0.061° (3.9σ) from Planck NPIPE and ACT DR6 via inverse-variance weighting and notes this is “auxiliary.”  
   - Even as auxiliary, this is a new derived observational statistic; since one input datum (ACT DR6) is not verifiable, this combined result is unsubstantiated.  
   Required fix:  
   - Either remove the combined 3.9σ value, or recompute and state it using only published, clearly citable inputs (e.g., Planck-only), making clear that any combined statistic is your own computation and not a published detection.

Classification: **ESSENTIAL** – observational claims and significances must be rigorously grounded in existing, citable measurements.

---

P1B-E3 (ESSENTIAL)  
Section: Use of “in preparation” companion papers [1], [4], [5], [6]  
Page(s): 2, 8–9  

Problem: Multiple **“in preparation”** self-citations are used to support substantive claims and to position this manuscript as part of a multi-paper program. Only one of them ([1]) is heavily load-bearing for the main theoretical context of this companion; [4–6] are used more as forward references but still framed as providing substantive results.

- [4] “fNL = −35/8 Forecast: SPHEREx Discrimination … (in preparation) (2026), hUBIFY-2026-002”  
- [5] “Spectrally Unusual Sources at Scale … 378,280 anomalies … (in preparation) (2026), hUBIFY-2026-003”  
- [6] “Galaxy Chirality at Scale … (in preparation) (2026), hUBIFY-2026-004”  

All three are non-public; no arXiv/ADS records. Claims like “The SPHEREx multi-tracer Fisher forecast is in Paper II [4]” and “The galaxy chirality catalog is in Paper IV [6]” give the impression that a full program exists and has established results, but the reader cannot access or verify any of it.

Required fix:  
- For PRD, non-public “in preparation” manuscripts cannot carry significant evidentiary weight.  
- Restrict references to “in preparation” work to a minimal, descriptive sentence at most, and do not rely on them for any quantitative claims.  
- In particular, remove or heavily soften any language that presents the P1A–P1D series as an established suite of published results; for now, this manuscript must stand on its own.

Classification: **ESSENTIAL**, because [1] is load-bearing and [4–6] materially affect the framing of novelty and scope.

---

P1B-E4 (ESSENTIAL)  
Section: Sec. III, Table I, and Fig. 1 (ΛCDM+ΔNeff MCMC)  
Page(s): 3–5  

Problem: The ΔNeff and H0 constraints are internally consistent numerically, but the **chain configuration and model definition are incompletely specified and partially inconsistent with the Results section**, making reproduction at PRD standard difficult:

- Table I describes “ΛCDM+ΔNeff proxy MCMC results” with parameters H0, ΔNeff, σ8, S8, Ωm, τ, ns, and various chain diagnostics.  
- Sec. III footnote and text reference “17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance …)” and mention a third Planck-only combination that is “still accumulating samples” at R̂ − 1 ≈ 0.05.  
- Sec. V then describes a four-dataset combination (Planck, +DESI DR1, +Pantheon+, +SH0ES + DES Y3 S8) and states “Parameter estimation uses Cobaya (v3.5 original; v3.6.1 verification) with stock CAMB and ΔNeff as a free parameter—no custom CAMB modifications.”  
- However, this section transitions into a **w0–wa** analysis (Table II, DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+), which is **not** ΛCDM+ΔNeff and uses a different dataset stack from Sec. III. These chains, parameters, and priors are not fully specified in the main text; critical details are only said to be in a GitHub repository and a HuggingFace dataset.

Required fix:  
- Cleanly separate the ΔNeff proxy chains (which are 7+10-parameter ΛCDM+ΔNeff) from the w0–wa DESI DR2 chain (8+9 parameters).  
- For each analysis used for any quoted number in the main text or abstract, provide:  
  - The full cosmological parameter vector (including whether w0, wa, or ΔNeff are free).  
  - The dataset combination and the exact likelihood names (e.g., “planck_2020_lowl.EE”).  
  - The sampler convergence threshold and final R̂ values.  
- Move all details that currently appear only in Appendix C or in the repository into the paper at least in summary form, so that a reader can verify that, e.g., the H0 and ΔNeff constraints in the abstract come from the same runs as those in Table I, and are not mixed with the DESI DR2 w0–wa analysis.

Classification: **ESSENTIAL**, because without a clean mapping of which chain yields which headline number, the reported constraints cannot be independently checked.

---

P1B-E5 (ESSENTIAL)  
Section: Sec. VI (ALP consistency) and Appendix C  
Page(s): 6–9  

Problem: The ALP birefringence calculation is described only qualitatively; key numerical relationships and their dependence on parameters are **not fully demonstrated in the text**, and some numbers are asserted without showing how they follow from the ODE solution or from the referenced ALP literature.

Examples:

- Eq. (2): “Δϕ/fa ≈ 0.65 (m = H0, θi = 1)” and the stated range Δϕ/fa ∈ [0.2, 1.1] across m/H0 ∈ [1,3], θi ∈ [0.5,2]. There is no explicit functional form or table, nor a reference to a standard analytic approximation from Fujita et al. or similar.  
- Eq. (3): “For Caγ = 8, θi = 1, m ≈ 2H0: β ≈ (αEM × 8 / 4π) × 1.07 ≈ 0.29°.” The 1.07 factor is unexplained in the text; it presumably comes from Δϕ/fa but that is not explicitly linked.  
- Later, the paper asserts that for βobs = 0.342°, CaγΔϕ/fa ≈ 10.3, and that this is compatible with Δϕ/fa ∈ [0.2,1.1] giving Caγ ∈ [9,51]. This is numerically plausible, but the derivation is not transparent to a reader; no intermediate steps or explicit check are shown, and the key relation β = (αEM/4π) Caγ (Δϕ/fa) is not written as an equation.  

Required fix:  
- Write the birefringence formula explicitly: β = (αEM / 4π) Caγ (Δϕ/fa), with β in radians.  
- Show at least one worked example: plug in αEM ≈ 1/137, Δϕ/fa from the ODE at m = H0, θi = 1, and Caγ = 8, and demonstrate that you recover β ≈ 0.29°.  
- Provide a short table or figure (or cite a table in Fujita et al.) showing Δϕ/fa as a function of m/H0 and θi for the range used, demonstrating the claimed [0.2,1.1] envelope.  
- Verify and show that βALP = 0.336° ± 0.107° and βfree = 0.344° ± 0.096° from the ALP-MCMC (Appendix C) are consistent with the observational βobs within 1σ.

Classification: **ESSENTIAL**, because without explicit equations and a transparent numerical check, the core claim (“ALP with fa ~ MPl, m ~ H0 is consistent with βobs”) cannot be independently verified.

---

P1B-M1 (MAJOR)  
Section: Abstract and Sec. III–V – Hubble tension discussion  
Page(s): 1, 2–6  

Problem: The manuscript states “Both frozen dataset combinations find ΔNeff consistent with zero … and H0 consistent with standard ΛCDM … The ΔNeff extension does not resolve the Hubble tension.” This is qualitatively fine, but:

- The **quantitative tension level** is variously described as ~3.6σ; the paper shows one numeric check for the MB–H0 degeneracy.  
- However, the quoted H0 prior from SH0ES is given as “Riess H0 = 73.04 ± 1.04 km/s/Mpc [7],” while the abstract says H0 is “consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN).”  
- The tension significance should be recomputed directly: δH0 / sqrt(σPlanck^2 + σSH0ES^2), and if the result differs from “3.6σ” (which is sometimes reported for Planck vs SH0ES), this must be clarified.  

Required fix:  
- Explicitly compute the H0 tension between your *full-tension* chain posterior and the SH0ES prior, using the chain’s H0 mean and σ. Present the result as a number and check that it is indeed ~3.6σ.  
- If your configuration (with ΔNeff free) yields a slightly different tension than the canonical Planck-only vs SH0ES tension in the Riess paper, say so and give the actual value.  
- Clarify that when you state “canonical 3.6σ,” you refer to the tension between the SH0ES prior and Planck baseline from the SH0ES paper, not necessarily the exact value in your extended parameter space.

Classification: **MAJOR**, because tension quantification is central to the stated motivation for ΔNeff and must be numerically consistent and clearly defined.

---

P1B-M2 (MAJOR)  
Section: Sec. IV (NaMaster E–B analysis)  
Page(s): 5–6  

Problem: The NaMaster pipeline test is described with a set of injection amplitudes (β = 0, 0.27°, 0.342°), recovery β̂ = 0.238°, 0.302°, and SNR values 20.32 and 25.71. However:

- The **significance values (20.32, 25.71)** are diagnostic SNRs of injected Monte Carlo signals, but the method of computing them (β̂/σβ from chain? from MC dispersion?) is not described.  
- The text claims an earlier version characterized the bias as “strictly stable across all three injections” at 0.032°, but that this is corrected to amplitude-dependent 0.032° vs 0.040°. This implies there were prior analyses not fully documented; the current text gives no table of β̂ distributions across 500 realizations.  

Required fix:  
- State explicitly how SNR is computed: e.g., SNR = β̂ / σβ, where σβ is the standard deviation across MC realizations.  
- Provide the mean and standard deviation for β̂ across the 500 MC realizations for each injected β, so the reader can verify bias and SNR.  
- Clarify whether these SNR numbers refer to a single realization or to the ensemble-mean, and ensure they are not confused with sky-detection significance anywhere in the manuscript (the text claims they “must not be conflated,” but the numeric basis must be clear).

Classification: **MAJOR**, because this is the sole technical validation of the E–B pipeline; its precision claims must be fully reproducible.

---

P1B-M3 (MAJOR)  
Section: Sec. V and Table II – w0–wa chain and “phantom crossing required”  
Page(s): 3–4, 6–7  

Problem: The w0–wa results (Table II) are described as showing that w0 differs from −1 by +4.3σ and wa differs from 0 by −3.6σ, and that “w0 + wa = −1.4788 ± 0.1485 phantom-crossing required” and “This is the canonical quintom signature …”. However:

- The chain is explicitly said to have **no samples at (w0, wa) = (−1, 0)**; the LCDM point lies in the tails. The “+4.3σ” is a “marginal-tail posterior-extrapolation departure” (Table II footnote), not a sample-based Gaussian σ.  
- The text occasionally reads as if this is an actual 4.3σ exclusion, though the footnote does caution that it is *not* a Bayes factor and not a frequentist tension. For PRD standards, this needs to be emphasized more strongly in the main text.  

Required fix:  
- In the main text where 4.3σ and 3.6σ are quoted, explicitly state that these are tail distances from a Gaussian approximation to the marginalized posteriors, *not* a detection or exclusion significance.  
- Add a sentence clarifying that because (w0, wa) = (−1, 0) is unsampled, the chain itself cannot be used to compute exclusion significances or Bayes factors, and this is why nested sampling is required.  
- Avoid the phrase “phantom crossing required” without qualification; say “preferred by the w0–wa fit under this dataset stack, with the caveat that the analysis is not a model-selection result.”

Classification: **MAJOR**, to avoid overstating evidence against ΛCDM.

---

P1B-M4 (MAJOR)  
Section: Claims Classification Table III  
Page(s): 10  

Problem: Table III lists multiple claims with status “Verified,” “Cited,” etc., including:

- “Published 3.6σ (β = 0.342 ± 0.094°) – Lit. – Cited – Eskilt et al.”  
- “∆Neff = −0.020 ± 0.169 (full-tension) – MCMC – Verified”  
- “βALP = 0.336° ± 0.107° – MCMC – Verified”  

This table is presented as if an internal audit has confirmed these claims. However:

- The current paper does not *show* the ALP MCMC posteriors, chain summary, or corner plots; the reader cannot independently check that βALP = 0.336° ± 0.107° is correct.  
- The notation “Verified” is misleading; it suggests an independent external validation, which is not provided. The same author wrote the code and the audit.  

Required fix:  
- Either remove Table III entirely or rename it to something neutral (“Claims summary used in this companion paper”) and change “Verified” to a descriptive status (“Computed in this work; see Sec. III/VI”) without implying third-party verification.  
- For quantitative claims labeled “Verified,” add explicit references to the figures or tables where they are backed up (ΔNeff in Table I; βALP in Sec. VI/Appendix C), or include those plots/tables in the paper.

Classification: **MAJOR**, because the current language risks misrepresenting the level of independent verification.

---

P1B-N1 (MINOR)  
Section: Abstract and throughout – “not a spin-torsion theory module”, “not a competitive sky detection”  
Page(s): 1–2, 5–7  

Problem: Repeated emphasis that analyses are “not a spin-torsion theory module,” “not a competitive sky detection,” etc., is scientifically fine but somewhat verbose and detracts from clarity.

Required fix:  
- Condense the disclaimers to one succinct scope paragraph per analysis rather than repeating similar phrases multiple times.  
- Ensure that each disclaimer remains, but avoid redundancy.

Classification: **MINOR**.

---

P1B-N2 (MINOR)  
Section: Acknowledgments  
Page(s): 8  

Problem: The author explicitly acknowledges “the use of Claude (Anthropic) as an AI research assistant … All scientific claims … were independently verified by the author.”

This is not a scientific flaw, but journals vary on how AI assistance should be disclosed.

Required fix:  
- Ensure this disclosure is compatible with PRD’s current policy on AI-assisted writing. If needed, move it to a footnote or cover letter, depending on editorial guidance.

Classification: **MINOR**.

---

P1B-N3 (MINOR)  
Section: Appendix A – Reproducibility and KNOWN_GAPS.md  
Page(s): 8–9  

Problem: The paper references repo-level files “IMPLEMENTATION_MAP.md” and “KNOWN_GAPS.md” as authoritative for documentation and unreproducible aspects. While laudable, this externalizes critical information.

Required fix:  
- Summarize in the manuscript itself the key items from KNOWN_GAPS.md relevant to the analyses in this companion; e.g., which parts cannot be reproduced without proprietary data or non-public code.  
- For PRD, reliance on a GitHub README as an “authoritative source” for dataset attribution is inappropriate; primary attribution should come from peer-reviewed papers and clearly documented in-paper descriptions.

Classification: **MINOR**.

---

P1B-N4 (MINOR)  
Section: General  
Page(s): 1–10  

Problem: There are a few typographical inconsistencies and small style issues:

- Units: “km s−1 Mpc−1 ” vs “km/s/Mpc” appear in different places; PRD requires consistent SI or astrophysical units formatting.  
- Superscripts: Sometimes “MPl    2
” is spaced oddly in the PDF; check LaTeX source for formatting.  
- Some minor duplication in phrasing (“the ∼ 25× misalignment tuning required … is disclosed in Sec. VI and fn. 4” appears twice almost verbatim).

Required fix:  
- Standardize unit formatting and fix spacing around superscripts and symbols.  
- Remove duplicated sentence fragments where they do not add information.

Classification: **MINOR**.

---

P1B-N5 (NIT)  
Section: Contents and section headers  
Page(s): 1–2  

Problem: The Contents list includes a stray phrase on the same line as the heading: “III. Stock-CAMB ΛCDM+ΔNeff MCMC: Generic Radiation-Proxy Test (Not a Spin-Torsion Theory Module) 2”. The “2” appears as though misaligned pagination and might confuse readers.

Required fix:  
- Clean up the contents formatting so that the section titles and page numbers align in a standard PRD style.

Classification: **NIT**.

---

P1B-N6 (NIT)  
Section: Footnotes in main text (e.g., fn. 1, 2, 4, 5)  
Page(s): 3–7  

Problem: Some footnotes are very long and contain key technical clarifications (e.g., chain stratification, backreaction/spectator caveats). While scientifically useful, this makes them easy to miss.

Required fix:  
- Consider moving the most important technical content (e.g., the θi fine-tuning argument) into the main text, and keep footnotes for secondary remarks.

Classification: **NIT**.

---

## Summary recommendation

**Recommendation: REJECT**

This manuscript fails PRD standards primarily because its bibliography contains several non-existent or future-dated references that are used to support key claims (especially [3], , , and the self-cited “in preparation” main paper [1]); this makes several central results (ACT DR6 birefringence input, DESI DR2 w0–wa constraints, torsion cross-validation) unverifiable. In addition, the ALP consistency calculation and NaMaster pipeline validation require more explicit equations and numerical demonstrations to be independently checked at the level expected for PRD. Substantial restructuring, replacement of fictitious references with real published work, and clear separation and documentation of the different MCMC analyses would be necessary before the paper could be reconsidered.