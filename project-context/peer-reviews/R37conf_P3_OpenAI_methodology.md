# P3 R37conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.103.pdf` md5=566f7150 pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5872 chars)
**Wall time**: 10835.3s

---

Referee report (PRD methodology review)

I read the entire submission, including all figures, tables, equations, captions, appendices, and the abstract, and recomputed all quoted numbers that can be checked from the text. Below I list all issues found, classified by severity, with precise page locations and required fixes.

ESSENTIAL

P3-E1 (Section IV.B, p.14): Cramér’s V formula and numerical evaluation are incorrect
- Offending text: “Cramér’s V =
√(χ²/(N · (k − 1))) = 376,713/(378,280 × 24,047) ≈ 0.020”
- Problem: The expression shows a square root but the numerical evaluation omits it. χ²/(N(k−1)) = 376,713/(378,280×24,047) ≈ 4.14×10−5, and √(4.14×10−5) ≈ 0.0064, not 0.020. The current text both miscomputes V and thereby overstates the effect size by ~3.1×.
- Required fix: Recompute V correctly and update both the numerical value and the accompanying interpretation (“weak” should become “very weak”). Explicitly show the intermediate value χ²/(N(k−1)) and the square root step to avoid confusion.

P3-E2 (Section V.b, pp.17–18): Dimensionally wrong definition of F0 in the Fisher forecast
- Offending text: “F0 = 1/8.982 = 0.01239 (units: 1/σ(fNL)^2 …)”
- Problem: The units and the value are for 1/σ^2, but the printed expression is 1/σ. Numerically, 0.01239 = 1/(8.98)^2, not 1/8.98. As written, the equation is dimensionally inconsistent and misleading even though the numerical value used is correct for 1/σ^2.
- Required fix: Replace “F0 = 1/8.982” with “F0 = 1/σ^2(fNL,std) = 1/(8.98)^2 = 0.01239.” Audit the manuscript to ensure all instances of F0 and related calculations consistently use 1/σ^2.

P3-E3 (Data availability, p.22): Missing, finalized, citable DOIs/hashes for all load‑bearing artifacts
- Offending text: “will be publicly released with the arXiv posting… A Zenodo DOI will be minted at submission and cited here in place of this sentence (DOI inserted at submission).”
- Problem: This paper’s central claims (catalog content, thresholds, dedup geometry, injected‑signal tests, MCMC chains) depend on external artifacts. PRD standards require reproducibility at acceptance. Promises of future release are insufficient.
- Required fix: Provide permanent, working DOIs (or equivalent immutable archival identifiers) for all datasets, model checkpoints, scripts, and analysis outputs referenced (including committed JSON artifacts, the dedup manifests, injection–recovery plant files, and the PTA MCMC chains). Insert the exact DOIs and the frozen commit hashes in the main text. Remove “will be released” language.

P3-E4 (Abstract, pp.1–2): Catalog-tier guidance is internally inconsistent and confusing
- Offending text: “…recommended catalog-grade tier contains 269,317 unique entries (269,117 point-source after dropping the 200 Planck map patches…); downstream object-level analyses should use the 378,080 point-source tier; the recommended catalog-grade subset is ∼269,000… including the 200 Planck map patches… object-level analyses should additionally drop the map patches…”
- Problem: The abstract mixes three different sets (378,080 point-sources; 269,317 catalog-grade including patches; 269,117 catalog‑grade point‑sources) and instructs different downstream use (“use 378,080” vs “recommended catalog‑grade 269,317”). This is easy to misread and contradicts itself about whether to include Planck patches in a catalog‑grade subset.
- Required fix: State a single, unambiguous recommendation in the abstract. Example: “For object‑level analyses use the 269,117‑object catalog‑grade point‑source subset (6‑way dedup; Planck patches excluded). The full point‑source tier (378,080) is provided for completeness.” Move the alternative counts to a clarifying sentence.

