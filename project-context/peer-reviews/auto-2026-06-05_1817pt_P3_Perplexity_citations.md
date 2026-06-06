# P3 auto-2026-06-05_1817pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 77.9s

---

The manuscript cannot be properly audited for citation accuracy or quantitative consistency because it is provided only as plain text; I do not have direct access to the rendered PDF, its page layout, figures, equations numbering, or the full reference metadata (DOIs, arXiv IDs, page ranges, etc.). This prevents me from fulfilling key parts of your requested task (page-accurate location, recomputation from plotted values, inspection of axis labels, etc.). Within those constraints, I will still do a detailed forensics pass on what *is* present in the text.

Below I treat “pages” as logical chunks in the order they appear, but I cannot guarantee they correspond to the actual PRD page numbers.

---

## Global ESSENTIAL issues

**P3-E1 – References section: incomplete/ambiguous citation metadata (no arXiv IDs, partial titles)**  
- **Location:** References section (end of manuscript).  
- **Problem:** The reference list as included here often lacks arXiv identifiers and in some cases gives incomplete titles or ambiguous internal labeling. For PRD, references must be precise (authors, journal, volume, page, year, arXiv ID where relevant). Several citations to cutting-edge work (e.g., NANOGrav, DESI DR1, SPHEREx forecasts, Heinrich et al.) are given only as prose-like entries with no arXiv number. Example:  
  - Ref. [1]: “DESI Collaboration, ‘The DESI Data Release 1,’ 2025, DESI DR1 documentation.” – no journal, no arXiv ID.  
  - Ref. : “Y. Liang et al., ‘Outlier detection in the DESI Bright Galaxy Survey,’ Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664.” – this one is ok.  
  - Ref. : notes that publication year is 2024 but bibkey label retained for arXiv-submission-year continuity. This is not standard PRD practice; PRD wants unambiguous bibliographic data for the *published* version plus the arXiv ID.  
- **Required fix:**  
  - For *every* reference, provide: full author list (or “et al.” after three authors as per PRD style), full title, standard journal abbreviation, volume, page, year, and arXiv ID where applicable.  
  - Ensure that the publication year in the citation matches the actual journal publication year; if a paper was first on arXiv in 2023 but published in 2024, list 2024 as the year and include “arXiv:…” as a separate entry.  
  - Remove internal notes like “bibkey label retained as Heinrich2023” from the reference text; that belongs in the .bib file, not in the manuscript.

---

**P3-E2 – Unsupported “largest catalog” and “73× / 141×” claims**  
- **Location:** Abstract and Conclusions (and echoed in Table I caption).  
- **Problem:** The manuscript claims:  
  - “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase.”  
  - At the end: “This is ∼ 141× the largest prior single-survey catalog ; DESI-only is a ∼ 73× like-for-like increase.”  
  From Liang et al.  (DESI BGS EDR outlier detection) the quoted number in the text is “2,685 anomalies (1.07%).” If that is indeed the largest previous catalog, then:  
  - 378,080 / 2,685 ≈ 141.0 (consistent with 141×).  
  - 195,829 / 2,685 ≈ 72.9 (≈73×).  
  However, the claim that  is “the largest prior single-survey anomaly catalog” is not substantiated. Baron & Poznanski  worked on SDSS spectra but they do not document their catalog size here; there is no systematic literature review to justify “largest.” There may be more recent or larger-scale anomaly catalogs (e.g., using Gaia or LSST precursors) not cited. This is a “first/largest” type claim that PRD expects to be demonstrably true.  
- **Required fix:**  
  - Explicitly check the literature for other large-scale anomaly catalogs (e.g., recent Gaia-based anomaly work, other DESI-based anomaly studies, SDSS photo+spec anomaly searches, etc.).  
  - Either provide explicit citations and numbers to show that 2,685 is indeed the largest previous anomaly catalog in the relevant class, or weaken the claim to something like “to our knowledge, this is among the largest” with clear qualifiers and scope (e.g., spectroscopic optical anomaly catalogs).  
  - Maintain the 73× and 141× as *numeric comparisons* to Liang et al.’s 2,685, but not as an absolute “largest ever” unless that statement is exhaustively justified.

