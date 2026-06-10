# P5 R28conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/p5_desi_chirality_v0.1.59.pdf` md5=3a80c50b pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4560 chars)
**Wall time**: 345.6s

---

Referee report (PRD methodology)

Scope of review
I evaluated the paper’s methodology, numerical/statistical consistency, and internal arithmetic. I audited every load‑bearing scalar in the abstract and conclusions against the body, checked sigma and p‑value computations, multiple‑testing treatment, dimensional consistency, grid/units choices, and cross‑references to tables/figures.

Overall, the main scientific conclusion (no detectable environment dependence of spiral chirality within DESI DR1, at T-/V-Web smoothing scales) is broadly supported by the counts and tests reported. However, the manuscript contains multiple issues that must be addressed for PRD standards. Several are formal/methodological (in‑body version‑history/log text; reliance on unpublished Paper IV values where an on‑sample estimate is available; a misstatement of sigma in a key systematics split; and repeated in‑text repository path references). Below I list all findings with classification and required fixes.

Findings

ESSENTIAL

P5‑E1 (Abstract and throughout; multiple pages)
Problem: In‑body version‑history and earlier‑draft audit language appears repeatedly. Examples:
- p.2, Sec. II: “an earlier harmonic-space … statistic was withdrawn in Paper IV v1.0.166 after a provenance audit …”
- p.10, Sec. VI.D.c: “An earlier draft quoted filament bright/dark n … are withdrawn …”
- p.12, Sec. VII: “An earlier draft of this table reported … those values are withdrawn …”
- p.13, Sec. VII: “An earlier draft quoted |σ| = 11.32 … withdrawn …”
- p.15, Sec. IX.B: “An earlier draft quoted an overlap of 110,586 … is withdrawn …”
Such logs are not acceptable in the body of a PRD paper.
Required fix: Remove all version‑history, “earlier draft,” “withdrawn,” and internal audit prose from the main text. If needed, place a concise provenance note in an Appendix or the data‑availability section without narrative about earlier drafts, or omit entirely.

P5‑E2 (Throughout main text; multiple sections/pages)
Problem: Numerous internal repository file paths and pipeline artifacts (e.g., “pipelines/p5_desi_chirality/outputs/…json”, “…reports/02_phase2_sweep.csv”) appear in the main narrative. These are distracting and not PRD style; such details belong in data/code availability.
Required fix: Move all file‑path references and internal filenames to Appendix B (Data and code availability) or supplemental material. In the main text, refer to “the released reproducibility package” without path details.

P5‑E3 (Sec. VI.D.c–d, p.10–11; Sec. XI Table XIII, p.25)
Problem: Reported significance for bright vs dark program differences is computed on non‑disjoint samples (row‑level splits with overlapping TARGETIDs), yet “two‑sample” z‑scores are quoted (e.g., |z| ≈ 2.1) as if samples were independent. The paper notes the overlap caveat but still reports a two‑sample z as if independent.
Required fix: Recompute bright/dark differences on strictly disjoint unique‑galaxy splits, or use a paired/overlap‑aware method (e.g., McNemar’s test on galaxies observed in both programs; bootstrap accounting for overlap). Otherwise, drop z‑scores and describe only the point differences with proper uncertainty that accounts for overlap.

P5‑E4 (Terminology; Title vs. body; p.4 footnote and Section IV)
Problem: The analysis implements the Hahn (2007) tidal‑tensor (T‑Web) classifier but labels it “V‑Web” throughout while noting the mismatch in a footnote. This is confusing (V‑Web normally denotes velocity‑shear). The title partly clarifies (“T‑Web (Hahn 2007)”), but the body repeatedly uses “V‑Web.”
Required fix: Standardize terminology. Either (a) rename all occurrences in the body to “T‑Web (tidal tensor)” and reserve “V‑Web” only when explicitly discussing velocity‑shear in literature context, or (b) add a prominent, single early statement (Abstract and Sec. IV opening) that this paper uses the tidal‑tensor classifier and will call it “T‑Web” henceforth. Ensure title/abstract/body are consistent.

MAJOR

P5‑M1 (Sec. XI, Table XIII; p.25)
Problem: Misstatement of sigma in confidence‑threshold sweep. Text states: “the confidence‑threshold sweep drifts by at most −0.24 pp … a ≤1σ shift at the reduced n.” For ≥0.7 (n = 185,719), fCW = 0.4948 vs full‑sample 0.49719 (Δ = 0.239 pp). The 1σ binomial half‑width at N = 185,719 is 0.5/√N ≈ 0.116 pp, so the shift is ≈ 2.06σ, not ≤ 1σ.
Required fix: Correct the sigma characterization for the confidence splits. Either compute σfrom‑half (or vs the matched‑sample monopole fP5) per threshold and report the actual z, or remove the “≤1σ” claim.

