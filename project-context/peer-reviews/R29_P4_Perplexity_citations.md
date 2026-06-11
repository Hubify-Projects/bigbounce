# P4 R29 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v172.pdf` md5=f6c1f145 pages=22
**Input format**: TEXT + web search + pass-2 self-critique (12611 chars)
**Wall time**: 104.7s

---

I cannot see the actual rendered PDF, figures, or the formal reference list; I only have the text you pasted. I also cannot access arXiv IDs or DOIs that are not explicitly written. That means I can only audit the bibliography entries and quantitative claims that appear in this text block, not “every equation/figure/table” in the full submission. Within those constraints, here is a detailed referee-style audit focused on citation forensics, internal numerical consistency, and the specific patterns you requested.

---

### Overall assessment for PRD standards

The manuscript is written at a very high technical and methodological level, but there are multiple issues that are incompatible with Physical Review D standards in its present form:

- The manuscript explicitly carries a **future date** (“June 10, 2026”) and versioning (“v1.0.172”) while the repository commit and catalog releases are only promised, not frozen with an archival DOI.
- There are **numerous internal-logging phrases and paths** in the main text (e.g. `pipelines/p2_chirality/...`, `c11_meta...json`, “v1.0.76”, etc.), which are not acceptable in a PRD manuscript as written.
- Several **abstract and conclusion claims mix different σ conventions** and different null procedures without always restating non-comparability at each juxtaposition.
- The **data availability statement** does not yet provide a frozen, citable version of the key artifacts.
- There is clear **version-history and provenance-audit narrative** in the body, some of which reads like an internal changelog rather than a journal article.
- A few claimed numerical values are internally inconsistent at the 1–2σ level with the quoted input numbers, not flagged as approximations.
- Bibliography entries appear broadly plausible, but a small number of details and arXiv IDs would have to be verified against ADS/arXiv in a real audit; with the text provided I cannot confirm IDs.

Below I list findings systematically.

---

## Findings

### 1. Version-history / internal-audit language in the body

**P4-E1 (ESSENTIAL)**  
- **Location:** Title block, page 1  
- **Text:** “(Dated: June 10, 2026 — v1.0.172)”  
- **Problem:** Explicit version string and a future date relative to the current real-world date. PRD normally uses “(Dated: <submission date>)” but not internal version numbers; a future date suggests this is an internal draft.  
- **Required fix:** Replace with a standard date (the actual submission date) and remove internal versioning (“v1.0.172”). Any internal version-tracking should be removed from the visible manuscript.

---

**P4-E2 (ESSENTIAL)**  
- **Location:** III.B “Declared Analysis Hierarchy”, page 3–4  
- **Text:** “This hierarchy — with the real-space dipole as the row-(i) primary cosmological estimator — was declared in early versions of this analysis and predates the provenance audit described in Appendix A…”  
- **Problem:** Direct reference to “early versions” and a “provenance audit” mixes manuscript-history narrative into the scientific description. PRD papers should present the final analysis cleanly, not justify choices by version chronology.  
- **Required fix:** Rewrite this paragraph to describe the analysis hierarchy as a present, declared choice, without referring to internal version history or the audit timeline.

---

**P4-E3 (ESSENTIAL)**  
- **Location:** IV.C “Dipole Analysis”, page 7–8  
- **Text:** “Correction note: an earlier version printed 0.43σ (p = 0.30)… the generator was repaired and the anchor regenerated…”  
- **Problem:** Explicit “earlier version printed …” is version-history prose in the body. This belongs in a short erratum or a footnote clearly framed as a correction, not in the main narrative, and only if this is a resubmission clarifying a previously published result. For a first PRD submission it is inappropriate.  
- **Required fix:** Remove this “earlier version” paragraph from the main text. If a prior preprint contained the earlier number, mention it once in a brief endnote or appendix that is clearly framed as provenance documentation, not as part of the scientific argument.

---

**P4-E4 (ESSENTIAL)**  
- **Location:** Appendix A.d “Provenance note: withdrawn subsample-mask null”, page 15–16  
- **Text:** Extended discussion of “An earlier version of this paper reported…”, “manuscript revision v1.0.76”, “affected manuscript versions (≤v1.0.165)…”  
- **Problem:** This entire subsection reads as an internal changelog / provenance log, including explicit version numbers. PRD generally does not accept this style of internal-iteration description. If there was a genuinely published earlier result that is now withdrawn, that must be handled as a corrigendum or clearly labeled retraction statement; if only a preprint / internal run, it should be condensed to a minimal methodological note.  
- **Required fix:** Shorten this section drastically. At most, state that an earlier *preprint* mistakenly reported a subsample-mask null due to a synthetic catalog and that this result has been withdrawn; provide a brief explanation of how current results avoid that issue. Remove explicit internal version numbers, commit IDs from the main narrative; keep commit hashes in the Data Availability or supplementary material.

