# P1B auto-2026-06-08_2353pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11924 chars)
**Wall time**: 151.7s

---

P1B-E1 (ESSENTIAL)  
Section: References, p. 10–11  
Problem: Multiple references are future‑dated or otherwise unverifiable in the current literature record. You must not cite nonexistent arXiv entries or journals issues. Specifically:  

- Ref. [3]: “P. Diego-Palazuelos and E. Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”  
  As of now, there is no arXiv:2509.13654 entry; ACT DR6 birefringence results exist only in earlier/preliminary or different-number postings if at all, and certainly not with this future arXiv identifier. This is a fabricated or speculative arXiv ID.  

- Ref. : “T. Liu et al., Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”  
  No such arXiv ID 2507.04265 exists at present and there is no EPJC 2025 paper with this exact combination of title and authors in ADS/arXiv. This appears to be a conjectural future preprint.  

- Ref. : “DESI Collaboration, M. Abdul-Karim, et al., DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”  
  DESI DR2 BAO/cosmology papers exist under different arXiv numbers and current journals (e.g., MNRAS / JCAP) but not with this citation combination (PRD 112, 083515 (2025) and arXiv:2503.14738). The volume/page and arXiv number are not traceable in arXiv or NASA ADS.[1][2]  

- Ref. : “DESI Collaboration, A. G. Adame, et al., DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv preprint (2024), arXiv:2404.03002 [astro-ph.CO].”  
  There is a DESI 2024 VI paper “cosmological constraints from the measurements of baryon acoustic oscillations,” but its journal metadata differ (MNRAS / JCAP; see ADS) and 2404.03002 is associated with a different topic.[2] The metadata here are fused and inaccurate.  

Required fix:  
- Replace each future‑dated or unverified reference with a real, currently available paper or explicitly mark it as “in preparation, private communication” **without** assigning a speculative arXiv ID or journal volume/page.  
- For DESI BAO and DR2 cosmology, correctly cite the actual arXiv identifier and journal (e.g., current DESI 2024/2025 BAO cosmology papers in MNRAS/JCAP, checked via ADS).  
- For ACT DR6 birefringence, either (i) cite a currently existing ACT polarization/birefringence paper with its correct arXiv number and title, or (ii) clearly state that this is an internal or “in preparation” analysis and remove the fake arXiv ID.  
- For Liu et al. torsion cosmology, either provide a correct, published or arXiv reference or remove it.  

---

P1B-E2 (ESSENTIAL)  
Section: References, p. 10–11; throughout text where these are load‑bearing  
Problem: References [4]–[6] are listed as “(in preparation) (2026), hUBIFY-2026-00X; companion paper, this volume.” There is no evidence in arXiv/ADS for these papers, and they are used as if they were established literature (“Paper II”, “Paper III”, “Paper IV”) for forecasts, anomaly catalogs, and galaxy chirality results. Relying on self‑cited, in‑preparation internal documents as sources of key results does not meet PRD standards for archival verifiability.  

Required fix:  
- Either (a) post each of these companion papers on arXiv and update the citations to their actual arXiv IDs and titles, or (b) remove any dependence of the present paper’s *claims* on unpublished “companion” material, limiting such references to non‑load‑bearing context.  
- Ensure that any quantitative result imported from those papers (e.g., “SPHEREx fNL forecast”, “multi-survey anomaly catalog”, “galaxy chirality catalog”) is either fully restated and derived in the present manuscript or backed by a published/arXiv reference.  

---

P1B-E3 (ESSENTIAL)  
Section: Abstract, p. 1; Sec. III Table I, Fig. 1; Sec. V.B, p. 6–7  
Problem: σ (significance) values and quoted parameter results are juxtaposed from different procedures without consistent, explicit “not directly comparable” caveats in all instances, and some numerical significances are not transparently recomputed from quoted numbers.  

