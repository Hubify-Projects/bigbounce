# P2 2026-06-04_R2pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 41.5s

---

Below is a citation-forensics referee report focused on the references, numerical claims, and internal consistency of the submitted text.

## P2-B1 — Abstract and main text repeatedly mix incompatible \(f_{\rm NL}\) conventions without a clean, stable translation
**Section/page:** Abstract, Secs. II, VI, X, App. A  
**Problem:** The paper alternates between claiming the “observational” matter-bounce value is \(f_{\rm NL}=-35/8\) and treating \(f_{\rm NL}=-35/16\) as a merely alternative convention, while also stating that the Li & Brandenberger value is a “single-time-ordering result” and that the Planck/Cai convention is the correct observational one. The text then repeatedly rescales significances by “halving” them when switching conventions, but the mapping is not kept cleanly separated from the scientific results.  
**Required fix:** Choose one convention as the primary reported quantity, define the conversion once, and propagate it consistently. Every quoted significance and Bayes factor must specify which \(f_{\rm NL}\) convention is used and whether the conversion has already been applied.

## P2-B2 — The claim that the paper “confirms” Cai et al.’s benchmark values is overstated and not actually demonstrated
**Section/page:** Sec. II A, Table I, Appendix A  
**Problem:** The paper says “We adopt the bispectrum shape function of Cai et al.  and confirm its published numerical values,” and Table I says “All values match the published results  exactly.” But the main text also states that the coefficients are underdetermined, multiple coefficient sets work, and the evaluated values depend on a chosen symmetrized basis. That is not a direct confirmation of the original derivation.  
**Required fix:** Rephrase as a numerical consistency check of benchmark values, not a confirmation of the full analytic derivation. State explicitly what was recomputed, with what conventions, and what was not independently derived.

## P2-B3 — The underdetermined coefficient/null-space discussion is internally inconsistent and needs mathematical repair
**Section/page:** Sec. II A  
**Problem:** The paper claims the constraint matrix has rank 3 and a 3D null space, but also says the three benchmark values and a “single-time-ordering polynomial of degree 9 in three variables symmetrized to six monomials” are exactly enough to fix the system. That cannot simultaneously support the later claim that the published benchmark values “uniquely” validate the physics, because the same text admits large coefficient ambiguity and \(r\)-scatter from that ambiguity.  
**Required fix:** Give a precise linear-algebra statement of what is determined and what is not. If the six-coefficient basis is redundant relative to the physical vertex-level expression, explain why the null space is physical, basis-induced, or an artifact of the chosen parametrization.

## P2-B4 — The paper repeatedly treats a non-unique polynomial fit as if it were a physical result
**Section/page:** Sec. II A, Sec. III B  
**Problem:** The manuscript states that a 10,000-sample null-space scan gives \(r=0.85\pm0.13\) and \(r_{\rm cos}>0.97\) for all samples, then uses that distribution as a systematic input to forecast significance. But the paper never demonstrates that the null-space sampling corresponds to physically allowed matter-bounce models rather than arbitrary coefficient deformations.  
**Required fix:** Justify the physical prior over coefficient space. If the scan is only a basis ambiguity, do not use it as a model uncertainty in detection forecasts unless you show that each sampled coefficient set is physically realizable.

## P2-B5 — The amplitude-recovery factor \(r\) is allowed to exceed 1, which breaks the paper’s own interpretation unless carefully qualified
**Section/page:** Sec. III B, footnote 2  
**Problem:** The text first says “\(r\) is bounded above near unity,” then later admits null-space directions give \(r\approx1.14\). This contradicts the interpretation of \(r\) as an amplitude recovery fraction.  
**Required fix:** Redefine \(r\) as a weighted projection coefficient that can exceed 1, or else enforce a physically meaningful normalization that guarantees \(0<r\le1\). The current interpretation is mathematically and conceptually inconsistent.

## P2-B6 — The use of \(r\) as both a shape overlap and a significance degrader is not sufficiently distinguished
**Section/page:** Secs. III B, IV, VII, IX  
**Problem:** The manuscript uses \(r\) sometimes as a Fisher-weighted template projection, sometimes as a signal recovery fraction, and sometimes as a direct multiplicative factor on \(\sigma(f_{\rm NL})\). These quantities are not identical without extra assumptions.  
**Required fix:** Define the estimator assumptions under which \(f_{\rm NL}^{\rm measured}=r\,f_{\rm NL}^{\rm true}\) is valid, and separate shape overlap, amplitude bias, and variance degradation.

