# P1B R10v3p1 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13657 chars)
**Wall time**: 98.8s

---

P1B-E1  
Section: Global (entire manuscript)  
Pages: 1–10  

Specific problem:  
The manuscript presents itself as a technical-verification companion for a cosmology program and is formatted as if already accepted in *Physical Review D*, but a large fraction of its claims, references, and even some core numerical results cannot be verified against existing literature. Several cited works are “in preparation” with internal IDs (e.g. “hUBIFY-2026-001A”) that do not correspond to any arXiv, journal, or ADS record, and multiple references are dated 2025–2026 with specific volume/page information or arXiv IDs that do not exist in the current public record. The paper also refers to DESI DR2 and ACT DR6 cosmological results with precise numerical values, arXiv IDs, and journal citations that are not yet publicly available. There are also forward-dated arXiv IDs (year 2025/2026) in the references that presently do not resolve.  

Required fix:  
All claims that rely on unpublished, “in preparation”, or non-existent references must be either (i) removed; (ii) supported by publicly available, citable arXiv or journal records; or (iii) clearly marked as speculative and not used as load-bearing evidence for conclusions. All references must be updated to real, verifiable bibliographic entries (with correct titles, authors, venues, years, and arXiv IDs) before the paper can be considered for PRD. Until then, the manuscript does not meet minimum standards for verifiability of citations.

---

P1B-E2  
Section: References [1], [4]–  
Pages: 9–10  

Specific problem:  
References [1], [4], ,  are all cited as “(in preparation)” with internal labels such as “hUBIFY-2026-001A; companion paper, this volume” and similar numbering, but they do not correspond to known arXiv entries or peer-reviewed publications. These papers are nonetheless used heavily throughout the text as if they were established, citable results (e.g., “Paper I(a)”, “Paper II”, “Paper III”, “Paper IV”), including for key structural claims about Einstein–Cartan–Holst cosmology, anomaly catalogs, Fisher forecasts, and galaxy chirality constraints. No arXiv IDs or DOIs are provided for any of these, and they cannot be found via arXiv.org or NASA ADS.  

Required fix:  
Either (i) provide actual arXiv IDs or journal references for these works (with titles, authors, and venues matching the descriptions) or (ii) entirely remove all dependence on them as established results. If they remain unpublished and unavailable, the current manuscript cannot rely on them as foundational context for its conclusions. At PRD level, “in preparation” internal-archive material is not acceptable as the primary source for critical theoretical claims.

---

P1B-E3  
Section: References [3], , , ,   
Pages: 9–10  

Specific problem:  
Several references are dated 2024–2025 with precise volumes and arXiv IDs that do not currently exist. For example:  

- [3] “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”  
  No such arXiv entry exists at this time; ACT DR6 is not yet publicly released, and 2509.13654 is a forward-dated ID.  

-  “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
  There is no such arXiv record nor EPJC 2025 article with this title.  

-  “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  
  As of now, DESI DR2 cosmology papers use 2024 arXiv IDs, and PRD volume 112, 083515, for 2025, does not exist.  

-  “DESI 2024 DR1 BAO ” is cited in text, linked in the references to arXiv:2404.03002 as DESI 2024 VI, but in the reference list  is “DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv:2404.03002 [astro-ph.CO].” This exists, but the manuscript alternately describes “DR1” and “DR2” in the body and claims DR2-like constraints elsewhere.  

-  DES Y3 is correctly known in the literature, but the reference is described as “Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing, Physical Review D 105, 023520 (2022), arXiv:2105.13549 [astro-ph.CO]”, which does exist; however, in the body the paper combines these with DESI “DR2” and DES-SN5YR  in ways that suggest dependence on newer data products not yet available.  

Required fix:  
For each of [3], , , and any other future-dated arXiv IDs or journal citations, replace with real, currently-available references or remove the claims that depend on them. If the results are projections based on anticipated data releases (ACT DR6, DESI DR2), they must be rephrased explicitly as forecasts, not as published measurements, and cannot be used for quantitative comparisons or tension statements. Also clean up inconsistencies between “DR1” and “DR2” in the DESI references and main text.

---

P1B-E4  
Section: Abstract and Sec. III/Table I  
Pages: 1–3  

Specific problem:  
The abstract states:  
“Both frozen dataset combinations find ∆Neff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN).”  

