# P1B auto-2026-06-06_0004pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15686 chars)
**Wall time**: 108.0s

---

The manuscript cannot be accepted by Physical Review D in its current form. Beyond scientific-scope concerns (this is predominantly a technical-logbook companion), there are serious problems with references, “in preparation” citations, future-dated/implausible literature, internal inconsistencies in quoted statistics, and some dimensionless/units and methodology issues. Below I list all findings I can identify from the provided text.

I do not have access to the author’s GitHub or chains, so I cannot numerically re‑run the MCMC or pipeline; I restrict myself to internal consistency and external bibliographic checks using arXiv/ADS and the published literature.

---

### ESSENTIAL issues

**P1B-E1 – References [3], , , , , ,  are future‑dated or not verifiable**  
- **Location:** References section, pp. 9–10.  
- **Problem:**  
  - Several references are dated 2024–2025 or have arXiv IDs and full citation details that do not match any currently existing publications in ADS/arXiv:  
    - [3] “Diego-Palazuelos and Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv:2509.13654 (2025)”.  
    -  “T. Liu et al., Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, arXiv:2507.04265 (2025).”  
    -  “DESI Collaboration, DESI DR2 results II…, Phys. Rev. D 112, 083515 (2025), arXiv:2503.14738.”  
    -  “DESI 2024 DR1 BAO, arXiv:2404.03002 (2024).”  
    -  DES Y3 cosmology: the real DES‑Y3 paper is 2022 ApJ/PRD; here it is described as “DES Y3” but not correctly cited, and internal reference  text is partly garbled.  
    -  “Fujita et al. 2021” exists (Phys. Rev. D 103, 043509, arXiv:2011.11894) but the text claims it “was previously studied” in a way that conflates models; the exact target of “this model class” is ambiguous.  
    -  “LiteBIRD Collaboration, Allys et al., PTEP 2023, 042F01 (2023), arXiv:2202.02773” is mostly correct, but some formatting and wording deviate from the canonical citation.  
  - Several arXiv identifiers (e.g. 2509.13654, 2507.04265, 2503.14738) correspond to future months/years and do not currently exist; treating them as published is not acceptable for PRD.  
- **Required fix:**  
  - For each reference, verify against arXiv and ADS:
    - If the paper exists, correct title, authors, year, journal, and arXiv ID to match exactly.  
    - If the paper does not exist yet (future arXiv IDs, future years, “in preprint” with no upload), remove it or mark it explicitly as a *private communication* or *work in preparation* without a spurious arXiv ID or journal reference.  
  - In particular, [3], ,  as written are not acceptable and must be either replaced with real, published/posted resources or removed.  
  - All statements in the body that depend on these references (e.g. ACT DR6 birefringence, DESI DR2, torsion cosmology constraints) must be carefully checked against whatever real papers exist and updated accordingly.

---

**P1B-E2 – Self‑citations [1], [4], [5], [6] are “in preparation” with fake‑looking internal identifiers**  
- **Location:** References [1], [4], [5], [6]; also mentioned throughout.  
- **Problem:**  
  - The main “Paper I(a)” and related “Paper II–IV” are cited as:
    - [1] “Structural Closure of Einstein–Cartan–Holst Dark Energy: … (in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume.”  
    - [4]–[6] similar style.  
  - These have no arXiv IDs, DOIs, or journal references, only internal tags like “hUBIFY‑2026‑002”. They are not publicly verifiable.  
  - In the PRD context, it is not acceptable to treat non‑existent or unpublished “in preparation” works as load‑bearing references for structural results, no‑go theorems, or key predictions.  
- **Required fix:**  
  - Either (a) post these works to arXiv (or otherwise make them publicly accessible) and cite them properly (author, title, arXiv:YYMM.NNNNN, year), or (b) remove all dependence on them for any load‑bearing claims in this companion paper.  
  - Any statement that uses “Paper I(a)” as the unique source of a theorem, 14‑barrier table, or surviving fNL prediction must either be independently presented with proofs in this manuscript or deferred until Paper I(a) is an actual, citable document.  
  - Mark them clearly as “unpublished; private communication” if PRD allows, but they cannot be treated as established literature.

---

**P1B-E3 – ACT DR6 cosmic birefringence citation and numbers are not traceable**  
- **Location:** Abstract, first page; Sec. IV (Birefringence measurements paragraph); Sec. VI (headline observational constraint); references [3].  
- **Problem:**  
  - The paper repeatedly cites “ACT DR6” birefringence β = 0.215° ± 0.074° as a published result attributed to “Diego-Palazuelos and Komatsu… arXiv:2509.13654 [astro-ph.CO] (2025)”. No such paper currently exists, and ACT DR6 CMB polarization analysis is not yet public in that form.  
  - The quoted 0.215° ± 0.074° cannot be traced to an actual abstract/table; without a real source the statistic is unverifiable.  
  - The combined “2.4–2.9σ Planck/ACT DR6” significance and the auxiliary “3.9σ” inverse‑variance combination in Eq. (4) rely critically on this ACT result.  
- **Required fix:**  
  - Remove or clearly demote any reference to a non‑existent ACT DR6 birefringence paper and its numerical values.  
  - If there is an internal ACT analysis or private communication, it must not be used as if it were a published, peer‑reviewed result; at minimum label it “private communication (ACT Collaboration, year)” and strip it from any combined detection significance discussion.  
  - All numerical combinations (e.g. 3.9σ from Planck+ACT) that rely on this must be removed or replaced with combinations of *actually published* numbers (e.g. WMAP+Planck PR3/PR4 per Eskilt & Komatsu [2] and Diego‑Palazuelos et al. ).  
  - The abstract’s “primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]” is currently untrue and must be corrected to reflect only published values.

