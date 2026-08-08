# P5 R55 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R55_P5/p5_desi_chirality.pdf` md5=b39a51ec pages=33
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6192 chars)
**Wall time**: 552.8s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with T‑Web (Hahn 2007) Tidal‑Tensor Cross‑Check Across the DR1 Matched‑Spiral Sample”

Scope of review
- Focus: methodological rigor, statistical validity, dimensional analysis, internal arithmetic consistency, null‑test design, error propagation, and traceability of all load‑bearing scalars in the abstract and conclusions.
- I read the full manuscript (33 pp), all figures/tables/equations/footnotes/appendices, and recomputed every headline number that can be derived from the printed counts.

Overall assessment
- The manuscript is unusually thorough in its statistical bookkeeping, multiple‑testing control, and reproducibility surface. Most numbers in the abstract are traceable to body tables with consistent arithmetic. The distinction between different σ statistics (σfrom half vs σvs monopole) is repeatedly and correctly flagged.
- Two items block full reproducibility from the PDF alone: (i) the selection‑corrected (z‑shell) T‑Web rerun is a load‑bearing robustness result but does not tabulate per‑class counts, making the stated χ2 = 0.11 (p = 0.99) uncheckable without downloading artifacts; and (ii) the data/code availability section advertises a DOI “accompanies submission” but does not give the DOI string. These require fixes before publication.
- Several smaller issues (unit notation consistency, scattered version‑history phrasing, one small Bonferroni threshold rounding, a stray footnote marker “a”) should be corrected.

Findings
ESSENTIAL (must fix before acceptance)
P5-E1. Section IX A (pp. 23–24): Missing per-class counts for the load‑bearing selection‑corrected T‑Web rerun
- Problem: The z‑shell selection‑corrected classifier is used to strengthen the headline (χ2 = 0.11, p = 0.99; cross‑class fCW range 0.05 pp), but the paper does not tabulate the corresponding per‑class n and nCW (only four n totals are given parenthetically: void 4,353; wall 154,541; filament 472,547; cluster 181,352; the nCW counts appear only later as a partial list in prose for three classes and cannot be verified from the PDF).
- Required fix: Add a table, analogous to Table III, for the selection‑corrected run: per-class n, nCW, fCW, σfrom half, and the 4×2 integer contingency table (like Appendix B, Table XVI) so that χ2 = 0.11, p = 0.99 can be recomputed from the PDF. If the interior‑buffer variant is quoted as “statistically indistinguishable,” provide its per‑class counts and 4×2 χ2 as well (or move to Supplemental Material with exact artifact pointer and frozen DOI).

P5-E2. Appendix C / Data availability (p. 31): DOI is promised but not provided
- Problem: The text states “A DOI‑minted archival snapshot of this directory accompanies journal submission” but no DOI string or landing page is given in the PDF.
- Required fix: Provide the permanent DOI (e.g., Zenodo) corresponding exactly to the frozen tag v0.1.83‑2026‑06‑19 (or the final camera‑ready tag), and ensure all artifact IDs [A1]–[A30] are reachable from that DOI snapshot. Include the exact commit/tag hash in the main text.

MAJOR (significant revisions required)
P5-M1. Section V A (pp. 6–7): Bonferroni threshold numerics and wording clarity
- Problem: Eq. (2) is correct, but one quoted threshold is slightly off: for NSIDE = 16 with K = 1054 and α = 0.05, zBonf ≈ z1−α/(2K) ≈ z0.999976 ≈ 4.01–4.03, whereas the text prints 4.05. This is minor numerically but symptomatic of mixing “per‑bin level α/K” with “two‑sided” language. Also, the later “Bonferroni‑9 at α = 0.05 gives 2.77” is low by ∼0.02–0.03 depending on the calculator; please standardize all thresholds to consistent precision.
- Required fix: Recompute and print all Bonferroni thresholds to two decimals with a single method (e.g., SciPy special.erfcinv), explicitly stating these are two‑sided family‑wise α thresholds. Confirm that all in‑text comparisons remain valid after the tiny numeric adjustments.

P5-M2. Section VI E / Table VI (p. 13): Deduplicated‑TARGETID permutation cross‑check not shown
- Problem: You correctly note that 3.56% of rows are repeats across program coadds and rerun the χ2 test on unique TARGETIDs. For the HEALPix label‑shuffle max‑|σ| pLEE, only the “free” and “leg×program‑stratified” shuffles are reported. A deduplicated‑TARGETID shuffle (labels permuted once per unique spiral and then broadcast to coadds) would complete the independence check for this permutation family.
- Required fix: Add a sentence reporting the NSIDE = 16/32/64 pLEE under a deduplicated‑TARGETID shuffle (or show that results are unchanged within one Monte‑Carlo SE). Artifact pointer acceptable, but print the three p‑values in the text.

