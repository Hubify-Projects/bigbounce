# P2 R35conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.56.pdf` md5=bd702ba5 pages=27
**Input format**: TEXT + web search + pass-2 self-critique (11794 chars)
**Wall time**: 104.5s

---

Chaussidon et al. 2024 is cited correctly and the DESI DR1 statistics in the abstract/body are now accurate and consistent with that paper; I do not see metadata or numerical regressions tied to this replacement. Below I give the full forensic report.

---

## Overall assessment

The submission is extremely long (27 pages main text plus extensive appendices) relative to what it actually *computes* (a one-parameter recast of an existing SPHEREx Fisher matrix plus an extensive narrative of systematics and priors). For PRD I would recommend compressing to ≲15–18 pages by moving large parts of Secs. VI–IX and Appendix A to a shorter, more focused presentation.

Numerically and citation-wise, the paper is unusually careful; most quoted numbers track back correctly. However, there are several **ESSENTIAL** issues:

- some claims of forecast significance and Bayes factors are not explicitly tied to a single, self‑consistent parameter set but instead to a shifting mix of “baseline”, “post‑systematic”, and “optimistic” assumptions;
- the current manuscript does not always label sigma values from different null/systematics procedures as *not directly comparable* when juxtaposed, as required in your instructions;
- there are a few inconsistencies and untraceable or misleading statistical claims in the Bayesian model comparison section;
- some “current data” and “birefringence” statements go beyond what is warranted by the cited references.

I also checked the **Chaussidon et al. 2024** replacement explicitly:

- The paper cited as *Chaussidon et al., Constraining Primordial Non-Gaussianity with DESI 2024 LRG and QSO samples* corresponds to arXiv:2411.17623.[1][9]
- That paper indeed reports, combining LRG+QSO, \(f_{\rm NL}^{\rm loc} = -3.6^{+9.0}_{-9.1}\) (68% C.L.) under the stated bias assumptions.[1][9]
- The manuscript now summarizes DESI DR1 constraints as “σ ≈ 9–10” and quotes the central value −3.6 with ±9.0/9.1, consistent with Chaussidon et al.[1][9]
- No stale reference to “DESI DR1 f_NL sentence” remains, and there is no mismatch between the quoted numbers and Chaussidon’s abstract or tables.[1][9]

So the EXT5 change is correct and internally consistent.

Below I list all findings systematically.

---

## ESSENTIAL issues

### P2‑E1: Mixed σ values / comparability

- **Location:** Abstract & Sec. IV and VII (pp. 1, 8–10, 14–17)
- **Problem:** The abstract and body place multiple significance ranges side‑by‑side – e.g. “5.2–5.5σ optimistic and ∼2.6–5σ realistic,” and in Fig. 2 multiple bars (6.25σ, 5.2–5.5σ, 2.6–5σ, 2.6–2.8σ) – that derive from *different* combinations of systematics, priors, and template overlaps, without **explicitly and repeatedly** stating that these σ values are not directly comparable as null‑test outcomes (they come from different σ_eff and nuisance treatments).
- **Why it matters:** Per instruction (7), distinct null procedures or different systematic budgets must be clearly flagged as non‑comparable wherever juxtaposed. Here the reader can easily misinterpret the span 2.6–7σ as a single forecast uncertainty band rather than as disjoint scenarios.
- **Required fix:**  
  - At every place where multiple σ ranges are juxtaposed (abstract; Fig. 2 caption; Sec. IV “headline forecast” paragraph; Sec. V “3–7σ envelope”), add explicit language such as:  
    *“These σ values are derived from different assumptions about GR projection, PNG bias priors, and template overlap and are not directly comparable as a single null‑test significance; they represent separate scenarios.”*  
  - In the abstract, reduce to one clearly defined “baseline” σ with an explicit description of what is included in σ_eff, and mention other values only as separately labeled limits.

### P2‑E2: Bayesian evidence vs. priors not cleanly separated

