# P5 R24conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.53.pdf` md5=b86b03f9 pages=25
**Input format**: TEXT + web search + pass-2 self-critique (17495 chars)
**Wall time**: 83.1s

---

The manuscript text you provided is extremely long and detailed, but it does **not** include the bibliography: the numbered references [1]– are cited in the body, yet the actual reference list (titles, authors, arXiv IDs, journals, years) is not present. Without the reference list, I cannot perform the citation-forensics tasks you asked for (verifying arXiv IDs, DOIs, titles, authors, and tracing quoted statistics to specific papers). I also cannot see any figures or tables beyond their captions as text. That means I must treat this as a **partial** PDF rendering and cannot deliver the line‑by‑line citation audit PRD would require.

Given those constraints, I will:

- Focus on internal consistency of the text you provided: statistics, σ’s, p-values, counts, internal cross‑checks, and obvious meta‑artifacts.
- Flag structural and policy violations that are visible (e.g., “in preparation” self‑citations, version/audit language, internal log references).
- Identify places where external references *must* be checked against arXiv/ADS once the bibliography is available, and where the paper currently over‑claims or uses “in preparation” work as load‑bearing evidence.

I will not invent details of references I cannot see. Below, “page X” refers to the pages as numbered in your text block (I infer approximate pages where explicit page numbers are missing).

---

### P5‑E1 – Missing reference list (entire paper)

- **Section + page:** End of manuscript, beyond Appendix B (pp. 24–25).
- **Problem:** The manuscript uses references [1]– extensively, but no bibliography is present in the supplied text (no titles, authors, years, journals, arXiv IDs, or DOIs). This makes it impossible to:
  - Verify that each citation corresponds to a real paper with correct metadata.
  - Check that claimed results and quoted numbers (e.g., Planck 2018 parameters, DESIVAST void counts, Tempel 2014 catalog properties, ASTRA EDR stats, Shamir 2022 amplitudes) are actually present in the cited works.
  - Confirm that the “concurrent literature” ,  are correctly described.
- **Required fix:**  
  - Provide a complete reference list listing all cited works [1]–, with full metadata (authors, titles, journals, years, volume/pages, DOIs, and, where applicable, arXiv IDs).  
  - Once provided, a referee (or an editorial check) must verify:  
    - Each arXiv ID is valid and corresponds to the stated title and authors.  
    - Journal, volume, year, and DOI match the arXiv/ADS records.  
    - All quoted numerical claims attributed to these papers (e.g., DESIVAST void counts, ASTRA sample sizes, Shamir amplitudes) trace back to their abstracts, tables, or main text.  
- **Severity:** ESSENTIAL

---

### P5‑E2 – Reliance on “in preparation / not yet peer reviewed” companion papers

- **Section + page:** Abstract (p. 1), Sec. II “Relation to Paper IV” (p. 3), references [3], [4].
- **Problem:**
  - The paper’s entire dataset of chirality labels and the key “catalog monopole” \(\Delta f_{\rm CW} \approx -0.0026\) are imported from **Paper IV [3]**, which is explicitly described as “in preparation and not yet peer reviewed.” Paper II [4] is also “in preparation.”  
  - The abstract calls Paper IV a “companion work, not yet peer-reviewed,” but the current manuscript uses its numerical results and catalog as **load‑bearing**, not just contextual. The headline null result is explicitly *conditional* on the Paper IV monopole and its systematics model.  
  - For PRD, it is not acceptable for a main result to rely critically on unpublished, non‑archived work that can change, be withdrawn, or be significantly revised. The text itself admits a substantial revision to Paper IV’s analysis (“earlier harmonic-space … statistic was withdrawn in Paper IV v1.0.166”), illustrating this risk.
- **Required fix:**
  - Either:
    - Have Paper IV accepted in a reputable, accessible journal or at least posted in a **stable** arXiv version, and then treat this manuscript as *explicitly conditional* on that public record; or
    - Integrate the **core elements of Paper IV that are used here** directly into this paper: data description, classifier architecture, training/validation procedures, the derivation of the monopole offset, and its systematic characterization, with enough detail to stand alone.  
  - In either path, you must:
    - Remove phrases like “in preparation” for the load‑bearing companion and instead cite a stable, public version.
    - Ensure that any earlier withdrawn claims from Paper IV are clearly quarantined and not used here; the text says this is done, but the referee needs to see the final Paper IV record.
