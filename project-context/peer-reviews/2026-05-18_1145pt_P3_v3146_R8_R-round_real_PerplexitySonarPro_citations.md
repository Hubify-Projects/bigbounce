# P3_v3146_R8 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1145pt
**Wall time**: 39.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=61008, completion=1552, total=62560

---

## PAPER-PER-B1 — Mis-cited Liang et al. survey and anomaly counts (BLOCKER)

**Location:** Abstract, lines mentioning “Liang et al. [Liang2023] (2,685 anomalies on DESI EDR)” and the same claim repeated later.

**Issue:** Liang et al. 2023 is *“Outlier Detection in the DESI Bright Galaxy Survey (BGS) dataset from the DESI Early Data Release”* and analyzes BGS galaxies, not “DESI EDR” as a whole.[1] The paper’s main outlier sample is 400 galaxies (top outliers), not a 2,685-anomaly catalog; 2,685 does not appear in the abstract or description of the public product.[1] The text here fuses the correct title/authors with incorrect sample characterization (EDR vs BGS and 2,685-object scale), i.e. metadata/scope confabulation.

**Fix (1–2 sentences):** Change the description of Liang et al. to match the actual paper, e.g. “Liang et al. [Liang2023] applied an autoencoder+normalizing-flow method to the DESI BGS subset of the Early Data Release, publishing a probability catalog and highlighting 400 top outliers.”[1] Remove or justify the “2,685 anomalies” number by either citing an actual table/threshold from Liang et al. or dropping that specific figure and the “1.07% rate” unless you can point to the exact definition and location in their released catalog.[1]


## PAPER-PER-M1 — Baron & Poznanski cited correctly (minor)

**Location:** Introduction, paragraph citing “Baron & Poznanski [Baron2017]”.

**Issue:** The cited work “The weirdest SDSS galaxies: results from an outlier detection algorithm” (MNRAS 465, 4530, 2017) is an outlier-detection study on SDSS galaxies; authors, title, venue, and general description as an anomaly/outlier search are all consistent with the ADS record.[2] No fused metadata detected.

**Fix (1–2 sentences):** No change needed for citation accuracy. If you want to be maximally precise, you could add that their algorithm is based on an unsupervised Random Forest applied to >2 million SDSS galaxy spectra, matching their abstract.[2]


## PAPER-PER-M2 — Wands (2010) citation generally correct but overly specific (minor)

**Location:** Introduction: “The quasi-matter bounce model predicts … \(f_{\rm NL} = -35/8 = -4.375\) [Wands2010, Cai:2009fn, WilsonEwing2012].”

**Issue:** Wands (2010) is a review on local non-Gaussianity from inflation, not a dedicated quasi-matter-bounce calculation, and does not itself derive \(f_{\rm NL} = -35/8\) for a matter bounce.[3] That specific value originates from matter-bounce calculations such as Cai et al. (2009) and related bounce papers, not Wands’ review.[3] Including Wands as if it directly provides the \(-35/8\) prediction is over-precise and slightly misleading, though not a full metadata fusion.

**Fix (1–2 sentences):** Keep Wands (2010) as a general non-Gaussianity reference but restrict the explicit \(-35/8\) attribution to Cai et al. (2009) and Wilson–Ewing (2012), e.g. “The quasi-matter bounce model predicts \(f_{\rm NL} = -35/8\) (see e.g. Cai et al. 2009; Wilson–Ewing 2013 for the matter-bounce derivation; Wands 2010 for review of local non-Gaussianity).”[3]


## PAPER-PER-M3 — SPHEREx white paper reference is real but ID should be explicit (minor)

**Location:** Introduction, SPHEREx citation “SPHEREx2014”.

**Issue:** The text refers to the SPHEREx satellite forecast and attributes it to “SPHEREx2014” without giving a clear arXiv ID. The relevant document is Doré et al. 2014, “Cosmology with the SPHEREx All-Sky Spectral Survey”, arXiv:1412.4872.[4] The arXiv ID and authorship match a SPHEREx cosmology white paper, but that identifier is implicit.

**Fix (1–2 sentences):** In the bibliography entry for SPHEREx2014, add the explicit arXiv ID and lead author, e.g. “Doré et al., ‘Cosmology with the SPHEREx All-Sky Spectral Survey’, arXiv:1412.4872 (2014).”[4] This removes any ambiguity about which SPHEREx document is being used as the forecast source.


## PAPER-PER-M4 — Baron et al. and Liang et al. context compressed but not fabricated (minor)

**Location:** Introduction, “Baron & Poznanski [Baron2017] demonstrated the approach on SDSS spectra… Liang et al. [Liang2023] applied an autoencoder coupled with a normalizing flow…”

**Issue:** Both referenced papers genuinely exist with those authors and use ML methods on SDSS and DESI BGS spectra respectively, and the high-level summaries (autoencoder-based anomaly/outlier detection, identification of unusual objects) match their abstracts.[1][2] The only material problem in this cluster is the later, more detailed misstatement of Liang’s sample size and EDR scope flagged in PAPER-PER-B1; the intro-level summaries themselves are accurate.

**Fix (1–2 sentences):** After correcting the EDR/BGS and 2,685-object issues per PAPER-PER-B1, no further change is needed here. You may optionally note that Liang’s method combines an autoencoder with a normalizing flow for probability estimation on BGS galaxies, matching their abstract.[1]


## PAPER-PER-n1 — ADS rate-limit handling (nit)

**Location:** Citations to Munchmeyer et al. 2019.

**Issue:** The ADS page for Munchmeyer et al. 2019 (“Constraining local non-Gaussianities with kSZ tomography”, Phys. Rev. D 100, 083508) is real, but the ADS API returns a rate-limit error, so you should rely on the known arXiv/PhysRev metadata rather than ADS content.[5] There’s no evidence of wrong title or authors in your current text, but the source you’re implicitly using (ADS) didn’t actually provide details.

**Fix (1–2 sentences):** Double-check the Munchmeyer et al. 2019 bibliographic entry against arxiv.org or the Phys. Rev. D site before final submission, to ensure the title, journal (Phys. Rev. D 100, 083508), year, and arXiv:1810.13424 are correct.[5] No textual change is required if that check passes.
