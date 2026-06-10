# P5 R27conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.58.pdf` md5=6ffcd714 pages=27
**Input format**: TEXT + web search + pass-2 self-critique (11701 chars)
**Wall time**: 40.9s

---

I can audit the *internal consistency* of the paper text you provided, but I **cannot complete the arXiv/NASA ADS verification you requested** because the only web search results available here are unrelated artifact-evaluation pages and do not contain the cited astronomy papers or bibliographic metadata needed for external verification. That means I can flag **textual, numerical, and structural** issues in the rendered paper, but I cannot honestly certify whether the cited papers [1]– match arXiv/ADS from the evidence available.

The paper, as rendered, has **multiple PRD-level citation and consistency problems** that are already sufficient to require at least **major revision**, and several are potentially **essential** if they reflect the actual PDF rather than reviewer metadata.

- **ESSENTIAL — internal review-log / draft-history language appears in the body.**  
  - **Section:** multiple places, including Introduction, VI A, VII, VIII, IX C, XI, Appendix B  
  - **Offending text:** “*current draft*”, “*earlier draft*”, “*withdrawn*”, “*superseded*”, “*pre-registration caveat*”, “*artifact outputs*”, “*committed*”, “*pipelines/...json*”, “*r23conf*”, “*r24conf*”, “*v0151*”, “*R7/R8/R-round*”-style internal bookkeeping.  
  - **Problem:** The paper body reads like a merged analysis log with revision notes and pipeline filenames. PRD papers should not contain internal audit prose or version-history commentary in the scientific narrative.  
  - **Required fix:** Remove all draft-history, provenance-log, and bookkeeping text from the manuscript body; move reproducibility details to an appendix or data availability statement, without internal revision labels.

- **ESSENTIAL — the manuscript contains self-contradictory sample counts.**  
  - **Section:** Abstract, II, III D, VI A, VIII F, XII  
  - **Offending text:** “*812,793 env-labeled spiral rows*”, “*783,820 unique env-matched spirals*”, “*791,635 unique chirality-relevant matched spirals*”, “*7,815 lack an environment row*”, “*21,158-row excess (2.7%)*”, “*21,158 = 812,793 - 791,635*”.  
  - **Problem:** Several counts are used interchangeably for different parents (row-level, unique-TARGETID, env-matched subset), but the paper repeatedly presents them as if they were the same parent sample. This makes load-bearing statistics ambiguous and undermines the validity of quoted \( \sigma \) values and \( p \)-values.  
  - **Required fix:** Define one canonical parent sample per analysis, then use consistent nomenclature and a flow chart/table that reconciles every count exactly once.

- **ESSENTIAL — key significance statements are not properly qualified when compared across different null procedures.**  
  - **Section:** Abstract, V, VI A, VI E, VII, VIII F, IX A  
  - **Offending text:** side-by-side reporting of raw \( \sigma \), monopole-subtracted residual \( \sigma_{\mathrm{vs\ monopole}} \), Bonferroni thresholds, and permutation \( p \)-values.  
  - **Problem:** The paper itself warns that these are “not comparable,” but then places them adjacent in a way that will be read as directly comparable in the abstract and results. Your instructions explicitly require a flag if different null procedures appear side-by-side without explicit “not directly comparable” qualification at every juxtaposition. That happens repeatedly.  
  - **Required fix:** Separate the inferential families into clearly labeled subsections and never place raw \( \sigma \), monopole-referenced residuals, and permutation \( p \)-values in the same sentence unless the non-comparability is stated in that sentence.

- **MAJOR — the abstract overstates the strength of the result relative to the body.**  
  - **Section:** Abstract vs. VI–VIII  
  - **Offending text:** “*Headline result: the CW fraction shows no environment dependence beyond...*” and “*no evidence for environment-dependent chirality beyond the catalog-monopole offset*”  
  - **Problem:** The body contains a nontrivial bright/dark sign-flip at roughly \(2\sigma\), strong dependence on selection-function structure, and a corrected reanalysis that changes class volumes substantially. The abstract compresses this into a clean null without fully reflecting the internal caveats and multiple residual structures.  
  - **Required fix:** State explicitly that the null is conditional on the chosen classifier and correction scheme, and summarize the strongest residuals, including the bright/dark and sky-mask effects.