P5-M3. Section X (pp. 26–27): ASTRA EDR per‑object variance model
- Problem: You correctly note the within‑object negative correlation of the four ASTRA class probabilities and validate the per‑class σ by Monte‑Carlo. However, the text currently states a per‑class variance ∑i P_i^2/4 “under the Bernoulli‑0.5 null,” which could be misread as exact when it is an approximation at the per‑class level only.
- Required fix: Rephrase to state explicitly that the analytic per‑class variance is an approximation ignoring within‑object negative covariances, validated by a 10^4‑draw Monte Carlo that reproduces the per‑class standard deviations to within 1.2%, and that joint cross‑class variance is not used for any inferential statement here.

P5-M4. Length vs. contribution (entire manuscript)
- Problem: The paper runs 33 pages for a single null result (environment‑independent fCW) with one primary estimator (DESIVAST void vs. non‑void contrast) and a large number of diagnostics. Much of Sections VI–X could be streamlined or moved to Supplemental Material without loss of scientific content.
- Required fix: Reduce the main text to ≤ 24–26 pages by moving (i) the full Phase‑2 9‑cell grid heat‑map details (retain headline numbers), (ii) the ASTRA EDR per‑object cross‑check figures/tables, and (iii) some of the HEALPix redraw diagnostics to Supplemental Material. Keep all load‑bearing counts and tests in the main paper.

MINOR (address before publication)
P5-m1. Units convention (pp. 5–6 and throughout)
- Problem: The manuscript alternates between “Mpc/h” and “h−1 Mpc.” You do explain the “multiply‑by‑h” convention in footnote 1 and state consistency with DESIVAST columns, but the mixed notation is distracting.
- Required fix: Standardize all distances to h−1 Mpc (or Mpc h−1) consistently across text, figures, and captions. Ensure Rs = 25 and cell size 25.9 are always labeled with the same convention.

P5-m2. Version‑history phrasing (multiple locations)
- Problem: The body contains phrases such as “earlier preprint versions used the ‘V‑Web’ label loosely,” and “an earlier preprint version cited 1,461/420/295, which were preliminary values.” PRD style disfavors version‑history narrative in the main text.
- Required fix: Move such statements to a brief footnote or remove. Keep the final algorithm nomenclature and counts; add a citation note if necessary.

P5-m3. Abstract footnote marker “a” (p. 1)
- Problem: In the abstract, “... (Hahn et al. 2007 [5]; Cautun et al. 2014 [7]) a on the full 14,622,283 ...” shows a dangling “a” before “on.”
- Required fix: Delete or correctly place the footnote marker.

P5-m4. Small rounding mismatches (scattered)
- Problem: A few σ values differ by 0.05–0.07 from back‑of‑envelope recomputation (e.g., cluster −4.66 vs. ≈ −4.72 by quick calculation). These are within rounding but readers will try to check.
- Required fix: Where space permits, show one more decimal or add a sentence noting that σ values are computed from exact counts and then rounded to two decimals; small hand‑recompute discrepancies are expected.

P5-m5. Clarify sign convention for ΔfCW in one place (p. 18, Table X caption)
- Problem: You state “The committed artifact stores the opposite‑signed fvoid − fnon‑void values.” This may confuse readers scanning the table.
- Required fix: Add a parenthetical in the caption: “Here we adopt ΔfCW ≡ fnon‑void − fvoid; artifacts tabulate (fvoid − fnon‑void).”

P5-m6. Provide explicit numbers for global Phase‑2 max‑statistic correction (p. 15)
- Problem: The text mentions “pglobal = 0.36 over all nine cells and 0.27 over the six resolved cells” in brackets. These are important for the robustness claim.
- Required fix: Move these pglobal values from brackets into the main sentence and reference [A14] as supporting artifact.

NITS (cosmetic)
P5-n1. Figure axes and legend consistency
- Fig. 6 and Fig. 8 colorbars: Add “σfrom half” explicitly to the bottom panels’ colorbar labels (you say σ in the caption; making it explicit on the colorbar aids standalone reading).
- Fig. 7: Add “pp” after the range numbers on the colorbar or in the title to indicate percentage points.

P5-n2. Minor grammar/typography
- Several em‑dash spacings and hyphenations (e.g., “Bonferroni‑5,” “per‑cell,” “null‑distribution”) vary. Standardize per journal style.
- Replace “sanity value” with “sanity check value” in footnote 1.

