# P3 auto-2026-06-05_1919pt — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: P3_Claude_brutal, P3_Gemini_cosmology, P3_Grok_brutal, P3_OpenAI_methodology, P3_Perplexity_citations
**Total findings (across all reviewers)**: 11
**Distinct consensus groups**: 4

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| P3_Claude_brutal | 0 | 0 | 0 | 0 |
| P3_Gemini_cosmology | 2 | 4 | 4 | 1 |
| P3_Grok_brutal | 0 | 0 | 0 | 0 |
| P3_OpenAI_methodology | 0 | 0 | 0 | 0 |
| P3_Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `audit_artifact` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: P3_Gemini_cosmology

- **[P3_Gemini_cosmology/P3-M1/MAJOR]**: **P3-M1** *   **Section:** Table I (p. 7) *   **Problem:** The structure of Table I is highly confusing. The main rows of the table present anomaly counts (`Nanom`) from the initial, superseded "cross-transfer" analysis, which the paper demonstrates is flawed. The final, canonical results from the "Path-C native-retrained" analysis are only presented in a summary row at the bottom and in the footnotes. This buries the headline results and foregrounds the diagnostic/rejected ones. *   **Fix:** Restructure Table I to be clearer. The main rows should present the final, canonical Path-C anomaly co…
- **[P3_Gemini_cosmology/P3-M4/MAJOR]**: **P3-M4** *   **Section:** References (p. 19), Table I (p. 7) *   **Problem:** The manuscript contains internal bookkeeping language not suitable for publication.     1.  Reference [33]: The entry includes the note "[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]".     2.  Table I, footnote `¶`: The text includes "The earlier 'strict subset' framing is replaced with this exact 284/298 = 95.3% overlap." *   **Fix:** Remove all such internal-facing comments, version history notes, and review-process artifacts from the manuscript. The text shoul…
- **[P3_Gemini_cosmology/P3-m3/MINOR]**: **P3-m3** *   **Section:** Figure 1 (p. 4) *   **Problem:** The figure shows the "Cross-transfer baseline map," which is a diagnostic result from a superseded analysis. While useful for illustrating the "before" state, the caption and title could be clearer that this does not represent the spatial distribution of the final, canonical catalog. *   **Fix:** Add a sentence to the beginning of the caption explicitly stating this, for example: "This figure shows the spatial distribution of the initial cross-transfer anomaly set, which is preserved as a diagnostic. It does not represent the final 37…

### `table_iv` — MAJOR — _single-reviewer_ (1 reviewer)

Reviewers: P3_Gemini_cosmology

- **[P3_Gemini_cosmology/P3-M2/MAJOR]**: **P3-M2** *   **Section:** Table IV (p. 13) *   **Problem:** Table IV, "Path-C residual caveats," is presented as a list of bullet points in a two-column "Headline result" / "Resolution" format. This reads like an internal document or a response to a previous review rather than a formal part of a scientific paper. The content is valuable but the format is inappropriate. For example, item (j) "GS corrected: ...; prior ±7.43 dropped" is cryptic. *   **Fix:** Rewrite the content of Table IV as a proper prose subsection within the Discussion (Section VI). Each point should be explained clearly in …
- **[P3_Gemini_cosmology/P3-m4/MINOR]**: **P3-m4** *   **Section:** V.c (p. 10) *   **Problem:** The text claims that GR projection corrections contribute "|Δσ/σ| < 0.02% at kmax = 0.2 h Mpc⁻¹" and cites §VID(e). However, Table IV on p. 13 is §VID, and item (e) simply states the result without derivation or a reference to a standard calculation. For a PRD paper, this claim should be substantiated. *   **Fix:** Provide a brief justification for this number, either with a back-of-the-envelope calculation or by citing a standard reference that computes the magnitude of these effects (e.g., Yoo et al. 2009, Bonvin & Durrer 2011, Challino…

### `table_ii` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: P3_Gemini_cosmology

- **[P3_Gemini_cosmology/P3-m2/MINOR]**: **P3-m2** *   **Section:** II.D (p. 3), Table III (p. 8) *   **Problem:** Several phrases are unclear or use undefined jargon.     1.  §II.D: "production-vs-5-seed-control Jaccard". The term "5-seed-control" is not defined.     2.  Table III caption: "IF raw scores are not a parallel catalog axis". The meaning of this phrase is obscure. *   **Fix:** Define "5-seed-control" or rephrase to be understandable (e.g., "Jaccard index between the production model and an ensemble of five models trained with different random seeds"). Rephrase the Table III caption to clearly explain the relationship bet…

## Other findings (5)

- **[P3_Gemini_cosmology/P3-E1/ESSENTIAL]**: **P3-E1** *   **Section:** Abstract (p. 1) and V.b (p. 10) *   **Problem:** There is a numerical error in a headline cosmological result. The abstract states: "a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)std = 8.98 single-tracer baseline)." The main text repeats the "7.9% improvement" claim. However, a direct calcula…
- **[P3_Gemini_cosmology/P3-E2/ESSENTIAL]**: **P3-E2** *   **Section:** References (p. 19) *   **Problem:** The manuscript cites key future-dated works as if they are already published. Specifically, "[1] DESI Collaboration, 'The DESI Data Release 1,' 2025" and "[12] C. Nicolaou et al., 'Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,' Mon. Not. Roy. Astron. Soc. (2026, in press)." A manuscript submitted for publicatio…
- **[P3_Gemini_cosmology/P3-M3/MAJOR]**: **P3-M3** *   **Section:** Throughout (e.g., Abstract, §III.D, §III.G) *   **Problem:** The catalogs for three surveys (LAMOST, Gaia, eROSITA) are acknowledged to fail the paper's own injection-recovery validation gates. While the author is transparent about this, the decision to include these "failed" catalogs in the main data release, even as "exploratory tiers," is questionable and weakens the …
- **[P3_Gemini_cosmology/P3-m1/MINOR]**: **P3-m1** *   **Section:** VI.D (i) (p. 12) *   **Problem:** The first paragraph of this subsection is a non-sequitur. It begins by discussing the "DESI in-sample training-test overlap" and the Jaccard stability results, but then abruptly pivots to the mathematical form of the Fisher forecast for fNL ("Fisher positivity-respecting form..."). These are two completely unrelated topics. *   **Fix:** …
- **[P3_Gemini_cosmology/P3-N1/NIT]**: **P3-N1** *   **Section:** Title page (p. 1) *   **Problem:** The paper is dated "June 2026". *   **Fix:** Correct the date to the month and year of submission.  ---  ### Summary recommendation
