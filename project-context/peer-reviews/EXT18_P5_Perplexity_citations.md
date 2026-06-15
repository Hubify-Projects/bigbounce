# P5 EXT18 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=7bb73989 pages=32
**Input format**: TEXT + web search + pass-2 self-critique (17806 chars)
**Wall time**: 96.6s

---

The manuscript, as provided, cannot be evaluated to Physical Review D standards for citation and statistical forensics because you have not supplied the reference list / bibliography pages, and I do not have actual access to the PDF or its reference section beyond the in‑text citation stubs. I therefore cannot perform the core parts of the requested task (checking arXiv IDs, DOIs, titles, venues, years, or tracing quoted statistics to specific tables/figures in the cited literature) to the level you describe.

Given only the body text, I can still identify several publishability‑blocking issues and structural problems that PRD would require to be fixed.

Below I treat the current text as if it were the complete manuscript and apply your requested audit categories.

---

## ESSENTIAL ISSUES

### P5‑E1 – “In preparation” companion papers as load‑bearing inputs  
- **Location**: Abstract, p.1; Sec. I, p.3; Sec. II, p.3; references [3], [4].  
- **Problem**: Paper IV (“A Survey‑Scale Chirality Catalog…”) and Paper II (“fNL = −35/8 Forecast…”) are repeatedly cited as *companion papers in preparation* and are clearly load‑bearing: Paper IV provides the 8.47M‑galaxy chirality catalog, the monopole offset, and the dipole null; Paper II is said to supply theoretical context and discrimination power. The current paper states it “treats [Paper IV’s] catalog and quoted monopole offset as inputs whose uncertainty is propagated,” but there is no self‑contained, fully specified description of the catalog construction, selection function, or classifier systematics. The chirality catalog lives on HuggingFace, not in a citable journal or arXiv entry, and the only detailed description is explicitly deferred to Paper IV. This violates the standalone‑reader requirement and PRD standards for reproducibility.  
- **Required fix**:  
  - Either (a) ensure that Paper IV is publicly available on arXiv with a stable identifier and that this manuscript’s description of the catalog is explicitly sufficient for a PRD reader to reproduce all *load‑bearing* aspects (label definition, classifier architecture, training set, augmentation scheme, quality cuts, monopole estimation procedure), or (b) move the necessary catalog and classifier description into this paper itself, so this article does not rely on an unpublished “in preparation” manuscript for its core data product.  
  - Remove reliance on Paper II for any claims of theoretical discrimination; if such discrimination is important, summarize the relevant model assumptions and results directly and cite a citable preprint.

### P5‑E2 – Version‑history / internal‑audit language in the body  
- **Location**: Sec. II, p.3.  
- **Problem**: The text contains explicit version‑history language about Paper IV, e.g. “Paper IV’s current headline (v1.0.166) … an earlier harmonic-space subsample-mask MASTER-deconvolved ℓ = 1 statistic was withdrawn in Paper IV v1.0.166 after a provenance audit traced its mask to a synthetic footprint.” This is internal audit / revision history prose that belongs in a methods note or a data‑release technical report, not in the body of a PRD paper. It also references a specific internal git‑like version tag, which is a moving target and not suitable as a scientific citation surface.  
- **Required fix**:  
  - Remove explicit version numbers (v1.0.166) and internal audit narrative from the main text, or compress it to a brief, neutral statement that the earlier harmonic‑space result was superseded by the current real‑space dipole result, with a proper reference to the final public version of Paper IV.  
  - If the provenance audit materially justifies why the harmonic‑space statistic is invalid, summarize the key technical point once, in controlled language, or move the detailed versioning discussion to an appendix clearly marked as historical context.

### P5‑E3 – Standalone‑reader / self‑containment failure for core data product  
- **Location**: Sec. III A (Chirality catalog), p.3; widespread references to Paper IV.  
- **Problem**: The chirality labels are central to every analysis in the paper. However, the description is extremely minimal: readers are told it is a “ViT‑Small classifier with Z2 test-time augmentation” providing {CW, CCW, NS}, but there is no architectural definition, no description of the training data, training loss, label curation, augmentation procedures, or failure modes. The text repeatedly says “see pipelines/p2_chirality/” and “catalog and methodology to be detailed separately,” which is not acceptable for a PRD article whose main result depends on that catalog.  
- **Required fix**: Add a fully specified summary, sufficient for an independent reader to recreate or at least critically evaluate the classifier: architecture class, training sample definition and size, training labels (source, possible biases), augmentation scheme, how equivariance is enforced, which cuts define the “chirality‑relevant” subset, and how the 0.4974 ± 0.000279 monopole was estimated. Provide at least an arXiv‑style methodological appendix if space is an issue.

