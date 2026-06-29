# P4 RA-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/P4_RA.pdf` md5=96b864b6 pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10522 chars)
**Wall time**: 287.7s

---

Referee report for PRD (methods/statistics): “Survey-Scale Galaxy Chirality with Equivariant TTA …”

Overall scope
The manuscript presents a very large chirality-labeled catalog from DESI Legacy DR8 and performs a hierarchy of statistical tests aimed at a real-space dipole in spiral galaxy chirality. The primary result is a null real-space dipole at sub-percent amplitude, with extensive secondary harmonic- and diagnostic-channel analyses. The paper is methods-heavy, and your stated primacy of the real-space estimator and care to separate null procedures are appropriate for PRD.

Below I audit the methodology, arithmetic, null-procedure hygiene, and reproducibility claims. I list findings with IDs, severity, exact locations, and required fixes.

ESSENTIAL issues (must fix before publication)
P4-E1 — Data availability and archival DOI missing
- Location: Data Availability (page 22–23)
- Text: “A persistent archival DOI (Zenodo deposit of the versioned release) has not yet been minted; until it is, the versioned release tag above is the citable artifact. … An immutable archival snapshot … will be deposited at journal submission; that tagged commit and DOI will be the single citable reproducibility handle for the published version, inserted here in place of this sentence at submission.”
- Problem: PRD requires a stable, citable archive at publication. Version tags on a hosting platform without DOI are not sufficient. The paper also relies throughout on analysis-artifact paths that are not formally archived.
- Required fix: Before acceptance, deposit:
  - The full catalog (Parquet), model weights, and the specific code commit used for the analyses, with a frozen DOI (e.g., Zenodo).
  - All null-distribution arrays and injection-recovery outputs used for the quoted σ/p values (at least for the headline numbers in Abstract/Conclusions) in an accessible archive with DOI.
  - Replace all “will be deposited” language with permanent DOIs and the exact commit hash.

P4-E2 — Internal path “artifact” pointers throughout the body
- Location: Many places across the paper; examples: p. 3–4 (Sec. II B), p. 5 (Table I footnotes), p. 7–9 (Sec. IV C), p. 10–12 (Sec. IV D, Table III/IV captions), Appendix A–E (numerous).
- Text examples: “artifact pipelines/p2_chirality/outputs/canonical_provenance/…”
- Problem: These are internal repository file paths and not stable scholarly references. They clutter the scientific narrative and are not acceptable as primary provenance in the body text.
- Required fix: Move path-level pointers to a Reproducibility Appendix or to the archived repository README. In the body, refer to an archived DOI and a short identifier (e.g., “artifact A1 in DOI:xxx”), and include a concise table mapping each load-bearing scalar (σ, p, amplitude, count) to its archived artifact.

P4-E3 — Abstract-to-body traceability: every abstract scalar must be directly locatable in the body with the same conventions
- Location: Abstract (page 1)
- Items checked and traced:
  - N = 8,474,531 galaxies; Nspiral = 3,201,160 — traced to Sec. IV A and Fig. 3; consistent.
  - Real-space dipole: z = +0.41 (moment-z, permutation null), p = 0.31; amplitude 4.4×10−3 toward (l,b) = (293°, 12°) — traced to Sec. IV C; consistent.
  - Label-shuffle null z = 0.58 and independent reimplementation z = 0.70 — traced to Sec. IV C; consistent.
  - MASTER ℓ = 1 residuals: +3.64σ (500-MC canonical), +7.28σ (apodized) — traced to Sec. IV C–D and Table III; consistent.
  - Monopole+mask leakage: 99.32% of pre-MASTER ℓ = 1 pseudo-Cℓ power — traced to Table IV; consistent.
  - Falsification A95 bracket (1.0%–1.5%) and A50 ≈ 0.75% — traced to Sec. VI B/Table V; consistent.
