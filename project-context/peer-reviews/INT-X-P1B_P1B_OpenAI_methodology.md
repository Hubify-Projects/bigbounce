# P1B INT-X-P1B — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=d013792f pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6666 chars)
**Wall time**: 359.5s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: methodology rigor, internal numerical/logic consistency, estimator validity, dimensional analysis, and statistical interpretation.
- I audited all tables, figures, equations, and every load‑bearing scalar in the abstract/conclusions against the body.

Overall assessment
- The paper is careful in scoping and generally conservative in claims. The ΛCDM+ΔNeff proxy run is appropriately framed as a null-consistency test; the NaMaster exercise is positioned as a methods validation; and the ALP section is a consistency check with clear spectator-status caveats. The w0wa cross-check now avoids inflated sigma-distance text and flags the DES‑Y5×Pantheon+ overlap.
- However, there is a systematic factor-of-10 error in the mapping between the log10(ma/eV) prior and m/H0 that appears in multiple places (Sec. VI, Fig. 4 caption, Appendix C). This must be corrected. In addition, several method descriptions (pixel/pixel-window/beam treatment in the pseudo‑Cℓ pipeline; choice of unweighted vs. inverse‑variance‑weighted fit while reporting a “pipeline bias floor”) need tightening. Archival/data-availability should be moved to persistent DOIs, and several repository-internals should be migrated to a supplement.

Findings
ESSENTIAL (paper cannot be accepted without these fixes)

P1B-E1 (Sec. VI, p. 16; Fig. 4 caption, p. 18; Appendix C, p. 20): Factor-of-10 error in m/H0 mapping
- Offending text (multiple instances):
  - p. 16: “For ALP masses in the scan prior m/H0 ∈ [7 × 10−3, 7 × 10^2]”
  - p. 18 (Fig. 4 caption): “the mass prior corresponds to m/H0 ≈ 7×10−3 to 7×10^2 for H0 = 1.44×10−33 eV”
  - p. 20 (Appendix C): “log10(ma/eV) ∈ [−35, −30] — the mass prior corresponds to m/H0 ≈ 7×10−3 to 7×10^2 for H0 = 1.44×10−33 eV”
- Why this is wrong: With H0 ≈ 1.44×10−33 eV, ma ∈ [10−35, 10−30] eV gives m/H0 = [10−35/1.44×10−33, 10−30/1.44×10−33] ≈ [6.9×10−2, 6.9×10^2]. The lower bound is ≈7×10−2, not 7×10−3.
- Required fix: Correct every instance of “7×10−3” to “7×10−2”; recheck any derived statements that depend on the lower edge (e.g., zosc ranges) and update text accordingly. State the numerical conversion once in the body to avoid future transcription errors.

MAJOR (significant revision required)

P1B-M1 (Sec. IV, pp. 8–11): Pixel window and beam handling in NaMaster pipeline insufficiently specified
- Offending text: “no instrumental beam is applied … the same cancellation argument covers the Nside = 512 HEALPix pixel-window smoothing, which is common to the simulated maps and the spectra entering the template fit — the decoupled spectra are not pixel-window-deconvolved, and no pixel-window mismatch enters the β estimate.”
- Issue: It is not explicitly shown that the template Cℓ used in the χ2 fit carries the same HEALPix pixel window Wℓ as the map-derived decoupled spectra. Without an explicit statement/formula (e.g., Cℓ^tmpl → Wℓ^2 Cℓ^theory) and/or a test showing invariance to including/removing Wℓ in both tracks, the asserted cancellation is ambiguous. Beam/pixel-window treatment can bias EB-based angle fits at the 10^−2 deg level if misapplied.
- Required fix: Explicitly state whether CEE,tmpl includes the Nside=512 pixel window and at what stage; show a robustness test where Wℓ is (i) applied consistently to both map and template, (ii) removed from both, demonstrating unchanged recovered β within the quoted SE. If not already done, provide a simple formula line indicating your evaluation of CEE,tmpl,b (including any Wℓ and binning). If a beam is omitted by construction, state that Cℓ^meas→M^-1 pseudo‑Cℓ decoupling is applied to spectra with Wℓ included on both sides.

