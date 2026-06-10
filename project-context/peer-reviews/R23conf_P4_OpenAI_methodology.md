# P4 R23conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v167.pdf` md5=b236c8d9 pages=17
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8435 chars)
**Wall time**: 380.2s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (17 pp)

Scope of review
I evaluated statistical/methodological rigor, derivations, dimensional consistency, and internal arithmetic consistency across the full 17-page manuscript, including all figures, tables, equations, captions, and the abstract and conclusions. I recomputed quoted σ, p-values, ratios, and percentages where the inputs were given. Findings below are categorized as ESSENTIAL, MAJOR, MINOR, or NIT.

ESSENTIAL ISSUES

P4-E1
- Location: Abstract (p.1), also Conclusions (pp.11–12), Sec. IV C–D (pp.6–8), Table III (p.8), Appendix A.c (p.12)
- Problem: Inconsistent and conflicting ℓ=1 MASTER “canonical-mask” significances are reported: the abstract claims “+3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask,” while Table III lists for the canonical unapodized mask z = +7.93 with rank p = 3×10−4. Appendix A.c states monopole subtraction increases σ to +3.64 (called “the canonical-mask number”). The text also says the earlier +3.64σ value is “superseded as a table entry,” yet the abstract still highlights +3.64σ.
- Required fix: Unify the estimator definitions and one authoritative number set. Either:
  1) Use only the Table III canonical rows everywhere (and update abstract/conclusions to reflect z ≈ +7.9 and rank p = 3×10−4 for that precise field/null), or
  2) Retain the +3.64σ canonical value, but then remove/replace the conflicting Table III canonical-row entries with the matching estimator/null, and revise Appendix A.c accordingly.
  In all cases, explicitly define the field (Ap or fCW−0.5), mask, weight, apodization, monopole treatment, coupling matrix, binning, and null used for each quoted σ, and ensure every quoted canonical-mask σ is numerically consistent across abstract/body/tables.

P4-E2
- Location: Abstract (p.1)
- Problem: Different σ values from different null procedures are juxtaposed without an explicit “not directly comparable” disclaimer in the abstract (e.g., “+3.64σ … canonical mask; +7.28σ, apodized footprint”), contrary to the paper’s own admonition elsewhere.
- Required fix: Add an explicit sentence in the abstract immediately around these numbers stating that σ values arise from different estimators and null procedures and are not directly comparable. Alternatively, remove σ from the abstract for these diagnostic channels and leave the detailed significances in the body.

P4-E3
- Location: Sec. IV C.b (p.6–7), Table III (p.8)
- Problem: In Sec. IV C.b you write “the 10^4-permutation recompute (Table III) confirms this channel at z = +7.31 with empirical rank p = 6.0 × 10−4 (one-sided, 5/10^4 null draws exceed the data).” If 5 out of 10,000 exceed, p = 5×10−4, not 6×10−4.
- Required fix: Correct the numerator or the printed p-value. Report both integers (k/N) and the resulting p with consistent rounding.

P4-E4
- Location: Throughout (e.g., Abstract p.1; Sec. I p.1–2; Sec. IV D p.6–8; Appendix A.d p.12; Appendix D p.14–15)
- Problem: Version-history/internal-audit prose and repository artifact pointers appear in the main text (e.g., “An earlier version of this paper reported… that result is withdrawn,” “artifact c9a/c9b/c9e,” “pipelines/...json,” “manuscript revision v1.0.76,” etc.). PRD articles should not include running audit logs, version identifiers, file paths, or provenance narrative in the main body.
- Required fix: Move all version-history/audit narrative and file-path pointers to a clearly labeled Supplementary Material or a dedicated data-provenance appendix that is referenced briefly in the main text (one sentence). Remove internal labels like “artifact c9e,” repository paths, and version numbers from the main text. Keep only a DOI or permanent link to the dataset/code snapshot.

P4-E5
- Location: Fig. 6 caption (p.8), Sec. VI A (p.10), Appendix E.b (p.15)
- Problem: Ambiguity/inconsistency in the definition of peq and in the counts tied to the indicated vertical lines in Fig. 6. The caption says the plot shows max(PCW, PCCW, PNS) with 73.6% at max p ≥ 0.9, but then states “The high-confidence (HC) cuts at peq > 0.6 (N = 949,584) and peq > 0.8 (N = 624,660) are indicated.” Those N correspond to a spiral-only cut peq ≡ max(Peq_CW, Peq_CCW), not to max over all three classes; on the shown distribution of max over 3 classes one would expect far larger counts above 0.6/0.8.
- Required fix: Define peq explicitly in the caption and in the first place it is used (Sec. III C or IV A): peq ≡ max(Peq_CW, Peq_CCW) for spiral-only cuts. In Fig. 6, either (a) replot the histogram of peq for spirals if you want the vertical lines and N to be meaningful on that figure, or (b) keep the current “max over all classes” histogram but remove the N statements or make crystal clear that the thresholds shown are for a different quantity used elsewhere (and not interpretable from this histogram).

