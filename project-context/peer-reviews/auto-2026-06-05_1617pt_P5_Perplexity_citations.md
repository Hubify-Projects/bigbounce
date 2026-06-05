# P5 auto-2026-06-05_1617pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11394 chars)
**Wall time**: 92.1s

---

P5-E1 (ESSENTIAL)  
Section: Abstract (page 1)  
Problem: The abstract repeatedly cites and relies on “Paper IV [3] (companion work, not yet peer-reviewed; in preparation)” as the sole source for the 8.47M-galaxy chirality catalog, the catalog monopole ∆fCW ≈ −0.0026, and the global parity/dipole null, and then treats these as hard priors throughout the paper (e.g. Eq. (1), σpred, and all “monopole-subtracted” interpretations). None of this is independently reproducible from published, peer‑reviewed literature. The arXiv entry or journal reference for Paper IV is not provided; the reference is explicitly “in preparation” and not traceable via ADS/arXiv.  
Required fix: Either (i) make Paper IV publicly available on arXiv with a stable identifier and ensure all quoted numbers (catalog size, monopole value, dipole constraints) are verifiable there, or (ii) re‑cast this paper to include a full, self‑contained description and validation of the chirality catalog (including classifier architecture, training, augmentation, selection function, catalog monopole measurement and uncertainties) sufficient for independent reproduction, and explicitly propagate the catalog-level uncertainty into every downstream σ and p-value. The current dependence on an unpublished “in preparation” companion work is unacceptable for PRD.

P5-E2 (ESSENTIAL)  
Section: Title, Abstract, throughout (pages 1–20)  
Problem: Numerous strong claims are made that are not supported by peer-reviewed external work and cannot be verified by citation forensics: e.g. “A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity” (Paper IV title in [3]), “Paper IV’s full-sky dipole null is at σ = 0.43, p = 0.30… and −0.12σ for the subsample-mask MASTER-deconvolved ℓ = 1 amplitude”, “catalog-wide ∆fCW ≈ −0.0026 offset from 0.5… ∼ 9.5σ catalog-level monopole”, etc. These values are load-bearing but not traceable to any existing arXiv/ADS record.  
Required fix: Provide verifiable bibliographic information (arXiv ID or journal reference) for Paper IV and ensure that all quoted statistics (monopole amplitude, dipole σ, etc.) are explicitly present in that work’s abstract or tables; alternatively, incorporate these derivations into this paper with full methodological detail and uncertainty accounting. Without this, the claimed sensitivity and all monopole-related corrections lack a firm foundation.

P5-E3 (ESSENTIAL)  
Section: Reference [3] (page 20)  
Problem: Reference [3] is “in preparation; manuscript in preparation” with no year, arXiv ID, journal, or other locators. PRD standards do not allow key results to depend critically on unpublished manuscripts that are neither submitted nor accessible.  
Required fix: Update [3] to a citable preprint or publication (include arXiv:YYMM.NNNNN and year, or journal citation) or clearly demote all dependence on this work to non-essential background; all main quantitative claims (monopole, dipole, catalog size, classifier details) must then be independently derived or removed.

P5-E4 (ESSENTIAL)  
Section: Abstract (page 1)  
Problem: The abstract gives specific σ and p-values (e.g. “n = 428, ∼2σ on the binomial null”; “label-shuffle p = 0.372”; “|σ|max = 3.94… residual |σobs − σpred| = 1.87, below all Bonferroni thresholds”; “p = 0.61/0.135/0.413”) but the paper does not provide enough explicit numbers (per-bin counts, exact threshold values used for each multipletest, etc.) to allow a referee to recompute all of them. For example, “∼2σ” for n=428 voids is not directly recomputed from any tabulated fCW; “below all Bonferroni thresholds” is asserted without listing all K and α in the abstract’s context.  
Required fix: Add explicit numerical details (n, nCW, fCW, σfrom half, K, α) in the main text and tables for every statistic quoted in the abstract so each σ or p can be recomputed directly. Where stated as approximate (∼2σ), the degree of approximation must be clear and consistent with the displayed data.

