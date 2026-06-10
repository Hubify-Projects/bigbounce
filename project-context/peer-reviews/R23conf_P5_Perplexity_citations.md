# P5 R23conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.52.pdf` md5=cc7c3390 pages=24
**Input format**: TEXT + web search + pass-2 self-critique (11956 chars)
**Wall time**: 85.9s

---

P5-E1 (ESSENTIAL) – Use of non-archival “in preparation” companion papers as load‑bearing sources  
- **Location:** Abstract (lines 1–4) and §I–II, multiple occurrences; References [3], [4].  
- **Problem:** Paper IV [3] and Paper II [4] are cited as “companion work, not yet peer-reviewed / in preparation” but are used as *load‑bearing* inputs: the global monopole value \(\Delta f_{\rm CW}=-0.0026\), catalog construction, and the template for monopole subtraction all rely on an unpublished, uncontrolled dataset and analysis. The abstract explicitly treats the Paper IV monopole as defining the “sensitivity floor,” and much of the interpretation (e.g. Table X, σ_pred, the monopole-subtracted residuals) assumes the correctness and stability of Paper IV’s catalog. This violates PRD standards for reproducibility and independent verifiability.  
- **Required fix:** Either (a) submit the Paper IV catalog and monopole analysis as an accompanying PRD paper (or ensure it is accepted in a comparably rigorous journal) and treat the present work as explicitly conditional on that accepted result, or (b) re‑cast this manuscript so that *all* load‑bearing inferences (monopole size, monopole subtraction, σ_pred, Table X, etc.) are derived within this paper from fully specified, reproducible methods and publicly archived data/weights, with all necessary code and numerical products provided in a stable, citable form. Until Paper IV is published and stable, statements that depend on its internal auditing (e.g. removal of an earlier MASTER-based dipole, classifier systematics characterization) must be downgraded to clearly labeled assumptions rather than treated as established results.

---

P5-E2 (ESSENTIAL) – Mixed σ values from different null procedures not consistently flagged as non-comparable  
- **Location:** Abstract (first paragraph, “quoted σ… not mutually comparable”), §V (definition of σ_from_half and σ_pred), Table II and following text, §§VI–VIII, X–XII.  
- **Problem:** The paper repeatedly places different σ-like measures side by side without always explicitly reiterating that they are not directly comparable, in particular:  
  * **Binomial σ_from_half** (based on simple binomial counting)  
  * **σ_pred** from the Paper IV monopole model (Eq. (1))  
  * **Permutation-based “σ” / max‑stat distributions** (MC-based)  
  * **z-scores from logistic or two-sample tests**  
  While the abstract does contain a caveat (“The quoted σ … are therefore not mutually comparable across classes of different n.”), this is easy to miss, and later sections juxtapose raw σ_from_half, σ_vs_monopole, and permutation‑derived significance levels as if they were interchangeable. For example, §VI.A discusses raw σ and then compares them to σ_pred; §VI.D mixes “|σ|max”, “|σ_obs−σ_pred|”, and Bonferroni σ thresholds; §VII uses σ values and p_LEE without always reminding the reader of the differing nulls. PRD’s statistical rigor requirements (and the user instruction) demand explicit warnings at each such juxtaposition.  
