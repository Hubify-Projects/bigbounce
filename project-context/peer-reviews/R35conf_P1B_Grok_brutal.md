# P1B R35conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.61.pdf` md5=56ec3f27 pages=19
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 76.7s

---

**Referee Report**

**P1B-E1** (ESSENTIAL)  
**Section:** Title + first paragraph (p. 1)  
**Problem:** The opening summary paragraph (functioning as abstract) states “the data prefer an extra radiation-like degree of freedom” and quotes specific posteriors (−0.020 ± 0.169, +0.058 ± 0.179) while the body repeatedly qualifies the identical run as “Not a spin-torsion theory module” and “generic radiation-proxy test.” The abstract claim is therefore stronger than, and ordered differently from, the body’s final calibrated statement.  
**Required fix:** Rewrite the summary paragraph to match the body’s explicit scope limitations verbatim; add the sentence “This run does not test the ECH spin-torsion sector” at the head of the abstract.

**P1B-E2** (ESSENTIAL)  
**Section:** I (p. 2) and throughout  
**Problem:** The paper is not self-contained. Every load-bearing claim about what is being verified (“ECH structural-closure no-go result,” “14 independent structural constraints”) is imported by citation to “Paper I(a)” whose arXiv ID is never given. A standalone reader cannot evaluate the verification without the companion.  
**Required fix:** Either embed the minimal necessary definitions and equations from Paper I(a) or withdraw the manuscript as a companion note.

**P1B-E3** (ESSENTIAL)  
**Section:** Abstract (p. 1) and §III (p. 3)  
**Problem:** The quoted 3.6σ WMAP+Planck birefringence value (0.342° ± 0.094°) is presented side-by-side with the pipeline-recovered 0.238° without the explicit qualifier “not directly comparable” that the body itself demands for other null tests. This violates the rule on juxtaposed σ values from different procedures.  
**Required fix:** Insert the qualifier at every such juxtaposition or remove the published 3.6σ number from the abstract.

**P1B-M1** (MAJOR)  
**Section:** §III (p. 3–4) and Table I (p. 17)  
**Problem:** The central claim that “the ΔN_eff extension alone does not resolve the Hubble tension” rests on a two-sided posterior (−0.020 ± 0.169) while the physically motivated one-sided limit ΔN_eff ≥ 0 is only mentioned in a footnote. The quantitative statement required by the one-sided 95 % upper limit is absent.  
**Required fix:** Report the one-sided 95 % upper limit explicitly and recompute all tension statements with it.

**P1B-M2** (MAJOR)  
**Section:** §VI (p. 9–11) and Fig. 4 (p. 12)  
**Problem:** The spectator-ALP “consistency check” requires a ~25× fine-tuning of the misalignment angle (θ_i ≪ 1) that is acknowledged only in footnotes. The headline statement “consistent with the published 3.6σ joint signal” therefore omits the dominant fine-tuning cost.  
**Required fix:** Move the fine-tuning requirement into the main text and qualify every consistency claim with it.

**P1B-M3** (MAJOR)  
**Section:** Data Availability (p. 13)  
**Problem:** The reproducibility section lists commit hashes and HuggingFace URLs but contains no frozen-release DOI or SHA256 manifest for the exact 309 189-sample chains used in Table I. The stated “v1B.0.61” stamp post-dates some of the archived chain directories.  
**Required fix:** Provide a single frozen DOI or tarball with manifest that exactly reproduces the numbers in Tables I–IV.

**P1B-N1** (MINOR)  
**Section:** Multiple scope statements (pp. 2, 3, 5, 9)  
**Problem:** The phrase “Not a spin-torsion theory module” (or close variants) appears at least six times. This is repetitive and dilutes the narrative.  
**Required fix:** Consolidate into a single, prominent scope paragraph.

**P1B-N2** (NIT)  
**Section:** Fig. 1 caption (p. 6)  
**Problem:** Axis labels use “ΔN_eff” while the text sometimes writes “N_eff”; minor notation inconsistency.  
**Required fix:** Standardize.

**Additional observations**  
- The 19-page length for a pure verification note exceeds typical PRD technical-note practice; a 6–8 page letter or companion note would be more appropriate.  
- No effect-size or practical-significance statement accompanies the headline χ² or σ values.  
- All quantitative claims in the abstract were successfully traced to the body after the above corrections; no untraceable scalars remain.

## Summary recommendation
**REJECT**

The manuscript is a narrowly scoped technical verification note whose central results are either null or explicitly “not tests” of the theory it claims to support. It cannot stand alone, relies on an unpublished companion for every substantive claim, and contains multiple instances of abstract–body mismatch and missing quantitative caveats. These are not cosmetic deficiencies; they place the work below the threshold for Physical Review D.