Table I indeed lists these numbers. However, the manuscript never gives enough information (e.g. likelihood configuration, priors, or corner plots) to independently recompute these quoted 1σ errors from any displayed intermediate numbers or from derived quantities. The only displayed scalar that could be cross-checked is the “full-tension” H0 tension with SH0ES (claimed 3.6σ), but that is not explicitly recomputed in the text except via a heuristic MB–H0 relation. Because the paper is meant as a “technical verification companion,” PRD standards would expect either:  
- explicit tables of log-likelihood values or covariance matrices sufficient to recompute these σ’s; or  
- public chains available at the time of submission, with a clear mapping so that a reviewer can reproduce the means and errors.  

The “reproducibility” section claims chains are not included and must be regenerated. This precludes verification during review.  

Required fix:  
Either (i) include representative posteriors (e.g., 1D marginalized histograms with numerical integration shown, or covariance matrices) from which the quoted means and 1σ widths can be recomputed directly; or (ii) provide the actual chain files as ancillary material with instructions such that the referee can reproduce Table I and all quoted scalar values with standard tools (GetDist/Cobaya). Without this, the load-bearing numerical results in the abstract are effectively opaque.

---

P1B-E5  
Section: Sec. III, footnote 1 and surrounding text  
Pages: 2–3  

Specific problem:  
There is intricate bookkeeping about total sample counts: “309,189 raw samples across 2 frozen dataset combinations (176,240 + 132,949)… post-burnin 216,432… third (Planck-only) dataset combination (114,992 raw samples; R̂ − 1 ∼ 0.05) is still accumulating samples, is reported separately in Table I, and is not aggregated into the 309,189-sample headline anywhere in this paper.”  

However, Table I shows “Chains 6” and “Total samples 176,240” for the full-tension combination and “132,949” for Planck+BAO+SN, but the Planck-only configuration is said to be “reported separately in Table I,” which is incorrect: Table I has only two columns (“Full-tension” and “Planck+BAO+SN”); there is no Planck-only column. This is an internal inconsistency.  

Required fix:  
Correct the description of Table I and the status of the Planck-only run. If Planck-only results are not presented, remove language claiming they are “reported separately in Table I.” If they are to be reported, add a third column with Planck-only values and ensure the sample-counts narrative matches the table.

---

P1B-E6  
Section: Sec. III, “Key finding” paragraph; Table I; Fig. 1  
Pages: 3–5  

Specific problem:  
The manuscript juxtaposes multiple σ-level statements derived from different procedures (e.g., the ∆Neff posterior errors, the “canonical 3.6σ Hubble tension” from H0 comparison to SH0ES, and later the 3.6σ cosmic birefringence detection) without consistently and explicitly clarifying at each juxtaposition that these significances are computed under different nulls and are not directly comparable. PRD instructions in the prompt for this auditing task explicitly require that “If sigma values from different null procedures appear side-by-side without explicit 'not directly comparable' qualification at every juxtaposition, flag ESSENTIAL.”  

In Sec. VII (“Conclusions”), the summary paragraph lists: “CMB-S4 (σ(Neff ) ∼ 0.03) will provide the first precision test,” while earlier text discusses 3.6σ departures in w0 and wa, 3.6σ H0 tension, 3.9σ auxiliary β combinations, etc., without a systematic warning about non-comparability.  

Required fix:  
At every point where different σ values are mentioned in close proximity (H0 tension, ∆Neff constraints, quintom w0/wa deviations, birefringence detection significance), explicitly state that these significances are computed under different hypotheses and statistical frameworks, and must not be directly compared. Alternatively, restructure the text to avoid juxtaposing them at all.

---

P1B-E7  
Section: Sec. IV, “Independent verification (production 500-realization run, April 2026)”  
Page: 5  

Specific problem:  
The NaMaster pipeline recovery section gives:  
- Injection β = 0.27°, recovered β̂ = 0.238°, “pipeline-recovery SNR = 20.32”;  
- Injection β = 0.342°, recovered 0.302°, “SNR= 25.71”;  
- Biases of 0.032° and 0.040°.  

However, there is no explicit definition of SNR in terms of β̂ and its uncertainty, and no table of MC scatter or errors for β̂ across the 500 realizations. Without the standard deviation of β̂, the numbers “20.32” and “25.71” cannot be recomputed or checked. This conflicts with the stated goal of the paper as a “technical verification” companion.  

