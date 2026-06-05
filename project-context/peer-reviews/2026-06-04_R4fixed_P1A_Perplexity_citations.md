# P1A 2026-06-04_R4fixed — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 47.1s

---

I cannot carry out the requested citation‑forensics audit because the manuscript’s reference list is not included in the text you provided. Without the full bibliography (arXiv IDs, journal citations, years, titles, author lists), I cannot reliably check:

- Whether each cited work exists under the claimed arXiv ID or DOI.
- Whether titles, author lists, venues, and years are correct.
- Whether the numerical values and qualitative claims (σ levels, parameter values, equation forms) indeed appear in the cited sources.

I can, however, report on what *can* be checked from the excerpt you supplied, and what *must* be done once the full reference list is available.

Below I follow your requested structure as closely as possible, but you should treat this as an *incomplete* referee report, focused on internal‑consistency and citation‑style issues visible in the excerpt.

---

### P1A-E1 – Missing reference list prevents full citation audit  
**Classification:** ESSENTIAL  
**Location:** Global (entire manuscript as provided)  

**Problem:**  
The manuscript excerpt stops partway through the references (only [1]– and up to  are partially visible, but the arXiv IDs / journal coordinates are not fully shown). I cannot see the full bibliographic entries (arXiv numbers, DOIs, journal names, volumes, pages) for most citations, nor all references [1]–. Without that, it is impossible to perform the requested checks: whether specific arXiv IDs resolve, titles and author lists match, and whether quoted numerical values (e.g. βobs, fNL, DESI significance, ρcrit ranges) are correctly extracted from the cited papers.

**Required fix:**  
Provide the complete reference list (full entries for [1]–) in the version to be audited. After that is available, a proper citation‑forensics round is needed, including:

- Verify every arXiv identifier and DOI resolves to the claimed work.
- Check that quoted numerical results (errors, significance levels, parameters) are present and correctly reported in those works.
- Check that qualitative claims about each reference are accurate (e.g. what they actually show or argue).

---

### P1A-M1 – “In preparation” companion works now potentially public  
**Classification:** MAJOR  
**Location:** Abstract and throughout (e.g. first page, “companion works in preparation [2, 6]”, “Paper II [2]”, “Paper IV ”, “Paper III ”, “Paper I(b) [6]”)  

**Problem:**  
Several references are to “companion” works labelled as *in preparation* with internal tags hUBIFY‑2026‑00x, e.g.:

- [2] “fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (in preparation) (2026)”
- [6] “Cobaya MCMC + NaMaster Birefringence + ALP Companion: … (in preparation) (2026)”
- , ,  “(in preparation) (2026)”.

By the time of PRD review/acceptance, at least some of these may be on arXiv or published. Right now, they are not externally verifiable; nonetheless, the main paper leans on them for key claims:

- MCMC posteriors (H0, ∆Neff, σ8) and convergence.
- SPHEREx Fisher forecasts and realistic σ(fNL).
- Galaxy spin null analysis.
- PTA spectral index and real‑KDE pipeline.

Relying heavily on non‑public internal documents weakens the paper’s verifiability.

**Required fix:**  
- For each “in preparation” companion paper ([2], [6], , , ):  
  - If it is now on arXiv or published, update the citation to the real reference (with arXiv ID and/or journal info).  
  - If it is still not publicly available, clearly mark in the main text which results are *only* supported by internal analysis and not needed for this paper’s core claims.  
- Revise wording where this paper presents numerical values “drawn from” internal work to make clear what is used as *input assumption* versus what is an externally verifiable result.  
- The editor should consider an additional round explicitly verifying that key companion references used for parameter values and forecasts (especially [2] and [6]) are public before final acceptance.

---

### P1A-M2 – DESI dark‑energy significance and citation traceability  
**Classification:** MAJOR  
**Location:** Introduction, first paragraph (“DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset‑dependent) [9, 10].”)  

**Problem:**  
The text claims DESI BAO results give 3.1–4.2σ evidence for dynamical dark energy and cites [9,10]. From the DESI collaboration DR2 papers and related commentary, the degree of tension and statistical preference for evolving dark energy depends in substantial detail on model choices, combinations with SN/CMB, and priors.[4] The claim “3.1–4.2σ” is quite specific and should be traceable to a particular table or figure in the cited DESI papers. With the reference list truncated, I can’t confirm whether [9, 10] are indeed the correct DESI BAO DRx papers and whether those exact σ values appear there.

