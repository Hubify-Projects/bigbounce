# P5 R28conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.59.pdf` md5=3a80c50b pages=28
**Input format**: TEXT + web search + pass-2 self-critique (6589 chars)
**Wall time**: 96.5s

---

P5-E1 (ESSENTIAL)  
Section: Abstract, p.1  
Problem: The paper repeatedly cites “Paper IV [3] (companion work, not yet peer-reviewed)” as the sole source of the 8.47M-galaxy chirality catalog, the classifier-monopole offset ∆fCW = −0.0026, and key claims about selection-function systematics, yet [3] is listed in the references as a normal journal-style citation (“companion paper (Paper IV), in preparation; manuscript in preparation.”). There is no arXiv ID or published venue. PRD will not accept a cosmology paper whose entire data product and dominant systematic error budget rests on an unpublished, unavailable, single-author “in preparation” manuscript.  
Required fix: Either (i) provide a public, citable release of Paper IV (at minimum, an arXiv preprint with stable versioning containing the catalog description, classifier architecture, validation, and the monopole estimate) and update the reference entry accordingly (title, arXiv ID, and version), or (ii) move all essential catalog construction and monopole-estimation material into this paper in enough technical detail to stand alone, and relabel [3] clearly as an internal companion with no load-bearing claims. As written, the paper relies on unverifiable external work.

P5-E2 (ESSENTIAL)  
Section: Abstract + §V (Statistical Methods), p.1,5–6  
Problem: The abstract states “The quoted σfrom half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n.” This important qualification appears only once and is later effectively undermined by free comparison of raw σfrom half values across classes (e.g., “The cluster σfrom half = −4.66 is the strongest single-class signal,” §VI D) without explicit restatement that these σ are not directly comparable and are dominated by the catalog monopole. PRD instruction 7 requires every juxtaposition of σ from different null procedures (or, here, different sample sizes) to carry an explicit “not directly comparable” qualification.  
Required fix: At every place where σfrom half for different classes or bins are compared side-by-side (e.g., Table II + Fig. 3, Table IV, Table VI, Table VII, Table VIII, Table XII, discussion paragraphs in §VI A–D, §VII, §VIII B–D, §X, §XI, §XII), explicitly restate that raw σfrom half are not directly comparable across bins because of √n scaling, and that only monopole-subtracted residuals or properly normalized tests are to be interpreted as evidence. Where “strongest signal” language is used, replace it with a statement framed in terms of residuals after monopole subtraction.

P5-E3 (ESSENTIAL)  
Section: Abstract, p.1  
Problem: The abstract’s headline quantitative claim for the DESIVAST void re-projection is “n = 56,981, ∆fCW = 0.0007.” In §VIII B and Table VII (p.15–16) the reported values are nvoid = 56,981, fCWvoid = 0.4964 and fCWnon−void = 0.4971, implying ∆fCW ≡ fnon−void − fvoid = +0.0007, consistent in magnitude and sign. However, the abstract later references “∆fCW = 0.0007” without explicitly stating the sign convention, and other sections flip sign conventions (e.g., Table VIII defines ∆fCW ≡ fnon−void − fvoid, but some discussion prose reads as fvoid − fnon−void). This makes it ambiguous whether the voids are higher or lower than the control.  
Required fix: Enforce a single, explicit sign convention for ∆fCW throughout (e.g., ∆fCW ≡ fCW,non−void − fCW,void), state it clearly in §VIII B at equation level, and ensure the abstract and all tables/figures use the same convention. Rephrase the abstract to “∆fCW ≡ fnon−void − fvoid = +0.0007” (or the chosen sign) to avoid any implied sign ambiguity.

P5-E4 (ESSENTIAL)  
Section: Throughout text, esp. §V B, §VIII, §IX, Appendix B, p.6–7, 14–27  
Problem: The manuscript contains extensive version-history and internal audit language (e.g., “An earlier draft quoted… are withdrawn”, “r24conf”, “v0151”, “v0.1.59-2026-06-11”, “RSD-robustness argument applies…”, references to specific JSON files and pipeline paths). These are internal provenance tags, not suitable for a PRD article, and violate instruction 8.  
Required fix: Remove all references to earlier drafts, internal filenames, run IDs, JSON filenames, Git paths, and “rXXconf” style tags from the body. Replace them with concise descriptions of the final analysis only. If reproducibility resources are to be referenced, they should be summarized in one data-availability section with a single permanent archive/DOI, not as inline file names.

