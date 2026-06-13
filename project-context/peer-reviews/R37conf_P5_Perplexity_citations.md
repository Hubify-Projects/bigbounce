# P5 R37conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.72.pdf` md5=544b6af2 pages=32
**Input format**: TEXT + web search + pass-2 self-critique (15114 chars)
**Wall time**: 85.1s

---

I cannot see the actual PDF or its reference list, and I also do not have direct access to arXiv/ADS records for this manuscript beyond what is quoted in the text. Because of that, I cannot perform the line‑by‑line citation forensics and consistency checks you requested (arXiv IDs, journal/volume/page, DOI verification, table/abstract statistic tracing, etc.) on the actual reference list or on any figures/tables that are only present in the rendered PDF.

What I can do is audit the *text you provided* for issues that Physical Review D would consider unacceptable and classify them. I focus on:

- Internal language not appropriate for a PRD paper.
- Use of non‑peer‑reviewed “companion” works as load‑bearing inputs.
- Version‑history and repository bookkeeping in the body.
- Use of future‑dated or “in preparation” references.
- Ambiguous or misleading labeling of T‑Web vs V‑Web.
- Procedural/statistical issues visible in the excerpt.

Because I do not see the actual page layout, I cannot assign precise page numbers, but I will still tag each finding with the section where it occurs.

---

## ESSENTIAL findings

### P5‑E1 – Unacceptable reliance on unpublished companion “Paper IV” as a load‑bearing source

- **Location:** Abstract, Introduction (§I–II), Data (§III.A), many places in the body.
- **Problem:**
  - The paper repeatedly treats “Paper IV” as a load‑bearing catalog, calibration, and systematics reference:
    - “Paper IV [3] (companion work, not yet peer-reviewed)…”
    - “Paper IV [3]… currently in preparation and not yet peer reviewed; the present manuscript treats its catalog and quoted monopole offset as inputs…”
    - The catalog monopole, sky‑systematics and classifier properties are taken as established and are crucial to the argument (e.g. the subtraction of Δf_CW≈−0.0026 everywhere).
  - Reference [3] itself is explicitly described as “in preparation; manuscript in preparation” at the end.
  - For PRD, a core input catalog and its key statistical properties cannot be relegated to an unpublished, non‑archived companion. A referee cannot verify any of the claimed Paper IV results or uncertainties.
- **Required fix:**
  - Either:
    1. Publish Paper IV (or an equivalent methods/catalog paper) in an accessible, citable form (arXiv + stable version) and restrict this paper to using only those results that are internally documented and reproducible at the level PRD requires, **or**
    2. Move all load‑bearing pieces of Paper IV into this manuscript: full classifier description, training data, catalog selection, monopole derivation, imaging‑leg systematics, etc., including enough detail (and released artifacts) that the catalog and its bias properties can be reproduced independently from this paper alone.
  - Until one of these is done, the current manuscript does not meet PRD standards for verifiability.

---

### P5‑E2 – Explicit version‑tracking / internal bookkeeping in the body

- **Location:** Title block, Abstract, §II, §VII, §VIII, Appendix C, references.
- **Problem:**
  - The manuscript contains numerous bits of version‑history and internal bookkeeping that must not appear in the body of a PRD article:
    - Title block: “(Dated: June 2026 — v0.1.72-2026-06-13)”.
    - Abstract and body: “Paper IV v1.0.166”, “withdrawn in Paper IV v1.0.166 after a provenance audit…”
    - Appendix C: “manuscript tag v0.1.72-2026-06-13”.
    - Multiple mentions of internal pipeline paths and filenames, e.g. `pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json`.
  - This reads like a lab notebook / repository log, not like a finished PRD manuscript. PRD allows a Dated line, but not internal Git tags and path names embedded throughout.
- **Required fix:**
  - Remove all explicit version tags and internal audit references from the body and abstract:
    - Replace “v0.1.72-2026-06-13”, “v1.0.166” with neutral text (“current version of Paper IV” or nothing).
    - Move any essential provenance information (e.g. which catalog release) into a short, stable description (e.g. “Paper IV catalog release 2026‑05”).
  - Move detailed file paths and internal JSON filenames to a data‑availability statement or a supplemental “analysis notes” document; in the main text use generic descriptions (“we provide machine‑readable tables with …”).