### P5‑E4 – Abstract claims rely on Paper IV without proper caveats and cross‑referencing  
- **Location**: Abstract, p.1; Sec. II, p.3; Sec. XII C (Shamir comparison), p.28.  
- **Problem**: The abstract treats the Paper IV monopole (∆fCW ≈ −0.0026) and dipole null as secure, established inputs, but the body later clarifies that Paper IV is “in preparation” and that its harmonic‑space statistic was withdrawn after a provenance audit. There is no explicit, early caveat that the chirality catalog and its monopole constraint are themselves provisional and subject to revision. This violates your pattern‑045 “abstract‑last drift” requirement.  
- **Required fix**:  
  - In the abstract, explicitly qualify every statement that depends on Paper IV as relying on a companion catalog whose construction is described either in this paper (if you fix P5‑E3) or in an accepted / submitted companion with a stable arXiv ID.  
  - Downgrade language such as “known Paper IV catalog‑wide classifier‑monopole systematic” to make clear that this is an *estimated* systematic with its own uncertainty, not a fixed constant.  
  - Ensure every quantitative abstract claim traceable to Paper IV has an explicit body reference showing how its uncertainty is propagated.

### P5‑E5 – Multiple internal pipeline paths and “analysis tree” without clear preregistration or control of garden‑of‑forking‑paths  
- **Location**: Sec. V B (Primary vs secondary analysis paths), p.7–8; Table II.  
- **Problem**: The paper introduces an elaborate “analysis tree” and admits that the “choice of which classifier to report as ‘primary’ is made post‑hoc,” then attempts to control this via Bonferroni corrections over selected families. For PRD, this is not inherently disqualifying, but several key inferences (e.g. the designation of DESIVAST as primary, and the structure of density and sky scans) are presented as if they were pre‑planned, even though they are clearly exploratory. The analysis‑tree description is long, but it does not *fully* specify the forking paths that were explored and discarded (e.g. grid‑resolution variations, alternative λth choices, different masks).  
- **Required fix**:  
  - Either (a) simplify the inferential structure to a small, clearly defined set of primary tests plus descriptive diagnostics, with a single global multiple‑testing control, or (b) move the full forking‑path discussion to a supplemental technical note and be absolutely explicit in the main text that the environment null is an *exploratory* result on a complex multi‑test tree.  
  - Remove any language that suggests a pseudo‑preregistration that did not in fact occur.

### P5‑E6 – Redshift‑space distortion (RSD) impact only qualitatively handled, yet headline is framed as a strong constraint  
- **Location**: Abstract, p.1 (discussion of “redshift‑space statement”); Sec. VIII (RSD for DESIVAST), pp.17–18; Sec. XIII (Limitations), pp.28–29.  
- **Problem**: You acknowledge RSD, but the treatment is qualitative and relies on scalar σv /(aH) arguments and a Monte‑Carlo radial jitter for DESIVAST void membership. For T‑Web, which depends on anisotropic tidal eigenvalues, you explicitly state that a proper reconstructed‑position rerun has not been performed. Yet the headline conclusion is worded as a strong bound on environment‑dependent chirality, and the abstract only briefly mentions that this is “a redshift‑space statement.” For PRD, this is not transparent enough: readers may overinterpret the constraints as real‑space statements on the cosmic web.  
- **Required fix**:  
  - Make the RSD limitation much more prominent and quantitative in the abstract and conclusions: explicitly say that all environment labels are derived in redshift space, that no reconstruction has been applied, and that anisotropic RSD could in principle reshuffle galaxies across environment boundaries at the few‑percent level.  
  - At minimum, provide a clear quantitative upper bound on the *fraction* of galaxies that could cross each class boundary under plausible RSD, based on your own eigenvalue‑spectrum analysis, and then propagate that into an uncertainty (or at least a systematic allowance) on the per‑class ∆fCW constraints.  

