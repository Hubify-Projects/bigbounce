# P4 RP4-INT-v200 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/chirality_catalog_paper.pdf` md5=a644743f pages=25
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7327 chars)
**Wall time**: 329.9s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (25 pp)

Scope of this review
I audited methodology rigor with an emphasis on:
- statistical validity and null definitions;
- internal numerical consistency (recomputing fractions, σ, p, and unit conversions);
- clarity and pre‑declaration of the primary estimator;
- treatment of look‑elsewhere and multiple nulls;
- completeness of reproducibility surfaces.

Overall assessment
The analysis is thorough and the statistical framing (distinct nulls; real‑space primary estimator; harmonic channel treated as diagnostic) is, in principle, defensible. Many headline numbers in the abstract and conclusions trace back to concrete calculations in the body and pass basic arithmetic checks. However, there are several essential issues that must be corrected prior to PRD acceptance: a wrong table cross‑reference in the abstract for a load‑bearing σ, forward‑looking reproducibility placeholders (no frozen DOI/commit), malformed URLs, a formatting error that fuses a numerical result with a footnote marker (“−18.1.34”), and a small but real internal inconsistency on the quoted block‑bootstrap z at NSIDE=8. In addition, the manuscript relies heavily on in‑text “artifact” filepaths; these must be moved to a proper data/supplement and the narrative streamlined. I list all findings below.

Findings

ESSENTIAL

P4‑E1 (Abstract, p.1)
Problem: Misreferenced table for a load‑bearing σ. The abstract states: “the 10^4‑permutation canonical unapodized row in Table III gives +7.93σ”. Table III is the global CW fraction; the +7.93σ MASTER value is in Table IV.
Required fix: Replace “Table III” with “Table IV” in the abstract and any other locations where this row is cited.

P4‑E2 (Appendix D, p.21; and Abstract p.1)
Problem: Inconsistent and malformed reporting of the block‑bootstrap exclusion z. The abstract: “z ≈ −18 under the adopted NSIDE = 8 block‑bootstrap error model.” Appendix D (main text) cites z ≈ −18.1; footnote 3 then gives z = −18.4 at NSIDE=8 (with a small block‑scale sweep). Additionally, the main text line reads “z ≈ −18.1.34” where “.34” are footnote markers (3 and 4) visually concatenated to the number.
Required fix: Choose a single canonical NSIDE and value for the headline exclusion (consistent with the abstract), report it once with its block‑scale sensitivity (e.g., NSIDE ∈ {4,8,16}), and correct the typesetting so the number is not fused with footnote markers (e.g., “z = −18.1; see footnotes 3–4”).

P4‑E3 (Data Availability, p.23–24)
Problem: Forward‑looking placeholders and missing frozen artifacts. The text promises a future Zenodo DOI and a future insertion (“…will be deposited at journal submission; … will be inserted here in place of this sentence…”). PRD requires a stable archival record at acceptance.
Required fix: Provide working, permanent DOIs (or equivalent) for: the catalog, code, and all primary artifacts used to produce the main results. Include exact version tags and a top‑level commit hash for the code and model. Remove all forward‑looking placeholder language.

P4‑E4 (Data Availability, p.24)
Problem: Malformed URLs due to embedded spaces/line breaks:
- “https://huggingface.co/datasets/bamfai/galaxy- chirality- catalog”
- “https://huggingface.co/bamfai/gala xy-chirality-v2”
Required fix: Replace with functional URLs (no spaces), e.g., “https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog” and “https://huggingface.co/bamfai/galaxy-chirality-v2”. Verify all external links resolve.

P4‑E5 (Abstract and §III B, p.1–3)
Problem: Misleading section cross‑reference for the low‑confidence‑tail systematic. The abstract cites “Secs. III B, IV C” in connection with the low‑confidence‑tail excess. Section III B is an estimator hierarchy, not the systematic analysis; the systematic is actually documented in §IV C and Appendix D/E.
Required fix: Update the abstract cross‑reference to the sections that actually analyze the low‑confidence tail (e.g., “Secs. IV C and Appendix D/E”).