- **Location:** Sec. VI.C (pp. 11–13), Table II (p. 15), Table III (p. 18), Fig. 6 (p. 20)
- **Problem:**  
  - The Bayes factors are correctly computed for the choices you state, but the text often slides between different prior choices (broad [−15,15] multifield, “curvaton‑natural” [−5,5], delta vs. σ_theory) and two different “bookkeepings” of r (r→1 vs. r≈0.84) within a single narrative. While the details are there, the main claims (“BF ≈ 9–14”, “BF ∼ 10–17 at r→1”) are not anchored to a single, clearly labeled parameter set, and the reader has to reconstruct ex post which priors were implied.
  - This is borderline for PRD: any headline Bayes factor must be tied to one explicit model pair and prior choice. At present, the text highlights high BF values which rely on somewhat optimistic priors (broad competitor prior, relatively narrow bounce prior) without always stating that a more conservative, physically motivated choice would lower BF substantially.
- **Required fix:**  
  - Choose **one** “baseline” model pair (e.g. bounce with σ_theory=1 Gaussian prior vs. curvaton‑natural competitor [−5,5]) and report that BF as the main text value, with all other choices moved to a “prior sensitivity” subsection.
  - In the abstract, remove the two‑number “BF ≈ 9–14” that conflates r→1 and r≈0.84 and different competitor priors. Instead, say explicitly e.g.:  
    *“For a σ_theory=1 Gaussian prior on the bounce prediction and a broad multifield competitor prior [−15,15], a SPHEREx detection at f_NL≈−4.4 with σ=0.7 would yield a Bayes factor BF≈10; narrower, curvaton‑motivated competitor priors reduce this to BF≈4–7.”*  
  - Everywhere Bayes factors are quoted, explicitly state the assumed (i) bounce prior (delta vs. Gaussian width), (ii) competitor prior range, and (iii) whether r→1 or r≈0.84 bookkeeping is being used. Make sure the abstract uses only one, clearly specified combination.

### P2‑E3: “Birefringence consistency” overreach vs. cited sources

- **Location:** Sec. IX.E.a (p. 21)
- **Problem:** You state that “bounce‑motivated physics allows for a spectator ALP coupling that predicts cosmic birefringence β ≈ 0.27°” and then describe this as “0.77σ from the Eskilt & Komatsu measurement β_obs=0.342°±0.094°”. Eskilt & Komatsu 2022 indeed quote β≈0.342°±0.094°. However:
  - There is no reference in the text to a specific bounce‑ALP model that predicts 0.27°; this looks like either an ad hoc number or from an unpublished calculation.
  - The arXiv or journal record for the cited birefringence papers  does **not** contain this bounce‑based prediction or this 0.77σ comparison; you give no derivation or parameter set.
  - Thus the “0.77σ from β_obs” is an unsupported quantitative statement.
- **Required fix:**  
  - Either (a) remove this paragraph entirely, or (b) clearly label the 0.27° as a *toy* value (“for illustration only”), not as a bounce prediction, and **do not** attach a σ‑distance to real data unless you provide an explicit formula, parameter set, and calculation in the text or appendix with clear citation.  
  - In either case, the phrase “the bounce prediction is 0.77σ from the Eskilt & Komatsu measurement” must be removed or rewritten to something non‑quantitative like “it would be straightforward to construct bounce‑motivated ALP spectra compatible with current birefringence constraints”.

### P2‑E4: Abstract‑body consistency and emphasis

- **Location:** Abstract vs. Secs. IV–VII
- **Problem:** Abstract claims:
  - “We adopt the bispectrum‑only 5.2–5.5σ optimistic and 2.6–5σ realistic ranges as the headline forecast.”
  - “MegaMapper … could reach σ(fNL) ≈ 0.5 ideally, projecting an illustrative 3–7σ envelope…”
- These “headline” statements omit the fact that:
  - The 5.2–5.5σ assumes no GR degradation and effectively fixed b_φ;  
  - The lower end of 2.6σ folds in b_φ degradation and GR into σ_eff;  
  - The “3–7σ envelope” for MegaMapper is not a single forecast but a mix of idealized (σ=0.5), degraded (σ≈0.7–1.0), and different b_φ prior assumptions.  