### P5‑E7 – Over‑reliance on internal pipeline paths and unpublished JSON artifacts as reproducibility surfaces  
- **Location**: Throughout (dozens of references to `pipelines/p5_desi_chirality/outputs/*.json`), Appendix C.  
- **Problem**: Many numeric statements are not derived in the text but only referenced as being in JSON outputs inside a private GitHub repo. A PRD paper cannot require access to a particular git tag on a private or mutable repository to check or reproduce core numbers. There is no DOI or permanent archival guarantee described for the code or data.  
- **Required fix**:  
  - Deposit all key analysis outputs (tables used for χ², σ values, bin counts) in a public, versioned data repository with a DOI (e.g., Zenodo).  
  - In the paper, ensure that every load‑bearing statistic (headline χ², n, fCW per bin) is either explicitly tabulated or given with enough information to recompute from standard public catalogs (DESI DR1, DESIVAST, etc.) without needing your repo.  
  - The GitHub path can be mentioned as a convenience, but not as the primary “proof” of numbers.

### P5‑E8 – Toy EFT operator in Appendix A is not sourced and risks misrepresenting the literature  
- **Location**: Appendix A, pp.30–31.  
- **Problem**: You introduce a toy operator \(L_{\text{parity}} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L\cdot\hat z)\) and loosely associate it with Chern–Simons gravity and parity‑violating cosmology ([1],[2]), then acknowledge it is not actually derived from those works. Presenting this as an “EFT mapping” risks misleading readers into thinking this is a known parametrization, and the discussion of rotational and gauge invariance is hand‑wavy. PRD would require either a properly derived EFT mapping or a very clear separation between speculative illustrative material and results.  
- **Required fix**:  
  - Clearly label this appendix as purely illustrative, remove any suggestion that the operator is grounded in [1] or [2], and refrain from calling it “EFT” unless you can show that it is gauge‑invariant and appropriately constructed.  
  - Alternatively, delete this appendix; it is not needed to support the empirical results and currently weakens the theoretical rigor.

### P5‑E9 – No explicit effect‑size measures accompanying headline σ and p values  
- **Location**: Abstract, p.1; Sec. VI A, VI C–E; Sec. VII.  
- **Problem**: You quote many σ‑level deviations and p‑values but only occasionally connect them to effect sizes (e.g., percentage‑point ∆fCW). For the main homogeneity tests and the DESIVAST void vs non‑void comparisons, you should include directly interpretable effect‑size quantities (difference in fCW, Cramér’s V, etc.) alongside σ. Some of this is present, but not systematically for every “headline” σ or χ², violating instruction 19.  
- **Required fix**: Wherever you call out a σ or χ² as a main result or an important null test (e.g., T‑Web 4×2 χ², DESIVAST z‑shell corrected test, Phase 2 sweep), add the corresponding effect sizes explicitly in the text, not only in tables or JSON.

---

## MAJOR ISSUES

### P5‑M1 – Statistical framework complexity and clarity  
- **Location**: Sec. V–VII, IX.  
- **Problem**: The paper uses Jeffreys intervals, σfrom half, σpred from monopole, label‑shuffle permutations with and without stratification, Bonferroni and empirical LEE. This is appropriate for a careful analysis, but the exposition is extremely dense and not easy to follow. It is hard for a reader to see exactly which test drives the main claims and how each test’s error rate is controlled.  
- **Required fix**: Streamline the description. Provide one concise subsection that, for each major family of tests (T‑Web 4‑class, DESIVAST void vs non‑void, Phase 2 sweep, redshift/density/sky scans), states: statistic, null hypothesis, multiple‑testing correction, and which numbers in the text correspond to the final decision. Remove redundant or near‑duplicate descriptions.

### P5‑M2 – Overlength relative to incremental contribution  
- **Location**: Entire manuscript (32 pages of dense methods for a single null result).  
- **Problem**: For a PRD methods paper, 32 pages can be acceptable, but here a large fraction of text is devoted to internal pipeline details, JSON filenames, and highly granular descriptive tests that do not materially change the scientific conclusion (a null environment dependence at the few‑×10⁻³ level). The incremental contribution beyond “we checked chirality vs environment using T‑Web and DESIVAST and found null” could be conveyed more compactly.  
- **Required fix**: Compress:  
  - Move many of the pipeline pathnames and JSON references to an online supplementary document.  
  - Condense Sections VI–IX by removing near‑duplicate robustness checks and focusing on a small, representative set.  
  - I would recommend a main‑text length of ≈20–22 PRD pages for the core paper, with additional robustness tests in an online supplement.

