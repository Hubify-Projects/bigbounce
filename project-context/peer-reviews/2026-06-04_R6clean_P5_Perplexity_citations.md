# P5 2026-06-04_R6clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.6s

---

P5-B1 (ESSENTIAL) – Mis-citation and mischaracterization of Paper IV throughout  
- **Location:** Abstract; Introduction §I; Relation to Paper IV §II; Data §III.A; Limitations §XIII; Appendix B; Reference [3]  
- **Problem:** The paper repeatedly treats “Paper IV” as a citable, immutable reference and uses its catalog and monopole offset as foundational inputs, but Reference [3] is explicitly listed only as “companion paper (Paper IV), in preparation; manuscript in preparation” with no arXiv ID, DOI, or journal, and the text refers to a specific HuggingFace revision “paper4‑v1.0.122” and a catalog monopole ∆fCW≈−0.0026 and f̄CW=0.4974 as if they were published, stable values. There is no way for a referee to verify that Paper IV indeed reports these exact numbers and systematics treatment.  
  - Example text: “Paper IV [3] ... establishes the global mixture ... CW fraction of 0.4974 ± 0.000279...” and “...the catalog-wide ∆fCW = −0.0026 classifier-monopole offset reported in Paper IV...” and “immutable HuggingFace revision paper4-v1.0.122.”  
- **Required fix:**  
  - Either (a) ensure Paper IV is on arXiv or in a journal at a fixed version and update [3] with full bibliographic information and identifier (arXiv ID and/or DOI), and verify that all quoted values (f̄CW, ∆fCW, σ, per-leg systematics) match that public version exactly; or (b) if Paper IV remains unpublished, treat its catalog as an internal data product: describe in this paper the training, test-time augmentation, monopole measurement, dipole constraints, and leg‑by‑leg systematics sufficiently that the present paper is scientifically self-contained, and remove language implying peer-reviewed status. In either case, the HuggingFace revision used must be explicitly versioned in the Data/Methods section as a *frozen* artifact, and claims about its monopole and uncertainties must be reproducible from that artifact or from the cited paper.

---

P5-B2 (ESSENTIAL) – Unverifiable numerical claims attributed to Paper IV  
- **Location:** §I (“Paper IV [3] ... CW fraction of 0.4974 ± 0.000279, ... global dipole null ... σ=0.43, p=0.30, ... −0.12σ”) ; §II; §XI; §VIII.F; §XII.C  
- **Problem:** Numerous specific statistics (f̄CW=0.4974±0.000279, ∆fCW≈−0.0026, “∼9.5σ catalog-level monopole,” dipole σ and p-values, leg-specific systematics |σ|<3) are presented as coming from Paper IV but cannot be checked because Paper IV is “in preparation” and no arXiv ID is provided. The paper also propagates these values as if their uncertainties, methodology, and selection were externally validated.  
- **Required fix:** Once [3] is public, verify that all these figures match its abstract, main tables, or clearly identified sections, and adjust them if not. If they differ (e.g., improved catalog version), state explicitly which updated numbers are used here and why they differ from the published version. If Paper IV cannot be made public before publication, then this paper must re-derive and document those statistics directly (including their uncertainties and null procedures) so the chain of reasoning is internally auditable.

---

P5-B3 (ESSENTIAL) – Claims about Paper II and Paper III with no references  
- **Location:** §XII.B: “Paper II [4] and Paper III (both companion, not-yet-published works ...) provide independent discriminators...” and Reference [4].  
- **Problem:** Paper II is also “in preparation” and Paper III is cited in the prose but not in the reference list at all. No arXiv ID or journal is given, and no numerical result or methodology is verifiable. Yet they are invoked as part of a multi‑paper “bounce vs inflation discrimination program.”  
- **Required fix:** Either (a) remove all references to Paper III and any claims relying on it, and restrict discussion of Paper II to a high‑level, clearly speculative mention that does not support any quantitative conclusion; or (b) provide proper citations (arXiv IDs/DOIs) and ensure that any quoted statistics or methodological claims about those works are traceable in the cited documents. The reference list must include Paper III if it is named, or the text must stop naming it.