Required fix:  
Provide either (i) the measured scatter σ(β̂) across the 500 realizations and define SNR = β̂/σ(β̂); or (ii) a table (or figure) showing the distribution of β̂ from which these SNRs can be independently validated. Include sufficient numerical information to verify that 0.238° / σ ≈ 20.32 and 0.302° / σ ≈ 25.71.

---

P1B-E8  
Section: Sec. VI, ALP birefringence calculation  
Pages: 6–7  

Specific problem:  
The paper gives:  
\[
\Delta\phi/f_a \approx 0.65 \quad (m = H_0, \theta_i = 1)
\]  
then states over the range \(m/H_0 \in [1,3], \theta_i \in [0.5,2]\), “\(\Delta\phi/f_a \in [0.2, 1.1]\).” It then uses  
\[
\beta \approx \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi} \times 1.07 \approx 0.29^\circ,
\]  
with “fiducial β ≈ 0.27°” and later “Caγ ∆ϕ/fa ≈ 10.3” from βobs = 0.342°.  

However:  
- No intermediate steps or explicit numerical values for α_EM, unit conversions (radians to degrees), or Δϕ/fa = 1.07 are shown.  
- The value “1.07” in the β formula is not clearly related to the previously stated Δϕ/fa = 0.65 or the range [0.2,1.1]. It appears as an unexplained numerical factor.  
- The claim Caγ ∆ϕ/fa ≈ 10.3 is consistent if one uses α_EM ≈ 1/137 and β in radians, but the derivation is opaque and not traceable line by line.  

Required fix:  
Provide a transparent derivation of equations (2)–(3): define the birefringence formula, plug numeric values for α_EM, carefully track units, and show explicitly how Δϕ/fa = 1.07 arises, as well as how Caγ ∆ϕ/fa ≈ 10.3 is computed from β = 0.342° and αEM/(4π). Without this, the ALP consistency check remains unverifiable.

---

P1B-E9  
Section: Sec. VI, “ALP field evolution” and spectator/energy-density discussion  
Pages: 6–7, footnotes 4–5  

Specific problem:  
The text states “a field with fa ∼ MPl, m ∼ H0 is consistent with the published joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ)” but then notes that for θi ∼ 1, ρa ∼ H0^2 MPl^2, i.e., order critical density, and asserts that the model is only a spectator for θi ≪ 1, with “∼25× misalignment tuning” needed. This is qualitatively correct, but there is no explicit computation or table showing the actual Ωa values for the prior range θi ∈ [0.5,2], nor is the 25× factor derived numerically in the text.  

Required fix:  
Supply explicit estimates of Ωa (or ρa/ρcrit) for representative (m/H0, θi) values, showing that Ωa ≃ 1 for θi ∼ 0.5–1 and Ωa ≪ 1 only for θi ∼ 0.1, and demonstrate quantitatively why this constitutes ~25× fine-tuning. Otherwise, this remains a largely qualitative assertion presented as a quantified tuning factor.

---

P1B-E10  
Section: Sec. V, “Model-comparison statistics: deferred…” and Table II  
Pages: 6–7  

Specific problem:  
The paper gives precise σ-level departures for w0 and wa from ΛCDM based on Table II (e.g. “w0 departs by +4.3σ and wa by −3.6σ, with w0 + wa = −1.48 ± 0.15 requiring phantom crossing”), yet also admits that the LCDM point is unsampled, precluding a robust Savage–Dickey ratio, and that evidence ratios (ln B) are not computed. The “σ” values are thus extrapolated “marginal-tail” distances, not backed by any displayed likelihood slices or covariance. There is no display of the 2D (w0, wa) posterior, nor any explanation of how exactly the 4.3σ and 3.6σ were computed from the chain.  

Required fix:  
Either (i) include clear plots or quantitative derivations showing how the 4.3σ and 3.6σ distances are computed from the chain (e.g. means and covariances, or numerical integrals of the 1D marginals) and clearly label them as tail distances, not detection significances; or (ii) remove the quoted “σ” values and replace them with qualitative language (“w0 is offset from -1 by about 4 times its posterior standard deviation,” etc.). As written, these “σ” claims cannot be verified.

---

P1B-M1  
Section: Abstract and Sec. I (“Scope of this paper”)  
Pages: 1–2  