P1B-M2 (Sec. IV, pp. 9–11): Estimator choice vs. reported “pipeline bias floor”
- Offending text: The “observed NaMaster pipeline bias floor” of 0.040° is carried forward from the unweighted estimator; inverse‑variance weighting reduces the bias by ≈80% (to −0.006°), but the unweighted figure is retained.
- Issue: Reporting a “pipeline bias floor” that is dominated by a deliberate suboptimal choice (equal-weighting high‑ℓ noise) risks misinterpretation. Since you already ran the weighted fit and showed it removes most of the bias, either (a) report a bracketed range (unweighted vs. inverse-variance) or (b) adopt the inverse-variance-weighted estimate as the canonical bias for methods validation. Anchoring on the worse configuration while calling it a “floor” is misleading in a methods paper.
- Required fix: Reframe the bias claim. Either present both bias numbers side‑by‑side as estimator-dependent and avoid “floor” language, or adopt the IV-weighted estimator as canonical (preferred for a methods paper) and give the residual bias and SE. Clarify that the published analyses you compare to also used unweighted fits (cite exact code) if you keep unweighted as the baseline.

P1B-M3 (Data availability, pp. 17–19): Lack of persistent DOIs and overlong in‑paper repository internals
- Offending text: multiple references to Git commit hashes, CHANGELOG entries, pathnames, and “DOI pending” for HuggingFace datasets.
- Issue: PRD requires durable, citable data/code. “DOI pending” is not adequate; repositories may change, and internal pathnames/commit chatter belongs in a supplement.
- Required fix: Deposit frozen artifacts (chains, NaMaster artifacts, ALP chains) to a service that issues DOIs (e.g., Zenodo) with versioned releases and include the DOIs in the paper. Move long operational audit notes (column-permutation warnings, per‑file paths, reproduction shell scripts) to a supplemental material appendix; keep the main text to a clean, journal‑style Data Availability paragraph with permanent identifiers.

P1B-M4 (Sec. IV, p. 10–11): Purification and apodization claims need statistical support in text
- Offending text: “purify b=True: 0.238° — unchanged … the bias is likewise independent of footprint geometry and purification.”
- Issue: These are important robustness statements but are given without uncertainties here. Provide the recovered mean ± SE to support “unchanged” within uncertainties.
- Required fix: Add the β̂ and SE (500‑MC mean ± SE) for the purification and apodization sweep configurations (they are in an artifact JSON, but values must appear in the text). State explicitly that changes are <1–2 SE.

P1B-M5 (Abstract and Sec. VI, pp. 1 and 13–16): Spectator-status and coupling-tuning statements are clear but need one consolidated quantitative line
- Issue: The narrative on misalignment tuning (θi ~ 0.1) and coupling range (Caγ ≈ 8–10 in the saturated regime; up to ≳50–160 at small displacements) is spread across paragraphs and footnotes.
- Required fix: Add a single consolidated quantitative statement summarizing the two tunings (misalignment and coupling) with numbers, with one pointer to the exact chain(s) from which they are read (e.g., “run c5_continuous, weighted posterior percentiles”). This will help readers assess the model-effort cost at a glance.

MINOR (address, paper can proceed)

P1B-m1 (Sec. IV, p. 9): Equation (1) definition
- Suggestion: Add a one‑line derivation or citation showing E→B gives CEB ≈ ½ sin(4β)(CEE − CBB) and state that CBB is negligible in the template in your baseline, with the robustness result when including CBB. This closes the algebraic loop for readers.

P1B-m2 (Table II, p. 6): “vs ΛCDM” column use
- You carefully label pivot statistics with “overlap‑inflated; not quotable” but the vs‑ΛCDM column header could mislead. Consider renaming the column “Notes relative to ΛCDM (no significance quoted)” to preempt confusion.

P1B-m3 (Sec. III, pp. 3–7): SH0ES anchor nomenclature and year
- You refer to “H0.riess2020Mb” and to Riess et al. (2022) for MB and H0. Please standardize the label/year to match the cited paper (ApJL 2022; arXiv:2112.04510) to avoid confusion.

P1B-m4 (Sec. VI, p. 14): β periodicity remark
- You note β ≡ β + n×90° for E/B; consider explicitly stating that the Gaussian summary likelihood is valid because |β|≪90° over posterior support, and that no wrapping correction is applied. It is already implicit; one sentence suffices.

P1B-m5 (Figures 1–4, captions): Include units explicitly where applicable
- E.g., Fig. 3 axes in degrees are clear; Fig. 1 corner labels appear to have units on H0 and S8 defined in caption; ensure all axes have units or are dimensionless.

P1B-m6 (Appendix A, p. 19): Broken URL spacing
- “https: //huggingface…” has a space; fix to valid URLs.

P1B-m7 (Sec. II, p. 2): “the ∆Neff extension does not reduce the residual ∼ 3.6σ tension...”
- You later quantify precisely in Sec. III; consider adding the explicit 3.6σ calculation or a parenthetical “computed from 67.68±1.06 vs 73.04±1.04”.

NITS (cosmetic)

P1B-n1 (Throughout): Hyphenation/spacing
- E.g., inconsistent spacing around “M−2 Pl‑suppressed2”, “a ∼ 25×”. Clean up minor typography.

