# EXT5 P2 — ChatGPT Pro Extended (in-thread delta round 5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d
**PDF**: paper2_fnl_forecast_v1.7.55.pdf · harvested 2026-06-12 00:47 PT · state done
---
Referee report on Paper 2 v1.7.55

Updated recommendation: MAJOR REVISIONS, narrowly.

I read the revised v1.7.55 PDF end-to-end, including the figures, appendix, and tables. This version moved toward publishability since v1.7.53: the stale-significance figures are fixed, the c-normalization scaling contradiction in Appendix A is fixed, the 2.6–5σ headline is much more consistently presented, and the GR-projection treatment is now appropriately framed as an internal stress-test grid rather than a direct translation of Addis et al.

The remaining reasons for major revision are concentrated: the polynomial-null-space uncertainty is still over-promoted as a physical/systematic ingredient of the headline budget, and the current-data section is now factually stale because DESI DR1 PNG constraints have appeared.

1. Closure verification against the original BLOCKERS / MAJORS
Original BLOCKERS
Original item	Status	Verification
B1. Cai/Li factor-of-two “closure” not demonstrated	PARTIAL	Appendix A is now much stronger and no longer contains the old c-scaling contradiction. It correctly states that under a consistent Komatsu–Spergel c-change both f
NL
	​

 and σ(f
NL
	​

) scale as 1/c, and it treats Li −35/16 as a single-time-ordering stress test rather than a physical branch. 

paper2_fnl_forecast_v1.7.55

 However, the paper still does not provide a full independent source-to-source rederivation of the four conformal-time integrals; it relies on operator-algebra/Wick-bookkeeping plus benchmark matching. That is acceptable if phrased as an audit, but still too strong if advertised as a complete closure of Li et al. at the level of the published integral calculation.
B2. Polynomial null-space treated as physical uncertainty	PARTIAL	This remains the main unresolved issue. The text still calls the null space a “genuine theory-modeling ambiguity” even while saying the six-monomial expansion is this paper’s doubled/symmetrized representation, not Cai et al.’s native derivation, and that coefficients are fixed from three benchmark values after direct transplantation fails. 

paper2_fnl_forecast_v1.7.55

 The shape-stability result is useful, but the ±0.13 scatter should be called a basis-dependent representation/surrogate uncertainty unless the exact symbolic map from Cai’s polynomial to the authors’ basis is supplied.
B3. r≃0.84 not a SPHEREx cross-Fisher response	CLOSED	The paper now consistently frames the result as a sensitivity recast, not an independent SPHEREx Fisher forecast. It explicitly uses Heinrich et al.’s σ(f
NL
	​

)≃0.7 baseline and applies r as a shape-weighted degradation. 

paper2_fnl_forecast_v1.7.55

 Heinrich et al. do report σ
f
NL
	​

	​

=0.7 from the SPHEREx bispectrum alone and ≃0.5 when combined with the power spectrum. 
arXiv

B4. Post-systematic 3–5σ headline unsupported	PARTIAL	The old overclaim is substantially fixed. The paper now uses 2.6–5σ, explicitly distinguishes the GR-only ≃3.0σ point from the all-combined 2.6–2.8σ endpoint, and Fig. 2 labels the naive 6.25σ bar as not used in any headline. 

paper2_fnl_forecast_v1.7.55

 Remaining gap: the abstract still lists polynomial-null-space scatter as part of the systematic budget, but the all-combined floor is not explicitly propagated through the lower null-space percentile; if that scatter is truly budgeted, the lower endpoint should be shown in a single budget table.
B5. GR-degradation parameterisation not supported by cited source	CLOSED	The GR grid is now described as an internal stress-test amplitude, motivated by relativistic-projection biases but not directly translated from Addis et al. This is the right framing. Addis et al. report large f
NL
	​

 biases when relativistic effects are neglected, including ∼3σ for a Euclid-like Hα survey and ∼20σ for a MegaMapper-like LBG survey, plus 15–20% improvement from bright/faint splitting; that supports the qualitative motivation, not a direct SPHEREx degradation table. 

paper2_fnl_forecast_v1.7.55

 
arXiv
Original MAJORS
Original item	Status	Verification
M1. Reframe “forecast” versus “recast” consistently	CLOSED	Title, abstract, §IV, and conclusion now consistently use the recast framing.
M2. Do not call the benchmark “parameter-free” without qualification	CLOSED	The manuscript now uses “minimally parameterized” and repeatedly lists assumptions (a)–(f), including scalar-only ECH restrictions, no prolonged post-bounce inflation, and unverified cubic transfer. 