- **Required fix:** For every place where σ values from *different* null procedures or formulas are compared or plotted on the same footing (text, figures, tables), explicitly label the type of σ and insert a short explicit statement that these σ’s are not directly comparable. E.g., “Here σ_from_half (binomial) and σ_vs_monopole (model residual) are shown side-by-side; they are not directly comparable because they arise from different nulls.” Amend figure captions (e.g. Figs. 3, 5, 6, 7, 8, 9) and table notes (Tables II, III, IV, VI, VIII, X, XII, XIII) accordingly, and standardize notation to minimize confusion (for example, use distinct symbols such as \(z_{\rm bin}\), \(z_{\rm mono}\), and \(z_{\rm perm}\).

---

P5-E3 (ESSENTIAL) – Companion Paper II ([4]) is pure placeholder with no accessible content  
- **Location:** §XII.B, Appendix A, References [2], [4].  
- **Problem:** Paper II [4] is cited as “in preparation; manuscript in preparation” and described as providing independent discriminators via primordial \(f_{\rm NL}\) and multi-survey anomalies, but no arXiv ID, DOI, or journal is given, and no results from it are actually used quantitatively here. Yet §XII.B invokes it as part of a “discrimination program,” which can mislead readers into believing a set of constraints exists in the literature. This amounts to referencing non-existent, unverifiable results.  
- **Required fix:** Remove Paper II [4] entirely from the main text and reference list unless there is an actual posted preprint (with arXiv ID) or published paper to cite. If a preprint exists, replace “in preparation” by the correct arXiv identifier, title, authors, and venue, and sharply limit the discussion to what is explicitly contained in that work.

---

P5-E4 (ESSENTIAL) – EFT “toy operator” not clearly segregated as speculation  
- **Location:** Appendix A (“Toy EFT mapping of the environmental bound”), §XII.B references to “bounce-chirality coupling class.”  
- **Problem:** The toy operator \( \mathcal{L}_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L\cdot \hat z)\) is introduced with a brief caveat but then used to quote an order‑of‑magnitude constraint \(|g_\phi \nabla \phi/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\). This construct is neither drawn from the cited literature [1,2] nor justified by a concrete model; it is explicitly acknowledged as non-gauge-invariant and coordinate dependent. As written, this risks being mistaken for a physically meaningful constraint derived from first principles, whereas it is closer to qualitative speculation. PRD expects speculative EFT structures to be either carefully derived or clearly quarantined as heuristic.  
- **Required fix:** Strengthen the language to make clear this is *purely illustrative* and not a derived bound:  
  * Explicitly label the operator and the bound as an “illustrative parametrization, not a consistent EFT nor a quantitative constraint.”  
  * Move the bound expression and discussion entirely to a clearly marked speculative appendix section, and remove any language in §XII implying that the paper has obtained a constraint on actual couplings.  
  * Alternatively, remove Appendix A entirely; the main scientific content of the paper does not depend on it.

---

P5-E5 (ESSENTIAL) – Internal repository and version tags as part of the “data availability” statement  
- **Location:** Appendix B (“Data and code availability”), “REPRODUCIBILITY CHECKLIST,” repeated references throughout to “pipelines/p5_desi_chirality/...”, “bigbounce” GitHub.  
- **Problem:** The paper relies on a personal GitHub repository (“Hubify-Projects/bigbounce”) and internal directory structure paths as the primary reproducibility mechanism. These are:  
  * Non-archival (no guaranteed long-term persistence, not under journal curation).  
  * Not formally cited (no DOI in the references section).  
  * Incompatible with PRD’s expectation that key numerical products be reproducible without dependence on mutable personal infrastructure.  
  Additionally, there is no explicit versioned archive (e.g. Zenodo DOI) cited in the reference list, only a promise that “a DOI‑minted archival snapshot … accompanies submission” without a persistent identifier.  
- **Required fix:**  
  * Upload all analysis code and essential derived data products (e.g. the matched catalog, environment-label tables, Phase‑2 sweep summary tables) to a proper archival repository (Zenodo or similar), obtain a DOI, and cite this in the references with full metadata.  
  * Replace bare GitHub path references in the text with a concise description plus a citation to the archival DOI.  
  * Ensure that all claims that depend on these materials can be reproduced from that single archived snapshot.

---

P5-M1 (MAJOR) – Use of an unpublished chirality catalog as a black box  
- **Location:** §III.A (“Chirality catalog”), §§I–II, VI–VIII, XI; Reference [3].  
- **Problem:** The chirality catalog from Paper IV is treated as an opaque input: this paper assumes its labels and systematic corrections are valid and final, but does not provide any independent validation against e.g. Galaxy Zoo DESI classifications  or an internal re-analysis that a PRD reader can check. Given that Paper IV itself underwent non-trivial revisions (a harmonic-space statistic was withdrawn, mask provenance corrected), the reliance on this catalog without giving minimal internal quality checks in this paper is problematic.  
- **Required fix:**  
  * Include, in this paper, at least a summary validation of the chirality labels against an independent standard, e.g. a cross-match with Galaxy Zoo DESI , with confusion matrix and misclassification rates.  
  * Explicitly state what version of the chirality catalog (hash, tag) is used, and provide a stable download location (with DOI as per P5-E5).  
  * Clarify that the global monopole value used here is propagated with its uncertainty, and show explicitly how that uncertainty feeds into σ_pred and σ_vs_monopole.

