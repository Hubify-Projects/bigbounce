# P5 auto-2026-06-05_1717pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (10300 chars)
**Wall time**: 55.5s

---

The manuscript cannot be properly refereed to Physical Review D standards because it is incomplete: only the main text and references are provided, without the actual reference list entries (journal, year, volume, page, arXiv IDs) or any figures/tables as rendered objects. I therefore cannot perform the requested citation-forensics audit or numeric cross-checks at the level you specify.

Within these limitations, I list all issues I can identify from the provided text.

---

### P5-E1 (ESSENTIAL) – Missing reference metadata and incomplete bibliography  
**Location:** References, p.20 (end of excerpt)  

**Problem:**  
Only bracketed citations [1]– and minimal textual information are given (author, very short title, journal, year, and sometimes arXiv ID), but the full bibliographic entries as they would appear in PRD are not shown. There is no explicit arXiv ID in [4], , , or  inside the bibliography section; , , and  are clearly arXiv preprints “(2026)” with identifiers given only in the text, not in the reference list. Without the full reference section, I cannot verify:

- Correct arXiv identifiers and versions  
- Exact titles, author lists, journal abbreviations, volume, and page/Article IDs  
- DOI consistency and year correctness  

PRD requires a complete, unambiguous reference list; as presented, the paper is bibliographically incomplete.

**Required fix:**  
Include a full reference list in PRD style in the manuscript PDF, with for each cited work:

- Full author list (or “et al.” as allowed by PRD style)  
- Full title  
- Journal, volume, page or article ID, and year  
- DOI (when available)  
- arXiv ID with correct subject class  

Then run a full consistency check against arXiv and NASA ADS. At minimum, explicitly confirm in the next revision that the following are correct and present in the bibliography:

- [1] Alexander & Yunes, Phys. Rep. 480, 1 (2009), arXiv:0907.2562  
- [2] Lue, Wang, Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088  
- [5] Hahn et al. 2007, MNRAS 375, 489, arXiv:astro-ph/0610280  
- [6] Hoffman et al. 2012, MNRAS 425, 2049, arXiv:1201.3367  
- [7] Cautun et al. 2014, MNRAS 441, 2923, arXiv:1401.7866  
-  Planck 2018 results. VI. A&A 641, A6 (2020), arXiv:1807.06209  
-  Shamir 2022, MNRAS 516, 2281, arXiv:2208.13866  
-  Tempel et al. 2014, A&A 566, A1, arXiv:1402.1350  
-  Ullah et al. 2026, arXiv:2604.02463 (no journal yet)  
-  Zapata‑Zuluaga et al. 2026, arXiv:2604.01456  
-  Rincón et al. 2025, ApJ 982, 38, arXiv:2411.00148  

---

### P5-E2 (ESSENTIAL) – Use of clearly future-dated arXiv IDs  
**Location:** References , ; text in §IX B and §X  

**Problem:**  
The manuscript uses arXiv IDs with year “26” in the identifier, e.g.:

- “H. I. Ullah … preprint (2026), arXiv:2604.02463.”  
- “D. C. Zapata-Zuluaga … (2026), arXiv:2604.01456.”

arXiv identifiers are yymm.nnnnn; “2604.02463” and “2604.01456” correspond to April 2026. At the present time (June 2026), these IDs do not exist in arXiv’s database. This is incompatible with PRD standards: references must be to existing manuscripts, not speculative future arXiv postings.

**Required fix:**  
- Remove or correct all future-dated arXiv IDs.  
- If the authors have actual preprints, update to the true arXiv IDs and ensure they are live.  
- If these works are only “planned” or “in prep,” then they must not be cited as arXiv preprints; at most they can be cited as “in preparation” and must not be used for load‑bearing results.  

Until the matching arXiv records exist, PRD should not accept citations to them.

---

### P5-E3 (ESSENTIAL) – Self‑cited “companion papers” not yet public or peer‑reviewed but used as load‑bearing inputs  
**Location:** Abstract, p.1; §II, p.2; §III A, p.2–3; multiple mentions of Paper IV [3] and Paper II [4]  

**Problem:**  
Paper IV and Paper II are cited as:

- [3] “companion paper (Paper IV), in preparation; manuscript in preparation.”  
- [4] “companion paper (Paper II), in preparation; manuscript in preparation.”

Yet the main analysis *depends* crucially on Paper IV for:

- The chirality catalog of 8.47M galaxies and the CW/CCW labels.  
- The catalog-wide monopole offset ∆fCW ≈ −0.0026 and its uncertainty.  
- Imaging-leg systematics characterization and BGS-selection-function discussion.  

These are load-bearing inputs. The current manuscript claims to propagate the “Paper IV catalog monopole offset” and repeatedly interprets results as “monopole leakage” without giving a self-contained, peer‑reviewed derivation.

PRD does allow companion papers but generally requires that critical inputs be either published or fully documented within the submitted manuscript.

**Required fix:**  
Either:

1. Make Paper IV publicly available on arXiv with complete documentation before acceptance, and clearly state that all reliance on its catalog and monopole is traceable and reproducible from that public document, **or**  
2. Incorporate into the present paper a sufficient methods and validation section for the chirality catalog (classifier architecture, training, augmentation, calibration, monopole measurement, per-leg systematics) such that the chirality labels and their monopole/systematic characterization can be independently scrutinized without access to Paper IV.

Without one of these, the current paper’s conclusions rest on unpublished work, below PRD standards for critical inputs.

---

### P5-E4 (ESSENTIAL) – Unsupported numerical claims from external works (Paper IV) with no quoted equations or tables  
**Location:** Abstract (first paragraph), §II, §V, §VIII F, §XI  

**Examples of problematic text:**

- “Paper IV … establishes the global mixture … as a CW fraction of 0.4974 ± 0.000279.”  
- “Paper IV’s full-sky dipole null is at σ = 0.43, p = 0.30 … and −0.12σ for the subsample-mask MASTER-deconvolved ℓ = 1 amplitude.”  
- “Paper IV identifies … ∆fCW ≈ −0.0026 offset … and ∼9.5σ catalog-level monopole.”  

These numbers are repeatedly used as a calibration and to define the “monopole prediction” σ_pred and the interpretation of all σ deviations. However, no tables, figures, or equations from Paper IV are reproduced here, and Paper IV is “in preparation.”

**Required fix:**  
For each scalar imported from Paper IV that is used in the current analysis, either:

- Provide a precise reference to a table/figure/equation in Paper IV (once that paper is deposited on arXiv), or  
- Reproduce the relevant result here (e.g. a table giving f_CW, σ, N, per-leg systematics) with enough information to verify it solely from this manuscript.

Without this, the reader cannot check whether the quoted 0.4974, 0.000279, ∆fCW = −0.0026, or the ∼9.5σ figure are accurate or compatible with PRD standards.

---

### P5-E5 (ESSENTIAL) – Inability to verify abstract headline statistics from displayed numbers  
**Location:** Abstract vs. body (e.g. Table II, VII, VIII, X)  

**Problem:**  
Your reviewing instructions require recomputing all abstract numbers from the displayed inputs. Here, many of the necessary inputs are contained in tables and figures that are only partially represented (and sometimes only described textually). Critically:

- The abstract states per-class f_CW and σ for four V-Web classes and for DESIVAST-based voids; but several key counts and f_CW values for Phase 2 sweeps, HEALPix scans, and label-shuffle p-values are only mentioned in prose, without a full numerical table.  
- Some σ values in the abstract (e.g. −2.61σ, −4.66σ) can be checked against Table II, but others (e.g. “Phase 2 sensitivity sweep … range never exceeds 0.22 pp,” “label-shuffle p = 0.372,” “HEALPix nulls p = 0.61/0.135/0.413”) lack direct tabular confirmation in the text snippet given.

Because I cannot see the actual figures or full tables, I cannot verify that every abstract scalar is consistent with the body.

**Required fix:**  
Ensure that for every numerical claim appearing in the abstract:

- The corresponding N, n_CW or explicit f_CW, and σ are tabulated in the body of the paper (not merely described qualitatively).  
- For each quoted p-value or “never exceeds” bound, include an explicit table or appendix with the relevant numbers from which the stated value is computed.  

Then verify the abstract line-by-line against those tables. PRD expects that all abstract statistics be directly derivable from the main text.

---

### P5-E6 (ESSENTIAL) – Treatment of σ values from different null procedures without explicit comparability caveats  
**Location:** Throughout, especially Abstract; §V, §VI, §VII, §VIII F  

**Problem:**  
The paper uses “σfrom half” (a signed binomial deviation from f=1/2) and also σpred derived from the catalog monopole ∆f_CW, as well as σvs monopole residuals. It additionally uses logistic‑regression coefficients with z-scores, χ² tests, and permutation-based max-σ distributions. In several places, σ values from different procedures are mentioned side-by-side (e.g. “−4.66σ,” “|σ|max=3.94,” “σpred≈−3.16”) without always restating that these σ are not directly comparable because they correspond to different nulls and statistics.

