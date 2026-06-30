# P4 INT-M2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/P4_m.pdf` md5=c63ae434 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7047 chars)
**Wall time**: 527.0s

---

Referee report for PRD (methods) — Paper tag P4

Scope of review: statistical methodology and numerical consistency, not novelty or astrophysical interpretation.

Overall assessment: The manuscript presents a large, carefully documented analysis of spiral-galaxy chirality using an explicitly flip-equivariant inference protocol and a clearly declared estimator hierarchy. The authors make strong efforts to segregate null conventions and to anchor all quoted significances to their own null distributions. Most load‑bearing numbers in the abstract and conclusions are traceable and internally consistent. A few items require correction or clarification before the paper meets PRD’s rigor and archival standards.

Findings

ESSENTIAL

P4-E1 (Data availability; p. 22–23, “Data Availability”)
- Problem: The catalog and analysis are currently referenced by mutable resources without an archival DOI. The text states “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted.” The analysis also relies on a Git commit hash (“commit 53b41d12”) and numerous repository-internal artifact paths. PRD requires that the exact version of all data/software used for figures and tables be permanently archived at acceptance.
- Required fix: Before acceptance, (i) mint archival DOIs (Zenodo or equivalent) for the exact dataset(s), the trained model weights, and the analysis artifacts sufficient to reproduce all figures/tables; (ii) freeze the code at the analysis commit and archive it with a DOI; (iii) replace mutable tags (“v2026.04”) and in-repository path pointers in the main text with the corresponding DOIs and a single “Reproducibility package” reference listing checksums for key artifacts. Keep path-level details in a Supplement or Reproducibility Note; the body of the paper should reference stable identifiers.

P4-E2 (Edge-on fraction statistic; Appendix E, p. 22)
- Problem: The statement “65.7% of b/a<0.3 objects receive CW/CCW labels rather than not spiral” is presented as a precise number tied to b/a<0.3, yet the same paragraph says “the axis-ratio cross-match … remains the canonical inclination test.” It is unclear how the 65.7% was computed (sample definition, cross-match source, N, mask, and uncertainty), and it appears inconsistent with the claim that the axis-ratio cross-match is future work.
- Required fix: Either (a) provide the exact derivation: sample size, catalog(s), mask, b/a source, selection, uncertainty, and an artifact pointer/DOI; or (b) remove this percentage and rephrase qualitatively, deferring quantitative statements to the proposed cross-match. As written, it reads as a load-bearing quantitative claim without a reproducible source.

P4-E3 (Unit consistency for amplitudes; multiple places)
- Problem: Amplitude units are occasionally mixed or ambiguously labeled. Example: p. 12 (“Comparison with Previous Work”) “maximum WLS template amplitude … 0.32% (in Ap units…)” — Ap is dimensionless and earlier defined as Ap = 2(fCW − 1/2); stating “% in Ap units” is confusing. Elsewhere, Aref = 1.7% is called “in fCW units (Aref = 0.034 in Ap units)” in Appendix D; this is clear and should be the consistent pattern.
- Required fix: Audit the manuscript for all amplitude mentions and standardize: always specify whether numbers are in Ap or fCW−0.5 units, and when using percent, make explicit that “x% in Ap units” means Ap = x/100. Prefer the explicit mapping (e.g., “Ap = 0.0032 (0.32%; fCW deviation = 0.16%)”). Apply this to Sec. V.A, the abstract, Fig. 7 caption, and Table X text to eliminate ambiguity.

MAJOR

P4-M1 (Presentation of internal artifact paths in main text; throughout, e.g., p. 3, 7–9, 16–21)
- Problem: Numerous in-repo artifact paths (e.g., pipelines/p2_chirality/outputs/…) appear in the body text. While commendable for transparency, these are ephemeral in a journal PDF and distract from the scientific narrative. PRD articles should confine such operational provenance to a dedicated Reproducibility section, Supplement, or data-release note cross-referenced by DOI.
- Required fix: Move the bulk of the path-level “artifact” references from the main body into a Supplementary “Reproducibility and Provenance” document or an archived README associated with the DOI. In the body, retain a short parenthetical like “(all provenance artifacts archived under DOI: …)”. Keep only the minimum pointers necessary to interpret methods/results.

P4-M2 (Sigma juxtaposition caveat consistency; Conclusion §VII.c, p. 16)
- Problem: In §VII.c the two σ values for the canonical mask (+3.64σ from N=500 and +7.93σ from N=10^4 permutations) are juxtaposed without the now-standard reminder that they are diagnostic-only and not comparable to the real-space estimator. Most other juxtapositions in the paper include an explicit “not directly comparable” caveat.
- Required fix: Add an explicit qualifier at the point of juxtaposition in §VII.c mirroring the rigor used elsewhere (e.g., “These values arise from different null-run sizes on the same diagnostic estimator and are not cosmological detection significances nor comparable to the primary real-space estimator.”).