P4‑E6 (Terminology, multiple locations)
Problem: Repeated use of “isotropic (pixel‑)permutation null” is potentially misleading: permuting per‑pixel Ap values over a fixed, patchy mask produces an exchangeable‑over‑mask null, not a rotationally isotropic sky in the strict sense.
Required fix: Rename consistently to “pixel‑permutation null (exchangeable across the in‑mask pixels)” wherever “isotropic” appears, or add a parenthetical clarification on first use that “isotropic” here refers to scrambling over the realized footprint, not a full‑sky rotationally invariant distribution.

MAJOR

P4‑M1 (Appendix C, p.20–21)
Problem: Look‑elsewhere significance reporting. The hemisphere scan reports “pLEE ≤ 10−4” with N=10,000 MC but does not state the realized k (number of null exceedances). With finite MC, the proper minimum is (k+1)/(N+1). Elsewhere the paper uses this convention explicitly.
Required fix: Report the exact (k+1)/(N+1) value and k for the hemisphere max‑statistic, or state it as an upper bound with that convention. Clarify that the bound is limited by N=10,000.

P4‑M2 (Global manuscript; many pages)
Problem: Heavy reliance on “artifact” filepaths in the main text (e.g., “pipelines/p2_chirality/outputs/…”) impedes readability and PRD style. These are valuable for reproducibility but should not clutter the narrative.
Required fix: Move detailed artifact pointers to a structured Supplementary Material or a README in the archived repository. Keep one consolidated “Reproducibility” table in the paper mapping each headline result to a single artifact or DOI.

P4‑M3 (Injection protocol, §VI B, p.14–16; Abstract p.1)
Problem: Two different axis‑draw conventions (θ‑uniform and area‑uniform) are used for injections. The text argues they agree within MC error, and quotes a “log‑interpolated 1.20%” A95 in one place and a bracket (1.0–1.5] % in others.
Required fix: Adopt a single, explicit axis‑draw convention for headline A50/A95 (area‑uniform is standard on S^2), and report a single best estimate (with MC uncertainty) for A50 and A95 in the body. The abstract may keep the bracket but should reference the body’s best estimate (e.g., “A95 = 1.20% (area‑uniform axes), bracketed by 1.0–1.5% on the tested grid”).

P4‑M4 (Length and presentation)
Problem: The paper is long (25 pages) for the stated (null) result and contains repeated disclaimers. Some content (e.g., extended mask fsky bookkeeping, extensive path listings) could be moved to Supplementary Material.
Required fix: Condense the main text to ~18–20 pages by relocating implementation details to a supplement and tightening repeated “not directly comparable” caveats to a single clearly demarcated boxed note referenced wherever needed.

MINOR

P4‑m1 (Table III, p.7)
Problem: Deviation values involve minor rounding mismatches (e.g., +28.72 vs recalculated ~+28.76 using displayed digits).
Required fix: State that deviations are computed from unrounded fractions (already noted) and ensure consistency across the table. Optionally round to one decimal.

P4‑m2 (Notation, multiple pages)
Problem: Typesetting of “C2 2◦ apodization” appears inconsistently as “C
2 2
◦”.
Required fix: Normalize to “C2 apodization with 2° length” throughout.

P4‑m3 (Appendix A, p.17–18)
Problem: The monopole‑subtraction example cites changes in C1 and z without quoting the corresponding null mean/σ after subtraction in the same sentence.
Required fix: Add the post‑subtraction null mean and σ alongside the data value so readers can reproduce the z change immediately.

