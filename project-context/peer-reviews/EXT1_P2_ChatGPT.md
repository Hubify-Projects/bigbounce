# EXT1 P2 — ChatGPT Pro Extended referee report
**Provider**: chatgpt.com web app (Big Bounce Book project) · intelligence **Pro Extended** (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e646-8510-83e8-8999-77b849c6519d
**PDF**: paper2_fnl_forecast_v1.7.48.pdf (md5 4cb0963e) · **Harvested**: 2026-06-10T17:05 PDT

---

Show more
Thought for 13m 32s
MNRAS-style referee report

Manuscript: Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook
Recommendation: MAJOR REVISIONS

I read the full 24-page PDF. The paper has a publishable core: a timely, potentially useful recast of the SPHEREx local-PNG sensitivity onto a matter-bounce benchmark. However, in its present form it overstates what has been demonstrated. The most serious issues are not cosmetic: the claimed closure of the Cai/Li factor-of-two ambiguity is not established by the appendix as written; the “null-space” treatment of the bounce shape appears to be an artefact of the authors’ internal polynomial reconstruction rather than a physical uncertainty; and the headline 3–5σ post-systematic-budget statement is not derived from a joint survey/nuisance Fisher calculation. The manuscript itself identifies many of these caveats, but then still carries a stronger headline than the analysis supports. 

paper2_fnl_forecast_v1.7.48

The paper should be resubmitted after being reframed as a sensitivity recast unless the authors actually implement a SPHEREx-consistent cross-Fisher calculation for the bounce template and a joint nuisance marginalisation.

BLOCKERS — must fix before publication
B1. Cai/Li factor-of-two “closure” is not demonstrated

Location: Abstract p.1–2; §II.C p.6; Appendix A pp.21–24; Table IV p.24. In extracted-text terms, see the abstract claim that the in-in identity establishes the −35/8 Planck normalisation, the statement that the Li value halves the significance, and Appendix A/Table IV where the Cai row gives 5.25σ and Li row gives 2.63σ. 

paper2_fnl_forecast_v1.7.48

 

paper2_fnl_forecast_v1.7.48

 

paper2_fnl_forecast_v1.7.48

Problem: The original Cai et al. matter-bounce paper indeed quotes the local squeezed-limit result f
NL
local
	​

=−35/8, with equilateral and folded benchmarks also matching the manuscript’s table. 
arXiv
 But the present manuscript’s stronger claim — that Appendix A establishes Li et al. as a single-time-ordering result and therefore closes the ambiguity in favour of Cai — is not proven. A generic operator identity,

i⟨[ζ
3
,H
int
	​

]⟩=−2Im⟨ζ
3
H
int
	​

⟩,

is necessary background, but it does not by itself show that Li et al. omitted the second in-in branch or that the published Li normalisation maps into Cai’s by simple doubling. Li et al. explicitly describe their calculation as an in-in evaluation, so the burden is on this manuscript to demonstrate the mapping equation by equation, not by assertion. 
ar5iv

Proposed fix: Either provide a full, source-to-source derivation mapping Cai’s and Li’s conventions at the level of the cubic action, field redefinition, permutation sums, power-spectrum normalisation, and local-template convention, or downgrade the claim. If the authors cannot prove the mapping, the paper must present −35/8 as the adopted Cai benchmark and −35/16 as an unresolved literature-normalisation alternative. The abstract, conclusion, Table IV, and all significance claims must then report both branches, not state that Appendix A closes the issue.

B2. The polynomial “null-space” is not a physical uncertainty as presented

Location: §II.A pp.3–4, especially the construction of a six-coefficient symmetrised polynomial from three benchmark configurations, the statement that Cai’s printed coefficients are not directly transplantable, and the subsequent 10,000-sample null-space scan. 

paper2_fnl_forecast_v1.7.48

Problem: The manuscript appears to create an underdetermined six-coefficient system by fitting three benchmark values after recompiling the Cai polynomial into the authors’ chosen symmetrised basis. That is not, by itself, a physical theory uncertainty. If Cai et al. give an explicit polynomial in their own convention, then the correct procedure is to transform that polynomial into the new basis algebraically, including all permutation and normalisation factors. Fitting three kinematic points to six coefficients and then sampling the remaining null directions risks propagating an artefact of the authors’ surrogate representation into the headline systematic budget.

This affects several central claims: the 84% template recovery, the ±0.13 amplitude scatter, the significance spread, and the language that the null-space scan validates robustness.

Proposed fix: Use Cai’s native polynomial directly, or provide the exact symbolic basis transformation from Cai’s printed expression into the authors’ basis and verify it on a dense set of triangle configurations, not only on squeezed/equilateral/folded points. If the transformation cannot be supplied, the null-space analysis should be explicitly labelled an internal surrogate robustness test and removed from the physical systematic budget.

B3. The template-overlap correction r≃0.84 is not a SPHEREx bispectrum Fisher response

Location: Abstract p.1; §III.B pp.7–8; §IV pp.8–9. The manuscript states that a local estimator recovers 84%±2% of the bounce signal and then applies this factor to the Heinrich et al. σ(f
NL
	​

)≃0.7 forecast. 

paper2_fnl_forecast_v1.7.48

 

paper2_fnl_forecast_v1.7.48

Problem: A shape-grid weighted average is not equivalent to the response of the Heinrich et al. multi-tracer galaxy-bispectrum estimator to the bounce template. The SPHEREx Fisher response should include the actual redshift bins, tracer weights, bias model, redshift-space distortions, photo-z damping, k-cuts, nuisance marginalisation, and covariance used in the published SPHEREx forecast. The manuscript acknowledges that it does not construct an independent multi-tracer bispectrum Fisher matrix and is instead adopting Heinrich et al.’s σ(f
NL
	​

)=0.7 as an external baseline. 

paper2_fnl_forecast_v1.7.48

The externalisation itself is acceptable: Heinrich et al. report a fiducial σ
f
NL
	​

	​

=0.7 from the bispectrum alone and σ
f
NL
	​

	​

=0.5 when combined with the power spectrum. 
arXiv
 But applying a heuristic r factor to that forecast is not yet a survey forecast for the bounce template.

Proposed fix: Compute the cross-Fisher response

r
survey
	​

=
F
local,local
	​

F
local,bounce
	​

	​


using the same survey covariance and nuisance treatment as Heinrich et al., or explicitly downgrade all template-corrected significances to approximate recast estimates. The title, abstract, and conclusion should then say “SPHEREx sensitivity recast” rather than implying an independent forecast.

B4. The post-systematic 3–5σ headline is not derived from a joint systematic budget

Location: Abstract p.1; §IV p.9; §VII.B–D pp.14–15; Fig. 2 and Fig. 5 captions. The manuscript quotes 5.2–5.5σ before GR and b
ϕ
	​

 degradation and 3–5σ after the combined systematic budget. 

paper2_fnl_forecast_v1.7.48

 

paper2_fnl_forecast_v1.7.48

 

paper2_fnl_forecast_v1.7.48

Problem: The ideal arithmetic is clear:

4.375×0.83/0.7≃5.2.

But the degraded 3–5σ range is not obtained from a joint marginalised Fisher calculation. It combines template mismatch, ϵ-corrections, b
ϕ
	​

, photo-z failures, GR projection effects, and additional unmodelled bias/lensing/integral-constraint effects through a set of illustrative degradations. The manuscript itself states that several effects are not jointly modelled and that some numbers are order-of-magnitude estimates. 

paper2_fnl_forecast_v1.7.48

This is not sufficient for a journal-level headline that SPHEREx “can test” the benchmark at >3σ after systematics. It is sufficient for “plausibly remains in the few-sigma regime under illustrative degradations.”

Proposed fix: Either perform a joint nuisance-marginalised Fisher analysis including b
ϕ
	​

, GR projection terms, photo-z outliers, nonlinear bias, and survey window effects, or change the headline to: “ideal template-corrected sensitivity is about 5σ; illustrative systematics can plausibly reduce this to roughly 3–5σ.” The abstract and conclusion should not present the lower end as a derived robust floor.

B5. The GR-degradation parameterisation is not supported by the cited source as written

Location: §VII.C p.15 and citation [25]. The manuscript maps relativistic projection effects to σ
GR
	​

=0.5 and 1.0, claiming this corresponds to a 10–30% degradation for SPHEREx/MegaMapper-like surveys. 

paper2_fnl_forecast_v1.7.48

Problem: The cited Addis/Jolicoeur-style result I checked discusses biases from neglecting relativistic terms and reports large survey-dependent biases, including order-3σ for a Euclid-like Hα survey and order-20σ for a MegaMapper-like LBG survey, plus 15–20% improvements under a bright/faint split. It does not directly justify the manuscript’s particular σ
GR
	​

=0.5,1.0 quadrature nuisance model or the stated 10–30% degradation mapping. 
arXiv

Proposed fix: Quote the cited result in its own terms, then explicitly derive any conversion to σ
GR
	​

 used here. If no derivation is available, label σ
GR
	​

 as an ad hoc stress-test parameter rather than an externally calibrated systematic model.

MAJORS — should fix
M1. Reframe “forecast” versus “recast” consistently

Location: Title, abstract, §IV, conclusion.

The paper says explicitly that it does not build an independent Heinrich-style multi-tracer bispectrum Fisher matrix and instead adopts the published σ(f
NL
	​

)=0.7. 

paper2_fnl_forecast_v1.7.48

 That is fine, but the presentation should be consistent. The result is a recast of an external local-template forecast, not a standalone SPHEREx bounce-template forecast.

Proposed fix: Retitle along the lines of “A SPHEREx sensitivity recast for the matter-bounce f
NL
	​

=−35/8 benchmark,” or provide the missing Fisher calculation.

M2. Do not call the benchmark “parameter-free” without qualification

Location: Abstract, introduction, §II.C, §VIII, conclusion.

The paper is already careful in places: it says the prediction is “minimally parameterized,” conditional on assumptions (a)–(f), affected by 0.6–8% quasi-dust corrections, and dependent on unverified cubic-order bounce transmission. 

paper2_fnl_forecast_v1.7.48

 But the headline still leans on “parameter-free” language.

Proposed fix: Use “conditional leading-order benchmark” or “minimally parameterized scalar-only matter-bounce benchmark” throughout. Reserve “parameter-free” only for the exact w=0, scalar-only, GR, Bunch-Davies, faithful-cubic-transfer limit.

M3. The Bayes factors are too prior-dominated for the current prominence

Location: §VI and Tables II–III.

The paper does disclose prior sensitivity, which is good. But the abstract-level BF∼10–17 still reads too strongly given that the result depends on a delta or Gaussian bounce prior, a broad uniform competitor prior, and an unresolved Cai/Li normalisation branch. 

paper2_fnl_forecast_v1.7.48

Proposed fix: Move much of the Bayes-factor machinery to an appendix or shorten it substantially. In the main text, state that a measurement near −4 would favour the bounce benchmark over broad/tuned multifield priors under the adopted prior choices, but avoid presenting the Bayes factor as robust model-selection evidence.

M4. Faithful cubic-order transfer through the bounce is central, not secondary

Location: §II.B–C, conclusion.

The paper correctly admits that faithful transfer of the bispectrum through the bounce is verified only at linear order and is the weakest link. That caveat must appear wherever the result is advertised as robust across a bounce class. 

paper2_fnl_forecast_v1.7.48

Proposed fix: Put this caveat in the abstract in a shorter but unambiguous form: “The test applies only if the contraction-phase cubic correlator is faithfully transmitted through the nonsingular bounce; this has not yet been demonstrated by a full third-order bounce calculation.”

M5. The exact Heinrich citation locator appears wrong or over-specific

Location: Abstract and §IV.

The manuscript cites “Heinrich et al. 2024, Fig. 6 / Table 3” for σ(f
NL
	​

)≃0.7. The published Heinrich abstract supports the σ=0.7 bispectrum-only and σ=0.5 combined numbers, but the locator should be checked; the exact full-analysis number also appears as about 0.73 in the body. 
arXiv

Proposed fix: Cite the abstract/summary or the exact equation/table where the number appears. If using 0.7, call it rounded. If using 0.73, update the ideal significance from 5.2σ to roughly 5.0σ for r=0.83.

M6. Speculative anomaly-tracer material distracts from the paper’s central claim

Location: §IV and §V.

The anomaly-selected QSO/emission-line paragraphs are not part of the headline forecast and are admitted to lack a shot-noise-corrected Fisher calculation. 

paper2_fnl_forecast_v1.7.48

Proposed fix: Remove these paragraphs or move them to a short “future work” appendix. They weaken the otherwise focused SPHEREx recast.

M7. The joint (f
NL
	​

,n
f
NL
	​

	​

) SDB section should be demoted

Location: §IX.D pp.18–19.

The manuscript is careful to state that the SDB-only joint analysis gives only 1.4σ to 0.6σ detection after marginalising over n
f
NL
	​

	​

, and that it is not the headline bispectrum forecast. 

paper2_fnl_forecast_v1.7.48

 

paper2_fnl_forecast_v1.7.48

 This is a useful self-check but too long for the main argument.

Proposed fix: Move most of §IX.D to an appendix, retaining only one paragraph in the discussion.

M8. Birefringence discussion is off-topic for this paper

Location: §IX.E p.19–20.

The ALP/cosmic-birefringence paragraph is not used in the SPHEREx forecast and risks making the paper look like a broad bounce advocacy piece rather than a focused PNG forecast.

Proposed fix: Delete it or reduce it to one sentence saying that other bounce-motivated observables exist but are independent of the present analysis.

MINORS — polish

Abstract length: The abstract is much too long for MNRAS/PRD/JCAP style. It reads like a compressed paper. Cut it to the essential claim, method, result, and caveats.

Figure readability: Figs. 2, 5, and 6 have small labels and dense captions. The rendered page images show that these will be hard to read at journal column width. Increase font sizes and simplify legends.

Fig. 5 sign convention: The right panel appears to title the signal as f
NL
	​

=35/8. Since the plotted quantity is a significance, use ∣f
NL
	​

∣=35/8 or include the minus sign.

Notation overload: The paper uses r for template overlap and r
t
	​

 for tensor-to-scalar ratio, P for both a polynomial and power spectra with qualifications, and multiple epsilon-related symbols. Definitions exist, but the text is dense. A notation table would help.

Reference formatting: Ref. [5] should use the correct arXiv category formatting for Li et al.; Ref. [27] is incomplete as printed (“JCAP arXiv:1712.09998”). Standardise all bibliography entries.

Data/code permanence: Replace or supplement the mutable GitHub branch with a tagged release or Zenodo DOI before publication.

Claims of “first to our knowledge”: The template-mismatch claim may be true, but it should be phrased conservatively unless a systematic literature search is documented.

MNRAS style: Avoid long correction-note blocks in the main body unless essential. Some can be moved to footnotes or an appendix.

MegaMapper language: The paper correctly says MegaMapper is proposed and unfunded; keep that qualification every time a MegaMapper significance is quoted. The Stage-5 concept status is consistent with the external description of MegaMapper as a proposed spectroscopic instrument concept. 
arXiv

Planck PR4 recast: The current-data discussion appears broadly consistent with the reported PR4 value f
NL
local
	​

=−0.1±5.0. 
arXiv
 No major issue, but keep the PR4/PR3 distinction concise.

Specific requested scrutiny
1. f
NL
	​

=−35/8=−4.375 as a parameter-free bounce prediction

The Cai benchmark itself is real: Cai et al. quote the matter-bounce squeezed/local value −35/8, with the equilateral and folded values also matching the manuscript’s Table I. 
arXiv
 The manuscript is therefore justified in studying −35/8 as a leading-order matter-bounce benchmark.

However, I would not allow the paper to call this “parameter-free” without immediate qualification. The manuscript itself lists quasi-dust corrections, w-dependence, unverified cubic transfer, scalar-only/ECH restrictions, and the Cai/Li ambiguity. The correct language is: conditional leading-order scalar-only matter-bounce benchmark.

2. Heinrich et al. σ(f
NL
	​

)=0.7: externalisation versus own Fisher

Externalising Heinrich et al. is acceptable, and the published paper supports the bispectrum-only σ
f
NL
	​

	​

=0.7 and combined σ
f
NL
	​

	​

=0.5 figures. 
arXiv
 But then this manuscript must consistently be a recast, not an independent SPHEREx forecast. The current text partly says that, but the title, abstract, and “validated via” language still overstate the independence of the result.

A proper bounce-template forecast requires the SPHEREx multi-tracer bispectrum Fisher response to the bounce shape, not a standalone shape-overlap factor multiplied into Heinrich’s local-template uncertainty.

3. Detection significance 3–5σ after systematics

The ideal number is arithmetically plausible:

σ
∣f
NL
	​

∣r
	​

≈
0.7
4.375×0.83
	​

≈5.2.

If the exact Heinrich value 0.73 is used instead of rounded 0.7, this becomes about 5.0σ. That is not a serious problem.

The problem is the post-systematic range. The manuscript has not shown a joint systematic covariance or Fisher degradation that yields a robust 3σ floor. The paper may say “illustrative systematics suggest a few-sigma test remains plausible,” but not “SPHEREx will test at 3–5σ after systematics” unless the authors perform the missing joint marginalisation.

The Cai/Li ambiguity is also decisive: under the Li branch, the manuscript’s own Table IV gives 2.63σ before the full systematic budget, so a firm >3σ post-budget claim cannot coexist with an unresolved normalisation ambiguity. 

paper2_fnl_forecast_v1.7.48

4. DBI category-error closure at §IV / §IX

I do not regard DBI as a remaining blocker. The manuscript now states the essential point correctly: DBI-type non-Gaussianity is equilateral/squeezed-suppressed and should not be compared to the bounce through the local n
f
NL
	​

	​

 scale-dependent-bias channel. The text explicitly says that DBI-vs-bounce discrimination requires the bispectrum-shape channel, not the local SDB running channel. 

paper2_fnl_forecast_v1.7.48

The only requested fix is editorial: move this clarification earlier, near §VI.A where inflationary mimics are discussed, so readers do not encounter the DBI correction only deep in §IX.

Strengths

Timely and relevant target. SPHEREx local-PNG sensitivity is an appropriate near-term arena for testing a matter-bounce benchmark.

Good physical motivation. The paper correctly identifies the local squeezed-limit amplitude as the sharpest observational discriminator between quasi-dust matter bounce and standard single-field slow-roll inflation.

Proper use of external survey literature in spirit. Using Heinrich et al.’s published SPHEREx σ(f
NL
	​

) as the baseline is sensible, provided the paper is consistently framed as a recast.

Improved gauge-frame/CFC distinction. The manuscript avoids the common mistake of treating the CFC physical squeezed-limit statement as the literal SPHEREx observable; it states that SPHEREx measures the conventional local-template/gauge-frame quantity. 

paper2_fnl_forecast_v1.7.48

Honest caveat culture. The paper is unusually transparent about assumptions, correction notes, unverified cubic transfer, b
ϕ
	​

 fragility, GR projection effects, and the Cai/Li ambiguity. The problem is not absence of caveats; it is that the headline remains too strong despite them.

DBI issue largely fixed. The text correctly removes DBI from the local-SDB n
f
NL
	​

	​

 comparison and treats it as an equilateral-shape bispectrum issue.

Potentially useful template-overlap exercise. Even if the present r≃0.84 is not yet a SPHEREx Fisher response, quantifying the local-template recovery of the matter-bounce shape is a worthwhile calculation once the polynomial-basis issue is fixed.

Sources

Pro Extended

