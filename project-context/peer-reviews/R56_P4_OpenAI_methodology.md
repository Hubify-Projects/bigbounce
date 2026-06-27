# P4 R56 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R56_P4/chirality_catalog_paper.pdf` md5=? pages=?
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5725 chars)
**Wall time**: 297.9s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole …” (23 pp.)

Scope of this review
- Focus: statistical/methodological rigor, internal arithmetic consistency, estimator declarations, null procedures and σ accounting, error propagation, figure/table audit, abstract–body consistency.
- I re-computed all headline numbers that can be derived from values given in the text/tables. I checked that distinct σ’s are not inappropriately compared across null procedures.

Overall assessment
The manuscript presents a very large chirality-labeled catalog (8.47M galaxies; 3.20M spirals) and a carefully bias-hardened analysis leading to a null real-space dipole. The authors are explicit about estimator hierarchy and repeatedly warn that σ’s from distinct null procedures are not directly comparable. The statistical methodology is, for the most part, transparent and numerically self-consistent.

However, there are several issues that must be corrected before this work can meet PRD standards, notably: (i) reproducibility/provenance surfaces (archival DOI/frozen release) are not finalized; (ii) one place where slab-level significance is quoted lacks clarity on which null mean is used; (iii) a few numerical precisions and definitions need tightening (e.g., binomial σ used in Table II Catalog B row, edge-on fraction claim); and (iv) some σ claims in the harmonic channel would benefit from stronger presentation discipline (moment-z vs rank-p separation already present, but the extreme “z~8” with only 10^4 permutations warrants an explicit caution where it appears in Table III). I list detailed findings below.

Findings

ESSENTIAL

P4-E1 (Data Availability/Provenance) — Sec. Data Availability, p. 22–23
Problem: “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted; until it is, the versioned release tag above is the citable artifact.” PRD requires that data/code necessary to reproduce main results be archived at acceptance, with stable identifiers.
Required fix: Mint permanent DOIs for (a) the released catalog (all three tiers), (b) the exact code version used to generate the results (frozen commit), and (c) the “canonical-provenance artifacts” repeatedly cited in-text (JSON/NPY arrays, null distributions, masks). Replace the “will be deposited” wording by actual DOIs. Verify that the SHA/commit hash in the main text matches exactly the frozen archive version.

P4-E2 (Abstract–Body consistency, load-bearing numbers) — Abstract, p. 1
Problem: The abstract is dense with σ’s from different nulls. You do add a general note at the end of the harmonic paragraph: “σ values quoted in this paragraph arise from distinct null procedures … and are not directly comparable.” That is good. However, the first occurrence “+0.41σ (moment-z … isotropic (pixel-)permutation null; … robust under a per-galaxy label-shuffle null, z=0.58 …)” presents two σ’s side-by-side; the immediate sentence does not state “not directly comparable.” You later add a “Note” just after the real-space paragraph clarifying this. For PRD clarity, the “not directly comparable” disclaimer must accompany every juxtaposition.
Required fix: In the abstract’s first dipole sentence, append “(these σ’s arise from distinct nulls and are not directly comparable)” immediately after listing the two σ’s. Similarly, after “+3.64σ …; +7.28σ …” add a parenthetical “(distinct nulls)” even though a general note follows. This keeps the caveat local to each juxtaposition, per PRD standards.

MAJOR

P4-M1 (Slab statistics: ambiguous σ reference point) — Sec. IV.B, p. 5–6
Quoted text: “per-slab fCW spans 0.49537–0.49890, i.e. deviations from 0.5 of −0.110% to −0.463%… The slab-to-slab scatter about the global fCW = 0.49735 is ≲2.7σ per slab…”
Problem: The first statistic is deviation from 0.5; the second (≤2.7σ) is deviation from the global rate. This shift in baseline is not made explicit. A deviation of 0.463% from 0.5 compared to the quoted binomial σ per slab (7.4×10^-4 ≈ 0.074%) would be ~6.3σ, not ≤2.7σ.
Required fix: State explicitly both reference points and give both σ’s: (i) deviations from 0.5 correspond to up to 6.3σ; (ii) deviations from the global 0.49735 correspond to up to 2.7σ. A compact 7-row table (per-slab fCW, Δ from 0.5, z(0.5), Δ from global, z(global)) would remove ambiguity.

