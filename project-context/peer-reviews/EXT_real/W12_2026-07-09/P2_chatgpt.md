chat: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a4ff9b5-6784-83e8-a9ba-2334dd4a980f
reviewer: ChatGPT (Pro Extended) | paper: P2 v1.7.106 (37pp) | date: 2026-07-09 W12
baseline W11: MINOR(accept-track) | movement: HARSHER PASS -> MAJOR (credits -35/16 + Eq.11 + Table V/Fig2 explicit; flags factor-of-2 algebra + budget internal contradictions)
verdict (from raw): VERDICT: MAJOR REVISIONS
---RAW---
Referee report on rt_P2.pdf 

rt_P2

I read the full 37-page PDF end-to-end, including the abstract, all forecast sections, Tables I–VIII, Figures 1–6, and Appendix A.

1. Focused revision assessment

Overall status: PARTIAL.

Calibrated f
NL
local
	​

=−35/16=−2.1875 claim: PARTIAL.
The manuscript now clearly intends a single central value. The abstract, Sec. II, Conclusion, and Table VIII repeatedly state that the adopted matter-bounce value is −35/16, with the −35/8 value retained only as an erroneous literature reference; Table VIII also correctly halves the SPHEREx headline from 5.25σ to 2.63σ under r=0.84,σ=0.7. 

rt_P2

 

rt_P2

 The normalization discussion also now explicitly says the SPHEREx estimator and the corrected bounce prediction use the same B
ζ
	​

=(6/5)f
NL
	​

P
ζ
	​

P
ζ
	​

 convention, with no residual conversion factor. 

rt_P2

However, the factor-of-two resolution is not closed at PRD standard. Appendix A says the vertex sum gives −35/16 and identifies a +(99/128)∑
i
	​

k
i
3
	​

 discrepancy, but it also concedes that this term alone has the wrong sign and is not the complete mechanism of the doubling. 

rt_P2

 That is incompatible with the abstract/conclusion language saying the published −35/8 “traces to a single spurious” term. 

rt_P2

 

rt_P2

 There are also downstream remnants that look like old −35/8 propagation: Sec. IX.A still says MegaMapper could reach “∼3–7σ” even though Sec. V’s corrected ideal range is only 3.7–3.85σ, and Table IV’s BF-vs-SSFSR column is still at ∼10
8
, which is the scale expected from a ∣f
NL
	​

∣≃4.4 point-hypothesis likelihood ratio, not from ∣f
NL
	​

∣=2.1875. 

rt_P2

 

rt_P2

 

rt_P2

Eq. (11) budget: PARTIAL.
Eq. (11) is now explicit and the arithmetic in Table V is mostly internally correct: S=∣f
NL
	​

∣r/σ
eff
	​

, σ
eff
2
	​

=σ
0
2
	​

+∑
j
	​

σ
j
2
	​

, r=0.84, b
ϕ
	​

 widening as σ
0
	​

→0.9,1.0, and GR nuisance values σ
GR
	​

=0,0.5,1.0. 

rt_P2

 The headline values 2.6–2.75σ, 1.36σ, and 1.30σ follow from the formula.

But it is not sufficient as a measurement/systematics budget. The text admits the budget is a scoping heuristic, not a joint covariance forecast. 

rt_P2

 Worse, the GR-correlation paragraph says the channel-native overlap could imply a marginalized floor of ∼0.8σ, while Table V and the abstract promote ∼1.3σ as the “conservative” endpoint. Using their own formula, ∣ρ∣≃0.95 gives σ
marg
	​

=0.7/
1−0.95
2
	​

≃2.24, hence S≃2.1875×0.84/2.24≃0.82σ. The paper cannot call 1.3σ conservative unless it either computes the channel-native covariance or explicitly excludes the ∣ρ∣≃0.95 case.

Sensitivity map: PARTIAL.
The map is now visible: Figure 2 summarizes SPHEREx and MegaMapper significance bars, Figures 4–5 show k
min
	​

 and b
ϕ
	​

 sensitivity, and Table V consolidates the budget. 

rt_P2

 

rt_P2

 

rt_P2

 But it is not yet a PRD-grade sensitivity map because it mixes qualitatively different objects: imported Heinrich recast, independent Fisher validation, SDB-only Fisher, additive-quadrature nuisances, and a correlation proxy transferred from a different channel. The map is useful as a scoping dashboard, not as a defensible final error budget.

2. Fresh pass: blockers

BLOCKER 1 — Factor-of-two forensic logic remains internally inconsistent.
Location: Abstract p. 1; Sec. II.C pp. 8–9; Appendix A pp. 31–35; Conclusion p. 30.
Problem: The manuscript says the −35/8 value “traces to” a single +(99/128)∑
i
	​