---

### P5‑E3 – Self‑contradictory “V‑Web” vs “T‑Web” terminology that can mislead readers

- **Location:** Title, Abstract, footnote “a” on first page, §IV A, §IX C.
- **Problem:**
  - The title says: “with T-Web (Hahn 2007) tidal-tensor cross-check…”.
  - Throughout the text the author calls their implementation “V‑Web” but explicitly acknowledges that it is **not** the velocity‑shear V‑Web of Hoffman+2012:
    - Footnote: “We use the tidal-tensor formulation … the Hahn 2007 recipe, sometimes called the T-Web variant… The Hoffman et al. 2012 [6] velocity-shear V-Web requires a separate velocity reconstruction not used here; for backward compatibility … we retain the ‘V-Web’ label which is sometimes used loosely…”
  - This is very confusing and, as written, incorrect by usual cosmology standards: “V‑Web” has a specific, velocity‑shear meaning in the literature; this paper uses the **density tidal tensor** (T‑Web).
- **Required fix:**
  - Use **consistent and correct terminology**:
    - In the title and everywhere in the paper, refer to your classifier as **T‑Web** (Hahn 2007 tidal tensor) unless you actually use the velocity‑shear V‑Web of Hoffman+2012.
    - If you want to mention that DESI collaborations sometimes refer loosely to any web finder as “V‑Web”, clarify that this paper strictly uses T‑Web and adjust all labels, axes, and text accordingly.
  - Re‑check all mentions of “V‑Web”, “T‑Web”, “velocity‑shear” and make them internally consistent with what is actually implemented.

---

### P5‑E4 – Use of σ values from different nulls side‑by‑side without per‑juxtaposition caveats

- **Location:** Abstract, §V, §§VI–VIII.
- **Problem:**
  - The abstract and body repeatedly present:
    - “σ_from half” (binomial z vs p=0.5),
    - “σ_pred” from the catalog monopole,
    - “z_Δ” from two‑sample tests,
    - “|z| ≈ 2.1σ” bright/dark comparison,
    - and permutation‑based p‑values,
    sometimes in the same sentence or table with the same “σ” notation.
  - The abstract warns once that σ values across different N are “not mutually comparable” (for the class counts), but there are multiple other juxtapositions where that caveat is not reiterated. The instructions you gave explicitly require that *every* juxtaposition of σ from different null procedures be explicitly qualified.
- **Required fix:**
  - For each place where two σ’s from different procedures or different denominators appear side‑by‑side (e.g. σ_from_half vs z_Δ vs “σ_vs_monopole”), add a **local explicit statement** that they are not directly comparable.
  - Alternatively, adopt distinct symbols or notation (e.g. z_bin, z_diff, z_mono) and explicitly define them and remind the reader when you compare them in the same paragraph.
  - Re‑check the abstract and every results subsection for such juxtapositions; if any remain unqualified, add the caveat there.

---

### P5‑E5 – Load‑bearing claims based on unpublished DR1/EDR catalogs without sufficient self‑containment

- **Location:** §IV (V‑Web construction), §IX C (concurrent DR1 T‑Web), §X (ASTRA), §XIII Limitations.
- **Problem:**
  - The analysis uses:
    - A custom T‑Web/V‑Web run on DESI DR1, described only sketchily (grid size, Rs, λ_th) and via internal pipeline paths.
    - A concurrent T‑Web DR1 analysis  that is “in submission to MNRAS”, not fully published.
    - ASTRA EDR probabilistic catalogs  to support cross‑checks.
  - For PRD, a reader must be able to reproduce the environment classification **without access to unpublished or unstable external VACs**. Merely pointing to an arXiv preprint plus GitHub structure is not enough if key steps (e.g. masking, selection functions, randoms) are only described in code.
- **Required fix:**
  - Consolidate a **complete, reproducible specification** of your T‑Web procedure in this paper: input selection, mask, grid geometry, mass assignment, smoothing, Poisson solve, eigenvalue sign conventions, and class thresholds. It must be sufficient that an independent group can rebuild the web classification from DR1 alone, without any of your code.
  - Treat  and  strictly as **secondary context**, not as load‑bearing pillars of the argument, and make clear that your main conclusions do not depend on them.
  - If any of your sky masks or selection functions are not described in DESI technical documentation, you must define them explicitly or provide a citable, frozen description.

