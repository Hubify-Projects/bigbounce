# P4 R57 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R57_P4/chirality_catalog_paper.pdf` md5=5ddefa62 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6714 chars)
**Wall time**: 367.5s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review: methodological rigor, statistical validity, internal arithmetic consistency, null procedures, estimator declarations, effect-size clarity, and reproducibility surfaces. I audited all quoted scalars in the abstract and conclusions against the body, recomputed accessible ratios, checked dimensional consistency, and inspected figures/tables and their captions.

Overall: The manuscript makes a careful attempt to separate primary and diagnostic estimators and carries many explicit caveats about non-comparable σ’s. The real-space primary estimator is clearly declared and the main null result is supported. However, there are several issues that must be fixed before PRD publication, including a critical inconsistency in the MASTER ℓ = 1 canonical-mask significance, broken/unstable data-release links, a contradictory use of b/a-based “edge-on” metrics, and several places where disparate σ values are juxtaposed without a local “not directly comparable” disclaimer. Excessive within-text repository path references should be moved to a Supplementary/Zenodo record with stable DOIs.

Findings

ESSENTIAL

- P4-E1 (Abstract/Page 1, Conclusions/Pages 14–16, Table III p.11, Sec. IV.D p.12–15): Inconsistent canonical-mask MASTER ℓ=1 significance
  • Problem: The paper reports two very different post-MASTER canonical-mask ℓ=1 significances:
    – “+3.64σ (500-MC direct run on the canonical unapodized mask)” (Abstract p.1; Sec. IV.D p.12; Conclusions p.15)
    – “+7.93σ (10^4-permutation canonical unapodized row in Table III)” (Table III p.11; also cited p.12)
    Both are explicitly labeled as canonical, post-MASTER, label-shuffle nulls. A factor ~2 change in z for the same footprint/estimator cannot be attributed to increasing NMC from 500 to 10^4, nor to a constant rescaling of the field (Ap vs Ap/2), since z and rank-p are invariant under constant rescaling when the null is transformed consistently (your caption asserts this). The caption mentions “different field conventions,” but both rows are canonical unapodized; the 500-MC value is said to be “retained for continuity,” yet it is not methodologically reconciled.
  • Required fix: Provide a single, unambiguous, reproducible canonical-mask post-MASTER ℓ=1 estimate with one declared field convention, weight, monopole treatment, and a sufficiently large null (≥10^4 permutations). Remove or reconcile the +3.64σ and +7.93σ discrepancy by:
    – Explicitly listing, side-by-side, the precise inputs that differ (field definition, monopole subtraction method, mask weights, binning matrix, and null construction) and demonstrating on the same data how each change modifies C1, ⟨C1⟩null, and σnull.
    – Adopt one canonical configuration for the paper and demote the other to a Supplement with a clear explanation of why it differs.
    – If heavy tails in the null are responsible, show the empirical null histograms and quantiles (500 vs 10^4) and quantify the expected sampling variability of z, demonstrating that a shift from 3.6σ to 7.9σ is statistically plausible under the declared changes. Otherwise, correct the inconsistent value.

- P4-E2 (Data Availability/Page 22): Broken/unstable repository links and lack of frozen DOIs
  • Problem: The Catalog link includes line-break spaces and hyphenation that render it unusable in its present form: “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog.” You also state “A persistent archival DOI (Zenodo) has not yet been minted.” PRD requires stable, citable, non-ephemeral links for data/code central to the paper’s claims. Several key statements (e.g., null arrays, injection-recovery, block bootstrap, etc.) rely on “artifact” paths that have no stable DOI.
  • Required fix: Provide functional, copyable URLs and persistent DOIs for:
    – The catalog release (freeze a specific version; give exact tag and DOI).
    – The model checkpoints and training/inference scripts.
    – The complete set of analysis artifacts used to produce every scalar in the paper (null arrays, injection-recovery outputs, WLS design matrices, masks), with a single, citable Zenodo DOI (or equivalent) and a manifest.
    – Remove line-break spaces/hyphenations in URLs throughout or provide a machine-readable link block.
    – Ensure the pinned Git commit corresponds exactly to the released artifacts (and remove language allowing “same-day” drift).

