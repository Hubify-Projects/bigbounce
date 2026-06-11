# EXT4 P2 — ChatGPT Pro Extended (in-thread delta round 4)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d
**PDF**: paper2_fnl_forecast_v1.7.53.pdf (ecf2f6fe) · harvested 2026-06-11 15:53 PT
---
Referee report on Paper 2 v1.7.53

Updated recommendation: MAJOR REVISIONS, narrowly.

The paper moved toward publishability since v1.7.52. The stale-significance figures are essentially fixed, the 2.6–5σ headline is now mostly consistent across the manuscript, the GR-systematics attribution is much safer, and Li −35/16 is now mostly demoted to a non-physical single-time-ordering stress test. I would still not recommend publication without revision because two central issues remain: the null-space uncertainty is still over-promoted as a physical systematic while not actually propagated into the all-combined lower endpoint, and Appendix A still contains a residual convention-scaling error in its summary prose.

1. Closure verification
A. Closure of my v1.7.52 blockers/majors
Prior finding	Status	Verification
NB1. Figures still communicated stale/uncorrected significance numbers	CLOSED	Fig. 2 now uses the template-corrected 2.6–5σ values and explicitly labels the naive 6.25σ value as not used in any headline; Fig. 5 now labels the SPHEREx curve as “5.2 template-corrected.” The rendered Fig. 5 title contains the minus sign; any extracted “+35/8” reading is a PDF-text artefact, not a visible plot error. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


NB2. Residual >3σ conservative claim after 2.6σ rebooking	CLOSED	The main text now distinguishes the GR-only 2.98σ≈3.0σ point from the all-combined 2.6–2.8σ endpoint, and the headline range is consistently given as 2.6–5σ. 

paper2_fnl_forecast_v1.7.53


NM1. Bayes-factor prior still treated Li −35/16 as live theory ambiguity	CLOSED	The current §VI says the Li value is not part of the physical uncertainty budget and is tracked only as an operator-algebra stress test. Table II still shows where it lies relative to the Gaussian prior, but this is now explicitly a stress test rather than a prior-width motivation. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


NM2. Appendix A c-normalization scaling error	PARTIAL / REGRESSION REMNANT	Appendix A.2 now correctly says that, at fixed physical bispectrum, both f
NL
	​

 and σ(f
NL
	​

) scale as 1/c. However, the earlier Appendix A summary still says more generally that σ(f
NL
	​

) scales inversely with c while f
NL
	​

 scales with c, which is the old wrong statement. This is a small but central convention error because Appendix A is the normalization audit. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


NM3. GR-degradation calibration unsupported / should be demoted	CLOSED	The revised text now says σ
GR
	​

∈[0,1] is an internal stress-test amplitude, motivated by but not directly translated from Addis et al.; it correctly states that Addis et al. discuss biases from neglecting relativistic effects rather than a SPHEREx σ(f
NL
	​

) degradation table. The external Addis abstract supports the bias framing: about 3σ for Euclid-like Hα, about 20σ for MegaMapper-like LBG, and 15–20% bright/faint improvement. 

paper2_fnl_forecast_v1.7.53

 
arXiv

NM4. Conclusion still quoted r→1 Bayes-factor endpoint as headline	CLOSED	The abstract and §VI now consistently present BF≃9–14 under the noise-weighted r≃0.84 bookkeeping, with BF≃10–17 retained as the r→1 endpoint. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

B. Carry-forward closure of the original v1.7.48 BLOCKERS / MAJORS
Original item	Status	Verification
B1. Cai/Li factor-of-two closure not demonstrated	PARTIAL	Much improved. Appendix A now gives an explicit in-in operator-algebra derivation of the −2Im doubling and labels Li −35/16 as a single-time-ordering stress test, not a physical branch. But the paper still admits it does not independently rederive the full four-vertex bispectrum integral, and the remaining c-scaling sentence weakens the normalization audit. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


