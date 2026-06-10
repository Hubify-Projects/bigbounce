# P4 2026-06-04_1920pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.8s

---

P4-B1 (ESSENTIAL)  
Section: Abstract & throughout (e.g. first page, “Falsification criterion”)  
Problem: σ from different null procedures is treated as if on a common scale, and at several points σ values from distinct nulls are compared or combined without always making the null dependence explicit in the prose. Example: “canonical-mask direct-MC residual is +3.64σ… The three discriminators that disfavor interpretation (i) are: (a) ℓ = 2 > ℓ = 1 broadband structure (auto-spectrum +4.73σ at ℓ = 2 vs +3.63σ at ℓ = 1…) … bootstrap pixel-resample test gives −0.22σ… These tests do not exclude a small primordial dipole component…”. Here 3.64σ (binomial per‑pixel shuffle), 4.73σ (a different MC on a different bandpower) and −0.22σ (bootstrap) are all quoted as “σ” without always re-stating that they are not comparable in scale.  
Required fix: Go through all occurrences of σ and add explicit qualifiers in the text (not just in scattered footnotes) stating which null procedure and data vector they refer to (per-pixel shuffle, label shuffle, bootstrap, monopole-only generative null, etc.). Anywhere you compare magnitudes (e.g. “ℓ = 2 > ℓ = 1”, “+3.64σ canonical vs −0.12σ subsample mask”) make clear this is a qualitative comparison under different nulls and that σ magnitudes cannot be directly compared. Add a single table near Section IV explicitly mapping each σ to its null and state clearly that σ’s from different rows should not be compared quantitatively.

P4-B2 (ESSENTIAL)  
Section: Abstract, “Falsification criterion”  
Problem: The falsification condition is expressed partly in terms of the empirical 0.75% 50%-recovery threshold (“≳0.75% (the demonstrated 50%-recovery-at-3σ threshold…)”) but there is residual language inherited from earlier versions where 0.29–0.4% statistical floors were being used as if they were effective sensitivity. That entire paragraph is very dense and mixes the empirical threshold, Fisher limit and LSST projections in a way that can mislead readers into thinking 0.29% is achieved systematics-inclusive.  
Required fix: Rewrite the falsification criterion paragraph to:  
– State *only* the empirical demonstrated threshold (0.75% full amplitude, 50% recovery at 3σ under the adopted per–pixel-shuffle null on the specified HC pipeline) as the operative number for this paper.  
– Move the Fisher ~0.29% discussion and LSST projections out of the abstract to the Discussion, clearly labeled as theoretical/statistical limits, not achieved performance.  
– Remove any phrasing that could be read as a hard falsification threshold at 0.1–0.5% unless it has an explicit empirical demonstration.

P4-B3 (MAJOR)  
Section: References (Shamir citations)  
Problem: Two Shamir entries are fused/mis-labeled. You cite “[2] Shamir (2022) … PASJ 74 1114” for “Analysis of the alignment of non‑random patterns of spin directions…”, but PASJ 74, 1114 (2022) is “Analysis of the alignment of non‑random patterns of spin directions in populations of spiral galaxies”, not the generic methodology paper you intend, and your description “reports analysis of ∼1.3×10^6 DESI Legacy galaxies” is actually from MNRAS 516, 2281 (the DESI Legacy paper) which you separately list as [3]. The bracket mapping is confusing: [2] is described as methodology, but the journal line attached to [2] is PASJ; [3] is the DESI DESI paper.  
Required fix:  
– Split the Shamir references unambiguously:  
  • One entry for the PASJ 74 1114 spiral‑alignment paper, with correct title, volume, page, year.  
  • One entry for MNRAS 516, 2281 DESI Legacy paper, with correct title and arXiv:2208.13866.  
– Ensure that when you discuss “nearly 1.3×10^6 spiral galaxies in DESI Legacy” the citation points only to the MNRAS DESI paper, not to a fused [2]/[3].  
– Check that the DOIs line up with the journal/volume you cite (e.g. PASJ vs MNRAS).  