---

### P5‑E6 – Abstract relies heavily on results and caveats defined only deep in the paper; risk of abstract–body mismatch

- **Location:** Abstract vs. §§VI–VIII.
- **Problem:**
  - The abstract is extremely dense, with many specific numbers (counts, σ, p‑values, Bonferroni thresholds, “Phase 2 sweep across nine cells”, “label‑shuffle look‑elsewhere p=0.13–0.56”, “Rs=10 Mpc/h cells… degenerate limit, §VII”). 
  - From the excerpt, these do seem to be backed in the body, but as a referee I cannot verify that the **final calibrated statements** in §VIII–XIII exactly match the abstract’s phrasing and caveats.
- **Required fix:**
  - After all other revisions, perform an explicit **abstract‑last sweep**:
    - For each quantitative claim in the abstract, point to the section/table where the same result appears and ensure the wording and level of caution are identical.
    - Strip anything that is only exploratory or not load‑bearing.
  - Given how specialized the methods are, simplify the abstract to stress just:
    - sample sizes,
    - main null result,
    - the DESIVAST void vs non‑void constraint,
    - and one sentence on robustness.
  - Remove technical config details from the abstract (e.g. “Rs=10 Mpc/h cells sit below the 25.9 Mpc/h grid…”) and keep them for the methods.

---

## MAJOR findings

### P5‑M1 – Overuse of internal pipeline paths and JSON filenames in the main text

- **Location:** many sections, especially §V, §VI, §VII, §VIII, Appendices.
- **Problem:**
  - The manuscript is littered with references like:
    - `pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json`
    - `env_finder/01_compute_vweb.py`
  - This is not standard style for PRD and severely hampers readability. It also hard‑codes a Git layout that may not match the final public archive.
- **Required fix:**
  - Move all such paths to:
    - A short Data/Code availability section (Appendix) and/or a README in the released repository.
  - In the main text, refer generically (“see the machine‑readable table with the per‑cell statistics”) and provide a stable label or table ID.

---

### P5‑M2 – Use of “in preparation” / “companion” references as if they are stable literature

- **Location:** references [3] and [4]; §II and elsewhere.
- **Problem:**
  - [3] and [4] are both described as “companion paper (in preparation)” and are central to the narrative (Paper II and IV).
  - PRD expects that references cited for scientific claims are at least on arXiv with stable identifiers; “in preparation” is acceptable only for minor, non‑load‑bearing pointers.
- **Required fix:**
  - Either:
    - Put these works on arXiv with stable IDs and cite those (and ensure the methods/results used here are consistent with the posted versions), **or**
    - Remove them as references and instead describe, within the present paper, any critical results you need from them.
  - Downgrade “companion paper” language in the main text; keep only brief mentions in the Introduction or Outlook if needed.

---

### P5‑M3 – Paper is overlong and reads partly like a pipeline technical note

- **Location:** whole manuscript (32 pages).
- **Problem:**
  - For the scientific contribution (“null detection of environmental dependence at the ~10^{-3} level”), 32 pages of dense pipeline detail and cross‑checks is excessive for PRD.
  - A substantial fraction describes:
    - grid and mask construction,
    - internal convergence tests,
    - multiple variants of the same null,
    - low‑impact stratifications (e.g. modest bright/dark residuals) with very fine detail.
- **Required fix:**
  - Condense the paper to focus on:
    - Data description,
    - T‑Web construction (once, clearly),
    - DESIVAST void vs non‑void results,
    - key secondary checks (redshift, density, HEALPix),
    - and essential systematic tests.
  - Move most of the internal closure tests, alternative mask definitions, and file‑path‑level descriptions to a Supplement or to the public repository.
  - A reasonable target would be **≤ 20 pages** main text (excluding appendices).

---

### P5‑M4 – Ambiguous treatment of redshift‑space distortions (RSD) and their effect on environment labels

