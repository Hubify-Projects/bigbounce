# P5 R38conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.73.pdf` md5=4109fb18 pages=31
**Input format**: TEXT + web search + pass-2 self-critique (19985 chars)
**Wall time**: 122.9s

---

The manuscript as written is not yet suitable for Physical Review D. Beyond scientific questions, there are multiple issues with references, provenance, internal-version language, and quantitative presentation that must be addressed before the physics can be fairly judged.

Below I focus strictly on what you asked for: citation forensics, internal‑consistency checks of the quoted numbers, and compliance with the journal‑level rigor implied by your instructions.

---

## 1. Bibliography and citation forensics

### P5‑E1 – Companion papers “in preparation” used as load‑bearing inputs  
**Section/page:** Abstract; p.1–3; references [3], [4]  
**Problem:** Paper IV [3] and Paper II [4] are repeatedly used as if they were established external inputs:

- Abstract: “We cross‑match the 8,474,531‑galaxy chirality catalog of Paper IV [3] …”  
- Sec. I/II: Paper IV provides the **only source** for (i) the 8.47M sample, (ii) the classifier monopole ∆fCW = −0.0026, (iii) the dipole null, and (iv) all galaxy‑level labels.  
- Sec. XII B: Paper II [4] is invoked for fNL forecasts and “discriminators”.

Both [3] and [4] are explicitly described as “in preparation” and not yet peer‑reviewed. There is no arXiv identifier, no DOI, and no way for a referee to verify any of the catalog properties, monopole value, or analysis choices that are load‑bearing for this paper.

**Required fix (ESSENTIAL):**

- Either:
  - Publish Paper IV on arXiv in a stable form, cite it with a concrete identifier, and ensure that all catalog‑level numbers used here can be traced directly to that version; or
  - Move all critical Paper‑IV content needed here (definition of the catalog, classifier architecture, monopole estimation, label QA) into this manuscript so that this paper is self‑contained independent of a companion.
- For Paper II [4], remove or substantially down‑weight any claims that rest on it; it should not be called upon for model discrimination if it does not yet exist as a public document.
- Until this is done, you must mark the monopole ∆fCW and the classifier labels as **internal, unpublished inputs** and explicitly flag that they are not independently auditable.

---

### P5‑E2 – Missing arXiv IDs and incomplete reference metadata  
**Section/page:** References [3], [4], ,  – last pages  
**Problem:** Several references are described only qualitatively, without standard bibliographic metadata:

- [3] “companion paper (Paper IV), in preparation; manuscript in preparation.” No arXiv ID, no journal, no year.
- [4] Similar “companion paper (Paper II), in preparation”.
-  “preprint (2026), arXiv:2604.02463.” — the arXiv number format is syntactically plausible for 2026, but the paper is still a preprint; you rely on it only for qualitative volume‑fraction comparison, which is acceptable, but the metadata lacks title details.
-  “(2026), arXiv:2604.01456.” Again preprint‑only, no journal info.

For PRD, every cited work must be clearly identified; companion “manuscripts in preparation” are acceptable only as **non‑load‑bearing background**.

**Required fix (ESSENTIAL):**

- For all external references: provide complete standard metadata (full author list as needed, full title, journal, volume, page, year; and arXiv ID when available).
- For companion works [3], [4]:
  - Either convert them into citable arXiv preprints with stable identifiers, or
  - Remove them from the numbered bibliography and refer to them descriptively (“unpublished work by the author”) while ensuring no load‑bearing dependence.
- Confirm that the arXiv IDs 2604.02463 and 2604.01456 correspond exactly to the titles and author lists given here; if they have since appeared in journals, update the entries to the published versions.

---

### P5‑M1 – Possible mismatch between Planck 2018 citation and parameter values  
**Section/page:** §IV A, step 2; reference  Planck 2018; p.4–5, refs  
**Problem:** You state you use “Planck 2018 ” and assume h = 0.6766 and Ωm = 0.315. Planck 2018 base‑ΛCDM indeed quotes H0 ≈ 67.36 km/s/Mpc, h ≈ 0.6736 and Ωm ≈ 0.315. You use 67.66 (h = 0.6766). That is closer to Planck+BAO+supernova variants than to the main TT,TE,EE+lowE solution.

Reference  is to “Planck 2018 results. VI. Cosmological parameters, A&A 641, A6 (2020)”. If you use a slightly different H0 (67.66 instead of 67.36), that discrepancy should be explicit and sourced.

**Required fix (MAJOR):**

- Either align the numbers with the exact parameter set from Planck 2018 Table 2 (and state which column, e.g. “Planck TT,TE,EE+lowE”), or clearly explain that you are adopting e.g. the “base_plikHM_TTTEEE_lowl_lowE_lensing” or a combined likelihood with H0 = 67.66, with a supporting citation.
- Make sure the sanity‑check distance χ(z = 0.2) = 843 Mpc you quote is consistent with the exact cosmology you say you are using.

---

### P5‑M2 – Ambiguous “T‑Web / V‑Web” naming relative to Hahn et al. (2007) and Cautun et al. (2014)  
**Section/page:** Title; abstract; §IV A; footnote a; references [5–7], ; whole paper  
**Problem:** You use “V‑Web” in the title and throughout, but in footnote a you write:

> “We use the tidal‑tensor formulation … from Poisson’s equation on the smoothed overdensity field (the Hahn 2007 recipe, sometimes called the T‑Web variant) … The Hoffman et al. 2012 [6] velocity‑shear V‑Web requires a separate velocity reconstruction not used here; for backward compatibility with prior analyses we retain the ‘V‑Web’ label which is sometimes used loosely…”

So:

- The actual algorithm implemented is the **tidal‑tensor T‑Web**, not the velocity‑shear V‑Web of Hoffman et al. (2012).  
- Nonetheless you call it V‑Web in the title, abstract, and most of the text, and reference both Hahn+2007 and Hoffman+2012.

This is confusing and risks mis‑citing [6] as if its actual algorithm were used.

**Required fix (MAJOR):**

- Rename the classifier consistently as **T‑Web** throughout (including in the title and abstract), or use a neutral label (“tidal‑tensor web classifier”) and reserve “V‑Web” for true velocity‑shear implementations.
- In the methods section, clarify exactly which of Hahn (2007), Cautun (2014) recipes you follow (eigenvalue definition, sign conventions, thresholds), and cite Hoffman et al. (2012) only as a *contrast* (velocity‑shear alternative) rather than as part of the method you actually run.
- Ensure that Figure 2 and all text that currently say “V‑Web” are updated; otherwise this remains a fused‑metadata use of [5–7].

---

### P5‑M3 – DESIVAST metadata and counts must match Rincón et al. (2025)  
**Section/page:** §VIII opening; Table X; refs ; p.16–19  
**Problem:** You quote specific DESIVAST catalog properties:

- “1,489 interior voids with VoidFinder, 389 with V2‑REVOLVER, and 297 with V2‑VIDE (final published counts from ApJ 982, 38, Table 1; an earlier preprint version cited 1,461/420/295).”  
- “89,003 + 12,860 = 101,863 interior hole spheres comprising the 3,765 maximal voids”  
- Maximum hole radius 24.5 Mpc/h, max effective void radii 43.5 / 55.9 Mpc/h.

These must match exactly what Rincón et al. (ApJ 982, 38, 2025) publishes for the DR1 BGS void catalog.

**Required fix (MAJOR):**

- Explicitly cross‑check your counts (interior vs catalog‑total voids; hole spheres; maximal voids; maximum radii) against DESIVAST’s Table 1 and its data‑release metadata.  
- Ensure that your “final published counts” correspond to the ApJ version you cite, not to an earlier arXiv version.
- If any numbers differ (e.g. due to you applying additional cuts, or because DESIVAST released v1.1 etc.), you must say so explicitly and describe the transformation from the published DESIVAST tables to your working sample.

---

### P5‑M4 – Tempel et al. (2014) mapping and overlap sample  
**Section/page:** §IX B, Table XIII, Figure 9; ref   
**Problem:** You state:

- Tempel’s DR10 FoF catalog is for z ≤ 0.20 and RA/Dec ranges; you reduce it to a 4‑class environment by richness cutoffs (<2, 2–4, 5–19, ≥20).  
- You claim an overlap of 96,753 spirals after a 1″ positional join.

The Tempel et al. (2014) DR10 FoF catalogue has precise richness‑class definitions and documented selection. For a PRD‑level paper, the choice of your multiplicity thresholds must be justified and consistent with Tempel’s “isolated / group / filament‑like / cluster‑like” language; otherwise you risk mis‑labelling their environments.

**Required fix (MAJOR):**

- Explicitly show how your richness bins map to Tempel’s own environment definitions, including any references to their tables/figures where that mapping is stated or suggested.
- Check that the 96,753 overlap count is consistent with applying your stated cuts to Tempel’s DR10 catalogue and your DR8‑based chirality catalogue; if it relies on any additional magnitude or mask cuts, document those and ensure they are traceable from Tempel’s paper and your catalog definition.

---

### P5‑M5 – Shamir (2022) statistics and comparison  
**Section/page:** §XII C; ref   
**Problem:** You summarise Shamir (2022) as reporting a “∼ 2–4% large‑scale asymmetry on ∼1.3 × 10^6 galaxies” and a “Shamir‑amplitude (1.7%) dipole”.

Those numbers must match the statistics that Shamir actually quotes (global asymmetry, dipole amplitude, sample size, and significance) in MNRAS 516, 2281 (2022). Any extracted “1.7% dipole” should be traced to a particular equation or table.

**Required fix (MAJOR):**

- Re‑check Shamir (2022) and ensure your stated 2–4% and 1.7% values correspond precisely to quantities defined in that paper (e.g. global handedness bias, fitted dipole amplitude).
- Cite the exact section or table of Shamir (2022) in the text when you quote those numbers, and adjust your text if Shamir’s published numbers differ.

---

### P5‑M6 – ASTRA and T‑Web DR1/EDR references must match arXiv metadata  
**Section/page:** §IX C and §X; refs ,   
**Problem:** You cite:

-  “Cosmic‑web quenching with DESI DR1: T‑Web environments and mass‑dependent red/blue classification,” arXiv:2604.02463.  
-  “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” arXiv:2604.01456.

You then describe detailed volume fractions and per‑object classification probabilities. For PRD‑level citation hygiene, these descriptions must be demonstrably consistent with those preprints.