---

**P3-E3 – “SPHEREx 3–5σ detection” claim not quantitatively tied to presented Fisher analysis**  
- **Location:** Introduction, Sec. V, and Conclusions.  
- **Problem:** The paper repeatedly states that the quasi-matter bounce model fNL = −35/8 is “testable at 3–5σ with SPHEREx  under the multi-tracer methodology of Heinrich et al. .” However, the only explicit Fisher expressions given are:  
  - A DESI-based single-tracer baseline σ(fNL)std = 8.98,  
  - A multi-tracer Fisher-positivity parameterization 1/σ(fNL)^2 = F0 + cα^2, with F0 = 1/8.982 and c = 0.0747, and measured α values or forecasts that lead to σ(fNL) ≈ 8.14 or similar.  
  None of these DESI-based numbers are in the SPHEREx regime; they are current-catalog forecasts. The reference  is a SPHEREx-specific bispectrum forecast that yields σ(fNL) ≈ 0.7 in the ideal case, but the manuscript never actually recomputes a SPHEREx-level σ(fNL) incorporating the anomaly tracers, nor does it propagate specific SPHEREx number densities or biases derived from this catalog. The “3–5σ” statement reads as an untested qualitative extrapolation.  
- **Required fix:**  
  - Either perform an explicit Fisher forecast for SPHEREx that uses the anomaly-tracer bias enhancement and number densities and report the resulting σ(fNL) (with and without the anomaly tracers), or clearly label the “3–5σ” statement as *a restatement of Heinrich et al.’s SPHEREx baseline* and not as a direct output of this catalog.  
  - In the abstract and conclusion, make clear what *this paper* proves: at present, with DESI-level data, the multi-tracer improvement is ∼8% and not statistically significant (<1σ). The projected SPHEREx 3–5σ test should be described as a conditional future possibility based on external forecasts, not as a result of this work.

---

**P3-E4 – Mixture of σ values from different nulls without explicit non-comparability warnings**  
- **Location:** Abstract; Sec. II D; Sec. III (injection-recovery gates), Sec. V (fNL Fisher forecast), Sec. V A (NANOGrav γ), Sec. VI.  
- **Problem:** The paper uses a wide variety of σ-based significance measures:  
  - 5σ thresholds for injection-recovery gates (on artificial injections in reconstruction MSE or IsolationForest latent space),  
  - “< 1σ from null” for αjk uncertainty,  
  - “+1.13σ” for NANOGrav γ relative to γ=3.0,  
  - “+4.61σ” for the SMBHB γ=4.33 relative to the same posterior,  
  - “5σ subspace injection” for eROSITA, etc.  
  These σ values arise from different likelihoods, different data, and different procedures (frequentist Gaussian approximations, MCMC standard deviations, injection-recovery detection fractions). In multiple places they are juxtaposed in the same paragraph as if they were directly comparable measures of “significance.” The instructions you provided require explicit qualification at each juxtaposition that these are *not* directly comparable. The manuscript does not consistently do this.  
- **Required fix:**  
  - In every place where σ values from different contexts appear together (e.g., abstract sentence listing “6 injection-recovery gates: 3 PASS … and 3 FAIL-with-diagnostic at 5σ … A NANOGrav 15-yr KDE free-spectrum MCMC yields γ = 2.567 ± 0.382; the matter-bounce prediction γ = 3.0 sits at +1.13σ; SMBHB at +4.61σ”), explicitly state that these σ values are defined on different data sets and likelihoods and are not directly comparable.  
  - For the abstract, this must be a standalone clause, e.g. “These σ-values arise from distinct likelihoods and nulls and are not directly comparable.”  
  - Clarify for each σ whether it is an empirical standard deviation of an estimator, an MCMC posterior σ, or a synthetic injection amplitude expressed in units of noise, and avoid side-by-side use without such labels.

