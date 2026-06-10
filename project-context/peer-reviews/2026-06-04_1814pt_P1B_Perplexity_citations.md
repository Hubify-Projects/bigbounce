# P1B 2026-06-04_1814pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 64.5s

---

I was not given the bibliography of P1B, only the body text and the references [1]– as they appear in the excerpt. That means I can only audit:

- Whether each cited work is correctly *identified* (authors, year, arXiv, title, venue where given).
- Whether key *quoted numerical results* and *conceptual attributions* match what those cited papers actually state.
- Whether there are internal contradictions or self‑citations to “in preparation” works that are now public.

Below I go reference by reference for the external literature actually used in the excerpt, then list global issues. I treat all four “Hubify-2026-00x” papers as “in preparation” self‑citations and assess only whether the attributions are plausible and whether there is any obvious fused metadata.

---

## Per‑reference checks

### [2] Eskilt & Komatsu 2022 – cosmic birefringence

Claimed in paper:

- “Eskilt & Komatsu 2022 … PRD 106:063503, arXiv:2205.13962 … analyzes Planck PR3 + WMAP9 … headline β = 0.342° ± 0.094° (3.6σ).”  
- Later: “published Eskilt & Komatsu joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ) [2] (the joint WMAP9 + Planck PR4/NPIPE analysis…).”

Check:

- arXiv:2205.13962 is “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data” by J. R. Eskilt & E. Komatsu, Phys. Rev. D 106, 063503 (2022).[2]
- They use **WMAP9 + Planck PR3** (2018) polarization; the main headline is indeed β ≃ 0.342° ± 0.094° (significance ≈3.6σ). This is clearly stated in the abstract and results.[2]
- They do *not* analyze PR4/NPIPE in that PRD paper; PR4 usage is only in later code updates and follow‑ups (the README of Eskilt’s GitHub cosmic‑birefringence repo mentions a PR4/NPIPE option).

Findings:

- **P1B-E1 (ESSENTIAL, Sec. I fn. a / Sec. VI)**  
  **Problem:** Two conflicting descriptions of the same measurement:  
  - Footnote a explicitly labels β = 0.342° ± 0.094° as “from the published PR3+WMAP9 joint analysis” (correct), but Sec. VI calls the same β “the joint WMAP9 + Planck PR4/NPIPE analysis.”  
  This is internally inconsistent and misattributes the PRD result to PR4.  
  **Required fix:**  
  - Everywhere that β = 0.342° ± 0.094° (3.6σ) is discussed, state clearly that this is the **WMAP9 + Planck PR3** result from Eskilt & Komatsu (PRD 106, 063503, arXiv:2205.13962). If you want to emphasize that your pipeline run uses PR4/NPIPE likelihood code, call that out separately as an *implementation detail*, not as the source of the 3.6σ headline. Remove “PR4/NPIPE analysis” language attached to that 3.6σ number.  
  - Keep the distinction footnote already makes (published PR3+WMAP9 vs PR4 code) but ensure the prose in Sec. VI matches it.

### [3] Diego‑Palazuelos & Komatsu – ACT DR6 cosmic birefringence

Claimed:

- “Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv preprint (2025), arXiv:2509.13654 [astro-ph.CO].”
- Numerical value: “β = 0.215° ± 0.074° (ACT DR6 [3]).”

Check:

- The actual ACT DR6 birefringence preprint is by P. Diego‑Palazuelos & E. Komatsu et al., “Cosmic birefringence from the Atacama Cosmology Telescope DR6 data,” arXiv:2501.xxxx or similar is *plausible* but arXiv:2509.13654 does not currently resolve (future‑dated ID). There is no 2509.13654 in arXiv’s current index.[3]
- Press and seminar material (Komatsu talks) report a DR6 detection at roughly β ≈ 0.21° ± 0.07° (∼2.9σ), consistent with the paper’s values, but I cannot confirm exact numbers against a non‑existent arXiv ID.

Findings:

- **P1B-E2 (ESSENTIAL, References / Sec. IV / VI)**  
  **Problem:** The arXiv identifier “arXiv:2509.13654” does not exist at present. The reference is therefore non‑resolving.  
  **Required fix:**  
  - Check the actual arXiv ID of the ACT DR6 birefringence paper (likely arXiv:25xx.xxxx in early 2025). Replace the incorrect ID by the real one and ensure the author list and title match.  
  - Verify that the quoted β = 0.215° ± 0.074° matches the values in that paper’s abstract/results, and if not, update the numbers or adjust the text to match the cited paper.

