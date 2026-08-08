# P3 EXT20 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=62d7b294 pages=30
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5937 chars)
**Wall time**: 490.7s

---

Referee report on “Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches”

Scope and role
I reviewed the entire 30‑page manuscript and all figures, tables, equations, and numerical claims. I focused on methodology rigor: statistical validity, derivation chains, dimensional and arithmetic consistency, uncertainty propagation, comparability of σ/p-values across different nulls, and reproducibility.

Overall assessment
The paper assembles a very large multi-archive anomaly catalog and includes two cosmology-oriented methodological applications (an fNL multi-tracer forecast using anomaly-selected tracers; and a PTA spectral-index refit using NANOGrav’s KDE free-spectrum). The authors include many commendable caveats and internal checks. However, for PRD standards, several core methodology and reproducibility issues must be fixed. The presentation also mixes internal pipeline artifacts and ad hoc engineering gates with publishable scientific results. The cosmology parts require fuller derivations and sensitivity analyses.

Below I list findings classified by severity, each with an ID, page/section, problem, and required fix.

ESSENTIAL

P3-E1 (Data availability; p. 23, “Data availability”)
Problem: The section states “will be made public with the arXiv posting” and “A Zenodo DOI will be minted at submission and cited here in place of this sentence.” These are placeholders. Numerous internal file paths (e.g., pipelines/p3_anomaly_engine/…) and audit artifacts are referenced throughout the paper, but there is no frozen DOI and no commit hash pinned to a specific release tag that a referee can verify today.
Required fix: Provide working, public DOIs for (i) the full catalog (including the 7‑way 5″ dedup manifest and per-survey tables), (ii) the model weights, and (iii) the scripts that reproduce every quoted scalar used in the text (e.g., the Jaccard overlaps, injection–recovery curves, HEALPix χ2, dedup sensitivity sweep, PTA MCMC, Fisher code, etc.). Pin exact commit hashes/tags in the manuscript. Remove all “will be made public” language.

P3-E2 (Fisher-forecast mapping; §V, pp. 18–19; Summary §VII item 5)
Problem: The key mapping 1/σ2(fNL) = F0 + c α2 is used to produce the headline σ(fNL) = 8.14 central with an envelope [3.92, 8.98]. The manuscript only states “c = 0.0747 from the 5‑α refit of §VI D caveat (i)” without a self-contained derivation or enough detail to reproduce c. There is no explicit Fisher matrix, k‑range, redshift binning, volume, shot-noise model, tracer densities, or bias model specification. This mapping is load‑bearing for all fNL statements.
Required fix: Add a full, reproducible Fisher derivation in the main text or an appendix: specify the data vector, parameter vector, binning, k‑cuts, window/volume, bias model, number densities of each tracer per redshift bin, shot-noise treatment, and how α couples to the cross‑ and auto‑spectra; show the derivation of the positivity‑respecting form and the determination of c from first principles or a documented fit; deposit the code that computes c with a DOI. Report the sensitivity of σ(fNL) to kmax, binning, and the assumed α prior.

P3-E3 (Rates vs fixed-count tiers; Table I pp. 9–10; Abstract p. 1)
Problem: Table I mixes measured “Rate (%)” entries (e.g., DESI 0.87%) with predetermined fixed-count selections (Planck, Gaia, NEOWISE “1.00%”, eROSITA “0.03%”) in the same column. Although the caption attempts to qualify this, the main table layout still invites misinterpretation (and is reused textually in the Abstract and elsewhere).
Required fix: Separate fixed-count/fixed-percentile tiers into a different column or a separate table with an explicit “Predetermined fraction” label, and reserve “Rate (%)” only for data‑driven detection rates. In the abstract and main text, never present fixed-count fractions as rates. Add uncertainty bars for bona fide rates; add an explicit “not a measured rate” label where appropriate.