---

**P3-E5 – NANOGrav γ analysis: incomplete referencing and validation**  
- **Location:** Abstract; Sec. V A; Appendix E; References.  
- **Problem:**  
  - The paper states it uses “NANOGrav 15-yr HD-correlated KDE free-spectrum likelihood  (Zenodo 10.5281/zenodo.8060824; 30 Fourier bins).” According to Agazie et al. (NANOGrav 15-yr GWB discovery paper), the main 15-yr dataset is indeed associated with a set of public data products; however, the exact Zenodo record and internal dataset naming (“30f fs{hd} ceffyl”) must match NANOGrav’s release. I cannot verify this from the text alone.  
  - The paper quotes γ = 2.567 ± 0.382, log10 A = −14.025 ± 0.380, and Bayes factors BMB/free = 3.23, BSMBHB/free = 4.52×10^-4, BMB/SMBHB = 7.14×10^3, but does not show any consistency checks against the values reported by NANOGrav for a power-law GWB in the 15-yr paper. NANOGrav’s own results (for a SMBHB-like spectrum) are not explicitly cited as a comparison. This is a nontrivial statistical re-analysis of collaboration data; PRD will expect a cross-check that the pipeline can reproduce their published SMBHB-like posterior when assuming that model.  
- **Required fix:**  
  - Explicitly cite the relevant NANOGrav 15-yr paper for the *HD-correlated free-spectrum product* and verify that the Zenodo ID and dataset name match exactly what NANOGrav release notes specify.  
  - Add a sanity-check analysis in Appendix E: run the same MCMC but with γ fixed to 13/3 or with a SMBHB-prior template and show that the recovered posterior for log10 A and Bayes evidence matches NANOGrav’s published SMBHB results within uncertainties.  
  - Clarify that this is a high-level re-use of published likelihoods; emphasize that systematic effects (solar system ephemeris, noise model choices) are taken as fixed by the NANOGrav KDE product and not newly modeled here.

---

**P3-E6 – Extensive version-history/internal-bookkeeping language in main text**  
- **Location:** Many places, especially Table I caption, Appendix F, and several footnotes (e.g., “Path-C final catalog,” “quarantined ACT block,” “companion data repository,” “gate criteria of §II D Step 1,” “Path-C protocol forbids…”).  
- **Problem:** The manuscript contains a lot of internal project bookkeeping language and versioning (“Path-C rebuild,” “R7” is not present but “Path-C final catalog,” “ACT DR6 quarantined,” “companion data repository,” “archival comparison artifact,” “private pending arXiv acceptance; public upon acceptance”). PRD articles are supposed to read as permanent, standalone scientific reports, not as internal audit memos or software-release notes.  
- **Required fix:**  
  - Remove or substantially reduce internal-protocol language that refers to “Path-C,” “quarantine,” “checkpoint,” and “gate FAIL/PASS,” or relegate it to a brief methods paragraph with neutral scientific phrasing.  
  - Eliminate references to “private pending arXiv acceptance; public upon acceptance.” Either the data/code are public at submission or they are not; you can state “will be released upon publication” in a short data-availability statement, but not as quasi-versioning text in the main body.  
  - Avoid describing this submission as “Path-C-final catalog” inside the paper. That is internal metadata, not scientific content.

---