## P2-B7 — The paper’s treatment of the Cai vs. Li & Brandenberger normalization is not reliably sourced
**Section/page:** Sec. II C, App. A, refs. ,   
**Problem:** The paper claims Cai & Brandenberger  gives \(-35/16\) and that the difference from Cai et al.  is “just” convention plus missing commutator doubling. The report text asserts the source-to-source audit found “all four individual vertex contributions agree … at the level of the \(k_i^3\) coefficients,” but no primary-source quotation or explicit derivation is provided in the body.  
**Required fix:** Provide a transparent side-by-side table showing the exact convention differences, the exact equations being compared, and which paper uses which normalization. If  now has a later/public version, cite the current canonical version and verify the title/authors/venue.

## P2-M1 — Reference  appears incomplete or likely stale as written
**Section/page:** refs. , App. A  
**Problem:** The bibliography gives “ Y.-F. Cai and R. Brandenberger, Non-Gaussianity in a matter bounce, Phys. Rev. D 90, 023534 (2014).” That is plausible, but the main text also discusses a “Cai & Brandenberger value” as if it were a distinct competing convention paper. The manuscript should verify that the cited paper is the correct one and that the arXiv/DOI metadata are correct.  
**Required fix:** Check and report the exact arXiv ID, DOI, article title, and whether the published PRD version matches the preprint and normalization used in the comparison.

## P2-B8 — The abstract overclaims what the paper proves versus what it forecasts
**Section/page:** Abstract  
**Problem:** The abstract states “We audit the Cai et al. bispectrum calculation, confirming that the intermediate \(\epsilon\)-order decomposition reproduces approximately half the full polynomial...” and then treats this as a confirmation of the “correct Planck-convention normalization.” This is not a proof of the observable normalization; it is at best a consistency check under the paper’s own assumptions and conventions.  
**Required fix:** Recast the abstract so it summarizes demonstrated calculations, not interpretive conclusions. Distinguish clearly between checked numerics, assumed conventions, and scientific inference.

## P2-B9 — The paper uses “\(\sigma\)” values from different null procedures on different scales without enough qualification
**Section/page:** Abstract, Secs. IV–VII, IX  
**Problem:** The paper compares bispectrum Fisher significances, scale-dependent-bias Fisher significances, GR-marginalized Bayesian comparisons, and joint \((f_{\rm NL},n_{f_{\rm NL}})\) Fisher outputs as if they are directly comparable. They are not all on the same statistical scale.  
**Required fix:** Explicitly label each \(\sigma\) as Fisher, posterior, or heuristic-equivalent significance, and do not juxtapose them as interchangeable discovery thresholds. This requires correction at the abstract level.

## P2-E1 — The abstract and conclusion quote many headline numbers that are not uniquely traceable to one calculation
**Section/page:** Abstract, Sec. X  
**Problem:** The abstract simultaneously reports 5.2–5.5\(\sigma\), 3–5\(\sigma\), 7.4–7.7\(\sigma\), 3–7\(\sigma\), BF \(\sim10\)–17, BF \(\sim4\), and a halved 1.5–2.5\(\sigma\) scenario. The reader cannot tell which are actual results, which are upper bounds, and which are sensitivity checks.  
**Required fix:** Reduce the number of headline metrics and assign each to a clearly labeled forecast scenario. State one primary result and move the rest to caveats.

## P2-M2 — The paper’s claimed observational timing for SPHEREx is dubious and may be outdated or internally inconsistent
**Section/page:** Abstract, Sec. IX, refs.   
**Problem:** The manuscript says SPHEREx was “launched March 2025,” with collection through \(\sim2027\) and first public data around 2028. These timing claims need verification against the current mission status and may have shifted.  
**Required fix:** Verify the mission status from the current NASA/mission documentation and update all timeline statements accordingly.

## P2-M3 — Reference  is a 2014 arXiv forecast paper; the manuscript treats it as foundational but does not distinguish forecast lineage from mission status
**Section/page:** Sec. IV, refs. ,   
**Problem:** The paper cites  as “the foundational SPHEREx galaxy-survey forecast paper” and  as a companion forecast. That may be fine, but the manuscript mixes these older forecasting papers with claims about current instrument capability without clearly separating them.  
**Required fix:** Distinguish mission design documents, forecast papers, and final survey specifications. Verify titles/authors/venues and whether the cited forecast assumptions still match the current SPHEREx concept.

## P2-E2 — The claimed “factor-of-two” derivation in Appendix A is not sufficient to settle the observability question
**Section/page:** Appendix A  
**Problem:** Appendix A correctly argues that a commutator produces a factor of \(-2\,\mathrm{Im}\), but the paper then uses this to conclude that the Cai convention is “physically correct” in the Planck observational framework. That conclusion is stronger than what the appendix establishes.  
**Required fix:** Limit the conclusion to normalization consistency under the paper’s chosen \(f_{\rm NL}\) convention. Do not claim the commutator identity settles a convention dispute unless you also trace the exact observable definition used in the comparison literature.

