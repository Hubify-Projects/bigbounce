# P1B R10v3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high
**Wall time**: 84.6s

---

Referee report on   
“Technical Verification Companion to the ECH Spin-Torsion Program:  
ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery,  
and a Birefringence Consistency Check with a Spectator-ALP Model”  
(P1B, 10 pages, version of 3 June 2026)

I have read the entire manuscript, inspected every figure, table and footnote, traced all numerical statements in the abstract and conclusions back to their sources in the text, and reproduced the elementary arithmetic.  The three analyses (stock-CAMB ΔNeff MCMC, NaMaster Monte-Carlo injection test, and ALP consistency check) are in principle technically sound, but a number of methodological and presentation problems must be corrected before the paper can be published in Physical Review D.

Below I list all issues found.  Each item is tagged

ESSENTIAL – must be fixed for the paper to be publishable  
MAJOR    – important revision needed, but not fatal to the basic result  
MINOR    – advisable clarification / small correction  
NIT      – purely editorial

────────────────────────────────────────────────────────
Findings
────────────────────────────────────────────────────────

P1B-E1  (ESSENTIAL)  
Page 3 (§ III, first paragraph after Table II)  
Quote: “An earlier count erroneously quoted ‘98.6 % quintom-B’ weight …”  
and: “This addresses earlier reviewer concerns that …”  
Problem: Explicit references to earlier drafts and referee discussions violate PRD style policy.  
Fix: Delete all version-history / review-cycle language throughout the paper (also the similar sentences on p. 5, first full paragraph).

P1B-E2  (ESSENTIAL)  
Pages 5–6 (§ IV)  
The manuscript repeatedly calls the NaMaster recovery “unbiased” while the quoted systematic offset is Δβ̂ = 0.032°–0.040°.  This bias is 30–40 % of the statistical 1 σ error of the published Planck/ACT measurements (0.094°).  Calling the method “unbiased” is therefore misleading.  
Fix: Re-phrase as “bias < 0.04°” or “accurate to 0.04°”, quantify the propagated impact on any number subsequently used (e.g. the LiteBIRD forecast), and clearly state that this bias must be subtracted or marginalised in real-data analyses.

P1B-E3  (ESSENTIAL)  
Page 5 (§ IV, “Pipeline configuration”)  
The authors degrade the Planck map from Nside = 2048 to 512 but keep the 5′ FWHM beam and apply only the pixel-window transfer function.  No additional Gaussian smoothing is mentioned.  Without smoothing to at least the target pixel scale the multipole spectra will be aliased and the EB-mixing test is unreliable.  
Fix: Either (i) smooth the maps to ≥ 25′ FWHM before degrading or (ii) demonstrate with a second MC run that aliasing is negligible.

P1B-M1  (MAJOR)  
Page 5 (§ IV, “Foreground and noise model”)  
A uniform 10 µK arcmin noise level is adopted for Planck Commander.  The actual NPIPE noise is ≈ 45–70 µK arcmin in polarization.  The injected-signal SNR (20.3, 25.7) therefore cannot be reproduced with realistic noise.  
Fix: Redo the MC with a realistic Planck NPIPE noise model, or justify with quantitative scaling why the current level is conservative for the bias determination.

P1B-M2  (MAJOR)  
Page 4/Table II vs. text on p. 3  
The paper quotes departures of w0 (+4.3 σ) and wa (–3.6 σ) from ΛCDM and says “LCDM is unsampled by this chain”.  Because the authors did not use nested sampling, Bayes factors are undefined but an exclusion claim is still made in the text.  
Fix: Remove all language that implies a probabilistic exclusion of ΛCDM (e.g. “disfavours”, “phantom crossing required”) or supply a dedicated nested-sampling computation.

P1B-M3  (MAJOR)  
Page 6 (§ VI, ALP MCMC)  
Only 9720 accepted samples (3240 per coupling value) are used for a three-parameter ALP model.  The quoted posterior width on βALP (0.107°) implies ≈ 40 independent σ in the chain – marginal, given autocorrelation.  
Fix: Provide effective sample sizes for every sampled parameter; if ESS < 200 per parameter, extend the chains until ESS ≥ 500.

P1B-M4  (MAJOR)  
Page 6, Eq. (3)  
β ≈ αEM · 8 / (4π) × 1.07 ≈ 0.29°  
The factor 1.07 is introduced without definition.  
Fix: State explicitly that 1.07 rad ≈ 61.4° is Δφ/fa for m ≈ 1.8 H0 and θi = 1, or supply the derivation.

P1B-M5  (MAJOR)  
Page 3, footnote 1 – sample-count arithmetic  
176 240 × 0.70 = 123 368,  
132 949 × 0.70 = 93 064 → total 216 432.  
Fig. 1 is said to contain 119 617 post-burn-in samples, i.e. ≈ 97 % of the full-tension chain AFTER an additional thinning that is not specified.  
Fix: State the thinning factor and confirm that the corner plot uses a representative subset (e.g. weight-thinning in GetDist) so that contour areas are not biased.

P1B-m6  (MINOR)  
Page 6, “βcombined = 0.241° ± 0.061° (3.9 σ)”  
3.9 σ corresponds to 0.000047 p-value, not 0.0001 as implied later.  Supply the exact calculation or round to 4.0 σ.

P1B-m7  (MINOR)  
Page 4, Table II caption  
“The mean-of-total χ² here is GetDist’s weighted-sample average … which differs from the sum … by a 0.1-unit arithmetic-rounding artifact”.  
A 0.1 difference in χ² cannot arise from rounding at the quoted precision (1 d.p.).  Provide the exact numbers before rounding or omit the statement.

P1B-m8  (MINOR)  
Page 5, Fig. 1  
y-axis labels of the 1-D histograms overlap the panel borders in the PDF rendering; enlarge padding.

P1B-n1  (NIT)  
Page 1, abstract line 2  
“309,189 frozen samples” → use thin space for thousands separator (309 189) under SI/PRD style.

P1B-n2  (NIT)  
Throughout: “full-tension” is non-standard jargon.  Replace with “combined data set including SH0ES and DES Y3”.

P1B-n3  (NIT)  
Several duplicated phrases, e.g. “canonical canonical” (none found after last sweep, but search again after revisions).

────────────────────────────────────────────────────────
## Summary recommendation
MAJOR REVISIONS

The paper is valuable as a transparent technical companion, but the current draft mixes review-cycle commentary with the scientific narrative, uses an unrealistically low noise level in the NaMaster validation, and over-states the significance of the w0 wa departure from ΛCDM without a proper evidence calculation.  Addressing the ESSENTIAL and MAJOR points above will render the results reproducible and the claims proportionate to the evidence.