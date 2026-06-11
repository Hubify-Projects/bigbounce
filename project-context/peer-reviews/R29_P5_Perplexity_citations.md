# P5 R29 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.61.pdf` md5=5eb81cd5 pages=30
**Input format**: TEXT + web search + pass-2 self-critique (14337 chars)
**Wall time**: 93.7s

---

I cannot access the actual rendered PDF of this manuscript or its reference list; I only see the plain text you provided. Without the full bibliography and without the ability to view figures, tables, or the actual reference entries, I cannot perform the citation-forensics audit you requested (verification of arXiv IDs, DOIs, venues, author lists, figure axes, etc.) at Physical Review D standards.

Given those constraints, I will instead flag issues that are already visible in the provided text and that would, by themselves, prevent acceptance in PRD. Every item below is based solely on the text you supplied.

---

## ESSENTIAL issues

### P5-E1 – Reliance on an unpublished “companion” catalog as load‑bearing input  
- **Location:** Abstract (page 1), §II, multiple later sections where “Paper IV [3]” and its catalog are used.  
- **Problem:** The analysis *critically* depends on the 8.47M‑galaxy chirality catalog and on its calibrated monopole offset from “Paper IV [3]”, which is explicitly described as “in preparation” and “not yet peer reviewed.” The monopole correction, the classification quality, and the claimed 9σ catalog-level monopole are all taken as fixed inputs, and the central environment-independence claim is made *conditional* on that catalog being correct. There is no independent re-validation of the classifier in this paper. For PRD, a central result cannot rest on an unpublished, non-public, mutable “companion” without either (i) reproducing the relevant parts in a fully self-contained way or (ii) using a frozen public catalog whose properties are independently verifiable.  
- **Required fix:**  
  - Either (a) publish Paper IV and update this manuscript to reference the *published* version, or (b) make this paper self-contained by including a complete description, validation, and recalculation of the chirality classifier and its monopole offset (training, tests, nulls) to PRD standards, with all required data and code made available.  
  - Explicitly state in the abstract and in §II that *all* environment null claims are conditional on the accuracy of this internally generated classifier, and quantify the impact of possible miscalibration on the environment tests.

### P5-E2 – Versioning / draft-status language in the body  
- **Location:** Title block, first page: “(Dated: June 2026 — v0.1.61-2026-06-10)”  
- **Problem:** The manuscript carries internal versioning (“v0.1.61-2026-06-10”), which is draft bookkeeping, not appropriate in a PRD submission. The instructions you gave specifically say to flag version-history / internal tags.  
- **Required fix:**  
  - Remove internal version IDs from the title block and any other locations. Use only a standard date if the journal allows it or omit entirely, per PRD style.

### P5-E3 – Multiple explicit references to earlier drafts, corrections, and withdrawn numbers inside the main text  
- **Location:** Many places throughout, e.g.  
  - §II: “an earlier harmonic-space … statistic was withdrawn in Paper IV v1.0.166…”  
  - §VI A: “pipelines/…; an earlier draft attributed the excess to a ‘relaxed env-label confidence filter’; … replaces that description.”  
  - §VI D: “An earlier draft quoted filament bright/dark n … those values were computed on an unfiltered nearest-label join … and are withdrawn in favor of the declared-parent recompute.”  
  - §VII: “An earlier draft of this table reported per-cell ranges of 0.05–0.22 pp … those values are withdrawn…”  
  - §VIII D: “An earlier draft reported nvoid = 86,276 / 64,514 … reproduce exactly only under a zone-indexing defect … supersede them.”  
  - §IX B, IX C, §X, §XI, etc.: multiple “earlier draft”, “superseded”, “withdrawn” statements.  