- This violates the ABSTRACT‑LAST check: the abstract implies a level of robustness that is frankly more optimistic than the body’s more cautious discussion in §VII.
- **Required fix:**  
  - Rewrite the abstract’s σ statements to map one‑to‑one onto a clearly defined baseline scenario. For example:
    - “Using the Heinrich et al. SPHEREx bispectrum Fisher matrix (σ(f_NL^loc)=0.7) and our shape overlap r≈0.83, the nominal matter‑bounce signal would correspond to ≈5.3σ before accounting for GR projection and PNG‑bias uncertainties; under a conservative systematic budget these reduce to ≈3σ, and a broader range 2.6–5σ brackets plausible survey/systematics scenarios discussed in the text.”
  - Similarly, for MegaMapper, explicitly say that “3–7σ” is not a forecast band but a design‑space envelope, and tie “7σ” only to the ideal σ=0.5, fixed‑b_φ, no‑GR case.

### P2‑E5: Standalone‑reader test – heavy dependence on external forecast without minimal re‑derivation

- **Location:** Sec. IV (pp. 8–10)
- **Problem:** The σ(f_NL)=0.7 SPHEREx number, crucial for all your conclusions, is taken entirely from Heinrich et al. (2024) with no minimal reproduction of the essential scaling or any reduced Fisher expression in the paper. You do mention that you do not recompute their Fisher matrix and that this is a “sensitivity recast”, but a PRD methods paper should at minimum give:
  - The explicit parameter vector and Fisher expression being adopted;
  - A consistency check (e.g., approximate scaling with volume, bias, and k_max) to show the 0.7 number is in the right ballpark.
- **Required fix:**  
  - Add a short subsection explicitly writing the Heinrich et al. bispectrum Fisher expression you reuse (even if schematic), the parameter set, and the redshift and k ranges.  
  - Provide at least one simple sanity check: for example, show that if you scale SPHEREx volume or number density by a factor, your resulting σ(f_NL) scales as expected from the Fisher integrand, even if you do not regenerate their exact 0.7.  
  - Clarify in the abstract and introduction that this is a **recast** that depends quantitatively on Heinrich et al.’s forecast being correct.

---

## MAJOR issues

### P2‑M1: Length / redundancy

- **Location:** Whole paper, especially Secs. VI–IX and Appendix A (pp. 11–25)
- **Problem:** For the claimed contribution (a single‑parameter recast of an existing Fisher forecast plus a polynomial‑basis analysis of template overlap), the current 27 pages are excessive. Large blocks are narrative explanations and prior‑sensitivity catalogues that can be compressed without loss of scientific content, in particular:
  - Repeated explanations of r, r_cos, and multiple scans over radii and weighting schemes;
  - Many paragraphs in VI.C about Bayes factors that restate the same prior‑sensitivity message;
  - Repeated caveats in VII–IX that could be consolidated.
- **Required fix:**  
  - Condense Sec. VI into a single clear baseline comparison plus one “prior sensitivity” paragraph; move detailed prior grids (Table II) to an appendix.  
  - Compress the discussion of null‑space scans and template overlap; once you have established r≈0.84±0.02 and r_cos>0.97 across your scan, you do not need multi‑page elaboration.  
  - Aim to bring the main text to ≲15–18 pages.

### P2‑M2: Joint (f_NL, n_fNL) forecast – traceability of numbers

- **Location:** Sec. X.D (pp. 20–21)
- **Problem:** You quote specific joint Fisher results for SDB: σ(n_fNL)=0.295/0.596, σ_marg(f_NL)=3.08/7.06 with correlations ρ=-0.87 / -0.969. There is no explicit equation showing how the (f_NL, n_fNL) parameterization enters the scale‑dependent bias, and no reference reproduces these exact numbers. You mention a code and claim consistency with Dore et al., but a reader cannot verify the formulas.
- **Required fix:**  
  - Add explicit formulas showing how n_fNL enters ∆b(k,z), e.g. \(f_{\rm NL}(k)=f_{\rm NL}(k_\ast)(k/k_\ast)^{n_{f_{\rm NL}}}\), and how derivatives w.r.t. f_NL and n_fNL enter the SDB Fisher.  
  - Add a brief scaling check comparing your σ(f_NL) (fixed n_fNL) to a known forecast (e.g. Dore et al.) to justify that your implementation is sound.  
  - Clarify that these SDB joint constraints are *secondary* and are not used in headline forecasts, to avoid confusion.

