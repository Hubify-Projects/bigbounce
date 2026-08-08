# P5 RP5-INT-v97 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` md5=9b3aad7a pages=35
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6158 chars)
**Wall time**: 310.1s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three‑Algorithm Void Null Test on 56,981 DESI DR1 Spirals, with a Secondary Tidal‑Tensor Cross‑Check”

Scope of review
I evaluated statistical and methodological rigor, internal arithmetic consistency, dimensional analysis, and reproducibility. I recomputed all checkable scalars quoted in the abstract, conclusions, tables, and figure captions from the numbers provided; audited key equations; and examined how uncertainties and multiple testing are handled.

Overall assessment
This is a careful null-test paper. Most load‑bearing counts, fractions, σ’s, χ²’s and p‑values I could recompute from the given integers check out, including:
- Table II matched counts and separations;
- T‑Web class counts and σfrom half in Table IV;
- Bonferroni thresholds (Eq. 2);
- Monopole predictions σpred = 2Δf√N (Eq. 1) and monopole‑subtracted residuals;
- DESIVAST primary contrasts (Table IX, XI);
- Contingency tests (Appendix C) and Cramér’s V;
- Density‑quintile test and its residuals;
- HEALPix per‑pixel thresholds (Table VII) within MC precision.

The authors clearly differentiate their analytic z from permutation p wherever it matters, and they propagate the classifier‑monopole uncertainty at the right order of magnitude. The post‑hoc “primary path” designation is explicitly acknowledged and a Bonferroni‑5 family is enforced for the DESIVAST estimators. The RSD sensitivity of the DESIVAST membership test is reasonably bounded by a membership perturbation Monte Carlo.

That said, before the paper reaches PRD standards, several essential corrections and clarifications are required, primarily on reproducibility/dois, explicit per‑caption statistical‑comparability reminders, and a few quantitative clarifications.

Findings and required actions

ESSENTIAL

P5‑E1 (Appendix D/E; multiple pages)
Problem: No stable, citable DOIs are given for the code/data artifacts that are used throughout the paper as [A1]–[A30]. The text says “A DOI‑minted archival snapshot accompanies journal submission,” but no DOI is provided. The chirality catalog on HuggingFace is referenced by handle (bamfai/galaxy‑chirality‑catalog) without DOI; Paper IV (in preparation) is cited as the source for the catalog and monopole.
Required fix: Provide (i) a Zenodo/Dataverse (or equivalent) DOI for the exact commit/tag of the analysis repository (the tag v0.1.97‑2026‑06‑30 is not sufficient without a DOI); (ii) a DOI for the released chirality catalog used here; and (iii) archive the T‑Web environment tables and DESIVAST cross‑match outputs used here (with DOIs) or state precisely how to regenerate them, including config hashes and exact DR1 paths. Replace all “committed artifact” pointers in the body with a short citation to the DOI and move the long artifact map to the Data Availability section or an appendix.

P5‑E2 (Global; Figures 3, 5, 6, 7; Tables IV, VI, VIII, XII, XIII; Section V)
Problem: Different null procedures (analytic one‑sample σfrom half, monopole‑referenced σobs−σpred, and permutation pLEE) appear side‑by‑side. While Section V cautions that σfrom half is not comparable across bins of different N and distinguishes σpred from σfrom half, several figures/tables present σ and p together without an explicit, local reminder that the statistics are not directly comparable or are testing different nulls (e.g., Table VIII lists max |σobs−σpred| next to pLEE; Table IV lists σfrom half while the text soon after discusses σpred; Figure 6 shows a σ map while Table VII gives pixel‑level permutation p).
Required fix: Add one‑sentence reminders in each affected caption (and/or immediately under each table) that (a) σfrom half is an analytic one‑sample binomial z about p=0.5 and scales as √N, (b) σobs−σpred is a monopole‑referenced residual, and (c) pLEE is a permutation‑based look‑elsewhere p and is not directly comparable to σ values. This is a readability and misuse guard PRD requires.