### P5‑M3 – Treatment of DESIVAST vs T‑Web discrepancies could be clearer  
- **Location**: Sec. VIII A, VIII C, IX C.  
- **Problem**: You note serious discrepancies between T‑Web void fractions and DESIVAST void geometry (e.g., only 6 T‑Web void spirals at z ≤ 0.24, none inside DESIVAST voids), but the implications for the validity of the T‑Web classification are scattered. For a reader, it is not entirely clear whether they should trust *any* T‑Web void‑based conclusion.  
- **Required fix**: Summarize explicitly, in one place, that (a) T‑Web voids at low z are strongly contaminated by survey‑edge artifacts and should not be used for physical void chirality conclusions; (b) DESIVAST supersedes T‑Web for voids; (c) T‑Web is still used for walls/filaments/clusters primarily as a diagnostic. This should be clearly stated in Sec. IV or the start of Sec. VI, not only in scattered remarks.

### P5‑M4 – Bright vs dark program residual not fully quantified as a systematic  
- **Location**: Sec. VI D, XI.  
- **Problem**: The ∼2σ bright/dark difference (0.81 pp) and the correlated T‑Web class vs program contingency (Cramér’s V = 0.078) are acknowledged but treated qualitatively. Given that the BGS selection function is known to carry systematics (from Paper IV), this needs more explicit quantification as a systematic on ∆fCW, including a clear statement of whether the DESIVAST void sample is dominated by bright‑program galaxies (it is, but this should be summarized crisply).  
- **Required fix**: Provide a single subsection that:  
  - Quantifies the contribution of bright vs dark selection to the catalog monopole and to each environment class;  
  - Demonstrates that the DESIVAST void vs non‑void contrast is effectively a bright‑only constraint and hence not biased by program mixing;  
  - Explicitly states the residual systematic uncertainty floor from this effect.

---

## MINOR ISSUES

### P5‑m1 – Minor internal inconsistencies and jargon  
- **Location**: Multiple, e.g. references to “V‑Web” in code paths while using “T‑Web” in text; “desi env vweb.parquet”.  
- **Problem**: The reader may be confused by conflicting nomenclature: the code file is called `compute_vweb.py` but you stress that the implementation is Hahn 2007 T‑Web, not Hoffman 2012 V‑Web.  
- **Required fix**: Add a concise clarification early in Sec. IV that all internal artifacts labeled “vweb” actually implement T‑Web, and that no velocity‑shear V‑Web classification is used anywhere.

### P5‑m2 – Occasional awkward phrasing and run‑on sentences  
- **Location**: Throughout.  
- **Problem**: Many sentences exceed 4 lines and mix multiple concepts (e.g., Sec. V, long sentences blending definitions and commentary). This hampers readability.  
- **Required fix**: Edit for clarity: split long sentences; limit each to a single main idea. This is editorial but will help acceptance.

### P5‑m3 – Excessive referencing of pipeline filenames and JSON artifacts in main text  
- **Location**: Virtually every section.  
- **Problem**: These are useful for internal reproducibility but clutter the scientific narrative.  
- **Required fix**: Move most of these references to a dedicated reproducibility appendix or an online table.

---

## NITS

### P5‑n1 – Overuse of abbreviations without a short list  
- **Location**: Entire manuscript (e.g., “PIS” appears once, “GALZONE,” “EDR,” “VAC,” etc.).  
- **Required fix**: Provide a short “Acronyms and notation” table early in the paper.