P5-E5 (ESSENTIAL)  
Section: V. Statistical Methods, Eq. (2) (page 4)  
Problem: The parametric Bonferroni calibration is given as  
\(|σ|_{\alpha,K}^{\rm Bonf} = \sqrt{2}\,\mathrm{erfc}^{-1}(\alpha/K)\).  
This is not a standard form and is presented without derivation; dimensional consistency and correctness are not checked via an explicit reference. It is later used numerically (e.g. |σ|Bonf0.01,5 ≈ 3.09), but these values are not supported by a cited external statistical reference.  
Required fix: Either (i) derive this mapping explicitly from the standard normal tail probability with clear steps, or (ii) replace it with the standard zα/K values from the normal distribution and cite a standard statistics reference or cosmology methods paper using the same mapping. Give sufficient detail so a referee can recompute 3.09, 4.05, etc., from first principles.

P5-E6 (ESSENTIAL)  
Section: Throughout (environment tests; pages 1–19)  
Problem: σ values from different null procedures (simple binomial σfrom half, Paper IV monopole-based σpred, permutation-derived p-values converted implicitly to σ language, “σvs monopole” residuals) are presented side by side and directly compared (e.g. “σobs”, “σpred”, “|σobs − σpred|”, “candidate environmental signals”, “no class crosses |σ|Bonf threshold”) without clear, repeated caveats that these σ figures are not strictly comparable across nulls. This directly violates the instruction that if sigma values from different null procedures appear side-by-side without explicit “not directly comparable” qualification at every juxtaposition, it must be flagged.  
Required fix: At every location where σ from distinct nulls are placed side by side or differenced (σobs vs σpred; σvs monopole vs binomial σfrom half; permutation-based significance compared to analytic Bonferroni thresholds), explicitly state that these σ values are not strictly comparable and that σ-differences are used only as heuristic diagnostics, not as exact significance comparisons. Consider re-expressing permutation results solely as p-values.

P5-E7 (ESSENTIAL)  
Section: VIII. DESIVAST-anchored void cross-validation (pages 10–12)  
Problem: The headline “primary” result hinges on DESIVAST  as a peer-reviewed void catalog, with detailed numbers (e.g. 101,863 holes; 3,765 maximal voids; 56,981 matched void spirals; three algorithms with effective radii 43.5 and 55.9 Mpc/h). Reference  is “H. Rincón et al., ApJ 982, 38 (2025)… arXiv:2411.00148”. Checking via ADS/arXiv: ApJ 982 is a volume nominally in 2025, but the arXiv identifier 2411.00148 corresponds to a November 2024 preprint; the ApJ volume and page may not yet correspond to a final published version, and the DESIVAST catalog described here (with exactly 101,863 holes and the quoted radii) must be confirmed.  
Required fix: Verify against ADS/arXiv that the DESIVAST paper indeed appears as ApJ 982, 38 with arXiv:2411.00148 and that the numbers used (void counts, radii, GALZONE semantics) match the published tables and data. If any numbers here are taken from internal DESI drafts or different versions of the DESIVAST VAC, they must be reconciled and corrected to match the published release, and any unfinalized values must be clearly labeled and not treated as peer-reviewed.

P5-E8 (ESSENTIAL)  
Section: IX.B, X (pages 15–17)  
Problem: Concurrent DR1/EDR environment catalogs T-Web  and ASTRA  are labeled as “preprint (2026), arXiv:2604.02463” and “(2026), arXiv:2604.01456”. arXiv identifiers of the form 2604.xxxxx correspond to April 2026, which at the time of writing may be extremely recent and not peer-reviewed. Moreover, the T-Web numbers quoted (“{0.16,0.45,0.37,0.04} for BGS”) and ASTRA descriptions (100 realizations per tracer-zone pair) must be traceable to their abstracts or tables.  
Required fix: Confirm via arXiv that these IDs and titles (“Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification”; “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog”) exactly match the references. Ensure that all volume fractions and methodological descriptions quoted here are explicitly documented in those preprints. Mark clearly that they are non-peer-reviewed preprints and that they are used only for cross-checks, not as primary validation.