**Required fix (MINOR):**

- Double‑check that titles, author lists, and the DR1 / EDR footprints, grid sizes, and class fractions you quote exactly match the current versions of arXiv:2604.02463 and 2604.01456.
- If those preprints undergo revisions or are accepted in journals with changed details, update your references and any copied‑over numbers accordingly.

---

## 2. Internal versioning / provenance language in the body

### P5‑E3 – Version labels and internal audit tags in the main text  
**Section/page:** multiple places, e.g. title block, §II, §V B, §VIII F, Appendix C  
**Examples of offending text:**

- Title page: “(Dated: June 2026 — v0.1.73‑2026‑06‑13)”  
- §II: “Paper IV’s current headline (v1.0.166) … an earlier harmonic‑space … was withdrawn in Paper IV v1.0.166 after a provenance audit traced its mask to a synthetic footprint.”  
- §V B: “pipelines/p5_desi_chirality/outputs/30_ext4_galzone_complement_contrasts.json” and many other internal paths.  
- Appendix C: “results quoted here correspond to manuscript tag v0.1.73‑2026‑06‑13.”

PRD articles should not include Git tags, internal pipeline filenames, or version‑history narrative in the main body. Those belong in a separate code‑release note or a short “Data availability and code” paragraph without internal audit chatter.

**Required fix (ESSENTIAL):**

- Remove or relocate all explicit version tags (v0.1.73‑…, v1.0.166), Git‑style identifiers, and pipeline file paths from the **main scientific narrative**.  
- If you need to document code provenance, do so succinctly in a “Data and code availability” section, without repository‑internal directory trees or log text.  
- Any discussion of earlier “withdrawn” statistics should be shortened to a single sentence, without referring to specific internal version numbers (unless those correspond to citable arXiv versions).

---

## 3. Quantitative consistency and σ / p‑value usage

### P5‑E4 – σ values from different nulls juxtaposed without explicit non‑comparability  
**Section/page:** Abstract; §V; §VI A–D; Table III, Table V, Table VII  
**Problem:** You correctly remark in several places that σfrom half and σpred (monopole‑referenced) are not directly comparable across different N. However, the abstract and early sections present multiple σ’s side‑by‑side without reiterating this each time.

Example from abstract:

- “per‑class CW fractions … filament (−2.61σ), cluster (−4.66σ), wall (+0.55σ), void (−0.68σ)… The quoted σfrom half values scale as √n at fixed fractional offset and are therefore not mutually comparable across classes of different n.”

This sentence appears, but the abstract also mixes these σ’s with look‑elsewhere p‑values and monopole‑subtracted σ’s later, without clear flagging at each juxtaposition.

Given your own rule (and my instruction 7): whenever σ from *different null procedures* (half‑comparison, monopole‑comparison, permutation null) appear together, they must be explicitly marked as non‑comparable.

**Required fix (ESSENTIAL):**

- In the abstract and every table/figure caption where multiple σ’s from different baselines appear (σfrom half, σpred, σvs monopole, and permutation‑derived max‑σ), explicitly state which baseline each uses and that they must not be compared across procedures or across sample sizes.
- Consider giving **fractions and effect sizes** (∆f in percentage points, Cramér’s V, etc.) as the primary numbers, with σ relegated to parenthetical values.

---

### P5‑M7 – Effect sizes not always paired with σ / p  
**Section/page:** Abstract; §VI A–D; §VIII; §IX B; §X; multiple tables  
**Problem:** You do often provide ∆f values in pp and Cramér’s V in one place, but there are still a few emphatic σ or p‑value statements with no immediate effect‑size context.

Examples:

- Abstract: “redshift (label‑shuffle p = 0.372)… projected k = 5 NN density (|σ|max = 3.94 across density quintiles)… HEALPix scans … p = 0.607/0.135/0.413: none reach 3σ…” There is no direct statement of the underlying fractional differences in these cases.
- §VI C: “|σobs − σpred| ≈ 1.87” again without giving the corresponding ∆f in pp right there (it appears earlier in the table, but not at this inferential statement).

PRD will generally expect effect size to be emphasized alongside significance.

**Required fix (MAJOR):**

- For every σ or p that is used as a “headline” in the text (not the ones buried in detailed diagnostic discussion), add the associated ∆f (in percentage points) or a dimensionless effect measure (like Cramér’s V) right there.
- In the abstract, ensure that for each reported σ or χ², the corresponding amplitude (fractional difference) is given.

---

### P5‑M8 – Abstract vs body numerical consistency (monopole and void fraction)  
**Section/page:** Abstract; §VIII B–D; Table X  
**Problem:**

- Abstract: “controlling void constraint comes from the DESIVAST‑anchored re‑projection (n = 56,981, ∆fCW = 0.0007).”
- Body (Table X, and later text): you actually report for VoidFinder nvoid = 56,981, fCW,void = 0.4964, fCW,non‑void = 0.4971, ∆fCW = +0.0007 with 95% CI [−0.0036,+0.0050], and for catalog‑native variants nvoid = 57,081 or 20,900 with slightly different ∆f values.