P4-E6
- Location: Appendix A.c (p.12)
- Problem: Statement “Monopole subtraction reduces decoupled C1 from 2.30×10−5 to 1.51×10−5 (∼34%) and increases σ from +1.85 to +3.64 (the canonical-mask number).” This σ progression is incompatible with the canonical z ≈ +7.9 values in Table III and with the abstract’s emphasis on +3.64σ being “post-MASTER.” This contributes to the global inconsistency flagged in P4-E1.
- Required fix: Recompute and/or restate these numbers for the exact estimator defined in Appendix A and ensure they match the canonical entry/entries you choose to retain. If different estimator conventions are being contrasted (single-mode vs full-bin-coupling; different field or weighting), explicitly label them and do not reference “the canonical-mask number” ambiguously.

MAJOR ISSUES

P4-M1
- Location: Table I caption (p.4) vs. body text
- Problem: Row (vi) in Table I lists “+1.68σ” for the generative monopole+mask leakage residual, while Sec. IV D/Table IV quotes +1.69σ (and the math from Table IV values gives 1.69). Minor numeric mismatch within the same manuscript.
- Required fix: Harmonize to a single rounded value across table and text (prefer 1.69σ to match Table IV).

P4-M2
- Location: Abstract (p.1), Sec. IV D (pp.6–8), Appendix D (pp.14–15)
- Problem: The paper uses both “moment-z” and “Gaussian-equivalent” σ (via rank p) for the same diagnostic, sometimes in close proximity. While you occasionally explain the mapping, readers can be confused about which number to use. The abstract’s “+3.64σ moment-z, ≈1.9σ Gaussian-equivalent” is particularly nonstandard without a crisp initial definition.
- Required fix: Early in the Methods (Sec. III A or a “Significance conventions” box), define rigorously:
  - zmom ≡ (value−⟨value⟩null)/σnull,
  - prank ≡ empirical one-sided rank,
  - zGauss ≡ Φ−1(1−prank), with the caveat about positive-definite estimators.
  Then, at every occurrence where both are quoted, format as “zmom = 3.64 (prank = 0.030; zGauss ≈ 1.88).” In the abstract, use only one representation or adopt this triplet form succinctly.

P4-M3
- Location: Sec. III C (p.4–5), Appendix B.d (p.13)
- Problem: Horizontal flip-only TTA is justified heuristically; however, both horizontal and vertical reflections reverse image parity. The paper states “we restrict to 2-fold TTA (original + horizontal flip)” without showing that adding vertical flips does not change catalog-level fCW or key estimators (you discuss D4 rotations more than vertical mirroring).
- Required fix: Add a brief quantitative check (e.g., on 100k random galaxies) showing that adding vertical-flip TTA leaves the catalog-level fCW and the real-space dipole within stated tolerances (|Δ| < 0.001 in fCW and |Δz| < 0.2σ for the dipole), or justify clearly why horizontal-only is sufficient given your pre-processing that standardizes image orientation.

P4-M4
- Location: Sec. VI A.b (p.10), Table V (p.10)
- Problem: Injection–recovery thresholds are reported on the HC-broad subsample (N=949,584) while the primary real-space null is run on the full spiral set (N=3.2M). The translation between the HC floor and the full-catalog floor is not given quantitatively.
- Required fix: Provide a short justification that the HC-derived A50 ≈ 0.75% is a conservative floor for the full catalog (e.g., show on 2–3 injected amplitudes that detection efficiency on the full catalog is within ±0.05 in probability relative to the HC subsample), or provide a small full-catalog injection–recovery spot check.

P4-M5
- Location: Data Availability (p.16)
- Problem: The catalog DOI is not yet minted; only a mutable HuggingFace tag is provided. PRD requires stable access to data/code.
- Required fix: Provide a permanent DOI (e.g., Zenodo) for the exact catalog and code snapshot used in this paper before publication. Update all pointers accordingly.

MINOR ISSUES