## P2-B10 — The paper states that the “local-template estimator recovers only a fraction \(r\)” but then calls the mismatch “intrinsic” and “cannot be removed by survey design”; this is overstated
**Section/page:** Sec. III B  
**Problem:** Template mismatch is partly a property of the signal-template pair, but estimator choice, weighting, and inclusion of additional shape degrees of freedom can change the recovered significance. The manuscript’s categorical statement is too strong.  
**Required fix:** Replace “cannot be removed by survey design” with a qualified statement about the specific local-template estimator and the current forecast framework.

## P2-M4 — The use of “CMB Fisher weighting” for a CMB-derived constraint needs a reference to an actual estimator setup
**Section/page:** Sec. VIII A  
**Problem:** The paper recasts Planck \(f_{\rm NL}^{\rm local}=-0.1\pm5.0\) into a bounce value using \(r=0.876\), but it is not clear that the overlap factor derived for the bounce-vs-local comparison is applicable to the exact Planck estimator family used in /.  
**Required fix:** Show the estimator correspondence explicitly. If the overlap is only approximate, say so and do not present the recast as exact.

## P2-M5 — Several references in the bibliography need metadata verification for title, venue, and year
**Section/page:** refs. [4], , , , , , ,   
**Problem:** The bibliography mixes journal articles, arXiv preprints, and possibly future-dated items. Some entries use incomplete venue formatting or likely wrong publication status. Examples needing verification include  (2025 arXiv only),  (arXiv-only but lacking clear title formatting), and  (2025 A&A article for Planck PR4/NPIPE NG constraints, which must be checked carefully).  
**Required fix:** Audit every reference against arXiv/NASA ADS and correct titles, author lists, venues, years, article numbers, and arXiv IDs.

## P2-B11 — The paper’s own internal version-history artifacts appear in the body prose and should be removed
**Section/page:** Abstract, Sec. VI, Table II caption, App. A  
**Problem:** The manuscript contains phrases like “v1.7.43,” “corrected v1.7.35 R-next-c-MAJ-1,” “R42 reviewer,” “sanity row,” “post-arXiv TODO,” “framework-specific priors,” and “companion artifact.” These are review-log or internal revision artifacts, not publication prose.  
**Required fix:** Remove all version-history language, internal ticket labels, and audit tags from the body text and captions.

## P2-B12 — Duplicate-phrase style issues appear in the prose and should be edited
**Section/page:** multiple  
**Problem:** The text contains repeated or near-duplicated constructions such as “multi-tracer multi-tracer” style repetitions in spirit, repeated restatements of the same headline numbers, and a few overlong parenthetical insertions that read like duplicated notes rather than polished prose.  
**Required fix:** Perform a line edit to remove repeated phrasing and collapse duplicate explanatory clauses.

## P2-M6 — The page count is high for the actual contribution
**Section/page:** whole paper  
**Problem:** The paper is 23 pages, but much of it is devoted to re-litigating convention choices, internal numerical recalibrations, and repeated sensitivity summaries. The core scientific contribution appears to be a template-overlap/forecast recast that could be presented more compactly.  
**Required fix:** Reduce to roughly 15–18 pages of main text for a methods/catalog-style PRD submission, with the convention audit and Bayesian sensitivity details pushed to appendices or supplementary material.

## P2-E3 — The paper’s Bayesian model-comparison numbers are not reproducible as written
**Section/page:** Sec. VI, Table II, Table III  
**Problem:** The manuscript reports BF \(\sim 10\)–17 and BF \(\sim 4\)–7 across multiple prior choices, but it never provides enough explicit likelihood/prior normalization detail to reproduce those exact values from the text alone. The “three ensembles” and “framework-specific priors” language does not substitute for a complete specification.  
**Required fix:** Provide the exact analytic likelihood, prior definitions, and parameter values for each Bayes-factor entry. If the numbers are from a companion artifact, do not present them as fully validated paper results yet.

## P2-M7 — The paper conflates forecast significance with post-hoc consistency checks
**Section/page:** Secs. IV, VIII, IX  
**Problem:** The text repeatedly uses current constraints (Planck) to validate the bounce prediction and then uses that validation to justify future forecast significance. That is not logically equivalent to forecasting power.  
**Required fix:** Separate validation against existing data from forecast performance against future survey sensitivity.

## P2-M8 — Reference  and the quoted Planck PR4 constraint need direct verification
**Section/page:** Sec. VIII A, refs.   
**Problem:** The paper quotes Planck PR4/NPIPE \(f_{\rm NL}^{\rm local}=-0.1\pm5.0\). This needs source verification against the actual paper abstract/table.  
**Required fix:** Confirm that  really reports the quoted value and that the title, authors, and venue are correct. If not, fix the citation and the number.

