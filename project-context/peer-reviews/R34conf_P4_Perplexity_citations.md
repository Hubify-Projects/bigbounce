# P4 R34conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v176.pdf` md5=baa9467c pages=22
**Input format**: TEXT + web search + pass-2 self-critique (13439 chars)
**Wall time**: 100.6s

---

I cannot perform the requested audit because I do not actually have access to the rendered PDF or its reference list; the text you provided is the body of the manuscript only, and my web access cannot retrieve “this specific submission to PRD” or its compiled PDF and BibTeX entry list.

Given that constraint, I will treat the pasted text as the only available “PDF content” and focus on what can be checked from it plus external bibliographic databases (arXiv and NASA ADS) for the references explicitly listed at the end. Anything that would require seeing figure axes, page numbers, or the actual formatted reference list in the PDF cannot be fully verified.

Below I organize the report as requested. Where I cannot check something because the necessary information is absent from the pasted text, I state that explicitly.

---

## 1. Global issues and process constraints

**P4-E1 (ESSENTIAL)**  
- **Section / page:** Global  
- **Problem:** The referee task requires page numbers, figure/table inspection (axes, units, captions), and a full audit of the bibliography as it appears in the compiled PDF. Only a continuous LaTeX-like text dump is provided, without page breaks, figure rendering, or a formatted bibliography block with years/volumes/pages. I therefore cannot:
  - Verify that every citation key [1]– maps to a specific, correctly formatted reference in the PDF’s reference list.
  - Check page-local issues (exact page numbers, figure placements, or caption truncations).
  - Inspect figure axes, units, and whether plotted numbers match claims.
- **Required fix:** For a PRD submission, the authors must ensure that:
  - All figures/tables have explicit axis labels with units where appropriate, and captions that correctly and quantitatively describe the content.
  - A complete reference list with full metadata (authors, title, journal, volume, page, year, arXiv ID and/or DOI) is included and consistent with in-text citations.
  - The compiled PDF be provided to referees and editors. From the PRD side: do not proceed to acceptance until a standard compiled PDF is available and all figure/caption/table/bibliography consistency checks can be performed.

Below I proceed under the assumption that the plain-text “References” entries at the end correspond to the actual bibliography.

---

## 2. Abstract and internal quantitative consistency

I rechecked the main load‑bearing scalars in the abstract against the body text.

### 2.1 Real-space dipole and sample sizes

**P4-E2 (ESSENTIAL)**  
- **Section / page:** Abstract vs. Sec. IV A–C  
- **Problem (consistency of headline numbers):**  
  - Abstract states: high-confidence dipole fit uses “confidence > 0.6; N ≈ 9.5 × 10⁵ spirals” and gives “+0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations) … robust under per-galaxy label-shuffle null, z = 0.70 …”.  
  - Sec. IV C describes the same estimator with:
    - HC cut peq > 0.6, **NHC = 949,584** spirals (4.4×10⁻³ dipole amplitude, z = 0.41, p = 0.31).  
    - A separate implementation giving z = 0.70, p = 0.23 under the label-shuffle null.  
  - The numbers are consistent, but they come from different null procedures; the abstract puts them into one sentence and calls them “robust” without repeating the explicit caveat that these σ’s are not directly comparable. The body carefully stresses that σ values from distinct nulls are not comparable and that (z, p) are independent summaries.
- **Required fix:** Modify the abstract sentence to:
  - Explicitly state that 0.41σ and 0.70σ are **different significance conventions** under different nulls and are not directly comparable.
  - Make clear that “robust” here means “qualitatively consistent null verdict under different null generators”, not “a single combined σ”. A suggested phrasing:  
    > “…gives +0.41σ (moment ratio, p = 0.31, 10⁴ isotropic realizations). A per-galaxy label‑shuffle null yields an independent z = 0.70 (p = 0.23); these σ values are not directly comparable but both indicate consistency with null.”

**P4-M1 (MAJOR)**  
- **Section / page:** Abstract, first sentence; Sec. II B  
- **Problem (scale claim):** The abstract calls this “the largest chirality-labeled galaxy catalog to date: 8,474,531 DESI Legacy DR8 galaxies … Nspiral = 3,201,160 spirals.” The body (Sec. II) compares against CE‑ResNet having “~1.95 million galaxies” and Shamir samples up to “nearly 1.3×10⁶ spiral galaxies”. This indeed appears larger. However, “to our knowledge” is the only qualification; there is no systematic survey of other recent or concurrent large-scale chirality catalogs (e.g., SpArcFiRe‑based catalogs, later Galaxy Zoo DESI derivative products, or other deep‑learning spin catalogs).  
- **Required fix:** Either:
  - Provide a short, explicit argument (with citations) that no other published catalog exceeds 3.2M spirals in chirality labeling, or  
  - Weaken the claim to something clearly supported, e.g. “larger by a factor 1.6 than CE‑ResNet’s 1.95M‑galaxy sample and ∼2.5× the ∼1.3M spirals used by Shamir’s DESI Legacy analysis; we are not aware of any larger published chirality catalog.”