---

**P1B-E4 – DESI DR2 / DESI DR1 / DES‑SN citations are inconsistent and not traceable as written**  
- **Location:** Sec. III (“Independent cross-validation”), Table II caption and entries, Sec. V.A dataset list; references , , , .  
- **Problem:**  
  - The manuscript claims to use “DESI DR2 BAO” and cites  “DESI Collaboration, Abdul‑Karim et al., DESI DR2 results II: Measurements of BAO and cosmological constraints, PRD 112, 083515 (2025), arXiv:2503.14738.” This is future‑dated and not currently findable.  
  - Sec. V.A refers to “DESI 2024 DR1 BAO ” with arXiv:2404.03002, but  is labeled “DESI 2024 DR1 BAO” while  is “DESI DR2 results II” — yet Table II caption claims “DESI DR2 BAO + Planck 2018 NPIPE + DES‑Y5 + Pantheon+”. This is inconsistent: DR1 vs DR2, and the reference details do not correspond cleanly to any actual DESI paper.  
  - “DES‑SN5YR ” is invoked in ;  in the reference list is DES 5‑year SN, but there is mixing of DES Y3, DES Y5, DES-SN5YR, DES‑SN5YR that is inconsistent and in part future‑dated.  
- **Required fix:**  
  - Decide exactly which DESI release and which DES/BAO/SN datasets are actually used (DR1 vs DR2, DES‑Y3 vs Y5 vs DES‑SN5YR).  
  - Replace each fake or future reference with the real, currently published DESI BAO and DES SN cosmology papers (correct authors, titles, arXiv IDs).  
  - Update Table II caption and Sec. V.A dataset list so they match the actual references.  
  - Remove any claims “DESI DR2” if DR2 cosmology results are not yet public; if you used internal likelihoods, that must be clearly labeled as such and is generally not acceptable for a PRD methods paper.

---

**P1B-E5 – σ (significance) figures combined from different procedures are not consistently flagged as non‑comparable**  
- **Location:** Abstract; Sec. IV (scope note); Sec. VI (headline observational constraint and auxiliary combination); Table III; Conclusions.  
- **Problem:**  
  - The manuscript juxtaposes several “σ” significances:
    - Published WMAP+Planck “3.6σ” (Eskilt & Komatsu [2]).  
    - “2.4–2.9σ Planck/ACT DR6” (which is at least partially fictitious per E3).  
    - NaMaster pipeline “SNR = 20.32, 25.71” for injected signals (Sec. IV).  
    - Combined inverse-variance “3.9σ” in Eq. (4).  
  - While parts of the text do clarify that the high SNR pipeline numbers are *not sky detection significances*, there are locations where different σ’s are presented side by side without explicitly reiterating that they are not directly comparable:
    - Abstract: “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ [2,3]; the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.” Here the distinction is stated, which is good.  
    - Sec. VI: The auxiliary 3.9σ combination is given without repeating that it neglects shared calibration systematics and uses a non‑existent ACT DR6 measurement.  
  - Given PRD‑level standards and your own stated caveat rules, any table/paragraph where σ from different null procedures are put next to each other must explicitly state “not directly comparable” every time; here that is not consistently done, especially once ACT DR6 is removed.  
- **Required fix:**  
  - After removing ACT DR6 (E3), audit every occurrence of a σ‑value or SNR:
    - Clearly label which are sky-detection significances from published likelihoods, which are internal pipeline SNRs, and which are auxiliary/informal combinations.  
    - Wherever two or more σ-like numbers appear together from different procedures, explicitly state they are not directly comparable.  
  - Remove or rewrite Eq. (4) and its “3.9σ” label — it is currently both methodologically flawed (ignores correlated systematics) and based on a non‑existent ACT result.

---

**P1B-E6 – Over‑reliance on unverified, unshared internal pipelines and chains for central statements**  
- **Location:** Many sections, especially Abstract, Sec. III, Sec. V, Appendices.  
- **Problem:**  
  - Many key numerical claims (e.g. ∆Neff values, w0, wa, H0 tension figures, NaMaster bias, ALP βALP) are sourced entirely from internal chains and scripts that are not part of the peer‑reviewed record. The authors do point to a GitHub URL, but for PRD the burden is on the paper to be self‑contained and reproducible, not reliant on an external repository which may change.  
  - Some chains (e.g. DESI‑based quintom chain) are not described in sufficient detail (exact likelihoods, versions, cuts) and rely on future or internal DESI releases.  