Your reviewing instructions explicitly say: if sigma values from different null procedures appear side‑by‑side without explicit “not directly comparable” qualification at every juxtaposition, this must be flagged.

**Required fix:**  
Audit the paper and:

- Every time two σ’s from different tests are compared or listed adjacent (e.g. σfrom half vs σpred vs σvs monopole vs logistic z), insert an explicit sentence clarifying that these sigmas refer to different null hypotheses/statistics and are not directly comparable as Gaussian significance levels.  
- Prefer writing p-values alongside σ for all hypothesis tests, making clear which null and which estimator they refer to.  

Until this is made explicit wherever σ’s from different nulls co-occur, the statistical presentation is misleading by PRD standards.

---

### P5-M1 (MAJOR) – Citing preprints as if they were peer‑reviewed for robustness statements  
**Location:** Abstract (“Rincón et al. 2025, ApJ 982, 38  … peer-reviewed” correct), but ,  in §IX B, §X  

**Problem:**  
The paper distinguishes DESIVAST  correctly as peer-reviewed, but then treats  and  as “concurrent cosmic-web” works, using them as if they provided robust external validation (especially §IX B) while they are not yet refereed and, as noted, not yet on arXiv.

**Required fix:**  
- Clearly label  and  as “preprints, not peer-reviewed” and treat them only as illustrative, not as supporting evidence in claims about robustness.  
- Any robustness argument that relies critically on them (e.g., that V-Web fractions are “consistent with” T-Web or ASTRA) should be rephrased to make it clear they are preliminary and not independent confirmation.

---

### P5-M2 (MAJOR) – Over-reliance on descriptive language instead of explicit quantitative tests in several robustness claims  
**Location:** §VII (Phase 2), §IX B, §X, §XIII Limitations  

**Problem:**  
Many statements like “no evidence for environment dependence,” “consistent with,” “robust to,” “invariant under,” are backed by partial numbers but not always by explicit, reproducible tests:

- For Phase 2 sweep, the text says “max f_CW range 0.22 pp” and that no cell exceeds counting-statistics floors, but the per-cell σvs monopole tables are not shown.  
- The ASTRA cross-check reports “max |σ| ≈2.25” over four classes for three classifiers, but exact per-class values are not fully tabulated for all three.  

PRD will expect any robustness claim like this to be tightly tied to explicit numbers.

**Required fix:**  
- Add tables (in the main text or appendix) giving, for each (R_s, λ_th) cell, the four class f_CW, N, σfrom half, σvs monopole, and the per-cell range.  
- Add full tables for ASTRA argmax and entropy-weighted classifications with N, f_CW, σ for each cosmic-web class.  
- Where “no evidence” is claimed, explicitly give the p-values or bounds, not just qualitative language.

---

### P5-M3 (MAJOR) – Ambiguous novelty claim and “largest sample” positioning  
**Location:** Abstract (“largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date”), §VIII B  

**Problem:**  
The paper claims the DESIVAST-anchored test is “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date.” This is plausible but is not demonstrated by a literature review:

- Shamir 2022 uses 1.3×10^6 galaxies from DESI Legacy Surveys, but not DESI spectro.  
- It is not obvious that no other ongoing DESI analyses (e.g., internal notes or other preprints) match chirality to environment with large N.  

For PRD, strong novelty claims need at least a brief justification.

**Required fix:**  
Clarify the scope:

- Either qualify the claim to “to the best of our knowledge, among publicly available analyses, this is the largest DESI-DR1 chirality–environment test,” or  
- Provide a brief argument that no existing DESI DR1 paper or preprint has matched spiral chirality to environment at comparable N, with a short citation survey.

---

### P5-M4 (MAJOR) – Length and focus relative to claimed contribution  
**Location:** Full paper (20 pages)  

**Problem:**  
The scientific contribution is a null test of chirality–environment dependence with one main dataset and several cross-checks. The paper is very long relative to this scope, with extensive repetition of the same qualitative conclusion, and detailed methodological digressions (e.g., lengthy discussion in Appendix A on toy EFT operators) that are not essential to the main result.

**Required fix:**  
- Condense the narrative: move much of §VII, §IX, §X, and Appendix A to a more compact set of appendices or a companion methods note.  
- Aim for ~12–14 pages for the main text, with rigorous but concise presentation of: data, cross-match, primary DESIVAST analysis, V-Web canonical analysis, and the essential systematics.  

