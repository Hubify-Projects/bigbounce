# EXT22 P2 chatgpt — chat: https://chatgpt.com/c/6a3e67aa-3fec-83e8-9a24-856d73646020

REFEREE REPORT — P2 REVISED
"Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"

Recommendation: MINOR REVISIONS

The revised manuscript is scientifically clear enough for publication after minor editorial and presentation fixes. I do not find a blocker or a missing control that would require substantial scientific rework. The paper now accurately frames itself as a sensitivity recast of the published Heinrich et al. SPHEREx bispectrum forecast rather than an independent survey Fisher forecast; it makes the relevant assumptions explicit; it distinguishes optimistic, realistic, and conservative systematic budgets; and it treats the Cai/Li time-ordering issue transparently, including a stress-test branch.
The principal result — that the quasi-dust matter-bounce benchmark fNL = −35/8 could be tested by SPHEREx at roughly 2.6–5σ after the stated systematic budget, with a 5.2–5.5σ optimistic bispectrum-only pre-GR/bϕ forecast — is appropriately qualified. The remaining issues are clarity, organization, and a few local wording inconsistencies, not publication-level scientific defects.

BLOCKERS
None.
I do not identify any must-fix blocker involving an unsupported load-bearing claim, missing critical control, or non-reproducibility from the manuscript itself. The central caveats — third-order bounce transmission, no prolonged post-bounce inflation, scalar-only/fermion suppression, template mismatch, bϕ marginalization, GR projection effects, and prior sensitivity of Bayes factors — are all explicitly stated.

MAJORS
None requiring major revision.
No new forecast machinery, new data analysis, or full independent in-in rederivation is necessary for this paper's stated scope, provided the authors preserve the current "sensitivity recast" framing. The Cai/Li factor-of-two discussion is load-bearing, but the manuscript no longer hides the issue: it provides an operator-algebra explanation, a stress-test branch, and a clear statement that −35/16 is not propagated as the physical headline branch. That is adequate for a forecast/recast paper, though one minor clarification below would make this still safer.

MINORS

Sec. III B, p. 8 — wording of LSS/noise weighting and squeezed weighting is locally confusing.
Fix: revise the sentence explaining why the LSS/SPHEREx-like weighting lowers r from the CMB-Fisher endpoint. As written, it says the weighting upweights large-scale modes where the templates coincide, "thereby increasing" the relative weight of intermediate/folded configurations where the mismatch is largest. That causal chain reads contradictory. State more directly that the survey/noise weighting used in the recast gives more effective weight to the configurations that drive the integrated mismatch than the signal-only CMB-Fisher weighting does.

Sec. IV and Table IV, pp. 10 and 20 — photometric-z degradation should be placed more cleanly in the systematic budget.
Fix: Table IV currently consolidates template mismatch, ϵ-correction, null-space scatter, bϕ, and GR, while photometric-z/outlier effects are discussed in prose. Add either a separate "photo-z/outliers" row or a parenthetical in the table caption stating that the Heinrich et al. σ(fNL)=0.7 already includes the baseline SPHEREx photo-z treatment, while the additional 10% catastrophic-outlier estimate is not stacked as an independent headline denominator.

Fig. 2 caption, p. 11 — the bar taxonomy is too dense and slightly hard to map onto the text.
Fix: simplify the caption into four explicit categories: naive uncorrected reference, template-corrected optimistic, post-systematic realistic envelope, and all-combined conservative endpoint. The current caption is technically understandable but overpacked and risks confusing the 2.6–5σ envelope with the 2.6–2.8σ all-combined endpoint.

Sec. VI, pp. 12–15 — Bayes-factor discussion is correct but overlong in the main text.
Fix: keep the four-corner grid, the recommended σtheory=1.0 statement, and the r≈0.84 rebooking explanation in the main text; move most of the self-consistency arithmetic and approximation-error discussion to an appendix or footnote.

Sec. VI / Table II, p. 15 — emphasize once more that the quoted Bayes factors are illustrative, not definitive evidence.
Fix: add one short sentence immediately below Table II: "These Bayes factors are prior-predictive comparisons under the stated toy competitor priors, not a full model-space evidence calculation over all inflationary alternatives."

Sec. IX.D, pp. 21–22 — the hierarchy between the bispectrum headline and the SDB running diagnostic should be stated earlier.
Fix: move the "Channel hierarchy and sub-labeling note" closer to the start of Sec. IX.D, before the numerical joint (fNL, nfNL) values. This prevents readers from mistaking the SDB-only σ(fNL)=3.08–7.06 diagnostic for a contradiction of the SPHEREx bispectrum σ(fNL)=0.7 headline.

Data and Code Availability, p. 24 — replace placeholder archival wording before submission.
Fix: replace "DOI inserted at submission" with the actual Zenodo DOI and add a commit hash or tagged release.

Appendix A.1–A.2, pp. 24–27 — make the status of the Cai/Li stress test even more explicit.
Fix: add one sentence such as: "The −35/16 row is retained only as an operator-algebra stress test; the headline forecast assumes the full in-in commutator normalization throughout."

Sec. IX.E, p. 23 — cosmic birefringence paragraph is interesting but tangential.
Fix: either shorten it or label it even more visibly as an auxiliary, non-forecast consistency note.

General presentation — reduce repeated reconciliation prose.
Fix: a light copy edit could reduce length without removing any scientific content.

Strengths

The paper is unusually transparent about scope. It repeatedly distinguishes a sensitivity recast from an independent Fisher forecast and does not overclaim SPHEREx or MegaMapper capabilities.

The assumptions behind the matter-bounce prediction are now explicit and appropriately limiting: matter domination/quasi-dust contraction, standard GR perturbations during contraction, Bunch-Davies initial state, faithful cubic-order transmission, no prolonged post-bounce inflation, and negligible fermion-sourced torsion.

The treatment of template mismatch is a genuine strength. The manuscript quantifies the local-template recovery factor r, separates CMB-Fisher and LSS/SPHEREx-like weightings, reports null-space scatter, and uses the mismatch consistently in both significance and Bayes-factor bookkeeping.

The systematic budget is transparent. The authors make clear which effects act on the numerator, which act on σ(fNL), and which are heuristic quadrature additions rather than a full joint Fisher marginalization.

The Bayesian comparison is appropriately caveated. The manuscript no longer presents the Bayes factor as a definitive model-selection result; it explains the dependence on bounce-prior width, competitor prior width, and the r≈0.84 template rebooking.

Appendix A is useful. The Cai/Li factor-of-two issue is potentially confusing and load-bearing; the revised manuscript addresses it openly and includes a single-time-ordering stress-test row rather than hiding the sensitivity.

The current-data recast is balanced. Planck PR4 and DESI constraints are correctly presented as non-discriminating at current precision, avoiding premature claims of evidence.

Overall, I recommend MINOR REVISIONS. The manuscript's scientific claims are acceptable for publication as a forecast/recast paper once the remaining clarity and presentation issues are cleaned up.