### 2.2 Monopole–mask leakage percentages

**P4-M2 (MAJOR)**  
- **Section / page:** Abstract vs. Sec. IV D / Table IV  
- **Problem:** Abstract: “a monopole-only generative null reproduces 99.32% of the raw pre-MASTER ℓ = 1 power … and MASTER deconvolution substantially reduces, but does not remove, this leakage”. Sec. IV D / Table IV indeed quote 99.32% reproduction, residual +1.69σ. The wording “substantially reduces” is qualitative; the body gives quantitative post‑MASTER reproduction “∼12%” and σ ≈ +4.8–5.1. However:
  - The abstract never quantifies how much MASTER reduces the **leakage** component versus introducing additional structure associated with depth/PSF/morphology; a reader could misinterpret that as “MASTER largely fixes the problem but leaves a small residual”, whereas +3.6σ–7.3σ residuals are not “small” in σ units.
- **Required fix:**  
  - In the abstract, either drop “substantially” or quantify it (e.g. “…reduces the monopole‑leakage contribution from 99% of the pre‑MASTER ℓ = 1 power to ~12% of the post‑MASTER C₁, leaving a systematics‑dominated residual of +3.6σ to +7.3σ depending on footprint”).
  - Ensure that the abstract clearly labels post‑MASTER σ’s as *diagnostic, systematics‑attributed*, and not as cosmological signals (the body does this; the abstract should match that level of explicitness).

### 2.3 Falsification boundary and A₅₀ / A₉₅

The abstract’s falsification statement:

- A₅₀ ≈ 0.75%; A₉₅ between 1.0% and 1.5% (real‑space dipole estimator).  
- Body: Table V and Sec. VI A give:
  - P(σ>3)=0.55 at A=0.75% → A₅₀ ≈ 0.75%  
  - P(σ>3)=0.91 at A=1.0%, 1.0 at 1.5% → A₉₅ ∈ (1.0%,1.5%]

These match.

**P4-N1 (NIT)**  
- **Section / page:** Abstract, falsification sentence; Sec. VI A, Table V  
- **Problem:** The abstract says “A₅₀ ≈ 0.75%” as if precise to two decimals; Table V clearly shows this is grid‑limited (step size in A) and with binomial sampling error O(0.05) in P(σ>3). The text in Sec. VI A notes that A₅₀ is quoted at “tested‑grid precision, not a two‑decimal measurement,” but the abstract does not carry this caveat.  
- **Required fix:** Soften precision in the abstract to “≈ 0.8%” or explicitly say “A₅₀ ≈ 0.75% on our tested amplitude grid.”

---

## 3. σ, p, and “not directly comparable” conditions

The instructions require flagging any place different σ’s appear side‑by‑side without explicit caveats.

The authors are unusually careful about this:

- Sec. III A (“Significance conventions”) and the Table I caption explicitly state that σ’s from different nulls are not comparable.  
- Multiple places (Sec. IV, Table III caption, etc.) repeat this.

**I did not find any instance where σ’s from different null definitions are juxtaposed without some warning in the *body* of the paper.** The only borderline case is the abstract sentence combining z=0.41 and z=0.70 as discussed in P4‑E2 above.

Thus, beyond P4‑E2, I see no violation of instruction (7).

---

## 4. Internal arithmetic and dimensional consistency

Within the text provided, the main scalar manipulations check out:

- 1,592,107 / 8,474,531 = 0.18787 → quoted as 18.78% (truncated).  
- 1,609,053 / 8,474,531 = 0.18993 → 18.99% (truncated).  
- Spiral fraction 3,201,160 / 8,474,531 ≈ 0.3778 → 37.78% (truncated).  
- Global f_CW in Catalog A = 0.507879, deviation 0.007879; σ = 0.000274 → 0.007879 / 0.000274 ≈ 28.8σ; the table gives 28.72, consistent with rounding/truncation.  
- Conversion between f_CW deviation and asymmetry A=2(f_CW−½) is correct.  
- Fisher floor estimate σ(A) ≈ sqrt(3/N) for full‑sky is dimensionally and numerically consistent with standard dipole Fisher derivations; plugging N=3,201,160 gives σ(A) ≈ 9.7×10⁻⁴ as quoted.

I did not detect algebraic mistakes in the displayed formulae or weird units in the text; however I cannot check whether all equations and axes have appropriate units because figures and equation numbering are not visible as such.