P4-m1
- Location: Table III caption (p.8)
- Problem: Units/normalization language: “Ap-map ×10−6 sr scale” can confuse readers (Cl units vs field variance). You mix “dimensionless band values” in Table IV and “×10−6” factors in Table III.
- Required fix: Add one clarifying sentence: specify the precise normalization of Cℓ (HEALPix convention; unitless field; Cl has units of field^2 sr; numbers in the table are Cl × 10^6). Ensure consistency between Table III and Table IV phrasing.

P4-m2
- Location: Sec. III A (p.2–3), Table I (p.4)
- Problem: Although Table I’s caption says σ across rows are not directly comparable, the main text near Table I does not reiterate this, and readers may still be tempted to compare.
- Required fix: Add an inline sentence in Sec. III A explicitly stating again that σ from different rows use different nulls and should not be cross-compared.

P4-m3
- Location: Sec. II B (p.2)
- Problem: “Independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91% (Cohen’s κ = 0.40).” κ requires class marginals; the denominator assumptions are not described.
- Required fix: Add a parenthetical specifying the class set used for κ (spirals labeled CW/CCW only; NS excluded) and whether κ is computed on argmax labels.

P4-m4
- Location: Sec. IV C.a (p.6)
- Problem: You report both z = +0.43 and p = 0.30 for the real-space dipole; some readers may assume Gaussian mapping. You note positive-definite caveat, but not the two-sided equivalence.
- Required fix: Add “(two-sided equivalent ≈ 0.60)” directly after p = 0.30 in this subsection (you already state this elsewhere but be consistent here too).

P4-m5
- Location: Multiple places (e.g., pp.1, 6, 10–12)
- Problem: Informal phrasing such as “headline,” “non-headline,” “load-bearing,” “artifact c9x,” “systematics-attributed,” “Shamir-class,” etc.
- Required fix: Replace with formal language. For example, “diagnostic-only channel,” “not used for cosmological inference,” “repository artifact,” “consistent with systematics,” etc.

P4-m6
- Location: Sec. V A (p.9), Sec. VII (p.11)
- Problem: Claims of inconsistency with prior work at the “amplitude level by a factor of ∼6–12” rely on your pipeline; you already hedge appropriately. To avoid overclaim, ensure no σ-level exclusion is implied.
- Required fix: Add one sentence: “A formal statistical exclusion requires a matched-footprint reanalysis under the Ganalyzer pipeline; we defer this to future work.”

NITS

P4-n1
- Location: Formatting throughout
- Problem: “C 2 2◦” vs “C2 2◦” apodization formatting is inconsistent.
- Required fix: Standardize to “C2 apodization with 2° length.”

P4-n2
- Location: Sec. II A (p.2)
- Problem: “r ≤ 19.0, half-light radius ≥3′′.” Missing space before arcsec in a few places; minor typography.
- Required fix: Insert nonbreaking space before arcsec symbols and standardize to ″.

P4-n3
- Location: Appendix A.c (p.12)
- Problem: “means over the full sky” could be misread; you mean over all pixels at NSIDE=64.
- Required fix: Clarify “means over all HEALPix pixels at NSIDE=64.”

P4-n4
- Location: References [6], [7], [9] (pp.16–17)
- Problem: Ensure journal volumes/pages correspond to final versions (e.g., Walmsley et al. 2023 MNRAS 526, 4768).
- Required fix: Double-check and correct any lingering preprint metadata.

ARITHMETIC/SPOT CHECKS (passed)
- Spiral counts and fractions: NCW + NCCW + NNS = 8,474,531; Nspiral = 3,201,160; fCW = 0.497353; σbinomial ≈ 0.000279; deviation ≈ −9.49σ. Matches text within rounding.
- Asymmetry suppression: |Araw|/|Aeq| ≈ 1.576%/0.529% ≈ 2.98. Matches.
- Fisher floor: σ(A) = √(3/N) with N=3,201,160 gives 9.7×10−4. Matches.
- Table IV reproduction: 1.6846/1.6961 = 0.9932; z = (0.0115)/(0.0068) ≈ 1.69. Matches.
- Sec. IV C.b apodized result: (2.348×10−5 − 1.71×10−6)/2.99×10−6 ≈ 7.28. Matches.

Paper length
At 17 pages, with extensive appendices and repeated audit narration, the manuscript is longer than necessary for the main methodological result (real-space null + leakage channel quantification). After removing version-history prose and moving repository/audit details to Supplementary Material, the main text could be reduced to ~12–13 pages without loss.

## Summary recommendation
MAJOR REVISIONS