P1B-n2 (Acknowledgments, p. 19): AI assistant acknowledgment
- Acceptable, but conform to PRD style if required (some journals request specific wording).

P1B-n3 (Redundancy): Repeated “not a real‑sky bias bound” disclaimers
- Good to be cautious, but you can tighten repeating sentences.

Arithmetic/consistency checks performed
- H0–SH0ES tension: (73.04−67.68)/sqrt(1.06^2+1.04^2) ≈ 3.61σ (matches “∼3.6σ”).
- S8 tension: (0.827−0.776)/sqrt(0.010^2+0.017^2) ≈ 2.59σ (reported 2.6σ).
- MB–h degeneracy constants: −19.253 − 5log10(0.7304)=−18.571; −19.263 − 5log10(0.6768)=−18.415; Δ=0.156 mag ≈ 3.2 σMB (correct).
- Eq. (4): αEM/(4π)=0.007297/12.566=5.81×10^−4; ×(8×1.06)=0.00493 rad=0.283° (≈0.28°, correct).
- Inverse-variance combine Planck (0.30±0.11) and ACT (0.215±0.074): β=0.242±0.061 → 3.94σ (your “3.9σ upper bound” is correct and properly caveated).
- NaMaster MC standard errors: σβ≈0.046° at fsky=0.32 → SE ≈ 0.046/√500 ≈ 0.0021° (matches “±0.002°”).

Stand‑alone reader test
- The paper is largely self‑contained; it clearly states that model preference (Bayes factors) is deferred. It does not require reading the companion to follow the present methods. Good.
- Some repository‑internal content should be moved to a supplement (see P1B‑M3).

Length
- For a methods companion (no new sky measurement), 22 pages is long. With the repository-internals moved to a supplement and some repetition tightened, the main text could reasonably be ~16–18 pages.

## Summary recommendation
MAJOR REVISIONS

The paper is careful and, with its explicit caveats, appropriate for PRD after revision. However, there is a substantive numerical error (factor‑of‑10 in m/H0 conversion) that must be corrected, and several methodological clarifications are required (pixel/beam/pixel‑window treatment and estimator choice for the “bias floor”). Persistent DOIs should replace “DOI pending,” and repository internals should move to supplemental material. Once these are addressed, the paper should be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND-PASS AUDIT (FRESH-EYES)

A. ARITHMETIC CHECKS

P1B-E2 (Table I, S8 “naive two-Gaussian combination” precision claim)
- Issue: You state the full-tension posterior S8 = 0.814 ± 0.008 is “consistent with the naive two-Gaussian combination … = 0.814 ± 0.009; agreement at the 0.01σ level.” The combined-width re‑compute gives σ = 0.00862, so the difference vs 0.008 is ≈0.00062 (about 0.07σ, not 0.01σ, if one normalizes by the Planck+BAO+SN σ=0.010), and the “agreement” refers to the mean, not the width. This is minor, but the “0.01σ level” phrasing is misleading.
- Required fix: Clarify that the agreement refers to the mean; drop the “0.01σ” phrase or restate as “means agree to <0.1σ; widths differ by ~0.0006.”

P1B-E3 (Footnote 4, template-SNR scaling numbers)
- Check: SNR scaling 20.32×sqrt(fsky/0.32) → 33.12 (0.85) and 28.96 (0.65) matches your quoted 32.98 and 28.81 within 0.5%. OK. No change required; keep as is.

B. FIGURE-CAPTION VS BODY-CLAIM

P1B-M6 (Fig. 3 caption vs. body: lack of uncertainties in robustness statements)
- Distinct from your earlier “purification/apodization” SE request: several “unchanged” claims in the robustness battery (apodization sweep; footprint geometry) are presented only as point estimates in the body, while Fig. 3(b) shows SEs for the fsky sweep. The caption and body should both include mean ± SE for each robustness variant to substantiate “unchanged.”
- Required fix: Add β̂ ± SE (mean of 500-MC ± SE) for each robustness line item in-text and, if space permits, into the Fig. 3 caption parentheticals.

C. EQUATION DIMENSIONAL CONSISTENCY

P1B-m8 (Eq. (1) nomenclature: “χ2” without variance weights)
- Issue: Eq. (1) is an unweighted quadratic cost function (no σb−2). Calling it “χ2” suggests a statistical chi-square with proper variance weighting and units, which it is not.
- Required fix: Rename it “cost function” (e.g., L(β)) or add an explicit sentence: “We minimize an unweighted quadratic cost (not a statistical χ2), chosen to match public driver scripts; the inverse-variance-weighted variant is reported in the robustness battery.”

D. INTERNAL CROSS-REFERENCES