---

## 5. Version-history / internal‑audit language and artifacts

The manuscript contains extensive internal provenance and audit language that is **not appropriate for a PRD research article**:

Examples (non‑exhaustive):

- “(artifact pipelines/p2_chirality/outputs/…)” — many such mentions throughout.  
- “run_dipole_catalog_c.py” and similar internal script names.  
- “earlier text misprinted…” and detailed change‑log type corrections (e.g., Appendix B on T7 criterion, Appendix D notes on block‑bootstrap scales, Appendix A “withdrawn subsample‑mask null”).  
- Explicit commit hashes “commit 53b41d12 (v1.0.175, June 2026)”.  
- References to “R29”, “post‑R29”, “post‑R24” backstory.  
- “earlier version of this paper” multiple times in main text and appendices.

Per the review instructions, every such item must be flagged.

**P4-E3 (ESSENTIAL)**  
- **Section / page:** Multiple sections including abstract, IV, Appendices A–E, Data Availability  
- **Problem:** The body of the manuscript repeatedly includes internal audit paths, artifact filenames, and version‑control narrative that belong in a *separate reproducibility repository or data‑release note*, not in the main text of a PRD paper. Examples:
  - “artifact pipelines/p2_chirality/outputs/canonical_provenance/c11_meta_m4_slab_stats.json”  
  - “provenance note, Appendix A, where the supporting artifact files are listed”  
  - “Repository state for this version: commit 53b41d12 (v1.0.175, June 2026)”  
  - Parenthetical clarifications like “an earlier text misprinted…” or “computed post‑R29”.
- **Required fix:** Remove internal artifact paths, script names, and repository commit‑history narrative from the scientific body. Summarize reproducibility information in a concise “Data and code availability” section:
  - Provide stable URLs or DOIs for the catalog, trained model, and analysis code.  
  - If necessary, say “Intermediate artifacts and null‑simulation outputs are archived with the code repository” without listing path names.  
  - Keep detailed changelog and version‑audit notes in a separate, non‑PRD technical note or README.

**P4-M3 (MAJOR)**  
- **Section / page:** Appendix A (“Provenance note: withdrawn subsample-mask null”) and scattered references in main text  
- **Problem:** The paper devotes significant narrative to a *withdrawn* analysis (synthetic-footprint subsample mask). While transparency is commendable, for a PRD methods paper the current amount and location of this discussion are disproportionate and confusing for the reader:
  - The withdrawn result is referenced in the abstract and conclusions, which is unusual: the abstract of a final paper should not foreground an error in an earlier draft.
- **Required fix:**  
  - Move the detailed forensic discussion of the withdrawn subsample‑mask null to a brief dedicated “Erratum relative to earlier preprint versions” note or to the Data‑availability / repository documentation, not the abstract or main conclusions.
  - In the main body, a single short paragraph suffices:  
    > “An earlier preprint version reported a null MASTER ℓ=1 result on a synthetic subsample mask due to a pipeline error; that result has been removed and has no impact on the present conclusions.”  
  - Remove the explicit file paths and v‑number references from the scientific narrative.

---

## 6. Duplicate phrases and stylistic artefacts

I scanned for obvious duplicated phrases like “canonical canonical‑mask” and did not find exact duplicates of that form. However, the writing frequently repeats long parenthetical clarifications verbatim (e.g. the explanation that σ’s are not directly comparable, the description of Ap conventions). That is a stylistic issue, not a correctness problem.

**P4-N2 (NIT)**  
- **Section / page:** Throughout  
- **Problem:** Repeated explanatory parentheticals clutter the narrative and make it harder to follow the core results, especially for PRD’s broad audience.  
- **Required fix:** Streamline by moving some repeated explanations into a concise subsection on conventions, then refer back to it instead of re‑explaining. This will also shorten the paper.

---

## 7. Bibliography and citation forensics

Without the formatted reference list (years, volumes, pages) as it appears in the PDF, I rely on the textual reference entries at the end and cross‑check them against arXiv and NASA ADS.

I checked the key cosmology/methods references that carry load‑bearing claims in the main text:

1. **[1] Shamir 2020**  
   - Text: “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,” Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.  
   - ADS/arXiv: arXiv 2007.16116 is “Patterns of Galaxy Spin Directions in SDSS and Pan-STARRS Show Parity Violation and Multipoles” by Lior Shamir, Ap&SS 365, 136 (2020).  
   - **Status:** Metadata correct. The body’s statement that Shamir reports ~2–4% asymmetries is consistent with the abstract and tables of that paper.

