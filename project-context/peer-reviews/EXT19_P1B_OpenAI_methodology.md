# P1B EXT19 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=135fdfb4 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6656 chars)
**Wall time**: 368.4s

---

Referee report (PRD methodology)

Overall scope and mandate
- I reviewed the entire 21‑page manuscript including abstract, body text, equations, figures, tables, footnotes, and appendices.
- Focus: methodological rigor (statistical validity, estimator definitions, dimensional analysis, internal arithmetic, error propagation, consistency of quoted σ values and null procedures), traceability of every quantitative claim, figure/table integrity, and reproducibility claims.

Findings are classified as ESSENTIAL, MAJOR, MINOR, or NIT. Page numbers refer to the rendered PDF pages (1–21). Each item cites the exact location/wording, the problem, and the required fix.

ESSENTIAL

P1B-E1 (Sec. VI, pp. 12–13): Ωa computation in the frozen (non‑oscillating) regime is unspecified
- Text: “Energy density today.—Once oscillating (z ≪ zosc), the ALP cycle-averaged energy density redshifts as matter: ρa(z) = ρa(zosc)[(1+z)/(1+zosc)]^3 … The dark-energy fraction today is therefore Ωa ≈ m_a^2 f_a^2 [1 − cos(θi)] / [ρcrit,0 (1+zosc)^3]. … At each MCMC step the ALP module receives (ma, θi), solves Eq. (7) for zosc, and evaluates Eq. (9).”
- Problem: Eq. (9) is only valid once the field has started oscillating (zosc > 0). For zosc ≤ 0 (the “frozen” regime) ρa(z=0) ≈ V(θi) and there is no matter‑like dilution factor. As written, the method implies Eq. (9) is applied uniformly; if applied with zosc < 0 it would spuriously amplify ρa by (1+zosc)^{-3}<1. Since the Ωa < 0.01 “spectator‑safe” classification is used repeatedly (abstract, conclusions, Table IV), correctness of the frozen/oscillating branch is load‑bearing.
- Required fix: Explicitly state and implement a branch: if zosc ≤ 0, set ρa(z=0)=V(θi) (no dilution). If zosc > 0, use Eq. (9). Provide a numerical validation example comparing the pipeline’s Ωa against a direct EOM integration for a representative frozen case (e.g., ma = 0.3 H0, θi = 0.5) and an oscillating case (e.g., ma = 10 H0, θi = 0.5), reporting fractional agreement at the ≤ few‑percent level. If this branch was already implemented, state it explicitly and point to the archived code line(s).

P1B-E2 (Sec. VI, p. 13, “Axion potential.”): Incorrect order of anharmonic correction
- Text: “For θi ∼ O(1) anharmonic corrections enter at O(θi^2/6).”
- Problem: Expansion is 1 − cos θ = θ^2/2 − θ^4/24 + …; the relative correction to the quadratic term is −θ^2/12, not O(θ^2/6). The stated order is wrong by a factor of two (and signless).
- Required fix: Correct to: “For small θi, 1 − cos θi = θi^2/2 − θi^4/24 + …, so the leading relative anharmonic correction to the quadratic approximation is −θi^2/12.” If an anharmonic rescaling is used anywhere in the chains, document it.

P1B-E3 (Data availability, p. 15; Appendix A, pp. 15–16): No archived DOI for key datasets/artifacts
- Text: “HuggingFace datasets … DOI assignment is pending (identifiers will be inserted at submission).”
- Problem: PRD requires durable archival for reproducibility. “Pending” DOI is insufficient at acceptance.
- Required fix: Deposit all load‑bearing artifacts (frozen chains, NaMaster MC outputs, ALP chains) to an archival repository with DOI (e.g., Zenodo) and provide the fixed DOIs in the manuscript. The DOI(s) must correspond to the exact version used (commit b22f8cc9, v1B.0.73), with checksums.

MAJOR

