# EXT Review — P3 × Gemini
- paper: P3
- version: v3.1.137
- reviewer: Gemini
- model: 3 Pro (Ultra)
- timestamp: 2026-07-06T19:06:59Z
- chat_url: https://gemini.google.com/u/1/app/a17b38854888f160
- pdf: /tmp/round_P3.pdf

## Raw verbatim response

VERDICT: MAJOR REVISIONS

ISSUES:

[MAJOR] Journal Scope and Cosmological Claims (Section V): The manuscript devotes the vast majority of its length to astronomical anomaly catalog generation and pipeline debugging (e.g., the "Path-C rebuild" ). The cosmological applications are explicitly stated to be "secondary methodological demonstrations" that yield no statistically significant improvement on f
NL
	​

 bounds. For Physical Review D, the primary focus must be fundamental physics or cosmology. The authors must either significantly expand the cosmological constraint analysis to yield robust, new physical results, or transfer the manuscript to a catalog/observational astronomy journal (e.g., ApJS, MNRAS).  
PDF
+ 4

[MAJOR] Irreproducible Scoring Axis for eROSITA (Section III E): The authors admit that the eROSITA anomaly threshold of 0.259 cannot be reconciled with any committed scoring axis, suggesting an undocumented post-hoc rescaling. Releasing a fixed top-298 list as a workaround  is unacceptable for a validated pipeline. The scoring must be mathematically reproducible from the raw model outputs.  
PDF
+ 3

[MAJOR] Inclusion of Failed/Artifact Tiers (Sections III D, III F, Appendix F): The manuscript includes extensive discussions of failed cross-transfer pipelines, such as the LAMOST 98% blue-excess training artifact and the quarantined ACT DR6 results. While valuable as internal "methodological lessons", these sections read like a post-mortem laboratory notebook. The manuscript should be streamlined to present only the validated, functional scientific products.  
PDF
+ 4

[MINOR] Overstated SIMBAD-Unmatched Fractions (Section IV A): The headline claims of high SIMBAD-unmatched fractions (e.g., 99% for DESI ) are later admitted to overstate true catalog novelty because SIMBAD does not index most wide-field photometric detections. This metric should be de-emphasized in favor of the more accurate 17.8% genuine novelty fraction derived from the 18-catalog cross-match.  
PDF
+ 4

[MINOR] SMBHB Environmental Caveat (Section V A): The Bayes factor of 7.14×10
3
 favoring the matter-bounce model over SMBHB is decisive only against an idealized circular-orbit reference of γ=4.33. Since environmentally modified SMBHB models can produce γ∼2.5−3 , the text should more prominently reflect that this does not constitute a detection of a cosmological gravitational wave background.  
PDF
+ 4

CENTRAL CLAIM SUMMARY:
The central claim of providing a validated, multi-survey anomaly catalog is supported by the extensive data processing and injection-recovery testing , but the secondary cosmological claims are, by the authors' own admission, purely demonstrative and do not advance current physical constraints.  
PDF
+ 4