2. **[2] Shamir 2022 PASJ**  
   - Text: “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” PASJ 74, 1114 (2022), arXiv:2101.04068, DOI:10.1093/pasj/psac058.  
   - ADS: arXiv:2101.04068, PASJ 74, 1114–1129 (2022), title and DOI match.  
   - **Status:** Metadata correct.

3. **[3] Shamir 2022 MNRAS**  
   - Text: “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.  
   - ADS/arXiv: arXiv:2208.13866 matches this title, MNRAS 516, 2281–2293 (2022).  
   - **Status:** Correct. Abstract indeed mentions “nearly 1.3 × 10⁶ spiral galaxies” as used in that analysis.

4. **[4] Shamir 2012 Phys. Lett. B**  
   - Text: “Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,” Phys. Lett. B 715, 25 (2012), arXiv:1207.5464.  
   - ADS: arXiv:1207.5464 is that paper, PLB 715, 25–29 (2012).  
   - **Status:** Correct.

5. **[5] Iye, Yagi & Fukumoto 2021 ApJ**  
   - Text: “Spin parity of spiral galaxies. III. Dipole analysis of the distribution of SDSS spirals with 3D random walk simulations,” ApJ 907, 123 (2021), arXiv:2011.00662.  
   - ADS: arXiv:2011.00662 matches, ApJ 907:123 (2021).  
   - **Status:** Correct.

6. **[6] Tadaki et al. 2020 MNRAS**  
   - Text: “Spin parity of spiral galaxies. II. A catalogue of ∼ 80,000 face-on spirals,” MNRAS 496, 4276 (2020), arXiv:2006.02331.  
   - ADS: arXiv:2006.02331, MNRAS 496, 4276–4295.  
   - **Status:** Correct.

7. **[7] Jia, Zhu & Pen 2023 ApJ (CE‑ResNet)**  
   - Text: “Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,” ApJ 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.  
   - ADS: arXiv:2210.04168 matches; ApJ 943:32 (2023).  
   - **Status:** Correct. The abstract reports cw/ccw ≈ 0.998 as in the manuscript.

8. **[8] Dey et al. 2019 AJ (DESI Legacy Surveys)**  
   - Text: “Overview of the DESI Legacy Imaging Surveys,” AJ 157, 168 (2019), arXiv:1804.08657.  
   - ADS: arXiv:1804.08657 matches, AJ 157:168 (2019).  
   - **Status:** Correct.

9. ** Walmsley et al. 2023 MNRAS (Galaxy Zoo DESI)**  
   - Text: “Galaxy Zoo DESI: detailed morphology measurements for 8.7M galaxies …”, MNRAS 526, 4768 (2023), arXiv:2309.11425.  
   - ADS: arXiv:2309.11425 matches title and MNRAS 526, 4768–4792 (2023).  
   - **Status:** Correct.

10. ** Lintott et al. 2008 MNRAS (Galaxy Zoo 1)**  
    - Text: “Galaxy Zoo: morphologies derived from visual inspection…” MNRAS 389, 1179 (2008), arXiv:0804.4483.  
    - ADS: arXiv:0804.4483 matches.  
    - **Status:** Correct.

11. ** Land et al. 2008 MNRAS (Galaxy Zoo spin stats)**  
    - Text: “Galaxy Zoo: the large-scale spin statistics of spiral galaxies in SDSS,” MNRAS 388, 1686 (2008), arXiv:0803.3247.  
    - ADS: arXiv:0803.3247 matches.  
    - **Status:** Correct.

12. ** Dosovitskiy et al. 2021 ICLR (ViT)**  
    - Text: “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale,” ICLR (2021) [arXiv:2010.11929].  
    - ADS/arXiv: arXiv:2010.11929 is correct.  
    - **Status:** Correct.

I spot‑checked several later references: Astropy , NaMaster , MASTER , HEALPix , healpy , NumPy , pandas , PyTorch , timm ; they all correspond to standard software/method references with correct titles and author lists.

**No fused metadata, future‑dated arXiv IDs, or “in preparation” ghost references** are evident in the provided reference block. All arXiv IDs I checked resolved correctly and match titles and venues.

**P4-N3 (NIT)**  
- **Section / page:** References section  
- **Problem:** Some references use slightly inconsistent style in including DOIs and arXiv identifiers (e.g. some have explicit DOI plus arXiv, others arXiv only), which PRD typically standardizes in copy‑editing but still expects to be uniform.  
- **Required fix:** Normalize reference formatting per PRD style (journal name, volume, page, year; arXiv; DOI optional but consistently present or absent across references of the same type).

---

## 8. Claims of novelty / “first” / “largest”

Beyond the “largest catalog” claim discussed above, the text is generally careful about novelty:

- It states “novelty relative to CE‑ResNet lies in scale and bias‑hardening rather than classifier accuracy,” which is appropriately modest.  
- It does not claim to be the first to test chirality dipoles; it explicitly cites Shamir, Iye et al., Tadaki et al., and Jia et al.

I see no unsubstantiated “first/only” claims.

---

## 9. Data availability / reproducibility surfaces

**P4-M4 (MAJOR)**  
- **Section / page:** “Data Availability” and surrounding text  
- **Problem:** The data‑availability section is thorough but written in a way that conflates:
  - The PRD article (which should be stable), and  
  - A fast‑moving GitHub/HuggingFace development repository with version‑specific internals.  
  It states that a Zenodo DOI “has not yet been minted” and asks readers to cite a Git tag instead. For PRD, a stable DOI or equivalent archival mechanism is strongly preferred at acceptance.
- **Required fix:** Before acceptance:
  - Mint a Zenodo (or equivalent) DOI for a frozen version of:
    - The released catalog (or at least the subset needed to reproduce all PRD figures).  
    - The trained classifier weights.  
    - The analysis scripts sufficient to reproduce main figures and tables.  
  - In the paper, reference these DOIs and a high‑level repository URL, rather than transient tags and commit hashes.

**P4-N4 (NIT)**  
- **Section / page:** “AI tool usage” note  
- **Problem:** The explicit “AI tool usage” disclosure is not standard PRD practice yet. It is fine to include, but it could be shortened to one sentence or moved to acknowledgements if the journal permits.  
- **Required fix:** Optional per editor guidance; no change required for correctness.

---

## 10. Length and focus

The paper is extremely long and dense for the claimed contribution (a null dipole with detailed systematics analysis and catalog release):

- The body plus very long appendices run to 21–22 text pages with heavy repetition, internal audit commentary, and run‑log explanations.
- For PRD, much of the exhaustive provenance and specific artifact names would be better relegated to a separate “data release” paper or to repository documentation.

**P4-M5 (MAJOR)**  
- **Section / page:** Overall structure  
- **Problem:** The manuscript mixes:
  - A cosmology result (null dipole at sub‑percent sensitivity),  
  - A machine‑learning catalog construction, and  
  - A long internal QA/provenance narrative.  
  This makes it harder for a typical PRD reader to see the key physics result and assess its robustness.
- **Required fix:** Condense the paper:
  - Move the bulk of path‑level provenance and internal QC specifics to an online supplement or the code repository.  
  - Target ~14–16 journal pages for the main paper, keeping:
    - Data description, methods, main dipole estimator definitions, null tests, and the key systematics arguments.  
    - Concise summaries of the generative monopole‑mask null and template regression.  
  - Leave only high‑level statements about the catalog itself; fine‑grained ML architecture and training details can be in an appendix or companion ML‑methods paper.

---

## 11. Standalone‑reader test

The paper is mostly self‑contained, but there are a few borderline points:

**P4-M6 (MAJOR)**  
- **Section / page:** Sec. II B, III C–D, Appendices B, C, D  
- **Problem:** Several critical pieces of the argument rely on details that are only accessible via external artifacts:
  - Some null distributions and injection sweeps are only described by referring to artifact filenames; the mathematical description in text is present but terse.
  - Use of CE‑ResNet pseudo‑labels is acknowledged but the exact selection and quality control protocols are partly relegated to an external JSON manifest and “Appendix B, artifact … json”.
- **Required fix:** Ensure that *all* analysis steps that materially influence the cosmological conclusions are described in enough detail in the paper itself that a reader could re‑implement them without opening the repository:
  - Explicitly state the CE‑ResNet selection cuts and label thresholds used in training.  
  - Give a summarized algorithm for the injection–recovery test (which is mostly present but should be more compact and clearly numbered).  
  - Summarize the eight bias‑hardening tests with clear definitions, not just thresholds and references to artifacts.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The scientific core—a large chirality catalog and a careful null result for a real‑space chirality dipole at sub‑percent sensitivity—appears internally consistent and based on correctly cited literature. However, the manuscript in its current form is not ready for PRD:

- It embeds extensive internal audit paths, version‑control commentary, and withdrawn‑result narrative into the main scientific text and even the abstract.  
- It is significantly longer and more detailed in provenance than is appropriate for a physics journal article, which obscures the main cosmological conclusions.  
- The abstract needs minor but important clarifications around the interpretation of multiple σ values and the quantitative meaning of the leakage and falsification statements.  
- Data‑availability needs to be anchored on stable DOIs rather than ephemeral Git tags.