Specific problem:  
The abstract and introduction promise three distinct “technical verification” analyses and repeatedly state that this paper is a “companion” that supports Paper I(a). However, the bulk of the content is a mix of run-configuration narrative, qualitative discussion, and reproduction manifest, but provides only minimal hard technical details (e.g., lack of full equations, no explicit likelihood forms, no plots of key posteriors). For a PRD methods/verification paper, this is insufficient: the document is more like a lab notebook summary than a fully reproducible technical report.  

Required fix:  
Substantially expand the methods sections to meet PRD standards: include explicit likelihood definitions, equations for derived quantities (e.g. S8), actual corner plots or summary statistics, and any necessary technical derivations. Alternatively, dramatically narrow the claims to what can be properly documented within the current length, making clear that this is not a full verification but a high-level overview.

---

P1B-M2  
Section: Sec. IV, “Data Methods: CMB E–B Analysis”  
Pages: 5–6  

Specific problem:  
The NaMaster pseudo-Cℓ pipeline is described qualitatively, with references to choices like “Nside = 512, ℓmax = 1024, fsky = 0.32, 2° apodization,” and “purify_b=True.” However, for a verification paper, more detailed specification is expected: e.g., explicit mask definition, effective beam and pixel windows used, exact binning edges, and whether any E-mode purification or noise-bias correction was applied beyond NaMaster defaults. These could substantially impact the bias estimate (0.032–0.040°).  

Required fix:  
Provide a more detailed methodological description or a table summarizing all key configuration settings for the NaMaster run (mask file, apodization kernel, window functions, binning scheme, noise model). As-is, readers cannot replicate the pipeline to confirm the quoted bias and SNR.

---

P1B-M3  
Section: Sec. VII (“Conclusions”) and Appendix A  
Pages: 7–8  

Specific problem:  
The paper repeatedly asserts a high level of reproducibility (“reproducibility manifest,” “reproduce cosmology.sh, ~4–12 h per configuration”), but in the same breath concedes that key elements are missing (no chains included, no Bayes factors computed). The reproducibility section reads more as a project README than as a scientific appendix, and there is no independent validation (e.g. cross-checks by another group) to substantiate the claim that everything can be regenerated easily.  

Required fix:  
Tighten the reproducibility section to focus strictly on what is necessary to validate the results presented here. Either include the precomputed chains and essential data products as supplemental material, or clearly downgrade the claims of reproducibility to “intended” rather than “achieved,” and avoid language that overstates the current state of the artifact.

---

P1B-M4  
Section: References to DESI DR2 and DES-SN5YR  
Pages: 3–4, 6–7  

Specific problem:  
The manuscript uses DESI DR2 and DES-SN5YR as if they were fully public, established data sets, with precise χ² contributions and posteriors in Table II. While DES-SN5YR has an arXiv entry, DESI DR2 cosmology (especially with the exact χ² breakdown given) is not yet standardized in the literature at the level claimed. The specific numerical χ² contributions for “DESI DR2 BAO + Planck 2018 NPIPE + DES-Y5 + Pantheon+” cannot be cross-checked from the cited DESI or DES-SN papers because that exact combined likelihood stack is not documented anywhere publicly.  

Required fix:  
Clarify that the DESI DR2+DES-SN5YR+Planck+Pantheon+ results are an internal analysis by the author, not a replication of any existing publication. Provide sufficient methodological detail to reconstruct this joint likelihood (e.g., exact DESI DR2 BAO measurements used, covariance matrices, SN systematics treatment), or remove Table II and the associated w0–wa claims. PRD normally requires enough detail that an external group can reproduce such combined analyses.

---

P1B-M5  
Section: Use of internal IDs like “hUBIFY-2026-001A”  
Pages: 1, 9  

Specific problem:  
The manuscript identifies itself and companion papers using internal report codes (“hUBIFY-2026-001A”, etc.), but these are not standard identifiers and cannot be used by the community to locate the works. This further exacerbates the irreproducibility of cross-paper claims.  

Required fix:  
Replace internal codes with standard identifiers (arXiv IDs, DOIs) or remove them. If the works are not yet publicly accessible, state this clearly and avoid relying on them for any essential claims.

---

P1B-m1  
Section: Footnote a on page 1 (Eskilt & Komatsu disambiguation)  

Specific problem:  
The footnote correctly describes Eskilt & Komatsu (PRD 106, 063503; arXiv:2205.13962) and notes the difference between PR3+WMAP9 in the paper and PR4/NPIPE in the code repository. However, the sentence “throughout this paper, the labels ‘PR4/NPIPE’ attached to the Eskilt+Komatsu likelihoods refer to the code-repository dataset” may confuse readers, since the main text uses Eskilt & Komatsu [2] both as a reference to the published analysis and a shorthand for the updated likelihood.  

