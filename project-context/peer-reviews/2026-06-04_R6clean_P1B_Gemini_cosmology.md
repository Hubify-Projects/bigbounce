# P1B 2026-06-04_R6clean — Physical Review D cosmology-physics referee

**Model**: `google/gemini-2.5-pro` [FALLBACK from gemini-2.5-pro]
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 120.5s

---

Referee Report for Paper P1B

## Preamble
This report assesses the suitability of the manuscript "Technical Verification Companion to the ECH Spin-Torsion Program..." for publication in Physical Review D. The assessment is based on the criteria of theoretical rigor, methodological soundness, scope, and readiness for publication.

## General Comments
The manuscript presents three technical analyses intended to support a larger research program on Einstein-Cartan-Holst (ECH) cosmology. These are: (1) a ΛCDM+∆Neff MCMC analysis, (2) a validation of a CMB pseudo-Cℓ pipeline, and (3) a consistency check of a spectator axion-like particle (ALP) model with cosmic birefringence data.

While the author is commendably transparent about the limitations of each analysis, the manuscript suffers from several fundamental issues that preclude its publication in its current form. The most critical is its dependency on a main paper, "Paper I(a)," and several other manuscripts that are "in preparation" and thus unavailable for review. This makes it impossible to assess the context, motivation, and significance of the presented work.

Furthermore, the paper is replete with artifacts from an internal review process, project management notes, and unprofessional formatting, indicating that it has been submitted prematurely. Methodologically, the analyses are either incomplete (the w0-wa analysis lacks a Bayes factor) or flawed in their setup (the spectator-ALP analysis is performed outside the spectator regime). The paper's structure is disjointed, reading as a collection of three separate, underdeveloped projects rather than a coherent scientific paper.

## Findings

### ESSENTIAL (Paper cannot be accepted without this fix)

**ID:** P1B-E1
**Section:** Throughout (e.g., Abstract, I, II)
**Problem Statement:** The manuscript is explicitly a "companion paper" to "Paper I(a) [1]", which is cited as "in preparation". Several other key papers ([4], [5], [6]) that provide context are also "in preparation". A manuscript cannot be peer-reviewed if its core motivation and scientific context are contained in unavailable documents.
**Required Fix:** The paper can only be considered for review once Paper I(a) and any other essential companion papers are publicly available, at a minimum as preprints on a repository like arXiv. The current manuscript must be rejected on these grounds.

**ID:** P1B-E2
**Section:** Throughout (e.g., p.3, p.4, p.6, p.7)
**Problem Statement:** The manuscript contains numerous "review-log artifacts"—phrases and paragraphs that are clearly responses to previous critiques or records of the author's evolving understanding. These are entirely inappropriate for a formal scientific paper. Specific examples include:
- p.3: "An earlier count erroneously quoted '98.6% quintom-B' weight..."
- p.3: "note: prior caveat promised a Savage-Dickey ratio on the converged 2D (w, wa) marginal, but..."
- p.4: "This addresses earlier reviewer concerns that the reported 67.68 was inconsistent with an active SH0ES likelihood;"
- p.4: "A concern was raised that..."
- p.6: "...the bias was initially characterized as strictly “stable across all three injections” at 0.032◦ , but the 0.342◦ injection actually gives 0.040◦..."
- p.7: "...correcting the earlier Caγ θi product)."
**Required Fix:** All such text must be removed. The paper needs to be rewritten from the perspective of a finished work, not a live journal of the research process.

**ID:** P1B-E3
**Section:** Throughout (e.g., ToC, Sec. III, Sec. IV, Table III)
**Problem Statement:** The paper is littered with internal process artifacts, unprofessional formatting, and project management metadata that have no place in a published article. Specific examples include:
- p.1, ToC: The note `(Not a Spin-Torsion Theory Module)`.
- p.2, Sec. III title: The parenthetical `(NOT A SPIN-TORSION THEORY MODULE)`.
- p.4: The filename `spin torsion.input.yaml`.
- p.5: The file path `pipelines/h200 results/pod1 namaster umap 2026-04-29/`.
- p.10, Table III: The entire "Claims classification" table, which appears to be an internal project tracking tool.
**Required Fix:** All such artifacts must be removed. The paper must be formatted as a professional scientific manuscript.

**ID:** P1B-E4
**Section:** VI, Appendix C
**Problem Statement:** The spectator-ALP analysis is fundamentally flawed in its design. It is presented as a "spectator-ALP consistency check," yet the MCMC analysis is performed over a parameter range for the initial misalignment angle, `θi ∈ [0.5, 2]`, which the author repeatedly admits (in fn. 4, fn. 5, and the main text) corresponds to a non-spectator, dark-energy-like ALP that would have significant backreaction. The actual spectator regime is identified as `θi ~ 0.1`, which is described as a "∼ 25× fine-tuning". Performing the analysis in an inconsistent parameter regime and then pointing out the inconsistency in a footnote is not rigorous.
**Required Fix:** The analysis must be re-run with priors that are consistent with the "spectator" hypothesis being tested (i.e., centered on `θi ≪ 1`). Alternatively, the analysis must be reframed as a constraint on a dark-energy ALP, which is a different claim and outside the stated scope of this check.

### MAJOR (Significant revision required)