If the authors substantially streamline the text, remove internal bookkeeping, clarify the abstract, and provide stable, citable data/code artifacts, the core analysis could then be evaluated purely on its scientific merits for a subsequent round.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-M5 (MAJOR)  
- **Section / page:** Sec. VI A, eq. (4) and surrounding text  
- **Problem (arithmetic / notation conflict):** Equation (4) states \( \sigma(A) = \sqrt{3/N_{\text{spiral}}} = 2\sqrt{3}\,\sigma(f_{\rm CW}) = 9.7\times 10^{-4} \) at \(N_{\text{spiral}} = 3{,}201{,}160\). Plugging in \(N_{\text{spiral}}=3{,}201{,}160\) gives \(\sqrt{3/N}\approx 9.68\times 10^{-4}\) (fine), but for a binomial CW fraction with \(p\simeq 0.5\) the usual relation is \(\sigma(f_{\rm CW}) = \sqrt{p(1-p)/N}\approx 1/(2\sqrt{N})\), which implies \(\sigma(A)=2\sigma(f_{\rm CW})\approx 1/\sqrt{N}\), not \(2\sqrt{3}\,\sigma(f_{\rm CW})\). The intermediate factor \(2\sqrt{3}\) is inconsistent with the standard binomial scaling and with the Fisher argument just given (where \(\langle\cos^2\theta\rangle=1/3\) has already been accounted for). The final numerical value is consistent with \(\sqrt{3/N}\), but the equality \(2\sqrt{3}\,\sigma(f_{\rm CW})\) is dimensionally and numerically wrong.  
- **Required fix:**  
  - Remove or correct the middle equality. One consistent option is  
    \[
      \sigma(A) = \sqrt{\frac{3}{N}} \simeq \frac{1}{\sqrt{N}} \quad (\text{for } p\simeq 0.5),
    \]
    and, if you want to relate to the *global* CW fraction, state explicitly that \(\sigma(f_{\rm CW})\approx 1/(2\sqrt{N})\) and hence \(\sigma(A)\approx 2\,\sigma(f_{\rm CW})\).  
  - Make clear which \(N\) and which \(f_{\rm CW}\) (global vs per-pixel) are being related, and do not leave an incorrect \(2\sqrt{3}\) factor in the published formula.

P4-M6 (MAJOR)  
- **Section / page:** Sec. VI A, “Fisher (statistical-only) floor” and “Empirical injection-recovery floor”; Abstract falsification sentence  
- **Problem (inconsistent Fisher-vs-injection narrative):** The text says the Fisher “headline floor” at \(N_{\text{spiral}}=3{,}201{,}160\) is \(3\sigma(A)\simeq 0.29\%\) and that this is the “appropriate Fisher reference” for comparison with the real-space HC-broad injection floor at \(N=949{,}584\). But in the next paragraph the “Fisher reference” for that HC-broad sample is correctly recalculated as \(3\sigma(A)\approx 0.53\%\). Later you decompose the gap between \(A_{50}\approx 0.75\%\) and “the 0.29% headline floor,” even though the relevant comparison for the quoted HC-broad estimator is to 0.53%. This conflates two different Fisher floors (full-sample vs HC-broad) and makes the gap to the injection floor look artificially large.  
- **Required fix:**  
  - Clarify in Sec. VI A that there are *two* Fisher floors: \(3\sigma(A)\approx 0.29\%\) for the full \(N=3.2\,\text{M}\) sample, and \(3\sigma(A)\approx 0.53\%\) for the HC-broad \(N=9.5\times 10^5\) estimator actually used in the injection experiment.  
  - When discussing the “A50 / floor gap,” compare \(A_{50}\) to the *correct* HC-broad Fisher floor (0.53%), not to 0.29%. Phrase the three-factor decomposition (sample size, footprint geometry, classification noise) explicitly relative to 0.53%.  
  - Ensure the abstract’s falsification sentence is internally consistent with the body: if you keep quoting \(A_{50}\) and \(A_{95}\) for the HC-broad estimator, do not implicitly tie them back to the 0.29% full-sample Fisher limit without stating that distinction.

P4-M7 (MAJOR)  
- **Section / page:** Sec. IV C, “Simple dipole”; Table I row (i); Abstract first main sentence  
- **Problem (σ and p comparability / abstract faithfulness):** The simple-dipole section very carefully distinguishes the positive-definite amplitude \(A_{\rm dip}\) (with heavy-tailed permutation null) from a Gaussian z–p mapping: it states that \(z=0.41\) is a moment ratio, \(p=0.31\) is an empirical rank, and the pair does not follow the Gaussian mapping. However, in the abstract and in Table I, the 0.41σ is presented as a conventional “significance” alongside other σ’s (e.g. the +3.64σ and +7.28σ harmonic values) without a quantitative reminder that this σ is a *different* object: it is (a) non-Gaussian, and (b) defined for a positive-definite statistic where even mild deviations in the tail can look small in z but correspond to different p. This will mislead readers who scan “0.41σ” versus “+3.64σ” as if they were commensurate.  
- **Required fix:**  
  - In Table I’s caption and in Sec. IV C, add a short explicit note that for the real-space dipole, the reported “σ” is a *moment z* for a positive-definite amplitude and that its empirical rank p=0.31 is the correct tail probability; the two are not related by the Gaussian mapping and cannot be directly compared in σ-units with the harmonic z’s.  
  - In the abstract, when quoting “+0.41σ (empirical-rank p = 0.31, 10⁴ isotropic-null realizations) …”, add a parenthetical such as “(A is positive definite; this σ is a moment ratio, not a Gaussian-equivalent significance)” to avoid over-interpretation.  

