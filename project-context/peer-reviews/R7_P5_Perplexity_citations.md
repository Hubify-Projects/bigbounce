# P5 R7 — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 50.6s

---

P5-B1 (ESSENTIAL) – References section, multiple pages  
**Problem:** Several references are “companion paper (in preparation)” by the same author, but they are cited as if they provide concrete, quantitative results that this paper relies on. In particular:  
- [3] “A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity, companion paper (Paper IV), in preparation.”  
- [4] “fN L = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation.”  
There is no arXiv ID, DOI, or public record for [3] or [4] that can be verified; yet [3] is used as the source for the catalog, the monopole ∆fCW, and several quoted σ-values and uncertainties throughout the paper. These are treated as established, citable results from the literature.  
**Required fix:**  
- Either (a) upload Paper IV (and Paper II if needed) to arXiv and update the references with arXiv IDs, or (b) clearly mark them as *unpublished internal work*, restate all needed technical details in the current paper, and adjust the language so that no unverifiable “result” is attributed to a non-public paper.  
- The abstract and body must be rewritten to make clear that the catalog and its monopole offset are produced in the same research program and are not independently peer‑reviewed inputs.  

P5-B2 (ESSENTIAL) – Paper IV quantitative claims unverifiable  
**Location:** Abstract; Introduction; Sec. II; Sec. V; Sec. VIII F; Conclusions; citations to [3].  
**Problem:** The paper repeatedly quotes numerical results from Paper IV ([3]) such as:  
- “Paper IV establishes the global mixture … CW fraction of 0.4974 ± 0.000279”  
- “the catalog-wide ∆fCW ≈ −0.0026 offset from 0.5 that is spatially uniform and quality-quartile-flat”  
- “Paper IV’s full-sky dipole null is at σ = 0.43, p = 0.30 … and −0.12σ for the subsample-mask MASTER-deconvolved ℓ = 1 amplitude”  
- “∼ 9.5σ catalog-level monopole reported in Paper IV”  
Because Paper IV is not publicly available (no arXiv/ADS record to check), these quantitative statistics cannot be audited against tables or abstract; it is impossible to confirm that the values and their stated interpretation match any accessible source. They are effectively black‑box inputs.  
**Required fix:**  
- Include in the present manuscript all necessary derivations, definitions, and tables for the catalog-level fCW, ∆fCW, and dipole constraints that are used as priors/inputs here, so that a referee can check consistency without access to Paper IV.  
- Alternatively, make Paper IV public and stable (arXiv), and ensure all quoted numbers here exactly match its text/tables; then update the reference with the arXiv ID.  

P5-B3 (ESSENTIAL) – σ from different null procedures compared on a single scale  
**Location:** Abstract; Sec. V; Sec. VI; Sec. VII; Sec. VIII F; Sec. XI.  
**Problem:** The paper uses “σfrom half”, “|σobs − σpred|”, binomial σ, and permutation‑based empirical p-values somewhat interchangeably, and phrases like “none reach 3σ after look-elsewhere correction” combine σ computed under different nulls and procedures as if they were all directly comparable. Example:  
- Abstract: “counting statistics of ∼ 5 pp (statistical-dominated for V-Web void at n = 428, ∼2σ on the binomial null)” vs. permutation p-values elsewhere.  
- Sec. V.A: Bonferroni thresholds in terms of σ are used alongside empirical max-stat permutation pLEE.  
- Sec. XI: “No test produces a > 3σ residual after Paper IV-monopole correction,” aggregating across χ² tests, binomial σ, and permutation results.  
This risks presenting σ from different test statistics and null structures as if they lived on a single, directly comparable “σ scale,” contrary to the instruction that such mixing must be explicitly qualified.  
**Required fix:**  
- For every occurrence where σ from different null procedures are compared or a global statement like “no 3σ signal” is made, explicitly state *which σ* is being used (e.g., binomial deviation σfrom half under the f=0.5 null; z from a χ²; Gaussian-equivalent σ from permutation pLEE), and avoid using a single 3σ threshold across heterogeneous tests unless you provide a clear mapping.  
- If a statement aggregates different tests (“no test exceeds 3σ”), either convert all p-values to a common Gaussian-equivalent σ explicitly, or rephrase in terms of p-value ranges without pooling the σ language.  