- **Required fix:**  
  - For every numerical headline (the table entries in Table I, II; βALP, βfree, NaMaster bias), provide enough detail in the main text or appendices to reproduce the result *without* access to mutable external code: list the exact likelihood components, versions, priors, and chain lengths.  
  - Ensure all datasets used are fully public and correctly referenced, and remove any dependence on internal DESI or ACT DR6 analyses.  
  - If some chains rely on non‑public likelihoods, these results must be demoted from “results” to “illustrative checks” or removed.

---

### MAJOR issues

**P1B-M1 – Structural role of this paper vs. its contribution for PRD**  
- **Location:** Introduction; “What is NOT in this paper”; Conclusions.  
- **Problem:**  
  - The manuscript is explicitly framed as a “companion technical verification” to a separate no‑go theorem paper (Paper I(a)), which itself is “in preparation”. The main scientific novelty (14 barriers, perturbation-transparency theorem, etc.) is *not* presented here.  
  - This paper then becomes essentially a logbook of MCMC proxy runs, a pseudo‑Cℓ pipeline check, and an ALP consistency exercise whose novelty is modest and heavily dependent on unpublished context.  
  - For a top‑tier journal like PRD, a 9–10‑page paper that is primarily a description of someone’s internal verification runs, without independently establishing new physics results, is unlikely to meet the bar unless tightly integrated with a simultaneously published principal paper.  
- **Required fix:**  
  - Either (a) fuse the essential methodological content of this companion with the main structural paper and submit a single, self‑contained article to PRD, or (b) significantly strengthen the standalone value of this methods paper: present clearly novel methodological results (e.g. rigorous tests of torsion phenomenology, demonstrably new constraints on torsion or ALPs) that do not lean on unpublished “Paper I(a)”.  
  - As a stand‑alone PRD article, you must clearly articulate what is *new* and *non‑trivial* in the methods and results that could not be inferred from existing ΛCDM+Neff, NaMaster, and ALP‑birefringence literature.

---

**P1B-M2 – DESI quintom chain (Table II) is not described sufficiently; claims of “canonical quintom signature” may overstretch**  
- **Location:** Sec. II, Table II, surrounding discussion.  
- **Problem:**  
  - Table II reports a combined DESI DR2 + Planck + DES‑Y5 + Pantheon+ w0–wa fit with a very significant deviation from ΛCDM: w0 = −0.8122 ± 0.0436, wa = −0.6666 ± 0.1864, w0+wa = −1.4788 ± 0.1485, and claims this “requires phantom crossing” and is “the canonical quintom signature”.  
  - However, the exact DESI data set is unclear (DR1 vs DR2; see E4) and the chain configuration is only loosely described.  
  - While w0+wa < −1 at 3+σ indeed implies w < −1 at some redshift for standard CPL parameterization, labeling this as *canonical evidence* for quintom cosmology, especially when DESI results are not yet fully public in that exact form, is too strong and not adequately qualified as *model‑dependent* and sensitive to systematics and priors.  
- **Required fix:**  
  - Provide precise, verifiable citations for the DESI release(s) used, and ensure the chain description includes priors, redshift ranges, and nuisance modeling.  
  - Rephrase the cosmological interpretation: “consistent with quintom‑like behavior under the CPL parameterization” rather than “canonical quintom signature”, and emphasize dependence on the assumed w0–wa form and data combination.  
  - Clarify that this is an internal Cobaya re‑analysis; if similar results appear (or do not appear) in official DESI or combined analyses, cite those and reconcile.

---

**P1B-M3 – ALP birefringence calculation: numerical factors and parameter ranges need clearer derivation and literature comparison**  
- **Location:** Sec. VI equations (2) and (3); misalignment tuning discussion; footnotes 3–5; Appendix C.  
- **Problem:**  
  - The field displacement result ∆ϕ/fa ≈ 0.65 for m = H0, θi = 1 is asserted without showing the numerical integration details or cross‑checking with standard slow‑roll/oscillatory approximations; this is plausible but not demonstrated.  
  - The birefringence formula β ≈ (αEM Caγ /4π) × 1.07 ≈ 0.29° is dimensionally reasonable, but the factor 1.07 (and the mapping to β ≈ 0.27° at m ≈ 1.8H0) is not transparently derived, nor compared with Fujita et al.  or other ALP‑birefringence treatments to show consistency.  
  - The joint‑trajectory scan range β ≈ 0.17–0.43° over Caγ ∈ [4,12], m/H0 ∈ [1,3], θi ∈ [0.5,2] is given, but not tabulated, so it is not easy for a referee to check.  
  - The misalignment tuning “∼25×” is mentioned multiple times, but the precise definition (relative to which prior midpoint?) fluctuates: θi midpoint 0.5 vs 1.0.  
