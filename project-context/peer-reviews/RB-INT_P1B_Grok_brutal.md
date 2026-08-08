# P1B RB-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=1cb9ff66 pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 171.6s

---

**Referee Report (Adversarial Review — PRD Standards)**

**Paper:** P1B — Technical Verification Companion to the ECH Spin-Torsion Program  
**Journal target:** Physical Review D (high bar)  
**Round context:** RB-INT (rigorous)

### ESSENTIAL Findings (paper cannot be accepted without fixes)

**P1B-E1**  
**Section:** Abstract / p. 1 (title page)  
**Problem:** Abstract states “Both frozen dataset combinations find ΔN_eff consistent with zero (−0.020 ± 0.169 full-tension; +0.058 ± 0.179 Planck+BAO+SN)”. The quoted values are taken from the truncated posterior after the physical restriction ΔN_eff ≥ 0 is imposed (see p. 4, footnote 1 and §III). The two-sided means are therefore not the direct MCMC output; the paper never shows the unrestricted two-sided posterior means that would be required for a fair null-consistency statement.  
**Required fix:** Replace the quoted numbers with the actual unrestricted posterior means (or explicitly state that the quoted values are post-processed one-sided quantities) and recompute the headline statement.

**P1B-E2**  
**Section:** I. Introduction, p. 2 and throughout  
**Problem:** The entire argument is not self-contained. Every load-bearing claim (“thirteen mechanism-class structural barriers”, “perturbation-transparency theorem”, “f_NL = −35/8”, “four independent minimal-ECH dark-energy routes”) is imported by citation to the unseen companion Paper I(a). No standalone reader can evaluate the scope statements or the “no-go” result.  
**Required fix:** Either (a) make the present manuscript self-contained for the three verification analyses it actually performs, or (b) withdraw it as a methods appendix rather than a companion paper.

**P1B-E3**  
**Section:** III (p. 3–4) and Table I caption  
**Problem:** The paper repeatedly juxtaposes the headline 3.6σ H_0 tension (Planck+BAO+SN) with the proxy-run H_0 = 67.68 ± 1.06 without ever stating that the two numbers are not directly comparable because the proxy run uses a different likelihood combination and an artificial ΔN_eff prior. The “not directly comparable” qualifier appears only in footnotes and scope notes, not at every juxtaposition required by PRD statistical standards.  
**Required fix:** Insert an explicit, prominent statement at every location where the two numbers appear side-by-side.

**P1B-E4**  
**Section:** VI (p. 13–15) and Fig. 4  
**Problem:** The spectator-ALP “consistency check” is performed inside a scan-prior box that already forces the model to accommodate the observed β ≈ 0.27° (C_αγ = 8, θ_i ≲ 0.1). The posterior therefore cannot be used to claim that the data are “consistent with” the model; the model was tuned to be consistent by construction. The paper acknowledges this only in fine print (fn. 6, “not a distinctive ECH prediction”).  
**Required fix:** Remove all language implying a successful consistency test; reframe strictly as an existence proof that a tuned spectator ALP can reproduce the central value.

### MAJOR Findings

**P1B-M1**  
**Section:** II (p. 3) and Table I  
**Problem:** The paper claims the ΔN_eff extension “does not reduce the residual ~3.6σ tension”. The actual shift is only 0.1–0.2σ (67.68 vs 67.78). No effect-size or practical-significance statement is supplied for this null result.

**P1B-M2**  
**Section:** IV (p. 8–11) and Fig. 3  
**Problem:** The NaMaster pipeline-recovery bias (worst-case |Δβ̂| = 0.040°) is presented as a methodological cross-check. The figure caption and text never state that this bias is already comparable to the entire published ACT DR6 uncertainty (0.074°). The test therefore demonstrates that the pipeline systematic is not negligible relative to the measurement precision.

**P1B-M3**  
**Section:** V.B (p. 12) and Table II  
**Problem:** The w_0w_a chain is overlap-uncorrected. The paper correctly flags this as a caveat but still reports posterior means and widths as if they were usable. No quantitative estimate of the bias induced by the ~20 % shared-event overlap is provided.

**P1B-M4**  
**Section:** Data Availability (p. 18)  
**Problem:** The reproducibility manifest lists commit hashes and HuggingFace URLs that pre-date the stated paper version (v1B.0.83). Several artifact descriptions (mask definitions, burn-in fractions, exact likelihood block names) are inconsistent with the YAMLS reproduced in the text.

### MINOR / NIT Findings (selected)

**P1B-N1** Future date “June 29, 2026” on title page.  
**P1B-N2** Duplicate phrasing “canonical canonical-mask” (p. 11).  
**P1B-N3** Multiple scope-statement paragraphs that read like internal review notes rather than journal prose.  
**P1B-N4** Table IV reports “indicative only” for the strict θ_i ≤ 0.1 sliver while still quoting a median; this is internally inconsistent.

### Summary recommendation

**REJECT**

The manuscript fails the standalone-reader test at the most basic level: its central scientific claims cannot be evaluated without the unseen companion Paper I(a). In addition, the headline statistical statements in the abstract are not reproducible from the displayed posteriors once the physical restrictions and overlap systematics are taken into account. The three “verification” analyses are so heavily caveated that they constitute null or existence results rather than positive support for the ECH framework. These are not cosmetic issues; they are structural. The paper would require a complete rewrite to meet PRD standards for a methods or companion article.