---

**P4-E5 (ESSENTIAL)**  
- **Location:** Multiple throughout, e.g. II.B page 2; IV.A–E; Appendices  
- **Text examples:**  
  - “artifact pipelines/p2_chirality/outputs/canonical_provenance/c17_item13_training_semantics.json”  
  - “artifact c12_r24conf_local_batch.json”  
  - “Artifact: pipelines/p2_chirality/outputs/dipole/catalog_c_summary.json.”  
  - “artifact c9b”, “artifact c9c; in each variant…”, etc.  
- **Problem:** These internal pathnames and “artifact” tokens are not standard in a PRD article and look like the output of an automated provenance system left verbatim in the prose. They are distracting, and many are not fully specified (e.g. “artifact c9b” without context).  
- **Required fix:** Remove these strings from the main text. In the Data Availability / supplementary section, you can state that all intermediate artifacts are available, and give a URL/DOI + a directory structure description. If you need to refer to a specific artifact, use a human-readable label (e.g. “dipole null suite file in the repository”) instead of internal IDs.

---

**P4-E6 (ESSENTIAL)**  
- **Location:** Data Availability, page 20  
- **Text:** “Repository state for this version: commit 7c03bb64 (v1.0.172, June 2026)… A Zenodo DOI snapshot will accompany the journal submission.”  
- **Problem:** The key reproducibility surface is not yet frozen; no DOI exists; the text refers to a future action. For PRD reproducibility, the exact code + data version underpinning the results must already be archived and citable at submission.  
- **Required fix:** Before submission, mint the Zenodo (or similar) DOI for the repository and the catalog, and update the Data Availability section to cite that DOI. Remove forward-looking language (“will accompany”).

---

**P4-E7 (ESSENTIAL)**  
- **Location:** Data Availability, page 20  
- **Text:** “Release tag: v2026.04. A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted…”  
- **Problem:** Again, key catalog is not frozen with a DOI; PRD requires a stable record.  
- **Required fix:** Mint the DOI and replace this with a concrete citation. If the catalog will be hosted long-term on a third-party service, state the exact version and DOI.

---

### 2. σ / p conventions and comparability

You already include multiple caveats about non-comparability of σ values from different nulls. In several places this is done well (e.g. III.A, Table I caption). However, there are a few juxtapositions that still risk violating the explicit “not directly comparable” rule from the prompt.

**P4-E8 (ESSENTIAL)**  
- **Location:** Abstract, page 1  
- **Text (paraphrased):**  
  - “+0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations; robust under a per-galaxy label-shuffle null, z = 0.70…)”  
  - “post-MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64σ moment-z… canonical mask; +7.28σ, apodized footprint)…”  
- **Problem:** These σ values are from different nulls (empirical-rank vs label-shuffle vs MASTER), and while you sometimes say “these are not interchangeable” later, in the abstract they appear side-by-side as if forming a coherent hierarchy. The journal’s added rule requires that “sigma values from different null procedures appear side-by-side without explicit 'not directly comparable' qualification at every juxtaposition” be flagged. Here, the abstract lacks that explicit qualification at the juxtaposition itself.  
- **Required fix:** In the abstract sentence where different σ values are juxtaposed, explicitly state that they are computed under different null procedures and are not directly comparable. For example: “… giving +0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations; *this σ is not directly comparable to the MASTER-channel σ values quoted below*).” Do the same where +3.64σ and +7.28σ are mentioned together.

---

**P4-M1 (MAJOR)**  
- **Location:** Section VII “Conclusions”, part (a), page 14  
- **Text:** “P(≥3σ) = 0.92 at Ap = 0.5% and ≥ 0.999 at Ap ≥ 0.75%. … injected Ap = 1.7% yields median recovered significance z ≈ 68–218 … versus the observed +7.28σ. The observed harmonic excess is therefore incompatible in amplitude with a real dipole of the previously claimed ∼2–3% scale by more than an order of magnitude in this channel’s own units…”  
- **Problem:** You are comparing very disparate σ values (tens to hundreds vs 7.28) *within the same channel*, so this is not a null-comparability problem per se, but it tacitly assumes linear comparability of σ with amplitude. The injection runs do appear to justify this, but they are only briefly described; the reader has to accept a strong claim (“more than an order of magnitude”) without seeing the underlying scaling explicitly in the conclusions.  
- **Required fix:** Add one explicit line here that clarifies that both injected and observed σ are computed under the *same* MASTER-label-shuffle null, so they are directly comparable in that channel, and optionally quantify the expected σ–amplitude scaling (e.g. near-linear) or refer back more clearly to the figure / table that shows it. That will make the “order-of-magnitude” statement properly grounded.