### P2‑M3: Use of “≫1” Bayes factors vs. SSFSR without specifying priors

- **Location:** Table II “BF vs. SSFSR” (p. 15), Table III (p. 18), Sec. VI
- **Problem:** You state BF vs standard single‑field slow‑roll inflation “≫1” and sometimes as large as >10^5, but do not explicitly specify the prior on SSFSR parameters – effectively you treat SSFSR as a point prediction f_NL≈0.015. That assumption is reasonable, but for PRD it should be unambiguously stated (e.g., “we treat SSFSR as a delta prior at f_NL=0.015”), otherwise BF magnitudes are ambiguous.
- **Required fix:**  
  - Explicitly state in Sec. VI and under Tables II–III the prior used for SSFSR (delta at the Maldacena prediction, no spread).  
  - Clarify that the enormous BF vs SSFSR is somewhat tautological in that sense, and not the main scientific discriminator; emphasize the bounce vs multifield comparison instead.

---

## MINOR issues

### P2‑m1: Chaussidon et al. 2024 citation

- **Location:** Sec. VIII.A (p. 17)
- **Problem:** You now correctly cite Chaussidon et al. for DESI DR1 PNG constraints.[1][9] Two small issues:
  - You say “DESI DR1 LRG and QSO analyses report combined f_NL^loc bounds at σ≈9–10 (… from LRG; … from QSO assembly bias).” Chaussidon’s combined LRG+QSO central result and uncertainties agree with this, but that paper is *not* titled “sample preparation and validation” as hinted (that sounds like an internal DESI support paper); its actual title is “Constraining primordial non-Gaussianity with DESI 2024 LRG and QSO samples”.[1][9]
- **Required fix:**  
  - Make sure the reference entry matches Chaussidon’s actual title, author list, and arXiv ID 2411.17623; avoid mixing in titles of DESI blinding/validation internal papers.[1][9]

### P2‑m2: “Launched March 2025” statements

- **Location:** Abstract; Sec. IX.A (pp. 1, 20)
- **Problem:** You assert “SPHEREx (launched March 2025…)”; at the time of writing, SPHEREx was planned for launch around 2025, but “launched March 2025” is a future‑specific statement that might not match reality at publication.
- **Required fix:**  
  - Replace with conditional language: “SPHEREx, planned for launch in mid‑2020s…” or similar and remove exact month/year.

### P2‑m3: “We are not aware of observational tensions” – needs clearer basis

- **Location:** Sec. II.D (p. 7)
- **Problem:** You say, “We are not aware of observational tensions with this [Wilson‑Ewing] model within current uncertainties.” The cited Wilson‑Ewing paper is a theoretical LQC toy model; there is no explicit combined likelihood test vs cosmological data. This sentence is mildly stronger than warranted.
- **Required fix:**  
  - Soften to: “We are not aware of any published analysis demonstrating decisive tension between this model and current data, but a full joint likelihood analysis has not been carried out.”

### P2‑m4: Data/code availability – repository permanence and versioning

- **Location:** “Data and code availability” section (p. 22)
- **Problem:** You promise a Zenodo DOI “inserted at submission” and specify a GitHub path with deep directory structure. For PRD, it is better to (i) give a frozen release tag, (ii) ensure that notebook and JSON filenames in the text match exactly.
- **Required fix:**  
  - At acceptance, ensure that:  
    - a Zenodo DOI is actually present,  
    - the GitHub repo has a release tag corresponding to the paper version,  
    - the filenames referenced in the text (e.g., `c9g_bf_table_recompute.py`) match those in the repo.

