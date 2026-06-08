# P5 auto-2026-06-08_1354pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11753 chars)
**Wall time**: 75.1s

---

P5-E1 (ESSENTIAL)  
Section: Abstract, page 1  
Issue: Multiple strong quantitative claims (e.g. “∆fCW = −0.0026… Paper IV”, “0.4974 ± 0.000279”, “∼ 9.5σ”, “∼ 0.2 pp monopole offset”, “−5σ catalog-level signal”) are taken from “Paper IV [3] (companion work, not yet peer-reviewed; in preparation)”. Paper IV is not available on arXiv, not published, and cannot be independently checked. Its quoted numbers, methods, and systematics (including the chirality monopole that is absolutely central to this paper’s interpretation) are therefore unauditable. The current manuscript treats Paper IV as if it were a stable, citable reference.  
Required fix: Paper IV must be (i) posted to arXiv with a stable identifier and (ii) submitted to a peer-reviewed journal, or its entire content must be folded into the present manuscript with full methodological detail, reproducible pipeline description, and all key numerical results so that the chirality catalog and its systematics are independently verifiable. The present paper cannot rely on an inaccessible “in preparation” work for its core inputs and for the key monopole subtraction that underpins all environmental conclusions.

P5-E2 (ESSENTIAL)  
Section: Abstract, page 1; §VIII F; Appendix B, page 19  
Issue: The abstract and §VIII F repeatedly treat the Paper IV catalog monopole as a precisely known external quantity (e.g. “∆fCW ≈ −0.0026… ∼9.5σ”, “P4 monopoly”, “fCW = 0.4974 ± 0.000279”) and use it to define σpred, σvs monopole, and “monopole-subtracted residuals.” Without seeing Paper IV it is impossible to verify (a) that 0.4974 ± 0.000279 is actually obtained, (b) that the quoted 9.5σ or ∆fCW = −0.0026 are correct, or (c) that the monopole is indeed “spatially uniform and quality-quartile-flat,” as claimed in §II. These facts and uncertainties directly control all claimed σ values in this paper.  
Required fix: Include in this manuscript a self-contained derivation of the chirality catalog monopole, including sample definition, training, test-time augmentation, error model, sky-systematics analysis, and the full calculation of fCW, its uncertainty, and the sky- and quality-dependence. Alternatively, if Paper IV is made public and peer-reviewed, the authors must explicitly quote from it the tables/figures where 0.4974 ± 0.000279 and ∆fCW = −0.0026 at “∼9.5σ” are obtained, and clearly propagate the corresponding uncertainty into all σpred / σvs monopole uses here.

P5-E3 (ESSENTIAL)  
Section: Abstract, page 1; throughout  
Issue: The abstract asserts precise σ and p-values (e.g. “label-shuffle p = 0.372”, “HEALPix scans… p = 0.61/0.135/0.413”, “Bonferroni thresholds”, “joint two-sample z-test |z| ≈ 3.4σ”) but the underlying counts, test statistics, and multiple-testing corrections are not fully tabulated anywhere accessible in the paper. Some calculations are sketched in prose but not reproducibly documented. As a result, I cannot re-compute every quoted σ, p, or percentage based solely on tables/figures in the current PDF as required. For example: the bright vs dark filament-class z ≈ 3.4σ is stated without the explicit fCW,b, fCW,d, nCW,b, nCW,d used; the label-shuffle p-values are given without top-level summary tables of the null distributions.  
Required fix: Add explicit tables for all load-bearing statistics referenced in the abstract and headline conclusions. Each table should list the underlying counts (n, nCW, nCCW or equivalent), the definition of the test statistic, and the resulting σ or p, so that every number in the abstract can be recomputed from the PDF alone.