- **Severity:** ESSENTIAL

---

### P5‑E3 – Internal version/audit language and pipeline bookkeeping in body text

- **Section + page:** Throughout, especially Appendix B and “Reproducibility checklist” (pp. 24–25), Secs. V, VII, VIII–XI (multiple pages).
- **Problem:** The manuscript contains extensive **internal pipeline and versioning prose** that does not belong in a PRD physics article, for example:
  - “manuscript tag v0.1.53-2026-06-09”
  - “pipelines/p5_desi_chirality/outputs/17_v0151_closure_recomputes.json”
  - “earlier draft quoted … and is withdrawn in favor of the declared-parent recompute”
  - “superseded unfiltered-join version is retained alongside as prefilter legacy”
  - “R23conf_meta_closures.json”, “r23conf_meta_closures”, etc.
  - “reproducibility checklist” bullets describing config paths, RNG seed “20260515”, and file locations.
- These are **review-log / internal-audit artifacts** and version history, violating the instruction to avoid review-log prose and version language in the body. They also make the paper read like a lab notebook rather than a journal article.
- **Required fix:**
  - Remove or severely compress all explicit file paths, git tags, JSON filenames, and “earlier draft” commentary from the main text.  
  - Replace with concise statements such as: “All analysis code and configuration files used in this work are archived in the companion data repository (DOI …). The random seed and configuration details are documented there.”  
  - Reserve any detailed reproducibility checklist for a separate data‑release note or supplementary material, if the journal allows it, but not in the main PRD article.
- **Severity:** MAJOR

---

### P5‑E4 – Excessive dependence on internal “earlier draft” corrections in the narrative

- **Section + page:** Multiple sections, e.g. Sec. VI D, VII, VIII B, IX B, X, XI (various pages).
- **Examples:**
  - “An earlier draft quoted filament bright/dark n of 416,701/21,203 with a 3.4σ two-sample split; those values were computed… and are withdrawn in favor of the declared-parent recompute…”
  - “An earlier draft of this table reported per-cell ranges of 0.05–0.22 pp… and are withdrawn…”
  - “An earlier draft quoted an overlap of 110,586; that join omitted the matched-primary deduplication filter and is withdrawn…”
  - “An earlier draft stated the bright/dark split agreed ‘within ±0.001’; that statement was stale and is corrected here…”
- **Problem:** These “earlier draft” remarks are inappropriate for a final PRD publication and read like an internal revision log. They also complicate the logic for readers: only the **final** numbers should appear, without exhuming prior mistakes in the main text.
- **Required fix:**
  - Remove all “earlier draft” commentary. Present only the **final, correct** numbers, with clear definitions of the parent samples and selection filters. If you want to show robustness to alternative pipelines, provide a clean comparison in a short paragraph or table, without referencing draft errors.
- **Severity:** MAJOR

---

### P5‑E5 – Use of “not directly comparable” caveat for σ across bins

- **Section + page:** Abstract (p. 1), Sec. V (p. 5), Table II (p. 6) and surrounding text.
- **Observation:** The instructions say: *“If sigma values from different null procedures appear side-by-side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.”*
- In the abstract, you explicitly write:  
  > “The quoted σ_from half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n.”  
  In Sec. V you also carefully distinguish σ_from half vs σ_pred and emphasize the scaling with \(N\).
- **Assessment:** The paper repeatedly and explicitly warns that σ’s from different bins are not directly comparable, and it systematically re-expresses class differences via **monopole-subtracted residuals** and χ² tests instead of comparing raw σ across bins.
- **Required fix:** None for this instruction: the caveat is present where needed, including in the abstract. Just ensure every figure or table that shows multiple σ_from half values (e.g., Table II, Fig. 3) either:
  - Includes a caption note that σ_from half is not comparable across different n; or
  - Points clearly to Sec. V where this is explained.
- **Severity:** NIT (just confirm captions are aligned)

---

### P5‑E6 – Over-use of internal filenames and pipelines as de facto citations

- **Section + page:** Throughout, e.g. Sec. VI A, VI C, VII, VIII B–F, IX A–C.
- **Problem:** Instead of citing a formal data or code DOI, you repeatedly refer to internal file paths like:
  - `pipelines/p5_desi_chirality/outputs/21_r23conf_meta_closures.json`
  - `outputs/16_cosmic_web_zshell_corrected.json`
  - `results/analysis_astra_per_object/cw_fraction_by_env_astra.csv`
