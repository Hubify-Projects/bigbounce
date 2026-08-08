chat: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a4fe194-08b0-83e8-b4f0-4e216d5c5ddb
reviewer: ChatGPT (Extended Thinking Pro) | paper: P2 v1.7.105 (36pp) | date: 2026-07-09
baseline: MINOR (R9) | movement: MINOR -> MAJOR REVISIONS (harsher / down one tier)
verdict (from raw): (1) VERDICT: MAJOR REVISIONS. BLOCKER quotes the paper's OWN hedging: per-vertex table sums to -35/16 but text concedes it 'does not claim a complete term-by-term derivation of Cais error' and the identified term is 'not by itself the full mechanism' — flags an overclaim/internal-tension (settles-exactly vs. evidence-favors), NOT a math/fabrication error. The derivation table is credited as internally summable to -35/16. Truth-audit target: claim-strength calibration.
---RAW---
(1) VERDICT: MAJOR REVISIONS

(2) BLOCKERS

Appendix A / Tables VI–VII: the factor-of-two resolution is not yet publication-proof. The per-vertex table sums to −35/16, but the text also admits the identified +(99/128)∑
i
	​

k
i
3
	​

 term is “not by itself the full mechanism” and that the paper does “not claim a complete term-by-term derivation of Cai’s error.” Proposed fix: either give the full algebraic map from Cai’s printed polynomial to the vertex sum and show exactly how −35/8→−35/16, or downgrade the claim from “settles/resolves exactly” to “evidence favors −35/16.” 

w2_P2

Appendix A / Sec. II.C: the manuscript simultaneously says Li’s printed polynomial agrees coefficient-for-coefficient with Cai’s printed polynomial at c
s
	​

=1, that both printed polynomials yield −35/8, and that Li’s Eq. 5.1 independently gives −35/16. This is a serious unresolved internal tension. Proposed fix: explicitly reconcile Li’s polynomial, Li’s Eq. 5.1, and the local-limit extraction step in one derivation.

Sec. II.C / IX.E / Conclusion: cubic-order bounce transmission is still overstated. The paper says transmission is “derived” to ≲10
−3
 from single-clock nonlinear ζ-conservation, but this relies on nontrivial assumptions about LQC effective dynamics, gradient expansion validity through the bounce, and absence of entropy/transient growing modes. Proposed fix: present it as a controlled argument/assumption, not a closed derivation, unless a model-specific cubic evolution calculation or theorem with all hypotheses verified is supplied.

(3) MAJORS

Sec. IV: the SPHEREx recast mixes three distinct quantities—flat-weight shape overlap r=0.84, survey-optimal recovery r
eff
	​

≃0.99, and imported Heinrich σ(f
NL
	​

)=0.7. The paper explains the distinction, but the headline still depends on choosing the conservative r=0.84 while also citing the independent Fisher as validation. Proposed fix: make the headline forecast one internally consistent pipeline, and relegate the alternate recovery factor to a clearly non-headline cross-check.

Sec. VII / Table V: the systematic budget is not a true joint forecast. Additive quadrature, proxy GR correlations, b
ϕ
	​

 widening, and GR-projection covariance are stitched together from heterogeneous assumptions. Proposed fix: either perform the joint Fisher over at least (f
NL
	​

,b
ϕ
	​

,A
GR
	​

), or label the 1.3–2.75σ interval more prominently as a heuristic sensitivity envelope.

Sec. V: MegaMapper projections are too imprecise for the same prominence as SPHEREx. The manuscript admits MegaMapper is proposed, unfunded, and design-uncertain, yet quotes 1.5–3.5σ and ideal 3.7–3.85σ. Proposed fix: move MegaMapper to a short outlook section and avoid presenting it as a calibrated forecast.

Sec. VI / Table III: Bayes factors are over-elaborated relative to their evidentiary value. They are strongly prior-driven and based on illustrative competitor priors, yet the abstract-level BF 9–14 risks sounding like robust model selection. Proposed fix: demote Bayes factors to an illustrative appendix or state in the abstract that they are prior-volume diagnostics, not evidence forecasts.

(4) MINORS

Abstract: too long and overloaded with caveats, code artifacts, and internal bookkeeping. Proposed fix: cut to the corrected f
NL
	​

, SPHEREx recast, main caveat, and headline significance.

Sec. II: the null-space discussion is useful but too detailed for the main text. Proposed fix: move most coefficient-basis and scan-radius discussion to an appendix.

Table V: multiple rows are not cumulative in the same sense. Proposed fix: separate “amplitude effects,” “denominator effects,” and “illustrative marginalization alternatives.”

Sec. IX.B: “A detection of f
NL
	​

≈−4” is inconsistent with the corrected central value −2.1875. Proposed fix: change to “≈−2” or explicitly mark −4 as the discarded Cai value.

(5) Strengths

The paper is unusually transparent about scope, imported forecasts, and systematic fragilities.

The corrected −35/16 value, if fully certified, is a valuable clarification for matter-bounce phenomenology.

The SPHEREx sensitivity recast is scientifically interesting and timely.

The manuscript makes a serious attempt to distinguish optimistic, realistic, and conservative significance levels.

Code/data availability and auditability are stronger than typical theory-forecast papers.

(6) Specific scrutiny

The per-vertex table is internally summable and supports −35/16, but it does not yet close the Cai–Li discrepancy exactly because the manuscript itself concedes that the identified polynomial discrepancy is not the complete mechanism. The SPHEREx recast is useful but not yet a self-contained forecast. The MegaMapper section should be treated as speculative outlook, not a firm forecast.