P5-E4 (ESSENTIAL)  
Section: §V, eq. (1), page 4; abstract; multiple sections  
Issue: The paper uses the Paper-IV monopole ∆fCW to predict a σpred = 2∆fCW√N, and then compares observed σfrom half to σpred to declare residuals insignificant. However, the uncertainty on ∆fCW itself is never propagated into σpred, nor into σvs monopole. Treating an uncertain monopole as fixed biases the significance assessment of environmental residuals, especially at large N where σpred is large. This is particularly important given the claimed ∼8% discrepancy between the P4 monopole and the P5 matched-sample monopole in §VIII F.  
Required fix: Propagate the uncertainty on ∆fCW (from Paper IV or from a recomputation in this manuscript) into σpred and σvs monopole, and recompute all “within ∼1σ of the monopole prediction” statements with proper error propagation. If this significantly enlarges the error bars, the environmental null must be restated accordingly.

P5-E5 (ESSENTIAL)  
Section: §II, §XII, Appendix A; references [1], [2]  
Issue: The paper introduces a “bounce-chirality coupling class” and gives a schematic EFT operator in Appendix A, citing Alexander & Yunes 2009 [1] and Lue–Wang–Kamionkowski 1999 [2]. The text explicitly states that the specific operator used is not actually contained in those works, but the prose in §II and §XII may be read as suggesting that current bounce/inflation models motivate an environment-dependent chirality signature at the scales considered. This risks overstating the connection to the cited literature.  
Required fix: Make explicit, in the main text (not only in Appendix A), that no current bounce or inflation model predicts the specific environmental chirality signature being constrained here, and that the toy operator is introduced purely ad hoc for interpretive purposes. Clarify that [1] and [2] motivate only the generic idea of parity-violating couplings, not the particular density-gradient operator studied, and ensure that this distinction is present wherever “bounce-chirality coupling class” is mentioned.

P5-E6 (ESSENTIAL)  
Section: References , , ; multiple mentions in §§VIII–X  
Issue: Several core cross-checks rely on recently posted arXiv preprints:  
–  H. I. Ullah et al., arXiv:2604.02463 (2026) – verifies T-Web volume fractions.  
–  D. C. Zapata-Zuluaga et al., arXiv:2604.01456 (2026) – ASTRA catalog.  
–  H. Rincón et al., ApJ 982, 38 (2025); arXiv:2411.00148 – DESIVAST void catalog.  
 appears to have correct metadata as cited: arXiv:2411.00148, title and journal match, and it indeed presents DESI DR1 void catalogs with three algorithms, confirming the citation is accurate.  and  both appear on arXiv with the given authors, titles, and arXiv IDs; they are correctly cited as preprints “in submission” or equivalent, not as peer-reviewed. However, the manuscript leans heavily on DESIVAST as “peer-reviewed” and “standardized across the DESI collaboration.” While the ApJ reference is correct for , the paper treats DESIVAST as an absolutely authoritative classifier, while V-Web, ASTRA, and T-Web are still in preprint. That hierarchy is fine, but the text on p. 10–11 arguably overstates the immunity to redshift-space distortions (“essentially RSD-immune”) in a way that goes beyond what  itself claims;  does not provide such a strong RSD-invariance statement for per-galaxy membership.  
Required fix: Keep the bibliographic metadata as-is (they are correct), but temper the claims about DESIVAST’s RSD immunity to match what  actually states. Explicitly acknowledge that DESIVAST voids are identified in redshift space and that there is still residual RSD contamination at void boundaries, even if small. Any strong RSD immunity claim should either be supported by a specific section in  or weakened.

P5-E7 (ESSENTIAL)  
Section: Throughout; especially §V B “Primary vs. secondary analysis paths”, §VI, §VIII, §X  
Issue: The paper performs many analyses, splits, and hyperparameter sweeps (multiple environment classifiers, multiple stratifications, nine {Rs, λth} cells, HEALPix scans at three NSIDEs, several density and redshift stratifications, program splits), but a clear and fully pre-defined multiple-testing strategy is missing. §V B acknowledges that no preregistration exists and declares DESIVAST as “primary” post hoc, but the paper still reports numerous σ values and p-values without always stating that they are exploratory and not part of the main-tested family. This invites forking-path bias and creates ambiguity about which results are truly controlled at a given family-wise error rate.  
Required fix: Explicitly separate confirmatory from exploratory analyses. For the primary test family, list all statistics that are to be controlled (e.g., DESIVAST void vs non-void for three algorithms plus two zone definitions). For all other σ and p-values, explicitly flag them as exploratory diagnostics not controlled for multiplicity, and avoid numerical σ language (“3.4σ”, etc.) unless corrected for multiple testing within a clearly defined family. Rephrase any borderline “significance” findings (e.g. the 3.4σ bright/dark filament difference) accordingly.