The core methodology and most computations are sound, and many numerical claims check out. However, there are critical internal inconsistencies between the canonical-mask MASTER significances reported in the abstract, body, and Table III; an explicit error in a quoted permutation p-value; and pervasive version-history/audit prose that must be removed from the main text for PRD. Clarifying the peq definition and aligning all σ values with their precise estimator/null are essential for methodological clarity. With these corrections and consolidation of the harmonic-channel reporting, the paper can be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass review)

ESSENTIAL ISSUES

P4-E7
- Location: Sec. VI A (p.10) vs. Appendix E.b (p.15)
- Problem: “HC-strict” threshold is inconsistent. Sec. VI A defines HC-strict as peq > 0.9 with N = 471,049, while Appendix E.b defines HC-strict as peq > 0.8 with N = 624,660.
- Required fix: Use one HC-strict definition and count everywhere (preferably peq > 0.9 if that’s the intent), rename the other to “HC-0.8” (or similar), and propagate the corrected labels and N through the text where referenced.

P4-E8
- Location: Fig. 4 caption (p.7) vs. Appendix A/Table VI (p.12)
- Problem: Fig. 4: “The Nall ≥ 1 analysis footprint (fsky = 0.494) is used for the apodized MASTER diagnostic.” Appendix A/Table VI report fsky = 0.488 for the apodized binary footprint, and f_eff,sky = 0.452 for the apodized, weighted Wp = Nall case actually used in the MASTER diagnostic rows. The caption suggests 0.494 applies to the apodized analysis, which is misleading.
- Required fix: Correct Fig. 4 caption to state explicitly: footprint extent fsky ≈ 0.494 (binary, unapodized); apodized effective sky fractions are 0.488 (binary apodized) and 0.452 (weighted, apodized) in the MASTER analysis. Ensure consistency with Table VI.

P4-E9
- Location: Fig. 8 caption (p.9)
- Problem: Mis-citation. The caption says “The post-MASTER canonical-mask residual is +3.64σ (pMC = 0.030; Table IV).” Table IV is the monopole+mask generative-null table and does not contain the +3.64σ or pMC = 0.030 values.
- Required fix: Replace “Table IV” with the correct source for the canonical post-MASTER single-mode result (the text in Sec. IV D/Appendix A.c, or add a canonical-mask row to Table III that matches the stated estimator). Ensure all cross-references to these numbers point to the right table/section.

P4-E10
- Location: Appendix D, Table IX (p.15)
- Problem: Plainly incorrect uncertainty magnitudes for leg-fraction templates: σ ≈ 6.2 × 10^2 (620) for coefficients of order 10^−3 is dimensionally/scale inconsistent. Likely a typo for 6.2 × 10^−3 (or similar).
- Required fix: Correct the σ entries for the BASS+MzLS, DECaLS, and DES leg-fraction templates to the proper order of magnitude and recompute any derived statements if needed.

P4-E11
- Location: Table I caption/row (iv) (p.4) vs. Appendix A/Table VI (p.12)
- Problem: Nmap weighted is defined as Σp Wp for the field used. Row (iv) uses an apodized, weighted MASTER field (Wp = Nall with C2 apodization), but Table I lists Nmap weighted = 8,474,531 (the unapodized sum of Nall). This is inconsistent with the definition and with the f_eff,sky accounting in Table VI.
- Required fix: Report Nmap weighted for the actual weight map used in that row (i.e., after apodization), or explicitly state that Nmap weighted shown is the unapodized tally and provide the apodized effective weight or f_eff,sky alongside. Align the definition and the number.

P4-E12
- Location: Table III caption (p.8) vs. canonical-mask rows
- Problem: Shot-noise statement inconsistency. The caption says the analytic binomial shot-noise floor for “this field” is Nℓ=1 ≈ 2.0×10^−6 and is consistent with null means above; but the canonical, unapodized null mean listed is 0.57×10^−6, which is well below 2.0×10^−6.
- Required fix: Provide footprint/weight-specific shot-noise floors (apodized/weighted vs canonical/binary) or correct the single number. Ensure each row’s null mean is consistent with the stated analytic floor for that exact field.

P4-E13
- Location: Appendix C.c (p.13), Table I caption row (v) (p.4)
- Problem: Double-counting the look-elsewhere effect. You compute a direct-MC distribution of the maximum-hemisphere statistic (which already accounts for the scan) and obtain pLEE ≤ 10^−4, then additionally apply Bonferroni/BH across the 648 tested directions, which is an improper second penalty for the same scan.
- Required fix: Report only the direct-MC p of the maximum statistic (this is the correct look-elsewhere accounting). If you also show per-direction p-values, avoid a second family-wise correction on top of the max-statistic MC unless you clearly separate two different hypotheses/tests.

