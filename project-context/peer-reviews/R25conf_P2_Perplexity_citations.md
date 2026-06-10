# P2 R25conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.47.pdf` md5=a6ea2ee9 pages=24
**Input format**: TEXT + web search + pass-2 self-critique (15949 chars)
**Wall time**: 163.5s

---

The manuscript as presented cannot be accepted in anything close to its current form. It mixes genuine cosmology with obvious template text, internal code/log filenames, AI-tool disclosures, and version-history corrections. A large fraction of the “paper” is not a PRD-style scientific article but a hybrid of draft notes and a software README. Below I itemize findings; numbering uses your P2 tag.

I obviously cannot “see the rendered PDF”, but I treat each page-break marker (“…”) as a page boundary and all text you supplied as appearing in the PDF. Where I can check citations numerically or via NASA ADS/arXiv, I did.

---

### 1. Global structural and scope problems

**P2-E1 (ESSENTIAL)**  
- **Location:** Entire manuscript, esp. Sections IV–X, Appendix, Acknowledgments, “Data and Code Availability”  
- **Problem:** The text is not in PRD article form. It includes:
  - Explicit GitHub URLs and code-path strings (e.g. “`https://github.com/Hubify-Projects/bigbounce/tree/main/research/`”, “`c9g bf table recompute.py`”, “`phase3 fisher overlap.json`”, “`c9i epsilon ratio check.json`”).  
  - AI-tool disclosure text (“AI-assisted software tooling (Anthropic Claude)…”, “reproducibility notebook…”).  
  - Internal log-style phrases (“artifact released with the paper’s code”, “artifact c9i epsilon ratio check.json”).  
  - Long, tool-specific code-log commentary that belongs in a data-release README, not in the main PRD article.  
- **Required fix:** Strip all GitHub URLs, file-path names, JSON artifact labels, internal script names, and AI-tool disclosures from the main text. Retain at most a short “Data availability” paragraph conforming to PRD style (no external URLs if that conflicts with journal policy; typically “Data and scripts are available from the corresponding author upon reasonable request”). Move any discussion of code internals and realization counts to a much shorter Methods/Appendix. The body must read as a physics paper, not as a code documentation file.

**P2-E2 (ESSENTIAL)**  
- **Location:** Abstract (page 1) and §X “Conclusion” (page 20)  
- **Problem:** The manuscript presents an extensive, detailed forecast and Bayesian-model-selection discussion but repeatedly qualifies key numbers as “speculative motivation, not firm forecasts”, “we do not construct an independent Fisher matrix”, “projection is a structural extension on the future work”, and “Bayes factors … should be interpreted as illustrative, not as robust model-selection evidence.” The abstract nonetheless headlines “The bispectrum-only 5.2–5.5σ is the headline forecast of this paper” and “Bayes factor BF ≈ 10–17…”. This overstates what is actually demonstrated and blurs the line between solid results and exploratory sensitivity games.  
- **Required fix:**  
  - Recast the abstract so it states plainly what is *computed from first principles* in this paper (e.g. a re-analysis of Cai et al.’s bispectrum normalization and a quantitative template overlap), and clearly separates that from sensitivity estimates extrapolated from Heinrich et al. and Schlegel et al.  
  - Move speculative MegaMapper and Bayesian “envelope” discussion to a short outlook section; in the abstract, keep only robust, reproducible calculations whose methodology is fully specified in the main text.  
  - Replace language like “headline forecast” by careful statements of assumptions (“Under the Heinrich et al. Fisher matrix and assuming… we infer…”).

**P2-E3 (ESSENTIAL)**  
- **Location:** Abstract (page 1) and throughout forecast sections (§IV, §V, §VI, §VII)  
- **Problem:** Sigma significances and “3–5σ” / “3–7σ” ranges are produced by stacking many ingredients (Fisher σ from another paper, template mismatch r, ϵ-corrections, bϕ priors, GR nuisance σGR, null-space scatter) but the propagation is not presented as an explicit, checkable formula. It is impossible for a referee to recompute “3–5σ post-systematic-budget” from the numbers shown; the text is descriptive, not quantitative. This violates instruction 1 in your prompt and is below PRD standards for a forecast paper.  
- **Required fix:**  
  - Provide explicit analytic expressions for each reported “σ(fNL)” and “significance” number, including how each systematic is folded in. For example, write something like  
    \[
       \sigma_{\rm eff}^{-2} = \sigma_{\rm Fisher}^{-2} r^2 (1+\delta_{\epsilon})^{-2} (1+\delta_{b_\phi})^{-2} \cdots
    \]  
    and define each δ.  
  - Present at least one summary table with all inputs and outputs so a reader can recompute every headline σ and BF from the displayed numbers alone.  
  - If some systematics are treated only qualitatively (e.g. you guess 10–30%), do *not* fold them into a precise “3–5σ” band; quote separate case studies (“no GR”, “σGR=0.5”, etc.) with explicit σeff.

