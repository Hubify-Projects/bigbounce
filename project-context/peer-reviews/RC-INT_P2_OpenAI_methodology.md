# P2 RC-INT — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=5e23ad4c pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6940 chars)
**Wall time**: 310.2s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook” (29 pages)

Scope of review
I reviewed the full manuscript, including all equations, figures, tables, captions, appendix, and references. Below I list all methodological, statistical, arithmetic, and provenance issues found, with classification and concrete required fixes.

Findings

ESSENTIAL

P2-E1 (Data & Code Availability; p. 25–26, “DATA AND CODE AVAILABILITY”)
Problem: The section promises an archived Zenodo release but contains a placeholder: “DOI inserted at submission.” Numerous in‑text references to internal artifact filenames (e.g., c9g bf table recompute.py, c9i epsilon ratio check.json, phase3 bispectrum shape overlap.json) appear throughout the main text (pp. 4–5, 8–10, 12–17, 25–27) as load‑bearing provenance pointers, but no immutable release DOI or commit hash is provided. As written, the results are not reproducible to PRD standards.
Required fix: Provide a permanent DOI to a frozen archive (Zenodo/OSF) and a git commit hash matching the exact code/data used to produce all numbers in the paper. Move all filename-level artifact pointers from the main text to a consolidated “Supplemental Material / Code archive manifest” with checksums. The main text should reference only the DOI and a short manifest identifier.

P2-E2 (Estimator declaration and significance procedures; multiple pages)
Problem: The paper uses multiple “significance” constructs derived under different null procedures: (i) naive |fNL|/σlocal = 6.25σ (no template correction), (ii) template‑corrected 5.2–5.5σ, (iii) post‑systematic‑budget 2.6–5.5σ envelopes combining additive quadrature systematics, and (iv) single‑time‑ordering “stress‑test” 2.6σ (Table V). While many places note differences, there are instances where numbers from distinct null procedures are juxtaposed without an explicit “not directly comparable” qualifier at that immediate location (e.g., Sec. V, p. 11: “significance … 7.4–7.7σ … without template correction the naive significance is 8.75σ”).
Required fix: At every location where any pair of these σ values appear together, add the explicit phrase “not directly comparable” and state which numerator/denominator and which null/assumption set is used. Add a single table early in Sec. IV that enumerates each σ definition, its inputs, and the intended use. Make the headline a single recommended value (with a clearly delineated assumptions line), and keep other values as labeled sensitivity checks only.

P2-E3 (Main‑text reliance on internal file names for methodology; pp. 4–5, 8–10, 12–17)
Problem: The manuscript repeatedly cites internal filenames to support numerical claims (e.g., “artifact c9i epsilon ratio check.json,” “phase3 bispectrum shape overlap.json,” “null space analysis.py,” “c9j bf template rescale.py”). This is internal bookkeeping in the main text and does not meet PRD documentation style.
Required fix: Remove all internal filenames from the main text. Replace with references to (i) methods described in the paper, (ii) equations, and (iii) a supplemental methods/code-manifest table. Keep filenames exclusively in the Supplement/manifest.

P2-E4 (Bayes‑factor presentation and headline wording in the abstract; p. 1)
Problem: The abstract headlines “BF ≈ 9 (… σtheory = 1.0 Gaussian bounce prior, broad multifield [−15, +15]) up to BF ≈ 14 at the delta‑prior theoretical maximum,” then notes this is “evaluated under the noise‑weighted r ≈ 0.84 template‑mismatch bookkeeping.” In the body, Table II is the r → 1 endpoint, with the noise‑weighted “rebooking” discussed separately. This split invites confusion about which BF set is the actual primary result.
Required fix: In the abstract and the main text, present a single primary BF line keyed to the same bookkeeping used for the headline σ (i.e., with σeff = 0.7/0.84 if that is the baseline), explicitly stating priors and bookkeeping. Move all other endpoint values to a clearly marked sensitivity paragraph. Add a one‑line equation showing the exact σeff used in the abstract BF computation.