- P4-E3 (Appendix E, Page 21): Contradictory use of b/a (“edge-on”) without a documented cross-match
  • Problem: You state “65.7% of b/a<0.3 objects receive CW/CCW labels,” yet in the same subsection you say “the axis-ratio cross-match that will supply the b/a<0.3 catalog fraction is deferred.” Reporting 65.7% conditioned on b/a<0.3 implies you have already computed b/a for at least a subset. The provenance, sample size, and methodology of this estimate are unclear, and it reads as internally contradictory.
  • Required fix: Either (a) provide the exact cross-match procedure, sample size, and a table backing the 65.7% figure (including how b/a was obtained, selection criteria, and uncertainties) with a stable DOI to the underlying list, or (b) remove this quantitative claim and rephrase as a hypothesis to be tested in future work. If kept, state whether 65.7% applies to the full HC sample, a subset, or a visually selected subset.

- P4-E4 (Multiple locations, e.g., Sec. VI p.12; Sec. IV.C p.8; Fig. 7 caption okay but text not): Juxtaposition of σ values from different null procedures without a contemporaneous “not directly comparable” disclaimer
  • Problem: In several places, disparate σ’s are given side-by-side without the explicit local qualifier you use elsewhere (e.g., Sec. VI: “2.31σ real-space dipole and a +6.48σ pre-MASTER pseudo-Cℓ” with no “not directly comparable” clause in that sentence). The instructions for clarity are followed in most places but not all.
  • Required fix: At every juxtaposition of two or more σ values from different nulls/estimators (e.g., real-space vs pre-MASTER vs post-MASTER), add the explicit local qualifier “computed against distinct null procedures and not directly comparable,” or rephrase to avoid side-by-side presentation.

MAJOR

- P4-M1 (Sec. II.B Page 3): Ambiguity in training augmentation counts and selection rule
  • Problem: You report 25,790 source images; post-augmentation pool 26,616; “the 826-image difference arises entirely from horizontal-flip augmentation applied to the training split only,” but this implies only 826 of ~20.5k training images were augmented, which is unusual and not explained. This matters for reproducibility and potential bias.
  • Required fix: Precisely document the augmentation policy: which images were flipped and why (class balancing? QC-based subset?), per-class counts before/after augmentation, and how this integrates with the flip-equivariance consistency loss. Include a small table in Appendix B stating the exact counts per class in train/val pre-/post-augmentation and the selection rule for the 826 flips.

- P4-M2 (Throughout, e.g., Secs. IV–VII and Appendices): Excessive reliance on in-text repository path references (“artifact pipelines/...”) for evidentiary support
  • Problem: Many key statements are backed only by internal path references. While admirable for provenance, PRD readers must be able to follow the logic without browsing a repo. Some numbers (e.g., fixed-axis recovery medians, null histograms) are not summarized in the paper and live only in artifacts.
  • Required fix: Move detailed artifact-path references to a Supplement/Zenodo README and replace in-text path strings with concise summaries and a single DOI link. For every load-bearing claim that currently points only to an artifact, add a compact in-paper numeric summary (sample sizes, means, σ, p, and a single figure/table where appropriate).

- P4-M3 (Sec. IV.C Page 8; Table I Page 5): Real-space null definitions and mask thresholds—clarify equivalence and choices
  • Problem: The isotropic “pixel-permutation null” (permute Ap across in-mask pixels) is used as your primary real-space null. On a highly non-uniform mask this maintains the one-point distribution but destroys spatial correlations in a way that is not equivalent to a draw from an isotropic sky on the given mask. You also use a per-galaxy label-shuffle null (preserving per-pixel totals). While both appear, the rationale for preferring one as “primary” is scattered.
  • Required fix: Add a short methodological subsection justifying the pixel-permutation null as an appropriate isotropy baseline on a patchy mask and explain the relation to the per-galaxy label-shuffle null (what each preserves/breaks). Show that both yield consistent p,z for the HC estimator (a two-line table is sufficient). State explicitly which null is used for every quoted real-space σ and why.

- P4-M4 (Sec. III.A Page 3, notation across paper): Notation reuse for A and Ap may confuse readers
  • Problem: You use “A” both for the full-amplitude dipole in injection and for “asymmetry-A units = 2(fCW−1/2)”. Although you explain the mapping, the reuse risks confusion.
  • Required fix: Adopt distinct symbols: e.g., use Adip for the full-amplitude dipole in pCW(ˆn) and retain Ap for map asymmetry. Where you equate them, show the short one-line derivation once and then stick to one symbol thereafter.