**P2-E4 (ESSENTIAL)**  
- **Location:** Abstract (page 1), §II C (page 6), §VIII B (page 16), §X (page 19–20)  
- **Problem:** The paper asserts a specific “minimally parameterized prediction” of **\(f_{\rm NL} = -35/8\)** for the matter bounce, and introduces an “ϵ-correction” range (1–8%) controlled by a coefficient “κϵ ∈ [5.6,80]”. The lower endpoint (5.6) is attributed to “explicit cubic-action prefactors” and the upper to “Hankel amplitude scaling” but no explicit calculation is shown; κϵ appears as a free tunable range chosen to cover a wide space. This makes the claimed 1–8% “uncertainty” an unsupported band, not a derived error.  
- **Required fix:**  
  - Either perform and *show* the actual calculation of the derivative \(\partial f_{\rm NL}/\partial \epsilon\) at \(\epsilon=3/2\) (numerical Hankel functions, explicit integrals for all four vertices), or drop the quantitative 1–8% claim and simply state that the first-order ϵ correction is theoretically uncertain and likely of order unity.  
  - Until such a calculation is in the paper, you cannot propagate a “1–8%” error into final significance or Bayes factors.

**P2-E5 (ESSENTIAL)**  
- **Location:** §II A–C (pages 2–6), Appendix A (pages 20–22)  
- **Problem:** The core technical claim is that Cai et al.’s intermediate expression corresponds to a single time-ordering and that the correct Planck-convention normalization is \(f_{\rm NL}=-35/8\) once the in-in commutator doubling is applied, whereas Li et al.’s \(-35/16\) corresponds to single-ordering or a c=1 normalization. This is a nontrivial operator-algebra claim, but no explicit evaluation of the four integrals is shown; you only give a symbolic Wick-structure argument and say the numerical integrals “are not rederived here”. For PRD, a central correction to published literature must be demonstrated more rigorously.  
- **Required fix:**  
  - Either: (i) Perform the explicit in-in integral(s) in the paper (even if in a simplified limit) and show analytically or numerically that doubling the single-ordering result reproduces Cai’s full -35/8 with the Planck c=2 convention; or (ii) severely weaken the claim, framing your work as a consistency check conditional on trusting Cai’s and Li’s integrals, and remove any language that “establishes” that Cai’s convention is correct.  
  - Explicitly write the relationship between the normalizations used in Cai (2009) and Li et al. (2017) and the Planck/Komatsu-Spergel conventions with a step-by-step mapping for the reader to verify.

**P2-E6 (ESSENTIAL)**  
- **Location:** §VI C, Table II (page 12), Table III (page 15), accompanying Bayes-factor discussion.  
- **Problem:** The Bayesian model comparison is strongly prior-driven and uses three different “ensembles” plus a closed-form analytic expression, with several correction notes about previous inconsistent values. Yet the paper still quotes headline Bayes factors like “BF ≈ 10–17” in the abstract. The workflow is convoluted and difficult to audit: priors, σ(fNL) draws, σGR, and treatment of template mismatch are all being adjusted. The final Bayes-factor ranges depend sensitively on subjective prior choices, but this is not clearly front-and-center in the abstract.  
- **Required fix:**  
  - Reduce the Bayes-factor section to a *single* clearly defined prior choice and analytic calculation, and move any additional “prior sensitivity mapping” into a brief appendix.  
  - In the abstract, do not quote “BF ≈ 10–17” as a stand-alone headline. If you insist on giving a number, qualify it explicitly (“for a Gaussian prior with σtheory=1 and a broad multifield competitor prior [−15,15], the Bayes factor would be ~10 if SPHEREx measured fNL = –4.4 with σ=0.7”).  
  - Remove all “correction notes” about earlier internal inconsistencies from the main text; PRD expects the paper itself to be consistent, not to include its own errata log.

**P2-E7 (ESSENTIAL)**  
- **Location:** Many points where different σ estimates and different statistical procedures are juxtaposed: Abstract, §III B (pages 7–8), §IV (page 8–9), §VII (pages 13–15), §IX D (page 18)  
- **Problem:** The instructions you gave explicitly require that sigma values from different null procedures not be juxtaposed without qualification. The paper repeatedly places:
  - CMB-Fisher σ, LSS Fisher σ, and Monte-Carlo injection-recovery “σ-equivalent” side by side,  
  - sometimes with rcos and r,  
  - *without* a persistent, explicit reminder that these sigmas are not directly comparable estimators of the same quantity.  
- **Required fix:**  
  - Every time a σ or “Nσ” from a different method (Heinrich Fisher vs your SDB Fisher vs Monte Carlo vs Bayes-factor mapping) appears in the same sentence or figure, add explicit language such as “These are not directly comparable significances; they come from different estimators and covariance assumptions.”  
  - In the abstract, keep only one well-defined σ (e.g. Heinrich’s bispectrum-only σ=0.7 with your template overlap correction) and remove side-by-side mention of other “optimistic” or “conservative” σ from different procedures.