P5-E5 (ESSENTIAL)  
Section: References, refs. [1]–, p.27–28  
Problem: Several references are clearly incomplete or fused: [3] and [4] are “companion paper… in preparation; manuscript in preparation” with no arXiv ID or journal;  and  are described as “preprint (2026), arXiv:2604.02463” and “(2026), arXiv:2604.01456” — these arXiv IDs lie in the future relative to arXiv’s current allocation and cannot be verified;  has an ApJ 982, 38 (2025) reference with arXiv:2411.00148 which does not currently map to a DESI voids paper on NASA ADS; [8] is “Planck Collaboration, 2020 A&A 641 A6” but no arXiv ID is listed;  Walmsley et al. 2023 MNRAS 526, 4768 is plausible but needs verification (title and arXiv).  
Required fix: For each reference:  
– Verify via arXiv.org and NASA ADS that the arXiv ID, title, author list, journal, volume, page, and year match the cited paper.  
– Remove any fabricated or future-dated arXiv IDs; if the paper is still in submission with no arXiv, cite as “submitted” without an arXiv number and avoid relying on unpublished quantitative claims.  
– For DESIVAST , supply the actual ApJ citation and correct arXiv ID (or state “in press” if appropriate).  
– For the concurrent DR1 web papers , , either supply valid arXiv IDs or treat them as “private communication / internal DESI note” and remove their use in any load-bearing quantitative comparisons.  
– Ensure every quoted statistic attributed to these works (volume fractions, void counts, etc.) can be found in the cited paper’s abstract or tables.

P5-E6 (ESSENTIAL)  
Section: §IV A Algorithm, eqs. for Φ and Tij, p.4–5  
Problem: Dimensional consistency and sign conventions: the text states Φ(k) = −δk/k^2 and Tij(k) = −ki kj Φ(k) with ∂i∂j ↔ (ik_i)(ik_j) = −k_i k_j, then asserts this gives Tij(k) = +k_i k_j δ_k/k^2. With that sign, the eigenvalue threshold λth = 0 is said to reproduce standard volume fractions. However, no explicit units are given for Φ, δ, and Tij, and the derivation assumes a particular Fourier convention. For PRD standards, a cosmology methods paper must spell out the convention and show that the Poisson normalization is consistent.  
Required fix: Add a brief derivation with explicit Fourier convention: define δ(x), Φ(x) with Poisson equation ∇^2Φ = 4πG a^2 ρ̄ δ, write the Fourier transforms with your convention, and derive Φ(k) and Tij(k) including constants. Then note that you drop overall constants for classification and keep only relative eigenvalue ordering. Verify and state the units of Φ and Tij (e.g., dimensionless after rescaling) and show that λth = 0 is defined on that dimensionless normalization.

