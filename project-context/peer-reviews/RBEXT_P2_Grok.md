# RBEXT P2 Grok — chat: https://grok.com/c/cad5de13-9232-4734-9154-bafc6f110e43
VERDICT: MINOR REVISIONS

Provider: Grok (Expert tier)
PDF: RBEXT_P2.pdf | md5: 291b9956a032c5a57e12896a128e7f40
Harvested: 2026-06-29

---

Referee Report: MNRAS / PRD / JCAP (high bar)
Paper: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Author: Houston Golden
Date: 29 June 2026

Recommendation: MINOR REVISIONS

BLOCKERS: None. No fundamental flaws, uncontrolled leading systematics that invalidate the headline claims, internal inconsistencies, or unstated assumptions that undermine the core results. The work is a thorough, carefully scoped sensitivity recast with strong reproducibility provisions.

MAJORS (2)

Heuristic additive-quadrature systematic budget and the realistic significance envelope (Sec. VII, Table IV, abstract)

The consolidated budget (Table IV) and the realistic ∼2.6–5.5σ range are constructed via additive quadrature (σ_eff = √(σ_base² + Σσ_i²)). You explicitly label this a "scoping sensitivity envelope under an additive-quadrature heuristic systematic budget, not a joint-covariance forecasted measurement precision" and note that a full bispectrum joint Fisher over nuisances was not performed.

However, the headline realistic range (and its lower edge ∼2.6σ) inherits the heuristic character. Correlations among nuisances (bϕ marginalization, GR projection, photo-z outliers, etc.) could in principle shift the envelope in either direction.

Requested revision: Add a concise paragraph (Sec. VII or Conclusions) stating that (a) the additive-quadrature combination is a transparent scoping choice, (b) a full multi-tracer bispectrum joint Fisher over the systematic nuisances remains future work, and (c) the quoted 2.6–5.5σ envelope should be read as indicative/scoping. Consider a one-sentence softening in the abstract ("scoping sensitivity envelope of ∼2.6–5.5σ under the additive-quadrature heuristic budget of Sec. VII").

Status of assumption (d) — faithful cubic-order bispectrum transmission (Sec. II.C, abstract, Sec. X)

You correctly identify (d) as the weakest link: verified at linear order; cubic order supported only by a superhorizon scaling estimate (k η_bounce)² ∼ 10^{-4} giving δfNL ∼ 10^{-3}.

Requested revision: Add one sentence noting that a full numerical verification (evaluating all four Maldacena cubic integrals with bounce-modified mode functions, preserving the delicate cancellations) would be required to remove the conditional character from "robust across the bounce class." Add in the abstract (or end of Sec. I) and in the Conclusions.

MINORS (4–5 items)

- Bayes-factor prior sensitivity (Sec. VI, Table II, abstract): Add one short clause in the abstract's BF sentence ("BF values depend on assumed competitor prior width and theoretical uncertainty in the bounce prediction; see Sec. VI").
- SDB joint Fisher subsection labeling (Sec. IX.D): Make subsection title more explicit ("Subordinate scale-dependent-bias (fNL, nfNL) running discriminator — distinct Fisher matrix and tracer selection from the bispectrum forecast of Sec. IV").
- Unmodeled projection noise from non-local tails (Sec. III.B): Add one sentence in Sec. VII or Table IV caption stating this contribution is not modeled but is expected subdominant.
- Figure/table cross-referencing for significance ranges (Fig. 2, Table IV): Ensure Fig. 2 caption explicitly maps error bars to specific rows/scenarios of Table IV.
- Data/Code Availability: Zenodo DOI "inserted at submission" is standard and acceptable.

STRENGTHS (≥3)

- Rigorous operator-algebra resolution of the Cai et al. vs. Li et al. factor-of-two discrepancy (Appendix A + derivation A.1): a genuine, publishable clarification to the matter-bounce PNG literature.
- Multi-method, high-resolution quantification of template overlap r (Secs. II–III.B): 10,000-sample null-space scan, Fisher-weighted r = 0.84 ± 0.02, shape-cosine stability r_cos > 0.97, 200-realization KSW-style injection-recovery (r_meas = 0.90 ± 0.01). This level of validation is rare in forecast recasts.
- Exemplary transparency in scoping both theoretical assumptions and observational systematics: six assumptions (a)–(f) listed explicitly; (d) flagged as weakest; systematic budget presented as additive-quadrature scoping heuristic (not joint Fisher).
- Dedicated joint SDB Fisher demonstrating real degeneracy impact (Sec. IX.D): marginalizing nfNL degrades σ(fNL) by 2.0× (fixed bias) to 4.6× (bias-marginalized) with strong anti-correlation (ρ ≈ −0.87 to −0.97).
- Closed-form Bayesian model comparison with extensive validation and prior-sensitivity mapping (Sec. VI, Tables II–III): analytic derivation (Eq. 9), three independent 10^5-realization MC ensembles, continuous marginalization over σ_theory and σGR, explicit four-corner grid.

Overall: MINOR REVISIONS — primarily presentational/emphasis on heuristic budget and assumption (d) framing. The methodological transparency, multi-layered template overlap validation, operator-algebra clarification, and dedicated joint Fisher computation are strengths that meet PRD/JCAP/MNRAS standards.
