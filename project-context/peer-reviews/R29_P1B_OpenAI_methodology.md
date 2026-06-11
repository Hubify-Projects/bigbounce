# P1B R29 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.55.pdf` md5=b776a111 pages=17
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7541 chars)
**Wall time**: 299.2s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
I reviewed the full manuscript, including abstract, main text, all tables and figures, footnotes, appendices, and references, for methodological rigor, statistical validity, internal numerical consistency, dimensional analysis, reproducibility, and the precision of the claims. I recomputed the quoted significances, ratios, and simple derived quantities from the values provided in the paper.

Overall assessment
The paper presents three technical components: (i) a stock-CAMB ΛCDM+ΔNeff proxy MCMC, (ii) a NaMaster pseudo-Cl MC validation, and (iii) a spectator-ALP birefringence consistency check. The manuscript explicitly avoids over-claiming on detection significance and carefully separates pipeline validation from sky measurements. Many numbers check out on recomputation. However, there are several essential issues that must be addressed for PRD standards, notably the double-counting of supernovae in the w0wa analysis used to make “quintom-B” statements, provenance/version inconsistencies in the Data Availability, pervasive internal version-history and artifact-path prose that belongs in a separate data release (not in the body of a PRD paper), and a few methodological gaps (e.g., the estimator choice in the NaMaster validation and lack of a low-ℓ/lensing pairing-robustness test for the Planck likelihood mix). I list detailed findings below.

Findings

ESSENTIAL

P1B-E1
- Location: Sec. III (pp. 4–6), Sec. V (Table II, p. 5), and related text where w0–wa results are used; “Caveats—(e) DES-SN5YR and Pantheon+ supernovae overlap.”
- Problem: The w0wa chain combines DES-SN5YR and Pantheon+ SN datasets via a product likelihood without a joint covariance accounting for their ≈20% shared events. The paper still presents headline departures from ΛCDM at +4.3σ (w0) and −3.6σ (wa) and states “phantom crossing required.” Without correcting for the known catalog overlap (shared SNe with different Malmquist/correction treatments), these significance statements are not methodologically sound. The authors acknowledge this bias but proceed to use the results as an empirical anchor.
- Required fix: Either (i) re-run the w0wa analysis using a rigorous joint-covariance treatment (as per DES Collaboration recommendations) or (ii) remove DES-SN5YR or Pantheon+ from the stack and re-analyze; then revisit all quoted σ-levels and “phantom-crossing” statements. If the w0wa results are kept, add a quantitative sensitivity analysis (how much the tail-significances change under a clean combination) and move any “quintom-B” claims to a clearly qualified statement. As is, the current significance statements must be withdrawn.

P1B-E2
- Location: Data and Code Availability (p. 14) and Appendix A (pp. 14–15).
- Problem: Provenance/Version inconsistency. The paper tag and title page state v1B.0.55. The Data Availability section says: “HuggingFace dataset DOIs … pinned to the v1B.0.54 commit in the repository README,” while the main text asserts the paper corresponds to tag v1B.0.55. This is a provenance mismatch; PRD requires an immutable, uniquely identified release matching the paper version.
- Required fix: Release a frozen archive (e.g., a Zenodo DOI) corresponding exactly to v1B.0.55 with the precise commit hash and update all links in the manuscript to point to that frozen release. Remove references to a different tag (v1B.0.54) or explain why two tags are necessary with explicit mapping. The reader must be able to reproduce the results from a single, immutable release.

P1B-E3
- Location: Throughout main text and appendices (e.g., pp. 3, 4, 6–12, 14–15).
- Problem: Version-history and internal-process prose appears in the paper body, contrary to PRD style. Examples include “an earlier draft quoted… and are corrected here,” explicit file paths and artifact names (e.g., reproducibility/p1_namaster_500mc/results/c9f_negative_beta.json), “committed driver,” “pod run,” “COUNT EXPLANATION.md,” and similar lab-log content. The Instructions to Authors expect the paper to read as a polished scientific article; internal audit trails belong in supplemental material or a data repository.
- Required fix: Remove all version-history language and internal artifact/path references from the main text and confine such details to a properly curated Supplemental Material or data-release README. Replace them with concise methodological descriptions and a single citation to the archived release.