- **Problem:** The manuscript reads like a lab notebook or internal audit log, with extensive prose about previous drafts and bugs. PRD expects a clean, final analysis; internal history belongs in a private log or, if absolutely necessary, a short note in an appendix. As written, this makes the narrative confusing and raises questions about whether all errors have truly been fixed.  
- **Required fix:**  
  - Remove all “earlier draft”, “withdrawn”, “superseded”, and similar historical commentary from the main text.  
  - Present only the final analysis and results. If some corrections must be documented for transparency, move them to a brief “Errata relative to internal pipeline versions” appendix, with concise statements.

### P5-E4 – Heavy dependence on internal pipeline files as primary “citations” for quantitative claims  
- **Location:** Many sections, e.g. §VI A (“pipelines/p5_desi_chirality/outputs/21_r23conf_meta_closures.json”), §V, §VII, §VIII, IX, X, XI, Appendix B.  
- **Problem:** The manuscript repeatedly cites internal JSON and CSV artifacts under a GitHub directory tree as if they were referenceable scientific sources. PRD requires that all load‑bearing data products and code be archived with persistent identifiers (e.g. Zenodo DOI, institutional repository) and that key results be reproducible from information in the paper and the archived material. Raw pathnames in a private repository are not acceptable provenance.  
- **Required fix:**  
  - Publish a frozen, citable archive of all analysis code and data products used for the paper (e.g. Zenodo) and refer to that archive in a proper Data Availability section and/or in the references.  
  - In the main text, replace raw paths like `pipelines/.../outputs/17_v0151_closure_recomputes.json` with a short description + pointer to the archived artifact (e.g. “see Archive A1, file X”).  
  - Ensure that a competent reader can reproduce the numbers without needing access to a private repo.

### P5-E5 – Abstract claims rely on significance language without always giving effect sizes and with mixing of incomparable σ’s  
- **Location:** Abstract, long paragraph.  
- **Problem:**  
  - The abstract mixes several σ‑based statements from different tests (per-class σ from half, monopole-subtracted residuals, label-shuffle p-values) in a single narrative. You do state once that σfrom half is not comparable across classes, but in the abstract itself, different “σ” statements appear side-by-side and can easily be misread as directly comparable.  
  - PRD-level statistical reporting requires that every headline σ/p result has a clear associated effect size. For instance, “cluster class σ = −4.66” is mentioned (in the abstract and body) but only later is it emphasized that this is entirely due to the global monopole; in the abstract this nuance is easy to miss.  
- **Required fix:**  
  - In the abstract, explicitly qualify *every* σ that is not a direct test of the same null and same statistic as “not directly comparable across classes/procedures,” or remove σ values that are purely incidental and emphasize the effect sizes (percentage-point differences, ranges).  
  - For each abstract σ or p‑value, directly mention the corresponding effect size (ΔfCW, range in percentage points, etc.), which you often have in the body.

### P5-E6 – Abstract-last drift: abstract overstates the status of the companion classifier and of the DESI/ASTRA cross-checks  
- **Location:** Abstract, end of first paragraph and “Robustness” part.  
- **Problem:**  
  - The abstract treats the Paper IV catalog and its monopole offset as a solid “known” systematic and uses it as a foundation, but §II acknowledges that the harmonic-space statistic was withdrawn and that aspects of Paper IV evolved. To pass the abstract–body consistency test, you must either soften the abstract or more carefully qualify the reliance on an evolving in-preparation work.  
  - The abstract’s robustness paragraph gives roughly equal rhetorical weight to several cross-checks (Tempel FoF, ASTRA EDR, DESIVAST three-algorithm consistency) although in the body you yourself say ASTRA is “supporting rather than load‑bearing” and EDR overlap is small.  
- **Required fix:**  
  - Rephrase the abstract so that it clearly states: (a) the catalog and its monopole correction come from an in-preparation companion paper, and (b) cross-checks such as Tempel FoF and ASTRA are limited in scope/overlap and are supporting only.  
  - Ensure the strength of every claim in the abstract is no stronger than the most careful statement in the body.

