# P5 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v2_P5_v0_1_31
**Wall time**: 30.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=26229, completion=1553, total=27782

---

## PAPER-PER-B1 – Self-citation “Paper IV” is not externally published

Paper section: Abstract, Introduction, §II, bibliography entry `\bibitem{golden_chirality_2026}`.  
Issue: The paper cites “Paper IV” as if it were a normal published reference, but the bib entry only points to an internal LaTeX source and version tag without arXiv ID, journal, or DOI. This makes it impossible for an external reader to verify key claims (global chirality monopole, dipole bound) that underlie much of the analysis and interpretation.  
Fix: Explicitly state that Paper IV is an in-prep/companion manuscript and provide its public identifier once available (arXiv ID, journal info), or clearly label it as an internal technical report until then; adjust language in the main text to avoid relying on it as a “publication-grade” external constraint until such an identifier exists.  

## PAPER-PER-M1 – Tempel 2014 metadata: SDSS DR10 and galaxy count

Paper section: Abstract (“Tempel et al. 2014 friends-of-friends group classifier … SDSS DR10, only ~14k galaxies in the filament-like bin”) and §Tempel.  
Issue: The Tempel et al. paper is correctly cited (A&A 566 A1, arXiv:1402.1350), but the description “SDSS DR10” is ambiguous: Tempel’s catalogue is constructed from an SDSS DR10 spectroscopic sample but is released as an SDSS DR10-based group catalogue with 588,193 galaxies and 82,458 groups, not “a classifier with only ~14k galaxies in the filament-like bin.” [1] The “~14k” is actually your overlap filament-like subsample, not a property of Tempel itself, and as written it can be read as a characterization of Tempel’s catalogue. [1]  
Fix: Rephrase the abstract/§Tempel description to make clear that Tempel et al. (2014) provide a 588,193-galaxy SDSS DR10 FoF group catalogue, and that “~14k filament-like” refers specifically to your matched-spiral overlap in that richness bin, not to the Tempel catalogue size. [1]  

## PAPER-PER-M2 – Cautun et al. 2014 usage vs. method

Paper section: Abstract and §V-Web (“Cautun et al. 2014 geometric default λ_th=0”).  
Issue: The Cautun et al. paper (arXiv:1401.7866, “Evolution of the cosmic web”) introduces and applies the NEXUS Multiscale Morphology Filter, not the Hahn/Hoffman tidal-tensor V-Web/T-Web scheme; it does discuss void/wall/filament/cluster taxonomy but does not define a single canonical tidal-eigenvalue threshold “geometric default λ_th=0” for the Hahn/Hoffman-style classifier. [2] Attributing “geometric default λ_th=0” specifically to Cautun et al. is therefore overstated. [2][3]  
Fix: Attribute λ_th=0 as a standard choice in the tidal-tensor web-classification literature (e.g. following Hahn et al. 2007 and related work), and cite Cautun et al. 2014 only for general cosmic-web morphology and volume-filling fractions rather than for this precise threshold choice. [2][3]  

## PAPER-PER-M3 – Shamir 2022 amplitude and sample description

Paper section: §XIII.3 “Comparison to Shamir 2022 DESI Legacy,” citation `\bibitem{Shamir2022DESI}`.  
Issue: Shamir (2022) indeed analyses spin directions of galaxies in DESI Legacy, uses a sample of nearly \(1.3 \times 10^6\) spirals, and reports a significant large-scale asymmetry/dipole with \(P<10^{-5}\).[4] However, the paper does not summarize its result as a simple “2–4% large-scale asymmetry” in the abstract; that specific 2–4% range is an interpretive compression rather than a number clearly quoted by Shamir, and could mislead readers into thinking it is his published headline. [4]  
Fix: Either (a) quote the exact amplitude language used by Shamir (e.g. “dipole axis alignment with probability \(P<10^{-5}\)” and the specific hemispheric count differences) with a citation, or (b) clearly mark “2–4%” as your approximate back-of-envelope restatement of his asymmetry rather than a published number. [4]  

## PAPER-PER-M4 – T-Web DESI DR1 citation details and author list

Paper section: §“Concurrent-literature DR1/EDR cosmic-web cross-validation,” citation `\bibitem{TWebDESI2026}`.  
Issue: The arXiv preprint 2604.02463 is correctly titled “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” but the actual author list is Hafiz Inam Ullah, Muhammad Awais, Tonatiuh Matos, and John F. Suárez-Pérez, not “DESI Collaboration.” [5] It is also submitted to JCAP, not MNRAS as implied by the “submitted to MNRAS” wording. [5] Treating it as a DESI-collaboration, MNRAS-submitted paper fuses metadata.  
Fix: Update the bib entry to use the correct author list and submission venue: cite Ullah et al. (2026), arXiv:2604.02463, “submitted to JCAP,” and avoid labeling it as a DESI Collaboration MNRAS submission unless a later version actually appears under that byline and journal. [5]  

## PAPER-PER-nit1 – Minor mischaracterization of Hoffman et al. 2012

Paper section: §V-Web Algorithm and multiple references to Hoffman et al. 2012 as “tidal-tensor classifier” (V-Web).  
Issue: Hoffman et al. 2012 (arXiv:1201.3367) introduces a *velocity-shear based* kinematic web classification (“V-web”) and explicitly distinguishes it from the tidal-tensor (“T-web”) method of Hahn et al. 2007.[3][6] The manuscript sometimes blurs this, describing a tidal-tensor classifier while citing Hoffman’s kinematic V-web as if it were the same algorithm. [3][6]  
Fix: Clarify in §V-Web that you implement a gravitational tidal-tensor classifier following Hahn et al. 2007, and that Hoffman et al. 2012 is cited for the broader V-web/T-web context (or explicitly state if you are using the velocity-shear V-web rather than the density-based tidal tensor); align terminology so that “V-Web” and “T-Web” are not conflated. [3][6]