---

## NIT (cosmetic) issues

### P2‑n1: Minor typographical errors

- Example instances:
  - p. 2: “mechanism-independent” is placed in quotes appropriately; fine but a bit overused – consider cutting one or two occurrences.
  - p. 9: “p∼ 19% degradation in σ(fNL)” – missing space or better write “∼19%”.
  - p. 15: In Table II caption, “lower-bound and point-hypothesis dependent” → “lower‑bound and point‑hypothesis‑dependent”.
- **Fix:** Standard copy‑editing.

### P2‑n2: Repeated clarifications about DBI

- **Location:** Secs. IV, VII.D (pp. 9–10, 20–21)
- **Problem:** Multiple paragraphs state that DBI has equilateral shape and is not constrained by local estimators. This is true but somewhat repetitive.
- **Required fix:**  
  - Condense to a single clear statement in one section and refer there.

### P2‑n3: Occasional very long sentences

- Many sentences span 4–6 lines with multiple parenthetical clauses; this harms readability.
- **Fix:** Break especially long sentences into 2–3 shorter ones, particularly in Sec. II.C and VI.C.

---

## Bibliography and citation forensics

I checked all *load‑bearing* references:

- Maldacena 2003 (JHEP 0305, 013, astro‑ph/0210603) – correctly cited.[2]
- Planck 2018 cosmological parameters paper (A&A 641, A6, 2018, arXiv:1807.06209) – ns value is correctly used.[3]
- Cai et al. 2009 “Non‑Gaussianity in a matter bounce” JCAP 0905:011, arXiv:0903.0631 – f_NL=−35/8 in their normalization is correctly quoted.
- Li et al. 2017 “Matter bounce cosmology with a generalized single field” JCAP 2017(3):031, arXiv:1612.02036 – their f_NL=−35/16 intermediate is correctly described as a single‑time‑ordering result.[7]
- Heinrich et al. 2024 SPHEREx bispectrum forecast: Phys. Rev. D 109, 123511; arXiv:2311.13082 – σ(f_NL^loc)=0.7 bispectrum‑only is correctly quoted.[6]
- Schlegel et al. 2022 MegaMapper white paper: arXiv:2209.04322 – stage‑V σ(f_NL)≈0.5 is consistent with their forecasts.
- Chaussidon et al. 2024 DESI DR1 PNG: arXiv:2411.17623 – f_NL^loc = −3.6^{+9.0}_{−9.1} is correctly used; you approximate this as σ≈9–10.[1][9]
- Jung et al. Planck PR4 PNG: A&A 702, A204 (2025) – consistent with your PR4 numbers (f_NL=−0.1±5.0).
- Eskilt & Komatsu 2022 birefringence; Cosmoglobe 2023; ACT 2025 – the β values you quote match those papers qualitatively, but see P2‑E3 above for over‑interpretation.

No obvious fake arXiv IDs or “in preparation” placeholders are present. No duplicate bibliography entries were found.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core technical idea (recasting SPHEREx bispectrum forecasts for a matter‑bounce bispectrum with careful template overlap and systematics discussion) is interesting and, with corrections, could meet PRD standards. However, the current version requires (i) consolidation and explicit labeling of different significance regimes, (ii) a more disciplined and clearly parameterized treatment of Bayes factors and priors, (iii) removal or softening of a few over‑strong or loosely supported claims (especially the birefringence “0.77σ” remark), and (iv) substantive reduction in length and redundancy. Once these are addressed, the paper will be clearer, more rigorous, and more suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P2‑E6: Additional mixed‑σ / comparability problems beyond those already flagged
- **Location:** Sec. IV, Fig. 2 caption and text around it (pp. 9–10)
- **Problem (new):** In Fig. 2 and the surrounding text, four SPHEREx σ‑regimes are juxtaposed as if they were points on a single axis:  
  - 6.25σ “naive” (no template mismatch, σ = 0.7)  
  - 5.2–5.5σ “template‑corrected optimistic” (r = 0.83–0.876, no GR or bϕ)  
  - “∼3.0σ” “GR‑only floor” (σGR = 1, but still fixed bϕ universality)  
  - “∼2.6–2.8σ” “all‑combined endpoint” (GR + bϕ + other systematics, σeff ≈ 1.35–1.41)  
  They are plotted and described as a single ladder of “detection significance,” but they correspond to different effective σ(fNL), different nuisance priors, and different choices of what is folded into σ_eff. The caption does not explicitly say that these outcomes come from mutually exclusive, non‑comparable null procedures.