---

P5-B4 (ESSENTIAL) – Use of HuggingFace catalog revision as “immutable” citation without a proper archival identifier  
- **Location:** Abstract; §III.A; Appendix B  
- **Problem:** The paper refers to “HuggingFace catalog (bamfai/galaxy-chirality-catalog, immutable revision paper4-v1.0.122)” as if this were a scientific reference. HuggingFace revisions are not standard citable scientific identifiers (no DOI is given), and the revision string is not linked to any arXiv/ADS‑indexed document. The word “immutable” is a platform property, not a scientific provenance guarantee.  
- **Required fix:**  
  - Deposit the catalog corresponding to “paper4-v1.0.122” into a DOI‑granting repository (e.g., Zenodo) and cite it with a proper DOI, including exact version number.  
  - In the text, replace platform‑specific language (“immutable revision paper4-v1.0.122”) with a formal data citation including DOI and, if needed, a short note that this is the catalog used in Paper IV. Ensure that the version used here matches the version documented in Paper IV.

---

P5-B5 (ESSENTIAL) – EFT “toy operator” is explicitly not in cited sources but is framed as literature‑motivated  
- **Location:** Appendix A; References [1], [2]  
- **Problem:** The text states that the toy operator is “inspired by but not derived from the cited parity-violating-gravity literature” and explicitly that the operator is “not contained in either” [1] or [2]. Nonetheless, it is presented in a way that could be read as grounded in those works. Since the operator’s structure and scaling are new to this paper, it must not be seen as a direct statement *about* [1,2].  
- **Required fix:** Clarify the novelty and scope:  
  - Explicitly state that the operator is a new, ad hoc parametrization introduced in this paper for illustration, and that [1,2] do not contain it or its mapping to ∆fCW.  
  - Remove or rephrase any language that could mislead a reader into thinking [1,2] propose anything like this specific coupling or the bound |gϕ(∇ϕ)/H0|≲10⁻²/⟨|Δρ/ρbg|⟩.  
  - Ensure that [1,2] are only cited for general background on parity‑violating gravity and not as support for this specific operator.

---

P5-B6 (ESSENTIAL) – Abstract overstates robustness relative to what is actually proved  
- **Location:** Abstract  
- **Problem:** The abstract claims, e.g., “the CW fraction shows no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset...” and lists multiple nulls (“none reach 3σ after look-elsewhere correction”), culminating in “no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity.” However:  
  - The primary DESIVAST analysis is restricted to z≤0.24 BGS, not to all environments or redshift ranges in DR1.  
  - The V‑Web void sample is explicitly small (n=428) and contaminated by survey-edge artifacts, and this is only corrected by the DESIVAST re‑projection.  
  - Systematics from redshift-space distortions and selection-function correlations are acknowledged but not quantitatively controlled at the 10⁻³ level.  
- **Required fix:** Recast the abstract to state clearly the *conditional* nature of the null: e.g., “within DESI DR1, for the chirality‑relevant matched spirals and within the tested redshift range and smoothing scales, we find no statistically significant environment dependence above X pp after accounting for the Paper IV monopole and our estimated systematics.” Make explicit that the strongest, best‑controlled result is for DESIVAST void vs non‑void at z≤0.24, and that higher‑z and small‑void V‑Web tests are secondary and systematics‑limited.

---

P5-B7 (ESSENTIAL) – σ values from different null procedures and baselines are implicitly compared on a single scale  
- **Location:** Abstract, §V, §VI, §VII, §VIII.F, §IX, §X, §XI  
- **Problem:** The paper uses σ from several distinct constructions:  
  - “σfrom half” deviations from f=0.5.  
  - σpred based on the Paper IV monopole model (Eq. 1).  
  - z‑statistics from two‑sample tests (e.g., bright vs dark, |z|≈3.4σ).  
  - Label‑shuffle max‑stat σ distributions and Bonferroni σ thresholds.  
  These are repeatedly described simply as “σ” and occasionally juxtaposed in prose (“−5σ catalog-level signal,” “3.4σ filament sign-flip,” “none reach 3σ after look‑elsewhere correction”) without always restating which null or baseline is being used. That conflation risks reading these σ’s as directly comparable on a common significance scale, which violates the user’s instruction 7.  