- This is pseudo‑citation that is not stable or interpretable for future readers; it also makes the paper fragile to repository reorganization.
- **Required fix:**
  - Provide a **single DOI** for the code/data archive (Zenodo or similar) as suggested in Appendix B, and then cite it once in the main text and in the references.  
  - Remove the low‑level paths from the text, or move them to a separate README in the archive.
- **Severity:** MAJOR

---

### P5‑E7 – Ambiguous or informal statements about external literature without explicit reference details

Because the reference list is missing, I can’t verify these fully, but there are several places where you make strong claims about prior work:

- **Shamir 2022 (ref ):** You quote:
  - “a ∼ 2–4% large-scale asymmetry on ∼ 1.3 × 10⁶ Ganalyzer-classified galaxies” and an amplitude “about an order of magnitude larger” than your bound. This must be checked against Shamir’s abstract and figures once the reference is present.
- **DESIVAST (ref ):** You attribute:
  - Specific counts: “1,461 interior voids,” “420 with V2-REVOLVER, 295 with V2-VIDE,” “101,863 holes,” “3,765 maximal voids,” etc.
- **ASTRA (ref ):** You quote:
  - Sample sizes (648,428 unique targets), EDR footprint (≈175 deg²), number of realizations (“100 realizations per tracer‑zone pair”).

Without the full references:

- **Required fix:**
  - Once the bibliography is provided, check each of these numeric claims directly against the cited papers or data release notes (arXiv or ADS). Ensure every quoted number and qualitative statement (“probabilistic classifier with 100 realizations per tracer-zone pair”) is explicitly supported.
  - If any of these details are from private communication or not in the public release, they must be downgraded or clearly labeled as such.
- **Severity:** ESSENTIAL (once references appear)

---

### P5‑M1 – Length and focus relative to contribution

- **Overall:** The manuscript is 25 pages and reads more like a full pipeline technical report than a concise cosmology methods paper. Large portions of the text are devoted to:
  - Detailed internal re‑runs (“Phase 2 sweep,” z-shell corrected, geometry‑footprint corrections).
  - Extensive bright/dark, density, HEALPix, max‑voids/pixel, ASTRA/Tempel/T-Web cross‑checks, each with path-level provenance.
- **Problem:** PRD expects a focused presentation of the **physics result**. Here, the core physics content is:
  - Definition of matched spiral sample.
  - Description of environment classifiers and the main DESIVAST void test.
  - Statistical test of chirality vs environment.
- Much of the heavy internal-audit and cross‑check narrative could be significantly compressed or moved to supplementary materials.
- **Required fix:**
  - Reduce the main text to a tighter narrative of at most **15–18 journal pages** (PRD 2‑column style), focusing on:
    - Data and cross‑match.
    - Environment classification (V-Web plus DESIVAST).
    - Main chirality vs environment tests and essential robustness checks (a subset of the most informative ones).
  - Move detailed pipeline descriptions, file names, multiple re‑runs, and exhaustive cross‑checks (especially those that simply reconfirm nulls at the 1–2σ level) into an online supplement or the data/code repository.
- **Severity:** MAJOR

---

### P5‑M2 – Overly informal tone and frequent self‑referential remarks

- **Section + page:** multiple; examples:
  - “We deliberately keep the parameterization schematic.”
  - “a real exclusion would require… we do not claim either calculation here; the parameterization is included as a guide…”
  - “we caution that…”
  - “this is a strong robustness result” etc.
- **Problem:** The narrative is unusually conversational for PRD, with explicit commentary on the author’s choices, prior drafts, and internal decisions. While not fatal, it detracts from the scientific clarity and can be perceived as advocating rather than reporting.
- **Required fix:**
  - Edit to a more neutral, impersonal scientific tone: describe procedures and results without discourse on “drafts,” “we deliberately,” or “we caution,” unless genuinely needed for clarity.
- **Severity:** MINOR

---

### P5‑M3 – EFT “toy operator” in Appendix A is speculative and poorly grounded in cited literature

- **Section + page:** Appendix A (pp. 24–25).
- **Problem:**
  - You introduce a specific operator \(L_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat{L}\cdot\hat{z})\) and then explicitly admit that this form is *not* present in [1] or [2], and is not gauge invariant.
  - The appendix then loosely maps your observational bound to an order‑of‑magnitude bound \(|g_\phi (\nabla\phi)/H_0|\lesssim 10^{-2}\) without a proper derivation.