**P3-E7 – Abstract overclaims relative to what is demonstrated**  
- **Location:** Abstract.  
- **Problem:**  
  - The abstract claims: “An empirical Landy–Szalay bias measurement on the 5,384 QSO-candidate sample yields αjk = 0.19 ± 0.65 (< 1σ from null); inserting this into the Fisher-positivity-respecting form 1/σ(fNL)^2 = F0 + c α^2 gives a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at < 1σ; σ(fNL)std = 8.98 single-tracer baseline).”  
    This is technically described as “consistent with no improvement,” but the very presence of a 3.92 lower bound in the envelope is visually suggestive of a much stronger constraint than is actually supported. The envelope itself is derived from a parameterization that is only tested in a limited α-range and relies on a heuristic “positivity-respecting” form.  
  - Similarly, for NANOGrav, the abstract quotes γ = 2.567 ± 0.382 and Bayes factors classified as “decisive” on Jeffreys’ scale, which is a strong claim, yet the text acknowledges that “Neither constitutes a detection.” The combination of “decisive Bayes factor” and “not a detection” is conceptually conflicting without further clarification.  
- **Required fix:**  
  - In the abstract, de-emphasize the numerical “3.92–8.98” envelope; say instead that the empirical α measurement implies at most a ∼8% potential improvement in σ(fNL) under optimistic assumptions, and at present the result is statistically consistent with no improvement.  
  - For NANOGrav, explicitly state in the abstract that the Bayes factor is computed with highly simplified priors and a 2-parameter model, and that the classification as “decisive” is in that restricted model space; avoid giving the impression of a new, stronger constraint than NANOGrav itself reports.  
  - Ensure the abstract only states what is *actually demonstrated* with current data (DESI-era and public PTA products) and clearly separates this from forecasts or interpretive speculation.

---

## MAJOR issues

**P3-M1 – Some referenced works appear “in press” / future-dated without clear traceability**  
- **Location:** Ref. : “C. Nicolaou et al., ‘Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,’ Mon. Not. Roy. Astron. Soc. (2026, in press).”  
- **Problem:** The citation states “in press 2026” but no volume/page or arXiv ID. This is borderline acceptable only if:  
  - the paper is genuinely accepted in MNRAS,  
  - an arXiv preprint exists.  
  As text-only, this cannot be verified. PRD expects either an arXiv ID or such references to be clearly labeled as “in preparation” and used only very sparingly, not as quantitative support.  
- **Required fix:**  
  - If the Nicolaou et al. paper is on arXiv, add the arXiv ID and, if available by the time of revision, the volume/page.  
  - If it is not yet on arXiv and only “submitted” or “in preparation,” reclassify it as such, move detailed dependence on it out of the main text, and remove any numerical statements that rely solely on that work.

---

**P3-M2 – BigAE score normalization and DESI σ(fNL) baseline are not fully reconstructible from given numbers**  
- **Location:** Eq. (2) and the DESI DR1 description in Sec. II B and III A; Sec. V.  
- **Problem:**  
  - The anomaly score S(x) = (MSE − μ_val)/σ_val is defined, and it is stated that “For DESI DR1, μ_val ≈ 0.0287 (validation MSE) and σ_val is set such that the S > 5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.” This implies σ_val ≈ (0.143 − 0.0287)/5 ≈ 0.0229. But in Fig. 2 and elsewhere, scores go up to S ≈ 25; this implies MSE around μ_val + 25 σ_val ≈ 0.0287 + 25×0.0229 ≈ 0.60. Without actual MSE distributions or error bars, one cannot check whether this is consistent with the stated val-loss 0.0287 or with the training objective.  
  - The DESI σ(fNL)std = 8.98 single-tracer baseline is taken as a given, but no equation or table shows how this number is obtained (e.g., number densities, biases, k-range, survey volume). There is a later mention of “plane-parallel monopole, k_max = 0.2 h Mpc^-1,” but not a fully specified Fisher matrix. As a referee, I cannot reconstruct 8.98 from the text alone.  
- **Required fix:**  
  - Provide explicit numeric values for μ_val and σ_val for DESI and at least one other survey in a small table, and show the mapping between MSE and S for the threshold(s) used.  
  - Include at least a brief formula for σ(fNL)std, specifying survey volume, redshift bins, number density, bias, k-range, and key nuisance parameters, so that an informed reader can replicate the ∼8.98 value.  
  - For PRD, a short, explicit Fisher-matrix expression is expected, not just a reference to “F0 = 1/8.982.”