Arithmetic and consistency audit (selected checks)
- Table III: fCW values from n and nCW recompute to the printed decimals. σfrom half recomputes (void −0.68; wall +0.55; filament −2.61; cluster −4.66) within rounding.
- Abstract: “range across classes is 1.98 percentage points” matches 0.5034 − 0.4836 = 0.0198.
- Abstract: χ2 = 3.55, p = 0.31 matches contingency Table XVI tallies; the unique‑spiral recompute χ2 = 3.00, p = 0.39 is plausible given the small duplicate fraction.
- Eq. (1): σpred = 2 ΔfCW √N dimensionless and consistent. For filament N = 408,187, Δf = −0.0026 gives σpred ≈ −3.32 (matches text).
- Density‑quintile Table IV: With N ≈ 158,327 per quintile, σpred ≈ −2.07; residuals |σobs − σpred| match printed values to 0.01–0.02.
- Cluster density‑quartiles (Table V): subtracting σpred ≈ −1.64 for N ≈ 99,4xx yields residuals (−1.43, −1.78, +1.27, −0.82), as printed.
- DESIVAST void vs. non‑void (Table VIII): ΔfCW = 0.4971 − 0.4964 = +0.0007; two‑sample SE ≈ 0.00219; zΔ ≈ 0.31; p = 0.76; matches.
- V2‑REVOLVER catalog‑native (Sec. VIII D): nvoid = 104,912 vs nnon‑void = 40,877, Δ = −0.0037; SE ≈ 0.0029; |z| ≈ 1.25; p = 0.21; matches.
- Cramér’s V for class × program (Table XVII): √(χ2/n) = √(4933/811,609) = 0.078; matches.
- HEALPix max‑|σ| pLEE (Table VI): All > 0.05; consistent with the null and with the Bonferroni threshold magnitudes.

Abstract‑last drift sweep
- Every abstract scalar (N’s, fP5_CW = 0.49719; per‑class fCW; χ2 and p; Phase‑2 ranges and pLEE’s; DESIVAST void counts and ΔfCW; HEALPix correlations) is traceable to a table/figure or explicit body computation. The disclaimers about σfrom half scaling with √n and the catalog‑monopole subtraction are present in both abstract and body. No over‑claim detected.

Provenance surfaces
- The frozen tag v0.1.83‑2026‑06‑19 and deterministic seed are documented; however, the DOI is missing (ESSENTIAL). The artifact IDs are internally consistent with the narrative and appear to cover every quoted number.

Effect sizes
- Where χ2 is large only due to sample size (class × program), Cramér’s V is reported (0.078). For other omnibus tests, the effect sizes are essentially “range in pp,” which is appropriate given the null. This meets the requirement.

## Summary recommendation
MINOR REVISIONS

The analysis is careful and technically strong; most claims are supported and numerically consistent with the printed counts. The two essential fixes (publish the DOI for the frozen analysis snapshot and tabulate the selection‑corrected per‑class counts to make the χ2 = 0.11 result checkable from the PDF) are straightforward. A handful of major/minor presentation edits (clean Bonferroni numerics/wording, add a deduplicated‑TARGETID permutation p‑value, unify units/terminology, remove version‑history phrasing) will improve clarity. With these addressed, the manuscript meets PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL (must fix before acceptance)
P5-E3. Phase-2 sweep: missing per-cell class counts needed to verify “range within void-bin counting floor”
- Problem: Table VII lists, per (Rs, λth) cell, only the void-bin n and two summary statistics (max |σobs − σpred|, pLEE). The text’s core robustness statement for the sweep (“the per-cell range never exceeds 1.01× the void-bin 2σ counting floor,” and “every per-class residual ≤ 1.64σ in resolved cells”) is not checkable from the PDF because the wall/filament/cluster populations per cell are not printed.
- Required fix: Add a compact table (or move to Supplemental Material with a firm DOI) listing, for each of the 9 cells, the four class counts nclass and the four fCW (or nCW) so that: (i) the per-cell range claim can be recomputed; (ii) the per-class |σobs − σpred| maxima can be verified; and (iii) the “grid‑unresolved” rows can be cleanly excluded from any “max across cells” statements.

MAJOR (significant revisions required)
P5-M5. Ambiguous/misrendered Clopper–Pearson bound (0 successes in n = 6)
- Location: §VIII A, “0/6 T‑Web ‘void’ spirals … one‑sided 95% upper bound 1 − 0.051/6 = 39%.”
- Problem: The exponent is misrendered; as printed it reads like division (“0.051/6”). The standard bound is 1 − α^(1/n) with α = 0.05, i.e., 1 − 0.05^(1/6) ≈ 0.393.
- Required fix: Correct the notation to 1 − 0.05^(1/6) (and, if space allows, add a short parenthetical “= 39.3%”). This is both a clarity and a reproducibility issue.

