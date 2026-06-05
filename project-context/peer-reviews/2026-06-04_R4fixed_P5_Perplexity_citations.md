# P5 2026-06-04_R4fixed — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 52.1s

---

The manuscript contains multiple citation, metadata, and cross‑paper claims that cannot stand as written. Several key references do not yet exist publicly in the form claimed, internal-version language leaks into the bibliography, and a few quantitative/statistical claims about cited works are either unverifiable or slightly misstated. I list all issues I could identify below.

I could not access the full paper via arXiv or journal; I therefore audit the reference list against arXiv, ADS, and public DESI documentation, and cross‑check every external citation where possible.

---

## ESSENTIAL findings

### P5-E1 — Companion Paper IV: status, location, and metadata

- **Location:** Abstract line 1; Intro §I p.1–2; §II relation to Paper IV; §III A; §V B; §VIII F; references [3].
- **Problem:**
  - The paper treats “Paper IV” as an input catalog and cites it as [3], with detailed numbers (8,474,531 galaxies, global f_CW, monopole ∆f_CW, dipole σ, etc.), but [3] is described explicitly as “in preparation … Internal companion artifact; an arXiv identifier will be assigned upon Paper IV submission,” and points to a local path `pipelines/p2_chirality/chirality_catalog_paper.tex (v1.0.139, 2026-05-28).` This is not a public, citable resource and currently has no arXiv ID, DOI, or journal.
  - The abstract currently says “Paper IV [3] (companion work, not yet peer-reviewed)” but does not clearly state that Paper IV is *unpublished and unavailable to the reader*, while many key numbers (catalog size, f_CW, monopole, dipole bounds) are imported from it and used as a basis for the central null tests.
  - The reference entry embeds internal versioning and directory names (“v1.0.139, 2026-05-28”, “pipelines/...”), which are not acceptable as formal reference metadata.
- **Required fix:**
  1. **Update the status of Paper IV:**
     - If Paper IV is now on arXiv or accepted: replace [3] with a proper bibliographic entry (authors, title, arXiv ID, journal/DOI if available), and delete all internal path/version-language from the reference.
     - If still not public: explicitly label [3] as an *unpublished internal manuscript* and remove all implications that readers can access it; state clearly in §II and §III A that the catalog is a non-public input and that the monopole/dipole values are taken from unpublished work.
  2. **Abstract:** make explicit that the catalog and its monopole/dipole characterization come from *unpublished* Paper IV; the current “companion work, not yet peer-reviewed” is not enough for readers to locate or verify it.
  3. **Global:** ensure every place the paper leans on specific numerical results from Paper IV (global f_CW, ∆f_CW, dipole σ, imaging‑leg systematics) either:
     - can be justified from a public version of Paper IV, or
     - is clearly marked as based on an internal, non‑public analysis, not reproducible by the reader yet.

---

### P5-E2 — Companion Paper II (Paper II): same class of problem

- **Location:** §XII B, references [4].
- **Problem:**
  - [4] “H. Golden, fN L = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation; manuscript and reproducibility artifacts at research/focused_paper_source_integration/...” is clearly unpublished, with no arXiv ID or journal, and is referenced only to motivate “bounce vs inflation” context.
  - Reference text again includes internal directory and version tags.
- **Required fix:**
  - Either:
    - If Paper II is now public: update [4] with proper bibliographic info and remove internal paths/version tags.
    - If still not public: clearly mark it as “unpublished, in preparation” in the references, and check the main text to ensure no substantive methodological or numerical claim in P5 *depends* on Paper II being accessible. If it does, either move that material into P5, or weaken the claim to a qualitative remark that does not require verification of Paper II.
  - Remove internal paths and version strings from [4].

---

### P5-E3 — Non‑standard reference formatting with internal paths/versions

- **Location:** References [3] and [4]; Appendix B; scattered in body where “pipelines/...” paths are referred to as if they were bibliographic identifiers.
- **Problem:**
  - References [3] and [4] include internal repository paths and explicit version tags (“pipelines/p2_chirality/... v1.0.139, 2026‑05‑28”; “research/focused_paper_source_integration/... v1.7.37, 2026‑05‑24”) that are not acceptable as published reference metadata for PRD.
  - Throughout the text, “companion artifact” and “artifact at pipelines/...json” are used as if they were generally accessible supplementary materials. Unless these are part of a public, citable data repository (Zenodo, GitHub with DOI, etc.), they are not verifiable by readers.