- Problem: The abstract contains many σ values from distinct null procedures in close proximity. You do add caveats inside the abstract. However, PRD requires that whenever multiple σ appear side-by-side they be explicitly tagged with their null conventions. One sentence (“… +3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask; +7.28σ, apodized footprint”) could be misread without remembering the different nulls.
- Required fix: In the abstract, add parenthetical null labels directly after each σ (e.g., “+3.64σ (label-shuffle null, canonical mask; pMC = 0.030 ≈ 1.9σ Gaussian-equivalent)”; “+7.28σ (label-shuffle null, apodized footprint)”). Keep the “not directly comparable” disclaimer as you already do.

P4-E4 — Ambiguous “largest chirality-labeled catalog” claim
- Location: Abstract p. 1; Sec. I p. 2; Sec. V.B p. 13
- Text: “largest chirality-labeled galaxy catalog to date: 8.47M DESI Legacy DR8 galaxies … 3.2M spirals … 1.6× CE-ResNet’s scale”
- Problem: Only 3.201M objects have chirality labels (CW/CCW). The 8.47M includes non-spiral/edge-on. CE-ResNet’s reported figure (∼1.95M) refers to chirality-labeled spirals. As written, “largest chirality-labeled catalog (8.47M)” is misleading.
- Required fix: Rephrase unambiguously: e.g., “largest chirality-classified survey to date (8.47M total galaxies) with 3.20M chirality-labeled spirals, 1.6× CE-ResNet’s 1.95M spirals.” Provide a citation-backed one-to-one comparison (spirals vs spirals).

P4-E5 — Define once and use consistently the “C2 2° apodization” notation
- Location: Multiple places (e.g., Table I row iv, Sec. IV C p. 9, Appendix A-a p. 16–17, Appendix A-d p. 18)
- Text: “C 2 2 ◦”, “C
2
2
◦” and variants
- Problem: The apodization type/scale appears with inconsistent typography and spacing. Readers should not have to infer that all variants mean the same NaMaster “C2” with 2° scale.
- Required fix: Standardize everywhere to, e.g., “C2 apodization with 2° scale” (NaMaster option ‘C2’, θapo = 2°). Update figures/tables/captions accordingly.

MAJOR issues (significant revisions)
P4-M1 — Independence from CE-ResNet pseudo-labels: add an analysis on a truly human-labeled subset
- Location: Sec. II B (p. 3), Sec. VI A (p. 13–14)
- Text: “66.5% of training labels derive from CE-ResNet predictions … shuffle/permutation nulls do not by themselves test independence … fully independent check is flagged as canonical follow-up.”
- Problem: The primary cosmological estimator is a null, which is conservative against inherited survey-correlated bias, but PRD readers need at least one independence demonstration within this manuscript. You acknowledge the limitation but defer the test.
- Required fix: Add at least one of the following using already-available labels:
  - Compute the real-space dipole and its null on the subset cross-matched to GZ1 human spirals that your pipeline also labels CW/CCW (even with reduced sensitivity), and report the result with its own fsky/mask.
  - Alternatively, train a lightweight sub-model on the 6,637 high-confidence GZ1 labels only (as you suggest), reclassify the full catalog, and recompute the primary real-space dipole. A coarse-grained check is acceptable if computationally constrained, but it must be present in the paper.

P4-M2 — Move core numerical stability diagnostics from artifacts into the paper
- Location: Appendix A-c p. 17; Appendix D-g p. 20–21
- Text: References to condition numbers, apodization insensitivity, block-bootstrap NSIDE choice are made with claims like “insensitive to apodization length (artifact …)” and “block-scale sensitivity check … (artifact …)”.
- Problem: Key stability claims (conditioning of the ℓ=1 row, NSIDE choice for block bootstrap) are hidden behind artifact mentions. PRD requires these justifications to be in-paper.
- Required fix: Include a concise table/paragraph with:
  - Apodization length 1°, 2°, 3°: measured C1, null mean/std, resulting z (for the canonical footprint), showing stability.
  - Block-bootstrap NSIDE ∈ {4, 8, 16}: the inflation factors and z vs Aref. You already computed these; reproduce the numbers in the text or a table.