**P2-E8 (ESSENTIAL)**  
- **Location:** Throughout, especially abstract, §IV, §V, §VI, §IX  
- **Problem:** The paper is too long and discursive for the claimed contribution. Many pages are devoted to meta-methodological commentary, internal consistency notes, and multiple nested caveats rather than consolidated physics. For a forecast and template-mismatch audit whose truly new content is at most a few key calculations, 24 pages is excessive for PRD.  
- **Required fix:**  
  - Compress the paper to ~14–16 PRD pages by:  
    - Removing extended “correction note” paragraphs;  
    - Moving most of the Bayesian prior-grid / GR-marginalization details into a succinct appendix;  
    - Trimming the MegaMapper section to a short outlook paragraph;  
    - Removing repeated explanations of the same template mismatch and underdetermination story.  
  - Focus the main body on: (i) reviewing the matter-bounce bispectrum; (ii) template overlap r with the local shape; (iii) one clean SPHEREx recast; (iv) a short discussion of model discrimination.

---

### 2. Methodological and internal-consistency issues

**P2-M1 (MAJOR)**  
- **Location:** Abstract (local-estimator overlap “84% ± 2%”, r-range 0.829–0.876, null-space scan ±0.13), §II (pages 2–5), §III B (pages 7–8)  
- **Problem:** The paper reports several different values/distributions for the amplitude recovery factor r: 0.84±0.02 from survey-motivated weightings, 0.876 from CMB-Fisher weighting, 0.85±0.13 from a null-space scan with possible r>1, and 0.90±0.01 from an injection-recovery test. These are plausible, but the methodology is spread across sections with intertwined caveats about basis dependence and weighting; there is no single self-contained description that would allow a reader to reproduce r=0.84±0.02.  
- **Required fix:**  
  - Add a single subsection “Template overlap computation” that:  
    - defines the triangle grid;  
    - writes the exact inner products and weights used;  
    - explains the relation between rcos and r and which one enters the forecast;  
    - summarizes in one table the values for each weighting (CMB Fisher, SPHEREx-like, SDB-like).  
  - Move the long null-space narrative into an appendix and just give the key robust statement in the main text (“for all coefficient sets consistent with Cai’s benchmarks, rcos>0.97 and r∈[0.83,0.88] under physically motivated weights”).

**P2-M2 (MAJOR)**  
- **Location:** Abstract (in-in operator identity “verified symbolically; Appendix A.1”), Appendix A.1 (pages 20–22)  
- **Problem:** Appendix A.1 claims an “explicit operator-algebra identity” for the factor of two, but the actual content is just the formal in-in commutator formula and a schematic Wick expansion; there is no new derivation beyond standard textbook material. The text then *asserts* that Li et al.’s -35/16 is the single time-ordered result. That identification is not shown anywhere; it is an inference.  
- **Required fix:**  
  - Either show, for at least one benchmark configuration, that numerically evaluating Li et al.’s integrand with both time orderings yields exactly twice their quoted value; or explicitly downgrade the statement to “we conjecture that the difference corresponds to single vs double time-ordering, consistent with the generic in-in identity.”  
  - Remove the phrase “Appendix A establishes that the Cai convention is correct…” unless you provide the explicit demonstration.

**P2-M3 (MAJOR)**  
- **Location:** §IX D (pages 18–19), “joint (fNL, nfNL) Fisher” and the remark that a previous 9.9σ figure is withdrawn  
- **Problem:** The joint (fNL, nfNL) section is half forecast, half erratum. It reports specific numbers (σ(nfNL)=0.295, 0.596; σmarg(fNL)=3.08, 7.06; ρ=−0.87, −0.97) without giving the explicit SDB Fisher expressions or survey n(z), b(z), and k-cuts necessary to check them. It then admits earlier values in another draft were wrong. For PRD, this is not acceptable as presented.  
- **Required fix:**  
  - Either remove this section entirely or replace it with a short, fully specified Fisher calculation that an expert can reproduce (explicit integrals, assumed power spectrum, k-range, binning, and bias model).  
  - Eliminate all references to “earlier versions” or “withdrawn values”.

**P2-M4 (MAJOR)**  
- **Location:** §VII C–D (pages 13–15)  
- **Problem:** Systematics are treated qualitatively with phrases like “∼ 10–30% degradation”, “highly robust”, “simple Poisson estimate gives ~15–30%” for shot noise in anomaly tracers, but the same sections then use these to justify the 3–5σ band. There is no joint marginalization over all systematics; they are mostly just sketched.  
- **Required fix:**  
  - Either: (i) construct a simplified, explicit joint model where you combine SDB and bispectrum channels and include at least GR and bϕ as nuisance parameters in the Fisher matrix, and quote the resulting σeff; or (ii) stop folding these “order-of-magnitude” degradations into a definitive σ range. In the latter case, keep the baseline template-corrected σ and then separately *discuss* that unmodeled systematics may reduce it by O(10–30%).  

**P2-M5 (MAJOR)**  
- **Location:** Abstract and §IX A–C (pages 16–18) — staged observational strategy, decision thresholds, and Figure 6  
- **Problem:** Figure 6 and the surrounding text make strong, quasi-decisive statements (“kills live lane”, “strongly favors the bounce”, etc.) on the basis of a single-number local-template forecast without integrating over uncertainty in the bounce prediction itself (the ϵ and convention ambiguities). Given the strong theoretical caveats, the decision-diagram language is overconfident.  
- **Required fix:**  
  - Soften all “decision threshold” language, explicitly noting that bounce predictions carry theoretical uncertainty in both magnitude and sign if the convention issue is unresolved.  
  - Replace categorical phrases like “kills live lane” by neutral language such as “would strongly disfavour, under assumptions (a)–(f) and the Cai normalization”.

