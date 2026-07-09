chat: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a5026ac-4c54-83e8-8c24-125836db36b3
reviewer: ChatGPT (Pro Extended Thinking) | paper: P2 v1.7.107 (38pp) | date: 2026-07-09 W13
baseline W12: MINOR | movement: DOWNGRADE → MAJOR REVISIONS — re-raised the factor-of-2 amplitude objection: 'displayed equations do not algebraically connect the proposed polynomial discrepancy to the claimed factor-of-two correction'; wants exact vertex-sum polynomial + corrected full shape in one common convention. (Recurring factor-of-2 item, verified-review-reset memory: 'factor-of-2 genuinely unresolved'.) Presentation-set closure did NOT hold ChatGPT at MINOR.
verdict (from raw): Recommendation: MAJOR REVISIONS
---RAW---
Show moreShow lessChatGPT said:ChatGPT said:Referee Report
Recommendation: MAJOR REVISIONS
The manuscript contains a potentially valuable forecast recast and makes a commendable effort to separate the corrected matter-bounce amplitude from the externally imported SPHEREx sensitivity. The sensitivity-recast status and the unavailability of the Heinrich et al. per-triangle covariance are disclosed unusually clearly. However, the manuscript’s central theoretical contribution—the claimed resolution of the Cai–Li factor-of-two discrepancy—is not yet algebraically self-consistent. The same unresolved inconsistency propagates directly into the adopted bounce shape, the template-recovery factor rrr, and hence the forecasted significance. These are publication-blocking issues rather than presentational concerns. x_P2
BLOCKERS
1. The stated polynomial difference cannot produce the claimed change from −35/16-35/16−35/16 to −35/8-35/8−35/8
Location: Abstract; Sec. II A, pp. 4–5; Appendix A, Eqs. (A1)–(A5), pp. 31–33; Conclusion, p. 30.
The manuscript claims
ATprinted−∑vAv=+99128∑iki3,A_T^{\rm printed}-\sum_v A_v
=+\frac{99}{128}\sum_i k_i^3,ATprinted​−v∑​Av​=+12899​i∑​ki3​,
while using
fNL=103A∑iki3.f_{\rm NL}=\frac{10}{3}\frac{A}{\sum_i k_i^3}.fNL​=310​∑i​ki3​A​.
Under those equations, the displayed discrepancy shifts the squeezed-limit amplitude by
ΔfNL=10399128=16564≃+2.578.\Delta f_{\rm NL}
=\frac{10}{3}\frac{99}{128}
=\frac{165}{64}
\simeq +2.578.ΔfNL​=310​12899​=64165​≃+2.578.
But the difference between the two amplitudes the paper seeks to reconcile is
−358−(−3516)=−3516≃−2.188.-\frac{35}{8}-\left(-\frac{35}{16}\right)
=-\frac{35}{16}
\simeq -2.188.−835​−(−1635​)=−1635​≃−2.188.
The sign and magnitude are both different. The manuscript recognizes this locally, saying the 99/12899/12899/128 term “is not the sole complete mechanism,” but elsewhere calls it “the single term by which” the printed polynomial yields −35/8-35/8−35/8, “the algebraic origin,” and the term “that produces” the erroneous result. These statements are mutually incompatible.
This matters because the advertised central contribution is not merely that a direct vertex sum gives −35/16-35/16−35/16; it is that the literature discrepancy has been traced and resolved. At present the paper has certified one candidate vertex sum and identified one polynomial mismatch, but it has not shown how the complete algebra maps the published polynomial result to the claimed corrected result.
Proposed fix: Provide one exact symbolic identity in a single common basis and normalization containing:
the four source-level vertex expressions;
their exact sum;
the complete printed Cai polynomial after translating all permutation conventions;
the full difference between the two expressions, with no omitted terms;
the squeezed reduction of each side;
the resulting exact ΔfNL\Delta f_{\rm NL}ΔfNL​.
The difference polynomial must reproduce −35/16→−35/8-35/16\to-35/8−35/16→−35/8 numerically under the displayed fNLf_{\rm NL}fNL​ definition. Until it does, the language should be reduced to: “our direct transcription and summation gives −35/16-35/16−35/16, but the precise origin of the disagreement with the published polynomial remains unresolved.”
2. The manuscript uses an unestablished “corrected shape” in the template-overlap forecast
Location: Sec. II A, pp. 4–6; Table I and Fig. 1, p. 7; Sec. III B, pp. 9–11; Appendix A.
The paper says that the overlap analysis uses Cai et al.’s printed monomial shape because the correction affects only the overall normalization and is therefore irrelevant to shape ratios. That conclusion does not follow from the manuscript’s own proposed correction. An additive term proportional to ∑iki3\sum_i k_i^3∑i​ki3​ is a local-shaped addition, not a global multiplicative rescaling of the complete shape. It generally changes
Bbounce(k1,k2,k3)Bbouncesqueezed,\frac{B_{\rm bounce}(k_1,k_2,k_3)}
{B_{\rm bounce}^{\rm squeezed}},Bbouncesqueezed​Bbounce​(k1​,k2​,k3​)​,
and therefore changes rrr, rcosr_{\rm cos}rcos​, and the projection onto local/equilateral/orthogonal templates.
The manuscript nevertheless constructs Fig. 1 and Table I by taking the published benchmark values at squeezed, equilateral and folded configurations and dividing all three by exactly two. That is a global rescaling prescription. It is not demonstrated to be equivalent to the displayed additive correction in Eq. (A2). Indeed, the paper explicitly states that the additive term alone does not generate the factor of two.
The underdetermined six-coefficient reconstruction does not solve this problem. It generates shapes satisfying three rescaled benchmark values, but those benchmark values themselves presume the unproved global-halving rule.
Proposed fix: Recompute the full corrected shape directly from the verified sum of the four vertices over the complete triangle domain. Use that vertex-summed expression—not the printed polynomial rescaled by one half and not a three-benchmark reconstruction—to calculate:
Fig. 1 and Table I;
rrr under every weighting scheme;
rcosr_{\rm cos}rcos​;
the standard-template decomposition;
the independent Fisher result reffr_{\rm eff}reff​;
every significance and Bayes-factor rebooking that depends on rrr.
If the full vertex-summed shape is exactly one half of the published shape, display and prove that polynomial identity. If it is not, the present r=0.84r=0.84r=0.84 forecast cannot be retained without recomputation.
3. The treatment of time ordering and the ϵ\epsilonϵ-grouped expressions is internally contradictory
Location: Appendix A, especially Eqs. (A5), (A7)–(A12), and Appendix A.1(d), pp. 33–35.
Equation (A5) states that Cai et al.’s ϵ\epsilonϵ-grouped pieces give
−52+516+0=−3516,-\frac52+\frac5{16}+0=-\frac{35}{16},−25​+165​+0=−1635​,
and the surrounding text presents this as an independent cross-check of the full four-vertex result.
Later, Appendix A.1(d) states that Cai et al.’s Eqs. 34–36 are the single-time-ordered correlator before the −2 Im-2\,\mathrm{Im}−2Im doubling, and that their ratio to the full result is exactly 1/21/21/2. These claims cannot both hold in the same normalization. If Eq. (A5) represents the undoubled contribution, doubling it would not leave −35/16-35/16−35/16.
Moreover, Appendix A.1 first says the commutator identity does not adjudicate the Cai–Li discrepancy, but subsection (d) assigns a specific factor-of-two status to Cai’s intermediate equations without displaying the source-level normalization that makes this assignment valid.
Proposed fix: Add an explicit normalization ledger for every object:
Aintegrand,Asingle ordering,−2 Im A,Aϵ,Aϵ2,Aϵ3,AT,fNL.A_{\rm integrand},\quad
A_{\rm single\ ordering},\quad
-2\,{\rm Im}\,A,\quad
A_{\epsilon},A_{\epsilon^2},A_{\epsilon^3},\quad
A_T,\quad f_{\rm NL}.Aintegrand​,Asingle ordering​,−2ImA,Aϵ​,Aϵ2​,Aϵ3​,AT​,fNL​.
For each cited equation from Cai et al., state whether all Wick permutations, the commutator factor, external mode-function factors and the 10/310/310/3 conversion have already been included. Then show the exact equality between the source equations and the manuscript’s Eqs. (A3)–(A5). The current contradictory statements must be eliminated.
4. The central forecast depends on a theoretical correction that is not independently established by the displayed derivation
Location: Abstract; Secs. II–IV; Appendix A.
The manuscript repeatedly invokes Li et al.’s general-csc_scs​ expression as independent support for −35/16-35/16−35/16. However, it also states that Li et al.’s printed total polynomial agrees coefficient-for-coefficient with Cai et al.’s printed polynomial and therefore produces −35/8-35/8−35/8 when squeezed directly. Thus, within the manuscript’s own account, Li et al.’s formula and Li et al.’s polynomial are themselves inconsistent.
That may indeed indicate an error in the literature, but it means that citing the closed-form Li result is not sufficient to close the derivation. The manuscript must establish which of Li et al.’s two mutually inconsistent outputs follows from their actual vertex integrals and normalization.
Proposed fix: Extend the source-level audit to Li et al. At minimum, evaluate their general-csc_scs​ vertex expressions at cs=1c_s=1cs​=1 before their final polynomial reduction and show whether they reproduce Table VII. A statement that one printed formula agrees with the preferred answer is not an independent derivation when another printed formula in the same work agrees with the rejected answer.
MAJORS
1. The GR-covariance bracket and the adopted “conservative endpoint” are mislabeled
Location: Sec. VII opening discussion, pp. 20–21; Eq. (11); Table V, pp. 23–25; Data and Code Availability, p. 31.
The covariance-availability limitation requested for scrutiny is disclosed prominently and honestly. The paper clearly states that Heinrich et al.’s per-triangle CovB{\rm Cov}_BCovB​ is unavailable, that a channel-native noise-weighted correlation cannot therefore be calculated, and that ρ=−0.868\rho=-0.868ρ=−0.868 is transferred from an SDB Fisher calculation as a proxy.
The numerical interpretation is nevertheless inconsistent. The paper reports:
ρ=−0.868⇒S≃1.3σ\rho=-0.868 \Rightarrow S\simeq1.3\sigmaρ=−0.868⇒S≃1.3σ;
a geometry-only overlap ∣ρ∣≃0.95⇒S≃0.8σ|\rho|\simeq0.95 \Rightarrow S\simeq0.8\sigma∣ρ∣≃0.95⇒S≃0.8σ;
an overall unresolved bracket of approximately 0.80.80.8–1.3σ1.3\sigma1.3σ.
It then calls the 1.3σ1.3\sigma1.3σ proxy the “conservative endpoint.” Within the stated bracket, 0.8σ0.8\sigma0.8σ is the conservative lower-significance endpoint. The ρ=−0.868\rho=-0.868ρ=−0.868 result is instead the less-degraded or optimistic edge of the unresolved correlated-nuisance bracket.
The assertion that −0.868-0.868−0.868 is “now shown not to be an underestimate” is also not justified by a covariance-free shape overlap. A uniform or k2k^2k2-weighted shape cosine does not order the true multi-tracer Fisher correlation unless the covariance weighting is known.
Proposed fix: Report the result as:
best currently calculable proxy: 1.3σ1.3\sigma1.3σ;
unresolved channel-native bracket under the paper’s two weighting proxies: 0.80.80.8–1.3σ1.3\sigma1.3σ;
conservative lower edge: 0.8σ0.8\sigma0.8σ;
adopted headline endpoint, if retained: 1.3σ1.3\sigma1.3σ, explicitly as a convention rather than a proven floor.
Alternatively, omit the 0.8σ0.8\sigma0.8σ calculation from the quantitative envelope if the authors judge its metric too incommensurate with the bispectrum covariance to be interpreted as a bound.
2. The headline 1.31.31.3–2.75σ2.75\sigma2.75σ interval mixes incompatible procedures and is not a statistical confidence interval
Location: Abstract, pp. 1–3; Secs. IV and VII; Table V.
The manuscript does disclose that the endpoints come from different procedures. Nevertheless, the same interval is repeatedly described as the “realistic” significance. Its upper endpoint assumes no GR degradation and the fixed/universality-level bϕb_\phibϕ​ treatment, while its lower endpoint combines widened bϕb_\phibϕ​, an assumed GR nuisance and, in one version, a correlation proxy imported from another observable. It is therefore a scenario span, not a forecast uncertainty range.
A reader can easily interpret “SPHEREx sensitivity after systematic budget is 1.31.31.3–2.75σ2.75\sigma2.75σ” as though both endpoints result from one propagated budget.
Proposed fix: Replace the range with separately named scenarios in the abstract and conclusion, for example:
published-local-baseline recast: 2.62.62.6–2.75σ2.75\sigma2.75σ;
selected additive-budget scenario: approximately 1.31.31.3–1.5σ1.5\sigma1.5σ;
unresolved GR-correlation stress bracket: approximately 0.80.80.8–1.3σ1.3\sigma1.3σ.
Do not join these into one interval unless a probability model or explicit scenario prior is supplied.
3. The independent Fisher calculation creates a second, materially different SPHEREx forecast that is not adequately reconciled with the adopted headline
Location: Abstract pp. 1–2; Sec. IV, pp. 12–13.
The manuscript calls itself a sensitivity recast while also presenting an in-house Fisher calculation giving:
real-space σ(fNL)=0.63\sigma(f_{\rm NL})=0.63σ(fNL​)=0.63–0.69;
redshift-space σ(fNL)=0.42\sigma(f_{\rm NL})=0.42σ(fNL​)=0.42–0.45;
an unmarginalized 4.94.94.9–5.2σ5.2\sigma5.2σ redshift-space sensitivity.
The last result is substantially stronger than the imported Heinrich baseline. It is not merely a check of the template-overlap ratio; it is a separate absolute forecast. Its covariance, nuisance treatment, RSD model and omission of b2,bs2b_2,b_{s^2}b2​,bs2​ marginalization differ from Heinrich et al.
The manuscript labels the limitations, but presenting the 4.94.94.9–5.2σ5.2\sigma5.2σ result while continuing to call all quantitative findings a single-source recast is confusing.
Proposed fix: Either move the independent Fisher to a technical validation appendix and restrict it to the ratio reffr_{\rm eff}reff​, or present it as a genuinely separate forecast with its own complete nuisance model, convergence tests and table. The absolute redshift-space significance should not be highlighted until the bias and theoretical-error marginalization is comparable to the published forecast being validated.
4. Claims that cubic-order transmission is “derived” and bounded at ≲10−3\lesssim10^{-3}≲10−3 are too strong
Location: Abstract; Sec. II C, pp. 7–9; Sec. IX E, pp. 28–30; Conclusion.
Single-clock degree-of-freedom counting is not, by itself, sufficient to establish ζ˙=0\dot\zeta=0ζ˙​=0 across a nonsingular LQC bounce at nonlinear order. Absence of an additional propagating scalar does not automatically exclude a non-attractor adiabatic mode, singular gauge behavior, a modified constraint algebra, or nonlinear mode mixing. The manuscript initially identifies ζ˙→0\dot\zeta\to0ζ˙​→0 as the load-bearing condition and notes that only linear transmission has been verified, but later says cubic transmission is “guaranteed,” “derived,” and “closed” to δfNL≲10−3\delta f_{\rm NL}\lesssim10^{-3}δfNL​≲10−3.
The numerical estimate also depends on the asserted kηbounce∼10−2k\eta_{\rm bounce}\sim10^{-2}kηbounce​∼10−2, for which the mapping between observable modes and the bounce scale is not derived in the text.
Proposed fix: Restore assumption (d) as a motivated but unverified nonlinear-transfer assumption unless an explicit nonlinear conservation theorem is demonstrated for the precise effective-LQC equations and matching conditions used here. The ≲10−3\lesssim10^{-3}≲10−3 value should be described as a gradient-scaling estimate, not a rigorous bound.
5. The bϕb_\phibϕ​ degradation figures are not derived from the cited bispectrum forecast
Location: Sec. IV, pp. 13–14; Sec. VII B, pp. 21–22; Table V.
The paper assigns combined-sample replacements σ(fNL)=0.9\sigma(f_{\rm NL})=0.9σ(fNL​)=0.9 and 1.01.01.0 for “30%” and “50%” bϕb_\phibϕ​ cases, but no bispectrum Fisher calculation is shown that maps those prior widths to those errors. The cited literature motivates uncertainty in the universality relation but does not, as presented here, establish the numerical SPHEREx bispectrum degradation used in Table V.
The manuscript sometimes describes the 20%20\%20% prior as already embedded in the Heinrich baseline and elsewhere describes Heinrich as fixing bϕb_\phibϕ​ through universality. A fixed relation and a 20%20\%20% Gaussian prior are not equivalent.
Proposed fix: Either compute the bispectrum Fisher with per-tracer bϕb_\phibϕ​ nuisance parameters and the stated priors or label the 0.90.90.9 and 1.01.01.0 values explicitly as illustrative stress-test assumptions. Clarify whether Heinrich et al. fixed bϕb_\phibϕ​, imposed a prior, or marginalized a reduced universality parameter.
6. Bayes factors are more prior-volume statements than model-discrimination forecasts
Location: Sec. VI, pp. 16–20; Tables III–IV.
For a point prediction against a broad uniform alternative, the leading result
B≃W2πσB \simeq \frac{W}{\sqrt{2\pi}\sigma}B≃2π​σW​
is dominated by the arbitrarily selected alternative-prior width WWW. The manuscript acknowledges this, but still promotes BF≃9BF\simeq9BF≃9–14 as a principal result. The Gaussian bounce prior width σtheory=1\sigma_{\rm theory}=1σtheory​=1 is also much broader than the manuscript’s stated 0.180.180.18 theoretical correction, and is selected heuristically.
More importantly, the alternatives are not complete inflationary models with priors on their physical parameters and induced distributions in amplitude and shape. They are phenomenological prior densities in one observable. Calling the resulting ratio “bounce versus tuned multifield competitors” overstates what is being compared.
Proposed fix: Rename these quantities “one-dimensional prior-predictive likelihood ratios” or construct evidence integrals from specified physical competitor models. The abstract should not headline the Bayes factor unless the dependence on WWW and σtheory\sigma_{\rm theory}σtheory​ appears in the same sentence.
MINORS
1. Abstract length and density
Location: pp. 1–3.
The abstract spans several pages and incorporates appendix-level derivations, caveat hierarchies, multiple Fisher analyses and detailed Bayesian bookkeeping. This is far beyond normal MNRAS/PRD/JCAP abstract conventions and makes the principal contribution difficult to identify.
Proposed fix: Reduce it to approximately 200–300 words: corrected benchmark, recast methodology, principal scenario values, and the two load-bearing limitations.
2. Ambiguous use of “headline”
Location: throughout, especially Abstract, Secs. IV, VII and X.
The paper refers to several different quantities as the headline: 2.62.62.6–2.75σ2.75\sigma2.75σ, 1.31.31.3–2.75σ2.75\sigma2.75σ, 1.3σ1.3\sigma1.3σ, the independent 3.23.23.2–3.5σ3.5\sigma3.5σ, and occasionally the redshift-space 4.94.94.9–5.2σ5.2\sigma5.2σ.
Proposed fix: Define exactly one primary result and label all others as optimistic, validation, or stress-test scenarios.
3. Table V’s ϵ\epsilonϵ-correction row has an unclear combination rule
Location: Table V, p. 25.
The ϵ\epsilonϵ correction changes the predicted signal amplitude and possibly the shape overlap; it is not naturally an “add in quadrature” uncertainty in the same sense as an observational noise contribution.
Proposed fix: Propagate it as a theoretical prediction interval in the numerator, preferably recomputing the shape overlap if the shape correction is retained.
4. The null-space scatter is assigned quantitative significance despite being basis-measure dependent
Location: Sec. II A, pp. 5–6; Table V.
The manuscript correctly notes that uniform sampling in Euclidean coefficient coordinates is not invariant under a basis transformation. The associated r=0.85±0.13r=0.85\pm0.13r=0.85±0.13, percentiles and “distributional floor” therefore have no objective probabilistic interpretation.
Proposed fix: Retain the scan only as a sensitivity test. Do not quote percentiles or treat its 16th percentile as a forecast floor unless a physically motivated prior measure is supplied.
5. The anomaly-tracer discussion is extraneous
Location: Secs. IV–V, pp. 14–15.
The projected 10–20% benefit from anomaly-selected tracers is acknowledged as an upper bound and is not used in the headline forecast. It distracts from the paper’s main question.
Proposed fix: Remove it or confine it to a brief outlook paragraph.
6. The cosmic-birefringence paragraph is unrelated to the forecast
Location: Sec. IX E(c), p. 30.
The paragraph introduces a model-dependent spectator-ALP observation that is not quantitatively connected to the matter-bounce fNLf_{\rm NL}fNL​ prediction.
Proposed fix: Delete it from this manuscript.
7. Several figures mix quantities from non-equivalent forecast channels
Location: Figs. 2, 4–6.
The figures juxtapose SDB-only, imported bispectrum, independent Fisher and heuristic systematic scenarios. This can imply stronger comparability than exists.
Proposed fix: Separate bispectrum and SDB results visually and state in each caption which Fisher matrix, nuisance assumptions and template convention are being used.
Strengths
The paper is exceptionally explicit that the SPHEREx headline is a sensitivity recast rather than a claimed detection or an analysis of survey data. The matter-bounce prediction, imported σ(fNL)\sigma(f_{\rm NL})σ(fNL​), and template-overlap correction are generally kept conceptually separate.
The manuscript adopts one central benchmark, fNL=−35/16=−2.1875f_{\rm NL}=-35/16=-2.1875fNL​=−35/16=−2.1875, rather than exploiting the more favorable −35/8-35/8−35/8 value in its forecast. This is scientifically conservative, provided the correction is ultimately established.
The covariance limitation is disclosed prominently: the Heinrich et al. per-triangle multi-tracer covariance is said to be unavailable, the ρ=−0.868\rho=-0.868ρ=−0.868 result is identified as a proxy imported from another Fisher channel, and the paper does not falsely claim to have completed the channel-native marginalization.
The distinction between the bispectrum headline and the separate SDB (fNL,nfNL)(f_{\rm NL},n_{f_{\rm NL}})(fNL​,nfNL​​) Fisher calculation is explained repeatedly, including the fact that the bispectrum shape-overlap factor rrr does not apply to SDB.
The manuscript makes substantial reproducibility efforts, including exact-fraction vertex tables, named scripts, committed outputs, convergence studies and an intended archival release.
The discussion of MegaMapper is appropriately cautious: the facility is identified as proposed and unfunded, and its systematic envelope is explicitly described as uncalibrated.
Specific scrutiny requested by the editor
Sensitivity-recast presentation
Assessment: Substantially satisfactory in framing, but not yet reliable numerically.
The manuscript repeatedly states that the principal SPHEREx result is a recast of the Heinrich et al. local-template forecast rather than a detection claim. It also clearly separates the theoretical benchmark fNL=−35/16f_{\rm NL}=-35/16fNL​=−35/16 from the forecasted uncertainties σ(fNL)≃0.7\sigma(f_{\rm NL})\simeq0.7σ(fNL​)≃0.7 for SPHEREx and the more speculative MegaMapper values. The abstract, Sec. IV, Table V and conclusion all include this qualification.
The problem is not concealment of forecast status. It is that the recast factor rrr is calculated from a “corrected shape” whose derivation is not presently consistent with the paper’s own polynomial-error diagnosis. Thus, the framing passes scrutiny, but the quantitative implementation does not yet do so.
Covariance-availability caveat
Assessment: Honestly disclosed, but the resulting bound is overstated and mislabeled.
The manuscript clearly states that the Heinrich et al. per-triangle CovB{\rm Cov}_BCovB​ is not publicly available and that only the scalar σ(fNL)≃0.7\sigma(f_{\rm NL})\simeq0.7σ(fNL​)≃0.7 is imported. It also explains why a channel-native correlation coefficient requires that covariance. This is an adequate and commendably direct disclosure.
However, ρ=−0.868\rho=-0.868ρ=−0.868 is not demonstrated to be the “marginalized floor.” It is a transferred SDB proxy. The manuscript’s own alternative shape-overlap exercise produces a still lower significance of approximately 0.8σ0.8\sigma0.8σ, and the absence of the true covariance prevents ordering either proxy rigorously. The honest conclusion is that 1.3σ1.3\sigma1.3σ is the best currently implemented proxy under one weighting assumption, while the channel-native marginalized sensitivity remains unresolved.
Overall judgment
The observational recast is carefully scoped, but the paper’s foundation is the claimed exact correction of the matter-bounce amplitude and shape. The displayed equations currently do not algebraically connect the proposed polynomial discrepancy to the claimed factor-of-two correction, and the forecast then assumes a global halving of a shape that the manuscript simultaneously describes as receiving an additive local component. Until the exact vertex-sum polynomial and the corrected full shape are established in one common convention and all overlap quantities are recomputed from it, the central scientific chain is incomplete.
Recommendation: MAJOR REVISIONSSourcesInstant