P4-M2 (Table II: Catalog B uncertainty and N) — Sec. IV.B/Table II, p. 7
Problem: The Catalog B (calibrated) row quotes 0.50400(27), Dev = +14.6σ, but does not state which Nspiral was used to compute the binomial σ for the calibrated fraction. If N differs between tiers A/B/C, the σ must change. From the table, the parenthetical uncertainty matches ~0.00027, implying N~3.2M, but this is not stated.
Required fix: Add a footnote to Table II specifying the exact Nspiral used for binomial σ in the calibrated row (and, if distinct from A or C, give the integer Nspiral for B).

P4-M3 (Harmonic-channel σ presentation at extreme tails) — Table III, p. 11
Problem: The canonical, unapodized ℓ=1 entry reports z=+7.93 with only 10^4 permutations. You correctly provide rank p (3×10^-4) and note heavy tails, but the presence of “+7.93σ” can be misread as a Gaussian tail probability unsupported by the finite null sample.
Required fix: Add an explicit note in the Table III caption at the canonical block: “The z values are moment-based (mean/std) and do not imply Gaussian tail probabilities; with N=10^4 permutations, the minimum resolvable rank p is ~10^-4.” Alternatively, gray out or parenthesize z for |z|>5 and emphasize rank p.

P4-M4 (Edge-on contamination fraction; quantitative basis) — Appendix E.a, p. 21
Quoted text: “65.7% of b/a < 0.3 objects receive CW/CCW labels… The Neff reduction is estimated at order ∼10–15%, corresponding to a ∼5–8% sensitivity penalty… pending the axis-ratio cross-match…”
Problem: The 65.7% fraction is presented without a clear derivation in the body (no count or sample definition), yet it is used to motivate an Neff penalty (and hence sensitivity). The authors themselves say the axis-ratio cross-match is pending.
Required fix: Provide the actual counts underlying the 65.7% statement (sample selection; number of b/a<0.3 objects; how b/a was obtained). If the cross-match truly is pending, remove the numeric 65.7% and replace with a qualitative statement; do not compute a percentage penalty from an undefined f_edge. Alternatively, provide the cross-match now.

P4-M5 (Injection axis distribution convention) — Sec. VI.A.b and Table V, p. 13–14
Problem: The main completeness curve uses θ-uniform axis draws (not area-uniform), then a spot-check with area-uniform draws is reported to be consistent. For clarity and to avoid any concern about anisotropic weighting of axes in the presence of a patchy footprint, the default should be area-uniform draws.
Required fix: Either (i) re-run the tabulated sweep with area-uniform axis draws and make that the default (moving θ-uniform to an appendix cross-check), or (ii) justify quantitatively that θ-uniform and area-uniform yield indistinguishable completeness on this footprint (beyond the spot check), and promote the area-uniform sweep you already ran (c16_r24conf_pod_batch.json) to the main text/table.

P4-M6 (Abstract phrasing: “disfavors … at z ≈ −18”) — Abstract, p. 1; Appendix D.g, p. 20
Problem: The z≈−18 exclusion is derived under a specific block-bootstrap covariance model (NSIDE=8). While you do note the adopted model in Appendix D and give an NSIDE sweep in a footnote, the abstract should carry a brief qualifier to avoid overstatement.
Required fix: In the abstract, change to: “a block-bootstrap WLS template fit disfavors a clean 1.7% dipole at z ≈ −18 under our NSIDE=8 block-bootstrap covariance (Appendix D; similar at NSIDE=4,16).”

MINOR

P4-m1 (Arithmetic/consistency checks; all OK but please show one tie-out explicitly) — Sec. IV.A/Table II, p. 5–7
Check: For Catalog C, fCW = 0.497353 ± 0.000279 (binomial σ with N=3,201,160): σ = sqrt(0.25/N)=0.000279; z from 0.5 is −0.002647/0.000279=−9.49 (table shows −9.47). For Catalog A, 0.507879 ± 0.000274 gives z=+28.8 (table 28.72). Fine. 
Suggestion: Add one line in the text demonstrating the binomial σ computation and z for Catalog C (to fix the reference σ definitively for readers without a calculator).

