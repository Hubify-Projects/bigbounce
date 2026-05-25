# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-25_R-ext_P3_v3_1_62
**Wall time**: 31.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68008, completion=1596, total=69604

---

## PAPER-PER-B1 — Mis-citation of Heinrich et al. forecast (astro-ph.C0)

**Grade:** BLOCKER  

**Location:** Introduction, para 2 (cosmology motivation) and §5 / Appendix refs around Heinrich et al.  

**Issue:** The paper attributes a “Heinrich+2024 $\sigma_{f_{\rm NL}}\approx0.7$ bispectrum-only forecast” and uses it as a concrete external benchmark, but the cited work “Heinrich et al. 2023” (arXiv:2311.13082) is a *forecast for SPHEREx using multi-tracer redshift-space bispectrum*, with detailed numbers that depend on survey configuration; there is no widely used standalone “0.7” headline identical to what’s written here, and certainly not as a finalized “2024” reference yet.[1] The combination “Heinrich+2024, σ≈0.7 bispectrum-only” appears to be fused / forecast-number confabulation rather than a verbatim literature claim.  

**Fix (1–2 sentences):** Reword all mentions to say explicitly that you adopt an *illustrative* SPHEREx-class benchmark based on Heinrich et al.’s projected multi-tracer bispectrum sensitivities, quoting the actual forecast range and configuration dependence rather than a single “0.7” headline; clearly label it as “following Heinrich et al. (2023)” rather than “Heinrich+2024” and avoid treating it as an established consensus number.


## PAPER-PER-M1 — Liang et al. prior-catalog comparison framing

**Grade:** MAJOR  

**Location:** Abstract, paragraph describing “Liang et al. (2023)” and 2,685 anomalies; Introduction 2nd paragraph.  

**Issue:** The paper repeatedly states “Liang et al. (2023) ... 2,685 anomalies at a 1.07% rate on ~250,000 DESI EDR spectra”, and uses this as the “largest prior single-survey spectroscopic anomaly catalog.” Liang et al. (arXiv:2307.07664) indeed finds 2,685 outliers in the DESI Bright Galaxy Survey, but the pipeline is not just “autoencoder anomaly detection” in the same sense—it's an AE+normalizing-flow probability model on a *subsample* of EDR BGS galaxies, not “all DESI EDR spectra.”[0] Calling it “largest prior single-survey spectroscopic anomaly catalog” without the BGS restriction and with “DESI EDR spectra” language overstates the scope.  

**Fix:** Tighten the description to “Liang et al. (2023) applied an autoencoder+normalizing-flow outlier search to ~250,000 DESI EDR Bright Galaxy Survey galaxies and found 2,685 outliers (1.07%).” Explicitly mention “BGS subsample of EDR” and adjust the “largest prior catalog” phrasing to “largest prior DESI-BGS spectroscopic anomaly sample” so readers don’t infer a full-EDR, all-target-class baseline.[0]


## PAPER-PER-m1 — Baron & Poznanski reference is correct but under-specified

**Grade:** minor  

**Location:** Introduction, “Baron & Poznanski 2017 demonstrated the approach on SDSS spectra...”  

**Issue:** The reference clearly points to Baron & Poznanski, 2017, MNRAS 465, 4530 “The weirdest SDSS galaxies: results from an outlier detection algorithm” and is conceptually correct (outlier detection on SDSS spectra), but the text implies a general “autoencoder-based” method, whereas Baron & Poznanski used an unsupervised Random Forest, not an autoencoder.[1]  

**Fix:** Adjust the wording to remove “autoencoder-based” from that sentence and instead say “unsupervised outlier detection (using a Random Forest) on SDSS spectra,” keeping autoencoders for later citations that actually used them.


## PAPER-PER-m2 — UMAP citation is accurate but missing full arXiv ID

**Grade:** minor  

**Location:** SDSS section §3.2 (UMAP description) and Appendix galleries.  

**Issue:** The paper cites “McInnes et al. 2018” for UMAP but does not include arXiv ID or journal reference; the canonical reference is “UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction,” arXiv:1802.03426.[2] This is a stylistic/incompleteness issue rather than a mis-citation.  

**Fix:** In the bibliography entry for UMAP, add the full arXiv identifier “arXiv:1802.03426” and, if desired, the 2020 v3 revision date, so that readers can unambiguously locate the exact implementation you used.[2]


## PAPER-PER-n1 — Claims about “all prior anomaly searches” limited to individual surveys

**Grade:** nit  

**Location:** Introduction, end of 2nd paragraph: “However, all prior anomaly searches have been limited to individual surveys at sub-million scale.”  

**Issue:** While the specific references named (Baron & Poznanski, Liang et al., Nicolaou et al.) *are* single-survey studies with sample sizes <1M, the phrase “all prior anomaly searches” is non-literal and could be read as a broad literature claim. There are other anomaly/outlier efforts (including random-forest and isolation-forest style searches) that might not fit neatly into that characterization.  

**Fix:** Soften to “these prior SDSS and DESI anomaly searches have been limited to individual surveys at sub-million scale” or “to our knowledge, previous spectroscopic anomaly searches of this type...” to avoid an absolute universal statement that you are not exhaustively backing up with citations.


## PAPER-PER-n2 — Matter-bounce/non-Gaussianity citations are plausible but thin

**Grade:** nit  

**Location:** Introduction 2nd paragraph and §5/§6.7 where “Wands 2010, Cai:2009fn, Wilson-Ewing 2012” are cited for $\fnl = -35/8$ and quasi-matter bounce.  

**Issue:** The triple-citation cluster looks qualitatively consistent with the matter-bounce literature (Cai et al. 2009 non-Gaussianity in matter bounce; Wilson-Ewing 2013/2012 for loop quantum cosmology; Wands 2010 for local non-Gaussianity review), but the specific value $\fnl = -35/8$ is more precisely derived in Cai et al. (2009) and follow-ups rather than Wands (which is a review).[3] Treating Wands 2010 as a direct source of the exact numeric prediction is slightly sloppy.  

**Fix:** Make Cai et al. (2009) the primary citation for the precise $\fnl = -35/8$ prediction and keep Wands (2010) as a general background review, e.g., “The quasi-matter bounce model predicts a tightly constrained local non-Gaussianity $\fnl = -35/8$ (Cai et al. 2009; see also Wands 2010; Wilson‑Ewing 2012 for related bounce scenarios).”[3]

---