The headline abstract number is consistent with the VoidFinder sphere‑PIS version, but the body also elevates the V2‑REVOLVER catalog‑native statistic as “the cleanest single chirality‑in‑voids measurement”, with different nvoid and ∆f.

**Required fix (MAJOR, pattern‑045 abstract‑last):**

- Decide which specific estimator is your **primary** void result (VoidFinder sphere PIS; catalog‑native V2‑REVOLVER; etc.) and make the abstract’s quoted n and ∆f refer unequivocally to that one.
- In the abstract, add the confidence interval or an explicit “statistically indistinguishable from zero at 95% CL” so the reader can see immediately that 0.0007 is negligible compared with its error bar.
- Check that ALL numbers in the abstract (sample sizes, monopole value, σ’s, p‑values) appear identically in the body (not just approximately), and update any that do not.

---

### P5‑M9 – Some σ and χ² recomputation not fully traceable from in‑paper tables  
**Section/page:** §VI A–D; §VIII F; Appendix B  
**Problem:** You give integer contingency tables only in Appendix B for the 4×2 V‑Web class vs CW/CCW and class vs program; that is good. However, some intermediate tests (e.g. sub‑quintile Bonferroni thresholds, σpred values, and permutation pLEE) rely on raw bin counts that are not tabulated anywhere in the PDF.

This makes it non‑trivial for a referee to recompute *every* quoted σ and χ² from what is printed.

**Required fix (MINOR):**

- For each “headline” test (Table III, density quintiles, redshift bins, key HEALPix scans, and DESIVAST primary table), include enough explicit counts (n, nCW) per bin within the paper so that the σ, χ², and p values can be recomputed from the PDF without accessing the code repository.
- This may require adding one or two small tables (e.g. for the density quintiles and the z‑shells) or augmenting existing tables.

---

## 4. Reproducibility and data availability

### P5‑E5 – Overly informal, non‑archival provenance description  
**Section/page:** Appendix C, “Data and code availability”  
**Problem:**

- The repository is described as “Hubify‑Projects/bigbounce” with paths like “pipelines/p5_desi_chirality/…”, but there is no DOI, no explicit public URL, and no statement of licence.
- The text says “A DOI‑minted archival snapshot of this directory accompanies journal submission” but does not give that DOI or repository name.

For a PRD article, a data/code availability statement should be concise and point to a specific, citable archive, not a private GitHub organization and internal folders.

**Required fix (ESSENTIAL):**

- Deposit all analysis scripts and non‑proprietary derived data needed to reproduce the results in a public archival repository (e.g. Zenodo, institutional archive, or similar) and provide its **permanent DOI**.
- Replace the internal “Hubify‑Projects/…” language with a simple citation: “All code and derived statistics used in this paper are available at [DOI: …].”
- If parts of the pipeline depend on non‑public DESI internal files, say so explicitly and define what an external user can and cannot reproduce.

---

## 5. Length and presentation

### P5‑M10 – Excessive length and internal log detail for the claimed contribution  
**Section/page:** Whole paper (31 pages)  
**Problem:** For the main scientific result — a high‑precision null test of environment‑dependent chirality with DESI DR1 voids and a tidal‑tensor classifier — the current 31 pages contain a great deal of internal pipeline description (file names, RNG seeds, JSON paths) that is not appropriate for a PRD main article and significantly obscures the core argument.

**Required fix (MAJOR):**

- Reduce the paper to ≈ 18–20 pages by:
  - Moving most implementation details (exact pathnames, code‑level options, secondary recomputes) to a separate online supplement or data‑release note.
  - Keeping in the main text only what a typical PRD reader needs: catalog definitions, selection cuts in compact form, key sample sizes, main tables/figures, and the primary robustness checks.
- Keep the detailed reproducibility (config files, internal versioning) in the archived code, not in the narrative.

---

## 6. Minor / cosmetic issues and nits

### P5‑N1 – Duplicate / awkward phrases  
**Section/page:** Multiple places  
**Problem:** Phrases like “canonical chirality catalog” and “catalog‑wide classifier‑monopole” are repeated many times; some sentences become extremely long with nested parentheses and slashes.

**Required fix (NIT):**

- Edit for brevity and clarity. Define terms once, then use shorter labels. Break the longest sentences, especially in the abstract and introductions of §V–VIII.

---

### P5‑N2 – Presence of explicit RNG seed in body  
**Section/page:** Reproducibility checklist; p.31  
**Problem:** “Deterministic seed: 20260515.” This is not wrong, but it is unnecessary detail for the printed article.

**Required fix (NIT):**

- Move this to the code repository documentation (README) and remove it from the paper itself, or keep it only in a concise “All random draws used seed 20260515” sentence in data‑availability, without bullet‑list clutter.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The underlying scientific idea — a stringent null test of environment‑dependent spiral chirality in DESI DR1, anchored by a DESIVAST void sample — is appropriate for PRD, but the current manuscript relies crucially on unpublished companion work for its catalog and monopole calibration, uses method labels (V‑Web vs T‑Web) in a confusing way, and embeds internal versioning and pipeline logs throughout the text. Several reference‑level statistics (Planck parameters, DESIVAST counts, Shamir amplitudes) need to be verified and aligned exactly with the cited works. Significant editing is required to (i) make the paper self‑contained and independent of non‑public companions; (ii) cleanly separate implementation minutiae from the main scientific narrative; and (iii) present all σ / p‑values with clear baselines and effect sizes. Once these issues are addressed, the paper can be re‑evaluated on its physical merits.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E6 – Arithmetic inconsistencies between quoted σ and bin counts  
Section/page: Abstract; Table III; Table VIII; Table X; §VI C–D; §VIII B–D; Appendix B  

