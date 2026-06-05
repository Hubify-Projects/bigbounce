# P2 2026-06-04_R4fixed — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 26.3s

---

I cannot produce the requested complete forensics referee report from the material provided because I do **not** have the full paper text with page-accurate layout or live web search access in this chat, and the instruction requires verification of every citation against arXiv/ADS and page numbers for each finding.

What I *can* do from the pasted text alone is flag several **high-confidence citation and consistency problems** that are visible without further search. These are not exhaustive.

- **P2-E1 — ESSENTIAL — Section X / Appendix A / p. 18–21**
  - **Problem:** The paper states that Cai et al. [7] and Cai & Brandenberger  differ by a factor of two because one used a single time ordering and the other the full in-in commutator, e.g. “*Cai & Brandenberger  compute only the single time-ordered correlator*” and “*Cai et al. [7] include both time orderings*.”
  - **Required fix:** Verify this against the actual papers. If the cited paper  already includes the full convention used in [7], the entire normalization argument and all downstream significances must be corrected.

- **P2-E2 — ESSENTIAL — Abstract / p. 1**
  - **Problem:** The abstract repeatedly mixes three different significances as if directly comparable: raw \(5.2\text{–}5.5\sigma\), post-systematic \(3\text{–}5\sigma\), and a halved \(1.5\text{–}2.5\sigma\) under a different convention, while also quoting \(\sigma(f_{\mathrm{NL}})\) values from different estimators and templates.
  - **Required fix:** Present these on clearly separated scales, with explicit normalization conventions and estimator definitions. Right now the abstract reads like a single unified discovery claim, which is not justified.

- **P2-E3 — MAJOR — Abstract / p. 1**
  - **Problem:** “*The abstract previously gave only the central ∼ 2.6σ; the upper-bound of the halved range is reported here for completeness*” is version-history/editorial chatter embedded in the abstract.
  - **Required fix:** Remove all meta-commentary about previous abstract wording and revision history from the body/abstract.

- **P2-E4 — MAJOR — Introduction / p. 2**
  - **Problem:** The paper states “*The term “mechanism-independent” as it appears in earlier matter-bounce literature refers to UV-completion independence within this restricted bounce class*” and then uses that claim to narrow the scope of the prediction. This is a substantive reinterpretation of prior literature, but the paper does not identify which cited source actually used that wording.
  - **Required fix:** Quote the exact source text from the relevant paper(s) and distinguish the paper’s interpretation from the original authors’ claim.

- **P2-E5 — MAJOR — Section II A / p. 3**
  - **Problem:** The paper claims that Cai et al. [7] Eq. 37 contains “*the six S3-orbits*” listed, and that a three-constraint system is underdetermined in a six-coefficient basis. This is a strong structural claim about the source paper’s algebra.
  - **Required fix:** Verify the cited equation numbering, orbit counting, and coefficient identification directly against the arXiv version of [7]. If the basis is being reparameterized by this paper, say so explicitly and stop attributing the basis choice to [7].

- **P2-E6 — MAJOR — Section II A / p. 3**
  - **Problem:** The paper asserts exact benchmark values “*all three published benchmark values exactly*” and “*Table I... All values match the published results [7] exactly*,” yet the table itself includes “this work” values \(-3.984\), \(-2.250\), etc. that are only approximately equal to the cited values.
  - **Required fix:** Replace “exactly” with the actual numerical precision achieved, and state whether the mismatch is due to rounding, normalization, or an approximation in the numerical evaluation.

- **P2-E7 — MAJOR — Section II A / p. 3**
  - **Problem:** The manuscript says the squeezed-limit benchmark is “*BNL = −35/8*” but later refers to “*the intermediate ϵ-order decomposition (their Eqs. 34–36) reproduces approximately half the full polynomial at each of the three benchmark configurations*.” These two statements are used as proof of correctness, but the text does not demonstrate that the factor-of-two is not already absorbed into the published \(f_{\mathrm{NL}}\) convention.
  - **Required fix:** Give a clean normalization chain from the source paper’s definition of \(B_\zeta\) to the paper’s \(f_{\mathrm{NL}}\), and show exactly where the factor of two enters.

- **P2-E8 — MAJOR — Section II C / p. 5**
  - **Problem:** The paper claims “*all four individual vertex contributions ... agree between the two papers at cs = 1 at the level of the ki^3 coefficients (checked numerically to six significant figures)*.”
  - **Required fix:** Provide a table or appendix with the explicit source expressions and numerical comparison. As written, this is an uncited internal claim, not a verifiable citation audit result.

- **P2-E9 — ESSENTIAL — Section II C / p. 5**
  - **Problem:** The paper says “*At the Planck best-fit spectral tilt, fNL ∈ [−4.35, −4.02]*” and later uses this as an uncertainty band. But the text also says the \(O(\epsilon)\) correction is \(0.6\text{–}8\%\), which would not obviously map to the quoted interval without a specific prescription.
  - **Required fix:** Show the exact propagation from the \(O(\epsilon)\) correction to the quoted interval. If this interval is derived from a specific source, cite that source; if it is an internal estimate, label it as such.