- **Required fix:**  
  - Introduce a strict notation and enforce it consistently: e.g., σ½ for deviation from 0.5, σmono for deviation from the monopole-prediction model, z₂samp for two-sample z-tests, and σLEE for look‑elsewhere‑corrected thresholds.  
  - In any sentence where σ from different constructions are compared or referenced together, explicitly state the type (e.g., “2.1σ½,” “3.4σ₂samp,” “4.1σnull,max from label shuffle”).  
  - In the abstract and conclusions, avoid “σ” without a qualifier. State clearly which test and null each reported σ refers to.

---

P5-B8 (MAJOR) – T‑Web, ASTRA, and DESIVAST cross-checks: titles, arXiv IDs and status  
- **Location:** §IX.B, §X, §VIII, References , ,   
- **Problem:**  
  -  is cited as “preprint (2026), arXiv:2604.02463” with a descriptive title. This should be verified against arXiv and ADS for correct title, authors, and whether it is indeed only a preprint.  
  -  is cited as arXiv:2604.01456 and as a “Zenodo 10.5281/zenodo.19358024” dataset; these identifiers must be checked for consistency (title, author list, and whether the Zenodo DOI corresponds to the exact version used).  
  -  DESIVAST is cited as ApJ 982, 38 (2025), arXiv:2411.00148. Titles, author list, and ApJ volume/page must be checked against ADS.  
- **Required fix:**  
  - Verify via arXiv.org and NASA ADS that , ,  have the exact titles, author lists, journals/volumes/pages, and years claimed in the reference list. If any differ (e.g., updated titles, accepted journal versions), update the references accordingly.  
  - For , verify that the Zenodo DOI points to the exact version of the ASTRA catalog used, and note that version in the text if multiple exist.  
  - Confirm that DESIVAST  is indeed publicly released in DR1 form and that the void radii and counts quoted here match that paper / its data release.

*(I cannot perform the actual web lookups here; the author must do this carefully.)*

---

P5-B9 (MAJOR) – Shamir 2022 comparison not fully grounded in that paper’s numbers  
- **Location:** §XII.C; Reference [9]  
- **Problem:** Shamir 2022 is summarized as reporting “a ∼2–4% large-scale asymmetry on ∼1.3×10⁶ Ganalyzer-classified galaxies,” but the paper does not show where in [9] those precise ranges appear (e.g., abstract, a particular table, or figure). The comparison “an order of magnitude smaller than the Shamir 2022 amplitude” likewise needs to trace to a clearly defined statistic in [9] (e.g., a reported dipole amplitude, hemispheric asymmetry, etc.).  
- **Required fix:**  
  - Re-check [9] to identify the exact statistic and value that correspond to “2–4% asymmetry” and “∼1.3×10⁶ galaxies,” and cite the relevant part (e.g., “Shamir 2022 Table X reports an asymmetry of Y% on N galaxies...”).  
  - If [9] reports a different numerical range, adjust the text.  
  - Define precisely which asymmetry measure from [9] you are comparing to your ∼0.2 pp environment variation, so that “order of magnitude” is not ambiguous.

---