P5-B4 (ESSENTIAL) – Version‑/review‑log language in body text  
**Location:** Sec. V.B (“pre-registration caveat”), Sec. XIII–XV, Appendix, Reproducibility checklist.  
**Problem:** The paper includes internal process language that reads as a version/audit log rather than scientific content:  
- “Primary vs. secondary analysis paths (pre-registration caveat)”  
- “the choice of which classifier to report as ‘primary’ is therefore made post‑hoc, and we declare it explicitly here”  
- “garden-of-forking-paths concern”  
- “companion data repository” plus a “Reproducibility checklist” with seed “20260515” and bullet points.  
While some of this can be acceptable as transparency, the style is closer to a pipeline audit and pre‑registration commentary than standard PRD prose, and appears multiple times, making the manuscript read like an internal methods log.  
**Required fix:**  
- Remove or heavily condense all explicit “pre‑registration,” “garden of forking paths,” and “Reproducibility checklist” language from the main body. At most, keep a brief, neutral “Analysis choices and robustness” subsection, phrased in standard scientific terms (e.g., “We treat DESIVAST as the primary environment definition; other classifiers provide diagnostics only.”).  
- Move any remaining reproducibility information to a short “Data and code availability” paragraph in a conventional style, without bullet‑point audit language.  

P5-B5 (ESSENTIAL) – Theoretical operator attribution is misleading  
**Location:** Appendix A, first paragraph.  
**Problem:** The paper introduces a toy parity‑violating operator  
“Lparity ⊃ gϕ (∇i ϕ)(∇i ρ/ρbg)(L̂ · ẑ)”  
and says this “is not contained in either Alexander & Yunes [1] or Lue–Wang–Kamionkowski [2],” but is “inspired by” them. However, in the main text (Sec. XII.B) and earlier, it uses language such as “parity‑violating interactions in the bounce‑chirality coupling class (Sec. II)” without very clearly separating established literature from this new schematic operator. This risks readers inferring that the operator has some grounding in [1,2] beyond generic inspiration.  
**Required fix:**  
- In Appendix A and any body references to it, clearly label this operator as *purely illustrative and original to this work*, not part of the existing EFT literature. Explicitly state that no quantitative constraint on gϕ is derived in this paper.  
- Ensure no sentence suggests that [1] or [2] contain this form; keep all connections clearly at the “motivates the idea of parity‑violating gravity” level.  

P5-B6 (ESSENTIAL) – Abstract claims rely on non‑public or non‑verifiable inputs  
**Location:** Abstract.  
**Problem:** The abstract’s headline result and its stated sensitivity floor are phrased as if based on independently established, verifiable inputs:  
- “sensitivity floor set by the Paper IV catalog‑monopole offset of ∼0.2 pp”  
- “Paper IV catalog-monopole offset … reported in Paper IV”  
Because Paper IV is non‑public, its monopole measurement, error budget, and systematic treatment cannot be checked. Yet the abstract positions it as the limiting error source for environment tests, effectively privileging an unreviewed prior.  
**Required fix:**  
- Rephrase the abstract to make it explicit that the catalog and monopole offset are produced within the same program and that the environment‑dependence null is conditional on that internal calibration.  
- Either provide enough information in the current paper to independently reconstruct that monopole estimate, or soften the language so that the monopole is treated as a working assumption rather than a hard “sensitivity floor.”  

P5-M1 (MAJOR) – Cited external papers: metadata and content checks  

Below, I list each reference that can be checked via arXiv/ADS, and whether the citation (title, journal, year) and usage are accurate.

- **[1] S. Alexander & N. Yunes, “Chern–Simons modified general relativity,” Phys. Rep. 480, 1 (2009), arXiv:0907.2562.**  
  - ADS/arXiv confirm title, authors, year, journal, and DOI are correct. The paper is indeed a review of Chern–Simons modified gravity and parity‑violating effects in GR.  
  - In the body, [1] is only used at a high level (“parity‑violating interactions”/“Chern–Simons modified general relativity”). That use is faithful.  
  - **No changes required.**

- **[2] A. Lue, L. Wang, M. Kamionkowski, “Cosmological signature of new parity-violating interactions,” Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088.**  
  - ADS confirms the title, authors, journal, and year.  
  - Used appropriately as an example of cosmological parity‑violating interactions. No specific numeric result is quoted.  
  - **No changes required.**

- **[5] O. Hahn et al. 2007, “Properties of dark matter haloes in clusters, filaments, sheets and voids,” MNRAS 375, 489, astro-ph/0610280.**  
  - Checked via ADS: metadata is correct. This paper proposes a cosmic web classification based on the tidal tensor (T‑Web; they use the deformation tensor and eigenvalues).  
  - The paper uses [5] as part of the basis for the V‑Web classification methodology. That is consistent; although Hahn et al. discuss a deformation tensor version, the “count of positive eigenvalues defines environment type” usage matches.  
  - **No changes required.**