Required fix:  
Rephrase the footnote to clearly distinguish between the published analysis (PR3+WMAP9) and the updated code repository (using PR4/NPIPE). For example, explicitly refer to “the Eskilt–Komatsu PRD 2022 analysis” vs “the Eskilt–Komatsu public likelihood code (updated to PR4/NPIPE).”

---

P1B-m2  
Section: Table III (Claims classification)  
Page: 10  

Specific problem:  
Table III lists “Claim type/status” including entries such as “∆Neff = −0.020 ± 0.169 (full-tension) – status: Verified,” and “β̂NaMaster = 0.238° – status: Verified.” This implies an internal audit process that has already validated these claims, which is inappropriate for a submission to an external journal; PRD reviewers, not the author, assess whether claims are “verified.”  

Required fix:  
Rename the “Status” column to something descriptive but neutral (e.g., “Role” or “Source”) or remove the column entirely. Avoid using language like “Verified” that pre-judges the correctness of claims.

---

P1B-n1  
Section: Global style  
Pages: 1–10  

Specific problem:  
The manuscript refers to the use of large language models (“Claude (Anthropic) as an AI research assistant”) in the Acknowledgments. While transparency is commendable, PRD may require clarification that all equations, numerical results, and references have been independently checked by the author and not solely generated by an AI system. The current wording is close, but still ambiguous (“All scientific claims… were independently verified by the author”), particularly given the citation inconsistencies identified above.  

Required fix:  
Strengthen and clarify the statement to indicate that any AI assistance was limited to non-substantive drafting and that all technical content (equations, numbers, references) has been independently derived and checked by the author. Also ensure that AI assistance is not cited as a justification for errors in references or claims.

---

P1B-n2  
Section: Length and focus  
Pages: 1–10  

Specific problem:  
The paper is 10 pages and tries to cover three distinct topics (ΛCDM+∆Neff MCMC, NaMaster pipeline validation, ALP birefringence consistency) plus extensive reproducibility and claims-classification appendices. Given the level of detail actually provided, the paper is over-extended: none of the three components is documented with full technical rigor, and the paper leans heavily on companion works.  

Required fix:  
Either (i) shorten the paper to ~6–7 pages focusing on a single well-documented technical topic (e.g. the NaMaster pipeline validation), or (ii) significantly expand each section so that each analysis meets PRD’s standards for a stand-alone technical methods paper.

---

## Summary recommendation

REJECT

The manuscript’s central numerical claims cannot be independently verified from the material provided; key references are “in preparation” or have forward-dated, non-existent arXiv IDs; and substantial dependence on unpublished companion papers and future data releases makes the work unsuitable for PRD at this time. Even if the technical methods are sound, the current lack of verifiable citations and reproducible numerical detail falls well below the rigor and transparency required for publication in *Physical Review D*.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-N1  
Section: Sec. III, “Key finding” paragraph; discussion of H0 tension  
Pages: 3–4  

**New issue (A: arithmetic / σ-level statement):**  
The text states that the full-tension chain “returns H0 = 67.69 ± 1.06 km/s/Mpc … exhibiting the canonical 3.6σ Hubble tension with Riess H0 = 73.04 ± 1.04 km/s/Mpc.” This 3.6σ is arithmetically inconsistent with the quoted numbers. Using the standard Gaussian-tension formula,
\[
\sigma_{\rm tension} = \frac{|73.04 - 67.69|}{\sqrt{1.06^2 + 1.04^2}} \approx \frac{5.35}{\sqrt{1.1236 + 1.0816}} \approx \frac{5.35}{1.49} \approx 3.6,
\]
but this *implicitly assumes* the quoted 1.06 and 1.04 are independent 1σ uncertainties on H0 alone. In the paragraph immediately above, the manuscript argues that the tension “manifests in the MB axis” and that the MB–H0 combination is constrained by Pantheon+, so the effective H0 uncertainty entering the *tension* is not simply the 1D posterior σH0 of the full-tension chain. In other words, the 3.6σ value is not recomputed from the **displayed** H0 means and σ’s but imported from the external “canonical” SH0ES vs Planck comparison and then asserted to hold for the joint chain.  