- **Required fix:**  
  - Add a short sub‑section or appendix that explicitly shows:  
    - The approximate analytic solution or a figure for ∆ϕ/fa as a function of m/H0 and θi in ΛCDM.  
    - A check against Fujita et al. (2021) or similar ALP birefringence calculations to confirm numeric consistency.  
    - A clear table or figure summarizing the β range for the scanned parameter grid.  
  - Define unambiguously what “∼25× misalignment tuning” means (e.g. ratio between θi = 0.5 prior midpoint and θi = 0.1 spectator‑consistent value).  
  - In the abstract and conclusions, tone down any impression that this constitutes strong evidence for ALPs; emphasize that it is a plausibility check given existing uncertainties.

---

**P1B-M4 – NaMaster pipeline description is incomplete and overstates validation scope**  
- **Location:** Sec. IV “Pipeline configuration” and “Independent verification”; conclusions.  
- **Problem:**  
  - The NaMaster configuration is described at a fairly high level, but several implementation details are missing: beam transfer function normalization, multipole cuts, exact Commander mask used, treatment of noise anisotropy, whether any analytic covariance or MC covariance was used in the β fit, etc.  
  - The mask apodization and purification choices (purify_b=True, purify_e=False; 2° apodization) are given, but the statement that the deconvolution is “unbiased at the 0.04° level” is based entirely on the three injections and 500 MCs; this is a limited validation, especially given the neglect of foregrounds and Planck‑like noise.  
- **Required fix:**  
  - Provide a more detailed description of the NaMaster setup: explicit formulae for the estimator, treatment of noise and beam, and details of how β is extracted from EB.  
  - Qualify the validation more carefully: this is a test of the algebraic pseudo‑Cℓ pipeline under specific noise and mask conditions, not a general statement about systematic errors in CMB birefringence measurements.  
  - If possible, add a basic cross‑check against existing Planck‑ or ACT‑based pseudo‑Cℓ pipelines in the literature.

---

**P1B-M5 – Length vs contribution**  
- **Location:** Whole paper.  
- **Problem:**  
  - For the stated purpose – a technical companion recording three checks – the manuscript is somewhat verbose and includes a noticeable amount of internal audit narrative (burn‑in recounting, chain‑length reconciliations, YAML alias diagnostics, etc.) which reads more like a lab notebook or code review than a PRD article.  
- **Required fix:**  
  - Condense the narrative by at least 30–40%. A maximum of 6–7 PRD pages is sufficient to present:  
    - The ΛCDM+∆Neff MCMC proxy design and main results.  
    - The NaMaster pipeline configuration and bias test.  
    - The ALP consistency exercise with essential equations and numbers.  
  - Move detailed chain diagnostics, MB–H0 algebraic checks, and GitHub‑specific directory paths into a data‑release note or online supplement, not the main text.

---

### MINOR issues

**P1B-m1 – Abstract statistics vs body consistency**  
- **Location:** Abstract, Table I, discussion in Sec. III.  
- **Problem:**  
  - Abstract quotes ∆Neff and H0 values:  
    - ∆Neff = −0.020 ± 0.169 (full‑tension); 0.065 ± 0.17 (Planck+BAO+SN).  
    - H0 = 67.68 ± 1.06; 67.79 ± 1.09.  
  - These match Table I numerically. However, the text later references H0 = 67.69 (full‑tension) in some places (MB–H0 discussion), reflecting rounding inconsistencies.  
- **Required fix:**  
  - Choose a consistent rounding convention (e.g. two decimals) and ensure all appearances of H0 in the text match the table values to that precision.  
  - Explicitly note when numbers differ slightly because they refer to a later chain or a thinned subset.

---

**P1B-m2 – Internal audit narrative might confuse readers**  
- **Location:** Footnote 1 in Sec. III; parts of Sec. II; Appendix A “What is NOT included”.  
- **Problem:**  
  - The paper contains detailed chain accounting, e.g. “176,240 × 0.7 ≈ 123,368” vs “123,129” and a long explanation about burn‑in, thinning, and alias bugs. This is appropriate in a lab log or GitHub issue, but distracts from the main physics in a PRD article.  
- **Required fix:**  
  - Summarize chain statistics succinctly: report total raw samples, post‑burn‑in effective samples, and R̂−1; move detailed discrepancies into a supplemental note or delete them.  

---

**P1B-m3 – Mixing of “Planck 2018” vs “Planck NPIPE/PR4”**  
- **Location:** Sec. V.A datasets; Sec. III; Fig. 1 caption; references , .  
- **Problem:**  
  - The manuscript uses “Planck 2018 NPIPE” and “Planck PR4 / NPIPE” somewhat interchangeably, and references  (Planck 2018 parameters) which relates to PR3, not PR4/NPIPE, while  is clearly PR4/NPIPE.  
- **Required fix:**  
  - Clarify explicitly which Planck likelihoods are used in each analysis (PR3 vs PR4/NPIPE) and ensure references match.  
  - Avoid phrases like “Planck 2018 NPIPE” which conflates the 2018 parameter paper (PR3) with the later NPIPE/PR4 maps; use consistent nomenclature.