- **[6] Y. Hoffman et al. 2012, “A kinematic classification of the cosmic web,” MNRAS 425, 2049 (2012), arXiv:1201.3367.**  
  - ADS confirms title, authors, year, journal are correct. This is indeed the original V‑Web paper (based on the velocity shear tensor).  
  - The manuscript cites [6] properly as the V‑Web method’s source. It does not misquote any numerical results from that paper.  
  - **No changes required.**

- ** M. Cautun et al. 2014, “Evolution of the cosmic web,” MNRAS 441, 2923 (2014), arXiv:1401.7866.**  
  - ADS confirms metadata. Cautun et al. do use a λth threshold and discuss classification into void/sheet/filament/cluster using eigenvalues.  
  - The paper refers to “Cautun et al.  geometric default λth = 0,” which matches what is standard in that work and the subsequent literature. No quantitative values from  are misquoted.  
  - **No changes required.**

- ** Planck Collaboration 2018 – “Planck 2018 results. VI. Cosmological parameters,” A&A 641, A6 (2020), arXiv:1807.06209.**  
  - Metadata matches ADS. Planck 2018 does provide H0=67.4–67.7 km/s/Mpc and Ωm≈0.315 depending on model, consistent with what is used here (H0 = 67.66, Ωm = 0.315).  
  - The use is only to define the background cosmology; no Planck‑level constraints are misquoted.  
  - **No changes required.**

- ** L. Shamir 2022, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866.**  
  - ADS and arXiv confirm title, journal, year, and that Shamir indeed finds a few‑per‑cent level large‑scale chirality asymmetry.  
  - The manuscript states that Shamir reports “a ∼2–4% large-scale asymmetry on ∼1.3×10^6 Ganalyzer-classified galaxies,” which is consistent with the abstract and figures in Shamir (he quotes anisotropies at a few‑percent level).  
  - **No changes required.**

- ** E. Tempel et al. 2014, “Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation,” A&A 566, A1 (2014), arXiv:1402.1350.**  
  - ADS confirms metadata.  
  - The paper uses this as the source of the FoF group catalog with multiplicity‑based environment classification (isolated/small group/filament‑like/cluster‑like). That is consistent with Tempel et al.’s environment definitions via group richness.  
  - The paper does not misquote any of Tempel’s quantitative results; all quoted numbers (e.g., n=588,193 SDSS DR10 galaxies) can be matched to Tempel’s catalog description.  
  - **No changes required.**

- ** H. I. Ullah et al. 2026, “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” arXiv:2604.02463.**  
  - The arXiv record exists; the title, authors, and DR1/T‑Web methodology match. The paper’s description of void/sheet/filament/knot volume fractions in Ullah et al. as roughly {0.16,0.45,0.37,0.04} for BGS is compatible with their reported numbers.  
  - The present manuscript uses those values qualitatively (“sheet and filament fractions agree within a few percentage points, void fraction larger in V‑Web,” etc.), which is consistent with Ullah et al.’s results given the differing geometry and selection.  
  - **No changes required.**

- ** D. C. Zapata-Zuluaga et al. 2026, “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456.**  
  - ArXiv exists with that title and authors; it indeed describes ASTRA, a probabilistic cosmic web classifier on DESI EDR.  
  - The usage here (EDR rosettes only, per-object probabilities, 4‑class void/sheet/filament/knot) matches Zapata-Zuluaga et al. No specific numeric constraints from  are misquoted.  
  - **No changes required.**

- ** H. Rincón et al. 2025, ApJ 982, 38, “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” arXiv:2411.00148.**  
  - ADS/arXiv confirm the title, journal, year, and that it is indeed a DR1 BGS void catalog with VoidFinder and ZOBOV (REVOLVER/VIDE) implementations and ~3,700 maximal voids.  
  - This paper is accurately represented as a public DR1 void catalog; the reported numbers—e.g., ~1,461 interior voids (VoidFinder), 420 REVOLVER, 295 VIDE, and ~3,765 maximal voids—match Rincón et al.’s catalog description.  
  - **No changes required.**

P5-M2 (MAJOR) – “Companion data repository” and Zenodo references lack concrete identifiers  
**Location:** Sec. V, VII, VIII.A, X, Appendix B.  
**Problem:** Several sections refer to a “companion data repository” and to the ASTRA catalog’s Zenodo ID, but the paper as written does not give a concrete DOI or URL (PRD will strip raw URLs anyway). For reproducibility, the repository must be uniquely identifiable and stable.  
**Required fix:**  
- Replace generic “companion data repository” with a citable Zenodo (or similar) DOI in the text, preferably in a short “Data and code availability” section.  
- For ASTRA, cite  as the primary source (which already exists on arXiv) and only mention Zenodo in passing if necessary, without unresolvable URLs.  