P4‑m4 (Appendix D, p.21–22)
Problem: The leg‑fraction templates are declared nearly collinear with the constant, with a huge naive σ. This is explained, but the presentation would benefit from stating explicitly which basis (e.g., SVD‑orthogonalized nuisances) is used for the quoted dipole coefficient and its invariance.
Required fix: Add one sentence stating that the dipole estimate and uncertainty are invariant under SVD pseudoinverse / leg‑drop / Gram–Schmidt, with a pointer to the (now archived) artifact.

P4‑m5 (Abstract, p.1)
Problem: “1.7% reference amplitude … at z ≈ −18” would be clearer with the explicit mapping to Ap units in‑line.
Required fix: Append “(Aref = 0.034 in Ap units)” to the abstract clause for immediate clarity.

NITS

P4‑n1 (Typographic artifacts, passim)
Problem: Occasional hard hyphenation artifacts in PDF text (e.g., “ap￾parent”, “decon￾volution”) due to line breaking.
Required fix: Clean PDF hyphenation.

P4‑n2 (Claims of scale, p.2)
Problem: “to our knowledge, the largest …” is plausible (3.2M spirals vs CE‑ResNet’s ∼1.95M), but cite the exact CE‑ResNet chirality‑labeled count or rephrase as “larger than the ∼1.95M scale reported by CE‑ResNet”.
Required fix: Minor wording tweak.

P4‑n3 (AI tool usage note, p.24)
Problem: The “AI tool usage” declaration is fine but can be moved to a footnote or end note per journal style.
Required fix: Adjust placement to conform with PRD style.

Methodology and arithmetic checks (selected)
- Catalog counts and fractions (p.7): 1,592,107 CW, 1,609,053 CCW, 5,273,371 NS sum to 8,474,531; fCW = 1,592,107/3,201,160 = 0.497353; binomial σ ≈ 0.000279; dev from 0.5 ~ −9.47σ. Consistent.
- NSIDE=64 pixel area: 41,253 deg^2 / 49,152 ≈ 0.839 deg^2. Consistent with text “∼0.84 deg^2”.
- MASTER apodized ℓ=1 (Table IV): z = (24.74−1.93)/3.12 = 7.31; rank p = (5+1)/(10,000+1) = 6×10^-4. Consistent.
- Canonical unapodized ℓ=1 (Table IV): z ≈ (7.27−0.57)/0.84 ≈ 7.98; authors quote 7.93 (likely σ rounded to 0.845). Acceptable with rounding note.
- Monopole leakage (Table V): 1.6846/1.6961 = 0.9932 ⇒ 99.32%; residual z = (1.6961−1.6846)/0.0068 = 1.69. Consistent.
- Fisher floor (eq. 4): σ(A) = √(3/N) for N=3,201,160 gives 9.68×10^-4; 3σ ≈ 0.29%. Consistent.
- Injection A50/A95 (Table VI): The discrete probabilities and MC errors are consistent with text; abstract brackets are supported; the body’s “log‑interpolated 1.20%” should be adopted as the best estimate.

Statistical‑null discipline and comparability
The manuscript is unusually careful to separate null conventions and avoid direct comparability across channels. I verified that every major juxtaposition of σ values is accompanied by an explicit “not directly comparable” warning. Maintain this discipline after the required edits.

Effect‑size clarity
Real‑space effect sizes are reported as Ap or fCW deviations and dipole amplitude Adip; harmonic channel gives C1 values. This meets PRD expectations. Retain the Ap ↔ fCW conversion reminders near any amplitudes in the conclusions.

Standalone‑reader test
The paper is largely self‑contained, but the heavy use of path‑like artifact references makes the narrative harder to follow without repository access. Consolidate these into a Supplement/appendix table and streamline the main text, as noted above.

Recommended page length
The main text could be tightened to ∼18–20 pages without loss of scientific content by moving implementation detail (mask/apodization bookkeeping, numerous artifact path listings) to Supplementary Material.

## Summary recommendation
MAJOR REVISIONS