### P5-E7 – Standalone-reader test: dependence on multiple “companion papers” for physical motivation and model mapping  
- **Location:** §I–II, §XII B, Appendix A.  
- **Problem:** Key parts of the interpretation (“bounce-chirality coupling class”, discrimination vs inflation, relation to “Paper II”, “Paper III”) are pushed into unpublished companion works. For a PRD paper, the reader should not need to read non-existent companion papers to understand what physical models are being tested, what parameter space is being constrained, and how.  
- **Required fix:**  
  - Either remove the detailed bounce/inflation discrimination discussion from this paper altogether and present it once in a later, self-contained theory paper, or substantially expand §II and Appendix A to give a complete, consistent, *self-contained* formulation of the relevant model space and how your bounds map onto it.  
  - Do not rely on “Paper II” or “Paper III” for any load‑bearing argument; any such dependence must be removed or reproduced here.

### P5-E8 – Data availability / reproducibility not yet at PRD standard  
- **Location:** Appendix B and scattered pipeline references.  
- **Problem:** Appendix B describes a GitHub repo and internal directories; there is no explicit commitment that the exact code and data used for the analysis will be publicly archived with a stable identifier at the time of publication. The DESIVAST, DR1, and ASTRA data are public, but your cross-match, environment tables, and derived products are not clearly specified as public artifacts.  
- **Required fix:**  
  - Provide a formal Data and Code Availability section stating clearly:  
    - where the cross-matched catalogs, environment labels, and analysis scripts are archived (with DOI),  
    - what version of the DESI DR1 and DESIVAST catalogs you used, and  
    - how a reader can exactly reproduce the main tables and figures.  
  - Ensure the pipeline is actually runnable without private infrastructure.

### P5-E9 – Use of in-preparation / preprint references as if they were fully stable  
- **Location:** References [3], [4], ,  (described in text).  
- **Problem:** You cite several works in preparation or preprints as if they were fixed. In particular, [3] is “in preparation”;  and  are described as “preprint (2026)” and not yet published. PRD allows preprint citations but where they are *load‑bearing* (here, [3]), this is problematic.  
- **Required fix:**  
  - For [3], resolve as in P5‑E1.  
  - For  and , clearly label them as preprints and ensure that no quantitative claim in your paper *depends* critically on their content (right now you mostly use them as context/cross-check; that is acceptable once clearly labeled).

---

## MAJOR issues

### P5-M1 – Length and narrative structure vs. contribution  
- **Location:** Entire manuscript (~30 pages of dense text plus many internal pipeline discussions).  
- **Problem:** For what is essentially a single null result (“no environment dependence within current sensitivity”), the manuscript is very long and includes extensive pipeline/method-history prose, multiple minor cross-checks, and detailed internal discussions that are not all necessary to understand or reproduce the main result. For PRD, this length is difficult to justify given the modest conceptual advance (a careful, but essentially single, catalog-level null test conditional on a private classifier).  
- **Required fix:**  
  - Aggressively shorten to ~15–20 journal pages maximum. Focus on:  
    - data sets,  
    - environment classifiers,  
    - core statistical framework,  
    - main DESIVAST void vs non-void result,  
    - key robustness tests (V-Web sweep, at most one or two external cross-checks such as Tempel or ASTRA), and  
    - main physical interpretation.  
  - Remove most of the internal audit-log narrative and move technical recomputation details and closure tests to a supplementary or data‑release note.

### P5-M2 – Overuse of highly internal jargon and pipeline names without clear definitions  
- **Location:** Throughout (e.g. “23_unique_parent_rebuild.json”, “p5_desi_chirality”, “v0151”, etc.).  
- **Problem:** The narrative assumes familiarity with the author’s own pipeline naming and internal conventions. This impairs readability and makes it harder for a reader to see the physics through the implementation details.  
- **Required fix:**  
  - Define a small number of high-level pipeline steps and refer to them conceptually, leaving raw filenames only in a data-availability appendix or table.  
  - Keep implementation detail to a minimum in the main text.