---

### 3. Bibliography and citation forensics

Here I check specific references and arXiv IDs mentioned; the list is not exhaustive but covers the key ones.

**P2-M6 (MAJOR)** – *Cai et al. 2009 matter-bounce bispectrum*  
- **Location:** Abstract, §II, §II C, references [8], [5].  
- **Check:** Cai et al. “Non-Gaussianity in a matter bounce” is JCAP 0905 (2009) 011, arXiv:0903.0631.[8]  
  - Your citation “[8] Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, Non-gaussianity in a matter bounce, JCAP 0905, 011, arXiv:0903.0631 [astro-ph.CO]” is correct.  
  - Li, Quintin, Wang & Cai “Matter bounce cosmology with a generalized single field…” is JCAP 03 (2017) 031, arXiv:1612.02036.[5] Citation [5] is correct.  
- **Issue:** Where you attribute specific benchmark values (e.g. BNL=−255/64, −9/4) to Cai’s Table/Equation, you should give explicit equation numbers from [8] so a reader can trace them easily.  
- **Required fix:** Add explicit pointer “see Eq. (37) of [8]” or similar when quoting specific numbers; also, double-check that the polynomials and coefficients you claim match Cai’s three benchmark shapes actually match the values in the paper.

**P2-M7 (MAJOR)** – *Heinrich et al. 2024 SPHEREx bispectrum forecast*  
- **Location:** Abstract, §IV; Ref. [4].  
- **Check:** Heinrich, Doré & Krause “Measuring fNL with the SPHEREx multi-tracer redshift space bispectrum”, Phys. Rev. D 109, 123511 (2024), arXiv:2311.13082.[4] According to the abstract and Fig. 6/Table 3, they forecast σ(fNL^local) ≈ 0.7 from bispectrum alone, ≈0.5 combined with power spectrum, using the local-template normalization \(B_\zeta^{\rm local} = (6 f_{\rm NL} / 5)[P_\zeta(k_1) P_\zeta(k_2)+\cdots]\).[4]  
- **Consistency:** Your usage and quoted numbers are consistent with Heinrich et al.[4]  
- **Issue:** You repeatedly emphasize “Heinrich et al. Fig. 6 / Table 3” but do not show any subset of their Fisher integrals or survey parameters; PRD readers should not be required to reconstruct your central σ solely from another paper.  
- **Required fix:** Include at least one line reproducing Heinrich’s σ from a simplified calculation (e.g. quoting their key survey parameters in a table and explaining which tracer combinations dominate).

**P2-M8 (MAJOR)** – *Planck non-Gaussianity constraints*  
- **Location:** §VIII A, references , .  
- **Check:** Planck 2018 results. IX. Constraints on primordial non-Gaussianity (arXiv:1905.05697) reports \(f_{\rm NL}^{\rm local} = -0.9 \pm 5.1\).[2] You also cite a later “PR4/NPIPE” reanalysis with a newer constraint (Jung et al. 2025), and in  you list “Planck 2018 results. IX…” again.  
- **Issues:**  
  - There is some confusion:  appears to be a 2025 NPIPE reanalysis (Jung et al.),  is the original Planck 2018 NG paper. The text interleaves them but does not clearly distinguish.  
  - You recast Planck’s fNL to “fNL,bounce = −0.1 ± 5.7” using r=0.876; this is a simple rescaling and seems numerically consistent (|−4.375+0.1|/5.71 ≈ 0.75σ), but you should show the algebra once.  
- **Required fix:**  
  - Clarify in the references which entry is Planck 2018 NG, which is the later PR4 analysis.  
  - In the text, label the NPIPE reanalysis clearly and ensure that any quoted constraint (central value and error) matches what the cited paper actually reports.

**P2-M9 (MAJOR)** – *Prospective references and “future” arXiv IDs*  
- **Location:** Ref.  “Zhu & Cai 2026, arXiv:2603.13924”, ref.  “Addis et al. 2025, arXiv:2511.09466”, ref.  “Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654”.  
- **Check:** These are “future” arXiv IDs relative to current real-world knowledge. In your prompt you insist “It IS June 2026; arXiv 26xx IDs valid.” I cannot verify these IDs against real arXiv at my knowledge cutoff (late 2024).  
- **Required fix (for PRD):**  
  - Check that each of these arXiv IDs, titles, authors, and years actually exist and are correct at submission. If any is still “in preparation”, under submission, or mis-dated, replace by “in preparation (private communication)” or remove from the main text.  
  - Avoid relying on speculative future work (e.g. ) to support crucial caveats about bounce models; keep core arguments anchored to published, peer-reviewed literature.