B2. Polynomial null-space treated as physical uncertainty	PARTIAL	The manuscript now discloses basis-dependence much more clearly, but it still calls the null space a “genuine theory-modeling ambiguity” even though the underdetermination arises in the authors’ recompiled symmetrized basis and the coefficients are fixed from only three benchmark values after a claimed full-rank transformation. This remains overinterpreted. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


B3. r≃0.84 not a SPHEREx cross-Fisher response	CLOSED	The paper now consistently calls the result a sensitivity recast and says r is applied as a shape-weighted degradation to Heinrich et al., not recomputed as an independent cross-Fisher matrix. 

paper2_fnl_forecast_v1.7.53


B4. Post-systematic 3–5σ headline unsupported	PARTIAL	The old overclaim is fixed: the realistic headline is now 2.6–5σ, with the GR-only and all-combined arithmetic shown. Remaining issue: the paper says the systematic budget includes null-space scatter, but the all-combined lower endpoint appears to use central r, not the lower null-space percentile combined with GR and b
ϕ
	​

. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


B5. GR-degradation model not supported by cited source	CLOSED	The manuscript now treats σ
GR
	​

 as an internal stress test and does not claim a direct Addis-to-SPHEREx degradation calibration. 

paper2_fnl_forecast_v1.7.53


M1. Forecast vs recast framing	CLOSED	Title, abstract, and §IV are now consistently recast-framed.
M2. “Parameter-free” overclaim	CLOSED	The paper now uses “minimally parameterized” and lists the assumptions, including cubic transfer and scalar-only restrictions. 

paper2_fnl_forecast_v1.7.53


M3. Bayes factors too prominent / prior dominated	CLOSED enough	The paper now labels the Bayes factors illustrative, uses BF≃9–14 as the noise-weighted headline, and clearly reports prior sensitivity. 

paper2_fnl_forecast_v1.7.53


M4. Cubic transfer caveat central	CLOSED	The abstract and assumptions section now state that third-order bounce transmission is assumed and verified only indirectly. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53


M5. Heinrich σ(f
NL
	​

)=0.7 citation/use	CLOSED	The manuscript uses the Heinrich et al. value as an external baseline and does not claim an independent Fisher forecast. 

paper2_fnl_forecast_v1.7.53


M6. Anomaly-tracer material distracts	PARTIAL	It is now explicitly caveated and excluded from the headline, but it remains long and tangential for a recast paper. 

paper2_fnl_forecast_v1.7.53


M7. Joint (f
NL
	​

,n
f
NL
	​

	​

) SDB section too prominent	PARTIAL / science mostly closed	Scientifically, the section is now safe: it clearly says the SDB joint channel gives only 1.4σ to 0.6σ after n
f
NL
	​

	​

 marginalization and is subordinate to the bispectrum headline. It is still overlong for the main text. 

paper2_fnl_forecast_v1.7.53


M8. Birefringence off-topic	CLOSED	No remaining scientific concern in this version.
2. Fresh pass on v1.7.53 — new findings only
New BLOCKERS

None. The manuscript no longer has a fresh publication-blocking error of the sort that would force rejection or a complete reframing. The remaining problems are major-revision items because they affect the credibility of the headline error budget and the convention audit.

New MAJORS
FM1. The headline budget says it includes null-space scatter, but the lower endpoint does not propagate it

Location: Abstract p.1; §II.A pp.4–5; §IV pp.9–10.

Problem: The abstract lists “polynomial-null-space scatter ±0.13 in r” as part of the systematic budget leading to the realistic 2.6–5σ range. But §II shows that the 16th-percentile null-space draw gives 4.4σ pre-systematics and 2.5σ after GR-only marginalization; §IV’s all-combined 2.6–2.8σ endpoint appears to use the central r≃0.83 with widened b
ϕ
	​

+GR, not the lower null-space percentile combined with widened b
ϕ
	​

+GR. If the lower r percentile is also combined with the widened b
ϕ
	​

 endpoint, the floor would fall below 2.6σ. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