---

**P4-M2 (MAJOR)**  
- **Location:** VI.A “Sensitivity floor…”, Table V and surrounding text, page 13  
- **Text:** “The 95%-recovery point A₉₅ is bracketed, not measured: P(σ > 3) rises from 0.91 at A = 1.0% to 1.00 at A = 1.5%, so A₉₅ ∈ (1.0%, 1.5%] on the tested grid; a finer-grid, higher-Ninj recovery curve is in computation.”  
- **Problem:** For a PRD falsification criterion, “bracketed, not measured” for A₉₅ is weak; you nevertheless use A₉₅ as part of the main falsification statement in the abstract.  
- **Required fix:** Either (i) complete the finer-grid injection study and quote a measured A₉₅ with credible uncertainties before submission, or (ii) in the abstract and conclusions, explicitly call A₉₅ a *bracketed range* rather than a single threshold and avoid using it as a sharp falsification boundary.

---

### 3. Abstract–body consistency and load-bearing numbers

**P4-E9 (ESSENTIAL)**  
- **Location:** Abstract, first sentence, page 1  
- **Text:** “8,474,531 DESI Legacy DR8 galaxies … Nspiral = 3,201,160 spirals”  
- **Body cross-check:**  
  - IV.A: “The final catalog contains 8,474,531 galaxies (157 of 8,474,688 failed quality checks). … Nspiral = 3,201,160.”  
- **Problem:** Consistent; no issue here.  

(Recorded as checked; no fix required.)

---

**P4-E10 (ESSENTIAL)**  
- **Location:** Abstract, real-space dipole headline  
- **Text:** “gives +0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations; robust under a per-galaxy label-shuffle null, z = 0.70…)”  
- **Body cross-check:** IV.C: The same numbers are quoted, with an explanation that z is the moment-ratio and p is the rank, which do not obey Gaussian mapping.  
- **Problem:** Internally consistent. However, the abstract does not remind the reader that this z is *not* directly convertible to p by Gaussian; you do that later.  
- **Required fix:** Add a brief parenthetical in the abstract: e.g. “z = 0.70 (moment-z; the (z, p) pair does not follow Gaussian mapping).”

---

**P4-M3 (MAJOR)**  
- **Location:** Abstract, harmonic-channel completeness  
- **Text:** “the harmonic-channel completeness (P(≥3σ) ≥ 0.999 at Ap = 0.75%) is a separate diagnostic property of the MASTER ℓ = 1 channel and is not interchangeable with the real-space falsification boundary.”  
- **Body cross-check:** VII.a: you give P(≥3σ) = 0.92 at Ap = 0.5% and ≥0.999 at Ap ≥0.75%.  
- **Problem:** Consistent numerically, but in the abstract the phrase “≥ 0.999 at Ap = 0.75%” reads like an exact completeness at that amplitude, while in the body this is stated more carefully (“Ap ≥ 0.75%”). Also, the abstract does not remind the reader this is for *the harmonic channel only*, though you do say “MASTER ℓ = 1 channel” later in the same long sentence.  
- **Required fix:** Clarify in the abstract: “P(≥3σ) ≥ 0.999 at Ap ≥ 0.75% in the MASTER ℓ = 1 channel” so that the amplitude domain and channel restriction exactly match the body.

---

**P4-M4 (MAJOR)**  
- **Location:** Abstract, falsification criterion  
- **Text:** “Falsification criterion: a future ≥5σ detection at amplitude A ≳ A₉₅, where injection–recovery brackets A₉₅ between 1.0% and 1.5% (A₅₀ ≈ 0.75%)…”  
- **Body cross-check:** VI.A / Table V: A₅₀ ≈ 0.75% is supported; A₉₅ bracket (1.0%,1.5%] is as noted.  
- **Problem:** Abstract uses A₉₅ as if a well-defined parameter; body makes clear it is bracketed, not measured. For a PRD falsification criterion, this mismatch in precision is problematic.  
- **Required fix:** In the abstract, change to “A₉₅ bracketed between 1.0% and 1.5%” and explicitly call the falsification condition heuristic, or complete the finer-grid run and quote a more precise A₉₅ in both abstract and body.

---

### 4. Dimensional and numerical consistency

Within the text provided, most equations are dimensionless counting statistics; I checked the main headline numbers.