### P5‑n2 – Some footnotes are essentially methods paragraphs  
- **Location**: Footnote a on p.2 (Tij definition and sign conventions).  
- **Required fix**: Move such content into the main methods section or a dedicated technical appendix.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core empirical result—a null detection of environment‑dependent spiral chirality in DESI DR1 at the ≲10⁻² level—is potentially interesting and methodologically careful. However, the manuscript in its current form does not meet PRD standards for self‑containment, clarity of statistical inference, and theoretical rigor. The dependence on an unpublished companion catalog (Paper IV), the proliferation of internal pipeline references, the only qualitative RSD treatment, and the speculative EFT appendix all need substantial revision. With a clearer, more compact presentation, a fully self‑contained chirality‑catalog description, strengthened handling of systematics, and explicit caveats in the abstract and conclusions, the work could become suitable for PRD, but this will require significant restructuring and tightening.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E10 – Inconsistent or unjustified numerical claims (arithmetic and σ/p bookkeeping)  
- **Location**: Abstract, §V, §VI A, §VI C–D, §VII, §VIII B–E, Tables III–VIII, X, XII, XV.  
- **Problem**: Several quoted σ, ranges, and “floor” numbers are numerically inconsistent with the counts, or are derived with conventions that are never made explicit and therefore easy to misread or misapply. Concrete examples:  
  - **“Counting-statistics floor of ±2.4 pp (the 1σ binomial half-width of the n = 428 T‑Web void bin)”** in the abstract: for a binomial with p≈0.5 and n=428, the 1σ half‑width is ≈\(1.0/\sqrt{428} ≈ 4.8\) percentage points, not 2.4; 2.4 pp is the 1σ half-width for n≈1730, or the 2σ half-width for n=428.[body text] The abstract itself then calls “2σ half‑width ±4.8 pp,” so the 1σ number is internally inconsistent.  
  - **“range across classes is 1.98 pp”** (Abstract, Table III): the class fractions are {0.4836, 0.5034, 0.4980, 0.4963}. The max–min difference is 0.5034–0.4836 = 0.0198 = 1.98 pp, which is correct, but you claim this is “dominated” by the void bin counting floor derived as “±2.4 pp.” With the corrected 1σ floor of ±4.8 pp, the narrative of “dominated by the floor” still holds, but the quoted number does not.  
  - **σfrom half values in Table III and text** (e.g. filament –2.61, cluster –4.66, void –0.68) are consistent with \(σ = (n_{CW}−0.5n)/\sqrt{0.5n}\) to numerical precision, but in several places you call them “σ from half” *and* compare them to Bonferroni thresholds derived for standard normal z, without ever stating that you always use p0=0.5 rather than p̂ or the P4 monopole, and that you ignore the small correction for p0≠0.5. The choice is defensible (you partially explain it once in §V), but the abstract and some later passages behave as if σ were generic “Gaussian σ” while they are in fact under a fixed‑p and fixed‑denominator convention. This matters where you later juxtapose **σfrom half** and two‑sample **zΔ** without warning the reader that the nulls and denominators differ (§VIII B, Table X, §XI).  
  - **Phase‑2 sweep “per-cell range vs void‑bin 2σ floor”** (§VII, Table VII): you repeatedly claim that per‑cell ranges “stay within 1.01× the void-class 2σ counting floor \(1/\sqrt{n_{void}}\).” For example, for the cell Rs=50, λth=0.1, Table VII quotes nvoid=599 and range=4.12 pp. The **1σ** binomial half‑width at p=0.5 and n=599 is ≈4.1%; 2σ is ≈8.2%; your 4.12 pp range is ≈1.0× the *1σ* void floor, not the 2σ floor you refer to. Several other cells show the same pattern. The text conflates “2σ floor” and the observed 1σ‑scale ranges.  
  - **Per‑class σpred from the P4 monopole** (§VI A, §V): you write \(σ_{\rm pred} = 2\,Δf_{CW}\sqrt{N}\). For N≈4×10^5 and Δf=−0.0026, this gives |σpred|≈3.3, matching your filament/cluster statements, but later you mix σpred based on P4 with residuals based on the P5 monopole (Table XII) and with two‑sample zΔ (Table X). The different nulls and denominators are not clearly kept separate; this is a bookkeeping rather than a raw arithmetic problem.  
- **Required fix**:  
  - Audit all quoted “floors” and half‑widths (±2.4 pp, ±4.8 pp, 1/(2√n), 1/√n) and recompute them directly from n. Correct any mis‑stated numbers (at minimum the 1σ=2.4 pp in the abstract and the “2σ floor” language in §VII).  
  - Make the σ definitions absolutely explicit once, and then refer back: clearly distinguish (i) one‑sample σfrom half at p0=0.5, (ii) σpred from the P4 monopole, and (iii) two‑sample zΔ. Avoid mixing them in the same sentence without stating which is used.  
  - Where you compare “range” to a “2σ floor,” use the correct numerical factor (either use 1σ, or rescale your narrative to the proper 2σ values), or drop the “2σ” wording and simply state that ranges are of the same order as the 1σ void noise.

---