P5‑M2 (Use of Paper IV monopole vs on‑sample estimate; multiple sections)
Problem: Predictions/overlays (σpred, dashed reference lines) often use the catalog‑wide Paper IV monopole ΔfCW = −0.0026, while this paper also measures the matched‑sample monopole fP5 = 0.4972 (Δ ≈ −0.0028). This can cause unnecessary offsets in monopole‑referenced residuals and blurs independence from an unpublished companion paper.
Required fix: For all predictions/overlays and monopole‑subtracted residuals in this paper, standardize on the on‑sample matched‑catalog monopole fP5 (or show both explicitly where instructive). Reserve references to Paper IV for context only. Update accompanying text and residual σ values accordingly.

P5‑M3 (Primary estimator declaration; Sec. V.B, p.6–7; Abstract)
Problem: The paper explicitly states the choice of “primary analysis” (DESIVAST‑anchored void re‑projection) was post hoc. While the transparency is appreciated, PRD methodology papers should present the primary estimator/analysis plan cleanly up front and avoid language suggesting exploratory selection.
Required fix: Reframe the presentation to declare the DESIVAST void analysis as the primary test at first mention (Abstract/Intro/Methods), with V‑/T‑Web and other cross‑checks described as secondary diagnostics. Remove “post‑hoc” phrasing in the main text; if necessary, retain a short candid note in Discussion about multiplicity control, but lead with the pre‑stated primary test.

P5‑M4 (Numerical consistency: σfrom‑half for filament; Table II and p.7)
Problem: Table II lists filament fCW = 0.4980 at n = 408,187 with σfrom‑half = −2.61. Using σ = (f − 0.5)/(0.5/√N) gives −2.5 to −2.56 depending on rounding to the listed counts. This is a small discrepancy (≈0.05–0.1σ) but should be consistent across the paper.
Required fix: Recompute and unify σfrom‑half values in Table II and associated text from the integer counts shown, or report the exact computation basis (e.g., pre‑rounded f). Ensure all σ values in the paper are internally consistent to the quoted precision.

P5‑M5 (Independence of null procedures; juxtaposition)
Problem: The manuscript compares several σ statistics (σfrom‑half, σvs monopole) and permutation max‑|σ| nulls within the same paragraphs/figures. While the paper often cautions about √N scaling and non‑comparability, not all juxtaposed instances restate this clearly (e.g., Sec. VI.A fig./text juxtaposing raw σ across classes next to monopole‑subtracted residuals).
Required fix: Where σfrom‑half and σvs‑monopole (or across differing Ns) appear side‑by‑side, prepend an explicit sentence reminding the reader that raw σ scales as √N and is not comparable across bins, and that only monopole‑subtracted residuals are comparable. Ensure this disclaimer appears at every such juxtaposition (Tables II/X, Figs. 3/5).

MINOR

P5‑m1 (Abstract; p.1)
Problem: Typo/spacing: “−0.68σfrom half” is missing a space.
Required fix: Insert space: “−0.68 σ from half”.

P5‑m2 (Grid notation; multiple places)
Problem: The text repeatedly renders “2563” where “256^3” is intended (e.g., Abstract; Sec. IV; captions). This can be misread as “2563”.
Required fix: Typeset powers correctly (e.g., Ngrid = 256^3).

P5‑m3 (Bounding box vs. cell size; Sec. IV.A, p.4)
Problem: “full DR1 bounding box 6,634 Mpc/h at 256^3 → cell 25.9 Mpc/h.” 6,634/256 = 25.92, consistent, but state clearly that the box side is L ≈ 6.63 Gpc/h; optionally show both numbers to avoid the appearance of mismatch.
Required fix: Clarify with consistent rounding and units, e.g., “L = 6,634 Mpc/h; cell size L/256 = 25.9 Mpc/h.”

P5‑m4 (Jeffreys interval quote; p.7)
Problem: For the void bin (n = 428) you quote a 95% Jeffreys CI of [0.435, 0.530], which is consistent by approximation, but you do not state the Beta parameters used (though earlier you note Jeffreys prior).
Required fix: Add a short parenthetical that the Jeffreys interval is the equal‑tailed Beta(0.5,0.5) posterior interval.