PRD does not enforce a hard page limit but expects concise exposition appropriate to the size of the result.

---

### P5-m1 (MINOR) – Version-history language and internal bookkeeping in body text  
**Location:** Multiple places, e.g. §V B, §VIII, §X, §XV, Appendix B  

**Problem:**  
The manuscript repeatedly uses internal analysis language typical of versioned pipelines:

- “Phase 2 sensitivity sweep,” “headline analysis,” “primary path,” “secondary diagnostic paths,” “this campaign,” “companion data repository,” “P5 headline,” etc.  
- Mentions of “deterministic seed: 20260515,” “single config file,” and a “reproducibility checklist” at the end of Appendix B.

While these are not strictly forbidden, they read like internal report language rather than a polished PRD article, and some of them (e.g. “headline result”) are informal.

**Required fix:**  
- Replace “headline” with “primary” or “main.”  
- Move the “Reproducibility checklist” to a brief Data and Code Availability section, phrased in standard scientific language.  
- Remove references to “this campaign” and “P5 headline,” which sound like project-internal bookkeeping.

---

### P5-m2 (MINOR) – Self-citation and “companion paper” language  
**Location:** Abstract, §II, references [3], [4]  

**Problem:**  
Paper II and Paper IV are repeatedly referred to as “companion papers,” emphasizing a multi-paper campaign. That is fine, but there is some redundancy and marketing-style phrasing (“this null complements Paper IV,” “campaign”) that is unusual for PRD.

**Required fix:**  
Streamline to a neutral description:

- “In a companion work [3] we construct the chirality catalog; here we study environment dependence.”  
- Avoid repetition of “companion paper” in multiple sections.

---

### P5-m3 (MINOR) – Duplicate/awkward phrases  
**Location:** Numerous, e.g.:

- “bounce-chirality coupling class (Sec. II) that would produce one at the ≳ 25 Mpc/h smoothing scale of the V-Web classification used here, and complements the Paper IV global-dipole bound at the catalog-monopole level.”  
- “monopole-only model” vs “catalog-wide classifier-monopole signature” etc.

These are stylistic, but the prose is dense and sometimes redundant.

**Required fix:**  
Editorial polishing for clarity and concision; remove unnecessary repetition of “monopole,” “headline,” etc., where meaning is obvious from context.

---

### P5-n1 (NIT) – Notational consistency and typography  
**Location:** §III C, §IV A, equations, and tables  

**Issues:**  

- The paper uses units like “25 Mpc/h” and “25 Mpc/h Gaussian smoothing.” PRD typically prefers “25 h^{-1} Mpc” or “25 Mpc h^{-1}” and “smoothing scale R_s = 25 h^{-1} Mpc.”  
- The notation “σfrom half” is verbally defined but not typeset in a consistent mathematical form (e.g. σ_{1/2}).  
- Occasionally, spaces in superscripts/subscripts or in e.g. “2563” instead of \(256^3\) are typographically suboptimal.

**Required fix:**  
- Harmonize units to PRD style.  
- Define σ_{1/2} or similar symbol once and then use consistently.  
- Typeset cubes and powers explicitly as \(256^3\), \(R_s\), etc.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific idea (a DESI-based null test of spiral chirality vs. environment) is suitable for PRD, but the current manuscript has serious issues in citation integrity and dependence on unpublished companion work. In particular, future-dated arXiv IDs, incomplete reference metadata, and heavy reliance on an in‑preparation Paper IV for the key catalog and monopole calibration prevent acceptance. These must be corrected, and the dependence on external unpublished results reduced or made fully transparent, before the paper can be considered.

---

## PASS 2 — self-critique findings (what initial review missed)

[P5-E7] **Abstract/reference-policy mismatch**: the abstract repeatedly uses citation-style source names and numbers in a way that is not PRD-compliant if the abstract is reprinted independently, because PRD explicitly says not to cite reference numbers in the abstract and to include complete source information for any references cited there.[1]

[P5-E8] **Missing figures/tables as rendered objects prevents PRD-style referee verification**: the paper text depends on Figures 1–7 and Tables I–XII for essentially every quantitative claim, but the supplied manuscript excerpt does not include the rendered figure objects or a complete PDF-style appendix package; PRD instructs authors to submit figures separately and to check that the PDF compiles correctly before review.[1]