P5‑E11 – Abstract/conclusion over‑tighten the environment bound relative to what is actually shown (LEEs and RSD)  
- **Location**: Abstract (headline statement and last paragraph), §VI A, §VII, §VIII, §XII, §XV, §XIII.  
- **Problem**: The abstract and conclusions speak in terms that read as a **single, survey‑wide, 4‑class constraint** on environment‑dependent chirality, but the body makes clear that (i) you have multiple, heterogenous null procedures (simple σfrom half, χ² tests, permutation max‑stat pLEE, multiple Bonferroni families), and (ii) all results are explicitly *redshift‑space* and subject to unquantified anisotropic RSD boundary‑crossing. Specific gaps:  
  - You describe “no evidence for environment‑dependent chirality beyond the catalog‑monopole offset at current sensitivity” as if there were a single global test, whereas in practice you have a large garden of nested tests (T‑Web 4×2 χ², DESIVAST void vs non‑void, Phase 2 nine‑cell sweep, Tempel, ASTRA, redshift, density, HEALPix, program splits). The only place that multiplicity is even partially controlled is §V B / Table II (Bonferroni‑5 and Bonferroni‑9), and you explicitly state that many paths are *descriptive*. Yet the abstract and §§XII–XV read as if all these explorations fed into one joint “upper bound.”  
  - RSD: In §XIII you explain quite clearly that a truly quantitative RSD treatment would require reconstructed positions and that the eigenvalue spectrum near class boundaries can lead to anisotropic class flips not captured by your scalar σv/(aH) argument. Nonetheless, the abstract and §XV present the results as a fairly definitive statement on “environment‑dependent chirality” without stating prominently that this is **only in DESI DR1 redshift space at Rs≈25 Mpc/h** and **without reconstruction**. The brief abstract clause “the headline environment‑independence statement is therefore a redshift-space statement” is easy to miss and does not quantify how much boundary leakage RSD could plausibly induce.  
- **Required fix**:  
  - In the abstract, explicitly state that: (a) the main bound comes from a **single pre‑declared primary family** (the five DESIVAST void/non‑void contrasts), controlled at Bonferroni‑5, and (b) all other environment tests are exploratory/diagnostic and not jointly controlled for multiplicity.  
  - Move a concise “multiplicity caveat” into the abstract or early in the conclusions so readers do not over‑interpret the ensemble of nulls as a single global p‑value.  
  - Strengthen the RSD caveat where the results are summarized: spell out in the abstract/conclusions that all classifications are in **observed redshift space, without reconstruction**, that anisotropic RSD can reshuffle a few percent of galaxies across environment boundaries, and that you **do not propagate** this into the quoted σ and ∆fCW limits. This makes the scope of the bound honest and PRD‑level transparent.

---

P5‑E12 – Heterogeneous σ values from different null procedures juxtaposed as if interchangeable  
- **Location**: Abstract (σfrom half, χ² p, look‑elsewhere p), §V, §VI A–E, §VII, §VIII B–F, §IX B–C, §X, §XI, §XII C.  
- **Problem**: You use multiple σ‑like quantities with different underlying nulls and denominators—one‑sample σfrom half, monopole‑referenced σpred, two‑sample zΔ, logistic‑regression Wald z, and permutation‑derived max‑stat pLEE converted qualitatively to “σ” language—but often present them in the same paragraph without clarifying that they are **not directly comparable**. Examples:  
  - In §VI A you quote σfrom half per class, then immediately discuss χ² p‑values from a 4×2 contingency test; later in §VI D you discuss two‑sample z for bright vs dark; in §VIII B and Table X you use zΔ for void vs non‑void contrasts. All are called “σ” or “z” but the reader is never explicitly told which values **can** be sensibly compared and which cannot.  
  - The abstract mixes: σfrom half in the T‑Web void bin, χ² p for the omnibus test, permutation pLEE values for density and HEALPix scans, and again σ thresholds from Bonferroni formulas, all without ever stating that these belong to different families and are not calibrated to a common false‑positive rate across the whole analysis.  
  - In the density section (§VI C–D), you compare per‑quintile σobs, σpred from the monopole, and then a Bonferroni‑5 threshold derived for standard normal maxima, again without spelling out that σobs and σpred are computed under different effective nulls than zΔ used elsewhere.  