P1B-E4
- Location: Sec. V.A and Table III (p. 10).
- Problem: The Planck likelihood pairing mixes PR4 (NPIPE) high-ℓ CamSpec with Planck 2018 low-ℓ TT/EE and lensing (clik/native). The paper acknowledges no pairing-robustness test and “any pairing-induced bias is unquantified.” For PRD, if PR4 high-ℓ is used, a consistent low-ℓ/lensing pairing or a robustness swap test is required, especially because ΔNeff and H0 posteriors can be sensitive to low-ℓ τ and lensing.
- Required fix: Provide a pairing-robustness test (swap in PR4-consistent low-ℓ and lensing likelihoods, or cite a validated justification from the Planck likelihood documentation), and report any shifts in ΔNeff, H0, S8 within quoted errors. If not feasible, restrict to a single self-consistent Planck release for all Planck blocks used.

P1B-E5
- Location: Fig. 3(b) and Sec. IV (pp. 7–9).
- Problem: Figure 3(b) shows the fsky sweep, but the canonical fsky = 0.32 point lacks per-realization error bars; the text states this σβ was “not recorded” and is measured in a dedicated rerun with β = −0.27°. The figure as printed remains incomplete (missing the error bar for the canonical configuration).
- Required fix: Reproduce the canonical fsky = 0.32 case with the same β = +0.27° injection and include the per-realization σβ and the standard error of the mean in Fig. 3(b). Do not infer symmetry through a different sign-injection rerun only; show the canonical configuration’s uncertainty directly in the figure.

MAJOR

P1B-M1
- Location: Sec. IV (pp. 6–9), “Canonical estimator choice,” robustness battery.
- Problem: The canonical NaMaster estimator is the unweighted χ² template fit, which the authors show induces a ≈12% multiplicative under-recovery (≈0.032° at 0.27°) and a worst-case absolute bias of 0.040°. An inverse-variance-weighted fit reduces ≈80% of this bias. Using a known-biased estimator as “canonical” for a validation study is not ideal, even if you aim to match prior public scripts.
- Required fix: Either adopt the inverse-variance-weighted estimator as the primary validation (with results/figures updated) or present both, highlighting the weighted version as the recommended unbiased estimator. If the unweighted estimator remains in the main text, the rationale must be strengthened and the bias characterized more broadly (e.g., across noise levels, binning, and ℓ-ranges).

P1B-M2
- Location: Sec. IV, “Only this single binning/ℓ-range configuration is exercised; an ℓ-range robustness sweep is not part of the present MC suite.” (p. 7)
- Problem: A single binning and ℓ-range configuration is insufficient to validate pseudo-Cl EB recovery robustness. The authors demonstrate some robustness to apodization and purification, but an ℓ-range/binning sensitivity test is part of standard pseudo-Cl validation.
- Required fix: Add a limited ℓ-range and binning robustness sweep (e.g., re-fit on [30, 512], [30, 768] and with 10/30 bins) and show that the recovered β and bias remain stable within the quoted 0.040° systematic floor.

P1B-M3
- Location: Abstract and Conclusions (pp. 1, 13) “CMB-S4 (σ(Neff) ∼ 0.03) will provide the first precision test.”
- Problem: No citation provided for the σ(Neff) ∼ 0.03 forecast, and “first precision test” is phrased strongly given current Planck+BAO constraints.
- Required fix: Cite an authoritative CMB-S4 forecast reference (e.g., CMB-S4 Science Case) and soften the phrasing to “will significantly improve constraints on Neff (σ ∼ 0.03), enabling a precision test of small ΔNeff.”

P1B-M4
- Location: Data and Code Availability (p. 14)
- Problem: The paper admits a “unit warning”: a committed diagnostic file stores Cobaya-normalized units with a separate “CORRECTED” companion. As written, a reader could easily use the wrong file.
- Required fix: Replace the problematic file in the archived release with a single, clearly labeled, physically unit-consistent version; update the manuscript to reflect there is no unit ambiguity in the released diagnostics.

P1B-M5
- Location: Fig. 2(a) (p. 7)
- Problem: The legend label “SM ( Neff = 0)” is inconsistent with the plotted variable, which is ΔNeff. Standard Model corresponds to ΔNeff = 0, not Neff = 0.
- Required fix: Relabel the legend to “SM (ΔNeff = 0).”

MINOR