- **MAJOR — there are multiple places where quoted \( \sigma \) values do not match the provided counts exactly or are not transparently recomputed.**  
  - **Section:** Abstract, VI A, VI C, VIII F, IX E, X, XIII  
  - **Offending text:** Examples include “\(-2.61\sigma\)”, “\(-4.66\sigma\)”, “\(-0.68\sigma\)”, “\(-5.00\sigma\)”, “\(-4.75\sigma\)”, “\(1.87\)” residuals, “\(|z|\approx2.1\sigma\)”.  
  - **Problem:** Several of these are presented as load-bearing scalars, but the paper does not provide a transparent recomputation path from the displayed counts in every case, and in some places the same quantity is re-expressed under different denominators.  
  - **Required fix:** Add explicit recomputation formulas and a table of every scalar with input counts, denominator choice, and rounding convention.

- **MAJOR — the manuscript uses a questionable mix of “row-level” and “unique-galaxy” statistics for the same inference.**  
  - **Section:** VI A, VI D, VI E, VIII F, IX A, XI  
  - **Offending text:** “*row-level parent repeats 2.7% of TARGETIDs*”, “*unique-spiral subset*”, “*recomputed on unique-TARGETID parent*”, “*row-level two-sample z is approximate*”.  
  - **Problem:** The paper repeatedly draws inferential conclusions from non-disjoint row-level splits, then retroactively cautions they are approximate. In PRD standards, this must be resolved before publication.  
  - **Required fix:** Use one statistically valid unit of analysis, or present a mixed-effects / clustered uncertainty treatment that accounts for repeated targets.

- **MAJOR — the DESIVAST/V-Web comparison is internally inconsistent in multiple places.**  
  - **Section:** VIII B–D, VIII F, IX C  
  - **Offending text:** V-Web void class at \(n=428\) vs DESIVAST void \(n=56{,}981\); “*0/6 V-Web void spirals inside any DESIVAST hole*”; “*all three algorithms return |∆fCW| ≲ 0.002*”; “*catalog-native void definition is the cleaner statistic*”.  
  - **Problem:** The paper alternates between a permissive hole-union criterion, maximal-sphere criterion, and catalog-native zone membership. These are materially different classifiers and are not always distinguished clearly enough when the conclusions are stated.  
  - **Required fix:** Present each void definition as a separate estimator with separate sample sizes and explicitly state which one anchors the headline claim.

- **MAJOR — the grid/smoothing discussion contains physically dubious and self-contradictory statements.**  
  - **Section:** IV A, VII, IX A  
  - **Offending text:** “*Rs = 10 Mpc/h cells sit below the 25.9 Mpc/h grid resolution and are retained only as a degenerate near-unsmoothed limit*”; “*the field carries no modes at that scale*”; “*selected cells are below the tested convergence regime*”.  
  - **Problem:** The text acknowledges the smoothing scale is below the grid cell size, then still uses those cells in the phase-2 sweep. That is methodologically problematic and likely invalid for claiming a physical robustness scan.  
  - **Required fix:** Either remove the \(R_s=10\) cells entirely or justify them with a proper resolution analysis showing they are meaningful at the discretized field level.

- **MAJOR — several figure captions do not fully match the body claims.**  
  - **Section:** Figures 1–9  
  - **Offending text:** Figure 3, 5, 6, 7, 8, 9 captions versus the surrounding text.  
  - **Problem:** Captions often summarize “no coherent large-scale structure” or “null” while the body reports nontrivial residuals, selection effects, and a \( \sim 2\sigma \) bright/dark sign flip. Captions also sometimes omit key caveats (e.g. row-level repetition, unique-target deduplication, or the fact that some plots are only on a restricted overlap sample).  
  - **Required fix:** Make each caption self-contained and consistent with the exact sample and null procedure used.

- **MAJOR — bibliography entries [3], [4], , ,  are not verifiable from the supplied search results and include future-dated or unpublished claims.**  
  - **Section:** References  
  - **Offending text:** “*in preparation*”, “*preprint (2026)*”, “*ArXiv 2604.02463*”, “*ApJ 982, 38 (2025)*”, “*DESI-EDR-based probabilistic environment catalog*”.  
  - **Problem:** I cannot verify these against arXiv/ADS from the provided results, and [3], [4] are explicitly unpublished companion works. In a PRD submission, citing unpublished companion papers as load-bearing evidence is risky unless the claims are independently supported in the present manuscript.  
  - **Required fix:** Either publish the companion works or remove any claim that depends on them.

- **MAJOR — the paper contains unsupported “first/largest/cleanest” style claims.**  
  - **Section:** VIII, X, XII, XIV, XV  
  - **Offending text:** “*largest matched-sample environmental-dependence test... to date*”, “*cleanest single chirality-in-voids measurement*”, “*closest currently available substitute*”, “*most cleanly read as a null*”.  
  - **Problem:** These are not supported by a systematic literature review in the paper and are stronger than what the evidence shown here can establish.  
  - **Required fix:** Remove superlatives unless backed by a documented literature survey.