- **Required fix**:  
  - Add a compact “σ taxonomy” subsection at the end of §V that lists every σ‑like quantity you use, its exact definition, and its null hypothesis.  
  - Whenever you juxtapose numbers (e.g. “cluster −4.7σ” and “bright vs dark |z|≈2.1σ”), state explicitly which statistic each refers to and that they are not on a single unified scale unless you have verified that.  
  - Remove any phrasing that implies, or might be read as implying, that a 2σ σfrom half, a 2σ two‑sample zΔ, and a “2σ” permutation max‑stat are interchangeable. For PRD readers, clarity that these are different tests is essential.

---

P5‑E13 – Abstract and “toy EFT” appendix blur the line between data‑driven bound and speculative parametrization  
- **Location**: Appendix A, abstract (last sentences), §XII B.  
- **Problem**: You have already flagged in your own text that the toy operator \(L_{\text{parity}}\supset g_\phi(\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)\) is *not* derived from the cited parity‑violating literature and is not gauge‑ or rotationally‑invariant in its literal form. However, Appendix A and the tail of the conclusions still present an **order‑of‑magnitude bound on \(g_\phi \nabla\phi\)** and call this an “EFT mapping.” This risks being read as a substantive theoretical constraint rather than a heuristic back‑of‑the‑envelope. The abstract and conclusions hint at “an observational upper bound that any future model… must respect” without making clear that this is **not** a rigorously derived EFT constraint and depends on an unworked transfer function and slicing choice.  
- **Required fix**:  
  - Downgrade all language in Appendix A and in the abstract/conclusions that could be read as a genuine EFT bound. For example, call it explicitly a “heuristic toy parametrization for intuition only” and remove any symbolic inequality that looks like a constraint on \(g_\phi\) unless you either (a) actually propagate your data into a properly‑defined EFT parameter with clear assumptions, or (b) move the inequality into a clearly labeled “numerical illustration.”  
  - Make sure the abstract does not suggest that PRD readers should interpret this as a model‑independent bound on parity‑violating couplings. If you keep Appendix A, it must be clearly decoupled from the empirical claims.

---

P5‑M5 – Several figure captions vs. body claims rely on off‑paper JSON for key numbers, making consistency hard to verify  
- **Location**: Figures 3–9 captions, §IV A (Fig. 2), §VI A–E, §VII (Fig. 7), §VIII E (Fig. 8), §IX A, §X.  
- **Problem**: You often state that figure values (e.g. volume fractions in Fig. 2, per‑pixel σ ranges and p99 null thresholds in Figs. 6 and 8, phase‑2 ranges in Fig. 7) are supported by JSON artifacts in your repository, but the captions themselves do not quote the underlying numbers in a way that lets a reader check consistency against the text without accessing the code. For example, Fig. 2’s caption says the cluster fraction “1.0%” and wall+filament “74.5%,” while the body text in §IV B gives {void 0.244, wall 0.413, filament 0.333, cluster 0.010}. This is arithmetically consistent, but only because you re‑state the exact numbers in the prose. For the HEALPix figures (Figs. 6, 8) you give σ ranges and npix in the captions and different, more detailed counts in the body – all *appear* compatible, but there is no self‑contained explicit numerical bridge (e.g. exact max |σ| vs. p99) in the caption, and the only full values are buried in JSON.  
- **Required fix**:  
  - For each figure that carries a quantitative message (esp. Figs. 2–8), ensure that the caption and the immediately associated body paragraph together contain **all numbers needed** to verify the claim without the repo. E.g. for Fig. 7, explicitly list the Rs,λth cell giving 4.12 pp and its nvoid and the corresponding 1σ void floor in the text, not only in Table VII or JSON.  
  - Where a caption cites a range or p99 null (e.g. Table VI / Fig. 6), ensure that the body text reproduces those values directly and that they are internally consistent, so PRD referees do not have to chase JSON to check Figure–body consistency.

---

P5‑M6 – Some internal cross‑references mislead about where justification actually appears  
- **Location**: §VIII A–E, §IX A–C, §X, Appendix B–C.  
- **Problem**: Several sentences use “see §X”, “see §VIII E”, “see pipelines/…” in ways that suggest the referenced section contains a full derivation, when in fact it contains only a brief qualitative remark plus a pointer to off‑paper artifacts. Examples:  
  - §VIII C (“the three‑algorithm robustness extends the P5 headline… see Table X”) – Table X has the basic counts, but key caveats (e.g. GALZONE vs hole‑union differences, EDGE/DEPTH flags) are only in §VIII D and in JSON.  
  - §IX C (“the BGS‑anchored volume‑filling‑fraction calibration… is consistent with the T‑Web sheet/filament fractions here”) – the sole “calibration” is a qualitative 5–10 pp comparison without any quantitative uncertainty or explicit mapping between samples. The reference to  and  is fine, but the phrasing suggests a more detailed validation than is actually provided.  