P4-M3 — Hemisphere look-elsewhere details are artifact-only; summarize in-paper
- Location: Appendix C-c p. 19–20
- Text: “direct-MC look-elsewhere test (N = 10,000) gives pLEE ≤ 10−4 …”
- Problem: This is a useful diagnostic. However, the paper provides no figure/table of the max-statistic null distribution or its summary moments.
- Required fix: Add a small figure or a table summarizing the distribution of the max-statistic across the 10,000 label-shuffles (mean, median, 68%/95% intervals) and the observed value. State explicitly the grid size (648 directions, 10° spacing) in the caption.

P4-M4 — Clarify the “Gaussian-equivalent” usage and ensure mapping is always defined
- Location: Sec. IV D (p. 10–12), Table III caption (p. 11), multiple mentions
- Problem: You sometimes translate empirical rank p to a “Gaussian-equivalent σ” and, elsewhere, use a “moment-z” even when the null is heavy-tailed. This is fine if always stated. In several places you write “+3.64σ (pMC = 0.030; ≈1.9σ Gaussian-equivalent)”, which is clear. But ensure there is no instance where a moment-z is casually compared to a Gaussian σ from rank p without stating the mapping (especially in narrative sentences).
- Required fix: Search-and-correct any remaining instances where a σ is written without its null label and mapping convention. Add a one-line reminder in Sec. III A that all “Gaussian-equivalent” σ refer to N(0,1) inverse-CDF of the one-sided empirical rank unless stated two-sided.

P4-M5 — Page length and presentation
- Observation: The core methodological contribution (catalog + null result) is diluted by extensive inline path references and very long parenthetical caveats.
- Recommendation: Condense the main text to ≤16–18 pages excluding appendices by:
  - Moving internal artifact pointers to a Reproducibility Appendix.
  - Keeping the body’s narrative to method essentials and headline numbers.

MINOR issues (address but do not block publication)
P4-m1 — Consistent units and effect sizes
- Location: Sec. IV C (p. 7–9), Fig. 4–7 captions
- Problem: Sometimes you state Ap amplitudes (e.g., 4.4×10−3) without the percent equivalent; elsewhere you give percent. For readability, always pair Ap with its % equivalent on first mention in a section or caption.
- Required fix: E.g., “Adip = 4.4×10−3 (0.44%)”.

P4-m2 — Confluent typography glitches
- Location: Throughout (PDF hyphenations and accents)
- Examples: “equivari￾ant”, “C
2
2
◦”, “ˆ zˆ”
- Required fix: Repair hyphenation/encoding artifacts before final proof.

P4-m3 — “Superseded” wording
- Location: Appendix D-g (p. 21)
- Text: “naive WLS … superseded by the block-bootstrap values”
- Problem: Non-standard phrasing for PRD.
- Required fix: Rephrase neutrally: “we adopt the block-bootstrap covariance in all inferences; naive-WLS errors are reported for reference only.”

P4-m4 — Bibliographic cross-checks
- Location: References [1]–[7]
- Outcome: Years/journals/arXiv IDs appear correct for the cited headline claims. Ensure DOIs are added where available (e.g., [7] already includes DOI; add for [5] ApJ if available).

NITs (cosmetic)
P4-n1 — Figure usefulness
- Location: Fig. 6 (confidence histogram)
- Comment: Consider adding counts on the plot or a table for the HC cuts you repeatedly use (peq > 0.6 and 0.8).

P4-n2 — Equation (4) clarity
- Location: Sec. VI B-a (p. 13–14)
- Suggested improvement: Spell out the link σ(A)=√(3/N) and the relation to σ(fCW)=√(p(1−p))/√N with p≈1/2 in one sentence to help readers not versed in this mapping.

