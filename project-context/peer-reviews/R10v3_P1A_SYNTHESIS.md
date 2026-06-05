# P1A R10v3 — v3 native-PDF cross-vendor SYNTHESIS

**Reviewers**: Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations
**Total findings (across all reviewers)**: 31
**Distinct consensus groups**: 5

## Per-reviewer finding counts

| Reviewer | ESSENTIAL | MAJOR | MINOR | NIT |
|----------|-----------|-------|-------|-----|
| Claude_brutal | 0 | 0 | 0 | 0 |
| Gemini_cosmology | 2 | 2 | 5 | 0 |
| Grok_brutal | 0 | 0 | 0 | 0 |
| OpenAI_methodology | 10 | 5 | 7 | 0 |
| Perplexity_citations | 0 | 0 | 0 | 0 |

---

## Consensus-grouped findings (most reviewers first)

### `companion` — ESSENTIAL — **CONSENSUS** (2 reviewers)

Reviewers: Gemini_cosmology, OpenAI_methodology

- **[Gemini_cosmology/P1A-E2/ESSENTIAL]**: **P1A-E2: Over-reliance on Unpublished, Unverifiable Companion Works** *   **Location:** Throughout the paper (e.g., Abstract, Sec. III.B, Sec. V, Sec. VII, Sec. XV, Refs. [2, 6, 23, 46]). *   **Problem:** The paper makes numerous specific, quantitative claims that are not derived or substantiated within the manuscript itself. Instead, the reader is referred to companion papers that are "in preparation." These include:     *   The `f_NL = -35/8` SPHEREx forecast (Ref. [2]).     *   All MCMC analysis, parameter values (`H_0`, `ΔN_eff`), and pipeline validation (Ref. [6]).     *   The crucial nu…
- **[OpenAI_methodology/P1A-E2/ESSENTIAL]**: P1A-E2 p. 1 (Abstract) & p. 18 (Data and Code Availability)   Statement All numerical results (Cobaya chains, NaMaster pipeline, ALP MCMC, Fisher forecast) are “documented separately in companion work in preparation [6]”.   Problem PRD requires that all analysis supporting headline numbers be available to referees.  None of the chains, likelihood files or scripts cited in Paper I(b)/Paper II were provided.  The public github repository advertised on p. 18 contains only a placeholder README.   Required fix Upload every chain, likelihood, and analysis script used in the present paper to a perman…
- **[OpenAI_methodology/P1A-E7/ESSENTIAL]**: P1A-E7 p. 15, §XIII   Statement SPHEREx is forecast to detect fNL = −35/8 at “3–5 σ realistic”.   Problem The Fisher numbers are taken from a companion study [2] that is “in preparation”.  No Fisher matrix, survey specifications, or systematic error model is provided here.  The uncertainty σ(fNL)=0.7 implies a 5.6 σ detection but the text quotes 3–5 σ without explaining the downgrading.   Required fix Present the complete Fisher pipeline in an Appendix (k-range, bias priors, redshift bins, treatment of GR projection & photo-z errors) so that the quoted 3–5 σ range can be reproduced.

### `companion,audit_artifact` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P1A-E9/ESSENTIAL]**: P1A-E9 Throughout (e.g. pp. 3, 5, 13)   Problem Version-history and internal-review language (“this manuscript”, “earlier drafts”, “internal extrapolation”, “hUBIFY-2026-003”) appears repeatedly.  Such text is not permissible in a final PRD article.   Required fix Strip all version-tracking, draft history, and companion-paper boiler-plate.

### `table_ii` — ESSENTIAL — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P1A-E1/ESSENTIAL]**: P1A-E1 p. 1 (Abstract)   Statement “we report 13 logically-independent mechanism-class constraints that collectively constrain the enumerated channels …”   Problem One of the 14 numbered constraints (B8) is explicitly said to be the “observational consequence” of B14 and therefore not independent.  Claiming 13 independent constraints is internally contradictory.   Required fix Either drop B8 or re-count B14 so that the number of independent constraints is correct and consistent in all places (abstract, Sec. IX and Table II).
- **[OpenAI_methodology/P1A-E5/ESSENTIAL]**: P1A-E5 p. 10, Eq. (15)   Statement Δθone-loop/Δθobs ratio evaluated as 10−58…10−60.   Problem The equation misses a factor of 1/MPl in the numerator (dimension mismatch).  If restored, the quoted suppression becomes ≈1.2 × 10−60, not up to 10−58 as claimed.   Required fix Insert the missing factor, recompute the range, and update every place (text, Table II, abstract) where the 10−58–10−60 figure is quoted.
- **[OpenAI_methodology/P1A-E6/ESSENTIAL]**: P1A-E6 p. 11-12, Table II   Problem Barrier 8 (“Parity-even interaction”) and Barrier 14 (“Perturbation transparency”) eliminate the same observable channel.  Listing both in the table as distinct barriers overstates the number of independent mechanisms blocked.   Required fix Merge the two barriers or mark B8 as derivative (not independent).
- **[OpenAI_methodology/P1A-E8/ESSENTIAL]**: P1A-E8 p. 16, Table III   Problem Table reports a PTA spectral index γ = 2.567 ± 0.382 obtained with a “real-KDE GPU MCMC” that is not described anywhere in the manuscript.   Required fix Add a methods subsection that details the PTA data set, the likelihood construction, the KDE procedure, and chain diagnostics, or remove the number.