- **Location:** §VIII (RSD treatment), §XIII Limitations.
- **Problem:**
  - The text acknowledges that:
    - Environment labels are computed in **redshift space**, not reconstructed.
    - RSD can move boundaries between T‑Web classes.
  - It then argues, essentially by order‑of‑magnitude, that this is “bounded”. The argument is heuristic, and its quantitative impact on the chirality null (i.e. on Δf_CW) is not demonstrated rigorously.
- **Required fix:**
  - Either:
    - Perform a concrete RSD robustness test using an existing DR1 reconstruction (if available) or a simple Zel’dovich reconstruction, recompute the web, and show that Δf_CW shifts are well below your error bars; **or**
    - Sharpen the existing argument into a clearly bounding inequality, and state explicitly that RSD could at most induce, say, |Δf_CW| < X, which is below the observed limits. This must be framed as an assumption, not as a proven negligible effect.
  - At minimum, move the current detailed but ultimately heuristic RSD discussion into a dedicated “Limitations” subsection and be explicit that the environment labels are in redshift space.

---

### P5‑M5 – Toy EFT mapping in Appendix A is not derived and risks overclaiming

- **Location:** Appendix A.
- **Problem:**
  - The appendix introduces an operator “L_parity ⊃ g_ϕ (∇ϕ)(∇ρ/ρ_bg)(L̂·ẑ)” and a bound “|g_ϕ ∇ϕ/H₀| ≲ 10^{-2}/⟨|Δρ/ρ_bg|⟩” and says this is **not** directly derived from [1],[2].
  - As written, this is a speculative mapping with no calculation, but it is presented in the same formal style as real EFT constraints.
- **Required fix:**
  - Either:
    - Remove Appendix A completely, or
    - Recast it as a very short, clearly speculative paragraph in the Discussion, avoiding any quasi‑quantitative “bound” and stressing it is purely heuristic.
  - PRD typically requires that operator‑level constraints be demonstrably derived or else be labeled clearly as a “toy illustration” without implied quantitative significance.

---

## MINOR findings

### P5‑m1 – Confusing title phrasing

- **Location:** Title.
- **Problem:**
  - “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T-Web (Hahn 2007) Tidal-Tensor Cross-Check Across the DR1 Matched-Spiral Sample”
  - Very long, includes methods jargon (“T‑Web”) and the sample size, and mixes DESIVAST and T‑Web in a way that is hard to parse.
- **Required fix:**
  - Shorten and clarify, e.g.:
    - “Environmental Dependence of Spiral Chirality in DESI DR1: DESIVAST Void Tests and T‑Web Cross‑Checks”
  - Leave detailed sample sizes and algorithm counts to the abstract/body.

---

### P5‑m2 – Duplicate or near‑duplicate phrases

- **Location:** e.g. Appendix C (“manuscript in preparation; manuscript in preparation”), several “canonical canonical‑” style near repeats when describing catalogs.
- **Problem:**
  - While I did not find a literal “canonical canonical‑mask” phrase, there are several near‑repetitions (e.g. “manuscript in preparation; manuscript in preparation”) that read as editing artifacts.
- **Required fix:**
  - Run a careful copy‑edit pass to remove duplicated words/phrases and ensure each sentence is concise.

---

### P5‑m3 – Overuse of acronyms and internal shorthand

- **Location:** Throughout (BGS, EDR, VAC, PIS, GALZONE, etc.).
- **Problem:**
  - Many acronyms are used with only one definition many pages earlier; readers not deeply embedded in DESI will struggle.
- **Required fix:**
  - Ensure each acronym is defined on first use, and consider repeating definitions for critical ones in figure captions and key result sections.

---

### P5‑m4 – Data‑availability description is repository‑centric, not publication‑centric

- **Location:** Appendix C.
- **Problem:**
  - Data and code availability is phrased as “GitHub repository Hubify-Projects/bigbounce… pipelines/p5_desi_chirality/… will be DOI‑minted with submission”.
- **Required fix:**
  - Rephrase to:
    - Identify a permanent archive (e.g. Zenodo) with DOI.
    - State what is provided there (code, configs, tables) at a high level.
  - Avoid relying solely on a personal GitHub as the canonical location for reproducibility.

---

## NITs (cosmetic)

