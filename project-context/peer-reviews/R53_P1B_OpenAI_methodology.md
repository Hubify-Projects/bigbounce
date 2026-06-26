# P1B R53 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R53_P1B/paper1b_mcmc_companion.pdf` md5=9a4aa5f5 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4747 chars)
**Wall time**: 338.6s

---

Referee report on “Technical Verification Companion to the ECH Spin‑Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator‑ALP Model”

I have carefully read the full manuscript, checked equations for dimensional consistency, recomputed all explicitly quoted statistics that can be reconstructed from the paper, and audited the figures/tables against the text. Below I list all findings with IDs, severity, exact locations, the specific issue, and the required fixes.

ESSENTIAL FINDINGS

P1B-E1 (Sec. VI, p.16, LiteBIRD paragraph)
Problem: Incorrect variance combination written inside a square root.
Quoted text: “|0.342 − 0.27|/√0.032 + 0.0942 ≈ 0.7σ”
Issues:
- The terms under the root must be variances (squared uncertainties). As written, “0.032” and “0.0942” are ambiguous and numerically wrong.
- Correct combination for Δβ = 0.072° with σLB = 0.03° and σobs = 0.094° is 0.072 / sqrt(0.03^2 + 0.094^2) = 0.072 / 0.0987 ≈ 0.73σ.
Required fix:
- Replace the expression with “|0.342 − 0.27| / sqrt(0.03^2 + 0.094^2) ≈ 0.73σ”.
- Ensure all other instances (if any) use squared uncertainties under the root and carry units explicitly where helpful (degrees).

P1B-E2 (Sec. VI, p.15; Appendix C, p.20; Fig. 4 caption p.18)
Problem: Factor‑of‑10 error in mapping the mass prior log10(ma/eV) ∈ [−35, −30] to m/H0.
Quoted text/locations:
- Sec. VI (Ωa computation subsection): “For ALP masses in the scan prior m/H0 ∈ [7 × 10−3, 7 × 10^2]…”
- Fig. 4 caption: “… the mass prior corresponds to m/H0 ≈ 7×10−3 to 7×10^2 for H0 = 1.44×10−33 eV”
- Appendix C: “log10(ma/eV) ∈ [−35, −30] (m/H0 ≈ 7×10−3 to 7×10^2)”
Issue:
- With H0 ≈ 1.44×10^−33 eV, 10^−35 eV / H0 = 6.94×10^−2, not 7×10^−3. The correct mapping is m/H0 ≈ 6.9×10^−2 to 6.9×10^2.
Required fix:
- Correct the lower bound to 6.9×10^−2 (or 0.069) everywhere it appears (text, caption, Appendix C).
- Recheck and amend any dependent statements (e.g., onset regime comments, “still frozen” assertion) that rely on the incorrect lower bound.

P1B-E3 (Appendix A: Data and Code Availability, pp.17–19)
Problem: Non‑final archival references; “DOI assignment is pending” and mutable repository paths dominate the provenance.
Issue:
- PRD requires stable, citable data/software resources. “Pending DOI” and mutable HuggingFace dataset URLs are not acceptable at acceptance.
Required fix:
- Mint permanent DOIs (e.g., via Zenodo) for the exact versions of: (i) frozen MCMC chains backing Table I; (ii) NaMaster MC artifacts backing Fig. 3; (iii) ALP chains backing Table IV/Fig. 4; and (iv) any auxiliary artifacts used to compute quoted diagnostics.
- Replace “pending” language with finalized DOIs in the paper. Move internal pathnames (e.g., reproducibility/... .json) to a short “artifact map” in Supplemental Material or a concise data‑release note referenced by DOI.

MAJOR FINDINGS

P1B-M1 (Sec. V.A and throughout; Table III, p.12; Conclusions p.16)
Problem: Mixed Planck releases in the primary frozen chains.
Issue:
- The headline ΛCDM+ΔNeff constraints are obtained with PR4/NPIPE high‑ℓ paired with 2018 low‑ℓ EE and lensing. Although a PR4‑consistent rerun (planck 2020 lollipop.lowlE + planckpr4lensing) is reported to agree at 0.04σ, the primary reported/frozen chains remain the mixed‑release ones.
Required fix:
- Either (a) promote the PR4‑consistent rerun to be the headline result (with frozen chains archived and cited), or (b) include both sets side‑by‑side in Table I with explicit “release‑pairing robustness” language and confirm all quoted ΔNeff/H0 figures are stable at the stated precision.