P1B-M1 (Sec. IV, pp. 6–9; many places): Estimator definition is sound but per‑realization SNR and angle‑recovery ratio are loosely defined
- Text: Footnote 4 and surrounding text define SNRtmpl but then state “per‑realization angle‑recovery ratio β/σ̂β … is 5.2,” evidently using |β̂| rather than βinj in the numerator at fsky = 0.32.
- Problem: Ambiguity in “β” vs “β̂” in the ratio and whether σβ is per‑realization or across realizations makes it hard to reproduce the exact 5.2 figure without opening the artifacts. Since SNR language appears next to sky‑measurement σ’s elsewhere (though you do caution they are not comparable), clarity here matters.
- Required fix: Replace “β/σ̂β” by an explicit definition, e.g., “|β̂|/σβ, where |β̂| is the recovered (biased) angle for that realization and σβ is the across‑realization standard deviation of β̂.” Provide the numeric: 0.238°/0.046° = 5.17 (rounded to 5.2). Also state the alternative using βinj (0.27°/0.046° = 5.9) to avoid confusion.

P1B-M2 (Sec. IV, pp. 7–9): Table/Figure consistency and bias attribution need one consolidated quantitative summary
- Text: Bias is discussed across caption, text, and footnote; worst‑case |Δβ̂| = 0.040°, multiplicative under‑recovery ≈ 12%, dominant source is unweighted fit, BB shape secondary.
- Problem: The narrative is split; the reader must piece together multiple artifacts and sentences to understand the estimator‑induced bias. For a methods paper, a single table summarizing bias under each robustness configuration (canonical, inverse‑variance weighting, CAMB BB, purification, mask variations) with numbers would remove ambiguity.
- Required fix: Add a small table (or a single compact paragraph with a bullet list) reporting βinj, β̂, Δβ̂ for each configuration (including inv‑var fit: β̂ = 0.264°, Δβ̂ = −0.006°; CAMB BB injected: 0.251°, etc.). This is a presentation fix but important for methodological clarity.

P1B-M3 (Sec. V.C, p. 10; Table II, p. 20): Release‑pairing robustness for w0wa chain is untested
- Text: “The iter2 chain uses planck 2018 lensing.native in place of planck 2018 lensing.clik … a dedicated release‑pairing swap test … has not been performed and is left to a post‑submission follow-up.”
- Problem: You provide an excellent PR4/2018 pairing test for the ΛCDM+∆Neff proxy but not for the w0wa chain, where the headline posterior distances (+4.3σ in w0, −3.6σ in wa) are emphasized. At minimum, a consistency check that these large departures are not an artifact of the particular lensing likelihood backend is required before publication.
- Required fix: Run a focused w0wa chain swapping planck 2018 lensing.native for planck 2018 lensing.clik (and, ideally, PR4‑consistent planckpr4lensing) and report the shifts in (w0, wa, wpivot). If not feasible in time, explicitly down‑scope and move the w0wa claims to an appendix, or temper the language further and add a boldfaced limitation at first mention that these posteriors have not been tested for Planck‑lensing likelihood backend sensitivity.

P1B-M4 (Table IV, p. 21; Sec. VI pp. 12–14): Ambiguity in “m/H0 (Caγ = 8) 4.7/37.7/264” entries
- Text: Table IV “m/H0 (Caγ = 8) 4.7/37.7/264”, “θi 0.22/0.41/0.70”, “Caγ 14.2/26.2/46.4”.
- Problem: It is not stated whether these are 16/50/84 percentiles, [min/median/max], or something else. Elsewhere you state “median ≃ 36 H0,” but the table suggests triplets throughout. This ambiguity undermines interpretability.
- Required fix: Label each triplet unambiguously (e.g., “16/50/84 percentiles”) in the table header/footnote and ensure consistency for all columns.