Internal arithmetic and dimensional checks (selected audits)
- Catalog C fraction and binomial error (Table II): fCW = 1,592,107/3,201,160 = 0.497353; σbin = √(f(1−f)/N)=2.795×10−4; z=(f−0.5)/σ≈−9.49. Matches quoted 0.497353(279), −9.47σ.
- Pre-/post-MASTER ℓ=1 (Sec. IV C–D, Table III): Cmeas1 = 2.348×10−5; ⟨C1⟩null=1.71×10−6; σnull=2.99×10−6 ⇒ z = (2.177×10−5)/2.99×10−6 = 7.28. Table III 10k-run gives 24.74×10−6 vs null 1.93±3.12×10−6 ⇒ z=7.31. Consistent within run-to-run fluctuations.
- Monopole-leakage reproduction (Table IV): Data 1.6961×10−2; null mean 1.6846×10−2; difference 1.15×10−4; null σ 6.8×10−5 ⇒ z=1.69; reproduction fraction 0.9932=99.32%. Correct.
- Block-bootstrap WLS exclusion (Appendix D-g): Abest=4.55×10−3; Aref=0.034; σboot=1.63×10−3 ⇒ z=(0.00455−0.034)/0.00163≈−18.1; consistent.
- Injection floor (Table V): Reported P(σ>3)=0.55 at A=0.75% with Ninj=100 ⇒ SE ≈ √[p(1−p)/100] ≈ 0.05 as stated. Fisher floor σ(A)=√(3/N)=0.00178 for N=949,584 ⇒ 3σ≈0.53%; consistent with their discussion.

Null-procedure hygiene
- I carefully checked multiple juxtapositions of distinct σ. In nearly all cases you explicitly note the null type and state non-comparability (good). Keep this standard in the abstract per P4-E3.

Effect sizes
- You generally report amplitudes with σ. Good. Continue to pair σ with A or Ap where relevant, especially in the Conclusions bullets.

## Summary recommendation
MAJOR REVISIONS

The central statistical analysis is careful, internal arithmetic checks out, and the separation of null conventions is (commendably) explicit. However, the paper is not yet publication-ready for PRD because (i) the reproducibility and archival requirements are not met (no DOI, heavy reliance on in-text internal path pointers), (ii) critical numerical-stability justifications are only available via “artifact” pointers and must be summarized in-paper, and (iii) at least one independence check from CE-ResNet pseudo-labels should be included. Addressing the essential and major items above should make the manuscript suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-pass audit)

ESSENTIAL issues (must fix)
P4-E6 — Mislabeling of “exact values” for class fractions
- Location: Sec. IV A (p. 5–6), paragraph beginning “The final catalog contains 8,474,531…”
- Text: “exact values: CW 18.787%, CCW 18.987%, NS 62.226%”
- Problem: The stated CCW “exact” percentage does not equal the integer ratio. 1,609,053 / 8,474,531 ≈ 18.975% (not 18.987%). You appear to have adjusted the percentages to force an exact 100% sum at two decimals, but then called them “exact values.”
- Required fix: Replace “exact values” with the true exact ratios (to ≥5 significant digits) or clearly label the shown percentages as rounded/adjusted to sum to 100% at the second decimal. Provide the exact fractional values (to, e.g., 6 significant digits) in a footnote or table.

MAJOR issues (significant revisions)
P4-M6 — Primary null for real-space dipole should preserve per-pixel noise geometry, or be co-primary
- Location: Sec. IV C (p. 7–9)
- Text: Primary real-space dipole uses an “isotropic (pixel-)permutation” null; a label-shuffle null is given as a robustness check (z = 0.58).
- Problem: Permuting Ap across pixels breaks the coupling between per-pixel asymmetry noise and the local Nspiral(p), potentially mis-estimating the variance on a highly non-uniform mask. You do provide the label-shuffle result (which preserves per-pixel counts) and it is close, but PRD readers will expect the noise-preserving null to be primary.
- Required fix: Either (i) promote the per-galaxy label-shuffle null to the primary null for the real-space dipole (report both z and rank-p in the abstract), or (ii) explicitly co-elevate both nulls as co-primary in the abstract and conclusions, stating that the two yield z = 0.41 (pixel-permutation) and z = 0.58 (label-shuffle) with corresponding one-sided rank p’s. Justify the choice in Sec. III A.

P4-M7 — “Pre-specified” high-confidence (peq > 0.6) threshold: provide archival evidence
- Location: Sec. III B (p. 3–4), Sec. IV C (p. 7–9), Abstract
- Text: “pre-specified selection threshold — not tuned post-hoc”
- Problem: The paper asserts pre-specification but provides no archived proof. For a threshold that materially affects the result, PRD requires objective evidence (e.g., a dated commit or preregistration).
- Required fix: Archive (with DOI) a short note or commit log showing the threshold was fixed before the presented analyses. Cite its DOI/commit hash where claimed.