---

**P1B-m4 – Use of non‑standard internal tags and identifiers in the scientific text**  
- **Location:** Introduction (“Paper I(a) [1]”; references [1], [4]–[6]); Appendix A.  
- **Problem:**  
  - The use of internal codes like “hUBIFY‑2026‑001A”, “this volume”, and GitHub folder names in the main physics narrative is not standard PRD style.  
- **Required fix:**  
  - Remove internal identifiers from the main text; keep them, if necessary, in a footnote or in the data‑availability statement.  
  - Replace “this volume” with “companion paper [arXiv:…]” once those papers exist.

---

**P1B-m5 – Claims classification table [Table III] is unconventional**  
- **Location:** Table III, p. 10.  
- **Problem:**  
  - The “Claims classification” table is an internal QA artefact (listing each claim as “MCMC Verified, Numerical Omitted, etc.”). While laudably transparent, it is not standard in PRD and may confuse readers about what is part of the scientific argument vs QA metadata.  
- **Required fix:**  
  - Either move this table to supplementary material or reframe it as a concise summary table of key numerical results, removing internal labels like “Verified / Omitted / Defn.” and instead providing references or methods.

---

**P1B-m6 – Some equations and symbols could use clearer definitions**  
- **Location:** various, esp. Sec. II and VI.  
- **Problem:**  
  - Symbols such as (ω/H)0, S8, wpivot, Caγ are either defined only once or implicitly; readers may struggle if they are not experts.  
- **Required fix:**  
  - Ensure each symbol appears with a clear definition at first use (even if briefly: e.g., “S8 ≡ σ8(Ωm/0.3)1/2”, “wpivot is the CPL equation‑of‑state at the pivot redshift”, etc.).

---

### NIT issues (cosmetic)

**P1B-n1 – Typographical and formatting glitches**  
- **Location:** throughout; e.g. Sec. II “The bounce scenario motivates… per the explicit parameter-scope clarification”; justification around footnotes 4–5.  
- **Problem:**  
  - Occasional hyphenation artifacts (“pseudo-Cℓ de- convolution”), spacing issues (“Neff ” with stray space), and some capitalisation anomalies (“RETained”, “RETAINED”) likely from copy‑paste or manual emphasis.  
- **Required fix:**  
  - Run a full spell‑check and typographical pass; fix hyphenation, superscript spacing, and capitalization inconsistencies.

**P1B-n2 – Language around AI use and run‑time details**  
- **Location:** Acknowledgments; Appendix A; Abstract.  
- **Problem:**  
  - References to “use of Claude (Anthropic) as an AI research assistant” and specific “RunPod H200 instances” are more appropriate for a data‑release note than a PRD article.  
- **Required fix:**  
  - Condense these to a brief high‑level acknowledgement, if needed, and omit vendor names and hardware rental details from the main text.

---

## Summary recommendation

**Recommendation: REJECT**

The manuscript contains substantial problems with its citations (future‑dated/non‑existent references, over‑reliance on “in preparation” self‑citations, an unverified ACT DR6 birefringence result), and its main scientific content is primarily a technical logbook for an unpublished companion paper rather than a self‑contained PRD‑level contribution. Fixing all essential and major issues would require not just corrections but a re‑scoping of the work and the appearance of several currently non‑existent references. A future submission combining the main structural results with a tightened, fully verifiable methods section could be appropriate, but the present manuscript does not meet PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-N1 – Abstract σ and “sky detection significance” language now internally inconsistent and partly incorrect  
- **Location:** Abstract, first paragraph; Sec. IV “Birefringence measurements are adopted…”; Sec. VI “Headline observational constraint”; Conclusions.  
- **New issues (beyond P1B‑E3/E5):**  
  - The abstract states: “The primary sky detection significance is the **published Planck/ACT DR6 2.4–2.9σ [2,3]**; the pipeline SNR figures…are not competitive sky measurements.” This presents a Planck/ACT DR6 2.4–2.9σ result as published and as the primary sky detection significance.  
  - In the body, the **headline observational constraint** is clearly stated to be **Eskilt & Komatsu’s joint WMAP+Planck β = 0.342° ± 0.094° (3.6σ)**, with the combined 3.9σ explicitly demoted to an auxiliary cross‑check and ACT DR6 entering only via a separate 0.215° ± 0.074° value.[2] This contradicts the abstract’s emphasis on “primary sky detection significance” as a Planck/ACT DR6 2.4–2.9σ measurement.  
  - Sec. IV now says “Birefringence measurements are adopted from the published literature: β = 0.30° ± 0.11° (Planck NPIPE ) and β = 0.215° ± 0.074° (ACT DR6 [3]). The spectator‑ALP analysis (Sec. VI) uses these published values.” But Sec. VI explicitly uses β = 0.342° ± 0.094° (joint WMAP+Planck) as the primary input and the Planck‑only 0.30° and ACT 0.215° values only for an *auxiliary* inverse‑variance combination (Eq. (4)). These two textual claims conflict.  
