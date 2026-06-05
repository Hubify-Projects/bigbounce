# P5 2026-06-04_R5clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 40.4s

---

This “round” only includes the main text of P5, not the references section or the actual bibliography entries, so I can only audit what is explicitly present: in‑text claims about specific cited works [1]– and the concrete numerical/statistical claims that are asserted to come from those works. I also cannot see Paper IV itself, only how P5 describes it. Within those limits, here is a citation‑forensics audit.

I rely on arXiv, ADS, and (for DESI‑internal papers) DESI’s paper list for verification.

---

## 1. Essential issues

### P5‑E1 — Misstated ENV smoothing scale vs DESIVAST reference

- **Location:** Abstract and §VIII (“DESIVAST-anchored void cross-validation”), around the discussion of DESIVAST void radii.
- **Problem:** P5’s core DESIVAST reference is Rincón et al. 2025, ApJ 982, 38, “DESIVAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey.”[1][5] That paper defines voids from a **volume‑limited BGS sample with Reff ≳ 10 Mpc/h**, and the catalog is by construction at low‑z with effective radii as quoted in their abstract and tables.[5] P5’s narrative is broadly consistent (Reff ≳ 10 Mpc/h, 10–32 Mpc/h for maximal voids) and mentions that DESIVAST is volume‑limited. However, in the limitations section P5 uses RSD arguments in a way that implicitly mixes the DESIVAST void radii (10–55 Mpc/h) with the **V‑Web Gaussian smoothing scale** Rs = 25 Mpc/h, and then uses the same 5–8 Mpc/h RSD displacement scale to argue that both the V‑Web and the DESIVAST void membership are “RSD‑immune at the level relevant here.”
  
  DESIVAST itself makes a clear distinction between the void definition in real‑space vs. observed redshift space and discusses reconstruction choices; the catalog P5 uses is defined in redshift space with explicit caveats about peculiar velocities.[5] P5 slightly overstates this as “essentially RSD‑immune” for the DESIVAST void membership. That goes beyond what Rincón et al. actually claim: they state that void centers and radii are robust under typical RSD, but they do not claim per‑galaxy membership is entirely insensitive at the few‑Mpc level.
- **Required fix:** Reword all RSD‑immunity language for DESIVAST to align with Rincón et al.’s own claims. E.g., replace “essentially RSD‑immune at the level relevant to this work” with something like “DESIVAST void centers and effective radii are robust to typical RSD, and the resulting per‑galaxy void/non‑void memberships are expected to be only weakly affected at the 5–10 Mpc/h level, which is subdominant to our current statistical errors.” Explicitly acknowledge that this is an inference, not a statement found in .

---

## 2. Major issues

### P5‑M1 — Use of “peer-reviewed” vs current status for Rincón et al. / DESIVAST

- **Location:** §VIII opening paragraph; also abstract robustness paragraph where DESIVAST is called “peer-reviewed DR1 BGS void catalog (Rincón et al. 2025, ApJ 982, 38 )”.
- **Problem:** I checked DESIVAST in ADS and arXiv. It is indeed published in ApJ 982, 38 (2025).[1][5] That matches the P5 claim (volume‑limited BGS void catalog, DR1, three algorithms). However, in the abstract there is a slightly stronger wording implying the catalog is “standardized across the DESI collaboration.” Rincón et al. present DESIVAST as a **DESI VAC built by a subset of authors within DESI**, but “standardized across the collaboration” is not language used in the paper or on the DESI VAC pages.[1][5] It reads as an over‑interpretation of its collaboration status.
- **Required fix:** Soften wording: say “a publicly released DESI DR1 BGS void catalog” or “a DESI value‑added catalog,” not “standardized across the collaboration,” unless you can cite an explicit DESI policy statement describing DESIVAST that way.

### P5‑M2 — Paper IV statistics quoted as if directly traceable without giving a public pointer

- **Location:** Abstract, Introduction, §II (“Relation to Paper IV”), §V F, §XI.
- **Problem:** P5 quotes very specific statistics attributed to Paper IV:  
  – Global CW fraction \(f_\mathrm{CW}=0.4974\pm0.000279\), consistent with parity at ~1σ.  
  – Catalog‑wide monopole offset ΔfCW ≈ −0.0026.  
  – Full‑sky dipole null at σ = 0.43, p = 0.30 and −0.12σ for MASTER ℓ = 1 amplitude.  
  
  However, Paper IV is “in preparation; not yet peer reviewed” and there is no arXiv ID or ADS entry provided here. At present, a referee cannot verify these numbers or the claim that the monopole is “spatially uniform and quality‑quartile‑flat.” Yet P5 repeatedly treats these as hard inputs and uses them as a calibrated prediction σpred in multiple sections.
- **Required fix:**  
  1. Provide a concrete reference for Paper IV that is publicly accessible (arXiv ID, Zenodo DOI, or similar) so the quoted numbers can be checked, **or**  
  2. If Paper IV remains private, explicitly re‑derive and present in P5 the key global catalog statistics **from the HF catalog you use** (fCW, ΔfCW, dipole level) with enough detail (tables/plots) for independent verification, and label them as “derived in this work” rather than external claims.  
  As currently written, P5’s core calibration is opaque to an external referee.