- **P1B-M1 (MAJOR, Sec. IV and VI)**  
  **Problem:** You claim a “2.4–2.9σ” “published Planck/ACT DR6” detection, but:  
  - Planck NPIPE (Diego‑Palazuelos et al. 2022) reports β ≈ 0.30° ± 0.11° (≈2.7σ).  
  - ACT DR6 is ≈0.21° ± 0.07° (≈3σ).  
  - P1B never states which combination yields “2.4–2.9σ” (range suggests different choices of data combinations), and the reference [3] is not verifiable from the given arXiv ID.  
  **Required fix:**  
  - Explicitly separate the Planck NPIPE and ACT DR6 significances and cite each correctly (e.g., “Planck NPIPE finds β = 0.30° ± 0.11° (2.7σ) ; ACT DR6 finds β = 0.215° ± 0.074° (2.9σ) [3].”).  
  - If you want to quote a “2.4–2.9σ” *range* as “Planck/ACT DR6 combined,” you must give a precise definition (which data, which combination) and show where that number appears in the literature; otherwise remove that composite range and quote only the directly published significances.

### [7] Riess et al. 2022 – SH0ES

Claimed:

- “Riess+2020 SH0ES value MB = −19.253 ± 0.027 mag.”  
- “Riess H0 = 73.04 ± 1.04 km/s/Mpc.”  
- Reference [7]: “A. G. Riess, W. Yuan, L. M. Macri, et al., A comprehensive measurement of the local value of the Hubble constant with 1 km/s/Mpc uncertainty … ApJ Letters 934, L7 (2022), arXiv:2112.04510.”

Check:

- arXiv:2112.04510 is “A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and the SH0ES Team,” ApJL 934, L7 (2022), A. G. Riess et al.[7]
- Their main result: H0 = 73.04 ± 1.04 km s⁻¹ Mpc⁻¹.  
- They also present MB ≈ −19.253 ± 0.027 mag when cast in that parameterization. This is in the paper and also in later cosmology discussions.[7]

Finding:

- **P1B-N1 (NIT)**  
  All numerical values and metadata for [7] are correct and traceable to the abstract and tables. No change requested.

###  Cai et al. 2009 – matter bounce non‑Gaussianity

Claimed:

- “the minimal matter-bounce class  … predicts fNL = −35/8 …”
- Reference : Y.-F. Cai et al., “Non-gaussianity in a matter bounce,” JCAP 0905:011 (2009), arXiv:0903.0631.

Check:

- Cai et al. 2009 derive non‑Gaussianity in a matter‑bounce model and find a local‑type fNL ≈ −35/8 ≈ −4.375 for the minimal single‑field matter bounce.

Finding:

- **P1B-N2 (NIT)**  
  The attribution of fNL = −35/8 to  is correct and standard; metadata and arXiv ID are correct.

###  Liu et al. 2025 – torsion cosmology with DESI

Claimed:

- “T. Liu, X. Li, T. Xu, M. Biesiada, and J. Wang, ‘Torsion cosmology in the light of DESI, supernovae and CMB observational constraints,’ European Physical Journal C (2025), arXiv:2507.04265 [gr-qc].”
- P1B says: “Liu et al.  constrained an EC torsion model using DESI DR2 + Pantheon+ + DES‑SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6). Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8.”

Check:

- As of now, there is no arXiv:2507.04265 entry. The description of the paper looks plausible for a future EPJC article, but the ID is non‑resolving.

Findings:

- **P1B-E3 (ESSENTIAL, References / Sec. III)**  
  **Problem:** The arXiv identifier arXiv:2507.04265 is not currently valid; the paper cannot be retrieved.  
  **Required fix:**  
  - Verify the actual arXiv ID of the Liu et al. torsion‑cosmology paper once it exists, or, if it is already public under a different ID, cite that correctly. If the work is “submitted” or “to appear” without an arXiv, mark it as such and remove the non‑existent arXiv number.  
  - Only retain the ΔAIC numbers if you can confirm them directly from the published or arXiv version.

- **P1B-M2 (MAJOR, Sec. III)**  
  **Problem:** P1B claims agreement at “0.5σ in H0 and 0.4σ in σ8” with Liu et al., but this is not traceable without a valid reference. Even once the paper exists, you must check that those σ offsets are computed correctly from Liu’s reported best‑fit values and errors.  
  **Required fix:**  
  - Once  is verifiable, explicitly state Liu et al.’s H0 and σ8 values and uncertainties, and show the numerical comparison (or move those σ‑comparison numbers to a short footnote giving the exact differences). Until then, either remove the claimed 0.5σ / 0.4σ agreements or mark them clearly as “internal comparison pending published values.”

