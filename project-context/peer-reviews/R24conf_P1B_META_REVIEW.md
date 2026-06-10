# P1B R24conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 339.1s

---

Meta-referee report for PRD submission “Technical Verification Companion to the ECH Spin‑Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator‑ALP Model”

Below I list issues that, to the best of my reading, are not covered by any of the five prior referee reports. I focus on cross‑section consistency, end‑to‑end arithmetic chains, hidden assumptions, and missing robustness tests.

P1B-META-E1
Severity: ESSENTIAL
Section/page: Table I (p. 3), Sec. III (pp. 2–5), Fig. 2 (p. 6)
Why others missed it: Prior reports asked to specify the DES‑Y3 S8 prior numerically but did not audit the implied pull quantitatively.
Problem (quote): “Full‑tension … S8 = 0.814 ± 0.008 … Planck+BAO+SN S8 = 0.831 ± 0.018 … the full‑tension combination includes … DES‑Y3 S8 Gaussian.”
Required fix: Disclose the exact Gaussian prior used (central value and σ) and show a simple, reproducible pull check: e.g., overlay the Planck+BAO+SN S8 posterior with the Gaussian prior and the full‑tension posterior in one panel, and quantify the expected naïve inverse‑variance combination (using your Planck+BAO+SN result and the DES‑Y3 prior). As is, a naïve combination of 0.831±0.018 with 0.776±0.017 would land at ≈0.802±0.012, which is notably lower than 0.814±0.008. Either demonstrate why the joint parameter degeneracies legitimately shift to 0.814, or correct the chain configuration/description.

P1B-META-M1
Severity: MAJOR
Section/page: Sec. III (p. 3), Sec. V.A (p. 8), Table III (p. 9)
Why others missed it: The .native vs .clik lensing inconsistency was flagged, but the mixed‑release pairing itself wasn’t.
Problem (quote): “Planck NPIPE (PR4) CamSpec high‑ℓ TTTEEE + Planck 2018 low‑ℓ TT/EE + Planck 2018 lensing … the standard pairing in the Cobaya likelihood stack.”
Required fix: Provide a demonstrated justification that the PR4 (NPIPE) high‑ℓ + 2018 low‑ℓ/lensing mixture does not bias ΔNeff/H0/S8 at the quoted precision. Either add a short test swapping low‑ℓ TT/EE and lensing to PR4‑consistent counterparts (or to Commander/SimAll for low‑ℓ) and show shifts <0.2σ for the headline parameters, or clearly state this as a limitation.

P1B-META-M2
Severity: MAJOR
Section/page: Sec. IV (pp. 6–8)
Why others missed it: One reviewer noted lack of an analytic −CBB derivation; none noted that the injection/template shapes are internally inconsistent in the robustness test.
Problem (quote): “Synthetic skies: … BB component (CBBℓ = 0.05 CEEℓ). … Robustness: replacing … CBBℓ = 0.05 CEEℓ proxy with a CAMB lensed‑ΛCDM BB spectrum recovers β̂ = 0.251° (bias −0.019°), consistent with the analytic −CBB template‑mismatch estimate…”
Required fix: This robustness change improves the fit even though the injected BB shape stays 0.05 CEE while the template switches to CAMB BB, i.e., the template/injection shapes are now mismatched. Either (a) re‑run a matched injection (CAMB‑lensed BB in the maps and in the template) to isolate the role of the −CBB term cleanly, or (b) explicitly state that any nonzero −CBB term (even shape‑mismatched) reduces the multiplicative bias and quantify the residual shape‑mismatch effect. As written, the attribution to “template‑mismatch” is not established.

P1B-META-M3
Severity: MAJOR
Section/page: Sec. VI (pp. 9–11), Appendix C (p. 13)
Why others missed it: Prior reviews noted prior‑driven posteriors but not the choice of angular prior itself.
Problem (quote): “θi: uniform prior on [0.01, π]. … The strict θi ≤ 0.1 sliver … carries only 0.33% of the posterior mass…”
Required fix: Justify the choice of a flat prior in θ rather than in, e.g., cosθ (which is uniform over the vacuum manifold S¹) or over the energy density proxy 1−cosθ. Show the impact of changing to a cosθ‑flat prior (or at minimum discuss) on the inferred Cαγ and ma posteriors given the single‑datum Gaussian likelihood. This materially affects how “natural” the required misalignment looks and the fraction of posterior mass in the spectator regime.

P1B-META-M4
Severity: MAJOR
Section/page: Sec. VI (pp. 9–10)
Why others missed it: Others critiqued language about “naturalness,” but not the loss of periodicity in the likelihood model.
Problem (quote): “Likelihood: a Gaussian summary likelihood on βobs = 0.342° ± 0.094° … βfree = 0.344° ± 0.10°.”
Required fix: Explicitly address the periodicity of uniform polarization rotation (β ≡ β + n×90° for E/B; small‑β Gaussian is fine near 0, but tails are not strictly Gaussian/linear). At least note that the β‑likelihood is approximated as Gaussian around zero and justify that this is harmless at 0.3° with σ ≈0.094°. Ideally, show that wrapping/periodicity does not change the posterior at the quoted precision.