P5-E7 (ESSENTIAL)  
Section: §V A Look-Elsewhere, eq. (3), p.6  
Problem: The look-elsewhere correction formula p_LEE = (1 + #{k : |σ|max^(k) ≥ |σ|max^obs})/(1 + N_MC) is reasonable, but the paper repeatedly compares p_LEE to Bonferroni thresholds as if they were equivalent without clearly defining which p-values are pre-registered primary tests and which are post-hoc. This is a multiple-testing and forking-paths issue; PRD will reject if the statistical decision framework is ambiguous.  
Required fix: Explicitly specify in §V which tests are pre-defined primary hypotheses (e.g., DESIVAST void vs non-void) and which are exploratory. For primary tests, define a clear α (e.g. 0.01) and say whether you control family-wise error via Bonferroni or via the empirical max-statistic. For all secondary scans, rephrase results as descriptive (e.g., “no bin exceeds 3σ”) without using language implying formal hypothesis rejection. Clarify that the DESIVAST void null is the only load-bearing result, and that all other p-values are confirmatory diagnostics.

P5-E8 (ESSENTIAL)  
Section: §VIII A, p.15; Table VII, p.16; Abstract, p.1  
Problem: The DESIVAST point-in-sphere algorithm is described only qualitatively (“k=20 KDTree”, “we re-ran unbounded”). The void membership classification is crucial to the main scientific conclusion, yet there is no precise mathematical specification and no error estimation for membership near void boundaries.  
Required fix: Provide a clear algorithmic definition of DESIVAST void membership: exact coordinate system, metric, sphere centers and radii (referencing specific DESIVAST columns), and the criteria for “inside any hole”. Quantify the fraction of spirals that lie within one radial bin of a void boundary and estimate how sensitive ∆fCW is to ±Δr perturbations (beyond the quoted Gaussian line-of-sight perturbations). This needs at least one concise table or figure giving boundary statistics and confirming that boundary uncertainty cannot produce |∆fCW| ≳ 0.002.

P5-E9 (ESSENTIAL)  
Section: General length and scope, entire paper (28 pp)  
Problem: For the stated contribution — a null test of environment-dependent chirality conditioned on a pre-existing classifier and a published DESI void catalog — the paper is excessively long and reads more like an internal analysis note than a focused PRD article. There is heavy repetition of similar nulls (multiple V-Web configurations, Tempel, ASTRA, HEALPix scans, redshift/density splits, etc.), many of which add marginal value beyond the primary DESIVAST analysis and could live in a supplementary document. PRD expects concision commensurate with the conceptual advance.  
Required fix: Reduce the main text to ≤ 18 pages by:  
– Keeping the catalog definition, V-Web description (one canonical configuration plus a single robustness sweep), DESIVAST void re-projection, and the key bright/dark systematic.  
– Moving most secondary cross-checks (Tempel, ASTRA per-object, detailed HEALPix maps, many z-shell and density decompositions, and the toy EFT mapping) into an online appendix or a data-release note.  
– Eliminating repeated descriptions of the same pipeline and internal filenames. Focus the main paper on the core methodology and the DESIVAST-based null.

P5-M1 (MAJOR)  
Section: Abstract vs body, first paragraph and headline results, p.1 vs. §§III–VIII  
Problem: The abstract compresses a complex sample ledger (“16.4 × 10^6 ZWARN=0 input rows… 2,232,212 unique galaxies… 791,635 chirality-relevant… 812,793 env-labeled rows… 56,981 void spirals”) into a single paragraph. These numbers are important and must be internally consistent. Re-deriving: Table I gives 16,361,731 DR1 rows; §III B says that is the post-cut value used; §III D gives 2,232,212 matched primaries and 791,635 chirality-relevant; §VI A gives 812,793 env-labeled rows covering 783,820 unique spirals; §VIII B gives 678,945 z≤0.24 spirals and 56,981 DESIVAST voids. These are consistent, but the abstract’s “783,820 unique chirality-relevant matched spirals (791,635 minus 7,815 without an environment row)” is never shown explicitly in a table, and the 7,815 count is buried. This obscures the selection and could mislead readers.  
Required fix: Add a compact “sample ledger” table early in the paper (e.g., end of §III) listing all key counts: initial DR1 post-cuts, matched primaries, chirality-relevant, env-labeled rows vs unique spirals, z≤0.24 subset, and DESIVAST void vs non-void counts. Ensure the abstract’s ledger phrasing is numerically identical to that table. State explicitly which objects are excluded at each step and why (e.g., missing env row).

P5-M2 (MAJOR)  
Section: §VI A headline V-Web table and Fig. 3, p.7–8  
Problem: Table II and Fig. 3 present the V-Web class fCW and σfrom half as a “headline” result, but the paper later argues that this table is dominated by the Paper IV classifier monopole and is secondary to DESIVAST. Without that later context, a reader could misinterpret the −4.66σ cluster deviation as evidence for an environment effect.  
Required fix: Immediately under Table II / Fig. 3, add text explicitly stating that (i) these σfrom half are entirely consistent with the Paper IV monopole when scaled by √n, (ii) the V-Web void sample is tiny and contaminated by edge artifacts, and (iii) therefore this table is treated as a diagnostic, not the main scientific conclusion. Insert a pointer to §VIII for the primary DESIVAST result.

P5-M3 (MAJOR)  
Section: §VI D “Filament-class within-class decomposition” and bright vs dark discussion, p.10–11  
Problem: The bright/dark filament and cluster splits show |z| ≈ 2.0–2.1 two-sample differences in opposite directions. The text couches these as “residual structure that current data do not allow us to cleanly partition” but leans toward a BGS-selection-function explanation without quantitative modeling. There is a risk of over-interpreting sub-3σ differences in a heavily multi-tested setting.  
Required fix: Either (i) perform a simple quantitative model showing that the observed bright/dark difference is compatible with the known per-leg systematics reported in Paper IV (e.g., by propagating leg-specific monopoles through the bright/dark mix), or (ii) explicitly downgrade these bright/dark differences to anecdotal hints and clearly label them as exploratory with no bearing on the main null. In either case, avoid any suggestion that this constitutes evidence for an astrophysical effect.

P5-M4 (MAJOR)  
Section: §XII C Comparison to Shamir 2022, p.25  
Problem: The comparison to Shamir (2022) claims that the present null “leaves no room for a residual environment-dependent chirality of the Shamir 2022 amplitude” based on per-class ranges. However, Shamir’s reported asymmetry is a full-sky dipole/hemispheric asymmetry, not explicitly conditioned on environment class, and nothing in this paper analyzes chirality as a joint function of environment and sky direction in a way that exactly matches Shamir’s tests.  
Required fix: Rephrase the comparison to Shamir more carefully: make clear that you rule out an environment-conditional effect at the 2–4 pp level in well-populated classes, but that this does not by itself resolve the global anisotropy claims, which are addressed in Paper IV. Remove phrases like “no room” and replace with precise numerical upper bounds; add a caveat that the tests differ in design.

P5-M5 (MAJOR)  
Section: Appendix A “Toy EFT mapping”, p.27  
Problem: The toy EFT coupling L_parity ⊃ g_ϕ (∇ϕ)(∇ρ/ρ_bg)(L̂·ẑ) is not supported by any of the cited EFT literature [1,2]. The text acknowledges this, but the derivation of the “order-of-magnitude bound” |g_ϕ ∇ϕ/H0| ≲ 10^−2/⟨|Δρ/ρ|⟩ is not actually computed from the data in any explicit way. Given PRD’s standards in theoretical cosmology, this section reads speculative and could mislead readers into thinking a genuine operator-level constraint has been derived.  
Required fix: Either (i) remove Appendix A entirely, or (ii) drastically shorten and clearly label it as a non-rigorous illustrative parametrization, dropping any inequality that resembles a constraint and any mention of “bound”. If retained, add a disclaimer at the start that no EFT constraint is claimed, only an illustration of how such a model would need to accommodate a null in ∆fCW.

P5-M6 (MAJOR)  
Section: §III C “Cross-match method” and Table I, p.3–4  
Problem: The cross-match uses 1″ radius on coordinates that are derived from the same imaging catalog, leading to a median separation of 0.0066″ and 99th percentile 0.30″. The paper acknowledges this is dominated by shared coordinate provenance, but there is no quantitative estimate of the false-match rate (chance alignments, especially for high-z, small-galaxy tail). PRD readers will expect at least a rough contamination estimate.  
Required fix: Provide an estimate (analytic or via randomized catalogs) of the expected number of spurious matches at 1″ given the source density and spatial distribution, and show that varying the match radius over the reported range changes fCW by < some small tolerance (you already claim ≤4% in matched-primary rows; you need the impact on chirality fractions per environment). Present a concise table of fCW vs radius to support the statement that the science results are insensitive to this choice.

P5-M7 (MAJOR)  
Section: §IX A “Randoms-weighted rebuild” and z-shell corrections, p.20–21  
Problem: The completeness-weighted rebuild and z-shell correction analysis are very detailed, but crucial algorithmic elements (random catalog properties, FKP-like weights, treatment of empty cells) are only sketched. Since you use these to argue robustness of environmental labels, PRD standards demand more transparency.  
Required fix: Add a concise description of the randoms catalog (what DESI random product, how many points, what weights) and the exact formula for δ_w = n_g/(α n_r) − 1, specifying how you handle cells with zero randoms or galaxies. For the z-shell correction, tabulate the number of galaxies and mean density per shell, and show that the shell-corrected class fractions remain within statistical errors of the canonical case. This can be done in a compact table.

P5-M8 (MAJOR)  
Section: §X ASTRA cross-validation, Table XII, p.23–24  
Problem: ASTRA and V-Web disagree strongly on per-galaxy labels in the EDR overlap, yet this is only qualitatively discussed. The ASTRA result is then used as a “strong robustness result.” Given the small overlap (N ~ 2.5×10^4) and classifier disagreement, the independent weight of this check is modest.  
Required fix: Quantify classifier agreement: provide a confusion matrix between ASTRA argmax and V-Web for the overlap, including effective per-class n. Rephrase the conclusion to emphasize that ASTRA supports the null but, because of label disagreement and limited coverage, it does not materially tighten constraints beyond DESIVAST.

P5-M9 (MAJOR)  
Section: Figures (Fig.1–9), various pages  
Problem: Several figures (especially Figs. 6, 8, 9) are heavy for the marginal insight they provide and, for PRD typesetting, must be justified. For example, Fig. 6 shows an NSIDE=32 σ map but adds little beyond the statement “no coherent pattern”; Fig. 9 replicates information largely contained in Table XI.  
Required fix: Consider removing or moving to supplementary material the lower-value figures (likely Fig.6, Fig.8, possibly Fig.9) and ensure that the remaining figures have clear, quantitative axes (with units), readable labels, and directly support key claims. Each figure caption should explicitly connect to a specific result in the text (e.g., “used to support the sky-coherence null in §VI E”).

P5-Min1 (MINOR)  
Section: Throughout, especially abstract and §VI–VIII, p.1,7–18  
Problem: The prose is dense and full of internal jargon (“Phase 2 sweep”, “closure-wave recompute drivers”, “artifact outputs/…”). This strongly reduces accessibility for the general PRD readership.  
Required fix: Edit for clarity: remove internal pipeline terms from the main narrative, replacing them with simple descriptions (“we reran the classification with these parameters”). Reserve technical implementation details for a short data-availability section or supplementary note.

P5-Min2 (MINOR)  
Section: §III B, Table I, p.3–4  
Problem: The description of the DR1 “input rows” being post-cut could mislead some readers into thinking 16.36M is an official DESI DR1 constant, which you later say explicitly it is not.  
Required fix: In Table I and §III B, explicitly label 16,361,731 as “this work’s DR1 zall selection after ZWARN, SPECTYPE, and redshift cuts; not an official DR1 constant.” This avoids potential misinterpretation.

P5-Min3 (MINOR)  
Section: §IV B, Fig. 2, p.4–5  
Problem: Fig. 2 caption claims the cluster volume fraction (1.0%) is “consistent with the high-density tail expected at this smoothing scale.” This is true in broad terms, but you cite no source.  
Required fix: Either provide a reference (e.g., Hahn et al. 2007 or Cautun et al. 2014) with comparable void/wall/filament/cluster fractions, or soften the statement to “typical of tidal-tensor classifications at this smoothing scale” without implying a precise theoretical expectation.

P5-Min4 (MINOR)  
Section: §VIII D “Catalog-native V2 membership”, p.16–17  
Problem: The description of the zone-indexing defect (NGC+SGC concatenation without offset) is useful, but the detailed recounting of wrong numbers in earlier drafts is not needed.  
Required fix: Compress this to a simple statement: “A zone-indexing bug in an earlier join undercounted V2 void members; all results quoted here use the corrected join.” Drop the exact obsolete n and σ values.

P5-Min5 (MINOR)  
Section: Appendix B (Data and code availability), p.27  
Problem: The repository path “Hubify-Projects/bigbounce” and version tag “v0.1.59-2026-06-11” look like internal names. For publication, PRD prefers stable archival identifiers.  
Required fix: Before acceptance, deposit the analysis code and key artifacts in a long-term archive (e.g. Zenodo) and cite the DOI in Appendix B. Keep GitHub as a convenience but ensure that the primary reference is a DOI.

P5-N1 (NIT)  
Section: Title, p.1  
Problem: The title is very long and somewhat unwieldy (“Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across 791,635 DR1 Matched Spirals”).  
Required fix: Consider shortening to something like “Environmental Dependence of Spiral Chirality in DESI DR1: DESIVAST Void and Tidal-Tensor Tests” and move the detailed counts to the abstract.

P5-N2 (NIT)  
Section: Footnote a in Introduction, p.2  
Problem: The footnote explains the T-Web nomenclature but mixes notation (“Tij = ∂^2Φ/∂xi ∂xj”) and commentary. Minor stylistic issue.  
Required fix: Consider moving the definition of T_ij into §IV A as a proper equation and keep the footnote purely about nomenclature.

P5-N3 (NIT)  
Section: Throughout  
Problem: Occasional duplicated or awkward phrases, e.g., “canonical chirality catalog” vs “canonical labels” interchanged; “per-galaxy CW/CCW labels we test here; we make no independent classification” could be tightened.  
Required fix: Light copy-editing pass to remove minor redundancies and ensure consistent terminology.

## Summary recommendation

REJECT

The central scientific idea — testing spiral chirality for environmental dependence using DESI DR1 and DESIVAST voids — is interesting and potentially suitable for PRD, and the analysis is technically ambitious. However, the manuscript in its current form relies heavily on an unpublished companion paper for the core catalog and systematics, contains unverifiable or future-dated citations, embeds extensive internal versioning/logging prose unsuitable for a journal article, and is significantly overlength relative to its conceptual contribution. Addressing the essential and major issues would require substantial restructuring, clarification of the statistical framework, externalization of key catalog details, and cleanup of the reference list and narrative. A fresh submission, after these issues are resolved and the companion catalog paper is publicly available, would be more appropriate than a revision within this review cycle.

---

## PASS 2 — self-critique findings (what initial review missed)

[P5-E10] The abstract and results contain at least one **arithmetic inconsistency** in the void-reprojection counts: the paper states \(n_{\text{void}}=56{,}981\) and \(n_{\text{non-void}}=621{,}964\) in Table VII, which sum to 678,945, matching the stated \(z\le 0.24\) sample size; however, the same section later says the “exact rerun moves 100 galaxies” and that the void count rises from 56,981 to 57,081, but the table still reports the original 56,981 and the abstract keeps \(n=56{,}981\). This is not wrong by itself, but the paper never clearly distinguishes **catalog-native** vs **rerun** counts in the headline narrative, so the same analysis is described with two different \(n_{\text{void}}\) values without an explicit “baseline vs exact rerun” qualifier in the abstract or table captions. [No citation]

[P5-M10] The **sign convention** for the DESIVAST void result is internally inconsistent in the prose around Table VII/ VIII. Table VIII explicitly defines \(\Delta f_{\mathrm{CW}}\equiv f_{\mathrm{CW,non-void}}-f_{\mathrm{CW,void}}\), but elsewhere the text says “\(\Delta f_{\mathrm{CW}} = -0.06\) pp” for the maximal-sphere variant while discussing the same void/non-void ordering, and the sign flips again in the surrounding prose. The main result is numerically small either way, but the paper should use one convention everywhere and restate it in every caption that quotes \(\Delta f_{\mathrm{CW}}\). [No citation]

[P5-M11] The **look-elsewhere p-values** in the Phase 2 sweep and sky scans are not always presented consistently with the reported Monte Carlo resolution. The paper states \(N_{\mathrm{MC}}=1000\), so the Monte Carlo standard error is about \(0.01\) near \(p=0.5\), yet Table V reports values like \(p=0.135, 0.413, 0.607\) to three decimals and later treats differences of order \(0.01\)–\(0.02\) between “free” and “stratified” reruns as meaningful. Those differences are at or below the quoted Monte Carlo uncertainty, so the paper should not imply that such small changes are substantive. [No citation]

[P5-M12] The equation for the **density proxy** is dimensionally underexplained in the main text. The paper defines \(\delta=\rho/\bar{\rho}-1\), smooths it, and then uses \(\log_{10}(1+\delta_{\text{smooth}})\) as the per-galaxy covariate, but it never states in the equation block that this quantity is dimensionless and monotonic in \(\delta_{\text{smooth}}\). The surrounding prose later relies on quartile equivalence between the log transform and the linear density, so that equivalence should be stated directly where the variable is introduced. [No citation]

[P5-M13] The paper’s **cross-reference chain** between §VIII C, §VIII D, and Table VIII is easy to misread and appears internally overloaded. §VIII C says “the same null verdict” for all three DESIVAST algorithms, but §VIII D then introduces catalog-native V2 membership as a separate cross-check with different \(n_{\text{void}}\) values and later claims the earlier draft values were caused by a zone-indexing defect. The result is that a reader cannot tell, from the section references alone, which numbers are the final authoritative ones without reading several paragraphs forward and backward. The paper needs a clearer distinction between “public catalog-native membership,” “point-in-sphere hole-union membership,” and “older withdrawn values.” [No citation]

[P5-M14] The **abstract is not fully faithful** to the body in one important respect: it presents the DESIVAST result as a simple “\(n=56{,}981, \Delta f_{\mathrm{CW}}=0.0007\)” headline, but the body immediately qualifies that this comes from a void/non-void split on a z-limited matched subset, that the exact rerun changes the void count to 57,081 and \(\Delta f_{\mathrm{CW}}\) to \(+0.0006\), and that the catalog-native V2 algorithms return different void sample sizes and different \(\Delta f_{\mathrm{CW}}\) values. The abstract therefore compresses three slightly different DESIVAST variants into one headline number without warning the reader that the exact count and offset depend on which void definition is used. [No citation]

[P5-M15] The paper repeatedly compares **raw \(\sigma_{\text{from half}}\)** values across classes, but one more place needs the “not directly comparable” qualifier: Table XI for the Tempel cross-validation. The Tempel isolated class has the largest \(|\sigma|\) simply because it is the largest Tempel class with the strongest imbalance relative to the null, while the V-Web overlap classes have very different \(n\) and class-definition support. Even though the text says the V-Web and Tempel class labels are only approximately matched, the table layout still invites direct visual comparison of the \(\sigma\) values. This should be annotated more explicitly at the table level. [No citation]

[P5-M16] The **ASTRA overlap** section appears to overstate its independence. The paper says the ASTRA EDR overlap is a “per-galaxy cross-check” and then later notes that V-Web and ASTRA disagree strongly on labels because the V-Web 25.9 Mpc/h grid is comparable to the EDR rosette scale. That means the overlap is not a clean independent validation of environment assignment in the way the prose initially suggests; it is primarily a consistency check that both classifiers still give a null for chirality. The section should soften the implied strength of the validation claim. [No citation]

[P5-M17] The **systematics table** in §XI contains a potential stale-number issue: the text says the match-radius sweep is “flat to 0.02 pp across \(\{0.5,1,2,3,5\}''\),” but Table XIII only explicitly lists the 0.5″ and 5.0″ rows. The intermediate radii are referenced in prose but not shown in the table, so the reader cannot verify the 0.02 pp claim from the table itself. Either the table should include all radii or the prose should say that the intermediate values are available only in the artifact. [No citation]

[P5-M18] The paper’s **length/scoping** problem is still stronger than the original review suggests because several sections are not just supplemental but effectively duplicate the same null claim in different language. In particular, §VIII F, §IX A, §XI, and §XV each restate the same catalog-monopole-vs-environment conclusion with nearly identical numerical examples. That repetition makes it harder to see which result is actually primary and which are support checks; consolidating those passages would materially improve readability and reduce the chance of readers treating secondary diagnostics as independent discoveries. [No citation]