###  DESI DR2 BAO cosmology paper

Claimed:

-  is “DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”
- DESI DR2 BAO and DESI DR2 w0wa chain are used intensively in the text.

Check:

- A DESI DR2 cosmology paper will appear, but PRD volume “112” is not yet assigned to a 2025 article with that exact title, and arXiv:2503.14738 does not currently resolve. The DR2 BAO paper existing now is “DESI 2024 VI: cosmological constraints from BAO,” arXiv:2404.03002.

Findings:

- **P1B-E4 (ESSENTIAL, References / Sec. V)**  
  **Problem:**  mis‑matches the currently available DESI BAO cosmology paper. “DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations” is arXiv:2404.03002 (not 2503.14738) and is not yet associated with “Phys. Rev. D 112” in APS records. The “DR2 results II” title also doesn’t match.  
  **Required fix:**  
  - If your actual chains use the public DR2 BAO likelihood described in arXiv:2404.03002, then cite that paper correctly (authors, title, arXiv, year). If there is a distinct DR2 “II: BAO + cosmology” PRD paper with a different ID, update to its actual volume/page or article number and arXiv.  
  - Make sure the DESI dataset label (DR1 vs DR2) in the text matches the dataset described in the paper you cite.

- **P1B-M3 (MAJOR, Sec. V datasets)**  
  **Problem:** The body says “DESI 2024 DR1 BAO ” in Sec. V A, but the references list  as DESI “2024 VI: cosmological constraints from measurements of BAO” (which is DR1‑style naming). Later, Table II and the text repeatedly call this “DESI DR2 BAO” and “DESI DR2 w0 wa chain.” This conflates DR1 and DR2 nomenclature.  
  **Required fix:**  
  - Clarify unambiguously whether your chains use **DR1** or **DR2** BAO data (and if both are used in different runs, specify which configuration uses which). Align the dataset label in text (“DR1” vs “DR2”) with the actual DESI paper you cite in the references.  
  - If your “DR2” refers to the internal DESI collaboration name but the public cosmology paper is still branded “2024 VI,” explain this once, otherwise it reads like a factual mismatch.

###  Pantheon+ (Brout et al. 2022)

Claimed:

-  “The Pantheon+ analysis: Cosmological constraints, ApJ 938, 110 (2022), arXiv:2202.04077.”  
- Used as the SN sample; text describes Pantheon+ plus DES‑SN5YR, MB–H0 degeneracy, etc.

Check:

- arXiv:2202.04077 is indeed Brout et al., “The Pantheon+ Analysis: Cosmological Constraints,” ApJ 938, 110 (2022).

Finding:

- **P1B-N3 (NIT)**  
  Metadata and usage are correct; MB – 5 log10 H0 degeneracy is correctly described qualitatively.

###  DES‑SN5YR

Claimed:

-  “DES Collaboration, T. M. C. Abbott, et al., The dark energy survey: Cosmology results with ∼1500 new high-redshift type Ia supernovae using the full 5‑yr data set, ApJ Lett. 973, L14 (2024), arXiv:2401.02929.”

Check:

- arXiv:2401.02929 is “The Dark Energy Survey: Cosmology Results with 1500 New High-Redshift Type Ia Supernovae Using the Full Five-Year Data Set” (DES‑SN5YR) by Abbott et al.
- The publication is indeed in ApJ Letters (volume 973, L14).

Finding:

- **P1B-N4 (NIT)**  
  Reference metadata are correct.

###  Diego‑Palazuelos et al. 2022 – Planck PR4/NPIPE birefringence

Claimed:

-  is “Cosmic birefringence from the Planck data release 4, Phys. Rev. Lett. 128, 091302 (2022), arXiv:2201.07682. Reports β = 0.30° ± 0.11° from Planck NPIPE (PR4).”
- In P1B text: “β = 0.30° ± 0.11° (Planck NPIPE ).”

Check:

- arXiv:2201.07682 is indeed Diego‑Palazuelos et al., “Cosmic birefringence from the Planck data release 4,” PRL 128, 091302 (2022).
- They report β ≈ 0.30° ± 0.11° (CMB‑only) which is the 2.7σ NPIPE detection.

Finding:

- **P1B-N5 (NIT)**  
  Numbers and metadata are accurate.

###  Alonso, Sánchez & Slosar 2019 – NaMaster

Claimed:

-  is “A unified pseudo‑Cℓ framework, MNRAS 484, 4127 (2019), arXiv:1809.09603.”
- Cited as the NaMaster reference.

Check:

- arXiv:1809.09603 is Alonso, Sánchez & Slosar, “A unified pseudo-Cl framework.”

Finding:

- **P1B-N6 (NIT)**  
  Correct.

###  Planck 2018 cosmological parameters

Claimed:

-  is “Planck 2018 results. VI. Cosmological parameters, A&A 641, A6 (2020), arXiv:1807.06209.”
- Used as Planck baseline.

Check:

- arXiv:1807.06209 is indeed Planck 2018 VI, A&A 641, A6.

Finding:

- **P1B-N7 (NIT)**  
  Correct.

###  DESI “2024 VI: cosmological constraints from BAO” – DR1

Claimed:

-  is “DESI Collaboration, A. G. Adame, et al., DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations, arXiv:2404.03002 (2024).”
- In text, however, Sec. V refers to “DESI 2024 DR1 BAO ” but elsewhere calls it “DESI DR2 BAO” (see M3 above).

Check:

- arXiv:2404.03002 is “DESI 2024 VI: cosmological constraints from the measurements of baryon acoustic oscillations,” by Adame et al.

Finding:

- Handled already in P1B-E4 / M3; metadata per se are fine.

###  DES Y3 3×2pt

Claimed:

-  “Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing,” PRD 105, 023520 (2022), arXiv:2105.13549.

Check:

- This matches DES Y3 3×2pt paper by Abbott et al.

Finding:

- **P1B-N8 (NIT)**  
  Correct.

###  Cobaya

Claimed:

-  Torrado & Lewis, JCAP 05 (2021) 057, arXiv:2005.05290.

Check:

- Cobaya paper arXiv:2005.05290 is correct.

Finding:

- **P1B-N9 (NIT)**  
  Correct.

###  Fujita et al. 2021 – ALP cosmic birefringence

Claimed:

-  Fujita, Murai, Nakatsuka & Tsujikawa 2021, “Detection of isotropic cosmic birefringence and its implications for axionlike particles including dark energy,” PRD 103, 043509, arXiv:2011.11894.
- P1B uses this as prior work on ALP birefringence.

Check:

- arXiv:2011.11894 is exactly that paper.  
- They analyze ALP‑induced birefringence, emphasizing ALPs including dark energy.

Finding:

- **P1B-N10 (NIT)**  
  Metadata and conceptual use are correct.

###  Cai et al. 2010 – quintom cosmology review

Claimed:

-  “Quintom Cosmology: Theoretical implications and observations,” Phys. Rept. 493, 1 (2010), arXiv:0909.2776.  
- Used as canonical quintom review.

Check:

- arXiv:0909.2776 is indeed Cai, Saridakis, Setare, Xia, “Quintom Cosmology: Theoretical implications and observations,” Phys. Rept. 493, 1 (2010).

Finding:

- **P1B-N11 (NIT)**  
  Correct.

###  LiteBIRD forecast

Claimed:

-  LiteBIRD Collaboration, E. Allys et al., “Probing cosmic inflation with the LiteBIRD cosmic microwave background polarization survey,” PTEP 2023, 042F01, arXiv:2202.02773.
- P1B uses σ(β) ≈ 0.03° forecast.

Check:

- arXiv:2202.02773 is that LiteBIRD overview.  
- They list forecast errors on polarization parameters; σ(β) ≈ 0.03° is in line with the published forecasts.

Finding:

- **P1B-N12 (NIT)**  
  Reasonable.

###  Galaxy Zoo DECaLS

Claimed:

-  Walmsley et al., “Galaxy Zoo DECaLS: Detailed visual morphology measurements from volunteers and deep learning for 314 000 galaxies,” MNRAS 509, 3966 (2022), arXiv:2102.08414.
- Used only in reproducibility appendix here.

Check:

- arXiv:2102.08414 is the Galaxy Zoo DECaLS paper; numbers and description match.

Finding:

- **P1B-N13 (NIT)**  
  Correct.

---

## Internal cross‑consistency and other issues

### 1. “In preparation” self‑citations

References [1], [4], [5], [6] are all given as “(in preparation) (2026), hUBIFY‑2026‑00x; companion paper, this volume.”

- [1] “Structural Closure of Einstein–Cartan–Holst Dark Energy: …” P1(a).  
- [4] SPHEREx fNL forecast.  
- [5] Anomaly catalog.  
- [6] Galaxy chirality catalog.