P3-E4 (Planck top-200 uses patches seen in training; §III F p. 12)
Problem: The released top‑200 Planck anomalies are selected from a bank that includes training patches (152/200 are in the training split). Publishing anomalies that the model has seen during training is not acceptable for a catalog claim without a held‑out test confirmation.
Required fix: Recompute the Planck top-200 on a strictly held‑out set (no training patches) and release that list. Alternatively, demonstrate that the ranking is unchanged by excluding all training patches (top‑200 overlap and rank correlations) and publish the held‑out list as the main tier. Update all numbers accordingly.

MAJOR

P3-M1 (KDE/Bayes-factor specification; Appendix E pp. 25–27; §V A pp. 19–20)
Problem: The Savage–Dickey Bayes factors BMB/free and BSMBHB/free are sensitive to tail densities of the γ posterior. The manuscript gives posterior means and ESS but omits the KDE kernel choice, bandwidth selection rule, and robustness checks that directly control the tail density at γ = 4.33. The quoted large factor BMB/SMBHB = 7.14 × 10^3 needs bandwidth sensitivity reporting.
Required fix: Specify the KDE kernel, bandwidth, and selection method; report the value of the posterior density at γ = 3.0 and 4.33 under at least two bandwidth choices (e.g., Scott/Silverman; ±25% bandwidth perturbations). Show that BMB/SMBHB is stable under reasonable bandwidth variation. Deposit the fitter and KDE code with a DOI.

P3-M2 (Scaler-fit leakage for tabular surveys; §II B pp. 3–5; §III G–H p. 12–13)
Problem: For eROSITA/NEOWISE/Gaia the per-feature scalers are fit on the full sample (including validation/tail), not on the training split. A robustness check is provided only for eROSITA; for NEOWISE and Gaia it is “queued,” yet their results are used in the headline catalog and figure/novelty tallies.
Required fix: Repeat the NEOWISE and Gaia training with scalers fit strictly on the training split and quantify tail churn (membership overlap, rank correlation, Jaccard at the 1% cut). Include these numbers in the main text. If churn exceeds 20% at the extreme tail, downgrade those tiers or re‑frame as exploratory.

P3-M3 (Unweighted MSE for spectra; §II B Eq. (1) pp. 4–5; §VI C p. 20)
Problem: The anomaly score uses unweighted MSE on standardized spectra. Without inverse-variance weighting, low‑S/N regions can dominate residuals. This choice is likely consequential for spectroscopic tails and is acknowledged but not quantified.
Required fix: Provide a subset analysis on DESI (and SDSS native) comparing the published unweighted score to an inverse‑variance‑weighted MSE on a few hundred thousand spectra: quantify top‑tail membership overlap (e.g., at S>5 or top‑1%), rank correlations, and arm-dominance changes. If materially different, discuss implications or adopt the noise‑weighted score.

P3-M4 (NEOWISE injection–recovery labeling; §III H p. 13; Fig. 10 p. 22)
Problem: The NEOWISE “100% PASS” injection–recovery is a mask-geometry QA that guarantees success by construction. In Fig. 10 it appears alongside true detector-sensitivity curves with the same PASS label, which is misleading.
Required fix: In Fig. 10, visually separate “mask geometry QA” from “detector sensitivity” tests (e.g., dashed gray box and legend) and remove the PASS label from NEOWISE or re‑label clearly as “Mask geometry check (not sensitivity).” Reflect this consistently in the caption and text.

P3-M5 (Use of training spectra in DESI scoring; §II B p. 5; §III A p. 6)
Problem: The final DESI catalog and S>5 threshold are computed on the full 22.5M including the 47k training spectra. While k‑fold stability is reported, a PRD methods paper should either exclude training spectra from the published top‑tail or document their presence precisely.
Required fix: Provide the count of DESI anomalies among the 47k training spectra that enter the S>5 set; supply their IDs so users can remove them; and/or recompute the headline DESI S>5 tail excluding training spectra to show negligible impact.

P3-M6 (Abstract/table novelty wording; Abstract p. 1; §IV A pp. 13–14)
Problem: The Abstract lists survey‑wise SIMBAD‑unmatched percentages and a DESI “genuine novelty fraction,” but mixing these in the same paragraph risks misinterpretation as comparable notions of novelty (though later caveated).
Required fix: In the Abstract, explicitly segregate the SIMBAD‑unmatched rates as “database‑coverage diagnostics” and present the 17.8% DESI figure as the only genuine novelty estimate, with its limitations. Repeat that the full‑catalog novelty rate is unmeasured.