P4-m2 (Null-quantile label) — Sec. IV.C.a, p. 7–8
Problem: You define A95,nq as “null-quantile” and explicitly warn it is not a coverage-guaranteed limit. Good. To avoid any confusion with a 95% CL upper limit, please relabel in-text as “A95,null-quantile” everywhere it appears and add “(descriptive only)” once in Sec. IV.C.a.

P4-m3 (MASTER configuration: apodization name formatting) — Appendix A, p. 16
Problem: The text shows “C 2 2 ◦” which reads awkwardly.
Required fix: Typeset consistently as “C2 apodization with 2° scale” (or “C2, 2°”).

P4-m4 (Moment-z vs rank-p consistency note placement) — Figures 7–9 captions, pp. 10, 15
Problem: You include a global caveat “σ values across panels arise from distinct null procedures” in these captions, which is good. Add “z refers to moment-z; rank p is permutation-based” to the first occurrence (Fig. 8 or 9) for reader clarity.

P4-m5 (Training set accounting clarity) — Sec. II.B, p. 3
Problem: The text on augmentation and the 826-image difference could be clearer. The numbers are consistent (25,790 source images; 79.4/20.6 split; augmentation applied to training only → 21,293 train after augmentation; 5,323 val), but the prose is dense.
Required fix: Add a one-sentence arithmetic tie-out: “Train split pre-augmentation = 20,467 images; after horizontal flips → 40,934 images presented over epochs; the unique augmented-pool manifest lists 21,293 training exemplars and 5,323 validation exemplars, totaling 26,616; the 826 difference to the 25,790 source images comes from the train-only augmentation.”

P4-m6 (Table I: Nmap,weighted equals total) — Sec. IV.E/Table I, p. 5
Problem: You list Nmap,weighted = 8,474,531 for apodized Wp=Nall, which equals the catalog total. That is correct. Add a footnote making explicit that each galaxy contributes once to the sum of per-pixel weights, hence equality.

P4-m7 (Harmonic-channel effect sizes) — Sec. IV.C.b/Table III, p. 9–11
Problem: You present C1 data vs null means and σ’s. Good. Add the explicit analytic shot-noise floor value you compute (Nℓ=1 ≈ 2.0×10^-6 for the Wp=Nall field) into the main body (currently only in the caption), with a one-line comparison to C1,meas to anchor effect size.

P4-m8 (Typos/hyphenation artifacts) — throughout
Problem: Several words are broken across lines with hyphenation artifacts (e.g., “di￾rectly”, “sys￾tematics”). 
Required fix: Recompile with proper hyphenation or manually fix the most visible occurrences (abstract and section headers).

P4-m9 (Bibliography: consistency check) — Refs., p. 22–23
Problem: References appear correct; please add explicit page numbers or article IDs for [32] NaMaster/pymaster and [39] timm if required by PRD style (some entries are software with URLs—ensure compliance with PRD style guide).

P4-m10 (Clarity: “largest chirality-labeled catalog”) — Abstract and Sec. I, pp. 1–2
Problem: The claim is correct when “chirality-labeled” includes the not-spiral class (8.47M). To avoid possible misreading that you have 8.47M spiral chiralities, keep the parenthetical “(3.2M spirals)” attached to the first mention in the abstract (it appears now, good). Ensure the same phrasing appears in Sec. I.

NIT

P4-N1 (Overuse of internal artifact paths in body text) — multiple pages
Comment: The numerous in-text path fragments (pipelines/p2_chirality/…json) are useful for your lab book but clutter the prose. Keep them to Data Availability and Appendices; in the main text, refer to “released artifact A1/A2” keyed to a short appendix table.

P4-N2 (Units labeling) — Fig. 7 caption, p. 10
Comment: You correctly remind readers that Fig. 7 panels are in fCW units and relate to Ap by a factor of 2. Consider adding “[fCW ∈ 0.47–0.53] corresponds to Ap ∈ [−0.06,+0.06]” directly on the figure for instant readability.

P4-N3 (Minor consistency) — Sec. IV.C.a, p. 7–8
Comment: When reporting the best-fit real-space dipole amplitude (4.4×10^-3), also state explicitly “=0.44% in Ap units” as you do elsewhere, to maintain effect-size visibility in the primary result paragraph.