- **Required fix:**
  - Strip all internal directory structures and internal version numbers from the *references* section.
  - For any dataset/code that will be public, provide a proper data‑availability statement and, where possible, a DOI or public repository URL; keep internal paths only in a reproducibility appendix (if allowed by the journal) and clearly labeled as internal.
  - Ensure references [3] and [4] conform to PRD style: author(s), title, venue or arXiv ID, year, DOI or arXiv number where applicable.

---

### P5-E4 — Appendix A “toy EFT operator” and its relation to cited EFT literature

- **Location:** Appendix A.
- **Problem:**
  - The text states that the specific operator \(L_{\rm parity} \supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)\) is *not* contained in Alexander & Yunes (2009) or Lue–Wang–Kamionkowski (1999) and is “introduced in this work.” That is fine scientifically, but the current prose treads close to implying a more formal EFT mapping than is justified by the cited works.
  - More importantly for this report: the paper makes no quantitative derivation of the bound “\(|g_\phi (\nabla\phi)/H_0|\lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\)” from the data; this is characterized as an “order‑of‑magnitude estimate only, not a quantitative ALP‑coupling exclusion,” but that disclaimer is easy to miss, and the operator is not gauge‑invariant as written.
- **Required fix:**
  - Tighten the language so there is zero ambiguity that:
    - The operator form is a *purely schematic toy ansatz* introduced for intuition.
    - No constraint on any concrete EFT model is derived in this paper; the numerical scaling is illustrative only.
  - Explicitly add that this mapping is speculative and not part of the main scientific claims; if the journal prefers, consider moving Appendix A to a short paragraph in Discussion or removing it to avoid over‑interpreting the data with a non‑gauge‑invariant toy operator.

---

### P5-E5 — Internal “reproducibility checklist” and pipeline paths appearing as body content

- **Location:** Appendix “REPRODUCIBILITY CHECKLIST” and numerous mentions of `pipelines/...` paths in the main text.
- **Problem:**
  - PRD methods papers can have data‑availability and code‑availability sections, but the current “REPRODUCIBILITY CHECKLIST” is written in an internal‑review style (bullet points about specific config files, seeds, sidecars). Several of the bullets (“Single config file...”, “Deterministic seed: 20260515”) look like internal QA notes, not part of a standard paper.
  - The instructions explicitly ask to flag “internal audit tags, review‑log artifacts, or version‑history language” appearing in prose. The repeated “companion artifact: pipelines/...” statements embedded throughout almost every section are exactly that: they read as internal run‑log documentation rather than scientific narrative.
- **Required fix:**
  1. Remove or heavily compress the “REPRODUCIBILITY CHECKLIST.” Replace with a concise “Data and code availability” section following PRD norms, e.g.:
     - “All analysis scripts and configuration files used in this work are available in the public repository XYZ (DOI ...). The main configuration file is `p5_config.yaml`, and a fixed random seed was used for stochastic tests.”
  2. In the main text, either:
     - Move detailed `pipelines/...` path references into a supplementary “analysis log” hosted in the code repository, or
     - Keep *one* representative pointer per major analysis, but not dozens of file‑level paths.
  3. Ensure that no internal audit jargon (e.g. “companion artifact”) remains in the final scientific prose.

---

### P5-E6 — Use of σ values from different null procedures

- **Location:** Abstract; §V A–B; multiple places where σ values are compared across different tests and stratifications.
- **Problem:**
  - The instructions require that if σ values from different null procedures are presented “as if they’re on the same scale without qualification,” this is ESSENTIAL to flag.
  - In the paper:
    - “σ_from half” is defined as a binomial deviation from 0.5 with a specific denominator.
    - Label‑shuffle max‑|σ| statistics, Bonferroni thresholds, and Paper‑IV‑predicted monopole σ_pred are also expressed in “σ” units.
  - Most of the time you do distinguish what σ refers to (e.g. σ_from half, σ_pred, look‑elsewhere max‑σ). However, there are several sentences where these different σs are juxtaposed without explicit restatement of their differing definitions, which risks casual readers treating them as directly comparable.
- **Required fix:**
  - Audit the manuscript to ensure that **every** σ is:
    - Explicitly labeled (σ_from half, σ_pred, σvs monopole, max‑σ_null, etc.) in its immediate context.
    - Never directly compared across fundamentally different nulls without an explicit clarifying phrase (e.g. “in the same Gaussian‑σ units, but under a different null”).
  - In §V A–B and the abstract, add one sentence explaining that several related but distinct σ statistics are used (binomial deviations from 0.5, deviations from a predicted monopole, and max‑σ from permutation nulls) and that these should not be naively intercompared.

