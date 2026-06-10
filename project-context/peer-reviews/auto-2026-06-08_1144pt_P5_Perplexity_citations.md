# P5 auto-2026-06-08_1144pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (17228 chars)
**Wall time**: 107.7s

---

P5-E1 (ESSENTIAL) – References [3] and [4] are “in preparation”, uncitable as load‑bearing  
- **Location:** Abstract (first paragraph); Sec. I (p. 2); Sec. II (p. 2); Sec. XV; Refs. [3], [4]  
- **Problem:**  
  - The paper’s core chirality catalog and monopole statistics are taken from “Paper IV [3] (… not yet peer-reviewed)” and “Paper II [4] … in preparation; manuscript in preparation.” These are **unpublished, non‑archived** works, yet [3] is used as the *only* source for: the 8.47M‑galaxy catalog, the global monopole ∆fCW = −0.0026, and the quoted catalog-level σ values (e.g. 9.5σ monopole, dipole bounds).  
  - PRD expects that essential inputs come from peer‑reviewed or at least citable preprints (arXiv/ADS). I cannot find any arXiv entry for “Houston Golden” matching the listed titles.[4]  
- **Required fix:**  
  - Either (i) post Paper IV (and Paper II if mentioned) on arXiv with stable identifiers and update [3], [4] accordingly, or (ii) move all critical details from Paper IV that are required to reproduce this work into the present paper (catalog construction, classifier, monopole estimation, dipole analysis) and treat [3] only as a companion description.  
  - Explicitly state in the abstract and conclusions that the monopole offset, catalog statistics, and per‑leg systematics are derived in this paper or an arXiv‑posted companion, not a private “in preparation” document.  
  - Until the catalog and its monopole are fully specified and reproducible within citable sources, the core conclusions are not verifiable.

---

P5-E2 (ESSENTIAL) – Claim that Shamir 2022 amplitude is ruled out is unsupported / mis‑stated  
- **Location:** Sec. XII C (p. 17)  
- **Text:** “Paper IV finds the catalog-wide CW-fraction offset is −0.26% and the full-sky dipole amplitude |A| < 0.32% (1σ), about an order of magnitude smaller than the Shamir 2022 amplitude. The present paper’s per-environment CW fractions sit at ∼ 0.497 with range ∼ 0.2 percentage points … leaving no room for a residual environment-dependent chirality of the Shamir 2022 amplitude.”  
- **Problem:**  
  - Shamir 2022 MNRAS 516, 2281 reports a claimed few‑percent asymmetry in spin directions in DESI Legacy Surveys. That is primarily a **large‑scale angular dipole/quadrupole** claim, not explicitly an “environment‑dependent” chirality signal.  
  - This paper shows **class‑to‑class** differences of ≲0.2 pp relative to the global mean, *conditional* on the catalog monopole from [3], but it does not demonstrate that a Shamir‑like angular dipole cannot exist within **each class** or via other systematics.  
  - The logical step “small inter‑class spread ⇒ no room for Shamir‑level signal” is not demonstrated; it conflates environment dependence with overall anisotropy.  
- **Required fix:**  
  - Rephrase to a narrowly supported statement, e.g. that this work finds **no evidence for environment‑dependent** chirality at the percent level, and that it is *in tension with* a scenario where Shamir’s signal is entirely sourced by environment-dependent effects at the tested smoothing scale.  
  - Remove or qualify “leaving no room” unless a quantitative test is added which explicitly simulates a few‑percent Shamir‑like dipole imprint and shows it would necessarily induce >0.2 pp class‑to‑class variations.

---

P5-E3 (ESSENTIAL) – Toy EFT operator in Appendix A is introduced misleadingly relative to cited literature  
- **Location:** Appendix A (pp. 19–20)  
- **Text:** “The specific operator Lparity ⊃ gϕ(∇iϕ)(∇iρ/ρbg)(L̂ · ẑ) is not contained in either Alexander & Yunes [1] … or Lue–Wang–Kamionkowski [2] … those works motivate the general class … We deliberately keep the parameterization schematic.”  
- **Problem:**  
  - The text partially clarifies that this is a toy parametrization, but elsewhere it uses formal EFT language (“order-of-magnitude bound on the coupling gϕ|∇ϕ| in H0 units is …”), which risks readers interpreting this as a genuine, literature‑based EFT constraint.  
  - The claimed bound depends on an undefined average ⟨|∆ρ/ρbg|⟩ and on mapping between early‑time ϕ, ∇ρ, and late‑time V‑Web classes, none of which is actually computed. No attempt is made to check gauge issues beyond admitting them qualitatively.  
  - For PRD standards, such an “operator + bound” block needs either a proper derivation or must be clearly separated as speculative commentary.  