---

**P3-M3 – ACT DR6 “quarantine” section is methodological but distracts from main results**  
- **Location:** Appendix F and multiple references in main text (e.g., abstract parenthetical “ACT DR6 quarantined as a cross-transfer artifact”; Table I; Sec. III F).  
- **Problem:** ACT DR6 is repeatedly mentioned as “quarantined,” and a detailed cross-transfer failure analysis is included. This is interesting methodologically but not central to the cosmology or anomaly catalog science. In its current form it consumes substantial textual space and adds complexity that may confuse readers about what is and is not part of the main result.  
- **Required fix:**  
  - Move ACT DR6 discussion to a very short subsection clearly labeled as a *non-science-methodology test*, and remove repeated ACT mentions from the abstract and main results (e.g., “ACT DR6 quarantined as a cross-transfer artifact” in the abstract is unnecessary).  
  - Emphasize once, in the methods, that ACT DR6 is *not* included in any headline numbers and that the ACT autoencoder never passed the quality gate; the long appendix can be shortened or removed.

---

**P3-M4 – Internal duplication in data-availability section and references to code repositories**  
- **Location:** Data availability paragraph at end of main text; references to HuggingFace and GitHub throughout.  
- **Problem:** The manuscript contains detailed URLs and notes like “private pending arXiv acceptance; public upon acceptance” inside the main text. PRD typically does not include raw HTTP URLs in the article; they’re either in footnotes, in a data-availability statement, or omitted in favor of DOIs.  
- **Required fix:**  
  - Replace explicit HTTP URLs with a concise data-availability statement such as: “The catalog and code used in this analysis are available at a public repository (DOI: …) and will be made public upon publication.”  
  - Remove redundant references to the same repositories and avoid embedding versioning language in the text.

---

## MINOR issues

**P3-m1 – Repeated phrase “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository)”**  
- **Location:** Sec. II C / II D.  
- **Problem:** The phrase “reproducibility scripts shipped with the data release” is immediately followed by “(reproducibility scripts shipped with the companion data repository).” This is semantically redundant and likely an editing oversight.  
- **Required fix:**  
  - Reduce to a single clause: e.g., “reproducibility scripts provided in the companion data repository.”

---

**P3-m2 – Ambiguous use of “canonical” for S and BigAE / IF scores**  
- **Location:** Throughout, e.g. Eq. (2), Table I notes, Table III.  
- **Problem:** The term “canonical-S” is used multiple times to denote the BigAE-based z-score. However, Table III also lists S_IF,raw as a second score and uses BigAE vs IF interplay. In some places “canonical-S” is used to denote the threshold-defining value for eROSITA (S > 0.259), which is not the same as the DESI S > 5 definition. This can confuse readers about which “S” is the canonical anomaly score.  
- **Required fix:**  
  - Clearly define “S” once as the BigAE-based z-score, and whenever another axis (IsolationForest raw score S_IF,raw) is used, refer to it solely as “IF score” to avoid ambiguous “S.”  
  - In Table I footnotes, carefully distinguish “BigAE S” vs “IF raw score” to avoid overloading S.

---

**P3-m3 – Minor dimensionality consistency checks**  
- **Location:** Eq. (1) and Eq. (2).  
- **Problem:** MSE(x) as defined is dimensionful if x has physical units (flux, counts). However, the paper implicitly uses normalized/standardized spectra and catalog features, so MSE is effectively dimensionless; this is never stated explicitly. For a journal like PRD, clarity on dimensionless vs physical units is expected.  
- **Required fix:**  
  - Add a short sentence in Sec. II A/B that all input features are scaled to dimensionless standardized units prior to training, so that MSE and S are dimensionless quantities.

---