P2-E5 (Choice and calibration of σGR systematic; pp. 17–19, 20)
Problem: The σGR = 0.5 and 1.0 “stress‑test amplitude grid” is not calibrated to a SPHEREx‑like bispectrum Fisher or to the cited Addis et al. power‑spectrum study. Yet the lower endpoint 2.6–2.7σ critically depends on σGR = 1.0 and is labeled “realistic range” in several places (e.g., abstract p. 1; Sec. IV p. 10; Table IV p. 20).
Required fix: Re‑label the 2.6–2.7σ endpoint as “stress‑test lower bound under an additive‑quadrature GR‑nuisance of σGR ∈ [0.5,1.0], not calibrated by a SPHEREx bispectrum Fisher” everywhere it appears (abstract, Sec. IV, Table IV caption). Alternatively, supply a SPHEREx‑bispectrum relativistic‑projection Fisher/marginalization (or a literature‑anchored mapping) supporting σGR choices.

MAJOR

P2-M1 (Template‑overlap r: uncertainty summary; Sec. III.B pp. 8–10)
Problem: The noise‑weighted central r = 0.84 ± 0.02 is described as “spanning all physically motivated weighting schemes,” but only four concrete values are listed (0.829, 0.830, 0.835, 0.876), with the ±0.02 stated as “dominated by the noise‑weighted schemes.” This is not yet a transparent uncertainty summary.
Required fix: Add a small table listing each weighting scheme, its definition, and the corresponding r value with numerical integration settings. State clearly how ±0.02 is computed (e.g., half‑range over the LSS‑relevant schemes). Make explicit that the 0.876 CMB‑Fisher value is excluded from the ±0.02 band and why.

P2-M2 (Photo‑z outlier degradation claim; Sec. IV p. 11)
Problem: The statement “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼ 5% … from a first‑order Fisher correction … ∼ fcat^2/(1+fcat)^2 ≈ 0.008” is heuristic and not derived for the SPHEREx bispectrum estimator. No validation or literature pointer specific to bispectrum/photo‑z is given.
Required fix: Either (i) provide a derivation or simulation showing this 5% bispectrum degradation for a SPHEREx‑like sample (or a published citation), or (ii) move this to a clearly labeled conjectural note in the Discussion, and remove the 5% number from the consolidated budget language.

P2-M3 (Length vs. contribution)
Problem: The manuscript is a sensitivity recast (the core σ(fNL) = 0.7 baseline is imported from Heinrich et al.), but runs 29 pages with repeated caveat paragraphs and file‑name provenance in the main text.
Required fix: Condense to ≤18 pages by moving: (i) much of Sec. VI (Bayes‑factor algebra and multiple repetitions of endpoint wording) to Appendix; (ii) long null‑space basis and permutation‑group discussions to Appendix; (iii) code‑artifact mentions to Supplement.

P2-M4 (Equation clarity, Eq. (2); Sec. II.A p. 3)
Problem: “BNL = 10/3 ∑ AT / ∑ k_i^3” is ambiguous: what is being summed over in the numerator? (Permutations, operator pieces, or configurations?) The surrounding text implies the permutation sum, but this is not stated.
Required fix: Rewrite Eq. (2) as BNL(k1,k2,k3) = (10/3) AT(k1,k2,k3) / (k1^3 + k2^3 + k3^3) (if no sum in numerator) or explicitly index the sum if intended.

P2-M5 (MegaMapper section language; Sec. V p. 11)
Problem: The text mixes “template‑corrected ideal 7.4–7.7σ” with “without template correction the naive significance is 8.75σ” in one sentence without the “not directly comparable” qualifier mandated in this review’s instructions.
Required fix: Add the explicit qualifier at that location and throughout Sec. V where naive vs. template‑corrected numbers appear together.

P2-M6 (Use of internal algorithmic choices as apparent uncertainties; Sec. II pp. 4–5)
Problem: The “uniform ball of radius 50” in coefficient‑null‑space basis and uniform Euclidean measure are arbitrary. While the text acknowledges basis dependence, the r = 0.85 ± 0.13 percentile‑based propagation is used to state “conservative floors.”
Required fix: Move the percentile‑derived “floors” to Supplementary as a methodological sensitivity study; in the body, emphasize only the physics‑motivated r values and the LSS/CMB weightings. If retaining percentiles, explicitly state in the consolidated budget that null‑space scatter is not included in σeff and is not a defensible systematic.