- **MAJOR — statistical methodology is overcomplicated and not fully justified.**  
  - **Section:** V, VII, IX A, XI  
  - **Offending text:** mixture of Jeffreys intervals, raw \( \sigma \), predicted \( \sigma_{\mathrm{pred}} \), Bonferroni, permutation maxima, stratified shuffles, and multiple alternative denominators.  
  - **Problem:** The inferential framework is not cleanly hierarchical, and the paper does not isolate one primary test with a predeclared null. This makes the analysis vulnerable to researcher degrees of freedom.  
  - **Required fix:** Predefine one primary endpoint, one primary null, and one multiplicity correction scheme; move the rest to sensitivity checks.

- **MINOR — duplicate / awkward phrasing and typographical issues.**  
  - **Section:** Abstract, IV, V, VIII, IX, X, Appendix B  
  - **Offending text:** “*canonical canonical-mask*” is not present, but several near-duplicate constructions and awkward repetitions appear, e.g. “*per-pixel per-pixel*”-style redundancy, “*row-level parent*” repeated excessively, “*void bin binomial*” style phrasing.  
  - **Problem:** Readability is impaired, and some repeated phrases suggest copy/paste from analysis notes.  
  - **Required fix:** Edit for concision and consistency.

- **MINOR — notation is not consistently defined.**  
  - **Section:** Abstract, I, IV, V, VII, VIII, IX  
  - **Offending text:** \( \sigma_{\mathrm{from\ half}} \), \( \sigma_{\mathrm{pred}} \), \( \sigma_{\mathrm{vs\ monopole}} \), \( \Delta f_{\mathrm{CW}} \), \( n_{\mathrm{void}} \), \( N_{\mathrm{MC}} \), “Paper IV monopole”, “P4 monopole”.  
  - **Problem:** Notation shifts between prose and equations, and abbreviations are sometimes introduced only after use.  
  - **Required fix:** Add a notation table.

- **MINOR — some units and coordinate conventions are underexplained.**  
  - **Section:** IV A, VIII A, IX A, XIII  
  - **Offending text:** “*25 Mpc/h Gaussian smoothing*”, “*h−1 Mpc*”, “*comoving Cartesian*”, “*equatorial coordinates*”.  
  - **Problem:** The conventions are probably standard, but the paper mixes \(h^{-1}\,\mathrm{Mpc}\), Mpc/h, and comoving/h without always defining them at first use.  
  - **Required fix:** Standardize units and define them once.

- **MINOR — the paper is too long for the stated contribution.**  
  - **Section:** overall manuscript  
  - **Problem:** For a negative result on environment dependence, the manuscript is exceptionally long and includes many secondary analyses, reanalyses, and corrective digressions that read like internal validation notes rather than a focused PRD article.  
  - **Required fix:** The paper should be trimmed substantially; a recommended maximum for this contribution would be **~18–20 pages** of main text, with the exhaustive robustness material moved to an appendix or supplement.

## Summary recommendation
**REJECT**

This manuscript is not yet at PRD standard because the rendered text contains extensive internal-draft bookkeeping, unresolved sample-definition inconsistencies, mixed row-level vs unique-object inference, and a results narrative that is not cleanly separated from diagnostic reanalyses and sensitivity checks. Even before external arXiv/ADS verification, the paper as written has enough internal contradictions and presentation problems that the main claim cannot be trusted in its current form.

---

## PASS 2 — self-critique findings (what initial review missed)

[P5-E1] **Arithmetic mismatch in the abstract’s row-count arithmetic.** The abstract states “**812,793 env-labeled spiral rows**” and also “**783,820 of the 791,635 unique chirality-relevant matched spirals**,” but \(791{,}635 - 7{,}815 = 783{,}820\) is a unique-galaxy count, not a row count, so the text is mixing denominators in a way that makes the “21,158-row excess (2.7%)” bookkeeping ambiguous. This is not just a style issue: the same paragraph uses row-level, unique-TARGETID, and env-matched counts as if they were interchangeable.

[M1] **Abstract overstates a null while the body contains a stronger qualifier.** The abstract says the headline result is that CW fraction shows no environment dependence beyond the catalog monopole, but later sections explicitly say the result is *conditional* on the chosen classifier/correction scheme and that the bright/dark residual is a notable structure that is not fully partitioned. The abstract should reflect that conditionality, not present the null as unconditional.