P1B-M2 (Sec. IV, p.9–11; Fig. 3 caption p.9–10)
Problem: Estimator dependence and “bias floor” nomenclature.
Issue:
- The unweighted χ^2 estimator is adopted to match “canonical scripts,” but this choice drives most of the ~12% multiplicative bias, whereas inverse‑variance weighting reduces the bias by ~80% (to −0.006°).
- The text repeatedly calls 0.040° an “observed pipeline bias floor,” which is estimator‑dependent and not universal.
Required fix:
- Pre‑declare the estimator at the start of Sec. IV (and in the abstract parenthetical) as “unweighted χ^2 over bandpowers.”
- Add the inverse‑variance‑weighted recovery number for the canonical configuration (−0.006°) to the main text and/or Fig. 3 caption.
- Replace “bias floor” with “observed bias for the unweighted estimator on these MCs”; clarify explicitly that the bias depends on estimator weighting and the injected BB shape.

P1B-M3 (Sec. VI, p.15; Eq. (9) discussion)
Problem: Under‑justified claim on anharmonic corrections to Ωa.
Quoted text: “… anharmonic corrections at O(θi^2/12) shift Ωa by ≲ 5% for θi ∼ 1 …”
Issue:
- For θi ~ 1 rad, the small‑angle expansion is not obviously ≤5% accurate without a reference or explicit calculation; near π the corrections are large. Even at θi ≈ 1 the statement needs quantitative backing.
Required fix:
- Provide a citation quantifying anharmonic corrections in this regime or a short derivation/plot that demonstrates the ≤5% claim for θi ≈ 1 under your potential and mass range. Otherwise, weaken the claim (e.g., “order‑few‑percent for θi ≲ 1”) and/or restrict its scope.

P1B-M4 (Sec. IV, p.11)
Problem: Claim “Restricting the fit to bins with ℓ ≤ 1024 changes nothing (0.238°)” lacks a number or plot.
Issue:
- The statement is qualitative in the text; a precise delta is not shown in a table/figure.
Required fix:
- Add the explicit recovered angle for the ℓ ≤ 1024 restriction (e.g., 0.2380° vs 0.2383°; Δ=0.0003°), either in the text or as a small inset/table, to substantiate the claim.

P1B-M5 (Sec. III footnote 1, pp.3–5; Table I caption p.5)
Problem: Convoluted and partially inconsistent burn‑in/sample‑count narrative.
Issue:
- The paper carries multiple burn‑in percentages (20% vs 30%), mixed per‑chain vs combined counts, and different post‑burn‑in totals depending on tool. This is hard to follow and invites confusion.
Required fix:
- Consolidate the sampling details in one Method subsection: report (i) raw accepted samples; (ii) the single burn‑in fraction actually used for the final posteriors; (iii) post‑burn‑in counts; and (iv) the definition of ESS used (weight‑expanded Sokal vs integrated autocorrelation). Remove or relegate ancillary variants to Supplemental Material.

P1B-M6 (Sec. II/Table I caption p.5–6)
Problem: “2.6σ two‑Gaussian tension” between S8 posteriors and DES‑Y3; the paper also quotes overlap integrals 0.05 and 0.12 without a compact reproducible definition.
Required fix:
- In addition to the overlap integral, include the straightforward Δ/σcomb calculation in the text (by my recomputation 2.5–2.6σ). Provide the formula for the overlap integral p = ∫min(p1, p2) and a one‑sentence recipe (grid, spacing) or move this to Supplemental with a data file of the 1D marginals for exact reproducibility.

P1B-M7 (Appendix A, pp.17–19; throughout the paper where internal paths/versions occur)
Problem: Overexposure of repository internals and process notes in the main paper.
Issue:
- Numerous internal pathnames, commit hashes, file‑bug narratives, and “pod” run identifiers appear in the body and appendices. PRD papers should point to concise, archival records rather than detailed development logs.
Required fix:
- Move detailed pathnames, CHANGELOG excerpts, and the column‑permutation bug narrative to an external, DOI‑archived “data release” note. In the paper, keep a succinct Data Availability paragraph with the minimal stable DOIs and a one‑paragraph description.

MINOR FINDINGS

P1B-m1 (Abstract p.1; Sec. IV p.8–11)
Problem: SNR terminology.
Issue:
- Although explained later, the abstract mentions “pipeline template‑fit SNR (e.g., 20.32)” which could still be misread as detection significance.
Required fix:
- In the abstract parenthetical, change to “template‑fit SNR on MC injections (not a sky detection significance)” to eliminate residual ambiguity.

P1B-m2 (Sec. IV, Eq. (1), p.8)
Problem: Notation switch between sin(2β)cos(2β) and ½ sin(4β).
Required fix:
- Add a parenthetical “(½ sin 4β = sin 2β cos 2β)” immediately below Eq. (1) to prevent reader doubt about consistency.

