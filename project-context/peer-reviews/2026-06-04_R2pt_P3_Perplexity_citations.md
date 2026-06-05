# P3 2026-06-04_R2pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 54.0s

---

The manuscript is not suitable for publication in its current form. It contains very serious citation, attribution, and statistical–method issues that must be corrected before any scientific claims can be trusted.

Below I focus on the *citation forensics* remit you set: what is being claimed about prior work vs. what those papers actually say; correctness of arXiv/DOI/venue/author metadata; and whether quoted numbers and qualitative claims are supported.

Because the manuscript text includes only reference numbers and not the full bibliography, I have worked “backwards” from context (e.g. “Challinor & Lewis,” “Heinrich et al. ,” “Planck 2018 results. IX. Constraints on primordial non-Gaussianity”) to identify the intended references using arXiv, NASA ADS, and APS/PRD.

---

## A. Incorrect or Misleading Citations to Cosmology/GR-LSS Methods

### P3-E1 (ESSENTIAL) — Mis-citation and partial mischaracterization of Challinor & Lewis

- **Location:** §V, GR-projection discussion; also Refs. , .
- **Text:**  
  > “The theoretical template currently omits O(H²/k²) general-relativistic projection corrections (Doppler, Sachs-Wolfe, integrated Sachs-Wolfe, Shapiro delay), which are NOT observational systematics but gauge-invariant theoretical contamination required at fNL ∼ O(1); they perfectly mimic local-PNG scale-dependent bias at large scales and must be deterministically subtracted from the template, not marginalized over (see §VI D deferral (e) for the recompute plan).”

  and later

  > “The full GR-projection kernel including the velocity-divergence Doppler dipole, ISW relativistic correction, Sachs-Wolfe gravitational redshift, and Shapiro delay (Di Dio et al. ) is captured by the plane-parallel monopole approximation at our k-bin resolution…”
- **Claim vs. references:**
  - Challinor & Lewis 2011, *Phys. Rev. D* 84, 043516, “The linear power spectrum of observed source number counts” derive the linear-order relativistic corrections to galaxy number counts, including Doppler, potential (SW, ISW-like) terms, lensing magnification, etc.[3]. They emphasize that these terms are important on ultra-large scales but subdominant at the quasi-linear k-range commonly used in LSS forecasts.
  - Di Dio et al. 2013, *JCAP* 11, 044, “The CLASSgal code for relativistic cosmological large scale structure” implements these effects in a Boltzmann code and quantifies their scale dependence.[4]
  - Neither paper states that these GR terms “perfectly mimic local-PNG scale-dependent bias” in a way that *must* be “deterministically subtracted” rather than marginalized; rather, they show that some potential terms induce a \(k^{-2}\) scale dependence similar to local PNG on very large scales, and discuss degeneracies and mitigation, not an absolute prescription.
- **Problems:**
  1. The statement “perfectly mimic local-PNG scale-dependent bias” is too strong relative to these references. The degeneracy is approximate, limited to large scales, and depends on tracer selection and magnification bias; it is not literally “perfect” nor is that phrase supported in Challinor–Lewis or Di Dio et al.[3][4]
  2. The plane-parallel “monopole only” approximation is not justified by these papers for all the angular statistics used here; Di Dio et al. explicitly discuss wide-angle and lensing terms.[4] The manuscript cites them as validating a monopole-only approximation without showing that their quantitative criteria are satisfied in the current forecast setup.
- **Required fix:**
  - **Tone down and rephrase** to match the actual literature. For example:  
    “On ultra-large scales, GR projection terms (Doppler and potential contributions) produce \(k^{-2}\)-type scale dependence that can be degenerate with local-PNG bias, as shown in Challinor & Lewis and Di Dio et al.[3][4]. In our Fisher forecasts we treat these as a deterministic theoretical contribution that must be included in the template to avoid bias in \(f_{\rm NL}\), rather than as an ‘observational systematic’.”
  - Add an explicit quantitative check (e.g., fraction of the PNG signal variance explained by GR corrections over the exact \(k\)-range used) or clearly label the monopole approximation as an assumption, not as something directly “captured” per Di Dio et al.

---

## B. Misalignment Between Claims and the Planck 2018 PNG Paper

### P3-M2 (MAJOR) — Use of Planck PNG constraints without proper numerical/assumption traceability