- **Required fix:**
  - Either:
    - Remove Appendix A entirely, or
    - Replace it with a rigorously derived, gauge‑invariant EFT mapping, including clear assumptions, and only if it is of genuine interest to PRD’s theoretical readership.
  - As it stands, Appendix A is speculative and only loosely connected to the main analysis; it risks confusing readers and over‑interpreting the observational null.
- **Severity:** MAJOR

---

### P5‑M4 – Statements of “largest” or “most rigorous” (if present)

I saw: “This is, to our knowledge, the largest matched‑sample environmental‑dependence test of spiral chirality in DESI DR1 to date…” (Sec. VIII B).  

- **Problem:** This type of novelty claim is acceptable if narrowly stated (“in DESI DR1”) and if true. However, without a complete literature survey in the references (including any other DESI DR1 environment‑chirality works, or other large survey chirality‑environment tests), it might overstate novelty.
- **Required fix:**
  - Qualify such statements even more carefully, e.g.: “Within DESI DR1 and given publicly available catalogs as of 2026, we are not aware of a larger matched‑sample chirality vs void test.”  
  - Ensure the reference list includes any known competing analyses; once the list is available, an editor/referee should check this.
- **Severity:** MINOR

---

### P5‑N1 – Duplicate phrase / potential typo checks

Given the length, I did not see obvious two‑word duplicates like “canonical canonical-mask,” but there are a few clunky constructions:

- “survey-edge artifact dominated    √ at z ≲ 0.24” – the spacing and stray square-root symbol look like a typesetting artifact.
- “cluster-restricted dark sample will be ≳ 5× larger.” – stylistically fine, but check the “≳” rendering in PRD style.
- Various small hyphenation inconsistencies (“per-object” vs “per object,” “near-unsmoothed”).

- **Required fix:**
  - Run a careful LaTeX and copy‑edit pass to fix stray math symbols, spacing, and hyphenation.
- **Severity:** NIT

---

### P5‑M5 – Abstract is very dense and mixes method, robustness, and internal caveats

- **Section + page:** Abstract (p. 1).
- **Problem:**
  - The abstract is extremely long, mixing:
    - Detailed internal counts (812,793/783,820/7,815).
    - Multiple σ values, χ² values, and specific p-values.
    - Detailed Phase 2 sweep parameters and program‑specific diagnostics.
  - For PRD, the abstract should emphasize:
    - The question asked.
    - The main result (no environment dependence at a given sensitivity).
    - The main method and one or two key robustness checks, not the entire audit trace.
- **Required fix:**
  - Shorten and refocus the abstract so it:
    - Clearly states the null result and the dominant sensitivity scale.
    - Summarizes the main dataset and environment classifiers briefly.
    - Confines detailed σ, p, and program-specific caveats to the main text.
- **Severity:** MAJOR (presentation)

---

### P5‑M6 – Load-bearing scalar consistency (abstract vs body)

Given what is visible, I checked several key numbers for internal consistency:

- **812,793 / 783,820 / 7,815**:  
  - Later you explain: 812,793 env-labeled rows from 783,820 unique spirals, with 7,815 matched spirals lacking an environment row. This is logically consistent.
- **Per-class counts in Table II**:  
  - 428 + 6,673 + 408,187 + 397,505 = 812,793, matches the env-labeled parent.
- **f_CW values** in Table II roughly match the stated σ_from half; precise re‑computation is not possible without full n_CW, but the scale seems plausible (you supply n_CW so in principle it’s checkable).
- **χ² and p** for the 4×2 table: you report χ² = 3.55 with 3 d.o.f., p = 0.31, which is numerically consistent with standard χ² tables.

I did not find obvious internal contradictions in these headline scalars, though I cannot recompute all σ and p-values without raw counts from all sub‑bins.

- **Required fix:** None obvious, but a full referee with access to all tables and the actual PDF must:
  - Recompute a handful of σ and χ² values from the provided counts to confirm no arithmetic mistakes.
  - Make sure every abstract number is present and consistent in the body.