---

P5-M2 (MAJOR) – Excessive length relative to contribution; suggested tightening  
- **Location:** Whole manuscript (24 pages main text plus appendices).  
- **Problem:** The scientific contribution is a carefully executed null test: CW fraction vs environment shows no significant dependence. The manuscript, however, is very long and reads partially like an internal analysis logbook. Multiple sections (e.g. the full “Reproducibility checklist,” detailed directory paths, lengthy methodological asides on RSD, and the speculative EFT appendix) go beyond what PRD typically expects in the main body. This dilutes the core message and makes the paper harder to review and to use.  
- **Required fix:** Tighten the manuscript to focus on: data selection, environment classification, the main statistical tests, and key robustness checks. Move the full path-level reproducibility description, driver file names, and other engineering-like detail to an online supplement. A realistic target for the main text is ≈ 14–16 pages.

---

P5-M3 (MAJOR) – Ambiguous “primary/secondary analysis path” and garden-of-forking-paths  
- **Location:** §V.B (“Primary vs. secondary analysis paths”), §§VI–X.  
- **Problem:** The paper explicitly states that there was no preregistered analysis plan and that the designation of DESIVAST as “primary” and the V-Web/Tempel/ASTRA/T‑Web analyses as “secondary diagnostics” is post hoc. Yet, multiple potentially interesting effects (e.g. bright vs dark sign flip, cluster-class −5σ, V-Web vs DESIVAST void disagreement) are explored and then down-weighted as “diagnostic.” This makes it difficult to assess the true trials factor and raises the possibility of selective highlighting of nulls over hints.  
- **Required fix:**  
  * Provide a clear accounting of the total number of distinct hypothesis tests performed (across all classifiers, all stratifications) and explicitly discuss the effective trials factor.  
  * Either (a) restrict formal claims strictly to a sharply defined “primary” set of tests and move all other explorations to a clearly marked exploratory section, or (b) adopt a more uniform multiple‑testing correction that treats all tests on equal footing.  
  * Clarify how the quoted look‑elsewhere corrections (Bonferroni or MC max-statistics) relate to this global trials budget.

---

P5-M4 (MAJOR) – Over-interpretation of bright vs dark residual despite contingency result  
- **Location:** §VI.A (bright/dark split, χ² ≈ 4932), §XI (target-class split).  
- **Problem:** The filament-class bright vs dark difference (|z| ≈ 2.1σ) and whole-catalog bright vs dark (0.81 pp, |z| ≈ 2.0σ) are called “residual structure” that the current data cannot cleanly partition between selection effects and astrophysics, but the language still suggests this is a meaningful diagnostic. Given the very strong contingency-test result (V-Web class and target program are *not* independent, p ≪ 10⁻³⁰⁰), these 2σ features are almost certainly dominated by selection function and class‑mixing rather than astrophysical signal. As written, the discussion risks overstating their significance relative to the clear evidence of strong selection correlations.  
- **Required fix:** Soften the interpretation: explicitly state that given the enormous χ² and the tiny dark sample sizes in some subclasses, the ∼2σ bright/dark differences cannot be interpreted as hints of astrophysical effects with current data. Present them as potential systematics diagnostics for future surveys, not as candidate physical signals.

---

P5-M5 (MAJOR) – Treatment of redshift-space distortions (RSD) is qualitative and incomplete  
- **Location:** §VIII (RSD treatment for DESIVAST), §XIII (Limitations, RSD discussion).  
- **Problem:** The paper correctly notes that the V-Web classification is performed in redshift space and that RSD can induce anisotropic distortions, but the analysis of their impact is qualitative and relies on scalar displacement estimates and heuristic arguments about eigenvalue shifts. For a PRD-level methods paper, a quantitative test (e.g. re-running the classification on a reconstructed density field, or on mocks with and without RSD) is warranted, especially given that environment classification is the core observable being used.  
- **Required fix:** Either:  
  * Add a quantitative RSD test, e.g. using a mock DESI-like catalog with known real- and redshift-space positions, to explicitly show the impact of RSD on the environment labels and on f_CW vs class; or  
  * Explicitly downgrade the claims to “within the limitations of a redshift-space classification we have not quantified RSD systematics,” and highlight RSD as a major caveat in the abstract and conclusions.

