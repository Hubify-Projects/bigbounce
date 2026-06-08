# P3 auto-2026-06-08_1520pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 341.3s

---

META-REFEREE REPORT — new issues not caught by the 5 prior reviews

P3-META-E1
- Severity: ESSENTIAL
- Location: §IV.B Spatial Analysis, p. 10
- Why missed: Reviewers focused on the interpretability of χ² but not on the pixel-count arithmetic.
- Problem: The paper states “across 38,330 HEALPix pixels (Nside = 64) … χ² = 143,936, dof = 38,329.” For HEALPix, Nside = 64 implies Npix = 12 × Nside² = 12 × 4096 = 49,152, not 38,330. 38,330 is not equal to 12 × Nside² for any integer Nside, and the dof quoted is therefore inconsistent with the claimed Nside.
- Required fix: Recompute the spatial test with a correctly specified pixelization. If a mask is applied, report Nside, the number of pixels used after masking, and the dof derivation. If Nside ≠ 64 in the actual analysis, correct the text accordingly and revise χ² and dof.

P3-META-E2
- Severity: ESSENTIAL
- Location: Table I, long footnote (∥), p. 7
- Why missed: Others flagged total-count inconsistencies elsewhere but not this specific 200 vs 20,000 mismatch.
- Problem: The footnote claims “excluding ACT subtracts exactly 200 from both the input sum and the unique-object count.” However, “input sum” Ntotal differs by 37,292,042 (cross‑transfer, ACT‑incl.) vs 37,272,042 (Path‑C). That is a 20,000 difference (the number of ACT patches processed), not 200. Subtracting 200 applies to the anomaly count, not the total processed.
- Required fix: Correct the statement to “excluding ACT subtracts 20,000 from Ntotal processed and 200 from Nanom.” Audit all totals in Table I and surrounding text and reconcile any derived numbers that used the incorrect 200 figure.

P3-META-E3
- Severity: ESSENTIAL
- Location: §III C and Table II, pp. 5 and 8
- Why missed: Prior reviews challenged SDSS thresholding but not the internal SDSS×SIMBAD contradiction.
- Problem: §III C states “SIMBAD‑unmatched: 90%” for SDSS anomalies, yet Table II classifies 52.7% of the SDSS anomalies as “Uncategorized,” defined in the caption as “objects that match a SIMBAD entry but lack a specific astrophysical type classification.” If 90% are unmatched, at most 10% can be any SIMBAD‑matched subtype; 52.7% “Uncategorized” is impossible under the stated 90% unmatched rate.
- Required fix: Recompute the SDSS SIMBAD cross‑match fractions, correct either the 90% figure or the Table II class counts/definitions, and ensure a single consistent SDSS×SIMBAD accounting throughout the manuscript.

P3-META-M1
- Severity: MAJOR
- Location: Eq. (2) in §II.B, p. 2 and Table I footnotes (♡, ♠), p. 7
- Why missed: Reviewers noted cross-survey score-scale drift but not the contradiction with the canonical S definition.
- Problem: S is defined as a per‑survey z‑score using that survey’s μval and σval. Yet Table I footnotes explicitly state the SDSS and LAMOST cross‑transfer anomalies “share the DESI‑trained BigAE score scale,” i.e., normalized by DESI’s μval, σval. This contradicts the global definition of S and explains pathologically large SDSS “S” values in cross‑transfer mode. It also invalidates any cross‑transfer S‑threshold (e.g., “S > 5”) as a statistically interpretable z‑cut for those surveys.
- Required fix: Either (i) restrict “S” to truly per‑survey standardized scores and rename the DESI‑scaled values (e.g., S_DESI scale), or (ii) clearly separate native standardized S from cross‑transfer “S” on the DESI scale, and do not interpret cross‑transfer “S” as a z‑score. Update all thresholds and figures accordingly.

P3-META-M2
- Severity: MAJOR
- Location: §III E and Table I footnote (§VI D (f)), pp. 6–8
- Why missed: Others verified the enrichment arithmetic but not the independence assumption behind it.
- Problem: The 95.3× “enrichment over random‑independence” for eROSITA (284/298 of canonical‑S top‑298 also lie in the IF top‑1%) uses a hypergeometric null that assumes independence between detectors. But the IsolationForest is trained on the 16‑dim BigAE latent space; the two detectors are therefore not independent, making the hypergeometric null inapplicable and the “95.3× enrichment” claim inflated.
- Required fix: Replace the independence‑based enrichment with an overlap baseline computed from permutation or resampling that preserves the dependence structure (e.g., label permutation within latent‑space neighborhoods). Report an uncertainty on the overlap and avoid “× enrichment” language unless the null properly reflects dependence.