P4-B4 (MAJOR)  
Section: I. Introduction, discussion of Shamir 2012 / 2020 / 2022  
Problem: You compress Shamir’s claimed asymmetry amplitudes into “2–4%” and “∼3%” without clearly attributing exact numbers to a specific paper/table or pointing to where those amplitudes are given. You also say “Shamir’s earlier work [1] reported ~3% asymmetries with a consistent dipole axis; Shamir (2022)[3] reported DESI Legacy Survey results in the same magnitude regime”, but you do not quote any specific table/statistic from these papers. As a methods paper doing “citation forensics”, these claims should be traceable.  
Required fix: For each of the three Shamir works you discuss, identify one concrete quoted statistic (e.g. asymmetry amplitude and σ) and reference the specific table/section in the source; if the number 2–4% is an envelope over multiple subsamples, say so explicitly and reference precisely which samples. Replace generic wordings (“∼2–4%”, “∼3%”) with something like “Shamir (2012, Table X) reports A=Y1±...; Shamir (2020, Section Y) reports A=Y2…, etc.” or clearly state that you are summarizing ranges across multiple tables.

P4-B5 (MAJOR)  
Section: II.B (Training Labels) and CE‑ResNet description  
Problem: You describe the CE‑ResNet catalog as “∼1.95 million spiral classifications” and “cw/ccw=0.998, consistent with parity” based on Jia et al. (2023) without quoting a specific line/table. The 0.998 ratio and sample size should be verified against Jia’s abstract or tables.  
Required fix:  
– Verify directly from Jia et al. whether the catalog size is indeed 1,953,246 labeled galaxies and whether the cw/ccw ratio 0.998 is correct; then state the exact values and where they appear (e.g. “Table 1 of ”).  
– If 0.998 is from your own re-count of their released table rather than their paper, explicitly say so.

P4-B6 (MINOR)  
Section: V.C (SpArcFiRe)  
Problem: You state that SpArcFiRe has “∼140,000 galaxies” and “a DR9 overlap catalog” with CW/CCW consistent with 50/50 to within ~0.3%, but you do not give a reference to a specific SpArcFiRe catalog release or table. The reader cannot trace the 0.3% figure.  
Required fix: Add a precise citation to the SpArcFiRe release (e.g. Davis & Hayes 2014 plus the DR9 overlap catalog; name and year) and clarify whether the 0.3% is from the published paper or from your own count of their released table.

P4-B7 (MINOR)  
Section: References [5] Iye et al. 2021, [6] Tadaki 2020  
Problem: You summarize Iye and Tadaki as “null” results and quote sample sizes (~80,000, etc.), but again without specific table references. For example, you say Tadaki “studied a smaller sample with HSC‑SSP… found null results”; this should map to a known sample size and statistic.  
Required fix: For Iye et al. and Tadaki et al., add one sentence each referencing the exact place in the paper where (i) sample size, and (ii) “null result” are reported (e.g. “see Table 1 of [5] for N=…”; “see Fig. 5 of [6], where the asymmetry is consistent with zero”).

P4-B8 (MINOR)  
Section: V.D (Motloch & Pen 2021)  
Problem: You quote a “∼2.7σ correlation” but don’t reference a specific figure/result in Motloch & Pen.  
Required fix: Cite the exact section or figure where the 2.7σ correlation is reported (they may express it as a p‑value or as a sigma for a specific template). Ensure that the 2.7σ is indeed the number they quote, not an inference.