P5-E8 (ESSENTIAL)  
Section: §III B, §VIII A–C, Table VIII; DESIVAST usage  
Issue: The DESIVAST cross-match claims specific hole counts and void membership statistics: 101,863 VoidFinder holes, 3,765 maximal voids, etc. These are broadly compatible with , but some numbers and selections are new: e.g. “nvoid = 56,981 DESIVAST-defined void galaxies (8.39% of low-z sample)” and specific per-algorithm nvoid and fCW values in Table VIII. These cannot be checked against  because they depend on the author’s proprietary cross-match and selection pipeline; there is no public reference catalog or script in the paper showing the exact joins and cuts.  
Required fix: Either (i) provide a fully documented, versioned, public code repository with the exact scripts used for the DESIVAST cross-match and the chirality joins, or (ii) move all such derived quantities into a supplementary data table embedded with the paper (e.g. a machine-readable table of TARGETIDs with DESIVAST membership and chirality labels), so that a referee can reconstruct the numbers. At PRD standards, a reader must be able to reproduce every scalar like nvoid = 56,981 from the published data and instructions.

P5-E9 (ESSENTIAL – per instruction 7)  
Section: Abstract, Table II (p. 5), Figure 2, Table VIII, Table XII, §§VI–VIII  
Issue: The instructions require that if sigma values from different null procedures appear side-by-side without explicit “not directly comparable” statements at each juxtaposition, this must be flagged. The paper often mixes:  
– σfrom half (binomial deviation from 0.5),  
– σpred from the catalog monopole,  
– σvs monopole (residual after subtracting σpred),  
– z from two-sample tests,  
– σ values implicit in label-shuffle p-values.  
These different σ’s are placed adjacent in text and sometimes in the same paragraphs and tables without explicit warnings that they are not directly comparable and are derived under different null hypotheses and error models.  
Required fix: In every place where two “σ” quantities of different type are reported in the same breath (e.g. σfrom half vs σpred, or σfrom half vs σvs monopole, or σfrom half vs two-sample |z|), label them distinctly in notation and add explicit text that these are not directly comparable significance measures. For example, rename σpred to ζpred or similar and σvs monopole to δσ, and add explanatory sentences wherever they are discussed together.

P5-M1 (MAJOR)  
Section: Abstract, §I, §XV  
Issue: The abstract and conclusions make strong qualitative claims like “no evidence for environment-dependent chirality beyond the catalog-monopole offset at current sensitivity” and “Spiral galaxy chirality is statistically independent of large-scale structure environment within DESI DR1 at V-Web resolution.” Given that the only sizable environmental anomaly discussed (the filament bright/dark sign flip at |z| ≈ 3.4σ) is left unresolved and could potentially reflect real astrophysical or environment-dependent systematics, these blanket null statements are too strong.  
Required fix: Soften the central claims to reflect the unresolved bright/dark filament residual and the fact that the analysis is limited by current catalog systematics. For example, state that no robust environment-dependent signal is detected after accounting for the catalog monopole and known selection effects, but that a ∼3σ filament bright/dark residual remains and requires further data to interpret.