P2-M7 (Provenance of Planck PR4 recast; Sec. VIII.A p. 20)
Problem: The recast of Planck PR4/NPIPE to bounce template uses r = 0.876 (CMB Fisher). This is fine, but the source and exact ℓ‑range/noise model used should be clearly stated. Currently only “fiducial Cℓ from CAMB with a Planck noise model; ℓref = 50–950” appears elsewhere in the paper.
Required fix: In Sec. VIII.A, specify the ℓ‑range, masks (if any), and exact noise model used for generating the CMB‑Fisher overlap r = 0.876, or add a pointer to a Supplement section with these details.

MINOR

P2-m1 (Arithmetic checks; multiple)
- 4.375/0.7 = 6.25 (naive). 0.83×6.25 = 5.1875, 0.876×6.25 = 5.475 → the stated 5.2–5.5σ is consistent.
- 4.375×0.84/√(0.7^2+1.0^2) = 3.01σ (consistent with “~3.0σ”).
- Combined σeff = √(0.9^2+1.0^2) = 1.345 → 4.375×0.84/1.345 = 2.73σ (consistent with “~2.7σ”).
- ns–fNL linearization: with ns = 0.9649 and c′ ∈ [0.7,10], fNL ∈ [−4.35, −4.02] matches the text.
No action required; consider adding a compact table of these arithmetic checks (optional).

P2-m2 (Typographical/format)
- A few occurrences of “dESI” (e.g., Ref. [34], [35] prose on p. 21) should be “DESI”.
- Several very long sentences impede readability; consider splitting for clarity.
Required fix: Correct “dESI” to “DESI”; minor copy‑editing.

P2-m3 (Figure/caption clarity)
- Fig. 2: The y‑axis implicitly denotes σ; add “Detection significance (σ)” as explicit label.
- Fig. 5: Ensure axes include units where relevant (none seem required beyond % on x in the left panel, but label “%” explicitly).
Required fix: Clarify axis labels.

P2-m4 (Reference consistency)
- Check that all arXiv IDs and years match the statements in prose (e.g., Addis et al. 2025 arXiv:2511.09466, Heinrich et al. 2024 PRD 109, 123511). No blocking error found, but please run a final consistency check.
Required fix: Verify bibliographic consistency in production.

P2-m5 (DBI discussion scope; Sec. IV p. 10)
Problem: The brief DBI aside is not necessary in the SPHEREx local‑template forecast section and interrupts flow.
Required fix: Move DBI aside to Discussion or an appendix.

NIT

P2-n1 (Hyphenation and em dashes)
Some overuse of em dashes and stacked parentheses; stylistic. Consider tightening.
P2-n2 (“bookkeeping”)
The term “bookkeeping” is used very frequently; consider varying language for readability.

Abstract‑last drift sweep
I re‑checked each abstract claim against the body:
- r range [0.829, 0.876] and rcos > 0.97: supported (Sec. III.B, Sec. II).
- 5.2–5.5σ template‑corrected and 2.6–5.5σ “realistic” envelope: supported, but must be re‑labeled per P2‑E5.
- SDB Fisher degradation 2.0–4.6×: supported by Sec. IX.D numbers (1.53→3.08→7.06).
- Bayes factors (≈9 recommended, ≈14 delta): supported by Sec. VI/Table II after applying the r = 0.84 σeff rebooking; please adopt a single primary set as per P2‑E4.
- Factor‑of‑two audit (−2 Im): Appendix A is consistent and equations are dimensionally consistent.

Stand‑alone reader test
The paper is largely stand‑alone. However, several load‑bearing results hinge on the external Heinrich et al. σ(fNL) = 0.7 (clearly stated as an import) and on code artifacts (which must be fixed per P2‑E1/E3).

