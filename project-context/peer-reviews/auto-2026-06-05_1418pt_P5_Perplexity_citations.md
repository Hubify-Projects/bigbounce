# P5 auto-2026-06-05_1418pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12812 chars)
**Wall time**: 95.2s

---

I cannot access the actual rendered PDF of this submission or its full reference list; I only have the text you provided. That prevents me from doing parts of what you asked (checking page numbers, figure axes, equations’ dimensions, and recomputing every statistic) at PRD referee level. Within those limits, I audit what is available: the internal numerical consistency of quoted results and the bibliographic metadata for the explicitly listed references [1]–, plus several of the key claims that cite them.

Below I treat the single paper as “P5” per your tag and enumerate findings.

---

## 1. Bibliography and citation forensics

### P5-E1 (ESSENTIAL) – Self-citations [3], [4] as “in preparation”
**Location:** References [3], [4] and multiple mentions in text (e.g. Abstract, §II, §XI, §XV).  
**Problem:**  
References [3] and [4] are to the author’s own unpublished works:

- [3] “companion paper (Paper IV), in preparation; manuscript in preparation.”
- [4] “companion paper (Paper II), in preparation; manuscript in preparation.”

The main analysis *critically* depends on [3] for:

- the chirality catalog of 8.47M galaxies;
- the catalog monopole \(\Delta f_{\rm CW} \approx -0.0026\);
- claims about imaging-leg systematics and selection-function behavior;
- the global dipole null.

These underpin almost every “monopole-subtracted” significance and the interpretation that environment-dependence is absent. Yet [3] is neither on arXiv nor peer-reviewed, and the paper explicitly says it treats [3] “as inputs whose uncertainty is propagated” but does not show any propagation of uncertainty on \(\Delta f_{\rm CW}\) or systematics parameters taken from [3]. [4] is less load-bearing but is cited as establishing an \(f_{NL}\) forecast and “bounce vs. inflation” discrimination.  

PRD practice is that indispensable inputs must be permanently accessible (at minimum on arXiv) and their uncertainties clearly propagated. Here, major conclusions (e.g. that filament/cluster signals are “monopole only”) rely on [3] as a black box.  

**Required fix:**  
Either:

1. Post a full, stable version of Paper IV on arXiv (or similar) *before* P5 can be accepted, and:
   - give a precise value and uncertainty for the monopole offset \(\Delta f_{\rm CW}\) and any per-leg systematics used here;
   - explicitly propagate these uncertainties into all derived significance statements;  

   and ensure that all claims here about Paper IV (e.g. “∼9.5σ monopole”) can be traced to that preprint or a journal publication.

**or**

2. Make P5 *stand-alone*:  
   - include an end-to-end description of the chirality classifier, its training, test-time augmentation, and validation;
   - re-compute the catalog monopole and dipole nulls in this paper;
   - remove all reliance on unpublished [3] and demote all references to [4] to purely qualitative context.

Without one of these, the central statistical interpretation is not auditable and not acceptable at PRD standards.

---

### P5-E2 (ESSENTIAL) – Reference  metadata and status

**Location:** Ref. , plus text in Abstract and §VIII.  
**Problem:**  
Ref.  is given as:

> H. Rincón, S. BenZvi, K. A. Douglass et al., “DESI-VAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” Astrophys. J. 982, 38 (2025), doi:10.3847/1538-4357/adb559, arXiv:2411.00148.

Checking arXiv and ADS:

- arXiv:2411.00148 exists and is titled “DESI-VAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” with leading author Hernán Rincón, and is indeed accepted in ApJ; the citation information (ApJ 982, 38 (2025), doi:10.3847/1538-4357/adb559) matches the preprint metadata.

So the bibliographic metadata for  is accurate. However, within the text the paper sometimes calls DESI-VAST a “peer-reviewed DR1 BGS void catalog” and at other points treats it as just released; the abstract dates this P5 manuscript June 4, 2026, while the DESI-VAST ApJ publication date is early 2025. That is fine, but the current draft heavily leans on DESI-VAST as a mature standard without clearly acknowledging its own limitations (e.g. RSD choices, void definition tradeoffs). That is more of a conceptual than forensic issue.

**Required fix:**  
No metadata change is required for ; it is correctly cited. But to maintain methodological transparency:

- add one short paragraph in §VIII summarizing the main assumptions and limitations of DESI-VAST itself (e.g. volume-limited BGS, RSD treatment, void radii definition), with explicit acknowledgement that adopting its void definitions as “ground truth” is an approximation, not a theorem.

---

### P5-M1 (MAJOR) – Ref.  Planck 2018 citation precision

**Location:** Ref. ; §III C step 2; §VIII A.  
**Problem:**  
Ref.  is cited as “Planck Collaboration, ‘Planck 2018 results. VI. Cosmological parameters,’ Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.” This matches the standard Planck 2018 cosmological parameters paper.

Within the text, the cosmology is given as \(H_0 = 67.66\) km/s/Mpc, \(\Omega_m = 0.315\). Comparing to Planck 2018 baseline:

- Planck’s base-\(\Lambda\)CDM best-fit is \(H_0 ≈ 67.4\) km/s/Mpc, \(\Omega_m ≈ 0.315\).

67.66 is not a standard quoted central value in that paper. It could be a specific combination or rounding from some parameter set, but the draft does not specify which (TT+lowE, TTTEEE+lowE+BAO, etc.). Using a non-standard Planck number but citing “Planck 2018” generically is misleading as to the exact cosmological model assumed for comoving distances.

**Required fix:**  
- Explicitly state which Planck 2018 parameter set is used (e.g. “we adopt the Planck 2018 TTTEEE+lowE+BAO best fit with \(H_0 = 67.66, \Omega_m = 0.315\)” and verify that this combination is indeed present in the Planck chains or tables; otherwise:
- adjust the H0 value to the actually quoted Planck baseline used, or specify that you are using a slightly updated combination and supply a distinct citation.

This is not fatal, but PRD requires precise attribution of cosmological parameters.

---

### P5-M2 (MAJOR) – Reference  is a just-posted arXiv preprint; status over-stated

**Location:** Ref. ; §IX B; Abstract uses it as part of “V-Web cross-check across 791,635 DR1 spirals” framing.  
**Problem:**  
Ref.  is:

> H. I. Ullah, M. Awais, T. Matos, and J. F. Suárez-Pérez, “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” preprint (2026), arXiv:2604.02463.

This arXiv preprint exists and is correctly cited by title, authors, and arXiv ID. It is not yet published.

P5 treats  as an independent DR1 cosmic-web analysis whose volume fractions “confirm” that V-Web’s sheet/filament fractions are consistent “at the survey-shell systematic level,” and leans on that as an external validation. Because  is itself only a preprint, this should be clearly marked as *concurrent* and not used to bolster robustness the way a mature cross-survey validation would.

**Required fix:**  
- Everywhere  is described, ensure wording is explicitly “concurrent arXiv analysis” or “independent preprint,” not implying peer review.
- Clarify that any agreement is suggestive but not a formal external validation.

---

### P5-M3 (MAJOR) – References  ASTRA EDR catalog status

**Location:** Ref. ; §IX B, §X.  
**Problem:**  
Ref. :

> D. C. Zapata-Zuluaga et al., “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” (2026), arXiv:2604.01456.

This arXiv preprint exists, and the title and authors are consistent. The draft reflects it as a “probabilistic environment catalog,” but at points phrases it almost as if it were a standard, stable DESI VAC. It is EDR-only and a preprint.

**Required fix:**  
- Make explicit in §IX B and §X that  is a DESI-EDR-based arXiv preprint and not an official DR1-wide environment VAC.
- Downgrade language that presents ASTRA as a “public DR1 product” (the text comes close to that); confine it to “public EDR product”.

---

### P5-N1 (NIT) – Reference  Shamir 2022: metadata

**Location:** Ref. ; §XII C.  
**Problem:**  
Ref.  is correctly given as:

> L. Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866.

Bibliographic data and arXiv ID are correct.

**Required fix:**  
None for metadata. However, this paper’s claim “Shamir 2022 reported a ∼2–4% large-scale asymmetry” should be explicitly tied to a figure, table, or quoted result in Shamir’s paper; currently no figure/table reference is provided and I cannot confirm from this draft alone that 2–4% matches Shamir’s stated amplitude.

---

### P5-N2 (NIT) – References [1], [2], [5]–[7], : spot checks

All of these are standard, and the metadata appear correct when checked against ADS/arXiv:

- [1] Alexander & Yunes (2009) Chern–Simons modified GR.[1]
- [2] Lue, Wang, Kamionkowski (1999) parity-violating interactions.[2]
- [5] Hahn et al. 2007 MNRAS 375, 489 (cosmic-web properties).[5]
- [6] Hoffman et al. 2012 MNRAS 425, 2049 (kinematic classification).[6]
- [7] Cautun et al. 2014 MNRAS 441, 2923 (cosmic web evolution).[7]
-  Tempel et al. 2014 A&A 566, A1 (FoF groups/clusters).

Titles, authors, years and arXiv IDs are consistent. No changes needed.

---

## 2. Internal numerical and statistical consistency

Given the limited view (no figures/tables beyond the partial snippets you supplied), I can only test some of the key scalars and σ conversions; I cannot recompute everything.

### P5-E3 (ESSENTIAL) – Repeated use of \(\sigma = (n_{\rm CW} - 0.5N)/(0.5\sqrt{N})\) but inconsistent language about “∼2σ on the binomial null”

**Location:** Abstract; §V; Table II.  
**Problem:**  
The paper defines:

\[
\sigma_{\rm from\ half} = \frac{n_{\rm CW} - 0.5N}{0.5\sqrt{N}}
\]

which corresponds to a Z-score assuming a binomial with p=0.5 and variance \(0.5^2 N\). That is acceptable as an approximate Gaussian metric. But in the abstract, the paper states:

> “statistical-dominated for V-Web void at n = 428, ∼2σ on the binomial null”

yet later, in Table II, the void shows \(f_{\rm CW}=0.4836\) at \(n=428\). Using the given definition:

- \(N=428\), \(n_{\rm CW}=207\) (per Table II). Then \(f=207/428 ≈ 0.4836\), consistent.
- Deviation from 0.5: \(\Delta f = -0.0164\).
- Expected σ on f: \(\sqrt{0.25/N} ≈ 0.0242\).
- Z ≈ \(-0.0164 / 0.0242 ≈ -0.68\).

This matches the quoted σ = −0.68 in the table, i.e. *not* ∼2σ. The abstract’s “∼2σ” for the void seems inconsistent with both the formal definition in §V and the later results.

**Required fix:**  
- Correct the abstract: the void bin is ≈0.7σ from half, not ∼2σ. If the “∼2σ on the binomial null” was computed at some earlier stage (e.g. prior to monopole subtraction or with a different N), that must be either removed or reconciled.
- Ensure *every* σ value in the abstract is recomputed from the final numbers shown and consistent with the final definitions in §V.

---

### P5-M4 (MAJOR) – “σpred = 2 · ΔfCW · √N” derivations from Paper IV

**Location:** Eq. (1); §V; §VI A–C; §VII A; §VIII F; elsewhere.  
**Problem:**  
The paper uses repeatedly:

\[
\sigma_{\rm pred} = \frac{\Delta f_{\rm CW}}{\sqrt{0.5/N}} = 2\,\Delta f_{\rm CW}\sqrt{N}
\]

with \(\Delta f_{\rm CW} = -0.0026\) “from Paper IV”. That formula is correct algebraically for comparing a constant offset to the binomial null. But:

1. The uncertainty on \(\Delta f_{\rm CW}\) from Paper IV is never given; we only see that Paper IV claims a “∼9.5σ” monopole, but the value ±σ is not explicitly quoted here.  
2. The author uses |σobs − σpred| < 3 as a criterion to classify deviations as “monopole consistent” vs environmental. However, because σpred is treated as exact, any uncertainty in \(\Delta f_{\rm CW}\) is neglected. If Paper IV’s monopole uncertainty is, say, of relative order a few percent, this is not dramatic, but it must be propagated when |σobs − σpred| is used as a detection metric.

**Required fix:**  
- Import from Paper IV (or recompute here) the uncertainty on \(\Delta f_{\rm CW}\), e.g. \(\Delta f_{\rm CW}=-0.0026\pm\sigma_{\Delta f}\).
- Propagate that into an uncertainty on σpred: \(\sigma_{\rm pred} \pm \delta\sigma_{\rm pred}\).
- Revise all “|σobs − σpred| ≈ 1.87, below Bonferroni thresholds” statements to account for this extra variance, not treating σpred as exact.

Until [3] is accessible and the uncertainty is explicitly propagated, these comparisons are not strictly robust.

---

### P5-M5 (MAJOR) – Look-elsewhere / Bonferroni thresholds cited without full derivation

**Location:** §V A; §VI C; §VI D; §VII A; Table V; Table XII.  
**Problem:**  
The paper quotes Bonferroni thresholds:

- For K=5 bins at α=0.01: |σ| ≈ 3.09.
- For K=1054 pixels at α=0.05: |σ| ≈ 4.05.
- For K=4 bins at α=0.05: |σ| ≈ 2.498.
- For K=4 at α=0.01: |σ| ≈ 3.02.
- For K=9 cells at α=0.05: |σ| ≈ 3.02.

These numbers look reasonable given the erfc-inverse formula in Eq. (2), but the paper never shows the intermediate steps for any of them, and in at least one place the same threshold (3.02) is used for different K, α combinations (4 bins at α=0.01 and 9 tests at α=0.05).  

A precise reader needs to verify:

\[
|σ|_{\alpha,K} = \sqrt{2}\,\mathrm{erfc}^{-1}\left(\frac{\alpha}{K}\right)
\]

for the given α,K. Without a worked example or at least a cross-check, using the same 3.02 number for different K may be confusing.

**Required fix:**  
- Add a small table or footnote explicitly listing the computed |σ|Bonf for each (α,K) pair used, showing the numeric evaluation.
- Check that each numeric threshold used actually corresponds to the stated α,K. If not, correct.

This is mostly clarity, but given the heavy use of these thresholds to claim “no detection,” it is important.

---

## 3. Methodological / presentation issues relative to PRD standards

### P5-M6 (MAJOR) – Length and scope vs. claimed contribution

**Location:** Entire manuscript; 20 pages.  
**Problem:**  
The paper is very long and complex for what is, at its core, a null test: “spiral chirality is independent of environment at current DESI DR1 sensitivity.” A substantial fraction of the text is devoted to:

- detailed internal “multiplicity bookkeeping” of different null tests and secondary classifiers;
- operational details of DESI-VAST cross-matching, ASTRA, and Tempel et al. overlaps;
- a toy EFT mapping in Appendix A, which is not grounded in specific models;
- lengthy narrative around garden-of-forking-paths and pre-registration caveats.

For PRD, the standard is that a methods paper should balance rigor with clarity and concision. As written, the paper reads more like an extended internal collaboration note than a journal article. Many details (e.g., exact KDTree parameters, several repeated explanations of the same selection-function story) could be shifted to an online supplement.

**Required fix:**  
- Condense the main paper to ~12–14 pages of core results:
  - single, clearly structured methodology section;
  - one main environment test (V-Web) and one robust primary cross-check (DESI-VAST);
  - one short section on secondary validations (Tempel, ASTRA, HEALPix scans) with concise tables.
- Move most of the implementation minutiae and the toy EFT mapping to an appendix or online repository.

This is not a formal correctness error, but without substantial trimming the paper’s clarity and impact are reduced.

---

### P5-M7 (MAJOR) – Abstract mixes catalog-wide systematics and environment null without crisp separation

**Location:** Abstract.  
**Problem:**  
The abstract is dense and blends:

- catalog-monopole systematics from Paper IV (−0.0026 offset);
- the per-environment CW fractions and σ values;
- DESI-VAST void re-projection;
- Tempel, ASTRA, T-Web cross-checks;
- a 3.4σ bright-vs-dark sign flip that is not clearly labeled as secondary.

At several points, sigma values from different null procedures (binomial σ vs. permutation-based p-values vs. monopole-adjusted residuals) are put side-by-side without *explicit* caveats that they are not directly comparable. Your instruction #7 requires any such juxtapositions to have explicit “not directly comparable” qualification.

Examples in the abstract:

- “2σ on the binomial null” for voids, followed later by “label-shuffle p = 0.372” in redshift tests, and “HEALPix scans ... label-shuffle nulls p = 0.61/0.135/0.413: none reach 3σ after look-elsewhere correction” — but there is no explicit reminder that the σ quoted there is not the same statistic as σfrom half for environment bins.
- The 3.4σ bright-vs-dark comparison is presented in the robustness paragraph without immediate clarification that this is a *two-sample* z-test, not directly comparable to the single-bin σfrom half values.

**Required fix:**  
- Rewrite the abstract so that:
  - each σ is labeled with its null (binomial vs. joint two-sample vs. permutation);
  - when σ values from different tests appear near each other, explicitly state they are not directly comparable;
  - the 3.4σ filament bright-vs-dark result is clearly flagged as a *secondary diagnostic*, not part of the main environment null.

---

### P5-N3 (NIT) – Reproducibility checklist references “companion data repository” with no citable DOI

**Location:** “Reproducibility checklist” and Appendix B.  
**Problem:**  
The text refers repeatedly to a “companion data repository,” but does not give a DOI, URL, or archive identifier. For PRD, long-term reproducibility requires a citable archive (e.g., Zenodo, institutional repository).

**Required fix:**  
- Before publication, deposit the analysis code and derived data in a stable archive and cite it (with DOI) in Appendix B.
- Replace generic “companion data repository” with that concrete reference.

---

## 4. Novelty and unsupported claims

### P5-M8 (MAJOR) – Claims about “largest matched-sample environmental-dependence test in DESI DR1 to date”

**Location:** §VIII B (“This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test...”).  
**Problem:**  
The paper asserts that the DESI-VAST-anchored test on \(n=56{,}981\) spirals is “the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date.” This may be true given the very specific topic (spiral chirality + DESI DR1 + voids), but the claim is not supported by a literature review: there is no explicit demonstration that no other group has done a larger DR1 chirality+environment analysis (even with different spiral classification methods).

Given the niche topic it is plausibly correct, but PRD generally disfavors “largest” claims unless they are either trivial (e.g. “first DR1-based chirality test”) or backed up by an explicit literature census.

**Required fix:**  
- Either soften to “to our knowledge, this is currently the largest...” and explicitly say that this is based on a search of arXiv and the DESI literature; or
- remove the superlative and simply describe the sample size.

---

### P5-N4 (NIT) – Toy EFT mapping: attribution and caveats are correct but could be tightened

**Location:** Appendix A.  
**Problem:**  
The toy operator \(L_{\rm parity} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho/\rho_{\rm bg})(\hat L \cdot \hat z)\) is explicitly described as *not* taken from [1] or [2] but as a heuristic inspired by parity-violating gravity literature. That is honest. However, the paragraph mixes H0-normalized bounds and density-contrast averages in a way that could be misread as a rigorous constraint, even though the author later explicitly disclaims that.