P4-B9 (NIT)  
Section: Multiple locations (e.g. I. Introduction, “Shamir’s earlier work [1] reported ~3% asymmetries…” and several later appearances)  
Problem: Some Shamir references use arXiv IDs only (“arXiv:2007.16116”) and some use journal references; in at least one place you say “Shamir (2020) [1] (arXiv:2007.16116, SDSS DR8 + Pan-STARRS…” but in References [1] you already refer to that arXiv as an Astrophys. Space Sci. 365, 136 paper. The text mixes preprint and journal forms inconsistently.  
Required fix: Choose a single canonical form (journal if published; arXiv only if not yet published) for each Shamir paper and use it consistently in the main text; ensure arXiv identifiers match the final published version’s content.

P4-B10 (NIT)  
Section: References [7] Iye, Yagi & Fukumoto 2026  
Problem: You cite Iye:2026 as arXiv:2605.05570 and say “we do not rely on its quantitative result for any headline statistic”. That is fine, but all mention of 2605.05570 should be checked: at this point only the arXiv preprint exists and no journal is given.  
Required fix: Make sure the title, authors and year for arXiv:2605.05570 match exactly what appears on arXiv. If a journal appears before PRD submission, update the reference accordingly.

P4-B11 (NIT)  
Section: VI.G (transfer‑function caveats) and parity‑violation references  
Problem: You mention Lue, Wang & Kamionkowski, Cabass–Ivanov–Philcox, Philcox (BOSS 4PCF), Hou–Slepian–Cahn, Eskilt & Komatsu etc. with correct qualitative descriptions, but there are no explicit arXiv IDs for some of them in the narrative (only in the reference list). For a methods paper emphasizing “citation forensics”, it would help to tie those directly.  
Required fix: Consider adding explicit arXiv IDs for [17–23] inline the first time each paper is discussed so that readers can quickly locate the precise works you are paraphrasing.

P4-B12 (NIT)  
Section: Data availability (DESI DR8, Galaxy Zoo DESI, Smith42/galaxies)  
Problem: For DESI DR8 and Galaxy Zoo DESI, you give journal citations ,  but for “Smith42/galaxies” on HuggingFace you only give the URL in a footnote and label it “Smith42/galaxies dataset hosted on HuggingFace2”. It is not a conventional journal citation, but you *do* use it as a primary data source.  
Required fix: Explicitly state in the main text that “Smith42/galaxies” is a user-contributed HuggingFace dataset, not an official DESI product, and that you have verified that its DR8 cutouts and metadata are consistent with the official Legacy imaging (e.g. by spot checks on positions and Tractor IDs). That clarifies provenance.

P4-B13 (NIT)  
Section: References  DESI white paper  
Problem: You cite the DESI white paper as “DESI Collaboration, Aghamousa et al. (2016), arXiv:1611.00036; white‑paper only, no journal”. That is accurate, but you then loosely refer to “DESI DR1+ spectra” in the Discussion. DESI DR1 is a later public release with its own documentation, not covered by 1611.00036.  
Required fix: Either (a) add a reference for DESI DR1 if you explicitly refer to DR1, or (b) change wording to “DESI spectroscopic survey” and keep the white paper as the only DESI-theory reference.

P4-L1 (MAJOR — length / scope)  
Section: Whole paper  
Problem: The manuscript is 56 pages and reads as a hybrid of catalog description, method development, internal reproducibility log, and systematic-audit narrative. For a PRD “methods/catalog” paper, this is significantly longer than the typical 15–30 pages and many of the internal audit-path details (e.g. long accounts of GPU throughput, pathnames, seeds, and JSON filenames) are not necessary for the core scientific content.  
Required fix: Compress the main text to ≲ 35 pages by:  
– Moving much of the “reproducibility artifact” detail (file paths, JSON names, seeds, GPU specs) into a supplementary material or an online repository README.  
– Collapsing subsections like III.E, III.F, VI.D into shorter summaries with references to a supplementary note for full confusion matrices and hold‑out experiments.  
– Focusing the main text on (i) catalog construction, (ii) bias-hardening tests *at a summary level*, and (iii) cosmological null results.  

P4-L2 (NIT — version artifacts)  
Section: Title page, footnotes, and throughout  
Problem: Numerous internal-version artifacts remain, e.g. “HUBIFY-2026-004”, “v1.0.152”, “smoke snapshot”, “earlier-snapshot value 2.75σ”, “on the pod”, “post-arXiv TODO list”, “external peer review”, and named JSON filenames. These are internal or version-history notes, not appropriate for a PRD final manuscript.  
Required fix: Remove all references to internal version IDs, earlier snapshots, “smoke” runs, pods, and TODOs from the main text. If previous runs are methodologically important (e.g. to say that a prior error was corrected), summarize that in one neutral sentence without referring to file names or “smoke” runs.

P4-L3 (NIT — duplicate / awkward phrasing)  
Section: Various, e.g. Abstract and Sec. IV.D  
Problem: Some phrases are duplicated or awkward: e.g. “canonical-mask residual is interpretation (ii) systematic, not a primordial detection” followed by multiple paraphrases of the same point; “these tests do not exclude a small primordial dipole component sitting beneath the canonical-mask systematic; what they exclude is a clean dipole-only explanation…” appears in very similar form multiple times.  
Required fix: Pass through the text to remove duplicate clauses and compress repeated explanations of the canonical-mask systematic vs subsample-mask null; keep a single clean explanation in Sec. IV.D/VI.G and refer back to it as needed.

P4-L4 (NIT — σ‑convention paragraph)  
Section: IV. Results, opening paragraphs  
Problem: You added a σ‑convention paragraph but it is buried and still a bit opaque for readers unfamiliar with multiple-null analyses.  
Required fix: Move or duplicate a short version of the σ‑convention at the start of Section IV: one sentence saying “All σ values are defined relative to the specific null indicated in Table II; σ from different rows are not directly comparable and should be interpreted only via their own p‑values.” That will prevent misinterpretation.

P4-C1 (MINOR — abstract accuracy)  
Section: Abstract  
Problem: The abstract states: “Our null dipole at sub‑percent sensitivity… does not depend on any companion work” and “The ℓ=1 subsample‑mask null is the load‑bearing scientific result; the canonical‑mask residual is interpretation (ii) systematic, not a primordial detection.” That correctly describes what is *claimed*, but it does not state that the practical empirical sensitivity is ≳0.75% (not “any sub‑percent” level) and that the canonical-mask systematic is not fully modeled.  
Required fix: Adjust the abstract wording to something like “sub‑percent *statistical* sensitivity, with an empirically demonstrated ≥0.75% 50%-recovery‑at‑3σ floor” and explicitly say “we interpret the canonical-mask residual as likely systematic based on a suite of null tests, but do not provide a full physical template model of that systematic.”

P4-C2 (NIT — edge-on fraction)  
Section: VI.D Edge-on galaxy contamination  
Problem: Two different numbers appear in different places for “edge-on contamination”: 65.7% and later 59.4% after a refinement. The text explains the change, but this is confusing.  
Required fix: Settle on a single, final edge-on spiral fraction (59.4% as per the DR8 sweep join) and move the earlier 65.7% to a brief footnote “an earlier visual-ID estimate of 65.7% was superseded by the catalog cross-match; we use 59.4% hereafter”.

P4-C3 (NIT — McNemar Z)  
Section: III.G (Catalog B Platt calibration paragraph, long McNemar discussion)  
Problem: You compute McNemar’s statistic as Z≈13.4σ on b and c. That’s formally correct for large N, but in context it reads like a “13σ” scientific discrepancy, which you then immediately downplay.  
Required fix: Clarify that this is a *paired classification disagreement* significance given very large N (∼10^5), and that even small percentage-level differences become extremely significant by that metric. Suggest rephrasing as “statistically highly significant but numerically small (2.1 percentage-point) disagreement” rather than emphasizing the σ.

P4-C4 (NIT — σ parity-even/odd explanation)  
Section: VI.G (symmetry classification)  
Problem: The explanation that ℓ=1 for a pseudoscalar field is parity-even (axial) is correct but dense, and readers might misread “parity‑EVEN” to mean “has nothing to do with parity tests”.  
Required fix: Add one clarifying sentence: “In this sense our null ℓ=1 constraint is a test of isotropy (preferred axis) in a parity-odd scalar field, not a direct test of microscopic parity violation like CMB birefringence.”

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper presents a technically serious catalog and a careful multi-null analysis, but it is too long and dense for PRD in its current form and still has several citation‑forensics issues and σ‑interpretation pitfalls that must be cleaned up. With the references tidied, the σ‑conventions made unambiguous, the abstract/falsification criterion aligned with the demonstrated empirical sensitivity, and the length reduced to a more focused 30–35 pages, it would be suitable for reconsideration.