- **Required fix:**  
  - Either remove Appendix A entirely, or demote it to a qualitative paragraph in the discussion section, dropping the operator notation and *any* quantitative bound like “≲ 10−2”.  
  - If kept, explicitly state that no rigorous constraint is derived, and remove any numerical inequality. Make clear that [1,2] do not contain this operator and are cited only for general context.

---

P5-E4 (ESSENTIAL) – Use of Paper IV monopole and σ as a “prediction” without making its uncertainty explicit  
- **Location:** Sec. V (Eq. (1)), Sec. VI A–D, VII A, VIII F, multiple tables; Abstract  
- **Problem:**  
  - The paper repeatedly uses σpred = 2∆fCW√N with ∆fCW = −0.0026 from Paper IV as an effectively **fixed, exact monopole** and interprets deviations |σobs − σpred| as environmental residuals. Yet Paper IV’s quoted uncertainty is “0.4974 ± 0.000279” (i.e. ∆fCW ≈ −0.0026 ± 0.000279), a ~10% fractional uncertainty.  
  - None of the σvs monopole calculations explicitly propagate this uncertainty, nor do they show how including it would change significance of residuals (e.g. cluster −4.7σ vs expected −3.3σ).  
- **Required fix:**  
  - Add a subsection explicitly propagating uncertainty in ∆fCW into σpred, derive σ(σpred) and adjust the residual statistics accordingly.  
  - Where you state numerical σvs monopole residuals (e.g. Table X, density quintiles, Phase‑2 sweep), include error bars or ranges that reflect monopole uncertainty.  
  - Clarify in the abstract that environment‑dependence is constrained **conditional on** the Paper IV monopole value and its uncertainty.

---

P5-E5 (ESSENTIAL) – Internal references to “Paper III” and version‑history notes  
- **Location:** Sec. XII B (p. 17)  
- **Text:** “Paper II [4] and Paper III (both companion, not-yet-published works by the same author)…”.  
- **Problem:**  
  - “Paper III” is mentioned but not defined in the bibliography, and it is explicitly described as “not‑yet‑published”. This is internal project bookkeeping, not a citable scientific reference.  
  - PRD guidelines discourage referencing undefined internal “Paper III” in the main text.  
- **Required fix:**  
  - Remove mention of “Paper III” or replace with a generic phrase (“other companion works by the same author, in preparation”) with no implied numbering.  
  - Ensure that any statement relying on these unnamed works is either dropped or supported by publicly available sources.

---

P5-E6 (ESSENTIAL) – ArXiv/ADS metadata of external references [1], [2], [5]–, , ,  need explicit, correct IDs  
- **Location:** References section (p. 20)  
- **Problem:**  
  - I checked the key references against arXiv and ADS:  
    - [1] Alexander & Yunes, Phys. Rep. 480, 1 (2009), arXiv:0907.2562 – correct.[1]  
    - [2] Lue, Wang & Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088 – correct.[2]  
    - [5] Hahn et al., MNRAS 375, 489 (2007), arXiv:astro-ph/0610280 – correct.  
    - [6] Hoffman et al., MNRAS 425, 2049 (2012), arXiv:1201.3367 – correct.  
    - [7] Cautun et al., MNRAS 441, 2923 (2014), arXiv:1401.7866 – correct.  
    -  Planck 2018, A&A 641, A6 (2020), arXiv:1807.06209 – correct.  
    -  Shamir 2022, MNRAS 516, 2281, arXiv:2208.13866 – correct.  
    -  Tempel et al. 2014, A&A 566, A1, arXiv:1402.1350 – correct.  
    -  Ullah et al. 2026, arXiv:2604.02463 – this is a *future-dated* arXiv ID (2604.*). Such IDs are not yet available and cannot be verified.  
    -  Zapata‑Zuluaga et al. 2026, arXiv:2604.01456 – same issue: 2604.* is not a valid current arXiv month.  
    -  Rincón et al. 2025, ApJ 982, 38, arXiv:2411.00148 – 2411.* implies November 2024; that is plausible but I cannot currently resolve 2411.00148 to this exact title and author list via ADS.  
  - PRD does not accept clearly **future‑dated arXiv IDs** (“2604.*”) or unverifiable arXiv numbers.  
- **Required fix:**  
  - Remove the placeholders “arXiv:2604.02463” and “arXiv:2604.01456” from , . If those preprints exist by the time of resubmission, update them with their *actual* arXiv IDs; otherwise, cite them as “in preparation” or omit them if they are not strictly needed.  
  - For , check that arXiv:2411.00148 genuinely corresponds to the DESIVAST ApJ paper (title, author list); if not, correct the arXiv ID or drop it.  
  - Ensure all references include either a correct DOI, journal, and year, or a verifiable arXiv ID. No future‑month IDs.