P5-M3 (MAJOR) – Length vs. contribution  
**Location:** Entire manuscript (20 pages).  
**Problem:** For a single central conclusion (environmental independence of spiral chirality), the paper is very long and includes extended discussions of analysis-path bookkeeping, toy EFT mapping, future LSST extension, and a lengthy multi‑page exposition of null tests and audit‑style notes. This dilutes focus and makes it harder to evaluate the core result.  
**Required fix:**  
- Condense the manuscript to ~14–15 pages maximum for the stated contribution. In particular, the following can be shortened or moved to Supplementary material: Phase‑2 sweep derivation details, much of Sec. IX–X diagnostic cross‑checks, the Reproducibility checklist, and Appendix A’s EFT toy mapping (or make Appendix A significantly more concise and clearly optional).  

P5-M4 (MAJOR) – Abstract vs. body: emphasis and scope  
**Location:** Abstract vs. Sec. XII, XIII, XV.  
**Problem:** The abstract is quite dense, with a long paragraph of method and result, and explicitly mentions future Rubin/LSST + DESI DR2 disentangling, bounce‑model implications, and a bright/dark “real residual structure.” The main text later acknowledges that the bright/dark filament sign‑flip at ~3.4σ cannot be disentangled with current data and is not part of the primary headline, yet the abstract touches on it indirectly (via mention of tracer‑program decomposition) without equal clarity about its status as a residual diagnostic, not a detection.  
**Required fix:**  
- Simplify the abstract so that it states only: (i) the main headline result (no environment dependence beyond a catalog monopole), (ii) the main methods and datasets, and (iii) a brief, unambiguous statement that any residual hints (like the bright/dark sign flip) are below decisive significance and not claimed as detections.  

P5-M5 (MAJOR) – Use of “pre‑registered,” “primary/secondary” may confuse scientific vs. statistical pre‑registration  
**Location:** Sec. V.B.  
**Problem:** The “pre-registration caveat” section uses clinical‑trial style language (primary vs. secondary endpoints, pre‑registration, multiplicity bookkeeping) that may mislead readers into thinking there was a formal, externally registered analysis plan. Instead, this is internal post‑hoc choice of “primary” statistic.  
**Required fix:**  
- Rephrase to something like: “We designate the DESIVAST void analysis as the primary environment test for interpretation; the V‑Web, Tempel, and ASTRA analyses are secondary cross‑checks.”  
- Remove explicit “pre-registration” claims unless there was an actual pre‑registered plan with a time‑stamped record; if so, cite it and provide enough detail to verify.  

P5-M6 (MAJOR) – Reliance on DESI internal file paths / reduction tags  
**Location:** Sec. III.B (“zall-pix-iron.fits”; “specprod tag iron”).  
**Problem:** The paper refers directly to an internal reduction label “zall-pix-iron.fits” and “specprod tag iron,” as well as the full DESI path. This is standard in DESI collaboration papers, but PRD readers outside DESI may not know what “iron” means and whether this is the official DR1 zcatalog product.  
**Required fix:**  
- Clarify in prose that “iron” is the official DR1 spectroscopic reduction and that zall-pix-iron.fits corresponds to the public DR1 zcatalog product.  
- Make sure to match DESI DR1 documentation wording so that a reader can unambiguously identify the exact file in the DR1 release, without relying on collaboration‑internal jargon.  

P5-M7 (MAJOR) – RSD discussion ambiguities  
**Location:** Sec. VIII introduction and Sec. XIII (Limitations).  
**Problem:** The discussion of redshift‑space distortions mixes a relatively strong, qualitative claim (“essentially RSD‑immune at the level relevant to this work”) with an admission that a full RSD treatment would require reconstruction and is not done. The scalar σv/(aH) bound is given, then immediately caveated as insufficient. This may confuse readers about how robust the environmental classification is to RSD.  
**Required fix:**  
- Rewrite the RSD section to:  
  - Clearly distinguish the void membership (DESIVAST) case from the tidal‑tensor (V‑Web) case.  
  - For V‑Web, explicitly state that classifications are in redshift space without reconstruction, and that RSD could in principle move some galaxies between filament/wall/void boundaries at a level comparable to the 0.2 pp variations, but that no attempt is made here to quantify this beyond order‑of‑magnitude estimates.  
  - Avoid “RSD‑immune” phrasing unless you provide a rigorous bound.  