### P5‑n1 – Some sentences are extremely long and hard to parse

- **Location:** Abstract, §V–VIII.
- **Problem:**
  - There are multiple >5‑line sentences with many parenthetical clauses.
- **Required fix:**
  - Break such sentences into 2–3 simpler ones for readability.

---

### P5‑n2 – Occasional informal language

- **Location:** e.g. “garden‑of‑forking‑paths concern”, “we flag this as a diagnostic…”.
- **Problem:**
  - Slightly informal; PRD generally prefers neutral technical prose.
- **Required fix:**
  - Replace with more formal phrasing (e.g. “multiple comparisons concern”, “we identify this as a diagnostic…”).

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The manuscript contains a technically serious and careful null result, but as currently written it does not meet PRD standards of verifiability and presentation. The strongest blockers are the heavy dependence on an unpublished “Paper IV” for the core catalog and monopole calibration, the inconsistent and potentially misleading use of “V‑Web” vs “T‑Web”, and the presence of explicit version‑history and internal pipeline paths throughout the text. In addition, the paper is substantially longer and more pipeline‑oriented than needed for the stated scientific contribution. With a significant restructuring—moving all load‑bearing catalog information into citable and self‑contained form, cleaning up terminology and presentation, and shortening to a more focused physics narrative—the work could be brought into shape for serious consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E7 – Several quoted σ and p values are arithmetically inconsistent with the stated inputs or with each other
- **Location:** Abstract; §§V–VII; Tables III, IV, VII, X; text around density and DESIVAST results.
- **Problem (selected examples):**
  - **Abstract “counting‑statistics floor ±2.4 pp (1σ … n = 428)”**: for a binomial with \(N=428\), the 1σ half‑width around 0.5 is \(\sqrt{0.25/N} ≈ 0.0242\), i.e. 2.42 percentage points—this is fine. But later in §VII the void 1σ floor is written as “1.7–2.6 pp… 2σ… ≤1.01× void 2σ floor,” and in Table VII some ranges (e.g. 4.12 pp at Rs=50, λ=0.1, n_void=599) barely match or slightly exceed “1.01×2σ” depending on rounding. You need to recompute these ratios with consistent rounding and either (i) loosen the “≤1.01×2σ” wording or (ii) correct ranges/σ values so the inequalities actually hold numerically.
  - **σ_pred formula versus numbers**: Eq. (1) defines \(\sigma_{\rm pred} = 2\,\Delta f_{\rm CW}\sqrt{N}\) with \(\Delta f_{\rm CW}=-0.0026\). For filament with \(N=408{,}187\), this gives \(|\sigma_{\rm pred}| ≈ 2×0.0026×\sqrt{408{,}187} ≈ 3.32\), matching text. For the density‑quintile example (§VI C, Table IV), the text says \(N=158{,}327\) per quintile; \(2×0.0026×\sqrt{158{,}327} ≈ 2.61\), but you quote σ_pred = −2.07 for all quintiles. That implies either the quoted N or σ_pred is stale or miscomputed.  
  - **Phase‑2 sweep max residual**: Table VII claims a maximum resolved‑cell \(|\sigma_{\rm obs}-\sigma_{\rm pred}|=1.64\), and the text states the canonical cluster cell has observed |σ|=4.66 and predicted ≈3.3, “leaving…−1.38.” That matches. But some Rs=10 entries show max residuals of 1.69–1.87; applying the same formula with the tabulated n_void values and ∆f_CW often gives slightly different residuals, suggesting those numbers were recomputed after changing N and not fully propagated.  
  - **DESIVAST void vs non‑void contrast:** Table VIII reports Δf_CW ≈ +0.0007 between f_void=0.4964 and f_non‑void=0.4971: the difference is exactly 0.0007, OK. But later you quote for the exact k‑unbounded rerun f_void=0.4965 with Δf≈+0.0006; the abstract still has 0.0007. The text mixes both values; either keep one (with a consistent SE and z) or explicitly treat 0.0006/0.0007 as numerically indistinguishable but indicate which is used for all quoted z and p.  