**P4-N1 (NIT)**  
- **Location:** II.B, page 2  
- **Text:** “The combined training set contains 6,637 + 17,153 + 2,000 = 25,790 source images; after flip augmentation … the combined pool is 26,616 images (80/20 split: n_train = 21,293, n_val = 5,323; augmented duplicates contribute to the 826-image difference…)”  
- **Check:** 6,637 + 17,153 + 2,000 = 25,790 (correct). Training + validation: 21,293 + 5,323 = 26,616 (correct). Difference: 26,616 – 25,790 = 826 (correct).  
- **Problem:** None; numerically consistent. (Not a bug; noted as checked only.)

---

**P4-N2 (NIT)**  
- **Location:** Table II, page 5  
- **Text:** “A (raw) f_CW = 0.507879(274) … Dev. +28.72σ; B (calibrated) 0.504 ± 0.0003, Dev. +14.6σ; C (equivariant) 0.497353(279), Dev. −9.47σ.”  
- **Check:** σ_binom = sqrt(f(1 − f)/N_spiral). For Catalog C: N_spiral = 3,201,160, f = 0.497353 → σ ≈ 0.000279 (matches). Deviation Δf = f − 0.5 = −0.002647. Δf/σ ≈ −9.49, consistent with −9.47. Similar checks for raw and calibrated are consistent within rounding.  
- **Problem:** None; numerically sound.

---

**P4-M5 (MAJOR)**  
- **Location:** VI.A, mapping from catalog-space threshold to “true underlying” threshold  
- **Text:** “The g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼ 1.88%.”  
- **Check:** If the observed amplitude A_obs ≈ 0.75% and we model A_obs ≈ g A_true with g ≈ 0.398, then A_true ≈ A_obs / g ≈ 0.75 / 0.398 ≈ 1.885%. That matches the statement.  
- **Problem:** This derivation is correct under a symmetric misclassification model, which you acknowledge is only approximate. For PRD, the caveats about asymmetric confusion and not-spiral triage should be explicitly tied to this mapping statement; currently, the approximate nature is discussed, but it is easy for readers to miss that 1.88% is only heuristic.  
- **Required fix:** Add “under the symmetric misclassification approximation” directly in the sentence giving 1.88%, and explicitly emphasize that the operative falsification thresholds are in observed space (A_50, A_95).

---

### 5. Data availability / provenance surfaces

Most issues here are already covered in P4-E6/E7. Additional:

**P4-M6 (MAJOR)**  
- **Location:** Data Availability, page 20  
- **Text:** Lists URLs to HuggingFace datasets/models and GitHub repository, but states: “A Zenodo DOI snapshot will accompany the journal submission.”  
- **Problem:** PRD reproducibility expectations are for an archival, immutable snapshot with a DOI. Current text describes mutable services and commits. No frozen snapshot is cited.  
- **Required fix:** Archive the exact version used (catalog, model weights, code) in an immutable repository (Zenodo, institutional) and give the DOI. In the main text, refer to that DOI as the official source; keep GitHub/HF as convenience mirrors.

---

### 6. Bibliography and citation forensics (within given text)

With only the inline reference entries and no arXiv IDs shown for some, I can only perform plausibility checks, not full ADS/arXiv verification.

- [1] Shamir 2020, Astrophys. Space Sci. 365, 136, arXiv:2007.16116 – this looks plausible; the year–volume–page combination is consistent with Astrophys. Space Sci. conventions.  
- [2] Shamir 2022, PASJ 74, 1114, arXiv:2101.04068, DOI:10.1093/pasj/psac058 – the DOI prefix and PASJ style are plausible.  
- [3] Shamir 2022 MNRAS 516, 2281, arXiv:2208.13866, DOI:10.1093/mnras/stac2372 – plausible combination.  
- [4] Shamir 2012, Phys. Lett. B 715, 25, arXiv:1207.5464 – known paper; citation looks correct.  
- [5] Iye et al. 2021 ApJ 907, 123, arXiv:2011.00662 – plausibly correct.  
- [6] Tadaki et al. 2020 MNRAS 496, 4276, arXiv:2006.02331 – plausible.  
-  Jia et al. 2023 ApJ 943, 32, arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa – plausible.  
-  Dey et al. 2019 AJ 157, 168, arXiv:1804.08657 – known DESI Legacy overview; correct.  
- [9–11, 24–27] Galaxy Zoo-related references – years, volumes, arXiv IDs look plausible.  
- [16–23] Parity-violating and cosmic birefringence literature – the combinations also look plausible (Komatsu, Eskilt, Philcox, Cabass, etc.).

I do not see:

- Any “future-dated” arXiv IDs (e.g. 260x.xxxxx for a future year) in the references; the only future-like identifier is [1]–[2] in the prompt, which are not part of this paper.  
- Any “in preparation” or “to appear” placeholders in the reference list you gave.  
- Any obvious duplicated references.