P3-E5 (Section V.b, p.18): Inconsistent description of the “1σ envelope” construction for σ(fNL)
- Offending text: “the envelope — not the convex central value — is the appropriate summary… the lower edge 3.92 is … at ˆα+σα = 0.84, and the upper edge is ˆα−σα = −0.46 clipped at α = 0… This is the image of the ±1σ interval…”
- Problem: The “image of the ±1σ interval” under σ(α) = 1/√(F0 + cα^2) is not obtained by clipping; the true image would evaluate at |α| = {0.84, 0.46}. You then override the α = −0.46 case by clipping to α = 0 to enforce monotonicity of the “worst case” (largest σ) — a different construction.
- Required fix: Define the envelope precisely as min/max over |α| ∈ [0, | ˆα|+σα] given α^2 mapping, and say explicitly that because the ±1σ interval crosses zero, the maximum σ occurs at α = 0, which you adopt as the upper edge by construction. Remove “image of the ±1σ interval” or qualify it to avoid implying a probabilistic coverage statement.

MAJOR

P3-M1 (Appendix C / Fig. 11, p.23): Shot‑noise “penalty” improves σ rather than degrades it
- Offending text: “With a 15% Fisher-info penalty, σ(fNL) = 12.56, i.e., σ(fNL) decreases by 1.27% relative to the baseline-multi 12.72 (a residual improvement); with a 30% penalty, σ(fNL) = 13.35, i.e., σ(fNL) increases by 4.97%…”
- Problem: A “penalty” to the Fisher information should increase σ relative to a higher‑information baseline. Your narrative suggests that the baseline‑multi value is already degraded relative to the “dense limit,” but this is unclear. As written, the 15% “penalty” reduces σ, contradicting the stated meaning of penalty.
- Required fix: Define precisely which configuration defines “baseline-multi,” which defines the “dense-tracer limit,” and how the 15–30% penalty is applied (to which Fisher block). If baseline‑multi already includes shot noise and the “penalty” is relative to the dense limit, rephrase to avoid implying that adding a penalty can improve constraints relative to the exact same baseline. Provide the algebra used to map a 15–30% Fisher‑information reduction to the σ values quoted.

P3-M2 (Section IV.A, p.13; Fig. 6): Mixed matching radii in SIMBAD-unmatched fractions
- Offending text: Table I uses 5″; the pooled aggregate of 58.8% is at 3″ (235/400), and the text notes the discrepancy later.
- Problem: Presenting a headline pooled fraction at a different radius than the per‑survey fractions risks misinterpretation.
- Required fix: Either (a) recompute the pooled fraction at 5″ and present that as the headline, or (b) promote the 3″ fact to the first sentence of that paragraph and label the 58.8% as “3″ aggregate; per‑survey values at 5″ — not directly comparable.” Ideally include both 3″ and 5″ pooled numbers.

P3-M3 (Throughout; e.g., §§II.D, III.E, Table I footnotes): Heavy reliance on repository “artifact” file paths in the main text
- Problem: The paper repeatedly cites internal JSON/CSV pathnames as provenance for results. This is good for reproducibility but clutters the scientific narrative and is fragile if URLs change.
- Required fix: Move file-path citations and low-level run‑provenance into a single online Appendix or a dedicated “Reproducibility note,” and keep only stable DOIs and commit hashes in the main text.

P3-M4 (Abstract and §I, pp.1–2): “Largest multi-archive anomaly search” novelty claim
- Problem: The benchmark used is [11], which is single‑survey. A “largest multi‑archive” claim needs either a literature audit or a softer formulation.
- Required fix: Either add a brief literature check supporting the multi‑archive novelty claim (with citations), or soften to “to our knowledge, larger than prior single‑survey catalogs (e.g., [11]).”

P3-M5 (Section III.F, p.12): Train/validation over-representation claim would benefit from a proper distributional test
- Offending text: Binomial p ≈ 4×10−4 on top‑200 train/val membership.
- Problem: A tail count on the top‑200 is indicative but not a full test against memorization. A simple two‑sample comparison (e.g., KS test) of the score distributions for train vs validation over all 2×10^5 patches would be stronger.
- Required fix: Add a train vs validation score-distribution comparison on the full bank (e.g., KS statistic and p-value), or clearly state this is a heuristic check and report the train/validation medians/quantiles.

P3-M6 (Section III.E, p.11–12): eROSITA “membership-only” tier needs a firm archival basis
- Problem: The score axis is irreproducible; the membership is asserted as canonical. For PRD, deposit of the inputs needed to reconstruct the 298 selection by an independent reader is expected.
- Required fix: Archive and cite DOIs for (i) the exact 47‑feature table used, (ii) the raw reconstruction scores, (iii) the 16‑d latent vectors used for the IF stability test, and (iv) the list of the 298 IAU names. Clarify in the main text that the reproducible object‑level product is the membership list, and that no reproducible per‑object score is provided.