- **Required fix**:  
  - Audit every “see §X” and ensure the target section actually contains the *quantitative* content implied (not just a narrative plus an artifact pointer). Where it does not, either move the necessary numbers into the text or rephrase to make clear that this is a qualitative or partial check.  
  - For cross‑references to appendices and to the code repo, make sure the main text contains enough to stand alone for PRD’s “self‑contained article” standard, and use cross‑refs only for genuine further detail.

---

P5‑m4 – Abstract and body occasionally hedge (“consistent with,” “tracks,” “reinforces”) without quoting the underlying deltas  
- **Location**: Abstract, §VI A–D, §VIII C–E, §IX B–C, §X, §XII C.  
- **Problem**: There are several sentences of the form “this is consistent with the BGS‑selection‑function‑conditioned imaging‑leg systematics,” “the signal tracks survey‑mask geometry,” “no tension,” etc., where a numerical comparison is implicitly invoked but not made explicit in the same sentence or paragraph. For example, the statement that the bright vs dark filament sign‑flip “is best read as a residual structure” is supported by numbers earlier in §VI D, but the summary lines themselves carry only qualitative language.  
- **Required fix**:  
  - Wherever you use terms like “consistent with,” “tracks,” or “no significant tension,” add a parenthetical or short clause with the actual ∆ + uncertainty (e.g. “difference 0.81 pp, |z|=1.95 unique‑galaxy”) to anchor the phrase numerically. This is a PRD‑style expectation for quantitative papers.  
  - Do a quick search for those phrases and ensure each one is backed by an explicit ∆ and σ in the immediate context, not only somewhere earlier in the section.

---

P5‑m5 – Appendix A dimensional and invariance caveats are buried late and could still confuse readers  
- **Location**: Appendix A.  
- **Problem**: You do a good job at the end of Appendix A explaining that the operator is not gauge‑invariant and that the \(\hat L\cdot\hat z\) factor is only schematic, but these caveats come after you have already introduced a scaling \( |g_\phi (\nabla \phi)/H_0| \lesssim 10^{-2}/⟨|\Delta\rho/\rho_{\rm bg}|⟩\). A hurried reader might read the inequality, miss the caveats, and treat it as a robust EFT constraint.  
- **Required fix**:  
  - Move a short, explicit disclaimer to the *beginning* of Appendix A: e.g. “This appendix presents a non‑covariant, non‑gauge‑invariant toy parametrization for intuition only; it is not a derived EFT bound.”  
  - Optionally, drop the explicit inequality and replace it with a verbal statement (“numerically, the observed per‑class ∆fCW≲0.01 would correspond, in such a toy mapping, to order‑unity values of …”). This reduces the risk of misinterpretation.

---

P5‑N3 – Minor stale or inconsistent numbers between overlapping descriptions  
- **Location**: §VIII E, Fig. 8 caption, §VIII B, §IX A.  
- **Problem**: Several places describe the same quantity in slightly different ways, which can confuse readers checking consistency:  
  - The number of NSIDE=32 pixels with both voids and ≥200 spirals is given as “nboth_pix = 727” in §VIII F and “885 occupied pixels at NSIDE=32” in the Fig. 8 caption (the latter is total pixels with any voids, the former is the subset with enough spirals, but this is not stated explicitly).  
  - In §VIII E you state “297 occupied pixels at NSIDE 16” and “885 occupied pixels at NSIDE 32,” but Table XI works only at NSIDE 16. The mapping is correct but slightly opaque.  
- **Required fix**:  
  - When the same symbol (e.g. npix) is used at different resolutions or with different occupancy criteria, make that explicit each time (“npix(≥1 void), npix(≥200 spirals)”).  
  - Where possible, harmonize or annotate overlapping numbers (e.g., in the Fig. 8 caption, specify “885 pixels with ≥1 maximal void; of these, 727 also meet the ≥200 spirals cut used in §VIII F”). This will help referees who systematically cross‑check counts.

---

If you address these numerical and clarity issues on top of the structural problems in the original review, the manuscript will be substantially closer to PRD’s standards for rigor and self‑consistency.