P3-M7 (Planck training/test split and p‑value; §III F p. 12)
Problem: The “naive binomial p ≈ 4 × 10^−4” assumes independence across 10° × 10° tiles. Correlations and sky anisotropy likely invalidate the naive null.
Required fix: Replace the naive binomial with a permutation test that respects patch geometry (e.g., random split assignments preserving sky footprint) or remove the p‑value and simply report the training/validation counts without inference.

P3-M8 (Cross-survey dedup false‑match accounting; §IV C pp. 15–16)
Problem: The text states “expected random coincidence contribution is ≲10 across all survey pairs” without a derivation. This feeds directly into claims of low contamination in the 637 multi‑survey clusters.
Required fix: Provide the computation (pairwise surface densities, areas, matching radius; or a rotation/RA‑shift null) and deposit the script. Include uncertainties and show that the result is robust against footprint edges and density gradients.

P3-M9 (eROSITA axis irreproducibility; §III E pp. 11–12)
Problem: The paper retains eROSITA as a membership‑only tier (good), but Table IV still prints an IF raw score and the text discusses a production threshold 0.259 that is “irreproducible.” For a PRD methods paper this section must be simplified and made less dependent on internal pipeline lore.
Required fix: Move all discussion of the unrecoverable production axis to an appendix; in the main text state crisply that the eROSITA tier is a fixed top‑298 membership list derived from the BigAE latent with a separately trained IF cross‑check (report only reproducible quantities). Ensure no per-object, non‑reproducible SBigAE values appear in any released product.

MINOR

P3-n1 (Cramér’s V arithmetic display; §IV B p. 15)
Problem: The text prints “Cramér’s V = √(χ^2/(N(k−1))) = 376,713/(378,280 × 24,047) ≈ 0.0064” which mixes the pre‑sqrt fraction with the post‑sqrt value. χ^2/(N(k−1)) ≈ 4.15×10^−5; its square root is ≈ 0.00644.
Required fix: Correct the displayed intermediate to show the sqrt explicitly (e.g., “= √(376,713/(378,280 × 24,047)) = 0.0064”).

P3-n2 (Top‑200 Planck patch MSE units; §III F p. 12)
Problem: The MSE range [0.558, 0.621] is presented without stating that inputs are standardized patches (dimensionless).
Required fix: Add “dimensionless standardized patch MSE” in text or caption.

P3-n3 (Fig. 8 “display score (non‑catalog)” labels; p. 17)
Problem: These labels can be confused with the canonical catalog S. The caption clarifies, but the figure text is easy to misread.
Required fix: Change the on‑plot text to “display-only score (not catalog S)” or remove the numeric label.

P3-n4 (Aggregate SIMBAD unmatched 58.8% vs per‑survey 5″; §IV A pp. 13–14; Fig. 6 p. 14)
Problem: The pooled 58.8% is computed at 3″ while Table I per-survey uses 5″. The manuscript notes this, but an unaware reader could still compare them.
Required fix: Put the radius in the pooled figure title/subtitle and repeat the warning in the caption.

P3-n5 (Length and structure)
Problem: The main text is 30 pages and carries many internal pipeline file‑path references. The presentation would benefit from condensing the main claims and moving engineering details to a Supplement.
Required fix: Reduce the main text to <= 20 pages by moving internal audit artifacts, file paths, and long pipeline descriptions into an SI with a DOI.

NIT

P3-nt1 (Typos/formatting)
- Several “p” artifacts around square roots (e.g., “p χ2 p”) likely due to PDF symbol encoding. Standardize mathematical notation.
- Ensure consistent hyphenation of “cross‑transfer,” “re‑score,” “retrain,” and “Jaccard‑stability.”