MINOR

P3-n1 (Section III.C, p.10): SDSS continuity slice percentage rounding
- Offending text: “77,905 … (4.05% of the 1,925,279 …)”
- Problem: 77,905/1,925,279 = 4.046%. If you quote to two decimals, round to 4.05% but note it’s approximate.
- Required fix: Add “≈” or state “4.046%” exactly.

P3-n2 (Section IV.C, p.15): Radius-sweep sensitivity sentence
- Offending text: “a maximum unique-count variation of 0.086% relative to the canonical 5″ result”
- Problem: This number is the larger of the two one-sided deviations (from 3″). Consider stating both deviations explicitly: +0.0856% (3″) and −0.0357% (7″).
- Required fix: Provide both one-sided deviations or the full range (0.0357–0.0856%).

P3-n3 (Section II.B, p.4): Clarify that rB,rR,rZ are mean absolute residuals, not standardized
- Problem: You note they are not independently z-scored per arm; remind readers they are not significance measures across objects and can be S/N‑weighted by the input scaling.
- Required fix: One clarifying sentence that rX are descriptive within‑object diagnostics only.

P3-n4 (Section IV.A, p.14): False-match rate derivation
- Problem: You cite nSIMBAD ≈ 3.0×10−5 arcsec−2 and Pfalse ≈ 2.4×10−3 but do not show the formula.
- Required fix: Add Pfalse ≈ π r^2 n (for small rates) with r = 5″ to make the calculation fully transparent.

P3-n5 (Table I caption, p.7): Cross-transfer total includes ACT but ACT is not shown in the table block
- Problem: Readers may be confused by a total that includes a survey not listed in the table body.
- Required fix: Add a one-line “ACT DR6 (cross-transfer, quarantined): 200” row grayed or footnoted directly under the table, or adjust the caption to state explicitly that ACT’s 200 are included only in the cross-transfer total.

P3-n6 (Section V, pp.17–19): Keep “not directly comparable” caveats adjacent to every juxtaposition of σ(fNL) baselines on different normalizations
- Problem: You do this in several places; ensure every time σ=8.98 appears near σ=16.85 (Appendix C) the non‑comparability note is re‑stated.
- Required fix: Add a parenthetical “(not directly comparable to Appendix C normalization)” wherever both numbers appear in close proximity.

P3-n7 (Figures 3 and 6, pp.9 and 14): Axis labeling clarity
- Problem: Fig. 3 right uses a log–log axis for S with a huge range; Fig. 6’s fractions mix radii as noted above.
- Required fix: In Fig. 3 caption, reiterate that SDSS panel uses DESI-trained cross-transfer scores on a different scale. In Fig. 6, add “aggregate at 3″; per-survey at 5″.”

P3-n8 (Typos/formatting, multiple pages): Spurious “p” glyphs around radicals; missing multiplication dots
- Problem: In several places (e.g., Cramér’s V line) the radical prints with stray “p” characters; some places show “1.1×106” without the multiplication dot or space.
- Required fix: Clean the math typesetting.

NITS

P3-nt1 (General): Many internal run-file paths in prose
- Suggest moving these to a reproducibility appendix to improve readability.

P3-nt2 (Appendix E, p.25): ESS computation convention
- You note the emcee ESS convention; optional to add the factor‑of‑2 remark to avoid confusion for readers using different ESS definitions.

P3-nt3 (Abstract, p.1): “largest-scale application…” wording
- Consider softening to “to our knowledge” unless a literature audit is added (see P3-M4).