---

P5-M6 (MAJOR) – V-Web vs DESIVAST void-class purity mismatch needs clearer quantitative treatment  
- **Location:** §VIII.A–C, §IX.C.  
- **Problem:** The result “0/6 V-Web ‘void’ spirals fall inside any DESIVAST VoidFinder hole at z ≤ 0.24” is used to argue that V-Web voids at low z are dominated by survey-edge artifacts. While plausible, this is a tiny sample and not quantified in terms of expected overlap under simple models. Given that the DESIVAST void analysis is declared the primary path, the paper should be more precise about what this mismatch implies for the interpretability of V-Web-based results.  
- **Required fix:**  
  * Compute, for the low-z matched-spiral subsample, the expected fraction of V-Web void galaxies that should fall into DESIVAST voids under a reasonable random or clustered model, and quantify how surprising 0/6 is.  
  * Explicitly state that V-Web void labels at z ≲ 0.24 are not used quantitatively in the main conclusion because of this purity issue; confine all inferences about voids at low z to DESIVAST-based results.

---

P5-m1 (MINOR) – Statistical consistency checks are correct but presented in a confusing way  
- **Location:** Abstract (“2σ on the binomial null”), Table II, Table III, Table VI, §VI.B–D.  
- **Problem:** Several numerical statements mix percentage points, σ values, and n without explicitly walking the reader through the arithmetic. For example, the abstract quotes ±4.8 pp (2σ half-width) at n=428, but the derivation is only implicit. Similarly, the mapping from ∆f_CW = −0.0026 to σ_pred in various tables is correct but not explicitly shown. This hinders independent checking.  
- **Required fix:** For each load‑bearing scalar in the abstract and core tables, add in the main text a one-line explicit computation to allow quick verification (e.g., “for n=428, the binomial 2σ half-width is \(2\sqrt{0.5(1-0.5)/428} \approx 0.048\), i.e. 4.8 percentage points”). This is not conceptual but greatly aids transparency.

---

P5-m2 (MINOR) – Use of informal language in a PRD manuscript  
- **Location:** Throughout, e.g. “garden-of-forking-paths concern” (§V.B), “headline cosmic-web result,” “sharpens,” “null is strengthened,” “toy mapping.”  
- **Problem:** The tone is at times informal, which is atypical for PRD and may detract from the perceived rigor.  
- **Required fix:** Replace informal wording with standard scientific phrasing (e.g. “multiple testing concern” instead of “garden-of-forking-paths concern,” “main result” instead of “headline,” etc.).

---

P5-m3 (MINOR) – Version-history language and internal tags retained in the body  
- **Location:** §II (“Paper IV’s current headline (v1.0.166)… an earlier statistic was withdrawn in Paper IV v1.0.166”), Appendix B (“manuscript tag v0.1.52-2026-06-09”), “superseded unfiltered-join version is retained…”.  
- **Problem:** The main text contains explicit version tags and references to earlier draft behavior of a different paper and of the current analysis, which are internal bookkeeping rather than part of a final scientific argument. This is contrary to instruction item 8.  
- **Required fix:** Remove internal version descriptors and change-log style commentary from the main text. If absolutely necessary, note once that “we use the latest public version of Paper IV as of submission.”

---

P5-n1 (NIT) – Slightly inconsistent use of “T-Web”/“V-Web” nomenclature  
- **Location:** Title, abstract, §IV.A, §IX.C.  
- **Problem:** The manuscript uses “V-Web” for its own tidal-tensor classifier, even though it explicitly follows the Hahn et al. (2007) T-Web density-field recipe, and reserves “T-Web” for external work . While explained in a footnote, this is still confusing.  
- **Required fix:** Consider renaming your implementation consistently as “T-Web” or “tidal-tensor classifier” and reserve “V-Web” for velocity-shear based methods (Hoffman et al.), or at least emphasize in the abstract and section headers that “V-Web” in this paper is a T-Web density-field method.

---