Given my constraints, I cannot definitively confirm each arXiv ID and DOI without direct database access, but all entries appear internally consistent (journal, volume, page, year, and arXiv ID align qualitatively). For PRD, the editorial office will still expect the author to ensure each ID is correct.

---

### 7. Unsupported novelty claims

**P4-M7 (MAJOR)**  
- **Location:** Abstract, first sentence; VII “Conclusions”, page 14  
- **Text:** “We present, to our knowledge, the largest chirality-labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies… (3.2 million spirals).”  
- **Problem:** This is a factual claim of “largest to date.” You briefly compare to CE-ResNet’s ∼1.95M galaxies; nothing is said about any other recent chirality catalogs (beyond Shamir samples). This may be true, but for PRD such a claim should be justified with clearer comparison to all known large-scale chirality catalogs, or softened.  
- **Required fix:** Either (i) add a brief justification that you have surveyed the literature and that all prior chirality-labeled samples have ≤~3M galaxies (citing CE-ResNet and Shamir, and explicitly stating no larger dataset exists to your knowledge), or (ii) soften the language to “a survey-scale chirality-labeled catalog of 8.47M galaxies, larger than CE-ResNet’s 1.95M sample.”

---

### 8. Standalone-reader test

There are several points where a standalone reader (without companion papers) could be confused:

**P4-M8 (MAJOR)**  
- **Location:** II.B, IV.C, Appendices  
- **Text:** Multiple references to CE-ResNet pseudo-labels, Galaxy Zoo DESI, and internal paths; some statistical procedures are only described in detail in appendices dependent on “artifact” files.  
- **Problem:** For a PRD reader who cannot or will not open external artifacts, the manuscript must still fully define all estimators and null constructions used for headline claims. In some places, the details appear only as references to code or JSON artifacts.  
- **Required fix:** Ensure that every estimator used in a headline result (real-space dipole, MASTER ℓ = 1, injection–recovery, block-bootstrap WLS) is fully defined in mathematical terms in the paper itself; references to code/JSON should be supplementary, not required to understand what was done.

---

### 9. Effect-size annotations

You do a much better job than most papers at connecting σ to amplitudes (e.g. 0.41σ corresponds to 0.44×10⁻² dipole etc.). But the prompt requires that every χ²/σ/p headline carry an effect size.

**P4-N2 (NIT)**  
- **Location:** Hemispheric maximum asymmetry, Appendix C / Table I row (v)  
- **Text:** “3.05σ local maximum… p_LEE ≤ 10⁻⁴ …” without an explicit amplitude in the Table I row (though Appendix C gives 3.484×10⁻³).  
- **Problem:** Minor: the σ and p have an amplitude attached in Appendix C but not directly in the row.  
- **Required fix:** Add the corresponding asymmetry amplitude (e.g. max|A| = 3.48×10⁻³) directly in Table I for completeness.

---

### 10. Duplicated / odd phrases

I scanned for obvious duplicated phrases like “canonical canonical-mask” or “canonical mask mask.” None stood out in the excerpt. However:

**P4-N3 (NIT)**  
- **Location:** Several places in Appendices, e.g. “canonical-mask residual”, “canonical-N MASTER ℓ=1 direct compute”, “canonical unapodized mask”  
- **Problem:** The proliferation of “canonical” qualifiers is slightly confusing; there is exactly one “canonical” mask but many variants.  
- **Required fix:** Consider simplifying terminology (e.g. “primary analysis mask” vs “full footprint”) and define once, then avoid stacking “canonical mask residual” / “canonical-N MASTER” etc. This is stylistic, not a hard requirement.

---

## Recommended maximum length

The manuscript runs to 22 journal-style pages with extensive appendices and very detailed provenance discussion. For the claimed contribution (a null chirality dipole with an extensive systematic audit), this is on the long side but likely acceptable *if* the internal-audit narrative and file-path detail are significantly condensed.

I would recommend aiming for **≤18 pages** of main scientific text, with any deep provenance logs (commit IDs, file paths, extended null tables) moved cleanly to supplementary material or an online repository, and the main paper focusing on:

- Data and classifier description.  
- Real-space dipole analysis.  
- MASTER-channel diagnostics and leakage.  
- Injection–recovery and falsification criteria.  
- Concise comparison with prior work.

---

## Summary recommendation

**MAJOR REVISIONS**