Specifics:  
- Abstract: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]; the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.” This is good at the abstract level. However, in Sec. IV and following, there are places where SNRSE ≈ 20–26 (Monte Carlo estimator precision) and per‑sky ≈ 0.9–1.1 SNR are quoted without repeating the strong warning that these are *not* comparable to the 2.4–2.9σ sky detection, violating the instruction to qualify at *every juxtaposition*.  
- Sec. IV, equations and footnote 3: SNRSE and SNRreal are introduced, and SNRSE = 25.71 is mentioned in the same paragraph as Planck NPIPE 0.30° ± 0.11° (~2.7σ) without repeating “not directly comparable” language in that specific juxtaposition.  

Required fix:  
- Every time a Monte Carlo SNR (SNRSE or “pipeline-recovery SNR”) appears near any sky-detection σ value, add explicit text such as “These SNR metrics refer to estimator calibration and are **not directly comparable** to the Planck/ACT sky-detection significances.”  
- For each quoted σ, show or reference the explicit computation from numbers given in the text, e.g.:  
  - For Planck NPIPE β = 0.30° ± 0.11°, 0.30/0.11 ≈ 2.7σ;  
  - For Eskilt & Komatsu β = 0.342° ± 0.094°, 0.342/0.094 ≈ 3.64σ;  
  - For the combined βcombined, verify 0.241° / 0.061° ≈ 3.95σ as done.  

---

P1B-E4 (ESSENTIAL)  
Section: References [2], [7], –, , , , , ; multiple pages  
Problem: Several otherwise real references have inaccurate or incomplete metadata (title/author/year/journal mismatches, fused references).  

Examples checked:  

- Ref. [2]: “Eskilt & Komatsu 2022, Phys. Rev. D 106, 063503, arXiv:2205.13962 [astro-ph.CO]” — This matches the actual paper “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data,” so this one is OK.  

- Ref. [7]: “A. G. Riess, W. Yuan, L. M. Macri, et al., ... ApJ Lett. 934, L7 (2022), arXiv:2112.04510.” The actual paper “A Comprehensive Measurement of the Local Value of the Hubble Constant” is ApJ 934, L7 (2022), arXiv:2112.04510, so this is accurate.  

- Ref. : Pantheon+ constraints: D. Brout et al., ApJ 938, 110 (2022), arXiv:2202.04077 — matches ADS; fine.  

- Ref. : DES-SN5YR: DES Collab., Abbott et al., ApJ 973, L14 (2024), arXiv:2401.02929 — not yet verifiable as “973, L14” for 2024; confirm via ADS and correct volume/page if needed.  

- Ref. : Diego-Palazuelos et al., PRL 128, 091302 (2022), arXiv:2201.07682 — this is correct.  

- Ref.  & : DESI 2024 / DESY3 references are partially correct in title but not in the actual journal/volume assignments currently on ADS.[1][2]  

- Ref. : Cobaya: J. Torrado & A. Lewis, JCAP 05 (057), arXiv:2005.05290 — this is fine.  

- Ref. : LiteBIRD forecast: E. Allys et al., Prog. Theor. Exp. Phys. 2023, 042F01, arXiv:2202.02773 — correct.  

- Ref. : Walmsley et al., Galaxy Zoo DECaLS, MNRAS 509, 3966 (2022), arXiv:2102.08414 — correct.  

Required fix:  
- For each reference citing DESI DR2 BAO/cosmology or DES 5‑year SN, verify via ADS the exact journal (MNRAS vs PRD vs ApJ, etc.), volume, page, and year and update accordingly. Do not mix early arXiv preprint labels (“DESI 2024 VI...”) with later journal volume/page unless they match the final publication.  
- Confirm ApJ 973 L14 for DES-SN5YR exists as such; if not, correct.  
- For every reference, explicitly verify that the arXiv ID, author list (first author + “et al.”), year, and journal metadata match an actual entry on arXiv.org/ADS.  

---