P5-minor findings (MINOR)

P5-m1 (MINOR) – Abstract length and density  
**Location:** Abstract.  
**Problem:** The abstract is overlong, with multiple numeric details (sample sizes, σ values, p-values) that overwhelm the main takeaway. PRD prefers abstracts that clearly state the problem, method, and key result without excessive technical detail.  
**Required fix:**  
- Shorten the abstract, keeping: data sets, key sample sizes, one representative quantification of the null result, and the main physical interpretation. Move detailed p-values and σ ranges to the main text.  

P5-m2 (MINOR) – Slightly ambiguous use of “headline” and “supporting”  
**Location:** Title; Abstract; Sec. V.B; Sec. VIII.  
**Problem:** Terms like “headline result,” “supporting cross-check,” “load‑bearing,” “supporting rather than load‑bearing” are informal and non-standard in PRD.  
**Required fix:**  
- Replace with standard terminology: “primary result,” “secondary cross-check,” “not used in the main constraint,” etc.  

P5-m3 (MINOR) – Occasional informal wording  
**Location:** Various, e.g., “bounce-chirality coupling class,” “garden-of-forking-paths concern,” “null is not positive evidence,” “headline cosmic-web result,” “load-bearing structural property.”  
**Problem:** While readable, some phrasing is closer to blog or internal note style than journal style.  
**Required fix:**  
- Systematically replace informal phrases with neutral, technical wording. For instance, “garden-of-forking-paths concern” → “multiple-comparisons concern”; “load-bearing” → “crucial” or “key.”  

P5-m4 (MINOR) – Appendix A overlaps main text  
**Location:** Appendix A vs. Sec. XII.B.  
**Problem:** Some high-level implications for bounce/inflation and parity‑violating models appear both in Sec. XII.B and Appendix A, with slightly different emphasis. This is duplicative.  
**Required fix:**  
- Either keep the conceptual discussion in the main text and strip Appendix A to a minimal schematic, or move all speculative EFT mapping entirely into Appendix A and keep Sec. XII.B strictly observational.  

P5-nits (NIT)

P5-n1 (NIT) – Minor typographical issues  
**Location:** Various.  
**Examples:**  
- Missing spaces in some places around hyphens (e.g., “class- and-target-program-conditioned”).  
- Occasional unmatched parentheses and commas in long sentences could be re-checked.  
**Required fix:**  
- Run a careful proofread or use a LaTeX linter to catch stray hyphens, missing spaces, and punctuation issues.  

P5-n2 (NIT) – “JSON artifact above”  
**Location:** Sec. VI.D.a.  
**Problem:** The text says “(sixteen-cell table, JSON artifact above),” which looks like a leftover comment referring to a removed figure or block.  
**Required fix:**  
- Remove “JSON artifact above” or replace with a proper reference to a table or figure if one exists.  

P5-n3 (NIT) – Phrase “companion data repository” repeated  
**Location:** Sec. V, VII, X, Appendix B.  
**Problem:** Repetitive wording; minor.  
**Required fix:**  
- Use a single standardized phrase once, e.g. “All analysis scripts are available in the public repository associated with this paper (see Data and code availability).”  

P5-n4 (NIT) – HEALPix/NSIDE capitalization consistency  
**Location:** Sec. VI.E, VIII.E, IX, X.  
**Problem:** “NSIDE” appears; sometimes “NSIDE-16” vs “NSIDE = 16”; minor consistency.  
**Required fix:**  
- Use uniform notation, e.g. “NSIDE = 16, 32, 64” throughout.  

P5-n5 (NIT) – Clarify “P5” in text vs. paper tag  
**Location:** Sec. XIII (“The primary P5 environment-independence claim …”).  
**Problem:** “P5” is used internally (likely paper tag); readers may not know it.  
**Required fix:**  
- Either define “P5” explicitly once as “this paper” or remove the tag and just write “The primary environment-independence claim in this paper…”.  

## Summary recommendation

**MAJOR REVISIONS**

The core scientific result—a null detection of environment-dependent spiral chirality in DESI DR1—is carefully analyzed and appears internally consistent, and all external, published references are correctly cited and used. However, heavy reliance on a non-public “Paper IV” for the catalog and monopole prior, mixing of σ from heterogeneous null procedures in global 3σ statements, and the presence of internal audit/pre-registration language in the prose all require substantial revision before publication. The paper should also be shortened and refocused on the main contribution, with ancillary material relegated to appendices or supplementary resources.