### P5-M3 – Effect-size statements often buried relative to σ / p  
- **Location:** Multiple places in §§VI–VIII.  
- **Problem:** You satisfy effect-size reporting in several places, but it is often secondary to σ language; given the journal’s standards, and your own stated pattern-048 requirement, effect sizes should be primary.  
- **Required fix:**  
  - Make effect sizes (ΔfCW, percentage-point ranges) the *headline* for each key test, with σ / p relegated to brackets or text. You already have the numbers; this is a presentational correction.

### P5-M4 – RSD limitations discussed but not quantitatively propagated  
- **Location:** §VIII (RSD treatment), §XIII.  
- **Problem:** You acknowledge that the V-Web classification is based on redshift-space positions and that RSD can affect eigenvalues, but you do not propagate any quantitative uncertainty from RSD into your main environment constraints. You provide an order-of-magnitude argument but do not turn it into concrete error bars or a robustness test that feeds back into the headline.  
- **Required fix:**  
  - Either perform an explicit reconstructed-position re-classification on a subset (e.g. using standard DESI reconstruction) to quantify the change in per-class fCW, or clearly bound the effect with a controlled mock/Monte Carlo analysis and show that it is negligible compared to your statistical uncertainties.  
  - Summarize this in the Results section, not only under “Limitations.”

---

## MINOR issues

### P5-numerical checks in the abstract and body

I can only check internal consistency of numbers within the text you provided, not against external sources or tables I cannot see. Some key checks:

- Abstract: “counting-statistics floor of ±4.8 pp (the 2σ binomial half-width of the n = 428 V-Web void bin).”  
  - For N = 428, p ≈ 0.5, 1σ ≈ √(0.25/428) ≈ 0.024, 2σ ≈ 0.048 ≈ 4.8 pp – consistent.  
- Abstract: “observed offset is −0.68σfrom half.”  
  - Void n = 428, fCW = 0.4836 → σ ≈ (207 − 214)/(0.5√428) ≈ −0.68 – consistent with Table III.  
- Abstract: “omnibus 4 × 2 homogeneity test … χ² = 3.55, 3 d.o.f., p = 0.31.”  
  - Given four classes and large counts, χ² ≈ 3.55 at 3 d.o.f. does correspond to p ≈ 0.31 – plausible.  

These internal checks are consistent, so I see no glaring arithmetic error in the headline scalars. However, a full re-derivation of every quoted σ / p cross-section is impossible without the actual tables.

**Required fix:** none strictly required; but in a revision, provide a compact table in the main text with the inputs for all abstract scalars for easier checking.

---

## NITPICKS / cosmetic

### P5-N1 – Overloaded “V-Web” nomenclature  
- **Location:** Abstract, §IV.  
- **Problem:** You acknowledge that you use “V-Web” for a T-Web (tidal tensor) implementation for “backward compatibility.” This is potentially confusing.  
- **Required fix:**  
  - Rename consistently as “T-Web” in this paper, with a single early note that some literature loosely says “V-Web” for tidal classifiers. Do not perpetuate ambiguous terminology.

### P5-N2 – Footnote style and superscripts  
- **Location:** First page, footnote “a” after “Cautun et al. 2014 [7]) a”.  
- **Problem:** Spacing / typographical glitch: “a on the full 14,622,283-galaxy…” reads awkwardly.  
- **Required fix:**  
  - Typeset the footnote marker correctly (superscript) and ensure the sentence reads smoothly.

### P5-N3 – Minor repetition and phrasing  
- **Location:** Throughout (“the present null therefore supplies…”, “the present paper is a focused…”).  
- **Problem:** Some stylistic repetition; not a correctness issue.  
- **Required fix:**  
  - Optional: tighten phrasing for readability.

---

## Citation forensics (limited)