paper2_fnl_forecast_v1.7.55


M3. Bayes factors too prior-dominated for prominence	CLOSED	The Bayes-factor result is now caveated as illustrative, prior-sensitive, and not definitive model selection. The headline BF≃9–14 under noise-weighted r≃0.84 bookkeeping is consistent with the body and conclusion. 

paper2_fnl_forecast_v1.7.55

 

paper2_fnl_forecast_v1.7.55


M4. Faithful cubic-order transfer through the bounce is central	CLOSED	The caveat is now in the abstract, assumptions section, and conclusion.
M5. Heinrich σ(f
NL
	​

)=0.7 citation/use	CLOSED	The number is now used as an external baseline, not as a derived result of this paper, and is supported by Heinrich et al. 
arXiv

M6. Speculative anomaly-tracer material distracts	PARTIAL	The anomaly-tracer material is now clearly labelled as an upper bound and excluded from the headline 2.6–5σ result. 

paper2_fnl_forecast_v1.7.55

 It remains too long for a focused recast paper, but this is now a presentation issue rather than a scientific blocker.
M7. Joint (f
NL
	​

,n
f
NL
	​

	​

) SDB section should be demoted	PARTIAL	Scientifically safe now: the paper clearly says the SDB-only joint channel gives only 1.4σ to 0.6σ after n
f
NL
	​

	​

 marginalisation and is subordinate to the bispectrum headline. 

paper2_fnl_forecast_v1.7.55

 It remains overlong for the main text.
M8. Birefringence discussion off-topic	CLOSED	No remaining scientific concern; it is now scoped as auxiliary and does not enter the f
NL
	​

 forecast.
2. Fresh pass on v1.7.55 — new findings only
New BLOCKERS

None. I do not see a new error that forces rejection or wholesale reframing.

New MAJORS
FM1. Current-data section is stale: DESI DR1 has published independent LSS f
NL
	​

 constraints

Location: §VIII.A, p.18; also §IX.B, p.20.

Problem: The manuscript states that “DESI DR1 has not published an independent f
NL
	​

 constraint from scale-dependent bias as of this writing,” and therefore says the current-data bound rests on Planck alone. 

paper2_fnl_forecast_v1.7.55

 That is no longer true. DESI DR1 LRG/QSO analyses now report LSS constraints on local PNG from scale-dependent bias. Chaussidon et al. report, for DESI 2024 LRG and QSO samples, combined constraints such as f
NL
loc
	​

=−3.6
−9.1
+9.0
	​

 under one bias-assumption combination and 3.5
−7.4
+10.7
	​

 under another; a later DESI DR1 QSO assembly-bias analysis reports f
NL
	​

=−3.3±9.2. 
arXiv
+1

Proposed fix: Update §VIII.A to include the DESI DR1 LSS constraints and state that they remain far too weak to discriminate the bounce from inflation, but are no longer absent. If the authors want to recast them onto the bounce template, do so with the appropriate LSS/noise-weighted r≃0.84, or explicitly say the recast is not attempted because the DESI analyses use different tracer and bias assumptions. Also update §IX.B, where DESI is currently treated only as a forecast/complementary probe.

New MINORS

§II.A, pp.3–4: Even if retained, the phrase “genuine theory-modeling ambiguity” should be softened to “basis-dependent representation uncertainty in our doubled symmetrized implementation.” This is the single most important wording change left in the paper.

§VI/Table II, pp.12–15: The Li −35/16 value is now mostly handled correctly as a non-physical stress test, but every mention of its location inside σ
theory
	​

 tails should be paired with “not part of the physical uncertainty budget” to avoid reintroducing the old branch interpretation.

Data and Code Availability, p.23: Replace “Zenodo DOI inserted at submission” with the actual DOI before publication. 

paper2_fnl_forecast_v1.7.55

Main-text length: The abstract, anomaly-tracer discussion, and SDB running subsection remain too long. They are scientifically safer now, but the paper would be more publishable if those details were moved to appendices.

3. Updated recommendation

Recommendation: MAJOR REVISIONS, narrowly.

The paper moved toward publishability since v1.7.53; after the DESI current-data update and a final demotion of the null-space scatter from “physical systematic” to “basis-dependent representation stress test,” I would likely move this to minor revisions.