[M2] **A stale sample-size statement appears in the body.** In Section IX C, the paper says the V-Web/T-Web volume-fraction comparison is on the same survey-shell systematic footing, but the accompanying numeric comparison of void and cluster fractions is stated against a full-sample DR1 V-Web run and a different 800 Mpc cube T-Web study. The text presents the comparison as if it were more directly like-for-like than it is, which is a stale framing problem rather than just a citation problem.

[M3] **The “largest matched-sample environmental-dependence test” claim is unsupported by the paper’s own comparison set.** Section VIII B claims this is “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date,” but the paper itself also discusses a 96,753-spiral Tempel overlap, a 25,186-galaxy ASTRA overlap, and a full 791,635-galaxy matched chirality parent. Because no systematic comparison table is given that justifies “largest” across the relevant literature, the novelty claim is hand-waved.

[N1] **Figure 3 caption/body mismatch on what is being visualized.** The caption says all four classes bracket the Paper IV monopole and parity line, but the body immediately emphasizes that the filament and cluster deviations are sample-size-scaled projections of the monopole rather than environment effects. The caption suppresses the more important interpretive qualifier, so it overstates the visual message.

[N2] **Figure 5/Table III mismatch on the interpretation of the residuals.** Figure 5 and Table III present the quintiles as a clean monopole-consistent null, but the body says the maximum raw deviation is \(3.94\sigma\) and that the relevant conclusion is only after subtracting the Paper IV monopole prediction. The caption does not clearly warn that the apparent significance depends on using the raw \( \sigma \) rather than the monopole-referenced residual.

[N3] **Figure 7/body mismatch on the physical status of the \(R_s=10\) cells.** The body explicitly says the \(R_s = 10\) rows are below the 25.9 Mpc/h grid sampling scale and excluded from the robustness claim, yet Figure 7 still visually summarizes the full nine-cell sweep without separating resolved from under-resolved cells. That makes the figure easier to misread as a physical sweep than the text allows.

[N4] **Figure 8 caption/body mismatch on sample scope.** The caption describes the plotted map as the \(z \le 0.24\) matched-spiral subsample, but the body switches between the 727-pixel overlap set, the 1,496 valid-pixel set, and the 885 occupied-pixel map without making the figure scope explicit. A reader could reasonably infer the correlation statistic applies to the full plotted pixels, but it only applies to the intersection subset.

[C1] **Equation (1) is dimensionally incomplete as written.** The paper defines \( \sigma_{\mathrm{pred}} = \Delta f_{\mathrm{CW}} / (0.5/\sqrt{N}) = 2\,\Delta f_{\mathrm{CW}}\sqrt{N} \), which is dimensionless only if \( \Delta f_{\mathrm{CW}} \) is already a fraction, not a percentage point. But elsewhere the manuscript switches between “pp” and fractional units without always restating the conversion, so the equation is dimensionally safe only under an unstated unit convention.

[C2] **The \( \sigma_{\mathrm{from\,half}} \) naming is not fully consistent with the denominator actually used.** Section V says the exact \( p_0(1-p_0)/N \) denominator differs from the \(0.5/\sqrt{N}\) approximation by less than 0.01% in \( \sigma \), yet the paper then reuses the same symbol in contexts where the reference is not \(p_0=0.5\). That makes the notation internally unstable even if the numeric effect is tiny.

[C3] **The PEALPix/HEALPix threshold discussion has a units gap.** In Section VII A, the text converts \( \sigma_{\mathrm{v}} /(aH) \) into an approximate displacement scale and then estimates the fraction of cells near a class boundary from \( \sigma_{\mathrm{rsd}}/R_s \), but it never explicitly carries the units through the boundary-crossing criterion. The argument is plausible, but the dimensional chain is not written carefully enough for a load-bearing robustness claim.

[D1] **Internal cross-reference error in Section VIII F.** The text says “Table X” contains the per-class residuals after subtracting the P4 monopole, and then describes the unique-galaxy monopole result as “the same monopole shows up as −5.00σ,” but Table X only lists class residuals, not the sample-wide projection. The sample-wide number is therefore not actually recoverable from the cited table.

[D2] **Internal cross-reference error in Section VI A on the duplicate-row diagnosis.** The text cites “§VIII F documents the reconciliation,” but the actual reconciliation is introduced later in Section VIII F after the earlier statistical claims have already been made. This is a forward-reference problem: the manuscript relies on a later section to justify an earlier inference.

[E1] **Null-procedure comparability is still too loose in the results narrative.** The paper repeatedly juxtaposes raw \( \sigma \), monopole-subtracted \( \sigma_{\mathrm{vs\,monopole}} \), Bonferroni thresholds, and permutation \( p \)-values in the same paragraph, especially in Sections VI, VII, and VIII, even though these come from different null constructions. The text often says they are “not comparable” in a general sense, but not always in the same sentence where the values are juxtaposed.