P5‑E3 (Section VIII, page 18–19)
Problem: RSD Monte Carlo membership perturbation language is potentially confusing: “reassigns ∼ 4.4 × 10^4 hole‑union memberships per realization (the void count rises from 57,081 to 76,490 ± 161…)”. A net increase of ~19,400 void members is quoted, while the 44,000 figure implies total flips in+out. Without both in‑ and out‑flip counts, readers cannot reconcile “reassigns ~44k” with “+19.4k net.”
Required fix: Report both the number of in‑to‑out and out‑to‑in flips per realization (means and standard deviations), and the net change, so the 44k number is unambiguous. State the fraction of boundary galaxies affected (relative to both void and non‑void sets).

P5‑E4 (Appendix A; Section II)
Problem: The paper relies on Paper IV (in preparation) for the classifier and for ΔfP4CW = −0.0026. Appendix A substantially improves self‑containment, but the paper still uses an external number (ΔfP4CW) in Eq. (1) and several predictions. Although you also re‑measure fP5CW internally, the two values differ by ~8%.
Required fix: Explicitly use your internal matched‑sample monopole (fP5CW = 0.49719; ΔfP5CW ≈ −0.00281) for all predictions and σpred comparisons in the main text and figures, or present both (ΔfP4CW and ΔfP5CW) side‑by‑side wherever σpred is plotted/quoted, with a short statement that the conclusions are invariant to this ~8% difference and why. As is, some places use ΔfP4CW without showing the impact of switching to ΔfP5CW.

P5‑E5 (Data availability wording; Appendix D/E; throughout)
Problem: Extensive “internal pipeline” terminology and versioning (e.g., “committed artifact,” “driver,” “outputs/23…json,” “deterministic seed 20260515”) are woven into the main body (not just Data Availability), which obstructs scientific narrative and risks link rot if the reader cannot access the repo.
Required fix: Move all artifact‑path prose out of the main text and into a compact, citable Data/Code Availability section (plus Appendix E if desired). In the main text, keep only high‑level descriptions and DOI citations.

MAJOR

P5‑M1 (Section VII; Table VIII; grid‑unresolved cells)
Problem: The Rs = 10 Mpc/h cells are below the 25.9 Mpc/h grid resolution. While you state they are excluded from the robustness claim, they are still tabulated together with resolved cells.
Required fix: Either (a) move the three Rs = 10 rows to a separate table in the appendix with a boldface note “grid‑unresolved; not part of robustness claim,” or (b) gray‑shade them and add a caption sentence to ensure readers cannot accidentally interpret them as co‑equal evidence.

P5‑M2 (Section IX.A; selection‑corrected T‑Web)
Problem: The selection‑corrected classifier is an important diagnostic. However, the class counts and nCW are scattered in prose; there is no compact table akin to Table IV for the corrected labels, making reproduction more cumbersome.
Required fix: Add a one‑line table (like Table IV) for the selection‑corrected classes giving per‑class n, nCW, fCW, and σfrom half, so the stated χ² = 0.11 (p = 0.99) can be traced at a glance.

P5‑M3 (Section VI.A; “void cells vs. DESIVAST point‑in‑sphere”)
Problem: The text claims “only ≈ 0.1% of in‑footprint grid cells fall inside a DESIVAST VoidFinder sphere” but gives no number of cells to back this. Given the importance of this assertion to justify why the T‑Web void bin is tiny in the matched sample, a number is warranted.
Required fix: Provide the actual count of in‑footprint grid cells inside any hole sphere (and the corresponding percentage) and, if feasible, the fractional in‑mask volume those spheres subtend, using the stated 25.9 Mpc/h grid.