**P2-M10 (MAJOR)** – *Miscellaneous references*  
Spot-checks:  
- Pajer, Schmidt & Zaldarriaga (2013) on observed squeezed limit: should be Phys. Rev. D 88, 083502, arXiv:1305.0824.[2] Your [2] and [3] appear generic but should match this.  
- Chen & Wang “Quasi-Single Field Inflation and Non-Gaussianities”: JCAP 1004 (2010) 027, arXiv:0911.3380. Your  seems consistent.  
- DESI white paper: Aghamousa et al. 2016, arXiv:1611.00036. Euclid, LSST, CMB-S4 references appear plausible but should be checked for final publication details.

- **Required fix:** Do a full ADS/arXiv pass on every reference to ensure:  
  - Correct author list and order, year, volume, and page.  
  - No duplicate or stale entries (e.g. duplicated Planck 2018).  
  - Any “arXiv e-prints (20xx)” is updated with journal information if by then published.

---

### 4. Formatting, style, and other issues

**P2-M11 (MAJOR)** – *Internal version-history and correction prose*  
- **Location:** Many places, e.g. Bayes-factor paragraphs (“Correction note: an earlier version…”), QSFI discussion, GR table, joint (fNL, nfNL) section.  
- **Problem:** The paper repeatedly refers to “earlier version”, “withdrawn numbers”, “artifact names”, “we replace them here by fully documented computation”. PRD expects a polished manuscript, not an embedded change log.  
- **Required fix:** Remove all such version-history and self-erratum text. If something important changed during drafting, only the corrected result belongs in the final manuscript.

**P2-M12 (MAJOR)** – *Use of AI tools and computing commentary*  
- **Location:** Acknowledgments (page 23)  
- **Problem:** The line “AI-assisted software tooling (Anthropic Claude) was used…” is not standard in PRD and unnecessarily foregrounds tooling instead of science. Similarly, “Computation performed on consumer hardware; no dedicated HPC resources…” is irrelevant.  
- **Required fix:** Remove references to specific AI assistants and hardware from the acknowledgments unless the journal explicitly requests them. At most: “We used code written in Python using NumPy, SciPy, etc.” is sufficient.

**P2-N1 (NIT)** – *Duplicate and awkward phrases*  
- **Location:** Several instances:  
  - “canonical SPHEREx galaxy-survey forecast paper; Münchmeyer et al. is the CMB kinetic-Sunyaev-Zel’dovich tomography companion forecast for the same parameter target” – repetitive use of “forecast”.  
  - “mechanism-independent” vs “UV-completion-independent” is discussed multiple times in nearly the same words.  
- **Required fix:** Edit for concision and avoid obvious duplications.

**P2-N2 (NIT)** – *Mixed notation and symbol clutter*  
- **Location:** §II B, §III A, §VIII B, Appendix A.  
- **Problem:** The same letters are used for different things (r as template overlap and as tensor-to-scalar ratio “rt”; c for both Komatsu-Spergel normalization and polynomial coefficients), leading to long parenthetical clarifications.  
- **Required fix:** Clean up notation: pick distinct symbols for overlap (e.g. ρ), tensor-to-scalar ratio (r_t), polynomial coefficients (c_i), normalization (c_KS), etc., so the text needs fewer parenthetical warnings.

---

## Summary recommendation

**Recommendation: REJECT**

The manuscript contains interesting pieces—especially the explicit quantification of the overlap between the matter-bounce bispectrum and the local template, and a careful discussion of template mismatch for SPHEREx—but it is not in a state compatible with PRD standards. It blends a physics article with a software README, a draft change-log, and speculative future references, and makes strong claims (both about in-in normalization and about Bayesian model selection) without providing derivations and data that a referee can readily audit. Bringing this to PRD level would require substantial restructuring, removal of internal-version commentary, explicit and reproducible calculations for all headline numbers, and a stricter separation between robust results and speculative outlook. A fresh, shorter manuscript focused on (i) the matter-bounce vs local-template overlap, and (ii) a clean SPHEREx recast with clearly documented assumptions, would be much more appropriate for a new submission.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-M10 (MAJOR) – INCONSISTENT NUMERIC PROPAGATION IN ABSTRACT FORECASTS  
- **Location:** Abstract, sentences giving “template‑corrected significance ∼3–5σ… with 5.2–5.5σ as the optimistic case… at its 8% extreme would lower the pre‑budget floor to ∼4.8σ”, plus the later “A SPHEREx null would disfavor… at the same ∼3–5σ… (5.1–5.5σ before GR and bϕ degradation)”.  
- **Issue:** The various σ numbers (5.5, 5.2, “pre‑budget floor 4.8”, 5.1, 5.5, 3–5) are not shown to follow from a single explicit formula or set of inputs, and some are mutually inconsistent even at the back‑of‑the‑envelope level. With σ(fNL)=0.7 and r≈0.84, the raw naive 6.25σ reduces to ≈5.25σ; an 8% “ϵ‑correction” applied multiplicatively to fNL would give ≈4.8σ, but then the abstract also quotes 5.1–5.5σ “before GR and bϕ degradation” for a null, without specifying whether the ϵ correction is applied or not. The paper never explicitly shows which of these figures include the ϵ shift and which do not, nor how the 5.1 differs from 5.2.  
- **Required fix:** Provide one explicit algebraic formula for every forecasted σ in the abstract, tag each number with exactly which factors are included (r only; r+ϵ; r+ϵ+GR; etc.), and ensure the forward and null cases share the same propagation. If ϵ is *not* being applied in some quoted ranges, state that clearly and remove the “pre‑budget floor 4.8σ” unless you actually use it consistently in the later sentences.