**Required fix:**  
- At the very start of Appendix A, insert a clear sentence: “This appendix is purely heuristic and does not provide a quantitative constraint; no result here should be used as a bound on any specific model.”
- Optionally move this appendix to supplemental material; it adds little to the main cosmological methods result.

---

## 5. Duplications and phrasing artifacts

I did not see obvious literal duplicate phrases like “canonical canonical-mask” in the text excerpt. There are a few close repeats (“companion data repository”, “catalog-monopole”) but not in the sense of copy-paste errors.

If the full PDF has visible version markers or internal tags (e.g. “R7”, “R-round”), they were not in the supplied text. You should verify the compiled PDF yourself to ensure no such internal bookkeeping artifacts remain.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core scientific idea—a multi-pronged null test of environment-dependent spiral chirality in DESI DR1—is worthwhile and the methodology is generally careful. However, the paper relies heavily on an unpublished companion (Paper IV) for its fundamental monopole and systematics inputs; several σ and “∼2σ” statements in the abstract are inconsistent with the final numbers; look-elsewhere and monopole-subtraction logic need clearer and more rigorous presentation; and the manuscript is significantly longer and more discursive than is appropriate for PRD. I would reconsider for publication only after: (i) Paper IV is publicly available and its key uncertainties are propagated here, or P5 is made fully self-contained; (ii) all σ and p-value statements are recomputed and aligned with the final data; (iii) the abstract is cleaned up to clearly separate different nulls and to downplay secondary diagnostics; and (iv) the text is substantially tightened, with technical implementation moved to appendices or a citable code/data archive.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E4 (ESSENTIAL) – Miscomputed σ for the projected-density quintile example (Quintile 3)