P4-M3 (HuggingFace links formatting; p. 22–23)
- Problem: The catalog URL contains embedded spaces (“galaxy- chirality- catalog”). This can break hyperlinks or confuse readers.
- Required fix: Verify and correct all URLs. Provide clickable, space-free links and DOIs. If line breaks in LaTeX introduced spurious spaces, add \url or \href wrappers to ensure faithful rendering.

MINOR

P4-m1 (Abstract-last drift sweep; p. 1)
- Problem: The abstract contains several parenthetical caveats differentiating null procedures — this is good — but one more explicit mapping of A units would help (see ESSENTIAL P4-E3). Also, “≈1.9σ Gaussian-equivalent” corresponds to p ≈ 0.029 one-sided; please confirm the conversion is one-sided (the body uses one-sided empirical ranks unless noted).
- Required fix: Clarify in abstract that Gaussian equivalences are one-sided unless stated.

P4-m2 (Figure captions: unit labels)
- Problem: Fig. 7 captions refer to fCW with range [0.47, 0.53]; adding an explicit note “equivalently Ap ∈ [−0.06, 0.06]” is present — good. Ensure the colorbar label shows the correct quantity (fCW or Ap) consistently across Figs. 4 and 7 to avoid misinterpretation.
- Required fix: Verify all figure colorbar labels match the field used in the panel.

P4-m3 (Equation typesetting; Eq. 4, p. 13)
- Problem: OCR/LaTeX glitch: “σ(A) = s 3/Nspiral” should read σ(A) = sqrt(3/Nspiral). Also clarify the relation σ(A) = 2√3 σ(fCW) with a one-line derivation in a footnote or parenthesis for readers.
- Required fix: Correct the typesetting and optionally add the short derivation or reference.

P4-m4 (Typos/notation)
- Problem: Minor typesetting artifacts: “C 2 2 ◦” (should be C2 with 2° apodization), repeated carets “ˆ y, ˆ zˆ”, inconsistent spacing around vectors, etc.
- Required fix: Clean up notation and spacing for readability.

P4-m5 (Effect-size pairing)
- Problem: You generally pair σ with amplitudes (good). In §IV.C, after giving z = +0.41 and A = 4.4×10−3, consider also restating A in fCW deviation units for readers who think in number-count asymmetries (i.e., 0.22% in fCW units).
- Required fix: Add one sentence giving the fCW deviation.

P4-m6 (Consistency of area- vs θ-uniform axis draws; p. 14)
- Problem: The body text contains the area-uniform re-run result (“reproduces the tabulated thresholds”) but cites only artifact IDs. A brief numerical summary (e.g., the A50/A95 confirmation values) would improve self-containedness.
- Required fix: Add the explicit area-uniform A50 and A95 numbers to the text (you already have them: A50 = 0.75%; A95 ≈ 1.20% by log interpolation).

NITS

P4-n1 (Over-long prose)
- Comment: At 24 pages the paper is dense but acceptable for PRD given the systematics analysis. Consider moving some of the very detailed NaMaster condition-number diagnostics and path-level provenance notes to Supplement to improve flow without sacrificing rigor.

P4-n2 (Bibliography hygiene)
- Comment: Spot-checks on Shamir (2012/2020/2022), Jia et al. (2023), Dosovitskiy (2021) look correct. Ensure all arXiv IDs and DOIs render as links in the final PDF.

Numerical/consistency audits (selected)

- Catalog composition (p. 5): NCW=1,592,107; NCCW=1,609,053; NNS=5,273,371 sums to 8,474,531. Percentages 18.787% + 18.987% + 62.226% = 100%. Spiral fraction = 3,201,160/8,474,531 = 37.774%. Consistent.

- Table II: For Catalog A, fCW=0.507879 with N=3,321,795 gives σbin = sqrt(f(1−f)/N)=0.000274; deviation (f−0.5)/σ=28.72; matches. For Catalog C, 0.497353 with N=3,201,160 gives σ=0.000279; deviation −9.47; matches.

- Real-space dipole (p. 7–8): Adip = 4.4×10−3; null-quantiles {3.5,4.4,6.0,6.8,8.4}×10−3 and A95,nq=6.8×10−3 (all Ap units) are consistent with zmom = +0.41 and rank p=0.31 (one-sided).