P1B-n1
- Location: Sec. III, one-sided upper limits for ΔNeff (p. 3).
- Problem: Method for the one-sided 95% upper limit is described qualitatively; the values 0.31 and 0.39 check out on recomputation, but a short explicit definition would aid clarity.
- Required fix: Add a one-sentence formula: “We compute the 95% upper limit as the 95th percentile of the posterior truncated to ΔNeff ≥ 0.”

P1B-n2
- Location: Sec. III, “Sample-count stratification (reconciliation)” footnote (p. 3).
- Problem: The burn-in discussion mixes 20% and 30% cuts and “conservative” choices. While transparent, it is confusing.
- Required fix: Standardize the burn-in convention across the paper to a single value (e.g., 30%) and report consistent post–burn-in counts in all places, relegating reconciliation details to supplemental material.

P1B-n3
- Location: Sec. VI, Eq. (3) (p. 11)
- Problem: The normalization choice for β = (gaγ/2) Δϕ is called “convention-dependent.” While correct, readers benefit from a quick pointer to the adopted Lagrangian.
- Required fix: Keep the equation but cite a standard reference for the convention used (e.g., axion-electrodynamics review) in addition to your internal documentation.

P1B-n4
- Location: Appendix A (pp. 14–15)
- Problem: The repository description includes modules not used in this paper. This is fine, but the current phrasing may suggest readers need to navigate unrelated code.
- Required fix: Explicitly state that a minimal set of scripts sufficient to reproduce this paper’s results is provided in a clearly labeled subdirectory.

NIT

P1B-N1
- Location: Title page (p. 1): “(Dated: June 10, 2026 PDT — v1B.0.55)”
- Problem: Internal version stamp in the title block is not typical PRD style.
- Required fix: Remove the version tag from the title block in the final accepted version (it can remain in the arXiv metadata and repository).

P1B-N2
- Location: Stylistic throughout
- Problem: Frequent hyphenation “chain-only,” “pod run,” and colloquial terms (“anchor,” “floor”) appear in technical contexts.
- Required fix: Consider replacing colloquialisms with standard terminology for clarity and style.

Numerical/consistency checks (spot audit)

- H0 tension: |73.04 − 67.68| / sqrt(1.06² + 1.04²) = 5.36 / 1.485 = 3.61σ (matches “3.6σ”).
- S8 Planck+BAO+SN vs DES-Y3: Δ = 0.827 − 0.776 = 0.051; σcomb = sqrt(0.010² + 0.017²) = 0.0197; Δ/σ=2.59σ (reported 2.6σ).
- Full-tension S8 vs DES-Y3: Δ = 0.814 − 0.776 = 0.038; σcomb = sqrt(0.008² + 0.017²) = 0.0188; Δ/σ = 2.02σ (reported 2.0σ).
- One-sided ΔNeff UL (full-tension): 0.318 (Gaussian/truncated) ~ 0.31 (reported).
- w0: (-0.8122 – (−1))/0.0436 = 4.31σ (reported +4.3σ).
- wa: 0.6666/0.1864 = 3.57σ (reported −3.6σ).
- wpivot: (−0.952 – (−1))/0.019 = 2.5σ (reported +2.5σ).
- Phantom crossing: (−1 − w0)/wa = 0.2818 → z× = 1/0.718 − 1 = 0.392 (reported z× ≈ 0.39).
- ALP rotation: β = (α/4π) Caγ (Δϕ/fa) with α ≈ 1/137.036; α/(4π) ≈ 5.81×10−4; for Caγ=8, Δϕ/fa=1.06 → β ≈ 4.93×10−3 rad = 0.282° (reported 0.28°).
- Caγ(Δϕ/fa) for βobs = 0.342°: 0.342° × π/180 = 5.97×10−3 rad; divide by 5.81×10−4 ≈ 10.3 (as reported).
- LiteBIRD forecast: 0.27°/0.03° = 9σ (as reported, with appropriate caveat).

Abstract-last drift sweep
- ΔNeff and H0 values match Table I.
- Pipeline recovery bias values (−0.032°, −0.040°) match Sec. IV and Fig. 3.
- Explicit caveat that the NaMaster validation is not a sky detection is consistent in body.
- Spectator-ALP consistency statement (fa ∼ MPl, m ∼ H0, β consistent with 0.342° ± 0.094°) is supported in Sec. VI; the misalignment fine-tuning caveat is mentioned in abstract and elaborated in body.
- No abstract overclaims found; however, the w0wa-driven “quintom” statements in the body (Table II and surrounding text) should not be used as an empirical anchor until P1B-E1 is resolved.