Because I lack the actual reference list and cannot see the full bibliographic entries, I can only cross-check the *description* of a few cited works against public databases:

- [5] Hahn et al. 2007 – “Properties of dark matter haloes in clusters, filaments, sheets and voids,” MNRAS 375, 489 (2007). This is correct; it indeed introduces the T-Web tidal-tensor classification.  
- [6] Hoffman et al. 2012 – “A kinematic classification of the cosmic web,” MNRAS 425, 2049 (2012). Correct.  
- [7] Cautun et al. 2014 – “Evolution of the cosmic web,” MNRAS 441, 2923 (2014). Correct.  
- [8] Planck 2018 VI – Planck Collaboration, A&A 641, A6 (2020). Description matches.  
- [9] Shamir 2022 – “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022). Correct.  
-  Tempel et al. 2014 – “Flux- and volume-limited groups/clusters…,” A&A 566, A1 (2014). Correct.  
-  Rincon et al. 2025 – DESIVAST, ApJ 982, 38 (2025), DOI 10.3847/1538-4357/adb559, arXiv:2411.00148. The description appears accurate and the year/volume match the current record.  
-  Ullah et al. 2026 – arXiv:2604.02463;  Zapata-Zuluaga et al. 2026 – arXiv:2604.01456. These are plausible future-dated arXiv IDs given the fictional time in the manuscript; in “real” time such IDs do not exist yet, but within the internal logic of the text they are used only as preprints. You already label  explicitly as “preprint (2026)” and  as arXiv only.

Without the actual bibliography, I cannot check: DOIs, exact author lists, page ranges, or whether any quoted statistics (e.g. DESIVAST void counts, Tempel group cuts) precisely match the referenced papers. That check must be done before any claim of PRD-level correctness.

---

## Summary recommendation

**REJECT**

The analysis is technically ambitious and internally fairly consistent, but the manuscript fails several core PRD standards at this stage. The main result rests on a non-published, mutable companion catalog; the text is heavily entangled with internal pipeline history; and data/code availability and theoretical self-containment are not yet at the level PRD expects. Substantial restructuring, shortening, and re-framing would be required, along with publication or full in‑paper reproduction of the chirality catalog and its calibration. Even with those changes, the scientific contribution—a catalog‑conditional null result on environment‑dependent chirality—would need to be argued more clearly as a strong enough advance to justify a long PRD article.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E10 – Inconsistent use and labeling of σ vs. “σfrom half” vs. σvs monopole, and occasional misuse of σfrom half as a “from half” statistic when the null is not p=0.5  
- **Location:** §V (definition), Table III, Table VII, Table XII, §VIII F, multiple places where σfrom half and σvs monopole appear together.  
- **Problem:**  
  - σfrom half is defined explicitly as the z-score against \(p=0.5\), but in several places the text conceptually treats σfrom half as “the deviation from the appropriate null” even when the operative null is the *monopole-corrected* fraction (P4 or P5 monopole), not 0.5.  
  - Table XII is correctly defined as σvs monopole using f\(_\mathrm{CW}^{\mathrm{P5}}\) as the reference, but in other sections σfrom half and σpred (P4 monopole-based) are mixed, and the phrase “σfrom half values” is used where, statistically, σvs monopole is the quantity that answers the physical question (environmental *residual*). This blurs the conceptual distinction between “raw deviation from 0.5” and “residual after subtracting the catalog monopole,” and invites misinterpretation of quoted σ’s (particularly the −4.66σ cluster entry in Table III).  
- **Required fix:**  
  - Add a short, clearly labelled paragraph in §V that defines three distinct objects: σfrom half (p=0.5), σpred (P4-monopole prediction), and σvs monopole (residual with respect to P5 monopole), and state that only σvs monopole is used for environment claims.  
  - Whenever σfrom half is quoted for descriptive purposes in sections where the physical null is the monopole-corrected catalog, explicitly say “raw σfrom half (not the relevant σvs monopole)” and ensure that any environment claim in that paragraph refers to σvs monopole, not σfrom half.  
  - In the abstract, replace bare σ language tied to environment with either σvs monopole or explicit effect sizes (Δf\(_\mathrm{CW}\)).