P5-M2 (MAJOR)  
Section: §III C, §III D, Table I  
Issue: The cross-matching methodology relies on a 1″ nearest-neighbour association between the chirality catalog and DESI DR1, resolving duplicates by nearest separation. While the paper lists p50 and p99 separations, it does not quantify the expected rate of false matches or blending given DESI’s fiber assignment and the Legacy imaging resolution, nor does it show a control test (e.g. random-offset cross-matches) to demonstrate that contamination is negligible. At PRD standards, a cross-match of this scale should include a quantitative false-association estimate.  
Required fix: Add a sanity check quantifying the expected false-match rate, for example by repeating the cross-match after applying a large random offset to one catalog and comparing the match statistics, or by using a smaller radius and extrapolating. Present a short table or figure summarizing this, and discuss whether any residual mis-matches could bias fCW at the ∼10⁻³ level.

P5-M3 (MAJOR)  
Section: §IV A, algorithm step 5; Figure 1  
Issue: The V-Web algorithm description uses a survey-footprint mask “by dilation of occupied cells” and then quotes in-footprint volume fractions {void 0.244, wall 0.413, filament 0.333, cluster 0.010}. There is no explicit description of how the dilation scale was chosen, how edge cells are treated, or how this compares quantitatively with the volume-limited geometry used in [5–7]. Since the cosmic-web classification underpins the main result, the masking and edge treatment should be more explicit.  
Required fix: Provide a more detailed description of the mask construction (e.g., how many dilation steps, what criteria decide in-mask cells, and how sensitive the volume fractions are to this choice). Ideally, include a small table of volume fractions for at least two different masking schemes to demonstrate robustness.

P5-M4 (MAJOR)  
Section: §VIII, §IX A, §X  
Issue: The cross-validation with Tempel et al. 2014  and ASTRA  is described qualitatively with some numbers, but there is no global consistency table linking all four environment schemes (V-Web, T-Web, Tempel richness, DESIVAST voids, ASTRA probabilities) with their effective mappings to {void, wall/sheet, filament, cluster/knot}. This makes it hard to check that the environment mappings used are sensible and not cherry-picked.  
Required fix: Add a single harmonized table that lists, for each environment classifier, how its native classes are mapped onto the four canonical classes used for chirality analysis, along with the resulting counts. This will make the cross-comparisons reproducible and transparent.

P5-M5 (MAJOR)  
Section: Length & scope (entire 20 pages)  
Issue: Relative to its core claimed contribution (environmental dependence of CW fraction), the paper is quite long and heavily layered with secondary diagnostics, extensive null tests, and toy-theory discussion (Appendix A). For PRD, this level of breadth may be excessive given that the main result is a null and much of the analysis is repetition of similar tests yielding no signal.  
Required fix: Condense the manuscript by focusing on the main DESIVAST-based result and one or two key cross-checks (e.g. V-Web and Tempel or ASTRA). Consider moving the full Phase 2 sweep, several of the HEALPix permutations, and the EFT toy operator to a separate companion or to online supplementary material. A target length in the 12–14 page range would be more appropriate for the level of new physics insight delivered.

P5-M6 (MAJOR)  
Section: §XIII (Limitations), RSD discussion  
Issue: The discussion of RSD effects is partly qualitative and somewhat self-contradictory: it calls the DESIVAST path “essentially RSD-immune” while simultaneously acknowledging that, at the V-Web level, anisotropic eigenvalue distortions can lead to class flips and that a proper treatment requires reconstructed positions. This may mislead readers into underestimating the impact of RSD on environment classification and hence on any subtle fCW differences.  
Required fix: Clarify the RSD discussion to avoid overstatements. Make clear that: (i) DESIVAST voids are defined in redshift space and can be affected at the few-percent level by RSD; (ii) V-Web environment labels are definitely RSD-sensitive; and (iii) a full reconstruction-based reassignment has not been done here. Then explicitly state that, given current errors, these RSD uncertainties are subdominant, but they limit how far the null can be interpreted.

