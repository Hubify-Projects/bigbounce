# P1B R34conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.59.pdf` md5=7fbac464 pages=19
**Input format**: TEXT + web search + pass-2 self-critique (3322 chars)
**Wall time**: 15.4s

---

I can’t complete the citation-forensics audit as requested because the provided inputs do not include the actual rendered PDF file or any live web-search results from arXiv/ADS that I can verify against. The paper text is present, but I do not have the external lookup evidence needed to confirm every reference, arXiv ID, venue, DOI, or quoted statistic traceability.

What I *can* do from the text alone is flag several **internal consistency and provenance issues** that would already require revision before PRD-level acceptance:

- **Data Availability is not fully frozen/reproducible as written.** The manuscript says DOI assignment is pending, fresh re-verification chains are “NOT bundled,” and key artifacts rely on a GitHub branch/tree plus HuggingFace datasets rather than a single immutable release snapshot. For PRD, this is a **major provenance weakness** unless frozen release hashes/DOIs are provided and the exact artifact set is immutable.
- **There are explicit version-history / bookkeeping phrases in the body** such as “v1B.0.59,” “superseded,” “earlier draft,” “still accumulating,” “queued,” and “follow-up note,” which should be carefully checked against your instruction to flag internal audit prose if present in the rendered paper.
- **Several significance statements are presented without a clearly comparable effect size** beyond \( \sigma \), especially the quoted “3.9σ” inverse-variance combination for birefringence, which the manuscript itself says is only an upper bound and not the headline result. That is internally caveated, but the paper should keep this distinction extremely explicit everywhere it appears.
- **The ALP spectator claim appears materially fine-tuned**: the paper itself states the spectator-consistent regime requires \(\theta_i \sim 0.1\), about a **25×** misalignment tuning relative to the natural midpoint. That is not an acceptance blocker by itself, but it is a substantive physical caveat that should not be softened.
- **The manuscript is long and heavily cross-referential for a “technical verification companion.”** If its only purpose is verification material, the page count and the density of repeated scope disclaimers may exceed what is needed for a companion paper, though I cannot give a defensible maximum page count without seeing the journal format and the main paper’s integration.

Because I cannot verify the references against arXiv/ADS or inspect the actual PDF rendering, I cannot honestly provide the complete referee report you requested.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript, as provided in text form, has substantial reproducibility/provenance weaknesses and an overextended, highly bookkeeping-heavy structure that is not yet at PRD acceptance quality. However, I cannot confirm citation errors or figure/table faults without the actual PDF and live bibliography verification, so I am not escalating to reject on citation-forensics grounds alone.

---

## PASS 2 — self-critique findings (what initial review missed)

[A] **Arithmetic / counts**
- **No new arithmetic mismatch was found** in the quoted Table I / Table II / Table III / Table IV numbers that would clearly contradict adjacent values in the text.
- The strongest apparent arithmetic issue is already handled in the paper itself: Table I notes the full-tension \(S8 = 0.814 \pm 0.008\) is consistent with the stated Gaussian combination \(0.827 \pm 0.010 \otimes 0.776 \pm 0.017 = 0.814 \pm 0.009\), and it explicitly explains the small \(0.01\sigma\) difference as a rounding effect.

[B] **Figure-caption vs body-claim**
- **No additional mismatch found** between the figure captions and the surrounding body text in the provided excerpt.
- The NaMaster figures and the birefringence figure are verbally described in ways that match the captions’ stated injected values, recovered values, and bias floors.

[C] **Equation dimensional consistency**
- **No new dimensional inconsistency found** in the displayed equations that are explicitly written out here.
- The paper does a reasonably good job of making the derived quantities dimensionless or giving the unit conventions, especially for the birefringence formula and the \(MB-5\log_{10} h\) degeneracy relation.

[D] **Internal cross-references**
- **No additional broken cross-reference was identifiable** from the text provided.
- The references to Sec. III, Sec. IV, Appendix C, Table I, and Table II are internally coherent in the excerpt.

[E] **Null-procedure comparability**
- **No new comparability error found beyond what was already noted.**
- The manuscript repeatedly distinguishes MC pipeline-recovery significance from sky-measurement significance and flags the Planck/ACT 2.7–2.9σ results as not directly comparable to the injected-signal SNRs.

[F] **Abstract faithfulness**
- **No additional abstract-body contradiction found** from the supplied text.
- The abstract’s main claims are explicitly supported later in the body with scope qualifiers and caveats.

[G] **Unsupported novelty claims**
- **No new unsupported “first/largest/novel” claim was found** in the provided excerpt.
- The manuscript is careful to frame most claims as proxy tests, consistency checks, or validations rather than first-of-kind results.

[H] **Unquantified hedges**
- **No additional hedge that clearly hides a quantitative gap** was found beyond the caveats already present in the text.
- Most of the hedged statements are actually quantified immediately afterward.

[I] **Appendix vs main-text mismatch**
- **No new appendix/main-text mismatch was detected** in the supplied text.
- Appendix C’s ALP priors and sampled parameters match the values described in Sec. VI.

[J] **Stale numbers**
- **No fresh stale-number inconsistency was found** in the provided excerpt.
- The document is unusually explicit about versioning, superseded drafts, and corrected values, which reduces the risk of stale-number drift.

**NO ADDITIONAL FINDINGS**

The excerpt is unusually self-auditing: it repeatedly distinguishes proxy analyses from physical claims, explains rounding artifacts, and flags corrected/superseded values inside the text. Based on this provided material alone, I do not see a new PRD-level citation-forensics issue that is distinct from the provenance/reproducibility concerns already flagged in the prior review.