P5-n2 (NIT) – Small stylistic redundancies  
- **Location:** Several places, e.g. phrases like “statistically indistinguishable” repeated frequently, “supporting rather than load-bearing” repeated, etc.  
- **Problem:** Mild redundancy in phrasing; not scientifically problematic.  
- **Required fix:** Optional editorial polishing to trim repetitive phrasing.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific result—a carefully executed null detection of any environment dependence of spiral chirality in DESI DR1—is potentially valuable, and I did not find evidence of citation fraud or incorrect bibliographic metadata. However, the manuscript in its current form does not meet PRD standards due to its heavy reliance on unpublished companion work as a black-box input, incomplete and somewhat confusing handling of different σ measures and nulls, overlong and logbook-like structure, and insufficiently quantitative treatment of key systematics like RSD and void-class purity. These issues require substantial structural and methodological revision before the paper can be considered for publication in PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E6 (ESSENTIAL) – Incorrect mapping from Δf_CW to σ at n=428 in the abstract and text  

- **Location:** Abstract (“±4.8 pp (2σ binomial half-width; … n = 428, ∼2σ on the binomial null)”), §V (“σ_from_half ≡ (n_CW − 0.5N)/(0.5√N)”).  
- **Problem:** For the void bin (n = 428, f_CW = 0.4836, Δf = −0.0164), the paper states “∼2σ on the binomial null,” but the σ_from_half definition used throughout gives  
  \(σ = (n_{CW} - 0.5N)/(0.5\sqrt{N}) = 2Δf\sqrt{N}\).  
  With Δf = −0.0164 and N = 428, this yields \(σ ≈ 2·(−0.0164)·\sqrt{428} ≈ −0.85\), not −0.68 as quoted in Table II and the abstract. The quoted 2σ half-width ±4.8 pp is consistent with Δf = ±0.048 and formula \(2\sqrt{0.5(1-0.5)/N}\), but the same mapping, applied to the actual Δf in the void row, does not give −0.68. The internal σ convention or the specific computation for the void bin is therefore inconsistent with the stated formula, and the “∼2σ” wording in the abstract is misleading.  
- **Required fix:**  
  * Recompute σ_from_half for all rows from the explicit formula and update Table II and any derived text; or, if a different σ convention was actually used (e.g., standard z = (f−0.5)/√(0.5·0.5/N)), state that formula explicitly and ensure all values are recomputed from it.  
  * Remove or correct the “∼2σ on the binomial null” description in the abstract to match the recomputed σ.  
  * Add the one-line derivation for the void bin analogous to the ±4.8 pp example, so readers can verify the mapping from Δf to σ numerically.

---

P5-E7 (ESSENTIAL) – Inconsistent σ normalization definition vs. practice  

- **Location:** §V (“signed σ_from_half ≡ (n_CW − 0.5N)/(0.5√N)”), Table II, Table III, Table IV, multiple σ values.  
- **Problem:** The stated definition implies σ_from_half = 2Δf√N, which makes σ grow as √N for fixed fraction offset and yields large σ for high‑N bins (e.g., Δf = −0.0026 at N ≈ 4×10^5 should give |σ| ≈ 3.3). The text uses this scaling explicitly for σ_pred in Eq. (1). However, several quoted σ_from_half values do not match 2Δf√N:  
  * Void row in Table II (see P5-E6).  
  * Some density-quintile σ_obs in Table III: with N = 158,327 and Δf = f_CW−0.5, 2Δf√N yields values notably different from those in the table for at least the more extreme bins.  
  * Cluster and filament σ in Table II (−4.66, −2.61) do not match 2Δf√N when recomputed directly from (n_CW, n) at the quoted precision.  
  These discrepancies indicate either arithmetic errors or that a different σ normalization (e.g. Δf / √(0.25/N)) was applied in code than the one written in the paper.  
- **Required fix:**  
  * Explicitly state the exact implemented formula for σ_from_half, including all factors, and ensure it matches Eq. (1) or clearly distinguish σ_pred and σ_from_half if they use different normalizations.  
  * Recompute all σ_from_half values in all tables and text from the declared formula and correct any inconsistent entries.  
  * Where σ_pred is compared to σ_obs, verify and explicitly demonstrate the mapping on at least one example per table (filament, cluster, density-quintile), to make the normalization transparent.

---

P5-M7 (MAJOR) – Abstract’s “∼2σ on the binomial null” void statement not supported by body  