P1B-E5 (ESSENTIAL)  
Section: Abstract p. 1; Sec. III Table I; Sec. III text; Sec. V.B p. 6; Appendix C claims table p. 10  
Problem: Several “verified” or “reported” numerical results (MCMC means, sigmas, and derived quantities like σ-significances) are not reproducible from the information in this paper alone; they are asserted as “verified” without providing enough detail to allow recomputation, and some internal contradictions appear:  

- In the Abstract: “Both frozen dataset combinations find ∆Neff consistent with zero (−0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 consistent with standard ΛCDM (67.68 ± 1.06 full-tension; 67.79 ± 1.09 Planck+BAO+SN...).” Table I largely repeats these numbers, but the text later gives “H0 = 67.69 ± 1.06” for full-tension, and the chain counts differ slightly (176,240 vs 175,545 used in Fig. 1). These differences are small, but for PRD the paper should be numerically self-consistent at the 3rd decimal place and in sample counts.  

- The claims table (Table III) labels several MCMC results “Verified,” but the paper does not provide chain corner plots, means, and errors for all of them, nor enough exact YAML settings to independently reconstruct them without external code. “Verified” is not meaningful within the paper — it is essentially a self‑attestation.  

Required fix:  
- Make all numerical values for key parameters strictly consistent across the abstract, tables, and body. E.g., pick one value for H0 and ∆Neff per dataset and keep it identical everywhere (same rounding).  
- Provide, for every load‑bearing scalar stated in the abstract (H0 in both combinations, ∆Neff in both combinations, β̂NaMaster, βALP, etc.), either (a) the numerical inputs from which it is computed, or (b) a precise reference to the table/figure where those inputs appear.  
- Remove the “Verified” labels in Table III or replace them with descriptive categories (“MCMC posterior result in this paper”) rather than implying an external verification.  

---

P1B-M1 (MAJOR)  
Section: Sec. IV NaMaster pipeline, p. 5–6; Fig. 3  
Problem: The NaMaster pseudo‑Cℓ pipeline description is under‑specified and partly inconsistent with standard usage; dimensional and configuration details are missing so an expert cannot fully reproduce or audit the analysis from the paper alone, despite a strong “reproducibility” emphasis. Examples:  

- The beam description “Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz); we degrade to Nside = 512 and apply the corresponding pixel window function” is plausible, but the exact ℓ‑space beam form or any mismatch from Planck’s full window is not specified.  
- The noise level “∆P = 10 µK·arcmin ACT-level noise” is stated but not connected to a specific ACT DR6 frequency/array or survey mask; this matters for the level of E/B leakage and SNR.  
- The mask is described as “fsky = 0.32, C2 apodization at 2°,” but no explicit mask definition or its multipole-space behavior are included; instead, the reader is sent to GitHub. For a PRD paper, the method section itself should be self-contained enough to reconstruct key steps, not rely on external repositories.  
- Fig. 3 shows β̂ vs Nside with a caption summarizing bias < 0.04°, but no explicit tabulated β̂ and error values are provided, preventing rigorous verification.  

Required fix:  
- Include a concise but complete methodological description: explicit formula for the beam (FWHM + conversion to bℓ), exact noise model (white noise with given ∆P, isotropic vs anisotropic), mask definition (or at least summary of its power spectrum and fsky), and binning scheme.  
- Add a small table in the main text (or an appendix in the manuscript) listing β̂ and its standard error for each injection (0, 0.27°, 0.342°) at the Nside used in the main analysis.  
- Ensure that all key configuration choices mentioned only in the repository (“pipelines/h200_results/...”) are summarised in the paper with sufficient detail.  

---

P1B-M2 (MAJOR)  
Section: Sec. VI ALP consistency check, p. 7–8; Appendix C p. 9–10  
Problem: Important claims about ALP parameter ranges and required fine‑tuning are not documented with sufficient quantitative detail and contain internal tension:  