- **Why it matters:** It is easy for a reader to read Fig. 2 as one continuous forecast band, rather than as separate, incompatible modeling choices. This is exactly the comparability issue your instructions warned against.
- **Required fix:**  
  - In the Fig. 2 caption and the main‑text paragraph describing the figure, add an explicit qualifier, e.g.:  
    *“Each bar corresponds to a different set of assumptions about GR projection, PNG‑bias priors, and template mismatch. These σ values are not directly comparable as a single null‑test; they represent separate, mutually exclusive scenarios.”*  
  - Consider visually separating the scenarios (e.g. grouping “naive”, “template‑only”, “GR‑only”, “all‑combined” with different hatching) and explicitly labeling σ_eff for each.

---

P2‑E7: Quadrature combination of heterogeneous “systematics” is not consistently defined
- **Location:** Abstract; Sec. IV (pp. 1, 8–10); Sec. VII.A–C (pp. 15–18)
- **Problem (new):**
  - In multiple places you say “these systematics are combined additively in quadrature,” listing ingredients that are not all uncertainties on the *same underlying mean* and in some cases are not strictly random quantities. For example, Sec. IV combines:  
    - template mismatch (a fixed multiplicative r)  
    - ϵ‑correction “uncertainty” (a shift in the true fNL, not σ(fNL))  
    - polynomial‑null‑space scatter (scatter in r when you change the *theory* representation, not a survey noise term)  
    - photometric‑z degradation (a change in survey σ(fNL))  
    - bϕ prior widening (a prior‑driven σ change)  
    - GR projection nuisance σGR  
  - These are conceptually distinct: some are biases in the prediction, some are multiplicative re‑scalings, some are survey‑noise degradations, some are prior widths. Treating them as if they were independent Gaussian errors all entering a single σ_eff is not rigorously justified, yet the text presents the quadrature as if it were a well‑defined statistic (e.g. the specific use of \(\sqrt{0.7^2+1.0^2}\) in the 3.0σ “GR‑only floor”).
- **Why it matters:** PRD expects clarity about what is being treated as an “error bar.” At present it is unclear (i) which effects are modeled as shifts of the mean fNL vs. broadening of σ(fNL), (ii) whether the quadrature σ_eff that sets “2.6–5σ” is uniquely defined, and (iii) how double counting is avoided.
- **Required fix:**  
  - Introduce an explicit decomposition in Sec. IV or VII:  
    \[
      f_{\rm NL}^{\rm pred} \to f_{\rm NL}^{\rm pred} + \delta f_{\epsilon} \pm \sigma_{\rm theory},\quad
      \sigma_{\rm survey}\to \sigma_{\rm survey}^{\rm (inst)}\oplus\sigma_{b_\phi}\oplus\sigma_{\rm GR}\oplus\cdots
    \]  
    and state exactly which items are treated as biases on the mean and which as contributions to σ_eff.  
  - For the “2.6–5σ realistic” and “3.0σ floor” numbers, write out the formula for σ_eff and list its components numerically in one place.  
  - Clarify that this quadrature is a heuristic scoping device, not a rigorously derived combined error, and remove phrases that could be read as implying a unique, covariance‑level construction.

---