- Harmonic ℓ=1 (p. 9–11): Apodized Wp=Nall C1 = 2.348×10−5, null mean 1.71×10−6, σ=2.99×10−6 ⇒ z = 7.28. The N=10^4 recompute (Table III) gives C1 = 24.74×10−6, null mean 1.93×10−6, σ=3.12×10−6 ⇒ z=7.31; rank p = 6/10001 = 6.0×10−4 (k=5). Consistent.

- Monopole leakage (Table IV, p. 12): Pre-MASTER data C(ℓ=1) = 1.6961×10−2 vs null (1.6846±0.0068)×10−2 ⇒ z=+1.69; hemisphere max asymmetry 3.484×10−3 vs (1.693±0.405)×10−3 ⇒ z=+4.42. Matches.

- Block-bootstrap WLS (Table X, p. 21): Abest_dipole = 4.55×10−3; σboot=1.63×10−3; Aref = 0.034 (Ap) ⇒ z = (0.00455−0.034)/0.00163 = −18.1. Matches.

- Fisher floor (p. 13): σ(A)=sqrt(3/N) = 9.68×10−4 for N=3,201,160; for N=949,584, σ(A)=1.78×10−3; 3σ floors 0.29% and 0.53% full-amplitude respectively; consistent.

- Injection-recovery (Table V, p. 14): P(σ>3)=0.55 at A=0.75% ⇒ A50≈0.75% (axis-averaged). A95 bracketed between 1.0% and 1.5%. The later area-uniform check states A50=0.75% and A95≈1.20%; request adding these numbers explicitly (see P4-m6).

- Confusion matrix (Table IX, p. 19): Three-class accuracy = 141,438/240,919 = 58.7%. Chirality accuracy among GZ1 spirals triaged to CW/CCW only = 81,939/117,205 = 69.9%; κ=0.40 as quoted.

- Abstract/conclusion consistency: All headline numbers in the abstract appear traceable and consistent with the body, and caveats about distinct nulls are present. Ensure unit fixes per P4‑E3.

## Summary recommendation
MINOR REVISIONS

The analysis is careful, most numerical claims are well supported, and the authors are appropriately conservative about the interpretation of different σ values. Before PRD publication, the authors must (i) archive all data/code/model artifacts with DOIs and point the paper to those immutable resources; (ii) clarify or remove the unreferenced “65.7% edge‑on” statistic; and (iii) clean up amplitude unit labeling. Additional minor presentation fixes will improve readability but do not affect the scientific conclusions. With these addressed, the paper meets PRD’s methodological rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS (fresh-eyes audit)

ESSENTIAL
None newly identified as blocking, beyond items already listed in P4-E1–E3. See MAJOR items below that materially improve rigor and reproducibility.

MAJOR

P4-M4 (Primary null choice for the real-space dipole)
- Issue: The “primary” real-space dipole significance uses the pixel-permutation (“isotropic permutation”) null, which destroys the heteroscedastic noise geometry tied to Nspiral(p). The text provides a check with the per-galaxy label-shuffle null (z = 0.58), but the abstract and headline “+0.41σ” emphasize the permutation-null result as primary. Given the clear heteroscedasticity, the label-shuffle null that preserves per-pixel counts is methodologically better matched to the estimator.
- Required fix: Either (a) promote the label-shuffle null to co‑primary (report both in the abstract and main text with equal status), or (b) justify in Methods why the permutation null is preferred despite heteroscedastic noise, including a quantitative comparison of null widths and small-sample behavior. In either case, avoid calling the permutation null “isotropic” without qualification (see P4-m11).

P4-M5 (Harmonic-channel completeness assessed on only three axes)
- Issue: Figure 9 and §VII.a report MASTER ℓ = 1 completeness P(≥3σ) based on injections along only three fixed Cartesian axes {x, y, z}. Describing this as “axis-averaged” can overstate generality; completeness can depend strongly on the dipole orientation relative to the patchy footprint/weights.
- Required fix: Add a random-axis injection battery (e.g., ≥200 random axes per amplitude) and report the axis-averaged P(≥3σ) with uncertainty bands, plus the orientation spread. Archive the injection outputs with a DOI. Keep the {x, y, z} curves as representative but do not use them alone to claim axis-averaged completeness.

P4-M6 (Potential reader confusion from nearly equal 3.63σ vs 3.64σ)
- Issue: The pre-MASTER pseudo-Cℓ ℓ = 1 significance (+3.63σ) and the post-MASTER canonical residual (+3.64σ) are numerically close but refer to different estimators and nulls. Although you note “distinct estimator” in Fig. 8 caption, elsewhere the near-equality can mislead readers.
- Required fix: Add an explicit warning where both appear together (e.g., near Fig. 8 and in §IV.D) that these two ≈3.6σ values are for different estimators/nulls and their numerical similarity is coincidental.