Arithmetic and logic spot-checks (no action needed, all consistent)
- Catalog composition: 1,592,107 + 1,609,053 + 5,273,371 = 8,474,531; fractions 18.787%, 18.987%, 62.226% sum to 100% (rounding OK).
- Catalog C monopole deviation: Δf = −0.002647; σ_binom ≈ sqrt(0.25/3,201,160) = 0.000279 ⇒ |z| ≈ 9.5 (matches).
- Catalog A deviation: Δf = +0.007879; σ ≈ 0.000274 ⇒ z ≈ 28.8 (table: 28.72).
- Real-space HC dipole: Aobs = 4.4×10^-3; null 95th percentile A95,nq = 6.8×10^-3; injection floor A50 ≈ 0.75%; numbers hang together.
- MASTER apodized ℓ=1: (2.348×10^-5 − 1.71×10^-6)/2.99×10^-6 = 7.28 (OK).
- WLS bootstrap exclusion: Aref (Ap) = 0.034; Abest = 4.55×10^-3; Δ=−2.945×10^-2; σboot = 1.63×10^-3 ⇒ z ≈ −18.1 (OK).
- Fisher floor σ(A)=sqrt(3/N) with N=3.20116×10^6 ⇒ 9.68×10^-4 (OK).

Length
At 23 pages (including extensive appendices), the paper is on the long side for the core methodological message (null real-space dipole with explicit bias hardening). If trimming is needed, I suggest:
- Move most artifact-path mentions to a compact appendix table (saves ≳1 page of clutter).
- Consolidate repeated harmonic-diagnostic caveats (Sec. IV.C–D) into one prominent box plus pointers (saves ≳1 page).
Target length ≲18–20 pages without losing content.

## Summary recommendation
MAJOR REVISIONS

The core analysis appears statistically sound and internally consistent, and the authors are commendably careful about null procedures and σ comparability. However, PRD requires finalized, frozen reproducibility artifacts (archival DOIs), and several clarity/precision issues must be fixed (slab σ baseline, Table II N for Catalog B, edge-on fraction basis, and an explicit caution on extreme z values with finite permutation nulls). Addressing the essential/major items above should be straightforward and will bring the manuscript to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P4-E3 (Local null-comparability disclaimers still missing in body text) — Sec. VI, p. 12
Problem: The opening sentence juxtaposes “2.31σ real-space dipole” with “+6.48σ pre-MASTER” without an explicit local statement that these σ’s arise from different null procedures/estimators. Earlier you keep such caveats close to juxtapositions; here it’s absent.
Required fix: Append “(distinct estimators/nulls; not directly comparable)” at this first juxtaposition in Sec. VI.

MAJOR

P4-M7 (Rank-deficiency vs finite condition number inconsistency) — Appendix D.g, p. 20
Problem: You state that the 3 leg-fraction templates make X^T W X “exactly rank-8 (condition number 4.5×10^16).” If the design is exactly rank-deficient, the condition number is mathematically infinite; reporting a large finite value conflicts with “exactly.”
Required fix: Clarify this as “numerically rank-deficient” and report both (i) the smallest singular value and (ii) the numerical rank at a stated tolerance (e.g., rcond). If you keep a condition number, say it’s the finite value from a floating-point SVD on the unreduced 9-column design. Keep “exact” only for the linear dependence identity of the centered leg templates.

P4-M8 (C1 numbers after monopole subtraction: footprint/weight ambiguity) — Appendix A.a, p. 16
Problem: “Monopole subtraction reduces decoupled C1 at ℓ=1 from 2.30×10−5 to 1.51×10−5” is not tied to a specific field convention/footprint/weight. In Sec. IV C you quote Cmeas1 = 2.348×10−5 (apodized Nall≥1, Wp=Nall). The 2.30→1.51×10−5 pair likely refers to the canonical unapodized/binary-weight field, but that’s not stated and invites confusion.
Required fix: Specify explicitly: “canonical unapodized mask, binary weight, fCW−0.5 field” (or whichever it is), and ensure these two values are reproduced by the cited artifact. If they are instead for the apodized Wp=Nall case, reconcile the slight mismatch to 2.348×10−5 in the main text.