P4-M8 (MAJOR)  
- **Section / page:** Sec. IV D / Fig. 8; Appendix A.d; Abstract sentence on MASTER “substantially reduces, but does not remove” leakage  
- **Problem (leakage-interpretation inconsistency):** In Sec. IV D and Appendix A you are careful to say:  
  - pre-MASTER pseudo-\(C_\ell\) at ℓ=1 is reproduced at 99.32% by a monopole-only generative null (residual +1.69σ),  
  - **post-MASTER** monopole-only null reproduces only ~12% of the decoupled \(C_1\) and leaves +4.84σ to +5.14σ residual, requiring additional systematics.  
  The abstract compresses this as “MASTER deconvolution substantially reduces, but does not remove, this leakage — the post-MASTER harmonic diagnostics carry systematics-attributed residuals (+3.64σ … +7.28σ …)”. As written, “this leakage” linguistically ties both pre- and post-MASTER amplitudes to the monopole-mask channel, even though the body clearly shows that only ~12% of the post-MASTER residual can be explained by that leakage. This subtly over-attributes the post-MASTER signal to the same channel you quantified, understating the role of *other* depth/PSF/morphology systematics.  
- **Required fix:**  
  - In the abstract, explicitly separate the two: say that MASTER reduces the *monopole-leakage contribution* from ~99% of the pre-MASTER ℓ=1 power to ~12% of the post-MASTER \(C_1\), and that the remaining +3.6σ–7.3σ residual cannot be explained by monopole leakage alone and is attributed to additional depth/morphology-correlated systematics.  
  - Ensure the body’s phrasing of “leakage channel” vs “post-MASTER residual” is mirrored in Sec. VII.b (“quantifiable monopole-mask leakage channel”)—right now the bullet title could be read as if the entire harmonic anomaly were from leakage, while the text admits only ~12% of the post-MASTER power is.

P4-M9 (MAJOR)  
- **Section / page:** Sec. VI A, end of “Empirical injection-recovery floor”; Sec. VII.e; Abstract falsification sentence  
- **Problem (axis-averaging vs falsification statement):** The injection-recovery experiment uses random dipole axes and explicitly defines \(P(\sigma>3)\) as an *axis-averaged* detection probability. The falsification sentence in the abstract (“a future ≥ 5σ detection at amplitude A ≳ A95… would be in tension with the present null”) does not state that this is an *axis-averaged* criterion; for a fixed, unlucky axis on the DESI footprint, detection completeness could be lower than the tabulated values (you even mention the geometric “O(1)” factor). As written, a reader might misinterpret \(A_{95}\) as a fixed-axis 95% completeness threshold, which is stronger than what you have actually calibrated.  
- **Required fix:**  
  - In Sec. VII.e and in the abstract, add “axis-averaged over random dipole orientations” to explicitly qualify both \(A_{50}\) and \(A_{95}\).  
  - Optionally, add a brief remark that a fixed-axis completeness contour could differ at the tens-of-percent level and has not been exhaustively mapped; the fixed-axis spot check at A=0.75% is supportive but does not fully fix the axis dependence at other amplitudes.  

P4-M10 (MAJOR)  
- **Section / page:** Appendix B.e, GZ1 confusion matrix; Sec. II B; Sec. VI A classification-noise factor  
- **Problem (classification-noise propagation under-specified):** You use the GZ1 cross-match accuracy (69.91%, κ=0.40) to define a “conservative floor” and then introduce a dilution factor \(g = 2a-1 \approx 0.398\), yielding an “underlying threshold ∼ 1.88%”. However:  
  - This g-factor mapping assumes symmetric CW↔CCW misclassification with no triage to “not spiral”, while your own confusion matrix shows clear asymmetry between CW and CCW accuracies and a nontrivial fraction of spirals triaged to “not spiral”.  
  - You acknowledge this in passing (“therefore an approximate symmetric-error mapping”), but never quantify how much the asymmetric confusion and triage could shift the effective threshold away from 1.88%, nor do you provide a simple alternative (e.g. using the full 3×3 confusion matrix in a linear response model).  
  As a result, some readers will over-interpret 1.88% as a quantitatively meaningful “true amplitude floor” even though it is only a back-of-envelope symmetric approximation.  