k
i
3
	​

 term, but Appendix A explicitly says that term alone would shift f
NL
	​

 by +(10/3)(99/128)≈+2.58, the wrong sign to reach −35/8. 

rt_P2

 This makes the central forensic claim over-stated even if the vertex-sum value −35/16 is correct.
Fix: Replace all “single spurious term produced the factor of two” language with a mathematically exact statement. Provide a compact algebra table: printed polynomial squeezed limit, vertex-sum squeezed limit, their exact difference under the same A, B
NL
	​

, and f
NL
	​

 definitions. If the +(99/128)∑k
3
 term is only one discrepancy, say so consistently and do not call the factor-of-two “fully resolved” beyond the vertex-sum certification.

BLOCKER 2 — The template-overlap r=0.84 may be computed from a shape the paper itself declares erroneous.
Location: Sec. II.A pp. 4–6; Sec. III.B pp. 9–11; Appendix A pp. 31–33.
Problem: Sec. II says the shape-overlap analysis uses Cai et al.’s printed monomial shape and treats the −35/16 correction as an overall amplitude normalization. 

rt_P2

 But Appendix A says Cai’s printed polynomial differs from the vertex sum by a local-shaped term, not by a pure multiplicative factor. 

rt_P2

 A local-shaped additive error directly changes the local-template overlap and thus the forecast r, not merely the amplitude.
Fix: Recompute every r, r
cos
	​

, null-space scan, Figure 1 curve, Table I benchmark, and SPHEREx significance using the corrected vertex-sum polynomial, not the printed Cai polynomial. If the corrected and printed shapes give numerically identical r after normalization, demonstrate that explicitly.

BLOCKER 3 — The null-space uncertainty conflicts with the claimed vertex-level exact polynomial.
Location: Sec. II.A pp. 4–6; Appendix A pp. 31–33; Table V p. 25.
Problem: Sec. II spends substantial space treating the six monomial coefficients as underdetermined by three benchmark configurations, yielding r=0.85±0.13. But Appendix A then claims an exact vertex-by-vertex resummation and even gives the collapsed degree-9 vertex-sum polynomial. Once the vertices are resummed, the coefficient null space is not a physical uncertainty.
Fix: Delete the null-space scatter from the central budget or reclassify it as a historical reconstruction diagnostic only. The actual forecast should use the corrected vertex-sum shape. Table V should not include a null-space “systematic” unless the exact vertex polynomial remains unavailable.

BLOCKER 4 — Eq. (11)/Table V conservative floor is not actually conservative.
Location: Sec. VII pp. 20–25; Table V p. 25; Figure 2 p. 14.
Problem: The paper claims the 1.3σ floor is conservative, but its own GR-template discussion admits a possible ∣ρ∣≃0.95 channel-native degeneracy, which would push the floor to ∼0.8σ. The Table V final row using ρ=−0.868 is a proxy, not a bound. 

rt_P2


Fix: Either compute the SPHEREx bispectrum F
f
NL
	​

A
GR
	​

	​

 with the actual multi-tracer covariance, or change the headline to something like “∼0.8–2.75σ under the unresolved GR-correlation bracket; ∼1.3σ under the SDB-proxy correlation.” Do not call 1.3σ the conservative endpoint.

BLOCKER 5 — Old-amplitude forecast remnants remain.
Location: Sec. IX.A p. 26; Table IV p. 23; Table III p. 19.
Problem: Sec. IX.A’s “MegaMapper ∼3–7σ” is inconsistent with the corrected −35/16 forecast; Sec. V gives 3.7–3.85σ ideal and 1.5–3.5σ design envelope. 

rt_P2

 

rt_P2

 Table IV’s BF-vs-SSFSR values ∼10
8
,∼10
5
,∼10
2
 are also not credible for a point detection at −2.1875 with σ=0.7; the ideal point-hypothesis likelihood ratio against f
NL
	​

≃0.015 is only exp[(2.2025)
2
/(2×0.7
2
)]≈1.4×10
2
. 

rt_P2


Fix: Globally grep all old −35/8-scaled significances and Bayes factors. Recompute the SSFSR BF column or remove it. Replace the MegaMapper staged-strategy sentence with the Sec. V numbers.

3. Fresh pass: majors

MAJOR 1 — The independent Fisher validation and the headline recast are not coherently reconciled.
Location: Abstract pp. 1–2; Sec. IV pp. 12–13; Sec. IX.E p. 29.
The paper says the independent Fisher gives r
eff
	​

≈0.99 and ∼3.2–3.5σ, while the headline keeps r=0.84 as a conservative recast. 

rt_P2

 

rt_P2

 That can be acceptable, but the present text alternates between treating r=0.84 as noise-weighted, flat-weight, conservative, and estimator-relevant.