P1B-M5 (Sec. IV, pp. 6–9): Excessive in‑line code paths in the main text
- Text: Many explicit file paths, script names, and line numbers are embedded in the main text (e.g., “namaster_500mc.py L223”, “reproducibility/p1_namaster_500mc/scripts/...”, “pod run pipelines/.../summary.json”).
- Problem: While excellent for reproducibility, PRD prefers such implementation detail in a Reproducibility/Code appendix or data‑availability section. Embedding file paths in the main flow hinders readability and will stale quickly.
- Required fix: Move all file‑path and line‑number references to Appendix A (or a dedicated Reproducibility appendix) and keep the main text to scientific content (estimator definition, assumptions, and numerical outcomes). Leave a brief pointer in Sec. IV to the appendix for full implementation details.

MINOR

P1B-m1 (Abstract p. 1; Sec. IV, pp. 6–9): Keep null‑procedure σ’s segregated at every juxtaposition
- Text: The manuscript is generally careful (e.g., “naive 3.9σ upper bound” vs. “published 3.6σ”), and repeatedly states the MC‑pipeline SNR is not a sky significance. In a few places, the SNR numbers (20.32, 25.71) appear near the 2.7–2.9σ sky results without repetition of the “not comparable” caveat in the same sentence/paragraph.
- Required fix: Wherever SNRtmpl figures and sky σ’s appear in the same paragraph, add a short parenthetical “(pipeline SNR; not a sky significance)” to prevent any inadvertent conflation by readers.

P1B-m2 (Sec. III, pp. 3–5): Internal process artifacts in footnote 1
- Text: References to COUNT_EXPLANATION.md, getdist ignore_rows, and per‑chain rounding details.
- Problem: Overly detailed internal bookkeeping in the body footnotes reduces clarity.
- Required fix: Move this footnote to Appendix A (or summarize in one sentence that 30% burn‑in was applied uniformly; detailed reconciliation is archived).

P1B-m3 (Sec. VI, p. 12): αEM/(4π) convention statement
- Text: “The αEM/(4π) prefactor is convention‑dependent … here it corresponds to L ⊃ −(gaγ/4) ϕ F F̃ with gaγ = Caγ αEM/(2π fa) and β = (gaγ/2) Δϕ.”
- Problem: Correct and consistent, but add a one‑line cross‑check: plugging αEM = 1/137.036 and Δϕ/fa = 1.0601 gives β ≈ 0.282° to confirm Eq. (4) numerically within the text (you already do this computation—consider keeping only one numeric line to avoid redundancy).

P1B-m4 (Sec. II, p. 2; Sec. III, p. 4): “predicts ∆Neff ≈ 0 by construction”
- Text: “… minimal matter‑bounce class … predicts ∆Neff ≈ 0 by construction.”
- Problem: Fine as context but, for a methods companion, add a parenthetical citation or a brief one‑line derivation reference explaining that no light bounce‑internal species are thermalized at recombination in that minimal class.

P1B-m5 (Tables I–III, pp. 19–20): Units and derived‑parameter definitions
- Text: S8 definition is given; units on H0 consistent.
- Problem: Consider adding a one‑line reminder that S8 is computed as a derived parameter inside Cobaya per S8 = σ8 (Ωm/0.3)^{1/2} to match the precise code definition (you did this in Table I’s caption—ensure it is present in all reader‑facing places where S8 is central).

NIT

P1B-n1 (Throughout): Stylistic density and length
- The paper is dense and heavy with caveats. This is appreciated for rigor, but some of the verbosity (especially long footnotes and in‑line path references) could be trimmed or moved to appendices to streamline the narrative.
- Recommended max length: 17–18 pages for the main text, with the reproducibility specifics consolidated in appendices.

P1B-n2 (Sec. V, p. 10): “40,349 raw rows, 107,853 effective weight”
- The effective weight exceeding raw rows can be confusing to some readers. Consider adding one clause explaining how effective samples are computed from autocorrelation times across combined chains.

Arithmetic and consistency checks performed