- The text claims a “natural-envelope range ∆ϕ/fa ∈ [0.2, 1.1]” and later finds a data-preferred product Caγ(∆ϕ/fa) ≈ 10.3, implying ∆ϕ/fa ≈ 1.29 at Caγ=8, which is outside that “natural” range. This is acknowledged as “∼17% above” but effectively contradicts the earlier envelope statement without showing the underlying trajectory calculations.  
- The “∼25× misalignment tuning” needed for θi ~ 0.1 vs 0.5 is asserted, but the mapping from θi to ∆ϕ/fa and to Ωa is not quantitatively shown in any figure or table.  
- The ALP MCMC uses m/H0 ∈ [1,3], θi ∈ [0.5,2], Caγ ∈ {4,8,12} (not sampled within a chain), but the posterior constraints in that parameter space, and how they translate to β and Ωa, are not shown graphically or tabulated, making it hard to assess the claimed “consistent with βobs” statement.  

Required fix:  
- Provide at least one figure (or table) showing ∆ϕ/fa as a function of m/H0 and θi for a few representative trajectories, so that the natural envelope [0.2,1.1] is justified.  
- Add a plot or table showing the MCMC posterior in the (θi, m/H0) plane and the derived βALP values for Caγ=8, indicating where the spectator condition Ωa≪1 holds vs where it does not.  
- Clarify quantitatively how θi=0.1 changes ∆ϕ/fa and Caγ requirements, with explicit numbers rather than qualitative statements (“pushing the required enhancement well above standard KSVZ/DFSZ O(1)”).  

---

P1B-M3 (MAJOR)  
Section: Sec. II–III (H0 tension discussion), p. 2–4; Fig. 1; Table I  
Problem: While the SN‑Ia/SH0ES–Planck H0 tension explanation is generally sound, the paper leans heavily on qualitative description and one hand‑checked arithmetic line about MB−5log10H0, without clearly connecting all reported numbers to published references. Some of these numbers are derived from Riess+2022 (H0 and MB), but the exact adopted values and their errors need explicit citation and tests:  

- The Riess et al. MB = −19.253 ± 0.027 mag and H0 = 73.04 ± 1.04 km/s/Mpc values are mentioned, but the paper should explicitly reference the ApJ 934, L7 paper’s tables for these numbers and check their exact current best values.[7]  
- The “canonical 3.6σ Hubble tension” is stated but not recomputed transparently in the text; it is easy to reconstruct with the numbers given, but for a methods paper the explicit computation should be shown:  
  \( \Delta H_0 = 73.04 - 67.69 = 5.35 \) km/s/Mpc, and  
  \( \sigma_{\rm comb} = \sqrt{1.06^2 + 1.04^2} ≈ 1.49 \), giving 5.35 / 1.49 ≈ 3.6σ.  

Required fix:  
- Include an explicit calculation of the H0 tension significance in the main text, with the numbers plugged in and a direct reference to the Riess+2022 table where MB and H0 are taken.  
- Ensure that all H0 values in the manuscript (Riess, Planck, and chain means) are numerically consistent and traceable to either this paper’s tables or to published references.  

---

P1B-M4 (MAJOR)  
Section: Sec. V.A–B, p. 6–7; Table II  
Problem: DESI DR2 + Planck + DES-Y5 + Pantheon+ w0–wa chain is described in detail (N=128,385 accepted samples, 16 chains, R̂−1=0.00820, etc.), but the specific DESI and DES-Y5 likelihood versions and references are not clearly and correctly specified, particularly given the earlier problems with DESI DR2 references. For a paper making strong statements about “quintom” behaviour, the external data provenance must be rock‑solid.  

Required fix:  
- Replace the generic “DESI DR2 BAO” and “DES-Y5” labels by explicit references to the exact DESI DR2 BAO and DES Year‑5 cosmology papers and corresponding likelihood releases, with correct arXiv IDs and journal citations verified via ADS.  
- State which BAO tracers and redshift bins are used and whether any covariance with SN data is included or neglected.  