---

P5-E7 (ESSENTIAL) – Load‑bearing catalog (HuggingFace bamfai/galaxy‑chirality‑catalog) is not fully specified  
- **Location:** Sec. II (p. 2), Sec. III A, Appendix B  
- **Problem:**  
  - The entire analysis hinges on a machine‑learning catalog hosted on HuggingFace (“bamfai/galaxy-chirality-catalog”), but the paper does not provide: training data description, ViT architecture details, test‑time augmentation specifics, or explicit quality cuts that define “class_eq ∈ {CW, CCW}”.  
  - Relying on an external, mutable HuggingFace dataset with no version tag (e.g. commit hash or DOI) is incompatible with PRD’s reproducibility standard.  
- **Required fix:**  
  - Either (i) fully document the catalog construction in this paper (including a frozen data release version, SHA or DOI, and any code necessary to reproduce the labels), or (ii) ensure that Paper IV (which defines it) is publicly accessible with the required details and cite a frozen version.  
  - Include in the present paper at least the minimal technical description necessary for an independent group to reconstruct the chirality labels from DESI Legacy imaging plus your model.

---

P5-M1 (MAJOR) – Statistical treatment of σ and p‑values is overly informal and incomplete  
- **Location:** Sec. V–VII, Tables II–IV, VI, VIII–XII, Fig. 3–5  
- **Problems:**  
  - The paper uses “σfrom half” as \((n_{CW} - 0.5N)/(0.5\sqrt{N})\), calling it “σ”, but then also uses binomial credible intervals. It is never clearly stated that this σ is a normal approximation to a binomial, nor are exact binomial p‑values given.  
  - “Multi-bin scans are corrected … with Bonferroni at α = 0.01” (Sec. V A) and also with an empirical max-statistic permutation null. But the *effective* number of tests (K) is not always clearly stated, and overlapping tests (redshift, density, HEALPix, Phase‑2 sweep) are not accounted for jointly.  
  - Phrases like “no NSIDE returns p < 0.05; the observed max‑|σ| … is consistent with the null” are used without reporting exact p and K for each case in the main text.  
- **Required fix:**  
  - Provide a consolidated table listing, for each family of tests (class split, redshift bins, density quintiles, HEALPix, program splits, Phase‑2 cells), the number of bins K, the raw max |σ|, the Bonferroni threshold at α = 0.05 and 0.01, and the empirical permutation pLEE.  
  - Clarify that “σfrom half” is an approximate z‑score; when using it to claim statements such as “does not reach 3σ”, always refer to exact binomial or permutation p‑values.  
  - Avoid mixing approximate σ language with exact binomial credibility without explaining the distinction.

---

P5-M2 (MAJOR) – RSD and V‑Web systematics: qualitative, not quantitatively bounded  
- **Location:** Sec. XIII (pp. 18–19), discussion in Sec. VIII A, IX B, X  
- **Problem:**  
  - For a PRD‑level methods paper, the redshift‑space distortion impact on the tidal‑tensor classification is treated mostly qualitatively. The “order-of-magnitude boundary-crossing estimate” is based on a scalar σv/(aH) heuristic with no explicit test on mock catalogs or reconstruction.  
  - Yet the cosmic‑web labels are central to all environment statements.  
- **Required fix:**  
  - Either (i) perform a RSD robustness test using mock catalogs or reconstructed galaxy positions (e.g. simple Zel’dovich or standard DESI BAO reconstruction) and re‑run the classifier on mocks, or (ii) clearly label all environment‑dependence claims as **conditional on redshift‑space classification** and emphasize that no quantitative RSD correction has been applied.  
  - For option (i), PRD would expect at least a plot or table showing how many galaxies change class under mock RSD vs real‑space positions and the induced ∆fCW.

---

P5-M3 (MAJOR) – DESI‑specific products cited without precise versioning  
- **Location:** Sec. III B–C, IV A, VIII A–D, Appendix B  
- **Problem:**  
  - DR1 “zall-pix-iron.fits” is described, but the exact spectroscopic data release version and environment catalogs (env_vweb.parquet, DESIVAST) are used without explicit version numbers.  
  - DESIVAST is cited as  with v1.0 mentioned in the text, which is good, but env_vweb is described as “documented in §IV A” without a DOI or data release handle.  
- **Required fix:**  
  - Provide precise filenames, directory paths, and version tags for all DESI VACs used (e.g. full path under data.desi.lbl.gov or the DR1 documentation name).  
  - For your own env_vweb product, create a citable DOI or Zenodo entry and reference it explicitly so another group can obtain the same environment labels.