MAJOR ISSUES

P4-M6
- Location: Sec. IV C.b (p.6–7), Sec. IV D (p.6–8), Table III (p.8)
- Problem: Inconsistent “label-shuffle” null terminology. Some places say per-galaxy label shuffle (Table III), others say per-pixel/permutation shuffles for related canonical/apodized diagnostics. This affects tail behavior (hence rank p) and comparability.
- Required fix: Define precisely the null in each channel (per-galaxy vs per-pixel, with/without depth stratification), and standardize wording. Consider a small study showing the quantitative impact of per-galaxy vs per-pixel shuffles on z and p for ℓ = 1.

P4-M7
- Location: Sec. IV C.a (p.6), Methods hierarchy/Table I (p.4)
- Problem: The real-space dipole is fit with uniform pixel weighting, while other analyses use galaxy-count or depth weights. With strongly varying Nspiral(p), uniform-pixel vs count-weighted regressions can differ.
- Required fix: Justify the choice of uniform-pixel weighting (e.g., show a spot check that the fitted Adip and p-value are stable under count weighting or inverse-variance weighting), or switch to a weighting aligned with the variance model of Ap.

P4-M8
- Location: Sec. IV C.b (p.6–7) vs. Table III (p.8)
- Problem: Two distinct MASTER ℓ = 1 amplitudes are reported for the same apodized footprint: C1 = 2.348×10^−5 (Sec. IV C.b, single-mode decoupling; +7.28σ) vs 24.74×10^−6 (Table III, full 39-band coupling; +7.31σ). Although you note they are “distinct estimators,” readers will ask why the point estimates differ by ~5%. 
- Required fix: Add a one-sentence reconciliation (e.g., finite-bin coupling vs single-ℓ inversion differences) and, ideally, show the two values fall within the expected estimator scatter by quoting their joint covariance or a bootstrap showing ΔC1 is within tolerance.

MINOR ISSUES

P4-m7
- Location: Table II (p.4)
- Problem: Catalog B (calibrated) row lacks Nspiral(B). The quoted ±0.0003 uncertainty and σ rely on N, which is unspecified.
- Required fix: Add Nspiral for Catalog B (and confirm whether calibration alters the spiral count or only the probabilities). Recompute σ if N differs from A/C.

P4-m8
- Location: Sec. IV B (p.5), Fig. 4 (p.7)
- Problem: “Within 0.5% of 50/50 across 7 equatorial slabs” is qualitative only. Given your sub-percent goals, this needs numbers.
- Required fix: Provide the per-slab fCW ± σ (binomial) in a small table or sentence (e.g., range and median with uncertainties) so readers can verify “spatially uniform” quantitatively.

P4-m9
- Location: Table III (p.8)
- Problem: Large discrepancies between zmom and prank across several bands (e.g., z ≈ 4.2 with prank ≈ 9×10^−4) could confuse readers about tail behavior.
- Required fix: Add a short note that the permutation null is heavy-tailed relative to Gaussian at low ℓ (or show a Q–Q plot in Supplementary Material), explaining why zmom and prank-to-zGauss do not match.

P4-m10
- Location: Appendix E.b, footnote 3 (p.15)
- Problem: Cross-reference style: “Sec. D” is used to refer to an appendix section; ambiguous.
- Required fix: Change to “Appendix D” (and check for other “Sec. D” occurrences pointing to appendices).

NITS

P4-n5
- Location: Throughout MASTER sections (e.g., Sec. IV C–D, Appendix A)
- Problem: Minor inconsistencies in referring to the apodized analysis mask/weights (e.g., sometimes “apodized footprint fsky = 0.494” when 0.488/0.452 apply after apodization/weighting).
- Required fix: Standardize phrasing to distinguish geometric footprint fsky (binary, unapodized) from effective sky fraction f_eff,sky after weighting/apodization, and use consistent degree symbol (2°) formatting where apodization length is mentioned.

Explanation
This second-pass focused on arithmetic re-checks, caption/body alignment, equations/units, cross-references, null-procedure comparability, and abstract fidelity. Newly identified issues include a wrong table reference (Fig. 8), inconsistent HC-strict thresholds, an obvious magnitude typo in Table IX uncertainties, inconsistent Nmap_weighted reporting under apodization, a shot-noise vs null-mean mismatch, and a methodological double-penalization of the hemisphere look-elsewhere correction. These were not covered in the first review and should be addressed for PRD-level clarity and rigor.