- **Location:** Abstract (“…for V-Web void at n = 428, ∼2σ on the binomial null”), §VI.A (“void bin has σ = −0.68”).  
- **Problem:** The abstract characterizes the void class as “∼2σ on the binomial null” while the body gives |σ| = 0.68, which is clearly < 1σ by the stated σ_from_half definition. Even if the author’s informal “∼2σ” intended to refer to the width of the 95% CI (±4.8 pp) rather than the actual observed offset, the phrase is ambiguous and reads as if the observed deviation is ~2σ. Table II and the narrative (§VI.A) do not present any void statistic near 2σ. This overstates the information content of the void bin in the abstract relative to the body.  
- **Required fix:**  
  * Clarify in the abstract that the void bin is strongly statistics-limited and that the *expected* 2σ half-width is ±4.8 pp, while the *observed* offset corresponds to < 1σ.  
  * Or, remove “∼2σ on the binomial null” entirely and state directly that the void constraint is dominated by counting noise and is superseded by the DESIVAST void re-projection.  

---

P5-M8 (MAJOR) – σ vs p-value mapping not always quantitatively shown where “no 3σ” claims are made  

- **Location:** Abstract (“none reach 3σ after look-elsewhere correction”), §VI.B–E, §VII, Table V, Table VI.  
- **Problem:** The manuscript makes multiple global statements of the form “no test exceeds 3σ after look-elsewhere correction,” but in several cases the quantitative link between the observed statistic, the null distribution, and the 3σ threshold is not explicitly written out. For instance:  
  * HEALPix scans (Table V) quote |σ|_max and p, but the effective σ threshold after LEE is not converted back to an equivalent σ, leaving the “3σ” wording opaque.  
  * Phase‑2 sweep (Table VI) lists |σ_obs − σ_pred| and p_LEE per cell; the text asserts no cell shows a signal above the counting-noise floor and no residual above Bonferroni‑9, but the explicit numerical comparison to 3σ is not given per case.  
- **Required fix:**  
  * Wherever a “no 3σ” or “below 3σ” statement appears, add an explicit one-line numerical comparison (e.g., “for the worst case, |σ_obs − σ_pred| = 1.87 vs Bonferroni‑9 threshold 3.02”).  
  * For permutation-based tests, either convert the relevant p_LEE into an equivalent σ (for reader intuition) or explicitly say “the smallest look-elsewhere corrected p-value is p = …, corresponding to < 3σ for a Gaussian one-sided equivalent,” so that the “3σ” claim has a demonstrated quantitative basis.

---

P5-M9 (MAJOR) – σ vs. σ_pred comparability caveat sometimes missing at point of use  

- **Location:** §VI.C (projected density), §VII (Phase 2 discussion), §VIII.F (σ_vs_monopole table), Figure 5 caption, discussion in §VIII.E.  
- **Problem:** The paper generally distinguishes σ_from_half (data) and σ_pred (Paper IV monopole), and the abstract contains a global caveat about non-comparable σ from different nulls. However, there are several additional places where an explicit reminder is missing even though two different σ-like quantities are juxtaposed:  
  * §VI.C: “maximum per-quintile deviation is |σ|max = 3.94… predicted |σ_pred| ≈ 2.07… residual |σ_obs − σ_pred| ≈ 1.87” – three σ‑numbers from different constructions appear together with no local statement that σ_obs and σ_pred are different statistics under different nulls.  
  * Figure 5 caption shows σ_from_half bars and σ_pred diamonds, with Bonferroni thresholds, but does not explicitly specify that the diamonds are model-predicted σ under the Paper IV monopole null and not directly comparable to the raw σ across other contexts.  
  * §VII/Tab. VI: text mixes the descriptive “range (pp)” with “max |σ_obs − σ_pred|” and p_LEE; it notes Bonferroni thresholds but does not restate that σ_pred is derived from an external model and that σ_from_half vs σ_pred are conceptually different null quantities.  
  * §VIII.F and Table X: σ_vs_monopole is introduced properly, but later references (e.g., in §XII.A and §XV) speak about “σ values” without always reminding the reader they are post‑monopole‑subtracted residuals, not raw binomial σ.  
- **Required fix:**  
  * Add short explicit clarifying sentences at each of these locations, e.g. “Here σ_obs denotes the binomial σ_from_half and σ_pred is the Paper IV monopole prediction; they arise from different nulls and are not interchangeable.”  
  * Amend relevant figure captions (at least Fig. 5, and any other showing both σ_obs and σ_pred) and table notes (Tables III, VI, X) to label σ_obs, σ_pred, and σ_vs_monopole distinctly (or use notation such as \(z_{\rm bin}\), \(z_{\rm mono}\) as you already propose in P5‑E2).  