Bibliography
- Spot-checked key references. [3] PRL 128, 091302 (2022) is appropriate for Planck PR4 birefringence. [5] PRD 106 (2022) matches the 0.342° ± 0.094° figure. [4] is listed as a 2025 arXiv preprint (future-dated but acceptable as preprint). Please add a citation for the CMB-S4 Neff sensitivity claim (P1B-M3).

Length and focus
- At 17 pages, the paper is acceptable for a methodology companion if the essential issues are corrected. However, much of the internal artifact-path prose should be moved to Supplemental Material, which will effectively reduce the main-text density.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains solid numerical work and careful caveating in several places; many headline numbers check out. However, there are essential methodological and provenance issues that must be addressed for PRD: (i) correct the SN double-counting in the w0wa analysis (or remove the resultant significance claims), (ii) fix the version/DOI mismatch and remove internal version-history prose from the main text, (iii) add a Planck likelihood-pairing robustness check or use a fully consistent pairing, and (iv) complete the NaMaster figure with the canonical fsky error bars and reconsider the estimator choice or give the inverse-variance-weighted estimator pride of place. With these corrections and a few minor edits, the paper could be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (second-pass audit)

ESSENTIAL

P1B-E6
- Location: Table I caption and surrounding text (p. 4) where “tension” vs DES-Y3 is discussed for both Planck+BAO+SN and “full-tension” stacks.
- Problem: The paper labels the full-tension posterior (which includes the DES-Y3 S8 Gaussian prior 0.776 ± 0.017 as an active likelihood) as “2.0σ from DES-Y3.” This is not a meaningful “tension” because the DES-Y3 prior is already included in that posterior; the quoted offset is influenced by double-counting the same information.
- Required fix: Do not describe the full-tension posterior as being “in tension” with the DES-Y3 prior. Either remove that statement or rephrase as a descriptive offset only, with a clear caveat that DES-Y3 is part of the posterior. If a tension metric is desired, report it only for posteriors that exclude the DES-Y3 prior.

P1B-E7
- Location: Sec. IV, “Pipeline configuration” and “Noise model and injections” (pp. 6–8); robustness battery (p. 9).
- Problem: Ambiguity in whether the template CEE entering the fit carries the same pixel window (and any beam) as the decoupled spectra. The text asserts cancellation (“the same spectra,” “not pixel-window-deconvolved”), but never states explicitly if the β-fit template uses bandpowers that include the same Wℓ (and any beam) as the measured EB bandpowers. If the template lacks the identical filtering, a multiplicative mismatch can bias β beyond the quoted estimator-weighting and CBB-shape effects.
- Required fix: State explicitly whether the template CEEb are the measured, decoupled, non-deconvolved bandpowers from the same maps (including Wℓ and mask-coupling) or a theory spectrum forward-filtered by the identical Wℓ and binning. If not identical, re-run including the exact same filtering in the template and report the change in β and bias.

MAJOR

P1B-M6
- Location: Table III (p. 10) and Sec. V.A.
- Problem: Inconsistent Planck lensing likelihood between chains: ΔNeff chains use planck_2018_lensing.clik, while the w0wa “iter2” chain uses planck_2018_lensing.native. This breaks strict comparability across chains (and with statements in the main paper) because small but non-negligible shifts can occur between the two lensing implementations.
- Required fix: Homogenize the lensing block across chains and/or provide a lensing-implementation robustness test (clik vs native) quantifying shifts in H0, S8, w0, wa, and ΔNeff. Report that the differences are within quoted uncertainties, or switch to a single implementation.

P1B-M7
- Location: Sec. III (pp. 2–5), ΛCDM+ΔNeff proxy setup.
- Problem: Neutrino mass is fixed to Σmν = 0.06 eV (one massive eigenstate). ΔNeff constraints can be degenerate with Σmν in Planck+BAO+SN analyses; fixing Σmν can artificially tighten or shift ΔNeff and H0 posteriors.
- Required fix: Provide a robustness run allowing Σmν to vary (e.g., minimal normal-hierarchy prior or flat prior above 0.06 eV) and quantify the impact on ΔNeff, H0, and S8. If computationally infeasible, justify with citations that the chosen datasets render this degeneracy negligible at current precision.