- **Required fix:**
  - Systematically re‑run the arithmetic for **every** σ_from_half, σ_pred, σ_obs−σ_pred, and Δf_CW‑based z and p in tables, in the abstract, and in the text. Use one consistent binomial convention and a single value of ∆f_CW (0.0026 vs 0.0028) in any given calculation, and clearly state when you switch from the Paper IV monopole to the matched‑sample monopole.
  - Where approximations or rounding push inequalities (e.g. “≤1.01×2σ”) into marginal or false territory, either update the numbers or weaken the inequality to something that actually holds with the recomputed values.
  - After recomputation, ensure the numbers in the abstract (floor values, σ, p, Δf_CW) match the final tables.

---

P5‑E8 – Repeated mixing of σ from incompatible null procedures without local caveats
- **Location:** Abstract; §§V–VII, X–XI, XIII.
- **Problem:**
  - You compare or list together:
    - σ_from_half (binomial vs p=0.5),
    - σ_pred (analytic expectation from the catalog monopole),
    - z_Δ from two‑sample tests,
    - permutation‑based p values,
    often in the *same sentence* or paragraph.  
  - While §V defines the different quantities and you note once that σ_from_half scales with √N and “is not comparable across rows,” many later juxtapositions do not contain an explicit local reminder that σ_from_half, σ_vs_monopole, and z_Δ are not directly comparable statistics.
  - Examples:
    - Abstract: void “−0.68σ_from_half” is described as “well inside the 1σ floor… ±2.4 pp,” but later you talk about a “1.64σ” Phase‑2 residual, and “|z| ≈ 2.1σ bright/dark comparison,” with no local statement that “σ” has switched definitions.
    - §VI D cluster follow‑up: you quote σ values for quartiles and also discuss monopole‑subtracted residuals and Bonferroni thresholds; the paragraph relies on the reader remembering the definitions from §V.
    - §X ASTRA: Table XIV quotes “max |σ| vs 1/2,” and in the same section you refer back to V‑Web σ_from_half values and to Bonferroni thresholds defined for other families, again without local caveats.
- **Required fix:**
  - Introduce **distinct notation** (e.g. z_bin, z_mono, z_Δ) and **enforce it everywhere**. For each place where two or more of these appear together, add a short explicit statement such as “These σ arise from different nulls and are not directly comparable; here we only compare each statistic to its own threshold.”
  - In the abstract and conclusions, whenever a “σ” value is quoted, indicate which null it belongs to (e.g. “2.1σ two‑sample z” vs “−0.68σ_from_half”).
  - Re‑read all result sections, especially §VI, §VII, §VIII, §X, and §XI, and insert local disclaimers wherever different σ or z are juxtaposed.

---

P5‑E9 – Abstract and discussion rely on σ and p claims not consistently traceable to a unique location in the body
- **Location:** Abstract, “Headline result” and “Robustness” paragraphs; §XII; Conclusions.
- **Problem:**
  - Several abstract claims either cannot be tied to *one* definitive result statement in the body, or the body contains multiple slightly different versions:
    - “counting‑statistics floor ±2.4 pp… n = 428” – the value appears implicitly in §VI A but is not explicitly calculated there; the number is consistent but not quoted.
    - “Phase 2 sweep… per‑cell range 1.7–4.1 pp… max residual 1.64σ… p=0.13–0.56” – these values come from Table VII and text in §VII, but the ranges in the abstract differ slightly (e.g. abstract: “0.13–0.56”; Table VII: 0.13–0.55). This looks like a stale update.
    - “redshift (label‑shuffle p=0.372)” – §VI B gives p=0.372 for one redshift test, but also mentions p≈0.80–0.81 for stratified shuffles; it is unclear which value is “the” headline redshift result and why.
    - “HEALPix scans p = 0.607/0.135/0.413” – Table VI’s re‑draws give slightly different values (0.64/0.10/0.42), and the text then quotes both the original and re‑draw. The abstract uses only the original set.
  - The discussion and conclusion repeat some of these exact numbers without acknowledging that multiple variants exist in the body.