**ID:** P1B-M1
**Section:** Overall Structure
**Problem Statement:** The paper lacks a coherent narrative and reads as three disconnected analyses (∆Neff MCMC, w0-wa MCMC, and an ALP check) loosely bundled together. The w0-wa analysis, in particular, is introduced abruptly in the middle of a section on the ∆Neff proxy run, with its results discussed on page 3 before the relevant table (Table II) appears on page 4. The motivation for including a standard w0-wa analysis in a paper on ECH spin-torsion is not adequately established.
**Required Fix:** The paper must be restructured to present a single, clear argument. The author must either establish a strong, explicit link between the three analyses or consider splitting them into separate, more focused communications (or appendices for the main paper, once it exists).

**ID:** P1B-M2
**Section:** V.B, VII
**Problem Statement:** The w0-wa analysis (Table II) suggests a >4σ (marginal) departure from ΛCDM, which is a significant claim. However, the author explicitly defers the calculation of the Bayes factor (ln B), which is the appropriate statistic for model comparison in this context. The justification for this deferral (i.e., that Metropolis-Hastings chains are unsuitable) is correct, but it highlights that the analysis as presented is incomplete. Presenting a strong "quintom signature" claim based on parameter tails without the requisite evidence calculation is insufficient for a high-impact journal.
**Required Fix:** To support the claims made, the analysis must be completed with a proper model comparison using nested sampling (e.g., PolyChord/MultiNest) to calculate the Bayesian evidence and Bayes factor against ΛCDM. Without this, the w0-wa section is merely a preliminary finding, not a publishable result.

**ID:** P1B-M3
**Section:** Throughout
**Problem Statement:** The paper is excessively redundant. The same caveats and disclosures are repeated in the abstract, main text, footnotes, and appendices. For example, the non-viability of a Savage-Dickey ratio is explained on p.3, p.6, and p.8. The fine-tuning of the spectator ALP is discussed in the abstract, Sec. VI, fn. 4, fn. 5, and Sec. VII. This makes the paper difficult to read and unnecessarily long.
**Required Fix:** The paper requires substantial editing for clarity and conciseness. Each key point or caveat should be stated once, clearly and in the most appropriate location. The current length of 10 pages is not justified by the contribution; a properly edited version would be significantly shorter.

**ID:** P1B-M4
**Section:** Appendix B
**Problem Statement:** Appendix B, titled "Claims Classification," is an empty section header.
**Required Fix:** This formatting error must be corrected. Either provide the content for this appendix or remove the section entirely.

### MINOR (Should be addressed)

**ID:** P1B-m1
**Section:** III, Figure 1 caption, fn. 1
**Problem Statement:** The explanation of MCMC sample counts is convoluted and difficult to follow. Footnote 1, in particular, reads like an internal reconciliation of numbers rather than a clear statement for the reader. The distinction between raw samples, post-burn-in samples, and getdist-thinned samples for plotting is confusingly presented.
**Required Fix:** Simplify the reporting of sample statistics. For each chain, clearly state the total number of samples, the burn-in fraction removed, and the final number of samples used for posterior estimation.

**ID:** P1B-m2
**Section:** III, Table I, VII
**Problem Statement:** The text mentions a third, unconverged "Planck-only" MCMC run that is supposedly reported in Table I but is not clearly identifiable in the table's two columns ("Full-tension" and "Planck+BAO+SN"). This creates confusion about which results are being presented.
**Required Fix:** Clarify where, if anywhere, the results of this third run are reported. If they are not used in the paper's conclusions due to lack of convergence, they should be removed to avoid confusion.

**ID:** P1B-m3
**Section:** p.1 fn. a, p.9 Ref. [22]
**Problem Statement:** Several parts of the paper are written in a conversational or informal tone. Footnote `a` on page 1 ("The repository README is the authoritative source...") and the annotation to reference [22] ("Used in P1A Sec. VI to point readers to...") are not written in a formal academic style.
**Required Fix:** Rewrite all such passages in a formal, objective tone suitable for a scientific publication.

### NIT (Very minor, fix if time permits)

**ID:** P1B-N1
**Section:** p.1
**Problem Statement:** The date format `(Dated: 2026-06-03 PDT)` is non-standard and includes a timezone.
**Required Fix:** Use the journal's standard date format, or omit it for the journal's production team to handle.

**ID:** P1B-N2
**Section:** VI
**Problem Statement:** A sentence is broken across the page boundary between pages 6 and 7: "The ALP equation of motion... in a ΛCDM background3 yields the field displacement from" [page break] "recombination to today...".
**Required Fix:** Correct this formatting error.

## Summary recommendation
**REJECT**

This manuscript is recommended for rejection. It is not possible to conduct a meaningful peer review of a "companion paper" when the main paper it depends on is unavailable. This is a fatal procedural flaw. Beyond this, the manuscript is not ready for publication, as it is filled with internal review notes, project management artifacts, and unprofessional language that demonstrate a premature submission. The scientific content itself suffers from major issues, including an incomplete analysis of a key result (the w0-wa posterior) and a fundamentally flawed methodology in another (the spectator-ALP check). The paper requires a complete reconceptualization and rewrite, and should only be reconsidered for submission after its foundational companion papers are publicly available and the analyses within it are brought to a state of completion and rigor.