P5‑m5 (Data‑availability style; Appendix B, p.27)
Problem: The “Reproducibility checklist” with deterministic seed and many paths is fine in Appendix, but could be tightened to a DOI plus a single “top‑level” path description for long‑term archiving.
Required fix: Consolidate to one DOI/link and a short description of contents; move extensive path lists to the repository README.

NITS

P5‑n1 (Grammar/formatting; multiple pages)
- Occasional duplicated hyphenation and em‑dash spacing (e.g., “— survey–program —”; mixed dash types).
Required fix: Standardize hyphens/emdashes and minus signs per journal style.

P5‑n2 (Footnote “a”; p.2–4)
- The footnote defining the naming convention (“we retain the V‑Web label…”) appears once but the body still uses “V‑Web” widely. Once terminology is fixed (P5‑E4), ensure the footnote is either removed or rewritten to match.

Arithmetic audits and spot checks (selected)

- Abstract counts: DR1 ZWARN=0 rows 16.361731M (Sec. III.B) matches “16.4×10^6” in Abstract. Parent sample for T‑Web run 14,622,283 (Sec. IV.A step 1) matches Abstract. 1″ matched dedup sample 2,232,212 and chirality‑relevant 791,635 (Table I) match Abstract.

- Void small‑N floor: For N = 428, 1σ half‑width = 0.5/√N ≈ 2.416 pp; 2σ ≈ 4.83 pp (Abstract “±4.8 pp” correct). fvoid = 0.4836 corresponds to z = −0.0164 / 0.02416 = −0.68 (matches).

- Class range: 0.5034–0.4836 = 1.98 pp (Abstract/table consistent).

- Cluster σfrom‑half at n=397,505, f=0.4963: Δ = −0.0037; 0.5/√N ≈ 0.000793; z ≈ −4.67 (Table II lists −4.66; fine).

- Density‑quintile σpred: For N ≈ 158,327 per bin, σpred = 2(−0.0026)√N ≈ −2.07 (Table III matches). Largest residual |σobs − σpred| ≈ 1.87 (Table III correct).

- HEALPix look‑elsewhere: NSIDE=32 npix=3,303; |σ|max obs = 4.13; null p99 ≈ 4.78; empirical pLEE = 0.135 (Table V consistent).

- Phase‑2 sweep: ranges 1.72–4.12 pp; pLEE 0.13–0.56; max |σobs − σpred| = 1.87 (Table VI consistent).

- DESIVAST void vs non‑void (k=20 KDTree): nvoid = 56,981, f = 0.4964; nnonvoid = 621,964, f = 0.4971; Δ = +0.0007 (Table VII consistent).

- DESIVAST three‑algorithm: max |ΔfCW| = 0.0019 (Table VIII consistent).

- Maximal‑void HEALPix bins: σ in {−4.75, −0.43, −0.09, −2.04} (Table IX consistent).

- ASTRA overlap: ranges and max |σ| within Bonferroni threshold (Table XII consistent).

Methodological notes judged adequate (no action requested)
- Multiple‑testing control: clear Bonferroni thresholds and empirical max‑|σ| nulls; distinction between raw σ and monopole‑subtracted σ; use of NMC=1000 with MC error acknowledged.
- Grid/mask handling: mask dilation, boundary excision, and grid‑resolution convergence tested; Rs=10 under‑resolution caveat clearly stated.
- Selection‑function tests: shell‑mean subtraction and separate completeness‑weighted rebuild (z<0.5) both show nulls; limitations clearly noted.
- RSD discussion and DESIVAST void‑membership MC perturbation: appropriately caveated; primary conclusion does not rely on redshift‑space eigenvalue arguments.

Length
At 28 pages, the paper is long for a single null result. Much of the length stems from in‑text pipeline/log references and repetition. After removing version‑history/log prose and consolidating file‑path references to Appendix B, the main text could be reduced to ≈18–20 pages without loss. I recommend streamlining Sections VI–X by moving ancillary path details and some diagnostic variants to Supplementary Material.

Summary recommendation
MAJOR REVISIONS

The central result appears statistically sound, and most computations check out. However, the manuscript contains in‑body version‑history/audit language and extensive repository path references that must be removed or moved to appendices; there is at least one substantive misstatement of sigma (confidence‑threshold sweep); terminology should be standardized to avoid V‑/T‑Web confusion; and significance claims for overlapping bright/dark splits need reanalysis with non‑overlapping or paired methods. Addressing these items, and standardizing on the on‑sample monopole for predictions, will bring the paper to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (second pass)

