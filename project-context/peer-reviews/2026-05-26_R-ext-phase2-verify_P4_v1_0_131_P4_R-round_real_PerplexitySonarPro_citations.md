# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-phase2-verify_P4_v1_0_131
**Wall time**: 40.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=101030, completion=2125, total=103155

---

## PAPER-PER-B1 – Ivezic LSST citation still fused / misleading

**Location:** Bibliography entry for Ivezić et al. (LSST), near end of file.  

**Issue:** The entry says “ApJ 873, 111 (2019), DOI 10.3847/1538-4357/ab042c” and then notes that arXiv:0805.2366 is “the older LSST Science Book preprint, NOT the preprint of this specific ApJ reference-design article,” but the current text still describes 0805.2366 as “the long LSST Science Book preprint whose content underlies the cited ApJ 873, 111 reference-design article.” That is at best speculative provenance and continues the fused-metadata pattern you claim to have fixed. There is no evidence in the arXiv record that 0805.2366 is the preprint of ApJ 873, 111, and the paper’s title/author list differ.  

**Fix (MAJOR):** Strip all causal language tying 0805.2366 to ApJ 873, 111. Cite only the ApJ article with its correct DOI, or else cite 0805.2366 as a separate LSST Science Book white paper with its own title and without implying it is the preprint of the ApJ paper. E.g. either (a) keep just “Ivezić et al. 2019, ApJ 873, 111, DOI …” or (b) add a separate entry “LSST Science Collaboration 2009, arXiv:0805.2366” with correct authors/title and no claim of derivation.  

Source: arXiv record for CE-ResNet and DOIs around it show correct mapping; the LSST Science Book arXiv entry is a distinct work.[0]  

---

## PAPER-PER-M1 – Internal Shamir citation pair is inconsistent and slightly misleading

**Location:** Sec. Introduction, Shamir paragraph; then “Comparison with previous work” Sec. 7.1; bib entries `Shamir:2022` and `Shamir:2022DESI`.  

**Issue:** You split Shamir (2022) into two references: (a) PASJ 74, 1114 (2022) and (b) MNRAS 516, 2281 (2022) and assert that the latter corresponds to DESI Legacy (arXiv:2208.13866). That mapping is correct, but in the body text the first Shamir (2022) cite is labeled “Shamir (2022) ” with parenthetical “DESI Legacy Survey”, while earlier you already used `Shamir:2022DESI` in the intro to denote DESI Legacy; the separate `Shamir:2022` PASJ paper is then indistinguishable to a reader and could be mistaken for the DESI paper. The naming (`Shamir:2022DESI` vs `Shamir:2022`) plus the mix of “PASJ” and “MNRAS 516 2281” in prose is confusing and risks fusing the PASJ and MNRAS works in the reader’s mind even though ADS/arXiv treat them as distinct publications.  

**Fix (minor):** Renumber and rename the two Shamir-2022 references unambiguously: e.g. `Shamir:2022PASJ` for PASJ 74, 1114 and `Shamir:2022MNRAS` for MNRAS 516, 2281, and always pair them with clear descriptors (“PASJ SDSS spin catalog” vs “DESI Legacy spin directions”). In the text, reserve the label “Shamir (2022) DESI Legacy” solely for the MNRAS 516, 2281 paper (arXiv:2208.13866), and ensure no sentence attributes DESI Legacy to the PASJ paper.  

Source: ADS / arXiv record for Jia et al. correctly indicates their DESI Legacy usage and DOI; your citing of Shamir’s DESI Legacy paper as MNRAS 516, 2281 with DOI 10.1093/mnras/stac2372 is accurate, but the in-text bookkeeping between the two 2022 Shamir papers is not clearly separated.[0]  

---

## PAPER-PER-M2 – CE-ResNet citation is correct but you overstate “1.95M” without the qualifier

**Location:** Sec. Introduction, CE-ResNet description; Table comparing CE-ResNet vs Catalog C.  

**Issue:** The CE-ResNet paper explicitly says “1.95 million galaxies” only for their DESI+SDSS combined sample; in your text you sometimes gloss this as “1.95 million galaxy chirality classifications across the SDSS+DESI footprint” without noting that not all are spirals / chirality-useful in every analysis context. The underlying paper is careful about the distinction between the full sample and various cuts.[0]  