- **Severity:** MINOR (pending full numerical audit).

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific result―a carefully conditioned null detection of environment‑dependent spiral chirality in DESI DR1 with robust void-based tests―is potentially suitable for PRD, but the current manuscript falls short of PRD standards on several fronts: it lacks a visible reference list; it relies critically on an unpublished companion (Paper IV) for its catalog and monopole model; it is overloaded with internal pipeline/versioning prose and “earlier draft” commentary; and it includes a speculative EFT appendix that is not tightly grounded in the cited theory literature. A substantial editorial and structural revision is required: provide a complete bibliography and verify all external claims; either stabilize or internalize Paper IV; remove internal audit logs and draft history from the body; streamline the presentation (especially the abstract and Sections V–XI); and, ideally, excise or rigorously reformulate the EFT toy mapping. Only after these changes, and with full citation verification, should the paper be reconsidered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

[P5-E8] The abstract’s statement that the paper tests a **“8,474,531-galaxy chirality catalog”** against DR1 appears internally inconsistent with the manuscript’s own data section, which says Paper IV’s catalog is 8,474,531 galaxies but only **791,635** are chirality-relevant matched spirals used here; the abstract’s phrasing can be read as if the full 8.47M are being analyzed in this paper, which the body does *not* support. The body makes clear that the actual environment analysis is on the matched spiral subsample, so the abstract should explicitly say so to avoid overstating the analyzed sample size.[1]

[P5-E9] The abstract’s claim that the **“controlling void constraint comes from the DESIVAST-anchored re-projection (n = 56,981, ∆fCW = 0.0007)”** is not numerically consistent with Table VII and Section VIII B, where the DESIVAST void fraction is **0.4964**, the non-void fraction is **0.4971**, and the difference is **0.0007**; however, the table also shows the void-bin shift in σ-space is **−1.71**, not a near-zero significance. The text is technically consistent on the fraction difference, but the abstract omits that the constraint is sample-size powered and can be misread as a strong null significance rather than a small raw fraction gap.[1]

[P5-E10] The abstract states that the V-Web void class is at **“n = 428”** and that the observed offset is **“−0.68σfrom half”**; Table II gives the void bin as **428** with **fCW = 0.4836** and **σfrom half = −0.68**, so this matches. However, the same sentence also says the binomial half-width is **“±4.8 pp”**, which is only true if one uses a 2σ estimate on \(n=428\); the body later uses **95% Jeffreys intervals** and other σ conventions. The abstract should state explicitly which uncertainty convention is being quoted, because the current wording mixes a 2σ binomial floor with 1σ σfrom half language.[1]

[P5-E11] The abstract says the **“quoted σfrom half values scale as n at fixed fractional offset”**. This is a direct arithmetic error: \(\sigma_{\text{from half}} = (n_{\rm CW}-0.5N)/(0.5\sqrt{N})\) scales as **\(\sqrt{N}\)** at fixed fractional offset, not \(N\). The body later states the correct \(\sqrt{N}\) scaling in Section V, so the abstract contains a typo-level but mathematically significant mistake that should be corrected everywhere it appears.[1]

[P5-E12] The abstract reports **“the range across classes is 1.98 percentage points”** and **“χ² = 3.55, 3 d.o.f., p = 0.31 on the row-level parent; χ² = 3.00, p = 0.39 on the 783,820 unique-spiral subset.”** These are internally consistent with Table II and the body, but the abstract omits the fact that the unique-spiral recomputation is on **783,820**, not the full **791,635** chirality-relevant sample. Because the conclusion relies on the duplicate-row correction, the abstract is incomplete unless it states that the omnibus test is robust under the deduplication step.[1]

[P5-E13] The abstract says the Phase 2 sweep spans **“n = 363–853 per cell”** and the per-cell cross-class range is **“1.7–4.1 percentage points.”** Table VI gives the exact ranges **1.72, 2.71, 2.01, 1.97, 2.48, 1.83, 3.69, 4.12, 2.81**, so the body supports the stated interval. But the abstract’s wording compresses the result too aggressively: the largest range is **4.12 pp**, not merely “4.1,” and the minimum is **1.72 pp**, not “1.7.” This is not a logical contradiction, but it is a rounding issue that should be kept consistent with the table if the abstract is meant to be exact.[1]

