# P2 auto-2026-06-08_1737pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (3326 chars)
**Wall time**: 95.5s

---

Referee report on “Cosmic Birefringence from a Planck-Scale Axion-Like Particle: Predictions, Constraints, and LiteBIRD Forecasts” (6 pp)

--------------------------------------------------------------------
FINDINGS
--------------------------------------------------------------------
Key to labels:  P2-E = ESSENTIAL, P2-M = MAJOR, P2-m = MINOR, P2-n = NIT

P2-E1  
Section 2.2, p. 1, Eqs. (1)–(2) and following paragraph  
Problem:  The numerical propagation from Eq. (1) to the quoted prediction β ≈ 0.27° is internally inconsistent by almost two orders of magnitude.  
• With m/H0 ≈ 1 the Bessel factor gives (1–J0) ≈ 0.235, hence  
Δφ/fa = θi × 0.235 ⇒ β = C0 θi × 0.118 rad ≈ 6.8° (for C0 ≈ θi ≈ 1), not 0.27°.  
• The manuscript simultaneously asserts “Δφ/fa ∼ 10⁻²” to justify β ≈ 0.27°, contradicting the analytic expression.  
Required fix: Provide a self-consistent derivation showing how the 10⁻² scaling is obtained (or adopt a different fiducial m/H0), propagate the correct value into all subsequent claims (Abstract, pp. 2, 3, 6, Fig. 2).

P2-E2  
Section 2.2, p. 1 (all β expressions)  
Problem: Units of β and Δφ are never stated and the algebra mixes radians and degrees. The numerical mismatch in P2-E1 stems partly from silent unit changes.  
Required fix: State units explicitly in every equation, convert consistently, label figure axes accordingly.

P2-E3  
Section 3.2, p. 2, Eq. (3)  
Problem: Planck and ACT cover the same CMB sky; cosmic-variance covariances make the two β estimates statistically correlated. Treating them as independent in the product likelihood underestimates σ(β).  
Required fix: Either (i) include a covariance term (or at least bound its impact), or (ii) demonstrate with simulations that the correlation is negligible (< 10 % of quoted σ).

P2-E4  
Table 1 & §3.3, p. 3  
Problem: MCMC chains contain only 720–6 840 retained samples, yet tail quantities, Bayes factors and 0.1°-level parameter errors are quoted. Such sample sizes are insufficient for converged evidence estimates (Neff ≈ 10³).  
Required fix: Run ≥ O(5×10⁴) post-burn-in samples per chain, report effective sample sizes for every parameter, recompute β posteriors and Bayes factors.

P2-E5  
§3.4, p. 3  
Problem: ln B = 5.17 is presented as “evidence”, but its calculation is not reproducible: prior width, normalisation and Savage–Dickey implementation are undocumented, and the small chains of P2-E4 cannot yield a stable value.  
Required fix: Provide full computational details (prior bounds, kernel density bandwidth, number of posterior samples) and quote a robust error bar on ln B.

P2-E6  
Eq. (5), p. 2 and Abstract  
Problem: “Effective photon coupling fphoton × C0 = 1.73 ± 0.44” appears without definition of fphoton, derivation or link to model parameters.  
Required fix: Define fphoton explicitly, show how Eq. (5) follows from the data, propagate its uncertainty correctly.

P2-M1  
§3.1, p. 2  
Problem: The paper selects one of several published Planck values (Eskilt joint fit) but combines a different pair (NPIPE + ACT) for its likelihood, without justification of selection criteria.  
Required fix: State objective data-selection rules; repeat the analysis for all published Planck estimates or demonstrate that choices do not materially affect results.

P2-M2  
Table 1 notation, p. 3  
Problem: “C” appears interchangeably as C, C0, Cαγ. This obscures which anomaly coefficient is held fixed or sampled.  
Required fix: Adopt a single symbol, define once, and use consistently throughout text, tables and figures.

P2-M3  
Fig. 1, p. 4  
Problem: θi axis is unlabeled with units; β axis says “[deg]” but the caption and text use both deg and rad.  
Required fix: Label all axes with units; update caption accordingly.

P2-M4  
Fig. 2, p. 5  
Problem: The green shaded “observed 1σ band” uses 0.342 ± 0.094° yet the combined likelihood in the text is 0.242 ± 0.061°. The meaning of the band is unclear and risks mixing incompatible σ estimates.  
Required fix: State explicitly which measurement the band represents and why it is compared to a different combined posterior.

P2-m1  
Eq. (10), p. 3  
Problem: Quoted 9σ significance ignores that anticipated LiteBIRD systematics may inflate σ(β).  
Fix: Cite LiteBIRD systematic floor and quote range (e.g. 0.03°–0.05°).