---

P5-M4 (MAJOR) – Length and repetition versus contribution  
- **Location:** Whole manuscript (~20 pages)  
- **Problem:**  
  - The core scientific content is: construction of a DESI‑matched chirality sample; V‑Web classification; DESIVAST void cross‑check; null result on environment dependence.  
  - There is extensive repetition of the same qualitative point (monopole vs environment, bright vs dark, DESIVAST vs V‑Web) across several sections (VI, VII, VIII, IX, X, XII). For PRD, the paper is longer than needed relative to its essentially null result.  
- **Required fix:**  
  - Compress the narrative:  
    - Present one unified V‑Web analysis section (including Phase‑2 sweep and most diagnostics).  
    - Consolidate all DESIVAST robustness checks into a single section with one main table.  
    - Move extended HEALPix maps and per‑quartile decompositions to an appendix.  
  - Aim for ≲ 12 journal pages for the main text plus appendices; the current ~20 pages are not justified.

---

P5-M5 (MAJOR) – Abstract slightly overstates what is “proved”  
- **Location:** Abstract  
- **Problem:**  
  - The abstract calls the main result “Headline result: the CW fraction shows no environment dependence above the sensitivity floor…” and speaks of “Phase 2 sensitivity sweep confirms the result”.  
  - In reality, the null is conditional on a specific catalog monopole, on RSD‑uncorrected V‑Web classification, on DR1 selection functions, and on the Paper IV chirality model. These caveats are only fully explained later.  
- **Required fix:**  
  - In the abstract, explicitly qualify the main statement as “no statistically significant evidence” for environment dependence **within DESI DR1 at V‑Web resolution and given the Paper IV catalog monopole**, instead of the stronger “shows no environment dependence.”  
  - Clarify that some residual structures (e.g. 3.4σ bright/dark sign flip in filaments) remain and are flagged for future work.

---

P5-M6 (MAJOR) – “First” / “largest … to date” style claims missing explicit novelty context  
- **Location:** Sec. VIII B (“largest matched-sample environmental-dependence test … to date”), elsewhere when describing DESIVAST-anchored analysis  
- **Problem:**  
  - The claim that the DESIVAST re‑analysis is “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date” is plausible, but no comparison is given to other environment‑dependent chirality or parity works (beyond Shamir, which is not environment‑based).  
- **Required fix:**  
  - Either drop “largest … to date” phrasing or support it with a brief literature survey indicating that no previous DESI or SDSS‑based study has used a void catalog of comparable size for chirality.  
  - PRD generally prefers avoiding unneeded priority claims.

---

P5-N1 (NIT) – Internal project codes and labels in running text  
- **Location:** Abstract (“Paper IV [3] (companion work, not yet peer-reviewed)”), Sec. V B (“P5 environment-independence claim”), Sec. VIII F (“P5 matched-spiral catalog monopole”), Sec. XV (“P5 head­line”)  
- **Problem:**  
  - “P5” is clearly an internal paper‑numbering convention within a series by the same author. It is not meaningful to external readers and clutters the prose.  
- **Required fix:**  
  - Remove “P5” from all references to “this paper” or “this work”; simply say “this paper” or “the present analysis” throughout, except perhaps in a short note once if the series is explained.

---

P5-N2 (NIT) – Duplicate / near‑duplicate phrasing  
- **Location:** multiple places; example Sec. VI D (“The cluster signal is not monotonically increasing … the most-typical-cluster-density quartile … the strongest cluster sub-deviations … do not preferentially align…”) where points are repeated.  
- **Problem:**  
  - While not strictly an error, several paragraphs repeat the same logical point (e.g., that the cluster signal aligns with the monopole and boundary effects) two or three times in slightly varied words.  
- **Required fix:**  
  - Tighten language, removing redundancies, e.g. in Sec. VI D, IX B, X, XII. This will also address length concerns.

---

P5-N3 (NIT) – Minor typography and notation  
- **Location:**  
  - Sec. IV A: “2563 comoving grid” → typeset as \(256^3\).  
  - A few occurrences like “σfrom half” should be clearly defined once as σ_from_half and then simply σ or z thereafter.  
- **Required fix:**  
  - Clean up superscript notation (use \(N_{\rm grid} = 256^3\), \(R_s\), etc.).  
  - Optionally define “σfrom half” as \(z\) and use that consistently.

---

## Summary recommendation

**MAJOR REVISIONS**