[P5-E14] The abstract says the **“label-shuffle look-elsewhere p-values span 0.13–0.56”** and later gives **“no cell below 0.05.”** Table VI indeed lists p-values **0.56, 0.42, 0.38, 0.13, 0.14, 0.23, 0.34, 0.41, 0.48**. That matches. However, the abstract omits that the **canonical** cell is the one at **p = 0.13**, which is still not close to the Bonferroni threshold. This is not an error, but it is a place where the paper could more explicitly prevent readers from overinterpreting the smallest p-value.[1]

[P5-E15] The abstract says **“the V-Web void class at z ≲ 0.24 is sample-size limited at n = 428 chirality-relevant spirals and dominated by survey-edge artifacts.”** Section VIII and Table II support the n=428 value, but the body later shows that the **DESIVAST-anchored** void sample is **56,981**, and the survey-edge artifact issue is specifically a property of the **V-Web void label**, not the underlying chirality sample. The abstract compresses two different void notions into one sentence and risks conflating the V-Web void bin with the DESIVAST void cross-check.[1]

[P5-E16] The sentence in the abstract stating **“the controlling void constraint comes from the DESIVAST-anchored re-projection (n = 56,981, ∆fCW = 0.0007) rather than the V-Web void label”** is supported by Section VIII B, but the body gives a more precise result: the DESIVAST void class is **0.4964** vs **0.4971** non-void, and the catalog-native V2-REVOLVER definition gives **σ = −0.24** on **n = 86,276**. The abstract mentions only one DESIVAST number and therefore underrepresents the stronger internal evidence from the catalog-native cross-checks.[1]

[P5-E17] In the Introduction, the sentence **“The present paper is a focused, environment-conditional null test”** is supported, but the follow-on claim that **“No published bounce or inflation model currently predicts a specific environment-conditional chirality signature at this scale”** is *not directly substantiated* anywhere in the body by a systematic literature survey. The paper later states this again in the conclusions, but the supporting comparison remains qualitative. This is an unsupported novelty-by-absence claim unless the author adds an explicit survey of the relevant model literature.[1]

[P5-E18] Section II says Paper IV’s **“current headline (v1.0.166) is a real-space full-sky dipole null at +0.43σ (p = 0.30)”** and that an earlier harmonic-space statistic was withdrawn. In the conclusion, however, the paper refers to a **“∼ 9.5σ catalog-level monopole reported in Paper IV.”** Those two statements are not the same quantity, and the body never clearly reconciles them as separate statistics. The manuscript needs an explicit distinction between the **catalog-wide monopole significance** and the **dipole null**, otherwise the reader can easily infer an impossible inconsistency.[1]

[P5-E19] The discussion says Paper IV finds a **“full-sky dipole amplitude |A| < 0.32% (1σ), about an order of magnitude smaller than the Shamir 2022 amplitude.”** The body also says Shamir’s amplitude is **2–4%**, so the order-of-magnitude comparison is arithmetically fine. But later the paper says the present environment-dependent null would require **“2–4 pp”** to matter in at least one class. These are different metrics — percent points versus percent amplitude — and the manuscript never explicitly converts them into the same basis. That is an unquantified comparison that should be normalized before making the “order of magnitude” claim.[1]

[P5-E20] Section VI D says the bright-vs-dark difference in the filament class is **“|z| ≈ 2.1σ on the filament class”**, while the same section later gives the whole-catalog bright-vs-dark difference as **“0.81 pp, |z| ≈ 2.0σ.”** The two statements are compatible, but the manuscript never shows the arithmetic linking the **2.1σ** per-class result to the **2.0σ** whole-catalog result. Because one is row-level and one is whole-catalog, they are not directly comparable without the underlying counts; the text should say so more explicitly.[1]

[P5-E21] Table IV and the surrounding text claim that within-class density stratification gives cluster quartile values **−3.07, −3.42, −0.37, −2.46** and filament quartiles **−0.69, −1.97, −0.63, −1.92**. The text then says the cluster signal is not monotonically increasing in density and that the within-class density-stratified follow-up reinforces the null. Arithmetic check: the cluster quartile range is **3.05 σ**, which is not a trivial null-looking scatter if read naively. The manuscript’s inference is only valid because it subtracts the catalog monopole; without that subtraction, the raw spread looks signal-like. This should be stated more sharply to prevent misreading the table as evidence *for* structure rather than *after* monopole removal.[1]