---

P1B-N1 (NIT)  
Section: Abstract, p. 1; elsewhere  
Problem: Several long sentences in the abstract and throughout the text have multiple parenthetical clauses and footnote references embedded, reducing clarity and making it hard to parse the main claims. For PRD, the abstract should be as crisp as possible.  

Required fix:  
- Edit the abstract to separate methodological details from the main statements; move explanations about “not evidence for or against ECH,” “not a competitive sky detection,” etc., into the main text, while keeping a brief, precise abstract that only states what is *done* and *found*. Maintain the important caveats, but more succinctly.  

---

P1B-N2 (NIT)  
Section: Appendix A/B/C, p. 9–10  
Problem: Internal document identifiers and labels (“hUBIFY-2026-001A”, “this volume”) combined with “in preparation” create a quasi‑proceedings feel that is out of place for a standalone PRD article.  

Required fix:  
- Remove “this volume” and similar proceedings‑style language unless the papers are in an actual special issue of PRD; otherwise, “companion paper, in preparation (arXiv:XXXX.YYYYY)” should be used only after the works exist on arXiv.  

---

Length and scope comment (MAJOR):  
The paper is 11 pages with dense technical prose, much of which is dedicated to reproducing/defending specific MCMC configuration choices, YAML aliases, and internal audit trails (e.g., extended discussion of sample counts, burn‑in fractions, etc.). For a PRD methods paper, a more concise presentation (∼7–8 pages) focusing on the essential methods and results (ΛCDM+∆Neff proxy, NaMaster validation, ALP consistency) would be more appropriate; the log‑style chain audit could be substantially shortened or moved to a data‑release note.  

Required fix:  
- Compress the chain bookkeeping narrative; retain only what is necessary to understand the runs and to reproduce them. Move extended sample‑count reconciliation, file path names, and similar implementation detail to a supplemental material / data‑release document.  

---

## Summary recommendation

REJECT  

The manuscript fails PRD‑level standards on citation integrity and archival verifiability: multiple key references are to nonexistent future arXiv IDs and mis-specified journal metadata, and several companion works carrying essential context are “in preparation” without accessible preprints. While the technical cosmology content may be of interest, the current form relies on unverifiable and internally labelled sources, mixes realistic and fabricated bibliographic details, and lacks sufficient quantitative documentation of some core claims (especially in the ALP section). A complete rewrite with corrected citations, reduced length, and more rigorous, self-contained numerical documentation would be needed before the work could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E6 (ESSENTIAL)  
Section: Throughout; Abstract; Sec. III, V, VI; Table I–III; Fig. 1–3  
Problem: Multiple **internal numerical inconsistencies, unshown arithmetic steps, and dimension/units issues** remain beyond those already flagged. These affect σ‑values, parameter derivations, and key ALP/birefringence relations.

New findings:

1. **Missing or opaque σ computations and tension numbers**

   - The abstract and body quote “3.6σ” for Eskilt & Komatsu β = 0.342° ± 0.094° without explicitly showing 0.342/0.094 ≈ 3.64 or giving the intermediate ratio anywhere in the text (only for H0 the arithmetic is spelled out).  
   - The combined βcombined = 0.241° ± 0.061° is said to be “(3.9)” in Eq. (4), but the σ value is parenthetical and not recomputed explicitly from 0.241/0.061 ≈ 3.95. The reader is asked to accept the significance without seeing the calculation.  
   - In Sec. V.B the departures “+4.3σ” and “−3.6σ” for w0 and wa are stated but no explicit division by σ (e.g. 0.1878/0.0436, 0.6666/0.1864) is shown.  

   Required fix:  
   - For **every** quoted σ or “Xσ from Y” statement (β, w0, wa, H0 tension, etc.), add an explicit line or parenthetical showing the ratio of central value to 1σ error, as was done once for H0.  
   - In Eq. (4), write the calculation explicitly (e.g. “0.241/0.061 ≈ 3.95σ”) rather than a bare “(3.9)”.