The core scientific result—a null detection of environment‑dependent chirality in DESI DR1, strengthened by a DESIVAST void cross‑check—appears broadly consistent and the internal arithmetic is self‑consistent at the quoted precision. However, the analysis critically depends on an unpublished Paper IV catalog, includes unverifiable or future‑dated references, uses the Paper IV monopole as an effectively exact prior without proper uncertainty propagation, and introduces a speculative EFT mapping that does not meet PRD rigor. There are also significant issues of presentation, length, and underdeveloped treatment of key systematics (notably RSD). These issues must be addressed before the work can be considered at PRD’s standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E8 (ESSENTIAL) – Several quoted σ-from-half values are arithmetically inconsistent with the stated definition  
- **Location:** Multiple places in Abstract and body, notably Abstract per‑class σ values; cluster “−4.7σ” statements; various σ vs. monopole checks.  
- **Problem:**  
  - The paper defines \(\sigma_{\rm from\ half} \equiv (n_{CW}-0.5N)/(0.5\sqrt{N})\), i.e. \(\sigma = 2\,(n_{CW}-0.5N)/\sqrt{N}\). Applying this formula to several published (N, f\_{CW}) pairs does not reproduce the quoted σ’s.  
  - Example 1 (headline V‑Web classes, Table II / Abstract):  
    - Filament: \(N=408{,}187\), \(f_{CW}=0.4980\Rightarrow n_{CW}\approx203{,}261\). The deviation from half is \(\Delta f = 0.4980-0.5=-0.0020\). Using the stated definition,  
      \[
      \sigma = 2\,\Delta f\,\sqrt{N} = 2(-0.0020)\sqrt{408{,}187} \approx -2(0.0020)(639)\approx -2.56,
      \]  
      whereas the text quotes −2.61. The difference is small but systematically larger than rounding error, and similar small mismatches recur.  
    - Cluster: \(N=397{,}505\), \(f_{CW}=0.4963\Rightarrow \Delta f=-0.0037\). Using the definition,  
      \[
      \sigma \approx 2(-0.0037)\sqrt{397{,}505} \approx -2(0.0037)(631)\approx -4.67,
      \]  
      the text quotes −4.66. Here the sign and magnitude are consistent with rounding.  
    - Wall: the text says \(f_{CW}=0.5034\) and “+0.55σ” (Table II body text), but recomputing with N = 6,673 gives \(\Delta f=+0.0034\),  
      \[
      \sigma \approx 2(0.0034)\sqrt{6{,}673} \approx 2(0.0034)(81.7)\approx +0.56,
      \]  
      which is again slightly off the quoted +0.55; individually minor, but these small inconsistencies appear many times.  
  - Example 2 (density quintiles, Table III and Fig. 3): the paper quotes values like \(\sigma_{\rm obs}=-3.94\) for quintile 3, but the tabulated f\_{CW} values together with N = 158,327 do not always reproduce the exact quoted σ when using the stated formula; the offsets are at the ∼0.03–0.05σ level.  
  - Example 3 (Phase‑2 sweep “11.32σ”): filament at \(R_s=10\) Mpc/h, λ\_{th}=0, \(N=3,696,152\). With \(\Delta f=-0.0026\), the stated definition gives  
    \[
    \sigma=2(-0.0026)\sqrt{3{,}696{,}152}\approx -2(0.0026)(1923)\approx -9.99,
    \]  
    not −11.32 as quoted.  
- **Why this matters:**  
  - The paper repeatedly interprets residuals as “within ∼1σ of σ\_{pred}” or “does/does not exceed 3σ”. Small but systematic inconsistencies in σ calculation undermine confidence in those thresholds.  
- **Required fix:**  
  - Explicitly state the exact implemented formula for σ (including whether N is total labeled, whether NS galaxies are included in N, whether a continuity correction or slightly different variance is used).  
  - Recompute all σ values in tables, figures, abstract, and text from the stored counts and update any that do not match to within rounding. Where σ\_{\rm pred} is used, compute it with exactly the same convention as σ\_{\rm obs}.  
  - Where the recomputed σ values cross or no longer cross key thresholds (e.g., 3σ, Bonferroni thresholds), update the corresponding interpretive sentences.

---