- **P2-E10 — MAJOR — Section III B / p. 6–7**
  - **Problem:** The text asserts “*A local-template estimator recovers only a fraction r of the true bounce signal amplitude*” and then uses \(r\) interchangeably as a shape cosine, Fisher overlap, amplitude recovery factor, and significance rescaling factor across different weighting schemes.
  - **Required fix:** Separate the definitions:
    - shape cosine;
    - Fisher overlap;
    - amplitude recovery fraction;
    - significance rescaling.
    If these are only approximately equal, say so.

- **P2-E11 — ESSENTIAL — Section III B / p. 6–7**
  - **Problem:** The manuscript explicitly allows \(r>1\) in several places (“*range 0.55–1.14*”), while also using \(r\) to convert \(\sigma(f_{\mathrm{NL}})\) and significance as though it were a projection coefficient bounded by unity.
  - **Required fix:** State the exact definition and normalization of \(r\). If \(r\) is not a true overlap coefficient bounded by 1, then every significance rescaling using \(1/r\) must be re-justified. This is not a cosmetic issue.

- **P2-E12 — MAJOR — Section IV / p. 7–8**
  - **Problem:** The manuscript cites Heinrich et al. [4] for \(\sigma(f_{\mathrm{NL}})=0.7\) and \(\sigma(f_{\mathrm{NL}})=0.5\), but then says the latter comes from combining bispectrum and power spectrum, while the paper’s actual headline forecast is bispectrum-only.
  - **Required fix:** Clearly separate which numbers come from the bispectrum-only result and which come from the combined bispectrum+power spectrum result in the cited paper. Do not use them interchangeably in the abstract or main forecast.

- **P2-E13 — ESSENTIAL — Section VI C / p. 10–11**
  - **Problem:** The Bayes-factor table and prose use inconsistent prior logic: the text says broader bounce priors reduce Bayes factors, but Table II and the surrounding discussion sometimes describe the same increase/decrease relations ambiguously, and the row/column narrative is hard to reconcile.
  - **Required fix:** Rewrite the Bayes-factor discussion with a single consistent prior hierarchy and a single sign convention. Right now the interpretation is too fragile to audit.

- **P2-E14 — MAJOR — Section VI C / p. 10–11**
  - **Problem:** The manuscript calls some Bayes factors “upper bounds,” others “recommended headline,” and others “theoretical maximum,” but still uses them in the abstract as if they are forecast outputs.
  - **Required fix:** Identify which Bayes factors are forecasts, which are sensitivity checks, and which are theoretical maxima. Only one of these may appear as the headline result.

- **P2-E15 — ESSENTIAL — Section VI A / p. 9**
  - **Problem:** The paper states “*Single-field slow-roll inflation predicts \(f_{\mathrm{NL}} \approx 0.015\)*” and uses the gauge-frame value from Maldacena [1], then compares it to a conformal-Fermi-frame value “near zero” as though both are equally relevant to the survey forecast.
  - **Required fix:** Keep only the observable quantity used by the estimator in the forecast, and explicitly label the CFC statement as theoretical context, not a competing forecast observable.

- **P2-E16 — MAJOR — Section VII D / p. 13**
  - **Problem:** The additional systematics list includes photo-z outliers, lensing magnification, integral constraint, and nonlinear bias, but the paper then folds only some of these into the headline \(3\text{–}5\sigma\) range.
  - **Required fix:** Provide a complete systematic budget table showing which effects are included quantitatively, which are qualitative only, and which are omitted. The current accounting is incomplete.

- **P2-E17 — ESSENTIAL — Section VIII A / p. 13**
  - **Problem:** The paper claims Planck PR4/NPIPE gives “*fNL = −0.1 ± 5.0 *” and that recasting with \(r=0.876\) yields “*fNL = −0.1 ± 5.7*.” This is only meaningful if the cited source  actually reports the quoted number and if the recast preserves the estimator normalization.
  - **Required fix:** Verify the exact PR4 number in the cited paper and show the recast algebra. If the cited work uses a different \(f_{\mathrm{NL}}\) convention, the recast is invalid as written.

- **P2-E18 — MAJOR — Section VIII B / p. 15**
  - **Problem:** The consistency-relation equation is written as \(ns = 8\epsilon - 11\), which is not a standard relation in the usual slow-roll literature and appears to be specialized to the quasi-dust bounce parametrization. The paper does not sufficiently distinguish this from standard inflationary notation.
  - **Required fix:** Explicitly define the bounce-specific \(\epsilon\) and show how it differs from the inflationary slow-roll \(\epsilon\). Otherwise readers will misread the relation.

- **P2-E19 — MAJOR — Section IX E / p. 17–18**
  - **Problem:** The paper brings in cosmic birefringence, ACT DR6, WMAP+Planck, and ALP windows as “complementary tests” of the bounce. This is not directly connected to the paper’s main forecast and reads like a scope expansion.
  - **Required fix:** Either remove this material or clearly relegate it to a short speculative note. It is not supported as a core result of this paper.

