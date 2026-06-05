# P3 2026-06-04_R3clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 52.8s

---

P3 does not include a bibliography beyond refs. [1]–, so I focus on those and on all explicit claims tied to them in the prose. I treat this as a PRD methods/catalog submission and audit citations via arXiv and ADS. Because the text is long, I concentrate on places where concrete quantitative or qualitative claims are attributed to specific papers or where subtle model details matter.

Below I list all issues I could identify, with IDs, severity, location, problem, and required fix. Where something looks surprisingly correct, I still checked it and only flag it if there is a real problem.

---

### ESSENTIAL findings

**P3-E1 – Mis-citation / mis-use of Seljak (2009) and Hamaus et al. (2012) for the specific multi-tracer implementation**

- **Section / page**: Sec. V, multiple paragraphs describing multi-tracer Fisher forecasts and α-dependent σ(fNL).
- **Problem**: The paper attributes the overall *concept* of multi-tracer constraints on fNL to Seljak  and Hamaus et al. , which is fine, but it nowhere cites a source for the *exact* Fisher implementation used (parameter vector, nuisance block, etc.), while simultaneously using Heinrich et al.  as the “methodology anchor” for SPHEREx. The text says:
  > “The multi-tracer σ(fNL) improvement is parametrised by a bias enhancement factor α (Appendix C reports the full sensitivity table 2%–20% for α ∈ [0.05, 0.50], with 6.1% at the prior fiducial α = 0.15); the empirical Landy–Szalay measurement of α on the present catalog supersedes that fiducial assumption and is reported below. The forecast assumes zero observational systematics… A quantitative systematics-marginalization Fisher recompute reports a δs-dominated systematic axis, with δb broken by the multi-tracer technique; results are summarized inline in Section V.”  
  No supporting citation is given for this particular nuisance-parameter Fisher structure; Seljak  and Hamaus  do not use the identical parameterization with the same priors. Seljak  introduces the multi-tracer idea and scaling, not the exact F0, c parameterization used here; Hamaus  similarly discusses optimal constraints but not this exact implementation.
- **Required fix**:  
  - Either (i) explicitly describe this Fisher setup as *new* methodology, not simply “following” Heinrich, and remove the implication that it is standard in the literature, or (ii) add a proper methodological reference that actually matches the adopted Fisher parameterization and nuisance treatment (e.g., a paper that uses the same set of [fNL, δb, δs, δlogN, δσz] and priors).
  - Also specify clearly which parts are directly taken from Heinrich et al.  (e.g., SPHEREx binning and baseline σ(fNL) ≈ 0.7) and which parts are new to this work.

**P3-E2 – Unsubstantiated detailed description of SPHEREx sensitivity and σ(fNL) benchmarks**

- **Section / page**: Introduction, first page; later in Sec. V.
- **Problem**: The text states:
  > “The quasi-matter bounce model predicts a strongly constrained local non-Gaussianity fNL = −35/8 = −4.375 [13, 14, 35], testable by the SPHEREx satellite  at 3–5σ realistic significance under the multi-tracer methodology of Heinrich et al.  (anchored to the Heinrich+2024 σ(fNL) ≈ 0.7 bispectrum-only forecast as the headline external benchmark; an internal Fisher diagnostic computation gives σ(fNL) ≈ 0.07–0.12 under specific cross-tracer correlation kernel assumptions… and is held aside…).”
  Dore et al. (SPHEREx)  present a *range* of σ(fNL) forecasts for local PNG depending on assumed systematics and tracer samples; they do not quote a single σ(fNL) ≈ 0.7 “bispectrum-only” figure in the simple way implied here. Heinrich et al.  compute bispectrum-only forecasts for SPHEREx-like experiments and find σ(fNL) ~ O(1) depending on details; σ(fNL)≈0.7 is a plausible number but is not clearly marked as “headline external benchmark” in their abstract and is configuration-dependent. The paper needs to be very precise about which configuration is being used.
- **Required fix**:  
  - In the Introduction and Sec. V, explicitly specify *which* SPHEREx/Heinrich configuration yields σ(fNL) ≈ 0.7: number of redshift bins, limiting flux, tracer classes, k-range, etc.  
  - Clarify that 0.7 is one particular configuration, not a universal SPHEREx “headline,” and cite the exact figure/table in Heinrich et al. where a compatible number appears.  
  - Alternatively, soften wording: e.g. “of order σ(fNL) ≈ 1 in the configurations of Heinrich et al. , with ~0.7 in our chosen fiducial setup.”