- **Required fix:**
  - After recomputing all statistics, choose a single definitive value for each *headline* number (e.g. the first free‑shuffle run, or the stratified run) and ensure:
    - Abstract,
    - the specific results subsection,
    - the Discussion (§XII),
    - and Conclusions (§XV)
    all quote the *same* value and uncertainty, or clearly explain when several consistent variants exist.
  - Strip non‑essential specific numbers from the abstract where small stream‑to‑stream variations exist (e.g. 0.135 vs 0.10), and replace with a qualitative statement (“all NSIDE tests give p ≳ 0.1”).

---

P5‑E10 – Some equations and quantitative arguments are dimensionally or conceptually underspecified
- **Location:** §IV A steps 2–9; footnote on units; Appendix A toy EFT mapping.
- **Problem:**
  - In §IV A:
    - You state χ(z) is returned in Mpc and you “multiply by h explicitly to work in h⁻¹ Mpc,” which is dimensionally consistent, but the text uses “Mpc/h” and “h⁻¹ Mpc” interchangeably. That is largely cosmetic, but later you use k in “h Mpc⁻¹” without explicitly stating whether k is constructed from the h⁻¹ Mpc‑scaled box or the original Mpc one. A careful dimensional check is possible but not shown.
    - The Poisson step uses Φ(k) = −δ_k/k² with k≠0. In comoving units with c=1, Φ is dimensionless; that’s fine, but the *normalization* (e.g. factors of 4πG a² ρ̄) is absorbed into Φ, and you never state which convention you adopt. Since only the sign and ordering of eigenvalues are used, this is acceptable physically but should be explicit to avoid dimension confusion.
  - Appendix A:
    - The toy operator \(L_{\rm parity} \supset g_\phi (\nabla\phi)(\nabla\rho/\rho_{bg})(\hat L\cdot\hat z)\) mixes quantities without a clear dimensional accounting. You then write a bound \(|g_\phi \nabla\phi/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{bg}|\rangle\). The left‑hand side has dimensions of (g_\phi × gradient)/H₀, while the right‑hand side is dimensionless; you do not specify the dimensions of g_φ, nor of ∇ϕ, so the statement is formally dimensionally ambiguous.
- **Required fix:**
  - In §IV A, add a short, explicit statement of your unit system: e.g. “We work in comoving units with distances in h⁻¹ Mpc and k in h Mpc⁻¹; we absorb the 4πG a²ρ̄ factor into the definition of Φ, so Φ is dimensionless and only its second derivatives’ sign and ordering matter.” This will make the dimensional consistency of steps 2–9 clear.
  - In Appendix A, either:
    - fully specify the dimensions of g_φ and ∇ϕ and show that the combination \(|g_\phi \nabla\phi/H_0|\) is dimensionless, or
    - remove any equation that *looks* like a quantitative bound and restate the mapping purely qualitatively (“schematically, one expects…”) without a numeric inequality. Given you already say this is not derived, the safest option is to strip that bound entirely.

---

P5‑M6 – Some internal cross‑references point to the wrong objects or mix “parent” populations without warning
- **Location:** §VI A (references to Appendices and JSONs), §VIII F, Appendix B tables.
- **Problem:**
  - You repeatedly refer readers to JSON artifacts and appendix tables for reproduction (e.g. “Table XVI… Table XVII… 21_r23conf_meta_closures.json”), but the narrative sometimes conflates:
    - the 812,793 env‑labeled *row‑level* parent,
    - the 783,820 unique‑galaxy env‑matched subset,
    - and the 791,635 chirality‑relevant matched spirals.  
    For instance, in §VIII F you mention that the σ vs monopole per‑pixel distribution is computed on the env‑labeled parent, but later switch to the unique‑TARGETID parent and quote new σ statistics; the cross‑reference back to Appendix B does not distinguish which parent is used.
  - The abstract and some body text say “χ² = 3.55, 3 d.o.f., p = 0.31 (row‑level parent; χ² = 3.00, p = 0.39 on unique‑spiral subset)”, but Appendix B tabulates only the row‑level contingency table; there is no table for the unique‑spiral version. This makes it impossible for a referee to reproduce the second χ² from the printed paper alone.
- **Required fix:**
  - Whenever you cite a contingency table, explicitly state which parent (row‑level vs unique‑spiral) it uses, and ensure that each χ² or other statistic that is “headline” has an explicit table in the paper itself (not only in repository JSON).
  - Add a second contingency table in Appendix B for the unique‑spiral χ² = 3.00, p = 0.39 case, or, if space is an issue, give the four class counts (CW/CCW) so the reader can reconstruct the test.
  - In the main text, ensure all references to Appendix B indicate which table corresponds to which χ² and which parent sample.