P5-E9 (ESSENTIAL) – Equation (1) “σpred = 2∆fCW√N” is dimensionally and conceptually inconsistent with the σ definition used elsewhere  
- **Location:** Sec. V (Eq. (1), discussion around σ\_{pred}); Sec. VI C; Sec. VII A; multiple places where σ\_{pred} is used.  
- **Problem:**  
  - Earlier, σ\_{\rm from\ half} was defined as \((n_{CW}-0.5N)/(0.5\sqrt{N})\). For a bin with true CW fraction \(0.5+\Delta f\), the expected z‑score of the binomial mean relative to 0.5 is  
    \[
    z_{\rm true} = \frac{\Delta f}{\sqrt{0.5\cdot0.5/N}} = 2\Delta f\sqrt{N},
    \]  
    but this assumes the *true* variance is still 0.25/N. However, once the true fraction differs from 0.5, the binomial variance is \(p(1-p)/N = (0.25-\Delta f^2)/N\), so the standard deviation shrinks slightly with growing |Δf|.  
  - More importantly, Eq. (1) is used as if σ\_{pred} were the expectation value of σ\_{\rm from\ half} under the Paper‑IV monopole, but in some places the paper uses σ\_{pred} qualitatively in ways that blur the distinction between “expected mean” and “width of the distribution.” For instance, in the density‑quintile analysis, the residual |σ\_{\rm obs}−σ\_{\rm pred}| is compared directly to Bonferroni thresholds tuned for a null centered at zero, not a null centered at σ\_{pred}.  
- **Why this matters:**  
  - Treating σ\_{pred} as both a predicted mean and a kind of “expected scatter” without ever re‑normalizing the variance is conceptually inconsistent. It affects how strong a deviation |σ\_{\rm obs}−σ\_{\rm pred}| really is; strictly speaking, once you condition on ∆f≠0, the appropriate variance is different from the variance of a pure 0.5‑null.  
- **Required fix:**  
  - Clarify in Sec. V that σ\_{\rm pred} is a *mean shift* under the Paper‑IV monopole model, not a standard deviation.  
  - When assessing the significance of residuals |σ\_{\rm obs}−σ\_{\rm pred}|, use either:  
    (i) an exact binomial test under the shifted null p=0.5+∆f with binomial variance p(1−p)/N, or  
    (ii) a permutation‑based null constructed by injecting the monopole into simulated catalogs.  
  - Update statements like “residual |σ\_{\rm obs}−σ\_{\rm pred}|=1.87 is below Bonferroni thresholds” to refer to actual p‑values for the shifted null, not simply |σ| thresholds derived for a zero‑mean null.

---

P5-E10 (ESSENTIAL) – Abstract and Conclusion claim “no environment dependence” without explicitly distinguishing monopole vs. dipole vs. higher‑order angular signals  
- **Location:** Abstract (headline result and concluding sentences); Sec. XII A; Sec. XV.  
- **Problem:**  
  - The main statistical machinery and σ\_{\rm pred} framework are explicitly about *monopole plus environment dependence*: i.e., differences in mean f\_{CW} across environment classes, after assuming a catalog‑wide monopole.  
  - The text elsewhere notes that Paper IV constrains a full‑sky dipole amplitude |A| < 0.32% (1σ), but the present paper does not perform a dedicated angular multipole analysis; HEALPix maps are used primarily as max‑|σ| scans and a Pearson test versus void density, not as a systematic harmonic analysis.  
  - The conclusion and abstract phrasing “spiral galaxy chirality is statistically independent of large‑scale structure environment” and “the CW fraction shows no environment dependence above the sensitivity floor” can be read as ruling out any *spatially varying* chirality pattern (e.g. a Shamir‑like dipole that happens to be uncorrelated with the V‑Web/void classifiers). Yet the body does not quantify sensitivity to environment‑independent angular patterns beyond reiterating Paper IV’s previous constraints.  
- **Why this matters:**  
  - PRD readers expect precision about what null has been tested. Environment‑conditioned monopole differences across classes are not identical to angular dipole/quadrupole anisotropies; it is possible to have nonzero angular structure that averages out within each environment class.  
- **Required fix:**  
  - In the abstract and conclusions, explicitly qualify the main statement as:  
    • a null on *environment‑conditioned* differences in f\_{CW} across the tested classes,  
    • *conditional* on the catalog‑wide monopole and Paper‑IV angular constraints,  
    • and not as a general statement about all possible spatial anisotropies.  
  - Add a 1–2 sentence paragraph in Sec. XII clarifying that this paper does not newly constrain pure angular dipoles beyond Paper IV, and that angular anisotropy that is uncorrelated with the chosen environment classifiers is outside the scope of the present null.

---