P5‑M4 (Appendix A; parity‑equivariance and accuracy)
Problem: Appendix A reports an “independent accuracy floor 69.91%” on a GZ1 cross‑match but does not give the class balance or how spirals were selected for that test; the generalizability to the DESI morphology regime is not discussed.
Required fix: State the positive/negative counts in the GZ1 test set used for accuracy/κ, the class balance, and the approximate redshift/magnitude range of that cross‑match. Clarify that this is a conservative lower bound and that the environmental analysis uses only the CW/CCW labels (NS excluded).

P5‑M5 (Length and focus)
Problem: At 35 pages for a null‑test with one primary estimand, the paper is longer than necessary. A significant fraction is pipeline provenance that belongs in Data Availability.
Required fix: Condense the main text to ~22–26 pages by moving pipeline details to appendices, tightening repeated explanatory passages (e.g., multiple retellings of the σpred vs σfrom half distinction), and consolidating robustness items. This improves readability and aligns with PRD expectations for a methods‑forward null test.

MINOR

P5‑m1 (Section IV.A, footnote 1; h‑conversion wording)
Problem: The statement “The incorrect divide‑by‑h operation… is not a valid alternative” is rhetorically strong. The math is correct (value[h⁻¹ Mpc] = h × value[Mpc]).
Required fix: Rephrase to neutral, e.g., “We adopt the conventional mapping value[h⁻¹ Mpc] = h × value[Mpc]; using value[Mpc]/h would be inconsistent with this unit definition.”

P5‑m2 (Tables and captions; units and notation)
Problem: Some captions use “pp” without first expansion; some axis labels show σ without “dimensionless.”
Required fix: On first use in each figure/table: expand “pp” to “percentage points” and note “σ (dimensionless).”

P5‑m3 (Section VI.D; cluster/filament overlap in ρ̄)
Problem: The helpful observation “cluster Q1 is less dense than filament Q4” is stated but not visualized.
Required fix: Add a small inset figure or explicit numerical min–max ranges of ρ̄ per quartile to demonstrate the overlap (acceptable to move to supplementary).

P5‑m4 (Section VIII.E; HEALPix footprint proxy)
Problem: You correctly caution that “0 maximal voids per pixel” is a proxy for being outside the DESIVAST coverage. But the main message hinges on it.
Required fix: Retain your new footprint‑restricted control (now in Table IX) and add one sentence in the main text, just before Table XII, pointing to that control as confirmation that the −4.75σ signal is outside‑footprint.

P5‑m5 (Typographical nits)
- A few occurrences of “σfrom half” are run together; add thin space or format consistently.
- Ensure consistent hyphenation of “per‑class,” “per‑pixel,” and “point‑in‑sphere.”
- Fix trivial punctuation spacing around en‑dashes in several places.

NIT

P5‑n1 (Section III.D)
Phrase “The 6.6‑mas median is far below any independent‑astrometry match precision” could be tightened (“far below typical independent‑astrometry precision”). No action strictly required.

P5‑n2 (Section XII.B)
The “toy EFT mapping” is clearly caveated; consider moving to supplement if space is needed. It is orthogonal to the empirical contribution.

Arithmetic spot‑checks (passed)
- Table IV σfrom half: recomputed values −0.68, +0.55, −2.61, −4.66 from provided integers — match.
- ΔfCW void vs non‑void (Table IX): 0.0007; SE ≈ 0.00219; z ≈ 0.31; p ≈ 0.76 — match.
- V2‑REVOLVER sphere PIS: nvoid=102,911; SE≈0.0017; z≈−1.12 — match.
- V2‑VIDE sphere PIS: SE≈0.0019; z≈−0.05 — match.
- V2‑REVOLVER GALZONE: SE≈0.0029; z≈−1.25 — essentially match.
- Cramér’s V = sqrt(4933/811,609) ≈ 0.078 — match.
- Density quintiles: σpred = 2(−0.0026)√158,327 ≈ −2.07; largest |σobs − σpred| ≈ 1.87; Bonferroni‑5 threshold at α=0.01 ≈ 3.09 — consistent.
- HEALPix NSIDE=16 threshold (two‑sided, K=1054): ≈ 4.07 — match.
- Void‑bin counting floor: 1/(2√428) ≈ 2.42 pp — match to 2.4 pp quoted.