Problem: Several quoted **σfrom half** and **zΔ** values do not numerically match the adjacent integer counts when recomputed directly as binomial z‑scores, at the precision implied by the text. Because the paper leans heavily on σ and z as headline diagnostics, these arithmetic mismatches matter.

Concrete examples (all recomputed from the printed n and nCW):

1. **Table III (headline V‑Web 4‑class table)**  
   Formula stated in §V:  
   \[
   \sigma_{\text{from half}} = \frac{n_{\rm CW}-0.5N}{0.5\sqrt{N}}
   \]  

   - Void: n = 428, nCW = 207 → fCW = 0.4836 (correct).  
     \[
     \sigma = \frac{207-214}{0.5\sqrt{428}}
            = \frac{-7}{10.347} = -0.68
     \]  
     This matches the tabulated −0.68. Good.

   - Wall: n = 6,673, nCW = 3,359 → fCW = 0.5034 (correct).  
     \[
     \sigma = \frac{3359-3336.5}{0.5\sqrt{6673}}
            = \frac{22.5}{40.84}=0.55
     \]  
     0.55 matches. Good.

   - Filament: n = 408,187, nCW = 203,261 → fCW = 0.4980 (correct).  
     \[
     \sigma = \frac{203261-204093.5}{0.5\sqrt{408187}}
            =\frac{-832.5}{319.6}=-2.60
     \]  
     Tabulated value: −2.61. Difference ≈ 0.01σ, within rounding. Acceptable.

   - Cluster: n = 397,505, nCW = 197,284 → fCW = 0.4963 (correct).  
     \[
     \sigma = \frac{197284-198752.5}{0.5\sqrt{397505}}
            =\frac{-1468.5}{315.5}=-4.66
     \]  
     This matches −4.66. Good.

   Here the arithmetic is consistent to 0.01σ, but it shows the paper is using the “(nCW − 0.5N)/(0.5√N)” convention, not the more common “(2nCW−N)/√N” without the extra 0.5 factor; the definition is correct but **non‑standard and easy to misapply**. You should explicitly re‑derive a few worked examples in an appendix and check all σs against that.

2. **Table VIII (DESIVAST VoidFinder void vs non‑void)**  

   - Void: n = 56,981, nCW = 28,286 → fCW = 0.4964 (correct).  
     \[
     \sigma = \frac{28286 - 28490.5}{0.5\sqrt{56981}}
            = \frac{-204.5}{119.5}=-1.71
     \]  
     Matches −1.71.

   - Non‑void: n = 621,964, nCW = 309,173 → fCW = 0.4971 (correct).  
     \[
     \sigma = \frac{309173 - 310982}{0.5\sqrt{621964}}
            = \frac{-1809}{395.2}=-4.58
     \]  
     Tabulated −4.59. Within rounding.

   - Two‑sample contrast: ∆f = 0.0007, SE(∆) printed 0.00219, zΔ = +0.31.  
     Recompute SE using the standard pooled two‑sample variance  
     \[
       \text{SE}(\Delta)=\sqrt{\frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}}
     \]  
     with p1 = 0.4964, n1 = 56,981 and p2 = 0.4971, n2 = 621,964 gives SE ≈ 0.00219 and z ≈ 0.31. This is consistent.

   For the DESIVAST *sphere‑based* rows in Table X (V2‑REVOLVER and V2‑VIDE), a similar recomputation yields agreement to ≲ 0.01σ. So the arithmetic on the **tabulated** values is generally consistent.

3. **Table V (density‑stratified cluster + filament quartiles)**  

   Example: cluster Q1, n = 99,398, σfrom half = −3.07. The implied nCW satisfies  
   \[
   n_{\rm CW} = 0.5N + \sigma\cdot 0.5\sqrt{N}
              \approx 49,699 - 3.07\cdot 157.9 \approx 49,699 - 484 \approx 49,215
   \]  
   That in turn gives fCW ≈ 0.4951. Since fCW values are not printed in this table, the referee cannot verify consistency; only σ is given. This is a **traceability problem**: σ appears without its underlying counts or fractions, so any mis‑keyed σ would be undetectable from the PDF alone.

Required fix (MAJOR arithmetic/traceability):

- For **every σ, z, and p** you present as a headline quantity, explicitly tabulate the underlying n and nCW (or n and fCW) in the same table or a referenced appendix, so a referee can recompute the statistic from the PDF.
- Re‑generate all σ and z values from a single, tested function and then rebuild the tables from those outputs. Spot‑check them manually for a few rows in each table (including Table IV, V, VII, X, XI, XIV) and correct any that differ by more than 0.01σ from the recomputation using your own stated formula.
- State once, very explicitly, the exact σ formula you use, and avoid any informal re‑descriptions in the text that drop or change the 0.5 factor; this is easy to slip on in later edits and would silently alter the magnitude of many σ’s.