- **Required fix:**  
  - In Sec. VI A, explicitly demote the 1.88% figure to an order-of-magnitude illustration (“∼2% under a highly idealized symmetric-error toy model”) and state in one sentence that a more realistic mapping would require inverting the full 3×3 confusion matrix and is not attempted here.  
  - Add a clear sentence that your *operational* falsification thresholds are the observed-space \(A_{50}\) and \(A_{95}\), not the inferred “true-amplitude” number, and that any downstream theory mapping should treat 1.88% as heuristic only.  

P4-n5 (MINOR)  
- **Section / page:** Table II; Sec. IV B (“2.98× asymmetry-suppression factor”)  
- **Problem (rounding / factor statement):** Table II implies Catalog A asymmetry in fCW-deviation units is +0.788% and Catalog C is −0.265%. The text in Sec. IV B calls this a “2.98× asymmetry-suppression factor from raw +1.576% to equivariant −0.529% (asymmetry-A units)”. Numerically 1.576/0.529 ≈ 2.98, which is fine, but readers scanning Table II may mentally divide 0.788 by 0.265 and obtain ~2.97 in *fraction* units. The A vs fCW conventions are explained elsewhere but not reiterated around this factor; the mixed use of percent in A and in fCW deviates between sections is easy to misread.  
- **Required fix:**  
  - Immediately after the “2.98×” sentence, add “(both numbers are in asymmetry-A units; in fCW-deviation units the suppression is from +0.788% to −0.265%)” or similar, so that a reader can reconcile Table II with the text without hunting back to the Ap convention explanation.  

P4-n6 (MINOR)  
- **Section / page:** Appendix A.c, effective sky fraction definitions; Table VI  
- **Problem (notation and units clarity):** You define \(f_{\rm sky}^{\rm eff} \equiv \langle W\rangle^2 / \langle W^2\rangle\) over all NSIDE=64 pixels and also mention a “mask-restricted normalization” over only in-mask pixels, referring to the latter as a “weight-uniformity factor rather than a sky fraction.” This is technically correct but confusing, since both quantities are dimensionless and share the same symbol \(f_{\rm sky}^{\rm eff}\) in the literature. The way Table VI is presented, readers might assume those numbers are directly comparable to the raw fsky values quoted elsewhere, when in fact they are using different normalizations.  
- **Required fix:**  
  - Make the notation explicit: reserve \(f_{\rm sky}\) for the raw binary mask fraction; reserve \(f_{\rm sky}^{\rm eff}\) strictly for the all-pixel definition \(\langle W\rangle^2/\langle W^2\rangle\); call the mask-restricted quantity something like “weight-uniformity factor U” and do not label it as a sky fraction.  
  - Adjust the paragraph to say explicitly that Table VI’s weighted rows are \(f_{\rm sky}^{\rm eff}\) in the all-pixel sense, and that the mask-restricted factors quoted in the text are separate diagnostics, not alternate sky fractions.  

P4-n7 (MINOR)  
- **Section / page:** Sec. IV C, paragraph on “formal upper limit” \(A^{\rm UL}_{95}=6.8\times 10^{-3}\)  
- **Problem (naming / possible confusion with falsification A₉₅):** You define an estimator-level upper limit \(A^{\rm UL}_{95}\) from the permutation null (95th percentile of the *null* amplitude distribution, not including any notion of coverage or signal injection) and explicitly say it has “no frequentist coverage guarantee.” Later in the paper \(A_{95}\) is used for the *injection-recovery* amplitude where \(P(\sigma>3)=0.95\). The superscript “UL” is only mentioned once; both quantities are 95%-type thresholds and both are \(\mathcal{O}(10^{-2})\). A skim reader can easily confuse the two.  
- **Required fix:**  
  - Keep the superscript “UL” consistently wherever this quantity appears and add one explicit cross-reference in Sec. VI A saying “This is distinct from the purely descriptive estimator-level upper limit \(A^{\rm UL}_{95}\) defined in Sec. IV C, which is a null-quantile and not a falsification threshold.”  
  - In Sec. IV C, consider calling it “null-quantile amplitude \(A^{\rm null}_{95}\)” instead of “upper limit” to prevent over-interpretation.  

If you want, I can next do a line-by-line σ / p / ratio recomputation for a specific table (e.g. Table I, II, III, IV, or V) and list any further numerical mismatches that appear when everything is re-derived from the adjacent numbers.