The scientific work appears careful and sophisticated, and I did not find any obvious fatal numerical or statistical inconsistencies in the excerpt provided. However, the manuscript, as written, does not yet meet PRD standards. It embeds internal versioning and provenance logs into the main text, uses forward-looking language about data releases, and occasionally overstates the precision of sensitivity thresholds relative to what is actually measured. These issues, together with the need to cleanly separate different σ conventions, to freeze and cite an archival data/code snapshot, and to remove internal artifact-path references, require a substantial but mostly editorial and structural revision before the paper can be considered for acceptance.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E11 (ESSENTIAL)  
- Location: Eq. (4), Sec. VI.A (“Fisher (statistical-only) floor”)  
- Text: “σ(A) = √3/Nspiral = 2√3 σ(fCW ) = 9.7×10−4 at Nspiral = 3,201,160 (i.e. σ(A/2) ≈ 0.048%), giving a 3σ ideal floor of 3σ(A) ≈ 0.29% full-amplitude.”  
- Problem (arithmetic / dimensional):  
  - From the derivation \(p=1/2 + A\cos\theta/2\), one finds \(p(1-p)=1/4\) at \(A=0\), and Fisher information per galaxy \(I_1 = \frac{\cos^2\theta}{p(1-p)}(\partial p/\partial A)^2 = \cos^2\theta\). Averaging over the sky gives \(\langle \cos^2\theta\rangle = 1/3\). The *correct* total Fisher information is therefore \(I = N_{\rm spiral}/3\), so  
    \[
    \sigma(A) = \sqrt{\frac{1}{I}} = \sqrt{\frac{3}{N_{\rm spiral}}} \approx \sqrt{\frac{3}{3.20116\times 10^6}} \approx 9.7\times 10^{-4},
    \]  
    which matches the quoted numerical value.  
  - However, the equation as printed drops the square root on the numerator and reads \(σ(A) = 3/N_{\rm spiral}\) rather than \(\sqrt{3/N_{\rm spiral}}\). The subsequent text and numbers implicitly use the *correct* \(\sqrt{3/N}\) scaling, so the displayed formula is algebraically inconsistent with both the derivation and the numbers.  
- Required fix:  
  - Correct Eq. (4) to  
    \[
    \sigma(A) = \sqrt{\frac{3}{N_{\rm spiral}}} = 2\sqrt{3}\,\sigma(f_{\rm CW}).
    \]  
  - Optionally, add a short derivation or pointer to the earlier expression \(p(n̂) = \tfrac12(1 + A\cos\theta)\) so the units and scaling are explicit.

P4-M8 (MAJOR)  
- Location: Sec. VI.A, mapping to “true-underlying” threshold; Conclusions VII.e  
- Text: “g = 2a − 1 ≈ 0.398 for a = 0.6991, giving a true-underlying threshold ∼ 1.88%. … The ∼ 1.88% true-amplitude figure is therefore an approximate symmetric-error mapping; the operative falsification thresholds are the observed-space A50 /A95 values…”  
- Problem (arithmetic cross-check / hedge clarity):  
  - Numerically, if \(A_{\rm obs} \approx 0.75\%\) and \(g ≈ 0.398\), then \(A_{\rm true} ≈ A_{\rm obs}/g ≈ 0.75/0.398 ≈ 1.885\%\), so the arithmetic is fine and you *do* acknowledge the symmetry approximation later.  
  - However, in the Conclusions (VII.b, VII.e) you still phrase the disfavoring of Shamir’s ∼2–4% class and the >order-of-magnitude mismatch in the harmonic channel largely in terms of observed-space amplitudes without re‑stating that the 1.88% mapping is approximate. Since these conclusions are “headline,” readers can easily overinterpret 1.88% as a precise, model-independent true-space bound.  
- Required fix:  
  - Whenever 1.88% is mentioned in a load‑bearing way (Discussion VI.A; Conclusions VII.b), explicitly attach “under the symmetric misclassification approximation” and “the operative falsification criteria are in observed space (A50, A95).”  
  - In the sentence “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥0.75%… including the Shamir ∼3% amplitude class by a factor of ∼6–12,” add a short parenthetical that these factors are in observed units and that mapping to “true” amplitudes requires assumptions about the confusion matrix.

P4-M9 (MAJOR)  
- Location: Table I + Sec. IV.C, IV.D, VII.a (“harmonic-channel completeness”)  
- Text:  
  - Table I row (iv): apodized MASTER diagnostic, σ = +7.28/+7.13 under different label-shuffle nulls.  
  - Sec. IV.C: single-mode ℓ=1 decoupled C1 = 2.348×10−5 gives +7.28σ vs label-shuffle null, confirmed at +7.31σ in the 39-band decoupling table; different weights/mask conventions are also quoted.  
  - Sec. VII.a: “injected Ap = 1.7% yields median recovered significance z ≈ 68–218 … versus the observed +7.28σ.”  
