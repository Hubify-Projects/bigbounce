# P4 2026-06-04_1733pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 27.1s

---

Referee report on P4 (v1.0.151, 4 June 2026)  
Methodology / statistics / internal-consistency review  
Physical Review D – Cosmology Methods

I have read the full 57-page manuscript, the on-disk JSON/NPY artefacts and the quoted code snippets.  
The analysis has clearly progressed since v1.0.149; all six editor-mandated “BLOCKER” items are now present in some form (see Finding E1).  Nevertheless, multiple essential problems remain.  The paper is not yet publishable in PRD.

Below I list 31 findings grouped by severity.  Section/page numbers refer to the PDF margins; “Sec.” refers to the manuscript headings.

------------------------------------------------------------------
ESSENTIAL
------------------------------------------------------------------

E1  (Throughout)  BLOCKER-compliance audit  
• 18 σ “overclaim”: removed – OK.  
• Mask hierarchy relabelled – present.  
• Canonical–residual decomposition table – Table VIII present.  
• Sensitivity-budget table – Table IX present.  
• “Shamir shorthand” – mostly removed, but “Shamir’s ∼3 % class” (Sec. VII ¶2) still uses the shorthand instead of quoting the actual numbers or σ.  
• “Journal-clean sweep” – NOT satisfied: tens of occurrences of version-history language and internal audit tags such as  
“pipelines/p2_chirality/outputs/…”, “earlier-draft claim”, “retraction note”, “honesty note”, “pod run 29.3 s”, “$0 marginal GPU spend”, etc.  
Fix: scrub all history/log language and file-path chatter from the body text.  Provide those details only in a supplemental materials section or data-availability note.

E2  Sec. III E – Rotational-equivariance validation  
The manuscript claims full rotational robustness on the basis of two 2 000-galaxy “hold-outs”, yet later concedes a 21 % per-galaxy argmax flip rate.  That rate is large enough to degrade all hard-label statistics.  No propagation into Table XVI injection tests or hemisphere scan is shown.  
Fix: propagate the 21 % extra noise into every hard-label σ, or redo all hard-label analyses with a D4-TTA catalogue.

E3  Sec. VI C – Sensitivity floor confusion  
The text alternates between  
(i) 0.2 % (statistical)  
(ii) 0.29 % (Fisher)  
(iii) 0.4 % (full-amplitude)  
(iv) 0.75 % (empirical)  
with factor-of-two conversions half explained.  Figures 0.2 % and 0.29 % are quoted in the Abstract and Conclusions without the caveats.  
Fix: pick one definition (full-amplitude A) and quote a single number everywhere, giving the conversion once.  State explicitly that the empirical systematic-inclusive threshold is 0.75 %.

E4  Tables VI and VII – Mixed nulls reported as comparable σ  
Table VI lines 2–5 use a “label-shuffle” null; the canonical ℓ=1 row of Table VII uses a “monopole-only binomial” null.  Values are juxtaposed as if differences are physical.  This violates Instruction #7 (σ values from different nulls must not be presented on the same scale).  
Fix: rewrite the discussion; never compare σ computed under different null families without renormalising.

E5  Section III A – “Declared analysis hierarchy”  
The hierarchy was fixed only after first-round results (v1.0.76).  That is post-hoc and violates the “primary estimator pre-declared before looking at data” rule.  
Fix: move the entire hierarchy to a time-stamped preregistration document (even if retrospective) and cite it.  Alternatively, demote the present work to “exploratory” and adjust claims (remove falsification language).

E6  Sec. IV E/Table XI – Multiple-comparison treatment incorrect  
The 4.50 σ DECaLS [0.5,0.6) result is called “family-significant” after applying a Bonferroni over 15 cells, yet also a “max-statistic MC” over 15 gives only 2.4 σ.  The manuscript keeps the larger number in the narrative.  
Fix: adopt one global LEE procedure (Bonferroni OR max-statistic) and use it consistently.

E7  Length – 57 pages (main text 50 pp).  PRD methods papers normally ≤30 pp.  
Fix: shorten by deleting the extensive version-history digressions and all code-path prose.  28–32 pp should suffice.

------------------------------------------------------------------
MAJOR
------------------------------------------------------------------

M1  Sec. III C – External training labels  
67.6 % of training labels are CE-ResNet pseudo-labels; 32.4 % are genuine human.  No weighting or uncertainty propagation is provided.  That affects the quoted “69.9 % agreement with GZ1”.  
Fix: include a confusion-matrix with CE-ResNet removed from both training and validation, or justify the circular usage.

M2  Sec. IV C – Counting of Monte-Carlo realisations  
Different MC sizes (500, 1 000, 10 000) are used interchangeably.  The relative error on σnull ≈3 % at N=500 is not included in any z.  
Fix: report MC-error bars and propagate them or rerun all nulls at a single fixed N (≥5 000).

M3  Sec. VI G – Template regression  
The “9-template” fit uses a WLS with no explanation why the pixel weighting is optimal.  The block-bootstrap rescaling (×14.7) is arbitrary.  
Fix: supply the full covariance model or drop the quantitative g∗/Π claims.

M4  Many places – duplicate phrases  
E.g. “canonical canonical-mask”, “Catalog C is the canonical tier … canonical mask”, etc.  Edit.

M5  Sections labelled “Honesty note”, “Retraction note” inside the body.  These belong only in change-log / cover-letter.  Remove.

M6  Self-citation overload: >200 in-text citations to the author’s own GitHub paths.  Move to a “Reproducibility” appendix.

M7  Mention of “AI assistants (Anthropic Claude)” is irrelevant for PRD.  Delete.

------------------------------------------------------------------
MINOR
------------------------------------------------------------------

m1  Abstract last sentence: “… with journal-clean sweep” appears – residual editorial note.

m2  Footnote markers jump in and out of numeric/bib style.

m3  Figure 7 colour-bar units not stated.

m4  Table XV column headers wrap awkwardly.

m5  Some references missing journal pages (e.g. Ref. [18]).

m6  Typos: “equivariance-corrected angular dipole” → “equivariance-corrected”, “interpre-tations”.

------------------------------------------------------------------
NIT
------------------------------------------------------------------

n1  p. 17 “∼” typeset as ASCII tilde in running text.

n2  Extra space before percent signs in several tables.

n3  Units “sr” appear without definition.

------------------------------------------------------------------
##  Summary recommendation  
MAJOR REVISIONS

The six editorial blockers are largely cleared, but the manuscript still mixes null hypotheses, carries unresolved rotation noise, embeds code-path language throughout, and is far over length.  A focused 30-page revision that (i) cleans the prose, (ii) propagates the 21 % flip noise, (iii) unifies the null treatments, and (iv) removes all post-hoc estimator choices is required before the work can be considered for publication.