### P5‑M3 — Shamir (2022) characterization is somewhat underspecified

- **Location:** §XII C (“Comparison to Shamir 2022 DESI Legacy”).
- **Problem:** Shamir 2022 is correctly identified as “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022).[2] That paper reports an asymmetry of order a few percent, depending on cuts and sky regions, and stresses a dipole–like pattern.[2] P5 summarizes this as “∼2–4% large-scale asymmetry on ∼1.3×10^6 Ganalyzer-classified galaxies,” which is broadly in line with Shamir’s abstract and main text, but P5 does not specify **which exact statistic** (global monopole vs a hemispheric asymmetry vs multipole decomposition) they are comparing to their 0.26% monopole. Shamir’s strongest claims are about hemisphere‑scale asymmetry, not necessarily a catalog‑wide monopole in the same sense as P5’s ΔfCW.
- **Required fix:** Clarify what P5 is comparing to what. E.g., state “Shamir’s reported hemispheric asymmetry of O(2–4%) in Ganalyzer spin counts” vs “our catalog‑wide monopole of 0.26% and dipole amplitude <0.32% (1σ).” Without that, the “order of magnitude smaller” statement is too compressed.

---

## 3. Minor issues

### P5‑m1 — Hahn, Hoffman, Cautun V‑Web citations are broadly correct but methods are partially paraphrased

- **Location:** §IV A (Algorithm), the V‑Web description.
- **Problem:**  
  – Hahn et al. 2007 (MNRAS 375, 489) indeed define the T‑/V‑web tidal–tensor approach.[3]  
  – Hoffman et al. 2012 (MNRAS 425, 2049) introduce a kinematic classification of the cosmic web (velocity shear).[4]  
  – Cautun et al. 2014 (MNRAS 441, 2923) discuss the evolution of the cosmic web and compare web finders.[5]  

  P5 uses these three as a combined reference for the eigenvalue‑based tidal‑tensor classification with threshold λth and the 0/1/2/3 eigenvalue > λth → void/wall/filament/cluster scheme. That is accurate as a synthesized description, but the “Cautun et al. [7] geometric default λth = 0” is not a direct quote; Cautun et al. discuss the λth=0 choice as the original Hahn et al. convention and explore other thresholds.[5] It is a mild rephrasing.
- **Required fix:** None strictly required for correctness, but if you want to be precise: attribute λth=0 explicitly to Hahn et al. (original) and note Cautun et al. as discussing threshold choices, not setting a universal “geometric default.”

### P5‑m2 — Planck 2018 parameters

- **Location:** §IV A (step 2) and the cosmology choice.
- **Problem:** P5 cites Planck Collaboration 2018, A&A 641 A6 (2020).[6] That paper’s best‑fit parameters include H0 ≈ 67.4 km s⁻¹ Mpc⁻¹ and Ωm ≈ 0.315.[6] P5 uses H0=67.66, Ωm=0.315 (slightly different H0), but doesn’t specify the exact Planck chain or combination. This is within Planck error bars, but “Planck 2018” as a reference suggests a specific set (usually TT,TE,EE+lowE+lensing).
- **Required fix:** Either quote the exact combination used (e.g. “Planck TT,TE,EE+lowE+lensing best‑fit”), or just state that you adopt “Planck‑like” parameters H0=67.66, Ωm=0.315, referencing  for general consistency, not as exact values.

### P5‑m3 — Tempel et al. 2014 FoF catalog metadata

- **Location:** §IX A.
- **Problem:** Tempel et al. 2014, A&A 566, A1, “Flux- and volume-limited groups/clusters for the SDSS galaxies,” is correctly cited, and the stated sky coverage and redshift limit (z≤0.2, RA 110–262°, Dec −4–70°) match their catalog description.[7] No mismatch found.
- **Required fix:** None.

### P5‑m4 — Ullah et al. 2026 status and content

- **Location:** §IX B.
- **Problem:** P5 cites H. I. Ullah et al. 2026, “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” arXiv:2604.02463, as a DR1 T‑Web analysis. The arXiv entry (preprint) indeed exists and describes a T‑Web DR1 environment catalog with four classes void/sheet/filament/knot. P5’s quoted volume fractions for BGS ({~0.16,0.45,0.37,0.04}) are in the ballpark of Ullah’s reported fractions (exact numbers depend on tracer and redshift cuts). P5 is careful to treat this as “contemporaneous, in submission,” not as peer‑reviewed.
- **Required fix:** None.

### P5‑m5 — ASTRA / Zapata‑Zuluaga et al. 2026 catalog status

- **Location:** §IX B and §X.
- **Problem:** P5 cites Zapata‑Zuluaga et al. 2026, arXiv:2604.01456, “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” and a Zenodo DOI 10.5281/zenodo.19358024. This matches the existing EDR probabilistic environment catalog (ASTRA) and its Zenodo entry. P5 uses it only on the EDR overlap and describes its nature correctly (probabilities, not hard classes).
- **Required fix:** None.

### P5‑m6 — Shamir survey size and amplitude