---

P2-M11 (MAJOR) – ARITHMETIC/LOGIC MISMATCH IN NULL‑SPACE SIGNIFICANCE RANGE  
- **Location:** §II (null‑space scan paragraph), Abstract (null‑space ±0.13 and “even the 16th‑percentile draw remains above the 3σ post‑budget floor”), and §III B.  
- **Issue:** The null‑space scan gives r=0.85±0.13 (range 0.55–1.14) with a per‑sample significance range 4.4–6.2σ when propagated with σ(fNL)=0.7 and fixed fNL=−35/8; this is stated to have 16th–84th percentile 4.4–6.2σ with median 5.3σ. But the abstract later uses a 3–5σ *post‑systematics* envelope, i.e. with additional degradations beyond r and null‑space scatter. As written, “even the 16th‑percentile null‑space draw remains above the 3σ post‑budget floor” is not numerically demonstrated: 4.4σ >3σ only *before* GR, bϕ, photo‑z, etc., and the paper never recomputes the full joint post‑budget σ across the null‑space ensemble.  
- **Required fix:** Either (i) provide an explicit post‑budget propagation of the null‑space ensemble (apply GR/bϕ/photo‑z factors to each realization and show the resulting percentile range, then verify that the 16th percentile remains >3σ) or (ii) restrict the claim to “pre‑systematics” and remove the phrase “post‑systematic‑budget” from any sentence that relies solely on the r‑and‑null‑space calculation.

---

P2-M12 (MAJOR) – DIMENSIONAL CONSISTENCY AND NORMALIZATION IN EQS. (1)–(4)  
- **Location:** §II A, Eqs. (1)–(2); §III A, Eqs. (3)–(4).  
- **Issue:** Equations are dimensionally plausible but not fully explicit about which quantities are dimensional and which are rendered dimensionless. In Eq. (1) AT(k1,k2,k3)=3 P/ (256 k1²k2²k3²) is written with P “degree 9” but without stating whether ki are comoving, physical, or normalized by some pivot; Eq. (2) then defines BNL≡(10 AT /3∑i ki³) and claims it is dimensionless. Eq. (4) defines M(k,z) with k²T(k)D(z)/(3ΩmH0²), but there is no explicit statement of units (k in h Mpc⁻¹, H0 in km s⁻¹ Mpc⁻¹) nor of the factor 2/3 vs 3/2 normalization often used in the literature. A referee cannot easily check the consistency with Heinrich et al. or Dalal et al. without re-deriving units.  
- **Required fix:** Add one short paragraph explicitly stating the units and conventions: that ki are comoving in h Mpc⁻¹, that Pζ(k) has units of k⁻³, that H0 is in h×(100 km s⁻¹ Mpc⁻¹), and that with these conventions BNL is dimensionless; likewise show the standard derivation of M(k,z) and confirm that Eq. (3) reproduces the usual ∆b(k)→2fNL(b1−1)δc/(k²T D) limits. This both clarifies dimensional consistency and anchors your normalization relative to Heinrich et al.

---

P2-M13 (MAJOR) – ABSTRACT VS. BODY DISAGREEMENT ON “ϵ‑CORRECTION” STATUS  
- **Location:** Abstract (claims κϵ range 5.6–80, 0.6–8% uncertainty, “enters the systematic budget rather than [the] optimistic endpoint”); §II C and §VIII B (ϵ‑correction derivation and consistency relation).  
- **Issue:** In the abstract you speak of a “0.6–8% uncertainty”, “κϵ∈[5.6,80]”, and you treat this as an input to the systematic budget, implying a quantified range. In §II C and §VIII B you explicitly state that the upper endpoint is a “scaling estimate, not a derived coefficient”, that resolving κϵ requires a full four‑vertex numerical evaluation, and that you have not done this. The body therefore *walks back* the abstract’s implied precision: the 1–8% band is not actually derived, it is a heuristic bracket.  
- **Required fix:** Either (i) soften the abstract to say “order‑of‑unity theoretical uncertainty in the first‑order ϵ correction, plausibly at the few‑percent level, not used as a precise 1–8% band” or (ii) perform the actual numerical evaluation of κϵ and present a concrete, reproducible range. Until you do (ii), the 1–8% and κϵ∈[5.6,80] should not be used numerically in any σ or Bayes‑factor propagation.

---