Abstract–body consistency (passed)
Every load‑bearing number in the abstract I could trace appears and is consistent in the body: total DR1 rows, T‑Web parent size, matched unique counts, void/non‑void n and Δf, per‑class fractions and σ, χ² and p values (both omnibus and Phase‑2 sweeps), and selection‑function/tracer‑program caveats.

Bibliography
- Check journal/years: ApJ 982 (2025) for DESIVAST; Planck 2018 A&A 641 A6; Tempel+2014 A&A 566 A1. ArXiv identifiers present. Acceptable.

Stand‑alone reader test
With Appendix A, the paper is nearly self‑contained for the labels and monopole. The remaining reproducibility gap is the absence of stable DOIs for the analysis artifacts and the use of an external (in‑preparation) monopole in some predictions without always showing the internal‑monopole alternative (addressed in P5‑E1/E4).

## Summary recommendation
MAJOR REVISIONS

The statistical methodology is sound and the arithmetic checks out. The primary result — a DESIVAST‑anchored, three‑algorithm, Bonferroni‑controlled null on environment‑dependent chirality — is well supported. However, PRD requires stronger, DOI‑anchored reproducibility and clearer local reminders wherever different null statistics are juxtaposed. A few quantitative clarifications (RSD flip counts; small missing counts; a compact table for the selection‑corrected classifier) and improved organization are also needed. With these addressed, the paper would meet PRD’s methodological rigor bar.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh‑eyes pass)

ESSENTIAL

P5‑E6 (Section VIII.A, Clopper–Pearson notation)
Problem: The one‑sided 95% upper bound for 0/6 successes is written as “1 − 0.051/6 = 39% (… 1 − α1/n)”. As typeset, this reads “0.05×(1/6)”, not α^(1/n).
Required fix: Correct the notation to 1 − α^(1/n) and show the numeric 1 − 0.05^(1/6) = 0.393. This avoids misinterpretation and matches the standard Clopper–Pearson formula.

MAJOR

P5‑M6 (Permutation tests and duplicate rows; Sections VI.A, VI.E, VII; Tables VII–VIII)
Problem: Several permutation‑based p values (HEALPix pLEE, Phase‑2 cell pLEE, density‑quintile scan) are computed on the 812,793 env‑labeled parent that contains 3.56% duplicate TARGETIDs. While you quantify a small design‑effect for Jeffreys intervals and redo the omnibus χ² on the unique‑spiral parent, you do not provide deduplicated permutation p’s. Duplicates violate the i.i.d. assumption underlying the permutation reference and can slightly reduce the effective sample size within pixels/cells.
Required fix: Recompute the HEALPix, density‑quintile, and Phase‑2 pLEE on the 783,820 unique‑TARGETID parent and report the paired p values (row‑level vs unique‑ID), or stratify by TARGETID and permute labels within duplicate blocks. Confirm that conclusions are unchanged.

P5‑M7 (RNG stream reuse across families; Section V)
Problem: You state “the same config‑level seed initializes each scan family’s generator, so identical underlying random streams are shared across families,” and show a distinct‑stream re‑draw for one scan. Using identical streams across multiple tests can accidentally correlate tails across families.
Required fix: Assign independent, recorded seeds per scan family (and per figure/table) and report them. Provide a second full set of permutation p’s with an independent seed schedule in the artifact (or as a supplementary table) to demonstrate stream‑robustness across all permutation‑based results, not only the HEALPix example.

P5‑M8 (Missing integers in DESIVAST tables; Table XI, §VIII.D)
Problem: Table XI (sphere‑PIS) and the catalog‑native GALZONE contrasts report nvoid and fCW but not the integer nCW (and nCCW). This inhibits exact arithmetic verification of σ and ∆f, and rounding in fCW can mask small but non‑negligible differences.
Required fix: Add nCW (and optionally nCCW) columns for each row in Table XI and for the catalog‑native rows in §VIII.D (or move all five contrasts into a single table with counts). This matches the verification standard used elsewhere (e.g., Tables IV, IX, XVII).