### `duplicate_phrase` — MINOR — _single-reviewer_ (1 reviewer)

Reviewers: OpenAI_methodology

- **[OpenAI_methodology/P1A-m2/MINOR]**: P1A-m2 p. 7, first paragraph: duplicate phrase “is aesthetic at this level rather than calculated” → remove duplication.

## Other findings (22)

- **[Gemini_cosmology/P1A-E1/ESSENTIAL]**: **P1A-E1: Fundamentally Flawed Dimensional Analysis of the Dark Energy Ansatz** *   **Location:** Section II.A.2 (p. 6), Appendix B (p. 19) *   **Problem:** The entire connection between the ECH parity-odd operator and dark energy rests on a "phenomenological on-shell scaling ansatz" that appears dimensionally inconsistent. Appendix B states that the operator in Eq. (6) leads to a Lagrangian term …
- **[Gemini_cosmology/P1A-M1/MAJOR]**: **P1A-M1: Opaque Derivation of One-Loop Suppression** *   **Location:** Section IV.B (p. 9) *   **Problem:** The argument to close Route 2 (one-loop graviton corrections) hinges on the dimensionless ratio in Eq. (15). The derivation of this ratio is not provided and is difficult to reconstruct. The expression `Δθ_one-loop / Δθ_obs ~ [α_em (H_0/M_Pl)] / [M_Pl (α/M) β_obs]` seems to be missing facto…
- **[Gemini_cosmology/P1A-M2/MAJOR]**: **P1A-M2: Idiosyncratic Jargon and Structure Obscures Physical Arguments** *   **Location:** Abstract, Section I, Section IX (p. 12) *   **Problem:** The paper is structured around a novel classification scheme of "7 foundation studies," "6 observational research branches," and "14 mechanism-class constraints" (or "barriers"). This terminology is idiosyncratic and creates a layer of jargon that ma…
- **[Gemini_cosmology/P1A-m1/MINOR]**: **P1A-m1: Misleading Language on Fine-Tuning** *   **Location:** Section XII.A (p. 15) *   **Problem:** The text describes a "fine-tuning reduction from 10^120 to 10^5". While the paper correctly clarifies this is a reparameterization of the problem into a sensitivity to `N_tot`, the initial phrasing is misleading and could be misinterpreted as a partial solution to the cosmological constant probl…
- **[Gemini_cosmology/P1A-m2/MINOR]**: **P1A-m2: Missing Derivation for Prefactor** *   **Location:** Section II.C.1 (p. 7), Section XII.A (p. 15) *   **Problem:** The `(T_reh/M_GUT)^3/2` prefactor in the inflationary dilution formula is justified on grounds of "dimensional-analysis aesthetic" and is acknowledged as not being rigorously derived. While the exponential term is dominant, this is a weakness in the quantitative argument. * …
- **[Gemini_cosmology/P1A-m3/MINOR]**: **P1A-m3: Future Publication Date** *   **Location:** Page 1 *   **Problem:** The paper is dated "June 2, 2026 PDT." This is presumably a typo. *   **Required Fix:** Correct the date to the date of submission.  ### NITs
- **[Gemini_cosmology/P1A-N1/MINOR]**: **P1A-N1: Outdated PACS numbers** *   **Location:** Page 1 *   **Problem:** The PACS (Physics and Astronomy Classification Scheme) system is obsolete. *   **Required Fix:** Remove the PACS numbers line.
- **[Gemini_cosmology/P1A-N2/MINOR]**: **P1A-N2: Unprofessional Contact Information** *   **Location:** Page 1 *   **Problem:** The email address `houston@hubify.com` is non-standard for an academic publication. *   **Required Fix:** The author should use an institutional, university, or professionally recognized email address.  ## Summary recommendation  **REJECT**  This manuscript attempts to tackle a significant problem in cosmology…
- **[OpenAI_methodology/P1A-E3/ESSENTIAL]**: P1A-E3 p. 6, Eq. (6)   Statement Parity–odd operator written with overall coefficient α/M; off-shell mass dimension is +1.   Problem A dimension-1 operator cannot be inserted in a 4-D action without additional powers of mass.  The mapping to a vacuum energy density in Eq. (B2) is therefore not an EFT derivation but a phenomenological guess; nevertheless it is used throughout the paper to set the a…
- **[OpenAI_methodology/P1A-E4/ESSENTIAL]**: P1A-E4 p. 7, Eq. (11)   Statement Inflationary dilution factor Dinf = exp[−3 Ntot] ×(Treh/MGUT)3/2.   Problem The exponent 3/2 is justified only by “phase-space aesthetics”; no derivation or citation is given.  Yet Dinf is used to translate the Planck-scale density to late-time ρΛ.   Required fix Provide a derivation (e.g. from a Boltzmann calculation) or drop the (Treh/MGUT)3/2 factor and re-comp…
- **[OpenAI_methodology/P1A-E10/ESSENTIAL]**: P1A-E10 Length   The manuscript is 21 pages but ~30 % is meta-discussion and duplicate caveats, obscuring the actual derivations.   Required fix Reduce to ≤14 typeset pages by removing repetition, internal notes, and forward references.  --------------------------------------------------------------------
- **[OpenAI_methodology/P1A-M1/MAJOR]**: P1A-M1 p. 5, Eq. (2)   The numerical spread “∼0.020” is called an “effective range” but later treated as an uncertainty.  Clarify that this is scheme dependence, not a statistical 1 σ error.
- **[OpenAI_methodology/P1A-M2/MAJOR]**: P1A-M2 p. 6, Step 3 (parity-odd effective action)   Text says α/M is “motivated by” Shapiro & Teixeira [20] but reference [20] treats a different operator.  Provide the correct citation or an explicit derivation.
- **[OpenAI_methodology/P1A-M3/MAJOR]**: P1A-M3 p. 8, galaxy spin null   The machine-learning classifier and its accuracy, purity, and systematics are deferred to Paper IV.  A one-paragraph summary is needed here; without it the reader cannot judge whether the “null” is statistically meaningful.
- **[OpenAI_methodology/P1A-M4/MAJOR]**: P1A-M4 Figs. 1 & 2   Axes lack units; several arrows cross without labels; Fig. 2 needs a numeric scale.  Both figures must be redrawn for clarity or moved to Supplementary.
- **[OpenAI_methodology/P1A-M5/MAJOR]**: P1A-M5 References   Several citations marked “(in preparation) (2026)” are nowhere accessible.  PRD requires that key supporting material be published or submitted.  Supply arXiv links or remove dependence on unpublished work.  --------------------------------------------------------------------
- **[OpenAI_methodology/P1A-m1/MINOR]**: P1A-m1 p. 4, Table I caption “fNL = −35/8 (Paper II forecastb)” → move footnote ‘b’ into main caption to avoid confusion.
- **[OpenAI_methodology/P1A-m3/MINOR]**: P1A-m3 p. 14, Eq. (23) missing factor of ½ in definition of Pontryagin density (check normalisation).
- **[OpenAI_methodology/P1A-m4/MINOR]**: P1A-m4 p. 19, Appendix B first paragraph “do not arise from off-shell EFT counting but from on-shell scaling assumptions applied to a Planck-scale bounce geometry” – stylistically confusing; please re-phrase.
- **[OpenAI_methodology/P1A-m5/MINOR]**: P1A-m5 Typos: “Domaga la–Lewandowski” → “Domagała–Lewandowski”; “Pop lawski” → “Popławski”.  -------------------------------------------------------------------- NITS --------------------------------------------------------------------
- **[OpenAI_methodology/P1A-n1/MINOR]**: P1A-n1 Repeated “tension resolution?” row in Table I ends with a dangling question mark; re-phrase.
- **[OpenAI_methodology/P1A-n2/MINOR]**: P1A-n2 Several occasions of “etc.” in technical sentences; replace by explicit items or delete.  -------------------------------------------------------------------- ## Summary recommendation
