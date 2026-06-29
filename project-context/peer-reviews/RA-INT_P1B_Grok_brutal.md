# P1B RA-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=f2838e5b pages=22
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 100.1s

---

**Referee Report**

**Paper:** Technical Verification Companion to the ECH Spin-Torsion Program… (Houston Golden)

**Journal target:** Phys. Rev. D (high bar for methods/novelty papers)

**Finding classification**

**P1B-E1 (ESSENTIAL)**  
Section I (p. 2) + abstract (p. 1): “Three verification analyses are documented.” The abstract reports load-bearing scalars (ΔN_eff = −0.020 ± 0.169, H_0 = 67.68 ± 1.06, β_NaMaster = 0.238°) without the explicit qualifier that appears in every body scope statement (“NOT a spin-torsion theory module”, “not a distinctive ECH prediction”).  
**Required fix:** Rewrite abstract to match the body’s final calibrated language or remove the scalars.

**P1B-E2 (ESSENTIAL)**  
Abstract (p. 1) vs. §III (p. 3) and Table I (p. 5): The headline ΔN_eff and H_0 numbers are presented as if they test the ECH framework. Body repeatedly states the run uses unmodified stock CAMB with ΔN_eff as a free parameter. No torsion-modified Boltzmann equations are solved.  
**Required fix:** Remove any implication that the MCMC constitutes a test of the ECH spin-torsion sector.

**P1B-E3 (ESSENTIAL)**  
§IV (p. 8–11) + Fig. 3: NaMaster “pipeline recovery” is performed exclusively on synthetic skies containing no galactic foregrounds. The published 2.7–2.9σ birefringence significance is a real-sky measurement. The paper itself states these figures “are not directly comparable.” Yet they are placed side-by-side without the required qualification at every juxtaposition.  
**Required fix:** Either delete the comparison or add the explicit non-comparability statement in every location where the numbers appear together.

**P1B-E4 (ESSENTIAL)**  
§VI (p. 13) + abstract: The spectator-ALP exercise is labeled a “consistency check” and “not a distinctive ECH prediction.” The abstract nevertheless lists it as one of the three headline results of the paper.  
**Required fix:** Remove the ALP result from the abstract or re-title the paper to reflect that it contains no ECH-specific prediction.

**P1B-M1 (MAJOR)**  
Standalone-reader test (entire paper): Dozens of load-bearing statements (“Paper I(a) establishes…”, “the 13 mechanism-class barriers”, f_NL = −35/8, etc.) are imported by citation to a companion manuscript that is not supplied. The argument is not self-contained.  
**Required fix:** Either make the present manuscript self-contained or withdraw it as a companion.

**P1B-M2 (MAJOR)**  
Length vs. contribution (22 pages): The paper is almost entirely negative results (“does not resolve”, “not distinctive”, “not evidence for or against”) plus pipeline-validation figures on synthetic skies. PRD does not publish 22-page technical appendices whose primary conclusion is “our null tests passed and we found nothing new.”

**P1B-M3 (MAJOR)**  
Fig. 1 & Table I (p. 5): The one-sided 95 % upper limits on ΔN_eff are obtained only after post-hoc truncation of the negative tail and re-normalization. The procedure is described in a footnote; the headline numbers in the abstract and Table I do not carry this caveat.

**P1B-M4 (MAJOR)**  
§V.C (p. 12) and Table II: The w_0w_a posterior is reported from an overlap-uncorrected DES-SN5YR × Pantheon+ product likelihood. The paper itself flags this as a known systematic that artificially narrows the contours, yet still presents the numbers in a table without a quantitative correction or a “not for model comparison” label.

**P1B-N1 (MINOR)**  
Future date in header: “Dated: June 28, 2026.” Typographical or archival error.

**P1B-N2 (MINOR)**  
Multiple instances of “canonical canonical-mask” phrasing and repeated scope-statement boilerplate that could be condensed.

**P1B-NIT-1**  
Minor axis-label and caption inconsistencies in Fig. 3 (recovered β vs. injected β) that do not affect conclusions.

**Summary recommendation: REJECT**

The manuscript is a conscientiously scoped technical verification exercise whose central findings are null results and whose positive content consists of (a) an unmodified-CAMB MCMC proxy that the authors themselves state does not test the ECH sector and (b) a synthetic-sky pipeline test whose numbers are explicitly declared non-comparable to the published sky measurements. After the essential scope, self-containment, and abstract–body mismatches are corrected, the remaining contribution does not meet the novelty or significance threshold of Physical Review D.