The scientific result (a null real‑space dipole with documented sensitivity and a quantified harmonic-systematics residual) appears sound and is backed by consistent arithmetic. However, the paper cannot be accepted in PRD in its present form due to (i) an incorrect table cross‑reference in the abstract for a key σ; (ii) inconsistent/malformed reporting of the block‑bootstrap exclusion z (including a typesetting error that fuses a number with footnote markers); (iii) missing frozen reproducibility artifacts (DOIs/commits) and malformed URLs; and (iv) presentation issues (terminology around “isotropic” permutation nulls; overuse of internal path references). Addressing the Essential and Major items above should bring the manuscript to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P4‑E7 (Training‑set augmentation arithmetic, §II.B, p.3)
Problem: The stated flip augmentation and the counts are inconsistent. Source images: 25,790. Held‑out validation: 5,323. That implies a pre‑augmentation training pool of 25,790 − 5,323 = 20,467 images. Yet the paper reports “post‑augmentation ntrain = 21,293” and a “combined pool 26,616,” i.e., only 826 extra images were created by “flip augmentation of the training split.” If all training images were horizontally flipped once, the training pool should roughly double (to ~40k), not increase by 826.
Required fix: Clarify exactly which subset was augmented and why only 826 images were added. Report the pre‑augmentation training count, the number actually augmented, and the final counts per class before/after augmentation. If only a subset was augmented by design, state the selection criterion and rationale. Ensure all numbers sum consistently.

P4‑E8 (Figure‑text mismatch on canonical MASTER σ, Fig. 8 vs. body; and stale σ values)
Problem: Fig. 8 embeds σℓ=1 = +3.63 in the caption/panel, but the body repeatedly cites +3.64 for the same canonical pre‑MASTER pseudo‑Cℓ result (and +3.64 appears in the abstract’s systematics paragraph). This is a small but recurrent inconsistency suggesting numbers were updated in one place but not the other.
Required fix: Harmonize the canonical pre‑MASTER ℓ=1 σ everywhere (figure panel annotation, caption, body). State one value (to two decimals if needed) computed from the same null run.

MAJOR

P4‑M5 (QC/reproducibility of flip‑probabilities; §B.d, p.19)
Problem: The paper reconstructs per‑galaxy flipped‑image probabilities from stored raw and TTA outputs via pflip = 2 peq − praw, and reports 2.9% of rows with out‑of‑range probabilities up to 0.09 because the “raw” columns sometimes come from a separate inference pass. Although a QC flag is provided, this leaves a 2.9% ambiguity in the flip leg for downstream users and for audit of T1–T7 tests.
Required fix: Archive and cite artifacts that include, for every galaxy, the same‑pass original and flipped softmax vectors used to compute peq (or re‑run inference to generate them) so that pflip is not reconstructed algebraically across mismatched runs. In the paper, explicitly state that the headline science results exclude the QC‑flagged rows and quantify the effect of excluding them on all headline estimators (not just the one dipole rerun presently shown).

P4‑M6 (Hemispheric scan uses two different direction grids and nulls; §IV.D, Table V vs. Appendix C)
Problem: Two hemisphere statistics are presented: (i) a 648‑direction 10° grid with a label‑shuffle null (max 3.05σ; pLEE ≤ 10−4), and (ii) a 768‑direction NSIDEdir=8 grid with a monopole‑only generative null (z=+4.42; Table V). The paper notes they are “not comparable,” but the dual presentation without a single canonical definition invites confusion.
Required fix: Pick one hemisphere scan definition and null as canonical in the body (recommend the label‑shuffle max‑stat with its direct‑MC LEE control), move the alternate grid/statistic to Supplementary Material, and add a one‑line rationale for why the canonical choice is the appropriate directional diagnostic for this dataset.