P1B-m9 (Mass-parameter notation consistency: m vs ma)
- Issue: The main text alternates between m and ma for the axion mass; Eq. (6–9) and Appendix C use ma, while Sec. VI often uses m. This can confuse readers when mapping to priors (log10 ma/eV).
- Required fix: Standardize to ma throughout equations, text, and figure captions; update “m/H0” to “ma/H0” consistently.

E. NULL PROCEDURE COMPARABILITY

P1B-M7 (Template-fit SNR definition vs. correlated bandpowers)
- Issue: SNRtmpl ≡ [Σb(Cth
EB,b/σb)2]1/2 uses diagonal per-bin scatters from the MC as denominators. After MASTER decoupling, residual inter-bin correlations remain; a true matched-filter SNR would use the full MC covariance. You already caution this SNR is for a pipeline check, but the numeric values (20.32, 25.71, etc.) invite over-interpretation.
- Required fix: Either (a) compute and report SNR with the full 20×20 MC covariance (C−1) to show the diagonal vs. full-covariance difference is negligible for your setup, or (b) explicitly label SNRtmpl as a “diagonal-approximate matched-filter SNR for internal pipeline comparison only,” and remove significance-like language in the caption.

F. ABSTRACT FAITHFULNESS

P1B-M8 (Goodness-of-fit χ2 decomposition under SN double counting)
- Issue: Table II quotes χ2
SN and χ2
total for the DES‑Y5×Pantheon+ product likelihood that knowingly double-counts ~20% shared SNe. The abstract states caveats elsewhere, but the presence of a χ2 breakdown without a direct “not interpretable” label can mislead.
- Required fix: Add a one-line qualifier in Table II caption: “The SN and total χ2 are not interpretable as absolute GOF due to the known DES‑Y5×Pantheon+ overlap (double counting).”

G. UNSUPPORTED NOVELTY CLAIMS

- None new found beyond your already-scoped caveats.

H. UNQUANTIFIED HEDGES

P1B-m10 (ΔP convention for Q/U noise)
- Issue: You state “no √2 factor;” this implicitly assumes ΔP is the per‑Stokes (Q or U) white‑noise level in µK·arcmin, which is standard but not universal.
- Required fix: Add one sentence explicitly stating the ΔP convention (per Q or U) and a citation (e.g., Planck/ACT conventions).

I. APPENDIX VS MAIN-TEXT MISMATCH

P1B-E4 (Minor: pixel-window handling described differently across sections)
- The body asserts cancellation of the Nside=512 pixel window because the same window is used in the template and the decoupled spectra. Appendix A focuses on repository logistics; there’s no explicit confirming formula there.
- Required fix: Add in Sec. IV a one-line explicit formula for the template bandpower entering the fit, e.g., CEE,tmpl,b = B{Wℓ
2 CEE,ΛCDM
ℓ}b with B the binning operator, and state that the same Wℓ is implicitly present in CEB,decoupled
b from the maps. This disambiguates the cancellation claim. (This is complementary to your earlier required robustness test in P1B‑M1.)

J. STALE NUMBERS

P1B-E5 (Fig. 4 caption prior-to-m/H0 mapping — additional stale echo)
- You already correct the factor‑of‑10 lower‑bound error in the body via P1B‑E1. A second echo of the same mapping appears in the Fig. 4 caption (“m/H0 ≈ 7×10−3 to 7×10^2”). Ensure this instance is corrected to 7×10−2 as well and that any downstream statements (e.g., “zosc ≲ 0” coverage) are rechecked.

K. ADDITIONAL METHOD CLARIFICATIONS

P1B-m11 (β-grid step-size quantization)
- Issue: β is scanned on a uniform 0.001° grid for minimization. With SE ~0.002° at fsky=0.32, grid quantization could contribute at the few×10−4° level.
- Required fix: State that halving the step (0.0005°) leaves β̂ unchanged within ≤0.0005° (or provide the measured change from a quick rerun). This closes a common estimator‑granularity question.

P1B-m12 (NaMaster workspace ℓmax choice)
- Issue: You compute coupling up to 3Nside but generate CMB signal to 2Nside. This is standard, but a one-liner clarifying that using 2Nside instead of 3Nside in the workspace leaves β̂ unchanged within SE would aid reproducibility.
- Required fix: Add that invariance check or sentence in the robustness battery.

SUMMARY

- No additional show‑stopper numerical errors beyond P1B‑E1 were found. The new items above mostly tighten nomenclature, comparability, and method transparency (unweighted “χ2,” SNR with diagonal vs. full covariance, explicit pixel‑window formula, and SEs for robustness claims), plus small language/notation clarifications and one stale echo of the m/H0 mapping in a caption.

Recommendation status unchanged: MAJOR REVISIONS, now including these additional items.