[P5-E22] In Section VII, the manuscript says the maximum single-cell \(|\sigma_{\rm from\ half}|\) is **4.66** at the canonical \(R_s = 25\), \(\lambda_{\rm th}=0\) cell, and then says this is “the catalog-wide monopole leaking through a large sample bin” with **\(\sigma_{\rm pred} \approx -3.3\)** and a **monopole-subtracted residual of −1.38**. That arithmetic works only if one uses the per-class \(n\) and not the sweep’s bin population generically. The text needs to show the exact \(n\) used in the prediction directly in the sentence, because otherwise the residual is not reproducible from the immediately adjacent numbers.[1]

[P5-E23] Section VIII C says V2-REVOLVER has **catalog-native \(n_{\rm void}=86,276\)** and **\(\sigma_{\rm void}=-0.24\)**, while the sphere-approximation gave **\(n_{\rm void}=56,981\)** and **\(\sigma_{\rm void}=-0.88\)**. The body says the native definition excludes survey-mask edge galaxies and is “the cleaner statistic.” That conclusion is directionally plausible, but the manuscript never quantifies whether the shift in \(n\) is expected from the changed void definition. A reviewer would want to know whether the two definitions are *supposed* to differ by ~29,000 galaxies or whether this is unexpectedly large; the paper currently leaves that comparison unquantified.[1]

[P5-E24] In Section VIII E / Table IX, the manuscript states that the **“0 maximal voids per pixel”** bin has **\(n = 378,511\)** and **\(\sigma = -4.75\)**, while the **6+** bin has **\(n = 258,060\)** and **\(\sigma = -2.04\)**. The text then claims the **Paper IV monopole prediction** at \(N=378,511\) is **\(-3.20\)** and the observed residual is **\(-1.55\)**. Arithmetic check: using the earlier paper’s \(\Delta f_{CW} = -0.0026\), \(2|\Delta f|\sqrt{N}\) gives about **3.20**, so the residual is indeed about **1.55**. That matches. But the manuscript never similarly computes the expected \(\sigma_{\rm pred}\) for the 6+ bin in the table itself, only in prose. This asymmetry makes the table harder to audit than necessary.[1]

[P5-E25] The Section IX B Tempel cross-validation says the overlap is **96,753** spirals, with **95,247** carrying a V-Web environment row and **1,506** lacking one, and that the like-for-like filament concordance is **0.29 pp**. The table, however, gives only the Tempel class counts and the prose gives the V-Web-on-overlap filament count **16,701**. If one checks the numbers, the total V-Web overlap counts listed in the bullets are **23 + 145 + 16,701 + 78,378 = 95,247**, which is consistent. But the manuscript never explicitly states that the 1,506 missing rows are excluded from the like-for-like comparison, so a reader can mistakenly assume the 96,753 overlap all enter the concordance metric. That exclusion should be made explicit in the paragraph where the 0.29 pp number appears.[1]

[P5-E26] The ASTRA cross-validation says the overlap sample is **25,186** and that the ASTRA argmax and V-Web assignments disagree strongly, yet the chirality-vs-environment conclusion is the same. Table XII lists **V-Web on same overlap: fCW range 1.08 pp, max |σ| = 2.68, per-class n = 1 / 2 / 7,972 / 17,211**, while ASTRA argmax has **2.08 pp, max |σ| = 2.25**. The V-Web per-class n values sum to **25,186**, so the table is internally consistent. But the phrase **“same conclusion”** is too strong unless the manuscript explicitly notes that the V-Web overlap still has only **3** spirals in the void+wall classes combined; the agreement is driven almost entirely by filament + cluster. That limitation is present in prose, but the summary sentence should not overgeneralize across all four classes.[1]

[P5-E27] The systematics section says the **confidence-threshold sweep** drifts by at most **−0.24 pp** from the full-sample value at **\(p_{\rm cls}^{\rm eq} \ge 0.7\)** and that this is “a ≤ 1σ shift at the reduced \(n\).” Table XIII lists the actual fCW values as **0.4971, 0.4954, 0.4948, 0.4950** for thresholds **0.4, 0.6, 0.7, 0.8**. Relative to the full-sample **0.49719**, the largest raw deviation is actually **0.24 pp** at the 0.7 cut and **0.22 pp** at the 0.8 cut, so the prose is consistent. However, the paper does not show the corresponding counts for the 0.7 and 0.8 cuts in the main text sentence, even though the table does. A reviewer could miss that the apparent stability is partly a consequence of the much smaller retained sample at high confidence thresholds.[1]