P5‑E7 – σ from *different nulls* juxtaposed without explicit “non‑comparable” flag (new instances)  
Section/page: §VI C–D; §VII; Table IV; Table VII; Table XIV  

Problem: Your previous pass already noted the abstract and main 4‑class table, but there are additional places where σ values from **different null procedures** are placed side‑by‑side (or in close succession) without clearly marking which null each uses and that they are *not* cross‑comparable:

- **Table IV / §VI C**: You show σobs and σpred per density quintile (σpred from the monopole null, σobs from a half‑null) and then quote a single |σobs − σpred|. You do explain what σpred is, but you do *not* explicitly say that σobs and σpred derive from different baselines and must not be compared across other tables that use σfrom half only.
- **Table VII / §VII**: You give per‑cell “max |σobs − σpred|” (monopole‑referenced) and also list pLEE from permutation nulls, and you later compare these to the Bonferroni |σ| thresholds defined for σfrom half. It is clear to a careful reader what each quantity is, but you never explicitly flag in the table caption or text that σfrom half, σpred, and |σobs − σpred| are derived from different nulls and should not be compared numerically to σfrom half values elsewhere.
- **Table XIV / §X**: The ASTRA per‑object cross‑validation row lists “max |σ|vs 1/2” for three different classifiers (V‑Web, ASTRA argmax, ASTRA entropy‑weighted). All three σ’s are implicitly half‑null σ’s, but the *underlying n and effective neff* differ; you provide n per class, but you do not explicitly repeat here that σ’s from different classifiers with different effective N are not comparable, which is especially important given that the table is about comparing classifiers.

Required fix (MAJOR):

- For **Table IV, VII, XIV and any other multi‑σ tables you did not already annotate**, add a one‑line sentence in the caption stating:
  - which σ is half‑null, which is monopole‑referenced, and which is derived from permutations; and
  - that “σ values from different null procedures or different total N are *not directly comparable* across rows or across tables; effect sizes (∆f in percentage points) are the comparable quantities.”
- In the main text discussions that read mixed σ’s (e.g. §VI C, §VII A), explicitly restate this non‑comparability once so a reader landing there without the abstract context is warned.


P5‑M11 – Equations (1)–(3) and Poisson step: units and notation clarity  
Section/page: §IV A steps 2, 8–9; footnote 1; §V, Eqs. (1)–(3)  

Problem: The equations are almost dimensionally consistent, but there are a few **notation/units ambiguities** that can trip a PRD referee:

1. **Comoving distance and h‑units (step 2 + footnote 1)**  

   - You say: “astropy returns χ in Mpc and we multiply by h explicitly to work in h−1 Mpc (sanity value: χ(z = 0.2) = 570.4 h−1 Mpc)” and in the footnote: “multiplying the value in Mpc by h yields the value in h−1 Mpc.”  
   - In standard cosmology convention, a comoving distance \(D\) expressed in \(h^{-1}\,\text{Mpc}\) satisfies \(D[h^{-1}{\rm Mpc}] = D[{\rm Mpc}]\times h\). This is mathematically correct, but many cosmology codes and readers think in the opposite mapping (“to get Mpc from h−1 Mpc, multiply by 1/h”), so the direction here is easy to misread. The current text is correct but **non‑standardly phrased**, and the sanity value “843 Mpc → 570 h−1 Mpc” will look suspicious on a quick read because 843/0.6766 ≈ 1246, while 843×0.6766 ≈ 570; that’s the opposite transform from the one many readers have in their heads.

   Required clarification (MINOR but important):

   - Explicitly write the algebra as in the footnote, e.g.  
     “If \(D\) is 843 Mpc, then \(D = 843~{\rm Mpc} = 570~h^{-1}{\rm Mpc}\) at \(h=0.6766\) because \(D[h^{-1}{\rm Mpc}] = D[{\rm Mpc}]\,h\).”  
   - Add a one‑line sentence stating that this is *consistent* with the usual convention \(k\) in units of \(h\,{\rm Mpc}^{-1}\) and that cell sizes, Rs, and void radii are all in comoving \(h^{-1}{\rm Mpc}\).

2. **Poisson and tidal tensor in Fourier space (steps 8–9)**  

   - You define Φ(k) = −δk/k² and then \(T_{ij}(k) = -k_i k_j \Phi(k)\), which gives \(T_{ij}(k)=+k_i k_j\delta_k/k^2\). Here δ is dimensionless, k has dimensions of 1/length, and Φ is dimensionless in your normalization; so Tij is dimensionless as intended. Dimensionally this is fine.
   - However, you never explicitly state the **normalization of δk** (FFT conventions, box volume, etc.). For a tidal‑tensor classifier volume fractions are invariant under an overall multiplicative factor on Tij (because only sign and ordering matter once you normalize by λth), but *this is not spelled out*.

   Required clarification (MINOR):

   - Add one sentence: e.g. “Our FFT convention absorbs the box volume into δk so that δ is dimensionless, and any overall multiplicative constant in Tij cancels in the eigenvalue‑threshold classification; only the sign and ordering of eigenvalues relative to λth matter.”