P1B-m3 (Sec. VI, p.14)
Problem: Coupling–displacement product.
Issue:
- You derive Caγ Δφ/fa ≈ 10.3 from βobs and α/(4π). Add the explicit numerical conversion βobs = 0.342° = 5.97×10^−3 rad in‑line to aid the reader.

P1B-m4 (Fig. 4 caption, p.18)
Problem: Caption includes an external dataset DOI unrelated to this figure (Galaxy Zoo DECaLS) and various repository pointers.
Required fix:
- Remove extraneous DOI and repository pointers from the caption; keep captions focused on the figure content.

P1B-m5 (Appendix C, p.20; Table IV caption p.17)
Problem: ESS definition.
Required fix:
- Define ESS precisely once (e.g., “weight‑expanded Sokal ESS from the integrated autocorrelation time”) and ensure the same definition is used across the paper.

NITS

P1B-n1 (throughout)
Problem: Minor hyphenation artifacts (foreground￾free, etc.) and inconsistent “≈/≃” usage.
Required fix:
- Clean hyphenation after final typesetting; standardize to “≈”.

P1B-n2 (Sec. VI, p.13)
Problem: Minor rounding drift: 5.81×10^−4×8×1.06 = 4.93×10^−3 rad = 0.2825°, text says “≈ 0.28°”.
Required fix:
- Optionally show 0.283° to keep three significant figures consistent with inputs, or keep 0.28° and add “(0.2825°)” in parentheses.

Abstract-last drift sweep (pattern‑045)
I re‑checked each abstract claim against the body:
- All ΛCDM+ΔNeff figures and caveats match Table I and Sec. III/V.
- NaMaster bias numbers match Sec. IV and Fig. 3; the “not a sky significance” caveat is present.
- Spectator‑ALP statements (fa ~ MPl; prior box; m ≫ H0 in posterior at Caγ=8; spectator tuning; not an ECH‑distinct prediction) match Sec. VI/Table IV. However, the mass‑prior mapping error (P1B‑E2) must be corrected globally.
- No model‑preference claim is made; Bayes‑factor deferral is consistent.

Provenance surfaces (patterns 046/047)
- Replace “pending” DOIs with final DOIs; compress internal pathnames and bug logs to a succinct, archival data‑release pointer (P1B‑E3, P1B‑M7).

Uncomputed quantitative claims (pattern‑048)
- Add the explicit ℓ ≤ 1024 restriction value (P1B‑M4).
- Add explicit formula/numbers behind the S8 overlap integral and the 2.6σ (P1B‑M6).

Standalone‑reader test
- The paper is self‑contained for its three verification tasks (ΔNeff proxy, pseudo‑Cl recovery on MC skies, ALP consistency check). Dependence on Paper I(a) is limited to motivation and is acceptable.

Effect sizes
- Good practice is followed for the w0wa example (1.7% H(z=0.5) difference). ΔNeff is a parameter constraint; no effect size needed. The MB–H0 degeneracy line offset is correctly flagged as descriptive only.

Length
- The main text is acceptable in length; however, many repository‑path/process details should be moved to Supplement/archival note (P1B‑M7). With that clean‑up, the paper would be more concise without losing reproducibility.

## Summary recommendation
MAJOR REVISIONS

The manuscript is generally careful about scope and statistical caveats and contains valuable methodological verification. However, there are several essential corrections required before the paper can meet PRD standards: (i) fix the incorrect variance combination in the LiteBIRD separation formula; (ii) correct the factor‑of‑10 error in the mass‑prior mapping to m/H0 (multiple locations); and (iii) replace “pending”/mutable resource pointers with finalized, DOI‑archived datasets/software. In addition, several major presentational/methods clarifications are needed (estimator‑dependence in the NaMaster bias; consolidation of sampling/burn‑in accounting; mixed Planck release pairing). With these addressed and minor/nit corrections implemented, the paper will meet PRD’s methodological rigor and reproducibility expectations.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS (fresh-eyes audit)

ESSENTIAL FINDINGS

P1B-E4 (Sec. IV, Eq. (1), p.8; terminology throughout Sec. IV, Fig. 3 caption)
Problem: Dimensionally inconsistent “χ^2” usage.
Issue:
- Eq. (1) is called χ^2 but omits the per-bin variances. As written it is a sum of squared residuals with units of Cℓ^2, not a dimensionless χ^2 statistic.
Required fix:
- Either (a) rename it to “unweighted sum of squared residuals (SSR)” everywhere, or (b) explicitly normalize by the per-bin variances σb^2 to make it a true χ^2. Update text and the Fig. 3 caption to match the chosen nomenclature.