P4‑M7 (Random‑seed provenance for stochastic calibrations; multiple sections)
Problem: Several key results depend on Monte Carlo or permutation streams (e.g., 10,000 pixel‑permutation nulls; injection–recovery with 100/axis/amplitude; 500‑MC MASTER nulls). Only some explicitly state a seed (“seed 42” appears in places), others do not. This hampers exact reproducibility at acceptance time.
Required fix: For every stochastic computation that feeds a headline number (tables, figures, abstract), record the RNG family and seed(s) in the manuscript or a single “Reproducibility” table keyed to DOIs. Confirm the archived artifacts were produced with those seeds.

P4‑M8 (Training‑label composition transparency; §II.B, p.3)
Problem: The CE‑ResNet‑derived pseudo‑labels (66.5% of training labels) are described as “high‑confidence spiral classifications,” but it is not stated explicitly how many are CW vs. CCW (class balance) and whether any CE‑ResNet not‑spiral labels were used. Given the dependence of the monopole on training‑label priors, this matters.
Required fix: Report per‑class counts (CW/CCW/not‑spiral) for each training‑label source (GZ1, CE‑ResNet, synthetic negatives) before/after any filtering; state any thresholds used to select CE‑ResNet labels and whether CE‑ResNet not‑spiral outputs entered the training set.

MINOR

P4‑m6 (Arithmetic: equal‑count slab totals; §IV.B, p.7)
Observation: The seven equal‑spiral‑count slabs are stated as N = 457,308–457,309 each. Seven slabs at those counts span 3,201,156–3,201,163, consistent with the catalog total 3,201,160. This checks out but is worth clarifying with an explicit statement that the seven slabs exactly partition the spiral catalog (no remainder).
Required fix: Add a short clause confirming the seven slabs cover all Nspiral with no leftovers.

P4‑m7 (Symbols/diacritics; §VII, Fig. 9 caption)
Problem: Axis labels contain stray diacritics/hats (“axis yˆ, ˆzˆ”), likely LaTeX artifacts.
Required fix: Normalize to plain x, y, z (or ˆx, ˆy, ˆz consistently).

P4‑m8 (Equation label scoping; Appendix A captions “a., b., c.”)
Problem: Subsection labels appear as “a.”, “b.” within Appendix A, but are referenced in the body as “Appendix A, Table VIII” and “Appendix A.a”. Mixing styles (“A.a”) is non‑standard.
Required fix: Use consistent subsection labels and references (e.g., “Appendix A1, A2” or “Appendix A(a), A(b)”) throughout.

P4‑m9 (Class‑weight specification; §B.a, p.19)
Problem: The loss is “class‑weighted cross‑entropy” plus consistency term (Eq. B1), but the actual class weights are not stated. This is minor but relevant to reproducing the raw CW/CCW monopole.
Required fix: Report the three class weights used in LCE (or state they were uniform).

P4‑m10 (Acronym resolution on first use; multiple)
Problem: Some acronyms are used before expansion in the main text (e.g., “TTA” in Fig. 2 caption context).
Required fix: Ensure every acronym is expanded at first occurrence in the main text and figures.

NITS

P4‑n4 (Consistency of significant digits; §IV.C, null quantiles)
Problem: The pixel‑permutation null quantiles are given as {3.5, 4.4, 6.0, 6.8, 8.4}×10−3. Elsewhere, closely related numbers are quoted to three decimals. Minor presentation nit.
Required fix: Use a consistent rounding convention (e.g., three significant digits) for all null quantiles across the paper.

P4‑n5 (“θ‑uniform mildly over‑weights poles” wording; §VI.B)
Observation: The statement is correct mathematically; consider adding the one‑line derivation (area element ∝ sinθ) in a footnote to preempt reviewer confusion.

Reason for additional pass outcome
This fresh pass focused on places my initial review under‑checked: the training‑set arithmetic and augmentation semantics, flip‑probability reconstruction integrity, and subtle figure/body σ mismatches. These yielded new, concrete issues (P4‑E7, P4‑M5, P4‑E8) that affect clarity and reproducibility, plus several smaller presentation fixes. All earlier Essential/Major items remain applicable and are not repeated here.