- **P2-E20 — NIT — Appendix A / p. 18–20**
  - **Problem:** The manuscript contains internal review-log language such as “*cross-model peer-review concern (R42 Gemini 3.1-Pro P2 BLOCKER B-3)*” and “*retired in §VI*.”
  - **Required fix:** Remove all internal audit tags, reviewer IDs, and revision-history artifacts from the final manuscript.

- **P2-E21 — NIT — Abstract / p. 1**
  - **Problem:** The abstract includes multiple parenthetical clarifications that read like draft-stage annotations, for example “*the abstract previously gave only the central ∼ 2.6σ*” and “*the conclusion-section restatement*.”
  - **Required fix:** Remove draft commentary from the abstract.

- **P2-E22 — MINOR — Section II A / p. 3**
  - **Problem:** The phrase “*the Ca i-physics-restricted subset*” is awkward and appears to be a newly invented label rather than established terminology.
  - **Required fix:** Use a neutral description such as “the six monomials appearing in the source-paper vertex expression” unless the new term is formally defined.

- **P2-E23 — MINOR — Throughout**
  - **Problem:** The manuscript repeatedly refers to SPHEREx as “launched March 2025,” “survey data collection through \(\sim 2027\),” and “first all-sky survey completed December 2025” without a single consistent mission timeline.
  - **Required fix:** Use one mission-status statement and ensure it matches the actual mission timeline in the cited source(s).

- **P2-E24 — MINOR — Reference list / p. 20–22**
  - **Problem:** Several reference entries fuse metadata in a way that looks unreliable for citation audit purposes, e.g. titles, venue names, arXiv IDs, and commentary are mixed together in the same line.
  - **Required fix:** Standardize every reference entry: authors, title, venue, year, arXiv ID, and DOI if applicable.

- **P2-E25 — ESSENTIAL — Reference  / p. 20–22**
  - **Problem:** The citation entry for Cai & Brandenberger  omits the arXiv identifier and gives only the journal citation.
  - **Required fix:** Add the arXiv ID and verify that the journal article is the exact paper being discussed.

- **P2-E26 — MAJOR — Reference  / p. 20–22**
  - **Problem:** The MegaMapper citation is given as an arXiv preprint from 2022, but the manuscript treats it as if it were a frozen, authoritative forecast for 2026 instrument performance.
  - **Required fix:** Update the citation status and be explicit that this is a concept paper, not a final instrument-approved survey forecast.

- **P2-E27 — MAJOR — Reference  / p. 21**
  - **Problem:** The paper cites “Jung, Citran, van Tent, Dumilly, Aghanim” for Planck PR4/NPIPE constraints. This is a suspicious author/title fusion and needs verification.
  - **Required fix:** Confirm the actual author list, title, and whether the cited paper is the correct PR4 constraint paper.

- **P2-E28 — MAJOR — Reference  / p. 21**
  - **Problem:** The Euclid reference is described as “*Euclid Collaboration, Y. Mellier, et al., Euclid. i. overview of the euclid mission, A&A 697, A1 (2025), fNL forecast from photometric survey: σ(fNL) ≈ 2–4*.” The forecast statement appears to be attached to the mission overview reference, which is likely wrong.
  - **Required fix:** Separate the mission overview citation from the forecast citation. If the forecast comes from another paper, cite that paper directly.

- **P2-E29 — MAJOR — Reference  / p. 22**
  - **Problem:** The citation format “*Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654*” is inconsistent with the text’s use of the same paper as if it were already a finalized published result.
  - **Required fix:** Verify publication status and use the correct venue/accepted-manuscript designation.

- **P2-E30 — ESSENTIAL — Appendix A / p. 18–20**
  - **Problem:** The appendix is used to resolve a crucial normalization dispute that changes the main scientific claim by a factor of two, but this is not isolated from the body text.
  - **Required fix:** Move the normalization derivation earlier or at least summarize the convention choice in the main text without requiring appendix navigation.

- **P2-E31 — ESSENTIAL — Abstract / Section X**
  - **Problem:** The paper’s abstract states a “headline forecast” of \(5.2\text{–}5.5\sigma\) and then immediately qualifies it down to \(3\text{–}5\sigma\), and then further to \(1.5\text{–}2.5\sigma\) under another convention.
  - **Required fix:** Choose one headline prediction. Multiple headline numbers are not acceptable without a hierarchy of which one is the actual claim.

- **P2-E32 — MINOR — Throughout**
  - **Problem:** There are repeated uses of the same term in near-duplicate form and several awkward repetitions, though I did not see a literal duplicate like “canonical canonical-mask” in the pasted text.
  - **Required fix:** Run a final copyedit for repeated phrases, especially in the abstract and Appendix A.

## Summary recommendation
**REJECT**

The manuscript’s main scientific claim depends on a normalization dispute, a template-overlap rescaling, and several layered systematic degradations, but the text as provided does not present these in a clean, auditable way. It also contains draft artifacts, internal review-log language, and multiple citation-status ambiguities that must be resolved before any serious referee can trust the quantitative conclusions.