MAJOR FINDINGS

P1B-M8 (Sec. IV, footnote 4 and main text around the sky-fraction sweep; Fig. 3 caption)
Problem: Inconsistent “per‑realization SNR” notation vs arithmetic.
Issues:
- The text states “per‑realization angle‑recovery ratio β/σβ … ≈ 5.2 at fsky = 0.32,” but this 5.2 value equals |β̂|/σβ = 0.238/0.046, not β/σβ = 0.27/0.046 ≈ 5.9 as written.
- At fsky = 0.85 and 0.65, the same phrase “β/σβ” is used for values 8.1 and 7.2; it is unclear whether β or |β̂| is used.
Required fix:
- Define a single quantity unambiguously (either |β̂|/σβ or βinj/σβ), use it consistently, and correct the numbers and symbols accordingly. If both are shown, present both with clear labels and values.

P1B-M9 (Sec. VI, p.13–14; consistency of “natural box” examples)
Problem: Example parameter point outside the stated “natural” mass range without explicit flag.
Issue:
- You define a “natural” box m/H0 ∈ [1, 3], θi ∈ [0.5, 2]. Later, to reach Δφ/fa ≈ 1.06 you cite “m ≈ 3.9 H0, θi = 1” (outside the stated box) and emphasize that this reproduces Δφ/fa = 1.0601. This can mislead readers about what is achievable inside the stated envelope.
Required fix:
- Either (a) provide an explicit in‑box example (e.g., θi and m/H0 within [0.5,2]×[1,3]) that yields a comparable Δφ/fa, or (b) clearly label m ≈ 3.9 H0 as outside the “natural” mass prior and explain why the outside‑box example is chosen.

MINOR FINDINGS

P1B-m6 (Sec. IV, footnote 4 and surrounding text; sky‑fraction sweep paragraph)
Problem: Ambiguous “template‑fit SNR” vs “angle‑recovery SNR” naming.
Issue:
- Two different notions of significance appear: (i) the matched‑template SNR across bandpowers (driver’s SNRtmpl), and (ii) |β̂|/σβ at the realization level. The text blends them in a few spots.
Required fix:
- Name and define both quantities once (e.g., “SNRtmpl” and “per‑realization angle SNR”), and use consistent symbols and values wherever they appear.

P1B-m7 (Sec. IV, Eq. (1), p.8)
Problem: Parenthetical identity not stated adjacent to the estimator form actually used.
Issue:
- You use the ½ sin 4β form in Eq. (1) but also refer to sin 2β cos 2β elsewhere.
Required fix:
- Add the explicit identity “(½ sin 4β = sin 2β cos 2β)” immediately below Eq. (1) to remove any doubt (even if mentioned elsewhere).

P1B-m8 (Sec. VI, p.15; “H0‑marginalization note” in the spectator‑subset readout)
Problem: Under‑justified “≤3%” shift claim for Ωa under H0 marginalization.
Issue:
- The statement “Marginalizing H0 over the Planck 1σ interval shifts Ωa by ≲ 3% (Ωa ∝ H0−2)” ignores the zosc(H0) dependence in Eq. (9). While likely small, the ≤3% bound is asserted without a quick estimate.
Required fix:
- Either supply a 1–2 line derivation showing the zosc contribution is sub‑percent over the Planck H0 range for the posterior‑supported masses, or soften to “few‑percent level” and note that the quoted bound neglects the weak H0‑dependence of zosc.

NITS

P1B-n3 (Sec. IV, binning paragraph)
Problem: ℓ‑range phrasing could confuse readers about the role of bins beyond the map band limit.
Issue:
- Bins above ℓ = 1024 contain noise‑only CEB,b but zero template weight, so they do not affect the minimizer. This is correct but is easy to miss.
Required fix:
- Add a brief parenthetical: “(these bins contribute a β‑independent constant to the SSR and therefore do not affect the best‑fit angle).”

P1B-n4 (Terminology)
Problem: Occasional “χ^2” typeset without superscript (as “χ 2”) in captions/body.
Required fix:
- Normalize typesetting to χ^2 throughout.

Explanation
The first review already covered the biggest issues (variance‑combination error; m/H0 prior mapping; archival DOIs; mixed Planck releases; estimator‑dependence of the NaMaster bias; anharmonic correction claim; ℓ ≤ 1024 restriction quantification; burn‑in/accounting consolidation; S8 tension reproducibility; and repository path overexposure). The fresh‑eyes pass focused on arithmetic/notation consistency and dimensional terminology within Sec. IV and on consistency of the “natural box” parameter examples in Sec. VI. The new items above address those gaps without duplicating prior findings.