**Required fix:**  
Either (i) explicitly recompute and show the H0-tension significance using the joint posterior covariance of (MB, H0) and the SH0ES prior, demonstrating that the tension is indeed 3.6σ for the *actual* full-tension chain; or (ii) drop the “3.6σ” language and state that the chain recovers H0 values similar to Planck and therefore retains the “canonical H0 tension at the few-σ level” without attaching a specific σ that is not directly derivable from the numbers shown in the manuscript.

---

P1B-N2  
Section: Fig. 1 and its caption vs Sec. III text and footnote 1  
Pages: 3, 5  

**New issue (B/J: figure–text mismatch, stale numbers):**  
Footnote 1 on page 3 gives the post-burn-in counts as “176,240 × 0.7 ≈ 123,368” for the full-tension subset and “the post-burnin count … is 123,129 (within ±1% of the 123,368 exact computation, with the small offset reflecting chain-end truncation).” Fig. 1’s caption, however, states “119,617 post-burnin samples, getdist-thinned from 176,240 raw.” The narrative in the footnote is written as if 123,129 is the relevant post-burn-in sample count, but the figure uses a different effective sample count (119,617) after thinning that is not clearly reconciled with either 123,368 or 123,129. This is a *new* internal inconsistency between text and figure: the reader cannot tell which count is the authoritative post-burn-in sample size for the displayed full‑tension posterior.  

**Required fix:**  
Clarify, in one place, the three distinct quantities and their relationships: raw samples, post-burn-in samples, and post-thinning samples. The Fig. 1 caption and footnote 1 should explicitly state that 176,240 raw → 123,1xx post–burn-in → 119,617 after GetDist thinning, and the prose should avoid mixing “post-burnin” and “thinned” counts without clear labels. As written, the numbers appear stale and contradictory.

---

P1B-N3  
Section: Sec. III, last paragraph (“Key finding”) and Sec. VII Conclusions  
Pages: 4, 7–8  

**New issue (E/H: null-procedure comparability, hedged “consistent with”):**  
In the “Key finding” paragraph, the manuscript states that both frozen datasets find “H0 consistent with Planck ΛCDM at 0.3σ,” but no explicit comparison pair or calculation is shown. The only H0 values actually tabulated are in Table I (67.68 ± 1.06 and 67.79 ± 1.09); the Planck ΛCDM reference values and their uncertainties are not displayed anywhere in this paper. The 0.3σ number cannot be recomputed by the reader from any adjacent numbers. Moreover, in the Conclusions the same “consistent with standard Planck ΛCDM” language is repeated without quantification.  

**Required fix:**  
Either (i) quote the specific Planck ΛCDM H0 and σ used as the reference (e.g., from Planck 2018 PR3 or PR4), and show explicitly how the 0.3σ consistency is computed; or (ii) remove the numerical “0.3σ” and use purely qualitative language (“in line with Planck ΛCDM within 1σ”) unless you provide the necessary reference values and arithmetic. As written, “0.3σ” is a quantitatively uncheckable claim.

---

P1B-N4  
Section: Sec. IV, NaMaster pipeline results; Sec. VII Conclusions; Table III  
Pages: 5–6, 7–8, 10  

**New issue (A/E: arithmetic & σ comparability):**  
The pipeline “SNR = 20.32” and “SNR = 25.71” are given without any definition in terms of β̂ and σ(β̂), and no scatter σ(β̂) over the 500 realizations is provided. This was already flagged as P1B-E7, but there is an *additional* comparability problem: in the Conclusions and Table III, β̂NaMaster = 0.238° is labeled as “Verified” without reiterating that the very high “SNR” values are MC‑pipeline metrics, not sky-detection significances, while the same page also cites the “published 3.6σ” sky detection. The abstract and Sec. IV body do contain some warnings, but the juxtaposition in the Conclusions and in Table III is unqualified: a non-expert reader could easily misinterpret the 20–25 “SNR” as stronger evidence than the 2.4–3.6σ sky measurements.  

**Required fix:**  
Augment the Conclusions paragraph and Table III to explicitly annotate the NaMaster SNR values as *MC pipeline-recovery SNR, not sky detection σ*, and avoid any sentence structure that puts “SNR = 20.32/25.71” and “3.6σ” side by side without an explicit “not comparable” disclaimer. This is distinct from P1B-E6, which focused on cosmological σ’s; here the issue is *pipeline* SNR vs sky detection significance.