Fix: Define one primary observable and one primary estimator. Make the headline either “local-template recast” or “shape-matched Fisher forecast,” not both. Move the other to validation.

MAJOR 2 — Cubic-order bounce transmission is overclaimed.
Location: Sec. II.C pp. 7–9; Sec. IX.E p. 29; Conclusion p. 30.
The text begins with a legitimate assumption—faithful cubic-order transfer—but then says it is “derived,” “closed,” and requires no numerical cubic bounce evolution. 

rt_P2

 For PRD, an all-orders separate-universe argument through an LQC bounce is not a substitute for an explicit third-order matching calculation unless all hypotheses are shown in the same effective theory.
Fix: Either supply the actual cubic matching/gradient-expansion derivation in the paper, or demote the claim to: “assumed, motivated by single-clock superhorizon conservation, with expected (kη
bounce
	​

)
2
 suppression.”

MAJOR 3 — The b
ϕ
	​

 and GR nuisance numbers are not calibrated enough for a “budget.”
Location: Sec. VII.B–E pp. 21–25; Figures 4–5 pp. 22.
The b
ϕ
	​

 rows use σ(f
NL
	​

)→0.9,1.0 as replacements, while GR is added in quadrature, but no joint nuisance model connects these choices. The text admits the σ
GR
	​

 values are stress-test amplitudes, not translated from SPHEREx. 

rt_P2


Fix: Rename Table V “scenario budget” rather than “measurement budget,” or provide a minimal Fisher with nuisance parameters (f
NL
	​

,b
ϕ
	​

,A
GR
	​

,b
1
	​

,b
2
	​

).

MAJOR 4 — Bayes-factor section remains too complicated and still partly inconsistent.
Location: Sec. VI pp. 16–20; Tables III–IV pp. 19, 23.
The tuned-multifield BF values are clearer than in earlier drafts, but the SSFSR values and multiple bookkeeping schemes make the section difficult to audit. Table III says entries are “exact closed-form” while also saying order-of-magnitude caution is needed. 

rt_P2


Fix: Keep one primary BF table: recommended σ
theory
	​

=1.0, broad and narrow competitor priors, with r=0.84 bookkeeping. Move all delta-prior and SSFSR point-hypothesis extremes to an appendix after recomputation.

MAJOR 5 — The abstract is not a PRD abstract.
Location: pp. 1–2.
The abstract is effectively an executive summary plus caveats plus methods plus results. It is too long and too detailed for PRD.
Fix: Compress to one paragraph of problem, one paragraph of result/scope. Move the detailed scope caveats to the Introduction or a “Summary of assumptions” box.

MAJOR 6 — Reproducibility claims need a frozen artifact.
Location: Data and Code Availability p. 30; Appendix A.
The paper refers to many scripts and JSON files, but the Zenodo DOI is “inserted at submission,” and the review PDF does not include a commit hash. 

rt_P2


Fix: Provide the exact commit hash, Zenodo DOI, and a minimal make reproduce script that regenerates Tables I, V, VIII and the key r, BF, and Fisher numbers.

4. Fresh pass: minors

MINOR 1 — Figure captions are doing too much.
Location: Figures 2, 4, 5 pp. 14, 22.
Move detailed caveats to text; captions should identify plotted quantities and scenarios only.

MINOR 2 — Notation remains overloaded.
Location: Secs. II–IV.
The paper uses r for template recovery, r
t
	​

 for tensor-to-scalar ratio, r
eff
	​

, r
cos
	​

, and ρ for Fisher correlations. This is manageable but heavy. Add a notation table.

MINOR 3 — Several “headline” ranges should be named consistently.
Location: Abstract, Secs. IV, V, VII, IX.
Use fixed labels: “SPHEREx optimistic,” “SPHEREx post-budget,” “MegaMapper ideal,” “MegaMapper design envelope,” “SDB-only cross-check.” Do not alternate between “realistic,” “conservative,” “all-combined,” and “post-budget” without a table key.

MINOR 4 — AI-assisted methodology paragraph is unusually prominent.
Location: Acknowledgments p. 35.
It is acceptable to disclose, but the wording is defensive and distracts from scientific reproducibility. Shorten it and let the artifact hash/DOI carry the verification burden.

5. Recommendation

The revision moved in the right direction: the authors now make the intended −35/16 value visible everywhere important, add Eq. (11), and provide a real Table V/Figure 2 sensitivity dashboard. But at PRD full standard, the central factor-of-two forensic claim and the forecast budget still have unresolved internal contradictions. The paper is not ready for acceptance until those are fixed.

VERDICT: MAJOR REVISIONS — The paper moved toward publishability by making the headline amplitude and budget explicit, but it still needs major tightening of the factor-of-two algebra, corrected-shape forecast propagation, and covariance/systematics treatment.