P5-m1 (MINOR)  
Section: Abstract, “three-algorithm test”; §VIII  
Issue: The phrase “three-algorithm test on 56,981 void spirals” could be misread as three independent chirality classifiers, whereas it actually refers to three void-finding algorithms (VoidFinder, V2-REVOLVER, V2-VIDE) under a single chirality catalog.  
Required fix: Rephrase in the abstract to “three void-finding algorithms (VoidFinder, V2-REVOLVER, V2-VIDE)” to avoid ambiguity.

P5-m2 (MINOR)  
Section: §II, first paragraph  
Issue: The statement “No published bounce or inflation model currently predicts a specific environment-conditional chirality signature at this scale; the present null therefore supplies an empirical upper bound on any future model in the bounce-chirality coupling class” is correct in spirit, but the phrase “therefore supplies” might be interpreted as a quantitative bound on existing models.  
Required fix: Slightly soften to “thus can be interpreted as an empirical upper bound that any such future model would need to satisfy” to avoid over-claiming.

P5-m3 (MINOR)  
Section: Table II caption, Figure 2 caption  
Issue: Table II and Figure 2 present σfrom half without explicitly stating that σ is computed under a binomial assumption with no monopole subtraction. The reader must infer this from §V.  
Required fix: Add a brief note to the captions clarifying that σfrom half is the binomial deviation from parity fCW = 0.5 and that monopole-subtracted residuals are given separately in §VIII F.

P5-m4 (MINOR)  
Section: References  
Issue: Reference [3] and [4] are listed as “companion paper… in preparation; manuscript in preparation” with no arXiv identifiers, making it unclear when these will be available.  
Required fix: Once arXiv IDs exist, update references [3], [4] accordingly, or, if these works remain unpublished for an extended period, avoid referring to them as “papers” and instead summarize any needed content within the present article.

P5-n1 (NIT)  
Section: Footnote a, page 2  
Issue: The text calls the tidal-tensor classifier “V-Web” while clarifying it is actually a T-Web-style potential Hessian, not the velocity-shear V-Web of Hoffman et al. 2012. This is explained, but the naming is still a bit confusing.  
Required fix: Optionally rename in the text to “tidal-tensor web (T-Web-like; hereafter ‘V-Web’ for continuity with some literature)” once, to reduce confusion.

P5-n2 (NIT)  
Section: Typographical  
Issue: A few minor typos, e.g. “σfrom half” is sometimes written without a space (“σfrom half”) and sometimes with conceptual spacing; “σ void” vs “σ void” formatting; “monopole- subtraction” with stray hyphenation. These are small but visible at PRD’s style level.  
Required fix: Run a careful copy-edit pass to standardize notation and fix minor hyphenation and spacing issues.

P5-n3 (NIT)  
Section: Appendix B, “Reproducibility checklist”  
Issue: The checklist mentions “Deterministic seed: 20260515” and “All Phase 2 sweep cell configs persisted in companion data repository” but does not give any identifier (e.g. a DOI or repository name) in the main text.  
Required fix: Provide a generic, non-URL identifier in the main text (e.g. “data and code are archived under DOI: XXX or in the DESI collaboration’s GitLab under project name YYY”) to make the claim verifiable.

P5-n4 (NIT)  
Section: §XII C, “Comparison to Shamir 2022”  
Issue: The statement that this result leaves “no room” for a Shamir-level signal is somewhat strong given the different methodologies and systematics between Shamir 2022  and this analysis.  
Required fix: Soften to “strongly disfavors” or “is in clear tension with” instead of “leaves no room for.”

## Summary recommendation

REJECT