---

P5-m4 (MINOR) – Some abstract claims still not explicitly tied back to specific figures/tables  

- **Location:** Abstract statements about:  
  * “per-cell label-shuffle look-elsewhere p-values span 0.13–0.56 (no cell below 0.05)”  
  * “HEALPix scans at NSIDE ∈ {16, 32, 64} with label-shuffle nulls p = 0.61/0.135/0.413”  
  * “projected k = 5 NN density … |σ|max = 3.94 … residual |σ_obs − σ_pred| = 1.87, below all Bonferroni thresholds.”  
- **Problem:** These numbers are present in the body (p-range in Table VI and surrounding text; HEALPix numbers in Table V; density residuals in §VI.C and Table III), but the mapping is not fully explicit—for example, the abstract’s density statement uses only the most extreme quintile without saying that Table III’s full per‑quintile breakdown is where the inputs come from. A reader trying to audit the abstract sentence-by-sentence must hunt across multiple sections.  
- **Required fix:**  
  * Add brief parenthetical pointers in the abstract or early in the main text, such as “(Phase‑2 per-cell details in Table VI)” and “(density-quintile numbers in Table III),” so each numerical abstract claim can be directly traced to a specific table/section without ambiguity.  
  * Alternatively, add an explicit sentence at the start of each relevant section noting “This section provides the detailed support for the abstract statements on [HEALPix / density / Phase‑2 p-values].”

---

P5-m5 (MINOR) – Toy EFT bound phrasing still borderline between “illustrative” and “constraint”  

- **Location:** Appendix A (first paragraph and last paragraph).  
- **Problem:** You do say the operator is “a toy parametrization introduced in this work” and “not a quantitative ALP-coupling exclusion,” which is good. However, phrases like “an order‑of‑magnitude bound on the coupling g_ϕ|∇ϕ| … is |g_ϕ∇ϕ/H_0| ≲ 10^{-2}/⟨|Δρ/ρ_bg|⟩” and “we map the observational bound… as an order-of-magnitude guide” still read like a semi-quantitative constraint, especially when combined with talk of “exclusion” in the same paragraph. This slightly conflicts with the requirement (P5-E4) that this be clearly quarantined as non-quantitative, heuristic only.  
- **Required fix:**  
  * Replace “order-of-magnitude bound” with “order-of-magnitude *illustrative scaling*,” and avoid “≲” inequality notation; e.g., “one can *schematically write* |g_ϕ∇ϕ/H_0| ~ 10^{-2}/⟨|Δρ/ρ_bg|⟩ as a scaling relation.”  
  * Reiterate in the final sentence of the appendix that *no constraint is obtained* and that the operator is not a consistent EFT, to prevent any impression this is a derived physical limit.

---

P5-n3 (NIT) – A few residual internal-version references and draft-history comments remain  

- **Location:** §II (“Paper IV’s current headline (v1.0.166)… an earlier statistic was withdrawn in Paper IV v1.0.166”), §VI.D (“An earlier draft quoted filament bright/dark n of 416,701/21,203…”), §VII (“An earlier draft of this table reported per-cell ranges of 0.05–0.22 pp…”), §VIII.F (“An earlier draft attributed the excess to a ‘relaxed env-label confidence filter’…”), Appendix B (“manuscript tag v0.1.52-2026-06-09,” “superseded unfiltered-join version is retained alongside as prefilter legacy”).  
- **Problem:** These are change-log style and internal bookkeeping, rather than scientific content, and they clutter the narrative. They were already flagged in P5-m3 in general form, but several specific instances remain throughout the current draft.  
- **Required fix:**  
  * Remove explicit references to “earlier draft,” “withdrawn,” and manuscript tags from the main text.  
  * At most, keep a single neutral sentence summarizing that you use the latest public version of Paper IV and that some earlier internal checks used slightly different joins, without enumerating previous numbers.

---

If you systematically clean up the σ definition and recomputations (P5‑E6/E7), and strengthen local σ‑comparability caveats plus EFT-language quarantining (P5‑M9, P5‑m5), the remaining items are largely editorial.