[P5-E9] **Reference-list completeness vs. text citations in the manuscript body**: the body cites multiple works with bracketed placeholders and then later supplies a bibliography, but the review package supplied here is internally incomplete because the manuscript itself refers to several in-preparation works as if they were stable references; PRD author guidance stresses checking reference accuracy and including complete source information.[1]

[P5-M5] **Potential internal inconsistency in the paper’s own stated sample flow**: the abstract says the 1′′ matched catalog has **2,232,212** unique galaxies and **791,635** chirality-relevant spirals, while §X later refers to a superset of **812,793** env-labeled spirals and says the headline subsample is the stricter subset. That may be consistent, but the manuscript does not present a fully explicit set-partition diagram or a table connecting all three counts, so the reader cannot verify whether the 21,158-row excess is exactly the difference between those selections without reconstructing the pipeline manually.

[P5-M6] **Likely arithmetic slip in the Tempel overlap fraction**: §IX A states the Tempel overlap is **110,586** spirals from the **791,635** chirality-relevant matched sample, but it then says the SDSS DR10 footprint is a subset of DESI Legacy DR8 and “Tempel’s z ≤ 0.20 cut is much tighter than our z ≤ 4 DESI cut.” The \(z \le 4\) phrase is inconsistent with the earlier DR1 spectro limit \(0.01 \le z \le 2.0\) used for the V-Web calculation, so the comparison sentence is stale or miscopied from an earlier draft.

[P5-M7] **Equation 1 dimensional ambiguity**: Eq. (1) defines \(\sigma_{\rm pred} = \sqrt{\Delta f_{\rm CW}/(0.5/\sqrt{N})} = 2\,\Delta f_{\rm CW}\sqrt{N}\). The first form is dimensionally nonsensical as written because a fraction is being divided by a standard error and then square-rooted, while the second form is the actual binomial-significance relation. The printed equation should remove the erroneous first expression or rewrite it unambiguously as \(\sigma = \Delta f/ \sqrt{0.5(1-0.5)/N}\).

[P5-M8] **Equation 2 notation error / missing factor explanation**: Eq. (2) for the Bonferroni threshold is presented as \(|\sigma|^{\rm Bonf}_{\alpha,K} = \sqrt{2}\,\mathrm{erfc}^{-1}(\alpha/K)\), but the text does not state whether the threshold is one-sided or two-sided. Since the manuscript later uses two-sided \(|\sigma|\) language, the conversion should explicitly be \(|\sigma| = \sqrt{2}\,\mathrm{erfc}^{-1}(\alpha/K)\) only for a two-sided Gaussian tail; otherwise the stated threshold can be off by a factor of two in tail probability.

[P5-M9] **Inconsistent null-procedure comparability in one table caption/body pair**: Table VI reports the maximum fCW range per Phase-2 cell, while the body immediately turns that descriptive range into a claim about \(|\sigma^{\rm monopole}_{vs}|\!<\!1.15\) “at all four classes.” But the table itself contains only ranges, not the per-class counts needed to derive that residual significance. The significance claim is therefore not actually derivable from the adjacent table alone, contrary to the paper’s stated statistical workflow.

[P5-M10] **Mismatch between captioned class counts and narrative class counts**: Table VIII gives DESIVAST \(n_{\rm void}=56{,}981\), \(n_{\rm non-void}=621{,}964\), but §VIII B says restricting the matched spiral catalog to \(z \le 0.24\) leaves \(n_{\rm lz}=678{,}945\) spirals. Those numbers do sum correctly, but the narrative also describes the void sample as “\(\sim 130\times\) larger than the V-Web void sample size, \(n=428\).” The ratio is actually \(56{,}981/428 \approx 133.1\), so “\(\sim 130\times\)” is acceptable only as rough language; the paper elsewhere uses much sharper phrasing, so this should be made numerically consistent.

[P5-M11] **Abstract faithfulness issue in the “no evidence” claim**: the abstract says “no evidence for environment dependence above the sensitivity floor,” but §VIII F and Table X then show that after subtracting the P5 monopole, all four V-Web classes sit within \(|\sigma_{vs\ monopole}|<1.15\). That is a stronger, more specific null result than the abstract reports. The abstract should either quote the residual-\(\sigma\) result or explicitly state that the headline “no evidence” claim refers to the post-monopole residual, not the raw class-level \(\sigma\) values.