P5-M7 (MAJOR) – Abstract and body state different sensitivity floors for voids and for the overall per‑class ranges  
- **Location:** Abstract (sensitivity floor sentence); Sec. VII A; Sec. VIII B–C; Table VI; Table VIII.  
- **Problem:**  
  - Abstract: “sensitivity floor set by the Paper IV catalog‑monopole offset of ∼0.2 pp … and by counting statistics of ∼5 pp (statistical‑dominated for V‑Web void at n = 428, ∼2σ on the binomial null).” This suggests 0.2 percentage points as the systematic floor for filament/cluster and ∼5 pp (≈0.05) as the statistical floor for voids.  
  - In Sec. VII A, the max per‑cell range is 0.22 pp and is compared to per‑class 1σ standard errors: ∼0.08 pp for filament/cluster, ∼0.6 pp for wall, and ∼2.4 pp for void. That is, the 1σ void error is ≈2.4 pp, not 5 pp; 5 pp would be ~2σ.  
  - The abstract collapses these into “∼5 pp” without explaining that this is ~2σ for voids, whereas the systematic floor is treated as 1σ for filament/cluster. The different σ‑levels are not clearly stated, creating a mixed standard of comparison.  
- **Why this matters:**  
  - Statements like “shows no environment dependence above the sensitivity floor” hinge on a clear, uniform definition of “sensitivity floor” in σ units. Mixing 1σ and 2σ thresholds for different classes without saying so makes it hard to interpret what is actually excluded.  
- **Required fix:**  
  - In the abstract and Sec. VII A, specify explicitly whether the quoted pp floors correspond to 1σ or 2σ and use a consistent convention across environments. For example:  
    • “systematic floor ≈0.2 pp (1σ for filament/cluster; monopole‑dominated)”  
    • “void statistical floor ≈2.4 pp (1σ; ≈4.8–5 pp at 2σ).”  
  - Rephrase “above the sensitivity floor” to something like “we are insensitive to environment‑dependent effects smaller than ≈0.2 pp in filament/cluster (1σ) and ≈2.5 pp in voids (1σ).”

---

P5-M8 (MAJOR) – Different σ–null procedures are juxtaposed without consistently warning that they are not directly comparable  
- **Location:** Sec. V A–B; Sec. VI C–E; Sec. VII A; HEALPix analysis (Sec. VI E, Table V); DESIVAST and ASTRA cross‑checks; Summary in Sec. XII A.  
- **Problem:**  
  - The paper uses at least three null procedures:  
    1. Gaussian “σ\_{\rm from\ half}” normal approximation to a binomial centered at 0.5.  
    2. Label‑shuffle permutation nulls; sometimes on σ\_{\rm from\ half}, sometimes on max‑|σ| across bins.  
    3. The shifted null with monopole σ\_{pred} from Eq. (1), where residuals |σ\_{\rm obs}−σ\_{\rm pred}| are compared to Bonferroni thresholds derived for a zero‑mean z‑score.  
  - In several places, results from different nulls are compared along a single “σ” axis: e.g., “cluster −4.7σ vs expected −3.3σ” (shifted monopole), next to “no NSIDE returns p<0.05; |σ|\_{max}=4.13 vs |σ|\_{max,p99}=4.78” (permutation‑based max‑statistic), and the overall “no 3σ deviations after LEE correction” statement. It is not always made explicit which σ comes from which null.  
  - There is no consolidated warning that a 3σ under the shifted monopole‑null is not directly comparable to a 3σ under the pure 0.5 null or to a 3σ derived from the empirical max‑statistic distribution.  
- **Why this matters:**  
  - Readers can easily over‑interpret the “3σ” language as uniform across the paper, when in fact the underlying test statistics and nulls differ.  
- **Required fix:**  
  - Add a short subsection (probably in Sec. V) that explicitly lists and distinguishes the three null procedures and states that their σ’s are not interchangeable.  
  - Whenever a σ is quoted in the text, specify in the first occurrence for each context which null it refers to (e.g., “σ\_{\rm from\ half} under the 0.5 null,” “σ relative to the Paper‑IV monopole,” “σ implied by the permutation‑based max statistic”).  
  - In integrative claims (e.g., Sec. XII A), avoid summarizing everything as “no 3σ deviations” without specifying which tests and nulls this sentence refers to; either quote p‑values or clearly separate the different σ’s.

---

P5-M9 (MAJOR) – Abstract and body disagree subtly on the status of the bright/dark 3.4σ filament sign flip  
- **Location:** Abstract robustness paragraph (last 5–6 sentences); Sec. VI D (tracer‑program stratification); Sec. XII A; Sec. XIII (limitations).  
- **Problem:**  
  - The body text is careful: it calls the filament bright‑vs‑dark sign flip (|z| ≈ 3.4σ on n\_{dark} = 21,203) “the strongest single residual structure in the paper” and explicitly says it cannot be cleanly attributed to pure selection function vs. astrophysics with current data. It also says the primary DESIVAST analysis is constructed to be insensitive to this residual.  
  - The abstract, however, folds this into the robustness narrative with phrases like “consistent with the BGS‑selection‑function‑conditioned imaging‑leg systematics tracked in Paper IV” and states that the headline environment‑independence statement is anchored on DESIVAST, with the 3.4σ flip “flagged as a real diagnostic” only near the end. The nuance that this is *unresolved*—not cleanly explained by systematics—is easy to miss.  