## P2-M9 — The current data section overstates the strength of the Planck test
**Section/page:** Sec. VIII A, Conclusion  
**Problem:** The manuscript says current data “cannot discriminate between the bounce and inflation,” which is plausible, but then uses the Planck recast to claim strong consistency with the bounce prediction. Consistency is not discrimination.  
**Required fix:** State only that current data are consistent with the prediction within uncertainties. Do not suggest the data meaningfully validate the bounce.

## P2-M10 — The use of “physical-frame local detection would disfavor single-field slow-roll attractor” is true only within the stated approximation regime, which the paper does not enforce tightly enough
**Section/page:** Abstract, Sec. IX E  
**Problem:** The conformal-Fermi squeezed-limit statement is qualified by gradient, projection, and finite-squeezed corrections, but the abstract and conclusion make it sound like a direct observable discrimination.  
**Required fix:** Restrict the claim to a theoretical statement about the squeezed limit, not an observational one, and keep it separate from the survey forecast.

## P2-M11 — The paper’s quoted \(n_s\)-\(f_{\rm NL}\) relation should not be presented as an exact observational discriminator without error propagation
**Section/page:** Sec. VIII B  
**Problem:** The relation \(f_{\rm NL}(n_s)\approx-35/8-c'(n_s-1)\) is presented as a testable curve, but the manuscript does not propagate the full uncertainty in \(n_s\), \(\kappa_1\), and the bounce-specific corrections coherently.  
**Required fix:** Add an explicit uncertainty band or refrain from treating the relation as a sharp discriminator.

## P2-M12 — The manuscript uses several speculative or nonstandard claims without citation support
**Section/page:** multiple  
**Problem:** Examples include “SPHEREx launched March 2025,” “MegaMapper could reach \(\sigma(f_{\rm NL})\approx0.5\) ideally,” “anomaly-selected tracers improve constraints by 10–20%,” and “a Planck-scale ALP predicts \(\beta\approx0.27^\circ\).” Some may be defensible, but several are either uncited or tangential to the paper’s core claim.  
**Required fix:** Either remove these side claims or provide direct citations and make clear they are peripheral, not central to the paper.

## P2-E4 — The paper needs a complete arXiv/NASA ADS metadata audit of every cited paper
**Section/page:** refs. [1]–  
**Problem:** The submission explicitly asks for citation forensics, and the text contains many places where title/authorship/venue/year/arXiv ID must be checked, especially for [4], , , , , , , –. The current bibliography is not sufficiently clean for publication-level trust.  
**Required fix:** Verify every citation against arXiv and ADS. Correct any fused metadata, outdated preprint references, missing journal article numbers, and any “arXiv preprint” entries that now have published versions.

## P2-M13 — The paper’s length is inflated by repeated re-statements of the same central point
**Section/page:** Abstract, Secs. II, VI, VII, IX, X  
**Problem:** The same quantitative claims are repeated multiple times in slightly different wording. This makes the paper harder to audit and obscures which numbers are primary.  
**Required fix:** Deduplicate repeated prose and keep one canonical statement of each key result.

## P2-B13 — The paper should not describe internal scripts and file names in the main text
**Section/page:** Abstract, Sec. VI, Data and Code Availability  
**Problem:** The text names files like “04b fast ensemble.py,” “03b fast mock validation.py,” and “02 compute gr aware bayes update.py.” This is not publication prose and looks like a project notebook dump.  
**Required fix:** Remove script names from the main text. If code provenance matters, put it in a separate reproducibility note.

## P2-M14 — The claim that the paper is “validated across three independent ensembles” is insufficiently defined
**Section/page:** Sec. VI  
**Problem:** The three ensembles are described in confusing, overlapping ways, and it is unclear whether they are independent draws from distinct likelihoods or just repackaged analyses of the same result.  
**Required fix:** Define the three ensembles mathematically, specify what differs between them, and show why they validate the Bayes-factor calculation rather than merely restating it.

## P2-N1 — Minor typography and notation cleanup is needed
**Section/page:** multiple  
**Problem:** There are several spacing and notation inconsistencies in citations, hyphenation, and variables.  
**Required fix:** Standardize notation throughout, especially \(f_{\rm NL}\), \(n_{f_{\rm NL}}\), \(b_\phi\), and \(r_{\rm cos}\).

## Summary recommendation
**REJECT**

The paper in its current form is not publication-ready because the central result depends on unstable convention handling, non-unique polynomial reconstruction, and a large number of internally inconsistent or insufficiently justified forecast claims. The citation audit also shows that the bibliography and quoted literature results need a full metadata and claim-by-claim verification before the work can be trusted. The manuscript would require major structural simplification, a clean convention framework, and a complete reference audit before reconsideration.