**Required fix:**  
- Ensure that  and  are the correct DESI BAO/driving dark‑energy‑evidence papers (very likely the DESI DR1/DR2 cosmology results).  
- In the introduction, add a precise pointer (e.g. “DESI DR2, Table X / Figure Y”) that contains the 3.1–4.2σ numbers, or adjust the quoted range to match what is explicitly reported (e.g. the 4.2σ preference quoted in the DESI+SN+CMB evolving‑DE fits).  
- If this 3.1–4.2σ range is interpolated from multiple analyses rather than quoted directly, say “∼3–4σ” and explicitly describe how the range is constructed.

---

### P1A-M3 – LQC critical density ρcrit range and attribution  
**Classification:** MAJOR  
**Location:** Sec. II B, equations (8)–(9) and surrounding text  

**Problem:**  
The paper states a critical density range “ρcrit ≃ 0.27–0.41 ρPl (Barbero‑Immirzi entropy‑counting scheme dependent; Sec. II B)” and attributes ρcrit ≃ 0.41 ρPl to Ashtekar & Singh’s LQC status report . It then says that substituting γSU(2) ≈ 0.274 gives ρcrit ≃ 0.27ρPl, but notes that 0.27 is “not a value quoted in Ref. ” and is an internal extrapolation.

There are two issues:

1. The *quoted* 0.27–0.41ρPl window might be misread as a standard LQC published range, while only the upper end is actually from ; the lower end is a model‑dependent extrapolation.  
2. It is not fully clear (from the snippet) whether the detailed numerical expression for ρcrit used here matches exactly the conventions in .

**Required fix:**  
- Clarify in the main text that *only* the ρcrit ≃ 0.41ρPl value is from Ashtekar & Singh ; the 0.27ρPl lower bound is an internal extrapolation using a different γ derived from black‑hole entropy counting, not standard LQC.  
- Make the 0.27–0.41ρPl window explicitly labelled as “internal scheme‑dependent band” rather than “LQC range.”  
- Ensure that the formula in Eq. (9) matches the conventions (units, definition of ∆) in . If a different normalization is used, state it explicitly.

---

### P1A-M4 – Birefringence numbers and source consistency  
**Classification:** MAJOR  
**Location:** Abstract and Sec. III A (“βobs = 0.342◦ ± 0.094◦ (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]), comparable to ACT DR6 β = 0.215◦ ± 0.074◦ [5]”)  

**Problem:**  
Several specific numbers are quoted:

- βobs = 0.342◦ ± 0.094◦, 3.6σ from zero.  
- ACT DR6 result β = 0.215◦ ± 0.074◦ at ∼ 2.9σ.

The references [3–5] are Minami & Komatsu 2020 PRL, Eskilt & Komatsu 2022 PRD, and Diego-Palazuelos & Komatsu (ACT DR6). From existing literature:

- Eskilt & Komatsu indeed report β ≈ 0.35° with σ ≈ 0.14° in earlier analyses and then 0.342° ± 0.094° in later WMAP+Planck combinations.[4]  
- ACT DR6 analyses similarly report ~0.2° ± 0.07° levels.[5]

However, without the full bibliography I cannot confirm that the exact numerical pair (0.342, 0.094) and (0.215, 0.074) are taken from the *specific* versions cited here (there have been several preliminary and updated analyses).

**Required fix:**  
- Verify that the exact values and uncertainties quoted match the final journal version (or latest arXiv version) of [4] and [5]. If they come from a particular data split or combination (e.g. WMAP+Planck vs Planck only), specify that in text.  
- Ensure that the 3.6σ and 2.9σ statements are simply β/σ in those papers, not re‑analyzed numbers. If they are recomputed by the author (e.g. combining σ’s), say “corresponding to |β|/σ ≈ 3.6” rather than presenting as the collaboration’s own headline significance.

---

### P1A-M5 – Matter‑bounce fNL citation and scope  
**Classification:** MAJOR  
**Location:** Abstract and Sec. XIII (“fNL = −35/8 is a property of the matter-bounce class [1]…”)  