The central dependence on an unpublished, non-arXiv “Paper IV” for the chirality catalog, monopole bias, and key numerical inputs is incompatible with PRD standards of verifiability and reproducibility. In addition, the handling of multiple testing, σ definitions, and RSD systematics needs significant tightening, and the paper’s length is disproportionate to its incremental null result. These issues require structural changes (especially making the chirality catalog and its systematics fully public and independently reviewable) rather than minor revision.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E10 (ESSENTIAL)  
Section: Abstract; §V, eq. (1); §VI A; §VII A; §VIII F; Table X  
Issue: The paper uses σpred = 2∆fCW√N with ∆fCW ≈ −0.0026 to interpret deviations, but this relation is only approximately valid when the catalog monopole is treated as a fixed offset and N is large. In several places the text compares observed σfrom half directly to σpred without making explicit that σpred is an *approximate* expected σ, not a measured test statistic, and that an exact comparison would require binomial error propagation around fCW = 0.5 + ∆fCW (including the uncertainty on ∆fCW). This is especially critical where σpred is used to argue that an 11.3σ filament deviation in the Phase-2 sweep is “predicted, not measured,” or where σvs monopole is claimed < 1.15σ after subtraction.  
Required fix: Make explicit in §V that σpred is an approximate expectation under a model with a fixed monopole and that, formally, the null variance should include both binomial counting noise and monopole uncertainty. Either (i) replace σpred with an exact z-score computed from f = 0.5 + ∆fCW and binomial variance, or (ii) clearly label σpred as an approximation and quantify its error (e.g., by MC using Paper IV’s posterior on ∆fCW). Revisit all “predicted, not measured” and “within 1σ of σpred” statements accordingly.

P5-E11 (ESSENTIAL)  
Section: §V A (Look-elsewhere); §VI C; §VI E; Table V; Figure 4  
Issue: The Bonferroni thresholds and empirical max-stat p-values are reported, but the arithmetic is not fully reproducible from the text. For example, HEALPix NSIDE = 16 has npix = 1054 and NMC = 1000, and Table V quotes p = 0.607 with |σ|max,obs = 3.32 and |σ|max,null,p99 = 4.50, but the paper does not report the actual empirical null quantiles or the count of permutations exceeding |σ|max,obs, making it impossible to check p = 0.607. Similarly, for density quintiles (Table III) the Bonferroni threshold |σ|Bonf0.01,5 ≈ 3.09 is given, but not derived numerically from Eq. (2), and no explicit check (e.g. 3.09 vs 3.94) is tabulated.  
Required fix: For each LEE-corrected family used in the abstract or headline narrative (redshift, density, HEALPix), add a compact table listing: K, α, the resulting |σ|Bonfα,K, and, for the empirical max-stat null, the number of MC realizations with |σ|max ≥ |σ|max,obs and the resulting p from Eq. (3). This makes every reported Bonferroni threshold and p-value arithmetically auditable from the PDF.

P5-E12 (ESSENTIAL)  
Section: §VIII B–D; Table VII; Table VIII; DESIVAST cross-match  
Issue: The DESIVAST void vs non-void numbers (e.g. nvoid = 56,981, ∆fCW = 0.0007; three-algorithm |∆fCW| < 0.002) rely on a custom point-in-sphere and GALZONE/ZONEVOID pipeline. Although some arithmetic can be recomputed (e.g. σfrom half from n, fCW in Table VII), the paper does not provide enough detail to reproduce the *geometry* of the cross-match (exact radius handling, KDTree parameters, handling of overlapping holes, masking of EDGE/OUT flags). This means the quoted 8.39% void fraction and per-algorithm nvoid cannot be independently recomputed from DESIVAST plus DR1 without code.  
Required fix: Extend §VIII A–D or Appendix B with a precise, step-by-step description of the DESIVAST cross-match algorithm, including (i) how overlapping VoidFinder holes are treated; (ii) the exact KDTree query parameters; (iii) how EDGE/OUT/DEPTH flags are filtered in GALZONE; and (iv) how conflicting memberships between algorithms are handled. Ideally include a small, human-readable pseudo-code block so that a reader with DESIVAST and DR1 in hand can recreate nvoid and nnon−void without needing your repository.