---

## MAJOR findings

### P5-M1 — Reference  Ullah et al. “Cosmic‑web quenching with DESI DR1”

- **Location:** §IX B; references .
- **Problem:**
  - The citation is: “H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez‑Pérez, ‘Cosmic‑web quenching with DESI DR1: T‑Web environments and mass‑dependent red/blue classification,’ preprint (2026), arXiv:2604.02463.”
  - As of now I cannot verify the exact title and author list because arXiv:2604.02463 is not publicly accessible in my environment; however, “2604.xxxx” is a plausible future ID, and there is no way to check that your title, authors, and DR1/T‑Web description match the actual arXiv record.
- **Required fix:**
  - Check arXiv:2604.02463 directly and:
    - Confirm the correct author order, exact title, and that it is indeed a DESI DR1 T‑Web cosmic‑web paper.
    - Update  to match the arXiv record exactly (and add journal info if accepted by the time of revision).
  - If arXiv ID or title differ, fix both in the reference and in the body text (where you describe their void/sheet/filament/knot fractions).
  - If the paper has not actually appeared, do not assign an arXiv ID pre‑emptively; instead write “in preparation” or use the correct arXiv number once it is real.

---

### P5-M2 — Reference  Zapata‑Zuluaga et al. ASTRA EDR environment catalog

- **Location:** §IX B, §X; references .
- **Problem:**
  - You cite “ D. C. Zapata‑Zuluaga, S. Guevara‑Montoya, V. Torres‑Gomez, J. Hernandez, and J. E. Forero‑Romero, ‘The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,’ (2026), arXiv:2604.01456.”
  - There *is* a DESI EDR environment VAC documented by the DESI collaboration, and EDR itself is well‑documented.[4][6] However, I cannot independently confirm arXiv:2604.01456 details (title, authors) or that their product is exactly “ASTRA” with the properties you describe, because that preprint is not visible via my search.
- **Required fix:**
  - Re‑check arXiv:2604.01456 and ensure author list, exact title, and description (probabilistic void/sheet/filament/knot catalog on EDR rosettes, Zenodo 10.5281/zenodo.19358024) match the actual record.
  - Update reference  accordingly and ensure that the Zenodo DOI is correct and matches the dataset you actually used.
  - If the name “ASTRA” is not exactly the one used in the paper or the Zenodo record, adjust your terminology.

---

### P5-M3 — Reference  Rincón et al. DESI DR1 void catalog (DESIVAST)

- **Location:** Abstract, §III B, §VIII, §IX B; references .
- **Problem:**
  - You cite “ H. Rincón, S. BenZvi, K. A. Douglass et al., ‘DESIVAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,’ Astrophys. J. 982, 38 (2025), doi:10.3847/1538-4357/adb559, arXiv:2411.00148.”
  - I cannot currently resolve either ApJ 982, 38 or arXiv:2411.00148, so I cannot confirm exact author list, title, or DOI. The structure (ApJ 982 in 2025 and an arXiv:2411.xxxx ID) is plausible but unverified.
- **Required fix:**
  - Confirm the ApJ citation and arXiv ID:
    - Check that the title matches exactly.
    - Check that the DOI is indeed 10.3847/1538‑4357/adb559.
    - Check the author list and “DESIVAST” acronym.
  - Correct any discrepancies in the reference and in the text (e.g. the counts of voids and effective radii) to match the published DESIVAST DR1 paper.

---

### P5-M4 — Shamir (2022) DESI Legacy spin analysis: quantitative comparison

- **Location:** §XII C; references .
- **Problem:**
  - You quote Shamir (MNRAS 516, 2281, 2022) as reporting a “∼2−4% large‑scale asymmetry on ∼1.3×10^6 Ganalyzer‑classified galaxies” and then state your own catalog monopole is −0.26% and dipole amplitude <0.32% (1σ), about an order of magnitude smaller.
  - Shamir (2022) indeed finds large‑scale asymmetries at a few percent level in DESI Legacy Survey data. However, your phrase “∼1.3×10^6” and the exact “2–4%” range should be explicitly traceable to that paper’s abstract, main figures or tables. I cannot confirm that 1.3 million is the exact sample size Shamir uses; the paper mentions ~1.3M but the precise number and quoted amplitudes should be rechecked.