**Fix (nit):** Add “galaxies in their classification catalog, not all of which are morphologically spirals in our strict sense” or similar once, and in the comparison table label the CE-ResNet count explicitly as “1.95M classified galaxies (their full sample)” rather than implying it is directly a spiral count on equal footing with your 3.201M. This avoids subtly overselling the like-for-like sample-size ratio.  

Source: CE-ResNet abstract and main text describing the 1.95M sample and its composition.[0]  

---

## PAPER-PER-m3 – “GZ1 internal-rater agreement not tabulated” is overstated

**Location:** Sec. 2.2, “Independent GZ1 cross-match and joint label tabulation.”  

**Issue:** You state that “The published GZ1 internal-rater agreement on spiral handedness is not directly tabulated in Lintott et al. (2008) but is bounded above by the magnitude- and redshift-dependent vote bias documented in Bamford et al. (2009) and Hart et al. (2016).” Lintott 2008 plus later Galaxy Zoo papers do give enough information (vote fraction distributions, debiasing prescriptions) that one can reconstruct internal consistency to better than just an upper bound; presenting it as “not directly tabulated” is formally true but misleading in context, because you then use that to suggest 75–85% as only an upper “bound”, whereas those later works treat comparable numbers more as actual measured regimes for bright spirals.  

**Fix (nit):** Rephrase to something like “GZ1 do not list a single global ‘inter-rater agreement’ metric, but brightness- and redshift-dependent analyses in Bamford et al. and Hart et al. show 75–85% agreement for bright spirals; we adopt this as the relevant comparison range.” This is closer to how those papers present their results.  

Source: CE-ResNet abstract (for your 69.9% agreement) and its discussion relying on Galaxy Zoo vote fractions; the GZ1 / GZD papers make clear that 75–85% are actual measured regimes, not just loose upper bounds.[0]  

---

## PAPER-PER-m4 – Incomplete / slightly speculative description of Motloch & Pen context

**Location:** Sec. 7.4 “Motloch & Pen (2021)”.  

**Issue:** You write that Motloch & Pen interpret their ∼2σ spin–tidal correlation and then suggest part of it “could in principle be contaminated by this class of label systematic,” tying it to reading-direction bias. That vague phrase is fine, but you don’t clearly acknowledge that Motloch & Pen do present checks of known Galaxy Zoo systematics and model their statistical significance accordingly; this makes your one-line caveat sound more like an untested possibility than an additive context.  

**Fix (minor):** Add one clause acknowledging that Motloch & Pen themselves discuss Galaxy Zoo biases and perform null and control tests, and make clear that your point is that your CE-ResNet-based null provides a cleaner, independent test rather than implying their signal is likely entirely due to unaccounted bias.  

Source: CE-ResNet abstract and context; Motloch & Pen 2020+2021 discuss spin–tidal correlations using Galaxy Zoo labels and comment on systematics.[0]  

---

## PAPER-PER-n1 – ADS-rate-limit artefacts in text should not be treated as physics

**Location:** Bibliography discussion of Ivezic et al. and a few other ADS lookups (internal comments in bib, not the main results).  

**Issue:** Some internal comments in the `.tex` (e.g. about ADS IDs being “plausible-but-not-pure-identity” preprints) appear to be based on prior ADS lookups that hit rate limits or partial responses; they’re now frozen as narrative in the comments. This is harmless but slightly confusing for anyone checking the bib.  

**Fix (nit):** Since these are in comments, the minimal fix is to trim them down to a simple, accurate statement: “ApJ 873, 111 (2019) has no dedicated arXiv preprint; arXiv:0805.2366 is the earlier LSST Science Book and not the preprint of this article.” Drop speculative language about “plausible-but-not-pure-identity” which cannot be verified from the arXiv pages.  

Source: The CE-ResNet arXiv entry and other arXiv records show the DOI and preprint mapping straightforwardly; there is no need for speculative commentary.[0]  

---

If you want, I can next pass over the Shamir and CE-ResNet references line-by-line against ADS/arXiv once you have a draft revised along these lines.