P4-M9 (Hemisphere LEE p-value phrasing at resolution limit) — Appendix C.c, p. 19
Problem: You report “pLEE ≤ 10−4 (rejection of the random-label null).” With N=10,000 permutations, 10−4 is the resolution floor; the strict statement is “pLEE < 10−4 (resolution-limited).”
Required fix: Change to “pLEE < 10−4 (limited by 10,000 permutations)” and avoid the word “rejection” here; keep the systematic attribution as you already do.

MINOR

P4-m11 (Stray numeric artifact in exclusion sentence) — Appendix D.g, p. 20
Problem: “the primary exclusion statistic is the block-bootstrap z ≈ −18.1.34” includes an extraneous “.34” (likely footnote-marker bleed).
Required fix: Correct to “z ≈ −18.1” and move any footnote markers so they do not attach to the numeral.

P4-m12 (Mislabeling of noise model) — Sec. IV.C.a, p. 7
Problem: “per-galaxy label-shuffle null — which preserves the per-pixel counts Nspiral(p) and their Poisson noise geometry” is imprecise. Given fixed Nspiral(p), the stochasticity is binomial, not Poisson.
Required fix: Replace “Poisson noise geometry” with “binomial noise geometry.”

P4-m13 (Small z inconsistency due to rounding in Table III should be acknowledged) — Table III, p. 11
Observation: Using the rounded canonical-unapodized entries (7.27−0.57)/0.84 ≈ 7.98, while you report z=7.93. This is almost certainly from unrounded internal values.
Suggestion: Add “Computed from full-precision arrays; rounding of displayed numbers may shift back-of-envelope z by ~0.05” to the caption to preempt reader confusion.

P4-m14 (Another local null-comparability hint would help) — Fig. 7 body text tie-in, p. 10–11
Problem: In the body just below the figure you cite “2.31σ real-space dipole + +6.48σ pre-MASTER” (Catalog A) without an immediate local qualifier. The figure caption has a global caveat, but the body sentence would also benefit from it.
Required fix: Append “(distinct estimators/nulls)” to the sentence in Sec. IV.C around Fig. 7.

P4-m15 (Define σiso once and use consistently) — Appendix C.b, p. 19
Observation: You use “σiso” and do define it in parentheses there; ensure the same symbol is not used elsewhere for any different null. A brief one-line pointer “σiso ≡ moment-z vs isotropic pixel-permutation null (Sec. III A)” would improve clarity.

P4-m16 (Numerical tie-out for RA equal-count slab) — Sec. IV.B, p. 6
Observation: You give the RA equal-count range (−0.060% to −0.501%) but no σ context, unlike the declination slabs. Since these are equal-count slabs, σ per slab is the same 7.4×10−4 as before.
Suggestion: Add “corresponding to |z(0.5)| ≤ 6.8 with the same per-slab binomial σ=7.4×10−4; |z| vs global rate ≤ 2.8,” mirroring the declination-slab clarification you will add per P4-M1.

P4-m17 (Shot-noise floor visibility in body) — Sec. IV.C.b, p. 9–11
Observation: The analytic shot-noise floor Nℓ=1 ≈ 2.0×10−6 for the apodized Wp=Nall field is only in the Table III caption.
Required fix: Add one sentence in Sec. IV.C.b: “For this field convention, the analytic binomial shot-noise floor at ℓ=1 is Nℓ=1 ≈ 2.0×10−6, within 4% of the permutation-null mean 1.93×10−6, anchoring effect size.”

P4-m18 (Abstract harmonization of apodized-ℓ=1 σ) — Abstract vs Table III
Observation: The abstract cites “+7.28σ” for the apodized footprint; Table III reports +7.31σ for the 10^4-permutation recompute, while Sec. IV.C.b gives +7.28σ for the 500-MC run.
Required fix: Add “(+7.28σ with N=500; +7.31σ with N=10^4 permutations)” in the body (Sec. IV.C.b) to explicitly reconcile both appearances, or standardize on one and reword the other as a cross-check.

NO CHANGES TO PRIOR FINDINGS
All new items above are in addition to, and do not duplicate, the issues listed in my initial review.