P5-E9 (ESSENTIAL)  
Section: XII.C “Comparison to Shamir 2022 DESI Legacy” and Ref.  (pages 17, 20)  
Problem: Reference  is given as L. Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866. Checking arXiv/ADS confirms the title and bibliographic data. However, the paper here states that Shamir 2022 reported a “∼ 2 − 4% large-scale asymmetry on ∼ 1.3 × 10^6 Ganalyzer-classified galaxies”, while Shamir’s abstract and main results must be checked for the exact amplitude and sample size.  
Required fix: Verify directly from Shamir’s paper that the quoted asymmetry amplitude and sample size (“2–4%” and “1.3×10^6” galaxies) match the numbers actually reported (in the abstract or tables). If they differ (e.g., Shamir quotes a specific asymmetry level or slightly different N), adjust the text here to match the published values and explicitly cite where in  the numbers are taken from.

P5-E10 (ESSENTIAL)  
Section: Appendix A (pages 18–19)  
Problem: The “toy EFT mapping” introduces an operator \(L_{\rm parity} \supset g_\phi(\nabla_i\phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L\cdot \hat z)\) and asserts a schematic bound |gϕ(∇ϕ)/H0| ≲ 1×10−2/⟨|Δρ/ρbg|⟩, explicitly stating that this operator is “inspired by but not derived from” [1,2], and is not present in the cited parity-violating gravity literature. This is speculative theory content not supported by the referenced works and only heuristically related to the data.  
Required fix: Either remove Appendix A entirely, or substantially rework it to make absolutely clear that it is a speculative, model-dependent illustration that should not be interpreted as a quantitative bound on any specific EFT, and ensure that no numerical “bound” is given without a carefully derived mapping and explicit assumptions. In a methods paper in PRD, speculative operators that are not grounded in existing literature or in the body’s derivations should be minimized or omitted.