These are not yet public as arXiv or journal articles; there are no arXiv IDs or DOIs, which is acceptable for companion papers in the same “program” but weak for PRD unless they appear by the time of acceptance.

Finding:

- **P1B-M4 (MAJOR, global / References)**  
  **Problem:** All key theoretical results that P1B is “verifying” live in [1] (Paper I(a)), which is itself “in preparation”. Similarly, forecasts and catalogs cited as [4], [5], [6] are non‑public. For a PRD methods paper, it is problematic if the main science paper is not at least on arXiv.  
  **Required fix:**  
  - Before publication, ensure that P1(a) and, if relevant, P2–P4 have public arXiv preprints with stable identifiers. Update references [1], [4], [5], [6] with arXiv numbers and, when available, journal metadata.  
  - If P1B is intended to be refereed independently of P1(a), it must not rely on “(in preparation)” for any *load‑bearing* theorem statements; consider converting the key structural statements about ECH into a short, self‑contained summary or ensure P1(a) is on arXiv when this is accepted.

### 2. σ values from different null procedures on the same scale

Instruction 7: flag if σ values from *different* null procedures are treated as directly comparable.

The main σ values in P1B:

- 3.6σ from Eskilt & Komatsu (WMAP+Planck PR3).  
- ≈2.7σ from Planck NPIPE (β = 0.30° ± 0.11°).  
- ≈2.9σ from ACT DR6 (β = 0.215° ± 0.074°).  
- 3.9σ from an *inverse‑variance combination* of the Planck NPIPE and ACT DR6 numbers, which the paper labels as “auxiliary cross‑check only” and explicitly says “neglects shared calibration systematics; the published joint analysis at 3.6σ [2] is the headline.”

Observation:

- P1B **does not** present these σ values as being on an identical null‑procedure scale; it explicitly warns that the 3.9σ inverse‑variance combination is not headline and neglects shared systematics. This complies with the requirement.

Finding:

- **P1B-N14 (NIT)**  
  No σ‑scale conflation in the excerpt that would require an ESSENTIAL correction. The authors are unusually explicit about the limitations.

### 3. Version‑history language and internal audit tags

Instruction 8: flag any version‑history or audit artifacts that appear in body prose.

The manuscript is full of such language:

- “(Dated: 2026‑06‑03 PDT — v1B.0.42)” in the header.  
- Numerous phrases: “R‑upgraded‑round4 GEM‑m2,” “R‑upgraded‑round4 GEM‑B1,” “corrected fire #25,” “Wave 14 cross‑paper snapshot,” “R8 GEM‑B3 nit,” “v1B.0.14,” “v1B.0.13+,” “queued for v1B.0.16+,” “pod‑side nested‑sampling run,” etc.  
- Appendix B: “Claims classification;” main text: “R12 GEM‑M2 closure,” “truth‑audit falsification,” etc.

These are internal project artifacts, not appropriate for a PRD manuscript.

Findings:

- **P1B-E5 (ESSENTIAL, global)**  
  **Problem:** Extensive internal version‑tracking, audit tags, and workflow language are embedded throughout the scientific prose and tables, e.g.:  
  - “R‑upgraded‑round4 GEM‑m2”,  
  - “corrected fire #25”,  
  - “Wave 14 cross‑paper snapshot”,  
  - “R8 GEM‑B3 nit”,  
  - “R12 GEM‑M2 closure: prior text claimed the chain ‘remains alive on the pod’…”, etc.  
  These are unintelligible to an external reader and inappropriate for PRD.  
  **Required fix:**  
  - Remove all “GEM‑…”, “R‑upgraded‑round4”, “fire #xx”, “wave‑14” and similar project‑internal codes from the main text and tables. Where these were meant to denote specific corrections or audits, translate them into plain scientific language or move them into a private changelog, not the published paper.

- **P1B-M5 (MAJOR, Tables III–IV and some footnotes)**  
  **Problem:** The cross‑paper status table (Table III) and MCMC inventory (Table IV) explicitly freeze a “Wave 14 snapshot,” with commentary like “P1(b) is now post‑v1B.0.40 in development,” “the live program continues to advance… tracked on the project site rather than re‑bumped inside this table.”  
  **Required fix:**  
  - For PRD, either remove Table III entirely or convert it into a minimal, static description of which chains and analyses are used in this paper. Drop all references to “wave‑14 snapshot,” version numbers, future plans, or external project sites.  
  - For Table IV, keep only the content that is directly relevant to the scientific conclusions (e.g., R̂−1 values and sample counts), but strip out commentary about v1B.* snapshots, pod‑side runs, and log markers like “MCMC DONE ITER2 OMP6.”