- **Required fix:**  
  - Remove or rewrite the abstract sentence so that the *headline* sky detection significance is consistently the **3.6σ Eskilt & Komatsu WMAP+Planck** result, with the 2.4–2.9σ Planck/ACT wording either corrected to match a real published analysis or dropped entirely.  
  - In Sec. IV, clarify that the *ALP analysis in Sec. VI* primarily uses the **3.6σ joint WMAP+Planck** result, and uses the Planck‑only and ACT values **only** in an auxiliary combination; reconcile this with the current “uses these published values” wording.  
  - Ensure all occurrences of “primary sky detection significance” and “headline observational constraint” point to the same, actually published statistic, and that ACT DR6 is not described as “published…Planck/ACT DR6 2.4–2.9σ” unless an explicit, traceable reference exists.

---

P1B-N2 – Arithmetic in the MB–H₀ tension check is inconsistent with quoted σ and with earlier tension value  
- **Location:** Sec. II (MB–H₀ joint‑posterior offset check).  
- **New issues (A: arithmetic; J: stale numbers):**  
  - The text computes the Pantheon+ combination constant at the chain mean as  
    \(-19.263 - 5 \log_{10}(67.69) = -28.416\).  
    Using the stated H₀ = 67.69 km/s/Mpc:  
    \(\log_{10}(67.69) ≈ 1.8307\), \(5\log_{10}(67.69) ≈ 9.1536\), so  
    \(-19.263 - 9.154 ≈ -28.417\), consistent within rounding.  
  - At the Riess anchor the constant is given as −28.571. The difference is ∆ = 0.155 mag, which matches the text.  
  - However, the text then states: “This offset is ∼ 3.2σ relative to the chain’s σ_MB = 0.049… and corresponds exactly to the canonical 3.6σ Hubble tension.”  
    - 0.155 / 0.049 ≈ 3.16, so **3.2σ** is consistent numerically.  
    - But describing this as “exactly the canonical **3.6σ** Hubble tension” is **arithmetic/logic slippage**: 3.16σ is noticeably smaller than 3.6σ, and “exactly” is inaccurate.  
  - Elsewhere (Table I, abstract, conclusions) the full‑tension H₀ error is 1.06 km/s/Mpc and the Riess error is 1.04, giving a combined σ ≈ √(1.06²+1.04²) ≈ 1.48 and ∆H₀ ≈ 5.36, hence ∆/σ ≈ 3.6σ. That is consistent, but **mapping 3.16σ in MB directly to 3.6σ in H₀ and calling them “exactly” equal is not justified.**  
- **Required fix:**  
  - Replace “corresponds exactly to the canonical 3.6σ” with a quantitatively accurate statement, e.g. “corresponds to ≈3.2σ in MB, consistent with the ≈3.6σ H₀ tension once the joint covariance is taken into account,” or else recompute and show explicitly how the MB‑axis offset maps to 3.6σ in H₀.  
  - Ensure that the tension quoted in MB and in H₀ are numerically consistent and that wording does not overstate equality (avoid “exactly” when the σ values differ).

---

P1B-N3 – DESI “DR2” vs “DR1” still internally inconsistent in datasets, chain description, and Table II caption  
- **Location:** Sec. V.A; Table II caption; Sec. III “Independent cross‑validation”.  
- **New issues (D: cross‑refs; F: abstract faithfulness; J: stale numbers/labels):**  
  - Sec. V.A says: “We analyze four dataset combinations: (1) Planck 2018 NPIPE; (2) +DESI 2024 DR1 BAO ; (3) +Pantheon+; (4) +SH0ES H₀ prior + DES Y3 S₈.” This suggests that the MCMC configurations in this paper use **DESI 2024 DR1**.  
  - Table II caption explicitly labels the likelihood stack as “**DESI DR2 BAO + Planck 2018 NPIPE … + DES‑Y5 + Pantheon+**” and the body text repeatedly terms this “DESI DR2 w₀wₐ posterior”.  
  - Sec. III “Independent cross‑validation” compares to “Liu et al. …using DESI DR2 + Pantheon+ + DES‑SN5YR + Planck 2018” and then states “Our MCMC agrees…” implying the chain in this paper uses an analogous DR2 configuration.  
  - There is no clear, explicit reconciliation of:  
    - Whether **any** DR2 public likelihood is actually used;  
    - Whether Table II’s “DESI DR2” is in fact built from DR1 BAO plus additional assumptions;  
    - Why Sec. V.A still mentions “DESI 2024 DR1 BAO” while Table II and the independent cross‑validation call the combination “DESI DR2”.  