Arithmetic spot-checks and consistency notes
- Abstract scale comparisons: 378,080/2,685 ≈ 140.8 (≈141×), 269,117/2,685 ≈ 100.2 (≈100×), 195,829/2,685 ≈ 72.9 (≈73×): correct; the manuscript appropriately caveats non‑like‑for‑like science‑class comparisons later.
- DESI science‑class recount: 2,468/190,015 ≈ 1.30% (as stated); SPECTYPE breakdown sums to 2,468: correct.
- SDSS native continuity slice fraction: 77,905/1,925,279 ≈ 4.05%: correct. Top‑1% = 19,253: correct rounding.
- LAMOST native top‑1%: 113,342/11,334,161 ≈ 1.00%: correct rounding.
- Dedup geometry: native sums to 388,493, minus 10,213 collapsed -> 378,280 unique; compression 10,213/388,493 ≈ 2.63%: consistent. 6‑way catalog‑grade = 269,317; minus 200 Planck patches = 269,117: consistent.
- SIMBAD random false-match at 5″ using n≈3×10^−5 arcsec^−2: P≈2.36×10^−3 per source: consistent with 0.24%.
- fNL mapping: F0 = 1/8.98^2 ≈ 0.01239; with α=0.19 and c=0.0747 yields σ≈8.14; envelope endpoints 3.92 and 8.98: correct.
- NANOGrav parameter shifts: (3.0−2.567)/0.382 ≈ 1.13σ; (4.33−2.567)/0.382 ≈ 4.62σ: consistent.

Scope and suitability for PRD
- The paper’s core contribution is an astronomical catalog plus internal QA. The cosmology‑methods elements (fNL Fisher mapping; PTA KDE refit) are interesting but currently presented at a summary level and rely on ad hoc gates and internal artifacts. For PRD, these parts need full derivations and public code/data deposits as specified above.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains substantial methodological work and careful self‑audits, but several items fall short of PRD standards: (i) missing DOIs/commit-pinned, reproducible materials for all load‑bearing results; (ii) incomplete derivation/specification of the fNL Fisher mapping used for the headline forecast; (iii) Planck anomaly selection includes training patches and must be recomputed on a held‑out set; (iv) insufficient KDE/Bayes-factor specification and sensitivity checks; (v) unresolved scaler‑fit leakage for NEOWISE/Gaia; and (vi) mixing fixed-count fractions with measured rates in Table I. Addressing the ESSENTIAL and MAJOR items above is required before the paper can be considered further for PRD. The remaining MINOR/NIT items can be handled during a revision pass.

---

## PASS 2 — self-critique findings (what initial review missed)

P3 — ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P3-E5 (Injection amplitude “5σ” definition; §II D Step 5 p. 6; §III F p. 12; Fig. 10 p. 22)
Problem: The injection–recovery gates hinge on a “5σ” amplitude, but the paper defines σ rigorously only for the Planck case (standardized patch units; Appendix footnote in Table VI). For spectral surveys (DESI/SDSS/LAMOST) and tabular catalogs (Gaia/NEOWISE/eROSITA), the notion of “local noise σ” used for planting continuum dips/emission lines or tabular perturbations is not specified (per-pixel vs per-wavelength-bin vs per-object; pre/post standardization; which variance estimator; whether inverse-variance spectral noise models were used). Because pass/fail gate calls rest on this σ, the results are not reproducible or interpretable across surveys.
Required fix: For each survey and plant family, define σ precisely (data space, estimator, units, pre/post transforms), state the detection threshold used for recovery (e.g., top-1% S within-survey or a fixed S cut), and deposit the injection scripts with a DOI. Add a table summarizing σ definitions across surveys to ensure gate comparability.

MAJOR

P3-M10 (Misuse of p-value under stratified sampling; §III A p. 6)
Problem: The score–SNR correlation is reported as Spearman ρ = −0.03 with p = 0.12 on a stratified subsample “deliberately log-uniform in SNR.” The quoted p-value assumes i.i.d. sampling under a null; it is invalid under the described stratified design (the text acknowledges this but still reports p).
Required fix: Remove the p-value or replace it with a permutation or design-based test appropriate for the stratified sample; report only the effect size (ρ) or recompute on a true random subsample.