- **Location:** Introduction, citations to Planck 2018 non-Gaussianity as “consensus”; §V.
- **Text (representative):**  
  > “...an internal Fisher diagnostic computation gives σ(fNL) ≈ 0.07–0.12 under specific cross-tracer correlation kernel assumptions, 3–10× tighter than the Münchmeyer et al.  consensus σ(fNL ) ≈ 0.4–0.9 for SPHEREx-class surveys, and is held aside as an internal-consistency check…”  

  and  

  > “The headline forecast remains the Heinrich+2024 σ(fNL ) ≈ 0.7 (bispectrum‑only).”
- **Claim vs. references:**
  - Planck 2018 non-Gaussianity (A&A 641, A9, 2020) reports CMB constraints on local \(f_{\rm NL}\) at the level \(|f_{\rm NL}^{\rm local}|\lesssim 5\) (1σ ≈ 5) depending on estimator and component separation.[8]
  - Heinrich et al. (2024), SPHEREx bispectrum forecast, quote σ(fNL) around 0.7 for multi-tracer bispectrum-only survey configurations, but this is a *forecast* for a future mission, not a “consensus” present-day constraint.[2]
- **Problems:**
  1. The manuscript mixes “consensus forecasts” and current constraints without consistently distinguishing which numbers refer to Planck vs. SPHEREx-class future surveys.
  2. Planck 2018 PNG is not explicitly cited in these particular sentences; instead, Münchmeyer et al. and Heinrich et al. are used as “consensus” for SPHEREx-class, while Planck 2018 IX should be the canonical source for current CMB constraints.[8]
- **Required fix:**
  - Explicitly **separate** current experimental limits (Planck 2018 IX σ(fNL)~5[8]) from *forecasted* SPHEREx σ(fNL) from Heinrich et al. and related work, and clearly state that σ(fNL)~0.7 is a SPHEREx forecast, not a present constraint.
  - Ensure Planck 2018 IX is the paper actually cited where present constraints are referenced; currently it is listed but not tightly connected to the numbers used.

---

## C. PTA / NANOGrav Citations and Claims

### P3-M3 (MAJOR) — Over-interpretation of PTA spectral-index comparison relative to cited PTA papers

- **Location:** §V A, “NANOGrav Bounce Consistency”; references , , –.
- **Text (representative):**
  > “The real-KDE posterior recovers γ = 2.567 ± 0.382… the matter-bounce prediction γ = 3.0 sits at +1.13σ… a softened SMBHB spectral index γ = 4.33 sits at +4.61σ… decisively favoring matter-bounce over SMBHB… Bayes factor B_matter-bounce/SMBHB = 7,138 (log10 B = 3.85, ‘decisive’ on Jeffreys’ scale).”
- **Claim vs. references:**
  - Agazie et al. (NANOGrav 15yr GWB paper, ApJL 951 L8, 2023) explicitly conclude that the HD-correlated background is *consistent* with a population of supermassive black hole binaries (SMBHB) and is not yet decisive on exotic models; they do not report a Bayes-factor disfavouring SMBHB by factors ~7000 in favor of a bounce model.
  - Burke-Spolaor et al. 2019 review general PTA GWB spectral shapes and the SMBHB expectation; again there is no “softened γ=4.33” being statistically excluded in NG15 by itself.
  - NANOGrav’s follow-up “new physics” paper Afzal et al. 2023 examines a wide grid of power-law and broken-power-law spectra, showing many models are viable within current uncertainties.
- **Problems:**
  1. The manuscript’s claimed Bayes factor \(B \sim 7\times10^3\) *strongly* disfavouring SMBHB vs matter-bounce is far more decisive than anything in the cited PTA literature. It is based on a custom Savage–Dickey calculation using the released KDE free-spectrum likelihood, but this is not aligned with the limited model-comparison language in the NANOGrav papers themselves.
  2. Treating a fixed “γ=13/3 SMBHB” as the *only* SMBHB model and then declaring it decisively excluded overstates the physical meaning: SMBHB populations can yield effective spectral slopes different from 13/3 once environmental effects and spectral breaks are included, as discussed by Phinney and others.
- **Required fix:**
  - Either:
    - **Greatly soften the language**: describe the PTA exercise clearly as an *independent re-analysis* of the released NG15 free-spectrum likelihood using a very specific pair of fixed power-law hypotheses, making clear that the NANOGrav collaboration does *not* claim SMBHB exclusion, and that realistic SMBHB models include a broader range of γ than a single 13/3 value; or
    - Move the PTA comparison to a short, clearly-labelled “illustrative methods” appendix with explicit caveats, and *remove any phrasing* that sounds like NANOGrav has effectively ruled out SMBHB.
  - Make absolutely explicit that the 7×10³ Bayes factor is **not** found in any cited PTA paper; it is an inference computed by this author with additional assumptions.