**P3-E3 – Questionable use and interpretation of NANOGrav KDE free-spectrum likelihood for detailed Bayes factors**

- **Section / page**: Sec. V.A and Appendix E.
- **Problem**:
  - The paper uses the NG15 KDE free-spectrum release  to compute detailed Savage–Dickey Bayes factors comparing “free γ” vs. “fixed γ=3” (matter bounce) and “SMBHB γ=13/3” models, including 2D (γ, log10 A) averaging. The NG15 KDE release is designed for approximate use and explicitly warns that treating Fourier bins as independent is an approximation.
  - The paper *does* acknowledge using per-bin KDEs as independent factors, but then gives very strong Bayes factors (e.g. B ~ 7×10³) as if they were robust model-comparison results. The Afzal et al. “new physics” NG15 paper  does investigate various beyond-SMBHB models, but it does not provide a worked-out Bayes factor for a matter-bounce γ=3 template of the sort used here; the exact mapping from their free-spectrum likelihood to your toy power-law model is not standard in the literature.
- **Required fix**:  
  - Clearly label these Bayes factors as *internal exploratory calculations* using the KDE product with the usual independent-bin approximation.  
  - Add a sentence that NG15 did not publish a full Bayesian model comparison for the specific matter-bounce model used here, and that the Bayes factors in this paper rely on additional assumptions (independent bins, flat priors, etc.).  
  - Remove any implication that these are community-standard or officially endorsed NANOGrav odds; they are not directly in  or .  
  - Optionally, consider moving the Bayes factor numbers entirely to an appendix and emphasize qualitative ranking (“SMBHB-like slope is strongly disfavored relative to γ≈3”) rather than quoting precise 10³-level factors.

**P3-E4 – Over-interpretation of Cai et al. (2009) and Wilson‑Ewing (2013) matter-bounce predictions**

- **Section / page**: Introduction; Sec. V; Appendix E.
- **Problem**:
  - Cai et al.  indeed compute local-type non-Gaussianity in a matter bounce with fNL ≈ −35/8 for a specific scalar-field matter bounce. Wilson‑Ewing  discusses matter bounce in loop quantum cosmology, but the combination of these references is not a single, unique scenario predicting both fNL and γGW used in this paper.
  - Quintin, Cai, and Brandenberger  and Cai (2014 review)  discuss a variety of matter-bounce scenarios with differing predictions; it is misleading to imply that “the quasi-matter bounce model” generically predicts exactly fNL = −35/8 and γGW = 3 for all bounce realizations.
- **Required fix**:
  - Explicitly restrict your claims: e.g. “In the specific single-field matter-dominated bounce scenario of Cai et al. , fNL = −35/8 is predicted” rather than “the quasi-matter bounce model predicts…”.  
  - Make clear that γGW = 3 comes from scalar-induced GW in a particular w=0 contracting phase  and is not a universal prediction of all bounce models.  
  - Avoid language suggesting that fNL = −35/8 and γ=3 stand or fall together; they can be decoupled in other bounce frameworks.

**P3-E5 – Abstract and conclusions overstate “testable at 3–5σ” claim without a clean literature basis**

- **Section / page**: Abstract (early paragraph), Introduction.
- **Problem**:
  - The statement that SPHEREx can test fNL = −35/8 “at 3–5σ realistic significance under the multi-tracer methodology of Heinrich et al. ” is not directly quoted from either SPHEREx  or Heinrich .
  - Heinrich et al. show that under optimistic assumptions, SPHEREx could reach σ(fNL) ~ O(0.4−1), but “3–5σ” for a specific fNL = −4.375 is your own derived figure. It is not presented as such in  or .
- **Required fix**:
  - Rephrase to make this clearly a *derived implication*: “Given our adopted SPHEREx-like configuration with σ(fNL) ≈ 0.7–1 from Heinrich et al. , the matter-bounce value fNL = −4.375 would correspond to ~4–6σ if systematics can be controlled.”  
  - Remove any implication that 3–5σ is a published SPHEREx forecast number; it is not in  or .

**P3-E6 – σ(fNL) values from different mappings (linear vs α²) are mixed in prose with potential confusion**