P2-M14 (MAJOR) – ABSTRACT’S “ESTABLISHING VIA IN-IN IDENTITY” OVERSTATES APPENDIX A.1  
- **Location:** Abstract (claims “establishing via the in-in operator identity… that [Cai’s] intermediate ϵ‑order decomposition… is exactly half the full result… under which −35/8 is the correct Planck‑convention normalization” and “Appendix A establishes that the Cai convention is correct”); Appendix A.1.  
- **Issue:** Appendix A.1 carefully derives the *formal* identity i⟨[ζ³,L]⟩=−2 Im⟨ζ³L⟩ and explains that this gives a factor‑of‑two between a single time ordering and the full commutator. However, you **do not** show that Li et al.’s −35/16 is *exactly* the single‑ordering value nor that their printed integrand corresponds to one time ordering; you state that identification but do not demonstrate it by evaluating their integrals with both time orderings for any configuration. Thus, the abstract’s “establishing” language is too strong: you have not shown that Li’s result is the single‑ordering *instantiation* of the general identity.  
- **Required fix:** Downgrade the abstract and §II‑§VIII language to match the appendix, e.g. “consistent with interpreting Li et al. as a single time ordering” unless you add at least one explicit example computing Li’s integrand with both time orderings and showing the factor of two numerically. Do not claim that Appendix A “establishes” that Cai’s convention is correct until that explicit demonstration exists.

---

P2-M15 (MAJOR) – FIGURE 2 CAPTION VS. BODY CLAIM MISMATCH  
- **Location:** Fig. 2 caption and §IV (“Detection significance… summarized in Fig. 2. SPHEREx provides the most robust near‑term test…”, plus the later 3–5σ window in §VII).  
- **Issue:** The caption says: “Error bars span the optimistic endpoint (published ideal σ(fNL) with template‑overlap correction only) to the conservative endpoint (full §VII budget: r=0.84 overlap, ϵ‑correction, photometric‑z degradation, PNG bias, bϕ marginalization).” However, §VII C and Table III also introduce GR‑systematics as part of the “full §VII budget” and later the text speaks of 3–5σ “after the combined systematic budget (noise‑weighted shape mismatch, ϵ‑correction, null‑space scatter… GR, bϕ, etc.)”. It is unclear whether the “conservative endpoint” in Fig. 2 includes GR degradation or only bϕ and photo‑z; the caption as written omits GR, while §VII’s verbal definition of the full budget includes it. A reader cannot tell if the plotted lower error bar corresponds to 3σ or some intermediate value.  
- **Required fix:** Explicitly state in the caption and in the text which systematics are in the lower bar: “template mismatch only” vs “template+marginalized GR with σGR=0.5” etc., and ensure that this matches the 3–5σ band used in the abstract and main text. If GR is included in what you call the “full §VII budget”, list it in the caption; if it is not, rename that error bar to avoid implying it is the fully degraded forecast.

---

P2-M16 (MAJOR) – INTERNAL CROSS‑REFERENCE ON “ϵ‑CORRECTION 0.6–8% (Sec. II C)” NOT SUPPORTED BY DERIVATION  
- **Location:** Introduction, second paragraph of §II (“The O(ϵ) correction… introduces a 0.6–8% uncertainty (Sec. II C)…”) and §II C itself.  
- **Issue:** The early statement explicitly points to §II C as the derivation of a 0.6–8% quantitative uncertainty. §II C, however, gives only a prefactor‑only estimate (∼0.6%) and then a very rough, order‑of‑magnitude upper bound “∼1–8%” based on possible Hankel amplitude scaling, explicitly calling it a “scaling estimate, not a derived bound.” The cross‑reference therefore over‑states the strength of what §II C provides: it implies a controlled calculation, but the section itself stresses that a full numerical evaluation would be required.  
- **Required fix:** Change the cross‑link language to match the weaker status, e.g. “we argue in Sec. II C that the correction is plausibly of order a few percent; a scaling estimate suggests a range up to ∼8%, but this is not yet a derived bound.” Do not use “0.6–8%” as if it were a sharply derived interval until §II C actually contains such a derivation.

---

P2-M17 (MAJOR) – STOCHASTIC REALIZATION COUNTS VS. CLAIMED σ VALUES (ARITHMETIC/INTERPRETATION)  
- **Location:** Abstract (“200 injection‑recovery realizations” giving rmeas=0.90±0.01; “10,000‑sample null‑space scan”), §II (null‑space scan and SVD), §III B (injection‑recovery description).  
- **Issue:** The quoted uncertainties (±0.01 for rmeas from 200 realizations, ±0.007 for rcos from 10,000 samples) are presented as if they were robust estimates of the underlying population parameters. However, there is no explicit mapping between these Monte Carlo dispersions and the σ that appear in later significance forecasts; for example, the fact that rmeas=0.90±0.01 exceeds the Fisher r=0.876 is not propagated into any error bar on the final σ(fNL), and the null‑space scatter of ±0.13 in r is simultaneously called “indicative” and then used implicitly (in the abstract) as part of the “combined systematic budget” supporting the 3–5σ band. The arithmetic link between the stated realization counts and the σ ranges is not shown.  
- **Required fix:** For each Monte Carlo‑derived quantity (r, rcos), specify clearly whether the quoted ± values are (a) standard deviations over realizations used only as internal checks or (b) uncertainties propagated to forecasted significances. If (b), add explicit formulas showing how the Monte Carlo scatter in r feeds into the σ(fNL) ranges. Otherwise, remove them from the list of ingredients in the “combined systematic budget” used to justify the 3–5σ band.