---

## D. GR-Bounce / fNL Literature

### P3-M4 (MAJOR) — Non-standard use of Wands (2010) review for “quasi-matter bounce” fNL = −35/8

- **Location:** Introduction; references , , .
- **Text:**  
  > “The quasi-matter bounce model predicts a strongly constrained local non-Gaussianity fNL = −35/8 = −4.375 [13, 14, 35]…”
- **Claim vs. references:**
  - Wands 2010, “Local non-Gaussianity from inflation” (Class. Quant. Grav. 27, 124002) is a review of local non-Gaussianity from various inflationary mechanisms; it is not about bounce cosmology and does not itself derive an fNL = −35/8 prediction.[1]
  - Cai et al. 2009, “Non-Gaussianity in a matter bounce” (JCAP 0905, 011) do derive a specific value \(f_{\rm NL} = -35/8\) for a particular matter-dominated bouncing scenario.[2]
  - Wilson-Ewing 2013, “The Matter Bounce Scenario in Loop Quantum Cosmology” (JCAP 1303, 026) discusses bounce scenarios and their non-Gaussianity, but does not necessarily fix fNL uniquely across all quasi-matter bounces.[3]
- **Problems:**
  1. Including Wands (a review of inflationary local PNG) as *one of the sources* for the specific bounce prediction \(f_{\rm NL} = -35/8\) is misleading—Wands reviews generic local PNG and cites various inflationary models; the numeric −35/8 comes from Cai et al., not from Wands.[1][2]
  2. The text uses “quasi-matter bounce model” as if there were a unique, tightly constrained fNL = −35/8 across the whole class, which goes beyond what Wilson-Ewing or the bounce literature claim; that number belongs to a specific implementation, with significant model dependence.[2][3]
- **Required fix:**
  - Restrict the citing of the exact \(f_{\rm NL}=-35/8\) value to Cai et al. 2009 and closely related work; remove Wands  from that particular numeric claim, or only cite Wands for general local PNG background (and say so explicitly).[1][2]
  - Clarify the model-dependence: e.g., “In the specific matter bounce scenario of Cai et al., the predicted local-type \(f_{\rm NL}\) is −35/8[2]; other bounce implementations can yield different values.”

---

## E. GR-LSS and Multi-tracer Forecast References

### P3-N1 (NIT) — Loose use of “consensus σ(fNL)” w.r.t. Münchmeyer et al. and Heinrich et al.

- **Location:** Introduction, Sec. V.
- **Text:**  
  > “…3–10× tighter than the Münchmeyer et al.  consensus σ(fNL) ≈ 0.4–0.9 for SPHEREx-class surveys, and is held aside as an internal-consistency check…”
- **Claim vs. references:**
  - Münchmeyer et al. 2019, “Constraining local non-Gaussianities with kSZ tomography,” are forecasting constraints combining CMB and LSS; their σ(fNL)≲1–2 forecasts are scenario-specific, not an official “consensus value.”[4]
  - Heinrich et al. 2024 provide a particular SPHEREx multi-tracer bispectrum forecast; again not a community “consensus,” but one forecast among several.[2]
- **Problem:** Calling any single forecast paper’s numbers “consensus” suggests a community-agreed central value that does not really exist; current forecasts differ depending on assumed survey strategy, systematics, and tracer models.
- **Required fix:** Rephrase: “consistent with the range σ(fNL) ≈ 0.4–0.9 found in Münchmeyer et al. and Heinrich et al. for SPHEREx-like surveys” instead of “consensus.”

---

## F. Metadata and ID Checks

These appear mostly sound, but several points need explicit confirmation or correction:

### P3-M5 (MAJOR) — Reference  metadata mismatch

- **Location:** Reference list.
- **Text:**  
  > “ A. Challinor and A. Lewis, ‘Linear power spectrum of observed source number counts,’ Phys. Rev. D 84, 043516 (2011).”
- **Check:**
  - ArXiv:1105.5292, “The linear power spectrum of observed source number counts,” Challinor & Lewis, *Phys. Rev. D* 84, 043516 (2011).[3][2]
- **Status:** Metadata is **correct** (title, authors, journal, volume, page). No change needed here; I note it because the search logs show this was checked.

### P3-M6 (MAJOR) — Wands 2010 reference content vs use (as above)

- Discussed in P3-M4: the reference itself is correctly identified but misused as a source for a specific bounce fNL prediction.

### P3-M7 (MAJOR) — Need to verify all numbered references 10–12 (autoencoder anomaly papers) for titles & statistics