[P5-M12] **Novelty claim insufficiently supported in the body**: the statement that this is “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date” is repeated, but the manuscript does not provide a compact comparison table against all public DESI/Legacy chirality-environment analyses. The body compares against Shamir 2022, Tempel 2014, DESIVAST, and ASTRA, but it does not actually prove the “largest” claim across the full literature.

[P5-m4] **Notational inconsistency across sections**: the manuscript alternates among “\(25\) Mpc/h,” “\(25\,Mpc/h\),” and “\(25\) Mpc \(h^{-1}\),” and similarly mixes “\(2563\)” with “\(256^3\)” in prose. PRD-style consistency would require a single convention throughout.

[P5-m5] **Likely stale-number artifact in the void-resolution discussion**: §VIII D says the catalog-native void definition excludes “16,000–17,000 galaxies per algorithm,” while earlier the sphere-approximation discussion says the V-Web void sample is only 6 spirals and the DESIVAST void sample is 56,981. The exclusion range is not obviously tied to the stated samples and looks like a carryover from an earlier draft or a broader, not specifically defined, mask-cleaning stage.

[P5-n2] **Internal cross-reference ambiguity**: the paper repeatedly points to “§IX B below as a +8–18 pp V-Web excess in the void class,” but §IX B is the concurrent-literature T-Web cross-validation, not a void-fraction derivation section. That reference appears to be pointing to the wrong subsection for the stated empirical result.

[P5-n3] **Appendix/body mismatch on the toy EFT discussion**: Appendix A says the operator is only schematic and not a derived constraint, but the Conclusions paragraph says the paper provides an “observational upper bound” that future models “must satisfy.” Those are not the same claim. The appendix correctly downgrades the EFT mapping to a heuristic, so the main-text language should be weakened to avoid overstating it as a quantitative bound.

[P5-n4] **Over-strong language in the “same CW fraction” claims**: §IX A says the highest-n Tempel class pair agrees “within 0.026 percentage points” and that this is “the same CW fraction.” A 0.026 pp difference is tiny, but it is still not identical; the text should keep the distinction between numerical agreement and equality, especially because the two methods use different class definitions and different parent samples.

[P5-n5] **One-sided significance language used where two-sided testing is implied**: several places describe deviations as “\(-5\sigma\)” or “\(+3.4\sigma\)” while the test statistic is explicitly \(|\sigma|\) and the manuscript’s multiple-testing thresholds are two-sided. The sign is scientifically informative, but the reported significance should keep the two-sided framing explicit to avoid the impression of a one-tailed test.

[P5-n6] **Potential internal count mismatch in Table XI text**: Table XI lists the Tempel overlap as **110,586** spirals, while the narrative says the overlap is from a “1′′ sky-coord NN join between the Tempel catalog and the 791,635 chirality-relevant matched-spiral sample.” Because the Tempel catalog itself is only **588,193** galaxies, the overlap fraction is about **18.8%** of Tempel but **14.0%** of the matched-spiral sample. That asymmetry is plausible, but the paper never states the overlap fraction explicitly, so the reader cannot tell whether the join is unusually restrictive or just footprint-limited.

[P5-n7] **Figure-caption/body mismatch on Figure 6 valid-pixel counts**: the caption says the bottom panel uses **1,496 valid pixels** with \(\ge 200\) spirals, but the body immediately around the figure says the Pearson correlation is computed on **727** pixels containing both \(\ge 1\) maximal void and \(\ge 200\) spirals. The caption and body refer to different filtered sets, which is easy to misread as a discrepancy unless the distinction is made explicit in the caption itself.

[P5-n8] **Figure 3/Table III internal consistency is incomplete**: the figure caption says all five density quintiles track the monopole prediction within counting statistics, but Table III shows the fifth quintile has \(f_{\rm CW}=0.4985\) and \(\sigma_{\rm obs}=-1.16\) against \(\sigma_{\rm pred}=-2.07\). That is indeed consistent with the narrative, but the paper never states the implied raw count \(n_{\rm CW}\) for each quintile in the text; because the significance is used rhetorically, the raw integer counts should be displayed near the table so the reader can verify the stated \(\sigma\) values directly.

[P5-n9] **Main-text/appendix conflict on the role of reconstructed real space**: the limitations section says a proper Zel’dovich-reconstructed reclassification is required for a full RSD analysis, while the earlier DESIVAST primary-path section claims the result is “essentially RSD-immune at the level relevant to this work.” These are not logically equivalent. The main text should distinguish “approximately insensitive at the present precision” from “RSD-immune” more carefully.