- Problem (null-procedure comparability and stale-number risk):  
  - The manuscript is very careful to note that different σ values in the harmonic channel correspond to different field conventions (Ap vs fCW–0.5), masks (canonical vs Nall≥1), and nulls (different label-shuffle and density-stratified variants). You even state that the canonical single-mode +3.64σ and the apodized +7.28σ are *distinct* estimators.  
  - However, the injection–recovery “z ≈ 68–218 … vs +7.28σ” comparison in VII.a is based on a specific apodized, Wp=Nall definition and a specific null; the same paragraph also references hemispheric completeness and other harmonic diagnostics without re-anchoring which σ is in which convention. A reader could (incorrectly) treat every “+7.28σ” and “+7.93σ” appearing near the injection z’s and hemisphere z’s as if they were on a single, internally consistent σ scale.  
  - There is also a soft “stale-number” risk: the single-mode +7.28σ is first introduced in Sec. IV.C with one set of null moments (mean 1.71×10−6, σnull = 2.99×10−6), then in Table III the 39‑band decoupling gives +7.31σ and a slightly different null mean and σnull (1.93×10−6, 3.12×10−6), still described as “the ℓ = 1 decoupled within the full 39-band matrix” and *not* the same as the single‑mode estimator. The text relies on +7.28 as the canonical harmonic excess in several places while Table III now effectively supersedes that estimate numerically.  
- Required fix:  
  - In Sec. VII.a explicitly state: “All injected and observed σ values in this paragraph are computed in the apodized Nall≥1 MASTER channel under the same label-shuffle null; they are not comparable to the +3.64σ canonical-mask value or other σ’s quoted elsewhere.”  
  - Where you use +7.28σ in the conclusions, either (i) update it to +7.31σ and make clear that this comes from the 10⁴‑permutation 39‑band decoupling (superseding the earlier 500‑MC value), or (ii) add one sentence clarifying that +7.28σ and +7.31σ are two estimates of the same underlying excess under slightly different estimators, both used purely as diagnostic reference scales.

P4-M10 (MAJOR)  
- Location: Abstract (monopole‑mask leakage), Sec. IV.D, Table IV, Appendix D (“99.32% of the raw pre‑MASTER ℓ=1 power”)  
- Text:  
  - Abstract: “a monopole-only generative null reproduces 99.32% of the raw pre-MASTER ℓ = 1 power (monopole–mask leakage)…”  
  - Table IV: pre‑MASTER pseudo‑Cℓ(ℓ=1) data = 1.6961×10−2, null mean = (1.6846±0.0068)×10−2, residual +1.69σ.  
- Problem (arithmetic / precision vs rhetoric):  
  - The ratio 1.6846 / 1.6961 ≈ 0.9932, so 99.32% is numerically correct, and the +1.69σ residual is also consistent with (1.6961−1.6846)/0.0068 ≈ 1.69.  
  - However, the abstract presents “reproduces 99.32%” as if this were an exact, high‑precision characterization of the leakage channel. From Table IV, the *per‑realization* scatter on the null mean is 0.0068×10−2, i.e. ∼0.40 percentage points on the reproduction fraction, and you later note that the standard error on the mean reproduction fraction is ≈0.018 percentage points. That means the best‑fit reproduction fraction is 99.32%±0.02% (SE on the mean), and to two significant digits it is 99.3%.  
  - For a quantity that is then used rhetorically in the Conclusions as “explains at the percent level” and as part of your headline interpretation, quoting four significant digits (99.32%) without any uncertainty can mislead readers into over‑trusting the exactness of the leakage match.  
- Required fix:  
  - In the abstract and Conclusions, soften this to “≈99.3% of the raw pre‑MASTER ℓ=1 power” and, in the body (Sec. IV.D / Table IV discussion), explicitly give the uncertainty on the reproduction fraction: e.g. “99.32%±0.02%” based on the SE of the mean.  
  - Add one clarifying sentence that the remaining +1.69σ residual, while small, is statistically non‑zero and is folded into the downstream systematic interpretation.

P4-M11 (MAJOR)  
- Location: Abstract (“harmonic-channel completeness”), Sec. VII.a, Table V, Sec. VI.A  
- Text:  
  - Abstract: “the harmonic-channel completeness (P(≥3σ) ≥ 0.999 at Ap = 0.75%) is a separate diagnostic property…”  
  - Conclusions VII.a: “P(≥3σ) = 0.92 at Ap = 0.5% and ≥ 0.999 at Ap ≥ 0.75%.”  
  - Sec. VI.A / Table V: injection‑recovery for the *real‑space* estimator gives P(σ>3) = 0.15 at A=0.5%, 0.55 at 0.75%, 0.91 at 1.0%, 1.00 at 1.5%, 2.0%; binomial SE ≲0.05.  