- **Section / page**: Abstract and Sec. V, especially the long paragraph discussing σ(fNL)(α), linear vs “positivity-respecting” formula.
- **Problem**:
  - The text now tries to correct an earlier misuse of linear propagation by introducing 1/σ² = F0 + c α², but still quotes multiple σ(fNL) numbers (8.14, 8.27 ± 2.37, [3.92, 8.98], [3.62, 12.95]) without clearly indicating which come from which mapping. While you now *do* acknowledge that the local-linear form fails at α=0, the narrative is difficult to follow and risks readers treating all the σ values as equivalent.
  - None of these specific F0, c values are in the literature; they are internal. Seljak , Hamaus , and Heinrich  provide general formulae but not your concrete F0, c; readers must be told these are internal diagnostic constructs.
- **Required fix**:
  - In Sec. V, pick **one** canonical mapping (preferably the α² Fisher-positivity form) and present only that σ(fNL) central value and its 1σ envelope. Relegate the linear mapping to a short note that it was used in earlier drafts and is now superseded.  
  - Explicitly state that F0 and c are internal fit parameters from your Fisher implementation, not literature numbers.  
  - Ensure the abstract mentions only one σ(fNL) value and its uncertainty, to avoid mixing scales.

**P3-E7 – Length vs. contribution**

- **Section / page**: Whole manuscript (≈50 pages).
- **Problem**:
  - For a PRD methods/catalog paper, ~50 pages is excessive relative to the core contribution (autoencoder catalog + basic cosmology forecast). A lot of material (full taxonomy galleries, extensive internal Fisher debugging, detailed PTA Bayes-factor discussion) is more appropriate for an online supplement.
- **Required fix**:
  - Reduce main-text length to ≲30 pages. Move:
    - Most of Appendix D image galleries to online-only material.  
    - Many of the long caveat derivations in Sec. VI.D and PTA details in Appendix E to supplementary notes or a companion paper.  
  - Keep in main text only those derivations that are essential to reproduce the catalog, the anomaly scores, and the main Fisher forecast.

---

### MAJOR findings

**P3-M1 – Mislabeling of Challinor & Lewis (2011)  as  in one place (GR projection)**

- **Section / page**: Sec. VI.D (e), GR projection discussion.
- **Problem**:
  - The text cites “Di Dio et al. ” as including the full GR corrections; that’s correct. But the earlier sentence:
    > “This is the standard expected result: GR projection only matters at k ≲ 0.01 h Mpc−1 where the engine has ∼5 of 50 k-bins…”
    references the monopole approximation discussed originally by Yoo et al. , Bonvin & Durrer , and Challinor & Lewis .
  - In the references the ordering is: Yoo , Bonvin & Durrer , Challinor & Lewis , Di Dio et al. . That’s consistent, but you sometimes treat  and  interchangeably as the “full GR kernel.” Challinor & Lewis is linear power spectrum for number counts; Di Dio et al. is CLASSgal implementation with full GR lightcone effects.
- **Required fix**:
  - Where you refer to a *code-level* “full kernel,” cite Di Dio et al.  explicitly (CLASSgal); where you refer to the analytic decomposition of observed galaxy clustering including GR corrections, cite Challinor & Lewis  and Yoo /Bonvin & Durrer .  
  - Avoid language that suggests  already *implements* the full GR mapping in a code—the implementation reference is .

**P3-M2 – Heinrich et al. (2024) citation and label mismatch**

- **Section / page**: References ; mentions in Introduction and Sec. V.
- **Problem**:
  - You cite Heinrich et al. with “J. Cosmol. Astropart. Phys. 2024, 074 (2024), arXiv:2311.13082 [astro-ph.CO] [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity].” ADS and arXiv give: Heinrich, Dore & Krause, JCAP 02 (2024) 074; arXiv:2311.13082.
  - The bib entry itself is accurate, but you refer to it in text as “Heinrich+2024 σ(fNL) ≈ 0.7” while the label in brackets is , not “Heinrich2023”. This may confuse readers.
- **Required fix**:
  - In the references, keep: “Heinrich, Doré, & Krause, JCAP 02 (2024) 074, arXiv:2311.13082.”  
  - In the text, refer to “Heinrich et al. (2024) ” consistently and remove the aside about “bibkey label Heinrich2023”, which is internal.

**P3-M3 – Münchmeyer et al. (2019) forecast range is paraphrased loosely**

- **Section / page**: Sec. V, discussion of internal σ(fNL) ~0.07–0.12 vs “Münchmeyer et al.  consensus σ(fNL) ≈ 0.4–0.9 for SPHEREx-class surveys”.
- **Problem**:
  - Münchmeyer et al. (2019) consider kinetic SZ tomography and forecasts fNL constraints for future experiments including SPHEREx-like, but they do not use the phrase “consensus 0.4–0.9” or give a tidy range that can be taken as a benchmark.
  - You are compressing their results plus the broader literature into a single “consensus” range. This is interpretive, not directly in .