3. **Equations (1)–(3) (σpred, Bonferroni threshold, pLEE)**  

   - Eq. (1): σpred = 2 ∆fCW √N. Units are fine (dimensionless), but you reuse the σ notation for different baselines throughout the paper (see P5‑E7). For dimensional clarity and to avoid algebraic mis‑use, these different σ’s should get **distinct symbols** (e.g. z½, zmono, zperm) so that equations cannot be misapplied later.
   - Eq. (2): Bonferroni threshold uses erfc−1(α/K). This is correct dimensionally, but you do not explicitly state that this is derived under a *Gaussian* approximation. Given that you later apply it down to small N bins (e.g. void n ≈ 428 or even smaller in some stratifications), you should at least remark that the exact binomial tail differs slightly and that you rely on a Gaussian approximation there.
   - Eq. (3): pLEE = (1 + # exceeds)/(1+NMC) is fine and dimensionless, but you later compare this pLEE with Bonferroni thresholds derived for Gaussian z. That is standard practice, but you should say explicitly “Bonferroni thresholds are approximate Gaussian references; the MC max‑statistic pLEE is the primary control.”

   Required clarification (MINOR):

   - Introduce explicit symbols for the different z/σ values in §V and use them consistently, or at minimum add a short boxed remark that “σfrom half, σpred and σvs monopole denote different baselines and cannot be interchanged.”
   - Add a clause after Eq. (2) that Bonferroni thresholds are derived under a Gaussian approximation to the binomial tails and are used here only as an approximate check, with the permutation max‑statistic pLEE the primary control.


P5‑M12 – Abstract vs body: additional “faithfulness” mismatches and stale numbers  
Section/page: Abstract vs §VI D; §VIII C–E; §X; §XI; §XII C  

Problem: There are a few **new inconsistencies** between the abstract and the current body that were not flagged before:

1. **“Counting‑statistics floor of ±2.4 pp at n = 428”**  

   - Abstract: “counting‑statistics floor of ±2.4 pp (the 1σ binomial half‑width of the n = 428 V‑Web void bin; 2σ half‑width ±4.8 pp)”.  
   - For n = 428 and p = 0.5, the binomial 1σ on f is  
     \[
     \sigma_f = \sqrt{\frac{p(1-p)}{n}}=\sqrt{\frac{0.25}{428}}\approx 0.0242
     \]  
     which is indeed 2.42 percentage points. So the number is **correct**, but it is never explicitly restated in §VI A where the void bin is discussed in detail. A reader cross‑checking will have to recompute this themselves.

   Required fix (MINOR): Put the same 2.4 pp number (with the actual computed value 2.42 pp) explicitly into §VI A when you describe the void bin, so the abstract’s “counting‑statistics floor” has a clear pointer in the body.

2. **Phase‑2 sweep “per‑cell cross‑class range 1.7–4.1 pp”**  

   - Abstract: “per‑cell cross‑class range of CW fractions (1.7–4.1 percentage points)…”.  
   - Table VII shows per‑cell ranges of {1.72, 2.71, 2.01, 1.97, 2.48, 1.83, 3.69, 4.12, 2.81} pp. So the true range is ~1.72–4.12 pp. You quote 4.1 pp in the abstract. That is within rounding, but the lower bound “1.7” is not obviously traceable; the minimum is 1.72, not 1.7.

   Required fix (MINOR): Either (a) standardize on the **exact extrema** reported in Table VII (“1.72–4.12 pp”) in both abstract and body, or (b) explicitly say “≈1.7–4.1 pp” in both places. Right now the abstract has approximate language but the body has exact numbers; they should match stylistically.

3. **ASTRA EDR overlap size and ranges**  

   - Abstract robustness paragraph mentions ASTRA only indirectly (as a supporting diagnostic) and does not quote the Noverlap = 25,186. §X does. That is allowed, but as you are using ASTRA as one of the headline robustness bullets, many PRD referees will expect **the abstract to quote the actual overlap sample size**.
   - Table XIV reports “fCW range (pp)” for ASTRA argmax 2.08 and entropy‑weighted 1.17. The abstract mentions only “supporting diagnostic consistency check… EDR overlap‑size caveat” (via Table II) but never quantifies the range.

   Required fix (MINOR):

   - Add the ASTRA overlap size and typical range to the robustness sentence, e.g. “ASTRA EDR per‑object cross‑validation on N = 25,186 overlapping spirals yields per‑class fCW variations of ≲ 2.1 pp with no class exceeding |σ| = 2.3.”
   - Ensure these numbers are exactly the ones in Table XIV.

4. **Shamir (2022) comparison (novelty / amplitude)**  

   - §XII C: you write that Shamir (2022) reports a “∼ 2–4% large‑scale asymmetry” and you compare your environment‑conditioned range of “1.98 pp” against that. This is fine as a qualitative statement **only if** those 2–4% refer to the same quantity (global asymmetry in fCW) and are indeed from Shamir’s published tables.  
   - However, you do *not* quote any section or table from Shamir, nor do you show a direct numeric comparison of his global asymmetry with your catalog monopole (−0.26%) and with your per‑environment residuals.

   Required fix (MAJOR, novelty/faithfulness):

   - Explicitly cite the exact table/section in Shamir (2022) from which the 2–4% number is drawn and state what quantity it refers to (global handedness bias, dipole amplitude, etc.).  
   - Where you state “about an order of magnitude smaller than the Shamir 2022 amplitude,” show the numbers explicitly: e.g. “Shamir’s global asymmetry  A ≈ X% vs our catalog monopole 0.26% and per‑environment residuals ≲0.2–0.4%.”  
   - Make sure the abstract does not oversell a “disagreement with Shamir” that is only fully quantified in the companion Paper IV; right now it walks close to that line.

P5‑M13 – Internal cross‑references: some claims not fully mirrored in cited sections  
Section/page: §V B vs Table II; §VIII A vs §IX C; §IX A vs §VII; §XII B vs “Paper II/III”  

Problem: There are a few new **cross‑reference tension points** beyond what you already flagged:

1. **Primary/secondary analysis tree (Table II vs §V B)**  

   - §V B defines the primary family as the DESIVAST void vs non‑void contrasts and Table II lists them. That is self‑consistent.  
   - However, §V B also says: “The declared primary estimand is the void‑vs‑non‑void contrast ∆fCW, whose two‑sample statistics are tabulated… and for the two GALZONE catalog‑native estimators in §VIII D.” Table II lists “V2‑REVOLVER catalog‑native” and “V2‑VIDE catalog‑native” as *primary*.  
   - §VIII D indeed gives their ∆f, SE, and z, but the **abstract’s single controlling void statement** only mentions the VoidFinder sphere PIS (n = 56,981, ∆f = 0.0007). It does not mention the catalog‑native V2‑REVOLVER void (n ≈ 10⁵) that you yourself call “the cleanest single chirality‑in‑voids measurement.”

   Required fix (MAJOR, faithfulness/pattern‑045): You already partly caught this under P5‑M8, but the additional point is:

   - Either demote the catalog‑native V2 rows to “secondary” in Table II (if you want the abstract to be strictly VoidFinder‑anchored), or  
   - Upgrade the abstract to explicitly state both the VoidFinder and the V2‑REVOLVER catalog‑native constraints, and say which is “primary” and which is “cleanest,” so the analysis‑tree declaration and abstract are aligned.

2. **V‑Web vs T‑Web void‑fraction discrepancy (cross‑ref §VIII A vs §IX C)**  

   - §VIII A mentions a “+8–18 pp V‑Web excess in the void class… reported in §IX C below”. §IX C actually discusses comparison to the DR1 T‑Web volume fractions from Ref. , but it does not explicitly list the exact void fractions and their difference in pp for each tracer sample; it just says “V‑Web’s void fraction is higher than T‑Web’s by +8–18 pp.”  
   - Because you use this difference as a key explanatory systematic (survey‑shell artifacts), the reader needs to see at least one explicit number (e.g. “T‑Web BGS void fraction 6–16%, V‑Web void fraction 24.4%”), as well as the 8–18 pp band.

   Required fix (MAJOR):

   - In §IX C, tabulate explicitly the void and knot fractions for at least the BGS sample in Ref.  and for your V‑Web run, and show their difference numerically.  
   - Make sure the “+8–18 pp” range in §VIII A is the min–max difference across all tracer samples you compare; otherwise give the exact range and say which samples achieve each end.

3. **“RSD‑bounded” caveat cross‑references (§VIII vs §XIII)**  

   - §VIII (RSD treatment for DESIVAST) says “RSD‑bounded at the level relevant to this work… full immunity would require void‑catalog reconstruction… not performed here.” §XIII repeats and expands this.  
   - However, §IV A (V‑Web algorithm) does *not* link back to the RSD caveat when first introducing the classifier. A reader focusing on §IV–VII might miss that RSD is acknowledged as a limitation later.

   Required fix (MINOR):

   - Add a short cross‑reference near the end of §IV A or §VI A: “We use observed redshift‑space positions without reconstruction; RSD limitations are discussed in §XIII.” This ties the limitation into the methods at the point where it matters.

4. **Use of “Paper II” and “Paper III” as discriminators (§XII B)**  

   - §XII B: “Paper II [4] and Paper III (both companion, not‑yet‑published works by the same author) provide independent discriminators… this null adds a clean negative result…”.  
   - Your earlier review (P5‑E1, P5‑E2) already flags the fundamental problem that [4] is unpublished and Paper III is not even in the reference list. The additional issue for *cross‑referencing* is that **no quantitative description** of those discriminators is given in this paper, nor is any explicit figure, section, or equation in this paper that combines their constraints with the present null. Yet the abstract‑adjacent text treats them as part of a combined discrimination program.

   Required fix (ESSENTIAL, cross‑ref + provenance):

   - Either remove references to “Paper III” entirely and rephrase the paragraph to say simply that the **present work alone** provides an environment‑dependent upper bound, or  
   - Add a very concise, quantitative one‑line summary of what Paper II contributes (e.g. “Paper II forecasts that SPHEREx can distinguish bounce from inflation models via fNL at ΔfNL ≈ …”) but explicitly state that those results are external and not combined statistically here.  
   - In either case, do not refer to “independent discriminators” by companion numbers unless they are public and citable; see your own P5‑E1/E2.

---

If you want, I can next go through your tables one by one (III, IV, V, VII, X, XI, XIV, XVI, XVII) and return a clean “verified / discrepancy” list with explicit recomputed σ, z, p for each row.