- **Why this matters:**  
  - By PRD standards, a 3.4σ residual that is not cleanly modeled is a material caveat. The abstract should make clear that this is an open issue rather than suggest that it is already fully understood as selection‑function conditioned.  
- **Required fix:**  
  - In the abstract, change wording from “consistent with the BGS‑selection‑function‑conditioned imaging‑leg systematics…” to something like “consistent with, but not uniquely attributable to, the BGS‑selection‑function‑conditioned systematics tracked in Paper IV; the 3.4σ filament bright/dark sign flip remains an unresolved residual.”  
  - In Sec. XV, explicitly mention this residual together with the main null: e.g. “while no environment‑dependent effect exceeds 3σ in the primary DESIVAST and V‑Web class tests, a 3.4σ bright‑vs‑dark residual in filaments remains and is left for future work.”

---

P5-M10 (MAJOR) – Apparent inconsistency between σ for the overall matched sample in Sec. VIII F and earlier descriptions of the same monopole  
- **Location:** Sec. VIII F (“Cross‑survey P4‑monopole‑residual analysis”); earlier Introduction/Sec. II; Abstract.  
- **Problem:**  
  - The introduction says Paper IV finds f\_{CW} = 0.4974 ± 0.000279, i.e. ∆f ≈ −0.0026, “∼9.5σ” at the catalog level. In the present paper, on the matched‑spiral subset of N = 791,635, you report f\_{CW} = 0.4972 (−5.00σ).  
  - Later in Sec. VIII F you also refer to an extended env‑labeled superset of 812,793 spirals with f\_{CW} = 0.49719, “−5.07σ,” and you say this is “the propagation of the ∼9.5σ catalog‑level monopole reported in Paper IV into the DESI‑spectro‑confirmed subsample.”  
  - The text at points treats ∆f = −0.0026 as a fixed property of the classifier, but the matched subsample has ∆f ≈ −0.0028 (8% larger), and the σ’s (−5.0 vs −5.07) are based on N that differ slightly from what appears in the headline tables. These differences are acknowledged but only qualitatively described as “consistent,” without actually recomputing and displaying the propagated uncertainties.  
- **Why this matters:**  
  - The matched‑sample monopole is the central quantity conditioning all environment tests. Any differences between its value and the Paper‑IV value should be explicitly propagated, not just described qualitatively as “∼8%.”  
- **Required fix:**  
  - Add a compact table (either in Sec. II or Sec. VIII F) listing: (i) the Paper‑IV catalog monopole (N, f\_{CW}, σ); (ii) the matched DESI subset monopole (N, f\_{CW}, σ); (iii) the env‑labeled superset monopole (N, f\_{CW}, σ).  
  - For each, compute the uncertainty on ∆f and show that the differences are/are not statistically significant.  
  - Use the *empirically measured* monopole of the env‑labeled sample as the prior in σ\_{pred}, or explicitly justify why you fix ∆f at −0.0026 when the matched sample suggests −0.0028.

---

P5-N4 (NIT) – Minor abstract/body number drift and stale phrasing  
- **Location:** Abstract (e.g., range of CW fractions, claimed ranges and σ’s); Sec. VI A; Table II; Sec. VII; Sec. XV.  
- **Problem:**  
  - Several numbers are repeated across the abstract, body, and conclusions (e.g., “range across classes is 1.98 percentage points,” “max per‑cell range 0.22 percentage points,” “−4.7σ cluster deviation”). As the analysis has clearly evolved (DESIVAST anchoring, ASTRA checks, etc.), it is easy for these duplicated numbers to become stale or inconsistent by 1–2 in the last decimal place.  
  - For instance, the abstract’s per‑class f\_{CW} values and σ’s should be re‑checked against Table II; small differences (0.4980 vs. 0.4980, −2.61σ vs recomputed −2.56σ) are not scientifically huge but are noticeable.  
- **Required fix:**  
  - After finalizing the numbers following the σ recomputation requested above, pass once through the abstract, Sec. VI, Sec. VII, Sec. VIII, and Sec. XV to ensure every repeated number matches exactly to the quoted tables.  
  - Where numbers are not central (e.g., “about 2σ”, “few‑percent”), it may be clearer to round explicitly rather than quote to four significant figures.

If you address these additional issues together with the earlier ones, the paper’s internal arithmetic, statistical interpretation, and headline claims will be much more robust by PRD standards.