P3-META-M3
- Severity: MAJOR
- Location: §IV C Deduplication, p. 10; §II D Step 6, p. 4
- Why missed: Prior reviews discussed matching radius and random overlaps but not FoF chain-bridging.
- Problem: The 7‑way dedup uses a single 5″ friends‑of‑friends (FoF) linking radius across heterogeneous surveys. FoF can create chain‑bridged associations where a sequence of offsets <5″ links sources whose end‑to‑end separation exceeds 5″, particularly hazardous when combining surveys of different astrometric precision and epochs. No test is shown for maximum intra‑cluster diameter or for the stability of clusters to shrinking the linking length.
- Required fix: Report the distribution of intra‑cluster maximum pairwise separations; recompute dedup with radii {3″, 5″, 7″} and a “no‑bridging” constraint (all members within R of a common centroid) to demonstrate that unique‑object counts and the 637 multi‑survey clusters are robust. Include Gaia proper‑motion propagation where possible.

P3-META-M4
- Severity: MAJOR
- Location: Table V (Computational details), p. 16; §III F, p. 6
- Why missed: Reviewers checked throughput totals, not the training‑time units per survey.
- Problem: Table V lists “Train time (s)” for the Planck native convolutional autoencoder as 10.6 seconds on 2×10^5 patches with ~1.1M parameters, which contradicts §III F’s training description (native convolutional autoencoder, substantial dataset) and is not realistic. Similar sub‑second to few‑second “training times” are also given for other surveys. These are almost certainly unit errors (minutes or hours, not seconds).
- Required fix: Correct the training‑time units, provide wall‑clock times with hardware details and epoch counts for each native retrain, and reconcile them with the stated training schedules. Update §II C’s wall‑clock accounting accordingly.

P3-META-M5
- Severity: MAJOR
- Location: §IV D Planck × ACT cross‑correlation, p. 10; Appendix F, pp. 18–19
- Why missed: Others objected to using quarantined ACT anomalies but did not note the lack of consistent sky masks.
- Problem: The Planck anomalies are trained and selected with a |b| ≥ 20° mask; ACT anomalies are described as concentrating along the Galactic plane. The Planck×ACT “null” is reported without demonstrating common sky coverage, consistent masks, or flux/beam homogenization. Even absent the ACT quarantine, the analysis is apples‑to‑oranges and cannot support the stated inference.
- Required fix: If retaining any cross‑correlation, restrict to a common mask and quantify the sky‑overlap fraction, use matched beams/noise where applicable, and report a formal null test with Monte Carlo sky rotations. Otherwise, remove the section entirely (as already warranted by the ACT quarantine).

P3-META-m1
- Severity: MINOR
- Location: §III B (“Confirmed High‑z QSO Candidates”), p. 5
- Why missed: One reviewer suggested renaming, but no one checked the internal consistency of the Z‑dominance criterion.
- Problem: The selection requires “Z‑arm dominated anomaly scores, rZ > rB and rZ > rR,” motivated by Gunn–Peterson troughs. However, a strong GP trough suppresses B and R flux relative to Z; depending on how the autoencoder reconstructs continua vs. lines, one expects substantial B/R residuals as well. Without quantifying per‑arm residual SNRs, “Z‑dominance” as a necessary condition is not physically justified.
- Required fix: Provide per‑arm residual metrics (and their uncertainties) for the 12 candidates demonstrating that Z‑dominance is a robust discriminator of z ~ 6 QSOs under the adopted model; otherwise, relax the criterion to a multi‑arm signature and revise the selection accordingly.

P3-META-n1
- Severity: NIT
- Location: Appendix D, p. 15
- Why missed: Reviewers did not scrutinize stability metrics.
- Problem: UMAP “trustworthiness 0.9797 ± 5×10^−5 across 20 independent seeds” is given to five significant decimal places without reporting sample size or neighborhood parameters per seed. This level of precision is implausible and suggests either over‑rounding or a reporting artifact.
- Required fix: Report mean ± standard deviation with realistic precision and provide the exact sample size and UMAP parameters used per seed. If the dispersion is genuinely that small, explain why (e.g., fixed random states, same initialization, or extremely stable manifold structure).

## Meta-review recommendation
REJECT

Given the union of all six reviews, the paper has multiple essential arithmetic and internal‑consistency errors (this meta‑review adds critical new ones: the HEALPix pixel/dof mismatch; the ACT 200 vs 20,000 input‑sum error; and the SDSS×SIMBAD contradiction), plus methodological problems (score‑scale definition drift; dependence‑violating enrichment; dedup bridging without robustness tests; unrealistic training‑time units). Combined with earlier blockers (use of quarantined ACT in a main‑text conclusion; misdefined Fisher constant; SDSS threshold mislabeling; private data; Bayes‑factor misframing; novelty‑rate overclaims), the manuscript would not survive external peer review without a substantial rewrite, full re‑tabulation, and reruns of several analyses. My confidence that the current results are robust is low.