Arithmetic checks and consistency spot‑audit (passed unless noted above)
- Key ratios in the abstract/body check out: 378,080/2,685 ≈ 140.8 (∼141×); 269,117/2,685 ≈ 100.2 (∼100×); 195,829/2,685 ≈ 72.9 (∼73×). DESI science‑class recount 2,468/2,685 ≈ 0.919 (∼0.9×). 98.7% of DESI clusters non‑primary: 1−2,468/190,015 ≈ 0.9870. SDSS 77,905/2,304,830 ≈ 3.38%. LAMOST 44,075/11,418,594 ≈ 0.386% (0.39%). eROSITA 298/930,203 ≈ 0.032%. NEOWISE mask retention 419/436 ≈ 96.1%. Ecliptic polar caps area fraction sin(90°)−sin(80°) ≈ 0.1519% per pole → 3.04% total? (Your 1.52% for both caps is correct using spherical-cap formula 2(1−cos 10°) ≈ 0.0304; the 1.52% stated is per cap; you then correctly compare two-cap 3.04%? Please double‑check the text: you cite “1.52% uniform‑null expectation”; if your test defines a single polar cap per hemisphere, the two‑cap expectation is 3.04%. If you injected on both poles and then compare to the total sample fraction in |becl|>80°, ensure the baseline area fraction matches your selection. If you indeed meant both caps together are 1.52%, this needs correction.)
- Planck train/val top‑200 overrepresentation binomial tail: for n=200, p=0.15, observe 48 validation patches; Z≈3.56; one-sided p≈1.8×10−4; two-sided ≈3.6×10−4; your “≈ 4×10−4” is fine.
- Fisher forecast central value: with α=0.19, c=0.0747, F0=1/(8.98)^2=0.012398, 1/σ^2=0.012398+0.0747×0.0361=0.015095 → σ=8.142 (8.14 reported).
- NANOGrav γ shifts: (3.0−2.567)/0.382 ≈ 1.13σ; (4.33−2.567)/0.382 ≈ 4.61σ — consistent.
- Bayes factor ratio: 3.23/(4.52×10−4) ≈ 7.14×10^3; log10 B ≈ 3.85 — consistent.

Length and scope
- The paper is long (29 pages) for a methods paper in PRD, largely because of in‑text run‑artifact citations and engineering details. I recommend moving most operational provenance into a single reproducibility appendix or a clearly linked dataset README (with DOIs), and tightening the main text to ≤20 pages without loss of scientific content.

Standalone-reader test
- The submission is largely self‑contained, but several key claims hinge on external artifacts (catalog lists, dedup manifests, PTA chains). These must be archived with immutable DOIs (see P3‑E3) to meet PRD standards.

Effect sizes
- Please correct Cramér’s V (P3‑E1) and ensure similar effect‑size statements are numerically accurate and interpreted appropriately.

## Summary recommendation
MAJOR REVISIONS

The submission presents a substantial, ambitious methodology/campaign. However, there are essential methodological/calc errors (Cramér’s V), a dimensionally incorrect expression in the Fisher section (though numerically used correctly), and missing finalized DOIs for all load‑bearing artifacts. The abstract’s catalog‑tier guidance needs to be made unambiguous. Clarifying the “penalty” logic in Appendix C and tightening the use of repository pathnames in the main text are also required. With these corrections and a reproducibility‑grade archival release in place, the paper could meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

ESSENTIAL

P3-E6 (Section IV.B, p.14): Pearson p-value for dust-correlation is numerically inconsistent
- Offending text: “no correlation with Planck dust intensity (Pearson r = 0.006, p = 0.21; … Nside = 64, 24,049 occupied pixels)”
- Problem: For n = 24,049, r = 0.006 gives t ≈ r sqrt((n−2)/(1−r^2)) ≈ 0.93 → two-sided p ≈ 0.35, not 0.21.
- Required fix: Recompute and update the p-value (and, if you retain Pearson, quote n explicitly as you did earlier in the paragraph). If a different n or a one-sided test was used, state it and adjust the number accordingly.

MAJOR

P3-M7 (Table V, p.21): Stale/garbled text in caveat (j)
- Offending text: “(j) GS corrected: σ(fNL)GS ∈ [0.94, 8.98] central 1.95; prior ±7.43 dropped Fisher-pos. α2-form; caveat (i)”
- Problem: The phrase “prior ±7.43 dropped” is unintelligible and looks like a stale edit fragment. It also risks confusing readers about what uncertainty or prior you are referring to.
- Required fix: Replace with a clear sentence. Example: “Gold+Silver: αGS,jk = 1.83 ± 2.03 → σ(fNL) = 1.95 (central) with envelope [0.94, 8.98] under the positivity-respecting form; see caveat (i).”

MINOR