P5-E13 (ESSENTIAL)  
Section: §X; Table XII; ASTRA cross-check  
Issue: Table XII reports “fCW range (pp)” and “max |σ|vs 1/2” for three classifiers on the Noverlap = 25,186 sample, but does not give the underlying per-class n and nCW. Without those counts, the σ values and the stated Bonferroni assessment (no class exceeding |σ| ≈ 3.02 at α = 0.01) cannot be independently verified. This is a load-bearing robustness claim because the paper uses ASTRA to show classifier-agnostic environment independence on the EDR overlap.  
Required fix: Add a full per-class table for the ASTRA argmax, ASTRA entropy-weighted, and V-Web-on-overlap classifiers, listing n, nCW, fCW, and σfrom half per class. This will allow a referee to recompute the ranges, σ values, and Bonferroni statements directly.

P5-E14 (ESSENTIAL)  
Section: §IX A; Table XI; Figure 7 (Tempel cross-check)  
Issue: The cross-validation with Tempel et al. quotes a key concordance figure of 0.026 percentage points between Tempel filament-like and V-Web filament fCW, and uses this to support the main environmental null. However, the exact V-Web fCW for the *Tempel-overlap* filament subset is not tabulated; the reader only sees global V-Web fCW from Table II and the Tempel numbers from Table XI. Without a table of V-Web fCW computed on the same 110,586-galaxy overlap, the stated 0.026 pp concordance cannot be checked.  
Required fix: Add a small table giving, for the Tempel-overlap subset, V-Web per-class n, nCW, fCW, and σfrom half, and explicitly compute the difference |fCW,Tempel – fCW,V-Web| for each mapped class pair. Ensure the 0.026 pp value can be recomputed from that table alone.

P5-M7 (MAJOR)  
Section: Abstract; §VI A; Table II; Figure 2  
Issue: The abstract states “Per-class CW fractions … are, in order of decreasing n: 0.4980 (filament; n = 408,187, −2.61σ), 0.4963 (cluster; n = 397,505, −4.66σ), 0.5034 (wall; n = 6,673, +0.55σ), and 0.4836 (void; n = 428, −0.68σ). The range across classes is 1.98 percentage points.” Table II lists the same fCW values and σ, but does not provide the raw counts nCW used to derive σ. While σ can be recalculated approximately from n and fCW, the difference between σ = −4.66 and a recomputed value depends sensitively on rounding of fCW and on whether Jeffreys or Wald intervals were used. At PRD standards, headline σ from half should be exactly recomputable.  
Required fix: Extend Table II to include nCW (or nCCW), and, in the caption, explicitly state the exact formula used for σfrom half (e.g. σ = (nCW − 0.5N)/√(0.5N)). This will allow exact reproduction of the -2.61σ, -4.66σ, etc., from the table alone, tightening arithmetic transparency between abstract and body.

P5-M8 (MAJOR)  
Section: §VII; Figure 5; Table VI  
Issue: The Phase 2 sweep claims that “the max fCW range across env classes, maximized over the nine cells, is 0.22 percentage points (at Rs = 25, λth = 0.3)” and that this is below per-class counting-statistics floors. Table VI reports ranges per cell, but the underlying fCW values per class per cell are not given, so the 0.22 pp max and the statement “no (Rs, λth) cell shows an inter-class range that exceeds the dominant per-class measurement uncertainty” cannot be checked. This sweep is repeatedly invoked as a key robustness check.  
Required fix: Add a supplementary table (main text or appendix) that, for each of the nine (Rs, λth) cells, lists per-class n, nCW, and fCW. Then the reader can compute the ranges in Table VI, verify the 0.22 pp maximum, and independently compare these ranges to 1/(2√nclass).

P5-M9 (MAJOR)  
Section: §VIII F; Table X; §VI A; §VIII E–F  
Issue: The “cross-survey P4-monopole-residual analysis” introduces a P5 matched-sample monopole fCW^P5 = 0.4972 based on n = 812,793 env-labeled spirals, but Table X uses the 791,635-subset and lists σvs monopole values for each environment. The text claims the 812,793 and 791,635 monopoles agree to 4 decimals, but no σ or nCW is given for the 812,793 sample, and the exact mapping from the P4 ∆fCW = −0.0026 to the P5 ∆fCW ≈ −0.0028 is only sketched. This makes the internal consistency between catalog-level and matched-sample monopoles difficult to audit.  
Required fix: Provide a small table summarizing the P5 monopole calculation: total n, nCW, fCW, σfrom half for both the 791,635 and 812,793 samples. Explicitly show how σpred ≈ 4.6σ is obtained from ∆fCW = −0.0026 and how the observed −5.00σ implies ∆fCW ≈ −0.0028. This will close the loop between the P4 monopole, the P5 monopole, and the residual 8% discrepancy cited.