- H0 tension (67.68 ± 1.06 vs 73.04 ± 1.04) → Δ = 5.36; σcomb = 1.485; 3.61σ (your “∼3.6σ” is accurate).
- S8 tension (0.8245 ± 0.0089 vs 0.776 ± 0.017) → Δ = 0.0485; σcomb = 0.0192; 2.53σ (you quote 2.6σ—consistent with rounding).
- wpivot derivation: Cov(w0, wa) = −0.00729; Var(wa) = 0.03474 → 1 − ap = 0.210; ap = 0.790; zp = 0.266; wpivot = −0.952 ± 0.019 (all match).
- Phantom crossing: (−1 − w0)/wa = −0.1878/(−0.6666) = 0.282; z× ≈ 0.39 (matches).
- β from ALP displacement: (αEM/(4π)) × Caγ × Δϕ/fa = 5.81e−4 × 8 × 1.0601 = 4.93e−3 rad = 0.282° (matches).
- βobs combination (Planck+ACT, naive uncorrelated): 0.241° ± 0.061°; significance 3.9σ—correctly labeled as an optimistic upper bound.
- βobs vs LiteBIRD σ forecast: Δ = 0.072°; σcomb = sqrt(0.03^2 + 0.094^2) = 0.0987°; 0.73σ—matches your 0.7σ statement.
- ρcrit,0 = 3 H0^2 MPl^2: with H0 ≃ 1.44×10^−33 eV, MPl = 2.44×10^27 eV → 3.7×10^−11 eV^4 (as quoted).
- Pixel RMS noise: Nside = 512 → Ωpix ≈ 47.3 arcmin^2 → σpix = 10/√Ωpix ≈ 1.455 μK (matches).
- Multiplicative under‑recovery of β: 0.238/0.270 ≈ 0.882; 0.302/0.342 ≈ 0.883 → ~12% under‑recovery (consistent).

Figures and tables

- Fig. 1–2: Axis labels and units are clear; values consistent with Table I.
- Fig. 3: Axes labeled in degrees; sky‑fraction sweep bars appropriately described; lack of σβ for fsky = 0.32 acknowledged and later measured (0.046°). Consider adding that measured σβ number directly to the caption for completeness.
- Fig. 4: Triangle plot is informative; prior ranges clearly stated in text. Table IV needs quantile labeling (MAJOR).
- Table I–III: Internally consistent; the two‑Gaussian combination in Table I (S8) reproduces your stated fused value within rounding.

Stand‑alone reader test

- The paper is mostly self‑contained for methods. Where cross‑paper theoretical context is cited (Paper I(a)), it is not required to follow the methods here. Good.

Abstract–body consistency check (pattern‑045)

- Abstract claims on ∆Neff, H0, β̂ pipeline bias, and ALP consistency are all supported in‑body with numbers and caveats. The statement that the ALP result is not an ECH‑distinctive prediction is appropriately repeated in Sec. VI and the conclusions. The only required abstract‑level amendment is to ensure that the Ωa spectator criterion and its computation are unambiguously correct for both frozen and oscillating regimes (see P1B‑E1).

Provenance surfaces (patterns 046/047)

- Versioning is explicit (v1B.0.73, commit b22f8cc9). Good. However, DOIs are “pending” (ESSENTIAL to resolve before acceptance).

Uncomputed quantitative claims (pattern‑048)

- Most “robust/insensitive” statements are backed by a numeric robustness battery. After moving details to an appendix, keep a concise numerical summary in the main text (P1B‑M2).

Effect sizes

- For w0wa, you provide a note that H(z=0.5) differs by ≈ +1.7%. Good to include one sentence interpreting that effect size where the σ distances are reported.

## Summary recommendation
MAJOR REVISIONS