P5-M6. Permutation RNG stream reuse across families not ideal; document or decouple
- Location: §V, “the same config‑level seed initializes each scan family’s generator, so identical underlying random streams are shared across families…”
- Problem: Sharing the same RNG stream across distinct permutation families is unconventional and can unintentionally correlate nominally independent robustness checks. While you show spot re‑draws that are “stream‑independent within MC SE,” the paper should either (a) use independent seeding per family, or (b) document the exact per‑family seeds and justify the reuse.
- Required fix: Either re‑run the permutation families with independent seeds (one per family; print the seeds in Appendix C) or add a short Methods paragraph documenting the per‑family seeds and an explicit cross‑family “same‑vs‑independent seed” comparison for one representative scan (numbers printed in text).

P5-M7. Weighted Pearson correlation not fully specified
- Location: §VIII F (per‑pixel correlation r, rw, ρ)
- Problem: The error‑weighted correlation rw is reported with “weights ∝ Npix” and “neff ≈ 683,” but the exact weighting, normalization, and p‑value calculation are not stated. Readers cannot reproduce rw or its p without the precise formula.
- Required fix: Add the explicit formula used for rw (e.g., rw = covw(X, Y)/[σw(X) σw(Y)] with w = Npix, and definitions of covw and σw), and state how p was computed (e.g., t‑approximation with dof = neff − 2 and the formula used for neff). Point to the artifact containing the per‑pixel triplets (Nvoids, σ, Nspirals).

P5-M8. Stray/broken internal cross-reference “sec:vweb”
- Location: §IV A, “Nomenclature reminder … the artifact filename [A3] and the sec:vweb cross‑reference label are retained…”
- Problem: “sec:vweb” appears to be a leftover label; there is no section by that name. This is confusing and looks like a broken cross‑reference.
- Required fix: Remove “sec:vweb” or replace with the correct section label (“T‑Web”) and ensure all in‑text cross‑references compile to existing sections.

MINOR (address before publication)
P5-m7. Define “pp” upon first use
- Problem: “percentage points (pp)” is used early and often; a one‑time parenthetical definition at first occurrence will help readers.
- Required fix: Add “percentage points (pp)” at the first mention.

P5-m8. Shamir-amplitude comparison would benefit from a quantitative class‑pair bound
- Location: §XII C
- Problem: You conclude there is “no room” for a 2–4 pp effect. This is true qualitatively, but the statement would be stronger with a numeric two‑sample 95% CI on the largest well‑populated T‑Web class contrast (e.g., filament vs cluster) to show an explicit upper bound (<1 pp).
- Required fix: Add the class‑pair two‑sample 95% CI (unique‑TARGETID version preferable) and note that it excludes 2–4 pp effects.

P5-m9. “Knot” vs “cluster” nomenclature toggles
- Problem: The paper alternates between “knot” (Cautun taxonomy) and “cluster.” While you note equivalence, the switching can confuse readers scanning different sections.
- Required fix: Pick one as the main term (e.g., “cluster”) and in the first occurrence add “(a.k.a. ‘knot’ in some T‑Web papers)”; use the chosen term consistently thereafter.

P5-m10. Unit-conversion footnote could be crisper
- Location: Footnote 1 (units)
- Problem: The multiply‑by‑h conversion is correct, but the prose conflates numeric conversion with unit labeling. Some readers routinely think in “divide‑by‑h” when going from h−1 Mpc to Mpc.
- Required fix: Add one clarifying sentence: “Astropy returns χ in Mpc; we multiply the numeric value by h and then interpret the resulting number as expressed in h−1 Mpc (so 843 Mpc → 570 h−1 Mpc at h = 0.6766).” This eliminates any ambiguity.

NITS (cosmetic)
P5-n3. Clarify figure labeling
- Fig. 6 and Fig. 8 bottom panels: label the colorbar “σfrom half” explicitly (you say it in captions).
- Fig. 7: add “pp” to the colorbar or title (“range of fCW across classes (pp)”) for stand‑alone clarity.

EXPLANATION
These items were not raised in my initial report and emerged from a second pass focused on hard reproducibility and editorial precision. The two most material new issues are (i) the absence of per‑cell class counts for the Phase‑2 sweep (needed to verify the “range vs floor” assertions), and (ii) the ambiguous Clopper–Pearson notation that currently reads like “division” rather than an exponent. The RNG‑stream reuse, weighted‑correlation specification, and stray cross‑reference are methodological/editorial gaps that are straightforward to fix and will improve clarity and reproducibility.