# RCEXT P2 ChatGPT — chat: https://chatgpt.com/c/6a42cd9b-e604-83e8-bd9f-5fcdf7f18de4
VERDICT: MAJOR REVISIONS

Provider: ChatGPT (Instant/default)
PDF: RCEXT_P2.pdf (md5: 291b9956a032c5a57e12896a128e7f40)
Harvested: 2026-06-29

---

1. Recommendation: MAJOR REVISIONS

The paper is promising and unusually self-auditing, but not yet publishable at a top-journal bar because the headline 2.6–5.5σ / BF≈9–14 claims still rest on a sensitivity recast, additive-quadrature systematics, and a non-independent bispectrum forecast rather than a joint survey covariance forecast.

2. BLOCKERS

Headline significance overstates forecast status. The paper repeatedly admits the 2.6–5.5σ range is not a joint-covariance forecast, but still presents it as the main observational forecast. This must be reframed as a sensitivity envelope unless a full joint Fisher/marginalization is performed.

Cubic-order bounce transmission is assumed, not demonstrated. Assumption (d) is explicitly "verified only at linear order" and supported at cubic order only by a superhorizon scaling estimate. Since the entire fNL prediction depends on faithful cubic transfer through the bounce, this is a core theoretical uncertainty, not a caveat.

Imported Heinrich et al. σ(fNL)=0.7 is doing most of the work. The paper is a recast, not an independent SPHEREx forecast. That is acceptable, but the title/abstract/conclusions must not imply an internally derived forecast precision.

Systematic budget is heuristic. GR projection, bϕ uncertainty, photo-z, template mismatch, and ε-corrections are combined additively in quadrature without covariance. This is transparently stated, but the headline still depends on it.

3. MAJORS

Bayes factors are too headline-forward. The BF≈9–14 result is prior-sensitive and partly bookkeeping-sensitive. The paper should present it as illustrative only, not as robust model-selection evidence.

The Cai/Li factor-of-two resolution is ambitious but not fully independent. The operator-algebra argument is useful, but the paper does not rederive the full in-in integrals. The claim that −35/8 is "closed" should be softened to "supported/adopted after convention audit."

Template-overlap uncertainty is basis-measure dependent. The null-space r scatter is explicitly not basis invariant. The forecast should not lean on the stronger-looking precision of r=0.84±0.02 without making clear that this is only the chosen noise-weighted central bookkeeping.

SDB and bispectrum channels risk reader confusion. The narrative mixes SDB Fisher results, bispectrum recast, nfNL running, and template-overlap factors. A clearer "channel accounting" table early in the paper is needed.

MegaMapper discussion should be demoted. Since MegaMapper is proposed/unfunded, the 3–7σ range should not appear alongside SPHEREx as a comparable forecast.

4. MINORS

The abstract is too long and overburdened with caveats; move bookkeeping details to a forecast-summary table.
Figures on pages 11, 18, and 22 are useful, but captions are too dense and partly repeat main text.
"Mechanism-independent," "UV-completion-independent," and "minimally parameterized" should be standardized.
The cosmic-birefringence paragraph is tangential and should be cut or moved to a short appendix.
Clarify whether all public-code artifacts existed at submission or are intended Zenodo release artifacts.

5. Strengths

Strong self-audit: the manuscript openly flags assumptions, caveats, and bookkeeping choices.
The template-mismatch treatment is valuable and likely publishable as a careful recast.
The separation between bispectrum and SDB channels is scientifically important.
The Cai/Li convention audit is useful even if it should be softened.
The paper makes a falsifiable observational target clear: fNL≈−4.375 versus near-zero slow-roll.