The paper is careful, numerically consistent, and commendably transparent. However, before PRD acceptance as a methods companion, the authors must (1) explicitly handle and document the Ωa computation in the frozen regime (zosc ≤ 0), correcting a potential misapplication of the dilution factor; (2) correct the stated order of anharmonic corrections; (3) provide archival DOIs for all frozen artifacts; (4) clarify ambiguous triplets in Table IV; and (5) perform or sharply down‑scope the w0wa release‑pairing robustness test. Several presentation and clarity fixes (estimator/SNR definitions; consolidating the bias summary; relocating file‑path details) are also requested. With these addressed, the manuscript would meet PRD’s high methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second pass)

ESSENTIAL

NO NEW ESSENTIAL ITEMS FOUND
- I re-checked all equations for dimensions, all arithmetic quoted in the abstract and conclusions, and the most load‑bearing numerical chains. Aside from the already‑flagged Ωa frozen‑regime branch (P1B‑E1) and the anharmonic‑order fix (P1B‑E2), I did not find additional essential errors that would invalidate a headline conclusion.

MAJOR

P1B-M6 (Table IV, p. 21): Mislabeling of the “m/H0 (Caγ = 8)” column in a Caγ-free chain
- Text: Table IV header reads “m/H0 (Caγ = 8)” while the table is explicitly a “Restricted‑posterior readout of the continuous‑prior c5_continuous chain” where Caγ is sampled freely.
- Problem: The parenthetical “(Caγ = 8)” is incorrect for this table and implies the mass summary was taken from a fixed‑coupling slice, which it was not. This can mislead readers (e.g., the Ωa ≤ 0.01 line lists 6.0/40.5/238 for m/H0 together with a Caγ triplet 29.9/43.3/54.1 that clearly shows Caγ was free).
- Required fix: Correct the column header to “m/H0” (no parenthetical) and add an explicit table footnote: “All columns are computed from the Caγ‑free c5_continuous chain; entries are 16/50/84 percentiles.” Ensure the same labeling appears consistently where the 40.5 H0 median is discussed in the text.

P1B-M7 (Sec. IV, pp. 7–8): “χ2” nomenclature suggests a weighted, statistically interpretable chi‑square, but the fit is unweighted
- Text: “The estimator minimises χ2(β) = Σb [ CEB,decoupled
b − ½ sin(4β) CEE,tmpl
b ]2 … the fit is unweighted — all bins carry equal weight regardless of their noise level.”
- Problem: Calling the objective “χ2” implies variance weighting and a statistical interpretation of Δχ2, which do not hold here. You do later show that moving to inverse‑variance weighting removes most of the bias; that further underlines that the current ‘χ2’ is not a chi‑square.
- Required fix: Rename the objective to “unweighted least‑squares objective” throughout Sec. IV and the caption(s), or explicitly write “unweighted χ2 (not a statistical chi‑square)”. Add one sentence clarifying that no Δχ2 significance is inferred from this objective.

P1B-M8 (Sec. III, caveat (e), pp. 4–5; Sec. V.C, p. 10; Table II, p. 20): SN overlap not quantified in‑paper while large |w0|, |wa| tail distances are emphasized
- Text: You note the ∼20% DES‑SN5YR × Pantheon+ overlap and state two control chains exist “as a separate follow‑up note.”
- Problem: The paper repeatedly quotes +4.3σ (w0) and −3.6σ (wa) marginalized distances. Given the known overlap and the absence of a joint SN covariance, PRD readers need at least a minimal, in‑paper sensitivity quantification.
- Required fix: Add a short control test to the manuscript (main text or appendix): re‑run with each SN catalog alone (DES‑Y5 only; Pantheon+ only) on the same stack and report the shifts in (w0, wa, wpivot). If compute time prevents this, demote the w0wa claims to an appendix and add a boldface limitation the first time those σ distances are mentioned: “These posterior distances have not been corrected for DES‑SN5YR × Pantheon+ overlap; quantitative sensitivity to SN overlap is not included here.”

MINOR