P4-M7 (Flip-equivariance verification/reproducibility of TTA)
- Issue: You claim flip-swap correlation = 1.000 “by construction,” but the archived columns used to reconstruct flipped probabilities lead to out-of-range values for 2.9% of rows (QC notes attribute this to raw vs. equivariant pass mismatch). This undermines external verification of per-object flip consistency from the public release.
- Required fix: Archive, with a DOI, the exact per-object probabilities from both the “original” and the “flipped” passes used to form the TTA averages (or provide a deterministic script that re-runs the exact inference to reproduce them). Add a one-line check in the paper (and a machine-readable artifact) showing per-row equality p_eq, CW(original) = p_eq, CCW(flip) to float precision over all rows.

MINOR

P4-m7 (Training augmentation accounting is unclear)
- Issue: §II.B states “after flip augmentation of the training split the combined pool is 26,616,” but only 826 images were added (26,616 − 25,790), implying partial rather than full flip augmentation of the training set. The prose implies full augmentation.
- Required fix: Clarify exactly how many training images were augmented, why only 826 were added, and provide the precise pre/post split sizes (T0, V0) and augmentation rule. Point to an archived manifest for the training pool.

P4-m8 (RA/Dec slab wording)
- Issue: §IV.B says the RA equal-count partition is “within 0.5%,” but the stated span includes −0.501%. This is pedantic but visible.
- Required fix: Rephrase to “≈0.5%” or provide the exact max deviation value consistently.

P4-m9 (Hemispheric-balance test T6 needs definition)
- Issue: Appendix B (T6) reports “< 0.4%” hemispheric CW difference, but the hemisphere definition (equatorial? Galactic?), mask, and weighting are unspecified.
- Required fix: Specify the hemisphere definition, mask predicate, and weighting used; archive the calculation (script + outputs) under a DOI.

P4-m10 (Monopole-leakage reproduction fraction needs an uncertainty)
- Issue: The headline 99.32% reproduction fraction (Table IV) is reported without an uncertainty on the mean reproduction ratio.
- Required fix: Add the standard error on the mean reproduction fraction (≈0.00018 absolute, i.e., 0.018 percentage points given the quoted per-realization scatter and N = 500), and state clearly whether this is the mean of ratios or ratio of means (you already note they coincide here).

P4-m11 (Naming of the “isotropic (pixel-) permutation” null)
- Issue: Referring to the permutation null as “isotropic” is potentially misleading because it randomizes spatial structure but does not preserve heteroscedastic pixel noise. The paper already distinguishes this from the label-shuffle null.
- Required fix: Rename consistently to “pixel-permutation null” in the main text and abstract; reserve “isotropic” for the conceptual symmetry you intend to probe, with a sentence explaining why permutation is used.

P4-m12 (One- vs two-sided p specification)
- Issue: Some p-values (e.g., hemisphere LEE pLEE ≤ 10−4) are given without explicit one-/two-sided specification. The paper otherwise tries to be consistent about one-sided ranks.
- Required fix: Add explicit “one-sided” or “two-sided” labels wherever p-values are quoted (including the LEE result).

P4-m13 (Clarify “uniform in θ” comment)
- Issue: §VI.B describes θ-uniform axis draws as “mildly” overweighting near-polar axes. The overweighting is appreciable (relative density ∝ 1/sinθ vs isotropic).
- Required fix: Either remove the adverb or replace it with a quantitative comparison; you already include a full area-uniform re-run—quote those numerical A50/A95 values inline (A50 = 0.75%, A95 ≈ 1.20%) as you do elsewhere.

P4-m14 (Potential colorbar/field mismatch reminder)
- Issue: Fig. 4 vs Fig. 7 use different fields (Ap vs fCW). You note the mapping in Fig. 7; ensure the colorbar labels themselves match the fields shown.
- Required fix: Double-check that the colorbar text in the figure files (not just the captions) explicitly states “Ap” for Fig. 4 and “fCW” for Fig. 7; add “Ap = 2(fCW − 0.5)” in at least one caption.

NITS

P4-n3 (Tighten MASTER-vs-pseudo-Cℓ narrative)
- Suggest adding a small table or boxed note contrasting the three low-ℓ estimators used (pre-MASTER pseudo-Cℓ, post-MASTER canonical, post-MASTER apodized/weighted) with their nulls, so readers can keep straight why 3.63σ, 3.64σ, and 7.28σ coexist and are not directly comparable.

NO DUPLICATES
The above items are new; they do not repeat P4-E1–E3, P4-M1–M3, P4-m1–m6, or P4-n1–n2 from the initial report.