**P3-m4 – Language / style nits (“gate FAIL-with-diagnostic at 5σ,” “PASS/FAIL”)**  
- **Location:** Sec. II D, III, VI D, Fig. 7 caption.  
- **Problem:** The “gate PASS/FAIL” language is reminiscent of internal QA rather than a scientific description. While understandable for project documentation, it is somewhat informal for PRD.  
- **Required fix:**  
  - Replace “gate PASS/FAIL” with more neutral phrasing such as “meets the 5σ injection-recovery criterion” or “does not meet the 5σ criterion but passes cross-validation stability checks.”

---

**P3-m5 – Overly verbose Table I caption**  
- **Location:** Table I.  
- **Problem:** Table I’s caption is very long, effectively reading as a sub-section of the paper. Some of that content belongs in the main text with a simpler caption that describes the table columns and key footnotes.  
- **Required fix:**  
  - Shorten the caption to focus on what is in the table; move extended discussion of gate criteria, cross-transfer vs native, and deduplication into the main Methods or Results sections.

---

## NITs / cosmetics

**P3-n1 – Placeholder “Fig. ??” in several places**  
- **Location:** Sec. II A, II B, III B, Appendix D.  
- **Problem:** Several references to figures use “Fig. ??” as if the labels were not resolved, e.g. “architecture shown schematically in Fig. ??” and “Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts.” These are clear editing placeholders and must be fixed before publication.  
- **Required fix:**  
  - Resolve all figure references to the correct numbers; ensure no “??” remains.

---

**P3-n2 – Typographical / minor repetition issues**  
- **Location:** Multiple places:  
  - “survey-by-survey” vs “per-survey” used inconsistently.  
  - Slight sentence repetition in the Description of Path-C rebuild.  
- **Required fix:**  
  - Clean up minor stylistic inconsistencies and redundant phrases; a careful copy-editing pass is recommended.

---

**P3-n3 – Some axes in figures not described in text**  
- **Location:** Fig. 2 (right panel) anomaly score S on log–log scale; Fig. 7; Fig. 8.  
- **Problem:** The descriptive text mostly explains what the axes represent, but in a few cases it is not fully clear from the captions alone how to read the vertical units (“Probability density” vs “Prob. density” on log scales, “Recovery fraction (%)” but not restating that 50% at 5σ is the pass criterion).  
- **Required fix:**  
  - Tighten figure captions to explicitly state the units and definitions of both axes, and reiterate where applicable that vertical axes are log10 of the quantity.

---

## Length of the paper

The manuscript is very long (effectively ~19–20 pages of dense text) for the claimed contributions:

- Construction of a large multi-survey anomaly catalog,
- A few specific astrophysical highlights (high-z QSOs, BAL QSO, NEOWISE extreme source),
- Methodological lessons (LAMOST training bias),
- Preliminary cosmological applications (fNL Fisher forecast, PTA γ analysis).

For PRD, which emphasizes focused methodological and cosmological advances, the current length and density are high relative to the *demonstrated* cosmological impact (which is, by the authors’ own admission, currently <1σ). Much of the internal Path-C QA discussion, ACT cross-transfer appendix, and repetition of gate criteria could be condensed.

**Recommendation on page count:**  
- The paper could reasonably be reduced to **≈12–14 PRD pages** by:

  - Moving all ACT-specific and most “gate” QA discussion into a very short technical appendix or supplementary material,  
  - Shortening Table I’s caption and some of the methodological narrative,  
  - Tightening the cosmology sections to focus on what is directly supported by the catalog, and relegating speculative forecasts to a compact subsection.

---

## Summary recommendation

**MAJOR REVISIONS**

The catalog-building and anomaly-detection work are substantial and, if properly documented and trimmed, could merit publication as a methodological cosmology/astro-statistics paper. However, the current draft mixes internal QA language with scientific narrative, overstates some novelty claims, juxtaposes non-comparable σ-values without sufficient qualification, and relies on incomplete citation metadata and partially specified Fisher/PTA analyses. These issues must be corrected, and the manuscript should be significantly streamlined, before it can meet the standards of Physical Review D.