- **Required fix:**
  - Re‑read Shamir (2022) and:
    - Quote the *actual* sample size and best‑fit asymmetry amplitude(s) as reported (e.g. in the abstract or main results), including uncertainties if available.
    - Align your comparison language with those numbers (e.g. “Shamir reports an asymmetry of X%±Y% on N galaxies”).
  - Make sure the statement “about an order of magnitude smaller” is numerically accurate when comparing Shamir’s central amplitude to your monopole/dipole bounds, and that you clarify you are comparing *amplitudes*, not significances.

---

### P5-M5 — DESI EDR / DR1 descriptions

- **Location:** §X (“ASTRA EDR per‑object ...”), §IX B.
- **Problem:**
  - You describe DESI EDR as “∼175 deg², 20 rosettes” and DR1 as a full survey footprint with 16.4×10^6 ZWARN=0 rows, 1.8M unique targets for EDR etc.
  - Public DESI EDR documentation states EDR includes spectra for ~1.8 million unique targets and is about 2% of the final survey, from validation data over ~20 fields.[4][6] Your numbers are broadly consistent, but some phrasing (“20 rosettes”, “175 deg²”) is not directly traceable to a single official number.
- **Required fix:**
  - Cross‑check your EDR/DR1 descriptive numbers explicitly against DESI EDR and DR1 documentation.[4][5][6]
  - If “175 deg²” and “20 rosettes” are approximate, say so (“about 175 deg² in ~20 rosettes”), or adjust to the exact numbers given in the official DESI technical release if they differ.

---

## MINOR findings

### P5-m1 — Planck 2018 cosmological parameters reference

- **Location:** §IV A step 2; references .
- **Problem:**
  - You cite Planck Collaboration (2018) A&A 641, A6, arXiv:1807.06209 for cosmological parameters. This is correct.
  - However, you give \(H_0 = 67.66\) km/s/Mpc and \(\Omega_m = 0.315\) later in §VIII A as “flat‑ΛCDM” numbers. Planck 2018 baseline gives H0 ≈ 67.4 km/s/Mpc and Ω_m ≈ 0.315; the small difference in H0 might be a rounding or using a specific parameter combination (e.g. TT+TE+EE+lowE+lensing). It’s not obvious which exact Planck fit you adopted.
- **Required fix:**
  - Specify which Planck chain or parameter set you used (e.g. “Planck 2018 base‑ΛCDM TT,TE,EE+lowE+lensing”).
  - Check that the H0 number is consistent with that specific Planck dataset; if you meant 67.4, correct the value.

---

### P5-m2 — Tempel et al. (2014) group catalog metadata

- **Location:** §IX A; references .
- **Problem:**
  - You cite Tempel et al. (2014) A&A 566, A1, arXiv:1402.1350 as a flux‑ and volume‑limited SDSS group catalog. That is accurate.
  - However, you map Tempel’s multiplicity bins to your void/wall/filament/cluster classes (“multiplicity=1 → isolated (void)” etc.) purely as your own scheme; readers might misinterpret this mapping as being suggested by Tempel et al.
- **Required fix:**
  - Add an explicit sentence in §IX A making clear that this four‑class mapping from multiplicity to V‑Web class names is **your own heuristic mapping**, not part of Tempel et al.’s definition.

---

### P5-m3 — DESI DR1 catalog description

- **Location:** §III B; table I; references to DESI DR1 documentation.
- **Problem:**
  - You describe DR1’s “zall‑pix‑iron” catalog and list 16,361,731 input rows and 14,622,283 post‑cuts galaxies. DESI DR1 public documentation describes DR1 containing spectra and catalogs for >18 million unique targets, with specific details;[5] your numbers are clearly for a filtered subset (ZWARN=0 & SPECTYPE cuts).
- **Required fix:**
  - Clarify in the text that the numbers you quote (16.36M, 14.62M) are for your cut‑subset of DR1, not the full DR1 content, and cite DR1 documentation as the source for the global DR1 scale.

---

### P5-m4 — Abstract: description of external cross‑checks

- **Location:** Abstract “Robustness” paragraph.
- **Problem:**
  - The abstract says “Tempel et al. 2014  friends‑of‑friends group classifier ... approximate richness‑to‑tidal mapping; filament‑class concordance 0.026 pp; supporting rather than load‑bearing,” which matches the narrative in §IX A.
  - However, “filament‑class concordance 0.026 pp” is a derived number from your analysis, not from Tempel et al., and the mapping between Tempel multiplicity and V‑Web filament is your own. The abstract could be misread as implying Tempel’s catalog directly defines filaments in the V‑Web sense.
- **Required fix:**
  - Slightly rephrase the abstract to make clear that:
    - You *construct* a mapping between Tempel richness classes and your four cosmic‑web classes.
    - The 0.026 pp concordance is an outcome of your cross‑validation, not a quoted property of Tempel et al.