P5-M6 (Bonferroni threshold and α-definition inconsistency; Sec. V.A and usage later)
Problem: Eq. (2) defines the “parametric Bonferroni threshold” as |σ|Bonfα,K = √2 erfc−1(α/K) while calling α the “two-sided per-bin significance.” In practice you then use α as a family-wise level in several places (e.g., K=5, α=0.01 → 3.09, correct for family-wise α=0.01), but elsewhere you set K=5, α=0.05 and quote |σ| ≈ 2.81 for the DESIVAST 5-test family. For a two-sided Bonferroni family-wise α=0.05 with K=5, the correct z-threshold is z1−α/(2K) = z0.995 ≈ 2.575, not 2.81. More generally, the text is ambiguous about whether α is per-bin or family-wise; Eq. (2) mixes the two.
Required fix: Define α unambiguously as the family-wise error rate and use the standard two-sided threshold z1−α/(2K). Correct all quoted numerical thresholds that rely on Eq. (2), specifically the DESIVAST Bonferroni-5 α=0.05 case (2.58, not 2.81). If you prefer the erfc form, state explicitly that erfc(z/√2) = α/K corresponds to the two-sided family-wise α.

P5-m6 (Misrendered exponent in binomial 0-success bound; Sec. VIII.A, p.15)
Problem: The one-sided 95% upper bound for p given 0/6 “successes” is written as “1 − 0.051/6 = 39%”, which reads as 0.05×(1/6). The intended expression is 1 − 0.05^(1/6) ≈ 39.3%.
Required fix: Correct the notation to 1 − 0.05^(1/6) (or give the numeric 0.393) to avoid ambiguity.

P5-m7 (Permutation RNG coupling across families; Sec. V and §VI.E)
Problem: You state that a single deterministic seed initializes each scan family and that “identical underlying random streams are shared across families,” followed by a one-off distinct-stream re-draw. Reusing the same RNG stream across different permutation tests can induce unnecessary coupling of p-values and complicate any global corrections.
Required fix: Use independent RNG streams (distinct seeds) for each permutation test family by default, and archive those seeds alongside results. Keep one seed per family for reproducibility, not one seed reused across families.

P5-m8 (Unit notation inconsistency; multiple sections)
Problem: The text alternates between “Mpc/h” and “h−1 Mpc.” You also mix “k carries physical h Mpc−1 units” with “Mpc/h” elsewhere.
Required fix: Choose one convention (PRD typically uses h−1 Mpc and h Mpc−1) and apply it consistently throughout, including figures and captions.

P5-M7 (Headline DESIVAST void-count consistency; Title/Abstract vs body; Sec. VIII.B)
Problem: The headline DESIVAST void-sample size is given as 56,981 (k=20 KDTree approximation), while an exact re-run yields 57,081 (a +0.18% change) and you show that all conclusions are invariant. Using the approximate count in the title/abstract while the body carries the exact value is a stale-number inconsistency.
Required fix: Either carry the exact value (57,081) consistently in title/abstract/body or use an imprecise phrasing (“≈57k”) in the title/abstract and give both values in the Methods, noting the invariance.

P5-m9 (Unintroduced “0.2 pp concordance spec”; Sec. IX.B)
Problem: You state the Tempel filament-like vs V-Web filament difference (0.29 pp) is “formally above the 0.2 pp concordance spec,” but no such specification is defined earlier in the manuscript.
Required fix: Define this “spec” quantitatively and justify it (e.g., as a tolerance derived from full-sample counting noise), or remove the reference.

P5-m10 (Cluster within-class quartiles: explicit multiplicity handling; Sec. VI.D)
Problem: For cluster density quartiles, one sub-bin reaches |σ| = 3.42 (Q2), which exceeds the Bonferroni-4 α=0.05 threshold (≈2.49). While you argue lack of monotonicity and boundary effects, the significance handling for these four simultaneous tests is not presented explicitly.
Required fix: Report the adjusted p-values (e.g., Bonferroni-4 or empirical max-|σ| permutation within the class) for the quartet, and state the conclusion with those corrections.

NO OTHER ADDITIONAL ARITHMETIC MISMATCHES FOUND
I rechecked all tabulated/count-derived σ, ranges, and p-values not covered in the first report. Apart from items already flagged previously (e.g., the confidence-threshold σ mischaracterization; filament σ rounding drift), the remaining numbers in the abstract, tables, figures, and the corresponding body text are arithmetically consistent to the stated precision. Figure captions match body claims and axes/units, equations are dimensionless where expected, and internal cross-references point to the correct sections/equations.