MINOR issues (address but do not block publication)
P4-m5 — Figure–body mismatch in observed MASTER ℓ = 1 significance
- Location: Fig. 9 caption and panel; Sec. IV C; Sec. VII(a)
- Problem: The figure panel annotation shows “obs. σ ≈ 7.21” (from the c9b-internal null), while the text consistently cites +7.28σ (500-MC apodized canonical). The caption attempts to reconcile this but leaves a visible discrepancy.
- Required fix: Harmonize the displayed “obs.” value in the figure with the paper-canonical +7.28σ, or annotate both values unambiguously in the panel legend with their distinct nulls. Avoid a mixed-message in the graphic.

P4-m6 — “Lowest bandpower” wording at ℓ = 1
- Location: Fig. 7 caption (p. 10), sentence “… +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower…”
- Problem: ℓ = 1 is a single multipole, not a bandpower bin (unless binned). The current wording is imprecise.
- Required fix: Replace “lowest bandpower” with “lowest multipole (ℓ = 1)”.

P4-m7 — fsky reporting with apodization is inconsistent/confusing
- Location: Table I row (iv), Sec. IV C (p. 9), Appendix A-a (p. 16–17)
- Problem: You report “fsky = 0.494” for the apodized-footprint diagnostic in the body, but Table VII correctly distinguishes geometric fsky from effective sky fraction feffsky under weights/apodization (0.452 for Wp = Nall with C2, 2°). Mixing fsky = 0.494 with an apodized analysis can confuse readers.
- Required fix: When quoting an apodized analysis in the body, report both the geometric fsky and the effective feffsky (with a parenthetical reminder of the difference). Align Table I row (iv) text and Sec. IV C wording to this convention.

P4-m8 — Rounding in Table III yields z that does not reproduce from printed numbers
- Location: Table III (p. 11), canonical unapodized ℓ = 1 row
- Problem: From the rounded entries 7.27, 0.57, 0.84 (×10−6), z computes to ≈ 7.98, not 7.93. This is likely rounding.
- Required fix: Add one more significant figure to Cdata, ⟨C⟩null, and σnull so that z recomputes from the table within ≤0.01, or add a footnote that z is computed from full-precision values in the archived artifact.

P4-m9 — Edge-on contamination statistic lacks provenance
- Location: Appendix E-a (p. 22)
- Text: “65.7% of visually identified edge-on systems (b/a < 0.3) receive CW/CCW labels…”
- Problem: You cite a precise percentage but no sample size, selection protocol, or source (manual selection? how many objects? which subset?). Moreover, b/a < 0.3 implies photometric axis ratios, yet you also state the axis-ratio cross-match is pending.
- Required fix: Provide N, selection method (manual/automatic), and data source for b/a. If this was a small or qualitative spot-check, label it as such (e.g., “N=… subset”), or remove the precise 65.7% and treat it qualitatively.

P4-m10 — Mask-declaration language vs. primary HC analysis could mislead
- Location: Sec. IV C (p. 7), first paragraph after Eq. (3); Table I footnote a
- Problem: You state the Nspiral(p) ≥ 10 “is the single mask definition referenced by every figure and table... unless explicitly noted,” yet the primary HC analysis uses a re-evaluated mask on the HC subset (fsky = 0.4801), not the canonical 0.49005. The footnote clarifies this; the body text could still be read as contradictory.
- Required fix: In Sec. IV C, explicitly flag the HC-mask exception in the same paragraph that declares the “single mask” rule, pointing to the footnote and giving both pixel counts (23,600/49,152) for transparency.

P4-m11 — Abstract/Conclusions completeness claim vs. figure (clarity)
- Location: Sec. VII(a), Fig. 9
- Problem: The conclusions claim “observed harmonic excess is incompatible… by more than an order of magnitude,” which is derived solely within the harmonic channel’s own completeness units. This is correct but easy to misread as a cross-estimator statement despite your caveats.
- Required fix: Add a short clarifying phrase: “This incompatibility is in the MASTER-channel units only; it does not imply an inconsistency with the real-space estimator.”