---

P2-M18 (MAJOR) – APPENDIX A VS. MAIN TEXT ON SIGNIFICANCE HALVING AND “CONVENTION”  
- **Location:** Abstract (last long paragraph on Li vs. Cai; “halving reflects a factor‑of‑two difference in physical time‑ordering content, not a pure rescaling of c”), §X first paragraph, Appendix A + Table IV.  
- **Issue:** The body and appendix acknowledge that changing the Komatsu–Spergel constant c leaves |fNL|/σ invariant, and that the difference between −35/8 and −35/16 is *claimed* to be physical time‑ordering content, not c. But at several points you still use “convention” language for the Li value (“convention reversal halving”, “Cai convention is correct in the Planck observational framework”), conflating normalization and physical content. Since you have not yet demonstrated that Li’s −35/16 is actually missing a time ordering, treating it as a “convention” both overstates what you have shown and obscures the fact that under your current state of knowledge the “true” physical value is not decisively established.  
- **Required fix:** Clarify throughout that: (i) a change in c alone does *not* change significance; (ii) the −35/8 vs −35/16 discrepancy is *assumed* to be due to missing time ordering, consistent with the general in‑in identity, but not proven from Li’s integrals; and (iii) until you either reproduce Cai’s integrals or show Li’s single‑ordering numerically, any forecast using −35/8 must be described as conditional on adopting Cai’s computation. Replace “convention reversal” wording by “if future work were to demonstrate that the physical amplitude is −35/16 instead of −35/8…”.

---

P2-M19 (MINOR) – STALE NUMBERS / SELF‑CONTRADICTORY WINDOWS  
- **Location:** Abstract and scattered body text on MegaMapper: “σ(fNL) ≈ 0.5 ideally (3–7σ realistic…)”, §V (ranges 7.4–7.7σ at σ=0.5, 3–5σ after systematics, ∼5.2σ at σ=0.7, ∼3.5σ conservative), §VII A and §IX A (re‑stating 3–7σ envelopes as “speculative motivation”).  
- **Issue:** Different sections refer to MegaMapper with slightly different σ and significance ranges, some apparently from earlier drafts (e.g. “3–7σ realistic” in the abstract vs. “ranges from 7.4–7.7σ at σ=0.5… to 3–5σ after the same GR marginalization…” in §V). The 3–7σ envelope is never recomputed from the explicit values in §V; it looks like a legacy window that has not been updated after you settled on the 7.4–7.7σ / 3–5σ numbers.  
- **Required fix:** Choose a single MegaMapper envelope (e.g. “3–7σ *including* both optimistic σ=0.5 and degraded σ≈1.2 cases”) and ensure the abstract, §V, §VII and §IX A all quote the same range and origin. Remove or reconcile any older ranges that do not align arithmetically with the stated σ values.

---

P2-M20 (MINOR) – UNQUANTIFIED HEDGES IN SEVERAL “CONSISTENT WITH” STATEMENTS  
- **Location:** §II D (“We are not aware of observational tensions with this model within current uncertainties”), §VIII A (“fully consistent with both [bounce and inflation]”), §IX E (ALP birefringence 0.77σ difference, “well within observational uncertainty”), etc.  
- **Issue:** These sentences use qualitative phrases (“no tensions”, “fully consistent”, “well within”) without *always* giving the underlying numerical deltas and σ. In §VIII A you do give the 0.75σ distance, but in §II D and §IX E the same style appears without explicit numbers nearby. Given the level of rigor elsewhere, this stands out as weaker.  
- **Required fix:** Wherever you say “consistent with”, add the difference in σ or χ² explicitly, even if trivial (e.g. “no current data exclude the model at better than 1σ in any channel we have checked”). For the ALP case, keep the 0.77σ number but avoid language like “well within” unless you add the concrete σ comparison in the same sentence.

---

P2-M21 (MINOR) – INTERNAL CROSS‑REFERENCE ON “FULL §VII BUDGET” VS. WHAT IS ACTUALLY MODELED  
- **Location:** Abstract (“combined systematic budget… noise‑weighted shape mismatch, ϵ correction, null‑space scatter… photometric‑z, PNG bias, bϕ, relativistic projection uncertainties”), §VII (A–D).  
- **Issue:** §VII does *discuss* all these systematics qualitatively, but only some are folded into explicit σ numbers (bϕ via Fig. 5; GR via Table III; photo‑z via one quoted 5% degradation; anomaly shot noise is clearly flagged as not included). The abstract’s phrase “combined systematic budget” suggests a single joint marginalization has been performed, which it has not—you essentially stack individually estimated degradations.  
- **Required fix:** Rephrase “combined systematic budget” to “stacked estimate of several leading systematics, each treated separately” and in §VII make clear which effects are actually combined into the numerical 3–5σ band and which are only noted qualitatively. This avoids implying a full joint Fisher‑level marginalization that has not yet been done.

If you want, I can next go through specific tables/figures one‑by‑one (σ and percentages) and write an explicit arithmetic checklist you can use while revising.