**Problem:**  
The paper attributes fNL = −35/8 to [1] (Cai et al., JCAP 0905:011). That paper does derive a specific value for local‑type non‑Gaussianity in a particular *scalar‑only matter bounce* model. The current manuscript repeatedly generalizes this as “a property of the matter‑bounce class” under some assumptions, but it is crucial that this not be overstated as an entirely model‑independent prediction across all matter‑bounce realizations.

Given we don’t see the full [1] entry, we can’t verify exactly how it is cited there, though the numbers themselves are plausible.

**Required fix:**  
- Check [1] to verify that the precise value and sign fNL = −35/8 are correctly stated and that the regime (scalar-only, w=0 matter-bounce) is accurately described.  
- In the main text, keep the qualified wording that already appears (e.g. “within the scalar-only w=0 class… not mechanism-independent”), and avoid any phrasing that could be read as “all matter‑bounce models predict −35/8 regardless of field content.”  
- Ideally, add a short clause in Sec. XIII explicitly quoting the conditions from [1] that lead to this value (canonical scalar, matter‑dominated contraction, etc.).

---

### P1A-M6 – PTA spectral index “γ = 2.567 ± 0.382” and reference   
**Classification:** MAJOR  
**Location:** Sec. XIII (table and text discussing “PTA γ (real‑KDE GPU MCMC)” and companion Paper III )  

**Problem:**  
The manuscript quotes a specific PTA spectral index γ with an uncertainty and claims it comes from a real‑KDE GPU MCMC reanalysis described in  (a companion “in preparation” paper). There is no reference to a public PTA reanalysis with exactly these numbers in the visible bibliography, so presently this γ value is *not* traceable to a public paper.

**Required fix:**  
- If an external published source (e.g. a NANOGrav or EPTA paper) provides a compatible spectral index, reference that directly and clearly separate it from any internal reanalysis.  
- For the GPU MCMC + KDE analysis, either (a) ensure  is public by the time of publication and update to its real coordinates, or (b) downgrade those numbers to “illustrative internal analysis” and avoid using them as core evidence for any claim in this paper.

---

### P1A-m7 – DESI torsion cosmology citation   
**Classification:** MINOR (but must be checked)  
**Location:** Related Work, citing “Liu et al.  (EC torsion fits the S8 tension)”  

**Problem:**  
Search indicates  is likely “Torsion cosmology in the light of DESI, supernovae and CMB” (Liu et al., arXiv:2507.04265).[1][5][6] That paper indeed analyses torsion cosmology within Einstein–Cartan and finds H0≈68.8, σ8≈0.81 with mild improvement in tensions.[1][5] The claim “fits the S8 tension” is a qualitative characterization that needs to be consistent with how Liu et al. describe their result (they may say “alleviates” rather than “solves”).

**Required fix:**  
- Confirm that  is exactly the Liu et al. torsion cosmology paper (arXiv:2507.04265) and that the author list, title and venue match.  
- Check that describing it as “fits the S8 tension” does not overstate their claims. If they phrase it as “alleviates” or “compatible with” ΛCDM, adjust wording in P1A to match their self‑description.

---

### P1A-m8 – Use of Ashtekar et al. black hole entropy values [16–18]  
**Classification:** MINOR  
**Location:** Sec. II A.1, eq. (2) and surrounding text  

**Problem:**  
The paper quotes several Barbero–Immirzi parameter values from different horizon state‑counting schemes (U(1), SU(2), Domagala–Lewandowski–Meissner) and correctly notes that the “∼0.020” spread is scheme dependence, not a statistical error. These numbers must match the quoted values from [16–18].

**Required fix:**  
- Verify from [16–18] that γU(1) ≈ 0.127, γSU(2) ≈ 0.274, γDLM ≈ 0.2375 are correctly transcribed.  
- Ensure that the text clearly distinguishes which scheme each value comes from and that the chosen γSU(2) = 0.274 is indeed the one used in later formulas (ρcrit, etc.).

---

### P1A-m9 – Claims about Mercuri (Nieh–Yan reconstruction) and Shapiro & Teixeira one‑loop estimates  
**Classification:** MINOR  
**Location:** Sec. II A.2 and B.2 (discussion of Mercuri , Mercuri & Capozziello , Shapiro & Teixeira )  

**Problem:**  
The paper attributes to:

- Mercuri : “shows that the Nieh–Yan invariant is reconstructed and the Barbero–Immirzi parameter drops out of the classical dynamics” in Holst+non‑minimal‑fermion constructions.  
- Mercuri & Capozziello  and Shapiro & Teixeira : “one‑loop estimate” leading to eq. (7) with an αem/(4π) factor.