P4-m12 — Injection axis sampling: summarize area-uniform rerun in-paper
- Location: Sec. VI B-b (p. 14)
- Problem: You note a full area-uniform axis rerun “reproduces the tabulated thresholds” but provide no numbers in the paper proper.
- Required fix: Add a one-line numeric summary (e.g., “area-uniform: P(≥3σ)=0.59 at A=0.75%, A50=0.75%, A95≈1.20%”) and a pointer to the DOI artifact.

P4-m13 — Metadata leakage test T5: request in-paper circular-statistics wording
- Location: Appendix B-d (p. 18–19)
- Problem: You correctly note Pearson r on RA is not appropriate for a circular variable. While you already add a spherical-harmonic regression supplement, this is buried in Appendix text.
- Required fix: In the main text (Methods or Bias tests), add a sentence noting RA is circular and that you therefore rely on the low-ℓ Yℓm regression (give the |z| ≤ 1.25 result for ℓ=1) rather than T5 for directional leakage.

P4-m14 — Provide a numeric amplitude CI for the WLS dipole posterior
- Location: Appendix D-g (p. 20–21); Conclusions (Sec. VII)
- Problem: You quote Abest and σboot and a z vs Aref, but not an explicit 68% CI on Adip or a one-sided 95% upper bound in Ap or percent units.
- Required fix: Report Adip = (4.55 ± 1.63) × 10−3 (68% CL, Ap units), and the corresponding 95% upper bound on a clean cosmological dipole amplitude from the joint-nuisance-marginalized fit.

NITs (cosmetic)
P4-n3 — Units pairing for amplitudes in text
- Location: Sec. IV C (p. 7–9), captions for Figs. 4–7
- Problem: Some Ap amplitudes appear without their percent equivalents on first mention.
- Required fix: Add the percent in parentheses on first mention in each section/caption (e.g., “Adip = 4.4×10−3 (0.44%)”).

P4-n4 — Minor hyphenation/encoding remnants
- Location: Multiple (e.g., “equivari￾ant”, “ˆ zˆ”)
- Required fix: Clean final PDF encoding and hyphenation.

WHAT I CHECKED AND DID NOT FLAG

A. Arithmetic: I recomputed representative items not covered in my first review. Apart from the mislabeled “exact” class percentages (P4-E6) and the expected rounding mismatch in Table III (P4-m8), values (σ, p, amplitudes) audited here are internally consistent with the adjacent numbers and conventions.

B. Figure–caption vs body: The main mismatch is Fig. 9’s observed σ (P4-m5) and the ℓ = 1 “bandpower” wording (P4-m6). Other figures/captions are consistent with the body.

C. Equations: Displayed equations are dimensionless/consistent as written (Eqs. 2–4).

D. Internal cross-references: Spot-checked refs to Table VII, Appendices A–D; content matches the citing claims.

E. Null comparability: You are generally careful. The new P4-M6 requests elevating the noise-preserving label-shuffle null or co-reporting it as primary for the real-space dipole.

F. Abstract faithfulness: Aside from the null-labeling clarity already requested in my initial review (P4-E3), the abstract statements are supported in the body.

G. Novelty claims: The only remaining concern is already in my initial review (P4-E4).

H. Unquantified hedges: The major hedges are quantified; I request adding an explicit CI for Abest (P4-m14).

I. Appendix vs main mismatch: None new beyond fsky/apodization clarity (P4-m7) and the Fig. 9 numeric mismatch (P4-m5).

J. Stale numbers: None detected beyond acknowledged run-to-run differences (500-MC vs 10k permutations), which you already flag in text.

Summary
These additions focus on (i) correcting a mislabeled “exact” percentage, (ii) elevating or co-reporting a noise-preserving null as primary for the real-space dipole, (iii) providing archival evidence for the pre-specified HC cut, and (iv) tightening several presentation/consistency items (figure value, ℓ wording, apodized fsky reporting, rounding precision, provenance of the edge-on statistic, area-uniform injection summary, and a CI for the WLS amplitude). Addressing these, together with the Essential/Major points from my initial report, will materially strengthen rigor and clarity.