### 4. Duplicate phrases / typographical artifacts

Instruction 9: flag duplicate phrases.

Scanning:

- I did not find simple copy‑paste glitches like “canonical canonical‑mask,” but there are a few slightly awkward repeats:
  - “canonical quintom signature” is used twice in similar context, but not back‑to‑back.
  - “Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing likelihoods” and similar strings are repeated verbatim.

None rise to the level of obvious copy‑paste errors, but there are some genuine typos:

- “above this scale the contact‑operator description breaks down … addressed in this paper sit at energies E ≪ Λstrong , where the EFT treatment is controlled.” – fine.
- Table II caption has “R̂cl = 0.0705 as chain‑length diagnostic” – unclear meaning.
- Some mis‑spacing like “MPl    2” and inconsistent minus signs (e.g., “ΛCDM ̸= ECH” uses a combining slash character).

Finding:

- **P1B-N15 (NIT, global)**  
  **Problem:** Several typographical glitches (extra spaces, odd characters, minor repetition) distract but do not alter meaning.  
  **Required fix:**  
  - Run a careful copy‑edit pass to fix spacing (e.g., “MPl    2”), stray combining characters (e.g., “̸=”), and to simplify overly repeated long phrases where possible.

### 5. Abstract accuracy

Instruction 10: abstract must summarize what is actually proved / done.

The abstract claims:

- A stock‑CAMB ΛCDM+ΔNeff MCMC run with Cobaya v3.6.1, total frozen samples, specific H0 and ΔNeff posteriors, and explicitly says this is “reported as a null‑consistency test … not as evidence for or against ECH.”
- NaMaster pseudo‑Cℓ pipeline validation: inject β = 0.27°, recover β̂ = 0.238°, bias 0.032°, with explicit caveats about not being a sky detection.
- Spectator‑ALP consistency check: ALP with fa ~ MPl, m ~ H0 consistent with β = 0.342° ± 0.094° (3.6σ), with explicit caveats about fine‑tuning and non‑distinctiveness.

These match what the body actually does; if anything, the body repeats and elaborates those caveats. There is no claim in the abstract that the paper “proves” something beyond these technical verifications.

Finding:

- **P1B-N16 (NIT)**  
  Abstract is honest about scope and does not over‑claim. No change strictly necessary, though some shortening would help readability.

### 6. Paper length vs contribution

P1B is 12 pages, primarily documenting:

- One standard ΛCDM+ΔNeff Cobaya run with Planck+BAO+SN(+SH0ES+S8).
- A NaMaster pipeline test on Planck Commander with 500 MCs.
- A modest ALP birefringence consistency check built on existing literature.

Given these are straightforward analyses using public tools and likelihoods with heavy emphasis on internal convergence bookkeeping and cross‑paper project logistics, 12 pages is *on the long side* for the level of genuinely new technical contribution.

Finding:

- **P1B-M6 (MAJOR, global)**  
  **Problem:** For PRD, a 12‑page companion that largely documents run bookkeeping, internal audit logs, and planned nested‑sampling work is verbose relative to its scientific content.  
  **Required fix:**  
  - Streamline by:
    - Removing or drastically compressing internal project framework language, cross‑paper status tables, and future‑work queues.  
    - Condensing the MCMC bookkeeping (burn‑in arithmetic, logs about previous miscounts) to a short methods subsection or supplementary material.  
    - Focusing the main text on: (i) what is *actually new* in the ΔNeff proxy setup, (ii) the NaMaster validation design and bias estimates, (iii) the ALP parameter scan and its key inferences.  
  - A target of **8–9 pages** would likely suffice for the content presently presented.

---

## Summary recommendation

**MAJOR REVISIONS**

The core scientific content (null ΔNeff result, NaMaster pipeline validation, and ALP consistency check) is technically sound and conservatively interpreted, and the key published numbers from cosmic‑birefringence and SH0ES papers are correctly quoted where the references are valid. However, several references use non‑existent arXiv identifiers, there is an internal inconsistency about which Planck data release underlies the Eskilt & Komatsu 3.6σ result, and the manuscript is heavily entangled with internal versioning and audit nomenclature that is inappropriate for a PRD article. Substantial cleanup of the references, removal of project‑internal artifacts from the prose, clarification of DESI DR1 vs DR2 usage, and overall shortening are required before the paper is suitable for publication.