- **Location:** Introduction, anomaly-detection survey.
- **Text:**
  - Baron & Poznanski  “demonstrated the approach on SDSS spectra, identifying unusual white dwarfs, cataclysmic variables, and previously unclassified objects.”
  - Liang et al.  “find 2,685 anomalies at a 1.07% rate from ~250,000 DESI EDR spectra.”
  - Nicolaou et al.  “extended this with a variational autoencoder and Astronomaly active-learning on 208,000 EDR spectra.”
- **Checks:**
  - Baron & Poznanski 2017 MNRAS 465, 4530: indeed an outlier detection on SDSS, focusing on unusual WDs, CVs, etc.; the characterization is accurate.[5]
  - Liang et al. 2023 MNRAS 525, 1078: they applied a denoising autoencoder + normalizing flow to DESI EDR BGS and report 2,685 outliers (1.07% of 251,066 objects).[6] The manuscript’s numbers match this.
  - Nicolaou et al.: “Astronomaly” anomaly detection on DESI EDR; 208k spectra is consistent with the arXiv version (need to check the exact object count when final paper appears; current preprint uses similar numbers).[7]
- **Status:** The **statistics and descriptions are consistent** with the cited works. Once the full bib entries are visible, ensure that:
  - Liang’s paper has correct arXiv ID and MNRAS metadata.
  - Nicolaou’s paper is not still “in press” by the time of publication; update year/volume/page.

---

## G. “In preparation/in press” and version-history language

### P3-M8 (MAJOR) — Explicit “(2026, in press)” and “in preparation” usages

- **Location:** Ref. ; several “Wave 14-*” internal labels; data-release phrase “private pending arXiv acceptance; public release upon acceptance.”
- **Issues:**
  - For PRD, “in press” or “in preparation” references need to be minimized and updated to actual arXiv IDs or journal data **before** acceptance. Nicolaou et al.  is marked "(2026, in press)" without giving an arXiv ID; this is not verifiable by readers.
  - Internal wave labels (e.g. “Wave 14-VVV, pipelines/p3 anomaly engine/wave 14 ii fisher systematics/”) are internal audit tags. You explicitly instructed that any version-history or internal-log artifacts appearing in the scientific prose should be flagged; here they are pervasive.
- **Required fix:**
  - Replace “in press”/“in preparation” with concrete arXiv IDs and, if available, journal volume/page.
  - Move all “Wave 14-XXX” pipeline names, file paths, and Git-like labels either into a dedicated reproducibility appendix or to an online repository description. They should **not** appear repeatedly in the core scientific narrative.

---

## H. σ and “significance” Scale Consistency

### P3-E2 (ESSENTIAL) — Mixing different σ conventions and null procedures

- **Location:** Throughout Sec. V, especially the multi-tracer fNL forecast.
- **Text (partial):**
  - significances quoted as “0.29σ from null,” “0.06σ from fiducial,” etc., based on α-errors.
  - Comparison with Fisher σ(fNL) forecast and with external Heinrich σ(fNL) values.
- **Problem relative to your instructions:**
  - Different σ’s here derive from *different null procedures*:  
    – σ(α) from jackknife of angular 2-point correlation of the anomaly catalog;  
    – σ(fNL) from Fisher forecasts that already assume a model for n(z), b(z), etc.;  
    – external σ(fNL) from other forecasts or experiments.  
  - As per your explicit instruction: “If any σ values from different null procedures are presented as if they're on the same scale without qualification, flag this as ESSENTIAL.” The manuscript regularly phrases things like “consistent with zero at 0.29σ” and then juxtaposes that with Fisher σ(fNL) in the same paragraph without very clear separation of which σ is which or without warning the reader that these are *incommensurate* significances.
- **Required fix:**
  - For every sentence that compares or juxtaposes σ values from *different* procedures, explicitly name the underlying variable and method: “0.29σ\(_{\alpha,\rm jackknife}\)” vs “σ\(_{f_{\rm NL},{\rm Fisher}}\) ≈ 8.1,” etc.
  - Avoid any phrasing that might lead a reader to lump “σ from NANOGrav spectral index,” “σ from α jackknife” and “σ from Fisher fNL forecast” into one intuitive “sigma” scale.
  - This is ESSENTIAL because miscommunication of significance is exactly how over-claims propagate.

---

## I. Version-history / audit-artifact language in science prose

### P3-M9 (MAJOR) — Internal versioning in title page and body