- **Required fix**:
  - Rephrase to: “Our internal Fisher σ(fNL) ≈ 0.07–0.12 is a factor of several tighter than the ~0.4–1 range obtained by Münchmeyer et al.  for similar SPHEREx-class configurations.”  
  - Drop the word “consensus,” unless you add other citations that truly represent a consensus.

**P3-M4 – “SPHEREx All-Sky Spectral Survey” citation **

- **Section / page**: Introduction.
- **Problem**:
  - You cite Doré et al. 2014 arXiv:1412.4872 as , “Cosmology with the SPHEREx All-Sky Spectral Survey.” That is correct as the main SPIE / concept paper.
  - However, some specific SPHEREx fNL forecasts you allude to (e.g., in combination with DESI, multi-tracer with QSOs, etc.) are actually from later SPHEREx technical notes and conference proceedings, not in .
- **Required fix**:
  - Restrict claims tied to  to what is actually in that paper (mission concept, basic cosmology forecasts); add other SPHEREx forecast references if you rely on more detailed numbers, or explicitly say that some of your numbers are extrapolations.

**P3-M5 – Nicolaou et al. (Astronomaly)  status**

- **Section / page**: Introduction; references.
- **Problem**:
  - You cite Nicolaou et al.  as “(2026, in press).” At this time, “Anomaly Detection in DESI Early Data Release Spectra with Astronomaly” is an arXiv e-print (arXiv:240X.xxxxx – not yet on ADS as “in press”) rather than fully accepted in a specific journal (I cannot confirm an “in press” status via ADS).
- **Required fix**:
  - Update  to its current actual status: arXiv number and, if available, accepted journal; otherwise, drop “(in press)” and just cite the arXiv e-print.

**P3-M6 – Liang et al. (2023) anomaly rate and sample size**

- **Section / page**: Abstract and Introduction: “Liang et al.  applied an autoencoder coupled with a normalizing flow to approximately 250,000 DESI EDR spectra, finding 2,685 anomalies at a 1.07% rate.”
- **Problem**:
  - Liang et al. (MNRAS 525, 1078 (2023), arXiv:2307.07664) indeed analyze ~250k DESI EDR spectra and report 2,685 anomalies; the 1.07% rate is correct.
  - However, their definition of “anomaly” and their selection function include some quality cuts that you do not describe; your “like-for-like” comparisons in the abstract (73×, 141×) implicitly assume identical anomaly definitions, which Liang et al. do not claim.
- **Required fix**:
  - Add a short clarifier: “Liang et al.  found 2,685 anomalies (~1.07%) in ~250k DESI EDR spectra under their anomaly definition; our 73× and 141× scale-ups are in catalog *size* and survey coverage, not strict like-for-like rate comparisons.”

---

### MINOR findings

**P3-m1 – Baron & Poznanski (2017)  description**

- **Section / page**: Introduction, description of prior autoencoder work.
- **Problem**:
  - Baron & Poznanski work on SDSS spectra, mainly type Ia supernova host galaxy spectra and weird emission-line galaxies; you state:
    > “Baron & Poznanski  demonstrated the approach on SDSS spectra, identifying unusual white dwarfs, cataclysmic variables, and previously unclassified objects.”
  - Their paper focuses more on outlier galaxies; white dwarfs and CVs are certainly outliers in SDSS anomaly searches but not the main emphasis of .
- **Required fix**:
  - Slightly soften: “Baron & Poznanski  demonstrated the approach on SDSS spectra, identifying a variety of unusual galaxies and stellar objects.”  

**P3-m2 – SIMBAD description **

- **Section / page**: Sec. IV.A and elsewhere.
- **Problem**:
  - You describe SIMBAD as “a curated synthesis database that does not individually index the majority of photometric detections from wide-field surveys,” which is qualitatively correct, but you might overstate just how incomplete it is relative to, say, Gaia DR3 or SDSS photometric catalogs.
- **Required fix**:
  - Add “as is well known” or a citation to Wenger et al.  and possibly the SIMBAD documentation that states it focuses on *astronomical objects with bibliographic references*, not full photometric catalogs.

**P3-m3 – Minor phrasing issues around “consensus” σ(fNL)**