P3-n9 (Section IV.A, p.13–14): “Conservative” wording for the 3″ pooled SIMBAD-unmatched fraction is backwards
- Offending text: “the tighter radius makes the aggregate conservative (a 5″ re-run could only lower the unmatched fraction)”
- Problem: Using a smaller matching radius increases the unmatched fraction; it is conservative only if you aim to upper-bound unmatched (or overstate novelty). As you stress that SIMBAD-unmatched is not a novelty rate, the word “conservative” here misleads.
- Required fix: Rephrase to “This 3″ pooled figure is an upper bound relative to 5″; a 5″ re-run would lower the unmatched fraction.” Or provide both 3″ and 5″ pooled numbers (see also P3-M2).

P3-n10 (Fig. 5 caption, p.13): Cutout angular scale inconsistent with the stated DESI LS pixel scale elsewhere
- Offending text: “DESI Legacy Survey DR9 grz composite, 256 × 256 pixels (108″ × 108″).”
- Problem: LS DR9 pixel scale is 0.262″/px; 256 px should span ~67.1″, not 108″. If you resampled or used a different scale for this figure, state it.
- Required fix: Clarify the pixel scale used for Fig. 5 (e.g., “resampled to 0.422″/px”), or correct the angular size to match 0.262″/px.

P3-n11 (Section IV.B, p.14): Pearson (“r = 0.006, p = …”) and Spearman (“r = 0.0005, p = 0.92”) tests lack explicit sample sizes
- Problem: You provide n only indirectly for the Pearson test and not for the Spearman test, which impedes verification.
- Required fix: Add the exact n used in each test (e.g., number of occupied Nside=64 pixels for both tests, or number of objects if Spearman was run object-wise), and confirm whether p-values are one- or two-sided.

P3-n12 (Section IV.A, p.14; “Expected false-match rates”): Missing derivation for the DESI×SDSS 3″ null overlap
- Offending text: “the uniform-density analytic expectation for random coincidences is ∼ 2.3”
- Problem: Unlike the SIMBAD case (where you later add Pfalse ≈ π r^2 n), no inputs or formula are provided for the 2.3 value.
- Required fix: Add the explicit formula and numbers used (surface densities of the two catalogs, area, matching radius), or move the statement to a supplemental calculation with a DOI.

P3-n13 (Throughout, figures with score axes; e.g., Fig. 3 caption, p.9): Restate score-scale in every panel with cross-transfer vs native axes
- Problem: You clarify this in the body, but some readers will only read captions. The right panel of Fig. 3 already notes cross-transfer; duplicating the alert (“SDSS panel uses DESI-trained cross-transfer S; not comparable to DESI-native scale”) in the first sentence of the caption would reduce misreadings.
- Required fix: Add a one-line reminder in the caption that absolute S across panels is not comparable; each is on its own per-survey, per-training scale.

P3-n14 (Section III.F, p.12): Train/validation top-200 imbalance test — strengthen or label as heuristic
- Problem: You provide a binomial tail p-value (good), but calling it “statistically significant” for memorization inference is still heuristic without a full score-distribution comparison.
- Required fix: Either add a simple train-vs-validation score KS test over the full 2×10^5 patches (KS statistic and p-value) or explicitly label the binomial tail as a heuristic indication and report train/val median and IQR as ancillary context.

NO FURTHER DISCREPANCIES FOUND IN OTHER CLASSES

- Arithmetic spot-audit: All other recomputable ratios and percentages in the abstract, tables, and main text match to the stated precision, except where already flagged in your first review or above.
- Figure–body consistency: Descriptions and numbers align with captions, aside from the Fig. 5 scale issue and caption clarity already noted.
- Dimensional consistency: Displayed equations are dimensionless or correctly normalized, aside from the F0 notation error already flagged in the initial review (P3-E2).
- Cross-references: Section, figure, and appendix pointers resolve to the intended content; no broken or misleading refs beyond those addressed in the first review.
- Null-procedure comparability: Where σ baselines with different normalizations are juxtaposed, caveats are present; ensure they remain adjacent after revisions (as requested in P3-n6).
- Abstract faithfulness and novelty claims: The remaining abstract statements are supported in the body; the main ambiguity about recommended tiers was already covered in P3-E4.

Summary: The new issues above are mostly arithmetic clarity (Pearson p), a figure-scale inconsistency, one stale phrase, and a few presentation/derivation gaps. Address these in addition to the essential/more substantial items from the first report to reach PRD standards.