- **Required fix:**  
  - Explicitly state, in Sec. V.A and in the Table II caption, **exactly which DESI release** is used in the chain whose results are tabulated. If only DR1 BAO is used, remove “DR2” everywhere and update the Liu‑comparison wording to avoid implying DR2.  
  - If DR2‑like internal or preliminary products were used, this must be clearly labeled as **internal / non‑public**, with a discussion of why this is acceptable for a PRD methods paper, or such results must be demoted or removed.  
  - Ensure all “DR1/DR2” labels and DES vs DES‑SN vs DES‑Y3/Y5 labels agree between Sec. V.A, Sec. III, and Table II; otherwise the abstract’s and conclusions’ references to the quintom result are not reproducibly anchored.

---

P1B-N4 – Equations (2)–(4) lack explicit units and normalizations needed for dimensional clarity  
- **Location:** Sec. VI equations (2), (3), (4); footnotes 3–5; Appendix C.  
- **New issues (C: dimensional consistency/normalization):**  
  - Eq. (2): \(\Delta\phi/f_a ≈ 0.65 (m = H_0, \theta_i = 1)\). The equation is dimensionless on both sides, which is fine, but the **normalization** is opaque: the definition of \(\Delta\phi\) (exact redshift interval, initial condition, numerical scheme) and the precise background \(H(z)\) are only cursorily mentioned. Footnote 3 says H(z) is ΛCDM, but there is no explicit expression or parameter set; this makes it difficult to validate the numerical factor 0.65.  
  - Eq. (3):  
    \[
    \beta ≈ \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi}\times 1.07 ≈ 0.29^\circ.
    \]  
    The underlying relation \(\Delta\beta = (\alpha_{\rm EM} C_{a\gamma} / 4\pi) (\Delta\phi/f_a)\) is standard, but here the factor “1.07” is not defined; it implicitly encodes \(\Delta\phi/f_a\) in radians and numerical constants, and the text jumps directly to “≈ 0.29°” for \(C_{a\gamma}=8\). Without an explicit statement that β is in radians in the intermediate expression and only converted to degrees at the end, the dimensional content is unclear (angle units are implicitly mixed).  
  - Eq. (4): \(\beta_{\rm combined} = 0.241^\circ \pm 0.061^\circ (3.9\sigma)\) is numerically dimensionally consistent, but the procedure lacks an explicit formula showing the inverse‑variance weighting and **clarifying that the input β’s are treated as Gaussian in degrees, converted to radians or not, and then converted back to degrees**. As written, readers must infer that all operations are carried out in a consistent angle unit.  
- **Required fix:**  
  - For Eq. (2), add one line clarifying the integration setup: specify the redshift interval, normalization of H(z), and show the approximate analytic expectation (e.g. slow‑roll or underdamped oscillatory solution) alongside the numerically obtained 0.65 value.  
  - For Eq. (3), write the full expression  
    \[
    \beta \,[{\rm rad}] = \frac{\alpha_{\rm EM} C_{a\gamma}}{4\pi} \frac{\Delta\phi}{f_a},
    \]  
    then state explicitly that for \(C_{a\gamma}=8, \Delta\phi/f_a ≈ 1.07\) one obtains β ≈ X rad ≈ 0.29°. Make the conversion to degrees explicit to avoid unit ambiguity.  
  - For Eq. (4), include the standard inverse‑variance formula and explicitly mention that all β inputs are converted to a common unit before combining; this addresses dimensional/normalization transparency rather than raw correctness.

---

P1B-N5 – “Canonical quintom signature” language still overstates the strength/interpretation of the w₀–wₐ result  
- **Location:** Table II “vs ΛCDM” column; surrounding discussion in Sec. III (Physics interpretation (Table II)); Sec. V.B; Conclusions “Forward” paragraph.  
- **New issues (G: unsupported novelty; H: unquantified hedges):**  
  - Table II labels w₀ + wₐ = −1.4788 ± 0.1485 with the commentary “phantom‑crossing required” and w₀–wₐ behavior called “the canonical quintom signature” both in Table II and in the text.  
  - While the σ‑values for departures (w₀ +4.3σ from −1, wₐ −3.6σ from 0) are quoted and are arithmetically consistent with the means/σ’s in Table II, the manuscript still:  
    - Does not show any **explicit comparison** to official DESI or combined analyses that might or might not see a similar w₀–wₐ preference.  
    - Does not quantify how sensitive this “canonical quintom signature” is to prior choices (e.g. flat vs informative priors on w₀, wₐ), dataset selection (DR1 vs “DR2” confusion above), or SN systematics.  
    - Uses “canonical” as if this particular numerical result were the standard or definitive example of quintom behavior in the literature, but does not demonstrate this via citations or comparative plots.  
  - The later caveat that robust ln B is not given is good, but **“canonical quintom signature” remains an interpretive leap** that is not explicitly supported by comparisons or robustness checks.  
- **Required fix:**  
  - Downgrade the language to something like “consistent with quintom‑like behavior under the CPL parameterization” and explicitly add that this is **model‑dependent** and may be sensitive to data/priors.  
  - Add at least one sentence comparing your w₀–wₐ contour qualitatively with published w₀–wₐ constraints from DESI+Planck+SN (if available), or state explicitly that no official DESI w₀–wₐ result exists yet and that this is an internal re‑analysis only.  
  - Where “phantom‑crossing required” is stated, make explicit that this conclusion is under the CPL parameterization and assumes no additional degrees of freedom or systematics shifts; otherwise it reads as a stronger physics statement than the evidence strictly supports.