- P4-M5 (Sec. V.A Page 12, Sec. VII Page 14): Strength of statements vis-à-vis Shamir claims
  • Problem: You say your pipeline is “inconsistent in amplitude with Shamir’s claimed ~3% signal by a factor ~5–12,” while acknowledging no matched-footprint Ganalyzer re-analysis has been done. This is acceptable as an amplitude-level tension, but in places it reads borderline exclusionary.
  • Required fix: Rephrase all such statements to “in tension at the amplitude level under our pipeline; a matched-footprint Ganalyzer re-analysis is required for a likelihood-level exclusion.” Ensure no sentence can be read as a formal exclusion.

MINOR

- P4-m1 (Sec. I Page 2, novelty claim): “largest chirality-labeled galaxy catalog to date”
  • Problem: The claim is plausible, but it would benefit from a one-line quantitative comparison to specific prior labeled datasets (e.g., CE-ResNet’s 1.95M sample; Shamir’s ∼1.3M spirals) with a citation back to those numbers to avoid ambiguity.
  • Required fix: Add a parenthetical with the exact comparative numbers and citations.

- P4-m2 (Fig. 8 caption Page 10; Table III caption Page 11): Apodization label formatting
  • Problem: The notation “C 2 2◦” for the apodization reads awkwardly. In some places you say “C2 apodization with 2° length,” elsewhere “C 2 2◦.”
  • Required fix: Standardize to “C2 (cosine-squared) apodization, 2° length” everywhere.

- P4-m3 (Sec. VII.a Page 14–15): Harmonic completeness curve labeling vs observed z
  • Problem: The panel text says “obs. σ≈+7.28,” but the caption mentions 7.21 in that exact run due to a different background null. This is easy to misread.
  • Required fix: Add a single sentence in the panel caption clarifying why the plotted point’s σ differs from the canonical value, and place the canonical value in bold in the text to avoid confusion.

- P4-m4 (Appendix A Page 16): Monopole subtraction effect on σ
  • Problem: You note C1 drops ~34% while σ rises from +1.85 to +3.64. You explain this due to null-mean/width shrinkage, but readers may want a number.
  • Required fix: Add the corresponding ⟨C1⟩null and σnull before/after subtraction as a small 2×2 table to demonstrate the effect numerically.

- P4-m5 (Sec. II.B Page 3): 66.5% training labels from CE-ResNet and independence
  • Problem: You correctly caveat dependence. To strengthen, quantify the spatial cross-correlation (if any) between your final map and CE-ResNet’s predictions on an overlapping footprint, even if only in a small diagnostic table.
  • Required fix: Include a one-line numeric summary (e.g., cross-spectrum rℓ at ℓ=1–3) or add this to future work and soften any language implying full independence.

NIT

- P4-n1 (Throughout): Typographical issues
  • Examples: “apodized-footprint MASTER at ℓ = 1 (Nall ≥ 1 mask, fsky = 0.494, C 2 2◦; +7.28σ …)” – stray spacing; occasional missing hyphens around “label-shuffle” and “block-bootstrap.”
  • Fix: Copy-edit for consistent hyphenation and spacing.

- P4-n2 (Appendix B Page 17): Units and symbols
  • Problem: Occasional missing subscripts/superscripts in inline math (“vit small patch16 224”).
  • Fix: Typeset consistently.

- P4-n3 (References Page 22–23): Minor formatting
  • Problem: Some references include backticks/diacritics that render oddly (e.g., “Iveˇzi´c, … Tyson ˇ et al.”).
  • Fix: Normalize references with proper LaTeX accent macros.

Arithmetic and consistency checks performed

- Table II binomial uncertainties and σ-deviations recompute correctly:
  • A (raw) fCW=0.507879, σbin ≈ 0.000274 → deviation (f−0.5)/σ ≈ +28.7σ (table: +28.72σ) OK.
  • C (equivariant) fCW=0.497353, σbin ≈ 0.000279 → deviation ≈ −9.49σ (table: −9.47σ) OK.

- Fisher floor Eq. (4) σ(A)=√(3/N):
  • N=3,201,160 → σ(A)≈9.68×10^-4; 3σ≈0.29% OK.
  • N=949,584 → σ(A)≈1.78×10^-3; 3σ≈0.53% OK.

- WLS template-fit exclusion (Appendix D):
  • Abest=4.55×10^-3 (Ap units), Aref=0.034, σboot=1.63×10^-3 → z≈(0.00455−0.034)/0.00163=−18.1 OK.

- Table IV monopole+mask reproduction:
  • (1.6961−1.6846)/0.0068=+1.69σ OK; hemisphere max asymmetry (3.484−1.693)/0.405=+4.42σ OK.