P1B-META-M5
Severity: MAJOR
Section/page: Sec. III (p. 5) “MB–H0 joint‑posterior offset check”
Why others missed it: Others checked arithmetic; none flagged the hidden conditioning on the degeneracy direction.
Problem (quote): “sn.pantheonplus enforces a soft constraint on … MB − 5 log10(h) ≈ const… This offset is ∼ 3.2σ relative to the chain’s σMB = 0.049… the same Hubble tension manifesting in the MB axis…”
Required fix: The 3.2σ figure uses σMB only and ignores the covariance of MB with H0 along the SN degeneracy direction (and the uncertainty in the Pantheon+ constraint). Provide the uncertainty in the degenerate combination (MB − 5 log10h), not just σMB, and report the significance along that axis; otherwise the “3.2σ” is not a properly conditioned statement.

P1B-META-M6
Severity: MAJOR
Section/page: Sec. IV (pp. 6–7), Footnote 3
Why others missed it: Prior reviews asked you to clarify ΔP convention but not units domain.
Problem (quote): “∆P = 10 µK·arcmin white noise … σpix = ∆P/√Ωpix … no √2 factor; … identical for Q and U.”
Required fix: State explicitly that ∆P is in thermodynamic CMB units (not antenna K) and that mapbandpass/colour‑correction issues are irrelevant here. Include one sentence confirming the unit consistency between synfast (thermodynamic µK_CMB) and your ∆P to σpix conversion. This avoids hidden unit drift at the integrated pipeline level.

P1B-META-m1
Severity: MINOR
Section/page: Sec. IV Fig. 3 (p. 7) and text (pp. 6–7)
Why others missed it: They focused on estimator definition; not on plotting completeness.
Problem (quote): “per‑realization σβ was not recorded in the original canonical fsky = 0.32 artifact, so that point is plotted with the mean only…”
Required fix: Add the measured σβ from the dedicated 500‑MC re‑run (0.046°) to the plotted point or include an inset table in the caption. As plotted, the canonical point lacks error bars while neighbouring points have them; this invites misinterpretation.

P1B-META-m2
Severity: MINOR
Section/page: Sec. VI (p. 10)
Why others missed it: Others checked the CaγΔφ/fa product; not this small closure inconsistency.
Problem (quote): “the required coupling extends well beyond the Caγ ∈ [1, 30] prior … we reran … Caγ ∈ [4, 60] … the dropped [1, 4) interval lies entirely below the EOM‑required minimum ≈8.6…”
Required fix: Close the arithmetic by harmonizing all places that quote the “required” Caγ band. Where you state “≈8.6–160” elsewhere, add a parenthetical that the continuous‑prior analysis only covers [4,60], and explicitly note that corners with Δφ/fa ≲0.17 would require Caγ >60 and thus lie outside your continuous‑prior scan.

P1B-META-m3
Severity: MINOR
Section/page: Sec. V Table II (p. 4), Sec. V.A (p. 8)
Why others missed it: They asked for a parameter/prior table but not this specific definition.
Problem (quote): “S8 … listed in tables and figures without explicit definition.”
Required fix: Define S8 once in the text and in the Table II caption, e.g., “S8 ≡ σ8 (Ωm/0.3)1/2,” and confirm this is how Cobaya/GetDist compute it in your runs. This is necessary for reproducibility of any S8 prior application and for cross‑study comparisons.

P1B-META-N1
Severity: NIT
Section/page: Sec. IV (p. 6)
Why others missed it: They focused on weighting and ℓ‑range.
Problem (quote): “No real Planck map enters the Monte Carlo, and no instrumental beam is applied (the synthetic skies and the recovery template share the same spectra, so a common beam would cancel in the β estimate).”
Required fix: Add a clause that this argument neglects pixel‑window smoothing; acknowledge that, at Nside=512, the HEALPix pixel window introduces additional small‑scale suppression that is present in both the simulated maps and any EE template derived from binned spectra. State whether you deconvolve the pixel window in the decoupled spectra before template fitting. This avoids a latent “beam/pixel window” mismatch silently entering the MC bias.

Meta-review recommendation
MAJOR REVISIONS

Union of all six reviews (five prior + this meta‑review) surfaces multiple essential/major items: fabricated or inaccurate citations and dataset naming, estimator definition/ℓ‑range inconsistencies, missing DOI‑archival deposition, version‑history prose in the body, lensing‑likelihood inconsistency across chains, and the S8‑prior pull/definition gap noted here. I count ~10–15 blockers (ESSENTIAL/MAJOR combined) that must be addressed before the work could pass external peer review. With these corrected—and the narrative tightened as suggested by several reviewers—I’m moderately confident the paper’s technical content (as a verification note) would withstand external scrutiny; however, the citation corrections and estimator/likelihood harmonization are non‑negotiable for PRD.