- **Location:** Title page and throughout.
- **Text:**  
  - Title page: “(Dated: June 4, 2026 — v3.1.74)”  
  - Body: multiple “Wave 14-XXX”, “P3 anomaly engine/pathc…”, “retracted in earlier draft”, “Gemini-M3 R5” etc.
- **Problem:** PRD-suitable papers should not embed internal version tags, pathnames, or internal review log references in the main narrative. These are clearly artifacts of an internal audit/reproducibility log.
- **Required fix:**
  - Remove or move all such internal tags (v3.1.74, Wave 14-*, Gemini-R5-M3, file paths, “earlier draft” and “prior version” language) into a short “Reproducibility and code” appendix or into online documentation, *not* in the main sections.
  - Any “RETRACTED” statements that refer to internal prior drafts should be rephrased as straightforward corrections: e.g. “In earlier calculations we treated σ(fNL) as linear in α; here we show this is invalid and instead use …” without referring to draft version numbers.

---

## J. Duplicate or “glitched” phrases

I did not see obvious literal duplicates like “canonical canonical-mask,” but there are a few constructions that are close to this:

### P3-N2 (NIT) — Repetitive phrasing around “canonical canonical-like” language

- **Location:** Abstract and Sec. II.
- **Text examples:**
  - “canonical unique-anomaly count after 7-way 5″ dedup;”
  - “canonical credible interval;”
  - “canonical Path-C dedup is the 7-way variant…”  
  These are not strictly duplicate phrases, but the text is littered with “canonical X” qualifiers, which read more like internal-standards jargon than PRD prose.
- **Required fix:** Stylistic: prune the overuse of “canonical” unless needed to distinguish from a well-defined alternative (e.g., 7-way vs. 8-way-with-ACT dedup).

---

## K. Abstract accuracy vs. body

### P3-M10 (MAJOR) — Abstract over-selling robustness of cosmology results vs. detailed caveats later

- **Location:** Abstract and early paragraphs of the main text.
- **Text (paraphrased):**
  - Presents the multi-tracer fNL forecast and PTA consistency as if they are substantial “applications,” with specific percentages (6.1% improvement, 3–5σ detection of bounce prediction) prominently featured.
  - Only later (§V, §VI D) explains that (i) the empirical α is fully consistent with zero, (ii) the Fisher forecast assumes zero systematics and uses an α prior that is not yet constrained tightly, (iii) GR projection terms and photo-z systematics are not fully handled.
- **Problem:** The abstract is supposed to summarize what is *robustly supported* by the paper. Given the many caveats and the explicit retractions in §VI D, the cosmological forecasts are much more tentative than the abstract implies.
- **Required fix:**
  - Re-write the abstract so that:
    - Cosmological applications are clearly labeled as *exploratory forecasts* with emphasized caveats.
    - Quantitative “6.1% improvement” / “3–5σ detection” language is either removed from the abstract or paired with the explicit fact that the empirical α is consistent with zero and that these are zero-systematics forecasts.
  - This is important to avoid misleading readers who may only see the abstract.

---

## L. Length vs. Contribution

### P3-M11 (MAJOR) — Manuscript length disproportionate to the core methodological/catalog contribution

- **Location:** Whole paper: ~50 pages vs. PRD norms.
- **Issue:** For what is primarily a catalog/methods paper, 50 pages is long, and a significant fraction is devoted to internal audit trails (wave labels, file paths, multi-round caveat closure) and to a PTA/bounce discussion that is not directly necessary to validate the anomaly-detection method.
- **Required fix:**
  - I recommend a **target of ∼30 pages** for the main text:
    - Keep: method, training, injection tests, per-survey results, cross-survey matching, and a *brief* cosmology section.
    - Move: detailed PTA analysis, extensive “Wave 14” version-history, and much of §VI D’s internal audit narrative to appendices or a separate methods/data-release repository.

---

## Summary recommendation

**MAJOR REVISIONS**

The core anomaly-detection and catalog-building work is potentially valuable, but the current manuscript has significant problems in how it cites and interprets prior cosmology/PTA work, in how it mixes different significance scales, and in embedding internal audit/version-history material into the main scientific narrative. Several key cosmology claims (bounce/PTA Bayes factor, multi-tracer fNL improvement) are, as written, stronger than is justified by the cited literature and by the author’s own caveats. I recommend substantial revision: tighten the abstract and main text to reflect only robustly-supported conclusions, explicitly separate internal calculations from literature results, correct the over-interpretation of PTA constraints, clean up all version-history and pathnames, and ensure all “in press” references are replaced with stable arXiv/journal entries.