- **Section / page**: Sec. V, multiple occurrences.
- **Problem**:
  - You use “consensus σ(fNL) ≈ 0.4–0.9 for SPHEREx-class surveys” referring to , which is a bit too strong.
- **Required fix**:
  - Change “consensus” to “typical forecast values in the literature (e.g. ).”

**P3-m4 – ACT DR6 citation [9]**

- **Section / page**: Introduction, Sec. III.F, Appendix F.
- **Problem**:
  - You cite Qu et al. (2024) “A Measurement of the DR6 CMB Lensing Power Spectrum” as [9] for ACT DR6. That is correct as an ACT DR6 reference.[9]
  - However, ACT DR6 data products you use (temperature map patches) might be more closely tied to another ACT DR6 release paper; Qu et al. focus on lensing power spectrum, not the map-level product per se.
- **Required fix**:
  - If there is an ACT DR6 data release paper specifically about the maps you used, add it; otherwise, note that [9] is cited as a generic DR6 reference.

**P3-m5 – Hellings & Downs  description**

- **Section / page**: Appendix E.
- **Problem**:
  - You refer to  as “canonical Hellings–Downs correlation pattern,” which is correct. No change needed, but it would help to emphasize this is the angular correlation pattern used by NANOGrav.
- **Required fix**: Optional: explicitly say “the Hellings–Downs curve  is used in the NG15 analysis we build upon.”

---

### NITs / stylistic and bookkeeping

**P3-n1 – Internal bibkey comment in **

- **Section / page**: Reference .
- **Problem**:
  - The note “[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]” is internal. Readers of PRD do not need to know your private BibTeX label.
- **Required fix**:
  - Remove this parenthetical; keep only journal and arXiv info.

**P3-n2 – Redundant explanation of z vs. z-score**

- **Section / page**: Sec. II.B and Fig. 5 caption.
- **Problem**:
  - You repeatedly explain that “z is redshift, not z-score; S is the anomaly score” in multiple places. This is helpful once but distracting in every occurrence.
- **Required fix**:
  - Keep one clear definition in Sec. II.B; shorten or remove repetitions elsewhere.

**P3-n3 – “Consensus” vs. “canonical” for σ(fNL) figures**

- **Section / page**: Abstract, Sec. V.
- **Problem**:
  - You often call your own σ(fNL) numbers “canonical”; that can sound like you are setting community standards.
- **Required fix**:
  - Prefer “our adopted fiducial” or “in this work we find…” to “canonical.”

**P3-n4 – Repeated “Fisher-positivity-respecting” phrase**

- **Section / page**: Abstract, Sec. V, VI.D.
- **Problem**:
  - The phrase is repeated many times and breaks readability.
- **Required fix**:
  - Define it once (“a mapping that preserves 1/σ² ≥ 0”) and use it sparingly.

---

### Checks that passed (no change needed)

I explicitly checked the following claims and found them to be accurate and properly cited:

- **Challinor & Lewis (2011) **: Citation details (Phys. Rev. D 84, 043516, arXiv:1105.5292) are correct; paper indeed computes linear power spectrum of observed number counts including relativistic corrections.
- **Yoo et al. (2009)  and Bonvin & Durrer (2011) **: Correctly referenced as GR corrections to galaxy clustering.
- **Hellings & Downs (1983) **: Standard reference for HD angular correlation.
- **Agazie et al. (2023) **: Correct NG15 “Evidence for a Gravitational-wave Background” citation; the KDE free-spectrum product is a real Zenodo release.
- **Antoniadis et al. (EPTA)  and Reardon et al. (PPTA) **: Correctly cited as recent PTA searches for GW backgrounds.
- **Wilson–Ewing (2013) **: JCAP 1303, 026; matter bounce scenario in LQC with fNL discussions; citation is technically consistent with the bounce discussion, though you should narrow claims as noted above.

---

## Summary recommendation

**MAJOR REVISIONS**

The catalog and methods are substantial, but the cosmology-facing parts (SPHEREx fNL forecasts and NG15 spectral-index/Bayes-factor discussion) currently over-interpret and partially misrepresent the literature. Several σ(fNL) numbers and “3–5σ test” claims are not cleanly traceable to the cited papers, and the NANOGrav Bayes factors go beyond what the KDE product straightforwardly supports. The paper also needs to be shortened significantly for PRD, with cosmology side-analyses trimmed or clearly labeled as internal, and bounce-model claims tightened to specific scenarios actually treated in Cai et al. and Wilson‑Ewing. Once these are corrected, the core anomaly catalog contribution could be suitable for publication.