- Table III MASTER rows:
  • Apodized ℓ=1: (24.74−1.93)/3.12=+7.31σ OK; Canonical ℓ=1: (7.27−0.57)/0.84=+7.98σ (tabulated +7.93σ; minor rounding) OK.
  • Rank-p computation with (k+1)/(N+1) is consistent with examples.

- Real-space primary amplitude:
  • Reported Adip=4.4×10^-3 (Ap) = 0.44% full amplitude; below the A50≈0.75% HC floor—consistent.

Length and focus

- The manuscript is long (23 pages) for a single principal conclusion (a null real-space dipole) plus diagnostics. Consider consolidating diagnostics and moving the majority of repository-path detail to a Supplement. A focused ≤15-page main text would improve readability without sacrificing rigor.

Effect sizes

- The paper generally states amplitudes (e.g., Adip in Ap/fCW units) alongside σ, which is good. Ensure every σ in the abstract and conclusions is accompanied by either a fractional amplitude or a statement identifying the estimator units (you largely do this).

Abstract-last drift sweep

- Most abstract claims are backed and carry caveats. The sole major inconsistency is P4-E1 (3.64σ vs 7.93σ for the same canonical ℓ=1 channel). This must be resolved to avoid confusing or overstating a diagnostic residual. The rest of the abstract’s careful disclaimers about non-comparability are appropriate.

Provenance surfaces

- Commit hash and version tag are provided, but without a frozen DOI the release is not stable (P4-E2). Please fix.

Standalone-reader test

- With P4-E1/E2/E3/E4 addressed, the paper will be self-contained. Currently, several key artifacts are only referenced by path and should be summarized in-paper (P4-M2).

## Summary recommendation
MAJOR REVISIONS

The primary null result in real space appears sound and carefully caveated, and much of the statistical methodology is well thought out. However, the contradictory canonical MASTER ℓ=1 significances (+3.64σ vs +7.93σ) must be reconciled; stable, working DOIs/URLs must be provided for all released artifacts; a contradictory b/a-based “edge-on” statistic must be clarified or removed; and every juxtaposition of σ values from different nulls needs a local non-comparability disclaimer. Additional clarity on the augmentation policy and moving heavy path references to a stable Supplement will substantially improve reproducibility and readability. Once these issues are corrected, the paper could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

ESSENTIAL

- P4-E5 (p-value definition inconsistency; Table III caption vs body text, multiple places)
  • Problem: Rank p is defined in Table III as (k+1)/(N+1). Elsewhere you report pMC = 15/500 = 0.030 for the 500-MC “canonical direct” run (e.g., Sec. IV.D, Conclusions §VII.c), i.e., k/N. These two conventions are not equivalent at small N and lead to different quoted probabilities (here 0.030 vs 16/501 ≈ 0.0319).
  • Required fix: Adopt a single definition for empirical p throughout (preferably (k+1)/(N+1) for small-sample bias control), recompute all quoted p’s to that convention, and annotate which convention is used in every figure/table reporting p-values.

- P4-E6 (MASTER null-construction inconsistency: “per-pixel label-shuffle” vs “per-galaxy label-shuffle”)
  • Problem: The canonical MASTER ℓ=1 null is alternately described as “per-pixel label-shuffle” (Fig. 8 caption; Sec. IV.D first paragraph) and “per-galaxy label-shuffle” (Sec. IV.C.b; Table III caption). These are different operations and can produce different null widths/means, directly affecting z and rank p. This inconsistency may also contribute to the unresolved +3.64σ vs +7.93σ discrepancy for the canonical unapodized mask (P4-E1 in your initial report).
  • Required fix: State precisely which shuffle is used for each MASTER result (canonical/apodized), justify that choice, and, if both were used at different times, show side-by-side how “per-pixel” vs “per-galaxy” shuffles change ⟨C1⟩null, σnull, z, and rank p on the same data/field. Then standardize on one null for each channel and revise all σ/p accordingly.

MAJOR

- P4-M6 (Appendix A.a conflates footprints and field conventions around the monopole-subtraction discussion)
  • Problem: The paragraph starts by declaring the apodized analysis footprint (Nall ≥ 1; Wp = Nall), then immediately discusses “canonical unapodized rows,” and then reports the monopole-subtraction effect (“C1 from 2.30×10^-5 to 1.51×10^-5 and σ rises from +1.85 to +3.64 (the canonical-mask number)”) without clearly specifying whether these before/after numbers refer to the apodized footprint or the canonical mask. The +3.64σ value is the canonical 500-MC figure, but the surrounding context has just switched footprints/weights, which is confusing and impedes reproducibility.
  • Required fix: Split this into two clearly labeled subparagraphs (apodized footprint vs canonical mask), and for each list: field definition, weight, monopole treatment, ⟨C1⟩null, σnull, z, and NMC, so the reader can track which numbers correspond to which footprint/configuration.