P1B-M8
- Location: Sec. IV, Eq./text for the β-fit template and robustness battery (pp. 7–9).
- Problem: Treatment of bins above the map band limit. The fit includes bins to ℓ = 1536 while signal is band-limited at ℓmax = 1024. The text asserts “noise-only bins above the band limit carry zero template weight,” but the estimator is described as an unweighted χ2 fit. Those bins do contribute unless the template CEEb is explicitly zeroed there.
- Required fix: Clarify whether the CEE template is set to zero for bins above ℓmax or the fit range is truncated in practice. Otherwise, re-fit with ℓmax = 1024 (or zero the template above ℓmax) and report any change in β and bias.

P1B-M9
- Location: Sec. IV, “Noise model and injections” (p. 7).
- Problem: Polarization-noise convention. The conversion σpix = ΔP/√Ωpix is implemented “with no √2 factor for Q and U.” In the literature, ΔP is sometimes quoted per Stokes (Q or U) and sometimes per polarization pair P, leading to a possible √2 difference.
- Required fix: Specify the ΔP convention (per Q/U map or per combined polarization) and cite a standard reference. If the convention used is different from that assumed in ACT-like levels, show that a √2 factor swap does not change the recovered β bias within the quoted 0.040° floor.

P1B-M10
- Location: Table I caption (p. 4) — “posterior-overlap integral ∫min(p1, p2) dS8 = 0.05 (0.12).”
- Problem: The overlap statistic is reported without a formal definition or method (kernel choice, binning, numerical integration settings). This limits reproducibility and interpretability.
- Required fix: Provide the precise definition and computation details for the overlap integral in the main text or Supplemental Material, including any smoothing and sampling procedures.

MINOR

P1B-n5
- Location: Fig. 2(b) (p. 7), panel labeling.
- Problem: Axis label appears garbled (“(x xfull_tension) / full_tension”) and does not clearly indicate the plotted normalization, likely from a plotting-template artifact.
- Required fix: Replace with a clear label such as “(x − μfull-tension)/σfull-tension” for each parameter, or equivalent.

P1B-n6
- Location: Sec. IV, “Mask” (p. 7).
- Problem: The mask is defined by a Galactic |b| cut and an equatorial declination cut. The coordinate-system sequence (frame of construction) is not specified; applying both cuts in different frames can create edge-systematics.
- Required fix: State explicitly the coordinate frame used to build the mask and the order of operations (e.g., apply |b| cut in Galactic coordinates, then transform to equatorial and apply declination cut), and confirm that this choice does not bias β (e.g., via the existing robustness battery).

P1B-n7
- Location: Sec. III, one-sided ΔNeff upper limits (p. 3).
- Problem: Truncated-posterior one-sided 95% ULs are reported without a precise definition of the truncation procedure (conditioning vs renormalization).
- Required fix: Add a precise definition: “We renormalize the posterior on ΔNeff ≥ 0 and quote the 95th percentile of the renormalized CDF.”

NIT

P1B-N3
- Location: Throughout (e.g., Sec. V; Table II footnotes a/b).
- Problem: Footnote markers “a,” “b” are reused in multiple contexts, which can confuse readers tracking references and caveats.
- Required fix: Ensure unique footnote markers per context or convert to numbered footnotes; verify that each marker points unambiguously to a single note.

P1B-N4
- Location: Sec. IV and Appendices.
- Problem: Code-path snippets (np.linspace, directory names) appear in the prose of the main text beyond what PRD typically allows.
- Required fix: Move code-path specifics to Supplemental Material or a data-release README and keep only a concise methodological description in the main text.

Explanation for focus of new findings
The second pass emphasized arithmetic cross-checks, figure/body consistency, dimensional and procedural clarity, and comparability of quoted significances. Most arithmetic in the manuscript is internally consistent; no new numerical contradictions were found. The added items mainly concern methodological clarity and comparability (mask/coordinate construction, pixel-window handling, bins above the band limit, neutrino-mass prior robustness, and the mischaracterization of “tension” when a prior is part of the posterior). These were not captured in the initial review and are important for PRD-level rigor.