P5-B10 (MAJOR) – Over-reliance on internal “JSON artifact” and pipeline references, not accessible to readers  
- **Location:** §VI.D.b: “(sixteen-cell table, JSON artifact above)”; scattered “companion data repository” mentions; Appendix B  
- **Problem:** The paper references a “sixteen-cell table, JSON artifact above” and several analysis drivers “available in the companion data repository.” But no DOI, URL, or version for this repository is provided in the References; Appendix B only mentions “companion data repository” generically. This prevents independent verification of the decompositions and null tests claimed to support the main conclusions.  
- **Required fix:**  
  - Archive the analysis code, configuration files, and key derived tables (e.g., the 16‑cell z×density cluster table, Phase 2 sweep summary) in a public repository with a DOI (e.g., Zenodo, institutional archive).  
  - Add a formal data/software citation in the References and give the DOI and version in Appendix B.  
  - Replace vague phrases like “JSON artifact above” with precise references to files in that archived package (e.g., “see file `cluster_z_density_table.json` in [Data/Code ref]”).

---

P5-B11 (MAJOR) – Redshift-space distortion (RSD) caveats vs. strength of claims  
- **Location:** §VIII (RSD treatment), §XIII (Limitations)  
- **Problem:** The paper acknowledges that the V‑Web classification is done in redshift space and that anisotropic RSD can shift eigenvalues and class boundaries, and admits that a proper bound would require a reconstructed-position rerun. Nonetheless, strong null statements are made for environment dependence “at V‑Web resolution,” and the Phase‑2 sweep is interpreted as robust to Rs and λth. Without a quantitative RSD error propagation, these claims are somewhat overstated.  
- **Required fix:**  
  - Either perform a reconstructed-position V-Web classification (or at least a controlled mock-based RSD test) to quantify how class assignments and per-class fCW change, and include those numbers; or explicitly weaken the language around the V-Web-based conclusions, stating that they are conditional on redshift-space classification and that RSD could in principle induce class mixing at the ∼10⁻³ level.  
  - In the conclusions, highlight that the DESIVAST void/non‑void test is genuinely more RSD‑robust and that the V-Web statements are secondary and subject to this systematic.

---

P5-B12 (MAJOR) – Ambiguity in what is “primary” vs “secondary,” especially relative to abstract  
- **Location:** Abstract; §V.B; §VIII; §IX; §X; §XV  
- **Problem:** The text explicitly designates DESIVAST void vs non‑void as the primary analysis and V-Web, Tempel, ASTRA, etc., as secondary diagnostics. The abstract, however, leads with a V-Web‑centric description and then only later mentions “DESIVAST-anchored re-projection,” which can mislead readers into thinking the V-Web classification across 791k spirals is the main result.  
- **Required fix:**  
  - Reorder the abstract so that the DESIVAST void vs non‑void result at n=56,981 is clearly identified as the primary, most robust constraint, including its ∆fCW and σ.  
  - Describe the V-Web multi‑class results and the 791k sample as a secondary consistency check in the abstract, in alignment with §V.B.  
  - Likewise in §XV, ensure that the first sentence explicitly mentions that the headline claim is anchored on DESIVAST void vs non‑void, with V-Web and other classifiers providing consistency checks.

---

P5-B13 (MINOR) – Reference [8] Planck 2018 parameters: check exact numbers and use  
- **Location:** §III.C (Planck 2018 cosmology), various comoving conversions  
- **Problem:** The text uses “Planck 2018 [8] ... H0=67.66 km/s/Mpc, Ωm=0.315” for comoving distances. These values must match exactly what Planck Collaboration 2018 reports for the chosen baseline model. If a particular chain (e.g., TT,TE,EE+lowE+lensing) is used, that should be stated.  
- **Required fix:** Verify from Planck 2018 [8] that the H0 and Ωm values are correct for the specific cosmological parameter set used. If you use a different combination than Planck’s baseline TT,TE,EE+lowE, specify which one and adjust numbers as needed.

---