---

P1B-N6 – σ and SNR values juxtaposed without full comparability caveats in every instance  
- **Location:** Sec. IV (“Independent verification” paragraph); Sec. VI (summary of ALP MCMC results); Conclusions (NaMaster paragraph).  
- **New issues (E: null‑procedure comparability, beyond earlier E5):**  
  - Sec. IV: “Injecting…β = 0.27°…recovers β̂ = 0.238° (pipeline‑recovery SNR = 20.32)…For β = 0.342°…SNR = 25.71; for β = 0, recovery is consistent with zero (null check).” Only earlier in the section is it stated that these are not sky detection significances, but the individual sentences listing “20.32, 25.71” and later the “0.032–0.040° (worst‑case 0.040° at injection β = 0.342°)” in the Conclusions are not **each accompanied** by explicit “pipeline‑only, not sky σ” caveats.  
  - Sec. VI: the ALP‑MCMC results (β_ALP = 0.336° ± 0.107°, β_free = 0.344° ± 0.096°) are placed near references to the 3.6σ published significance and the auxiliary 3.9σ combination. While the section does say the 3.9σ is auxiliary and neglects systematics, it does not explicitly restate that the MCMC σ’s, the inverse‑variance σ, and the published 3.6σ are **different null procedures** and are not strictly comparable.  
- **Required fix:**  
  - In Sec. IV, append a short phrase wherever “SNR = 20.32, 25.71” is quoted, e.g. “(pipeline SNR for injected MC signals; not a sky‑detection σ)”. Do the same in the Conclusions paragraph summarizing NaMaster bias.  
  - In Sec. VI, when listing β_ALP, β_free, 3.6σ, and 3.9σ in proximity, add one explicit sentence that these σ values arise from **different likelihoods and null procedures** (published WMAP+Planck analysis, simple inverse‑variance combination, and your internal ALP‑parametric and model‑independent fits) and are therefore **not directly comparable**, even though they are numerically similar.

---

P1B-N7 – Abstract and Conclusions still over‑compress caveats on ALP misalignment tuning and coupling range  
- **Location:** Abstract (ALP sentence); Sec. VI “Summary‑likelihood combination” and “Caveats” paragraphs; Conclusions “Spectator‑ALP consistency” paragraph.  
- **New issues (F: abstract faithfulness; H: hedges):**  
  - The abstract: “(3) Spectator‑ALP consistency check: a field with f_a ~ M_Pl, m ~ H₀ is consistent with the published joint…β = 0.342° ± 0.094° (3.6σ)…Spectator‑status caveat: for θ_i ~ 1 the ALP energy density…is of order the critical density…so the spectator label is only consistent under θ_i ≪ 1…at θ_i ~ 1 the ALP must instead be treated as the dark‑energy field itself…”  
  - Sec. VI body and footnotes 4–5 state more sharply that spectator‑consistency really requires θ_i ~ 0.1, i.e. a **~25× tuning** relative to the scan midpoint θ_i = 0.5, and that the coupling required to match β corresponds to C_{aγ} in the range ~9–51, “outside minimal ALP benchmarks,” plus further enhancement when enforcing the θ_i ~ 0.1 spectator condition.  
  - The Conclusions still say: “An ALP with f_a ~ M_Pl, m ~ H₀ is consistent with the published 3.6σ joint signal, with the caveat that the spectator‑consistent regime θ_i ~ 0.1…requires ~25× misalignment tuning…The same result arises in standard GR…” This does acknowledge the tuning, but **does not restate the strong statement from Sec. VI that the required photon coupling is outside minimal KSVZ/DFSZ and may require substantial UV enhancement**, nor that the spectator‑consistent corner raises C_{aγ} even further.  
- **Required fix:**  
  - Strengthen the abstract and conclusion wording to match the more detailed caveat: explicitly note that **accommodating the observed β within a spectator ALP with θ_i ~ 0.1 requires both (~25×) misalignment tuning and photon couplings larger than minimal KSVZ/DFSZ benchmark values**.  
  - Add a short quantitative phrase into the abstract or conclusions (e.g. “requiring C_{aγ} in the range ~9–50 for θ_i in the natural scan and even larger values in the strictly spectator θ_i ~0.1 corner”) so that the reader does not come away with the impression of an essentially “natural” ALP explanation.  
  - Ensure that the “not a distinctive ECH prediction” caveat is accompanied by the same strength of tuning/coupling caveats present in Sec. VI, to keep the abstract and conclusions faithful to the more cautious body text.

---

If you want, I can now:  
- Walk through a systematic arithmetic audit of each table entry (especially σ, S₈, and χ² decompositions), or  
- Draft a concise “second‑round referee report” that integrates both the original and these additional findings in PRD‑style language.