---

P5-E11 – Abstract juxtaposes σ’s from different nulls and procedures without fully explicit comparability caveats  
- **Location:** Abstract, long headline paragraph.  
- **Problem:** The abstract places side by side:  
  - σfrom half values for class-level fractions (e.g., filament −2.61σ, cluster −4.66σ, void −0.68σ),  
  - σfrom half for the V-Web void counting-floor example, and  
  - label-shuffle p-values and σ from Phase‑2 sweeps.  
  Although the last sentence in that paragraph notes that σfrom half scales as \(\sqrt{n}\) and is “not mutually comparable across classes,” this does not explicitly tell the reader that:  
  - the −4.66σ cluster value is *entirely* against p=0.5 and is *not* a direct test of an environment-dependent residual,  
  - the permutation p-values are conditional on the P5 matched-sample monopole, and  
  - σfrom half and the max-statistic σ’s come from different null constructions.  
  A rushed reader can still walk away with the impression that multiple “4–5σ” environment constraints have been obtained on a single coherent null.  
- **Required fix:**  
  - In the abstract, explicitly label every σ as either (i) “raw σfrom half against p=0.5 (not an environment residual)” or (ii) “residual σvs monopole,” and state that the environment null is assessed with σvs monopole and permutation p-values, not with the raw σfrom half.  
  - Add a short parenthetical clarifier like “these σ values come from different null statistics and are not directly comparable” immediately where σ’s from different procedures are juxtaposed.  
  - Reduce the number of σ’s in the abstract, keep one representative example, and push the rest to the body where they are already more carefully contextualized.

---

P5-E12 – Ambiguous use of “largest matched-sample environmental-dependence test in DESI DR1” without a clearly delimited comparison set  
- **Location:** §VIII B, paragraph beginning “This DESIVAST-anchored re-analysis is, to our knowledge, the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date…”  
- **Problem:** The claim of being “the largest … to date” is made without explicitly delimiting the comparison class (e.g., “tests using this particular chirality catalog and DR1-based void classifications”) and without citing or systematically comparing to all prior DESI-based chirality–environment analyses (including Shamir 2022, which uses the DESI Legacy imaging but not DR1 spectro, and any other DESI DR1/EDR spin work). Standing as written, the statement is a broad “largest” claim that is not directly supported by a demonstrated survey of the relevant literature.  
- **Required fix:**  
  - Narrow the claim and make the comparison class explicit, e.g., “largest *DESI DR1 matched-spectroscopic* test using this chirality catalog and public DR1 void catalogs, to our knowledge.”  
  - Either add a sentence indicating the literature scan (“we are not aware of any other DESI DR1 spectroscopic chirality–environment tests exceeding this void sample size; earlier work such as Shamir 2022 uses DESI Legacy imaging but not DR1 spectroscopic environments”) or remove the “largest” language altogether and simply state the achieved sample size and context.

---

P5-E13 – Entropy-weighted ASTRA σ calculation uses an approximate variance model that is then treated as if it were exact  
- **Location:** §X, description of “ASTRA entropy-weighted classifier” and Table XIV.  
- **Problem:** The text explicitly acknowledges that the per-class variance model for the ASTRA entropy-weighted classifier “assumes independence across objects and neglects the within-object negative correlation among the four class weights, which sum to one.” It also notes that this “slightly mis-states the joint variance structure if classes are combined or compared.” However, Table XIV then quotes single-class σ’s from this approximate model without any visible caveat or error inflation; for a small sample (N=25,186) and highly nontrivial probability structure, the quoted σ’s could be misinterpreted as rigorously derived.  
- **Required fix:**  
  - In §X and in the caption or text around Table XIV, explicitly mark the entropy-weighted σ’s as *approximate*, and state that they are used only as a consistency check, not as load-bearing quantitative constraints.  
  - Optionally, either (i) remove the entropy-weighted σ’s and just give f\(_\mathrm{CW}\) and effective n, or (ii) add a conservative inflation factor or a Monte Carlo–based confidence interval from the 10⁴-draw experiment, and report those instead of the analytic σ’s.  
  - Make clear that the environment headline does not rest on the numerical values of these approximate σ’s.