P5-B14 (MINOR) – Tempel et al. 2014 environment mapping  
- **Location:** §IX.A; Table XI; Reference   
- **Problem:** The mapping of Tempel multiplicity bins to {isolated, small group, filament like, cluster like} is plausible but not explicitly backed by a citation to Tempel’s own environment categorization thresholds (if any). Also, the claim of “0.2 pp spec” for concordance is internal; Tempel  does not define such a spec.  
- **Required fix:**  
  - Check Tempel et al. 2014 to see whether they propose particular richness thresholds for “groups,” “clusters,” etc. If so, align your mapping or explain deviations.  
  - Clarify that the 0.2 pp concordance “spec” is a threshold chosen in this paper, not something defined in . Phrase it as “we adopt a 0.2 pp concordance tolerance” rather than implying it is externally defined.

---

P5-B15 (MINOR) – Use of “json artifact above” and “immutable” reads like internal log language  
- **Location:** §VI.D.b (“JSON artifact above”); §II (“immutable HuggingFace revision paper4-v1.0.122”); Appendix B (provenance bullet list)  
- **Problem:** These phrases resemble internal version‑control or audit log language rather than standard paper prose. While not strictly incorrect, they harm clarity and will confuse readers who do not see the JSON or know what “immutable” means for HuggingFace.  
- **Required fix:** Replace with standard descriptions:  
  - “The full 4×4 z–density table is provided as a machine‑readable JSON file in the archived data package [Data ref].”  
  - “We use the catalog version corresponding to HuggingFace commit `<hash>`, archived as DOI:XXXX.”  
  - Avoid “immutable” unless you define what it means in this context.

---

P5-B16 (NIT) – Minor typos and phrasing  
- **Location:** Throughout; examples:  
  - Abstract: “σ void = −0.24 near-perfect null...” (missing comma after σvoid value).  
  - §II: “σfrom half” typeset in inconsistent ways.  
  - §VIII.B: “0/6 V-Web ‘void’ spirals inside any of the 101,863 DESIVAST VoidFinder holes at z ≤ 0.24” – consider rephrasing to “...are inside...”  
- **Required fix:** Run a careful proofread to standardize notation (σfrom half, fCW, etc.), add missing commas, and smooth awkward constructions.

---

P5-B17 (NIT) – Paper length vs. contribution  
- **Location:** Whole paper (20 pages main text plus appendices)  
- **Problem:** For a single-core result (environmental independence of chirality conditioned on Paper IV’s catalog), the paper devotes extensive space to multiple cross-checks, nulls, and internal bookkeeping. While this is scientifically laudable, the length is high relative to the net new contribution beyond Paper IV.  
- **Required fix:** Consider trimming by ~20–25% (e.g., target ~14–16 pages) by:  
  - Moving some of the more technical LEE derivations, detailed per‑cell sweeps, and repeated restatements of the primary vs secondary status entirely into an online supplement or data‑repository documentation.  
  - Shortening narrative explanations of null tests where the numeric content is already clearly shown in tables.

---

P5-B18 (NIT) – Appendix A gauge/rotation caveats vs main-text prominence  
- **Location:** Appendix A  
- **Problem:** The toy EFT mapping is heavily caveated as non‑gauge‑invariant and non‑covariant, and not used anywhere in the main analysis. Its presence may distract from the observational focus, especially if not clearly marked as speculative.  
- **Required fix:** Precede Appendix A with a brief one‑sentence disclaimer (“This appendix is purely illustrative and does not enter any of the data analysis or conclusions in the main text”). Ensure that nothing in the conclusions depends on the bound written there.

---

## Summary recommendation
**MAJOR REVISIONS**

The central empirical message—that, given the Paper IV chirality catalog, DESIVAST void vs non‑void and V-Web classes show no significant environment dependence at current sensitivity—appears internally consistent. However, too many key inputs are anchored in unpublished companion papers and platform‑specific revisions that cannot be externally verified; σ values from different nulls are conflated in notation; and several literature comparisons (Shamir 2022, Planck 2018, Tempel 2014, T‑Web/ASTRA/DESIVAST) need careful cross‑checking of metadata and statistics. The paper should only proceed once the catalog provenance and companion-paper claims are properly exposed via public identifiers, the σ notation is disambiguated, and the abstract and conclusions are aligned with what is demonstrably proved under the stated systematics.