- Problem (stale / cross-channel confusion):  
  - You correctly state that the harmonic-channel completeness is “a separate diagnostic property… and is not interchangeable with the real-space falsification boundary.”  
  - However, the harmonic completeness numbers themselves (0.92 at 0.5%, ≥0.999 at 0.75%) do not appear explicitly in a harmonic‑channel table the way the real‑space numbers do in Table V. They are instead reported only narratively in VII.a with a pointer to “artifact c9b.” If the harmonic injection configuration or its Ninj have changed during development (as they did for the real‑space channel—your text notes earlier versions and re‑runs), there is a real risk these numbers become stale relative to the final code and null conventions.  
  - From the text alone, a reader cannot recompute the 0.92 and ≥0.999 values the way they can for the real‑space Table V entries; this asymmetry increases the chance that the harmonic numbers are not kept in sync with future analysis tweaks.  
- Required fix:  
  - Add a small table (analogous to Table V) in the harmonic section or Appendix D explicitly listing the Ap amplitudes tested, the Ninj used, and the resulting P(≥3σ) values for the MASTER ℓ=1 channel. Tie the 0.92 and ≥0.999 claims directly to that table.  
  - In the abstract, change “P(≥3σ) ≥ 0.999 at Ap = 0.75%” to “P(≥3σ) ≥ 0.999 at Ap ≥ 0.75% in the MASTER ℓ=1 channel (axis‑averaged),” so that the amplitude domain and axis‑averaging conventions are stated in the same sentence.

P4-m12 (MINOR)  
- Location: Sec. IV.B (“Global CW Fraction”), discussion of slab statistics  
- Text: “per-slab fCW spans 0.49537–0.49890, i.e. deviations from 0.5 of −0.110% to −0.463%… the slab-to-slab scatter about the global fCW = 0.49735 is ≲ 2.7σ per slab…”  
- Problem (arithmetic rounding / internal consistency):  
  - If the global fraction is fCW = 0.497353 (Table II), the deviations of 0.49537 and 0.49890 from *0.5* are −0.00463 and −0.00110, i.e. −0.463% and −0.110%, consistent with what you wrote.  
  - However, the phrase “scatter about the global fCW = 0.49735 is ≲ 2.7σ per slab” mixes two baselines: earlier in the same paragraph you describe deviations from 0.5, not from 0.49735. If one instead measures absolute deviations from the global value (0.49735), the slab range 0.49537–0.49890 corresponds to −0.00198 to +0.00155, i.e. −0.198% to +0.155%. Given the per-slab binomial σ ≈ 7.4×10−4 (0.074%), those are about −2.7σ and +2.1σ, so “≲2.7σ” is numerically consistent but uses a different baseline than the percentage deviations just quoted.  
- Required fix:  
  - Clarify the two baselines explicitly, e.g.: “…spans 0.49537–0.49890, i.e. −0.463% to −0.110% relative to 0.5. Relative to the catalog‑wide mean fCW = 0.49735, the slab deviations are −0.20% (−2.7σ) to +0.16% (+2.1σ).”  
  - This removes any impression that the −0.463% etc. percentages are being interpreted as deviations about the global mean.

P4-m13 (MINOR)  
- Location: Appendix B.a (“Training”), headline accuracies  
- Text: “Headline 93.7% accuracy is the best-epoch three-class … and 94.9% is the CW per-class validation accuracy … an earlier text mis-attributed this pair to augmentation-on/off evaluations…”  
- Problem (stale-number / clarity):  
  - You carefully explain the provenance of 93.7% and 94.9%, but the main body never uses these numbers in any load‑bearing argument; the *only* scientifically relevant accuracy figure is the independent GZ1 spiral‑chirality accuracy 69.91%. Persistently quoting 93.7%/94.9% — which are purely internal validation metrics on a small 80/20 split with CE‑ResNet–derived labels — risks confusing readers into thinking the effective survey‑scale reliability is ~94%, not ~70%.  
- Required fix:  
  - In the main text, mention 93.7%/94.9% at most once, with a strong qualifier (“on the internal pseudo‑labeled training split; not an external truth metric”), and consider moving the detailed provenance discussion entirely to the repository README rather than the paper.  
  - Alternatively, keep the Appendix exposition but add a brief sentence in Sec. II.B explicitly stating that all cosmological inferences use 69.91% (GZ1 cross-match) as the operative accuracy and that the higher internal accuracies are not used for any quantitative bound.

If you want, I can now step through the tables and p‑value calculations line‑by‑line (class A issues) and produce a strict numerical audit table you can paste into your own checklist.