P5-E11 (ESSENTIAL)  
Section: Reproducibility Checklist (page 19)  
Problem: Claims of reproducibility (“All scripts and configuration files are available in the companion data repository”; “canonical chirality catalog is mirrored on HuggingFace at bamfai/galaxy-chirality-catalog”; “DESI DR1 is available at https://data.desi.lbl.gov/public/dr1/”) are made, but no DOI or frozen version tags are given for the companion repository or the HF dataset. PRD reproducibility expectations are higher for a pipeline of this complexity.  
Required fix: Provide stable DOIs or tagged version identifiers (e.g., Git commit hashes or Zenodo DOIs) for the code and catalog used in this analysis, and specify exactly which version of the HuggingFace dataset and which DESI specprod tag (iron) were used, so that a referee can reproduce every table and figure.

P5-M1 (MAJOR)  
Section: Abstract (page 1) vs. Table II (page 5) and §VI A  
Problem: The abstract lists per-class CW fractions and σ values: “void 0.4836 (n=428, −0.68σ) … filament 0.4980 (n=408,187, −2.61σ) … cluster 0.4963 (n=397,505, −4.66σ) … wall 0.5034 (n=6,673, +0.55σ)”. Table II reproduces these. Recomputing σfrom half as (fCW − 0.5)/√(0.25/N) nominally yields different σ for the void bin: using fCW=0.4836 and N=428 gives Δf = −0.0164, σ ≈ Δf·√N /0.5 ≈ −0.0164×√428/0.5 ≈ −0.0164×(20.7)/0.5 ≈ −0.68 – consistent; but the abstract describes this as “∼2σ on the binomial null” when discussing the sensitivity floor for V-Web void. That 2σ reference conflicts with the actual −0.68σ from Table II.  
Required fix: Clarify and correct this mismatch: either the approximate “∼2σ” in the abstract is incorrect and must be changed to “∼0.7σ”, or the underlying σ computation needs to be rechecked and all table entries updated. Ensure all load-bearing σ values in the abstract match the exact σfrom half given in the body.

P5-M2 (MAJOR)  
Section: VI.C / Figure 3 / Table III (page 6)  
Problem: The density-quintile analysis quotes N=158,327 per quintile and uses σpred = 2·ΔfCW·√N with ΔfCW = −0.0026, yielding |σpred|≈2.07. The observed quintile with maximum |σobs − σpred| is given as 1.87, and it is stated that this is “below the Bonferroni-5 |σ|Bonf0.01,5=3.09 threshold”. However, K=5 and α=0.01 correspond to a family-wise α=0.01, not necessarily the correct combination for this particular test unless the family definition is clearly specified. The text is ambiguous about whether other quintile-based scans elsewhere are included in the same family, which can materially affect the Bonferroni threshold.  
Required fix: Explicitly define, for each multi-bin analysis, the full family of tests K used for Bonferroni correction, and confirm that each quoted threshold (e.g., 3.09) corresponds to that K and α. Where families overlap (e.g., multiple quintile splits across different variables), clarify how multiple-testing across families is handled or justify treating them as independent.

P5-M3 (MAJOR)  
Section: VIII.A (page 10)  
Problem: The V-Web vs DESIVAST void comparison finds “0/6 V-Web ‘void’ spirals fall inside any of the 101,863 DESIVAST VoidFinder holes at z ≤ 0.24” and interprets this as confirming V-Web void-class impurity at low z. With N=6, this is extreme small-number statistics; the paper acknowledges that “the n=6 sample size is too small for a binomial significance constraint” but still uses this result qualitatively to bolster later claims of survey-edge artifacts.  
Required fix: Downgrade this specific 0/6 result to a clearly marked anecdotal diagnostic only, with no interpretive weight, or reframe it in a purely descriptive way without implying any statistical support. The survey-edge-artifact argument should rely instead on the much larger DESIVAST cross-checks (n=56,981, etc.).

P5-M4 (MAJOR)  
Section: IX.A Tempel FoF cross-validation (page 14–16)  
Problem: The mapping from Tempel richness classes to V-Web classes (isolated↔void, small group↔wall, filament-like↔filament, cluster-like↔cluster) is imposed by this paper and is not part of Tempel et al. . The statement “the Tempel classifier defines environment by FoF multiplicity rather than tidal eigenvalues” is correct, but the later interpretation that “filament class concordance 0.026 pp; supporting rather than load-bearing” implicitly treats this mapping as physically meaningful. There is no citation showing that such a one-to-one mapping has been validated in the literature.  
Required fix: Explicitly state that this mapping is a heuristic choice made in this work, not validated or guaranteed by Tempel et al., and quantify how sensitive the concordance is to reasonable alternative mappings (e.g. merging small-group+filament-like vs V-Web filament). Remove or soften any language that overstates this as a “validation” rather than a consistency check under a particular assumed mapping.

P5-M5 (MAJOR)  
Section: X ASTRA cross-validation (pages 16–17)  
Problem: The ASTRA-based cross-check uses a small EDR overlap (N=25,186) and acknowledges that “per-galaxy classifier agreement between V-Web and ASTRA argmax is poor… V-Web puts essentially the entire sample into filament and cluster… only 3 spirals in void+wall.” Despite this, the text presents the fact that both classifiers yield <3σ deviations as “a strong robustness result” for the environmental null. Given the small sample, strong per-galaxy disagreement, and very different classifier philosophies (deterministic vs probabilistic), this is overstated.  
Required fix: Re-characterize the ASTRA EDR cross-check as a weak, supplemental consistency test, not as “strong robustness.” Emphasize its statistical limitations (small N, poor label agreement, EDR footprint), and avoid giving it equal rhetorical weight with the DESIVAST and internal V-Web tests.

P5-M6 (MAJOR)  
Section: XIII Limitations (pages 17–18), RSD discussion  
Problem: The discussion of redshift-space distortions (RSD) is internally inconsistent. The scalar displacement estimate (~5–8 Mpc/h vs Rs=25 Mpc/h) is used to argue that per-class ∆fCW contamination is “sub-percent (∼0.2 pp)”, but simultaneously the text admits that anisotropic eigenvalue deformation is the actual relevant effect and has not been quantified. Yet later in the conclusions the null is asserted without carrying any explicit systematic RSD uncertainty into the per-class fCW constraints.  
Required fix: Provide a quantitative upper bound on the impact of RSD on the V-Web classification in terms of fCW (e.g. via mocks, or via analytic perturbations of the eigenvalue distribution), or explicitly include an RSD systematic error budget on the environment-dependent ∆fCW bounds. Alternatively, clearly state that the environment-independence null is conditional on the fixed redshift-space classification and that a full RSD treatment is deferred, so the current constraints should be considered preliminary.

P5-M7 (MAJOR)  
Section: Length and scope (entire manuscript, 20 pages)  
Problem: For a methods paper whose core new result is that fCW is environment-independent at the current DESI DR1 sensitivity and grid resolution, 20 pages of dense text plus multiple appendices is excessive. Large sections (e.g. the detailed bounce/inflation discussion, the toy EFT Appendix A, some of the overlapping cross-checks) are not essential to the main methodological advance and contribute to “garden of forking paths” complexity rather than clarity.  
Required fix: Condense the manuscript to ~12–14 journal pages by removing speculative theory (Appendix A), trimming repetitious cross-check descriptions, and moving non-critical diagnostics to a supplementary material. Focus the main text on the construction of the matched catalog, the V-Web and DESIVAST environment definitions, the main statistical tests, and one or two key robustness checks.

P5-m1 (MINOR)  
Section: III.B “DESI Data Release 1” (page 3)  
Problem: The paper refers to “the canonical zall-pix-iron.fits” from DESI DR1 with specprod tag “iron” and cites the DESI DR1 data portal, but does not include the full filename or version tag. While this can be inferred, explicitness would aid reproducibility.  
Required fix: Specify the exact DR1 specprod path and file version used (e.g., “spectro/redux/iron/zcatalog/zall-pix-iron.fits from DESI DR1 v1.0”), consistent with DESI documentation.

P5-m2 (MINOR)  
Section: IV.A Algorithm, step 4 (page 3)  
Problem: The text states “full DR1 bounding box 6,634 Mpc/h at 256^3 → cell 25.9 Mpc/h”. This appears dimensionally consistent (6634/256 ≈ 25.9), but no reference is given for the bounding box size, which is not an obvious DR1 constant.  
Required fix: Provide a brief justification or reference for the 6,634 Mpc/h bounding box (e.g., the RA/Dec/z limits used and how they map to this comoving extent), or include the calculation explicitly.

P5-m3 (MINOR)  
Section: VI.D Table IV (page 6)  
Problem: The density quartiles listed for cluster and filament classes show overlapping mean densities (e.g. cluster Q1 ρ̄=1.55 < filament Q4 ρ̄=1.86). The text states this is by construction, but for readers not steeped in V-Web classification this may be confusing.  
Required fix: Add one clarifying sentence explaining that V-Web class labels are based on eigenvalue thresholds rather than monotonic density, so modest overlap of average densities across classes is expected and not an error.

P5-m4 (MINOR)  
Section: IX.B T-Web cross-check (page 15)  
Problem: The text gives approximate T-Web volume fractions “≈{0.16,0.45,0.37,0.04}” for BGS without citing the specific figure or table in . For citation forensics, that mapping must be traceable.  
Required fix: Cite the specific figure, table, or section of  where these fractions are reported, and note that they are approximate values read off that source.

P5-m5 (MINOR)  
Section: XI Systematics and null tests (page 17)  
Problem: The text lists a “confidence-threshold sweep pmax_cls eq ∈ {0.4,0.5,0.6,0.7,0.8} with CW-fraction flat to within ±0.001” but provides no table or figure showing the actual fCW values at each threshold.  
Required fix: Provide a small table (even in supplementary material) with N and fCW for each threshold, or at least give one explicit example in the main text so the ±0.001 statement can be checked.

P5-n1 (NIT)  
Section: Throughout  
Problem: A few typographical glitches: “σfrom half” sometimes appears without a space, “σfrom half” vs “σ from half”; “per-footprint values within ±0.002 of global” could be more clearly stated as fCW.  
Required fix: Perform a thorough copy-edit for typography and consistent notation (e.g., always σ_from-half or σfrom half, but not both).

P5-n2 (NIT)  
Section: Reference formatting (page 20)  
Problem: Some references are missing DOIs (e.g.,  Tempel et al. 2014, [7] Cautun et al. 2014) even though DOIs exist and are commonly included in PRD submissions.  
Required fix: Add DOIs for all references where available, consistent with PRD style.

P5-n3 (NIT)  
Section: Section headings (pages 1–20)  
Problem: There are backward references to “§XIII” and “§IX B” in a few places that may change if major reorganization/shortening is done; these internal references will likely become invalid.  
Required fix: After restructuring, ensure all internal section references are updated and consistent.

## Summary recommendation

REJECT.

The manuscript attempts a comprehensive environment-independence test of spiral chirality using DESI DR1 and several environment classifiers, but it critically depends on an unpublished, non-archived companion “Paper IV” for the chirality catalog and monopole/dipole characterization, and it introduces speculative EFT content in Appendix A not grounded in the cited literature. Several key significance comparisons mix σ from different nulls without adequate caveats, and reliance on very recent, non-peer-reviewed DR1 environment catalogs further weakens the foundation. While the technical ambition is notable, the dependence on unpublished work and speculative content, combined with the excessive length and complexity relative to the core claim, place it below PRD’s standards in its current form. A future, substantially revised and fully self-contained version, built on publicly documented catalogs and cleaned-up statistical methodology, could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-N1 (NEW)  
Section: VI.C / Table III (page 6)  
Problem: The predicted sigma for the density-quintile test is mis‑computed and inconsistent between text, table, and Eq. (1). The text states that with \(N=158{,}327\) per quintile and \(\Delta f_{\rm CW}=-0.0026\), the prediction is \(|\sigma_{\rm pred}|\approx 2.07\). However, using Eq. (1) as written in the paper, \(\sigma_{\rm pred} = 2\,\Delta f_{\rm CW}\sqrt{N}\), one obtains \(|\sigma_{\rm pred}| \approx 2\times 0.0026 \times \sqrt{158{,}327} \simeq 2.6\), not 2.07. Conversely, if one uses the correct normalisation \(\sigma_{\rm pred} = \Delta f_{\rm CW}\sqrt{N}/0.5 = 2\,\Delta f_{\rm CW}\sqrt{N}\), the table’s “residual” \(|\sigma_{\rm obs}-\sigma_{\rm pred}|=1.87\) for the worst quintile also does not match what is obtained from the listed \(\sigma_{\rm obs}=-3.94\): using \(|\sigma_{\rm pred}|=2.07\) gives a residual 1.87, but then Eq. (1) is numerically wrong; using Eq. (1) strictly gives \(|\sigma_{\rm pred}|\approx 2.6\) and |σobs−σpred|≈1.34.  
Required fix: Decide on a single, correct mapping between \(\Delta f_{\rm CW}\), N, and \(\sigma_{\rm pred}\) that is consistent with the basic binomial σ‑from‑half definition, rewrite Eq. (1) accordingly, and recompute all instances of \(\sigma_{\rm pred}\), including the 2.07 value and all residuals in Table III and the surrounding text. Make the arithmetic transparent so a referee can reproduce every number from first principles.

P5-N2 (NEW)  
Section: VII / “Per-cell significance framework” (page 9)  
Problem: The text claims a Bonferroni‑9 threshold of \(|\sigma|^{\rm Bonf}_{0.05,9} \approx 3.02\). Using the paper’s own Eq. (2), \(|\sigma|^{\rm Bonf}_{\alpha,K} = \sqrt{2}\,\mathrm{erfc}^{-1}(\alpha/K)\), one finds for \(\alpha=0.05\), \(K=9\) that \(|\sigma|^{\rm Bonf}_{0.05,9}\) is substantially larger (~3.4–3.5σ depending on numerical precision), not 3.02. The quoted 3.02 is instead the value appropriate to \(\alpha=0.01\), \(K=4\) (used elsewhere), and appears to have been copied without updating K and α.  
Required fix: Recompute \(|\sigma|^{\rm Bonf}_{0.05,9}\) from Eq. (2) and correct the numerical value; verify every other Bonferroni threshold (3.09, 4.05, 2.81, 2.50, 3.02, etc.) against Eq. (2) and the stated \(\alpha,K\), and update any that do not match. Ensure that each threshold is explicitly tied to the correct α and K in the text.

P5-N3 (NEW)  
Section: VI.A / Table II vs. σ‑from‑half definition (pages 4–5)  
Problem: The definition of \(\sigma_{\rm from\,half} \equiv (n_{\rm CW}-0.5\,N)/(0.5\sqrt{N})\) is implicitly used throughout, yet the void-bin σ = −0.68 in Table II is only reproduced if that exact normalization is used. This is nowhere written explicitly in formula form (the text says “\(\sqrt{}\) signed deviation” and then a compressed inline expression), and the algebraic equivalence to the standard z‑score \((f-0.5)/\sqrt{0.25/N}\) is not clear. For several bins (e.g. filament N=408,187, f=0.4980; cluster N=397,505, f=0.4963) the quoted σ values (−2.61, −4.66) are plausible but not trivially reproducible without guessing the exact convention; small rounding differences also make it hard to verify if they are consistent to better than the first decimal.  
Required fix: Write the σ‑from‑half definition explicitly as \(\sigma_{\rm from\,half} = (f_{\rm CW}-0.5)\sqrt{N}/0.5 = 2(f_{\rm CW}-0.5)\sqrt{N}\), and add a short numerical worked example (e.g. the void bin) in the text or a footnote. Recalculate and, if necessary, slightly adjust all σ values in Tables II, III, IV, VII, VIII, IX, X, XI and any others so they match this definition to the rounding precision displayed.

P5-N4 (NEW)  
Section: VII / Phase 2 sweep, “largest single-cell |σfrom half|” (page 8)  
Problem: The description of the extreme σ value in the Phase 2 sweep mixes two different normalizations and obscures the arithmetic check. The text states: “largest single-cell |σfrom half| … is 11.32 (filament at Rs=10, λth=0, n=3,696,152). This is … predicted, not measured: \(\sigma_{\rm pred} \approx -0.0026 \cdot 2\sqrt{N} \approx -10\) matches −11.3 within order unity.” However, inserting N=3,696,152 into \(2\Delta f\sqrt{N}\) gives \(|\sigma_{\rm pred}|\approx 9.8\), and the observed 11.32 differs by ~1.5σ, which is not negligible compared to the σ scale itself. The phrase “matches within order unity” is vague and could be hiding either a mis‑computed N (e.g. using a different effective N) or an inconsistent application of \(\Delta f_{\rm CW}=-0.0026\).  
Required fix: Make the arithmetic explicit: state the exact N used in this σ calculation, compute \(|\sigma_{\rm pred}| = 2|\Delta f_{\rm CW}|\sqrt{N}\) numerically, and quote the difference \(|\sigma_{\rm obs}-\sigma_{\rm pred}|\). If N or \(\Delta f_{\rm CW}\) differ from the canonical values elsewhere, say so and justify. Either drop the “order unity” language or replace it with the actual numerical residual and a clear statement of whether that residual is treated as acceptable.

P5-N5 (NEW)  
Section: VIII.A / DESIVAST per-galaxy cross-match, percentages (page 10–11)  
Problem: Several percentages are stated without matching the raw counts well enough for a referee to check: for example, the DESIVAST void fraction “8.39% of the low-z matched sample” for nvoid=56,981 and nlz=678,945 actually evaluates to 8.39% only if those integers are exact; any rounding in nlz is not disclosed. Similarly, the statement that “DESIVAST void class is ∼130× larger than the V-Web void class (n=428)” is consistent numerically (~133×), but the tilde and the exact numbers may leave a referee wondering whether 130 is a rounded design target or an approximate ratio.  
Required fix: Where integer counts are given, ensure the percentages are computed to consistent precision (e.g. 56,981 / 678,945 = 8.39%) and, if “∼130×” is meant as a rounded ratio, either give the exact ratio 133× or explicitly say “≈133×” so that the arithmetic is completely transparent.

P5-N6 (NEW)  
Section: XI / Systematics and null tests, “per-env CW fraction shifts below 0.001” (page 17)  
Problem: The abstract and conclusions rely on statements like “per-env CW fraction shifts below 0.001” for several robustness sweeps (match-radius, confidence threshold, footprint split), but no table or explicit numbers are given in the body to allow recomputation. This is similar in spirit to P5-E4 but applies specifically to the Section XI systematics: for example, the footprint split (“per-footprint values within ±0.002”) is not accompanied by n and fCW per region.  
Required fix: Add a compact table or appendix line listing, for each of the six systematics tests, the relevant n, fCW, and \(\sigma_{\rm from\,half}\) per bin so that the claimed “<0.001” or “within ±0.002” shifts can be directly recomputed. Make sure all quoted tolerances in Section XI and the abstract are numerically traceable to these entries.

P5-N7 (NEW)  
Section: X / ASTRA EDR per-object cross-validation, “fCW does not vary by more than ∼2 pp” (page 16)  
Problem: Table XII gives only the maximum fCW range per classifier, not the actual per-class fCW values and Ns. The abstract-level claim “does not vary by more than ∼2 pp across the four classes” therefore cannot be checked by a referee from the body text: with no explicit fCW per class, there is no way to verify that the range is in fact 2.08 pp (ASTRA argmax) or 1.17 pp (ASTRA entropy-weighted) and that the underlying Ns are large enough for Gaussian σfrom‑half to be valid.  
Required fix: Expand Table XII or add an additional small table giving, for each classifier and each environment class with n≥100, the values of n, nCW, and fCW. This will allow a referee to recompute the quoted ranges and the max-|σ| values from first principles.

P5-N8 (NEW)  
Section: Figures 2–5 vs. body text (pages 5–9)  
Problem: Several figure captions and body descriptions use qualitative phrases (“range 1.98 percentage points”, “never exceeds 0.22 percentage points”, “high-|σ| pixels are isolated rather than clustered”) without explicitly quoting the same numerical values that appear or can be inferred from the plots. For example, Figure 3’s caption mentions the monopole prediction and Bonferroni thresholds, while the body text uses specific values (2.07, 3.09) that, as noted above, are internally inconsistent. This makes it difficult to check caption/body agreement numerically.  
Required fix: For each figure that is used quantitatively in the text (especially Figures 2–5), include in the caption the key numerical values that the text relies on (e.g. the 1.98 pp class range in Fig. 2, the numerical Bonferroni thresholds in Fig. 3, the maximum fCW range 0.22 pp in Fig. 5) and ensure that these match those in the body. Where the text quotes a number derived from a figure, verify that the axes and units in the figure are clearly labeled to permit recomputation (e.g. indicate that ranges are in “percentage points”).

P5-N9 (NEW)  
Section: Abstract vs. body, HEALPix p-values (pages 1, 7, 8)  
Problem: The abstract quotes HEALPix label-shuffle null p-values “p = 0.61/0.135/0.413” for NSIDE = {16,32,64}. Table V later reports p = 0.607, 0.135, 0.413, and the text in Section VII again refers to “p = 0.135 null verdict” for NSIDE=32. The 0.61 vs 0.607 discrepancy is small but, taken with other small rounded inconsistencies (2.07 vs 2.6, 3.02 vs correct Bonferroni), it contributes to a general difficulty in verifying the arithmetic behind precise sigma and p-value claims.  
Required fix: Decide on a consistent rounding convention for p-values in the abstract and body (e.g. three significant figures), and ensure that the values in the abstract (0.607→0.607, or 0.61 consistently used everywhere) match those in Table V. Explicitly link each abstract p-value to the corresponding NSIDE row in the main text so there is no ambiguity.

P5-N10 (NEW)  
Section: Appendix A vs. main text, numerical bound (pages 17–19)  
Problem: Appendix A gives a “schematic” bound \(|g_\phi (\nabla\phi)/H_0| \lesssim 1\times 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\), tracing it loosely to per-class \(|\Delta f_{\rm CW}|<0.01\). However, nowhere in the main text is a clear numeric mapping shown from the empirical upper bound on environment-dependent \(\Delta f_{\rm CW}\) (which is in practice at the level of a few ×10−3 across classes) to this 10−2/H0 scaling. Given that the operator is explicitly “toy” and not in the literature, the absence of a reproducible arithmetic chain from the observational numbers to the bound exacerbates the risk that this will be misread as a quantitative constraint.  
Required fix: Either remove the explicit numerical bound (keep only a symbolic \(\propto\) scaling), or provide a clear, step-by-step derivation from the main-text empirical numbers (maximum \(|\Delta f_{\rm CW}|\), N, and assumptions on \(\langle|\Delta\rho/\rho_{\rm bg}|\rangle\)) to the quoted \(10^{-2}\) coefficient. Make it explicit which approximations and order-of-magnitude steps are taken, so that a referee can reconstruct the mapping and verify that it is indeed only heuristic.

If you address these new items alongside the previously flagged issues, virtually every σ, p-value, and range quoted in the abstract and conclusions will become numerically traceable and internally consistent, which is what PRD expects.