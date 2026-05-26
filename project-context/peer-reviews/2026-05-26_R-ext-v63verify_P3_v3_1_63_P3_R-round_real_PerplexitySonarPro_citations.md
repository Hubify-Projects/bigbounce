# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v63verify_P3_v3_1_63
**Wall time**: 29.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=69004, completion=1589, total=70593

---

## Finding 1 — PAPER-FNL-HEINRICH (MAJOR)

Heinrich et al. citation claims: “Heinrich+2024 σ_fNL ≈ 0.7 bispectrum-only forecast; internal Fisher σ_fNL ≈ 0.07–0.12 is 3–10× tighter than Munchmeyer et al. σ_fNL ≈ 0.4–0.9 for SPHEREx-class surveys.”  
Issue: Heinrich et al. (arXiv:2311.xxxx) and Munchmeyer et al. (arXiv:1810.13424) are not present in the provided text or checked sources; only Doré et al. 2014 (SPHEREx white paper) is verifiable, and it does not state those specific σ_fNL numbers or ratios.  The paper attributes specific σ_fNL values and a “consensus” range to named works that have not been explicitly verified and may be misremembered or fused from multiple forecasts.  
Fix: Replace the explicit “Heinrich+2024 σ_fNL ≈ 0.7” and “Münchmeyer et al. σ_fNL ≈ 0.4–0.9” numerical claims with a softer, sourced summary tied directly to Doré et al. 2014 and whichever exact arXiv IDs you have checked, or add the correct Heinrich/Münchmeyer references and re-derive the quoted numbers from those papers.

---

## Finding 2 — PAPER-LIANG-ARXIV-ID (nit)

Location: Introduction, Liang et al. citation; also abstract’s 141× comparison.  
Issue: The paper cites “Liang et al. 2023” without an explicit arXiv ID; the correct paper is “Outlier Detection in the DESI Bright Galaxy Survey” (arXiv:2307.07664) with 2,685 BGS outliers from DESI EDR.  The description “DESI Early Data Release (EDR) spectra, finding 2,685 anomalies at a 1.07% rate” is consistent with the abstract, but adding the ID would remove ambiguity and ensure non-fused metadata.   
Fix: In the bibliography, set Liang et al. to the exact title and ID “Outlier Detection in the DESI Bright Galaxy Survey, arXiv:2307.07664 (astro-ph.GA)” and confirm that all text referring to 2,685 anomalies and ~1% rate explicitly mentions “Bright Galaxy Survey (BGS) in DESI EDR” to match the paper.

---

## Finding 3 — PAPER-SPHEREX-TITLE+ID (nit)

Location: Introduction, SPHEREx reference; multiple mentions of “SPHEREx 2014”.  
Issue: The SPHEREx reference is described generically (“SPHEREx satellite”) but the correct, citable paper is “Cosmology with the SPHEREX All-Sky Spectral Survey” (Doré et al., arXiv:1412.4872).  The text’s description of SPHEREx as an all-sky spectroscopic survey for cosmology and galaxy/ice science matches Doré et al., but the title and arXiv ID are not spelled out; that’s formally incomplete rather than wrong.   
Fix: In the references, give the full title and arXiv:1412.4872 for Doré et al., and in the body ensure that when “SPHEREx 2014” is quoted as the forecast anchor, it explicitly points to Doré et al. (2015, arXiv:1412.4872).

---

## Finding 4 — PAPER-SPHEREX-σFNL-RANGE (MAJOR)

Location: Introduction and §5 cosmology; claims that SPHEREx-class surveys have “σ_fNL ≈ 0.4–0.9” consensus range from Munchmeyer et al., and that internal Fisher gives σ_fNL ≈ 0.07–0.12 “3–10× tighter than the consensus.”  
Issue: Doré et al. 2014 give projected SPHEREx σ_fNL of order unity but not the specific 0.4–0.9 band, and our fetched reference (Vlah et al. 2016, arXiv:1509.02120) is unrelated; Munchmeyer et al. is not among the checked URLs, so the claimed “consensus” band and the factor-of-3–10 tightening are not directly traceable to verified sources.  This is likely approximate but currently unsupported by the specific citations listed.  
Fix: Either (a) verify Munchmeyer et al. directly and adjust the quoted 0.4–0.9 range to match their exact SPHEREx-class numbers, or (b) restate this as “our internal Fisher is significantly tighter than typical SPHEREx-class σ_fNL ~ O(1) forecasts (e.g. Doré et al. 2014)” without giving a numerical factor unless it can be tied to a checked paper.

---

## Finding 5 — PAPER-MIXED-BOUNCING-CITATIONS (minor)

Location: Introduction and cosmology sections: Wands 2010, Cai 2009, Wilson–Ewing 2012.  
Issue: The text attributes f_NL = −35/8 to the “quasi-matter bounce model” citing Wands 2010, Cai 2009, Wilson–Ewing 2012. Wands (2010) is a review on local non-Gaussianity in inflation, not a bounce-model paper; Cai et al. 2009 and Wilson–Ewing 2012 are bounce-specific.  Using Wands as part of the triad for that specific numerical prediction is a mild fusion of roles (review vs. model-derivation references).  
Fix: Keep Wands 2010 as a general-local-NG citation but restrict the explicit f_NL = −35/8 attribution to Cai et al. and Wilson–Ewing (or whichever bounce papers actually derive it), clarifying in-text that Wands is cited for background on local non-Gaussianity, not for the matter-bounce value itself.

---

## Finding 6 — PAPER-CROSS-CHECKED-ARXIVS (nit, positive confirmation)

Location: All mentions of Liang 2023 and SPHEREx white paper.  
Issue: Potential concern about confabulated titles / IDs is alleviated: “Outlier Detection in the DESI Bright Galaxy Survey” (Liang et al., arXiv:2307.07664) and “Cosmology with the SPHEREX All-Sky Spectral Survey” (Doré et al., arXiv:1412.4872) are real and correctly described: an autoencoder+normalizing-flow DESI-BGS outlier search and a SPHEREx cosmology white paper respectively.  No fused metadata (e.g., wrong title attached to an ID) is evident for these two key references.  
Fix: No change needed beyond tightening the references as in Findings 2–3; you can explicitly note in your internal log that these core citations are cleanly matched to real arXiv entries.

---

If you want a follow-up pass, which single block of cosmology text (e.g., the NANOGrav section vs. the f_NL section) should I target for line-by-line citation sanity checks next? 