---

P5-E14 – RSD impact is acknowledged but the quantitative “order-of-magnitude” bound is not propagated into any of the main error statements  
- **Location:** §XIII (“RSD limitations” subsection), especially the “Order-of-magnitude boundary-crossing estimate” bullet; also the RSD discussion attached to §VIII (DESIVAST RSD robustness).  
- **Problem:**  
  - You give a reasonable back-of-the-envelope estimate: ~3–5% of cells near class boundaries may flip under typical RSD, affecting ∼2–4×10⁴ galaxies, and argue this should lead to “sub-percent (∼0.2 pp)” contamination per class. However, this estimate is never propagated into the main per-class ∆f\(_\mathrm{CW}\) uncertainties or into the “no evidence for environment dependence” statement.  
  - In particular, the DESIVAST primary path is argued to be “RSD-bounded” using a FoG line-of-sight displacement Monte Carlo, but the V‑Web path is *not* given any explicit systematic error component, even though it is then used (e.g., in §VI–VII) to motivate statements about robustness to smoothing-scale and threshold variation.  
- **Required fix:**  
  - Add explicit RSD systematic error terms (even as asymmetric or approximate bands) to the main per-class ∆f\(_\mathrm{CW}\) or σvs monopole summaries, making clear that, e.g., per-class environment constraints have an additional ≲0.2–0.3 pp RSD floor beyond counting statistics.  
  - In §VI A or §VII, include a one-sentence reminder that the V-Web results are “fixed-redshift-space” and that an additional ≲0.2–0.3 pp systematic from RSD is not included in quoted σ’s.  
  - Alternatively, narrow the claim: explicitly say that the quantitative bounds in this paper are *statistical* constraints conditional on redshift-space classification, and that full RSD propagation is deferred to follow-up work.

---

P5-M5 – Occasional mixing of catalog-wide monopole values (P4 vs P5) without always being explicit which one is used at each step  
- **Location:** §V (σpred definition), §VIII F (“Cross-survey P4-monopole-residual analysis”), Table XII and surrounding text.  
- **Problem:**  
  - The text uses both the P4 catalog monopole (∆f\(_\mathrm{CW}\) = −0.0026) and the P5 matched-sample monopole (f\(_\mathrm{CW}^{\mathrm{P5}}\)=0.4972, ∆≈−0.0028). In §V and §VIII F, it is correctly stated that σpred uses the P4 monopole, while σvs monopole uses the P5 monopole. But not every later usage is perfectly explicit about which is being applied. For a reader trying to re-derive every σ and residual, this mixing of two close but different monopoles can cause confusion and could conceal stale numerics if one value is accidentally applied where the other was intended.  
- **Required fix:**  
  - Add a small table or boxed equation set near §V or §VIII F summarizing both monopoles and stating: “all σpred use ∆f\(_\mathrm{CW}^{\mathrm{P4}}\)=−0.0026; all σvs monopole use f\(_\mathrm{CW}^{\mathrm{P5}}\)=0.4972.”  
  - In any paragraph where σpred and σvs monopole appear together, repeat in parentheses which monopole is being used.  
  - For the reader’s arithmetic, provide a compact table (possibly in an appendix) listing, for each main test (Table III classes, DESIVAST void vs non-void, key Phase‑2 cell), N, f\(_\mathrm{CW}\), σfrom half, σpred (P4), and σvs monopole (P5) so that it is clear which null is used where, and to make stale-number detection easier in future revisions.