P5‑M9 (Abstract, Phase‑2 sweep includes grid‑unresolved cells)
Problem: The abstract quotes the Phase‑2 look‑elsewhere p range (0.13–0.56) and per‑cell fCW ranges without noting that the Rs = 10 Mpc/h cells are below the 25.9 Mpc/h grid scale and are excluded from the robustness claim in the body.
Required fix: Amend the abstract to state explicitly that Rs = 10 Mpc/h cells are grid‑unresolved and excluded from the robustness statement; optionally give the resolved‑cell p‑range (0.13–0.48) alongside the all‑cells range.

P5‑M10 (Selection‑corrected omnibus test on row‑level parent only; §IX.A)
Problem: For the selection‑corrected T‑Web labels you report χ² = 0.11 (p = 0.99) on the 812,793 env‑labeled parent, but do not repeat the unique‑TARGETID χ² check done for the canonical labels. Duplicates could, in principle, alter χ² even if modestly.
Required fix: Report the 4×2 homogeneity χ² and p on the 783,820 unique‑spiral subset for the selection‑corrected labels (and, if possible, after the interior‑buffer excision), mirroring the canonical analysis.

P5‑M11 (Sky‑proxy outside‑footprint assertion; §VIII.E, Table XII)
Problem: The interpretation that the −4.75σ bin (“0 maximal voids per pixel”) corresponds to outside DESIVAST coverage rests on a proxy. While you provide a sample‑level footprint‑restricted control for the void/non‑void contrast, you do not quantify how much of the 0‑void bin is truly outside the DESIVAST angular mask.
Required fix: Intersect the HEALPix pixels with an explicit DESIVAST angular mask (or the union of maximal‑void discs) and report the fraction of the “0‑void” pixels that fall outside the mask (by pixel count and by spiral count). This secures the attribution of the −4.75σ to outside‑coverage regions.

MINOR

P5‑m6 (Units/pp vs fraction; §VIII.C)
Problem: You compare |∆fCW| with the “nvoid counting floor 1/(2√n) ≈ 0.0016” without stating whether 0.0016 is a fraction (0.16%) or “percentage points.” Elsewhere “pp” denotes percentage‑points explicitly.
Required fix: Add “(fractional; 0.16 percentage points)” or similar to avoid unit ambiguity.

P5‑m7 (Terminology/typos; §VIII.D)
Problem: “per‑cap join values” and “caplocal zone indices” appear to be typos.
Required fix: Correct to “per‑capita” or simply “per‑catalog,” and “cap‑local” (or remove “cap”).

P5‑m8 (Definition of “confidence” in Table XVI)
Problem: The confidence‑threshold sweep lists “pmax_cls_eq ≥ …” but the text never explicitly defines this variable (e.g., the maximum of the equivariant CW/CCW posteriors from the ViT‑Small classifier).
Required fix: Define “confidence” precisely at first use in the main text (source, range, and whether it is the max posterior over {CW, CCW} after Z2 symmetrization).

P5‑m9 (Figure/abstract phrasing; §VIII.E and Abstract “entirely”)
Problem: The text says the catalog‑wide −5σ “is concentrated entirely in the ‘0 maximal voids per pixel’ bin” while Table XII shows the ≥6 bin also negative (−2.04σ).
Required fix: Soften to “concentrated in” or “dominated by,” or quantify the relative contribution (e.g., share of total χ contribution by bin).

RATIONALE
These issues were not covered in the initial review. They focus on (i) exact reproducibility of integer counts and permutation p‑values in the presence of duplicates; (ii) seed independence for all permutation families; (iii) precise notation and unit clarity; and (iv) small but important presentation clarifications (abstract scope, typos, and definitions). Addressing them will further align the manuscript with PRD’s rigor and reproducibility standards.