[E2] **The abstract mixes different null families without a sentence-level disclaimer.** The abstract places the V-Web class \( \sigma \), the DESIVAST \( \Delta f_{\mathrm{CW}} \), and the label-shuffle \( p \)-values side by side as if they were commensurate evidence. Because those are different null procedures, every such juxtaposition needs an explicit “not directly comparable” qualifier to avoid overstating the evidentiary synthesis.

[F1] **Abstract sentence about “no evidence beyond the catalog-monopole offset” is only partially supported.** The body supports a *conditional* null, but Sections VI A and VI D explicitly show nontrivial bright/dark and class-boundary residual structures. So the abstract sentence is too clean relative to the body: the manuscript does not fully prove the unconditional phrasing used there.

[F2] **Abstract sentence about the DESIVAST primary result is supported, but only after multiple caveats omitted there.** The body does support the DESIVAST \( \Delta f_{\mathrm{CW}} \approx 0.0007 \) null, yet it also says the V-Web void sample is sample-size-limited and survey-edge contaminated, and that the DESIVAST test is the “primary” one by post hoc declaration. The abstract does not mention those caveats, so the claim is faithful but incomplete.

[G1] **Unsupported “cleanest” claim in Section VIII C.** The phrase “the cleanest single chirality-in-voids measurement in this paper” is asserted for the V2-REVOLVER catalog-native statistic, but the manuscript does not provide a quantitative ranking criterion over the other reported estimators. That is a novelty/superlative claim without a supporting comparison.

[G2] **Unsupported “closest currently available substitute” claim in Section IX C and X.** The ASTRA EDR overlap is described as “the closest currently available substitute for the full-DR1 environmental VAC,” but the paper gives no systematic comparison showing why ASTRA is the closest rather than merely another overlapping catalog. That wording should be softened unless a documented survey of alternatives is added.

[H1] **“Consistent with” hides a quantified mismatch in Section IX C.** The paper says the V-Web and T-Web volume fractions are “consistent” at the survey-shell systematic level, but the void fraction differs by +8–18 pp and the cluster fraction by 3–5 pp. That is a large discrepancy that deserves the actual numerical delta and uncertainty in the same sentence, not a qualitative hedge.

[H2] **“No significant tension” masks a non-negligible sign flip in Section VI A.** The body says the bright-specific and dark-specific filament deviations are opposite-signed and around \(2\sigma\), yet the interpretive language repeatedly compresses this to a residual that is “null” or “not significant.” The manuscript should state the magnitude and sign explicitly whenever it uses that hedge.

[I1] **Appendix A is a toy model, not a validated mapping, but the main text risks reading it as more than that.** The appendix itself clearly says the operator is schematic, not a derived EFT constraint, but Section XV references it as a “schematic toy mapping” without reiterating the limitation. That creates an appendix/main-text mismatch in emphasis, even though the technical caveat exists.

[J1] **A stale number persists in the manuscript’s self-description of the bright/dark split.** Section XI says “the bright/dark split agreed within ±0.001” was an earlier draft statement and corrects it to a \( \sim 2\sigma \) residual, but the broader narrative still occasionally summarizes the systematics as though the split is merely a small perturbation. This is a versioning inconsistency: the correction is present, but the prose tone elsewhere did not fully update.

[J2] **Another stale-number issue appears in the Tempel overlap discussion.** The manuscript first mentions a 110,586 overlap in an earlier draft, then corrects it to 96,753, but later prose still frames the Tempel test as if the overlap were large enough to support broad class-by-class concordance claims beyond the filament-like bin. The numeric correction is real, but the interpretive language still reads like it was written for the larger, outdated sample.

[N5] **The Appendix B reproducibility checklist is internally incomplete relative to the claims made in the main text.** The checklist lists a single config file and a deterministic seed, but the main body also depends on multiple output JSON/CSV artifacts, a grid pipeline, a Tempel cross-validation driver, and several selection-correction rebuilds. Because those are central to the paper’s quantitative claims, the appendix does not fully match the operational complexity actually used.

[N6] **The manuscript’s conclusions section is broader than the evidence on the page.** Section XV says the result is robust under six classes of systematics tests and under grid resolutions 128\(^3\)–384\(^3\), but the body explicitly excludes the \(R_s = 10\) phase-2 rows from the physical robustness claim and treats the selection-corrected rebuild as a stress test rather than an independent confirmation. The conclusion should distinguish *primary evidence* from *stress tests* more sharply.