P5-M10 (MAJOR)  
Section: §VI B–E; Abstract; multiple places discussing label-shuffle p-values  
Issue: The abstract reports label-shuffle p = 0.372 (redshift) and HEALPix label-shuffle p = 0.61/0.135/0.413, but the body never shows the explicit test statistic distributions (e.g. histograms of max-|σ| from permutations) nor the rank of the observed statistic within those distributions. Without those, it is impossible to check that, for instance, p = 0.135 at NSIDE = 32 corresponds to the fraction of permutations exceeding |σ|max,obs = 4.13.  
Required fix: For each null procedure that leads to a quoted p in the abstract, add either (i) a compact figure showing the null distribution of the test statistic with the observed value marked and the empirical p reported, or (ii) a table giving the empirical CDF at the observed statistic and the implied p. This makes the p-values numerically reproducible and ties abstract numbers to explicit plots or tables.

P5-m5 (MINOR)  
Section: §IV A; Figure 1 caption; §III B  
Issue: Figure 1’s caption and §IV B state that the in-footprint volume fractions sum to {0.244, 0.413, 0.333, 0.010} ≈ 1.000, and §IV A step 5 gives 3,150,086 in-mask cells out of 256^3 = 16,777,216, i.e. 18.8% of the cube. The paper does not explicitly confirm that the quoted fractions are computed only over those in-mask cells, although this is implied. This can confuse readers trying to reconcile “in-footprint” with the 18.8% mask coverage.  
Required fix: Add a sentence to §IV B or the Figure 1 caption explicitly stating that the quoted volume fractions are computed over the 3,150,086 in-mask cells only (18.8% of the cube) and not over the full 256^3 grid. This removes an implicit assumption that complicates arithmetic cross-checks.

P5-m6 (MINOR)  
Section: §VIII A; DESIVAST per-galaxy cross-match  
Issue: The text states “restricting the matched-spiral catalog to z ≤ 0.24 leaves only n = 6 V-Web void-class spirals” and later “Converting each of the 6 spirals … returns 0/6 V-Web ‘void’ spirals inside any of the 101,863 DESIVAST VoidFinder holes.” This 0/6 is used to illustrate V-Web void impurity at low z, but no explicit binomial uncertainty or caveat is given; 0/6 is consistent with up to ~45% true void fraction at 95% C.L. and therefore is too small to be informative quantitatively.  
Required fix: Add a brief quantitative caveat that 0/6 implies only a very weak upper bound on the true V-Web void purity at low z, and that this statistic is used qualitatively to illustrate the survey-shell artifact, not as a strong quantitative constraint.

P5-n4 (NIT)  
Section: §VI E; §VIII E; HEALPix analyses  
Issue: The HEALPix analyses use different NSIDE and minimum per-pixel spiral-count cuts (e.g. ≥200 in §VIII E for the correlation test), but the text occasionally uses phrases like “HEALPix scans at NSIDE ∈ {16, 32, 64}” without always reminding the reader of the specific cut applied in that context. This makes it slightly harder to track which NSIDE/cut combination produced which σ or p.  
Required fix: When referring to HEALPix results outside the immediate subsection where they are defined, briefly restate the NSIDE and spiral-count threshold used (e.g. “NSIDE = 32, ≥200-spiral pixels”). This improves internal cross-reference clarity without changing any results.

If you address all of the above in addition to the original P5-E/M/m/n items, the manuscript’s numerical and logical transparency will be substantially closer to PRD’s expected rigor.