Recommended maximum length
Given that this is explicitly a sensitivity recast anchored to an external σ(fNL), a ≤18‑page main text (with appendices for Bayes‑factor algebra, null‑space scans, and operator‑algebra details) would suffice. Much of the repetition in Secs. IV–VII could be compressed.

## Summary recommendation
MAJOR REVISIONS

The manuscript is careful and numerically consistent in most of its claims, with many caveats given. However, for PRD standards the reproducibility/provenance issues (missing DOI/commit hash and extensive main‑text reliance on internal file names), the mixing of σ definitions without consistent local qualifiers, and the labeling of the σGR‑driven lower envelopes as “realistic” without a SPHEREx‑bispectrum calibration must be fixed. Clarify the primary estimator/procedure and present a single recommended significance and Bayes‑factor line keyed to one well‑defined bookkeeping choice, with all else as sensitivity checks. Once these essential and major issues are addressed and the paper is condensed, the manuscript could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes audit)

ESSENTIAL

P2-E6 (Dimensional consistency and unit conventions; Eqs. (3)–(4), Sec. III.A p. 7)
Problem: M(k, z) = 2 k^2 T(k) D(z) / [3 Ωm H0^2] is written with k “quoted in h Mpc−1 throughout,” but H0 is not given in commensurate units, and no c = 1 convention is stated. As written, Eq. (3)–(4) mix comoving k in h Mpc−1 with H0 in s−1 (or km s−1 Mpc−1), which leaves ∆b(k, z) dimensionally ambiguous.
Required fix: State the unit convention explicitly (e.g., c = 1, H0 in h Mpc−1 units) or include the missing c−2 factor so that M(k, z) is dimensionless. Alternatively, define M(k, z) in the commonly used normalized form M(k, z) ≡ 2 k^2 T(k) D(z) / [3 Ωm H0^2] with k and H0 both in h Mpc−1 units, and say so. Ensure that every downstream use of Eqs. (3)–(4) is consistent with this convention.

P2-E7 (Stale/inconsistent CMB-Fisher overlap value r; abstract vs. body)
Problem: Two different “signal-only CMB-Fisher” overlaps appear: r = 0.876 (abstract; Sec. III.B p. 9) and r = 0.878 ± 0.012 (Sec. III.B p. 9). The abstract headlines r = 0.876; the body later quotes 0.878 ± 0.012 “stable across ℓref.”
Required fix: Choose a single value and uncertainty (with the exact ℓ-range/noise model), use it consistently in the abstract and main text, and update any dependent numbers if needed.

P2-E8 (Unsupported mission timeline in abstract; p. 1)
Problem: The abstract states “SPHEREx (launched March 2025, primary survey through ∼2027, first PNG-suitable release expected ∼2028)” without a citation.
Required fix: Cite an official SPHEREx mission document (NASA/Caltech/JPL) for launch/operations milestones and expected data-release schedule, or soften/remove the dates.

MAJOR

P2-M8 (Figure 2 category definitions; p. 11)
Problem: The MegaMapper bars labeled “conservative” and “single-tracer” are shown, but those terms are not precisely defined in the caption or tied to explicit assumptions in Sec. V (e.g., what σ, which priors, what redshift/number density).
Required fix: Define each bar’s inputs in the caption (σ used, priors, redshift range, tracer model, whether bϕ and GR are included and how). Alternatively, add a pointer to a short table in Sec. V or the Supplement that lists these inputs.

P2-M9 (Anomaly-selected tracers 10–20% improvement claim; Sec. IV p. 10–11)
Problem: The text states a “preliminary Fisher forecast … projects a ∼10–20% improvement” from anomaly-selected tracers, but no methodology, inputs, or figure/table are provided; only a later shot-noise caveat is discussed.
Required fix: Provide the forecasting setup (n̄, b1, z-distribution, window, noise model) and a quantitative result (e.g., a small table), or move this to a non-quantitative Discussion remark without percentages.