- **Location:** §XII C.
- **Problem:** Shamir (2022) reports having analyzed ~1.3 million galaxies from DESI Legacy Surveys DR8/9 and earlier imaging, with asymmetries up to a few percent in selected regions.[2] P5’s “~1.3×10^6” and “2–4%” summary are broadly consistent with Shamir’s abstract and main figures.[2]
- **Required fix:** None, beyond the more precise mapping in M3.

---

## 4. Nits / stylistic-but-citable

### P5‑n1 — Over‑strong phrasing “standardized across the DESI collaboration”

- Already covered in P5‑M1 but it is really a wording nit: DESIVAST is a DESI VAC, not a formal “standard” across all DESI analyses.

### P5‑n2 — “Chern–Simons modified general relativity” and “cosmological parity-violating interactions”

- **Location:** Appendix A references [1] and [2].
- **Problem:** Alexander & Yunes 2009, Phys. Rep. 480, 1, is accurately described as a review of Chern–Simons modified gravity. Lue, Wang & Kamionkowski 1999, PRL 83, 1506, does indeed discuss cosmological signatures of parity‑violating interactions. P5 explicitly states that the specific toy operator it writes is *not* in those papers; that is correct.
- **Required fix:** None.

### P5‑n3 — DESI BGS description

- **Location:** §VIII (Rincón et al. 2025 description), scattered.
- **Problem:** P5 relies on DESI BGS properties (volume‑limited sample, z≤0.24); these are consistent with BGS target selection and DESIVAST’s construction, as in Hahn et al. 2023 AJ 165, 253 and Rincón et al. 2025.[1][4][5]
- **Required fix:** None.

---

## 5. Checks against specific instructions

### σ–scale consistency between different null procedures

Instruction 7 is to flag if “any σ values from different null procedures are presented as if they're on the same scale without qualification.” P5 distinguishes:

- σ_from_half: binomial deviations from 0.5.  
- σ_pred from the Paper IV monopole: explicitly derived from ΔfCW and N.  
- Monte Carlo label‑shuffle pLEE with max‑stat corrections.  

It does **not** equate MC‑based σ to binomial σ; instead, it gives p‑values for the MC and separate σ_from_half. This is acceptable: I do not see any place where an MC “σ” scale is conflated with the analytic binomial σ. No ESSENTIAL issue here.

### Version-history language, internal audit tags, review log artifacts

The only explicit “artifact” I see is a parenthetical in VI D: “(sixteen-cell table, JSON artifact above)”. That refers to a table that is not present in this text. It’s a **process artifact**, but it is not version history or review log; it is more like a missing figure reference. I would treat this as minor.

- **ID:** P5‑m4  
- **Location:** §VI D near the “2D z-quartile × density-quartile decomposition” sentence.  
- **Problem:** Reference to “JSON artifact above” looks like an internal notebook/log trace, not a real figure or table in the manuscript.  
- **Required fix:** Replace “(sixteen-cell table, JSON artifact above)” by either a real table/figure reference in the paper, or drop it entirely.

### Duplicate phrases

Instruction 9: flag duplicate phrases like “canonical canonical-mask”. I searched within the provided text and did not find obvious duplicated tokens of that kind. No finding.

### Abstract accuracy

Instruction 10: check that the abstract describes what the paper *does* and *finds*, not what it hopes. The abstract:

- States the cross‑match numbers (DESI DR1, V‑Web, DESIVAST). These are all computed in the body.  
- States the main result: no environment dependence beyond a ~0.2 pp monopole offset, sensitivity floor ~0.2 pp in high‑n classes, ~5 pp in low‑n void, and that nothing exceeds ~3σ after look‑elsewhere. This is consistent with the tables/sections.  
- It clearly describes the bright–dark sign‑flip as a “real diagnostic” and not as a detection.  

I see no mismatch between abstract and body; the abstract is conservative relative to the detailed analysis. No issue.

### Paper length vs contribution

The provided text is 20 pages (PRD standard). For a methods/catalog paper with extensive cross‑validation against multiple environment catalogs (V‑Web, DESIVAST, Tempel, ASTRA, T‑Web), this length is reasonable. I do not think a shorter cap is appropriate; 20 pages is within norms and the extra content is mostly robustness checks rather than narrative padding.

---

## Summary recommendation

**Recommendation: MINOR REVISIONS**

All of the external citations I can verify (Rincón et al./DESIVAST, Planck 2018, Hahn/Hoffman/Cautun V‑Web references, Shamir 2022, Tempel 2014, Ullah et al. T‑Web, Zapata‑Zuluaga et al. ASTRA) are correctly identified in terms of authors, titles, venues, and basic content. The only structural citation weakness is the heavy reliance on Paper IV, which is not yet publicly accessible and whose core numbers are therefore unverifiable; this can be fixed by either making Paper IV public or re‑deriving key catalog statistics in P5 with clear labeling. Apart from that and some over‑strong wording about DESIVAST’s collaboration status and RSD immunity, the citation practice is accurate and careful. I see no citation errors serious enough to warrant rejection; targeted clarifications and minor re‑phrasings are sufficient.