Proposed fix: Add a compact “budget arithmetic” table with rows for central r, 16th-percentile r, and 84th-percentile r, and columns for baseline, +GR, +b
ϕ
	​

, and +GR+b
ϕ
	​

. Then either revise the headline to the true all-combined lower percentile or explicitly state that the 2.6–5σ headline uses central r, while null-space excursions are reported separately and not folded into the headline floor.

FM2. Appendix A still contains a convention-scaling contradiction

Location: Appendix A summary p.22; Appendix A.2 p.24.

Problem: A.2 correctly states that under a consistent change of Komatsu–Spergel constant c, both f
NL
	​

 and σ(f
NL
	​

) scale as 1/c. But the earlier Appendix A summary still says f
NL
	​

 scales with c, which is wrong for fixed physical bispectrum B=cf
NL
	​

P
2
. This is a small textual remnant, but it sits inside the paper’s central convention audit. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

Proposed fix: Replace the p.22 sentence with: “Under a consistent change of c at fixed physical bispectrum, both f
NL
	​

 and σ(f
NL
	​

) scale as 1/c, so ∣f
NL
	​

∣/σ(f
NL
	​

) is invariant.” Then grep the source for “scales with c” and remove all instances of the old statement.

FM3. The null-space “genuine theory-modeling ambiguity” language remains too strong

Location: §II.A pp.3–4 and footnote 1.

Problem: The current text is transparent, but the logic remains unsatisfactory. It says the six-monomial expansion is this paper’s symmetrization choice, not Cai et al.’s; that Cai’s derivation itself fixes the redundancy; that the transformation matrix is full rank; and that the authors nevertheless fix coefficients from three benchmark values because direct transplantation fails. That is not enough to elevate the resulting three-dimensional null space to a physical theory ambiguity. It is better described as an internal representation/surrogate uncertainty unless the authors provide the explicit mapped polynomial. 

paper2_fnl_forecast_v1.7.53

 

paper2_fnl_forecast_v1.7.53

Proposed fix: Downgrade “genuine theory-modeling ambiguity” to “basis-dependent representation uncertainty in our doubled symmetrized implementation.” Alternatively, supply the full symbolic map from Cai’s printed expression to the authors’ basis and show why the physical polynomial remains non-unique despite the claimed full-rank transformation.

New MINORS

Abstract length and density, p.1–2. The revised abstract is scientifically much safer, but it is still far too long and reads like an executive summary. A journal abstract should not include the full Bayes-factor grid, the Li stress-test paragraph, and multiple caveat chains.

MegaMapper wording, §V p.10. The text says MegaMapper ranges from 7.4–7.7σ ideal to 2.6–5σ after applying the same systematic budget as SPHEREx, while the abstract quotes 3–7σ. This is not wrong, but it is easy to misread. Say explicitly that 2.6–5σ is the SPHEREx-budget transplant and 3–7σ is the adopted design-uncertainty envelope.

Li stress-test language, Appendix A.2 p.24. The phrase “worst-case lower bound” is acceptable only if immediately paired with “non-physical single-time-ordering stress test.” Keep that pairing every time; otherwise readers will again treat it as a live branch.

Anomaly-tracer discussion, §IV p.9–10. The caveats are now adequate, but the material is still tangential. Move it to a future-work paragraph unless the shot-noise-corrected Fisher calculation is included.

SDB running section, §IX.D p.19–20. Scientifically fixed, but too long. The main text only needs the headline: SDB joint running is a subordinate cross-check, not competitive with the bispectrum forecast. Move the detailed covariance/degeneracy arithmetic to an appendix.

3. Updated recommendation

Recommendation: MAJOR REVISIONS.

This version is substantially closer to publishable than v1.7.52, but I would still require revision before acceptance because the central headline budget must consistently propagate the null-space scatter it claims to include, and Appendix A must remove the remaining c-scaling contradiction.