---

P5‑M7 – Several novelty/comparison claims remain weakly supported
- **Location:** Abstract; §VIII B (“largest matched‑sample environmental‑dependence test…”); §XII C (comparison to Shamir 2022).
- **Problem:**
  - You claim the DESIVAST‑anchored re‑analysis is “to our knowledge, the largest matched‑sample environmental‑dependence test of spiral chirality in DESI DR1 to date.” That is plausible, but the paper does not present a systematic comparison to prior DESI‑based chirality studies—only to Shamir 2022 on DESI Legacy imaging (which is not a DR1 spectroscopic cross‑match) and to your own Paper IV. The phrasing “largest matched‑sample… in DESI DR1” is thus somewhat stronger than what’s shown.
  - Similar language (“primary robustness evidence… three‑algorithm DESIVAST robustness… on‑DESI DESIVAST cross‑classifier and Phase 2 V‑Web sensitivity analyses”) borders on “unprecedented” novelty without quantitative survey‑by‑survey comparison.
- **Required fix:**
  - Either soften these claims to something like “a large matched‑sample test” or add a short paragraph explicitly surveying previous *DESI‑based* or DESI‑Legacy‑based chirality/environment tests and stating why your sample is larger (e.g. N vs N, or void‑spiral counts).
  - For the Shamir comparison, explicitly quantify the amplitude and sample differences *in one place* (sample sizes, catalog definitions, redshift ranges), so that the reader sees clearly what is being compared.

---

P5‑M8 – Redshift‑space distortion (RSD) “order‑of‑magnitude” argument still lacks a clearly stated quantitative bound on Δf_CW
- **Location:** §VIII (RSD treatment); §XIII Limitations.
- **Problem:**
  - You describe an RSD Monte Carlo that perturbs line‑of‑sight positions by 5 h⁻¹ Mpc, finds ∼3.4×10⁴ membership changes, and reports that Δf_CW stays within ±0.34–0.37 pp and |z|<2. That is exactly the sort of quantitative bound the initial review asked for, but in §XIII you still describe the RSD discussion as “heuristic” and say you “do not quantify the propagated uncertainty” in the present paper.
- **Required fix:**
  - Promote the ±0.37 pp and max |z|<2 results into §XIII as an explicit quantitative bound: e.g. “Under fixed‑void geometry, RSD‑scale perturbations change void membership by ~34% but shift Δf_CW by at most 0.37 percentage points (|z|<2), which is below our statistical sensitivity.”  
  - Make clear that this bound applies only to the DESIVAST void/non‑void test, not to the internal redistribution among non‑void subclasses, and keep the limitation about not re‑running the full V‑Web in reconstructed space. But do not continue to call the entire RSD discussion purely heuristic when you now have a real Monte‑Carlo bound.

---

P5‑m5 – Minor arithmetic staleness and wording inconsistencies
- **Location:** Abstract; §§VI, VII, VIII, X, XI.
- **Problem:**
  - Some numbers have clearly been updated at one place but not another (e.g. Phase‑2 p‑ranges, HEALPix p‑values, 0.0006 vs 0.0007 for DESIVAST Δf_CW, σ_pred for quintiles). This suggests the manuscript has undergone partial numerical edits without a final global check.
- **Required fix:**
  - After recomputing all statistics as in P5‑E7, run a systematic “number audit”:
    - search for each key number from the abstract and ensure it appears identically (to the chosen precision) wherever re‑used;
    - remove legacy numbers (e.g. 0.10 vs 0.135) that refer to earlier RNG streams and are no longer in the main chosen run.

---

If you address the above, in addition to the issues already identified in the first review, you will have a much more internally consistent and forensically sound manuscript. The key new concerns are: (1) some σ_pred and residual values appear numerically inconsistent with the stated N or with Eq. (1); (2) σ values from different nulls are still mixed without local caveats in several places; and (3) a few abstract/headline numbers do not cleanly track a single, uniquely defined result in the body.