P2-m2  
References, p. 6  
Problem: Two “in preparation” citations (Namikawa et al. 2025; Golden 2026b). PRD requires publicly available references.  
Fix: Replace by public arXiv numbers or remove.

P2-n1  
Duplicate phrase, Abstract line 6: “order-unity inputs … order-unity coefficient”.  
Fix: streamline wording.

--------------------------------------------------------------------
## Summary recommendation
REJECT

The manuscript’s central quantitative claim—natural prediction β ≈ 0.27° matching the data—is not supported by its own equations (P2-E1, P2-E2). Core statistical results rely on unjustified independence assumptions and severely under-sampled MCMC chains (P2-E3–E5). Several key parameters are undefined or inconsistently denoted. These are fundamental methodological flaws; addressing them would require a substantial re-derivation, new simulations and a complete rewrite exceeding the scope of a “minor revision”.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (2nd-pass review)

Key:  P2-E = ESSENTIAL, P2-M = MAJOR, P2-m = MINOR, P2-n = NIT  
(continuing numbering from the first report)

--------------------------------------------------------------------
P2-E7  
§3.4, Bayes–factor arithmetic and sign  
Problem:  For a flat prior β∈[0°,1°] the prior density at β=0 is 1 deg⁻¹.  
Using the authors’ own combined likelihood (β̂=0.242°, σ=0.061°) the posterior
density at β=0 is  

p(0)= (1/√(2π)σ) exp[-β̂²/(2σ²)] ≃ 0.0025 deg⁻¹,

so the Savage–Dickey ratio is  
ln B = ln[p(0)/π(0)] ≃ ln(0.0025) = -6.0, i.e. decisive evidence against (not
for) β=0.  The manuscript reports +5.17.  The sign is wrong and the magnitude
is off by nearly a factor of two on the log scale.  
Required fix: recompute B with reproducible code; show numerical inputs and
propagate an error bar.  All statements claiming “evidence for rotation” based
on ln B must be revised.

P2-E8  
§3.3, Eq. (8) vs Fig. 1  
Problem:  Eq. (8) quotes Caγ θi = 3.4 ± 1.1, yet Fig. 1 shows the 1-D posteriors
θi ≃ 1.33 and Caγ ≃ 13.4, whose product is ≃ 18 — a factor ≈ 5 larger than the
text.  Either the figure or the equation (and the ensuing discussion of
“order-unity” parameters) is wrong.  
Required fix: clarify which value is correct and update figure labels, Eq. (8),
and all statements that rely on the product being O(1).

P2-E9  
§3.4, prior-width dependence of ln B  
Problem:  The manuscript claims ln B = 4.48 for β∈[0°,2°] and ln B = 5.86 for
β∈[0°,0.5°].  A narrower uniform prior increases the prior density at β=0,
which must decrease (make more negative) ln B if the posterior is held fixed.
The reported trend (larger ln B for the narrower prior) violates this
monotonicity test, signalling a coding or transcription error independent of
E7.  
Required fix: redo the prior-width study and plot ln B versus Δβ to demonstrate
the expected monotonic behaviour.

P2-M5  
Fig. 1 caption vs numerical annotations  
Problem:  The caption states “Caγ × θi is centered at 3.4 ± 1.1” but the diagonal
panels in the plot annotate Caγ = 13.4… and θi = 1.33…, inconsistent with the
caption and with Eq. (8).  Readers cannot tell which numbers correspond to the
chains.  
Fix: synchronise the figure annotations with the text or regenerate the corner
plot showing the *product* explicitly.

P2-M6  
Abstract vs body: “ln B = 5.17 (indicative evidence)”  
Problem:  After correcting E7–E9 the quoted ln B value (and its interpretation
as evidence *for* rotation) will change.  The abstract will therefore be
misleading.  
Fix: make abstract values symbolic (“ln B = …”) until the final, audited
number is established.

P2-m3  
§3.2, significance wording  
Problem:  The text calls the combined result “3.9 σ from zero” while the
abstract advertises “3.6 σ”.  Only one of these can survive once the correlation
issue (P2-E3, first report) is fixed.  
Fix: choose one number, specify which likelihood it comes from, and use it
consistently.

P2-m4  
Internal cross-reference typo  
Problem:  “(indicative; prior-dependent, see Sec. 3.4)” appears *inside*
Sec. 3.4.  
Fix: change to “see discussion below” or remove the self-reference.

--------------------------------------------------------------------
These additional problems compound the already critical issues identified in
the first report.