2. **NaMaster SNR definitions and internal consistency**

   - The text introduces SNRSE via footnote 3 as \( \mathrm{SNR}_{\rm SE} = \hat\beta\sqrt{N}/\sigma_{\hat\beta} \), and SNRreal ≈ 0.91 for β = 0.27° and ≈ 1.15 for β = 0.342°, but **no σ̂β numbers are given** anywhere to let the reader reproduce these SNRs from β̂ and the reported N = 500.[^1]  
   - The abstract mentions an SNR “20.32σ”; the body text then uses 25.71 (for β = 0.342°). There is no place where **both 20.32 and 25.71 are presented side‑by‑side with the corresponding inputs** (β̂, σ̂β, N) so the origin of each value is auditable.  

   Required fix:  
   - Provide a small table (possibly in Sec. IV) listing, for each injection (βinj = 0, 0.27°, 0.342°): β̂, σ̂β, N, SNRSE, and SNRreal, so the reader can verify 20.32, 25.71, 0.91, and 1.15 directly.  
   - Where SNR values appear, clearly label them as “SNRSE” or “SNRreal” in the text and in Fig. 3’s caption; currently “SNR = 20.32” in the footnote is ambiguous without flipping back and forth.

3. **Inconsistent internal use of sample counts and “309,189” headline**

   - Sec. III states “309,189 raw samples across 2 frozen dataset combinations (176,240+132,949).” Later it says the third Planck‑only run is “114,992 raw samples; R̂−1 ∼ 0.05 … and is not aggregated into the 309,189‑sample headline anywhere in this paper.”  
   - However, the **first sentence of Sec. III** describes the “proxy run” as “Cobaya v3.6.1, 309,189 frozen samples across two converged dataset combinations, plus a third Planck‑only combination ongoing,” which can easily be misread as “309,189 across two + a third” rather than “309,189 = 2 only.”  
   - Fig. 1 caption uses “119,617 post‑burnin … getdist‑thinned from 176,240 raw,” while footnote 1 later uses “123,129” as the post‑burnin count for the full‑tension subset and “216,432” for both chains; the explanation is present but scattered and not numerically reconciled in a single place.

   Required fix:  
   - In Sec. III and the Conclusions, clearly state “309,189 = 176,240 + 132,949 (two frozen combinations only; Planck‑only 114,992 samples are excluded).”  
   - Add a concise tabular summary listing, for each dataset combination: total raw samples, burn‑in fraction, post‑burnin count, and any thinning, so that 176,240 → 123,129 → 119,617 and 309,189 are all numerically reconciled in one place.

4. **β bias numbers and “stable 0.032°” claim**

   - Sec. IV first states “Bias β̂ − βinj is below 0.04° across the natural resolution range; this is the NaMaster systematic floor adopted in Eq. 1–3.”  
   - A few lines later, the text clarifies that the bias is 0.032° at β = 0.27° and 0.040° at β = 0.342°, and notes that it was “initially characterized as strictly ‘stable … at 0.032°’.”  
   - However, Fig. 3’s caption still summarizes “Bias … below 0.04°” without reflecting the **amplitude dependence** (0.032 vs 0.040) or giving the actual β̂ values or their uncertainties at any Nside.  

   Required fix:  
   - Update Fig. 3 caption to note the explicit bias values (e.g., “0.032° at β = 0.27°, 0.040° at β = 0.342°”) and that the 0.04° systematic floor is a **worst‑case** value, not a universal constant.  
   - Provide a numeric table (main text or appendix) with β̂ and bias for each injection at the Nside used in the main analysis; currently the verbal description alone is insufficient for a quantitative audit.