P3-M11 (Per-arm residual metric inconsistency; §II B p. 5; §III B p. 8; Table VII p. 24)
Problem: The total anomaly score uses squared residuals (MSE), while per-arm sub-scores rB, rR, rZ use mean absolute residuals without z-scaling. Mixing L1 (per-arm) and L2 (total) metrics can bias “arm-dominance” classifications and their scientific interpretation (e.g., Z-dominant high‑z claims). There is no justification or ablation to show stability of arm-dominance to the choice of residual norm or per-arm normalization.
Required fix: Justify the choice (L1 vs L2) and demonstrate robustness: report overlap and rank correlations of arm-dominance classifications when using (i) per-arm MSE, (ii) per-arm robust-z scores. If materially different, adopt a consistent metric or clearly qualify arm-dominance conclusions.

P3-M12 (PTA model normalization/units; Appendix E Eq. (E1) pp. 25–26)
Problem: The power-law template for the KDE likelihood is given in log10 ρi form, but the paper does not define ρi (strain PSD? characteristic-strain power? timing-residual PSD), nor the units of A, fyr, fi, and Tobs in the specific normalization used (e.g., the 12π^2 factor depends on the PSD convention). Without explicit units/normalization, the mapping is not reproducible and the Bayes-factor densities at γ = 3.0 and 4.33 are ambiguous.
Required fix: Define ρi precisely (quantity and units), specify the PSD convention and A’s units, and show the derivation of Eq. (E1) from the standard timing-residual PSD. Include the exact values used for fyr and Tobs, and deposit the fitter with these definitions pinned.

MINOR

P3-m6 (Dedup radius inequality; §IV C p. 15)
Problem: The FoF audit reports “maximum pairwise separation is 4.999″ and zero clusters exceed the 5″ link length,” suggesting a strict “< 5″” merge criterion and/or rounding. The main text elsewhere describes a “5″” merge without stating whether it is < 5″ or ≤ 5″.
Required fix: State explicitly whether the dedup uses < 5.0″ or ≤ 5.0″ and confirm that the rounding does not exclude borderline pairs. If necessary, recompute with a ≤ test and report the sensitivity (expected to be negligible).

P3-m7 (NEOWISE polar-cap enrichment quantification; §III H p. 13)
Problem: The 3.9% polar-cap fraction is reported as 2.6× the uniform-sphere expectation (1.52%) without an uncertainty or significance. A simple binomial calculation (n = 436, p0 = 0.0152) suggests a highly significant excess.
Required fix: Add the binomial confidence interval for the observed fraction and a p-value for the enrichment (or a bootstrap with sky-density weights if available), and clarify that this is a geometry/scan artifact, not detector sensitivity.

P3-m8 (Survey-by-survey score-axis summary; §II B pp. 4–5; §III E–H pp. 11–13; Table I pp. 9–10)
Problem: Multiple score axes are used (canonical S, raw MSE for Planck, fixed top‑k for eROSITA, native vs cross-transfer S for SDSS/LAMOST). While discussed in prose, there is no single consolidated schema.
Required fix: Add a compact table summarizing, per survey: score axis, scaler provenance, training/validation split source, detection threshold type, and whether the released tier is a score-thresholded set or a fixed-k membership list.

NIT

P3-nt2 (Planck training/validation fraction significance language; §III F p. 12)
Problem: The “naive binomial p ≈ 4 × 10^−4” for the held-out over-representation is qualified as indicative, but a more neutral wording would avoid implying statistical significance given known spatial correlations.
Required fix: Remove the p-value (already requested at P3-M7) and keep the descriptive counts (152 train / 48 val), or label the p-value as “heuristic” and defer formal inference to a permutation that respects sky geometry.

Explanation
These items focus on missing or ambiguous definitions that affect gate decisions (P3‑E5), statistical testing under a non‑i.i.d. design (P3‑M10), metric consistency for arm‑dominance claims (P3‑M11), and explicit unit/normalization for the PTA likelihood (P3‑M12). Additional minors clarify implementation details and presentation. These were not covered in the initial review and materially improve reproducibility and interpretability.