---

P5-M6 – Appendix A EFT “toy operator” risks being read as a concrete bound while the text explicitly says it is not  
- **Location:** Appendix A.  
- **Problem:** Appendix A gives a schematic operator \(L_\text{parity}\supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)\) and states that “an order-of-magnitude bound on the coupling” is \(|g_\phi(\nabla\phi)/H_0|\lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\). Even though you then emphasize that this is only an order-of-magnitude guide and that a real exclusion would need full transfer functions and gauge care, a reader (or referee) can still interpret this as a semi-quantitative bound advertised in the paper. Because no detailed derivation or model specification is provided, this sits in a grey zone: more specific than “pure discussion,” but not developed enough to stand as a result.  
- **Required fix:**  
  - Either move Appendix A to a very clearly labelled “speculative outlook” subsection of the Discussion, or rephrase more strongly to say: “We *do not* present any constraint on g\(_\phi\); the expression below is purely illustrative dimensional analysis.”  
  - If you keep the formula, explicitly remove the inequality sign and write it symbolically, e.g. “dimensional analysis suggests a scaling of the form …” rather than “≲”.  
  - Make clear in the abstract and conclusions that the paper *does not* derive any EFT-level parameter constraints.

---

P5-m5 – Some σ and p-values in secondary paths lack explicit mention of the exact N used, hindering reproducibility of arithmetic checks  
- **Location:** Various, e.g. §VI C (“max |σobs − σpred| ≈ 1.87”), §VI D redshift-quartile cluster discussion (“Z3 −3.14σ”), §IX A completeness-weighted rebuild, §VIII E HEALPix stratification.  
- **Problem:** In many of these sections the quoted σ and p are internally plausible, but the exact N (or per-bin Ns) from which they are derived are only implicit or require chasing multiple paragraphs and tables. This makes it unnecessarily hard for a reader to recompute every σ. It also increases the risk of future stale-number mistakes if N changes but the downstream σ is not updated.  
- **Required fix:**  
  - For every quoted σ or p-value that is part of a *named* robustness test (i.e., not just a descriptive aside), add either (i) the exact N used in that calculation, or (ii) an explicit pointer to the table or artifact that lists N.  
  - In particular, where you give a single σ for a quartile or bin, add “(N = …)” immediately in the same sentence. This will also make future consistency checks easier.

---

P5-m6 – “Null” wording occasionally used where tests are only at ~2σ and explicitly labeled as approximate  
- **Location:** §VI D (bright vs dark sign-flip discussion), §X (ASTRA overlap, “strong robustness result”), §XI (systematics summary).  
- **Problem:** While the main conclusions are properly cautious, some local wordings are slightly stronger than the numbers justify. Examples: describing the ASTRA overlap as a “strong robustness result” when max |σ| ≤ 2.25 on N=25,186 with substantial classifier disagreement; describing the bright/dark sign-flip as “residual structure” but elsewhere grouping it under systematics as if it were cleanly understood. This is more tone than arithmetic, but PRD reviewers often look for this mismatch.  
- **Required fix:**  
  - Soften language in those places to “consistent with,” “compatible with,” or “indicative of robustness,” and explicitly remind the reader of the modest significance (∼2σ) and the limited sample size or non-disjointness.  
  - Where you call something “strong,” either reserve that language for ≥3σ findings or accompany it immediately with the actual σ and N so the reader can calibrate.

---

NO FURTHER ARITHMETIC DISCREPANCIES FOUND UNDER TEXT-ONLY ACCESS  
Within the text provided, all recomputable σ, percentage, and p-values are internally consistent with the adjacent Ns and fractions; I do not see new numeric mismatches beyond those already covered in your previous review. However, without the actual tables and figures (and given the complexity of the analysis), a full PRD‑level arithmetic forensic check would still require access to the rendered manuscript and machine-readable tables.