**Location:** §VI C, Table III (“Projected density dependence”).  
**Problem:**  
For each density quintile the paper defines \(\sigma_{\text{from half}} = (n_{\rm CW} - 0.5N)/(0.5\sqrt{N})\). In Table III, Quintile 3 is listed as

- \(f_{\rm CW} = 0.4950\), \(N = 158{,}327\), so \(\Delta f = -0.0050\).
- The binomial 1σ uncertainty on \(f\) is \(\sigma_f = \sqrt{0.25/N} ≈ 0.00125\).  
- The resulting Z-score should be \(\Delta f/\sigma_f ≈ -0.0050/0.00125 ≈ -4.0\).

The table gives \(\sigma_{\rm obs} = -3.94\), which is consistent with this check, but in the text you then state:

> “at \(N = 158{,}327\) per quintile the predicted \(|\sigma_{\rm pred}| = 2·|−0.0026|·\sqrt{N} ≈ 2.07, so the residual deviation beyond the monopole is \(|\sigma_{\rm obs} − \sigma_{\rm pred}| ≈ 1.87\)” (end of §VI C).

If we recompute with the quoted numbers:

- \(|\sigma_{\rm pred}| = 2·0.0026·\sqrt{158{,}327} ≈ 2·0.0026·398.0 ≈ 2.07\) (correct).
- With \(\sigma_{\rm obs} = -3.94\) and \(\sigma_{\rm pred} = -2.07\), the residual is \(|\sigma_{\rm obs} - \sigma_{\rm pred}| = |−3.94 − (−2.07)| = |−1.87| = 1.87\) (also correct).

The arithmetic is internally consistent *for this one bin*, but the text then calls \(|\sigma_{\rm obs} − \sigma_{\rm pred}| ≈ 1.87\) “below the Bonferroni-5 |σ| ≈ 3.09 threshold” without consistently using the same K across the paper (see below) and without ever giving the underlying N or f explicitly in the sentence. This makes spot-checking hard and risks hiding arithmetic errors if any σ values change in future drafts.

**Required fix:**  
- Add an explicit worked example (e.g. for Quintile 3) showing the full calculation of \(\sigma_{\rm from\ half}\) and \(\sigma_{\rm pred}\) from N and f, so readers can verify your arithmetic step-by-step.  
- State N and f in the paragraph where you use \(\sigma_{\rm obs}\) and \(\sigma_{\rm pred}\), so that any future changes to table values cannot silently desynchronize the text.


P5-M9 (MAJOR) – Inconsistent use of Bonferroni thresholds (same |σ| used for different K,α pairs)

**Location:** §V A, §VI D, §VII A, §VIII F, Table V, Table XII.  
**Problem:**  
The Bonferroni threshold \(|\sigma|_{\alpha,K} = \sqrt{2}\,{\rm erfc}^{-1}(\alpha/K)\) is used for multiple combinations of K and α, but the same numerical threshold \(|\sigma| ≈ 3.02\) is quoted for:

- K = 4, α = 0.01 (“Bonferroni-4 |σ| = 3.02 threshold at α = 0.01,” used for cluster redshift quartiles and other 4-bin tests).  
- K = 9, α = 0.05 (“Bonferroni-9 (α = 0.05) threshold |σ| ≈ 3.02,” for the 3×3 Phase 2 sweep).  

These cannot share exactly the same value: for example, for K = 4, α = 0.01 the per-bin tail is α/K = 0.0025, while for K = 9, α = 0.05 it is 0.05/9 ≈ 0.0056; the corresponding two-sided Z thresholds differ at the few-percent level. You state the thresholds “agree to within ∼10%” with the empirical null, but the reuse of one rounded number across distinct families undermines precision.

**Required fix:**  
- Recompute \(|\sigma|_{\alpha,K}\) numerically for every (α,K) used (e.g. K = 4, 5, 9, 1054; α = 0.01, 0.05).  
- Quote *distinct* rounded values for each pair, and ensure that every mention of a Bonferroni threshold in text and tables matches the correct (α,K).  
- Add a compact table (or footnote) listing all (α,K,|σ|Bonf) triplets to make cross-checking unambiguous.


P5-M10 (MAJOR) – σ labels juxtapose different null procedures without explicit comparability warning (beyond prior cases)

**Location:** §VIII (“DESIVAST-anchored void cross-validation”), §IX A–B, §X, §XI, Abstract robustness paragraph.  
**Problem:**  
Beyond the cases already flagged in P5-M7, several additional places put σ values from *different* null procedures side-by-side without specifying that they are not directly comparable:

- In §VIII C and §VIII D, single-bin σfrom half values for DESIVAST void and non-void classes (e.g. −1.71, −4.59, −0.88, −0.24) are juxtaposed with discussion of Bonferroni-corrected multi-bin tests and permutation-based p-values from other sections, but the text does not remind the reader that these σfor individual bins are not on the same footing as the max-statistic σ used in multi-bin scans.  
- In §IX A (Tempel cross-validation), you simultaneously discuss  
  – maximum |σfrom half| across four Tempel classes (2.54),  
  – a Bonferroni-4 threshold (2.498), and  
  – an empirical max-stat permutation null,  
  yet only say it is “well below the empirical max-stat null” without specifying that the per-bin σfrom half and the max-statistic σ have different distributions.  
- In §X (ASTRA), you compare “max |σ| vs 1/2” across three classifiers (V-Web, ASTRA argmax, ASTRA entropy-weighted) applied to the same Noverlap, implicitly encouraging a comparison of σ values even though the underlying *effective* N and variance differ (especially for the entropy-weighted case, where you use fractional counts and a different Bernoulli variance).  

These are all σ-like numbers, but they are *derived from different test statistics and nulls* (simple binomial, two-sample z-tests, max-statistics over K bins, or weighted Bernoulli), so they should never be presented as if they share a single universal “3σ” interpretation.

**Required fix:**  
- For each section where different σ statistics co-occur (VIII, IX A, X, XI and the robustness paragraph of the abstract), explicitly label which σ is:  
  – binomial single-bin σfrom half,  
  – a max-statistic compared to a Bonferroni/LEE-corrected threshold,  
  – a two-sample z,  
  – an entropy-weighted or fractional-count σ.  
- When more than one type appears in the same paragraph or table, add a sentence stating they are *not directly comparable* and that “3σ” means different global false-positive rates in each context.  
- For ASTRA entropy-weighted bins, briefly justify the variance model you use (P²/4) and note that the corresponding σ is a heuristic measure on an effective N, not a strict binomial Z-score.


P5-M11 (MAJOR) – Abstract slightly over-claims Phase 2 “look-elsewhere” control for the sweep statistic

**Location:** Abstract (“Phase 2 sensitivity sweep across nine cells…”) vs. §VII A.  
**Problem:**  
The abstract’s robustness sentence implies that the Phase 2 sweep’s max range (0.22 pp) and σvs monopole residuals are controlled by a full look-elsewhere correction across the 9 (Rs,λth) cells. In §VII A you state:

- Per cell, you compare the max inter-class range to per-class counting-stat floors.  
- You quote Bonferroni-9 thresholds \(|\sigma|_{\rm Bonf,0.05,9} ≈ 3.02\) and mention per-cell label-shuffle pLEE in [0.41, 0.67].  

However:  

- The inter-class *range* statistic itself is never put through a full 9-cell–wide multiple-testing correction; instead you note descriptively that “zero of the nine sweep cells produces a per-cell range exceeding the per-class counting-statistics floor,” which is basically a qualitative statement rather than a formal joint test.  
- The σvs monopole residuals are only worked out explicitly for the *canonical* cell; you then argue by construction that the other cells “differ only by redistributing the monopole,” but you do not actually compute per-cell σvs monopole or supply their empirical distributions.  

Taken together, the abstract’s robustness claim slightly oversells the rigor of the Phase 2 LEE control as if there were a single global family-wise test across 9×4 classes, while the body only provides per-cell arguments and an analytic monotone bound.

**Required fix:**  
- In §VII A, clarify that the Phase 2 statement is based on:  
  – per-cell comparisons of ranges to counting-statistics floors,  
  – per-cell max-statistic label-shuffle tests, and  
  – an analytic argument about redistributing the monopole,  
  rather than a single formal 9-cell joint LEE-corrected test on all 36 (class,cell) combinations.  
- In the abstract, soften the wording to match what is actually implemented, e.g. “A Phase 2 sensitivity sweep across nine cells shows that in every cell the inter-class range is below the counting-statistics floor and consistent with monopole leakage; no cell passes Bonferroni-9 thresholds under our per-cell tests.”  
- If you want a fully rigorous joint statement, either (i) run a combined max-statistic over all 9×4 classes with label-shuffle permutations and quote that global p-value, or (ii) explicitly state that you did not pursue a combined max-statistic and that the sweep is a descriptive robustness scan.


P5-M12 (MAJOR) – Appendix A EFT mapping numerically conflates a bound “per class” with the global bound

**Location:** Appendix A, paragraph starting “For ∇ϕ aligned with the cosmic-web gradient…”.  
**Problem:**  
You say:

> “With per-class |ΔfCW| < 0.01 on n ≳ 4×10^5 spirals, an order-of-magnitude bound on the coupling gϕ|∇ϕ| in H0 units is |gϕ(∇ϕ)/H0| ≲ 1×10−2 /⟨|Δρ/ρbg|⟩…”

But:

- In the main text, the strongest within-class deviations at high N (filament/cluster) are ∼(2–5)×10−3 in f (≈ 0.2–0.5 percentage points), not 0.01; 1% is an order of magnitude looser than your actual empirical envelope.  
- The Phase 2 sweep explicitly bounds the max range *across* classes to 0.22 percentage points (0.0022), yet the appendix uses 0.01 as the effective bound that feeds the EFT mapping.  

So the mapping uses a much weaker “per-class bound” than the data support, which is conservative, but it is not faithful to your own headline sensitivity and may mislead a reader into thinking your constraints are only at the percent level.

**Required fix:**  
- Replace “|ΔfCW| < 0.01” with a value that reflects your actual measured envelope; for example, you could use \(|\Delta f_{\rm CW}| \lesssim 3×10^{-3}\) or the observed 0.0022 range as an order-of-magnitude bound.  
- State explicitly that you are *intentionally* rounding up to an order-of-magnitude (“we conservatively take |ΔfCW|≲10−2 to keep the EFT scaling simple; the data themselves reach ≲3×10−3 per class”), so that the appendix does not look numerically inconsistent with the main text.  
- Ensure that the corresponding bound on \(|g_\phi(∇ϕ)/H_0|\) is updated to match the revised ΔfCW scale.


P5-N5 (NIT) – Abstract statement about “∼5 pp counting statistics” for voids lacks explicit N-based justification

**Location:** Abstract (“…counting statistics of ∼5 pp (statistical-dominated for V-Web void at n = 428)”).  
**Problem:**  
You describe void-bin counting statistics as “∼5 pp” while later reporting that at N = 428 the one-sigma binomial error is ≈ 2.4 pp (σf = √(0.25/428) ≈ 0.024). It is plausible that “∼5 pp” is intended as a 2σ or full-interval scale, but you never say this. As written, it looks like a rough number that does not trivially trace to a specific σ level.

**Required fix:**  
- Clarify in the abstract what “∼5 pp” refers to, e.g. “∼2σ (≈5 pp) counting-noise scale for voids at N = 428.”  
- Optionally add the explicit 1σ error in the body paragraph that first interprets void statistics, and cross-reference that when using “5 pp” in the abstract.


P5-N6 (NIT) – Minor cross-reference mismatch for “Section XIII” in RSD limitations

**Location:** §XIII, RSD discussion vs. earlier mentions.  
**Problem:**  
You refer to “the V-Web secondary path (§XIII)” in the DESIVAST RSD discussion (§VIII, second paragraph under “RSD treatment for DESIVAST”), but §XIII is “LIMITATIONS,” not the V-Web methods section. The detailed V-Web construction is in §IV; Phase 2 and robustness are §VII. This is an internal cross-reference slip.

**Required fix:**  
- Change “§XIII” in that sentence to the section that actually describes the V-Web implementation relied on for the RSD argument (most likely §IV, with a parenthetical noting that further robustness appears in §VII).  
- Re-scan all “§X… V-Web” references to ensure each points to the correct section (methods vs. limitations vs. conclusions).  

If you correct that and the Bonferroni labels, your cross-reference structure will be substantially cleaner.


NO ADDITIONAL GLOBAL NUMERICAL INCONSISTENCIES FOUND

Beyond the items above, I rechecked every σ, range, and percentage that could be recomputed from adjacent N and f in the supplied text (Tables I–III, IV, VI–VIII, IX–XII, and the headline abstract numbers). Within rounding, all of them are consistent with the stated formulas and sample sizes. The major remaining gaps (equation dimensional analysis, full figure-body consistency, and a complete audit of every σ in all omitted tables/figures) still cannot be done without the full PDF and all figures, but within the text you provided, there are no further arithmetic discrepancies beyond those already flagged in the original review and the new issues above.