P2‑E8: Joint (fNL, n_fNL) forecast – dimensional consistency and missing definition of n_fNL
- **Location:** Sec. VII.D (pp. 20–21)
- **Problem (new):**
  - You define \(n_{f_{\rm NL}} \equiv d\ln|f_{\rm NL}|/d\ln k\) only briefly and then immediately quote Fisher errors \(\sigma(n_{f_{\rm NL}}) = 0.295, 0.596\), \(\sigma_{\rm marg}(f_{\rm NL})\), and correlation coefficients. However, nowhere in the main text is there an explicit equation for how this running feeds into the observable scale‑dependent bias \(\Delta b(k,z)\). The reader is told the numbers but not given the forward model.  
  - You say the matter‑bounce prediction is \(n_{f_{\rm NL}} = 0\) “exact scale invariance in the squeezed limit” while earlier you emphasize that the shape is *not* exactly local and that there is ϵ‑dependent shape variation. The text never clarifies whether your SDB Fisher actually uses a strictly local ansatz \(f_{\rm NL}(k) = f_{\rm NL}(k_*) (k/k_*)^{n_{f_{\rm NL}}}\) or some modified bounce‑motivated shape.
- **Why it matters:** Without the explicit model, the quoted joint errors are not traceable. Dimensional consistency (units of k, choice of pivot k*, etc.) also cannot be checked.
- **Required fix:**  
  - Add a short subsection or paragraph with explicit equations: e.g.  
    \[
      f_{\rm NL}(k) = f_{\rm NL}(k_\ast)\left(\frac{k}{k_\ast}\right)^{n_{f_{\rm NL}}},\quad
      \Delta b(k,z)\propto \frac{f_{\rm NL}(k)\,b_\phi}{M(k,z)}.
    \]  
    and specify the pivot \(k_\ast\), the k‑range used, and whether you treat the shape as strictly local in this calculation.  
  - State explicitly that in the forecast you set \(n_{f_{\rm NL}}=0\) for the quasi‑dust bounce, and that all quoted \(\sigma(n_{f_{\rm NL}})\) are around that fiducial.  
  - Make clear that these SDB joint constraints are methodologically separate from, and weaker than, the Heinrich bispectrum forecast, to prevent readers from conflating the two baselines.

---

P2‑M4: Arithmetic / propagation inconsistencies in null‑space significance example
- **Location:** Sec. II (pp. 3–5)
- **Problem (new):**
  - You state that for the 10,000 null‑space coefficient samples, the 16th–84th percentile range of pre‑systematic |fNL| r/σ(fNL) at σ = 0.7 is 4.4–6.2σ, with median 5.3σ, and that pushing these through the “conservative GR‑marginalization budget (σGR = 1.0 in quadrature with σ(fNL) = 0.7)” maps the 16th percentile 4.4σ to “≈2.5σ, … consistent with the ∼2.6–2.8σ all‑combined endpoint.”
  - Numerically, if one simply does what is written — combine σ = 0.7 and σGR = 1.0 in quadrature and rescale the significance:
    \[
      \sigma_{\rm eff} = \sqrt{0.7^2 + 1.0^2} \approx 1.22,\quad
      S_{\rm new} = 4.4 \times \frac{0.7}{1.22} \approx 2.5,
    \]
    which matches the 2.5σ number. But “all‑combined 2.6–2.8σ” in Sec. IV and Fig. 2 uses a *larger* σ_eff (you quote √(0.9² + 1.0²) ≈ 1.35–1.41), so the same 4.4σ baseline fed through that should give ≲2.3σ, not “consistent with 2.6–2.8σ.”
- **Why it matters:** The text blends two different σ_eff constructions (“GR‑only” vs “all‑combined”) and then asserts consistency between them. This conflation obscures what σ_eff underlies the final 2.6–2.8σ endpoint.
- **Required fix:**  
  - Cleanly separate:  
    - the GR‑only mapping (σ_eff = √(0.7² + 1.0²), giving ~2.5σ for the 4.4 baseline), and  
    - the all‑combined mapping (σ_eff ≈ 1.35–1.41, which would give ≲2.3σ for the same 4.4 baseline).  
  - Remove or qualify the statement that 2.5σ is “consistent with the ∼2.6–2.8σ all‑combined endpoint”; either show the explicit arithmetic for the coefficient set that yields the 2.6–2.8σ endpoint, or restrict that comparison to the GR‑only floor.  
  - In one place (e.g. Sec. IV), provide a table or equation set that defines the exact σ_eff used for each of: “GR‑only floor”, “all‑combined endpoint”, and “null‑space 16th percentile mapping.”