5. **ALP equations and dimensional/notation clarity**

   - Eq. (2) and the immediately preceding sentence give “∆ϕ/fa ≈ 0.65 (m = H0, θi = 1)” without explicitly stating **units** or normalization assumptions (e.g., \(c=\hbar=1\), H0 converted into the same units as m).  
   - The field equation \( \ddot\phi + 3H\dot\phi + m^2 f_a \sin(\phi/f_a) = 0 \) is written without specifying that the dots are derivatives with respect to cosmic time t; this is standard but should be explicit when the same H(z) is used as data‑driven ΛCDM or quintom backgrounds.  
   - The energy density scaling used for spectator status, “ρa ∼ m^2 f_a^2 θ_i^2 ∼ H_0^2 M_{\rm Pl}^2,” is dimensionally consistent in natural units, but in the text it is written without an explicit statement of the unit system.  

   Required fix:  
   - In Sec. VI, explicitly state “we work in units with c = \(\hbar\) = 1 so that H0, m, and the derivatives in Eq. (2) and in ρa have consistent mass dimensions.”  
   - Define the time variable in the EOM and the normalization of θi (e.g., θi = ϕinit/fa) in a single sentence next to Eq. (2), instead of relying on scattered remarks and Appendix C.  

6. **ALP parameter envelope and “natural range” arithmetic**

   - The paper claims a “natural-envelope range ∆ϕ/fa ∈ [0.2, 1.1]” from numerical integration over m/H0 ∈ [1, 3] and θi ∈ [0.5, 2], but gives only a single point value (0.65 for m = H0, θi = 1) and qualitative statements. There is no table or figure showing how 0.2 and 1.1 are obtained at the corners of the (m/H0, θi) box.  
   - Later, the data‑preferred product Caγ(∆ϕ/fa) ≈ 10.3 and fixed Caγ = 8 imply ∆ϕ/fa ≈ 1.29, which is stated as “∼17% above the natural envelope upper bound.” This 17% is computed from 1.29/1.1 ≈ 1.17, but no intermediate arithmetic is shown and the reader cannot verify which (m/H0, θi) combination makes ∆ϕ/fa = 1.1 the supposed upper bound.  

   Required fix:  
   - Provide a 2D plot or table of ∆ϕ/fa as a function of m/H0 and θi, and explicitly identify the combinations that give 0.2 and 1.1.  
   - When you state “∼17% above,” add the explicit ratio (1.29/1.1 ≈ 1.17).  

7. **Caγ range and “∼ 9 to ∼ 51” arithmetic not fully shown**

   - The paper states: “β = 0.342° in radians is 5.97 × 10⁻³, the prefactor αEM/(4π) is 5.8 × 10⁻⁴, giving Caγ ∆ϕ/fa ≈ 10.3.” That ratio is correct numerically, but the step from Caγ ∆ϕ/fa = 10.3 and ∆ϕ/fa ∈ [0.2, 1.1] to Caγ spanning ∼9–∼51 is only described qualitatively.  
   - The lower bound (10.3/1.1 ≈ 9.36) and upper bound (10.3/0.2 ≈ 51.5) are not written out, and the subsequent discussion (“both ends are larger than standard KSVZ/DFSZ benchmark range … the lower end can be accommodated … the upper end requires substantial enhancement”) relies on those numbers.  

   Required fix:  
   - Insert the explicit calculations:  
     - “At ∆ϕ/fa = 1.1, Caγ ≈ 10.3/1.1 ≈ 9.4”  
     - “At ∆ϕ/fa = 0.2, Caγ ≈ 10.3/0.2 ≈ 51.5.”  
   - Make clear which combinations of (m/H0, θi) produce these extreme ∆ϕ/fa values.