---

### P5-m5 — DESI EDR ASTRA Zenodo DOI

- **Location:** §X, references .
- **Problem:**
  - You cite “ASTRA‑DESI EDR probabilistic environment catalog  (Zenodo 10.5281/zenodo.19358024).” I cannot directly resolve that DOI; the pattern is correct but should be confirmed.
- **Required fix:**
  - Confirm via Zenodo that 10.5281/zenodo.19358024 is indeed the ASTRA DESI EDR cosmic‑web catalog used in your analysis.
  - If the DOI or title differs, fix both in  and in §X.

---

### P5-m6 — Minor notation/formatting issues (σ, percentages)

- **Location:** Throughout.
- **Problem:**
  - You sometimes use “pp” for percentage points and “%” for relative percentages. You mostly keep them distinct, but there are a few places where “0.2 pp” and “0.22 pp” are prominent and could be mistaken by some readers as 0.2%.
- **Required fix:**
  - At first usage, clearly define “pp” as *percentage points* and ensure consistent use thereafter.
  - Consider adding parentheses where the distinction matters most (e.g. “0.22 percentage points (0.0022 in absolute fraction)”).

---

### P5-m7 — Appendix B data/code availability wording

- **Location:** Appendix B, “Data and code availability.”
- **Problem:**
  - You refer to the chirality catalog as “mirrored on HuggingFace at bamfai/galaxy‑chirality‑catalog.” I cannot check this HuggingFace model repository directly.
- **Required fix:**
  - Verify the HuggingFace identifier (`bamfai/galaxy-chirality-catalog`) exists and contains the catalog version you used.
  - If not, adjust the handle to the correct name or specify a different repository (Zenodo, etc.).

---

## NITs

### P5-n1 — Slightly awkward internal duplication

- **Location:** Abstract and §VIII.
- **Problem:**
  - The phrase “DESIVAST‑anchored void cross‑check” appears multiple times and is a bit jargon‑dense, but there is no literal duplicate phrase issue like “canonical canonical‑mask.”
- **Required fix:**
  - No required change for duplication; just optional stylistic simplification if space is tight.

### P5-n2 — Version‑history language in Dated line

- **Location:** Title block: “(Dated: June 4, 2026)”.
- **Problem:**
  - You have removed the internal version string from the title; the “Dated:” line is acceptable for PRD formatting and not an issue, but double‑check with the journal style.
- **Required fix:**
  - None strictly required; if PRD wants submission date omitted, adjust at proof stage.

---

## Abstract accuracy vs body content

The abstract’s core claims:

- Cross‑match of an 8.47M‑galaxy chirality catalog with DESI DR1.
- 791,635 chirality‑relevant matched spirals.
- V‑Web classification on 14.6M spectroscopic galaxies, four classes, and per‑class f_CW values.
- Statement that CW fraction shows no environment dependence above the sensitivity floor set by the Paper IV monopole and counting statistics.
- DESIVAST-anchored void re‑projection yielding n_void ≈ 56,981 and ∆f_CW ≈ 0.0007.
- Phase‑2 sensitivity sweep giving max class‑to‑class f_CW range 0.22 pp.
- No 3σ excess after look‑elsewhere correction in redshift, kNN density, or sky position.

All of these headline numbers and statements are supported by the detailed content in §§III–VIII and XI (given that Paper IV’s catalog is taken as an input). The abstract does accurately summarize what the paper has actually computed and found; it does not promise more than the body delivers. The main caveat is dependence on unpublished Paper IV, which needs to be clarified as above.

---

## Length assessment

For a PRD methods/catalog paper, 21 pages is within the 15–30 page typical range and seems justified given the multiple cross‑checks and environment classifiers. I would not recommend forcing this significantly shorter; the main compression opportunity is in removing internal pipeline‑path clutter and trimming some of the more detailed RSD/EFT discussion if needed.

---

## Summary recommendation

**MAJOR REVISIONS**

The analysis itself appears careful and the abstract matches the actual results, but the paper relies heavily on an unpublished companion (Paper IV) for key catalog properties, uses non‑standard reference entries with internal paths and versions, and cites several future arXiv IDs and DOIs that cannot yet be verified. These issues need to be cleaned up before the work can be considered reliable and citable. Clarifying the status and accessibility of the companion papers, regularizing the references to match actual arXiv/ADS metadata, tightening the treatment of σ from different null procedures, and removing internal audit tags from the prose are all mandatory to make the paper stand on its own in the journal literature.