P2-M10 (Appendix A symmetry factor usage; Eq. (A7), p. 27)
Problem: Eq. (A7) introduces a symmetry factor Sv and then divides by Sv (Bζ = −2 Im Σv Σσ [1/Sv Iv]). It is unclear whether Sv is defined as a multiplicity to divide out or a count already absorbed in Iv; the text does not justify the 1/Sv placement.
Required fix: Clarify the definition of Sv and show (or cite) the standard derivation that fixes whether it multiplies or divides each vertex contribution. A one-line explanation (or reference to Maldacena 2003 conventions) will suffice.

P2-M11 (Heuristic covariance scaling used quantitatively; Eq. (7), Sec. IV p. 10)
Problem: The text concludes “δσ/σ ≲ 5×10−4” using the primordial-field ζ scaling δC/C ∼ fNL^2 Δζ^2 / Nmodes(k). It immediately notes this is not a galaxy-field covariance, but still quotes a precise numerical bound that is then used to justify not recomputing the Fisher matrix at the bounce fiducial.
Required fix: Recast this as a back-of-the-envelope check without a numerical bound (or provide a corresponding galaxy-bispectrum covariance scaling or literature reference that justifies the numerical size). Do not present ≲ 5×10−4 as a quantitative bound without galaxy-field support.

P2-M12 (Shape-cosine generalization; abstract vs. body)
Problem: The abstract states “shape cosine rcos > 0.97 for all samples.” In Sec. II (pp. 4–5) the radius-50 scan gives rcos = 0.985 ± 0.007 (> 0.97), but the multi-radius convergence test only guarantees rcos > 0.95 for radii 10–500.
Required fix: Clarify in the abstract that rcos > 0.97 applies to the radius-50 scan used for the headline distribution; if claiming “for all samples,” restrict “samples” to that scan. Otherwise, state the conservative multi-radius floor rcos > 0.95.

MINOR

P2-m6 (Index/ratio notation consistency; Sec. II vs. Fig. 1)
Problem: Sec. II uses x3 ≡ k3/k1 for the squeeze ratio (with k3 the long mode in the scan), while Fig. 1’s x-axis is k1/k (with k1 → 0 as the long mode). This can confuse readers about which index carries the long mode.
Required fix: Add a brief note in the Fig. 1 caption that the long-mode index differs from the scan convention in Sec. II, and that the result is permutation-invariant.

P2-m7 (σGR units/interpretation; Secs. IV, VII, Tables III–IV)
Problem: σGR is used as an additive-in-quadrature nuisance in “fNL units,” but this is not stated explicitly.
Required fix: Add a one-line statement that σGR is treated as an effective additional 1σ uncertainty in the fNL estimator (i.e., in fNL units), added in quadrature to σ(fNL), and does not arise from a bispectrum Fisher.

P2-m8 (Definition of “H0” units; Sec. III.A)
Problem: H0 appears without specifying whether it is H0 = 100 h km s−1 Mpc−1 or H0/h in Mpc−1. This is entangled with P2-E6 but is a readability issue on its own.
Required fix: State explicitly which H0 convention is used when writing M(k, z).

P2-m9 (Citations for mission timelines and survey specifics; scattered)
Problem: A few schedule/scope statements (SPHEREx data release timing; MegaMapper instrument status) are unreferenced.
Required fix: Add citations (e.g., SPHEREx Overview white paper; MegaMapper concept paper arXiv:2209.04322) where these statements first appear.

J. STALE NUMBERS

P2-J1 (Consistent reporting of rCMB across the manuscript)
Problem: rCMB is quoted as 0.876 (abstract; multiple places) and 0.878 ± 0.012 (Sec. III.B). While consistent within 0.2%, PRD production benefits from a single canonical number and uncertainty.
Required fix: Harmonize to one value and propagate it consistently (including Fig. 2 labels if applicable).

NO OTHER NEW FINDINGS

Rationale: All additional classes requested (A–J) were checked. The initial review already covered the big comparability/provenance issues (mixed σ definitions, BF bookkeeping, missing DOI/commit hash, reliance on internal filenames, σGR labeling). The fresh-eyes pass mainly uncovered (i) dimensional/units clarity around M(k, z), (ii) minor stale/inconsistent rCMB values, (iii) figure-category definitions, (iv) a quantitative use of a heuristic covariance estimate, and (v) a few unsupported timeline/percentage statements.