[P5-E28] Section XII C says the present paper constrains an environment-conditioned chirality asymmetry of the **Shamir 2022 amplitude (2–4 pp)** and that the current classes sit at **\(\sim 0.497\)** with inter-class range **1.98 pp**. This comparison is not apples-to-apples: Shamir’s figure is a *global asymmetry amplitude* in a different catalog and methodology, while 1.98 pp is a *range across four environment bins* in this paper. The manuscript should not imply a direct amplitude bound unless it translates the class-range into the same observable as Shamir’s statistic.[1]

[P5-E29] The limitations section says the **RSD displacement scale** is **\(\sigma_v/(aH) \lesssim 5\text{–}8\) Mpc/h**, which is “a factor of \(\sim 3\text{–}5\) smaller than the chosen Gaussian smoothing scale \(R_s = 25\) Mpc/h.” That arithmetic is fine. But the same section then says the implied per-class \(\Delta f_{CW}\) contamination is **\(\sim 0.2\) pp**, which is not derived anywhere from the earlier numbers. This is an unsupported quantitative estimate; the text should show the calculation or soften the claim to a qualitative expectation.[1]

[P5-E30] Appendix A says the toy EFT mapping gives an order-of-magnitude bound **\(|g_\phi(\nabla\phi)/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\)** and then later says this is **“not a quantitative ALP-coupling exclusion.”** Those two statements are compatible, but the manuscript never specifies what \(\langle|\Delta\rho/\rho_{\rm bg}|\rangle\) is numerically. Without that, the bound is symbolic only. If the appendix is retained, it should provide an explicit fiducial value or a range for the density contrast so the reader can interpret the inequality.[1]

[P5-E31] Appendix B says the manuscript corresponds to **tag v0.1.53-2026-06-09** and that a **DOI-minted archival snapshot** accompanies submission. But the main text repeatedly references **“pipelines/p5_desi_chirality/outputs/17_v0151_closure_recomputes.json”** and similar files. That creates a version mismatch: the manuscript tag is **v0.1.53**, while the analysis artifacts are **v0151** and **v0151**-prefixed. The paper never explains the relation between these version schemes, so a reviewer cannot tell whether the cited files are in sync with the manuscript version or leftovers from an earlier analysis branch.[1]

[P5-E32] The conclusion says the result is robust under **“nine (Rs, λth) Phase 2 sweep cells, under grid resolutions 1283–3843, and under six classes of systematics tests.”** The body does discuss Phase 2, grid resolution, and systematics, but the count **“six classes”** is not explicitly enumerated in one place. A reviewer has to piece together the six from the earlier sections. That is not an arithmetic error, but it is a completeness issue: the conclusion should name the six tests so the reader can verify the count.[1]

[P5-E33] The paper’s own arithmetic shows the canonical V-Web class counts in Table II sum to **812,793**, and the unique-spiral counts sum to **783,820**. The difference is **28,973** rows, while the prose says the row-level parent repeats **2.7%** of TARGETIDs and that **7,815** spirals lack an environment row. These numbers are not directly the same quantity, so the manuscript should avoid mixing them without explanation. As written, the reader must infer that the remaining difference is due to duplicated environment rows from repeat coadds; that inference is reasonable but not explicitly laid out in one place.[1]

[P5-E34] The body says the V-Web class vs target-program contingency test gives **χ² = 4932, 3 d.o.f., p \ll 10^{-300}** and max class-to-overall bright-fraction deviation **1.5 pp**. That \(\chi^2\) is enormous relative to the 1.5 pp deviation, which is plausible only because of the very large \(n\). The manuscript never provides the underlying \(2 \times 4\) table or expected counts in the same location, so the reader cannot verify the calculation from the displayed numbers alone. This is a missing arithmetic audit trail, not necessarily an error, but it is exactly the sort of thing PRD reviewers often flag.[1]

[P5-E35] The manuscript repeatedly states that the **DESIVAST-anchored primary analysis is “∼130× larger”** than the V-Web void sample. Using the paper’s own counts, \(56{,}981 / 428 \approx 133.1\), so **“∼130×”** is fine. But the same section also says the DESIVAST result is “properly powered,” while the V-Web void sample is “sample-size limited.” That is consistent, but the paper should consider using the exact ratio **133×** in the main text rather than a rounded 130×, because the ratio is a headline comparative claim.[1]