P1B-m6 (Sec. IV, p. 8; Fig. 3 caption, p. 7): Report the standard error of the 500‑MC mean numerically
- Text: “The standard error of the 500‑realization mean is smaller by √N = 22.4.”
- Problem: Readers must compute the number themselves.
- Required fix: State σβ/√N explicitly at fsky = 0.32: 0.046°/√500 = 0.0021°. Consider also inserting “σβ = 0.046° (measured in the dedicated rerun)” directly in the Fig. 3 caption for completeness.

P1B-m7 (Sec. VI vs Conclusions; pp. 12–15): Clarify which chain/subset each quoted median m refers to
- Text: Sec. VI: “median m ≈ 36 H0” (fixed Caγ = 8). Conclusions: “median m ≃ 40.5 H0” (Ωa ≤ 0.01 subset of the Caγ‑free chain).
- Problem: Both numbers are correct but refer to different analyses; this can read as an inconsistency.
- Required fix: Each time a median mass is quoted, append the parenthetical context: “(fixed‑Caγ = 8 chain)” or “(Caγ‑free chain, Ωa ≤ 0.01 subset)”.

P1B-m8 (Sec. IV, p. 7; Footnote 4 usage across text): Keep “pipeline SNR” label attached wherever SNRtmpl appears without nearby sky σ discussion
- Text: Some SNRtmpl mentions (e.g., “template‑fit SNR = 25.71”) appear in paragraphs that do not simultaneously reiterate “not a sky significance.”
- Problem: Although you state this clearly elsewhere, scattering SNR values can still be misread.
- Required fix: Append “(pipeline SNR; not a sky significance)” the first time SNRtmpl is mentioned in any paragraph that lacks an adjacent reminder.

NIT

P1B-n3 (Sec. V, p. 10): Briefly explain “effective weight” exceeding raw rows
- Text: “40,349 raw rows, 28,245 post‑burn‑in … 107,853 effective weight.”
- Problem: Some readers may be puzzled by ESS > Nrows due to multi‑chain weight aggregation and thinning.
- Required fix: One clause: “The ‘effective weight’ is the GetDist effective sample size computed from integrated autocorrelation times over weight‑expanded, combined chains; it can exceed per‑chain raw rows.”

Arithmetic audit spot checks (new)
- βcombined (Planck+ACT, Eq. 5): weights 1/0.11^2 and 1/0.074^2 give 0.2415° ± 0.0614°; matches 0.241° ± 0.061° (rounding).
- SNR scaling with βinj: SNRtmpl(0.342°) ≈ SNRtmpl(0.27°) × [sin(4×0.342°)/sin(4×0.27°)] ≈ 20.32 × 1.265 ≈ 25.7; matches 25.71.
- fsky scaling of σβ: 0.046° × √(0.32/0.85) = 0.0283° (vs 0.029° reported) and × √(0.32/0.65) = 0.0322° (vs 0.033°), consistent.

Figure–text consistency (new)
- Fig. 3 caption numbers (σβ = 0.029° at fsky = 0.85; 0.033° at 0.65) match the body text. Suggest adding the measured σβ = 0.046° for fsky = 0.32 in the caption for completeness (P1B‑m6).

Equation dimensional checks (new)
- Eqs. (6)–(9): dimensions consistent in natural units. The already‑flagged frozen‑regime branch (P1B‑E1) remains the only methodological hazard here.

Internal cross‑references (new)
- Eq. (1), (5) citations map correctly; Sec. V “Release‑pairing note” indeed contains the PR4/2018 pairing discussion for the ΛCDM+ΔNeff proxy. No broken or mismatched refs found.

Abstract faithfulness (new)
- All abstract statements trace to the body. The only caveat remains the Ωa spectator criterion implementation (P1B‑E1), which you should fix and then echo in the abstract as already requested.

NO OTHER ADDITIONAL FINDINGS
- Beyond the items above, the remaining σ’s, ratios, and pivot calculations checked out on recomputation; figure axes/units match the body text; and the remaining null‑procedure juxtapositions carry adequate “not comparable” qualifiers.