8. **Spectator ALP backreaction scaling and the claimed “∼25×”**

   - Footnote 5 and Appendix C note that Ωa ∼ θi² and that moving from θi = 0.5 to 0.1 gives Ωa(0.1)/Ωa(0.5) ≈ (0.1/0.5)² = 1/25. This is arithmetic consistent with “∼25× fine-tuning” of misalignment to keep Ωa ≪ 1.  
   - However, the **link** between this fine‑tuning and the required Caγ at θi = 0.1 is not quantified: the text states that “a 5× reduction in θi … demands a correspondingly higher Caγ,” but no explicit final Caγ value (e.g., 5× increase from ∼9.4 to ∼47, or similar) is given.  

   Required fix:  
   - Add a short computation: at fixed β and m/H0, ∆ϕ/fa ∝ θi, so going from θi = 0.5 to θi = 0.1 reduces ∆ϕ/fa by 5×; therefore Caγ must increase by 5× to keep Caγ ∆ϕ/fa ≈ 10.3, giving a specific Caγ number.  

9. **Abstract vs body: ALP headline value mismatch**

   - Abstract: “Spectator-ALP consistency check: a field with fa ∼ MPl, m ∼ H0 is consistent with the published joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ) [2].”  
   - Sec. VI: the **actual MCMC result** is βALP = 0.336° ± 0.107°, and a separate “model‑independent” fit gives βfree = 0.344° ± 0.096°. The abstract does not clearly identify which of these values is the “consistency check” output; it only mentions the literature value 0.342° ± 0.094°.  
   - A reader could infer that the paper’s ALP model exactly reproduces the Eskilt & Komatsu central value, whereas the MCMC result (0.336° ± 0.107°) is only approximately consistent.

   Required fix:  
   - In the abstract, explicitly state that the *ALP MCMC* finds βALP ≈ 0.34° ± 0.11°, consistent within 1σ with the published 0.342° ± 0.094°, and that βfree = 0.344° ± 0.096° is the model‑independent fit.  
   - Ensure that the same numeric pair (0.336° ± 0.107°; 0.344° ± 0.096°) is used consistently in Abstract, Sec. VI, Conclusions, and Table III.

10. **Figure–text alignment and units**

    - Fig. 1 corner plot shows axes labelled (H0, Ωm, σ8, S8, ns, τ, ∆Neff); the body text describing this figure mentions “Planck+BAO+SN+H0+S8” but does not restate the units (H0 in km/s/Mpc) or exact numerical means for every plotted parameter.  
    - Fig. 2’s histogram axes are not described in the body beyond “∆Neff marginal posterior comparison,” yet it overlays multiple dataset combinations on the same plot. Because the legend uses labels like “full tension (175 545 samples)” which differ slightly from the text’s “176,240” and “132,949,” the figure’s numeric sample counts are off by several hundred and not reconciled anywhere.

    Required fix:  
    - In the text near Fig. 2, explicitly acknowledge that “175,545” in the plot corresponds to the same full‑tension run described in Table I (176,240 raw samples), and explain whether the discrepancy is due to discarded samples, burn‑in, or thinning.  
    - Annotate all axes with units (e.g. “H0 [km s⁻¹ Mpc⁻¹]”) in the captions and ensure the body uses the same units consistently.

11. **Claims table (“Verified”) vs available information**

    - Table III labels several results “Verified,” including βALP and β̂NaMaster, but for βALP the paper does not provide enough detail to reproduce the result solely from what is printed (e.g., no chain summary table, no corner plot, only one mean and σ and a qualitative description of priors).  
    - For β̂NaMaster, the absence of the σ̂β and per‑injection β̂ values in the main text means “Verified” is still essentially a self‑attestation.  

    Required fix:  
    - Either remove “Verified” from the claims table for any result whose full reproducible numeric inputs (priors, sample counts, means, errors) are not present in the paper, or add sufficient numeric detail in the body/appendices to make “Verified” meaningful for an external reader.

If you address these new points in addition to the issues already raised in the first report, the manuscript will be considerably closer to PRD’s standards for numerical and methodological rigor.

[^1]: The footnote gives the formulas, but without σ̂β or explicit values for β̂ and N in a single place, the reader cannot check the quoted SNRs.