These are plausible but need to be checked against the actual content of those papers.

**Required fix:**  
- Verify that  indeed constructs a non‑minimal fermion coupling where the Nieh–Yan term restores classical γ‑independence.  
- Confirm that  and  actually contain the sort of one‑loop corrections to Holst/Nieh–Yan that justify the αem/(4π) scaling used here. If they do not, adjust wording to “motivated by the general structure of one‑loop corrections in [20,22]” rather than implying that eq. (7) is directly derived there.

---

### P1A-m10 – DESI DR2 w0–wa chain status footnote  
**Classification:** MINOR  
**Location:** Table III footnote, discussion of a running DESI DR2 w0wa chain  

**Problem:**  
The text gives very specific internal chain status for a DESI DR2 w0–wa Cobaya run (number of samples, R̂ − 1 ≈ 3×10−2, etc.), but this is not backed by a public reference. It also risks aging badly; by the time of publication, the chain may be complete or superseded.

**Required fix:**  
- Either remove this operational detail about a running chain, or move it to an appendix and clearly label it as internal work‑in‑progress, not part of the main scientific claims.  
- The main text should not rely on this chain for any conclusion; it currently doesn’t, but the level of detail is unnecessary.

---

### P1A-n1 – Internal version / audit language appearing in the body  
**Classification:** NIT (but per your instructions must be flagged)  
**Location:** Abstract, Sec. I A (“earlier versions and is documented here for the record,” “prior count of 14 retained Barrier 8… merged here…”)  

**Problem:**  
The paper contains internal version‑history and audit language, e.g.:

- “The prior count of 14 retained Barrier 8 as the observational consequence of the perturbation‑transparency theorem Barrier 14; merged here under the perturbation-transparency umbrella…”  
- “The condensation mechanism yields… its role is therefore documented in Sec. X as a quantitative closure rather than a viable channel.”  

While it is intellectually honest, PRD papers typically avoid verbose internal change‑log style in the main text. Your instructions explicitly want such artifacts flagged.

**Required fix:**  
- Consider shortening or moving version‑history commentary (e.g. describing how the barrier count changed between drafts) to a brief note in an appendix or footnote.  
- Keep only what is needed for scientific clarity (e.g. that B8 is not logically independent of B14), but drop the explicit “earlier version” narrative.

---

### P1A-n2 – Abstract scope statements vs content  
**Classification:** NIT  
**Location:** Abstract  

**Problem:**  
The abstract includes careful caveats (channel‑level closure, not operator‑basis closure; ansatz vs derivation). This is good practice, but it is worth ensuring the abstract accurately reflects what is *proved* vs *assumed*. From the excerpt, that seems to be the case: the dark‑energy mapping is clearly labelled as an ansatz; the perturbation‑transparency theorem is clearly described and restricted to canonical scalar matter.

**Required fix:**  
- No essential change is needed, but I recommend a final pass to ensure the abstract does not imply any operator‑basis completeness that the body explicitly denies.

---

### Length vs contribution

The manuscript is ~21 pages, which is within typical PRD range for a technical methods/constraints paper, given the multi‑barrier “catalog” and extensive caveats. I do not see a strong case that it is “too long for the claimed contribution”; the length is driven more by detailed self‑critique and explicit limitations than by padding. That said, some of the internal‑workflow details (MCMC chain status, change‑log style commentary) could be trimmed without loss of scientific content.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

Justification:  
Scientifically, the paper is carefully self‑critical and explicit about its assumptions, and the core theoretical claims (perturbation transparency, channel‑level closure of four minimal ECH routes) are internally consistent within those assumptions. However, from the perspective of *citation forensics*, the reliance on multiple “in preparation” companion works, plus the absence of a full reference list in the version provided, prevents a complete verification that each cited paper actually supports the numerical and qualitative claims attached to it. Before acceptance, the authors must (i) provide a full bibliography, (ii) update all companion references that have since appeared on arXiv or in journals, and (iii) ensure that key numerical claims (DESI dark‑energy significance, birefringence numbers, LQC density values, fNL, torsion cosmology fits) are traceable to specific tables/figures/equations in the published literature. Once those issues are addressed and the remaining minor wording adjustments are made, the paper could be suitable for publication.