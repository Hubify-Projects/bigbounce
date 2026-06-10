# P3 2026-06-04_R6clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 47.9s

---

P3-E1 (ESSENTIAL) – Incorrect citation of Heinrich et al. multi-tracer SPHEREx forecast  
- **Location:** Introduction, p.1–2 (“…multi-tracer methodology of Heinrich et al.  (anchored to the Heinrich+2024 σ(fNL ) ≈ 0.7 bispectrum-only forecast…)”; also §V, §VII and ref. .  
- **Problem:** Reference  is given as “Heinrich … JCAP 2024, 074 (2024)” and used as the source of a *bispectrum-only* SPHEREx σ(fNL) ≈ 0.7 forecast and as the methodological template for the seven-bin multi-tracer Fisher pipeline. This is inconsistent with the actual paper. The arXiv version “Heinrich, Doré, Krause, ‘Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum’, JCAP 03 (2024) 074, arXiv:2311.13082” is a *redshift-space bispectrum* forecast for SPHEREx using SPHEREx tracers plus LSST/Euclid-like samples; it does **not** (i) present a σ(fNL) ≈ 0.7 **bispectrum-only** number as a simple “headline external benchmark” applicable to this catalog, nor (ii) define the particular 7-bin Fisher implementation with the nuisance-parameter structure described here. The way the manuscript phrases this makes it sound as if the exact σ(fNL) ≈ 0.7 number and specific nuisance-block construction are directly taken from Heinrich et al., which is misleading.  
- **Required fix:**  
  - Verify Heinrich et al. (arXiv:2311.13082) and correct all statements to match what that paper actually contains. In particular:  
    • State clearly whether the cited σ(fNL) ≈ 0.7 is **your own derived number** from re-running their public Fisher machinery under your assumptions, or a value literally quoted from that paper.  
    • If it is your own derivative computation, rephrase to “following the methodology of Heinrich et al. , we obtain σ(fNL) ≈ …” rather than “anchored to the Heinrich+2024 σ(fNL) ≈ 0.7 forecast.”  
    • Ensure that the description of bins, systematics treatment, and nuisance parameters correctly reflects Heinrich et al., or is explicitly labeled as your own adaptation.  
  - Update ref.  metadata: title, journal, year are mostly correct but check against ADS and match exactly the published JCAP citation (volume/issue/page, full author list).  
  - Remove any implication that Heinrich et al.  provides the *same* 7-bin, multi-tracer, anomaly-tracer-specific Fisher pipeline used here unless you can point to explicit formulae and configuration choices in Heinrich et al. that exactly match yours.

---

P3-E2 (ESSENTIAL) – Mischaracterization of Münchmeyer et al. σ(fNL) range and context  
- **Location:** Introduction, p.2 (“…3–10× tighter than the Münchmeyer et al.  consensus σ(fNL ) ≈ 0.4–0.9 for SPHEREx-class surveys…”); §V.  
- **Problem:** Reference  is “Münchmeyer et al., Phys. Rev. D 100, 083508 (2019), arXiv:1810.13424” on kSZ tomography constraints on local PNG. That paper does **not** present a “σ(fNL) ≈ 0.4–0.9 *consensus* forecast for SPHEREx-class surveys”; it gives kSZ-based constraints for specific survey combinations (CMB experiments + galaxy tracers), not a direct SPHEREx-alone “consensus” number over that range. Calling 0.4–0.9 a “consensus” SPHEREx forecast from Münchmeyer et al. is factually inaccurate and overstates the connection between their setup and the present work.  
- **Required fix:**  
  - Re-check arXiv:1810.13424 (and any other Münchmeyer PNG forecast paper you actually intend to cite).  
  - Replace “Münchmeyer et al.  consensus σ(fNL ) ≈ 0.4–0.9 for SPHEREx-class surveys” with a statement that correctly reflects what the paper computes (e.g., “Münchmeyer et al.  forecast σ(fNL) ≈ X for a kSZ-tomography configuration combining CMB-S4 with [survey Y]”).  
  - If you want to compare to a 0.4–0.9 SPHEREx expectation, cite the correct SPHEREx-forecast source (e.g., official SPHEREx forecasting papers) and clearly separate that from Münchmeyer’s kSZ result.  
  - Ensure that any “3–10× tighter than” comparisons are recomputed using numbers unambiguously traceable to their actual published values.

---

P3-E3 (ESSENTIAL) – Unsubstantiated claim of “Heinrich+2024 σ(fNL) ≈ 0.7 bispectrum-only”  
- **Location:** Introduction, p.2; Section V (“The headline σ(fNL ) improvement quoted below was originally reported at the fiducial bias enhancement factor α = 0.15 together with an α-dependent sensitivity table … (Appendix C); we now empirically anchor that fiducial value with a direct measurement…”).  
- **Problem:** The manuscript repeatedly refers to a “Heinrich+2024 σ(fNL ) ≈ 0.7 bispectrum-only forecast” as an external benchmark, but ref.  as listed is *this* Heinrich, Doré & Krause JCAP 2024 paper, which is being used as the methodological template. There is no clear evidence in the cited paper of a standalone “0.7 bispectrum-only SPHEREx σ(fNL)” that can be directly quoted as a benchmark for the anomaly-tracer configuration in this manuscript, and the phrasing blurs the line between what is imported from the literature and what is newly computed by the author.  
- **Required fix:**  
  - Explicitly verify whether the “≈ 0.7” number appears in Heinrich et al. as a main-text forecast or if it is derived by you by re-running their code.  
  - If it is not explicitly in their abstract/tables, then you must:  
    • Present it as your own recomputation (“using the Heinrich et al. Fisher set-up, we find σ(fNL) ≈ 0.7 for [configuration]”), not as “the Heinrich+2024 forecast”.  
    • Specify the tracer set, redshift range, and systematics assumptions you used to obtain 0.7, so that it is reproducible.  
  - If Heinrich et al. do quote ≈ 0.7 but for a different tracer or redshift configuration than what you are using, that difference must be spelled out.  

---

P3-M1 (MAJOR) – Reference  status and mismatch with in-press claim  
- **Location:** Intro, p.1 (“Nicolaou et al. … Mon. Not. Roy. Astron. Soc. (2026, in press).”), refs. .  
- **Problem:** Reference  is described as “(2026, in press)” and used as an already accepted MNRAS paper. As of now, arXiv/ADS show Nicolaou et al.’s Astronomaly-related DESI EDR anomaly work as an arXiv preprint and/or submitted manuscript; “in press 2026” may not be accurate. The title, journal, and year need to match the actual current status.  
- **Required fix:**  
  - Check NASA ADS/arXiv for the current status (journal, year, volume, pages or arXiv only).  
  - Update  accordingly (e.g., “Mon. Not. R. Astron. Soc., submitted, arXiv:…” or “MNRAS, in press, 2025, arXiv:…”) rather than asserting a 2026 in-press status unless this is already posted by the journal.  
  - Ensure any numerical claims attributed to Nicolaou et al. (sample size, anomaly rate) exactly match their abstract/tables.

---

P3-M2 (MAJOR) – Liang et al. DESI EDR sample size and anomaly rate  
- **Location:** Intro, p.1 (“Liang et al.  … approximately 250,000 DESI EDR spectra, finding 2,685 anomalies at a 1.07% rate.”); abstract (“largest prior single-survey spectroscopic anomaly catalog of Liang et al.  (2,685 anomalies on DESI EDR; 2,685/250k etc.)”).  
- **Problem:** Liang et al. (MNRAS 525, 1078 (2023), arXiv:2307.07664) indeed report 2,685 anomalies in DESI EDR, but the *denominator* and stated rate in the paper must be checked. Liang et al. use a BGS-ELG-QSO subset of EDR; the exact sample size and resulting fraction may not be “approximately 250,000” nor exactly “1.07%” in the sense quoted here. If your 1.07% is based on your own recomputation on their released catalog, that must be stated; otherwise this is presented as their value.  
- **Required fix:**  
  - Verify from Liang’s abstract/Section 3/tables the **exact** number of spectra used and the anomaly fraction they quote.  
  - Replace “approximately 250,000” and “1.07% rate” with the precise figures from their paper (or clearly state that 1.07% is your recomputed rate on their public table).  
  - Make sure the 73× and 141× ratios (195,829/2,685, 378,080/2,685) are numerically correct and explicitly described as being comparisons to Liang’s *count of 2,685 anomalies*, not to their *rate* or to strictly matched survey selections.

---

P3-M3 (MAJOR) – Cai et al. and Wilson‑Ewing bounce-cosmology citations loosely mapped to specific numeric predictions  
- **Location:** Introduction, p.1–2 (“The quasi-matter bounce model predicts a strongly constrained local non-Gaussianity fNL = −35/8…” citing [13,14,35]); §V; Appendix E.  
- **Problem:** The papers  (Cai et al. JCAP 0905:011, arXiv:0903.0631) and  (Wilson-Ewing JCAP 1303:026, arXiv:1211.6269) discuss matter-bounce cosmologies and non-Gaussianity, but the specific statement “quasi-matter bounce model predicts fNL = −35/8 = −4.375” is much more narrow than their general results. Cai et al. derive non-Gaussianity in matter bounce scenarios; Wilson‑Ewing constructs loop quantum cosmology bounce models. You are asserting a **single hard number** (−35/8) as “the” prediction, which is only valid under restrictive assumptions (single-field, w=0, specific matching). The current text does not make these model assumptions explicit and makes it sound like a universal prediction of “the quasi-matter bounce model.”  
- **Required fix:**  
  - Check in  and  where fNL = −35/8 is actually derived (including all assumptions).  
  - Rephrase everywhere to something like: “In the simplest single-field, w = 0 matter-bounce scenario studied in Cai et al.  and Wilson‑Ewing , the local-type non-Gaussianity can reach fNL ≈ −35/8.”  
  - Make explicit in §V and Appendix E that your σ(fNL) forecast tests that **particular** matter-bounce realization, not “bounce cosmology” in general.  

---

P3-M4 (MAJOR) – Afzal et al. (NANOGrav) and Agazie et al. usage  
- **Location:** §V.A; Appendix E; refs. , .  
- **Problem:** The paper uses NANOGrav 15-yr results in two ways: Agazie et al.  (discovery of GWB) and Afzal et al.  (new-physics interpretation). You construct a KDE-based likelihood using the “free-spectrum KDE pack, Zenodo 10.5281/zenodo.8060824”, and then quote σ and Bayes factors for the matter-bounce vs SMBHB hypotheses. You must ensure that:  
  - The exact data product you use (file name, free-spectrum type, whether HD correlation has been conditioned on) is the one actually described in Agazie et al. and Afzal et al.  
  - Any priors on γ and log10 A you adopt are either identical to, or clearly distinguished from, those used in .  
  - The Bayes-factor comparison “decisive on Jeffreys’ scale” is not presented as their conclusion, but as your own new analysis.  
- **Required fix:**  
  - Cross-check  and  to verify the description of the free-spectrum data and the fact that it is an HD‑correlated posterior in 30 bins; adjust wording if those bin counts or correlation structures differ.  
  - Everywhere you discuss likelihoods or Bayes factors, explicitly label them as “our own KDE–MCMC analysis” of the public NG15 free-spectrum, not as “NANOGrav’s result.”  
  - Check that ref.  and  metadata (author list, title, journal, year) match the ADS entries exactly.

---

P3-M5 (MAJOR) – Nicolaou Astronomaly citation and claims  
- **Location:** Intro, p.1 (“Nicolaou et al.  extended this with a variational autoencoder and the Astronomaly active-learning framework on 208,000 EDR spectra.”).  
- **Problem:** The text attributes a very specific methodology (variational autoencoder + Astronomaly active learning) and an exact sample size (208,000 EDR spectra) to Nicolaou et al. The actual Astronomaly DESI work has a particular pipeline and dataset size; numbers like 208,000 and detailed pipeline composition must be checked directly against that paper.  
- **Required fix:**  
  - Verify in  that (i) the architecture is indeed a VAE plus Astronomaly, (ii) the sample size is 208,000 EDR spectra, and (iii) this is the correct survey subset.  
  - If your number differs by > a few percent from their stated N, fix the text accordingly or qualify that 208,000 is approximate.  
  - Make sure you are not conflating Astronomaly’s own “active learning” loop with any additional procedures you have layered on in your work.

---

P3-M6 (MAJOR) – Heinrich et al. cosmological context vs your internal Fisher engine  
- **Location:** §V, §VI.D and multiple places where you describe a 4n+1 nuisance block, δs-dominated systematics, etc., all “following Heinrich et al. ”.  
- **Problem:** While Heinrich et al. is indeed a Fisher-forecast paper for SPHEREx bispectrum, the very specific nuisance-parameter structure you use (e.g., per-tracer [fNL, δb, δs, δ log N, δσz]) and the numerical priors (0.05, 0.10, 0.10, 0.001) must be checked whether they *exactly* come from that paper or are your own choices. Several of your statements read as if Heinrich et al. provides those nuisance blocks and priors verbatim, which is unlikely.  
- **Required fix:**  
  - Verify the nuisance-parameterization actually used in Heinrich et al.  
  - If your [fNL, δb, δs, δ log N, δσz] block and priors are **not** lifted directly from , rephrase to “we adopt a nuisance-parameter structure inspired by Heinrich et al. ” and clearly list which parts are new.  
  - Remove any wording that suggests that your internal Fisher σ(fNL) ≈ 0.07–0.12 are literature “consensus” values; they must be explicitly labeled as internal checks.

---

P3-M7 (MAJOR) – Abstract overclaims for cosmology relative to the body  
- **Location:** Abstract.  
- **Problem:** The abstract states: “Cosmological applications of the anomaly-selected tracers (multi-tracer fNL forecast; PTA spectral-index consistency) are summarized inline using primary-source methodology. … A multi-tracer σ(fNL) improvement … is parametrised…, the empirical Landy–Szalay measurement … is reported below.” This is a very strong framing (“applications”) but the body of the paper itself concludes that:  
  - The Landy-Szalay bias measurement is consistent with zero improvement at < 1σ,  
  - The σ(fNL) forecasts are highly model-dependent and strongly limited by current α uncertainty,  
  - The PTA spectral index is only ~1.1σ away from the bounce value and ~4.6σ from SMBHB, with no model-comparison concluded.  
- **Required fix:**  
  - Reword the abstract’s cosmology portion so it accurately reflects that your cosmology results are *exploratory forecasts and consistency checks*, not detections or tight constraints.  
  - Explicitly state in the abstract that the multi-tracer σ(fNL) improvement is “consistent with zero at <1σ given current uncertainty on α, and should be viewed as a forecast pending higher-S/N bias measurements.”  
  - Similarly, make explicit that the PTA analysis is a phenomenological fit to public NG15 free-spectrum posteriors, not a new detection.

---

P3-Min1 (MINOR) – Inconsistent treatment of Heinrich (2023 vs 2024)  
- **Location:** Ref.  and surrounding text (“Heinrich+2024”, but label retained as “Heinrich2023 for arXiv‑submission-year continuity”).  
- **Problem:** You are mixing arXiv-submission year and journal publication year within the same reference and calling it “Heinrich+2024” in the text while also saying “label retained as Heinrich2023.” This is confusing for readers and for citation indexing.  
- **Required fix:**  
  - Choose a consistent convention: either refer to it throughout as “Heinrich et al. (2023)” keyed to arXiv:2311.13082, or as “Heinrich et al. (2024)” keyed to JCAP 2024.  
  - Make sure the in-text year matches the reference list year.  

---

P3-Min2 (MINOR) – “Münchmeyer et al. consensus” wording  
- **Location:** Intro, p.2.  
- **Problem:** Using “consensus” when referring to a specific numeric range from a single Münchmeyer paper is over-reaching for a single reference.  
- **Required fix:**  
  - Replace “consensus σ(fNL ) ≈ 0.4–0.9” with “forecast σ(fNL ) values of order 0.4–0.9 in Münchmeyer et al.  for their kSZ configuration” or similar.  

---

P3-Min3 (MINOR) – “In preparation” reference P2 mentioned in text  
- **Location:** Appendix E (“companion paper P2 in preparation”).  
- **Problem:** You refer to a companion paper P2 without providing an arXiv ID or clarifying that it is not yet publicly available. For a cosmology methods paper in PRD, cross-references to non-public work need to be clearly bounded.  
- **Required fix:**  
  - Make clear that P2 is “work in preparation” and ensure no central result in this paper depends on P2.  
  - If any quantitative statements about bounce cosmology rely on P2, either bring the necessary derivations into this paper or delete the dependency.

---

P3-Min4 (MINOR) – Check Cai/Wands/Wilson-Ewing arXiv IDs and titles  
- **Location:** refs. , , , , .  
- **Problem:** These are all bounce-cosmology references. Their titles and years appear plausible, but you must ensure exact correctness (e.g., Wands 2010 “Local non-Gaussianity from inflation” is Class. Quant. Grav. 27, 124002; Cai 2014 “Exploring bouncing cosmologies with cosmological surveys” etc.).  
- **Required fix:**  
  - Verify each of these five references against ADS (title, journal, volume, page, year, arXiv ID) and correct any discrepancies.  

---

P3-Min5 (MINOR) – Minor wording: “Heinrich+2024” vs “Heinrich et al.”  
- **Location:** Introduction, §V.  
- **Problem:** The use of “Heinrich+2024” shorthand is informal and inconsistent with standard PRD style.  
- **Required fix:**  
  - Replace “Heinrich+2024” with “Heinrich et al. ” or “Heinrich, Doré & Krause ” throughout.

---

P3-Nit1 (NIT) – Duplicated and inconsistent parenthetical about Heinrich ref  
- **Location:** Ref.  annotation.  
- **Problem:** The note “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity” is an internal code/library comment rather than something readers need.  
- **Required fix:**  
  - Remove this note from the reference list or move it to a footnote in the LaTeX source only, not the published bibliography.

---

P3-Nit2 (NIT) – Minor arithmetic precision in Liang scaling statement  
- **Location:** Abstract, first paragraph (141×, 73× ratios).  
- **Problem:** You quote 378,080/2,685 = 140.8 ≈ 141 and 195,829/2,685 = 72.9 ≈ 73. The arithmetic is fine, but you might be implying those prior numbers are exact.  
- **Required fix:**  
  - Consider adding “approximately” before “141×” and “73×” or giving the exact ratios once and then using “≈ 141×” later.  

---

## Page-length assessment

The paper is 49 pages and mixes (i) a very long methods and validation section, (ii) full-survey catalog description, and (iii) substantial cosmology and PTA analysis. For the claimed core contribution—construction and characterization of a multi-survey anomaly catalog—this is significantly longer than necessary. A focused version that:  

- Keeps all survey- and method-validation details,  
- Moves most of the cosmology/PTA discussion and UMAP image galleries to appendices,  
- Trims internal “audit log” style caveat prose,  

could be brought to **≈30 pages of main text** plus appendices without loss of scientific content. I recommend the editor strongly encourage such condensation.

---

## σ-scale consistency check

The text explicitly distinguishes between:  

- Autoencoder anomaly σ-like scores (z-scored MSE per survey), and  
- Cosmological σ(fNL) forecast uncertainties and σ significances from the PTA and bias measurements.  

It does *not* combine σ values from different null procedures on the same scale: the author is careful to explain where a local-linear approximation fails and replaces it with a Fisher-positivity-respecting α² mapping. On that specific instruction, I do **not** see an ESSENTIAL issue to flag.

---

## Version-history / internal-log artifacts

The paper text still contains multiple explicit “caveat” and “deferral” labels that read like internal review logs (e.g., “§VI D caveat (i)”, “deferral (a)”), but they are now integrated into the narrative and clearly part of the scientific discussion of residual systematics. I do not see stray ROUND tags or audit headers inside the PAPER TEXT itself. No duplicate phrases like “canonical canonical-mask” appear.

---

## Summary recommendation

**MAJOR REVISIONS**

The catalog-building and survey-method parts are substantial and technically interesting, but there are several factual and interpretational problems in how prior cosmological forecast and PTA papers are cited and used, plus at least one questionable “consensus” statement. These must be corrected before the paper can serve as a reliable reference in PRD. In addition, the manuscript is over-long relative to its main contribution and should be condensed, with clearer separation between established external results and the author’s own internal Fisher/NANOGrav analyses.