---

P2‑M5: Abstract‑body mismatch about SPHEREx launch timeline persists
- **Location:** Abstract; Sec. IX.A and Conclusion (pp. 1, 20, 22)
- **Problem (new):** In several places you still write as if the SPHEREx launch and survey milestones are fixed facts (“launched March 2025”, “first all‑sky survey completed December 2025”), even while the rest of the paper treats forecasts and future data releases. At publication time these specific months may already be wrong.
- **Why it matters:** For a PRD paper intended to have a long shelf‑life, hard‑coded calendar months for future events are undesirable unless they are already in the past at acceptance.
- **Required fix:**  
  - Everywhere you have “launched March 2025”, “completed December 2025”, etc., replace with neutral phrasing such as “planned for launch in the mid‑2020s” and “expected to complete its primary all‑sky survey within ~2–3 years” without specific months.  
  - Ensure the Conclusion and Sec. IX.A are updated consistently, not only the abstract.

---

P2‑m5: Minor arithmetic / rounding issue in DBI robustness paragraph
- **Location:** Sec. X (Conclusion), first paragraph
- **Problem (new):** You say that if one (incorrectly) used Li et al.’s −35/16 value, the “pre‑systematic raw ratio” drops to “≈3.1σ” and “post‑budget to ∼1.5–2.5σ.” The pre‑systematic figure corresponds to |−35/16|/0.7 = 2.1875/0.7 ≈ 3.125σ, which is fine. But the earlier, correct Cai value 4.375/0.7 = 6.25σ is often referred to as “6.25σ” exactly, while 3.125σ is rounded inconsistently (sometimes “3.1σ”, sometimes “3.2σ” depending on context).
- **Why it matters:** This is minor, but for a paper that leans heavily on numerical significance, using a consistent rounding convention strengthens the impression of care.
- **Required fix:**  
  - Choose a consistent rounding scheme (e.g. two significant figures) and apply it to all headline σ values derived from simple ratios, including the 3.125σ Li intermediate. For example, always present it as “3.1σ” everywhere.

---

P2‑n4: Residual overstatement of “no tensions” with current data
- **Location:** Sec. II.D (p. 7), Sec. VIII.A (p. 18)
- **Problem (new):**
  - In II.D you now soften to “We are not aware of observational tensions… but a full joint likelihood analysis has not been carried out.” However, in VIII.A you still write that Planck PR4 recast is “0.75σ from the bounce prediction and 0.02σ from zero—fully consistent with both,” and that DESI DR1 is “far too weak to discriminate” but do not quantify how likely a future σ≈0.7 measurement at −4.4 would be under the inflation prior.  
  - The phrase “fully consistent with both” is factually true at 0.75σ, but it subtly suggests symmetry between the bounce and inflation hypotheses, while the prior volume for fNL in inflationary models is tightly peaked near zero.
- **Why it matters:** This is an interpretational hedge that could be seen as downplaying that current data weakly *prefer* fNL≈0 over −4.4, even if the preference is not statistically meaningful.
- **Required fix:**  
  - Rephrase to something like: “The recast Planck PR4 constraint is only 0.75σ away from the bounce prediction and 0.02σ from zero, so current CMB data are statistically consistent with both scenarios and do not meaningfully discriminate between them.”  
  - Make explicit that the present Bayes‑factor analysis and forecasted discrimination are forward‑looking; current data modestly favor fNL≈0 but at a level that does not warrant strong conclusions.

---

If you want, I can next go through the figures and equations one by one against your LaTeX source to systematically tick off (A) arithmetic on every reported σ and ratio and (C) dimensional consistency line‑by‑line; that would require the actual compiled tables/figures rather than the narrative text alone.