- P4-M7 (“Uniform in θ” axis draws characterized as “mildly” non-isotropic; injection protocol clarity)
  • Problem: The text describes θ-uniform axis draws as “mildly” over-weighting near-polar axes. Uniform in θ is substantially non-isotropic (area measure ∝ sinθ). While you do provide an area-uniform spot check, the description understates the difference and could mislead readers about completeness biases.
  • Required fix: Rephrase to “non-isotropic (over-weights near-polar axes by 1/sinθ)” and keep the area-uniform reproduction you already did as the primary robustness check in the main text (not just a spot check footnote). Consider standardizing the completeness curve to area-uniform axes and relegating θ-uniform to a sensitivity cross-check.

MINOR

- P4-m6 (Figure–text unit discipline: Fig. 8 vs surrounding text)
  • Problem: Fig. 8 caption states “per-pixel label-shuffle null,” but the body text in Sec. IV.C.b switches to “per-galaxy label-shuffle” without local clarification (see P4-E6). Even if you retain both in the paper, each figure/caption/paragraph that quotes a σ must explicitly specify which null it uses.
  • Required fix: Add a parenthetical “(per-pixel label-shuffle null)” or “(per-galaxy label-shuffle null)” to every sentence that reports a MASTER σ, including Fig. 8 caption and the first sentences of Sec. IV.D and VII.c.

- P4-m7 (Family-wise p-convention in Appendix C, leg/confidence max-statistic)
  • Problem: You define the per-cell statistic as two-sided |σ|, then state the family-corrected p as “the one-sided empirical exceedance” of the observed max|σ|. Mixing a two-sided per-cell statistic with a one-sided family exceedance can confuse interpretation.
  • Required fix: Clarify explicitly: “We compute the distribution of the maximum of |σ| (two-sided per test); the family-wise p is the empirical exceedance of the observed max |σ| in that distribution.” If you intend truly one-sided testing, align the per-cell statistic and family aggregation accordingly.

- P4-m8 (Abstract/Conclusions: occasional “per-pixel vs per-galaxy” null labels missing)
  • Problem: In the abstract, some σ’s are tagged with “label-shuffle null” or “pixel-permutation null,” others are not. Given the number of distinct nulls, every σ should be locally tagged to avoid ambiguity.
  • Required fix: Append the null label to each σ in the abstract and conclusions (e.g., “+7.28σ (MASTER ℓ=1, apodized, per-galaxy label-shuffle null)”).

- P4-m9 (Terminology: “monopole-preserving” vs “pre-MASTER”)
  • Problem: You sometimes use “pre-MASTER pseudo-Cℓ” and elsewhere “monopole-preserving” for closely related but not necessarily identical estimators. In Appendix E you compare a “monopole-preserving” +4.31σ to canonical +3.64σ; the relationship is not immediately obvious to a reader.
  • Required fix: Add a one-sentence glossary noting: “pre-MASTER pseudo-Cℓ” = no mode-coupling deconvolution; “monopole-preserving” = no monopole subtraction prior to pseudo-Cℓ; and state explicitly which of these two toggles are on/off for each quoted σ.

NIT

- P4-n4 (Verb tense/wording around axis draws)
  • Problem: Phrases like “each injection draws an independent random dipole axis (polar angle θ∼U(0,π), azimuth ϕ∼U(0,2π), equatorial frame; uniform in polar angle, which mildly over-weights near-polar axes)” could be tightened and corrected per P4-M7.
  • Fix: Replace with “axes drawn isotropically unless otherwise stated; where noted, θ-uniform draws are used (non-isotropic; over-weights near-polar axes by 1/sinθ).”

Rationale for “fresh eyes”
- The first review did not check for inconsistent p-value conventions, nor did it catch the “per-pixel” vs “per-galaxy” null-construction inconsistency that recurs across figures, captions, and tables. It also did not flag the footprint/field conflation in Appendix A.a around the monopole-subtraction discussion, or the understatement of the θ-uniform axis-draw anisotropy. These issues directly affect statistical interpretation and reproducibility and should be corrected prior to publication.