---

P1B-N5  
Section: Sec. VI, ALP birefringence equations (2)–(3) and surrounding text  
Pages: 6–7  

**New issue (C/A: dimensional/numerical consistency):**  
Equation (3) states  
\[
\beta \approx \frac{\alpha_{\rm EM}\, C_{a\gamma}}{4\pi} \times 1.07 \approx 0.29^\circ,
\]  
with Caγ = 8, θi = 1, m ≈ 2H0 and earlier “∆ϕ/fa ≈ 0.65 (m = H0, θi = 1)” and later “∆ϕ/fa ∈ [0.2, 1.1].” There are *three* different effective values for ∆ϕ/fa implicitly in play: 0.65, the unspecified “1.07” in Eq. (3), and “≈1.0” (“fiducial value … corresponds to the midpoint … ∆ϕ/fa ≈ 1.0”). This is more than just missing derivation (your P1B-E8): the numbers are internally inconsistent even at the order-of-10% level:  
- Using ∆ϕ/fa = 0.65 in radians with Caγ = 8 gives β ≈ (αEM/4π) × (8 × 0.65) ≈ 0.17°, not 0.29°.  
- Using the stated 1.07 in Eq. (3) gives ∆ϕ/fa ≈ 1.07, but this value is never connected to the ODE solution in Eq. (2), and it already lies at the *upper* end of the numerically quoted [0.2, 1.1] range.  
- The text then asserts that the fiducial β ≈ 0.27° “corresponds to … ∆ϕ/fa ≈ 1.0,” which again mismatches the 1.07 used in Eq. (3).  

**Required fix:**  
Provide a single, self-consistent chain of numbers: (i) clearly state the ∆ϕ/fa used to obtain β ≈ 0.29°, (ii) show that this value arises from the ODE integration for the chosen (m/H0, θi), and (iii) ensure that Eq. (2), the [0.2,1.1] range, the 1.07 factor, and the “≈1.0” midpoint all agree numerically to within rounding. If you intend ∆ϕ/fa = 1.07 for the fiducial point, then Eq. (2) should not quote 0.65 for θi = 1, or you must explain that 0.65 corresponds to a different parameter choice. Right now, the internal arithmetic among 0.65, 1.0, 1.07, and 0.29° is opaque and inconsistent.

---

P1B-N6  
Section: Sec. VI, “Backreaction disclosure” (footnote 4 and footnote 5); Sec. VI body  
Pages: 6–7, 9  

**New issue (A/H: arithmetic & quantified tuning):**  
Footnote 4 states that moving θi from 0.5 (scan midpoint) to 0.1 (spectator-consistent corner) corresponds to “Ωa(0.1)/Ωa(0.5) ∼ 1/25 (i.e., a ∼ 25× fine-tuning of the misalignment initial condition).” Since ρa ∝ θi², the ratio is (0.1/0.5)² = (0.2)² = 0.04, i.e. 1/25, which is fine. But the *text* in Sec. VI repeatedly refers to a “∼25× misalignment tuning … relative to the natural prior midpoint values,” while the numerical scan range is θi ∈ [0.5, 2]. If 0.5 is the “prior midpoint,” then “tuning” θi down to 0.1 indeed involves a factor of 5 in θi (and 25 in θi²), but if “natural prior midpoint” is interpreted as O(1) (i.e., θi ∼ 1), then the corresponding reduction in θi² is 100×, not 25×. The manuscript uses “∼25×” throughout without clearly specifying whether the tuning is defined in θi or in θi², and relative to which “midpoint” (0.5 or 1.0).  

**Required fix:**  
Define precisely what “25× tuning” refers to:  
- If it is tuning in θi (angle) itself, then the factor is 5× (0.5 → 0.1), not 25×.  
- If it is tuning in energy density (θi²), then 25× is correct for 0.5 → 0.1, but the text should say so explicitly (“25× reduction in ρa ∝ θi²”), and you should not refer to “θi ∼ 1” as the midpoint in the same breath.  
Pick one reference point and state it clearly; otherwise the numerical meaning of “25× tuning” is ambiguous and cannot be audited from the text.

---

P1B-N7  
Section: Sec. VI, “Summary-likelihood combination (auxiliary cross-check)”  
Page: 7  

**New issue (A: arithmetic check of inverse-variance combination):**  
The combined value βcombined = 0.241° ± 0.061° from β1 = 0.30° ± 0.11° and β2 = 0.215° ± 0.074° is numerically correct if you assume statistically independent Gaussians:  
- w1 = 1/0.11² ≈ 82.64, w2 = 1/0.074² ≈ 182.7  
- βcombined ≈ (w1β1 + w2β2)/(w1 + w2) ≈ 0.242°  
- σcombined ≈ 1/√(w1 + w2) ≈ 0.061°.  

However, the text then describes this as a 3.9σ detection. Using 0.241/0.061 ≈ 3.95, this is internally consistent *arithmetically* but not with the earlier caution about shared calibration systematics (“This neglects shared calibration systematics; the published joint analysis at 3.6σ [2] is the headline.”). You are effectively presenting a *stronger* detection (3.9σ) from a naive combination than the “headline” joint analysis (3.6σ) without quantifying the size of the bias such shared systematics would introduce.  

**Required fix:**  
Clarify that the 3.9σ is the *formal* significance under the unrealistic assumption of independent errors and that, in practice, the presence of shared systematics reduces this to the published 3.6σ. Explicitly state that the 3.9σ value is not physically meaningful and is shown only as an algebraic check, not as evidence. As written, the arithmetic is correct, but the statistical interpretation is misleadingly stronger than the properly calibrated 3.6σ.

---

P1B-N8  
Section: Abstract vs body (faithfulness of NaMaster result and ALP “consistency”)  
Pages: 1–2, 5–7  

**New issue (F/H: abstract faithfulness / hedged language):**  
The abstract states: “Injecting the spectator-ALP fiducial value β = 0.27° recovers β̂ = 0.238° (pipeline-recovery bias 0.032°).” In the body (Sec. IV), the corresponding passage clarifies that the bias is 0.032° for β = 0.27°, but 0.040° for β = 0.342°, and that the bias has a “∼12% amplitude-dependent component.” This amplitude dependence is not mentioned in the abstract, which presents “0.032°” as *the* pipeline bias. Given that the paper positions itself as a “technical verification companion,” this omission is non-trivial: an amplitude dependence at the 10% level in the bias is part of the core finding and its limitations.  

Similarly, the abstract says, “a field with fa ∼ MPl, m ∼ H0 is consistent with the published joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ),” with only a brief “spectator-status caveat.” The body later reveals that this requires (i) Caγ ∆ϕ/fa ≈ 10.3, (ii) Caγ in the ∼9–51 range, and (iii) ∼25× misalignment tuning for spectator status. None of these quantitative qualifications appear in the abstract. The abstract thus overstates “consistency” without disclosing the degree of tuning or the fact that the required coupling range lies well outside minimal KSVZ/DFSZ benchmarks.  

**Required fix:**  
Revise the abstract to:  
- Mention that the NaMaster bias is 0.032–0.040° and mildly amplitude‑dependent (worst-case 0.040° at β = 0.342°), rather than a single fixed value.  
- Qualify the ALP “consistency” claim by indicating that it requires O(10–50) photon couplings and ∼25× misalignment tuning for spectator status. A brief phrase such as “consistent but requires O(10–50) photon couplings and tuned misalignment” would make the abstract numerically faithful to the body.

---

P1B-N9  
Section: Appendix A vs main text (reproducibility of DESI+DES-SN+Planck+Pantheon+ chain)  
Pages: 7–8, 8  

**New issue (I: appendix vs main-text mismatch):**  
Sec. VII (“Forward”) describes a DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR quintom chain (128,385 samples, χ² decomposition in Table II) and frames this as an *available* test of the quintom-B scenario. Appendix A (Reproducibility Materials) lists the public repository contents but does not provide any configuration, YAML file, or data product corresponding to this specific DESI DR2 + DES-SN5YR + Planck + Pantheon+ quintom run—the YAMLs described there are only for ΛCDM+∆Neff on four dataset combinations, not for the w0–wa extension with DESI DR2 and DES-SN5YR used in Table II. This is a new inconsistency between the claimed availability in the main text and the actual contents listed in the appendix.  

**Required fix:**  
Either (i) add the DESI DR2 + DES-SN5YR + Planck + Pantheon+ w0–wa YAML configuration and any necessary data files to the repository and reference them explicitly in Appendix A; or (ii) clearly state in Appendix A that the Table II chain configuration is not yet included and will be provided in a future update, adjusting the main-text language accordingly (e.g., “will be made available” rather than “are available”).